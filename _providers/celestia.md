---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 35.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 10
  human_in_the_loop: 0
  name: Celestia Agentic Access
  operation_count: 10
  slug: celestia-agentic-access
  summary_line: 10 operations · 10 acting
api_count: 1
apis:
- baseURL: http://localhost:26658
  baseurl_source: spec
  description: JSON-RPC methods in the blob module of celestia-node. Submit blobs to one or more namespaces with blob.Submit, retrieve them by height with blob.Get and blob.GetAll, generate inclusion proofs with blo
  name: Celestia Node Blob API
  slug: celestia-blob-api
- baseURL: https://celestia.org
  baseurl_source: spec
  description: The Contact API from Celestia — 1 operation(s) for contact.
  name: Celestia Contact API
  slug: celestia-contact-api
- baseURL: https://celestia.org
  baseurl_source: spec
  description: The Health API from Celestia — 1 operation(s) for health.
  name: Celestia Health API
  slug: celestia-health-api
- baseURL: https://celestia.org
  baseurl_source: spec
  description: The Subscribe API from Celestia — 1 operation(s) for subscribe.
  name: Celestia Subscribe API
  slug: celestia-subscribe-api
artifact_total: 57
collections:
- collection_type: open
  name: Celestia Node Blob API
  slug: open-celestia-blob-api
- collection_type: open
  name: Celestia Node Blob Blobstream API
  slug: open-celestia-blobstream-api
- collection_type: open
  name: Celestia Node Blob DA API
  slug: open-celestia-da-api
- collection_type: open
  name: Celestia Node Blob DAS API
  slug: open-celestia-das-api
- collection_type: open
  name: Celestia Node Blob Fraud API
  slug: open-celestia-fraud-api
- collection_type: open
  name: Celestia Node Blob Header API
  slug: open-celestia-header-api
- collection_type: open
  name: Celestia Blob Node API
  slug: open-celestia-node-api
- collection_type: open
  name: Celestia Node Blob P2P API
  slug: open-celestia-p2p-api
- collection_type: open
  name: Celestia Node Blob Share API
  slug: open-celestia-share-api
- collection_type: open
  name: Celestia Node Blob State API
  slug: open-celestia-state-api
- collection_type: open
  name: Celestia Node Subscriptions
  slug: open-celestia-subscriptions-asyncapi
common:
- group: other
  href: https://artifacts.apis.io/celestia/overlays/celestia-header-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/celestia-header-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/celestia/overlays/celestia-da-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/celestia-da-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/celestia/overlays/celestia-share-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/celestia-share-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/celestia/overlays/celestia-state-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/celestia-state-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/celestia/overlays/celestia-das-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/celestia-das-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/celestia/overlays/celestia-fraud-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/celestia-fraud-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/celestia/overlays/celestia-node-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/celestia-node-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/celestia/overlays/celestia-blobstream-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/celestia-blobstream-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/celestia/overlays/celestia-p2-p-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/celestia-p2-p-api-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.celestia.org/
- group: agent
  href: https://artifacts.apis.io/celestia/agentic-access/celestia-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/celestia-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/celestia/security/celestia-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/celestia-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/celestia/authentication/celestia-authentication.yml
  title: ''
  type: Authentication
  url: authentication/celestia-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://celestia.org
- group: docs
  title: ''
  type: Documentation
  url: https://docs.celestia.org
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.celestia.org/learn/celestia-101/data-availability/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.celestia.org/build/quick-start
- group: company
  title: ''
  type: Blog
  url: https://blog.celestia.org
- group: operate
  title: ''
  type: Forums
  url: https://forum.celestia.org
- group: operate
  title: ''
  type: Forums
  url: https://discord.com/invite/YsnTPcSfWQ
- group: company
  title: ''
  type: Twitter
  url: https://x.com/CelestiaOrg
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/celestiaorg
- group: build
  title: ''
  type: SDKs
  url: https://github.com/celestiaorg/celestia-node
- group: build
  title: ''
  type: SDKs
  url: https://github.com/celestiaorg/celestia-app
- group: build
  title: ''
  type: SDKs
  url: https://github.com/celestiaorg/celestia-core
- group: build
  title: ''
  type: SDKs
  url: https://github.com/celestiaorg/celestia-openrpc
- group: build
  title: ''
  type: SDKs
  url: https://github.com/celestiaorg/celestia-ts
- group: build
  title: ''
  type: SDKs
  url: https://github.com/celestiaorg/celestia-node-client-rs
- group: build
  title: ''
  type: SDKs
  url: https://docs.rs/celestia-rpc
- group: build
  title: ''
  type: SDKs
  url: https://github.com/celestiaorg/lumina
- group: build
  title: ''
  type: Tools
  url: https://github.com/celestiaorg/nmt
- group: build
  title: ''
  type: Tools
  url: https://github.com/celestiaorg/rsmt2d
- group: build
  title: ''
  type: Tools
  url: https://github.com/celestiaorg/go-square
