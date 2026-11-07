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
  band: agent-aware
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
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: platform
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: false
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 28.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Dflow Agentic Access
  operation_count: 14
  slug: dflow-agentic-access
  summary_line: 14 operations · 3 acting
api_count: 1
apis:
- baseURL: https://quote-api.dflow.net
  baseurl_source: declared
  description: The admin API from DFlow — 1 operation(s) for admin.
  name: DFlow Admin API
  slug: dflow-admin-api
- baseURL: https://quote-api.dflow.net
  baseurl_source: declared
  description: Intent trading endpoints
  name: DFlow Intent API
  slug: dflow-intent-api
- baseURL: https://quote-api.dflow.net
  baseurl_source: declared
  description: Order API endpoints
  name: DFlow Order API
  slug: dflow-order-api
- baseURL: https://quote-api.dflow.net
  baseurl_source: declared
  description: Prediction market endpoints
  name: DFlow Prediction Market API
  slug: dflow-prediction-market-api
- baseURL: https://quote-api.dflow.net
  baseurl_source: declared
  description: Swap API endpoints
  name: DFlow Swap API
  slug: dflow-swap-api
- baseURL: https://quote-api.dflow.net
  baseurl_source: declared
  description: Token endpoints
  name: DFlow Tokens API
  slug: dflow-tokens-api
- baseURL: https://quote-api.dflow.net
  baseurl_source: declared
  description: Venue endpoints
  name: DFlow Venues API
  slug: dflow-venues-api
