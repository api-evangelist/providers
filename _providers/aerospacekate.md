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
  scored_at: '2026-09-15'
api_count: 0
artifact_total: 1
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aerospacekate/refs/heads/main/security/aerospacekate-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aerospacekate-domain-security.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/aerospacekate/refs/heads/main/llms/aerospacekate-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aerospacekate-llms.txt
- group: company
  title: ''
  type: Website
  url: http://www.htktjd.com/
- group: operate
  title: ''
  type: Support
  url: http://www.htktjd.com/contact.html
- group: company
  title: ''
  type: Blog
  url: http://www.htktjd.com/news/1.html
coverage:
  checked: '2026-09-12'
  detail: Aerospace Kate is a Chengdu hardware manufacturer of servo drivers, hollow-cup motors, robot joint modules and optoelectronic detection units — its 261-URL Simplified-Chinese marketing site has no developer section at all (nav is About / Core Technology / Products / News / Careers / Contact, and the only "api" strings in the HTML are the 300.cn CMS's own internal /fwebapi/ low-code datasource calls), and api./docs./developer./open.htktjd.com do not resolve.
  evidence:
  - status: 200
    url: http://www.htktjd.com/
  - status: 404
    url: http://www.htktjd.com/llms.txt
  - status: 403
    url: http://www.htktjd.com/openapi.json
  - status: 403
    url: http://www.htktjd.com/.well-known/agent-card.json
  - status: 200
    url: https://equityzen.com/company/aerospacekate/
  reason: not-a-software-company
  state: none
created: '2026-09-12'
description: Aerospace Kate (航天凯特) is the trading name of Chengdu Aerospace Kate Mechanical & Electrical Technology Co., Ltd. (成都航天凯特机电科技有限公司), a Chinese high-precision servo drive manufacturer founded in 2017 in Pidu District, Chengdu, Sichuan. A national high-tech and state-designated "little giant" specialized-and-innovative enterprise with roughly 200 staff (over half in R&D) and 210+ registered IP rights, it builds fully domestically-sourced servo drivers spanning 15V to 800V (KTSD, 蜀芯, 蓉驭 and 锦驱 series), KTMT hollow-cup motors, underwater thrusters and electric actuators, phased-array antenna steering gear, and the 灵捷 (Lingjie) line of robot joint modules, collaborative arms, quadruped robots and humanoid platforms. A second line covers optoelectronic detection — panoramic detectors, maritime search lights and airport runway FOD detection. The product is physical hardware; Aerospace Kate publishes no API, SDK, developer portal or machine-readable contract of any kind.
layout: provider
modified: '2026-09-12'
name: Aerospace Kate
nav: Providers
network: true
overview: 'Aerospace Kate is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Manufacturing, Robotics, Industrial Automation, and Motion Control.


  Aerospace Kate''s developer surface includes support, engineering blog, and 3 more developer resources.'
random_paper: 3
score:
  band: minimal
  composite: 6.1
  coverage:
    artifact_dirs: 4
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 46.3
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - china
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - greater-china
  previous_composite: 6.1
  schema_version: 0.22.0
  scored_at: '2026-09-15'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Aerospacekate Domain Security
  slug: aerospacekate-domain-security
  summary_line: no transport/DNS hardening detected
slug: aerospacekate
tags:
- Company
- Manufacturing
- Robotics
- Industrial Automation
- Motion Control
- Aerospace
- Defense
- Hardware
- China
- No Developer Program
website: http://www.htktjd.com/
---
