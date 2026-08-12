---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
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
  scored_at: '2026-08-11'
api_count: 1
apis:
- description: Roomstorm's B2B hotel-room marketplace REST API (Django REST framework backend). Documented in API Blueprint, it covers a bootstrap discovery endpoint, JWT username/password authentication, hotel sear
  name: Roomstorm API
  slug: roomstorm-api
artifact_total: 3
common:
- group: commercial
  title: ''
  type: License
  url: https://github.com/walksource/roomstorm-api/blob/master/LICENSE
- group: auth
  title: ''
  type: DomainSecurity
  url: security/roomstorm-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.roomstorm.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/walksource
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/walksource/roomstorm-api
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/roomstorm-llms.txt
created: '2026-07-17'
description: Roomstorm is a real-time B2B hotel room marketplace, best known for building the airline industry's first fully automated platform for providing hotel accommodations to distressed passengers during flight disruptions. Founded by Maksim Izmaylov and backed by Y Combinator (Summer 2014), the San Francisco company connects airlines, hotels, and travelers so that irregular-operations (IROPS) rebooking, room sourcing, invoicing, and voucher issuance happen programmatically instead of through manual phone calls. Its backend exposes a JSON REST API (documented in API Blueprint) covering authentication, bookings, hotels, rooms, vacancies, organizations, vouchers, and airport search.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/roomstorm.png
layout: provider
modified: '2026-07-21'
name: Roomstorm
nav: Providers
network: true
overview: Roomstorm publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Travel, Hospitality, Hotels, and Airlines.
random_paper: 82
score:
  band: minimal
  composite: 8.3
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 8.3
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
security:
- kind: authentication
  name: Roomstorm Authentication
  slug: roomstorm-authentication
  summary_line: http/cookie · 2 schemes
- kind: domain-security
  name: Roomstorm Domain Security
  slug: roomstorm-domain-security
  summary_line: TLSv1.3 · HSTS
slug: roomstorm
tags:
- Company
- Travel
- Hospitality
- Hotels
- Airlines
- Marketplace
- Bookings
- Y Combinator
website: https://www.roomstorm.com/
---
