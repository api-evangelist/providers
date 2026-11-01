---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: unknown
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
    openapi_examples: verified
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 23.7
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: 'TeslaLogger (self-hosted) API as documented publicly: 1 operations. Contract generated from the documentation by API Evangelist (2026-10-28); not the provider''s own document.'
  name: TeslaLogger (self-hosted) API
  slug: teslalogger-api
artifact_total: 7
common:
- group: design
  href: https://artifacts.apis.io/teslalogger/rules/teslalogger-rules.yml
  title: ''
  type: Spectral
  url: rules/teslalogger-rules.yml
- group: design
  href: https://artifacts.apis.io/teslalogger/json-ld/teslalogger-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/teslalogger-context.jsonld
- group: design
  href: https://artifacts.apis.io/teslalogger/vocabulary/teslalogger-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/teslalogger-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/teslalogger/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/teslalogger/data-model/teslalogger-data-model.yml
  title: ''
  type: DataModel
  url: data-model/teslalogger-data-model.yml
- group: auth
  href: https://artifacts.apis.io/teslalogger/authentication/teslalogger-authentication.yml
  title: ''
  type: Authentication
  url: authentication/teslalogger-authentication.yml
- group: design
  href: https://artifacts.apis.io/teslalogger/conformance/teslalogger-conformance.yml
  title: ''
  type: Conformance
  url: conformance/teslalogger-conformance.yml
- group: other
  href: https://artifacts.apis.io/teslalogger/hosts/teslalogger-hosts.yml
  title: ''
  type: Hosts
  url: hosts/teslalogger-hosts.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://teslalogger.de/docs/extras/changelog
- group: auth
  href: https://artifacts.apis.io/teslalogger/security/teslalogger-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/teslalogger-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://teslalogger.de/degradation.php
- group: docs
  title: ''
  type: Documentation
  url: https://teslalogger.de/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://teslalogger.de/docs/installation/raspberry-install
coverage:
  checked: '2026-10-28'
  detail: Documentation is provided as static HTML without a machine‑readable OpenAPI or other contract.
  evidence:
  - status: 200
    url: https://teslalogger.de/docs/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: TeslaLogger (self-hosted) provides a self‑hosted data logger for Tesla vehicles, enabling owners to collect and analyse battery, charging, and usage metrics. It runs on Raspberry Pi, Docker, Synology NAS and other platforms, offering a web interface and API to retrieve vehicle telemetry, battery degradation, charging sessions, and more. The solution supports integration with ScanMyTesla and offers detailed dashboards for monitoring range, consumption, and firmware updates.
image: https://teslalogger.de/degradation_M3.PNG
json_schemas:
- name: PostMcpRequest
  property_count: 3
  slug: teslalogger-post-mcp-request
- name: PostMcpResponse
  property_count: 3
  slug: teslalogger-post-mcp-response
jsonld:
- class_count: 2
  name: Teslalogger Context
  property_count: 6
  slug: teslalogger-context
layout: provider
modified: '2026-10-28'
name: TeslaLogger (self-hosted)
nav: Providers
network: true
overview: 'TeslaLogger (self-hosted) is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Automotive, DataLogging, OpenSource, and Tesla.


  The TeslaLogger (self-hosted) catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  TeslaLogger (self-hosted)''s developer surface includes authentication, changelog, documentation, getting-started guide, and 9 more developer resources.'
random_paper: 1
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: TeslaLogger (self-hosted) API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: teslalogger-rules
score:
  band: emerging
  composite: 23.5
  coverage:
    artifact_dirs: 16
    catalog_earned: 51.8
    catalog_earned_first_party: 0.0
    catalog_gap: 63.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 19.6
    developer_ergonomics: 39.8
    discoverability: 57.1
    operational_transparency: 15.8
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 2
      marker_coverage: 100.0
      total: 2
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Teslalogger Authentication
  slug: teslalogger-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Teslalogger Domain Security
  slug: teslalogger-domain-security
  summary_line: TLSv1.3 · DMARC
slug: teslalogger
tags:
- Company
- Automotive
- DataLogging
- OpenSource
- Tesla
website: https://teslalogger.de/degradation.php
---
