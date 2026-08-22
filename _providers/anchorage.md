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
    idempotency: verified
    mcp_server: documented
    openapi_examples: partial
    rate_limit_signal: documented
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 62.0
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 86
  human_in_the_loop: 0
  name: Anchorage Agentic Access
  operation_count: 202
  slug: anchorage-agentic-access
  summary_line: 202 operations · 86 acting
api_count: 28
apis:
- description: 'These endpoints allow the user to create and retrieve deposit addresses for specific assets. # Verifying Deposit Addresses The addresses REST API endpoints return signatures of the address strings and'
  name: Anchorage Digital Addresses API
  slug: anchorage-addresses-api
- description: Anti-Money Laundering compliance endpoints
  name: Anchorage Digital AML API
  slug: anchorage-aml-api
- description: These endpoints allow querying information about the current API key in use.
  name: Anchorage Digital API Key API
  slug: anchorage-api-key-api
- description: Descriptions of supported asset types
  name: Anchorage Digital Asset Types API
  slug: anchorage-asset-types-api
- description: Operations for querying supported asset types, networks, and wallet key compatibility
  name: Anchorage Digital Asset Types & Networks API
  slug: anchorage-asset-types-networks-api
- description: The Atlas Settlement Network API from Anchorage Digital — 9 operation(s) for atlas settlement network.
  name: Anchorage Digital Atlas Settlement Network API
  slug: anchorage-atlas-settlement-network-api
- description: Operations for querying wallet balances and staking positions
  name: Anchorage Digital Balances API
  slug: anchorage-balances-api
- description: The Collateral Management API from Anchorage Digital — 8 operation(s) for collateral management.
  name: Anchorage Digital Collateral Management API
  slug: anchorage-collateral-management-api
- description: Deposit Attribution is the process of gathering information about the originator of a given deposit. Once a deposit is initiated this process is automatically started being represented by a Deposit At
  name: Anchorage Digital Deposit Attribution API
  slug: anchorage-deposit-attribution-api
- description: Operations for managing fiat bank payments and accounts
  name: Anchorage Digital Fiat Banking Operations API
  slug: anchorage-fiat-banking-operations-api
- description: These endpoints allow clients/partner institutions to start the customer onboarding process for a B2B2B/B2B2C end customer who would not be using the Anchorage Digital applications directly. They coll
  name: Anchorage Digital Onboarding API
  slug: anchorage-onboarding-api
- description: Endpoints for stablecoin conversion operations including issuance and redemption
  name: Anchorage Digital Stablecoins API
  slug: anchorage-stablecoins-api
- description: The Statements API from Anchorage Digital — 4 operation(s) for statements.
  name: Anchorage Digital Statements API
  slug: anchorage-statements-api
- description: These endpoints allow the organization to manage subaccounts.
  name: Anchorage Digital Subaccounts API
  slug: anchorage-subaccounts-api
- description: These endpoints allow creating, applying, removing, and searching tags on operations.
  name: Anchorage Digital Tagging API
  slug: anchorage-tagging-api
- description: These endpoints allow the organization to manage tax. ** UNDER DEVELOPMENT **
  name: Anchorage Digital Tax API
  slug: anchorage-tax-api
- description: Operations for managing tax accounts and cost basis reporting
  name: Anchorage Digital Tax Reporting API
  slug: anchorage-tax-reporting-api
