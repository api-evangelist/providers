---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
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
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 30.1
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Provides authenticated REST endpoints for current fiat rates, gold, crypto, history, and source context.
  name: Market Data API
  slug: market-data-api
- baseURL: https://hub.arzbin.com
  baseurl_source: declared
  description: 'Arzbin API as documented publicly: 6 operations. Contract generated from the documentation by API Evangelist (2026-11-01); not the provider''s own document.'
  name: Arzbin API
  slug: arzbin-com-api
artifact_total: 14
common:
- group: design
  href: https://artifacts.apis.io/arzbin-com/rules/arzbin-com-rules.yml
  title: ''
  type: Spectral
  url: rules/arzbin-com-rules.yml
- group: design
  href: https://artifacts.apis.io/arzbin-com/json-ld/arzbin-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/arzbin-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/arzbin-com/vocabulary/arzbin-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/arzbin-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/arzbin-com/data-model/arzbin-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/arzbin-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/arzbin-com/conformance/arzbin-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/arzbin-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/arzbin-com/llms/arzbin-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/arzbin-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/arzbin-com/mcp/arzbin-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/arzbin-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/arzbin-com/well-known/arzbin-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/arzbin-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/arzbin-com/hosts/arzbin-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/arzbin-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/arzbin-com/vendors/arzbin-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/arzbin-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.arzbin.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.arzbin.com/privacy-policy
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.arzbin.com/developers
- group: company
  title: ''
  type: Blog
  url: https://www.arzbin.com/blog
- group: auth
  href: https://artifacts.apis.io/arzbin-com/security/arzbin-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/arzbin-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.arzbin.com/
coverage:
  checked: '2026-11-02'
  detail: API documentation is public HTML but no OpenAPI/GraphQL/AsyncAPI spec is published.
  evidence:
  - status: 200
    url: https://www.arzbin.com/developers/api
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-01'
description: Arzbin provides live Iran market rates for currencies, gold, and cryptocurrencies, along with market briefs, analysis, Toman converters, and a comprehensive dashboard that tracks daily market movements and price trends across multiple asset classes.
image: https://www.arzbin.com/og-image.png
json_schemas:
- name: GetApiV1MarketCryptoResponse
  property_count: 3
  slug: arzbin-com-get-api-v1-market-crypto-response
- name: GetApiV1MarketGoldResponse
  property_count: 3
  slug: arzbin-com-get-api-v1-market-gold-response
- name: GetApiV1MarketHistoryResponse
  property_count: 3
  slug: arzbin-com-get-api-v1-market-history-response
- name: GetApiV1MarketRatesCodeResponse
  property_count: 3
  slug: arzbin-com-get-api-v1-market-rates-code-response
- name: GetApiV1MarketRatesResponse
  property_count: 3
  slug: arzbin-com-get-api-v1-market-rates-response
- name: GetApiV1MarketSourcesResponse
  property_count: 3
  slug: arzbin-com-get-api-v1-market-sources-response
jsonld:
- class_count: 6
  name: Arzbin Com Context
  property_count: 3
  slug: arzbin-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at hub.arzbin.com.
  name: Arzbin MCP Server
  slug: arzbin-com-mcp-yml
modified: '2026-11-01'
name: Arzbin
nav: Providers
network: true
overview: 'Arzbin is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Finance, Currency, Market Data, Iran, and Cryptocurrency.


  The Arzbin catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Arzbin''s developer surface includes engineering blog and 15 more developer resources.'
random_paper: 2
rules:
- authorship: generated
  effective_rule_count: 84
  extends:
  - spectral:oas
  name: Arzbin API Rules
  rule_count: 43
  severity_counts:
    error: 41
    hint: 0
    info: 1
    warn: 1
  slug: arzbin-com-rules
scopes:
- name: Arzbin Com Scopes
  scope_count: 0
  slug: arzbin-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 19.7
  coverage:
    artifact_dirs: 24
    catalog_earned: 59.8
    catalog_earned_first_party: 0.0
    catalog_gap: 55.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.9
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 24.1
    developer_ergonomics: 6.0
    discoverability: 65.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - iran
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 24.6
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 28.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Arzbin Com Authentication
  slug: arzbin-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Arzbin Com Domain Security
  slug: arzbin-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: arzbin-com
tags:
- Finance
- Currency
- Market Data
- Iran
- Cryptocurrency
- Gold
website: https://www.arzbin.com/
---
