---
access_model:
  confidence: low
  gated: partner
  gated_source:
  - x-api-posture
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
    mcp_tool_quality: full
    openapi_examples: verified
    operation_distinctiveness: false
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 45.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 137
  human_in_the_loop: 0
  name: Booking Com Agentic Access
  operation_count: 210
  slug: booking-com-agentic-access
  summary_line: 210 operations · 137 acting
api_count: 17
apis:
- baseURL: https://partnerships-status.booking.com
  baseurl_source: declared
  description: The Status API reports the current operational status of monitored Demand API endpoints, grouped by endpoint group, so partners can detect degradation and drive automated responses such as adjusting r
  name: Booking.com Status API
  slug: booking-com-status-api
- baseURL: https://supply-xml.booking.com
  baseurl_source: declared
  description: The Connectivity Contacts endpoint manages the contact records attached to a property on Booking.com, letting connectivity providers read and maintain property contact details programmatically instead
  name: Booking.com Contacts API
  slug: booking-com-contacts-api
- baseURL: https://supply-xml.booking.com
  baseurl_source: declared
  description: 'Retrieve a property''s historical reservation details to initialise or reconcile reservation data for revenue management. Room reservations are selected by creation timestamp and optionally by status, '
  name: Booking.com Historical Reservations API
  slug: booking-com-historical-reservations-api
- baseURL: https://supply-xml.booking.com/property-health-api
  baseurl_source: declared
  description: A read-only JSON API for connectivity providers that returns property health and status data, explaining why properties are unbookable or at risk so providers can prioritise action across the properti
  name: Booking.com Property Health API
  slug: booking-com-property-health-api
- baseURL: https://demandapi.booking.com/3.2
  baseurl_source: declared
  description: 'This API collection is specific for the stay part of the connected trip. </br></br>Use these endpoints to search for stays such as hotels and apartments, check availability, retrieve reviews, and get '
  name: Booking.com Accommodations API
  slug: booking-com-accommodations-api
- baseURL: https://demandapi.booking.com/3.2
  baseurl_source: declared
  description: Provides endpoints for handling message attachments. </br></br>Use these endpoints to upload and download images shared within conversations.
  name: Booking.com Attachments API
  slug: booking-com-attachments-api
- baseURL: https://demandapi.booking.com/3.2
  baseurl_source: declared
  description: The Attractions API from Booking.com — 5 operation(s) for attractions.
  name: Booking.com Attractions API
  slug: booking-com-attractions-api
- baseURL: https://demandapi.booking.com/3.2
  baseurl_source: declared
  description: Retrieve Bank Transfer payout details for accommodation reservations.
  name: Booking.com Bank transfer payout API
  slug: booking-com-bank-transfer-payout-api
- baseURL: https://demandapi.booking.com/3.2
  baseurl_source: declared
  description: This API collection is specific to the car rentals part of the connected trip.</br></br> Use these endpoints to search for car rentals, check car details and look for depots and suppliers.
  name: Booking.com Cars API
  slug: booking-com-cars-api
- baseURL: https://demandapi.booking.com/3.2
  baseurl_source: declared
  description: Lists the details of the Charges endpoints to set and retrieve taxes and fees at the property and room level.
  name: Booking.com Charges endpoint API
  slug: booking-com-charges-endpoint-api
- baseURL: https://demandapi.booking.com/3.2
  baseurl_source: declared
  description: Lists the details of the Charges meta endpoint to retrieve a full list of charge types supported by the Charges API.
  name: Booking.com Charges meta endpoint API
  slug: booking-com-charges-meta-endpoint-api
- baseURL: https://demandapi.booking.com/3.2
  baseurl_source: declared
  description: Check legal details of Partner using email or entity ID.
  name: Booking.com Check legal details API
  slug: booking-com-check-legal-details-api
- baseURL: https://demandapi.booking.com/3.2
  baseurl_source: declared
  description: Use this endpoint to retrieve ranked suggestions based on a free-text query. Designed for real-time "as-you-type" autocomplete experiences.
  name: Booking.com Common/autocomplete API
  slug: booking-com-common-autocomplete-api
- baseURL: https://demandapi.booking.com/3.2
  baseurl_source: declared
  description: Provides a list of supported language codes for use in API requests.
  name: Booking.com Common/languages API
  slug: booking-com-common-languages-api
