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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
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
  score: 19.8
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 14
  human_in_the_loop: 0
  name: Wodify Agentic Access
  operation_count: 30
  slug: wodify-agentic-access
  summary_line: 30 operations · 14 acting
api_count: 1
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
artifact_total: 28
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Wodify Classes API
  slug: open-wodify-classes-api
- collection_type: open
  name: Wodify Classes Clients API
  slug: open-wodify-clients-api
- collection_type: open
  name: Wodify Classes Communications API
  slug: open-wodify-communications-api
- collection_type: open
  name: Wodify Classes Financials API
  slug: open-wodify-financials-api
- collection_type: open
  name: Wodify Classes Leads API
  slug: open-wodify-leads-api
- collection_type: open
  name: Wodify Classes Memberships API
  slug: open-wodify-memberships-api
- collection_type: open
  name: Wodify Classes Programs API
  slug: open-wodify-programs-api
- collection_type: open
  name: Wodify Classes Reference API
  slug: open-wodify-reference-api
- collection_type: open
  name: Wodify Classes Services API
  slug: open-wodify-services-api
- collection_type: open
  name: Wodify Classes Workouts API
  slug: open-wodify-workouts-api
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
random_paper: 7
rate_limits:
- limit_count: 2
  name: Wodify Rate Limits
  slug: wodify-rate-limits
score:
  band: thin
  composite: 26.3
  coverage:
    artifact_dirs: 9
    catalog_gap: 55.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 17.3
    developer_ergonomics: 22.6
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 26.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 10
      marker_coverage: 100.0
      total: 10
  schema_version: 0.17.2
  scored_at: '2026-09-01'
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
- Software-as-a-Service
website: https://www.wodify.com
---
