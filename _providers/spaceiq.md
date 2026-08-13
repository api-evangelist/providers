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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 16.4
  scored_at: '2026-08-12'
api_count: 1
apis:
- description: SpaceIQ's (SiQ) GraphQL API. A single endpoint at https://api.spaceiq.com/queries accepts POST requests with a JSON query body and an access-token bearer header. Read operations cover companies, build
  name: SiQ GraphQL API
  slug: siq-graphql-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/spaceiq-trust-center.yml
- group: company
  title: ''
  type: Website
  url: https://eptura.com/spaceiq/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.spaceiq.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.spaceiq.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.spaceiq.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.spaceiq.com/
- group: company
  title: ''
  type: Blog
  url: https://eptura.com/discover-more/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://eptura.com/pricing/
- group: operate
  title: ''
  type: Support
  url: https://eptura.com/contact-us/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://eptura.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://eptura.com/terms/privacy-policy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.eptura.com/
- group: auth
  title: ''
  type: Compliance
  url: https://security.eptura.com/
- group: auth
  title: ''
  type: Security
  url: https://security.eptura.com/
- group: auth
  title: ''
  type: Authentication
  url: authentication/spaceiq-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/spaceiq-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/spaceiq-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/spaceiq-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/spaceiq-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/spaceiq-conformance.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/spaceiq-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/spaceiq-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/spaceiq-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/spaceiq-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/spaceiq-vulnerability-disclosure.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: 'SpaceIQ (branded SiQ, now part of Eptura) is a workplace and space-management platform for optimizing physical office environments: space planning, desk and meeting-room booking, hoteling, moves management, wayfinding, floorplan management, occupancy analytics, building-attendance reporting, and real-estate forecasting. SpaceIQ exposes a GraphQL API (schema version 1.7) at api.spaceiq.com/queries for reading workplace data (companies, buildings, floors, spaces, departments, employees, meeting-room calendars, map images, and reports/exports) and for creating and deleting meeting-room calendar events. All access is over HTTPS with an admin/IT-generated access token; the schema is fully introspectable.'
image: https://eptura.com/spaceiq/
layout: provider
mcp_servers:
- description: ''
  name: spaceiq-mcp.yml
  slug: spaceiq-mcpyml
modified: '2026-07-21'
name: SpaceIQ
nav: Providers
network: true
overview: 'SpaceIQ publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Workplace Management, Space Management, Facilities Management, and Desk Booking.


  SpaceIQ''s developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, support, authentication, and 19 more developer resources.'
random_paper: 22
score:
  band: thin
  composite: 32.1
  delta: 0.0
  facets:
    commercial_clarity: 47.4
    contract_quality: 0.0
    developer_ergonomics: 56.0
    discoverability: 75.9
    governance: 3.1
    operational_transparency: 26.3
  previous_composite: 32.1
  provenance:
    conformance: derived
    mcp: derived
    skills: derived
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
security:
- kind: authentication
  name: Spaceiq Authentication
  slug: spaceiq-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Spaceiq Domain Security
  slug: spaceiq-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Spaceiq Vulnerability Disclosure
  slug: spaceiq-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Spaceiq Trust Center
  slug: spaceiq-trust-center
  summary_line: ISO 27001, FedRAMP, GDPR
slug: spaceiq
tags:
- Company
- Workplace Management
- Space Management
- Facilities Management
- Desk Booking
- Hoteling
- Meeting Rooms
- Occupancy Analytics
- Real Estate
- Floorplans
- GraphQL
- IWMS
- Eptura
website: https://eptura.com/spaceiq/
---
