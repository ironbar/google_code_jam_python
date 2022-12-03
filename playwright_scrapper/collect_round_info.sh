#! /bin/bash
# Example of use:
# bash collect_round_info.sh https://codingcompetitions.withgoogle.com/codejam/round/000000000087762e
ROUND_URL=$1
OUTPUT_PATH=$(basename ${ROUND_URL}).csv
echo "Collecting round info from ${ROUND_URL}..."
echo "Saving on ${OUTPUT_PATH}..."
if [ ! -f ${OUTPUT_PATH} ]
then
	conda run -n playwright --no-capture-output python collect_round_participants.py ${ROUND_URL}
fi
conda run -n playwright --no-capture-output python collect_participants_languages.py $(basename ${ROUND_URL}).csv