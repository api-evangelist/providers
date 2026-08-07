---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 44.1
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Quandoo Agentic Access
  operation_count: 24
  slug: quandoo-agentic-access
  summary_line: 24 operations · 6 acting
api_count: 10
apis:
- description: The Availabilities API from Quandoo — 2 operation(s) for availabilities.
  name: Quandoo Availabilities API
  slug: quandoo-availabilities-api
- description: The Customers API from Quandoo — 3 operation(s) for customers.
  name: Quandoo Customers API
  slug: quandoo-customers-api
- description: The Merchants API from Quandoo — 5 operation(s) for merchants.
  name: Quandoo Merchants API
  slug: quandoo-merchants-api
- description: The Reservation Enquiries API from Quandoo — 3 operation(s) for reservation enquiries.
  name: Quandoo Reservation Enquiries API
  slug: quandoo-reservation-enquiries-api
- description: The Reservation Settings API from Quandoo — 1 operation(s) for reservation settings.
  name: Quandoo Reservation Settings API
  slug: quandoo-reservation-settings-api
- description: The Reservations API from Quandoo — 2 operation(s) for reservations.
  name: Quandoo Reservations API
  slug: quandoo-reservations-api
- description: The Reservations Tags API from Quandoo — 1 operation(s) for reservations tags.
  name: Quandoo Reservations Tags API
  slug: quandoo-reservations-tags-api
- description: The Reviews API from Quandoo — 1 operation(s) for reviews.
  name: Quandoo Reviews API
  slug: quandoo-reviews-api
- description: The Status API from Quandoo — 1 operation(s) for status.
  name: Quandoo Status API
  slug: quandoo-status-api
- description: The Validations API from Quandoo — 1 operation(s) for validations.
  name: Quandoo Validations API
  slug: quandoo-validations-api
artifact_total: 224
collections:
- collection_type: postman
  name: Quandoo Public Partner Availabilities API
  slug: postman-quandoo-availabilities-api
- collection_type: postman
  name: Quandoo Public Partner Availabilities Customers API
  slug: postman-quandoo-customers-api
- collection_type: postman
  name: Quandoo Public Partner Availabilities Merchants API
  slug: postman-quandoo-merchants-api
- collection_type: postman
  name: Quandoo Public Partner Availabilities Reservation Enquiries API
  slug: postman-quandoo-reservation-enquiries-api
- collection_type: postman
  name: Quandoo Public Partner Availabilities Reservation Settings API
  slug: postman-quandoo-reservation-settings-api
- collection_type: postman
  name: Quandoo Public Partner Availabilities Reservations API
  slug: postman-quandoo-reservations-api
- collection_type: postman
  name: Quandoo Public Partner Availabilities Reservations Tags API
  slug: postman-quandoo-reservations-tags-api
- collection_type: postman
  name: Quandoo Public Partner Availabilities Reviews API
  slug: postman-quandoo-reviews-api
- collection_type: postman
  name: Quandoo Public Partner Availabilities Status API
  slug: postman-quandoo-status-api
- collection_type: postman
  name: Quandoo Public Partner Availabilities Validations API
  slug: postman-quandoo-validations-api
- collection_type: open
  name: Quandoo Public Partner API
  slug: open-quandoo-public-partner-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/quandoo/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/quandoo-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/quandoo-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/quandoo-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/quandoo-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.quandoo.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.quandoo.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.quandoo.com/interactive-api/
- group: operate
  title: ''
  type: Support
  url: mailto:developers@quandoo.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/quandoo
- group: design
  title: ''
  type: SpectralRules
  url: rules/quandoo-public-partner-api-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/quandoo-vocabulary.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/quandoo-context.jsonld
- group: commercial
  title: ''
  type: Plans
  url: plans/quandoo-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/quandoo-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/quandoo-finops.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://restaurants.quandoo.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://restaurants.quandoo.com/en-gb/terms-and-conditions
