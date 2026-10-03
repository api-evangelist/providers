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
  scored_at: '2026-10-03'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/apis-point-energy/refs/heads/main/hosts/apis-point-energy-hosts.yml
  title: ''
  type: Hosts
  url: hosts/apis-point-energy-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/apis-point-energy/refs/heads/main/vendors/apis-point-energy-vendors.yml
  title: ''
  type: Vendors
  url: vendors/apis-point-energy-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.apispoint.energy/privacy-policy/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/apis-point-energy/refs/heads/main/security/apis-point-energy-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/apis-point-energy-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.apispoint.energy/
coverage:
  checked: 2026-09-25
  detail: OpenAPI spec endpoints returned empty responses (0 bytes) with HTTP 200.
  evidence:
  - status: 200
    url: https://api.apispoint.energy/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-25'
description: Apis Point Energy is a physical commodity trading house specializing in distillate in the Northeast United States. It provides risk management solutions, hedging products priced off local terminal prices, and over‑the‑counter swaps and options on a principal‑to‑principal basis. The company serves fuel providers across the country, offering locally‑protected fuel contracts and focusing on Northeast Distillate markets.
layout: provider
modified: '2026-09-25'
name: Apis Point Energy
nav: Providers
network: true
overview: Apis Point Energy is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Energy, Trading, Distillate, and Risk Management.
random_paper: 7
score:
  band: minimal
  composite: 5.8
  coverage:
    artifact_dirs: 5
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 44.6
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 8.2
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Apis Point Energy Domain Security
  slug: apis-point-energy-domain-security
  summary_line: TLSv1.3 · DMARC
slug: apis-point-energy
tags:
- Company
- Energy
- Trading
- Distillate
- Risk Management
website: https://www.apispoint.energy/
---
