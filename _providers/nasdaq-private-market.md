---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 15.1
  scored_at: '2026-09-02'
api_count: 1
apis:
- description: Tape D is NPM's private-company pricing and valuation dataset — real-time private market pricing integrating primary round data, secondary market transactions, mutual fund marks and 409A valuations ac
  name: Nasdaq Private Market Tape D API
  slug: tape-d
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nasdaq-private-market-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.nasdaqprivatemarket.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.nasdaqprivatemarket.com/learning-hub/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.nasdaqprivatemarket.com/learning-hub/
- group: company
  title: ''
  type: Blog
  url: https://www.nasdaqprivatemarket.com/about-us/insights/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.nasdaqprivatemarket.com/about-us/insights/feed/
- group: operate
  title: ''
  type: Support
  url: https://www.nasdaqprivatemarket.com/about-us/contact-us-3/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.nasdaqprivatemarket.com/data-intelligence/
- group: start
  title: ''
  type: SignUp
  url: https://fe.secondmarket.com/preplatform/
- group: start
  title: ''
  type: Login
  url: https://fe.secondmarket.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.nasdaqprivatemarket.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.nasdaqprivatemarket.com/privacy-policy/
- group: commercial
  title: ''
  type: DataTerms
  url: https://www.nasdaqprivatemarket.com/data-terms/
- group: commercial
  title: ''
  type: AITermsOfUse
  url: https://www.nasdaqprivatemarket.com/ai-terms-of-use/
- group: other
  title: ''
  type: DataProcessingAddendum
  url: https://www.nasdaqprivatemarket.com/data-processing-addendum/
- group: auth
  title: ''
  type: Disclosures
  url: https://www.nasdaqprivatemarket.com/disclosures-disclaimers/
- group: agent
  title: ''
  type: WellKnown
  url: well-known/nasdaq-private-market-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/nasdaq-private-market-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/nasdaq-private-market-scopes.yml
- group: other
  title: ''
  type: OpenIDConnect
  url: well-known/nasdaq-private-market-openid-configuration.json
- group: design
  title: ''
  type: Conformance
  url: conformance/nasdaq-private-market-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.nasdaqprivatemarket.com/data-intelligence/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/nasdaq-private-market-llms.txt
coverage:
  checked: '2026-08-04'
  detail: NPM's Data & Intelligence page sells API access only on the Premium "Talk to Sales" tier, and its own "Learn about API Access" call to action is an empty "#" anchor — the Tape D API is distributed exclusively through Nasdaq Data Link, whose public docs index carries no Tape D dataset entry, so no reference or spec is reachable without a sales conversation.
  evidence:
  - status: 200
    url: https://www.nasdaqprivatemarket.com/data-intelligence/
  - status: 200
    url: https://docs.data.nasdaq.com/llms.txt
  - status: 404
    url: https://www.nasdaqprivatemarket.com/openapi.json
  - status: 404
    url: https://www.nasdaqprivatemarket.com/llms.txt
  - status: 404
    url: https://www.nasdaqprivatemarket.com/.well-known/agent-card.json
  reason: sales-gate
  state: gated
created: '2026-08-04'
description: Nasdaq Private Market (NPM) operates infrastructure for the secondary market in pre-IPO private company equity — tender offers, company buybacks, auctions, block trades and a settlement engine for private share transfers — alongside a Data & Intelligence business built on NPM Price, a daily price estimate for 400+ liquid private companies, and Tape D, a private-company pricing dataset combining primary round data, secondary market transactions, mutual fund marks and 409A valuations. Securities are offered through NPM Securities, LLC (member FINRA/SIPC); SecondMarket Financial, LLC is an SEC-registered investment adviser and wholly owned subsidiary. Programmatic access to Tape D is sold on the Premium tier and distributed exclusively through Nasdaq Data Link; NPM itself publishes no developer portal, API reference, or machine-readable specification.
image: https://www.nasdaqprivatemarket.com/wp-content/uploads/2026/05/logo-header.svg
layout: provider
modified: '2026-08-04'
name: Nasdaq Private Market
nav: Providers
network: true
overview: 'Nasdaq Private Market publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Private Markets, Secondary Markets, Market Data, and Financial-Services.


  Nasdaq Private Market''s developer surface includes documentation, getting-started guide, engineering blog, support, pricing, signup flow, authentication, and 16 more developer resources.'
random_paper: 8
scopes:
- name: Nasdaq Private Market Scopes
  scope_count: 7
  slug: nasdaq-private-market-scopes
  summary_line: 7 scopes · authorizationCode/implicit
score:
  band: thin
  composite: 31.1
  coverage:
    artifact_dirs: 8
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 46.1
    commercial_clarity: 46.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 40.5
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 31.1
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 66.7
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/nasdaq-private-market/refs/heads/main/screenshots/nasdaq-private-market-2026-08-07T184636.png
security:
- kind: authentication
  name: Nasdaq Private Market Authentication
  slug: nasdaq-private-market-authentication
  summary_line: openIdConnect/oauth2 · 2 schemes
- kind: domain-security
  name: Nasdaq Private Market Domain Security
  slug: nasdaq-private-market-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: nasdaq-private-market
tags:
- Company
- Private Markets
- Secondary Markets
- Market Data
- Financial-Services
- Valuations
- Pre-IPO Equity
- Capital Markets
website: https://www.nasdaqprivatemarket.com/
---