created: '2026-06-02'
description: 'Quandoo is a restaurant reservations marketplace that connects diners with thousands of restaurants and gives merchants table, reservation, and reputation management tooling. Quandoo publishes the Public Partner API, a multi-purpose REST API (host public-api.prod.quandoo.com, authenticated with the X-Quandoo-AuthToken header) that lets partners check merchant availability, search merchants, read merchant reservation and enquiry settings, create and manage reservations and reservation enquiries, manage customers and reviews, handle reservation tags, and validate phone numbers. Reservation and enquiry creation is idempotent via agent-supplied unique identifiers, and returns HTTP 409 when a slot is no longer bookable. Quandoo offers widget, portal, discovery-widget, and direct integration paths plus an interactive API explorer. Note: Quandoo announced in March 2026 that it will wind down operations, with new bookings ending 30 September 2026; this profile documents the still-live
  Public Partner API as published.'
examples:
- key_count: 1
  name: Quandoo Public Partner Api Agent Tracking Example
  slug: quandoo-public-partner-api-agent-tracking-example
- key_count: 3
  name: Quandoo Public Partner Api Area Dto Example
  slug: quandoo-public-partner-api-area-dto-example
- key_count: 2
  name: Quandoo Public Partner Api Chain Dto Example
  slug: quandoo-public-partner-api-chain-dto-example
- key_count: 3
  name: Quandoo Public Partner Api Changed Review Dto Example
  slug: quandoo-public-partner-api-changed-review-dto-example
- key_count: 2
  name: Quandoo Public Partner Api Coordinates Dto Example
  slug: quandoo-public-partner-api-coordinates-dto-example
- key_count: 3
  name: Quandoo Public Partner Api Create Review Dto Example
  slug: quandoo-public-partner-api-create-review-dto-example
- key_count: 1
  name: Quandoo Public Partner Api Created Customer Example
  slug: quandoo-public-partner-api-created-customer-example
- key_count: 3
  name: Quandoo Public Partner Api Created Reservation Data Example
  slug: quandoo-public-partner-api-created-reservation-data-example
- key_count: 3
  name: Quandoo Public Partner Api Created Reservation Enquiry Data Example
  slug: quandoo-public-partner-api-created-reservation-enquiry-data-example
- key_count: 1
  name: Quandoo Public Partner Api Created Reservation Enquiry Example
  slug: quandoo-public-partner-api-created-reservation-enquiry-example
- key_count: 5
  name: Quandoo Public Partner Api Created Reservation Example
  slug: quandoo-public-partner-api-created-reservation-example
- key_count: 3
  name: Quandoo Public Partner Api Customer Data List Example
  slug: quandoo-public-partner-api-customer-data-list-example
- key_count: 3
  name: Quandoo Public Partner Api Customer Dto Example
  slug: quandoo-public-partner-api-customer-dto-example
- key_count: 10
  name: Quandoo Public Partner Api Customer Response Example
  slug: quandoo-public-partner-api-customer-response-example
- key_count: 4
  name: Quandoo Public Partner Api Customer Review Data Example
  slug: quandoo-public-partner-api-customer-review-data-example
- key_count: 3
  name: Quandoo Public Partner Api Customer Statistics Data Example
  slug: quandoo-public-partner-api-customer-statistics-data-example
- key_count: 4
  name: Quandoo Public Partner Api Document Dto Example
  slug: quandoo-public-partner-api-document-dto-example
- key_count: 7
  name: Quandoo Public Partner Api Get Reservation Enquiry Data Example
  slug: quandoo-public-partner-api-get-reservation-enquiry-data-example
- key_count: 9
  name: Quandoo Public Partner Api Get Review Dto Example
  slug: quandoo-public-partner-api-get-review-dto-example
- key_count: 4
  name: Quandoo Public Partner Api Get Reviews Dto Example
  slug: quandoo-public-partner-api-get-reviews-dto-example
- key_count: 1
  name: Quandoo Public Partner Api Image Dto Example
  slug: quandoo-public-partner-api-image-dto-example
- key_count: 3
  name: Quandoo Public Partner Api Link Relation Dto Example
  slug: quandoo-public-partner-api-link-relation-dto-example
- key_count: 2
  name: Quandoo Public Partner Api Location Dto Example
  slug: quandoo-public-partner-api-location-dto-example
- key_count: 2
  name: Quandoo Public Partner Api Marketing Setting Dto Example
  slug: quandoo-public-partner-api-marketing-setting-dto-example
- key_count: 6
  name: Quandoo Public Partner Api Merchant Address Dto Example
  slug: quandoo-public-partner-api-merchant-address-dto-example
