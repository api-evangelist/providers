---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
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
    openapi_examples: partial
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 22.5
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 627
  human_in_the_loop: 4
  name: Oystehr Agentic Access
  operation_count: 1377
  slug: oystehr-agentic-access
  summary_line: 1377 operations · 627 acting · 4 human-in-the-loop
api_count: 8
apis:
- baseURL: https://extensions.fhir.oystehr.com
  baseurl_source: declared
  description: 'Oystehr API as documented publicly: 19 operations. Contract generated from the documentation by API Evangelist (2026-10-27); not the provider''s own document.'
  name: Oystehr API
  slug: oystehr-api
artifact_total: 13
common:
- group: design
  href: https://artifacts.apis.io/oystehr/rules/oystehr-rules.yml
  title: ''
  type: Spectral
  url: rules/oystehr-rules.yml
- group: design
  href: https://artifacts.apis.io/oystehr/json-ld/oystehr-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/oystehr-context.jsonld
- group: design
  href: https://artifacts.apis.io/oystehr/vocabulary/oystehr-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/oystehr-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/oystehr/data-model/oystehr-data-model.yml
  title: ''
  type: DataModel
  url: data-model/oystehr-data-model.yml
- group: operate
  href: https://artifacts.apis.io/oystehr/changelog/oystehr-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/oystehr-changelog.yml
- group: auth
  href: https://artifacts.apis.io/oystehr/authentication/oystehr-authentication.yml
  title: ''
  type: Authentication
  url: authentication/oystehr-authentication.yml
- group: design
  href: https://artifacts.apis.io/oystehr/conformance/oystehr-conformance.yml
  title: ''
  type: Conformance
  url: conformance/oystehr-conformance.yml
- group: other
  href: https://artifacts.apis.io/oystehr/hosts/oystehr-hosts.yml
  title: ''
  type: Hosts
  url: hosts/oystehr-hosts.yml
- group: other
  href: https://artifacts.apis.io/oystehr/vendors/oystehr-vendors.yml
  title: ''
  type: Vendors
  url: vendors/oystehr-vendors.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.oystehr.com/ottehr/setup/introduction/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.oystehr.com/
- group: auth
  href: https://artifacts.apis.io/oystehr/security/oystehr-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/oystehr-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://oystehr.com/
created: '2026-10-27'
description: Oystehr provides a developer‑first, headless electronic health record (EHR) platform that is ONC certified. It offers a comprehensive set of APIs and infrastructure enabling developers to build next‑generation health‑tech applications, including telehealth, messaging, eRx, insurance validation, and claims submission, all at a fraction of traditional costs.
json_schemas:
- name: GetR4ExportJobIdResponse
  property_count: 3
  slug: oystehr-get-r4-export-job-id-response
- name: GetR4GroupIdExportResponse
  property_count: 3
  slug: oystehr-get-r4-group-id-export-response
- name: GetR4Practitioner2419A78E4C0A411DB9E290Dc081F5EfaResponse
  property_count: 2
  slug: oystehr-get-r4-practitioner2419-a78-e4-c0-a411-db9-e290-dc081-f5-efa-response
- name: GetRestSearchCurrentResponse
  property_count: 2
  slug: oystehr-get-rest-search-current-response
- name: PatchV1ZambdaZambdaidRequest
  property_count: 1
  slug: oystehr-patch-v1-zambda-zambdaid-request
- name: PostV1ZambdaYourZambdaIdExecuteResponse
  property_count: 2
  slug: oystehr-post-v1-zambda-your-zambda-id-execute-response
jsonld:
- class_count: 7
  name: Oystehr Context
  property_count: 8
  slug: oystehr-context
layout: provider
modified: '2026-10-27'
name: Oystehr
nav: Providers
network: true
overview: 'Oystehr publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network. Tagged areas include Company, HealthTech, EHR, API, and DeveloperFirst.


  The Oystehr catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Oystehr''s developer surface includes changelog, authentication, getting-started guide, documentation, and 9 more developer resources.'
random_paper: 14
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: Oystehr API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: oystehr-rules
score:
  band: thin
  composite: 32.4
  coverage:
    artifact_dirs: 21
    catalog_earned: 60.8
    catalog_earned_first_party: 0.0
    catalog_gap: 54.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 56.3
    developer_ergonomics: 33.3
    discoverability: 67.9
    operational_transparency: 15.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 9
      marker_coverage: 100.0
      total: 167
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 13.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Oystehr Authentication
  slug: oystehr-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Oystehr Domain Security
  slug: oystehr-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: sample-skill
  slug: oystehr-sample-skill
slug: oystehr
tags:
- Company
- HealthTech
- EHR
- API
- DeveloperFirst
website: https://oystehr.com/
---
