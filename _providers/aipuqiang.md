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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 2.5
  scored_at: '2026-09-18'
api_count: 0
artifact_total: 3
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aipuqiang/refs/heads/main/security/aipuqiang-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aipuqiang-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aptr.com.cn/
- group: company
  title: ''
  type: About
  url: https://aptr.com.cn/About
- group: company
  title: ''
  type: Blog
  url: https://aptr.com.cn/News
- group: operate
  title: ''
  type: Contact
  url: https://aptr.com.cn/Contact
- group: company
  title: ''
  type: Careers
  url: https://aptr.com.cn/Job
- group: other
  title: ''
  type: CaseStudies
  url: https://aptr.com.cn/Cases
- group: other
  title: ''
  type: x-KeyLaboratory
  url: https://aptr.com.cn/Laboratory
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/aipuqiang/refs/heads/main/llms/aipuqiang-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aipuqiang-llms.txt
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/aipuqiang/refs/heads/main/plans/aipuqiang-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/aipuqiang-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/aipuqiang/refs/heads/main/rate-limits/aipuqiang-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/aipuqiang-rate-limits.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/aipuqiang/refs/heads/main/packages/aipuqiang-packages.yml
  title: ''
  type: Packages
  url: packages/aipuqiang-packages.yml
coverage:
  checked: '2026-09-14'
  detail: 'Aipuqiang (Shanghai APACTRON Particle Equipment) manufactures installed proton therapy accelerators for hospitals, so its product is a physical machine rather than software: aptr.com.cn carries company, product, case-study, news, careers and laboratory sections and no developer area at all, and every contract and discovery path probed on both aptr.com.cn and www.aptr.com.cn returned 404.'
  evidence:
  - status: 200
    url: https://aptr.com.cn/
  - status: 404
    url: https://aptr.com.cn/openapi.json
  - status: 404
    url: https://aptr.com.cn/swagger.json
  - status: 404
    url: https://aptr.com.cn/graphql
  - status: 404
    url: https://aptr.com.cn/llms.txt
  - status: 404
    url: https://aptr.com.cn/.well-known/agent-card.json
  - status: 404
    url: https://aptr.com.cn/.well-known/api-catalog
  - status: 404
    url: https://www.aptr.com.cn/.well-known/security.txt
  - status: 500
    url: https://aptr.com.cn/en/
  reason: not-a-software-company
  state: none
created: '2026-09-14'
description: 'Aipuqiang is the transliterated name of Shanghai APACTRON Particle Equipment Co., Ltd. (上海艾普强粒子设备有限公司), a Shanghai-based manufacturer of proton therapy systems for cancer treatment. Founded in June 2011 and controlled by Shanghai Alliance Investment Co., Ltd. under the Shanghai SASAC, the company was the industrialization partner for China''s first domestically developed proton therapy demonstration facility, which received NMPA innovative medical device registration in September 2022 and entered clinical service at the Tumor Proton Center of Ruijin Hospital in November 2023. Its product line covers the accelerator system (injector, synchrotron and high-energy beam transport) together with 180-degree and 360-degree rotating-gantry and horizontal fixed-beam treatment rooms. Aipuqiang is a capital medical-equipment manufacturer: it sells installed proton therapy systems to hospitals and publishes no public API, developer portal, SDK or machine-readable specification.'
image: https://aptr.com.cn/web/Nimg/logo.png
layout: provider
modified: '2026-09-14'
name: Aipuqiang
nav: Providers
network: true
overview: 'Aipuqiang is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Medical Devices, Healthcare, Proton Therapy, and Radiation Oncology.


  Aipuqiang''s developer surface includes engineering blog and 11 more developer resources.'
plans:
- name: Aipuqiang Plans Pricing
  plan_count: 0
  slug: aipuqiang-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 0
  name: Aipuqiang Rate Limits
  slug: aipuqiang-rate-limits
score:
  band: minimal
  composite: 3.8
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
    developer_ergonomics: 2.4
    discoverability: 50.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - china
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - greater-china
  previous_composite: 3.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.22.0
  scored_at: '2026-09-18'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Aipuqiang Domain Security
  slug: aipuqiang-domain-security
  summary_line: TLSv1.2 · HSTS
slug: aipuqiang
tags:
- Company
- Medical Devices
- Healthcare
- Proton Therapy
- Radiation Oncology
- Particle Accelerators
- Medical Equipment
- Oncology
- Manufacturing
- China
website: https://aptr.com.cn/
---
