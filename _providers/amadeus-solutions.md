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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 32.9
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Amadeus Solutions Agentic Access
  operation_count: 6
  slug: amadeus-solutions-agentic-access
  summary_line: 6 operations · 4 acting
api_count: 2
apis:
- description: The Display SeatMaps API from Amadeus Solutions — 1 operation(s) for display seatmaps.
  name: Amadeus Solutions Display SeatMaps API
  slug: amadeus-solutions-display-seatmaps-api
- description: The Shopping API from Amadeus Solutions — 3 operation(s) for shopping.
  name: Amadeus Solutions Shopping API
  slug: amadeus-solutions-shopping-api
artifact_total: 728
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Branded Fares Upsell Display SeatMaps API
  slug: open-amadeus-solutions-display-seatmaps-api
- collection_type: open
  name: Branded Fares Upsell Display SeatMaps Shopping API
  slug: open-amadeus-solutions-shopping-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/amadeus-solutions-branded-fares-upsell-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/amadeus-solutions-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/amadeus-solutions-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amadeus-solutions-domain-security.yml
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
  url: rules/amadeus-solutions-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/amadeus-solutions-vocabulary.yaml
- group: build
  title: ''
  type: Packages
  url: packages/amadeus-solutions-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/amadeus-solutions-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/amadeus-solutions-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/amadeus-solutions-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/amadeus-solutions-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/amadeus-solutions-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/amadeus-solutions-lifecycle.yml
created: '2024-01-01'
description: Amadeus is a leading technology partner for the global travel industry, providing technology solutions for airlines, airports, hotels, travel sellers, and corporate travel. The Amadeus platform includes a global distribution system (GDS), passenger service systems, airport operations, hospitality management, and a suite of APIs enabling developers to search, price, book, and manage travel across air, hotel, and ground transportation.
examples:
- key_count: 0
  name: Branded Fares Upsell Additional Service Type Example
  slug: branded-fares-upsell-additional-service-type-example
- key_count: 0
  name: Branded Fares Upsell Aircraft Entry Example
  slug: branded-fares-upsell-aircraft-entry-example
- key_count: 1
  name: Branded Fares Upsell Aircraft Equipment Example
  slug: branded-fares-upsell-aircraft-equipment-example
- key_count: 2
  name: Branded Fares Upsell Allotment Details Example
  slug: branded-fares-upsell-allotment-details-example
- key_count: 3
  name: Branded Fares Upsell Baggage Allowance Example
  slug: branded-fares-upsell-baggage-allowance-example
- key_count: 0
  name: Branded Fares Upsell Carrier Entry Example
  slug: branded-fares-upsell-carrier-entry-example
- key_count: 0
  name: Branded Fares Upsell Chargeable Checkd Bags Example
  slug: branded-fares-upsell-chargeable-checkd-bags-example
- key_count: 2
  name: Branded Fares Upsell Chargeable Seat Example
  slug: branded-fares-upsell-chargeable-seat-example
- key_count: 3
  name: Branded Fares Upsell Co2 Emission Example
  slug: branded-fares-upsell-co2-emission-example
- key_count: 2
  name: Branded Fares Upsell Collection_ Meta_ Upsell Example
  slug: branded-fares-upsell-collection_-meta_-upsell-example
- key_count: 0
  name: Branded Fares Upsell Currency Entry Example
  slug: branded-fares-upsell-currency-entry-example
- key_count: 4
  name: Branded Fares Upsell Dictionaries Example
  slug: branded-fares-upsell-dictionaries-example
- key_count: 1
  name: Branded Fares Upsell Error_400 Example
  slug: branded-fares-upsell-error_400-example
- key_count: 1
  name: Branded Fares Upsell Error_500 Example
  slug: branded-fares-upsell-error_500-example
- key_count: 0
  name: Branded Fares Upsell Extended_ Price Example
  slug: branded-fares-upsell-extended_-price-example
- key_count: 2
  name: Branded Fares Upsell Fee Example
  slug: branded-fares-upsell-fee-example
- key_count: 0
  name: Branded Fares Upsell Fee Type Example
  slug: branded-fares-upsell-fee-type-example
- key_count: 0
  name: Branded Fares Upsell Flight End Point Example
  slug: branded-fares-upsell-flight-end-point-example
- key_count: 16
  name: Branded Fares Upsell Flight Offer Example
  slug: branded-fares-upsell-flight-offer-example
- key_count: 0
  name: Branded Fares Upsell Flight Offer Source Example
  slug: branded-fares-upsell-flight-offer-source-example
- key_count: 3
  name: Branded Fares Upsell Flight Offer Upsell In Example
  slug: branded-fares-upsell-flight-offer-upsell-in-example
- key_count: 8
  name: Branded Fares Upsell Flight Segment Example
  slug: branded-fares-upsell-flight-segment-example
- key_count: 0
  name: Branded Fares Upsell Flight Stop Example
  slug: branded-fares-upsell-flight-stop-example
- key_count: 5
  name: Branded Fares Upsell Issue Example
  slug: branded-fares-upsell-issue-example
- key_count: 0
  name: Branded Fares Upsell Location Entry Example
  slug: branded-fares-upsell-location-entry-example
- key_count: 2
  name: Branded Fares Upsell Location Value Example
  slug: branded-fares-upsell-location-value-example
- key_count: 1
  name: Branded Fares Upsell Operating Flight Example
  slug: branded-fares-upsell-operating-flight-example
- key_count: 2
  name: Branded Fares Upsell Original Flight End Point Example
  slug: branded-fares-upsell-original-flight-end-point-example
- key_count: 2
  name: Branded Fares Upsell Original Flight Stop Example
  slug: branded-fares-upsell-original-flight-stop-example
- key_count: 0
  name: Branded Fares Upsell Payment Brand Example
  slug: branded-fares-upsell-payment-brand-example
- key_count: 3
  name: Branded Fares Upsell Payment Example
  slug: branded-fares-upsell-payment-example
- key_count: 6
  name: Branded Fares Upsell Price Example
  slug: branded-fares-upsell-price-example
- key_count: 0
  name: Branded Fares Upsell Pricing Options Fare Type Example
  slug: branded-fares-upsell-pricing-options-fare-type-example
- key_count: 0
  name: Branded Fares Upsell Segment Example
  slug: branded-fares-upsell-segment-example
- key_count: 0
  name: Branded Fares Upsell Service Name Example
  slug: branded-fares-upsell-service-name-example
- key_count: 0
  name: Branded Fares Upsell Slice Dice Indicator Example
  slug: branded-fares-upsell-slice-dice-indicator-example
- key_count: 2
  name: Branded Fares Upsell Tax Example
  slug: branded-fares-upsell-tax-example
- key_count: 0
  name: Branded Fares Upsell Travel Class Example
  slug: branded-fares-upsell-travel-class-example
- key_count: 0
  name: Branded Fares Upsell Traveler Pricing Fare Option Example
  slug: branded-fares-upsell-traveler-pricing-fare-option-example
- key_count: 0
  name: Branded Fares Upsell Traveler Type Example
  slug: branded-fares-upsell-traveler-type-example
- key_count: 0
  name: Flight Offers Price Additional Service Type Example
  slug: flight-offers-price-additional-service-type-example
- key_count: 6
  name: Flight Offers Price Address Example
  slug: flight-offers-price-address-example
- key_count: 0
  name: Flight Offers Price Aircraft Entry Example
  slug: flight-offers-price-aircraft-entry-example
- key_count: 1
  name: Flight Offers Price Aircraft Equipment Example
  slug: flight-offers-price-aircraft-equipment-example
- key_count: 2
  name: Flight Offers Price Allotment Details Example
  slug: flight-offers-price-allotment-details-example
- key_count: 3
  name: Flight Offers Price Baggage Allowance Example
  slug: flight-offers-price-baggage-allowance-example
- key_count: 0
  name: Flight Offers Price Bags Example
  slug: flight-offers-price-bags-example
- key_count: 3
  name: Flight Offers Price Base Name Example
  slug: flight-offers-price-base-name-example
- key_count: 0
  name: Flight Offers Price Carrier Entry Example
  slug: flight-offers-price-carrier-entry-example
- key_count: 0
  name: Flight Offers Price Chargeable Checkd Bags Example
  slug: flight-offers-price-chargeable-checkd-bags-example
- key_count: 2
  name: Flight Offers Price Chargeable Seat Example
  slug: flight-offers-price-chargeable-seat-example
- key_count: 3
  name: Flight Offers Price Co2 Emission Example
  slug: flight-offers-price-co2-emission-example
- key_count: 4
  name: Flight Offers Price Contact Dictionary Example
  slug: flight-offers-price-contact-dictionary-example
- key_count: 0
  name: Flight Offers Price Contact Example
  slug: flight-offers-price-contact-example
- key_count: 0
  name: Flight Offers Price Contact Purpose Example
  slug: flight-offers-price-contact-purpose-example
- key_count: 4
  name: Flight Offers Price Credit Card Fee Example
  slug: flight-offers-price-credit-card-fee-example
- key_count: 0
  name: Flight Offers Price Currency Entry Example
  slug: flight-offers-price-currency-entry-example
- key_count: 4
  name: Flight Offers Price Detailed Fare Rules Example
  slug: flight-offers-price-detailed-fare-rules-example
- key_count: 4
  name: Flight Offers Price Dictionaries Example
  slug: flight-offers-price-dictionaries-example
- key_count: 5
  name: Flight Offers Price Discount Example
  slug: flight-offers-price-discount-example
- key_count: 0
  name: Flight Offers Price Discount Traveler Type Example
  slug: flight-offers-price-discount-traveler-type-example
- key_count: 0
  name: Flight Offers Price Discount Type Example
  slug: flight-offers-price-discount-type-example
- key_count: 7
  name: Flight Offers Price Document Example
  slug: flight-offers-price-document-example
- key_count: 0
  name: Flight Offers Price Document Type Example
  slug: flight-offers-price-document-type-example
- key_count: 2
  name: Flight Offers Price Elementary Price Example
  slug: flight-offers-price-elementary-price-example
- key_count: 4
  name: Flight Offers Price Emergency Contact Example
  slug: flight-offers-price-emergency-contact-example
- key_count: 1
  name: Flight Offers Price Error_400 Example
  slug: flight-offers-price-error_400-example
- key_count: 1
  name: Flight Offers Price Error_500 Example
  slug: flight-offers-price-error_500-example
- key_count: 0
  name: Flight Offers Price Extended_ Price Example
  slug: flight-offers-price-extended_-price-example
- key_count: 2
  name: Flight Offers Price Fare Rules Example
  slug: flight-offers-price-fare-rules-example
- key_count: 2
  name: Flight Offers Price Fee Example
  slug: flight-offers-price-fee-example
