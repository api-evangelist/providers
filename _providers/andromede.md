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
api_count: 1
apis:
- description: Developer portal for Andromede AI platform
  name: Andromede API
  slug: andromede-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/andromede/hosts/andromede-hosts.yml
  title: ''
  type: Hosts
  url: hosts/andromede-hosts.yml
- group: other
  href: https://artifacts.apis.io/andromede/vendors/andromede-vendors.yml
  title: ''
  type: Vendors
  url: vendors/andromede-vendors.yml
- group: docs
  title: ''
  type: Documentation
  url: https://console.andromede.ai/docs
- group: start
  title: ''
  type: DeveloperPortal
  url: https://portal.andromede.ai/
- group: auth
  href: https://artifacts.apis.io/andromede/security/andromede-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/andromede-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://andromede.ai
coverage:
  checked: '2026-10-29'
  detail: Documentation pages render only via JavaScript and provide no machine‑readable spec.
  evidence:
  - status: 200
    url: https://console.andromede.ai/docs
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-29'
description: Andromede AI provides a reinforcement learning data lab that programmatically generates environments, tasks, and verifiers from real-world data. It enables scalable, repeatable post‑training evaluation pipelines for long‑horizon RL agents, targeting frontier applications. The platform operates in private beta, collaborating with partners to define next‑generation simulation environments.
layout: provider
modified: '2026-10-29'
name: Andromede
nav: Providers
network: true
overview: 'Andromede is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI, Reinforcement Learning, Data Lab, and Simulation.


  Andromede''s developer surface includes documentation and 5 more developer resources.'
random_paper: 7
score:
  band: minimal
  composite: 7.7
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
    developer_ergonomics: 19.0
    discoverability: 53.6
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Andromede Domain Security
  slug: andromede-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: andromede
tags:
- Company
- AI
- Reinforcement Learning
- Data Lab
- Simulation
- Private Beta
website: https://andromede.ai
---
