---
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/500nettechnologycoltd-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.500net.com.tw/
- group: operate
  title: ''
  type: Support
  url: https://www.500net.com.tw/tw/Contact_Us.html
- group: company
  title: ''
  type: Newsroom
  url: https://www.500net.com.tw/tw/News_Center.html
- group: company
  title: ''
  type: About
  url: https://www.500net.com.tw/tw/About500Net.html
- group: company
  title: ''
  type: InvestorRelations
  url: https://www.500net.com.tw/tw/Financials.html
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/500nettechnologycoltd-llms.txt
coverage:
  checked: '2026-09-05'
  detail: 500net is a Taipei project-delivery systems integrator whose corporate site has no developer, docs or API section at all — the only integration language it publishes is device-level (RS-485/Modbus, wired/wireless/4G-5G controller integration), and every REST, GraphQL, MCP, agent-card and /.well-known discovery path returned a hard 404 from the origin's own error handler on both www.500net.com.tw and the legacy www.500-home.com.
  evidence:
  - status: 200
    url: https://www.500net.com.tw/tw/index.html
  - status: 404
    url: https://www.500net.com.tw/openapi.json
  - status: 404
    url: https://www.500net.com.tw/.well-known/agent-card.json
  - status: 404
    url: https://www.500net.com.tw/llms.txt
  - status: 404
    url: https://www.500-home.com/.well-known/security.txt
  reason: no-developer-program
  state: none
created: '2026-09-05'
description: 500net Technology Co., Ltd. (五百戶科技股份有限公司) is a Taipei-based systems integrator, founded in 2004, that combines telecommunications integration, electromechanical engineering, hardware design and custom software development into smart-building, smart-factory, smart-parking and AI+IoT platforms for enterprise clients. Its published solution set covers BA central-monitoring systems, smart property-management and parking operations, the 500net-EMS energy-management platform, carbon-footprint / ESG inventory reporting, digital twins, AMR robotics and AI/AOI inspection, integrated across heterogeneous controllers over RS-485/Modbus, wired, wireless and 4G/5G links. Work is delivered as project-based system integration for named enterprise customers; the company publishes a corporate site and an investor section but no public developer program, API reference, SDK or machine-readable contract.
image: https://www.500net.com.tw/tw/Image/logo.png
layout: provider
modified: '2026-09-05'
name: 500net Technology Co., Ltd.
nav: Providers
network: true
overview: '500net Technology Co., Ltd. is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Systems Integration, Smart Buildings, Smart Factory, and Internet of Things.


  500net Technology Co., Ltd.''s developer surface includes support and 6 more developer resources.'
random_paper: 15
score:
  band: minimal
  composite: 5.0
  coverage:
    artifact_dirs: 3
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 8.1
  schema_version: 0.18.3
  scored_at: '2026-09-05'
security:
- kind: domain-security
  name: 500Nettechnologycoltd Domain Security
  slug: 500nettechnologycoltd-domain-security
  summary_line: TLSv1.3
slug: 500nettechnologycoltd
tags:
- Company
- Systems Integration
- Smart Buildings
- Smart Factory
- Internet of Things
- Artificial Intelligence
- Energy Management
- Building Automation
- Smart Parking
- ESG
- Taiwan
website: https://www.500net.com.tw/
---
