---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: documented
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 45.9
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 58
  human_in_the_loop: 0
  name: Viator Agentic Access
  operation_count: 96
  slug: viator-agentic-access
  summary_line: 96 operations · 58 acting
api_count: 4
apis:
- baseURL: https://api.viator.com/partner
  baseurl_source: declared
  description: Attraction services
  name: Viator Attraction services API
  slug: viator-attraction-services-api
- baseURL: https://api.viator.com/partner
  baseurl_source: declared
  description: The Attractions API from Viator — 2 operation(s) for attractions.
  name: Viator Attractions API
  slug: viator-attractions-api
- baseURL: https://api.viator.com/partner
  baseurl_source: declared
  description: The Auxiliary API from Viator — 6 operation(s) for auxiliary.
  name: Viator Auxiliary API
  slug: viator-auxiliary-api
- baseURL: https://api.viator.com/partner
  baseurl_source: declared
  description: The Availability API from Viator — 4 operation(s) for availability.
  name: Viator Availability API
  slug: viator-availability-api
- baseURL: https://api.viator.com/partner
  baseurl_source: declared
  description: Booking services
  name: Viator Booking services API
  slug: viator-booking-services-api
- baseURL: https://api.viator.com/partner
  baseurl_source: declared
  description: The Bookings API from Viator — 13 operation(s) for bookings.
  name: Viator Bookings API
  slug: viator-bookings-api
- baseURL: https://api.viator.com/partner
  baseurl_source: declared
  description: This section lists endpoints that are no longer recommended for new or updated integrations. These endpoints remain available for existing connections only, will stop receiving new features or behavio
  name: Viator Deprecated API
  slug: viator-deprecated-api
- baseURL: https://api.viator.com/partner
  baseurl_source: declared
  description: Deprecated services
  name: Viator Deprecated services API
  slug: viator-deprecated-services-api
- baseURL: https://api.viator.com/partner
  baseurl_source: declared
  description: General services
  name: Viator General services API
  slug: viator-general-services-api
- baseURL: https://api.viator.com/partner
  baseurl_source: declared
  description: The Payments API from Viator — 1 operation(s) for payments.
  name: Viator Payments API
  slug: viator-payments-api
- baseURL: https://api.viator.com/partner
  baseurl_source: declared
  description: Product services
  name: Viator Product services API
  slug: viator-product-services-api
- baseURL: https://api.viator.com/partner
  baseurl_source: declared
  description: The Products API from Viator — 7 operation(s) for products.
  name: Viator Products API
  slug: viator-products-api
- baseURL: https://api.viator.com/partner
  baseurl_source: declared
  description: 'This section describes all the possible services, some of which are mandatory, that reservation systems can develop to integrate with Viator. All API requests made by Viator to the reservation system '
  name: Viator Reservation system APIs API
  slug: viator-reservation-system-apis-api
- baseURL: https://api.viator.com/partner
  baseurl_source: declared
  description: Support services
  name: Viator Support services API
  slug: viator-support-services-api
- baseURL: https://api.viator.com/partner
  baseurl_source: declared
  description: Taxonomy services
  name: Viator Taxonomy services API
  slug: viator-taxonomy-services-api
- baseURL: https://api.viator.com/partner
  baseurl_source: declared
  description: Utility services
  name: Viator Utility services API
  slug: viator-utility-services-api
- baseURL: https://api.viator.com/partner
  baseurl_source: declared
  description: 'This section describes the Viator built API(s) available for reservation system consumption. **Note**: For these APIs, the request is sent **to** Viator and the response is received **from** Viator.'
  name: Viator Viator APIs API
  slug: viator-viator-apis-api
artifact_total: 26
asyncapis:
- description: ''
  name: Viator Events
  slug: viator-events
collections:
- collection_type: open
  name: Viator API Documentation & Specification - Affiliate Partners
  slug: open-viator-affiliate-api-v1
- collection_type: open
  name: Viator API Documentation & Specification – Merchant Partners
  slug: open-viator-merchant-api-v1
- collection_type: open
  name: Viator Partner API
  slug: open-viator-partner-api-v2
- collection_type: open
  name: Viator Reservation System API
  slug: open-viator-reservation-system-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/viator-capability-edges.yml
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
  type: X-MCPServerCandidate
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
modified: '2026-07-28'
name: Viator
nav: Providers
network: true
overview: 'Viator publishes 17 APIs on the [APIs.io](https://apis.io/) network, including Attraction services API, Attractions API, Auxiliary API, and 14 more. Tagged areas include Travel, United States, Tours and Activities, Experience, and OTA.


  The Viator catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Viator''s developer surface includes authentication, documentation, developer portal, support, engineering blog, API reference, getting-started guide, and 36 more developer resources.'
random_paper: 10
rate_limits:
- limit_count: 0
  name: Viator Rate Limits
  slug: viator-rate-limits
score:
  band: developing
  composite: 47.6
  coverage:
    artifact_dirs: 24
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.7
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 4.5
    contract_quality: 62.3
    developer_ergonomics: 62.5
    discoverability: 59.3
    governance: 4.5
    operational_transparency: 31.6
  previous_composite: 48.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 82.4
      derived: 0
      marker_coverage: 0.0
      total: 17
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/viator/refs/heads/main/screenshots/viator-2026-08-17T082742.png
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
- Experience
- OTA
- Booking
- Distribution
- Marketplace
- Affiliates
- Hospitality
website: https://www.viator.com/
---
