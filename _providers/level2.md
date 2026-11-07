---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: true
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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 28.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 116
  human_in_the_loop: 6
  name: Level2 Agentic Access
  operation_count: 316
  slug: level2-agentic-access
  summary_line: 316 operations · 116 acting · 6 human-in-the-loop
api_count: 3
apis:
- baseURL: https://api.trylevel2.com/v1
  baseurl_source: declared
  description: Endpoints for running backtests on strategies against historical market data to validate performance before live deployment.
  name: level2 Backtesting API
  slug: level2-backtesting-api
- baseURL: https://app.bytemine.io/api
  baseurl_source: declared
  description: Endpoints for discovering similar stocks and retrieving company fundamental summaries.
  name: level2 Discovery API
  slug: level2-discovery-api
- baseURL: https://app.bytemine.io/api
  baseurl_source: declared
  description: Endpoints for retrieving historical OHLC price data for financial instruments across global exchanges.
  name: level2 Market Data API
  slug: level2-market-data-api
- baseURL: https://api.trylevel2.com/v1
  baseurl_source: declared
  description: Endpoints for managing user trading strategies, including creation, retrieval, updating, deployment, and deletion of automated trading strategies built with the Level2 visual strategy builder.
  name: level2 Strategies API
  slug: level2-strategies-api
- baseURL: https://app.bytemine.io/api
  baseurl_source: declared
  description: Endpoints for detecting candlestick patterns and analyzing ticker trends using technical indicators.
  name: level2 Technical Analysis API
  slug: level2-technical-analysis-api
