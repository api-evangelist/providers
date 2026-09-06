---
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/vesttoo-domain-security.yml
coverage:
  checked: '2026-09-02'
  detail: Vesttoo was liquidated in Chapter 11 (plan effective April 2024) and its domain now publishes MX and TXT records but no A, AAAA or CNAME, so vesttoo.com has no web host at all and every HTTPS probe fails at connection setup rather than returning a page.
  evidence:
  - status: 0
    url: https://vesttoo.com/
  - status: 0
    url: https://www.vesttoo.com/
  - status: 0
    url: https://vesttoo.com/.well-known/security.txt
  - status: 0
    url: https://vesttoo.com/openapi.json
  - status: 404
    url: https://api.github.com/orgs/vesttoo
  reason: defunct
  state: none
created: '2026-09-02'
description: Vesttoo Ltd. was an Israeli insurtech, founded in Tel Aviv in 2018, that operated a technology platform for insurance-linked securities and alternative risk transfer — matching insurers, reinsurers and MGAs seeking capacity with institutional investors in the capital markets, with an emphasis on non-catastrophe life and property/casualty risk. The company collapsed in 2023 after billions of dollars of counterfeit letters of credit were discovered being used as collateral on its platform. Vesttoo filed for Chapter 11 in Delaware in August 2023; a creditors' plan of liquidation was confirmed in early 2024 and went effective in April 2024, and the estate is now administered by the Vesttoo Creditors Liquidating Trust, which continues to pursue recovery litigation. The company no longer operates. Its domain publishes no web host, and no developer portal, API documentation, SDK or machine-readable contract survives at any reachable address.
layout: provider
modified: '2026-09-02'
name: Vesttoo
nav: Providers
network: true
overview: Vesttoo is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Insurance, Insurtech, Reinsurance, and Insurance-Linked Securities.
random_paper: 11
security:
- kind: domain-security
  name: Vesttoo Domain Security
  slug: vesttoo-domain-security
  summary_line: DMARC
slug: vesttoo
tags:
- Company
- Insurance
- Insurtech
- Reinsurance
- Insurance-Linked Securities
- Alternative Risk Transfer
- Capital Markets
- Financial Services
- Defunct
---
