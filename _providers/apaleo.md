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
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.8
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 17
  human_in_the_loop: 0
  name: Apaleo Agentic Access
  operation_count: 41
  slug: apaleo-agentic-access
  summary_line: 41 operations · 17 acting
api_count: 1
apis:
- baseURL: https://api.apaleo.com/booking/v1
  baseurl_source: declared
  description: Real-time availability for units, unit groups, and services.
  name: apaleo Availability API
  slug: apaleo-availability-api
- baseURL: https://api.apaleo.com/booking/v1
  baseurl_source: declared
  description: Bookings, reservations, blocks, groups, and offers.
  name: apaleo Booking API
  slug: apaleo-booking-api
- baseURL: https://api.apaleo.com/booking/v1
  baseurl_source: declared
  description: Folios, payments, refunds, invoices, and accounts.
  name: apaleo Finance API
  slug: apaleo-finance-api
- baseURL: https://api.apaleo.com/booking/v1
  baseurl_source: declared
  description: Properties, units, unit groups, and unit attributes.
  name: apaleo Inventory API
  slug: apaleo-inventory-api
- baseURL: https://api.apaleo.com/booking/v1
  baseurl_source: declared
  description: Rate plans, rates, services, and policies.
  name: apaleo Rate Plan API
  slug: apaleo-rate-plan-api
- baseURL: https://api.apaleo.com/booking/v1
  baseurl_source: declared
  description: Account- and property-level configuration.
  name: apaleo Settings API
  slug: apaleo-settings-api
artifact_total: 21
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: apaleo Platform Availability API
  slug: open-apaleo-availability-api
- collection_type: open
  name: apaleo Platform Availability Booking API
  slug: open-apaleo-booking-api
- collection_type: open
  name: apaleo Platform Availability Finance API
  slug: open-apaleo-finance-api
- collection_type: open
  name: apaleo Platform Availability Inventory API
  slug: open-apaleo-inventory-api
- collection_type: open
  name: apaleo Platform Availability Rate Plan API
  slug: open-apaleo-rate-plan-api
- collection_type: open
  name: apaleo Platform Availability Settings API
  slug: open-apaleo-settings-api
- collection_type: open
  name: apaleo Platform API
  slug: open-apaleo
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/apaleo-capability-edges.yml
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


  apaleo''s developer surface includes authentication, documentation, engineering blog, and 10 more developer resources.'
plans:
- name: Apaleo Plans Pricing
  plan_count: 3
  slug: apaleo-plans-pricing
random_paper: 17
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
  composite: 36.4
  coverage:
    artifact_dirs: 12
    catalog_gap: 55.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 49.3
    developer_ergonomics: 31.0
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 23.7
  previous_composite: 36.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.18.0
  scored_at: '2026-09-02'
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
