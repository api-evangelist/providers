---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
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
    error_semantics: false
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
    well_known_catalog: true
  schema_version: '0.2'
  score: 15.8
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Real-time synchronous Amazon data extraction API. Instantly fetch product titles, prices, and ratings with direct responses. Ideal for on-demand single ASIN lookups.
  name: Amazon Scraper API
  slug: amazon-scraper-api
- baseURL: https://scrapeapi.pangolinfo.com
  baseurl_source: declared
  description: 'pangolinfo-com API as documented publicly: 27 operations. Contract generated from the documentation by API Evangelist (2026-10-30); not the provider''s own document.'
  name: pangolinfo-com API
  slug: pangolinfo-com-api
artifact_total: 11
common:
- group: design
  href: https://artifacts.apis.io/pangolinfo-com/rules/pangolinfo-com-rules.yml
  title: ''
  type: Spectral
  url: rules/pangolinfo-com-rules.yml
- group: design
  href: https://artifacts.apis.io/pangolinfo-com/json-ld/pangolinfo-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/pangolinfo-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/pangolinfo-com/vocabulary/pangolinfo-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/pangolinfo-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/pangolinfo-com/data-model/pangolinfo-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/pangolinfo-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/pangolinfo-com/conformance/pangolinfo-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/pangolinfo-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/pangolinfo-com/llms/pangolinfo-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/pangolinfo-com-llms.txt
- group: other
  href: https://artifacts.apis.io/pangolinfo-com/hosts/pangolinfo-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/pangolinfo-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/pangolinfo-com/vendors/pangolinfo-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/pangolinfo-com-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.pangolinfo.com/privacy-policy/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.pangolinfo.com/en-help-center/mcp/agents
- group: auth
  href: https://artifacts.apis.io/pangolinfo-com/security/pangolinfo-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/pangolinfo-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://pangolinfo.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.pangolinfo.com/en-index
- group: company
  title: ''
  type: Blog
  url: https://blog.pangolinfo.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.pangolinfo.com/pricing/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Pangolin-spg
coverage:
  checked: '2026-10-30'
  detail: Documentation pages describe APIs but no OpenAPI/AsyncAPI/GraphQL spec was found despite probing common spec URLs.
  evidence:
  - status: 404
    url: https://www.pangolinfo.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-30'
description: Pangolinfo provides structured Amazon and search engine data through APIs, MCP servers, and AI skills. It helps developers, e-commerce teams, and AI agents access product, review, seller, category, and search result data for market research, competitive analysis, and workflow automation.
image: https://www.pangolinfo.com/wp-content/uploads/2026/06/pangolinfo-amazon-data-api-cover-en.webp
json_schemas:
- name: PostApiV1AmzscopeCategoriesFilterResponse
  property_count: 1
  slug: pangolinfo-com-post-api-v1-amzscope-categories-filter-response
- name: PostApiV1AmzscopeNichesFilterResponse
  property_count: 1
  slug: pangolinfo-com-post-api-v1-amzscope-niches-filter-response
- name: PostApiV1RevenueCalculatorResponse
  property_count: 2
  slug: pangolinfo-com-post-api-v1-revenue-calculator-response
- name: PostApiV3PacerResponse
  property_count: 16
  slug: pangolinfo-com-post-api-v3-pacer-response
- name: PostApiV3WipoResponse
  property_count: 21
  slug: pangolinfo-com-post-api-v3-wipo-response
- name: PostRevenueCalculatorRequest
  property_count: 12
  slug: pangolinfo-com-post-revenue-calculator-request
jsonld:
- class_count: 51
  name: Pangolinfo Com Context
  property_count: 117
  slug: pangolinfo-com-context
layout: provider
modified: '2026-10-30'
name: pangolinfo-com
nav: Providers
network: true
overview: 'pangolinfo-com is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, E-Commerce, Data API, Amazon, and Artificial Intelligence.


  The pangolinfo-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  pangolinfo-com''s developer surface includes getting-started guide, documentation, engineering blog, pricing, and 12 more developer resources.'
random_paper: 17
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: pangolinfo-com API Rules
  rule_count: 14
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 3
  slug: pangolinfo-com-rules
score:
  band: emerging
  composite: 20.2
  coverage:
    artifact_dirs: 18
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.1
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 26.3
    developer_ergonomics: 11.9
    discoverability: 73.2
    operational_transparency: 2.6
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 25.3
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/pangolinfo-com/pangolinfo-com-2026-11-03T140918.png
security:
- kind: domain-security
  name: Pangolinfo Com Domain Security
  slug: pangolinfo-com-domain-security
  summary_line: TLSv1.3 · HSTS
slug: pangolinfo-com
tags:
- Company
- E-Commerce
- Data API
- Amazon
- Artificial Intelligence
website: https://pangolinfo.com/
---
