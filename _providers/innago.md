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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Innago Agentic Access
  operation_count: 21
  slug: innago-agentic-access
  summary_line: 21 operations · 7 acting
api_count: 9
apis:
- description: Manage expenses
  name: Innago Expenses API
  slug: innago-expenses-api
- description: Map and manage external reference identifiers
  name: Innago External References API
  slug: innago-external-references-api
- description: API health check
  name: Innago Health API
  slug: innago-health-api
- description: Manage invoices
  name: Innago Invoices API
  slug: innago-invoices-api
- description: Manage lease agreements
  name: Innago Leases API
  slug: innago-leases-api
- description: Manage maintenance tickets
  name: Innago Maintenance API
  slug: innago-maintenance-api
- description: Manage payments
  name: Innago Payments API
  slug: innago-payments-api
- description: Manage properties and units
  name: Innago Properties API
  slug: innago-properties-api
- description: Manage tenant information
  name: Innago Tenants API
  slug: innago-tenants-api
artifact_total: 21
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/innago-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/innago-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/innago-authentication.yml
- group: commercial
  title: ''
  type: Plans
  url: https://raw.githubusercontent.com/api-evangelist/innago/refs/heads/main/plans/plans.yml
- group: operate
  title: ''
  type: RateLimits
  url: https://raw.githubusercontent.com/api-evangelist/innago/refs/heads/main/rate-limits/rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: https://raw.githubusercontent.com/api-evangelist/innago/refs/heads/main/finops/finops.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://innago.com/pricing/
- group: company
  title: ''
  type: Blog
  url: https://innago.com/blog/
- group: start
  title: ''
  type: Login
  url: https://auth.innago.com/login
- group: start
  title: ''
  type: Signup
  url: https://innago.com/get-started/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://auth.innago.com/termsandcondition
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://auth.innago.com/privacypolicy
created: '2026-06-13'
description: Innago is a free property management software platform with a REST API for managing leases, tenant applications, rent collection, maintenance requests, invoicing, and landlord-tenant communication. The API uses Bearer token and API key authentication and provides endpoints for properties, units, tenants, leases, invoices, payments, expenses, and maintenance tickets.
finops:
- name: Finops
  service_category: ''
  slug: finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/innago.png
json_schemas:
- name: Invoice
  property_count: 6
  slug: invoice
- name: Lease
  property_count: 18
  slug: lease
- name: MaintenanceTicket
  property_count: 13
  slug: maintenance
- name: Property
  property_count: 12
  slug: property
jsonld:
- class_count: 0
  name: Innago Context
  property_count: 0
  slug: innago
layout: provider
modified: '2026-06-13'
name: Innago
nav: Providers
network: true
overview: 'Innago publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Expenses API, External References API, Health API, and 6 more. Tagged areas include Property Management, Real Estate, Leases, Rent Collection, and Maintenance.


  The Innago catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Innago''s developer surface includes authentication, pricing, engineering blog, signup flow, and 8 more developer resources.'
plans:
- name: Plans
  plan_count: 2
  slug: plans
random_paper: 4
rate_limits:
- limit_count: 0
  name: Rate Limits
  slug: rate-limits
rules:
- name: Innago API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: innago-jsonschema-spectral-rules
score:
  band: developing
  composite: 47.6
  delta: -5.8
  facets:
    commercial_clarity: 73.7
    contract_quality: 69.5
    developer_ergonomics: 13.0
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 0.0
  previous_composite: 53.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 39.1
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/innago/refs/heads/main/screenshots/innago-2026-06-20T183356.png
security:
- kind: authentication
  name: Innago Authentication
  slug: innago-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Innago Domain Security
  slug: innago-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: innago
tags:
- Property Management
- Real Estate
- Leases
- Rent Collection
- Maintenance
- Tenants
- Invoicing
- Payments
---
