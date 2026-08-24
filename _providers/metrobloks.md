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
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/metrobloks-domain-security.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/metrobloks-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.metrobloks.com/esg
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/metrobloks-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/metrobloks-plans-pricing.yml
- group: company
  title: ''
  type: Website
  url: https://www.metrobloks.com
- group: company
  title: ''
  type: About
  url: https://www.metrobloks.com/about-us
- group: company
  title: ''
  type: Blog
  url: https://www.metrobloks.com/blog
- group: company
  title: ''
  type: News
  url: https://www.metrobloks.com/newsroom
- group: operate
  title: ''
  type: Support
  url: https://www.metrobloks.com/contact
- group: company
  title: ''
  type: Partners
  url: https://www.metrobloks.com/channel-partners
- group: company
  title: ''
  type: Careers
  url: https://www.metrobloks.com/careers
- group: company
  title: ''
  type: Investors
  url: https://www.metrobloks.com/investors
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.metrobloks.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.metrobloks.com/privacy-policy
coverage:
  checked: '2026-08-17'
  detail: 'Metrobloks sells physical data-center capacity — halls, power, cooling and fiber cross-connects in seven metros — not software: its 54-URL Webflow sitemap contains no developer, API, docs, portal or login page at all, the "Self-Perform Interconnect" on its interconnection page is a customer pulling their own fiber rather than a software surface, and every /.well-known/* path returns a static "Invalid .well-known request" 404.'
  evidence:
  - status: 200
    url: https://www.metrobloks.com/sitemap.xml
  - status: 404
    url: https://www.metrobloks.com/openapi.json
  - status: 404
    url: https://www.metrobloks.com/llms.txt
  - status: 404
    url: https://www.metrobloks.com/.well-known/api-catalog
  - status: 404
    url: https://www.metrobloks.com/.well-known/agent-card.json
  - status: 200
    url: https://www.metrobloks.com/interconnection
  reason: not-a-software-company
  state: none
created: '2026-08-17'
description: 'Metrobloks, LLC develops and operates multi-tenant colocation data centers in underserved metropolitan markets, positioning capacity at the metro edge so that AI inference, IoT, gaming, streaming, telecom and financial workloads run closer to the users and devices that generate them. Founded by Ernest Popescu (CEO), Scott Couzens (COO), Ryan Shea (SVP Real Estate) and Alejandro Maldonado (CMO), the company came out of stealth in June 2024 with an oversubscribed $5.2M seed round led by Current Equity Partners with participation from Serena Capital, and has since announced a Eurazeo commitment of up to EUR 100 million for European expansion, a financing round led by the Canopy Generations Fund, a Kansas City joint venture with Lincoln Property Company, and a partnership with Soluna. Sites are announced or under development in Miami FL, Phoenix AZ, Detroit MI, Kansas City MO, Indianapolis IN and McAllen TX in North America, plus Paris in Europe. The product is physical: modular
  standardized halls, scalable power, air and hybrid liquid cooling with near-zero water consumption, and carrier-neutral interconnection including a self-perform cross-connect option. Metrobloks sells infrastructure, not software. It publishes no API, no developer portal, no customer self-service platform and no machine-readable specification of any kind; its only published compliance claim is a SOC 2 and SOC 3 assertion on its ESG page.'
image: https://cdn.prod.website-files.com/6608ba4eccae58b99bf07f74/66a404c6882244d7a030dca6_MB-LogoMark%40256.png
layout: provider
modified: '2026-08-17'
name: Metrobloks
nav: Providers
network: true
overview: 'Metrobloks is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Data Centers, Colocation, Interconnection, and Edge Computing.


  Metrobloks'' developer surface includes engineering blog, product news, support, and 12 more developer resources.'
plans:
- name: Metrobloks Plans Pricing
  plan_count: 0
  slug: metrobloks-plans-pricing
random_paper: 19
score:
  band: emerging
  composite: 15.1
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 15.1
  provenance:
    conformance: first-party
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
security:
- kind: domain-security
  name: Metrobloks Domain Security
  slug: metrobloks-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: metrobloks
tags:
- Company
- Data Centers
- Colocation
- Interconnection
- Edge Computing
- AI Infrastructure
- Digital Infrastructure
- Cloud Infrastructure
- Low Latency
- Liquid Cooling
- Sustainability
- Commercial Real Estate
- United States
- France
website: https://www.metrobloks.com
---
