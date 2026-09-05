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
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.3
  scored_at: '2026-09-04'
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
  name: DFlow admin API
  slug: dflow-admin-api
- baseURL: https://quote-api.dflow.net
  baseurl_source: declared
  description: Intent trading endpoints
  name: DFlow intent API
  slug: dflow-intent-api
- baseURL: https://quote-api.dflow.net
  baseurl_source: declared
  description: Order API endpoints
  name: DFlow order API
  slug: dflow-order-api
- baseURL: https://quote-api.dflow.net
  baseurl_source: declared
  description: Prediction market endpoints
  name: DFlow prediction_market API
  slug: dflow-prediction-market-api
- baseURL: https://quote-api.dflow.net
  baseurl_source: declared
  description: Swap API endpoints
  name: DFlow swap API
  slug: dflow-swap-api
- baseURL: https://quote-api.dflow.net
  baseurl_source: declared
  description: Token endpoints
  name: DFlow tokens API
  slug: dflow-tokens-api
- baseURL: https://quote-api.dflow.net
  baseurl_source: declared
  description: Venue endpoints
  name: DFlow venues API
  slug: dflow-venues-api
artifact_total: 20
asyncapis:
- description: DERIVED event surface for the DFlow Trading API real-time WebSocket streams. Modeled by API Evangelist from the published DFlow docs (https://pond.dflow.net/resources/trading-api/websockets/overview a
  name: DFlow Trading API WebSocket Streams
  slug: dflow-trading-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
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
- group: other
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
  title: ''
  type: LLMsTxt
  url: llms/dflow-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/dflow-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/dflow-spot-trading.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/dflow-platform-fees.md
- group: build
  title: ''
  type: CLI
  url: cli/dflow-cli.yml
- group: build
  title: ''
  type: Packages
  url: packages/dflow-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/dflow-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/dflow-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/dflow-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/dflow-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/dflow-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/dflow-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/dflow-data-model.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/dflow-agentic-access.yml
- group: auth
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
modified: '2026-07-18'
name: DFlow
nav: Providers
network: true
overview: 'DFlow publishes 7 APIs on the [APIs.io](https://apis.io/) network, including admin API, intent API, order API, and 4 more. Tagged areas include Company, Crypto Web3, Solana, Trading API, and DeFi.


  The DFlow catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  DFlow''s developer surface includes documentation, API reference, getting-started guide, support, signup flow, CLI, authentication, and 17 more developer resources.'
random_paper: 15
score:
  band: developing
  composite: 39.5
  coverage:
    artifact_dirs: 20
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 4.5
    contract_quality: 56.7
    developer_ergonomics: 76.2
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 2.6
  previous_composite: 39.5
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
    score: 28.3
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dflow/refs/heads/main/screenshots/dflow-2026-07-25T211845.png
security:
- kind: authentication
  name: Dflow Authentication
  slug: dflow-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Dflow Domain Security
  slug: dflow-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: dflow
tags:
- Company
- Crypto Web3
- Solana
- Trading API
- DeFi
- DEX Aggregator
- Token Swap
- Blockchain
- MEV Protection
- Prediction Markets
- Agent Ready
website: https://dflow.net
---
