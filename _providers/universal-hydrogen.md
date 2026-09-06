---
api_count: 0
artifact_total: 0
common:
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/universal-hydrogen
coverage:
  checked: '2026-09-02'
  detail: 'Universal Hydrogen Co. ran out of cash and shut down on 27 June 2024, and both of its web hosts are gone: hydrogen.aero and www.hydrogen.aero answer a bare HTTP 404 "Unknown site" page on the root and on every /.well-known/ and specification path despite the A record still resolving, while universalhydrogen.com has been re-pointed to a Sedo parking lander whose wildcard catch-all returns the same parking HTML with a 200 on /llms.txt and /api-docs and CHEQ bot-filter 440/441 codes elsewhere. Its real GitHub organization is still live but holds zero public repositories, api./docs./developers.hydrogen.aero do not resolve, and the Wayback archive of the domain contains no developer or specification path — the company was a hydrogen fuel-capsule and powertrain hardware business that never published an API.'
  evidence:
  - status: 404
    url: https://hydrogen.aero/
  - status: 404
    url: https://www.hydrogen.aero/
  - status: 404
    url: https://hydrogen.aero/openapi.json
  - status: 404
    url: https://hydrogen.aero/llms.txt
  - status: 404
    url: https://hydrogen.aero/.well-known/agent-card.json
  - status: 404
    url: https://hydrogen.aero/.well-known/agent.json
  - status: 404
    url: https://hydrogen.aero/.well-known/security.txt
  - status: 200
    url: https://universalhydrogen.com/
  - status: 441
    url: https://universalhydrogen.com/openapi.json
  - status: 200
    url: https://api.github.com/orgs/universal-hydrogen
  - status: 404
    url: https://registry.npmjs.org/universal-hydrogen
  reason: defunct
  state: none
created: '2026-09-02'
description: 'Universal Hydrogen Co. was a Hawthorne, California hydrogen-aviation startup founded in 2020 by former Airbus CTO Paul Eremenko to decarbonize regional air travel. Rather than building a hydrogen pipeline network, it proposed a modular capsule model: lightweight hydrogen capsules loaded into aircraft with existing cargo handling equipment, paired with fuel-cell powertrain conversion kits for regional turboprops such as the ATR 72 and De Havilland Dash 8. In March 2023 it flew a converted Dash 8-300 testbed with one propeller driven by a hydrogen fuel cell. The company raised roughly $100 million from backers including GE Aviation, American Airlines, JetBlue Ventures, Airbus Ventures, Toyota Ventures and Mitsubishi. Unable to raise further equity or debt or to find a buyer, it ceased operations on 27 June 2024 and liquidated. It was a hardware and fuel-logistics business and never shipped a public API, SDK, developer portal or machine-readable specification; its domains no longer
  serve a site.'
layout: provider
modified: '2026-09-02'
name: Universal Hydrogen
nav: Providers
network: true
overview: Universal Hydrogen is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Defunct, Aviation, Aerospace, and Hydrogen.
random_paper: 4
slug: universal-hydrogen
tags:
- Company
- Defunct
- Aviation
- Aerospace
- Hydrogen
- Clean Energy
- Fuel Cells
- Sustainability
- Decarbonization
- Hardware
- Logistics
---
