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
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 45.1
  scored_at: '2026-09-17'
agentic_access:
- acting_count: 56
  human_in_the_loop: 5
  name: Grubhub Agentic Access
  operation_count: 91
  slug: grubhub-agentic-access
  summary_line: 91 operations · 56 acting · 5 human-in-the-loop
api_count: 12
apis:
- baseURL: https://api-third-party-gtm.grubhub.com
  baseurl_source: declared
  description: 'Create, update and manage Grubhub Marketplace menus. Ingestion is diff-based against external IDs: validate a normalized menu, submit it, poll the ingestion job, and read back what Grubhub stored. Als'
  name: Grubhub Menu API
  slug: grubhub-menu
- baseURL: https://api-third-party-gtm.grubhub.com
  baseurl_source: declared
  description: 'Receive and manage Grubhub Marketplace orders. Retrieve an order by UUID, list a merchant''s or a group''s orders by status and date range, advance an order through its status lifecycle, raise and poll '
  name: Grubhub Orders API
  slug: grubhub-orders
- baseURL: https://api-third-party-gtm.grubhub.com
  baseurl_source: declared
  description: 'Read and maintain merchant configuration on Grubhub: profile, tax rate, delivery minimum, delivery boundaries and area fees, fulfillment estimates, pre-order window, scheduled-ordering opt-in, and onl'
  name: Grubhub Merchant Data API
  slug: grubhub-merchant-data
- baseURL: https://api-third-party-gtm.grubhub.com
  baseurl_source: declared
  description: 'Manage restaurant operating hours on Grubhub: repeating weekly schedules for delivery, pickup and catering, one-off schedule overrides for closures and special hours, and immediate open-now / close-no'
  name: Grubhub Merchant Schedules API
  slug: grubhub-merchant-schedules
- baseURL: https://api-third-party-gtm.grubhub.com
  baseurl_source: declared
  description: Mark a restaurant as busy for a bounded interval so Grubhub extends quoted times or pauses new orders, then read, update or clear the active interval.
  name: Grubhub Busy Intervals API
  slug: grubhub-busy-intervals
- baseURL: https://api-third-party-gtm.grubhub.com
  baseurl_source: declared
  description: Read the delivery state of a Grubhub Marketplace order, by order UUID or by delivery ID. The only operation in the whole Grubhub contract that declares a 429 lives here.
  name: Grubhub Deliveries API
  slug: grubhub-deliveries
- baseURL: https://api-third-party-gtm.grubhub.com
  baseurl_source: declared
  description: Grubhub Connect is delivery-as-a-service on Grubhub's national courier network for aggregators, marketplaces and enterprise merchants. Request and accept delivery quotes, check service areas, track st
  name: Grubhub Connect (Delivery as a Service) API
  slug: grubhub-connect-endpoints
- baseURL: https://api-third-party-gtm.grubhub.com
  baseurl_source: declared
  description: 'The egress event contract for Grubhub Connect, published as an OpenAPI 3.1.0 webhooks-only document: Delivery Status Update (Created, Assigned, Unassigned, CourierAtPickup, PickedUp, InTransit, Courie'
  name: Grubhub Connect Webhooks
  slug: grubhub-connect-webhooks
- baseURL: https://api-third-party-gtm.grubhub.com
  baseurl_source: declared
  description: 'Self-service merchant onboarding for partners: list eligible merchants, refer a restaurant that is not yet on Grubhub, associate an existing merchant with the integration, activate and deactivate merc'
  name: Grubhub Onboarding API
  slug: grubhub-onboarding
- baseURL: https://api-third-party-gtm.grubhub.com
  baseurl_source: declared
  description: 'Asynchronous merchant report export: list the merchants enabled for reporting under a partner ID, request a report, and fetch its download URL once the report-status webhook fires.'
  name: Grubhub Merchant Reporting API
  slug: grubhub-reporting-endpoints
- baseURL: https://api-third-party-gtm.grubhub.com
  baseurl_source: declared
  description: 'The egress event contract for merchant report exports, published as an OpenAPI 3.1.0 webhooks-only document: Report Status Update. This is the intended completion signal for a requested report.'
  name: Grubhub Reporting Webhooks
  slug: grubhub-reporting-webhooks
- baseURL: https://api-third-party-gtm.grubhub.com
  baseurl_source: declared
  description: 'Grubhub ships its partner test surface as part of the published contract: create a transmission test, simulate a just-in-time order event, and create a test delivery against a preproduction merchant.'
  name: Grubhub Testing API
  slug: grubhub-testing