- key_count: 2
  name: Quandoo Public Partner Api Merchant Availability Days Dto Example
  slug: quandoo-public-partner-api-merchant-availability-days-dto-example
- key_count: 4
  name: Quandoo Public Partner Api Merchant Availability Dto Example
  slug: quandoo-public-partner-api-merchant-availability-dto-example
- key_count: 3
  name: Quandoo Public Partner Api Merchant Availability Dto List Example
  slug: quandoo-public-partner-api-merchant-availability-dto-list-example
- key_count: 14
  name: Quandoo Public Partner Api Merchant Customer Data Example
  slug: quandoo-public-partner-api-merchant-customer-data-example
- key_count: 8
  name: Quandoo Public Partner Api Merchant Customer Example
  slug: quandoo-public-partner-api-merchant-customer-example
- key_count: 19
  name: Quandoo Public Partner Api Merchant Details Dto Example
  slug: quandoo-public-partner-api-merchant-details-dto-example
- key_count: 4
  name: Quandoo Public Partner Api Merchant Details Dto List Example
  slug: quandoo-public-partner-api-merchant-details-dto-list-example
- key_count: 3
  name: Quandoo Public Partner Api Merchant Reservation Data Example
  slug: quandoo-public-partner-api-merchant-reservation-data-example
- key_count: 3
  name: Quandoo Public Partner Api Merchant Reservation Data List Example
  slug: quandoo-public-partner-api-merchant-reservation-data-list-example
- key_count: 3
  name: Quandoo Public Partner Api Merchant Reservation Enquiry Data Example
  slug: quandoo-public-partner-api-merchant-reservation-enquiry-data-example
- key_count: 6
  name: Quandoo Public Partner Api Merchant Reservation Enquiry Example
  slug: quandoo-public-partner-api-merchant-reservation-enquiry-example
- key_count: 10
  name: Quandoo Public Partner Api Merchant Reservation Example
  slug: quandoo-public-partner-api-merchant-reservation-example
- key_count: 11
  name: Quandoo Public Partner Api Merchant Reservation Settings Dto Example
  slug: quandoo-public-partner-api-merchant-reservation-settings-dto-example
- key_count: 1
  name: Quandoo Public Partner Api Merchant Subscription Example
  slug: quandoo-public-partner-api-merchant-subscription-example
- key_count: 4
  name: Quandoo Public Partner Api Merchant Vault Settings Dto Example
  slug: quandoo-public-partner-api-merchant-vault-settings-dto-example
- key_count: 3
  name: Quandoo Public Partner Api Merchant With Recommendations Dto Example
  slug: quandoo-public-partner-api-merchant-with-recommendations-dto-example
- key_count: 1
  name: Quandoo Public Partner Api Opening Times Dto Example
  slug: quandoo-public-partner-api-opening-times-dto-example
- key_count: 13
  name: Quandoo Public Partner Api Reservation Data Example
  slug: quandoo-public-partner-api-reservation-data-example
- key_count: 1
  name: Quandoo Public Partner Api Reservation Data List Example
  slug: quandoo-public-partner-api-reservation-data-list-example
- key_count: 6
  name: Quandoo Public Partner Api Reservation Details Example
  slug: quandoo-public-partner-api-reservation-details-example
- key_count: 3
  name: Quandoo Public Partner Api Reservation Enquiry Message Data Example
  slug: quandoo-public-partner-api-reservation-enquiry-message-data-example
- key_count: 1
  name: Quandoo Public Partner Api Reservation Enquiry Message List Example
  slug: quandoo-public-partner-api-reservation-enquiry-message-list-example
- key_count: 3
  name: Quandoo Public Partner Api Reservation Tag Dto Example
  slug: quandoo-public-partner-api-reservation-tag-dto-example
- key_count: 1
  name: Quandoo Public Partner Api Reservation Tags Dto Example
  slug: quandoo-public-partner-api-reservation-tags-dto-example
- key_count: 2
  name: Quandoo Public Partner Api Rest Cookie Example
  slug: quandoo-public-partner-api-rest-cookie-example
- key_count: 5
  name: Quandoo Public Partner Api Review Dto Example
  slug: quandoo-public-partner-api-review-dto-example
