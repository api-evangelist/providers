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
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 78
  human_in_the_loop: 1
  name: Tribe Payments Agentic Access
  operation_count: 104
  slug: tribe-payments-agentic-access
  summary_line: 104 operations · 78 acting · 1 human-in-the-loop
api_count: 15
apis:
- description: 'Tribe Payments Gateway Credit Card API (v3) for merchants processing credit and debit card e-commerce (ECOM) transactions - sale, authorization, capture, refund, and void - organized around REST with '
  name: Payment Gateway - Credit Card API
  slug: gateway-credit-card-api
- description: Tribe Payments Gateway Hosted Payments Page API (v3) that lets merchants collect card payments through a Tribe-hosted checkout, offloading PCI scope, plus a webhook interface for asynchronous transact
  name: Payment Gateway - Hosted Payments API (HPP)
  slug: gateway-hosted-payments-api
- description: Tribe Payments Gateway Credit Card Token API (v3) for tokenizing card credentials so merchants can store and reuse cards for recurring and card-on-file payments without holding raw PAN data, with an a
  name: Payment Gateway - Credit Card Token API
  slug: gateway-credit-card-token-api
- description: Tribe Payments Gateway Reports API (v3) providing merchants programmatic access to transaction reporting and reconciliation data over REST, with a report callback interface for delivering generated re
  name: Payment Gateway - Reports API
  slug: gateway-reports-api
- description: Tribe Payments Point of Sale Device Directory API (v3) for registering, managing, and querying the estate of physical and SoftPOS payment terminals (devices) connected to Tribe's acquiring platform. H
  name: Point of Sale - Device Directory API
  slug: pos-device-directory-api
- description: Tribe Payments Risk Monitor Client API (v1.1) for real-time fraud and transaction-risk monitoring, letting clients submit and query risk decisions, with a webhooks interface for risk event notificatio
  name: Risk Monitor - Client API
  slug: risk-monitor-client-api
- description: Tribe Payments Open Banking Bank API (v2) - the bank/ASPSP-facing side of Tribe's Open Banking product, exposing account information and payment-initiation capabilities to permissioned third-party pro
  name: Open Banking - Bank API
  slug: open-banking-bank-api
- description: Tribe Payments Open Banking Third-Party Providers (TPP) API (v2) - the TPP-facing side of Tribe's Open Banking product for initiating account-to-account payments (PIS) and retrieving account informati
  name: Open Banking - Third-Party Providers API (TPP)
  slug: open-banking-tpp-api
- description: Program Manager API (v1.2) for card issuers to interact with Tribe's ISAAC issuer-processing platform - issuing cards, managing programs and cardholders, and processing card transactions. Documented i
  name: Issuer Processor - Program Manager API (PM API)
  slug: issuer-program-manager-api
- description: Transaction Authorization Interface (v1.2) that sends webhook messages to issuers with the latest information about card-transaction status changes and system events on Tribe's ISAAC platform. Documen
  name: Issuer Processor - Transaction Authorization Interface (TAI API)
  slug: issuer-transaction-authorization-api
- description: Acquirer API (ACAPI, v1) for Tribe's acquiring-processor platform, covering acquirer-side transaction processing and settlement. Documented in the Tribe developer portal; no downloadable OpenAPI is pu
  name: Acquiring Processor - Acquirer API (ACAPI)
  slug: acquirer-api
- description: Merchant API (MAPI, v1) for onboarding and managing merchants on Tribe's acquiring-processor platform. Documented in the Tribe developer portal as Markdown; no downloadable OpenAPI is published for th
  name: Acquiring Processor - Merchant API (MAPI)
  slug: acquirer-merchant-api
- description: Terminal API (TAPI, v2) for integrating physical payment terminals with Tribe's acquiring-processor platform. Documented in the Tribe developer portal; no downloadable OpenAPI is published for the cur
  name: Acquiring Processor - Terminal API (TAPI)
  slug: acquirer-terminal-api
- description: Tokenization API (TOKAPI, v1) for tokenizing card data within Tribe's acquiring-processor platform. Documented in the Tribe developer portal; no downloadable OpenAPI is published for the current versi
  name: Acquiring Processor - Tokenization API (TOKAPI)
  slug: acquirer-tokenization-api
- description: Payment Services API (v1) for Tribe's Bank Connect / Banking-as-a-Service product, enabling fintechs to embed banking and payment services. Documented in the Tribe developer portal; no downloadable Op
  name: Bank Connect - Payment Services API
  slug: bank-connect-payment-services-api
artifact_total: 35
asyncapis:
- description: ''
  name: Tribe Payments Webhooks
  slug: tribe-payments-webhooks
collections:
- collection_type: open
  name: Bank Webhooks API
  slug: open-tribe-payments-obb-bank-api-webhooks
- collection_type: open
  name: 'Open Banking: Bank API'
  slug: open-tribe-payments-obb-bank-api
- collection_type: open
  name: Payment Webhooks
  slug: open-tribe-payments-obb-tpp-api-webhooks
- collection_type: open
  name: 'Open Banking: TPP API v2'
  slug: open-tribe-payments-obb-tpp-api
- collection_type: open
  name: Merchant API Credit Card Callback
  slug: open-tribe-payments-trb-cc-api-merchant-api-credit-card-callback-v3
