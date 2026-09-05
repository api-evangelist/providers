---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - rate-limits
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 3
common:
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/mod-pizza-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/mod-pizza-plans-pricing.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mod-pizza-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://modpizza.com/
- group: company
  title: ''
  type: Blog
  url: https://modpizza.com/blog/
- group: company
  title: ''
  type: News
  url: https://modpizza.com/news/
- group: operate
  title: ''
  type: Support
  url: https://modpizza.com/contact-us/
- group: operate
  title: ''
  type: FAQ
  url: https://modpizza.com/faq/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://modpizza.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://modpizza.com/privacy-policy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/MOD-PIZZA
- group: other
  title: ''
  type: Locations
  url: https://locations.modpizza.com/
- group: other
  title: ''
  type: OnlineOrdering
  url: https://orders.modpizza.com/
- group: other
  title: ''
  type: Menu
  url: https://modpizza.com/menu/
- group: other
  title: ''
  type: Loyalty
  url: https://modpizza.com/rewards/
- group: other
  title: ''
  type: Franchising
  url: https://modpizza.com/franchising/
- group: company
  title: ''
  type: Careers
  url: https://modpizza.com/careers/
coverage:
  checked: '2026-08-25'
  detail: 'MOD Pizza is a fast-casual restaurant chain that consumes restaurant-technology SaaS rather than publishing software: online ordering at orders.modpizza.com is a Koala-powered Next.js storefront calling api.koala.io, the MOD Rewards app ships under Punchh''s com.punchh.mod bundle, and locations.modpizza.com is served from Yext''s pages CDN -- so every machine-readable contract in the guest journey belongs to a vendor, not to MOD Pizza, which serves no OpenAPI, GraphQL, MCP or .well-known document on any host it controls and has 0 public repositories in its own github.com/MOD-PIZZA organization.'
  evidence:
  - status: 404
    url: https://modpizza.com/openapi.json
  - status: 404
    url: https://modpizza.com/llms.txt
  - status: 404
    url: https://modpizza.com/.well-known/api-catalog
  - status: 307
    url: https://orders.modpizza.com/.well-known/agent-card.json
  - status: 404
    url: https://locations.modpizza.com/openapi.json
  - status: 200
    url: https://api.github.com/orgs/MOD-PIZZA
  reason: not-a-software-company
  state: none
created: '2026-08-25'
description: 'MOD Pizza is a Seattle-based fast-casual restaurant chain built around individually sized, made-to-order artisan-style pizzas and salads sold at one fixed price regardless of how many of its 40-plus toppings, finishing sauces and dressings a guest chooses. The company operates and franchises hundreds of locations across the United States and runs a digital guest surface consisting of a WordPress marketing site, a Yext-powered store locator, a Koala-powered online ordering storefront at orders.modpizza.com, and a Punchh-powered MOD Rewards loyalty app on iOS and Android. MOD Pizza is a consumer of restaurant-technology APIs rather than a publisher of them: as of this profiling pass it operates no developer program, publishes no OpenAPI, AsyncAPI, GraphQL or MCP contract, and exposes no partner or franchisee API documentation on any host it controls. Delivery is fulfilled through third-party marketplaces such as DoorDash rather than a first-party delivery API.'
image: https://modpizza.com/wp-content/uploads/2021/12/260518_olo_image_square_01-23-1024x1024.jpg
layout: provider
modified: '2026-08-25'
name: MOD Pizza
nav: Providers
network: true
overview: 'MOD Pizza is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Restaurant, Food and Beverage, Fast Casual, and Pizza.


  MOD Pizza''s developer surface includes engineering blog, product news, support, FAQ, and 13 more developer resources.'
plans:
- name: Mod Pizza Plans Pricing
  plan_count: 0
  slug: mod-pizza-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 0
  name: Mod Pizza Rate Limits
  slug: mod-pizza-rate-limits
score:
  band: emerging
  composite: 11.0
  coverage:
    artifact_dirs: 7
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
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 11.0
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mod-pizza/refs/heads/main/screenshots/mod-pizza-2026-09-02T150623.png
security:
- kind: domain-security
  name: Mod Pizza Domain Security
  slug: mod-pizza-domain-security
  summary_line: TLSv1.3 · DMARC
slug: mod-pizza
tags:
- Company
- Restaurant
- Food and Beverage
- Fast Casual
- Pizza
- Retail
- Consumer
- Loyalty
- Online Ordering
- Franchising
website: https://modpizza.com/
---
