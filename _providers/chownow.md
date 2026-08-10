---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
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
  scored_at: '2026-08-10'
api_count: 0
artifact_total: 25
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/chownow-domain-security.yml
- group: start
  title: Website
  type: Portal
  url: https://get.chownow.com
- group: other
  title: ''
  type: Marketplace
  url: https://www.chownow.com
- group: other
  title: Products
  type: Resources
  url: https://get.chownow.com/products/
- group: commercial
  title: ''
  type: Pricing
  url: https://get.chownow.com/pricing/
- group: commercial
  title: ''
  type: Plans
  url: plans/chownow-plans-pricing.yml
- group: other
  title: Demo
  type: Resources
  url: https://get.chownow.com/demo/
- group: company
  title: ''
  type: Blog
  url: https://get.chownow.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://support.chownow.com
- group: other
  title: About
  type: Resources
  url: https://get.chownow.com/about/
- group: other
  title: Careers
  type: Resources
  url: https://chownow.com/careers
- group: company
  title: Partner Program
  type: Partners
  url: https://get.chownow.com/affiliates/partner-signup/
- group: other
  title: Refer A Restaurant
  type: Resources
  url: https://get.chownow.com/refer-a-restaurant/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ChowNow
- group: other
  title: ''
  type: X
  url: https://twitter.com/ChowNow
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/chownow
- group: other
  title: Facebook
  type: Resources
  url: https://www.facebook.com/ChowNow
- group: other
  title: Instagram
  type: Resources
  url: https://www.instagram.com/chownow
created: '2026-05-25'
description: ChowNow is a Playa Vista, Los Angeles-based restaurant technology company providing commission-free online ordering, branded mobile apps, marketing tools, and operational software purpose-built for independent restaurants. Founded in 2011, ChowNow powers ordering websites, native iOS/Android apps, QR-code dine-in ordering, catering, email and SMS marketing, a rewards program, Flex Delivery, order aggregation, and centralized menu management for 20,000+ restaurants. The platform integrates with 20+ point-of-sale systems including Toast, Square, Revel, Clover, Lightspeed, Heartland Genius, Skytab, and PosiTouch, and syndicates restaurant menus through a Discovery Network spanning Google, Apple Maps, Yelp, and other channels, with optional hand-off to DoorDash, UberEats, and Grubhub for last-mile delivery. ChowNow's business model is flat-fee software-as-a-service for restaurants rather than per-order commissions, and the company does not publish a public developer API, SDK, OpenAPI
  specification, webhooks reference, or open developer portal. Third-party integration is handled through pre-built connectors managed inside the restaurant dashboard and a private partnerships program; prospective POS, delivery, and technology partners apply through a partnerships form rather than self-serve API documentation. The company's public GitHub presence consists primarily of forks of open-source Python/JavaScript tooling and archived internal libraries, with no SDK, client library, or specification repositories.
features:
- description: Commission-free direct online ordering for restaurant websites, replacing per-order marketplace commissions with flat-fee SaaS.
  name: Online Ordering
- description: Custom-branded native iOS and Android ordering apps published under the restaurant's own identity.
  name: Branded Mobile Apps
- description: Restaurant website creation with integrated direct ordering.
  name: Website Builder
- description: ChowNow's aggregated consumer ordering marketplace that surfaces member restaurants to diners.
  name: Marketplace
- description: Menu and ordering syndication across Google, Apple Maps, Yelp, Tripadvisor, Snap, and other discovery channels.
  name: Discovery Network
- description: Scan-to-order experience for on-premise dine-in service.
  name: QR Code Dine-In Ordering
- description: Specialized catering and large-order management.
  name: Catering
- description: Customer communication campaigns with contact slots and email/SMS credits scaled by plan tier.
  name: Email And Text Marketing
- description: Customer loyalty and rewards program to drive repeat ordering.
  name: Rewards Program
- description: Flexible last-mile delivery with optional hand-off to DoorDash, UberEats, and Grubhub, billed per delivery order.
  name: Flex Delivery
- description: Consolidation of orders from multiple ordering channels into a single stream sent to the POS or printer.
  name: Order Aggregation
- description: Business analytics, payment insights, and operational reporting.
  name: Advanced Reporting
- description: Pre-built connectors to 20+ point-of-sale systems for direct order injection.
  name: POS Integrations
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/chownow.png
integrations:
- description: Auphan, Brink, Clover Connect, Curv, Dinerware, EPOSnow, Givex, Genius for Restaurants, InTouch POS, Lavu, Lightspeed, Maitre'D, Oracle MICROS, PixelPoint, POSitouch, Revel, Silverware, Skytab, Square, Stream, Toast, Universal POS, Verona, and Volante.
  name: Point Of Sale Systems
- description: DoorDash, Grubhub, Skip, and Uber Eats for last-mile delivery hand-off.
  name: Delivery Apps
- description: Apple Maps, Google, Snap, Tripadvisor, and Yelp.
  name: Discovery Networks
- description: Epson and Star Micronics receipt printers and kitchen display systems.
  name: Printers And KDS
- description: Card processing through ChowNow's transaction-fee model, with payment insights surfaced via Stripe.
  name: Payments
layout: provider
modified: '2026-06-02'
name: ChowNow
nav: Providers
network: true
overview: 'ChowNow is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Restaurants, Online Ordering, Food And Beverage, Restaurant Technology, and Point Of Sale.


  ChowNow''s developer surface includes developer portal, pricing, engineering blog, support, and 14 more developer resources.'
plans:
- name: Chownow Plans Pricing
  plan_count: 4
  slug: chownow-plans-pricing
random_paper: 77
score:
  band: emerging
  composite: 17.1
  delta: 0.0
  facets:
    commercial_clarity: 42.1
    contract_quality: 0.0
    developer_ergonomics: 15.2
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 17.1
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/chownow/refs/heads/main/screenshots/chownow-2026-06-20T174325.png
security:
- kind: domain-security
  name: Chownow Domain Security
  slug: chownow-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: chownow
tags:
- Restaurants
- Online Ordering
- Food And Beverage
- Restaurant Technology
- Point Of Sale
- Delivery
- Catering
- Marketing
- Mobile Apps
- Independent Restaurants
- Commission Free
use_cases:
- description: Independent restaurants take online orders on their own site and apps without paying per-order commissions to marketplaces.
  name: Commission-Free Direct Ordering
- description: Restaurants retain customer contact data and use built-in marketing to drive repeat business rather than renting access from aggregators.
  name: Owning The Customer Relationship
- description: Order aggregation routes web, app, dine-in QR, and third-party delivery orders into one POS or printer workflow.
  name: Unifying Multi-Channel Orders
- description: Syndicating menus and ordering through Google, Apple Maps, and Yelp to capture demand without ceding margin.
  name: Expanding Discovery Reach
- description: Using Flex Delivery to offer last-mile fulfillment on a per-order fee basis instead of marketplace commission tiers.
  name: Adding Delivery Without Commission Lock-In
website: https://get.chownow.com
---
