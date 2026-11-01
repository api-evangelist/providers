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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.1
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/tradefeedr/hosts/tradefeedr-hosts.yml
  title: ''
  type: Hosts
  url: hosts/tradefeedr-hosts.yml
- group: other
  href: https://artifacts.apis.io/tradefeedr/vendors/tradefeedr-vendors.yml
  title: ''
  type: Vendors
  url: vendors/tradefeedr-vendors.yml
- group: auth
  href: https://artifacts.apis.io/tradefeedr/security/tradefeedr-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/tradefeedr-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://tradefeedr.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.tradefeedr.com/platform
- group: docs
  title: ''
  type: APIReference
  url: https://www.tradefeedr.com/platform
- group: company
  title: ''
  type: Blog
  url: https://www.tradefeedr.com/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.tradefeedr.com/legal
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.tradefeedr.com/legal
created: '2026-10-21'
description: Tradefeedr provides a unified API platform that aggregates and normalizes trading data from multiple liquidity providers, exchanges, and market participants. By offering standardized data, metrics, and analytics, it enables traders, brokers, and financial institutions to gain deeper insights, improve market efficiency, and streamline workflows across the trading ecosystem.
layout: provider
modified: '2026-10-21'
name: Tradefeedr
nav: Providers
network: true
overview: 'Tradefeedr is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Finance, Data, Trading, API, and Analytics.


  Tradefeedr''s developer surface includes documentation, API reference, engineering blog, and 6 more developer resources.'
random_paper: 14
score:
  band: emerging
  composite: 11.3
  coverage:
    artifact_dirs: 7
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 44.6
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: weak_tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 13.0
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Tradefeedr Domain Security
  slug: tradefeedr-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: tradefeedr
tags:
- Finance
- Data
- Trading
- API
- Analytics
- Platform
website: https://tradefeedr.com/
---
