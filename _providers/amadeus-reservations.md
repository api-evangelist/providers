---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.4
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Amadeus Reservations Agentic Access
  operation_count: 6
  slug: amadeus-reservations-agentic-access
  summary_line: 6 operations · 5 acting
api_count: 1
apis:
- description: The Booking API from Amadeus Reservations — 5 operation(s) for booking.
  name: Amadeus Reservations Booking API
  slug: amadeus-reservations-booking-api
artifact_total: 755
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Flight Create Orders Booking API
  slug: open-amadeus-reservations-booking-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/amadeus-reservations-flight-create-orders-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/amadeus-reservations-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/amadeus-reservations-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amadeus-reservations-domain-security.yml
- group: start
  title: ''
  type: Portal
  url: https://developers.amadeus.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.amadeus.com/self-service/apis-docs/guides/developer-guides/
- group: auth
  title: ''
  type: Authentication
  url: https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262
- group: start
  title: ''
  type: SignUp
  url: https://developers.amadeus.com/register
- group: commercial
  title: ''
  type: Pricing
  url: https://developers.amadeus.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://developers.amadeus.com/blog
- group: operate
  title: ''
  type: FAQ
  url: https://developers.amadeus.com/self-service/apis-docs/guides/developer-guides/faq/
- group: operate
  title: ''
  type: Support
  url: https://developers.amadeus.com/support
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developers.amadeus.com/legal/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://developers.amadeus.com/legal/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/amadeus4dev
- group: build
  title: Python SDK
  type: SDK
  url: https://github.com/amadeus4dev/amadeus-python
- group: build
  title: Node.js SDK
  type: SDK
  url: https://github.com/amadeus4dev/amadeus-node
- group: build
  title: Java SDK
  type: SDK
  url: https://github.com/amadeus4dev/amadeus-java
- group: operate
  title: ''
  type: StatusPage
  url: https://developers.amadeus.com/status
- group: design
  title: ''
  type: SpectralRules
  url: rules/amadeus-reservations-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/amadeus-reservations-vocabulary.yaml
- group: build
  title: ''
  type: Packages
  url: packages/amadeus-reservations-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/amadeus-reservations-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/amadeus-reservations-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/amadeus-reservations-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/amadeus-reservations-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/amadeus-reservations-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/amadeus-reservations-lifecycle.yml
created: '2024-01-01'
description: Amadeus Reservations provides APIs for creating and managing travel bookings including flight orders, hotel reservations, and ground transfer bookings. These APIs power the full reservation lifecycle for online travel agencies, corporate travel platforms, and travel management companies, connecting to Amadeus's global distribution network of airlines, hotels, and transfer operators.
examples:
- key_count: 0
  name: Flight Create Orders Additional Service Type Example
  slug: flight-create-orders-additional-service-type-example
- key_count: 6
  name: Flight Create Orders Address Example
  slug: flight-create-orders-address-example
- key_count: 3
  name: Flight Create Orders Air Travel Document Common Example
  slug: flight-create-orders-air-travel-document-common-example
- key_count: 0
  name: Flight Create Orders Air Travel Document Example
  slug: flight-create-orders-air-travel-document-example
- key_count: 0
  name: Flight Create Orders Aircraft Entry Example
  slug: flight-create-orders-aircraft-entry-example
- key_count: 1
  name: Flight Create Orders Aircraft Equipment Example
  slug: flight-create-orders-aircraft-equipment-example
- key_count: 6
  name: Flight Create Orders Airline Remark Example
  slug: flight-create-orders-airline-remark-example
- key_count: 0
  name: Flight Create Orders Airline Remark Type Example
  slug: flight-create-orders-airline-remark-type-example
- key_count: 2
  name: Flight Create Orders Allotment Details Example
  slug: flight-create-orders-allotment-details-example
- key_count: 3
  name: Flight Create Orders Associated Record Common Example
  slug: flight-create-orders-associated-record-common-example
- key_count: 0
  name: Flight Create Orders Associated Record Example
  slug: flight-create-orders-associated-record-example
- key_count: 0
  name: Flight Create Orders Automated Process Code Example
  slug: flight-create-orders-automated-process-code-example
- key_count: 3
  name: Flight Create Orders Automated Process Common Example
  slug: flight-create-orders-automated-process-common-example
- key_count: 0
  name: Flight Create Orders Automated Process Example
  slug: flight-create-orders-automated-process-example
- key_count: 6
  name: Flight Create Orders B2B Wallet Example
  slug: flight-create-orders-b2b-wallet-example
- key_count: 3
  name: Flight Create Orders Baggage Allowance Example
  slug: flight-create-orders-baggage-allowance-example
- key_count: 3
  name: Flight Create Orders Base Name Example
  slug: flight-create-orders-base-name-example
- key_count: 0
  name: Flight Create Orders Carrier Entry Example
  slug: flight-create-orders-carrier-entry-example
- key_count: 0
  name: Flight Create Orders Chargeable Checkd Bags Example
  slug: flight-create-orders-chargeable-checkd-bags-example
- key_count: 2
  name: Flight Create Orders Chargeable Seat Example
  slug: flight-create-orders-chargeable-seat-example
- key_count: 3
  name: Flight Create Orders Co2 Emission Example
  slug: flight-create-orders-co2-emission-example
- key_count: 2
  name: Flight Create Orders Collection_ Meta_ Link Example
  slug: flight-create-orders-collection_-meta_-link-example
- key_count: 4
  name: Flight Create Orders Contact Dictionary Example
  slug: flight-create-orders-contact-dictionary-example
- key_count: 0
  name: Flight Create Orders Contact Example
  slug: flight-create-orders-contact-example
- key_count: 0
  name: Flight Create Orders Contact Purpose Example
  slug: flight-create-orders-contact-purpose-example
- key_count: 0
  name: Flight Create Orders Credit Card Brand Example
  slug: flight-create-orders-credit-card-brand-example
- key_count: 4
  name: Flight Create Orders Credit Card Common Example
  slug: flight-create-orders-credit-card-common-example
- key_count: 0
  name: Flight Create Orders Credit Card Example
  slug: flight-create-orders-credit-card-example
- key_count: 0
  name: Flight Create Orders Currency Entry Example
  slug: flight-create-orders-currency-entry-example
- key_count: 4
  name: Flight Create Orders Dictionaries Example
  slug: flight-create-orders-dictionaries-example
- key_count: 5
  name: Flight Create Orders Discount Example
  slug: flight-create-orders-discount-example
- key_count: 0
  name: Flight Create Orders Discount Traveler Type Example
  slug: flight-create-orders-discount-traveler-type-example
- key_count: 0
  name: Flight Create Orders Discount Type Example
  slug: flight-create-orders-discount-type-example
- key_count: 7
  name: Flight Create Orders Document Example
  slug: flight-create-orders-document-example
- key_count: 0
  name: Flight Create Orders Document Type Example
  slug: flight-create-orders-document-type-example
- key_count: 2
  name: Flight Create Orders Elementary Price Example
  slug: flight-create-orders-elementary-price-example
- key_count: 4
  name: Flight Create Orders Emergency Contact Example
  slug: flight-create-orders-emergency-contact-example
- key_count: 1
  name: Flight Create Orders Error_400 Example
  slug: flight-create-orders-error_400-example
- key_count: 1
  name: Flight Create Orders Error_500 Example
  slug: flight-create-orders-error_500-example
- key_count: 0
  name: Flight Create Orders Extended_ Price Example
  slug: flight-create-orders-extended_-price-example
- key_count: 2
  name: Flight Create Orders Fee Example
  slug: flight-create-orders-fee-example
- key_count: 0
  name: Flight Create Orders Fee Type Example
  slug: flight-create-orders-fee-type-example
- key_count: 0
  name: Flight Create Orders Flight End Point Example
  slug: flight-create-orders-flight-end-point-example
- key_count: 16
  name: Flight Create Orders Flight Offer Example
  slug: flight-create-orders-flight-offer-example
- key_count: 0
  name: Flight Create Orders Flight Offer Source Example
  slug: flight-create-orders-flight-offer-source-example
- key_count: 14
  name: Flight Create Orders Flight Order Example
  slug: flight-create-orders-flight-order-example
- key_count: 8
  name: Flight Create Orders Flight Segment Example
  slug: flight-create-orders-flight-segment-example
- key_count: 0
  name: Flight Create Orders Flight Stop Example
  slug: flight-create-orders-flight-stop-example
- key_count: 5
  name: Flight Create Orders Form Of Identification Example
  slug: flight-create-orders-form-of-identification-example
- key_count: 3
  name: Flight Create Orders Form Of Payment Example
  slug: flight-create-orders-form-of-payment-example
- key_count: 5
  name: Flight Create Orders General Remark Example
  slug: flight-create-orders-general-remark-example
- key_count: 0
  name: Flight Create Orders General Remark Type Example
  slug: flight-create-orders-general-remark-type-example
- key_count: 0
  name: Flight Create Orders Identity Document Example
  slug: flight-create-orders-identity-document-example
- key_count: 5
  name: Flight Create Orders Issue Example
  slug: flight-create-orders-issue-example
- key_count: 0
  name: Flight Create Orders Location Entry Example
  slug: flight-create-orders-location-entry-example
- key_count: 2
  name: Flight Create Orders Location Value Example
  slug: flight-create-orders-location-value-example
- key_count: 2
  name: Flight Create Orders Loyalty Program Example
  slug: flight-create-orders-loyalty-program-example
- key_count: 0
  name: Flight Create Orders Name Example
  slug: flight-create-orders-name-example
- key_count: 1
  name: Flight Create Orders Operating Flight Example
  slug: flight-create-orders-operating-flight-example
- key_count: 2
  name: Flight Create Orders Original Flight End Point Example
  slug: flight-create-orders-original-flight-end-point-example
- key_count: 2
  name: Flight Create Orders Original Flight Stop Example
  slug: flight-create-orders-original-flight-stop-example
- key_count: 2
  name: Flight Create Orders Other Method Example
  slug: flight-create-orders-other-method-example
- key_count: 0
  name: Flight Create Orders Other Payment Method Example
  slug: flight-create-orders-other-payment-method-example
- key_count: 0
  name: Flight Create Orders Phone Device Type Example
  slug: flight-create-orders-phone-device-type-example
- key_count: 3
  name: Flight Create Orders Phone Example
  slug: flight-create-orders-phone-example
- key_count: 6
  name: Flight Create Orders Price Example
  slug: flight-create-orders-price-example
- key_count: 0
  name: Flight Create Orders Pricing Options Fare Type Example
  slug: flight-create-orders-pricing-options-fare-type-example
- key_count: 2
  name: Flight Create Orders Remarks Example
  slug: flight-create-orders-remarks-example
- key_count: 0
  name: Flight Create Orders Segment Example
  slug: flight-create-orders-segment-example
- key_count: 0
  name: Flight Create Orders Service Name Example
  slug: flight-create-orders-service-name-example
