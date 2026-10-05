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
  scored_at: '2026-10-04'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/ambri/refs/heads/main/hosts/ambri-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ambri-hosts.yml
- group: company
  title: ''
  type: Newsroom
  url: https://ambri.com/news/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/ambri/refs/heads/main/security/ambri-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ambri-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ambri.com
coverage:
  checked: 2026-09-24
  detail: The main site loads content via JavaScript and provides no machine‑readable API spec.
  evidence:
  - status: 200
    url: https://ambri.com
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-24'
description: Ambri develops and commercializes liquid metal battery technology for grid‑scale renewable energy storage. Founded by MIT professors, the company delivers long‑duration energy storage solutions that enable higher renewable penetration and reduce reliance on fossil‑fuel power plants. Ambri’s batteries are deployed in data centers and utility projects, and the firm has secured funding from notable investors such as Bill Gates and Total.
layout: provider
modified: '2026-09-24'
name: Ambri
nav: Providers
network: true
overview: Ambri is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Energy, Storage, Battery, and Renewables.
random_paper: 17
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
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 4.9
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Ambri Domain Security
  slug: ambri-domain-security
  summary_line: TLSv1.3
slug: ambri
tags:
- Company
- Energy
- Storage
- Battery
- Renewables
website: https://ambri.com
---
