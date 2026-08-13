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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-12'
api_count: 0
artifact_total: 11
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ritas-italian-ice-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.ritasice.com
- group: operate
  title: ''
  type: ContactUs
  url: https://www.ritasice.com/contact/
- group: company
  title: ''
  type: Careers
  url: https://www.ritasice.com/careers/
- group: other
  title: ''
  type: Franchise
  url: https://ownaritasfranchise.com/
- group: other
  title: ''
  type: Rewards
  url: https://www.ritasice.com/rewards/
- group: other
  title: ''
  type: GiftCards
  url: https://www.ritasice.com/gift-cards
- group: company
  title: ''
  type: Press
  url: https://www.ritasice.com/press-contact/
- group: start
  title: Rewards Account Login
  type: Login
  url: https://api.ritasice.com/login
- group: commercial
  title: Loyalty Terms and Conditions
  type: TermsOfService
  url: https://www.ritasice.com/loyalty-terms-and-conditions/
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/RitasItalianIceCompany
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/ritasice
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/ritasitalianice
description: Rita's Italian Ice is a Philadelphia-area founded franchise chain of frozen treat shops known for Italian Ice, Frozen Custard, Gelati, and Misto, operating approximately 550-590 locations across the United States under the tagline "Ice Custard Happiness." The brand is privately held under MTY Food Group (acquired 2021). Rita's maintains a consumer-facing loyalty mobile app and a franchise development site, but exposes no public developer API, OpenAPI specification, SDK, webhooks, status page, or developer portal at this time. The loyalty program runs on the third-party Punchh customer engagement platform, and the mobile app was developed with Relevant Mobile; the only network-facing endpoint (api.ritasice.com) is a private backend for the consumer app and returns HTTP 403 to unauthenticated requests.
features:
- description: Consumer loyalty program where guests earn credit per visit and unlock a free treat reward, accessible via the Rita's Ice mobile app, phone number, or email at the point of sale.
  name: Rita's Rewards Loyalty
- description: Native iOS and Android app providing a store locator, rewards tracking, mobile check-in, and personalized offers.
  name: Mobile App
- description: Find Rita's locations across the United States, surfaced in the mobile app and on the public website.
  name: Store Locator
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ritas-italian-ice.png
integrations:
- description: Cloud-based customer loyalty and engagement platform powering the Rita's Rewards program and its point-of-sale integration. Third-party vendor; Rita's exposes no public API for this integration.
  name: Punchh
- description: Mobile app development partner behind the revamped Rita's Ice app, including beacon-based targeting and social check-in features.
  name: Relevant Mobile
- description: Distribution channel for the Rita's Ice iOS app (apps.apple.com/us/app/ritas-ice/id532627057).
  name: Apple App Store
- description: Distribution channel for the Rita's Ice Android app (play.google.com/store/apps/details?id=com.app.ritas).
  name: Google Play
layout: provider
modified: '2026-06-03'
name: Rita's Italian Ice
nav: Providers
network: true
overview: Rita's Italian Ice is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Restaurants, Food and Beverage, Frozen Desserts, Franchise, and Quick Service Restaurant.
random_paper: 0
score:
  band: minimal
  composite: 9.7
  delta: 0.0
  facets:
    commercial_clarity: 23.7
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 9.7
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
security:
- kind: domain-security
  name: Ritas Italian Ice Domain Security
  slug: ritas-italian-ice-domain-security
  summary_line: TLSv1.3 · DMARC
slug: ritas-italian-ice
tags:
- Restaurants
- Food and Beverage
- Frozen Desserts
- Franchise
- Quick Service Restaurant
use_cases:
- description: Guests present the mobile app, phone number, or email at checkout to earn visit credit and redeem a free Italian Ice, Frozen Custard, or Gelati reward.
  name: Earn and Redeem Rewards
- description: Customers locate nearby Rita's shops using the in-app and website store locator.
  name: Find a Location
- description: Prospective franchisees research and apply to operate a Rita's Italian Ice location through the franchise development site.
  name: Own a Franchise
website: https://www.ritasice.com
---
