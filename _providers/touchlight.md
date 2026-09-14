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
  url: security/touchlight-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://touchlight.com/
- group: company
  title: ''
  type: About
  url: https://touchlight.com/about-us/
- group: company
  title: ''
  type: Blog
  url: https://touchlight.com/news/
- group: company
  title: ''
  type: BlogRSS
  url: https://touchlight.com/feed/
- group: operate
  title: ''
  type: Contact
  url: https://touchlight.com/contact/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://touchlight.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://touchlight.com/privacy-policy/
- group: company
  title: ''
  type: Careers
  url: https://touchlight.com/about-us/careers/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/touchlight-llms.txt
coverage:
  checked: '2026-08-30'
  detail: 'Touchlight sells physical genetic material — GMP-grade cell-free dbDNA constructs and custom DNA manufacturing — so its only web surface is a WordPress marketing site: there is no developer portal, no /developers, /api or docs host, and the site''s own Yoast-generated llms.txt indexes only marketing pages, news posts and an "Applications" post type with no API named anywhere.'
  evidence:
  - status: 200
    url: https://touchlight.com/llms.txt
  - status: 404
    url: https://touchlight.com/developers/
  - status: 404
    url: https://touchlight.com/api/
  - status: 404
    url: https://touchlight.com/openapi.json
  - status: 404
    url: https://touchlight.com/.well-known/api-catalog
  reason: not-a-software-company
  state: none
created: '2026-08-30'
description: Touchlight is a UK-based cell-free DNA manufacturer, founded in 2007 and headquartered in Hampton, London, that produces synthetic DNA enzymatically rather than by bacterial fermentation. Its doggybone DNA (dbDNA) platform — along with mbDNA and z-dbDNA — is a cell-free, plasmid-free DNA vector used as starting material for mRNA, viral vector (AAV, lentivirus), non-viral gene therapy, gene editing and DNA vaccine programs, manufactured at what the company describes as the first GMP-licensed facility for fully cell-free enzymatic DNA. Touchlight sells physical DNA material — off-the-shelf catalogue constructs and custom RUO-to-GMP manufacturing — and operates no developer program, public API, or machine-readable API contract of any kind.
image: https://touchlight.com/wp-content/uploads/2025/07/website_meta-1.png
layout: provider
modified: '2026-08-30'
name: Touchlight
nav: Providers
network: true
overview: 'Touchlight is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Life Sciences, DNA Manufacturing, and Synthetic Biology.


  Touchlight''s developer surface includes engineering blog and 9 more developer resources.'
random_paper: 12
screenshot: https://raw.githubusercontent.com/api-evangelist/touchlight/refs/heads/main/screenshots/touchlight-2026-09-02T163947.png
security:
- kind: domain-security
  name: Touchlight Domain Security
  slug: touchlight-domain-security
  summary_line: TLSv1.3 · DMARC
slug: touchlight
tags:
- Company
- Biotechnology
- Life Sciences
- DNA Manufacturing
- Synthetic Biology
- Gene Therapy
- Vaccines
- Contract Manufacturing
website: https://touchlight.com/
---
