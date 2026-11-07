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
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 33.7
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'Decree API as documented publicly: 2 operations. Contract generated from the documentation by API Evangelist (2026-11-05); not the provider''s own document.'
  name: Decree API
  slug: decree-om-api
artifact_total: 6
common:
- group: design
  href: https://artifacts.apis.io/decree-om/rules/decree-om-rules.yml
  title: ''
  type: Spectral
  url: rules/decree-om-rules.yml
- group: design
  href: https://artifacts.apis.io/decree-om/json-ld/decree-om-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/decree-om-context.jsonld
- group: design
  href: https://artifacts.apis.io/decree-om/vocabulary/decree-om-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/decree-om-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/decree-om/data-model/decree-om-data-model.yml
  title: ''
  type: DataModel
  url: data-model/decree-om-data-model.yml
- group: design
  href: https://artifacts.apis.io/decree-om/conformance/decree-om-conformance.yml
  title: ''
  type: Conformance
  url: conformance/decree-om-conformance.yml
- group: agent
  href: https://artifacts.apis.io/decree-om/well-known/decree-om-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/decree-om-well-known.yml
- group: other
  href: https://artifacts.apis.io/decree-om/hosts/decree-om-hosts.yml
  title: ''
  type: Hosts
  url: hosts/decree-om-hosts.yml
- group: other
  href: https://artifacts.apis.io/decree-om/vendors/decree-om-vendors.yml
  title: ''
  type: Vendors
  url: vendors/decree-om-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://decree.om/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://decree.om/privacy-policy/
- group: commercial
  title: ''
  type: Pricing
  url: https://decree.om/pricing/
- group: start
  title: ''
  type: Login
  url: https://decree.om/login/
- group: company
  title: ''
  type: Blog
  url: https://blog.decree.om/
- group: auth
  href: https://artifacts.apis.io/decree-om/security/decree-om-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/decree-om-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://decree.om/
coverage:
  checked: '2026-11-05'
  detail: The provider's website offers no developer documentation or API reference pages.
  evidence:
  - status: 200
    url: https://decree.om/
  reason: no-developer-program
  state: none
created: '2026-11-05'
description: 'decree-om is a company surfaced via the API Evangelist harvest backlog (source: mcp-registry) and added to the network as a stub for full-pipeline profiling.'
json_schemas:
- name: GetAnnouncementsByCrResponse
  property_count: 6
  slug: decree-om-get-announcements-by-cr-response
- name: GetAnnouncementsRecentResponse
  property_count: 6
  slug: decree-om-get-announcements-recent-response
jsonld:
- class_count: 2
  name: Decree Om Context
  property_count: 7
  slug: decree-om-context
layout: provider
modified: '2026-11-05'
name: Decree
nav: Providers
network: true
overview: 'Decree is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Legislation, Omani Law, Search Engines, and Artificial Intelligence.


  The Decree catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Decree''s developer surface includes pricing, engineering blog, and 13 more developer resources.'
random_paper: 17
rules:
- authorship: generated
  effective_rule_count: 79
  extends:
  - spectral:oas
  name: Decree API Rules
  rule_count: 38
  severity_counts:
    error: 36
    hint: 0
    info: 1
    warn: 1
  slug: decree-om-rules
score:
  band: emerging
  composite: 21.7
  coverage:
    artifact_dirs: 15
    catalog_earned: 39.8
    catalog_earned_first_party: 0.0
    catalog_gap: 75.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 44.7
    contract_governance: 22.0
    contract_quality: 19.9
    developer_ergonomics: 2.4
    discoverability: 35.7
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
    score: 22.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Decree Om Domain Security
  slug: decree-om-domain-security
  summary_line: TLSv1.2 · DMARC
slug: decree-om
tags:
- Legislation
- Omani Law
- Search Engines
- Artificial Intelligence
website: https://decree.om/
---
