---
api_count: 0
artifact_total: 0
coverage:
  checked: '2026-09-12'
  detail: African Rainbow Minerals is a JSE-listed South African mining house that sells iron ore, manganese, chrome, PGMs, nickel and coal, and its only web property is a 30-page WordPress corporate/investor site (arm.co.za) whose sitemap contains no developer, docs, portal, API or integration page at all; every OpenAPI, Swagger, GraphQL, MCP, llms.txt and agent-card path probed on arm.co.za returned a hard 404 with an empty body (a random control path 404s the same way, so these are real misses and not an SPA catch-all), no api./dev./docs./developer./ portal./data./gis./geo./maps. subdomain resolves in DNS on either arm.co.za or arm-online.co.za, and the only machine-readable surface on the domain is the stock WordPress /wp-json/wp/v2 route index, which describes the CMS that renders the investor site rather than any African Rainbow Minerals product, so it was deliberately not registered as a contract.
  evidence:
  - status: 200
    url: https://arm.co.za/
  - status: 404
    url: https://arm.co.za/openapi.json
  - status: 404
    url: https://arm.co.za/swagger.json
  - status: 404
    url: https://arm.co.za/api-docs
  - status: 404
    url: https://arm.co.za/llms.txt
  - status: 404
    url: https://arm.co.za/developers
  - status: 404
    url: https://arm.co.za/.well-known/agent-card.json
  - status: 404
    url: https://arm.co.za/.well-known/agent.json
  - status: 404
    url: https://arm.co.za/.well-known/security.txt
  - status: 404
    url: https://arm.co.za/.well-known/api-catalog
  - status: 404
    url: https://arm.co.za/zz-api-evangelist-control
  - status: 200
    url: https://arm.co.za/wp-json/
  - status: 404
    url: https://www.arm-online.co.za/openapi.json
  reason: not-a-software-company
  state: none
created: '2026-09-12'
description: 'African Rainbow Minerals Limited (ARM) is a niche, diversified South African mining and minerals company, founded by Dr Patrice Motsepe and created in its present form in May 2004 through the merger of ARMgold and Harmony assets. ARM is listed on the Johannesburg Stock Exchange under the ticker ARI and is headquartered in Sandton, Gauteng. The company mines and beneficiates iron ore, manganese ore and alloys, chrome ore, platinum group metals, nickel and coal through ARM Ferrous, ARM Platinum and ARM Coal, plus a strategic gold investment in Harmony Gold Mining Company — spanning Khumani iron ore, Black Rock manganese, Two Rivers, Modikwa and Bokoni platinum, Nkomati nickel, Goedgevonden coal and Sakura Ferroalloys in Malaysia. ARM sells physical mined commodity, not software: it runs no developer program and publishes no public API, SDK, webhook or machine-readable API contract of any kind.'
image: https://arm.co.za/wp-content/themes/african_rainbow_minerals/theme-default-images/resources/arm-logo.png
layout: provider
modified: '2026-09-12'
name: African Rainbow Minerals
nav: Providers
network: true
random_paper: 6
slug: africanrainbowminerals
tags:
- Company
- Mining
- Metals and Mining
- Natural Resources
- Commodities
- Iron Ore
- Manganese
- Platinum Group Metals
- Coal
- South Africa
- Publicly Traded
---
