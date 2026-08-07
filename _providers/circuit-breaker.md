---
access_model:
  confidence: low
  generated: '2026-07-22'
  label: Unknown
  method: derived
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
api_count: 0
artifact_total: 0
created: '2025-01-01'
description: The Circuit Breaker is a stability pattern for distributed systems and API architectures that prevents cascading failure when a downstream service degrades. A breaker wraps a remote call and tracks failures against a threshold; when the threshold is exceeded the breaker "opens" and short-circuits subsequent calls (typically returning an error or fallback) without contacting the downstream service. After a cooldown the breaker enters a "half-open" probe state and either resets to "closed" on success or re-opens on failure. The pattern was popularized by Michael Nygard in *Release It!* and is now standard in resilient microservice and API gateway design.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/circuit-breaker.png
layout: provider
modified: '2026-04-23'
name: Circuit Breaker
nav: Providers
network: true
random_paper: 63
slug: circuit-breaker
tags:
- Circuit Breaker
- Distributed Systems
- Fault Tolerance
- Microservices
- Patterns
- Resilience
- Stability
---
