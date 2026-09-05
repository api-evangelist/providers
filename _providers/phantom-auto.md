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
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 0
common:
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/PhantomAuto
coverage:
  checked: '2026-08-26'
  detail: Phantom Auto ceased operations on 12 March 2024 and its domain phantom.auto has since lapsed entirely — public resolvers return NXDOMAIN with no NS delegation, so there is no host left to probe for a spec, docs, llms.txt or /.well-known document — while its GitHub organization's single public repository is a 2019 fork of the third-party uNetworking/uWebSockets library rather than any first-party code.
  evidence:
  - status: 0
    url: https://phantom.auto/
  - status: 200
    url: https://www.phantomauto.com/
  - status: 200
    url: https://api.github.com/orgs/phantomauto
  - status: 200
    url: https://api.github.com/repos/PhantomAuto/uWebSockets
  - status: 404
    url: https://pypi.org/pypi/phantom-auto/json
  - status: 403
    url: https://forgeglobal.com/phantom-auto_stock/
  reason: defunct
  state: none
created: '2026-08-26'
description: Phantom Auto was a Mountain View, California and Ra'anana, Israel teleoperation company founded in 2017 by Shai Magzimof (CEO) and Elliot Katz (CBO) that built a remote-driving and remote-operation platform letting a human operator monitor and drive a vehicle from thousands of miles away over bonded commercial cellular links. It launched aimed at robotaxis and self-driving trucks as a safety fallback for autonomous vehicles, then pivoted in 2019 to logistics — remotely operated forklifts and yard trucks that have no autonomy of their own, plus autonomous sidewalk delivery robots — and signed customers including Maersk, CJ Logistics, ArcBest and Serve Robotics. It raised roughly $95M in total from Bessemer Venture Partners, Maniv Mobility, InfraBridge and strategic investors ArcBest and ConGlobal, closing a $25M round in 2023, and acquired Swedish low-latency video streaming company Voysys AB in October 2022. Phantom Auto ceased operations on 12 March 2024 after a funding round
  fell through, laying off its roughly 100-120 remaining employees. The company published no developer portal, public API reference, SDK, or machine-readable specification (OpenAPI, AsyncAPI, GraphQL SDL, MCP manifest or agent card) while it operated, and its primary host phantom.auto no longer resolves in DNS at all. This profile is retained as a historical record; there is no API surface to enrich.
layout: provider
modified: '2026-08-26'
name: Phantom Auto
nav: Providers
network: true
overview: Phantom Auto is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Defunct, Teleoperation, Remote Driving, and Autonomous Vehicles.
random_paper: 6
score:
  band: minimal
  composite: 5.0
  coverage:
    artifact_dirs: 0
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
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
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
    - owner: catalog
      reason: never_enriched
  previous_composite: 5.0
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
slug: phantom-auto
tags:
- Company
- Defunct
- Teleoperation
- Remote Driving
- Autonomous Vehicles
- Logistics
- Supply Chain
- Robotics
- Warehouse Automation
- Transportation
- Mobility
---
