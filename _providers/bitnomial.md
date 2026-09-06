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
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.4
  scored_at: '2026-09-05'
api_count: 2
apis:
- description: Public HTTPS REST API for the Bitnomial exchange — products and contract specs, orders, fills, block trades, indexes, funding rates, and market statistics. HMAC-SHA256 signed authentication; cursor pa
  name: Bitnomial Exchange REST API
  slug: bitnomial-exchange-rest-api
- baseURL: https://bitnomial.com/exchange/api/v1/prod
  baseurl_source: declared
  description: Real-time WebSocket market-data feed delivering trade, order book, block trade, and market status messages for subscribed products.
  name: Bitnomial Market Data WebSocket API
  slug: bitnomial-market-data-websocket-api
artifact_total: 6
asyncapis:
- description: Real-time market-data feed for Bitnomial's CFTC-regulated derivatives exchange. Clients open a WebSocket connection and must send a subscribe message within 10 seconds or they are disconnected. Faithf
  name: Bitnomial Market Data WebSocket API
  slug: bitnomial-market-data-asyncapi
common:
- group: company
  title: ''
  type: Website
  url: https://bitnomial.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://bitnomial.com/exchange/docs
- group: docs
  title: ''
  type: Documentation
  url: https://bitnomial.com/exchange/docs/api/overview/
- group: docs
  title: ''
  type: APIReference
  url: https://bitnomial.com/exchange/docs/api/rest/overview/
- group: start
  title: ''
  type: GettingStarted
  url: https://bitnomial.com/exchange/docs/api/rest/authentication/
- group: company
  title: ''
  type: Blog
  url: https://bitnomial.com/blog
- group: operate
  title: ''
  type: Support
  url: mailto:help@exchange.bitnomial.com
- group: operate
  title: ''
  type: StatusPage
  url: https://bitnomial.statuspage.io
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bitnomial
- group: auth
  title: ''
  type: Authentication
  url: authentication/bitnomial-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/bitnomial-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/bitnomial-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/bitnomial-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/bitnomial-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/bitnomial-sandbox.yml
- group: build
  title: ''
  type: Packages
  url: packages/bitnomial-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/bitnomial-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/bitnomial-cli.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/bitnomial-llms.txt
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/bitnomial-mcp.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/bitnomial-market-data-asyncapi.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/bitnomial-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bitnomial-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/bitnomial-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://bitnomial.com/security
created: '2026-07-17'
description: Bitnomial is a Chicago-based derivatives exchange company that owns and operates U.S. CFTC-regulated subsidiaries — a Designated Contract Market (exchange/DCM), a Derivatives Clearing Organization (clearinghouse/DCO), and a Futures Commission Merchant (clearing brokerage/FCM). It offers leveraged spot, perpetuals, futures, options, and prediction markets on a single regulated venue with crypto margin and settlement. For developers, Bitnomial publishes a public HTTPS REST API (products, orders, fills, block trades, indexes, funding rates, market stats), a real-time WebSocket market-data feed (trade, book, block, status channels), a low-latency binary order-entry protocol (BTP), and a FIX 4.4 API with dropcopy. REST authentication uses HMAC-SHA256 request signing with per-connection credentials. Surfaced as a portfolio company of Electric Capital and enriched by the API Evangelist pipeline.
image: https://bitnomial.com/images/social-preview.jpg
layout: provider
modified: '2026-07-18'
name: Bitnomial
nav: Providers
network: true
overview: 'Bitnomial publishes 1 API on the [APIs.io](https://apis.io/) network: Market Data WebSocket API. Tagged areas include Company, Fintech, Cryptocurrency, Derivatives, and Exchange.


  The Bitnomial catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Bitnomial''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, authentication, sandbox, and 18 more developer resources.'
random_paper: 14
score:
  band: developing
  composite: 40.1
  coverage:
    artifact_dirs: 16
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 18.2
    contract_quality: 41.7
    developer_ergonomics: 78.6
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 28.9
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 40.1
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 38.3
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bitnomial/refs/heads/main/screenshots/bitnomial-2026-07-25T203158.png
security:
- kind: authentication
  name: Bitnomial Authentication
  slug: bitnomial-authentication
  summary_line: hmac-signed-api-key · 1 scheme
- kind: domain-security
  name: Bitnomial Domain Security
  slug: bitnomial-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Bitnomial Vulnerability Disclosure
  slug: bitnomial-vulnerability-disclosure
  summary_line: disclosure policy published
slug: bitnomial
tags:
- Company
- Fintech
- Cryptocurrency
- Derivatives
- Exchange
- Trading
- Market Data
- Futures
- Options
- CFTC Regulated
website: https://bitnomial.com/
---