- key_count: 0
  name: Flight Offers Price Fee Type Example
  slug: flight-offers-price-fee-type-example
- key_count: 0
  name: Flight Offers Price Flight End Point Example
  slug: flight-offers-price-flight-end-point-example
- key_count: 16
  name: Flight Offers Price Flight Offer Example
  slug: flight-offers-price-flight-offer-example
- key_count: 4
  name: Flight Offers Price Flight Offer Pricing In Example
  slug: flight-offers-price-flight-offer-pricing-in-example
- key_count: 3
  name: Flight Offers Price Flight Offer Pricing Out Example
  slug: flight-offers-price-flight-offer-pricing-out-example
- key_count: 0
  name: Flight Offers Price Flight Offer Source Example
  slug: flight-offers-price-flight-offer-source-example
- key_count: 8
  name: Flight Offers Price Flight Segment Example
  slug: flight-offers-price-flight-segment-example
- key_count: 0
  name: Flight Offers Price Flight Stop Example
  slug: flight-offers-price-flight-stop-example
- key_count: 0
  name: Flight Offers Price Identity Document Example
  slug: flight-offers-price-identity-document-example
- key_count: 5
  name: Flight Offers Price Issue Example
  slug: flight-offers-price-issue-example
- key_count: 0
  name: Flight Offers Price Location Entry Example
  slug: flight-offers-price-location-entry-example
- key_count: 2
  name: Flight Offers Price Location Value Example
  slug: flight-offers-price-location-value-example
- key_count: 2
  name: Flight Offers Price Loyalty Program Example
  slug: flight-offers-price-loyalty-program-example
- key_count: 0
  name: Flight Offers Price Name Example
  slug: flight-offers-price-name-example
- key_count: 1
  name: Flight Offers Price Operating Flight Example
  slug: flight-offers-price-operating-flight-example
- key_count: 2
  name: Flight Offers Price Original Flight End Point Example
  slug: flight-offers-price-original-flight-end-point-example
- key_count: 2
  name: Flight Offers Price Original Flight Stop Example
  slug: flight-offers-price-original-flight-stop-example
- key_count: 6
  name: Flight Offers Price Other Services Example
  slug: flight-offers-price-other-services-example
- key_count: 0
  name: Flight Offers Price Payment Brand Example
  slug: flight-offers-price-payment-brand-example
- key_count: 0
  name: Flight Offers Price Phone Device Type Example
  slug: flight-offers-price-phone-device-type-example
- key_count: 3
  name: Flight Offers Price Phone Example
  slug: flight-offers-price-phone-example
- key_count: 6
  name: Flight Offers Price Price Example
  slug: flight-offers-price-price-example
- key_count: 0
  name: Flight Offers Price Pricing Options Fare Type Example
  slug: flight-offers-price-pricing-options-fare-type-example
- key_count: 0
  name: Flight Offers Price Segment Example
  slug: flight-offers-price-segment-example
- key_count: 0
  name: Flight Offers Price Service Name Example
  slug: flight-offers-price-service-name-example
- key_count: 0
  name: Flight Offers Price Slice Dice Indicator Example
  slug: flight-offers-price-slice-dice-indicator-example
- key_count: 5
  name: Flight Offers Price Stakeholder Example
  slug: flight-offers-price-stakeholder-example
- key_count: 0
  name: Flight Offers Price Stakeholder Gender Example
  slug: flight-offers-price-stakeholder-gender-example
- key_count: 2
  name: Flight Offers Price Tax Example
  slug: flight-offers-price-tax-example
- key_count: 5
  name: Flight Offers Price Term And Condition Example
  slug: flight-offers-price-term-and-condition-example
- key_count: 0
  name: Flight Offers Price Travel Class Example
  slug: flight-offers-price-travel-class-example
- key_count: 0
  name: Flight Offers Price Traveler Example
  slug: flight-offers-price-traveler-example
- key_count: 0
  name: Flight Offers Price Traveler Pricing Fare Option Example
  slug: flight-offers-price-traveler-pricing-fare-option-example
- key_count: 0
  name: Flight Offers Price Traveler Type Example
  slug: flight-offers-price-traveler-type-example
- key_count: 0
  name: Flight Offers Search Additional Service Type Example
  slug: flight-offers-search-additional-service-type-example
- key_count: 0
  name: Flight Offers Search Aircraft Entry Example
  slug: flight-offers-search-aircraft-entry-example
- key_count: 1
  name: Flight Offers Search Aircraft Equipment Example
  slug: flight-offers-search-aircraft-equipment-example
- key_count: 2
  name: Flight Offers Search Allotment Details Example
  slug: flight-offers-search-allotment-details-example
- key_count: 3
  name: Flight Offers Search Baggage Allowance Example
  slug: flight-offers-search-baggage-allowance-example
- key_count: 2
  name: Flight Offers Search Cabin Restriction Example
  slug: flight-offers-search-cabin-restriction-example
- key_count: 0
  name: Flight Offers Search Carrier Entry Example
  slug: flight-offers-search-carrier-entry-example
- key_count: 3
  name: Flight Offers Search Carrier Restrictions Example
  slug: flight-offers-search-carrier-restrictions-example
- key_count: 0
  name: Flight Offers Search Chargeable Checkd Bags Example
  slug: flight-offers-search-chargeable-checkd-bags-example
- key_count: 2
  name: Flight Offers Search Chargeable Seat Example
  slug: flight-offers-search-chargeable-seat-example
- key_count: 3
  name: Flight Offers Search Co2 Emission Example
  slug: flight-offers-search-co2-emission-example
- key_count: 2
  name: Flight Offers Search Collection_ Meta Example
  slug: flight-offers-search-collection_-meta-example
- key_count: 2
  name: Flight Offers Search Collection_ Meta_ Link Example
  slug: flight-offers-search-collection_-meta_-link-example
- key_count: 4
  name: Flight Offers Search Connection Restriction Example
  slug: flight-offers-search-connection-restriction-example
- key_count: 0
  name: Flight Offers Search Coverage Example
  slug: flight-offers-search-coverage-example
- key_count: 0
  name: Flight Offers Search Currency Entry Example
  slug: flight-offers-search-currency-entry-example
- key_count: 0
  name: Flight Offers Search Date Time Range Example
  slug: flight-offers-search-date-time-range-example
- key_count: 2
  name: Flight Offers Search Date Time Type Example
  slug: flight-offers-search-date-time-type-example
- key_count: 4
  name: Flight Offers Search Dictionaries Example
  slug: flight-offers-search-dictionaries-example
- key_count: 1
  name: Flight Offers Search Error_400 Example
  slug: flight-offers-search-error_400-example
- key_count: 1
  name: Flight Offers Search Error_500 Example
  slug: flight-offers-search-error_500-example
- key_count: 4
  name: Flight Offers Search Extended Pricing Options Example
  slug: flight-offers-search-extended-pricing-options-example
- key_count: 0
  name: Flight Offers Search Extended_ Cabin Restriction Example
  slug: flight-offers-search-extended_-cabin-restriction-example
- key_count: 0
  name: Flight Offers Search Extended_ Price Example
  slug: flight-offers-search-extended_-price-example
- key_count: 4
  name: Flight Offers Search Extended_ Pricing Options Example
  slug: flight-offers-search-extended_-pricing-options-example
- key_count: 0
  name: Flight Offers Search Extended_ Traveler Info Example
  slug: flight-offers-search-extended_-traveler-info-example
- key_count: 2
  name: Flight Offers Search Fee Example
  slug: flight-offers-search-fee-example
- key_count: 0
  name: Flight Offers Search Fee Type Example
  slug: flight-offers-search-fee-type-example
- key_count: 0
  name: Flight Offers Search Flight End Point Example
  slug: flight-offers-search-flight-end-point-example
- key_count: 9
  name: Flight Offers Search Flight Filters Example
  slug: flight-offers-search-flight-filters-example
- key_count: 16
  name: Flight Offers Search Flight Offer Example
  slug: flight-offers-search-flight-offer-example
- key_count: 0
  name: Flight Offers Search Flight Offer Source Example
  slug: flight-offers-search-flight-offer-source-example
- key_count: 8
  name: Flight Offers Search Flight Segment Example
  slug: flight-offers-search-flight-segment-example
- key_count: 0
  name: Flight Offers Search Flight Stop Example
  slug: flight-offers-search-flight-stop-example
- key_count: 5
  name: Flight Offers Search Get Flight Offers Query Example
  slug: flight-offers-search-get-flight-offers-query-example
- key_count: 5
  name: Flight Offers Search Issue Example
  slug: flight-offers-search-issue-example
- key_count: 0
  name: Flight Offers Search Location Entry Example
  slug: flight-offers-search-location-entry-example
- key_count: 2
  name: Flight Offers Search Location Value Example
  slug: flight-offers-search-location-value-example
- key_count: 1
  name: Flight Offers Search Operating Flight Example
  slug: flight-offers-search-operating-flight-example
- key_count: 0
  name: Flight Offers Search Origin Destination Example
  slug: flight-offers-search-origin-destination-example
- key_count: 5
  name: Flight Offers Search Origin Destination Light Example
  slug: flight-offers-search-origin-destination-light-example
- key_count: 2
  name: Flight Offers Search Original Flight End Point Example
  slug: flight-offers-search-original-flight-end-point-example
- key_count: 2
  name: Flight Offers Search Original Flight Stop Example
  slug: flight-offers-search-original-flight-stop-example
- key_count: 6
  name: Flight Offers Search Price Example
  slug: flight-offers-search-price-example
- key_count: 0
  name: Flight Offers Search Pricing Options Fare Type Example
  slug: flight-offers-search-pricing-options-fare-type-example
- key_count: 9
  name: Flight Offers Search Search Criteria Example
  slug: flight-offers-search-search-criteria-example
- key_count: 0
  name: Flight Offers Search Segment Example
  slug: flight-offers-search-segment-example
- key_count: 0
  name: Flight Offers Search Service Name Example
  slug: flight-offers-search-service-name-example
- key_count: 0
  name: Flight Offers Search Slice Dice Indicator Example
  slug: flight-offers-search-slice-dice-indicator-example
- key_count: 2
  name: Flight Offers Search Tax Example
  slug: flight-offers-search-tax-example
- key_count: 0
  name: Flight Offers Search Travel Class Example
  slug: flight-offers-search-travel-class-example
- key_count: 3
  name: Flight Offers Search Traveler Info Example
  slug: flight-offers-search-traveler-info-example
- key_count: 0
  name: Flight Offers Search Traveler Pricing Fare Option Example
  slug: flight-offers-search-traveler-pricing-fare-option-example
