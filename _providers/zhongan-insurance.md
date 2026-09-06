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
  url: security/zhongan-insurance-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.zhongan.com
- group: start
  title: ''
  type: Portal
  url: https://open.zhongan.com
created: '2026-07-17'
description: ZhongAn Online P&C Insurance Co., Ltd. is China's first online-only insurance company, founded in 2013 by Ant Financial, Tencent, and Ping An and listed on the Hong Kong Stock Exchange (6060) in 2017. Headquartered in Shanghai, ZhongAn sells digital insurance across health, consumer finance, auto, and lifestyle lines entirely through internet channels, and operates a partner "open platform" (open.zhongan.com) plus a technology arm, ZhongAn Technology (zhongan.io), that offers insurtech and cloud services. ZhongAn does not publish a self-serve public developer API program or OpenAPI documentation; integration is partner/ecosystem-driven. This profile was surfaced as a portfolio company of softbank-vision-fund and enriched by the API Evangelist pipeline.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/zhongan-insurance.png
layout: provider
modified: '2026-07-21'
name: ZhongAn Insurance
nav: Providers
network: true
overview: 'ZhongAn Insurance is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Insurance, Insurtech, and Digital Insurance.


  ZhongAn Insurance''s developer surface includes developer portal and 2 more developer resources.'
random_paper: 6
score:
  band: minimal
  composite: 4.2
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
    developer_ergonomics: 9.5
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
  previous_composite: 4.2
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 9.1
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/zhongan-insurance/refs/heads/main/screenshots/zhongan-insurance-2026-09-02T171738.png
security:
- kind: domain-security
  name: Zhongan Insurance Domain Security
  slug: zhongan-insurance-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: zhongan-insurance
tags:
- Company
- Fintech
- Insurance
- Insurtech
- Digital Insurance
- China
website: https://www.zhongan.com
---
