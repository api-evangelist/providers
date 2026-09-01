---
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
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.1
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 281
  human_in_the_loop: 14
  name: Evedex Agentic Access
  operation_count: 557
  slug: evedex-agentic-access
  summary_line: 557 operations · 281 acting · 14 human-in-the-loop
api_count: 11
apis:
- description: The GitBook developer portal and agent-native documentation surface. Every page is retrievable as markdown by appending .md, llms.txt indexes the full corpus, and GitBook exposes an ask= query paramet
  name: EVEDEX Documentation & Agent Surface
  slug: evedex-documentation-agent-surface
- description: Real-time exchange events over WebSocket, brokered by Centrifugo with JWT channel access rights and epoch-based state recovery. Seventeen documented channels cover heartbeat, matcher state, instrument
  name: EVEDEX Async API (Centrifugo)
  slug: evedex-async-api-centrifugo
- description: The ACL API from EVEDEX — 3 operation(s) for acl.
  name: EVEDEX ACL API
  slug: evedex-acl-api
- description: The AI Strategy API from EVEDEX — 5 operation(s) for ai strategy.
  name: EVEDEX AI Strategy API
  slug: evedex-ai-strategy-api
- description: The Aml API from EVEDEX — 3 operation(s) for aml.
  name: EVEDEX Aml API
  slug: evedex-aml-api
- description: The ApiKey API from EVEDEX — 3 operation(s) for apikey.
  name: EVEDEX API Key API
  slug: evedex-apikey-api
- description: The Article API from EVEDEX — 2 operation(s) for article.
  name: EVEDEX Article API
  slug: evedex-article-api
- description: The Auth API from EVEDEX — 11 operation(s) for auth.
  name: EVEDEX Auth API
  slug: evedex-auth-api
- description: The Badge API from EVEDEX — 10 operation(s) for badge.
  name: EVEDEX Badge API
  slug: evedex-badge-api
- description: The Bill API from EVEDEX — 5 operation(s) for bill.
  name: EVEDEX Bill API
  slug: evedex-bill-api
- description: The Blocked API from EVEDEX — 3 operation(s) for blocked.
  name: EVEDEX Blocked API
  slug: evedex-blocked-api
- description: The Bot API from EVEDEX — 6 operation(s) for bot.
  name: EVEDEX Bot API
  slug: evedex-bot-api
- description: The Cashback API from EVEDEX — 2 operation(s) for cashback.
  name: EVEDEX Cashback API
  slug: evedex-cashback-api
- description: The Centrifugo API from EVEDEX — 1 operation(s) for centrifugo.
  name: EVEDEX Centrifugo API
  slug: evedex-centrifugo-api
- description: The Challenges API from EVEDEX — 10 operation(s) for challenges.
  name: EVEDEX Challenges API
  slug: evedex-challenges-api
- description: The Checkout API from EVEDEX — 1 operation(s) for checkout.
  name: EVEDEX Checkout API
  slug: evedex-checkout-api
- description: The Claim stop list API from EVEDEX — 1 operation(s) for claim stop list.
  name: EVEDEX Claim stop list API
  slug: evedex-claim-stop-list-api
- description: The Coin API from EVEDEX — 2 operation(s) for coin.
  name: EVEDEX Coin API
  slug: evedex-coin-api
- description: The Collectable API from EVEDEX — 5 operation(s) for collectable.
  name: EVEDEX Collectable API
  slug: evedex-collectable-api
- description: The Comment API from EVEDEX — 2 operation(s) for comment.
  name: EVEDEX Comment API
  slug: evedex-comment-api
- description: The Competition Templates API from EVEDEX — 3 operation(s) for competition templates.
  name: EVEDEX Competition Templates API
  slug: evedex-competition-templates-api
- description: The Competitions API from EVEDEX — 8 operation(s) for competitions.
  name: EVEDEX Competitions API
  slug: evedex-competitions-api
- description: The Course API from EVEDEX — 10 operation(s) for course.
  name: EVEDEX Course API
  slug: evedex-course-api
- description: The CuratorCourse API from EVEDEX — 2 operation(s) for curatorcourse.
  name: EVEDEX Curator Course API
  slug: evedex-curatorcourse-api
- description: The DailyStatistics API from EVEDEX — 1 operation(s) for dailystatistics.
  name: EVEDEX Daily Statistics API
  slug: evedex-dailystatistics-api
