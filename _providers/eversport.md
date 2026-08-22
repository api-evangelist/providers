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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.0
  scored_at: '2026-08-19'
api_count: 2
apis:
- description: Read-only GraphQL API exposing activity schedules (classes, courses, workshops, trainings, events, camps, retreats, educations), activity groups, venues, companies, teachers, and per-activity checkout
  name: Eversports Provider API
  slug: eversports-provider-api
- description: Legacy JSON:API REST integration API used by aggregator and partner systems to manage users, venues, courts, and orders on the Eversports platform. Requests and responses follow the jsonapi.org format
  name: Eversports Integration API (v2)
  slug: eversports-integration-api-v2
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://www.eversports.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://helpcenter.eversportsmanager.com/what-is-the-provider-api
- group: docs
  title: ''
  type: Documentation
  url: https://helpcenter.eversportsmanager.com/what-is-the-provider-api
- group: docs
  title: ''
  type: APIReference
  url: https://provider-api.eversportsmanager.io/api/graphql
- group: operate
  title: ''
  type: HelpCenter
  url: https://helpcenter.eversportsmanager.com/
- group: operate
  title: ''
  type: Support
  url: mailto:support@eversports.com
- group: commercial
  title: ''
  type: Pricing
  url: https://helpcenter.eversportsmanager.com/what-is-the-provider-api
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/eversport
- group: docs
  title: ''
  type: GraphQL
  url: graphql/eversport-provider-api.graphql
- group: auth
  title: ''
  type: Authentication
  url: authentication/eversport-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/eversport-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/eversport-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/eversport-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/eversport-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/eversport-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/eversport-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/eversport-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/eversport-domain-security.yml
created: '2026-07-17'
description: Eversports is a European sports and fitness activity platform founded in 2013 and headquartered in Vienna, Austria. Its consumer marketplace lets people discover, book, and pay for classes, courts, and memberships across yoga, pilates, tennis, badminton, climbing and more, while Eversports Manager is the studio-management SaaS that venues use to run schedules, bookings, memberships, and payments. The platform facilitates roughly 1.5 million bookings per month for more than 4,000 active sport providers and 500,000 monthly active users. For developers, Eversports exposes a read-only GraphQL Provider API surfacing activity schedules, venues, teachers, and per-activity checkout links for integrated Eversports Manager venues, plus a legacy JSON:API REST integration API for users, venues, courts, and orders, and aggregator integrations with Urban Sports Club, Wellhub, ClassPass, EGYM Wellpass, and others.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/eversport.png
layout: provider
mcp_servers:
- description: ''
  name: eversport-mcp.yml
  slug: eversport-mcpyml
modified: '2026-07-19'
name: Eversports
nav: Providers
network: true
overview: 'Eversports publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Sports, Fitness, Booking, and Scheduling.


  Eversports'' developer surface includes documentation, API reference, support, pricing, authentication, and 14 more developer resources.'
random_paper: 15
score:
  band: thin
  composite: 30.3
  delta: -1.1
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 4.5
    contract_quality: 43.3
    developer_ergonomics: 44.6
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 2.6
  previous_composite: 31.4
  provenance:
    conformance: derived
    mcp: derived
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/eversport/refs/heads/main/screenshots/eversport-2026-07-25T213737.png
security:
- kind: authentication
  name: Eversport Authentication
  slug: eversport-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Eversport Domain Security
  slug: eversport-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: eversport
tags:
- Company
- Sports
- Fitness
- Booking
- Scheduling
- Wellness
- Marketplace
- GraphQL
- Reservations
- Studio Management
- Events
website: https://www.eversports.com/
---
