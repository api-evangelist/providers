---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 16.5
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 33
  human_in_the_loop: 4
  name: Asendia Agentic Access
  operation_count: 50
  slug: asendia-agentic-access
  summary_line: 50 operations · 33 acting · 4 human-in-the-loop
api_count: 32
apis:
- baseURL: https://a1api.asendiausa.com
  baseurl_source: declared
  description: The CloseShipment API from Asendia — 2 operation(s) for closeshipment.
  name: Asendia Close Shipment API
  slug: asendia-closeshipment-api
- baseURL: https://a1api.asendiausa.com
  baseurl_source: declared
  description: The Consolidation API from Asendia — 1 operation(s) for consolidation.
  name: Asendia Consolidation API
  slug: asendia-consolidation-api
- baseURL: https://a1api.asendiausa.com
  baseurl_source: declared
  description: The DPDTracking API from Asendia — 1 operation(s) for dpdtracking.
  name: Asendia DPD Tracking API
  slug: asendia-dpdtracking-api
- baseURL: https://a1api.asendiausa.com
  baseurl_source: declared
  description: The DWS API from Asendia — 8 operation(s) for dws.
  name: Asendia DWS API
  slug: asendia-dws-api
- baseURL: https://a1api.asendiausa.com
  baseurl_source: declared
  description: The ExternalInvoiceImport API from Asendia — 1 operation(s) for externalinvoiceimport.
  name: Asendia External Invoice Import API
  slug: asendia-externalinvoiceimport-api
- baseURL: https://a1api.asendiausa.com
  baseurl_source: declared
  description: The Fulfillment API from Asendia — 4 operation(s) for fulfillment.
  name: Asendia Fulfillment API
  slug: asendia-fulfillment-api
- baseURL: https://a1api.asendiausa.com
  baseurl_source: declared
  description: The IDMailInterface API from Asendia — 3 operation(s) for idmailinterface.
  name: Asendia ID Mail Interface API
  slug: asendia-idmailinterface-api
- baseURL: https://a1api.asendiausa.com
  baseurl_source: declared
  description: The NPI API from Asendia — 2 operation(s) for npi.
  name: Asendia NPI API
  slug: asendia-npi-api
- baseURL: https://a1api.asendiausa.com
  baseurl_source: declared
  description: The Parcel API from Asendia — 4 operation(s) for parcel.
  name: Asendia Parcel API
  slug: asendia-parcel-api
- baseURL: https://a1api.asendiausa.com
  baseurl_source: declared
  description: The PudoLocator API from Asendia — 1 operation(s) for pudolocator.
  name: Asendia Pudo Locator API
  slug: asendia-pudolocator-api
- baseURL: https://a1api.asendiausa.com
  baseurl_source: declared
  description: The PutToLight API from Asendia — 2 operation(s) for puttolight.
  name: Asendia Put To Light API
  slug: asendia-puttolight-api
- baseURL: https://a1api.asendiausa.com
  baseurl_source: declared
  description: The ReceptacleSorting API from Asendia — 2 operation(s) for receptaclesorting.
  name: Asendia Receptacle Sorting API
  slug: asendia-receptaclesorting-api
- baseURL: https://a1api.asendiausa.com
  baseurl_source: declared
  description: The ServiceNow API from Asendia — 2 operation(s) for servicenow.
  name: Asendia Service Now API
  slug: asendia-servicenow-api
- baseURL: https://a1api.asendiausa.com
  baseurl_source: declared
  description: The ShippingPlatform API from Asendia — 6 operation(s) for shippingplatform.
  name: Asendia Shipping Platform API
  slug: asendia-shippingplatform-api
- baseURL: https://a1api.asendiausa.com
  baseurl_source: declared
  description: The ShippingPlatformBulk API from Asendia — 1 operation(s) for shippingplatformbulk.
  name: Asendia Shipping Platform Bulk API
  slug: asendia-shippingplatformbulk-api
- baseURL: https://a1api.asendiausa.com
  baseurl_source: declared
  description: The Tracking API from Asendia — 4 operation(s) for tracking.
  name: Asendia Tracking API
  slug: asendia-tracking-api
