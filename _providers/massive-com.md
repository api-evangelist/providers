---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - scopes
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
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
    error_semantics: derived
    event_surface_described: derived
    idempotency: na
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: mostly
    pagination_ratio: paginated
    protected_resource_metadata: verified
    rate_limit_signal: derived
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 59.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Polygon Agentic Access
  operation_count: 175
  slug: polygon-agentic-access
  summary_line: 175 operations
api_count: 70
apis:
- baseURL: wss://socket.polygon.io
  baseurl_source: declared
  description: Real-time streaming WebSocket clusters per asset class (stocks/options/indices/forex/crypto). Subscribers authenticate with an API key and subscribe to channels for trades, quotes, aggregates, and boo
  name: Polygon WebSocket API
  slug: websocket-api
- baseURL: https://api.polygon.io
  baseurl_source: declared
  description: 'Real-time and historical US equity market data including aggregates (minute/hour/day bars), trades, NBBO quotes, snapshots, ticker reference, splits, dividends, and financials. Available via REST and '
  name: Polygon.io Stocks API
  slug: polygonio-stocks-api
- baseURL: https://api.polygon.io
  baseurl_source: declared
  description: 'OPRA-licensed options market data via REST and WebSocket: aggregates, trades, quotes, snapshots, contract reference, and option chains.'
  name: Polygon.io Options API
  slug: polygonio-options-api
- baseURL: https://api.polygon.io
  baseurl_source: declared
  description: Real-time and historical index values for major US and global indices via REST and WebSocket.
  name: Polygon.io Indices API
  slug: polygonio-indices-api
- baseURL: https://api.polygon.io
  baseurl_source: declared
  description: Real-time and historical FX prices for 1,000+ currency pairs via REST and WebSocket.
  name: Polygon.io Forex API
  slug: polygonio-forex-api
- baseURL: https://api.polygon.io
  baseurl_source: declared
  description: Aggregates, trades, snapshots, level-2 books, and L2 streaming for crypto pairs across major exchanges.
  name: Polygon.io Crypto API
  slug: polygonio-crypto-api
- baseURL: https://api.polygon.io
  baseurl_source: declared
  description: Real-time and historical futures market data including aggregates, trades, quotes, and snapshots.
  name: Polygon.io Futures API
  slug: polygonio-futures-api
- baseURL: wss://socket.polygon.io
  baseurl_source: declared
  description: The benzinga API from Massive (formerly Polygon.io) — 9 operation(s) for benzinga.
  name: Massive (formerly Polygon.io) Benzinga API
  phrasing_intents:
  - id: get_benzinga_v1_analyst-insights
    intent: Browse analyst insights and rating calls
    question: Where can I read analyst insights behind recent rating calls on a stock?
  - id: get_benzinga_v1_analysts
    intent: Look up financial analysts and their track records
    question: Which analysts work at a particular research firm, and how accurate are they?
  - id: get_benzinga_v1_bulls-bears-say
    intent: Get bull and bear case summaries for a stock
    question: What are the bullish and bearish arguments analysts make about a stock?
  - id: get_benzinga_v1_consensus-ratings_ticker
    intent: Get a stock's consensus analyst rating
    question: What is the Wall Street consensus rating and average price target for a stock?
  - id: get_benzinga_v1_earnings
    intent: Get company earnings results and estimates
    question: When does a company report earnings and what EPS is expected?
  - id: get_benzinga_v1_firms
    intent: List financial research firms
    question: Which brokerage and research firms are covered in the analyst ratings data?
  - id: get_benzinga_v1_guidance
    intent: Get company earnings and revenue guidance
    question: What EPS and revenue guidance has a company given for the coming fiscal year?
  - id: get_benzinga_v1_ratings
    intent: Track analyst upgrades, downgrades and price targets
    question: Which analysts upgraded or downgraded a stock this week?
  phrasing_ops: 9
  slug: massive-com-benzinga-api
- baseURL: wss://socket.polygon.io
  baseurl_source: declared
  description: The crypto:aggregates API from Massive (formerly Polygon.io) — 7 operation(s) for crypto:aggregates.
  name: Massive (formerly Polygon.io) Crypto:aggregates API
  phrasing_intents:
  - id: CryptoEMA
    intent: Get the exponential moving average of a crypto pair
    question: What is the exponential moving average of Bitcoin over the last few weeks?
  - id: CryptoMACD
    intent: Get MACD for a crypto pair
    question: Is MACD showing a bullish crossover on Ethereum?
  - id: CryptoRSI
    intent: Get the relative strength index of a crypto pair
    question: Is a cryptocurrency overbought or oversold according to RSI?
  - id: CryptoSMA
    intent: Get the simple moving average of a crypto pair
    question: What's the 50-day simple moving average of a crypto pair?
  - id: GetGroupedCryptoAggregates
    intent: Get daily OHLC for every crypto pair
    question: Can I get the open, high, low and close for the whole crypto market on one day?
  - id: GetPreviousCryptoAggregates
    intent: Get a crypto pair's previous-day OHLC
    question: What was yesterday's open, high, low and close for a crypto pair?
  - id: GetCryptoAggregates
    intent: Get crypto price bars over a date range
    question: Can I get 5-minute candles for a crypto pair across a date range?
  phrasing_ops: 7
  slug: massive-com-crypto-aggregates-api
- baseURL: wss://socket.polygon.io
  baseurl_source: declared
  description: The crypto:last:trade API from Massive (formerly Polygon.io) — 1 operation(s) for crypto:last:trade.
  name: Massive (formerly Polygon.io) Crypto:last:trade API
  phrasing_intents:
  - id: LastTradeCrypto
    intent: Get the last trade for a crypto pair
    question: What was the most recent trade price for Bitcoin in US dollars?
  phrasing_ops: 1
  slug: massive-com-crypto-last-trade-api
- baseURL: wss://socket.polygon.io
  baseurl_source: declared
  description: The crypto:open-close API from Massive (formerly Polygon.io) — 1 operation(s) for crypto:open-close.
  name: Massive (formerly Polygon.io) Crypto:open Close API
  phrasing_intents:
  - id: GetCryptoOpenClose
    intent: Get a crypto pair's open and close for a day
    question: What were a cryptocurrency's opening and closing prices on a specific day?
  phrasing_ops: 1
  slug: massive-com-crypto-open-close-api
