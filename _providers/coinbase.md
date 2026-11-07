---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: true
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: verified
    mcp_server: platform
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: mostly
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 51.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 32
  human_in_the_loop: 0
  name: Coinbase Agentic Access
  operation_count: 95
  slug: coinbase-agentic-access
  summary_line: 95 operations · 32 acting
api_count: 4
apis:
- description: The Coinbase Wallet SDK allows developers to integrate Coinbase Wallet connectivity into decentralized applications. It provides a streamlined interface for users to connect their wallets, sign transa
  name: Coinbase Wallet SDK
  slug: wallet-sdk
- description: The Coinbase Data API provides developers with access to cryptocurrency market data, blockchain analytics, and pricing information. It delivers real-time and historical data for a wide range of digita
  name: Coinbase Data API
  slug: data-api
- description: Coinbase AgentKit is a toolkit that enables AI agents to interact with blockchain networks through secure wallet management and comprehensive onchain capabilities. Built on the Coinbase Developer Plat
  name: Coinbase AgentKit
  slug: agentkit
- baseURL: https://api.coinbase.com
  baseurl_source: declared
  description: Manage user accounts and retrieve account information including balances and holds.
  name: Coinbase Accounts API
  slug: coinbase-accounts-api
- baseURL: https://api.coinbase.com
  baseurl_source: declared
  description: View activity history for portfolios including trades, transfers, and other events.
  name: Coinbase Activities API
  slug: coinbase-activities-api
- baseURL: https://api.coinbase.com
  baseurl_source: declared
  description: Manage approved withdrawal addresses in the address book.
  name: Coinbase Address Book API
  slug: coinbase-address-book-api
- baseURL: https://api.coinbase.com
  baseurl_source: declared
  description: View and manage order allocations across sub-portfolios.
  name: Coinbase Allocations API
  slug: coinbase-allocations-api
- baseURL: https://api.coinbase.com
  baseurl_source: declared
  description: Retrieve information about supported assets and products.
  name: Coinbase Assets API
  slug: coinbase-assets-api
- baseURL: https://api.coinbase.com
  baseurl_source: declared
  description: Retrieve portfolio balance information across all assets.
  name: Coinbase Balances API
  slug: coinbase-balances-api
- baseURL: https://api.coinbase.com
  baseurl_source: declared
  description: Endpoints for discovering buy options, generating buy quotes, and retrieving buy configuration for fiat-to-crypto purchases.
  name: Coinbase Buy API
  slug: coinbase-buy-api
- baseURL: https://api.coinbase.com
  baseurl_source: declared
  description: Create and manage payment charges. A charge represents a request for cryptocurrency payment from a customer.
  name: Coinbase Charges API
  slug: coinbase-charges-api
- baseURL: https://api.coinbase.com
  baseurl_source: declared
  description: Create and manage reusable checkout pages for accepting recurring or standardized payments.
  name: Coinbase Checkouts API
  slug: coinbase-checkouts-api
- baseURL: https://api.coinbase.com
  baseurl_source: declared
  description: Retrieve webhook events that track the lifecycle of charges, checkouts, and invoices.
  name: Coinbase Events API
  slug: coinbase-events-api
- baseURL: https://api.coinbase.com
  baseurl_source: declared
  description: Create and manage invoices for billing customers with cryptocurrency payment options.
  name: Coinbase Invoices API
  slug: coinbase-invoices-api
- baseURL: https://api.coinbase.com
  baseurl_source: declared
  description: Create, cancel, and manage trading orders including market, limit, and stop-limit order types.
  name: Coinbase Orders API
  slug: coinbase-orders-api
- baseURL: https://api.coinbase.com
  baseurl_source: declared
  description: Create and manage portfolios for organizing trading activity and asset allocation.
  name: Coinbase Portfolios API
  slug: coinbase-portfolios-api
- baseURL: https://api.coinbase.com
  baseurl_source: declared
  description: Endpoints for discovering sell options and generating sell quotes for crypto-to-fiat transactions.
  name: Coinbase Sell API
  slug: coinbase-sell-api
- baseURL: https://api.coinbase.com
  baseurl_source: declared
  description: Manage session tokens for embedded onramp widget authentication.
  name: Coinbase Session API
  slug: coinbase-session-api
- baseURL: https://api.coinbase.com
  baseurl_source: declared
  description: View and create transactions including withdrawals and transfers.
  name: Coinbase Transactions API
  slug: coinbase-transactions-api
