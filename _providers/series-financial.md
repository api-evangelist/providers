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
artifact_total: 0
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/series-financial/refs/heads/main/hosts/series-financial-hosts.yml
  title: ''
  type: Hosts
  url: hosts/series-financial-hosts.yml
- group: company
  title: ''
  type: Website
  url: https://www.seriesfi.com/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: null
    url: https://www.seriesfi.com/
  reason: no-developer-program
  state: none
created: '2026-10-12'
description: Series Financial provides a modular, automated back‑office platform that streamlines finance and operations management for innovative teams worldwide. Their solution automates payments, global payroll, HR, contracts, treasury management, and more, delivering a unified, scalable system for modern enterprises.
layout: provider
modified: '2026-10-12'
name: Series Financial
nav: Providers
network: true
overview: Series Financial is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company.
random_paper: 1
score:
  band: minimal
  composite: 1.3
  coverage:
    artifact_dirs: 3
    catalog_earned: 20.0
    catalog_earned_first_party: 0.0
    catalog_gap: 95.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 35.7
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 0.0
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
slug: series-financial
tags:
- Company
website: https://www.seriesfi.com/
---
