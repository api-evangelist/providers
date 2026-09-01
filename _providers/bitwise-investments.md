---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: Bitwise index, ETF, and fund data API — crypto asset prices, index values, and index methodologies. Authentication uses an Authorization header; API keys are issued on request via api@bitwiseinvestmen
  name: Bitwise API
  slug: bitwise-api
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bitwise-investments-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bitwiseinvestments.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.bitwiseinvestments.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.bitwiseinvestments.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developers.bitwiseinvestments.com/
- group: build
  title: ''
  type: Postman
  url: https://developers.bitwiseinvestments.com/
- group: company
  title: ''
  type: Blog
  url: https://bitwiseinvestments.com/crypto-market-insights
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bitwise-invest
- group: start
  title: ''
  type: SignUp
  url: https://experts.bitwiseinvestments.com/sign-up
- group: start
  title: ''
  type: Login
  url: https://app.bitwiseinvestments.com/investor-portal
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bitwiseinvestments.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bitwiseinvestments.com/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.bitwiseinvestments.com/
- group: auth
  title: ''
  type: Authentication
  url: authentication/bitwise-investments-authentication.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/bitwise-investments-lifecycle.yml
created: '2026-07-17'
description: Bitwise Asset Management is one of the world's largest crypto asset managers, founded in 2017 and managing roughly $9 billion in client assets across more than 70 investment products — including crypto index funds, ETFs (such as the Bitwise 10 Crypto Index ETF, BITW, and the Bitwise Bitcoin ETF, BITB), separately managed accounts, private funds, hedge fund strategies, and staking. Bitwise serves thousands of financial advisors, RIAs, family offices, and institutional investors, bridging crypto and traditional finance. The Bitwise API (developers.bitwiseinvestments.com) exposes Bitwise index, ETF, and fund data — crypto asset prices, index values, and methodologies — to partners; access uses an Authorization header with API keys issued on request (api@bitwiseinvestments.com).
image: https://www.datocms-assets.com/62087/1674679915-insights.png?auto=format&fit=max&w=1200
layout: provider
modified: '2026-07-18'
name: Bitwise Investments
nav: Providers
network: true
overview: 'Bitwise Investments publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Crypto, Asset Management, ETFs, and Index Funds.


  Bitwise Investments'' developer surface includes documentation, API reference, engineering blog, signup flow, authentication, and 10 more developer resources.'
random_paper: 4
score:
  band: emerging
  composite: 24.8
  coverage:
    artifact_dirs: 5
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 45.2
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 18.4
  previous_composite: 24.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 33.3
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bitwise-investments/refs/heads/main/screenshots/bitwise-investments-2026-07-25T203216.png
security:
- kind: authentication
  name: Bitwise Investments Authentication
  slug: bitwise-investments-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Bitwise Investments Domain Security
  slug: bitwise-investments-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: bitwise-investments
tags:
- Company
- Crypto
- Asset Management
- ETFs
- Index Funds
- Market Data
- Financial-Services
- Investment Management
website: https://bitwiseinvestments.com
---
