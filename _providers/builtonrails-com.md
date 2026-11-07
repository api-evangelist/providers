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
  score: 22.3
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: API documentation for BuiltOnRails, providing access to stack intelligence via MCP server.
  name: BuiltOnRails API
  slug: builtonrails-api
- description: 'BuiltOnRails API as documented publicly: 13 operations. Contract generated from the documentation by API Evangelist (2026-11-03); not the provider''s own document.'
  name: BuiltOnRails API
  slug: builtonrails-com-api
artifact_total: 12
common:
- group: design
  href: https://artifacts.apis.io/builtonrails-com/rules/builtonrails-com-rules.yml
  title: ''
  type: Spectral
  url: rules/builtonrails-com-rules.yml
- group: design
  href: https://artifacts.apis.io/builtonrails-com/json-ld/builtonrails-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/builtonrails-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/builtonrails-com/vocabulary/builtonrails-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/builtonrails-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/builtonrails-com/data-model/builtonrails-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/builtonrails-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/builtonrails-com/conformance/builtonrails-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/builtonrails-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/builtonrails-com/llms/builtonrails-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/builtonrails-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/builtonrails-com/mcp/builtonrails-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/builtonrails-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/builtonrails-com/hosts/builtonrails-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/builtonrails-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/builtonrails-com/vendors/builtonrails-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/builtonrails-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://builtonrails.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://builtonrails.com/privacy
- group: company
  title: ''
  type: Blog
  url: https://builtonrails.com/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://builtonrails.com/daily/getting-started-with-ruby-2840
- group: auth
  href: https://artifacts.apis.io/builtonrails-com/security/builtonrails-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/builtonrails-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://builtonrails.com/
coverage:
  checked: '2026-11-03'
  detail: API documentation is served as markdown but no machine‑readable OpenAPI spec is available.
  evidence:
  - status: 200
    url: https://builtonrails.com/api-docs.md
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-03'
description: 'builtonrails-com is a company surfaced via the API Evangelist harvest backlog (source: mcp-registry) and added to the network as a stub for full-pipeline profiling.'
image: https://builtonrails.com/og/default.png
json_schemas:
- name: GetApiV1StacksResponse
  property_count: 2
  slug: builtonrails-com-get-api-v1-stacks-response
- name: PostApiV1ProductStacksRequest
  property_count: 2
  slug: builtonrails-com-post-api-v1-product-stacks-request
- name: PostApiV1ProductsResponse
  property_count: 2
  slug: builtonrails-com-post-api-v1-products-response
- name: PostApiV1ProductsSlugUpdatesRequest
  property_count: 5
  slug: builtonrails-com-post-api-v1-products-slug-updates-request
- name: PostApiV1ProductsSlugUpdatesResponse
  property_count: 2
  slug: builtonrails-com-post-api-v1-products-slug-updates-response
- name: PostApiV1StacksDetectResponse
  property_count: 1
  slug: builtonrails-com-post-api-v1-stacks-detect-response
jsonld:
- class_count: 14
  name: Builtonrails Com Context
  property_count: 14
  slug: builtonrails-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at builtonrails.com.
  name: BuiltOnRails MCP Server
  slug: builtonrails-com-mcp-yml
modified: '2026-11-03'
name: BuiltOnRails
nav: Providers
network: true
overview: 'BuiltOnRails is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Ruby on Rails and Stack Data.


  The BuiltOnRails catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  BuiltOnRails'' developer surface includes engineering blog, getting-started guide, and 13 more developer resources.'
random_paper: 12
rules:
- authorship: generated
  effective_rule_count: 84
  extends:
  - spectral:oas
  name: BuiltOnRails API Rules
  rule_count: 43
  severity_counts:
    error: 41
    hint: 0
    info: 1
    warn: 1
  slug: builtonrails-com-rules
score:
  band: emerging
  composite: 16.3
  coverage:
    artifact_dirs: 15
    catalog_earned: 47.8
    catalog_earned_first_party: 0.0
    catalog_gap: 67.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 24.8
    developer_ergonomics: 7.1
    discoverability: 40.0
    operational_transparency: 0.0
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Builtonrails Com Domain Security
  slug: builtonrails-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: builtonrails-com
tags:
- Ruby on Rails
- Stack Data
website: https://builtonrails.com/
---
