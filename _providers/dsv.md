---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 44.1
  scored_at: '2026-08-10'
api_count: 29
apis:
- description: OAuth 2.0 token endpoint for the DSV Generic APIs. Exchanges myDSV username/password (sent as client_id/client_secret with grant_type=client_credentials) plus a DSV-Subscription-Key for a 10-minute be
  name: DSV Access Token API
  slug: dsv-access-token-api
- description: Submits and updates shipment bookings to DSV across air, sea, European road and rail. Carries GS1 SSCC package tracking numbers (explicitly referenced to gs1.org/standards/id-keys/sscc), EORI numbers,
  name: DSV Booking API (Air, Sea, Road EU, Rail)
  slug: dsv-booking-api-air-sea-road-eu-rail
- description: Polling track-and-trace over DSV-moved shipments. Lookups by DSV bookingId, DSV TMS shipment id or customer reference; responses carry house and master bill of lading numbers, air waybill numbers, con
  name: DSV Tracking API (Air, Sea, Road EU, Rail)
  slug: dsv-tracking-api-air-sea-road-eu-rail
- description: Prints package labels as PDF for bookings submitted through the DSV Booking API or myDSV, addressed by bookingId and GS1 SSCC package number.
  name: DSV Label Print API
  slug: dsv-label-print-api
- description: Uploads documents against an existing DSV booking or shipment for air, sea, European road and rail traffic.
  name: DSV Document Upload API
  slug: dsv-document-upload-api
- description: Downloads the documents DSV holds against a booking or shipment — proof of delivery, transport documents and customs paperwork — for air, sea, European road and rail traffic.
  name: DSV Document Download API
  slug: dsv-document-download-api
- description: Retrieves freight invoice detail for DSV air, sea and rail shipments, including carrier SCAC, master and house bill of lading references and UN/LOCODE locations.
  name: DSV Invoice API
  slug: dsv-invoice-api
- description: Returns live IoT device readings from DSV Visibility for air, sea, rail and XPress shipments, queried by search filter.
  name: DSV Visibility API
  slug: dsv-visibility-api
- description: Requests freight quotations from DSV. Origin and destination are expressed as 5-character UN/LOCODEs for both ports and airports — the spec explicitly rejects IATA 3-letter airport codes — alongside I
  name: DSV Quote API
  slug: dsv-quote-api
