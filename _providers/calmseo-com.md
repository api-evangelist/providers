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
    auth_clarity: bearer
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
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 17.3
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://api.calmseo.com
  baseurl_source: declared
  description: 'CalmSEO API as documented publicly: 16 operations. Contract generated from the documentation by API Evangelist (2026-11-04); not the provider''s own document.'
  name: CalmSEO API
  slug: calmseo-com-api
artifact_total: 10
common:
- group: design
  href: https://artifacts.apis.io/calmseo-com/rules/calmseo-com-rules.yml
  title: ''
  type: Spectral
  url: rules/calmseo-com-rules.yml
- group: design
  href: https://artifacts.apis.io/calmseo-com/json-ld/calmseo-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/calmseo-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/calmseo-com/vocabulary/calmseo-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/calmseo-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/calmseo-com/data-model/calmseo-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/calmseo-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/calmseo-com/conformance/calmseo-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/calmseo-com-conformance.yml
- group: other
  href: https://artifacts.apis.io/calmseo-com/hosts/calmseo-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/calmseo-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/calmseo-com/vendors/calmseo-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/calmseo-com-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://calmseo.com/login
- group: start
  title: ''
  type: GettingStarted
  url: https://calmseo.com/docs/claude
- group: auth
  href: https://artifacts.apis.io/calmseo-com/security/calmseo-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/calmseo-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://calmseo.com/
- group: docs
  title: ''
  type: Documentation
  url: https://calmseo.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://calmseo.com/api
- group: commercial
  title: ''
  type: Pricing
  url: https://calmseo.com/terms-and-conditions
- group: commercial
  title: ''
  type: TermsOfService
  url: https://calmseo.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://calmseo.com/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://calmseo.com/support
- group: company
  title: ''
  type: Blog
  url: https://calmseo.com/blog
coverage:
  checked: '2026-11-04'
  detail: The API reference page https://calmseo.com/api returns HTML but no OpenAPI or other machine‑readable contract.
  evidence:
  - status: 200
    url: https://calmseo.com/api
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-04'
description: CalmSEO is a hosted SEO MCP server for Claude, ChatGPT, and Cursor, providing Google Search Console data, live SERPs, keyword volumes, and page audits. It offers a free plan with starter credits and integrates with DataForSEO. The platform enables AI agents and developers to call SEO tools via a REST API or MCP, supporting multiple agents without coding.
image: https://calmseo.com/og-image.png
json_schemas:
- name: PostGscPageQueriesRequest
  property_count: 6
  slug: calmseo-com-post-gsc-page-queries-request
- name: PostGscSearchAnalyticsRequest
  property_count: 6
  slug: calmseo-com-post-gsc-search-analytics-request
- name: PostGscTopPagesRequest
  property_count: 5
  slug: calmseo-com-post-gsc-top-pages-request
- name: PostGscTopQueriesRequest
  property_count: 5
  slug: calmseo-com-post-gsc-top-queries-request
- name: PostKeywordsIdeasRequest
  property_count: 4
  slug: calmseo-com-post-keywords-ideas-request
- name: PostSerpSearchRequest
  property_count: 6
  slug: calmseo-com-post-serp-search-request
jsonld:
- class_count: 12
  name: Calmseo Com Context
  property_count: 21
  slug: calmseo-com-context
layout: provider
modified: '2026-11-04'
name: CalmSEO
nav: Providers
network: true
overview: 'CalmSEO is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include SEO, MCP, Artificial Intelligence, Search, and Tools.


  The CalmSEO catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  CalmSEO''s developer surface includes getting-started guide, documentation, API reference, pricing, support, engineering blog, and 12 more developer resources.'
random_paper: 0
rules:
- authorship: generated
  effective_rule_count: 88
  extends:
  - spectral:oas
  name: CalmSEO API Rules
  rule_count: 47
  severity_counts:
    error: 45
    hint: 0
    info: 1
    warn: 1
  slug: calmseo-com-rules
score:
  band: emerging
  composite: 23.6
  coverage:
    artifact_dirs: 16
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 22.4
    contract_governance: 22.0
    contract_quality: 26.0
    developer_ergonomics: 17.9
    discoverability: 66.1
    operational_transparency: 0.0
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
    score: 13.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Calmseo Com Domain Security
  slug: calmseo-com-domain-security
  summary_line: TLSv1.3
slug: calmseo-com
tags:
- SEO
- MCP
- Artificial Intelligence
- Search
- Tools
website: https://calmseo.com/
---
