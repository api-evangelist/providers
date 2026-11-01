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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 2.5
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 5
common:
- group: other
  href: https://artifacts.apis.io/kingman-ag/hosts/kingman-ag-hosts.yml
  title: ''
  type: Hosts
  url: hosts/kingman-ag-hosts.yml
- group: other
  href: https://artifacts.apis.io/kingman-ag/vendors/kingman-ag-vendors.yml
  title: ''
  type: Vendors
  url: vendors/kingman-ag-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://kingmanag.com/privacy-policy
- group: auth
  href: https://artifacts.apis.io/kingman-ag/security/kingman-ag-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/kingman-ag-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://kingmanag.com/
- group: start
  title: ''
  type: SignUp
  url: https://dashboard.kingmanag.com/users/sign_in
coverage:
  checked: '2026-10-28'
  detail: No public developer program or API documentation was found on kingmanag.com or its subdomains.
  evidence:
  - status: 200
    url: https://kingmanag.com/
  reason: no-developer-program
  state: none
created: '2026-10-28'
description: Kingman Ag retrofits tractors you already own—any make—to run orchards and vineyards autonomously around the clock with no on‑site operators. The company maps fields, installs bolt‑on kits with cameras, RTK GPS and proprietary antennae, and then runs jobs while a monitoring team watches each machine day and night. Supported manufacturers include John Deere, New Holland, Kubota, Deutz‑Fahr and Fendt, delivering AI‑vision guidance without lidar and connectivity without towers.
image: https://www.kingmanag.com/_astro/logo-lockup.qGIiOCLz.svg
layout: provider
modified: '2026-10-28'
name: Kingman Ag
nav: Providers
network: true
overview: 'Kingman Ag is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Agriculture, Autonomous Vehicles, Tractor Retrofit, Precision Farming, and AI.


  Kingman Ag''s developer surface includes signup flow and 5 more developer resources.'
plans:
- name: Kingman Ag Plans Pricing
  plan_count: 0
  slug: kingman-ag-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 0
  name: Kingman Ag Rate Limits
  slug: kingman-ag-rate-limits
scopes:
- name: Kingman Ag Scopes
  scope_count: 0
  slug: kingman-ag-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: minimal
  composite: 10.0
  coverage:
    artifact_dirs: 19
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.2
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Kingman Ag Authentication
  slug: kingman-ag-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Kingman Ag Domain Security
  slug: kingman-ag-domain-security
  summary_line: TLSv1.3 · DMARC
slug: kingman-ag
tags:
- Agriculture
- Autonomous Vehicles
- Tractor Retrofit
- Precision Farming
- AI
website: https://kingmanag.com/
---
