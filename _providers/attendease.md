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
  scored_at: '2026-08-03'
api_count: 2
apis:
- description: Organization-level REST API (v2) spanning business units, events, members, attendees, session attendance, check-ins, partners, and contact lists. Authenticated with HMAC-SHA1 request signing (APIAuth)
  name: Attendease Organization API
  slug: attendease-organization-api
- description: Event-scoped REST API bound to a single event subdomain covering event properties, sessions and session instances, presenters, surveys, sponsors, rooms, venues, filters, and content. Authenticated wit
  name: Attendease Event API
  slug: attendease-event-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/attendease-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://eventupplanner.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.attendease.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.attendease.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.attendease.com/
- group: start
  title: ''
  type: SignUp
  url: https://dashboard.attendease.com/
- group: start
  title: ''
  type: Login
  url: https://dashboard.attendease.com/
- group: operate
  title: ''
  type: Support
  url: https://eventupplanner.zendesk.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://eventupplanner.com/blog/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://eventupplanner.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://eventupplanner.com/privacy-policy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/attendease
- group: build
  title: ''
  type: Packages
  url: packages/attendease-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/attendease-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/attendease-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/attendease-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/attendease-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/attendease-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/attendease-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/attendease-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/attendease-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/attendease-llms.txt
- group: design
  title: ''
  type: Components
  url: components/attendease-components.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: 'Attendease (now EventUp Planner, following its acquisition by Tripleseat) is an event and meeting management platform for planning, promoting, and running virtual, in-person, and hybrid events such as conferences, webinars, roadshows, and product launches. Attendease exposes a public developer API in two tiers: an Event API scoped to a single event subdomain (attendee tokens, sessions, presenters, surveys, sponsors, rooms, venues, and content) and an Organization API (`/api/v2/`) that spans business units, events, members, attendees, session attendance, check-ins, partners, and contact lists. The Organization API is authenticated with HMAC-SHA1 request signing (`Authorization: APIAuth access_key:signature`) while the Event API uses attendee/event tokens and HTTP Basic auth. First-party JavaScript and Ruby SDKs plus a Jekyll plugin are published to npm and RubyGems.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/attendease.png
layout: provider
mcp_servers:
- description: ''
  name: attendease-mcp.yml
  slug: attendease-mcpyml
modified: '2026-07-18'
name: Attendease
nav: Providers
network: true
overview: 'Attendease publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Events, Event Management, Event Marketing, and Conferences.


  Attendease''s developer surface includes documentation, API reference, signup flow, support, engineering blog, authentication, and 18 more developer resources.'
random_paper: 9
score:
  band: emerging
  composite: 25.8
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 0.0
    developer_ergonomics: 51.6
    discoverability: 75.9
    governance: 3.1
    operational_transparency: 5.3
  previous_composite: 25.8
  provenance:
    conformance: derived
    mcp: derived
    skills: derived
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/attendease/refs/heads/main/screenshots/attendease-2026-07-25T201628.png
security:
- kind: authentication
  name: Attendease Authentication
  slug: attendease-authentication
  summary_line: 4 schemes
- kind: domain-security
  name: Attendease Domain Security
  slug: attendease-domain-security
  summary_line: TLSv1.3 · DMARC
slug: attendease
tags:
- Company
- Events
- Event Management
- Event Marketing
- Conferences
- Webinars
- Attendees
- Registration
- SaaS
website: https://eventupplanner.com
---
