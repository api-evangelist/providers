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
    error_semantics: documented
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
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 5.4
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Open Source software to talk to Hoymiles solar inverters.
  name: OpenDTU API
  slug: opendtu-api
artifact_total: 5
common:
- group: design
  href: https://artifacts.apis.io/opendtu/rules/opendtu-rules.yml
  title: ''
  type: Spectral
  url: rules/opendtu-rules.yml
- group: design
  href: https://artifacts.apis.io/opendtu/vocabulary/opendtu-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/opendtu-vocabulary.yml
- group: auth
  href: https://artifacts.apis.io/opendtu/authentication/opendtu-authentication.yml
  title: ''
  type: Authentication
  url: authentication/opendtu-authentication.yml
- group: design
  href: https://artifacts.apis.io/opendtu/lifecycle/opendtu-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/opendtu-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/opendtu/errors/opendtu-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/opendtu-problem-types.yml
- group: design
  href: https://artifacts.apis.io/opendtu/conformance/opendtu-conformance.yml
  title: ''
  type: Conformance
  url: conformance/opendtu-conformance.yml
- group: other
  href: https://artifacts.apis.io/opendtu/hosts/opendtu-hosts.yml
  title: ''
  type: Hosts
  url: hosts/opendtu-hosts.yml
- group: other
  href: https://artifacts.apis.io/opendtu/vendors/opendtu-vendors.yml
  title: ''
  type: Vendors
  url: vendors/opendtu-vendors.yml
- group: start
  title: ''
  type: Sandbox
  url: https://www.opendtu.solar/firmware/configuration/console/
- group: start
  title: ''
  type: Login
  url: https://www.opendtu.solar/firmware/configuration/login/
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/tbnobody/OpenDTU-docs/raw/master/docs/index.md
- group: auth
  href: https://artifacts.apis.io/opendtu/security/opendtu-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/opendtu-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.opendtu.solar/
- group: docs
  title: ''
  type: APIReference
  url: https://www.opendtu.solar/firmware/web_api/
- group: operate
  title: ''
  type: Support
  url: https://www.opendtu.solar/#support
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tbnobody
coverage:
  checked: '2026-10-28'
  detail: Documentation exists but no OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contract was found.
  evidence:
  - status: 200
    url: https://www.opendtu.solar/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: OpenDTU provides open-source firmware for solar inverters, enabling local monitoring and control without reliance on cloud services. The project supports ESP32-based hardware, offers a web UI, MQTT integration, and a documented Web API for retrieving inverter data, configuring settings, and managing devices. It targets DIY solar enthusiasts and small installations seeking transparent, self-hosted energy monitoring solutions.
image: https://www.opendtu.solar/assets/images/logo.png
layout: provider
modified: '2026-10-28'
name: OpenDTU
nav: Providers
network: true
overview: 'OpenDTU publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network. Tagged areas include Solar, Firmware, Open Source, IoT, and Energy Monitoring.


  The OpenDTU catalog on APIs.io includes 1 Spectral governance ruleset.


  OpenDTU''s developer surface includes authentication, sandbox, documentation, API reference, support, and 11 more developer resources.'
random_paper: 23
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: OpenDTU API Rules
  rule_count: 9
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 1
  slug: opendtu-rules
scopes:
- name: Opendtu Scopes
  scope_count: 0
  slug: opendtu-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 16.7
  coverage:
    artifact_dirs: 21
    catalog_earned: 37.8
    catalog_earned_first_party: 0.0
    catalog_gap: 77.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.6
  facets:
    access_clarity: 6.6
    contract_governance: 22.0
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 57.1
    operational_transparency: 2.6
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 21.3
  provenance:
    conformance: derived
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 27.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/opendtu/opendtu-2026-11-03T140636.png
security:
- kind: authentication
  name: Opendtu Authentication
  slug: opendtu-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Opendtu Domain Security
  slug: opendtu-domain-security
  summary_line: TLSv1.3
slug: opendtu
tags:
- Solar
- Firmware
- Open Source
- IoT
- Energy Monitoring
website: https://www.opendtu.solar/
---
