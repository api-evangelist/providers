---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.9
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 11
  human_in_the_loop: 0
  name: Coyote Agentic Access
  operation_count: 22
  slug: coyote-agentic-access
  summary_line: 22 operations · 11 acting
api_count: 9
apis:
- description: The primary REST API for Coyote Logistics enabling shippers and carriers to integrate freight operations directly into their TMS, WMS, ERP, or accounting systems. Provides real-time freight quotes for
  name: CoyoteGO API
  slug: coyotego-api
- description: The Associated Entities API API from Coyote Logistics — 1 operation(s) for associated entities api.
  name: Coyote Logistics Associated Entities API API
  slug: coyote-associated-entities-api-api
- description: The Carrier - Available Load APIs API from Coyote Logistics — 2 operation(s) for carrier - available load apis.
  name: Coyote Logistics Carrier - Available Load APIs API
  slug: coyote-carrier-available-load-apis-api
- description: The Carrier - Booking APIs API from Coyote Logistics — 2 operation(s) for carrier - booking apis.
  name: Coyote Logistics Carrier - Booking APIs API
  slug: coyote-carrier-booking-apis-api
- description: The Carrier - Offer APIs API from Coyote Logistics — 4 operation(s) for carrier - offer apis.
  name: Coyote Logistics Carrier - Offer APIs API
  slug: coyote-carrier-offer-apis-api
- description: The Document APIs API from Coyote Logistics — 2 operation(s) for document apis.
  name: Coyote Logistics Document APIs API
  slug: coyote-document-apis-api
- description: The Shipper - Quoting APIs API from Coyote Logistics — 2 operation(s) for shipper - quoting apis.
  name: Coyote Logistics Shipper - Quoting APIs API
  slug: coyote-shipper-quoting-apis-api
- description: The Shipper - Shipment APIs API from Coyote Logistics — 4 operation(s) for shipper - shipment apis.
  name: Coyote Logistics Shipper - Shipment APIs API
  slug: coyote-shipper-shipment-apis-api
- description: The Shipper - Tracking APIs API from Coyote Logistics — 4 operation(s) for shipper - tracking apis.
  name: Coyote Logistics Shipper - Tracking APIs API
  slug: coyote-shipper-tracking-apis-api
artifact_total: 136
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/coyote-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/coyote-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://coyote.com/
- group: docs
  title: ''
  type: Documentation
  url: https://api2-dev.coyote.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/coyote-team
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/coyote-logistics
- group: company
  title: ''
  type: Blog
  url: https://coyote.com/resources/
- group: commercial
  title: ''
  type: Pricing
  url: https://coyote.com/technology/
- group: operate
  title: ''
  type: StatusPage
  url: https://tracking.coyote.com/
- group: other
  title: ''
  type: X
  url: https://x.com/CoyoteLogistics
- group: commercial
  title: ''
  type: Plans
  url: plans/coyote-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/coyote-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/coyote-finops.yml
created: '2026-06-13'
description: Coyote Logistics is a global third-party logistics (3PL) provider and freight brokerage platform, now part of RXO, offering REST APIs for truckload capacity, less-than-truckload (LTL) shipping, freight quoting, shipment tracking, load management, customs brokerage, and supply chain visibility. Originally founded in 2006 and acquired by UPS in 2015, Coyote was subsequently acquired by RXO in 2024. The CoyoteGO API platform serves both shippers and carriers, providing real-time freight quotes, live tracking updates, and load booking capabilities. The API uses OAuth 2.0 client credentials flow and is backed by a network of 100,000 carriers serving 15,000 customers. Integration is available at no additional cost for shippers and carriers working with Coyote, with native connectors to leading TMS, WMS, and ERP systems.
examples:
- key_count: 2
  name: Get _Api_V1_Associatedentities Response 200
  slug: get-_api_v1_associatedentities-response-200
- key_count: 2
  name: Get _Api_V1_Availableloads_{Loadid} Response 200
  slug: get-_api_v1_availableloads_{loadid}-response-200
