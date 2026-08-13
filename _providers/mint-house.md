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
  scored_at: '2026-08-12'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mint-house-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://minthouse.com/
- group: company
  title: ''
  type: About
  url: https://minthouse.com/our-story/
- group: operate
  title: ''
  type: Support
  url: https://minthouse.com/contact-us/
- group: operate
  title: ''
  type: Contact
  url: https://minthouse.com/contact-us/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://minthouse.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://minthouse.com/terms-of-service/
- group: company
  title: ''
  type: Press
  url: https://minthouse.com/press/
- group: company
  title: ''
  type: Careers
  url: https://minthouse.com/careers/
coverage:
  checked: '2026-08-04'
  detail: 'Mint House was fully absorbed into Kasa in an all-equity combination that closed in January 2026 — minthouse.com now 301s its homepage to minthouse.kasa.com and every corporate page (our-story, partnerships, press, careers, privacy, terms) to kasa.com — and no Mint House host ever published a developer program: the only machine-readable endpoint anywhere on the domain is the marketing site''s default WordPress /wp-json/ index (Yoast, Klaviyo, contact-form-7 plugin namespaces), not a product API.'
  evidence:
  - status: 301
    url: https://minthouse.com/our-story/
  - status: 404
    url: https://minthouse.com/openapi.json
  - status: 404
    url: https://minthouse.com/.well-known/agent-card.json
  - status: 404
    url: https://minthouse.com/.well-known/security.txt
  - status: 404
    url: https://minthouse.com/llms.txt
  - status: 404
    url: https://minthouse.com/graphql
  - status: 404
    url: https://minthouse.kasa.com/openapi.json
  - status: 200
    url: https://minthouse.com/wp-json/
  reason: defunct
  state: none
created: '2026-08-04'
description: 'Mint House is a US residential-hospitality operator founded in 2017 by Will Lucas that runs tech-enabled apartment-hotel units — full kitchens, workspaces and app-based check-in — in downtown districts of markets including New York, Miami, Nashville, Dallas, Washington DC, Houston, Phoenix and Madison. It raised a $35M Series B in May 2022 led by Mohari Hospitality with Revolution Ventures, Allegion Ventures and Ingleside Investors. In January 2026 Mint House entered an all-equity strategic combination with Kasa; the portfolio now operates as "Mint House by Kasa" and every corporate page on minthouse.com redirects to kasa.com. Mint House is a hospitality operator, not a software vendor: it publishes a consumer booking site and no public API, SDK, webhook or developer program of any kind.'
image: https://framerusercontent.com/images/JM7Xx4oLAi797Ygekd5Ao7AGwg.png
layout: provider
modified: '2026-08-04'
name: Mint House
nav: Providers
network: true
overview: 'Mint House is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Hospitality, Travel, Lodging, and Apartment Hotels.


  Mint House''s developer surface includes support and 8 more developer resources.'
random_paper: 73
score:
  band: minimal
  composite: 10.1
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 0.0
    developer_ergonomics: 4.3
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 10.1
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mint-house/refs/heads/main/screenshots/mint-house-2026-08-07T172959.png
security:
- kind: domain-security
  name: Mint House Domain Security
  slug: mint-house-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: mint-house
tags:
- Company
- Hospitality
- Travel
- Lodging
- Apartment Hotels
- Short Term Rental
- Real Estate
- Property Management
website: https://minthouse.com/
---
