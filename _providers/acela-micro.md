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
  scored_at: '2026-09-07'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/acela-micro-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.acelamicro.com/en/
- group: company
  title: ''
  type: About
  url: https://www.acelamicro.com/en/index.php?c=category&id=6
coverage:
  checked: '2026-09-06'
  detail: Acela Micro is a Suzhou fabless chip designer whose product is silicon — ADC/DAC converters, clock chips and RF transceivers — so its entire Service & Support area distributes PDF product manuals and datasheets, with no developer portal, no API, no SDK and no software download of any kind on the site.
  evidence:
  - status: 200
    url: https://www.acelamicro.com/en/index.php?c=category&id=16
  - status: 200
    url: https://www.acelamicro.com/en/index.php?c=category&id=4
  - status: 404
    url: https://acelamicro.com/openapi.json
  - status: 404
    url: https://acelamicro.com/llms.txt
  - status: 404
    url: https://acelamicro.com/.well-known/agent-card.json
  - status: 404
    url: https://acelamicro.com/.well-known/api-catalog
  reason: not-a-software-company
  state: none
created: '2026-09-06'
description: Acela Micro (Suzhou Acela Microelectronics, founded 2013) is a Chinese fabless semiconductor company designing high-end signal chain integrated circuits — ultra-high-speed and high-precision analog-to-digital converters (ADC), digital-to-analog converters (DAC), high-speed clock and wideband signal conditioning chips, and RF agile transceivers — plus system-level validation platforms such as the AUV1302 wideband real-time validation board. Its parts target 5G base stations, optical communications, test and measurement instrumentation, high-speed data acquisition, broadband radar, security imaging and medical devices, and the company positions itself around the domestic localization of high-performance data converters. Headquartered in Suzhou Industrial Park with branches in Beijing, Chengdu, Wuhan and Shenzhen, it holds 90+ invention patents across 80+ product families. The company sells silicon, datasheets and reference hardware; it operates no developer program, publishes
  no public API, SDK or machine-readable contract, and its Service and Support area distributes product manuals as PDFs.
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-09-06'
name: Acela Micro
nav: Providers
network: true
overview: Acela Micro is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Semiconductors, Integrated Circuits, Analog to Digital Converters, and Digital to Analog Converters.
random_paper: 14
score:
  band: minimal
  composite: 5.0
  coverage:
    artifact_dirs: 2
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - china
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - greater-china
  previous_composite: 5.0
  schema_version: 0.20.0
  scored_at: '2026-09-07'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Acela Micro Domain Security
  slug: acela-micro-domain-security
  summary_line: TLSv1.2
slug: acela-micro
tags:
- Company
- Semiconductors
- Integrated Circuits
- Analog to Digital Converters
- Digital to Analog Converters
- RF Transceivers
- Signal Chain
- Electronic Components
- Hardware
- China
website: https://www.acelamicro.com/en/
---