- key_count: 0
  name: Flight Create Orders Slice Dice Indicator Example
  slug: flight-create-orders-slice-dice-indicator-example
- key_count: 5
  name: Flight Create Orders Stakeholder Example
  slug: flight-create-orders-stakeholder-example
- key_count: 0
  name: Flight Create Orders Stakeholder Gender Example
  slug: flight-create-orders-stakeholder-gender-example
- key_count: 2
  name: Flight Create Orders Tax Example
  slug: flight-create-orders-tax-example
- key_count: 4
  name: Flight Create Orders Ticketing Agreement Example
  slug: flight-create-orders-ticketing-agreement-example
- key_count: 0
  name: Flight Create Orders Ticketing Agreement Option Example
  slug: flight-create-orders-ticketing-agreement-option-example
- key_count: 0
  name: Flight Create Orders Travel Class Example
  slug: flight-create-orders-travel-class-example
- key_count: 0
  name: Flight Create Orders Traveler Example
  slug: flight-create-orders-traveler-example
- key_count: 0
  name: Flight Create Orders Traveler Pricing Fare Option Example
  slug: flight-create-orders-traveler-pricing-fare-option-example
- key_count: 0
  name: Flight Create Orders Traveler Type Example
  slug: flight-create-orders-traveler-type-example
- key_count: 0
  name: Flight Create Orders Virtual Credit Card Details Example
  slug: flight-create-orders-virtual-credit-card-details-example
- key_count: 0
  name: Flight Order Management Additional Service Type Example
  slug: flight-order-management-additional-service-type-example
- key_count: 6
  name: Flight Order Management Address Example
  slug: flight-order-management-address-example
- key_count: 3
  name: Flight Order Management Air Travel Document Common Example
  slug: flight-order-management-air-travel-document-common-example
- key_count: 0
  name: Flight Order Management Air Travel Document Example
  slug: flight-order-management-air-travel-document-example
- key_count: 0
  name: Flight Order Management Aircraft Entry Example
  slug: flight-order-management-aircraft-entry-example
- key_count: 1
  name: Flight Order Management Aircraft Equipment Example
  slug: flight-order-management-aircraft-equipment-example
- key_count: 6
  name: Flight Order Management Airline Remark Example
  slug: flight-order-management-airline-remark-example
- key_count: 0
  name: Flight Order Management Airline Remark Type Example
  slug: flight-order-management-airline-remark-type-example
- key_count: 2
  name: Flight Order Management Allotment Details Example
  slug: flight-order-management-allotment-details-example
- key_count: 3
  name: Flight Order Management Associated Record Common Example
  slug: flight-order-management-associated-record-common-example
- key_count: 0
  name: Flight Order Management Associated Record Example
  slug: flight-order-management-associated-record-example
- key_count: 0
  name: Flight Order Management Automated Process Code Example
  slug: flight-order-management-automated-process-code-example
- key_count: 3
  name: Flight Order Management Automated Process Common Example
  slug: flight-order-management-automated-process-common-example
- key_count: 0
  name: Flight Order Management Automated Process Example
  slug: flight-order-management-automated-process-example
- key_count: 6
  name: Flight Order Management B2B Wallet Example
  slug: flight-order-management-b2b-wallet-example
- key_count: 3
  name: Flight Order Management Baggage Allowance Example
  slug: flight-order-management-baggage-allowance-example
- key_count: 3
  name: Flight Order Management Base Name Example
  slug: flight-order-management-base-name-example
- key_count: 0
  name: Flight Order Management Carrier Entry Example
  slug: flight-order-management-carrier-entry-example
- key_count: 0
  name: Flight Order Management Chargeable Checkd Bags Example
  slug: flight-order-management-chargeable-checkd-bags-example
- key_count: 2
  name: Flight Order Management Chargeable Seat Example
  slug: flight-order-management-chargeable-seat-example
- key_count: 3
  name: Flight Order Management Co2 Emission Example
  slug: flight-order-management-co2-emission-example
- key_count: 2
  name: Flight Order Management Collection_ Meta_ Link Example
  slug: flight-order-management-collection_-meta_-link-example
- key_count: 4
  name: Flight Order Management Contact Dictionary Example
  slug: flight-order-management-contact-dictionary-example
- key_count: 0
  name: Flight Order Management Contact Example
  slug: flight-order-management-contact-example
- key_count: 0
  name: Flight Order Management Contact Purpose Example
  slug: flight-order-management-contact-purpose-example
- key_count: 0
  name: Flight Order Management Credit Card Brand Example
  slug: flight-order-management-credit-card-brand-example
- key_count: 4
  name: Flight Order Management Credit Card Common Example
  slug: flight-order-management-credit-card-common-example
- key_count: 0
  name: Flight Order Management Credit Card Example
  slug: flight-order-management-credit-card-example
- key_count: 0
  name: Flight Order Management Currency Entry Example
  slug: flight-order-management-currency-entry-example
- key_count: 4
  name: Flight Order Management Dictionaries Example
  slug: flight-order-management-dictionaries-example
- key_count: 5
  name: Flight Order Management Discount Example
  slug: flight-order-management-discount-example
- key_count: 0
  name: Flight Order Management Discount Traveler Type Example
  slug: flight-order-management-discount-traveler-type-example
- key_count: 0
  name: Flight Order Management Discount Type Example
  slug: flight-order-management-discount-type-example
- key_count: 7
  name: Flight Order Management Document Example
  slug: flight-order-management-document-example
- key_count: 0
  name: Flight Order Management Document Type Example
  slug: flight-order-management-document-type-example
- key_count: 2
  name: Flight Order Management Elementary Price Example
  slug: flight-order-management-elementary-price-example
- key_count: 4
  name: Flight Order Management Emergency Contact Example
  slug: flight-order-management-emergency-contact-example
- key_count: 1
  name: Flight Order Management Error_400 Example
  slug: flight-order-management-error_400-example
- key_count: 1
  name: Flight Order Management Error_404 Example
  slug: flight-order-management-error_404-example
- key_count: 1
  name: Flight Order Management Error_500 Example
  slug: flight-order-management-error_500-example
- key_count: 0
  name: Flight Order Management Extended_ Price Example
  slug: flight-order-management-extended_-price-example
- key_count: 2
  name: Flight Order Management Fee Example
  slug: flight-order-management-fee-example
- key_count: 0
  name: Flight Order Management Fee Type Example
  slug: flight-order-management-fee-type-example
- key_count: 0
  name: Flight Order Management Flight End Point Example
  slug: flight-order-management-flight-end-point-example
- key_count: 16
  name: Flight Order Management Flight Offer Example
  slug: flight-order-management-flight-offer-example
- key_count: 0
  name: Flight Order Management Flight Offer Source Example
  slug: flight-order-management-flight-offer-source-example
- key_count: 14
  name: Flight Order Management Flight Order Example
  slug: flight-order-management-flight-order-example
- key_count: 11
  name: Flight Order Management Flight Segment Example
  slug: flight-order-management-flight-segment-example
- key_count: 0
  name: Flight Order Management Flight Stop Example
  slug: flight-order-management-flight-stop-example
- key_count: 5
  name: Flight Order Management Form Of Identification Example
  slug: flight-order-management-form-of-identification-example
- key_count: 3
  name: Flight Order Management Form Of Payment Example
  slug: flight-order-management-form-of-payment-example
- key_count: 5
  name: Flight Order Management General Remark Example
  slug: flight-order-management-general-remark-example
- key_count: 0
  name: Flight Order Management General Remark Type Example
  slug: flight-order-management-general-remark-type-example
- key_count: 0
  name: Flight Order Management Identity Document Example
  slug: flight-order-management-identity-document-example
- key_count: 5
  name: Flight Order Management Issue Example
  slug: flight-order-management-issue-example
- key_count: 0
  name: Flight Order Management Location Entry Example
  slug: flight-order-management-location-entry-example
- key_count: 2
  name: Flight Order Management Location Value Example
  slug: flight-order-management-location-value-example
- key_count: 2
  name: Flight Order Management Loyalty Program Example
  slug: flight-order-management-loyalty-program-example
- key_count: 0
  name: Flight Order Management Name Example
  slug: flight-order-management-name-example
- key_count: 1
  name: Flight Order Management Operating Flight Example
  slug: flight-order-management-operating-flight-example
- key_count: 2
  name: Flight Order Management Original Flight End Point Example
  slug: flight-order-management-original-flight-end-point-example
- key_count: 2
  name: Flight Order Management Original Flight Stop Example
  slug: flight-order-management-original-flight-stop-example
- key_count: 2
  name: Flight Order Management Other Method Example
  slug: flight-order-management-other-method-example
- key_count: 0
  name: Flight Order Management Other Payment Method Example
  slug: flight-order-management-other-payment-method-example
- key_count: 0
  name: Flight Order Management Phone Device Type Example
  slug: flight-order-management-phone-device-type-example
- key_count: 3
  name: Flight Order Management Phone Example
  slug: flight-order-management-phone-example
- key_count: 6
  name: Flight Order Management Price Example
  slug: flight-order-management-price-example
- key_count: 0
  name: Flight Order Management Pricing Options Fare Type Example
  slug: flight-order-management-pricing-options-fare-type-example
- key_count: 2
  name: Flight Order Management Remarks Example
  slug: flight-order-management-remarks-example
- key_count: 0
  name: Flight Order Management Segment Example
  slug: flight-order-management-segment-example
- key_count: 0
  name: Flight Order Management Service Name Example
  slug: flight-order-management-service-name-example
- key_count: 0
  name: Flight Order Management Slice Dice Indicator Example
  slug: flight-order-management-slice-dice-indicator-example
- key_count: 5
  name: Flight Order Management Stakeholder Example
  slug: flight-order-management-stakeholder-example
- key_count: 0
  name: Flight Order Management Stakeholder Gender Example
  slug: flight-order-management-stakeholder-gender-example
- key_count: 2
  name: Flight Order Management Tax Example
  slug: flight-order-management-tax-example
- key_count: 4
  name: Flight Order Management Ticketing Agreement Example
  slug: flight-order-management-ticketing-agreement-example
- key_count: 0
  name: Flight Order Management Ticketing Agreement Option Example
  slug: flight-order-management-ticketing-agreement-option-example
- key_count: 0
  name: Flight Order Management Travel Class Example
  slug: flight-order-management-travel-class-example
- key_count: 0
  name: Flight Order Management Traveler Example
  slug: flight-order-management-traveler-example
- key_count: 0
  name: Flight Order Management Traveler Pricing Fare Option Example
  slug: flight-order-management-traveler-pricing-fare-option-example
- key_count: 0
  name: Flight Order Management Traveler Type Example
  slug: flight-order-management-traveler-type-example
- key_count: 0
  name: Flight Order Management Virtual Credit Card Details Example
  slug: flight-order-management-virtual-credit-card-details-example
- key_count: 5
  name: Hotel Booking Address Example
  slug: hotel-booking-address-example
