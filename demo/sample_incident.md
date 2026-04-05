# Incident: Checkout service instability after rollout

## Symptoms
- Elevated p95 latency
- Frequent pod restarts
- HPA oscillation
- Increased 5xx responses

## Timeline
- 10:02 UTC: Helm change merged
- 10:05 UTC: Deployment rolled out
- 10:07 UTC: CPU usage spikes
- 10:08 UTC: HPA begins scaling up and down
- 10:10 UTC: Error rate increases

## Suspected cause
CPU request lowered in Helm values, causing unstable autoscaling behavior under burst load.
