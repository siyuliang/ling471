'''
Sample solution for evaluation.py.

Implements computeAccuracy and computePrecisionRecall.
NONE predictions count as mistakes: they are never true positives for
either class, and they suppress recall for the gold class they belong to.
'''


def computeAccuracy(predictions, gold_labels):
    assert len(predictions) == len(gold_labels)
    mistakes = []
    correct = 0
    index = 0
    for pred, gold in zip(predictions, gold_labels):
        if pred == gold:
            correct = correct + 1
        else:
            mistakes.append(index)
        index = index + 1
    if len(predictions) > 0:
        accuracy = correct / len(predictions)
    else:
        accuracy = 0.0
    return (accuracy, mistakes)


def computePrecisionRecall(predictions, gold_labels, relevant_class):
    assert len(predictions) == len(gold_labels)
    tp = 0
    fp = 0
    fn = 0
    for pred, gold in zip(predictions, gold_labels):
        if pred == relevant_class and gold == relevant_class:
            tp = tp + 1
        elif pred == relevant_class and gold != relevant_class:
            fp = fp + 1
        elif pred != relevant_class and gold == relevant_class:
            fn = fn + 1
    if (tp + fp) > 0:
        precision = tp / (tp + fp)
    else:
        precision = 0.0
    if (tp + fn) > 0:
        recall = tp / (tp + fn)
    else:
        recall = 0.0
    return (precision, recall)