- key_count: 4
  name: Hotel Booking Arrival Flight Details Example
  slug: hotel-booking-arrival-flight-details-example
- key_count: 4
  name: Hotel Booking Create Hotel Booking Example
  slug: hotel-booking-create-hotel-booking-example
- key_count: 1
  name: Hotel Booking Errors Example
  slug: hotel-booking-errors-example
- key_count: 7
  name: Hotel Booking Guest Example
  slug: hotel-booking-guest-example
- key_count: 2
  name: Hotel Booking Guests Example
  slug: hotel-booking-guests-example
- key_count: 10
  name: Hotel Booking Hotel Booking Example
  slug: hotel-booking-hotel-booking-example
- key_count: 0
  name: Hotel Booking Hotel Offer Example
  slug: hotel-booking-hotel-offer-example
- key_count: 6
  name: Hotel Booking Hotel Order Example
  slug: hotel-booking-hotel-order-example
- key_count: 11
  name: Hotel Booking Hotel Product Example
  slug: hotel-booking-hotel-product-example
- key_count: 4
  name: Hotel Booking Hotel Product_ Deposit Policy Example
  slug: hotel-booking-hotel-product_-deposit-policy-example
- key_count: 2
  name: Hotel Booking Hotel Product_ Payment Policy Example
  slug: hotel-booking-hotel-product_-payment-policy-example
- key_count: 3
  name: Hotel Booking Hotel_ Contact Example
  slug: hotel-booking-hotel_-contact-example
- key_count: 3
  name: Hotel Booking Payment Input Example
  slug: hotel-booking-payment-input-example
- key_count: 5
  name: Hotel Booking Payment Output Example
  slug: hotel-booking-payment-output-example
- key_count: 5
  name: Hotel Booking Price Example
  slug: hotel-booking-price-example
- key_count: 2
  name: Hotel Booking Qualified Free Text Example
  slug: hotel-booking-qualified-free-text-example
- key_count: 3
  name: Hotel Booking Room Association Example
  slug: hotel-booking-room-association-example
- key_count: 7
  name: Hotel Booking Warning Example
  slug: hotel-booking-warning-example
- key_count: 5
  name: Transfer Booking Address Common Example
  slug: transfer-booking-address-common-example
- key_count: 7
  name: Transfer Booking Address Example
  slug: transfer-booking-address-example
- key_count: 1
  name: Transfer Booking Agency Example
  slug: transfer-booking-agency-example
- key_count: 2
  name: Transfer Booking Baggage Example
  slug: transfer-booking-baggage-example
- key_count: 7
  name: Transfer Booking Cancellation Rule Example
  slug: transfer-booking-cancellation-rule-example
- key_count: 2
  name: Transfer Booking Contact Example
  slug: transfer-booking-contact-example
- key_count: 0
  name: Transfer Booking Contact With Address Example
  slug: transfer-booking-contact-with-address-example
- key_count: 2
  name: Transfer Booking Corporation Example
  slug: transfer-booking-corporation-example
- key_count: 5
  name: Transfer Booking Credit Card Example
  slug: transfer-booking-credit-card-example
- key_count: 2
  name: Transfer Booking Discount Code Example
  slug: transfer-booking-discount-code-example
- key_count: 2
  name: Transfer Booking Distance Example
  slug: transfer-booking-distance-example
- key_count: 8
  name: Transfer Booking Equipment Example
  slug: transfer-booking-equipment-example
- key_count: 1
  name: Transfer Booking Error_400 Example
  slug: transfer-booking-error_400-example
- key_count: 1
  name: Transfer Booking Error_401 Example
  slug: transfer-booking-error_401-example
- key_count: 1
  name: Transfer Booking Error_500 Example
  slug: transfer-booking-error_500-example
- key_count: 10
  name: Transfer Booking Extra Service Example
  slug: transfer-booking-extra-service-example
- key_count: 0
  name: Transfer Booking Fee Example
  slug: transfer-booking-fee-example
- key_count: 5
  name: Transfer Booking Issue Example
  slug: transfer-booking-issue-example
- key_count: 6
  name: Transfer Booking Location Example
  slug: transfer-booking-location-example
- key_count: 2
  name: Transfer Booking Loyalty Number Example
  slug: transfer-booking-loyalty-number-example
- key_count: 4
  name: Transfer Booking Name Example
  slug: transfer-booking-name-example
- key_count: 1
  name: Transfer Booking Partner Info Example
  slug: transfer-booking-partner-info-example
- key_count: 2
  name: Transfer Booking Passenger Characteristics Example
  slug: transfer-booking-passenger-characteristics-example
- key_count: 0
  name: Transfer Booking Passenger Example
  slug: transfer-booking-passenger-example
- key_count: 4
  name: Transfer Booking Payment Example
  slug: transfer-booking-payment-example
- key_count: 1
  name: Transfer Booking Points And Cash Example
  slug: transfer-booking-points-and-cash-example
- key_count: 0
  name: Transfer Booking Quotation Example
  slug: transfer-booking-quotation-example
- key_count: 3
  name: Transfer Booking Seat Example
  slug: transfer-booking-seat-example
- key_count: 8
  name: Transfer Booking Service Provider Example
  slug: transfer-booking-service-provider-example
- key_count: 3
  name: Transfer Booking Stop Over Example
  slug: transfer-booking-stop-over-example
- key_count: 0
  name: Transfer Booking Tax Example
  slug: transfer-booking-tax-example
- key_count: 17
  name: Transfer Booking Transfer Example
  slug: transfer-booking-transfer-example
- key_count: 6
  name: Transfer Booking Transfer Order Example
  slug: transfer-booking-transfer-order-example
- key_count: 0
  name: Transfer Booking Transfer Reservation Example
  slug: transfer-booking-transfer-reservation-example
- key_count: 0
  name: Transfer Booking Transportation Type Example
  slug: transfer-booking-transportation-type-example
- key_count: 4
  name: Transfer Booking Travel Segment Example
  slug: transfer-booking-travel-segment-example
- key_count: 3
  name: Transfer Booking Travel Segment Location Example
  slug: transfer-booking-travel-segment-location-example
- key_count: 6
  name: Transfer Booking Vehicle Example
  slug: transfer-booking-vehicle-example
- key_count: 1
  name: Transfer Management Error_400 Example
  slug: transfer-management-error_400-example
- key_count: 1
  name: Transfer Management Error_401 Example
  slug: transfer-management-error_401-example
- key_count: 1
  name: Transfer Management Error_404 Example
  slug: transfer-management-error_404-example
- key_count: 1
  name: Transfer Management Error_500 Example
  slug: transfer-management-error_500-example
- key_count: 5
  name: Transfer Management Issue Example
  slug: transfer-management-issue-example
- key_count: 2
  name: Transfer Management Transfer Cancellation Example
  slug: transfer-management-transfer-cancellation-example
features:
- description: Book rooms at over 150,000 hotels worldwide using Amadeus GDS connectivity, with instant confirmation and property reference numbers.
  name: Hotel Booking at Scale
- description: Create confirmed airline reservations with full PNR support across hundreds of airlines in the Amadeus inventory.
  name: Flight Order Creation
- description: Create reservations for multiple travelers in a single API call, managing individual passenger details and fare assignments.
  name: Multi-Traveler Bookings
- description: Book airport taxis, private cars, and shuttle services with real-time availability and instant confirmation.
  name: Ground Transfer Bookings
- description: Retrieve and cancel existing flight and transfer reservations programmatically with full booking detail access.
  name: Order Management
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/amadeus-reservations.png
integrations:
- description: Flight Create Orders works with Flight Offers Search to convert priced flight offers into confirmed airline reservations.
  name: Amadeus Flight Offers Search
- description: Hotel Booking completes the hotel shopping flow started by Hotel Search, converting hotel offers into confirmed reservations.
  name: Amadeus Hotel Search
- description: Transfer Booking confirms ground transportation offers returned by the Transfer Search API.
  name: Amadeus Transfer Search
- description: Validate and reprice flight offers before booking to ensure accurate pricing at time of reservation creation.
  name: Amadeus Flight Offers Price
- description: Use Hotel Name Autocomplete to let users search for properties before fetching offers and creating hotel bookings.
  name: Amadeus Hotel Name Autocomplete
json_schemas:
- name: AdditionalServiceType
  property_count: 0
  slug: flight-create-orders-additional-service-type
- name: Address
  property_count: 6
  slug: flight-create-orders-address
- name: AirTravelDocumentCommon
  property_count: 3
  slug: flight-create-orders-air-travel-document-common
- name: AirTravelDocument
  property_count: 0
  slug: flight-create-orders-air-travel-document
- name: AircraftEntry
  property_count: 0
  slug: flight-create-orders-aircraft-entry
- name: AircraftEquipment
  property_count: 1
  slug: flight-create-orders-aircraft-equipment
- name: AirlineRemark
  property_count: 6
  slug: flight-create-orders-airline-remark
- name: AirlineRemarkType
  property_count: 0
  slug: flight-create-orders-airline-remark-type
- name: AllotmentDetails
  property_count: 2
  slug: flight-create-orders-allotment-details
- name: AssociatedRecordCommon
  property_count: 3
  slug: flight-create-orders-associated-record-common
- name: AssociatedRecord
  property_count: 0
  slug: flight-create-orders-associated-record
- name: AutomatedProcessCode
  property_count: 0
  slug: flight-create-orders-automated-process-code
- name: AutomatedProcessCommon
  property_count: 3
  slug: flight-create-orders-automated-process-common
- name: AutomatedProcess
  property_count: 0
  slug: flight-create-orders-automated-process
- name: B2bWallet
  property_count: 6
  slug: flight-create-orders-b2b-wallet
- name: BaggageAllowance
  property_count: 3
  slug: flight-create-orders-baggage-allowance
- name: BaseName
  property_count: 3
  slug: flight-create-orders-base-name
- name: CarrierEntry
  property_count: 0
  slug: flight-create-orders-carrier-entry
- name: ChargeableCheckdBags
  property_count: 0
  slug: flight-create-orders-chargeable-checkd-bags
- name: ChargeableSeat
  property_count: 2
  slug: flight-create-orders-chargeable-seat
- name: Co2Emission
  property_count: 3
  slug: flight-create-orders-co2-emission
- name: Collection_Meta_Link
  property_count: 2
  slug: flight-create-orders-collection_-meta_-link
- name: ContactDictionary
  property_count: 4
  slug: flight-create-orders-contact-dictionary
- name: ContactPurpose
  property_count: 0
  slug: flight-create-orders-contact-purpose
- name: Contact
  property_count: 0
  slug: flight-create-orders-contact
- name: CreditCardBrand
  property_count: 0
  slug: flight-create-orders-credit-card-brand
- name: CreditCardCommon
  property_count: 4
  slug: flight-create-orders-credit-card-common
- name: CreditCard
  property_count: 0
  slug: flight-create-orders-credit-card
- name: CurrencyEntry
  property_count: 0
  slug: flight-create-orders-currency-entry
