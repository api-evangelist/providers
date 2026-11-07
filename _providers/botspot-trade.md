---
access_model:
  confidence: low
  label: Paid
  onboarding: unknown
  pricing: paid
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
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
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
    well_known_catalog: false
  schema_version: '0.2'
  score: 35.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Botspot Trade Agentic Access
  operation_count: 5
  slug: botspot-trade-agentic-access
  summary_line: 5 operations
api_count: 1
apis:
- baseURL: https://botspot.trade
  baseurl_source: declared
  description: The Llms.txt API from botspot-trade — 1 operation(s) for llms.txt.
  name: botspot-trade Llms.txt API
  slug: botspot-trade-llms-txt-api
- baseURL: https://botspot.trade
  baseurl_source: declared
  description: The Openapi.json API from botspot-trade — 1 operation(s) for openapi.json.
  name: botspot-trade Openapi.json API
  slug: botspot-trade-openapi-json-api
- baseURL: https://botspot.trade
  baseurl_source: declared
  description: The Sitemap.xml API from botspot-trade — 1 operation(s) for sitemap.xml.
  name: botspot-trade Sitemap.xml API
  slug: botspot-trade-sitemap-xml-api
- baseURL: https://botspot.trade
  baseurl_source: declared
  description: The .well Known API from botspot-trade — 2 operation(s) for .well known.
  name: botspot-trade .well Known API
  slug: botspot-trade-well-known-api
artifact_total: 10
common:
- group: agent
  href: https://artifacts.apis.io/botspot-trade/agentic-access/botspot-trade-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/botspot-trade-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/botspot-trade/plans/botspot-trade-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/botspot-trade-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/botspot-trade/rules/botspot-trade-rules.yml
  title: ''
  type: Spectral
  url: rules/botspot-trade-rules.yml
- group: design
  href: https://artifacts.apis.io/botspot-trade/json-ld/botspot-trade-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/botspot-trade-context.jsonld
- group: design
  href: https://artifacts.apis.io/botspot-trade/vocabulary/botspot-trade-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/botspot-trade-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/botspot-trade/data-model/botspot-trade-data-model.yml
  title: ''
  type: DataModel
  url: data-model/botspot-trade-data-model.yml
- group: design
  href: https://artifacts.apis.io/botspot-trade/errors/botspot-trade-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/botspot-trade-problem-types.yml
- group: design
  href: https://artifacts.apis.io/botspot-trade/conformance/botspot-trade-conformance.yml
  title: ''
  type: Conformance
  url: conformance/botspot-trade-conformance.yml
- group: agent
  href: https://artifacts.apis.io/botspot-trade/llms/botspot-trade-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/botspot-trade-llms.txt
- group: agent
  href: https://artifacts.apis.io/botspot-trade/well-known/botspot-trade-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/botspot-trade-well-known.yml
- group: other
  href: https://artifacts.apis.io/botspot-trade/hosts/botspot-trade-hosts.yml
  title: ''
  type: Hosts
  url: hosts/botspot-trade-hosts.yml
- group: other
  href: https://artifacts.apis.io/botspot-trade/vendors/botspot-trade-vendors.yml
  title: ''
  type: Vendors
  url: vendors/botspot-trade-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://botspot.trade/terms
- group: operate
  title: ''
  type: Support
  url: https://botspot.trade/help
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://botspot.trade/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://botspot.trade/pricing
- group: company
  title: ''
  type: Blog
  url: https://botspot.trade/blog
- group: docs
  title: ''
  type: Documentation
  url: https://dev.botspot.trade/
- group: docs
  title: ''
  type: APIReference
  url: https://dev.botspot.trade/llms.txt
- group: auth
  href: https://artifacts.apis.io/botspot-trade/security/botspot-trade-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/botspot-trade-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://botspot.trade/
created: '2026-11-02'
description: BotSpot offers an AI‑driven trading bot builder and backtesting platform that lets users describe trading ideas in plain English, generate bots, test them on historical data, and run them through supported brokers such as Alpaca, Tradier, Tradovate, Kraken, or Coinbase. The service includes an AI Agent for market research, a marketplace of strategy templates, and educational programs like the AI Trading Bootcamp, targeting traders who want to automate strategies without coding.
image: https://botspot.trade/social-share-image.jpg
json_schemas:
- name: PublicManifest
  property_count: 5
  slug: botspot-trade-public-manifest
jsonld:
- class_count: 2
  name: Botspot Trade Context
  property_count: 6
  slug: botspot-trade-context
layout: provider
modified: '2026-11-02'
name: botspot-trade
nav: Providers
network: true
overview: 'botspot-trade publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Llms.txt API, Openapi.json API, Sitemap.xml API, and 1 more. Tagged areas include AI Trading, Bot Builder, Backtesting, and Trading Platform.


  The botspot-trade catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  botspot-trade''s developer surface includes support, pricing, engineering blog, documentation, API reference, and 16 more developer resources.'
plans:
- name: Botspot Trade Plans Pricing
  plan_count: 4
  slug: botspot-trade-plans-pricing
random_paper: 8
rules:
- authorship: generated
  effective_rule_count: 76
  extends:
  - spectral:oas
  name: botspot-trade API Rules
  rule_count: 35
  severity_counts:
    error: 32
    hint: 0
    info: 2
    warn: 1
  slug: botspot-trade-rules
score:
  band: thin
  composite: 33.6
  coverage:
    artifact_dirs: 18
    catalog_earned: 60.2
    catalog_earned_first_party: 12.0
    catalog_gap: 54.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 47.4
    contract_governance: 22.0
    contract_quality: 51.0
    developer_ergonomics: 11.9
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 25.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Botspot Trade Domain Security
  slug: botspot-trade-domain-security
  summary_line: TLSv1.3 · DMARC
slug: botspot-trade
tags:
- AI Trading
- Bot Builder
- Backtesting
- Trading Platform
website: https://botspot.trade/
---
