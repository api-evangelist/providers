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
  scored_at: '2026-09-20'
api_count: 0
artifact_total: 1
common:
- group: company
  title: ''
  type: Website
  url: http://descnc-china.com/
- group: company
  title: ''
  type: About
  url: http://descnc-china.com/about.html
- group: company
  title: ''
  type: Blog
  url: http://descnc-china.com/news.html
- group: operate
  title: ''
  type: Support
  url: http://descnc-china.com/about_7.html
- group: company
  title: ''
  type: InvestorRelations
  url: http://descnc-china.com/tz1_class_6.html
- group: company
  title: ''
  type: Careers
  url: http://descnc-china.com/jobs.html
- group: other
  title: ''
  type: x-EquityZenProfile
  url: https://equityzen.com/company/aimachautomation
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aimachautomation/refs/heads/main/security/aimachautomation-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aimachautomation-domain-security.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/aimachautomation/refs/heads/main/well-known/aimachautomation-well-known.yml
  title: ''
  type: x-WellKnownProbe
  url: well-known/aimachautomation-well-known.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/aimachautomation/refs/heads/main/llms/aimachautomation-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aimachautomation-llms.txt
coverage:
  checked: '2026-09-14'
  detail: AIMACH Automation is the brand of Jiangsu Desu Intelligent Machinery, a Changzhou machine-tool components manufacturer whose products are physical assemblies (tool magazines, spindles, rotary tables, mineral-cast beds); its seven-section Chinese corporate site has no developer, API or documentation section at all, and every named /.well-known/ and spec path 404s on both of its hosts.
  evidence:
  - status: 200
    url: http://descnc-china.com/
  - status: 200
    url: http://descnc-china.com/js.html
  - status: 404
    url: http://descnc-china.com/openapi.json
  - status: 404
    url: http://descnc-china.com/.well-known/agent-card.json
  - status: 404
    url: http://www.descnc-china.com/.well-known/api-catalog
  reason: not-a-software-company
  state: none
created: '2026-09-14'
description: AIMACH Automation is the international brand of Jiangsu Desu Intelligent Machinery Co., Ltd. (江苏德速智能机械股份有限公司), a Changzhou, Jiangsu-based manufacturer of machine-tool core functional components founded in 2009. Its product lines are physical assemblies — CNC tool magazines (刀库), motorized spindles (主轴), rotary / index tables (转台) and mineral-cast machine beds (矿物铸件) — which the company states account for more than 60% of a machine tool's total cost. It also builds five-axis machining-centre platforms, ultra-precision grinders and turnkey automated production lines for automotive and general manufacturing customers, and operates provincial R&D centres for CNC machine-tool functional components. The company is pre-IPO and runs a Chinese-language corporate site with an investor-relations section; it publishes no developer portal, API documentation, SDK, or machine-readable contract of any kind.
layout: provider
modified: '2026-09-14'
name: AIMACH Automation
nav: Providers
network: true
overview: 'AIMACH Automation is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Industrial Automation, Manufacturing, Machine Tools, and CNC.


  AIMACH Automation''s developer surface includes engineering blog, support, and 8 more developer resources.'
random_paper: 6
score:
  band: minimal
  composite: 6.8
  coverage:
    artifact_dirs: 5
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
    discoverability: 53.7
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - china
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - greater-china
  previous_composite: 6.8
  schema_version: 0.22.0
  scored_at: '2026-09-20'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Aimachautomation Domain Security
  slug: aimachautomation-domain-security
  summary_line: no transport/DNS hardening detected
slug: aimachautomation
tags:
- Company
- Industrial Automation
- Manufacturing
- Machine Tools
- CNC
- Robotics
- Hardware
- China
website: http://descnc-china.com/
---
