---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: verified
    mcp_server: verified
    openapi_examples: partial
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 63.3
  scored_at: '2026-09-24'
agentic_access:
- acting_count: 64
  human_in_the_loop: 0
  name: Amazon Seller Central Agentic Access
  operation_count: 152
  slug: amazon-seller-central-agentic-access
  summary_line: 152 operations · 64 acting
api_count: 21
apis:
- description: REST API that lets approved developers and sellers manage Amazon Selling Partner accounts including catalog items, listings, orders, shipments, inventory, pricing, fees, reports, feeds, finances, noti
  name: Amazon Selling Partner API (SP-API)
  slug: sp-api
- baseURL: https://sellingpartnerapi-na.amazon.com
  baseurl_source: declared
  description: The Catalog API from Amazon Selling Partner API — 2 operation(s) for catalog.
  name: Amazon Selling Partner API Catalog API
  slug: amazon-seller-central-catalog-api
- baseURL: https://sellingpartnerapi-na.amazon.com
  baseurl_source: declared
  description: The Feeds API from Amazon Selling Partner API — 1 operation(s) for feeds.
  name: Amazon Selling Partner API Feeds API
  slug: amazon-seller-central-feeds-api
- baseURL: https://sellingpartnerapi-na.amazon.com
  baseurl_source: declared
  description: The Finances API from Amazon Selling Partner API — 1 operation(s) for finances.
  name: Amazon Selling Partner API Finances API
  slug: amazon-seller-central-finances-api
- baseURL: https://sellingpartnerapi-na.amazon.com
  baseurl_source: declared
  description: The Listings API from Amazon Selling Partner API — 1 operation(s) for listings.
  name: Amazon Selling Partner API Listings API
  slug: amazon-seller-central-listings-api
- baseURL: https://sellingpartnerapi-na.amazon.com
  baseurl_source: declared
  description: The Notifications API from Amazon Selling Partner API — 1 operation(s) for notifications.
  name: Amazon Selling Partner API Notifications API
  slug: amazon-seller-central-notifications-api
- baseURL: https://sellingpartnerapi-na.amazon.com
  baseurl_source: declared
  description: The Reports API from Amazon Selling Partner API — 2 operation(s) for reports.
  name: Amazon Selling Partner API Reports API
  slug: amazon-seller-central-reports-api
- baseURL: https://sellingpartnerapi-na.amazon.com
  baseurl_source: declared
  description: The Shipping API from Amazon Selling Partner API — 1 operation(s) for shipping.
  name: Amazon Selling Partner API Shipping API
  slug: amazon-seller-central-shipping-api
- baseURL: https://sellingpartnerapi-na.amazon.com
  baseurl_source: declared
  description: The Tokens API from Amazon Selling Partner API — 1 operation(s) for tokens.
  name: Amazon Selling Partner API Tokens API
  slug: amazon-seller-central-tokens-api
- baseURL: https://sellingpartnerapi-na.amazon.com
  baseurl_source: declared
  description: The definitions API from Amazon Selling Partner API — 2 operation(s) for definitions.
  name: Amazon Selling Partner API Definitions API
  slug: amazon-seller-central-definitions-api
- baseURL: https://sellingpartnerapi-na.amazon.com
  baseurl_source: declared
  description: The fbaInbound API from Amazon Selling Partner API — 36 operation(s) for fbainbound.
  name: Amazon Selling Partner API Fba Inbound API
  slug: amazon-seller-central-fbainbound-api
- baseURL: https://sellingpartnerapi-na.amazon.com
  baseurl_source: declared
  description: The fbaInventory API from Amazon Selling Partner API — 4 operation(s) for fbainventory.
  name: Amazon Selling Partner API Fba Inventory API
  slug: amazon-seller-central-fbainventory-api
- baseURL: https://sellingpartnerapi-na.amazon.com
  baseurl_source: declared
  description: The fbaOutbound API from Amazon Selling Partner API — 12 operation(s) for fbaoutbound.
  name: Amazon Selling Partner API Fba Outbound API
  slug: amazon-seller-central-fbaoutbound-api
