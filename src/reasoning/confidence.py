def score_confidence(events):
    return min(len(events) / 10, 1.0)
