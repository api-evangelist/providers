---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.6
  scored_at: '2026-08-24'
api_count: 1
apis:
- description: Ethereum-compatible JSON-RPC 2.0 API for the ZKsync Era ZK rollup. Standard eth_* methods plus the ZKsync-specific zks_* namespace (batches, bridging, fee estimation, proofs) over HTTPS POST, with a W
  name: ZKsync Era JSON-RPC API
  slug: zksync-era-json-rpc-api
artifact_total: 5
asyncapis:
- description: Generated from the ZKsync Era pub-sub JSON-RPC documentation. ZKsync Era supports the Ethereum-style eth_subscribe / eth_unsubscribe subscription model over WebSocket. This is a faithful description o
  name: ZKsync Era Pub/Sub (WebSocket) API
  slug: matter-labs-pubsub-asyncapi
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/matter-labs-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://matterlabs.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.zksync.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.zksync.io/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.zksync.io/zksync-protocol/api
- group: start
  title: ''
  type: Quickstart
  url: https://docs.zksync.io/zksync-network/quick-start/build-a-frontend
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/matter-labs
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.zksync.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.zksync.io/privacy
- group: build
  title: ''
  type: Packages
  url: packages/matter-labs-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/matter-labs-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/matter-labs-cli.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/matter-labs-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/matter-labs-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/matter-labs-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/matter-labs-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/matter-labs-lifecycle.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/matter-labs-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/matter-labs-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/matter-labs-llms.txt
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/matter-labs-pubsub-asyncapi.yml
created: '2026-07-17'
description: Matter Labs is the company behind ZKsync, a family of zero-knowledge (ZK) rollup Layer 2 scaling solutions for Ethereum. Its flagship network, ZKsync Era, is an EVM-compatible ZK rollup that inherits Ethereum security while offering low fees and high throughput. For developers ZKsync Era exposes a public, Ethereum-compatible JSON-RPC API (the standard eth_* namespace) extended with a ZKsync-specific zks_* namespace covering L1 batches, L1<->L2 bridging, fee and gas-per-pubdata estimation, token discovery, and Merkle proofs, plus a WebSocket pub/sub surface. First-party SDKs ship for JavaScript/TypeScript (zksync-ethers), Python (zksync2), and Go (zksync2-go), alongside a zksync-cli developer tool and native account-abstraction support. Matter Labs also builds the ZK Stack for launching sovereign ZK chains. The company is backed by a16z.
image: https://avatars.githubusercontent.com/matter-labs
layout: provider
mcp_servers:
- description: ''
  name: Matter Labs MCP Server
  slug: matter-labs-mcp-server
modified: '2026-07-20'
name: Matter Labs
nav: Providers
network: true
overview: 'Matter Labs publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Blockchain, Ethereum, Layer 2, and Zero-Knowledge Proofs.


  The Matter Labs catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Matter Labs'' developer surface includes documentation, API reference, quickstart, CLI, authentication, and 16 more developer resources.'
random_paper: 3
score:
  band: thin
  composite: 36.8
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 45.1
    developer_ergonomics: 64.3
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 2.6
  previous_composite: 36.8
  provenance:
    conformance: derived
    mcp: derived
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/matter-labs/refs/heads/main/screenshots/matter-labs-2026-07-25T230425.png
security:
- kind: authentication
  name: Matter Labs Authentication
  slug: matter-labs-authentication
  summary_line: none · 1 scheme
- kind: domain-security
  name: Matter Labs Domain Security
  slug: matter-labs-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: matter-labs
tags:
- Company
- Blockchain
- Ethereum
- Layer 2
- Zero-Knowledge Proofs
- Rollup
- JSON-RPC
- Web3
- Cryptography
- Scaling
website: https://matterlabs.com/
---