- baseURL: https://api.trylevel2.com/v1
  baseurl_source: declared
  description: Endpoints for managing broker user accounts and their association with the Level2 platform.
  name: level2 Users API
  slug: level2-users-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Accept Collaboration Invitation API from Level2 — 1 operation(s) for accept collaboration invitation.
  name: Level2 Accept Collaboration Invitation API
  slug: level2-accept-collaboration-invitation-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Accounts API from Level2 — 2 operation(s) for accounts.
  name: Level2 Accounts API
  slug: level2-accounts-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Add Showcase Videos API from Level2 — 1 operation(s) for add showcase videos.
  name: Level2 Add Showcase Videos API
  slug: level2-add-showcase-videos-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Admin API from Level2 — 13 operation(s) for admin.
  name: Level2 Admin API
  slug: level2-admin-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Auth API from Level2 — 1 operation(s) for auth.
  name: Level2 Auth API
  slug: level2-auth-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Backtest On Different Timeframe API from Level2 — 1 operation(s) for backtest on different timeframe.
  name: Level2 Backtest On Different Timeframe API
  slug: level2-backtest-on-different-timeframe-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Backtest Strategy API from Level2 — 1 operation(s) for backtest strategy.
  name: Level2 Backtest Strategy API
  slug: level2-backtest-strategy-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Blloo API from Level2 — 1 operation(s) for blloo.
  name: Level2 Blloo API
  slug: level2-blloo-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Broker API from Level2 — 18 operation(s) for broker.
  name: Level2 Broker API
  slug: level2-broker-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Broker Get User Strategy Performance API from Level2 — 1 operation(s) for broker get user strategy performance.
  name: Level2 Broker Get User Strategy Performance API
  slug: level2-broker-get-user-strategy-performance-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Broker Oauth API from Level2 — 3 operation(s) for broker oauth.
  name: Level2 Broker Oauth API
  slug: level2-broker-oauth-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Build New Strategy API from Level2 — 1 operation(s) for build new strategy.
  name: Level2 Build New Strategy API
  slug: level2-build-new-strategy-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Calculate Broker Stats V2 API from Level2 — 1 operation(s) for calculate broker stats v2.
  name: Level2 Calculate Broker Stats V2 API
  slug: level2-calculate-broker-stats-v2-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Canvas Add Comment API from Level2 — 1 operation(s) for canvas add comment.
  name: Level2 Canvas Add Comment API
  slug: level2-canvas-add-comment-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Canvas Get Actions API from Level2 — 1 operation(s) for canvas get actions.
  name: Level2 Canvas Get Actions API
  slug: level2-canvas-get-actions-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Canvas Get Categories API from Level2 — 1 operation(s) for canvas get categories.
  name: Level2 Canvas Get Categories API
  slug: level2-canvas-get-categories-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Canvas Get Chart Patterns API from Level2 — 1 operation(s) for canvas get chart patterns.
  name: Level2 Canvas Get Chart Patterns API
  slug: level2-canvas-get-chart-patterns-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Canvas Get Comments API from Level2 — 1 operation(s) for canvas get comments.
  name: Level2 Canvas Get Comments API
  slug: level2-canvas-get-comments-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Canvas Get Datas API from Level2 — 1 operation(s) for canvas get datas.
  name: Level2 Canvas Get Datas API
  slug: level2-canvas-get-datas-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Canvas Get Indicators API from Level2 — 1 operation(s) for canvas get indicators.
  name: Level2 Canvas Get Indicators API
  slug: level2-canvas-get-indicators-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Canvas Get Logics API from Level2 — 1 operation(s) for canvas get logics.
  name: Level2 Canvas Get Logics API
  slug: level2-canvas-get-logics-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Canvas Get Logics V2 API from Level2 — 1 operation(s) for canvas get logics v2.
  name: Level2 Canvas Get Logics V2 API
  slug: level2-canvas-get-logics-v2-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Canvas Get Notifications API from Level2 — 1 operation(s) for canvas get notifications.
  name: Level2 Canvas Get Notifications API
  slug: level2-canvas-get-notifications-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Canvas Get Pair Trading API from Level2 — 1 operation(s) for canvas get pair trading.
  name: Level2 Canvas Get Pair Trading API
  slug: level2-canvas-get-pair-trading-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Canvas Get Patterns API from Level2 — 1 operation(s) for canvas get patterns.
  name: Level2 Canvas Get Patterns API
  slug: level2-canvas-get-patterns-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Canvas Query Indicator API from Level2 — 1 operation(s) for canvas query indicator.
  name: Level2 Canvas Query Indicator API
  slug: level2-canvas-query-indicator-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Challenge Leaderboard API from Level2 — 1 operation(s) for challenge leaderboard.
  name: Level2 Challenge Leaderboard API
  slug: level2-challenge-leaderboard-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Challenge Stats API from Level2 — 1 operation(s) for challenge stats.
  name: Level2 Challenge Stats API
  slug: level2-challenge-stats-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Change Backtest Mode API from Level2 — 1 operation(s) for change backtest mode.
  name: Level2 Change Backtest Mode API
  slug: level2-change-backtest-mode-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Change Strategy Category API from Level2 — 1 operation(s) for change strategy category.
  name: Level2 Change Strategy Category API
  slug: level2-change-strategy-category-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Change Strategy Name API from Level2 — 1 operation(s) for change strategy name.
  name: Level2 Change Strategy Name API
  slug: level2-change-strategy-name-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Change Strategy Timeframe API from Level2 — 1 operation(s) for change strategy timeframe.
  name: Level2 Change Strategy Timeframe API
  slug: level2-change-strategy-timeframe-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Change Strategy Via Trainer API from Level2 — 1 operation(s) for change strategy via trainer.
  name: Level2 Change Strategy Via Trainer API
  slug: level2-change-strategy-via-trainer-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Change Tp Sl Percent API from Level2 — 1 operation(s) for change tp sl percent.
  name: Level2 Change Tp Sl Percent API
  slug: level2-change-tp-sl-percent-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Check For Token API from Level2 — 1 operation(s) for check for token.
  name: Level2 Check For Token API
  slug: level2-check-for-token-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Check Latest Order Status API from Level2 — 1 operation(s) for check latest order status.
  name: Level2 Check Latest Order Status API
  slug: level2-check-latest-order-status-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Check Strategy Author API from Level2 — 1 operation(s) for check strategy author.
  name: Level2 Check Strategy Author API
  slug: level2-check-strategy-author-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Check Subscription Status API from Level2 — 1 operation(s) for check subscription status.
  name: Level2 Check Subscription Status API
  slug: level2-check-subscription-status-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Check Symbol Forex API from Level2 — 1 operation(s) for check symbol forex.
  name: Level2 Check Symbol Forex API
  slug: level2-check-symbol-forex-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Check Symbol Type API from Level2 — 1 operation(s) for check symbol type.
  name: Level2 Check Symbol Type API
  slug: level2-check-symbol-type-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Check Trades Position API from Level2 — 1 operation(s) for check trades position.
  name: Level2 Check Trades Position API
  slug: level2-check-trades-position-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Choose Account API from Level2 — 2 operation(s) for choose account.
  name: Level2 Choose Account API
  slug: level2-choose-account-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Ci API from Level2 — 1 operation(s) for ci.
  name: Level2 Ci API
  slug: level2-ci-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Composer Generate Strategy API from Level2 — 1 operation(s) for composer generate strategy.
  name: Level2 Composer Generate Strategy API
  slug: level2-composer-generate-strategy-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Contact Us Form Main Web API from Level2 — 1 operation(s) for contact us form main web.
  name: Level2 Contact Us Form Main Web API
  slug: level2-contact-us-form-main-web-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Copy Marketplace Strategy API from Level2 — 1 operation(s) for copy marketplace strategy.
  name: Level2 Copy Marketplace Strategy API
  slug: level2-copy-marketplace-strategy-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Copy Strategy API from Level2 — 1 operation(s) for copy strategy.
  name: Level2 Copy Strategy API
  slug: level2-copy-strategy-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Copy User Strategy API from Level2 — 1 operation(s) for copy user strategy.
  name: Level2 Copy User Strategy API
  slug: level2-copy-user-strategy-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Create Live Order API from Level2 — 1 operation(s) for create live order.
  name: Level2 Create Live Order API
  slug: level2-create-live-order-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Create Market Scanner Strategy API from Level2 — 1 operation(s) for create market scanner strategy.
  name: Level2 Create Market Scanner Strategy API
  slug: level2-create-market-scanner-strategy-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Create Market Scanner Universe API from Level2 — 1 operation(s) for create market scanner universe.
  name: Level2 Create Market Scanner Universe API
  slug: level2-create-market-scanner-universe-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Create Stripe Checkout Session API from Level2 — 1 operation(s) for create stripe checkout session.
  name: Level2 Create Stripe Checkout Session API
  slug: level2-create-stripe-checkout-session-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Critical Alerts API from Level2 — 1 operation(s) for critical alerts.
  name: Level2 Critical Alerts API
  slug: level2-critical-alerts-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Ctrader Access API from Level2 — 1 operation(s) for ctrader access.
  name: Level2 Ctrader Access API
  slug: level2-ctrader-access-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Ctrader Auth Callback API from Level2 — 1 operation(s) for ctrader auth callback.
  name: Level2 Ctrader Auth Callback API
  slug: level2-ctrader-auth-callback-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Deactivate Email API from Level2 — 1 operation(s) for deactivate email.
  name: Level2 Deactivate Email API
  slug: level2-deactivate-email-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Delete Account API from Level2 — 1 operation(s) for delete account.
  name: Level2 Delete Account API
  slug: level2-delete-account-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Delete Market Scanner Strategy API from Level2 — 1 operation(s) for delete market scanner strategy.
  name: Level2 Delete Market Scanner Strategy API
  slug: level2-delete-market-scanner-strategy-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Delete Multiple Strategies API from Level2 — 1 operation(s) for delete multiple strategies.
  name: Level2 Delete Multiple Strategies API
  slug: level2-delete-multiple-strategies-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Delete Strategy API from Level2 — 1 operation(s) for delete strategy.
  name: Level2 Delete Strategy API
  slug: level2-delete-strategy-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Deploy Live Multi Asset Strategy API from Level2 — 1 operation(s) for deploy live multi asset strategy.
  name: Level2 Deploy Live Multi Asset Strategy API
  slug: level2-deploy-live-multi-asset-strategy-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Deploy Live Strategy API from Level2 — 1 operation(s) for deploy live strategy.
  name: Level2 Deploy Live Strategy API
  slug: level2-deploy-live-strategy-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Deploy Notification Strategy API from Level2 — 1 operation(s) for deploy notification strategy.
  name: Level2 Deploy Notification Strategy API
  slug: level2-deploy-notification-strategy-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Deploy Scanner API from Level2 — 1 operation(s) for deploy scanner.
  name: Level2 Deploy Scanner API
  slug: level2-deploy-scanner-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Expert Trader API from Level2 — 1 operation(s) for expert trader.
  name: Level2 Expert Trader API
  slug: level2-expert-trader-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The External Analysis API from Level2 — 1 operation(s) for external analysis.
  name: Level2 External Analysis API
  slug: level2-external-analysis-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Fetch Active Live Deployments API from Level2 — 1 operation(s) for fetch active live deployments.
  name: Level2 Fetch Active Live Deployments API
  slug: level2-fetch-active-live-deployments-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Fetch Pricing Plan Details API from Level2 — 1 operation(s) for fetch pricing plan details.
  name: Level2 Fetch Pricing Plan Details API
  slug: level2-fetch-pricing-plan-details-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Filter Broker Stats Get Meta API from Level2 — 1 operation(s) for filter broker stats get meta.
  name: Level2 Filter Broker Stats Get Meta API
  slug: level2-filter-broker-stats-get-meta-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Filter Broker User Stats Via Date All API from Level2 — 1 operation(s) for filter broker user stats via date all.
  name: Level2 Filter Broker User Stats Via Date All API
  slug: level2-filter-broker-user-stats-via-date-all-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Filter Broker User Stats Via Date API from Level2 — 1 operation(s) for filter broker user stats via date.
  name: Level2 Filter Broker User Stats Via Date API
  slug: level2-filter-broker-user-stats-via-date-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Forex Rates API from Level2 — 1 operation(s) for forex rates.
  name: Level2 Forex Rates API
  slug: level2-forex-rates-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Forward Test Metrics API from Level2 — 1 operation(s) for forward test metrics.
  name: Level2 Forward Test Metrics API
  slug: level2-forward-test-metrics-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Generate Email Otp API from Level2 — 1 operation(s) for generate email otp.
  name: Level2 Generate Email Otp API
  slug: level2-generate-email-otp-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Generate Token API from Level2 — 1 operation(s) for generate token.
  name: Level2 Generate Token API
  slug: level2-generate-token-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Generate Trending Strategies API from Level2 — 1 operation(s) for generate trending strategies.
  name: Level2 Generate Trending Strategies API
  slug: level2-generate-trending-strategies-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Generate Trending Symbols API from Level2 — 1 operation(s) for generate trending symbols.
  name: Level2 Generate Trending Symbols API
  slug: level2-generate-trending-symbols-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Generate Trending Traders API from Level2 — 1 operation(s) for generate trending traders.
  name: Level2 Generate Trending Traders API
  slug: level2-generate-trending-traders-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Generate View Strategy Get Canvas Data API from Level2 — 1 operation(s) for generate view strategy get canvas data.
  name: Level2 Generate View Strategy Get Canvas Data API
  slug: level2-generate-view-strategy-get-canvas-data-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Get Account Balances API from Level2 — 1 operation(s) for get account balances.
  name: Level2 Get Account Balances API
  slug: level2-get-account-balances-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Get All Broker User Stats API from Level2 — 1 operation(s) for get all broker user stats.
  name: Level2 Get All Broker User Stats API
  slug: level2-get-all-broker-user-stats-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Get All Live Deployments V2 API from Level2 — 1 operation(s) for get all live deployments v2.
  name: Level2 Get All Live Deployments V2 API
  slug: level2-get-all-live-deployments-v2-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Get All Notification Deployments API from Level2 — 1 operation(s) for get all notification deployments.
  name: Level2 Get All Notification Deployments API
  slug: level2-get-all-notification-deployments-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Get All Report Versions API from Level2 — 1 operation(s) for get all report versions.
  name: Level2 Get All Report Versions API
  slug: level2-get-all-report-versions-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Get All User Brokers API from Level2 — 1 operation(s) for get all user brokers.
  name: Level2 Get All User Brokers API
  slug: level2-get-all-user-brokers-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Get Alltime Live Pnl API from Level2 — 1 operation(s) for get alltime live pnl.
  name: Level2 Get Alltime Live Pnl API
  slug: level2-get-alltime-live-pnl-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Get B2c Brokers API from Level2 — 1 operation(s) for get b2c brokers.
  name: Level2 Get B2c Brokers API
  slug: level2-get-b2c-brokers-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Get Benchmark Performance API from Level2 — 1 operation(s) for get benchmark performance.
  name: Level2 Get Benchmark Performance API
  slug: level2-get-benchmark-performance-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Get Broker Api Keys API from Level2 — 1 operation(s) for get broker api keys.
  name: Level2 Get Broker Api Keys API
  slug: level2-get-broker-api-keys-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Get Broker Specific Tickers API from Level2 — 1 operation(s) for get broker specific tickers.
  name: Level2 Get Broker Specific Tickers API
  slug: level2-get-broker-specific-tickers-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Get Broker User Latency Slippage API from Level2 — 1 operation(s) for get broker user latency slippage.
  name: Level2 Get Broker User Latency Slippage API
  slug: level2-get-broker-user-latency-slippage-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Get Broker User Stats API from Level2 — 1 operation(s) for get broker user stats.
  name: Level2 Get Broker User Stats API
  slug: level2-get-broker-user-stats-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Get Cohort Stats API from Level2 — 1 operation(s) for get cohort stats.
  name: Level2 Get Cohort Stats API
  slug: level2-get-cohort-stats-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Get Connected Broker Details V2 API from Level2 — 1 operation(s) for get connected broker details v2.
  name: Level2 Get Connected Broker Details V2 API
  slug: level2-get-connected-broker-details-v2-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Get Copiers Data Broker Stats API from Level2 — 1 operation(s) for get copiers data broker stats.
  name: Level2 Get Copiers Data Broker Stats API
  slug: level2-get-copiers-data-broker-stats-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Get Ctrader Accounts API from Level2 — 1 operation(s) for get ctrader accounts.
  name: Level2 Get Ctrader Accounts API
  slug: level2-get-ctrader-accounts-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Get Ctrader Instruments API from Level2 — 1 operation(s) for get ctrader instruments.
  name: Level2 Get Ctrader Instruments API
  slug: level2-get-ctrader-instruments-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Get Current Registered Count API from Level2 — 1 operation(s) for get current registered count.
  name: Level2 Get Current Registered Count API
  slug: level2-get-current-registered-count-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Get Deploy Live Stats API from Level2 — 1 operation(s) for get deploy live stats.
  name: Level2 Get Deploy Live Stats API
  slug: level2-get-deploy-live-stats-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Get Deployment Hint V2 API from Level2 — 1 operation(s) for get deployment hint v2.
  name: Level2 Get Deployment Hint V2 API
  slug: level2-get-deployment-hint-v2-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Get Deployment Notifications API from Level2 — 1 operation(s) for get deployment notifications.
  name: Level2 Get Deployment Notifications API
  slug: level2-get-deployment-notifications-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Get Earnings Calendar API from Level2 — 1 operation(s) for get earnings calendar.
  name: Level2 Get Earnings Calendar API
  slug: level2-get-earnings-calendar-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Get Explore Strategies API from Level2 — 1 operation(s) for get explore strategies.
  name: Level2 Get Explore Strategies API
  slug: level2-get-explore-strategies-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Get Explore Strategy Favourites API from Level2 — 1 operation(s) for get explore strategy favourites.
  name: Level2 Get Explore Strategy Favourites API
  slug: level2-get-explore-strategy-favourites-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Get Fcm Token Web API from Level2 — 1 operation(s) for get fcm token web.
  name: Level2 Get Fcm Token Web API
  slug: level2-get-fcm-token-web-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Get Fennel Accounts API from Level2 — 1 operation(s) for get fennel accounts.
  name: Level2 Get Fennel Accounts API
  slug: level2-get-fennel-accounts-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Get Global Order Book API from Level2 — 1 operation(s) for get global order book.
  name: Level2 Get Global Order Book API
  slug: level2-get-global-order-book-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Get Indicator Data From Ai API from Level2 — 1 operation(s) for get indicator data from ai.
  name: Level2 Get Indicator Data From Ai API
  slug: level2-get-indicator-data-from-ai-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Get Instrument Suggestions V2 API from Level2 — 1 operation(s) for get instrument suggestions v2.
  name: Level2 Get Instrument Suggestions V2 API
  slug: level2-get-instrument-suggestions-v2-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Get Leaderboard Stats API from Level2 — 1 operation(s) for get leaderboard stats.
  name: Level2 Get Leaderboard Stats API
  slug: level2-get-leaderboard-stats-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Get Leverate Brokers API from Level2 — 1 operation(s) for get leverate brokers.
  name: Level2 Get Leverate Brokers API
  slug: level2-get-leverate-brokers-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Get Leverate Instruments API from Level2 — 1 operation(s) for get leverate instruments.
  name: Level2 Get Leverate Instruments API
  slug: level2-get-leverate-instruments-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Get Live Deployment Strategies Volume API from Level2 — 1 operation(s) for get live deployment strategies volume.
  name: Level2 Get Live Deployment Strategies Volume API
  slug: level2-get-live-deployment-strategies-volume-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Get Live Deployments Aggregated Stats API from Level2 — 1 operation(s) for get live deployments aggregated stats.
  name: Level2 Get Live Deployments Aggregated Stats API
  slug: level2-get-live-deployments-aggregated-stats-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Get Live Deployments Order Status API from Level2 — 1 operation(s) for get live deployments order status.
  name: Level2 Get Live Deployments Order Status API
  slug: level2-get-live-deployments-order-status-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Get Live Deps Pnl API from Level2 — 1 operation(s) for get live deps pnl.
  name: Level2 Get Live Deps Pnl API
  slug: level2-get-live-deps-pnl-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Get Live Expired Strategies V2 API from Level2 — 1 operation(s) for get live expired strategies v2.
  name: Level2 Get Live Expired Strategies V2 API
  slug: level2-get-live-expired-strategies-v2-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Get Live Strategy Full Order Book API from Level2 — 1 operation(s) for get live strategy full order book.
  name: Level2 Get Live Strategy Full Order Book API
  slug: level2-get-live-strategy-full-order-book-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Get Live Strategy Order Book API from Level2 — 1 operation(s) for get live strategy order book.
  name: Level2 Get Live Strategy Order Book API
  slug: level2-get-live-strategy-order-book-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Get Logos API from Level2 — 1 operation(s) for get logos.
  name: Level2 Get Logos API
  slug: level2-get-logos-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Get Main Pricing Plan Details API from Level2 — 1 operation(s) for get main pricing plan details.
  name: Level2 Get Main Pricing Plan Details API
  slug: level2-get-main-pricing-plan-details-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Get Market Scanner Pre Built Strategies API from Level2 — 1 operation(s) for get market scanner pre built strategies.
  name: Level2 Get Market Scanner Pre Built Strategies API
  slug: level2-get-market-scanner-pre-built-strategies-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Get Market Scanner Strategies V2 API from Level2 — 1 operation(s) for get market scanner strategies v2.
  name: Level2 Get Market Scanner Strategies V2 API
  slug: level2-get-market-scanner-strategies-v2-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Get Market Scanner Universes API from Level2 — 1 operation(s) for get market scanner universes.
  name: Level2 Get Market Scanner Universes API
  slug: level2-get-market-scanner-universes-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Get Matchtrader Symbols API from Level2 — 1 operation(s) for get matchtrader symbols.
  name: Level2 Get Matchtrader Symbols API
  slug: level2-get-matchtrader-symbols-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Get Monitor Deployments Stats API from Level2 — 1 operation(s) for get monitor deployments stats.
  name: Level2 Get Monitor Deployments Stats API
  slug: level2-get-monitor-deployments-stats-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Get Monthly Live Pnl API from Level2 — 1 operation(s) for get monthly live pnl.
  name: Level2 Get Monthly Live Pnl API
  slug: level2-get-monthly-live-pnl-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Get Multi Asset Strategies API from Level2 — 1 operation(s) for get multi asset strategies.
  name: Level2 Get Multi Asset Strategies API
  slug: level2-get-multi-asset-strategies-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Get Notification Preference API from Level2 — 1 operation(s) for get notification preference.
  name: Level2 Get Notification Preference API
  slug: level2-get-notification-preference-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Get Open Live Order API from Level2 — 1 operation(s) for get open live order.
  name: Level2 Get Open Live Order API
  slug: level2-get-open-live-order-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Get P L Live Deployed Strategies API from Level2 — 1 operation(s) for get p l live deployed strategies.
  name: Level2 Get P L Live Deployed Strategies API
  slug: level2-get-p-l-live-deployed-strategies-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Get Post Trade Analysis API from Level2 — 1 operation(s) for get post trade analysis.
  name: Level2 Get Post Trade Analysis API
  slug: level2-get-post-trade-analysis-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Get Prediction Market Trending Events API from Level2 — 1 operation(s) for get prediction market trending events.
  name: Level2 Get Prediction Market Trending Events API
  slug: level2-get-prediction-market-trending-events-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Get Profitability By Entry Probability API from Level2 — 1 operation(s) for get profitability by entry probability.
  name: Level2 Get Profitability By Entry Probability API
  slug: level2-get-profitability-by-entry-probability-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Get Published Strategies API from Level2 — 1 operation(s) for get published strategies.
  name: Level2 Get Published Strategies API
  slug: level2-get-published-strategies-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Get Recent Fcm Token API from Level2 — 1 operation(s) for get recent fcm token.
  name: Level2 Get Recent Fcm Token API
  slug: level2-get-recent-fcm-token-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Get Recent Strategies API from Level2 — 1 operation(s) for get recent strategies.
  name: Level2 Get Recent Strategies API
  slug: level2-get-recent-strategies-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Get Referred User Count API from Level2 — 1 operation(s) for get referred user count.
  name: Level2 Get Referred User Count API
  slug: level2-get-referred-user-count-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Get Report Data API from Level2 — 1 operation(s) for get report data.
  name: Level2 Get Report Data API
  slug: level2-get-report-data-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Get Scanner Deployments API from Level2 — 1 operation(s) for get scanner deployments.
  name: Level2 Get Scanner Deployments API
  slug: level2-get-scanner-deployments-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Get Search Items Suggestions V2 API from Level2 — 1 operation(s) for get search items suggestions v2.
  name: Level2 Get Search Items Suggestions V2 API
  slug: level2-get-search-items-suggestions-v2-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Get Showcase Strategies API from Level2 — 1 operation(s) for get showcase strategies.
  name: Level2 Get Showcase Strategies API
  slug: level2-get-showcase-strategies-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Get Showcase Videos API from Level2 — 1 operation(s) for get showcase videos.
  name: Level2 Get Showcase Videos API
  slug: level2-get-showcase-videos-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Get Strategies By User API from Level2 — 1 operation(s) for get strategies by user.
  name: Level2 Get Strategies By User API
  slug: level2-get-strategies-by-user-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Get Strategies Performance Metrics API from Level2 — 1 operation(s) for get strategies performance metrics.
  name: Level2 Get Strategies Performance Metrics API
  slug: level2-get-strategies-performance-metrics-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Get Strategy Add Ons API from Level2 — 1 operation(s) for get strategy add ons.
  name: Level2 Get Strategy Add Ons API
  slug: level2-get-strategy-add-ons-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Get Strategy Categories API from Level2 — 1 operation(s) for get strategy categories.
  name: Level2 Get Strategy Categories API
  slug: level2-get-strategy-categories-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Get Strategy Details API from Level2 — 1 operation(s) for get strategy details.
  name: Level2 Get Strategy Details API
  slug: level2-get-strategy-details-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Get Strategy Details Collab API from Level2 — 1 operation(s) for get strategy details collab.
  name: Level2 Get Strategy Details Collab API
  slug: level2-get-strategy-details-collab-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Get Strategy Details For Multiasset API from Level2 — 1 operation(s) for get strategy details for multiasset.
  name: Level2 Get Strategy Details For Multiasset API
  slug: level2-get-strategy-details-for-multiasset-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Get Strategy From Key API from Level2 — 1 operation(s) for get strategy from key.
  name: Level2 Get Strategy From Key API
  slug: level2-get-strategy-from-key-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Get Strategy Library API from Level2 — 1 operation(s) for get strategy library.
  name: Level2 Get Strategy Library API
  slug: level2-get-strategy-library-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Get Strategy Performance Stats API from Level2 — 1 operation(s) for get strategy performance stats.
  name: Level2 Get Strategy Performance Stats API
  slug: level2-get-strategy-performance-stats-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Get Swap Values API from Level2 — 1 operation(s) for get swap values.
  name: Level2 Get Swap Values API
  slug: level2-get-swap-values-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Get Symbol Data Tickers V3 API from Level2 — 1 operation(s) for get symbol data tickers v3.
  name: Level2 Get Symbol Data Tickers V3 API
  slug: level2-get-symbol-data-tickers-v3-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Get Symbol Data V2 API from Level2 — 1 operation(s) for get symbol data v2.
  name: Level2 Get Symbol Data V2 API
  slug: level2-get-symbol-data-v2-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Get Symbols Details API from Level2 — 1 operation(s) for get symbols details.
  name: Level2 Get Symbols Details API
  slug: level2-get-symbols-details-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Get Ticker Data V2 API from Level2 — 1 operation(s) for get ticker data v2.
  name: Level2 Get Ticker Data V2 API
  slug: level2-get-ticker-data-v2-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Get Tickers Snapshot API from Level2 — 1 operation(s) for get tickers snapshot.
  name: Level2 Get Tickers Snapshot API
  slug: level2-get-tickers-snapshot-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Get Trader Stats API from Level2 — 1 operation(s) for get trader stats.
  name: Level2 Get Trader Stats API
  slug: level2-get-trader-stats-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Get Trending Events API from Level2 — 1 operation(s) for get trending events.
  name: Level2 Get Trending Events API
  slug: level2-get-trending-events-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Get Trending Indicators API from Level2 — 1 operation(s) for get trending indicators.
  name: Level2 Get Trending Indicators API
  slug: level2-get-trending-indicators-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Get Trending Strategies API from Level2 — 1 operation(s) for get trending strategies.
  name: Level2 Get Trending Strategies API
  slug: level2-get-trending-strategies-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Get Trending Traders API from Level2 — 1 operation(s) for get trending traders.
  name: Level2 Get Trending Traders API
  slug: level2-get-trending-traders-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Get Tv Symbol API from Level2 — 1 operation(s) for get tv symbol.
  name: Level2 Get Tv Symbol API
  slug: level2-get-tv-symbol-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Get User Preferences API from Level2 — 1 operation(s) for get user preferences.
  name: Level2 Get User Preferences API
  slug: level2-get-user-preferences-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Get User Strategy Names API from Level2 — 1 operation(s) for get user strategy names.
  name: Level2 Get User Strategy Names API
  slug: level2-get-user-strategy-names-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Get User Walkthrough Status API from Level2 — 1 operation(s) for get user walkthrough status.
  name: Level2 Get User Walkthrough Status API
  slug: level2-get-user-walkthrough-status-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Get Yesterday Today Live Pnl API from Level2 — 1 operation(s) for get yesterday today live pnl.
  name: Level2 Get Yesterday Today Live Pnl API
  slug: level2-get-yesterday-today-live-pnl-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Health API from Level2 — 1 operation(s) for health.
  name: Level2 Health API
  slug: level2-health-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Ibkr Data Section API from Level2 — 1 operation(s) for ibkr data section.
  name: Level2 Ibkr Data Section API
  slug: level2-ibkr-data-section-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Join Us Form Main Web API from Level2 — 1 operation(s) for join us form main web.
  name: Level2 Join Us Form Main Web API
  slug: level2-join-us-form-main-web-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Leverate Auth API from Level2 — 1 operation(s) for leverate auth.
  name: Level2 Leverate Auth API
  slug: level2-leverate-auth-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Leverate Util APIs API from Level2 — 3 operation(s) for leverate util apis.
  name: Level2 Leverate Util APIs API
  slug: level2-leverate-util-apis-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Lightspeed API from Level2 — 1 operation(s) for lightspeed.
  name: Level2 Lightspeed API
  slug: level2-lightspeed-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Like Strategy API from Level2 — 1 operation(s) for like strategy.
  name: Level2 Like Strategy API
  slug: level2-like-strategy-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Live Strategy Metrics API from Level2 — 1 operation(s) for live strategy metrics.
  name: Level2 Live Strategy Metrics API
  slug: level2-live-strategy-metrics-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Login API from Level2 — 1 operation(s) for login.
  name: Level2 Login API
  slug: level2-login-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Login User Broker API from Level2 — 1 operation(s) for login user broker.
  name: Level2 Login User Broker API
  slug: level2-login-user-broker-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Marketplace Child Categories API from Level2 — 1 operation(s) for marketplace child categories.
  name: Level2 Marketplace Child Categories API
  slug: level2-marketplace-child-categories-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Marketplace Entry Exit Dominance API from Level2 — 1 operation(s) for marketplace entry exit dominance.
  name: Level2 Marketplace Entry Exit Dominance API
  slug: level2-marketplace-entry-exit-dominance-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Marketplace Filter Authors API from Level2 — 1 operation(s) for marketplace filter authors.
  name: Level2 Marketplace Filter Authors API
  slug: level2-marketplace-filter-authors-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Marketplace Filter Strategies API from Level2 — 1 operation(s) for marketplace filter strategies.
  name: Level2 Marketplace Filter Strategies API
  slug: level2-marketplace-filter-strategies-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Marketplace List API from Level2 — 1 operation(s) for marketplace list.
  name: Level2 Marketplace List API
  slug: level2-marketplace-list-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Marketplace Long Short Dominance API from Level2 — 1 operation(s) for marketplace long short dominance.
  name: Level2 Marketplace Long Short Dominance API
  slug: level2-marketplace-long-short-dominance-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Marketplace Parent Categories API from Level2 — 1 operation(s) for marketplace parent categories.
  name: Level2 Marketplace Parent Categories API
  slug: level2-marketplace-parent-categories-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Marketplace Recent Trades API from Level2 — 1 operation(s) for marketplace recent trades.
  name: Level2 Marketplace Recent Trades API
  slug: level2-marketplace-recent-trades-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Migrate Users API from Level2 — 1 operation(s) for migrate users.
  name: Level2 Migrate Users API
  slug: level2-migrate-users-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Migration API from Level2 — 1 operation(s) for migration.
  name: Level2 Migration API
  slug: level2-migration-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Pre Built Strategies View Data API from Level2 — 1 operation(s) for pre built strategies view data.
  name: Level2 Pre Built Strategies View Data API
  slug: level2-pre-built-strategies-view-data-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Prediction Market Candlesticks API from Level2 — 1 operation(s) for prediction market candlesticks.
  name: Level2 Prediction Market Candlesticks API
  slug: level2-prediction-market-candlesticks-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Prediction Market Event Details API from Level2 — 1 operation(s) for prediction market event details.
  name: Level2 Prediction Market Event Details API
  slug: level2-prediction-market-event-details-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Prediction Market Event Readable Names API from Level2 — 1 operation(s) for prediction market event readable names.
  name: Level2 Prediction Market Event Readable Names API
  slug: level2-prediction-market-event-readable-names-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Prediction Market Events API from Level2 — 1 operation(s) for prediction market events.
  name: Level2 Prediction Market Events API
  slug: level2-prediction-market-events-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Prediction Market Strict Sl API from Level2 — 1 operation(s) for prediction market strict sl.
  name: Level2 Prediction Market Strict Sl API
  slug: level2-prediction-market-strict-sl-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Profile Publish Strategy API from Level2 — 1 operation(s) for profile publish strategy.
  name: Level2 Profile Publish Strategy API
  slug: level2-profile-publish-strategy-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Public Connection Url API from Level2 — 1 operation(s) for public connection url.
  name: Level2 Public Connection Url API
  slug: level2-public-connection-url-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Publish Explore Strategy API from Level2 — 1 operation(s) for publish explore strategy.
  name: Level2 Publish Explore Strategy API
  slug: level2-publish-explore-strategy-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Publish To Marketplace API from Level2 — 1 operation(s) for publish to marketplace.
  name: Level2 Publish To Marketplace API
  slug: level2-publish-to-marketplace-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Read Deployment Notifications API from Level2 — 1 operation(s) for read deployment notifications.
  name: Level2 Read Deployment Notifications API
  slug: level2-read-deployment-notifications-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Register Fcm Token API from Level2 — 1 operation(s) for register fcm token.
  name: Level2 Register Fcm Token API
  slug: level2-register-fcm-token-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Register Login API from Level2 — 1 operation(s) for register login.
  name: Level2 Register Login API
  slug: level2-register-login-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Register User API from Level2 — 1 operation(s) for register user.
  name: Level2 Register User API
  slug: level2-register-user-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Register User Broker API from Level2 — 1 operation(s) for register user broker.
  name: Level2 Register User Broker API
  slug: level2-register-user-broker-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Remove Subscription API from Level2 — 1 operation(s) for remove subscription.
  name: Level2 Remove Subscription API
  slug: level2-remove-subscription-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Reset Broker Configuration API from Level2 — 1 operation(s) for reset broker configuration.
  name: Level2 Reset Broker Configuration API
  slug: level2-reset-broker-configuration-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Reset Password API from Level2 — 1 operation(s) for reset password.
  name: Level2 Reset Password API
  slug: level2-reset-password-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Reset User Broker Configuration API from Level2 — 1 operation(s) for reset user broker configuration.
  name: Level2 Reset User Broker Configuration API
  slug: level2-reset-user-broker-configuration-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Save Addons API from Level2 — 1 operation(s) for save addons.
  name: Level2 Save Addons API
  slug: level2-save-addons-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Save Broker Api Keys API from Level2 — 1 operation(s) for save broker api keys.
  name: Level2 Save Broker Api Keys API
  slug: level2-save-broker-api-keys-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Save Broker Api Keys V2 API from Level2 — 1 operation(s) for save broker api keys v2.
  name: Level2 Save Broker Api Keys V2 API
  slug: level2-save-broker-api-keys-v2-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Save Strategy API from Level2 — 1 operation(s) for save strategy.
  name: Level2 Save Strategy API
  slug: level2-save-strategy-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Search Category Name API from Level2 — 1 operation(s) for search category name.
  name: Level2 Search Category Name API
  slug: level2-search-category-name-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Search Explore Strategies API from Level2 — 1 operation(s) for search explore strategies.
  name: Level2 Search Explore Strategies API
  slug: level2-search-explore-strategies-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Search Marketplace API from Level2 — 1 operation(s) for search marketplace.
  name: Level2 Search Marketplace API
  slug: level2-search-marketplace-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Search Trending Traders API from Level2 — 1 operation(s) for search trending traders.
  name: Level2 Search Trending Traders API
  slug: level2-search-trending-traders-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Send Canvas Attendance API from Level2 — 1 operation(s) for send canvas attendance.
  name: Level2 Send Canvas Attendance API
  slug: level2-send-canvas-attendance-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Send Engine Email API from Level2 — 1 operation(s) for send engine email.
  name: Level2 Send Engine Email API
  slug: level2-send-engine-email-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Send Otp Password Reset API from Level2 — 1 operation(s) for send otp password reset.
  name: Level2 Send Otp Password Reset API
  slug: level2-send-otp-password-reset-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Send Sms Otp API from Level2 — 1 operation(s) for send sms otp.
  name: Level2 Send Sms Otp API
  slug: level2-send-sms-otp-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Session API from Level2 — 1 operation(s) for session.
  name: Level2 Session API
  slug: level2-session-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Set Language Preference API from Level2 — 1 operation(s) for set language preference.
  name: Level2 Set Language Preference API
  slug: level2-set-language-preference-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Set Notification Config API from Level2 — 1 operation(s) for set notification config.
  name: Level2 Set Notification Config API
  slug: level2-set-notification-config-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Set Notification Preference API from Level2 — 1 operation(s) for set notification preference.
  name: Level2 Set Notification Preference API
  slug: level2-set-notification-preference-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Set Nudges Tracker API from Level2 — 1 operation(s) for set nudges tracker.
  name: Level2 Set Nudges Tracker API
  slug: level2-set-nudges-tracker-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Set Strategy Size API from Level2 — 1 operation(s) for set strategy size.
  name: Level2 Set Strategy Size API
  slug: level2-set-strategy-size-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Set User Walkthrough Status API from Level2 — 1 operation(s) for set user walkthrough status.
  name: Level2 Set User Walkthrough Status API
  slug: level2-set-user-walkthrough-status-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Share Invitation API from Level2 — 1 operation(s) for share invitation.
  name: Level2 Share Invitation API
  slug: level2-share-invitation-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Strategy Trainer Try Action V2 API from Level2 — 1 operation(s) for strategy trainer try action v2.
  name: Level2 Strategy Trainer Try Action V2 API
  slug: level2-strategy-trainer-try-action-v2-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Strategy Trainer Try Tpsl V2 API from Level2 — 1 operation(s) for strategy trainer try tpsl v2.
  name: Level2 Strategy Trainer Try Tpsl V2 API
  slug: level2-strategy-trainer-try-tpsl-v2-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Stripe API from Level2 — 1 operation(s) for stripe.
  name: Level2 Stripe API
  slug: level2-stripe-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Submit Email For Video API from Level2 — 1 operation(s) for submit email for video.
  name: Level2 Submit Email For Video API
  slug: level2-submit-email-for-video-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Support Request API from Level2 — 1 operation(s) for support request.
  name: Level2 Support Request API
  slug: level2-support-request-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Tess API from Level2 — 1 operation(s) for tess.
  name: Level2 Tess API
  slug: level2-tess-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Test Twitter API from Level2 — 1 operation(s) for test twitter.
  name: Level2 Test Twitter API
  slug: level2-test-twitter-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Trading Challenge Cambridge API from Level2 — 1 operation(s) for trading challenge cambridge.
  name: Level2 Trading Challenge Cambridge API
  slug: level2-trading-challenge-cambridge-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Trading Challenge Email API from Level2 — 1 operation(s) for trading challenge email.
  name: Level2 Trading Challenge Email API
  slug: level2-trading-challenge-email-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Trading Challenge Oxford API from Level2 — 1 operation(s) for trading challenge oxford.
  name: Level2 Trading Challenge Oxford API
  slug: level2-trading-challenge-oxford-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Trading Challenge Tracker API from Level2 — 1 operation(s) for trading challenge tracker.
  name: Level2 Trading Challenge Tracker API
  slug: level2-trading-challenge-tracker-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Trading Challenge Ww API from Level2 — 1 operation(s) for trading challenge ww.
  name: Level2 Trading Challenge Ww API
  slug: level2-trading-challenge-ww-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Undeploy Live Deployment API from Level2 — 1 operation(s) for undeploy live deployment.
  name: Level2 Undeploy Live Deployment API
  slug: level2-undeploy-live-deployment-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Undeploy Live Multi Asset Strategy API from Level2 — 1 operation(s) for undeploy live multi asset strategy.
  name: Level2 Undeploy Live Multi Asset Strategy API
  slug: level2-undeploy-live-multi-asset-strategy-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Undeploy Live Strategy API from Level2 — 1 operation(s) for undeploy live strategy.
  name: Level2 Undeploy Live Strategy API
  slug: level2-undeploy-live-strategy-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Undeploy Notification Strategy API from Level2 — 1 operation(s) for undeploy notification strategy.
  name: Level2 Undeploy Notification Strategy API
  slug: level2-undeploy-notification-strategy-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Undeploy Scanner API from Level2 — 1 operation(s) for undeploy scanner.
  name: Level2 Undeploy Scanner API
  slug: level2-undeploy-scanner-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Unlike Strategy API from Level2 — 1 operation(s) for unlike strategy.
  name: Level2 Unlike Strategy API
  slug: level2-unlike-strategy-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Unlok Util APIs API from Level2 — 2 operation(s) for unlok util apis.
  name: Level2 Unlok Util APIs API
  slug: level2-unlok-util-apis-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Update Live Deployment Flag API from Level2 — 1 operation(s) for update live deployment flag.
  name: Level2 Update Live Deployment Flag API
  slug: level2-update-live-deployment-flag-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Update Live Deployment Order Flag API from Level2 — 1 operation(s) for update live deployment order flag.
  name: Level2 Update Live Deployment Order Flag API
  slug: level2-update-live-deployment-order-flag-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Update Live Order API from Level2 — 1 operation(s) for update live order.
  name: Level2 Update Live Order API
  slug: level2-update-live-order-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Update Live Trade API from Level2 — 1 operation(s) for update live trade.
  name: Level2 Update Live Trade API
  slug: level2-update-live-trade-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Update Live Trade In Order Book API from Level2 — 1 operation(s) for update live trade in order book.
  name: Level2 Update Live Trade In Order Book API
  slug: level2-update-live-trade-in-order-book-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Update Market Scanner Universe API from Level2 — 1 operation(s) for update market scanner universe.
  name: Level2 Update Market Scanner Universe API
  slug: level2-update-market-scanner-universe-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Update User Description API from Level2 — 1 operation(s) for update user description.
  name: Level2 Update User Description API
  slug: level2-update-user-description-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Update User Preferences API from Level2 — 1 operation(s) for update user preferences.
  name: Level2 Update User Preferences API
  slug: level2-update-user-preferences-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Update User Socials API from Level2 — 1 operation(s) for update user socials.
  name: Level2 Update User Socials API
  slug: level2-update-user-socials-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Upgrade Plan API from Level2 — 1 operation(s) for upgrade plan.
  name: Level2 Upgrade Plan API
  slug: level2-upgrade-plan-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Upload Backtest Report V2 API from Level2 — 1 operation(s) for upload backtest report v2.
  name: Level2 Upload Backtest Report V2 API
  slug: level2-upload-backtest-report-v2-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Upload Profile Image API from Level2 — 1 operation(s) for upload profile image.
  name: Level2 Upload Profile Image API
  slug: level2-upload-profile-image-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Upload Strategy Image API from Level2 — 1 operation(s) for upload strategy image.
  name: Level2 Upload Strategy Image API
  slug: level2-upload-strategy-image-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Validate Sms Otp API from Level2 — 1 operation(s) for validate sms otp.
  name: Level2 Validate Sms Otp API
  slug: level2-validate-sms-otp-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Verify Otp Token API from Level2 — 1 operation(s) for verify otp token.
  name: Level2 Verify Otp Token API
  slug: level2-verify-otp-token-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Verify Session API from Level2 — 1 operation(s) for verify session.
  name: Level2 Verify Session API
  slug: level2-verify-session-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Verify User Account API from Level2 — 1 operation(s) for verify user account.
  name: Level2 Verify User Account API
  slug: level2-verify-user-account-api
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The Verify User API from Level2 — 1 operation(s) for verify user.
  name: Level2 Verify User API
  slug: level2-verify-user-api
