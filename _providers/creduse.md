---
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
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 28.0
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: 'API for Creduse, providing credit management operations. Base URL: https://api.creduse.com'
  name: Creduse API
  slug: creduse-api-2
- baseURL: https://api.creduse.com
  baseurl_source: declared
  description: 'Creduse API as documented publicly: 8 operations. Contract generated from the documentation by API Evangelist (2026-10-20); not the provider''s own document.'
  name: Creduse API
  slug: creduse-api
artifact_total: 12
common:
- group: design
  href: https://artifacts.apis.io/creduse/rules/creduse-rules.yml
  title: ''
  type: Spectral
  url: rules/creduse-rules.yml
- group: design
  href: https://artifacts.apis.io/creduse/json-ld/creduse-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/creduse-context.jsonld
- group: design
  href: https://artifacts.apis.io/creduse/vocabulary/creduse-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/creduse-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/creduse/data-model/creduse-data-model.yml
  title: ''
  type: DataModel
  url: data-model/creduse-data-model.yml
- group: auth
  href: https://artifacts.apis.io/creduse/authentication/creduse-authentication.yml
  title: ''
  type: Authentication
  url: authentication/creduse-authentication.yml
- group: design
  href: https://artifacts.apis.io/creduse/conformance/creduse-conformance.yml
  title: ''
  type: Conformance
  url: conformance/creduse-conformance.yml
- group: other
  href: https://artifacts.apis.io/creduse/hosts/creduse-hosts.yml
  title: ''
  type: Hosts
  url: hosts/creduse-hosts.yml
- group: other
  href: https://artifacts.apis.io/creduse/vendors/creduse-vendors.yml
  title: ''
  type: Vendors
  url: vendors/creduse-vendors.yml
- group: build
  href: https://artifacts.apis.io/creduse/packages/creduse-packages.yml
  title: ''
  type: SDKs
  url: packages/creduse-packages.yml
- group: build
  href: https://artifacts.apis.io/creduse/packages/creduse-packages.yml
  title: ''
  type: Packages
  url: packages/creduse-packages.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://doc.creduse.com/api-reference/getting-started.html
- group: docs
  title: ''
  type: Documentation
  url: https://doc.creduse.com/
- group: auth
  href: https://artifacts.apis.io/creduse/security/creduse-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/creduse-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://creduse.com/
created: '2026-10-19'
description: 'Creduse is a company surfaced via the API Evangelist harvest backlog (source: g2-catalog) and added to the network as a stub for full-pipeline profiling.'
json_schemas:
- name: PostAddRequest
  property_count: 3
  slug: creduse-post-add-request
- name: PostAddResponse
  property_count: 2
  slug: creduse-post-add-response
- name: PostStartCycleRequest
  property_count: 3
  slug: creduse-post-start-cycle-request
- name: PostStartCycleResponse
  property_count: 7
  slug: creduse-post-start-cycle-response
- name: PostStopCycleResponse
  property_count: 7
  slug: creduse-post-stop-cycle-response
- name: PostSubtractRequest
  property_count: 2
  slug: creduse-post-subtract-request
jsonld:
- class_count: 10
  name: Creduse Context
  property_count: 8
  slug: creduse-context
layout: provider
modified: '2026-10-19'
name: Creduse
nav: Providers
network: true
overview: 'Creduse is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company.


  The Creduse catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Creduse''s developer surface includes authentication, getting-started guide, documentation, and 11 more developer resources.'
random_paper: 3
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: Creduse API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: creduse-rules
score:
  band: emerging
  composite: 21.5
  coverage:
    artifact_dirs: 16
    catalog_earned: 47.8
    catalog_earned_first_party: 0.0
    catalog_gap: 67.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 24.3
    developer_ergonomics: 40.5
    discoverability: 44.6
    operational_transparency: 0.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 7
      marker_coverage: 100.0
      total: 7
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Creduse Authentication
  slug: creduse-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Creduse Domain Security
  slug: creduse-domain-security
  summary_line: TLSv1.3 · DMARC
slug: creduse
tags:
- Company
website: https://creduse.com/
---
