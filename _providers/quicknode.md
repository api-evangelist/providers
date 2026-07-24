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
    asyncapi_events: true
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
  score: 53.8
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 13
  human_in_the_loop: 0
  name: Quicknode Agentic Access
  operation_count: 22
  slug: quicknode-agentic-access
  summary_line: 22 operations · 13 acting
api_count: 12
apis:
- description: Multi-chain JSON-RPC, REST, and gRPC endpoints across 77+ blockchains (Ethereum, Solana, Polygon, Arbitrum, Optimism, Base, Bitcoin, Aptos, Avalanche, BNB, etc.).
  name: QuickNode Core RPC API
  slug: core-rpc
- description: Event-driven webhook subscriptions with custom filtering for blockchain events.
  name: QuickNode Webhooks
  slug: webhooks
- description: Catalog of opt-in add-on APIs (NFT API, Token API, DeFi API, Functions, etc.) attached to a QuickNode endpoint.
  name: QuickNode Marketplace Add-ons
  slug: marketplace
- description: Serverless on-chain logic runtime for executing custom code triggered by Streams or HTTP.
  name: QuickNode Functions
  slug: functions
- description: Fetch account usage information including bandwidth and storage metrics.
  name: QuickNode Account API
  slug: quicknode-account-api
- description: Bulk-load operations against a database.
  name: QuickNode Batch API
  slug: quicknode-batch-api
- description: Manage key-value namespaces (databases).
  name: QuickNode Database API
  slug: quicknode-database-api
- description: Create and manage gateways for retrieving content from the IPFS network.
  name: QuickNode Gateway API
  slug: quicknode-gateway-api
- description: Read, write, and delete keys within a database.
  name: QuickNode Keys API
  slug: quicknode-keys-api
- description: Inspect Stream execution logs.
  name: QuickNode Logs API
  slug: quicknode-logs-api
- description: Pin, view, and manage pinned content to ensure its availability on the IPFS network.
  name: QuickNode Pinning API
  slug: quicknode-pinning-api
- description: Manage Streams definitions and lifecycle.
  name: QuickNode Streams API
  slug: quicknode-streams-api
artifact_total: 31
asyncapis:
- description: AsyncAPI definition for QuickNode WebSocket subscription endpoints across Ethereum (and EVM-compatible chains) and Solana. All subscriptions use the JSON-RPC 2.0 envelope. After a successful subscript
  name: QuickNode WebSocket Subscription API
  slug: quicknode-asyncapi
collections:
- collection_type: open
  name: QuickNode IPFS REST API
  slug: open-quicknode-ipfs
- collection_type: open
  name: QuickNode Key-Value Store REST API
  slug: open-quicknode-key-value-store
- collection_type: open
  name: QuickNode Streams REST API
  slug: open-quicknode-streams
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/quicknode-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/quicknode-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/quicknode-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/quicknode-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/quicknode-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/quiknode-labs
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/quicknode
- group: company
  title: ''
  type: Website
  url: https://www.quicknode.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/quicknode-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/quicknode-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/quicknode-finops.yml
created: '2026-05-08'
description: QuickNode is a multi-chain Web3 infrastructure provider supporting 77+ blockchains via JSON-RPC, REST, and gRPC. Core products include high-performance RPC nodes, Streams (real-time event streaming), Webhooks, IPFS, a Key-Value Store, and a Marketplace of add-ons.
finops:
- name: Quicknode Finops
  service_category: Web3
  slug: quicknode-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/quicknode.png
json_schemas:
- name: QuickNode Key-Value Record
  property_count: 5
  slug: quicknode-kv
- name: QuickNode IPFS Pin
  property_count: 6
  slug: quicknode-pin
- name: QuickNode Stream
  property_count: 8
  slug: quicknode-stream
json_structures:
- name: Quicknode Structure
  property_count: 0
  slug: quicknode-structure
jsonld:
- class_count: 5
  name: Quicknode Context
  property_count: 2
  slug: quicknode-context
layout: provider
modified: '2026-05-29'
name: QuickNode
nav: Providers
network: true
overview: 'QuickNode publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Core RPC API, Account API, Batch API, and 6 more. Tagged areas include Web3, Blockchain, RPC, Streams, and IPFS.


  The QuickNode catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 2 Spectral governance rulesets.


  QuickNode''s developer surface includes authentication and 10 more developer resources.'
plans:
- name: Quicknode Plans Pricing
  plan_count: 5
  slug: quicknode-plans-pricing
random_paper: 45
rate_limits:
- limit_count: 5
  name: Quicknode Rate Limits
  slug: quicknode-rate-limits
rules:
- name: QuickNode API Rules
  rule_count: 7
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 6
  slug: quicknode-asyncapi-spectral-rules
- name: QuickNode API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: quicknode-jsonschema-spectral-rules
score:
  band: developing
  composite: 46.9
  delta: 0.0
  facets:
    commercial_clarity: 47.4
    contract_quality: 69.7
    developer_ergonomics: 10.9
    discoverability: 67.5
    governance: 52.6
    operational_transparency: 36.8
  previous_composite: 46.9
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/quicknode/refs/heads/main/screenshots/quicknode-2026-06-20T192434.png
security:
- kind: authentication
  name: Quicknode Authentication
  slug: quicknode-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Quicknode Domain Security
  slug: quicknode-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Quicknode Vulnerability Disclosure
  slug: quicknode-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Quicknode Trust Center
  slug: quicknode-trust-center
  summary_line: trust center published
slug: quicknode
tags:
- Web3
- Blockchain
- RPC
- Streams
- IPFS
- Multi-chain
website: https://www.quicknode.com/
---
