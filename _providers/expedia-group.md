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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 44.1
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 22
  human_in_the_loop: 0
  name: Expedia Group Agentic Access
  operation_count: 49
  slug: expedia-group-agentic-access
  summary_line: 49 operations · 22 acting
api_count: 15
apis:
- description: The primary itinerary method of the Booking API creates a reservation for the selected hotel, room, rate and occupancy.
  name: Expedia Group Bookings API
  slug: expedia-group-bookings-api
- description: This section outlines the API calls available to you to access property content.
  name: Expedia Group Content API
  slug: expedia-group-content-api
- description: The Deposit resource
  name: Expedia Group Deposit API
  slug: expedia-group-deposit-api
- description: The EPS Geography API provides geography content for regions around the world.
  name: Expedia Group Geography API
  slug: expedia-group-geography-api
- description: Template Loyalty Earn API
  name: Expedia Group Loyalty API
  slug: expedia-group-loyalty-api
- description: Retrieve existing itineraries or cancel existing rooms.
  name: Expedia Group Manage Booking API
  slug: expedia-group-manage-booking-api
- description: Requests test notifications and undelivered notifications.
  name: Expedia Group Notifications API
  slug: expedia-group-notifications-api
- description: The OrderPurchaseScreen API from Expedia Group — 1 operation(s) for orderpurchasescreen.
  name: Expedia Group OrderPurchaseScreen API
  slug: expedia-group-orderpurchasescreen-api
- description: The OrderPurchaseUpdate API from Expedia Group — 1 operation(s) for orderpurchaseupdate.
  name: Expedia Group OrderPurchaseUpdate API
  slug: expedia-group-orderpurchaseupdate-api
- description: The property resource
  name: Expedia Group Property API
  slug: expedia-group-property-api
- description: The rate plan resource
  name: Expedia Group Rate Plan API
  slug: expedia-group-rate-plan-api
- description: Manage room types Rate Verification Thresholds
  name: Expedia Group Rate Verification Thresholds API
  slug: expedia-group-rate-verification-thresholds-api
- description: Manage room type amenities
  name: Expedia Group Room Type Amenities API
  slug: expedia-group-room-type-amenities-api
- description: Manage room types
  name: Expedia Group Room Type API
  slug: expedia-group-room-type-api
- description: The EPS shopping APIs provide you with access to live rates & availability.
  name: Expedia Group Shopping API
  slug: expedia-group-shopping-api
artifact_total: 25
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/expedia-group-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/expedia-group-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/expedia-group-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/expedia-group-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/expediagroup
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/expediagroup
- group: start
  title: ''
  type: Portal
  url: https://developers.expediagroup.com/docs/
- group: build
  title: ''
  type: SDKs
  url: https://developers.expediagroup.com/docs/sdk
- group: company
  title: ''
  type: Blog
  url: https://medium.com/expedia-group-tech
- group: company
  title: ''
  type: BlogRSS
  url: https://medium.com/feed/expedia-group-tech
- group: operate
  title: ''
  type: Support
  url: https://developers.expediagroup.com/docs/support
- group: operate
  title: ''
  type: StatusPage
  url: https://status.developers.expediagroup.com/
created: '2024-06-07'
description: Expedia Group is an American travel technology company that owns and operates travel fare aggregators and travel metasearch engines, including Expedia, Hotels.com, Vrbo, Travelocity, Hotwire.com, Orbitz, Ebookers, CheapTickets, CarRentals.com, and Trivago. Their developer platform provides APIs for travel inventory, lodging, and analytics.
features:
- 'Expedia Group: API access via partner / B2B contracts only'
- No public API pricing published — contact enterprise sales
- Expedia Group Rapid API (formerly EAN) and Partner Central require commercial agreements.
finops:
- name: Expedia Group Finops
  service_category: Travel / Hospitality
  slug: expedia-group-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/expedia-group.png
layout: provider
modified: '2026-05-19'
name: Expedia Group
nav: Providers
network: true
overview: 'Expedia Group publishes 15 APIs on the [APIs.io](https://apis.io/) network, including Bookings API, Content API, Deposit API, and 12 more. Tagged areas include Flights, Hotels, Lodging, Travel, and Fortune 500.


  Expedia Group''s developer surface includes authentication, developer portal, engineering blog, support, and 8 more developer resources.'
plans:
- name: Expedia Group Plans Pricing
  plan_count: 1
  slug: expedia-group-plans-pricing
random_paper: 42
rate_limits:
- limit_count: 1
  name: Expedia Group Rate Limits
  slug: expedia-group-rate-limits
scopes:
- name: Expedia Group Scopes
  scope_count: 3
  slug: expedia-group-scopes
  summary_line: 3 scopes · clientCredentials
score:
  band: thin
  composite: 39.2
  delta: -1.1
  facets:
    commercial_clarity: 28.9
    contract_quality: 56.7
    developer_ergonomics: 32.6
    discoverability: 72.2
    governance: 0.0
    operational_transparency: 42.1
  previous_composite: 40.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 15
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/expedia-group/refs/heads/main/screenshots/expedia-group-2026-06-20T180935.png
security:
- kind: authentication
  name: Expedia Group Authentication
  slug: expedia-group-authentication
  summary_line: apiKey/http/oauth2 · 3 schemes
- kind: domain-security
  name: Expedia Group Domain Security
  slug: expedia-group-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: expedia-group
tags:
- Flights
- Hotels
- Lodging
- Travel
- Fortune 500
website: https://developers.expediagroup.com/docs/
---
