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
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 40.1
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: 3D Printer Plugin APIs
  name: Spoolman API
  slug: spoolman-api-2
- baseURL: https://octoeverywhere.com
  baseurl_source: declared
  description: 'Spoolman API as documented publicly: 12 operations. Contract generated from the documentation by API Evangelist (2026-10-28); not the provider''s own document.'
  name: Spoolman API
  slug: spoolman-api
artifact_total: 11
common:
- group: design
  href: https://artifacts.apis.io/spoolman/rules/spoolman-rules.yml
  title: ''
  type: Spectral
  url: rules/spoolman-rules.yml
- group: design
  href: https://artifacts.apis.io/spoolman/json-ld/spoolman-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/spoolman-context.jsonld
- group: design
  href: https://artifacts.apis.io/spoolman/vocabulary/spoolman-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/spoolman-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/spoolman/data-model/spoolman-data-model.yml
  title: ''
  type: DataModel
  url: data-model/spoolman-data-model.yml
- group: design
  href: https://artifacts.apis.io/spoolman/conformance/spoolman-conformance.yml
  title: ''
  type: Conformance
  url: conformance/spoolman-conformance.yml
- group: agent
  href: https://artifacts.apis.io/spoolman/well-known/spoolman-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/spoolman-well-known.yml
- group: other
  href: https://artifacts.apis.io/spoolman/hosts/spoolman-hosts.yml
  title: ''
  type: Hosts
  url: hosts/spoolman-hosts.yml
- group: other
  href: https://artifacts.apis.io/spoolman/vendors/spoolman-vendors.yml
  title: ''
  type: Vendors
  url: vendors/spoolman-vendors.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.octoeverywhere.com/webhook-notifications/setup/
- group: company
  title: ''
  type: Website
  url: https://github.com/Donkie/Spoolman
- group: auth
  href: https://artifacts.apis.io/spoolman/security/spoolman-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/spoolman-domain-security.yml
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/Donkie/Spoolman#readme
- group: operate
  title: ''
  type: Support
  url: https://github.com/Donkie/Spoolman/issues
- group: company
  title: ''
  type: Blog
  url: https://blog.octoeverywhere.com/tag/spoolman/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Donkie
coverage:
  checked: '2026-10-28'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine-readable contract was found despite public documentation.
  evidence:
  - status: 200
    url: https://docs.octoeverywhere.com/plugin-api/overview/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: Spoolman is an open-source tool for tracking 3D-printer filament spools. It provides a public REST API that lets users query, add, update, and delete spool records, enabling integration with OctoPrint, Klipper, and other printer management platforms. The project is maintained on GitHub and aims to simplify inventory management for hobbyists and small-scale makers.
json_schemas:
- name: GetApiAppconnectionInfoResponse
  property_count: 10
  slug: spoolman-get-api-appconnection-info-response
- name: PostApiAppconnectionSetnotificationwebhookRequest
  property_count: 3
  slug: spoolman-post-api-appconnection-setnotificationwebhook-request
- name: PostApiGadgetGetstatusfromappconnectionResponse
  property_count: 4
  slug: spoolman-post-api-gadget-getstatusfromappconnection-response
- name: PostApiGadgetV1ContextinfoIdResponse
  property_count: 9
  slug: spoolman-post-api-gadget-v1-contextinfo-id-response
- name: PostApiGadgetV1ExtendcontextIdResponse
  property_count: 2
  slug: spoolman-post-api-gadget-v1-extendcontext-id-response
- name: PostApiLiveCreatefromappconnectionRequest
  property_count: 3
  slug: spoolman-post-api-live-createfromappconnection-request
jsonld:
- class_count: 12
  name: Spoolman Context
  property_count: 34
  slug: spoolman-context
layout: provider
modified: '2026-10-28'
name: Spoolman
nav: Providers
network: true
overview: 'Spoolman is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include 3D Printing, Inventory, Open Source, and filament.


  The Spoolman catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Spoolman''s developer surface includes getting-started guide, documentation, support, engineering blog, and 11 more developer resources.'
random_paper: 9
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: Spoolman API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: spoolman-rules
score:
  band: emerging
  composite: 16.4
  coverage:
    artifact_dirs: 16
    catalog_earned: 50.8
    catalog_earned_first_party: 0.0
    catalog_gap: 64.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.1
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 26.1
    developer_ergonomics: 14.3
    discoverability: 44.6
    operational_transparency: 2.6
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 20.5
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
    score: 16.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/spoolman/spoolman-2026-11-03T143645.png
security:
- kind: domain-security
  name: Spoolman Domain Security
  slug: spoolman-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: spoolman
tags:
- 3D Printing
- Inventory
- Open Source
- filament
---
