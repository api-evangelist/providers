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
- acting_count: 26
  human_in_the_loop: 0
  name: Tutorcruncher Agentic Access
  operation_count: 54
  slug: tutorcruncher-agentic-access
  summary_line: 54 operations · 26 acting
api_count: 10
apis:
- description: Affiliates / agents.
  name: TutorCruncher Agents API
  slug: tutorcruncher-agents-api
- description: Appointments (individual lessons / sessions).
  name: TutorCruncher Appointments API
  slug: tutorcruncher-appointments-api
- description: Paying customers (parents or organizations).
  name: TutorCruncher Clients API
  slug: tutorcruncher-clients-api
- description: Tutors who deliver lessons.
  name: TutorCruncher Contractors API
  slug: tutorcruncher-contractors-api
- description: Client invoices and payment.
  name: TutorCruncher Invoices API
  slug: tutorcruncher-invoices-api
- description: Payment orders, proforma invoices, and ad hoc charges.
  name: TutorCruncher Payments API
  slug: tutorcruncher-payments-api
- description: Students who receive tutoring.
  name: TutorCruncher Recipients API
  slug: tutorcruncher-recipients-api
- description: Reference data - subjects, countries, categories, action types.
  name: TutorCruncher Reference API
  slug: tutorcruncher-reference-api
- description: Services (jobs) tying recipients and contractors together.
  name: TutorCruncher Services API
  slug: tutorcruncher-services-api
- description: Webhook event catalog (action types).
  name: TutorCruncher Webhooks API
  slug: tutorcruncher-webhooks-api
artifact_total: 18
collections:
- collection_type: open
  name: TutorCruncher API
  slug: open-tutorcruncher
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/tutorcruncher-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/tutorcruncher-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tutorcruncher-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/tutorcruncher-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tutorcruncher
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/tutorcruncher
- group: company
  title: ''
  type: Website
  url: https://tutorcruncher.com
- group: docs
  title: ''
  type: Documentation
  url: https://api.tutorcruncher.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/tutorcruncher-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/tutorcruncher-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/tutorcruncher-finops.yml
created: '2026-07-03'
description: TutorCruncher is tutoring business management software for agencies, companies, and independent tutors - handling clients, students, tutors, lesson scheduling, invoicing, and payments. Its documented REST API (base https://app.tutorcruncher.com/api/, token-authenticated) exposes clients, recipients (students), contractors (tutors), agents, services (jobs), appointments (lessons), invoices, payment orders, proforma invoices, ad hoc charges, and reference data, with HTTP webhooks for event notifications. Its "Socket" product is a JavaScript embed for publishing public tutor and lesson listings on a provider's own website - not a WebSocket API.
finops:
- name: Tutorcruncher Finops
  service_category: Business Management Software
  slug: tutorcruncher-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tutorcruncher.png
layout: provider
modified: '2026-07-03'
name: TutorCruncher
nav: Providers
network: true
overview: 'TutorCruncher publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Agents API, Appointments API, Clients API, and 7 more. Tagged areas include Tutoring, Education, Business Management, Scheduling, and Invoicing.


  TutorCruncher''s developer surface includes authentication, documentation, and 9 more developer resources.'
plans:
- name: Tutorcruncher Plans Pricing
  plan_count: 3
  slug: tutorcruncher-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 3
  name: Tutorcruncher Rate Limits
  slug: tutorcruncher-rate-limits
score:
  band: thin
  composite: 36.4
  delta: 0.4
  facets:
    commercial_clarity: 39.5
    contract_quality: 50.4
    developer_ergonomics: 19.6
    discoverability: 67.5
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 36.0
  regulatory:
    applies: true
    regime: Payments
    regime_id: payments
    score: 39.1
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Tutorcruncher Authentication
  slug: tutorcruncher-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Tutorcruncher Domain Security
  slug: tutorcruncher-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Tutorcruncher Vulnerability Disclosure
  slug: tutorcruncher-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: tutorcruncher
tags:
- Tutoring
- Education
- Business Management
- Scheduling
- Invoicing
- Payments
- EdTech
website: https://tutorcruncher.com
---
