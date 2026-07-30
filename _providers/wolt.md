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
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    asyncapi_events: true
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: documented
    idempotency: documented
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 48.4
  scored_at: '2026-07-28'
api_count: 2
apis:
- description: 'On-demand last-mile delivery: generate binding shipment promises (price + ETA), create deliveries, calculate venueless delivery fees, cancel before courier acceptance, retrieve handshake PINs, and rec'
  name: Wolt Drive API
  slug: wolt-drive-api
- description: 'Receive and fulfill consumer marketplace orders in a POS/in-store system: accept, reject, mark ready, mark delivered, refund items or basket, and handle preorders and group orders.'
  name: Wolt Order / Marketplace API
  slug: wolt-order-marketplace-api
artifact_total: 8
asyncapis:
- description: ''
  name: Wolt Webhooks
  slug: wolt-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://wolt.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.wolt.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.wolt.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://developer.wolt.com/docs/api
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.wolt.com/docs/getting-started/restaurant
- group: operate
  title: ''
  type: Support
  url: https://developer.wolt.com/docs/faq
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/woltapp
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.wolt.com/docs/changelog
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/wolt-changelog.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/wolt-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/wolt-scopes.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/wolt-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/wolt-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/wolt-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/wolt-lifecycle.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/wolt-webhooks.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/wolt-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/wolt-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/wolt-conformance.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/wolt-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/wolt-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/wolt-security.txt
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/wolt-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://app.intigriti.com/programs/wolt/wolt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/wolt-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/wolt-llms.txt
created: '2026-07-17'
description: 'Wolt is a marketplace and last-mile delivery platform (part of DoorDash) operating across Europe and beyond. Its developer surface exposes two production APIs: the Order / Marketplace API, which delivers consumer orders into a merchant POS or in-store system and drives them through accept, ready, and delivered states with refunds and group-order support; and the Wolt Drive API, which provides on-demand last-mile delivery via shipment promises, delivery creation, courier tracking, and webhooks. Authentication is OAuth 2.0 issuing one-hour bearer JWTs (Wolt Drive uses a Merchant Key bearer token), with HMAC-SHA256 / HS256-JWT signed webhooks for order and delivery lifecycle events.'
image: https://wolt.com/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: wolt-mcp.yml
  slug: wolt-mcpyml
modified: '2026-07-21'
name: Wolt
nav: Providers
network: true
overview: 'Wolt publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Marketplace, Food Delivery, Last Mile Delivery, and Logistics.


  The Wolt catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Wolt''s developer surface includes documentation, API reference, getting-started guide, support, changelog, authentication, sandbox, and 20 more developer resources.'
random_paper: 44
scopes:
- name: Wolt Scopes
  scope_count: 1
  slug: wolt-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: thin
  composite: 40.3
  delta: 5.9
  facets:
    commercial_clarity: 0.0
    contract_quality: 51.6
    developer_ergonomics: 60.3
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 39.5
  previous_composite: 34.4
  provenance:
    conformance: first-party
    mcp: derived
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: rising
security:
- kind: authentication
  name: Wolt Authentication
  slug: wolt-authentication
  summary_line: oauth2/http · 2 schemes
- kind: domain-security
  name: Wolt Domain Security
  slug: wolt-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Wolt Vulnerability Disclosure
  slug: wolt-vulnerability-disclosure
  summary_line: Intigriti · security.txt · contact published
slug: wolt
tags:
- Company
- Marketplace
- Food Delivery
- Last Mile Delivery
- Logistics
- Webhooks
- OAuth
- Point of Sale
website: https://wolt.com
---
