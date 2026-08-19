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
  scored_at: '2026-08-19'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/oxa-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://oxa.tech/
- group: company
  title: ''
  type: About
  url: https://oxa.tech/about/
- group: other
  title: ''
  type: Products
  url: https://oxa.tech/products/
- group: company
  title: ''
  type: Blog
  url: https://oxa.tech/news-and-insights/
- group: operate
  title: ''
  type: Contact
  url: https://oxa.tech/contact/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://oxa.tech/terms-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://oxa.tech/privacy-policy/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/oxauniversalautonomy
- group: company
  title: ''
  type: Careers
  url: https://oxa.tech/careers/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/oxa_stock/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/oxa-llms.txt
coverage:
  checked: '2026-08-04'
  detail: Oxa's products and technology pages both advertise that Oxa Hub ships "an API for optional integration with existing logistics systems", but there is no developer portal, no reference and no spec anywhere public — every developer path on oxa.tech 404s, not one developer subdomain resolves, and the only route to the API is the Sales option on the contact form.
  evidence:
  - status: 200
    url: https://oxa.tech/products/
  - status: 404
    url: https://oxa.tech/developers
  - status: 404
    url: https://oxa.tech/openapi.json
  - status: 404
    url: https://oxa.tech/.well-known/agent-card.json
  - status: 200
    url: https://oxa.tech/contact/
  reason: sales-gate
  state: gated
created: '2026-08-04'
description: Oxa (formerly Oxbotica, rebranded in 2023) is a British autonomous vehicle software company founded in 2014 in Oxford, England by Paul Newman and Ingmar Posner. Oxa builds what it calls Universal Autonomy — self-driving software configurable for almost any vehicle in almost any environment — and sells it as Industrial Mobility Automation for ports, airports, manufacturing yards, solar farms and shuttle networks. Its product line is Oxa Driver (the autonomy stack), Oxa Foundry (a generative-AI training and assurance toolchain, previously marketed as Oxa MetaDriver), Reference Autonomy Designs (modular hardware integration blueprints), and Oxa Hub (a cloud fleet-management suite covering remote assist, task design, workspace mapping, digital twins and in-use monitoring). Oxa Hub is described on the marketing site as offering "an API for optional integration with existing logistics systems", but Oxa publishes no developer portal, no API reference and no machine-readable specification
  on any public host. The company raised a $115M Series C in 2023 with participation from Google, and works with Ocado Group, ZF and bp.
image: https://oxa.tech/_nuxt/image/012618.jpg
layout: provider
modified: '2026-08-04'
name: Oxa
nav: Providers
network: true
overview: 'Oxa is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Autonomous Vehicles, Automotive, Robotics, and Artificial Intelligence.


  Oxa''s developer surface includes engineering blog and 11 more developer resources.'
random_paper: 30
score:
  band: minimal
  composite: 10.4
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 10.4
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/oxa/refs/heads/main/screenshots/oxa-2026-08-07T191159.png
security:
- kind: domain-security
  name: Oxa Domain Security
  slug: oxa-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: oxa
tags:
- Company
- Autonomous Vehicles
- Automotive
- Robotics
- Artificial Intelligence
- Fleet Management
- Logistics
- Transportation
- Industrial Automation
- United Kingdom
website: https://oxa.tech/
---