- baseURL: wss://socket.polygon.io
  baseurl_source: declared
  description: The crypto:snapshot API from Massive (formerly Polygon.io) — 4 operation(s) for crypto:snapshot.
  name: Massive (formerly Polygon.io) Crypto:snapshot API
  phrasing_intents:
  - id: GetCryptoSnapshotTickers
    intent: Snapshot all traded crypto tickers
    question: Can I get current prices for every traded cryptocurrency in one call?
  - id: GetCryptoSnapshotTicker
    intent: Snapshot a single crypto ticker
    question: What's the current day bar, last trade and quote for one crypto ticker?
  - id: DeprecatedGetCryptoSnapshotTickerBook
    intent: Get the level 2 order book for a crypto ticker
    question: Can I see the full L2 order book combined across exchanges for a crypto ticker?
  - id: GetCryptoSnapshotDirection
    intent: Get today's top crypto gainers or losers
    question: Which cryptocurrencies are up the most today?
  phrasing_ops: 4
  slug: massive-com-crypto-snapshot-api
- baseURL: wss://socket.polygon.io
  baseurl_source: declared
  description: The crypto:trades API from Massive (formerly Polygon.io) — 2 operation(s) for crypto:trades.
  name: Massive (formerly Polygon.io) Crypto:trades API
  phrasing_intents:
  - id: DeprecatedGetHistoricCryptoTrades
    intent: Get a crypto pair's trades on one day (legacy)
    question: Can I pull historic trade ticks for a crypto pair on a single date with the older v1 endpoint?
  - id: TradesCrypto
    intent: Get crypto trades over a time range
    question: What trades printed for a crypto ticker between two timestamps?
  phrasing_ops: 2
  slug: massive-com-crypto-trades-api
- baseURL: wss://socket.polygon.io
  baseurl_source: declared
  description: The etfglobal API from Massive (formerly Polygon.io) — 5 operation(s) for etfglobal.
  name: Massive (formerly Polygon.io) Etfglobal API
  phrasing_intents:
  - id: get_etf-global_v1_analytics
    intent: Get ETF risk, reward and quant scores
    question: How risky is an ETF according to its quantitative risk score?
  - id: get_etf-global_v1_constituents
    intent: List the holdings inside an ETF
    question: What stocks does an ETF hold and at what weights?
  - id: get_etf-global_v1_fund-flows
    intent: Get ETF fund flows and NAV
    question: Is money flowing into or out of an ETF?
  - id: get_etf-global_v1_profiles
    intent: Get an ETF's profile and metadata
    question: What are an ETF's key financial and operational details, like issuer and exposure?
  - id: get_etf-global_v1_taxonomies
    intent: Get an ETF's strategy classification
    question: How is an ETF classified by investment strategy and methodology?
  phrasing_ops: 5
  slug: massive-com-etfglobal-api
- baseURL: wss://socket.polygon.io
  baseurl_source: declared
  description: The fable API from Massive (formerly Polygon.io) — 2 operation(s) for fable.
  name: Massive (formerly Polygon.io) Fable API
  phrasing_intents:
  - id: get_consumer-spending_eu_v1_merchant-aggregates
    intent: Get European consumer spending by merchant
    question: How much are European consumers spending at a given merchant each day?
  - id: get_consumer-spending_eu_v1_merchant-hierarchy
    intent: Map European merchants to parent companies
    question: Which parent company and stock ticker does a European merchant belong to?
  phrasing_ops: 2
  slug: massive-com-fable-api
- baseURL: wss://socket.polygon.io
  baseurl_source: declared
  description: The fed API from Massive (formerly Polygon.io) — 4 operation(s) for fed.
  name: Massive (formerly Polygon.io) Fed API
  phrasing_intents:
  - id: get_fed_v1_inflation
    intent: Get CPI and PCE inflation data
    question: What is the latest CPI inflation reading?
  - id: get_fed_v1_inflation-expectations
    intent: Get market and model inflation expectations
    question: What do markets expect inflation to be over the next five or ten years?
  - id: get_fed_v1_labor-market
    intent: Get labor market indicators
    question: What's the current US unemployment rate?
  - id: get_fed_v1_treasury-yields
    intent: Get US Treasury yields by maturity
    question: What's the 10-year Treasury yield today?
  phrasing_ops: 4
  slug: massive-com-fed-api
- baseURL: wss://socket.polygon.io
  baseurl_source: declared
  description: The financials API from Massive (formerly Polygon.io) — 4 operation(s) for financials.
  name: Massive (formerly Polygon.io) Financials API
  phrasing_intents:
  - id: get_stocks_financials_v1_balance-sheets
    intent: Get a company's balance sheets
    question: What are a company's total assets, liabilities and equity?
  - id: get_stocks_financials_v1_cash-flow-statements
    intent: Get a company's cash flow statements
    question: How much operating cash flow did a company generate?
  - id: get_stocks_financials_v1_income-statements
    intent: Get a company's income statements
    question: What were a company's revenue and net income last quarter?
  - id: get_stocks_financials_v1_ratios
    intent: Screen stocks by financial ratios
    question: What is a stock's P/E, price-to-book and debt-to-equity ratio?
  phrasing_ops: 4
  slug: massive-com-financials-api
- baseURL: wss://socket.polygon.io
  baseurl_source: declared
  description: The futures:aggregates API from Massive (formerly Polygon.io) — 1 operation(s) for futures:aggregates.
  name: Massive (formerly Polygon.io) Futures:aggregates API
  phrasing_intents:
  - id: AggregatesV1
    intent: Get price bars for a futures contract
    question: Can I get OHLC bars for a futures contract over a time window?
  phrasing_ops: 1
  slug: massive-com-futures-aggregates-api
- baseURL: wss://socket.polygon.io
  baseurl_source: declared
  description: The fx:aggregates API from Massive (formerly Polygon.io) — 7 operation(s) for fx:aggregates.
  name: Massive (formerly Polygon.io) Fx:aggregates API
  phrasing_intents:
  - id: ForexEMA
    intent: Get the exponential moving average of a forex pair
    question: What's the exponential moving average of EUR/USD on hourly bars?
  - id: ForexMACD
    intent: Get MACD for a forex pair
    question: Is the MACD histogram turning positive on a currency pair?
  - id: ForexRSI
    intent: Get the relative strength index of a forex pair
    question: Is a currency pair overbought on the RSI?
  - id: ForexSMA
    intent: Get the simple moving average of a forex pair
    question: What's the 200-day simple moving average for a currency pair?
  - id: GetGroupedForexAggregates
    intent: Get daily OHLC for every forex pair
    question: Can I download one day's open, high, low and close for all currency pairs?
  - id: GetPreviousForexAggregates
    intent: Get a forex pair's previous-day OHLC
    question: Where did a currency pair close yesterday?
  - id: GetForexAggregates
    intent: Get forex price bars over a date range
    question: Can I get 15-minute candles for a currency pair across a date range?
  phrasing_ops: 7
  slug: massive-com-fx-aggregates-api
