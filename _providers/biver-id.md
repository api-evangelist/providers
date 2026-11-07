---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
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
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 35.1
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://api.biver.id
  baseurl_source: declared
  description: 'Biver API as documented publicly: 93 operations. Contract generated from the documentation by API Evangelist (2026-11-02); not the provider''s own document.'
  name: Biver API
  slug: biver-id-api
artifact_total: 13
common:
- group: commercial
  href: https://artifacts.apis.io/biver-id/plans/biver-id-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/biver-id-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/biver-id/rules/biver-id-rules.yml
  title: ''
  type: Spectral
  url: rules/biver-id-rules.yml
- group: design
  href: https://artifacts.apis.io/biver-id/json-ld/biver-id-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/biver-id-context.jsonld
- group: design
  href: https://artifacts.apis.io/biver-id/vocabulary/biver-id-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/biver-id-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/biver-id/data-model/biver-id-data-model.yml
  title: ''
  type: DataModel
  url: data-model/biver-id-data-model.yml
- group: auth
  href: https://artifacts.apis.io/biver-id/authentication/biver-id-authentication.yml
  title: ''
  type: Authentication
  url: authentication/biver-id-authentication.yml
- group: design
  href: https://artifacts.apis.io/biver-id/conformance/biver-id-conformance.yml
  title: ''
  type: Conformance
  url: conformance/biver-id-conformance.yml
- group: agent
  href: https://artifacts.apis.io/biver-id/llms/biver-id-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/biver-id-llms.txt
- group: agent
  href: https://artifacts.apis.io/biver-id/mcp/biver-id-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/biver-id-mcp.yml
- group: agent
  href: https://artifacts.apis.io/biver-id/well-known/biver-id-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/biver-id-well-known.yml
- group: other
  href: https://artifacts.apis.io/biver-id/hosts/biver-id-hosts.yml
  title: ''
  type: Hosts
  url: hosts/biver-id-hosts.yml
- group: other
  href: https://artifacts.apis.io/biver-id/vendors/biver-id-vendors.yml
  title: ''
  type: Vendors
  url: vendors/biver-id-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://biver.id/login
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.biver.id</code
- group: auth
  href: https://artifacts.apis.io/biver-id/security/biver-id-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/biver-id-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://biver.id/
- group: docs
  title: ''
  type: Documentation
  url: https://biver.id/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://biver.id/docs/getting-started
- group: commercial
  title: ''
  type: Pricing
  url: https://biver.id/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://biver.id/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://biver.id/privacy
- group: operate
  title: ''
  type: Support
  url: https://biver.id/tentang
coverage:
  checked: '2026-11-02'
  detail: Documentation exists but no machine‑readable OpenAPI/AsyncAPI/GraphQL spec was found.
  evidence:
  - status: 200
    url: https://biver.id/docs/rest-api
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-02'
description: Biver is an AI‑powered landing‑page builder and online store platform designed for Indonesian micro, small and medium enterprises (UMKM). It enables merchants to create sales pages, product catalogs, and checkout flows with QRIS, virtual accounts and e‑wallets without any coding. Operated by PT Global Raya Oris Wijaya, Biver offers free domain or sub‑domain hosting, automatic shipping cost calculation, and integrates with DOKU payment gateway. The service launched in 2026, is built in Bali, and claims zero transaction commission, supporting over 485 Indonesian businesses with more than 981 published storefronts.
image: https://biver.id/og/default.png
json_schemas:
- name: GetV1PagesIdVersionsVersionidResponse
  property_count: 5
  slug: biver-id-get-v1-pages-id-versions-versionid-response
- name: PostV1AiPagesGenerateRequest
  property_count: 7
  slug: biver-id-post-v1-ai-pages-generate-request
- name: PostV1AiPagesRequest
  property_count: 7
  slug: biver-id-post-v1-ai-pages-request
- name: PostV1AiSectionsRequest
  property_count: 5
  slug: biver-id-post-v1-ai-sections-request
- name: PostV1SectionsImportHtmlResponse
  property_count: 8
  slug: biver-id-post-v1-sections-import-html-response
- name: PostV1TrackingEventsRequest
  property_count: 6
  slug: biver-id-post-v1-tracking-events-request
jsonld:
- class_count: 120
  name: Biver Id Context
  property_count: 116
  slug: biver-id-context
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.biver.id requiring OAuth.
  name: Biver MCP Server
  slug: biver-id-mcp-yml
modified: '2026-11-02'
name: Biver
nav: Providers
network: true
overview: 'Biver is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include E-Commerce, Artificial Intelligence, Landing Page Builder, Indonesia, and UMKM.


  The Biver catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Biver''s developer surface includes authentication, documentation, getting-started guide, pricing, support, and 17 more developer resources.'
plans:
- name: Biver Id Plans Pricing
  plan_count: 3
  slug: biver-id-plans-pricing
random_paper: 18
rules:
- authorship: generated
  effective_rule_count: 89
  extends:
  - spectral:oas
  name: Biver API Rules
  rule_count: 48
  severity_counts:
    error: 40
    hint: 0
    info: 1
    warn: 7
  slug: biver-id-rules
score:
  band: thin
  composite: 33.1
  coverage:
    artifact_dirs: 17
    catalog_earned: 74.8
    catalog_earned_first_party: 12.0
    catalog_gap: 40.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 26.3
    developer_ergonomics: 29.8
    discoverability: 65.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - indonesia
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - southeast-asia
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
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Biver Id Authentication
  slug: biver-id-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Biver Id Domain Security
  slug: biver-id-domain-security
  summary_line: TLSv1.3 · DMARC
slug: biver-id
tags:
- E-Commerce
- Artificial Intelligence
- Landing Page Builder
- Indonesia
- UMKM
website: https://biver.id/
---
