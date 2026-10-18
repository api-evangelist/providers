---
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
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 29.9
  scored_at: '2026-10-17'
api_count: 7
apis:
- description: CloudHealth API provides access to cloud financial management data.
  name: CloudHealth API
  slug: cloudhealth-api
- baseURL: https://chapi.cloudhealthtech.com
  baseurl_source: declared
  description: The Aws Accounts API from Cloudhealthsystems — 2 operation(s) for aws accounts.
  name: Cloudhealthsystems Aws Accounts API
  slug: cloudhealthsystems-aws-accounts-api
- baseURL: https://chapi.cloudhealthtech.com
  baseurl_source: declared
  description: The Cloudhealthsystems API API from Cloudhealthsystems — 4 operation(s) for cloudhealthsystems api.
  name: Cloudhealthsystems Cloudhealthsystems API
  slug: cloudhealthsystems-cloudhealthsystems-api-api
- baseURL: https://chapi.cloudhealthtech.com
  baseurl_source: declared
  description: The Olap Reports API from Cloudhealthsystems — 6 operation(s) for olap reports.
  name: Cloudhealthsystems Olap Reports API
  slug: cloudhealthsystems-olap-reports-api
- baseURL: https://chapi.cloudhealthtech.com
  baseurl_source: declared
  description: The Perspective Schemas API from Cloudhealthsystems — 1 operation(s) for perspective schemas.
  name: Cloudhealthsystems Perspective Schemas API
  slug: cloudhealthsystems-perspective-schemas-api
- baseURL: https://chapi.cloudhealthtech.com
  baseurl_source: declared
  description: The Rest API from Cloudhealthsystems — 1 operation(s) for rest.
  name: Cloudhealthsystems Rest API
  slug: cloudhealthsystems-rest-api
- baseURL: https://chapi.cloudhealthtech.com
  baseurl_source: declared
  description: The Sso API from Cloudhealthsystems — 2 operation(s) for sso.
  name: Cloudhealthsystems SSO API
  slug: cloudhealthsystems-sso-api
artifact_total: 16
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cloudhealthsystems/refs/heads/main/vendors/cloudhealthsystems-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cloudhealthsystems-vendors.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cloudhealthsystems/refs/heads/main/rules/cloudhealthsystems-rules.yml
  title: ''
  type: Spectral
  url: rules/cloudhealthsystems-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cloudhealthsystems/refs/heads/main/json-ld/cloudhealthsystems-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/cloudhealthsystems-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cloudhealthsystems/refs/heads/main/vocabulary/cloudhealthsystems-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/cloudhealthsystems-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cloudhealthsystems/refs/heads/main/data-model/cloudhealthsystems-data-model.yml
  title: ''
  type: DataModel
  url: data-model/cloudhealthsystems-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cloudhealthsystems/refs/heads/main/conformance/cloudhealthsystems-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cloudhealthsystems-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cloudhealthsystems/refs/heads/main/well-known/cloudhealthsystems-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cloudhealthsystems-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cloudhealthsystems/refs/heads/main/hosts/cloudhealthsystems-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cloudhealthsystems-hosts.yml
- group: operate
  title: ''
  type: Support
  url: https://help.cloudhealthtech.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://help.cloudhealthtech.com/quickstart/
- group: docs
  title: ''
  type: Documentation
  url: https://apidocs.cloudhealthtech.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cloudhealthsystems/refs/heads/main/security/cloudhealthsystems-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cloudhealthsystems-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://apps.cloudhealthtech.com
created: '2026-10-09'
description: CloudHealth, part of Broadcom, provides a cloud financial management platform that simplifies cost management, governance, and security across multi‑cloud environments. The service offers dashboards, reporting, automation, and optimization tools to help enterprises control cloud spend, enforce policies, and improve operational efficiency. It integrates with major cloud providers and supports multi‑account, multi‑region visibility, enabling finance and engineering teams to collaborate on cloud cost governance.
json_schemas:
- name: GetOlapReportsCustomReportidResponse
  property_count: 8
  slug: cloudhealthsystems-get-olap-reports-custom-reportid-response
- name: GetOlapReportsOlapreportidResponse
  property_count: 1
  slug: cloudhealthsystems-get-olap-reports-olapreportid-response
- name: GetOlapReportsResponse
  property_count: 1
  slug: cloudhealthsystems-get-olap-reports-response
- name: GetOlapReportsUsageInstanceResponse
  property_count: 8
  slug: cloudhealthsystems-get-olap-reports-usage-instance-response
- name: PostV1V1IdRequest
  property_count: 6
  slug: cloudhealthsystems-post-v1-v1-id-request
- name: PutV1PerspectiveSchemasPerspectiveidResponse
  property_count: 8
  slug: cloudhealthsystems-put-v1-perspective-schemas-perspectiveid-response
jsonld:
- class_count: 10
  name: Cloudhealthsystems Context
  property_count: 17
  slug: cloudhealthsystems-context
layout: provider
modified: '2026-10-09'
name: Cloudhealthsystems
nav: Providers
network: true
overview: 'Cloudhealthsystems is listed with 7 APIs on the [APIs.io](https://apis.io/) network, including Aws Accounts API, Cloudhealthsystems API, Olap Reports API, and 4 more. Tagged areas include Cloud, Financial Management, Multi-Cloud, Cost Optimization, and Governance.


  The Cloudhealthsystems catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Cloudhealthsystems'' developer surface includes support, getting-started guide, documentation, and 10 more developer resources.'
random_paper: 21
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: Cloudhealthsystems API Rules
  rule_count: 12
  severity_counts:
    error: 9
    hint: 0
    info: 2
    warn: 1
  slug: cloudhealthsystems-rules
score:
  band: emerging
  composite: 20.6
  coverage:
    artifact_dirs: 13
    catalog_earned: 63.8
    catalog_earned_first_party: 0.0
    catalog_gap: 51.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 25.7
    developer_ergonomics: 26.2
    discoverability: 67.9
    operational_transparency: 0.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 7
      marker_coverage: 100.0
      total: 7
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: domain-security
  name: Cloudhealthsystems Domain Security
  slug: cloudhealthsystems-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: cloudhealthsystems
tags:
- Cloud
- Financial Management
- Multi-Cloud
- Cost Optimization
- Governance
website: https://apps.cloudhealthtech.com
---