- name: Dictionaries
  property_count: 4
  slug: flight-create-orders-dictionaries
- name: Discount
  property_count: 5
  slug: flight-create-orders-discount
- name: DiscountTravelerType
  property_count: 0
  slug: flight-create-orders-discount-traveler-type
- name: DiscountType
  property_count: 0
  slug: flight-create-orders-discount-type
- name: Document
  property_count: 7
  slug: flight-create-orders-document
- name: DocumentType
  property_count: 0
  slug: flight-create-orders-document-type
- name: ElementaryPrice
  property_count: 2
  slug: flight-create-orders-elementary-price
- name: EmergencyContact
  property_count: 4
  slug: flight-create-orders-emergency-contact
- name: Error_400
  property_count: 1
  slug: flight-create-orders-error_400
- name: Error_500
  property_count: 1
  slug: flight-create-orders-error_500
- name: Extended_Price
  property_count: 0
  slug: flight-create-orders-extended_-price
- name: Fee
  property_count: 2
  slug: flight-create-orders-fee
- name: FeeType
  property_count: 0
  slug: flight-create-orders-fee-type
- name: FlightEndPoint
  property_count: 0
  slug: flight-create-orders-flight-end-point
- name: FlightOffer
  property_count: 16
  slug: flight-create-orders-flight-offer
- name: FlightOfferSource
  property_count: 0
  slug: flight-create-orders-flight-offer-source
- name: FlightOrder
  property_count: 14
  slug: flight-create-orders-flight-order
- name: FlightSegment
  property_count: 8
  slug: flight-create-orders-flight-segment
- name: FlightStop
  property_count: 0
  slug: flight-create-orders-flight-stop
- name: FormOfIdentification
  property_count: 5
  slug: flight-create-orders-form-of-identification
- name: FormOfPayment
  property_count: 3
  slug: flight-create-orders-form-of-payment
- name: GeneralRemark
  property_count: 5
  slug: flight-create-orders-general-remark
- name: GeneralRemarkType
  property_count: 0
  slug: flight-create-orders-general-remark-type
- name: IdentityDocument
  property_count: 0
  slug: flight-create-orders-identity-document
- name: Issue
  property_count: 5
  slug: flight-create-orders-issue
- name: LocationEntry
  property_count: 0
  slug: flight-create-orders-location-entry
- name: LocationValue
  property_count: 2
  slug: flight-create-orders-location-value
- name: LoyaltyProgram
  property_count: 2
  slug: flight-create-orders-loyalty-program
- name: Name
  property_count: 0
  slug: flight-create-orders-name
- name: OperatingFlight
  property_count: 1
  slug: flight-create-orders-operating-flight
- name: OriginalFlightEndPoint
  property_count: 2
  slug: flight-create-orders-original-flight-end-point
- name: OriginalFlightStop
  property_count: 2
  slug: flight-create-orders-original-flight-stop
- name: OtherMethod
  property_count: 2
  slug: flight-create-orders-other-method
- name: OtherPaymentMethod
  property_count: 0
  slug: flight-create-orders-other-payment-method
- name: PhoneDeviceType
  property_count: 0
  slug: flight-create-orders-phone-device-type
- name: Phone
  property_count: 3
  slug: flight-create-orders-phone
- name: Price
  property_count: 6
  slug: flight-create-orders-price
- name: PricingOptionsFareType
  property_count: 0
  slug: flight-create-orders-pricing-options-fare-type
- name: Remarks
  property_count: 2
  slug: flight-create-orders-remarks
- name: Segment
  property_count: 0
  slug: flight-create-orders-segment
- name: ServiceName
  property_count: 0
  slug: flight-create-orders-service-name
- name: SliceDiceIndicator
  property_count: 0
  slug: flight-create-orders-slice-dice-indicator
- name: StakeholderGender
  property_count: 0
  slug: flight-create-orders-stakeholder-gender
- name: Stakeholder
  property_count: 5
  slug: flight-create-orders-stakeholder
- name: Tax
  property_count: 2
  slug: flight-create-orders-tax
- name: TicketingAgreementOption
  property_count: 0
  slug: flight-create-orders-ticketing-agreement-option
- name: TicketingAgreement
  property_count: 4
  slug: flight-create-orders-ticketing-agreement
- name: TravelClass
  property_count: 0
  slug: flight-create-orders-travel-class
- name: TravelerPricingFareOption
  property_count: 0
  slug: flight-create-orders-traveler-pricing-fare-option
- name: Traveler
  property_count: 0
  slug: flight-create-orders-traveler
- name: TravelerType
  property_count: 0
  slug: flight-create-orders-traveler-type
- name: VirtualCreditCardDetails
  property_count: 0
  slug: flight-create-orders-virtual-credit-card-details
- name: AdditionalServiceType
  property_count: 0
  slug: flight-order-management-additional-service-type
- name: Address
  property_count: 6
  slug: flight-order-management-address
- name: AirTravelDocumentCommon
  property_count: 3
  slug: flight-order-management-air-travel-document-common
- name: AirTravelDocument
  property_count: 0
  slug: flight-order-management-air-travel-document
- name: AircraftEntry
  property_count: 0
  slug: flight-order-management-aircraft-entry
- name: AircraftEquipment
  property_count: 1
  slug: flight-order-management-aircraft-equipment
- name: AirlineRemark
  property_count: 6
  slug: flight-order-management-airline-remark
- name: AirlineRemarkType
  property_count: 0
  slug: flight-order-management-airline-remark-type
- name: AllotmentDetails
  property_count: 2
  slug: flight-order-management-allotment-details
- name: AssociatedRecordCommon
  property_count: 3
  slug: flight-order-management-associated-record-common
- name: AssociatedRecord
  property_count: 0
  slug: flight-order-management-associated-record
- name: AutomatedProcessCode
  property_count: 0
  slug: flight-order-management-automated-process-code
- name: AutomatedProcessCommon
  property_count: 3
  slug: flight-order-management-automated-process-common
- name: AutomatedProcess
  property_count: 0
  slug: flight-order-management-automated-process
- name: B2bWallet
  property_count: 6
  slug: flight-order-management-b2b-wallet
- name: BaggageAllowance
  property_count: 3
  slug: flight-order-management-baggage-allowance
- name: BaseName
  property_count: 3
  slug: flight-order-management-base-name
- name: CarrierEntry
  property_count: 0
  slug: flight-order-management-carrier-entry
- name: ChargeableCheckdBags
  property_count: 0
  slug: flight-order-management-chargeable-checkd-bags
- name: ChargeableSeat
  property_count: 2
  slug: flight-order-management-chargeable-seat
- name: Co2Emission
  property_count: 3
  slug: flight-order-management-co2-emission
- name: Collection_Meta_Link
  property_count: 2
  slug: flight-order-management-collection_-meta_-link
- name: ContactDictionary
  property_count: 4
  slug: flight-order-management-contact-dictionary
- name: ContactPurpose
  property_count: 0
  slug: flight-order-management-contact-purpose
- name: Contact
  property_count: 0
  slug: flight-order-management-contact
- name: CreditCardBrand
  property_count: 0
  slug: flight-order-management-credit-card-brand
- name: CreditCardCommon
  property_count: 4
  slug: flight-order-management-credit-card-common
- name: CreditCard
  property_count: 0
  slug: flight-order-management-credit-card
- name: CurrencyEntry
  property_count: 0
  slug: flight-order-management-currency-entry
- name: Dictionaries
  property_count: 4
  slug: flight-order-management-dictionaries
- name: Discount
  property_count: 5
  slug: flight-order-management-discount
- name: DiscountTravelerType
  property_count: 0
  slug: flight-order-management-discount-traveler-type
- name: DiscountType
  property_count: 0
  slug: flight-order-management-discount-type
- name: Document
  property_count: 7
  slug: flight-order-management-document
- name: DocumentType
  property_count: 0
  slug: flight-order-management-document-type
- name: ElementaryPrice
  property_count: 2
  slug: flight-order-management-elementary-price
- name: EmergencyContact
  property_count: 4
  slug: flight-order-management-emergency-contact
- name: Error_400
  property_count: 1
  slug: flight-order-management-error_400
- name: Error_404
  property_count: 1
  slug: flight-order-management-error_404
- name: Error_500
  property_count: 1
  slug: flight-order-management-error_500
- name: Extended_Price
  property_count: 0
  slug: flight-order-management-extended_-price
- name: Fee
  property_count: 2
  slug: flight-order-management-fee
- name: FeeType
  property_count: 0
  slug: flight-order-management-fee-type
- name: FlightEndPoint
  property_count: 0
  slug: flight-order-management-flight-end-point
- name: FlightOffer
  property_count: 16
  slug: flight-order-management-flight-offer
- name: FlightOfferSource
  property_count: 0
  slug: flight-order-management-flight-offer-source
- name: FlightOrder
  property_count: 14
  slug: flight-order-management-flight-order
- name: FlightSegment
  property_count: 11
  slug: flight-order-management-flight-segment
- name: FlightStop
  property_count: 0
  slug: flight-order-management-flight-stop
- name: FormOfIdentification
  property_count: 5
  slug: flight-order-management-form-of-identification
- name: FormOfPayment
  property_count: 3
  slug: flight-order-management-form-of-payment
- name: GeneralRemark
  property_count: 5
  slug: flight-order-management-general-remark
- name: GeneralRemarkType
  property_count: 0
  slug: flight-order-management-general-remark-type
- name: IdentityDocument
  property_count: 0
  slug: flight-order-management-identity-document
- name: Issue
  property_count: 5
  slug: flight-order-management-issue
- name: LocationEntry
  property_count: 0
  slug: flight-order-management-location-entry
- name: LocationValue
  property_count: 2
  slug: flight-order-management-location-value
- name: LoyaltyProgram
  property_count: 2
  slug: flight-order-management-loyalty-program
- name: Name
  property_count: 0
  slug: flight-order-management-name
- name: OperatingFlight
  property_count: 1
  slug: flight-order-management-operating-flight
- name: OriginalFlightEndPoint
  property_count: 2
  slug: flight-order-management-original-flight-end-point
- name: OriginalFlightStop
  property_count: 2
  slug: flight-order-management-original-flight-stop
- name: OtherMethod
  property_count: 2
  slug: flight-order-management-other-method
- name: OtherPaymentMethod
  property_count: 0
  slug: flight-order-management-other-payment-method
- name: PhoneDeviceType
  property_count: 0
  slug: flight-order-management-phone-device-type
- name: Phone
  property_count: 3
  slug: flight-order-management-phone
- name: Price
  property_count: 6
  slug: flight-order-management-price
- name: PricingOptionsFareType
  property_count: 0
  slug: flight-order-management-pricing-options-fare-type
- name: Remarks
  property_count: 2
  slug: flight-order-management-remarks
- name: Segment
  property_count: 0
  slug: flight-order-management-segment
- name: ServiceName
  property_count: 0
  slug: flight-order-management-service-name
