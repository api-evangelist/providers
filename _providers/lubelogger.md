---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 17.3
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
asyncapis:
- description: ''
  name: Lubelogger Webhooks
  slug: lubelogger-webhooks
common:
- group: other
  href: https://artifacts.apis.io/lubelogger/vendors/lubelogger-vendors.yml
  title: ''
  type: Vendors
  url: vendors/lubelogger-vendors.yml
- group: design
  href: https://artifacts.apis.io/lubelogger/asyncapi/lubelogger-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/lubelogger-webhooks.yml
- group: other
  href: https://artifacts.apis.io/lubelogger/hosts/lubelogger-hosts.yml
  title: ''
  type: Hosts
  url: hosts/lubelogger-hosts.yml
- group: start
  title: ''
  type: Login
  url: https://app.lubelogger.com/Login/Index
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.lubelogger.com/Installation/Getting Started
- group: docs
  title: ''
  type: Documentation
  url: https://docs.lubelogger.com/
- group: auth
  href: https://artifacts.apis.io/lubelogger/security/lubelogger-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/lubelogger-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://lubelogger.com/
coverage:
  checked: '2026-10-28'
  detail: Documentation at https://docs.lubelogger.com provides no OpenAPI or other machine‑readable contract.
  evidence:
  - status: 404
    url: https://docs.lubelogger.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: LubeLogger provides a self‑hosted, open‑source vehicle maintenance and fuel mileage tracking platform. It lets users log service records, track fuel consumption, set reminders, and view detailed analytics through a web interface. The solution is designed for enthusiasts and small fleets seeking a customizable, privacy‑focused alternative to commercial telematics services.
layout: provider
modified: '2026-10-28'
name: LubeLogger
nav: Providers
network: true
overview: 'LubeLogger is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Open Source, Vehicle Maintenance, FuelTracking, and Self-Hosted.


  The LubeLogger catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  LubeLogger''s developer surface includes getting-started guide, documentation, and 6 more developer resources.'
random_paper: 8
score:
  band: emerging
  composite: 18.5
  coverage:
    artifact_dirs: 10
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.3
  facets:
    access_clarity: 6.6
    contract_governance: 0.0
    contract_quality: 39.0
    developer_ergonomics: 16.7
    discoverability: 44.6
    operational_transparency: 7.9
  previous_composite: 20.8
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/lubelogger/lubelogger-2026-11-03T135102.png
security:
- kind: domain-security
  name: Lubelogger Domain Security
  slug: lubelogger-domain-security
  summary_line: TLSv1.2 · DMARC
slug: lubelogger
tags:
- Company
- Open Source
- Vehicle Maintenance
- FuelTracking
- Self-Hosted
website: https://lubelogger.com/
---
