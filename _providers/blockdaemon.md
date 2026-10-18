---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: unknown
    idempotency: verified
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 45.3
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 161
  human_in_the_loop: 0
  name: Blockdaemon Agentic Access
  operation_count: 363
  slug: blockdaemon-agentic-access
  summary_line: 363 operations · 161 acting
api_count: 15
apis:
- description: Unified, multi-chain REST data API (formerly Ubiquity) providing fully indexed blockchain data across 50+ networks. Lookup blocks by number or hash, fetch transactions, account balances for one or man
  name: Blockdaemon Data API
  slug: blockdaemon-data-api
- description: Production-ready shared and dedicated JSON-RPC and REST node endpoints across 50+ protocols including Bitcoin, Ethereum, Solana, Polygon, Arbitrum, Avalanche, Base, Optimism, Cosmos, Polkadot, NEAR, C
  name: Blockdaemon RPC API
  slug: blockdaemon-rpc-api
- description: 'Institutional staking-as-a-service API for creating validators and signed staking, unstaking, delegation, consolidation, exit, and reward-claim transactions across Ethereum, Solana, Cosmos, Polkadot, '
  name: Blockdaemon Staking API
  slug: blockdaemon-staking-api
- description: Standardized staking-reward and yield-reporting API delivering historical and current stake, validator status, reward, slashing, and financial summaries across all supported PoS networks for audit, ac
  name: Blockdaemon Staking Reporting API
  slug: blockdaemon-staking-reporting-api
- description: Single REST interface (formerly Expand Network) into multiple DeFi protocols — DEX swaps and aggregation across 200+ DEXs, cross-chain bridge swaps and aggregation, and lending/borrowing on Aave V2/V3
  name: Blockdaemon DeFi API
  slug: blockdaemon-defi-api
- description: Token metadata, tag, and pricing API — name, symbol, decimals, logo URI, and category tags (e.g., stablecoins) with token quote pricing for display, filtering, and FX calculations across supported EVM
  name: Blockdaemon Token Pricing API
  slug: blockdaemon-token-pricing-api
- description: Real-time push-based on-chain event streaming for institutional wallets and finance systems. Configure Targets (webhook/Kafka/WebSocket), Rules, Variables, and Variable Values to monitor transactions,
  name: Blockdaemon Chain Watch Events API
  slug: blockdaemon-events-api
- baseURL: https://svc.blockdaemon.com
  baseurl_source: spec
  description: 'Programmatic access to current period Compute Unit usage, request usage, and organization audit logs. Powers usage dashboards, FinOps reporting, and quota alerting for organizations subscribed to the '
  name: Blockdaemon Management API
  slug: blockdaemon-management-api
- description: A wallet-application toolbox for scaling wallet operations on top of indexed multi-chain infrastructure. Combines balance lookups, transaction construction, broadcasting, and event streaming for custo
  name: Blockdaemon Wallet Transact API
  slug: blockdaemon-wallet-transact-api
- description: Threshold Signature Scheme (TSM) MPC wallet platform for builders. Customizable, deployable on-premises or in cloud, with EVM Web3 provider, Kubernetes Helm chart, and reference integrations for ERC-t
  name: Blockdaemon Builder Vault TSM
  slug: blockdaemon-builder-vault-tsm
- description: Self-hosted MPC wallet for institutional hot, warm, and cold storage with granular governance, transaction policies, role-based approvals, and an Automated Approver Service for policy-driven signing.
  name: Blockdaemon Institutional Vault
  slug: blockdaemon-institutional-vault
- baseURL: https://svc.blockdaemon.com/pricing/v1
  baseurl_source: spec
  description: The pricing API from Blockdaemon — 3 operation(s) for pricing.
  name: Blockdaemon Pricing API
  slug: blockdaemon-pricing-api
- baseURL: https://svc.blockdaemon.com
  baseurl_source: spec
  description: The aa API from Blockdaemon — 4 operation(s) for aa.
  name: Blockdaemon Aa API
  slug: blockdaemon-aa-api
- baseURL: https://svc.blockdaemon.com
  baseurl_source: spec
  description: API endpoints for fetching information about account
  name: Blockdaemon Account API
  slug: blockdaemon-account-api
- baseURL_template: '{server}'
  baseurl_source: spec_template
  description: API key management operations
  name: Blockdaemon API Keys API
  slug: blockdaemon-api-keys-api
- baseURL: https://svc.blockdaemon.com/boss
  baseurl_source: spec
  description: Avalanche endpoints
  name: Blockdaemon Avalanche API
  slug: blockdaemon-avalanche-api
- baseURL_template: https://svc.blockdaemon.com/universal/{version}
  baseurl_source: spec_template
  description: The Balances & UTXO API from Blockdaemon — 5 operation(s) for balances & utxo.
  name: Blockdaemon Balances & UTXO API
  slug: blockdaemon-balances-utxo-api
