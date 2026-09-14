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
  url: security/mos-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://mos.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://mos.com/service-terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://mos.com/privacy-notice/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/mos-llms.txt
coverage:
  checked: '2026-08-26'
  detail: Mos ships only a consumer scholarship-matching app — mos.com serves a marketing page plus four legal pages and nothing else; app.mos.com now 301s to the marketing site, and the one real API host, api.mos.com, is an AWS API Gateway that answers 403 Forbidden to every anonymous request including its root, so there is no developer portal, reference, spec or SDK to read.
  evidence:
  - status: 404
    url: https://mos.com/developers
  - status: 404
    url: https://mos.com/openapi.json
  - status: 403
    url: https://api.mos.com/openapi.json
  - status: 301
    url: https://app.mos.com/
  - status: 404
    url: https://mos.com/llms.txt
  reason: no-developer-program
  state: none
created: '2026-08-26'
description: 'Mos is a consumer fintech that helps students find and win money for college. Founded in 2017 by Tunisian human-rights activist Amira Yahyaoui and backed by Sequoia Capital, Lux Capital and Expa, the company began as a financial-aid application service — FAFSA filing plus human advisor support — then added a fee-free student checking account and debit card in 2021. Mos shut the banking product down and cut staff in 2023 after press and investor scrutiny of its account metrics, refocusing on its original financial-aid business. The live product at mos.com is a scholarship-matching app: students swipe through awards drawn from a database the company describes as $160 billion in available funding, with college financial-planning tools and access to a personal advisor. Sequoia''s own company page records Mos as acquired in 2025; the acquirer is not disclosed. Mos ships only an end-user consumer app — it publishes no developer portal, API documentation, SDK or machine-readable contract
  of any kind.'
image: https://mos.com/static/img/shared/phone.png
layout: provider
modified: '2026-08-26'
name: Mos
nav: Providers
network: true
overview: Mos is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Education, Higher Education, Financial Aid, and Scholarships.
random_paper: 20
screenshot: https://raw.githubusercontent.com/api-evangelist/mos/refs/heads/main/screenshots/mos-2026-09-02T150633.png
security:
- kind: domain-security
  name: Mos Domain Security
  slug: mos-domain-security
  summary_line: TLSv1.3 · DMARC
slug: mos
tags:
- Company
- Education
- Higher Education
- Financial Aid
- Scholarships
- Student Finance
- Fintech
- Consumer Finance
website: https://mos.com/
---
