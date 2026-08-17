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
  scored_at: '2026-08-17'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/clerio-vision-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.cleriovision.com/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/clerio-vision-inc.
coverage:
  checked: '2026-08-09'
  detail: Clerio Vision sells femtosecond-laser systems and LIRIC-written contact lenses, not software; cleriovision.com is a single-page WordPress site whose sitemap contains exactly one URL, there is no developer, docs or api subdomain in DNS, and the GitHub account referenced in search results does not exist.
  evidence:
  - status: 200
    url: https://www.cleriovision.com/
  - status: 404
    url: https://www.cleriovision.com/developers
  - status: 404
    url: https://www.cleriovision.com/openapi.json
  - status: 404
    url: https://www.cleriovision.com/.well-known/agent-card.json
  - status: 200
    url: https://www.cleriovision.com/sitemap_index.xml
  - status: 404
    url: https://api.github.com/users/cleriovision
  reason: not-a-software-company
  state: none
created: '2026-08-09'
description: 'Clerio Vision is a development-stage ophthalmic medical device company based in Rochester, New York, commercializing LIRIC (Laser Induced Refractive Index Change) — a non-invasive femtosecond-laser platform, licensed from the University of Rochester''s Center for Visual Science, that alters the refractive index of corneal tissue and of polymer optics without cutting or removing material. The company applies LIRIC across four ophthalmic segments: multifocal soft contact lenses for presbyopia, myopia control in children, post-implant intraocular lens (IOL) optimization after cataract surgery, and incisionless corneal refractive correction. Clerio has raised roughly $40 million from Safar Partners, Armory Square Ventures, Topmark Partners, Proxima Ventures, Atma Capital, Hegemon Capital and the National Science Foundation, and holds more than 90 patents across over 30 families. Its products are lasers, optics and lenses rather than software; the company publishes a single-page
  marketing and investor website and operates no public developer program, API, SDK or developer portal.'
image: https://www.cleriovision.com/Images/CV_logo.jpeg
layout: provider
modified: '2026-08-09'
name: Clerio Vision
nav: Providers
network: true
overview: Clerio Vision is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Medical Devices, Ophthalmology, Vision Care, and Health.
random_paper: 6
score:
  band: minimal
  composite: 5.4
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 5.4
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
security:
- kind: domain-security
  name: Clerio Vision Domain Security
  slug: clerio-vision-domain-security
  summary_line: TLSv1.3 · DMARC
slug: clerio-vision
tags:
- Company
- Medical Devices
- Ophthalmology
- Vision Care
- Health
- Laser Systems
- Contact Lenses
- Medical Technology
website: https://www.cleriovision.com/
---
