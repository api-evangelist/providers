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
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: API for Calterah semiconductor products
  name: Calterah API
  slug: calterah-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/calterah/refs/heads/main/hosts/calterah-hosts.yml
  title: ''
  type: Hosts
  url: hosts/calterah-hosts.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/calterah/refs/heads/main/security/calterah-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/calterah-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.calterah.com/en
- group: company
  title: ''
  type: About
  url: https://www.calterah.com/en/about-calterah
coverage:
  checked: '2026-10-06'
  detail: Developer pages are rendered via JavaScript and no machine‑readable spec was found.
  evidence:
  - status: 200
    url: https://www.calterah.com/en/developer
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-06'
description: Calterah is a semiconductor company specializing in CMOS mmWave radar and ultra‑wideband SoCs for automotive, industrial, and consumer applications. It provides a portfolio of radar and UWB platforms enabling advanced driver‑assistance, smart city, and IoT solutions. The company offers detailed developer documentation, SDKs, and support for integration of its radar and digital‑key technologies into vehicles and devices.
layout: provider
modified: '2026-10-06'
name: Calterah
nav: Providers
network: true
overview: Calterah is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Semiconductors, Radar, UWB, and Automotive.
random_paper: 0
score:
  band: minimal
  composite: 4.0
  coverage:
    artifact_dirs: 6
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 53.6
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Calterah Domain Security
  slug: calterah-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
slug: calterah
tags:
- Company
- Semiconductors
- Radar
- UWB
- Automotive
website: https://www.calterah.com/en
---
