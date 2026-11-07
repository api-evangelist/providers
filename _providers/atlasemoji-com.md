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
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 29.2
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Atlasemoji is a manifest-first geospatial publishing system.
  name: Atlasemoji API
  slug: atlasemoji-api
- description: 'Atlasemoji API as documented publicly: 23 operations. Contract generated from the documentation by API Evangelist (2026-11-01); not the provider''s own document.'
  name: Atlasemoji API
  slug: atlasemoji-com-api
artifact_total: 13
common:
- group: design
  href: https://artifacts.apis.io/atlasemoji-com/rules/atlasemoji-com-rules.yml
  title: ''
  type: Spectral
  url: rules/atlasemoji-com-rules.yml
- group: design
  href: https://artifacts.apis.io/atlasemoji-com/json-ld/atlasemoji-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/atlasemoji-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/atlasemoji-com/vocabulary/atlasemoji-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/atlasemoji-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/atlasemoji-com/data-model/atlasemoji-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/atlasemoji-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/atlasemoji-com/conformance/atlasemoji-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/atlasemoji-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/atlasemoji-com/well-known/atlasemoji-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/atlasemoji-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/atlasemoji-com/hosts/atlasemoji-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/atlasemoji-com-hosts.yml
- group: auth
  href: https://artifacts.apis.io/atlasemoji-com/security/atlasemoji-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/atlasemoji-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://atlasemoji.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://atlasemoji.com/developers
- group: docs
  title: ''
  type: Documentation
  url: https://atlasemoji.com/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://atlasemoji.com/ar/developers/api/quick-start
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://atlasemoji.com/privacy
- group: start
  title: ''
  type: SignUp
  url: https://atlasemoji.com/register
coverage:
  checked: '2026-11-02'
  detail: MCP endpoint requires JSON-RPC POST and returns 406 without authentication.
  evidence:
  - status: 405
    url: https://atlasemoji.com/api/mcp
  reason: auth-required
  state: gated
created: '2026-11-01'
description: 'Atlasemoji is a GIS+PaaS platform for B2B, UAV, UUV, ROV, sensor and AI workflows, connecting spatial data, APIs, MCP, agents and operational systems. Most maps help people find where they are going. Atlasemoji helps people explain why a place matters. A point can become a waypoint. A few waypoints can become a route. A boundary can become a service area, study zone, safety perimeter, customer territory, or geofence. A map can become a story, workspace, dataset, API object, or live operational surface. The idea is simple: geographic work should not have to be rebuilt from scratch every time someone needs it. Atlasemoji does something similar for spatial geometry, holding places, routes, boundaries, observations, layers, manifests, and map-ready objects that evolve over time.'
image: https://atlasemoji.com/home/atlasemoji-home-hero-desktop.png
json_schemas:
- name: PostApiDatasynchGeofenceEventsRequest
  property_count: 4
  slug: atlasemoji-com-post-api-datasynch-geofence-events-request
- name: PostApiDatasynchIntegrationsReceiverRequest
  property_count: 5
  slug: atlasemoji-com-post-api-datasynch-integrations-receiver-request
- name: PostApiDatasynchMasterTablesImportRequest
  property_count: 5
  slug: atlasemoji-com-post-api-datasynch-master-tables-import-request
- name: PostApiDatasynchTelemetryEventsRequest
  property_count: 5
  slug: atlasemoji-com-post-api-datasynch-telemetry-events-request
- name: PostApiDatasynchXrefEvaluateRequest
  property_count: 4
  slug: atlasemoji-com-post-api-datasynch-xref-evaluate-request
- name: PostApiImportGeojsonRequest
  property_count: 2
  slug: atlasemoji-com-post-api-import-geojson-request
jsonld:
- class_count: 13
  name: Atlasemoji Com Context
  property_count: 29
  slug: atlasemoji-com-context
layout: provider
modified: '2026-11-01'
name: Atlasemoji
nav: Providers
network: true
overview: 'Atlasemoji is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include GIS, Platform, Artificial Intelligence, UAV, and Location Intelligence.


  The Atlasemoji catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Atlasemoji''s developer surface includes documentation, getting-started guide, signup flow, and 11 more developer resources.'
random_paper: 13
rules:
- authorship: generated
  effective_rule_count: 87
  extends:
  - spectral:oas
  name: Atlasemoji API Rules
  rule_count: 46
  severity_counts:
    error: 44
    hint: 0
    info: 1
    warn: 1
  slug: atlasemoji-com-rules
scopes:
- name: Atlasemoji Com Scopes
  scope_count: 0
  slug: atlasemoji-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 21.7
  coverage:
    artifact_dirs: 25
    catalog_earned: 57.8
    catalog_earned_first_party: 0.0
    catalog_gap: 57.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.7
  facets:
    access_clarity: 11.8
    contract_governance: 22.0
    contract_quality: 24.7
    developer_ergonomics: 15.5
    discoverability: 57.1
    operational_transparency: 0.0
  previous_composite: 27.4
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
    score: 26.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Atlasemoji Com Authentication
  slug: atlasemoji-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Atlasemoji Com Domain Security
  slug: atlasemoji-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: atlasemoji-com
tags:
- GIS
- Platform
- Artificial Intelligence
- UAV
- Location Intelligence
website: https://atlasemoji.com/
---
