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
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 49.5
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 53
  human_in_the_loop: 0
  name: Lightspeed Pos Agentic Access
  operation_count: 124
  slug: lightspeed-pos-agentic-access
  summary_line: 124 operations · 53 acting
api_count: 27
apis:
- description: REST API for the Lightspeed eCom C-Series storefront platform.
  name: Lightspeed eCom C-Series API
  slug: ecom-c-series
- description: REST API for Ecwid-powered Lightspeed eCom E-Series stores.
  name: Lightspeed eCom E-Series API (Ecwid)
  slug: ecom-e-series
- description: REST API for the Lightspeed Restaurant L-Series cloud POS.
  name: Lightspeed Restaurant L-Series API
  slug: restaurant-l-series
- description: REST API for Lightspeed Restaurant O-Series (Kounta).
  name: Lightspeed Restaurant O-Series API (Kounta)
  slug: restaurant-o-series
- description: REST API for Lightspeed Restaurant G-Series (Gastrofix).
  name: Lightspeed Restaurant G-Series API (Gastrofix)
  slug: restaurant-g-series
- description: Partner API for ChronoGolf, Lightspeed's tee-time and course management platform.
  name: Lightspeed ChronoGolf Partner API
  slug: chronogolf-partner
- description: The Lightspeed Retail account associated with the access token.
  name: Lightspeed Account API
  slug: lightspeed-pos-account-api
- description: The Brands API from Lightspeed — 2 operation(s) for brands.
  name: Lightspeed Brands API
  slug: lightspeed-pos-brands-api
- description: Categories, manufacturers, and vendors that classify items.
  name: Lightspeed Catalog API
  slug: lightspeed-pos-catalog-api
- description: Customer records and contact details.
  name: Lightspeed Customer API
  slug: lightspeed-pos-customer-api
- description: The Customers API from Lightspeed — 2 operation(s) for customers.
  name: Lightspeed Customers API
  slug: lightspeed-pos-customers-api
- description: 'V1 endpoints (`/f/finance/...`) for retrieving sales and financial data. For the newer V2 versions of these endpoints see FinancialV2 ### V1 behaviour - **Sorting**: No guaranteed sorting order; inter'
  name: Lightspeed Financial API
  slug: lightspeed-pos-financial-api
- description: 'V2 endpoints (`/f/v2/...`) for retrieving sales and financial data. ### Endpoint Mapping | V1 Endpoint | V2 Endpoint | |-------------|-------------| | `getFinancials` (`/f/finance/{id}/financials/{fro'
  name: Lightspeed FinancialV2 API
  slug: lightspeed-pos-financialv2-api
- description: The Gift Cards API from Lightspeed — 1 operation(s) for gift cards.
  name: Lightspeed Gift Cards API
  slug: lightspeed-pos-gift-cards-api
- description: The ID Cards API from Lightspeed — 2 operation(s) for id cards.
  name: Lightspeed ID Cards API
  slug: lightspeed-pos-id-cards-api
- description: Inventory items sold and tracked in Lightspeed Retail.
  name: Lightspeed Item API
  slug: lightspeed-pos-item-api
- description: The Items API from Lightspeed — 2 operation(s) for items.
  name: Lightspeed Items API
  slug: lightspeed-pos-items-api
- description: The Order and Pay API from Lightspeed — 18 operation(s) for order and pay.
  name: Lightspeed Order and Pay API
  slug: lightspeed-pos-order-and-pay-api
- description: 'The Order and Pay: Webhook API from Lightspeed — 4 operation(s) for order and pay: webhook.'
  name: 'Lightspeed Order and Pay: Webhook API'
  slug: lightspeed-pos-order-and-pay-webhook-api
- description: The PMS API from Lightspeed — 3 operation(s) for pms.
  name: Lightspeed PMS API
  slug: lightspeed-pos-pms-api
- description: The Products API from Lightspeed — 2 operation(s) for products.
  name: Lightspeed Products API
  slug: lightspeed-pos-products-api
- description: The Reservations for Platforms API from Lightspeed — 11 operation(s) for reservations for platforms.
  name: Lightspeed Reservations for Platforms API
  slug: lightspeed-pos-reservations-for-platforms-api
- description: The Rich Item API from Lightspeed — 6 operation(s) for rich item.
  name: Lightspeed Rich Item API
  slug: lightspeed-pos-rich-item-api
- description: Point-of-sale transactions and their line items.
  name: Lightspeed Sale API
  slug: lightspeed-pos-sale-api
- description: The Sales API from Lightspeed — 2 operation(s) for sales.
  name: Lightspeed Sales API
  slug: lightspeed-pos-sales-api
- description: Staff API. Authorisation Code grant type is required for this API with permission ROLE_CONFIG_USERS.
  name: Lightspeed Staff API
  slug: lightspeed-pos-staff-api
- description: The Tax Breakdown API from Lightspeed — 1 operation(s) for tax breakdown.
  name: Lightspeed Tax Breakdown API
  slug: lightspeed-pos-tax-breakdown-api
artifact_total: 315
collections:
- collection_type: open
  name: Lightspeed Restaurant K Series API
  slug: open-lightspeed-pos-restaurant-k-series
- collection_type: open
  name: Lightspeed Retail R-Series API
  slug: open-lightspeed-pos-retail-r-series
- collection_type: open
  name: Lightspeed Retail X-Series API
  slug: open-lightspeed-pos-retail-x-series
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/lightspeed-pos-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lightspeed-pos-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/lightspeed-pos-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/lightspeed-pos-scopes.yml
- group: company
  title: ''
  type: Blog
  url: https://www.lightspeedhq.com/blog/feed/
