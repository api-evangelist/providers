---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: platform
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 4.5
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Bruvi provides a coffee brewing and pod ordering API accessible via GraphQL.
  name: Bruvi API
  slug: bruvi-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/bruvi/llms/bruvi-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bruvi-llms.txt
- group: agent
  href: https://artifacts.apis.io/bruvi/well-known/bruvi-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bruvi-well-known.yml
- group: other
  href: https://artifacts.apis.io/bruvi/hosts/bruvi-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bruvi-hosts.yml
- group: other
  href: https://artifacts.apis.io/bruvi/vendors/bruvi-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bruvi-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bruvi.com/policies/terms-of-service
- group: operate
  title: ''
  type: Support
  url: https://help.bruvi.com/hc/en-us
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bruvi.com/policies/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://bruvi.com/blogs/articles/tagged/press
- group: docs
  title: ''
  type: Documentation
  url: https://help.bruvi.com/
- group: auth
  href: https://artifacts.apis.io/bruvi/security/bruvi-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bruvi-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bruvi.com/
created: '2026-10-06'
description: Bruvi is a Los Angeles‑based company offering a next‑generation single‑serve coffee system. It sells brewers, reusable B‑Pods and a mobile app that automates brewing, pod ordering and personalization. The brand emphasizes sustainability, premium craft coffee, and a subscription model for fresh pods delivered to customers.
image: https://cdn.shopify.com/s/files/1/0078/7582/1620/files/Cream-Brewer-New-Bundle-With-Filter.png?v=1745960737
layout: provider
modified: '2026-10-06'
name: Bruvi
nav: Providers
network: true
overview: 'Bruvi is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Coffee, Subscription, Sustainability, and E-Commerce.


  Bruvi''s developer surface includes support, documentation, and 9 more developer resources.'
random_paper: 0
score:
  band: minimal
  composite: 10.1
  coverage:
    artifact_dirs: 8
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.3
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 74.1
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 14.4
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/bruvi/bruvi-2026-11-03T122709.png
security:
- kind: domain-security
  name: Bruvi Domain Security
  slug: bruvi-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bruvi
tags:
- Company
- Coffee
- Subscription
- Sustainability
- E-Commerce
website: https://bruvi.com/
---
