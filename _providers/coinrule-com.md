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
  band: agent-ready
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 35.9
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'Coinrule API as documented publicly: 2 operations. Contract generated from the documentation by API Evangelist (2026-11-04); not the provider''s own document.'
  name: Coinrule API
  slug: coinrule-com-api
artifact_total: 6
common:
- group: commercial
  href: https://artifacts.apis.io/coinrule-com/plans/coinrule-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/coinrule-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/coinrule-com/rules/coinrule-com-rules.yml
  title: ''
  type: Spectral
  url: rules/coinrule-com-rules.yml
- group: design
  href: https://artifacts.apis.io/coinrule-com/json-ld/coinrule-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/coinrule-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/coinrule-com/vocabulary/coinrule-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/coinrule-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/coinrule-com/data-model/coinrule-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/coinrule-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/coinrule-com/conformance/coinrule-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/coinrule-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/coinrule-com/llms/coinrule-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/coinrule-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/coinrule-com/well-known/coinrule-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/coinrule-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/coinrule-com/hosts/coinrule-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/coinrule-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/coinrule-com/vendors/coinrule-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/coinrule-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cloud.coinrule.com/terms
- group: operate
  title: ''
  type: Roadmap
  url: https://coinrule.com/trade/roadmap/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cloud.coinrule.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://cloud.coinrule.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://coinrule.com/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://cloud.coinrule.com/docs/getting-started
- group: docs
  title: ''
  type: Documentation
  url: https://help.coinrule.com/
- group: auth
  href: https://artifacts.apis.io/coinrule-com/security/coinrule-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/coinrule-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://coinrule.com/
coverage:
  checked: '2026-11-04'
  detail: The docs pages return XML error blobs and appear to be generated via JavaScript, providing no machine‑readable OpenAPI spec.
  evidence:
  - status: 301
    url: https://coinrule.com/docs/
  - status: 200
    url: https://coinrule.com/docs/
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-04'
description: Coinrule provides AI-powered automated trading bots for crypto and stock markets, enabling users to create, backtest, and run strategies across exchanges like Binance, Kraken, Coinbase, and brokers such as Trading212 and E‑Trade. The platform offers a no‑code interface, advanced indicators, and integrates with large language models for strategy generation, aiming to simplify algorithmic trading for both beginners and professionals.
image: https://coinrule.com/assets/png/Coinrule-Logo-Crypto-Trading-Bot.png
json_schemas:
- name: PostApiWebhooksTradingviewStrategyidRequest
  property_count: 5
  slug: coinrule-com-post-api-webhooks-tradingview-strategyid-request
jsonld:
- class_count: 1
  name: Coinrule Com Context
  property_count: 5
  slug: coinrule-com-context
layout: provider
modified: '2026-11-04'
name: Coinrule
nav: Providers
network: true
overview: 'Coinrule is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include TradingBots, Cryptocurrency, Stocks, ETFs, and Automated Trading.


  The Coinrule catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Coinrule''s developer surface includes pricing, engineering blog, getting-started guide, documentation, and 15 more developer resources.'
plans:
- name: Coinrule Com Plans Pricing
  plan_count: 5
  slug: coinrule-com-plans-pricing
random_paper: 5
rules:
- authorship: generated
  effective_rule_count: 72
  extends:
  - spectral:oas
  name: Coinrule API Rules
  rule_count: 31
  severity_counts:
    error: 29
    hint: 0
    info: 1
    warn: 1
  slug: coinrule-com-rules
score:
  band: thin
  composite: 31.5
  coverage:
    artifact_dirs: 17
    catalog_earned: 60.2
    catalog_earned_first_party: 12.0
    catalog_gap: 54.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.2
    contract_governance: 22.0
    contract_quality: 16.4
    developer_ergonomics: 23.8
    discoverability: 57.1
    operational_transparency: 5.3
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 26.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Coinrule Com Domain Security
  slug: coinrule-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: coinrule-com
tags:
- TradingBots
- Cryptocurrency
- Stocks
- ETFs
- Automated Trading
- Artificial Intelligence
- Exchange
website: https://coinrule.com/
---