- baseURL: https://sellingpartnerapi-na.amazon.com
  baseurl_source: declared
  description: The fees API from Amazon Selling Partner API — 3 operation(s) for fees.
  name: Amazon Selling Partner API Fees API
  slug: amazon-seller-central-fees-api
- baseURL: https://sellingpartnerapi-na.amazon.com
  baseurl_source: declared
  description: The getOrder API from Amazon Selling Partner API — 1 operation(s) for getorder.
  name: Amazon Selling Partner API Get Order API
  slug: amazon-seller-central-getorder-api
- baseURL: https://sellingpartnerapi-na.amazon.com
  baseurl_source: declared
  description: The ordersV0 API from Amazon Selling Partner API — 8 operation(s) for ordersv0.
  name: Amazon Selling Partner API Orders V0 API
  slug: amazon-seller-central-ordersv0-api
- baseURL: https://sellingpartnerapi-na.amazon.com
  baseurl_source: declared
  description: The productPricing API from Amazon Selling Partner API — 8 operation(s) for productpricing.
  name: Amazon Selling Partner API Product Pricing API
  slug: amazon-seller-central-productpricing-api
- baseURL: https://sellingpartnerapi-na.amazon.com
  baseurl_source: declared
  description: The sales API from Amazon Selling Partner API — 1 operation(s) for sales.
  name: Amazon Selling Partner API Sales API
  slug: amazon-seller-central-sales-api
- baseURL: https://sellingpartnerapi-na.amazon.com
  baseurl_source: declared
  description: The searchOrders API from Amazon Selling Partner API — 1 operation(s) for searchorders.
  name: Amazon Selling Partner API Search Orders API
  slug: amazon-seller-central-searchorders-api
- baseURL: https://sellingpartnerapi-na.amazon.com
  baseurl_source: declared
  description: The sellers API from Amazon Selling Partner API — 2 operation(s) for sellers.
  name: Amazon Selling Partner API Sellers API
  slug: amazon-seller-central-sellers-api
- baseURL: https://sellingpartnerapi-na.amazon.com
  baseurl_source: declared
  description: The shipment API from Amazon Selling Partner API — 1 operation(s) for shipment.
  name: Amazon Selling Partner API Shipment API
  slug: amazon-seller-central-shipment-api
- description: Amazon's first-party remote MCP server for Seller Central (streamable HTTP), announced at Amazon Accelerate on 2026-09-23 and in beta for US stores. Sellers authorize access through the Seller Central
  name: Amazon Selling Partner Connector (MCP)
  slug: selling-partner-connector-mcp
artifact_total: 127
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Selling Partner API for Items Catalog API
  slug: open-amazon-seller-central-catalog-api
- collection_type: open
  name: Selling Partner API for Product Type Definitions API
  slug: open-amazon-seller-central-definitions-api
- collection_type: open
  name: Selling Partner API for operations. Fba Inbound API
  slug: open-amazon-seller-central-fbainbound-api
- collection_type: open
  name: Selling Partner Fba Inventory API
  slug: open-amazon-seller-central-fbainventory-api
- collection_type: open
  name: Selling Partner APIs for Fulfillment Outbound Fba Outbound API
  slug: open-amazon-seller-central-fbaoutbound-api
- collection_type: open
  name: Selling Partner Feeds API
  slug: open-amazon-seller-central-feeds-api
- collection_type: open
  name: Selling Partner API for Product Fees API
  slug: open-amazon-seller-central-fees-api
- collection_type: open
  name: Amazon Seller Central Finances API
  slug: open-amazon-seller-central-finances-api
- collection_type: open
  name: Selling Partner API for Orders Get Order API
  slug: open-amazon-seller-central-getorder-api
- collection_type: open
  name: Amazon Seller Central Listings API
  slug: open-amazon-seller-central-listings-api
- collection_type: open
  name: Selling Partner Notifications API
  slug: open-amazon-seller-central-notifications-api
- collection_type: open
  name: Selling Partner API for Orders Orders V0 API
  slug: open-amazon-seller-central-ordersv0-api
- collection_type: open
  name: Amazon Seller Central Product Pricing API
  slug: open-amazon-seller-central-productpricing-api
