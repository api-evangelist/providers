---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
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
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 38.8
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: 'Sift API as documented publicly: 11 operations. Contract generated from the documentation by API Evangelist (2026-10-26); not the provider''s own document.'
  name: Sift API
  slug: siftscience-com-api
artifact_total: 11
common:
- group: auth
  href: https://artifacts.apis.io/siftscience-com/well-known/siftscience-com-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/siftscience-com-status-security.txt
- group: design
  href: https://artifacts.apis.io/siftscience-com/rules/siftscience-com-rules.yml
  title: ''
  type: Spectral
  url: rules/siftscience-com-rules.yml
- group: design
  href: https://artifacts.apis.io/siftscience-com/json-ld/siftscience-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/siftscience-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/siftscience-com/vocabulary/siftscience-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/siftscience-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/siftscience-com/data-model/siftscience-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/siftscience-com-data-model.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.siftscience.com/
- group: design
  href: https://artifacts.apis.io/siftscience-com/conformance/siftscience-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/siftscience-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/siftscience-com/llms/siftscience-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/siftscience-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/siftscience-com/well-known/siftscience-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/siftscience-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/siftscience-com/hosts/siftscience-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/siftscience-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/siftscience-com/vendors/siftscience-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/siftscience-com-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.sift.com/?_gl=1*1i2xc1z*_gcl_au*MTU1MjA1MDc5Ny4xNzI5MDEwMTg3*_ga*NDU5MTA0MjYwLjE3MjkwMTAxODc.*_ga_R8SV2EK5NZ*MTczMjkxMjI5Ny44NS4xLjE3MzI5MTI3OTguNTkuMC4w
- group: company
  title: ''
  type: Newsroom
  url: https://sift.com/company/newsroom/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.sift.com/?_gl=1*1xozy3y*_gcl_au*ODE1MTM0MDY0LjE3NzkyMTkyNTIuNDc3NzU2NTIxLjE3ODI5MzM0MjMuMTc4MjkzNTM0OA..*_ga*MTI3MDM3NDI2NS4xNzcwNjU0MjYz*_ga_R8SV2EK5NZ*czE3ODQxMjI3ODUkbzIxNCRnMSR0MTc4NDEyMzU3NyRqNTkkbDAkaDA.
- group: company
  title: ''
  type: Blog
  url: https://sift.com/blog/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.siftscience.com/
- group: auth
  href: https://artifacts.apis.io/siftscience-com/security/siftscience-com-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/siftscience-com-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/siftscience-com/security/siftscience-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/siftscience-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://siftscience.com/
coverage:
  checked: '2026-10-26'
  detail: Documentation is served as JavaScript‑rendered HTML with no machine‑readable OpenAPI spec discovered.
  evidence:
  - status: 200
    url: https://sift.com/docs/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-25'
description: Sift provides a real‑time fraud prevention platform that stops payment fraud and account takeover. It offers transparent workflows, global data, and expert analysts, delivering machine‑learning‑driven risk decisions via APIs and dashboards. The service protects e‑commerce, fintech, and digital businesses with customizable rules, scoring, and extensive reporting.
image: https://sift.com/wp-content/uploads/2026/07/Digital-Fraud-Prevention-Risk-Based-Authentication-Sift.png
json_schemas:
- name: GetV3AccountsAccountidSessionsSessionidResponse
  property_count: 3
  slug: siftscience-com-get-v3-accounts-accountid-sessions-sessionid-response
- name: PostV203EventsRequest
  property_count: 3
  slug: siftscience-com-post-v203-events-request
- name: PostV203EventsResponse
  property_count: 3
  slug: siftscience-com-post-v203-events-response
- name: PostV204EventsRequest
  property_count: 3
  slug: siftscience-com-post-v204-events-request
- name: PostV3AccountsIdDevicesIdResponse
  property_count: 1
  slug: siftscience-com-post-v3-accounts-id-devices-id-response
- name: PutV3AccountsAccountidDevicesDeviceidLabelRequest
  property_count: 1
  slug: siftscience-com-put-v3-accounts-accountid-devices-deviceid-label-request
jsonld:
- class_count: 10
  name: Siftscience Com Context
  property_count: 5
  slug: siftscience-com-context
layout: provider
modified: '2026-10-25'
name: Sift
nav: Providers
network: true
overview: 'Sift is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fraud Prevention, Real-time, Machine Learning, and API.


  The Sift catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Sift''s developer surface includes engineering blog, documentation, and 17 more developer resources.'
random_paper: 20
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: Sift API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: siftscience-com-rules
score:
  band: emerging
  composite: 25.5
  coverage:
    artifact_dirs: 14
    catalog_earned: 54.8
    catalog_earned_first_party: 0.0
    catalog_gap: 60.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 15.8
    contract_governance: 22.0
    contract_quality: 21.6
    developer_ergonomics: 21.4
    discoverability: 58.9
    operational_transparency: 26.3
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
    score: 20.0
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Siftscience Com Domain Security
  slug: siftscience-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Siftscience Com Trust Center
  slug: siftscience-com-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: siftscience-com
tags:
- Company
- Fraud Prevention
- Real-time
- Machine Learning
- API
website: https://siftscience.com/
---
