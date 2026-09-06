---
api_count: 0
artifact_total: 0
common:
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/katerra_stock/
coverage:
  checked: '2026-08-23'
  detail: Katerra shut down and filed Chapter 11 on 6 June 2021 and its Apollo software was sold to Builders FirstSource that September; katerra.com now answers Cloudflare error 1001 (HTTP 409) on every path and refuses a TLS handshake entirely, api/docs/developer/apollo subdomains no longer resolve, and 4,068 archived katerra.com URLs contain no developer portal, OpenAPI, Swagger or SDK — only Adobe Experience Manager site JSON such as /bin/www/projects.json — so there is no API surface to profile.
  evidence:
  - status: 409
    url: http://katerra.com/
  - status: 409
    url: http://katerra.com/openapi.json
  - status: 409
    url: http://katerra.com/.well-known/agent-card.json
  - status: 409
    url: http://katerra.com/llms.txt
  - status: 200
    url: https://api.github.com/orgs/katerrainc
  reason: defunct
  state: none
created: '2026-08-23'
description: 'Katerra was a Menlo Park, California off-site construction and building-technology company founded in 2015 by former Flextronics chief executive Michael Marks with Fritz Wolff and Jim Davidson, built on the thesis that a single vertically integrated firm could design, engineer, manufacture and assemble buildings end to end — running its own architecture practice, factories in Phoenix, Tracy and Spokane producing cross-laminated timber and prefabricated wall, floor and bathroom assemblies, and its own supply chain and general contracting arm. It raised more than $2 billion across a dozen rounds, including an $865M Series D led by the SoftBank Vision Fund in January 2018 at a valuation above $3 billion and a $200M recapitalization in December 2020 that handed SoftBank majority control. Its only software product was Katerra Apollo, announced in February 2019 as a design-to-field platform (Apollo Construct, Apollo Insight, Apollo Connect) whose launch materials promised "open API
  integration" with existing construction workflows — but Apollo was sold to Katerra''s own construction customers and never shipped a public developer portal, API reference, SDK or machine-readable specification. The insolvency of its SoftBank-backed lender Greensill Capital cost Katerra its bonding capacity, and the company shut down and filed Chapter 11 in the Southern District of Texas on 6 June 2021. Its assets were broken up: the Apollo software went to Builders FirstSource for roughly $4.5M on 9 September 2021, and the factories were sold separately. katerra.com no longer serves a site — it answers a Cloudflare error 1001 on every path and cannot complete a TLS handshake at all. This profile is retained as a historical record; there is no API surface left to catalog.'
image: https://web.archive.org/web/20190712083445id_/http://katerra.com/content/dam/katerra/www/en_us/assets/images/logo/katerra.jpg/_jcr_content/renditions/cq5dam.web.1280.1280.jpeg
layout: provider
modified: '2026-08-23'
name: Katerra
nav: Providers
network: true
overview: Katerra is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Defunct, Construction, Construction Technology, and Building Materials.
random_paper: 11
slug: katerra
tags:
- Company
- Defunct
- Construction
- Construction Technology
- Building Materials
- Modular Construction
- Prefabrication
- Manufacturing
- Real-Estate
- Supply Chain
---