- group: build
  title: ''
  type: Tools
  url: https://github.com/celestiaorg/blobstream-contracts
- group: build
  title: ''
  type: Tools
  url: https://github.com/celestiaorg/orchestrator-relayer
- group: docs
  title: ''
  type: Specification
  url: https://github.com/celestiaorg/celestia-specs
- group: docs
  title: ''
  type: Specification
  url: https://github.com/celestiaorg/CIPs
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/celestiaorg/docs
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/celestiaorg/awesome-celestia
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/celestiaorg/networks
- group: build
  title: ''
  type: Tools
  url: https://github.com/celestiaorg/helm-charts
- group: commercial
  title: ''
  type: License
  url: https://www.apache.org/licenses/LICENSE-2.0
- group: docs
  title: ''
  type: APIReference
  url: https://docs.celestia.org/build/rpc/node-api/
- group: other
  href: https://artifacts.apis.io/celestia/openapi/celestia-node-api-openrpc.json
  title: ''
  type: OpenRPC
  url: openapi/celestia-node-api-openrpc.json
- group: agent
  href: https://artifacts.apis.io/celestia/well-known/celestia-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/celestia-well-known.yml
- group: other
  href: https://artifacts.apis.io/celestia/well-known/celestia-api-catalog.json
  title: ''
  type: APICatalog
  url: well-known/celestia-api-catalog.json
- group: agent
  href: https://artifacts.apis.io/celestia/llms/celestia-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/celestia-llms.txt
- group: agent
  href: https://artifacts.apis.io/celestia/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/celestia/mcp/celestia-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/celestia-mcp.yml
- group: build
  href: https://artifacts.apis.io/celestia/packages/celestia-packages.yml
  title: ''
  type: Packages
  url: packages/celestia-packages.yml
- group: design
  href: https://artifacts.apis.io/celestia/lifecycle/celestia-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/celestia-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.celestia.org
- group: operate
  href: https://artifacts.apis.io/celestia/lifecycle/celestia-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/celestia-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/celestia/changelog/celestia-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/celestia-changelog.yml
- group: design
  href: https://artifacts.apis.io/celestia/conventions/celestia-conventions.yml
  title: ''
  type: Conventions
  url: conventions/celestia-conventions.yml
- group: design
  href: https://artifacts.apis.io/celestia/errors/celestia-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/celestia-problem-types.yml
- group: design
  href: https://artifacts.apis.io/celestia/conformance/celestia-conformance.yml
  title: ''
  type: Conformance
  url: conformance/celestia-conformance.yml
- group: design
  href: https://artifacts.apis.io/celestia/data-model/celestia-data-model.yml
  title: ''
  type: DataModel
  url: data-model/celestia-data-model.yml
- group: commercial
  href: https://artifacts.apis.io/celestia/plans/celestia-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/celestia-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/celestia/rate-limits/celestia-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/celestia-rate-limits.yml
- group: build
  href: https://artifacts.apis.io/celestia/cli/celestia-cli.yml
  title: ''
  type: CLI
  url: cli/celestia-cli.yml
- group: start
  href: https://artifacts.apis.io/celestia/sandbox/celestia-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/celestia-sandbox.yml
- group: auth
  href: https://artifacts.apis.io/celestia/security/celestia-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/celestia-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/celestia/security/celestia-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/celestia-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/celestia/security/celestia-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/celestia-trust-center.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://celestia.org/tos/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://celestia.org/privacy/
- group: operate
  title: ''
  type: Support
  url: https://forum.celestia.org
- group: start
  title: ''
  type: GettingStarted
  url: https://celestia.org/get-started/
created: '2026-05-24T00:00:00.000Z'
description: Celestia is the first production modular data availability blockchain. It separates consensus and data availability from execution and settlement, letting rollups, sovereign chains, and other execution layers post their transaction data as blobs to Celestia under namespaces while running their own state machines. Light nodes use Data Availability Sampling and Namespaced Merkle Trees to verify availability without downloading full blocks, and the Blobstream / Blobstream X bridge attests Celestia data commitments on Ethereum and other EVM chains. The reference stack — celestia-app (consensus, Cosmos SDK + CometBFT) and celestia-node (DA bridge/full/ light nodes) — exposes a JSON-RPC API with nine modules (blob, header, share, state, das, fraud, p2p, node, da, blobstream), plus a modular DA interface used by Rollkit, Optimism Alt-DA, Arbitrum Nitro DAS, and other rollup frameworks.
examples:
- key_count: 4
  name: Celestia Blob Get Example
  slug: celestia-blob-get-example
- key_count: 4
  name: Celestia Blob Submit Example
  slug: celestia-blob-submit-example
- key_count: 4
  name: Celestia Da Submit Example
  slug: celestia-da-submit-example
- key_count: 4
  name: Celestia Header Getbyheight Example
  slug: celestia-header-getbyheight-example
- key_count: 4
  name: Celestia Share Getnamespacedata Example
  slug: celestia-share-getnamespacedata-example