- key_count: 4
  name: Quandoo Public Partner Api Review Dto List Example
  slug: quandoo-public-partner-api-review-dto-list-example
- key_count: 0
  name: Quandoo Public Partner Api Standard Opening Times Dto Example
  slug: quandoo-public-partner-api-standard-opening-times-dto-example
- key_count: 2
  name: Quandoo Public Partner Api Tag Group Dto Example
  slug: quandoo-public-partner-api-tag-group-dto-example
- key_count: 2
  name: Quandoo Public Partner Api Tracking Example
  slug: quandoo-public-partner-api-tracking-example
- key_count: 2
  name: Quandoo Public Partner Api Translated Tag Dto Example
  slug: quandoo-public-partner-api-translated-tag-dto-example
- key_count: 1
  name: Quandoo Public Partner Api Update Reservation Data Example
  slug: quandoo-public-partner-api-update-reservation-data-example
- key_count: 1
  name: Quandoo Public Partner Api Update Reservation Enquiry Data Example
  slug: quandoo-public-partner-api-update-reservation-enquiry-data-example
- key_count: 3
  name: Quandoo Public Partner Api Update Review Dto Example
  slug: quandoo-public-partner-api-update-review-dto-example
features:
- description: Check merchant availability days and time slots and search bookable merchants by place, location, date, time, and capacity.
  name: Availability Search
- description: Create, retrieve, and update reservations with idempotent creation keyed on an agent-specific unique ID.
  name: Reservation Management
- description: Create and manage reservation enquiries (for larger groups) including reading enquiry messages and updating status.
  name: Reservation Enquiries
- description: Read merchant reservation and enquiry settings such as capacities, areas, online reservation interval, and credit-card-vault requirements.
  name: Merchant Settings
- description: Read, create, and update customer reviews tied to reservations.
  name: Reviews
- description: Validate customer phone numbers before submitting a reservation.
  name: Phone Validation
- description: Widget, portal, discovery-widget, and direct integration options plus an interactive API explorer.
  name: Multiple Integration Paths
finops:
- name: Quandoo Finops
  service_category: Restaurant Reservations Marketplace
  slug: quandoo-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/quandoo.png
integrations:
- description: Embeddable Quandoo booking widget for merchant websites and apps.
  name: Booking Widget
- description: Reservations sourced through the Google network.
  name: Google Network
- description: Booking integrations across social media channels.
  name: Social Media
- description: Restaurant discovery widget for surfacing bookable merchants.
  name: Discovery Widget
json_schemas:
- name: AgentTracking
  property_count: 1
  slug: quandoo-public-partner-api-agent-tracking
- name: AreaDto
  property_count: 3
  slug: quandoo-public-partner-api-area-dto
- name: ChainDto
  property_count: 2
  slug: quandoo-public-partner-api-chain-dto
- name: ChangedReviewDto
  property_count: 3
  slug: quandoo-public-partner-api-changed-review-dto
- name: CoordinatesDto
  property_count: 2
  slug: quandoo-public-partner-api-coordinates-dto
- name: CreateReviewDto
  property_count: 3
  slug: quandoo-public-partner-api-create-review-dto
- name: CreatedCustomer
  property_count: 1
  slug: quandoo-public-partner-api-created-customer
- name: CreatedReservationData
  property_count: 3
  slug: quandoo-public-partner-api-created-reservation-data
- name: CreatedReservationEnquiryData
  property_count: 3
  slug: quandoo-public-partner-api-created-reservation-enquiry-data
- name: CreatedReservationEnquiry
  property_count: 1
  slug: quandoo-public-partner-api-created-reservation-enquiry
- name: CreatedReservation
  property_count: 5
  slug: quandoo-public-partner-api-created-reservation
- name: CustomerDataList
  property_count: 3
  slug: quandoo-public-partner-api-customer-data-list
- name: CustomerDto
  property_count: 3
  slug: quandoo-public-partner-api-customer-dto
- name: CustomerResponse
  property_count: 10
  slug: quandoo-public-partner-api-customer-response
- name: CustomerReviewData
  property_count: 4
  slug: quandoo-public-partner-api-customer-review-data
- name: CustomerStatisticsData
  property_count: 3
  slug: quandoo-public-partner-api-customer-statistics-data