- description: The DailyTask API from EVEDEX — 3 operation(s) for dailytask.
  name: EVEDEX Daily Task API
  slug: evedex-dailytask-api
- description: The Deposit API from EVEDEX — 1 operation(s) for deposit.
  name: EVEDEX Deposit API
  slug: evedex-deposit-api
- description: The Deposit Bonus API from EVEDEX — 4 operation(s) for deposit bonus.
  name: EVEDEX Deposit Bonus API
  slug: evedex-deposit-bonus-api
- description: The Dev API from EVEDEX — 10 operation(s) for dev.
  name: EVEDEX Dev API
  slug: evedex-dev-api
- description: The Discord API from EVEDEX — 3 operation(s) for discord.
  name: EVEDEX Discord API
  slug: evedex-discord-api
- description: The Distribution API from EVEDEX — 5 operation(s) for distribution.
  name: EVEDEX Distribution API
  slug: evedex-distribution-api
- description: The Event API from EVEDEX — 3 operation(s) for event.
  name: EVEDEX Event API
  slug: evedex-event-api
- description: The Exchange API from EVEDEX — 5 operation(s) for exchange.
  name: EVEDEX Exchange API
  slug: evedex-exchange-api
- description: The External API from EVEDEX — 3 operation(s) for external.
  name: EVEDEX External API
  slug: evedex-external-api
- description: The File API from EVEDEX — 10 operation(s) for file.
  name: EVEDEX File API
  slug: evedex-file-api
- description: The Funded Account API from EVEDEX — 3 operation(s) for funded account.
  name: EVEDEX Funded Account API
  slug: evedex-funded-account-api
- description: The GrandContest API from EVEDEX — 7 operation(s) for grandcontest.
  name: EVEDEX Grand Contest API
  slug: evedex-grandcontest-api
- description: The Hedging API from EVEDEX — 2 operation(s) for hedging.
  name: EVEDEX Hedging API
  slug: evedex-hedging-api
- description: The History API from EVEDEX — 5 operation(s) for history.
  name: EVEDEX History API
  slug: evedex-history-api
- description: The Homework API from EVEDEX — 2 operation(s) for homework.
  name: EVEDEX Homework API
  slug: evedex-homework-api
- description: The Invitation API from EVEDEX — 1 operation(s) for invitation.
  name: EVEDEX Invitation API
  slug: evedex-invitation-api
- description: The Journal API from EVEDEX — 1 operation(s) for journal.
  name: EVEDEX Journal API
  slug: evedex-journal-api
- description: The Leaderboard API from EVEDEX — 7 operation(s) for leaderboard.
  name: EVEDEX Leaderboard API
  slug: evedex-leaderboard-api
- description: The League API from EVEDEX — 1 operation(s) for league.
  name: EVEDEX League API
  slug: evedex-league-api
- description: The Lesson API from EVEDEX — 2 operation(s) for lesson.
  name: EVEDEX Lesson API
  slug: evedex-lesson-api
- description: The Link API from EVEDEX — 7 operation(s) for link.
  name: EVEDEX Link API
  slug: evedex-link-api
- description: The Liquidation API from EVEDEX — 1 operation(s) for liquidation.
  name: EVEDEX Liquidation API
  slug: evedex-liquidation-api
- description: The Lucky Shot API from EVEDEX — 8 operation(s) for lucky shot.
  name: EVEDEX Lucky Shot API
  slug: evedex-lucky-shot-api
- description: The Mail API from EVEDEX — 1 operation(s) for mail.
  name: EVEDEX Mail API
  slug: evedex-mail-api
- description: The Market API from EVEDEX — 9 operation(s) for market.
  name: EVEDEX Market API
  slug: evedex-market-api
- description: The Material API from EVEDEX — 2 operation(s) for material.
  name: EVEDEX Material API
  slug: evedex-material-api
- description: The Message API from EVEDEX — 4 operation(s) for message.
  name: EVEDEX Message API
  slug: evedex-message-api
- description: The MobileApp API from EVEDEX — 9 operation(s) for mobileapp.
  name: EVEDEX Mobile App API
  slug: evedex-mobileapp-api
- description: The Module API from EVEDEX — 2 operation(s) for module.
  name: EVEDEX Module API
  slug: evedex-module-api
