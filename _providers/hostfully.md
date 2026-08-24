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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.0
  scored_at: '2026-08-24'
api_count: 2
apis:
- description: Hostfully Property Management Platform REST API v3.x covering properties (single and multi-unit), leads (inquiries, booking requests, bookings, group bookings, holds, cancellations, rebooking), orders
  name: Hostfully REST API
  slug: hostfully-rest-api
- description: Hostfully GraphQL endpoint for executing queries and mutations against the same underlying property-management domain as the REST API. Useful for clients that need to shape responses, fetch multi-reso
  name: Hostfully GraphQL API
  slug: hostfully-graphql-api
artifact_total: 24
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hostfully-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.hostfully.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dev.hostfully.com
- group: docs
  title: ''
  type: Documentation
  url: https://dev.hostfully.com/reference/getting-started
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.hostfully.com
- group: commercial
  title: ''
  type: Pricing
  url: https://www.hostfully.com/pricing/property-management-software/
- group: commercial
  title: ''
  type: Plans
  url: ''
- group: operate
  title: ''
  type: RateLimits
  url: https://dev.hostfully.com/reference/getting-started
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/hostfully
- group: other
  title: ''
  type: ChannelManager
  url: https://www.hostfully.com/property-management-software/features/channel-manager/
- group: other
  title: ''
  type: Product
  url: https://www.hostfully.com/property-management-software/
- group: other
  title: ''
  type: Product
  url: https://www.hostfully.com/digital-guidebooks/
- group: company
  title: ''
  type: Partners
  url: https://www.hostfully.com/partners/
- group: company
  title: ''
  type: Blog
  url: https://www.hostfully.com/blog/
- group: other
  title: ''
  type: Customers
  url: https://www.hostfully.com/customers/
- group: start
  title: ''
  type: Signup
  url: https://www.hostfully.com/sign-up/
- group: start
  title: ''
  type: Login
  url: https://platform.hostfully.com/login
- group: operate
  title: ''
  type: Contact
  url: https://www.hostfully.com/contact/
- group: company
  title: ''
  type: About
  url: https://www.hostfully.com/about/
- group: company
  title: ''
  type: Careers
  url: https://www.hostfully.com/careers/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.hostfully.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.hostfully.com/privacy-policy/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/hostfully
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/hostfully
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/hostfully
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@Hostfully
created: '2026-05-25'
description: Hostfully is a San Francisco-based short-term rental (STR) property management platform serving vacation rental managers, property managers, and hospitality operators worldwide. The Hostfully Property Management Platform (PMP) provides a channel manager that syncs listings across 60+ booking channels including Airbnb, Vrbo, and Booking.com (where Hostfully holds preferred/elite partner status), a central calendar, unified inbox with InboxAI for guest communication, direct booking site builder, automation and task management, multi-unit and group-booking management, payment processing via Stripe/PayPal/VRP, owner portal, mobile apps for iOS and Android, and digital guidebooks. The platform manages 62,000+ properties for 40,000+ customers, processing 96,000+ bookings monthly. Hostfully exposes a developer-grade public REST API (v3.3) and a GraphQL API for partners and property managers, supporting OAuth 2.0 authorization-code, basic auth, and X-HOSTFULLY-APIKEY authentication,
  cursor-based pagination, webhooks for agency/booking/property/messaging/custom-data events, and a 10,000 calls/hour per-client rate limit. The API is offered as an add-on across the Growth, Pro, and Enterprise Property Management Software plans.
features:
- REST API v3.3 covering Properties, Leads, Bookings, Group Bookings, Orders, Fees, Owner Adjustments, Messaging, Webhooks, Photos, Amenities, Jobs, Custom Data, Agencies, Employees, Owners, Guests, and Reviews
- GraphQL API endpoint for shaped queries and mutations across the property-management domain
- OAuth 2.0 Authorization Code Flow for partner-to-customer authorization
- X-HOSTFULLY-APIKEY header authentication for direct account access
- Basic Auth for partner OAuth token exchange
- 10,000 calls per hour per client rate limit with x-ratelimit-* response headers
- Cursor-based pagination across list endpoints
- Sandbox environment for partner integration testing prior to production approval
- Webhooks for booking, property, messaging, custom-data, pincode, and partner-channel events with POST_JSON or POST_FORM callback formats
- Multi-unit (hotel) property management with master/sub-unit hierarchy
- Group bookings spanning multi-unit properties with main-lead and sub-lead structure
- Channel manager integrations with Airbnb, Vrbo, Booking.com, and 60+ OTAs (Hostfully holds Preferred/Elite Partner status)
- 100+ third-party software partner integrations (dynamic pricing, smart locks, cleaning, accounting, CRM, analytics)
- InboxAI unified messaging across channels (email, Airbnb, Vrbo, Booking.com)
- Direct booking site builder with DBS (Direct Booking System) settings exposed via API
- Per-property monthly subscription pricing across Growth ($15), Pro ($25), and Enterprise (custom) plans
- Open API offered as add-on across all PMP plans
- Digital Guidebooks product available standalone
- Screen & Protect guest screening and damage protection up to $50K
- Hostfully Devices smart-home integrations
graphqls:
- description: Hostfully GraphQL endpoint for executing queries and mutations against the same underlying property-management domain as the REST API. Useful for clients that need to shape responses, fetch multi-reso
  name: Hostfully GraphQL API
  slug: hostfully-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/hostfully.png
layout: provider
modified: '2026-05-25'
name: Hostfully
nav: Providers
network: true
overview: 'Hostfully publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Short-Term Rental, Vacation Rental, Property Management, PMS, and Hospitality.


  Hostfully''s developer surface includes documentation, pricing, engineering blog, signup flow, YouTube channel, and 20 more developer resources.'
random_paper: 15
score:
  band: emerging
  composite: 18.9
  delta: 0.0
  facets:
    access_clarity: 38.2
    commercial_clarity: 38.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 66.7
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 18.9
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hostfully/refs/heads/main/screenshots/hostfully-2026-06-20T182842.png
security:
- kind: domain-security
  name: Hostfully Domain Security
  slug: hostfully-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: hostfully
tags:
- Short-Term Rental
- Vacation Rental
- Property Management
- PMS
- Hospitality
- Channel Manager
- Direct Booking
- Real-Estate
- Travel
- Booking
- Reservations
- Guest Communication
- Webhook
- GraphQL
- Authentication
website: https://www.hostfully.com
---
