---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: human-only
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
  score: 5.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Provides real‑time and historical EV charging station data.
  name: NOBIL API
  slug: nobil-api
artifact_total: 6
common:
- group: auth
  href: https://artifacts.apis.io/nobil/authentication/nobil-authentication.yml
  title: ''
  type: Authentication
  url: authentication/nobil-authentication.yml
- group: design
  href: https://artifacts.apis.io/nobil/lifecycle/nobil-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/nobil-lifecycle.yml
- group: other
  href: https://artifacts.apis.io/nobil/hosts/nobil-hosts.yml
  title: ''
  type: Hosts
  url: hosts/nobil-hosts.yml
- group: auth
  href: https://artifacts.apis.io/nobil/security/nobil-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/nobil-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://nobil.no/
- group: docs
  title: ''
  type: Documentation
  url: https://info.nobil.no/images/API_NOBIL_Documentation_v3_20260816.pdf
- group: docs
  title: ''
  type: APIReference
  url: https://info.nobil.no/images/API_NOBIL_Documentation_v3_20260816.pdf
- group: company
  title: ''
  type: Blog
  url: https://info.nobil.no/nyheter
- group: operate
  title: ''
  type: Support
  url: https://info.nobil.no/kontakt
coverage:
  checked: '2026-10-28'
  detail: API key request required to access the API, as indicated on the API information page.
  evidence:
  - status: 200
    url: https://info.nobil.no/api
  reason: sales-gate
  state: gated
created: '2026-10-28'
description: NOBIL (Enova) provides a comprehensive API delivering real‑time and historical data on electric vehicle charging stations across Norway and other Nordic countries. The service offers information on station locations, availability, connector types, pricing, and operational status, supporting developers building EV navigation, fleet management, and energy‑grid applications. Data is sourced from public and private operators and is updated regularly to reflect changes in infrastructure and usage.
image: https://info.nobil.no/images/liten_Nobil4-logo.jpg
layout: provider
modified: '2026-10-28'
name: NOBIL (Enova)
nav: Providers
network: true
overview: 'NOBIL (Enova) is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Electric Vehicles, Charging, Energy, Data, and Norway.


  NOBIL (Enova)''s developer surface includes authentication, documentation, API reference, engineering blog, support, and 4 more developer resources.'
plans:
- name: Nobil Plans Pricing
  plan_count: 0
  slug: nobil-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 0
  name: Nobil Rate Limits
  slug: nobil-rate-limits
scopes:
- name: Nobil Scopes
  scope_count: 0
  slug: nobil-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 12.1
  coverage:
    artifact_dirs: 21
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.3
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 57.1
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - norway
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - nordics
  previous_composite: 14.4
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 23.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/nobil/nobil-2026-11-03T140238.png
security:
- kind: authentication
  name: Nobil Authentication
  slug: nobil-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Nobil Domain Security
  slug: nobil-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: nobil
tags:
- Electric Vehicles
- Charging
- Energy
- Data
- Norway
- Transportation
website: https://nobil.no/
---