- key_count: 0
  name: Flight Offers Search Traveler Type Example
  slug: flight-offers-search-traveler-type-example
- key_count: 0
  name: Seat Map Display Additional Service Type Example
  slug: seat-map-display-additional-service-type-example
- key_count: 9
  name: Seat Map Display Address Example
  slug: seat-map-display-address-example
- key_count: 6
  name: Seat Map Display Aircraft Cabin Amenities Example
  slug: seat-map-display-aircraft-cabin-amenities-example
- key_count: 0
  name: Seat Map Display Aircraft Cabin Amenities_ Beverage Example
  slug: seat-map-display-aircraft-cabin-amenities_-beverage-example
- key_count: 0
  name: Seat Map Display Aircraft Cabin Amenities_ Entertainment Example
  slug: seat-map-display-aircraft-cabin-amenities_-entertainment-example
- key_count: 0
  name: Seat Map Display Aircraft Cabin Amenities_ Food Example
  slug: seat-map-display-aircraft-cabin-amenities_-food-example
- key_count: 0
  name: Seat Map Display Aircraft Cabin Amenities_ Power Example
  slug: seat-map-display-aircraft-cabin-amenities_-power-example
- key_count: 0
  name: Seat Map Display Aircraft Cabin Amenities_ Wifi Example
  slug: seat-map-display-aircraft-cabin-amenities_-wifi-example
- key_count: 1
  name: Seat Map Display Aircraft Equipment Example
  slug: seat-map-display-aircraft-equipment-example
- key_count: 1
  name: Seat Map Display Amenity Example
  slug: seat-map-display-amenity-example
- key_count: 4
  name: Seat Map Display Amenity_ Media Example
  slug: seat-map-display-amenity_-media-example
- key_count: 5
  name: Seat Map Display Amenity_ Seat Example
  slug: seat-map-display-amenity_-seat-example
- key_count: 2
  name: Seat Map Display Available Seats Counter Example
  slug: seat-map-display-available-seats-counter-example
- key_count: 4
  name: Seat Map Display Baggage Allowance Example
  slug: seat-map-display-baggage-allowance-example
- key_count: 3
  name: Seat Map Display Base Name Example
  slug: seat-map-display-base-name-example
- key_count: 3
  name: Seat Map Display Co2 Emission Example
  slug: seat-map-display-co2-emission-example
- key_count: 2
  name: Seat Map Display Collection_ Meta Example
  slug: seat-map-display-collection_-meta-example
- key_count: 3
  name: Seat Map Display Contact Dictionary Example
  slug: seat-map-display-contact-dictionary-example
- key_count: 0
  name: Seat Map Display Contact Example
  slug: seat-map-display-contact-example
- key_count: 0
  name: Seat Map Display Contact Purpose Example
  slug: seat-map-display-contact-purpose-example
- key_count: 2
  name: Seat Map Display Coordinates Example
  slug: seat-map-display-coordinates-example
- key_count: 9
  name: Seat Map Display Deck Configuration Example
  slug: seat-map-display-deck-configuration-example
- key_count: 4
  name: Seat Map Display Deck Example
  slug: seat-map-display-deck-example
- key_count: 5
  name: Seat Map Display Discount Example
  slug: seat-map-display-discount-example
- key_count: 0
  name: Seat Map Display Discount Traveler Type Example
  slug: seat-map-display-discount-traveler-type-example
- key_count: 0
  name: Seat Map Display Discount Type Example
  slug: seat-map-display-discount-type-example
- key_count: 7
  name: Seat Map Display Document Example
  slug: seat-map-display-document-example
- key_count: 0
  name: Seat Map Display Document Type Example
  slug: seat-map-display-document-type-example
- key_count: 2
  name: Seat Map Display Elementary Price Example
  slug: seat-map-display-elementary-price-example
- key_count: 4
  name: Seat Map Display Emergency Contact Example
  slug: seat-map-display-emergency-contact-example
- key_count: 1
  name: Seat Map Display Error_400 Example
  slug: seat-map-display-error_400-example
- key_count: 1
  name: Seat Map Display Error_404 Example
  slug: seat-map-display-error_404-example
- key_count: 1
  name: Seat Map Display Error_500 Example
  slug: seat-map-display-error_500-example
- key_count: 0
  name: Seat Map Display Extended_ Price Example
  slug: seat-map-display-extended_-price-example
- key_count: 0
  name: Seat Map Display Facility Dictionary Example
  slug: seat-map-display-facility-dictionary-example
- key_count: 5
  name: Seat Map Display Facility Example
  slug: seat-map-display-facility-example
- key_count: 2
  name: Seat Map Display Fare Rules Example
  slug: seat-map-display-fare-rules-example
- key_count: 2
  name: Seat Map Display Fee Example
  slug: seat-map-display-fee-example
- key_count: 0
  name: Seat Map Display Fee Type Example
  slug: seat-map-display-fee-type-example
- key_count: 3
  name: Seat Map Display Flight End Point Example
  slug: seat-map-display-flight-end-point-example
- key_count: 16
  name: Seat Map Display Flight Offer Example
  slug: seat-map-display-flight-offer-example
- key_count: 0
  name: Seat Map Display Flight Offer Source Example
  slug: seat-map-display-flight-offer-source-example
- key_count: 8
  name: Seat Map Display Flight Segment Example
  slug: seat-map-display-flight-segment-example
- key_count: 5
  name: Seat Map Display Flight Stop Example
  slug: seat-map-display-flight-stop-example
- key_count: 0
  name: Seat Map Display Identity Document Example
  slug: seat-map-display-identity-document-example
- key_count: 5
  name: Seat Map Display Issue Example
  slug: seat-map-display-issue-example
- key_count: 3
  name: Seat Map Display Link Example
  slug: seat-map-display-link-example
- key_count: 0
  name: Seat Map Display Location Entry Example
  slug: seat-map-display-location-entry-example
- key_count: 2
  name: Seat Map Display Location Value Example
  slug: seat-map-display-location-value-example
- key_count: 2
  name: Seat Map Display Loyalty Program Example
  slug: seat-map-display-loyalty-program-example
- key_count: 0
  name: Seat Map Display Name Example
  slug: seat-map-display-name-example
- key_count: 3
  name: Seat Map Display Operating Flight Example
  slug: seat-map-display-operating-flight-example
- key_count: 0
  name: Seat Map Display Phone Device Type Example
  slug: seat-map-display-phone-device-type-example
- key_count: 9
  name: Seat Map Display Phone Example
  slug: seat-map-display-phone-example
- key_count: 5
  name: Seat Map Display Price Example
  slug: seat-map-display-price-example
- key_count: 0
  name: Seat Map Display Pricing Options Fare Type Example
  slug: seat-map-display-pricing-options-fare-type-example
- key_count: 2
  name: Seat Map Display Qualified Free Text Example
  slug: seat-map-display-qualified-free-text-example
- key_count: 0
  name: Seat Map Display Seat Characteristic Dictionary Example
  slug: seat-map-display-seat-characteristic-dictionary-example
- key_count: 5
  name: Seat Map Display Seat Example
  slug: seat-map-display-seat-example
- key_count: 15
  name: Seat Map Display Seat Map Example
  slug: seat-map-display-seat-map-example
- key_count: 3
  name: Seat Map Display Seatmap Traveler Pricing Example
  slug: seat-map-display-seatmap-traveler-pricing-example
- key_count: 0
  name: Seat Map Display Segment Example
  slug: seat-map-display-segment-example
- key_count: 0
  name: Seat Map Display Service Name Example
  slug: seat-map-display-service-name-example
- key_count: 0
  name: Seat Map Display Slice Dice Indicator Example
  slug: seat-map-display-slice-dice-indicator-example
- key_count: 5
  name: Seat Map Display Stakeholder Example
  slug: seat-map-display-stakeholder-example
- key_count: 0
  name: Seat Map Display Stakeholder Gender Example
  slug: seat-map-display-stakeholder-gender-example
- key_count: 2
  name: Seat Map Display Tax Example
  slug: seat-map-display-tax-example
- key_count: 5
  name: Seat Map Display Term And Condition Example
  slug: seat-map-display-term-and-condition-example
- key_count: 0
  name: Seat Map Display Travel Class Example
  slug: seat-map-display-travel-class-example
- key_count: 0
  name: Seat Map Display Traveler Example
  slug: seat-map-display-traveler-example
- key_count: 0
  name: Seat Map Display Traveler Pricing Fare Option Example
  slug: seat-map-display-traveler-pricing-fare-option-example
- key_count: 0
  name: Seat Map Display Traveler Type Example
  slug: seat-map-display-traveler-type-example
features:
- description: Access flight schedules and availability from over 400 airlines through a single integration with the Amadeus GDS.
  name: Global Flight Inventory
- description: Connect to airline NDC offers alongside traditional GDS content for a comprehensive view of available fares and ancillaries.
  name: NDC Content Support
- description: Display branded fare options with included services, restrictions, and price differences to enable informed purchase decisions.
  name: Branded Fares and Fare Families
- description: Access seat selection, baggage, meals, and other ancillary services through integrated APIs alongside fare shopping.
  name: Ancillary Services
- description: Confirm current pricing and availability before booking with the Flight Offers Price API to prevent pricing discrepancies.
  name: Real-Time Pricing
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/amadeus-solutions.png
integrations:
- description: Convert searched and priced flight offers into confirmed bookings using the Flight Create Orders API.
  name: Amadeus Flight Create Orders
- description: Combine flight search with hotel search to build complete trip planning experiences for travelers.
  name: Amadeus Hotel Search
- description: Enhance destination content alongside flight search with attractions, experiences, and activities data.
  name: Amadeus Points of Interest
- description: Add ground transportation options to flight itineraries through the Transfer Search API.
  name: Amadeus Transfer Search
- description: Integrate travel payments processing through Amadeus Outpayce for airline and OTA payment acceptance.
  name: Outpayce (Payments)
json_schemas:
- name: AdditionalServiceType
  property_count: 0
  slug: branded-fares-upsell-additional-service-type
- name: AircraftEntry
  property_count: 0
  slug: branded-fares-upsell-aircraft-entry
- name: AircraftEquipment
  property_count: 1
  slug: branded-fares-upsell-aircraft-equipment
- name: AllotmentDetails
  property_count: 2
  slug: branded-fares-upsell-allotment-details
- name: BaggageAllowance
  property_count: 3
  slug: branded-fares-upsell-baggage-allowance
- name: CarrierEntry
  property_count: 0
  slug: branded-fares-upsell-carrier-entry
- name: ChargeableCheckdBags
  property_count: 0
  slug: branded-fares-upsell-chargeable-checkd-bags
- name: ChargeableSeat
  property_count: 2
  slug: branded-fares-upsell-chargeable-seat