- key_count: 2
  name: Get _Api_V1_Documents_{Loadid}_{Documenttype} Response 200
  slug: get-_api_v1_documents_{loadid}_{documenttype}-response-200
- key_count: 2
  name: Get _Api_V1_Loads_Search Response 200
  slug: get-_api_v1_loads_search-response-200
- key_count: 2
  name: Get _Api_V1_Loads_{Loadrequestid}_Buildstatus Response 200
  slug: get-_api_v1_loads_{loadrequestid}_buildstatus-response-200
- key_count: 2
  name: Get _Api_V1_Locationstatuses_{Loadid} Response 200
  slug: get-_api_v1_locationstatuses_{loadid}-response-200
- key_count: 2
  name: Get _Api_V1_Locationstatuses_{Loadid}_Latest Response 200
  slug: get-_api_v1_locationstatuses_{loadid}_latest-response-200
- key_count: 2
  name: Get _Api_V1_Offer_{Id} Response 200
  slug: get-_api_v1_offer_{id}-response-200
- key_count: 2
  name: Get _Api_V1_Trackings_{Loadid}_Stopdetails Response 200
  slug: get-_api_v1_trackings_{loadid}_stopdetails-response-200
- key_count: 2
  name: Get _Api_V1_Trackings_{Loadid}_Summaries Response 200
  slug: get-_api_v1_trackings_{loadid}_summaries-response-200
- key_count: 2
  name: Post _Api_V1_Availableloads_Search Request
  slug: post-_api_v1_availableloads_search-request
- key_count: 2
  name: Post _Api_V1_Availableloads_Search Response 200
  slug: post-_api_v1_availableloads_search-response-200
- key_count: 2
  name: Post _Api_V1_Booking Request
  slug: post-_api_v1_booking-request
- key_count: 2
  name: Post _Api_V1_Booking Response 200
  slug: post-_api_v1_booking-response-200
- key_count: 2
  name: Post _Api_V1_Booking Response 409
  slug: post-_api_v1_booking-response-409
- key_count: 2
  name: Post _Api_V1_Documents Request
  slug: post-_api_v1_documents-request
- key_count: 2
  name: Post _Api_V1_Loads Request
  slug: post-_api_v1_loads-request
- key_count: 2
  name: Post _Api_V1_Loads Response 200
  slug: post-_api_v1_loads-response-200
- key_count: 2
  name: Post _Api_V1_Ltlspotquotes Request
  slug: post-_api_v1_ltlspotquotes-request
- key_count: 2
  name: Post _Api_V1_Ltlspotquotes Response 200
  slug: post-_api_v1_ltlspotquotes-response-200
- key_count: 2
  name: Post _Api_V1_Offer_Create Request
  slug: post-_api_v1_offer_create-request
- key_count: 2
  name: Post _Api_V1_Offer_Create Response 200
  slug: post-_api_v1_offer_create-response-200
- key_count: 2
  name: Post _Api_V1_Spotquotes Request
  slug: post-_api_v1_spotquotes-request
- key_count: 2
  name: Post _Api_V1_Spotquotes Response 200
  slug: post-_api_v1_spotquotes-response-200
finops:
- name: Coyote Finops
  service_category: ''
  slug: coyote-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/coyote.png
json_schemas:
- name: Accessorial
  property_count: 2
  slug: accessorial
- name: Address
  property_count: 6
  slug: address
- name: Appointment
  property_count: 4
  slug: appointment
- name: AppointmentDate
  property_count: 2
  slug: appointmentdate
- name: AssociatedEntity
  property_count: 2
  slug: associatedentity
- name: AvailableLoad
  property_count: 4
  slug: availableload
- name: AvailableLoadsFilterMode
  property_count: 0
  slug: availableloadsfiltermode
- name: AvailableLoadsRequest
  property_count: 4
  slug: availableloadsrequest
- name: BookingConflict
  property_count: 4
  slug: bookingconflict
- name: BookingRequest
  property_count: 2
  slug: bookingrequest