artifact_total: 293
collections:
- collection_type: open
  name: Level2 Strategy Builder Backtesting API
  slug: open-level2-backtesting-api
- collection_type: open
  name: Level2 Strategy Builder Backtesting Discovery API
  slug: open-level2-discovery-api
- collection_type: open
  name: Level2 Strategy Builder Backtesting Market Data API
  slug: open-level2-market-data-api
- collection_type: open
  name: Level2 Strategy Builder Backtesting Strategies API
  slug: open-level2-strategies-api
- collection_type: open
  name: Level2 Strategy Builder API
  slug: open-level2-strategy-builder
- collection_type: open
  name: Level2 Strategy Builder Backtesting Technical Analysis API
  slug: open-level2-technical-analysis-api
- collection_type: open
  name: Level2 TradeStation Integration API
  slug: open-level2-tradestation-integration
- collection_type: open
  name: Level2 Strategy Builder Backtesting Users API
  slug: open-level2-users-api
common:
- group: other
  href: https://artifacts.apis.io/level2/capabilities/level2-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/level2-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/level2/agentic-access/level2-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/level2-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/level2/security/level2-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/level2-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/level2/security/level2-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/level2-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/level2/authentication/level2-authentication.yml
  title: ''
  type: Authentication
  url: authentication/level2-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/mylevel2
