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
  url: security/achates-power-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://achatespower.com/
- group: company
  title: ''
  type: Blog
  url: https://achatespower.com/news-blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://achatespower.com/news-blog/feed/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://achatespower.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://achatespower.com/wp-content/uploads/2020/03/achates_power_terms_and_conditions.pdf
- group: company
  title: ''
  type: Careers
  url: https://achatespower.com/careers/
- group: company
  title: ''
  type: About
  url: https://achatespower.com/about-achates-power/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/achates-power_stock/
coverage:
  checked: '2026-08-06'
  detail: Achates Power licenses opposed-piston engine hardware designs and simulation tooling to OEMs under contract; its entire 26-page WordPress sitemap contains no developer, API or docs page, its only partner surface is a supplier-application contact form, and no api/developer/docs subdomain resolves in DNS.
  evidence:
  - status: 404
    url: https://achatespower.com/openapi.json
  - status: 404
    url: https://achatespower.com/.well-known/agent-card.json
  - status: 404
    url: https://achatespower.com/.well-known/security.txt
  - status: 404
    url: https://achatespower.com/llms.txt
  - status: 200
    url: https://achatespower.com/page-sitemap.xml
  - status: 200
    url: https://achatespower.com/supplier-portal/
  reason: not-a-software-company
  state: none
created: '2026-08-06'
description: Achates Power is a San Diego, California engine technology company founded in 2004 by Dr. James Lemke and John Walton that develops opposed-piston, two-stroke compression-ignition engine architecture and licenses the resulting engine designs, development tools, simulation software and patents to engine manufacturers and OEMs. Its engines target passenger vehicles, medium and heavy-duty commercial trucks, military vehicles, and off-road and power-generation applications, and the company has claimed fuel-efficiency improvements of as much as 30 percent over conventional engines at comparable or better emissions. Achates Power has received U.S. Army TARDEC, Department of Energy and ARPA-E funding and partners with engine manufacturers such as Fairbanks Morse. It is a privately held hardware and engineering licensing business and publishes no public developer program, API, or machine-readable API artifacts.
image: https://achatespower.com/wp-content/uploads/2019/10/AchatesPower_Logo_RBG.svg
layout: provider
modified: '2026-08-06'
name: Achates Power
nav: Providers
network: true
overview: 'Achates Power is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Automotive, Engines, Manufacturing, and Clean Technology.


  Achates Power''s developer surface includes engineering blog and 8 more developer resources.'
random_paper: 8
score:
  band: minimal
  composite: 9.6
  coverage:
    artifact_dirs: 3
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 9.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 18.9
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/achates-power/refs/heads/main/screenshots/achates-power-2026-08-07T160824.png
security:
- kind: domain-security
  name: Achates Power Domain Security
  slug: achates-power-domain-security
  summary_line: TLSv1.3 · DMARC
slug: achates-power
tags:
- Company
- Automotive
- Engines
- Manufacturing
- Clean Technology
- Transportation
- Defense
- Power Generation
website: https://achatespower.com/
---
