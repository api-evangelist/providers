---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.7
  scored_at: '2026-07-28'
api_count: 8
apis:
- description: Franchise dashboards and dashboard types
  name: Modern Dashboards API
  slug: modern-dashboards-api
- description: Work-order event types and event creation
  name: Modern Events API
  slug: modern-events-api
- description: Token exchange / authentication
  name: Modern Federation API
  slug: modern-federation-api
- description: Technician / work-order notes
  name: Modern Notes API
  slug: modern-notes-api
- description: Customer notifications
  name: Modern Notifications API
  slug: modern-notifications-api
- description: Technician records
  name: Modern Technicians API
  slug: modern-technicians-api
- description: Dashboard users
  name: Modern Users API
  slug: modern-users-api
- description: Service work order lifecycle
  name: Modern Work Orders API
  slug: modern-work-orders-api
artifact_total: 11
collections:
- collection_type: postman
  name: MODERN Partner API - Documentation
  slug: postman-modern-partner-api
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/modern-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://modernis.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.modernis.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.modernis.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.modernis.com/
- group: auth
  title: ''
  type: Authentication
  url: authentication/modern-authentication.yml
- group: start
  title: ''
  type: Login
  url: https://service.modernis.com/login
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://modernis.com/privacy-policy/
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Modern (modernis.com) is a two-way customer interaction platform for heavy-equipment dealerships, unifying service communications "from intake to invoice" across construction, agriculture, mining, landscaping, and material-handling sectors. It provides two-way text and email messaging, digital repair-order approvals, inspection and warranty documentation, outbound maintenance scheduling, rental tracking, parts-order status, and DMS integration. The MODERN Partner API (docs.modernis.com, base https://connect.modernis.com) lets authorized integrators read dealership dashboards, manage service work orders, post work-order events, send customer notifications, and maintain technicians and notes on a franchise's behalf using 24-hour bearer tokens exchanged from franchise credentials.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/modern.png
layout: provider
modified: '2026-07-20'
name: Modern
nav: Providers
network: true
overview: 'Modern publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Dashboards API, Events API, Federation API, and 5 more. Tagged areas include Company, Heavy Equipment, Dealership, Field Service, and Work Orders.


  Modern''s developer surface includes documentation, API reference, authentication, and 6 more developer resources.'
random_paper: 29
score:
  band: thin
  composite: 36.8
  delta: -0.4
  facets:
    commercial_clarity: 23.7
    contract_quality: 56.6
    developer_ergonomics: 36.4
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 0.0
  previous_composite: 37.2
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: derived
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Modern Authentication
  slug: modern-authentication
  summary_line: http-basic/http-bearer · 2 schemes
- kind: domain-security
  name: Modern Domain Security
  slug: modern-domain-security
  summary_line: TLSv1.3
slug: modern
tags:
- Company
- Heavy Equipment
- Dealership
- Field Service
- Work Orders
- Customer Communications
- Notifications
- Partner API
website: https://modernis.com/
---