- baseURL: https://demandapi.booking.com/3.2
  baseurl_source: declared
  description: 'Provides identifiers for a wide range of geographical locations, including airports, countries, cities, and regions. </br></br>Use these identifiers to construct your requests. </br></br>Note: These i'
  name: Booking.com Common/locations API
  slug: booking-com-common-locations-api
- baseURL: https://demandapi.booking.com/3.2
  baseurl_source: declared
  description: Provides generic payment-related endpoints, including supported currencies and payment types.
  name: Booking.com Common/payments API
  slug: booking-com-common-payments-api
- baseURL: https://demandapi.booking.com/3.2
  baseurl_source: declared
  description: Provides endpoints to retrieve and manage messaging conversations. </br></br>Use these endpoints to list conversations, fetch conversation details, and track updates.
  name: Booking.com Conversations API
  slug: booking-com-conversations-api
- baseURL: https://demandapi.booking.com/3.2
  baseurl_source: declared
  description: The demand-api-v2-compatible API from Booking.com — 8 operation(s) for demand-api-v2-compatible.
  name: Booking.com Demand API V2 Compatible API
  slug: booking-com-demand-api-v2-compatible-api
- baseURL: https://demandapi.booking.com/3.2
  baseurl_source: declared
  description: The Inventory API from Booking.com — 1 operation(s) for inventory.
  name: Booking.com Inventory API
  slug: booking-com-inventory-api
- baseURL: https://demandapi.booking.com/3.2
  baseurl_source: declared
  description: 'Use the GET and the PUT endpoints to: <ul><li>Retrieve room bathroom configuration</li> <li>Add, modify or delete room-level bathroom information</li></ul>'
  name: Booking.com Manage bathrooms API
  slug: booking-com-manage-bathrooms-api
- baseURL: https://demandapi.booking.com/3.2
  baseurl_source: declared
  description: Create, update or resend contract details.
  name: Booking.com Manage contracts API
  slug: booking-com-manage-contracts-api
- baseURL: https://demandapi.booking.com/3.2
  baseurl_source: declared
  description: 'Use the GET and the PUT endpoints to: <ul><li>Retrieve property-level facilities details</li> <li>Add, modify or delete property-level facilities details<ul><li>Add single-instance facilities</li> <li'
  name: Booking.com Manage property facilities API
  slug: booking-com-manage-property-facilities-api
- baseURL: https://demandapi.booking.com/3.2
  baseurl_source: declared
  description: 'Use the GET and the PUT endpoints to: <ul><li>Retrieve room facilities set for a property.</li><li>Add, modify or delete room facilities.</li></ul>'
  name: Booking.com Manage room facilities API
  slug: booking-com-manage-room-facilities-api
- baseURL: https://demandapi.booking.com/3.2
  baseurl_source: declared
  description: Provides endpoints for two-way post-booking communication between guests and properties. </br></br>Use these endpoints to send and retrieve messages, exchange images, and check conversation details.
  name: Booking.com Messages API
  slug: booking-com-messages-api
- baseURL: https://demandapi.booking.com/3.2
  baseurl_source: declared
  description: Retrieve units meta data and translations
  name: Booking.com Meta API
  slug: booking-com-meta-api
- baseURL: https://demandapi.booking.com/3.2
  baseurl_source: declared
  description: '<p>Retrieve the latest facility definitions.</p> <ul> <li>Get the list of all supported facilities<ul> <li>To get the details of a property-level facility: Look for a matching name under the facility_'
  name: Booking.com Meta data endpoint API
  slug: booking-com-meta-data-endpoint-api
- baseURL: https://demandapi.booking.com/3.2
  baseurl_source: declared
  description: Enables management of booking orders within the Demand API. </br></br>Use these endpoints to preview and create new orders, check order details, cancel or modify existing orders. This collection is re
  name: Booking.com Orders API
  slug: booking-com-orders-api
- baseURL: https://demandapi.booking.com/3.2
  baseurl_source: declared
  description: Update Payments by Booking payout configurations for properties.
  name: Booking.com Payments by Booking configurations API
  slug: booking-com-payments-by-booking-configurations-api