artifact_total: 275
asyncapis:
- description: 'Egress webhooks Grubhub sends to a Grubhub Connect (delivery-as-a-service) partner: delivery status transitions and delivery refund updates. Derived verbatim from the webhooks object of Grubhub''s own '
  name: Grubhub Connect Delivery Events
  slug: grubhub-delivery-events-asyncapi
- description: Event-driven interface for receiving real-time order notifications from Grubhub. When a diner places an order, Grubhub monitors that order and sends notifications based on the current status. The webh
  name: Grubhub Order Events
  slug: grubhub-order-events-asyncapi
- description: Egress webhook Grubhub sends when a requested merchant export report changes state. This is the intended completion signal for the asynchronous Reporting API - poll only as a fallback.
  name: Grubhub Merchant Reporting Events
  slug: grubhub-reporting-events-asyncapi
- description: ''
  name: Grubhub Webhooks
  slug: grubhub-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.grubhub.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.grubhub.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.grubhub.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.grubhub.com/api/menu
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.grubhub.com/get-started
- group: operate
  title: ''
  type: Support
  url: https://get.grubhub.com/help-center/
- group: operate
  title: ''
  type: HelpCenter
  url: https://get.grubhub.com/contact/
- group: commercial
  title: ''
  type: Pricing
  url: https://get.grubhub.com/grubhub-pricing-and-fees/
- group: start
  title: ''
  type: SignUp
  url: https://restaurant.grubhub.com/login/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.grubhub.com/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.grubhub.com/legal/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/GrubhubProd
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/grubhub-seamless
- group: company
  title: ''
  type: Blog
  url: https://get.grubhub.com/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://get.grubhub.com/blog/feed/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/grubhub/refs/heads/main/authentication/grubhub-authentication.yml
  title: ''
  type: Authentication
  url: authentication/grubhub-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/grubhub/refs/heads/main/scopes/grubhub-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/grubhub-scopes.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/grubhub/refs/heads/main/well-known/grubhub-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/grubhub-well-known.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/grubhub/refs/heads/main/conventions/grubhub-conventions.yml
  title: ''
  type: Conventions
  url: conventions/grubhub-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/grubhub/refs/heads/main/errors/grubhub-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/grubhub-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/grubhub/refs/heads/main/data-model/grubhub-data-model.yml
  title: ''
  type: DataModel
  url: data-model/grubhub-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/grubhub/refs/heads/main/lifecycle/grubhub-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/grubhub-lifecycle.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/grubhub/refs/heads/main/sandbox/grubhub-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/grubhub-sandbox.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/grubhub/refs/heads/main/conformance/grubhub-conformance.yml
  title: ''
  type: Conformance
  url: conformance/grubhub-conformance.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/grubhub/refs/heads/main/packages/grubhub-packages.yml
  title: ''
  type: Packages
  url: packages/grubhub-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/grubhub/refs/heads/main/llms/grubhub-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/grubhub-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/grubhub/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/grubhub/refs/heads/main/asyncapi/grubhub-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/grubhub-webhooks.yml
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/grubhub/refs/heads/main/asyncapi/grubhub-delivery-events-asyncapi.yml
  title: ''
  type: AsyncAPI
  url: asyncapi/grubhub-delivery-events-asyncapi.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/grubhub/refs/heads/main/agentic-access/grubhub-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/grubhub-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/grubhub/refs/heads/main/security/grubhub-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/grubhub-domain-security.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/grubhub/refs/heads/main/rate-limits/grubhub-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/grubhub-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/grubhub/refs/heads/main/plans/grubhub-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/grubhub-plans-pricing.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/grubhub/refs/heads/main/finops/grubhub-finops.yml
  title: ''
  type: FinOps
  url: finops/grubhub-finops.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/grubhub/refs/heads/main/vocabulary/grubhub-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/grubhub-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/grubhub/refs/heads/main/rules/grubhub-spectral-rules.yml
  title: ''
  type: Rules
  url: rules/grubhub-spectral-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/grubhub/refs/heads/main/json-ld/grubhub-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/grubhub-context.jsonld
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/grubhub/refs/heads/main/json-schema/grubhub-posorder-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/grubhub-posorder-schema.json
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/grubhub/refs/heads/main/json-schema/grubhub-posnormalizedmenu-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/grubhub-posnormalizedmenu-schema.json
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/grubhub/refs/heads/main/json-schema/grubhub-posmerchantdata-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/grubhub-posmerchantdata-schema.json
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/grubhub/refs/heads/main/json-schema/grubhub-delivery-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/grubhub-delivery-schema.json
created: '2026-05-04'
description: 'Grubhub is a US online food-ordering and delivery marketplace connecting diners with local restaurants across Grubhub and Seamless. Its partner platform lets point-of-sale vendors, online-ordering providers, delivery aggregators and enterprise restaurant brands integrate directly: ingest normalized menus, receive and fulfil Marketplace orders, control merchant availability and schedules, run last-mile delivery on Grubhub''s national courier network through Grubhub Connect, onboard merchants self-service, and export merchant reports. Grubhub publishes twelve first-party OpenAPI documents covering 91 operations and three egress webhooks from its partner developer portal.'
finops:
- name: Grubhub Finops
  service_category: Food Delivery / Marketplaces
  slug: grubhub-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/grubhub.png