- baseURL: https://svc.blockdaemon.com/boss
  baseurl_source: spec
  description: Binance endpoints
  name: Blockdaemon Binance API
  slug: blockdaemon-binance-api
- baseURL_template: https://svc.blockdaemon.com/universal/{version}
  baseurl_source: spec_template
  description: The Blocks API from Blockdaemon — 7 operation(s) for blocks.
  name: Blockdaemon Blocks API
  slug: blockdaemon-blocks-api
- baseURL: https://svc.blockdaemon.com
  baseurl_source: spec
  description: API endpoints for operations related to bridges
  name: Blockdaemon Bridge API
  slug: blockdaemon-bridge-api
- baseURL: https://svc.blockdaemon.com/boss
  baseurl_source: spec
  description: Cardano endpoints
  name: Blockdaemon Cardano API
  slug: blockdaemon-cardano-api
- baseURL: https://svc.blockdaemon.com/reporting/staking
  baseurl_source: spec
  description: The Cardano Staking Reporting API from Blockdaemon — 8 operation(s) for cardano staking reporting.
  name: Blockdaemon Cardano Staking Reporting API
  slug: blockdaemon-cardano-staking-reporting-api
- baseURL: https://svc.blockdaemon.com
  baseurl_source: spec
  description: API endpoints for fetching information about blockchains
  name: Blockdaemon Chain API
  slug: blockdaemon-chain-api
- baseURL: https://svc.blockdaemon.com/tx/v1
  baseurl_source: spec
  description: The Compile And Send API from Blockdaemon — 1 operation(s) for compile and send.
  name: Blockdaemon Compile And Send API
  slug: blockdaemon-compile-and-send-api
- baseURL: https://svc.blockdaemon.com/tx/v1
  baseurl_source: spec
  description: The Compile API from Blockdaemon — 1 operation(s) for compile.
  name: Blockdaemon Compile API
  slug: blockdaemon-compile-api
- baseURL_template: '{server}'
  baseurl_source: spec_template
  description: Configuration information operations
  name: Blockdaemon Configuration API
  slug: blockdaemon-configuration-api
- baseURL: https://svc.blockdaemon.com/boss
  baseurl_source: spec
  description: Cosmos endpoints
  name: Blockdaemon Cosmos API
  slug: blockdaemon-cosmos-api
- baseURL: https://svc.blockdaemon.com/reporting/staking
  baseurl_source: spec
  description: The Cosmos Staking Reporting API from Blockdaemon — 6 operation(s) for cosmos staking reporting.
  name: Blockdaemon Cosmos Staking Reporting API
  slug: blockdaemon-cosmos-staking-reporting-api
- baseURL: https://svc.blockdaemon.com/tx/v1
  baseurl_source: spec
  description: The Create API from Blockdaemon — 2 operation(s) for create.
  name: Blockdaemon Create API
  slug: blockdaemon-create-api
- baseURL: https://svc.blockdaemon.com/tx/v1
  baseurl_source: spec
  description: The Decode API from Blockdaemon — 1 operation(s) for decode.
  name: Blockdaemon Decode API
  slug: blockdaemon-decode-api
- baseURL: https://svc.blockdaemon.com/tx/v1
  baseurl_source: spec
  description: The Derive Signing Payload API from Blockdaemon — 1 operation(s) for derive signing payload.
  name: Blockdaemon Derive Signing Payload API
  slug: blockdaemon-derive-signing-payload-api
- baseURL: https://svc.blockdaemon.com
  baseurl_source: spec
  description: API endpoints for operations related to decentralized exchange
  name: Blockdaemon Dex API
  slug: blockdaemon-dex-api
- baseURL: https://svc.blockdaemon.com/tx/v1
  baseurl_source: spec
  description: The Estimate Fee API from Blockdaemon — 1 operation(s) for estimate fee.
  name: Blockdaemon Estimate Fee API
  slug: blockdaemon-estimate-fee-api
- baseURL: https://svc.blockdaemon.com/boss
  baseurl_source: spec
  description: Ethereum endpoints
  name: Blockdaemon Ethereum API
  slug: blockdaemon-ethereum-api
- baseURL: https://svc.blockdaemon.com/reporting/staking
  baseurl_source: spec
  description: The Ethereum Staking Reporting API from Blockdaemon — 10 operation(s) for ethereum staking reporting.
  name: Blockdaemon Ethereum Staking Reporting API
  slug: blockdaemon-ethereum-staking-reporting-api
- baseURL_template: https://svc.blockdaemon.com/universal/{version}
  baseurl_source: spec_template
  description: The Fee estimator API from Blockdaemon — 1 operation(s) for fee estimator.
  name: Blockdaemon Fee estimator API
  slug: blockdaemon-fee-estimator-api
