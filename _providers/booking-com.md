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
  band_gated_from: agent-native
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
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 46.1
  scored_at: '2026-09-17'
agentic_access:
- acting_count: 164
  human_in_the_loop: 0
  name: Booking Com Agentic Access
  operation_count: 210
  slug: booking-com-agentic-access
  summary_line: 210 operations · 164 acting
api_count: 15
apis:
- baseURL: https://demandapi.booking.com/3.2
  baseurl_source: declared
  description: 'The Demand API is Booking.com''s RESTful JSON API for affiliate partners: search and book accommodations, car rentals, attractions and transfers, preview and create orders, manage cancellations and mod'
  name: Booking.com Demand API
  slug: booking-com-demand-api
- baseURL: https://metasearch-connect-api.booking.com
  baseurl_source: declared
  description: The metasearch Connect API streams Booking.com property inventory and conversion reporting to metasearch partners, and carries a Demand API v2 compatible surface for hotels, availability, reviews, rev
  name: Booking.com Connect API
  slug: booking-com-connect-api
- baseURL: https://partnerships-status.booking.com
  baseurl_source: declared
  description: The Status API reports the current operational status of monitored Demand API endpoints, grouped by endpoint group, so partners can detect degradation and drive automated responses such as adjusting r
  name: Booking.com Status API
  slug: booking-com-status-api
- baseURL: https://supply-xml.booking.com
  baseurl_source: declared
  description: Create and update charges that apply at the property and room level for Connectivity partners, and set up different charge configurations for different date ranges.
  name: Booking.com Charges API
  slug: booking-com-charges-api
- baseURL: https://supply-xml.booking.com
  baseurl_source: declared
  description: The Connectivity Contacts endpoint manages the contact records attached to a property on Booking.com, letting connectivity providers read and maintain property contact details programmatically instead
  name: Booking.com Contacts API
  slug: booking-com-contacts-api
- baseURL: https://supply-xml.booking.com/contracts-api
  baseurl_source: declared
  description: Use the Contracting API to invite a new partner to Booking.com, check whether a partner has signed the contract, resend the invitation mail and retrieve the legal entity of the partner. Requests carry
  name: Booking.com Contracting API
  slug: booking-com-contracting-api
- baseURL: https://supply-xml.booking.com
  baseurl_source: declared
  description: Manage facilities at both property and room level on Booking.com, covering single-instance facilities that toggle on or off, single-instance facilities carrying optional parameters, and multi-instance
  name: Booking.com Facilities API
  slug: booking-com-facilities-api
- baseURL: https://supply-xml.booking.com
  baseurl_source: declared
  description: 'Retrieve a property''s historical reservation details to initialise or reconcile reservation data for revenue management. Room reservations are selected by creation timestamp and optionally by status, '
  name: Booking.com Historical Reservations API
  slug: booking-com-historical-reservations-api
- baseURL: https://payments-api.booking.com
  baseurl_source: declared
  description: Retrieve payment and payout details for accommodation reservations, including partner payout information, payout breakdowns, bank transfer details, virtual credit card payout details, VCCs to be charg
  name: Booking.com Payments API
  slug: booking-com-payments-api
- baseURL: https://payments-api.booking.com
  baseurl_source: declared
  description: Manage Payments by Booking onboarding configurations, check property eligibility for the different payout options, and monitor the processing status of configuration update requests. Accepted change r
  name: Booking.com Payments by Booking Onboarding API
  slug: booking-com-payments-by-booking-onboarding-api
- baseURL: https://supply-xml.booking.com/property-api
  baseurl_source: declared
  description: Use the Property API to create or update a property and its settings, check and update property status, and create or update the property description, replacing extranet work for connectivity provider
  name: Booking.com Property API
  slug: booking-com-property-api
- baseURL: https://supply-xml.booking.com/property-health-api
  baseurl_source: declared
  description: A read-only JSON API for connectivity providers that returns property health and status data, explaining why properties are unbookable or at risk so providers can prioritise action across the properti
  name: Booking.com Property Health API
  slug: booking-com-property-health-api
