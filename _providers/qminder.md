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
    agentic_access: derived
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: derived
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 49.8
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 41
  human_in_the_loop: 1
  name: Qminder Agentic Access
  operation_count: 53
  slug: qminder-agentic-access
  summary_line: 53 operations · 41 acting · 1 human-in-the-loop
api_count: 7
apis:
- description: Manage scheduled appointments
  name: Qminder Appointments API
  slug: qminder-appointments-api
- description: Manage custom data fields for locations
  name: Qminder Input Fields API
  slug: qminder-input-fields-api
- description: Manage virtual queues within locations
  name: Qminder Lines API
  slug: qminder-lines-api
- description: Manage physical service locations
  name: Qminder Locations API
  slug: qminder-locations-api
- description: Manage visitor queue entries
  name: Qminder Tickets API
  slug: qminder-tickets-api
- description: Manage user accounts and permissions
  name: Qminder Users API
  slug: qminder-users-api
- description: Manage webhook subscriptions
  name: Qminder Webhooks API
  slug: qminder-webhooks-api
artifact_total: 14
asyncapis:
- description: ''
  name: Qminder Events Webhooks
  slug: qminder-events-webhooks
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.qminder.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.qminder.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.qminder.com/api-reference/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.qminder.com/reference/overview
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/qminder-openapi-original.json
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/qminder-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/qminder-authentication.yml
- group: build
  title: ''
  type: SDKs
  url: packages/qminder-packages.yml
- group: build
  title: ''
  type: Packages
  url: packages/qminder-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/qminder-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/qminder-agentic-access.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/qminder-events-webhooks.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/qminder-rate-limits.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/qminder-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/qminder-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/qminder-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/qminder-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.qminder.com/security/
- group: auth
  title: ''
  type: TrustCenter
  url: security/qminder-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/qminder-domain-security.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/qminder-openapi-overlay.yaml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/qminder-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.qminder.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Qminder
- group: company
  title: ''
  type: Blog
  url: https://www.qminder.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://support.qminder.com
- group: commercial
  title: ''
  type: Pricing
  url: https://www.qminder.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://dashboard.qminder.com/signup
- group: start
  title: ''
  type: Login
  url: https://dashboard.qminder.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.qminder.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.qminder.com/privacy-policy/
- group: company
  title: ''
  type: Website
  url: https://www.qminder.com
created: '2026-07-17'
description: Qminder is a cloud-based queue management and appointment scheduling platform that helps retail, healthcare, government, and education organizations manage visitor flow, virtual queues, and service points across physical locations. Its developer platform exposes a REST API and a GraphQL API (with real-time subscriptions) at api.qminder.com for creating tickets, calling and serving visitors, scheduling appointments, managing locations, lines, desks, users, and custom input fields, plus webhooks for ticket, line, and location events. An official JavaScript/TypeScript SDK (qminder-api) is published to npm.
image: https://www.qminder.com/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: qminder-mcp.yml
  slug: qminder-mcpyml
modified: '2026-07-20'
name: Qminder
nav: Providers
network: true
overview: 'Qminder publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Appointments API, Input Fields API, Lines API, and 4 more. Tagged areas include Company, Queue Management, Appointment Scheduling, Visitor Management, and Customer Experience.


  The Qminder catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Qminder''s developer surface includes documentation, API reference, getting-started guide, authentication, engineering blog, support, pricing, and 26 more developer resources.'
random_paper: 41
rate_limits:
- limit_count: 0
  name: Qminder Rate Limits
  slug: qminder-rate-limits
score:
  band: developing
  composite: 55.2
  delta: -1.3
  facets:
    commercial_clarity: 60.5
    contract_quality: 64.6
    developer_ergonomics: 62.5
    discoverability: 81.5
    governance: 20.8
    operational_transparency: 28.9
  previous_composite: 56.5
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: derived
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Qminder Authentication
  slug: qminder-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Qminder Domain Security
  slug: qminder-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Qminder Trust Center
  slug: qminder-trust-center
  summary_line: SOC 2, HIPAA, GDPR
slug: qminder
tags:
- Company
- Queue Management
- Appointment Scheduling
- Visitor Management
- Customer Experience
- REST
- GraphQL
- Webhooks
- SaaS
website: https://www.qminder.com
---
