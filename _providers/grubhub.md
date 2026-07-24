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
    agent_skills: false
    agentic_access: true
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 53.8
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 18
  human_in_the_loop: 3
  name: Grubhub Agentic Access
  operation_count: 35
  slug: grubhub-agentic-access
  summary_line: 35 operations · 18 acting · 3 human-in-the-loop
api_count: 17
apis:
- description: Endpoints for tracking delivery status, driver information, and estimated arrival times.
  name: grubhub Delivery Status API
  slug: grubhub-delivery-status-api
- description: Endpoints for establishing communication with delivery drivers through proxy phone numbers.
  name: grubhub Driver Communication API
  slug: grubhub-driver-communication-api
- description: Endpoints for reporting onboarding issues to Grubhub.
  name: grubhub Issue Reporting API
  slug: grubhub-issue-reporting-api
- description: Endpoints for uploading and managing normalized menus including schedules, sections, items, and modifiers.
  name: grubhub Menu Ingestion API
  slug: grubhub-menu-ingestion-api
- description: Endpoints for retrieving the current menu for a merchant.
  name: grubhub Menu Retrieval API
  slug: grubhub-menu-retrieval-api
- description: Endpoints for managing menu schedule overrides such as temporary availability changes.
  name: grubhub Menu Schedule Overrides API
  slug: grubhub-menu-schedule-overrides-api
- description: Endpoints for checking merchant eligibility for onboarding.
  name: grubhub Merchant Eligibility API
  slug: grubhub-merchant-eligibility-api
- description: Endpoints for onboarding merchants to the Grubhub platform, including referrals, activation, and association.
  name: grubhub Merchant Onboarding API
  slug: grubhub-merchant-onboarding-api
- description: Endpoints for updating merchant properties such as fulfillment settings and tax rates.
  name: grubhub Merchant Properties API
  slug: grubhub-merchant-properties-api
- description: Endpoints for managing merchant online/offline status on Grubhub, including soft and hard pauses.
  name: grubhub Merchant Status API
  slug: grubhub-merchant-status-api
- description: Endpoints for retrieving merchant information and ID mappings.
  name: grubhub Merchants API
  slug: grubhub-merchants-api
- description: Endpoints for managing order change requests and modifications.
  name: grubhub Order Change Requests API
  slug: grubhub-order-change-requests-api
- description: Endpoints for polling orders across multiple merchants. Webhook subscription is the preferred method for receiving new orders.
  name: grubhub Order Polling API
  slug: grubhub-order-polling-api
- description: Endpoints for confirming orders and updating order lifecycle states.
  name: grubhub Order Status API
  slug: grubhub-order-status-api
- description: Endpoints for retrieving and managing orders placed through the Grubhub Marketplace.
  name: grubhub Orders API
  slug: grubhub-orders-api
- description: Endpoints for creating and managing temporary schedule overrides such as closures and holiday hours.
  name: grubhub Schedule Overrides API
  slug: grubhub-schedule-overrides-api
- description: Endpoints for retrieving and managing merchant operating hours for delivery, pickup, and catering.
  name: grubhub Schedules API
  slug: grubhub-schedules-api
artifact_total: 199
asyncapis:
- description: 'Event-driven interface for receiving real-time delivery status updates from Grubhub. Partners can subscribe to webhook notifications for delivery updates including driver assignment, courier location '
  name: Grubhub Delivery Events
  slug: grubhub-delivery-events-asyncapi
- description: Event-driven interface for receiving real-time order notifications from Grubhub. When a diner places an order, Grubhub monitors that order and sends notifications based on the current status. The webh
  name: Grubhub Order Events
  slug: grubhub-order-events-asyncapi
collections:
- collection_type: open
  name: Grubhub Deliveries API
  slug: open-grubhub-deliveries
- collection_type: open
  name: Grubhub Menu API
  slug: open-grubhub-menu
- collection_type: open
  name: Grubhub Merchant Data API
  slug: open-grubhub-merchant-data
- collection_type: open
  name: Grubhub Merchant Schedules API
  slug: open-grubhub-merchant-schedules
- collection_type: open
  name: Grubhub Onboarding API
  slug: open-grubhub-onboarding
