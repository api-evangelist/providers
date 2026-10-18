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
  href: https://raw.githubusercontent.com/api-evangelist/fifa/refs/heads/main/hosts/fifa-hosts.yml
  title: ''
  type: Hosts
  url: hosts/fifa-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/fifa/refs/heads/main/vendors/fifa-vendors.yml
  title: ''
  type: Vendors
  url: vendors/fifa-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/fifa/refs/heads/main/security/fifa-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/fifa-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.fifa.com
coverage:
  checked: '2026-10-14'
  detail: The main site https://www.fifa.com returns a JavaScript shell with no machine‑readable documentation.
  evidence:
  - status: 200
    url: https://www.fifa.com
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-13'
description: FIFA (Fédération Internationale de Football Association) is the global governing body for football (soccer), overseeing international competitions such as the FIFA World Cup, Women’s World Cup, and various youth tournaments. It sets the rules of the game, promotes the sport worldwide, and manages rankings, development programs, and commercial partnerships. The organization operates a comprehensive digital presence, offering news, match data, ticketing, and fan engagement platforms through its website and APIs.
layout: provider
modified: '2026-10-13'
name: FIFA
nav: Providers
network: true
overview: FIFA is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Sports, Football, GoverningBody, International, and Organization.
random_paper: 10
score:
  band: minimal
  composite: 3.1
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
    discoverability: 44.6
    operational_transparency: 0.0
  provenance:
    mcp: unknown
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
  name: Fifa Domain Security
  slug: fifa-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: fifa
tags:
- Sports
- Football
- GoverningBody
- International
- Organization
website: https://www.fifa.com
---
