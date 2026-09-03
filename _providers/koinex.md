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
  scored_at: '2026-09-03'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/koinex-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://koinex.in/
created: '2026-07-17'
description: 'Koinex was an Indian digital-asset exchange launched in 2017, describing itself as India''s first and largest cryptocurrency exchange with more than one million users. It offered spot trading across multiple crypto assets with INR pairs before regulatory uncertainty around Indian banking access forced it to shut down all services in June 2019, asking users to withdraw their holdings by July 15, 2019. The company is DEFUNCT: koinex.in now serves only a single static wind-down notice directing former users to claim any crypto assets left on the platform through CoinDCX, with which Koinex partnered for the transition. There is no live product, developer portal, documentation, or API surface; the domain''s TLS certificate expired in March 2025 and every path other than the notice returns 403. Retained in the API Evangelist network as a historical record of a shut-down crypto exchange and as a Pantera Capital portfolio lead.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/koinex.png
layout: provider
modified: '2026-07-19'
name: Koinex
nav: Providers
network: true
overview: Koinex is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Crypto, Cryptocurrency Exchange, Digital Assets, and Trading.
random_paper: 3
score:
  band: minimal
  composite: 1.2
  coverage:
    artifact_dirs: 2
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 1.2
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 10.0
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/koinex/refs/heads/main/screenshots/koinex-2026-07-25T224111.png
security:
- kind: domain-security
  name: Koinex Domain Security
  slug: koinex-domain-security
  summary_line: no transport/DNS hardening detected
slug: koinex
tags:
- Company
- Crypto
- Cryptocurrency Exchange
- Digital Assets
- Trading
- India
- Fintech
- Defunct
website: https://koinex.in/
---
