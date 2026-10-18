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
  href: https://raw.githubusercontent.com/api-evangelist/bonnier/refs/heads/main/hosts/bonnier-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bonnier-hosts.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.bonnier.com/news
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bonnier/refs/heads/main/security/bonnier-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bonnier-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bonnier.com/
coverage:
  checked: '2026-10-15'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other contract found on discovered hosts.
  evidence:
  - status: 0
    url: https://api.bonnier.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-15'
description: 'Bonnier is a company surfaced via the API Evangelist harvest backlog (source: stockholm-trip) and added to the network as a stub for full-pipeline profiling.'
image: https://www.bonnier.com/wp-content/uploads/2025/09/Bonnierhuset-start-Lstart_L.jpg
layout: provider
modified: '2026-10-15'
name: Bonnier
nav: Providers
network: true
overview: Bonnier is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company.
random_paper: 1
score:
  band: minimal
  composite: 1.8
  coverage:
    artifact_dirs: 4
    catalog_earned: 17.0
    catalog_earned_first_party: 0.0
    catalog_gap: 98.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 32.1
    operational_transparency: 0.0
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
  name: Bonnier Domain Security
  slug: bonnier-domain-security
  summary_line: DMARC
slug: bonnier
tags:
- Company
website: https://bonnier.com/
---
