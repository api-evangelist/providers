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
    event_surface_described: derived
    idempotency: documented
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 47.1
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 55
  human_in_the_loop: 0
  name: Anchorage Digital Agentic Access
  operation_count: 134
  slug: anchorage-digital-agentic-access
  summary_line: 134 operations · 55 acting
api_count: 20
apis:
- description: 'These endpoints allow the user to create and retrieve deposit addresses for specific assets. # Verifying Deposit Addresses The addresses REST API endpoints return signatures of the address strings and'
  name: Anchorage Digital Addresses API
  slug: anchorage-digital-addresses-api
- description: These endpoints allow querying information about the current API key in use.
  name: Anchorage Digital API Key API
  slug: anchorage-digital-api-key-api
- description: Descriptions of supported asset types
  name: Anchorage Digital Asset Types API
  slug: anchorage-digital-asset-types-api
- description: The Atlas Settlement Network API from Anchorage Digital — 9 operation(s) for atlas settlement network.
  name: Anchorage Digital Atlas Settlement Network API
  slug: anchorage-digital-atlas-settlement-network-api
- description: The Collateral Management API from Anchorage Digital — 6 operation(s) for collateral management.
  name: Anchorage Digital Collateral Management API
  slug: anchorage-digital-collateral-management-api
- description: Deposit Attribution is the process of gathering information about the originator of a given deposit. Once a deposit is initiated this process is automatically started being represented by a Deposit At
  name: Anchorage Digital Deposit Attribution API
  slug: anchorage-digital-deposit-attribution-api
- description: These endpoints allow clients/partner institutions to start the customer onboarding process for a B2B2B/B2B2C end customer who would not be using the Anchorage Digital applications directly. They coll
  name: Anchorage Digital Onboarding API
  slug: anchorage-digital-onboarding-api
- description: Endpoints for stablecoin conversion operations including issuance and redemption
  name: Anchorage Digital Stablecoins API
  slug: anchorage-digital-stablecoins-api
- description: The Statements API from Anchorage Digital — 4 operation(s) for statements.
  name: Anchorage Digital Statements API
  slug: anchorage-digital-statements-api
- description: These endpoints allow the organization to manage subaccounts.
  name: Anchorage Digital Subaccounts API
  slug: anchorage-digital-subaccounts-api
- description: These endpoints allow the organization to manage tax. ** UNDER DEVELOPMENT **
  name: Anchorage Digital Tax API
  slug: anchorage-digital-tax-api
- description: Operations for managing tax accounts and cost basis reporting
  name: Anchorage Digital Tax Reporting API
  slug: anchorage-digital-tax-reporting-api
