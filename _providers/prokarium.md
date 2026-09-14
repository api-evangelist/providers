---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
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
screenshot: https://raw.githubusercontent.com/api-evangelist/prokarium/refs/heads/main/screenshots/prokarium-2026-09-02T152133.png
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
