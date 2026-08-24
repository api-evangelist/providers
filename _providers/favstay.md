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
  scored_at: '2026-08-24'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/favstay-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://favstay.com
created: '2026-07-17'
description: FavStay is a hotel and accommodation booking company in the travel and hospitality sector, surfaced as a portfolio company of 500 Global and added to the API Evangelist network. As of this enrichment pass the public site at favstay.com is offline (the host returns a Microsoft Azure Web App 404 error and its TLS certificate does not match the domain), indicating the product is defunct or the web presence has been retired. The domain still resolves with Google Workspace email and an SPF record delegating to the Juniper (ejuniper.com) hospitality booking engine, but no public developer surface, API documentation, or machine-readable specification could be found.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/favstay.png
layout: provider
modified: '2026-07-19'
name: FavStay
nav: Providers
network: true
overview: FavStay is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Travel, Hospitality, Hotels, and Accommodation.
random_paper: 10
score:
  band: minimal
  composite: 5.0
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
  previous_composite: 5.0
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
security:
- kind: domain-security
  name: Favstay Domain Security
  slug: favstay-domain-security
  summary_line: no transport/DNS hardening detected
slug: favstay
tags:
- Company
- Travel
- Hospitality
- Hotels
- Accommodation
- Booking
website: https://favstay.com
---