- baseURL: wss://socket.polygon.io
  baseurl_source: declared
  description: The fx:conversion API from Massive (formerly Polygon.io) — 1 operation(s) for fx:conversion.
  name: Massive (formerly Polygon.io) Fx:conversion API
  phrasing_intents:
  - id: RealTimeCurrencyConversion
    intent: Convert an amount between two currencies
    question: How many Canadian dollars is 100 US dollars right now?
  phrasing_ops: 1
  slug: massive-com-fx-conversion-api
- baseURL: wss://socket.polygon.io
  baseurl_source: declared
  description: The fx:last:quote API from Massive (formerly Polygon.io) — 1 operation(s) for fx:last:quote.
  name: Massive (formerly Polygon.io) Fx:last:quote API
  phrasing_intents:
  - id: LastQuoteCurrencies
    intent: Get the latest quote for a currency pair
    question: What's the current bid and ask for EUR/USD?
  phrasing_ops: 1
  slug: massive-com-fx-last-quote-api
- baseURL: wss://socket.polygon.io
  baseurl_source: declared
  description: The fx:quotes API from Massive (formerly Polygon.io) — 1 operation(s) for fx:quotes.
  name: Massive (formerly Polygon.io) Fx:quotes API
  phrasing_intents:
  - id: QuotesFx
    intent: Get forex BBO quotes over a time range
    question: Can I get the best bid and offer history for a currency pair?
  phrasing_ops: 1
  slug: massive-com-fx-quotes-api
- baseURL: wss://socket.polygon.io
  baseurl_source: declared
  description: The fx:snapshot API from Massive (formerly Polygon.io) — 3 operation(s) for fx:snapshot.
  name: Massive (formerly Polygon.io) Fx:snapshot API
  phrasing_intents:
  - id: GetForexSnapshotTickers
    intent: Snapshot all traded forex pairs
    question: Can I get the latest price for every currency pair at once?
  - id: GetForexSnapshotTicker
    intent: Snapshot a single forex pair
    question: What's the current day bar and last quote for one currency pair?
  - id: GetForexSnapshotDirection
    intent: Get today's top forex gainers or losers
    question: Which currency pairs have gained the most today?
  phrasing_ops: 3
  slug: massive-com-fx-snapshot-api
- baseURL: wss://socket.polygon.io
  baseurl_source: declared
  description: The fx:trades API from Massive (formerly Polygon.io) — 1 operation(s) for fx:trades.
  name: Massive (formerly Polygon.io) Fx:trades API
  phrasing_intents:
  - id: DeprecatedGetHistoricForexQuotes
    intent: Get historic forex ticks for a day (legacy)
    question: Can I pull a currency pair's historic ticks for one date from the older v1 endpoint?
  phrasing_ops: 1
  slug: massive-com-fx-trades-api
- baseURL: wss://socket.polygon.io
  baseurl_source: declared
  description: The global_crypto API from Massive (formerly Polygon.io) — 1 operation(s) for global_crypto.
  name: Massive (formerly Polygon.io) Global Crypto API
  phrasing_intents:
  - id: get_crypto_v1_exchanges
    intent: List global crypto exchanges
    question: Which cryptocurrency exchanges are covered in the market data?
  phrasing_ops: 1
  slug: massive-com-global-crypto-api
- baseURL: wss://socket.polygon.io
  baseurl_source: declared
  description: The global_forex API from Massive (formerly Polygon.io) — 1 operation(s) for global_forex.
  name: Massive (formerly Polygon.io) Global Forex API
  phrasing_intents:
  - id: get_forex_v1_exchanges
    intent: List global forex trading venues
    question: Which foreign exchange trading venues supply currency data?
  phrasing_ops: 1
  slug: massive-com-global-forex-api
- baseURL: wss://socket.polygon.io
  baseurl_source: declared
  description: The indices:aggregates API from Massive (formerly Polygon.io) — 6 operation(s) for indices:aggregates.
  name: Massive (formerly Polygon.io) Indices:aggregates API
  phrasing_intents:
  - id: IndicesEMA
    intent: Get the exponential moving average of an index
    question: What's the exponential moving average of the S&P 500 index?
  - id: IndicesMACD
    intent: Get MACD for an index
    question: Is MACD signaling a trend change on the Nasdaq-100 index?
  - id: IndicesRSI
    intent: Get the relative strength index of an index
    question: Is the broad market index overbought on RSI?
  - id: IndicesSMA
    intent: Get the simple moving average of an index
    question: Is an index trading above its 200-day simple moving average?
  - id: GetPreviousIndicesAggregates
    intent: Get an index's previous-day OHLC
    question: Where did an index close on the prior trading day?
  - id: GetIndicesAggregates
    intent: Get index value bars over a date range
    question: Can I get hourly bars for an index across a date range?
  phrasing_ops: 6
  slug: massive-com-indices-aggregates-api
- baseURL: wss://socket.polygon.io
  baseurl_source: declared
  description: The indices:snapshot API from Massive (formerly Polygon.io) — 1 operation(s) for indices:snapshot.
  name: Massive (formerly Polygon.io) Indices:snapshot API
  phrasing_intents:
  - id: IndicesSnapshot
    intent: Snapshot current index values
    question: What's the current value of the major market indices?
  phrasing_ops: 1
  slug: massive-com-indices-snapshot-api
- baseURL: https://api.polygon.io
  baseurl_source: declared
  description: Markets, exchanges, holidays, and status.
  name: Massive (formerly Polygon.io) Markets API
  phrasing_intents:
  - id: listMarkets
    intent: List supported markets
    question: Which markets are supported for data?
  - id: listExchanges
    intent: List exchanges by asset class
    question: Which exchanges are listed for stocks or options?
  - id: listUpcomingMarketHolidays
    intent: List upcoming US market holidays
    question: When is the next US stock market holiday?
  - id: getCurrentMarketStatus
    intent: Check whether US markets are open now
    question: Is the US stock market open right now?
  phrasing_ops: 4
  slug: massive-com-markets-api
- baseURL: https://api.polygon.io
  baseurl_source: declared
  description: Ticker news.
  name: Massive (formerly Polygon.io) News API
  phrasing_intents:
  - id: listTickerNews
    intent: List news articles for a ticker
    question: What's the latest news about a stock?
  phrasing_ops: 1
  slug: massive-com-news-api