- baseURL: https://demandapi.booking.com/3.2
  baseurl_source: declared
  description: Check the processing status of Payments by Booking configuration update requests.
  name: Booking.com Payments by Booking configurations status API
  slug: booking-com-payments-by-booking-configurations-status-api
- baseURL: https://demandapi.booking.com/3.2
  baseurl_source: declared
  description: Retrieve payments eligibility details for partners.
  name: Booking.com Payments eligibility details for partners API
  slug: booking-com-payments-eligibility-details-for-partners-api
- baseURL: https://demandapi.booking.com/3.2
  baseurl_source: declared
  description: Create, update and retrieve property description
  name: Booking.com Property Description API
  slug: booking-com-property-description-api-api
- baseURL: https://demandapi.booking.com/3.2
  baseurl_source: declared
  description: Create, update and retrieve property details
  name: Booking.com Property Details API
  slug: booking-com-property-details-api-api
- baseURL: https://demandapi.booking.com/3.2
  baseurl_source: declared
  description: Add, update or retrieve property settings
  name: Booking.com Property Settings API
  slug: booking-com-property-settings-api-api
- baseURL: https://demandapi.booking.com/3.2
  baseurl_source: declared
  description: Check if a property is ready to open; open or close a property
  name: Booking.com Property Status API
  slug: booking-com-property-status-api-api
- baseURL: https://demandapi.booking.com/3.2
  baseurl_source: declared
  description: Generate financial reconciliation reports for one or more properties.
  name: Booking.com Reconciliation reports API
  slug: booking-com-reconciliation-reports-api
- baseURL: https://demandapi.booking.com/3.2
  baseurl_source: declared
  description: Provides information of the refundable VCCs.
  name: Booking.com Refundable VCCs API
  slug: booking-com-refundable-vccs-api
- baseURL: https://demandapi.booking.com/3.2
  baseurl_source: declared
  description: Retrieve the available filter and configuration options for reconciliation report generation.
  name: Booking.com Report filters API
  slug: booking-com-report-filters-api
- baseURL: https://demandapi.booking.com/3.2
  baseurl_source: declared
  description: Check the processing status of a reconciliation report generation request and retrieve the download URL when the report is ready.
  name: Booking.com Report status API
  slug: booking-com-report-status-api
- baseURL: https://demandapi.booking.com/3.2
  baseurl_source: declared
  description: The Reports API from Booking.com — 1 operation(s) for reports.
  name: Booking.com Reports API
  slug: booking-com-reports-api
- baseURL: https://demandapi.booking.com/3.2
  baseurl_source: declared
  description: Request access to existing partner.
  name: Booking.com Request access API
  slug: booking-com-request-access-api
- baseURL: https://demandapi.booking.com/3.2
  baseurl_source: declared
  description: Retrieve detailed breakdown for accommodation reservations with respect to partner payout.
  name: Booking.com Reservation breakdown API
  slug: booking-com-reservation-breakdown-api
- baseURL: https://demandapi.booking.com/3.2
  baseurl_source: declared
  description: Retrieve detailed partner payout information for accommodation reservations.
  name: Booking.com Reservation payout details API
  slug: booking-com-reservation-payout-details-api
- baseURL: https://demandapi.booking.com/3.2
  baseurl_source: declared
  description: Provides reservation status information with respect to a reservation ID.
  name: Booking.com Reservation Status API
  slug: booking-com-reservation-status-api-api
- baseURL: https://demandapi.booking.com/3.2
  baseurl_source: declared
  description: Create, update, retrieve and delete property units
  name: Booking.com Rooms API
  slug: booking-com-rooms-api-api
- baseURL: https://demandapi.booking.com/3.2
  baseurl_source: declared
  description: Create, update and delete multiple units
  name: Booking.com Rooms API Bulk API
  slug: booking-com-rooms-api-bulk-api
- baseURL: https://demandapi.booking.com/3.2
  baseurl_source: declared
  description: This collection includes endpoints related to **transfer** services within the connected trip experience.<br/>Use these endpoints to:<br/>- Search for airport transfers and point-to-point rides.<br/>-
  name: Booking.com Transfers API
  slug: booking-com-transfers-api
