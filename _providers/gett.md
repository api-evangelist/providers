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
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.0
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 10
  human_in_the_loop: 0
  name: Gett Agentic Access
  operation_count: 17
  slug: gett-agentic-access
  summary_line: 17 operations · 10 acting
api_count: 6
apis:
- description: OAuth 2.0 token management
  name: Gett Authentication API
  slug: gett-authentication-api
- description: Employee account management
  name: Gett Employee Management API
  slug: gett-employee-management-api
- description: Receipt retrieval and financial operations
  name: Gett Finance API
  slug: gett-finance-api
- description: Ride booking and management operations
  name: Gett Orders API
  slug: gett-orders-api
- description: Available ride products and services
  name: Gett Products API
  slug: gett-products-api
- description: Webhook subscription management
  name: Gett Webhooks API
  slug: gett-webhooks-api
artifact_total: 23
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/gett-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/gett-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/gett-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/gett-authentication.yml
- group: docs
  title: ''
  type: Documentation
  url: https://developer.gett.com/docs/introduction
- group: auth
  title: ''
  type: Authentication
  url: https://developer.gett.com/docs/authorization
- group: operate
  title: ''
  type: StatusPage
  url: https://gett2.statuspage.io/
- group: commercial
  title: ''
  type: Plans
  url: https://raw.githubusercontent.com/api-evangelist/gett/refs/heads/main/plans/plans.yml
- group: operate
  title: ''
  type: RateLimits
  url: https://raw.githubusercontent.com/api-evangelist/gett/refs/heads/main/rate-limits/rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: https://raw.githubusercontent.com/api-evangelist/gett/refs/heads/main/finops/finops.yml
created: '2026-06-13'
description: Gett is a corporate ground transportation platform offering a REST API for booking on-demand and pre-scheduled rides, managing business travel accounts, handling employee records, accessing order receipts, and integrating with expense management systems. The API supports multi-passenger, multi-stop, and multi-dropoff scenarios and connects businesses with a global supplier network of taxis, black cars, and private-hire vehicles.
examples:
- key_count: 3
  name: Create Order Request
  slug: create-order-request
- key_count: 3
  name: Create Order Response
  slug: create-order-response
- key_count: 3
  name: Oauth Token Request
  slug: oauth-token-request
- key_count: 3
  name: Oauth Token Response
  slug: oauth-token-response
- key_count: 3
  name: Webhook Event
  slug: webhook-event
finops:
- name: Finops
  service_category: ''
  slug: finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/gett.png
json_schemas:
- name: Employee
  property_count: 9
  slug: employee
- name: Order
  property_count: 16
  slug: order
- name: WebhookSubscription
  property_count: 7
  slug: webhook-subscription
jsonld:
- class_count: 19
  name: context Context
  property_count: 10
  slug: context
layout: provider
modified: '2026-06-13'
name: Gett
nav: Providers
network: true
overview: 'Gett publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Employee Management API, Finance API, and 3 more. Tagged areas include Ground Transportation, Corporate Travel, Ride Booking, Business Travel, and Expense Management.


  The Gett catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Gett''s developer surface includes authentication, documentation, and 8 more developer resources.'
plans:
- name: Plans
  plan_count: 1
  slug: plans
random_paper: 76
rate_limits:
- limit_count: 1
  name: Rate Limits
  slug: rate-limits
rules:
- name: Gett API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: gett-jsonschema-spectral-rules
score:
  band: developing
  composite: 47.8
  delta: 0.0
  facets:
    commercial_clarity: 36.8
    contract_quality: 69.5
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 36.8
  previous_composite: 47.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/gett/refs/heads/main/screenshots/gett-2026-06-20T181812.png
security:
- kind: authentication
  name: Gett Authentication
  slug: gett-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Gett Domain Security
  slug: gett-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Gett Trust Center
  slug: gett-trust-center
  summary_line: ISO 27001, ISO 27018, PCI DSS, GDPR
slug: gett
tags:
- Ground Transportation
- Corporate Travel
- Ride Booking
- Business Travel
- Expense Management
---
