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
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: true
    idempotency: documented
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 51.4
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 63
  human_in_the_loop: 1
  name: Shift4 Agentic Access
  operation_count: 72
  slug: shift4-agentic-access
  summary_line: 72 operations · 63 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.shift4api.net/api/rest/v1
  baseurl_source: declared
  description: The 3D Secure API from Shift4 — 2 operation(s) for 3d secure.
  name: Shift4 3D Secure API
  slug: shift4-3d-secure-api
- baseURL: https://api.shift4api.net/api/rest/v1
  baseurl_source: declared
  description: The ACH API from Shift4 — 5 operation(s) for ach.
  name: Shift4 ACH API
  slug: shift4-ach-api
- baseURL: https://api.shift4api.net/api/rest/v1
  baseurl_source: declared
  description: The Batches API from Shift4 — 1 operation(s) for batches.
  name: Shift4 Batches API
  slug: shift4-batches-api
- baseURL: https://api.shift4api.net/api/rest/v1
  baseurl_source: declared
  description: The Cards API from Shift4 — 2 operation(s) for cards.
  name: Shift4 Cards API
  slug: shift4-cards-api
- baseURL: https://api.shift4api.net/api/rest/v1
  baseurl_source: declared
  description: The Checkout Sessions API from Shift4 — 2 operation(s) for checkout sessions.
  name: Shift4 Checkout Sessions API
  slug: shift4-checkout-sessions-api
- baseURL: https://api.shift4api.net/api/rest/v1
  baseurl_source: declared
  description: The Credentials API from Shift4 — 1 operation(s) for credentials.
  name: Shift4 Credentials API
  slug: shift4-credentials-api
- baseURL: https://api.shift4api.net/api/rest/v1
  baseurl_source: declared
  description: The DCC API from Shift4 — 1 operation(s) for dcc.
  name: Shift4 DCC API
  slug: shift4-dcc-api
- baseURL: https://api.shift4api.net/api/rest/v1
  baseurl_source: declared
  description: The Devices API from Shift4 — 13 operation(s) for devices.
  name: Shift4 Devices API
  slug: shift4-devices-api
- baseURL: https://api.shift4api.net/api/rest/v1
  baseurl_source: declared
  description: The Gift Cards API from Shift4 — 9 operation(s) for gift cards.
  name: Shift4 Gift Cards API
  slug: shift4-gift-cards-api
- baseURL: https://api.shift4api.net/api/rest/v1
  baseurl_source: declared
  description: The Merchants API from Shift4 — 1 operation(s) for merchants.
  name: Shift4 Merchants API
  slug: shift4-merchants-api
- baseURL: https://api.shift4api.net/api/rest/v1
  baseurl_source: declared
  description: The Mode API from Shift4 — 2 operation(s) for mode.
  name: Shift4 Mode API
  slug: shift4-mode-api
- baseURL: https://api.shift4api.net/api/rest/v1
  baseurl_source: declared
  description: The OCT API from Shift4 — 2 operation(s) for oct.
  name: Shift4 OCT API
  slug: shift4-oct-api
- baseURL: https://api.shift4api.net/api/rest/v1
  baseurl_source: declared
  description: The Payment Links API from Shift4 — 4 operation(s) for payment links.
  name: Shift4 Payment Links API
  slug: shift4-payment-links-api
- baseURL: https://api.shift4api.net/api/rest/v1
  baseurl_source: declared
  description: The PayPal API from Shift4 — 3 operation(s) for paypal.
  name: Shift4 Pay Pal API
  slug: shift4-paypal-api
- baseURL: https://api.shift4api.net/api/rest/v1
  baseurl_source: declared
  description: The QR Payments API from Shift4 — 4 operation(s) for qr payments.
  name: Shift4 QR Payments API
  slug: shift4-qr-payments-api
- baseURL: https://api.shift4api.net/api/rest/v1
  baseurl_source: declared
  description: The Reports API from Shift4 — 1 operation(s) for reports.
  name: Shift4 Reports API
  slug: shift4-reports-api
- baseURL: https://api.shift4api.net/api/rest/v1
  baseurl_source: declared
  description: The Risk API from Shift4 — 1 operation(s) for risk.
  name: Shift4 Risk API
  slug: shift4-risk-api
- baseURL: https://api.shift4api.net/api/rest/v1
  baseurl_source: declared
  description: The Rule API from Shift4 — 1 operation(s) for rule.
  name: Shift4 Rule API
  slug: shift4-rule-api
- baseURL: https://api.shift4api.net/api/rest/v1
  baseurl_source: declared
  description: The Tokens API from Shift4 — 5 operation(s) for tokens.
  name: Shift4 Tokens API
  slug: shift4-tokens-api
- baseURL: https://api.shift4api.net/api/rest/v1
  baseurl_source: declared
  description: The Transactions API from Shift4 — 8 operation(s) for transactions.
  name: Shift4 Transactions API
  slug: shift4-transactions-api