created: '2026-05-08'
description: 'Lightspeed (Lightspeed Commerce) operates a portfolio of Retail, Restaurant, eCom, and Golf POS platforms via series-named product lines: X-Series (Vend), R-Series (Retail Pro/Cloud), C-Series (eCom), E-Series (Ecwid), K-Series (Restaurant Lightspeed), L-Series, O-Series (Kounta), G-Series (Gastrofix), and the ChronoGolf Partner API.'
examples:
- key_count: 4
  name: Restaurant K Series Ape Account Profile Example
  slug: restaurant-k-series-ape-account-profile-example
- key_count: 2
  name: Restaurant K Series Ape Account Profiles Example
  slug: restaurant-k-series-ape-account-profiles-example
- key_count: 19
  name: Restaurant K Series Ape Account Snapshot Example
  slug: restaurant-k-series-ape-account-snapshot-example
- key_count: 9
  name: Restaurant K Series Ape Customer Info Example
  slug: restaurant-k-series-ape-customer-info-example
- key_count: 4
  name: Restaurant K Series Ape Discount Example
  slug: restaurant-k-series-ape-discount-example
- key_count: 10
  name: Restaurant K Series Ape Local Order Item Line Example
  slug: restaurant-k-series-ape-local-order-item-line-example
- key_count: 5
  name: Restaurant K Series Ape Menu Example
  slug: restaurant-k-series-ape-menu-example
- key_count: 5
  name: Restaurant K Series Ape Menu V2 Example
  slug: restaurant-k-series-ape-menu-v2-example
- key_count: 3
  name: Restaurant K Series Ape Order Payment Example
  slug: restaurant-k-series-ape-order-payment-example
- key_count: 5
  name: Restaurant K Series Ape Payment Bad Request Error Example
  slug: restaurant-k-series-ape-payment-bad-request-error-example
- key_count: 1
  name: Restaurant K Series Ape Payment Submission Response Example
  slug: restaurant-k-series-ape-payment-submission-response-example
- key_count: 4
  name: Restaurant K Series Ape Production Instruction Example
  slug: restaurant-k-series-ape-production-instruction-example
- key_count: 2
  name: Restaurant K Series Ape Restricted Item Paginated Response Example
  slug: restaurant-k-series-ape-restricted-item-paginated-response-example
- key_count: 1
  name: Restaurant K Series Ape Skus Request Example
  slug: restaurant-k-series-ape-skus-request-example
- key_count: 12
  name: Restaurant K Series Ape Standalone Payment Example
  slug: restaurant-k-series-ape-standalone-payment-example
- key_count: 6
  name: Restaurant K Series Ape Table Example
  slug: restaurant-k-series-ape-table-example
- key_count: 9
  name: Restaurant K Series Ape To Go Order Item Line Example
  slug: restaurant-k-series-ape-to-go-order-item-line-example
- key_count: 4
  name: Restaurant K Series Ape Webhook Endpoint Business Location Dto Example
  slug: restaurant-k-series-ape-webhook-endpoint-business-location-dto-example
- key_count: 9
  name: Restaurant K Series Ape Webhook Endpoint Example
  slug: restaurant-k-series-ape-webhook-endpoint-example
- key_count: 4
  name: Restaurant K Series Financial Api Aborted Order Dto Example
  slug: restaurant-k-series-financial-api-aborted-order-dto-example
- key_count: 6
  name: Restaurant K Series Financial Api Financial Dto Example
  slug: restaurant-k-series-financial-api-financial-dto-example
- key_count: 4
  name: Restaurant K Series Financial Api Lspayments Dto Example
  slug: restaurant-k-series-financial-api-lspayments-dto-example
- key_count: 2
  name: Restaurant K Series Financial Api Resources Tax Rate Example
  slug: restaurant-k-series-financial-api-resources-tax-rate-example
- key_count: 22
  name: Restaurant K Series Financial Api Sale Dto Example
  slug: restaurant-k-series-financial-api-sale-dto-example
- key_count: 3
  name: Restaurant K Series Financial Api Sales Daily Export Dto Example
  slug: restaurant-k-series-financial-api-sales-daily-export-dto-example
- key_count: 2
  name: Restaurant K Series Financial Api Sales Export Dto Example
  slug: restaurant-k-series-financial-api-sales-export-dto-example
- key_count: 1
  name: Restaurant K Series Id Cards Api Create Id Card Batch Request Example
  slug: restaurant-k-series-id-cards-api-create-id-card-batch-request-example
- key_count: 1
  name: Restaurant K Series Id Cards Api Create Id Cards Request Example
  slug: restaurant-k-series-id-cards-api-create-id-cards-request-example
- key_count: 2
  name: Restaurant K Series Id Cards Api Create Id Cards Response Example
  slug: restaurant-k-series-id-cards-api-create-id-cards-response-example
- key_count: 3
  name: Restaurant K Series Id Cards Api Id Card Batch Example
  slug: restaurant-k-series-id-cards-api-id-card-batch-example
- key_count: 11
  name: Restaurant K Series Items Api Create Item Dto Example
  slug: restaurant-k-series-items-api-create-item-dto-example
- key_count: 19
  name: Restaurant K Series Items Api Item Dto Example
  slug: restaurant-k-series-items-api-item-dto-example
- key_count: 11
  name: Restaurant K Series Items Api Update Item Dto Example
  slug: restaurant-k-series-items-api-update-item-dto-example
- key_count: 6
  name: Restaurant K Series Pms Api Get Provider Example
  slug: restaurant-k-series-pms-api-get-provider-example
- key_count: 4
  name: Restaurant K Series Reservation Service Onboarding Callback Request Example
  slug: restaurant-k-series-reservation-service-onboarding-callback-request-example
- key_count: 1
  name: Restaurant K Series Reservation Service Onboarding Callback Response Example
  slug: restaurant-k-series-reservation-service-onboarding-callback-response-example
