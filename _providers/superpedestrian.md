---
api_count: 0
artifact_total: 0
common:
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Superpedestrian
coverage:
  checked: '2026-08-29'
  detail: Superpedestrian shut down US operations on 2023-12-31 and sold its European business to SURF Beyond and then ZEUS Mobility; superpedestrian.com and link.city are now domain-parking landers that return HTTP 200 with the same '<script>window.location.href="/lander"</script>' shell for every path including /openapi.json and /.well-known/agent-card.json, api./developer./docs. subdomains no longer resolve in DNS, and the historical GBFS host mds.linkyour.city is gone.
  evidence:
  - status: 200
    url: https://superpedestrian.com/
  - status: 200
    url: https://superpedestrian.com/openapi.json
  - status: 200
    url: https://superpedestrian.com/.well-known/agent-card.json
  - status: 404
    url: https://www.superpedestrian.com/
  - status: 0
    url: https://api.superpedestrian.com/
  - status: 0
    url: https://mds.linkyour.city/gbfs/gbfs.json
  - status: 200
    url: https://link.city/
  reason: defunct
  state: none
created: '2026-08-29'
description: Superpedestrian was a Cambridge, Massachusetts micromobility company founded in December 2012 by MIT Senseable City Lab co-inventor Assaf Biderman. It built the Copenhagen Wheel electric bicycle retrofit (2017) and then the LINK shared e-scooter fleet (2020), whose differentiator was an onboard Vehicle Intelligence System running self-diagnostic safety checks on every ride. It raised roughly $185M (a $60M round in December 2020 and a $125M Series C in February 2022 with Citi Impact Fund and Sony Innovation Fund) and at its 2022 peak ran shared fleets in about 57 cities across eleven US states and seven European countries. Superpedestrian closed its US operations on 31 December 2023 and auctioned more than 20,000 scooters in January 2024; the European business was sold to Norway's SURF Beyond in February 2024 and subsequently folded into ZEUS Mobility. The company published no public developer program and no machine-readable API contract. Its only known machine-readable surface
  was per-city GBFS feeds served for host cities at mds.linkyour.city, which are offline. Both superpedestrian.com and link.city are now parked domains that answer HTTP 200 to every path with a domain-parking lander, and link.city is delegated to afternic.com nameservers and listed for sale.
layout: provider
modified: '2026-08-29'
name: Superpedestrian
nav: Providers
network: true
overview: Superpedestrian is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Micromobility, Transportation, Mobility, and Electric Scooters.
random_paper: 13
slug: superpedestrian
tags:
- Company
- Micromobility
- Transportation
- Mobility
- Electric Scooters
- Shared Mobility
- Fleet Management
- Internet of Things
- Defunct
---