- group: company
  title: ''
  type: Website
  url: https://www.trylevel2.com
- group: design
  href: https://artifacts.apis.io/level2/json-ld/level2-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/level2-context.jsonld
- group: docs
  href: https://artifacts.apis.io/level2/json-schema/level2-strategy-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/level2-strategy-schema.json
- group: agent
  href: https://artifacts.apis.io/level2/llms/level2-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/level2-llms.txt
- group: agent
  href: https://artifacts.apis.io/level2/well-known/level2-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/level2-well-known.yml
- group: auth
  href: https://artifacts.apis.io/level2/well-known/level2-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/level2-security.txt
- group: auth
  title: ''
  type: Security
  url: https://www.trylevel2.com/security
- group: agent
  href: https://artifacts.apis.io/level2/mcp/level2-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/level2-mcp.yml
- group: other
  href: https://artifacts.apis.io/level2/overlays/level2-hub-controller-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/level2-hub-controller-overlay.yaml
- group: design
  href: https://artifacts.apis.io/level2/conformance/level2-conformance.yml
  title: ''
  type: Conformance
  url: conformance/level2-conformance.yml
- group: design
  href: https://artifacts.apis.io/level2/errors/level2-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/level2-problem-types.yml
- group: design
  href: https://artifacts.apis.io/level2/lifecycle/level2-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/level2-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/level2/conventions/level2-conventions.yml
  title: ''
  type: Conventions
  url: conventions/level2-conventions.yml