- collection_type: open
  name: Grubhub Orders API
  slug: open-grubhub-orders
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/grubhub-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/grubhub-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/grubhub-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/grubhub-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/GrubhubProd
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/grubhub-seamless
- group: design
  title: ''
  type: JSONLD
  url: json-ld/grubhub-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/grubhub-order-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/grubhub-menu-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/grubhub-merchant-schema.json
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/grubhub-vocabulary.yml
- group: design
  title: ''
  type: Rules
  url: rules/grubhub-spectral-rules.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/grubhub-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/grubhub-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/grubhub-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://get.grubhub.com/blog/feed/
description: Grubhub works with brands, point of sale companies, and online ordering providers to power an ordering experience in Grubhub Marketplace and within restaurant-branded web experiences. This documentation describes the normalized endpoints required for ingesting menu content and facilitating order transmission.
examples:
- key_count: 6
  name: Grubhub Address Example
  slug: grubhub-address-example
- key_count: 3
  name: Grubhub Availability Example
  slug: grubhub-availability-example
- key_count: 1
  name: Grubhub Batchjobresponse Example
  slug: grubhub-batchjobresponse-example
- key_count: 3
  name: Grubhub Batchjobstatus Example
  slug: grubhub-batchjobstatus-example
- key_count: 3
  name: Grubhub Contact Example
  slug: grubhub-contact-example
- key_count: 8
  name: Grubhub Courierlocationpayload Example
  slug: grubhub-courierlocationpayload-example
- key_count: 3
  name: Grubhub Customer Example
  slug: grubhub-customer-example
- key_count: 2
  name: Grubhub Dayschedule Example
  slug: grubhub-dayschedule-example
- key_count: 7
  name: Grubhub Delivery Example
  slug: grubhub-delivery-example
- key_count: 5
  name: Grubhub Deliverycancelledpayload Example
  slug: grubhub-deliverycancelledpayload-example
- key_count: 7
  name: Grubhub Deliveryrefundpayload Example
  slug: grubhub-deliveryrefundpayload-example
- key_count: 7
  name: Grubhub Deliverystatuspayload Example
  slug: grubhub-deliverystatuspayload-example
- key_count: 5
  name: Grubhub Driver Example
  slug: grubhub-driver-example
- key_count: 7
  name: Grubhub Driverassignedpayload Example
  slug: grubhub-driverassignedpayload-example
- key_count: 3
  name: Grubhub Eligibilityresponse Example
  slug: grubhub-eligibilityresponse-example
- key_count: 3
  name: Grubhub Error Example
  slug: grubhub-error-example
- key_count: 6
  name: Grubhub Fulfillmentinfo Example
  slug: grubhub-fulfillmentinfo-example
- key_count: 1
  name: Grubhub Ingestionjobresponse Example
  slug: grubhub-ingestionjobresponse-example
- key_count: 3
  name: Grubhub Ingestionjobstatus Example
  slug: grubhub-ingestionjobstatus-example
- key_count: 2
  name: Grubhub Menu Example
  slug: grubhub-menu-example
- key_count: 7
  name: Grubhub Menuitem Example
  slug: grubhub-menuitem-example
- key_count: 4
  name: Grubhub Menuschedule Example
  slug: grubhub-menuschedule-example
- key_count: 1
  name: Grubhub Menuscheduleoverriderequest Example
  slug: grubhub-menuscheduleoverriderequest-example
- key_count: 3
  name: Grubhub Menusection Example
  slug: grubhub-menusection-example
- key_count: 11
  name: Grubhub Merchant Example
  slug: grubhub-merchant-example
- key_count: 1
  name: Grubhub Merchantactivationrequest Example
  slug: grubhub-merchantactivationrequest-example
- key_count: 1
  name: Grubhub Merchantassociationrequest Example
  slug: grubhub-merchantassociationrequest-example
- key_count: 2
  name: Grubhub Merchantdeactivationrequest Example
  slug: grubhub-merchantdeactivationrequest-example
- key_count: 4
  name: Grubhub Merchantmapping Example
  slug: grubhub-merchantmapping-example
