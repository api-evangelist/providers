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
  scored_at: '2026-10-04'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/athena-club/refs/heads/main/hosts/athena-club-hosts.yml
  title: ''
  type: Hosts
  url: hosts/athena-club-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/athena-club/refs/heads/main/vendors/athena-club-vendors.yml
  title: ''
  type: Vendors
  url: vendors/athena-club-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/athena-club/refs/heads/main/security/athena-club-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/athena-club-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://forgeglobal.com/athena-club_stock/
created: '2026-09-26'
description: Athena Club is a private-company investment opportunity listed on the Forge Global marketplace. It represents a share class of a privately held entity, offering accredited investors a way to buy and sell equity in a secondary market. The company appears in Forge’s catalog of pre‑IPO firms, with valuation data and trading activity visible to platform users. This profile expands the stub with detailed context about its market presence and investor relevance.
layout: provider
modified: '2026-09-26'
name: Athena Club
nav: Providers
network: true
overview: Athena Club is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Private-Market, Investment, Secondary Market, Equity, and Platform.
random_paper: 14
score:
  band: minimal
  composite: 3.0
  coverage:
    artifact_dirs: 3
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
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: venue_as_website
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Athena Club Domain Security
  slug: athena-club-domain-security
  summary_line: TLSv1.3 · DMARC
slug: athena-club
tags:
- Private-Market
- Investment
- Secondary Market
- Equity
- Platform
website: https://forgeglobal.com/athena-club_stock/
---
