---
access_model:
  confidence: high
  label: Paid (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - scopes
  - security
  trial: true
  try_now: true
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 2.5
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 5
common:
- group: other
  href: https://artifacts.apis.io/iternio/hosts/iternio-hosts.yml
  title: ''
  type: Hosts
  url: hosts/iternio-hosts.yml
- group: other
  href: https://artifacts.apis.io/iternio/vendors/iternio-vendors.yml
  title: ''
  type: Vendors
  url: vendors/iternio-vendors.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dev.abetterrouteplanner.com/
- group: auth
  href: https://artifacts.apis.io/iternio/security/iternio-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/iternio-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://abetterrouteplanner.com/
- group: docs
  title: ''
  type: Documentation
  url: https://abetterrouteplanner.com/resources/api
coverage:
  checked: '2026-10-28'
  detail: API documentation page renders a JavaScript SPA with no machine‑readable OpenAPI or other contract.
  evidence:
  - status: 200
    url: https://abetterrouteplanner.com/resources/api
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-28'
description: A Better Route Planner (Iternio) provides an advanced route planning platform for electric vehicle (EV) owners, offering real‑time navigation, charging station integration, and energy consumption forecasts. The service includes a public API that enables developers to access routing, charging point data, and vehicle telemetry, supporting integration into third‑party apps, fleet management tools, and in‑car infotainment systems. ABRP aims to simplify EV travel by optimizing routes based on battery state, charger availability, and user preferences.
image: https://abetterrouteplanner.com/icon/abrp_icon.png
layout: provider
modified: '2026-10-28'
name: A Better Route Planner (Iternio)
nav: Providers
network: true
overview: 'A Better Route Planner (Iternio) is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Electric Vehicles, Routing, and Transportation.


  A Better Route Planner (Iternio)''s developer surface includes documentation and 5 more developer resources.'
plans:
- name: Iternio Plans Pricing
  plan_count: 2
  slug: iternio-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 0
  name: Iternio Rate Limits
  slug: iternio-rate-limits
scopes:
- name: Iternio Scopes
  scope_count: 0
  slug: iternio-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 12.3
  coverage:
    artifact_dirs: 22
    catalog_earned: 30.0
    catalog_earned_first_party: 8.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.8
  facets:
    access_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 39.3
    operational_transparency: 0.0
  previous_composite: 15.1
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/iternio/iternio-2026-11-03T134117.png
security:
- kind: authentication
  name: Iternio Authentication
  slug: iternio-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Iternio Domain Security
  slug: iternio-domain-security
  summary_line: TLSv1.3 · DMARC
slug: iternio
tags:
- Company
- Electric Vehicles
- Routing
- Transportation
website: https://abetterrouteplanner.com/
---
