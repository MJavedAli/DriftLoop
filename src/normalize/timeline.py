def build_timeline(changes, metrics):
    events = []
    for c in changes:
        events.append((c.timestamp, "change", c.summary))
    for m in metrics:
        events.append((m.timestamp, "metric", m.value))
    return sorted(events, key=lambda x: x[0])