- key_count: 4
  name: Celestia State Submitpayforblob Example
  slug: celestia-state-submitpayforblob-example
features:
- First production modular data availability layer; separates consensus + DA from execution and settlement
- Mainnet Beta launched October 2023; chain id celestia
- Mocha-4 public testnet and Arabica devnet for application developers
- PayForBlobs (MsgPayForBlobs) transactions for publishing namespaced blob data
- Namespaced Merkle Trees (NMT) so each rollup only downloads data for its namespace
- 2D Reed-Solomon erasure coding over the extended data square (EDS)
- Data Availability Sampling (DAS) lets light nodes verify availability without downloading full blocks
- Bridge, full, and light celestia-node modes
- JSON-RPC over HTTP (default :26658) with bearer-token auth and four permission scopes (public, read, write, admin)
- WebSocket subscriptions for blob.Subscribe, header.Subscribe, fraud.Subscribe
- Modular DA interface (da.*) compatible with Rollkit, Optimism Alt-DA, Arbitrum Nitro DAS, OP-Succinct, Kona, Hana
- celestia-app exposes Cosmos SDK gRPC (:9090), REST (:1317), and CometBFT RPC (:26657) for consensus-level queries
- Blobstream and Blobstream X bridge to Ethereum and EVM chains for cross-chain data root verification
- Lumina Rust+Wasm light node runs in the browser
- Funded by TIA staking and PayForBlobs gas fees; no central API key or commercial pricing tier
- Reference implementations in Go (celestia-node, celestia-app) and Rust (lumina, celestia-rpc)
- Apache-2.0 licensed across the celestia-node, celestia-app, celestia-core, and tooling repos
- Active CIP (Celestia Improvement Proposal) process for protocol governance
- Ecosystem rollups include Manta Pacific, Eclipse, Movement, Lightlink, Polygon CDK Validium, Astria, Hyperliquid (DA usage), and many more
finops:
- has_sources: true
  method: derived
  name: Celestia Finops
  primary_unit: ''
  service_category: ''
  slug: celestia-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/celestia.png
json_schemas:
- name: Celestia Blob
  property_count: 6
  slug: celestia-blob
- name: Celestia Extended Header
  property_count: 4
  slug: celestia-extended-header
- name: Celestia Namespace
  property_count: 3
  slug: celestia-namespace
json_structures:
- name: Celestia Blob Structure
  property_count: 6
  slug: celestia-blob-structure
jsonld:
- class_count: 39
  name: Celestia Context
  property_count: 0
  slug: celestia-context
layout: provider
mcp_servers:
- description: Celestia publishes NO MCP server. Its own documentation llms.txt states so in as many words ("Celestia does not currently publish an official MCP server for this documentation site"), a GitHub code se
  name: Derived candidate only — Celestia publishes no MCP server
  slug: derived-candidate-only-celestia-publishes-no-mcp-server
modified: '2026-09-17'
name: Celestia
nav: Providers
network: true
overview: 'Celestia publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Node Blob API, Contact API, Health API, and 1 more. Tagged areas include Blockchain, Data Availability, Web3, Infrastructure, and Open Source.


  The Celestia catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Celestia''s developer surface includes authentication, developer portal, documentation, getting-started guide, engineering blog, tooling, code examples, and 62 more developer resources.'
plans:
- name: Celestia Plans Pricing
  plan_count: 0
  slug: celestia-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 4
  name: Celestia Rate Limits
  slug: celestia-rate-limits
rules:
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: Celestia — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: celestia-jsonschema-spectral-rules
- authorship: unmarked
  effective_rule_count: 45
  extends:
  - spectral:oas
  name: Celestia API Rules
  rule_count: 4
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 4
  slug: celestia-rules
score:
  band: strong
  composite: 64.5
  coverage:
    artifact_dirs: 34
    catalog_earned: 65.5
    catalog_earned_first_party: 12.0
    catalog_gap: 49.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.8
  facets:
    access_clarity: 28.9
    contract_governance: 31.8
    contract_quality: 63.3
    developer_ergonomics: 95.2
    discoverability: 64.3
    operational_transparency: 86.8
  previous_composite: 63.7
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 60.0
      total: 5
    mcp: derived
    skills: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 35.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/celestia/celestia-2026-06-20T174212.png
security:
- kind: authentication
  name: Celestia Authentication
  slug: celestia-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Celestia Domain Security
  slug: celestia-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Celestia Vulnerability Disclosure
  slug: celestia-vulnerability-disclosure
  summary_line: contact published
- kind: trust-center
  name: Celestia Trust Center
  slug: celestia-trust-center
  summary_line: trust center published
skill_count: 1
skills:
- name: celestia
  slug: celestia
slug: celestia
tags:
- Blockchain
- Data Availability
- Web3
- Infrastructure
- Open Source
- JSON-RPC
- Modular Blockchain
- Rollup
- Cryptography
- Developer Tools
website: https://www.celestia.org/
---
