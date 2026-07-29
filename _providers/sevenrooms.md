---
access_model:
  confidence: medium
  label: Paid · Requires approval
  onboarding: approval
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
api_count: 1
apis:
- description: The SevenRooms API is a RESTful interface for hospitality data and operations. It exposes reservations, guest profiles, and feedback scores, and supports retrieving venue info, searching shift-level a
  name: SevenRooms API
  slug: rest-api
artifact_total: 27
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/sevenrooms-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sevenrooms-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://sevenrooms.com/
- group: docs
  title: ''
  type: Documentation
  url: https://api-docs.sevenrooms.com/
- group: docs
  title: ''
  type: APIReference
  url: https://sevenrooms.com/platform/integrations-apis/
- group: start
  title: Partnerships / API Access Request
  type: Signup
  url: https://sevenrooms.com/lets-talk/
- group: start
  title: ''
  type: Login
  url: https://www.sevenrooms.com/login
- group: operate
  title: API Integration Support (api-integration-support@sevenrooms.com)
  type: Support
  url: https://api-docs.sevenrooms.com/
- group: company
  title: ''
  type: Blog
  url: https://sevenrooms.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/sevenrooms
- group: commercial
  title: Quote-Based (Request a Demo)
  type: Pricing
  url: https://sevenrooms.com/request-a-demo/
- group: commercial
  title: ''
  type: Plans
  url: plans/sevenrooms-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/sevenrooms-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/sevenrooms-finops.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://sevenrooms.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://sevenrooms.com/privacy-policy/
- group: auth
  title: Data Processing Addendum
  type: Compliance
  url: https://sevenrooms.com/dpa/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/sevenrooms
- group: other
  title: ''
  type: X
  url: https://x.com/sevenrooms
created: '2026-06-02'
description: SevenRooms is a guest experience, reservations, and retention platform for the hospitality industry, helping restaurants, hotels, nightlife, and entertainment venues manage reservations, waitlists, CRM, and marketing. Founded in 2011 and serving clients in more than 1,000 cities worldwide, the platform unifies a restaurant tech stack with 100-plus integrations across POS, payments, booking channels, delivery, and marketing tools, plus a flexible RESTful API. The API exposes reservation, guest profile, and feedback data and supports searching availability and creating bookings. Access to the partner-facing developer documentation is gated to approved venue operators and integration partners via individually provisioned accounts (as of February 26, SevenRooms moved to individually provisioned documentation accounts).
features:
- description: Real-time availability, online and in-house bookings, and waitlist management across shifts and seating areas.
  name: Reservations & Waitlist
- description: Automatic guest profile building that centralizes preferences, visit history, spend, and tags for personalized service.
  name: CRM & Guest Profiles
- description: Seating optimization and floor-plan control for venue operations.
  name: Table & Floor Management
- description: Automated, multi-channel marketing campaigns driven by guest profile and behavioral data.
  name: Email & SMS Marketing
- description: Guest retention, rewards, and perks programs.
  name: Loyalty & Perks
- description: Booking and management of private dining and special events.
  name: Event & Private Dining Management
- description: Review monitoring and response across feedback channels.
  name: Reputation Management
- description: AI-powered phone reservation automation and phone-to-booking conversion.
  name: Voice AI
- description: Direct-to-consumer online ordering platform.
  name: Online Ordering
- description: Business intelligence dashboards for venue performance.
  name: Reporting & Analytics
finops:
- name: Sevenrooms Finops
  service_category: Hospitality Guest Experience Software
  slug: sevenrooms-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sevenrooms.png
integrations:
- description: 35-plus point-of-sale integrations including Square, Toast, Lightspeed, MICROS Simphony, NCR Aloha, Revel, and SpotOn.
  name: POS Systems
- description: Stripe, Adyen, CyberSource, FreedomPay, and Network International.
  name: Payments
- description: Google, Facebook, Instagram, TheFork, TripAdvisor, Reserveout, Chope, and OpenRice.
  name: Booking Channels
- description: DoorDash Drive, Olo, Deliverect, ItsaCheckmate, Drive Yello, and Orkestro.
  name: Delivery & Pickup
- description: Twilio, SMSGlobal, Bookline, Slang, Amazon Alexa, and VoiceMpower.
  name: SMS & Voice
- description: Mailchimp, Emma, and Widewail.
  name: Marketing & CRM
- description: Revinate, Journey, Tripleseat, and iVvy.
  name: Hotel & Events
layout: provider
modified: '2026-06-03'
name: SevenRooms
nav: Providers
network: true
overview: 'SevenRooms publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Restaurant, Reservations, Waitlist, CRM, and Marketing.


  SevenRooms'' developer surface includes documentation, API reference, signup flow, support, engineering blog, pricing, and 13 more developer resources.'
plans:
- name: Sevenrooms Plans Pricing
  plan_count: 2
  slug: sevenrooms-plans-pricing
random_paper: 52
rate_limits:
- limit_count: 2
  name: Sevenrooms Rate Limits
  slug: sevenrooms-rate-limits
score:
  band: thin
  composite: 31.6
  delta: -2.1
  facets:
    commercial_clarity: 89.5
    contract_quality: 0.0
    developer_ergonomics: 21.7
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 33.7
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sevenrooms/refs/heads/main/screenshots/sevenrooms-2026-06-20T193741.png
security:
- kind: domain-security
  name: Sevenrooms Domain Security
  slug: sevenrooms-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Sevenrooms Trust Center
  slug: sevenrooms-trust-center
  summary_line: SOC 2, PCI DSS, GDPR
slug: sevenrooms
tags:
- Restaurant
- Reservations
- Waitlist
- CRM
- Marketing
- Hospitality
- Guest Experience
use_cases:
- description: Consolidate reservations, CRM, marketing, and operations across 100-plus integrations into a single hospitality platform.
  name: Unify the Restaurant Tech Stack
- description: Accept and synchronize bookings across discovery and booking channels such as Google, TheFork, and TripAdvisor.
  name: Multi-Channel Reservation Distribution
- description: Retrieve venue info, search shift-level availability, and create, modify, or cancel reservations via the RESTful API.
  name: Programmatic Availability & Booking
- description: Build unified guest profiles from reservations, POS, payments, and WiFi capture to drive personalized marketing and service.
  name: Guest Data Capture & Personalization
website: https://sevenrooms.com/
---
