---
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
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 78
  human_in_the_loop: 1
  name: Tribe Payments Agentic Access
  operation_count: 104
  slug: tribe-payments-agentic-access
  summary_line: 104 operations · 78 acting · 1 human-in-the-loop
api_count: 15
apis:
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
- description: The 3DS authentication required API from Tribe Payments — 1 operation(s) for 3ds authentication required.
  name: Tribe Payments 3DS authentication required API
  slug: tribe-payments-3ds-authentication-required-api
- description: Endpoints for confirming funds in the account.
  name: Tribe Payments Account API
  slug: tribe-payments-account-api
- description: The Accounts API from Tribe Payments — 4 operation(s) for accounts.
  name: Tribe Payments Accounts API
  slug: tribe-payments-accounts-api
- description: The App API from Tribe Payments — 4 operation(s) for app.
  name: Tribe Payments App API
  slug: tribe-payments-app-api
- description: The Authorization API from Tribe Payments — 3 operation(s) for authorization.
  name: Tribe Payments Authorization API
  slug: tribe-payments-authorization-api
- description: The Authorize API from Tribe Payments — 2 operation(s) for authorize.
  name: Tribe Payments Authorize API
  slug: tribe-payments-authorize-api
- description: Endpoints for executing bulk payments.
  name: Tribe Payments Bulk payments API
  slug: tribe-payments-bulk-payments-api
- description: The Cancel API from Tribe Payments — 2 operation(s) for cancel.
  name: Tribe Payments Cancel API
  slug: tribe-payments-cancel-api
- description: The Cancel recurring API from Tribe Payments — 2 operation(s) for cancel recurring.
  name: Tribe Payments Cancel recurring API
  slug: tribe-payments-cancel-recurring-api
- description: The Capture API from Tribe Payments — 2 operation(s) for capture.
  name: Tribe Payments Capture API
  slug: tribe-payments-capture-api
- description: The Credit API from Tribe Payments — 2 operation(s) for credit.
  name: Tribe Payments Credit API
  slug: tribe-payments-credit-api