json_schemas:
- name: AcceptQuoteResponse
  property_count: 1
  slug: grubhub-acceptquoteresponse
- name: ActivateRequest
  property_count: 1
  slug: grubhub-activaterequest
- name: AddLineSubstitution
  property_count: 0
  slug: grubhub-addlinesubstitution
- name: Address
  property_count: 12
  slug: grubhub-address
- name: Affiliate
  property_count: 3
  slug: grubhub-affiliate
- name: Assigned
  property_count: 0
  slug: grubhub-assigned
- name: AssociationResponse
  property_count: 4
  slug: grubhub-associationresponse
- name: AvailabilityOverride
  property_count: 5
  slug: grubhub-availabilityoverride
- name: AvailabilityRange
  property_count: 4
  slug: grubhub-availabilityrange
- name: BulkProcessingItemEntityStatus
  property_count: 4
  slug: grubhub-bulkprocessingitementitystatus
- name: CancelDeliveryRequest
  property_count: 2
  slug: grubhub-canceldeliveryrequest
- name: Canceled
  property_count: 0
  slug: grubhub-canceled
- name: CatalogVersion
  property_count: 1
  slug: grubhub-catalogversion
- name: Catering
  property_count: 7
  slug: grubhub-catering
- name: Charges
  property_count: 2
  slug: grubhub-charges
- name: Chronology
  property_count: 1
  slug: grubhub-chronology
- name: ClientData
  property_count: 4
  slug: grubhub-clientdata
- name: com.grubhub.pos.generic.delivery.fulfillment.common.model.PickupVerification
  property_count: 2
  slug: grubhub-com-grubhub-pos-generic-delivery-fulfillment-common-model-pickupverification
- name: ConfigGroup
  property_count: 2
  slug: grubhub-configgroup
- name: ContactInfo
  property_count: 3
  slug: grubhub-contactinfo
- name: Coordinates
  property_count: 2
  slug: grubhub-coordinates
- name: Courier
  property_count: 3
  slug: grubhub-courier
- name: CourierAtDropoff
  property_count: 0
  slug: grubhub-courieratdropoff
- name: CourierAtPickup
  property_count: 0
  slug: grubhub-courieratpickup
- name: Created
  property_count: 0
  slug: grubhub-created
- name: CreateExportReportRequestByPartner
  property_count: 5
  slug: grubhub-createexportreportrequestbypartner
- name: CreateExportReportResponseByPartner
  property_count: 1
  slug: grubhub-createexportreportresponsebypartner
- name: CustomScheduleMetadata
  property_count: 8
  slug: grubhub-customschedulemetadata
- name: DateRange
  property_count: 2
  slug: grubhub-daterange
- name: DateTimeField
  property_count: 9
  slug: grubhub-datetimefield
- name: DateTimeFieldType
  property_count: 3
  slug: grubhub-datetimefieldtype
- name: DateTimeZone
  property_count: 2
  slug: grubhub-datetimezone
- name: DeactivateRequest
  property_count: 1
  slug: grubhub-deactivaterequest
- name: DeactivateResponse
  property_count: 2
  slug: grubhub-deactivateresponse
- name: DefaultContext
  property_count: 3
  slug: grubhub-defaultcontext
- name: Delivered
  property_count: 0
  slug: grubhub-delivered
- name: Delivery
  property_count: 4
  slug: grubhub-delivery
- name: DeliveryAddress
  property_count: 6
  slug: grubhub-deliveryaddress
- name: DeliveryArea
  property_count: 2
  slug: grubhub-deliveryarea
- name: DeliveryAreaStats
  property_count: 4
  slug: grubhub-deliveryareastats
- name: DeliveryEvent
  property_count: 2
  slug: grubhub-deliveryevent
- name: DeliveryInfo
  property_count: 12
  slug: grubhub-deliveryinfo
- name: DeliveryItem
  property_count: 8
  slug: grubhub-deliveryitem
- name: DeliveryItemOption
  property_count: 4
  slug: grubhub-deliveryitemoption
- name: DeliveryPreferences
  property_count: 2
  slug: grubhub-deliverypreferences