- name: DocumentDto
  property_count: 4
  slug: quandoo-public-partner-api-document-dto
- name: GetReservationEnquiryData
  property_count: 7
  slug: quandoo-public-partner-api-get-reservation-enquiry-data
- name: GetReviewDto
  property_count: 9
  slug: quandoo-public-partner-api-get-review-dto
- name: GetReviewsDto
  property_count: 4
  slug: quandoo-public-partner-api-get-reviews-dto
- name: ImageDto
  property_count: 1
  slug: quandoo-public-partner-api-image-dto
- name: LinkRelationDto
  property_count: 3
  slug: quandoo-public-partner-api-link-relation-dto
- name: LocationDto
  property_count: 2
  slug: quandoo-public-partner-api-location-dto
- name: MarketingSettingDto
  property_count: 2
  slug: quandoo-public-partner-api-marketing-setting-dto
- name: MerchantAddressDto
  property_count: 6
  slug: quandoo-public-partner-api-merchant-address-dto
- name: MerchantAvailabilityDaysDto
  property_count: 2
  slug: quandoo-public-partner-api-merchant-availability-days-dto
- name: MerchantAvailabilityDtoList
  property_count: 3
  slug: quandoo-public-partner-api-merchant-availability-dto-list
- name: MerchantAvailabilityDto
  property_count: 4
  slug: quandoo-public-partner-api-merchant-availability-dto
- name: MerchantCustomerData
  property_count: 14
  slug: quandoo-public-partner-api-merchant-customer-data
- name: MerchantCustomer
  property_count: 8
  slug: quandoo-public-partner-api-merchant-customer
- name: MerchantDetailsDtoList
  property_count: 4
  slug: quandoo-public-partner-api-merchant-details-dto-list
- name: MerchantDetailsDto
  property_count: 19
  slug: quandoo-public-partner-api-merchant-details-dto
- name: MerchantReservationDataList
  property_count: 3
  slug: quandoo-public-partner-api-merchant-reservation-data-list
- name: MerchantReservationData
  property_count: 3
  slug: quandoo-public-partner-api-merchant-reservation-data
- name: MerchantReservationEnquiryData
  property_count: 3
  slug: quandoo-public-partner-api-merchant-reservation-enquiry-data
- name: MerchantReservationEnquiry
  property_count: 6
  slug: quandoo-public-partner-api-merchant-reservation-enquiry
- name: MerchantReservation
  property_count: 10
  slug: quandoo-public-partner-api-merchant-reservation
- name: MerchantReservationSettingsDto
  property_count: 11
  slug: quandoo-public-partner-api-merchant-reservation-settings-dto
- name: MerchantSubscription
  property_count: 1
  slug: quandoo-public-partner-api-merchant-subscription
- name: MerchantVaultSettingsDto
  property_count: 4
  slug: quandoo-public-partner-api-merchant-vault-settings-dto
- name: MerchantWithRecommendationsDto
  property_count: 3
  slug: quandoo-public-partner-api-merchant-with-recommendations-dto
- name: OpeningTimesDto
  property_count: 1
  slug: quandoo-public-partner-api-opening-times-dto
- name: ReservationDataList
  property_count: 1
  slug: quandoo-public-partner-api-reservation-data-list
- name: ReservationData
  property_count: 13
  slug: quandoo-public-partner-api-reservation-data
- name: ReservationDetails
  property_count: 6
  slug: quandoo-public-partner-api-reservation-details
- name: ReservationEnquiryMessageData
  property_count: 3
  slug: quandoo-public-partner-api-reservation-enquiry-message-data
- name: ReservationEnquiryMessageList
  property_count: 1
  slug: quandoo-public-partner-api-reservation-enquiry-message-list
- name: ReservationTagDto
  property_count: 3
  slug: quandoo-public-partner-api-reservation-tag-dto
- name: ReservationTagsDto
  property_count: 1
  slug: quandoo-public-partner-api-reservation-tags-dto
- name: RestCookie
  property_count: 2
  slug: quandoo-public-partner-api-rest-cookie
- name: ReviewDtoList
  property_count: 4
  slug: quandoo-public-partner-api-review-dto-list
- name: ReviewDto
  property_count: 5
  slug: quandoo-public-partner-api-review-dto