- name: Co2Emission
  property_count: 3
  slug: branded-fares-upsell-co2-emission
- name: Collection_Meta_Upsell
  property_count: 2
  slug: branded-fares-upsell-collection_-meta_-upsell
- name: CurrencyEntry
  property_count: 0
  slug: branded-fares-upsell-currency-entry
- name: Dictionaries
  property_count: 4
  slug: branded-fares-upsell-dictionaries
- name: Error_400
  property_count: 1
  slug: branded-fares-upsell-error_400
- name: Error_500
  property_count: 1
  slug: branded-fares-upsell-error_500
- name: Extended_Price
  property_count: 0
  slug: branded-fares-upsell-extended_-price
- name: Fee
  property_count: 2
  slug: branded-fares-upsell-fee
- name: FeeType
  property_count: 0
  slug: branded-fares-upsell-fee-type
- name: FlightEndPoint
  property_count: 0
  slug: branded-fares-upsell-flight-end-point
- name: FlightOffer
  property_count: 16
  slug: branded-fares-upsell-flight-offer
- name: FlightOfferSource
  property_count: 0
  slug: branded-fares-upsell-flight-offer-source
- name: FlightOfferUpsellIn
  property_count: 3
  slug: branded-fares-upsell-flight-offer-upsell-in
- name: FlightSegment
  property_count: 8
  slug: branded-fares-upsell-flight-segment
- name: FlightStop
  property_count: 0
  slug: branded-fares-upsell-flight-stop
- name: Issue
  property_count: 5
  slug: branded-fares-upsell-issue
- name: LocationEntry
  property_count: 0
  slug: branded-fares-upsell-location-entry
- name: LocationValue
  property_count: 2
  slug: branded-fares-upsell-location-value
- name: OperatingFlight
  property_count: 1
  slug: branded-fares-upsell-operating-flight
- name: OriginalFlightEndPoint
  property_count: 2
  slug: branded-fares-upsell-original-flight-end-point
- name: OriginalFlightStop
  property_count: 2
  slug: branded-fares-upsell-original-flight-stop
- name: PaymentBrand
  property_count: 0
  slug: branded-fares-upsell-payment-brand
- name: Payment
  property_count: 3
  slug: branded-fares-upsell-payment
- name: Price
  property_count: 6
  slug: branded-fares-upsell-price
- name: PricingOptionsFareType
  property_count: 0
  slug: branded-fares-upsell-pricing-options-fare-type
- name: Segment
  property_count: 0
  slug: branded-fares-upsell-segment
- name: ServiceName
  property_count: 0
  slug: branded-fares-upsell-service-name
- name: SliceDiceIndicator
  property_count: 0
  slug: branded-fares-upsell-slice-dice-indicator
- name: Tax
  property_count: 2
  slug: branded-fares-upsell-tax
- name: TravelClass
  property_count: 0
  slug: branded-fares-upsell-travel-class
- name: TravelerPricingFareOption
  property_count: 0
  slug: branded-fares-upsell-traveler-pricing-fare-option
- name: TravelerType
  property_count: 0
  slug: branded-fares-upsell-traveler-type
- name: AdditionalServiceType
  property_count: 0
  slug: flight-offers-price-additional-service-type
- name: Address
  property_count: 6
  slug: flight-offers-price-address
- name: AircraftEntry
  property_count: 0
  slug: flight-offers-price-aircraft-entry
- name: AircraftEquipment
  property_count: 1
  slug: flight-offers-price-aircraft-equipment
- name: AllotmentDetails
  property_count: 2
  slug: flight-offers-price-allotment-details
- name: BaggageAllowance
  property_count: 3
  slug: flight-offers-price-baggage-allowance
- name: Bags
  property_count: 0
  slug: flight-offers-price-bags
- name: BaseName
  property_count: 3
  slug: flight-offers-price-base-name
- name: CarrierEntry
  property_count: 0
  slug: flight-offers-price-carrier-entry
- name: ChargeableCheckdBags
  property_count: 0
  slug: flight-offers-price-chargeable-checkd-bags
- name: ChargeableSeat
  property_count: 2
  slug: flight-offers-price-chargeable-seat
- name: Co2Emission
  property_count: 3
  slug: flight-offers-price-co2-emission
- name: ContactDictionary
  property_count: 4
  slug: flight-offers-price-contact-dictionary
- name: ContactPurpose
  property_count: 0
  slug: flight-offers-price-contact-purpose
- name: Contact
  property_count: 0
  slug: flight-offers-price-contact
- name: CreditCardFee
  property_count: 4
  slug: flight-offers-price-credit-card-fee
- name: CurrencyEntry
  property_count: 0
  slug: flight-offers-price-currency-entry
- name: DetailedFareRules
  property_count: 4
  slug: flight-offers-price-detailed-fare-rules
- name: Dictionaries
  property_count: 4
  slug: flight-offers-price-dictionaries
- name: Discount
  property_count: 5
  slug: flight-offers-price-discount
- name: DiscountTravelerType
  property_count: 0
  slug: flight-offers-price-discount-traveler-type
- name: DiscountType
  property_count: 0
  slug: flight-offers-price-discount-type
- name: Document
  property_count: 7
  slug: flight-offers-price-document
- name: DocumentType
  property_count: 0
  slug: flight-offers-price-document-type
- name: ElementaryPrice
  property_count: 2
  slug: flight-offers-price-elementary-price
- name: EmergencyContact
  property_count: 4
  slug: flight-offers-price-emergency-contact
- name: Error_400
  property_count: 1
  slug: flight-offers-price-error_400
- name: Error_500
  property_count: 1
  slug: flight-offers-price-error_500
- name: Extended_Price
  property_count: 0
  slug: flight-offers-price-extended_-price
- name: FareRules
  property_count: 2
  slug: flight-offers-price-fare-rules
- name: Fee
  property_count: 2
  slug: flight-offers-price-fee
- name: FeeType
  property_count: 0
  slug: flight-offers-price-fee-type
- name: FlightEndPoint
  property_count: 0
  slug: flight-offers-price-flight-end-point
- name: FlightOfferPricingIn
  property_count: 4
  slug: flight-offers-price-flight-offer-pricing-in
- name: FlightOfferPricingOut
  property_count: 3
  slug: flight-offers-price-flight-offer-pricing-out
- name: FlightOffer
  property_count: 16
  slug: flight-offers-price-flight-offer
- name: FlightOfferSource
  property_count: 0
  slug: flight-offers-price-flight-offer-source
- name: FlightSegment
  property_count: 8
  slug: flight-offers-price-flight-segment
- name: FlightStop
  property_count: 0
  slug: flight-offers-price-flight-stop
- name: IdentityDocument
  property_count: 0
  slug: flight-offers-price-identity-document
- name: Issue
  property_count: 5
  slug: flight-offers-price-issue
- name: LocationEntry
  property_count: 0
  slug: flight-offers-price-location-entry
- name: LocationValue
  property_count: 2
  slug: flight-offers-price-location-value
- name: LoyaltyProgram
  property_count: 2
  slug: flight-offers-price-loyalty-program
- name: Name
  property_count: 0
  slug: flight-offers-price-name
- name: OperatingFlight
  property_count: 1
  slug: flight-offers-price-operating-flight
- name: OriginalFlightEndPoint
  property_count: 2
  slug: flight-offers-price-original-flight-end-point
- name: OriginalFlightStop
  property_count: 2
  slug: flight-offers-price-original-flight-stop
- name: OtherServices
  property_count: 6
  slug: flight-offers-price-other-services
- name: PaymentBrand
  property_count: 0
  slug: flight-offers-price-payment-brand
- name: PhoneDeviceType
  property_count: 0
  slug: flight-offers-price-phone-device-type
- name: Phone
  property_count: 3
  slug: flight-offers-price-phone
- name: Price
  property_count: 6
  slug: flight-offers-price-price
- name: PricingOptionsFareType
  property_count: 0
  slug: flight-offers-price-pricing-options-fare-type
- name: Segment
  property_count: 0
  slug: flight-offers-price-segment
- name: ServiceName
  property_count: 0
  slug: flight-offers-price-service-name
- name: SliceDiceIndicator
  property_count: 0
  slug: flight-offers-price-slice-dice-indicator
- name: StakeholderGender
  property_count: 0
  slug: flight-offers-price-stakeholder-gender
- name: Stakeholder
  property_count: 5
  slug: flight-offers-price-stakeholder
- name: Tax
  property_count: 2
  slug: flight-offers-price-tax
- name: TermAndCondition
  property_count: 5
  slug: flight-offers-price-term-and-condition
- name: TravelClass
  property_count: 0
  slug: flight-offers-price-travel-class
- name: TravelerPricingFareOption
  property_count: 0
  slug: flight-offers-price-traveler-pricing-fare-option
- name: Traveler
  property_count: 0
  slug: flight-offers-price-traveler
- name: TravelerType
  property_count: 0
  slug: flight-offers-price-traveler-type
- name: AdditionalServiceType
  property_count: 0
  slug: flight-offers-search-additional-service-type
- name: AircraftEntry
  property_count: 0
  slug: flight-offers-search-aircraft-entry
- name: AircraftEquipment
  property_count: 1
  slug: flight-offers-search-aircraft-equipment
- name: AllotmentDetails
  property_count: 2
  slug: flight-offers-search-allotment-details
- name: BaggageAllowance
  property_count: 3
  slug: flight-offers-search-baggage-allowance
- name: CabinRestriction
  property_count: 2
  slug: flight-offers-search-cabin-restriction
- name: CarrierEntry
  property_count: 0
  slug: flight-offers-search-carrier-entry
- name: CarrierRestrictions
  property_count: 3
  slug: flight-offers-search-carrier-restrictions
- name: ChargeableCheckdBags
  property_count: 0
  slug: flight-offers-search-chargeable-checkd-bags
- name: ChargeableSeat
  property_count: 2
  slug: flight-offers-search-chargeable-seat
- name: Co2Emission
  property_count: 3
  slug: flight-offers-search-co2-emission
- name: Collection_Meta
  property_count: 2
  slug: flight-offers-search-collection_-meta
- name: Collection_Meta_Link
  property_count: 2
  slug: flight-offers-search-collection_-meta_-link
- name: ConnectionRestriction
  property_count: 4
  slug: flight-offers-search-connection-restriction
- name: Coverage
  property_count: 0
  slug: flight-offers-search-coverage
- name: CurrencyEntry
  property_count: 0
  slug: flight-offers-search-currency-entry
- name: DateTimeRange
  property_count: 0
  slug: flight-offers-search-date-time-range
- name: DateTimeType
  property_count: 2
  slug: flight-offers-search-date-time-type
- name: Dictionaries
  property_count: 4
  slug: flight-offers-search-dictionaries
