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
    mcp_server: documented
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
  score: 20.3
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'CutConvert API as documented publicly: 2 operations. Contract generated from the documentation by API Evangelist (2026-11-04); not the provider''s own document.'
  name: CutConvert API
  slug: cutconvert-com-api
artifact_total: 7
common:
- group: commercial
  href: https://artifacts.apis.io/cutconvert-com/plans/cutconvert-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/cutconvert-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/cutconvert-com/rules/cutconvert-com-rules.yml
  title: ''
  type: Spectral
  url: rules/cutconvert-com-rules.yml
- group: design
  href: https://artifacts.apis.io/cutconvert-com/json-ld/cutconvert-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/cutconvert-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/cutconvert-com/vocabulary/cutconvert-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/cutconvert-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/cutconvert-com/data-model/cutconvert-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/cutconvert-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/cutconvert-com/conformance/cutconvert-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cutconvert-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/cutconvert-com/llms/cutconvert-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cutconvert-com-llms.txt
- group: other
  href: https://artifacts.apis.io/cutconvert-com/hosts/cutconvert-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cutconvert-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/cutconvert-com/vendors/cutconvert-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cutconvert-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cutconvert.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cutconvert.com/privacy
- group: start
  title: ''
  type: DeveloperPortal
  url: https://cutconvert.com/developers
- group: docs
  title: ''
  type: Documentation
  url: https://apidocs.cutconvert.com/
- group: auth
  href: https://artifacts.apis.io/cutconvert-com/security/cutconvert-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cutconvert-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cutconvert.com/
created: '2026-11-04'
description: CutConvert provides free file conversion tools for video editors and post‑production workflows. It enables moving timelines between CapCut, Premiere, Resolve, Final Cut and Avid, and converts subtitles and transcripts (SRT, VTT, SCC) directly in the browser without uploading files. The service is offered at no cost and targets creators needing quick format swaps.
image: https://cutconvert.com/opengraph-image?e71c76949c6563df
json_schemas:
- name: PostApiEditExportRequest
  property_count: 3
  slug: cutconvert-com-post-api-edit-export-request
- name: PostApiEditExportResponse
  property_count: 9
  slug: cutconvert-com-post-api-edit-export-response
jsonld:
- class_count: 2
  name: Cutconvert Com Context
  property_count: 3
  slug: cutconvert-com-context
layout: provider
modified: '2026-11-04'
name: CutConvert
nav: Providers
network: true
overview: 'CutConvert is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Video Editing, File Conversion, Post-Production, Captions, and Subtitle Translation.


  The CutConvert catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  CutConvert''s developer surface includes documentation and 14 more developer resources.'
plans:
- name: Cutconvert Com Plans Pricing
  plan_count: 6
  slug: cutconvert-com-plans-pricing
random_paper: 1
rules:
- authorship: generated
  effective_rule_count: 74
  extends:
  - spectral:oas
  name: CutConvert API Rules
  rule_count: 33
  severity_counts:
    error: 31
    hint: 0
    info: 1
    warn: 1
  slug: cutconvert-com-rules
score:
  band: thin
  composite: 28.9
  coverage:
    artifact_dirs: 17
    catalog_earned: 63.8
    catalog_earned_first_party: 12.0
    catalog_gap: 51.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 52.6
    contract_governance: 22.0
    contract_quality: 20.1
    developer_ergonomics: 19.0
    discoverability: 64.3
    operational_transparency: 0.0
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
    score: 18.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cutconvert Com Domain Security
  slug: cutconvert-com-domain-security
  summary_line: TLSv1.3
slug: cutconvert-com
tags:
- Video Editing
- File Conversion
- Post-Production
- Captions
- Subtitle Translation
website: https://cutconvert.com/
---
