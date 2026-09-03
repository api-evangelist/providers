---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - '{''url'': ''https://polygon.io/'', ''status'': 301, ''note'': ''declared website redirects to https://massive.com/ — a different registrable domain (polygon.io -> massive.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
  trial: false
  try_now: true
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: na
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: derived
    idempotency: na
    mcp_server: verified
    openapi_examples: verified
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 63.1
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Polygon Agentic Access
  operation_count: 175
  slug: polygon-agentic-access
  summary_line: 175 operations
api_count: 7
apis:
- baseURL: wss://socket.polygon.io
  baseurl_source: declared
  description: Real-time streaming WebSocket clusters per asset class (stocks/options/indices/forex/crypto). Subscribers authenticate with an API key and subscribe to channels for trades, quotes, aggregates, and boo
  name: Polygon WebSocket API
  slug: websocket-api
- baseURL: https://api.polygon.io
  baseurl_source: declared
  description: Crypto aggregate bars.
  name: Polygon Aggregates API
  slug: polygon-aggregates-api
- baseURL: https://api.polygon.io
  baseurl_source: declared
  description: Level-2 order book.
  name: Polygon Books API
  slug: polygon-books-api
- baseURL: https://api.polygon.io
  baseurl_source: declared
  description: Option contract reference data.
  name: Polygon Contracts API
  slug: polygon-contracts-api
- baseURL: https://api.polygon.io
  baseurl_source: declared
  description: Real-time currency conversion.
  name: Polygon Conversion API
  slug: polygon-conversion-api
- baseURL: https://api.polygon.io
  baseurl_source: declared
  description: Stock splits and dividends.
  name: Polygon CorporateActions API
  slug: polygon-corporateactions-api
- baseURL: https://api.polygon.io
  baseurl_source: declared
  description: Daily open/close.
  name: Polygon DailyBars API
  slug: polygon-dailybars-api
- baseURL: https://api.polygon.io
  baseurl_source: declared
  description: Markets, exchanges, holidays, and status.
  name: Polygon Markets API
  slug: polygon-markets-api
- baseURL: https://api.polygon.io
  baseurl_source: declared
  description: Ticker news.
  name: Polygon News API
  slug: polygon-news-api
- baseURL: https://api.polygon.io
  baseurl_source: declared
  description: FX quote endpoints.
  name: Polygon Quotes API
  slug: polygon-quotes-api
- baseURL: https://api.polygon.io
  baseurl_source: declared
  description: Snapshot endpoints.
  name: Polygon Snapshots API
  slug: polygon-snapshots-api
- baseURL: https://api.polygon.io
  baseurl_source: declared
  description: Ticker reference and metadata.
  name: Polygon Tickers API
  slug: polygon-tickers-api
- baseURL: wss://socket.polygon.io
  baseurl_source: declared
  description: The benzinga API from Polygon — 9 operation(s) for benzinga.
  name: Polygon Benzinga API
  slug: polygon-benzinga-api
- baseURL: wss://socket.polygon.io
  baseurl_source: declared
  description: The crypto:aggregates API from Polygon — 7 operation(s) for crypto:aggregates.
  name: Polygon Crypto:aggregates API
  slug: polygon-crypto-aggregates-api
- baseURL: wss://socket.polygon.io
  baseurl_source: declared
  description: The crypto:last:trade API from Polygon — 1 operation(s) for crypto:last:trade.
  name: Polygon Crypto:last:trade API
  slug: polygon-crypto-last-trade-api
- baseURL: wss://socket.polygon.io
  baseurl_source: declared
  description: The crypto:open-close API from Polygon — 1 operation(s) for crypto:open-close.
  name: Polygon Crypto:open Close API
  slug: polygon-crypto-open-close-api
- baseURL: wss://socket.polygon.io
  baseurl_source: declared
  description: The crypto:snapshot API from Polygon — 4 operation(s) for crypto:snapshot.
  name: Polygon Crypto:snapshot API
  slug: polygon-crypto-snapshot-api
