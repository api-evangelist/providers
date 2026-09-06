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
  band: agent-aware
  dimensions:
    agent_card: flavored
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.3
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 13
  human_in_the_loop: 0
  name: Quicknode Agentic Access
  operation_count: 22
  slug: quicknode-agentic-access
  summary_line: 22 operations · 13 acting
api_count: 3
apis:
- baseURL: https://{endpoint-name}.{network}.quiknode.pro/{token}
  baseurl_source: declared
  description: Multi-chain JSON-RPC, REST, and gRPC endpoints across 77+ blockchains (Ethereum, Solana, Polygon, Arbitrum, Optimism, Base, Bitcoin, Aptos, Avalanche, BNB, etc.).
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
- baseURL: https://{endpoint-name}.{network}.quiknode.pro/{token}
  baseurl_source: declared
  description: Fetch account usage information including bandwidth and storage metrics.
  name: QuickNode Account API
  slug: quicknode-account-api
- baseURL: https://{endpoint-name}.{network}.quiknode.pro/{token}
  baseurl_source: declared
  description: Bulk-load operations against a database.
  name: QuickNode Batch API
  slug: quicknode-batch-api
- baseURL: https://{endpoint-name}.{network}.quiknode.pro/{token}
  baseurl_source: declared
  description: Manage key-value namespaces (databases).
  name: QuickNode Database API
  slug: quicknode-database-api
- baseURL: https://{endpoint-name}.{network}.quiknode.pro/{token}
  baseurl_source: declared
  description: Create and manage gateways for retrieving content from the IPFS network.
  name: QuickNode Gateway API
  slug: quicknode-gateway-api
- baseURL: https://{endpoint-name}.{network}.quiknode.pro/{token}
  baseurl_source: declared
  description: Read, write, and delete keys within a database.
  name: QuickNode Keys API
  slug: quicknode-keys-api
- baseURL: https://{endpoint-name}.{network}.quiknode.pro/{token}
  baseurl_source: declared
  description: Inspect Stream execution logs.
  name: QuickNode Logs API
  slug: quicknode-logs-api
- baseURL: https://{endpoint-name}.{network}.quiknode.pro/{token}
  baseurl_source: declared
  description: Pin, view, and manage pinned content to ensure its availability on the IPFS network.
  name: QuickNode Pinning API
  slug: quicknode-pinning-api
- baseURL: https://{endpoint-name}.{network}.quiknode.pro/{token}
  baseurl_source: declared
  description: Manage Streams definitions and lifecycle.
  name: QuickNode Streams API
  slug: quicknode-streams-api
artifact_total: 40
asyncapis:
- description: AsyncAPI definition for QuickNode WebSocket subscription endpoints across Ethereum (and EVM-compatible chains) and Solana. All subscriptions use the JSON-RPC 2.0 envelope. After a successful subscript
  name: QuickNode WebSocket Subscription API
  slug: quicknode-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: QuickNode IPFS REST Account API
  slug: open-quicknode-account-api
- collection_type: open
  name: QuickNode IPFS REST Account Batch API
  slug: open-quicknode-batch-api
- collection_type: open
  name: QuickNode IPFS REST Account Database API
  slug: open-quicknode-database-api
- collection_type: open
  name: QuickNode IPFS REST Account Gateway API
  slug: open-quicknode-gateway-api
- collection_type: open
  name: QuickNode IPFS REST API
  slug: open-quicknode-ipfs
- collection_type: open
  name: QuickNode Key-Value Store REST API
  slug: open-quicknode-key-value-store
- collection_type: open
  name: QuickNode IPFS REST Account Keys API
  slug: open-quicknode-keys-api
- collection_type: open
  name: QuickNode IPFS REST Account Logs API
  slug: open-quicknode-logs-api
- collection_type: open
  name: QuickNode IPFS REST Account Pinning API
  slug: open-quicknode-pinning-api
- collection_type: open
  name: QuickNode IPFS REST Account Streams API
  slug: open-quicknode-streams-api
- collection_type: open
  name: QuickNode Streams REST API
  slug: open-quicknode-streams
common:
- group: other
  title: ''
  type: AgentCard
  url: a2a/quicknode-a2a.yml
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
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
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


  QuickNode''s developer surface includes authentication and 11 more developer resources.'
plans:
- name: Quicknode Plans Pricing
  plan_count: 5
  slug: quicknode-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 5
  name: Quicknode Rate Limits
  slug: quicknode-rate-limits
rules:
- effective_rule_count: 34
  extends:
  - spectral:asyncapi
  name: QuickNode API Rules
  rule_count: 7
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 6
  slug: quicknode-asyncapi-spectral-rules
- effective_rule_count: 5
  extends: []
  name: QuickNode API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: quicknode-jsonschema-spectral-rules
score:
  band: thin
  composite: 34.1
  coverage:
    artifact_dirs: 17
    catalog_earned: 61.5
    catalog_earned_first_party: 0.0
    catalog_gap: 53.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 13.6
    contract_quality: 58.8
    developer_ergonomics: 21.4
    discoverability: 74.1
    governance: 13.6
    operational_transparency: 10.5
  previous_composite: 34.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.18.3
  scored_at: '2026-09-05'
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
- Multi-Chain
website: https://www.quicknode.com/
---
