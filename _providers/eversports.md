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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.2
  scored_at: '2026-09-01'
api_count: 2
apis:
- description: Read-only GraphQL API serving a venue's activity schedules — classes, trainings, workshops, courses, events, retreats, camps, and educations — with venue, teacher, room, sport, and availability detail
  name: Eversports Provider API
  slug: eversports-provider-api
- description: GraphQL API for aggregator partners exposing venues, classes, sessions, and reservations, plus mutations to make, cancel, and check in reservations. Separate test and production hosts. Bearer auth, Re
  name: Eversports Aggregator API
  slug: eversports-aggregator-api
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://www.eversports.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://aggregator.eversports.io/
- group: docs
  title: ''
  type: Documentation
  url: https://helpcenter.eversportsmanager.com/what-is-the-provider-api
- group: operate
  title: ''
  type: Support
  url: https://helpcenter.eversportsmanager.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/eversport
- group: commercial
  title: ''
  type: Pricing
  url: https://www.eversportsmanager.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.eversportsmanager.com/demo
- group: start
  title: ''
  type: Login
  url: https://app.eversportsmanager.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.eversportsmanager.com/gtc
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.eversportsmanager.com/privacy-policy
- group: auth
  title: ''
  type: Authentication
  url: authentication/eversports-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/eversports-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/eversports-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/eversports-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/eversports-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/eversports-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/eversports-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/eversports-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/eversports-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/eversports-domain-security.yml
created: '2026-07-17'
description: 'Eversports is a European sports and fitness platform that lets consumers discover and book classes, courts, and memberships across studios, gyms, and clubs, and gives those businesses a back-office management suite (Eversports Manager) for scheduling, bookings, payments, and customer management. Eversports Manager exposes two public GraphQL APIs: a read-only Provider API that serves a venue''s activity schedules (classes, trainings, workshops, courses, events, retreats, camps, educations) with venue, teacher, room, sport, and availability detail; and an Aggregator API that exposes venues, classes, sessions, and reservations plus mutations to make, cancel, and check in reservations for aggregator partners. Both APIs authenticate with a Bearer token issued by Eversports and use Relay-style cursor pagination.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/eversports.png
layout: provider
mcp_servers:
- description: ''
  name: Eversports MCP Server
  slug: eversports-mcp-server
modified: '2026-07-19'
name: Eversports
nav: Providers
network: true
overview: 'Eversports publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Sports, Fitness, Booking, and Scheduling.


  Eversports'' developer surface includes documentation, support, pricing, signup flow, authentication, sandbox, and 15 more developer resources.'
random_paper: 4
score:
  band: thin
  composite: 35.6
  coverage:
    artifact_dirs: 13
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 4.5
    contract_quality: 37.2
    developer_ergonomics: 44.6
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 2.6
  previous_composite: 35.6
  provenance:
    conformance: derived
    mcp: derived
    skills: derived
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/eversports/refs/heads/main/screenshots/eversports-2026-07-25T213739.png
security:
- kind: authentication
  name: Eversports Authentication
  slug: eversports-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Eversports Domain Security
  slug: eversports-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: eversports
tags:
- Company
- Sports
- Fitness
- Booking
- Scheduling
- Wellness
- GraphQL
- Reservations
- Event
website: https://www.eversports.com
---
