---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
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
- description: Radicale is a small but powerful CalDAV (calendars, to‑do lists) and CardDAV (contacts) server offering calendar and contact synchronization via standard protocols.
  name: Radicale API
  slug: radicale-api
artifact_total: 4
common:
- group: other
  href: https://artifacts.apis.io/radicale/hosts/radicale-hosts.yml
  title: ''
  type: Hosts
  url: hosts/radicale-hosts.yml
- group: other
  href: https://artifacts.apis.io/radicale/vendors/radicale-vendors.yml
  title: ''
  type: Vendors
  url: vendors/radicale-vendors.yml
- group: build
  href: https://artifacts.apis.io/radicale/packages/radicale-packages.yml
  title: ''
  type: SDKs
  url: packages/radicale-packages.yml
- group: build
  href: https://artifacts.apis.io/radicale/packages/radicale-packages.yml
  title: ''
  type: Packages
  url: packages/radicale-packages.yml
- group: auth
  href: https://artifacts.apis.io/radicale/security/radicale-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/radicale-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://radicale.org/
coverage:
  checked: '2026-10-27'
  detail: Documentation pages render via JavaScript and provide no machine‑readable OpenAPI or other contract.
  evidence:
  - status: 200
    url: https://radicale.org/v3.html
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-27'
description: Radicale provides a simple, open-source CalDAV and CardDAV server for calendars and contacts. It is lightweight, written in Python, and aims to be easy to install and configure, supporting multiple users and authentication methods. The project focuses on interoperability with various clients and offers a straightforward solution for personal and small‑team scheduling needs.
layout: provider
modified: '2026-10-27'
name: Radicale
nav: Providers
network: true
overview: Radicale is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, CalDAV, CardDAV, Open Source, and Python.
random_paper: 5
rate_limits:
- limit_count: 0
  name: Radicale Rate Limits
  slug: radicale-rate-limits
score:
  band: minimal
  composite: 7.6
  coverage:
    artifact_dirs: 17
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 53.6
    operational_transparency: 0.0
  previous_composite: 7.6
  provenance:
    conformance: first-party
    mcp: unknown
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
screenshot: https://apis.io/screenshots/radicale/radicale-2026-11-03T141858.png
security:
- kind: authentication
  name: Radicale Authentication
  slug: radicale-authentication
  summary_line: 9 schemes
- kind: domain-security
  name: Radicale Domain Security
  slug: radicale-domain-security
  summary_line: TLSv1.3
slug: radicale
tags:
- Company
- CalDAV
- CardDAV
- Open Source
- Python
- Calendar
website: https://radicale.org/
---
