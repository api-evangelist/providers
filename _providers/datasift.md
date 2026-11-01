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
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 2
common:
- group: commercial
  href: https://artifacts.apis.io/datasift/plans/datasift-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/datasift-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/datasift/llms/datasift-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/datasift-llms.txt
- group: auth
  href: https://artifacts.apis.io/datasift/well-known/datasift-intercom-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/datasift-intercom-security.txt
- group: auth
  href: https://artifacts.apis.io/datasift/well-known/datasift-api-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/datasift-api-security.txt
- group: agent
  href: https://artifacts.apis.io/datasift/well-known/datasift-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/datasift-well-known.yml
- group: other
  href: https://artifacts.apis.io/datasift/hosts/datasift-hosts.yml
  title: ''
  type: Hosts
  url: hosts/datasift-hosts.yml
- group: other
  href: https://artifacts.apis.io/datasift/vendors/datasift-vendors.yml
  title: ''
  type: Vendors
  url: vendors/datasift-vendors.yml
- group: docs
  title: ''
  type: Documentation
  url: https://developers.datasift.ai/
- group: auth
  href: https://artifacts.apis.io/datasift/security/datasift-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/datasift-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.datasift.ai
- group: company
  title: ''
  type: Blog
  url: https://www.datasift.ai/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.datasift.ai/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.datasift.ai/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.datasift.ai/legal/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://intercom.help/reisift/en/
created: '2026-10-22'
description: DataSift provides a real‑estate data platform that aggregates, enriches, and delivers property‑related information to developers, marketers, and analysts. Their APIs enable access to property listings, transaction histories, market trends, and predictive analytics, helping users build applications for property search, valuation, and market intelligence. DataSift focuses on delivering high‑quality, up‑to‑date real‑estate data across multiple regions, with robust documentation and developer support.
layout: provider
modified: '2026-10-22'
name: Datasift
nav: Providers
network: true
overview: 'Datasift is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Real Estate, Data Platform, Marketing, and Analytics.


  Datasift''s developer surface includes documentation, engineering blog, pricing, support, and 11 more developer resources.'
plans:
- name: Datasift Plans Pricing
  plan_count: 3
  slug: datasift-plans-pricing
random_paper: 8
score:
  band: emerging
  composite: 20.7
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 12.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 35.7
    operational_transparency: 10.5
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Datasift Domain Security
  slug: datasift-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: datasift
tags:
- Real Estate
- Data Platform
- Marketing
- Analytics
website: https://www.datasift.ai
---
