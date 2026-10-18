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
- description: CellControl provides biotech data services.
  name: CellControl API
  slug: cellcontrol-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cellcontrol/refs/heads/main/hosts/cellcontrol-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cellcontrol-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cellcontrol/refs/heads/main/vendors/cellcontrol-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cellcontrol-vendors.yml
- group: other
  title: ''
  type: Leadership
  url: https://cellcontrolbio.com/team
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cellcontrol/refs/heads/main/security/cellcontrol-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cellcontrol-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cellcontrolbio.com
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://cellcontrolbio.com
  - status: 403
    url: https://equityzen.com/company/cellcontrol
  reason: no-developer-program
  state: none
created: '2026-10-07'
description: Cellcontrol is a biotechnology company developing tunable, armed in vivo CAR‑T cell therapeutics. It focuses on platform technologies for safe and potent cell therapy, offering modular solutions for oncology and hematology. The company aims to advance next‑generation cell therapies with controllable dosing and integrated payloads, targeting solid tumors and improving manufacturing efficiency.
image: http://static1.squarespace.com/static/6a0765abf0ed5f03edce2ba2/t/6a088a1d4269d7153942c3db/1778944541505/Cell_Control_transparent.png?format=1500w
layout: provider
modified: '2026-10-07'
name: Cellcontrol
nav: Providers
network: true
overview: Cellcontrol is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Biotechnology, Cell Therapy, CAR-T, Therapeutics, and Company.
random_paper: 19
score:
  band: minimal
  composite: 4.5
  coverage:
    artifact_dirs: 6
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
    discoverability: 58.9
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
  name: Cellcontrol Domain Security
  slug: cellcontrol-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
slug: cellcontrol
tags:
- Biotechnology
- Cell Therapy
- CAR-T
- Therapeutics
- Company
website: https://cellcontrolbio.com
---
