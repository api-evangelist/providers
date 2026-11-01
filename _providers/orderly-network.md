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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: derived
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    operation_distinctiveness: mostly
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 28.6
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 66
  human_in_the_loop: 4
  name: Orderly Network Agentic Access
  operation_count: 248
  slug: orderly-network-agentic-access
  summary_line: 248 operations · 66 acting · 4 human-in-the-loop
api_count: 2
apis:
- baseURL: https://api.orderly.org
  baseurl_source: declared
  description: The admin API from Orderly Network — 1 operation(s) for admin.
  name: Orderly Network Admin API
  slug: orderly-network-admin-api
- baseURL: https://api.orderly.org
  baseurl_source: declared
  description: The client API from Orderly Network — 1 operation(s) for client.
  name: Orderly Network Client API
  slug: orderly-network-client-api
- baseURL: https://api.orderly.org
  baseurl_source: declared
  description: The private API from Orderly Network — 137 operation(s) for private.
  name: Orderly Network Private API
  slug: orderly-network-private-api
- baseURL: https://api.orderly.org
  baseurl_source: declared
  description: The public API from Orderly Network — 97 operation(s) for public.
  name: Orderly Network Public API
  slug: orderly-network-public-api
artifact_total: 16
asyncapis:
- description: Real-time WebSocket streams for Orderly Network. Public streams carry market data (orderbook, trades, ticker, klines); private streams carry authenticated account, balance, position, and execution-rep
  name: Orderly Network WebSocket API
  slug: orderly-network-websocket-asyncapi
collections:
- collection_type: open
  name: EVM admin API
  slug: open-orderly-network-admin-api
- collection_type: open
  name: EVM admin client API
  slug: open-orderly-network-client-api
- collection_type: open
  name: EVM admin private API
  slug: open-orderly-network-private-api
- collection_type: open
  name: EVM admin public API
  slug: open-orderly-network-public-api
common:
- group: other
  href: https://artifacts.apis.io/orderly-network/overlays/orderly-network-evm-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/orderly-network-evm-overlay.yaml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://orderly.network/docs/sdks/overview
- group: docs
  title: ''
  type: Documentation
  url: https://orderly.network/docs/introduction/getting-started/what-is-orderly
- group: docs
  title: ''
  type: APIReference
  url: https://orderly.network/docs/build-on-omnichain/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://orderly.network/docs/introduction/getting-started/builder-onboarding
- group: company
  title: ''
  type: Blog
  url: https://orderly.network/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/OrderlyNetwork
- group: operate
  title: ''
  type: Support
  url: https://discord.com/invite/OrderlyNetwork
- group: commercial
  title: ''
  type: TermsOfService
  url: https://orderly.network/docs/introduction/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://orderly.network/docs/introduction/privacy-policy
- group: agent
  href: https://artifacts.apis.io/orderly-network/llms/orderly-network-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/orderly-network-llms.txt
- group: build
  href: https://artifacts.apis.io/orderly-network/packages/orderly-network-packages.yml
  title: ''
  type: Packages
  url: packages/orderly-network-packages.yml
- group: build
  href: https://artifacts.apis.io/orderly-network/packages/orderly-network-packages.yml
  title: ''
  type: SDKs
  url: packages/orderly-network-packages.yml
- group: build
  href: https://artifacts.apis.io/orderly-network/cli/orderly-network-cli.yml
  title: ''
  type: CLI
  url: cli/orderly-network-cli.yml
- group: design
  href: https://artifacts.apis.io/orderly-network/components/orderly-network-components.yml
  title: ''
  type: Components
  url: components/orderly-network-components.yml
- group: agent
  href: https://artifacts.apis.io/orderly-network/mcp/orderly-network-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/orderly-network-mcp.yml
- group: agent
  href: https://artifacts.apis.io/orderly-network/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://artifacts.apis.io/orderly-network/authentication/orderly-network-authentication.yml
  title: ''
  type: Authentication
  url: authentication/orderly-network-authentication.yml