- description: The Newcomer API from EVEDEX — 2 operation(s) for newcomer.
  name: EVEDEX Newcomer API
  slug: evedex-newcomer-api
- description: The Notification API from EVEDEX — 1 operation(s) for notification.
  name: EVEDEX Notification API
  slug: evedex-notification-api
- description: The Notifications API from EVEDEX — 6 operation(s) for notifications.
  name: EVEDEX Notifications API
  slug: evedex-notifications-api
- description: The Oauth API from EVEDEX — 5 operation(s) for oauth.
  name: EVEDEX OAUTH API
  slug: evedex-oauth-api
- description: The Order API from EVEDEX — 15 operation(s) for order.
  name: EVEDEX Order API
  slug: evedex-order-api
- description: The PaymentService API from EVEDEX — 1 operation(s) for paymentservice.
  name: EVEDEX Payment Service API
  slug: evedex-paymentservice-api
- description: The Paysystem API from EVEDEX — 1 operation(s) for paysystem.
  name: EVEDEX Paysystem API
  slug: evedex-paysystem-api
- description: The Podium API from EVEDEX — 4 operation(s) for podium.
  name: EVEDEX Podium API
  slug: evedex-podium-api
- description: The Points API from EVEDEX — 4 operation(s) for points.
  name: EVEDEX Points API
  slug: evedex-points-api
- description: The Position API from EVEDEX — 4 operation(s) for position.
  name: EVEDEX Position API
  slug: evedex-position-api
- description: The Product API from EVEDEX — 3 operation(s) for product.
  name: EVEDEX Product API
  slug: evedex-product-api
- description: The Promocodes API from EVEDEX — 4 operation(s) for promocodes.
  name: EVEDEX Promocodes API
  slug: evedex-promocodes-api
- description: The Public profile API from EVEDEX — 2 operation(s) for public profile.
  name: EVEDEX Public profile API
  slug: evedex-public-profile-api
- description: The Push API from EVEDEX — 1 operation(s) for push.
  name: EVEDEX Push API
  slug: evedex-push-api
- description: The Quest API from EVEDEX — 4 operation(s) for quest.
  name: EVEDEX Quest API
  slug: evedex-quest-api
- description: The Question API from EVEDEX — 2 operation(s) for question.
  name: EVEDEX Question API
  slug: evedex-question-api
- description: The Redirect API from EVEDEX — 6 operation(s) for redirect.
  name: EVEDEX Redirect API
  slug: evedex-redirect-api
- description: The Referral API from EVEDEX — 1 operation(s) for referral.
  name: EVEDEX Referral API
  slug: evedex-referral-api
- description: The ReferralCompetition API from EVEDEX — 1 operation(s) for referralcompetition.
  name: EVEDEX Referral Competition API
  slug: evedex-referralcompetition-api
- description: The Refund API from EVEDEX — 1 operation(s) for refund.
  name: EVEDEX Refund API
  slug: evedex-refund-api
- description: The Registration request API from EVEDEX — 3 operation(s) for registration request.
  name: EVEDEX Registration request API
  slug: evedex-registration-request-api
- description: The Reward API from EVEDEX — 8 operation(s) for reward.
  name: EVEDEX Reward API
  slug: evedex-reward-api
- description: The Rhino API from EVEDEX — 2 operation(s) for rhino.
  name: EVEDEX Rhino API
  slug: evedex-rhino-api
- description: The Service API from EVEDEX — 2 operation(s) for service.
  name: EVEDEX Service API
  slug: evedex-service-api
- description: The Session API from EVEDEX — 5 operation(s) for session.
  name: EVEDEX Session API
  slug: evedex-session-api
- description: The ShareContent API from EVEDEX — 2 operation(s) for sharecontent.
  name: EVEDEX Share Content API
  slug: evedex-sharecontent-api
- description: The ShortLink API from EVEDEX — 3 operation(s) for shortlink.
  name: EVEDEX Short Link API
  slug: evedex-shortlink-api
- description: The Simulator API from EVEDEX — 2 operation(s) for simulator.
  name: EVEDEX Simulator API
  slug: evedex-simulator-api
- description: The Skill API from EVEDEX — 6 operation(s) for skill.
  name: EVEDEX Skill API
  slug: evedex-skill-api