- group: start
  href: https://artifacts.apis.io/level2/sandbox/level2-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/level2-sandbox.yml
- group: design
  href: https://artifacts.apis.io/level2/components/level2-components.yml
  title: ''
  type: Components
  url: components/level2-components.yml
- group: design
  href: https://artifacts.apis.io/level2/data-model/level2-data-model.yml
  title: ''
  type: DataModel
  url: data-model/level2-data-model.yml
- group: agent
  href: https://artifacts.apis.io/level2/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  href: https://artifacts.apis.io/level2/packages/level2-packages.yml
  title: ''
  type: Packages
  url: packages/level2-packages.yml
- group: commercial
  href: https://artifacts.apis.io/level2/plans/level2-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/level2-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/level2/rate-limits/level2-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/level2-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/level2/rules/level2-jsonschema-spectral-rules.yml
  title: ''
  type: SpectralRules
  url: rules/level2-jsonschema-spectral-rules.yml
- group: commercial
  href: https://artifacts.apis.io/level2/finops/level2-finops.yml
  title: ''
  type: FinOps
  url: finops/level2-finops.yml
- group: build
  title: ''
  type: Postman
  url: https://learn.trylevel2.com/broker_apis.json
- group: start
  title: ''
  type: DeveloperPortal
  url: https://learn.trylevel2.com/