- baseURL: wss://socket.polygon.io
  baseurl_source: declared
  description: The options:aggregates API from Massive (formerly Polygon.io) — 6 operation(s) for options:aggregates.
  name: Massive (formerly Polygon.io) Options:aggregates API
  phrasing_intents:
  - id: OptionsEMA
    intent: Get the exponential moving average of an option
    question: What's the exponential moving average of an options contract's price?
  - id: OptionsMACD
    intent: Get MACD for an options contract
    question: Is an option's price momentum turning according to MACD?
  - id: OptionsRSI
    intent: Get the relative strength index of an option
    question: Is an options contract overbought on the RSI?
  - id: OptionsSMA
    intent: Get the simple moving average of an option
    question: What's the simple moving average of an options contract's price?
  - id: GetPreviousOptionsAggregates
    intent: Get an option's previous-day OHLC
    question: What did an options contract close at yesterday?
  - id: GetOptionsAggregates
    intent: Get option price bars over a date range
    question: Can I get minute bars for an option contract across several days?
  phrasing_ops: 6
  slug: massive-com-options-aggregates-api
- baseURL: wss://socket.polygon.io
  baseurl_source: declared
  description: The options:last:trade API from Massive (formerly Polygon.io) — 1 operation(s) for options:last:trade.
  name: Massive (formerly Polygon.io) Options:last:trade API
  phrasing_intents:
  - id: LastTradeOptions
    intent: Get the last trade for an options contract
    question: What was the most recent trade price for an options contract?
  phrasing_ops: 1
  slug: massive-com-options-last-trade-api
- baseURL: wss://socket.polygon.io
  baseurl_source: declared
  description: The options:open-close API from Massive (formerly Polygon.io) — 1 operation(s) for options:open-close.
  name: Massive (formerly Polygon.io) Options:open Close API
  phrasing_intents:
  - id: GetOptionsOpenClose
    intent: Get an option's open, close and after-hours prices
    question: What were an options contract's open and close prices on a past date?
  phrasing_ops: 1
  slug: massive-com-options-open-close-api
- baseURL: wss://socket.polygon.io
  baseurl_source: declared
  description: The options:quotes API from Massive (formerly Polygon.io) — 1 operation(s) for options:quotes.
  name: Massive (formerly Polygon.io) Options:quotes API
  phrasing_intents:
  - id: QuotesOptions
    intent: Get quotes for an options contract over time
    question: What bid and ask quotes did an options contract have during the day?
  phrasing_ops: 1
  slug: massive-com-options-quotes-api
- baseURL: wss://socket.polygon.io
  baseurl_source: declared
  description: The options:snapshot API from Massive (formerly Polygon.io) — 2 operation(s) for options:snapshot.
  name: Massive (formerly Polygon.io) Options:snapshot API
  phrasing_intents:
  - id: OptionsChain
    intent: Get the options chain for an underlying
    question: What does the full options chain look like for a stock?
  - id: OptionContract
    intent: Snapshot a single option contract
    question: What does the latest market snapshot show for one specific option contract?
  phrasing_ops: 2
  slug: massive-com-options-snapshot-api
- baseURL: wss://socket.polygon.io
  baseurl_source: declared
  description: The options:trades API from Massive (formerly Polygon.io) — 1 operation(s) for options:trades.
  name: Massive (formerly Polygon.io) Options:trades API
  phrasing_intents:
  - id: TradesOptions
    intent: Get trades for an options contract over time
    question: What trades printed for an options contract today?
  phrasing_ops: 1
  slug: massive-com-options-trades-api
- baseURL: wss://socket.polygon.io
  baseurl_source: declared
  description: Reference API
  name: Massive (formerly Polygon.io) Reference API
  phrasing_intents:
  - id: get_stocks_filings_10-K_vX_sections
    intent: Read sections of 10-K filings (vX)
    question: Can I pull the raw text of a specific section, like risk factors or MD&A, from a company's 10-K?
  - id: get_stocks_filings_10-K_vX_0_sections
    intent: Read sections of 10-K filings (vX_0 variant)
    question: Is there a vX_0 version of the 10-K sections endpoint I can call instead?
  - id: get_stocks_filings_8-K_vX_disclosures
    intent: Get categorized 8-K disclosures
    question: What kind of material event did a company disclose in its latest 8-K?
  - id: get_stocks_filings_8-K_vX_text
    intent: Read the text of 8-K current reports
    question: Can I read the full parsed text of a company's 8-K about an acquisition or executive change?
  - id: get_stocks_filings_vX_13-F
    intent: Get institutional 13F holdings filings
    question: What stocks does a large institutional investment manager hold?
  - id: get_stocks_filings_vX_form-3
    intent: Get Form 3 initial insider ownership filings
    question: Who became a new insider at a company and filed an initial ownership statement?
  - id: get_stocks_filings_vX_form-4
    intent: Get Form 4 insider transaction filings
    question: Have any executives bought or sold shares of a stock recently?
  - id: get_stocks_filings_vX_index
    intent: Search the SEC EDGAR filings index
    question: Where can I find links to every SEC filing a company has made?
  phrasing_ops: 14
  slug: massive-com-reference-api
- baseURL: wss://socket.polygon.io
  baseurl_source: declared
  description: The reference:conditions API from Massive (formerly Polygon.io) — 1 operation(s) for reference:conditions.
  name: Massive (formerly Polygon.io) Reference:conditions API
  phrasing_intents:
  - id: ListConditions
    intent: List trade and quote condition codes
    question: What does a trade condition code on a tick mean?
  phrasing_ops: 1
  slug: massive-com-reference-conditions-api
- baseURL: wss://socket.polygon.io
  baseurl_source: declared
  description: The reference:dividends API from Massive (formerly Polygon.io) — 1 operation(s) for reference:dividends.
  name: Massive (formerly Polygon.io) Reference:dividends API
  phrasing_intents:
  - id: ListDividends
    intent: List historical cash dividends
    question: What dividends has a stock paid, and when was each ex-dividend date?
  phrasing_ops: 1
  slug: massive-com-reference-dividends-api
- baseURL: wss://socket.polygon.io
  baseurl_source: declared
  description: The reference:exchanges API from Massive (formerly Polygon.io) — 1 operation(s) for reference:exchanges.
  name: Massive (formerly Polygon.io) Reference:exchanges API
  phrasing_intents:
  - id: ListExchanges
    intent: List known exchanges
    question: Which exchanges does the market data cover?
  phrasing_ops: 1
  slug: massive-com-reference-exchanges-api