- description: API endpoints for managing RFQ, Market or Limit orders [Anchorage Digital websocket API documentation.](https://anchorage-wsapi.netlify.app/)
  name: Anchorage Digital Trading API
  slug: anchorage-trading-api
- description: Operations for constructing and signing transactions via the Construct API
  name: Anchorage Digital Transaction Construction API
  slug: anchorage-transaction-construction-api
- description: Operations for creating transactions with managed fees and replay protection
  name: Anchorage Digital Transaction Creation API
  slug: anchorage-transaction-creation-api
- description: Transactions include all of the blockchain actions that affect your vault balances, such as withdrawals, deposits, transfers, and participation actions. Each transaction may have a corresponding block
  name: Anchorage Digital Transactions API
  slug: anchorage-transactions-api
- description: These endpoints allow you to transfer assets from one of your API-enabled vaults to *another resource custodied by Anchorage Digital*.
  name: Anchorage Digital Transfers API
  slug: anchorage-transfers-api
- description: The Trusted Destinations API from Anchorage Digital — 4 operation(s) for trusted destinations.
  name: Anchorage Digital Trusted Destinations API
  slug: anchorage-trusted-destinations-api
- description: An Anchorage Digital organization has one or more vaults. Each vault may contain one or more assets which are held in wallets. Each wallet may be comprised of one or more addresses depending on the ty
  name: Anchorage Digital Vaults API
  slug: anchorage-vaults-api
- description: These endpoints allow access to vesting balance information for allocations.
  name: Anchorage Digital Vesting API
  slug: anchorage-vesting-api
- description: Operations for creating and signing transactions that your organization broadcasts on-chain
  name: Anchorage Digital Wallet Operations API
  slug: anchorage-wallet-operations-api
- description: A vault has one or more wallets. Each wallet is a collection of one or more addresses depending on the asset type. A wallet is created for a particular blockchain network, e.g. Bitcoin, Ethereum, etc.
  name: Anchorage Digital Wallets API
  slug: anchorage-wallets-api
- description: The Webhook Notifications API from Anchorage Digital — 6 operation(s) for webhook notifications.
  name: Anchorage Digital Webhook Notifications API
  slug: anchorage-webhook-notifications-api
arazzos:
- description: Create a wallet in a vault, provision a deposit address, and watch for the inbound deposit.
  name: Anchorage Digital - Receive a crypto deposit
  slug: anchorage-receive-deposit
- description: Request a quote, accept it, and confirm the resulting order and trade.
  name: Anchorage Digital - Trade via RFQ
  slug: anchorage-trade-rfq
artifact_total: 66
asyncapis:
- description: ''
  name: Anchorage Webhooks
  slug: anchorage-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Anchorage Digital API Reference Addresses API
  slug: open-anchorage-addresses-api
- collection_type: open
  name: Anchorage Digital API Reference Addresses AML API
  slug: open-anchorage-aml-api
- collection_type: open
  name: Anchorage Digital API Reference Addresses API Key API
  slug: open-anchorage-api-key-api
- collection_type: open
  name: Anchorage Digital API Reference Addresses Asset Types API
  slug: open-anchorage-asset-types-api
- collection_type: open
  name: Anchorage Digital API Reference Addresses Asset Types & Networks API
  slug: open-anchorage-asset-types-networks-api
- collection_type: open
  name: Anchorage Digital API Reference Addresses Atlas Settlement Network API
  slug: open-anchorage-atlas-settlement-network-api
- collection_type: open
  name: Anchorage Digital API Reference Addresses Balances API
  slug: open-anchorage-balances-api
- collection_type: open
  name: Anchorage Digital API Reference Addresses Collateral Management API
  slug: open-anchorage-collateral-management-api
- collection_type: open
  name: Anchorage Digital API Reference Addresses Deposit Attribution API
  slug: open-anchorage-deposit-attribution-api
- collection_type: open
  name: Anchorage Digital API Reference Addresses Fiat Banking Operations API
  slug: open-anchorage-fiat-banking-operations-api
- collection_type: open
  name: Anchorage Digital API Reference Addresses Onboarding API
  slug: open-anchorage-onboarding-api
- collection_type: open
  name: Anchorage Digital API Reference Addresses Stablecoins API
  slug: open-anchorage-stablecoins-api
- collection_type: open
  name: Anchorage Digital API Reference Addresses Statements API
  slug: open-anchorage-statements-api
- collection_type: open
  name: Anchorage Digital API Reference Addresses Subaccounts API
  slug: open-anchorage-subaccounts-api
- collection_type: open
  name: Anchorage Digital API Reference Addresses Tagging API
  slug: open-anchorage-tagging-api
- collection_type: open
  name: Anchorage Digital API Reference Addresses Tax API
  slug: open-anchorage-tax-api
- collection_type: open
  name: Anchorage Digital API Reference Addresses Tax Reporting API
  slug: open-anchorage-tax-reporting-api
- collection_type: open
  name: Anchorage Digital API Reference Addresses Trading API
  slug: open-anchorage-trading-api
- collection_type: open
  name: Anchorage Digital API Reference Addresses Transaction Construction API
  slug: open-anchorage-transaction-construction-api
- collection_type: open
  name: Anchorage Digital API Reference Addresses Transaction Creation API
  slug: open-anchorage-transaction-creation-api
- collection_type: open
  name: Anchorage Digital API Reference Addresses Transactions API
  slug: open-anchorage-transactions-api
- collection_type: open
  name: Anchorage Digital API Reference Addresses Transfers API
  slug: open-anchorage-transfers-api
- collection_type: open
  name: Anchorage Digital API Reference Addresses Trusted Destinations API
  slug: open-anchorage-trusted-destinations-api
- collection_type: open
  name: Anchorage Digital API Reference Addresses Vaults API
  slug: open-anchorage-vaults-api
- collection_type: open
  name: Anchorage Digital API Reference Addresses Vesting API
  slug: open-anchorage-vesting-api
- collection_type: open
  name: Anchorage Digital API Reference Addresses Wallet Operations API
  slug: open-anchorage-wallet-operations-api
- collection_type: open
  name: Anchorage Digital API Reference Addresses Wallets API
  slug: open-anchorage-wallets-api
- collection_type: open
  name: Anchorage Digital API Reference Addresses Webhook Notifications API
  slug: open-anchorage-webhook-notifications-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/anchorage-v2-overlay.yaml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.anchorage.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.anchorage.com/knowledge-base/index
- group: docs
  title: ''
  type: APIReference
  url: https://docs.anchorage.com/knowledge-base/api-reference/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.anchorage.com/knowledge-base/platform/developers/setting-up
- group: company
  title: ''
  type: Blog
  url: https://www.anchorage.com/insights
- group: start
  title: ''
  type: Login
  url: https://anchoragelogin.com/login/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.anchorage.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.anchorage.com/privacy-policy
- group: auth
  title: ''
  type: Authentication
  url: authentication/anchorage-authentication.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/anchorage-v2-openapi-original.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/anchorage-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/anchorage-llms.txt
- group: start
  title: ''
  type: Sandbox
  url: sandbox/anchorage-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/anchorage-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/anchorage-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/anchorage-rate-limits.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/anchorage-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/anchorage-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://anchorage.statuspage.io
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.anchorage.com/knowledge-base/api-reference/changelog.md
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/anchorage-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/anchorage-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/anchorage-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/anchorage-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/anchorage-receive-deposit.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/anchorage-trade-rfq.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/anchorage-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/anchorage-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.anchorage.com/vulnerability-disclosure
- group: auth
  title: ''
  type: DomainSecurity
  url: security/anchorage-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://anchorage.com
created: '2026-07-17'
description: 'Anchorage Digital is the first federally chartered crypto bank in the U.S., providing institutional-grade digital asset infrastructure through its integrated Prime platform: qualified custody of crypto and USD, institutional trading with deep liquidity, staking across dozens of proof-of-stake networks, the Atlas on-chain settlement network, stablecoin issuance and conversion, and integrated cash-and-crypto banking. Its REST API v2.0 (and newer v3 surface) exposes 100+ operations across custody, wallets, addresses, transfers, transactions, trading, Atlas settlement, collateral management, onboarding, subaccounts, tax, stablecoins, and webhook notifications, secured with API keys plus Ed25519 request signing and quorum approval. Trusted by institutions including BlackRock, Goldman Sachs, and Grayscale.'
image: https://cdn.prod.website-files.com/649e7e19aca422fdfb636e26/64de142d90faade0441ac39c_favicon-256x256.png
layout: provider
mcp_servers:
- description: ''
  name: anchorage-mcp.yml
  slug: anchorage-mcpyml
modified: '2026-07-17'
name: Anchorage Digital
nav: Providers
network: true
overview: 'Anchorage Digital publishes 28 APIs on the [APIs.io](https://apis.io/) network, including Addresses API, AML API, API Key API, and 25 more. Tagged areas include Company, Crypto, Digital Assets, Custody, and Trading.


  The Anchorage Digital catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Anchorage Digital''s developer surface includes documentation, API reference, getting-started guide, engineering blog, authentication, sandbox, changelog, and 26 more developer resources.'
random_paper: 12
rate_limits:
- limit_count: 1
  name: Anchorage Rate Limits
  slug: anchorage-rate-limits
score:
  band: developing
  composite: 48.8
  delta: -5.7
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 16.7
    contract_quality: 68.0
    developer_ergonomics: 23.2
    discoverability: 81.5
    governance: 16.7
    operational_transparency: 78.9
  previous_composite: 54.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 28
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 39.2
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/anchorage/refs/heads/main/screenshots/anchorage-2026-07-25T200219.png
security:
- kind: authentication
  name: Anchorage Authentication
  slug: anchorage-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Anchorage Domain Security
  slug: anchorage-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Anchorage Vulnerability Disclosure
  slug: anchorage-vulnerability-disclosure
  summary_line: disclosure policy published
slug: anchorage
tags:
- Company
- Crypto
- Digital Assets
- Custody
- Trading
- Staking
- Settlement
- Stablecoins
- Banking
- Institutional
website: https://anchorage.com
---
