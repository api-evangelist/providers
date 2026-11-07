---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
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
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 20.1
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Frigate provides a RESTful API for managing cameras, recordings, and detections as documented in the configuration reference.
  name: Frigate API
  slug: frigate-api-2
- description: 'Frigate NVR API as documented publicly: 5 operations. Contract generated from the documentation by API Evangelist (2026-10-28); not the provider''s own document.'
  name: Frigate NVR API
  slug: frigate-api
artifact_total: 10
common:
- group: design
  href: https://artifacts.apis.io/frigate/rules/frigate-rules.yml
  title: ''
  type: Spectral
  url: rules/frigate-rules.yml
- group: design
  href: https://artifacts.apis.io/frigate/json-ld/frigate-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/frigate-context.jsonld
- group: design
  href: https://artifacts.apis.io/frigate/vocabulary/frigate-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/frigate-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/frigate/data-model/frigate-data-model.yml
  title: ''
  type: DataModel
  url: data-model/frigate-data-model.yml
- group: auth
  href: https://artifacts.apis.io/frigate/authentication/frigate-authentication.yml
  title: ''
  type: Authentication
  url: authentication/frigate-authentication.yml
- group: design
  href: https://artifacts.apis.io/frigate/conformance/frigate-conformance.yml
  title: ''
  type: Conformance
  url: conformance/frigate-conformance.yml
- group: other
  href: https://artifacts.apis.io/frigate/hosts/frigate-hosts.yml
  title: ''
  type: Hosts
  url: hosts/frigate-hosts.yml
- group: other
  href: https://artifacts.apis.io/frigate/vendors/frigate-vendors.yml
  title: ''
  type: Vendors
  url: vendors/frigate-vendors.yml
- group: build
  href: https://artifacts.apis.io/frigate/packages/frigate-packages.yml
  title: ''
  type: SDKs
  url: packages/frigate-packages.yml
- group: build
  href: https://artifacts.apis.io/frigate/packages/frigate-packages.yml
  title: ''
  type: Packages
  url: packages/frigate-packages.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/blakeblackshear/frigate/releases
- group: docs
  title: ''
  type: APIReference
  url: https://docs.frigate.video/configuration/advanced/reference
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.frigate-cn.video
- group: auth
  href: https://artifacts.apis.io/frigate/security/frigate-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/frigate-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://frigate.video/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.frigate.video
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/blakeblackshear/frigate
coverage:
  checked: '2026-10-28'
  detail: Documentation provides configuration reference but no machine‑readable OpenAPI, AsyncAPI, GraphQL, gRPC or WSDL contracts.
  evidence:
  - status: 200
    url: https://docs.frigate.video/configuration/advanced/reference
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: Frigate NVR provides an open source network video recorder (NVR) that uses modern AI object detection to monitor security cameras. It integrates with popular camera platforms, offers a web UI, and supports real‑time alerts, recordings, and customizable zones. The project is community‑driven, with extensive documentation, Docker deployment options, and active development aimed at simplifying video surveillance for homes and businesses.
image: https://frigate.video/logo.png
json_schemas:
- name: PostApiLoginRequest
  property_count: 2
  slug: frigate-post-api-login-request
- name: PostApiMediaSyncResponse
  property_count: 1
  slug: frigate-post-api-media-sync-response
- name: PostExportCustomCameranameStartStarttimeEndEndtimeRequest
  property_count: 4
  slug: frigate-post-export-custom-cameraname-start-starttime-end-endtime-request
- name: PostExportCustomCameranameStartStarttimeEndEndtimeResponse
  property_count: 1
  slug: frigate-post-export-custom-cameraname-start-starttime-end-endtime-response
jsonld:
- class_count: 4
  name: Frigate Context
  property_count: 7
  slug: frigate-context
layout: provider
modified: '2026-10-28'
name: Frigate NVR
nav: Providers
network: true
overview: 'Frigate NVR is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Video, Surveillance, Open Source, and Artificial Intelligence.


  The Frigate NVR catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Frigate NVR''s developer surface includes authentication, changelog, API reference, documentation, and 13 more developer resources.'
random_paper: 18
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: Frigate NVR API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: frigate-rules
score:
  band: emerging
  composite: 20.5
  coverage:
    artifact_dirs: 18
    catalog_earned: 51.8
    catalog_earned_first_party: 0.0
    catalog_gap: 63.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.0
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 20.1
    developer_ergonomics: 32.1
    discoverability: 57.1
    operational_transparency: 10.5
  previous_composite: 24.5
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
    score: 15.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/frigate/frigate-2026-11-03T132345.png
security:
- kind: authentication
  name: Frigate Authentication
  slug: frigate-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Frigate Domain Security
  slug: frigate-domain-security
  summary_line: TLSv1.3 · DMARC
slug: frigate
tags:
- Company
- Video
- Surveillance
- Open Source
- Artificial Intelligence
website: https://frigate.video/
---
