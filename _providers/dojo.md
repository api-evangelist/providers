---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: verified
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 35.7
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 52
  human_in_the_loop: 0
  name: Dojo Agentic Access
  operation_count: 75
  slug: dojo-agentic-access
  summary_line: 75 operations · 52 acting
api_count: 5
apis:
- baseURL: https://api.dojo.tech
  baseurl_source: declared
  description: The Areas API from Dojo — 1 operation(s) for areas.
  name: Dojo Areas API
  slug: dojo-areas-api
- baseURL: https://api.dojo.tech
  baseurl_source: declared
  description: Register your REST and WebSockets endpoints.
  name: Dojo Capabilities API
  slug: dojo-capabilities-api
- baseURL: https://api.dojo.tech
  baseurl_source: declared
  description: 'Allows you to capture the full payment amount or part of the amount. **Documentation**: [Captures](../../payments/manage-payments/capture)'
  name: Dojo Captures API
  slug: dojo-captures-api
- baseURL: https://api.dojo.tech
  baseurl_source: declared
  description: Allows to create and manage a customer of your business.
  name: Dojo Customers API
  slug: dojo-customers-api
- baseURL: https://api.dojo.tech
  baseurl_source: declared
  description: The Events API from Dojo — 1 operation(s) for events.
  name: Dojo Events API
  slug: dojo-events-api
- baseURL: https://api.dojo.tech
  baseurl_source: declared
  description: The Flows API from Dojo — 2 operation(s) for flows.
  name: Dojo Flows API
  slug: dojo-flows-api
- baseURL: https://api.dojo.tech
  baseurl_source: declared
  description: The Orders API from Dojo — 7 operation(s) for orders.
  name: Dojo Orders API
  slug: dojo-orders-api
- baseURL: https://api.dojo.tech
  baseurl_source: declared
  description: The Parties API from Dojo — 3 operation(s) for parties.
  name: Dojo Parties API
  slug: dojo-parties-api
- baseURL: https://api.dojo.tech
  baseurl_source: declared
  description: 'Allows you to take and manage payments. **Documentation**: [Payment intents](../../payments/manage-payments/payment-intent)'
  name: Dojo Payment intents API
  slug: dojo-payment-intents-api
- baseURL: https://api.dojo.tech
  baseurl_source: declared
  description: 'Allows you to create a refund for a captured payment. **Documentation**: [Refunds](/payments/manage-payments/cancelling-payments/refund)'
  name: Dojo Refunds API
  slug: dojo-refunds-api
- baseURL: https://api.dojo.tech
  baseurl_source: declared
  description: The Reservations API from Dojo — 3 operation(s) for reservations.
  name: Dojo Reservations API
  slug: dojo-reservations-api
- baseURL: https://api.dojo.tech
  baseurl_source: declared
  description: 'Allows you to create a reversal for payments. **Documentation**: [Reversal](../../payments/manage-payments/cancelling-payments/reversal)'
  name: Dojo Reversal API
  slug: dojo-reversal-api
- baseURL: https://api.dojo.tech
  baseurl_source: declared
  description: 'Allows you to setup a card for future payments. **Documentation**: [Setup intent](../payments/manage-payments/setup-intent)'
  name: Dojo Setup intents API
  slug: dojo-setup-intents-api
- baseURL: https://api.dojo.tech
  baseurl_source: declared
  description: The Tables API from Dojo — 1 operation(s) for tables.
  name: Dojo Tables API
  slug: dojo-tables-api
- baseURL: https://api.dojo.tech
  baseurl_source: declared
  description: Allows you to create a terminal secret value.
  name: Dojo Tap to Pay on iPhone API
  slug: dojo-tap-to-pay-on-iphone-api
- baseURL: https://api.dojo.tech
  baseurl_source: declared
  description: Allows you to manage sessions on the terminal.
  name: Dojo Terminal sessions API
  slug: dojo-terminal-sessions-api
- baseURL: https://api.dojo.tech
  baseurl_source: declared
  description: 'Allows you to manage payments on the terminal. **Documentation**: [Terminals](../payments/accept-payments/in-person-payments/pay-at-counter/terminals)'
  name: Dojo Terminals API
  slug: dojo-terminals-api
- baseURL: https://api.dojo.tech
  baseurl_source: declared
  description: Allows you to take and manage payments.
  name: Dojo Transactions API
  slug: dojo-transactions-api
- baseURL: https://api.dojo.tech
  baseurl_source: declared
  description: 'Webhooks notify you when a specific event has occurred. **Documentation**: [Webhooks](../../development-resources/webhooks)'
  name: Dojo Webhooks API
  slug: dojo-webhooks-api
artifact_total: 30
asyncapis:
- description: 'The Async Websocket API to enable Dojo integrated products. Core modules: - Tables - Areas - Orders - Parties - Reservations API modules can generally be implemented independently, with a small number'
  name: EPOS Data API (WebSockets)
  slug: dojo-epos-data-asyncapi
collections:
- collection_type: open
  name: Dojo API
  slug: open-dojo-api
- collection_type: open
  name: EPOS Data API (REST)
  slug: open-dojo-epos-data-api
- collection_type: open
  name: EPOS Tester
  slug: open-dojo-epos-tester-tool-api
- collection_type: open
  name: Tap to Pay on iPhone
  slug: open-dojo-tap-to-pay-on-iphone-api
- collection_type: open
  name: Transaction API
  slug: open-dojo-transactions-api
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
  name: Dojo MCP Server
  slug: dojo-mcp-server
modified: '2026-07-24'
name: Dojo
nav: Providers
network: true
overview: 'Dojo publishes 19 APIs on the [APIs.io](https://apis.io/) network, including Areas API, Capabilities API, Captures API, and 16 more. Tagged areas include Payments, United Kingdom, Payment Gateway, Payment Processing, and Acquiring.


  The Dojo catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Dojo''s developer surface includes authentication, documentation, API reference, getting-started guide, changelog, sandbox, engineering blog, and 31 more developer resources.'
random_paper: 8
score:
  band: developing
  composite: 54.2
  coverage:
    artifact_dirs: 21
    catalog_gap: 75.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 38.2
    commercial_clarity: 38.2
    contract_governance: 4.5
    contract_quality: 65.4
    developer_ergonomics: 61.3
    discoverability: 81.5
    governance: 4.5
    operational_transparency: 52.6
  previous_composite: 54.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 68.4
      derived: 0
      marker_coverage: 0.0
      total: 19
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 48.4
  schema_version: 0.18.0
  scored_at: '2026-09-02'
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
- Point-of-Sale
- Webhook
website: https://dojo.tech/
---
