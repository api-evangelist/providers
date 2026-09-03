---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.3
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 16
  human_in_the_loop: 0
  name: Triton One Agentic Access
  operation_count: 23
  slug: triton-one-agentic-access
  summary_line: 23 operations · 16 acting
api_count: 3
apis:
- description: Dragon's Mouth — Triton's high-performance Solana streaming gRPC service. Subscribe to slots, blocks, transactions, accounts, and blockmeta updates over a single bidirectional gRPC stream. Open-source
  name: Triton One Yellowstone gRPC (Dragon's Mouth)
  slug: triton-one-yellowstone-grpc
- description: Fumarole — persistent Yellowstone streams with gap-free reconnect and 4-day server-side cache. Built for consumers that must not miss events across client restarts or network blips.
  name: Triton One Fumarole Persistent Streams
  slug: triton-one-fumarole
- description: Whirligig — Triton's enhanced WebSocket layer over Solana RPC. Adds the missing transactionSubscribe stream and hardened account/slot subscribe behaviour with stable backpressure.
  name: Triton One Whirligig WebSockets
  slug: triton-one-whirligig-websockets
- description: Old Faithful — content-addressable, queryable archive of all Solana history from genesis. Complete-ledger queries in milliseconds, flat-rate pricing across all epochs and methods. Open-source server a
  name: Triton One Old Faithful Historical Archive
  slug: triton-one-old-faithful
- description: Cascade — high-performance transaction delivery network leveraging Solana's Stake-Weighted Quality of Service (SWQoS). Routes transactions through reserved, private connection pools of staked validato
  name: Triton One Cascade Transaction Delivery
  slug: triton-one-cascade
- description: Hosted trading APIs available on the Triton platform — Pyth Hermes price feeds, Jito bundle simulation, Metis Swap, and Titan Swap. Metered separately under the unified PAYG pricing model.
  name: Triton One Trading APIs
  slug: triton-one-trading-apis
- baseURL: https://customers.triton.one/api/v1
  baseurl_source: declared
  description: Manage customer accounts.
  name: Triton One Accounts API
  slug: triton-one-accounts-api
- baseURL: https://customers.triton.one/api/v1
  baseurl_source: declared
  description: Manage on-chain address watch lists for collections and Merkle trees.
  name: Triton One AddressWatchLists API
  slug: triton-one-addresswatchlists-api
- baseURL: https://customers.triton.one/api/v1
  baseurl_source: declared
  description: Read methods for compressed and standard digital assets.
  name: Triton One Assets API
  slug: triton-one-assets-api
- baseURL: https://customers.triton.one/api/v1
  baseurl_source: declared
  description: Manage RPC endpoints attached to subscriptions.
  name: Triton One Endpoints API
  slug: triton-one-endpoints-api
- baseURL: https://customers.triton.one/api/v1
  baseurl_source: declared
  description: Standard Solana JSON-RPC methods accepted at the same endpoint.
  name: Triton One Standard API
  slug: triton-one-standard-api
- baseURL: https://customers.triton.one/api/v1
  baseurl_source: declared
  description: Manage subscriptions (Developer, Mainnet-Shared, Mainnet-Dedicated).
  name: Triton One Subscriptions API
  slug: triton-one-subscriptions-api
- baseURL: https://customers.triton.one/api/v1
  baseurl_source: declared
  description: Manage RPC consumption tokens.
  name: Triton One Tokens API
  slug: triton-one-tokens-api
artifact_total: 69
collections:
- collection_type: postman
  name: Triton One Customers Accounts API
  slug: postman-triton-one-accounts-api
- collection_type: postman
  name: Triton One Customers Accounts AddressWatchLists API
  slug: postman-triton-one-addresswatchlists-api
- collection_type: postman
  name: Triton One Customers Accounts Assets API
  slug: postman-triton-one-assets-api
- collection_type: postman
  name: Triton One Customers Accounts Endpoints API
  slug: postman-triton-one-endpoints-api
- collection_type: postman
  name: Triton One Customers Accounts Standard API
  slug: postman-triton-one-standard-api
- collection_type: postman
  name: Triton One Customers Accounts Subscriptions API
  slug: postman-triton-one-subscriptions-api
- collection_type: postman
  name: Triton One Customers Accounts Tokens API
  slug: postman-triton-one-tokens-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Triton One Customers Accounts API
  slug: open-triton-one-accounts-api
- collection_type: open
  name: Triton One Customers Accounts AddressWatchLists API
  slug: open-triton-one-addresswatchlists-api
- collection_type: open
  name: Triton One Customers Accounts Assets API
  slug: open-triton-one-assets-api
- collection_type: open
  name: Triton One Customers API
  slug: open-triton-one-customers-api
- collection_type: open
  name: Triton One Digital Assets API
  slug: open-triton-one-digital-assets-api
- collection_type: open
  name: Triton One Customers Accounts Endpoints API
  slug: open-triton-one-endpoints-api
- collection_type: open
  name: Triton One Solana RPC API
  slug: open-triton-one-solana-rpc-api
- collection_type: open
  name: Triton One Customers Accounts Standard API
  slug: open-triton-one-standard-api
- collection_type: open
  name: Triton One Customers Accounts Subscriptions API
  slug: open-triton-one-subscriptions-api
- collection_type: open
  name: Triton One Customers Accounts Tokens API
  slug: open-triton-one-tokens-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/triton-one/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/triton-one-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/triton-one-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/triton-one-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://triton.one
- group: docs
  title: ''
  type: Documentation
  url: https://docs.triton.one
- group: commercial
  title: ''
  type: Pricing
  url: https://triton.one/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.triton.one
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/rpcpool
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/triton-one
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/triton_one
- group: operate
  title: ''
  type: Support
  url: mailto:support@triton.one
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.triton.one/getting-started
- group: commercial
  title: ''
  type: TermsOfService
  url: https://triton.one/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://docs.triton.one/core-features/privacy-and-security
- group: operate
  title: ''
  type: RateLimits
  url: https://docs.triton.one/core-features/ratelimits
- group: auth
  title: ''
  type: Authentication
  url: https://docs.triton.one/account-management/api-access/auth-and-headers
- group: other
  title: ''
  type: Tiers
  url: https://docs.triton.one/account-management/api-access/rate-tiers
- group: build
  title: ''
  type: SDKs
  url: https://github.com/rpcpool/yellowstone-grpc
- group: build
  title: ''
  type: SDKs
  url: https://github.com/rpcpool/yellowstone-vixen
- group: build
  title: ''
  type: SDKs
  url: https://github.com/rpcpool/yellowstone-jet
- group: build
  title: ''
  type: SDKs
  url: https://github.com/rpcpool/yellowstone-fumarole
- group: build
  title: ''
  type: SDKs
  url: https://github.com/rpcpool/yellowstone-faithful
- group: build
  title: ''
  type: Tools
  url: https://github.com/rpcpool/solana-rpc-ansible
- group: commercial
  title: ''
  type: Plans
  url: https://plans/triton-one-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: https://rate-limits/triton-one-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: https://finops/triton-one-finops.yml
created: '2026-05-25'
description: Triton One is a high-performance Solana RPC and blockchain infrastructure provider operating globally distributed bare-metal node networks for Solana, Pythnet, Sui, and Monad. Beyond standard Solana JSON-RPC, Triton ships the Yellowstone ecosystem — Dragon's Mouth gRPC streaming, Whirligig WebSockets, Fumarole persistent streams, Old Faithful historical archive, Steamboat custom indexes, Vixen program parsing, Jet QUIC transaction sending, and Shield transaction policies — plus the hosted Metaplex Digital Assets API, Cascade SWQoS transaction delivery, and trading APIs (Pyth Hermes, Jito bundles, Metis, Titan). The Customers REST API at customers.triton.one programmatically manages accounts, subscriptions, endpoints, tokens, address watch lists, and rate tiers. Pricing is a single unified pay-as-you-go model with a $125 prepaid deposit and no tier gating.
features:
- Global bare-metal node network across 10+ tier-one data centers with GeoDNS routing and auto-failover
- Multi-chain coverage Solana, Pythnet (1,700+ price feeds), Sui, and Monad
- Three subscription types Developer (devnet/testnet), Mainnet-Shared, and Mainnet-Dedicated
- Five rate tiers free, tier1, tier2, tier3, and dedi (dedicated)
- Yellowstone Dragon's Mouth gRPC streaming for slots/blocks/transactions/accounts/blockmeta
- Whirligig WebSocket with transactionSubscribe — the missing Solana subscription
- Fumarole persistent streams with gap-free reconnect and 4-day cache
- Old Faithful complete-ledger archive queryable in milliseconds from genesis
- Submillisecond reads from head cache for recent history
- Steamboat custom indexes built automatically from query patterns
- Vixen Solana program parsing toolkit with Codama parser generation
- getTransactionsForAddress — single-call consolidated address history with slot/blockTime/status/tokenAccounts filters
- Improved getRecentPrioritizationFees with percentile parameter (1-10000)
- Cascade transaction delivery with Stake-Weighted Quality of Service routing
- Shield on-chain transaction policy enforcement
- Metaplex Digital Assets API hosted via the Photon indexer
- Trading APIs Pyth Hermes, Jito bundle simulation, Metis Swap, Titan Swap, Titan Prime
- Validator services vote account setup, node identity protection, NGINX proxy guidance
- Customers REST API at customers.triton.one for accounts, subscriptions, endpoints, tokens, watch lists
- Token-scoped role model reseller, operator, read-only
- Address watch lists for collections and Merkle trees
- Unified PAYG pricing — no tiers, no feature gating, no overage premiums
- $125 USD minimum prepaid deposit valid for 12 months
- $0.08/GB bandwidth across all services
- 1-1 senior engineer support included on every account
- Open-source Yellowstone components on github.com/rpcpool under AGPL-3.0 / Apache-2.0 / MIT
finops:
- name: Triton One Finops
  service_category: ''
  slug: triton-one-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/triton-one.png
json_schemas:
- name: Triton One Account
  property_count: 13
  slug: triton-one-account
- name: Triton One RPC Endpoint
  property_count: 7
  slug: triton-one-endpoint
- name: Triton One Subscription
  property_count: 8
  slug: triton-one-subscription
- name: Triton One RPC Token
  property_count: 7
  slug: triton-one-token
jsonld:
- class_count: 30
  name: Triton One Context
  property_count: 0
  slug: triton-one-context
layout: provider
modified: '2026-05-25'
name: Triton One
nav: Providers
network: true
overview: 'Triton One publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, AddressWatchLists API, Assets API, and 4 more. Tagged areas include Solana, RPC, Blockchain, Web3, and Streaming.


  The Triton One catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Triton One''s developer surface includes authentication, developer portal, documentation, pricing, support, getting-started guide, tooling, and 20 more developer resources.'
plans:
- name: Triton One Plans Pricing
  plan_count: 1
  slug: triton-one-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 0
  name: Triton One Rate Limits
  slug: triton-one-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Triton One API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: triton-one-jsonschema-spectral-rules
score:
  band: developing
  composite: 49.4
  coverage:
    artifact_dirs: 13
    catalog_gap: 47.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 9.8
    contract_quality: 66.3
    developer_ergonomics: 69.0
    discoverability: 64.8
    governance: 9.8
    operational_transparency: 10.5
  previous_composite: 49.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/triton-one/refs/heads/main/screenshots/triton-one-2026-06-20T195737.png
security:
- kind: authentication
  name: Triton One Authentication
  slug: triton-one-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Triton One Domain Security
  slug: triton-one-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: triton-one
tags:
- Solana
- RPC
- Blockchain
- Web3
- Streaming
- Yellowstone
- Validator
- gRPC
- Pythnet
- Sui
- Monad
website: https://triton.one
---
