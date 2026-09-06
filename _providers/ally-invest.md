---
access_model:
  confidence: high
  label: Paid · Open access
  onboarding: open
  pricing: paid
  public: true
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.0
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Ally Invest Agentic Access
  operation_count: 28
  slug: ally-invest-agentic-access
  summary_line: 28 operations · 7 acting
api_count: 1
apis:
- baseURL: https://api.ally.com/v1
  baseurl_source: declared
  description: 'The Ally Invest Orders API enables programmatic placement and management of equity and options orders for self-directed brokerage accounts. Orders are submitted using a FIXML-variant format. Supports '
  name: Ally Invest Orders API
  slug: ally-invest-orders-api
- baseURL: https://api.ally.com/v1
  baseurl_source: declared
  description: The Ally Invest Market Data API provides access to real-time and delayed market data including equity and options quotes, option chains, option strikes and expirations, market news search, time-and-sa
  name: Ally Invest Market Data API
  slug: ally-invest-market-data-api
- description: The Ally Invest Streaming API delivers real-time market quotes via a persistent HTTP streaming connection. Clients subscribe to one or more ticker symbols and receive continuous quote updates as marke
  name: Ally Invest Streaming Market Data API
  slug: ally-invest-streaming-api
- baseURL: https://api.ally.com/v1
  baseurl_source: declared
  description: The Ally Invest Watchlists API allows programmatic creation and management of symbol watchlists associated with a member account. Supports listing all watchlists, creating new watchlists, retrieving w
  name: Ally Invest Watchlists API
  slug: ally-invest-watchlists-api
- baseURL: https://api.ally.com/v1
  baseurl_source: declared
  description: The Ally Invest Member API provides access to the authenticated member's profile information including account identifiers and user details associated with the OAuth credentials.
  name: Ally Invest Member API
  slug: ally-invest-member-api
- baseURL: https://api.ally.com/v1
  baseurl_source: declared
  description: Account balances, holdings, history, and portfolio data
  name: Ally Invest Accounts API
  slug: ally-invest-accounts-api
- baseURL: https://api.ally.com/v1
  baseurl_source: declared
  description: Quotes, options, news, time-and-sales, and top lists
  name: Ally Invest Market Data API
  slug: ally-invest-market-data-api
- baseURL: https://api.ally.com/v1
  baseurl_source: declared
  description: Member profile and identity
  name: Ally Invest Member API
  slug: ally-invest-member-api
- baseURL: https://api.ally.com/v1
  baseurl_source: declared
  description: Order placement, preview, retrieval, and cancellation
  name: Ally Invest Orders API
  slug: ally-invest-orders-api
- baseURL: https://api.ally.com/v1
  baseurl_source: declared
  description: API status and version utilities
  name: Ally Invest Utilities API
  slug: ally-invest-utilities-api
- baseURL: https://api.ally.com/v1
  baseurl_source: declared
  description: Watchlist creation and symbol management
  name: Ally Invest Watchlists API
  slug: ally-invest-watchlists-api
artifact_total: 45
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Ally Invest Accounts API
  slug: open-ally-invest-accounts-api
- collection_type: open
  name: Ally Invest Accounts Market Data API
  slug: open-ally-invest-market-data-api
- collection_type: open
  name: Ally Invest Accounts Member API
  slug: open-ally-invest-member-api
- collection_type: open
  name: Ally Invest Accounts Orders API
  slug: open-ally-invest-orders-api
- collection_type: open
  name: Ally Invest Accounts Utilities API
  slug: open-ally-invest-utilities-api
- collection_type: open
  name: Ally Invest Accounts Watchlists API
  slug: open-ally-invest-watchlists-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/ally-invest-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ally-invest-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ally-invest-authentication.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/ally-invest-openapi.yml
- group: company
  title: ''
  type: Website
  url: https://www.ally.com/invest/
- group: docs
  title: ''
  type: Documentation
  url: https://www.ally.com/api/invest/documentation/getting-started/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.ally.com/api/invest/documentation/getting-started/
- group: auth
  title: ''
  type: Authentication
  url: https://www.ally.com/api/invest/documentation/getting-started/
- group: operate
  title: ''
  type: RateLimiting
  url: https://www.ally.com/api/invest/documentation/rate-limiting/
- group: docs
  title: ''
  type: AttributionGuidelines
  url: https://www.ally.com/api/invest/documentation/attribution-guidelines/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ally.com/content/dam/pdf/invest/api-agreement.pdf
- group: operate
  title: ''
  type: Support
  url: mailto:InvestAPI@ally.com
- group: build
  title: AllyInvestPy Python SDK (Community)
  type: SDKs
  url: https://pypi.org/project/AllyInvestPy/