- group: design
  href: https://artifacts.apis.io/orderly-network/conventions/orderly-network-conventions.yml
  title: ''
  type: Conventions
  url: conventions/orderly-network-conventions.yml
- group: design
  href: https://artifacts.apis.io/orderly-network/errors/orderly-network-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/orderly-network-error-codes.yml
- group: design
  href: https://artifacts.apis.io/orderly-network/data-model/orderly-network-data-model.yml
  title: ''
  type: DataModel
  url: data-model/orderly-network-data-model.yml
- group: design
  href: https://artifacts.apis.io/orderly-network/conformance/orderly-network-conformance.yml
  title: ''
  type: Conformance
  url: conformance/orderly-network-conformance.yml
- group: design
  href: https://artifacts.apis.io/orderly-network/lifecycle/orderly-network-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/orderly-network-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/orderly-network/changelog/orderly-network-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/orderly-network-changelog.yml
- group: start
  href: https://artifacts.apis.io/orderly-network/sandbox/orderly-network-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/orderly-network-sandbox.yml
- group: docs
  href: https://artifacts.apis.io/orderly-network/asyncapi/orderly-network-websocket-asyncapi.yml
  title: ''
  type: AsyncAPI
  url: asyncapi/orderly-network-websocket-asyncapi.yml
- group: design
  href: https://artifacts.apis.io/orderly-network/asyncapi/orderly-network-websocket-asyncapi.yml
  title: ''
  type: Webhooks
  url: asyncapi/orderly-network-websocket-asyncapi.yml
- group: agent
  href: https://artifacts.apis.io/orderly-network/agentic-access/orderly-network-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/orderly-network-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/orderly-network/security/orderly-network-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/orderly-network-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://orderly.network/
created: '2026-07-17'
description: Orderly Network is an omnichain, orderbook-based trading infrastructure that provides perpetual-futures liquidity for decentralized exchanges and builders. It exposes a full EVM REST API and WebSocket streams for order management, account and sub-account handling, cross-chain deposits/withdrawals, positions, settlement, and market data, plus a Strategy Vault API and a zero-auth Public Info API aimed at AI agents and analytics. Authentication uses ed25519 request signing with registered Orderly Keys. Builders integrate via React component and hooks SDKs, a devkit CLI, a Builders Marketplace plugin system, and an official MCP server. Markets use the PERP_<TOKEN>_USDC symbol format across a public mainnet and testnet.
image: https://raw.githubusercontent.com/OrderlyNetwork/documentation-public/main/logo/light.svg
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.orderly.network; 10 tools listed.
  name: Orderly Network MCP Server
  slug: orderly
modified: '2026-07-20'
name: Orderly Network
nav: Providers
network: true
overview: 'Orderly Network publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Admin API, Client API, Private API, and 1 more. Tagged areas include Company, Cryptocurrency, DeFi, Trading, and Perpetual Futures.


  The Orderly Network catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Orderly Network''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, CLI, authentication, and 23 more developer resources.'
random_paper: 8
score:
  band: developing
  composite: 43.9
  coverage:
    artifact_dirs: 25
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 49.9
    developer_ergonomics: 80.4
    discoverability: 65.0
    operational_transparency: 28.9
  previous_composite: 43.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 23.1
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/orderly-network/orderly-network-2026-08-07T190918.png
security:
- kind: authentication
  name: Orderly Network Authentication
  slug: orderly-network-authentication
  summary_line: signature · 1 scheme
- kind: domain-security
  name: Orderly Network Domain Security
  slug: orderly-network-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 3
skills:
- name: Register an account and Orderly Key
  slug: orderly-network-account-onboarding
- name: Read market data and positions
  slug: orderly-network-market-data
- name: Place and manage a perpetual-futures order
  slug: orderly-network-place-and-manage-order
slug: orderly-network
tags:
- Company
- Cryptocurrency
- DeFi
- Trading
- Perpetual Futures
- Derivatives
- Order Book
- Web3
- Blockchain
- Liquidity
- Real-Time
website: https://orderly.network/
---