- baseURL: https://demandapi.booking.com/3.2
  baseurl_source: declared
  description: Retrieve catalog of value adds available for properties with dynamic attributes
  name: Booking.com Value Adds API
  slug: booking-com-value-adds-api
- baseURL: https://demandapi.booking.com/3.2
  baseurl_source: declared
  description: Provides VCC payout details for an accommodation reservation
  name: Booking.com VCC payout details, per accommodation reservation API
  slug: booking-com-vcc-payout-details-per-accommodation-reservation-api
- baseURL: https://demandapi.booking.com/3.2
  baseurl_source: declared
  description: Provides information of the VCCs to be charged.
  name: Booking.com VCCs to be charged API
  slug: booking-com-vccs-to-be-charged-api
artifact_total: 101
asyncapis:
- description: ''
  name: Booking Com Webhooks
  slug: booking-com-webhooks
collections:
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
- group: other
  href: https://artifacts.apis.io/booking-com/capabilities/booking-com-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/booking-com-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/booking-com/overlays/booking-com-demand-api-3-2-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/booking-com-demand-api-3-2-overlay.yaml
- group: other
  href: https://artifacts.apis.io/booking-com/overlays/booking-com-demand-api-3-1-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/booking-com-demand-api-3-1-overlay.yaml
- group: other
  href: https://artifacts.apis.io/booking-com/overlays/booking-com-demand-api-3-2-beta-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/booking-com-demand-api-3-2-beta-overlay.yaml
- group: other
  href: https://artifacts.apis.io/booking-com/overlays/booking-com-connect-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/booking-com-connect-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/booking-com/overlays/booking-com-charges-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/booking-com-charges-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/booking-com/overlays/booking-com-contracting-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/booking-com-contracting-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/booking-com/overlays/booking-com-facilities-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/booking-com-facilities-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/booking-com/overlays/booking-com-facilities-api-remote-sync-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/booking-com-facilities-api-remote-sync-overlay.yaml
- group: other
  href: https://artifacts.apis.io/booking-com/overlays/booking-com-payments-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/booking-com-payments-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/booking-com/overlays/booking-com-payments-by-booking-onboarding-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/booking-com-payments-by-booking-onboarding-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/booking-com/overlays/booking-com-property-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/booking-com-property-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/booking-com/overlays/booking-com-reconciliation-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/booking-com-reconciliation-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/booking-com/overlays/booking-com-rooms-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/booking-com-rooms-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/booking-com/overlays/booking-com-rooms-api-bulk-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/booking-com-rooms-api-bulk-overlay.yaml
- group: other
  href: https://artifacts.apis.io/booking-com/overlays/booking-com-rooms-api-generated-names-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/booking-com-rooms-api-generated-names-overlay.yaml
- group: other
  href: https://artifacts.apis.io/booking-com/overlays/booking-com-valueadds-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/booking-com-valueadds-api-overlay.yaml
- group: auth
  href: https://artifacts.apis.io/booking-com/security/booking-com-trust-center.yml
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
  href: https://artifacts.apis.io/booking-com/agentic-access/booking-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/booking-com-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/booking-com/security/booking-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/booking-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/booking-com/security/booking-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/booking-com-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/booking-com/authentication/booking-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/booking-com-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bookingcom
- group: design
  href: https://artifacts.apis.io/booking-com/json-ld/booking-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/booking-com-context.jsonld
- group: docs
  href: https://artifacts.apis.io/booking-com/json-schema/booking-com-accommodation-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/booking-com-accommodation-schema.json
- group: docs
  href: https://artifacts.apis.io/booking-com/json-schema/booking-com-order-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/booking-com-order-schema.json
- group: docs
  href: https://artifacts.apis.io/booking-com/json-schema/booking-com-promotion-schema.json
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
  href: https://artifacts.apis.io/booking-com/well-known/booking-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/booking-com-well-known.yml
- group: auth
  href: https://artifacts.apis.io/booking-com/well-known/booking-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/booking-com-security.txt
- group: other
  href: https://artifacts.apis.io/booking-com/a2a/booking-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/booking-com-a2a.yml
- group: agent
  href: https://artifacts.apis.io/booking-com/mcp/booking-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/booking-com-mcp.yml
- group: build
  href: https://artifacts.apis.io/booking-com/mcp/booking-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/booking-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/booking-com/llms/booking-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/booking-com-llms.txt
