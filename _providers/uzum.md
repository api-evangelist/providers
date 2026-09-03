---
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
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 35.2
  scored_at: '2026-09-02'
api_count: 11
apis:
- description: Payment gateway for websites and mobile applications. Card payments (Visa, Mastercard, Uzcard, Humo), one-step and two-step authorization, back-to-back payment without the hosted form, card binding an
  name: Uzum Checkout
  slug: uzum-checkout
- baseURL: https://crossborder.transfer.uz
  baseurl_source: declared
  description: International money transfer between Uzbekistan and other countries. Transfers to Uzbekistan by phone number or card number, transfers from Uzbekistan by card number, cross-border payments for service
  name: Uzum CrossBorder Transfer
  slug: uzum-crossborder-transfer
- baseURL: https://remit-core.ipt-merch.com
  baseurl_source: declared
  description: Single integration point for cross-border remittances. Partners register, process, confirm, cancel and status-check CREDIT and DEBIT transfers; Remit Core handles routing, validation and interaction w
  name: Remit Core
  slug: uzum-remit-core
- baseURL: https://merchants-api.uzumnasiya.uz
  baseurl_source: declared
  description: REST API for partner integration with the Uzum Nasiya installment (BNPL) service. Buyer registration through an Uzum Nasiya WebView, buyer status and credit limit checks, basket pre-calculation of ins
  name: Uzum Nasiya Partner API
  slug: uzum-nasiya-partner
- baseURL: https://ofd-key.inplat-tech.com
  baseurl_source: declared
  description: Fiscalizes sales and refund receipts and submits them to the Uzbekistan State Tax Committee through a Fiscal Data Operator. Generates receipt links, supports non-fiscal receipts for advance and credit
  name: Uzum Fiscalization
  slug: uzum-fiscalization
- baseURL: https://mobile.apelsin.uz
  baseurl_source: declared
  description: 'Instant QR-code payments and payments through cash-register and POS / fiscal register systems, where the seller scans the customer''s QR code from the Uzum Bank app. Payment processing, fiscalization, '
  name: Uzum Fast Pay
  slug: uzum-fast-pay
- baseURL: https://mobile.apelsin.uz
  baseurl_source: declared
  description: Dynamic QR payment for a QR code printed on a POS receipt or shown on a cash-register screen, scanned by the customer in the Uzum Bank mobile application. Order creation and payment-link generation, o
  name: Uzum Dynamic QR
  slug: uzum-dynamic-qr
- description: Webhook protocol that lets partners accept payments from inside the Uzum Bank mobile application. Uzum Bank calls five partner-implemented webhooks — check, create, confirm, reverse and status — carry
  name: Uzum Merchant API
  slug: uzum-merchant-api
- description: Partner-facing foreign-exchange rate service. Converts an amount between currencies at the current Uzum rate and returns the partner's conversion limits. Documented on the Uzum Bank developer portal a
  name: Uzum RateKeeper
  slug: uzum-ratekeeper
- description: Banking-as-a-Service JSON-RPC 2.0 API that lets partners embed payments, transfers and account and card operations inside Uzbekistan's national payment system. Covers account balance, history and atta
  name: Uzum BaaS Payment Hub
  slug: uzum-payment-hub-baas
- description: Seller-cabinet API for Uzum Market used to synchronise marketplace orders, inventory and prices for both Fulfilment by Operator (FBO) and Fulfilment by Seller (FBS) models. Access requires an API toke
  name: Uzum Market Seller API
  slug: uzum-market-seller
artifact_total: 17
asyncapis:
- description: ''
  name: Uzum Merchant Webhooks
  slug: uzum-merchant-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://uzum.com/en/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.uzumbank.uz/en/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.uzumbank.uz/en/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.uzumbank.uz/en/checkout
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.uzumbank.uz/en/paymenthub/testing/getting-started/
- group: start
  title: ''
  type: SignUp
  url: https://merchants.uzumbank.uz/en/
