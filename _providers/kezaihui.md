---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kezaihui-domain-security.yml
- group: company
  title: ''
  type: Website
  url: http://www.kezaihui.com/
created: '2026-07-17'
description: Kezaihui (再惠 / Zaihuihui (Shanghai) Network Technology Co., Ltd.) is a Shanghai-based Chinese SaaS platform for local-life-service commerce, providing offline merchants — primarily mid-tier restaurants plus entertainment, beauty, and hospitality businesses — with one-stop store-opening and digital-operations tooling. Founded around 2012, the company offers private-domain member and community management, trading-platform shop diagnostics and automated strategy recommendations, content-creator (influencer) marketing, multi-channel precision ad delivery, and the Hui Shenghuo (惠生活) rights-aggregation platform, helping merchants operate across Meituan, Douyin, Xiaohongshu, and Taobao. It reports serving hundreds of thousands of merchants across dozens of Chinese cities with more than 1,000 employees. Surfaced as a portfolio company of DCM Ventures and added to the API Evangelist network; no public developer program or API surface was found during enrichment.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/kezaihui.png
layout: provider
modified: '2026-07-19'
name: Kezaihui
nav: Providers
network: true
overview: Kezaihui is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Enterprise, Software-as-a-Service, Local Commerce, and China.
random_paper: 18
score:
  band: minimal
  composite: 1.5
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
  previous_composite: 1.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 9.4
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kezaihui/refs/heads/main/screenshots/kezaihui-2026-07-25T223708.png
security:
- kind: domain-security
  name: Kezaihui Domain Security
  slug: kezaihui-domain-security
  summary_line: TLSv1.2 · DNSSEC
slug: kezaihui
tags:
- Company
- Enterprise
- Software-as-a-Service
- Local Commerce
- China
- Restaurant Technology
- Merchant Marketing
website: http://www.kezaihui.com/
---
