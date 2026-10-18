---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 20.8
  scored_at: '2026-10-17'
api_count: 3
apis:
- description: Provides real‑time commodity price data via REST endpoints such as gold-price and silver-price.
  name: CommodityPriceAPI
  slug: commoditypriceapi
- baseURL: https://api.commoditypriceapi.com
  baseurl_source: declared
  description: The CommodityPriceAPI API API from CommodityPriceAPI — 3 operation(s) for commoditypriceapi api.
  name: CommodityPriceAPI CommodityPriceAPI API
  slug: commoditypriceapi-commoditypriceapi-api-api
- baseURL: https://api.commoditypriceapi.com
  baseurl_source: declared
  description: The Rates API from CommodityPriceAPI — 3 operation(s) for rates.
  name: CommodityPriceAPI Rates API
  slug: commoditypriceapi-rates-api
artifact_total: 12
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/commoditypriceapi/refs/heads/main/plans/commoditypriceapi-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/commoditypriceapi-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/commoditypriceapi/refs/heads/main/rules/commoditypriceapi-rules.yml
  title: ''
  type: Spectral
  url: rules/commoditypriceapi-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/commoditypriceapi/refs/heads/main/json-ld/commoditypriceapi-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/commoditypriceapi-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/commoditypriceapi/refs/heads/main/vocabulary/commoditypriceapi-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/commoditypriceapi-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/commoditypriceapi/refs/heads/main/data-model/commoditypriceapi-data-model.yml
  title: ''
  type: DataModel
  url: data-model/commoditypriceapi-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/commoditypriceapi/refs/heads/main/conformance/commoditypriceapi-conformance.yml
  title: ''
  type: Conformance
  url: conformance/commoditypriceapi-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/commoditypriceapi/refs/heads/main/hosts/commoditypriceapi-hosts.yml
  title: ''
  type: Hosts
  url: hosts/commoditypriceapi-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://commoditypriceapi.com/terms
- group: operate
  title: ''
  type: Support
  url: https://commoditypriceapi.com/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://commoditypriceapi.com/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://commoditypriceapi.com/pricing
- group: start
  title: ''
  type: Login
  url: https://commoditypriceapi.com/auth/signin
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Commodity-Price-API
- group: company
  title: ''
  type: Blog
  url: https://commoditypriceapi.com/blog
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/commoditypriceapi/refs/heads/main/security/commoditypriceapi-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/commoditypriceapi-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://commoditypriceapi.com/
coverage:
  checked: '2026-10-16'
  detail: The provider's website offers API documentation pages but no machine‑readable OpenAPI, AsyncAPI, GraphQL, gRPC or WSDL contracts were found.
  evidence:
  - status: 200
    url: https://commoditypriceapi.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-16'
description: Commodity Price API provides real-time market data for over 520 commodities, including precious metals, oil, and natural gas. Developers can retrieve live price quotes via a simple REST endpoint, enabling integration of up-to-date commodity pricing into applications, dashboards, and trading platforms. The service offers a free trial, no credit card required, and flexible pricing plans for various usage levels.
image: https://commoditypriceapi.com/images/pages/home.png
json_schemas:
- name: GetV2RatesLatestResponse
  property_count: 1
  slug: commoditypriceapi-get-v2-rates-latest-response
- name: GetV3RatesLatestSymbolResponse
  property_count: 4
  slug: commoditypriceapi-get-v3-rates-latest-symbol-response
- name: GetV3RatesRateidResponse
  property_count: 5
  slug: commoditypriceapi-get-v3-rates-rateid-response
- name: GetV3Response
  property_count: 3
  slug: commoditypriceapi-get-v3-response
- name: GetV3V3IdResponse
  property_count: 2
  slug: commoditypriceapi-get-v3-v3-id-response
jsonld:
- class_count: 5
  name: Commoditypriceapi Context
  property_count: 11
  slug: commoditypriceapi-context
layout: provider
modified: '2026-10-16'
name: CommodityPriceAPI
nav: Providers
network: true
overview: 'CommodityPriceAPI is listed with 3 APIs on the [APIs.io](https://apis.io/) network, including CommodityPriceAPI API, Rates API, and 1 more. Tagged areas include Company, Commodities, Finance, and Real-Time.


  The CommodityPriceAPI catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  CommodityPriceAPI''s developer surface includes support, pricing, engineering blog, and 13 more developer resources.'
plans:
- name: Commoditypriceapi Plans Pricing
  plan_count: 4
  slug: commoditypriceapi-plans-pricing
random_paper: 0
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: CommodityPriceAPI API Rules
  rule_count: 13
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 1
  slug: commoditypriceapi-rules
score:
  band: thin
  composite: 32.3
  coverage:
    artifact_dirs: 14
    catalog_earned: 67.8
    catalog_earned_first_party: 12.0
    catalog_gap: 47.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 22.0
    contract_quality: 25.7
    developer_ergonomics: 7.1
    discoverability: 53.6
    operational_transparency: 5.3
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
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.6
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
security:
- kind: domain-security
  name: Commoditypriceapi Domain Security
  slug: commoditypriceapi-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
slug: commoditypriceapi
tags:
- Company
- Commodities
- Finance
- Real-Time
website: https://commoditypriceapi.com/
---
