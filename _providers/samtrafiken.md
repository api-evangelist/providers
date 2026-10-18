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
- description: Realtime public transport APIs provided via Trafiklab platform.
  name: Trafiklab Realtime APIs
  slug: trafiklab-realtime-apis
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/samtrafiken/refs/heads/main/hosts/samtrafiken-hosts.yml
  title: ''
  type: Hosts
  url: hosts/samtrafiken-hosts.yml
- group: company
  title: ''
  type: Newsroom
  url: https://samtrafiken.se/news/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/samtrafiken
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/samtrafiken/refs/heads/main/security/samtrafiken-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/samtrafiken-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://samtrafiken.se/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://samtrafiken.se/
  reason: no-developer-program
  state: none
created: '2026-10-15'
description: Samtrafiken i Sverige AB is a Swedish public transport collaboration platform that aggregates and distributes timetable, ticketing and service data from multiple operators. It provides open traffic data through its Trafiklab portal, enabling developers and innovators to build applications that improve sustainable travel. The organization also offers services like Resplus for combined travel solutions and supports operators with data management tools. Recent initiatives include the ARTUR project for automated schedule updates, reflecting its commitment to modernizing transport information.
image: https://samtrafiken.se/wp-content/uploads/2021/02/group-4.jpg
layout: provider
modified: '2026-10-15'
name: Samtrafiken
nav: Providers
network: true
overview: Samtrafiken is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Transport, Open Data, Sweden, and Collaboration.
random_paper: 7
score:
  band: minimal
  composite: 5.5
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 58.9
    operational_transparency: 5.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 5.9
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Samtrafiken Domain Security
  slug: samtrafiken-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: samtrafiken
tags:
- Company
- Transport
- Open Data
- Sweden
- Collaboration
website: https://samtrafiken.se/
---
