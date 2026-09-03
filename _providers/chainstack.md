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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.9
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 1123
  human_in_the_loop: 0
  name: Chainstack Agentic Access
  operation_count: 1226
  slug: chainstack-agentic-access
  summary_line: 1226 operations · 1123 acting
api_count: 25
apis:
- baseURL: https://api.chainstack.com
  baseurl_source: spec
  description: Public Chainstack-operated testnet faucet for Hoodi, Sepolia, BNB Testnet, zkSync Testnet, Scroll Sepolia, and Polygon Amoy. JWT-authenticated POST /v1/faucet/{chain} request endpoint plus a transacti
  name: Chainstack Faucet API
  slug: chainstack-faucet-api
- baseURL_template: https://{node_id}.p2pify.com/{api_key}
  baseurl_source: spec_template
  description: The Account Info API from Chainstack — 6 operation(s) for account info.
  name: Chainstack Account Info API
  slug: chainstack-account-info-api
- baseURL_template: https://{node_id}.p2pify.com/{api_key}
  baseurl_source: spec_template
  description: The Accounts Info API from Chainstack — 6 operation(s) for accounts info.
  name: Chainstack Accounts Info API
  slug: chainstack-accounts-info-api
- baseURL_template: https://{node_id}.p2pify.com/{api_key}
  baseurl_source: spec_template
  description: The Blocks Info API from Chainstack — 13 operation(s) for blocks info.
  name: Chainstack Blocks Info API
  slug: chainstack-blocks-info-api
- baseURL_template: https://{node_id}.p2pify.com/{api_key}
  baseurl_source: spec_template
  description: The Chain Info API from Chainstack — 5 operation(s) for chain info.
  name: Chainstack Chain Info API
  slug: chainstack-chain-info-api
- baseURL_template: https://{node_id}.p2pify.com/{api_key}
  baseurl_source: spec_template
  description: The Client Info API from Chainstack — 5 operation(s) for client info.
  name: Chainstack Client Info API
  slug: chainstack-client-info-api
- baseURL_template: https://{node_id}.p2pify.com/{api_key}
  baseurl_source: spec_template
  description: The Configuration Info API from Chainstack — 5 operation(s) for configuration info.
  name: Chainstack Configuration Info API
  slug: chainstack-configuration-info-api
- baseURL_template: https://{node_id}.p2pify.com/{api_key}
  baseurl_source: spec_template
  description: The Debug And Trace API from Chainstack — 37 operation(s) for debug and trace.
  name: Chainstack Debug And Trace API
  slug: chainstack-debug-and-trace-api
- baseURL_template: https://{node_id}.p2pify.com/{api_key}
  baseurl_source: spec_template
  description: The Debug API from Chainstack — 3 operation(s) for debug.
  name: Chainstack Debug API
  slug: chainstack-debug-api
- baseURL: https://api.chainstack.com
  baseurl_source: spec
  description: The Deployment Options API from Chainstack — 1 operation(s) for deployment options.
  name: Chainstack Deployment Options API
  slug: chainstack-deployment-options-api
- baseURL_template: https://{node_id}.p2pify.com/{api_key}
  baseurl_source: spec_template
  description: The Events API from Chainstack — 1 operation(s) for events.
  name: Chainstack Events API
  slug: chainstack-events-api
- baseURL_template: https://{node_id}.p2pify.com/{api_key}
  baseurl_source: spec_template
  description: The Execute Transactions API from Chainstack — 6 operation(s) for execute transactions.
  name: Chainstack Execute Transactions API
  slug: chainstack-execute-transactions-api
- baseURL_template: https://{node_id}.p2pify.com/{api_key}
  baseurl_source: spec_template
  description: The Filter Handling API from Chainstack — 5 operation(s) for filter handling.
  name: Chainstack Filter Handling API
  slug: chainstack-filter-handling-api
- baseURL_template: https://{node_id}.p2pify.com/{api_key}
  baseurl_source: spec_template
  description: The Gas Data API from Chainstack — 5 operation(s) for gas data.
  name: Chainstack Gas Data API
  slug: chainstack-gas-data-api
- baseURL_template: https://{node_id}.p2pify.com/{api_key}
  baseurl_source: spec_template
  description: The General API from Chainstack — 520 operation(s) for general.
  name: Chainstack General API
  slug: chainstack-general-api
- baseURL_template: https://{node_id}.p2pify.com/{api_key}
  baseurl_source: spec_template
  description: The Logs And Events API from Chainstack — 3 operation(s) for logs and events.
  name: Chainstack Logs And Events API
  slug: chainstack-logs-and-events-api