- baseURL: https://svc.blockdaemon.com
  baseurl_source: spec
  description: API endpoints for operations related to fungible tokens
  name: Blockdaemon Fungibletoken API
  slug: blockdaemon-fungibletoken-api
- baseURL: https://svc.blockdaemon.com/boss
  baseurl_source: spec
  description: General endpoints
  name: Blockdaemon General API
  slug: blockdaemon-general-api
- baseURL_template: '{server}'
  baseurl_source: spec_template
  description: Health check operations
  name: Blockdaemon Health API
  slug: blockdaemon-health-api
- baseURL: https://svc.blockdaemon.com
  baseurl_source: spec
  description: API endpoints for operations related to lending and borrowing
  name: Blockdaemon Lendborrow API
  slug: blockdaemon-lendborrow-api
- baseURL: https://svc.blockdaemon.com
  baseurl_source: spec
  description: The liquidstaking API from Blockdaemon — 20 operation(s) for liquidstaking.
  name: Blockdaemon Liquidstaking API
  slug: blockdaemon-liquidstaking-api
- baseURL: https://svc.blockdaemon.com
  baseurl_source: spec
  description: Management APIs
  name: Blockdaemon Management API
  slug: blockdaemon-management-api
- baseURL_template: '{server}'
  baseurl_source: spec_template
  description: System metrics operations
  name: Blockdaemon Metrics API
  slug: blockdaemon-metrics-api
- baseURL: https://svc.blockdaemon.com
  baseurl_source: spec
  description: The Native API from Blockdaemon — 1 operation(s) for native.
  name: Blockdaemon Native API
  slug: blockdaemon-native-api
- baseURL: https://svc.blockdaemon.com/boss
  baseurl_source: spec
  description: Near endpoints
  name: Blockdaemon NEAR API
  slug: blockdaemon-near-api
- baseURL: https://svc.blockdaemon.com
  baseurl_source: spec
  description: The nft API from Blockdaemon — 5 operation(s) for nft.
  name: Blockdaemon Nft API
  slug: blockdaemon-nft-api
- baseURL: https://svc.blockdaemon.com
  baseurl_source: spec
  description: The oracle API from Blockdaemon — 2 operation(s) for oracle.
  name: Blockdaemon Oracle API
  slug: blockdaemon-oracle-api
- baseURL: https://svc.blockdaemon.com
  baseurl_source: spec
  description: The organization API from Blockdaemon — 1 operation(s) for organization.
  name: Blockdaemon Organization API
  slug: blockdaemon-organization-api
- baseURL: https://svc.blockdaemon.com
  baseurl_source: spec
  description: The overview API from Blockdaemon — 1 operation(s) for overview.
  name: Blockdaemon Overview API
  slug: blockdaemon-overview-api
- baseURL: https://svc.blockdaemon.com/reporting/staking
  baseurl_source: spec
  description: The Polkadot Staking Reporting API from Blockdaemon — 16 operation(s) for polkadot staking reporting.
  name: Blockdaemon Polkadot Staking Reporting API
  slug: blockdaemon-polkadot-staking-reporting-api
- baseURL: https://svc.blockdaemon.com/boss
  baseurl_source: spec
  description: Polygon endpoints
  name: Blockdaemon Polygon API
  slug: blockdaemon-polygon-api
- baseURL: https://svc.blockdaemon.com/reporting/staking
  baseurl_source: spec
  description: The Polygon Staking Reporting API from Blockdaemon — 5 operation(s) for polygon staking reporting.
  name: Blockdaemon Polygon Staking Reporting API
  slug: blockdaemon-polygon-staking-reporting-api
- baseURL_template: '{server}'
  baseurl_source: spec_template
  description: Application profiling operations
  name: Blockdaemon Profiling API
  slug: blockdaemon-profiling-api
- baseURL_template: https://svc.blockdaemon.com/universal/{version}
  baseurl_source: spec_template
  description: The Protocol and Endpoint Support API from Blockdaemon — 2 operation(s) for protocol and endpoint support.
  name: Blockdaemon Protocol and Endpoint Support API
  slug: blockdaemon-protocol-and-endpoint-support-api
- baseURL: https://svc.blockdaemon.com
  baseurl_source: spec
  description: The rule API from Blockdaemon — 2 operation(s) for rule.
  name: Blockdaemon Rule API
  slug: blockdaemon-rule-api
- baseURL: https://svc.blockdaemon.com
  baseurl_source: spec
  description: The rwa API from Blockdaemon — 10 operation(s) for rwa.
  name: Blockdaemon Rwa API
  slug: blockdaemon-rwa-api
- baseURL: https://svc.blockdaemon.com/tx/v1
  baseurl_source: spec
  description: The Send API from Blockdaemon — 1 operation(s) for send.
  name: Blockdaemon Send API
  slug: blockdaemon-send-api
