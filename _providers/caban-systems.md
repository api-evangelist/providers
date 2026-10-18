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
  href: https://raw.githubusercontent.com/api-evangelist/caban-systems/refs/heads/main/hosts/caban-systems-hosts.yml
  title: ''
  type: Hosts
  url: hosts/caban-systems-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/caban-systems/refs/heads/main/vendors/caban-systems-vendors.yml
  title: ''
  type: Vendors
  url: vendors/caban-systems-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/caban-systems/refs/heads/main/security/caban-systems-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/caban-systems-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://forgeglobal.com/caban-systems_stock/
coverage:
  checked: '2026-10-06'
  detail: The company provides no public developer program or API documentation on its own website.
  evidence:
  - status: 200
    url: https://www.cabanenergy.com/en
  reason: no-developer-program
  state: none
created: '2026-10-06'
description: Caban Systems is a private company listed on the Forge Global marketplace, offering a platform for trading private company shares. The company appears as a tradable entity within Forge’s secondary market, providing liquidity solutions, IPO insights, and investment opportunities for accredited investors and institutions. While no dedicated corporate website is identified, its presence on Forge includes detailed company information, market data, and access to private market tools.
layout: provider
modified: '2026-10-06'
name: Caban Systems
nav: Providers
network: true
overview: Caban Systems is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Finance, Marketplace, Private Equity, and Trading.
random_paper: 18
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
    matched_via: weak_tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 5.6
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Caban Systems Domain Security
  slug: caban-systems-domain-security
  summary_line: TLSv1.3 · DMARC
slug: caban-systems
tags:
- Company
- Finance
- Marketplace
- Private Equity
- Trading
website: https://forgeglobal.com/caban-systems_stock/
---
