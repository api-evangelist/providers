---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: true
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 30.1
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 13
  human_in_the_loop: 0
  name: Dpd Group Agentic Access
  operation_count: 23
  slug: dpd-group-agentic-access
  summary_line: 23 operations · 13 acting
api_count: 3
apis:
- baseURL: https://geoapi.dpd.cz/v1
  baseurl_source: declared
  description: Lists countries supported by DPD CZ GeoAPI. Part of DPD Czech Republic GeoAPI (v1).
  name: DPD Geo Countries API
  slug: geoapi-countries
- baseURL: https://geoapi.dpd.cz/v1
  baseurl_source: declared
  description: Retrieves customer and address data for the authenticated DPD CZ account. Part of DPD Czech Republic GeoAPI (v1).
  name: DPD Geo Customers API
  slug: geoapi-customers
- baseURL: https://geoapi.dpd.cz/v1
  baseurl_source: declared
  description: Returns details about the authenticated GeoAPI user. Part of DPD Czech Republic GeoAPI (v1).
  name: DPD Geo Me API
  slug: geoapi-me
- baseURL: https://geoapi.dpd.cz/v1
  baseurl_source: declared
  description: Retrieves parcel details, tracking and labels from DPD CZ GeoAPI. Part of DPD Czech Republic GeoAPI (v1).
  name: DPD Geo Parcels API
  slug: geoapi-parcels
- baseURL: https://geoapi.dpd.cz/v1
  baseurl_source: declared
  description: Creates and manages pickup orders with DPD CZ. Part of DPD Czech Republic GeoAPI (v1).
  name: DPD Geo Pickup Orders API
  slug: geoapi-pickup-orders
- baseURL: https://geoapi.dpd.cz/v1
  baseurl_source: declared
  description: Creates shipments in DPD CZ GeoAPI. Part of DPD Czech Republic GeoAPI (v1).
  name: DPD Geo Shipments API
  slug: geoapi-shipments
- baseURL: https://geoapi.dpd.cz/v1
  baseurl_source: declared
  description: Lists DPD CZ shipping services available to the account. Part of DPD Czech Republic GeoAPI (v1).
  name: DPD Geo Shipping Services API
  slug: geoapi-shipping-services
- baseURL: https://api.dpdgroup.com
  baseurl_source: declared
  description: DPD Group META-API for creating shipments, generating labels and managing parcels across DPD Group business units.
  name: DPD META-API Shipment
  slug: meta-api-shipping
- description: DPD Belgium/Luxembourg SOAP web service (endofdayservicev10) for DPD shipping, tracking and parcel shop data.
  name: DPD Belgium/Luxembourg endofdayservicev10 SOAP Service
  slug: dpd-belux-endofdayservicev10
- description: DPD Belgium/Luxembourg SOAP web service (loginservicev21) for DPD shipping, tracking and parcel shop data.
  name: DPD Belgium/Luxembourg loginservicev21 SOAP Service
  slug: dpd-belux-loginservicev21
- description: DPD Belgium/Luxembourg SOAP web service (parcellifecycleservicev20) for DPD shipping, tracking and parcel shop data.
  name: DPD Belgium/Luxembourg parcellifecycleservicev20 SOAP Service
  slug: dpd-belux-parcellifecycleservicev20
- description: DPD Belgium/Luxembourg SOAP web service (parcelshopfinderservicev50) for DPD shipping, tracking and parcel shop data.
  name: DPD Belgium/Luxembourg parcelshopfinderservicev50 SOAP Service
  slug: dpd-belux-parcelshopfinderservicev50
- description: DPD Belgium/Luxembourg SOAP web service (shipmentservicev34) for DPD shipping, tracking and parcel shop data.
  name: DPD Belgium/Luxembourg shipmentservicev34 SOAP Service
  slug: dpd-belux-shipmentservicev34
