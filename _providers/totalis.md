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
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 33.3
  scored_at: '2026-10-31'
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
- baseURL: https://api.totalis.trade
  baseurl_source: declared
  description: The RFQs API from Totalis — 2 operation(s) for rfqs.
  name: Totalis RF Qs API
  slug: totalis-rfqs-api
artifact_total: 25
asyncapis:
- description: Totalis pushes HMAC-signed webhook events when positions settle, get bought back, or funds move. Deliveries are at-least-once with exponential-backoff retries and dead-lettering, replayable via the AP
  name: Totalis Webhooks
  slug: totalis-webhooks-asyncapi
- description: Post-trade events in real time — quote acceptances and confirmations, position creation and settlement. Authenticate after connecting with {"type":"auth","api_key":"<key>"}, then subscribe with {"type
  name: Totalis WebSocket
  slug: totalis-websocket-asyncapi
collections:
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
- group: commercial
  href: https://artifacts.apis.io/totalis/plans/totalis-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/totalis-plans-pricing.yml
- group: company
  title: ''
  type: Blog
  url: https://www.totalis.trade/blogs
- group: company
  title: ''
  type: BlogRSS
  url: https://www.totalis.trade/blogs/rss.xml
- group: other
  href: https://artifacts.apis.io/totalis/capabilities/totalis-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/totalis-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/totalis/overlays/totalis-rfq-overlay.yaml
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
  href: https://artifacts.apis.io/totalis/llms/totalis-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/totalis-llms.txt
- group: auth
  href: https://artifacts.apis.io/totalis/authentication/totalis-authentication.yml
  title: ''
  type: Authentication
  url: authentication/totalis-authentication.yml
- group: agent
  href: https://artifacts.apis.io/totalis/mcp/totalis-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/totalis-mcp.yml
- group: docs
  href: https://artifacts.apis.io/totalis/asyncapi/totalis-webhooks-asyncapi.yml
  title: ''
  type: AsyncAPI
  url: asyncapi/totalis-webhooks-asyncapi.yml
- group: design
  href: https://artifacts.apis.io/totalis/asyncapi/totalis-webhooks-asyncapi.yml
  title: ''
  type: Webhooks
  url: asyncapi/totalis-webhooks-asyncapi.yml
- group: design
  href: https://artifacts.apis.io/totalis/errors/totalis-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/totalis-problem-types.yml
- group: design
  href: https://artifacts.apis.io/totalis/conventions/totalis-conventions.yml
  title: ''
  type: Conventions
  url: conventions/totalis-conventions.yml
- group: operate
  href: https://artifacts.apis.io/totalis/rate-limits/totalis-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/totalis-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/totalis/lifecycle/totalis-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/totalis-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/totalis/conformance/totalis-conformance.yml
  title: ''
  type: Conformance
  url: conformance/totalis-conformance.yml
- group: design
  href: https://artifacts.apis.io/totalis/data-model/totalis-data-model.yml
  title: ''
  type: DataModel
  url: data-model/totalis-data-model.yml
- group: auth
  href: https://artifacts.apis.io/totalis/security/totalis-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/totalis-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/totalis/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Totalis (totalis.trade), operated by UCALLEDIT, Inc., is a Y Combinator-backed (Spring 2026) derivatives layer for prediction markets. Users pick two to five outcomes across underlying venues like Kalshi and Polymarket and combine them into a single parlay; market makers compete to price the trade through a request-for-quote (RFQ) system, and positions settle in non-custodial Solana vaults with USDC collateral. The Totalis RFQ API is a documented REST + SSE surface with scoped API keys, a WebSocket for post-trade events, and HMAC-signed webhooks — covering markets, quote requests, parlays, portfolio, funds, and market-maker flows.
finops:
- has_sources: true
  method: derived
  name: Totalis Finops
  primary_unit: bet amount
  service_category: ''
  slug: totalis-finops
  template: false
image: https://www.totalis.trade/favicon.png
layout: provider
modified: '2026-10-06'
name: Totalis
nav: Providers
network: true
overview: 'Totalis publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including API Keys API, Markets API, Portfolio API, and 4 more. Tagged areas include Company, Prediction Markets, Derivatives, Parlays, and Trading.


  The Totalis catalog on APIs.io includes 2 event-driven AsyncAPI specifications.


  Totalis'' developer surface includes engineering blog, documentation, API reference, getting-started guide, signup flow, pricing, FAQ, and 22 more developer resources.'
plans:
- name: Totalis Plans Pricing
  plan_count: 2
  slug: totalis-plans-pricing
- name: Totalis Price Estimates
  plan_count: 0
  slug: totalis-price-estimates
random_paper: 0
rate_limits:
- limit_count: 3
  name: Totalis Rate Limits
  slug: totalis-rate-limits
score:
  band: developing
  composite: 53.1
  coverage:
    artifact_dirs: 22
    catalog_earned: 60.0
    catalog_earned_first_party: 20.0
    catalog_gap: 55.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 6.7
  facets:
    access_clarity: 73.7
    contract_governance: 4.5
    contract_quality: 55.9
    developer_ergonomics: 54.2
    discoverability: 66.1
    operational_transparency: 39.5
  previous_composite: 46.4
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
    score: 28.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: rising
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/totalis/totalis-2026-08-17T082410.png
security:
- kind: authentication
  name: Totalis Authentication
  slug: totalis-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Totalis Domain Security
  slug: totalis-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 3
skills:
- name: Browse Totalis prediction markets
  slug: totalis-browse-markets
- name: Configure and operate Totalis webhooks
  slug: totalis-configure-webhooks
- name: Read a Totalis portfolio, parlays, and P&L
  slug: totalis-read-portfolio-and-pnl
slug: totalis
tags:
- Company
- Prediction Markets
- Derivatives
- Parlays
- Trading
- RFQ
- Solana
- Web3
- Market Data
- Webhook
- Real-Time
- Cryptocurrency
website: https://www.totalis.trade
---