- baseURL: https://svc.blockdaemon.com/boss
  baseurl_source: spec
  description: Solana endpoints
  name: Blockdaemon Solana API
  slug: blockdaemon-solana-api
- baseURL: https://svc.blockdaemon.com/reporting/staking
  baseurl_source: spec
  description: The Solana Staking Reporting API from Blockdaemon — 8 operation(s) for solana staking reporting.
  name: Blockdaemon Solana Staking Reporting API
  slug: blockdaemon-solana-staking-reporting-api
- baseURL: https://svc.blockdaemon.com
  baseurl_source: spec
  description: The stablecoin API from Blockdaemon — 1 operation(s) for stablecoin.
  name: Blockdaemon Stablecoin API
  slug: blockdaemon-stablecoin-api
- baseURL: https://svc.blockdaemon.com
  baseurl_source: spec
  description: API endpoints for supported chains or protocols
  name: Blockdaemon Support API
  slug: blockdaemon-support-api
- baseURL: https://svc.blockdaemon.com
  baseurl_source: spec
  description: The synthetic API from Blockdaemon — 3 operation(s) for synthetic.
  name: Blockdaemon Synthetic API
  slug: blockdaemon-synthetic-api
- baseURL: https://svc.blockdaemon.com
  baseurl_source: spec
  description: The target API from Blockdaemon — 5 operation(s) for target.
  name: Blockdaemon Target API
  slug: blockdaemon-target-api
- baseURL: https://svc.blockdaemon.com/sia
  baseurl_source: spec
  description: The TON API from Blockdaemon — 1 operation(s) for ton.
  name: Blockdaemon TON API
  slug: blockdaemon-ton-api
- baseURL: https://svc.blockdaemon.com/tx/v1
  baseurl_source: spec
  description: The Transaction API API from Blockdaemon — 1 operation(s) for transaction api.
  name: Blockdaemon Transaction API
  slug: blockdaemon-transaction-api-api
- baseURL_template: https://svc.blockdaemon.com/universal/{version}
  baseurl_source: spec_template
  description: The Transactions API from Blockdaemon — 3 operation(s) for transactions.
  name: Blockdaemon Transactions API
  slug: blockdaemon-transactions-api
- baseURL: https://svc.blockdaemon.com
  baseurl_source: spec
  description: The variable API from Blockdaemon — 2 operation(s) for variable.
  name: Blockdaemon Variable API
  slug: blockdaemon-variable-api
- baseURL: https://svc.blockdaemon.com
  baseurl_source: spec
  description: The variable_values API from Blockdaemon — 2 operation(s) for variable_values.
  name: Blockdaemon Variable Values API
  slug: blockdaemon-variable-values-api
- baseURL: https://svc.blockdaemon.com/tx/v1
  baseurl_source: spec
  description: The Verify API from Blockdaemon — 1 operation(s) for verify.
  name: Blockdaemon Verify API
  slug: blockdaemon-verify-api
- baseURL: https://svc.blockdaemon.com/streaming/v2
  baseurl_source: spec
  description: The webhook API from Blockdaemon — 1 operation(s) for webhook.
  name: Blockdaemon Webhook API
  slug: blockdaemon-webhook-api
- baseURL: https://svc.blockdaemon.com
  baseurl_source: spec
  description: The weth API from Blockdaemon — 2 operation(s) for weth.
  name: Blockdaemon Weth API
  slug: blockdaemon-weth-api
- baseURL: https://svc.blockdaemon.com
  baseurl_source: spec
  description: The yieldaggregator API from Blockdaemon — 15 operation(s) for yieldaggregator.
  name: Blockdaemon Yieldaggregator API
  slug: blockdaemon-yieldaggregator-api
artifact_total: 167
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/blockdaemon/refs/heads/main/capabilities/blockdaemon-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/blockdaemon-capability-edges.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/blockdaemon/refs/heads/main/agentic-access/blockdaemon-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/blockdaemon-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/blockdaemon/refs/heads/main/rules/blockdaemon-rules.yml
  title: ''
  type: Spectral
  url: rules/blockdaemon-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/blockdaemon/refs/heads/main/rules/blockdaemon-jsonschema-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/blockdaemon-jsonschema-spectral-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/blockdaemon/refs/heads/main/data-model/blockdaemon-data-model.yml
  title: ''
  type: DataModel
  url: data-model/blockdaemon-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/blockdaemon/refs/heads/main/conventions/blockdaemon-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/blockdaemon-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/blockdaemon/refs/heads/main/conventions/blockdaemon-conventions.yml
  title: ''
  type: Conventions
  url: conventions/blockdaemon-conventions.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.blockdaemon.com/security
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/blockdaemon/refs/heads/main/errors/blockdaemon-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/blockdaemon-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/blockdaemon/refs/heads/main/conformance/blockdaemon-conformance.yml
  title: ''
  type: Conformance
  url: conformance/blockdaemon-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/blockdaemon/refs/heads/main/llms/blockdaemon-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/blockdaemon-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/blockdaemon/refs/heads/main/well-known/blockdaemon-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/blockdaemon-status-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/blockdaemon/refs/heads/main/well-known/blockdaemon-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/blockdaemon-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/blockdaemon/refs/heads/main/hosts/blockdaemon-hosts.yml
  title: ''
  type: Hosts
  url: hosts/blockdaemon-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/blockdaemon/refs/heads/main/vendors/blockdaemon-vendors.yml
  title: ''
  type: Vendors
  url: vendors/blockdaemon-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.blockdaemon.com/press
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/blockdaemon/refs/heads/main/authentication/blockdaemon-authentication.yml
  title: ''
  type: Authentication
  url: authentication/blockdaemon-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.blockdaemon.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/blockdaemon/refs/heads/main/security/blockdaemon-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/blockdaemon-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/blockdaemon/refs/heads/main/security/blockdaemon-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/blockdaemon-domain-security.yml
