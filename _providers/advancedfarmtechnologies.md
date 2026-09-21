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
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-09-20'
api_count: 0
artifact_total: 0
coverage:
  checked: '2026-09-07'
  detail: CNH Industrial absorbed Advanced Farm on 2025-04-02 and the company's own domain advanced.farm now answers every path — including /openapi.json, /llms.txt and every /.well-known probe — with a catch-all HTTP 301 to https://agriculture.newholland.com/en-us/nar, while HTTPS on that host no longer completes a TLS handshake at all.
  evidence:
  - status: 301
    url: http://advanced.farm/openapi.json
  - status: 301
    url: http://advanced.farm/.well-known/agent-card.json
  - status: 0
    url: https://advanced.farm/
  - status: 404
    url: https://api.github.com/orgs/advanced-farm
  - status: 200
    url: https://equityzen.com/company/advancedfarmtechnologies
  reason: defunct
  state: none
created: '2026-09-07'
description: 'Advanced Farm Technologies (brand: advanced.farm) was an agricultural robotics company founded in 2017 in Davis, California, building autonomous robotic harvesters for specialty crops. Its T-6 robotic strawberry harvester and six-armed robotic apple harvester used custom rugged stereo cameras and machine-learning ripeness models to identify and pick fruit alongside human crews, and the company sold harvesting as a service rather than selling the machines. It raised roughly $34M from investors including CNH Industrial, Yamaha Motor Ventures and Catapult Ventures. On 2025-04-02 CNH Industrial acquired the company''s intellectual property and assets and the majority of its technical team joined CNH; the company no longer operates independently. Its domain, advanced.farm, now returns a blanket HTTP 301 to CNH''s New Holland Agriculture site. Advanced Farm never published a public API, developer portal, SDK or machine-readable contract.'
layout: provider
modified: '2026-09-07'
name: Advanced Farm Technologies
nav: Providers
network: true
overview: Advanced Farm Technologies is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Agriculture, Agricultural Robotics, Robotics, and Automation.
random_paper: 20
score:
  band: minimal
  composite: 4.6
  coverage:
    artifact_dirs: 1
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 46.3
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
  previous_composite: 4.6
  schema_version: 0.22.0
  scored_at: '2026-09-20'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
slug: advancedfarmtechnologies
tags:
- Company
- Agriculture
- Agricultural Robotics
- Robotics
- Automation
- Computer-Vision
- Harvesting
---
