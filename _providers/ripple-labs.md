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
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: true
    idempotency: documented
    mcp_server: true
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 59.2
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 109
  human_in_the_loop: 0
  name: Ripple Labs Agentic Access
  operation_count: 201
  slug: ripple-labs-agentic-access
  summary_line: 201 operations · 109 acting
api_count: 36
apis:
- description: Used to manage addresses
  name: Ripple Labs Addresses API
  slug: ripple-labs-addresses-api
- description: Used to manage credentials
  name: Ripple Labs API Credentials API
  slug: ripple-labs-api-credentials-api
- description: 'Use these operations to audit your accounts. | Operation | Method | Description | | -- | -- | -- | | [Get audits](/products/payments-odl/api-docs/ripplenet/reference/openapi/auditing/getaudits) | GET '
  name: Ripple Labs Auditing API
  slug: ripple-labs-auditing-api
- description: Use this API operation to manage your authentication tokens. | Operation | Method | Description | | --------- | ------ | ----------- | | [Obtain an access token](#operation/getAccessToken) | POST | Re
  name: Ripple Labs Authentication API
  slug: ripple-labs-authentication-api
- description: Use these operations to view balances and statements for a ledger. | Operation | Method | Description | | -- | -- | -- | | [Get balances](/products/payments-odl/api-docs/ripplenet/reference/openapi/ba
  name: Ripple Labs Balances and statements API
  slug: ripple-labs-balances-and-statements-api
- description: Used to view balances
  name: Ripple Labs Balances API
  slug: ripple-labs-balances-api
- description: Use these operations to perform beneficiary confirmations. | Operation | Method | Description | | -- | -- | -- | | [Get account lookup by status](/products/payments-odl/api-docs/ripplenet/reference/op
  name: Ripple Labs Beneficiary confirmation API
  slug: ripple-labs-beneficiary-confirmation-api
- description: Used to manage counterparties
  name: Ripple Labs Counterparties API
  slug: ripple-labs-counterparties-api
- description: Use these operations to view RippleNet Server health. | Operation | Method | Description | | -- | -- | -- | | [Check health](/products/payments-odl/api-docs/ripplenet/reference/openapi/diagnostics/che
  name: Ripple Labs Diagnostics API
  slug: ripple-labs-diagnostics-api
- description: Use these operations to manage exchange transfers. | Operation | Method | Description | | -- | -- | -- | | [Get exchange transfers](/products/payments-odl/api-docs/ripplenet/reference/openapi/exchange
  name: Ripple Labs Exchange transfers API
  slug: ripple-labs-exchange-transfers-api
- description: Use these operations to configure fees. | Operation | Method | Description | | -- | -- | -- | | [Get fees](/products/payments-odl/api-docs/ripplenet/reference/openapi/fees/getfees) | GET | List all fe
  name: Ripple Labs Fees API
  slug: ripple-labs-fees-api
- description: Use these operations to retrieve liquidations from the Smart Liquidation service. | Operation | Method | Description | | -- | -- | -- | | [Get liquidations](#operation/getLiquidations) | GET | List al
  name: Ripple Labs Liquidations API
  slug: ripple-labs-liquidations-api
- description: Use these API operations to obtain details about market-capitalization supply for a stablecoin currency. | Operation | Method | Description | | --------- | ------ | ----------- | | [Get total supply](
  name: Ripple Labs Market Cap API
  slug: ripple-labs-market-cap-api
- description: ''
  name: Ripple Labs Non-orchestration payments API
  slug: ripple-labs-non-orchestration-payments-api
- description: ''
  name: Ripple Labs Orchestration payments API
  slug: ripple-labs-orchestration-payments-api
- description: Use these operations to manage payment expirations. | Operation | Method | Description | | -- | -- | -- | | [Get payment expiry by ID](/products/payments-odl/api-docs/ripplenet/reference/openapi/payme
  name: Ripple Labs Payment expiration API
  slug: ripple-labs-payment-expiration-api
- description: Payout Method operations let receivers create and manage payout methods. Senders can generate quotes based on these receiver payout methods. | Operation | Method | Description | | -- | -- | -- | | [Cr
  name: Ripple Labs Payout method API
  slug: ripple-labs-payout-method-api
- description: Use these operations to configure your RippleNet platform accounts. | Operation | Method | Description | | -- | -- | -- | | [Create platform](/products/payments-odl/api-docs/ripplenet/reference/openap
  name: Ripple Labs Platform accounts API
  slug: ripple-labs-platform-accounts-api
- description: Used to manage connections policies
  name: Ripple Labs Policies API
  slug: ripple-labs-policies-api
- description: Use these operations to configure your RippleNet pool accounts. | Operation | Method | Description | | -- | -- | -- | | [Get all pool accounts](/products/payments-odl/api-docs/ripplenet/reference/open
  name: Ripple Labs Pool accounts API
  slug: ripple-labs-pool-accounts-api
- description: Use these operations to manage quote expirations. | Operation | Method | Description | | -- | -- | -- | | [List quote expiries](/products/payments-odl/api-docs/ripplenet/reference/openapi/quote-expira
  name: Ripple Labs Quote expiration API
  slug: ripple-labs-quote-expiration-api
- description: Use these operations to manage your quotes. | Operation | Method | Description | | -- | -- | -- | | [Accept quote](/products/payments-odl/api-docs/ripplenet/reference/openapi/quotes/acceptquote) | POS
  name: Ripple Labs Quotes API
  slug: ripple-labs-quotes-api
- description: 'Use these operations to manage your rates. | Operation | Method | Description | | -- | -- | -- | | [Get rates](/products/payments-odl/api-docs/ripplenet/reference/openapi/rates/getrates) | GET | Gets '
  name: Ripple Labs Rates API
  slug: ripple-labs-rates-api
- description: The Report Service API provides `PAYMENT_OPS`, `RECON`, and `FAILURE_CONVERSION_SSA` reports in either CSV or JSON format.
  name: Ripple Labs Reports API
  slug: ripple-labs-reports-api
- description: Use these operations to interact with your payment requests. | Operation | Method | Description | | -- | -- | -- | | [Get requests for payment](/products/payments-odl/api-docs/ripplenet/reference/open
  name: Ripple Labs Request for payment API
  slug: ripple-labs-request-for-payment-api
- description: Used to manage sweep configurations
  name: Ripple Labs Sweep Configurations API
  slug: ripple-labs-sweep-configurations-api
- description: Used to manage organization tags
  name: Ripple Labs Tags API
  slug: ripple-labs-tags-api
- description: Used to manage transactions
  name: Ripple Labs Transactions API
  slug: ripple-labs-transactions-api
- description: The Transactions - Sweep API from Ripple Labs — 2 operation(s) for transactions - sweep.
  name: Ripple Labs Transactions - Sweep API
  slug: ripple-labs-transactions-sweep-api
- description: Used to manage XRP specific transactions
  name: Ripple Labs Transactions - XRP API
  slug: ripple-labs-transactions-xrp-api
- description: Use these operations to manage your transfers. | Operation | Method | Description | | -- | -- | -- | | [Get transfers](/products/payments-odl/api-docs/ripplenet/reference/openapi/transfers/gettransfer
  name: Ripple Labs Transfers API
  slug: ripple-labs-transfers-api
- description: Used to manage vault tags
  name: Ripple Labs Vault Tags API
  slug: ripple-labs-vault-tags-api
- description: Used to manage vaults
  name: Ripple Labs Vaults API
  slug: ripple-labs-vaults-api
- description: Used to manage wallet tags
  name: Ripple Labs Wallet Tags API
  slug: ripple-labs-wallet-tags-api
- description: Used to manage wallets
  name: Ripple Labs Wallets API
  slug: ripple-labs-wallets-api
- description: Used to manage webhooks
  name: Ripple Labs Webhooks API
  slug: ripple-labs-webhooks-api
artifact_total: 43
asyncapis:
- description: ''
  name: Ripple Labs Stablecoin Webhooks
  slug: ripple-labs-stablecoin-webhooks
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/ripple-labs-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ripple-labs-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/ripple-labs-agentic-access.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/ripple-labs-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ripple-labs-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://ripple.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.ripple.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ripple.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.ripple.com/products/stablecoin/api/reference/rlusd-openapi
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.ripple.com/products/stablecoin/api/get-started
- group: company
  title: ''
  type: Blog
  url: https://ripple.com/insights/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ripple
- group: operate
  title: ''
  type: Support
  url: https://ripple.com/contact/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ripple.com/legal/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ripple.com/legal/privacy-policy/
- group: auth
  title: ''
  type: Compliance
  url: https://ripple.com/security/
- group: design
  title: ''
  type: Conformance
  url: conformance/ripple-labs-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/ripple-labs-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/ripple-labs-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/ripple-labs-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/ripple-labs-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ripple-labs-llms.txt
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/ripple-labs-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/ripple-labs-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.ripple.com/products/stablecoin/api/change-history
- group: start
  title: ''
  type: Sandbox
  url: sandbox/ripple-labs-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/ripple-labs-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/ripple-labs-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/ripple-labs-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/ripple-labs-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/ripple-labs-stablecoin-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/ripple-labs-rlusd-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/ripple-labs-ripplenet-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/ripple-labs-report-service-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/ripple-labs-smart-liquidation-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/ripple-labs-palisade-wallet-overlay.yaml
created: '2026-07-17'
description: Ripple (legally Ripple Labs Inc.) is a blockchain and crypto-enabled financial infrastructure company whose developer surface spans Ripple Payments (RippleNet Server API, On-Demand Liquidity, Payments Direct, Report Service, and Smart Liquidation), the RLUSD stablecoin "Ripple Mint" API, and Palisade Wallet-as-a-Service for institutional digital-asset custody. Its APIs let banks, fintechs, and enterprises move money cross-border, mint and redeem the RLUSD stablecoin, run treasury and reporting, and custody digital assets. Ripple also stewards the open-source XRP Ledger (documented at xrpl.org) with first-party client libraries xrpl.js and xrpl-py. Product documentation lives at docs.ripple.com; the legacy ripplelabs.com domain redirects to ripple.com.
image: https://ripple.com/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: ripple-labs-mcp.yml
  slug: ripple-labs-mcpyml
modified: '2026-07-21'
name: Ripple Labs
nav: Providers
network: true
overview: 'Ripple Labs publishes 36 APIs on the [APIs.io](https://apis.io/) network, including Addresses API, API Credentials API, Auditing API, and 33 more. Tagged areas include Company, Financial Services, Payments, Cross-Border Payments, and Blockchain.


  The Ripple Labs catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Ripple Labs'' developer surface includes authentication, documentation, API reference, getting-started guide, engineering blog, support, sandbox, and 30 more developer resources.'
random_paper: 35
scopes:
- name: Ripple Labs Scopes
  scope_count: 2
  slug: ripple-labs-scopes
  summary_line: 2 scopes · clientCredentials
score:
  band: strong
  composite: 57.1
  delta: 0.0
  facets:
    commercial_clarity: 36.8
    contract_quality: 68.5
    developer_ergonomics: 75.5
    discoverability: 92.6
    governance: 20.8
    operational_transparency: 36.8
  previous_composite: 57.1
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 36
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 62.5
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
security:
- kind: authentication
  name: Ripple Labs Authentication
  slug: ripple-labs-authentication
  summary_line: apiKey/http/oauth2 · 3 schemes
- kind: domain-security
  name: Ripple Labs Domain Security
  slug: ripple-labs-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Ripple Labs Trust Center
  slug: ripple-labs-trust-center
  summary_line: SOC 2, ISO 27001
slug: ripple-labs
tags:
- Company
- Financial Services
- Payments
- Cross-Border Payments
- Blockchain
- Cryptocurrency
- Stablecoin
- Digital Assets
- Custody
- Wallet
- Fintech
website: https://ripple.com
---
