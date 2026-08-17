---
api_count: 1
artifact_total: 0
coverage:
  checked: '2026-08-17'
  detail: Accenta's effiPilot API reference is real and is Accenta's own — the login application at app.accenta.ai explicitly offers redirectTo=api%2Fdoc and search engines still index the page title "documentation API effiPilot 2.16.3" — but the /api/doc route is only served to an authenticated tenant session, so an anonymous GET returns {"message":"Route not found"} and no machine-readable contract of any kind (OpenAPI, GraphQL, MCP, AsyncAPI, agent card, or any /.well-known/ document) is reachable on www.accenta.ai, app.accenta.ai or demo.accenta.ai.
  evidence:
  - status: 404
    url: https://app.accenta.ai/api/doc
  - status: 200
    url: https://app.accenta.ai/api/method/brandConf
  - status: 301
    url: https://app.effipilot.com/api/doc/
  - status: 404
    url: https://app.accenta.ai/api/v3/api-docs
  - status: 404
    url: https://www.accenta.ai/.well-known/agent-card.json
  - status: 403
    url: https://app.accenta.ai/.well-known/security.txt
  reason: customer-only-docs
  state: gated
created: '2026-08-17'
description: Accenta is a French energy and carbon performance company for real estate portfolios, founded in 2016 and headquartered in Boulogne-Billancourt. It combines AI-driven building control (an intelligent building management system plus an Accenta Communication Box for sites with no BMS) with low-carbon heat and cold production built on shallow geothermal energy, inter-seasonal geostorage, heat pumps and solar, and it wraps the whole package in audit, design, build, operate, financing and performance-contract services. Accenta says it manages roughly 10 million square metres of real estate for owners such as Airbus, Prologis, Icade, Redevco and Decathlon, targeting energy reductions up to 80% and CO2 reductions up to 95%. Its software platform is effiPilot, acquired in 2020, delivered as a per-customer tenant on accenta.ai with a web application, an Android app and an HTTP API whose reference documentation sits behind the customer login.
image: https://www.accenta.ai/app/uploads/2020/09/og_fb.jpg
layout: provider
modified: '2026-08-17'
name: Accenta
nav: Providers
network: true
random_paper: 123
slug: accenta
tags:
- Company
- Ai Data
- Energy
- Buildings
- Smart Buildings
- Building Management
- Geothermal
- Decarbonization
- Sustainability
- Energy Management
- Artificial Intelligence
- Real Estate
- IoT
- France
---
