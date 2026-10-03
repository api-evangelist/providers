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
  href: https://raw.githubusercontent.com/api-evangelist/blue-current/refs/heads/main/llms/blue-current-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/blue-current-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/blue-current/refs/heads/main/hosts/blue-current-hosts.yml
  title: ''
  type: Hosts
  url: hosts/blue-current-hosts.yml
- group: company
  title: ''
  type: Newsroom
  url: https://bluecurrent.com/news/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/blue-current/refs/heads/main/security/blue-current-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/blue-current-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bluecurrent.com/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 403
    url: https://forgeglobal.com/blue-current_stock/
  reason: no-developer-program
  state: none
created: '2026-09-29'
description: Blue Current is a stub entry created by the API Evangelist harvest process, representing a company identified in secondary-market data sources. The entry serves as a placeholder for future enrichment, awaiting verification of its official website, detailed description, and associated API documentation. This placeholder enables the profiling pipeline to track and eventually incorporate comprehensive information about the company’s services, products, and technical interfaces as they become available.
layout: provider
modified: '2026-09-29'
name: Blue Current
nav: Providers
network: true
overview: Blue Current is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Battery, Energy, Silicon, and Startups.
random_paper: 8
score:
  band: minimal
  composite: 4.1
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
    discoverability: 53.6
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
  name: Blue Current Domain Security
  slug: blue-current-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: blue-current
tags:
- Company
- Battery
- Energy
- Silicon
- Startups
- Hayward
website: https://bluecurrent.com/
---
