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
  scored_at: '2026-09-16'
api_count: 0
artifact_total: 3
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aijieboya/refs/heads/main/security/aijieboya-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aijieboya-domain-security.yml
- group: company
  title: ''
  type: Website
  url: http://agilebio.com.cn/
- group: company
  title: ''
  type: About
  url: http://agilebio.com.cn/en/about-us
- group: company
  title: ''
  type: Blog
  url: http://agilebio.com.cn/en/news
- group: operate
  title: ''
  type: Support
  url: http://agilebio.com.cn/en/contact-us-2
- group: other
  title: ''
  type: SecondaryMarket
  url: https://equityzen.com/company/aijieboya
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/aijieboya/refs/heads/main/llms/aijieboya-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aijieboya-llms.txt
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/aijieboya/refs/heads/main/plans/aijieboya-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/aijieboya-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/aijieboya/refs/heads/main/rate-limits/aijieboya-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/aijieboya-rate-limits.yml
coverage:
  checked: '2026-09-14'
  detail: Aijieboya (Agilebio) sells physical laboratory hardware — chromatography columns, silica gel separation media and automated sample-pretreatment instruments — and its entire web presence is a WordPress product-catalog site at http://agilebio.com.cn/ with no developer, API, docs or integration section anywhere in its navigation; every OpenAPI, GraphQL, MCP, A2A and /.well-known/ path probed on that host returned 404, and even the CMS's own /wp-json/ REST route never answers.
  evidence:
  - status: 200
    url: http://agilebio.com.cn/en
  - status: 404
    url: http://agilebio.com.cn/openapi.json
  - status: 404
    url: http://agilebio.com.cn/.well-known/agent-card.json
  - status: 404
    url: http://agilebio.com.cn/.well-known/api-catalog
  - status: 0
    url: http://agilebio.com.cn/wp-json/
  reason: not-a-software-company
  state: none
created: '2026-09-14'
description: 'Suzhou Aijie Boya Technology Co., Ltd. (苏州艾捷博雅科技有限公司), trading internationally as Agilebio, is a Suzhou Industrial Park manufacturer of chromatography separation and purification technology founded in 2020 by Dr. Wang Qunjie. It develops high-purity spherical silica gel chromatographic media, magnetic solid-phase extraction (mSPE) consumables and precision fluid automation instruments — the AutoY32 automated sample pretreatment system, the SmartPurifier preparative MPLC series and the Bonnasil filler lines — for biopharmaceutical manufacturing, clinical mass spectrometry, peptide and nucleic-acid drug purification and food testing laboratories. It runs the Agilebio and Biosepur brands and an "Industrial Chromatography 4.0" platform. An instrument and consumables maker: it publishes no public API, SDK, developer portal or machine-readable contract.'
image: http://agilebio.com.cn/wp-content/uploads/2024/01/logo-0229.png
layout: provider
modified: '2026-09-14'
name: Aijieboya
nav: Providers
network: true
overview: 'Aijieboya is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Chromatography, Laboratory Instruments, Sample Preparation, and Separation and Purification.


  Aijieboya''s developer surface includes engineering blog, support, and 7 more developer resources.'
plans:
- name: Aijieboya Plans Pricing
  plan_count: 0
  slug: aijieboya-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 0
  name: Aijieboya Rate Limits
  slug: aijieboya-rate-limits
score:
  band: minimal
  composite: 5.5
  coverage:
    artifact_dirs: 5
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
    developer_ergonomics: 7.1
    discoverability: 57.4
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - china
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - greater-china
  previous_composite: 5.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.22.0
  scored_at: '2026-09-16'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Aijieboya Domain Security
  slug: aijieboya-domain-security
  summary_line: no transport/DNS hardening detected
slug: aijieboya
tags:
- Company
- Chromatography
- Laboratory Instruments
- Sample Preparation
- Separation and Purification
- Scientific Instruments
- Life Sciences
- Clinical Mass Spectrometry
- Biotechnology
- Manufacturing
- China
website: http://agilebio.com.cn/
---