- key_count: 2
  name: Restaurant K Series Reservation Service Platform Apikeys Webhook Example
  slug: restaurant-k-series-reservation-service-platform-apikeys-webhook-example
- key_count: 2
  name: Restaurant K Series Reservation Service Platform Basic Auth Webhook Example
  slug: restaurant-k-series-reservation-service-platform-basic-auth-webhook-example
- key_count: 2
  name: Restaurant K Series Reservation Service Platform Bearer Token Webhook Example
  slug: restaurant-k-series-reservation-service-platform-bearer-token-webhook-example
- key_count: 8
  name: Restaurant K Series Reservation Service Platform Business Location Example
  slug: restaurant-k-series-reservation-service-platform-business-location-example
- key_count: 2
  name: Restaurant K Series Reservation Service Platform Course Settings Dto Example
  slug: restaurant-k-series-reservation-service-platform-course-settings-dto-example
- key_count: 2
  name: Restaurant K Series Reservation Service Platform Integration Dto Example
  slug: restaurant-k-series-reservation-service-platform-integration-dto-example
- key_count: 8
  name: Restaurant K Series Reservation Service Platform Oauth2 Webhook Example
  slug: restaurant-k-series-reservation-service-platform-oauth2-webhook-example
- key_count: 15
  name: Restaurant K Series Reservation Service Platform Profile Example
  slug: restaurant-k-series-reservation-service-platform-profile-example
- key_count: 14
  name: Restaurant K Series Reservation Service Platform Profile Response Example
  slug: restaurant-k-series-reservation-service-platform-profile-response-example
- key_count: 4
  name: Restaurant K Series Reservation Service Platform Reservation Accepted Dto Example
  slug: restaurant-k-series-reservation-service-platform-reservation-accepted-dto-example
- key_count: 13
  name: Restaurant K Series Reservation Service Platform Reservation Example
  slug: restaurant-k-series-reservation-service-platform-reservation-example
- key_count: 2
  name: Restaurant K Series Reservation Service Platform Webhook Response Dto Example
  slug: restaurant-k-series-reservation-service-platform-webhook-response-dto-example
- key_count: 13
  name: Restaurant K Series Staff Api Bostaff Example
  slug: restaurant-k-series-staff-api-bostaff-example
- key_count: 1
  name: Restaurant K Series Staff Api Business Location Ids Example
  slug: restaurant-k-series-staff-api-business-location-ids-example
- key_count: 9
  name: Restaurant K Series Staff Api Create Pos Staff Dto Example
  slug: restaurant-k-series-staff-api-create-pos-staff-dto-example
- key_count: 3
  name: Restaurant K Series Staff Api Create Webhook Request Example
  slug: restaurant-k-series-staff-api-create-webhook-request-example
- key_count: 14
  name: Restaurant K Series Staff Api Posstaff Example
  slug: restaurant-k-series-staff-api-posstaff-example
- key_count: 2
  name: Restaurant K Series Staff Api Report Access Level Example
  slug: restaurant-k-series-staff-api-report-access-level-example
- key_count: 3
  name: Restaurant K Series Staff Api Response Schema Example
  slug: restaurant-k-series-staff-api-response-schema-example
- key_count: 8
  name: Restaurant K Series Staff Api Shift Example
  slug: restaurant-k-series-staff-api-shift-example
- key_count: 15
  name: Restaurant K Series Staff Api Staff Example
  slug: restaurant-k-series-staff-api-staff-example
- key_count: 4
  name: Restaurant K Series Staff Api Staff Group Example
  slug: restaurant-k-series-staff-api-staff-group-example
- key_count: 9
  name: Restaurant K Series Staff Api Update Pos Staff Dto Example
  slug: restaurant-k-series-staff-api-update-pos-staff-dto-example
- key_count: 2
  name: Restaurant K Series Staff Api User Permission Example
  slug: restaurant-k-series-staff-api-user-permission-example
- key_count: 7
  name: Restaurant K Series Staff Api Webhook Dto Example
  slug: restaurant-k-series-staff-api-webhook-dto-example
- key_count: 1
  name: Restaurant K Series Teckel Link Self Example
  slug: restaurant-k-series-teckel-link-self-example
- key_count: 1
  name: Restaurant K Series Teckel Link Self Page Example
  slug: restaurant-k-series-teckel-link-self-page-example
- key_count: 4
  name: Restaurant K Series Teckel Picture Spec Dto Example
  slug: restaurant-k-series-teckel-picture-spec-dto-example
- key_count: 3
  name: Restaurant K Series Teckel Rich Item Description Dto Example
  slug: restaurant-k-series-teckel-rich-item-description-dto-example
- key_count: 2
  name: Restaurant K Series Teckel Rich Item Dto Dates Example
  slug: restaurant-k-series-teckel-rich-item-dto-dates-example
- key_count: 4
  name: Restaurant K Series Teckel Rich Item Dto Example
  slug: restaurant-k-series-teckel-rich-item-dto-example
- key_count: 1
  name: Restaurant K Series Teckel Rich Item Dto Links Example
  slug: restaurant-k-series-teckel-rich-item-dto-links-example
- key_count: 3
  name: Restaurant K Series Teckel Rich Item Dto Pictures Example
  slug: restaurant-k-series-teckel-rich-item-dto-pictures-example
- key_count: 3
  name: Retail R Series Account Example
  slug: retail-r-series-account-example
- key_count: 3
  name: Retail R Series Attributes Example
  slug: retail-r-series-attributes-example
- key_count: 4
  name: Retail R Series Category Example
  slug: retail-r-series-category-example
- key_count: 5
  name: Retail R Series Contact Example
  slug: retail-r-series-contact-example
- key_count: 8
  name: Retail R Series Customer Example
  slug: retail-r-series-customer-example
