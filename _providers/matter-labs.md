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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 17.3
  scored_at: '2026-09-25'
api_count: 1
apis:
- description: Ethereum-compatible JSON-RPC 2.0 API for the ZKsync Era ZK rollup. Standard eth_* methods plus the ZKsync-specific zks_* namespace (batches, bridging, fee estimation, proofs) over HTTPS POST, with a W
  name: ZKsync Era JSON-RPC API
  slug: zksync-era-json-rpc-api
artifact_total: 4
asyncapis:
- description: Generated from the ZKsync Era pub-sub JSON-RPC documentation. ZKsync Era supports the Ethereum-style eth_subscribe / eth_unsubscribe subscription model over WebSocket. This is a faithful description o
  name: ZKsync Era Pub/Sub (WebSocket) API
  slug: matter-labs-pubsub-asyncapi
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/matter-labs/refs/heads/main/security/matter-labs-domain-security.yml
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
  href: https://raw.githubusercontent.com/api-evangelist/matter-labs/refs/heads/main/packages/matter-labs-packages.yml
  title: ''
  type: Packages
  url: packages/matter-labs-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/matter-labs/refs/heads/main/packages/matter-labs-packages.yml
  title: ''
  type: SDKs
  url: packages/matter-labs-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/matter-labs/refs/heads/main/cli/matter-labs-cli.yml
  title: ''
  type: CLI
  url: cli/matter-labs-cli.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/matter-labs/refs/heads/main/authentication/matter-labs-authentication.yml
  title: ''
  type: Authentication
  url: authentication/matter-labs-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/matter-labs/refs/heads/main/conventions/matter-labs-conventions.yml
  title: ''
  type: Conventions
  url: conventions/matter-labs-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/matter-labs/refs/heads/main/conformance/matter-labs-conformance.yml
  title: ''
  type: Conformance
  url: conformance/matter-labs-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/matter-labs/refs/heads/main/errors/matter-labs-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/matter-labs-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/matter-labs/refs/heads/main/lifecycle/matter-labs-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/matter-labs-lifecycle.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/matter-labs/refs/heads/main/well-known/matter-labs-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/matter-labs-well-known.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/matter-labs/refs/heads/main/mcp/matter-labs-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/matter-labs-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/matter-labs/refs/heads/main/llms/matter-labs-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/matter-labs-llms.txt
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/matter-labs/refs/heads/main/asyncapi/matter-labs-pubsub-asyncapi.yml
  title: ''
  type: AsyncAPI
  url: asyncapi/matter-labs-pubsub-asyncapi.yml
created: '2026-07-17'
description: Matter Labs is the company behind ZKsync, a family of zero-knowledge (ZK) rollup Layer 2 scaling solutions for Ethereum. Its flagship network, ZKsync Era, is an EVM-compatible ZK rollup that inherits Ethereum security while offering low fees and high throughput. For developers ZKsync Era exposes a public, Ethereum-compatible JSON-RPC API (the standard eth_* namespace) extended with a ZKsync-specific zks_* namespace covering L1 batches, L1<->L2 bridging, fee and gas-per-pubdata estimation, token discovery, and Merkle proofs, plus a WebSocket pub/sub surface. First-party SDKs ship for JavaScript/TypeScript (zksync-ethers), Python (zksync2), and Go (zksync2-go), alongside a zksync-cli developer tool and native account-abstraction support. Matter Labs also builds the ZK Stack for launching sovereign ZK chains. The company is backed by a16z.
image: https://avatars.githubusercontent.com/matter-labs
layout: provider
modified: '2026-07-20'
name: Matter Labs
nav: Providers
network: true
overview: 'Matter Labs publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Blockchain, Ethereum, Layer 2, and Zero-Knowledge Proofs.


  The Matter Labs catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Matter Labs'' developer surface includes documentation, API reference, quickstart, CLI, authentication, and 16 more developer resources.'
random_paper: 16
score:
  band: thin
  composite: 36.4
  coverage:
    artifact_dirs: 14
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.5
  facets:
    access_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 39.0
    developer_ergonomics: 64.3
    discoverability: 73.2
    operational_transparency: 2.6
  previous_composite: 35.9
  provenance:
    conformance: derived
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
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
- Real-Time
website: https://matterlabs.com/
---
