---
api_count: 0
artifact_total: 0
coverage:
  checked: '2026-09-12'
  detail: Aether Biomachines sells physical goods — RapidPrint and Ultra reinforced 3D printing filaments, and protein-based critical mineral processing — and its entire public surface is a 15-page Webflow marketing site (home, technology, products, about, two TDS download forms, three news posts, privacy, terms) whose nav and footer contain no developer, docs, portal, API or integration link at all; its Protein Function Model and "Platform + ML" team are internal, with no external access mechanism described anywhere on the site. Every REST/OpenAPI, GraphQL, MCP, agent-card, /llms.txt, /agents.md and /.well-known/ path probed on aetherbio.com and www.aetherbio.com returned a hard 404 (verified against a control path returning the identical 52,431-byte 404 body), api./developer./developers./app./platform./portal./mcp..aetherbio.com do not resolve in DNS, docs.aetherbio.com is an internal Google Drive alias that 302s to drive.google.com, and both company GitHub organizations (aetherbio, aetherbiomachines)
    contain only an abandoned 2020 static website repo, an empty placeholder and four forks of third-party ML/bio tools — no first-party SDK, contract or spec.
  evidence:
  - status: 200
    url: https://aetherbio.com/
  - status: 404
    url: https://aetherbio.com/openapi.json
  - status: 404
    url: https://aetherbio.com/swagger.json
  - status: 404
    url: https://aetherbio.com/api-docs
  - status: 404
    url: https://aetherbio.com/graphql
  - status: 404
    url: https://aetherbio.com/llms.txt
  - status: 404
    url: https://aetherbio.com/agents.md
  - status: 404
    url: https://aetherbio.com/developers
  - status: 404
    url: https://aetherbio.com/.well-known/agent-card.json
  - status: 404
    url: https://aetherbio.com/.well-known/agent.json
  - status: 404
    url: https://aetherbio.com/.well-known/api-catalog
  - status: 404
    url: https://www.aetherbio.com/.well-known/security.txt
  - status: 404
    url: https://aetherbio.com/zz-api-evangelist-control-9f3a
  reason: not-a-software-company
  state: none
created: '2026-09-12'
description: 'Aether Biomachines, Inc. (trading as Aether Bio) is a Menlo Park, California protein engineering and advanced materials company founded in 2017 by Pavle Jeremic, which operates a proprietary robotic high-throughput screening laboratory and trains a Protein Function Model on millions of micro-scale enzyme experiments in order to discover novel proteins with novel functions. The company converts that discovery platform into physical products rather than software: the RapidPrint series of reinforced nylon 3D printing filaments and the Ultra series of carbon fiber-loaded filaments for aerospace and defense additive manufacturing, with aluminum-replacing super materials and AI-designed proteins for selective extraction of lithium, nickel and rare earth elements from low-concentration brines in development. It raised a $49M Series A in 2023 and a $15M round led by Tribe Capital in December 2025. Aether Bio runs no developer program and publishes no public API, SDK, webhook surface
  or machine-readable API contract on any host it operates; its platform and machine learning work is internal to the company.'
image: https://cdn.prod.website-files.com/693839bb65b9bdaa8d3db9d2/693839bb65b9bdaa8d3dba14_Aether%20Bio_Webclip.png
layout: provider
modified: '2026-09-12'
name: Aether Biomachines
nav: Providers
network: true
random_paper: 2
slug: aetherbio
tags:
- Company
- Biotechnology
- Protein Engineering
- Synthetic Biology
- Advanced Materials
- Advanced Manufacturing
- Additive Manufacturing
- Critical Minerals
- Machine Learning
- Aerospace and Defense
---
