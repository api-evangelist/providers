---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  - security
  trial: false
  try_now: false
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
api_count: 1
apis:
- description: API documentation for openWB
  name: openWB API
  slug: openwb-api
artifact_total: 6
common:
- group: other
  href: https://artifacts.apis.io/openwb/hosts/openwb-hosts.yml
  title: ''
  type: Hosts
  url: hosts/openwb-hosts.yml
- group: operate
  title: ''
  type: Support
  url: https://openwb.de/main/support/
- group: auth
  href: https://artifacts.apis.io/openwb/security/openwb-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/openwb-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://openwb.de/
coverage:
  checked: '2026-10-28'
  detail: The provider's wiki page documents an API but provides no machine‑readable OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL spec.
  evidence:
  - status: 200
    url: https://wiki.openwb.de/doku.php?id=openwb:vc:2.2.0:api
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: openWB provides a self‑hosted, modular electric vehicle charging solution that combines a 7‑inch touchscreen controller with integrated energy management software. The system enables smart charging for households, businesses and residential property owners (WEGs), allowing users to monitor and control energy consumption, integrate photovoltaic surplus, and upgrade existing wallboxes. openWB’s open‑source approach lets installers customize and extend functionality while maintaining compliance with European charging standards.
image: https://openwb.de/main/wp-content/uploads/2025/02/logo-512x512-transparent.png
layout: provider
modified: '2026-10-28'
name: openWB (self-hosted)
nav: Providers
network: true
overview: 'openWB (self-hosted) is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Energy, EV Charging, Smart Home, and Open Source.


  openWB (self-hosted)''s developer surface includes support and 3 more developer resources.'
plans:
- name: Openwb Plans Pricing
  plan_count: 0
  slug: openwb-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 0
  name: Openwb Rate Limits
  slug: openwb-rate-limits
scopes:
- name: Openwb Scopes
  scope_count: 0
  slug: openwb-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: minimal
  composite: 7.0
  coverage:
    artifact_dirs: 21
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.5
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 57.1
    operational_transparency: 0.0
  previous_composite: 7.5
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 18.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/openwb/openwb-2026-11-03T140659.png
security:
- kind: authentication
  name: Openwb Authentication
  slug: openwb-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Openwb Domain Security
  slug: openwb-domain-security
  summary_line: TLSv1.3
slug: openwb
tags:
- Company
- Energy
- EV Charging
- Smart Home
- Open Source
- Self-Hosted
website: https://openwb.de/
---
