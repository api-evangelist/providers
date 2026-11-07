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
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/1balance/llms/1balance-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/1balance-llms.txt
- group: agent
  href: https://artifacts.apis.io/1balance/well-known/1balance-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/1balance-well-known.yml
- group: other
  href: https://artifacts.apis.io/1balance/hosts/1balance-hosts.yml
  title: ''
  type: Hosts
  url: hosts/1balance-hosts.yml
- group: other
  href: https://artifacts.apis.io/1balance/vendors/1balance-vendors.yml
  title: ''
  type: Vendors
  url: vendors/1balance-vendors.yml
- group: company
  title: ''
  type: BlogRSS
  url: https://1balance.com/blogs/well-true.atom
- group: company
  title: ''
  type: Website
  url: https://1balance.com
- group: company
  title: ''
  type: Blog
  url: https://1balance.com/blogs/well-true
- group: commercial
  title: ''
  type: TermsOfService
  url: https://1balance.com/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://1balance.com/policies/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://1balance.com/pages/contact-us
- group: docs
  title: ''
  type: Documentation
  url: https://1balance.com/pages/about-us
coverage:
  detail: The GraphQL endpoint returns Shopify's Storefront schema, which is not owned by 1Balance, so no owned contract is available.
  evidence:
  - status: 200
    url: https://1balance.com/api/graphql
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-07-17'
description: 1Balance (1Balance Living) is a personalized herbal-wellness and tea brand offering curated caffeinated and caffeine-free tisane blends formulated for different times of day — spanning gut health, energy, metabolism, adaptogenic immune support, relaxation, and menopause support. The company blends traditional herbal science and personalization (drawing on Ayurveda and naturopathy) with modern subscription commerce, selling whole-herb capsule and loose-leaf tea blends directly to consumers through a Shopify-powered storefront with free shipping over $30 and a 30-day money-back guarantee. Backed by an Accel-led seed round, 1Balance operates as a US/India direct-to-consumer consumer-wellness company. This API Evangelist profile tracks 1Balance as a consumer brand; it runs a retail e-commerce experience and does not publish a public developer API, SDKs, or developer portal.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/1balance.png
layout: provider
modified: '2026-10-06'
name: 1Balance
nav: Providers
network: true
overview: '1Balance is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Wellness, Herbal Tea, and Nutrition.


  1Balance''s developer surface includes engineering blog, support, documentation, and 8 more developer resources.'
random_paper: 15
score:
  band: minimal
  composite: 10.6
  coverage:
    artifact_dirs: 13
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.4
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 55.4
    operational_transparency: 0.0
  previous_composite: 12.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 7.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/1balance/1balance-2026-08-07T160647.png
security:
- kind: domain-security
  name: 1Balance Domain Security
  slug: 1balance-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: 1balance
tags:
- Company
- Consumer
- Wellness
- Herbal Tea
- Nutrition
- Supplements
- E-Commerce
- Direct to Consumer
- Subscription
website: https://1balance.com
---
