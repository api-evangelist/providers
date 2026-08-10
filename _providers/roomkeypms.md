---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
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
- acting_count: 1
  human_in_the_loop: 0
  name: Roomkeypms Agentic Access
  operation_count: 8
  slug: roomkeypms-agentic-access
  summary_line: 8 operations · 1 acting
api_count: 3
apis:
- description: Point-of-sale guest lookup and folio charge posting.
  name: RoomKeyPMS POS API
  slug: roomkeypms-pos-api
- description: Pull reservation and guest-profile data by hotel.
  name: RoomKeyPMS Reservation Data API
  slug: roomkeypms-reservation-data-api
- description: Hotel statistics and transaction receipts.
  name: RoomKeyPMS Statistics API
  slug: roomkeypms-statistics-api
artifact_total: 10
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/roomkeypms-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/roomkeypms-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/roomkeypms-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/roomkeypms-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://ca.linkedin.com/company/roomkeypms
- group: company
  title: ''
  type: Website
  url: https://roomkeypms.com/
- group: docs
  title: ''
  type: Documentation
  url: https://support.roomkeypms.com/a/972656-api-documentation
- group: commercial
  title: ''
  type: Plans
  url: plans/roomkeypms-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/roomkeypms-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/roomkeypms-finops.yml
created: '2026-07-03'
description: RoomKeyPMS is a cloud property management system (PMS) for independent hotels and small chains across the US and Canada, with a team of hoteliers behind roughly 70,000 managed rooms. Alongside the core PMS it sells Pulse (AI marketing and guest messaging), Embedded Payments, Capital (growth financing), Mobile Guest, a built-in Distribution/CRS module, and an integrations marketplace. RoomKeyPMS publishes a real REST API (JSON or XML, selectable via request header) documented publicly at its support portal under three API types - Pulling Reservation Data, POS, and Statistics and Forecasts. The API is described as "a one-way interface that allows you to draw out key data from your hotel or chain environment" for use in marketing (e.g. exporting guest lists to MailChimp) and BI tools (e.g. Cvent). It is partner-gated - a hotel's IT team must email RoomKeyPMS support and the property must sign off before an API key and per-hotel credentials are issued - so no open self-serve signup
  or public sandbox exists. Endpoint paths and query parameters below are taken directly from RoomKeyPMS's own published support articles; the exact API base host is inferred from the same documentation (RoomKeyPMS hosts its interactive Help/reference pages alongside the live API) and should be confirmed once credentials are issued.
finops:
- name: Roomkeypms Finops
  service_category: Hospitality Property Management System
  slug: roomkeypms-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/roomkeypms.png
layout: provider
modified: '2026-07-03'
name: RoomKeyPMS
nav: Providers
network: true
overview: 'RoomKeyPMS publishes 3 APIs on the [APIs.io](https://apis.io/) network: POS API, Reservation Data API, and Statistics API. Tagged areas include Hospitality, Hotel Technology, Property Management System, PMS, and Reservations.


  RoomKeyPMS''s developer surface includes authentication, documentation, and 8 more developer resources.'
plans:
- name: Roomkeypms Plans Pricing
  plan_count: 2
  slug: roomkeypms-plans-pricing
random_paper: 66
rate_limits:
- limit_count: 4
  name: Roomkeypms Rate Limits
  slug: roomkeypms-rate-limits
score:
  band: thin
  composite: 36.5
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 61.2
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 36.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
security:
- kind: authentication
  name: Roomkeypms Authentication
  slug: roomkeypms-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Roomkeypms Domain Security
  slug: roomkeypms-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Roomkeypms Vulnerability Disclosure
  slug: roomkeypms-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: roomkeypms
tags:
- Hospitality
- Hotel Technology
- Property Management System
- PMS
- Reservations
- POS
- Gated API
website: https://roomkeypms.com/
---
