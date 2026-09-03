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
  scored_at: '2026-09-03'
api_count: 0
artifact_total: 0
coverage:
  checked: '2026-09-02'
  detail: Vector Launch filed Chapter 11 in December 2019 and its residue was absorbed by Phantom Space on 26 February 2026, so its own host vector-launch.com is now a dormant holding domain that fails TLS name validation and returns HTTP 404 on every path — root, robots.txt, /openapi.json and all /.well-known/* — while the earlier vectorspacesystems.com brand domain has lapsed and redirects to an unrelated gambling site.
  evidence:
  - status: 404
    url: http://vector-launch.com/
  - status: 404
    url: http://vector-launch.com/robots.txt
  - status: 404
    url: http://vector-launch.com/openapi.json
  - status: 404
    url: http://vector-launch.com/llms.txt
  - status: 404
    url: http://vector-launch.com/.well-known/agent-card.json
  - status: 0
    url: https://vector-launch.com/
  - status: 200
    url: https://vectorspacesystems.com/
  - status: 404
    url: https://api.github.com/orgs/vector-launch
  - status: 404
    url: https://api.github.com/orgs/galacticsky
  - status: 429
    url: http://web.archive.org/cdx/search/cdx?url=vector-launch.com*
  - status: 403
    url: https://forgeglobal.com/vector-launch_stock/
  reason: defunct
  state: none
created: '2026-09-02'
description: 'Vector Launch, Inc. (originally Vector Space Systems) was an American small-launch and space software company founded in February 2016 in Tucson, Arizona by Jim Cantrell — an early SpaceX executive — with John Garvey, Shaun Coleman, Ken Sunshine and Eric Besnard. It acquired Garvey Spacecraft in July 2016 and developed two LOX/propylene micro-launch vehicles, the Vector-R and the larger Vector-H, aimed at a high-cadence smallsat launch market, alongside GalacticSky, a San Jose based software-defined-satellite platform that produced more than forty patents and was marketed in 2016 with a promised suite of satellite SDKs, APIs and a satellite-optimised Linux distribution called GalacticOS. Those developer surfaces were announced but never shipped publicly: Vector operated no developer portal, published no OpenAPI, AsyncAPI, GraphQL SDL or Postman collection, ran no public GitHub organisation, and distributed no client SDK to any package registry. The company raised roughly $22M
  disclosed (a $1M angel round from Shaun Coleman, then $21M in June 2017 from Sequoia Capital, Shasta Ventures and Lightspeed Venture Partners), flew suborbital prototypes from Mojave and Spaceport Camden, and won a $3.4M U.S. Air Force ASLON-45 mission in August 2019 that was cancelled days later on solvency grounds. Sequoia withdrew support in August 2019, Cantrell departed, operations halted, and Vector filed Chapter 11 in Delaware on 13 December 2019; Lockheed Martin took the GalacticSky assets by default for $4.25M when no qualified competing bid appeared, and a separate bidder took the launch-vehicle assets. A relaunched entity under Robert Spalding re-emerged on 29 October 2020, shareholders voted a wind-down in January 2021, and the residual business was finally absorbed on 26 February 2026 when Phantom Space — Jim Cantrell''s later company — acquired Vector''s remaining assets, engineering data, tooling and intellectual property to accelerate its Daytona launch vehicle. Nothing
  of Vector''s own web presence survives: vector-launch.com is a dormant GoDaddy-registered holding domain that fails TLS name validation and returns 404 on every path, and the earlier vectorspacesystems.com brand domain lapsed and now redirects off-domain to an unrelated gambling site. This profile is retained as a historical record; there is no API surface to enrich.'
layout: provider
modified: '2026-09-02'
name: Vector Launch
nav: Providers
network: true
overview: Vector Launch is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Defunct, Acquired, Aerospace, and Space.
random_paper: 16
score:
  band: minimal
  composite: 4.6
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
    operational_transparency: 0.0
  previous_composite: 4.6
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
slug: vector-launch
tags:
- Company
- Defunct
- Acquired
- Aerospace
- Space
- Launch-Services
- Small-Satellites
- Satellite
- Rockets
- Software-Defined-Satellites
- Deep-Tech
---
