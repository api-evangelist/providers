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
    mcp_server: false
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 19.7
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: 'Primeur API as documented publicly: 17 operations. Contract generated from the documentation by API Evangelist (2026-10-21); not the provider''s own document.'
  name: Primeur API
  slug: primeur-api
artifact_total: 11
common:
- group: design
  href: https://artifacts.apis.io/primeur/rules/primeur-rules.yml
  title: ''
  type: Spectral
  url: rules/primeur-rules.yml
- group: design
  href: https://artifacts.apis.io/primeur/json-ld/primeur-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/primeur-context.jsonld
- group: design
  href: https://artifacts.apis.io/primeur/vocabulary/primeur-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/primeur-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/primeur/data-model/primeur-data-model.yml
  title: ''
  type: DataModel
  url: data-model/primeur-data-model.yml
- group: operate
  href: https://artifacts.apis.io/primeur/changelog/primeur-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/primeur-changelog.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.primeur.com/en/compliance
- group: design
  href: https://artifacts.apis.io/primeur/conformance/primeur-conformance.yml
  title: ''
  type: Conformance
  url: conformance/primeur-conformance.yml
- group: agent
  href: https://artifacts.apis.io/primeur/llms/primeur-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/primeur-llms.txt
- group: agent
  href: https://artifacts.apis.io/primeur/well-known/primeur-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/primeur-well-known.yml
- group: other
  href: https://artifacts.apis.io/primeur/hosts/primeur-hosts.yml
  title: ''
  type: Hosts
  url: hosts/primeur-hosts.yml
- group: other
  href: https://artifacts.apis.io/primeur/vendors/primeur-vendors.yml
  title: ''
  type: Vendors
  url: vendors/primeur-vendors.yml
- group: auth
  href: https://artifacts.apis.io/primeur/security/primeur-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/primeur-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/primeur/security/primeur-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/primeur-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.primeur.com/en/
- group: company
  title: ''
  type: Blog
  url: https://www.primeur.com/blog
- group: docs
  title: ''
  type: Documentation
  url: https://www.primeur.com/en/
- group: operate
  title: ''
  type: Support
  url: https://www.primeur.com/en/work-with-us
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.primeur.com/en/data-privacy
created: '2026-10-21'
description: Primeur is a Smart Data Integration company offering tools and consulting services. It provides data integration, secured managed file transfer, data transformation, monitoring, GDPR compliance, and data science solutions. Primeur helps enterprises unlock data value through platforms like Data One, Data Mover, and Data Watcher, supporting operational resilience and compliance initiatives.
json_schemas:
- name: DeleteDataOneApplicationApiV1InfrastructureClustersServerSes
  property_count: 5
  slug: primeur-delete-data-one-application-api-v1-infrastructure-clusters-server-ses
- name: DeleteDataOneApplicationApiV1InfrastructureClustersServerSes2
  property_count: 5
  slug: primeur-delete-data-one-application-api-v1-infrastructure-clusters-server-ses2
- name: Get20MetadataHttpApiHttpuploadv2Cookies3TxtResponse
  property_count: 6
  slug: primeur-get20-metadata-http-api-httpuploadv2-cookies3-txt-response
- name: PostDataOneApplicationApiV1InfrastructureClustersServerSessi
  property_count: 5
  slug: primeur-post-data-one-application-api-v1-infrastructure-clusters-server-sessi
- name: PostJobManagerJobsRequest
  property_count: 4
  slug: primeur-post-job-manager-jobs-request
- name: PostJobManagerJobsResponse
  property_count: 15
  slug: primeur-post-job-manager-jobs-response
jsonld:
- class_count: 8
  name: Primeur Context
  property_count: 36
  slug: primeur-context
layout: provider
modified: '2026-10-21'
name: Primeur
nav: Providers
network: true
overview: 'Primeur is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Data Integration, Consulting, GDPR, and Data Science.


  The Primeur catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Primeur''s developer surface includes changelog, engineering blog, documentation, support, and 14 more developer resources.'
random_paper: 4
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: Primeur API Rules
  rule_count: 9
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 0
  slug: primeur-rules
score:
  band: emerging
  composite: 25.3
  coverage:
    artifact_dirs: 15
    catalog_earned: 55.0
    catalog_earned_first_party: 0.0
    catalog_gap: 60.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 26.3
    contract_governance: 19.7
    contract_quality: 24.8
    developer_ergonomics: 16.7
    discoverability: 53.6
    operational_transparency: 15.8
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 9
      marker_coverage: 100.0
      total: 9
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Primeur Domain Security
  slug: primeur-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Primeur Trust Center
  slug: primeur-trust-center
  summary_line: ISO 27001, GDPR
slug: primeur
tags:
- Company
- Data Integration
- Consulting
- GDPR
- Data Science
website: https://www.primeur.com/en/
---