- name: Error_400
  property_count: 1
  slug: flight-offers-search-error_400
- name: Error_500
  property_count: 1
  slug: flight-offers-search-error_500
- name: ExtendedPricingOptions
  property_count: 4
  slug: flight-offers-search-extended-pricing-options
- name: Extended_CabinRestriction
  property_count: 0
  slug: flight-offers-search-extended_-cabin-restriction
- name: Extended_Price
  property_count: 0
  slug: flight-offers-search-extended_-price
- name: Extended_PricingOptions
  property_count: 4
  slug: flight-offers-search-extended_-pricing-options
- name: Extended_TravelerInfo
  property_count: 0
  slug: flight-offers-search-extended_-traveler-info
- name: Fee
  property_count: 2
  slug: flight-offers-search-fee
- name: FeeType
  property_count: 0
  slug: flight-offers-search-fee-type
- name: FlightEndPoint
  property_count: 0
  slug: flight-offers-search-flight-end-point
- name: FlightFilters
  property_count: 9
  slug: flight-offers-search-flight-filters
- name: FlightOffer
  property_count: 16
  slug: flight-offers-search-flight-offer
- name: FlightOfferSource
  property_count: 0
  slug: flight-offers-search-flight-offer-source
- name: FlightSegment
  property_count: 8
  slug: flight-offers-search-flight-segment
- name: FlightStop
  property_count: 0
  slug: flight-offers-search-flight-stop
- name: GetFlightOffersQuery
  property_count: 5
  slug: flight-offers-search-get-flight-offers-query
- name: Issue
  property_count: 5
  slug: flight-offers-search-issue
- name: LocationEntry
  property_count: 0
  slug: flight-offers-search-location-entry
- name: LocationValue
  property_count: 2
  slug: flight-offers-search-location-value
- name: OperatingFlight
  property_count: 1
  slug: flight-offers-search-operating-flight
- name: OriginDestinationLight
  property_count: 5
  slug: flight-offers-search-origin-destination-light
- name: OriginDestination
  property_count: 0
  slug: flight-offers-search-origin-destination
- name: OriginalFlightEndPoint
  property_count: 2
  slug: flight-offers-search-original-flight-end-point
- name: OriginalFlightStop
  property_count: 2
  slug: flight-offers-search-original-flight-stop
- name: Price
  property_count: 6
  slug: flight-offers-search-price
- name: PricingOptionsFareType
  property_count: 0
  slug: flight-offers-search-pricing-options-fare-type
- name: SearchCriteria
  property_count: 9
  slug: flight-offers-search-search-criteria
- name: Segment
  property_count: 0
  slug: flight-offers-search-segment
- name: ServiceName
  property_count: 0
  slug: flight-offers-search-service-name
- name: SliceDiceIndicator
  property_count: 0
  slug: flight-offers-search-slice-dice-indicator
- name: Tax
  property_count: 2
  slug: flight-offers-search-tax
- name: TravelClass
  property_count: 0
  slug: flight-offers-search-travel-class
- name: TravelerInfo
  property_count: 3
  slug: flight-offers-search-traveler-info
- name: TravelerPricingFareOption
  property_count: 0
  slug: flight-offers-search-traveler-pricing-fare-option
- name: TravelerType
  property_count: 0
  slug: flight-offers-search-traveler-type
- name: AdditionalServiceType
  property_count: 0
  slug: seat-map-display-additional-service-type
- name: Address
  property_count: 9
  slug: seat-map-display-address
- name: AircraftCabinAmenities
  property_count: 6
  slug: seat-map-display-aircraft-cabin-amenities
- name: AircraftCabinAmenities_Beverage
  property_count: 0
  slug: seat-map-display-aircraft-cabin-amenities_-beverage
- name: AircraftCabinAmenities_Entertainment
  property_count: 0
  slug: seat-map-display-aircraft-cabin-amenities_-entertainment
- name: AircraftCabinAmenities_Food
  property_count: 0
  slug: seat-map-display-aircraft-cabin-amenities_-food
- name: AircraftCabinAmenities_Power
  property_count: 0
  slug: seat-map-display-aircraft-cabin-amenities_-power
- name: AircraftCabinAmenities_Wifi
  property_count: 0
  slug: seat-map-display-aircraft-cabin-amenities_-wifi
- name: AircraftEquipment
  property_count: 1
  slug: seat-map-display-aircraft-equipment
- name: Amenity
  property_count: 1
  slug: seat-map-display-amenity
- name: Amenity_Media
  property_count: 4
  slug: seat-map-display-amenity_-media
- name: Amenity_Seat
  property_count: 5
  slug: seat-map-display-amenity_-seat
- name: AvailableSeatsCounter
  property_count: 2
  slug: seat-map-display-available-seats-counter
- name: BaggageAllowance
  property_count: 4
  slug: seat-map-display-baggage-allowance
- name: BaseName
  property_count: 3
  slug: seat-map-display-base-name
- name: Co2Emission
  property_count: 3
  slug: seat-map-display-co2-emission
- name: Collection_Meta
  property_count: 2
  slug: seat-map-display-collection_-meta
- name: ContactDictionary
  property_count: 3
  slug: seat-map-display-contact-dictionary
- name: ContactPurpose
  property_count: 0
  slug: seat-map-display-contact-purpose
- name: Contact
  property_count: 0
  slug: seat-map-display-contact
- name: Coordinates
  property_count: 2
  slug: seat-map-display-coordinates
- name: DeckConfiguration
  property_count: 9
  slug: seat-map-display-deck-configuration
- name: Deck
  property_count: 4
  slug: seat-map-display-deck
- name: Discount
  property_count: 5
  slug: seat-map-display-discount
- name: DiscountTravelerType
  property_count: 0
  slug: seat-map-display-discount-traveler-type
- name: DiscountType
  property_count: 0
  slug: seat-map-display-discount-type
- name: Document
  property_count: 7
  slug: seat-map-display-document
- name: DocumentType
  property_count: 0
  slug: seat-map-display-document-type
- name: ElementaryPrice
  property_count: 2
  slug: seat-map-display-elementary-price
- name: EmergencyContact
  property_count: 4
  slug: seat-map-display-emergency-contact
- name: Error_400
  property_count: 1
  slug: seat-map-display-error_400
- name: Error_404
  property_count: 1
  slug: seat-map-display-error_404
- name: Error_500
  property_count: 1
  slug: seat-map-display-error_500
- name: Extended_Price
  property_count: 0
  slug: seat-map-display-extended_-price
- name: FacilityDictionary
  property_count: 0
  slug: seat-map-display-facility-dictionary
- name: Facility
  property_count: 5
  slug: seat-map-display-facility
- name: FareRules
  property_count: 2
  slug: seat-map-display-fare-rules
- name: Fee
  property_count: 2
  slug: seat-map-display-fee
- name: FeeType
  property_count: 0
  slug: seat-map-display-fee-type
- name: FlightEndPoint
  property_count: 3
  slug: seat-map-display-flight-end-point
- name: FlightOffer
  property_count: 16
  slug: seat-map-display-flight-offer
- name: FlightOfferSource
  property_count: 0
  slug: seat-map-display-flight-offer-source
- name: FlightSegment
  property_count: 8
  slug: seat-map-display-flight-segment
- name: FlightStop
  property_count: 5
  slug: seat-map-display-flight-stop
- name: IdentityDocument
  property_count: 0
  slug: seat-map-display-identity-document
- name: Issue
  property_count: 5
  slug: seat-map-display-issue
- name: Link
  property_count: 3
  slug: seat-map-display-link
- name: LocationEntry
  property_count: 0
  slug: seat-map-display-location-entry
- name: LocationValue
  property_count: 2
  slug: seat-map-display-location-value
- name: LoyaltyProgram
  property_count: 2
  slug: seat-map-display-loyalty-program
- name: Name
  property_count: 0
  slug: seat-map-display-name
- name: OperatingFlight
  property_count: 3
  slug: seat-map-display-operating-flight
- name: PhoneDeviceType
  property_count: 0
  slug: seat-map-display-phone-device-type
- name: Phone
  property_count: 9
  slug: seat-map-display-phone
- name: Price
  property_count: 5
  slug: seat-map-display-price
- name: PricingOptionsFareType
  property_count: 0
  slug: seat-map-display-pricing-options-fare-type
- name: QualifiedFreeText
  property_count: 2
  slug: seat-map-display-qualified-free-text
- name: SeatCharacteristicDictionary
  property_count: 0
  slug: seat-map-display-seat-characteristic-dictionary
- name: SeatMap
  property_count: 15
  slug: seat-map-display-seat-map
- name: Seat
  property_count: 5
  slug: seat-map-display-seat
- name: SeatmapTravelerPricing
  property_count: 3
  slug: seat-map-display-seatmap-traveler-pricing
- name: Segment
  property_count: 0
  slug: seat-map-display-segment
- name: ServiceName
  property_count: 0
  slug: seat-map-display-service-name
- name: SliceDiceIndicator
  property_count: 0
  slug: seat-map-display-slice-dice-indicator
- name: StakeholderGender
  property_count: 0
  slug: seat-map-display-stakeholder-gender
- name: Stakeholder
  property_count: 5
  slug: seat-map-display-stakeholder
- name: Tax
  property_count: 2
  slug: seat-map-display-tax
- name: TermAndCondition
  property_count: 5
  slug: seat-map-display-term-and-condition
- name: TravelClass
  property_count: 0
  slug: seat-map-display-travel-class
- name: TravelerPricingFareOption
  property_count: 0
  slug: seat-map-display-traveler-pricing-fare-option
- name: Traveler
  property_count: 0
  slug: seat-map-display-traveler
- name: TravelerType
  property_count: 0
  slug: seat-map-display-traveler-type
json_structures:
- name: Branded Fares Upsell Additional Service Type Structure
  property_count: 0
  slug: branded-fares-upsell-additional-service-type-structure
- name: Branded Fares Upsell Aircraft Entry Structure
  property_count: 0
  slug: branded-fares-upsell-aircraft-entry-structure
- name: Branded Fares Upsell Aircraft Equipment Structure
  property_count: 1
  slug: branded-fares-upsell-aircraft-equipment-structure
- name: Branded Fares Upsell Allotment Details Structure
  property_count: 2
  slug: branded-fares-upsell-allotment-details-structure
- name: Branded Fares Upsell Baggage Allowance Structure
  property_count: 3
  slug: branded-fares-upsell-baggage-allowance-structure
- name: Branded Fares Upsell Carrier Entry Structure
  property_count: 0
  slug: branded-fares-upsell-carrier-entry-structure
- name: Branded Fares Upsell Chargeable Checkd Bags Structure
  property_count: 0
  slug: branded-fares-upsell-chargeable-checkd-bags-structure