- baseURL: wss://socket.polygon.io
  baseurl_source: declared
  description: The crypto:trades API from Polygon — 2 operation(s) for crypto:trades.
  name: Polygon Crypto:trades API
  slug: polygon-crypto-trades-api
- baseURL: wss://socket.polygon.io
  baseurl_source: declared
  description: The etfglobal API from Polygon — 5 operation(s) for etfglobal.
  name: Polygon Etfglobal API
  slug: polygon-etfglobal-api
- baseURL: wss://socket.polygon.io
  baseurl_source: declared
  description: The fable API from Polygon — 2 operation(s) for fable.
  name: Polygon Fable API
  slug: polygon-fable-api
- baseURL: wss://socket.polygon.io
  baseurl_source: declared
  description: The fed API from Polygon — 4 operation(s) for fed.
  name: Polygon Fed API
  slug: polygon-fed-api
- baseURL: wss://socket.polygon.io
  baseurl_source: declared
  description: The financials API from Polygon — 4 operation(s) for financials.
  name: Polygon Financials API
  slug: polygon-financials-api
- baseURL: wss://socket.polygon.io
  baseurl_source: declared
  description: The futures:aggregates API from Polygon — 1 operation(s) for futures:aggregates.
  name: Polygon Futures:aggregates API
  slug: polygon-futures-aggregates-api
- baseURL: wss://socket.polygon.io
  baseurl_source: declared
  description: The fx:aggregates API from Polygon — 7 operation(s) for fx:aggregates.
  name: Polygon Fx:aggregates API
  slug: polygon-fx-aggregates-api
- baseURL: wss://socket.polygon.io
  baseurl_source: declared
  description: The fx:conversion API from Polygon — 1 operation(s) for fx:conversion.
  name: Polygon Fx:conversion API
  slug: polygon-fx-conversion-api
- baseURL: wss://socket.polygon.io
  baseurl_source: declared
  description: The fx:last:quote API from Polygon — 1 operation(s) for fx:last:quote.
  name: Polygon Fx:last:quote API
  slug: polygon-fx-last-quote-api
- baseURL: wss://socket.polygon.io
  baseurl_source: declared
  description: The fx:quotes API from Polygon — 1 operation(s) for fx:quotes.
  name: Polygon Fx:quotes API
  slug: polygon-fx-quotes-api
- baseURL: wss://socket.polygon.io
  baseurl_source: declared
  description: The fx:snapshot API from Polygon — 3 operation(s) for fx:snapshot.
  name: Polygon Fx:snapshot API
  slug: polygon-fx-snapshot-api
- baseURL: wss://socket.polygon.io
  baseurl_source: declared
  description: The fx:trades API from Polygon — 1 operation(s) for fx:trades.
  name: Polygon Fx:trades API
  slug: polygon-fx-trades-api
- baseURL: wss://socket.polygon.io
  baseurl_source: declared
  description: The global_crypto API from Polygon — 1 operation(s) for global_crypto.
  name: Polygon Global Crypto API
  slug: polygon-global-crypto-api
- baseURL: wss://socket.polygon.io
  baseurl_source: declared
  description: The global_forex API from Polygon — 1 operation(s) for global_forex.
  name: Polygon Global Forex API
  slug: polygon-global-forex-api
- baseURL: wss://socket.polygon.io
  baseurl_source: declared
  description: The indices:aggregates API from Polygon — 6 operation(s) for indices:aggregates.
  name: Polygon Indices:aggregates API
  slug: polygon-indices-aggregates-api
- baseURL: wss://socket.polygon.io
  baseurl_source: declared
  description: The indices:snapshot API from Polygon — 1 operation(s) for indices:snapshot.
  name: Polygon Indices:snapshot API
  slug: polygon-indices-snapshot-api
- baseURL: wss://socket.polygon.io
  baseurl_source: declared
  description: The options:aggregates API from Polygon — 6 operation(s) for options:aggregates.
  name: Polygon Options:aggregates API
  slug: polygon-options-aggregates-api
- baseURL: wss://socket.polygon.io
  baseurl_source: declared
  description: The options:last:trade API from Polygon — 1 operation(s) for options:last:trade.
  name: Polygon Options:last:trade API
  slug: polygon-options-last-trade-api
