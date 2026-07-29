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
api_count: 1
apis:
- description: Authenticated API surface behind api.turquoise.health (returns HTTP 401 without credentials; no public OpenAPI or developer documentation is published). Exposes Turquoise Health price transparency and
  name: Turquoise Health API
  slug: turquoise-health-api
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/turquoise-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://turquoise.health
- group: company
  title: ''
  type: Blog
  url: https://turquoise.health/resources/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://turquoise.health/plans/providers
- group: start
  title: ''
  type: SignUp
  url: https://turquoise.health/request-a-demo
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/turquoisehealth
- group: build
  title: ''
  type: Packages
  url: packages/turquoise-packages.yml
created: '2026-07-17'
description: Turquoise Health is a healthcare price transparency company (backed by a16z) that runs a platform aggregating and normalizing hospital and payer machine-readable price transparency files, negotiated contract rates, and out-of-network pricing into searchable, benchmarked rate data and analytics. Its products span rate analysis and benchmarking, contract management, clear rates and data assets, healthcare transactions, out-of-network pricing, patient cost estimates / Good Faith Estimates, and price-transparency compliance tooling, serving providers, payers, life sciences, and employers.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/turquoise.png
layout: provider
modified: '2026-07-21'
name: Turquoise Health
nav: Providers
network: true
overview: 'Turquoise Health publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Price Transparency, Health Insurance, and Rate Data.


  Turquoise Health''s developer surface includes engineering blog, pricing, signup flow, and 4 more developer resources.'
random_paper: 49
score:
  band: minimal
  composite: 12.9
  delta: -1.9
  facets:
    commercial_clarity: 23.7
    contract_quality: 0.0
    developer_ergonomics: 2.2
    discoverability: 79.6
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 14.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: domain-security
  name: Turquoise Domain Security
  slug: turquoise-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
slug: turquoise
tags:
- Company
- Healthcare
- Price Transparency
- Health Insurance
- Rate Data
- Analytics
- Compliance
- Payer
- Provider
website: https://turquoise.health
---