artifact_total: 22
asyncapis:
- description: DERIVED event surface for the DFlow Trading API real-time WebSocket streams. Modeled by API Evangelist from the published DFlow docs (https://pond.dflow.net/resources/trading-api/websockets/overview a
  name: DFlow Trading API WebSocket Streams
  slug: dflow-trading-asyncapi
collections:
- collection_type: open
  name: DFlow Aggregator admin API
  slug: open-dflow-admin-api
- collection_type: open
  name: DFlow Aggregator admin intent API
  slug: open-dflow-intent-api
- collection_type: open
  name: DFlow Aggregator admin order API
  slug: open-dflow-order-api
- collection_type: open
  name: DFlow Aggregator admin prediction_market API
  slug: open-dflow-prediction-market-api
- collection_type: open
  name: DFlow Aggregator admin swap API
  slug: open-dflow-swap-api
- collection_type: open
  name: DFlow Aggregator admin tokens API
  slug: open-dflow-tokens-api
- collection_type: open
  name: DFlow Aggregator admin venues API
  slug: open-dflow-venues-api
common:
- group: company
  title: ''
  type: Blog
  url: https://dflow.net/blog/
- group: other
  href: https://artifacts.apis.io/dflow/overlays/dflow-aggregator-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/dflow-aggregator-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://dflow.net
- group: start
  title: ''
  type: DeveloperPortal
  url: https://pond.dflow.net
- group: docs
  title: ''
  type: Documentation
  url: https://pond.dflow.net/resources/introduction
- group: docs
  title: ''
  type: APIReference
  url: https://pond.dflow.net/resources/trading-api/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://pond.dflow.net/get-started/what-is-dflow
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/DFlowProtocol
- group: operate
  title: ''
  type: Support
  url: https://t.me/+GubbVyulzDFjZTkx
- group: start
  title: ''
  type: SignUp
  url: https://forms.gle/eX3cghbMF8VBB9qa9
- group: agent
  href: https://artifacts.apis.io/dflow/llms/dflow-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dflow-llms.txt
- group: agent
  href: https://artifacts.apis.io/dflow/mcp/dflow-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/dflow-mcp.yml
- group: agent
  href: https://artifacts.apis.io/dflow/skills/dflow-spot-trading.md
  title: ''
  type: AgentSkill
  url: skills/dflow-spot-trading.md
- group: agent
  href: https://artifacts.apis.io/dflow/skills/dflow-platform-fees.md
  title: ''
  type: AgentSkill
  url: skills/dflow-platform-fees.md
- group: build
  href: https://artifacts.apis.io/dflow/cli/dflow-cli.yml
  title: ''
  type: CLI
  url: cli/dflow-cli.yml
- group: build
  href: https://artifacts.apis.io/dflow/packages/dflow-packages.yml
  title: ''
  type: Packages
  url: packages/dflow-packages.yml
- group: auth
  href: https://artifacts.apis.io/dflow/authentication/dflow-authentication.yml
  title: ''
  type: Authentication
  url: authentication/dflow-authentication.yml
- group: design
  href: https://artifacts.apis.io/dflow/conventions/dflow-conventions.yml
  title: ''
  type: Conventions
  url: conventions/dflow-conventions.yml
- group: design
  href: https://artifacts.apis.io/dflow/errors/dflow-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/dflow-problem-types.yml
- group: design
  href: https://artifacts.apis.io/dflow/conformance/dflow-conformance.yml
  title: ''
  type: Conformance
  url: conformance/dflow-conformance.yml
- group: design
  href: https://artifacts.apis.io/dflow/lifecycle/dflow-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/dflow-lifecycle.yml
- group: start
  href: https://artifacts.apis.io/dflow/sandbox/dflow-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/dflow-sandbox.yml
- group: design
  href: https://artifacts.apis.io/dflow/data-model/dflow-data-model.yml
  title: ''
  type: DataModel
  url: data-model/dflow-data-model.yml
- group: agent
  href: https://artifacts.apis.io/dflow/agentic-access/dflow-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/dflow-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/dflow/security/dflow-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dflow-domain-security.yml
created: '2026-07-17'
description: 'DFlow is a trading protocol and aggregator for spot trading natively on Solana, offering a Trading API that powers tens of billions of dollars in transacted value for traders, applications, and financial institutions. It provides imperative and declarative (intent-based) swaps, JIT routing across liquidity venues, MEV / sandwich protection, priority-fee and slippage controls, builder platform-fee monetization (platformFeeBps), sponsored (gasless) swaps, WebSocket market-data streams (quotes, order-book depth, priority fees), and prediction-market initialization. DFlow is agent-native: a single-binary agent CLI with an encrypted local wallet, published Claude Code Skills, and a hosted documentation MCP server. Authentication is via an x-api-key header; REST responses can be cryptographically signed with ed25519 per RFC 9421. Backed by Multicoin Capital.'
image: https://dflow.net/og-image.png
layout: provider
mcp_servers:
- description: Hosted documentation MCP server. Gives AI tools (Claude, Claude Code, Cursor, VS Code, Windsurf) direct search access to DFlow's documentation, Trading API specs, code recipes, and FAQ library so they
  name: DFlow
  slug: dflow
modified: '2026-10-06'
name: DFlow
nav: Providers
network: true
overview: 'DFlow publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Admin API, Intent API, Order API, and 4 more. Tagged areas include Company, Web3, Solana, Trading API, and DeFi.


  The DFlow catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  DFlow''s developer surface includes engineering blog, documentation, API reference, getting-started guide, support, signup flow, CLI, and 18 more developer resources.'
random_paper: 12
rules:
- authorship: generated
  effective_rule_count: 98
  extends:
  - spectral:oas
  name: DFlow API Rules
  rule_count: 57
  severity_counts:
    error: 48
    hint: 0
    info: 3
    warn: 6
  slug: dflow-rules
score:
  band: developing
  composite: 40.0
  coverage:
    artifact_dirs: 25
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 13.2
    contract_governance: 18.2
    contract_quality: 52.3
    developer_ergonomics: 78.6
    discoverability: 75.0
    operational_transparency: 2.6
  previous_composite: 40.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: first-party
    skills: first-party
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
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/dflow/dflow-2026-07-25T211845.png
security:
- kind: authentication
  name: Dflow Authentication
  slug: dflow-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Dflow Domain Security
  slug: dflow-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 2
skills:
- name: dflow-platform-fees
  slug: dflow-platform-fees
- name: dflow-spot-trading
  slug: dflow-spot-trading
slug: dflow
tags:
- Company
- Web3
- Solana
- Trading API
- DeFi
- DEX Aggregator
- Token Swap
- Blockchain
- MEV Protection
- Prediction Markets
- Agent Ready
- Real-Time
- Cryptocurrency
website: https://dflow.net
---