- collection_type: open
  name: Selling Partner Reports API
  slug: open-amazon-seller-central-reports-api
- collection_type: open
  name: Selling Partner Sales API
  slug: open-amazon-seller-central-sales-api
- collection_type: open
  name: Selling Partner API for Orders Search Orders API
  slug: open-amazon-seller-central-searchorders-api
- collection_type: open
  name: Selling Partner Sellers API
  slug: open-amazon-seller-central-sellers-api
- collection_type: open
  name: Selling Partner API for Orders Shipment API
  slug: open-amazon-seller-central-shipment-api
- collection_type: open
  name: Amazon Shipping API
  slug: open-amazon-seller-central-shipping-api
- collection_type: open
  name: Selling Partner Tokens API
  slug: open-amazon-seller-central-tokens-api
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/amazon-seller-central/refs/heads/main/llms/amazon-seller-central-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/amazon-seller-central-llms.txt
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/amazon-seller-central/refs/heads/main/mcp/amazon-seller-central-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/amazon-seller-central-tool-crosswalk.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/amazon-seller-central/refs/heads/main/rules/amazon-seller-central-rules.yml
  title: ''
  type: Spectral
  url: rules/amazon-seller-central-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/amazon-seller-central/refs/heads/main/json-ld/amazon-seller-central-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/amazon-seller-central-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/amazon-seller-central/refs/heads/main/vocabulary/amazon-seller-central-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/amazon-seller-central-vocabulary.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/amazon-seller-central/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/amazon-seller-central/refs/heads/main/data-model/amazon-seller-central-data-model.yml
  title: ''
  type: DataModel
  url: data-model/amazon-seller-central-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/amazon-seller-central/refs/heads/main/conventions/amazon-seller-central-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/amazon-seller-central-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/amazon-seller-central/refs/heads/main/conventions/amazon-seller-central-conventions.yml
  title: ''
  type: Conventions
  url: conventions/amazon-seller-central-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/amazon-seller-central/refs/heads/main/errors/amazon-seller-central-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/amazon-seller-central-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/amazon-seller-central/refs/heads/main/conformance/amazon-seller-central-conformance.yml
  title: ''
  type: Conformance
  url: conformance/amazon-seller-central-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/amazon-seller-central/refs/heads/main/mcp/amazon-seller-central-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/amazon-seller-central-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/amazon-seller-central/refs/heads/main/well-known/amazon-seller-central-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/amazon-seller-central-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/amazon-seller-central/refs/heads/main/hosts/amazon-seller-central-hosts.yml
  title: ''
  type: Hosts
  url: hosts/amazon-seller-central-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/amazon-seller-central/refs/heads/main/vendors/amazon-seller-central-vendors.yml
  title: ''
  type: Vendors
  url: vendors/amazon-seller-central-vendors.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/amazon-seller-central/refs/heads/main/capabilities/amazon-seller-central-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/amazon-seller-central-capability-edges.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/amazon-seller-central/refs/heads/main/agentic-access/amazon-seller-central-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/amazon-seller-central-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/amazon-seller-central/refs/heads/main/security/amazon-seller-central-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/amazon-seller-central-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/amazon-seller-central/refs/heads/main/authentication/amazon-seller-central-authentication.yml
  title: ''
  type: Authentication
  url: authentication/amazon-seller-central-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://developer.amazonservices.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer-docs.amazon.com/sp-api
- group: commercial
  title: ''
  type: Pricing
  url: https://sell.amazon.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://sellercentral.amazon.com/
- group: agent
  title: ''
  type: LlmsText
  url: https://developer-docs.amazon.com/llms.txt
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/amazon-seller-central/refs/heads/main/webhooks/amazon-seller-central-notifications.yml
  title: ''
  type: Webhooks
  url: webhooks/amazon-seller-central-notifications.yml
