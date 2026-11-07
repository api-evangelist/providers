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
- description: API reference for Delovabiotech services
  name: Delovabiotech API
  slug: delovabiotech-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/delovabiotech/hosts/delovabiotech-hosts.yml
  title: ''
  type: Hosts
  url: hosts/delovabiotech-hosts.yml
- group: auth
  href: https://artifacts.apis.io/delovabiotech/security/delovabiotech-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/delovabiotech-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://delovabio.com
- group: docs
  title: ''
  type: Documentation
  url: https://delovabio.com/about/about.aspx
- group: docs
  title: ''
  type: APIReference
  url: https://delovabio.com/pro/pro.aspx
- group: start
  title: ''
  type: GettingStarted
  url: https://delovabio.com/recruitment/recruitment.aspx
- group: company
  title: ''
  type: Blog
  url: https://delovabio.com/news/news.aspx
- group: company
  title: ''
  type: InvestorRelations
  url: https://delovabio.com/investor/investor.aspx
coverage:
  checked: '2026-10-22'
  detail: The provider's documentation site is a JavaScript‑rendered Next.js application, preventing machine‑readable spec discovery.
  evidence:
  - status: 200
    url: https://delovabio.com
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-22'
description: Delovabiotech (南京清普生物科技有限公司) is a China‑based biotechnology company focused on developing non‑opioid, long‑acting pain management drugs. It aims to improve human health by innovating scientifically, offering products such as the patented long‑acting NSAID injection ‘普坦宁®’ and the newly approved oral formulation ‘美洛昔康注射液（II）’. The firm has a robust pipeline with over 10 projects, multiple IND filings, and has secured significant C‑round financing to accelerate clinical translation and commercialization.
layout: provider
modified: '2026-10-22'
name: Delovabiotech
nav: Providers
network: true
overview: 'Delovabiotech is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Pain Management, China, and Non-Opioid.


  Delovabiotech''s developer surface includes documentation, API reference, getting-started guide, engineering blog, and 4 more developer resources.'
random_paper: 1
score:
  band: minimal
  composite: 7.1
  coverage:
    artifact_dirs: 9
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.1
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 15.5
    discoverability: 53.6
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - china
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - greater-china
  previous_composite: 10.2
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
screenshot: https://apis.io/screenshots/delovabiotech/delovabiotech-2026-11-03T130507.png
security:
- kind: domain-security
  name: Delovabiotech Domain Security
  slug: delovabiotech-domain-security
  summary_line: TLSv1.2 · HSTS
slug: delovabiotech
tags:
- Company
- Biotechnology
- Pain Management
- China
- Non-Opioid
website: https://delovabio.com
---
