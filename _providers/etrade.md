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
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Etrade Agentic Access
  operation_count: 8
  slug: etrade-agentic-access
  summary_line: 8 operations · 2 acting
api_count: 1
apis:
- description: Customer account list, balances, portfolio, and transactions
  name: Etrade Accounts API
  slug: etrade-accounts-api
- description: Quotes, option chains, option expirations, and product lookup
  name: Etrade Market API
  slug: etrade-market-api
- description: Preview, place, change, and cancel equity and option orders
  name: Etrade Order API
  slug: etrade-order-api
artifact_total: 14
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: E*TRADE Accounts API
  slug: open-etrade-accounts-api
- collection_type: open
  name: E*TRADE Accounts Market API
  slug: open-etrade-market-api
- collection_type: open
  name: E*TRADE Accounts Order API
  slug: open-etrade-order-api
- collection_type: open
  name: E*TRADE API
  slug: open-etrade
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/etrade-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/etrade-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/etrade-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/etrade
- group: start
  title: ''
  type: Portal
  url: https://us.etrade.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.etrade.com/home
- group: start
  title: ''
  type: Signup
  url: https://developer.etrade.com/home
- group: commercial
  title: ''
  type: TermsOfService
  url: https://us.etrade.com/etx/sd/legaldoc/customer-agreements
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://us.etrade.com/l/f/privacy/security-center
created: '2025-02-17'
description: E*TRADE is an online brokerage firm that provides a platform for investors to trade stocks, options, futures, and bonds. The E*TRADE Developer Platform offers REST APIs for account management, real-time quotes, option chains, and order placement, secured by OAuth 1.0a. The APIs are available to E*TRADE customers who register through the developer portal and provide both a sandbox and production environment.
finops:
- name: Etrade Finops
  service_category: API
  slug: etrade-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/etrade.png
layout: provider
modified: '2026-05-19'
name: Etrade
nav: Providers
network: true
overview: 'Etrade publishes 3 APIs on the [APIs.io](https://apis.io/) network: Accounts API, Market API, and Order API. Tagged areas include Bonds, Brokerage, Financial, Futures, and Options.


  Etrade''s developer surface includes authentication, developer portal, documentation, signup flow, and 5 more developer resources.'
plans:
- name: Etrade Plans Pricing
  plan_count: 3
  slug: etrade-plans-pricing
press:
- date: '2026-05-25'
  title: How to Invest in the Artificial Intelligence (AI) Boom
  url: https://us.etrade.com/knowledge/library/perspectives/market-happenings/megatrends-how-to-invest-in-the-artificial-intelligence
- date: '2026-05-25'
  title: Artificial Intelligence | Learn and Invest | E*TRADE
  url: https://us.etrade.com/knowledge/thematic-investing/artificial-intelligence
- date: '2026-05-25'
  title: Morgan Stanley finalises $13bn E*TRADE acquisition deal
  url: https://www.privatebankerinternational.com/news/morgan-stanley-finalises-13bn-etrade-acquisition-deal/
- date: '2026-05-25'
  title: E*TRADE from Morgan Stanley
  url: https://www.facebook.com/ETRADE/posts/take-your-strategy-to-the-next-level-with-etrades-powerful-platforms-now-superch/1243747861116570/
- date: '2026-05-25'
  title: Morgan Stanley Dives Deeper Into Retail With E*Trade Deal
  url: https://www.wealthmanagement.com/equities/morgan-stanley-dives-deeper-into-retail-with-e-trade-deal
random_paper: 20
rate_limits:
- limit_count: 5
  name: Etrade Rate Limits
  slug: etrade-rate-limits
score:
  band: developing
  composite: 39.9
  coverage:
    artifact_dirs: 12
    catalog_gap: 69.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.6
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 0.0
    contract_quality: 49.0
    developer_ergonomics: 42.9
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 40.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  regulatory:
    applies: true
    matched_via: weak_tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 43.3
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/etrade/refs/heads/main/screenshots/etrade-2026-06-20T180840.png
security:
- kind: authentication
  name: Etrade Authentication
  slug: etrade-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Etrade Domain Security
  slug: etrade-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: etrade
tags:
- Bonds
- Brokerage
- Financial
- Futures
- Options
- Stocks
- Trading
website: https://us.etrade.com/
---
