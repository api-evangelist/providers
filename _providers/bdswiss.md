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
  href: https://raw.githubusercontent.com/api-evangelist/bdswiss/refs/heads/main/hosts/bdswiss-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bdswiss-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bdswiss/refs/heads/main/vendors/bdswiss-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bdswiss-vendors.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bdswiss
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bdswiss/refs/heads/main/security/bdswiss-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bdswiss-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bdswiss.com
coverage:
  checked: '2026-09-27'
  detail: The main site bdswiss.com returns a JavaScript shell and OpenAPI URLs serve HTML pages, not machine‑readable specs.
  evidence:
  - status: 200
    url: https://bdswiss.com/openapi.json
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-27'
description: Bdswiss is a global online brokerage firm offering a range of trading services, including forex, CFDs, commodities, and cryptocurrencies. Founded in 2009, the company provides a proprietary trading platform, educational resources, and customer support to retail traders worldwide. Bdswiss aims to deliver a user-friendly experience with competitive spreads, multiple account types, and a focus on security and regulatory compliance. The firm operates under various licenses across multiple jurisdictions, catering to both beginner and experienced traders.
layout: provider
modified: '2026-09-27'
name: Bdswiss
nav: Providers
network: true
overview: Bdswiss is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Brokerage, Trading, Forex, and CFDs.
random_paper: 19
score:
  band: minimal
  composite: 2.9
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
    operational_transparency: 5.3
  regulatory:
    applies: true
    matched_via: weak_tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 5.6
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bdswiss Domain Security
  slug: bdswiss-domain-security
  summary_line: TLSv1.3 · DMARC
slug: bdswiss
tags:
- Company
- Brokerage
- Trading
- Forex
- CFDs
- Cryptocurrency
- Financial Services
website: https://bdswiss.com
---
