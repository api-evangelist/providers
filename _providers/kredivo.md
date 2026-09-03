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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: documented
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.6
  scored_at: '2026-09-02'
api_count: 5
apis:
- baseURL: https://sandbox.kredivo.com
  baseurl_source: declared
  description: Installment, interest and service-fee breakdown.
  name: Kredivo Calculator API
  slug: kredivo-calculator-api
- baseURL: https://sandbox.kredivo.com
  baseurl_source: declared
  description: Initiating a Kredivo installment checkout (2-click, 0-click, QR, EDC).
  name: Kredivo Checkout API
  slug: kredivo-checkout-api
- baseURL: https://sandbox.kredivo.com
  baseurl_source: declared
  description: Confirming a transaction after a push notification.
  name: Kredivo Confirmation API
  slug: kredivo-confirmation-api
- baseURL: https://sandbox.kredivo.com
  baseurl_source: declared
  description: Managing tokenized (0-click) shoppers and their credit limits.
  name: Kredivo Tokenization API
  slug: kredivo-tokenization-api
- baseURL: https://sandbox.kredivo.com
  baseurl_source: declared
  description: Status, cancellation and reversal of transactions.
  name: Kredivo Transactions API
  slug: kredivo-transactions-api
artifact_total: 16
asyncapis:
- description: ''
  name: Kredivo Checkout Webhooks
  slug: kredivo-checkout-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Kredivo Checkout Calculator API
  slug: open-kredivo-calculator-api
- collection_type: open
  name: Kredivo Calculator Checkout API
  slug: open-kredivo-checkout-api
- collection_type: open
  name: Kredivo Checkout Calculator Confirmation API
  slug: open-kredivo-confirmation-api
- collection_type: open
  name: Kredivo Checkout Calculator Tokenization API
  slug: open-kredivo-tokenization-api
- collection_type: open
  name: Kredivo Checkout Calculator Transactions API
  slug: open-kredivo-transactions-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/kredivo-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/kredivo-checkout-overlay.yaml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kredivo-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/kredivo-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/kredivo-vulnerability-disclosure.yml
- group: company
  title: ''
  type: Website
  url: https://finaccel.co
- group: company
  title: ''
  type: CorporateWebsite
  url: https://kredivocorp.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://doc.kredivo.com/
- group: docs
  title: ''
  type: Documentation
  url: https://doc.kredivo.com/
- group: docs
  title: ''
  type: APIReference
  url: https://doc.kredivo.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://doc.kredivo.com/
- group: company
  title: ''
  type: Blog
  url: https://blog.kredivo.com/
- group: operate
  title: ''
  type: Support
  url: https://kredivo.com/faqs/
- group: start
  title: ''
  type: SignUp
  url: https://kredivo.com/merchant/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://kredivo.com/p/in/tos.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://kredivo.com/p/in/privacy.html
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://kredivo.com/security-policy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.kredivo.com/
- group: company
  title: ''
  type: Partners
  url: https://kredivo.com/p/partners.html
- group: build
  title: ''
  type: Packages
  url: packages/kredivo-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/kredivo-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/kredivo-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/kredivo-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/kredivo-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/kredivo-error-codes.yml
- group: build
  title: ''
  type: DeclineCodes
  url: errors/kredivo-decline-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/kredivo-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/kredivo-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/kredivo-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/kredivo-conformance.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/kredivo-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/kredivo-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/kredivo-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/kredivo-checkout-webhooks.yml
created: '2026-07-17'
description: Kredivo is a Southeast Asian consumer credit platform operated by FinAccel (Kredivo Group), best known for its "Buy Now, Pay Later" product offering instant real-time credit decisioning for online and offline purchases across Indonesia, Vietnam, Thailand and the Philippines. For developers, Kredivo publishes the Kredivo Checkout API — a merchant-facing HTTP/JSON payment API that lets an ecommerce store, marketplace, POS or EDC terminal offer installment payment (30 days through 24 months) at checkout. The API covers 2-click redirect checkout, 0-click tokenized express checkout, dynamic and static QR checkout for physical stores, EDC terminal checkout, transaction status polling, full and partial cancellation, user credit-limit lookup, and an installment/interest calculator, with asynchronous push notifications to a merchant-supplied push_uri and a signature-key confirmation callback. Kredivo Group also operates KrediFazz (instant cash loans), Krom (digital bank), Timo and GajiGesa.
image: https://doc.kredivo.com/images/logo.png
layout: provider
mcp_servers:
- description: ''
  name: Kredivo MCP Server
  slug: kredivo-mcp-server
modified: '2026-07-19'
name: Kredivo
nav: Providers
network: true
overview: 'Kredivo publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Calculator API, Checkout API, Confirmation API, and 2 more. Tagged areas include Company, Payments, Buy Now Pay Later, BNPL, and Lending.


  The Kredivo catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Kredivo''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, signup flow, authentication, and 28 more developer resources.'
random_paper: 0
score:
  band: developing
  composite: 42.5
  coverage:
    artifact_dirs: 20
    catalog_gap: 75.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 4.5
    contract_quality: 22.0
    developer_ergonomics: 73.2
    discoverability: 81.5
    governance: 4.5
    operational_transparency: 34.2
  previous_composite: 42.5
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 6
      marker_coverage: 100.0
      total: 6
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
screenshot: https://raw.githubusercontent.com/api-evangelist/kredivo/refs/heads/main/screenshots/kredivo-2026-07-25T224258.png
security:
- kind: authentication
  name: Kredivo Authentication
  slug: kredivo-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Kredivo Domain Security
  slug: kredivo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Kredivo Vulnerability Disclosure
  slug: kredivo-vulnerability-disclosure
  summary_line: Hackerone · contact published
slug: kredivo
tags:
- Company
- Payments
- Buy Now Pay Later
- BNPL
- Lending
- Consumer Credit
- Checkout
- Fintech
- E-Commerce
- Indonesia
- Southeast Asia
- Financial-Services
website: https://finaccel.co
---
