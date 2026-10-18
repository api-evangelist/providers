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
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/betsson/refs/heads/main/hosts/betsson-hosts.yml
  title: ''
  type: Hosts
  url: hosts/betsson-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/betsson/refs/heads/main/vendors/betsson-vendors.yml
  title: ''
  type: Vendors
  url: vendors/betsson-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.betssonab.com/newsroom
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/betsson/refs/heads/main/security/betsson-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/betsson-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://betssonab.com/
coverage:
  checked: '2026-10-15'
  detail: API host https://api.betssonab.com/ returned no OpenAPI or other machine-readable contract despite probing multiple common endpoints.
  evidence:
  - status: 0
    url: https://api.betssonab.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-14'
description: Betsson AB is a leading online gaming group headquartered in Stockholm, Sweden. It owns fast‑growing companies in the online gambling sector and operates across multiple markets. Betsson focuses on profitable, sustainable growth and is listed on Nasdaq Stockholm Large Cap. The group emphasizes responsible gaming, sustainability, and strong corporate governance, offering a range of betting, casino, and sports‑book services worldwide.
layout: provider
modified: '2026-10-14'
name: Betsson
nav: Providers
network: true
overview: Betsson is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Gaming, Online Gambling, Sweden, and NASDAQ.
random_paper: 18
score:
  band: minimal
  composite: 3.3
  coverage:
    artifact_dirs: 6
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 46.4
    operational_transparency: 0.0
  provenance:
    mcp: derived
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
  name: Betsson Domain Security
  slug: betsson-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: betsson
tags:
- Company
- Gaming
- Online Gambling
- Sweden
- NASDAQ
website: https://betssonab.com/
---
