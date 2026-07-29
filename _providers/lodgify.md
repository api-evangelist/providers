---
access_model:
  confidence: high
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: true
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 11
  human_in_the_loop: 0
  name: Lodgify Agentic Access
  operation_count: 23
  slug: lodgify-agentic-access
  summary_line: 23 operations · 11 acting
api_count: 6
apis:
- description: Availability calendars for properties and room types.
  name: Lodgify Availability API
  slug: lodgify-availability-api
- description: Booking and reservation lifecycle management.
  name: Lodgify Bookings API
  slug: lodgify-bookings-api
- description: Guest conversation threads and messages.
  name: Lodgify Messaging API
  slug: lodgify-messaging-api
- description: Vacation rental properties and their room types.
  name: Lodgify Properties API
  slug: lodgify-properties-api
- description: Daily rates, rate settings, and priced stay quotes.
  name: Lodgify Rates & Quotes API
  slug: lodgify-rates-quotes-api
- description: Event subscriptions for real-time notifications.
  name: Lodgify Webhooks API
  slug: lodgify-webhooks-api
artifact_total: 13
collections:
- collection_type: open
  name: Lodgify Public API
  slug: open-lodgify
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/lodgify-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lodgify-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/lodgify-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/lodgify
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/lodgify
- group: company
  title: ''
  type: Website
  url: https://www.lodgify.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.lodgify.com
- group: commercial
  title: ''
  type: Plans
  url: plans/lodgify-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/lodgify-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/lodgify-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.lodgify.com/blog/feed/
created: '2026-06-25'
description: Lodgify is all-in-one vacation rental software for property owners and managers, providing a website builder, booking engine, channel manager, and property management system. The Lodgify Public API (v1 and v2) exposes a REST interface at https://api.lodgify.com for managing properties, availability, rates and quotes, bookings and reservations, guest messaging, and webhook subscriptions, authenticated with an X-ApiKey header.
finops:
- name: Lodgify Finops
  service_category: Vacation Rental Software
  slug: lodgify-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/lodgify.png
layout: provider
modified: '2026-06-25'
name: Lodgify
nav: Providers
network: true
overview: 'Lodgify publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Availability API, Bookings API, Messaging API, and 3 more. Tagged areas include Vacation Rental, Property Management, Booking, Channel Manager, and Travel.


  Lodgify''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Lodgify Plans Pricing
  plan_count: 4
  slug: lodgify-plans-pricing
random_paper: 57
rate_limits:
- limit_count: 1
  name: Lodgify Rate Limits
  slug: lodgify-rate-limits
score:
  band: thin
  composite: 38.1
  delta: -2.2
  facets:
    commercial_clarity: 39.5
    contract_quality: 60.2
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 40.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lodgify/refs/heads/main/screenshots/lodgify-2026-07-25T225448.png
security:
- kind: authentication
  name: Lodgify Authentication
  slug: lodgify-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Lodgify Domain Security
  slug: lodgify-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: lodgify
tags:
- Vacation Rental
- Property Management
- Booking
- Channel Manager
- Travel
website: https://www.lodgify.com
---
