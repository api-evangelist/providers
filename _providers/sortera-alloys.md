---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-24'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sortera-alloys-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.sorteratechnologies.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.sorteratechnologies.com/privacy-policy/
- group: operate
  title: ''
  type: Contact
  url: https://www.sorteratechnologies.com/contact/
- group: company
  title: ''
  type: News
  url: https://www.sorteratechnologies.com/news-press/
- group: company
  title: ''
  type: Careers
  url: https://www.sorteratechnologies.com/careers/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/sorteratech
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/sortera-alloys_stock/
coverage:
  checked: '2026-08-05'
  detail: Sortera sells sorted aluminum scrap rather than software - its AI runs inside its own sortation lines - and the published sitemap.xml enumerates only marketing, team, careers and press pages, with /developers, /api and /docs returning 404 and no api., docs. or developer. subdomain resolving in DNS.
  evidence:
  - status: 200
    url: https://www.sorteratechnologies.com/sitemap.xml
  - status: 404
    url: https://www.sorteratechnologies.com/developers
  - status: 404
    url: https://www.sorteratechnologies.com/api
  - status: 404
    url: https://www.sorteratechnologies.com/docs
  - status: 404
    url: https://www.sorteratechnologies.com/openapi.json
  - status: 404
    url: https://www.sorteratechnologies.com/llms.txt
  - status: 404
    url: https://www.sorteratechnologies.com/.well-known/agent-card.json
  - status: 404
    url: https://www.sorteratechnologies.com/.well-known/agent.json
  - status: 404
    url: https://www.sorteratechnologies.com/.well-known/security.txt
  - status: 0
    url: https://api.sorteratechnologies.com/
  reason: not-a-software-company
  state: none
created: '2026-08-05'
description: Sortera Technologies (formerly Sortera Alloys) is an AI-driven metals recycling company founded in 2020 and headquartered in Markle / Fort Wayne, Indiana. It combines sensor fusion (XRF plus optical), machine-learning image and data analytics, and an advanced high-throughput scrap feeder to sort end-of-life scrap by metal type and alloy composition, upgrading feedstock streams and removing contaminants at industrial scale. From a 200,000 square foot sortation facility opened in 2023 the company produces specification aluminum scrap across cast, extrusion and sheet fractions - including 380, 356, 319 and wrought grades such as 3105 - and sells it back into domestic manufacturing. Its stated vision is 100% reuse of metals recovered from end-of-life products. The artificial intelligence runs inside Sortera's own sorting lines as an in-house platform; the product sold is recycled metal, not software, and the company publishes no public API, SDK, developer portal or machine-readable
  specification.
image: https://sortera.wpengine.com/wp-content/uploads/2022/07/Screen-Shot-2022-07-07-at-10.01.57-AM.png
layout: provider
modified: '2026-08-05'
name: Sortera Technologies
nav: Providers
network: true
overview: 'Sortera Technologies is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Recycling, Metals, Manufacturing, and Artificial Intelligence.


  Sortera Technologies'' developer surface includes product news and 7 more developer resources.'
random_paper: 3
score:
  band: minimal
  composite: 7.1
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 7.1
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
security:
- kind: domain-security
  name: Sortera Alloys Domain Security
  slug: sortera-alloys-domain-security
  summary_line: TLSv1.3 · HSTS
slug: sortera-alloys
tags:
- Company
- Recycling
- Metals
- Manufacturing
- Artificial Intelligence
- Circular Economy
- Industrial
- Sustainability
website: https://www.sorteratechnologies.com/
---
