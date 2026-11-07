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
  href: https://artifacts.apis.io/incarey/hosts/incarey-hosts.yml
  title: ''
  type: Hosts
  url: hosts/incarey-hosts.yml
- group: auth
  href: https://artifacts.apis.io/incarey/security/incarey-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/incarey-domain-security.yml
- group: company
  title: ''
  type: Website
  url: http://www.incarey.cn/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: http://www.incarey.cn/
  reason: no-developer-program
  state: none
created: '2026-10-22'
description: InCarey, officially Zhejiang YunKai YaMei Medical Technology Co., Ltd., is a Chinese digital health company founded in November 2011. It operates an integrated internet-based multi-specialty medical service platform, offering telemedicine, pharmaceutical services, and innovative payment solutions for chronic and high-value disease patients. With subsidiaries across several provinces and over 300 employees, InCarey serves more than 4 million patients, connecting top-tier hospitals, doctors, and pharmacists through its online and offline platforms to improve disease management and patient outcomes.
image: http://www.incarey.cn/static/img/logoh.png?v=1.4
layout: provider
modified: '2026-10-22'
name: InCarey
nav: Providers
network: true
overview: InCarey is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Health, Digital Health, Telehealth, and China.
random_paper: 3
score:
  band: minimal
  composite: 3.7
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.2
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - china
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - greater-china
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 3.7
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 4.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/incarey/incarey-2026-11-03T133730.png
security:
- kind: domain-security
  name: Incarey Domain Security
  slug: incarey-domain-security
  summary_line: no transport/DNS hardening detected
slug: incarey
tags:
- Company
- Health
- Digital Health
- Telehealth
- China
website: http://www.incarey.cn/
---
