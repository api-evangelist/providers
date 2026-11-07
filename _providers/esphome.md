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
  band: human-only
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
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/esphome/hosts/esphome-hosts.yml
  title: ''
  type: Hosts
  url: hosts/esphome-hosts.yml
- group: other
  href: https://artifacts.apis.io/esphome/vendors/esphome-vendors.yml
  title: ''
  type: Vendors
  url: vendors/esphome-vendors.yml
- group: build
  href: https://artifacts.apis.io/esphome/packages/esphome-packages.yml
  title: ''
  type: SDKs
  url: packages/esphome-packages.yml
- group: build
  href: https://artifacts.apis.io/esphome/packages/esphome-packages.yml
  title: ''
  type: Packages
  url: packages/esphome-packages.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.esphome.io/
- group: operate
  title: ''
  type: ChangeLog
  url: https://esphome.io/changelog/
- group: docs
  title: ''
  type: Documentation
  url: https://api-docs.esphome.io/
- group: auth
  href: https://artifacts.apis.io/esphome/security/esphome-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/esphome-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://esphome.io/
- group: start
  title: ''
  type: GettingStarted
  url: https://esphome.io/install/getting-started/
- group: company
  title: ''
  type: Blog
  url: https://esphome.io/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/esphome
- group: operate
  title: ''
  type: Support
  url: https://esphome.io/chat
- group: commercial
  title: ''
  type: Pricing
  url: https://esphome.io/starter-kit/
coverage:
  checked: '2026-10-28'
  detail: The provider's documentation site https://api-docs.esphome.io returns no OpenAPI or other machine‑readable contract, only HTML pages.
  evidence:
  - status: 520
    url: https://api-docs.esphome.io/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: ESPHome is an open-source platform that simplifies building custom smart home devices using ESP8266/ESP32 microcontrollers. It provides a visual device builder, YAML configuration files, and seamless integration with Home Assistant, allowing users to create sensors, switches, lights, and more without extensive coding. The platform offers extensive component libraries, OTA updates, and local control, emphasizing privacy and flexibility for hobbyists and developers alike.
image: https://esphome.io/images/og.webp
layout: provider
modified: '2026-10-28'
name: ESPHome
nav: Providers
network: true
overview: 'ESPHome is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Smart Home, Home Automation, Microcontrollers, Open Source, and ESP32.


  ESPHome''s developer surface includes changelog, documentation, getting-started guide, engineering blog, support, pricing, and 8 more developer resources.'
random_paper: 9
score:
  band: emerging
  composite: 11.1
  coverage:
    artifact_dirs: 11
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.2
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 48.2
    operational_transparency: 10.5
  previous_composite: 17.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/esphome/esphome-2026-11-03T131620.png
security:
- kind: domain-security
  name: Esphome Domain Security
  slug: esphome-domain-security
  summary_line: TLSv1.3 · DMARC
slug: esphome
tags:
- Smart Home
- Home Automation
- Microcontrollers
- Open Source
- ESP32
- Home Assistant
website: https://esphome.io/
---
