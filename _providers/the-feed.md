---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/the-feed-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/the-feed-llms.txt
- group: company
  title: ''
  type: Blog
  url: https://thefeed.com/insider
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://thefeed.com/page/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://thefeed.com/page/terms
- group: company
  title: ''
  type: Website
  url: https://thefeed.com
created: '2026-07-17'
description: The Feed is an online sports nutrition store for endurance athletes, stocking products from more than 300 brands across fuel, hydration, supplements, and recovery. Founded by Matt Johnson while managing a Tour de France cycling team, it sells gels, chews, and drink mixes as single servings so athletes can test products without committing to full boxes, offers AutoShip subscriptions and a Feed First membership, and is the official nutrition partner of USA Triathlon. The company builds personalized fueling plans around before/during/after-workout nutrition, tested with input from over 200,000 athletes. It is a consumer e-commerce brand (Shopify storefront) with no public developer API; its machine-readable surfaces are a published llms.txt and a Google Merchant product feed.
image: https://cdn.shopify.com/s/files/1/1515/2714/files/homepage_og_1200x630.png?v=1727115010
layout: provider
modified: '2026-07-21'
name: The Feed
nav: Providers
network: true
overview: 'The Feed is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Sports Nutrition, E-Commerce, and Endurance Sports.


  The Feed''s developer surface includes engineering blog and 5 more developer resources.'
random_paper: 14
score:
  band: minimal
  composite: 10.4
  coverage:
    artifact_dirs: 3
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 10.4
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/the-feed/refs/heads/main/screenshots/the-feed-2026-09-02T163346.png
security:
- kind: domain-security
  name: The Feed Domain Security
  slug: the-feed-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: the-feed
tags:
- Company
- Consumer
- Sports Nutrition
- E-Commerce
- Endurance Sports
- Hydration
- Supplements
- Subscription
website: https://thefeed.com
---