artifact_total: 70
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/asendia/refs/heads/main/agentic-access/asendia-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/asendia-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/asendia/refs/heads/main/rules/asendia-rules.yml
  title: ''
  type: Spectral
  url: rules/asendia-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/asendia/refs/heads/main/json-ld/asendia-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/asendia-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/asendia/refs/heads/main/vocabulary/asendia-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/asendia-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/asendia/refs/heads/main/data-model/asendia-data-model.yml
  title: ''
  type: DataModel
  url: data-model/asendia-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/asendia/refs/heads/main/conformance/asendia-conformance.yml
  title: ''
  type: Conformance
  url: conformance/asendia-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/asendia/refs/heads/main/llms/asendia-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/asendia-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/asendia/refs/heads/main/hosts/asendia-hosts.yml
  title: ''
  type: Hosts
  url: hosts/asendia-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/asendia/refs/heads/main/vendors/asendia-vendors.yml
  title: ''
  type: Vendors
  url: vendors/asendia-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/asendia/refs/heads/main/security/asendia-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/asendia-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.asendia.com
- group: docs
  title: ''
  type: Documentation
  url: https://a1api.asendiausa.com/swagger/index.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.asendia.com/privacy-notice
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.asendia.com/legal-notice
- group: company
  title: ''
  type: Newsroom
  url: https://www.asendia.com/media
- group: company
  title: ''
  type: Website
  url: https://www.asendiausa.com/
created: '2026-10-13'
description: Asendia is a global cross-border e-commerce shipping and international mail carrier, a joint venture between La Poste and Swiss Post. Its US arm, Asendia USA, publishes the A1 Web Services as public OpenAPI 3.0 documents (parcel, shipping platform, tracking, PUDO locator, fulfillment and more) at a1api.asendiausa.com; the Asendia Sync shipping platform (asendia-sync.com) exposes an API whose Swagger documentation requires authentication.
image: https://www.asendia.com/hubfs/Website%20Optimization%20Project/Consumer%20images/Asendia%20e-paq%20services%20view.jpg
json_schemas:
- name: BarcodeScan
  property_count: 4
  slug: asendia-barcode-scan
- name: BooleanApiResponse
  property_count: 2
  slug: asendia-boolean-api-response
- name: CloseBagRequest
  property_count: 4
  slug: asendia-close-bag-request
- name: closeShipmentRequest
  property_count: 1
  slug: asendia-close-shipment-request
- name: ConsolidationOrdersRequest
  property_count: 4
  slug: asendia-consolidation-orders-request
- name: ConsolidationOrdersResponseApiResponse
  property_count: 2
  slug: asendia-consolidation-orders-response-api-response
- name: CreateReceptacleResponse
  property_count: 2
  slug: asendia-create-receptacle-response
- name: CustomerAccountListApiResponse
  property_count: 2
  slug: asendia-customer-account-list-api-response
- name: CustomerContactListApiResponse
  property_count: 2
  slug: asendia-customer-contact-list-api-response
- name: deleteParcelRequest
  property_count: 3
  slug: asendia-delete-parcel-request
- name: ExternalInvoice
  property_count: 7
  slug: asendia-external-invoice
- name: FinishRunRequest
  property_count: 3
  slug: asendia-finish-run-request
- name: GenericPreProcessParcelRequest
  property_count: 9
  slug: asendia-generic-pre-process-parcel-request
- name: GenericPreProcessParcelResponseApiResponse
  property_count: 2
  slug: asendia-generic-pre-process-parcel-response-api-response
- name: getBinNumberResponseApiResponse
  property_count: 2
  slug: asendia-get-bin-number-response-api-response
- name: GetReceptacleResponse
  property_count: 2
  slug: asendia-get-receptacle-response
- name: getTrackingDetailResponse
  property_count: 2
  slug: asendia-get-tracking-detail-response
- name: getTrackingMilestoneResponse
  property_count: 2
  slug: asendia-get-tracking-milestone-response
- name: InsertProcessingEntryRequest
  property_count: 17
  slug: asendia-insert-processing-entry-request
- name: Int32ApiResponse
  property_count: 2
  slug: asendia-int32-api-response
- name: InventoryAdjustmentResponseListApiResponse
  property_count: 2
  slug: asendia-inventory-adjustment-response-list-api-response
- name: ItemReceiptApiResponse
  property_count: 2
  slug: asendia-item-receipt-api-response