- key_count: 5
  name: Retail R Series Employee Example
  slug: retail-r-series-employee-example
- key_count: 13
  name: Retail R Series Item Example
  slug: retail-r-series-item-example
- key_count: 2
  name: Retail R Series Manufacturer Example
  slug: retail-r-series-manufacturer-example
- key_count: 12
  name: Retail R Series Sale Example
  slug: retail-r-series-sale-example
- key_count: 7
  name: Retail R Series Sale Line Example
  slug: retail-r-series-sale-line-example
- key_count: 4
  name: Retail R Series Shop Example
  slug: retail-r-series-shop-example
- key_count: 4
  name: Retail R Series Vendor Example
  slug: retail-r-series-vendor-example
- key_count: 4
  name: Retail X Series Brand Example
  slug: retail-x-series-brand-example
- key_count: 6
  name: Retail X Series Customer Example
  slug: retail-x-series-customer-example
- key_count: 9
  name: Retail X Series Product Example
  slug: retail-x-series-product-example
- key_count: 9
  name: Retail X Series Sale Example
  slug: retail-x-series-sale-example
finops:
- name: Lightspeed Pos Finops
  service_category: Payments & POS
  slug: lightspeed-pos-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/lightspeed-pos.png
json_schemas:
- name: apeAccountProfile
  property_count: 4
  slug: restaurant-k-series-ape-account-profile
- name: apeAccountProfiles
  property_count: 2
  slug: restaurant-k-series-ape-account-profiles
- name: apeAccountSnapshot
  property_count: 19
  slug: restaurant-k-series-ape-account-snapshot
- name: apeBusinessLocationId
  property_count: 0
  slug: restaurant-k-series-ape-business-location-id
- name: apeCustomerInfo
  property_count: 9
  slug: restaurant-k-series-ape-customer-info
- name: apeDiscount
  property_count: 4
  slug: restaurant-k-series-ape-discount
- name: apeLocalOrderItemLine
  property_count: 10
  slug: restaurant-k-series-ape-local-order-item-line
- name: apeMenu
  property_count: 5
  slug: restaurant-k-series-ape-menu
- name: apeMenuV2
  property_count: 5
  slug: restaurant-k-series-ape-menu-v2
- name: apeOrderPayment
  property_count: 3
  slug: restaurant-k-series-ape-order-payment
- name: apePaymentBadRequestError
  property_count: 5
  slug: restaurant-k-series-ape-payment-bad-request-error
- name: apePaymentSubmissionResponse
  property_count: 1
  slug: restaurant-k-series-ape-payment-submission-response
- name: apeProductionInstruction
  property_count: 4
  slug: restaurant-k-series-ape-production-instruction
- name: apeRestrictedItemPaginatedResponse
  property_count: 2
  slug: restaurant-k-series-ape-restricted-item-paginated-response
- name: apeSkusRequest
  property_count: 1
  slug: restaurant-k-series-ape-skus-request
- name: apeStandalonePayment
  property_count: 12
  slug: restaurant-k-series-ape-standalone-payment
- name: apeTable
  property_count: 6
  slug: restaurant-k-series-ape-table
- name: apeToGoOrderItemLine
  property_count: 9
  slug: restaurant-k-series-ape-to-go-order-item-line
- name: apeWebhookEndpointBusinessLocationDto
  property_count: 4
  slug: restaurant-k-series-ape-webhook-endpoint-business-location-dto
- name: apeWebhookEndpoint
  property_count: 9
  slug: restaurant-k-series-ape-webhook-endpoint
- name: financial-apiAbortedOrderDto
  property_count: 4
  slug: restaurant-k-series-financial-api-aborted-order-dto
- name: financial-apiFinancialDto
  property_count: 6
  slug: restaurant-k-series-financial-api-financial-dto
- name: financial-apiLSPaymentsDto
  property_count: 4
  slug: restaurant-k-series-financial-api-lspayments-dto
- name: financial-apiResourcesTaxRate
  property_count: 2
  slug: restaurant-k-series-financial-api-resources-tax-rate
- name: financial-apiSaleDto
  property_count: 22
  slug: restaurant-k-series-financial-api-sale-dto
- name: financial-apiSalesDailyExportDto
  property_count: 3
  slug: restaurant-k-series-financial-api-sales-daily-export-dto
- name: financial-apiSalesExportDto
  property_count: 2
  slug: restaurant-k-series-financial-api-sales-export-dto
- name: id-cards-apiCreateIdCardBatchRequest
  property_count: 1
  slug: restaurant-k-series-id-cards-api-create-id-card-batch-request
- name: id-cards-apiCreateIdCardsRequest
  property_count: 1
  slug: restaurant-k-series-id-cards-api-create-id-cards-request
- name: id-cards-apiCreateIdCardsResponse
  property_count: 2
  slug: restaurant-k-series-id-cards-api-create-id-cards-response
- name: id-cards-apiIdCardBatch
  property_count: 3
  slug: restaurant-k-series-id-cards-api-id-card-batch
- name: items-apiCreateItemDTO
  property_count: 11
  slug: restaurant-k-series-items-api-create-item-dto
- name: items-apiItemDTO
  property_count: 19
  slug: restaurant-k-series-items-api-item-dto
- name: items-apiUpdateItemDTO
  property_count: 11
  slug: restaurant-k-series-items-api-update-item-dto
- name: pms-apiBusinessLocationId
  property_count: 0
  slug: restaurant-k-series-pms-api-business-location-id
- name: pms-apiGetProvider
  property_count: 6
  slug: restaurant-k-series-pms-api-get-provider
- name: pms-apiProviderApiKey
  property_count: 0
  slug: restaurant-k-series-pms-api-provider-api-key
- name: pms-apiProviderEndpoint
  property_count: 0
  slug: restaurant-k-series-pms-api-provider-endpoint
