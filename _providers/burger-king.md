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
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-07-28'
api_count: 4
apis:
- description: The Burger King mobile app provides mobile ordering, in-store pickup, curbside pickup, and delivery via integration with DoorDash and other partners. Includes Royal Perks loyalty program access, digit
  name: Burger King Mobile App
  slug: bk-mobile-app
- description: Royal Perks is Burger King's loyalty rewards program that earns members crowns for purchases that can be redeemed for menu items and exclusive offers. The program launched in 2021 and is accessed thro
  name: Burger King Royal Perks
  slug: royal-perks
- description: 'Burger King''s online ordering platform on bk.com lets customers place pickup, curbside, dine-in, and delivery orders directly through the web. Integrates with the same Royal Perks loyalty and payment '
  name: Burger King Online Ordering
  slug: bk-online-ordering
- description: Burger King's restaurant locator providing search by city, state, ZIP code, or geolocation to find the nearest restaurant locations, hours, services (drive-thru, delivery, dine-in), and contact detail
  name: Burger King Store Locator
  slug: bk-store-locator
artifact_total: 20
common:
- group: auth
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
modified: '2026-06-02'
name: Burger King
nav: Providers
network: true
overview: 'Burger King publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Fast Food, Restaurants, Food & Beverage, Loyalty, and Mobile Ordering.


  Burger King''s developer surface includes signup flow and 5 more developer resources.'
random_paper: 51
score:
  band: minimal
  composite: 9.1
  delta: -2.3
  facets:
    commercial_clarity: 13.2
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 11.4
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/burger-king/refs/heads/main/screenshots/burger-king-2026-06-20T173819.png
security:
- kind: domain-security
  name: Burger King Domain Security
  slug: burger-king-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: burger-king
tags:
- Fast Food
- Restaurants
- Food & Beverage
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