- baseURL: wss://socket.polygon.io
  baseurl_source: declared
  description: The reference:news API from Massive (formerly Polygon.io) — 1 operation(s) for reference:news.
  name: Massive (formerly Polygon.io) Reference:news API
  phrasing_intents:
  - id: ListNews
    intent: Get recent news articles about a stock
    question: What are the most recent news stories about a company?
  phrasing_ops: 1
  slug: massive-com-reference-news-api
- baseURL: wss://socket.polygon.io
  baseurl_source: declared
  description: The reference:options:contract API from Massive (formerly Polygon.io) — 1 operation(s) for reference:options:contract.
  name: Massive (formerly Polygon.io) Reference:options:contract API
  phrasing_intents:
  - id: GetOptionsContract
    intent: Get details for one options contract
    question: What are the strike, expiration and type of a specific options contract?
  phrasing_ops: 1
  slug: massive-com-reference-options-contract-api
- baseURL: wss://socket.polygon.io
  baseurl_source: declared
  description: The reference:options:contracts:list API from Massive (formerly Polygon.io) — 1 operation(s) for reference:options:contracts:list.
  name: Massive (formerly Polygon.io) Reference:options:contracts:list API
  phrasing_intents:
  - id: ListOptionsContracts
    intent: Search active and expired options contracts
    question: Which options contracts exist on a stock, including expired ones?
  phrasing_ops: 1
  slug: massive-com-reference-options-contracts-list-api
- baseURL: wss://socket.polygon.io
  baseurl_source: declared
  description: The reference:related:companies API from Massive (formerly Polygon.io) — 1 operation(s) for reference:related:companies.
  name: Massive (formerly Polygon.io) Reference:related:companies API
  phrasing_intents:
  - id: GetRelatedCompanies
    intent: Find companies related to a ticker
    question: Which companies are related to a stock based on news and returns?
  phrasing_ops: 1
  slug: massive-com-reference-related-companies-api
- baseURL: wss://socket.polygon.io
  baseurl_source: declared
  description: The reference:sec:filing API from Massive (formerly Polygon.io) — 1 operation(s) for reference:sec:filing.
  name: Massive (formerly Polygon.io) Reference:sec:filing API
  phrasing_intents:
  - id: GetFiling
    intent: Get one SEC filing
    question: Can I look up a single SEC filing by its ID?
  phrasing_ops: 1
  slug: massive-com-reference-sec-filing-api
- baseURL: wss://socket.polygon.io
  baseurl_source: declared
  description: The reference:sec:filing:file API from Massive (formerly Polygon.io) — 1 operation(s) for reference:sec:filing:file.
  name: Massive (formerly Polygon.io) Reference:sec:filing:file API
  phrasing_intents:
  - id: GetFilingFile
    intent: Get one file from an SEC filing
    question: Can I fetch a specific document attached to an SEC filing?
  phrasing_ops: 1
  slug: massive-com-reference-sec-filing-file-api
- baseURL: wss://socket.polygon.io
  baseurl_source: declared
  description: The reference:sec:filing:files API from Massive (formerly Polygon.io) — 1 operation(s) for reference:sec:filing:files.
  name: Massive (formerly Polygon.io) Reference:sec:filing:files API
  phrasing_intents:
  - id: ListFilingFiles
    intent: List the files in an SEC filing
    question: What documents are included in an SEC filing?
  phrasing_ops: 1
  slug: massive-com-reference-sec-filing-files-api
- baseURL: wss://socket.polygon.io
  baseurl_source: declared
  description: The reference:sec:filings API from Massive (formerly Polygon.io) — 1 operation(s) for reference:sec:filings.
  name: Massive (formerly Polygon.io) Reference:sec:filings API
  phrasing_intents:
  - id: ListFilings
    intent: Search SEC filings
    question: Which SEC filings has a company submitted recently?
  phrasing_ops: 1
  slug: massive-com-reference-sec-filings-api
- baseURL: wss://socket.polygon.io
  baseurl_source: declared
  description: The reference:stocks API from Massive (formerly Polygon.io) — 2 operation(s) for reference:stocks.
  name: Massive (formerly Polygon.io) Reference:stocks API
  phrasing_intents:
  - id: ListStockSplits
    intent: List historical stock splits
    question: When did a company last split its stock, and at what ratio?
  - id: ListFinancials
    intent: Get XBRL financials from SEC filings
    question: What financial statements did a company report in its SEC filings?
  phrasing_ops: 2
  slug: massive-com-reference-stocks-api
- baseURL: wss://socket.polygon.io
  baseurl_source: declared
  description: The reference:stocks:ipos API from Massive (formerly Polygon.io) — 1 operation(s) for reference:stocks:ipos.
  name: Massive (formerly Polygon.io) Reference:stocks:ipos API
  phrasing_intents:
  - id: ListIPOs
    intent: List upcoming and past IPOs
    question: Which companies are going public soon?
  phrasing_ops: 1
  slug: massive-com-reference-stocks-ipos-api
- baseURL: wss://socket.polygon.io
  baseurl_source: declared
  description: The reference:stocks:market API from Massive (formerly Polygon.io) — 2 operation(s) for reference:stocks:market.
  name: Massive (formerly Polygon.io) Reference:stocks:market API
  phrasing_intents:
  - id: GetMarketStatus
    intent: Check current market status
    question: Are the exchanges open for trading right now?
  - id: GetMarketHolidays
    intent: List upcoming market holidays
    question: When is the market closed next for a holiday?
  phrasing_ops: 2
  slug: massive-com-reference-stocks-market-api
- baseURL: wss://socket.polygon.io
  baseurl_source: declared
  description: The reference:tickers:get API from Massive (formerly Polygon.io) — 2 operation(s) for reference:tickers:get.
  name: Massive (formerly Polygon.io) Reference:tickers:get API
  phrasing_intents:
  - id: GetTicker
    intent: Get detailed information about a ticker
    question: What company is behind a ticker, and what are its key details?
  - id: GetEvents
    intent: Get a timeline of ticker events
    question: Has a company changed its ticker symbol over time?
  phrasing_ops: 2
  slug: massive-com-reference-tickers-get-api
- baseURL: wss://socket.polygon.io
  baseurl_source: declared
  description: The reference:tickers:list API from Massive (formerly Polygon.io) — 1 operation(s) for reference:tickers:list.
  name: Massive (formerly Polygon.io) Reference:tickers:list API
  phrasing_intents:
  - id: ListTickers
    intent: Search supported ticker symbols
    question: What ticker symbols are available for stocks, indices, forex and crypto?
  phrasing_ops: 1
  slug: massive-com-reference-tickers-list-api
