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
  url: security/amartha-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://amartha.com/en
- group: company
  title: ''
  type: About
  url: https://amartha.com/en/about-us/
- group: company
  title: ''
  type: Blog
  url: https://amartha.com/en/blog
- group: operate
  title: ''
  type: HelpCenter
  url: https://faq.amartha.com/hc/en-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://amartha.com/en/syarat-dan-ketentuan
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://amartha.com/en/kebijakan-privasi
- group: company
  title: ''
  type: Careers
  url: https://amartha.com/en/karir
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/amartha-llms.txt
coverage:
  checked: '2026-08-06'
  detail: Amartha markets Embedded Lending and Institutional Investments to partner banks, insurers and technology companies, but neither product page publishes an integration reference — both route to an amartha.typeform.com contact form, and api./developer./docs.amartha.com do not resolve at all.
  evidence:
  - status: 200
    url: https://amartha.com/en/bisnis/embedded-lending
  - status: 200
    url: https://amartha.typeform.com/loan-channeling
  - status: 404
    url: https://amartha.com/openapi.json
  - status: 404
    url: https://amartha.com/.well-known/api-catalog
  reason: sales-gate
  state: gated
created: '2026-08-06'
description: Amartha (PT Amartha Mikro Fintek, operating as Amartha Financial Group) is an Indonesian technology company founded in 2010 that builds digital financial infrastructure for the grassroots economy, connecting micro-entrepreneurs — predominantly women running micro and small businesses in rural villages — with affordable working capital from retail and institutional funders. Its consumer and agent brands include Amartha Prosper (investment), Celengan (savings), Modal (group loans), AmarthaLink (agent network) and the AmarthaFin mobile app for payments and bill purchase, alongside two business lines — Institutional Investments and Embedded Lending — that let banks, non-bank financial institutions, insurers and technology partners channel loans to Amartha borrowers. The company is headquartered at Amartha Village in South Jakarta, and runs its social impact programs through Amartha.org.
image: https://amartha.com/logo.svg
layout: provider
modified: '2026-08-06'
name: Amartha
nav: Providers
network: true
overview: 'Amartha is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Financial-Services, Fintech, Lending, and Microfinance.


  Amartha''s developer surface includes engineering blog and 8 more developer resources.'
random_paper: 20
screenshot: https://raw.githubusercontent.com/api-evangelist/amartha/refs/heads/main/screenshots/amartha-2026-08-07T161308.png
security:
- kind: domain-security
  name: Amartha Domain Security
  slug: amartha-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: amartha
tags:
- Company
- Financial-Services
- Fintech
- Lending
- Microfinance
- Peer-to-Peer Lending
- Financial Inclusion
- Payments
- Indonesia
website: https://amartha.com/en
---
