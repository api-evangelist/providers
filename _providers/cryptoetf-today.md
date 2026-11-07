---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
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
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 13.7
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Free REST API for US spot crypto ETF data, providing flows, fund info, pricing and analytics.
  name: CryptoETF API
  slug: cryptoetf-api
- baseURL: https://api.cryptoetf.today/api
  baseurl_source: declared
  description: 'Free REST API for US spot crypto ETF data: daily net flows for 16 assets and for every fund behind them (IBIT, FBTC, ETHA, …), a fund directory with net assets (AUM), the CEFI — Crypto ETF Flow Index,'
  name: CryptoETF API V1 API
  slug: cryptoetf-api-v1-api
artifact_total: 12
common:
- group: design
  href: https://artifacts.apis.io/cryptoetf-today/rules/cryptoetf-today-rules.yml
  title: ''
  type: Spectral
  url: rules/cryptoetf-today-rules.yml
- group: design
  href: https://artifacts.apis.io/cryptoetf-today/json-ld/cryptoetf-today-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/cryptoetf-today-context.jsonld
- group: design
  href: https://artifacts.apis.io/cryptoetf-today/vocabulary/cryptoetf-today-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/cryptoetf-today-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/cryptoetf-today/conformance/cryptoetf-today-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cryptoetf-today-conformance.yml
- group: commercial
  href: https://artifacts.apis.io/cryptoetf-today/plans/cryptoetf-today-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/cryptoetf-today-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/cryptoetf-today/data-model/cryptoetf-today-data-model.yml
  title: ''
  type: DataModel
  url: data-model/cryptoetf-today-data-model.yml
- group: design
  href: https://artifacts.apis.io/cryptoetf-today/errors/cryptoetf-today-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/cryptoetf-today-problem-types.yml
- group: agent
  href: https://artifacts.apis.io/cryptoetf-today/llms/cryptoetf-today-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cryptoetf-today-llms.txt
- group: other
  href: https://artifacts.apis.io/cryptoetf-today/hosts/cryptoetf-today-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cryptoetf-today-hosts.yml
- group: other
  href: https://artifacts.apis.io/cryptoetf-today/vendors/cryptoetf-today-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cryptoetf-today-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cryptoetf.today/en/terms
- group: operate
  title: ''
  type: Support
  url: https://cryptoetf.today/en/support
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cryptoetf.today/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cryptoetf.today/en/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://cryptoetf.today/en/pricing
- group: company
  title: ''
  type: Newsroom
  url: https://cryptoetf.today/en/news
- group: start
  title: ''
  type: Login
  url: https://cryptoetf.today/en/login
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.cryptoetf.today/guide/changelog/
- group: company
  title: ''
  type: Blog
  url: https://cryptoetf.today/en/blog
- group: docs
  title: ''
  type: Documentation
  url: https://docs.cryptoetf.today/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.cryptoetf.today/reference/funds/
- group: auth
  href: https://artifacts.apis.io/cryptoetf-today/security/cryptoetf-today-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cryptoetf-today-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cryptoetf.today/
created: '2026-11-04'
description: CryptoETF provides market data and analytics on US spot crypto ETFs, offering daily inflows and outflows, fund holdings, and issuer breakdowns across 16 assets including Bitcoin, Ethereum, Solana, XRP, and more. It serves worldwide users with comprehensive financial data and insights.
image: https://cryptoetf.today/og?type=home
json_schemas:
- name: AssetFlowsDto
  property_count: 5
  slug: cryptoetf-today-asset-flows-dto
- name: AssetFundFlowsDto
  property_count: 5
  slug: cryptoetf-today-asset-fund-flows-dto
- name: CefiIndexDto
  property_count: 6
  slug: cryptoetf-today-cefi-index-dto
- name: FundsDto
  property_count: 3
  slug: cryptoetf-today-funds-dto
- name: PricesDto
  property_count: 2
  slug: cryptoetf-today-prices-dto
- name: WeeklyAnalyticsDto
  property_count: 3
  slug: cryptoetf-today-weekly-analytics-dto
jsonld:
- class_count: 21
  name: Cryptoetf Today Context
  property_count: 59
  slug: cryptoetf-today-context
layout: provider
modified: '2026-11-04'
name: CryptoETF
nav: Providers
network: true
overview: 'CryptoETF publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network, including API V1 API, and 1 more. Tagged areas include Cryptocurrency, ETFs, Market Data, Analytics, and Finance.


  The CryptoETF catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  CryptoETF''s developer surface includes support, pricing, changelog, engineering blog, documentation, API reference, and 17 more developer resources.'
plans:
- name: Cryptoetf Today Plans Pricing
  plan_count: 4
  slug: cryptoetf-today-plans-pricing
random_paper: 22
rules:
- authorship: generated
  effective_rule_count: 101
  extends:
  - spectral:oas
  name: CryptoETF API Rules
  rule_count: 60
  severity_counts:
    error: 57
    hint: 0
    info: 2
    warn: 1
  slug: cryptoetf-today-rules
score:
  band: developing
  composite: 46.6
  coverage:
    artifact_dirs: 16
    catalog_earned: 74.8
    catalog_earned_first_party: 12.0
    catalog_gap: 40.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 22.0
    contract_quality: 50.7
    developer_ergonomics: 23.8
    discoverability: 67.9
    operational_transparency: 31.6
  provenance:
    conformance: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 23.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cryptoetf Today Domain Security
  slug: cryptoetf-today-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cryptoetf-today
tags:
- Cryptocurrency
- ETFs
- Market Data
- Analytics
- Finance
website: https://cryptoetf.today/
---
