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
  href: https://artifacts.apis.io/waypoint/hosts/waypoint-hosts.yml
  title: ''
  type: Hosts
  url: hosts/waypoint-hosts.yml
- group: other
  href: https://artifacts.apis.io/waypoint/vendors/waypoint-vendors.yml
  title: ''
  type: Vendors
  url: vendors/waypoint-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.waypointcommodities.com/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://www.waypointcommodities.com/news
- group: auth
  href: https://artifacts.apis.io/waypoint/security/waypoint-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/waypoint-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.waypointcommodities.com/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://www.waypointcommodities.com/
  reason: no-developer-program
  state: none
created: '2026-10-24'
description: Waypoint offers an end‑to‑end platform for buying and selling fertilizers and commodity chemicals in international markets. It provides buyers—including end users, importers, distributors, and traders—with supply sourcing, freight services, multi‑currency transactions, and market intelligence, while giving suppliers access to new markets and sales volume. The service integrates quoting, tracking, documentation, and support in a single interface.
layout: provider
modified: '2026-10-24'
name: Waypoint
nav: Providers
network: true
overview: Waypoint is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Commodities, Chemical Trading, Supply Chain, Freight, and Working Capital.
random_paper: 3
score:
  band: minimal
  composite: 5.9
  coverage:
    artifact_dirs: 6
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 46.4
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Waypoint Domain Security
  slug: waypoint-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: waypoint
tags:
- Commodities
- Chemical Trading
- Supply Chain
- Freight
- Working Capital
- Market Intelligence
website: https://www.waypointcommodities.com/
---