- name: BookingRequestStatus
  property_count: 4
  slug: bookingrequeststatus
- name: BookingStatus
  property_count: 0
  slug: bookingstatus
- name: CarrierQuote
  property_count: 12
  slug: carrierquote
- name: Commodity
  property_count: 11
  slug: commodity
- name: Contact
  property_count: 5
  slug: contact
- name: CurrencyType
  property_count: 0
  slug: currencytype
- name: Customer
  property_count: 2
  slug: customer
- name: DestinationRequirements
  property_count: 8
  slug: destinationrequirements
- name: Dimension
  property_count: 2
  slug: dimension
- name: Distance
  property_count: 2
  slug: distance
- name: DocumentRequest
  property_count: 4
  slug: documentrequest
- name: DriverWorkType
  property_count: 0
  slug: driverworktype
- name: Enums_Currency
  property_count: 0
  slug: enums_currency
- name: Enums_CurrencyType
  property_count: 0
  slug: enums_currencytype
- name: Enums_DimensionUnit
  property_count: 0
  slug: enums_dimensionunit
- name: Enums_DistanceUnit
  property_count: 0
  slug: enums_distanceunit
- name: Enums_DocumentExtensionType
  property_count: 0
  slug: enums_documentextensiontype
- name: Enums_DocumentType
  property_count: 0
  slug: enums_documenttype
- name: Enums_EquipmentType
  property_count: 0
  slug: enums_equipmenttype
- name: Enums_FreightClass
  property_count: 0
  slug: enums_freightclass
- name: Enums_LengthUnitType
  property_count: 0
  slug: enums_lengthunittype
- name: Enums_LimitedAccessType
  property_count: 0
  slug: enums_limitedaccesstype
- name: Enums_MultipleNumberType
  property_count: 0
  slug: enums_multiplenumbertype
- name: Enums_WeightType
  property_count: 0
  slug: enums_weighttype
- name: Enums_WeightUnitType
  property_count: 0
  slug: enums_weightunittype
- name: EquipmentAttributes
  property_count: 33
  slug: equipmentattributes
- name: EquipmentDetails
  property_count: 6
  slug: equipmentdetails
- name: EquipmentType
  property_count: 0
  slug: equipmenttype
- name: Facility
  property_count: 3
  slug: facility
- name: GenericAttributeItem
  property_count: 2
  slug: genericattributeitem
- name: GeoCoordinates
  property_count: 2
  slug: geocoordinates
- name: GeoLocation
  property_count: 2
  slug: geolocation
- name: HazMatClass
  property_count: 0
  slug: hazmatclass
- name: HazMatProperties
  property_count: 3
  slug: hazmatproperties
- name: Load
  property_count: 2
  slug: load
- name: LoadAttributes
  property_count: 49
  slug: loadattributes
- name: LoadBuildStatus
  property_count: 0
  slug: loadbuildstatus
- name: LoadCommodity
  property_count: 24
  slug: loadcommodity
- name: LoadDetail
  property_count: 8
  slug: loaddetail
- name: LoadDetails
  property_count: 8
  slug: loaddetails
- name: LoadEquipmentRequirement
  property_count: 2
  slug: loadequipmentrequirement
- name: LoadEquipmentRequirementType
  property_count: 0
  slug: loadequipmentrequirementtype
- name: LoadRequestStatus
  property_count: 4
  slug: loadrequeststatus
- name: LoadRequirement
  property_count: 2
  slug: loadrequirement
- name: LoadRequirementType
  property_count: 0
  slug: loadrequirementtype
- name: LoadSearchResult
  property_count: 4
  slug: loadsearchresult
- name: LoadStop
  property_count: 4
  slug: loadstop
- name: LoadStopAttributes
  property_count: 86
  slug: loadstopattributes
- name: LoadStopLocationInfo
  property_count: 3
  slug: loadstoplocationinfo
- name: LoadStopProgress
  property_count: 5
  slug: loadstopprogress
