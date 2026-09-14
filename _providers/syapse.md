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
  url: security/syapse-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://syapse.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/syapse
- group: build
  title: ''
  type: Packages
  url: packages/syapse-packages.yml
coverage:
  checked: '2026-08-29'
  detail: 'Syapse was fully absorbed into N-Power Medicine (stock-for-stock, closed 2024-12-30) and its entire web property was retired the same week: syapse.com and www.syapse.com now answer every path — including an invented control path — with the identical 292-byte HTML meta-refresh stub to npowermedicine.com, Last-Modified 2025-01-12, so there is no docs host, no API host and no contract left to read.'
  evidence:
  - status: 200
    url: https://syapse.com/
  - status: 200
    url: https://syapse.com/this-path-does-not-exist-9f3a
  - status: 200
    url: https://syapse.com/openapi.json
  - status: 200
    url: https://www.syapse.com/.well-known/security.txt
  - status: 404
    url: https://www.npowermedicine.com/openapi.json
  reason: defunct
  state: none
created: '2026-08-29'
description: 'Syapse was a San Francisco precision-medicine software company, founded in 2008, that built a real-world evidence platform for community oncology. Its product integrated structured clinical data from health-system EHRs with genomic/NGS results to support molecular tumor boards, care coordination, quality improvement and life-sciences research, and it ran the Syapse Learning Health Network of community health systems alongside collaborations with Roche, Amgen and the US Department of Veterans Affairs. Syapse Holdings was acquired by N-Power Medicine in a stock-for-stock exchange that closed 2024-12-30 and was announced 2025-01-12; its network of 1,000+ community oncologists, its data and technology stack, and its team were folded into N-Power Medicine''s always-on community clinical-research model. The Syapse brand has since been fully retired: syapse.com now serves nothing but a 292-byte meta-refresh stub redirecting to npowermedicine.com, dated 2025-01-12. Syapse never published
  a public developer program, and no public API, OpenAPI/AsyncAPI/GraphQL contract, SDK or developer portal survives.'
image: https://avatars.githubusercontent.com/u/1268822?v=4
layout: provider
modified: '2026-08-29'
name: Syapse
nav: Providers
network: true
overview: Syapse is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Oncology, Precision Medicine, and Real-World Evidence.
random_paper: 10
screenshot: https://raw.githubusercontent.com/api-evangelist/syapse/refs/heads/main/screenshots/syapse-2026-09-02T161430.png
security:
- kind: domain-security
  name: Syapse Domain Security
  slug: syapse-domain-security
  summary_line: TLSv1.3 · DMARC
slug: syapse
tags:
- Company
- Healthcare
- Oncology
- Precision Medicine
- Real-World Evidence
- Clinical Research
- Health Data
- Life Sciences
- Acquired
website: https://syapse.com/
---
