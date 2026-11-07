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
- group: agent
  href: https://artifacts.apis.io/autokz/llms/autokz-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/autokz-llms.txt
- group: other
  href: https://artifacts.apis.io/autokz/hosts/autokz-hosts.yml
  title: ''
  type: Hosts
  url: hosts/autokz-hosts.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.autokz.com/news/shenbuyufuzadicengzuantanjishuzhengchengweixingyehexinjingzhengli/duancezhinengyuxinxingtongxinjishuqudongchanpingexin.html
- group: auth
  href: https://artifacts.apis.io/autokz/security/autokz-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/autokz-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.autokz.com
coverage:
  checked: 2026-09-26
  detail: No OpenAPI or other machine-readable contract found at standard locations on api.autokz.com.
  evidence:
  - status: 0
    url: https://api.autokz.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-26'
description: Autokz, operating as Aoto Technology Co., Ltd., is a heavy‑machinery enterprise based in Kazakhstan that designs, manufactures, and services drilling equipment for water‑well, geological exploration, and engineering borehole applications. The company offers a broad product line including multi‑functional top‑drive drilling rigs, crawler‑mounted rigs, wireline coring rigs, and specialized drilling solutions for mining, energy, water‑conservation and municipal engineering projects worldwide.
layout: provider
modified: '2026-09-26'
name: Autokz
nav: Providers
network: true
overview: Autokz is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Heavy Machinery, Drilling Equipment, Kazakhstan, Industrial Engineering, and Water Well.
random_paper: 22
score:
  band: minimal
  composite: 3.9
  coverage:
    artifact_dirs: 7
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.1
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 52.7
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - kazakhstan
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 4.0
  provenance:
    mcp: unknown
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
screenshot: https://apis.io/screenshots/autokz/autokz-2026-10-11T100932.png
security:
- kind: domain-security
  name: Autokz Domain Security
  slug: autokz-domain-security
  summary_line: TLSv1.3 · HSTS
slug: autokz
tags:
- Heavy Machinery
- Drilling Equipment
- Kazakhstan
- Industrial Engineering
- Water Well
website: https://www.autokz.com
---
