---
access_model:
  confidence: high
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
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
- acting_count: 0
  human_in_the_loop: 0
  name: Bookingcom Agentic Access
  operation_count: 1
  slug: bookingcom-agentic-access
  summary_line: 1 operation
api_count: 1
apis:
- description: Travel operations
  name: Booking.com Travel API
  slug: bookingcom-travel-api
artifact_total: 9
collections:
- collection_type: open
  name: Booking.com API
  slug: open-bookingcom-booking-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/bookingcom-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/bookingcom-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bookingcom-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/bookingcom-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bookingcom
- group: company
  title: ''
  type: Website
  url: https://www.booking.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.booking.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.booking.com/demand/docs/getting-started/overview
- group: other
  title: ''
  type: AffiliateProgram
  url: https://www.booking.com/affiliate-program/v2/
- group: company
  title: ''
  type: ConnectivityPartners
  url: https://developers.booking.com/connectivity/docs
- group: company
  title: ''
  type: About
  url: https://www.booking.com/content/about.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.booking.com/content/privacy.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.booking.com/content/terms.html
- group: agent
  title: ''
  type: LlmsText
  url: https://developers.booking.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://news.booking.com/feed/
created: '2024-01-01'
description: Booking.com is the world's leading online travel platform for accommodations, offering over 28 million listings including hotels, apartments, villas, homes, and unique places to stay. Part of Booking Holdings, Booking.com provides APIs for affiliate partners and connectivity partners to integrate its extensive travel inventory into third-party applications and property management systems.
finops:
- name: Bookingcom Finops
  service_category: Travel & Hospitality
  slug: bookingcom-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bookingcom.png
layout: provider
modified: '2026-05-19'
name: Booking.com
nav: Providers
network: true
overview: 'Booking.com publishes 1 API on the [APIs.io](https://apis.io/) network: Travel API. Tagged areas include Accommodations, Affiliates, Connectivity, Hospitality, and Hotels.


  Booking.com''s developer surface includes authentication, documentation, engineering blog, and 12 more developer resources.'
plans:
- name: Bookingcom Plans Pricing
  plan_count: 2
  slug: bookingcom-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 2
  name: Bookingcom Rate Limits
  slug: bookingcom-rate-limits
score:
  band: thin
  composite: 41.8
  delta: -2.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 61.9
    developer_ergonomics: 30.4
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 43.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bookingcom/refs/heads/main/screenshots/bookingcom-2026-06-20T173603.png
security:
- kind: authentication
  name: Bookingcom Authentication
  slug: bookingcom-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Bookingcom Domain Security
  slug: bookingcom-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Bookingcom Vulnerability Disclosure
  slug: bookingcom-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: bookingcom
tags:
- Accommodations
- Affiliates
- Connectivity
- Hospitality
- Hotels
- Reservations
- Travel
website: https://www.booking.com
---