- baseURL: https://payments-api.booking.com
  baseurl_source: declared
  description: 'Generate and download financial reconciliation reports for properties: request payout reports for a date range and set of properties, poll report generation status, and retrieve the available filter a'
  name: Booking.com Reconciliation API
  slug: booking-com-reconciliation-api
- baseURL: https://supply-xml.booking.com
  baseurl_source: declared
  description: Create and manage room types on Booking.com, including the bulk surface and the generated-names variant. Room definitions carry occupancy, extra beds configuration and rate-relevant attributes; the le
  name: Booking.com Rooms API
  slug: booking-com-rooms-api
- baseURL: https://supply-xml.booking.com
  baseurl_source: declared
  description: Returns the catalogue of value adds available for properties on Booking.com. Responses are JSON or XML depending on the Accept header, and each value add carries dynamic attributes such as currency an
  name: Booking.com Value Adds Catalog API
  slug: booking-com-valueadds-api
artifact_total: 65
asyncapis:
- description: ''
  name: Booking Com Webhooks
  slug: booking-com-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Booking.com Car Rentals Accommodations API
  slug: open-booking-com-accommodations-api
- collection_type: open
  name: Booking.com Car Rentals Accommodations Availability API
  slug: open-booking-com-availability-api
- collection_type: open
  name: Booking.com Car Rentals API
  slug: open-booking-com-car-rentals-api
- collection_type: open
  name: Booking.com Car Rentals Accommodations Cars API
  slug: open-booking-com-cars-api
- collection_type: open
  name: Booking.com Connectivity Content API
  slug: open-booking-com-connectivity-content-api
- collection_type: open
  name: Booking.com Connectivity Promotions API
  slug: open-booking-com-connectivity-promotions-api
- collection_type: open
  name: Booking.com Connectivity Rates and Availability API
  slug: open-booking-com-connectivity-rates-availability-api
- collection_type: open
  name: Booking.com Connectivity Reservations API
  slug: open-booking-com-connectivity-reservations-api
- collection_type: open
  name: Booking.com Car Rentals Accommodations Constants API
  slug: open-booking-com-constants-api
- collection_type: open
  name: Booking.com Car Rentals Accommodations Conversations API
  slug: open-booking-com-conversations-api
- collection_type: open
  name: Booking.com Demand API
  slug: open-booking-com-demand-api
- collection_type: open
  name: Booking.com Car Rentals Accommodations Depots API
  slug: open-booking-com-depots-api
- collection_type: open
  name: Booking.com Car Rentals Accommodations Derived Pricing API
  slug: open-booking-com-derived-pricing-api
- collection_type: open
  name: Booking.com Car Rentals Accommodations Facilities API
  slug: open-booking-com-facilities-api
- collection_type: open
  name: Booking.com Car Rentals Accommodations Inventory API
  slug: open-booking-com-inventory-api
- collection_type: open
  name: Booking.com Car Rentals Accommodations Locations API
  slug: open-booking-com-locations-api
- collection_type: open
  name: Booking.com Car Rentals Accommodations Messages API
  slug: open-booking-com-messages-api
- collection_type: open
  name: Booking.com Car Rentals Accommodations Orders API
  slug: open-booking-com-orders-api
- collection_type: open
  name: Booking.com Car Rentals Accommodations OTA Availability API
  slug: open-booking-com-ota-availability-api
- collection_type: open
  name: Booking.com Car Rentals Accommodations OTA Legacy API
  slug: open-booking-com-ota-legacy-api
- collection_type: open
  name: Booking.com Car Rentals Accommodations OTA Reservations API
  slug: open-booking-com-ota-reservations-api
- collection_type: open
  name: Booking.com Car Rentals Accommodations Payments API
  slug: open-booking-com-payments-api
- collection_type: open
  name: Booking.com Car Rentals Accommodations Photos API
  slug: open-booking-com-photos-api
- collection_type: open
  name: Booking.com Car Rentals Accommodations Promotions API
  slug: open-booking-com-promotions-api
- collection_type: open
  name: Booking.com Car Rentals Accommodations Property Management API
  slug: open-booking-com-property-management-api
- collection_type: open
  name: Booking.com Car Rentals Accommodations Rates API
  slug: open-booking-com-rates-api