- baseURL: wss://socket.polygon.io
  baseurl_source: declared
  description: The options:open-close API from Polygon — 1 operation(s) for options:open-close.
  name: Polygon Options:open Close API
  slug: polygon-options-open-close-api
- baseURL: wss://socket.polygon.io
  baseurl_source: declared
  description: The options:quotes API from Polygon — 1 operation(s) for options:quotes.
  name: Polygon Options:quotes API
  slug: polygon-options-quotes-api
- baseURL: wss://socket.polygon.io
  baseurl_source: declared
  description: The options:snapshot API from Polygon — 2 operation(s) for options:snapshot.
  name: Polygon Options:snapshot API
  slug: polygon-options-snapshot-api
- baseURL: wss://socket.polygon.io
  baseurl_source: declared
  description: The options:trades API from Polygon — 1 operation(s) for options:trades.
  name: Polygon Options:trades API
  slug: polygon-options-trades-api
- baseURL: wss://socket.polygon.io
  baseurl_source: declared
  description: Reference API
  name: Polygon Reference API
  slug: polygon-reference-api
- baseURL: wss://socket.polygon.io
  baseurl_source: declared
  description: The reference:conditions API from Polygon — 1 operation(s) for reference:conditions.
  name: Polygon Reference:conditions API
  slug: polygon-reference-conditions-api
- baseURL: wss://socket.polygon.io
  baseurl_source: declared
  description: The reference:dividends API from Polygon — 1 operation(s) for reference:dividends.
  name: Polygon Reference:dividends API
  slug: polygon-reference-dividends-api
- baseURL: wss://socket.polygon.io
  baseurl_source: declared
  description: The reference:exchanges API from Polygon — 1 operation(s) for reference:exchanges.
  name: Polygon Reference:exchanges API
  slug: polygon-reference-exchanges-api
- baseURL: wss://socket.polygon.io
  baseurl_source: declared
  description: The reference:news API from Polygon — 1 operation(s) for reference:news.
  name: Polygon Reference:news API
  slug: polygon-reference-news-api
- baseURL: wss://socket.polygon.io
  baseurl_source: declared
  description: The reference:options:contract API from Polygon — 1 operation(s) for reference:options:contract.
  name: Polygon Reference:options:contract API
  slug: polygon-reference-options-contract-api
- baseURL: wss://socket.polygon.io
  baseurl_source: declared
  description: The reference:options:contracts:list API from Polygon — 1 operation(s) for reference:options:contracts:list.
  name: Polygon Reference:options:contracts:list API
  slug: polygon-reference-options-contracts-list-api
- baseURL: wss://socket.polygon.io
  baseurl_source: declared
  description: The reference:related:companies API from Polygon — 1 operation(s) for reference:related:companies.
  name: Polygon Reference:related:companies API
  slug: polygon-reference-related-companies-api
- baseURL: wss://socket.polygon.io
  baseurl_source: declared
  description: The reference:sec:filing API from Polygon — 1 operation(s) for reference:sec:filing.
  name: Polygon Reference:sec:filing API
  slug: polygon-reference-sec-filing-api
- baseURL: wss://socket.polygon.io
  baseurl_source: declared
  description: The reference:sec:filing:file API from Polygon — 1 operation(s) for reference:sec:filing:file.
  name: Polygon Reference:sec:filing:file API
  slug: polygon-reference-sec-filing-file-api
- baseURL: wss://socket.polygon.io
  baseurl_source: declared
  description: The reference:sec:filing:files API from Polygon — 1 operation(s) for reference:sec:filing:files.
  name: Polygon Reference:sec:filing:files API
  slug: polygon-reference-sec-filing-files-api
- baseURL: wss://socket.polygon.io
  baseurl_source: declared
  description: The reference:sec:filings API from Polygon — 1 operation(s) for reference:sec:filings.
  name: Polygon Reference:sec:filings API
  slug: polygon-reference-sec-filings-api
- baseURL: wss://socket.polygon.io
  baseurl_source: declared
  description: The reference:stocks API from Polygon — 2 operation(s) for reference:stocks.
  name: Polygon Reference:stocks API
  slug: polygon-reference-stocks-api
