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
  href: https://raw.githubusercontent.com/api-evangelist/aracan/refs/heads/main/hosts/aracan-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aracan-hosts.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aracan/refs/heads/main/security/aracan-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aracan-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aracan.co.jp
coverage:
  checked: 2026-09-25
  detail: Access to https://aracan.co.jp returns HTTP 403 Forbidden, blocking documentation.
  evidence:
  - status: 403
    url: https://aracan.co.jp
  reason: partner-login
  state: gated
created: '2026-09-25'
description: Aracan is a Nagoya, Aichi, Japan‑based company founded in 2019 that operates an e‑commerce platform dedicated to online and offline car‑sharing and vehicle matching services. The organization provides a digital marketplace designed to connect individual car owners with prospective drivers, facilitating secure peer‑to‑peer automotive transactions across the country. It competes with services such as GO2GO and Anyca, offering a platform for professionally inspected used cars and enabling users to buy, sell, or rent vehicles through its online flea market.
layout: provider
modified: '2026-09-25'
name: Aracan
nav: Providers
network: true
overview: Aracan is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Automotive, Marketplace, Car Sharing, and Japan.
random_paper: 20
score:
  band: minimal
  composite: 3.0
  coverage:
    artifact_dirs: 4
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
  name: Aracan Domain Security
  slug: aracan-domain-security
  summary_line: TLSv1.3 · DMARC
slug: aracan
tags:
- Company
- Automotive
- Marketplace
- Car Sharing
- Japan
website: https://aracan.co.jp
---