- description: API endpoints for managing RFQ, Market or Limit orders [Anchorage Digital websocket API documentation.](https://anchorage-wsapi.netlify.app/)
  name: Anchorage Digital Trading API
  slug: anchorage-digital-trading-api
- description: Transactions include all of the blockchain actions that affect your vault balances, such as withdrawals, deposits, transfers, and participation actions. Each transaction may have a corresponding block
  name: Anchorage Digital Transactions API
  slug: anchorage-digital-transactions-api
- description: These endpoints allow you to transfer assets from one of your API-enabled vaults to *another resource custodied by Anchorage Digital*.
  name: Anchorage Digital Transfers API
  slug: anchorage-digital-transfers-api
- description: The Trusted Destinations API from Anchorage Digital — 4 operation(s) for trusted destinations.
  name: Anchorage Digital Trusted Destinations API
  slug: anchorage-digital-trusted-destinations-api
- description: An Anchorage Digital organization has one or more vaults. Each vault may contain one or more assets which are held in wallets. Each wallet may be comprised of one or more addresses depending on the ty
  name: Anchorage Digital Vaults API
  slug: anchorage-digital-vaults-api
- description: These endpoints allow access to vesting balance information for allocations.
  name: Anchorage Digital Vesting API
  slug: anchorage-digital-vesting-api
- description: A vault has one or more wallets. Each wallet is a collection of one or more addresses depending on the asset type. A wallet is created for a particular blockchain network, e.g. Bitcoin, Ethereum, etc.
  name: Anchorage Digital Wallets API
  slug: anchorage-digital-wallets-api
- description: The Webhook Notifications API from Anchorage Digital — 6 operation(s) for webhook notifications.
  name: Anchorage Digital Webhook Notifications API
  slug: anchorage-digital-webhook-notifications-api
artifact_total: 48
asyncapis:
- description: ''
  name: Anchorage Digital Webhooks
  slug: anchorage-digital-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Anchorage Digital API Reference Addresses API
  slug: open-anchorage-digital-addresses-api
- collection_type: open
  name: Anchorage Digital API Reference Addresses API Key API
  slug: open-anchorage-digital-api-key-api
- collection_type: open
  name: Anchorage Digital API Reference Addresses Asset Types API
  slug: open-anchorage-digital-asset-types-api
- collection_type: open
  name: Anchorage Digital API Reference Addresses Atlas Settlement Network API
  slug: open-anchorage-digital-atlas-settlement-network-api
- collection_type: open
  name: Anchorage Digital API Reference Addresses Collateral Management API
  slug: open-anchorage-digital-collateral-management-api
- collection_type: open
  name: Anchorage Digital API Reference Addresses Deposit Attribution API
  slug: open-anchorage-digital-deposit-attribution-api
- collection_type: open
  name: Anchorage Digital API Reference Addresses Onboarding API
  slug: open-anchorage-digital-onboarding-api
- collection_type: open
  name: Anchorage Digital API Reference Addresses Stablecoins API
  slug: open-anchorage-digital-stablecoins-api
- collection_type: open
  name: Anchorage Digital API Reference Addresses Statements API
  slug: open-anchorage-digital-statements-api
- collection_type: open
  name: Anchorage Digital API Reference Addresses Subaccounts API
  slug: open-anchorage-digital-subaccounts-api
- collection_type: open
  name: Anchorage Digital API Reference Addresses Tax API
  slug: open-anchorage-digital-tax-api
- collection_type: open
  name: Anchorage Digital API Reference Addresses Tax Reporting API
  slug: open-anchorage-digital-tax-reporting-api
- collection_type: open
  name: Anchorage Digital API Reference Addresses Trading API
  slug: open-anchorage-digital-trading-api
- collection_type: open
  name: Anchorage Digital API Reference Addresses Transactions API
  slug: open-anchorage-digital-transactions-api
- collection_type: open
  name: Anchorage Digital API Reference Addresses Transfers API
  slug: open-anchorage-digital-transfers-api
- collection_type: open
  name: Anchorage Digital API Reference Addresses Trusted Destinations API
  slug: open-anchorage-digital-trusted-destinations-api
- collection_type: open
  name: Anchorage Digital API Reference Addresses Vaults API
  slug: open-anchorage-digital-vaults-api
- collection_type: open
  name: Anchorage Digital API Reference Addresses Vesting API
  slug: open-anchorage-digital-vesting-api
- collection_type: open
  name: Anchorage Digital API Reference Addresses Wallets API
  slug: open-anchorage-digital-wallets-api
- collection_type: open
  name: Anchorage Digital API Reference Addresses Webhook Notifications API
  slug: open-anchorage-digital-webhook-notifications-api
common:
- group: company
  title: ''
  type: Website
  url: https://anchorage.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.anchorage.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.anchorage.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.anchorage.com/knowledge-base/api-reference/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.anchorage.com/knowledge-base/platform/users/overview
- group: company
  title: ''
  type: Blog
  url: https://www.anchorage.com/insights
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/anchorageoss
- group: operate
  title: ''
  type: Support
  url: mailto:contact@anchorage.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.anchorage.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.anchorage.com/privacy-policy
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/anchorage-digital-openapi-original.json
- group: other
  title: ''
  type: Overlay
  url: overlays/anchorage-digital-openapi-overlay.yaml
- group: design
  title: ''
  type: DataModel
  url: data-model/anchorage-digital-data-model.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/anchorage-digital-authentication.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/anchorage-digital-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/anchorage-digital-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.anchorage.com/vulnerability-disclosure
- group: auth
  title: ''
  type: DomainSecurity
  url: security/anchorage-digital-domain-security.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/anchorage-digital-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/anchorage-digital-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/anchorage-digital-well-known.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/anchorage-digital-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/anchorage-digital-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/anchorage-digital-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/anchorage-digital-rate-limits.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/anchorage-digital-conformance.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/anchorage-digital-sandbox.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/anchorage-digital-webhooks.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/anchorage-digital-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.anchorage.com/knowledge-base/api-reference/changelog
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/anchorage-digital-changelog.yml
created: '2026-07-17'
description: Anchorage Digital is a regulated digital-asset platform for institutions, operating Anchorage Digital Bank, N.A. — the first federally chartered (OCC) crypto bank in the United States — plus regulated entities in Singapore and New York. It provides qualified custody, trading (Anchorage Digital Prime), staking, on-chain settlement via the Atlas Settlement Network, stablecoin issuance and conversion, governance participation, and tax reporting. Its REST API v2.0 exposes 134 operations across custody, wallets, transfers, trading, Atlas settlement, onboarding, subaccounts, tax, and webhook notifications, secured with API keys plus Ed25519 request signing. Anchorage also ships an Agentic Banking product with a hosted MCP server that lets AI agents spend against pre-authorized budgets.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/anchorage-digital.png
layout: provider
mcp_servers:
- description: ''
  name: anchorage-digital-mcp.yml
  slug: anchorage-digital-mcpyml
modified: '2026-07-17'
name: Anchorage Digital
nav: Providers
network: true
overview: 'Anchorage Digital publishes 20 APIs on the [APIs.io](https://apis.io/) network, including Addresses API, API Key API, Asset Types API, and 17 more. Tagged areas include Company, Crypto, Custody, Digital Assets, and Banking.


  The Anchorage Digital catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Anchorage Digital''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, authentication, sandbox, and 25 more developer resources.'
random_paper: 14
rate_limits:
- limit_count: 1
  name: Anchorage Digital Rate Limits
  slug: anchorage-digital-rate-limits
score:
  band: developing
  composite: 42.1
  delta: -8.7
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 16.7
    contract_quality: 68.2
    developer_ergonomics: 16.1
    discoverability: 68.5
    governance: 16.7
    operational_transparency: 57.9
  previous_composite: 50.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 20
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
screenshot: https://raw.githubusercontent.com/api-evangelist/anchorage-digital/refs/heads/main/screenshots/anchorage-digital-2026-07-25T200222.png
security:
- kind: authentication
  name: Anchorage Digital Authentication
  slug: anchorage-digital-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Anchorage Digital Domain Security
  slug: anchorage-digital-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Anchorage Digital Vulnerability Disclosure
  slug: anchorage-digital-vulnerability-disclosure
  summary_line: disclosure policy published
slug: anchorage-digital
tags:
- Company
- Crypto
- Custody
- Digital Assets
- Banking
- Trading
- Staking
- Settlement
- Institutional
- Blockchain
- Stablecoins
website: https://anchorage.com/
---