- baseURL: wss://socket.polygon.io
  baseurl_source: declared
  description: The reference:tickers:types API from Massive (formerly Polygon.io) — 1 operation(s) for reference:tickers:types.
  name: Massive (formerly Polygon.io) Reference:tickers:types API
  phrasing_intents:
  - id: ListTickerTypes
    intent: List ticker types
    question: What types of tickers are there, like common stock, ETF or warrant?
  phrasing_ops: 1
  slug: massive-com-reference-tickers-types-api
- baseURL: wss://socket.polygon.io
  baseurl_source: declared
  description: The Snapshot API from Massive (formerly Polygon.io) — 1 operation(s) for snapshot.
  name: Massive (formerly Polygon.io) Snapshot API
  phrasing_intents:
  - id: Snapshots
    intent: Snapshot assets of any type
    question: Can I get snapshots for stocks, options, forex and crypto in one request?
  phrasing_ops: 1
  slug: massive-com-snapshot-api
- baseURL: wss://socket.polygon.io
  baseurl_source: declared
  description: The stocks:aggregates API from Massive (formerly Polygon.io) — 7 operation(s) for stocks:aggregates.
  name: Massive (formerly Polygon.io) Stocks:aggregates API
  phrasing_intents:
  - id: EMA
    intent: Get the exponential moving average of a stock
    question: What's the 20-day exponential moving average for Apple stock?
  - id: MACD
    intent: Get MACD for a stock
    question: Has a stock's MACD line crossed above its signal line?
  - id: RSI
    intent: Get the relative strength index of a stock
    question: Is a stock overbought or oversold on the RSI?
  - id: SMA
    intent: Get the simple moving average of a stock
    question: Is a stock trading above its 200-day simple moving average?
  - id: GetGroupedStocksAggregates
    intent: Get daily OHLC for every US stock
    question: Can I get the open, high, low and close for every US stock on one day?
  - id: GetPreviousStocksAggregates
    intent: Get a stock's previous-day OHLC
    question: What did a stock close at yesterday?
  - id: GetStocksAggregates
    intent: Get stock price bars over a date range
    question: Can I get 5-minute candles for a stock across a date range?
  phrasing_ops: 7
  slug: massive-com-stocks-aggregates-api
- baseURL: wss://socket.polygon.io
  baseurl_source: declared
  description: The stocks:last:quote API from Massive (formerly Polygon.io) — 1 operation(s) for stocks:last:quote.
  name: Massive (formerly Polygon.io) Stocks:last:quote API
  phrasing_intents:
  - id: LastQuote
    intent: Get the latest NBBO quote for a stock
    question: What's the current national best bid and offer for a stock?
  phrasing_ops: 1
  slug: massive-com-stocks-last-quote-api
- baseURL: wss://socket.polygon.io
  baseurl_source: declared
  description: The stocks:last:trade API from Massive (formerly Polygon.io) — 1 operation(s) for stocks:last:trade.
  name: Massive (formerly Polygon.io) Stocks:last:trade API
  phrasing_intents:
  - id: LastTrade
    intent: Get the latest trade for a stock
    question: What price did a stock last trade at?
  phrasing_ops: 1
  slug: massive-com-stocks-last-trade-api
- baseURL: wss://socket.polygon.io
  baseurl_source: declared
  description: The stocks:open-close API from Massive (formerly Polygon.io) — 2 operation(s) for stocks:open-close.
  name: Massive (formerly Polygon.io) Stocks:open Close API
  phrasing_intents:
  - id: GetIndicesOpenClose
    intent: Get an index's open, close and after-hours values
    question: What were a market index's opening and closing values on a specific date?
  - id: GetStocksOpenClose
    intent: Get a stock's open, close and after-hours prices
    question: What were a stock's opening and closing prices on a given day?
  phrasing_ops: 2
  slug: massive-com-stocks-open-close-api
- baseURL: wss://socket.polygon.io
  baseurl_source: declared
  description: The stocks:quotes API from Massive (formerly Polygon.io) — 2 operation(s) for stocks:quotes.
  name: Massive (formerly Polygon.io) Stocks:quotes API
  phrasing_intents:
  - id: DeprecatedGetHistoricStocksQuotes
    intent: Get a stock's NBBO quotes for one day (legacy v2)
    question: Can I pull a day of NBBO quotes for a stock from the older v2 ticks endpoint?
  - id: Quotes
    intent: Get a stock's NBBO quotes over a time range
    question: What were a stock's best bid and offer quotes between two timestamps?
  phrasing_ops: 2
  slug: massive-com-stocks-quotes-api
- baseURL: wss://socket.polygon.io
  baseurl_source: declared
  description: The stocks:snapshot API from Massive (formerly Polygon.io) — 3 operation(s) for stocks:snapshot.
  name: Massive (formerly Polygon.io) Stocks:snapshot API
  phrasing_intents:
  - id: GetStocksSnapshotTickers
    intent: Snapshot all US stock tickers
    question: Can I get up-to-date market data for every traded US stock at once?
  - id: GetStocksSnapshotTicker
    intent: Snapshot a single US stock
    question: What's the most up-to-date market data for one stock?
  - id: GetStocksSnapshotDirection
    intent: Get today's top stock gainers or losers
    question: Which stocks are the biggest gainers today?
  phrasing_ops: 3
  slug: massive-com-stocks-snapshot-api
- baseURL: wss://socket.polygon.io
  baseurl_source: declared
  description: The stocks:trades API from Massive (formerly Polygon.io) — 2 operation(s) for stocks:trades.
  name: Massive (formerly Polygon.io) Stocks:trades API
  phrasing_intents:
  - id: DeprecatedGetHistoricStocksTrades
    intent: Get a stock's trades for one day (legacy v2)
    question: Can I pull all trades for a stock on one date from the older v2 ticks endpoint?
  - id: Trades
    intent: Get a stock's trades over a time range
    question: What trades printed in a stock between two timestamps?
  phrasing_ops: 2
  slug: massive-com-stocks-trades-api
- baseURL: wss://socket.polygon.io
  baseurl_source: declared
  description: The Summaries API from Massive (formerly Polygon.io) — 1 operation(s) for summaries.
  name: Massive (formerly Polygon.io) Summaries API
  phrasing_intents:
  - id: SnapshotSummary
    intent: Get price summaries for a list of tickers
    question: Can I get everything needed to chart the tick-by-tick movement of several tickers?
  phrasing_ops: 1
  slug: massive-com-summaries-api
