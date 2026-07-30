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
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-07-28'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fraugster-domain-security.yml
- group: company
  title: ''
  type: Website
  url: http://fraugster.com
created: '2026-07-17'
description: Fraugster is a Berlin-based artificial intelligence company focused on payment fraud prevention and transaction risk scoring for online merchants, payment service providers, and acquirers. Its machine-learning platform was designed to analyze payments in real time to detect and block fraudulent transactions while reducing false declines and chargebacks. The company was surfaced through venture portfolio data (backed by Seedcamp) and added to the API Evangelist network. During this enrichment pass the company's public developer surface was not reachable to automated clients (the primary domain returns HTTP 403), so no API specifications, SDKs, or documentation could be harvested; only live infrastructure/domain-security signals were probed.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/fraugster.png
layout: provider
modified: '2026-07-19'
name: Fraugster
nav: Providers
network: true
overview: Fraugster is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fraud Prevention, Payments, Machine Learning, and Artificial Intelligence.
random_paper: 77
score:
  band: minimal
  composite: 5.7
  delta: -2.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 7.7
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 9.4
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/fraugster/refs/heads/main/screenshots/fraugster-2026-07-25T215134.png
security:
- kind: domain-security
  name: Fraugster Domain Security
  slug: fraugster-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: fraugster
tags:
- Company
- Fraud Prevention
- Payments
- Machine Learning
- Artificial Intelligence
- Risk Management
- Security
website: http://fraugster.com
---
