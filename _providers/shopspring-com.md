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
  href: https://artifacts.apis.io/shopspring-com/hosts/shopspring-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/shopspring-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/shopspring-com/vendors/shopspring-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/shopspring-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/shopspring-com/security/shopspring-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/shopspring-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.shopspring.ca
- group: docs
  title: ''
  type: Documentation
  url: https://www.shopspring.ca/
- group: company
  title: ''
  type: About
  url: https://www.shopspring.ca/about
- group: operate
  title: ''
  type: Contact
  url: https://www.shopspring.ca/contact
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.shopspring.ca/privacy-policy
coverage:
  detail: the company publishes developer documentation but serves no machine-readable contract from it
  evidence:
  - status: 200
    url: https://www.shopspring.ca
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-22'
description: ShopSpring is a Toronto‑based ecommerce solutions provider delivering platforms for entertainment, consumer packaged goods and retail brands. It offers end‑to‑end services including custom storefronts, advertising, analytics and ongoing support to help businesses grow online. The company emphasizes immersive digital experiences, omnichannel integration and data‑driven insights for its clients.
layout: provider
modified: '2026-10-22'
name: Spring *
nav: Providers
network: true
overview: 'Spring * is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, E-commerce, Marketing, SaaS, and Platform.


  Spring *''s developer surface includes documentation and 7 more developer resources.'
random_paper: 1
score:
  band: minimal
  composite: 7.7
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
    developer_ergonomics: 9.5
    discoverability: 44.6
    operational_transparency: 0.0
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
  name: Shopspring Com Domain Security
  slug: shopspring-com-domain-security
  summary_line: TLSv1.3 · HSTS
slug: shopspring-com
tags:
- Company
- E-commerce
- Marketing
- SaaS
- Platform
website: https://www.shopspring.ca
---