- name: postCloseDAShipmentResponse
  property_count: 2
  slug: asendia-post-close-dashipment-response
- name: postCloseDirectShipmentDispatchRequest
  property_count: 10
  slug: asendia-post-close-direct-shipment-dispatch-request
- name: postCloseDispatchRequest
  property_count: 3
  slug: asendia-post-close-dispatch-request
- name: postCloseShipmentResponse
  property_count: 2
  slug: asendia-post-close-shipment-response
- name: postPackageBulkRequest
  property_count: 67
  slug: asendia-post-package-bulk-request
- name: postPackageRequest
  property_count: 66
  slug: asendia-post-package-request
- name: postPackageResponse
  property_count: 3
  slug: asendia-post-package-response
- name: postParcelResponse
  property_count: 9
  slug: asendia-post-parcel-response
- name: postPreAlertRequest
  property_count: 6
  slug: asendia-post-pre-alert-request
- name: postPreAlertRequestWithReceptacle
  property_count: 6
  slug: asendia-post-pre-alert-request-with-receptacle
- name: PostReceptacleApiModel
  property_count: 8
  slug: asendia-post-receptacle-api-model
- name: PreProcessParcelRequest
  property_count: 8
  slug: asendia-pre-process-parcel-request
- name: PudoLocatorResponseApiResponse
  property_count: 2
  slug: asendia-pudo-locator-response-api-response
- name: PurchaseOrder
  property_count: 5
  slug: asendia-purchase-order
- name: putBinCloseRequest
  property_count: 2
  slug: asendia-put-bin-close-request
- name: putPackageToBinRequest
  property_count: 5
  slug: asendia-put-package-to-bin-request
- name: ResponseSalesOrderApiResponse
  property_count: 2
  slug: asendia-response-sales-order-api-response
- name: responseStatus
  property_count: 2
  slug: asendia-response-status
- name: SalesOrder
  property_count: 14
  slug: asendia-sales-order
- name: StringApiResponse
  property_count: 2
  slug: asendia-string-api-response
- name: trackingDetailListApiResponse
  property_count: 2
  slug: asendia-tracking-detail-list-api-response
- name: trackingMilestoneListApiResponse
  property_count: 2
  slug: asendia-tracking-milestone-list-api-response
- name: TTEventsRequest
  property_count: 28
  slug: asendia-ttevents-request
- name: TTEventsResponseApiResponse
  property_count: 2
  slug: asendia-ttevents-response-api-response
- name: VitronicDataItemListApiResponse
  property_count: 2
  slug: asendia-vitronic-data-item-list-api-response
- name: VoidSalesOrder
  property_count: 3
  slug: asendia-void-sales-order
- name: VolumizerPreProcessParcelRequest
  property_count: 13
  slug: asendia-volumizer-pre-process-parcel-request
- name: VolumizerPreProcessParcelResponseApiResponse
  property_count: 2
  slug: asendia-volumizer-pre-process-parcel-response-api-response
jsonld:
- class_count: 120
  name: Asendia Context
  property_count: 457
  slug: asendia-context
layout: provider
modified: '2026-10-13'
name: Asendia
nav: Providers
network: true
overview: 'Asendia publishes 16 API contracts indexed on the [APIs.io](https://apis.io/) network, including Close Shipment API, Consolidation API, DPD Tracking API, and 13 more. Tagged areas include Company, Shipping, Logistics, Parcel, and Cross-border eCommerce.


  The Asendia catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Asendia''s developer surface includes documentation and 15 more developer resources.'
random_paper: 21
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: Asendia API Rules
  rule_count: 9
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 0
  slug: asendia-rules
score:
  band: thin
  composite: 28.9
  coverage:
    artifact_dirs: 15
    catalog_earned: 65.0
    catalog_earned_first_party: 0.0
    catalog_gap: 50.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 19.7
    contract_quality: 50.2
    developer_ergonomics: 9.5
    discoverability: 80.4
    operational_transparency: 0.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 16
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.6
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: domain-security
  name: Asendia Domain Security
  slug: asendia-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: asendia
tags:
- Company
- Shipping
- Logistics
- Parcel
- Cross-border eCommerce
- Tracking
- Postal
website: https://www.asendia.com
---
