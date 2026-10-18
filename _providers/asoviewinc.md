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
  href: https://raw.githubusercontent.com/api-evangelist/asoviewinc/refs/heads/main/hosts/asoviewinc-hosts.yml
  title: ''
  type: Hosts
  url: hosts/asoviewinc-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/asoviewinc/refs/heads/main/vendors/asoviewinc-vendors.yml
  title: ''
  type: Vendors
  url: vendors/asoviewinc-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/asoviewinc/refs/heads/main/security/asoviewinc-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/asoviewinc-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.asoview.co.jp/
created: '2026-09-26'
description: ASOVIEW Inc. (アソビュー株式会社) is a Tokyo company, founded in 2011, that runs Asoview!, an online booking service for leisure activities, tours, attractions and experiences in Japan. Shares in the private company are offered on the EquityZen secondary market, which is where this record was harvested from; the company itself is not a marketplace for pre-IPO shares.
layout: provider
modified: '2026-09-26'
name: ASOVIEW Inc.
nav: Providers
network: true
overview: ASOVIEW Inc. is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Marketplace, Travel, Booking, and Activities.
random_paper: 2
score:
  band: minimal
  composite: 3.1
  coverage:
    artifact_dirs: 4
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.3
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 44.6
    operational_transparency: 0.0
  previous_composite: 3.4
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/asoviewinc/refs/heads/main/screenshots/asoviewinc-2026-10-11T100543.png
security:
- kind: domain-security
  name: Asoviewinc Domain Security
  slug: asoviewinc-domain-security
  summary_line: TLSv1.3 · DMARC
slug: asoviewinc
tags:
- Company
- Marketplace
- Travel
- Booking
- Activities
- Tourism
- Japan
website: https://www.asoview.co.jp/
---