- group: start
  title: ''
  type: Portal
  url: https://www.blockdaemon.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.blockdaemon.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.blockdaemon.com/docs/homepage-guides
- group: start
  title: ''
  type: Portal
  url: https://docs.blockdaemon.com/reference/blockdaemon-api-suite
- group: docs
  title: ''
  type: Documentation
  url: https://docs.blockdaemon.com/docs/apisuite-overview
- group: docs
  title: ''
  type: Documentation
  url: https://docs.blockdaemon.com/docs/api-suite-dashboard
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.blockdaemon.com/docs/quick-start-blockdaemon-api-suite
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.blockdaemon.com/docs/send-your-first-api-request
- group: auth
  title: ''
  type: Authentication
  url: https://docs.blockdaemon.com/docs/authentication
- group: design
  title: ''
  type: ErrorCodes
  url: https://docs.blockdaemon.com/docs/error-handling
- group: operate
  title: ''
  type: RateLimits
  url: https://docs.blockdaemon.com/docs/rate-limits
- group: docs
  title: ''
  type: Documentation
  url: https://docs.blockdaemon.com/docs/compute-units
- group: docs
  title: ''
  type: Documentation
  url: https://docs.blockdaemon.com/docs/pagination
- group: docs
  title: ''
  type: Documentation
  url: https://docs.blockdaemon.com/docs/historical-data
- group: docs
  title: ''
  type: Documentation
  url: https://docs.blockdaemon.com/docs/supported-chains
- group: docs
  title: ''
  type: Documentation
  url: https://docs.blockdaemon.com/docs/business-verification-kyb
- group: docs
  title: ''
  type: Documentation
  url: https://docs.blockdaemon.com/docs/subscription-management
- group: docs
  title: ''
  type: Documentation
  url: https://docs.blockdaemon.com/docs/mcp
- group: docs
  title: ''
  type: Documentation
  url: https://docs.blockdaemon.com/llms.txt
- group: docs
  title: ''
  type: Documentation
  url: https://docs.blockdaemon.com/docs/blockchain-nodes
- group: docs
  title: ''
  type: Documentation
  url: https://docs.blockdaemon.com/docs/custom-solutions
- group: docs
  title: ''
  type: Documentation
  url: https://docs.blockdaemon.com/docs/earn-overview
- group: docs
  title: ''
  type: Documentation
  url: https://docs.blockdaemon.com/docs/widget
- group: docs
  title: ''
  type: Documentation
  url: https://docs.blockdaemon.com/docs/widget-embed-guide
- group: docs
  title: ''
  type: Documentation
  url: https://docs.blockdaemon.com/docs/canton-overview
- group: docs
  title: ''
  type: Documentation
  url: https://docs.blockdaemon.com/docs/tempo
- group: docs
  title: ''
  type: Documentation
  url: https://docs.blockdaemon.com/docs/layerzero-overview
- group: operate
  title: ''
  type: StatusPage
  url: https://status.blockdaemon.com/
- group: operate
  title: ''
  type: Support
  url: https://www.blockdaemon.com/support
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.blockdaemon.com/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.blockdaemon.com/legal/privacy-policy
- group: company
  title: ''
  type: Blog
  url: https://www.blockdaemon.com/blog
- group: company
  title: ''
  type: Blog
  url: https://www.blockdaemon.com/press
- group: company
  title: ''
  type: AboutUs
  url: https://www.blockdaemon.com/about
- group: company
  title: ''
  type: Careers
  url: https://www.blockdaemon.com/careers
- group: operate
  title: ''
  type: Contact
  url: https://www.blockdaemon.com/contact
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/blockdaemon
- group: other
  title: ''
  type: X
  url: https://twitter.com/Blockdaemon
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Blockdaemon
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Blockdaemon/buildervault-web3-provider
- group: build
  title: ''
  type: Tools
  url: https://github.com/Blockdaemon/builder-vault-helm
