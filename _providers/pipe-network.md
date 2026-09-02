---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
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
    agent_skills: derived
    agentic_access: false
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 6.3
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: 'Content-addressed decentralized object storage on Solana. Create users, upload/download files, resolve deterministic public URLs, and manage prepaid USDC credits. Auth is SIWS (Sign In With Solana -> '
  name: Pipe Storage (Firestarter) API
  slug: pipe-storage-firestarter-api
artifact_total: 4
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/PipeNetwork/lib-storage/issues
- group: commercial
  title: ''
  type: License
  url: https://github.com/PipeNetwork/lib-storage/blob/main/LICENSE
- group: company
  title: ''
  type: Website
  url: https://pipe.network
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/PipeNetwork
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/PipeNetwork/docs
- group: docs
  title: ''
  type: APIReference
  url: https://github.com/PipeNetwork/docs/blob/main/docs/cdn-api/api-documentation.md
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/PipeNetwork/lib-storage
- group: other
  title: ''
  type: X
  url: https://x.com/pipenetwork
- group: build
  title: ''
  type: Packages
  url: packages/pipe-network-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/pipe-network-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/pipe-network-cli.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/pipe-network-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/pipe-network-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/pipe-network-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/pipe-network-lifecycle.yml
- group: design
  title: ''
  type: Components
  url: components/pipe-network-components.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/pipe-network-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/pipe-network-data-model.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/pipe-network-problem-types.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/pipe-network-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/pipe-network-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pipe-network-domain-security.yml
created: '2026-07-17'
description: Pipe Network is a decentralized storage and content-delivery network built on Solana, marketed as "Firestarter" storage. It offers content-addressed (Blake3) object storage with client-side AES-256-GCM and post-quantum (Kyber-1024 / Dilithium5) encryption, deterministic public URLs of the form /{account}/{hash}, prepaid-USDC billing funded via Solana Pay, and first-party TypeScript / Python / Rust SDKs plus a Rust CLI. The SDKs ship native agent- framework tool adapters (OpenAI, Anthropic, LangChain, LlamaIndex, Vercel AI SDK, Cloudflare AI Workflows, AutoGen, CrewAI) and x402 machine-to-machine payment support. Backed by Multicoin Capital.
image: https://github.com/PipeNetwork.png
layout: provider
mcp_servers:
- description: ''
  name: Pipe Network MCP Server
  slug: pipe-network-mcp-server
modified: '2026-07-20'
name: Pipe Network
nav: Providers
network: true
overview: 'Pipe Network publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Crypto Web3, Storage, Decentralized Storage, and Content Delivery Network.


  Pipe Network''s developer surface includes documentation, API reference, CLI, authentication, changelog, and 18 more developer resources.'
random_paper: 14
score:
  band: emerging
  composite: 17.5
  coverage:
    artifact_dirs: 15
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 44.6
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 18.4
  open_source:
    applies: true
    score: 0.0
  previous_composite: 17.5
  provenance:
    conformance: derived
    mcp: derived
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: authentication
  name: Pipe Network Authentication
  slug: pipe-network-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Pipe Network Domain Security
  slug: pipe-network-domain-security
  summary_line: TLSv1.3 · DMARC
slug: pipe-network
tags:
- Company
- Crypto Web3
- Storage
- Decentralized Storage
- Content Delivery Network
- Solana
- Encryption
- AI Agents
- Web3
website: https://pipe.network
---
