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
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: na
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 34.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Orca Agentic Access
  operation_count: 11
  slug: orca-agentic-access
  summary_line: 11 operations
api_count: 1
apis:
- baseURL: https://api.orca.so/v2/solana
  baseurl_source: declared
  description: Orca protocol information endpoints
  name: Orca Protocol API
  slug: orca-protocol-api
- baseURL: https://api.orca.so/v2/solana
  baseurl_source: declared
  description: Token information endpoints
  name: Orca Tokens API
  slug: orca-tokens-api
- baseURL: https://api.orca.so/v2/solana
  baseurl_source: declared
  description: Whirlpool information endpoints
  name: Orca Whirlpools API
  slug: orca-whirlpools-api
arazzos:
- description: Search Orca Whirlpools for a token pair, then fetch full state for the top-matching pool. Read-only; runs against the open Orca Public REST API.
  name: Find an Orca pool by token pair and read its stats
  slug: orca-find-pool
artifact_total: 14
collections:
- collection_type: open
  name: Orca Public protocol API
  slug: open-orca-protocol-api
- collection_type: open
  name: Orca Public protocol tokens API
  slug: open-orca-tokens-api
- collection_type: open
  name: Orca Public protocol whirlpools API
  slug: open-orca-whirlpools-api
common:
- group: company
  title: ''
  type: BlogRSS
  url: https://blog.orca.so/rss/
- group: agent
  href: https://artifacts.apis.io/orca/agentic-access/orca-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/orca-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/orca/security/orca-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/orca-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://orca.so
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.orca.so/developers/overview
- group: docs
  title: ''
  type: Documentation
  url: https://docs.orca.so
- group: docs
  title: ''
  type: APIReference
  url: https://docs.orca.so/api-reference/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.orca.so/liquidity/getting-started/beginner-guide
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/orca-so
- group: operate
  title: ''
  type: Support
  url: https://docs.orca.so/support/faqs
- group: auth
  href: https://artifacts.apis.io/orca/authentication/orca-authentication.yml
  title: ''
  type: Authentication
  url: authentication/orca-authentication.yml
- group: build
  href: https://artifacts.apis.io/orca/packages/orca-packages.yml
  title: ''
  type: Packages
  url: packages/orca-packages.yml
- group: build
  href: https://artifacts.apis.io/orca/packages/orca-packages.yml
  title: ''
  type: SDKs
  url: packages/orca-packages.yml
- group: agent
  href: https://artifacts.apis.io/orca/mcp/orca-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/orca-mcp.yml
- group: agent
  href: https://artifacts.apis.io/orca/llms/orca-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/orca-llms.txt
- group: start
  href: https://artifacts.apis.io/orca/sandbox/orca-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/orca-sandbox.yml
- group: design
  href: https://artifacts.apis.io/orca/conventions/orca-conventions.yml
  title: ''
  type: Conventions
  url: conventions/orca-conventions.yml
- group: operate
  href: https://artifacts.apis.io/orca/changelog/orca-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/orca-changelog.yml
- group: design
  href: https://artifacts.apis.io/orca/lifecycle/orca-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/orca-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/orca/conformance/orca-conformance.yml
  title: ''
  type: Conformance
  url: conformance/orca-conformance.yml
- group: design
  href: https://artifacts.apis.io/orca/errors/orca-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/orca-problem-types.yml
- group: design
  href: https://artifacts.apis.io/orca/data-model/orca-data-model.yml
  title: ''
  type: DataModel
  url: data-model/orca-data-model.yml
- group: build
  href: https://artifacts.apis.io/orca/cli/orca-cli.yml
  title: ''
  type: CLI
  url: cli/orca-cli.yml
- group: other
  href: https://artifacts.apis.io/orca/overlays/orca-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/orca-openapi-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/orca/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/orca/arazzo/orca-find-pool.yml
  title: ''
  type: Arazzo
  url: arazzo/orca-find-pool.yml
created: '2026-07-17'
description: Orca is the leading user-friendly concentrated-liquidity automated market maker (AMM) on Solana, built around Whirlpools. Liquidity providers concentrate capital within custom price ranges for higher capital efficiency, traders swap tokens with dynamic Adaptive Fees, and creators launch tokens and lock liquidity for launches. Developers and autonomous agents integrate via the open Whirlpools SDKs (TypeScript, Rust, and a Python option) and the read-only Orca Public REST API (api.orca.so) for pool, token, lock, and protocol-wide data.
image: https://mintcdn.com/orca-ccf67c1f/K618mEucxJ6w73gh/logo/orca-logo.png
layout: provider
mcp_servers:
- description: Orca operates a live, hosted MCP (Model Context Protocol) server for native AI tool-use access to its documentation. No API key required; connect via any MCP-compatible client (Claude Desktop, Cursor,
  name: Orca MCP Server
  slug: orca-docs
modified: '2026-10-06'
name: Orca
nav: Providers
network: true
overview: 'Orca publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: Protocol API, Tokens API, and Whirlpools API. Tagged areas include Company, Defi Dex, DeFi, Decentralized Exchange, and Solana.


  The Orca catalog on APIs.io includes 1 Spectral governance ruleset.


  Orca''s developer surface includes documentation, API reference, getting-started guide, support, authentication, sandbox, changelog, and 19 more developer resources.'
random_paper: 13
rules:
- authorship: generated
  effective_rule_count: 94
  extends:
  - spectral:oas
  name: Orca API Rules
  rule_count: 53
  severity_counts:
    error: 43
    hint: 0
    info: 2
    warn: 8
  slug: orca-rules
score:
  band: thin
  composite: 37.7
  coverage:
    artifact_dirs: 26
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 58.5
    catalog_max: 100.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 18.2
    contract_quality: 44.5
    developer_ergonomics: 78.0
    discoverability: 71.7
    operational_transparency: 18.4
  previous_composite: 37.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 15.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/orca/orca-2026-08-07T190854.png
security:
- kind: authentication
  name: Orca Authentication
  slug: orca-authentication
  summary_line: none · 0 schemes
- kind: domain-security
  name: Orca Domain Security
  slug: orca-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 2
skills:
- name: Find and inspect an Orca liquidity pool
  slug: orca-find-pool
- name: Look up an Orca-listed token
  slug: orca-token-lookup
slug: orca
tags:
- Company
- Defi Dex
- DeFi
- Decentralized Exchange
- Solana
- AMM
- Liquidity
- Concentrated Liquidity
- Blockchain
- Cryptocurrency
website: https://orca.so
---
