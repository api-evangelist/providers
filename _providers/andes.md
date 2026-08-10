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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-10'
api_count: 0
artifact_total: 1
common:
- group: company
  title: ''
  type: Website
  url: https://www.andes.bio/
- group: company
  title: ''
  type: About
  url: https://www.andes.bio/about
- group: company
  title: ''
  type: Blog
  url: https://www.andes.bio/news-and-press
- group: company
  title: ''
  type: BlogRSS
  url: https://www.andes.bio/news?format=rss
- group: operate
  title: ''
  type: Support
  url: https://www.andes.bio/contact-general
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.andes.bio/privacy-policy
- group: company
  title: ''
  type: Careers
  url: https://www.andes.bio/careers
- group: auth
  title: ''
  type: DomainSecurity
  url: security/andes-domain-security.yml
coverage:
  checked: '2026-08-06'
  detail: Andes sells soil microbes and the durable carbon-removal credits they generate, not software; its entire public surface is a Squarespace marketing site and no api., developer., docs., app. or platform.andes.bio hostname resolves in DNS at all.
  evidence:
  - status: 200
    url: https://www.andes.bio/
  - status: 404
    url: https://www.andes.bio/openapi.json
  - status: 404
    url: https://www.andes.bio/llms.txt
  - status: 404
    url: https://www.andes.bio/.well-known/agent-card.json
  - status: 404
    url: https://www.andes.bio/.well-known/security.txt
  reason: not-a-software-company
  state: none
created: '2026-08-06'
description: Andes (Andes Ag, Inc.) is a climate-technology and agricultural-biotechnology company founded in 2018 and headquartered in Alameda, California. Andes engineers and selects beneficial soil microorganisms that are applied alongside seed in commodity row-crop production — corn, soybean, wheat and canola — where they accelerate the natural conversion of atmospheric carbon dioxide into stable soil inorganic carbon (carbonate minerals), a process the company calls Microbial Carbon Mineralization. Andes sells the resulting durable carbon dioxide removal as verified credits to corporate buyers and Scope 3 programs, and pays participating growers through the Andes Carbon Program. The company published the first Microbial Carbon Mineralization methodology, developed with EcoEngineers under ISO 14064, and has run field trials with Bayer, Cargill, Corteva, Nutrien and Wilbur-Ellis. Andes has raised roughly $38M, including a Series A co-led by Leaps by Bayer and Cavallo Ventures, and its
  shares trade on private secondary venues including EquityZen and Nasdaq Private Market. Andes publishes no public API, developer portal, SDK or machine-readable specification.
image: http://static1.squarespace.com/static/57a7b2f8f5e231cfd157e7fc/t/631ad6673365050a71e5ec8a/1662703207431/Logo+Andes+White.png?format=1500w
layout: provider
modified: '2026-08-06'
name: Andes
nav: Providers
network: true
overview: 'Andes is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Climate, Carbon Removal, Agriculture, and Agriculture Technology.


  Andes'' developer surface includes engineering blog, support, and 6 more developer resources.'
random_paper: 59
score:
  band: minimal
  composite: 8.4
  delta: 0.0
  facets:
    commercial_clarity: 10.5
    contract_quality: 0.0
    developer_ergonomics: 6.5
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 8.4
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/andes/refs/heads/main/screenshots/andes-2026-08-07T161407.png
security:
- kind: domain-security
  name: Andes Domain Security
  slug: andes-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: andes
tags:
- Company
- Climate
- Carbon Removal
- Agriculture
- Agriculture Technology
- Biotechnology
- Sustainability
- Carbon Credits
- Soil
website: https://www.andes.bio/
---
