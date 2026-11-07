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
- description: 'BrewMyPDF API as documented publicly: 28 operations. Contract generated from the documentation by API Evangelist (2026-11-03); not the provider''s own document.'
  name: BrewMyPDF API
  slug: brewmypdf-com-api
artifact_total: 11
common:
- group: commercial
  title: ''
  type: TermsOfService
  url: https://brewmypdf.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://brewmypdf.com/legal/privacy
- group: commercial
  href: https://artifacts.apis.io/brewmypdf-com/plans/brewmypdf-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/brewmypdf-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/brewmypdf-com/rules/brewmypdf-com-rules.yml
  title: ''
  type: Spectral
  url: rules/brewmypdf-com-rules.yml
- group: design
  href: https://artifacts.apis.io/brewmypdf-com/json-ld/brewmypdf-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/brewmypdf-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/brewmypdf-com/vocabulary/brewmypdf-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/brewmypdf-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/brewmypdf-com/data-model/brewmypdf-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/brewmypdf-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/brewmypdf-com/conformance/brewmypdf-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/brewmypdf-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/brewmypdf-com/llms/brewmypdf-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/brewmypdf-com-llms.txt
- group: other
  href: https://artifacts.apis.io/brewmypdf-com/hosts/brewmypdf-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/brewmypdf-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/brewmypdf-com/vendors/brewmypdf-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/brewmypdf-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/brewmypdf-com/security/brewmypdf-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/brewmypdf-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://brewmypdf.com/
- group: docs
  title: ''
  type: Documentation
  url: https://brewmypdf.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://brewmypdf.com/docs/api
- group: commercial
  title: ''
  type: Pricing
  url: https://brewmypdf.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://brewmypdf.com/app/signup
- group: start
  title: ''
  type: Login
  url: https://brewmypdf.com/app/login
- group: operate
  title: ''
  type: Support
  url: https://brewmypdf.com/faq
- group: company
  title: ''
  type: Blog
  url: https://brewmypdf.com/gallery
- group: other
  title: ''
  type: Image
  url: https://brewmypdf.com/favicon.svg
coverage:
  checked: '2026-11-03'
  detail: Documentation pages are JavaScript‑rendered single‑page apps with no machine‑readable spec.
  evidence:
  - status: 200
    url: https://brewmypdf.com/docs/api
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-03'
description: BrewMyPDF provides a visual template editor and a REST API to generate pixel‑perfect PDFs from JSON in under a second. Users can design templates with images, tables, charts, barcodes and fillable form fields, then call the API to render documents. The service offers a free tier (50 documents/month) and paid plans, supports batch processing, webhooks, and MCP for AI agents. It aims to simplify PDF generation without writing code.
json_schemas:
- name: PostMcpRequest
  property_count: 4
  slug: brewmypdf-com-post-mcp-request
- name: PostMcpResponse
  property_count: 4
  slug: brewmypdf-com-post-mcp-response
- name: PostV1EmbedSessionsRequest
  property_count: 3
  slug: brewmypdf-com-post-v1-embed-sessions-request
- name: PostV1IntakeRunsRequest
  property_count: 6
  slug: brewmypdf-com-post-v1-intake-runs-request
- name: PostV1PdfFieldsResponse
  property_count: 5
  slug: brewmypdf-com-post-v1-pdf-fields-response
- name: PostV1PdfStampRequest
  property_count: 9
  slug: brewmypdf-com-post-v1-pdf-stamp-request
jsonld:
- class_count: 31
  name: Brewmypdf Com Context
  property_count: 56
  slug: brewmypdf-com-context
layout: provider
modified: '2026-11-03'
name: BrewMyPDF
nav: Providers
network: true
overview: 'BrewMyPDF is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include PDF Generation, Visual Editor, Templates, MCP, and Embeddings.


  The BrewMyPDF catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  BrewMyPDF''s developer surface includes documentation, API reference, pricing, signup flow, support, engineering blog, and 15 more developer resources.'
plans:
- name: Brewmypdf Com Plans Pricing
  plan_count: 6
  slug: brewmypdf-com-plans-pricing
random_paper: 20
rules:
- authorship: generated
  effective_rule_count: 85
  extends:
  - spectral:oas
  name: BrewMyPDF API Rules
  rule_count: 44
  severity_counts:
    error: 38
    hint: 0
    info: 1
    warn: 5
  slug: brewmypdf-com-rules
score:
  band: thin
  composite: 27.1
  coverage:
    artifact_dirs: 18
    catalog_earned: 67.8
    catalog_earned_first_party: 12.0
    catalog_gap: 47.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 24.7
    developer_ergonomics: 11.9
    discoverability: 53.6
    operational_transparency: 0.0
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
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
  name: Brewmypdf Com Domain Security
  slug: brewmypdf-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: brewmypdf-com
tags:
- PDF Generation
- Visual Editor
- Templates
- MCP
- Embeddings
website: https://brewmypdf.com/
---
