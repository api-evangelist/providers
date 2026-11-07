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
- description: GraphQL endpoint for Bokksu services
  name: Bokksu GraphQL API
  slug: bokksu-graphql-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/bokksu/llms/bokksu-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bokksu-llms.txt
- group: agent
  href: https://artifacts.apis.io/bokksu/well-known/bokksu-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bokksu-well-known.yml
- group: other
  href: https://artifacts.apis.io/bokksu/hosts/bokksu-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bokksu-hosts.yml
- group: other
  href: https://artifacts.apis.io/bokksu/vendors/bokksu-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bokksu-vendors.yml
- group: auth
  href: https://artifacts.apis.io/bokksu/security/bokksu-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bokksu-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bokksu.com
- group: docs
  title: ''
  type: Documentation
  url: https://bokksu.com/pages/about
- group: company
  title: ''
  type: Blog
  url: https://bokksu.com/blogs/news
- group: operate
  title: ''
  type: Support
  url: https://bokksu.com/pages/faq
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bokksu.com/pages/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bokksu.com/pages/privacy-policy-with-ccpa
created: '2026-10-02'
description: Bokksu provides a curated subscription box delivering authentic Japanese snacks and candies sourced from centuries‑old family makers. Customers can choose classic, gift, or themed boxes with options for 3, 6, or 12‑month subscriptions, and the service includes rare extras, a blog, and corporate gifting options. The company emphasizes quality, cultural storytelling, and a seamless e‑commerce experience.
image: http://bokksu.com/cdn/shop/files/SNB_Compressed.jpg?v=1778135917
layout: provider
modified: '2026-10-02'
name: Bokksu
nav: Providers
network: true
overview: 'Bokksu is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Subscription, Snacks, Japan, and E-Commerce.


  Bokksu''s developer surface includes documentation, engineering blog, support, and 8 more developer resources.'
random_paper: 7
score:
  band: minimal
  composite: 10.3
  coverage:
    artifact_dirs: 9
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.4
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 8.3
    discoverability: 73.2
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - japan
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - japan-korea
  previous_composite: 14.7
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
screenshot: https://apis.io/screenshots/bokksu/bokksu-2026-11-03T122147.png
security:
- kind: domain-security
  name: Bokksu Domain Security
  slug: bokksu-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bokksu
tags:
- Company
- Subscription
- Snacks
- Japan
- E-Commerce
website: https://bokksu.com
---
