---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: platform
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 7.9
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/switchbot/llms/switchbot-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/switchbot-llms.txt
- group: agent
  href: https://artifacts.apis.io/switchbot/mcp/switchbot-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/switchbot-mcp.yml
- group: auth
  href: https://artifacts.apis.io/switchbot/well-known/switchbot-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/switchbot-status-security.txt
- group: agent
  href: https://artifacts.apis.io/switchbot/well-known/switchbot-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/switchbot-well-known.yml
- group: other
  href: https://artifacts.apis.io/switchbot/hosts/switchbot-hosts.yml
  title: ''
  type: Hosts
  url: hosts/switchbot-hosts.yml
- group: other
  href: https://artifacts.apis.io/switchbot/vendors/switchbot-vendors.yml
  title: ''
  type: Vendors
  url: vendors/switchbot-vendors.yml
- group: build
  href: https://artifacts.apis.io/switchbot/packages/switchbot-packages.yml
  title: ''
  type: SDKs
  url: packages/switchbot-packages.yml
- group: build
  href: https://artifacts.apis.io/switchbot/packages/switchbot-packages.yml
  title: ''
  type: Packages
  url: packages/switchbot-packages.yml
- group: operate
  title: ''
  type: Support
  url: https://support.switch-bot.com/hc/en-us
- group: operate
  title: ''
  type: StatusPage
  url: https://status.switch-bot.com/
- group: auth
  href: https://artifacts.apis.io/switchbot/security/switchbot-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/switchbot-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://switch-bot.com/
created: '2026-10-28'
description: SwitchBot provides smart home automation products, including robotic switches, curtains, bots, and sensors, enabling users to control devices via Bluetooth, Wi‑Fi, and cloud APIs. Their platform offers a developer portal with RESTful APIs for device management, status monitoring, and integration with third‑party services, supporting OAuth2 and API keys for secure access.
image: https://cdn.shopify.com/s/files/1/0335/7333/9269/files/SwitchBot.png?v=1787307605
layout: provider
mcp_servers:
- description: Remote MCP server at www.switch-bot.com.
  name: SwitchBot MCP Server
  slug: switchbot-mcp-yml
modified: '2026-10-28'
name: SwitchBot
nav: Providers
network: true
overview: 'SwitchBot is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include SmartHome, IoT, Automation, Robotics, and ConsumerElectronics.


  SwitchBot''s developer surface includes support and 11 more developer resources.'
random_paper: 23
score:
  band: minimal
  composite: 9.2
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 48.3
    operational_transparency: 26.3
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Switchbot Domain Security
  slug: switchbot-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: switchbot
tags:
- SmartHome
- IoT
- Automation
- Robotics
- ConsumerElectronics
website: https://switch-bot.com/
---
