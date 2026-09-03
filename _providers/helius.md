---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: near-conformant
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
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.6
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 16
  human_in_the_loop: 0
  name: Helius Agentic Access
  operation_count: 31
  slug: helius-agentic-access
  summary_line: 31 operations · 16 acting
api_count: 1
apis:
- baseURL: https://mainnet.helius-rpc.com/?api-key={apiKey}
  baseurl_source: declared
  description: Solana JSON-RPC and WebSocket endpoints with enhanced WebSockets, archival data, and staked connections.
  name: Helius Solana RPC
  slug: rpc
- description: Solana JSON-RPC API for unified asset queries (compressed NFTs, regular NFTs, tokens) including getAsset, getAssetsByOwner, searchAssets.
  name: Helius Digital Asset Standard (DAS) API
  slug: das
- description: REST API for parsed and human-readable Solana transaction history with token metadata.
  name: Helius Enhanced Transactions API
  slug: enhanced-tx
- description: REST API for managing webhook subscriptions for Solana on-chain events with parsed transaction payloads.
  name: Helius Webhooks
  slug: webhooks
- description: Low-latency gRPC streaming of Solana account, slot, transaction, and block updates (Geyser-compatible).
  name: Helius LaserStream
  slug: laserstream
- description: Parallel transaction routing through Helius and Jito for inclusion latency optimization.
  name: Helius Sender
  slug: sender
- description: Indexed RPC for Solana ZK compression (compressed accounts).
  name: Helius Photon RPC (ZK Compression)
  slug: photon
- baseURL: https://mainnet.helius-rpc.com/?api-key={apiKey}
  baseurl_source: declared
  description: Enhanced on-chain identity data with complete wallet activity and ownership information.
  name: Helius Addresses API
  slug: helius-addresses-api
- baseURL: https://mainnet.helius-rpc.com/?api-key={apiKey}
  baseurl_source: declared
  description: The Admin API from Helius — 1 operation(s) for admin.
  name: Helius Admin API
  slug: helius-admin-api
- baseURL: https://mainnet.helius-rpc.com/?api-key={apiKey}
  baseurl_source: declared
  description: Query token and NFT balances
  name: Helius Balances API
  slug: helius-balances-api
- baseURL: https://mainnet.helius-rpc.com/?api-key={apiKey}
  baseurl_source: declared
  description: Wallet funding information
  name: Helius Funding API
  slug: helius-funding-api
- baseURL: https://mainnet.helius-rpc.com/?api-key={apiKey}
  baseurl_source: declared
  description: The Helius API Catalog API from Helius — 1 operation(s) for helius api catalog.
  name: Helius Helius API Catalog API
  slug: helius-helius-api-catalog-api
- baseURL: https://mainnet.helius-rpc.com/?api-key={apiKey}
  baseurl_source: declared
  description: Transaction history and balance changes
  name: Helius History API
  slug: helius-history-api
- baseURL: https://mainnet.helius-rpc.com/?api-key={apiKey}
  baseurl_source: declared
  description: Lookup wallet identities and known addresses
  name: Helius Identity API
  slug: helius-identity-api
- baseURL: https://mainnet.helius-rpc.com/?api-key={apiKey}
  baseurl_source: declared
  description: Access comprehensive NFT data including events, collection aggregations, real-time stats, and complete historical activity on Solana.
  name: Helius NFTs API
  slug: helius-nfts-api
- baseURL: https://mainnet.helius-rpc.com/?api-key={apiKey}
  baseurl_source: declared
  description: The Sender API from Helius — 2 operation(s) for sender.
  name: Helius Sender API
  slug: helius-sender-api
- baseURL: https://mainnet.helius-rpc.com/?api-key={apiKey}
  baseurl_source: declared
  description: Complete token account data, on-chain and off-chain metadata, and detailed information for both fungible and non-fungible Solana tokens.
  name: Helius Tokens API
  slug: helius-tokens-api
- baseURL: https://mainnet.helius-rpc.com/?api-key={apiKey}
  baseurl_source: declared
  description: Enhanced and human-readable transaction histories with decoded instruction data and detailed context.
  name: Helius Transactions API
  slug: helius-transactions-api
- baseURL: https://mainnet.helius-rpc.com/?api-key={apiKey}
  baseurl_source: declared
  description: Token transfer activity
  name: Helius Transfers API
  slug: helius-transfers-api
