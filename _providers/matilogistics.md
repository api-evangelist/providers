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
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.2
  scored_at: '2026-09-02'
api_count: 1
apis:
- description: REST/JSON API versioned under /v2 at https://api.matilogistics.com for tracking requests, shipments, containers, carrier and terminal reference data, and webhooks. Bearer-token auth (tnt_ keys, one pe
  name: Mati Logistics Track and Trace API
  slug: mati-logistics-track-and-trace-api
artifact_total: 6
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
  title: ''
  type: Authentication
  url: authentication/matilogistics-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/matilogistics-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/matilogistics-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/matilogistics-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/matilogistics-lifecycle.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/matilogistics-webhooks.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/matilogistics-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/matilogistics-conformance.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/matilogistics-plans-pricing.yml
- group: build
  title: ''
  type: Packages
  url: packages/matilogistics-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/matilogistics-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/matilogistics-domain-security.yml
created: '2026-08-27'
description: 'Mati Logistics runs a network for global trade connecting buyers, suppliers, distributors, forwarders and NVOCCs, with two products: an AI sourcing agent over customs-derived trade data covering 66,459 manufacturers and exporters, and Track and Trace. Track and Trace is the API product: a REST/JSON API for ocean container, bill-of-lading and booking shipment visibility across 24 ocean carriers and NVOCCs, returning normalized milestone events, carrier-stated routes, transshipment dwell and last-free-day data by polling or by HMAC-signed webhook. Bearer-token auth, cursor pagination, ISO 6346 and SCAC identifiers. API access is gated behind a paid subscription tier.'
image: https://www.matilogistics.com/landing-logo.svg
layout: provider
modified: '2026-08-27'
name: Mati Logistics
nav: Providers
network: true
overview: 'Mati Logistics publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Logistics, Supply Chain, Shipping, Container Tracking, and Ocean Freight.


  The Mati Logistics catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Mati Logistics'' developer surface includes documentation, API reference, getting-started guide, pricing, signup flow, authentication, and 13 more developer resources.'
plans:
- name: Matilogistics Plans Pricing
  plan_count: 3
  slug: matilogistics-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 2
  name: Matilogistics Rate Limits
  slug: matilogistics-rate-limits
score:
  band: developing
  composite: 41.8
  coverage:
    artifact_dirs: 15
    catalog_gap: 61.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 55.3
    commercial_clarity: 55.3
    contract_governance: 18.2
    contract_quality: 41.6
    developer_ergonomics: 40.5
    discoverability: 63.0
    governance: 18.2
    operational_transparency: 28.9
  previous_composite: 41.8
  provenance:
    conformance: first-party
    mcp: derived
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/matilogistics/refs/heads/main/screenshots/matilogistics-2026-09-02T150521.png
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
