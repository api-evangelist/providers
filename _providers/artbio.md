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
  url: security/artbio-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://artbio.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://artbio.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://artbio.com/terms-of-service
- group: company
  title: ''
  type: News
  url: https://artbio.com/#news
- group: company
  title: ''
  type: Careers
  url: https://artbio.com/#careers
- group: operate
  title: ''
  type: Contact
  url: mailto:info@artbio.com
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/artbio-inc/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/artbio_inc
- group: other
  title: ''
  type: Technology
  url: https://artbio.com/our-approach
- group: start
  title: ''
  type: ClinicalTrials
  url: https://artbio.com/clinical-trials
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/artbio-llms.txt
coverage:
  checked: '2026-08-06'
  detail: ARTBIO is a clinical-stage radiopharmaceutical company whose product is a 212Pb alpha radioligand therapy and an isotope-manufacturing process, not software — artbio.com is a five-page corporate site (pipeline, approach, clinical trials, news, careers) that returns 404 for every spec, docs and .well-known path probed, and no api./docs./ developer./portal./app. subdomain resolves in DNS at all.
  evidence:
  - status: 404
    url: https://artbio.com/openapi.json
  - status: 404
    url: https://artbio.com/api-docs
  - status: 404
    url: https://artbio.com/docs
  - status: 404
    url: https://artbio.com/graphql
  - status: 404
    url: https://artbio.com/llms.txt
  - status: 404
    url: https://artbio.com/.well-known/agent-card.json
  - status: 404
    url: https://artbio.com/.well-known/agent.json
  - status: 404
    url: https://artbio.com/.well-known/security.txt
  - status: 0
    url: https://api.artbio.com/openapi.json
  - status: 0
    url: https://docs.artbio.com/
  reason: not-a-software-company
  state: none
created: '2026-08-06'
description: ARTBIO is a clinical-stage radiopharmaceutical company developing a new class of targeted Alpha Radioligand Therapies (ARTs) built on the lead-212 (212Pb) isotope. Founded in 2021 out of research at the University of Oslo and Norway's Radium Hospital by Roy Larsen and Oyvind Bruland - the scientific co-founders behind Xofigo - the company pairs a differentiated oncology pipeline with its proprietary AlphaDirect isotope-production technology, a first-of-its-kind 212Pb isolation method intended to enable distributed manufacturing and reliable supply of alpha radioligand therapies. Its lead program AB001 (212Pb-NG001) is in first-in-human Phase 1 trials in metastatic castration-resistant prostate cancer, with additional preclinical and discovery programs across breast, head and neck, lung, pancreatic and other solid tumors. ARTBIO operates from Cambridge, Massachusetts and Oslo, is backed by F-Prime Capital, Third Rock Ventures, Omega Funds, Sofinnova Partners, B Capital, ARE and
  QIA, and is privately held. It publishes no public API, developer portal, SDK or machine-readable specification - software is not its product.
image: https://artbio.com/icons/icon-512x512.png
layout: provider
modified: '2026-08-06'
name: ARTBIO
nav: Providers
network: true
overview: 'ARTBIO is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Pharmaceuticals, Radiopharmaceuticals, and Oncology.


  ARTBIO''s developer surface includes product news and 11 more developer resources.'
random_paper: 45
score:
  band: minimal
  composite: 11.1
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 11.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 17.5
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/artbio/refs/heads/main/screenshots/artbio-2026-08-07T161737.png
security:
- kind: domain-security
  name: Artbio Domain Security
  slug: artbio-domain-security
  summary_line: TLSv1.3 · HSTS
slug: artbio
tags:
- Company
- Biotechnology
- Pharmaceuticals
- Radiopharmaceuticals
- Oncology
- Clinical Trials
- Life Sciences
- Healthcare
website: https://artbio.com/
---
