---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
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
    event_surface_described: derived
    idempotency: verified
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 31.8
  scored_at: '2026-09-04'
api_count: 1
apis:
- baseURL: https://api.totalis.trade
  baseurl_source: declared
  description: Manage programmatic access keys for the authenticated user.
  name: Totalis API Keys API
  slug: totalis-api-keys-api
- baseURL: https://api.totalis.trade
  baseurl_source: declared
  description: Cached Kalshi and Polymarket market data.
  name: Totalis Markets API
  slug: totalis-markets-api
- baseURL: https://api.totalis.trade
  baseurl_source: declared
  description: The Portfolio API from Totalis — 1 operation(s) for portfolio.
  name: Totalis Portfolio API
  slug: totalis-portfolio-api
- baseURL: https://api.totalis.trade
  baseurl_source: declared
  description: The RFQs API from Totalis — 2 operation(s) for rfqs.
  name: Totalis RFQs API
  slug: totalis-rfqs-api
- baseURL: https://api.totalis.trade
  baseurl_source: declared
  description: User profile, wallet, and devnet helpers.
  name: Totalis User API
  slug: totalis-user-api
- baseURL: https://api.totalis.trade
  baseurl_source: declared
  description: The Vault API from Totalis — 1 operation(s) for vault.
  name: Totalis Vault API
  slug: totalis-vault-api
- baseURL: https://api.totalis.trade
  baseurl_source: declared
  description: The Webhooks API from Totalis — 4 operation(s) for webhooks.
  name: Totalis Webhooks API
  slug: totalis-webhooks-api
artifact_total: 20
asyncapis:
- description: Totalis pushes HMAC-signed webhook events when positions settle, get bought back, or funds move. Deliveries are at-least-once with exponential-backoff retries and dead-lettering, replayable via the AP
  name: Totalis Webhooks
  slug: totalis-webhooks-asyncapi
- description: Post-trade events in real time — quote acceptances and confirmations, position creation and settlement. Authenticate after connecting with {"type":"auth","api_key":"<key>"}, then subscribe with {"type
  name: Totalis WebSocket
  slug: totalis-websocket-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Totalis RFQ API Keys API
  slug: open-totalis-api-keys-api
- collection_type: open
  name: Totalis RFQ API Keys Markets API
  slug: open-totalis-markets-api
- collection_type: open
  name: Totalis RFQ API Keys Portfolio API
  slug: open-totalis-portfolio-api
- collection_type: open
  name: Totalis RFQ API Keys RFQs API
  slug: open-totalis-rfqs-api
- collection_type: open
  name: Totalis RFQ API Keys User API
  slug: open-totalis-user-api
- collection_type: open
  name: Totalis RFQ API Keys Vault API
  slug: open-totalis-vault-api
- collection_type: open
  name: Totalis RFQ API Keys Webhooks API
  slug: open-totalis-webhooks-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/totalis-rfq-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.totalis.trade
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.totalis.trade
- group: docs
  title: ''
  type: Documentation
  url: https://docs.totalis.trade
- group: docs
  title: ''
  type: APIReference
  url: https://docs.totalis.trade/api-reference/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.totalis.trade/guides/quickstart
- group: start
  title: ''
  type: SignUp
  url: https://app.totalis.trade
- group: commercial
  title: ''
  type: Pricing
  url: https://docs.totalis.trade/guides/faq
- group: operate
  title: ''
  type: FAQ
  url: https://docs.totalis.trade/guides/faq
- group: commercial
  title: ''
  type: TermsOfService
  url: https://docs.totalis.trade/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://docs.totalis.trade/privacy-policy
- group: company
  title: ''
  type: Twitter
  url: https://x.com/totalistrading
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/totalis-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/totalis-authentication.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/totalis-mcp.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/totalis-webhooks-asyncapi.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/totalis-webhooks-asyncapi.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/totalis-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/totalis-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/totalis-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/totalis-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/totalis-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/totalis-data-model.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/totalis-domain-security.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Totalis (totalis.trade), operated by UCALLEDIT, Inc., is a Y Combinator-backed (Spring 2026) derivatives layer for prediction markets. Users pick two to five outcomes across underlying venues like Kalshi and Polymarket and combine them into a single parlay; market makers compete to price the trade through a request-for-quote (RFQ) system, and positions settle in non-custodial Solana vaults with USDC collateral. The Totalis RFQ API is a documented REST + SSE surface with scoped API keys, a WebSocket for post-trade events, and HMAC-signed webhooks — covering markets, quote requests, parlays, portfolio, funds, and market-maker flows.
image: https://www.totalis.trade/favicon.png
layout: provider
modified: '2026-07-21'
name: Totalis
nav: Providers
network: true
overview: 'Totalis publishes 7 APIs on the [APIs.io](https://apis.io/) network, including API Keys API, Markets API, Portfolio API, and 4 more. Tagged areas include Company, Prediction Markets, Derivatives, Parlays, and Trading.


  The Totalis catalog on APIs.io includes 2 event-driven AsyncAPI specifications.


  Totalis'' developer surface includes documentation, API reference, getting-started guide, signup flow, pricing, FAQ, authentication, and 18 more developer resources.'
random_paper: 12
rate_limits:
- limit_count: 3
  name: Totalis Rate Limits
  slug: totalis-rate-limits
score:
  band: developing
  composite: 48.8
  coverage:
    artifact_dirs: 17
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 4.5
    contract_quality: 61.2
    developer_ergonomics: 51.8
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 39.5
  previous_composite: 48.8
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 41.7
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/totalis/refs/heads/main/screenshots/totalis-2026-08-17T082410.png
security:
- kind: authentication
  name: Totalis Authentication
  slug: totalis-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Totalis Domain Security
  slug: totalis-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: totalis
tags:
- Company
- Prediction Markets
- Derivatives
- Parlays
- Trading
- RFQ
- Solana
- Crypto Web3
- Market Data
- Webhook
website: https://www.totalis.trade
---