- baseURL: wss://socket.polygon.io
  baseurl_source: declared
  description: The reference:stocks:ipos API from Polygon — 1 operation(s) for reference:stocks:ipos.
  name: Polygon Reference:stocks:ipos API
  slug: polygon-reference-stocks-ipos-api
- baseURL: wss://socket.polygon.io
  baseurl_source: declared
  description: The reference:stocks:market API from Polygon — 2 operation(s) for reference:stocks:market.
  name: Polygon Reference:stocks:market API
  slug: polygon-reference-stocks-market-api
- baseURL: wss://socket.polygon.io
  baseurl_source: declared
  description: The reference:tickers:get API from Polygon — 2 operation(s) for reference:tickers:get.
  name: Polygon Reference:tickers:get API
  slug: polygon-reference-tickers-get-api
- baseURL: wss://socket.polygon.io
  baseurl_source: declared
  description: The reference:tickers:list API from Polygon — 1 operation(s) for reference:tickers:list.
  name: Polygon Reference:tickers:list API
  slug: polygon-reference-tickers-list-api
- baseURL: wss://socket.polygon.io
  baseurl_source: declared
  description: The reference:tickers:types API from Polygon — 1 operation(s) for reference:tickers:types.
  name: Polygon Reference:tickers:types API
  slug: polygon-reference-tickers-types-api
- baseURL: wss://socket.polygon.io
  baseurl_source: declared
  description: The Snapshot API from Polygon — 1 operation(s) for snapshot.
  name: Polygon Snapshot API
  slug: polygon-snapshot-api
- baseURL: wss://socket.polygon.io
  baseurl_source: declared
  description: The stocks:aggregates API from Polygon — 7 operation(s) for stocks:aggregates.
  name: Polygon Stocks:aggregates API
  slug: polygon-stocks-aggregates-api
- baseURL: wss://socket.polygon.io
  baseurl_source: declared
  description: The stocks:last:quote API from Polygon — 1 operation(s) for stocks:last:quote.
  name: Polygon Stocks:last:quote API
  slug: polygon-stocks-last-quote-api
- baseURL: wss://socket.polygon.io
  baseurl_source: declared
  description: The stocks:last:trade API from Polygon — 1 operation(s) for stocks:last:trade.
  name: Polygon Stocks:last:trade API
  slug: polygon-stocks-last-trade-api
- baseURL: wss://socket.polygon.io
  baseurl_source: declared
  description: The stocks:open-close API from Polygon — 2 operation(s) for stocks:open-close.
  name: Polygon Stocks:open Close API
  slug: polygon-stocks-open-close-api
- baseURL: wss://socket.polygon.io
  baseurl_source: declared
  description: The stocks:quotes API from Polygon — 2 operation(s) for stocks:quotes.
  name: Polygon Stocks:quotes API
  slug: polygon-stocks-quotes-api
- baseURL: wss://socket.polygon.io
  baseurl_source: declared
  description: The stocks:snapshot API from Polygon — 3 operation(s) for stocks:snapshot.
  name: Polygon Stocks:snapshot API
  slug: polygon-stocks-snapshot-api
- baseURL: wss://socket.polygon.io
  baseurl_source: declared
  description: The stocks:trades API from Polygon — 2 operation(s) for stocks:trades.
  name: Polygon Stocks:trades API
  slug: polygon-stocks-trades-api
- baseURL: wss://socket.polygon.io
  baseurl_source: declared
  description: The Summaries API from Polygon — 1 operation(s) for summaries.
  name: Polygon Summaries API
  slug: polygon-summaries-api
- baseURL: wss://socket.polygon.io
  baseurl_source: declared
  description: The tmx API from Polygon — 1 operation(s) for tmx.
  name: Polygon Tmx API
  slug: polygon-tmx-api
- baseURL: wss://socket.polygon.io
  baseurl_source: declared
  description: The us_futures API from Polygon — 8 operation(s) for us_futures.
  name: Polygon Us Futures API
  slug: polygon-us-futures-api
