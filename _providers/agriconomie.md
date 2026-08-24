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
  url: security/agriconomie-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.agryco.com/
- group: company
  title: ''
  type: Blog
  url: https://www.agryco.com/blog
- group: operate
  title: ''
  type: Support
  url: https://www.agryco.com/contact
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.agryco.com/publi/foire-aux-questions
- group: start
  title: ''
  type: Login
  url: https://www.agryco.com/account
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.agryco.com/publi/conditions-generales-vente
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.agryco.com/publi/politique-de-confidentialite
- group: commercial
  title: ''
  type: LegalNotice
  url: https://www.agryco.com/publi/mentions-legales
- group: company
  title: ''
  type: LinkedIn
  url: https://fr.linkedin.com/company/agryco-france
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@Agryco_com
coverage:
  checked: '2026-08-06'
  detail: 'Agryco (ex-Agriconomie) runs a real engineering stack — api.agriconomie.com is a live nginx origin — but it is closed: every anonymous path on it 404s, the storefront''s only API prefix is Disallow''d in the site''s own robots.txt, and agryco.com publishes no developer portal, API reference, SDK, llms.txt or .well-known document of any kind.'
  evidence:
  - status: 404
    url: https://api.agriconomie.com/openapi.json
  - status: 404
    url: https://api.agriconomie.com/graphql
  - status: 404
    url: https://www.agryco.com/llms.txt
  - status: 404
    url: https://www.agryco.com/.well-known/agent-card.json
  - status: 200
    url: https://www.agryco.com/robots.txt
  reason: no-developer-program
  state: none
created: '2026-08-06'
description: 'Agryco — trading as Agriconomie until its September 2024 rebrand — is a French online marketplace and e-commerce platform that sells agricultural supplies direct to farmers: mineral, organic and foliar fertilizers, conventional and organic seeds, phytosanitary products, animal nutrition and livestock equipment, plus tractor, spraying, harvesting and soil-working spare parts. Founded in 2014 by Clement Le Fournis, Dinh Nguyen and Paolin Pascot, the company operates a one-stop procurement site for professional farmers across France, Belgium, Germany, Spain and Italy, wrapping the catalog in advisory services (agronomy experts on the phone six days a week), fertilizer blending, equipment valuation and 60-day payment terms. It raised a EUR 60 million Series B in 2022 co-led by Treis Group, Temasek and Aliment Capital with Eurazeo participating, and publishes the Agrycomag technical magazine at agryco.com/blog. Agryco is an end-user commerce product: as of this profile it publishes
  no public developer program, API reference, SDK or machine-readable specification.'
image: https://www.agryco.com/assets/images/front-fr/layout/logo.png
layout: provider
modified: '2026-08-06'
name: Agryco
nav: Providers
network: true
overview: 'Agryco is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Agriculture, AgTech, E-Commerce, Marketplace, and Farm Supplies.


  Agryco''s developer surface includes engineering blog, support, YouTube channel, and 8 more developer resources.'
random_paper: 10
score:
  band: minimal
  composite: 9.1
  delta: 0.0
  facets:
    access_clarity: 17.1
    commercial_clarity: 17.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 3.6
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 9.1
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/agriconomie/refs/heads/main/screenshots/agriconomie-2026-08-07T161046.png
security:
- kind: domain-security
  name: Agriconomie Domain Security
  slug: agriconomie-domain-security
  summary_line: TLSv1.3
slug: agriconomie
tags:
- Agriculture
- AgTech
- E-Commerce
- Marketplace
- Farm Supplies
- Agricultural Inputs
- Retail
- France
- Europe
- Company
website: https://www.agryco.com/
---
