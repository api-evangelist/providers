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
- acting_count: 3
  human_in_the_loop: 0
  name: Vagaro Agentic Access
  operation_count: 11
  slug: vagaro-agentic-access
  summary_line: 11 operations · 3 acting
api_count: 7
apis:
- description: Outbound event notifications - HTTP POST requests to a merchant- registered HTTPS endpoint, not a WebSocket - fired whenever Appointments, Customers, Employees, Transactions, Form Responses, or Busine
  name: Vagaro Webhooks
  slug: vagaro-webhooks
- description: Appointment status, timing, and service-provider details. Endpoints modeled.
  name: Vagaro Appointments API
  slug: vagaro-appointments-api
- description: Access token issuance for the Enterprise Business API.
  name: Vagaro Authentication API
  slug: vagaro-authentication-api
- description: Customer contact information and tags. Endpoints modeled.
  name: Vagaro Customers API
  slug: vagaro-customers-api
- description: Assign/unassign staff across locations and provision calendars. Endpoints modeled.
  name: Vagaro Employee Management API
  slug: vagaro-employee-management-api
- description: Service provider contact information and reporting relationships. Endpoints modeled.
  name: Vagaro Employees API
  slug: vagaro-employees-api
- description: Single- and multi-location business details. Endpoints modeled.
  name: Vagaro Locations API
  slug: vagaro-locations-api
artifact_total: 13
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/vagaro-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/vagaro-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/vagaro-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/vagaro
- group: company
  title: ''
  type: Website
  url: https://www.vagaro.com/pro
- group: docs
  title: ''
  type: Documentation
  url: https://docs.vagaro.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/vagaro-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/vagaro-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/vagaro-finops.yml
created: '2026-07-03'
description: Vagaro is a cloud platform for salon, spa, and fitness/wellness business management - scheduling, point of sale and payments, marketing, and a consumer booking marketplace (Vagaro.com and the Vagaro app). Vagaro publishes a real developer surface at docs.vagaro.com, a readme.io-hosted "PUBLIC - Enterprise Business API V2" site with a documented OAuth-style Access Token endpoint, five REST capability areas (Employee Management, Locations, Appointments, Customers, Employees), and an outbound Webhooks system covering Appointments, Customers, Employees, Transactions, Form Responses, and Business Locations plus booking- widget interaction events, with fully specified event payloads. Access is gated behind Settings, Developers, APIs & Webhooks inside a Vagaro business account. It requires a paid, non-trial subscription with Credit Card Processing enabled on the computer, tablet, Pay Desk, or PayPro version, a submitted request form, and roughly five to seven business days for approval
  before credentials and full endpoint reference detail become visible.
finops:
- name: Vagaro Finops
  service_category: Vertical SaaS - Salon, Spa, and Fitness Business Management
  slug: vagaro-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/vagaro.png
layout: provider
modified: '2026-07-03'
name: Vagaro
nav: Providers
network: true
overview: 'Vagaro publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Appointments API, Authentication API, Customers API, and 3 more. Tagged areas include Salon, Spa, Fitness, Wellness, and Scheduling.


  Vagaro''s developer surface includes authentication, documentation, and 7 more developer resources.'
plans:
- name: Vagaro Plans Pricing
  plan_count: 5
  slug: vagaro-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 4
  name: Vagaro Rate Limits
  slug: vagaro-rate-limits
score:
  band: thin
  composite: 36.4
  delta: -1.9
  facets:
    commercial_clarity: 39.5
    contract_quality: 55.9
    developer_ergonomics: 19.6
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 38.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Vagaro Authentication
  slug: vagaro-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Vagaro Domain Security
  slug: vagaro-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: vagaro
tags:
- Salon
- Spa
- Fitness
- Wellness
- Scheduling
- Booking
- Vertical SaaS
website: https://www.vagaro.com/pro
---
