---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Open access
  onboarding: open
  pricing: freemium
  public: true
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
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
    idempotency: verified
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: mostly
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 35.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 10
  human_in_the_loop: 0
  name: Firstrade Agentic Access
  operation_count: 24
  slug: firstrade-agentic-access
  summary_line: 24 operations · 10 acting
api_count: 1
apis:
- description: 'Access to Firstrade account data is available through the Plaid financial data aggregation platform. Plaid supports four product categories for Firstrade: Assets (consolidated balance summaries and as'
  name: Firstrade Account Data API (via Plaid)
  slug: firstrade-account-data-api-via-plaid
- baseURL: https://production.plaid.com
  baseurl_source: declared
  description: The Plaid API
  name: Firstrade Plaid API
  slug: firstrade-plaid-api
artifact_total: 14
collections:
- collection_type: open
  name: Firstrade Unofficial Account API
  slug: open-firstrade-account-api
- collection_type: open
  name: Firstrade Unofficial Account Authentication API
  slug: open-firstrade-authentication-api
- collection_type: open
  name: Firstrade Unofficial Account Market Data API
  slug: open-firstrade-market-data-api
- collection_type: open
  name: Firstrade Unofficial Account Orders API
  slug: open-firstrade-orders-api
- collection_type: open
  name: Firstrade Unofficial Account Watchlist API
  slug: open-firstrade-watchlist-api
common:
- group: commercial
  href: https://artifacts.apis.io/firstrade/plans/plans.yml
  title: ''
  type: Plans
  url: plans/plans.yml
- group: operate
  href: https://artifacts.apis.io/firstrade/rate-limits/rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/firstrade/finops/finops.yml
  title: ''
  type: FinOps
  url: finops/finops.yml
- group: other
  href: https://artifacts.apis.io/firstrade/capabilities/firstrade-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/firstrade-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/firstrade/agentic-access/firstrade-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/firstrade-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/firstrade/security/firstrade-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/firstrade-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/firstrade/authentication/firstrade-authentication.yml
  title: ''
  type: Authentication
  url: authentication/firstrade-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.firstrade.com/
- group: other
  title: ''
  type: Trading
  url: https://www.firstrade.com/trading
- group: commercial
  title: ''
  type: Pricing
  url: https://www.firstrade.com/trading/pricing
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.firstrade.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.firstrade.com/content/en-us/aboutus/privacypolicy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.firstrade.com/content/en-us/aboutus/termsofuse
- group: company
  title: ''
  type: PressCenter
  url: https://www.firstrade.com/press
- group: other
  title: ''
  type: MobileApp
  url: https://apps.apple.com/us/app/firstrade-invest-trade/id405325225
- group: other
  title: ''
  type: OpenBankingTracker
  url: https://www.openbankingtracker.com/provider/firstrade
- group: build
  title: ''
  type: PlaidIntegration
  url: https://plaid.com/institutions/firstrade/
created: '2026-06-13'
description: Firstrade Securities is a commission-free online brokerage offering trading in stocks, ETFs, options, mutual funds, and fixed income securities with no account minimums and no inactivity fees. Firstrade does not publish an official public REST API; programmatic account access is available through the Plaid financial data aggregator, which supports account balance retrieval, transaction history, investment holdings, and asset reports for Firstrade accounts. Community-developed unofficial Python SDKs also exist for session- based automation but are not affiliated with or endorsed by Firstrade.
finops:
- has_sources: false
  method: generated
  name: Finops
  primary_unit: ''
  service_category: ''
  slug: finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/firstrade.png
layout: provider
modified: '2026-06-13'
name: Firstrade
nav: Providers
network: true
overview: 'Firstrade publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network, including Plaid API, and 1 more. Tagged areas include Brokerage, Commission-Free Trading, Stocks, ETFs, and Options.


  The Firstrade catalog on APIs.io includes 1 Spectral governance ruleset.


  Firstrade''s developer surface includes authentication, pricing, and 15 more developer resources.'
plans:
- name: Plans
  plan_count: 2
  slug: plans
random_paper: 4
rate_limits:
- limit_count: 0
  name: Rate Limits
  slug: rate-limits
rules:
- authorship: generated
  effective_rule_count: 109
  extends:
  - spectral:oas
  name: Firstrade API Rules
  rule_count: 68
  severity_counts:
    error: 54
    hint: 0
    info: 1
    warn: 13
  slug: firstrade-rules
score:
  band: thin
  composite: 37.5
  coverage:
    artifact_dirs: 17
    catalog_earned: 43.5
    catalog_earned_first_party: 0.0
    catalog_gap: 71.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.2
  facets:
    access_clarity: 36.8
    contract_governance: 13.6
    contract_quality: 52.8
    developer_ergonomics: 28.6
    discoverability: 66.1
    operational_transparency: 0.0
  previous_composite: 37.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 14.3
      total: 7
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 18.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 38.9
screenshot: https://apis.io/screenshots/firstrade/firstrade-2026-06-20T181243.png
security:
- kind: authentication
  name: Firstrade Authentication
  slug: firstrade-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Firstrade Domain Security
  slug: firstrade-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: firstrade
tags:
- Brokerage
- Commission-Free Trading
- Stocks
- ETFs
- Options
- Mutual Funds
- Fixed Income
- Retirement
- IRA
- Investing
- Finance
- Open Banking
- Financial Services
website: https://www.firstrade.com/
---
