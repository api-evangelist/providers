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
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Biconomy Agentic Access
  operation_count: 5
  slug: biconomy-agentic-access
  summary_line: 5 operations · 5 acting
api_count: 8
apis:
- description: Biconomy's open-source ERC-4337 TypeScript Bundler. Implements eth_sendUserOperation, eth_estimateUserOperationGas, eth_getUserOperationByHash, eth_getUserOperationReceipt, and eth_supportedEntryPoint
  name: Biconomy Bundler API
  slug: biconomy-bundler-api
- description: ERC-4337 paymaster service that fronts gas on behalf of end users so dApps can offer gasless UX. Two modes — full sponsorship (developer pays gas, post-paid invoiced monthly) and pay-in-tokens (user p
  name: Biconomy Sponsorship Paymaster
  slug: biconomy-sponsorship-paymaster
- description: Nexus is Biconomy's ERC-7579 modular smart contract account, audited by CodeHawks-Cyfrin (Sept 2024), Spearbit (Oct/Nov 2024), Zenith (Mar 2025), and Pashov (Mar 2025), and pre-deployed across 20+ EVM
  name: Biconomy Nexus Smart Account
  slug: biconomy-nexus-smart-account
- description: Smart Sessions is a delegated-execution framework layered on Nexus. A session key is granted a scoped set of policies (Sudo, Universal Action, Time Range, Usage Limit) that bound what an agent or auto
  name: Biconomy Smart Sessions API
  slug: biconomy-smart-sessions-api
- description: AbstractJS (@biconomy/abstractjs) is Biconomy's TypeScript-first SDK with a Viem-inspired API. Wraps the Supertransaction API and Nexus smart account operations, exposing createMeeClient, getQuote, ex
  name: Biconomy AbstractJS SDK
  slug: biconomy-abstractjs-sdk
- description: The instructions API from Biconomy — 2 operation(s) for instructions.
  name: Biconomy instructions API
  slug: biconomy-instructions-api
- description: The mee API from Biconomy — 1 operation(s) for mee.
  name: Biconomy mee API
  slug: biconomy-mee-api
- description: The root API from Biconomy — 2 operation(s) for root.
  name: Biconomy root API
  slug: biconomy-root-api
artifact_total: 22
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/biconomy-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/biconomy-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/biconomy-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://www.biconomy.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.biconomy.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.biconomy.io/llms.txt
- group: other
  title: ''
  type: Dashboard
  url: https://dashboard.biconomy.io
- group: other
  title: ''
  type: Explorer
  url: https://meescan.biconomy.io
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/bcnmy
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/bcnmy/nexus
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/bcnmy/abstractjs
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/bcnmy/bundler
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/bcnmy/biconomy-paymasters
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/bcnmy/mee-node
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/bcnmy/mee-contracts
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/bcnmy/stx-contracts
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/bcnmy/erc8211-contracts
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/bcnmy/entry-point-gas-estimations
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/bcnmy/session-permissioned-intents
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/bcnmy/awesome-biconomy
- group: build
  title: ''
  type: SDKs
  url: https://www.npmjs.com/package/@biconomy/abstractjs
- group: docs
  title: ''
  type: Documentation
  url: https://docs.biconomy.io/sdk-reference
- group: docs
  title: ''
  type: Documentation
  url: https://docs.biconomy.io/sdk-reference/account
- group: docs
  title: ''
  type: Documentation
  url: https://docs.biconomy.io/sdk-reference/client
- group: docs
  title: ''
  type: Documentation
  url: https://docs.biconomy.io/sdk-reference/instructions
- group: docs
  title: ''
  type: Documentation
  url: https://docs.biconomy.io/sdk-reference/runtime
- group: docs
  title: ''
  type: Documentation
  url: https://docs.biconomy.io/sdk-reference/conditions
- group: docs
  title: ''
  type: Documentation
  url: https://docs.biconomy.io/sdk-reference/sessions
- group: docs
  title: ''
  type: Documentation
  url: https://docs.biconomy.io/sdk-reference/utilities
- group: docs
  title: ''
  type: Documentation
  url: https://docs.biconomy.io/wallet-integrations
- group: docs
  title: ''
  type: Documentation
  url: https://docs.biconomy.io/wallet-integrations/privy/api
- group: docs
  title: ''
  type: Documentation
  url: https://docs.biconomy.io/wallet-integrations/turnkey/api
- group: docs
  title: ''
  type: Documentation
  url: https://docs.biconomy.io/wallet-integrations/para/api
- group: docs
  title: ''
  type: Documentation
  url: https://docs.biconomy.io/wallet-integrations/external-wallets/api
- group: docs
  title: ''
  type: Documentation
  url: https://docs.biconomy.io/swaps-trading
- group: docs
  title: ''
  type: Documentation
  url: https://docs.biconomy.io/swaps-trading/gasless-swap
- group: docs
  title: ''
  type: Documentation
  url: https://docs.biconomy.io/swaps-trading/cross-chain-swap
- group: docs
  title: ''
  type: Documentation
  url: https://docs.biconomy.io/swaps-trading/limit-order
- group: docs
  title: ''
  type: Documentation
  url: https://docs.biconomy.io/zaps
- group: docs
  title: ''
  type: Documentation
  url: https://docs.biconomy.io/agents-automation
- group: docs
  title: ''
  type: Documentation
  url: https://docs.biconomy.io/gasless-apps
- group: docs
  title: ''
  type: Documentation
  url: https://docs.biconomy.io/gasless-apps/sponsorship
- group: docs
  title: ''
  type: Documentation
  url: https://docs.biconomy.io/gasless-apps/pay-in-tokens
- group: docs
  title: ''
  type: Documentation
  url: https://docs.biconomy.io/contracts-and-audits
- group: docs
  title: ''
  type: Documentation
  url: https://docs.biconomy.io/contracts-and-audits/supported-chains
- group: company
  title: ''
  type: Blog
  url: https://www.biconomy.io/blog
- group: company
  title: ''
  type: Twitter
  url: https://x.com/biconomy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/biconomy
- group: operate
  title: ''
  type: Support
  url: https://discord.gg/biconomy
- group: commercial
  title: ''
  type: Plans
  url: plans/biconomy-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/biconomy-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/biconomy-finops.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/biconomy-vocabulary.yml
- group: design
  title: ''
  type: Rules
  url: rules/biconomy-rules.yml
examples:
- key_count: 3
  name: Biconomy Execute Example
  slug: biconomy-execute-example
- key_count: 3
  name: Biconomy Quote Eoa 7702 Example
  slug: biconomy-quote-eoa-7702-example
finops:
- name: Biconomy Finops
  service_category: Web3 Infrastructure
  slug: biconomy-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/biconomy.png
json_schemas:
- name: Biconomy MEE Quote Request
  property_count: 8
  slug: biconomy-quote-request
- name: Biconomy MEE Quote Response
  property_count: 3
  slug: biconomy-quote-response
json_structures:
- name: Biconomy Supertransaction Structure
  property_count: 1
  slug: biconomy-supertransaction-structure
jsonld:
- class_count: 24
  name: Biconomy Context
  property_count: 3
  slug: biconomy-context
layout: provider
name: Biconomy
nav: Providers
network: true
overview: 'Biconomy publishes 3 APIs on the [APIs.io](https://apis.io/) network: instructions API, mee API, and root API. Tagged areas include Account Abstraction, Blockchain, Bundler, Cross-Chain, and DeFi.


  The Biconomy catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Biconomy''s developer surface includes authentication, developer portal, documentation, engineering blog, support, and 49 more developer resources.'
plans:
- name: Biconomy Plans Pricing
  plan_count: 2
  slug: biconomy-plans-pricing
random_paper: 48
rate_limits:
- limit_count: 3
  name: Biconomy Rate Limits
  slug: biconomy-rate-limits
rules:
- name: Biconomy API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: biconomy-jsonschema-spectral-rules
- name: Biconomy API Rules
  rule_count: 6
  severity_counts:
    error: 4
    hint: 0
    info: 0
    warn: 2
  slug: biconomy-rules
score:
  band: developing
  composite: 54.2
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 72.6
    developer_ergonomics: 41.3
    discoverability: 75.0
    governance: 86.8
    operational_transparency: 31.6
  previous_composite: 54.2
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/biconomy/refs/heads/main/screenshots/biconomy-2026-06-20T173223.png
security:
- kind: authentication
  name: Biconomy Authentication
  slug: biconomy-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Biconomy Domain Security
  slug: biconomy-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: biconomy
tags:
- Account Abstraction
- Blockchain
- Bundler
- Cross-Chain
- DeFi
- ERC-4337
- ERC-7579
- ERC-7702
- Ethereum
- Gas Abstraction
- Gasless
- MEE
- Paymaster
- Smart Accounts
- Smart Sessions
- Wallets
- Web3
website: https://www.biconomy.io
---
