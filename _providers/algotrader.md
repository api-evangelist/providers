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
  href: https://raw.githubusercontent.com/api-evangelist/algotrader/refs/heads/main/hosts/algotrader-hosts.yml
  title: ''
  type: Hosts
  url: hosts/algotrader-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/algotrader/refs/heads/main/vendors/algotrader-vendors.yml
  title: ''
  type: Vendors
  url: vendors/algotrader-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/algotrader/refs/heads/main/security/algotrader-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/algotrader-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://equityzen.com/company/algotrader
created: '2026-09-24'
description: Algotrader is a fintech company that provides algorithmic trading solutions and APIs for developers to integrate automated trading strategies. The company focuses on delivering low-latency market data, order execution, and portfolio management tools for both retail and institutional clients. Algotrader aims to democratize access to sophisticated trading algorithms through a robust developer platform. and added to the network as a stub for full-pipeline profiling.
layout: provider
modified: '2026-09-24'
name: Algotrader
nav: Providers
network: true
overview: Algotrader is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, algorithmic-trading, Developer Platform, and Finance.
random_paper: 5
score:
  band: minimal
  composite: 2.2
  coverage:
    artifact_dirs: 3
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.0
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
  previous_composite: 1.2
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 5.6
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Algotrader Domain Security
  slug: algotrader-domain-security
  summary_line: TLSv1.3 · DMARC
slug: algotrader
tags:
- Company
- Fintech
- algorithmic-trading
- Developer Platform
- Finance
website: https://equityzen.com/company/algotrader
---
