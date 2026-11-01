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
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/b-stock/hosts/b-stock-hosts.yml
  title: ''
  type: Hosts
  url: hosts/b-stock-hosts.yml
- group: other
  href: https://artifacts.apis.io/b-stock/vendors/b-stock-vendors.yml
  title: ''
  type: Vendors
  url: vendors/b-stock-vendors.yml
- group: auth
  href: https://artifacts.apis.io/b-stock/security/b-stock-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/b-stock-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bstock.com
created: '2026-10-24'
description: B‑Stock operates an online marketplace that runs liquidation auctions and Buy Now listings for inventory resale. It enables buyers to source returned, excess, and trade‑in inventory—including smartphones, tablets, and other consumer goods—directly from top retailers, brands, and mobile carriers. The platform also offers contract agreements, direct sales, and Net Terms payment options for bulk purchasing.
layout: provider
modified: '2026-10-24'
name: B-Stock
nav: Providers
network: true
overview: B-Stock is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include liquidation, wholesale, inventory resale, auction, and buy now.
random_paper: 19
score:
  band: minimal
  composite: 3.1
  coverage:
    artifact_dirs: 6
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
  name: B Stock Domain Security
  slug: b-stock-domain-security
  summary_line: TLSv1.3 · DMARC
slug: b-stock
tags:
- liquidation
- wholesale
- inventory resale
- auction
- buy now
- net terms
website: https://bstock.com
---
