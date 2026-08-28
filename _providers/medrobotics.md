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
  scored_at: '2026-08-26'
api_count: 0
artifact_total: 0
common:
- group: other
  title: ''
  type: SecondaryMarketListing
  url: https://forgeglobal.com/medrobotics_stock/
coverage:
  checked: '2026-08-25'
  detail: Medrobotics Corporation filed Chapter 7 bankruptcy on 2022-01-24 and its plant and IP were auctioned off in June 2024; medrobotics.com is now a parked domain whose registry nameservers are NS1/NS2.PENDINGRENEWALDELETION.COM and which returns the same ~27KB parking shell with HTTP 200 for every path probed, including /docs, /api, /openapi.json and every /.well-known/ location.
  evidence:
  - status: 200
    url: https://medrobotics.com/
  - status: 200
    url: https://medrobotics.com/robots.txt
  - status: 200
    url: https://medrobotics.com/openapi.json
  - status: 200
    url: https://medrobotics.com/.well-known/api-catalog
  - status: 200
    url: https://medrobotics.com/.well-known/agent-card.json
  - status: 404
    url: https://registry.npmjs.org/medrobotics
  - status: 404
    url: https://pypi.org/pypi/medrobotics/json
  reason: defunct
  state: none
created: '2026-08-25'
description: 'Medrobotics Corporation was a Raynham, Massachusetts surgical robotics manufacturer, founded as CardioRobotics, that built the Flex Robotic System — an articulating, steerable robotic endoscope platform cleared by the FDA in 2015 and CE-marked for minimally invasive procedures in otolaryngology, colorectal surgery and gastroenterology, and deployed at roughly thirty hospitals worldwide. The company was a medical device manufacturer, not a software vendor: its product was an operating-room capital robot and its single-use accessories, and it never operated a developer program, a public API, an SDK or a developer portal. Medrobotics filed for Chapter 7 bankruptcy in the U.S. Bankruptcy Court for the District of Massachusetts on 2022-01-24 (case 1:22-bk-10077), following judgments in the Endobotics litigation, and in June 2024 the Chapter 7 trustee liquidated the entire 40,000-square-foot Raynham plant at auction — 23 complete Flex and Flex360 systems plus roughly 22 terabytes
  of technical specifications, customer lists and other intellectual property. The company is defunct. Its domain, medrobotics.com, is now a parked page served by a domain-parking network and its registry nameservers are NS1/NS2.PENDINGRENEWALDELETION.COM. This profile is retained as an honest zero: there is no API surface to catalog, and there never was one.'
layout: provider
modified: '2026-08-25'
name: Medrobotics
nav: Providers
network: true
overview: Medrobotics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Medical Devices, Surgical Robotics, Robotics, and Healthcare.
random_paper: 3
score:
  band: minimal
  composite: 1.8
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 46.3
    governance: 0.0
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 0.0
  schema_version: 0.15.0
  scored_at: '2026-08-26'
slug: medrobotics
tags:
- Company
- Medical Devices
- Surgical Robotics
- Robotics
- Healthcare
- Medical Technology
- Defunct
---
