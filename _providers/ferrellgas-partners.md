---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ferrellgas-partners-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.ferrellgas.com
- group: company
  title: ''
  type: Blog
  url: https://www.ferrellgas.com/tank-talk/
- group: operate
  title: ''
  type: Support
  url: https://www.ferrellgas.com/customer-support/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ferrellgas.com/privacy-policy/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ferrellgas-partners-lp
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/ferrellgas
coverage:
  checked: '2026-09-09'
  detail: 'Ferrellgas sells and delivers propane, not software: www.ferrellgas.com and the Blue Rhino brand site are Sitecore marketing sites with no /docs, /api-docs or /developers path and a true 404 on every discovery path, and the only API infrastructure the company runs — api.ferrellgas.com, which answers every anonymous request with HTTP 503, and bff.myferrellgas.com, the private backend-for-frontend behind the MyFerrellgas Angular account portal — is internal plumbing for its own customer app, with no published contract, no reference and no developer program of any kind.'
  evidence:
  - status: 404
    url: https://www.ferrellgas.com/openapi.json
  - status: 404
    url: https://www.ferrellgas.com/api-docs
  - status: 404
    url: https://www.ferrellgas.com/.well-known/api-catalog
  - status: 404
    url: https://bluerhino.com/openapi.json
  - status: 503
    url: https://api.ferrellgas.com/
  - status: 404
    url: https://bff.myferrellgas.com/
  - status: 200
    url: https://api.github.com/orgs/ferrellgas/repos
  reason: not-a-software-company
  state: none
created: '2026-03-24'
description: 'Ferrellgas Partners, L.P. (FGPR) is one of the largest propane distributors in the United States, selling and delivering propane to residential, commercial, industrial, agricultural, wholesale and portable tank exchange customers from a nationwide network of district locations, and operating the Blue Rhino propane tank exchange brand. Its digital surface is customer-facing rather than developer-facing: MyFerrellgas (myferrellgas.com) is an Angular single-page account portal backed by a private backend-for-frontend at bff.myferrellgas.com with Amazon Cognito sign-in, and api.ferrellgas.com resolves in DNS but answers every anonymous request with HTTP 503. As of this enrichment pass Ferrellgas publishes no developer program, no API documentation, no SDKs and no machine-readable API contract.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ferrellgas-partners.png
layout: provider
modified: '2026-09-09'
name: Ferrellgas Partners
nav: Providers
network: true
overview: 'Ferrellgas Partners is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Energy, Propane, Distribution, Fuel, and Logistics.


  Ferrellgas Partners'' developer surface includes engineering blog, support, and 5 more developer resources.'
press:
- date: '2026-05-25'
  title: Ferrellgas Partners files Form 3 initial beneficial ownership ...
  url: https://www.sahmcapital.com/news/content/ferrellgas-partners-files-form-3-initial-beneficial-ownership-statement-by-ares-management-2026-03-25
- date: '2026-05-25'
  title: Ferrellgas Partners (FGP) Posts Wider-Than-Expected Q4 ...
  url: https://finance.yahoo.com/news/ferrellgas-partners-fgp-posts-wider-133201557.html
- date: '2026-05-25'
  title: Ferrellgas Expands Descartes Routing Solution to Blue ...
  url: https://www.dcvelocity.com/articles/34608-ferrellgas-expands-descartes-routing-solution-to-blue-rhino-division-for-enhanced-customer-service
- date: '2026-05-25'
  title: Ferrellgas Partners L.P Unit (FGPR) reports earnings - Quartz
  url: https://qz.com/ferrellgas-partners-l-p-unit-fgpr-reports-earnings-1851726131
- date: '2026-05-25'
  title: 'Research Update: Ferrellgas Partners L.P. Upgrade'
  url: https://www.spglobal.com/ratings/en/regulatory/article/-/view/type/HTML/id/3458622
random_paper: 13
screenshot: https://raw.githubusercontent.com/api-evangelist/ferrellgas-partners/refs/heads/main/screenshots/ferrellgas-partners-2026-06-20T181140.png
security:
- kind: domain-security
  name: Ferrellgas Partners Domain Security
  slug: ferrellgas-partners-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ferrellgas-partners
tags:
- Energy
- Propane
- Distribution
- Fuel
- Logistics
- Retail
- Utilities
- Company
website: https://www.ferrellgas.com
---