- name: Branded Fares Upsell Chargeable Seat Structure
  property_count: 2
  slug: branded-fares-upsell-chargeable-seat-structure
- name: Branded Fares Upsell Co2 Emission Structure
  property_count: 3
  slug: branded-fares-upsell-co2-emission-structure
- name: Branded Fares Upsell Collection_ Meta_ Upsell Structure
  property_count: 2
  slug: branded-fares-upsell-collection_-meta_-upsell-structure
- name: Branded Fares Upsell Currency Entry Structure
  property_count: 0
  slug: branded-fares-upsell-currency-entry-structure
- name: Branded Fares Upsell Dictionaries Structure
  property_count: 4
  slug: branded-fares-upsell-dictionaries-structure
- name: Branded Fares Upsell Error_400 Structure
  property_count: 1
  slug: branded-fares-upsell-error_400-structure
- name: Branded Fares Upsell Error_500 Structure
  property_count: 1
  slug: branded-fares-upsell-error_500-structure
- name: Branded Fares Upsell Extended_ Price Structure
  property_count: 0
  slug: branded-fares-upsell-extended_-price-structure
- name: Branded Fares Upsell Fee Structure
  property_count: 2
  slug: branded-fares-upsell-fee-structure
- name: Branded Fares Upsell Fee Type Structure
  property_count: 0
  slug: branded-fares-upsell-fee-type-structure
- name: Branded Fares Upsell Flight End Point Structure
  property_count: 0
  slug: branded-fares-upsell-flight-end-point-structure
- name: Branded Fares Upsell Flight Offer Source Structure
  property_count: 0
  slug: branded-fares-upsell-flight-offer-source-structure
- name: Branded Fares Upsell Flight Offer Structure
  property_count: 16
  slug: branded-fares-upsell-flight-offer-structure
- name: Branded Fares Upsell Flight Offer Upsell In Structure
  property_count: 3
  slug: branded-fares-upsell-flight-offer-upsell-in-structure
- name: Branded Fares Upsell Flight Segment Structure
  property_count: 8
  slug: branded-fares-upsell-flight-segment-structure
- name: Branded Fares Upsell Flight Stop Structure
  property_count: 0
  slug: branded-fares-upsell-flight-stop-structure
- name: Branded Fares Upsell Issue Structure
  property_count: 5
  slug: branded-fares-upsell-issue-structure
- name: Branded Fares Upsell Location Entry Structure
  property_count: 0
  slug: branded-fares-upsell-location-entry-structure
- name: Branded Fares Upsell Location Value Structure
  property_count: 2
  slug: branded-fares-upsell-location-value-structure
- name: Branded Fares Upsell Operating Flight Structure
  property_count: 1
  slug: branded-fares-upsell-operating-flight-structure
- name: Branded Fares Upsell Original Flight End Point Structure
  property_count: 2
  slug: branded-fares-upsell-original-flight-end-point-structure
- name: Branded Fares Upsell Original Flight Stop Structure
  property_count: 2
  slug: branded-fares-upsell-original-flight-stop-structure
- name: Branded Fares Upsell Payment Brand Structure
  property_count: 0
  slug: branded-fares-upsell-payment-brand-structure
- name: Branded Fares Upsell Payment Structure
  property_count: 3
  slug: branded-fares-upsell-payment-structure
- name: Branded Fares Upsell Price Structure
  property_count: 6
  slug: branded-fares-upsell-price-structure
- name: Branded Fares Upsell Pricing Options Fare Type Structure
  property_count: 0
  slug: branded-fares-upsell-pricing-options-fare-type-structure
- name: Branded Fares Upsell Segment Structure
  property_count: 0
  slug: branded-fares-upsell-segment-structure
- name: Branded Fares Upsell Service Name Structure
  property_count: 0
  slug: branded-fares-upsell-service-name-structure
- name: Branded Fares Upsell Slice Dice Indicator Structure
  property_count: 0
  slug: branded-fares-upsell-slice-dice-indicator-structure
- name: Branded Fares Upsell Tax Structure
  property_count: 2
  slug: branded-fares-upsell-tax-structure
- name: Branded Fares Upsell Travel Class Structure
  property_count: 0
  slug: branded-fares-upsell-travel-class-structure
- name: Branded Fares Upsell Traveler Pricing Fare Option Structure
  property_count: 0
  slug: branded-fares-upsell-traveler-pricing-fare-option-structure
- name: Branded Fares Upsell Traveler Type Structure
  property_count: 0
  slug: branded-fares-upsell-traveler-type-structure
- name: Flight Offers Price Additional Service Type Structure
  property_count: 0
  slug: flight-offers-price-additional-service-type-structure
- name: Flight Offers Price Address Structure
  property_count: 6
  slug: flight-offers-price-address-structure
- name: Flight Offers Price Aircraft Entry Structure
  property_count: 0
  slug: flight-offers-price-aircraft-entry-structure
- name: Flight Offers Price Aircraft Equipment Structure
  property_count: 1
  slug: flight-offers-price-aircraft-equipment-structure
- name: Flight Offers Price Allotment Details Structure
  property_count: 2
  slug: flight-offers-price-allotment-details-structure
- name: Flight Offers Price Baggage Allowance Structure
  property_count: 3
  slug: flight-offers-price-baggage-allowance-structure
- name: Flight Offers Price Bags Structure
  property_count: 0
  slug: flight-offers-price-bags-structure
- name: Flight Offers Price Base Name Structure
  property_count: 3
  slug: flight-offers-price-base-name-structure
- name: Flight Offers Price Carrier Entry Structure
  property_count: 0
  slug: flight-offers-price-carrier-entry-structure
- name: Flight Offers Price Chargeable Checkd Bags Structure
  property_count: 0
  slug: flight-offers-price-chargeable-checkd-bags-structure
- name: Flight Offers Price Chargeable Seat Structure
  property_count: 2
  slug: flight-offers-price-chargeable-seat-structure
- name: Flight Offers Price Co2 Emission Structure
  property_count: 3
  slug: flight-offers-price-co2-emission-structure
- name: Flight Offers Price Contact Dictionary Structure
  property_count: 4
  slug: flight-offers-price-contact-dictionary-structure
- name: Flight Offers Price Contact Purpose Structure
  property_count: 0
  slug: flight-offers-price-contact-purpose-structure
- name: Flight Offers Price Contact Structure
  property_count: 0
  slug: flight-offers-price-contact-structure
- name: Flight Offers Price Credit Card Fee Structure
  property_count: 4
  slug: flight-offers-price-credit-card-fee-structure
- name: Flight Offers Price Currency Entry Structure
  property_count: 0
  slug: flight-offers-price-currency-entry-structure
- name: Flight Offers Price Detailed Fare Rules Structure
  property_count: 4
  slug: flight-offers-price-detailed-fare-rules-structure
- name: Flight Offers Price Dictionaries Structure
  property_count: 4
  slug: flight-offers-price-dictionaries-structure
- name: Flight Offers Price Discount Structure
  property_count: 5
  slug: flight-offers-price-discount-structure
- name: Flight Offers Price Discount Traveler Type Structure
  property_count: 0
  slug: flight-offers-price-discount-traveler-type-structure
- name: Flight Offers Price Discount Type Structure
  property_count: 0
  slug: flight-offers-price-discount-type-structure
- name: Flight Offers Price Document Structure
  property_count: 7
  slug: flight-offers-price-document-structure
- name: Flight Offers Price Document Type Structure
  property_count: 0
  slug: flight-offers-price-document-type-structure
- name: Flight Offers Price Elementary Price Structure
  property_count: 2
  slug: flight-offers-price-elementary-price-structure
- name: Flight Offers Price Emergency Contact Structure
  property_count: 4
  slug: flight-offers-price-emergency-contact-structure
- name: Flight Offers Price Error_400 Structure
  property_count: 1
  slug: flight-offers-price-error_400-structure
- name: Flight Offers Price Error_500 Structure
  property_count: 1
  slug: flight-offers-price-error_500-structure
- name: Flight Offers Price Extended_ Price Structure
  property_count: 0
  slug: flight-offers-price-extended_-price-structure
- name: Flight Offers Price Fare Rules Structure
  property_count: 2
  slug: flight-offers-price-fare-rules-structure
- name: Flight Offers Price Fee Structure
  property_count: 2
  slug: flight-offers-price-fee-structure
- name: Flight Offers Price Fee Type Structure
  property_count: 0
  slug: flight-offers-price-fee-type-structure
- name: Flight Offers Price Flight End Point Structure
  property_count: 0
  slug: flight-offers-price-flight-end-point-structure
- name: Flight Offers Price Flight Offer Pricing In Structure
  property_count: 4
  slug: flight-offers-price-flight-offer-pricing-in-structure
- name: Flight Offers Price Flight Offer Pricing Out Structure
  property_count: 3
  slug: flight-offers-price-flight-offer-pricing-out-structure
- name: Flight Offers Price Flight Offer Source Structure
  property_count: 0
  slug: flight-offers-price-flight-offer-source-structure
- name: Flight Offers Price Flight Offer Structure
  property_count: 16
  slug: flight-offers-price-flight-offer-structure
- name: Flight Offers Price Flight Segment Structure
  property_count: 8
  slug: flight-offers-price-flight-segment-structure
- name: Flight Offers Price Flight Stop Structure
  property_count: 0
  slug: flight-offers-price-flight-stop-structure
- name: Flight Offers Price Identity Document Structure
  property_count: 0
  slug: flight-offers-price-identity-document-structure
- name: Flight Offers Price Issue Structure
  property_count: 5
  slug: flight-offers-price-issue-structure
- name: Flight Offers Price Location Entry Structure
  property_count: 0
  slug: flight-offers-price-location-entry-structure
- name: Flight Offers Price Location Value Structure
  property_count: 2
  slug: flight-offers-price-location-value-structure
- name: Flight Offers Price Loyalty Program Structure
  property_count: 2
  slug: flight-offers-price-loyalty-program-structure
- name: Flight Offers Price Name Structure
  property_count: 0
  slug: flight-offers-price-name-structure
- name: Flight Offers Price Operating Flight Structure
  property_count: 1
  slug: flight-offers-price-operating-flight-structure
- name: Flight Offers Price Original Flight End Point Structure
  property_count: 2
  slug: flight-offers-price-original-flight-end-point-structure
- name: Flight Offers Price Original Flight Stop Structure
  property_count: 2
  slug: flight-offers-price-original-flight-stop-structure
- name: Flight Offers Price Other Services Structure
  property_count: 6
  slug: flight-offers-price-other-services-structure
- name: Flight Offers Price Payment Brand Structure
  property_count: 0
  slug: flight-offers-price-payment-brand-structure