- description: The SmartAccount API from EVEDEX — 2 operation(s) for smartaccount.
  name: EVEDEX Smart Account API
  slug: evedex-smartaccount-api
- description: The Statistics API from EVEDEX — 6 operation(s) for statistics.
  name: EVEDEX Statistics API
  slug: evedex-statistics-api
- description: The Statistics details API from EVEDEX — 2 operation(s) for statistics details.
  name: EVEDEX Statistics details API
  slug: evedex-statistics-details-api
- description: The Statistics List API from EVEDEX — 3 operation(s) for statistics list.
  name: EVEDEX Statistics List API
  slug: evedex-statistics-list-api
- description: The Strategy API from EVEDEX — 4 operation(s) for strategy.
  name: EVEDEX Strategy API
  slug: evedex-strategy-api
- description: The SubAccount API from EVEDEX — 7 operation(s) for subaccount.
  name: EVEDEX Sub Account API
  slug: evedex-subaccount-api
- description: The Subscription API from EVEDEX — 4 operation(s) for subscription.
  name: EVEDEX Subscription API
  slug: evedex-subscription-api
- description: The Subtitle API from EVEDEX — 2 operation(s) for subtitle.
  name: EVEDEX Subtitle API
  slug: evedex-subtitle-api
- description: The System API from EVEDEX — 2 operation(s) for system.
  name: EVEDEX System API
  slug: evedex-system-api
- description: The Tag API from EVEDEX — 5 operation(s) for tag.
  name: EVEDEX Tag API
  slug: evedex-tag-api
- description: The Tariff API from EVEDEX — 4 operation(s) for tariff.
  name: EVEDEX Tariff API
  slug: evedex-tariff-api
- description: The Telegram API from EVEDEX — 5 operation(s) for telegram.
  name: EVEDEX Telegram API
  slug: evedex-telegram-api
- description: The Template API from EVEDEX — 2 operation(s) for template.
  name: EVEDEX Template API
  slug: evedex-template-api
- description: The TpSl API from EVEDEX — 3 operation(s) for tpsl.
  name: EVEDEX Tp Sl API
  slug: evedex-tpsl-api
- description: The Trade signal API from EVEDEX — 2 operation(s) for trade signal.
  name: EVEDEX Trade signal API
  slug: evedex-trade-signal-api
- description: The Trading Platform API from EVEDEX — 5 operation(s) for trading platform.
  name: EVEDEX Trading Platform API
  slug: evedex-trading-platform-api
- description: The TradingCompetition API from EVEDEX — 1 operation(s) for tradingcompetition.
  name: EVEDEX Trading Competition API
  slug: evedex-tradingcompetition-api
- description: The TradingVolume API from EVEDEX — 1 operation(s) for tradingvolume.
  name: EVEDEX Trading Volume API
  slug: evedex-tradingvolume-api
- description: The Transfer API from EVEDEX — 8 operation(s) for transfer.
  name: EVEDEX Transfer API
  slug: evedex-transfer-api
- description: The User API from EVEDEX — 74 operation(s) for user.
  name: EVEDEX User API
  slug: evedex-user-api
- description: The UserImage API from EVEDEX — 1 operation(s) for userimage.
  name: EVEDEX User Image API
  slug: evedex-userimage-api
- description: The Wallet API from EVEDEX — 1 operation(s) for wallet.
  name: EVEDEX Wallet API
  slug: evedex-wallet-api
- description: The Webhook API from EVEDEX — 3 operation(s) for webhook.
  name: EVEDEX Webhook API
  slug: evedex-webhook-api
- description: The Winner API from EVEDEX — 1 operation(s) for winner.
  name: EVEDEX Winner API
  slug: evedex-winner-api
- description: The Withdraw API from EVEDEX — 3 operation(s) for withdraw.
  name: EVEDEX Withdraw API
  slug: evedex-withdraw-api
- description: The Yield API from EVEDEX — 2 operation(s) for yield.
  name: EVEDEX Yield API
  slug: evedex-yield-api
