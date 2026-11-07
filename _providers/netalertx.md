---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
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
    auth_clarity: false
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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 12.9
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Programmatic access to devices, events, sessions, metrics, network tools, and sync via REST and GraphQL.
  name: NetAlertX API
  slug: netalertx-api-2
- description: 'NetAlertX API as documented publicly: 69 operations. Contract generated from the documentation by API Evangelist (2026-10-28); not the provider''s own document.'
  name: NetAlertX API
  slug: netalertx-api
artifact_total: 13
common:
- group: design
  href: https://artifacts.apis.io/netalertx/rules/netalertx-rules.yml
  title: ''
  type: Spectral
  url: rules/netalertx-rules.yml
- group: design
  href: https://artifacts.apis.io/netalertx/json-ld/netalertx-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/netalertx-context.jsonld
- group: design
  href: https://artifacts.apis.io/netalertx/vocabulary/netalertx-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/netalertx-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/netalertx/data-model/netalertx-data-model.yml
  title: ''
  type: DataModel
  url: data-model/netalertx-data-model.yml
- group: operate
  href: https://artifacts.apis.io/netalertx/changelog/netalertx-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/netalertx-changelog.yml
- group: design
  href: https://artifacts.apis.io/netalertx/conformance/netalertx-conformance.yml
  title: ''
  type: Conformance
  url: conformance/netalertx-conformance.yml
- group: other
  href: https://artifacts.apis.io/netalertx/hosts/netalertx-hosts.yml
  title: ''
  type: Hosts
  url: hosts/netalertx-hosts.yml
- group: other
  href: https://artifacts.apis.io/netalertx/vendors/netalertx-vendors.yml
  title: ''
  type: Vendors
  url: vendors/netalertx-vendors.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/netalertx/NetAlertX/releases
- group: auth
  href: https://artifacts.apis.io/netalertx/security/netalertx-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/netalertx-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://netalertx.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.netalertx.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.netalertx.com/API/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.netalertx.com/PLUGINS_DEV_QUICK_START/
- group: operate
  title: ''
  type: Support
  url: https://github.com/netalertx/NetAlertX/discussions
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/netalertx
coverage:
  checked: '2026-10-28'
  detail: Documentation provides API description but no publicly available OpenAPI, AsyncAPI, GraphQL schema, or other machine‑readable contract.
  evidence:
  - status: 200
    url: https://docs.netalertx.com/API/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: NetAlertX provides centralized network visibility, continuous asset discovery, real-time alerts, and integration with smart-home and automation platforms. It supports Docker, Unraid, Home Assistant and offers over 80 notification services via Apprise. The open-source solution helps monitor devices, detect changes, and automate responses across single-site or multi-network deployments.
image: https://netalertx.com/favicon.ico
json_schemas:
- name: GetDeviceAaBbCcDdEeFfResponse
  property_count: 12
  slug: netalertx-get-device-aa-bb-cc-dd-ee-ff-response
- name: GetDevicesHistoryFiltersResponse
  property_count: 4
  slug: netalertx-get-devices-history-filters-response
- name: GetMetricsResponse
  property_count: 8
  slug: netalertx-get-metrics-response
- name: GetSyncResponse
  property_count: 5
  slug: netalertx-get-sync-response
- name: PostDeviceAaBbCcDdEeFfUpdateColumnRequest
  property_count: 2
  slug: netalertx-post-device-aa-bb-cc-dd-ee-ff-update-column-request
- name: PostSyncRequest
  property_count: 4
  slug: netalertx-post-sync-request
jsonld:
- class_count: 82
  name: Netalertx Context
  property_count: 101
  slug: netalertx-context
layout: provider
modified: '2026-10-28'
name: NetAlertX
nav: Providers
network: true
overview: 'NetAlertX is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Network Monitoring, Asset Discovery, Home Automation, Open Source, and Self-Hosted.


  The NetAlertX catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  NetAlertX''s developer surface includes changelog, documentation, API reference, getting-started guide, support, and 11 more developer resources.'
random_paper: 23
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: NetAlertX API Rules
  rule_count: 13
  severity_counts:
    error: 7
    hint: 0
    info: 4
    warn: 2
  slug: netalertx-rules
scopes:
- name: Netalertx Scopes
  scope_count: 0
  slug: netalertx-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 21.7
  coverage:
    artifact_dirs: 26
    catalog_earned: 57.8
    catalog_earned_first_party: 0.0
    catalog_gap: 57.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.4
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 25.2
    developer_ergonomics: 16.7
    discoverability: 57.1
    operational_transparency: 10.5
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 26.1
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
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 22.2
screenshot: https://apis.io/screenshots/netalertx/netalertx-2026-11-03T140109.png
security:
- kind: authentication
  name: Netalertx Authentication
  slug: netalertx-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Netalertx Domain Security
  slug: netalertx-domain-security
  summary_line: TLSv1.3 · HSTS
slug: netalertx
tags:
- Network Monitoring
- Asset Discovery
- Home Automation
- Open Source
- Self-Hosted
website: https://netalertx.com/
---