- description: Some supported ASPSPs provide a more direct approach to some actions. Instead of retrieving prior user consent, actions can be executed directly, followed by an SCA confirmation in the next step. [Dir
  name: Tribe Payments Direct payments API
  slug: tribe-payments-direct-payments-api
- description: Endpoints for executing direct payments (without acquiring previous consent).
  name: Tribe Payments Direct payments without Bank API
  slug: tribe-payments-direct-payments-without-bank-api
- description: The Disputes API from Tribe Payments — 2 operation(s) for disputes.
  name: Tribe Payments Disputes API
  slug: tribe-payments-disputes-api
- description: The Event Data API from Tribe Payments — 6 operation(s) for event data.
  name: Tribe Payments Event Data API
  slug: tribe-payments-event-data-api
- description: The Funds API from Tribe Payments — 1 operation(s) for funds.
  name: Tribe Payments Funds API
  slug: tribe-payments-funds-api
- description: Endpoints for confirming funds in the account.
  name: Tribe Payments Funds confirmation API
  slug: tribe-payments-funds-confirmation-api
- description: Endpoints for interacting with the general data.
  name: Tribe Payments General API
  slug: tribe-payments-general-api
- description: The Health Check API from Tribe Payments — 1 operation(s) for health check.
  name: Tribe Payments Health Check API
  slug: tribe-payments-health-check-api
- description: The Host API from Tribe Payments — 5 operation(s) for host.
  name: Tribe Payments Host API
  slug: tribe-payments-host-api
- description: The Incremental authorize API from Tribe Payments — 2 operation(s) for incremental authorize.
  name: Tribe Payments Incremental authorize API
  slug: tribe-payments-incremental-authorize-api
- description: The Order status API from Tribe Payments — 2 operation(s) for order status.
  name: Tribe Payments Order status API
  slug: tribe-payments-order-status-api
- description: The P2P API from Tribe Payments — 2 operation(s) for p2p.
  name: Tribe Payments P2 P API
  slug: tribe-payments-p2p-api
- description: The Payment API from Tribe Payments — 4 operation(s) for payment.
  name: Tribe Payments Payment API
  slug: tribe-payments-payment-api
- description: The Payments API from Tribe Payments — 7 operation(s) for payments.
  name: Tribe Payments Payments API
  slug: tribe-payments-payments-api
- description: The Performance API from Tribe Payments — 1 operation(s) for performance.
  name: Tribe Payments Performance API
  slug: tribe-payments-performance-api
- description: The Pre authorize API from Tribe Payments — 2 operation(s) for pre authorize.
  name: Tribe Payments Pre authorize API
  slug: tribe-payments-pre-authorize-api
- description: The Prepare API from Tribe Payments — 1 operation(s) for prepare.
  name: Tribe Payments Prepare API
  slug: tribe-payments-prepare-api
- description: The Prepare error API from Tribe Payments — 1 operation(s) for prepare error.
  name: Tribe Payments Prepare error API
  slug: tribe-payments-prepare-error-api
- description: The Prepare success API from Tribe Payments — 1 operation(s) for prepare success.
  name: Tribe Payments Prepare success API
  slug: tribe-payments-prepare-success-api
- description: The Process API from Tribe Payments — 2 operation(s) for process.
  name: Tribe Payments Process API
  slug: tribe-payments-process-api
- description: The Processing accounts API from Tribe Payments — 2 operation(s) for processing accounts.
  name: Tribe Payments Processing accounts API
  slug: tribe-payments-processing-accounts-api
- description: The Processor API from Tribe Payments — 5 operation(s) for processor.
  name: Tribe Payments Processor API
  slug: tribe-payments-processor-api
- description: The Refund API from Tribe Payments — 2 operation(s) for refund.
  name: Tribe Payments Refund API
  slug: tribe-payments-refund-api
- description: The Sale API from Tribe Payments — 2 operation(s) for sale.
  name: Tribe Payments Sale API
  slug: tribe-payments-sale-api
- description: The Status API from Tribe Payments — 1 operation(s) for status.
  name: Tribe Payments Status API
  slug: tribe-payments-status-api
- description: The Transactions API from Tribe Payments — 2 operation(s) for transactions.
  name: Tribe Payments Transactions API
  slug: tribe-payments-transactions-api
- description: The User Actions Trigger API from Tribe Payments — 1 operation(s) for user actions trigger.
  name: Tribe Payments User Actions Trigger API
  slug: tribe-payments-user-actions-trigger-api
artifact_total: 65
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
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/tribe-payments-capability-edges.yml
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
  name: Tribe Payments MCP Server
  slug: tribe-payments-mcp-server
modified: '2026-07-24'
name: Tribe Payments
nav: Providers
network: true
overview: 'Tribe Payments publishes 38 APIs on the [APIs.io](https://apis.io/) network, including 3DS authentication required API, Account API, Accounts API, and 35 more. Tagged areas include Payments, United Kingdom, Issuer Processor, Card Issuing, and Acquiring.


  The Tribe Payments catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Tribe Payments'' developer surface includes authentication, documentation, API reference, changelog, engineering blog, support, getting-started guide, and 24 more developer resources.'
random_paper: 11
score:
  band: developing
  composite: 44.2
  coverage:
    artifact_dirs: 21
    catalog_gap: 83.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 31.6
    commercial_clarity: 31.6
    contract_governance: 18.2
    contract_quality: 51.5
    developer_ergonomics: 28.0
    discoverability: 66.7
    governance: 18.2
    operational_transparency: 39.5
  previous_composite: 44.2
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
    jurisdictions:
    - jurisdiction: EU
      standard: berlin-group-nextgenpsd2
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: EU
      standard: psd2
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 68.8
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tribe-payments/refs/heads/main/screenshots/tribe-payments-2026-08-17T082436.png
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
- Point-of-Sale
website: https://www.tribepayments.com/
---
