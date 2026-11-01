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
    openapi_examples: false
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 18.0
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: Integration Platform API documented at docs.usemip.com
  name: MIP API
  slug: mip-api
- description: 'usemip.com API as documented publicly: 7 operations. Contract generated from the documentation by API Evangelist (2026-10-22); not the provider''s own document.'
  name: usemip.com API
  slug: usemip-api
artifact_total: 10
common:
- group: design
  href: https://artifacts.apis.io/usemip/rules/usemip-rules.yml
  title: ''
  type: Spectral
  url: rules/usemip-rules.yml
- group: design
  href: https://artifacts.apis.io/usemip/json-ld/usemip-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/usemip-context.jsonld
- group: design
  href: https://artifacts.apis.io/usemip/vocabulary/usemip-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/usemip-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/usemip/data-model/usemip-data-model.yml
  title: ''
  type: DataModel
  url: data-model/usemip-data-model.yml
- group: auth
  href: https://artifacts.apis.io/usemip/authentication/usemip-authentication.yml
  title: ''
  type: Authentication
  url: authentication/usemip-authentication.yml
- group: design
  href: https://artifacts.apis.io/usemip/conformance/usemip-conformance.yml
  title: ''
  type: Conformance
  url: conformance/usemip-conformance.yml
- group: other
  href: https://artifacts.apis.io/usemip/hosts/usemip-hosts.yml
  title: ''
  type: Hosts
  url: hosts/usemip-hosts.yml
- group: other
  href: https://artifacts.apis.io/usemip/vendors/usemip-vendors.yml
  title: ''
  type: Vendors
  url: vendors/usemip-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://usemip.com/privacy-policy/
- group: auth
  href: https://artifacts.apis.io/usemip/security/usemip-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/usemip-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://usemip.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.usemip.com/
- group: company
  title: ''
  type: Blog
  url: https://usemip.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://usemip.com/contact-us/
coverage:
  checked: '2026-10-22'
  detail: Docs are rendered via Docusaurus JavaScript and no OpenAPI spec is available.
  evidence:
  - status: 200
    url: https://docs.usemip.com/openapi.yaml
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-21'
description: MDP Integration Platform is an AI‑powered hybrid integration platform that manages end‑to‑end data flows between ERP and external systems. It enables organizations to streamline business processes, automate workflows, and optimize data integration across cloud and on‑premise applications, providing a unified view of data and operational efficiency.
json_schemas:
- name: DeleteApiFlowsFlowidResponse
  property_count: 2
  slug: usemip-delete-api-flows-flowid-response
- name: DeleteApiFlowsResponse
  property_count: 2
  slug: usemip-delete-api-flows-response
- name: GetApiFlowsFlowidDeploymentResponse
  property_count: 9
  slug: usemip-get-api-flows-flowid-deployment-response
- name: GetApiNumberRangesIdFlowsResponse
  property_count: 1
  slug: usemip-get-api-number-ranges-id-flows-response
jsonld:
- class_count: 4
  name: Usemip Context
  property_count: 10
  slug: usemip-context
layout: provider
modified: '2026-10-21'
name: usemip.com
nav: Providers
network: true
overview: 'usemip.com is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Integration, Artificial Intelligence, Data, Platform, and Hybrid.


  The usemip.com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  usemip.com''s developer surface includes authentication, documentation, engineering blog, support, and 10 more developer resources.'
random_paper: 11
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: usemip.com API Rules
  rule_count: 9
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 1
  slug: usemip-rules
score:
  band: emerging
  composite: 21.9
  coverage:
    artifact_dirs: 15
    catalog_earned: 52.8
    catalog_earned_first_party: 0.0
    catalog_gap: 62.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 22.1
    developer_ergonomics: 28.6
    discoverability: 53.6
    operational_transparency: 0.0
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 5
      marker_coverage: 100.0
      total: 5
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.1
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Usemip Authentication
  slug: usemip-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Usemip Domain Security
  slug: usemip-domain-security
  summary_line: TLSv1.3
slug: usemip
tags:
- Integration
- Artificial Intelligence
- Data
- Platform
- Hybrid
website: https://usemip.com/
---