- baseURL: https://api.coinbase.com
  baseurl_source: declared
  description: Manage users associated with a portfolio.
  name: Coinbase Users API
  slug: coinbase-users-api
- baseURL: https://api.coinbase.com
  baseurl_source: declared
  description: Manage wallets within a portfolio for different asset types.
  name: Coinbase Wallets API
  slug: coinbase-wallets-api
- description: Core CDP API v2 for onchain wallets, payments, trading, faucets, policies, and JSON-RPC access, authenticated with short-lived JWTs.
  name: Coinbase Developer Platform (CDP) API
  slug: coinbase-developer-platform-cdp-api
- description: Programmatic spot trading, order management, and market data for the Coinbase retail exchange (Advanced Trade).
  name: Coinbase Advanced Trade API
  slug: coinbase-advanced-trade-api
- description: Retail Coinbase App API v2 for accounts, addresses, transactions, buys/sells, with OAuth2 and API-key HMAC authentication.
  name: Coinbase App API (Sign in with Coinbase)
  slug: coinbase-app-api-sign-in-with-coinbase
- description: Institutional/pro exchange REST and WebSocket API for order books, trading, and market data.
  name: Coinbase Exchange API
  slug: coinbase-exchange-api
- description: Institutional trading, custody, and portfolio management API for Coinbase Prime.
  name: Coinbase Prime API
  slug: coinbase-prime-api
- description: Crypto payments/checkout API for accepting cryptocurrency payments.
  name: Coinbase Commerce API
  slug: coinbase-commerce-api
- baseURL: https://api.coinbase.com
  baseurl_source: declared
  description: The Customers APIs enable developers to create and manage their end-user customers. Customers can be individuals or businesses and have various capabilities like sending/receiving fiat and crypto, tra
  name: Coinbase Customers API
  slug: coinbase-customers-api
- baseURL: https://api.coinbase.com
  baseurl_source: declared
  description: 'Deposit Destinations allow you to manage where funds can be deposited into your accounts. ## Crypto Deposit Destinations Crypto deposit destinations are cryptocurrency addresses that you can generate '
  name: Coinbase Deposit Destinations API
  slug: coinbase-deposit-destinations-api
- baseURL: https://api.coinbase.com
  baseurl_source: declared
  description: Send funds from a CDP account you own to a Coinbase user account or an onchain address. Use disbursements for standalone refunds, rebates, and other payouts that are not associated with a payment sess
  name: Coinbase Disbursements API
  slug: coinbase-disbursements-api
- baseURL: https://api.coinbase.com
  baseurl_source: declared
  description: The End User Account Management APIs enable developers to manage the accounts belonging to their end users. End user accounts are typically created by end users themselves when they sign in to the dev
  name: Coinbase End User Account Management API
  slug: coinbase-end-user-account-management-api
- baseURL: https://api.coinbase.com
  baseurl_source: declared
  description: The End User Accounts APIs enable end users to directly create, manage, and use their accounts. They are typically accessed via the CDP Web SDK, which handles end-user authentication and Temporary Wal
  name: Coinbase End User Accounts API
  slug: coinbase-end-user-accounts-api
- baseURL: https://api.coinbase.com
  baseurl_source: declared
  description: The EVM Account APIs enable you to create and use accounts across blockchains that are compatible with the Ethereum Virtual Machine (EVM). An **account** is a private/public key pair that is used to s
  name: Coinbase EVM Accounts API
  slug: coinbase-evm-accounts-api
- baseURL: https://api.coinbase.com
  baseurl_source: declared
  description: The EVM Smart Account APIs enable you to create and manage Smart Account wallets across EVM-compatible blockchains. A **Smart Account** is an EVM account that enables enhanced functionality such as ac
  name: Coinbase EVM Smart Accounts API
  slug: coinbase-evm-smart-accounts-api
- baseURL: https://api.coinbase.com
  baseurl_source: declared
  description: 'A swap refers to the act of exchanging one token for another. The EVM Swap APIs enable you to create and manage swaps. A swap process involves: 1. A user approves token spending via smart contract. 2.'
  name: Coinbase EVM Swaps API
  slug: coinbase-evm-swaps-api
- baseURL: https://api.coinbase.com
  baseurl_source: declared
  description: 'The EVM Token Balances APIs enable you to retrieve the balances of EVM addresses. This includes tokens (i.e. ERC-20s) and the native gas token of the network. ## Denomination - ''amount'' is denominated'
  name: Coinbase EVM Token Balances API
  slug: coinbase-evm-token-balances-api
