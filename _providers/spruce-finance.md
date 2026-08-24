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
  url: security/spruce-finance-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://sprucepower.com
- group: operate
  title: ''
  type: Support
  url: https://sprucepower.com/get-in-touch
created: '2026-07-17'
description: 'Spruce Power operates sprucepower.com as a customer portal ("CustomerPortal") for its residential solar and home energy services, giving homeowners a dashboard to monitor their solar energy systems and production, manage their service agreement, and get in touch with support (public routes include /dashboard, /monitoring, /pro, and /get-in-touch). Surfaced as a GV portfolio company (sector: frontier-tech) and added to the API Evangelist network. Enrichment found no public developer API, developer portal, OpenAPI specification, or working /.well-known/ discovery surface — all /.well-known/ paths return the customer-portal single-page-app shell rather than real documents, and no api./developer./docs. host resolves.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/spruce-finance.png
layout: provider
modified: '2026-07-21'
name: Spruce Finance *
nav: Providers
network: true
overview: 'Spruce Finance * is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Frontier Tech, Energy, Solar, and Home Solar.


  Spruce Finance *''s developer surface includes support and 2 more developer resources.'
random_paper: 20
score:
  band: minimal
  composite: 3.3
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
  previous_composite: 3.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 8.1
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
security:
- kind: domain-security
  name: Spruce Finance Domain Security
  slug: spruce-finance-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: spruce-finance
tags:
- Company
- Frontier Tech
- Energy
- Solar
- Home Solar
- Energy Monitoring
- Customer Portal
website: https://sprucepower.com
---