- group: docs
  title: ''
  type: Documentation
  url: https://learn.trylevel2.com/docs/overview
- group: docs
  title: ''
  type: APIReference
  url: https://learn.trylevel2.com/docs/Broker/API/broker-api
- group: start
  title: ''
  type: GettingStarted
  url: https://learn.trylevel2.com/docs/Broker/getting-started
- group: operate
  title: ''
  type: Support
  url: https://help.trylevel2.com
- group: commercial
  title: ''
  type: Pricing
  url: https://www.trylevel2.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.trylevel2.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.trylevel2.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.trylevel2.com/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bytemine-io
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@trylevel2
created: '2026-05-04'
description: 'Level2 is a no-code systematic-trading platform from Bytemine Technologies Ltd that lets active retail traders build, backtest and deploy fully automated strategies from a visual drag-and-drop canvas, with no code and no proprietary scripting language. Strategies can be rehearsed against historical data or paper-traded with virtual funds before being deployed live through a connected brokerage account. Level2 also sells the platform to brokers and prop firms as an embeddable surface: a customised iframe of the strategy builder, four standalone market widgets, and the Level2 Hub Broker API, which lets a broker register and manage its own customers'' Level2 accounts, read their strategies, deployments, trades and backtests, and measure their execution latency and slippage.'
finops:
- has_sources: true
  method: derived
  name: Level2 Finops
  primary_unit: subscription
  service_category: ''
  slug: level2-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/level2.png