- name: SliceDiceIndicator
  property_count: 0
  slug: flight-order-management-slice-dice-indicator
- name: StakeholderGender
  property_count: 0
  slug: flight-order-management-stakeholder-gender
- name: Stakeholder
  property_count: 5
  slug: flight-order-management-stakeholder
- name: Tax
  property_count: 2
  slug: flight-order-management-tax
- name: TicketingAgreementOption
  property_count: 0
  slug: flight-order-management-ticketing-agreement-option
- name: TicketingAgreement
  property_count: 4
  slug: flight-order-management-ticketing-agreement
- name: TravelClass
  property_count: 0
  slug: flight-order-management-travel-class
- name: TravelerPricingFareOption
  property_count: 0
  slug: flight-order-management-traveler-pricing-fare-option
- name: Traveler
  property_count: 0
  slug: flight-order-management-traveler
- name: TravelerType
  property_count: 0
  slug: flight-order-management-traveler-type
- name: VirtualCreditCardDetails
  property_count: 0
  slug: flight-order-management-virtual-credit-card-details
- name: Address
  property_count: 5
  slug: hotel-booking-address
- name: ArrivalFlightDetails
  property_count: 4
  slug: hotel-booking-arrival-flight-details
- name: CreateHotelBooking
  property_count: 4
  slug: hotel-booking-create-hotel-booking
- name: Errors
  property_count: 1
  slug: hotel-booking-errors
- name: Guest
  property_count: 7
  slug: hotel-booking-guest
- name: guests
  property_count: 2
  slug: hotel-booking-guests
- name: HotelBooking
  property_count: 10
  slug: hotel-booking-hotel-booking
- name: HotelOffer
  property_count: 0
  slug: hotel-booking-hotel-offer
- name: HotelOrder
  property_count: 6
  slug: hotel-booking-hotel-order
- name: HotelProduct
  property_count: 11
  slug: hotel-booking-hotel-product
- name: HotelProduct_DepositPolicy
  property_count: 4
  slug: hotel-booking-hotel-product_-deposit-policy
- name: HotelProduct_PaymentPolicy
  property_count: 2
  slug: hotel-booking-hotel-product_-payment-policy
- name: Hotel_Contact
  property_count: 3
  slug: hotel-booking-hotel_-contact
- name: PaymentInput
  property_count: 3
  slug: hotel-booking-payment-input
- name: PaymentOutput
  property_count: 5
  slug: hotel-booking-payment-output
- name: Price
  property_count: 5
  slug: hotel-booking-price
- name: QualifiedFreeText
  property_count: 2
  slug: hotel-booking-qualified-free-text
- name: roomAssociation
  property_count: 3
  slug: hotel-booking-room-association
- name: Warning
  property_count: 7
  slug: hotel-booking-warning
- name: AddressCommon
  property_count: 5
  slug: transfer-booking-address-common
- name: Address
  property_count: 7
  slug: transfer-booking-address
- name: Agency
  property_count: 1
  slug: transfer-booking-agency
- name: Baggage
  property_count: 2
  slug: transfer-booking-baggage
- name: CancellationRule
  property_count: 7
  slug: transfer-booking-cancellation-rule
- name: Contact
  property_count: 2
  slug: transfer-booking-contact
- name: ContactWithAddress
  property_count: 0
  slug: transfer-booking-contact-with-address
- name: Corporation
  property_count: 2
  slug: transfer-booking-corporation
- name: CreditCard
  property_count: 5
  slug: transfer-booking-credit-card
- name: DiscountCode
  property_count: 2
  slug: transfer-booking-discount-code
- name: Distance
  property_count: 2
  slug: transfer-booking-distance
- name: Equipment
  property_count: 8
  slug: transfer-booking-equipment
- name: Error_400
  property_count: 1
  slug: transfer-booking-error_400
- name: Error_401
  property_count: 1
  slug: transfer-booking-error_401
- name: Error_500
  property_count: 1
  slug: transfer-booking-error_500
- name: ExtraService
  property_count: 10
  slug: transfer-booking-extra-service
- name: Fee
  property_count: 0
  slug: transfer-booking-fee
- name: Issue
  property_count: 5
  slug: transfer-booking-issue
- name: Location
  property_count: 6
  slug: transfer-booking-location
- name: LoyaltyNumber
  property_count: 2
  slug: transfer-booking-loyalty-number
- name: Name
  property_count: 4
  slug: transfer-booking-name
- name: PartnerInfo
  property_count: 1
  slug: transfer-booking-partner-info
- name: PassengerCharacteristics
  property_count: 2
  slug: transfer-booking-passenger-characteristics
- name: Passenger
  property_count: 0
  slug: transfer-booking-passenger
- name: Payment
  property_count: 4
  slug: transfer-booking-payment
- name: PointsAndCash
  property_count: 1
  slug: transfer-booking-points-and-cash
- name: Quotation
  property_count: 0
  slug: transfer-booking-quotation
- name: Seat
  property_count: 3
  slug: transfer-booking-seat
- name: ServiceProvider
  property_count: 8
  slug: transfer-booking-service-provider
- name: StopOver
  property_count: 3
  slug: transfer-booking-stop-over
- name: Tax
  property_count: 0
  slug: transfer-booking-tax
- name: TransferOrder
  property_count: 6
  slug: transfer-booking-transfer-order
- name: TransferReservation
  property_count: 0
  slug: transfer-booking-transfer-reservation
- name: Transfer
  property_count: 17
  slug: transfer-booking-transfer
- name: TransportationType
  property_count: 0
  slug: transfer-booking-transportation-type
- name: TravelSegmentLocation
  property_count: 3
  slug: transfer-booking-travel-segment-location
- name: TravelSegment
  property_count: 4
  slug: transfer-booking-travel-segment
- name: Vehicle
  property_count: 6
  slug: transfer-booking-vehicle
- name: Error_400
  property_count: 1
  slug: transfer-management-error_400
- name: Error_401
  property_count: 1
  slug: transfer-management-error_401
- name: Error_404
  property_count: 1
  slug: transfer-management-error_404
- name: Error_500
  property_count: 1
  slug: transfer-management-error_500
- name: Issue
  property_count: 5
  slug: transfer-management-issue
- name: TransferCancellation
  property_count: 2
  slug: transfer-management-transfer-cancellation
json_structures:
- name: Flight Create Orders Additional Service Type Structure
  property_count: 0
  slug: flight-create-orders-additional-service-type-structure
- name: Flight Create Orders Address Structure
  property_count: 6
  slug: flight-create-orders-address-structure
- name: Flight Create Orders Air Travel Document Common Structure
  property_count: 3
  slug: flight-create-orders-air-travel-document-common-structure
- name: Flight Create Orders Air Travel Document Structure
  property_count: 0
  slug: flight-create-orders-air-travel-document-structure
- name: Flight Create Orders Aircraft Entry Structure
  property_count: 0
  slug: flight-create-orders-aircraft-entry-structure
- name: Flight Create Orders Aircraft Equipment Structure
  property_count: 1
  slug: flight-create-orders-aircraft-equipment-structure
- name: Flight Create Orders Airline Remark Structure
  property_count: 6
  slug: flight-create-orders-airline-remark-structure
- name: Flight Create Orders Airline Remark Type Structure
  property_count: 0
  slug: flight-create-orders-airline-remark-type-structure
- name: Flight Create Orders Allotment Details Structure
  property_count: 2
  slug: flight-create-orders-allotment-details-structure
- name: Flight Create Orders Associated Record Common Structure
  property_count: 3
  slug: flight-create-orders-associated-record-common-structure
- name: Flight Create Orders Associated Record Structure
  property_count: 0
  slug: flight-create-orders-associated-record-structure
- name: Flight Create Orders Automated Process Code Structure
  property_count: 0
  slug: flight-create-orders-automated-process-code-structure
- name: Flight Create Orders Automated Process Common Structure
  property_count: 3
  slug: flight-create-orders-automated-process-common-structure
- name: Flight Create Orders Automated Process Structure
  property_count: 0
  slug: flight-create-orders-automated-process-structure
- name: Flight Create Orders B2B Wallet Structure
  property_count: 6
  slug: flight-create-orders-b2b-wallet-structure
- name: Flight Create Orders Baggage Allowance Structure
  property_count: 3
  slug: flight-create-orders-baggage-allowance-structure
- name: Flight Create Orders Base Name Structure
  property_count: 3
  slug: flight-create-orders-base-name-structure
- name: Flight Create Orders Carrier Entry Structure
  property_count: 0
  slug: flight-create-orders-carrier-entry-structure
- name: Flight Create Orders Chargeable Checkd Bags Structure
  property_count: 0
  slug: flight-create-orders-chargeable-checkd-bags-structure
- name: Flight Create Orders Chargeable Seat Structure
  property_count: 2
  slug: flight-create-orders-chargeable-seat-structure
- name: Flight Create Orders Co2 Emission Structure
  property_count: 3
  slug: flight-create-orders-co2-emission-structure
- name: Flight Create Orders Collection_ Meta_ Link Structure
  property_count: 2
  slug: flight-create-orders-collection_-meta_-link-structure
- name: Flight Create Orders Contact Dictionary Structure
  property_count: 4
  slug: flight-create-orders-contact-dictionary-structure
- name: Flight Create Orders Contact Purpose Structure
  property_count: 0
  slug: flight-create-orders-contact-purpose-structure
- name: Flight Create Orders Contact Structure
  property_count: 0
  slug: flight-create-orders-contact-structure
- name: Flight Create Orders Credit Card Brand Structure
  property_count: 0
  slug: flight-create-orders-credit-card-brand-structure
- name: Flight Create Orders Credit Card Common Structure
  property_count: 4
  slug: flight-create-orders-credit-card-common-structure
- name: Flight Create Orders Credit Card Structure
  property_count: 0
  slug: flight-create-orders-credit-card-structure
- name: Flight Create Orders Currency Entry Structure
  property_count: 0
  slug: flight-create-orders-currency-entry-structure
- name: Flight Create Orders Dictionaries Structure
  property_count: 4
  slug: flight-create-orders-dictionaries-structure
- name: Flight Create Orders Discount Structure
  property_count: 5
  slug: flight-create-orders-discount-structure
- name: Flight Create Orders Discount Traveler Type Structure
  property_count: 0
  slug: flight-create-orders-discount-traveler-type-structure
- name: Flight Create Orders Discount Type Structure
  property_count: 0
  slug: flight-create-orders-discount-type-structure
- name: Flight Create Orders Document Structure
  property_count: 7
  slug: flight-create-orders-document-structure
- name: Flight Create Orders Document Type Structure
  property_count: 0
  slug: flight-create-orders-document-type-structure
- name: Flight Create Orders Elementary Price Structure
  property_count: 2
  slug: flight-create-orders-elementary-price-structure
- name: Flight Create Orders Emergency Contact Structure
  property_count: 4
  slug: flight-create-orders-emergency-contact-structure