- group: company
  title: ''
  type: Blog
  url: https://uzum.com/en/press-center/news-and-press-releases/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://uzum.com/en/privacy-and-terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://uzum.com/en/privacy-and-terms/
- group: operate
  title: ''
  type: Support
  url: https://uzum.com/en/contacts/
- group: build
  title: ''
  type: Postman
  url: https://developer.uzumbank.uz/remitcore/remitcore_postman_collection_credit.json
- group: build
  title: ''
  type: Packages
  url: packages/uzum-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/uzum-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/uzum-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/uzum-checkout-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/uzum-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/uzum-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/uzum-problem-types.yml
- group: build
  title: ''
  type: DeclineCodes
  url: errors/uzum-decline-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/uzum-lifecycle.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/uzum-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/uzum-domain-security.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/uzum-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/uzum-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/uzum-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/uzum-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/uzum-merchant-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/uzum-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/uzum-rate-limits.yml
created: '2026-09-02'
description: 'Uzum is an Uzbekistan-based digital ecosystem headquartered in Tashkent that bundles e-commerce, fintech and digital banking into a single group: Uzum Market (the country''s largest online marketplace), Uzum Tezkor (rapid food and grocery delivery), Uzum Bank (a licensed digital bank), and Uzum Nasiya (consumer BNPL / installment lending). Its developer-facing API surface is published by Uzum Bank at developer.uzumbank.uz, where nine OpenAPI contracts and a JSON-RPC 2.0 Banking-as-a-Service hub cover card acquiring (Uzum Checkout), QR and cash-register payments (Uzum Fast Pay, Dynamic QR), tax receipt fiscalization to the Uzbek State Tax Committee (Uzum Fiscalization), inbound and outbound cross-border money transfer (Uzum CrossBorder Transfer, Remit Core), installment contract origination (Uzum Nasiya Partner API), in-app merchant billing (Merchant API webhooks) and FX rate quoting (RateKeeper). Uzum Market additionally operates a seller-cabinet API at api-seller.uzum.uz for
  FBO/FBS order, inventory and price synchronization, which is credential-gated. All Uzum Bank API programs are onboarded through an account manager rather than self-service signup.'
image: https://developer.uzumbank.uz/en/img/logo.svg
layout: provider
mcp_servers:
- description: ''
  name: Uzum MCP Server
  slug: uzum-mcp-server
modified: '2026-09-02'
name: Uzum
nav: Providers
network: true
overview: 'Uzum publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Checkout, CrossBorder Transfer, Remit Core, and 6 more. Tagged areas include Company, Payments, Banking, Financial Services, and E-Commerce.


  The Uzum catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Uzum''s developer surface includes documentation, API reference, getting-started guide, signup flow, engineering blog, support, authentication, and 23 more developer resources.'
plans:
- name: Uzum Plans Pricing
  plan_count: 0
  slug: uzum-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 0
  name: Uzum Rate Limits
  slug: uzum-rate-limits
score:
  band: developing
  composite: 52.8
  coverage:
    artifact_dirs: 19
    catalog_gap: 75.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  facets:
    access_clarity: 42.1
    commercial_clarity: 42.1
    contract_governance: 4.5
    contract_quality: 54.9
    developer_ergonomics: 70.8
    discoverability: 74.1
    governance: 4.5
    operational_transparency: 23.7
  provenance:
    conformance: derived
    contracts:
      callable: 37.5
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 68.8
  schema_version: 0.18.0
  scored_at: '2026-09-02'
security:
- kind: authentication
  name: Uzum Authentication
  slug: uzum-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Uzum Domain Security
  slug: uzum-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: uzum
tags:
- Company
- Payments
- Banking
- Financial Services
- E-Commerce
- Marketplace
- Money Transfer
- Remittances
- BNPL
- Acquiring
- QR Payments
- Fiscalization
- Banking as a Service
- Uzbekistan
- Central Asia
website: https://uzum.com/en/
---