- name: LoadStopRequirement
  property_count: 2
  slug: loadstoprequirement
- name: LoadStopRequirementType
  property_count: 0
  slug: loadstoprequirementtype
- name: Location
  property_count: 3
  slug: location
- name: LocationData
  property_count: 4
  slug: locationdata
- name: LocationStatus
  property_count: 4
  slug: locationstatus
- name: LtlLocationData
  property_count: 4
  slug: ltllocationdata
- name: LTLSpotQuote
  property_count: 2
  slug: ltlspotquote
- name: LTLSpotQuoteRequest
  property_count: 9
  slug: ltlspotquoterequest
- name: Milestone
  property_count: 5
  slug: milestone
- name: Mode
  property_count: 0
  slug: mode
- name: OfferDetails
  property_count: 5
  slug: offerdetails
- name: OfferRequest
  property_count: 4
  slug: offerrequest
- name: OfferStatus
  property_count: 0
  slug: offerstatus
- name: OriginRequirements
  property_count: 6
  slug: originrequirements
- name: PackagingType
  property_count: 0
  slug: packagingtype
- name: PagedAvailableLoads
  property_count: 2
  slug: pagedavailableloads
- name: Pagination
  property_count: 3
  slug: pagination
- name: Radius
  property_count: 2
  slug: radius
- name: Rate
  property_count: 2
  slug: rate
- name: RateCode
  property_count: 0
  slug: ratecode
- name: RateItem
  property_count: 6
  slug: rateitem
- name: ReferenceNumber
  property_count: 2
  slug: referencenumber
- name: SpotQuote
  property_count: 9
  slug: spotquote
- name: SpotQuoteRequest
  property_count: 12
  slug: spotquoterequest
- name: StopDetail
  property_count: 2
  slug: stopdetail
- name: StopDetails
  property_count: 5
  slug: stopdetails
- name: StopType
  property_count: 0
  slug: stoptype
- name: Summary
  property_count: 5
  slug: summary
- name: Temperature
  property_count: 2
  slug: temperature
- name: TemperatureSettings
  property_count: 3
  slug: temperaturesettings
- name: TemperatureSettingType
  property_count: 0
  slug: temperaturesettingtype
- name: TemperatureUnit
  property_count: 0
  slug: temperatureunit
- name: TimeSpan
  property_count: 11
  slug: timespan
- name: TrackingAddress
  property_count: 7
  slug: trackingaddress
- name: Unit
  property_count: 0
  slug: unit
- name: Weight
  property_count: 2
  slug: weight
jsonld:
- class_count: 0
  name: Apis Context
  property_count: 0
  slug: apis
layout: provider
modified: '2026-06-13'
name: Coyote Logistics
nav: Providers
network: true
overview: 'Coyote Logistics publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Associated Entities API API, Carrier - Available Load APIs API, Carrier - Booking APIs API, and 5 more. Tagged areas include freight brokerage, logistics, truckload, LTL, and less-than-truckload.


  The Coyote Logistics catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Coyote Logistics'' developer surface includes documentation, engineering blog, pricing, and 10 more developer resources.'
plans:
- name: Coyote Plans Pricing
  plan_count: 3
  slug: coyote-plans-pricing
random_paper: 89
rate_limits:
- limit_count: 3
  name: Coyote Rate Limits
  slug: coyote-rate-limits
rules:
- name: Coyote Logistics API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: coyote-jsonschema-spectral-rules
score:
  band: developing
  composite: 48.8
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 61.5
    developer_ergonomics: 10.9
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 52.6
  previous_composite: 48.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/coyote/refs/heads/main/screenshots/coyote-2026-06-20T175149.png
security:
- kind: domain-security
  name: Coyote Domain Security
  slug: coyote-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: coyote
tags:
- freight brokerage
- logistics
- truckload
- LTL
- less-than-truckload
- shipping
- supply chain
- freight quotes
- shipment tracking
- load management
- 3PL
- customs brokerage
- carrier API
- shipper API
website: https://coyote.com/
---
