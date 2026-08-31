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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.0
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 11
  human_in_the_loop: 0
  name: Stocktwits Agentic Access
  operation_count: 31
  slug: stocktwits-agentic-access
  summary_line: 31 operations · 11 acting
api_count: 1
apis:
- description: Account management endpoints for verifying and updating user profiles.
  name: StockTwits Account API
  slug: stocktwits-account-api
- description: Deletion tracking endpoints for finding messages and users that have been removed.
  name: StockTwits Deletions API
  slug: stocktwits-deletions-api
- description: Friendship management endpoints for following and unfollowing users.
  name: StockTwits Friendships API
  slug: stocktwits-friendships-api
- description: Social graph endpoints for viewing followers and following lists.
  name: StockTwits Graph (Social) API
  slug: stocktwits-graph-social-api
- description: Message endpoints for creating, viewing, liking, and managing individual messages (twits).
  name: StockTwits Messages API
  slug: stocktwits-messages-api
- description: Search endpoints for finding symbols and users on StockTwits.
  name: StockTwits Search API
  slug: stocktwits-search-api
- description: Stream endpoints return collections of messages (twits). Streams can be filtered by symbol, user, trending, etc.
  name: StockTwits Streams API
  slug: stocktwits-streams-api
- description: Trending endpoints return currently popular symbols based on message volume.
  name: StockTwits Trending API
  slug: stocktwits-trending-api
- description: Watchlist management endpoints for creating and managing symbol watchlists.
  name: StockTwits Watchlists API
  slug: stocktwits-watchlists-api
artifact_total: 24
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: StockTwits Account API
  slug: open-stocktwits-account-api
- collection_type: open
  name: StockTwits Account Deletions API
  slug: open-stocktwits-deletions-api
- collection_type: open
  name: StockTwits Account Friendships API
  slug: open-stocktwits-friendships-api
- collection_type: open
  name: StockTwits Account Graph (Social) API
  slug: open-stocktwits-graph-social-api
- collection_type: open
  name: StockTwits Account Messages API
  slug: open-stocktwits-messages-api
- collection_type: open
  name: StockTwits Account Search API
  slug: open-stocktwits-search-api
- collection_type: open
  name: StockTwits Account Streams API
  slug: open-stocktwits-streams-api
- collection_type: open
  name: StockTwits Account Trending API
  slug: open-stocktwits-trending-api
- collection_type: open
  name: StockTwits Account Watchlists API
  slug: open-stocktwits-watchlists-api
common:
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/stocktwits-openapi-original.json
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/stocktwits-agentic-access.yml
- group: build
  title: ''
  type: Packages
  url: packages/stocktwits-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/stocktwits-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/stocktwits-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/stocktwits-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/stocktwits-openapi-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/stocktwits-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/stocktwits-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/stocktwits-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/stocktwits-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/stocktwits-data-model.yml
- group: design
  title: ''
  type: Components
  url: components/stocktwits-components.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/stocktwits-domain-security.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/stocktwits-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/stocktwits-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://stocktwits.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.stocktwits.com/developers
- group: docs
  title: ''
  type: Documentation
  url: https://api.stocktwits.com/developers/docs
- group: docs
  title: ''
  type: APIReference
  url: https://api.stocktwits.com/developers/docs/api
- group: start
  title: ''
  type: GettingStarted
  url: https://api.stocktwits.com/developers
- group: operate
  title: ''
  type: Support
  url: https://help.stocktwits.com/
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.stocktwits.com/
- group: company
  title: ''
  type: Blog
  url: https://blog.stocktwits.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/stocktwits
- group: start
  title: ''
  type: SignUp
  url: https://stocktwits.com/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://stocktwits.com/about/legal/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://stocktwits.com/about/legal/privacy
created: '2026-07-17'
description: 'StockTwits is a social network for investors and traders, letting members share ideas (twits), follow tickers and people, build watchlists, and read real-time streams of market sentiment. The StockTwits API (v2) exposes this Social Finance graph over a REST/JSON interface at api.stocktwits.com/api/2: symbol/user/home/trending message streams, message create and like, symbol and user search, the social graph (followers/following), watchlist management, account verification, and deletion feeds. Authentication is OAuth 2.0 (authorization code) with app-level access tokens for public endpoints. StockTwits also publishes embeddable widgets, buttons, and message embeds for adding a Social Finance layer to any site. Sector: fintech; backed by Foundry Group.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/stocktwits.png
layout: provider
mcp_servers:
- description: ''
  name: StockTwits MCP Server
  slug: stocktwits-mcp-server
modified: '2026-07-21'
name: StockTwits
nav: Providers
network: true
overview: 'StockTwits publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Account API, Deletions API, Friendships API, and 6 more. Tagged areas include Company, Fintech, Social, Stocks, and Trading.


  StockTwits'' developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, signup flow, and 22 more developer resources.'
random_paper: 6
scopes:
- name: Stocktwits Scopes
  scope_count: 6
  slug: stocktwits-scopes
  summary_line: 6 scopes · authorizationCode
score:
  band: developing
  composite: 40.2
  coverage:
    artifact_dirs: 20
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.5
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 4.5
    contract_quality: 52.7
    developer_ergonomics: 41.1
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 2.6
  previous_composite: 40.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 58.3
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/stocktwits/refs/heads/main/screenshots/stocktwits-2026-08-17T082118.png
security:
- kind: authentication
  name: Stocktwits Authentication
  slug: stocktwits-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Stocktwits Domain Security
  slug: stocktwits-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: stocktwits
tags:
- Company
- Fintech
- Social
- Stocks
- Trading
- Investing
- Market Data
- Social Finance
- Watchlist
- Messaging
website: https://stocktwits.com
---