- name: DeliveryRefundUpdate
  property_count: 5
  slug: grubhub-deliveryrefundupdate
- name: DeliverySizing
  property_count: 2
  slug: grubhub-deliverysizing
- name: DeliveryStatusResponse
  property_count: 3
  slug: grubhub-deliverystatusresponse
- name: DeliveryStatusUpdate
  property_count: 4
  slug: grubhub-deliverystatusupdate
- name: DeliveryTestRequest
  property_count: 2
  slug: grubhub-deliverytestrequest
- name: DeliveryTime
  property_count: 2
  slug: grubhub-deliverytime
- name: DeliveryTimes
  property_count: 10
  slug: grubhub-deliverytimes
- name: Dimensions
  property_count: 3
  slug: grubhub-dimensions
- name: Diner
  property_count: 7
  slug: grubhub-diner
- name: DinerPickUpInstructions
  property_count: 3
  slug: grubhub-dinerpickupinstructions
- name: DropoffImageDetails
  property_count: 4
  slug: grubhub-dropoffimagedetails
- name: DropoffLocation
  property_count: 5
  slug: grubhub-dropofflocation
- name: DropoffPreferences
  property_count: 1
  slug: grubhub-dropoffpreferences
- name: DurationField
  property_count: 5
  slug: grubhub-durationfield
- name: DurationFieldType
  property_count: 1
  slug: grubhub-durationfieldtype
- name: EmulateDeliveryStatusUpdateWebhookRequest
  property_count: 1
  slug: grubhub-emulatedeliverystatusupdatewebhookrequest
- name: EstimatedEventTimes
  property_count: 2
  slug: grubhub-estimatedeventtimes
- name: ExternalId
  property_count: 4
  slug: grubhub-externalid
- name: Feature
  property_count: 3
  slug: grubhub-feature
- name: Fees
  property_count: 2
  slug: grubhub-fees
- name: FulfillmentInfo
  property_count: 2
  slug: grubhub-fulfillmentinfo
- name: GeoLocation
  property_count: 2
  slug: grubhub-geolocation
- name: Geometry
  property_count: 2
  slug: grubhub-geometry
- name: GetDownloadUrlResponseByPartner
  property_count: 1
  slug: grubhub-getdownloadurlresponsebypartner
- name: GetEnabledMerchantsResponse
  property_count: 1
  slug: grubhub-getenabledmerchantsresponse
- name: HeartbeatTriggeredPayload
  property_count: 2
  slug: grubhub-heartbeattriggeredpayload
- name: IncreaseTipRequest
  property_count: 1
  slug: grubhub-increasetiprequest
- name: Instant
  property_count: 6
  slug: grubhub-instant
- name: InTransit
  property_count: 0
  slug: grubhub-intransit
- name: InvalidCodeAndEntityIds
  property_count: 3
  slug: grubhub-invalidcodeandentityids
- name: Item
  property_count: 5
  slug: grubhub-item
- name: ItemDimensions
  property_count: 4
  slug: grubhub-itemdimensions
- name: ItemSizing
  property_count: 2
  slug: grubhub-itemsizing
- name: ItemWeight
  property_count: 2
  slug: grubhub-itemweight
- name: JitTestOrder
  property_count: 4
  slug: grubhub-jittestorder
- name: JsonNode
  property_count: 0
  slug: grubhub-jsonnode
- name: LeadTimeSettings
  property_count: 4
  slug: grubhub-leadtimesettings
- name: LeadTimeSettingsTier
  property_count: 3
  slug: grubhub-leadtimesettingstier
- name: Line
  property_count: 31
  slug: grubhub-line
- name: LineGroup
  property_count: 2
  slug: grubhub-linegroup
- name: LineOption
  property_count: 11
  slug: grubhub-lineoption
- name: LineOptionSubstitution
  property_count: 7
  slug: grubhub-lineoptionsubstitution
- name: LineSubOption
  property_count: 13
  slug: grubhub-linesuboption
- name: LineSubstitutionAdjustment
  property_count: 0
  slug: grubhub-linesubstitutionadjustment
- name: LineSubstitutionReplacement
  property_count: 10
  slug: grubhub-linesubstitutionreplacement
- name: LineSubstitutionType
  property_count: 1
  slug: grubhub-linesubstitutiontype
- name: LineTag
  property_count: 2
  slug: grubhub-linetag
- name: LocalTime
  property_count: 9
  slug: grubhub-localtime
- name: Location
  property_count: 8
  slug: grubhub-location
- name: MassScheduleOverrideMetadata
  property_count: 9
  slug: grubhub-massscheduleoverridemetadata
- name: MeasuredPrice
  property_count: 2
  slug: grubhub-measuredprice
