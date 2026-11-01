---
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
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 6.0
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/bmkg/hosts/bmkg-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bmkg-hosts.yml
- group: other
  href: https://artifacts.apis.io/bmkg/vendors/bmkg-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bmkg-vendors.yml
- group: build
  href: https://artifacts.apis.io/bmkg/packages/bmkg-packages.yml
  title: ''
  type: SDKs
  url: packages/bmkg-packages.yml
- group: build
  href: https://artifacts.apis.io/bmkg/packages/bmkg-packages.yml
  title: ''
  type: Packages
  url: packages/bmkg-packages.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://portal.bmkg.go.id
- group: auth
  href: https://artifacts.apis.io/bmkg/security/bmkg-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bmkg-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bmkg.go.id/
coverage:
  checked: '2026-10-28'
  detail: The BMKG website is a JavaScript‑rendered single‑page app with no machine‑readable API spec discovered.
  evidence:
  - status: 200
    url: https://www.bmkg.go.id/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-28'
description: The Meteorology, Climatology, and Geophysical Agency (BMKG) is the Indonesian government agency responsible for weather forecasting, climate monitoring, and geophysical observations. It provides public information on meteorological conditions, climate data, earthquake and tsunami alerts, and other geoscience services across Indonesia.
image: https://www.bmkg.go.id/images/og/default.png
layout: provider
modified: '2026-10-28'
name: BMKG
nav: Providers
network: true
overview: BMKG is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Weather, Climate, Geophysics, and Indonesia.
random_paper: 9
score:
  band: minimal
  composite: 6.8
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bmkg Domain Security
  slug: bmkg-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
slug: bmkg
tags:
- Company
- Weather
- Climate
- Geophysics
- Indonesia
website: https://bmkg.go.id/
---
