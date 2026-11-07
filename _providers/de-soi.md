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
- description: GraphQL API for De Soi beverage platform
  name: De Soi GraphQL API
  slug: de-soi-graphql-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/de-soi/llms/de-soi-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/de-soi-llms.txt
- group: agent
  href: https://artifacts.apis.io/de-soi/well-known/de-soi-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/de-soi-well-known.yml
- group: other
  href: https://artifacts.apis.io/de-soi/hosts/de-soi-hosts.yml
  title: ''
  type: Hosts
  url: hosts/de-soi-hosts.yml
- group: other
  href: https://artifacts.apis.io/de-soi/vendors/de-soi-vendors.yml
  title: ''
  type: Vendors
  url: vendors/de-soi-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://drinkdesoi.com/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://drinkdesoi.com/policies/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://drinkdesoi.com/blogs/press
- group: start
  title: ''
  type: Login
  url: https://drinkdesoi.com/a/account/login
- group: auth
  href: https://artifacts.apis.io/de-soi/security/de-soi-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/de-soi-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://drinkdesoi.com
created: '2026-10-22'
description: De Soi is a Los Angeles‑based startup offering non‑alcoholic sparkling aperitifs crafted with natural adaptogens and botanicals. Founded in 2022 by Katy Perry and Morgan McLachlan, the brand provides a mindful drinking experience with a range of cocktails such as Classic Sampler, Social Spritz, and Haute Margarita, available online and in select retail stores.
layout: provider
modified: '2026-10-22'
name: De Soi
nav: Providers
network: true
overview: De Soi is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Beverages, Non-Alcoholic, Startups, and Los Angeles.
random_paper: 1
score:
  band: minimal
  composite: 9.7
  coverage:
    artifact_dirs: 10
    catalog_earned: 35.0
    catalog_earned_first_party: 0.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.1
  facets:
    access_clarity: 17.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 70.5
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 13.8
  provenance:
    mcp: unknown
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
screenshot: https://apis.io/screenshots/de-soi/de-soi-2026-11-03T130402.png
security:
- kind: domain-security
  name: De Soi Domain Security
  slug: de-soi-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: de-soi
tags:
- Company
- Beverages
- Non-Alcoholic
- Startups
- Los Angeles
website: https://drinkdesoi.com
---
