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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 24.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Aibuildermarketplace Com Agentic Access
  operation_count: 4
  slug: aibuildermarketplace-com-agentic-access
  summary_line: 4 operations
api_count: 1
apis:
- baseURL: https://aibuildermarketplace.com/api/v1
  baseurl_source: declared
  description: The Categories.json API from AIBuilder Marketplace — 1 operation(s) for categories.json.
  name: AIBuilder Marketplace Categories.json API
  slug: aibuildermarketplace-com-categories-json-api
- baseURL: https://aibuildermarketplace.com/api/v1
  baseurl_source: declared
  description: The Index.json API from AIBuilder Marketplace — 1 operation(s) for index.json.
  name: AIBuilder Marketplace Index.json API
  slug: aibuildermarketplace-com-index-json-api
- baseURL: https://aibuildermarketplace.com/api/v1
  baseurl_source: declared
  description: The Offers.json API from AIBuilder Marketplace — 1 operation(s) for offers.json.
  name: AIBuilder Marketplace Offers.json API
  slug: aibuildermarketplace-com-offers-json-api
- baseURL: https://aibuildermarketplace.com/api/v1
  baseurl_source: declared
  description: The Products API from AIBuilder Marketplace — 1 operation(s) for products.
  name: AIBuilder Marketplace Products API
  slug: aibuildermarketplace-com-products-api
artifact_total: 16
common:
- group: agent
  href: https://artifacts.apis.io/aibuildermarketplace-com/agentic-access/aibuildermarketplace-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/aibuildermarketplace-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/aibuildermarketplace-com/rules/aibuildermarketplace-com-rules.yml
  title: ''
  type: Spectral
  url: rules/aibuildermarketplace-com-rules.yml
- group: design
  href: https://artifacts.apis.io/aibuildermarketplace-com/json-ld/aibuildermarketplace-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/aibuildermarketplace-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/aibuildermarketplace-com/vocabulary/aibuildermarketplace-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/aibuildermarketplace-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/aibuildermarketplace-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/aibuildermarketplace-com/data-model/aibuildermarketplace-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/aibuildermarketplace-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/aibuildermarketplace-com/errors/aibuildermarketplace-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/aibuildermarketplace-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/aibuildermarketplace-com/conformance/aibuildermarketplace-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/aibuildermarketplace-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/aibuildermarketplace-com/llms/aibuildermarketplace-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aibuildermarketplace-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/aibuildermarketplace-com/mcp/aibuildermarketplace-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/aibuildermarketplace-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/aibuildermarketplace-com/hosts/aibuildermarketplace-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aibuildermarketplace-com-hosts.yml
- group: operate
  title: ''
  type: Roadmap
  url: https://aibuildermarketplace.com/roadmap/
- group: company
  title: ''
  type: Newsroom
  url: https://aibuildermarketplace.com/research/press/
- group: docs
  title: ''
  type: Documentation
  url: https://aibuildermarketplace.com/guides/
- group: docs
  title: ''
  type: APIReference
  url: https://aibuildermarketplace.com/llms.txt
- group: auth
  href: https://artifacts.apis.io/aibuildermarketplace-com/security/aibuildermarketplace-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aibuildermarketplace-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aibuildermarketplace.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aibuildermarketplace.com/privacy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aibuildermarketplace.com/terms/
created: '2026-11-01'
description: AIBuilder Marketplace provides honest, hands‑on reviews of AI and business software tools. Each review includes the price at the time of reading, the date the price was captured, and guidance on who should or should not use the tool. The site compares pricing, usage limits, and suitability across a wide range of AI and business applications, offering transparent, up‑to‑date information for professionals seeking the right solution.
image: https://aibuildermarketplace.com/assets/og-default.png
json_schemas:
- name: Catalog
  property_count: 5
  slug: aibuildermarketplace-com-catalog
- name: Product
  property_count: 22
  slug: aibuildermarketplace-com-product
jsonld:
- class_count: 17
  name: Aibuildermarketplace Com Context
  property_count: 124
  slug: aibuildermarketplace-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at api.aibuildermarketplace.com.
  name: AIBuilder Marketplace MCP Server
  slug: aibuildermarketplace-com-mcp-yml
modified: '2026-11-01'
name: AIBuilder Marketplace
nav: Providers
network: true
overview: 'AIBuilder Marketplace publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Categories.json API, Index.json API, Offers.json API, and 1 more. Tagged areas include Artificial Intelligence, Business, Reviews, Marketplace, and Software.


  The AIBuilder Marketplace catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  AIBuilder Marketplace''s developer surface includes documentation, API reference, and 17 more developer resources.'
plans:
- name: Aibuildermarketplace Com Plans Pricing
  plan_count: 0
  slug: aibuildermarketplace-com-plans-pricing
random_paper: 22
rate_limits:
- limit_count: 0
  name: Aibuildermarketplace Com Rate Limits
  slug: aibuildermarketplace-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: AIBuilder Marketplace API Rules
  rule_count: 9
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 1
  slug: aibuildermarketplace-com-rules
scopes:
- name: Aibuildermarketplace Com Scopes
  scope_count: 0
  slug: aibuildermarketplace-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 29.7
  coverage:
    artifact_dirs: 31
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.8
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 55.7
    developer_ergonomics: 14.8
    discoverability: 65.8
    operational_transparency: 2.6
  previous_composite: 34.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Aibuildermarketplace Com Authentication
  slug: aibuildermarketplace-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Aibuildermarketplace Com Domain Security
  slug: aibuildermarketplace-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: aibuildermarketplace-com-catalog
  slug: aibuildermarketplace-com-catalog
slug: aibuildermarketplace-com
tags:
- Artificial Intelligence
- Business
- Reviews
- Marketplace
- Software
website: https://aibuildermarketplace.com/
---
