---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
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
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 34.6
  scored_at: '2026-09-16'
api_count: 1
apis:
- baseURL: https://bitculator.com/api/v1
  baseurl_source: declared
  description: Price-alarm CRUD — the same alarms the web app manages. Alarms consume the key owner's alarm inventory balance, are TARGET-type on coins only, and an above/below vs current-value guard blocks alarms t
  name: Bitculator Alarms API
  slug: bitculator-alarms-api
- baseURL: https://bitculator.com/api/v1
  baseurl_source: declared
  description: 'Server-side financial calculators mirroring the web tools: DCA, profit/loss and loan (which read cached market data), plus stateless compound-interest and staking math.'
  name: Bitculator Calculators API
  slug: bitculator-calculators-api
- baseURL: https://bitculator.com/api/v1
  baseurl_source: declared
  description: 'Ranked coin and token market data: paginated listings, single-coin detail, movers (gainers/losers), recently-added, trending, and per-coin time series. Prices, marketcap and supply are decimal STRINGS'
  name: Bitculator Coins API
  slug: bitculator-coins-api
- baseURL: https://bitculator.com/api/v1
  baseurl_source: declared
  description: Convert between any two active assets (crypto AND fiat), and list the currencies usable as conversion legs. Values are decimal strings. Fiat FX rates refresh ~twice daily; crypto rates ~every minute.
  name: Bitculator Conversion API
  slug: bitculator-conversion-api
- baseURL: https://bitculator.com/api/v1
  baseurl_source: declared
  description: 'Editorial articles — published (ACTIVE) only. `locale` picks the content language with per-field English fallback (the payload reports which `locale` actually won). Articles can be filtered by tag or '
  name: Bitculator Editorial API
  slug: bitculator-editorial-api
- baseURL: https://bitculator.com/api/v1
  baseurl_source: declared
  description: Exchange rankings, detail, trust scores, time series and per-exchange market/coin listings. Volumes are USD. There is no CEX/DEX column — `type` is derived from the exchange taxonomy, so it can be "ce
  name: Bitculator Exchanges API
  slug: bitculator-exchanges-api
- baseURL: https://bitculator.com/api/v1
  baseurl_source: declared
  description: Market-wide aggregates — total marketcap and volume, asset/exchange/pair/market counts, BTC/ETH dominance with a rank-based top-3, the market Fear & Greed reading, plus a top-100 heatmap and marketcap
  name: Bitculator Global Market API
  slug: bitculator-global-market-api
