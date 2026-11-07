---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
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
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 42.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Cspriceapi Com Agentic Access
  operation_count: 14
  slug: cspriceapi-com-agentic-access
  summary_line: 14 operations · 1 acting
api_count: 4
apis:
- baseURL: https://api.cspriceapi.com
  baseurl_source: declared
  description: 'Buy-order price data from supported marketplaces. **Plan: Pro** (included in Enterprise).'
  name: cspriceapi-com Buyorder Prices API
  slug: cspriceapi-com-buyorder-prices-api
- baseURL: https://api.cspriceapi.com
  baseurl_source: declared
  description: 'Float-range filtered listing prices (buckets such as `0.00-0.07`), including listing counts, phase translations for Doppler skins, and fade percentage for Fade skins. **Plan: Pro** (included in Enterp'
  name: cspriceapi-com Float Ranged API
  slug: cspriceapi-com-float-ranged-api
- baseURL: https://api.cspriceapi.com
  baseurl_source: declared
  description: 'Aggregate YouPin market-cap time series for the CS2 skin economy (`price × listing count`, outlier-filtered). Same series as the public Market Index page. **Plan: Enterprise**.'
  name: cspriceapi-com Indexes API
  slug: cspriceapi-com-indexes-api
- baseURL: https://api.cspriceapi.com
  baseurl_source: declared
  description: 'Latest listing prices across marketplaces via `/v1/prices/latest`, plus the single-skin `/v1/prices/search` helper. **Plan: Basic** (included in Pro and Enterprise).'
  name: cspriceapi-com Listing Prices API
  slug: cspriceapi-com-listing-prices-api
- baseURL: https://api.cspriceapi.com
  baseurl_source: declared
  description: Historical listing prices per marketplace. Use `resolution=hourly` for up to ~100 days (≈24 points/day) or `resolution=daily` for the full daily series (1 point/day). Exactly one `market_hash_name` pe
  name: cspriceapi-com Price History API
  slug: cspriceapi-com-price-history-api
- baseURL: https://api.cspriceapi.com
  baseurl_source: declared
  description: 'Daily ZIP/CSV bulk export of historical marketplace sales. Requires a subscription API key scoped to `/v1/market-sales/export`. **Plan: Enterprise** (includes all API endpoints).'
  name: cspriceapi-com Sales Data API
  slug: cspriceapi-com-sales-data-api
- baseURL: https://api.cspriceapi.com
  baseurl_source: declared
  description: 'Steam Community Market data from **`itemordershistogram`**: best ask/bid, spread, order-book depth, and internal liquidity. Requires `item_nameid`. **Plan: Basic** (included in Pro and Enterprise). Le'
  name: cspriceapi-com Steam API
  slug: cspriceapi-com-steam-api
artifact_total: 30
common:
- group: agent
  href: https://artifacts.apis.io/cspriceapi-com/agentic-access/cspriceapi-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/cspriceapi-com-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/cspriceapi-com/plans/cspriceapi-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/cspriceapi-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/cspriceapi-com/rules/cspriceapi-com-rules.yml
  title: ''
  type: Spectral
  url: rules/cspriceapi-com-rules.yml
- group: design
  href: https://artifacts.apis.io/cspriceapi-com/json-ld/cspriceapi-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/cspriceapi-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/cspriceapi-com/vocabulary/cspriceapi-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/cspriceapi-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/cspriceapi-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/cspriceapi-com/data-model/cspriceapi-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/cspriceapi-com-data-model.yml
- group: operate
  href: https://artifacts.apis.io/cspriceapi-com/changelog/cspriceapi-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/cspriceapi-com-changelog.yml
- group: auth
  href: https://artifacts.apis.io/cspriceapi-com/authentication/cspriceapi-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/cspriceapi-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/cspriceapi-com/errors/cspriceapi-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/cspriceapi-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/cspriceapi-com/conformance/cspriceapi-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cspriceapi-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/cspriceapi-com/llms/cspriceapi-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cspriceapi-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/cspriceapi-com/mcp/cspriceapi-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/cspriceapi-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/cspriceapi-com/well-known/cspriceapi-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cspriceapi-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/cspriceapi-com/hosts/cspriceapi-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cspriceapi-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/cspriceapi-com/vendors/cspriceapi-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cspriceapi-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cspriceapi.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cspriceapi.com/legal/privacy
- group: start
  title: ''
  type: Login
  url: https://cspriceapi.com/auth/login
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.cspriceapi.com\
- group: docs
  title: ''
  type: APIReference
  url: https://cspriceapi.com/docs/changelog