- name: Flight Create Orders Error_400 Structure
  property_count: 1
  slug: flight-create-orders-error_400-structure
- name: Flight Create Orders Error_500 Structure
  property_count: 1
  slug: flight-create-orders-error_500-structure
- name: Flight Create Orders Extended_ Price Structure
  property_count: 0
  slug: flight-create-orders-extended_-price-structure
- name: Flight Create Orders Fee Structure
  property_count: 2
  slug: flight-create-orders-fee-structure
- name: Flight Create Orders Fee Type Structure
  property_count: 0
  slug: flight-create-orders-fee-type-structure
- name: Flight Create Orders Flight End Point Structure
  property_count: 0
  slug: flight-create-orders-flight-end-point-structure
- name: Flight Create Orders Flight Offer Source Structure
  property_count: 0
  slug: flight-create-orders-flight-offer-source-structure
- name: Flight Create Orders Flight Offer Structure
  property_count: 16
  slug: flight-create-orders-flight-offer-structure
- name: Flight Create Orders Flight Order Structure
  property_count: 14
  slug: flight-create-orders-flight-order-structure
- name: Flight Create Orders Flight Segment Structure
  property_count: 8
  slug: flight-create-orders-flight-segment-structure
- name: Flight Create Orders Flight Stop Structure
  property_count: 0
  slug: flight-create-orders-flight-stop-structure
- name: Flight Create Orders Form Of Identification Structure
  property_count: 5
  slug: flight-create-orders-form-of-identification-structure
- name: Flight Create Orders Form Of Payment Structure
  property_count: 3
  slug: flight-create-orders-form-of-payment-structure
- name: Flight Create Orders General Remark Structure
  property_count: 5
  slug: flight-create-orders-general-remark-structure
- name: Flight Create Orders General Remark Type Structure
  property_count: 0
  slug: flight-create-orders-general-remark-type-structure
- name: Flight Create Orders Identity Document Structure
  property_count: 0
  slug: flight-create-orders-identity-document-structure
- name: Flight Create Orders Issue Structure
  property_count: 5
  slug: flight-create-orders-issue-structure
- name: Flight Create Orders Location Entry Structure
  property_count: 0
  slug: flight-create-orders-location-entry-structure
- name: Flight Create Orders Location Value Structure
  property_count: 2
  slug: flight-create-orders-location-value-structure
- name: Flight Create Orders Loyalty Program Structure
  property_count: 2
  slug: flight-create-orders-loyalty-program-structure
- name: Flight Create Orders Name Structure
  property_count: 0
  slug: flight-create-orders-name-structure
- name: Flight Create Orders Operating Flight Structure
  property_count: 1
  slug: flight-create-orders-operating-flight-structure
- name: Flight Create Orders Original Flight End Point Structure
  property_count: 2
  slug: flight-create-orders-original-flight-end-point-structure
- name: Flight Create Orders Original Flight Stop Structure
  property_count: 2
  slug: flight-create-orders-original-flight-stop-structure
- name: Flight Create Orders Other Method Structure
  property_count: 2
  slug: flight-create-orders-other-method-structure
- name: Flight Create Orders Other Payment Method Structure
  property_count: 0
  slug: flight-create-orders-other-payment-method-structure
- name: Flight Create Orders Phone Device Type Structure
  property_count: 0
  slug: flight-create-orders-phone-device-type-structure
- name: Flight Create Orders Phone Structure
  property_count: 3
  slug: flight-create-orders-phone-structure
- name: Flight Create Orders Price Structure
  property_count: 6
  slug: flight-create-orders-price-structure
- name: Flight Create Orders Pricing Options Fare Type Structure
  property_count: 0
  slug: flight-create-orders-pricing-options-fare-type-structure
- name: Flight Create Orders Remarks Structure
  property_count: 2
  slug: flight-create-orders-remarks-structure
- name: Flight Create Orders Segment Structure
  property_count: 0
  slug: flight-create-orders-segment-structure
- name: Flight Create Orders Service Name Structure
  property_count: 0
  slug: flight-create-orders-service-name-structure
- name: Flight Create Orders Slice Dice Indicator Structure
  property_count: 0
  slug: flight-create-orders-slice-dice-indicator-structure
- name: Flight Create Orders Stakeholder Gender Structure
  property_count: 0
  slug: flight-create-orders-stakeholder-gender-structure
- name: Flight Create Orders Stakeholder Structure
  property_count: 5
  slug: flight-create-orders-stakeholder-structure
- name: Flight Create Orders Tax Structure
  property_count: 2
  slug: flight-create-orders-tax-structure
- name: Flight Create Orders Ticketing Agreement Option Structure
  property_count: 0
  slug: flight-create-orders-ticketing-agreement-option-structure
- name: Flight Create Orders Ticketing Agreement Structure
  property_count: 4
  slug: flight-create-orders-ticketing-agreement-structure
- name: Flight Create Orders Travel Class Structure
  property_count: 0
  slug: flight-create-orders-travel-class-structure
- name: Flight Create Orders Traveler Pricing Fare Option Structure
  property_count: 0
  slug: flight-create-orders-traveler-pricing-fare-option-structure
- name: Flight Create Orders Traveler Structure
  property_count: 0
  slug: flight-create-orders-traveler-structure
- name: Flight Create Orders Traveler Type Structure
  property_count: 0
  slug: flight-create-orders-traveler-type-structure
- name: Flight Create Orders Virtual Credit Card Details Structure
  property_count: 0
  slug: flight-create-orders-virtual-credit-card-details-structure
- name: Flight Order Management Additional Service Type Structure
  property_count: 0
  slug: flight-order-management-additional-service-type-structure
- name: Flight Order Management Address Structure
  property_count: 6
  slug: flight-order-management-address-structure
- name: Flight Order Management Air Travel Document Common Structure
  property_count: 3
  slug: flight-order-management-air-travel-document-common-structure
- name: Flight Order Management Air Travel Document Structure
  property_count: 0
  slug: flight-order-management-air-travel-document-structure
- name: Flight Order Management Aircraft Entry Structure
  property_count: 0
  slug: flight-order-management-aircraft-entry-structure
- name: Flight Order Management Aircraft Equipment Structure
  property_count: 1
  slug: flight-order-management-aircraft-equipment-structure
- name: Flight Order Management Airline Remark Structure
  property_count: 6
  slug: flight-order-management-airline-remark-structure
- name: Flight Order Management Airline Remark Type Structure
  property_count: 0
  slug: flight-order-management-airline-remark-type-structure
- name: Flight Order Management Allotment Details Structure
  property_count: 2
  slug: flight-order-management-allotment-details-structure
- name: Flight Order Management Associated Record Common Structure
  property_count: 3
  slug: flight-order-management-associated-record-common-structure
- name: Flight Order Management Associated Record Structure
  property_count: 0
  slug: flight-order-management-associated-record-structure
- name: Flight Order Management Automated Process Code Structure
  property_count: 0
  slug: flight-order-management-automated-process-code-structure
- name: Flight Order Management Automated Process Common Structure
  property_count: 3
  slug: flight-order-management-automated-process-common-structure
- name: Flight Order Management Automated Process Structure
  property_count: 0
  slug: flight-order-management-automated-process-structure
- name: Flight Order Management B2B Wallet Structure
  property_count: 6
  slug: flight-order-management-b2b-wallet-structure
- name: Flight Order Management Baggage Allowance Structure
  property_count: 3
  slug: flight-order-management-baggage-allowance-structure
- name: Flight Order Management Base Name Structure
  property_count: 3
  slug: flight-order-management-base-name-structure
- name: Flight Order Management Carrier Entry Structure
  property_count: 0
  slug: flight-order-management-carrier-entry-structure
- name: Flight Order Management Chargeable Checkd Bags Structure
  property_count: 0
  slug: flight-order-management-chargeable-checkd-bags-structure
- name: Flight Order Management Chargeable Seat Structure
  property_count: 2
  slug: flight-order-management-chargeable-seat-structure
- name: Flight Order Management Co2 Emission Structure
  property_count: 3
  slug: flight-order-management-co2-emission-structure
- name: Flight Order Management Collection_ Meta_ Link Structure
  property_count: 2
  slug: flight-order-management-collection_-meta_-link-structure
- name: Flight Order Management Contact Dictionary Structure
  property_count: 4
  slug: flight-order-management-contact-dictionary-structure
- name: Flight Order Management Contact Purpose Structure
  property_count: 0
  slug: flight-order-management-contact-purpose-structure
- name: Flight Order Management Contact Structure
  property_count: 0
  slug: flight-order-management-contact-structure
- name: Flight Order Management Credit Card Brand Structure
  property_count: 0
  slug: flight-order-management-credit-card-brand-structure
- name: Flight Order Management Credit Card Common Structure
  property_count: 4
  slug: flight-order-management-credit-card-common-structure
- name: Flight Order Management Credit Card Structure
  property_count: 0
  slug: flight-order-management-credit-card-structure
- name: Flight Order Management Currency Entry Structure
  property_count: 0
  slug: flight-order-management-currency-entry-structure
- name: Flight Order Management Dictionaries Structure
  property_count: 4
  slug: flight-order-management-dictionaries-structure
- name: Flight Order Management Discount Structure
  property_count: 5
  slug: flight-order-management-discount-structure
- name: Flight Order Management Discount Traveler Type Structure
  property_count: 0
  slug: flight-order-management-discount-traveler-type-structure
- name: Flight Order Management Discount Type Structure
  property_count: 0
  slug: flight-order-management-discount-type-structure
- name: Flight Order Management Document Structure
  property_count: 7
  slug: flight-order-management-document-structure
- name: Flight Order Management Document Type Structure
  property_count: 0
  slug: flight-order-management-document-type-structure
- name: Flight Order Management Elementary Price Structure
  property_count: 2
  slug: flight-order-management-elementary-price-structure
- name: Flight Order Management Emergency Contact Structure
  property_count: 4
  slug: flight-order-management-emergency-contact-structure
- name: Flight Order Management Error_400 Structure
  property_count: 1
  slug: flight-order-management-error_400-structure
- name: Flight Order Management Error_404 Structure
  property_count: 1
  slug: flight-order-management-error_404-structure
- name: Flight Order Management Error_500 Structure
  property_count: 1
  slug: flight-order-management-error_500-structure
- name: Flight Order Management Extended_ Price Structure
  property_count: 0
  slug: flight-order-management-extended_-price-structure
- name: Flight Order Management Fee Structure
  property_count: 2
  slug: flight-order-management-fee-structure
- name: Flight Order Management Fee Type Structure
  property_count: 0
  slug: flight-order-management-fee-type-structure
- name: Flight Order Management Flight End Point Structure
  property_count: 0
  slug: flight-order-management-flight-end-point-structure
- name: Flight Order Management Flight Offer Source Structure
  property_count: 0
  slug: flight-order-management-flight-offer-source-structure
- name: Flight Order Management Flight Offer Structure
  property_count: 16
  slug: flight-order-management-flight-offer-structure
