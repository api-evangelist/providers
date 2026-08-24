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
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 46.7
  scored_at: '2026-08-24'
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
artifact_total: 22
asyncapis:
- description: ''
  name: Qminder Events Webhooks
  slug: qminder-events-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Qminder Appointments API
  slug: open-qminder-appointments-api
- collection_type: open
  name: Qminder Appointments Input Fields API
  slug: open-qminder-input-fields-api
- collection_type: open
  name: Qminder Appointments Lines API
  slug: open-qminder-lines-api
- collection_type: open
  name: Qminder Appointments Locations API
  slug: open-qminder-locations-api
- collection_type: open
  name: Qminder Appointments Tickets API
  slug: open-qminder-tickets-api
- collection_type: open
  name: Qminder Appointments Users API
  slug: open-qminder-users-api
- collection_type: open
  name: Qminder Appointments Webhooks API
  slug: open-qminder-webhooks-api
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
  url: openapi/_original/qminder-openapi-original.json
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
  name: Qminder MCP Server
  slug: qminder-mcp-server
modified: '2026-07-20'
name: Qminder
nav: Providers
network: true
overview: 'Qminder publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Appointments API, Input Fields API, Lines API, and 4 more. Tagged areas include Company, Queue Management, Appointment Scheduling, Visitor Management, and Customer Experience.


  The Qminder catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Qminder''s developer surface includes documentation, API reference, getting-started guide, authentication, engineering blog, support, pricing, and 26 more developer resources.'
random_paper: 17
rate_limits:
- limit_count: 1
  name: Qminder Rate Limits
  slug: qminder-rate-limits
score:
  band: strong
  composite: 56.5
  delta: 0.0
  facets:
    access_clarity: 53.9
    commercial_clarity: 53.9
    contract_governance: 30.3
    contract_quality: 62.2
    developer_ergonomics: 61.3
    discoverability: 81.5
    governance: 30.3
    operational_transparency: 47.4
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
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/qminder/refs/heads/main/screenshots/qminder-2026-08-17T081418.png
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
- Webhook
- Software-as-a-Service
website: https://www.qminder.com
---
