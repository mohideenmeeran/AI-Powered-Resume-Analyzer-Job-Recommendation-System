def precision_recall_f1(
    predicted: set,
    actual: set,
):
    if not predicted:
        precision = 0.0
    else:
        precision = len(predicted & actual) / len(predicted)

    if not actual:
        recall = 0.0
    else:
        recall = len(predicted & actual) / len(actual)

    if precision + recall == 0:
        f1 = 0.0
    else:
        f1 = (
            2 * precision * recall
            / (precision + recall)
        )

    return {
        "precision": round(precision, 4),
        "recall": round(recall, 4),
        "f1": round(f1, 4),
    }


def precision_at_k(
    recommended: list,
    relevant: set,
    k: int = 5,
) -> float:

    selected = recommended[:k]

    if not selected:
        return 0.0

    hits = sum(
        1
        for item in selected
        if item in relevant
    )

    return round(hits / len(selected), 4)