- name: MediaValidationErrorDTO
  property_count: 5
  slug: grubhub-mediavalidationerrordto
- name: MenuInfo
  property_count: 5
  slug: grubhub-menuinfo
- name: MenuMerchantStatus
  property_count: 8
  slug: grubhub-menumerchantstatus
- name: MenuSection
  property_count: 11
  slug: grubhub-menusection
- name: MerchantActivationEnablementResponse
  property_count: 3
  slug: grubhub-merchantactivationenablementresponse
- name: MerchantActivationResponse
  property_count: 2
  slug: grubhub-merchantactivationresponse
- name: MerchantAssociationResponse
  property_count: 1
  slug: grubhub-merchantassociationresponse
- name: MerchantEligibilityResponse
  property_count: 5
  slug: grubhub-merchanteligibilityresponse
- name: MerchantHeartbeatTriggeredPayload
  property_count: 3
  slug: grubhub-merchantheartbeattriggeredpayload
- name: MerchantOrderTypeHeartbeatPayload
  property_count: 2
  slug: grubhub-merchantordertypeheartbeatpayload
- name: MerchantPropertyUpdateRequest
  property_count: 2
  slug: grubhub-merchantpropertyupdaterequest
- name: MerchantReportingErrorResponse
  property_count: 1
  slug: grubhub-merchantreportingerrorresponse
- name: Merchant Report Status Webhook
  property_count: 4
  slug: grubhub-merchantreportstatuswebhook
- name: MerchantStatus
  property_count: 3
  slug: grubhub-merchantstatus
- name: Modifier
  property_count: 20
  slug: grubhub-modifier
- name: ModifierList
  property_count: 3
  slug: grubhub-modifierlist
- name: ModifierPrompt
  property_count: 9
  slug: grubhub-modifierprompt
- name: ModifierPromptFreeSettings
  property_count: 1
  slug: grubhub-modifierpromptfreesettings
- name: ModifierPromptQuantitySettings
  property_count: 2
  slug: grubhub-modifierpromptquantitysettings
- name: ModifierPromptSelectionSettings
  property_count: 2
  slug: grubhub-modifierpromptselectionsettings
- name: ModifierQuantitySettings
  property_count: 3
  slug: grubhub-modifierquantitysettings
- name: NormalizedItemFulfillmentTypeSettings
  property_count: 1
  slug: grubhub-normalizeditemfulfillmenttypesettings
- name: NormalizedModifierFulfillmentTypeSettings
  property_count: 1
  slug: grubhub-normalizedmodifierfulfillmenttypesettings
- name: NormalizedSizedPriceFulfillmentTypeSettings
  property_count: 1
  slug: grubhub-normalizedsizedpricefulfillmenttypesettings
- name: NormalizedSizeFulfillmentTypeSettings
  property_count: 1
  slug: grubhub-normalizedsizefulfillmenttypesettings
- name: NotificationPreferences
  property_count: 1
  slug: grubhub-notificationpreferences
- name: OrderChangeRequest
  property_count: 10
  slug: grubhub-orderchangerequest
- name: OrderChangeRequestStatus
  property_count: 6
  slug: grubhub-orderchangerequeststatus
- name: OrderFacetData
  property_count: 2
  slug: grubhub-orderfacetdata
- name: OrderPickupInstructions
  property_count: 3
  slug: grubhub-orderpickupinstructions
- name: OrderPickupVerification
  property_count: 2
  slug: grubhub-orderpickupverification
- name: OrderProcessingInfo
  property_count: 2
  slug: grubhub-orderprocessinginfo
- name: OrderTakingInfo
  property_count: 3
  slug: grubhub-ordertakinginfo
- name: OrderTypeHeartbeatPayload
  property_count: 1
  slug: grubhub-ordertypeheartbeatpayload
- name: PartnerDeactivateRequest
  property_count: 1
  slug: grubhub-partnerdeactivaterequest
- name: PartnerDeactivateResponse
  property_count: 2
  slug: grubhub-partnerdeactivateresponse
- name: Payment
  property_count: 6
  slug: grubhub-payment
- name: Payments
  property_count: 6
  slug: grubhub-payments
- name: PeriodSchedule
  property_count: 1
  slug: grubhub-periodschedule
- name: PhoneBridge
  property_count: 3
  slug: grubhub-phonebridge
- name: PhoneContactDetails
  property_count: 1
  slug: grubhub-phonecontactdetails
- name: PhysicalInfo
  property_count: 3
  slug: grubhub-physicalinfo
- name: PickedUp
  property_count: 0
  slug: grubhub-pickedup
- name: PickupInfo
  property_count: 5
  slug: grubhub-pickupinfo
