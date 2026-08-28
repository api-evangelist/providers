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
  url: security/prokarium-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.prokarium.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.prokarium.com/privacy
- group: company
  title: ''
  type: Blog
  url: https://www.prokarium.com/news
coverage:
  checked: '2026-08-26'
  detail: Prokarium is a clinical-stage biopharmaceutical company developing the ZH9 bacterial immunotherapy for bladder cancer; its entire 96-URL sitemap is corporate, pipeline and press-release pages with no developer, docs, API or data section, and github.com/prokarium returns 404, so there is no software product for an API to sit behind.
  evidence:
  - status: 404
    url: https://www.prokarium.com/openapi.json
  - status: 404
    url: https://www.prokarium.com/.well-known/agent-card.json
  - status: 404
    url: https://www.prokarium.com/llms.txt
  - status: 404
    url: https://github.com/prokarium
  - status: 200
    url: https://www.prokarium.com/sitemap.xml
  reason: not-a-software-company
  state: none
created: '2026-08-26'
description: Prokarium is a clinical-stage biopharmaceutical company headquartered in London, UK, developing bacterial immunotherapies for solid tumors. Its foundational technology uses a proprietary attenuated strain of Salmonella enterica serovar Typhi (ZH9) as a microbial immunotherapy platform that is naturally tumor-targeting and oncolytic, designed to overcome the suppressive tumor microenvironment and generate anti-tumor immune responses while enabling diverse cargo delivery. The lead program, ZH9 for non-muscle invasive bladder cancer, is in the Phase 1/1b PARADIGM-1 trial, with a muscle-invasive bladder cancer combination arm alongside checkpoint inhibitors, an oral immune fitness agent (IO Prime), and a discovery-stage Living Cures cargo-delivery platform. Prokarium is a therapeutics developer, not a software or data company, and publishes no public API, SDK, developer portal or machine-readable interface of any kind.
layout: provider
modified: '2026-08-26'
name: Prokarium
nav: Providers
network: true
overview: 'Prokarium is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Pharmaceuticals, Life Sciences, and Immunotherapy.


  Prokarium''s developer surface includes engineering blog and 3 more developer resources.'
random_paper: 20
score:
  band: minimal
  composite: 6.3
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 46.3
    governance: 0.0
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 12.5
  schema_version: 0.15.0
  scored_at: '2026-08-26'
security:
- kind: domain-security
  name: Prokarium Domain Security
  slug: prokarium-domain-security
  summary_line: TLSv1.3 · HSTS
slug: prokarium
tags:
- Company
- Biotechnology
- Pharmaceuticals
- Life Sciences
- Immunotherapy
- Oncology
- Synthetic Biology
- Clinical Trials
- Healthcare
website: https://www.prokarium.com/
---
