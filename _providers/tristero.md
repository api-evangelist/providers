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
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.2
  scored_at: '2026-09-04'
api_count: 2
apis:
- baseURL: https://api.tristero.com/v2
  baseurl_source: declared
  description: The Assets API from Tristero — 1 operation(s) for assets.
  name: Tristero Assets API
  slug: tristero-assets-api
- baseURL: https://api.tristero.com/v2
  baseurl_source: declared
  description: Margin position management
  name: Tristero Margin API
  slug: tristero-margin-api
- baseURL: https://api.tristero.com/v2
  baseurl_source: declared
  description: Submit and manage orders
  name: Tristero Orders API
  slug: tristero-orders-api
- baseURL: https://api.tristero.com/v2
  baseurl_source: declared
  description: The Pricing API from Tristero — 1 operation(s) for pricing.
  name: Tristero Pricing API
  slug: tristero-pricing-api
- baseURL: https://api.tristero.com/v2
  baseurl_source: declared
  description: Request quotes for swaps and margin positions
  name: Tristero Quotes API
  slug: tristero-quotes-api
- baseURL: https://api.tristero.com/v2
  baseurl_source: declared
  description: The Trading API from Tristero — 2 operation(s) for trading.
  name: Tristero Trading API
  slug: tristero-trading-api
- baseURL: https://api.tristero.com/v2
  baseurl_source: declared
  description: Wallet and position queries
  name: Tristero Wallets API
  slug: tristero-wallets-api
artifact_total: 18
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Tristero Assets API
  slug: open-tristero-assets-api
- collection_type: open
  name: Tristero Assets Margin API
  slug: open-tristero-margin-api
- collection_type: open
  name: Tristero Assets Orders API
  slug: open-tristero-orders-api
- collection_type: open
  name: Tristero Assets Pricing API
  slug: open-tristero-pricing-api
- collection_type: open
  name: Tristero Assets Quotes API
  slug: open-tristero-quotes-api
- collection_type: open
  name: Tristero Assets Trading API
  slug: open-tristero-trading-api
- collection_type: open
  name: Tristero Assets Wallets API
  slug: open-tristero-wallets-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/tristero-api-overlay.yaml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tristero-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/tristero-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://tristero.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.tristero.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.tristero.com/docs/tristero
- group: docs
  title: ''
  type: APIReference
  url: https://docs.tristero.com/docs/tristero/api/getQuote
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.tristero.com/docs/feather/quickstart
- group: company
  title: ''
  type: Blog
  url: https://tristero.substack.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tristeroresearch
- group: start
  title: ''
  type: Login
  url: https://app.tristero.com
- group: operate
  title: ''
  type: Support
  url: mailto:outreach@tristero.com
- group: company
  title: ''
  type: Twitter
  url: https://x.com/0xtristero
- group: build
  title: ''
  type: Packages
  url: packages/tristero-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/tristero-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/tristero-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/tristero-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/tristero-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/tristero-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/tristero-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/tristero-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/tristero-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/tristero-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/tristero-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Tristero is a trustless, cross-chain trading protocol backed by General Catalyst. On-chain traders use its API and Python/TypeScript SDKs to access deep liquidity across DEXs and CEXs for spot swaps of ERC-20 tokens across EVM chains (via Permit2 / EIP-712 signed orders), leveraged margin positions up to 10x, and cross-VM swaps into non-EVM assets like Bitcoin, Monero, and Litecoin through its Feather balance-sheet swap relay. Execution is non-custodial and MEV-protected, with real-time quote streaming over WebSocket, and the company's research roots are in on-chain dark pools and encrypted order matching.
image: https://docs.tristero.com/tristero.png
layout: provider
mcp_servers:
- description: 'No official Tristero MCP server was found (no MCP mention in docs.tristero.com, no @tristero/* or tristero MCP package on npm, none of the tristeroresearch GitHub repos ship one). This is a CANDIDATE '
  name: Tristero MCP Server
  slug: tristero-mcp-server
modified: '2026-07-21'
name: Tristero
nav: Providers
network: true
overview: 'Tristero publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Assets API, Margin API, Orders API, and 4 more. Tagged areas include Company, Cryptocurrency, Trading, DeFi, and Cross-Chain.


  Tristero''s developer surface includes authentication, documentation, API reference, getting-started guide, engineering blog, support, sandbox, and 18 more developer resources.'
random_paper: 10
score:
  band: developing
  composite: 39.7
  coverage:
    artifact_dirs: 18
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
    contract_quality: 58.4
    developer_ergonomics: 73.2
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 5.3
  previous_composite: 39.7
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: weak_tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 28.3
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tristero/refs/heads/main/screenshots/tristero-2026-09-02T164259.png
security:
- kind: authentication
  name: Tristero Authentication
  slug: tristero-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Tristero Domain Security
  slug: tristero-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: tristero
tags:
- Company
- Cryptocurrency
- Trading
- DeFi
- Cross-Chain
- Web3
- Margin Trading
- Dark Pools
website: https://tristero.com
---