json_schemas:
- name: Level2 Trading Strategy
  property_count: 12
  slug: level2-strategy
jsonld:
- class_count: 0
  name: Level2 Context
  property_count: 7
  slug: level2-context
layout: provider
modified: '2026-09-17'
name: Level2
nav: Providers
network: true
overview: 'Level2 publishes 271 API contracts indexed on the [APIs.io](https://apis.io/) network, including Backtesting API, Discovery API, Market Data API, and 268 more. Tagged areas include Trading, Fintech, Financial Services, Automation, and No-Code.


  The Level2 catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Level2''s developer surface includes authentication, sandbox, documentation, API reference, getting-started guide, support, pricing, and 33 more developer resources.'
plans:
- name: Level2 Plans Pricing
  plan_count: 3
  slug: level2-plans-pricing
- name: Level2 Price Estimates
  plan_count: 0
  slug: level2-price-estimates
random_paper: 10
rate_limits:
- limit_count: 0
  name: Level2 Rate Limits
  slug: level2-rate-limits
rules:
- authorship: generated
  effective_rule_count: 6
  extends: []
  name: Level2 — jsonschema rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: level2-jsonschema-spectral-rules
score:
  band: strong
  composite: 57.6
  coverage:
    artifact_dirs: 28
    catalog_earned: 63.3
    catalog_earned_first_party: 12.0
    catalog_gap: 51.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.1
  facets:
    access_clarity: 84.2
    contract_governance: 14.4
    contract_quality: 46.5
    developer_ergonomics: 68.5
    discoverability: 78.6
    operational_transparency: 13.2
  previous_composite: 56.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 1.1
      derived: 0
      marker_coverage: 97.8
      total: 271
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 34.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 27.8
screenshot: https://apis.io/screenshots/level2/level2-2026-06-20T184439.png
security:
- kind: authentication
  name: Level2 Authentication
  slug: level2-authentication
  summary_line: http/apiKey · 2 schemes
- kind: domain-security
  name: Level2 Domain Security
  slug: level2-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Level2 Vulnerability Disclosure
  slug: level2-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
skill_count: 3
skills:
- name: level2-broker-performance-review
  slug: level2-broker-performance-review
- name: level2-deploy-and-unwind-strategy
  slug: level2-deploy-and-unwind-strategy
- name: level2-onboard-broker-user
  slug: level2-onboard-broker-user
slug: level2
tags:
- Trading
- Fintech
- Financial Services
- Automation
- No-Code
- Backtesting
- Strategies
- Brokerage
- Market Data
- Prediction Markets
website: https://www.trylevel2.com
---
