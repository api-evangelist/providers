---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Nuitee Agentic Access
  operation_count: 20
  slug: nuitee-agentic-access
  summary_line: 20 operations · 7 acting
api_count: 4
apis:
- description: Prebook, book, retrieve, list, and cancel reservations.
  name: Nuitée (LiteAPI) Booking API
  slug: nuitee-booking-api
- description: Static hotel content, reviews, and reference data.
  name: Nuitée (LiteAPI) Hotel Data API
  slug: nuitee-hotel-data-api
- description: Loyalty program configuration, points, and vouchers.
  name: Nuitée (LiteAPI) Loyalty API
  slug: nuitee-loyalty-api
- description: Real-time room rates and availability search.
  name: Nuitée (LiteAPI) Rates API
  slug: nuitee-rates-api
artifact_total: 16
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: LiteAPI (Nuitée) Hotel Booking API
  slug: open-nuitee-booking-api
- collection_type: open
  name: LiteAPI (Nuitée) Hotel Booking Hotel Data API
  slug: open-nuitee-hotel-data-api
- collection_type: open
  name: LiteAPI (Nuitée) Hotel Booking Loyalty API
  slug: open-nuitee-loyalty-api
- collection_type: open
  name: LiteAPI (Nuitée) Hotel Booking Rates API
  slug: open-nuitee-rates-api
- collection_type: open
  name: LiteAPI (Nuitée) Hotel Booking API
  slug: open-nuitee
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/nuitee-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nuitee-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/nuitee-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/liteapi-travel
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/nuitee
- group: company
  title: ''
  type: Website
  url: https://www.liteapi.travel
- group: docs
  title: ''
  type: Documentation
  url: https://docs.liteapi.travel
- group: commercial
  title: ''
  type: Plans
  url: plans/nuitee-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/nuitee-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/nuitee-finops.yml
created: '2026-06-25'
description: Nuitée is the travel technology company behind LiteAPI, a hotel-booking and distribution API platform. LiteAPI exposes a unified REST interface over 2M+ hotels for static content, real-time rates and availability, the prebook/book/cancel reservation flow, loyalty and vouchers, and booking webhooks, with a commission/markup revenue model and a free sandbox.
finops:
- name: Nuitee Finops
  service_category: Travel and Hospitality
  slug: nuitee-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/nuitee.png
layout: provider
modified: '2026-06-25'
name: Nuitée (LiteAPI)
nav: Providers
network: true
overview: 'Nuitée (LiteAPI) publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Booking API, Hotel Data API, Loyalty API, and 1 more. Tagged areas include Travel, Hotels, Booking, Distribution, and Hospitality.


  Nuitée (LiteAPI)''s developer surface includes authentication, documentation, and 8 more developer resources.'
plans:
- name: Nuitee Plans Pricing
  plan_count: 3
  slug: nuitee-plans-pricing
random_paper: 54
rate_limits:
- limit_count: 2
  name: Nuitee Rate Limits
  slug: nuitee-rate-limits
score:
  band: thin
  composite: 36.6
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 56.0
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 36.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/nuitee/refs/heads/main/screenshots/nuitee-2026-08-07T185721.png
security:
- kind: authentication
  name: Nuitee Authentication
  slug: nuitee-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Nuitee Domain Security
  slug: nuitee-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: nuitee
tags:
- Travel
- Hotels
- Booking
- Distribution
- Hospitality
website: https://www.liteapi.travel
---