artifact_total: 116
asyncapis:
- description: ''
  name: Evedex Centrifugo Events
  slug: evedex-centrifugo-events
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/evedex-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/evedex-auth-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/evedex-exchange-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/evedex-market-data-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/evedex-referral-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/evedex-notifications-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/evedex-academy-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/evedex-game-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/evedex-billing-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/evedex-bridge-middleware-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/evedex-ai-strategies-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/evedex-backoffice-overlay.yaml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.evedex.com/developers/developers
- group: docs
  title: ''
  type: Documentation
  url: https://docs.evedex.com/developers/developers
- group: docs
  title: ''
  type: APIReference
  url: https://swagger.evedex.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.evedex.com/developers/developers/toolkit
- group: operate
  title: ''
  type: Support
  url: https://help.evedex.com/
- group: company
  title: ''
  type: Blog
  url: https://blog.evedex.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/evedex-official
- group: operate
  title: ''
  type: Roadmap
  url: https://docs.evedex.com/roadmap
- group: commercial
  title: ''
  type: Pricing
  url: https://docs.evedex.com/key-features-and-components/trading-platform-and-matching-engine/trading-fees
- group: start
  title: ''
  type: SignUp
  url: https://exchange.evedex.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://docs.evedex.com/legal/global/terms-of-use-global
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://docs.evedex.com/legal/global/privacy-policy-global
- group: company
  title: ''
  type: Website
  url: https://evedex.com/
- group: auth
  title: ''
  type: Authentication
  url: authentication/evedex-authentication.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/evedex-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/evedex-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/evedex-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/evedex-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/evedex-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/evedex-mcp.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/evedex-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/evedex-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/evedex-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/evedex-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/evedex-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/evedex-sandbox.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/evedex-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/evedex-plans-pricing.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/evedex-centrifugo-events.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-26'
description: EVEDEX is a hybrid decentralized perpetual-futures exchange built on Arbitrum (Layer 3) that pairs an off-chain order book and matching engine with on-chain settlement and full self-custody, so users trade at centralized-exchange latency without surrendering their keys. Its public developer program spans eleven live OpenAPI 3.1.0 services totalling 557 operations — Auth, Exchange, Market Data, Referral/Affiliate, Notifications, Academy, Game, Billing, Bridge Middleware, AI Strategies and Backoffice — all published from a single Swagger UI at swagger.evedex.com. Authentication is either an X-API-Key issued from the exchange UI or a short-lived JWT minted through EIP-4361 Sign-In with Ethereum, and every write that moves value (order creation, replacement, position closure, withdrawal) additionally requires an EIP-712 typed-data signature from the user's own wallet. Asynchronous state is delivered over seventeen documented Centrifugo WebSocket channels using a snapshot-plus-updates
  consistency pattern. EVEDEX ships an official TypeScript SDK (@evedex/exchange-bot-sdk) with separate demo and production containers, and publishes agent-native documentation via llms.txt and per-page markdown with a GitBook ask-parameter query interface.
image: https://static.evedex.com/images/opengraph/exchange.png
layout: provider
mcp_servers:
- description: ''
  name: EVEDEX MCP Server
  slug: evedex-mcp-server
modified: '2026-08-26'
name: EVEDEX
nav: Providers
network: true
overview: 'EVEDEX publishes 107 APIs on the [APIs.io](https://apis.io/) network, including ACL API, AI Strategy API, Aml API, and 104 more. Tagged areas include Cryptocurrency Exchange, DeFi, Decentralized Exchange, Derivatives, and Perpetual Futures.


  The EVEDEX catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  EVEDEX''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 35 more developer resources.'
plans:
- name: Evedex Plans Pricing
  plan_count: 3
  slug: evedex-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 4
  name: Evedex Rate Limits
  slug: evedex-rate-limits
score:
  band: strong
  composite: 55.7
  coverage:
    artifact_dirs: 22
    catalog_gap: 54.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 63.2
    commercial_clarity: 63.2
    contract_governance: 4.5
    contract_quality: 46.6
    developer_ergonomics: 73.2
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 47.4
  previous_composite: 55.7
  provenance:
    agentic_access: derived
    conformance: derived
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 51.7
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: authentication
  name: Evedex Authentication
  slug: evedex-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Evedex Domain Security
  slug: evedex-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: evedex
tags:
- Cryptocurrency Exchange
- DeFi
- Decentralized Exchange
- Derivatives
- Perpetual Futures
- Trading
- Market Data
- Blockchain
- Web3
- arbitrum-layer3
- Fintech
website: https://evedex.com/
---