- baseURL: wss://socket.polygon.io
  baseurl_source: declared
  description: The us_options API from Polygon — 3 operation(s) for us_options.
  name: Polygon Us Options API
  slug: polygon-us-options-api
- baseURL: wss://socket.polygon.io
  baseurl_source: declared
  description: The us_stocks_all API from Polygon — 2 operation(s) for us_stocks_all.
  name: Polygon Us Stocks All API
  slug: polygon-us-stocks-all-api
- baseURL: wss://socket.polygon.io
  baseurl_source: declared
  description: The us_stocks_reference API from Polygon — 3 operation(s) for us_stocks_reference.
  name: Polygon Us Stocks Reference API
  slug: polygon-us-stocks-reference-api
arazzos:
- description: Resolve a ticker, then list its stock splits and dividends history.
  name: Polygon Corporate Actions Review
  slug: polygon-corporate-actions-workflow
- description: Check market status, snapshot a crypto pair, and read its daily open/close.
  name: Polygon Crypto Daily Comparison
  slug: polygon-crypto-daily-comparison-workflow
- description: Snapshot a crypto pair, pull its aggregate bars, and read its Level-2 order book.
  name: Polygon Crypto Pair Analysis
  slug: polygon-crypto-pair-analysis-workflow
- description: Read a currency pair's last quote, convert an amount, and pull its aggregate bars.
  name: Polygon Forex Pair Analysis
  slug: polygon-forex-pair-analysis-workflow
- description: Check market status, pull grouped daily bars for all US stocks, and profile one symbol.
  name: Polygon Grouped Market Scan
  slug: polygon-grouped-market-scan-workflow
- description: Snapshot an index, pull its aggregate bars, and read its previous close.
  name: Polygon Index Analysis
  slug: polygon-index-analysis-workflow
- description: Check current US market status, then pull a stock's daily open/close and previous close.
  name: Polygon Market-Gated Stock Daily Snapshot
  slug: polygon-market-gated-stock-daily-workflow
- description: Resolve an underlying's details, scan its options chain, and read its previous close.
  name: Polygon Options Chain Scan
  slug: polygon-options-chain-scan-workflow
- description: List an underlying's option contracts, snapshot the top contract, and pull its bars.
  name: Polygon Options Contract Deep Dive
  slug: polygon-options-contract-deep-dive-workflow
- description: Resolve a stock ticker's reference details, pull its aggregate bars, and read its previous close.
  name: Polygon Stock Research
  slug: polygon-stock-research-workflow
- description: Search active stock tickers, resolve the top match's details, and pull its recent bars.
  name: Polygon Ticker Discovery and Profile
  slug: polygon-ticker-discovery-workflow
- description: Resolve a ticker's details, pull recent news, and read its previous close.
  name: Polygon Ticker News Context
  slug: polygon-ticker-news-context-workflow
artifact_total: 162
asyncapis:
- description: 'Polygon real-time market data WebSocket clusters. Each asset class (stocks, options, indices, forex, crypto) has its own dedicated cluster at `wss://socket.polygon.io/{cluster}`. Clients authenticate '
  name: Polygon WebSocket Streaming API
  slug: polygon-websocket-asyncapi
collections:
- collection_type: postman
  name: Polygon Crypto REST Aggregates API
  slug: postman-polygon-aggregates-api
- collection_type: postman
  name: Polygon Crypto REST Aggregates Books API
  slug: postman-polygon-books-api
- collection_type: postman
  name: Polygon Crypto REST Aggregates Contracts API
  slug: postman-polygon-contracts-api
- collection_type: postman
  name: Polygon Crypto REST Aggregates Conversion API
  slug: postman-polygon-conversion-api
- collection_type: postman
  name: Polygon Crypto REST Aggregates CorporateActions API
  slug: postman-polygon-corporateactions-api
- collection_type: postman
  name: Polygon Crypto REST API
  slug: postman-polygon-crypto
- collection_type: postman
  name: Polygon Crypto REST Aggregates DailyBars API
  slug: postman-polygon-dailybars-api
- collection_type: postman
  name: Polygon Forex REST API
  slug: postman-polygon-forex
