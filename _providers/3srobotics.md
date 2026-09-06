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
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/3srobotics-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/3srobotics-llms.txt
- group: company
  title: ''
  type: Website
  url: https://3srobotics.com/
- group: company
  title: ''
  type: About
  url: https://3srobotics.com/profile.html
- group: other
  title: ''
  type: Products
  url: https://3srobotics.com/universal.html
- group: other
  title: ''
  type: Software
  url: https://3srobotics.com/software.html
- group: other
  title: ''
  type: CaseStudies
  url: https://3srobotics.com/crec.html
- group: company
  title: ''
  type: Blog
  url: https://3srobotics.com/news.html
- group: operate
  title: ''
  type: Support
  url: https://3srobotics.com/why.html
- group: operate
  title: ''
  type: Contact
  url: https://3srobotics.com/contact.html
- group: company
  title: ''
  type: Careers
  url: https://3srobotics.com/join.html
- group: other
  title: ''
  type: Downloads
  url: https://3srobotics.com/download.html
- group: other
  title: ''
  type: Subsidiary
  url: https://www.hgxd.cn/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://equityzen.com/company/3srobotics
coverage:
  checked: '2026-09-05'
  detail: 3S robotics sells industrial welding, grinding and assembly robots whose "AI + 3D + ROBOT" vision and offline-programming software runs on the machine and ships with the hardware — 3srobotics.com is a 14-page static Bootstrap brochure whose only gated area is a member product-manual download, there is no developer portal, SDK or API subdomain (api., docs., developer. and open. all fail to resolve in DNS), and no GitHub organization exists.
  evidence:
  - status: 200
    url: https://3srobotics.com/software.html
  - status: 200
    url: https://3srobotics.com/download.html
  - status: 404
    url: https://3srobotics.com/openapi.json
  - status: 404
    url: https://3srobotics.com/.well-known/agent-card.json
  - status: 404
    url: https://3srobotics.com/sitemap.xml
  - status: 404
    url: https://github.com/3srobotics
  reason: no-developer-program
  state: none
created: '2026-09-05'
description: 3S robotics (Shanghai Shengshi Weisheng Technology Co., Ltd. / 上海昇视唯盛科技有限公司) is a Chinese intelligent-robotics manufacturer founded in 2020 and headquartered in the Songjiang district of Shanghai, with a smart factory in the Haining Economic Development Zone, Zhejiang. It is a member company of the listed Harbin Institute of Technology intelligent-robotics group (哈工智能), and its majority-held subsidiary Hagong Hyundai (哈工现代, HGXD) builds general-purpose industrial robots. The company develops an in-house "AI + 3D + ROBOT" stack — machine-vision cameras, motion control, and offline path-planning software — packaged as task-specific intelligent robots for welding, grinding and assembly, marketed as needing no teach-pendant programming. Its flagship line is a 3D-vision intelligent welding robot aimed at steel-structure, tunnel arch, rail-transit and heavy-equipment fabrication. The software it ships is embedded machine-side control and vision tooling sold with the hardware; the
  company publishes no public developer program, API, SDK or machine-readable interface contract.
layout: provider
modified: '2026-09-05'
name: 3S robotics
nav: Providers
network: true
overview: '3S robotics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Robotics, Industrial Robots, Manufacturing, and Machine Vision.


  3S robotics'' developer surface includes engineering blog, support, and 12 more developer resources.'
random_paper: 6
score:
  band: minimal
  composite: 5.8
  coverage:
    artifact_dirs: 3
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 6.0
    discoverability: 46.3
    governance: 0.0
    operational_transparency: 0.0
  schema_version: 0.18.3
  scored_at: '2026-09-05'
security:
- kind: domain-security
  name: 3Srobotics Domain Security
  slug: 3srobotics-domain-security
  summary_line: TLSv1.3 · DMARC
slug: 3srobotics
tags:
- Company
- Robotics
- Industrial Robots
- Manufacturing
- Machine Vision
- Welding Automation
- Industrial Automation
- Hardware
website: https://3srobotics.com/
---