- name: PickupLocation
  property_count: 9
  slug: grubhub-pickuplocation
- name: PickupVerification
  property_count: 0
  slug: grubhub-pickupverification
- name: PickupVerificationDetails
  property_count: 5
  slug: grubhub-pickupverificationdetails
- name: PosAccountStatus
  property_count: 8
  slug: grubhub-posaccountstatus
- name: PosBulkScheduleOverrideStatus
  property_count: 6
  slug: grubhub-posbulkscheduleoverridestatus
- name: PosBulkSupplementalTagStatus
  property_count: 6
  slug: grubhub-posbulksupplementaltagstatus
- name: PosBusyInterval
  property_count: 5
  slug: grubhub-posbusyinterval
- name: PosBusyModeRequest
  property_count: 3
  slug: grubhub-posbusymoderequest
- name: PosBusyModeResponse
  property_count: 5
  slug: grubhub-posbusymoderesponse
- name: PosCustomSchedule
  property_count: 4
  slug: grubhub-poscustomschedule
- name: PosDeleteScheduleOverride
  property_count: 2
  slug: grubhub-posdeletescheduleoverride
- name: PosDelivery
  property_count: 20
  slug: grubhub-posdelivery
- name: PosDeliveryFee
  property_count: 2
  slug: grubhub-posdeliveryfee
- name: PosEstimates
  property_count: 2
  slug: grubhub-posestimates
- name: PosEstimatesUpdateRequest
  property_count: 3
  slug: grubhub-posestimatesupdaterequest
- name: PosFullSchedule
  property_count: 11
  slug: grubhub-posfullschedule
- name: PosGetBusyModeResponse
  property_count: 2
  slug: grubhub-posgetbusymoderesponse
- name: PosItemScheduleOverrides
  property_count: 4
  slug: grubhub-positemscheduleoverrides
- name: PosMassScheduleOverride
  property_count: 7
  slug: grubhub-posmassscheduleoverride
- name: PosMerchantBatchOperationResponse
  property_count: 2
  slug: grubhub-posmerchantbatchoperationresponse
- name: PosMerchantBatchOperationStatus
  property_count: 4
  slug: grubhub-posmerchantbatchoperationstatus
- name: PosMerchantData
  property_count: 11
  slug: grubhub-posmerchantdata
- name: PosMerchantFulfillmentInfo
  property_count: 4
  slug: grubhub-posmerchantfulfillmentinfo
- name: PosMerchantIntegrationStatus
  property_count: 2
  slug: grubhub-posmerchantintegrationstatus
- name: PosMerchantRepeatingIntervalRequest
  property_count: 3
  slug: grubhub-posmerchantrepeatingintervalrequest
- name: PosMerchantRepeatingSchedule
  property_count: 6
  slug: grubhub-posmerchantrepeatingschedule
- name: PosModifierScheduleOverrides
  property_count: 4
  slug: grubhub-posmodifierscheduleoverrides
- name: PosNormalizedMenu
  property_count: 12
  slug: grubhub-posnormalizedmenu
- name: PosNormalizedMenuMedia
  property_count: 1
  slug: grubhub-posnormalizedmenumedia
- name: PosNormalizedMenuUpdateRequest
  property_count: 4
  slug: grubhub-posnormalizedmenuupdaterequest
- name: PosNormalizedMenuUpdateResult
  property_count: 1
  slug: grubhub-posnormalizedmenuupdateresult
- name: PosNormalizedMenuUpdateStatus
  property_count: 3
  slug: grubhub-posnormalizedmenuupdatestatus
- name: PosNormalizedMenuValidationResult
  property_count: 2
  slug: grubhub-posnormalizedmenuvalidationresult
- name: PosOrder
  property_count: 41
  slug: grubhub-posorder
- name: PosOrderCoupon
  property_count: 2
  slug: grubhub-posordercoupon
- name: PosOrderMerchantData
  property_count: 4
  slug: grubhub-posordermerchantdata
- name: PosScheduleOverride
  property_count: 9
  slug: grubhub-posscheduleoverride
- name: PosScheduleOverrideBaseRequest
  property_count: 5
  slug: grubhub-posscheduleoverridebaserequest
- name: PosScheduleOverrideBulkRequest
  property_count: 2
  slug: grubhub-posscheduleoverridebulkrequest
- name: PosScheduleOverrideMultiOperationResult
  property_count: 4
  slug: grubhub-posscheduleoverridemultioperationresult
- name: PosScheduleOverrideRequest
  property_count: 4
  slug: grubhub-posscheduleoverriderequest
- name: PosScheduleOverrides
  property_count: 3
  slug: grubhub-posscheduleoverrides