- collection_type: postman
  name: Polygon Indices REST API
  slug: postman-polygon-indices
- collection_type: postman
  name: Polygon Crypto REST Aggregates Markets API
  slug: postman-polygon-markets-api
- collection_type: postman
  name: Polygon Crypto REST Aggregates News API
  slug: postman-polygon-news-api
- collection_type: postman
  name: Polygon Options REST API
  slug: postman-polygon-options
- collection_type: postman
  name: Polygon Crypto REST Aggregates Quotes API
  slug: postman-polygon-quotes-api
- collection_type: postman
  name: Polygon Reference REST API
  slug: postman-polygon-reference
- collection_type: postman
  name: Polygon Crypto REST Aggregates Snapshots API
  slug: postman-polygon-snapshots-api
- collection_type: postman
  name: Polygon Stocks REST API
  slug: postman-polygon-stocks
- collection_type: postman
  name: Polygon Crypto REST Aggregates Tickers API
  slug: postman-polygon-tickers-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Polygon Crypto REST Aggregates API
  slug: open-polygon-aggregates-api
- collection_type: open
  name: Polygon Crypto REST Aggregates Books API
  slug: open-polygon-books-api
- collection_type: open
  name: Polygon Crypto REST Aggregates Contracts API
  slug: open-polygon-contracts-api
- collection_type: open
  name: Polygon Crypto REST Aggregates Conversion API
  slug: open-polygon-conversion-api
- collection_type: open
  name: Polygon Crypto REST Aggregates CorporateActions API
  slug: open-polygon-corporateactions-api
- collection_type: open
  name: Polygon Crypto REST API
  slug: open-polygon-crypto
- collection_type: open
  name: Polygon Crypto REST Aggregates DailyBars API
  slug: open-polygon-dailybars-api
- collection_type: open
  name: Polygon Forex REST API
  slug: open-polygon-forex
- collection_type: open
  name: Polygon Indices REST API
  slug: open-polygon-indices
- collection_type: open
  name: Polygon Crypto REST Aggregates Markets API
  slug: open-polygon-markets-api
- collection_type: open
  name: Polygon Crypto REST Aggregates News API
  slug: open-polygon-news-api
- collection_type: open
  name: Polygon API
  slug: open-polygon-openapi-original
- collection_type: open
  name: Polygon Options REST API
  slug: open-polygon-options
- collection_type: open
  name: Polygon Crypto REST Aggregates Quotes API
  slug: open-polygon-quotes-api
- collection_type: open
  name: Polygon Reference REST API
  slug: open-polygon-reference
- collection_type: open
  name: Polygon Crypto REST Aggregates Snapshots API
  slug: open-polygon-snapshots-api
- collection_type: open
  name: Polygon Stocks REST API
  slug: open-polygon-stocks
- collection_type: open
  name: Polygon Crypto REST Aggregates Tickers API
  slug: open-polygon-tickers-api
common:
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/polygon-openapi-original.json
- group: other
  title: ''
  type: Overlay
  url: overlays/polygon-openapi-overlay.yaml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/polygon-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/polygon-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/polygon-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/polygon-well-known.yml
- group: build
  title: ''
  type: Packages
  url: packages/polygon-packages.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/polygon-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/polygon-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/polygon-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/polygon-changelog.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/polygon-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/polygon-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/polygon-data-model.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/polygon-scopes.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/polygon-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/polygon-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/polygon-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/polygon/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/polygon-corporate-actions-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/polygon-crypto-daily-comparison-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/polygon-crypto-pair-analysis-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/polygon-forex-pair-analysis-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/polygon-grouped-market-scan-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/polygon-index-analysis-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/polygon-market-gated-stock-daily-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/polygon-options-chain-scan-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/polygon-options-contract-deep-dive-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/polygon-stock-research-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/polygon-ticker-discovery-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/polygon-ticker-news-context-workflow.yml
- group: start
  title: ''
  type: Portal
  url: https://polygon.io/
- group: docs
  title: ''
  type: Documentation
  url: https://polygon.io/docs
- group: docs
  title: ''
  type: APIReference
  url: https://polygon.io/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://polygon.io/docs/getting-started
