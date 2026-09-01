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
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/donkey-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://donkey.trade
- group: commercial
  title: ''
  type: TermsOfService
  url: https://donkey.trade/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://donkey.trade/privacy
created: '2026-07-17'
description: Donkey is an AI-native trading company (Y Combinator, Summer 2026) that buys directly from Chinese factories and sells delivered duty-paid to US importers. Donkey mines public US customs records to identify the factory that actually makes a product, returns a landed DDP quote within 72 hours, runs its own on-the-floor quality inspections before the factory is paid, clears customs, moves the money, and offers credit-insured net-45 terms to qualified buyers. Founded by Benjamin Martindale (CEO) and Minghao Tan (CTO), the company runs small teams in San Francisco and China. Donkey publishes no public API, SDK, or developer platform today; this profile tracks its company identity in the API Evangelist network.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/donkey.png
layout: provider
modified: '2026-07-18'
name: Donkey
nav: Providers
network: true
overview: Donkey is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Trading, Logistics, Supply Chain, and Manufacturing.
random_paper: 20
score:
  band: minimal
  composite: 7.4
  coverage:
    artifact_dirs: 2
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 7.4
  regulatory:
    applies: true
    matched_via: weak_tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 23.3
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/donkey/refs/heads/main/screenshots/donkey-2026-07-25T212249.png
security:
- kind: domain-security
  name: Donkey Domain Security
  slug: donkey-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: donkey
tags:
- Company
- Trading
- Logistics
- Supply Chain
- Manufacturing
- Import
- Customs
- Cross-Border
- Y Combinator
- Artificial Intelligence
website: https://donkey.trade
---