- description: DPD Germany SOAP web service (depotdataservice-v1_0) for DPD shipping, tracking and parcel shop data.
  name: DPD Germany depotdataservice-v1_0 SOAP Service
  slug: dpd-de-depotdataservice-v1_0
- description: DPD Germany SOAP web service (loginservice-v2_0) for DPD shipping, tracking and parcel shop data.
  name: DPD Germany loginservice-v2_0 SOAP Service
  slug: dpd-de-loginservice-v2_0
- description: DPD Germany SOAP web service (parcellifecycleservice-v2_0) for DPD shipping, tracking and parcel shop data.
  name: DPD Germany parcellifecycleservice-v2_0 SOAP Service
  slug: dpd-de-parcellifecycleservice-v2_0
- description: DPD Germany SOAP web service (parcelshopfinderservice-v5_0) for DPD shipping, tracking and parcel shop data.
  name: DPD Germany parcelshopfinderservice-v5_0 SOAP Service
  slug: dpd-de-parcelshopfinderservice-v5_0
- description: DPD Germany SOAP web service (shipmentservice-v3_2) for DPD shipping, tracking and parcel shop data.
  name: DPD Germany shipmentservice-v3_2 SOAP Service
  slug: dpd-de-shipmentservice-v3_2
- description: DPD Germany SOAP web service (shipmentservice-v4_4) for DPD shipping, tracking and parcel shop data.
  name: DPD Germany shipmentservice-v4_4 SOAP Service
  slug: dpd-de-shipmentservice-v4_4
- description: DPD Germany SOAP web service (shipmentservice-v4_5) for DPD shipping, tracking and parcel shop data.
  name: DPD Germany shipmentservice-v4_5 SOAP Service
  slug: dpd-de-shipmentservice-v4_5
- description: DPD Poland SOAP web service (package-obj-services) for DPD shipping, tracking and parcel shop data.
  name: DPD Poland package-obj-services SOAP Service
  slug: dpd-pl-package-obj-services
artifact_total: 52
collections:
- collection_type: open
  name: DPD GeoAPI
  slug: open-dpd-cz-geoapi-v1
- collection_type: open
  name: DPD GeoAPI
  slug: open-dpd-cz-geoapi-v2
- collection_type: open
  name: META-API Shipment
  slug: open-dpd-group-meta-api-shipping
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/dpd-group/refs/heads/main/agentic-access/dpd-group-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/dpd-group-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/dpd-group/refs/heads/main/rules/dpd-group-rules.yml
  title: ''
  type: Spectral
  url: rules/dpd-group-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/dpd-group/refs/heads/main/json-ld/dpd-group-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/dpd-group-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/dpd-group/refs/heads/main/vocabulary/dpd-group-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/dpd-group-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/dpd-group/refs/heads/main/data-model/dpd-group-data-model.yml
  title: ''
  type: DataModel
  url: data-model/dpd-group-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/dpd-group/refs/heads/main/errors/dpd-group-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/dpd-group-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/dpd-group/refs/heads/main/conformance/dpd-group-conformance.yml
  title: ''
  type: Conformance
  url: conformance/dpd-group-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/dpd-group/refs/heads/main/hosts/dpd-group-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dpd-group-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/dpd-group/refs/heads/main/vendors/dpd-group-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dpd-group-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/dpd-group/refs/heads/main/security/dpd-group-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dpd-group-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/dpd-group/refs/heads/main/authentication/dpd-group-authentication.yml
  title: ''
  type: Authentication
  url: authentication/dpd-group-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.dpd.com
- group: start
  title: ''
  type: Portal
  url: https://esolutions.dpd.com/entwickler.aspx
- group: docs
  title: ''
  type: Documentation
  url: https://nst-preprod.dpsin.dpdgroup.com/api/docs/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.geopost.com/en/data-privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.geopost.com/en/legal-and-copyright-notice-disclaimer-dispute-settlement/
