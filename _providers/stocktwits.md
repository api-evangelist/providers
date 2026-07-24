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
  band: agent-native
  dimensions:
    agent_skills: true
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.1
  score: 69.2
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 11
  human_in_the_loop: 0
  name: Stocktwits Agentic Access
  operation_count: 31
  slug: stocktwits-agentic-access
  summary_line: 31 operations · 11 acting
api_count: 9
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
artifact_total: 14
common:
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/stocktwits-openapi-original.json
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
  name: stocktwits-mcp.yml
  slug: stocktwits-mcpyml
modified: '2026-07-21'
name: StockTwits
nav: Providers
network: true
overview: 'StockTwits publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Account API, Deletions API, Friendships API, and 6 more. Tagged areas include Company, Fintech, Social, Stocks, and Trading.


  StockTwits'' developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, signup flow, and 22 more developer resources.'
random_paper: 48
scopes:
- name: Stocktwits Scopes
  scope_count: 6
  slug: stocktwits-scopes
  summary_line: 6 scopes · authorizationCode
score:
  band: developing
  composite: 49.8
  delta: 4.7
  facets:
    commercial_clarity: 34.2
    contract_quality: 56.4
    developer_ergonomics: 67.4
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 45.1
  regulatory:
    applies: true
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 76.1
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
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
- Watchlists
- Messaging
website: https://stocktwits.com
---
