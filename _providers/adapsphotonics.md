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
  scored_at: '2026-09-06'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/adapsphotonics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.adapsphotonics.com/en/
- group: company
  title: ''
  type: About
  url: https://www.adapsphotonics.com/en/page-81691.html
- group: company
  title: ''
  type: Newsroom
  url: https://www.adapsphotonics.com/en/list-73732.html
- group: operate
  title: ''
  type: Contact
  url: https://yejlwg.aliwork.com/o/clue2?__page_lang=en_US
- group: other
  title: ''
  type: x-secondary-market
  url: https://equityzen.com/company/adapsphotonics
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/adapsphotonics-llms.txt
coverage:
  checked: '2026-09-06'
  detail: Adaps Photonics is a fabless SPAD/dToF depth-sensor chip designer selling silicon and camera modules to device makers; its entire public site is a five-item marketing CMS (Company / Products / Newsroom / About / Contact) with no developer, documentation, download or support section, and its only contact channel is an Alibaba Yida sales form.
  evidence:
  - status: 200
    url: https://www.adapsphotonics.com/en/
  - status: 404
    url: https://www.adapsphotonics.com/llms.txt
  - status: 404
    url: https://www.adapsphotonics.com/.well-known/api-catalog
  - status: 403
    url: https://www.adapsphotonics.com/openapi.json
  - status: 404
    url: https://api.github.com/orgs/adapsphotonics
  reason: not-a-software-company
  state: none
created: '2026-09-06'
description: Adaps Photonics (Shenzhen Adaps Photonics Technology Co., Ltd. / 灵明光子) is a fabless semiconductor company founded in May 2018 in the Nanshan district of Shenzhen, China, with R&D centers in Shanghai and Zhejiang. It designs single-photon avalanche diode (SPAD) based direct time-of-flight (dToF) 3D depth-sensing chips and modules — silicon photomultipliers (SiPM), 3D-stacked SPAD arrays hybrid-bonded to custom DSP dies, and all-in-one integrated dToF depth sensors — for smartphones, automotive LiDAR, AR/VR headsets, robotics, smart home and industrial IoT. The company sells silicon and sensor modules to device makers through a direct sales motion; it publishes no public API, SDK, developer portal or machine-readable interface contract.
image: https://www.adapsphotonics.com/home/c/5/ifzufa/resource/2023/03/14/641049b289661.png
layout: provider
modified: '2026-09-06'
name: Adaps Photonics
nav: Providers
network: true
overview: Adaps Photonics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Semiconductors, Sensors, Photonics, and LiDAR.
random_paper: 13
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
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: venue_as_website
    - owner: catalog
      reason: never_enriched
  schema_version: 0.19.0
  scored_at: '2026-09-06'
security:
- kind: domain-security
  name: Adapsphotonics Domain Security
  slug: adapsphotonics-domain-security
  summary_line: TLSv1.3
slug: adapsphotonics
tags:
- Company
- Semiconductors
- Sensors
- Photonics
- LiDAR
- 3D Sensing
- Chip Design
- Automotive
- Consumer Electronics
- Hardware
website: https://www.adapsphotonics.com/en/
---
