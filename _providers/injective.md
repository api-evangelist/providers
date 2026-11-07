---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  - sandbox
  trial: false
  try_now: false
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
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 29.7
  scored_at: '2026-11-06'
api_count: 3
apis:
- description: High-throughput read/stream API over the Injective chain and exchange data, exposed via gRPC, gRPC-web, and REST plus a Chain Stream WebSocket. Provides accounts, auctions, spot and derivative markets
  name: Injective Indexer API
  slug: injective-indexer-api
- description: The Injective Chain LCD/REST + Tendermint RPC surface for querying chain state (bank, staking, governance, exchange, oracle, tokenfactory, peggy, permissions) and broadcasting transactions. Cosmos SDK
  name: Injective Chain API
  slug: injective-chain-api
- description: Injective provides blockchain and DeFi functionality via its platform. Documentation is available at https://docs.injective.network/. No machine‑readable API contract was found.
  name: Injective API
  slug: injective-api
artifact_total: 7
asyncapis:
- description: ''
  name: Injective Chain Stream Webhooks
  slug: injective-chain-stream-webhooks
common:
- group: auth
  href: https://artifacts.apis.io/injective/security/injective-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/injective-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://injective.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://injective.com/developers
- group: docs
  title: ''
  type: Documentation
  url: https://docs.injective.network/
- group: docs
  title: ''
  type: APIReference
  url: https://api.injective.network/swagger/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.injective.network/developers/index
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/InjectiveLabs
- group: company
  title: ''
  type: Blog
  url: https://injective.com/blog
- group: operate
  title: ''
  type: Support
  url: https://discord.com/invite/injective
- group: commercial
  title: ''
  type: TermsOfService
  url: https://injective.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://injective.com/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://injective.instatus.com/
- group: agent
  href: https://artifacts.apis.io/injective/llms/injective-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/injective-llms.txt
- group: build
  href: https://artifacts.apis.io/injective/packages/injective-packages.yml
  title: ''
  type: Packages
  url: packages/injective-packages.yml
- group: build
  href: https://artifacts.apis.io/injective/packages/injective-packages.yml
  title: ''
  type: SDKs
  url: packages/injective-packages.yml
- group: agent
  href: https://artifacts.apis.io/injective/mcp/injective-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/injective-mcp.yml
- group: agent
  href: https://artifacts.apis.io/injective/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  href: https://artifacts.apis.io/injective/cli/injective-cli.yml
  title: ''
  type: CLI
  url: cli/injective-cli.yml
- group: operate
  href: https://artifacts.apis.io/injective/changelog/injective-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/injective-changelog.yml
- group: design
  href: https://artifacts.apis.io/injective/lifecycle/injective-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/injective-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/injective/conformance/injective-conformance.yml
  title: ''
  type: Conformance
  url: conformance/injective-conformance.yml
- group: auth
  href: https://artifacts.apis.io/injective/authentication/injective-authentication.yml
  title: ''
  type: Authentication
  url: authentication/injective-authentication.yml
- group: design
  href: https://artifacts.apis.io/injective/errors/injective-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/injective-error-codes.yml
- group: design
  href: https://artifacts.apis.io/injective/conventions/injective-conventions.yml
  title: ''
  type: Conventions
  url: conventions/injective-conventions.yml
- group: design
  href: https://artifacts.apis.io/injective/asyncapi/injective-chain-stream-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/injective-chain-stream-webhooks.yml
- group: start
  href: https://artifacts.apis.io/injective/sandbox/injective-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/injective-sandbox.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://injective.com/dev
created: '2026-07-17'
description: Injective is a Layer 1 blockchain purpose-built for Web3 finance, enabling users, institutions, and AI agents to trade, tokenize, and transact on-chain with native financial primitives including an on-chain central-limit order book, derivatives (perpetuals, expiry and pre-launch futures, options), spot markets, real-world-asset tokenization, stablecoins, and near-zero-fee payments with instant finality. Developers integrate through the Injective Chain LCD/REST API, a high-throughput Indexer API (gRPC, gRPC-web, and REST), a Chain Stream WebSocket for real-time market and account events, first-party SDKs in TypeScript, Python, Go, Rust, and CosmWasm, the injectived CLI, an official Model Context Protocol (MCP) server, and a suite of packaged Agent Skills for AI-driven trading and integration.
image: https://github.com/InjectiveLabs.png
layout: provider
mcp_servers:
- description: Official Injective MCP server (InjectiveLabs/mcp-server) exposing 40+ tools that give AI agents trading and chain capabilities on Injective. Runs locally over the stdio MCP transport and connects to C
  name: Injective MCP Server
  slug: injective-mcp-server
modified: '2026-07-19'
name: Injective
nav: Providers
network: true
overview: 'Injective is listed with 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Cryptocurrency, Blockchain, DeFi, and Trading.


  The Injective catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Injective''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, CLI, changelog, and 20 more developer resources.'
random_paper: 1
score:
  band: developing
  composite: 41.4
  coverage:
    artifact_dirs: 20
    catalog_earned: 35.0
    catalog_earned_first_party: 0.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.6
  facets:
    access_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 39.0
    developer_ergonomics: 81.0
    discoverability: 68.3
    operational_transparency: 26.3
  previous_composite: 40.8
  provenance:
    conformance: derived
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 22.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/injective/injective-2026-07-25T222440.png
security:
- kind: authentication
  name: Injective Authentication
  slug: injective-authentication
  summary_line: none-public/signature-based-transactions · 4 schemes
- kind: domain-security
  name: Injective Domain Security
  slug: injective-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: injective
tags:
- Company
- Cryptocurrency
- Blockchain
- DeFi
- Trading
- Derivatives
- Web3
- Layer 1
- Cosmos
- Tokenization
- Payments
- AI Agents
- Finance
- Infrastructure
website: https://injective.com/
---