- name: PosSupplementalTagMultiOperationResult
  property_count: 4
  slug: grubhub-possupplementaltagmultioperationresult
- name: PosTaxTotal
  property_count: 3
  slug: grubhub-postaxtotal
- name: PosTestOrderRequest
  property_count: 3
  slug: grubhub-postestorderrequest
- name: PosUpdateRepeatingScheduleRequest
  property_count: 2
  slug: grubhub-posupdaterepeatingschedulerequest
- name: ProgressDeliveryRequest
  property_count: 2
  slug: grubhub-progressdeliveryrequest
- name: ProgressDeliveryResponse
  property_count: 1
  slug: grubhub-progressdeliveryresponse
- name: ProgressRefundRequest
  property_count: 4
  slug: grubhub-progressrefundrequest
- name: Promotion
  property_count: 3
  slug: grubhub-promotion
- name: ProofOfDelivery
  property_count: 0
  slug: grubhub-proofofdelivery
- name: Properties
  property_count: 1
  slug: grubhub-properties
- name: ProxyPhoneNumberRequest
  property_count: 1
  slug: grubhub-proxyphonenumberrequest
- name: ProxyPhoneNumberResponse
  property_count: 1
  slug: grubhub-proxyphonenumberresponse
- name: PublicApiError
  property_count: 2
  slug: grubhub-publicapierror
- name: QuantityAndWeightLineSubstitution
  property_count: 0
  slug: grubhub-quantityandweightlinesubstitution
- name: QuantityLineSubstitution
  property_count: 0
  slug: grubhub-quantitylinesubstitution
- name: Quote
  property_count: 6
  slug: grubhub-quote
- name: QuoteRequest
  property_count: 11
  slug: grubhub-quoterequest
- name: QuoteResponse
  property_count: 1
  slug: grubhub-quoteresponse
- name: ReferralResponse
  property_count: 2
  slug: grubhub-referralresponse
- name: ReferralSignup
  property_count: 12
  slug: grubhub-referralsignup
- name: RefundAmount
  property_count: 4
  slug: grubhub-refundamount
- name: RefundRequest
  property_count: 3
  slug: grubhub-refundrequest
- name: RemoveLineSubstitution
  property_count: 0
  slug: grubhub-removelinesubstitution
- name: RepeatingSchedule
  property_count: 4
  slug: grubhub-repeatingschedule
- name: RepeatingScheduleMetadata
  property_count: 7
  slug: grubhub-repeatingschedulemetadata
- name: RepeatingScheduleRule
  property_count: 3
  slug: grubhub-repeatingschedulerule
- name: RepeatingScheduleRuleInterval
  property_count: 2
  slug: grubhub-repeatingscheduleruleinterval
- name: ReplaceLineSubstitution
  property_count: 0
  slug: grubhub-replacelinesubstitution
- name: ReportRequestParametersByPartner
  property_count: 1
  slug: grubhub-reportrequestparametersbypartner
- name: ResponseWrapperAcceptQuoteResponse
  property_count: 2
  slug: grubhub-responsewrapperacceptquoteresponse
- name: ResponseWrapperDeliveryStatusResponse
  property_count: 2
  slug: grubhub-responsewrapperdeliverystatusresponse
- name: ResponseWrapperProgressDeliveryResponse
  property_count: 2
  slug: grubhub-responsewrapperprogressdeliveryresponse
- name: ResponseWrapperProxyPhoneNumberResponse
  property_count: 2
  slug: grubhub-responsewrapperproxyphonenumberresponse
- name: ResponseWrapperQuoteResponse
  property_count: 2
  slug: grubhub-responsewrapperquoteresponse
- name: ResponseWrapperServiceAreaResponse
  property_count: 2
  slug: grubhub-responsewrapperservicearearesponse
- name: RestaurantVersionId
  property_count: 1
  slug: grubhub-restaurantversionid
- name: ReturnArrived
  property_count: 0
  slug: grubhub-returnarrived
- name: ReturnCompleted
  property_count: 0
  slug: grubhub-returncompleted
- name: ReturnInitiated
  property_count: 0
  slug: grubhub-returninitiated
- name: Reward
  property_count: 3
  slug: grubhub-reward
- name: ScheduledOrdersUpdateRequest
  property_count: 1
  slug: grubhub-scheduledordersupdaterequest
- name: ScheduleOverride
  property_count: 3
  slug: grubhub-scheduleoverride
- name: ScheduleOverrideMetadata
  property_count: 7
  slug: grubhub-scheduleoverridemetadata
- name: ServiceAreaResponse
  property_count: 1
  slug: grubhub-servicearearesponse
- name: Size
  property_count: 5
  slug: grubhub-size