- name: Flight Offers Price Phone Device Type Structure
  property_count: 0
  slug: flight-offers-price-phone-device-type-structure
- name: Flight Offers Price Phone Structure
  property_count: 3
  slug: flight-offers-price-phone-structure
- name: Flight Offers Price Price Structure
  property_count: 6
  slug: flight-offers-price-price-structure
- name: Flight Offers Price Pricing Options Fare Type Structure
  property_count: 0
  slug: flight-offers-price-pricing-options-fare-type-structure
- name: Flight Offers Price Segment Structure
  property_count: 0
  slug: flight-offers-price-segment-structure
- name: Flight Offers Price Service Name Structure
  property_count: 0
  slug: flight-offers-price-service-name-structure
- name: Flight Offers Price Slice Dice Indicator Structure
  property_count: 0
  slug: flight-offers-price-slice-dice-indicator-structure
- name: Flight Offers Price Stakeholder Gender Structure
  property_count: 0
  slug: flight-offers-price-stakeholder-gender-structure
- name: Flight Offers Price Stakeholder Structure
  property_count: 5
  slug: flight-offers-price-stakeholder-structure
- name: Flight Offers Price Tax Structure
  property_count: 2
  slug: flight-offers-price-tax-structure
- name: Flight Offers Price Term And Condition Structure
  property_count: 5
  slug: flight-offers-price-term-and-condition-structure
- name: Flight Offers Price Travel Class Structure
  property_count: 0
  slug: flight-offers-price-travel-class-structure
- name: Flight Offers Price Traveler Pricing Fare Option Structure
  property_count: 0
  slug: flight-offers-price-traveler-pricing-fare-option-structure
- name: Flight Offers Price Traveler Structure
  property_count: 0
  slug: flight-offers-price-traveler-structure
- name: Flight Offers Price Traveler Type Structure
  property_count: 0
  slug: flight-offers-price-traveler-type-structure
- name: Flight Offers Search Additional Service Type Structure
  property_count: 0
  slug: flight-offers-search-additional-service-type-structure
- name: Flight Offers Search Aircraft Entry Structure
  property_count: 0
  slug: flight-offers-search-aircraft-entry-structure
- name: Flight Offers Search Aircraft Equipment Structure
  property_count: 1
  slug: flight-offers-search-aircraft-equipment-structure
- name: Flight Offers Search Allotment Details Structure
  property_count: 2
  slug: flight-offers-search-allotment-details-structure
- name: Flight Offers Search Baggage Allowance Structure
  property_count: 3
  slug: flight-offers-search-baggage-allowance-structure
- name: Flight Offers Search Cabin Restriction Structure
  property_count: 2
  slug: flight-offers-search-cabin-restriction-structure
- name: Flight Offers Search Carrier Entry Structure
  property_count: 0
  slug: flight-offers-search-carrier-entry-structure
- name: Flight Offers Search Carrier Restrictions Structure
  property_count: 3
  slug: flight-offers-search-carrier-restrictions-structure
- name: Flight Offers Search Chargeable Checkd Bags Structure
  property_count: 0
  slug: flight-offers-search-chargeable-checkd-bags-structure
- name: Flight Offers Search Chargeable Seat Structure
  property_count: 2
  slug: flight-offers-search-chargeable-seat-structure
- name: Flight Offers Search Co2 Emission Structure
  property_count: 3
  slug: flight-offers-search-co2-emission-structure
- name: Flight Offers Search Collection_ Meta Structure
  property_count: 2
  slug: flight-offers-search-collection_-meta-structure
- name: Flight Offers Search Collection_ Meta_ Link Structure
  property_count: 2
  slug: flight-offers-search-collection_-meta_-link-structure
- name: Flight Offers Search Connection Restriction Structure
  property_count: 4
  slug: flight-offers-search-connection-restriction-structure
- name: Flight Offers Search Coverage Structure
  property_count: 0
  slug: flight-offers-search-coverage-structure
- name: Flight Offers Search Currency Entry Structure
  property_count: 0
  slug: flight-offers-search-currency-entry-structure
- name: Flight Offers Search Date Time Range Structure
  property_count: 0
  slug: flight-offers-search-date-time-range-structure
- name: Flight Offers Search Date Time Type Structure
  property_count: 2
  slug: flight-offers-search-date-time-type-structure
- name: Flight Offers Search Dictionaries Structure
  property_count: 4
  slug: flight-offers-search-dictionaries-structure
- name: Flight Offers Search Error_400 Structure
  property_count: 1
  slug: flight-offers-search-error_400-structure
- name: Flight Offers Search Error_500 Structure
  property_count: 1
  slug: flight-offers-search-error_500-structure
- name: Flight Offers Search Extended Pricing Options Structure
  property_count: 4
  slug: flight-offers-search-extended-pricing-options-structure
- name: Flight Offers Search Extended_ Cabin Restriction Structure
  property_count: 0
  slug: flight-offers-search-extended_-cabin-restriction-structure
- name: Flight Offers Search Extended_ Price Structure
  property_count: 0
  slug: flight-offers-search-extended_-price-structure
- name: Flight Offers Search Extended_ Pricing Options Structure
  property_count: 4
  slug: flight-offers-search-extended_-pricing-options-structure
- name: Flight Offers Search Extended_ Traveler Info Structure
  property_count: 0
  slug: flight-offers-search-extended_-traveler-info-structure
- name: Flight Offers Search Fee Structure
  property_count: 2
  slug: flight-offers-search-fee-structure
- name: Flight Offers Search Fee Type Structure
  property_count: 0
  slug: flight-offers-search-fee-type-structure
- name: Flight Offers Search Flight End Point Structure
  property_count: 0
  slug: flight-offers-search-flight-end-point-structure
- name: Flight Offers Search Flight Filters Structure
  property_count: 9
  slug: flight-offers-search-flight-filters-structure
- name: Flight Offers Search Flight Offer Source Structure
  property_count: 0
  slug: flight-offers-search-flight-offer-source-structure
- name: Flight Offers Search Flight Offer Structure
  property_count: 16
  slug: flight-offers-search-flight-offer-structure
- name: Flight Offers Search Flight Segment Structure
  property_count: 8
  slug: flight-offers-search-flight-segment-structure
- name: Flight Offers Search Flight Stop Structure
  property_count: 0
  slug: flight-offers-search-flight-stop-structure
- name: Flight Offers Search Get Flight Offers Query Structure
  property_count: 5
  slug: flight-offers-search-get-flight-offers-query-structure
- name: Flight Offers Search Issue Structure
  property_count: 5
  slug: flight-offers-search-issue-structure
- name: Flight Offers Search Location Entry Structure
  property_count: 0
  slug: flight-offers-search-location-entry-structure
- name: Flight Offers Search Location Value Structure
  property_count: 2
  slug: flight-offers-search-location-value-structure
- name: Flight Offers Search Operating Flight Structure
  property_count: 1
  slug: flight-offers-search-operating-flight-structure
- name: Flight Offers Search Origin Destination Light Structure
  property_count: 5
  slug: flight-offers-search-origin-destination-light-structure
- name: Flight Offers Search Origin Destination Structure
  property_count: 0
  slug: flight-offers-search-origin-destination-structure
- name: Flight Offers Search Original Flight End Point Structure
  property_count: 2
  slug: flight-offers-search-original-flight-end-point-structure
- name: Flight Offers Search Original Flight Stop Structure
  property_count: 2
  slug: flight-offers-search-original-flight-stop-structure
- name: Flight Offers Search Price Structure
  property_count: 6
  slug: flight-offers-search-price-structure
- name: Flight Offers Search Pricing Options Fare Type Structure
  property_count: 0
  slug: flight-offers-search-pricing-options-fare-type-structure
- name: Flight Offers Search Search Criteria Structure
  property_count: 9
  slug: flight-offers-search-search-criteria-structure
- name: Flight Offers Search Segment Structure
  property_count: 0
  slug: flight-offers-search-segment-structure
- name: Flight Offers Search Service Name Structure
  property_count: 0
  slug: flight-offers-search-service-name-structure
- name: Flight Offers Search Slice Dice Indicator Structure
  property_count: 0
  slug: flight-offers-search-slice-dice-indicator-structure
- name: Flight Offers Search Tax Structure
  property_count: 2
  slug: flight-offers-search-tax-structure
- name: Flight Offers Search Travel Class Structure
  property_count: 0
  slug: flight-offers-search-travel-class-structure
- name: Flight Offers Search Traveler Info Structure
  property_count: 3
  slug: flight-offers-search-traveler-info-structure
- name: Flight Offers Search Traveler Pricing Fare Option Structure
  property_count: 0
  slug: flight-offers-search-traveler-pricing-fare-option-structure
- name: Flight Offers Search Traveler Type Structure
  property_count: 0
  slug: flight-offers-search-traveler-type-structure
- name: Seat Map Display Additional Service Type Structure
  property_count: 0
  slug: seat-map-display-additional-service-type-structure
- name: Seat Map Display Address Structure
  property_count: 9
  slug: seat-map-display-address-structure
- name: Seat Map Display Aircraft Cabin Amenities Structure
  property_count: 6
  slug: seat-map-display-aircraft-cabin-amenities-structure
- name: Seat Map Display Aircraft Cabin Amenities_ Beverage Structure
  property_count: 0
  slug: seat-map-display-aircraft-cabin-amenities_-beverage-structure
- name: Seat Map Display Aircraft Cabin Amenities_ Entertainment Structure
  property_count: 0
  slug: seat-map-display-aircraft-cabin-amenities_-entertainment-structure
- name: Seat Map Display Aircraft Cabin Amenities_ Food Structure
  property_count: 0
  slug: seat-map-display-aircraft-cabin-amenities_-food-structure
- name: Seat Map Display Aircraft Cabin Amenities_ Power Structure
  property_count: 0
  slug: seat-map-display-aircraft-cabin-amenities_-power-structure
- name: Seat Map Display Aircraft Cabin Amenities_ Wifi Structure
  property_count: 0
  slug: seat-map-display-aircraft-cabin-amenities_-wifi-structure
- name: Seat Map Display Aircraft Equipment Structure
  property_count: 1
  slug: seat-map-display-aircraft-equipment-structure
- name: Seat Map Display Amenity Structure
  property_count: 1
  slug: seat-map-display-amenity-structure
- name: Seat Map Display Amenity_ Media Structure
  property_count: 4
  slug: seat-map-display-amenity_-media-structure
- name: Seat Map Display Amenity_ Seat Structure
  property_count: 5
  slug: seat-map-display-amenity_-seat-structure
- name: Seat Map Display Available Seats Counter Structure
  property_count: 2
  slug: seat-map-display-available-seats-counter-structure
