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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.1
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 0
common:
- group: other
  href: https://artifacts.apis.io/wg-easy/hosts/wg-easy-hosts.yml
  title: ''
  type: Hosts
  url: hosts/wg-easy-hosts.yml
- group: other
  href: https://artifacts.apis.io/wg-easy/vendors/wg-easy-vendors.yml
  title: ''
  type: Vendors
  url: vendors/wg-easy-vendors.yml
- group: company
  title: ''
  type: Website
  url: https://wg-easy.github.io/wg-easy/latest
- group: docs
  title: ''
  type: Documentation
  url: https://wg-easy.github.io/wg-easy/latest/
- group: docs
  title: ''
  type: APIReference
  url: https://wg-easy.github.io/wg-easy/latest/advanced/api/
- group: start
  title: ''
  type: GettingStarted
  url: https://wg-easy.github.io/wg-easy/latest/getting-started/
- group: operate
  title: ''
  type: Support
  url: https://wg-easy.github.io/wg-easy/latest/faq/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/wg-easy
coverage:
  checked: '2026-10-28'
  detail: Documentation provides HTML pages but no machine‑readable OpenAPI or other contract.
  evidence:
  - status: 200
    url: https://wg-easy.github.io/wg-easy/latest/advanced/api/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: wg-easy provides an easy-to-deploy WireGuard VPN solution with a web-based admin UI. It offers simple installation, client management, QR code generation, metrics, multi‑language support, 2FA, OIDC, and extensive documentation hosted at https://wg-easy.github.io/wg-easy/latest. The project is open‑source and aims to simplify secure networking for individuals and teams.
layout: provider
modified: '2026-10-28'
name: wg-easy
nav: Providers
network: true
overview: 'wg-easy is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include VPN, WireGuard, Web UI, Docker, and Open‑source.


  wg-easy''s developer surface includes documentation, API reference, getting-started guide, support, and 4 more developer resources.'
random_paper: 5
score:
  band: minimal
  composite: 9.5
  coverage:
    artifact_dirs: 5
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 33.3
    discoverability: 44.6
    operational_transparency: 5.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 0.0
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
slug: wg-easy
tags:
- VPN
- WireGuard
- Web UI
- Docker
- Open‑source
website: https://wg-easy.github.io/wg-easy/latest
---
