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
  href: https://raw.githubusercontent.com/api-evangelist/china-resources-snow-breweries/refs/heads/main/hosts/china-resources-snow-breweries-hosts.yml
  title: ''
  type: Hosts
  url: hosts/china-resources-snow-breweries-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/china-resources-snow-breweries/refs/heads/main/vendors/china-resources-snow-breweries-vendors.yml
  title: ''
  type: Vendors
  url: vendors/china-resources-snow-breweries-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/china-resources-snow-breweries/refs/heads/main/security/china-resources-snow-breweries-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/china-resources-snow-breweries-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.hiive.com/securities/china-resources-snow-breweries-stock
created: '2026-10-08'
description: China Resources Snow Breweries, also known as Snow Beer, is a major Chinese brewery and beverage company under the China Resources group. It produces a range of beers and malt beverages, operating primarily in China with a focus on the Snow brand, one of the best-selling beers in the world. The company maintains a digital presence and engages in modern marketing, but currently provides limited public API documentation.
layout: provider
modified: '2026-10-08'
name: China Resources Snow Breweries
nav: Providers
network: true
overview: China Resources Snow Breweries is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company.
random_paper: 2
score:
  band: minimal
  composite: 2.2
  coverage:
    artifact_dirs: 3
    catalog_earned: 20.0
    catalog_earned_first_party: 0.0
    catalog_gap: 95.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 35.7
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
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: China Resources Snow Breweries Domain Security
  slug: china-resources-snow-breweries-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: china-resources-snow-breweries
tags:
- Company
website: https://www.hiive.com/securities/china-resources-snow-breweries-stock
---
