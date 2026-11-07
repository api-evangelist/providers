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
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 22.5
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: API documentation for Eagle Doc OCR technology, providing endpoints for document processing, receipt and invoice extraction.
  name: Eagle Doc API
  slug: eagle-doc-api-2
- baseURL: https://de.eagle-doc.com
  baseurl_source: declared
  description: 'Eagle Doc API as documented publicly: 23 operations. Contract generated from the documentation by API Evangelist (2026-10-27); not the provider''s own document.'
  name: Eagle Doc API
  slug: eagle-doc-api
artifact_total: 13
common:
- group: commercial
  href: https://artifacts.apis.io/eagle-doc/plans/eagle-doc-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/eagle-doc-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/eagle-doc/rules/eagle-doc-rules.yml
  title: ''
  type: Spectral
  url: rules/eagle-doc-rules.yml
- group: design
  href: https://artifacts.apis.io/eagle-doc/json-ld/eagle-doc-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/eagle-doc-context.jsonld
- group: design
  href: https://artifacts.apis.io/eagle-doc/vocabulary/eagle-doc-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/eagle-doc-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/eagle-doc/data-model/eagle-doc-data-model.yml
  title: ''
  type: DataModel
  url: data-model/eagle-doc-data-model.yml
- group: auth
  href: https://artifacts.apis.io/eagle-doc/authentication/eagle-doc-authentication.yml
  title: ''
  type: Authentication
  url: authentication/eagle-doc-authentication.yml
- group: design
  href: https://artifacts.apis.io/eagle-doc/conformance/eagle-doc-conformance.yml
  title: ''
  type: Conformance
  url: conformance/eagle-doc-conformance.yml
- group: other
  href: https://artifacts.apis.io/eagle-doc/hosts/eagle-doc-hosts.yml
  title: ''
  type: Hosts
  url: hosts/eagle-doc-hosts.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.eagle-doc.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/S2Tec
- group: auth
  href: https://artifacts.apis.io/eagle-doc/security/eagle-doc-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/eagle-doc-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://eagle-doc.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.eagle-doc.com/en/documentation/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.eagle-doc.com/en/pricing/
- group: operate
  title: ''
  type: Support
  url: https://www.eagle-doc.com/en/contact/
coverage:
  checked: '2026-10-27'
  detail: Documentation pages are HTML only and no OpenAPI or other machine‑readable contract was found.
  evidence:
  - status: 200
    url: https://www.eagle-doc.com/en/documentation/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-27'
description: Eagle Doc provides AI-powered Document OCR and bookkeeping automation APIs. Their platform extracts structured data from invoices, receipts, bank statements and other documents, offering high‑accuracy extraction (95%+), a developer dashboard, and integration with DATEV for tax firms. Services include Document AI, OCR APIs, and a bookkeeping solution for businesses and freelancers.
image: https://www.eagle-doc.com/assets/images/og/og-default.png
json_schemas:
- name: GetApiBusinessBusinessidSubBusinessesResponse
  property_count: 9
  slug: eagle-doc-get-api-business-businessid-sub-businesses-response
- name: GetApiBusinessBusinessidUsageCurrentResponse
  property_count: 8
  slug: eagle-doc-get-api-business-businessid-usage-current-response
- name: GetApiUsageV1LogsResponse
  property_count: 8
  slug: eagle-doc-get-api-usage-v1-logs-response
- name: GetApiUsageV1MonthlyResponse
  property_count: 8
  slug: eagle-doc-get-api-usage-v1-monthly-response
- name: PatchApiBusinessBusinessidSubBusinessesSubbusinessidResponse
  property_count: 9
  slug: eagle-doc-patch-api-business-businessid-sub-businesses-subbusinessid-response
- name: PostApiBusinessBusinessidSubBusinessesResponse
  property_count: 9
  slug: eagle-doc-post-api-business-businessid-sub-businesses-response
jsonld:
- class_count: 11
  name: Eagle Doc Context
  property_count: 23
  slug: eagle-doc-context
layout: provider
modified: '2026-10-27'
name: Eagle Doc
nav: Providers
network: true
overview: 'Eagle Doc is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, OCR, Bookkeeping, and Document Processing.


  The Eagle Doc catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Eagle Doc''s developer surface includes authentication, documentation, pricing, support, and 11 more developer resources.'
plans:
- name: Eagle Doc Plans Pricing
  plan_count: 4
  slug: eagle-doc-plans-pricing
random_paper: 1
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: Eagle Doc API Rules
  rule_count: 12
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 0
  slug: eagle-doc-rules
score:
  band: thin
  composite: 28.1
  coverage:
    artifact_dirs: 19
    catalog_earned: 69.0
    catalog_earned_first_party: 12.0
    catalog_gap: 46.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.8
  facets:
    access_clarity: 36.8
    contract_governance: 33.3
    contract_quality: 26.1
    developer_ergonomics: 19.0
    discoverability: 57.1
    operational_transparency: 10.5
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 31.9
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/eagle-doc/eagle-doc-2026-11-03T131200.png
security:
- kind: authentication
  name: Eagle Doc Authentication
  slug: eagle-doc-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Eagle Doc Domain Security
  slug: eagle-doc-domain-security
  summary_line: TLSv1.3 · DMARC
slug: eagle-doc
tags:
- Company
- Artificial Intelligence
- OCR
- Bookkeeping
- Document Processing
website: https://eagle-doc.com/
---