- name: StandardOpeningTimesDto
  property_count: 0
  slug: quandoo-public-partner-api-standard-opening-times-dto
- name: TagGroupDto
  property_count: 2
  slug: quandoo-public-partner-api-tag-group-dto
- name: Tracking
  property_count: 2
  slug: quandoo-public-partner-api-tracking
- name: TranslatedTagDto
  property_count: 2
  slug: quandoo-public-partner-api-translated-tag-dto
- name: UpdateReservationData
  property_count: 1
  slug: quandoo-public-partner-api-update-reservation-data
- name: UpdateReservationEnquiryData
  property_count: 1
  slug: quandoo-public-partner-api-update-reservation-enquiry-data
- name: UpdateReviewDto
  property_count: 3
  slug: quandoo-public-partner-api-update-review-dto
json_structures:
- name: Quandoo Public Partner Api Agent Tracking Structure
  property_count: 1
  slug: quandoo-public-partner-api-agent-tracking-structure
- name: Quandoo Public Partner Api Area Dto Structure
  property_count: 3
  slug: quandoo-public-partner-api-area-dto-structure
- name: Quandoo Public Partner Api Chain Dto Structure
  property_count: 2
  slug: quandoo-public-partner-api-chain-dto-structure
- name: Quandoo Public Partner Api Changed Review Dto Structure
  property_count: 3
  slug: quandoo-public-partner-api-changed-review-dto-structure
- name: Quandoo Public Partner Api Coordinates Dto Structure
  property_count: 2
  slug: quandoo-public-partner-api-coordinates-dto-structure
- name: Quandoo Public Partner Api Create Review Dto Structure
  property_count: 3
  slug: quandoo-public-partner-api-create-review-dto-structure
- name: Quandoo Public Partner Api Created Customer Structure
  property_count: 1
  slug: quandoo-public-partner-api-created-customer-structure
- name: Quandoo Public Partner Api Created Reservation Data Structure
  property_count: 3
  slug: quandoo-public-partner-api-created-reservation-data-structure
- name: Quandoo Public Partner Api Created Reservation Enquiry Data Structure
  property_count: 3
  slug: quandoo-public-partner-api-created-reservation-enquiry-data-structure
- name: Quandoo Public Partner Api Created Reservation Enquiry Structure
  property_count: 1
  slug: quandoo-public-partner-api-created-reservation-enquiry-structure
- name: Quandoo Public Partner Api Created Reservation Structure
  property_count: 5
  slug: quandoo-public-partner-api-created-reservation-structure
- name: Quandoo Public Partner Api Customer Data List Structure
  property_count: 3
  slug: quandoo-public-partner-api-customer-data-list-structure
- name: Quandoo Public Partner Api Customer Dto Structure
  property_count: 3
  slug: quandoo-public-partner-api-customer-dto-structure
- name: Quandoo Public Partner Api Customer Response Structure
  property_count: 10
  slug: quandoo-public-partner-api-customer-response-structure
- name: Quandoo Public Partner Api Customer Review Data Structure
  property_count: 4
  slug: quandoo-public-partner-api-customer-review-data-structure
- name: Quandoo Public Partner Api Customer Statistics Data Structure
  property_count: 3
  slug: quandoo-public-partner-api-customer-statistics-data-structure
- name: Quandoo Public Partner Api Document Dto Structure
  property_count: 4
  slug: quandoo-public-partner-api-document-dto-structure
- name: Quandoo Public Partner Api Get Reservation Enquiry Data Structure
  property_count: 7
  slug: quandoo-public-partner-api-get-reservation-enquiry-data-structure
- name: Quandoo Public Partner Api Get Review Dto Structure
  property_count: 9
  slug: quandoo-public-partner-api-get-review-dto-structure
- name: Quandoo Public Partner Api Get Reviews Dto Structure
  property_count: 4
  slug: quandoo-public-partner-api-get-reviews-dto-structure
- name: Quandoo Public Partner Api Image Dto Structure
  property_count: 1
  slug: quandoo-public-partner-api-image-dto-structure
- name: Quandoo Public Partner Api Link Relation Dto Structure
  property_count: 3
  slug: quandoo-public-partner-api-link-relation-dto-structure
- name: Quandoo Public Partner Api Location Dto Structure
  property_count: 2
  slug: quandoo-public-partner-api-location-dto-structure
