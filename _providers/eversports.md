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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.7
  scored_at: '2026-07-28'
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
  name: eversports-mcp.yml
  slug: eversports-mcpyml
modified: '2026-07-19'
name: Eversports
nav: Providers
network: true
overview: 'Eversports publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Sports, Fitness, Booking, and Scheduling.


  Eversports'' developer surface includes documentation, support, pricing, signup flow, authentication, sandbox, and 15 more developer resources.'
random_paper: 77
score:
  band: thin
  composite: 37.0
  delta: 7.3
  facets:
    commercial_clarity: 44.7
    contract_quality: 43.2
    developer_ergonomics: 42.9
    discoverability: 75.9
    governance: 3.1
    operational_transparency: 5.3
  previous_composite: 29.7
  provenance:
    conformance: derived
    mcp: derived
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: rising
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
- Events
website: https://www.eversports.com
---