- name: pms-apiProviderFeatures
  property_count: 0
  slug: restaurant-k-series-pms-api-provider-features
- name: pms-apiProviderName
  property_count: 0
  slug: restaurant-k-series-pms-api-provider-name
- name: pms-apiRevenueCenterId
  property_count: 0
  slug: restaurant-k-series-pms-api-revenue-center-id
- name: pms-apiRevenueCenterName
  property_count: 0
  slug: restaurant-k-series-pms-api-revenue-center-name
- name: reservation-serviceOnboardingCallbackRequest
  property_count: 4
  slug: restaurant-k-series-reservation-service-onboarding-callback-request
- name: reservation-serviceOnboardingCallbackResponse
  property_count: 1
  slug: restaurant-k-series-reservation-service-onboarding-callback-response
- name: reservation-servicePlatformAPIKeysWebhook
  property_count: 2
  slug: restaurant-k-series-reservation-service-platform-apikeys-webhook
- name: reservation-servicePlatformBasicAuthWebhook
  property_count: 2
  slug: restaurant-k-series-reservation-service-platform-basic-auth-webhook
- name: reservation-servicePlatformBearerTokenWebhook
  property_count: 2
  slug: restaurant-k-series-reservation-service-platform-bearer-token-webhook
- name: reservation-servicePlatformBusinessLocation
  property_count: 8
  slug: restaurant-k-series-reservation-service-platform-business-location
- name: reservation-servicePlatformCourseSettingsDto
  property_count: 2
  slug: restaurant-k-series-reservation-service-platform-course-settings-dto
- name: reservation-servicePlatformIntegrationDto
  property_count: 2
  slug: restaurant-k-series-reservation-service-platform-integration-dto
- name: reservation-servicePlatformOAuth2Webhook
  property_count: 8
  slug: restaurant-k-series-reservation-service-platform-oauth2-webhook
- name: reservation-servicePlatformProfileResponse
  property_count: 14
  slug: restaurant-k-series-reservation-service-platform-profile-response
- name: reservation-servicePlatformProfile
  property_count: 15
  slug: restaurant-k-series-reservation-service-platform-profile
- name: reservation-servicePlatformReservationAcceptedDto
  property_count: 4
  slug: restaurant-k-series-reservation-service-platform-reservation-accepted-dto
- name: reservation-servicePlatformReservation
  property_count: 13
  slug: restaurant-k-series-reservation-service-platform-reservation
- name: reservation-servicePlatformWebhookResponseDto
  property_count: 2
  slug: restaurant-k-series-reservation-service-platform-webhook-response-dto
- name: staff-apiBOStaff
  property_count: 13
  slug: restaurant-k-series-staff-api-bostaff
- name: staff-apiBusinessLocationIds
  property_count: 1
  slug: restaurant-k-series-staff-api-business-location-ids
- name: staff-apiCreatePosStaffDto
  property_count: 9
  slug: restaurant-k-series-staff-api-create-pos-staff-dto
- name: staff-apiCreateWebhookRequest
  property_count: 3
  slug: restaurant-k-series-staff-api-create-webhook-request
- name: staff-apiPOSStaff
  property_count: 14
  slug: restaurant-k-series-staff-api-posstaff
- name: staff-apiReportAccessLevel
  property_count: 2
  slug: restaurant-k-series-staff-api-report-access-level
- name: staff-apiResponseSchema
  property_count: 3
  slug: restaurant-k-series-staff-api-response-schema
- name: staff-apiShift
  property_count: 8
  slug: restaurant-k-series-staff-api-shift
- name: staff-apiStaffGroup
  property_count: 4
  slug: restaurant-k-series-staff-api-staff-group
- name: staff-apiStaff
  property_count: 15
  slug: restaurant-k-series-staff-api-staff
- name: staff-apiUpdatePosStaffDto
  property_count: 9
  slug: restaurant-k-series-staff-api-update-pos-staff-dto
- name: staff-apiUserPermission
  property_count: 2
  slug: restaurant-k-series-staff-api-user-permission
- name: staff-apiWebhookDto
  property_count: 7
  slug: restaurant-k-series-staff-api-webhook-dto
- name: teckelLinkSelfPage
  property_count: 1
  slug: restaurant-k-series-teckel-link-self-page
- name: teckelLinkSelf
  property_count: 1
  slug: restaurant-k-series-teckel-link-self
- name: teckelLocalesDto
  property_count: 0
  slug: restaurant-k-series-teckel-locales-dto
- name: teckelPictureSpecDto
  property_count: 4
  slug: restaurant-k-series-teckel-picture-spec-dto
- name: teckelRichItemDescriptionDto
  property_count: 3
  slug: restaurant-k-series-teckel-rich-item-description-dto
- name: teckelRichItemDtoDates
  property_count: 2
  slug: restaurant-k-series-teckel-rich-item-dto-dates
- name: teckelRichItemDtoLinks
  property_count: 1
  slug: restaurant-k-series-teckel-rich-item-dto-links
- name: teckelRichItemDtoPictures
  property_count: 3
  slug: restaurant-k-series-teckel-rich-item-dto-pictures
- name: teckelRichItemDto
  property_count: 4
  slug: restaurant-k-series-teckel-rich-item-dto
- name: Account
  property_count: 3
  slug: retail-r-series-account
- name: Attributes
  property_count: 3
  slug: retail-r-series-attributes
- name: Category
  property_count: 4
  slug: retail-r-series-category
- name: Contact
  property_count: 5
  slug: retail-r-series-contact
- name: Customer
  property_count: 8
  slug: retail-r-series-customer
- name: Employee
  property_count: 5
  slug: retail-r-series-employee
- name: Item
  property_count: 13
  slug: retail-r-series-item