- key_count: 1
  name: Grubhub Merchantpropertiesupdaterequest Example
  slug: grubhub-merchantpropertiesupdaterequest-example
- key_count: 5
  name: Grubhub Merchantreferral Example
  slug: grubhub-merchantreferral-example
- key_count: 1
  name: Grubhub Merchantstatusupdaterequest Example
  slug: grubhub-merchantstatusupdaterequest-example
- key_count: 4
  name: Grubhub Modifieroption Example
  slug: grubhub-modifieroption-example
- key_count: 6
  name: Grubhub Modifierprompt Example
  slug: grubhub-modifierprompt-example
- key_count: 3
  name: Grubhub Onboardingissue Example
  slug: grubhub-onboardingissue-example
- key_count: 14
  name: Grubhub Order Example
  slug: grubhub-order-example
- key_count: 6
  name: Grubhub Ordercancellationpayload Example
  slug: grubhub-ordercancellationpayload-example
- key_count: 5
  name: Grubhub Orderchangerequest Example
  slug: grubhub-orderchangerequest-example
- key_count: 7
  name: Grubhub Orderchangerequestpayload Example
  slug: grubhub-orderchangerequestpayload-example
- key_count: 1
  name: Grubhub Orderconfirmation Example
  slug: grubhub-orderconfirmation-example
- key_count: 6
  name: Grubhub Orderitem Example
  slug: grubhub-orderitem-example
- key_count: 2
  name: Grubhub Orderstatusupdate Example
  slug: grubhub-orderstatusupdate-example
- key_count: 6
  name: Grubhub Orderstatuswebhookpayload Example
  slug: grubhub-orderstatuswebhookpayload-example
- key_count: 5
  name: Grubhub Ordertotals Example
  slug: grubhub-ordertotals-example
- key_count: 10
  name: Grubhub Orderwebhookpayload Example
  slug: grubhub-orderwebhookpayload-example
- key_count: 2
  name: Grubhub Posnormalizedmenu Example
  slug: grubhub-posnormalizedmenu-example
- key_count: 2
  name: Grubhub Proxyphone Example
  slug: grubhub-proxyphone-example
- key_count: 3
  name: Grubhub Referralresponse Example
  slug: grubhub-referralresponse-example
- key_count: 6
  name: Grubhub Scheduleoverride Example
  slug: grubhub-scheduleoverride-example
- key_count: 5
  name: Grubhub Scheduleoverriderequest Example
  slug: grubhub-scheduleoverriderequest-example
- key_count: 3
  name: Grubhub Sizeoption Example
  slug: grubhub-sizeoption-example
- key_count: 3
  name: Grubhub Sizeprompt Example
  slug: grubhub-sizeprompt-example
- key_count: 2
  name: Grubhub Timewindow Example
  slug: grubhub-timewindow-example
- key_count: 7
  name: Grubhub Weeklyschedule Example
  slug: grubhub-weeklyschedule-example
finops:
- name: Grubhub Finops
  service_category: Food Delivery / Marketplaces
  slug: grubhub-finops
graphqls:
- description: This document describes a conceptual GraphQL schema for the Grubhub food delivery marketplace platform. Grubhub provides REST APIs for partners and merchants to manage menus, orders, deliveries, merch
  name: Grubhub GraphQL Schema
  slug: grubhub-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/grubhub.png
json_schemas:
- name: Address
  property_count: 6
  slug: grubhub-address
- name: Availability
  property_count: 3
  slug: grubhub-availability
- name: BatchJobResponse
  property_count: 1
  slug: grubhub-batchjobresponse
- name: BatchJobStatus
  property_count: 3
  slug: grubhub-batchjobstatus
- name: Contact
  property_count: 3
  slug: grubhub-contact
- name: Grubhub Courier Location Payload
  property_count: 8
  slug: grubhub-courierlocationpayload
- name: Customer
  property_count: 3
  slug: grubhub-customer
- name: DaySchedule
  property_count: 2
  slug: grubhub-dayschedule
- name: Delivery
  property_count: 7
  slug: grubhub-delivery
- name: Grubhub Delivery Cancelled Payload
  property_count: 5
  slug: grubhub-deliverycancelledpayload
