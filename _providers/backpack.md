---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 39.2
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 21
  human_in_the_loop: 0
  name: Backpack Agentic Access
  operation_count: 81
  slug: backpack-agentic-access
  summary_line: 81 operations · 21 acting
api_count: 15
apis:
- description: Backpack Wallet is a self-custodial multichain wallet for Solana, Ethereum, and Bitcoin, originally built around the xNFT (executable NFT) protocol that lets dApps run as plugins inside the wallet. Av
  name: Backpack Wallet
  slug: backpack-wallet
- description: Account settings and limits.
  name: Backpack Account API
  slug: backpack-account-api
- description: Assets and collateral data.
  name: Backpack Assets API
  slug: backpack-assets-api
- description: Borrowing and lending.
  name: Backpack Borrow Lend API
  slug: backpack-borrow-lend-api
- description: Borrowing and lending.
  name: Backpack Borrow Lend Markets API
  slug: backpack-borrow-lend-markets-api
- description: Capital management.
  name: Backpack Capital API
  slug: backpack-capital-api
- description: Public market data.
  name: Backpack Markets API
  slug: backpack-markets-api
- description: Order management.
  name: Backpack Order API
  slug: backpack-order-api
- description: Positions and futures data.
  name: Backpack Position API
  slug: backpack-position-api
- description: RFQ (Request For Quote) - Maker.
  name: Backpack RFQ API
  slug: backpack-rfq-api
- description: Strategies.
  name: Backpack Strategy API
  slug: backpack-strategy-api
- description: Exchange system status.
  name: Backpack System API
  slug: backpack-system-api
- description: Public trade data.
  name: Backpack Trades API
  slug: backpack-trades-api
- description: Vault data.
  name: Backpack Vaults API
  slug: backpack-vaults-api
- description: Withdrawal delays.
  name: Backpack Withdrawal Delays API
  slug: backpack-withdrawal-delays-api
arazzos:
- description: Confirm available balance, read the ticker, then place a market buy and verify the fill.
  name: Backpack Balance-Checked Market Buy
  slug: backpack-balance-checked-market-buy-workflow
- description: Confirm available balance, request a withdrawal, then reconcile it against withdrawal history.
  name: Backpack Balance-Checked Withdrawal
  slug: backpack-balance-checked-withdrawal-workflow
- description: Look up a resting order, cancel it, and place a replacement at a new price.
  name: Backpack Cancel and Replace an Order
  slug: backpack-cancel-replace-order-workflow
- description: Fetch a blockchain deposit address, then read deposit history to reconcile incoming funds.
  name: Backpack Get Deposit Address and Reconcile History
  slug: backpack-deposit-address-and-history-workflow
- description: List open orders on a market, cancel them all, and confirm none remain.
  name: Backpack Flatten Open Orders on a Market
  slug: backpack-flatten-market-orders-workflow
- description: Discover markets, pull all tickers, and read recent trades for a chosen symbol.
  name: Backpack Market and Trade Analytics
  slug: backpack-market-trade-analytics-workflow
- description: Price a market from the ticker and order book, then place and confirm a limit order.
  name: Backpack Place a Limit Order
  slug: backpack-place-limit-order-workflow
- description: Read an open futures position and the mark price, then place a reduce-only take-profit order.
  name: Backpack Add a Take-Profit to a Position
  slug: backpack-position-take-profit-workflow