- baseURL: https://api.shift4api.net/api/rest/v1
  baseurl_source: declared
  description: The Updater API from Shift4 — 2 operation(s) for updater.
  name: Shift4 Updater API
  slug: shift4-updater-api
artifact_total: 27
asyncapis:
- description: ''
  name: Shift4 Webhooks
  slug: shift4-webhooks
collections:
- collection_type: open
  name: Shift4 Payment API
  slug: open-shift4-payment-api
common:
- group: agent
  title: ''
  type: AgentSkill
  url: skills/shift4-authorize-and-capture.md
- group: build
  title: ''
  type: SDKs
  url: https://docs.shift4.com/sdks/ios
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/shift4-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/shift4-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/shift4-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.shift4.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.shift4.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.shift4.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.shift4.com/apis/payments-platform-rest/openapi
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.shift4.com/guides/quickstart
- group: build
  title: ''
  type: PostmanCollection
  url: https://docs.shift4.com/tools/postman
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.shift4.com/changelog
- group: operate
  title: ''
  type: Support
  url: https://docs.shift4.com/guides/support
- group: operate
  title: ''
  type: StatusPage
  url: https://status.shift4.com
- group: build
  title: ''
  type: JavaScriptLibrary
  url: https://dev.shift4.com/docs/js/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/shift4developer
- group: build
  title: ''
  type: Packages
  url: packages/shift4-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/shift4-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/shift4-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/shift4-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/shift4-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/shift4-payment-api-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/shift4-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.shift4.com/pdf/S4P-PCI-DSS-Roles-and-Responsibilities.pdf
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/shift4-error-codes.yml
- group: build
  title: ''
  type: DeclineCodes
  url: errors/shift4-decline-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/shift4-lifecycle.yml
- group: operate
  title: ''
  type: DeprecationPolicy
  url: https://docs.shift4.com/guides/deprecated/legacy-card-tokens
- group: start
  title: ''
  type: Sandbox
  url: sandbox/shift4-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/shift4-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/shift4-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/shift4-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/shift4-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/shift4-webhooks.yml
- group: design
  title: ''
  type: Components
  url: components/shift4-components.yml
- group: agent
  title: ''
  type: AgentSkills
  url: skills/_index.yml
created: '2026-07-24'
description: 'Shift4 (NYSE: FOUR) is a US-based integrated payments and commerce technology company headquartered in Center Valley, Pennsylvania, and a Fortune 1000 business serving restaurants, hospitality, retail, gaming, stadiums, e-commerce, and nonprofit verticals. It operates as an end-to-end acquirer-processor, owning the full stack from its own gateway and card acquiring through in-person SkyTab POS hardware, online checkout, and alternative payment methods, and has expanded internationally through acquisitions including Finaro (Credorax), Global Blue, and others. Its public developer surface is genuinely API-native: a Redocly-powered developer portal at docs.shift4.com publishes the Shift4 Payment API, a single downloadable OpenAPI 3.1 definition (v1.7.57, 70 paths) covering card transactions, tokenization, gift cards, devices/terminals, ACH, QR and PayPal alternative payments, 3D Secure, payment links, checkout sessions, OCT payouts, and reporting, authenticated with a header AccessToken
  (API key) plus HMAC-SHA256 request signing and backed by webhook event notifications, a sandbox, SDKs, and a published Postman collection.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
mcp_servers:
- description: ''
  name: Shift4 MCP Server
  slug: shift4-mcp-server
modified: '2026-07-24'
name: Shift4
nav: Providers
network: true
overview: 'Shift4 publishes 21 APIs on the [APIs.io](https://apis.io/) network, including 3D Secure API, ACH API, Batches API, and 18 more. Tagged areas include Payments, United States, Payment Processing, Payment Gateway, and Acquiring.


  The Shift4 catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Shift4''s developer surface includes authentication, documentation, API reference, getting-started guide, changelog, support, sandbox, and 29 more developer resources.'
random_paper: 6
score:
  band: developing
  composite: 51.6
  coverage:
    artifact_dirs: 21
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 3.9
    commercial_clarity: 3.9
    contract_governance: 18.2
    contract_quality: 65.9
    developer_ergonomics: 75.6
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 50.0
  previous_composite: 51.6
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 21
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 52.3
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/shift4/refs/heads/main/screenshots/shift4-2026-08-17T081829.png
security:
- kind: authentication
  name: Shift4 Authentication
  slug: shift4-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Shift4 Domain Security
  slug: shift4-domain-security
  summary_line: TLSv1.3 · DMARC
slug: shift4
tags:
- Payments
- United States
- Payment Processing
- Payment Gateway
- Acquiring
- Payment Terminal
- Tokenization
- ACH
- 3D Secure
- Gift Cards
- Payment Links
- Card Present
website: https://www.shift4.com
---
