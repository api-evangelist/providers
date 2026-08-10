---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Guesty Agentic Access
  operation_count: 10
  slug: guesty-agentic-access
  summary_line: 10 operations · 2 acting
api_count: 5
apis:
- description: Listing availability and pricing
  name: Guesty Calendars API
  slug: guesty-calendars-api
- description: Guest communication threads
  name: Guesty Conversations API
  slug: guesty-conversations-api
- description: Guest profiles
  name: Guesty Guests API
  slug: guesty-guests-api
- description: Property listings
  name: Guesty Listings API
  slug: guesty-listings-api
- description: Bookings and reservations
  name: Guesty Reservations API
  slug: guesty-reservations-api
artifact_total: 12
collections:
- collection_type: open
  name: Guesty Open API
  slug: open-guesty
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/guesty-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/guesty-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/guesty-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/guestyorg
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/guesty
- group: start
  title: ''
  type: Portal
  url: https://open-api-docs.guesty.com/
- group: company
  title: ''
  type: Website
  url: https://www.guesty.com/
- group: start
  title: ''
  type: Signup
  url: https://app.guesty.com/register
- group: operate
  title: ''
  type: Support
  url: https://help.guesty.com/
- group: company
  title: ''
  type: Blog
  url: https://www.guesty.com/blog/
- group: docs
  title: ''
  type: APIReference
  url: https://open-api-docs.guesty.com/reference
- group: agent
  title: ''
  type: LlmsText
  url: https://open-api-docs.guesty.com/llms.txt
created: '2025-02-12'
description: Guesty is a property management platform for short-term rental businesses. The Guesty Open API provides programmatic access to manage properties, reservations, guests, and operations across multiple listing channels.
finops:
- name: Guesty Finops
  service_category: API
  slug: guesty-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/guesty.png
layout: provider
modified: '2026-05-19'
name: Guesty
nav: Providers
network: true
overview: 'Guesty publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Calendars API, Conversations API, Guests API, and 2 more. Tagged areas include Booking, Hospitality, Property Management, Reservations, and Short-Term Rentals.


  Guesty''s developer surface includes authentication, developer portal, signup flow, support, engineering blog, API reference, and 6 more developer resources.'
plans:
- name: Guesty Plans Pricing
  plan_count: 3
  slug: guesty-plans-pricing
random_paper: 93
rate_limits:
- limit_count: 5
  name: Guesty Rate Limits
  slug: guesty-rate-limits
score:
  band: thin
  composite: 41.2
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 58.3
    developer_ergonomics: 32.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 41.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/guesty/refs/heads/main/screenshots/guesty-2026-06-20T182431.png
security:
- kind: authentication
  name: Guesty Authentication
  slug: guesty-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Guesty Domain Security
  slug: guesty-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: guesty
tags:
- Booking
- Hospitality
- Property Management
- Reservations
- Short-Term Rentals
- Vacation Rentals
website: https://www.guesty.com/
---
