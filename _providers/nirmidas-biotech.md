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
  scored_at: '2026-08-30'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nirmidas-biotech-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.nirmidas.com/
- group: company
  title: ''
  type: About
  url: https://nirmidas.com/company-overview/
- group: company
  title: ''
  type: Blog
  url: https://nirmidas.com/news/company-news/
- group: operate
  title: ''
  type: Support
  url: https://nirmidas.com/contact-us/
- group: operate
  title: ''
  type: FAQ
  url: https://nirmidas.com/faqs/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://nirmidas.com/ueditor/php/upload/file/20220118/1642497988201475.pdf
- group: other
  title: ''
  type: Shop
  url: https://nirmidas.com/shop/
- group: other
  title: ''
  type: Publications
  url: https://nirmidas.com/publications/academic-papers/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/nirmidas-biotech-inc-
- group: company
  title: ''
  type: Twitter
  url: https://x.com/nirmidas
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/nirmidas-biotech-llms.txt
coverage:
  checked: '2026-08-26'
  detail: Nirmidas Biotech sells physical diagnostics and imaging goods — plasmonic gold (pGOLD) microarray slides, MidaScan confocal scanners, MidaSpot antibody test kits and NIR-II dyes — through an inquiry form and sales@nirmidas.com, and its entire 39-URL sitemap contains no developer, docs or API path; /api, /developers, /docs and /openapi.json all return a clean HTTP 404 from the origin.
  evidence:
  - status: 200
    url: https://www.nirmidas.com/sitemap.xml
  - status: 404
    url: https://www.nirmidas.com/api
  - status: 404
    url: https://www.nirmidas.com/openapi.json
  - status: 404
    url: https://www.nirmidas.com/.well-known/agent-card.json
  reason: not-a-software-company
  state: none
created: '2026-08-26'
description: Nirmidas Biotech, Inc. is a Mountain View, California life-science company founded in September 2013 that develops and manufactures diagnostics and imaging products built on near-infrared (NIR) fluorescence enhancement. Its patented plasmonic gold (pGOLD) assay platform boosts biological detection signals on gold-coated microarray slides and 96-well microplates, and is paired with the MidaScan and MidaScan-IR confocal scanners, MidaSpot rapid antibody test kits, and the DeepVision, KingsVision, SockEye and AlbertSurgical in vivo NIR-I / NIR-II / SWIR imaging systems, plus a catalog of NIR-II dyes and probes. The company is a member of Janssen Labs (JLABS), QB3, Stanford StartX Med and the MIT Industrial Liaison Program, manufactures under ISO 13485:2016, and received FDA Emergency Use Authorization for its MidaSpot COVID-19 antibody fingerstick test. Products are sold as physical instruments, kits and reagents through an inquiry-based storefront; Nirmidas publishes no developer
  program, no public API, and no machine-readable API contract.
image: https://nirmidas.com/img/logo.png
layout: provider
modified: '2026-08-26'
name: Nirmidas Biotech
nav: Providers
network: true
overview: 'Nirmidas Biotech is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Diagnostics, Life Sciences, and Medical Imaging.


  Nirmidas Biotech''s developer surface includes engineering blog, support, FAQ, and 9 more developer resources.'
random_paper: 17
score:
  band: minimal
  composite: 6.2
  coverage:
    artifact_dirs: 4
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 5.3
    commercial_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 3.6
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 6.2
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 10.0
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
security:
- kind: domain-security
  name: Nirmidas Biotech Domain Security
  slug: nirmidas-biotech-domain-security
  summary_line: no transport/DNS hardening detected
slug: nirmidas-biotech
tags:
- Company
- Biotechnology
- Diagnostics
- Life Sciences
- Medical Imaging
- In Vitro Diagnostics
- Laboratory Instruments
- Research Reagents
- Nanotechnology
website: https://www.nirmidas.com/
---
