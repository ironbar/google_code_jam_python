
import sys
import argparse
import math
import nest_asyncio
nest_asyncio.apply()
from playwright.sync_api import sync_playwright
from tqdm import tqdm
import pandas as pd


def main(args=None):
    if args is None:
        args = sys.argv[1:]
    args = parse_args(args)
    collect_participants_languages(args.csv_path, args.save_period)


def collect_participants_languages(csv_path, save_period):
    df = pd.read_csv(csv_path)
    if 'programming_language' not in df:
        df['programming_language'] = math.nan

    page = create_page()
    for idx, row in tqdm(df.iterrows(), total=len(df)):
        if isinstance(row['programming_language'], float):
            df.loc[idx, 'programming_language'] = get_programming_language(row['participant_url'], page)
            if idx % save_period == 0:
                df.to_csv(csv_path, index=False)
    df.to_csv(csv_path, index=False)


def create_page():
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context(viewport={ 'width': 1000, 'height': 950 })
    page = context.new_page()
    return page


def get_programming_language(participant_url, page):
    try:
        page.goto(participant_url)
        page.locator(".ranking-table__row-cell > p").first.wait_for(timeout=10000)
        programming_language = page.locator(".ranking-table__row-cell > p").first.all_inner_texts()
        if isinstance(programming_language, list):
            programming_language = programming_language[0]
        return programming_language
    except Exception as e:
        print(e)
        return math.nan


def parse_args(args):
    epilog = """
    python collect_participants_languages.py 0000000000877b42.csv
    """
    description = """
    Adds information regarding the programming language for each participant
    """
    parser = argparse.ArgumentParser(
        description=description,
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        epilog=epilog)
    parser.add_argument('csv_path', help='Path to the csv file with the information of the round')
    parser.add_argument('--save_period', default=10, type=int, help='Save the dataframe every n participants')
    return parser.parse_args(args)


if __name__ == '__main__':
    main()
