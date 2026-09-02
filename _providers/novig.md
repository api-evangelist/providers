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
  url: security/novig-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://novig.us
- group: operate
  title: ''
  type: Support
  url: https://support.novig.us/en
- group: commercial
  title: ''
  type: TermsOfService
  url: https://support.novig.us/en/articles/8590101-terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://support.novig.us/en/articles/8288127-privacy-policy
created: '2026-07-17'
description: 'Novig is a peer-to-peer sports prediction and trading platform marketed as "America''s #1 Sports Trading App," operating as a betting exchange rather than a traditional sportsbook. Users can set their own odds or accept existing lines across two modes: free-to-play with Novig Coins and real-money trading with Novig Cash. The consumer product is delivered as iOS and Android apps and is available in 35+ U.S. states. Backed by Forerunner Ventures, Multicoin Capital, and Pantera Capital. As of this enrichment pass Novig exposes no public API, developer portal, SDKs, or machine-readable discovery surface.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/novig.png
layout: provider
modified: '2026-07-20'
name: Novig
nav: Providers
network: true
overview: 'Novig is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Sports Betting, Prediction Markets, and Trading.


  Novig''s developer surface includes support and 4 more developer resources.'
random_paper: 1
score:
  band: minimal
  composite: 2.2
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
    developer_ergonomics: 4.8
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 2.2
  regulatory:
    applies: true
    matched_via: weak_tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 10.0
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/novig/refs/heads/main/screenshots/novig-2026-08-07T185619.png
security:
- kind: domain-security
  name: Novig Domain Security
  slug: novig-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: novig
tags:
- Company
- Fintech
- Sports Betting
- Prediction Markets
- Trading
- Consumer App
website: https://novig.us
---