- baseURL: https://bitculator.com/api/v1
  baseurl_source: declared
  description: Per-coin technical indicators. Each indicator is its own dedicated endpoint — momentum oscillators (RSI, Stoch-RSI, CCI, MFI, Williams %R), trend and price baselines (SMA, MACD, VWAP), volume flow (OB
  name: Bitculator Indicators API
  slug: bitculator-indicators-api
- baseURL: https://bitculator.com/api/v1
  baseurl_source: declared
  description: 'Derivatives liquidations. Source coverage is currently OKX swap markets only (stated in every `meta.note`). The RAW feed (the `/liquidations` list and the hourly breakdown) is pruned after ~48 hours; '
  name: Bitculator Liquidations API
  slug: bitculator-liquidations-api
- baseURL: https://bitculator.com/api/v1
  baseurl_source: declared
  description: Tickers (per-exchange markets) and pairs (venue-aggregated markets), plus a coin's markets and raw per-exchange trading symbols. All of it is snapshot data — no per-ticker/pair history exists. USD vol
  name: Bitculator Markets API
  slug: bitculator-markets-api
- baseURL: https://bitculator.com/api/v1
  baseurl_source: declared
  description: 'API meta and introspection: an authenticated ping to verify a key and the middleware stack, current-key usage/quota, and the machine-readable OpenAPI spec.'
  name: Bitculator Meta API
  slug: bitculator-meta-api
- baseURL: https://bitculator.com/api/v1
  baseurl_source: declared
  description: The lightweight price hot path — current price, marketcap, 24h volume and recent changes for a requested set of coins. `/prices` requires a selector (ids, slugs or symbols); `/prices/{slug}` targets o
  name: Bitculator Prices API
  slug: bitculator-prices-api
- baseURL: https://bitculator.com/api/v1
  baseurl_source: declared
  description: Market and per-coin sentiment indices. Fear & Greed and Bull/Bear are 15-minute-refresh SNAPSHOTS — only the current reading exists, there is no time series for them. Altseason carries full daily hist
  name: Bitculator Sentiment API
  slug: bitculator-sentiment-api
- baseURL: https://bitculator.com/api/v1
  baseurl_source: declared
  description: 'Crypto wallet reviews — review `score`, supported-asset count, pros/cons counts, price model and release date, plus a grouped tag taxonomy on detail/compare responses. `meta.top_score` is the highest '
  name: Bitculator Wallets API
  slug: bitculator-wallets-api
- baseURL: https://bitculator.com/api/v1
  baseurl_source: declared
  description: 'Bitculator POSTs each event as JSON with an HMAC signature header: X-Bitculator-Signature: t=<unix-ts>,v1=<hex hmac_sha256("<ts>.<raw-body>", secret)> X-Bitculator-Event: alarm.triggered Verify it by '
  name: Bitculator Webhooks API
  slug: bitculator-webhooks-api
artifact_total: 21
asyncapis:
- description: ''
  name: Bitculator Webhooks
  slug: bitculator-webhooks
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bitculator/refs/heads/main/overlays/bitculator-data-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/bitculator-data-api-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.bitculator.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bitculator/refs/heads/main/authentication/bitculator-authentication.yml
  title: ''
  type: Authentication
  url: authentication/bitculator-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bitculator/refs/heads/main/security/bitculator-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bitculator-domain-security.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/bitculator/refs/heads/main/packages/bitculator-packages.yml
  title: ''
  type: Packages
  url: packages/bitculator-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/bitculator/refs/heads/main/packages/bitculator-packages.yml
  title: ''
  type: SDKs
  url: packages/bitculator-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bitculator/refs/heads/main/mcp/bitculator-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/bitculator-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/bitculator/refs/heads/main/mcp/bitculator-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/bitculator-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bitculator/refs/heads/main/llms/bitculator-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bitculator-llms.txt
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bitculator/refs/heads/main/conformance/bitculator-conformance.yml
  title: ''
  type: Conformance
  url: conformance/bitculator-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bitculator/refs/heads/main/errors/bitculator-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/bitculator-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bitculator/refs/heads/main/lifecycle/bitculator-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/bitculator-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bitculator/refs/heads/main/conventions/bitculator-conventions.yml
  title: ''
  type: Conventions
  url: conventions/bitculator-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bitculator/refs/heads/main/components/bitculator-components.yml
  title: ''
  type: Components
  url: components/bitculator-components.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bitculator/refs/heads/main/data-model/bitculator-data-model.yml
  title: ''
  type: DataModel
  url: data-model/bitculator-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bitculator/refs/heads/main/asyncapi/bitculator-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/bitculator-webhooks.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bitculator/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/bitculator/refs/heads/main/plans/bitculator-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/bitculator-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/bitculator/refs/heads/main/rate-limits/bitculator-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/bitculator-rate-limits.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Bitculator
- group: commercial
  title: ''
  type: Pricing
  url: https://bitculator.com/en/crypto-api
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bitculator.com/en/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bitculator.com/en/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://bitculator.com/en/contact
- group: start
  title: ''
  type: SignUp
  url: https://bitculator.com/en/register
created: '2026-07-05'
description: Modern cryptocurrency REST API providing programmatic read access to crypto market data including coins, prices, markets, exchanges, wallets, global market data, sentiment, indicators, liquidations, conversions, calculators, editorial content, alarms, and webhooks. Version 1.0.0 with 70+ endpoints across 15 groups.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bitculator.png
layout: provider
mcp_servers:
- description: 'Official hosted MCP server exposing the Bitculator Data API as 19 curated, read-only tools over Streamable HTTP. One key, one quota: every tool call counts as one Data API request against the plan''s m'
  name: Bitculator MCP Server
  slug: bitculator-mcp-server
modified: '2026-09-03'
name: Bitculator
nav: Providers
network: true
overview: 'Bitculator publishes 15 APIs on the [APIs.io](https://apis.io/) network, including Alarms API, Calculators API, Coins API, and 12 more. Tagged areas include Cryptocurrency, crypto-market-data, Blockchain, Finance, and Fintech.


  The Bitculator catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Bitculator''s developer surface includes authentication, pricing, support, signup flow, and 21 more developer resources.'
plans:
- name: Bitculator Plans Pricing
  plan_count: 3
  slug: bitculator-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 6
  name: Bitculator Rate Limits
  slug: bitculator-rate-limits
score:
  band: developing
  composite: 53.1
  coverage:
    artifact_dirs: 20
    catalog_earned: 61.0
    catalog_earned_first_party: 24.0
    catalog_gap: 54.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 4.2
  facets:
    access_clarity: 76.3
    contract_governance: 4.5
    contract_quality: 58.3
    developer_ergonomics: 47.0
    discoverability: 75.9
    operational_transparency: 42.1
  previous_composite: 48.9
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 15
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 39.1
  schema_version: 0.22.0
  scored_at: '2026-09-16'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/bitculator/refs/heads/main/screenshots/bitculator-2026-07-25T203141.png
security:
- kind: authentication
  name: Bitculator Authentication
  slug: bitculator-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Bitculator Domain Security
  slug: bitculator-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: bitculator
tags:
- Cryptocurrency
- crypto-market-data
- Blockchain
- Finance
- Fintech
- Web3
- Trading
- Exchange Data
- Wallets
- Sentiment
- Indicators
website: https://www.bitculator.com/
---
