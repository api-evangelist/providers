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
  scored_at: '2026-09-05'
api_count: 6
apis:
- description: Inner Circle Rewards is Circle K's free loyalty program letting members earn fuel discounts, food rewards, and other in-store rewards. Membership is managed via the Circle K mobile app, website, and i
  name: Circle K Inner Circle Rewards
  slug: inner-circle-rewards
- description: Easy Pay is Circle K's payment program enabling customers to pay for fuel directly at the pump using their linked checking account with a Circle K Easy Pay card or mobile-app payment.
  name: Circle K Easy Pay
  slug: easy-pay
- description: The Circle K mobile app provides access to Inner Circle Rewards membership, fuel-savings tracking, store locator, deals and offers, digital receipts, and integrated mobile payment.
  name: Circle K Mobile App
  slug: circle-k-mobile-app
- description: Circle K's EV charging network provides fast charging at select Circle K locations. The network supports CCS, CHAdeMO, and Tesla NACS connectors with payment via app, RFID card, or contactless payment
  name: Circle K EV Charging
  slug: circle-k-ev-charging
- description: 'Circle K PRO Business Fleet Card is a commercial fleet fuel card with discounts at Circle K locations, account-level controls, transaction reporting, and integration with fleet management systems for '
  name: Circle K PRO Business Fleet Card
  slug: circle-k-pro-fleet-card
- description: Circle K store locator for finding stores by ZIP code, city, or geolocation with filters for services such as EV charging, car wash, fuel brand, and 24-hour operation.
  name: Circle K Store Locator
  slug: store-locator
artifact_total: 23
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/circlek-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/circle-k
- group: company
  title: ''
  type: Website
  url: https://www.circlek.com/
- group: other
  title: ''
  type: ParentCompany
  url: https://corpo.couche-tard.com/
- group: start
  title: ''
  type: Login
  url: https://www.circlek.com/sign-in
- group: start
  title: ''
  type: Signup
  url: https://www.circlek.com/sign-up
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.circlek.com/
created: '2026-05-05'
description: Circle K is a global convenience store and fuel station chain operating more than 14,800 stores worldwide including 9,799 locations in North America and 2,697 in Europe across 48 U.S. states and over 30 countries. A subsidiary of Alimentation Couche-Tard, Circle K operates the Inner Circle Rewards loyalty program, the Easy Pay fuel payment system, an EV charging network, and the Circle K PRO Business Fleet Card.
features:
- description: Earn fuel and food rewards via Inner Circle Rewards membership.
  name: Loyalty Rewards
- description: Pay at the pump and in-store via the Circle K mobile app.
  name: Mobile Payments
- description: Linked-account payment for discounted fuel at the pump.
  name: Easy Pay Fuel Discount
- description: Fast EV charging at select Circle K locations.
  name: EV Charging
- description: Circle K PRO Business Fleet Card for commercial fleets.
  name: Fleet Fuel Cards
- description: Find Circle K locations with service filters.
  name: Store Locator
- description: Limited-time offers and discounts surfaced via the app.
  name: Promotions and Deals
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/circlek.png
integrations:
- description: Canadian parent company headquartered in Laval, Quebec.
  name: Alimentation Couche-Tard
- description: Some Circle K locations sell Shell-branded fuel under wholesale agreements.
  name: Shell Branded Fuel
- description: Some Circle K locations sell Valero-branded fuel.
  name: Valero Branded Fuel
- description: Additional fuel brand partnerships at select locations.
  name: BP and Exxon Branded Fuel
layout: provider
modified: '2026-05-16'
name: Circle K
nav: Providers
network: true
overview: 'Circle K publishes 6 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Retail, Convenience Stores, Fuel, Loyalty, and EV Charging.


  Circle K''s developer surface includes signup flow and 6 more developer resources.'
random_paper: 19
score:
  band: minimal
  composite: 9.9
  coverage:
    artifact_dirs: 3
    catalog_earned: 35.0
    catalog_earned_first_party: 0.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 6.6
    commercial_clarity: 6.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 9.9
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 8.1
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/circlek/refs/heads/main/screenshots/circlek-2026-06-20T174350.png
security:
- kind: domain-security
  name: Circlek Domain Security
  slug: circlek-domain-security
  summary_line: TLSv1.3 · DMARC
slug: circlek
tags:
- Retail
- Convenience Stores
- Fuel
- Loyalty
- EV Charging
- Fleet
use_cases:
- description: Driver fueling with linked-account discounts and rewards.
  name: Daily Fuel Purchases
- description: Quick-stop convenience-store purchases with loyalty earning.
  name: Snack and Beverage Convenience
- description: Public EV charging during convenience-store visits.
  name: EV Driver Charging
- description: Commercial fleet fuel purchasing with fleet card controls.
  name: Fleet Operator Refueling
- description: Purchase fuel under Circle K, Shell, Valero, BP, and other partner brands.
  name: Cross-Brand Fuel Purchasing
website: https://www.circlek.com/
---
