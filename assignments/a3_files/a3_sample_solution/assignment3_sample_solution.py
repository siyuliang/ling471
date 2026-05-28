'''
Sample solution for Assignment 3.

Run as:
    python assignment3_sample_solution.py path/to/pos_dir path/to/neg_dir

Outputs exactly 5 numbers, one per line, rounded to 4 decimals:
    1. Overall accuracy
    2. Precision wrt positive reviews
    3. Recall    wrt positive reviews
    4. Precision wrt negative reviews
    5. Recall    wrt negative reviews
'''

import sys
import string
from pathlib import Path

from review_vector import reviewVec
from evaluation import computeAccuracy, computePrecisionRecall

POS_REVIEW = "POSITIVE"
NEG_REVIEW = "NEGATIVE"
NONE = "NONE"
POS = 'good'
NEG = 'bad'


def cleanFileContents(f):
    with open(f, 'r', encoding='utf-8') as fh:
        text = fh.read()
    for ch in string.punctuation:
        text = text.replace(ch, ' ')
    tokens = text.split()
    return ' '.join(tokens)


def countTokens(text):
    token_counts = {}
    for token in text.split(' '):
        if token in token_counts:
            token_counts[token] = token_counts[token] + 1
        else:
            token_counts[token] = 1
    return token_counts


def predictFromText(clean_text):
    counts = countTokens(clean_text)
    pos_count = 0
    neg_count = 0
    if POS in counts:
        pos_count = counts[POS]
    if NEG in counts:
        neg_count = counts[NEG]
    if pos_count > neg_count:
        return POS_REVIEW
    elif neg_count > pos_count:
        return NEG_REVIEW
    else:
        return NONE


def simplisticPrediction(filename):
    clean_text = cleanFileContents(filename)
    return predictFromText(clean_text)


def main(argv):
    pos_dir = argv[1]
    neg_dir = argv[2]

    reviews = []

    for path in Path(pos_dir).glob('*.txt'):
        text = cleanFileContents(path)
        reviews.append(reviewVec(text, POS_REVIEW))

    for path in Path(neg_dir).glob('*.txt'):
        text = cleanFileContents(path)
        reviews.append(reviewVec(text, NEG_REVIEW))

    predictions = []
    gold_labels = []
    for review in reviews:
        predictions.append(predictFromText(review.text))
        gold_labels.append(review.correct_label)

    accuracy, _ = computeAccuracy(predictions, gold_labels)
    pos_prec, pos_rec = computePrecisionRecall(predictions, gold_labels, POS_REVIEW)
    neg_prec, neg_rec = computePrecisionRecall(predictions, gold_labels, NEG_REVIEW)

    print(round(accuracy, 4))
    print(round(pos_prec, 4))
    print(round(pos_rec, 4))
    print(round(neg_prec, 4))
    print(round(neg_rec, 4))

if __name__ == "__main__":
    main(sys.argv)
