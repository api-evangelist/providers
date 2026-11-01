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
- description: Dashdot provides a platform for managing dashboards and visualizations.
  name: dashdot
  slug: dashdot
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/dashdot/llms/dashdot-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dashdot-llms.txt
- group: other
  href: https://artifacts.apis.io/dashdot/hosts/dashdot-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dashdot-hosts.yml
- group: other
  href: https://artifacts.apis.io/dashdot/vendors/dashdot-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dashdot-vendors.yml
- group: auth
  href: https://artifacts.apis.io/dashdot/security/dashdot-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dashdot-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://getdashdot.com/
- group: docs
  title: ''
  type: Documentation
  url: https://getdashdot.com/docs
- group: operate
  title: ''
  type: Support
  url: https://discord.gg/3teHFBNQ9W
- group: start
  title: ''
  type: Demo
  url: https://dash.mauz.dev
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/MauriceNino/dashdot
coverage:
  detail: the company publishes developer documentation but serves no machine-readable contract from it
  evidence:
  - status: 200
    url: https://getdashdot.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: Dashdot is an open-source, self‑hosted server monitoring dashboard designed for single‑node setups. It provides a lightweight, glass‑morphic UI with dynamic backgrounds, real‑time metrics, and easy Docker deployment. Ideal for developers and sysadmins seeking a simple yet powerful way to keep an eye on system health without relying on external services.
layout: provider
modified: '2026-10-28'
name: dash.
nav: Providers
network: true
overview: 'dash. is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Monitoring, OpenSource, Dashboard, Server, and SingleNode.


  dash.''s developer surface includes documentation, support, and 7 more developer resources.'
random_paper: 23
score:
  band: minimal
  composite: 7.5
  coverage:
    artifact_dirs: 8
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 53.6
    operational_transparency: 5.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Dashdot Domain Security
  slug: dashdot-domain-security
  summary_line: TLSv1.3
slug: dashdot
tags:
- Monitoring
- OpenSource
- Dashboard
- Server
- SingleNode
- Docker
website: https://getdashdot.com/
---
