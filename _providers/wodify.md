---
access_model:
  confidence: high
  label: Paid (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: paid
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
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 14
  human_in_the_loop: 0
  name: Wodify Agentic Access
  operation_count: 30
  slug: wodify-agentic-access
  summary_line: 30 operations · 14 acting
api_count: 10
apis:
- description: Scheduled classes, waitlists, reservations, and sign-ins.
  name: Wodify Classes API
  slug: wodify-classes-api
- description: Gym clients (members).
  name: Wodify Clients API
  slug: wodify-clients-api
- description: Email, SMS, in-app chat, and tasks.
  name: Wodify Communications API
  slug: wodify-communications-api
- description: Invoices, transactions, discounts, tax rates, and revenue categories.
  name: Wodify Financials API
  slug: wodify-financials-api
- description: Prospective members and their conversion to clients.
  name: Wodify Leads API
  slug: wodify-leads-api
- description: Membership records, templates, holds, and billing configuration.
  name: Wodify Memberships API
  slug: wodify-memberships-api
- description: Training programs offered by the gym.
  name: Wodify Programs API
  slug: wodify-programs-api
- description: Reference data such as locations, employees, programs, and services.
  name: Wodify Reference API
  slug: wodify-reference-api
- description: Appointment services and bookings.
  name: Wodify Services API
  slug: wodify-services-api
- description: Workouts (WODs) and skill progressions.
  name: Wodify Workouts API
  slug: wodify-workouts-api
artifact_total: 17
collections:
- collection_type: open
  name: Wodify API
  slug: open-wodify
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/wodify-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/wodify-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/wodify-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/wodify
- group: company
  title: ''
  type: Website
  url: https://www.wodify.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.wodify.com
- group: commercial
  title: ''
  type: Plans
  url: plans/wodify-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/wodify-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/wodify-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.wodify.com/blog
created: '2026-07-12'
description: Wodify is gym, fitness, and CrossFit box management software covering membership management, billing, class scheduling, lead and client CRM, digital waivers, and workout/performance tracking. The Wodify API is a REST interface at https://api.wodify.com/v1, authenticated with an x-api-key header, that lets partners and gym operators manage leads, clients, memberships, classes, programs, services, appointments, workouts, financials, and communications programmatically.
finops:
- name: Wodify Finops
  service_category: Fitness and Gym Management Software
  slug: wodify-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/wodify.png
layout: provider
modified: '2026-07-12'
name: Wodify
nav: Providers
network: true
overview: 'Wodify publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Classes API, Clients API, Communications API, and 7 more. Tagged areas include Fitness, Gym Management, Membership Management, Fitness Software, and CrossFit.


  Wodify''s developer surface includes authentication, documentation, engineering blog, and 7 more developer resources.'
plans:
- name: Wodify Plans Pricing
  plan_count: 5
  slug: wodify-plans-pricing
random_paper: 88
rate_limits:
- limit_count: 2
  name: Wodify Rate Limits
  slug: wodify-rate-limits
score:
  band: thin
  composite: 38.3
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 63.6
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 38.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
security:
- kind: authentication
  name: Wodify Authentication
  slug: wodify-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Wodify Domain Security
  slug: wodify-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: wodify
tags:
- Fitness
- Gym Management
- Membership Management
- Fitness Software
- CrossFit
- Class Scheduling
- Billing
- Wellness
- SaaS
website: https://www.wodify.com
---
