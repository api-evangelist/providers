---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
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
    well_known_catalog: true
  schema_version: 0.2
  score: 7.9
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: WeaveGrid markets a partner API that lets aggregators, OEMs and device manufacturers align their software stack with electric utilities and participate in WeaveGrid-operated grid programs. The product
  name: WeaveGrid Partner API
  slug: weavegrid-partner-api
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://www.weavegrid.com/
- group: company
  title: ''
  type: Blog
  url: https://www.weavegrid.com/news
- group: operate
  title: ''
  type: Support
  url: https://www.weavegrid.com/contact
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.weavegrid.com/privacy-policy
- group: start
  title: ''
  type: Login
  url: https://charge.weavegrid.com/login
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/weavegrid
- group: auth
  title: ''
  type: DomainSecurity
  url: security/weavegrid-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/weavegrid-plans-pricing.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/weavegrid-llms.txt
coverage:
  checked: '2026-09-04'
  detail: 'WeaveGrid markets a partner API for aggregators on its partners page but publishes no reference or portal — the only route is the "Become a partner" contact form — and the FastAPI app on api.weavegrid.com keeps its own auto-generated OpenAPI document at /openapi.json and its Swagger UI at /docs behind an HTTP 401 "WWW-Authenticate: Basic" challenge, so the machine-readable contract provably exists and is simply not published.'
  evidence:
  - status: 401
    url: https://api.weavegrid.com/openapi.json
  - status: 401
    url: https://api.weavegrid.com/docs
  - status: 200
    url: https://www.weavegrid.com/partners
  - status: 404
    url: https://www.weavegrid.com/pricing
  reason: sales-gate
  state: gated
created: '2026-09-04'
description: WeaveGrid builds grid-orchestration software that lets electric utilities absorb rapid EV and distributed-energy load growth without overbuilding the distribution system. Its DISCO (Distribution-Integrated System Capacity Orchestration) platform ingests vehicle telematics and cloud-connected device data, then sends hyper-local, individualized charging and dispatch signals to EVs, home batteries, smart thermostats and other flexible loads so they respond to real constraints at the transformer, feeder and substation level. The company runs managed-charging and time-of-use programs for utilities including Pacific Gas and Electric, Dominion Energy, DTE, Xcel Energy, Baltimore Gas and Electric, Alabama Power, Ameren Illinois and Portland General Electric, and integrates directly with OEM and device partners such as Toyota, Lexus, Rivian, Hyundai, Kia, ChargePoint, Wallbox, Emporia, SolarEdge, FranklinWH and ecobee. WeaveGrid markets a partner API for aggregators, but publishes no
  public developer portal, reference or machine-readable specification.
image: https://cdn.prod.website-files.com/62c71c576987c5a343e57279/6303119bf01cad6a5d8540af_wg-meta-image.png
layout: provider
modified: '2026-09-04'
name: WeaveGrid
nav: Providers
network: true
overview: 'WeaveGrid publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Energy, Electric Utilities, Electric Vehicles, EV Charging, and Smart Grid.


  WeaveGrid''s developer surface includes engineering blog, support, and 7 more developer resources.'
plans:
- name: Weavegrid Plans Pricing
  plan_count: 0
  slug: weavegrid-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 0
  name: Weavegrid Rate Limits
  slug: weavegrid-rate-limits
score:
  band: emerging
  composite: 16.4
  coverage:
    artifact_dirs: 6
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 5.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 21.6
  schema_version: 0.18.3
  scored_at: '2026-09-04'
security:
- kind: authentication
  name: Weavegrid Authentication
  slug: weavegrid-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Weavegrid Domain Security
  slug: weavegrid-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: weavegrid
tags:
- Energy
- Electric Utilities
- Electric Vehicles
- EV Charging
- Smart Grid
- Managed Charging
- Distributed Energy Resources
- Demand Response
- Grid Orchestration
- Vehicle Telematics
- Climate Tech
- Company
website: https://www.weavegrid.com/
---
