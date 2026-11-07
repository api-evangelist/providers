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
  - scopes
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: derived
    mcp_server: platform
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 45.2
  scored_at: '2026-11-06'
api_count: 4
apis:
- description: A remote Model Context Protocol endpoint published on aeternity.com and advertised through RFC 9728 protected-resource metadata and RFC 8414 authorization-server metadata. The endpoint is OAuth 2.1 ga
  name: Aeternity MCP Server
  slug: aeternity-mcp-server
- baseURL: https://mainnet.aeternity.io/v3
  baseurl_source: declared
  description: The Accounts API from Aeternity — 7 operation(s) for accounts.
  name: Aeternity Accounts API
  slug: aeternity-accounts-api
- baseURL: https://mainnet.aeternity.io/v3
  baseurl_source: declared
  description: The Aex141 API from Aeternity — 7 operation(s) for aex141.
  name: Aeternity Aex141 API
  slug: aeternity-aex141-api
- baseURL: https://mainnet.aeternity.io/v3
  baseurl_source: declared
  description: The Aex9 API from Aeternity — 6 operation(s) for aex9.
  name: Aeternity Aex9 API
  slug: aeternity-aex9-api
- baseURL: https://mainnet.aeternity.io/v3
  baseurl_source: declared
  description: The Channels API from Aeternity — 2 operation(s) for channels.
  name: Aeternity Channels API
  slug: aeternity-channels-api
- baseURL: https://mainnet.aeternity.io/v3
  baseurl_source: declared
  description: The Contracts API from Aeternity — 3 operation(s) for contracts.
  name: Aeternity Contracts API
  slug: aeternity-contracts-api
- baseURL: https://mainnet.aeternity.io/v3
  baseurl_source: declared
  description: The Dex API from Aeternity — 2 operation(s) for dex.
  name: Aeternity Dex API
  slug: aeternity-dex-api
- baseURL: https://mainnet.aeternity.io/v3
  baseurl_source: declared
  description: External API
  name: Aeternity External API
  slug: aeternity-external-api
- baseURL: https://mainnet.aeternity.io/v3
  baseurl_source: declared
  description: The Hyperchain API from Aeternity — 8 operation(s) for hyperchain.
  name: Aeternity Hyperchain API
  slug: aeternity-hyperchain-api
- baseURL: https://mainnet.aeternity.io/v3
  baseurl_source: declared
  description: Internal API
  name: Aeternity Internal API
  slug: aeternity-internal-api
- baseURL: https://mainnet.aeternity.io/v3
  baseurl_source: declared
  description: The Key Blocks API from Aeternity — 3 operation(s) for key blocks.
  name: Aeternity Key Blocks API
  slug: aeternity-key-blocks-api
- baseURL: https://mainnet.aeternity.io/v3
  baseurl_source: declared
  description: The Micro Blocks API from Aeternity — 2 operation(s) for micro blocks.
  name: Aeternity Micro Blocks API
  slug: aeternity-micro-blocks-api
- baseURL: https://mainnet.aeternity.io/v3
  baseurl_source: declared
  description: The Names API from Aeternity — 9 operation(s) for names.
  name: Aeternity Names API
  slug: aeternity-names-api
- baseURL: https://mainnet.aeternity.io/v3
  baseurl_source: declared
  description: The Oracles API from Aeternity — 5 operation(s) for oracles.
  name: Aeternity Oracles API
  slug: aeternity-oracles-api
- baseURL: https://mainnet.aeternity.io/v3
  baseurl_source: declared
  description: The Stats API from Aeternity — 15 operation(s) for stats.
  name: Aeternity Stats API
  slug: aeternity-stats-api
- baseURL: https://mainnet.aeternity.io/v3
  baseurl_source: declared
  description: The Status API from Aeternity — 1 operation(s) for status.
  name: Aeternity Status API
  slug: aeternity-status-api
- baseURL: https://mainnet.aeternity.io/v3
  baseurl_source: declared
  description: The Transactions API from Aeternity — 5 operation(s) for transactions.
  name: Aeternity Transactions API
  slug: aeternity-transactions-api
