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
  url: security/shoreline-biosciences-domain-security.yml
coverage:
  checked: '2026-08-27'
  detail: Shoreline Biosciences' own domain shorelinebio.com no longer serves a website — both the apex and www answer HTTP 404 with a Squarespace "Website Expired" holding page — so there is no homepage, developer area, docs host or resolvable api./docs./developer. subdomain left to profile.
  evidence:
  - status: 404
    url: https://www.shorelinebio.com/
  - status: 404
    url: https://shorelinebio.com/
  - status: 404
    url: https://www.shorelinebio.com/.well-known/agent-card.json
  - status: 404
    url: https://www.shorelinebio.com/openapi.json
  - status: 404
    url: https://www.shorelinebio.com/llms.txt
  - status: 403
    url: https://forgeglobal.com/shoreline-biosciences_stock/
  reason: defunct
  state: none
created: '2026-08-27'
description: 'Shoreline Biosciences was a San Diego, California clinical-stage biotechnology company developing off-the-shelf, allogeneic cell therapies from induced pluripotent stem cells (iPSCs), principally iPSC-derived natural killer (iNK) cells and macrophages engineered for oncology indications. It raised roughly $140M, acquired Editas Medicine''s iNK cell franchise and related gene-editing technologies in 2023, and signed collaborations with Kite Pharma (Gilead) and BeiGene with headline values above $4B. Therapeutics, not software, were the product: no developer program, API, SDK or machine-readable specification was ever published. As of this profiling pass the company''s own domain, shorelinebio.com, no longer serves a website — it answers HTTP 404 with a Squarespace "Website Expired" holding page — and the company is tracked here only as a secondary-market entity.'
layout: provider
modified: '2026-08-27'
name: Shoreline Biosciences
nav: Providers
network: true
overview: Shoreline Biosciences is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Life Sciences, Cell Therapy, and Immunotherapy.
random_paper: 10
security:
- kind: domain-security
  name: Shoreline Biosciences Domain Security
  slug: shoreline-biosciences-domain-security
  summary_line: TLSv1.3
slug: shoreline-biosciences
tags:
- Company
- Biotechnology
- Life Sciences
- Cell Therapy
- Immunotherapy
- Oncology
- Stem Cells
- Pharmaceuticals
---
