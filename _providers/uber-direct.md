---
access_model:
  confidence: high
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
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
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Uber Direct Agentic Access
  operation_count: 3
  slug: uber-direct-agentic-access
  summary_line: 3 operations · 2 acting
api_count: 2
apis:
- description: Uber Direct API (DaaS) for quoting, creating, tracking, and managing deliveries through the Uber courier network. Includes Direct, Organizations, Courier Pick & Pack, Refund, and Business Location Man
  name: Uber Direct API
  slug: uber-direct-api
- description: The Customers API from Uber Direct — 2 operation(s) for customers.
  name: Uber Direct Customers API
  slug: uber-direct-customers-api
artifact_total: 12
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Uber Direct Customers API
  slug: open-uber-direct-customers-api
- collection_type: open
  name: Uber Direct API
  slug: open-uber-direct
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/uber-direct-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/uber-direct-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/uber-direct-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/uber-direct-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/uber
- group: company
  title: ''
  type: Website
  url: https://www.uber.com/us/en/business/services/deliveries/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.uber.com/docs/deliveries
- group: commercial
  title: ''
  type: Plans
  url: plans/uber-direct-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/uber-direct-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/uber-direct-finops.yml
created: '2026-05-08'
description: Uber Direct is Uber's last-mile delivery-as-a-service platform that lets merchants dispatch couriers via the Uber network for on-demand and scheduled deliveries.
finops:
- name: Uber Direct Finops
  service_category: Logistics
  slug: uber-direct-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/uber-direct.png
layout: provider
modified: '2026-05-08'
name: Uber Direct
nav: Providers
network: true
overview: 'Uber Direct publishes 1 API on the [APIs.io](https://apis.io/) network: Customers API. Tagged areas include Logistics, Last Mile Delivery, Couriers, Fulfillment, and DaaS.


  Uber Direct''s developer surface includes authentication, documentation, and 8 more developer resources.'
plans:
- name: Uber Direct Plans Pricing
  plan_count: 1
  slug: uber-direct-plans-pricing
random_paper: 67
rate_limits:
- limit_count: 1
  name: Uber Direct Rate Limits
  slug: uber-direct-rate-limits
scopes:
- name: Uber Direct Scopes
  scope_count: 1
  slug: uber-direct-scopes
  summary_line: 1 scope · clientCredentials
score:
  band: thin
  composite: 26.8
  delta: -0.9
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 51.7
    developer_ergonomics: 21.4
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 27.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/uber-direct/refs/heads/main/screenshots/uber-direct-2026-06-20T195931.png
security:
- kind: authentication
  name: Uber Direct Authentication
  slug: uber-direct-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Uber Direct Domain Security
  slug: uber-direct-domain-security
  summary_line: TLSv1.3 · DMARC
slug: uber-direct
tags:
- Logistics
- Last Mile Delivery
- Couriers
- Fulfillment
- DaaS
website: https://www.uber.com/us/en/business/services/deliveries/
---
