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
  scored_at: '2026-09-10'
api_count: 0
artifact_total: 0
common:
- group: company
  title: ''
  type: Website
  url: https://www.aernos.com/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/aernos-inc
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AerNos-Inc
coverage:
  checked: '2026-09-10'
  detail: 'AerNos sells nano gas-sensor hardware modules and never ran a developer program — the only API reference anywhere on its live or archived site is one marketing clause, "organizational access to data via the AerBand Data Cloud Auto API", with no portal, reference, base URL or spec behind it — and the question is now moot because the company''s entire web presence is dark: aernos.com still answers NS and Microsoft 365 MX but publishes no A record on the apex or www, and aerband.com resolves to an AWS address with TCP 80 and 443 both closed.'
  evidence:
  - status: 0
    url: https://www.aernos.com/
  - status: 0
    url: https://aernos.com/
  - status: 0
    url: https://aerband.com/
  - status: 200
    url: https://github.com/AerNos-Inc
  reason: no-developer-program
  state: none
created: '2026-09-10'
description: 'AerNos, Inc. is a San Diego, California nanotechnology company founded in 2016 by Sundip Doshi that develops application-specific nano gas sensor modules capable of detecting multiple harmful gases — carbon monoxide, ozone, formaldehyde, nitrogen oxides and other volatile organic compounds — at parts-per-billion concentrations. Its proprietary AerCNT / AerN2S technology combines multi-layer hybrid nanostructures, materials science, nanoengineering and predictive analytics into low-power sensor systems intended for plug-and-play integration into third-party smart products. Product lines announced between 2017 and 2021 include AerIoT (an IoT nano gas sensor module and development kit, a CES 2019 Innovation Award Honoree), AerBand (a wearable research unit), AerHome and AerCity (smart-home and smart-city air quality monitors) and SmartAer (a monitoring solution for commercial buildings, industrial sites and schools). Frost & Sullivan named AerNos its 2018 Global Gas Sensor Industry
  Entrepreneurial Company of the Year. AerNos is a hardware company that never operated a developer program: across its entire published and archived web surface the only mention of an API is a single marketing clause on the products page — "organizational access to data via the AerBand Data Cloud Auto API" — with no developer portal, API reference, base URL, authentication documentation or machine-readable specification of any kind, and its cloud offering was sold as a $12/year WooCommerce "Annual Subscription to Cloud Data Services" rather than as a metered developer product. Its GitHub organization contains only forks of third-party projects. As of September 2026 the company''s public web presence is dark — aernos.com serves nameserver and Microsoft 365 mail records but no address record, and aerband.com resolves to an AWS address with no listening web port.'
layout: provider
modified: '2026-09-10'
name: AerNos
nav: Providers
network: true
overview: AerNos is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Sensors, Internet of Things, Air Quality, and Nanotechnology.
random_paper: 20
score:
  band: minimal
  composite: 5.0
  coverage:
    artifact_dirs: 1
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 46.3
    governance: 0.0
    operational_transparency: 2.6
  schema_version: 0.20.0
  scored_at: '2026-09-10'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
slug: aernos-inc
tags:
- Company
- Sensors
- Internet of Things
- Air Quality
- Nanotechnology
- Environmental Monitoring
- Hardware
- Wearables
- Smart Home
- Smart Cities
website: https://www.aernos.com/
---
