---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: documented
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 50.5
  scored_at: '2026-08-06'
api_count: 4
apis:
- description: 'OpenAI- and Anthropic-compatible API gateway sitting in front of the entire 0G Compute Provider network. One endpoint and one API key reach every model: chat completions (streaming, tool calling, JSON'
  name: 0G Compute Router API
  slug: 0g-compute-router-api
- description: Ethereum-compatible JSON-RPC endpoint for the 0G Chain mainnet ("Aristotle", chain ID 16661), an AI-focused Layer 1 with sub-second finality. Standard EVM methods (eth_chainId, eth_call, eth_sendRawTr
  name: 0G Chain JSON-RPC
  slug: 0g-chain-json-rpc
- description: gRPC surface for the 0G data-availability layer. The Disperser service accepts blobs asynchronously (DisperseBlob), exposes polling for processing state (GetBlobStatus) and retrieval of a previously d
  name: 0G DA (Data Availability) gRPC
  slug: 0g-da-data-availability-grpc
- description: 'Indexer service for the 0G Storage network. It locates the storage nodes holding a file''s segments, brokers uploads and downloads addressed by Merkle root hash, and handles the on-chain Flow contract '
  name: 0G Storage Indexer
  slug: 0g-storage-indexer
artifact_total: 8
common:
- group: company
  title: ''
  type: Website
  url: https://0g.ai
- group: start
  title: ''
  type: DeveloperPortal
  url: https://build.0g.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.0g.ai
- group: docs
  title: ''
  type: APIReference
  url: https://0gfoundation.github.io/0g-router/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.0g.ai/developer-hub/getting-started
- group: operate
  title: ''
  type: Support
  url: https://discord.gg/0glabs
- group: company
  title: ''
  type: Blog
  url: https://0g.ai/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/0gfoundation
- group: operate
  title: ''
  type: StatusPage
  url: https://status.0g.ai
- group: start
  title: ''
  type: SignUp
  url: https://pc.0g.ai
- group: start
  title: ''
  type: Login
  url: https://pc.0g.ai
- group: commercial
  title: ''
  type: TermsOfService
  url: https://0g.ai/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://0g.ai/privacy-policy
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/0g-labs-llms.txt
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/0g-labs-router-openapi.yml
- group: build
  title: ''
  type: Packages
  url: packages/0g-labs-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/0g-labs-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/0g-labs-cli.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/0g-labs-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/0g-labs-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/0g-labs-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/0g-labs-rate-limits.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/0g-labs-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/0g-labs-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/0g-labs-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/0g-labs-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/0g-labs-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/0g-labs-sandbox.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/0g-labs-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/0g-labs-domain-security.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/0g-labs-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/0g-labs-tool-crosswalk.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/0g-labs-router-overlay.yaml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/0g-labs-changelog.yml
- group: design
  title: ''
  type: Components
  url: components/0g-labs-components.yml
- group: other
  title: ''
  type: Protobuf
  url: grpc/0g-labs-da-disperser.proto
- group: other
  title: ''
  type: Explorer
  url: https://chainscan.0g.ai
- group: other
  title: ''
  type: Faucet
  url: https://faucet.0g.ai
- group: other
  title: ''
  type: Whitepaper
  url: https://cdn.jsdelivr.net/gh/0glabs/0g-doc/static/whitepaper.pdf
created: '2026-08-05'
description: '0G Labs builds 0G (Zero Gravity), a decentralized AI operating system (deAIOS) that packages four modular layers into one stack: 0G Chain, an EVM-compatible Layer 1 with sub-second finality (mainnet "Aristotle", chain ID 16661); 0G Storage, a decentralized storage network for large AI datasets addressed by Merkle root hash and reachable through an indexer service, Go/TypeScript SDKs and a CLI; 0G DA, a data-availability layer using erasure coding and KZG commitments that OP Stack, Arbitrum Nitro and AVS rollups can settle against; and the 0G Compute Network, a decentralized GPU marketplace where every inference provider runs inside a TEE and attests to the model it serves. The developer-facing API is the 0G Compute Router at router-api.0g.ai — an OpenAI- and Anthropic-compatible gateway in front of the whole provider network, with a published OpenAPI 3.0 covering chat completions, the Anthropic messages shape, image generation and edits (sync and async), audio transcription,
  video generation, model and provider catalogs, routing preview, account balance and usage, and API-key management. Authentication splits into billable `sk-` API keys for inference and scope-limited `mk-` management keys for account and key administration.'
image: https://cdn.prod.website-files.com/680b884d38733122a923739b/68269581b10a2233094e3208_Group%201171275720.webp
layout: provider
mcp_servers:
- description: ''
  name: 0g-labs-mcp.yml
  slug: 0g-labs-mcpyml
modified: '2026-08-05'
name: 0G Labs
nav: Providers
network: true
overview: '0G Labs publishes 1 API on the [APIs.io](https://apis.io/) network: 0G Compute Router API. Tagged areas include artificial-intelligence, ai-inference, llm, gpu-compute, and decentralized-compute.


  0G Labs'' developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, CLI, and 33 more developer resources.'
random_paper: 49
rate_limits:
- limit_count: 0
  name: 0G Labs Rate Limits
  slug: 0g-labs-rate-limits
score:
  band: developing
  composite: 52.6
  facets:
    commercial_clarity: 34.2
    contract_quality: 56.6
    developer_ergonomics: 80.4
    discoverability: 83.3
    governance: 11.5
    operational_transparency: 44.7
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: first-party
  schema_version: 0.9.1
  scored_at: '2026-08-06'
security:
- kind: authentication
  name: 0G Labs Authentication
  slug: 0g-labs-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: 0G Labs Domain Security
  slug: 0g-labs-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: 0g-labs
tags:
- artificial-intelligence
- ai-inference
- llm
- gpu-compute
- decentralized-compute
- blockchain
- web3
- evm
- decentralized-storage
- data-availability
- openai-compatible
- trusted-execution-environment
- agent-native
- crypto-infrastructure
website: https://0g.ai
---