- name: Manufacturer
  property_count: 2
  slug: retail-r-series-manufacturer
- name: SaleLine
  property_count: 7
  slug: retail-r-series-sale-line
- name: Sale
  property_count: 12
  slug: retail-r-series-sale
- name: Shop
  property_count: 4
  slug: retail-r-series-shop
- name: Vendor
  property_count: 4
  slug: retail-r-series-vendor
- name: Brand
  property_count: 4
  slug: retail-x-series-brand
- name: Customer
  property_count: 6
  slug: retail-x-series-customer
- name: Product
  property_count: 9
  slug: retail-x-series-product
- name: Sale
  property_count: 9
  slug: retail-x-series-sale
json_structures:
- name: Restaurant K Series Ape Account Profile Structure
  property_count: 4
  slug: restaurant-k-series-ape-account-profile-structure
- name: Restaurant K Series Ape Account Profiles Structure
  property_count: 2
  slug: restaurant-k-series-ape-account-profiles-structure
- name: Restaurant K Series Ape Account Snapshot Structure
  property_count: 19
  slug: restaurant-k-series-ape-account-snapshot-structure
- name: Restaurant K Series Ape Business Location Id Structure
  property_count: 0
  slug: restaurant-k-series-ape-business-location-id-structure
- name: Restaurant K Series Ape Customer Info Structure
  property_count: 9
  slug: restaurant-k-series-ape-customer-info-structure
- name: Restaurant K Series Ape Discount Structure
  property_count: 4
  slug: restaurant-k-series-ape-discount-structure
- name: Restaurant K Series Ape Local Order Item Line Structure
  property_count: 10
  slug: restaurant-k-series-ape-local-order-item-line-structure
- name: Restaurant K Series Ape Menu Structure
  property_count: 5
  slug: restaurant-k-series-ape-menu-structure
- name: Restaurant K Series Ape Menu V2 Structure
  property_count: 5
  slug: restaurant-k-series-ape-menu-v2-structure
- name: Restaurant K Series Ape Order Payment Structure
  property_count: 3
  slug: restaurant-k-series-ape-order-payment-structure
- name: Restaurant K Series Ape Payment Bad Request Error Structure
  property_count: 5
  slug: restaurant-k-series-ape-payment-bad-request-error-structure
- name: Restaurant K Series Ape Payment Submission Response Structure
  property_count: 1
  slug: restaurant-k-series-ape-payment-submission-response-structure
- name: Restaurant K Series Ape Production Instruction Structure
  property_count: 4
  slug: restaurant-k-series-ape-production-instruction-structure
- name: Restaurant K Series Ape Restricted Item Paginated Response Structure
  property_count: 2
  slug: restaurant-k-series-ape-restricted-item-paginated-response-structure
- name: Restaurant K Series Ape Skus Request Structure
  property_count: 1
  slug: restaurant-k-series-ape-skus-request-structure
- name: Restaurant K Series Ape Standalone Payment Structure
  property_count: 12
  slug: restaurant-k-series-ape-standalone-payment-structure
- name: Restaurant K Series Ape Table Structure
  property_count: 6
  slug: restaurant-k-series-ape-table-structure
- name: Restaurant K Series Ape To Go Order Item Line Structure
  property_count: 9
  slug: restaurant-k-series-ape-to-go-order-item-line-structure
- name: Restaurant K Series Ape Webhook Endpoint Business Location Dto Structure
  property_count: 4
  slug: restaurant-k-series-ape-webhook-endpoint-business-location-dto-structure
- name: Restaurant K Series Ape Webhook Endpoint Structure
  property_count: 9
  slug: restaurant-k-series-ape-webhook-endpoint-structure
- name: Restaurant K Series Financial Api Aborted Order Dto Structure
  property_count: 4
  slug: restaurant-k-series-financial-api-aborted-order-dto-structure
- name: Restaurant K Series Financial Api Financial Dto Structure
  property_count: 6
  slug: restaurant-k-series-financial-api-financial-dto-structure
- name: Restaurant K Series Financial Api Lspayments Dto Structure
  property_count: 4
  slug: restaurant-k-series-financial-api-lspayments-dto-structure
- name: Restaurant K Series Financial Api Resources Tax Rate Structure
  property_count: 2
  slug: restaurant-k-series-financial-api-resources-tax-rate-structure
- name: Restaurant K Series Financial Api Sale Dto Structure
  property_count: 22
  slug: restaurant-k-series-financial-api-sale-dto-structure
- name: Restaurant K Series Financial Api Sales Daily Export Dto Structure
  property_count: 3
  slug: restaurant-k-series-financial-api-sales-daily-export-dto-structure
- name: Restaurant K Series Financial Api Sales Export Dto Structure
  property_count: 2
  slug: restaurant-k-series-financial-api-sales-export-dto-structure
- name: Restaurant K Series Id Cards Api Create Id Card Batch Request Structure
  property_count: 1
  slug: restaurant-k-series-id-cards-api-create-id-card-batch-request-structure
- name: Restaurant K Series Id Cards Api Create Id Cards Request Structure
  property_count: 1
  slug: restaurant-k-series-id-cards-api-create-id-cards-request-structure
- name: Restaurant K Series Id Cards Api Create Id Cards Response Structure
  property_count: 2
  slug: restaurant-k-series-id-cards-api-create-id-cards-response-structure
- name: Restaurant K Series Id Cards Api Id Card Batch Structure
  property_count: 3
  slug: restaurant-k-series-id-cards-api-id-card-batch-structure
- name: Restaurant K Series Items Api Create Item Dto Structure
  property_count: 11
  slug: restaurant-k-series-items-api-create-item-dto-structure
- name: Restaurant K Series Items Api Item Dto Structure
  property_count: 19
  slug: restaurant-k-series-items-api-item-dto-structure