- name: Flight Order Management Flight Order Structure
  property_count: 14
  slug: flight-order-management-flight-order-structure
- name: Flight Order Management Flight Segment Structure
  property_count: 11
  slug: flight-order-management-flight-segment-structure
- name: Flight Order Management Flight Stop Structure
  property_count: 0
  slug: flight-order-management-flight-stop-structure
- name: Flight Order Management Form Of Identification Structure
  property_count: 5
  slug: flight-order-management-form-of-identification-structure
- name: Flight Order Management Form Of Payment Structure
  property_count: 3
  slug: flight-order-management-form-of-payment-structure
- name: Flight Order Management General Remark Structure
  property_count: 5
  slug: flight-order-management-general-remark-structure
- name: Flight Order Management General Remark Type Structure
  property_count: 0
  slug: flight-order-management-general-remark-type-structure
- name: Flight Order Management Identity Document Structure
  property_count: 0
  slug: flight-order-management-identity-document-structure
- name: Flight Order Management Issue Structure
  property_count: 5
  slug: flight-order-management-issue-structure
- name: Flight Order Management Location Entry Structure
  property_count: 0
  slug: flight-order-management-location-entry-structure
- name: Flight Order Management Location Value Structure
  property_count: 2
  slug: flight-order-management-location-value-structure
- name: Flight Order Management Loyalty Program Structure
  property_count: 2
  slug: flight-order-management-loyalty-program-structure
- name: Flight Order Management Name Structure
  property_count: 0
  slug: flight-order-management-name-structure
- name: Flight Order Management Operating Flight Structure
  property_count: 1
  slug: flight-order-management-operating-flight-structure
- name: Flight Order Management Original Flight End Point Structure
  property_count: 2
  slug: flight-order-management-original-flight-end-point-structure
- name: Flight Order Management Original Flight Stop Structure
  property_count: 2
  slug: flight-order-management-original-flight-stop-structure
- name: Flight Order Management Other Method Structure
  property_count: 2
  slug: flight-order-management-other-method-structure
- name: Flight Order Management Other Payment Method Structure
  property_count: 0
  slug: flight-order-management-other-payment-method-structure
- name: Flight Order Management Phone Device Type Structure
  property_count: 0
  slug: flight-order-management-phone-device-type-structure
- name: Flight Order Management Phone Structure
  property_count: 3
  slug: flight-order-management-phone-structure
- name: Flight Order Management Price Structure
  property_count: 6
  slug: flight-order-management-price-structure
- name: Flight Order Management Pricing Options Fare Type Structure
  property_count: 0
  slug: flight-order-management-pricing-options-fare-type-structure
- name: Flight Order Management Remarks Structure
  property_count: 2
  slug: flight-order-management-remarks-structure
- name: Flight Order Management Segment Structure
  property_count: 0
  slug: flight-order-management-segment-structure
- name: Flight Order Management Service Name Structure
  property_count: 0
  slug: flight-order-management-service-name-structure
- name: Flight Order Management Slice Dice Indicator Structure
  property_count: 0
  slug: flight-order-management-slice-dice-indicator-structure
- name: Flight Order Management Stakeholder Gender Structure
  property_count: 0
  slug: flight-order-management-stakeholder-gender-structure
- name: Flight Order Management Stakeholder Structure
  property_count: 5
  slug: flight-order-management-stakeholder-structure
- name: Flight Order Management Tax Structure
  property_count: 2
  slug: flight-order-management-tax-structure
- name: Flight Order Management Ticketing Agreement Option Structure
  property_count: 0
  slug: flight-order-management-ticketing-agreement-option-structure
- name: Flight Order Management Ticketing Agreement Structure
  property_count: 4
  slug: flight-order-management-ticketing-agreement-structure
- name: Flight Order Management Travel Class Structure
  property_count: 0
  slug: flight-order-management-travel-class-structure
- name: Flight Order Management Traveler Pricing Fare Option Structure
  property_count: 0
  slug: flight-order-management-traveler-pricing-fare-option-structure
- name: Flight Order Management Traveler Structure
  property_count: 0
  slug: flight-order-management-traveler-structure
- name: Flight Order Management Traveler Type Structure
  property_count: 0
  slug: flight-order-management-traveler-type-structure
- name: Flight Order Management Virtual Credit Card Details Structure
  property_count: 0
  slug: flight-order-management-virtual-credit-card-details-structure
- name: Hotel Booking Address Structure
  property_count: 5
  slug: hotel-booking-address-structure
- name: Hotel Booking Arrival Flight Details Structure
  property_count: 4
  slug: hotel-booking-arrival-flight-details-structure
- name: Hotel Booking Create Hotel Booking Structure
  property_count: 4
  slug: hotel-booking-create-hotel-booking-structure
- name: Hotel Booking Errors Structure
  property_count: 1
  slug: hotel-booking-errors-structure
- name: Hotel Booking Guest Structure
  property_count: 7
  slug: hotel-booking-guest-structure
- name: Hotel Booking Guests Structure
  property_count: 2
  slug: hotel-booking-guests-structure
- name: Hotel Booking Hotel Booking Structure
  property_count: 10
  slug: hotel-booking-hotel-booking-structure
- name: Hotel Booking Hotel Offer Structure
  property_count: 0
  slug: hotel-booking-hotel-offer-structure
- name: Hotel Booking Hotel Order Structure
  property_count: 6
  slug: hotel-booking-hotel-order-structure
- name: Hotel Booking Hotel Product Structure
  property_count: 11
  slug: hotel-booking-hotel-product-structure
- name: Hotel Booking Hotel Product_ Deposit Policy Structure
  property_count: 4
  slug: hotel-booking-hotel-product_-deposit-policy-structure
- name: Hotel Booking Hotel Product_ Payment Policy Structure
  property_count: 2
  slug: hotel-booking-hotel-product_-payment-policy-structure
- name: Hotel Booking Hotel_ Contact Structure
  property_count: 3
  slug: hotel-booking-hotel_-contact-structure
- name: Hotel Booking Payment Input Structure
  property_count: 3
  slug: hotel-booking-payment-input-structure
- name: Hotel Booking Payment Output Structure
  property_count: 5
  slug: hotel-booking-payment-output-structure
- name: Hotel Booking Price Structure
  property_count: 5
  slug: hotel-booking-price-structure
- name: Hotel Booking Qualified Free Text Structure
  property_count: 2
  slug: hotel-booking-qualified-free-text-structure
- name: Hotel Booking Room Association Structure
  property_count: 3
  slug: hotel-booking-room-association-structure
- name: Hotel Booking Warning Structure
  property_count: 7
  slug: hotel-booking-warning-structure
- name: Transfer Booking Address Common Structure
  property_count: 5
  slug: transfer-booking-address-common-structure
- name: Transfer Booking Address Structure
  property_count: 7
  slug: transfer-booking-address-structure
- name: Transfer Booking Agency Structure
  property_count: 1
  slug: transfer-booking-agency-structure
- name: Transfer Booking Baggage Structure
  property_count: 2
  slug: transfer-booking-baggage-structure
- name: Transfer Booking Cancellation Rule Structure
  property_count: 7
  slug: transfer-booking-cancellation-rule-structure
- name: Transfer Booking Contact Structure
  property_count: 2
  slug: transfer-booking-contact-structure
- name: Transfer Booking Contact With Address Structure
  property_count: 0
  slug: transfer-booking-contact-with-address-structure
- name: Transfer Booking Corporation Structure
  property_count: 2
  slug: transfer-booking-corporation-structure
- name: Transfer Booking Credit Card Structure
  property_count: 5
  slug: transfer-booking-credit-card-structure
- name: Transfer Booking Discount Code Structure
  property_count: 2
  slug: transfer-booking-discount-code-structure
- name: Transfer Booking Distance Structure
  property_count: 2
  slug: transfer-booking-distance-structure
- name: Transfer Booking Equipment Structure
  property_count: 8
  slug: transfer-booking-equipment-structure
- name: Transfer Booking Error_400 Structure
  property_count: 1
  slug: transfer-booking-error_400-structure
- name: Transfer Booking Error_401 Structure
  property_count: 1
  slug: transfer-booking-error_401-structure
- name: Transfer Booking Error_500 Structure
  property_count: 1
  slug: transfer-booking-error_500-structure
- name: Transfer Booking Extra Service Structure
  property_count: 10
  slug: transfer-booking-extra-service-structure
- name: Transfer Booking Fee Structure
  property_count: 0
  slug: transfer-booking-fee-structure
- name: Transfer Booking Issue Structure
  property_count: 5
  slug: transfer-booking-issue-structure
- name: Transfer Booking Location Structure
  property_count: 6
  slug: transfer-booking-location-structure
- name: Transfer Booking Loyalty Number Structure
  property_count: 2
  slug: transfer-booking-loyalty-number-structure
- name: Transfer Booking Name Structure
  property_count: 4
  slug: transfer-booking-name-structure
- name: Transfer Booking Partner Info Structure
  property_count: 1
  slug: transfer-booking-partner-info-structure
- name: Transfer Booking Passenger Characteristics Structure
  property_count: 2
  slug: transfer-booking-passenger-characteristics-structure
- name: Transfer Booking Passenger Structure
  property_count: 0
  slug: transfer-booking-passenger-structure
- name: Transfer Booking Payment Structure
  property_count: 4
  slug: transfer-booking-payment-structure
- name: Transfer Booking Points And Cash Structure
  property_count: 1
  slug: transfer-booking-points-and-cash-structure
- name: Transfer Booking Quotation Structure
  property_count: 0
  slug: transfer-booking-quotation-structure
- name: Transfer Booking Seat Structure
  property_count: 3
  slug: transfer-booking-seat-structure
- name: Transfer Booking Service Provider Structure
  property_count: 8
  slug: transfer-booking-service-provider-structure
- name: Transfer Booking Stop Over Structure
  property_count: 3
  slug: transfer-booking-stop-over-structure
- name: Transfer Booking Tax Structure
  property_count: 0
  slug: transfer-booking-tax-structure
- name: Transfer Booking Transfer Order Structure
  property_count: 6
  slug: transfer-booking-transfer-order-structure
- name: Transfer Booking Transfer Reservation Structure
  property_count: 0
  slug: transfer-booking-transfer-reservation-structure
- name: Transfer Booking Transfer Structure
  property_count: 17
  slug: transfer-booking-transfer-structure
- name: Transfer Booking Transportation Type Structure
  property_count: 0
  slug: transfer-booking-transportation-type-structure
- name: Transfer Booking Travel Segment Location Structure
  property_count: 3
  slug: transfer-booking-travel-segment-location-structure
- name: Transfer Booking Travel Segment Structure
  property_count: 4
  slug: transfer-booking-travel-segment-structure
- name: Transfer Booking Vehicle Structure
  property_count: 6
  slug: transfer-booking-vehicle-structure
- name: Transfer Management Error_400 Structure
  property_count: 1
  slug: transfer-management-error_400-structure
