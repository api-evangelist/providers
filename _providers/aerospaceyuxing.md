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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 2.5
  scored_at: '2026-09-12'
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://www.emposat.com/
- group: operate
  title: ''
  type: Support
  url: https://www.emposat.com/contact
- group: company
  title: ''
  type: Blog
  url: https://www.emposat.com/news/list
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Emposat
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/emposat/
- group: company
  title: ''
  type: Crunchbase
  url: https://www.crunchbase.com/organization/aerospace-yuxing
- group: other
  title: ''
  type: SecondaryMarket
  url: https://equityzen.com/company/aerospaceyuxing
- group: auth
  title: ''
  type: DomainSecurity
  url: security/aerospaceyuxing-domain-security.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/aerospaceyuxing-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/aerospaceyuxing-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/aerospaceyuxing-llms.txt
coverage:
  checked: '2026-09-12'
  detail: Aerospace Yuxing (Emposat) ships real software - TT&C operations, task-planning and ground-station management systems - but only as installed systems delivered inside a satellite-operations contract; its public site has no developer section, no API or SDK word anywhere across eight pages, and the only machine integration it advertises is a center-to-center link over ground-segment protocols (PDXP, CSP, KISS, CORTEX, AX.25) negotiated per customer.
  evidence:
  - status: 200
    url: https://www.emposat.com/
  - status: 404
    url: https://www.emposat.com/openapi.json
  - status: 404
    url: https://www.emposat.com/.well-known/api-catalog
  - status: 404
    url: https://www.emposat.com/.well-known/agent-card.json
  - status: 200
    url: https://www.emposat.com/service/manageSupport
  reason: no-developer-program
  state: none
created: '2026-09-12'
description: 'Aerospace Yuxing (Chinese: 航天驭星; English brand: Emposat Co., Ltd.; legally Beijing Aerospace Yuxing Technology Co., Ltd.) is a Beijing-headquartered commercial space-infrastructure operator founded in 2016 by a core team drawn from the China Academy of Space Technology and the wider China Aerospace Science and Technology Corporation system. It builds and operates the ground segment that commercial satellites depend on: a global network of more than 60 satellite ground stations across China, Kenya, South Africa, Malaysia, the Philippines, Thailand, the South Pacific and South America, plus the Ningxia Zhongwei remote-sensing calibration site. Its service catalog spans launch-vehicle and spacecraft telemetry, tracking and command (TT&C), long-term on-orbit operations management, payload data reception and processing, remote-sensing satellite calibration, space situational awareness and collision warning, debris mitigation, frequency coordination and launch licensing support,
  and aerospace engineering consulting. It also manufactures ground-system, communication and software-system products - multifunction baseband units, on-board transceivers and transponders, portable and integrated TT&C/data-reception ground stations, and TT&C operations software. The company has served over 370 satellites and rockets, employs roughly 300 people, and closed nearly CNY 2 billion across D, D+ and D++ rounds in 2026. Its customer-facing systems are delivered as installed software and a China-hosted service portal; center-to-center integration is offered over space ground-segment protocols (PDXP, CSP, KISS, CORTEX, AX.25) rather than a public web API. Aerospace Yuxing publishes no developer portal, no public API documentation, no SDK and no machine-readable API contract of any kind.'
image: https://www.emposat.com/img/icon.png
layout: provider
modified: '2026-09-12'
name: Aerospace Yuxing
nav: Providers
network: true
overview: 'Aerospace Yuxing is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Aerospace, Commercial Space, Satellite, and Ground Station.


  Aerospace Yuxing''s developer surface includes support, engineering blog, and 9 more developer resources.'
plans:
- name: Aerospaceyuxing Plans Pricing
  plan_count: 0
  slug: aerospaceyuxing-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 0
  name: Aerospaceyuxing Rate Limits
  slug: aerospaceyuxing-rate-limits
score:
  band: minimal
  composite: 7.8
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    operational_transparency: 5.3
  provenance:
    conformance: first-party
  schema_version: 0.22.0
  scored_at: '2026-09-12'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Aerospaceyuxing Domain Security
  slug: aerospaceyuxing-domain-security
  summary_line: TLSv1.2
slug: aerospaceyuxing
tags:
- Company
- Aerospace
- Commercial Space
- Satellite
- Ground Station
- Telemetry Tracking And Command
- Satellite Operations
- Space Situational Awareness
- Remote Sensing
- Space Infrastructure
- China
website: https://www.emposat.com/
---
