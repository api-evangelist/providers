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
  url: security/petal-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.petalcard.com/
- group: company
  title: ''
  type: Blog
  url: https://www.petalcard.com/blog
- group: operate
  title: ''
  type: Support
  url: https://support.petalcard.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://tilt.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://tilt.com/privacy/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/petal-llms.txt
coverage:
  checked: '2026-08-05'
  detail: Petal is a direct-to-consumer Visa card issuer whose only integration surface is the private nginx origin behind its mobile apps at api.petalcard.com, which serves a bare 404 at every documented-spec path and is not accompanied by any developer portal, reference or SDK.
  evidence:
  - status: 404
    url: https://api.petalcard.com/openapi.json
  - status: 404
    url: https://www.petalcard.com/developers
  - status: 0
    url: https://developers.petalcard.com/
  - status: 404
    url: https://www.petalcard.com/llms.txt
  - status: 200
    url: https://www.petalcard.com/sitemap.xml
  reason: no-developer-program
  state: none
created: '2026-08-05'
description: 'Petal is a New York-based consumer fintech that issues Visa credit cards aimed at people with limited or no credit history, underwriting applicants from their bank-account cash flow (its proprietary CashScore metric) rather than a traditional credit score alone. Its Petal 1, Petal 1 Rise and Petal 2 cards are issued by WebBank, and the business is now part of the Tilt family of consumer finance brands (Tilt Card, Inc., NMLS #2295169). Petal reaches customers through iOS and Android apps plus a web dashboard and help center. It is a direct-to-consumer card issuer: as of this profile it operates no developer program, publishes no API documentation, and exposes no machine-readable API contract on any of its public hosts.'
image: https://cdn.prod.website-files.com/636a6f81a287f5628189d717/6377fffaa265e3a2b2945444_petal-og%20(1).jpg
layout: provider
modified: '2026-08-05'
name: Petal
nav: Providers
network: true
overview: 'Petal is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Financial-Services, Fintech, Credit Cards, and Consumer Finance.


  Petal''s developer surface includes engineering blog, support, and 5 more developer resources.'
random_paper: 9
screenshot: https://raw.githubusercontent.com/api-evangelist/petal/refs/heads/main/screenshots/petal-2026-09-02T151111.png
security:
- kind: domain-security
  name: Petal Domain Security
  slug: petal-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: petal
tags:
- Company
- Financial-Services
- Fintech
- Credit Cards
- Consumer Finance
- Credit Building
- Lending
website: https://www.petalcard.com/
---