created: '2026-10-13'
description: DPD Group (part of Geopost) is a European parcel delivery network. Its business units publish shipping APIs including the DPD Group META-API Shipment REST API, the DPD Czech Republic GeoAPI, and SOAP web services from DPD Germany, DPD Belgium/Luxembourg and DPD Poland for shipment creation, labels, tracking, pickups and parcel shop lookup.
json_schemas:
- name: Country
  property_count: 5
  slug: dpd-group-country
- name: CustomerAddress
  property_count: 4
  slug: dpd-group-customer-address
- name: Customer
  property_count: 3
  slug: dpd-group-customer
- name: DropoffCodes
  property_count: 2
  slug: dpd-group-dropoff-codes
- name: LabelBinary
  property_count: 0
  slug: dpd-group-label-binary
- name: LabelScript
  property_count: 0
  slug: dpd-group-label-script
- name: Me
  property_count: 2
  slug: dpd-group-me
- name: NewPickupOrder
  property_count: 0
  slug: dpd-group-new-pickup-order
- name: New Shipment
  property_count: 11
  slug: dpd-group-new-shipment
- name: Parcel
  property_count: 6
  slug: dpd-group-parcel
- name: _parcels_labels_post_request
  property_count: 0
  slug: dpd-group-parcels-labels-post-request
- name: PickupOrder
  property_count: 4
  slug: dpd-group-pickup-order
- name: _pickup_orders__pickupOrderId__delete_200_response
  property_count: 1
  slug: dpd-group-pickup-orders-pickup-order-id-delete-200-response
- name: PickupSchedule
  property_count: 15
  slug: dpd-group-pickup-schedule
- name: pickupscheduling.PickupSchedule
  property_count: 15
  slug: dpd-group-pickupscheduling-pickup-schedule
- name: ShipmentResponse
  property_count: 10
  slug: dpd-group-shipment-response
- name: Shipment
  property_count: 11
  slug: dpd-group-shipment
- name: shipment.ShipmentResponse
  property_count: 10
  slug: dpd-group-shipment-shipment-response
- name: shipment.Shipment
  property_count: 20
  slug: dpd-group-shipment-shipment
- name: ShippingServiceList
  property_count: 2
  slug: dpd-group-shipping-service-list
- name: SuccessfulTrackingResult
  property_count: 2
  slug: dpd-group-successful-tracking-result
- name: TrackingResultItem
  property_count: 0
  slug: dpd-group-tracking-result-item
- name: TrackingResult
  property_count: 2
  slug: dpd-group-tracking-result
jsonld:
- class_count: 120
  name: Dpd Group Context
  property_count: 248
  slug: dpd-group-context
layout: provider
modified: '2026-10-13'
name: DPD Group
nav: Providers
network: true
overview: 'DPD Group publishes 21 API contracts indexed on the [APIs.io](https://apis.io/) network, including DPD Geo Countries API, DPD Geo Customers API, DPD Geo Me API, and 18 more. Tagged areas include Logistics, Parcel, Shipping, Tracking, and Carrier.


  The DPD Group catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  DPD Group''s developer surface includes authentication, developer portal, documentation, and 13 more developer resources.'
random_paper: 12
rules:
- authorship: generated
  effective_rule_count: 58
  extends:
  - spectral:oas
  name: DPD Group API Rules
  rule_count: 17
  severity_counts:
    error: 12
    hint: 0
    info: 1
    warn: 4
  slug: dpd-group-rules
score:
  band: thin
  composite: 36.7
  coverage:
    artifact_dirs: 19
    catalog_earned: 63.8
    catalog_earned_first_party: 0.0
    catalog_gap: 51.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 22.0
    contract_quality: 66.5
    developer_ergonomics: 35.2
    discoverability: 67.9
    operational_transparency: 0.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 20.8
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Dpd Group Authentication
  slug: dpd-group-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Dpd Group Domain Security
  slug: dpd-group-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: dpd-group
tags:
- Logistics
- Parcel
- Shipping
- Tracking
- Carrier
website: https://www.dpd.com
---
