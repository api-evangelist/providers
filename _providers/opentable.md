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
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 6.7
  scored_at: '2026-07-23'
api_count: 2
apis:
- description: Restricted REST API for approved partners covering restaurant content, availability, reservations, and CRM. Access is granted through the OpenTable Partner Portal under contractual agreement.
  name: OpenTable Partner API
  slug: partner-api
- description: Widget and reservation embeds for affiliate sites, plus restaurant search/availability for approved partners.
  name: OpenTable Affiliate / Restaurant Search Widgets
  slug: affiliate-api
artifact_total: 16
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/opentable-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/opentable
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/opentable
- group: company
  title: ''
  type: Website
  url: https://www.opentable.com/
- group: other
  title: ''
  type: Developer
  url: https://dev.opentable.com/partner-portal
- group: docs
  title: ''
  type: Documentation
  url: https://docs.opentable.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.opentable.com/restaurant-solutions/plans/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.opentable.com/
- group: operate
  title: ''
  type: Support
  url: https://support.opentable.com/
- group: operate
  title: ''
  type: FAQ
  url: https://www.opentable.com/restaurant-solutions/api-partners/faqs/
- group: build
  title: HorizonCalendar (Swift Calendar UI)
  type: Tools
  url: https://github.com/opentable/HorizonCalendar
- group: build
  title: otj-pg-embedded (Java Embedded PostgreSQL)
  type: Tools
  url: https://github.com/opentable/otj-pg-embedded
- group: build
  title: spur-ioc (Node.js Dependency Injection)
  type: Tools
  url: https://github.com/opentable/spur-ioc
- group: build
  title: mercury-bot (Static Translation Bot)
  type: Tools
  url: https://github.com/opentable/mercury-bot
- group: build
  title: eslint-config-opentable (Shared ESLint Config)
  type: Tools
  url: https://github.com/opentable/eslint-config-opentable
- group: commercial
  title: ''
  type: Plans
  url: plans/opentable-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/opentable-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/opentable-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.opentable.com/blog/feed/
created: '2026-05-08'
description: OpenTable is a global restaurant reservation platform owned by Booking Holdings. The OpenTable Partner Portal exposes restricted partner APIs for reservations, availability, restaurant content, reviews, and CRM integrations to approved partners.
features:
- description: Programmatic access to restaurant profiles, locations, and metadata for approved partners.
  name: Restaurant Content and Directory
- description: Real-time table availability lookups and reservation booking for partner experiences.
  name: Availability and Reservations
- description: Access to diner reviews and guest/CRM data for approved integrations under contract.
  name: Reviews and Guest Data
- description: Approved partners receive a sandbox for discovery and testing before production access.
  name: Sandbox Environment
finops:
- name: Opentable Finops
  service_category: Hospitality
  slug: opentable-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/opentable.png
integrations:
- description: OpenTable integrates with point-of-sale systems to sync reservations, covers, and guest spend data with restaurant operations.
  name: POS Integrations
- description: Guest profile, reservation, and review data can flow to partner CRM and marketing tools through approved partner integrations.
  name: CRM and Marketing Platforms
- description: Affiliate sites and third-party platforms embed OpenTable reservation widgets and deep links to surface real-time availability and drive bookings.
  name: Affiliate and Booking Widgets
layout: provider
modified: '2026-06-03'
name: OpenTable
nav: Providers
network: true
overview: 'OpenTable publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Hospitality, Reservations, and Restaurants.


  OpenTable''s developer surface includes documentation, pricing, support, FAQ, tooling, engineering blog, and 13 more developer resources.'
plans:
- name: Opentable Plans Pricing
  plan_count: 2
  slug: opentable-plans-pricing
random_paper: 36
rate_limits:
- limit_count: 1
  name: Opentable Rate Limits
  slug: opentable-rate-limits
score:
  band: emerging
  composite: 23.2
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 0.0
    developer_ergonomics: 15.2
    discoverability: 67.5
    governance: 0.0
    operational_transparency: 42.1
  previous_composite: 23.2
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/opentable/refs/heads/main/screenshots/opentable-2026-06-20T191050.png
security:
- kind: domain-security
  name: Opentable Domain Security
  slug: opentable-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: opentable
tags:
- Hospitality
- Reservations
- Restaurants
use_cases:
- description: Third-party apps and sites embed availability and booking flows to let diners reserve tables without leaving the partner experience.
  name: Embedded Restaurant Booking
- description: Restaurants connect OpenTable to POS, CRM, and operations systems to unify reservation and guest data.
  name: Tech Stack Integration
- description: Affiliate partners surface OpenTable availability and earn from referred reservations.
  name: Affiliate Referrals
website: https://www.opentable.com/
---