- baseURL: https://api.chainstack.com
  baseurl_source: spec
  description: The Network API from Chainstack — 2 operation(s) for network.
  name: Chainstack Network API
  slug: chainstack-network-api
- baseURL: https://api.chainstack.com
  baseurl_source: spec
  description: The Node API from Chainstack — 2 operation(s) for node.
  name: Chainstack Node API
  slug: chainstack-node-api
- baseURL: https://api.chainstack.com
  baseurl_source: spec
  description: The Node V2 API from Chainstack — 2 operation(s) for node v2.
  name: Chainstack Node V2 API
  slug: chainstack-node-v2-api
- baseURL: https://api.chainstack.com
  baseurl_source: spec
  description: The Organization API from Chainstack — 1 operation(s) for organization.
  name: Chainstack Organization API
  slug: chainstack-organization-api
- baseURL: https://api.chainstack.com
  baseurl_source: spec
  description: The Project API from Chainstack — 3 operation(s) for project.
  name: Chainstack Project API
  slug: chainstack-project-api
- baseURL: https://api.chainstack.com
  baseurl_source: spec
  description: The Project V2 API from Chainstack — 2 operation(s) for project v2.
  name: Chainstack Project V2 API
  slug: chainstack-project-v2-api
- baseURL_template: https://{node_id}.p2pify.com/{api_key}
  baseurl_source: spec_template
  description: The State API from Chainstack — 10 operation(s) for state.
  name: Chainstack State API
  slug: chainstack-state-api
- baseURL_template: https://{node_id}.p2pify.com/{api_key}
  baseurl_source: spec_template
  description: The Tempo Specific API from Chainstack — 2 operation(s) for tempo specific.
  name: Chainstack Tempo Specific API
  slug: chainstack-tempo-specific-api
- baseURL_template: https://{node_id}.p2pify.com/{api_key}
  baseurl_source: spec_template
  description: The Transaction Info API from Chainstack — 14 operation(s) for transaction info.
  name: Chainstack Transaction Info API
  slug: chainstack-transaction-info-api
- baseURL_template: https://{node_id}.p2pify.com/{api_key}
  baseurl_source: spec_template
  description: The Transactions Info API from Chainstack — 5 operation(s) for transactions info.
  name: Chainstack Transactions Info API
  slug: chainstack-transactions-info-api
- baseURL_template: https://{node_id}.p2pify.com/{api_key}
  baseurl_source: spec_template
  description: The Txpool API from Chainstack — 2 operation(s) for txpool.
  name: Chainstack Txpool API
  slug: chainstack-txpool-api
- baseURL_template: https://{node_id}.p2pify.com/{api_key}
  baseurl_source: spec_template
  description: The V2 API from Chainstack — 29 operation(s) for v2.
  name: Chainstack V2 API
  slug: chainstack-v2-api
- baseURL_template: https://{node_id}.p2pify.com/{api_key}
  baseurl_source: spec_template
  description: The V3 API from Chainstack — 30 operation(s) for v3.
  name: Chainstack V3 API
  slug: chainstack-v3-api
- baseURL_template: https://{node_id}.p2pify.com/{api_key}
  baseurl_source: spec_template
  description: The Validatiors Info API from Chainstack — 12 operation(s) for validatiors info.
  name: Chainstack Validatiors Info API
  slug: chainstack-validatiors-info-api
- baseURL_template: https://{node_id}.p2pify.com/{api_key}
  baseurl_source: spec_template
  description: The Zkevm Methods API from Chainstack — 8 operation(s) for zkevm methods.
  name: Chainstack Zkevm Methods API
  slug: chainstack-zkevm-methods-api
artifact_total: 135
asyncapis:
- description: AsyncAPI 2.6 specification for Chainstack's JSON-RPC WebSocket (WSS) subscription APIs. Chainstack-managed nodes expose a persistent WebSocket endpoint per node that accepts JSON-RPC 2.0 messages. Cli
  name: Chainstack RPC WebSocket APIs
  slug: chainstack-asyncapi
collections:
- collection_type: postman
  name: Chainstack Arbitrum Node Account Info API
  slug: postman-chainstack-account-info-api
- collection_type: postman
  name: Chainstack Arbitrum Node Account Info Accounts Info API
  slug: postman-chainstack-accounts-info-api
- collection_type: postman
  name: Chainstack Arbitrum Node Account Info Blocks Info API
  slug: postman-chainstack-blocks-info-api