- baseURL: https://api.polygon.io
  baseurl_source: declared
  description: Ticker reference and metadata.
  name: Massive (formerly Polygon.io) Tickers API
  phrasing_intents:
  - id: listTickers
    intent: List supported ticker symbols
    question: Which ticker symbols are supported across asset classes?
  - id: getTickerDetails
    intent: Get reference details for one ticker
    question: What reference information is available for a single ticker symbol?
  - id: listTickerTypes
    intent: List the kinds of ticker types
    question: What ticker types exist, such as common stock or ETF?
  phrasing_ops: 3
  slug: massive-com-tickers-api
- baseURL: wss://socket.polygon.io
  baseurl_source: declared
  description: The tmx API from Massive (formerly Polygon.io) — 1 operation(s) for tmx.
  name: Massive (formerly Polygon.io) Tmx API
  phrasing_intents:
  - id: get_tmx_v1_corporate-events
    intent: Get corporate events from TMX
    question: When is a company's next earnings release or investor conference?
  phrasing_ops: 1
  slug: massive-com-tmx-api
- baseURL: wss://socket.polygon.io
  baseurl_source: declared
  description: The us_futures API from Massive (formerly Polygon.io) — 8 operation(s) for us_futures.
  name: Massive (formerly Polygon.io) Us Futures API
  phrasing_intents:
  - id: get_futures_v1_contracts
    intent: Look up futures contracts and specifications
    question: Which futures contracts are listed for a product code?
  - id: get_futures_v1_exchanges
    intent: List US futures exchanges
    question: Which US derivatives exchanges trade futures?
  - id: get_futures_v1_market-status
    intent: Check whether a futures product is trading
    question: Is a futures product open, paused or closed right now?
  - id: get_futures_v1_products
    intent: Browse futures products and specifications
    question: What futures products are available in a given sector?
  - id: get_futures_v1_quotes_ticker
    intent: Get bid and offer quotes for a futures contract
    question: What were the best bid and offer quotes for a futures contract today?
  - id: get_futures_v1_schedules
    intent: Get futures trading session schedules
    question: What are the trading hours and breaks for a futures product?
  - id: get_futures_v1_snapshot
    intent: Snapshot the latest futures contract data
    question: What's the latest price data for a futures contract?
  - id: get_futures_v1_trades_ticker
    intent: Get tick-level trades for a futures contract
    question: What trades executed in a futures contract over a time range?
  phrasing_ops: 8
  slug: massive-com-us-futures-api
- baseURL: wss://socket.polygon.io
  baseurl_source: declared
  description: The us_options API from Massive (formerly Polygon.io) — 3 operation(s) for us_options.
  name: Massive (formerly Polygon.io) Us Options API
  phrasing_intents:
  - id: get_options_v1_exchanges
    intent: List US options exchanges
    question: Which US options exchanges and SIPs are covered?
  - id: get_options_v3_quotes_ticker
    intent: Get NBBO quotes for a US options contract
    question: What were the best bid and ask for an options contract at nanosecond precision?
  - id: get_options_v3_trades_ticker
    intent: Get trades for a US options contract
    question: What individual trades executed in an options contract?
  phrasing_ops: 3
  slug: massive-com-us-options-api
- baseURL: wss://socket.polygon.io
  baseurl_source: declared
  description: The us_stocks_all API from Massive (formerly Polygon.io) — 2 operation(s) for us_stocks_all.
  name: Massive (formerly Polygon.io) Us Stocks All API
  phrasing_intents:
  - id: get_stocks_dev_trades_ticker
    intent: Get individual trades for a US stock
    question: What individual trades executed in a US stock and on which exchange?
  - id: get_stocks_v1_exchanges
    intent: List US stock exchanges and reporting facilities
    question: Which US stock exchanges, TRFs and SIPs are covered?
  phrasing_ops: 2
  slug: massive-com-us-stocks-all-api
- baseURL: wss://socket.polygon.io
  baseurl_source: declared
  description: The us_stocks_reference API from Massive (formerly Polygon.io) — 3 operation(s) for us_stocks_reference.
  name: Massive (formerly Polygon.io) Us Stocks Reference API
  phrasing_intents:
  - id: get_stocks_v1_dividends
    intent: Get split-adjusted dividend history
    question: What dividends has a US stock paid, adjusted for splits?
  - id: get_stocks_v1_splits
    intent: Get stock split history with adjustment factors
    question: Has a US stock done a split or reverse split?
  - id: get_v1_reference_ipos
    intent: Get IPOs and direct listings
    question: Which US companies have pending IPOs or direct listings?
  phrasing_ops: 3
  slug: massive-com-us-stocks-reference-api
- baseURL: wss://socket.polygon.io
  baseurl_source: declared
  description: Stock splits and dividends.
  name: Massive (formerly Polygon.io) Corporate Actions API
  phrasing_intents:
  - id: listStockSplits
    intent: List stock splits
    question: Has a company ever split its stock, and when?
  - id: listDividends
    intent: List stock dividends
    question: What dividends has a company paid historically?
  phrasing_ops: 2
  slug: massive-com-corporate-actions-api
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
artifact_total: 165
asyncapis:
- description: 'Streaming WebSocket APIs from Polygon.io (now operating as Massive) for real-time and delayed US Stocks, Options, Forex, Crypto, Indices, and Futures market data. Clients connect to a market-specific '
  name: Polygon.io WebSocket APIs
  slug: polygon-io-asyncapi
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
- group: company
  title: ''
  type: Website
  url: https://massive.com
- group: docs
  href: https://artifacts.apis.io/massive-com/openapi/_original/polygon-openapi-original.json
  title: ''
  type: OpenAPI
  url: openapi/_original/polygon-openapi-original.json
- group: other
  href: https://artifacts.apis.io/massive-com/overlays/polygon-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/polygon-openapi-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/massive-com/mcp/polygon-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/polygon-mcp.yml
- group: build
  href: https://artifacts.apis.io/massive-com/mcp/polygon-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/polygon-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/massive-com/llms/polygon-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/polygon-llms.txt
- group: agent
  href: https://artifacts.apis.io/massive-com/well-known/polygon-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/polygon-well-known.yml
- group: build
  href: https://artifacts.apis.io/massive-com/packages/polygon-packages.yml
  title: ''
  type: Packages
  url: packages/polygon-packages.yml
- group: design
  href: https://artifacts.apis.io/massive-com/conformance/polygon-conformance.yml
  title: ''
  type: Conformance
  url: conformance/polygon-conformance.yml
- group: design
  href: https://artifacts.apis.io/massive-com/errors/polygon-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/polygon-problem-types.yml
- group: design
  href: https://artifacts.apis.io/massive-com/lifecycle/polygon-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/polygon-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/massive-com/changelog/polygon-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/polygon-changelog.yml
