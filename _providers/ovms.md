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
    agent_skills: unknown
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
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 20.8
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: For some time now I’ve wanted to offer an HTTP API for OVMS. The existing car↔server and server↔app protocol is cool, but requires going through some hoops (perl, whatever) to handle the encryption an
  name: OVMS HTTP API
  slug: ovms-http-api
- baseURL: http://api.openvehicles.com:6868
  baseurl_source: declared
  description: 'Open Vehicle Monitoring System (self-hosted) API as documented publicly: 7 operations. Contract generated from the documentation by API Evangelist (2026-10-28); not the provider''s own document.'
  name: Open Vehicle Monitoring System (self-hosted) API
  slug: ovms-api
artifact_total: 6
common:
- group: design
  href: https://artifacts.apis.io/ovms/rules/ovms-rules.yml
  title: ''
  type: Spectral
  url: rules/ovms-rules.yml
- group: design
  href: https://artifacts.apis.io/ovms/vocabulary/ovms-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/ovms-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/ovms/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/ovms/conformance/ovms-conformance.yml
  title: ''
  type: Conformance
  url: conformance/ovms-conformance.yml
- group: other
  href: https://artifacts.apis.io/ovms/hosts/ovms-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ovms-hosts.yml
- group: other
  href: https://artifacts.apis.io/ovms/vendors/ovms-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ovms-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.openvehicles.com/
- group: start
  title: ''
  type: Login
  url: https://www.openvehicles.com/user/login
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.openvehicles.com/developers
- group: auth
  href: https://artifacts.apis.io/ovms/security/ovms-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ovms-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://openvehicles.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.openvehicles.com/
- group: operate
  title: ''
  type: Support
  url: https://www.openvehicles.com/forum
- group: commercial
  title: ''
  type: Pricing
  url: https://www.openvehicles.com/buy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/openvehicles
coverage:
  checked: '2026-10-28'
  detail: The OVMS HTTP API is documented in HTML pages but no OpenAPI or other machine‑readable spec is published.
  evidence:
  - status: 404
    url: https://api.openvehicles.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: Open Vehicle Monitoring System (OVMS) is an open‑source, self‑hosted telematics platform for electric and hybrid vehicles. It provides real‑time vehicle data, remote commands, and extensive support for many car models. Users can install the system on their own hardware, integrate with MQTT, and customize dashboards. The project is community‑driven, with documentation, source code, and hardware designs publicly available.
image: https://www.openvehicles.com/sites/default/files/OVMS_logo_57.png
layout: provider
modified: '2026-10-28'
name: Open Vehicle Monitoring System (self-hosted)
nav: Providers
network: true
overview: 'Open Vehicle Monitoring System (self-hosted) is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Telematics, Electric Vehicles, Open Source, and IoT.


  The Open Vehicle Monitoring System (self-hosted) catalog on APIs.io includes 1 Spectral governance ruleset.


  Open Vehicle Monitoring System (self-hosted)''s developer surface includes documentation, support, pricing, and 12 more developer resources.'
random_paper: 21
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: Open Vehicle Monitoring System (self-hosted) API Rules
  rule_count: 9
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 1
  slug: ovms-rules
scopes:
- name: Ovms Scopes
  scope_count: 0
  slug: ovms-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 19.2
  coverage:
    artifact_dirs: 25
    catalog_earned: 42.8
    catalog_earned_first_party: 0.0
    catalog_gap: 72.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.2
  facets:
    access_clarity: 11.8
    contract_governance: 22.0
    contract_quality: 9.9
    developer_ergonomics: 18.3
    discoverability: 66.1
    operational_transparency: 10.5
  previous_composite: 25.4
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/ovms/ovms-2026-11-03T140824.png
security:
- kind: authentication
  name: Ovms Authentication
  slug: ovms-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Ovms Domain Security
  slug: ovms-domain-security
  summary_line: TLSv1.3 · DMARC
slug: ovms
tags:
- Company
- Telematics
- Electric Vehicles
- Open Source
- IoT
- Automotive
website: https://openvehicles.com/
---