- group: auth
  href: https://artifacts.apis.io/cspriceapi-com/security/cspriceapi-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cspriceapi-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cspriceapi.com/
- group: docs
  title: ''
  type: Documentation
  url: https://cspriceapi.com/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://cspriceapi.com/pricing
- group: start
  title: ''
  type: GettingStarted
  url: https://cspriceapi.com/docs/quickstart
- group: operate
  title: ''
  type: Support
  url: https://cspriceapi.com/contact
created: '2026-10-30'
description: CSPriceAPI provides a real-time price data API for CS2 and CS:GO skin marketplaces, aggregating data from 13 Chinese and global marketplaces. It offers a unified JSON schema for price listings, buy orders, and item details, supporting developers building trading bots, dashboards, and price comparison tools. The service includes a Chrome extension, market hub, and extensive documentation for easy integration.
image: https://cspriceapi.com/opengraph-image
json_schemas:
- name: BuffBuyorderResponse
  property_count: 5
  slug: cspriceapi-com-buff-buyorder-response
- name: BuffFloatBuyorderResponse
  property_count: 6
  slug: cspriceapi-com-buff-float-buyorder-response
- name: BuffFloatRangedResponse
  property_count: 5
  slug: cspriceapi-com-buff-float-ranged-response
- name: FloatRangedV2PricesResponse
  property_count: 5
  slug: cspriceapi-com-float-ranged-v2-prices-response
- name: LatestPricesResponse
  property_count: 6
  slug: cspriceapi-com-latest-prices-response
- name: MarketCapResponse
  property_count: 18
  slug: cspriceapi-com-market-cap-response
- name: MarketSalesSearchResponse
  property_count: 7
  slug: cspriceapi-com-market-sales-search-response
- name: PriceHistoryResponse
  property_count: 12
  slug: cspriceapi-com-price-history-response
- name: SearchResponse
  property_count: 0
  slug: cspriceapi-com-search-response
- name: SteamMarketResponse
  property_count: 6
  slug: cspriceapi-com-steam-market-response
- name: YoupinBuyorderResponse
  property_count: 5
  slug: cspriceapi-com-youpin-buyorder-response
- name: YoupinFloatBuyorderResponse
  property_count: 6
  slug: cspriceapi-com-youpin-float-buyorder-response
jsonld:
- class_count: 44
  name: Cspriceapi Com Context
  property_count: 137
  slug: cspriceapi-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at api.cspriceapi.com.
  name: cspriceapi-com MCP Server
  slug: cspriceapi-com-mcp-yml
modified: '2026-10-30'
name: cspriceapi-com
nav: Providers
network: true
overview: 'cspriceapi-com publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Buyorder Prices API, Float Ranged API, Indexes API, and 4 more. Tagged areas include Company, Gaming, Price Data, and Marketplace.


  The cspriceapi-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  cspriceapi-com''s developer surface includes changelog, authentication, API reference, documentation, pricing, getting-started guide, support, and 20 more developer resources.'
plans:
- name: Cspriceapi Com Plans Pricing
  plan_count: 10
  slug: cspriceapi-com-plans-pricing
random_paper: 7
rules:
- authorship: generated
  effective_rule_count: 58
  extends:
  - spectral:oas
  name: cspriceapi-com API Rules
  rule_count: 17
  severity_counts:
    error: 15
    hint: 0
    info: 1
    warn: 1
  slug: cspriceapi-com-rules
score:
  band: developing
  composite: 47.2
  coverage:
    artifact_dirs: 24
    catalog_earned: 72.8
    catalog_earned_first_party: 12.0
    catalog_gap: 42.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -10.2
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 67.1
    developer_ergonomics: 39.8
    discoverability: 61.7
    operational_transparency: 15.8
  previous_composite: 57.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 87.5
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/cspriceapi-com/cspriceapi-com-2026-11-03T125725.png
security:
- kind: authentication
  name: Cspriceapi Com Authentication
  slug: cspriceapi-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Cspriceapi Com Domain Security
  slug: cspriceapi-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 4
skills:
- name: export-market-sales-zip
  slug: cspriceapi-com-exportMarketSalesZip
- name: get-latest-prices
  slug: cspriceapi-com-getLatestPrices
- name: get-market-price-history
  slug: cspriceapi-com-getMarketPriceHistory
- name: get-steam-market
  slug: cspriceapi-com-getSteamMarket
slug: cspriceapi-com
tags:
- Company
- Gaming
- Price Data
- Marketplace
website: https://cspriceapi.com/
---