- collection_type: open
  name: Merchant API Credit Card
  slug: open-tribe-payments-trb-cc-api-merchant-api-credit-card-v3
- collection_type: open
  name: Merchant API Credit Card Token
  slug: open-tribe-payments-trb-cc-token-api-merchant-api-credit-card-token-v3
- collection_type: open
  name: Merchant API Credit Card Token Webhook
  slug: open-tribe-payments-trb-cc-token-api-merchant-api-credit-card-token-webhook-v3
- collection_type: open
  name: Merchant API HPP
  slug: open-tribe-payments-trb-hpp-api-merchant-api-hpp-v3
- collection_type: open
  name: Merchant API HPP Webhook
  slug: open-tribe-payments-trb-hpp-api-merchant-api-hpp-webhook-v3
- collection_type: open
  name: Device Directory API
  slug: open-tribe-payments-trb-isac-pos-tdd-device-api-openapi-device-directory-api-v3
- collection_type: open
  name: Merchant API
  slug: open-tribe-payments-trb-report-api-merchant-api-report-callback-v3
- collection_type: open
  name: Merchant API Report
  slug: open-tribe-payments-trb-report-api-merchant-api-report-v3
- collection_type: open
  name: API Collection
  slug: open-tribe-payments-trb-risk-monitor-client-api-webhooks
- collection_type: open
  name: API Collection
  slug: open-tribe-payments-trb-risk-monitor-client-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/tribe-payments-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tribe-payments-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/tribe-payments-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.tribepayments.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://doc.tribepayments.com/
- group: docs
  title: ''
  type: Documentation
  url: https://doc.tribepayments.com/
- group: docs
  title: ''
  type: APIReference
  url: https://doc.tribepayments.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.tribepayments.com/product-updates
- group: company
  title: ''
  type: Blog
  url: https://www.tribepayments.com/news
- group: operate
  title: ''
  type: StatusPage
  url: https://status.tribepayments.com/
- group: operate
  title: ''
  type: Support
  url: https://www.tribepayments.com/contact-us
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.tribepayments.com/knowledge-hub
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.tribepayments.com/privacy-policy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/tribepayments/
- group: start
  title: ''
  type: GettingStarted
  url: https://doc.tribepayments.com/docs/getting-started
- group: start
  title: ''
  type: SignUp
  url: https://www.tribepayments.com/contact-us
- group: auth
  title: ''
  type: Compliance
  url: https://www.tribepayments.com/why-tribe
- group: design
  title: ''
  type: Conventions
  url: conventions/tribe-payments-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/tribe-payments-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/tribe-payments-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/tribe-payments-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/tribe-payments-conformance.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/tribe-payments-webhooks.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/tribe-payments-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/tribe-payments-data-model.yml
- group: design
  title: ''
  type: Components
  url: components/tribe-payments-components.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/tribe-payments-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/tribe-payments-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/tribe-payments-obb-tpp-api-openapi-overlay.yaml
created: '2026-07-24'
description: Tribe Payments is a London, United Kingdom-based payments technology company and issuer/acquirer processor that gives banks, acquirers, and fintechs a modular, API-driven platform to launch card and payment products without building core processing in-house. Built around its ISAAC processing engine, Tribe spans card issuing (issuer processing), merchant acquiring and a payment gateway, POS/SoftPOS terminal management, tokenization, fraud and risk monitoring, 3D Secure, digital wallets, Open Banking (PSD2 account-to-account payment initiation and account information), and Bank Connect / Banking-as-a-Service. Tribe positions itself as developer-led, publishing an extensive public API reference at doc.tribepayments.com; sandbox access is granted on request rather than through fully open self-service signup. Its home market is the United Kingdom, where PSD2/Open Banking and the Faster Payments and Bacs rails operated by Pay.UK anchor a dense cluster of API-native payment providers.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
mcp_servers:
- description: ''
  name: tribe-payments-mcp.yml
  slug: tribe-payments-mcpyml
modified: '2026-07-24'
name: Tribe Payments
nav: Providers
network: true
overview: 'Tribe Payments publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Payment Gateway - Credit Card API, Payment Gateway - Hosted Payments API (HPP), Payment Gateway - Credit Card Token API, and 5 more. Tagged areas include Payments, United Kingdom, Issuer Processor, Card Issuing, and Acquiring.


  The Tribe Payments catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Tribe Payments'' developer surface includes authentication, documentation, API reference, changelog, engineering blog, support, getting-started guide, and 23 more developer resources.'
random_paper: 119
score:
  band: developing
  composite: 46.7
  delta: 0.0
  facets:
    commercial_clarity: 31.6
    contract_quality: 56.4
    developer_ergonomics: 62.5
    discoverability: 72.2
    governance: 20.8
    operational_transparency: 39.5
  previous_composite: 46.7
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 15
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 40.6
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
security:
- kind: authentication
  name: Tribe Payments Authentication
  slug: tribe-payments-authentication
  summary_line: apiKey/http · 8 schemes
- kind: domain-security
  name: Tribe Payments Domain Security
  slug: tribe-payments-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: tribe-payments
tags:
- Payments
- United Kingdom
- Issuer Processor
- Card Issuing
- Acquiring
- Payment Gateway
- Payment Processing
- Open Banking
- Account-to-Account
- Banking-as-a-Service
- Fraud
- Point of Sale
website: https://www.tribepayments.com/
---
