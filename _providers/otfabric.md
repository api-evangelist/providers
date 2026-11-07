---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  - sandbox
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 2.5
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Open-source, MIT-licensed pure-Go protocol libraries (Modbus, OPC UA, BACnet/IP, IEC 60870-5-104, IEC 61850, Siemens S7, OpenADR, OCPP, DNP3, IEEE 2030.5, EtherNet/IP, PROFINET, CANopen, CAN bus, KNX,
  name: OT Fabric Protocol Libraries and CLIs
  slug: otfabric-protocol-libraries
- description: A small self-hosted HTTP control API served by the OT Fabric modbus-simulator when started with --control (the docs example binds 127.0.0.1:5021), so a test suite can reset or reload the simulated dev
  name: Modbus Simulator Control API
  slug: modbus-simulator-control-api
artifact_total: 5
common:
- group: build
  href: https://artifacts.apis.io/otfabric/cli/otfabric-cli.yml
  title: ''
  type: CLI
  url: cli/otfabric-cli.yml
- group: operate
  href: https://artifacts.apis.io/otfabric/changelog/otfabric-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/otfabric-changelog.yml
- group: design
  href: https://artifacts.apis.io/otfabric/conventions/otfabric-conventions.yml
  title: ''
  type: Conventions
  url: conventions/otfabric-conventions.yml
- group: start
  href: https://artifacts.apis.io/otfabric/sandbox/otfabric-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/otfabric-sandbox.yml
- group: design
  href: https://artifacts.apis.io/otfabric/lifecycle/otfabric-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/otfabric-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/otfabric/conformance/otfabric-conformance.yml
  title: ''
  type: Conformance
  url: conformance/otfabric-conformance.yml
- group: agent
  href: https://artifacts.apis.io/otfabric/llms/otfabric-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/otfabric-llms.txt
- group: other
  href: https://artifacts.apis.io/otfabric/hosts/otfabric-hosts.yml
  title: ''
  type: Hosts
  url: hosts/otfabric-hosts.yml
- group: other
  href: https://artifacts.apis.io/otfabric/vendors/otfabric-vendors.yml
  title: ''
  type: Vendors
  url: vendors/otfabric-vendors.yml
- group: build
  href: https://artifacts.apis.io/otfabric/packages/otfabric-packages.yml
  title: ''
  type: SDKs
  url: packages/otfabric-packages.yml
- group: build
  href: https://artifacts.apis.io/otfabric/packages/otfabric-packages.yml
  title: ''
  type: Packages
  url: packages/otfabric-packages.yml
- group: auth
  href: https://artifacts.apis.io/otfabric/security/otfabric-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/otfabric-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://otfabric.io/
- group: docs
  title: ''
  type: Documentation
  url: https://otfabric.io/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://otfabric.io/docs/getting-started/
- group: company
  title: ''
  type: Blog
  url: https://otfabric.io/blog/
- group: other
  title: ''
  type: RSSFeed
  url: https://otfabric.io/blog/rss.xml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/otfabric
- group: operate
  title: ''
  type: Support
  url: https://otfabric.io/contact/
- group: company
  title: ''
  type: About
  url: https://otfabric.io/about/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/otfabric
created: '2026-11-03'
description: 'OT Fabric (otfabric.io) builds open-source, MIT-licensed, pure-Go protocol libraries, command-line tools and Dockerized interoperability test suites for industrial operational technology (OT): Modbus, OPC UA, BACnet/IP, IEC 60870-5-104, IEC 61850, Siemens S7, OpenADR, OCPP, DNP3, IEEE 2030.5, EtherNet/IP, PROFINET, CANopen on CAN bus and KNX, plus SunSpec Modbus and IEC 61850 information models and Sparkplug B over MQTT. Its stated goal is ''unified data for industrial operations'': breaking down OT data silos so industrial data is easy to discover, access and use across systems, sites and teams. It publishes libraries and CLIs rather than a hosted web API.'
image: https://otfabric.io/og-image.png
layout: provider
modified: '2026-11-03'
name: OT Fabric
nav: Providers
network: true
overview: 'OT Fabric is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Industrial IoT, Operational Technology, Open Source, and Protocol.


  OT Fabric''s developer surface includes CLI, changelog, sandbox, documentation, getting-started guide, engineering blog, support, and 14 more developer resources.'
plans:
- name: Otfabric Plans Pricing
  plan_count: 0
  slug: otfabric-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 0
  name: Otfabric Rate Limits
  slug: otfabric-rate-limits
score:
  band: emerging
  composite: 16.8
  coverage:
    artifact_dirs: 17
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 35.7
    discoverability: 57.1
    operational_transparency: 18.4
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Otfabric Domain Security
  slug: otfabric-domain-security
  summary_line: TLSv1.3 · DMARC
slug: otfabric
tags:
- Company
- Industrial IoT
- Operational Technology
- Open Source
- Protocol
- Modbus
- OPC UA
- Go
- CLI
- Interoperability Testing
website: https://otfabric.io/
---
