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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 8.8
  scored_at: '2026-09-02'
api_count: 2
apis:
- description: Organization-level REST API (v2) spanning business units, events, members, attendees, session attendance, check-ins, partners, and contact lists. Authenticated with HMAC-SHA1 request signing (APIAuth)
  name: Attendease Organization API
  slug: attendease-organization-api
- description: Event-scoped REST API bound to a single event subdomain covering event properties, sessions and session instances, presenters, surveys, sponsors, rooms, venues, filters, and content. Authenticated wit
  name: Attendease Event API
  slug: attendease-event-api
artifact_total: 7
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
- group: commercial
  title: ''
  type: Plans
  url: plans/attendease-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/attendease-rate-limits.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/attendease-conformance.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://eventupplanner.com/plans-and-pricing/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.attendease.com/
- group: other
  title: ''
  type: Accessibility
  url: https://eventupplanner.com/accessibility/
- group: operate
  title: ''
  type: HelpCenter
  url: https://eventupplanner.zendesk.com/hc/en-us
- group: commercial
  title: ''
  type: ServicesAgreement
  url: https://eventupplanner.com/services-agreement/
created: '2026-07-17'
description: 'Attendease (now EventUp Planner, following its acquisition by Tripleseat) is an event and meeting management platform for planning, promoting, and running virtual, in-person, and hybrid events such as conferences, webinars, roadshows, and product launches. Attendease exposes a public developer API in two tiers: an Event API scoped to a single event subdomain (attendee tokens, sessions, presenters, surveys, sponsors, rooms, venues, and content) and an Organization API (`/api/v2/`) that spans business units, events, members, attendees, session attendance, check-ins, partners, and contact lists. The Organization API is authenticated with HMAC-SHA1 request signing (`Authorization: APIAuth access_key:signature`) while the Event API uses attendee/event tokens and HTTP Basic auth. First-party JavaScript and Ruby SDKs plus a Jekyll plugin are published to npm and RubyGems.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/attendease.png
layout: provider
mcp_servers:
- description: ''
  name: Attendease MCP Server
  slug: attendease-mcp-server
modified: '2026-08-13'
name: Attendease
nav: Providers
network: true
overview: 'Attendease publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Event, Event Management, Event Marketing, and Conferences.


  Attendease''s developer surface includes documentation, API reference, signup flow, support, engineering blog, authentication, pricing, and 25 more developer resources.'
plans:
- name: Attendease Plans Pricing
  plan_count: 3
  slug: attendease-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 1
  name: Attendease Rate Limits
  slug: attendease-rate-limits
score:
  band: thin
  composite: 36.0
  coverage:
    artifact_dirs: 17
    catalog_gap: 58.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 77.6
    commercial_clarity: 77.6
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 28.0
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 39.5
  previous_composite: 36.0
  provenance:
    conformance: first-party
    mcp: derived
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-02'
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
- Event
- Event Management
- Event Marketing
- Conferences
- Webinars
- Attendees
- Registration
- Software-as-a-Service
website: https://eventupplanner.com
---
