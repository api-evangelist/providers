---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: verified
    mcp_server: derived
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 51.1
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 52
  human_in_the_loop: 0
  name: Dojo Agentic Access
  operation_count: 75
  slug: dojo-agentic-access
  summary_line: 75 operations · 52 acting
api_count: 5
apis:
- description: 'Dojo''s core REST payments API for accepting and managing card payments. Covers payment intents, refunds, reversals, captures, customers, setup intents, terminals, terminal sessions, capabilities, and '
  name: Dojo API
  slug: dojo-api
- description: Retrieves transaction records for a merchant. Documented REST endpoint under https://api.dojo.tech for querying processed card transactions. Version 2023-11-12.
  name: Dojo Transaction API
  slug: dojo-transactions-api
- description: A REST contract that a merchant's EPOS (point-of-sale) system implements so Dojo can read orders, tables, areas, parties, and reservations for hospitality integrations. The server is merchant-hosted (
  name: Dojo EPOS Data API
  slug: dojo-epos-data-api
- description: API supporting Dojo's Tap to Pay on iPhone in-person acceptance flow, documented under https://api.dojo.tech. Version 2023-12-12.
  name: Dojo Tap to Pay on iPhone API
  slug: dojo-tap-to-pay-on-iphone-api
- description: A small helper API for the Dojo EPOS Tester tool, used to validate an EPOS integration against Dojo's EPOS Data contract. Version 1.0.0 (2 paths).
  name: Dojo EPOS Tester Tool API
  slug: dojo-epos-tester-tool-api
artifact_total: 11
asyncapis:
- description: 'The Async Websocket API to enable Dojo integrated products. Core modules: - Tables - Areas - Orders - Parties - Reservations API modules can generally be implemented independently, with a small number'
  name: EPOS Data API (WebSockets)
  slug: dojo-epos-data-asyncapi
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/dojo-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/dojo-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dojo-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/dojo-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://dojo.tech/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.dojo.tech
- group: docs
  title: ''
  type: Documentation
  url: https://docs.dojo.tech/docs
- group: docs
  title: ''
  type: APIReference
  url: https://docs.dojo.tech/api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.dojo.tech/get-started
- group: build
  title: ''
  type: Postman
  url: https://docs.dojo.tech/development-resources/postman
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.dojo.tech/changelog
- group: operate
  title: ''
  type: StatusPage
  url: https://status.dojo.tech
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/dojo-engineering
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/dojo-tech
- group: build
  title: ''
  type: SDKs
  url: packages/dojo-packages.yml
- group: build
  title: ''
  type: Packages
  url: packages/dojo-packages.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/dojo-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/dojo-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/dojo-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/dojo-lifecycle.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/dojo-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/dojo-api-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/dojo-conformance.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/dojo-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/dojo-data-model.yml
- group: design
  title: ''
  type: Components
  url: components/dojo-components.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/dojo-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/dojo-epos-data-asyncapi.yml
- group: auth
  title: ''
  type: Security
  url: security/dojo-vulnerability-disclosure.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/dojo-changelog.yml
- group: company
  title: ''
  type: Blog
  url: https://dojo.tech/blog/
- group: operate
  title: ''
  type: Support
  url: https://support.dojo.tech/hc/en-gb
- group: start
  title: ''
  type: SignUp
  url: https://developer.dojo.tech/signup
- group: start
  title: ''
  type: Login
  url: https://developer.dojo.tech/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://docs.dojo.tech/development-resources/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dojo.tech/legal/privacy-policy/
- group: commercial
  title: ''
  type: Pricing
  url: https://dojo.tech/pricing/
created: '2026-07-24'
description: Dojo is a United Kingdom payments company (Paymentsense trading as Dojo, headquartered in London) that provides card acquiring and payment processing for in-person, online, and omnichannel merchants. It combines Dojo card machines and terminals, a payment gateway, and merchant tooling (bookings, EPOS integrations, business banking-style accounts) into a single acquirer-processor stack aimed at UK small and mid-market businesses and hospitality. Dojo is genuinely API-native and publishes a public developer portal at docs.dojo.tech with a REST API for payment intents, customers, refunds, captures, terminals, and webhooks, alongside separate specs for transactions, EPOS data ingestion, and Tap to Pay on iPhone. Authentication is a secret API key sent in the Authorization header (sandbox sk_sandbox_ and production sk_prod_ prefixes), and the platform supports webhook event subscriptions. Positioned within the UK's dense card-acquiring and PSP cluster alongside players like Checkout.com
  and SumUp.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
mcp_servers:
- description: ''
  name: dojo-mcp.yml
  slug: dojo-mcpyml
modified: '2026-07-24'
name: Dojo
nav: Providers
network: true
overview: 'Dojo publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Transaction API, EPOS Data API, and 3 more. Tagged areas include Payments, United Kingdom, Payment Gateway, Payment Processing, and Acquiring.


  The Dojo catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Dojo''s developer surface includes authentication, documentation, API reference, getting-started guide, changelog, sandbox, engineering blog, and 31 more developer resources.'
random_paper: 80
score:
  band: developing
  composite: 54.2
  delta: 0.0
  facets:
    commercial_clarity: 44.7
    contract_quality: 62.9
    developer_ergonomics: 73.4
    discoverability: 83.3
    governance: 11.5
    operational_transparency: 47.4
  previous_composite: 54.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 60.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 48.4
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dojo/refs/heads/main/screenshots/dojo-2026-07-25T212236.png
security:
- kind: authentication
  name: Dojo Authentication
  slug: dojo-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Dojo Domain Security
  slug: dojo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Dojo Vulnerability Disclosure
  slug: dojo-vulnerability-disclosure
  summary_line: disclosure policy published
slug: dojo
tags:
- Payments
- United Kingdom
- Payment Gateway
- Payment Processing
- Acquiring
- Card Payments
- In-Person Payments
- Terminals
- Point of Sale
- Webhooks
website: https://dojo.tech/
---
