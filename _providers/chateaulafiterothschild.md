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
  href: https://raw.githubusercontent.com/api-evangelist/chateaulafiterothschild/refs/heads/main/hosts/chateaulafiterothschild-hosts.yml
  title: ''
  type: Hosts
  url: hosts/chateaulafiterothschild-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/chateaulafiterothschild/refs/heads/main/vendors/chateaulafiterothschild-vendors.yml
  title: ''
  type: Vendors
  url: vendors/chateaulafiterothschild-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/chateaulafiterothschild/refs/heads/main/security/chateaulafiterothschild-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/chateaulafiterothschild-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.lafite.com
created: '2026-10-08'
description: Château Lafite Rothschild is a historic French wine estate, part of the Domaines Barons de Rothschild group. It produces world‑renowned Bordeaux wines, operates vineyards across several appellations, and maintains a global presence through its luxury brand and heritage. The estate emphasizes terroir, tradition, and innovation in winemaking, offering tours, tastings, and a portfolio of premium wines.
layout: provider
modified: '2026-10-08'
name: Chateaulafiterothschild
nav: Providers
network: true
overview: Chateaulafiterothschild is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Wine, Luxury, Heritage, and Bordeaux.
random_paper: 16
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
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Chateaulafiterothschild Domain Security
  slug: chateaulafiterothschild-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: chateaulafiterothschild
tags:
- Company
- Wine
- Luxury
- Heritage
- Bordeaux
website: https://www.lafite.com
---
