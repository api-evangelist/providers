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
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Servicefusion Agentic Access
  operation_count: 24
  slug: servicefusion-agentic-access
  summary_line: 24 operations · 9 acting
api_count: 9
apis:
- description: Non-job scheduled calendar items and reminders.
  name: Service Fusion Calendar Tasks API
  slug: servicefusion-calendar-tasks-api
- description: Individual contacts and service locations on a customer account.
  name: Service Fusion Contacts API
  slug: servicefusion-contacts-api
- description: Customer accounts served by the contractor.
  name: Service Fusion Customers API
  slug: servicefusion-customers-api
- description: Estimates (quotes) presented to customers before work begins.
  name: Service Fusion Estimates API
  slug: servicefusion-estimates-api
- description: Invoices billed to customers for completed work.
  name: Service Fusion Invoices API
  slug: servicefusion-invoices-api
- description: Jobs (work orders) scheduled and dispatched to technicians.
  name: Service Fusion Jobs API
  slug: servicefusion-jobs-api
- description: Payments applied against invoices.
  name: Service Fusion Payments API
  slug: servicefusion-payments-api
- description: Catalog of products (parts/inventory) and services (labor/tasks).
  name: Service Fusion Products and Services API
  slug: servicefusion-products-and-services-api
- description: Technicians and users the work is assigned to.
  name: Service Fusion Techs and Users API
  slug: servicefusion-techs-and-users-api
artifact_total: 17
collections:
- collection_type: open
  name: Service Fusion Open API
  slug: open-servicefusion
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/servicefusion-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/servicefusion-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/servicefusion-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/servicefusion-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/service-fusion
- group: company
  title: ''
  type: Website
  url: https://www.servicefusion.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.servicefusion.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/servicefusion-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/servicefusion-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/servicefusion-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.servicefusion.com/blog/feed/
created: '2026-07-03'
description: Service Fusion is field service management (FSM) software for home-service contractors - HVAC, plumbing, electrical, appliance repair, and similar trades. It covers customer management, estimates, scheduling and dispatch, work orders/jobs, invoicing, payments, inventory, and a technician mobile app, with flat-rate pricing and unlimited users on every plan. Service Fusion exposes an Open API - a REST/JSON interface secured with OAuth 2.0 (base https://api.servicefusion.com/v1, token endpoint https://api.servicefusion.com/oauth/access_token) - that lets developers read and create records for customers, jobs, estimates, invoices, technicians, and related resources. API access is available on the Pro plan; the API is rate limited to roughly 60 requests per minute.
finops:
- name: Servicefusion Finops
  service_category: Field Service Management Software
  slug: servicefusion-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/servicefusion.png
layout: provider
modified: '2026-07-03'
name: Service Fusion
nav: Providers
network: true
overview: 'Service Fusion publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Calendar Tasks API, Contacts API, Customers API, and 6 more. Tagged areas include Field Service Management, FSM, Home Services, Contractors, and Scheduling.


  Service Fusion''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Servicefusion Plans Pricing
  plan_count: 3
  slug: servicefusion-plans-pricing
random_paper: 36
rate_limits:
- limit_count: 4
  name: Servicefusion Rate Limits
  slug: servicefusion-rate-limits
scopes:
- name: Servicefusion Scopes
  scope_count: 0
  slug: servicefusion-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 37.7
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 58.4
    developer_ergonomics: 21.7
    discoverability: 67.5
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 37.7
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Servicefusion Authentication
  slug: servicefusion-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Servicefusion Domain Security
  slug: servicefusion-domain-security
  summary_line: TLSv1.3 · DMARC
slug: servicefusion
tags:
- Field Service Management
- FSM
- Home Services
- Contractors
- Scheduling
- Dispatch
- Invoicing
website: https://www.servicefusion.com
---
