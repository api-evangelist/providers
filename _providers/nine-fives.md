---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_skills: true
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.1
  score: 54.8
  scored_at: '2026-07-27'
api_count: 5
apis:
- description: Attenuation setpoint control
  name: Nine Fives Attenuator API
  slug: nine-fives-attenuator-api
- description: Firmware status and dual-slot (A/B) updates
  name: Nine Fives Firmware API
  slug: nine-fives-firmware-api
- description: Ethernet and USB-C interface configuration
  name: Nine Fives Network API
  slug: nine-fives-network-api
- description: SPDT switch state control
  name: Nine Fives Switch API
  slug: nine-fives-switch-api
- description: Device status and reboot
  name: Nine Fives System API
  slug: nine-fives-system-api
artifact_total: 8
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nine-fives-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://ninefives.com/pages/documentation
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ninefives.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.ninefives.com/attenuator/rest-api/overview/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.ninefives.com/attenuator/getting-started/
- group: company
  title: ''
  type: Blog
  url: https://blog.ninefives.com/
- group: operate
  title: ''
  type: Support
  url: https://ninefives.com/pages/contact
- group: start
  title: ''
  type: SignUp
  url: https://ninefives.com/account/login
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ninefives.com/policies/privacy-policy
- group: company
  title: ''
  type: Website
  url: https://ninefives.com
- group: auth
  title: ''
  type: Authentication
  url: authentication/nine-fives-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/nine-fives-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/nine-fives-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/nine-fives-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/nine-fives-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/nine-fives-data-model.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/nine-fives-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/nine-fives-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/nine-fives-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: 'Nine Fives builds modern, simple-to-use RF (radio frequency) test equipment for next-generation spacecraft, drones, and cellphones. Founded in 2025 by Andrew Kurtz and Noah Levy — RF hardware engineers who spent a decade at SpaceX designing radios and test systems for Falcon 9, Dragon, and Starship — the Y Combinator-backed company sells programmable, network-connected instruments: the POE-ATTEN-6G programmable attenuator and the POE-SWITCH-6G programmable SPDT switch, powered over USB-C or Power over Ethernet. Each instrument is automation-first: it serves a JSON REST API and a SCPI command interface (raw TCP and HiSLIP/IVI-6.1) directly on the device, plus a browser Web UI and touchscreen, with no drivers to install — control it with a plain curl command. The NineVue platform adds version-controlled test-rack configuration and an LLM skill that turns a rack drawing into functional test-automation code.'
image: https://ninefives.com/cdn/shop/files/NineFivesLogo.svg?v=1775235707
layout: provider
mcp_servers:
- description: ''
  name: nine-fives-mcp.yml
  slug: nine-fives-mcpyml
modified: '2026-07-20'
name: Nine Fives
nav: Providers
network: true
overview: 'Nine Fives publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Attenuator API, Firmware API, Network API, and 2 more. Tagged areas include Company, RF Test Equipment, Test and Measurement, Hardware, and IoT.


  Nine Fives'' developer surface includes documentation, API reference, getting-started guide, engineering blog, support, signup flow, authentication, and 13 more developer resources.'
random_paper: 60
score:
  band: thin
  composite: 40.6
  delta: 0.0
  facets:
    commercial_clarity: 23.7
    contract_quality: 49.7
    developer_ergonomics: 67.4
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 40.6
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
security:
- kind: authentication
  name: Nine Fives Authentication
  slug: nine-fives-authentication
  summary_line: none · 0 schemes
- kind: domain-security
  name: Nine Fives Domain Security
  slug: nine-fives-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: nine-fives
tags:
- Company
- RF Test Equipment
- Test and Measurement
- Hardware
- IoT
- Instrumentation
- Automation
- Aerospace
- Attenuator
- RF Switch
- SCPI
website: https://ninefives.com
---
