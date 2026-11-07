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
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 32.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 29
  human_in_the_loop: 0
  name: Adaptris Agentic Access
  operation_count: 135
  slug: adaptris-agentic-access
  summary_line: 135 operations · 29 acting
api_count: 1
apis:
- baseURL: /interlok/api
  baseurl_source: spec
  description: The /adapter API from Adaptris — 12 operation(s) for /adapter.
  name: Adaptris /adapter API
  slug: adaptris-adapter-api
- baseURL: /interlok/api
  baseurl_source: spec
  description: The /adapter/component-checker API from Adaptris — 2 operation(s) for /adapter/component-checker.
  name: Adaptris /adapter/component Checker API
  slug: adaptris-adapter-component-checker-api
- baseURL: /interlok/api
  baseurl_source: spec
  description: The /adapter/failed-messages API from Adaptris — 12 operation(s) for /adapter/failed-messages.
  name: Adaptris /adapter/failed Messages API
  slug: adaptris-adapter-failed-messages-api
- baseURL: /interlok/api
  baseurl_source: spec
  description: The /adapter/metrics API from Adaptris — 4 operation(s) for /adapter/metrics.
  name: Adaptris /adapter/metrics API
  slug: adaptris-adapter-metrics-api
- baseURL: /interlok/api
  baseurl_source: spec
  description: The /adapter/platform API from Adaptris — 22 operation(s) for /adapter/platform.
  name: Adaptris /adapter/platform API
  slug: adaptris-adapter-platform-api
- baseURL: /interlok/api
  baseurl_source: spec
  description: The /channel API from Adaptris — 12 operation(s) for /channel.
  name: Adaptris /channel API
  slug: adaptris-channel-api
- baseURL: /interlok/api
  baseurl_source: spec
  description: The /channel/failed-messages API from Adaptris — 2 operation(s) for /channel/failed-messages.
  name: Adaptris /channel/failed Messages API
  slug: adaptris-channel-failed-messages-api
- baseURL: /interlok/api
  baseurl_source: spec
  description: The /channel/metrics API from Adaptris — 4 operation(s) for /channel/metrics.
  name: Adaptris /channel/metrics API
  slug: adaptris-channel-metrics-api
- baseURL: /interlok/api
  baseurl_source: spec
  description: The deprecated API from Adaptris — 21 operation(s) for deprecated.
  name: Adaptris Deprecated API
  slug: adaptris-deprecated-api
- baseURL: /interlok/api
  baseurl_source: spec
  description: The /workflow API from Adaptris — 12 operation(s) for /workflow.
  name: Adaptris /workflow API
  slug: adaptris-workflow-api
- baseURL: /interlok/api
  baseurl_source: spec
  description: The /workflow/failed-messages API from Adaptris — 2 operation(s) for /workflow/failed-messages.
  name: Adaptris /workflow/failed Messages API
  slug: adaptris-workflow-failed-messages-api
- baseURL: /interlok/api
  baseurl_source: spec
  description: The /workflow/metrics API from Adaptris — 10 operation(s) for /workflow/metrics.
  name: Adaptris /workflow/metrics API
  slug: adaptris-workflow-metrics-api
artifact_total: 19
common:
- group: agent
  href: https://artifacts.apis.io/adaptris/agentic-access/adaptris-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/adaptris-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/adaptris/rules/adaptris-rules.yml
  title: ''
  type: Spectral
  url: rules/adaptris-rules.yml
- group: design
  href: https://artifacts.apis.io/adaptris/json-ld/adaptris-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/adaptris-context.jsonld
- group: design
  href: https://artifacts.apis.io/adaptris/vocabulary/adaptris-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/adaptris-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/adaptris/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/adaptris/data-model/adaptris-data-model.yml
  title: ''
  type: DataModel
  url: data-model/adaptris-data-model.yml
- group: design
  href: https://artifacts.apis.io/adaptris/errors/adaptris-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/adaptris-problem-types.yml
- group: design
  href: https://artifacts.apis.io/adaptris/conformance/adaptris-conformance.yml
  title: ''
  type: Conformance
  url: conformance/adaptris-conformance.yml
- group: agent
  href: https://artifacts.apis.io/adaptris/well-known/adaptris-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/adaptris-well-known.yml
- group: other
  href: https://artifacts.apis.io/adaptris/hosts/adaptris-hosts.yml
  title: ''
  type: Hosts
  url: hosts/adaptris-hosts.yml
- group: auth
  href: https://artifacts.apis.io/adaptris/security/adaptris-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/adaptris-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://adaptris.com/
created: '2026-10-19'
description: Adaptris provides integration solutions enabling enterprises to connect applications, data, and devices across cloud and on‑premises environments. Their platform offers a range of adapters, messaging, and workflow capabilities to simplify building robust integration pipelines, supporting APIs, event‑driven architectures, and legacy system connectivity. Founded to accelerate digital transformation, Adaptris serves financial services, healthcare, and technology sectors with scalable, secure integration services.
json_schemas:
- name: AdapterJmxInterlokDetails
  property_count: 8
  slug: adaptris-adapter-jmx-interlok-details
- name: ComponentCheckWrapper
  property_count: 3
  slug: adaptris-component-check-wrapper
- name: StateWrapper
  property_count: 2
  slug: adaptris-state-wrapper
jsonld:
- class_count: 14
  name: Adaptris Context
  property_count: 50
  slug: adaptris-context
layout: provider
modified: '2026-10-19'
name: Adaptris
nav: Providers
network: true
overview: 'Adaptris publishes 12 API contracts indexed on the [APIs.io](https://apis.io/) network, including /adapter API, /adapter/component Checker API, /adapter/failed Messages API, and 9 more. Tagged areas include Company, Integration, Messaging, and Cloud.


  The Adaptris catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.'
random_paper: 16
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: Adaptris API Rules
  rule_count: 10
  severity_counts:
    error: 7
    hint: 0
    info: 2
    warn: 1
  slug: adaptris-rules
score:
  band: emerging
  composite: 19.1
  coverage:
    artifact_dirs: 19
    catalog_earned: 50.8
    catalog_earned_first_party: 0.0
    catalog_gap: 64.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 48.5
    developer_ergonomics: 1.8
    discoverability: 44.6
    operational_transparency: 0.0
  previous_composite: 19.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 12
    mcp: derived
    skills: derived
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
screenshot: https://apis.io/screenshots/adaptris/adaptris-2026-11-03T120240.png
security:
- kind: domain-security
  name: Adaptris Domain Security
  slug: adaptris-domain-security
  summary_line: TLSv1.3 · DMARC
slug: adaptris
tags:
- Company
- Integration
- Messaging
- Cloud
website: https://adaptris.com/
---
