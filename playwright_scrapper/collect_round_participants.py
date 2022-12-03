
import os
import sys
import argparse
import time
import nest_asyncio
nest_asyncio.apply()
from playwright.sync_api import sync_playwright, TimeoutError
from bs4 import BeautifulSoup
from tqdm import trange
import pandas as pd


def main(args=None):
    if args is None:
        args = sys.argv[1:]
    args = parse_args(args)
    collect_round_participants(args.round_url)


def collect_round_participants(round_url):
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context(viewport={ 'width': 1000, 'height': 950 })
    page = context.new_page()
    page.goto(round_url)
    page.locator(".section-row-pane > div:nth-child(2) > div").first.wait_for(timeout=10000)
    page.get_by_role("button", name="OK").click()

    soup = BeautifulSoup(page.content(), 'html.parser')
    n_pages = int(soup.find('p', {'class': 'ranking-table-page-number-total-pages'}).get_text()[3:])
    name, participant_url, score, penalty_time = [], [], [], []
    for _ in trange(n_pages):
        soup = BeautifulSoup(page.content(), 'html.parser')
        for element in soup.find_all('div', {'class':'ranking-table__row-cell ranking-table__row-cell--left ranking-table__row-cell__displayname'}):
            name.append(element.find('p').get_text())
            participant_url.append('https://codingcompetitions.withgoogle.com' + element.find('a').get('href'))
        score.extend([int(element.get_text()) for element in soup.find_all('span', {'class':'user-total-score has-tooltip'})])
        penalty_time.extend([element.get_text().strip() for element in soup.find_all('span', {'class':'penalty-time has-tooltip'})])
        try:
            page.get_by_role("button", name="chevron_right").click()
            time.sleep(2)
        except TimeoutError:
            print('Could not click on next page')

    df = pd.DataFrame(dict(name=name, score=score, penalty_time=penalty_time, participant_url=participant_url))
    df.to_csv(f'{os.path.basename(round_url)}.csv', index=False)


def parse_args(args):
    epilog = """
    python collect_round_participants.py https://codingcompetitions.withgoogle.com/codejam/round/0000000000877b42
    """
    description = """
    Creates a csv with the general information of the participants along their urls. This can be later
    used to gather the programming language
    """
    parser = argparse.ArgumentParser(
        description=description,
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        epilog=epilog)
    parser.add_argument('round_url', help='Url of the round to extract participants, f.e. https://codingcompetitions.withgoogle.com/codejam/round/0000000000877b42')
    return parser.parse_args(args)


if __name__ == '__main__':
    main()