- group: docs
  title: ''
  type: APIReference
  url: https://developer-docs.amazon.com/sp-api/reference
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer-docs.amazon.com/sp-api/changelog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/amzn
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/amzn/selling-partner-agentic-toolkit
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/amzn/selling-partner-api-models
created: '2026-05-11'
description: 'The Amazon Selling Partner API (SP-API) is the modern REST-based API that enables Amazon sellers, vendors, and third-party developers to programmatically access Seller Central data and operations including catalog management, orders, inventory, pricing, fulfillment, reports, finances, notifications, and advertising. SP-API uses Login with Amazon (LWA) OAuth 2.0 access tokens for authentication and replaces the legacy Amazon Marketplace Web Service (MWS). Since September 2026 Amazon also offers an agent surface: the Amazon Selling Partner Connector, a first-party remote MCP server at https://sellingpartner-ai.amazon.com/mcp (beta, US stores, Seller Central OAuth, write actions drafted for seller approval), and the Selling Partner Agentic Toolkit of provider-published Agent Skills.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/amazon-seller-central.png
json_schemas:
- name: AddInventoryRequest
  property_count: 1
  slug: amazon-seller-central-add-inventory-request
- name: AddInventoryResponse
  property_count: 1
  slug: amazon-seller-central-add-inventory-response
- name: CompetitiveSummaryBatchRequest
  property_count: 1
  slug: amazon-seller-central-competitive-summary-batch-request
- name: CompetitiveSummaryBatchResponse
  property_count: 1
  slug: amazon-seller-central-competitive-summary-batch-response
- name: ConfirmShipmentRequest
  property_count: 3
  slug: amazon-seller-central-confirm-shipment-request
- name: CreateClaimRequest
  property_count: 6
  slug: amazon-seller-central-create-claim-request
- name: CreateDestinationRequest
  property_count: 2
  slug: amazon-seller-central-create-destination-request
- name: CreateDestinationResponse
  property_count: 2
  slug: amazon-seller-central-create-destination-response
- name: CreateFeedDocumentResponse
  property_count: 2
  slug: amazon-seller-central-create-feed-document-response
- name: CreateFeedResponse
  property_count: 1
  slug: amazon-seller-central-create-feed-response
- name: CreateFeedSpecification
  property_count: 4
  slug: amazon-seller-central-create-feed-specification
- name: CreateFulfillmentOrderRequest
  property_count: 17
  slug: amazon-seller-central-create-fulfillment-order-request
- name: CreateFulfillmentReturnRequest
  property_count: 1
  slug: amazon-seller-central-create-fulfillment-return-request
- name: CreateInboundPlanRequest
  property_count: 4
  slug: amazon-seller-central-create-inbound-plan-request
- name: CreateInventoryItemRequest
  property_count: 3
  slug: amazon-seller-central-create-inventory-item-request
- name: CreateInventoryItemResponse
  property_count: 1
  slug: amazon-seller-central-create-inventory-item-response
- name: CreateMarketplaceItemLabelsRequest
  property_count: 7
  slug: amazon-seller-central-create-marketplace-item-labels-request
- name: CreateReportScheduleSpecification
  property_count: 5
  slug: amazon-seller-central-create-report-schedule-specification
- name: CreateReportSpecification
  property_count: 5
  slug: amazon-seller-central-create-report-specification
- name: CreateRestrictedDataTokenRequest
  property_count: 2
  slug: amazon-seller-central-create-restricted-data-token-request
- name: CreateRestrictedDataTokenResponse
  property_count: 2
  slug: amazon-seller-central-create-restricted-data-token-response
- name: CreateSubscriptionRequest
  property_count: 3
  slug: amazon-seller-central-create-subscription-request
- name: CreateSubscriptionResponse
  property_count: 2
  slug: amazon-seller-central-create-subscription-response
- name: DeleteInventoryItemResponse
  property_count: 1
  slug: amazon-seller-central-delete-inventory-item-response
- name: DirectPurchaseRequest
  property_count: 6
  slug: amazon-seller-central-direct-purchase-request
- name: FeedDocument
  property_count: 3
  slug: amazon-seller-central-feed-document
- name: Feed
  property_count: 8
  slug: amazon-seller-central-feed
- name: GenerateShipmentContentUpdatePreviewsRequest
  property_count: 2
  slug: amazon-seller-central-generate-shipment-content-update-previews-request