- name: Restaurant K Series Items Api Update Item Dto Structure
  property_count: 11
  slug: restaurant-k-series-items-api-update-item-dto-structure
- name: Restaurant K Series Pms Api Business Location Id Structure
  property_count: 0
  slug: restaurant-k-series-pms-api-business-location-id-structure
- name: Restaurant K Series Pms Api Get Provider Structure
  property_count: 6
  slug: restaurant-k-series-pms-api-get-provider-structure
- name: Restaurant K Series Pms Api Provider Api Key Structure
  property_count: 0
  slug: restaurant-k-series-pms-api-provider-api-key-structure
- name: Restaurant K Series Pms Api Provider Endpoint Structure
  property_count: 0
  slug: restaurant-k-series-pms-api-provider-endpoint-structure
- name: Restaurant K Series Pms Api Provider Features Structure
  property_count: 0
  slug: restaurant-k-series-pms-api-provider-features-structure
- name: Restaurant K Series Pms Api Provider Name Structure
  property_count: 0
  slug: restaurant-k-series-pms-api-provider-name-structure
- name: Restaurant K Series Pms Api Revenue Center Id Structure
  property_count: 0
  slug: restaurant-k-series-pms-api-revenue-center-id-structure
- name: Restaurant K Series Pms Api Revenue Center Name Structure
  property_count: 0
  slug: restaurant-k-series-pms-api-revenue-center-name-structure
- name: Restaurant K Series Reservation Service Onboarding Callback Request Structure
  property_count: 4
  slug: restaurant-k-series-reservation-service-onboarding-callback-request-structure
- name: Restaurant K Series Reservation Service Onboarding Callback Response Structure
  property_count: 1
  slug: restaurant-k-series-reservation-service-onboarding-callback-response-structure
- name: Restaurant K Series Reservation Service Platform Apikeys Webhook Structure
  property_count: 2
  slug: restaurant-k-series-reservation-service-platform-apikeys-webhook-structure
- name: Restaurant K Series Reservation Service Platform Basic Auth Webhook Structure
  property_count: 2
  slug: restaurant-k-series-reservation-service-platform-basic-auth-webhook-structure
- name: Restaurant K Series Reservation Service Platform Bearer Token Webhook Structure
  property_count: 2
  slug: restaurant-k-series-reservation-service-platform-bearer-token-webhook-structure
- name: Restaurant K Series Reservation Service Platform Business Location Structure
  property_count: 8
  slug: restaurant-k-series-reservation-service-platform-business-location-structure
- name: Restaurant K Series Reservation Service Platform Course Settings Dto Structure
  property_count: 2
  slug: restaurant-k-series-reservation-service-platform-course-settings-dto-structure
- name: Restaurant K Series Reservation Service Platform Integration Dto Structure
  property_count: 2
  slug: restaurant-k-series-reservation-service-platform-integration-dto-structure
- name: Restaurant K Series Reservation Service Platform Oauth2 Webhook Structure
  property_count: 8
  slug: restaurant-k-series-reservation-service-platform-oauth2-webhook-structure
- name: Restaurant K Series Reservation Service Platform Profile Response Structure
  property_count: 14
  slug: restaurant-k-series-reservation-service-platform-profile-response-structure
- name: Restaurant K Series Reservation Service Platform Profile Structure
  property_count: 15
  slug: restaurant-k-series-reservation-service-platform-profile-structure
- name: Restaurant K Series Reservation Service Platform Reservation Accepted Dto Structure
  property_count: 4
  slug: restaurant-k-series-reservation-service-platform-reservation-accepted-dto-structure
- name: Restaurant K Series Reservation Service Platform Reservation Structure
  property_count: 13
  slug: restaurant-k-series-reservation-service-platform-reservation-structure
- name: Restaurant K Series Reservation Service Platform Webhook Response Dto Structure
  property_count: 2
  slug: restaurant-k-series-reservation-service-platform-webhook-response-dto-structure
- name: Restaurant K Series Staff Api Bostaff Structure
  property_count: 13
  slug: restaurant-k-series-staff-api-bostaff-structure
- name: Restaurant K Series Staff Api Business Location Ids Structure
  property_count: 1
  slug: restaurant-k-series-staff-api-business-location-ids-structure
- name: Restaurant K Series Staff Api Create Pos Staff Dto Structure
  property_count: 9
  slug: restaurant-k-series-staff-api-create-pos-staff-dto-structure
- name: Restaurant K Series Staff Api Create Webhook Request Structure
  property_count: 3
  slug: restaurant-k-series-staff-api-create-webhook-request-structure
- name: Restaurant K Series Staff Api Posstaff Structure
  property_count: 14
  slug: restaurant-k-series-staff-api-posstaff-structure
- name: Restaurant K Series Staff Api Report Access Level Structure
  property_count: 2
  slug: restaurant-k-series-staff-api-report-access-level-structure
- name: Restaurant K Series Staff Api Response Schema Structure
  property_count: 3
  slug: restaurant-k-series-staff-api-response-schema-structure
- name: Restaurant K Series Staff Api Shift Structure
  property_count: 8
  slug: restaurant-k-series-staff-api-shift-structure
- name: Restaurant K Series Staff Api Staff Group Structure
  property_count: 4
  slug: restaurant-k-series-staff-api-staff-group-structure
- name: Restaurant K Series Staff Api Staff Structure
  property_count: 15
  slug: restaurant-k-series-staff-api-staff-structure
- name: Restaurant K Series Staff Api Update Pos Staff Dto Structure
  property_count: 9
  slug: restaurant-k-series-staff-api-update-pos-staff-dto-structure
- name: Restaurant K Series Staff Api User Permission Structure
  property_count: 2
  slug: restaurant-k-series-staff-api-user-permission-structure