- collection_type: postman
  name: Chainstack Arbitrum Node Account Info Chain Info API
  slug: postman-chainstack-chain-info-api
- collection_type: postman
  name: Chainstack Arbitrum Node Account Info Client Info API
  slug: postman-chainstack-client-info-api
- collection_type: postman
  name: Chainstack Arbitrum Node Account Info Configuration Info API
  slug: postman-chainstack-configuration-info-api
- collection_type: postman
  name: Chainstack Arbitrum Node Account Info Debug And Trace API
  slug: postman-chainstack-debug-and-trace-api
- collection_type: postman
  name: Chainstack Arbitrum Node Account Info Debug API
  slug: postman-chainstack-debug-api
- collection_type: postman
  name: Chainstack Arbitrum Node Account Info Deployment Options API
  slug: postman-chainstack-deployment-options-api
- collection_type: postman
  name: Chainstack Arbitrum Node Account Info Events API
  slug: postman-chainstack-events-api
- collection_type: postman
  name: Chainstack Arbitrum Node Account Info Execute Transactions API
  slug: postman-chainstack-execute-transactions-api
- collection_type: postman
  name: Chainstack Arbitrum Node Account Info faucet API
  slug: postman-chainstack-faucet-api
- collection_type: postman
  name: Chainstack Arbitrum Node Account Info Filter Handling API
  slug: postman-chainstack-filter-handling-api
- collection_type: postman
  name: Chainstack Arbitrum Node Account Info Gas Data API
  slug: postman-chainstack-gas-data-api
- collection_type: postman
  name: Chainstack Arbitrum Node Account Info General API
  slug: postman-chainstack-general-api
- collection_type: postman
  name: Chainstack Arbitrum Node Account Info History API
  slug: postman-chainstack-history-api
- collection_type: postman
  name: Chainstack Arbitrum Node Account Info Logs And Events API
  slug: postman-chainstack-logs-and-events-api
- collection_type: postman
  name: Chainstack Arbitrum Node Account Info Network API
  slug: postman-chainstack-network-api
- collection_type: postman
  name: Chainstack Arbitrum Account Info Node API
  slug: postman-chainstack-node-api
- collection_type: postman
  name: Chainstack Arbitrum Node Account Info Node V2 API
  slug: postman-chainstack-node-v2-api
- collection_type: postman
  name: Chainstack Arbitrum Node Account Info Organization API
  slug: postman-chainstack-organization-api
- collection_type: postman
  name: Chainstack Arbitrum Node Account Info Project API
  slug: postman-chainstack-project-api
- collection_type: postman
  name: Chainstack Arbitrum Node Account Info Project V2 API
  slug: postman-chainstack-project-v2-api
- collection_type: postman
  name: Chainstack Arbitrum Node Account Info State API
  slug: postman-chainstack-state-api
- collection_type: postman
  name: Chainstack Arbitrum Node Account Info Tempo Specific API
  slug: postman-chainstack-tempo-specific-api
- collection_type: postman
  name: Chainstack Arbitrum Node Account Info Transaction Info API
  slug: postman-chainstack-transaction-info-api
- collection_type: postman
  name: Chainstack Arbitrum Node Account Info Transactions Info API
  slug: postman-chainstack-transactions-info-api
- collection_type: postman
  name: Chainstack Arbitrum Node Account Info Txpool API
  slug: postman-chainstack-txpool-api
- collection_type: postman
  name: Chainstack Arbitrum Node Account Info V2 API
  slug: postman-chainstack-v2-api
- collection_type: postman
  name: Chainstack Arbitrum Node Account Info V3 API
  slug: postman-chainstack-v3-api
- collection_type: postman
  name: Chainstack Arbitrum Node Account Info Validatiors Info API
  slug: postman-chainstack-validatiors-info-api
- collection_type: postman
  name: Chainstack Arbitrum Node Account Info Zkevm Methods API
  slug: postman-chainstack-zkevm-methods-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Chainstack Arbitrum Node Account Info API
  slug: open-chainstack-account-info-api
- collection_type: open
  name: Chainstack Arbitrum Node Account Info Accounts Info API
  slug: open-chainstack-accounts-info-api
- collection_type: open
  name: Chainstack Arbitrum Node API
  slug: open-chainstack-arbitrum-node-api
- collection_type: open
  name: Chainstack Aurora Node API
  slug: open-chainstack-aurora-node-api
- collection_type: open
  name: Chainstack Avalanche Node API
  slug: open-chainstack-avalanche-node-api
