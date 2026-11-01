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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/deimos-space-s-l-u/llms/deimos-space-s-l-u-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/deimos-space-s-l-u-llms.txt
- group: other
  href: https://artifacts.apis.io/deimos-space-s-l-u/hosts/deimos-space-s-l-u-hosts.yml
  title: ''
  type: Hosts
  url: hosts/deimos-space-s-l-u-hosts.yml
- group: other
  href: https://artifacts.apis.io/deimos-space-s-l-u/vendors/deimos-space-s-l-u-vendors.yml
  title: ''
  type: Vendors
  url: vendors/deimos-space-s-l-u-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.indragroup.com/en/news/hisdesat-gives-the-go-ahead-to-the-launch-of-the-spainsat-ng-iii-satellite
- group: auth
  href: https://artifacts.apis.io/deimos-space-s-l-u/security/deimos-space-s-l-u-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/deimos-space-s-l-u-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://space.indragroup.com/en
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://space.indragroup.com/en
  reason: no-developer-program
  state: none
created: '2026-10-23'
description: DEIMOS Space S.L.U. is a Spanish aerospace subsidiary of Indra Group, providing satellite communications, data services, and space‑based solutions. It focuses on secure, high‑throughput satellite links for government, defense, and commercial customers, offering end‑to‑end connectivity, ground stations, and managed services across Europe and globally.
layout: provider
modified: '2026-10-23'
name: DEIMOS Space S.L.U.
nav: Providers
network: true
overview: DEIMOS Space S.L.U. is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company.
random_paper: 5
score:
  band: minimal
  composite: 2.4
  coverage:
    artifact_dirs: 7
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
    discoverability: 37.5
    operational_transparency: 0.0
  provenance:
    mcp: derived
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
  name: Deimos Space S L U Domain Security
  slug: deimos-space-s-l-u-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: deimos-space-s-l-u
tags:
- Company
website: https://space.indragroup.com/en
---
