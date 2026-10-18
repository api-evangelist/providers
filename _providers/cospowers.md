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
  href: https://raw.githubusercontent.com/api-evangelist/cospowers/refs/heads/main/hosts/cospowers-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cospowers-hosts.yml
- group: company
  title: ''
  type: Newsroom
  url: https://cospowers.com/index.php/about/news/?ctype=1&keywords=&per_page=2
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cospowers/refs/heads/main/security/cospowers-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cospowers-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cospowers.com
coverage:
  checked: '2026-10-11'
  detail: The homepage returns a JavaScript shell with no machine‑readable API documentation.
  evidence:
  - status: 200
    url: https://cospowers.com
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-11'
description: Cospowers (昆宇电源) is a leading Chinese lithium‑ion battery and energy‑storage solutions provider. With over 30 years of R&D, it offers integrated storage systems for power, industrial, data‑center, residential and communication applications, aiming to be a global smart‑energy solutions leader.
layout: provider
modified: '2026-10-11'
name: Cospowers
nav: Providers
network: true
overview: Cospowers is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Energy, Storage, Lithium-Ion, and Smart Solutions.
random_paper: 7
score:
  band: minimal
  composite: 3.4
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
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 4.9
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cospowers Domain Security
  slug: cospowers-domain-security
  summary_line: TLSv1.3
slug: cospowers
tags:
- Company
- Energy
- Storage
- Lithium-Ion
- Smart Solutions
website: https://cospowers.com
---
