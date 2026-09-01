---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-01'
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
score:
  band: minimal
  composite: 5.0
  coverage:
    artifact_dirs: 1
    catalog_gap: 90.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 46.3
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 5.0
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
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
