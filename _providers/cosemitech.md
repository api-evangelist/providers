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
- description: Semiconductor API (none documented)
  name: Cosemitech API
  slug: cosemitech-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cosemitech/refs/heads/main/hosts/cosemitech-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cosemitech-hosts.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cosemitech/refs/heads/main/security/cosemitech-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cosemitech-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.cosemitech.com
coverage:
  checked: '2026-10-11'
  detail: OpenAPI endpoint returns HTML page with no machine‑readable spec
  evidence:
  - status: 200
    url: https://www.cosemitech.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-11'
description: Cosemitech (意瑞半导体（上海）有限公司) is a high‑tech semiconductor solutions provider founded in 2014, designing and producing sensing and control ICs such as Hall switches, current sensors, linear Hall and speed sensor ICs for automotive, industrial, energy and consumer electronics markets. The company has shipped over 700 million units to more than 300 global customers, offering high‑performance, reliable and functional‑safety‑focused products.
layout: provider
modified: '2026-10-11'
name: Cosemitech
nav: Providers
network: true
overview: Cosemitech is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Semiconductors, IC, Automotive, Industrial, and Energy.
random_paper: 4
score:
  band: minimal
  composite: 4.1
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
  name: Cosemitech Domain Security
  slug: cosemitech-domain-security
  summary_line: TLSv1.2 · DMARC
slug: cosemitech
tags:
- Semiconductors
- IC
- Automotive
- Industrial
- Energy
- Consumer Electronics
- Company
website: https://www.cosemitech.com
---
