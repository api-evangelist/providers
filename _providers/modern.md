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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 39.4
  scored_at: '2026-08-17'
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
artifact_total: 21
collections:
- collection_type: postman
  name: MODERN Partner API - Documentation
  slug: postman-modern-partner-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: MODERN Partner Dashboards API
  slug: open-modern-dashboards-api
- collection_type: open
  name: MODERN Partner Dashboards Events API
  slug: open-modern-events-api
- collection_type: open
  name: MODERN Partner Dashboards Federation API
  slug: open-modern-federation-api
- collection_type: open
  name: MODERN Partner Dashboards Notes API
  slug: open-modern-notes-api
- collection_type: open
  name: MODERN Partner Dashboards Notifications API
  slug: open-modern-notifications-api
- collection_type: open
  name: MODERN Partner Dashboards Technicians API
  slug: open-modern-technicians-api
- collection_type: open
  name: MODERN Partner Dashboards Users API
  slug: open-modern-users-api
- collection_type: open
  name: MODERN Partner Dashboards Work Orders API
  slug: open-modern-work-orders-api
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/modern-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/modern-partner-api-overlay.yaml
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
mcp_servers:
- description: ''
  name: modern-mcp.yml
  slug: modern-mcpyml
modified: '2026-07-20'
name: Modern
nav: Providers
network: true
overview: 'Modern publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Dashboards API, Events API, Federation API, and 5 more. Tagged areas include Company, Heavy Equipment, Dealership, Field Service, and Work Orders.


  Modern''s developer surface includes documentation, API reference, authentication, and 8 more developer resources.'
random_paper: 49
score:
  band: thin
  composite: 36.5
  delta: 0.0
  facets:
    commercial_clarity: 23.7
    contract_quality: 58.1
    developer_ergonomics: 38.6
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 0.0
  previous_composite: 36.5
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: derived
    skills: derived
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/modern/refs/heads/main/screenshots/modern-2026-08-07T183934.png
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
