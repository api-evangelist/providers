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
  scored_at: '2026-08-26'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kiute-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.kiute.com/
coverage:
  checked: '2026-08-17'
  detail: Kiute was acquired by Booksy on 2021-11-09 and the brand is fully retired — every path on every Kiute host returns a blanket HTTP 301 to booksy.com or biz.booksy.com, no api/docs/ developers subdomain resolves, and the wildcard TLS certificate on www.kiute.com expired on 2026-08-13 and is being served unrenewed.
  evidence:
  - status: 301
    url: https://www.kiute.com/
  - status: 301
    url: https://pro.kiute.com/
  - status: 301
    url: https://www.kiute.com/openapi.json
  - status: 301
    url: https://www.kiute.com/.well-known/agent-card.json
  - status: 404
    url: https://api.github.com/orgs/kiute
  reason: defunct
  state: none
created: '2026-08-17'
description: 'Kiute was a French salon management and online booking platform for hair salons, barbershops and beauty institutes, formed from the September 2020 merger of Flexy (FlexyBeauty) and LeCiseau, backed by Serena, Newfund, Matmut Innovation, 123IM, UL Invest and Bourrelier Group. Its Kiute Pro product combined a point-of-sale till, appointment calendar, client records, marketing and an online booking marketplace serving roughly 10,000 beauty and wellness businesses. Booksy acquired Kiute on 2021-11-09 and has since retired the brand: as of 2026-08-17 every Kiute host answers a blanket HTTP 301 to Booksy for every path — kiute.com, www.kiute.com, app.kiute.com and kiute.fr to https://booksy.com/fr-fr/, pro.kiute.com to https://biz.booksy.com/fr-fr — and no api, docs, developers or help subdomain resolves. Kiute publishes no API, no specification and no developer program of its own; the successor surface is the Booksy Public API, profiled separately in this network at all/booksy/
  and documented at docs.booksy.com.'
layout: provider
modified: '2026-08-17'
name: Kiute
nav: Providers
network: true
overview: Kiute is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Marketplace, Beauty, Salons, and Booking.
random_paper: 0
score:
  band: minimal
  composite: 4.6
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 46.3
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 4.6
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
security:
- kind: domain-security
  name: Kiute Domain Security
  slug: kiute-domain-security
  summary_line: DMARC
slug: kiute
tags:
- Company
- Marketplace
- Beauty
- Salons
- Booking
- Appointments
- Point-of-Sale
- Small Business
- France
- Acquired
website: https://www.kiute.com/
---
