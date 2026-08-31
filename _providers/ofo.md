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
artifact_total: 1
common:
- group: build
  title: ''
  type: Packages
  url: packages/ofo-packages.yml
coverage:
  checked: '2026-08-26'
  detail: Ofo stopped operating bikes by 2020 and its own host ofo.com now refuses TCP connections on both port 80 and port 443 despite still resolving, so every /.well-known/, /openapi.json and /llms.txt probe fails to connect rather than returning a status; the company never published a developer program in the first place, and the only surviving documentation of its endpoints is third-party reverse-engineering of the private mobile-app API at one.ofo.com.
  evidence:
  - status: 0
    url: https://ofo.com/
  - status: 0
    url: https://ofo.com/openapi.json
  - status: 0
    url: https://one.ofo.com/.well-known/agent-card.json
  - status: 0
    url: https://ofobike.com/
  - status: 404
    url: https://ofo.so/.well-known/agent-card.json
  - status: 404
    url: https://api.github.com/orgs/ofo
  - status: 403
    url: https://forgeglobal.com/ofo_stock/
  reason: defunct
  state: none
created: '2026-08-26'
description: 'Ofo (Chinese: 小黄车, "little yellow bike") was a Beijing dockless bicycle-sharing company founded in 2014 by Dai Wei and four classmates from the Peking University cycling club, and launched publicly on 7 September 2015. At its 2017 peak it had deployed more than 10 million bicycles across roughly 250 cities in 20 countries, reported over 60 million monthly active users, and was valued at around US$2 billion; in March 2018 it raised an $866M round led by Alibaba. Ofo''s bikes were unlocked exclusively through its own consumer iOS and Android app. The company never operated a developer portal, never published a machine-readable API contract, and never shipped official client SDKs — the only documentation of its endpoints is third-party reverse-engineering of the private mobile-app API at one.ofo.com. Ofo withdrew from most international markets in July 2018, collapsed under a deposit-refund backlog that left more than 10 million users queuing for refunds from December 2018, and
  had ceased bike-rental operations by 2020. ofo.com is still registered through Alibaba Cloud and still resolves, but its origin refuses connections on ports 80 and 443; the historic ofo.so host dropped and was re-registered by an unrelated party in April 2025 and now serves a parked arcade-game lander. This profile is retained as a historical record; there is no API surface to enrich.'
layout: provider
modified: '2026-08-26'
name: Ofo
nav: Providers
network: true
overview: Ofo is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Defunct, Transportation, Mobility, and Micromobility.
random_paper: 9
score:
  band: minimal
  composite: 4.6
  coverage:
    artifact_dirs: 3
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
security:
- kind: domain-security
  name: Ofo Domain Security
  slug: ofo-domain-security
  summary_line: no transport/DNS hardening detected
slug: ofo
tags:
- Company
- Defunct
- Transportation
- Mobility
- Micromobility
- Bike Sharing
- Sharing Economy
- Consumer
- China
---