- group: docs
  title: ''
  type: ReferenceImplementation
  url: https://github.com/Blockdaemon/automated-approver-service
- group: build
  title: ''
  type: Tools
  url: https://github.com/Blockdaemon/chain_sink
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/Blockdaemon/demo-event-streaming
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/Blockdaemon/demo-stakingAPI
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/Blockdaemon/demo-buildervault-token-deployment
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/Blockdaemon/demo-buildervault-wallettransact
- group: build
  title: ''
  type: Tools
  url: https://github.com/Blockdaemon/solana-accountsdb-plugin-kafka
- group: build
  title: ''
  type: Tools
  url: https://github.com/Blockdaemon/solana-cluster
- group: build
  title: ''
  type: Tools
  url: https://github.com/Blockdaemon/agave-snapshot-gossip-client
- group: build
  title: ''
  type: Tools
  url: https://github.com/Blockdaemon/agave-snapshot-uploader
- group: build
  title: ''
  type: Tools
  url: https://github.com/Blockdaemon/pyth-exporter
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Blockdaemon/pyth-go
- group: build
  title: ''
  type: Tools
  url: https://github.com/Blockdaemon/EVM-trackooor
- group: build
  title: ''
  type: Tools
  url: https://github.com/Blockdaemon/validator-ownership-verification
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/Blockdaemon/prototype-eip7702-gas-sponsorship
- group: other
  title: ''
  type: BrandAssets
  url: https://github.com/Blockdaemon/media-kit
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/blockdaemon/refs/heads/main/plans/blockdaemon-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/blockdaemon-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/blockdaemon/refs/heads/main/rate-limits/blockdaemon-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/blockdaemon-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/blockdaemon/refs/heads/main/finops/blockdaemon-finops.yml
  title: ''
  type: FinOps
  url: finops/blockdaemon-finops.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/blockdaemon/refs/heads/main/json-ld/blockdaemon-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/blockdaemon-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/blockdaemon/refs/heads/main/vocabulary/blockdaemon-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/blockdaemon-vocabulary.yml
created: '2026-05-25T00:00:00.000Z'
description: Blockdaemon is an institutional blockchain infrastructure company founded in 2017 by Konstantin Richter. It runs production node infrastructure, staking, indexed data, DeFi, custody, and tokenization services across 80+ blockchain protocols for 400+ institutional clients including Goldman Sachs, Microsoft, JP Morgan, and Citi Ventures. The Blockdaemon API Suite bundles a unified Data API (Ubiquity), JSON-RPC nodes, a Staking API, Staking Reporting API, DeFi aggregator (expand.network), Token Pricing API, Chain Watch event streaming, and a Management API. Wallet products include Builder Vault TSM (MPC for builders), Institutional Vault (self-hosted MPC custody with Automated Approver Service), and Wallet Transact. Earn Stack covers a no-code embeddable Earn Widget plus liquid staking and restaking. Compute Unit metering, triple-mode authentication, an MCP server, and SOC 2 Type II / ISO 27001 certifications round out the platform. $110B+ in digital assets secured and $10B+ staked
  on Blockdaemon validators.
examples:
- key_count: 3
  name: Blockdaemon Chainwatch Event Example
  slug: blockdaemon-chainwatch-event-example
- key_count: 2
  name: Blockdaemon Getbalances Example
  slug: blockdaemon-getbalances-example
- key_count: 2
  name: Blockdaemon Staking Intent Example
  slug: blockdaemon-staking-intent-example