- name: Grubhub Delivery Refund Payload
  property_count: 7
  slug: grubhub-deliveryrefundpayload
- name: Grubhub Delivery Status Payload
  property_count: 7
  slug: grubhub-deliverystatuspayload
- name: Driver
  property_count: 5
  slug: grubhub-driver
- name: Grubhub Driver Assigned Payload
  property_count: 7
  slug: grubhub-driverassignedpayload
- name: EligibilityResponse
  property_count: 3
  slug: grubhub-eligibilityresponse
- name: Error
  property_count: 3
  slug: grubhub-error
- name: FulfillmentInfo
  property_count: 6
  slug: grubhub-fulfillmentinfo
- name: IngestionJobResponse
  property_count: 1
  slug: grubhub-ingestionjobresponse
- name: IngestionJobStatus
  property_count: 3
  slug: grubhub-ingestionjobstatus
- name: Grubhub Normalized Menu
  property_count: 2
  slug: grubhub-menu
- name: MenuItem
  property_count: 7
  slug: grubhub-menuitem
- name: MenuSchedule
  property_count: 4
  slug: grubhub-menuschedule
- name: MenuScheduleOverrideRequest
  property_count: 1
  slug: grubhub-menuscheduleoverriderequest
- name: MenuSection
  property_count: 3
  slug: grubhub-menusection
- name: Grubhub Merchant
  property_count: 11
  slug: grubhub-merchant
- name: MerchantActivationRequest
  property_count: 1
  slug: grubhub-merchantactivationrequest
- name: MerchantAssociationRequest
  property_count: 1
  slug: grubhub-merchantassociationrequest
- name: MerchantDeactivationRequest
  property_count: 2
  slug: grubhub-merchantdeactivationrequest
- name: MerchantMapping
  property_count: 4
  slug: grubhub-merchantmapping
- name: MerchantPropertiesUpdateRequest
  property_count: 1
  slug: grubhub-merchantpropertiesupdaterequest
- name: MerchantReferral
  property_count: 5
  slug: grubhub-merchantreferral
- name: MerchantStatusUpdateRequest
  property_count: 1
  slug: grubhub-merchantstatusupdaterequest
- name: ModifierOption
  property_count: 4
  slug: grubhub-modifieroption
- name: ModifierPrompt
  property_count: 6
  slug: grubhub-modifierprompt
- name: OnboardingIssue
  property_count: 3
  slug: grubhub-onboardingissue
- name: Grubhub Order
  property_count: 14
  slug: grubhub-order
- name: Grubhub Order Cancellation Payload
  property_count: 6
  slug: grubhub-ordercancellationpayload
- name: OrderChangeRequest
  property_count: 5
  slug: grubhub-orderchangerequest
- name: Grubhub Order Change Request Payload
  property_count: 7
  slug: grubhub-orderchangerequestpayload
- name: OrderConfirmation
  property_count: 1
  slug: grubhub-orderconfirmation
- name: OrderItem
  property_count: 6
  slug: grubhub-orderitem
- name: OrderStatusUpdate
  property_count: 2
  slug: grubhub-orderstatusupdate
- name: Grubhub Order Status Webhook Payload
  property_count: 6
  slug: grubhub-orderstatuswebhookpayload
- name: OrderTotals
  property_count: 5
  slug: grubhub-ordertotals
- name: Grubhub Order Webhook Payload
  property_count: 10
  slug: grubhub-orderwebhookpayload
- name: PosNormalizedMenu
  property_count: 2
  slug: grubhub-posnormalizedmenu
- name: ProxyPhone
  property_count: 2
  slug: grubhub-proxyphone
- name: ReferralResponse
  property_count: 3
  slug: grubhub-referralresponse
- name: ScheduleOverride
  property_count: 6
  slug: grubhub-scheduleoverride
- name: ScheduleOverrideRequest
  property_count: 5
  slug: grubhub-scheduleoverriderequest
- name: SizeOption
  property_count: 3
  slug: grubhub-sizeoption
- name: SizePrompt
  property_count: 3
  slug: grubhub-sizeprompt