artifact_total: 96
asyncapis:
- description: Real-time market data and account event streams for Backpack Exchange. Clients connect to a single WebSocket endpoint and manage many streams over that connection by sending `SUBSCRIBE` / `UNSUBSCRIBE
  name: Backpack Exchange WebSocket Streams API
  slug: backpack-asyncapi
collections:
- collection_type: postman
  name: Backpack Exchange API
  slug: postman-backpack-exchange
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Backpack Exchange Account API
  slug: open-backpack-account-api
- collection_type: open
  name: Backpack Exchange Account Assets API
  slug: open-backpack-assets-api
- collection_type: open
  name: Backpack Exchange Account Borrow Lend API
  slug: open-backpack-borrow-lend-api
- collection_type: open
  name: Backpack Exchange Account Borrow Lend Markets API
  slug: open-backpack-borrow-lend-markets-api
- collection_type: open
  name: Backpack Exchange Account Capital API
  slug: open-backpack-capital-api
- collection_type: open
  name: Backpack Exchange API
  slug: open-backpack-exchange
- collection_type: open
  name: Backpack Exchange Account Markets API
  slug: open-backpack-markets-api
- collection_type: open
  name: Backpack Exchange Account Order API
  slug: open-backpack-order-api
- collection_type: open
  name: Backpack Exchange Account Position API
  slug: open-backpack-position-api
- collection_type: open
  name: Backpack Exchange Account RFQ API
  slug: open-backpack-rfq-api
- collection_type: open
  name: Backpack Exchange Account Strategy API
  slug: open-backpack-strategy-api
- collection_type: open
  name: Backpack Exchange Account System API
  slug: open-backpack-system-api
- collection_type: open
  name: Backpack Exchange Account Trades API
  slug: open-backpack-trades-api
- collection_type: open
  name: Backpack Exchange Account Vaults API
  slug: open-backpack-vaults-api
- collection_type: open
  name: Backpack Exchange Account Withdrawal Delays API
  slug: open-backpack-withdrawal-delays-api
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/coral-xyz/backpack/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/coral-xyz/backpack/releases
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/coral-xyz/backpack/blob/master/SECURITY.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/coral-xyz/backpack/blob/master/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/backpack-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/backpack-domain-security.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/backpack/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/backpack-balance-checked-market-buy-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/backpack-balance-checked-withdrawal-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/backpack-cancel-replace-order-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/backpack-deposit-address-and-history-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/backpack-flatten-market-orders-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/backpack-market-trade-analytics-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/backpack-place-limit-order-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/backpack-position-take-profit-workflow.yml
- group: start
  title: ''
  type: Portal
  url: https://backpack.app/
- group: start
  title: ''
  type: Portal
  url: https://backpack.exchange/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.backpack.exchange/
- group: start
  title: ''
  type: Signup
  url: https://backpack.exchange/join
- group: start
  title: ''
  type: Signup
  url: https://backpack.exchange/refer
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/coral-xyz
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/coral-xyz/backpack
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/coral-xyz/anchor
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/coral-xyz/xnft
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/coral-xyz/multisig
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/coral-xyz/sealevel-attacks
- group: operate
  title: ''
  type: StatusPage
  url: https://status.backpack.exchange/
- group: company
  title: ''
  type: Blog
  url: https://backpack.exchange/blog
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/Backpack
- group: operate
  title: ''
  type: Forums
  url: https://discord.gg/backpack
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/backpack-exchange
- group: operate
  title: ''
  type: Support
  url: https://support.backpack.exchange/
- group: operate
  title: ''
  type: FAQ
  url: https://support.backpack.exchange/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://backpack.exchange/refer/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://backpack.exchange/privacy
- group: auth
  title: ''
  type: Authentication
  url: https://docs.backpack.exchange/#section/Authentication
- group: design
  title: ''
  type: SpectralRules
  url: rules/backpack-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/backpack-vocabulary.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/backpack-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/backpack-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/backpack-finops.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.backpack.exchange/#section/Changelog
- group: start
  title: ''
  type: Signup
  url: https://backpack.exchange/refer/api
created: '2026-05-24'
description: 'Backpack is a Solana-first crypto company founded by Armani Ferrante and Tristan Yver — the same team behind Coral and the Anchor framework that powers a majority of Solana programs. It operates two flagship products: Backpack Wallet, an open-source self-custodial multichain wallet (Solana, Ethereum, Bitcoin) with an xNFT plugin runtime, available as a Chrome/Brave extension and iOS/Android app; and Backpack Exchange, a fully fledged centralized exchange offering spot, perpetual futures, dated futures, prediction markets, borrow/lend, RFQ, strategies, vaults, and securities, with a comprehensive ED25519-signed REST + WebSocket API documented at docs.backpack.exchange. Backpack Exchange acquired and processes FTX EU claims and is one of the more technically transparent venues to emerge post-FTX.'
examples:
- key_count: 2
  name: Backpack Depth Example
  slug: backpack-depth-example
- key_count: 2
  name: Backpack Markets List Example
  slug: backpack-markets-list-example
- key_count: 2
  name: Backpack Order Execute Example
  slug: backpack-order-execute-example
features:
- All-in-one crypto app — spot, perpetual futures, dated futures, prediction markets, borrow/lend, RFQ, strategies, vaults
- Unified cross-margin — spot balances, perps margin, and lending balances live in one collateral pool
- ED25519 signed-request authentication with per-operation instruction binding and X-Window replay protection
- Public + authenticated WebSocket streams for market data, order updates, position updates, and RFQ
- Sub-accounts with aggregated VIP tier / fee tier across the main account
- Volume-based maker/taker fee tiers recalculated hourly, USDT/USDC pair at 0% fees
- Borrow/lend with auto-lend and manual modes, APY history endpoints, and liquidation-price simulation
- RFQ workflow with millisecond market-maker quotes and 2-minute acceptance windows
- Strategies API (grid bots and other programmatic strategies) with full lifecycle endpoints
- Configurable withdrawal delay policy (create/update/get) for account-level security
- Dust conversion endpoint for sweeping small balances
- Proof of Reserves publishing
- Multichain self-custodial wallet (Solana, Ethereum, Bitcoin) with xNFT plugin runtime
- Mobile apps (iOS, Android) and Chrome/Brave extension sharing exchange session
- Stocks and securities trading surface (regional)
- Prediction markets with tagged event discovery
- Vault tokens with mint/redeem flow and pending redemption queue
- Open source wallet under GPL-3.0 at github.com/coral-xyz/backpack
- Founded by Armani Ferrante (creator of the Anchor framework) and Tristan Yver via Coral
finops:
- name: Backpack Finops
  service_category: ''
  slug: backpack-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/backpack.png
integrations:
- description: Native settlement chain for the wallet and the home of the Anchor framework and xNFT protocol.
  name: Solana
- description: Supported in the multichain wallet for EVM signing and asset management.
  name: Ethereum
- description: Supported in the multichain wallet for BTC custody and transfers.
  name: Bitcoin
- description: Charting integration exposed via the TradingView tag in the API for klines and ticker data.
  name: TradingView
- description: US fiat onramp identity verification used during KYC and bank-link flows.
  name: Plaid
- description: Third-party crypto onramp partner integrated into the deposit flow.
  name: Banxa
- description: EUR onramp partners surfaced as dedicated API tag groups in the exchange spec.
  name: Easy Euro / Equals Money
- description: Travel Rule compliance partner for cross-VASP withdrawal information sharing.
  name: Sygna Bridge
- description: Same founding team (Armani Ferrante) — Backpack ships on top of Anchor-based Solana programs.
  name: Coral / Anchor
json_schemas:
- name: Backpack Balance
  property_count: 3
  slug: backpack-balance
- name: Backpack Market
  property_count: 15
  slug: backpack-market
- name: Backpack Order
  property_count: 29
  slug: backpack-order
- name: Backpack Position
  property_count: 20
  slug: backpack-position
- name: Backpack Trade
  property_count: 6
  slug: backpack-trade
jsonld:
- class_count: 8
  name: Backpack Context
  property_count: 25
  slug: backpack-context
layout: provider
modified: '2026-05-24'
name: Backpack
nav: Providers
network: true
overview: 'Backpack publishes 14 APIs on the [APIs.io](https://apis.io/) network, including Account API, Assets API, Borrow Lend API, and 11 more. Tagged areas include Crypto, Exchange, Wallets, Trading, and Perpetuals.


  The Backpack catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 3 Spectral governance rulesets.


  Backpack''s developer surface includes developer portal, documentation, signup flow, engineering blog, support, FAQ, authentication, and 36 more developer resources.'
plans:
- name: Backpack Plans Pricing
  plan_count: 5
  slug: backpack-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 3
  name: Backpack Rate Limits
  slug: backpack-rate-limits
rules:
- effective_rule_count: 35
  extends:
  - spectral:asyncapi
  name: Backpack API Rules
  rule_count: 8
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 6
  slug: backpack-asyncapi-spectral-rules
- effective_rule_count: 6
  extends: []
  name: Backpack API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: backpack-jsonschema-spectral-rules
- effective_rule_count: 47
  extends:
  - spectral:oas
  name: Backpack API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 3
    warn: 3
  slug: backpack-rules
score:
  band: strong
  composite: 57.5
  delta: 0.0
  facets:
    access_clarity: 63.2
    commercial_clarity: 63.2
    contract_governance: 28.8
    contract_quality: 75.8
    developer_ergonomics: 40.5
    discoverability: 64.8
    governance: 28.8
    operational_transparency: 60.5
  previous_composite: 57.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 14
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 32.8
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/backpack/refs/heads/main/screenshots/backpack-2026-06-20T172915.png
security:
- kind: domain-security
  name: Backpack Domain Security
  slug: backpack-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: backpack
solutions:
- description: Centralized crypto exchange with spot, perpetuals, lending, RFQ, strategies, and prediction markets — accessible via the REST + WebSocket API.
  name: Backpack Exchange
- description: Self-custody multichain wallet with xNFT runtime, available as Chrome/Brave extension and iOS/Android apps.
  name: Backpack Wallet
- description: Regulated European entity surfaced via European Private Beta and FTX EU Claims tags.
  name: Backpack EU
- description: Dedicated tag group for processing FTX creditor and FTX EU claims through the exchange.
  name: FTX Creditor Claims processing
tags:
- Crypto
- Exchange
- Wallets
- Trading
- Perpetuals
- Solana
- Web3
- DeFi
- xNFT
- Anchor
- Coral
- Centralized Exchange
- Self-Custody
use_cases:
- description: Build trading bots and execution algorithms against the Backpack Exchange order book using ED25519 signed requests and the orderExecute instruction set.
  name: Programmatic spot and perps trading
- description: Subscribe to WebSocket streams (ticker, depth, trades, klines, mark price, open interest, liquidation) for low-latency market state in research pipelines and dashboards.
  name: Real-time market data ingestion
- description: Respond to RFQs with quotes via /api/v1/rfq/quote and stream account.rfqUpdate events to compete on size-aware fills.
  name: Market making and RFQ liquidity provisioning
- description: Use the Borrow Lend endpoints to automate APY hunting across markets, manage liquidation price thresholds, and reconcile interest history.
  name: Lending and borrowing automation
- description: Pull fill, order, funding, settlement, deposit, and withdrawal history from /wapi/v1/history/* to build internal P&L and tax reporting.
  name: Portfolio reconciliation and TaxOps
- description: Embed or extend the open-source Backpack wallet for Solana / Ethereum / Bitcoin signing flows, or ship dApps as xNFTs inside the wallet runtime.
  name: Multichain wallet integration
website: https://backpack.app/
---