features:
- Unified Data API (Ubiquity) across 50+ blockchains with consistent block, transaction, balance, UTXO, and fee endpoints
- Shared and Dedicated JSON-RPC + WebSocket nodes for Bitcoin, Ethereum, Solana, Polygon, Arbitrum, Avalanche, Base, Optimism, Cosmos, Polkadot, NEAR, Cardano, Stellar, XRP, Tron, Monad, Hyperliquid, and more
- Institutional Staking API across Ethereum, Solana, Cosmos, Polkadot, Polygon, NEAR, Cardano, Avalanche, Binance
- Staking Reporting API for unified rewards, validator status, and financial summaries
- DeFi API (expand.network) with DEX, bridge, and lending aggregation across 200+ protocols
- Token Pricing & Metadata API (Beta) with tag-based filtering
- Chain Watch event streaming with webhooks, Kafka, and WebSocket targets
- Management API with current-period Compute Unit and request metrics plus audit logs
- Builder Vault TSM — MPC wallet platform with EVM Web3 provider, Helm chart, and ERC-token demos
- Institutional Vault — self-hosted MPC vault with Automated Approver Service for policy-driven signing
- Wallet Transact toolbox for scaling multi-chain wallet operations
- Earn Widget — no-code embeddable staking and DeFi UI across Ethereum, Solana, and more
- LayerZero DVN — Animoca-Blockdaemon DVN for cross-chain messaging
- Canton Network super validators, validators, and Canton Wallet Gateway for institutional tokenization
- Tempo Network validators, TIP-20 issuance, TIP-403 compliance, stablecoin gas support
- Solana Snapshot Delivery Network (SSDN) gossip client, uploader, and AccountsDB Kafka plugin
- Pyth Network publisher tooling — Prometheus exporter and Go client
- EIP-5792 and EIP-7702 transaction batching support in the DeFi API
- Compute Unit metering with XS/S/M/L/XL/Egress/Batch tiers
- Triple-mode authentication: Bearer, X-API-Key header, or apiKey query parameter
- MCP server at docs.blockdaemon.com/mcp for AI agent access to docs and APIs
- Status page at status.blockdaemon.com with per-component health
- SOC 2 Type II (June 2025) and ISO 27001 (July 2022) certifications; OFAC compliant
- 70+ points of presence globally; offices in San Francisco, Galway, London, Singapore, Newcastle, NYC, Abu Dhabi
- 400+ institutional customers including Goldman Sachs, Microsoft, JP Morgan, Citi Ventures
- $110B+ digital assets secured; $10B+ staked on Blockdaemon validators; 250K+ nodes launched; 80+ protocols
finops:
- has_sources: true
  method: generated
  name: Blockdaemon Finops
  primary_unit: compute_unit
  service_category: Blockchain Infrastructure
  slug: blockdaemon-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/blockdaemon.png
json_schemas:
- name: ApiKeyCreateRequest
  property_count: 2
  slug: blockdaemon-api-key-create-request
- name: ApiKeyCreateResponse
  property_count: 2
  slug: blockdaemon-api-key-create-response
- name: ApiKeyListResponse
  property_count: 1
  slug: blockdaemon-api-key-list-response
- name: ApiTxCompileRequest
  property_count: 0
  slug: blockdaemon-api-tx-compile-request
- name: ApiTxCreateRequest
  property_count: 0
  slug: blockdaemon-api-tx-create-request
- name: ApiTxCreateResponse
  property_count: 0
  slug: blockdaemon-api-tx-create-response
- name: ApiTxDecodeRequest
  property_count: 1
  slug: blockdaemon-api-tx-decode-request
- name: ApiTxDecodeResponse
  property_count: 0
  slug: blockdaemon-api-tx-decode-response
- name: ApiTxSigned
  property_count: 1
  slug: blockdaemon-api-tx-signed
- name: AuthenticatorInfo
  property_count: 0
  slug: blockdaemon-authenticator-info
- name: Blockdaemon Account Balance
  property_count: 5
  slug: blockdaemon-balance
- name: block_identifier
  property_count: 5
  slug: blockdaemon-block-identifier
- name: block
  property_count: 6
  slug: blockdaemon-block
- name: _bridge_swap_Request
  property_count: 20
  slug: blockdaemon-bridge-swap-request
- name: Chains
  property_count: 1
  slug: blockdaemon-chains
- name: DeactivationIntents
  property_count: 9
  slug: blockdaemon-deactivation-intents
- name: _dex_addliquidity_Request
  property_count: 24
  slug: blockdaemon-dex-addliquidity-request
- name: _dex_removeliquidity_Request
  property_count: 30
  slug: blockdaemon-dex-removeliquidity-request
- name: _dex_swap_Request
  property_count: 15
  slug: blockdaemon-dex-swap-request
- name: _dex_swapaggregator_Request
  property_count: 19
  slug: blockdaemon-dex-swapaggregator-request
- name: _dex_swapwithapproval_Request
  property_count: 15
  slug: blockdaemon-dex-swapwithapproval-request
- name: EthereumTopUpIntent
  property_count: 7
  slug: blockdaemon-ethereum-top-up-intent
- name: Blockdaemon Chain Watch Unified Event
  property_count: 12
  slug: blockdaemon-event
- name: HealthInformation
  property_count: 1
  slug: blockdaemon-health-information
- name: NewRule
  property_count: 12
  slug: blockdaemon-new-rule
- name: NewStakeIntentAvalanche
  property_count: 6
  slug: blockdaemon-new-stake-intent-avalanche
- name: NewStakeIntentNear
  property_count: 5
  slug: blockdaemon-new-stake-intent-near
- name: NewStakeIntentSolana
  property_count: 6
  slug: blockdaemon-new-stake-intent-solana
- name: NewTarget
  property_count: 6
  slug: blockdaemon-new-target
- name: PatchTarget
  property_count: 6
  slug: blockdaemon-patch-target
- name: QuotesRequestBody
  property_count: 2
  slug: blockdaemon-quotes-request-body
