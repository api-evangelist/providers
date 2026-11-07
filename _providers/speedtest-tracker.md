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
    event_surface_described: true
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
    well_known_catalog: false
  schema_version: '0.2'
  score: 19.0
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Speedtest Tracker provides a self‑hosted API for monitoring internet performance and uptime.
  name: Speedtest Tracker API
  slug: speedtest-tracker-api-2
- description: 'Speedtest Tracker API as documented publicly: 5 operations. Contract generated from the documentation by API Evangelist (2026-10-28); not the provider''s own document.'
  name: Speedtest Tracker API
  slug: speedtest-tracker-api
artifact_total: 11
asyncapis:
- description: ''
  name: Speedtest Tracker Webhooks
  slug: speedtest-tracker-webhooks
common:
- group: docs
  title: ''
  type: Documentation
  url: https://docs.speedtest-tracker.dev
- group: design
  href: https://artifacts.apis.io/speedtest-tracker/rules/speedtest-tracker-rules.yml
  title: ''
  type: Spectral
  url: rules/speedtest-tracker-rules.yml
- group: design
  href: https://artifacts.apis.io/speedtest-tracker/json-ld/speedtest-tracker-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/speedtest-tracker-context.jsonld
- group: design
  href: https://artifacts.apis.io/speedtest-tracker/vocabulary/speedtest-tracker-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/speedtest-tracker-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/speedtest-tracker/asyncapi/speedtest-tracker-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/speedtest-tracker-webhooks.yml
- group: design
  href: https://artifacts.apis.io/speedtest-tracker/data-model/speedtest-tracker-data-model.yml
  title: ''
  type: DataModel
  url: data-model/speedtest-tracker-data-model.yml
- group: design
  href: https://artifacts.apis.io/speedtest-tracker/conformance/speedtest-tracker-conformance.yml
  title: ''
  type: Conformance
  url: conformance/speedtest-tracker-conformance.yml
- group: agent
  href: https://artifacts.apis.io/speedtest-tracker/llms/speedtest-tracker-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/speedtest-tracker-llms.txt
- group: agent
  href: https://artifacts.apis.io/speedtest-tracker/well-known/speedtest-tracker-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/speedtest-tracker-well-known.yml
- group: other
  href: https://artifacts.apis.io/speedtest-tracker/hosts/speedtest-tracker-hosts.yml
  title: ''
  type: Hosts
  url: hosts/speedtest-tracker-hosts.yml
- group: other
  href: https://artifacts.apis.io/speedtest-tracker/vendors/speedtest-tracker-vendors.yml
  title: ''
  type: Vendors
  url: vendors/speedtest-tracker-vendors.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.speedtest-tracker.dev/releases
- group: auth
  href: https://artifacts.apis.io/speedtest-tracker/security/speedtest-tracker-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/speedtest-tracker-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://docs.speedtest-tracker.dev/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.speedtest-tracker.dev/getting-started/installation
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.speedtest-tracker.dev/releases
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/henrywhitaker3/Speedtest-Tracker
coverage:
  checked: '2026-10-28'
  detail: Documentation is public HTML without any OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL specifications.
  evidence:
  - status: 200
    url: https://docs.speedtest-tracker.dev/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: Speedtest Tracker is a self‑hosted application that monitors internet performance and uptime. Built with Laravel and the Ookla Speedtest CLI, it can be deployed via Docker and provides a web UI, API, and extensive documentation. The project aims to give users a historical view of their connection quality and ISP reliability, offering dashboards, notifications, and integrations for personal or community use.
image: https://docs.speedtest-tracker.dev/~gitbook/ogimage/E5O7qQk6wZ0bWhrjBZNp
json_schemas:
- name: GetApiV1ResultsIdResponse
  property_count: 5
  slug: speedtest-tracker-get-api-v1-results-id-response
- name: GetApiV1ResultsResponse
  property_count: 5
  slug: speedtest-tracker-get-api-v1-results-response
- name: GetApiV1SpeedtestsListServersResponse
  property_count: 4
  slug: speedtest-tracker-get-api-v1-speedtests-list-servers-response
- name: GetApiV1StatsResponse
  property_count: 5
  slug: speedtest-tracker-get-api-v1-stats-response
- name: PostApiV1SpeedtestsRunResponse
  property_count: 5
  slug: speedtest-tracker-post-api-v1-speedtests-run-response
jsonld:
- class_count: 5
  name: Speedtest Tracker Context
  property_count: 0
  slug: speedtest-tracker-context
layout: provider
modified: '2026-10-28'
name: Speedtest Tracker
nav: Providers
network: true
overview: 'Speedtest Tracker is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Self-Hosted, Monitoring, Speed Test, and Docker.


  The Speedtest Tracker catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Speedtest Tracker''s developer surface includes documentation, getting-started guide, changelog, and 14 more developer resources.'
random_paper: 18
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: Speedtest Tracker API Rules
  rule_count: 11
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 0
  slug: speedtest-tracker-rules
score:
  band: emerging
  composite: 20.2
  coverage:
    artifact_dirs: 18
    catalog_earned: 54.0
    catalog_earned_first_party: 0.0
    catalog_gap: 61.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.5
  facets:
    access_clarity: 0.0
    contract_governance: 19.7
    contract_quality: 29.2
    developer_ergonomics: 15.5
    discoverability: 64.3
    operational_transparency: 18.4
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 24.7
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
    score: 10.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/speedtest-tracker/speedtest-tracker-2026-11-03T143621.png
security:
- kind: domain-security
  name: Speedtest Tracker Domain Security
  slug: speedtest-tracker-domain-security
  summary_line: TLSv1.3 · HSTS
slug: speedtest-tracker
tags:
- Company
- Self-Hosted
- Monitoring
- Speed Test
- Docker
- Open Source
website: https://docs.speedtest-tracker.dev/
---