- baseURL: https://mainnet.aeternity.io/v3
  baseurl_source: declared
  description: The Transfers API from Aeternity — 1 operation(s) for transfers.
  name: Aeternity Transfers API
  slug: aeternity-transfers-api
artifact_total: 31
asyncapis:
- description: The æternity middleware (ae_mdw) WebSocket subscription stream. Clients subscribe to chain events and receive an asynchronous notification each time one occurs. Every event is published TWICE — once w
  name: Aeternity Middleware WebSocket API
  slug: aeternity-middleware-websocket-asyncapi
common:
- group: company
  title: ''
  type: Website
  url: https://aeternity.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.aeternity.com/aeternity-developer-tools
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aeternity.com/
- group: docs
  title: ''
  type: APIReference
  url: https://api-docs.aeternity.io/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.aeternity.com/aeternity-developer-tools/quick-start-guide
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aeternity
- group: company
  title: ''
  type: Blog
  url: https://blog.aeternity.com/
- group: operate
  title: ''
  type: Support
  url: https://forum.aeternity.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aeternity.com/legal-privacy
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aeternity.com/legal-privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.aeternity.io/
- group: design
  href: https://artifacts.apis.io/aeternity/lifecycle/aeternity-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/aeternity-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/aeternity/changelog/aeternity-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/aeternity-changelog.yml
- group: build
  href: https://artifacts.apis.io/aeternity/packages/aeternity-packages.yml
  title: ''
  type: Packages
  url: packages/aeternity-packages.yml
- group: build
  href: https://artifacts.apis.io/aeternity/packages/aeternity-packages.yml
  title: ''
  type: SDKs
  url: packages/aeternity-packages.yml
- group: build
  href: https://artifacts.apis.io/aeternity/cli/aeternity-cli.yml
  title: ''
  type: CLI
  url: cli/aeternity-cli.yml
- group: start
  href: https://artifacts.apis.io/aeternity/sandbox/aeternity-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/aeternity-sandbox.yml
- group: agent
  href: https://artifacts.apis.io/aeternity/llms/aeternity-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aeternity-llms.txt
- group: agent
  href: https://artifacts.apis.io/aeternity/well-known/aeternity-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/aeternity-well-known.yml
- group: design
  href: https://artifacts.apis.io/aeternity/conformance/aeternity-conformance.yml
  title: ''
  type: Conformance
  url: conformance/aeternity-conformance.yml
- group: auth
  href: https://artifacts.apis.io/aeternity/security/aeternity-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aeternity-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/aeternity/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://artifacts.apis.io/aeternity/scopes/aeternity-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/aeternity-scopes.yml
- group: operate
  href: https://artifacts.apis.io/aeternity/rate-limits/aeternity-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/aeternity-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/aeternity/plans/aeternity-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/aeternity-plans-pricing.yml
- group: auth
  href: https://artifacts.apis.io/aeternity/authentication/aeternity-authentication.yml
  title: ''
  type: Authentication
  url: authentication/aeternity-authentication.yml
- group: design
  href: https://artifacts.apis.io/aeternity/conventions/aeternity-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/aeternity-conventions.yml
- group: design
  href: https://artifacts.apis.io/aeternity/conventions/aeternity-conventions.yml
  title: ''
  type: Conventions
  url: conventions/aeternity-conventions.yml
- group: design
  href: https://artifacts.apis.io/aeternity/errors/aeternity-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/aeternity-problem-types.yml
- group: design
  href: https://artifacts.apis.io/aeternity/data-model/aeternity-data-model.yml
  title: ''
  type: DataModel
  url: data-model/aeternity-data-model.yml
- group: agent
  href: https://artifacts.apis.io/aeternity/mcp/aeternity-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/aeternity-mcp.yml
- group: docs
  href: https://artifacts.apis.io/aeternity/asyncapi/aeternity-middleware-websocket-asyncapi.yml
  title: ''
  type: AsyncAPI
  url: asyncapi/aeternity-middleware-websocket-asyncapi.yml
