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
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-09-23'
api_count: 0
artifact_total: 1
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/airtouch/refs/heads/main/security/airtouch-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/airtouch-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://en.airtouching.com/
- group: company
  title: ''
  type: About
  url: https://en.airtouching.com/about.html
- group: operate
  title: ''
  type: Contact
  url: https://en.airtouching.com/contact.html
- group: company
  title: ''
  type: Newsroom
  url: https://en.airtouching.com/News.html
- group: company
  title: ''
  type: Careers
  url: https://en.airtouching.com/Join.html
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@%E9%9A%94%E7%A9%BA%E7%A7%91%E6%8A%80AIRTOUCH
- group: other
  title: ''
  type: SecondaryMarket
  url: https://equityzen.com/company/airtouch
coverage:
  checked: '2026-09-19'
  detail: AirTouch (Shanghai) is a fabless radar-sensor chip designer whose entire public surface is a product catalog, news feed and contact page on en.airtouching.com; there is no developer portal, SDK, GitHub organization or contract of any kind, every non-content path (openapi.json, /docs, /api, /graphql, /.well-known/*) returns the edge's 403 HTML shell, and no api./docs./ developer./mcp. subdomain resolves.
  evidence:
  - status: 200
    url: https://en.airtouching.com/
  - status: 403
    url: https://en.airtouching.com/openapi.json
  - status: 403
    url: https://en.airtouching.com/docs
  - status: 403
    url: https://en.airtouching.com/.well-known/agent-card.json
  - status: 404
    url: https://en.airtouching.com/llms.txt
  - status: 404
    url: https://en.airtouching.com/.well-known/security.txt
  - status: 404
    url: https://api.github.com/orgs/airtouching
  reason: not-a-software-company
  state: none
created: '2026-09-19'
description: AirTouch (Shanghai) Intelligent Technology Co., Ltd. (隔空科技) is a Shanghai-based fabless semiconductor company founded in November 2017 that designs microwave and millimeter-wave radar sensor chips — 5.8 GHz, 10.525 GHz, 24 GHz, 60 GHz and 77 GHz series, including SoC parts with an integrated 32-bit MCU and antenna-in-package (AiP) variants — for smart lighting, security, home appliances, smart home and automotive / two-wheeler ADAS. Backed by Intel Capital, Xiaomi, TCL Venture Capital and Fosun, with R&D centers in Ningbo, Guangzhou and Shenzhen. The company sells silicon, modules and reference designs and publishes no public API, SDK, developer portal or machine-readable contract.
layout: provider
modified: '2026-09-19'
name: Airtouch
nav: Providers
network: true
overview: 'Airtouch is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Semiconductors, Radar, Sensors, and Millimeter Wave.


  Airtouch''s developer surface includes YouTube channel and 7 more developer resources.'
random_paper: 5
score:
  band: minimal
  composite: 4.6
  coverage:
    artifact_dirs: 3
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 46.3
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - china
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - greater-china
  previous_composite: 4.6
  schema_version: 0.22.0
  scored_at: '2026-09-23'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Airtouch Domain Security
  slug: airtouch-domain-security
  summary_line: TLSv1.3
slug: airtouch
tags:
- Company
- Semiconductors
- Radar
- Sensors
- Millimeter Wave
- IoT
- Smart Home
- Automotive
- Hardware
- China
website: https://en.airtouching.com/
---
