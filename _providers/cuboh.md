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
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 13
  human_in_the_loop: 0
  name: Cuboh Agentic Access
  operation_count: 20
  slug: cuboh-agentic-access
  summary_line: 20 operations · 13 acting
api_count: 3
apis:
- description: Merchant (location) status and integration completion.
  name: Cuboh Locations API
  slug: cuboh-locations-api
- description: Menu retrieval, push, creation, update, and validation.
  name: Cuboh Menu API
  slug: cuboh-menu-api
- description: Order creation, retrieval, and lifecycle actions.
  name: Cuboh Orders API
  slug: cuboh-orders-api
artifact_total: 10
collections:
- collection_type: open
  name: Cuboh Integration API
  slug: open-cuboh
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cuboh-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cuboh-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cuboh-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/getcuboh
- group: company
  title: ''
  type: Website
  url: https://www.cuboh.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.cuboh.com/direct
- group: commercial
  title: ''
  type: Plans
  url: plans/cuboh-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/cuboh-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/cuboh-finops.yml
created: '2026-06-21'
description: Cuboh is a restaurant online-ordering management platform that consolidates third-party delivery and pickup orders (DoorDash, Uber Eats, Grubhub, and more) onto a single tablet and into the restaurant POS. For technology partners, Cuboh exposes partner-gated Direct and Connect integration APIs covering orders, menus, merchant locations, and webhooks. API access is provisioned by Cuboh during a partner onboarding and QA-certification process; there is no public self-serve signup.
finops:
- name: Cuboh Finops
  service_category: Management and Governance
  slug: cuboh-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cuboh.png
layout: provider
modified: '2026-06-21'
name: Cuboh
nav: Providers
network: true
overview: 'Cuboh publishes 3 APIs on the [APIs.io](https://apis.io/) network: Locations API, Menu API, and Orders API. Tagged areas include Restaurant, Online Ordering, Delivery, POS, and Order Aggregation.


  Cuboh''s developer surface includes authentication, documentation, and 7 more developer resources.'
plans:
- name: Cuboh Plans Pricing
  plan_count: 5
  slug: cuboh-plans-pricing
random_paper: 53
rate_limits:
- limit_count: 5
  name: Cuboh Rate Limits
  slug: cuboh-rate-limits
score:
  band: thin
  composite: 38.8
  delta: 3.3
  facets:
    commercial_clarity: 39.5
    contract_quality: 51.3
    developer_ergonomics: 19.6
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 35.5
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cuboh/refs/heads/main/screenshots/cuboh-2026-07-25T210903.png
security:
- kind: authentication
  name: Cuboh Authentication
  slug: cuboh-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Cuboh Domain Security
  slug: cuboh-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cuboh
tags:
- Restaurant
- Online Ordering
- Delivery
- POS
- Order Aggregation
website: https://www.cuboh.com/
---
