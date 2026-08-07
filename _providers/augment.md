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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: derived
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 50.2
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 15
  human_in_the_loop: 0
  name: Augment Agentic Access
  operation_count: 23
  slug: augment-agentic-access
  summary_line: 23 operations · 15 acting
api_count: 6
apis:
- description: API key based authorization. Please refer to the [authorization documentation](docs/authorization.md) for details.
  name: Augment API Key API
  slug: augment-api-key-api
- description: API endpoints for managing carriers, carrier contacts, and carrier-manager relationships.
  name: Augment Carrier Management API
  slug: augment-carrier-management-api
- description: Public API endpoints for correlating carrier issues (detention, lumper, TONU, etc.) with the matching incidents in your TMS. Access is gated by brokerage; talk to Augment before using these endpoints.
  name: Augment Carrier Support API
  slug: augment-carrier-support-api
- description: API endpoints for creating, updating, and retrieving loads.
  name: Augment Load Management API
  slug: augment-load-management-api
- description: Public API endpoints for approved brokerages to create, update, list, and delete webhook endpoints. Self-service endpoints send version 2 webhook payloads only. Access is gated by brokerage; talk to A
  name: Augment Webhook Endpoints API
  slug: augment-webhook-endpoints-api
- description: Public API endpoints for approved brokerages to list supported webhook event types, subscribe endpoints to event types, and send test deliveries. Subscriptions created through these public APIs delive
  name: Augment Webhook Event Subscriptions API
  slug: augment-webhook-event-subscriptions-api
artifact_total: 13
asyncapis:
- description: ''
  name: Augment Webhooks
  slug: augment-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://goaugment.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://apidocs.goaugment.com/
- group: docs
  title: ''
  type: Documentation
  url: https://apidocs.goaugment.com/
- group: docs
  title: ''
  type: APIReference
  url: https://apidocs.goaugment.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://apidocs.goaugment.com/guide/start-developing/authorization/
- group: company
  title: ''
  type: Blog
  url: https://www.goaugment.com/blog
- group: start
  title: ''
  type: Login
  url: https://app.goaugment.com/
- group: start
  title: ''
  type: SignUp
  url: https://www.goaugment.com/get-a-demo
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.goaugment.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.goaugment.com/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/goaugment
- group: auth
  title: ''
  type: Authentication
  url: authentication/augment-authentication.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/augment-openapi-original.json
- group: other
  title: ''
  type: Overlay
  url: overlays/augment-openapi-overlay.yaml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/augment-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/augment-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/augment-agentic-access.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/augment-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/augment-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/augment-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://apidocs.goaugment.com/guide/start-developing/migration-guide
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/augment-rate-limits.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/augment-webhooks.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/augment-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/augment-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.goaugment.com/
- group: auth
  title: ''
  type: TrustCenter
  url: security/augment-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/augment-domain-security.yml
created: '2026-07-17'
description: Augment (Augie) is an AI productivity platform for the freight and logistics industry, automating complex supply-chain workflows for brokerages, carriers, and distributors — quoting, booking, load building, capacity sourcing, track & trace, carrier support, and order-to-cash — while integrating with existing TMS, ERP, email, and messaging systems. Its public REST API (api.prod.goaugment.com) lets partner systems manage loads and route stops, upsert and archive carriers, post tracking events, report carrier issues, and configure webhook endpoints and event subscriptions across nine event types. Authentication is HTTP Basic with an API key; the company is SOC 2 Type II certified. Augment is backed by 8VC, Lightspeed Venture Partners, and Redpoint Ventures.
image: https://framerusercontent.com/assets/hYTkXfUxYj558HcJLnhl8l2ogig.png
layout: provider
mcp_servers:
- description: ''
  name: augment-mcp.yml
  slug: augment-mcpyml
modified: '2026-07-18'
name: Augment
nav: Providers
network: true
overview: 'Augment publishes 6 APIs on the [APIs.io](https://apis.io/) network, including API Key API, Carrier Management API, Carrier Support API, and 3 more. Tagged areas include Company, Logistics, Freight, Supply Chain, and Transportation.


  The Augment catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Augment''s developer surface includes documentation, API reference, getting-started guide, engineering blog, signup flow, authentication, and 23 more developer resources.'
random_paper: 75
rate_limits:
- limit_count: 2
  name: Augment Rate Limits
  slug: augment-rate-limits
score:
  band: developing
  composite: 54.5
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 72.1
    developer_ergonomics: 51.6
    discoverability: 81.5
    governance: 20.8
    operational_transparency: 42.1
  previous_composite: 54.5
  provenance:
    agentic_access: derived
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
screenshot: https://raw.githubusercontent.com/api-evangelist/augment/refs/heads/main/screenshots/augment-2026-07-25T201709.png
security:
- kind: authentication
  name: Augment Authentication
  slug: augment-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Augment Domain Security
  slug: augment-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Augment Trust Center
  slug: augment-trust-center
  summary_line: SOC 2, GDPR
slug: augment
tags:
- Company
- Logistics
- Freight
- Supply Chain
- Transportation
- Webhooks
- Artificial Intelligence
- Automation
website: https://goaugment.com
---
