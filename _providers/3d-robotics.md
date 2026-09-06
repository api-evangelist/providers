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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://www.3dr.com/
- group: company
  title: ''
  type: About
  url: https://www.3dr.com/about
- group: docs
  title: ''
  type: Documentation
  url: https://docs.3dr.com/
- group: operate
  title: ''
  type: Support
  url: https://store.3dr.com/contact-us/
- group: operate
  title: ''
  type: Community
  url: https://discord.gg/E9XgqbpeGP
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://docs.3dr.com/irc/privacy-policy
- group: other
  title: ''
  type: X-Store
  url: https://store.3dr.com/
- group: other
  title: ''
  type: X-SecondaryMarket
  url: https://forgeglobal.com/3d-robotics_stock/
- group: build
  title: ''
  type: Packages
  url: packages/3d-robotics-packages.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/3d-robotics-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/3d-robotics-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/3d-robotics-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/3d-robotics-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/3d-robotics-llms.txt
coverage:
  checked: '2026-09-05'
  detail: 3DR, Inc. is an electronics manufacturer — docs.3dr.com / 3dr.wiki is a 61-page hardware knowledge base (autopilots, GNSS, telemetry, DroneCAN accessories) with no API reference, and the only machine endpoint on any 3DR host is BigCommerce's own storefront GraphQL on the store tenant, which answers 401 "GraphQL credentials were missing"; the web API the pre-2023 3D Robotics ran at api.3drobotics.com is NXDOMAIN.
  evidence:
  - status: 404
    url: https://3dr.wiki/openapi.json
  - status: 404
    url: https://docs.3dr.com/llms.txt
  - status: 404
    url: https://www.3dr.com/.well-known/api-catalog
  - status: 401
    url: https://store.3dr.com/graphql
  - status: 0
    url: https://api.3drobotics.com/
  reason: not-a-software-company
  state: none
created: '2026-09-05'
description: '3DR, Inc. is an American designer and manufacturer of electronic systems for unmanned vehicles, drones and UAVs, based in Chula Vista, California, and focused on open-source and open-hardware flight control: Control N1 / Control Zero / Pixracer Pro autopilots, Location One and ZED-F9P RTK GNSS receivers, SiK and Dualband Wi-Fi telemetry radios, DroneCAN power modules and sensors, ESCs, and an ArduRemoteID-based Remote ID module. The company states on its own site that "3DR Inc was a distinct entity before the year 2023" and does not support products sold under the earlier 3D Robotics label (Solo, Site Scan, DroneKit). Its published surface is a hardware knowledge base and a storefront; it operates no public web API.'
image: https://framerusercontent.com/assets/AIVTA0StByUN8m9CoyeXOFCN3E.jpg
layout: provider
modified: '2026-09-05'
name: 3DR
nav: Providers
network: true
overview: '3DR is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Drones, UAV, Robotics, and Hardware.


  3DR''s developer surface includes documentation, support, and 12 more developer resources.'
plans:
- name: 3D Robotics Plans Pricing
  plan_count: 0
  slug: 3d-robotics-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 0
  name: 3D Robotics Rate Limits
  slug: 3d-robotics-rate-limits
score:
  band: emerging
  composite: 13.7
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 18.4
    commercial_clarity: 18.4
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 50.0
    governance: 18.2
    operational_transparency: 0.0
  provenance:
    conformance: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-05'
security:
- kind: domain-security
  name: 3D Robotics Domain Security
  slug: 3d-robotics-domain-security
  summary_line: TLSv1.3 · HSTS
slug: 3d-robotics
tags:
- Company
- Drones
- UAV
- Robotics
- Hardware
- Autopilots
- GNSS
- Telemetry
- Electronics Manufacturing
- Open Source Hardware
website: https://www.3dr.com/
---