- collection_type: open
  name: Booking.com Car Rentals Accommodations Recovery API
  slug: open-booking-com-recovery-api
- collection_type: open
  name: Booking.com Car Rentals Accommodations Reservations API
  slug: open-booking-com-reservations-api
- collection_type: open
  name: Booking.com Car Rentals Accommodations Rooms API
  slug: open-booking-com-rooms-api
- collection_type: open
  name: Booking.com Car Rentals Accommodations Suppliers API
  slug: open-booking-com-suppliers-api
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/booking-com/refs/heads/main/security/booking-com-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/booking-com-trust-center.yml
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
  href: https://raw.githubusercontent.com/api-evangelist/booking-com/refs/heads/main/agentic-access/booking-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/booking-com-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/booking-com/refs/heads/main/security/booking-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/booking-com-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/booking-com/refs/heads/main/security/booking-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/booking-com-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/booking-com/refs/heads/main/authentication/booking-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/booking-com-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bookingcom
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/booking-com/refs/heads/main/json-ld/booking-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/booking-com-context.jsonld
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/booking-com/refs/heads/main/json-schema/booking-com-accommodation-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/booking-com-accommodation-schema.json
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/booking-com/refs/heads/main/json-schema/booking-com-order-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/booking-com-order-schema.json
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/booking-com/refs/heads/main/json-schema/booking-com-promotion-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/booking-com-promotion-schema.json
- group: agent
  title: ''
  type: LlmsText
  url: https://developers.booking.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://news.booking.com/feed/
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/booking-com/refs/heads/main/well-known/booking-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/booking-com-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/booking-com/refs/heads/main/well-known/booking-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/booking-com-security.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/booking-com/refs/heads/main/a2a/booking-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/booking-com-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/booking-com/refs/heads/main/mcp/booking-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/booking-com-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/booking-com/refs/heads/main/mcp/booking-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/booking-com-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/booking-com/refs/heads/main/llms/booking-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/booking-com-llms.txt
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/booking-com/refs/heads/main/conventions/booking-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/booking-com-conventions.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/booking-com/refs/heads/main/packages/booking-com-packages.yml
  title: ''
  type: Packages
  url: packages/booking-com-packages.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/booking-com/refs/heads/main/lifecycle/booking-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/booking-com-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://developers.booking.com/connectivity/docs/deprecation-policy/deprecation-and-sunsetting
- group: operate
  title: ''
  type: StatusPage
  url: https://developers.booking.com/demand/docs/additional-services/status-api/about
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/booking-com/refs/heads/main/security/booking-com-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/booking-com-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/booking-com/refs/heads/main/security/booking-com-trust-center.yml
  title: ''
  type: Compliance
  url: security/booking-com-trust-center.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/booking-com/refs/heads/main/conformance/booking-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/booking-com-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/booking-com/refs/heads/main/asyncapi/booking-com-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/booking-com-webhooks.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/booking-com/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/booking-com/refs/heads/main/sandbox/booking-com-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/booking-com-sandbox.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/booking-com/refs/heads/main/changelog/booking-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/booking-com-changelog.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/booking-com/refs/heads/main/plans/booking-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/booking-com-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/booking-com/refs/heads/main/rate-limits/booking-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/booking-com-rate-limits.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/booking-com/refs/heads/main/errors/booking-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/booking-com-problem-types.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/booking-com/refs/heads/main/errors/booking-com-decline-codes.yml
  title: ''
  type: DeclineCodes
  url: errors/booking-com-decline-codes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/booking-com/refs/heads/main/data-model/booking-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/booking-com-data-model.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/booking-com/refs/heads/main/finops/booking-com-finops.yml
  title: ''
  type: FinOps
  url: finops/booking-com-finops.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/booking-com/refs/heads/main/rules/booking-com-jsonschema-spectral-rules.yml
  title: ''
  type: Rules
  url: rules/booking-com-jsonschema-spectral-rules.yml
- group: docs
  title: ''
  type: APIReference
  url: https://developers.booking.com/demand/docs/open-api/3.2/demand-api
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.booking.com/demand/docs/getting-started/overview
- group: operate
  title: ''
  type: Support
  url: https://connectivity.booking.com/s/article/Contact-Us
