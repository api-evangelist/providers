---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Paid (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: true
  try_now: true
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
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 34.7
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'Aidoo API as documented publicly: 21 operations. Contract generated from the documentation by API Evangelist (2026-11-01); not the provider''s own document.'
  name: Aidoo API
  slug: aidoo-ai-api
artifact_total: 12
common:
- group: commercial
  href: https://artifacts.apis.io/aidoo-ai/plans/aidoo-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/aidoo-ai-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/aidoo-ai/rules/aidoo-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/aidoo-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/aidoo-ai/json-ld/aidoo-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/aidoo-ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/aidoo-ai/vocabulary/aidoo-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/aidoo-ai-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/aidoo-ai/data-model/aidoo-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/aidoo-ai-data-model.yml
- group: auth
  href: https://artifacts.apis.io/aidoo-ai/authentication/aidoo-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/aidoo-ai-authentication.yml
- group: design
  href: https://artifacts.apis.io/aidoo-ai/conformance/aidoo-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/aidoo-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/aidoo-ai/well-known/aidoo-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/aidoo-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/aidoo-ai/hosts/aidoo-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aidoo-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/aidoo-ai/vendors/aidoo-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/aidoo-ai-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aidoo.ai/fr/outils/explorateur-modeles-odoo/privacy-log
- group: auth
  href: https://artifacts.apis.io/aidoo-ai/security/aidoo-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aidoo-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aidoo.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://aidoo.ai/fr/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://aidoo.ai/fr/tarifs
- group: company
  title: ''
  type: Blog
  url: https://aidoo.ai/fr/blog
- group: operate
  title: ''
  type: Support
  url: https://aidoo.ai/fr/contact
coverage:
  checked: '2026-11-01'
  detail: No public API specification or developer portal is available beyond marketing documentation.
  evidence:
  - status: 200
    url: https://aidoo.ai/fr/docs
  reason: no-developer-program
  state: none
created: '2026-11-01'
description: Aidoo is a French AI agency that integrates artificial intelligence into Odoo ERP systems. Founded in 2021, it offers conversational agents, autonomous workflows, and AI‑enhanced modules for Odoo versions 17‑20. The platform connects Claude and ChatGPT to Odoo, enabling natural‑language queries, automated task execution, and custom module generation without coding. Aidoo provides a 14‑day free trial, transparent pricing, and tools for data reading, writing, reporting, and OCR, targeting SMEs and TPEs in France.
image: https://aidoo.ai/og/aidoo-og-fr.png
json_schemas:
- name: PostJson2AccountMoveLineSearchReadRequest
  property_count: 3
  slug: aidoo-ai-post-json2-account-move-line-search-read-request
- name: PostJson2AccountMoveSearchReadRequest
  property_count: 3
  slug: aidoo-ai-post-json2-account-move-search-read-request
- name: PostJson2AccountPaymentSearchReadRequest
  property_count: 3
  slug: aidoo-ai-post-json2-account-payment-search-read-request
- name: PostJson2CrmLeadSearchReadRequest
  property_count: 3
  slug: aidoo-ai-post-json2-crm-lead-search-read-request
- name: PostJson2HrEmployeeSearchReadRequest
  property_count: 3
  slug: aidoo-ai-post-json2-hr-employee-search-read-request
- name: PostJson2ResPartnerFieldsGetResponse
  property_count: 1
  slug: aidoo-ai-post-json2-res-partner-fields-get-response
jsonld:
- class_count: 20
  name: Aidoo Ai Context
  property_count: 4
  slug: aidoo-ai-context
layout: provider
modified: '2026-11-01'
name: Aidoo
nav: Providers
network: true
overview: 'Aidoo is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, ERP, Odoo, Automation, and French.


  The Aidoo catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Aidoo''s developer surface includes authentication, documentation, pricing, engineering blog, support, and 12 more developer resources.'
plans:
- name: Aidoo Ai Plans Pricing
  plan_count: 5
  slug: aidoo-ai-plans-pricing
random_paper: 3
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: Aidoo API Rules
  rule_count: 11
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 0
  slug: aidoo-ai-rules
score:
  band: thin
  composite: 26.5
  coverage:
    artifact_dirs: 17
    catalog_earned: 66.0
    catalog_earned_first_party: 12.0
    catalog_gap: 49.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.1
  facets:
    access_clarity: 42.1
    contract_governance: 19.7
    contract_quality: 22.6
    developer_ergonomics: 20.2
    discoverability: 57.1
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - france
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 30.6
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 17.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Aidoo Ai Authentication
  slug: aidoo-ai-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Aidoo Ai Domain Security
  slug: aidoo-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: aidoo-ai
tags:
- Artificial Intelligence
- ERP
- Odoo
- Automation
- French
website: https://aidoo.ai/
---
