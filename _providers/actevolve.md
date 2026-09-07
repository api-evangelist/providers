---
api_count: 0
artifact_total: 0
coverage:
  checked: '2026-09-06'
  detail: ActEvolve/VARK shut its VR platform down on 4 March 2024 and was sold outright in March 2025; vark.co.jp, corp.vark.co.jp and actevolve.com are all still registered to the company but publish no A/AAAA/CNAME record, so curl exits 6 ("could not resolve host") before any HTTP request can be made, and 1,812 archived URLs from when the sites were live contain no /api, /developers or specification path of any kind.
  evidence:
  - status: 0
    url: https://vark.co.jp/
  - status: 0
    url: https://corp.vark.co.jp/company
  - status: 0
    url: https://actevolve.com/
  - status: 404
    url: https://play.google.com/store/apps/details?id=jp.actevolve.vrpf_sp
  - status: 404
    url: https://pypi.org/pypi/actevolve/json
  - status: 200
    url: https://registry.npmjs.org/-/v1/search?text=actevolve
  - status: 200
    url: https://equityzen.com/company/actevolve/
  reason: defunct
  state: none
created: '2026-09-06'
description: 'ActEvolve Inc. (株式会社ActEvolve) was a Tokyo virtual-reality entertainment company incorporated on 9 August 2017 by Takuya Kato, a former Capcom game developer, together with other ex-game-industry engineers. In November 2018 it launched VARK, a VR live platform on which VTuber and virtual-artist performances — most visibly the long-running "Cinderella switch" series with hololive — were staged as ticketed, seat-based concerts for Meta Quest, Android and iOS, paid for with in-app VARK Coin. The company took strategic investment from KLab Inc. in August 2019, renamed itself VARK Inc. (株式会社VARK) on 1 May 2020 alongside a roughly ¥200M round from ANRI, raised a further ¥600M in May 2021, and diversified into the VARK SHORTS 3D animation tool and the STAR BLOOM liver-management agency, producing metaverse events for ANYCOLOR, Avex, KADOKAWA, COVER, Dwango, Shochiku and Meta. VARK was a consumer entertainment app rather than a platform business: it never operated a developer program,
  and no public API, SDK, webhook catalogue or machine-readable specification (OpenAPI, AsyncAPI, GraphQL SDL, MCP manifest, agent card) was published on any of its hosts at any point — 1,812 archived URLs across vark.co.jp and its subdomains contain no /api, /developers, /docs, /openapi or /graphql path of any kind. The VARK metaverse service shut down on 4 March 2024 with same-day notice, refunding unused VARK Coin until 5 May 2024 under Japan''s Payment Services Act; the free tier of VARK SHORTS ended on 30 September 2024; and in March 2025 the entire company was sold in an all-share transaction whose acquirer and terms were kept confidential, with founder Takuya Kato stepping down as representative director. This profile is retained as a historical record — there is no API surface to enrich.'
image: https://web.archive.org/web/20250209054433id_/https://corp.vark.co.jp/wp-content/themes/vark/assets/images/common/logo.svg
layout: provider
modified: '2026-09-06'
name: ActEvolve
nav: Providers
network: true
overview: ActEvolve is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Defunct, Acquired, Virtual Reality, and Metaverse.
random_paper: 3
slug: actevolve
tags:
- Company
- Defunct
- Acquired
- Virtual Reality
- Metaverse
- Entertainment
- Live Events
- VTuber
- Consumer
- Japan
---