- group: other
  href: https://artifacts.apis.io/aeternity/overlays/aeternity-node-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/aeternity-node-overlay.yaml
- group: other
  href: https://artifacts.apis.io/aeternity/overlays/aeternity-middleware-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/aeternity-middleware-overlay.yaml
created: '2026-09-12'
description: 'æternity is an open-source layer-1 blockchain platform, launched in 2018 and stewarded by the Aeternity Foundation, whose protocol ships two public, unauthenticated HTTP APIs: the æternity node API (OpenAPI 3.0, 79 operations across chain, transaction, account, contract, oracle, naming-system, state-channel and node-operator surfaces) and the æternity Middleware (ae_mdw) API (OpenAPI 3.0, 76 REST operations plus an open GraphQL endpoint with 85 query fields and a WebSocket subscription stream). The platform adds the Sophia smart-contract language, the FATE virtual machine, state channels, protocol-native oracles, the æternity Naming System (AENS) and Hyperchains, and is consumed through first-party JavaScript/TypeScript, CLI and calldata SDKs published to npm, plus the æScan explorer, ÆStudio IDE and Superhero wallet/DEX.'
finops:
- has_sources: true
  method: derived
  name: Aeternity Finops
  primary_unit: ''
  service_category: ''
  slug: aeternity-finops
  template: true
image: https://aeternity.com/wp-content/uploads/2022/05/aeternity-social-thumb.webp
layout: provider
mcp_servers:
- description: Remote MCP server at aeternity.com requiring OAuth.
  name: Aeternity MCP Server
  slug: aeternity-mcp-server
modified: '2026-09-12'
name: Aeternity
nav: Providers
network: true
overview: 'Aeternity publishes 18 API contracts indexed on the [APIs.io](https://apis.io/) network, including Accounts API, Aex141 API, Aex9 API, and 15 more. Tagged areas include Blockchain, Layer 1, Smart Contracts, Cryptocurrency, and Web3.


  The Aeternity catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Aeternity''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, changelog, CLI, and 27 more developer resources.'
plans:
- name: Aeternity Plans Pricing
  plan_count: 0
  slug: aeternity-plans-pricing
random_paper: 21
rate_limits:
- limit_count: 6
  name: Aeternity Rate Limits
  slug: aeternity-rate-limits
rules:
- authorship: generated
  effective_rule_count: 98
  extends:
  - spectral:oas
  name: Aeternity API Rules
  rule_count: 57
  severity_counts:
    error: 39
    hint: 0
    info: 3
    warn: 15
  slug: aeternity-rules
scopes:
- name: Aeternity Scopes
  scope_count: 1
  slug: aeternity-scopes
  summary_line: 1 scope · authorization_code
score:
  band: strong
  composite: 55.0
  coverage:
    artifact_dirs: 30
    catalog_earned: 56.5
    catalog_earned_first_party: 12.0
    catalog_gap: 58.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 55.1
    developer_ergonomics: 80.4
    discoverability: 80.0
    operational_transparency: 65.8
  previous_composite: 55.0
  provenance:
    conformance: derived
    contracts:
      callable: 88.2
      derived: 0
      marker_coverage: 0.0
      total: 17
    mcp: site-plugin
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 34.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/aeternity/aeternity-2026-10-11T093003.png
security:
- kind: authentication
  name: Aeternity Authentication
  slug: aeternity-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Aeternity Domain Security
  slug: aeternity-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 4
skills:
- name: aeternity-inspect-token-contract
  slug: aeternity-inspect-token-contract
- name: aeternity-read-account-history
  slug: aeternity-read-account-history
- name: aeternity-submit-transaction
  slug: aeternity-submit-transaction
- name: aeternity-watch-chain-events
  slug: aeternity-watch-chain-events
slug: aeternity
tags:
- Blockchain
- Layer 1
- Smart Contracts
- Cryptocurrency
- Web3
- Distributed Ledger
- Open Source
- GraphQL
- State Channels
- Oracle
- Naming System
- Developer Tools
- Real-Time
website: https://aeternity.com/
---
