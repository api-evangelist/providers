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
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 16.1
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Model Context Protocol API for BIM.HOUSE services
  name: MCP
  slug: mcp
- description: 'BIM.HOUSE API as documented publicly: 32 operations. Contract generated from the documentation by API Evangelist (2026-11-02); not the provider''s own document.'
  name: BIM.HOUSE API
  slug: bim-house-api
artifact_total: 13
common:
- group: commercial
  href: https://artifacts.apis.io/bim-house/plans/bim-house-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/bim-house-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/bim-house/rules/bim-house-rules.yml
  title: ''
  type: Spectral
  url: rules/bim-house-rules.yml
- group: design
  href: https://artifacts.apis.io/bim-house/json-ld/bim-house-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/bim-house-context.jsonld
- group: design
  href: https://artifacts.apis.io/bim-house/vocabulary/bim-house-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/bim-house-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/bim-house/data-model/bim-house-data-model.yml
  title: ''
  type: DataModel
  url: data-model/bim-house-data-model.yml
- group: design
  href: https://artifacts.apis.io/bim-house/conformance/bim-house-conformance.yml
  title: ''
  type: Conformance
  url: conformance/bim-house-conformance.yml
- group: agent
  href: https://artifacts.apis.io/bim-house/llms/bim-house-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bim-house-llms.txt
- group: agent
  href: https://artifacts.apis.io/bim-house/mcp/bim-house-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/bim-house-mcp.yml
- group: other
  href: https://artifacts.apis.io/bim-house/hosts/bim-house-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bim-house-hosts.yml
- group: other
  href: https://artifacts.apis.io/bim-house/vendors/bim-house-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bim-house-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://bim.house/trust/:slug
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bim.house/terms
- group: start
  title: ''
  type: Sandbox
  url: https://bim.house/console
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bim.house/privacy
- group: company
  title: ''
  type: Newsroom
  url: https://bim.house/press
- group: start
  title: ''
  type: Login
  url: https://bim.house/login
- group: auth
  href: https://artifacts.apis.io/bim-house/security/bim-house-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bim-house-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bim.house/
- group: docs
  title: ''
  type: APIReference
  url: https://bim.house/docs/api
- group: start
  title: ''
  type: GettingStarted
  url: https://bim.house/docs/mcp
- group: commercial
  title: ''
  type: Pricing
  url: https://bim.house/pricing
created: '2026-11-02'
description: BIM.HOUSE は AI が IFC 4.3 / Revit / DXF などの建築データを自動生成し、建築士事務所や施工業者向けに API と Webhook を提供するサービスです。土地寸法から 60 分で 3D モデルや構造計算 PDF を出力し、確認申請にも対応可能です。無料プランから有料プランまで複数用意され、国内外の建築ソフトウェアと連携します。
image: https://bim.house/static/img/mine/night.jpg
json_schemas:
- name: GetApiMaterialCatalogResponse
  property_count: 5
  slug: bim-house-get-api-material-catalog-response
- name: GetApiMaterialQuoteSlugResponse
  property_count: 2
  slug: bim-house-get-api-material-quote-slug-response
- name: GetApiMaterialRfqSlugorquoteSupplierResponse
  property_count: 2
  slug: bim-house-get-api-material-rfq-slugorquote-supplier-response
- name: GetApiProjectsSlugDiffFromToResponse
  property_count: 3
  slug: bim-house-get-api-projects-slug-diff-from-to-response
- name: PostApiImagePhotorealFromViewerRequest
  property_count: 2
  slug: bim-house-post-api-image-photoreal-from-viewer-request
- name: PostApiMaterialCatalogRequest
  property_count: 5
  slug: bim-house-post-api-material-catalog-request
jsonld:
- class_count: 16
  name: Bim House Context
  property_count: 26
  slug: bim-house-context
layout: provider
mcp_servers:
- description: Remote MCP server at bim.house.
  name: BIM.HOUSE MCP Server
  slug: bim-house-mcp-yml
modified: '2026-11-02'
name: BIM.HOUSE
nav: Providers
network: true
overview: 'BIM.HOUSE is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include BIM, Architecture, Construction, and Artificial Intelligence.


  The BIM.HOUSE catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  BIM.HOUSE''s developer surface includes sandbox, API reference, getting-started guide, pricing, and 17 more developer resources.'
plans:
- name: Bim House Plans Pricing
  plan_count: 2
  slug: bim-house-plans-pricing
random_paper: 17
rules:
- authorship: generated
  effective_rule_count: 78
  extends:
  - spectral:oas
  name: BIM.HOUSE API Rules
  rule_count: 37
  severity_counts:
    error: 32
    hint: 0
    info: 1
    warn: 4
  slug: bim-house-rules
score:
  band: emerging
  composite: 24.8
  coverage:
    artifact_dirs: 16
    catalog_earned: 55.8
    catalog_earned_first_party: 8.0
    catalog_gap: 59.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 47.4
    contract_governance: 22.0
    contract_quality: 23.5
    developer_ergonomics: 13.1
    discoverability: 40.8
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
    score: 15.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bim House Domain Security
  slug: bim-house-domain-security
  summary_line: TLSv1.3 · HSTS
slug: bim-house
tags:
- BIM
- Architecture
- Construction
- Artificial Intelligence
website: https://bim.house/
---
