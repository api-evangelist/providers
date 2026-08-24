---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
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
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.1
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Hotelbeds Agentic Access
  operation_count: 13
  slug: hotelbeds-agentic-access
  summary_line: 13 operations · 5 acting
api_count: 5
apis:
- description: The Activities API from Hotelbeds — 1 operation(s) for activities.
  name: Hotelbeds Activities API
  slug: hotelbeds-activities-api
- description: The Booking API from Hotelbeds — 5 operation(s) for booking.
  name: Hotelbeds Booking API
  slug: hotelbeds-booking-api
- description: The Cache API from Hotelbeds — 1 operation(s) for cache.
  name: Hotelbeds Cache API
  slug: hotelbeds-cache-api
- description: The Content API from Hotelbeds — 3 operation(s) for content.
  name: Hotelbeds Content API
  slug: hotelbeds-content-api
- description: The Transfers API from Hotelbeds — 1 operation(s) for transfers.
  name: Hotelbeds Transfers API
  slug: hotelbeds-transfers-api
artifact_total: 18
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Hotelbeds APItude Activities API
  slug: open-hotelbeds-activities-api
- collection_type: open
  name: Hotelbeds APItude Activities Booking API
  slug: open-hotelbeds-booking-api
- collection_type: open
  name: Hotelbeds APItude Activities Cache API
  slug: open-hotelbeds-cache-api
- collection_type: open
  name: Hotelbeds APItude Activities Content API
  slug: open-hotelbeds-content-api
- collection_type: open
  name: Hotelbeds APItude Activities Transfers API
  slug: open-hotelbeds-transfers-api
- collection_type: open
  name: Hotelbeds APItude API
  slug: open-hotelbeds
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/hotelbeds-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hotelbeds-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/hotelbeds-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/hbxgroup
- group: company
  title: ''
  type: Website
  url: https://www.hotelbeds.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.hotelbeds.com/documentation/
- group: commercial
  title: ''
  type: Plans
  url: plans/hotelbeds-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/hotelbeds-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/hotelbeds-finops.yml
created: '2026-06-25'
description: Hotelbeds (now part of HBX Group) is a global B2B travel bedbank and accommodation wholesaler. Its APItude suite of REST APIs lets travel sellers search, price, and book hotels, activities, and transfers, and pull static content and cached availability, authenticated with an Api-key plus a SHA256 X-Signature of the API key, secret, and request timestamp.
finops:
- name: Hotelbeds Finops
  service_category: Travel and Distribution
  slug: hotelbeds-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/hotelbeds.png
layout: provider
modified: '2026-06-25'
name: Hotelbeds
nav: Providers
network: true
overview: 'Hotelbeds publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Activities API, Booking API, Cache API, and 2 more. Tagged areas include Travel, Hotels, Bedbank, Accommodation, and Booking.


  Hotelbeds'' developer surface includes authentication, documentation, and 7 more developer resources.'
plans:
- name: Hotelbeds Plans Pricing
  plan_count: 2
  slug: hotelbeds-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 4
  name: Hotelbeds Rate Limits
  slug: hotelbeds-rate-limits
score:
  band: thin
  composite: 35.3
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 55.0
    developer_ergonomics: 21.4
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 35.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hotelbeds/refs/heads/main/screenshots/hotelbeds-2026-07-25T221500.png
security:
- kind: authentication
  name: Hotelbeds Authentication
  slug: hotelbeds-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Hotelbeds Domain Security
  slug: hotelbeds-domain-security
  summary_line: TLSv1.3 · DMARC
slug: hotelbeds
tags:
- Travel
- Hotels
- Bedbank
- Accommodation
- Booking
website: https://www.hotelbeds.com
---