- name: TimeWindow
  property_count: 2
  slug: grubhub-timewindow
- name: WeeklySchedule
  property_count: 7
  slug: grubhub-weeklyschedule
json_structures:
- name: Grubhub Address Structure
  property_count: 6
  slug: grubhub-address-structure
- name: Grubhub Availability Structure
  property_count: 3
  slug: grubhub-availability-structure
- name: Grubhub Batchjobresponse Structure
  property_count: 1
  slug: grubhub-batchjobresponse-structure
- name: Grubhub Batchjobstatus Structure
  property_count: 3
  slug: grubhub-batchjobstatus-structure
- name: Grubhub Contact Structure
  property_count: 3
  slug: grubhub-contact-structure
- name: Grubhub Courierlocationpayload Structure
  property_count: 8
  slug: grubhub-courierlocationpayload-structure
- name: Grubhub Customer Structure
  property_count: 3
  slug: grubhub-customer-structure
- name: Grubhub Dayschedule Structure
  property_count: 2
  slug: grubhub-dayschedule-structure
- name: Grubhub Delivery Structure
  property_count: 7
  slug: grubhub-delivery-structure
- name: Grubhub Deliverycancelledpayload Structure
  property_count: 5
  slug: grubhub-deliverycancelledpayload-structure
- name: Grubhub Deliveryrefundpayload Structure
  property_count: 7
  slug: grubhub-deliveryrefundpayload-structure
- name: Grubhub Deliverystatuspayload Structure
  property_count: 7
  slug: grubhub-deliverystatuspayload-structure
- name: Grubhub Driver Structure
  property_count: 5
  slug: grubhub-driver-structure
- name: Grubhub Driverassignedpayload Structure
  property_count: 7
  slug: grubhub-driverassignedpayload-structure
- name: Grubhub Eligibilityresponse Structure
  property_count: 3
  slug: grubhub-eligibilityresponse-structure
- name: Grubhub Error Structure
  property_count: 3
  slug: grubhub-error-structure
- name: Grubhub Fulfillmentinfo Structure
  property_count: 6
  slug: grubhub-fulfillmentinfo-structure
- name: Grubhub Ingestionjobresponse Structure
  property_count: 1
  slug: grubhub-ingestionjobresponse-structure
- name: Grubhub Ingestionjobstatus Structure
  property_count: 3
  slug: grubhub-ingestionjobstatus-structure
- name: Grubhub Menu Structure
  property_count: 2
  slug: grubhub-menu-structure
- name: Grubhub Menuitem Structure
  property_count: 7
  slug: grubhub-menuitem-structure
- name: Grubhub Menuschedule Structure
  property_count: 4
  slug: grubhub-menuschedule-structure
- name: Grubhub Menuscheduleoverriderequest Structure
  property_count: 1
  slug: grubhub-menuscheduleoverriderequest-structure
- name: Grubhub Menusection Structure
  property_count: 3
  slug: grubhub-menusection-structure
- name: Grubhub Merchant Structure
  property_count: 11
  slug: grubhub-merchant-structure
- name: Grubhub Merchantactivationrequest Structure
  property_count: 1
  slug: grubhub-merchantactivationrequest-structure
- name: Grubhub Merchantassociationrequest Structure
  property_count: 1
  slug: grubhub-merchantassociationrequest-structure
- name: Grubhub Merchantdeactivationrequest Structure
  property_count: 2
  slug: grubhub-merchantdeactivationrequest-structure
- name: Grubhub Merchantmapping Structure
  property_count: 4
  slug: grubhub-merchantmapping-structure
- name: Grubhub Merchantpropertiesupdaterequest Structure
  property_count: 1
  slug: grubhub-merchantpropertiesupdaterequest-structure
- name: Grubhub Merchantreferral Structure
  property_count: 5
  slug: grubhub-merchantreferral-structure
- name: Grubhub Merchantstatusupdaterequest Structure
  property_count: 1
  slug: grubhub-merchantstatusupdaterequest-structure
- name: Grubhub Modifieroption Structure
  property_count: 4
  slug: grubhub-modifieroption-structure
- name: Grubhub Modifierprompt Structure
  property_count: 6
  slug: grubhub-modifierprompt-structure
