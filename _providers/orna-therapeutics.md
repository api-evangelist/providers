---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  - '{''url'': ''https://www.ornatx.com/'', ''status'': 301, ''note'': ''declared website redirects to https://www.lilly.com/science/subsidiaries — a different registrable domain (ornatx.com -> lilly.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
  trial: false
  try_now: false
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/orna-therapeutics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.ornatx.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/OrnaComputationTeam
- group: other
  title: ''
  type: ParentCompany
  url: https://www.lilly.com/science/subsidiaries
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ornatx
coverage:
  checked: '2026-08-26'
  detail: Orna Therapeutics is a clinical-stage RNA therapeutics developer with no software product, and since Eli Lilly's acquisition (definitive agreement announced 2026-02-09) its entire domain ornatx.com answers HTTP 301 to https://lilly.com/science/subsidiaries — every /.well-known/* path included — so the only surface it still operates is a GitHub org of 44 forked third-party RNA structure-prediction tools and one internal CodeCommit sync action, none of which is an API.
  evidence:
  - status: 301
    url: https://www.ornatx.com/
  - status: 301
    url: https://www.ornatx.com/.well-known/api-catalog
  - status: 404
    url: https://www.ornatx.com/openapi.json
  - status: 404
    url: https://www.ornatx.com/llms.txt
  - status: 200
    url: https://github.com/OrnaComputationTeam
  reason: defunct
  state: none
created: '2026-08-26'
description: 'Orna Therapeutics is a Cambridge, Massachusetts biotechnology company, founded in 2019 on research from MIT and built by MPM Capital, that engineers circular RNA (oRNA) paired with lipid nanoparticle delivery so a patient''s own body generates cell therapies — its lead program ORN-252 is a CD19-targeting in vivo CAR-T designed for B-cell-driven autoimmune disease. Orna acquired ReNAgade Therapeutics in 2024, combining its circular RNA platform with ReNAgade''s LNP delivery and RNA editing capabilities, and Eli Lilly announced a definitive agreement to acquire Orna on 2026-02-09 for up to $2.4B. Orna is a therapeutics developer, not a software vendor: it publishes no API, developer portal, SDK or machine-readable contract, and as of this profile its own domain ornatx.com redirects in whole to Eli Lilly''s subsidiaries page.'
layout: provider
modified: '2026-08-26'
name: Orna Therapeutics
nav: Providers
network: true
overview: Orna Therapeutics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Therapeutics, RNA, and Life Sciences.
random_paper: 10
screenshot: https://raw.githubusercontent.com/api-evangelist/orna-therapeutics/refs/heads/main/screenshots/orna-therapeutics-2026-09-02T150857.png
security:
- kind: domain-security
  name: Orna Therapeutics Domain Security
  slug: orna-therapeutics-domain-security
  summary_line: TLSv1.3 · DMARC
slug: orna-therapeutics
tags:
- Company
- Biotechnology
- Therapeutics
- RNA
- Life Sciences
- Pharmaceuticals
- Cell Therapy
- Research
website: https://www.ornatx.com/
---
