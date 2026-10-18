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
  href: https://raw.githubusercontent.com/api-evangelist/countertopsmart/refs/heads/main/hosts/countertopsmart-hosts.yml
  title: ''
  type: Hosts
  url: hosts/countertopsmart-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/countertopsmart/refs/heads/main/vendors/countertopsmart-vendors.yml
  title: ''
  type: Vendors
  url: vendors/countertopsmart-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/countertopsmart/refs/heads/main/security/countertopsmart-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/countertopsmart-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.countertopsmart.com/
- group: company
  title: ''
  type: Blog
  url: https://www.countertopsmart.com/blog
- group: operate
  title: ''
  type: Support
  url: https://www.countertopsmart.com/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.countertopsmart.com/home/terms
created: '2026-10-11'
description: CountertopSmart is an online marketplace that lets users browse, visualize, and purchase a wide variety of countertop materials such as quartz, granite, marble, and porcelain. The site offers instant quotes, detailed product categories, and a showroom map, enabling homeowners and designers to select and buy countertops directly through an e‑commerce platform.
layout: provider
modified: '2026-10-11'
name: CountertopSmart
nav: Providers
network: true
overview: 'CountertopSmart is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, E-Commerce, HomeImprovement, Marketplace, and Countertops.


  CountertopSmart''s developer surface includes engineering blog, support, and 5 more developer resources.'
random_paper: 8
score:
  band: minimal
  composite: 7.2
  coverage:
    artifact_dirs: 5
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 44.6
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Countertopsmart Domain Security
  slug: countertopsmart-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: countertopsmart
tags:
- Company
- E-Commerce
- HomeImprovement
- Marketplace
- Countertops
website: https://www.countertopsmart.com/
---