- collection_type: open
  name: Chainstack Base Node API
  slug: open-chainstack-base-node-api
- collection_type: open
  name: Chainstack Bitcoin Node API
  slug: open-chainstack-bitcoin-node-api
- collection_type: open
  name: Chainstack Arbitrum Node Account Info Blocks Info API
  slug: open-chainstack-blocks-info-api
- collection_type: open
  name: Chainstack BNB Smart Chain Node API
  slug: open-chainstack-bnb-node-api
- collection_type: open
  name: Chainstack Arbitrum Node Account Info Chain Info API
  slug: open-chainstack-chain-info-api
- collection_type: open
  name: Chainstack Arbitrum Node Account Info Client Info API
  slug: open-chainstack-client-info-api
- collection_type: open
  name: Chainstack Arbitrum Node Account Info Configuration Info API
  slug: open-chainstack-configuration-info-api
- collection_type: open
  name: Chainstack Cronos Node API
  slug: open-chainstack-cronos-node-api
- collection_type: open
  name: Chainstack Arbitrum Node Account Info Debug And Trace API
  slug: open-chainstack-debug-and-trace-api
- collection_type: open
  name: Chainstack Arbitrum Node Account Info Debug API
  slug: open-chainstack-debug-api
- collection_type: open
  name: Chainstack Arbitrum Node Account Info Deployment Options API
  slug: open-chainstack-deployment-options-api
- collection_type: open
  name: Chainstack Ethereum Beacon Chain API
  slug: open-chainstack-ethereum-beacon-chain-api
- collection_type: open
  name: Chainstack Ethereum Node API
  slug: open-chainstack-ethereum-node-api
- collection_type: open
  name: Chainstack Arbitrum Node Account Info Events API
  slug: open-chainstack-events-api
- collection_type: open
  name: Chainstack Arbitrum Node Account Info Execute Transactions API
  slug: open-chainstack-execute-transactions-api
- collection_type: open
  name: Chainstack Fantom Node API
  slug: open-chainstack-fantom-node-api
- collection_type: open
  name: Chainstack Arbitrum Node Account Info faucet API
  slug: open-chainstack-faucet-api
- collection_type: open
  name: Chainstack Arbitrum Node Account Info Filter Handling API
  slug: open-chainstack-filter-handling-api
- collection_type: open
  name: Chainstack Arbitrum Node Account Info Gas Data API
  slug: open-chainstack-gas-data-api
- collection_type: open
  name: Chainstack Arbitrum Node Account Info General API
  slug: open-chainstack-general-api
- collection_type: open
  name: Chainstack Gnosis Node API
  slug: open-chainstack-gnosis-node-api
- collection_type: open
  name: Chainstack Arbitrum Node Account Info History API
  slug: open-chainstack-history-api
- collection_type: open
  name: Chainstack Hyperliquid Node API
  slug: open-chainstack-hyperliquid-node-api
- collection_type: open
  name: Chainstack Arbitrum Node Account Info Logs And Events API
  slug: open-chainstack-logs-and-events-api
- collection_type: open
  name: Chainstack Monad Node API
  slug: open-chainstack-monad-node-api
- collection_type: open
  name: Chainstack Arbitrum Node Account Info Network API
  slug: open-chainstack-network-api
- collection_type: open
  name: Chainstack Arbitrum Account Info Node API
  slug: open-chainstack-node-api
- collection_type: open
  name: Chainstack Arbitrum Node Account Info Node V2 API
  slug: open-chainstack-node-v2-api
- collection_type: open
  name: Chainstack Optimism Node API
  slug: open-chainstack-optimism-node-api
- collection_type: open
  name: Chainstack Arbitrum Node Account Info Organization API
  slug: open-chainstack-organization-api
- collection_type: open
  name: Chainstack Plasma Node API
  slug: open-chainstack-plasma-node-api
- collection_type: open
  name: 💙 CHAINSTACK PLATFORM API
  slug: open-chainstack-platform-api
- collection_type: open
  name: Chainstack Polygon Node API
  slug: open-chainstack-polygon-node-api
- collection_type: open
  name: Chainstack Polygon zkEVM Node API
  slug: open-chainstack-polygon-zkevm-node-api
- collection_type: open
  name: Chainstack Arbitrum Node Account Info Project API
  slug: open-chainstack-project-api
- collection_type: open
  name: Chainstack Arbitrum Node Account Info Project V2 API
  slug: open-chainstack-project-v2-api
- collection_type: open
  name: Chainstack Ronin Node API
  slug: open-chainstack-ronin-node-api
