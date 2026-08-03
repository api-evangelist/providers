---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: documented
    mcp_server: derived
    openapi_examples: verified
    rate_limit_signal: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 56.5
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 58
  human_in_the_loop: 0
  name: Viator Agentic Access
  operation_count: 96
  slug: viator-agentic-access
  summary_line: 96 operations · 58 acting
api_count: 9
apis:
- description: 'Product content and catalogue ingestion for the Viator Partner API v2 - full product detail, bulk retrieval, incremental modified-since ingestion, the product tag taxonomy, booking questions, product '
  name: Viator Partner Products API
  slug: viator-partner-products-api
- description: Real-time availability and price checking plus availability-schedule retrieval for a single product, in bulk, or incrementally by modification date, so partners can hold a local mirror of bookable cap
  name: Viator Partner Availability API
  slug: viator-partner-availability-api
- description: Transactional booking surface - cart and single-item hold and book, booking status, cancel reasons, cancellation quote and cancellation, amendment check, quote and amend, and the modified-since bookin
  name: Viator Partner Bookings API
  slug: viator-partner-bookings-api
- description: Checkout-session payment account endpoint used by Full Access plus Booking affiliate partners to pass traveller payment details to Viator in a PCI-compliant way when Viator remains the merchant of rec
  name: Viator Partner Payments API
  slug: viator-partner-payments-api
- description: Attraction search and attraction detail endpoints, letting partners build attraction landing pages and tie Viator's bookable products back to the places they visit.
  name: Viator Partner Attractions API
  slug: viator-partner-attractions-api
- description: Supporting reference and content services for the Partner API v2 - free-text search across products, destinations and attractions, bulk location resolution, exchange rates, product reviews, supplier p
  name: Viator Partner Auxiliary API
  slug: viator-partner-auxiliary-api
- description: The supplier-side connectivity contract, formerly the Viator Supplier API. This specification is inverted - it defines the endpoints a tour operator's reservation system or booking software must itsel
  name: Viator Reservation System API
  slug: viator-reservation-system-api
- description: The legacy v1 merchant-partner specification still published by Viator, exposing taxonomy, product, photo, review, availability, pricing-matrix, booking, voucher and cancellation services under viator
  name: Viator Merchant API v1
  slug: viator-merchant-api-v1
- description: The legacy v1 affiliate-partner specification, a non-transactional subset covering utility services, destination and category taxonomy, product and attraction search, product detail, reviews and photo
  name: Viator Affiliate API v1
  slug: viator-affiliate-api-v1
artifact_total: 15
asyncapis:
- description: ''
  name: Viator Events
  slug: viator-events
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/viator-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/viator-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/viator-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.viator.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.viator.com/partner-api/technical/
- group: start
  title: ''
  type: Portal
  url: https://partnerresources.viator.com/
- group: operate
  title: ''
  type: Support
  url: https://partnerhelp.viator.com/en
- group: company
  title: ''
  type: Blog
  url: https://partnerresources.viator.com/blog/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/viator
- group: build
  title: ''
  type: PostmanCollection
  url: collections/Viator-Basic-Access-Affiliate-API-v2.postman_collection.json
- group: build
  title: ''
  type: PostmanCollection
  url: collections/Viator-Affiliate-API-v2.postman_collection.json
- group: build
  title: ''
  type: PostmanCollection
  url: collections/Viator-Affiliate-Booking-API-v2.postman_collection.json
- group: build
  title: ''
  type: PostmanCollection
  url: collections/Viator-Merchant-API-v2.postman_collection.json
- group: docs
  title: ''
  type: APIReference
  url: https://docs.viator.com/partner-api/technical/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://partnerresources.viator.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://partnerresources.viator.com/travel-commerce/affiliate/basic-access/golden-path/
- group: commercial
  title: ''
  type: Pricing
  url: https://partnerresources.viator.com/travel-commerce/levels-of-access/
- group: start
  title: ''
  type: SignUp
  url: https://partners.viator.com/signup?mcid=66150&program=affiliate
- group: start
  title: ''
  type: Login
  url: https://partners.viator.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.viator.com/support/termsAndConditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.viator.com/support/privacyPolicy
- group: design
  title: ''
  type: Conventions
  url: conventions/viator-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/viator-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/viator-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/viator-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/viator-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.viator.com/partner-api/technical/#section/Localization/API-versioning-strategy
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/viator-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/viator-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/viator-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/viator-sandbox.yml
- group: build
  title: ''
  type: Packages
  url: packages/viator-packages.yml
- group: design
  title: ''
  type: Components
  url: components/viator-components.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/viator-events.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/viator-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/viator-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/viator-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/viator-partner-api-v2-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/viator-reservation-system-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/viator-merchant-api-v1-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/viator-affiliate-api-v1-overlay.yaml
created: '2026-07-28'
description: 'Viator is a Tripadvisor company and the largest online marketplace for tours, activities and travel experiences, headquartered in the United States and listing more than 300,000 bookable products across roughly 2,500 destinations. It sits on the demand side of the travel distribution chain as an aggregator and reseller of third-party operator inventory, and on the supply side as the channel counterparty that tour operators'' reservation systems connect into. Its API posture is unusually open for travel: the full Viator Partner API v2 OpenAPI, the legacy v1 affiliate and merchant specifications, the Viator Reservation System (supplier) API and four Postman collections are all published without a login at docs.viator.com, and Basic Access affiliate keys are issued self-serve at no cost on account creation. Everything beyond that is gated - Full Access, Full Access plus Booking, Merchant and supplier connectivity all require qualification by Viator and, for transactional integrations,
  passing a two-part front-end and back-end certification. No open travel standard is referenced anywhere in the specifications: the contract is entirely Viator-proprietary, product identifiers are Viator-internal, and partners are contractually required to prevent search engines indexing Viator reviews and unique content.'
image: https://partnerresources.viator.com/wp-content/uploads/2023/08/V-logo_Green.png
layout: provider
mcp_servers:
- description: ''
  name: viator-mcp.yml
  slug: viator-mcpyml
modified: '2026-07-28'
name: Viator
nav: Providers
network: true
overview: 'Viator publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Partner Products API, Partner Availability API, Partner Bookings API, and 6 more. Tagged areas include Travel, United States, Tours and Activities, Experiences, and OTA.


  The Viator catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Viator''s developer surface includes authentication, documentation, developer portal, support, engineering blog, API reference, getting-started guide, and 35 more developer resources.'
random_paper: 91
rate_limits:
- limit_count: 0
  name: Viator Rate Limits
  slug: viator-rate-limits
score:
  band: developing
  composite: 53.1
  delta: 0.0
  facets:
    commercial_clarity: 44.7
    contract_quality: 67.9
    developer_ergonomics: 66.8
    discoverability: 83.3
    governance: 11.5
    operational_transparency: 31.6
  previous_composite: 53.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
    skills: derived
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
security:
- kind: authentication
  name: Viator Authentication
  slug: viator-authentication
  summary_line: apiKey · 3 schemes
- kind: domain-security
  name: Viator Domain Security
  slug: viator-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: viator
tags:
- Travel
- United States
- Tours and Activities
- Experiences
- OTA
- Booking
- Distribution
- Marketplace
- Affiliate
- Hospitality
website: https://www.viator.com/
---
