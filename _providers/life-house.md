---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  - '{''url'': ''https://www.lifehousehotels.com/'', ''status'': 301, ''note'': ''declared website redirects to https://www.larkhotels.com/ — a different registrable domain (lifehousehotels.com -> larkhotels.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
  trial: false
  try_now: false
api_count: 0
artifact_total: 1
common:
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/life-house-llms.txt
- group: agent
  title: ''
  type: WellKnownProbe
  url: well-known/life-house-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/life-house-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.lifehousehotels.com/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://www.hiive.com/securities/life-house-stock
- group: other
  title: ''
  type: Successor
  url: https://www.larkhospitality.com/
- group: other
  title: ''
  type: SuccessorProduct
  url: https://www.diamo.ai/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Life-House
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/life-house-hotels
coverage:
  checked: '2026-08-25'
  detail: Life House was absorbed into the Lark Hospitality joint venture in December 2024 and its own domain lifehousehotels.com now returns HTTP 301 to www.larkhotels.com for every path, including /openapi.json and all eight /.well-known/ discovery paths; no api/developer/docs subdomain resolves in DNS, and its GitHub organization — renamed to Diamo after the revenue-management platform was spun out — holds one public repository, a fork of the third-party Numeral-js library.
  evidence:
  - status: 301
    url: https://www.lifehousehotels.com/
  - status: 403
    url: https://www.lifehousehotels.com/openapi.json
  - status: 404
    url: https://www.lifehousehotels.com/llms.txt
  - status: 404
    url: https://www.lifehousehotels.com/.well-known/agent-card.json
  - status: 404
    url: https://www.lifehousehotels.com/.well-known/security.txt
  - status: 200
    url: https://api.github.com/orgs/Life-House
  - status: 404
    url: https://www.diamo.ai/openapi.json
  - status: 200
    url: https://www.hiive.com/securities/life-house-stock
  reason: defunct
  state: none
created: '2026-08-25'
description: 'Life House was a vertically integrated hotel software, brand and management company founded in 2017 and headquartered in Miami Beach, Florida. It built its own back-of-house operating system — property management, revenue management, digital marketing and financial operations — for independent hotels, ran more than 50 properties across the United States, Mexico and Canada, and from 2021 sold the platform to third-party hoteliers. It raised over $100M from Inovia Capital, KAYAK, Tiger Global, Trinity Ventures, Sound Ventures and JLL. In December 2024 Life House combined its management portfolio with Lark Hotels to form Lark Hospitality — in which Lark holds the controlling interest — and spun its AI revenue-management platform out as Diamo. Life House never operated a public developer program: it was a consumer of hotel APIs (notably the Mews Open API) rather than a publisher of one, lifehousehotels.com now 301-redirects to larkhotels.com, no api/developer/docs subdomain resolves
  in DNS, and its GitHub organization holds a single fork of a third-party JavaScript library.'
layout: provider
modified: '2026-08-25'
name: Life House
nav: Providers
network: true
overview: Life House is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Hospitality, Hotels, Travel, and Hotel Management Software.
random_paper: 1
screenshot: https://raw.githubusercontent.com/api-evangelist/life-house/refs/heads/main/screenshots/life-house-2026-09-02T150258.png
security:
- kind: domain-security
  name: Life House Domain Security
  slug: life-house-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: life-house
tags:
- Company
- Hospitality
- Hotels
- Travel
- Hotel Management Software
- Property Management
- Revenue Management
- Real-Estate
website: https://www.lifehousehotels.com/
---
