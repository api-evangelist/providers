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
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 25.2
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: REST/JSON API versioned under /v2 at https://api.matilogistics.com for tracking requests, shipments, containers, carrier and terminal reference data, and webhooks. Bearer-token auth (tnt_ keys, one pe
  name: Mati Logistics Track and Trace API
  slug: mati-logistics-track-and-trace-api
artifact_total: 8
asyncapis:
- description: ''
  name: Matilogistics Webhooks
  slug: matilogistics-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.matilogistics.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.matilogistics.com/api
- group: docs
  title: ''
  type: APIReference
  url: https://www.matilogistics.com/api
- group: start
  title: ''
  type: GettingStarted
  url: https://www.matilogistics.com/api#access
- group: commercial
  title: ''
  type: Pricing
  url: https://www.matilogistics.com/track-trace#pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.matilogistics.com/signup
- group: start
  title: ''
  type: Login
  url: https://www.matilogistics.com/login
- group: auth
  href: https://artifacts.apis.io/matilogistics/authentication/matilogistics-authentication.yml
  title: ''
  type: Authentication
  url: authentication/matilogistics-authentication.yml
- group: design
  href: https://artifacts.apis.io/matilogistics/conventions/matilogistics-conventions.yml
  title: ''
  type: Conventions
  url: conventions/matilogistics-conventions.yml
- group: design
  href: https://artifacts.apis.io/matilogistics/errors/matilogistics-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/matilogistics-problem-types.yml
- group: operate
  href: https://artifacts.apis.io/matilogistics/rate-limits/matilogistics-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/matilogistics-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/matilogistics/lifecycle/matilogistics-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/matilogistics-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/matilogistics/asyncapi/matilogistics-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/matilogistics-webhooks.yml
- group: design
  href: https://artifacts.apis.io/matilogistics/data-model/matilogistics-data-model.yml
  title: ''
  type: DataModel
  url: data-model/matilogistics-data-model.yml
- group: design
  href: https://artifacts.apis.io/matilogistics/conformance/matilogistics-conformance.yml
  title: ''
  type: Conformance
  url: conformance/matilogistics-conformance.yml
- group: commercial
  href: https://artifacts.apis.io/matilogistics/plans/matilogistics-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/matilogistics-plans-pricing.yml
- group: build
  href: https://artifacts.apis.io/matilogistics/packages/matilogistics-packages.yml
  title: ''
  type: Packages
  url: packages/matilogistics-packages.yml
- group: agent
  href: https://artifacts.apis.io/matilogistics/llms/matilogistics-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/matilogistics-llms.txt
- group: auth
  href: https://artifacts.apis.io/matilogistics/security/matilogistics-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/matilogistics-domain-security.yml
created: '2026-08-27'
description: 'Mati Logistics runs a network for global trade connecting buyers, suppliers, distributors, forwarders and NVOCCs, with two products: an AI sourcing agent over customs-derived trade data covering 66,459 manufacturers and exporters, and Track and Trace. Track and Trace is the API product: a REST/JSON API for ocean container, bill-of-lading and booking shipment visibility across 24 ocean carriers and NVOCCs, returning normalized milestone events, carrier-stated routes, transshipment dwell and last-free-day data by polling or by HMAC-signed webhook. Bearer-token auth, cursor pagination, ISO 6346 and SCAC identifiers. API access is gated behind a paid subscription tier.'
finops:
- has_sources: true
  method: derived
  name: Matilogistics Finops
  primary_unit: shipment
  service_category: ''
  slug: matilogistics-finops
  template: false
image: https://www.matilogistics.com/landing-logo.svg
layout: provider
modified: '2026-08-27'
name: Mati Logistics
nav: Providers
network: true
overview: 'Mati Logistics is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Logistics, Supply Chain, Shipping, Container Tracking, and Ocean Freight.


  The Mati Logistics catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Mati Logistics'' developer surface includes documentation, API reference, getting-started guide, pricing, signup flow, authentication, and 13 more developer resources.'
plans:
- name: Matilogistics Plans Pricing
  plan_count: 4
  slug: matilogistics-plans-pricing
- name: Matilogistics Price Estimates
  plan_count: 0
  slug: matilogistics-price-estimates
random_paper: 12
rate_limits:
- limit_count: 2
  name: Matilogistics Rate Limits
  slug: matilogistics-rate-limits
score:
  band: developing
  composite: 42.7
  coverage:
    artifact_dirs: 18
    catalog_earned: 57.0
    catalog_earned_first_party: 20.0
    catalog_gap: 58.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.5
  facets:
    access_clarity: 63.2
    contract_governance: 18.2
    contract_quality: 39.0
    developer_ergonomics: 40.5
    discoverability: 60.7
    operational_transparency: 28.9
  previous_composite: 41.2
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/matilogistics/matilogistics-2026-09-02T150521.png
security:
- kind: authentication
  name: Matilogistics Authentication
  slug: matilogistics-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Matilogistics Domain Security
  slug: matilogistics-domain-security
  summary_line: TLSv1.3 · DMARC
slug: matilogistics
tags:
- Logistics
- Supply Chain
- Shipping
- Container Tracking
- Ocean Freight
- Track and Trace
- Shipment Visibility
- Freight Forwarding
- NVOCC
- Webhook
- REST
- Procurement
website: https://www.matilogistics.com
---