- name: Transfer Management Error_401 Structure
  property_count: 1
  slug: transfer-management-error_401-structure
- name: Transfer Management Error_404 Structure
  property_count: 1
  slug: transfer-management-error_404-structure
- name: Transfer Management Error_500 Structure
  property_count: 1
  slug: transfer-management-error_500-structure
- name: Transfer Management Issue Structure
  property_count: 5
  slug: transfer-management-issue-structure
- name: Transfer Management Transfer Cancellation Structure
  property_count: 2
  slug: transfer-management-transfer-cancellation-structure
jsonld:
- class_count: 45
  name: Amadeus Flight Create Orders Context
  property_count: 123
  slug: amadeus-flight-create-orders-context
- class_count: 46
  name: Amadeus Flight Order Management Context
  property_count: 126
  slug: amadeus-flight-order-management-context
- class_count: 1
  name: Amadeus Hotel Booking Address Context
  property_count: 5
  slug: amadeus-hotel-booking-address-context
- class_count: 1
  name: Amadeus Hotel Booking Arrival Context
  property_count: 4
  slug: amadeus-hotel-booking-arrival-context
- class_count: 1
  name: Amadeus Hotel Booking Create Context
  property_count: 4
  slug: amadeus-hotel-booking-create-context
- class_count: 1
  name: Amadeus Hotel Booking Errors Context
  property_count: 1
  slug: amadeus-hotel-booking-errors-context
- class_count: 2
  name: Amadeus Hotel Booking Guest Context
  property_count: 6
  slug: amadeus-hotel-booking-guest-context
- class_count: 1
  name: Amadeus Hotel Booking Guests Context
  property_count: 2
  slug: amadeus-hotel-booking-guests-context
- class_count: 6
  name: Amadeus Hotel Booking Hotel Context
  property_count: 29
  slug: amadeus-hotel-booking-hotel-context
- class_count: 2
  name: Amadeus Hotel Booking Hotel_ Context
  property_count: 2
  slug: amadeus-hotel-booking-hotel_-context
- class_count: 2
  name: Amadeus Hotel Booking Payment Context
  property_count: 5
  slug: amadeus-hotel-booking-payment-context
- class_count: 1
  name: Amadeus Hotel Booking Price Context
  property_count: 5
  slug: amadeus-hotel-booking-price-context
- class_count: 1
  name: Amadeus Hotel Booking Qualified Context
  property_count: 2
  slug: amadeus-hotel-booking-qualified-context
- class_count: 1
  name: Amadeus Hotel Booking Room Context
  property_count: 3
  slug: amadeus-hotel-booking-room-context
- class_count: 1
  name: Amadeus Hotel Booking Warning Context
  property_count: 7
  slug: amadeus-hotel-booking-warning-context
- class_count: 2
  name: Amadeus Transfer Booking Address Context
  property_count: 7
  slug: amadeus-transfer-booking-address-context
- class_count: 1
  name: Amadeus Transfer Booking Agency Context
  property_count: 1
  slug: amadeus-transfer-booking-agency-context
- class_count: 1
  name: Amadeus Transfer Booking Baggage Context
  property_count: 2
  slug: amadeus-transfer-booking-baggage-context
- class_count: 1
  name: Amadeus Transfer Booking Cancellation Context
  property_count: 7
  slug: amadeus-transfer-booking-cancellation-context
- class_count: 2
  name: Amadeus Transfer Booking Contact Context
  property_count: 1
  slug: amadeus-transfer-booking-contact-context
- class_count: 1
  name: Amadeus Transfer Booking Corporation Context
  property_count: 2
  slug: amadeus-transfer-booking-corporation-context
- class_count: 1
  name: Amadeus Transfer Booking Credit Context
  property_count: 5
  slug: amadeus-transfer-booking-credit-context
- class_count: 1
  name: Amadeus Transfer Booking Discount Context
  property_count: 2
  slug: amadeus-transfer-booking-discount-context
- class_count: 1
  name: Amadeus Transfer Booking Distance Context
  property_count: 2
  slug: amadeus-transfer-booking-distance-context
- class_count: 2
  name: Amadeus Transfer Booking Equipment Context
  property_count: 7
  slug: amadeus-transfer-booking-equipment-context
- class_count: 1
  name: Amadeus Transfer Booking Error_400 Context
  property_count: 1
  slug: amadeus-transfer-booking-error_400-context
- class_count: 1
  name: Amadeus Transfer Booking Error_401 Context
  property_count: 1
  slug: amadeus-transfer-booking-error_401-context
- class_count: 1
  name: Amadeus Transfer Booking Error_500 Context
  property_count: 1
  slug: amadeus-transfer-booking-error_500-context
- class_count: 2
  name: Amadeus Transfer Booking Extra Context
  property_count: 9
  slug: amadeus-transfer-booking-extra-context
- class_count: 0
  name: Amadeus Transfer Booking Fee Context
  property_count: 0
  slug: amadeus-transfer-booking-fee-context
- class_count: 1
  name: Amadeus Transfer Booking Issue Context
  property_count: 5
  slug: amadeus-transfer-booking-issue-context
- class_count: 2
  name: Amadeus Transfer Booking Location Context
  property_count: 5
  slug: amadeus-transfer-booking-location-context
- class_count: 1
  name: Amadeus Transfer Booking Loyalty Context
  property_count: 2
  slug: amadeus-transfer-booking-loyalty-context
- class_count: 1
  name: Amadeus Transfer Booking Name Context
  property_count: 4
  slug: amadeus-transfer-booking-name-context
- class_count: 1
  name: Amadeus Transfer Booking Partner Context
  property_count: 1
  slug: amadeus-transfer-booking-partner-context
- class_count: 1
  name: Amadeus Transfer Booking Passenger Context
  property_count: 2
  slug: amadeus-transfer-booking-passenger-context
- class_count: 1
  name: Amadeus Transfer Booking Payment Context
  property_count: 4
  slug: amadeus-transfer-booking-payment-context
- class_count: 1
  name: Amadeus Transfer Booking Points Context
  property_count: 1
  slug: amadeus-transfer-booking-points-context
- class_count: 0
  name: Amadeus Transfer Booking Quotation Context
  property_count: 0
  slug: amadeus-transfer-booking-quotation-context
- class_count: 1
  name: Amadeus Transfer Booking Seat Context
  property_count: 3
  slug: amadeus-transfer-booking-seat-context
- class_count: 2
  name: Amadeus Transfer Booking Service Context
  property_count: 7
  slug: amadeus-transfer-booking-service-context
- class_count: 1
  name: Amadeus Transfer Booking Stop Context
  property_count: 3
  slug: amadeus-transfer-booking-stop-context
- class_count: 0
  name: Amadeus Transfer Booking Tax Context
  property_count: 0
  slug: amadeus-transfer-booking-tax-context
- class_count: 2
  name: Amadeus Transfer Booking Transfer Context
  property_count: 23
  slug: amadeus-transfer-booking-transfer-context
- class_count: 0
  name: Amadeus Transfer Booking Transportation Context
  property_count: 0
  slug: amadeus-transfer-booking-transportation-context
- class_count: 2
  name: Amadeus Transfer Booking Travel Context
  property_count: 7
  slug: amadeus-transfer-booking-travel-context
- class_count: 2
  name: Amadeus Transfer Booking Vehicle Context
  property_count: 5
  slug: amadeus-transfer-booking-vehicle-context
- class_count: 1
  name: Amadeus Transfer Management Error_400 Context
  property_count: 1
  slug: amadeus-transfer-management-error_400-context
- class_count: 1
  name: Amadeus Transfer Management Error_401 Context
  property_count: 1
  slug: amadeus-transfer-management-error_401-context
- class_count: 1
  name: Amadeus Transfer Management Error_404 Context
  property_count: 1
  slug: amadeus-transfer-management-error_404-context
- class_count: 1
  name: Amadeus Transfer Management Error_500 Context
  property_count: 1
  slug: amadeus-transfer-management-error_500-context
- class_count: 1
  name: Amadeus Transfer Management Issue Context
  property_count: 5
  slug: amadeus-transfer-management-issue-context
- class_count: 1
  name: Amadeus Transfer Management Transfer Context
  property_count: 2
  slug: amadeus-transfer-management-transfer-context
layout: provider
mcp_servers:
- description: Candidate MCP server for the Amadeus reservation APIs, one tool per OpenAPI operation across the flight, hotel, and transfer booking/management APIs. Not published by Amadeus; provided as a design tar
  name: Amadeus Reservations MCP Server
  slug: amadeus-reservations-mcp-server
modified: '2026-06-20'
name: Amadeus Reservations
nav: Providers
network: true
overview: 'Amadeus Reservations publishes 1 API on the [APIs.io](https://apis.io/) network: Booking API. Tagged areas include Booking, Flights, Hotels, Reservations, and Travel.


  The Amadeus Reservations catalog on APIs.io includes 53 JSON-LD contexts and 2 Spectral governance rulesets.


  Amadeus Reservations'' developer surface includes developer portal, getting-started guide, authentication, signup flow, pricing, engineering blog, FAQ, and 21 more developer resources.'
random_paper: 19
rules:
- effective_rule_count: 5
  extends: []
  name: Amadeus Reservations API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: amadeus-reservations-jsonschema-spectral-rules
- effective_rule_count: 64
  extends:
  - spectral:oas
  name: Amadeus Reservations API Rules
  rule_count: 23
  severity_counts:
    error: 11
    hint: 0
    info: 2
    warn: 10
  slug: amadeus-reservations-spectral-rules
score:
  band: thin
  composite: 30.8
  delta: -0.9
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 45.5
    contract_quality: 48.8
    developer_ergonomics: 26.2
    discoverability: 75.9
    governance: 45.5
    operational_transparency: 2.6
  previous_composite: 31.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/amadeus-reservations/refs/heads/main/screenshots/amadeus-reservations-2026-07-25T195905.png
security:
- kind: domain-security
  name: Amadeus Reservations Domain Security
  slug: amadeus-reservations-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amadeus Reservations Vulnerability Disclosure
  slug: amadeus-reservations-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: amadeus-reservations
tags:
- Booking
- Flights
- Hotels
- Reservations
- Travel
use_cases:
- description: Power end-to-end booking flows for flights, hotels, and transfers on consumer-facing OTA platforms.
  name: Online Travel Agency Booking Engine
- description: Enable corporate travel managers to book and manage business travel including flights and hotel accommodations with policy compliance.
  name: Corporate Travel Management
- description: Integrate booking capabilities into mobile travel apps providing users with seamless reservation creation from search to confirmation.
  name: Travel App Integration
- description: Build complete multi-modal itineraries combining flight bookings with hotel reservations and ground transfers through unified API access.
  name: Itinerary Builder
- description: Enable AI-powered travel assistants to create and manage bookings on behalf of travelers through conversational interfaces.
  name: Travel Chatbot
website: https://developers.amadeus.com/
---