- group: start
  title: ''
  type: SignUp
  url: https://www.booking.com/affiliate-program/v2/index.html
created: '2026-05-03'
description: 'Booking.com is the world''s largest online travel agency, part of Booking Holdings, listing more than 28 million accommodation options plus car rentals, flights, attractions and airport transfers in over 60,000 destinations. It runs two distinct API programmes. The Demand API serves affiliate partners who want to search, price and book Booking.com inventory inside their own product; the Connectivity platform serves the supply side - channel managers, property management systems and hotel groups keeping rooms, rates, availability, content, reservations and payouts in sync. Twenty OpenAPI descriptions covering 210 operations are published through the developer portal, and the Connectivity estate additionally speaks OpenTravel Alliance (OTA) and Booking.com''s own B.XML message formats. Both programmes are credentialed: keys come from the Affiliate Partner Centre or from a machine account in the Connectivity Portal, and no API host answers an anonymous request.'
features:
- 'Booking.com: API access via partner / B2B contracts only'
- No public API pricing published — contact enterprise sales
- Booking.com Connectivity APIs require Hotel Manager/Connectivity Partner approval; commission per booking.
finops:
- name: Booking Com Finops
  service_category: Travel / Hospitality
  slug: booking-com-finops
graphqls:
- description: This is a conceptual GraphQL schema for the Booking.com platform, covering accommodation search, availability, booking, reviews, and property management. It is derived from the public REST/XML APIs av
  name: Booking.com GraphQL Schema
  slug: booking-com-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/booking-com.png
json_schemas:
- name: Booking.com Accommodation
  property_count: 25
  slug: booking-com-accommodation
- name: Booking.com Order
  property_count: 16
  slug: booking-com-order
- name: Booking.com Promotion
  property_count: 19
  slug: booking-com-promotion
jsonld:
- class_count: 0
  name: Booking Com Context
  property_count: 10
  slug: booking-com-context
layout: provider
mcp_servers:
- description: ''
  name: Booking.com Docs MCP server
  slug: bookingcom-docs-mcp-server
modified: '2026-09-17'
name: Booking.com
nav: Providers
network: true
overview: 'Booking.com publishes 15 APIs on the [APIs.io](https://apis.io/) network, including Demand API, Connect API, Status API, and 12 more. Tagged areas include Travel, Hospitality, Accommodation, Booking, and Car Rental.


  The Booking.com catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Booking.com''s developer surface includes documentation, authentication, engineering blog, sandbox, changelog, API reference, getting-started guide, and 42 more developer resources.'
plans:
- name: Booking Com Plans Pricing
  plan_count: 0
  slug: booking-com-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 3
  name: Booking Com Rate Limits
  slug: booking-com-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: Booking.com API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: booking-com-jsonschema-spectral-rules
score:
  band: exemplar
  composite: 70.8
  coverage:
    artifact_dirs: 30
    catalog_earned: 66.3
    catalog_earned_first_party: 12.0
    catalog_gap: 48.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 31.0
  facets:
    access_clarity: 57.9
    contract_governance: 14.4
    contract_quality: 70.5
    developer_ergonomics: 66.1
    discoverability: 81.5
    operational_transparency: 92.1
  previous_composite: 39.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 50
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 65.6
  schema_version: 0.22.0
  scored_at: '2026-09-17'
  trend: rising
  upsert:
    applies: true
    score: 22.2
screenshot: https://raw.githubusercontent.com/api-evangelist/booking-com/refs/heads/main/screenshots/booking-com-2026-06-20T173602.png
security:
- kind: authentication
  name: Booking Com Authentication
  slug: booking-com-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Booking Com Domain Security
  slug: booking-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Booking Com Vulnerability Disclosure
  slug: booking-com-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Booking Com Trust Center
  slug: booking-com-trust-center
  summary_line: PCI DSS, GDPR
slug: booking-com
tags:
- Travel
- Hospitality
- Accommodation
- Booking
- Car Rental
- Payments
- Connectivity
- Marketplace
- OTA
- Attractions
website: https://www.booking.com
---