- name: SizedPrice
  property_count: 5
  slug: grubhub-sizedprice
- name: SizePrompt
  property_count: 4
  slug: grubhub-sizeprompt
- name: StatusUpdate
  property_count: 5
  slug: grubhub-statusupdate
- name: StatusUpdateRequestPayload
  property_count: 10
  slug: grubhub-statusupdaterequestpayload
- name: SubItem
  property_count: 3
  slug: grubhub-subitem
- name: SubItemLineSubstitution
  property_count: 0
  slug: grubhub-subitemlinesubstitution
- name: SubstitutionAdjustment
  property_count: 1
  slug: grubhub-substitutionadjustment
- name: SubstitutionRequest
  property_count: 3
  slug: grubhub-substitutionrequest
- name: Tag
  property_count: 2
  slug: grubhub-tag
- name: TagProductsRequest
  property_count: 1
  slug: grubhub-tagproductsrequest
- name: TaxCategory
  property_count: 1
  slug: grubhub-taxcategory
- name: Taxes
  property_count: 10
  slug: grubhub-taxes
- name: TaxRate
  property_count: 4
  slug: grubhub-taxrate
- name: ThresholdSettings
  property_count: 2
  slug: grubhub-thresholdsettings
- name: TimePreferences
  property_count: 2
  slug: grubhub-timepreferences
- name: Tip
  property_count: 2
  slug: grubhub-tip
- name: TotalSubstitutionAdjustment
  property_count: 0
  slug: grubhub-totalsubstitutionadjustment
- name: Triage
  property_count: 2
  slug: grubhub-triage
- name: Unassigned
  property_count: 0
  slug: grubhub-unassigned
- name: UpdateDeliveryDropoffLocationRequest
  property_count: 2
  slug: grubhub-updatedeliverydropofflocationrequest
- name: Vehicle
  property_count: 2
  slug: grubhub-vehicle
jsonld:
- class_count: 0
  name: Grubhub Context
  property_count: 7
  slug: grubhub-context
layout: provider
modified: '2026-09-17'
name: Grubhub
nav: Providers
network: true
overview: 'Grubhub publishes 12 APIs on the [APIs.io](https://apis.io/) network, including Menu API, Orders API, Merchant Data API, and 9 more. Tagged areas include Food Delivery, Restaurant, Marketplace, Online Ordering, and Point-of-Sale.


  The Grubhub catalog on APIs.io includes 4 event-driven AsyncAPI specifications, 1 JSON-LD context, and 3 Spectral governance rulesets.


  Grubhub''s developer surface includes documentation, API reference, getting-started guide, support, pricing, signup flow, engineering blog, and 34 more developer resources.'
plans:
- name: Grubhub Plans Pricing
  plan_count: 4
  slug: grubhub-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 3
  name: Grubhub Rate Limits
  slug: grubhub-rate-limits
rules:
- effective_rule_count: 36
  extends:
  - spectral:asyncapi
  name: Grubhub API Rules
  rule_count: 9
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 8
  slug: grubhub-asyncapi-spectral-rules
- effective_rule_count: 6
  extends: []
  name: Grubhub API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: grubhub-jsonschema-spectral-rules
- effective_rule_count: 92
  extends:
  - spectral:oas
  name: Grubhub API Rules
  rule_count: 51
  severity_counts:
    error: 8
    hint: 0
    info: 14
    warn: 29
  slug: grubhub-spectral-rules
scopes:
- name: Grubhub Scopes
  scope_count: 2
  slug: grubhub-scopes
  summary_line: 2 scopes
score:
  band: exemplar
  composite: 67.7
  coverage:
    artifact_dirs: 28
    catalog_earned: 81.5
    catalog_earned_first_party: 24.0
    catalog_gap: 33.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 30.4
  facets:
    access_clarity: 84.2
    contract_governance: 47.0
    contract_quality: 59.5
    developer_ergonomics: 56.5
    discoverability: 81.5
    operational_transparency: 42.1
  previous_composite: 37.3
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 12
    mcp: derived
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-17'
  trend: rising
  upsert:
    applies: true
    score: 61.1
screenshot: https://raw.githubusercontent.com/api-evangelist/grubhub/refs/heads/main/screenshots/grubhub-2026-06-20T182426.png
security:
- kind: authentication
  name: Grubhub Authentication
  slug: grubhub-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Grubhub Domain Security
  slug: grubhub-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: grubhub
tags:
- Food Delivery
- Restaurant
- Marketplace
- Online Ordering
- Point-of-Sale
- Logistics
- Last Mile Delivery
- Menu Management
- Hospitality
- Local Commerce
website: https://www.grubhub.com
---