- name: Seat Map Display Baggage Allowance Structure
  property_count: 4
  slug: seat-map-display-baggage-allowance-structure
- name: Seat Map Display Base Name Structure
  property_count: 3
  slug: seat-map-display-base-name-structure
- name: Seat Map Display Co2 Emission Structure
  property_count: 3
  slug: seat-map-display-co2-emission-structure
- name: Seat Map Display Collection_ Meta Structure
  property_count: 2
  slug: seat-map-display-collection_-meta-structure
- name: Seat Map Display Contact Dictionary Structure
  property_count: 3
  slug: seat-map-display-contact-dictionary-structure
- name: Seat Map Display Contact Purpose Structure
  property_count: 0
  slug: seat-map-display-contact-purpose-structure
- name: Seat Map Display Contact Structure
  property_count: 0
  slug: seat-map-display-contact-structure
- name: Seat Map Display Coordinates Structure
  property_count: 2
  slug: seat-map-display-coordinates-structure
- name: Seat Map Display Deck Configuration Structure
  property_count: 9
  slug: seat-map-display-deck-configuration-structure
- name: Seat Map Display Deck Structure
  property_count: 4
  slug: seat-map-display-deck-structure
- name: Seat Map Display Discount Structure
  property_count: 5
  slug: seat-map-display-discount-structure
- name: Seat Map Display Discount Traveler Type Structure
  property_count: 0
  slug: seat-map-display-discount-traveler-type-structure
- name: Seat Map Display Discount Type Structure
  property_count: 0
  slug: seat-map-display-discount-type-structure
- name: Seat Map Display Document Structure
  property_count: 7
  slug: seat-map-display-document-structure
- name: Seat Map Display Document Type Structure
  property_count: 0
  slug: seat-map-display-document-type-structure
- name: Seat Map Display Elementary Price Structure
  property_count: 2
  slug: seat-map-display-elementary-price-structure
- name: Seat Map Display Emergency Contact Structure
  property_count: 4
  slug: seat-map-display-emergency-contact-structure
- name: Seat Map Display Error_400 Structure
  property_count: 1
  slug: seat-map-display-error_400-structure
- name: Seat Map Display Error_404 Structure
  property_count: 1
  slug: seat-map-display-error_404-structure
- name: Seat Map Display Error_500 Structure
  property_count: 1
  slug: seat-map-display-error_500-structure
- name: Seat Map Display Extended_ Price Structure
  property_count: 0
  slug: seat-map-display-extended_-price-structure
- name: Seat Map Display Facility Dictionary Structure
  property_count: 0
  slug: seat-map-display-facility-dictionary-structure
- name: Seat Map Display Facility Structure
  property_count: 5
  slug: seat-map-display-facility-structure
- name: Seat Map Display Fare Rules Structure
  property_count: 2
  slug: seat-map-display-fare-rules-structure
- name: Seat Map Display Fee Structure
  property_count: 2
  slug: seat-map-display-fee-structure
- name: Seat Map Display Fee Type Structure
  property_count: 0
  slug: seat-map-display-fee-type-structure
- name: Seat Map Display Flight End Point Structure
  property_count: 3
  slug: seat-map-display-flight-end-point-structure
- name: Seat Map Display Flight Offer Source Structure
  property_count: 0
  slug: seat-map-display-flight-offer-source-structure
- name: Seat Map Display Flight Offer Structure
  property_count: 16
  slug: seat-map-display-flight-offer-structure
- name: Seat Map Display Flight Segment Structure
  property_count: 8
  slug: seat-map-display-flight-segment-structure
- name: Seat Map Display Flight Stop Structure
  property_count: 5
  slug: seat-map-display-flight-stop-structure
- name: Seat Map Display Identity Document Structure
  property_count: 0
  slug: seat-map-display-identity-document-structure
- name: Seat Map Display Issue Structure
  property_count: 5
  slug: seat-map-display-issue-structure
- name: Seat Map Display Link Structure
  property_count: 3
  slug: seat-map-display-link-structure
- name: Seat Map Display Location Entry Structure
  property_count: 0
  slug: seat-map-display-location-entry-structure
- name: Seat Map Display Location Value Structure
  property_count: 2
  slug: seat-map-display-location-value-structure
- name: Seat Map Display Loyalty Program Structure
  property_count: 2
  slug: seat-map-display-loyalty-program-structure
- name: Seat Map Display Name Structure
  property_count: 0
  slug: seat-map-display-name-structure
- name: Seat Map Display Operating Flight Structure
  property_count: 3
  slug: seat-map-display-operating-flight-structure
- name: Seat Map Display Phone Device Type Structure
  property_count: 0
  slug: seat-map-display-phone-device-type-structure
- name: Seat Map Display Phone Structure
  property_count: 9
  slug: seat-map-display-phone-structure
- name: Seat Map Display Price Structure
  property_count: 5
  slug: seat-map-display-price-structure
- name: Seat Map Display Pricing Options Fare Type Structure
  property_count: 0
  slug: seat-map-display-pricing-options-fare-type-structure
- name: Seat Map Display Qualified Free Text Structure
  property_count: 2
  slug: seat-map-display-qualified-free-text-structure
- name: Seat Map Display Seat Characteristic Dictionary Structure
  property_count: 0
  slug: seat-map-display-seat-characteristic-dictionary-structure
- name: Seat Map Display Seat Map Structure
  property_count: 15
  slug: seat-map-display-seat-map-structure
- name: Seat Map Display Seat Structure
  property_count: 5
  slug: seat-map-display-seat-structure
- name: Seat Map Display Seatmap Traveler Pricing Structure
  property_count: 3
  slug: seat-map-display-seatmap-traveler-pricing-structure
- name: Seat Map Display Segment Structure
  property_count: 0
  slug: seat-map-display-segment-structure
- name: Seat Map Display Service Name Structure
  property_count: 0
  slug: seat-map-display-service-name-structure
- name: Seat Map Display Slice Dice Indicator Structure
  property_count: 0
  slug: seat-map-display-slice-dice-indicator-structure
- name: Seat Map Display Stakeholder Gender Structure
  property_count: 0
  slug: seat-map-display-stakeholder-gender-structure
- name: Seat Map Display Stakeholder Structure
  property_count: 5
  slug: seat-map-display-stakeholder-structure
- name: Seat Map Display Tax Structure
  property_count: 2
  slug: seat-map-display-tax-structure
- name: Seat Map Display Term And Condition Structure
  property_count: 5
  slug: seat-map-display-term-and-condition-structure
- name: Seat Map Display Travel Class Structure
  property_count: 0
  slug: seat-map-display-travel-class-structure
- name: Seat Map Display Traveler Pricing Fare Option Structure
  property_count: 0
  slug: seat-map-display-traveler-pricing-fare-option-structure
- name: Seat Map Display Traveler Structure
  property_count: 0
  slug: seat-map-display-traveler-structure
- name: Seat Map Display Traveler Type Structure
  property_count: 0
  slug: seat-map-display-traveler-type-structure
jsonld:
- class_count: 22
  name: Amadeus Branded Fares Upsell Context
  property_count: 56
  slug: amadeus-branded-fares-upsell-context
- class_count: 37
  name: Amadeus Flight Offers Price Context
  property_count: 98
  slug: amadeus-flight-offers-price-context
- class_count: 32
  name: Amadeus Flight Offers Search Context
  property_count: 94
  slug: amadeus-flight-offers-search-context
- class_count: 48
  name: Amadeus Seat Map Display Context
  property_count: 136
  slug: amadeus-seat-map-display-context
layout: provider
mcp_servers:
- description: ''
  name: amadeus-solutions-mcp.yml
  slug: amadeus-solutions-mcpyml
modified: '2026-06-20'
name: Amadeus Solutions
nav: Providers
network: true
overview: 'Amadeus Solutions publishes 2 APIs on the [APIs.io](https://apis.io/) network: Display SeatMaps API and Shopping API. Tagged areas include Airlines, Booking, Flights, GDS, and Hotels.


  The Amadeus Solutions catalog on APIs.io includes 4 JSON-LD contexts and 2 Spectral governance rulesets.


  Amadeus Solutions'' developer surface includes developer portal, getting-started guide, authentication, signup flow, pricing, engineering blog, FAQ, and 21 more developer resources.'
random_paper: 1
rules:
- effective_rule_count: 5
  extends: []
  name: Amadeus Solutions API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: amadeus-solutions-jsonschema-spectral-rules
- effective_rule_count: 60
  extends:
  - spectral:oas
  name: Amadeus Solutions API Rules
  rule_count: 19
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 8
  slug: amadeus-solutions-spectral-rules
score:
  band: thin
  composite: 32.6
  delta: -21.9
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 41.7
    contract_quality: 53.1
    developer_ergonomics: 26.2
    discoverability: 87.0
    governance: 41.7
    operational_transparency: 2.6
  previous_composite: 54.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/amadeus-solutions/refs/heads/main/screenshots/amadeus-solutions-2026-07-25T195907.png
security:
- kind: domain-security
  name: Amadeus Solutions Domain Security
  slug: amadeus-solutions-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amadeus Solutions Vulnerability Disclosure
  slug: amadeus-solutions-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: amadeus-solutions
solutions:
- description: Next-generation airline retailing platform enabling offer and order management for airlines pursuing NDC-based retailing strategies.
  name: Amadeus Nevio (Airline Retailing)
- description: Core passenger service system for full-service carriers providing reservations, inventory management, and departure control.
  name: Amadeus Altéa (Passenger Service System)
- description: Distribution platform for travel agencies providing GDS access, NDC content, and LCC integrations through a unified API.
  name: Amadeus Selling Platform Connect
- description: Corporate travel and expense management platform integrated with Microsoft Teams and major enterprise collaboration tools.
  name: Amadeus Cytric (Corporate Travel)
- description: Airport operations technology including baggage, passenger experience, ground handling, and border control solutions.
  name: Amadeus Airport IT
tags:
- Airlines
- Booking
- Flights
- GDS
- Hotels
- Travel
- Travel Technology
use_cases:
- description: Build complete flight shopping experiences searching, pricing, and booking flights across hundreds of airlines through a unified API.
  name: Flight Search and Booking Engine
- description: Power airline direct channels with offer creation, branded fares, seat maps, and ancillary upsell capabilities.
  name: Airline Retailing Platform
- description: Enable policy-compliant flight shopping for corporate travelers with fare filtering, approval workflows, and reporting.
  name: Corporate Travel Management
- description: Aggregate flight offers for price comparison across airlines with detailed fare family and service information.
  name: Travel Metasearch
- description: Enable conversational travel assistants to search and compare flights using natural language queries.
  name: AI Travel Assistant
website: https://developers.amadeus.com/
---
