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
api_count: 1
apis:
- description: Agronomic data services and platform APIs for farm management.
  name: WinField United Data Silo API
  slug: winfield-united-data-silo-api
artifact_total: 5
common:
- group: other
  href: https://artifacts.apis.io/winfield-united/hosts/winfield-united-hosts.yml
  title: ''
  type: Hosts
  url: hosts/winfield-united-hosts.yml
- group: other
  href: https://artifacts.apis.io/winfield-united/vendors/winfield-united-vendors.yml
  title: ''
  type: Vendors
  url: vendors/winfield-united-vendors.yml
- group: auth
  href: https://artifacts.apis.io/winfield-united/security/winfield-united-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/winfield-united-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://winfieldunited.com/
coverage:
  checked: '2026-10-28'
  detail: Portal pages return HTML SPA without machine-readable API specifications.
  evidence:
  - status: 200
    url: https://myportal.winfieldunited.com/openapi.json
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-28'
description: WinField ® United provides agriculture solutions, products, and services—including the Data Silo platform—to help farmers make informed decisions from planning through harvest. The company offers agronomic tools, data management, and integrated software for farm operations.
image: https://storwukenticomedia.blob.core.windows.net/media/wfu/media/images/wf-logo-wt.png
layout: provider
modified: '2026-10-28'
name: WinField United Data Silo
nav: Providers
network: true
overview: WinField United Data Silo is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Agriculture, AgTech, Data, Farming, and Software.
random_paper: 8
rate_limits:
- limit_count: 0
  name: Winfield United Rate Limits
  slug: winfield-united-rate-limits
scopes:
- name: Winfield United Scopes
  scope_count: 0
  slug: winfield-united-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: minimal
  composite: 5.8
  coverage:
    artifact_dirs: 17
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Winfield United Authentication
  slug: winfield-united-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Winfield United Domain Security
  slug: winfield-united-domain-security
  summary_line: TLSv1.3 · HSTS
slug: winfield-united
tags:
- Agriculture
- AgTech
- Data
- Farming
- Software
website: https://winfieldunited.com/
---
