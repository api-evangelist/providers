---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.0
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 160
  human_in_the_loop: 3
  name: Fireblocks Agentic Access
  operation_count: 303
  slug: fireblocks-agentic-access
  summary_line: 303 operations · 160 acting · 3 human-in-the-loop
api_count: 35
apis:
- description: Create and manage vault accounts, asset wallets, deposit addresses, attached tags, and balance inquiries. Vaults are the root container for MPC-secured keys, balances, and transactions inside a Firebl
  name: Fireblocks Vaults API
  slug: fireblocks-vaults-api
- description: Create, cancel, drop, and query digital-asset transactions across all supported chains. Every transaction passes the workspace Policy Engine, is signed by the MPC quorum, and is broadcast under Firebl
  name: Fireblocks Transactions API
  slug: fireblocks-transactions-api
- description: Deploy, mint, burn, and manage tokens across the chains supported by Fireblocks Tokenization Engine. Covers ERC-20 fungible tokens, multichain stablecoins, asset tokenization, smart contract managemen
  name: Fireblocks Tokenization API
  slug: fireblocks-tokenization-api
- description: Execute and track staking operations across multiple proof-of-stake chains. Browse staking providers and validators, initiate stake / unstake / withdraw / claim-rewards actions, and query position sta
  name: Fireblocks Staking API
  slug: fireblocks-staking-api
- description: Discover, index, and manage non-fungible tokens held in the workspace's vault accounts. List owned NFTs, fetch token-level metadata, refresh ownership state, and update token-spam classification.
  name: Fireblocks NFTs API
  slug: fireblocks-nfts-api
