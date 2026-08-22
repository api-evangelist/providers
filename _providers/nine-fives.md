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
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 40.7
  scored_at: '2026-08-19'
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
artifact_total: 14
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Nine Fives Programmable REST Attenuator API
  slug: open-nine-fives-attenuator-api
- collection_type: open
  name: Nine Fives Programmable REST Attenuator Firmware API
  slug: open-nine-fives-firmware-api
- collection_type: open
  name: Nine Fives Programmable REST Attenuator Network API
  slug: open-nine-fives-network-api
- collection_type: open
  name: Nine Fives Programmable REST Attenuator Switch API
  slug: open-nine-fives-switch-api
- collection_type: open
  name: Nine Fives Programmable REST Attenuator System API
  slug: open-nine-fives-system-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/nine-fives-attenuator-overlay.yaml
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


  Nine Fives'' developer surface includes documentation, API reference, getting-started guide, engineering blog, support, signup flow, authentication, and 14 more developer resources.'
random_paper: 4
score:
  band: developing
  composite: 40.1
  delta: -0.3
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 30.3
    contract_quality: 47.0
    developer_ergonomics: 58.9
    discoverability: 81.5
    governance: 30.3
    operational_transparency: 0.0
  previous_composite: 40.4
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: first-party
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/nine-fives/refs/heads/main/screenshots/nine-fives-2026-08-07T185318.png
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
