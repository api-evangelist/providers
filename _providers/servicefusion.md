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
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Servicefusion Agentic Access
  operation_count: 24
  slug: servicefusion-agentic-access
  summary_line: 24 operations · 9 acting
api_count: 1
apis:
- baseURL: https://api.servicefusion.com/v1
  baseurl_source: declared
  description: Non-job scheduled calendar items and reminders.
  name: Service Fusion Calendar Tasks API
  slug: servicefusion-calendar-tasks-api
- baseURL: https://api.servicefusion.com/v1
  baseurl_source: declared
  description: Individual contacts and service locations on a customer account.
  name: Service Fusion Contacts API
  slug: servicefusion-contacts-api
- baseURL: https://api.servicefusion.com/v1
  baseurl_source: declared
  description: Customer accounts served by the contractor.
  name: Service Fusion Customers API
  slug: servicefusion-customers-api
- baseURL: https://api.servicefusion.com/v1
  baseurl_source: declared
  description: Estimates (quotes) presented to customers before work begins.
  name: Service Fusion Estimates API
  slug: servicefusion-estimates-api
- baseURL: https://api.servicefusion.com/v1
  baseurl_source: declared
  description: Invoices billed to customers for completed work.
  name: Service Fusion Invoices API
  slug: servicefusion-invoices-api
- baseURL: https://api.servicefusion.com/v1
  baseurl_source: declared
  description: Jobs (work orders) scheduled and dispatched to technicians.
  name: Service Fusion Jobs API
  slug: servicefusion-jobs-api
- baseURL: https://api.servicefusion.com/v1
  baseurl_source: declared
  description: Payments applied against invoices.
  name: Service Fusion Payments API
  slug: servicefusion-payments-api
- baseURL: https://api.servicefusion.com/v1
  baseurl_source: declared
  description: Catalog of products (parts/inventory) and services (labor/tasks).
  name: Service Fusion Products and Services API
  slug: servicefusion-products-and-services-api
- baseURL: https://api.servicefusion.com/v1
  baseurl_source: declared
  description: Technicians and users the work is assigned to.
  name: Service Fusion Techs and Users API
  slug: servicefusion-techs-and-users-api
artifact_total: 27
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Service Fusion Open Calendar Tasks API
  slug: open-servicefusion-calendar-tasks-api
- collection_type: open
  name: Service Fusion Open Calendar Tasks Contacts API
  slug: open-servicefusion-contacts-api
- collection_type: open
  name: Service Fusion Open Calendar Tasks Customers API
  slug: open-servicefusion-customers-api
- collection_type: open
  name: Service Fusion Open Calendar Tasks Estimates API
  slug: open-servicefusion-estimates-api
- collection_type: open
  name: Service Fusion Open Calendar Tasks Invoices API
  slug: open-servicefusion-invoices-api
- collection_type: open
  name: Service Fusion Open Calendar Tasks Jobs API
  slug: open-servicefusion-jobs-api
- collection_type: open
  name: Service Fusion Open Calendar Tasks Payments API
  slug: open-servicefusion-payments-api
- collection_type: open
  name: Service Fusion Open Calendar Tasks Products and Services API
  slug: open-servicefusion-products-and-services-api
- collection_type: open
  name: Service Fusion Open Calendar Tasks Techs and Users API
  slug: open-servicefusion-techs-and-users-api
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
random_paper: 6
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
  composite: 39.0
  coverage:
    artifact_dirs: 11
    catalog_earned: 64.0
    catalog_earned_first_party: 0.0
    catalog_gap: 51.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.7
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 54.9
    developer_ergonomics: 32.1
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 39.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/servicefusion/refs/heads/main/screenshots/servicefusion-2026-09-02T155002.png
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
