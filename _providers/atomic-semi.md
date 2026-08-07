---
api_count: 0
artifact_total: 0
coverage:
  checked: '2026-08-06'
  detail: atomicsemi.com 301s to fab2.com, a three-page marketing site (root, /about/, /careers/) whose own sitemap.xml lists no developer surface at all; the company makes chip-fab hardware, its one software product (the Studio in-browser EDA) is used internally rather than sold, and its GitHub org holds only forks of upstream open-source EDA tools with no first-party code.
  evidence:
  - status: 301
    url: https://atomicsemi.com/
  - status: 200
    url: https://fab2.com/sitemap.xml
  - status: 404
    url: https://fab2.com/openapi.json
  - status: 404
    url: https://fab2.com/llms.txt
  - status: 404
    url: https://fab2.com/.well-known/agent-card.json
  - status: 200
    url: https://api.github.com/orgs/AtomicSemi/repos
  reason: no-developer-program
  state: none
created: '2026-08-06'
description: Atomic Semi is a semiconductor company founded in 2023 by Sam Zeloof and Jim Keller, now operating publicly as fab2 (atomicsemi.com redirects to fab2.com). It designs and manufactures semiconductor fabrication equipment and the fabs that house it — pumps, valves, sensors, actuators, chambers, heaters, gas lines and robots — with the stated goal of mass-producing small, software-defined chip fabs, a "fab fab". It runs a 120K sq ft chip fab in Austin TX (HQ), a 30K sq ft fab fab in Lockhart TX, and the original 25K sq ft garage fab in San Francisco. Its one software product, Studio (formerly Atomic Studio), is an in-browser collaborative EDA for schematic capture, layout and simulation, used internally rather than sold as a developer platform. The company publishes no API, SDK, developer portal or machine-readable specification.
layout: provider
modified: '2026-08-06'
name: Atomic Semi
nav: Providers
network: true
random_paper: 95
slug: atomic-semi
tags:
- Company
- Semiconductors
- Hardware
- Manufacturing
- Electronic Design Automation
- Chip Design
- Deep Tech
---
