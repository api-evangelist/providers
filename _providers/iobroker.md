---
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
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 5.4
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 5
common:
- group: other
  href: https://artifacts.apis.io/iobroker/hosts/iobroker-hosts.yml
  title: ''
  type: Hosts
  url: hosts/iobroker-hosts.yml
- group: build
  href: https://artifacts.apis.io/iobroker/packages/iobroker-packages.yml
  title: ''
  type: SDKs
  url: packages/iobroker-packages.yml
- group: build
  href: https://artifacts.apis.io/iobroker/packages/iobroker-packages.yml
  title: ''
  type: Packages
  url: packages/iobroker-packages.yml
- group: auth
  href: https://artifacts.apis.io/iobroker/security/iobroker-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/iobroker-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://iobroker.net/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://iobroker.net/
  reason: no-developer-program
  state: none
created: '2026-10-28'
description: ioBroker is an open-source integration platform for the Internet of Things, allowing users to connect and automate a wide variety of smart home devices, services, and protocols. It provides a modular, plugin‑based architecture where adapters enable communication with devices such as lights, thermostats, sensors, and cloud services. The platform can be self‑hosted on a server, Raspberry Pi, or Docker, offering a flexible, community‑driven solution for home automation enthusiasts and developers.
json_schemas:
- name: PostV1CommandSendtoRequest
  property_count: 3
  slug: iobroker-post-v1-command-sendto-request
jsonld:
- class_count: 1
  name: Iobroker Context
  property_count: 3
  slug: iobroker-context
layout: provider
modified: '2026-10-28'
name: ioBroker (self-hosted)
nav: Providers
network: true
overview: 'ioBroker (self-hosted) is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, IoT, HomeAutomation, OpenSource, and IntegrationPlatform.


  The ioBroker (self-hosted) catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.'
random_paper: 21
rate_limits:
- limit_count: 0
  name: Iobroker Rate Limits
  slug: iobroker-rate-limits
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: ioBroker (self-hosted) API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: iobroker-rules
score:
  band: minimal
  composite: 9.1
  coverage:
    artifact_dirs: 17
    catalog_earned: 34.5
    catalog_earned_first_party: 0.0
    catalog_gap: 80.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 18.2
    contract_quality: 6.7
    developer_ergonomics: 7.1
    discoverability: 44.6
    operational_transparency: 0.0
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 2
      marker_coverage: 100.0
      total: 2
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Iobroker Domain Security
  slug: iobroker-domain-security
  summary_line: TLSv1.2 · DMARC
slug: iobroker
tags:
- Company
- IoT
- HomeAutomation
- OpenSource
- IntegrationPlatform
- SelfHosted
website: https://iobroker.net/
---
