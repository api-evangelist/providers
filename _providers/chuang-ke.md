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
api_count: 1
apis:
- description: API surface referenced on the company's site, but no machine‑readable contract was found.
  name: CHUANG KE API
  slug: chuang-ke-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/chuang-ke/hosts/chuang-ke-hosts.yml
  title: ''
  type: Hosts
  url: hosts/chuang-ke-hosts.yml
- group: auth
  href: https://artifacts.apis.io/chuang-ke/security/chuang-ke-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/chuang-ke-domain-security.yml
- group: company
  title: ''
  type: Website
  url: http://www.ke-chuang.com/
coverage:
  checked: '2026-10-08'
  detail: Company site returns a JavaScript shell with no machine‑readable API documentation.
  evidence:
  - status: 200
    url: http://www.ke-chuang.com/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-08'
description: CHUANG KE (Zhejiang Kechuang Advanced Materials Technology Co., Ltd.) is a Chinese high‑tech company founded in 2010 that specializes in the research, development and manufacturing of silver nanowire materials and related advanced materials. It operates R&D centers in the United States and Hangzhou, holds multiple Chinese and US patents, and serves global customers including universities and technology firms. The company focuses on innovative nanomaterial solutions for electronics, optics, and biomedical applications.
layout: provider
modified: '2026-10-08'
name: CHUANG KE
nav: Providers
network: true
overview: CHUANG KE is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Materials, Nanotechnology, Manufacturing, and China.
random_paper: 19
score:
  band: minimal
  composite: 4.0
  coverage:
    artifact_dirs: 5
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 53.6
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - china
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - greater-china
  previous_composite: 4.0
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/chuang-ke/chuang-ke-2026-11-03T124126.png
security:
- kind: domain-security
  name: Chuang Ke Domain Security
  slug: chuang-ke-domain-security
  summary_line: DMARC
slug: chuang-ke
tags:
- Company
- Materials
- Nanotechnology
- Manufacturing
- China
website: http://www.ke-chuang.com/
---
