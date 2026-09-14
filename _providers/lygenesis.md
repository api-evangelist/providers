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
- group: company
  title: ''
  type: Website
  url: https://www.lygenesis.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.lygenesis.com/privacy-policy/
- group: operate
  title: ''
  type: Support
  url: https://www.lygenesis.com/contact/
- group: company
  title: ''
  type: Blog
  url: https://www.lygenesis.com/media/insights/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/lygenesis/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/LyGenesis_Inc
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lygenesis-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/lygenesis-llms.txt
coverage:
  checked: '2026-08-25'
  detail: 'LyGenesis is a clinical-stage cell therapy company whose product is a lymph-node organogenesis therapy in a Phase 2a trial, not software: its www.lygenesis.com Nuxt site 404s on every spec and /.well-known/ path, api./developer./docs.lygenesis.com do not resolve, and there is no GitHub org, npm or PyPI package.'
  evidence:
  - status: 404
    url: https://www.lygenesis.com/openapi.json
  - status: 404
    url: https://www.lygenesis.com/.well-known/agent-card.json
  - status: 404
    url: https://www.lygenesis.com/llms.txt
  - status: 200
    url: https://api.github.com/search/repositories?q=lygenesis
  reason: not-a-software-company
  state: none
created: '2026-08-25'
description: 'LyGenesis is a Pittsburgh-based clinical-stage cell therapy company developing allogeneic regenerative therapies that use a patient''s own lymph nodes as bioreactors to grow functioning ectopic organs. Its lead program transplants donor hepatocytes into upper-abdominal lymph nodes via endoscopic ultrasound to treat end-stage liver disease and is in a Phase 2a clinical trial; preclinical proof-of-concept programs target thymus (aging), kidney (end-stage renal disease) and pancreas (Type 1 diabetes). LyGenesis is a laboratory and clinical-research organization, not a software vendor: it publishes no developer portal, no API documentation and no machine-readable API contract, and this profile records that absence rather than any API surface.'
layout: provider
modified: '2026-08-25'
name: LyGenesis
nav: Providers
network: true
overview: 'LyGenesis is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Cell Therapy, Regenerative Medicine, and Life Sciences.


  LyGenesis'' developer surface includes support, engineering blog, and 6 more developer resources.'
random_paper: 13
screenshot: https://raw.githubusercontent.com/api-evangelist/lygenesis/refs/heads/main/screenshots/lygenesis-2026-09-02T150338.png
security:
- kind: domain-security
  name: Lygenesis Domain Security
  slug: lygenesis-domain-security
  summary_line: TLSv1.3 · HSTS
slug: lygenesis
tags:
- Company
- Biotechnology
- Cell Therapy
- Regenerative Medicine
- Life Sciences
- Healthcare
- Clinical Trials
- Organ Transplantation
website: https://www.lygenesis.com/
---
