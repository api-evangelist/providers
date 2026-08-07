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
    error_semantics: documented
    event_surface_described: derived
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.0
  scored_at: '2026-08-06'
api_count: 6
apis:
- description: Exchange access/secret keys for an access token.
  name: Airmeet Authentication API
  slug: airmeet-authentication-api
- description: Read events, participants, sessions, engagement and attendance data.
  name: Airmeet Event Details API
  slug: airmeet-event-details-api
- description: Create and manage events, speakers, sessions, booths and landing pages.
  name: Airmeet Manage Event API
  slug: airmeet-manage-event-api
- description: List event series and the events within a series.
  name: Airmeet Manage Event Series API
  slug: airmeet-manage-event-series-api
- description: Add authorized attendees and block or unblock them.
  name: Airmeet Manage Registrations API
  slug: airmeet-manage-registrations-api
- description: Register webhook subscriptions for Airmeet event triggers.
  name: Airmeet Webhooks API
  slug: airmeet-webhooks-api
artifact_total: 18
asyncapis:
- description: Airmeet delivers event engagement and lifecycle notifications via webhooks. Subscribers register a destination URL against a trigger via POST /platform-integration/v1/webhook-register (headers x-acces
  name: Airmeet Webhooks
  slug: airmeet-webhooks-asyncapi
collections:
- collection_type: postman
  name: Airmeet Public Authentication API
  slug: postman-airmeet-authentication-api
- collection_type: postman
  name: Airmeet Public Authentication Event Details API
  slug: postman-airmeet-event-details-api
- collection_type: postman
  name: Airmeet Public Authentication Manage Event API
  slug: postman-airmeet-manage-event-api
- collection_type: postman
  name: Airmeet Public Authentication Manage Event Series API
  slug: postman-airmeet-manage-event-series-api
- collection_type: postman
  name: Airmeet Public Authentication Manage Registrations API
  slug: postman-airmeet-manage-registrations-api
- collection_type: postman
  name: Airmeet Public Authentication Webhooks API
  slug: postman-airmeet-webhooks-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/airmeet/overview
- group: company
  title: ''
  type: Website
  url: https://www.airmeet.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://help.airmeet.com/support/solutions/82000362508
- group: docs
  title: ''
  type: Documentation
  url: https://help.airmeet.com/support/home
- group: docs
  title: ''
  type: APIReference
  url: https://help.airmeet.com/support/solutions/articles/82000467794-airmeet-public-api-introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://help.airmeet.com/support/solutions/articles/82000467794-airmeet-public-api-introduction
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/airmeet-openapi.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/airmeet-webhooks-asyncapi.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/airmeet-webhooks-asyncapi.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/airmeet-openapi-overlay.yaml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/airmeet-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/airmeet-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/airmeet-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/airmeet-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/airmeet-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/airmeet-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.airmeet.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://updates.airmeet.com/en/
- group: design
  title: ''
  type: Conformance
  url: conformance/airmeet-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.airmeet.com/hub/security-and-compliance/
- group: auth
  title: ''
  type: TrustCenter
  url: https://www.airmeet.com/hub/security-and-compliance/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/airmeet-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/airmeet-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.airmeet.com/hub/responsible-disclosure/
- group: operate
  title: ''
  type: Support
  url: https://help.airmeet.com/support/home
- group: company
  title: ''
  type: Blog
  url: https://www.airmeet.com/hub/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.airmeet.com/hub/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://www.airmeet.com/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.airmeet.com/hub/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.airmeet.com/hub/privacy-policy/
created: '2026-07-17'
description: 'Airmeet is a virtual, hybrid and in-person events platform used to run webinars, conferences, summits, meetups, workshops and trade shows with interactive stages, networking lounges, booths, polls, Q&A and engagement analytics. Its Public API lets developers create and manage events (Airmeets), sessions, speakers, booths and event series; manage registrations (add, block and unblock attendees with custom fields); pull engagement and attendance data including polls, questions, UTMs, recordings and replay attendance; and subscribe to 24+ webhook event triggers. Authentication is a two-step flow: exchange an access key and secret key for a 30-day access token, then send it as the X-Airmeet-Access-Token header. The API is served from regional gateways (default Mumbai, EU and US). Airmeet is backed by Accel, Prosus Ventures and Redpoint Ventures.'
image: https://www.airmeet.com/hub/wp-content/uploads/2023/03/Airmeet-Featured-Image.png
layout: provider
mcp_servers:
- description: ''
  name: airmeet-mcp.yml
  slug: airmeet-mcpyml
modified: '2026-07-17'
name: Airmeet
nav: Providers
network: true
overview: 'Airmeet publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Event Details API, Manage Event API, and 3 more. Tagged areas include Company, Cloud Saas, Events, Virtual Events, and Webinars.


  The Airmeet catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Airmeet''s developer surface includes documentation, API reference, getting-started guide, authentication, changelog, support, engineering blog, and 24 more developer resources.'
random_paper: 65
score:
  band: strong
  composite: 60.6
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 72.9
    developer_ergonomics: 60.3
    discoverability: 92.6
    governance: 20.8
    operational_transparency: 50.0
  previous_composite: 60.6
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: derived
    skills: derived
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/airmeet/refs/heads/main/screenshots/airmeet-2026-07-25T195432.png
security:
- kind: authentication
  name: Airmeet Authentication
  slug: airmeet-authentication
  summary_line: apiKey · 5 schemes
- kind: domain-security
  name: Airmeet Domain Security
  slug: airmeet-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Airmeet Vulnerability Disclosure
  slug: airmeet-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Airmeet Trust Center
  slug: airmeet-trust-center
  summary_line: ISO 27001:2022, SOC 2 Type 2
slug: airmeet
tags:
- Company
- Cloud Saas
- Events
- Virtual Events
- Webinars
- Event Management
- Community
- Webhooks
website: https://www.airmeet.com/
---
