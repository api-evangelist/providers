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
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 27.9
  scored_at: '2026-09-20'
api_count: 2
apis:
- description: High-performance proto3 gRPC API (with gRPC-Web for browsers) for the Thru blockchain. QueryService exposes 24 read operations over accounts, blocks, transactions, events, state proofs, and node statu
  name: Thru gRPC API
  slug: thru-grpc-api
- description: Official hosted Model Context Protocol server on the Thru block explorer. Exposes eight read-only tools (get_block, get_transaction, get_account, list_account_transactions, list_recent_blocks, list_re
  name: Thru Explorer MCP Server
  slug: thru-explorer-mcp-server
artifact_total: 5
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/unto-labs/refs/heads/main/security/unto-labs-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/unto-labs-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://untolabs.com/
- group: company
  title: ''
  type: ProductWebsite
  url: https://thru.org/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://thru.org/docs
- group: docs
  title: ''
  type: Documentation
  url: https://docs.thru.org
- group: start
  title: ''
  type: GettingStarted
  url: https://thru.org/docs/program-development/setting-up-thru-devkit
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Unto-Labs
- group: operate
  title: ''
  type: Support
  url: https://t.me/thruxyz
- group: other
  title: ''
  type: XAccount
  url: https://x.com/thru_xyz
- group: company
  title: ''
  type: Careers
  url: https://jobs.ashbyhq.com/unto-labs
- group: operate
  title: ''
  type: StatusPage
  url: https://status.thru.org
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/unto-labs/refs/heads/main/changelog/unto-labs-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/unto-labs-changelog.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/unto-labs/refs/heads/main/llms/unto-labs-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/unto-labs-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/unto-labs/refs/heads/main/mcp/unto-labs-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/unto-labs-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/unto-labs/refs/heads/main/packages/unto-labs-packages.yml
  title: ''
  type: Packages
  url: packages/unto-labs-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/unto-labs/refs/heads/main/packages/unto-labs-packages.yml
  title: ''
  type: SDKs
  url: packages/unto-labs-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/unto-labs/refs/heads/main/cli/unto-labs-cli.yml
  title: ''
  type: CLI
  url: cli/unto-labs-cli.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/unto-labs/refs/heads/main/errors/unto-labs-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/unto-labs-error-codes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/unto-labs/refs/heads/main/conventions/unto-labs-conventions.yml
  title: ''
  type: Conventions
  url: conventions/unto-labs-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/unto-labs/refs/heads/main/lifecycle/unto-labs-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/unto-labs-lifecycle.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/unto-labs/refs/heads/main/authentication/unto-labs-authentication.yml
  title: ''
  type: Authentication
  url: authentication/unto-labs-authentication.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/unto-labs/refs/heads/main/sandbox/unto-labs-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/unto-labs-sandbox.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/unto-labs/refs/heads/main/conformance/unto-labs-conformance.yml
  title: ''
  type: Conformance
  url: conformance/unto-labs-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/unto-labs/refs/heads/main/components/unto-labs-components.yml
  title: ''
  type: Components
  url: components/unto-labs-components.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/unto-labs/refs/heads/main/data-model/unto-labs-data-model.yml
  title: ''
  type: DataModel
  url: data-model/unto-labs-data-model.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/unto-labs/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Unto Labs is the team behind Thru, a high-performance Layer 1 blockchain for ultra-low-latency, ultra-high-throughput applications, built around ThruVM — a novel virtual machine targeting the RISC-V architecture so programs are written in plain C rather than crypto-specific languages. Founded in late 2024 by Jump Crypto / Solana alums and backed by Framework Ventures and Electric Capital, Unto Labs publishes a public gRPC and gRPC-Web API on the Thru Alphanet, protobuf definitions, C/Rust/TypeScript SDKs, a first-party CLI, a hosted Explorer MCP server for AI agents, llms.txt documentation sets, and installable agent skills.
image: https://github.com/Unto-Labs.png
layout: provider
mcp_servers:
- description: Official hosted MCP server on the Thru block explorer. Lets AI agents inspect blocks, transactions, accounts, recent activity, search results, and on-chain program ABIs with live chain context. Tool r
  name: Thru Explorer MCP
  slug: thru-explorer-mcp
modified: '2026-07-21'
name: Unto Labs
nav: Providers
network: true
overview: 'Unto Labs publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Crypto, Blockchain, Layer 1, and RISC-V.


  Unto Labs'' developer surface includes documentation, getting-started guide, support, changelog, CLI, authentication, sandbox, and 19 more developer resources.'
random_paper: 15
score:
  band: thin
  composite: 31.8
  coverage:
    artifact_dirs: 19
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 4.5
    contract_quality: 26.7
    developer_ergonomics: 62.5
    discoverability: 75.9
    operational_transparency: 34.2
  previous_composite: 31.8
  provenance:
    conformance: derived
    mcp: first-party
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-20'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/unto-labs/refs/heads/main/screenshots/unto-labs-2026-09-02T165002.png
security:
- kind: authentication
  name: Unto Labs Authentication
  slug: unto-labs-authentication
  summary_line: signature-based · 0 schemes
- kind: domain-security
  name: Unto Labs Domain Security
  slug: unto-labs-domain-security
  summary_line: TLSv1.3 · DMARC
slug: unto-labs
tags:
- Company
- Crypto
- Blockchain
- Layer 1
- RISC-V
- Virtual Machines
- gRPC
- Web3
- Infrastructure
website: https://untolabs.com/
---