- collection_type: open
  name: Chainstack Solana Node API
  slug: open-chainstack-solana-node-api
- collection_type: open
  name: Chainstack Starknet Node API
  slug: open-chainstack-starknet-node-api
- collection_type: open
  name: Chainstack Arbitrum Node Account Info State API
  slug: open-chainstack-state-api
- collection_type: open
  name: Chainstack Tempo Node API
  slug: open-chainstack-tempo-node-api
- collection_type: open
  name: Chainstack Arbitrum Node Account Info Tempo Specific API
  slug: open-chainstack-tempo-specific-api
- collection_type: open
  name: Chainstack TON Node API
  slug: open-chainstack-ton-node-api
- collection_type: open
  name: Chainstack Arbitrum Node Account Info Transaction Info API
  slug: open-chainstack-transaction-info-api
- collection_type: open
  name: Chainstack Arbitrum Node Account Info Transactions Info API
  slug: open-chainstack-transactions-info-api
- collection_type: open
  name: Chainstack TRON Node API
  slug: open-chainstack-tron-node-api
- collection_type: open
  name: Chainstack Arbitrum Node Account Info Txpool API
  slug: open-chainstack-txpool-api
- collection_type: open
  name: Chainstack Arbitrum Node Account Info V2 API
  slug: open-chainstack-v2-api
- collection_type: open
  name: Chainstack Arbitrum Node Account Info V3 API
  slug: open-chainstack-v3-api
- collection_type: open
  name: Chainstack Arbitrum Node Account Info Validatiors Info API
  slug: open-chainstack-validatiors-info-api
- collection_type: open
  name: Chainstack Arbitrum Node Account Info Zkevm Methods API
  slug: open-chainstack-zkevm-methods-api
- collection_type: open
  name: Chainstack zkSync Era Node API
  slug: open-chainstack-zksync-node-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/chainstack-capability-edges.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/chainstack/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/chainstack-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/chainstack-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/chainstack-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/chainstack-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/chainstack/
- group: company
  title: ''
  type: Twitter
  url: https://x.com/chainstackhq
- group: build
  title: ''
  type: Github
  url: https://github.com/chainstack
- group: operate
  title: ''
  type: Discord
  url: https://discord.com/invite/Cymtg2f7pX
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@Chainstack
- group: company
  title: ''
  type: Website
  url: https://chainstack.com
- group: start
  title: ''
  type: Portal
  url: https://docs.chainstack.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.chainstack.com/reference/platform-api-getting-started
- group: docs
  title: ''
  type: Documentation
  url: https://docs.chainstack.com/reference/getting-started
- group: operate
  title: ''
  type: RateLimits
  url: https://docs.chainstack.com/docs/about-limits
- group: docs
  title: ''
  type: Documentation
  url: https://docs.chainstack.com/docs/about-billing
- group: docs
  title: ''
  type: Documentation
  url: https://docs.chainstack.com/docs/pricing
- group: commercial
  title: ''
  type: Pricing
  url: https://chainstack.com/pricing/
- group: other
  title: ''
  type: Faucet
  url: https://faucet.chainstack.com/
- group: operate
  title: ''
  type: Support
  url: https://support.chainstack.com
- group: other
  title: ''
  type: Feedback
  url: https://ideas.chainstack.com/
- group: company
  title: ''
  type: Blog
  url: https://chainstack.com/blog/
- group: operate
  title: ''
  type: ChangeLog
  url: https://chainstack.com/changelog/
- group: operate
  title: ''
  type: StatusPage
  url: https://chainstack.status.io
- group: commercial
  title: ''
  type: TermsOfService
  url: https://chainstack.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://chainstack.com/privacy-policy/
- group: auth
  title: ''
  type: Security
  url: https://chainstack.com/security/
- group: other
  title: ''
  type: Source
  url: https://github.com/chainstack/dev-portal
- group: other
  title: ''
  type: Source
  url: https://github.com/chainstack/erigon
- group: other
  title: ''
  type: Source
  url: https://github.com/chainstack/bsc-erigon
- group: other
  title: ''
  type: Source
  url: https://github.com/chainstack/op-erigon
- group: build
  title: ''
  type: Tools
  url: https://github.com/chainstack/solana-exporter
- group: build
  title: ''
  type: SDKs
  url: https://github.com/chainstack/solana-rpc-ruby
- group: build
  title: ''
  type: SDKs
  url: https://github.com/chainstack/multichaincli
