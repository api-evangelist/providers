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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 31.1
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Taskrabbit Agentic Access
  operation_count: 14
  slug: taskrabbit-agentic-access
  summary_line: 14 operations · 9 acting
api_count: 5
apis:
- description: Dolly-based on-demand delivery, quoting, and routing.
  name: TaskRabbit Delivery API
  slug: taskrabbit-delivery-api
- description: Real-time bookable time windows for Home Services projects.
  name: TaskRabbit Home Services Availability API
  slug: taskrabbit-home-services-availability-api
- description: Bid, book, retrieve, cancel, and reschedule Home Services projects.
  name: TaskRabbit Home Services Booking API
  slug: taskrabbit-home-services-booking-api
- description: Partner brand service catalog for Home Services.
  name: TaskRabbit Home Services Catalog API
  slug: taskrabbit-home-services-catalog-api
- description: Pricing and eligibility estimation for Home Services projects.
  name: TaskRabbit Home Services Estimate API
  slug: taskrabbit-home-services-estimate-api
artifact_total: 16
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: TaskRabbit Partner Delivery API
  slug: open-taskrabbit-delivery-api
- collection_type: open
  name: TaskRabbit Partner Delivery Home Services Availability API
  slug: open-taskrabbit-home-services-availability-api
- collection_type: open
  name: TaskRabbit Partner Delivery Home Services Booking API
  slug: open-taskrabbit-home-services-booking-api
- collection_type: open
  name: TaskRabbit Partner Delivery Home Services Catalog API
  slug: open-taskrabbit-home-services-catalog-api
- collection_type: open
  name: TaskRabbit Partner Delivery Home Services Estimate API
  slug: open-taskrabbit-home-services-estimate-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/taskrabbit-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/taskrabbit-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/taskrabbit-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/taskrabbit-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/taskrabbit
- group: company
  title: ''
  type: Website
  url: https://www.taskrabbit.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.taskrabbit.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/taskrabbit-plans-pricing.yml
- group: company
  title: ''
  type: Blog
  url: https://www.taskrabbit.com/blog/
created: '2026-07-03'
description: TaskRabbit is a gig-economy marketplace connecting customers with local, vetted Taskers for furniture assembly, handyman work, moving, and other home services. Ingka Group (IKEA) acquired TaskRabbit in 2017 and has since deepened the integration, including in-store and checkout-time TaskRabbit assembly booking at IKEA. TaskRabbit's original developer story dates to February 2012, when it ran an open API that let third-party to-do apps (Astrid, Producteev) create tasks on a user's behalf; that early open, self-serve API is long gone. In November 2024 TaskRabbit acquired on-demand delivery company Dolly and rebranded its service as TaskRabbit Delivery. Today TaskRabbit operates one gated Partner API program (developer.taskrabbit.com) spanning two live surfaces - Delivery (built on Dolly's pre-existing Partner API, "PAPI") and a newer, 2025-12-versioned Home Services Partner Platform (Estimate, Availability, Bid, Book) that lets approved partners quote, book, and manage TaskRabbit
  projects, including IKEA-style furniture assembly, inside their own apps. Access requires partner approval (TaskRabbit reviews requests within about two business days) and Auth0 OAuth2 client-credentials (machine-to-machine) tokens; there is no public self-serve signup and no published API price list, since commercial terms are negotiated per partner. End-customer pricing on TaskRabbit itself follows a standard Service Fee plus Trust & Support Fee structure layered on top of each Tasker's hourly rate.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/taskrabbit.png
layout: provider
modified: '2026-07-03'
name: TaskRabbit
nav: Providers
network: true
overview: 'TaskRabbit publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Delivery API, Home Services Availability API, Home Services Booking API, and 2 more. Tagged areas include Gig Economy, Handyman, Home Services, Marketplace, and Delivery.


  TaskRabbit''s developer surface includes authentication, documentation, engineering blog, and 6 more developer resources.'
plans:
- name: Taskrabbit Plans Pricing
  plan_count: 3
  slug: taskrabbit-plans-pricing
random_paper: 13
scopes:
- name: Taskrabbit Scopes
  scope_count: 0
  slug: taskrabbit-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 31.0
  delta: 0.0
  facets:
    access_clarity: 31.6
    commercial_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 54.0
    developer_ergonomics: 19.0
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 31.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
security:
- kind: authentication
  name: Taskrabbit Authentication
  slug: taskrabbit-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Taskrabbit Domain Security
  slug: taskrabbit-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: taskrabbit
tags:
- Gig Economy
- Handyman
- Home Services
- Marketplace
- Delivery
- Moving
- Partner API
- IKEA
website: https://www.taskrabbit.com
---