- name: Grubhub Onboardingissue Structure
  property_count: 3
  slug: grubhub-onboardingissue-structure
- name: Grubhub Order Structure
  property_count: 14
  slug: grubhub-order-structure
- name: Grubhub Ordercancellationpayload Structure
  property_count: 6
  slug: grubhub-ordercancellationpayload-structure
- name: Grubhub Orderchangerequest Structure
  property_count: 5
  slug: grubhub-orderchangerequest-structure
- name: Grubhub Orderchangerequestpayload Structure
  property_count: 7
  slug: grubhub-orderchangerequestpayload-structure
- name: Grubhub Orderconfirmation Structure
  property_count: 1
  slug: grubhub-orderconfirmation-structure
- name: Grubhub Orderitem Structure
  property_count: 6
  slug: grubhub-orderitem-structure
- name: Grubhub Orderstatusupdate Structure
  property_count: 2
  slug: grubhub-orderstatusupdate-structure
- name: Grubhub Orderstatuswebhookpayload Structure
  property_count: 6
  slug: grubhub-orderstatuswebhookpayload-structure
- name: Grubhub Ordertotals Structure
  property_count: 5
  slug: grubhub-ordertotals-structure
- name: Grubhub Orderwebhookpayload Structure
  property_count: 10
  slug: grubhub-orderwebhookpayload-structure
- name: Grubhub Posnormalizedmenu Structure
  property_count: 2
  slug: grubhub-posnormalizedmenu-structure
- name: Grubhub Proxyphone Structure
  property_count: 2
  slug: grubhub-proxyphone-structure
- name: Grubhub Referralresponse Structure
  property_count: 3
  slug: grubhub-referralresponse-structure
- name: Grubhub Scheduleoverride Structure
  property_count: 6
  slug: grubhub-scheduleoverride-structure
- name: Grubhub Scheduleoverriderequest Structure
  property_count: 5
  slug: grubhub-scheduleoverriderequest-structure
- name: Grubhub Sizeoption Structure
  property_count: 3
  slug: grubhub-sizeoption-structure
- name: Grubhub Sizeprompt Structure
  property_count: 3
  slug: grubhub-sizeprompt-structure
- name: Grubhub Timewindow Structure
  property_count: 2
  slug: grubhub-timewindow-structure
- name: Grubhub Weeklyschedule Structure
  property_count: 7
  slug: grubhub-weeklyschedule-structure
jsonld:
- class_count: 0
  name: Grubhub Context
  property_count: 7
  slug: grubhub-context
layout: provider
modified: '2026-05-19'
name: grubhub
nav: Providers
network: true
overview: 'grubhub publishes 17 APIs on the [APIs.io](https://apis.io/) network, including Delivery Status API, Driver Communication API, Issue Reporting API, and 14 more.


  The grubhub catalog on APIs.io includes 2 event-driven AsyncAPI specifications, 1 JSON-LD context, and 3 Spectral governance rulesets.


  grubhub''s developer surface includes authentication, engineering blog, and 14 more developer resources.'
plans:
- name: Grubhub Plans Pricing
  plan_count: 4
  slug: grubhub-plans-pricing
random_paper: 37
rate_limits:
- limit_count: 3
  name: Grubhub Rate Limits
  slug: grubhub-rate-limits
rules:
- name: grubhub API Rules
  rule_count: 9
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 8
  slug: grubhub-asyncapi-spectral-rules
- name: grubhub API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: grubhub-jsonschema-spectral-rules
- name: grubhub API Rules
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
  summary_line: 2 scopes · clientCredentials
score:
  band: developing
  composite: 48.4
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 78.8
    developer_ergonomics: 13.0
    discoverability: 55.0
    governance: 65.8
    operational_transparency: 36.8
  previous_composite: 48.4
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/grubhub/refs/heads/main/screenshots/grubhub-2026-06-20T182426.png
security:
- kind: authentication
  name: Grubhub Authentication
  slug: grubhub-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Grubhub Domain Security
  slug: grubhub-domain-security
  summary_line: TLSv1.3 · DMARC
slug: grubhub
---
