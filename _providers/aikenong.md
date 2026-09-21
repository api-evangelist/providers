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
  scored_at: '2026-09-20'
api_count: 0
artifact_total: 3
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aikenong/refs/heads/main/security/aikenong-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aikenong-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.aikenong.com.cn/
- group: company
  title: ''
  type: Blog
  url: https://www.aikenong.com.cn/ican/newsList
- group: other
  title: ''
  type: SecondaryMarket
  url: https://equityzen.com/company/aikenong
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/aikenong/refs/heads/main/plans/aikenong-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/aikenong-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/aikenong/refs/heads/main/rate-limits/aikenong-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/aikenong-rate-limits.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/aikenong/refs/heads/main/llms/aikenong-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aikenong-llms.txt
coverage:
  checked: '2026-09-14'
  detail: Aikenong sells smart-agriculture SaaS, mobile apps and field hardware to growers and farming enterprises and runs no developer program at all — its marketing site has no developer, documentation or API section, the one real first-party API host (foreignapi4.aikenong.com.cn, the gateway hard-coded into the Aigengyun Enterprise web app) 404s every spec path, and api.aikenong.com.cn still serves the stock nginx default page installed in January 2019.
  evidence:
  - status: 200
    url: https://www.aikenong.com.cn/
  - status: 404
    url: https://foreignapi4.aikenong.com.cn/v3/api-docs
  - status: 404
    url: https://api.aikenong.com.cn/openapi.json
  - status: 404
    url: https://www.icanag.com/.well-known/apis.json
  - status: 404
    url: https://api.github.com/orgs/aikenong
  reason: no-developer-program
  state: none
created: '2026-09-14'
description: 'Aikenong (爱科农 / Beijing Aikenong Technology Co., Ltd., also trading internationally as ICAN) is a Chinese smart-agriculture company founded in 2016 in Chaoyang District, Beijing. It builds a proprietary plant-soil-atmosphere crop growth model and a data-driven agronomy platform (ICAN) that combines satellite and UAV remote sensing, weather and soil telemetry, and AI prediction into whole-season planting decision guidance for growers. Its product line spans the Aigengyun (爱耕耘) grower app and WeChat mini program, Aigengyun Enterprise and Business editions for farming enterprises and agri-input dealers, the AIGROW breeding information management system, a high-yield irrigation control system, and a catalogue of field hardware (weather stations, soil moisture stations, smart valves, fertigation controllers, greenhouse controllers, phenotyping cameras and inspection robots). The company reports service across roughly ten Chinese provinces and 30,000+ growers, and raised more than
  CNY 100 million in Series A/A+ rounds led by Source Code Capital, IDG Capital and GL Ventures. It is a SaaS and hardware vendor rather than an API vendor: no public developer program, API reference, SDK or machine-readable contract is published anywhere on its own domains as of this profile.'
image: https://www.aikenong.com.cn/resource/website/images/icon.png
layout: provider
modified: '2026-09-14'
name: Aikenong
nav: Providers
network: true
overview: 'Aikenong is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Agriculture, AgTech, Smart Agriculture, and Artificial Intelligence.


  Aikenong''s developer surface includes engineering blog and 6 more developer resources.'
plans:
- name: Aikenong Plans Pricing
  plan_count: 0
  slug: aikenong-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 0
  name: Aikenong Rate Limits
  slug: aikenong-rate-limits
score:
  band: minimal
  composite: 6.2
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
    discoverability: 57.4
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - china
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - greater-china
  previous_composite: 6.2
  schema_version: 0.22.0
  scored_at: '2026-09-20'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Aikenong Domain Security
  slug: aikenong-domain-security
  summary_line: TLSv1.3
slug: aikenong
tags:
- Company
- Agriculture
- AgTech
- Smart Agriculture
- Artificial Intelligence
- Remote Sensing
- IoT
- Data & Analytics
- China
website: https://www.aikenong.com.cn/
---
