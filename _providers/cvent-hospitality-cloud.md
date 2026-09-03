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
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.7
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Cvent Hospitality Cloud Agentic Access
  operation_count: 10
  slug: cvent-hospitality-cloud-agentic-access
  summary_line: 10 operations · 5 acting
api_count: 1
apis:
- description: Passkey RegLink APIs are RESTful JSON APIs (with legacy URL-based and SOAP options) that connect Cvent registration with Passkey hotel reservations. Primary functions include sending registrant inform
  name: Cvent Passkey RegLink API
  slug: passkey-reglink
- description: The unified Cvent Platform REST API also covers hospitality use cases including event-driven integrations, contact and attendee data exchange, and webhook-based notifications that can be wired into ho
  name: Cvent Platform REST API (Hospitality)
  slug: rest-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: The Authentication API from Cvent Hospitality Cloud — 1 operation(s) for authentication.
  name: Cvent Hospitality Cloud Authentication API
  slug: cvent-hospitality-cloud-authentication-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: The Connections API from Cvent Hospitality Cloud — 1 operation(s) for connections.
  name: Cvent Hospitality Cloud Connections API
  slug: cvent-hospitality-cloud-connections-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: The Events API from Cvent Hospitality Cloud — 2 operation(s) for events.
  name: Cvent Hospitality Cloud Events API
  slug: cvent-hospitality-cloud-events-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: The Hotels API from Cvent Hospitality Cloud — 1 operation(s) for hotels.
  name: Cvent Hospitality Cloud Hotels API
  slug: cvent-hospitality-cloud-hotels-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: The ReservationRequests API from Cvent Hospitality Cloud — 2 operation(s) for reservationrequests.
  name: Cvent Hospitality Cloud ReservationRequests API
  slug: cvent-hospitality-cloud-reservationrequests-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: The RoomTypes API from Cvent Hospitality Cloud — 1 operation(s) for roomtypes.
  name: Cvent Hospitality Cloud RoomTypes API
  slug: cvent-hospitality-cloud-roomtypes-api
artifact_total: 24
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Cvent Passkey RegLink REST Authentication API
  slug: open-cvent-hospitality-cloud-authentication-api
- collection_type: open
  name: Cvent Passkey RegLink REST Authentication Connections API
  slug: open-cvent-hospitality-cloud-connections-api
- collection_type: open
  name: Cvent Passkey RegLink REST Authentication Events API
  slug: open-cvent-hospitality-cloud-events-api
- collection_type: open
  name: Cvent Passkey RegLink REST Authentication Hotels API
  slug: open-cvent-hospitality-cloud-hotels-api
- collection_type: open
  name: Cvent Passkey RegLink REST Authentication ReservationRequests API
  slug: open-cvent-hospitality-cloud-reservationrequests-api
- collection_type: open
  name: Cvent Passkey RegLink REST Authentication RoomTypes API
  slug: open-cvent-hospitality-cloud-roomtypes-api
- collection_type: open
  name: Cvent Passkey RegLink REST API
  slug: open-cvent-hospitality-cloud
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/cvent-hospitality-cloud-capability-edges.yml
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


  Cvent Hospitality Cloud''s developer surface includes authentication, support, engineering blog, and 14 more developer resources.'
plans:
- name: Cvent Hospitality Cloud Plans Pricing
  plan_count: 3
  slug: cvent-hospitality-cloud-plans-pricing
random_paper: 6
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
  composite: 40.8
  coverage:
    artifact_dirs: 13
    catalog_gap: 69.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 51.7
    developer_ergonomics: 50.0
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 40.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.18.0
  scored_at: '2026-09-02'
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
- Authentication
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
