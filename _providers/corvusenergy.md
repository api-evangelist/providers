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
  href: https://raw.githubusercontent.com/api-evangelist/corvusenergy/refs/heads/main/hosts/corvusenergy-hosts.yml
  title: ''
  type: Hosts
  url: hosts/corvusenergy-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://corvusenergy.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://corvusenergy.com/privacy
- group: company
  title: ''
  type: Newsroom
  url: https://corvusenergy.com/news
- group: other
  title: ''
  type: Leadership
  url: https://corvusenergy.com/about/leadership
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/corvusenergy/refs/heads/main/security/corvusenergy-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/corvusenergy-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://corvusenergy.com
coverage:
  checked: '2026-10-11'
  detail: OpenAPI spec not found at https://api.corvusenergy.com/openapi.json (404)
  evidence:
  - status: 404
    url: https://api.corvusenergy.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-11'
description: Corvus Energy, founded in 2009, provides zero‑emission energy storage solutions for the maritime industry. The company designs, manufactures and deploys battery systems that power hybrid and fully electric vessels, aiming to reduce diesel consumption and CO₂ emissions worldwide. With over 1,300 installations and more than 50% market share in maritime zero‑emission solutions, Corvus Energy serves a global customer base across shipping, offshore, and ferry sectors, delivering innovative, reliable and sustainable power.
layout: provider
modified: '2026-10-11'
name: Corvusenergy
nav: Providers
network: true
overview: Corvusenergy is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Energy, Maritime, Battery, ZeroEmission, and Cleantech.
random_paper: 4
score:
  band: minimal
  composite: 8.8
  coverage:
    artifact_dirs: 5
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 11.5
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Corvusenergy Domain Security
  slug: corvusenergy-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: corvusenergy
tags:
- Energy
- Maritime
- Battery
- ZeroEmission
- Cleantech
- Company
website: https://corvusenergy.com
---
