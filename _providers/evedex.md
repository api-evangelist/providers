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
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 281
  human_in_the_loop: 14
  name: Evedex Agentic Access
  operation_count: 557
  slug: evedex-agentic-access
  summary_line: 557 operations · 281 acting · 14 human-in-the-loop
api_count: 13
apis:
- description: 'Identity and authorization for the exchange: EIP-4361 Sign-In with Ethereum nonce and sign-up, JWT access/refresh token issuance and revocation, API key management (including restore of a deleted key)'
  name: Auth Service
  slug: auth-service
- description: 'The trading core: market and matcher state, instrument catalogue, v1 and v2 order creation (limit, market, stop-limit, batch mass-limit), order replacement and cancellation, positions and leverage, TP'
  name: Exchange Service
  slug: exchange-service
- description: Public historical candlestick data by instrument and timeframe, with no authentication required. Returns positional candle tuples (timestamp, open, close, high, low, volumeUsd, volume), capped at 100,
  name: Market Data Service
  slug: market-data-service
- description: 'The partner and affiliate program: referral links, referred-user tracking, commission rewards and partner statistics. 78 operations.'
  name: Referral / Affiliate Service
  slug: referral-affiliate-service
- description: User messaging and notification delivery, mobile app registration and Telegram integration. 28 operations.
  name: Notifications Service
  slug: notifications-service
- description: 'EVEDEX Academy education platform: courses, lessons, tags, files and learner progress. Included with a Prime subscription. 54 operations.'
  name: Academy Service
  slug: academy-service
- description: 'The gamification layer that drives EVEDEX cashback: character levels, trader skills, badges, challenges and streaks, competitions, grand contests, leaderboards, Lucky Shot and collectables. 100 operat'
  name: Game Service
  slug: game-service
- description: 'Prime subscription billing: bills, subscriptions, subscription cancellation and refunds. 14 operations.'
  name: Billing Service
  slug: billing-service
- description: Cross-chain transfer bridging into and out of the exchange, including a transfer refund path. 12 operations.
  name: Bridge Middleware Service
  slug: bridge-middleware-service
- description: AI trading strategy surface. 13 operations, secured solely by an InternalToken bearer scheme, indicating a service that is publicly documented but not intended for third-party callers.
  name: AI Strategies Service
  slug: ai-strategies-service
- description: EVEDEX operator tooling — withdrawal blocking, unblocking and rejection. The OpenAPI is served publicly at backoffice-api.evedex.com but the spec itself declares its server as the internal host backof
  name: Backoffice Service
  slug: backoffice-service
- description: The GitBook developer portal and agent-native documentation surface. Every page is retrievable as markdown by appending .md, llms.txt indexes the full corpus, and GitBook exposes an ask= query paramet
  name: EVEDEX Documentation & Agent Surface
  slug: evedex-documentation-agent-surface
- description: Real-time exchange events over WebSocket, brokered by Centrifugo with JWT channel access rights and epoch-based state recovery. Seventeen documented channels cover heartbeat, matcher state, instrument
  name: EVEDEX Async API (Centrifugo)
  slug: evedex-async-api-centrifugo
artifact_total: 20
asyncapis:
- description: ''
  name: Evedex Centrifugo Events
  slug: evedex-centrifugo-events
common:
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
overview: 'EVEDEX publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Auth Service, Exchange Service, Market Data Service, and 8 more. Tagged areas include cryptocurrency-exchange, defi, decentralized-exchange, derivatives, and perpetual-futures.


  The EVEDEX catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  EVEDEX''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 23 more developer resources.'
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
  composite: 57.8
  facets:
    access_clarity: 63.2
    commercial_clarity: 63.2
    contract_governance: 16.7
    contract_quality: 47.0
    developer_ergonomics: 73.2
    discoverability: 81.5
    governance: 16.7
    operational_transparency: 47.4
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
  schema_version: 0.15.0
  scored_at: '2026-08-26'
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
- cryptocurrency-exchange
- defi
- decentralized-exchange
- derivatives
- perpetual-futures
- trading
- market-data
- blockchain
- web3
- arbitrum-layer3
- fintech
website: https://evedex.com/
---