- name: Restaurant K Series Staff Api Webhook Dto Structure
  property_count: 7
  slug: restaurant-k-series-staff-api-webhook-dto-structure
- name: Restaurant K Series Teckel Link Self Page Structure
  property_count: 1
  slug: restaurant-k-series-teckel-link-self-page-structure
- name: Restaurant K Series Teckel Link Self Structure
  property_count: 1
  slug: restaurant-k-series-teckel-link-self-structure
- name: Restaurant K Series Teckel Locales Dto Structure
  property_count: 0
  slug: restaurant-k-series-teckel-locales-dto-structure
- name: Restaurant K Series Teckel Picture Spec Dto Structure
  property_count: 4
  slug: restaurant-k-series-teckel-picture-spec-dto-structure
- name: Restaurant K Series Teckel Rich Item Description Dto Structure
  property_count: 3
  slug: restaurant-k-series-teckel-rich-item-description-dto-structure
- name: Restaurant K Series Teckel Rich Item Dto Dates Structure
  property_count: 2
  slug: restaurant-k-series-teckel-rich-item-dto-dates-structure
- name: Restaurant K Series Teckel Rich Item Dto Links Structure
  property_count: 1
  slug: restaurant-k-series-teckel-rich-item-dto-links-structure
- name: Restaurant K Series Teckel Rich Item Dto Pictures Structure
  property_count: 3
  slug: restaurant-k-series-teckel-rich-item-dto-pictures-structure
- name: Restaurant K Series Teckel Rich Item Dto Structure
  property_count: 4
  slug: restaurant-k-series-teckel-rich-item-dto-structure
- name: Retail R Series Account Structure
  property_count: 3
  slug: retail-r-series-account-structure
- name: Retail R Series Attributes Structure
  property_count: 3
  slug: retail-r-series-attributes-structure
- name: Retail R Series Category Structure
  property_count: 4
  slug: retail-r-series-category-structure
- name: Retail R Series Contact Structure
  property_count: 5
  slug: retail-r-series-contact-structure
- name: Retail R Series Customer Structure
  property_count: 8
  slug: retail-r-series-customer-structure
- name: Retail R Series Employee Structure
  property_count: 5
  slug: retail-r-series-employee-structure
- name: Retail R Series Item Structure
  property_count: 13
  slug: retail-r-series-item-structure
- name: Retail R Series Manufacturer Structure
  property_count: 2
  slug: retail-r-series-manufacturer-structure
- name: Retail R Series Sale Line Structure
  property_count: 7
  slug: retail-r-series-sale-line-structure
- name: Retail R Series Sale Structure
  property_count: 12
  slug: retail-r-series-sale-structure
- name: Retail R Series Shop Structure
  property_count: 4
  slug: retail-r-series-shop-structure
- name: Retail R Series Vendor Structure
  property_count: 4
  slug: retail-r-series-vendor-structure
- name: Retail X Series Brand Structure
  property_count: 4
  slug: retail-x-series-brand-structure
- name: Retail X Series Customer Structure
  property_count: 6
  slug: retail-x-series-customer-structure
- name: Retail X Series Product Structure
  property_count: 9
  slug: retail-x-series-product-structure
- name: Retail X Series Sale Structure
  property_count: 9
  slug: retail-x-series-sale-structure
jsonld:
- class_count: 69
  name: Lightspeed Pos Restaurant K Series Context
  property_count: 346
  slug: lightspeed-pos-restaurant-k-series-context
- class_count: 10
  name: Lightspeed Pos Retail R Series Context
  property_count: 53
  slug: lightspeed-pos-retail-r-series-context
- class_count: 4
  name: Lightspeed Pos Retail X Series Context
  property_count: 23
  slug: lightspeed-pos-retail-x-series-context
layout: provider
modified: '2026-06-02'
name: Lightspeed
nav: Providers
network: true
overview: 'Lightspeed publishes 21 APIs on the [APIs.io](https://apis.io/) network, including Account API, Brands API, Catalog API, and 18 more. Tagged areas include POS, Retail, Restaurant, and Ecommerce.


  The Lightspeed catalog on APIs.io includes 3 JSON-LD contexts and 2 Spectral governance rulesets.


  Lightspeed''s developer surface includes authentication, engineering blog, and 3 more developer resources.'
plans:
- name: Lightspeed Pos Plans Pricing
  plan_count: 1
  slug: lightspeed-pos-plans-pricing
random_paper: 56
rate_limits:
- limit_count: 4
  name: Lightspeed Pos Rate Limits
  slug: lightspeed-pos-rate-limits
rules:
- name: Lightspeed API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: lightspeed-pos-jsonschema-spectral-rules
- name: Lightspeed API Rules
  rule_count: 33
  severity_counts:
    error: 6
    hint: 0
    info: 13
    warn: 14
  slug: lightspeed-pos-spectral-rules
scopes:
- name: Lightspeed Pos Scopes
  scope_count: 24
  slug: lightspeed-pos-scopes
  summary_line: 24 scopes · authorizationCode
score:
  band: emerging
  composite: 24.7
  delta: -6.5
  facets:
    commercial_clarity: 13.2
    contract_quality: 23.7
    developer_ergonomics: 13.0
    discoverability: 55.6
    governance: 58.3
    operational_transparency: 7.9
  previous_composite: 31.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 21
      marker_coverage: 100.0
      total: 21
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/lightspeed-pos/refs/heads/main/screenshots/lightspeed-pos-2026-06-20T184525.png
security:
- kind: authentication
  name: Lightspeed Pos Authentication
  slug: lightspeed-pos-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Lightspeed Pos Domain Security
  slug: lightspeed-pos-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: lightspeed-pos
tags:
- POS
- Retail
- Restaurant
- Ecommerce
---
