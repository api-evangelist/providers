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
- group: auth
  title: ''
  type: DomainSecurity
  url: security/arzeda-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.arzeda.com/
- group: company
  title: ''
  type: About
  url: https://www.arzeda.com/about
- group: other
  title: ''
  type: Technology
  url: https://www.arzeda.com/technology
- group: company
  title: ''
  type: Blog
  url: https://www.arzeda.com/blog
- group: company
  title: ''
  type: News
  url: https://www.arzeda.com/news
- group: other
  title: ''
  type: Publications
  url: https://www.arzeda.com/publications
- group: other
  title: ''
  type: Team
  url: https://www.arzeda.com/team
- group: company
  title: ''
  type: Careers
  url: https://www.arzeda.com/careers
- group: operate
  title: ''
  type: Contact
  url: https://www.arzeda.com/contact
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Arzeda
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/arzeda-corp
- group: company
  title: ''
  type: Twitter
  url: https://x.com/ArzedaCo
- group: other
  title: ''
  type: Sitemap
  url: https://www.arzeda.com/sitemap.xml
coverage:
  checked: '2026-08-06'
  detail: Arzeda sells designed enzymes, molecules and joint-development programs rather than software — its arzeda.com Webflow site answers every unknown path (including /openapi.json, /llms.txt and /.well-known/agent-card.json) with the identical 97,718-byte homepage soft-404, and api./docs./developer./app./platform.arzeda.com do not resolve in DNS at all.
  evidence:
  - status: 200
    url: https://www.arzeda.com/openapi.json
  - status: 200
    url: https://www.arzeda.com/definitely-not-a-real-path-xyz123
  - status: 200
    url: https://www.arzeda.com/.well-known/agent-card.json
  - status: 200
    url: https://www.arzeda.com/.well-known/security.txt
  - status: 200
    url: https://www.arzeda.com/llms.txt
  - status: 0
    url: https://api.arzeda.com/
  - status: 0
    url: https://docs.arzeda.com/
  - status: 200
    url: https://www.arzeda.com/sitemap.xml
  reason: no-developer-program
  state: none
created: '2026-08-06'
description: Arzeda Corp is a Seattle, Washington protein design company — "The Protein Design Company" — founded in 2008 by David Baker (2024 Nobel Prize in Chemistry), Alexandre Zanghellini and colleagues out of the University of Washington Institute for Protein Design. Its Intelligent Protein Design Technology combines physics-based computational protein design, generative AI and an agentic design-build-test-learn loop over fifteen years of proprietary in-house experimental data to create designer enzymes and proteins that do not exist in nature, then scale them to commercial production. Commercial programs span food and beverage (ViaLeaf Reb M / ProSweet Reb M stevia sweeteners with MANE), home and personal care enzymes (Unilever), advanced materials (W. L. Gore & Associates) and pharmaceutical biologics (Takeda), alongside DARPA and NSF funded work on AI-driven protein design and cell-free biomanufacturing. Arzeda co-founded the OpenFold consortium for open-source protein structure
  prediction. It sells designed molecules and joint development programs, not software, and publishes no public developer program, API or machine-readable interface.
image: https://www.arzeda.com/assets/logos/arzeda_clr_wht.svg
layout: provider
modified: '2026-08-06'
name: Arzeda
nav: Providers
network: true
overview: 'Arzeda is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Synthetic Biology, Protein Design, and Enzymes.


  Arzeda''s developer surface includes engineering blog, product news, and 12 more developer resources.'
random_paper: 51
score:
  band: minimal
  composite: 6.3
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.2
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 6.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/arzeda/refs/heads/main/screenshots/arzeda-2026-08-07T161747.png
security:
- kind: domain-security
  name: Arzeda Domain Security
  slug: arzeda-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: arzeda
tags:
- Company
- Biotechnology
- Synthetic Biology
- Protein Design
- Enzymes
- Artificial Intelligence
- Life Sciences
- Specialty Chemicals
- Food Ingredients
- Materials Science
- Pharmaceuticals
- Seattle
website: https://www.arzeda.com/
---
