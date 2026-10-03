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
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/betteryeah/refs/heads/main/hosts/betteryeah-hosts.yml
  title: ''
  type: Hosts
  url: hosts/betteryeah-hosts.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/betteryeah/refs/heads/main/packages/betteryeah-packages.yml
  title: ''
  type: SDKs
  url: packages/betteryeah-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/betteryeah/refs/heads/main/packages/betteryeah-packages.yml
  title: ''
  type: Packages
  url: packages/betteryeah-packages.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/betteryeah/refs/heads/main/security/betteryeah-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/betteryeah-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://betteryeah.com
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 403
    url: https://equityzen.com/company/betteryeah
  reason: no-developer-program
  state: none
created: '2026-09-28'
description: 'Betteryeah is a company surfaced via the API Evangelist harvest backlog (source: secondary-market) and added to the network as a stub for full-pipeline profiling.'
layout: provider
modified: '2026-09-28'
name: Betteryeah
nav: Providers
network: true
overview: Betteryeah is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company.
random_paper: 13
score:
  band: minimal
  composite: 2.6
  coverage:
    artifact_dirs: 5
    catalog_earned: 15.0
    catalog_earned_first_party: 0.0
    catalog_gap: 100.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 26.8
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Betteryeah Domain Security
  slug: betteryeah-domain-security
  summary_line: DNSSEC
slug: betteryeah
tags:
- Company
website: https://betteryeah.com
---
