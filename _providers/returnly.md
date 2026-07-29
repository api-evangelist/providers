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
  url: security/returnly-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://returnly.com
created: '2026-07-17'
description: Returnly was a fintech-flavored e-commerce returns and exchanges platform (Returnly Green Returns, instant store credit, and return-shipping insurance) surfaced as a craft-ventures portfolio company. It was acquired by Affirm in 2021, and its returnly.com domain now permanently redirects to Loop Returns (www.loopreturns.com/returnly/); no independent Returnly developer portal, API reference, or API host resolves. An enrichment pass on 2026-07-20 found no surviving public API surface; only a live domain-security probe of the redirecting returnly.com domain was captured.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/returnly.png
layout: provider
modified: '2026-07-20'
name: Returnly
nav: Providers
network: true
overview: Returnly is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, E-commerce, Returns, and Exchanges.
random_paper: 10
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
security:
- kind: domain-security
  name: Returnly Domain Security
  slug: returnly-domain-security
  summary_line: TLSv1.3 · HSTS
slug: returnly
tags:
- Company
- Fintech
- E-commerce
- Returns
- Exchanges
- Payments
- Acquired
website: https://returnly.com
---
