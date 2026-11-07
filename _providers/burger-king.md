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
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: 'Burger King''s online ordering platform on bk.com lets customers place pickup, curbside, dine-in, and delivery orders directly through the web. Integrates with the same Royal Perks loyalty and payment '
  name: Burger King Online Ordering
  slug: bk-online-ordering
- description: Burger King's restaurant locator providing search by city, state, ZIP code, or geolocation to find the nearest restaurant locations, hours, services (drive-thru, delivery, dine-in), and contact detail
  name: Burger King Store Locator
  slug: bk-store-locator
artifact_total: 18
common:
- group: company
  title: ''
  type: Blog
  url: https://www.bk.com/blog/
- group: auth
  href: https://artifacts.apis.io/burger-king/security/burger-king-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/burger-king-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/burger-king
- group: company
  title: ''
  type: Website
  url: https://www.bk.com/
- group: other
  title: ''
  type: ParentCompany
  url: https://rbi.com/
- group: start
  title: ''
  type: Login
  url: https://www.bk.com/account
- group: start
  title: ''
  type: Signup
  url: https://www.bk.com/account/sign-up
created: '2026-05-05'
description: Burger King is one of the world's largest fast-food hamburger chains operating over 18,000 locations in more than 100 countries. Known for the flame-grilled Whopper, Burger King is a subsidiary of Restaurant Brands International (RBI) and operates the BK mobile app, Royal Perks loyalty program, and delivery partnerships with DoorDash, Uber Eats, and Grubhub.
features:
- description: Order ahead through the BK mobile app for pickup, curbside, or delivery.
  name: Mobile Ordering
- description: Earn crowns on every purchase and redeem for menu items and offers.
  name: Royal Perks Loyalty
- description: Delivery via DoorDash, Uber Eats, and Grubhub partnerships.
  name: Delivery Integration
- description: Find nearby Burger King locations, hours, and services.
  name: Restaurant Locator
- description: Mobile-app-exclusive offers and promotional discounts.
  name: Digital Coupons
- description: Real-time order status and pickup notifications.
  name: Order Tracking
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/burger-king.png
integrations:
- description: Third-party delivery partnership for home delivery orders.
  name: DoorDash
- description: Delivery integration through Uber Eats marketplace.
  name: Uber Eats
- description: Delivery integration through Grubhub marketplace.
  name: Grubhub
- description: Parent company operating Tim Hortons, Popeyes, and Firehouse Subs alongside Burger King.
  name: Restaurant Brands International
layout: provider
modified: '2026-10-06'
name: Burger King
nav: Providers
network: true
overview: 'Burger King is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Fast Food, Restaurant, Food and Beverage, Loyalty, and Mobile Ordering.


  Burger King''s developer surface includes engineering blog, signup flow, and 5 more developer resources.'
random_paper: 13
score:
  band: minimal
  composite: 8.0
  coverage:
    artifact_dirs: 5
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 6.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 57.1
    operational_transparency: 0.0
  previous_composite: 8.0
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/burger-king/burger-king-2026-06-20T173819.png
security:
- kind: domain-security
  name: Burger King Domain Security
  slug: burger-king-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: burger-king
tags:
- Fast Food
- Restaurant
- Food and Beverage
- Loyalty
- Mobile Ordering
use_cases:
- description: Customers ordering ahead for in-store or curbside pickup.
  name: Mobile Pickup Orders
- description: Repeat customers earning and redeeming crowns through Royal Perks.
  name: Loyalty Engagement
- description: Customers ordering Burger King through third-party delivery platforms.
  name: Delivery Orders
- description: Larger group orders for family meals and combos.
  name: Family Meal Ordering
- description: Drive-thru and curbside ordering integration with mobile app.
  name: Drive-Thru Ordering
website: https://www.bk.com/
---