- group: build
  title: ''
  type: SDKs
  url: https://github.com/chainstack/bitcoincli
- group: build
  title: ''
  type: SDKs
  url: https://github.com/chainstack/web3quorum
- group: build
  title: ''
  type: Tools
  url: https://github.com/chainstack/terraform-openstack-rke2
- group: other
  title: ''
  type: Product
  url: https://chainstack.com/products/global-nodes/
- group: other
  title: ''
  type: Product
  url: https://chainstack.com/products/dedicated-nodes/
- group: other
  title: ''
  type: Product
  url: https://chainstack.com/products/unlimited-nodes/
- group: other
  title: ''
  type: Product
  url: https://chainstack.com/products/trader-nodes/
- group: other
  title: ''
  type: Product
  url: https://chainstack.com/products/yellowstone-grpc/
- group: docs
  title: ''
  type: Documentation
  url: https://chainstack.com/build-better/
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/chainstack-vocabulary.yml
- group: design
  title: ''
  type: SpectralRules
  url: rules/chainstack-rules.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/chainstack-finops.yml
description: Chainstack is a managed multi-chain RPC and node infrastructure platform supporting 70+ blockchain protocols including Ethereum, Solana, Bitcoin, BNB Smart Chain, Polygon, Arbitrum, Optimism, Base, Avalanche, TON, TRON, Starknet, zkSync Era, Hyperliquid, Monad, and many more. The platform exposes a REST Platform API for organization, project, network, and node lifecycle management, JSON-RPC endpoints for every supported chain, a Faucet API for testnet funding, real- time Solana streaming via Yellowstone gRPC, low-latency Trader Nodes via bloXroute, archive data with debug and trace namespaces, MEV protection, Flashblocks preconfirmations, and a Chainstack MCP server for AI agents.
finops:
- name: Chainstack Finops
  service_category: Blockchain Infrastructure
  slug: chainstack-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/chainstack.png
json_schemas:
- name: ChainstackJsonRpcEnvelope
  property_count: 0
  slug: chainstack-jsonrpc-envelope
- name: ChainstackNode
  property_count: 11
  slug: chainstack-node
jsonld:
- class_count: 0
  name: Chainstack Context
  property_count: 8
  slug: chainstack-context
layout: provider
modified: 2026-05-29 00:00:00+00:00
name: Chainstack
nav: Providers
network: true
overview: 'Chainstack publishes 31 APIs on the [APIs.io](https://apis.io/) network, including Faucet API, Account Info API, Accounts Info API, and 28 more. Tagged areas include Blockchain, Multi-Chain, RPC, Node Infrastructure, and Web3.


  The Chainstack catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 3 Spectral governance rulesets.


  Chainstack''s developer surface includes authentication, GitHub presence, YouTube channel, developer portal, documentation, pricing, support, and 40 more developer resources.'
plans:
- name: Chainstack Plans Pricing
  plan_count: 6
  slug: chainstack-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 10
  name: Chainstack Rate Limits
  slug: chainstack-rate-limits
rules:
- effective_rule_count: 35
  extends:
  - spectral:asyncapi
  name: Chainstack API Rules
  rule_count: 8
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 6
  slug: chainstack-asyncapi-spectral-rules
- effective_rule_count: 6
  extends: []
  name: Chainstack API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: chainstack-jsonschema-spectral-rules
- effective_rule_count: 48
  extends:
  - spectral:oas
  name: Chainstack API Rules
  rule_count: 7
  severity_counts:
    error: 2
    hint: 0
    info: 0
    warn: 5
  slug: chainstack-rules
score:
  band: strong
  composite: 60.9
  coverage:
    artifact_dirs: 17
    catalog_gap: 36.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 71.1
    commercial_clarity: 71.1
    contract_governance: 28.8
    contract_quality: 66.9
    developer_ergonomics: 59.5
    discoverability: 50.0
    governance: 28.8
    operational_transparency: 73.7
  previous_composite: 60.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 32
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/chainstack/refs/heads/main/screenshots/chainstack-2026-06-20T174203.png
security:
- kind: authentication
  name: Chainstack Authentication
  slug: chainstack-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Chainstack Domain Security
  slug: chainstack-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Chainstack Vulnerability Disclosure
  slug: chainstack-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: chainstack
tags:
- Blockchain
- Multi-Chain
- RPC
- Node Infrastructure
- Web3
- Crypto
- Ethereum
- Solana
- Bitcoin
- DeFi
- MEV
- Trader Node
- Archive Data
- MCP
- AI Agents
website: https://chainstack.com
---
