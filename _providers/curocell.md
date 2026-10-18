---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 14.4
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/curocell/refs/heads/main/well-known/curocell-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/curocell-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/curocell/refs/heads/main/hosts/curocell-hosts.yml
  title: ''
  type: Hosts
  url: hosts/curocell-hosts.yml
- group: company
  title: ''
  type: Newsroom
  url: https://curocellbtx.com/news/
- group: other
  title: ''
  type: Leadership
  url: https://curocellbtx.com/management/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/curocell/refs/heads/main/security/curocell-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/curocell-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://curocellbtx.com
coverage:
  checked: '2026-10-12'
  detail: The Curocell website provides no developer documentation or API specifications.
  evidence:
  - status: 200
    url: https://curocellbtx.com
  reason: no-developer-program
  state: none
created: '2026-10-12'
description: Curocell is a cell therapy company that discovers and develops CAR‑T therapies for cancer, focusing on both blood and solid tumors. The firm aims to unleash the immune system through broad‑spectrum CAR‑T technologies, advancing multiple product candidates in oncology.
image: https://curocellbtx.com/logo.png
layout: provider
modified: '2026-10-12'
name: Curocell
nav: Providers
network: true
overview: Curocell is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Cell Therapy, Oncology, and CAR-T.
random_paper: 21
score:
  band: minimal
  composite: 4.7
  coverage:
    artifact_dirs: 5
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 51.8
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.8
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Curocell Domain Security
  slug: curocell-domain-security
  summary_line: TLSv1.2
slug: curocell
tags:
- Company
- Biotechnology
- Cell Therapy
- Oncology
- CAR-T
website: https://curocellbtx.com
---
