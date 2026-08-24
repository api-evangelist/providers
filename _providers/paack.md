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
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.5
  scored_at: '2026-08-24'
api_count: 1
apis:
- description: 'REST API for creating and managing parcel delivery orders, generating shipping labels, checking delivery coverage, retrieving proof of delivery, and consuming real-time tracking events. Authenticated '
  name: Paack API
  slug: paack-api
artifact_total: 5
asyncapis:
- description: ''
  name: Paack Webhooks
  slug: paack-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/paack-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/paack-authentication.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/paack-webhooks.yml
- group: build
  title: ''
  type: Packages
  url: packages/paack-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/paack-packages.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/paack-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/paack-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/paack-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/paack-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/paack-conformance.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/paack-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/paack-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/paack-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/paack-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/paack-llms.txt
- group: company
  title: ''
  type: Website
  url: https://paack.co/
- group: start
  title: ''
  type: Portal
  url: https://paack.readme.io/
- group: docs
  title: ''
  type: Documentation
  url: https://paack.readme.io/docs/start-intro
- group: docs
  title: ''
  type: APIReference
  url: https://paack.readme.io/reference/token
- group: start
  title: ''
  type: GettingStarted
  url: https://paack.readme.io/docs/start-integration
- group: operate
  title: ''
  type: Support
  url: https://help.paack.co/en/support/home
- group: company
  title: ''
  type: Blog
  url: https://paack.co/blog/
- group: operate
  title: ''
  type: ChangeLog
  url: https://paack.readme.io/changelog/welcome-to-paack
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/paacklogistics/paack-apis/collection/p93tvmy/paack-api-systems
- group: commercial
  title: ''
  type: TermsOfService
  url: https://paack.co/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://paack.co/privacy-policy/
created: '2026-07-17'
description: Paack is a technology-driven last-mile parcel delivery company serving e-commerce retailers across Spain, Portugal, the United Kingdom, France and Italy. Founded in 2015 and headquartered in Barcelona, Paack provides scheduled, precise home delivery, returns and reverse logistics, real-time parcel tracking, and proof of delivery. Its developer platform exposes REST APIs for order creation and management, label generation, delivery coverage and postcode-zone lookup, and real-time tracking events, complemented by webhooks for event notifications and an sFTP batch integration. APIs are authenticated with Auth0 OAuth2 client-credentials JSON Web Tokens and documented on a ReadMe developer hub with staging and production environments.
image: https://files.readme.io/005f576-small-Logo_paack_negativo.png
layout: provider
mcp_servers:
- description: ''
  name: Paack MCP Server
  slug: paack-mcp-server
modified: '2026-07-20'
name: Paack
nav: Providers
network: true
overview: 'Paack publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Logistics, Last Mile Delivery, Parcel Delivery, and E-Commerce.


  The Paack catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Paack''s developer surface includes authentication, changelog, sandbox, developer portal, documentation, API reference, getting-started guide, and 19 more developer resources.'
random_paper: 8
score:
  band: thin
  composite: 37.6
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 45.1
    developer_ergonomics: 51.2
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 15.8
  previous_composite: 37.6
  provenance:
    conformance: first-party
    mcp: derived
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/paack/refs/heads/main/screenshots/paack-2026-08-07T191232.png
security:
- kind: authentication
  name: Paack Authentication
  slug: paack-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Paack Domain Security
  slug: paack-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: paack
tags:
- Company
- Logistics
- Last Mile Delivery
- Parcel Delivery
- E-Commerce
- Shipping
- Fulfillment
- Tracking
- Reverse Logistics
website: https://paack.co/
---
