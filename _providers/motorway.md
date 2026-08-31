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
  url: security/motorway-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://motorway.co.uk/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/motorway-llms.txt
- group: company
  title: ''
  type: Blog
  url: https://motorway.co.uk/blog
- group: operate
  title: ''
  type: Support
  url: https://help.motorway.co.uk/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://motorway.co.uk/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://motorway.co.uk/privacy
created: '2026-07-17'
description: 'Motorway is the UK''s fastest-growing used car marketplace, connecting private sellers with a network of more than 8,000 verified car dealers through a daily online auction. Founded in 2017 and headquartered in London and Brighton, the platform provides instant AI-assisted vehicle valuations, a mobile app that builds a sale-ready car profile, nationwide home collection, same-day payment (Motorway Pay), transport (Motorway Move), and outstanding-finance handling. Over one million people have used Motorway to sell a car. It is a consumer and dealer (B2C/B2B) marketplace rather than a public API provider: no developer portal, OpenAPI, or public API surface is published as of this enrichment pass. Backed by Index Ventures, ICONIQ Growth, BMW i Ventures and LocalGlobe.'
image: https://static.motorway.co.uk/static/assets_seller/og-website-image-5.e59fc584148069c303fb.png
layout: provider
modified: '2026-07-20'
name: Motorway
nav: Providers
network: true
overview: 'Motorway is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Marketplace, Automotive, Used Cars, and Car Auction.


  Motorway''s developer surface includes engineering blog, support, and 5 more developer resources.'
random_paper: 16
score:
  band: minimal
  composite: 9.8
  coverage:
    artifact_dirs: 3
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 9.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 21.9
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/motorway/refs/heads/main/screenshots/motorway-2026-08-07T184338.png
security:
- kind: domain-security
  name: Motorway Domain Security
  slug: motorway-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: motorway
tags:
- Company
- Marketplace
- Automotive
- Used Cars
- Car Auction
- Vehicle Valuation
- Payments
website: https://motorway.co.uk/
---