- name: Quandoo Public Partner Api Marketing Setting Dto Structure
  property_count: 2
  slug: quandoo-public-partner-api-marketing-setting-dto-structure
- name: Quandoo Public Partner Api Merchant Address Dto Structure
  property_count: 6
  slug: quandoo-public-partner-api-merchant-address-dto-structure
- name: Quandoo Public Partner Api Merchant Availability Days Dto Structure
  property_count: 2
  slug: quandoo-public-partner-api-merchant-availability-days-dto-structure
- name: Quandoo Public Partner Api Merchant Availability Dto List Structure
  property_count: 3
  slug: quandoo-public-partner-api-merchant-availability-dto-list-structure
- name: Quandoo Public Partner Api Merchant Availability Dto Structure
  property_count: 4
  slug: quandoo-public-partner-api-merchant-availability-dto-structure
- name: Quandoo Public Partner Api Merchant Customer Data Structure
  property_count: 14
  slug: quandoo-public-partner-api-merchant-customer-data-structure
- name: Quandoo Public Partner Api Merchant Customer Structure
  property_count: 8
  slug: quandoo-public-partner-api-merchant-customer-structure
- name: Quandoo Public Partner Api Merchant Details Dto List Structure
  property_count: 4
  slug: quandoo-public-partner-api-merchant-details-dto-list-structure
- name: Quandoo Public Partner Api Merchant Details Dto Structure
  property_count: 19
  slug: quandoo-public-partner-api-merchant-details-dto-structure
- name: Quandoo Public Partner Api Merchant Reservation Data List Structure
  property_count: 3
  slug: quandoo-public-partner-api-merchant-reservation-data-list-structure
- name: Quandoo Public Partner Api Merchant Reservation Data Structure
  property_count: 3
  slug: quandoo-public-partner-api-merchant-reservation-data-structure
- name: Quandoo Public Partner Api Merchant Reservation Enquiry Data Structure
  property_count: 3
  slug: quandoo-public-partner-api-merchant-reservation-enquiry-data-structure
- name: Quandoo Public Partner Api Merchant Reservation Enquiry Structure
  property_count: 6
  slug: quandoo-public-partner-api-merchant-reservation-enquiry-structure
- name: Quandoo Public Partner Api Merchant Reservation Settings Dto Structure
  property_count: 11
  slug: quandoo-public-partner-api-merchant-reservation-settings-dto-structure
- name: Quandoo Public Partner Api Merchant Reservation Structure
  property_count: 10
  slug: quandoo-public-partner-api-merchant-reservation-structure
- name: Quandoo Public Partner Api Merchant Subscription Structure
  property_count: 1
  slug: quandoo-public-partner-api-merchant-subscription-structure
- name: Quandoo Public Partner Api Merchant Vault Settings Dto Structure
  property_count: 4
  slug: quandoo-public-partner-api-merchant-vault-settings-dto-structure
- name: Quandoo Public Partner Api Merchant With Recommendations Dto Structure
  property_count: 3
  slug: quandoo-public-partner-api-merchant-with-recommendations-dto-structure
- name: Quandoo Public Partner Api Opening Times Dto Structure
  property_count: 1
  slug: quandoo-public-partner-api-opening-times-dto-structure
- name: Quandoo Public Partner Api Reservation Data List Structure
  property_count: 1
  slug: quandoo-public-partner-api-reservation-data-list-structure
- name: Quandoo Public Partner Api Reservation Data Structure
  property_count: 13
  slug: quandoo-public-partner-api-reservation-data-structure
- name: Quandoo Public Partner Api Reservation Details Structure
  property_count: 6
  slug: quandoo-public-partner-api-reservation-details-structure
- name: Quandoo Public Partner Api Reservation Enquiry Message Data Structure
  property_count: 3
  slug: quandoo-public-partner-api-reservation-enquiry-message-data-structure
- name: Quandoo Public Partner Api Reservation Enquiry Message List Structure
  property_count: 1
  slug: quandoo-public-partner-api-reservation-enquiry-message-list-structure
- name: Quandoo Public Partner Api Reservation Tag Dto Structure
  property_count: 3
  slug: quandoo-public-partner-api-reservation-tag-dto-structure