- group: start
  title: ''
  type: Signup
  url: https://polygon.io/dashboard/signup
- group: start
  title: ''
  type: Login
  url: https://polygon.io/dashboard/login
- group: commercial
  title: ''
  type: Pricing
  url: https://polygon.io/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.polygon.io/
- group: company
  title: ''
  type: Blog
  url: https://polygon.io/blog
- group: operate
  title: ''
  type: Support
  url: https://polygon.io/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://polygon.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://polygon.io/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/polygon-io
- group: build
  title: Official Polygon (Massive) MCP Server
  type: Tools
  url: https://github.com/polygon-io/mcp_polygon
- group: build
  title: Official PHP SDK
  type: SDKs
  url: https://github.com/polygon-io/client-php
- group: build
  title: Python SDK
  type: SDKs
  url: https://pypi.org/project/polygon-api-client/
- group: build
  title: JavaScript / TypeScript SDK
  type: SDKs
  url: https://www.npmjs.com/package/@polygon.io/client-js
- group: build
  title: Kotlin / JVM SDK
  type: SDKs
  url: https://central.sonatype.com/artifact/io.polygon.kotlin.sdk/polygon-kotlin-sdk-jvm
- group: build
  title: Go SDK
  type: SDKs
  url: https://pkg.go.dev/github.com/polygon-io/client-go
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/polygon-io
- group: commercial
  title: ''
  type: Plans
  url: plans/polygon-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/polygon-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/polygon-finops.yml
- group: design
  title: ''
  type: SpectralRules
  url: rules/polygon-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/polygon-vocabulary.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/polygon-context.jsonld
created: '2026-05-28'
description: Polygon (Polygon.io, rebranded as Massive in early 2026) provides real-time and historical market data APIs across US stocks, options, indices, forex, cryptocurrencies, and futures. Coverage is delivered through REST endpoints and WebSocket streams under a single api.polygon.io surface plus an S3 flat files product, with tiered subscription plans for retail developers and Business contracts for redistribution and exchange-licensed data.
examples:
- key_count: 2
  name: Polygon Forex Conversion Example
  slug: polygon-forex-conversion-example
- key_count: 2
  name: Polygon Options Chain Snapshot Example
  slug: polygon-options-chain-snapshot-example
- key_count: 2
  name: Polygon Reference Tickers Example
  slug: polygon-reference-tickers-example
- key_count: 2
  name: Polygon Stocks Aggregate Bars Example
  slug: polygon-stocks-aggregate-bars-example
- key_count: 3
  name: Polygon Websocket Subscribe Example
  slug: polygon-websocket-subscribe-example
features:
- description: Unified REST and WebSocket surface for stocks, options, indices, forex, crypto, and futures.
  name: Multi-asset market data
- description: Sub-second live feeds plus 20+ years of historical aggregates depending on tier.
  name: Real-time and historical
- description: Dedicated streaming clusters for stocks, options, indices, forex, and crypto subscriptions.
  name: WebSocket clusters per asset class
- description: S3-style daily aggregate, trade, and quote files for bulk historical loads on paid tiers.
  name: Flat files
- description: Basic / Starter / Developer / Advanced / Business plans per asset class with distinct rate limits.
  name: Tiered subscriptions
finops:
- name: Polygon Finops
  service_category: Fintech
  slug: polygon-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/polygon.png
integrations:
- description: Polygon data feeds integrate with charting libraries used by trading apps.
  name: TradingView
- description: Python SDK returns DataFrames for direct use in research notebooks.
  name: Pandas and DataFrames
- description: Flat files load into modern data warehouses for SQL-based market analytics.
  name: Snowflake and Databricks
- description: WebSocket feeds bridge into Kafka, Redpanda, and Kinesis for downstream processing.
  name: Kafka and streaming platforms
json_schemas:
- name: Polygon Aggregate Bar
  property_count: 9
  slug: polygon-aggregate-bar
- name: Polygon Options Contract
  property_count: 9
  slug: polygon-options-contract
- name: Polygon NBBO Quote Tick
  property_count: 9
  slug: polygon-quote
