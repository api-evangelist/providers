---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: documented
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-09-01'
api_count: 2
apis:
- description: Ethereum-compatible JSON-RPC endpoint for the 0G Chain mainnet ("Aristotle", chain ID 16661), an AI-focused Layer 1 with sub-second finality. Standard EVM methods (eth_chainId, eth_call, eth_sendRawTr
  name: 0G Chain JSON-RPC
  slug: 0g-chain-json-rpc
- description: gRPC surface for the 0G data-availability layer. The Disperser service accepts blobs asynchronously (DisperseBlob), exposes polling for processing state (GetBlobStatus) and retrieval of a previously d
  name: 0G DA (Data Availability) gRPC
  slug: 0g-da-data-availability-grpc
- description: 'Indexer service for the 0G Storage network. It locates the storage nodes holding a file''s segments, brokers uploads and downloads addressed by Merkle root hash, and handles the on-chain Flow contract '
  name: 0G Storage Indexer
  slug: 0g-storage-indexer
- description: The Account API from 0G Labs — 5 operation(s) for account.
  name: 0G Labs Account API
  slug: 0g-labs-account-api
- description: The API Key API from 0G Labs — 2 operation(s) for api key.
  name: 0G Labs API Key API
  slug: 0g-labs-api-key-api
- description: The Inference API from 0G Labs — 11 operation(s) for inference.
  name: 0G Labs Inference API
  slug: 0g-labs-inference-api
- description: The Models API from 0G Labs — 1 operation(s) for models.
  name: 0G Labs Models API
  slug: 0g-labs-models-api
- description: The Provider API from 0G Labs — 1 operation(s) for provider.
  name: 0G Labs Provider API
  slug: 0g-labs-provider-api
- description: The Service Types API from 0G Labs — 1 operation(s) for service types.
  name: 0G Labs Service Types API
  slug: 0g-labs-service-types-api
artifact_total: 20
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: 0G Router Account API
  slug: open-0g-labs-account-api
- collection_type: open
  name: 0G Router API Key API
  slug: open-0g-labs-api-key-api
- collection_type: open
  name: 0G Router Inference API
  slug: open-0g-labs-inference-api
- collection_type: open
  name: 0G Router Models API
  slug: open-0g-labs-models-api
- collection_type: open
  name: 0G Router Provider API
  slug: open-0g-labs-provider-api
- collection_type: open
  name: 0G Router Service Types API
  slug: open-0g-labs-service-types-api
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/0gfoundation/0g-da-client/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/0gfoundation/0g-da-client/releases
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/0gfoundation/0g-da-client/blob/main/contributing.md
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
  url: openapi/_original/0g-labs-router-openapi.yml
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
  name: 0G Labs MCP Server
  slug: 0g-labs-mcp-server
modified: '2026-08-05'
name: 0G Labs
nav: Providers
network: true
overview: '0G Labs publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Account API, API Key API, Inference API, and 3 more. Tagged areas include Artificial Intelligence, AI Inference, LLM, GPU Compute, and Decentralized Compute.


  0G Labs'' developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, CLI, and 36 more developer resources.'
random_paper: 5
rate_limits:
- limit_count: 0
  name: 0G Labs Rate Limits
  slug: 0g-labs-rate-limits
score:
  band: developing
  composite: 49.2
  coverage:
    artifact_dirs: 23
    catalog_gap: 83.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 4.5
    contract_quality: 50.0
    developer_ergonomics: 85.7
    discoverability: 66.7
    governance: 4.5
    operational_transparency: 42.1
  open_source:
    applies: true
    score: 50.0
  previous_composite: 49.2
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: derived
    skills: first-party
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/0g-labs/refs/heads/main/screenshots/0g-labs-2026-08-07T160641.png
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
- Artificial Intelligence
- AI Inference
- LLM
- GPU Compute
- Decentralized Compute
- Blockchain
- Web3
- EVM
- Decentralized Storage
- Data Availability
- OpenAI-Compatible
- Trusted Execution Environment
- agent-native
- Crypto Infrastructure
website: https://0g.ai
---
