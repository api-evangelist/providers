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
  scored_at: '2026-08-30'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tripplus-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://tripplus.cc
created: '2026-07-17'
description: TripPlus (點數旅遊) is a Taiwan-based travel-rewards and loyalty-points platform. It provides airline mileage award-ticket search and redemption tools, curated recommendations and comparisons of US travel credit cards, and a marketplace for buying and selling airline miles and reward points. The consumer-facing site (tripplus.cc) is fronted by Cloudflare and, as of this enrichment pass, exposes no public developer API, OpenAPI specification, SDKs, or documented well-known endpoints. Backed by 500 Global; tracked in the API Evangelist network as a portfolio lead.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tripplus.png
layout: provider
modified: '2026-07-21'
name: Tripplus
nav: Providers
network: true
overview: Tripplus is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Travel, Loyalty, Rewards, and Points.
random_paper: 17
score:
  band: minimal
  composite: 1.5
  coverage:
    artifact_dirs: 1
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
  previous_composite: 1.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 9.4
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
security:
- kind: domain-security
  name: Tripplus Domain Security
  slug: tripplus-domain-security
  summary_line: TLSv1.3 · DMARC
slug: tripplus
tags:
- Company
- Travel
- Loyalty
- Rewards
- Points
- Miles
- Credit Cards
- Fintech
- Taiwan
website: https://tripplus.cc
---
