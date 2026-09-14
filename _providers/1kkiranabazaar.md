---
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/1kkiranabazaar-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.1knetworks.in/
coverage:
  checked: '2026-09-05'
  detail: '1K Kirana Bazaar sells a franchise operating system to kirana store owners as an end-user product — a PoS, a retailer app and a consumer ordering app — and has never run a developer program: its only live site, www.1knetworks.in, is a one-page Astro build whose whole navigation is in-page anchors (#home, #platform, #cta) with no /developers, /docs or /api page to reach and no occurrence of the words API, SDK, webhook or developer in its rendered text, while the former primary domain www.1knetworks.com returns HTTP 525 on every path and each of the eleven API hosts the Wayback Machine records for it (api., api-gateway., vendor-api., wms-staging-api., go-api-staging.1knetworks.com and siblings) is NXDOMAIN today.'
  evidence:
  - status: 403
    url: https://www.1knetworks.in/
  - status: 200
    url: https://www.1knetworks.in/.well-known/security.txt
  - status: 200
    url: https://www.1knetworks.in/.well-known/agent-card.json
  - status: 403
    url: https://www.1knetworks.in/this-path-cannot-exist-xyz9-1k
  - status: 403
    url: https://www.1knetworks.in/openapi.json
  - status: 200
    url: https://www.1knetworks.in/robots.txt
  - status: 525
    url: https://www.1knetworks.com/
  - status: 525
    url: https://www.1knetworks.com/openapi.json
  - status: 200
    url: https://web.archive.org/cdx/search/cdx?url=1knetworks.com&matchType=domain
  - status: 404
    url: https://registry.npmjs.org/1knetworks
  - status: 200
    url: https://equityzen.com/company/1kkiranabazaar
  reason: no-developer-program
  state: none
created: '2026-09-05'
description: '1K Kirana Bazaar (legal entity Odicea Distribution Technologies Private Limited, also trading as 1K Networks) is a Gurugram, Haryana based Indian kirana-tech company founded in 2018 by Kumar Sangeetesh, Sachin Sharma and Abhishek Halder. It franchised neighbourhood grocery stores across Delhi NCR, Haryana, Rajasthan and Uttar Pradesh and gave them an operating stack — a point-of-sale and inventory system, direct FMCG sourcing through its own B2B distribution network, store-level analytics, payments, the Farm Gold private label, the OneClub loyalty programme, and a consumer ordering app that turned the store into a local fulfilment point. At its peak the company reported around 1,000 partner stores, more than a million customers and coverage of 25-plus districts, and it raised roughly $36-44 million across seed, Series A ($7M, 2021), Series B ($25M, 2022) and a 2023 bridge round from Info Edge Ventures, Falcon Edge Capital, Alpha Wave Global and Quiet Capital. Operations all
  but stopped in May 2024 amid a funding shortfall and reported bankruptcy and distress-sale discussions, after headcount fell from over 1,000 to roughly 30. The company never operated a public developer program: there is no developer portal, API reference, OpenAPI or other machine-readable specification, SDK, package or webhook catalogue on any domain it controls, and the API hosts it once ran internally (api., api-gateway., vendor-api., wms-*-api., go-api-staging.1knetworks.com) are all NXDOMAIN today. The company''s own surviving web presence is the single-page marketing site at www.1knetworks.in, whose WHOIS registrant organization is Odicea Distribution Technologies Private Limited.'
layout: provider
modified: '2026-09-05'
name: 1K Kirana Bazaar
nav: Providers
network: true
overview: 1K Kirana Bazaar is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Retail, E-Commerce, Commerce, and Grocery.
random_paper: 4
security:
- kind: domain-security
  name: 1Kkiranabazaar Domain Security
  slug: 1kkiranabazaar-domain-security
  summary_line: TLSv1.3
slug: 1kkiranabazaar
tags:
- Company
- Retail
- E-Commerce
- Commerce
- Grocery
- B2B
- Supply Chain
- Distribution
- Point of Sale
- India
website: https://www.1knetworks.in/
---