- name: GenerateTransportationOptionsRequest
  property_count: 2
  slug: amazon-seller-central-generate-transportation-options-request
- name: GetAccountResponse
  property_count: 2
  slug: amazon-seller-central-get-account-response
- name: GetFeaturedOfferExpectedPriceBatchRequest
  property_count: 1
  slug: amazon-seller-central-get-featured-offer-expected-price-batch-request
- name: GetFeaturedOfferExpectedPriceBatchResponse
  property_count: 1
  slug: amazon-seller-central-get-featured-offer-expected-price-batch-response
- name: GetFeedsResponse
  property_count: 2
  slug: amazon-seller-central-get-feeds-response
- name: GetFulfillmentPreviewRequest
  property_count: 7
  slug: amazon-seller-central-get-fulfillment-preview-request
- name: GetFulfillmentPreviewResponse
  property_count: 2
  slug: amazon-seller-central-get-fulfillment-preview-response
- name: GetInventorySummariesResponse
  property_count: 3
  slug: amazon-seller-central-get-inventory-summaries-response
- name: GetMarketplaceParticipationsResponse
  property_count: 2
  slug: amazon-seller-central-get-marketplace-participations-response
- name: GetMyFeesEstimateRequest
  property_count: 1
  slug: amazon-seller-central-get-my-fees-estimate-request
- name: GetMyFeesEstimateResponse
  property_count: 2
  slug: amazon-seller-central-get-my-fees-estimate-response
- name: GetMyFeesEstimatesRequest
  property_count: 0
  slug: amazon-seller-central-get-my-fees-estimates-request
- name: GetOffersResponse
  property_count: 2
  slug: amazon-seller-central-get-offers-response
- name: GetOrderAddressResponse
  property_count: 2
  slug: amazon-seller-central-get-order-address-response
- name: GetOrderBuyerInfoResponse
  property_count: 2
  slug: amazon-seller-central-get-order-buyer-info-response
- name: GetOrderItemsBuyerInfoResponse
  property_count: 2
  slug: amazon-seller-central-get-order-items-buyer-info-response
- name: GetOrderItemsResponse
  property_count: 2
  slug: amazon-seller-central-get-order-items-response
- name: GetOrderMetricsResponse
  property_count: 2
  slug: amazon-seller-central-get-order-metrics-response
- name: GetOrderRegulatedInfoResponse
  property_count: 2
  slug: amazon-seller-central-get-order-regulated-info-response
- name: GetOrderResponse
  property_count: 1
  slug: amazon-seller-central-get-order-response
- name: GetPricingResponse
  property_count: 2
  slug: amazon-seller-central-get-pricing-response
- name: GetRatesRequest
  property_count: 13
  slug: amazon-seller-central-get-rates-request
- name: GetReportsResponse
  property_count: 2
  slug: amazon-seller-central-get-reports-response
- name: GetSubscriptionByIdResponse
  property_count: 2
  slug: amazon-seller-central-get-subscription-by-id-response
- name: GetSubscriptionsResponse
  property_count: 2
  slug: amazon-seller-central-get-subscriptions-response
- name: InboundPlan
  property_count: 10
  slug: amazon-seller-central-inbound-plan
- name: Item
  property_count: 11
  slug: amazon-seller-central-item
- name: ItemSearchResults
  property_count: 4
  slug: amazon-seller-central-item-search-results
- name: LinkCarrierAccountRequest
  property_count: 4
  slug: amazon-seller-central-link-carrier-account-request
- name: ListAllFulfillmentOrdersResponse
  property_count: 2
  slug: amazon-seller-central-list-all-fulfillment-orders-response
- name: ListBalancesResponse
  property_count: 2
  slug: amazon-seller-central-list-balances-response
- name: ListFinancialEventGroupsResponse
  property_count: 2
  slug: amazon-seller-central-list-financial-event-groups-response
- name: ListFinancialEventsResponse
  property_count: 2
  slug: amazon-seller-central-list-financial-events-response
- name: ListTransactionsResponse
  property_count: 1
  slug: amazon-seller-central-list-transactions-response
