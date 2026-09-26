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
artifact_total: 0
coverage:
  checked: '2026-09-06'
  detail: ActEvolve/VARK shut its VR platform down on 4 March 2024 and was sold outright in March 2025; vark.co.jp, corp.vark.co.jp and actevolve.com are all still registered to the company but publish no A/AAAA/CNAME record, so curl exits 6 ("could not resolve host") before any HTTP request can be made, and 1,812 archived URLs from when the sites were live contain no /api, /developers or specification path of any kind.
  evidence:
  - status: 0
    url: https://vark.co.jp/
  - status: 0
    url: https://corp.vark.co.jp/company
  - status: 0
    url: https://actevolve.com/
  - status: 404
    url: https://play.google.com/store/apps/details?id=jp.actevolve.vrpf_sp
  - status: 404
    url: https://pypi.org/pypi/actevolve/json
  - status: 200
    url: https://registry.npmjs.org/-/v1/search?text=actevolve
  - status: 200
    url: https://equityzen.com/company/actevolve/
  reason: defunct
  state: none
created: '2026-09-06'
description: 'ActEvolve Inc. (株式会社ActEvolve) was a Tokyo virtual-reality entertainment company incorporated on 9 August 2017 by Takuya Kato, a former Capcom game developer, together with other ex-game-industry engineers. In November 2018 it launched VARK, a VR live platform on which VTuber and virtual-artist performances — most visibly the long-running "Cinderella switch" series with hololive — were staged as ticketed, seat-based concerts for Meta Quest, Android and iOS, paid for with in-app VARK Coin. The company took strategic investment from KLab Inc. in August 2019, renamed itself VARK Inc. (株式会社VARK) on 1 May 2020 alongside a roughly ¥200M round from ANRI, raised a further ¥600M in May 2021, and diversified into the VARK SHORTS 3D animation tool and the STAR BLOOM liver-management agency, producing metaverse events for ANYCOLOR, Avex, KADOKAWA, COVER, Dwango, Shochiku and Meta. VARK was a consumer entertainment app rather than a platform business: it never operated a developer program,
  and no public API, SDK, webhook catalogue or machine-readable specification (OpenAPI, AsyncAPI, GraphQL SDL, MCP manifest, agent card) was published on any of its hosts at any point — 1,812 archived URLs across vark.co.jp and its subdomains contain no /api, /developers, /docs, /openapi or /graphql path of any kind. The VARK metaverse service shut down on 4 March 2024 with same-day notice, refunding unused VARK Coin until 5 May 2024 under Japan''s Payment Services Act; the free tier of VARK SHORTS ended on 30 September 2024; and in March 2025 the entire company was sold in an all-share transaction whose acquirer and terms were kept confidential, with founder Takuya Kato stepping down as representative director. This profile is retained as a historical record — there is no API surface to enrich.'
image: https://web.archive.org/web/20250209054433id_/https://corp.vark.co.jp/wp-content/themes/vark/assets/images/common/logo.svg
layout: provider
modified: '2026-09-06'
name: ActEvolve
nav: Providers
network: true
overview: ActEvolve is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Defunct, Acquired, Virtual Reality, and Metaverse.
random_paper: 1
score:
  band: minimal
  composite: 0.0
  coverage:
    artifact_dirs: 1
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 0.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - japan
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - japan-korea
  lifecycle: defunct
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 0.0
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
slug: actevolve
tags:
- Company
- Defunct
- Acquired
- Virtual Reality
- Metaverse
- Entertainment
- Live Events
- VTuber
- Consumer
- Japan
---