- group: build
  title: PyAlly Python3 SDK (Community)
  type: SDKs
  url: https://pypi.org/project/pyally/
- group: build
  title: ally-api Go Bindings (Community)
  type: SDKs
  url: https://pkg.go.dev/github.com/jmal1997/ally-api
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/anthonymorast/AllyInvest.py
- group: commercial
  title: ''
  type: Pricing
  url: https://www.ally.com/invest/commissions-and-fees/
- group: other
  title: ''
  type: SelfDirectedTrading
  url: https://www.ally.com/invest/self-directed-trading/
- group: commercial
  title: ''
  type: Plans
  url: plans/ally-invest-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/ally-invest-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/ally-invest-finops.yml
created: '2026-06-13'
description: Ally Invest is an online brokerage platform offering commission-free self-directed trading of US stocks, ETFs, and options with no account minimums. The platform provides REST APIs (originally developed from the TradeKing acquisition) for managing self-directed investment accounts, placing trades, accessing streaming real-time market data, retrieving account balances and holdings, managing watchlists, and querying market quotes and news. Authentication uses OAuth 1.0 with consumer and token credentials. Responses are available in JSON and XML formats.
examples:
- key_count: 1
  name: Get Accounts Example
  slug: get-accounts-example
- key_count: 1
  name: Get Market Clock Example
  slug: get-market-clock-example
- key_count: 1
  name: Get Quotes Example
  slug: get-quotes-example
- key_count: 1
  name: Get Watchlists Example
  slug: get-watchlists-example
features:
- description: No commissions on US stocks and ETFs; $0.50 per options contract
  name: Commission-Free Trading
- description: Self-directed cash accounts require no minimum deposit to open
  name: No Account Minimum
- description: API access secured via OAuth 1.0 with consumer key/secret and OAuth token/secret pairs
  name: OAuth 1.0 Authentication
- description: All REST API endpoints return responses in both JSON and XML formats
  name: JSON and XML Responses
- description: Real-time quote streaming via persistent HTTP connections for subscribed symbols
  name: Streaming Market Data
- description: Orders submitted in FIXML-variant XML format supporting equities and options
  name: FIXML Order Format
- description: Preview orders before execution to validate parameters and estimated costs
  name: Order Preview
finops:
- name: Ally Invest Finops
  service_category: ''
  slug: ally-invest-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ally-invest.png
json_schemas:
- name: AllyInvestAccountBalance
  property_count: 7
  slug: ally-invest-account-balance
- name: AllyInvestOrder
  property_count: 15
  slug: ally-invest-order
- name: AllyInvestQuote
  property_count: 95
  slug: ally-invest-quote
jsonld:
- class_count: 5
  name: Ally Invest Context
  property_count: 46
  slug: ally-invest-context
layout: provider
modified: '2026-06-13'
name: Ally Invest
nav: Providers
network: true
overview: 'Ally Invest publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Orders API, Market Data API, Watchlists API, and 7 more. Tagged areas include Brokerage, Investing, Trading, Finance, and Stocks.


  The Ally Invest catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Ally Invest''s developer surface includes authentication, documentation, getting-started guide, support, pricing, and 16 more developer resources.'
plans:
- name: Ally Invest Plans Pricing
  plan_count: 1
  slug: ally-invest-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 3
  name: Ally Invest Rate Limits
  slug: ally-invest-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Ally Invest API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: ally-invest-jsonschema-spectral-rules
score:
  band: developing
  composite: 51.1
  coverage:
    artifact_dirs: 13
    catalog_earned: 74.3
    catalog_earned_first_party: 0.0
    catalog_gap: 40.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 9.8
    contract_quality: 64.6
    developer_ergonomics: 54.8
    discoverability: 68.5
    governance: 9.8
    operational_transparency: 34.2
  previous_composite: 51.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 45.0
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
security:
- kind: authentication
  name: Ally Invest Authentication
  slug: ally-invest-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Ally Invest Domain Security
  slug: ally-invest-domain-security
  summary_line: TLSv1.3 · DMARC
slug: ally-invest
tags:
- Brokerage
- Investing
- Trading
- Finance
- Stocks
- Options
- Market Data
- Self-Directed
use_cases:
- description: Build automated trading systems that place and manage orders based on market signals
  name: Algorithmic Trading
- description: Track account balances, holdings, and performance in real time via API
  name: Portfolio Monitoring
- description: Retrieve real-time and delayed quotes, options chains, and news for analysis
  name: Market Data Aggregation
- description: Maintain dynamic symbol watchlists and retrieve quote updates for tracked securities
  name: Watchlist Management
- description: Pull account history and order records programmatically for trade journaling tools
  name: Trade Journaling
website: https://www.ally.com/invest/
---
