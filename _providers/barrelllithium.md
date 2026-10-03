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
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/barrelllithium/refs/heads/main/llms/barrelllithium-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/barrelllithium-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/barrelllithium/refs/heads/main/hosts/barrelllithium-hosts.yml
  title: ''
  type: Hosts
  url: hosts/barrelllithium-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/barrelllithium/refs/heads/main/vendors/barrelllithium-vendors.yml
  title: ''
  type: Vendors
  url: vendors/barrelllithium-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/barrelllithium/refs/heads/main/security/barrelllithium-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/barrelllithium-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.barrellenergy.com
coverage:
  checked: '2026-09-27'
  detail: API host https://api.barrellenergy.com returns no OpenAPI spec at standard paths
  evidence:
  - status: error
    url: https://api.barrellenergy.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-27'
description: Barrelllithium, operating under Barrell Energy Inc., focuses on diversified energy solutions including oil, natural gas, lithium brine extraction, solar power, data centers, battery storage, and carbon sequestration. The company aims to meet U.S. energy needs through expansion and diversification of energy sources, leveraging extensive projects and investments across the energy sector.
layout: provider
modified: '2026-09-27'
name: Barrelllithium
nav: Providers
network: true
overview: Barrelllithium is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Energy, Lithium, Oil and Gas, Renewable Energy, and Carbon Sequestration.
random_paper: 8
score:
  band: minimal
  composite: 3.9
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
    developer_ergonomics: 0.0
    discoverability: 51.8
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 4.9
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Barrelllithium Domain Security
  slug: barrelllithium-domain-security
  summary_line: TLSv1.3 · HSTS
slug: barrelllithium
tags:
- Energy
- Lithium
- Oil and Gas
- Renewable Energy
- Carbon Sequestration
website: https://www.barrellenergy.com
---