- name: Quandoo Public Partner Api Reservation Tags Dto Structure
  property_count: 1
  slug: quandoo-public-partner-api-reservation-tags-dto-structure
- name: Quandoo Public Partner Api Rest Cookie Structure
  property_count: 2
  slug: quandoo-public-partner-api-rest-cookie-structure
- name: Quandoo Public Partner Api Review Dto List Structure
  property_count: 4
  slug: quandoo-public-partner-api-review-dto-list-structure
- name: Quandoo Public Partner Api Review Dto Structure
  property_count: 5
  slug: quandoo-public-partner-api-review-dto-structure
- name: Quandoo Public Partner Api Standard Opening Times Dto Structure
  property_count: 0
  slug: quandoo-public-partner-api-standard-opening-times-dto-structure
- name: Quandoo Public Partner Api Tag Group Dto Structure
  property_count: 2
  slug: quandoo-public-partner-api-tag-group-dto-structure
- name: Quandoo Public Partner Api Tracking Structure
  property_count: 2
  slug: quandoo-public-partner-api-tracking-structure
- name: Quandoo Public Partner Api Translated Tag Dto Structure
  property_count: 2
  slug: quandoo-public-partner-api-translated-tag-dto-structure
- name: Quandoo Public Partner Api Update Reservation Data Structure
  property_count: 1
  slug: quandoo-public-partner-api-update-reservation-data-structure
- name: Quandoo Public Partner Api Update Reservation Enquiry Data Structure
  property_count: 1
  slug: quandoo-public-partner-api-update-reservation-enquiry-data-structure
- name: Quandoo Public Partner Api Update Review Dto Structure
  property_count: 3
  slug: quandoo-public-partner-api-update-review-dto-structure
jsonld:
- class_count: 59
  name: Quandoo Context
  property_count: 117
  slug: quandoo-context
layout: provider
modified: '2026-06-03'
name: Quandoo
nav: Providers
network: true
overview: 'Quandoo publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Availabilities API, Customers API, Merchants API, and 7 more. Tagged areas include Restaurant, Reservations, Booking, Availability, and Merchants.


  The Quandoo catalog on APIs.io includes 1 JSON-LD context and 3 Spectral governance rulesets.


  Quandoo''s developer surface includes authentication, documentation, API reference, support, pricing, and 13 more developer resources.'
plans:
- name: Quandoo Plans Pricing
  plan_count: 3
  slug: quandoo-plans-pricing
random_paper: 81
rate_limits:
- limit_count: 2
  name: Quandoo Rate Limits
  slug: quandoo-rate-limits
rules:
- name: Quandoo API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: quandoo-jsonschema-spectral-rules
- name: Quandoo API Rules
  rule_count: 31
  severity_counts:
    error: 10
    hint: 0
    info: 8
    warn: 13
  slug: quandoo-public-partner-api-spectral-rules
- name: Quandoo API Rules
  rule_count: 11
  severity_counts:
    error: 1
    hint: 0
    info: 2
    warn: 8
  slug: quandoo-spectral-rules
score:
  band: strong
  composite: 58.1
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 81.9
    developer_ergonomics: 34.8
    discoverability: 68.5
    governance: 68.8
    operational_transparency: 26.3
  previous_composite: 58.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/quandoo/refs/heads/main/screenshots/quandoo-2026-06-20T192405.png
security:
- kind: authentication
  name: Quandoo Authentication
  slug: quandoo-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Quandoo Domain Security
  slug: quandoo-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Quandoo Vulnerability Disclosure
  slug: quandoo-vulnerability-disclosure
  summary_line: disclosure policy published
slug: quandoo
tags:
- Restaurant
- Reservations
- Booking
- Availability
- Merchants
- Marketplace
use_cases:
- description: Build diner-facing booking flows that search merchants, check availability, and create reservations on top of Quandoo inventory.
  name: Embedded Booking Experiences
- description: Route large-party requests to the enquiry workflow when group size exceeds the merchant minimum for enquiries.
  name: Group Enquiry Handling
- description: Let restaurant operators manage reservations, customers, tags, and reviews for their venue.
  name: Merchant Operations
- description: Distinguish marketplace covers from free own-channel covers (widget, Google, social) for cost attribution.
  name: Channel Attribution
website: https://www.quandoo.com
---
