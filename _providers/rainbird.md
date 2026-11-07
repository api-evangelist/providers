---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
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
    mcp_tool_quality: na
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
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: GraphQL API for Rain Bird product data.
  name: Rain Bird GraphQL API
  slug: rain-bird-graphql-api
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/rainbird/plans/rainbird-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/rainbird-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/rainbird/hosts/rainbird-hosts.yml
  title: ''
  type: Hosts
  url: hosts/rainbird-hosts.yml
- group: other
  href: https://artifacts.apis.io/rainbird/vendors/rainbird-vendors.yml
  title: ''
  type: Vendors
  url: vendors/rainbird-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.rainbird.com/resources/terms-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.rainbird.com/privacy
- group: company
  title: ''
  type: Newsroom
  url: https://www.rainbird.com/news
- group: start
  title: ''
  type: GettingStarted
  url: https://store.rainbird.com/getting-started
- group: auth
  href: https://artifacts.apis.io/rainbird/security/rainbird-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/rainbird-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.rainbird.com/
created: '2026-10-28'
description: Rain Bird is a global irrigation company providing innovative water management solutions for residential, commercial, and agricultural customers. Their products include sprinklers, drip irrigation, controllers, and smart water‑saving technologies designed to conserve water while maintaining healthy landscapes and crops. The company emphasizes sustainability, advanced technology, and customer support across multiple regions worldwide.
layout: provider
modified: '2026-10-28'
name: Rain Bird
nav: Providers
network: true
overview: 'Rain Bird is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Irrigation, Water Management, Agriculture, and Sustainability.


  Rain Bird''s developer surface includes getting-started guide and 8 more developer resources.'
plans:
- name: Rainbird Plans Pricing
  plan_count: 13
  slug: rainbird-plans-pricing
random_paper: 3
score:
  band: emerging
  composite: 15.2
  coverage:
    artifact_dirs: 10
    catalog_earned: 47.0
    catalog_earned_first_party: 12.0
    catalog_gap: 68.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.9
  facets:
    access_clarity: 42.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 6.0
    discoverability: 63.4
    operational_transparency: 0.0
  previous_composite: 19.1
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
screenshot: https://apis.io/screenshots/rainbird/rainbird-2026-11-03T141910.png
security:
- kind: domain-security
  name: Rainbird Domain Security
  slug: rainbird-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: rainbird
tags:
- Company
- Irrigation
- Water Management
- Agriculture
- Sustainability
website: https://www.rainbird.com/
---
