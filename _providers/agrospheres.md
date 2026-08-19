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
  url: security/agrospheres-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.agrospheres.com/
- group: company
  title: ''
  type: About
  url: https://www.agrospheres.com/about
- group: company
  title: ''
  type: News
  url: https://www.agrospheres.com/news
- group: other
  title: ''
  type: Email
  url: mailto:contact@agrospheres.com
coverage:
  checked: '2026-08-06'
  detail: AgroSpheres sells biological crop-protection inputs manufactured by fermentation, and its entire web presence is a three-page Webflow marketing site (/, /about, /news) with no developer, API, docs, app or status subdomain resolving in DNS and no product that could carry an API.
  evidence:
  - status: 200
    url: https://www.agrospheres.com/
  - status: 404
    url: https://www.agrospheres.com/developers
  - status: 404
    url: https://www.agrospheres.com/api
  - status: 404
    url: https://www.agrospheres.com/openapi.json
  - status: 404
    url: https://www.agrospheres.com/.well-known/agent-card.json
  - status: 404
    url: https://www.agrospheres.com/llms.txt
  reason: not-a-software-company
  state: none
created: '2026-08-06'
description: AgroSpheres is an agricultural biotechnology company based in Charlottesville, Virginia, founded by University of Virginia researchers, that develops bio-based crop protection products built on its AgriCell bioparticle platform. The company uses a single-step fermentation process that produces and biodegradably encapsulates biological actives all at once, giving added stability and a tunable release profile for targeted, non-toxic pest and disease control intended to be safe for pollinators, people and soil. Its first commercial product, the broad-spectrum biofungicide FUN-THYME, is marketed through an exclusive partnership with Wilbur-Ellis and was approved in California in 2026. AgroSpheres manufactures at a biomanufacturing facility in Charlottesville. It is a physical agricultural-inputs business and publishes no developer program, public API, or machine-readable API artifacts.
image: https://cdn.prod.website-files.com/62333ec669078315d70a0478/62431435e48d5d211e7df3c4_webclip.png
layout: provider
modified: '2026-08-06'
name: AgroSpheres
nav: Providers
network: true
overview: 'AgroSpheres is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Agriculture, Agricultural Technology, Biotechnology, and Crop Protection.


  AgroSpheres'' developer surface includes product news and 4 more developer resources.'
random_paper: 144
score:
  band: minimal
  composite: 5.0
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 5.0
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/agrospheres/refs/heads/main/screenshots/agrospheres-2026-08-07T161046.png
security:
- kind: domain-security
  name: Agrospheres Domain Security
  slug: agrospheres-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: agrospheres
tags:
- Company
- Agriculture
- Agricultural Technology
- Biotechnology
- Crop Protection
- Biologicals
- Manufacturing
website: https://www.agrospheres.com/
---
