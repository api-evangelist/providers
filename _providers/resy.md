---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
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
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-07-28'
api_count: 3
apis:
- description: 'Partner-only REST API for reservations, availability, and restaurant metadata. Access is granted through Resy''s partnerships team for approved POS, CRM, loyalty, and discovery integrations. No public '
  name: Resy Partner API
  slug: partner-api
- description: Embeddable "Book with Resy" booking button/widget that restaurants and partners can place on their own websites to drive reservations into Resy. This is the primary publicly available integration surf
  name: Resy Booking Widget
  slug: booking-widget
- description: Resy's web and mobile clients communicate with an internal API at api.resy.com. This API is not publicly documented or supported, requires credentials extracted from a logged-in session, and is subjec
  name: Resy Internal Web/Mobile API (Undocumented)
  slug: internal-web-api
artifact_total: 21
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/resy-domain-security.yml
- group: start
  title: ''
  type: Portal
  url: https://resy.com/
- group: company
  title: ''
  type: Blog
  url: https://blog.resy.com/
- group: company
  title: ''
  type: Partners
  url: https://resy.com/join/integrations/
- group: operate
  title: ''
  type: Contact
  url: mailto:api@resy.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/resy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/resy-inc
- group: commercial
  title: ''
  type: Plans
  url: plans/resy-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/resy-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/resy-finops.yml
created: '2026-05-08'
description: Resy is a restaurant reservation and discovery platform owned by American Express. Resy does not maintain a publicly self-serve developer portal; integration is restricted to approved partners (POS, CRM, loyalty, marketing, and discovery) under direct partnership agreements. The primary public surface is the consumer web and mobile app and an embeddable "Book with Resy" booking widget for restaurants. The unofficial internal client API at api.resy.com has been widely reverse-engineered by the community, but it is undocumented, unsupported, and may change without notice.
features:
- description: Online table reservations, waitlists, and notify lists for diners and restaurants.
  name: Reservation Management
- description: Editorial dining guides, curated lists (e.g. the Resy 100), and search across cities.
  name: Restaurant Discovery
- description: Restaurant-facing operating system for table, guest, and reservation management.
  name: Resy OS
- description: Embeddable "Book with Resy" button restaurants place on their own sites.
  name: Booking Widget
- description: Guestbook, guest communications, and reservation notifications.
  name: Guest CRM and Notifications
finops:
- name: Resy Finops
  service_category: Hospitality
  slug: resy-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/resy.png
integrations:
- description: Toast, Square, Lightspeed, Aloha, Micros Simphony, Micros 3700, Heartland Xpient, Positouch, Squirrel, Lavu, Maitre D.
  name: POS Systems
- description: Tripleseat for private events and group bookings.
  name: Events and Bookings
- description: Loyalist, Fishbowl CRM, Bloom Intelligence.
  name: CRM and Guest Management
- description: Reserve with Google, MICHELIN, The Infatuation, Meta, Anthropic, Wine Enthusiast.
  name: Discovery and Distribution
- description: Google Analytics.
  name: Analytics
- description: WineDirect, Commerce7.
  name: Winery and eCommerce
layout: provider
modified: '2026-06-03'
name: Resy
nav: Providers
network: true
overview: 'Resy publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Hospitality, Reservations, Restaurants, Dining, and Booking.


  Resy''s developer surface includes developer portal, engineering blog, and 8 more developer resources.'
plans:
- name: Resy Plans Pricing
  plan_count: 2
  slug: resy-plans-pricing
random_paper: 51
rate_limits:
- limit_count: 1
  name: Resy Rate Limits
  slug: resy-rate-limits
score:
  band: emerging
  composite: 17.9
  delta: -2.2
  facets:
    commercial_clarity: 28.9
    contract_quality: 0.0
    developer_ergonomics: 10.9
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 20.1
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/resy/refs/heads/main/screenshots/resy-2026-06-20T193036.png
security:
- kind: domain-security
  name: Resy Domain Security
  slug: resy-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: resy
tags:
- Hospitality
- Reservations
- Restaurants
- Dining
- Booking
use_cases:
- description: Add the "Book with Resy" booking button to a restaurant website to capture bookings.
  name: Embed Reservations on a Restaurant Site
- description: Approved partners synchronize reservation, guest, and reporting data with POS/CRM systems.
  name: Sync Reservations with POS and CRM
- description: Surface restaurant availability through Resy and partner discovery channels.
  name: Discovery and Marketing Distribution
website: https://resy.com/
---