- description: AML transaction screening, Travel Rule VASP messaging (FATF Recommendation 16), address registry lookups, and the workspace Policy Editor (Beta and V2). Wire third-party screening providers (Chainalys
  name: Fireblocks Compliance and Policy API
  slug: fireblocks-compliance-api
- description: Configure the Fireblocks Gas Station — auto-fuel logic that tops up native-asset balances in vault accounts so ERC-20 / SPL / contract-call transactions don't fail for lack of gas. Per-asset threshold
  name: Fireblocks Gas Station API
  slug: fireblocks-gas-station-api
- description: Receive push notifications when workspace events occur — TRANSACTION_CREATED, TRANSACTION_STATUS_UPDATED, VAULT_ACCOUNT_ADDED, EMBEDDED_WALLET_DEVICE_PAIRED, SMART_TRANSFER events, and more. Each even
  name: Fireblocks Webhooks API
  slug: fireblocks-webhooks-api
- description: The Approval Requests API from fireblocks — 2 operation(s) for approval requests.
  name: fireblocks Approval Requests API
  slug: fireblocks-approval-requests-api
- description: The Blockchains & Assets API from fireblocks — 8 operation(s) for blockchains & assets.
  name: fireblocks Blockchains & Assets API
  slug: fireblocks-blockchains-assets-api
- description: The Connected Accounts (Beta) API from fireblocks — 5 operation(s) for connected accounts (beta).
  name: fireblocks Connected Accounts (Beta) API
  slug: fireblocks-connected-accounts-beta-api
- description: The Contract Interactions API from fireblocks — 4 operation(s) for contract interactions.
  name: fireblocks Contract Interactions API
  slug: fireblocks-contract-interactions-api
- description: The Contract Templates API from fireblocks — 5 operation(s) for contract templates.
  name: fireblocks Contract Templates API
  slug: fireblocks-contract-templates-api
- description: The Cosigners (Beta) API from fireblocks — 5 operation(s) for cosigners (beta).
  name: fireblocks Cosigners (Beta) API
  slug: fireblocks-cosigners-beta-api
- description: The dApp Connections API from fireblocks — 3 operation(s) for dapp connections.
  name: fireblocks dApp Connections API
  slug: fireblocks-dapp-connections-api
- description: The Deployed Contracts API from fireblocks — 5 operation(s) for deployed contracts.
  name: fireblocks Deployed Contracts API
  slug: fireblocks-deployed-contracts-api
- description: The Exchange Accounts API from fireblocks — 7 operation(s) for exchange accounts.
  name: fireblocks Exchange Accounts API
  slug: fireblocks-exchange-accounts-api
- description: The Fiat Accounts API from fireblocks — 4 operation(s) for fiat accounts.
  name: fireblocks Fiat Accounts API
  slug: fireblocks-fiat-accounts-api
- description: The Fireblocks Network API from fireblocks — 11 operation(s) for fireblocks network.
  name: fireblocks Fireblocks Network API
  slug: fireblocks-fireblocks-network-api
- description: The Job Management API from fireblocks — 6 operation(s) for job management.
  name: fireblocks Job Management API
  slug: fireblocks-job-management-api
- description: The Key Link API from fireblocks — 5 operation(s) for key link.
  name: fireblocks Key Link API
  slug: fireblocks-key-link-api
- description: The Keys (Beta) API from fireblocks — 2 operation(s) for keys (beta).
  name: fireblocks Keys (Beta) API
  slug: fireblocks-keys-beta-api
- description: The Off Exchange API from fireblocks — 5 operation(s) for off exchange.
  name: fireblocks Off Exchange API
  slug: fireblocks-off-exchange-api
- description: The Payments - Flows API from fireblocks — 5 operation(s) for payments - flows.
  name: fireblocks Payments - Flows API
  slug: fireblocks-payments-flows-api
- description: The Payments - Payout API from fireblocks — 3 operation(s) for payments - payout.
  name: fireblocks Payments - Payout API
  slug: fireblocks-payments-payout-api
- description: The Policy Editor (Beta) API from fireblocks — 3 operation(s) for policy editor (beta).
  name: fireblocks Policy Editor (Beta) API
  slug: fireblocks-policy-editor-beta-api
- description: The Policy Editor V2 (Beta) API from fireblocks — 2 operation(s) for policy editor v2 (beta).
  name: fireblocks Policy Editor V2 (Beta) API
  slug: fireblocks-policy-editor-v2-beta-api
- description: The Smart Transfers API from fireblocks — 15 operation(s) for smart transfers.
  name: fireblocks Smart Transfers API
  slug: fireblocks-smart-transfers-api
- description: The Tags API from fireblocks — 2 operation(s) for tags.
  name: fireblocks Tags API
  slug: fireblocks-tags-api
- description: The Trading (Beta) API from fireblocks — 4 operation(s) for trading (beta).
  name: fireblocks Trading (Beta) API
  slug: fireblocks-trading-beta-api
- description: The Webhooks V2 API from fireblocks — 9 operation(s) for webhooks v2.
  name: fireblocks Webhooks V2 API
  slug: fireblocks-webhooks-v2-api
- description: The Whitelisted Contracts API from fireblocks — 3 operation(s) for whitelisted contracts.
  name: fireblocks Whitelisted Contracts API
  slug: fireblocks-whitelisted-contracts-api
- description: The Whitelisted External Wallets API from fireblocks — 4 operation(s) for whitelisted external wallets.
  name: fireblocks Whitelisted External Wallets API
  slug: fireblocks-whitelisted-external-wallets-api
- description: The Whitelisted Internal Wallets API from fireblocks — 5 operation(s) for whitelisted internal wallets.
  name: fireblocks Whitelisted Internal Wallets API
  slug: fireblocks-whitelisted-internal-wallets-api
- description: The Workspace Management API from fireblocks — 13 operation(s) for workspace management.
  name: fireblocks Workspace Management API
  slug: fireblocks-workspace-management-api
artifact_total: 127
collections:
- collection_type: postman
  name: Fireblocks Blockchains and Assets Approval Requests API
  slug: postman-fireblocks-approval-requests-api
- collection_type: postman
  name: Fireblocks Blockchains and Assets Approval Requests Blockchains & Assets API
  slug: postman-fireblocks-blockchains-assets-api
- collection_type: postman
  name: Fireblocks Blockchains and Assets Approval Requests Compliance API
  slug: postman-fireblocks-compliance-api
- collection_type: postman
  name: Fireblocks Blockchains and Assets Approval Requests Connected Accounts (Beta) API
  slug: postman-fireblocks-connected-accounts-beta-api
- collection_type: postman
  name: Fireblocks Blockchains and Assets Approval Requests Contract Interactions API
  slug: postman-fireblocks-contract-interactions-api
- collection_type: postman
  name: Fireblocks Blockchains and Assets Approval Requests Contract Templates API
  slug: postman-fireblocks-contract-templates-api
- collection_type: postman
  name: Fireblocks Blockchains and Assets Approval Requests Cosigners (Beta) API
  slug: postman-fireblocks-cosigners-beta-api
- collection_type: postman
  name: Fireblocks Blockchains and Assets Approval Requests dApp Connections API
  slug: postman-fireblocks-dapp-connections-api
- collection_type: postman
  name: Fireblocks Blockchains and Assets Approval Requests Deployed Contracts API
  slug: postman-fireblocks-deployed-contracts-api
- collection_type: postman
  name: Fireblocks Blockchains and Assets Approval Requests Exchange Accounts API
  slug: postman-fireblocks-exchange-accounts-api
- collection_type: postman
  name: Fireblocks Blockchains and Assets Approval Requests Fiat Accounts API
  slug: postman-fireblocks-fiat-accounts-api
- collection_type: postman
  name: Fireblocks Blockchains and Assets Approval Requests Fireblocks Network API
  slug: postman-fireblocks-fireblocks-network-api
- collection_type: postman
  name: Fireblocks Blockchains and Assets Approval Requests Gas Station API
  slug: postman-fireblocks-gas-station-api
- collection_type: postman
  name: Fireblocks Blockchains and Assets Approval Requests Job Management API
  slug: postman-fireblocks-job-management-api
- collection_type: postman
  name: Fireblocks Blockchains and Assets Approval Requests Key Link API
  slug: postman-fireblocks-key-link-api
- collection_type: postman
  name: Fireblocks Blockchains and Assets Approval Requests Keys (Beta) API
  slug: postman-fireblocks-keys-beta-api
- collection_type: postman
  name: Fireblocks Blockchains and Assets Approval Requests NFTs API
  slug: postman-fireblocks-nfts-api
- collection_type: postman
  name: Fireblocks Blockchains and Assets Approval Requests Off Exchange API
  slug: postman-fireblocks-off-exchange-api
- collection_type: postman
  name: Fireblocks Blockchains and Assets Approval Requests Payments - Flows API
  slug: postman-fireblocks-payments-flows-api
- collection_type: postman
  name: Fireblocks Blockchains and Assets Approval Requests Payments - Payout API
  slug: postman-fireblocks-payments-payout-api
- collection_type: postman
  name: Fireblocks Blockchains and Assets Approval Requests Policy Editor (Beta) API
  slug: postman-fireblocks-policy-editor-beta-api
- collection_type: postman
  name: Fireblocks Blockchains and Assets Approval Requests Policy Editor V2 (Beta) API
  slug: postman-fireblocks-policy-editor-v2-beta-api
- collection_type: postman
  name: Fireblocks Blockchains and Assets Approval Requests Smart Transfers API
  slug: postman-fireblocks-smart-transfers-api
- collection_type: postman
  name: Fireblocks Blockchains and Assets Approval Requests Staking API
  slug: postman-fireblocks-staking-api
- collection_type: postman
  name: Fireblocks Blockchains and Assets Approval Requests Tags API
  slug: postman-fireblocks-tags-api
- collection_type: postman
  name: Fireblocks Blockchains and Assets Approval Requests Tokenization API
  slug: postman-fireblocks-tokenization-api
- collection_type: postman
  name: Fireblocks Blockchains and Assets Approval Requests Trading (Beta) API
  slug: postman-fireblocks-trading-beta-api
- collection_type: postman
  name: Fireblocks Blockchains and Assets Approval Requests Transactions API
  slug: postman-fireblocks-transactions-api
- collection_type: postman
  name: Fireblocks Blockchains and Assets Approval Requests Vaults API
  slug: postman-fireblocks-vaults-api
- collection_type: postman
  name: Fireblocks Blockchains and Assets Approval Requests Webhooks API
  slug: postman-fireblocks-webhooks-api
- collection_type: postman
  name: Fireblocks Blockchains and Assets Approval Requests Webhooks V2 API
  slug: postman-fireblocks-webhooks-v2-api
- collection_type: postman
  name: Fireblocks Blockchains and Assets Approval Requests Whitelisted Contracts API
  slug: postman-fireblocks-whitelisted-contracts-api
- collection_type: postman
  name: Fireblocks Blockchains and Assets Approval Requests Whitelisted External Wallets API
  slug: postman-fireblocks-whitelisted-external-wallets-api
- collection_type: postman
  name: Fireblocks Blockchains and Assets Approval Requests Whitelisted Internal Wallets API
  slug: postman-fireblocks-whitelisted-internal-wallets-api
- collection_type: postman
  name: Fireblocks Blockchains and Assets Approval Requests Workspace Management API
  slug: postman-fireblocks-workspace-management-api
- collection_type: open
  name: Fireblocks Blockchains and Assets API
  slug: open-fireblocks-assets-api
- collection_type: open
  name: Fireblocks Compliance and Policy API
  slug: open-fireblocks-compliance-api
- collection_type: open
  name: Fireblocks Smart Contracts API
  slug: open-fireblocks-contracts-api
- collection_type: open
  name: Fireblocks Exchange and Fiat Accounts API
  slug: open-fireblocks-exchange-api
- collection_type: open
  name: Fireblocks Gas Station API
  slug: open-fireblocks-gas-station-api
- collection_type: open
  name: Fireblocks Network and Off-Exchange API
  slug: open-fireblocks-network-api
- collection_type: open
  name: Fireblocks NFTs API
  slug: open-fireblocks-nfts-api
- collection_type: open
  name: Fireblocks Payments API
  slug: open-fireblocks-payments-api
- collection_type: open
  name: Fireblocks Staking API
  slug: open-fireblocks-staking-api
- collection_type: open
  name: Fireblocks Tokenization API
  slug: open-fireblocks-tokenization-api
- collection_type: open
  name: Fireblocks Transactions API
  slug: open-fireblocks-transactions-api
- collection_type: open
  name: Fireblocks Vaults API
  slug: open-fireblocks-vaults-api
- collection_type: open
  name: Fireblocks Whitelisted Wallets API
  slug: open-fireblocks-wallets-api
- collection_type: open
  name: Fireblocks Webhooks API
  slug: open-fireblocks-webhooks-api
- collection_type: open
  name: Fireblocks Workspace Management API
  slug: open-fireblocks-workspace-api
common:
- group: operate
  title: ''
  type: ChangeLog
  url: https://developers.fireblocks.com/changelog
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/fireblocks/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/fireblocks-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/fireblocks-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fireblocks-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/fireblocks-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://www.fireblocks.com
- group: docs
  title: ''
  type: Documentation
  url: https://developers.fireblocks.com
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.fireblocks.com/docs/quickstart
- group: docs
  title: ''
  type: Documentation
  url: https://developers.fireblocks.com/reference/api-overview
- group: commercial
  title: ''
  type: Pricing
  url: https://www.fireblocks.com/pricing
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/fireblocks
- group: docs
  title: ''
  type: OpenAPI
  url: https://github.com/fireblocks/fireblocks-openapi-spec
- group: docs
  title: ''
  type: OpenAPI
  url: https://github.com/fireblocks/fireblocks-ncw-open-api-spec
- group: operate
  title: ''
  type: StatusPage
  url: https://status.fireblocks.io
- group: company
  title: ''
  type: About
  url: https://www.fireblocks.com/about
- group: operate
  title: ''
  type: ContactForm
  url: https://www.fireblocks.com/contact
- group: company
  title: ''
  type: Careers
  url: https://www.fireblocks.com/careers
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.fireblocks.com/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.fireblocks.com/legal/privacy-notice
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.fireblocks.com/
- group: company
  title: ''
  type: Blog
  url: https://www.fireblocks.com/blog/
- group: company
  title: ''
  type: News
  url: https://www.fireblocks.com/newsroom/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/fireblocks/
- group: company
  title: ''
  type: Twitter
  url: https://x.com/fireblocks
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/c/Fireblocks
- group: other
  title: ''
  type: CaseStudies
  url: https://www.fireblocks.com/customer-stories/
- group: other
  title: ''
  type: Events
  url: https://www.fireblocks.com/events/
- group: learn
  title: ''
  type: Training
  url: https://academy.fireblocks.com/
- group: build
  title: ''
  type: SDKs
  url: https://github.com/fireblocks/fireblocks-sdk-js
- group: build
  title: ''
  type: SDKs
  url: https://github.com/fireblocks/ts-sdk
- group: build
  title: ''
  type: SDKs
  url: https://github.com/fireblocks/fireblocks-sdk-py
- group: build
  title: ''
  type: SDKs
  url: https://github.com/fireblocks/py-sdk
- group: build
  title: ''
  type: SDKs
  url: https://github.com/fireblocks/java-sdk
- group: build
  title: ''
  type: SDKs
  url: https://github.com/fireblocks/fireblocks-web3-provider
- group: build
  title: ''
  type: SDKs
  url: https://github.com/fireblocks/hardhat-fireblocks
- group: build
  title: ''
  type: SDKs
  url: https://github.com/fireblocks/fireblocks-defi-sdk
- group: build
  title: ''
  type: SDKs
  url: https://github.com/fireblocks/fireblocks-defi-sdk-py
- group: build
  title: ''
  type: SDKs
  url: https://github.com/fireblocks/fireblocks-json-rpc
- group: build
  title: ''
  type: SDKs
  url: https://github.com/fireblocks/solana-web3-adapter
- group: build
  title: ''
  type: SDKs
  url: https://github.com/fireblocks/fireblocks-xrp-sdk
- group: build
  title: ''
  type: SDKs
  url: https://github.com/fireblocks/hbar-fireblocks-sdk
- group: build
  title: ''
  type: SDKs
  url: https://github.com/fireblocks/cardano-raw-sdk
- group: build
  title: ''
  type: SDKs
  url: https://github.com/fireblocks/move-fireblocks-sdk
- group: build
  title: ''
  type: SDKs
  url: https://github.com/fireblocks/stacks-fireblocks-sdk
- group: build
  title: ''
  type: SDKs
  url: https://github.com/fireblocks/seismic-sdk
- group: build
  title: ''
  type: CLI
  url: https://github.com/fireblocks/fireblocks-cli
- group: build
  title: ''
  type: CLI
  url: https://github.com/fireblocks/homebrew-fireblocks-cli
- group: build
  title: ''
  type: Tools
  url: https://github.com/fireblocks/recovery
- group: build
  title: ''
  type: Tools
  url: https://github.com/fireblocks/fireblocks-key-recovery-tool
- group: build
  title: ''
  type: Tools
  url: https://github.com/fireblocks/fireblocks-agent
- group: build
  title: ''
  type: Tools
  url: https://github.com/fireblocks/fireblocks-mcp
- group: build
  title: ''
  type: Tools
  url: https://github.com/fireblocks/x402-facilitator
- group: build
  title: ''
  type: Tools
  url: https://github.com/fireblocks/x402-agent
- group: build
  title: ''
  type: Tools
  url: https://github.com/fireblocks/mpc-lib
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/fireblocks/developers-hub
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/fireblocks/retail-demo
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/fireblocks/tokenization-lab
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/fireblocks/ncw-web-demo
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/fireblocks/ncw-web-demo-v2
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/fireblocks/ncw-backend-demo
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/fireblocks/android-ncw-demo
- group: build
  title: ''
  type: SDKs
  url: https://github.com/fireblocks/ncw-ios-sdk
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/fireblocks/ncw-ios-demo
- group: build
  title: ''
  type: SDKs
  url: https://github.com/fireblocks/react-native-ncw-sdk
- group: build
  title: ''
  type: SDKs
  url: https://github.com/fireblocks/ew-ios-sdk
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/fireblocks/ew-node-demo
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/fireblocks/ew-backend-demo
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/fireblocks/plugin-based-callback-handler
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/fireblocks/btc_tx_validation
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/fireblocks/eth_tx_validation
- group: commercial
  title: ''
  type: Plans
  url: https://plans/fireblocks-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: https://rate-limits/fireblocks-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: https://finops/fireblocks-finops.yml
created: '2026-05-25'
description: Fireblocks is an institutional digital-asset and stablecoin infrastructure company providing MPC-secured custody, wallets (custodial and non-custodial / embedded), payments, tokenization, staking, smart contracts, off-exchange settlement, and DeFi security to trading firms, fintechs, exchanges, payment service providers, banks, financial institutions, and Web3 companies. The Fireblocks REST API exposes 236+ operations across 15 surface areas — Vaults, Transactions, Wallets, Assets, Exchange, Tokenization, Contracts, Staking, NFTs, Payments, Network/Off-Exchange, Compliance, Gas Station, Workspace Management, and Webhooks — alongside the separate Non-Custodial Wallet (NCW) API for embedded wallets.
features:
- Institutional-grade digital-asset custody secured by Multi-Party Computation (MPC)
- Vault account hierarchy with 100+ blockchains and 1000s of assets supported
- Workspace Policy Engine — quorum-based transaction authorization rules
- Webhooks V2 with replay-from-history and RSA-SHA512 signature verification
- Fireblocks Network — point-to-point connectivity layer between Fireblocks workspaces and exchanges
- Off-Exchange — collateral remains in MPC custody while mirroring balances to exchanges
- Tokenization Engine — deploy/mint/burn fungible tokens and stablecoins across chains (3-30 bps on AUC)
- Staking — managed validators for ETH, SOL, ADA, DOT, KSM, NEAR, TEZOS, MATIC, and more
- Smart Transfers — atomic multi-leg asset settlement between two counterparties
- Payments Platform and Agentic Payments Suite (agent-initiated payments)
- Embedded Wallets / Non-Custodial Wallets (NCW) — wallet-as-a-service with mobile and web SDKs
- Gas Station — auto-fuel native-asset balances so contract calls don't fail for lack of gas
- dApp Connections via WalletConnect with full policy-engine + simulation protection
- DeFi security suite — transaction simulation, contract whitelisting, dApp protection
- Travel Rule (FATF R.16) compliance with TRLink partner integrations
- AML transaction screening with Chainalysis / Elliptic / TRM Labs integration
- Compliance & AML integrations, address registry, screening events
- Multi-language SDKs — TypeScript (fireblocks-sdk-js, ts-sdk), Python (fireblocks-sdk-py, py-sdk), Java
- EIP-1193 Web3 provider, Hardhat plugin, Solana web3.js adapter
- Chain-specific SDKs for XRPL, Hedera, Cardano, Movement, Stacks, Seismic
- Fireblocks CLI plus Homebrew tap
- Fireblocks Agent — on-prem external key management
- Fireblocks MCP Server for AI agents
- x402 Payment Facilitator and x402 Agent for HTTP 402 micropayments
- Open-source MPC cryptography library (mpc-lib)
- Recovery Utility and Key Recovery Tool for disaster recovery
- JWT signing with RSA 4096 private key — per-request token with body-hash claim
- Sandbox environment with pre-funded test assets and communal test co-signer
- 'Production and Sandbox base URLs: https://api.fireblocks.io/v1, https://sandbox-api.fireblocks.io/v1'
- 'Pricing tiers: Developer Sandbox (free), Essentials ($699/mo + $1M outbound), Pro (from $18k/yr), Enterprise, Enterprise+'
finops:
- name: Fireblocks Finops
  service_category: Digital Asset Infrastructure
  slug: fireblocks-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/fireblocks.png
json_schemas:
- name: Fireblocks Transaction
  property_count: 26
  slug: fireblocks-transaction
- name: Fireblocks Vault Account
  property_count: 6
  slug: fireblocks-vault-account
- name: Fireblocks Webhook Event
  property_count: 4
  slug: fireblocks-webhook-event
jsonld:
- class_count: 0
  name: Fireblocks Context
  property_count: 12
  slug: fireblocks-context
layout: provider
modified: '2026-05-25'
name: fireblocks
nav: Providers
network: true
overview: 'fireblocks publishes 35 APIs on the [APIs.io](https://apis.io/) network, including Vaults API, Transactions API, Tokenization API, and 32 more.


  The fireblocks catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  fireblocks'' developer surface includes changelog, authentication, developer portal, documentation, getting-started guide, pricing, engineering blog, and 67 more developer resources.'
plans:
- name: Fireblocks Plans Pricing
  plan_count: 6
  slug: fireblocks-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 6
  name: Fireblocks Rate Limits
  slug: fireblocks-rate-limits
rules:
- name: fireblocks API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: fireblocks-jsonschema-spectral-rules
score:
  band: exemplar
  composite: 68.8
  delta: 1.6
  facets:
    commercial_clarity: 78.9
    contract_quality: 67.8
    developer_ergonomics: 67.4
    discoverability: 66.7
    governance: 58.3
    operational_transparency: 68.4
  previous_composite: 67.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 35
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/fireblocks/refs/heads/main/screenshots/fireblocks-2026-06-20T181228.png
security:
- kind: authentication
  name: Fireblocks Authentication
  slug: fireblocks-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Fireblocks Domain Security
  slug: fireblocks-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Fireblocks Trust Center
  slug: fireblocks-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018
slug: fireblocks
website: https://www.fireblocks.com
---
