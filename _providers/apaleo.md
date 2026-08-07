---
access_model:
  confidence: high
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: true
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
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 17
  human_in_the_loop: 0
  name: Apaleo Agentic Access
  operation_count: 41
  slug: apaleo-agentic-access
  summary_line: 41 operations · 17 acting
api_count: 6
apis:
- description: Real-time availability for units, unit groups, and services.
  name: apaleo Availability API
  slug: apaleo-availability-api
- description: Bookings, reservations, blocks, groups, and offers.
  name: apaleo Booking API
  slug: apaleo-booking-api
- description: Folios, payments, refunds, invoices, and accounts.
  name: apaleo Finance API
  slug: apaleo-finance-api
- description: Properties, units, unit groups, and unit attributes.
  name: apaleo Inventory API
  slug: apaleo-inventory-api
- description: Rate plans, rates, services, and policies.
  name: apaleo Rate Plan API
  slug: apaleo-rate-plan-api
- description: Account- and property-level configuration.
  name: apaleo Settings API
  slug: apaleo-settings-api
artifact_total: 14
collections:
- collection_type: open
  name: apaleo Platform API
  slug: open-apaleo
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/apaleo-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/apaleo-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/apaleo-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/apaleo-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/apaleo
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/apaleo
- group: company
  title: ''
  type: Website
  url: https://www.apaleo.com
- group: docs
  title: ''
  type: Documentation
  url: https://apaleo.dev
- group: commercial
  title: ''
  type: Plans
  url: plans/apaleo-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/apaleo-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/apaleo-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://apaleo.com/blog/home
created: '2026-06-25'
description: apaleo is an API-first cloud hotel property-management system (PMS) and platform. Every capability - reservations, bookings, blocks, inventory, rate plans, availability, and finance - is exposed through documented REST APIs secured with OAuth 2.0, published as OpenAPI, with webhooks for real-time events, enabling an open marketplace of integrations.
finops:
- name: Apaleo Finops
  service_category: Hospitality and Property Management
  slug: apaleo-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/apaleo.png
layout: provider
modified: '2026-06-25'
name: apaleo
nav: Providers
network: true
overview: 'apaleo publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Availability API, Booking API, Finance API, and 3 more. Tagged areas include Hospitality, PMS, Property Management, Hotels, and API-First.


  apaleo''s developer surface includes authentication, documentation, engineering blog, and 9 more developer resources.'
plans:
- name: Apaleo Plans Pricing
  plan_count: 3
  slug: apaleo-plans-pricing
random_paper: 61
rate_limits:
- limit_count: 2
  name: Apaleo Rate Limits
  slug: apaleo-rate-limits
scopes:
- name: Apaleo Scopes
  scope_count: 10
  slug: apaleo-scopes
  summary_line: 10 scopes · clientCredentials/authorizationCode
score:
  band: thin
  composite: 37.0
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 55.8
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 37.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/apaleo/refs/heads/main/screenshots/apaleo-2026-07-25T200530.png
security:
- kind: authentication
  name: Apaleo Authentication
  slug: apaleo-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Apaleo Domain Security
  slug: apaleo-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: apaleo
tags:
- Hospitality
- PMS
- Property Management
- Hotels
- API-First
website: https://www.apaleo.com
---