- group: design
  href: https://artifacts.apis.io/booking-com/conventions/booking-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/booking-com-conventions.yml
- group: build
  href: https://artifacts.apis.io/booking-com/packages/booking-com-packages.yml
  title: ''
  type: Packages
  url: packages/booking-com-packages.yml
- group: design
  href: https://artifacts.apis.io/booking-com/lifecycle/booking-com-lifecycle.yml
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
  href: https://artifacts.apis.io/booking-com/security/booking-com-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/booking-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/booking-com/security/booking-com-trust-center.yml
  title: ''
  type: Compliance
  url: security/booking-com-trust-center.yml
- group: design
  href: https://artifacts.apis.io/booking-com/conformance/booking-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/booking-com-conformance.yml
- group: design
  href: https://artifacts.apis.io/booking-com/asyncapi/booking-com-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/booking-com-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/booking-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  href: https://artifacts.apis.io/booking-com/sandbox/booking-com-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/booking-com-sandbox.yml
- group: operate
  href: https://artifacts.apis.io/booking-com/changelog/booking-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/booking-com-changelog.yml
- group: commercial
  href: https://artifacts.apis.io/booking-com/plans/booking-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/booking-com-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/booking-com/rate-limits/booking-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/booking-com-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/booking-com/errors/booking-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/booking-com-problem-types.yml
- group: build
  href: https://artifacts.apis.io/booking-com/errors/booking-com-decline-codes.yml
  title: ''
  type: DeclineCodes
  url: errors/booking-com-decline-codes.yml
- group: design
  href: https://artifacts.apis.io/booking-com/data-model/booking-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/booking-com-data-model.yml
- group: commercial
  href: https://artifacts.apis.io/booking-com/finops/booking-com-finops.yml
  title: ''
  type: FinOps
  url: finops/booking-com-finops.yml
- group: design
  href: https://artifacts.apis.io/booking-com/rules/booking-com-jsonschema-spectral-rules.yml
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
- has_sources: true
  method: derived
  name: Booking Com Finops
  primary_unit: ''
  service_category: ''
  slug: booking-com-finops
  template: true
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
- description: 'Booking.com runs a first-party, anonymous, remote MCP server on its developer portal host. It is a DOCUMENTATION server rather than a booking server: it exposes the portal''s own API catalogue, endpoin'
  name: Booking.com Docs MCP server
  slug: booking-com-docs-mcp-server
modified: '2026-09-17'
name: Booking.com
nav: Providers
network: true
overview: 'Booking.com publishes 49 API contracts indexed on the [APIs.io](https://apis.io/) network, including Status API, Contacts API, Historical Reservations API, and 46 more. Tagged areas include Travel, Hospitality, Accommodation, Booking, and Car Rental.


  The Booking.com catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Booking.com''s developer surface includes documentation, authentication, engineering blog, sandbox, changelog, API reference, getting-started guide, and 59 more developer resources.'
plans:
- name: Booking Com Plans Pricing
  plan_count: 0
  slug: booking-com-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 3
  name: Booking Com Rate Limits
  slug: booking-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 6
  extends: []
  name: Booking.com — jsonschema rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: booking-com-jsonschema-spectral-rules
score:
  band: strong
  composite: 64.8
  coverage:
    artifact_dirs: 32
    catalog_earned: 63.3
    catalog_earned_first_party: 12.0
    catalog_gap: 51.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 50.0
    contract_governance: 14.4
    contract_quality: 64.5
    developer_ergonomics: 63.7
    discoverability: 80.0
    operational_transparency: 92.1
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-kingdom
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 64.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 1.3
      total: 79
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 37.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 22.2
screenshot: https://apis.io/screenshots/booking-com/booking-com-2026-06-20T173602.png
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
skill_count: 4
skills:
- name: booking-com-cancel-or-modify-order
  slug: booking-com-cancel-or-modify-order
- name: booking-com-reconcile-connectivity-payouts
  slug: booking-com-reconcile-connectivity-payouts
- name: booking-com-search-and-book-accommodation
  slug: booking-com-search-and-book-accommodation
- name: booking-com-search-car-rentals
  slug: booking-com-search-car-rentals
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
- A2A
- Hotels
website: https://www.booking.com
---
