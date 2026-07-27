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
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Cvent Hospitality Cloud Agentic Access
  operation_count: 10
  slug: cvent-hospitality-cloud-agentic-access
  summary_line: 10 operations · 5 acting
api_count: 8
apis:
- description: Passkey RegLink APIs are RESTful JSON APIs (with legacy URL-based and SOAP options) that connect Cvent registration with Passkey hotel reservations. Primary functions include sending registrant inform
  name: Cvent Passkey RegLink API
  slug: passkey-reglink
- description: The unified Cvent Platform REST API also covers hospitality use cases including event-driven integrations, contact and attendee data exchange, and webhook-based notifications that can be wired into ho
  name: Cvent Platform REST API (Hospitality)
  slug: rest-api
- description: The Authentication API from Cvent Hospitality Cloud — 1 operation(s) for authentication.
  name: Cvent Hospitality Cloud Authentication API
  slug: cvent-hospitality-cloud-authentication-api
- description: The Connections API from Cvent Hospitality Cloud — 1 operation(s) for connections.
  name: Cvent Hospitality Cloud Connections API
  slug: cvent-hospitality-cloud-connections-api
- description: The Events API from Cvent Hospitality Cloud — 2 operation(s) for events.
  name: Cvent Hospitality Cloud Events API
  slug: cvent-hospitality-cloud-events-api
- description: The Hotels API from Cvent Hospitality Cloud — 1 operation(s) for hotels.
  name: Cvent Hospitality Cloud Hotels API
  slug: cvent-hospitality-cloud-hotels-api
- description: The ReservationRequests API from Cvent Hospitality Cloud — 2 operation(s) for reservationrequests.
  name: Cvent Hospitality Cloud ReservationRequests API
  slug: cvent-hospitality-cloud-reservationrequests-api
- description: The RoomTypes API from Cvent Hospitality Cloud — 1 operation(s) for roomtypes.
  name: Cvent Hospitality Cloud RoomTypes API
  slug: cvent-hospitality-cloud-roomtypes-api
artifact_total: 17
collections:
- collection_type: open
  name: Cvent Passkey RegLink REST API
  slug: open-cvent-hospitality-cloud
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cvent-hospitality-cloud-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/cvent-hospitality-cloud-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cvent-hospitality-cloud-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cvent-hospitality-cloud-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/cvent-hospitality-cloud-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cvent
- group: company
  title: ''
  type: Website
  url: https://www.cvent.com/en/hospitality-cloud
- group: other
  title: ''
  type: SupplierNetwork
  url: https://www.cvent.com/en/hospitality-cloud/event-management/cvent-supplier-network
- group: other
  title: ''
  type: Passkey
  url: https://www.cvent.com/en/hospitality-cloud/passkey
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.cvent.com/
- group: operate
  title: ''
  type: Support
  url: https://support.cvent.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cvent.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cvent.com/en/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cvent.com/en/privacy-policy
- group: agent
  title: ''
  type: LlmsText
  url: https://www.cvent.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://www.cvent.com/en/blog/feed.xml
created: '2024-01-01'
description: Cvent Hospitality Cloud is the hotel and venue product line of the Cvent Platform. It includes the Cvent Supplier Network (the marketplace connecting event planners with hotels and venues for RFPs and bookings), Passkey (hotel room block and housing management), Venue Sourcing (venue search and discovery), and Sales & Catering (booking management, catering, and contracts). Programmatic access is delivered primarily through the Passkey RegLink REST APIs (with legacy SOAP and URL-based options) and the unified Cvent Platform REST API. Authentication uses OAuth 2.0 client credentials with the token endpoint at api-platform.cvent.com/ea/oauth2/token.
finops:
- name: Cvent Hospitality Cloud Finops
  service_category: API
  slug: cvent-hospitality-cloud-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cvent-hospitality-cloud.png
layout: provider
modified: '2026-04-28'
name: Cvent Hospitality Cloud
nav: Providers
network: true
overview: 'Cvent Hospitality Cloud publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Connections API, Events API, and 3 more. Tagged areas include Catering, Group Bookings, Hospitality, Hospitality Cloud, and Hotels.


  Cvent Hospitality Cloud''s developer surface includes authentication, support, engineering blog, and 13 more developer resources.'
plans:
- name: Cvent Hospitality Cloud Plans Pricing
  plan_count: 3
  slug: cvent-hospitality-cloud-plans-pricing
random_paper: 67
rate_limits:
- limit_count: 5
  name: Cvent Hospitality Cloud Rate Limits
  slug: cvent-hospitality-cloud-rate-limits
scopes:
- name: Cvent Hospitality Cloud Scopes
  scope_count: 2
  slug: cvent-hospitality-cloud-scopes
  summary_line: 2 scopes · clientCredentials
score:
  band: developing
  composite: 48.1
  delta: 3.3
  facets:
    commercial_clarity: 68.4
    contract_quality: 49.3
    developer_ergonomics: 26.1
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 52.6
  previous_composite: 44.8
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cvent-hospitality-cloud/refs/heads/main/screenshots/cvent-hospitality-cloud-2026-06-20T175403.png
security:
- kind: authentication
  name: Cvent Hospitality Cloud Authentication
  slug: cvent-hospitality-cloud-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Cvent Hospitality Cloud Domain Security
  slug: cvent-hospitality-cloud-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Cvent Hospitality Cloud Trust Center
  slug: cvent-hospitality-cloud-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, PCI DSS, HIPAA, FedRAMP, GDPR
slug: cvent-hospitality-cloud
tags:
- Catering
- Group Bookings
- Hospitality
- Hospitality Cloud
- Hotels
- Housing
- OAuth 2.0
- Passkey
- Reservations
- RFP
- Room Blocks
- Sales
- Sourcing
- Supplier Network
- Venues
website: https://www.cvent.com/en/hospitality-cloud
---
