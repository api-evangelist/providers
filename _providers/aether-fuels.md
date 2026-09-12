---
api_count: 0
artifact_total: 0
coverage:
  checked: '2026-09-12'
  detail: Aether Fuels is a Singapore- and Chicago-based sustainable-fuels company that sells Aether Aurora gas-to-liquid process technology and the SAF it produces; its entire web presence is a seven-page Craft CMS marketing site (home, approach, technology, about, news, careers, contact) whose own sitemap index lists no developer, docs or API section, no api./developer./docs./portal./app./data./status. subdomain of aetherfuels.com resolves in DNS at all, and every OpenAPI, APIs.json, agent-card and .well-known path probed on the one live host returns a hard 404 that a negative-control probe confirms is a real 404 and not a catch-all.
  evidence:
  - status: 200
    url: https://aetherfuels.com/
  - status: 404
    url: https://aetherfuels.com/openapi.json
  - status: 404
    url: https://aetherfuels.com/apis.json
  - status: 404
    url: https://aetherfuels.com/llms.txt
  - status: 404
    url: https://aetherfuels.com/.well-known/agent-card.json
  - status: 404
    url: https://aetherfuels.com/.well-known/security.txt
  - status: 404
    url: https://aetherfuels.com/.well-known/aether-fuels-negative-control-7f3ab91c.json
  - status: 0
    url: https://api.aetherfuels.com/
  reason: not-a-software-company
  state: none
created: '2026-09-12'
description: 'Aether Fuels is a sustainable-fuels technology company founded in April 2022 by Conor Madigan with Xora Innovation, headquartered at Republic Plaza in Singapore with a U.S. R&D center on the GTI Energy campus in the Chicago area. Its Aether Aurora process is a radically simplified gas-to-liquid route that converts waste carbon — CO2, CO, methane and other hydrocarbons from gasified biomass, municipal solid waste, biogas and industrial off-gases — into drop-in sustainable liquid fuels for aviation and ocean shipping, combining an electrified thermochemical syngas reactor, three proprietary catalysts and by-product recycling to cut capital cost and raise carbon conversion efficiency at medium plant scale. The company runs a 1.5 gallon-per-day integrated pilot line with strategic partner GTI Energy, whose technology it licenses, and is building a 1+ barrel-per-day demonstration plant; it has signed MOUs with JetBlue and FlyORO and is partnered with Aster on a first commercial
  SAF plant in Singapore. Aether Fuels sells fuel and process technology, not software: it publishes no developer program, no public API, and no machine-readable API contract of any kind.'
image: https://aetherfuels.com/android-chrome-512x512.png
layout: provider
modified: '2026-09-12'
name: Aether Fuels
nav: Providers
network: true
random_paper: 3
slug: aether-fuels
tags:
- Company
- Energy
- Sustainable Aviation Fuel
- Synthetic Fuels
- Clean Energy
- Decarbonization
- Carbon Capture and Utilization
- Climate Tech
- Chemicals
- Deep Tech
- Manufacturing
- Singapore
---