- baseURL: https://mainnet.helius-rpc.com/?api-key={apiKey}
  baseurl_source: declared
  description: Configure real-time blockchain notifications for any Solana address, transaction type, or on-chain event with customizable delivery options.
  name: Helius Webhooks API
  slug: helius-webhooks-api
artifact_total: 44
asyncapis:
- description: 'AsyncAPI 2.6 description of Helius''s real-time WebSocket interfaces for Solana. Coverage: * Standard Solana JSON-RPC PubSub subscriptions exposed by Helius RPC. * Helius enhanced subscriptions (transa'
  name: Helius WebSocket APIs
  slug: helius-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Helius API Catalog Addresses API
  slug: open-helius-addresses-api
- collection_type: open
  name: Helius API Catalog Addresses Admin API
  slug: open-helius-admin-api
- collection_type: open
  name: Helius API Catalog Addresses Balances API
  slug: open-helius-balances-api
- collection_type: open
  name: Helius API Catalog Addresses Funding API
  slug: open-helius-funding-api
- collection_type: open
  name: Addresses Helius API Catalog API
  slug: open-helius-helius-api-catalog-api
- collection_type: open
  name: Helius API Catalog Addresses History API
  slug: open-helius-history-api
- collection_type: open
  name: Helius API Catalog Addresses Identity API
  slug: open-helius-identity-api
- collection_type: open
  name: Helius API Catalog Addresses NFTs API
  slug: open-helius-nfts-api
- collection_type: open
  name: Helius API Catalog Addresses Sender API
  slug: open-helius-sender-api
- collection_type: open
  name: Helius API Catalog Addresses Tokens API
  slug: open-helius-tokens-api
- collection_type: open
  name: Helius API Catalog Addresses Transactions API
  slug: open-helius-transactions-api
- collection_type: open
  name: Helius API Catalog Addresses Transfers API
  slug: open-helius-transfers-api
- collection_type: open
  name: Helius API Catalog Addresses Webhooks API
  slug: open-helius-webhooks-api
- collection_type: open
  name: Helius API Catalog
  slug: open-helius
common:
- group: other
  title: ''
  type: AgentCard
  url: a2a/helius-a2a.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/helius-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/helius-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/helius-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/helius-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/helius-labs
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/heliusapi
- group: company
  title: ''
  type: Website
  url: https://www.helius.dev/
- group: commercial
  title: ''
  type: Plans
  url: plans/helius-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/helius-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/helius-finops.yml
created: '2026-05-08'
description: Helius is a Solana developer platform offering Solana JSON-RPC, the Digital Asset Standard (DAS) API for NFTs/tokens, Enhanced Transactions, Webhooks, LaserStream gRPC streaming, Sender (transaction routing), Photon RPC, and Dedicated Nodes.
finops:
- name: Helius Finops
  service_category: Web3
  slug: helius-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-05-29'
name: Helius
nav: Providers
network: true
overview: 'Helius publishes 14 APIs on the [APIs.io](https://apis.io/) network, including Solana RPC, Addresses API, Admin API, and 11 more. Tagged areas include Web3, Blockchain, Solana, RPC, and DAS.


  The Helius catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Helius'' developer surface includes authentication and 10 more developer resources.'
plans:
- name: Helius Plans Pricing
  plan_count: 5
  slug: helius-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 5
  name: Helius Rate Limits
  slug: helius-rate-limits
rules:
- effective_rule_count: 35
  extends:
  - spectral:asyncapi
  name: Helius API Rules
  rule_count: 8
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 6
  slug: helius-asyncapi-spectral-rules
score:
  band: thin
  composite: 32.9
  coverage:
    artifact_dirs: 13
    catalog_gap: 64.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 13.6
    contract_quality: 62.3
    developer_ergonomics: 21.4
    discoverability: 68.5
    governance: 13.6
    operational_transparency: 10.5
  previous_composite: 32.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 13
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/helius/refs/heads/main/screenshots/helius-2026-06-20T182630.png
security:
- kind: authentication
  name: Helius Authentication
  slug: helius-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Helius Domain Security
  slug: helius-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Helius Vulnerability Disclosure
  slug: helius-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: helius
tags:
- Web3
- Blockchain
- Solana
- RPC
- DAS
- Streams
website: https://www.helius.dev/
---
