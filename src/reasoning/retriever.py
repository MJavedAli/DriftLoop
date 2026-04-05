def retrieve_context(session, service):
    changes = session.query("Change").all()
    metrics = session.query("Metric").all()
    return changes, metrics
