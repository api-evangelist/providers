---
api_count: 0
artifact_total: 0
coverage:
  checked: '2026-08-06'
  detail: Atom Power's "Atom Cloud" developer portal and API gateway are decommissioned — developers.atompower.com and api.atompower.com are still published as CNAMEs to Azure API Management, but both targets (apim-obsidian-prod-01.developer.azure-api.net and api-atompower.azure-api.net) return NXDOMAIN, so there is no reachable API, reference, or spec; the live Wix marketing site links no developer program at all.
  evidence:
  - note: 'DNS resolution failed: CNAME target apim-obsidian-prod-01.developer.azure-api.net returns NXDOMAIN'
    status: 0
    url: https://developers.atompower.com/apis
  - note: 'DNS resolution failed: CNAME target api-atompower.azure-api.net returns NXDOMAIN'
    status: 0
    url: https://api.atompower.com/
  - status: 400
    url: https://www.atompower.com/openapi.json
  - status: 400
    url: https://www.atompower.com/.well-known/agent-card.json
  - status: 200
    url: https://www.atompower.com/llms.txt
  reason: no-developer-program
  state: none
created: '2026-08-06'
description: Atom Power, Inc. is a Charlotte, North Carolina electrical technology company founded in 2014 that invented the Atom Switch, the world's first commercial UL-listed digital solid-state circuit breaker. The company builds SiC (silicon carbide) power modules, solid-state switchgear and panel-level Level 2 electric-vehicle charging hardware for commercial, industrial, data-center and grid-edge deployments, paired with cloud software for energy management, load balancing and charger operations. Atom Power previously ran an "Atom Cloud" developer portal on Azure API Management at developers.atompower.com with a gateway at api.atompower.com; both hostnames are now dangling CNAMEs to deleted Azure API Management instances, so no public API contract is currently reachable.
image: https://static.wixstatic.com/media/9b626a_6de3d6548956428a831983d5b6c5ef13%7Emv2.png/v1/fit/w_2500,h_1330,al_c/9b626a_6de3d6548956428a831983d5b6c5ef13%7Emv2.png
layout: provider
modified: '2026-08-06'
name: Atom Power
nav: Providers
network: true
random_paper: 18
slug: atom-power
tags:
- Company
- Energy
- Electric Vehicle Charging
- EV Charging
- Circuit Protection
- Solid State Circuit Breaker
- Electrical Equipment
- Energy Management
- Hardware
---
