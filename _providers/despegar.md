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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: true
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 53.4
  scored_at: '2026-07-28'
api_count: 20
apis:
- description: The Availability API from Despegar — 2 operation(s) for availability.
  name: Despegar Availability API
  slug: despegar-availability-api
- description: The Booking API from Despegar — 1 operation(s) for booking.
  name: Despegar Booking API
  slug: despegar-booking-api
- description: Validation, quotation, and confirmation of cancellations.
  name: Despegar Cancellations API
  slug: despegar-cancellations-api
- description: Date/itinerary changes and checkout processes.
  name: Despegar Changes API
  slug: despegar-changes-api
- description: The Commission Update API from Despegar — 1 operation(s) for commission update.
  name: Despegar Commission Update API
  slug: despegar-commission-update-api
- description: The Discovery API from Despegar — 1 operation(s) for discovery.
  name: Despegar Discovery API
  slug: despegar-discovery-api
- description: The Flights API from Despegar — 2 operation(s) for flights.
  name: Despegar Flights API
  slug: despegar-flights-api
- description: The Geography API from Despegar — 12 operation(s) for geography.
  name: Despegar Geography API
  slug: despegar-geography-api
- description: The hotel API from Despegar — 1 operation(s) for hotel.
  name: Despegar hotel API
  slug: despegar-hotel-api
- description: The Hotel content API from Despegar — 3 operation(s) for hotel content.
  name: Despegar Hotel content API
  slug: despegar-hotel-content-api
- description: The HotelAvailability API from Despegar — 1 operation(s) for hotelavailability.
  name: Despegar HotelAvailability API
  slug: despegar-hotelavailability-api
- description: The Hotels inventory API from Despegar — 1 operation(s) for hotels inventory.
  name: Despegar Hotels inventory API
  slug: despegar-hotels-inventory-api
- description: The Modalities API from Despegar — 1 operation(s) for modalities.
  name: Despegar Modalities API
  slug: despegar-modalities-api
- description: The Payments API from Despegar — 1 operation(s) for payments.
  name: Despegar Payments API
  slug: despegar-payments-api
- description: The Pre-booking API from Despegar — 1 operation(s) for pre-booking.
  name: Despegar Pre-booking API
  slug: despegar-pre-booking-api
- description: The Price Jump API from Despegar — 1 operation(s) for price jump.
  name: Despegar Price Jump API
  slug: despegar-price-jump-api
- description: Management of major reschedulings.
  name: Despegar Reschedulings API
  slug: despegar-reschedulings-api
- description: Reservation query and management.
  name: Despegar Reservations API
  slug: despegar-reservations-api
- description: Special requests associated with a reservation.
  name: Despegar Special Requests API
  slug: despegar-special-requests-api
- description: The Suggestions API from Despegar — 16 operation(s) for suggestions.
  name: Despegar Suggestions API
  slug: despegar-suggestions-api
artifact_total: 24
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api-docs.despegar.com
- group: docs
  title: ''
  type: Documentation
  url: https://api-docs.despegar.com/docs/ecosystem
- group: docs
  title: ''
  type: APIReference
  url: https://api-docs.despegar.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://api-docs.despegar.com/docs/general-information
- group: operate
  title: ''
  type: Support
  url: https://api-docs.despegar.com/docs/support
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/despegar
- group: agent
  title: ''
  type: MCPServer
  url: mcp/despegar-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/despegar-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/despegar-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/despegar-security.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/despegar-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/despegar-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/despegar-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/despegar-sandbox.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/despegar-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/despegar-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/despegar-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/despegar-packages.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/despegar-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.despegar.com/.well-known/security.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/despegar-domain-security.yml
- group: company
  title: ''
  type: Website
  url: http://www.despegar.com
created: '2026-07-17'
description: Despegar (Decolar in Brazil) is the leading online travel agency in Latin America, selling flights, hotels, activities, car rentals, insurance and vacation packages across the region. Its Despegar B2B platform exposes a partner API ecosystem so travel agencies and resellers can integrate hotel, flight and activity search, pre-booking, payment, booking and after-sales (cancellations, rescheduling, special requests) directly into their own systems, backed by geo/common-assets reference data and an event/notification channel. APIs are versioned under /v3, authenticated with a per-client API key (x-apikey header) with separate test and production keys, protected with mTLS for B2B transactions, and now also reachable through published Model Context Protocol (MCP) servers for AI agents. This profile was enriched from Despegar's public developer documentation at api-docs.despegar.com.
image: https://github.com/despegar.png
layout: provider
mcp_servers:
- description: ''
  name: despegar-mcp.yml
  slug: despegar-mcpyml
modified: '2026-07-18'
name: Despegar
nav: Providers
network: true
overview: 'Despegar publishes 20 APIs on the [APIs.io](https://apis.io/) network, including Availability API, Booking API, Cancellations API, and 17 more. Tagged areas include Company, Consumer, Travel, Hotels, and Flights.


  Despegar''s developer surface includes documentation, API reference, getting-started guide, support, authentication, sandbox, and 17 more developer resources.'
random_paper: 43
score:
  band: thin
  composite: 38.4
  delta: -0.9
  facets:
    commercial_clarity: 0.0
    contract_quality: 53.6
    developer_ergonomics: 66.8
    discoverability: 92.6
    governance: 3.1
    operational_transparency: 15.8
  previous_composite: 39.3
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 20
    mcp: first-party
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/despegar/refs/heads/main/screenshots/despegar-2026-07-25T211758.png
security:
- kind: authentication
  name: Despegar Authentication
  slug: despegar-authentication
  summary_line: apiKey/http/oauth2 · 3 schemes
- kind: domain-security
  name: Despegar Domain Security
  slug: despegar-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Despegar Vulnerability Disclosure
  slug: despegar-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: despegar
tags:
- Company
- Consumer
- Travel
- Hotels
- Flights
- Booking
- Tourism
- Latin America
- B2B
- MCP
website: http://www.despegar.com
---
