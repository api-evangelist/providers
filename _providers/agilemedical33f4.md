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
  scored_at: '2026-09-17'
api_count: 0
artifact_total: 1
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/agilemedical33f4/refs/heads/main/security/agilemedical33f4-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agilemedical33f4-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.agibot.cn/
- group: operate
  title: ''
  type: Support
  url: https://www.agibot.cn/contact.html
- group: company
  title: ''
  type: Blog
  url: https://www.agibot.cn/mjdt.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.agibot.cn/privacy.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.agibot.cn/legal.html
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/agilemedical33f4/refs/heads/main/llms/agilemedical33f4-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agilemedical33f4-llms.txt
coverage:
  checked: '2026-09-12'
  detail: Agile Medical sells the AGIBOT laparoscopic surgical robot — NMPA Class III capital medical equipment installed in hospital operating rooms — and its entire web presence is a 20-page nginx marketing site (home, product, about, news, contact, privacy, legal) with no developer section, no GitHub organization, and no API host; every contract and discovery path probed returned 404.
  evidence:
  - status: 200
    url: https://www.agibot.cn/sitemap.xml
  - status: 404
    url: https://www.agibot.cn/openapi.json
  - status: 404
    url: https://www.agibot.cn/llms.txt
  - status: 404
    url: https://www.agibot.cn/.well-known/api-catalog
  - status: 404
    url: https://www.agibot.cn/.well-known/agent-card.json
  reason: not-a-software-company
  state: none
created: '2026-09-12'
description: Agile Medical — 敏捷医疗科技（苏州）有限公司, trading under the AGIBOT brand — is a Chinese surgical robotics manufacturer founded in September 2020 and headquartered in Suzhou, Jiangsu, with R&D offices in the Suzhou Industrial Park Dushu Lake innovation district and Shanghai Zhangjiang. Its flagship AGIBOT endoscopic (laparoscopic) surgical robot system pairs a surgeon console, an eight-degree-of-freedom patient-side platform and an imaging processing platform that ingests third-party ultrasound, CT and endoscopic sources. The system received NMPA Class III medical device approval in March 2025 and is in clinical use for minimally invasive urology, gynecology, general, hepatobiliary and thoracic procedures. The company closed a several-hundred-million-RMB Series B in October 2025. It sells regulated capital equipment to hospitals and publishes no public API, developer portal, SDK or machine-readable specification.
image: https://www.agibot.cn/statics/home/images/logo.png
layout: provider
modified: '2026-09-12'
name: Agile Medical
nav: Providers
network: true
overview: 'Agile Medical is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Surgical Robotics, Medical Devices, Robotics, and Healthcare.


  Agile Medical''s developer surface includes support, engineering blog, and 5 more developer resources.'
random_paper: 15
score:
  band: emerging
  composite: 11.2
  coverage:
    artifact_dirs: 5
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
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
  previous_composite: 11.2
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 17.5
  schema_version: 0.22.0
  scored_at: '2026-09-17'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Agilemedical33F4 Domain Security
  slug: agilemedical33f4-domain-security
  summary_line: TLSv1.3 · HSTS
slug: agilemedical33f4
tags:
- Company
- Surgical Robotics
- Medical Devices
- Robotics
- Healthcare
- Minimally Invasive Surgery
- Medical Imaging
- Artificial Intelligence
- China
website: https://www.agibot.cn/
---