- group: design
  href: https://artifacts.apis.io/massive-com/conventions/polygon-conventions.yml
  title: ''
  type: Conventions
  url: conventions/polygon-conventions.yml
- group: design
  href: https://artifacts.apis.io/massive-com/conventions/polygon-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/polygon-conventions.yml
- group: design
  href: https://artifacts.apis.io/massive-com/data-model/polygon-data-model.yml
  title: ''
  type: DataModel
  url: data-model/polygon-data-model.yml
- group: auth
  href: https://artifacts.apis.io/massive-com/scopes/polygon-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/polygon-scopes.yml
- group: agent
  href: https://artifacts.apis.io/massive-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/massive-com/agentic-access/polygon-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/polygon-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/massive-com/security/polygon-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/polygon-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/massive-com/authentication/polygon-authentication.yml
  title: ''
  type: Authentication
  url: authentication/polygon-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/polygon/overview
- group: design
  href: https://artifacts.apis.io/massive-com/arazzo/polygon-corporate-actions-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/polygon-corporate-actions-workflow.yml
- group: design
  href: https://artifacts.apis.io/massive-com/arazzo/polygon-crypto-daily-comparison-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/polygon-crypto-daily-comparison-workflow.yml
- group: design
  href: https://artifacts.apis.io/massive-com/arazzo/polygon-crypto-pair-analysis-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/polygon-crypto-pair-analysis-workflow.yml
- group: design
  href: https://artifacts.apis.io/massive-com/arazzo/polygon-forex-pair-analysis-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/polygon-forex-pair-analysis-workflow.yml
- group: design
  href: https://artifacts.apis.io/massive-com/arazzo/polygon-grouped-market-scan-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/polygon-grouped-market-scan-workflow.yml
- group: design
  href: https://artifacts.apis.io/massive-com/arazzo/polygon-index-analysis-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/polygon-index-analysis-workflow.yml
- group: design
  href: https://artifacts.apis.io/massive-com/arazzo/polygon-market-gated-stock-daily-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/polygon-market-gated-stock-daily-workflow.yml
- group: design
  href: https://artifacts.apis.io/massive-com/arazzo/polygon-options-chain-scan-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/polygon-options-chain-scan-workflow.yml
- group: design
  href: https://artifacts.apis.io/massive-com/arazzo/polygon-options-contract-deep-dive-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/polygon-options-contract-deep-dive-workflow.yml
- group: design
  href: https://artifacts.apis.io/massive-com/arazzo/polygon-stock-research-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/polygon-stock-research-workflow.yml
- group: design
  href: https://artifacts.apis.io/massive-com/arazzo/polygon-ticker-discovery-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/polygon-ticker-discovery-workflow.yml
- group: design
  href: https://artifacts.apis.io/massive-com/arazzo/polygon-ticker-news-context-workflow.yml
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
  href: https://artifacts.apis.io/massive-com/plans/polygon-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/polygon-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/massive-com/rate-limits/polygon-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/polygon-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/massive-com/finops/polygon-finops.yml
  title: ''
  type: FinOps
  url: finops/polygon-finops.yml
- group: design
  href: https://artifacts.apis.io/massive-com/rules/polygon-rules.yml
  title: ''
  type: SpectralRules
  url: rules/polygon-rules.yml
- group: design
  href: https://artifacts.apis.io/massive-com/vocabulary/polygon-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/polygon-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/massive-com/json-ld/polygon-context.jsonld
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
- has_sources: true
  method: derived
  name: Polygon Finops
  primary_unit: individual use only
  service_category: ''
  slug: polygon-finops
  template: false
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
- description: Remote MCP server at mcp.massive.com; 3 tools listed.
  name: Massive MCP server — remote https://mcp.massive.com (OAuth) + open-source mcp_massive (stdio)
  slug: massive-mcp-server-remote-https-mcp-massive-com-oauth-open-source-mcp-massive-stdio
modified: '2026-09-16'
name: Massive (formerly Polygon.io)
nav: Providers
network: true
overview: 'Massive (formerly Polygon.io) publishes 70 API contracts indexed on the [APIs.io](https://apis.io/) network, including Polygon WebSocket API, Polygon.io Stocks API, Polygon.io Options API, and 67 more. Tagged areas include Finance, Fintech, Market Data, Stocks, and Options.


  The Massive (formerly Polygon.io) catalog on APIs.io includes 2 event-driven AsyncAPI specifications, 1 JSON-LD context, and 3 Spectral governance rulesets.


  Massive (formerly Polygon.io)''s developer surface includes changelog, authentication, developer portal, documentation, API reference, getting-started guide, signup flow, and 52 more developer resources.'
plans:
- name: Massive Com Price Estimates
  plan_count: 0
  slug: massive-com-price-estimates
- name: Polygon Plans Pricing
  plan_count: 7
  slug: polygon-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 6
  name: Polygon Rate Limits
  slug: polygon-rate-limits
rules:
- authorship: generated
  effective_rule_count: 32
  extends:
  - spectral:asyncapi
  name: Massive (formerly Polygon.io) — polygon asyncapi rules
  rule_count: 5
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 4
  slug: polygon-asyncapi-spectral-rules
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: Massive (formerly Polygon.io) — polygon jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: polygon-jsonschema-spectral-rules
- authorship: unmarked
  effective_rule_count: 62
  extends:
  - spectral:oas
  name: Massive (formerly Polygon.io) — polygon rules
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
  band: strong
  composite: 58.7
  coverage:
    artifact_dirs: 36
    catalog_earned: 75.0
    catalog_earned_first_party: 0.0
    catalog_gap: 40.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.2
  facets:
    access_clarity: 46.1
    contract_governance: 31.8
    contract_quality: 77.6
    developer_ergonomics: 56.1
    discoverability: 80.0
    operational_transparency: 34.2
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 64.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 98.4
      total: 63
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 38.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/massive-com/polygon-2026-06-20T191902.png
security:
- kind: authentication
  name: Polygon Authentication
  slug: polygon-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Polygon Domain Security
  slug: polygon-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 3
skills:
- name: Market-aware daily scan with Massive (Polygon.io)
  slug: polygon-market-status-scan
- name: Analyze an options chain with Massive (Polygon.io)
  slug: polygon-options-chain-analysis
- name: Research a stock with Massive (Polygon.io)
  slug: polygon-stock-research
slug: massive-com
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
- Foreign Exchange
- Cryptocurrency
- Indices
- Futures
- WebSocket
- Real-Time
- Historical
- Public APIs
- Financial Data
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
website: https://massive.com
---
