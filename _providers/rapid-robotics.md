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
  scored_at: '2026-08-30'
api_count: 0
artifact_total: 0
common:
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/robco/
coverage:
  checked: '2026-08-26'
  detail: Rapid Robotics wound down and its hardware, customers and US team were absorbed by RobCo; www.rapidrobotics.com now 302s to the Atom.com brand-name marketplace listing at atom.com/name/RapidRobotics and every developer path returns 404, and the 1,773 archived URLs from when the site was live contain no /api or /docs path at all.
  evidence:
  - status: 302
    url: https://www.rapidrobotics.com/
  - status: 404
    url: https://www.rapidrobotics.com/openapi.json
  - status: 404
    url: https://www.rapidrobotics.com/.well-known/agent-card.json
  - status: 404
    url: https://www.rapidrobotics.com/llms.txt
  - status: 403
    url: https://www.atom.com/name/RapidRobotics
  - status: 200
    url: https://apis.io/providers/robco/
  reason: defunct
  state: none
created: '2026-08-26'
description: 'Rapid Robotics was a San Francisco robotics-as-a-service (RaaS) company, founded in 2019 by Jordan Kretchmer, that rented pre-trained six-axis "Rapid Machine Operators" to small and mid-size manufacturers on a subscription — roughly $25,000 per robot per year — to cover repetitive machine-tending work such as pad printing, injection molding, heat staking, heat stamping, ultrasonic welding, pick-and-place and parts inspection. The robots shipped with grippers, computer-vision software and models pre-trained on CAD, and were set up and supervised through a proprietary no-code fleet console rather than through a developer interface. The company raised about $54.2M in total — a $12M Series A in 2021 and a $36.7M Series B co-led by Kleiner Perkins and Tiger Global — and announced partnerships with Universal Robots and Yaskawa Motoman in early 2023. Rapid Robotics subsequently wound down, and its assets — hardware, marquee customers and the US team — were acquired by Munich-based
  RaaS company RobCo, which used them to enter the US market and announced a new San Francisco headquarters on 9 September 2025. The company never published a public API, SDK, developer portal, or machine-readable specification of any kind: 1,773 unique archived URLs on rapidrobotics.com contain no /api, /apis, /docs, /developer, /graphql or /sdk path. The domain is no longer operated by the company — it is delegated to ns1/ns2.atom.com and redirects to a brand-name marketplace listing. This profile is retained in the API Evangelist network as a historical record; there is no API surface to catalog.'
layout: provider
modified: '2026-08-26'
name: Rapid Robotics
nav: Providers
network: true
overview: Rapid Robotics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Robotics, Robotics as a Service, Industrial Automation, and Manufacturing.
random_paper: 14
score:
  band: minimal
  composite: 4.6
  coverage:
    artifact_dirs: 0
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
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
slug: rapid-robotics
tags:
- Company
- Robotics
- Robotics as a Service
- Industrial Automation
- Manufacturing
- Machine Tending
- Computer-Vision
- Automation
- Defunct
- Acquired
---