- name: ListingsItemPatchRequest
  property_count: 2
  slug: amazon-seller-central-listings-item-patch-request
- name: ListingsItemPutRequest
  property_count: 3
  slug: amazon-seller-central-listings-item-put-request
- name: ListingsItemSubmissionResponse
  property_count: 5
  slug: amazon-seller-central-listings-item-submission-response
- name: OneClickShipmentRequest
  property_count: 13
  slug: amazon-seller-central-one-click-shipment-request
- name: ProductTypeDefinition
  property_count: 10
  slug: amazon-seller-central-product-type-definition
- name: ProductTypeList
  property_count: 2
  slug: amazon-seller-central-product-type-list
- name: PurchaseShipmentRequest
  property_count: 5
  slug: amazon-seller-central-purchase-shipment-request
- name: ReportDocument
  property_count: 3
  slug: amazon-seller-central-report-document
- name: ReportSchedule
  property_count: 6
  slug: amazon-seller-central-report-schedule
- name: Report
  property_count: 11
  slug: amazon-seller-central-report
- name: RestrictionList
  property_count: 1
  slug: amazon-seller-central-restriction-list
- name: SearchOrdersResponse
  property_count: 4
  slug: amazon-seller-central-search-orders-response
- name: Shipment
  property_count: 15
  slug: amazon-seller-central-shipment
- name: SummaryResponse
  property_count: 2
  slug: amazon-seller-central-summary-response
- name: UpdateFulfillmentOrderRequest
  property_count: 12
  slug: amazon-seller-central-update-fulfillment-order-request
- name: UpdateShipmentStatusRequest
  property_count: 3
  slug: amazon-seller-central-update-shipment-status-request
jsonld:
- class_count: 120
  name: Amazon Seller Central Context
  property_count: 200
  slug: amazon-seller-central-context
layout: provider
mcp_servers:
- description: 'Amazon''s first-party remote MCP server, the Amazon Selling Partner Connector, at https://sellingpartner-ai.amazon.com/mcp (streamable HTTP). Announced at Amazon Accelerate on 2026-09-23 alongside the '
  name: Amazon Selling Partner API MCP Server
  slug: amazon-selling-partner-api-mcp-server
modified: '2026-09-24'
name: Amazon Selling Partner API
nav: Providers
network: true
overview: 'Amazon Selling Partner API publishes 20 APIs on the [APIs.io](https://apis.io/) network, including Catalog API, Feeds API, Finances API, and 17 more. Tagged areas include E-Commerce, Marketplace, Selling Partner, Amazon, and Seller Central.


  The Amazon Selling Partner API catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Amazon Selling Partner API''s developer surface includes authentication, documentation, pricing, signup flow, API reference, changelog, and 24 more developer resources.'
random_paper: 16
rules:
- effective_rule_count: 58
  extends:
  - spectral:oas
  name: Amazon Selling Partner API API Rules
  rule_count: 17
  severity_counts:
    error: 14
    hint: 0
    info: 2
    warn: 1
  slug: amazon-seller-central-rules
score:
  band: developing
  composite: 47.1
  coverage:
    artifact_dirs: 23
    catalog_earned: 84.0
    catalog_earned_first_party: 0.0
    catalog_gap: 31.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 20.5
  facets:
    access_clarity: 23.7
    contract_governance: 87.9
    contract_quality: 61.3
    developer_ergonomics: 26.2
    discoverability: 81.5
    operational_transparency: 28.9
  previous_composite: 26.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 12
  schema_version: 0.22.0
  scored_at: '2026-09-24'
  trend: rising
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/amazon-seller-central/refs/heads/main/screenshots/amazon-seller-central-2026-06-20T171817.png
security:
- kind: authentication
  name: Amazon Seller Central Authentication
  slug: amazon-seller-central-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Amazon Seller Central Domain Security
  slug: amazon-seller-central-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: amazon-seller-central
tags:
- E-Commerce
- Marketplace
- Selling Partner
- Amazon
- Seller Central
- Catalog
- Order
- Inventory
- Fulfillment
- MCP
- Agent Skills
website: https://developer.amazonservices.com/
---
