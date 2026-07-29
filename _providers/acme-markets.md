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
api_count: 5
apis:
- description: Public store-locator surface used by the Acme Markets website to render store information (address, hours, services, phone, departments). Pages are rendered under the `local.acmemarkets.com` subdomain
  name: Acme Markets Store Locator
  slug: store-locator
- description: ACME for U is the chain's free loyalty program, surfacing personalized weekly ad deals, digital coupons, and Points redeemable for fuel and groceries. The program is delivered through the Acme Markets
  name: ACME for U Loyalty Program
  slug: acme-for-u-loyalty
- description: 'FreshPass is the Albertsons-family paid subscription that provides unlimited free grocery delivery, exclusive deals, and additional Points on the Acme Markets e-commerce platform. The Acme storefront '
  name: FreshPass Delivery Subscription
  slug: freshpass-subscription
- description: DriveUp & Go is the Acme Markets / Albertsons-family curbside pickup product ordered through the website and mobile app. Customers build an order online, schedule a pickup window, and check in via the
  name: DriveUp & Go Curbside Pickup
  slug: driveup-and-go
- description: Acme Markets operates in-store pharmacies offering prescription refills, transfers, immunizations, and pharmacy account management. The pharmacy surface is delivered through the website and the shared
  name: Acme Markets Pharmacy
  slug: pharmacy
artifact_total: 23
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/acme-markets-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.acmemarkets.com
- group: company
  title: ''
  type: AboutUs
  url: https://www.acmemarkets.com/about-us.html
- group: other
  title: ''
  type: ParentCompany
  url: https://www.albertsonscompanies.com
- group: company
  title: ''
  type: Careers
  url: https://www.acmemarkets.com/about-us/careers.html
- group: operate
  title: ''
  type: ContactUs
  url: https://www.acmemarkets.com/about-us/contact-us.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.acmemarkets.com/content/dam/shared/legal/terms-of-use.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.acmemarkets.com/content/dam/shared/legal/privacy-policy.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/api-evangelist/acme-markets
- group: company
  title: ''
  type: About
  url: https://www.acmemarkets.com/about-us/mobile-apps.html
created: '2026-05-22'
description: 'Acme Markets is a regional supermarket chain founded in 1891 and headquartered in the U.S. Northeast, operating approximately 164 stores across Pennsylvania, New Jersey, Delaware, New York, Connecticut, and Maryland. Acme is a banner of Albertsons Companies, Inc., one of the largest food and drug retailers in the United States. The brand has no publicly documented developer program or public API: digital surfaces (store locator, loyalty program "ACME for U", FreshPass subscription, DriveUp & Go, delivery, pharmacy) are delivered through Albertsons-shared web and mobile platforms. The Android package ID (`com.safeway.client.android.acme`) confirms that the Acme app is built on the shared Safeway/Albertsons banner application, suggesting a shared backend API surface across Albertsons banners that is not externally published.'
features:
- description: Free loyalty program with personalized deals, digital coupons, and Points redeemable for fuel and groceries.
  name: ACME for U Loyalty
- description: Paid membership providing unlimited free grocery delivery and exclusive member pricing on the Acme e-commerce platform.
  name: FreshPass Subscription
- description: Schedule-based curbside grocery pickup ordered through the website or mobile app.
  name: DriveUp & Go Curbside Pickup
- description: Grocery home delivery across the Northeast service area through the Acme storefront.
  name: Home Delivery
- description: Pharmacy services including prescription refills, transfers, immunizations, and account management.
  name: In-Store Pharmacy
- description: Points earned through ACME for U can be redeemed for cents-off per gallon at participating fuel stations.
  name: Fuel Rewards
- description: In-store mobile app mode surfacing aisle locations and one-tap coupon clipping while shopping.
  name: Store Mode
- description: Native iOS and Android client built on the shared Safeway/Albertsons banner codebase consolidating all shopping surfaces.
  name: Mobile Application
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/acme-markets.png
integrations:
- description: Acme is operated as an Albertsons banner; loyalty, e-commerce, pharmacy, and mobile surfaces share the parent platform.
  name: Albertsons Companies Platform
- description: The Acme Markets mobile app is built on the shared Safeway / Albertsons banner application (Android package `com.safeway.client.android.acme`).
  name: Safeway Mobile Codebase
- description: Cross-banner Albertsons subscription product surfaced on the Acme storefront.
  name: FreshPass Membership
- description: Per-store landing pages delivered via the `local.acmemarkets.com` subdomain, a pattern typical of vendor-hosted local-pages SEO platforms.
  name: Local Pages Platform
layout: provider
modified: '2026-07-25'
name: Acme Markets
nav: Providers
network: true
overview: Acme Markets publishes 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Albertsons Banner, Delivery, E-Commerce, Grocery, and Loyalty.
random_paper: 25
score:
  band: minimal
  composite: 12.3
  delta: -2.6
  facets:
    commercial_clarity: 21.1
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 14.9
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: domain-security
  name: Acme Markets Domain Security
  slug: acme-markets-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: acme-markets
tags:
- Albertsons Banner
- Delivery
- E-Commerce
- Grocery
- Loyalty
- Pharmacy
- Retail
- Store Locator
- Supermarket
use_cases:
- description: Locate the nearest Acme Markets store, departments, hours, and pharmacy services via the store locator.
  name: Store Discovery
- description: Browse the personalized weekly ad, clip digital coupons, and build a shopping list before visiting the store.
  name: Weekly Ad Shopping
- description: Place orders for DriveUp & Go pickup or home delivery through the website or mobile application.
  name: Online Grocery Ordering
- description: Refill prescriptions, transfer pharmacies, and schedule immunizations through the digital pharmacy surface.
  name: Pharmacy Management
- description: Earn and redeem Points across grocery and fuel purchases through the ACME for U program.
  name: Loyalty Engagement
website: https://www.acmemarkets.com
---
