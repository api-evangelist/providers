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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 48.4
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Stockx Agentic Access
  operation_count: 32
  slug: stockx-agentic-access
  summary_line: 32 operations · 9 acting
api_count: 4
apis:
- description: Batch APIs enable a user to create, update, delete listings in bulk. Batch APIs are asynchronous in nature and we provide mechanisms to poll the API so that you can keep track of the batch completion.
  name: StockX Batch API
  slug: stockx-batch-api
- description: The StockX Catalog API provides a means for partners to search for catalog data, and request products to be added. Partners can search our Catalog to get StockX product and variant IDs for various pur
  name: StockX Catalog API
  slug: stockx-catalog-api
- description: Listings APIs enable a seller to programmatically sell on StockX. The APIs enable a user to create, update and delete listings on the marketplace, as well as view and fetch live market data for any li
  name: StockX Listings API
  slug: stockx-listings-api
- description: Order APIs enable a user to view all their active orders / sales as well as details for a single order.
  name: StockX Order API
  slug: stockx-order-api
artifact_total: 10
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.stockx.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.stockx.com/portal/api-introduction
- group: docs
  title: ''
  type: APIReference
  url: https://developer.stockx.com/portal/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.stockx.com/portal/api-introduction
- group: auth
  title: ''
  type: Authentication
  url: authentication/stockx-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/stockx-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/stockx-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/stockx-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/stockx-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/stockx-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/stockx-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/stockx-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/stockx-mcp.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/stockx-agentic-access.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/stockx-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/stockx-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/stockx-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/stockx-domain-security.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/stockx-rate-limits.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/stockx
- group: company
  title: ''
  type: Blog
  url: https://stockx.com/news
- group: operate
  title: ''
  type: Support
  url: https://stockx.com/help
- group: start
  title: ''
  type: SignUp
  url: https://developer.stockx.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://stockx.com/en-us/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://stockx.com/about/privacy-policy
- group: company
  title: ''
  type: Website
  url: https://stockx.com
created: '2026-07-17'
description: StockX is a global online marketplace for sneakers, streetwear, electronics, collectibles, and trading cards, operating on a live bid/ask model similar to a stock exchange. The StockX Public API (v2.0.0) lets approved developers in the StockX Developer Program search the product catalog, read live market data (bids/asks), create and manage seller listings individually or in bulk via asynchronous batch operations, and track sales orders and their shipping documents. Requests authenticate with an x-api-key header plus an OAuth 2.0 bearer token issued by StockX's Auth0 tenant. StockX was surfaced as a portfolio company of Battery Ventures and GV.
image: https://developer.stockx.com/icon.png
layout: provider
mcp_servers:
- description: ''
  name: stockx-mcp.yml
  slug: stockx-mcpyml
modified: '2026-07-21'
name: StockX
nav: Providers
network: true
overview: 'StockX publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Batch API, Catalog API, Listings API, and 1 more. Tagged areas include Company, Marketplace, E-Commerce, Sneakers, and Streetwear.


  StockX''s developer surface includes documentation, API reference, getting-started guide, authentication, changelog, engineering blog, support, and 20 more developer resources.'
random_paper: 103
rate_limits:
- limit_count: 2
  name: Stockx Rate Limits
  slug: stockx-rate-limits
scopes:
- name: Stockx Scopes
  scope_count: 2
  slug: stockx-scopes
  summary_line: 2 scopes · authorizationCode
score:
  band: developing
  composite: 50.7
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 61.6
    developer_ergonomics: 56.0
    discoverability: 92.6
    governance: 20.8
    operational_transparency: 42.1
  previous_composite: 50.7
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
    skills: derived
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
security:
- kind: authentication
  name: Stockx Authentication
  slug: stockx-authentication
  summary_line: apiKey/http/oauth2 · 3 schemes
- kind: domain-security
  name: Stockx Domain Security
  slug: stockx-domain-security
  summary_line: TLSv1.3 · DMARC
slug: stockx
tags:
- Company
- Marketplace
- E-Commerce
- Sneakers
- Streetwear
- Resale
- Collectibles
- Catalog
- Selling
- Orders
website: https://stockx.com
---
