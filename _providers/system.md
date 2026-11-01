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
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 19.1
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: System REST API providing clinical graph endpoints
  name: System REST API
  slug: system-rest-api
- baseURL: https://api-prod.system.com
  baseurl_source: declared
  description: This page provides documentation for the System REST API.
  name: System REST API API
  slug: system-rest-api-api
artifact_total: 12
common:
- group: design
  href: https://artifacts.apis.io/system/rules/system-rules.yml
  title: ''
  type: Spectral
  url: rules/system-rules.yml
- group: design
  href: https://artifacts.apis.io/system/json-ld/system-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/system-context.jsonld
- group: design
  href: https://artifacts.apis.io/system/vocabulary/system-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/system-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/system/data-model/system-data-model.yml
  title: ''
  type: DataModel
  url: data-model/system-data-model.yml
- group: operate
  href: https://artifacts.apis.io/system/changelog/system-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/system-changelog.yml
- group: auth
  href: https://artifacts.apis.io/system/authentication/system-authentication.yml
  title: ''
  type: Authentication
  url: authentication/system-authentication.yml
- group: design
  href: https://artifacts.apis.io/system/errors/system-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/system-problem-types.yml
- group: design
  href: https://artifacts.apis.io/system/conformance/system-conformance.yml
  title: ''
  type: Conformance
  url: conformance/system-conformance.yml
- group: agent
  href: https://artifacts.apis.io/system/llms/system-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/system-llms.txt
- group: agent
  href: https://artifacts.apis.io/system/well-known/system-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/system-well-known.yml
- group: other
  href: https://artifacts.apis.io/system/hosts/system-hosts.yml
  title: ''
  type: Hosts
  url: hosts/system-hosts.yml
- group: other
  href: https://artifacts.apis.io/system/vendors/system-vendors.yml
  title: ''
  type: Vendors
  url: vendors/system-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://docs.system.com/system/legal/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://docs.system.com/system/legal/legal/privacy-policy
- group: other
  title: ''
  type: Leadership
  url: https://www.system.com/company/team
- group: company
  title: ''
  type: Blog
  url: https://www.system.com/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.system.com/system/public/quick-start-guide
- group: docs
  title: ''
  type: APIReference
  url: https://api-docs.system.com/
- group: auth
  href: https://artifacts.apis.io/system/security/system-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/system-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://system.com
created: '2026-10-24'
description: System provides a platform that models the world as an interconnected system, delivering structured clinical knowledge, ontologies, and a graph‑based API to support diagnostic accuracy, clinical decision‑making, and population health risk management for healthcare organizations and researchers.
image: https://cdn.prod.website-files.com/66e9dff32a2060cb9fa715a8/69a865335351c82eb8750ffc_system_opengraph.png
json_schemas:
- name: MechanisticFinding
  property_count: 10
  slug: system-mechanistic-finding
- name: PubmedSearchSynthesisJob
  property_count: 10
  slug: system-pubmed-search-synthesis-job
- name: Relationship
  property_count: 10
  slug: system-relationship
- name: StatisticalFinding
  property_count: 15
  slug: system-statistical-finding
- name: Study
  property_count: 13
  slug: system-study
- name: Topic
  property_count: 6
  slug: system-topic
jsonld:
- class_count: 50
  name: System Context
  property_count: 96
  slug: system-context
layout: provider
modified: '2026-10-24'
name: System
nav: Providers
network: true
overview: 'System publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network, including REST API API, and 1 more. Tagged areas include Healthcare, Population Health, Knowledge Graph, API Platform, and Public Benefit Corporation.


  The System catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  System''s developer surface includes changelog, authentication, engineering blog, getting-started guide, API reference, and 15 more developer resources.'
random_paper: 5
rules:
- authorship: generated
  effective_rule_count: 58
  extends:
  - spectral:oas
  name: System API Rules
  rule_count: 17
  severity_counts:
    error: 14
    hint: 0
    info: 2
    warn: 1
  slug: system-rules
score:
  band: thin
  composite: 37.6
  coverage:
    artifact_dirs: 20
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 22.0
    contract_quality: 56.7
    developer_ergonomics: 33.3
    discoverability: 67.9
    operational_transparency: 15.8
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 19.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: System Authentication
  slug: system-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: System Domain Security
  slug: system-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: system
tags:
- Healthcare
- Population Health
- Knowledge Graph
- API Platform
- Public Benefit Corporation
website: https://system.com
---
