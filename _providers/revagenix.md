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
  url: security/revagenix-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.revagenix.com/
- group: company
  title: ''
  type: About
  url: https://www.revagenix.com/company
- group: other
  title: ''
  type: Pipeline
  url: https://www.revagenix.com/pipeline
- group: other
  title: ''
  type: Team
  url: https://www.revagenix.com/team
- group: company
  title: ''
  type: Blog
  url: https://www.revagenix.com/news
- group: operate
  title: ''
  type: Support
  url: https://www.revagenix.com/contact
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/revagenix-inc
- group: company
  title: ''
  type: Careers
  url: https://www.linkedin.com/company/revagenix-inc/jobs/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/revagenix-llms.txt
coverage:
  checked: '2026-08-26'
  detail: Revagenix is a 15-person clinical-stage biopharma whose product is Rev-56, an inhaled drug entering Phase 1 in 2026; its entire web presence is a six-page Webflow marketing site (company, pipeline, team, news, contact) with no developer section, no GitHub organization, and no api./docs./developer. subdomain in DNS.
  evidence:
  - status: 200
    url: https://www.revagenix.com/
  - status: 404
    url: https://www.revagenix.com/openapi.json
  - status: 404
    url: https://www.revagenix.com/.well-known/api-catalog
  - status: 404
    url: https://api.github.com/orgs/revagenix
  reason: not-a-software-company
  state: none
created: '2026-08-26'
description: 'Revagenix, Inc. is a private clinical-stage precision-therapeutics company headquartered in San Francisco, California, founded in 2019 by antibacterial-discovery veterans from Achaogen. The company takes a first-principles approach to drug design for serious chronic disease, engineering each candidate around target biology, route of delivery and tolerability. Its lead program, Rev-56, is a first-in-class inhaled precision therapy with a novel mechanism of action targeting chronic Pseudomonas infection in non-cystic-fibrosis bronchiectasis (NCFB), a progressive respiratory disease affecting an estimated 350,000 to 500,000 adults in the United States; Rev-56 is entering Phase 1 clinical development in 2026, with a dry-powder formulation approaching candidate selection. Revagenix is backed by Novo Holdings, Tenmile, the REPAIR Impact Fund and the National Institute of Allergy and Infectious Diseases (NIAID contract 75N93022C00061). Revagenix is a therapeutics developer, not a
  software vendor: it publishes no API, SDK, developer portal or machine-readable contract.'
image: https://cdn.prod.website-files.com/615238718d430c9069b2aa1f/6167c5a4be0897de151aaa5e_open-graph.png
layout: provider
modified: '2026-08-26'
name: Revagenix
nav: Providers
network: true
overview: 'Revagenix is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Pharmaceuticals, Life Sciences, and Therapeutics.


  Revagenix''s developer surface includes engineering blog, support, and 8 more developer resources.'
random_paper: 3
screenshot: https://raw.githubusercontent.com/api-evangelist/revagenix/refs/heads/main/screenshots/revagenix-2026-09-02T153650.png
security:
- kind: domain-security
  name: Revagenix Domain Security
  slug: revagenix-domain-security
  summary_line: TLSv1.3 · HSTS
slug: revagenix
tags:
- Company
- Biotechnology
- Pharmaceuticals
- Life Sciences
- Therapeutics
- Anti-Infectives
- Respiratory
- Clinical Stage
- Drug Discovery
- Private Company
website: https://www.revagenix.com/
---
