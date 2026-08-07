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
  scored_at: '2026-08-06'
api_count: 0
artifact_total: 1
common:
- group: company
  title: ''
  type: Website
  url: https://alumebiosciences.com/
- group: company
  title: ''
  type: About
  url: https://alumebiosciences.com/about-us/
- group: company
  title: ''
  type: Blog
  url: https://alumebiosciences.com/news/
- group: operate
  title: ''
  type: Contact
  url: https://alumebiosciences.com/contact/
- group: company
  title: ''
  type: Careers
  url: https://alumebiosciences.com/careers/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/alumebioscience
- group: company
  title: ''
  type: Instagram
  url: https://instagram.com/alumebiosciences
- group: auth
  title: ''
  type: DomainSecurity
  url: security/alume-biosciences-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/alume-biosciences-llms.txt
coverage:
  checked: '2026-08-06'
  detail: Alume Biosciences is a clinical-stage drug developer whose entire web presence is a five-page WordPress marketing site (about, news, careers, contact) with no developer, API or documentation section anywhere in its sitemap; the only machine-readable endpoint on the host is the default WordPress /wp-json/ CMS route index, which is site infrastructure and not a published API product.
  evidence:
  - status: 404
    url: https://alumebiosciences.com/openapi.json
  - status: 404
    url: https://alumebiosciences.com/.well-known/agent-card.json
  - status: 404
    url: https://alumebiosciences.com/llms.txt
  - status: 200
    url: https://alumebiosciences.com/wp-sitemap-posts-page-1.xml
  - status: 404
    url: https://github.com/alumebio
  reason: not-a-software-company
  state: none
created: '2026-08-06'
description: 'Alume Biosciences is a clinical-stage biotechnology company in La Jolla, California, developing nerve-targeted fluorescent agents for precision surgery. Its lead candidate, bevonescein (ALM-488) — a peptide-dye conjugate co-invented by the late Nobel Laureate Dr. Roger Tsien and surgeon Dr. Quyen Nguyen — is administered intravenously roughly an hour before an operation so surgeons can see nerves illuminated in the surgical field and avoid inadvertent nerve injury. The compound has FDA Fast Track designation, is in Phase 3 pivotal trials in head-and-neck surgery, and the company has stated it plans a New Drug Application submission in 2026. Alume is a drug developer, not a software vendor: it publishes no developer program, API, SDK or machine-readable specification.'
image: https://alumebiosciences.com/wp-content/uploads/2019/08/apple-icon-180x180.png
layout: provider
modified: '2026-08-06'
name: Alume Biosciences
nav: Providers
network: true
overview: 'Alume Biosciences is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Life Sciences, Pharmaceuticals, and Clinical Trials.


  Alume Biosciences'' developer surface includes engineering blog and 8 more developer resources.'
random_paper: 41
score:
  band: minimal
  composite: 7.3
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.2
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.9.1
  scored_at: '2026-08-06'
security:
- kind: domain-security
  name: Alume Biosciences Domain Security
  slug: alume-biosciences-domain-security
  summary_line: TLSv1.3
slug: alume-biosciences
tags:
- Company
- Biotechnology
- Life Sciences
- Pharmaceuticals
- Clinical Trials
- Surgery
- Medical Imaging
- Health
website: https://alumebiosciences.com/
---
