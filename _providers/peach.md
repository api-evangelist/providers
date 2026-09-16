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
  href: https://raw.githubusercontent.com/api-evangelist/peach/refs/heads/main/security/peach-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/peach-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.discoverpeach.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.discoverpeach.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.discoverpeach.com/privacy
coverage:
  checked: '2026-08-26'
  detail: Peach, inc. wound down and its own homepage now carries a farewell notice ("Peach has closed its doors") pointing shoppers to Cabi Clothing, with the discoverpeach.com TLS certificate expired since 2025-08-03 and every /.well-known/ and spec path returning the storefront's 404 shell.
  evidence:
  - status: 200
    url: https://www.discoverpeach.com/
  - status: 404
    url: https://www.discoverpeach.com/openapi.json
  - status: 404
    url: https://www.discoverpeach.com/.well-known/agent-card.json
  - status: 404
    url: https://www.nasdaqprivatemarket.com/company/peach/
  reason: defunct
  state: none
created: '2026-08-26'
description: 'Peach (Peach, inc., ticker PEAC on secondary markets) was a Waltham, Massachusetts direct-sales retailer of intimate apparel, basics and athleisure for women, founded in 2013 by Janet Kraus (CEO) and Derek Ohly. It blended an in-home personal-styling experience delivered by a network of independent stylists with an online replenishment storefront at discoverpeach.com, raising roughly $10.2M before winding down. The company has since closed: its own homepage carries a farewell notice ("Peach has closed its doors") and refers customers to Cabi Clothing. Peach was a consumer retail brand, not a software vendor — it never operated a developer program, published no API documentation, and no machine-readable contract of any kind was found on its surviving surface.'
image: https://www.discoverpeach.com/assets/favicon-f5817c4c87497f7e49964de306be0d1a88c0c1a396d58bda874a36cfd59d822d.png
layout: provider
modified: '2026-09-15'
name: Peach
nav: Providers
network: true
overview: Peach is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Retail, E-Commerce, Apparel, and Direct Sales.
random_paper: 9
screenshot: https://raw.githubusercontent.com/api-evangelist/peach/refs/heads/main/screenshots/peach-2026-09-02T150926.png
security:
- kind: domain-security
  name: Peach Domain Security
  slug: peach-domain-security
  summary_line: DMARC
slug: peach
tags:
- Company
- Retail
- E-Commerce
- Apparel
- Direct Sales
- Consumer Goods
- Defunct
website: https://www.discoverpeach.com/
---
