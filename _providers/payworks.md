---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-19'
api_count: 0
artifact_total: 0
created: '2026-07-17'
description: Payworks was a Munich-based payment-infrastructure company backed by Speedinvest, building a mobile point-of-sale (mPOS) payment-gateway platform that let acquirers, PSPs and ISVs turn commodity smartphones and tablets into card-accepting terminals via a developer SDK and gateway. It was acquired by Visa in 2019 and its technology was folded into Visa's acceptance/CyberSource stack, after which the independent Payworks brand was wound down. As of this enrichment pass the company operates no active independent public developer surface — its primary domains are dormant (payworks.com resolves to a parked AWS S3 redirect bucket with no website configuration; payworks.de is a domain-for-sale parking page) and no docs/developer/api subdomains resolve — so there is no live OpenAPI, SDK, or documentation surface to harvest into the network. This profile is retained as a historical Speedinvest portfolio record.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/payworks.png
layout: provider
modified: '2026-07-20'
name: Payworks
nav: Providers
network: true
overview: Payworks is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Payments, Point of Sale, Payment Gateway, and Fintech.
random_paper: 14
score:
  band: minimal
  composite: 0.1
  delta: -4.2
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
    - owner: catalog
      reason: never_enriched
  previous_composite: 4.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 0.0
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
slug: payworks
tags:
- Company
- Payments
- Point of Sale
- Payment Gateway
- Fintech
- mPOS
- Acquired
---
