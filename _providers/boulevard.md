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
  scored_at: '2026-07-27'
api_count: 7
apis:
- description: Query and mutate client (customer) records synced from Boulevard's CRM - profiles, contact details, custom fields, loyalty point balances, and appointment history. Third parties such as Klaviyo and Ex
  name: Boulevard Admin API - Clients & CRM
  slug: boulevard-admin-clients-crm-api
- description: Read and sync appointment, staff, and location data across a business's calendar - past, current, and future appointments, professional rosters, and the physical/virtual locations services are deliver
  name: Boulevard Admin API - Appointments, Staff & Locations
  slug: boulevard-admin-appointments-scheduling-api
- description: 'Access recurring membership and prepaid package data - plan status, renewal state, and entitlements. Membership lifecycle changes are also pushed outbound as MEMBERSHIP_CREATED, MEMBERSHIP_CANCELLED, '
  name: Boulevard Admin API - Memberships & Packages
  slug: boulevard-admin-memberships-packages-api
- description: Issue and manage stored-value gift cards, service vouchers, and account credit adjustments as a certified payment facilitator. Documented mutations include `CreateGiftCard`, `vouchersCreate`, and `cre
  name: Boulevard Admin API - Payments, Gift Cards & Vouchers
  slug: boulevard-admin-payments-gift-cards-api
- description: Build custom, on-brand self-booking experiences on top of a cart workflow - create a cart for a location, add a selected purchasable (service) item, reserve an available timeslot, attach a tokenized c
  name: Boulevard Client API - Booking Cart & Checkout
  slug: boulevard-client-booking-cart-api
- description: Public-facing catalog reads that power a booking widget before a client ever creates a cart - business and location lookup, bookable service categories, staff/professional listings, and bookable dates
  name: Boulevard Client API - Catalog & Availability
  slug: boulevard-client-catalog-availability-api
- description: A narrow, non-GraphQL REST endpoint (`POST https://vault.blvd.co/cards/tokenize`, confirmed in the public `promotion-demo` reference client's source) used to exchange raw card details for a reusable p
  name: Boulevard Tokenization API
  slug: boulevard-tokenization-api
artifact_total: 13
collections:
- collection_type: open
  name: Boulevard API
  slug: open-boulevard
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/boulevard-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Boulevard
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/boulevard
- group: company
  title: ''
  type: Website
  url: https://www.joinblvd.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.joinblvd.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/boulevard-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/boulevard-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/boulevard-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.joinblvd.com/rss.xml
created: '2026-07-03'
description: Boulevard is a client experience platform purpose-built for appointment-based self-care businesses - hair salons, spas, medspas, barbershops, and nail salons. The platform covers self-scheduling, CRM, marketing, payments (as a certified PayFac), and reporting. Boulevard exposes its integration surface as GraphQL - a Client API for building custom booking experiences and an Admin API for syncing business operations data (clients, appointments, staff, locations, memberships, gift cards) - plus a separate Tokenization API for PCI-scope-reducing card capture. API access is gated to the Enterprise tier and provisioned through a developer sandbox (business ID + API key) via the Boulevard Developer Portal.
finops:
- name: Boulevard Finops
  service_category: Vertical SaaS - Salon, Spa & Med Spa Management
  slug: boulevard-finops
graphqls:
- description: Boulevard exposes two distinct, confirmed GraphQL surfaces plus one adjacent REST endpoint. All three require an Enterprise-tier Boulevard account and are provisioned through the Boulevard Developer P
  name: Boulevard GraphQL APIs
  slug: boulevard-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/boulevard.png
layout: provider
modified: '2026-07-03'
name: Boulevard
nav: Providers
network: true
overview: 'Boulevard publishes 7 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Salon Software, Spa Software, Med Spa, Appointment Scheduling, and GraphQL.


  Boulevard''s developer surface includes documentation, engineering blog, and 7 more developer resources.'
plans:
- name: Boulevard Plans Pricing
  plan_count: 5
  slug: boulevard-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 4
  name: Boulevard Rate Limits
  slug: boulevard-rate-limits
score:
  band: emerging
  composite: 23.1
  delta: 2.8
  facets:
    commercial_clarity: 39.5
    contract_quality: 0.0
    developer_ergonomics: 10.9
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 20.3
  regulatory:
    applies: true
    regime: Payments
    regime_id: payments
    score: 13.0
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/boulevard/refs/heads/main/screenshots/boulevard-2026-07-25T203646.png
security:
- kind: domain-security
  name: Boulevard Domain Security
  slug: boulevard-domain-security
  summary_line: TLSv1.3 · DMARC
slug: boulevard
tags:
- Salon Software
- Spa Software
- Med Spa
- Appointment Scheduling
- GraphQL
- CRM
- Payments
- Self-Care
website: https://www.joinblvd.com/
---