- name: Polygon Ticker
  property_count: 12
  slug: polygon-ticker
- name: Polygon Trade Tick
  property_count: 8
  slug: polygon-trade
json_structures:
- name: Polygon Aggregate Bar Structure
  property_count: 9
  slug: polygon-aggregate-bar-structure
- name: Polygon Options Contract Structure
  property_count: 9
  slug: polygon-options-contract-structure
- name: Polygon Ticker Structure
  property_count: 12
  slug: polygon-ticker-structure
jsonld:
- class_count: 10
  name: Polygon Context
  property_count: 40
  slug: polygon-context
layout: provider
mcp_servers:
- description: ''
  name: Massive MCP server — remote https://mcp.massive.com (OAuth) + open-source mcp_massive (stdio)
  slug: massive-mcp-server-remote-httpsmcpmassivecom-oauth-open-source-mcp-massive-stdio
modified: '2026-07-22'
name: Polygon
nav: Providers
network: true
overview: 'Polygon publishes 71 APIs on the [APIs.io](https://apis.io/) network, including WebSocket API, Aggregates API, Books API, and 68 more. Tagged areas include Finance, Fintech, Market Data, Stocks, and Options.


  The Polygon catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 3 Spectral governance rulesets.


  Polygon''s developer surface includes changelog, authentication, developer portal, documentation, API reference, getting-started guide, signup flow, and 51 more developer resources.'
plans:
- name: Polygon Plans Pricing
  plan_count: 12
  slug: polygon-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 6
  name: Polygon Rate Limits
  slug: polygon-rate-limits
rules:
- effective_rule_count: 32
  extends:
  - spectral:asyncapi
  name: Polygon API Rules
  rule_count: 5
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 4
  slug: polygon-asyncapi-spectral-rules
- effective_rule_count: 5
  extends: []
  name: Polygon API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: polygon-jsonschema-spectral-rules
- effective_rule_count: 62
  extends:
  - spectral:oas
  name: Polygon API Rules
  rule_count: 21
  severity_counts:
    error: 4
    hint: 0
    info: 4
    warn: 13
  slug: polygon-rules
scopes:
- name: Polygon Scopes
  scope_count: 6
  slug: polygon-scopes
  summary_line: 6 scopes · authorizationCode/clientCredentials
score:
  band: exemplar
  composite: 69.0
  coverage:
    artifact_dirs: 32
    catalog_gap: 20.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.9
  facets:
    access_clarity: 77.6
    commercial_clarity: 77.6
    contract_governance: 33.3
    contract_quality: 72.5
    developer_ergonomics: 56.5
    discoverability: 75.9
    governance: 33.3
    operational_transparency: 57.9
  previous_composite: 68.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 70
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 68.3
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/polygon/refs/heads/main/screenshots/polygon-2026-06-20T191902.png
security:
- kind: authentication
  name: Polygon Authentication
  slug: polygon-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Polygon Domain Security
  slug: polygon-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: polygon
solutions:
- description: Tiered plans for consumer-facing investing apps and personal-finance tools.
  name: Retail brokerages and fintech apps
- description: Business contracts for redistribution and full SIP / OPRA / CME exchange-licensed data.
  name: Quant funds and prop trading
- description: Flat files and historical APIs for ML feature engineering and financial NLP.
  name: Data and AI research
tags:
- Finance
- Fintech
- Market Data
- Stocks
- Options
- Forex
- Crypto
- Indices
- Futures
- WebSockets
- Real-Time
- Historical
- Public APIs
use_cases:
- description: Power retail and institutional trading UIs with consolidated real-time quotes and bars.
  name: Trading platform price feeds
- description: Pull decades of aggregated bars and tick data for systematic strategy research.
  name: Backtesting and research
- description: Stream live trades and quotes into compliance, surveillance, and risk engines.
  name: Risk and surveillance
- description: Build market dashboards, terminals, and embedded charts across asset classes.
  name: Analytics dashboards
- description: Drive options Greeks, volatility surfaces, and FX hedging models with reliable feeds.
  name: Quant pipelines
website: https://polygon.io/
---
