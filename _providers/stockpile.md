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
  href: https://raw.githubusercontent.com/api-evangelist/stockpile/refs/heads/main/security/stockpile-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/stockpile-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.stockpile.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/StockpileInc
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/stockpile/refs/heads/main/packages/stockpile-packages.yml
  title: ''
  type: Packages
  url: packages/stockpile-packages.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/stockpile/refs/heads/main/components/stockpile-components.yml
  title: ''
  type: Components
  url: components/stockpile-components.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/stockpile/refs/heads/main/lifecycle/stockpile-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/stockpile-lifecycle.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/stockpile/refs/heads/main/llms/stockpile-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/stockpile-llms.txt
coverage:
  checked: '2026-08-29'
  detail: Stockpile closed on 2026-04-17 and moved its customers to Public, Stash and Apex; www.stockpile.com now returns 200 for a single CIMI2603-operated gift-card refund form while /fees, /developers, /api and every /.well-known/* path 404, and help., api., developer., docs. and modal.stockpile.com no longer resolve at all.
  evidence:
  - status: 200
    url: https://www.stockpile.com/
  - status: 404
    url: https://www.stockpile.com/.well-known/agent-card.json
  - status: 404
    url: https://www.stockpile.com/openapi.json
  - status: 404
    url: https://www.stockpile.com/developers
  - status: 0
    url: https://help.stockpile.com/
  reason: defunct
  state: none
created: '2026-08-29'
description: Stockpile was a Palo Alto, California consumer investing company — "the money app for families" — that let people buy, sell and gift fractional shares in stocks and ETFs, and that popularized the stock gift card, a physical or digital card redeemed into a brokerage account at Stockpile Investments, Inc. (a FINRA/SIPC member broker-dealer). Alongside custodial kid and teen accounts it sold Family Base and Family Plus subscriptions bundling debit cards and savings. The company wound down on April 17, 2026; customer accounts were moved to Public, Stash and Apex, and www.stockpile.com now serves only a Stockpile gift-card refund request form operated on the issuer's behalf by CIMI2603, Inc. Stockpile never published a public API, developer portal or machine-readable contract; its only public developer surface was an embeddable stock/brand modal, archived in 2016.
image: https://avatars.githubusercontent.com/u/5335174?v=4
layout: provider
modified: '2026-09-15'
name: Stockpile
nav: Providers
network: true
overview: Stockpile is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Financial Services, Investing, Brokerage, and Fractional Shares.
random_paper: 6
screenshot: https://raw.githubusercontent.com/api-evangelist/stockpile/refs/heads/main/screenshots/stockpile-2026-09-02T160915.png
security:
- kind: domain-security
  name: Stockpile Domain Security
  slug: stockpile-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: stockpile
tags:
- Company
- Financial Services
- Investing
- Brokerage
- Fractional Shares
- Stock Gifting
- Gift Cards
- Consumer Finance
- Defunct
website: https://www.stockpile.com/
---
