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
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 25.6
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://api.tme.eu
  baseurl_source: declared
  description: 'TME API as documented publicly: 2 operations. Contract generated from the documentation by API Evangelist (2026-10-27); not the provider''s own document.'
  name: TME API
  slug: tme-api
artifact_total: 6
common:
- group: design
  href: https://artifacts.apis.io/tme/rules/tme-rules.yml
  title: ''
  type: Spectral
  url: rules/tme-rules.yml
- group: design
  href: https://artifacts.apis.io/tme/json-ld/tme-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/tme-context.jsonld
- group: design
  href: https://artifacts.apis.io/tme/vocabulary/tme-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/tme-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/tme/data-model/tme-data-model.yml
  title: ''
  type: DataModel
  url: data-model/tme-data-model.yml
- group: design
  href: https://artifacts.apis.io/tme/conformance/tme-conformance.yml
  title: ''
  type: Conformance
  url: conformance/tme-conformance.yml
- group: agent
  href: https://artifacts.apis.io/tme/llms/tme-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/tme-llms.txt
- group: other
  href: https://artifacts.apis.io/tme/hosts/tme-hosts.yml
  title: ''
  type: Hosts
  url: hosts/tme-hosts.yml
- group: other
  href: https://artifacts.apis.io/tme/vendors/tme-vendors.yml
  title: ''
  type: Vendors
  url: vendors/tme-vendors.yml
- group: docs
  title: ''
  type: Documentation
  url: https://developers.tme.eu/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.tme.eu\
- group: docs
  title: ''
  type: APIReference
  url: https://developers.tme.eu/en
- group: auth
  href: https://artifacts.apis.io/tme/security/tme-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/tme-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.tme.eu/
created: '2026-10-27'
description: 'TME is a company surfaced via the API Evangelist harvest backlog (source: new-submission) and added to the network as a stub for full-pipeline profiling.'
json_schemas:
- name: GetAuthTokenResponse
  property_count: 2
  slug: tme-get-auth-token-response
- name: GetProductsResponse
  property_count: 39
  slug: tme-get-products-response
jsonld:
- class_count: 2
  name: Tme Context
  property_count: 5
  slug: tme-context
layout: provider
modified: '2026-10-27'
name: TME
nav: Providers
network: true
overview: 'TME is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company.


  The TME catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  TME''s developer surface includes documentation, API reference, and 11 more developer resources.'
random_paper: 14
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: TME API Rules
  rule_count: 13
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 1
  slug: tme-rules
score:
  band: emerging
  composite: 15.2
  coverage:
    artifact_dirs: 15
    catalog_earned: 44.8
    catalog_earned_first_party: 0.0
    catalog_gap: 70.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.7
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 21.8
    developer_ergonomics: 13.1
    discoverability: 51.8
    operational_transparency: 0.0
  previous_composite: 17.9
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
    score: 10.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/tme/tme-2026-11-03T144827.png
security:
- kind: domain-security
  name: Tme Domain Security
  slug: tme-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: tme
tags:
- Company
website: https://www.tme.eu/
---
