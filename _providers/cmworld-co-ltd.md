---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/cmworld-co-ltd/hosts/cmworld-co-ltd-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cmworld-co-ltd-hosts.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.cmworld.co.kr/about/news
- group: auth
  href: https://artifacts.apis.io/cmworld-co-ltd/security/cmworld-co-ltd-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cmworld-co-ltd-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.cmworld.co.kr/
coverage:
  checked: '2026-10-26'
  detail: The provider's website offers no developer documentation or API reference pages.
  evidence:
  - status: 200
    url: https://www.cmworld.co.kr/
  reason: no-developer-program
  state: none
created: '2026-10-26'
description: CmWorld Co., Ltd. (주)씨엠월드 is a Korean technology company specializing in AI‑based 3D spatial information and digital twin technologies. It positions itself as a global leader in intelligent volumetric spatial data, offering solutions for smart cities, BIM, IoT, and autonomous flight. The company provides platforms for 3D GIS, digital twin creation, and related services, aiming to connect the world through advanced spatial data technologies.
image: https://www.cmworld.co.kr/resources/images/common/cmworld_logo_thumbnail.png
layout: provider
modified: '2026-10-26'
name: CmWorld Co., Ltd.
nav: Providers
network: true
overview: CmWorld Co., Ltd. is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Digital Twin, GIS, and Smart Cities.
random_paper: 16
score:
  band: minimal
  composite: 3.5
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.1
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 49.1
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - south-korea
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 3.6
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/cmworld-co-ltd/cmworld-co-ltd-2026-11-03T124635.png
security:
- kind: domain-security
  name: Cmworld Co Ltd Domain Security
  slug: cmworld-co-ltd-domain-security
  summary_line: TLSv1.3
slug: cmworld-co-ltd
tags:
- Company
- Artificial Intelligence
- Digital Twin
- GIS
- Smart Cities
website: https://www.cmworld.co.kr/
---
