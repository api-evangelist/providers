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
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/prologium-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://prologium.com/
- group: company
  title: ''
  type: About
  url: https://prologium.com/about/
- group: company
  title: ''
  type: Blog
  url: https://prologium.com/news/
- group: company
  title: ''
  type: BlogRSS
  url: https://prologium.com/feed/
- group: operate
  title: ''
  type: Support
  url: https://prologium.com/contact/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://prologium.com/privacy-cookie/
- group: company
  title: ''
  type: Careers
  url: https://prologium.com/careers-apac/
- group: company
  title: ''
  type: Investors
  url: https://prologium.com/investors/
- group: auth
  title: ''
  type: Certifications
  url: https://prologium.com/certification/
- group: other
  title: ''
  type: Products
  url: https://prologium.com/products/
- group: other
  title: ''
  type: Technology
  url: https://prologium.com/tech/core-technology/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/13667317
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/ProLogium
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/user/prologium
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/prologium.tech/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/prologium_stock/
coverage:
  checked: '2026-08-05'
  detail: ProLogium manufactures solid-state lithium ceramic battery cells, modules and packs — its site is a WordPress marketing and investor-relations presence with no developer section, and every contract-discovery path (/openapi.json, /swagger.json, /api-docs, /graphql, /llms.txt, /.well-known/agent-card.json) returns the same WordPress 404 template on both prologium.com and prologium.com.tw.
  evidence:
  - status: 404
    url: https://prologium.com/openapi.json
  - status: 404
    url: https://prologium.com/.well-known/agent-card.json
  - status: 404
    url: https://prologium.com/developers
  - status: 404
    url: https://prologium.com/llms.txt
  - status: 200
    url: https://prologium.com/sitemap.xml
  reason: not-a-software-company
  state: none
created: '2026-08-05'
description: 'ProLogium Technology Co., Ltd. is a Taiwanese energy-innovation company founded in 2006 that develops and manufactures next-generation solid-state lithium ceramic batteries built around a 100% ceramic separator. It commercialized its first solid-state cells in 2013, opened the world''s first giga-level solid-state lithium ceramic battery plant in Taoyuan, Taiwan in 2024, and operates a European R&D center at Paris-Saclay with a planned gigafactory in Dunkirk, France. Its product lines span FLCB, PLCB and LLCB cells plus battery modules and packs, targeting electric vehicles, energy storage systems, robotics, and consumer and industrial applications. ProLogium is a hardware manufacturer: it publishes no developer portal, no public API, and no machine-readable API contract of any kind.'
image: https://prologium.com/wp-content/uploads/2021/04/ProLogium-Group-fav.png
layout: provider
modified: '2026-08-05'
name: ProLogium Technology
nav: Providers
network: true
overview: 'ProLogium Technology is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Battery, Solid-State Battery, Energy Storage, and Electric Vehicles.


  ProLogium Technology''s developer surface includes engineering blog, support, YouTube channel, and 14 more developer resources.'
random_paper: 3
score:
  band: minimal
  composite: 7.6
  coverage:
    artifact_dirs: 2
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 7.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 13.5
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Prologium Domain Security
  slug: prologium-domain-security
  summary_line: TLSv1.3
slug: prologium
tags:
- Company
- Battery
- Solid-State Battery
- Energy Storage
- Electric Vehicles
- Manufacturing
- Hardware
- Automotive
- Taiwan
website: https://prologium.com/
---
