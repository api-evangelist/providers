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
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 19.9
  scored_at: '2026-11-06'
api_count: 3
apis:
- baseURL: https://api.cloud9trader.com
  baseurl_source: spec
  description: Unified API for algorithmic cryptocurrency and forex trading, providing REST and WebSocket endpoints for market data, order execution, and account management.
  name: Cloud9Trader API
  slug: cloud9trader-api
- baseURL: https://api.cloud9trader.com
  baseurl_source: declared
  description: The Cloud9trader API API from Cloud9trader — 1 operation(s) for cloud9trader api.
  name: Cloud9trader Cloud9trader API
  slug: cloud9trader-cloud9trader-api-api
- baseURL: https://api.cloud9trader.com
  baseurl_source: declared
  description: The Currency API from Cloud9trader — 2 operation(s) for currency.
  name: Cloud9trader Currency API
  slug: cloud9trader-currency-api
artifact_total: 10
common:
- group: commercial
  href: https://artifacts.apis.io/cloud9trader/plans/cloud9trader-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/cloud9trader-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/cloud9trader/rules/cloud9trader-rules.yml
  title: ''
  type: Spectral
  url: rules/cloud9trader-rules.yml
- group: design
  href: https://artifacts.apis.io/cloud9trader/json-ld/cloud9trader-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/cloud9trader-context.jsonld
- group: design
  href: https://artifacts.apis.io/cloud9trader/vocabulary/cloud9trader-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/cloud9trader-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/cloud9trader/data-model/cloud9trader-data-model.yml
  title: ''
  type: DataModel
  url: data-model/cloud9trader-data-model.yml
- group: design
  href: https://artifacts.apis.io/cloud9trader/conformance/cloud9trader-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cloud9trader-conformance.yml
- group: other
  href: https://artifacts.apis.io/cloud9trader/hosts/cloud9trader-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cloud9trader-hosts.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://www.cloud9trader.com/pricing
- group: start
  title: ''
  type: Login
  url: https://www.cloud9trader.com/login
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cloud9trader
- group: docs
  title: ''
  type: Documentation
  url: https://www.cloud9trader.com/documentation
- group: docs
  title: ''
  type: APIReference
  url: https://www.cloud9trader.com/documentation/algorithmic-trading/api-reference
- group: auth
  href: https://artifacts.apis.io/cloud9trader/security/cloud9trader-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cloud9trader-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.cloud9trader.com
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 401
    url: https://www.cloud9trader.com/api/mcp
  - status: 200
    url: https://www.cloud9trader.com
  - status: 403
    url: https://equityzen.com/company/cloud9trader
  reason: no-developer-program
  state: none
created: '2026-10-09'
description: Cloud9Trader provides a simple, powerful platform for algorithmic cryptocurrency and forex trading. It offers a unified API to connect to multiple crypto exchanges and forex brokers, delivering reliable JSON and WebSocket APIs for real-time pricing, order execution, and historical data. Users can build, backtest, and deploy trading strategies across markets through a single interface.
image: https://static.cloud9trader.com/0/images/open-graph-preview-2.png
json_schemas:
- name: GetV1CurrencyBtcHistoricalResponse
  property_count: 5
  slug: cloud9trader-get-v1-currency-btc-historical-response
- name: GetV1CurrencyBtcResponse
  property_count: 7
  slug: cloud9trader-get-v1-currency-btc-response
- name: GetV1V1IdResponse
  property_count: 2
  slug: cloud9trader-get-v1-v1-id-response
jsonld:
- class_count: 3
  name: Cloud9Trader Context
  property_count: 13
  slug: cloud9trader-context
layout: provider
modified: '2026-10-09'
name: Cloud9trader
nav: Providers
network: true
overview: 'Cloud9trader is listed with 3 APIs on the [APIs.io](https://apis.io/) network, including Cloud9trader API, Currency API, and 1 more. Tagged areas include Company, Fintech, Cryptocurrency, and Trading.


  The Cloud9trader catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Cloud9trader''s developer surface includes pricing, documentation, API reference, and 11 more developer resources.'
plans:
- name: Cloud9Trader Plans Pricing
  plan_count: 4
  slug: cloud9trader-plans-pricing
random_paper: 10
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: Cloud9trader API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: cloud9trader-rules
score:
  band: emerging
  composite: 23.6
  coverage:
    artifact_dirs: 17
    catalog_earned: 64.8
    catalog_earned_first_party: 12.0
    catalog_gap: 50.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.4
  facets:
    access_clarity: 43.4
    contract_governance: 22.0
    contract_quality: 22.5
    developer_ergonomics: 8.3
    discoverability: 53.6
    operational_transparency: 2.6
  previous_composite: 28.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 3
      marker_coverage: 100.0
      total: 3
    mcp: derived
  regulatory:
    applies: true
    matched_via: weak_tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 15.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/cloud9trader/cloud9trader-2026-11-03T124459.png
security:
- kind: domain-security
  name: Cloud9Trader Domain Security
  slug: cloud9trader-domain-security
  summary_line: TLSv1.3
slug: cloud9trader
tags:
- Company
- Fintech
- Cryptocurrency
- Trading
website: https://www.cloud9trader.com
---
