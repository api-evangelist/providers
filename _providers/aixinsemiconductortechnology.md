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
  scored_at: '2026-09-25'
api_count: 0
artifact_total: 1
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aixinsemiconductortechnology/refs/heads/main/security/aixinsemiconductortechnology-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aixinsemiconductortechnology-domain-security.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/aixinsemiconductortechnology/refs/heads/main/packages/aixinsemiconductortechnology-packages.yml
  title: ''
  type: SDKs
  url: packages/aixinsemiconductortechnology-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/aixinsemiconductortechnology/refs/heads/main/packages/aixinsemiconductortechnology-packages.yml
  title: ''
  type: Packages
  url: packages/aixinsemiconductortechnology-packages.yml
- group: company
  title: ''
  type: Newsroom
  url: https://axera-tech.com/zh-hans/news
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AXERA-TECH
- group: company
  title: ''
  type: Website
  url: https://axera-tech.com
coverage:
  checked: 2026-09-22
  detail: No public developer program or API documentation is available on the company's website.
  evidence:
  - status: 200
    url: https://axera-tech.com
  reason: no-developer-program
  state: none
created: '2026-09-22'
description: Axera Semiconductor Co., Ltd. (Aixin Semiconductor Technology) is a global leader in AI inference SoC solutions, delivering high‑performance perception and computing platforms for on‑device computing, edge AI inference, and smart vehicles. Listed on the Hong Kong Stock Exchange in February 2026, the company focuses on advanced edge and terminal‑side AI technologies, serving industries such as smart vehicles, vision, and edge AI chips.
layout: provider
modified: '2026-09-22'
name: Aixinsemiconductortechnology
nav: Providers
network: true
overview: Aixinsemiconductortechnology is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Semiconductors, Artificial Intelligence, Edge Computing, and Smart Vehicles.
random_paper: 14
score:
  band: minimal
  composite: 5.2
  coverage:
    artifact_dirs: 6
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.5
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 46.4
    operational_transparency: 5.3
  previous_composite: 6.7
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.5
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Aixinsemiconductortechnology Domain Security
  slug: aixinsemiconductortechnology-domain-security
  summary_line: TLSv1.3 · HSTS
slug: aixinsemiconductortechnology
tags:
- Company
- Semiconductors
- Artificial Intelligence
- Edge Computing
- Smart Vehicles
website: https://axera-tech.com
---