- baseURL: https://api.coinbase.com
  baseurl_source: declared
  description: The Faucet APIs enable you to request funds on supported test networks. Faucets are for testing purposes and make development easier by providing a source of funds.
  name: Coinbase Faucets API
  slug: coinbase-faucets-api
- baseURL: https://api.coinbase.com
  baseurl_source: declared
  description: The `health.*` webhook payloads describe health status changes and maintenance window events for a CDP service or operation.
  name: Coinbase Health API
  slug: coinbase-health-api
- baseURL: https://api.coinbase.com
  baseurl_source: declared
  description: A mandate is a durable, revocable standing authorization to debit a funding `source`. It lets a merchant debit the same source repeatedly without the customer present, which suits recurring payments a
  name: Coinbase Mandates API
  slug: coinbase-mandates-api
- baseURL: https://api.coinbase.com
  baseurl_source: declared
  description: 'Query and analyze blockchain data with high performance and reliability. Features include real-time token balances, token discovery, and transaction history with freshness, accuracy, and completeness '
  name: Coinbase Onchain Data API
  slug: coinbase-onchain-data-api
- baseURL: https://api.coinbase.com
  baseurl_source: declared
  description: The v2 Onramp APIs are an evolution of our [v1 APIs](https://docs.cdp.coinbase.com/api-reference/rest-api/onramp-offramp/), designed to make the fiat-to-crypto experience feel native to your applicati
  name: Coinbase Onramp API
  slug: coinbase-onramp-api
- baseURL: https://api.coinbase.com
  baseurl_source: declared
  description: The Payment Methods APIs enable you to create and manage payment methods for accounts. Payment methods represent ways to send and receive payments, such as ACH transfers and Fedwire transfers. These A
  name: Coinbase Payment Methods API
  slug: coinbase-payment-methods-api
- baseURL: https://api.coinbase.com
  baseurl_source: declared
  description: Payment Sessions track the full lifecycle of a merchant payment, from authorization through capture, void, or refund. Each session records every operation and balance change across its lifecycle. **Wh
  name: Coinbase Payment Sessions API
  slug: coinbase-payment-sessions-api
- baseURL: https://api.coinbase.com
  baseurl_source: declared
  description: The Policy Engine APIs evaluate policies (a set of rules) to govern the behavior of accounts or projects, such as enforce allowlists and denylists. - A **policy** is a collection of `rules` with defin
  name: Coinbase Policy Engine API
  slug: coinbase-policy-engine-api
- baseURL: https://api.coinbase.com
  baseurl_source: declared
  description: 'The Solana Account APIs enable you to create and use Solana accounts across SVM-compatible blockchains. An **account** is a private/public key pair that is used to sign transactions and messages. The '
  name: Coinbase Solana Accounts API
  slug: coinbase-solana-accounts-api
- baseURL: https://api.coinbase.com
  baseurl_source: declared
  description: 'The Solana Token Balances APIs enable you to retrieve the balances of Solana addresses. This includes SPL tokens and the native SOL token of the network. ## Denomination - ''amount'' is denominated in t'
  name: Coinbase Solana Token Balances API
  slug: coinbase-solana-token-balances-api
- baseURL: https://api.coinbase.com
  baseurl_source: declared
  description: The SQL API enables you to write performant, high-freshness, and endlessly flexible SQL queries against onchain data.
  name: Coinbase SQL API
  slug: coinbase-sql-api-api
- baseURL: https://api.coinbase.com
  baseurl_source: declared
  description: A Top-Up Link is a shareable hosted URL that lets a payer add funds to their balance. Create a link with **Create a Top-Up Link** and share the returned `topUpUrl` only with the intended payer. The UR
  name: Coinbase Top-Up Links API
  slug: coinbase-top-up-links-api
- baseURL: https://api.coinbase.com
  baseurl_source: declared
  description: '**Transfers** represent both the request and execution of fund transfers from a source to a target. They provide upfront fee quotes and track the complete lifecycle from initiation through completion,'
  name: Coinbase Transfers API
  slug: coinbase-transfers-api
- baseURL: https://api.coinbase.com
  baseurl_source: declared
  description: The `wallet.activity.*` webhook payloads describe wallet activity, transaction, delegation, and signing events emitted by CDP.
  name: Coinbase Wallet Webhooks API
  slug: coinbase-wallet-webhooks-api
- baseURL: https://api.coinbase.com
  baseurl_source: declared
  description: Subscribe to real-time events across CDP products. Monitor onchain activity on Base mainnet, track onramp/offramp transactions, and receive instant notifications for wallet events.
  name: Coinbase Webhooks API
  slug: coinbase-webhooks-api
- baseURL: https://api.coinbase.com
  baseurl_source: declared
  description: The x402 payment protocol is an HTTP-based payment protocol that enables developers running resource servers to accept payments from users using a variety of payment methods. For more details on the x
  name: Coinbase x402 Facilitator API
  slug: coinbase-x402-facilitator-api
artifact_total: 192
asyncapis:
- description: The Coinbase Advanced Trade WebSocket API provides real-time market data streaming including heartbeats, ticker updates, candle data, market trades, level2 order book updates, and user order status ch
  name: Coinbase Advanced Trade WebSocket
  slug: coinbase-advanced-trade-asyncapi
- description: Coinbase Commerce sends webhook events to notify your application when charges are created, confirmed, delayed, pending, failed, or resolved. Each webhook event is signed with a SHA-256 HMAC signature
  name: Coinbase Commerce Webhooks
  slug: coinbase-commerce-webhooks-asyncapi
- description: The Coinbase Exchange WebSocket Feed provides real-time market data for the Exchange platform. It supports multiple channels including heartbeat, ticker, level2 order book, full order feed, and user o
  name: Coinbase Exchange WebSocket Feed
  slug: coinbase-exchange-asyncapi
- description: ''
  name: Coinbase Webhooks
  slug: coinbase-webhooks
collections:
- collection_type: postman
  name: Coinbase Advanced Trade Accounts API
  slug: postman-coinbase-accounts-api
- collection_type: postman
  name: Coinbase Advanced Trade Accounts Activities API
  slug: postman-coinbase-activities-api
- collection_type: postman
  name: Coinbase Advanced Trade Accounts Address Book API
  slug: postman-coinbase-address-book-api
- collection_type: postman
  name: Coinbase Advanced Trade Accounts Allocations API
  slug: postman-coinbase-allocations-api
- collection_type: postman
  name: Coinbase Advanced Trade Accounts Assets API
  slug: postman-coinbase-assets-api
- collection_type: postman
  name: Coinbase Advanced Trade Accounts Balances API
  slug: postman-coinbase-balances-api
- collection_type: postman
  name: Coinbase Advanced Trade Accounts Buy API
  slug: postman-coinbase-buy-api
- collection_type: postman
  name: Coinbase Advanced Trade Accounts Charges API
  slug: postman-coinbase-charges-api
- collection_type: postman
  name: Coinbase Advanced Trade Accounts Checkouts API
  slug: postman-coinbase-checkouts-api
- collection_type: postman
  name: Coinbase Advanced Trade Accounts Conversions API
  slug: postman-coinbase-conversions-api
- collection_type: postman
  name: Coinbase Advanced Trade Accounts Currencies API
  slug: postman-coinbase-currencies-api
- collection_type: postman
  name: Coinbase Advanced Trade Accounts Deposits API
  slug: postman-coinbase-deposits-api
- collection_type: postman
  name: Coinbase Advanced Trade Accounts Events API
  slug: postman-coinbase-events-api
- collection_type: postman
  name: Coinbase Advanced Trade Accounts Fees API
  slug: postman-coinbase-fees-api
- collection_type: postman
  name: Coinbase Advanced Trade Accounts Invoices API
  slug: postman-coinbase-invoices-api
- collection_type: postman
  name: Coinbase Advanced Trade Accounts Market Data API
  slug: postman-coinbase-market-data-api
- collection_type: postman
  name: Coinbase Advanced Trade Accounts Orders API
  slug: postman-coinbase-orders-api
- collection_type: postman
  name: Coinbase Advanced Trade Accounts Portfolios API
  slug: postman-coinbase-portfolios-api
- collection_type: postman
  name: Coinbase Advanced Trade Accounts Products API
  slug: postman-coinbase-products-api
- collection_type: postman
  name: Coinbase Advanced Trade Accounts Profiles API
  slug: postman-coinbase-profiles-api
- collection_type: postman
  name: Coinbase Advanced Trade Accounts Sell API
  slug: postman-coinbase-sell-api
- collection_type: postman
  name: Coinbase Advanced Trade Accounts Session API
  slug: postman-coinbase-session-api
- collection_type: postman
  name: Coinbase Advanced Trade Accounts Transactions API
  slug: postman-coinbase-transactions-api
- collection_type: postman
  name: Coinbase Advanced Trade Accounts Users API
  slug: postman-coinbase-users-api
- collection_type: postman
  name: Coinbase Advanced Trade Accounts Wallets API
  slug: postman-coinbase-wallets-api
- collection_type: postman
  name: Coinbase Advanced Trade Accounts Withdrawals API
  slug: postman-coinbase-withdrawals-api
- collection_type: open
  name: Coinbase Advanced Trade Accounts API
  slug: open-coinbase-accounts-api
- collection_type: open
  name: Coinbase Advanced Trade Accounts Activities API
  slug: open-coinbase-activities-api
- collection_type: open
  name: Coinbase Advanced Trade Accounts Address Book API
  slug: open-coinbase-address-book-api
- collection_type: open
  name: Coinbase Advanced Trade API
  slug: open-coinbase-advanced-trade
- collection_type: open
  name: Coinbase Advanced Trade Accounts Allocations API
  slug: open-coinbase-allocations-api
- collection_type: open
  name: Coinbase Advanced Trade Accounts Assets API
  slug: open-coinbase-assets-api
- collection_type: open
  name: Coinbase Advanced Trade Accounts Balances API
  slug: open-coinbase-balances-api
- collection_type: open
  name: Coinbase Advanced Trade Accounts Buy API
  slug: open-coinbase-buy-api
- collection_type: open
  name: Coinbase Advanced Trade Accounts Charges API
  slug: open-coinbase-charges-api
- collection_type: open
  name: Coinbase Advanced Trade Accounts Checkouts API
  slug: open-coinbase-checkouts-api
- collection_type: open
  name: Coinbase Commerce API
  slug: open-coinbase-commerce
- collection_type: open
  name: Coinbase Advanced Trade Accounts Conversions API
  slug: open-coinbase-conversions-api
- collection_type: open
  name: Coinbase Advanced Trade Accounts Currencies API
  slug: open-coinbase-currencies-api
- collection_type: open
  name: Coinbase Advanced Trade Accounts Deposits API
  slug: open-coinbase-deposits-api
- collection_type: open
  name: Coinbase Advanced Trade Accounts Events API
  slug: open-coinbase-events-api
- collection_type: open
  name: Coinbase Exchange API
  slug: open-coinbase-exchange
- collection_type: open
  name: Coinbase Advanced Trade Accounts Fees API
  slug: open-coinbase-fees-api
- collection_type: open
  name: Coinbase Advanced Trade Accounts Invoices API
  slug: open-coinbase-invoices-api
- collection_type: open
  name: Coinbase Advanced Trade Accounts Market Data API
  slug: open-coinbase-market-data-api
- collection_type: open
  name: Coinbase Onramp API
  slug: open-coinbase-onramp
- collection_type: open
  name: Coinbase Advanced Trade Accounts Orders API
  slug: open-coinbase-orders-api
- collection_type: open
  name: Coinbase Advanced Trade Accounts Portfolios API
  slug: open-coinbase-portfolios-api
- collection_type: open
  name: Coinbase Prime API
  slug: open-coinbase-prime
- collection_type: open
  name: Coinbase Advanced Trade Accounts Products API
  slug: open-coinbase-products-api
- collection_type: open
  name: Coinbase Advanced Trade Accounts Profiles API
  slug: open-coinbase-profiles-api
- collection_type: open
  name: Coinbase Advanced Trade Accounts Sell API
  slug: open-coinbase-sell-api
- collection_type: open
  name: Coinbase Advanced Trade Accounts Session API
  slug: open-coinbase-session-api
- collection_type: open
  name: Coinbase Advanced Trade Accounts Transactions API
  slug: open-coinbase-transactions-api
- collection_type: open
  name: Coinbase Advanced Trade Accounts Users API
  slug: open-coinbase-users-api
- collection_type: open
  name: Coinbase Advanced Trade Accounts Wallets API
  slug: open-coinbase-wallets-api
- collection_type: open
  name: Coinbase Advanced Trade Accounts Withdrawals API
  slug: open-coinbase-withdrawals-api
common:
- group: design
  href: https://artifacts.apis.io/coinbase/conventions/coinbase-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/coinbase-conventions.yml
- group: design
  href: https://artifacts.apis.io/coinbase/conventions/coinbase-conventions.yml
  title: ''
  type: Conventions
  url: conventions/coinbase-conventions.yml
- group: design
  href: https://artifacts.apis.io/coinbase/rules/coinbase-rules.yml
  title: ''
  type: Spectral
  url: rules/coinbase-rules.yml
- group: design
  href: https://artifacts.apis.io/coinbase/rules/coinbase-jsonschema-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/coinbase-jsonschema-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/coinbase/rules/coinbase-asyncapi-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/coinbase-asyncapi-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/coinbase/vocabulary/coinbase-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/coinbase-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/coinbase/asyncapi/coinbase-commerce-webhooks-asyncapi.yml
  title: ''
  type: Webhooks
  url: asyncapi/coinbase-commerce-webhooks-asyncapi.yml
- group: design
  href: https://artifacts.apis.io/coinbase/data-model/coinbase-data-model.yml
  title: ''
  type: DataModel
  url: data-model/coinbase-data-model.yml
- group: auth
  href: https://artifacts.apis.io/coinbase/security/coinbase-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/coinbase-vulnerability-disclosure.yml
- group: design
  href: https://artifacts.apis.io/coinbase/errors/coinbase-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/coinbase-problem-types.yml
- group: design
  href: https://artifacts.apis.io/coinbase/conformance/coinbase-conformance.yml
  title: ''
  type: Conformance
  url: conformance/coinbase-conformance.yml
- group: agent
  href: https://artifacts.apis.io/coinbase/llms/coinbase-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/coinbase-llms.txt
- group: agent
  href: https://artifacts.apis.io/coinbase/mcp/coinbase-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/coinbase-mcp.yml
- group: build
  href: https://artifacts.apis.io/coinbase/integrations/coinbase-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/coinbase-integration-edges.yml
- group: commercial
  href: https://artifacts.apis.io/coinbase/plans/coinbase-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/coinbase-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/coinbase/rate-limits/coinbase-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/coinbase-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/coinbase/finops/coinbase-finops.yml
  title: ''
  type: FinOps
  url: finops/coinbase-finops.yml
- group: other
  href: https://artifacts.apis.io/coinbase/capabilities/coinbase-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/coinbase-capability-edges.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/coinbase/overview
- group: agent
  href: https://artifacts.apis.io/coinbase/agentic-access/coinbase-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/coinbase-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/coinbase/security/coinbase-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/coinbase-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/coinbase/security/coinbase-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/coinbase-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/coinbase/authentication/coinbase-authentication.yml
  title: ''
  type: Authentication
  url: authentication/coinbase-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/coinbase
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.coinbase.com/developer-platform
- group: docs
  title: ''
  type: Documentation
  url: https://docs.cdp.coinbase.com/
- group: company
  title: ''
  type: Website
  url: https://www.coinbase.com/
- group: company
  title: ''
  type: Blog
  url: https://www.coinbase.com/blog
- group: build
  title: ''
  type: GitHub
  url: https://github.com/coinbase
- group: start
  title: ''
  type: Login
  url: https://login.coinbase.com/
- group: operate
  title: ''
  type: Support
  url: https://help.coinbase.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.coinbase.com/legal/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.coinbase.com/legal/user-agreement
- group: design
  href: https://artifacts.apis.io/coinbase/json-ld/coinbase-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/coinbase-context.jsonld
- group: docs
  href: https://artifacts.apis.io/coinbase/json-schema/coinbase-order-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/coinbase-order-schema.json
- group: docs
  href: https://artifacts.apis.io/coinbase/json-schema/coinbase-charge-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/coinbase-charge-schema.json
- group: docs
  href: https://artifacts.apis.io/coinbase/json-schema/coinbase-product-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/coinbase-product-schema.json
- group: design
  href: https://artifacts.apis.io/coinbase/rules/coinbase-rules.yml
  title: ''
  type: Spectral Ruleset
  url: rules/coinbase-rules.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.cdp.coinbase.com/llms.txt
- group: build
  href: https://artifacts.apis.io/coinbase/packages/coinbase-packages.yml
  title: ''
  type: Packages
  url: packages/coinbase-packages.yml
- group: build
  href: https://artifacts.apis.io/coinbase/packages/coinbase-packages.yml
  title: ''
  type: SDKs
  url: packages/coinbase-packages.yml
- group: build
  href: https://artifacts.apis.io/coinbase/cli/coinbase-cli.yml
  title: ''
  type: CLI
  url: cli/coinbase-cli.yml
- group: agent
  href: https://artifacts.apis.io/coinbase/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/coinbase/well-known/coinbase-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/coinbase-well-known.yml
- group: auth
  href: https://artifacts.apis.io/coinbase/well-known/coinbase-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/coinbase-security.txt
- group: design
  href: https://artifacts.apis.io/coinbase/asyncapi/coinbase-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/coinbase-webhooks.yml
created: '2026-03-20'
description: Coinbase is a leading cryptocurrency platform providing trading, custody, and payment infrastructure for individuals, businesses, and institutions. The Coinbase Developer Platform (CDP) exposes a wide product surface across retail trading (Advanced Trade), professional and institutional trading (Exchange and Prime), merchant payments (Commerce), fiat onboarding (Onramp), developer wallet integration (Wallet SDK), market and on-chain data (Data API), and AI agent toolkits (AgentKit). Authentication is performed using API keys with HMAC-SHA256 signatures (Advanced Trade, Exchange) or JWT bearer tokens (Prime, CDP), with WebSocket and FIX feeds available for low-latency market data and order management.
finops:
- has_sources: true
  method: generated
  name: Coinbase Finops
  primary_unit: ''
  service_category: Financial Services
  slug: coinbase-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/coinbase.png
json_schemas:
- name: Account
  property_count: 11
  slug: coinbase-account
- name: Activity
  property_count: 8
  slug: coinbase-activity
- name: AddressBookEntry
  property_count: 5
  slug: coinbase-address-book-entry
- name: AddressBookEntry
  property_count: 5
  slug: coinbase-addressbookentry
- name: Allocation
  property_count: 10
  slug: coinbase-allocation
- name: Balance
  property_count: 2
  slug: coinbase-balance
- name: BuyConfig
  property_count: 1
  slug: coinbase-buy-config
- name: BuyQuoteRequest
  property_count: 6
  slug: coinbase-buy-quote-request
- name: BuyQuote
  property_count: 6
  slug: coinbase-buy-quote
- name: BuyConfig
  property_count: 1
  slug: coinbase-buyconfig
- name: BuyQuote
  property_count: 6
  slug: coinbase-buyquote
- name: BuyQuoteRequest
  property_count: 6
  slug: coinbase-buyquoterequest
- name: Candle
  property_count: 6
  slug: coinbase-candle
- name: Coinbase Commerce Charge
  property_count: 17
  slug: coinbase-charge
- name: Checkout
  property_count: 7
  slug: coinbase-checkout
- name: Conversion
  property_count: 6
  slug: coinbase-conversion
- name: CreateChargeRequest
  property_count: 7
  slug: coinbase-create-charge-request
- name: CreateCheckoutRequest
  property_count: 5
  slug: coinbase-create-checkout-request
- name: CreateInvoiceRequest
  property_count: 5
  slug: coinbase-create-invoice-request
- name: CreateOrderRequest_3
  property_count: 10
  slug: coinbase-create-order-request-3
- name: CreateChargeRequest
  property_count: 7
  slug: coinbase-createchargerequest
- name: CreateCheckoutRequest
  property_count: 5
  slug: coinbase-createcheckoutrequest
- name: CreateInvoiceRequest
  property_count: 5
  slug: coinbase-createinvoicerequest
- name: CreateOrderRequest
  property_count: 4
  slug: coinbase-createorderrequest
- name: Currency
  property_count: 5
  slug: coinbase-currency
- name: Event
  property_count: 6
  slug: coinbase-event
- name: Fill_2
  property_count: 10
  slug: coinbase-fill-2
- name: Fill_3
  property_count: 10
  slug: coinbase-fill-3
- name: Fill
  property_count: 10
  slug: coinbase-fill
- name: Hold
  property_count: 5
  slug: coinbase-hold
- name: Invoice
  property_count: 11
  slug: coinbase-invoice
- name: LedgerEntry
  property_count: 6
  slug: coinbase-ledger-entry
- name: LedgerEntry
  property_count: 6
  slug: coinbase-ledgerentry
- name: Order_3
  property_count: 15
  slug: coinbase-order-3
- name: OrderBook
  property_count: 3
  slug: coinbase-order-book
- name: Coinbase Order
  property_count: 22
  slug: coinbase-order
- name: OrderBook
  property_count: 3
  slug: coinbase-orderbook
- name: Pagination
  property_count: 6
  slug: coinbase-pagination
- name: PaymentCurrency
  property_count: 5
  slug: coinbase-payment-currency
- name: PaymentMethod
  property_count: 8
  slug: coinbase-payment-method
- name: Payment
  property_count: 5
  slug: coinbase-payment
- name: PaymentCurrency
  property_count: 5
  slug: coinbase-paymentcurrency
- name: PaymentMethod
  property_count: 8
  slug: coinbase-paymentmethod
- name: PortfolioBreakdown
  property_count: 3
  slug: coinbase-portfolio-breakdown
- name: Portfolio
  property_count: 4
  slug: coinbase-portfolio
- name: PortfolioBreakdown
  property_count: 3
  slug: coinbase-portfoliobreakdown
- name: PriceBook
  property_count: 4
  slug: coinbase-price-book
- name: PriceBook
  property_count: 4
  slug: coinbase-pricebook
- name: Coinbase Trading Product
  property_count: 20
  slug: coinbase-product
- name: Profile
  property_count: 6
  slug: coinbase-profile
- name: PurchaseCurrency
  property_count: 5
  slug: coinbase-purchase-currency
- name: PurchaseCurrency
  property_count: 5
  slug: coinbase-purchasecurrency
- name: SellQuoteRequest
  property_count: 5
  slug: coinbase-sell-quote-request
- name: SellQuote
  property_count: 4
  slug: coinbase-sell-quote
- name: SellQuote
  property_count: 4
  slug: coinbase-sellquote
- name: SellQuoteRequest
  property_count: 5
  slug: coinbase-sellquoterequest
- name: Ticker
  property_count: 7
  slug: coinbase-ticker
- name: Trade_2
  property_count: 5
  slug: coinbase-trade-2
- name: Trade
  property_count: 6
  slug: coinbase-trade
- name: Transaction
  property_count: 11
  slug: coinbase-transaction
- name: TransactionSummary
  property_count: 5
  slug: coinbase-transaction-summary
- name: TransactionSummary
  property_count: 5
  slug: coinbase-transactionsummary
- name: Transfer
  property_count: 6
  slug: coinbase-transfer
- name: User
  property_count: 4
  slug: coinbase-user
- name: Wallet
  property_count: 5
  slug: coinbase-wallet
json_structures:
- name: Coinbase Structure
  property_count: 0
  slug: coinbase-structure
jsonld:
- class_count: 0
  name: Coinbase Context
  property_count: 9
  slug: coinbase-context
layout: provider
mcp_servers:
- description: Remote MCP server at docs.cdp.coinbase.com over HTTP; 3 tools listed.
  name: Coinbase MCP Server
  slug: coinbase
modified: '2026-05-19'
name: Coinbase
nav: Providers
network: true
overview: 'Coinbase publishes 52 API contracts indexed on the [APIs.io](https://apis.io/) network, including Accounts API, Activities API, Address Book API, and 49 more. Tagged areas include Blockchain, Cryptocurrency, Custody, Exchange, and On-Ramp.


  The Coinbase catalog on APIs.io includes 4 event-driven AsyncAPI specifications, 1 JSON-LD context, and 3 Spectral governance rulesets.


  Coinbase''s developer surface includes authentication, documentation, engineering blog, GitHub presence, support, CLI, and 40 more developer resources.'
plans:
- name: Coinbase Plans Pricing
  plan_count: 11
  slug: coinbase-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 4
  name: Coinbase Rate Limits
  slug: coinbase-rate-limits
rules:
- authorship: generated
  effective_rule_count: 35
  extends:
  - spectral:asyncapi
  name: Coinbase — asyncapi rules
  rule_count: 8
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 7
  slug: coinbase-asyncapi-spectral-rules
- authorship: generated
  effective_rule_count: 6
  extends: []
  name: Coinbase — jsonschema rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: coinbase-jsonschema-spectral-rules
- authorship: unmarked
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: Coinbase API Rules
  rule_count: 12
  severity_counts:
    error: 5
    hint: 0
    info: 2
    warn: 5
  slug: coinbase-rules
score:
  band: strong
  composite: 56.6
  coverage:
    artifact_dirs: 33
    catalog_earned: 64.0
    catalog_earned_first_party: 0.0
    catalog_gap: 51.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.7
  facets:
    access_clarity: 25.0
    contract_governance: 31.8
    contract_quality: 74.0
    developer_ergonomics: 67.9
    discoverability: 71.7
    operational_transparency: 31.6
  previous_composite: 55.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 44.4
      total: 54
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 27.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 38.9
screenshot: https://apis.io/screenshots/coinbase/coinbase-2026-06-20T174726.png
security:
- kind: authentication
  name: Coinbase Authentication
  slug: coinbase-authentication
  summary_line: apiKey/http · 4 schemes
- kind: domain-security
  name: Coinbase Domain Security
  slug: coinbase-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Coinbase Vulnerability Disclosure
  slug: coinbase-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
skill_count: 1
skills:
- name: cdp-setup
  slug: coinbase-cdp-setup
slug: coinbase
tags:
- Blockchain
- Cryptocurrency
- Custody
- Exchange
- On-Ramp
- Payments
- Trading
- Wallets
- Web3
- Agentic Commerce
- x402
- Real-Time
website: https://www.coinbase.com/
---
