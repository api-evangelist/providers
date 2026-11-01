---
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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 24.6
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Marketparquet Agentic Access
  operation_count: 4
  slug: marketparquet-agentic-access
  summary_line: 4 operations
api_count: 1
apis:
- baseURL: https://marketparquet.com
  baseurl_source: spec
  description: The api-v1 API from MarketParquet — 4 operation(s) for api-v1.
  name: MarketParquet API V1 API
  slug: marketparquet-api-v1-api
artifact_total: 7
common:
- group: agent
  href: https://artifacts.apis.io/marketparquet/agentic-access/marketparquet-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/marketparquet-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/marketparquet/plans/marketparquet-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/marketparquet-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/marketparquet/rules/marketparquet-rules.yml
  title: ''
  type: Spectral
  url: rules/marketparquet-rules.yml
- group: design
  href: https://artifacts.apis.io/marketparquet/json-ld/marketparquet-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/marketparquet-context.jsonld
- group: design
  href: https://artifacts.apis.io/marketparquet/vocabulary/marketparquet-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/marketparquet-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/marketparquet/data-model/marketparquet-data-model.yml
  title: ''
  type: DataModel
  url: data-model/marketparquet-data-model.yml
- group: operate
  href: https://artifacts.apis.io/marketparquet/changelog/marketparquet-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/marketparquet-changelog.yml
- group: design
  href: https://artifacts.apis.io/marketparquet/errors/marketparquet-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/marketparquet-problem-types.yml
- group: design
  href: https://artifacts.apis.io/marketparquet/conformance/marketparquet-conformance.yml
  title: ''
  type: Conformance
  url: conformance/marketparquet-conformance.yml
- group: agent
  href: https://artifacts.apis.io/marketparquet/llms/marketparquet-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/marketparquet-llms.txt
- group: other
  href: https://artifacts.apis.io/marketparquet/hosts/marketparquet-hosts.yml
  title: ''
  type: Hosts
  url: hosts/marketparquet-hosts.yml
- group: other
  href: https://artifacts.apis.io/marketparquet/vendors/marketparquet-vendors.yml
  title: ''
  type: Vendors
  url: vendors/marketparquet-vendors.yml
- group: auth
  href: https://artifacts.apis.io/marketparquet/authentication/marketparquet-authentication.yml
  title: ''
  type: Authentication
  url: authentication/marketparquet-authentication.yml
- group: auth
  href: https://artifacts.apis.io/marketparquet/security/marketparquet-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/marketparquet-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://marketparquet.com/
- group: docs
  title: ''
  type: Documentation
  url: https://marketparquet.com/documentation
- group: commercial
  title: ''
  type: Pricing
  url: https://marketparquet.com/pricing
- group: start
  title: ''
  type: Login
  url: https://marketparquet.com/auth/login
- group: start
  title: ''
  type: SignUp
  url: https://marketparquet.com/auth/register
- group: commercial
  title: ''
  type: TermsOfService
  url: https://marketparquet.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://marketparquet.com/privacy
- group: operate
  title: ''
  type: ChangeLog
  url: https://marketparquet.com/changelog
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: 401
    url: https://marketparquet.com/mcp
  - status: 200
    url: https://marketparquet.com/
  reason: partner-login
  state: gated
created: '2026-10-18'
description: MarketParquet provides historical US stock, ETF, and futures market data in columnar Parquet format. It offers split‑adjusted OHLCV bars from 2000 to present, including delisted tickers, with free daily samples and a paid complete archive. The service targets quantitative analysts, backtesters, and data scientists needing high‑performance, ready‑to‑load datasets for pandas, Polars, or DuckDB.
image: https://marketparquet.com/static/og-image.png
jsonld:
- class_count: 1
  name: Marketparquet Context
  property_count: 1
  slug: marketparquet-context
layout: provider
modified: '2026-10-18'
name: MarketParquet
nav: Providers
network: true
overview: 'MarketParquet publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: API V1 API. Tagged areas include Company, Finance, Data, and Market Data.


  The MarketParquet catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  MarketParquet''s developer surface includes changelog, authentication, documentation, pricing, signup flow, and 17 more developer resources.'
plans:
- name: Marketparquet Plans Pricing
  plan_count: 3
  slug: marketparquet-plans-pricing
random_paper: 22
rules:
- authorship: generated
  effective_rule_count: 56
  extends:
  - spectral:oas
  name: MarketParquet API Rules
  rule_count: 15
  severity_counts:
    error: 13
    hint: 0
    info: 1
    warn: 1
  slug: marketparquet-rules
score:
  band: developing
  composite: 43.4
  coverage:
    artifact_dirs: 21
    catalog_earned: 49.8
    catalog_earned_first_party: 12.0
    catalog_gap: 65.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.1
  facets:
    access_clarity: 76.3
    contract_governance: 22.0
    contract_quality: 52.4
    developer_ergonomics: 21.4
    discoverability: 48.2
    operational_transparency: 15.8
  previous_composite: 44.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 28.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Marketparquet Authentication
  slug: marketparquet-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Marketparquet Domain Security
  slug: marketparquet-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: marketparquet
tags:
- Company
- Finance
- Data
- Market Data
website: https://marketparquet.com/
---