- description: Subscription API for DSV push notifications covering the Invoice, Visibility, Quote, Tracking, Warehousing, Customs and Downtime events. The subscriber supplies a push URL (validated with an OPTIONS t
  name: DSV Webhook API
  slug: dsv-webhook-api
- description: Integration-environment webhook subscription surface used for the Invoice and Visibility APIs and the Contract Logistics WMS events.
  name: DSV Webhook API (INT / Warehousing)
  slug: dsv-webhook-api-int-warehousing
- description: Transmits, updates and retrieves customs declarations through DSV Customs AI. Fields follow customs-authority vocabulary — HS commodity codes, EORI/importer/exporter registration codes, Incoterms with
  name: DSV Customs API
  slug: dsv-customs-api
- description: SOAP BookingWebService covering land, air and ocean (LCL/FCL) bookings. Inherited from the DB Schenker estate that DSV acquired in 2025 and fronted through the same Azure API Management gateway as the
  name: DSV Connect Booking API (SOAP)
  slug: dsv-connect-booking-api-soap
- description: SOAP TrackingWebService, described in DSV's own API Management metadata as the 'DB Schenker Standard Tracking SOAP API' — the legacy tracking contract carried over from the Schenker acquisition and re
  name: DSV Connect Tracking API (SOAP)
  slug: dsv-connect-tracking-api-soap
- description: Creates express/parcel shipments and retrieves package labels. Carries per-package air waybill numbers, underlying express carrier codes and carrier tracking numbers, plus ADR/IATA dangerous-goods pro
  name: DSV XPress Booking API
  slug: dsv-xpress-booking-api
- description: Express/parcel track-and-trace. Shipments are addressable by DSV shipment id or by air waybill number (GET /shipments/awb/{awb}); responses carry the underlying express carrier's own tracking number a
  name: DSV XPress Tracking API
  slug: dsv-xpress-tracking-api
- description: Compares services and rates for express/parcel shipments against the customer's agreed tariff, including ADR, ADR-LQ, IATA DGR and lithium-battery dangerous-goods service codes.
  name: DSV XPress Quote API
  slug: dsv-xpress-quote-api
- description: Submits and updates purchase orders in DSV's Supply Chain Management (eDC) platform, the order-management layer that sits above the forwarding products. Order and shipment records carry carrier SCAC c
  name: DSV SCM Orders API
  slug: dsv-scm-orders-api
- description: Creates and searches bookings in the DSV SCM (eDC) platform, including original/copy bill of lading counts, carrier SCAC and carrier contract numbers.
  name: DSV SCM Booking API
  slug: dsv-scm-booking-api
- description: Searches shipments in the DSV SCM (eDC) platform by criteria, returning carrier, bill of lading and container detail.
  name: DSV SCM Shipments API
  slug: dsv-scm-shipments-api
- description: Creates and manages load plans in the DSV SCM (eDC) platform across transport legs, each leg carrying carrier code, carrier SCAC and DSV's internal Dakosky carrier code.
  name: DSV SCM Load Plan API
  slug: dsv-scm-load-plan-api
- description: Adds and retrieves electronic documents against SCM orders, bookings and shipments in the DSV eDC platform.
  name: DSV SCM eDocs API
  slug: dsv-scm-edocs-api
- description: 'Writes milestone events into the DSV SCM (eDC) platform. Notably exposes POST /event/ServiceProvider so a third-party service provider — not only the account owner — can post events into DSV''s chain, '
  name: DSV SCM Events API
  slug: dsv-scm-events-api
- description: Customer-specific eDC surface published for the NEOM programme, covering orders, containers, harmonised commodity codes and house bill of lading references.
  name: DSV NEOM API (eDC)
  slug: dsv-neom-api-edc
- description: Creates and updates product master data records in DSV Contract Logistics warehouse management.
  name: DSV WMS Product Data API
  slug: dsv-wms-product-data-api
- description: Creates and updates inbound (pre-advice) orders for DSV Contract Logistics warehouses, with GS1 SSCC pallet/carton codes and container numbers on the line items.
  name: DSV WMS Inbound Notification API
  slug: dsv-wms-inbound-notification-api
- description: Creates and updates outbound delivery notification orders for DSV Contract Logistics warehouses.
  name: DSV WMS Delivery Notification API
  slug: dsv-wms-delivery-notification-api
- description: Retrieves inventory positions from DSV Contract Logistics warehouses, per product id or as a full inventory request.
  name: DSV WMS Inventory API
  slug: dsv-wms-inventory-api
- description: Returns the current status of a specific delivery or inbound order in DSV Contract Logistics warehouse management.
  name: DSV WMS Order Status API
  slug: dsv-wms-order-status-api
artifact_total: 29
common:
- group: company
  title: ''
  type: Website
  url: https://www.dsv.com/
- group: start
  title: ''
  type: Portal
  url: https://developer.dsv.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.dsv.com/getting-started
- group: docs
  title: ''
  type: APIReference
  url: https://developer.dsv.com/apicatalogue
- group: start
  title: ''
  type: Signup
  url: https://developer.dsv.com/signup
- group: other
  title: ''
  type: SignIn
  url: https://developer.dsv.com/signin
- group: auth
  title: ''
  type: Authentication
  url: https://developer.dsv.com/oauth-guide
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.dsv.com/release-notes
- group: design
  title: ''
  type: Webhooks
  url: https://developer.dsv.com/webhook-guide
- group: other
  title: ''
  type: EDI
  url: https://developer.dsv.com/getting-started-with-edi
- group: docs
  title: ''
  type: Documentation
  url: https://developer.dsv.com/editransport
- group: auth
  title: ''
  type: Security
  url: https://developer.dsv.com/edi-certificates
- group: company
  title: ''
  type: Partners
  url: https://developer.dsv.com/partner-integrations-and-plugins1
- group: build
  title: ''
  type: Plugins
  url: https://developer.dsv.com/ecommerce-shopify
- group: operate
  title: ''
  type: FAQ
  url: https://developer.dsv.com/api_faq
- group: operate
  title: ''
  type: Support
  url: https://developer.dsv.com/support-contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developer.dsv.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.dsv.com/en/about-dsv/corporate-responsibility/policies/data-privacy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/dsv
created: '2026-07-30'
description: 'DSV A/S is a Danish transport and logistics group headquartered in Hedehusene, Denmark, and one of the world''s largest freight forwarders — roughly 150,000 employees across more than 90 countries after its 2025 acquisition of Schenker from Deutsche Bahn. It sells air, sea, road, rail and parcel forwarding plus contract logistics and customs brokerage, sitting in the intermediation layer between shippers and the carriers, terminals and customs authorities it books capacity with. Its API posture is a real, publicly browsable Azure API Management developer portal at developer.dsv.com carrying 29 downloadable OpenAPI 3.0.1 contracts for booking, tracking, quoting, labels, documents, invoicing, customs, warehousing and webhooks — but every published product is a DEMO/test environment, production access is gated behind myDSV customer credentials and an ''apply to go live'' step, and for a large part of DSV''s customer base the real integration path is still EDIFACT D10B, ANSI X12
  and DSV XML message packages moved over AS2, SFTP or HTTPS. The REST surface is entirely DSV-proprietary: no DCSA, IATA ONE Record, Cargo-XML or GS1 EPCIS conformance is claimed anywhere.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/groq.png
layout: provider
modified: '2026-07-30'
name: DSV
nav: Providers
network: true
overview: 'DSV publishes 29 APIs on the [APIs.io](https://apis.io/) network, including Access Token API, Booking API (Air, Sea, Road EU, Rail), Tracking API (Air, Sea, Road EU, Rail), and 26 more. Tagged areas include Logistics, Supply Chain, Denmark, Freight Forwarding, and Air Cargo.


  DSV''s developer surface includes developer portal, documentation, API reference, signup flow, authentication, changelog, FAQ, and 12 more developer resources.'
random_paper: 101
score:
  band: thin
  composite: 38.8
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 59.6
    developer_ergonomics: 39.1
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 38.8
  provenance:
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 29
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dsv/refs/heads/main/screenshots/dsv-2026-08-07T164531.png
slug: dsv
tags:
- Logistics
- Supply Chain
- Denmark
- Freight Forwarding
- Air Cargo
- Ocean Freight
- Road Freight
- Rail Freight
- Parcel
- Contract Logistics
- Warehousing
- Customs
- Trade Compliance
- Track and Trace
- EDI
website: https://www.dsv.com/
---