- name: Quotes
  property_count: 1
  slug: blockdaemon-quotes
- name: report
  property_count: 5
  slug: blockdaemon-report
- name: Reward
  property_count: 8
  slug: blockdaemon-reward
- name: RewardsFormat1
  property_count: 8
  slug: blockdaemon-rewards-format1
- name: Rule
  property_count: 15
  slug: blockdaemon-rule
- name: solanaDeactivateTransactionResponse
  property_count: 7
  slug: blockdaemon-solana-deactivate-transaction-response
- name: solanaSplitTransactionResponse
  property_count: 8
  slug: blockdaemon-solana-split-transaction-response
- name: solanaStakeTransactionRequest
  property_count: 4
  slug: blockdaemon-solana-stake-transaction-request
- name: solanaStakeTransactionResponse
  property_count: 7
  slug: blockdaemon-solana-stake-transaction-response
- name: solanaWithdrawTransactionRequest
  property_count: 4
  slug: blockdaemon-solana-withdraw-transaction-request
- name: solanaWithdrawTransactionResponse
  property_count: 7
  slug: blockdaemon-solana-withdraw-transaction-response
- name: Target
  property_count: 10
  slug: blockdaemon-target
- name: Tokens
  property_count: 1
  slug: blockdaemon-tokens
- name: tx_output
  property_count: 5
  slug: blockdaemon-tx-output
- name: tx_outputs
  property_count: 3
  slug: blockdaemon-tx-outputs
- name: tx
  property_count: 11
  slug: blockdaemon-tx
- name: ValidatorRewardsFormat1
  property_count: 8
  slug: blockdaemon-validator-rewards-format1
- name: Blockdaemon Validator
  property_count: 13
  slug: blockdaemon-validator
- name: Variable
  property_count: 6
  slug: blockdaemon-variable
- name: WebhookSendRequest
  property_count: 0
  slug: blockdaemon-webhook-send-request
- name: WebhookVerificationResponse
  property_count: 1
  slug: blockdaemon-webhook-verification-response
- name: WithdrawalIntentNear
  property_count: 8
  slug: blockdaemon-withdrawal-intent-near
- name: YieldResponseCosmos
  property_count: 10
  slug: blockdaemon-yield-response-cosmos
- name: YieldResponse
  property_count: 10
  slug: blockdaemon-yield-response
- name: YieldResponseSolana
  property_count: 10
  slug: blockdaemon-yield-response-solana
jsonld:
- class_count: 54
  name: Blockdaemon Context
  property_count: 0
  slug: blockdaemon-context
layout: provider
modified: '2026-05-25'
name: Blockdaemon
nav: Providers
network: true
overview: 'Blockdaemon publishes 72 API contracts indexed on the [APIs.io](https://apis.io/) network, including Management API, Pricing API, Aa API, and 69 more. Tagged areas include Blockchain, Web3, Staking, Validator, and Custody.


  The Blockdaemon catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Blockdaemon''s developer surface includes authentication, developer portal, documentation, getting-started guide, support, engineering blog, tooling, and 75 more developer resources.'
plans:
- name: Blockdaemon Plans Pricing
  plan_count: 4
  slug: blockdaemon-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 6
  name: Blockdaemon Rate Limits
  slug: blockdaemon-rate-limits
rules:
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: Blockdaemon — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: blockdaemon-jsonschema-spectral-rules
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: Blockdaemon API Rules
  rule_count: 14
  severity_counts:
    error: 6
    hint: 0
    info: 1
    warn: 7
  slug: blockdaemon-rules
score:
  band: developing
  composite: 53.7
  coverage:
    artifact_dirs: 26
    catalog_earned: 70.0
    catalog_earned_first_party: 0.0
    catalog_gap: 45.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 8.9
  facets:
    access_clarity: 52.6
    contract_governance: 31.8
    contract_quality: 68.2
    developer_ergonomics: 52.4
    discoverability: 71.4
    operational_transparency: 32.9
  previous_composite: 44.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 61
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 26.8
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: rising
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/blockdaemon/refs/heads/main/screenshots/blockdaemon-2026-06-20T173357.png
security:
- kind: authentication
  name: Blockdaemon Authentication
  slug: blockdaemon-authentication
  summary_line: apiKey/http · 4 schemes
- kind: domain-security
  name: Blockdaemon Domain Security
  slug: blockdaemon-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Blockdaemon Trust Center
  slug: blockdaemon-trust-center
  summary_line: SOC 2, ISO 27001
slug: blockdaemon
tags:
- Blockchain
- Web3
- Staking
- Validator
- Custody
- MPC
- Wallets
- Node
- RPC
- DeFi
- Indexer
- Tokenization
- Institutional
- Cryptocurrency
- Ethereum
website: https://www.blockdaemon.com/
---
