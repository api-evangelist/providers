---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.2
  scored_at: '2026-08-19'
api_count: 17
apis:
- description: Find and show details of the customer's shipments, with contents reflecting the visibility configured in myKN. Search shipments, load a single shipment by unique reference, and read history records. R
  name: Kuehne+Nagel ShipmentTracking API
  slug: shipment-tracking
- description: 'Find and show details of the customer''s seafreight containers, reflecting myKN visibility. Container search plus a per-container read keyed on the Kuehne+Nagel unique shipment reference and container '
  name: Kuehne+Nagel ContainerTracking API
  slug: container-tracking
- description: A service for consumers to receive order data information, searched by order attributes. Carries UN/LOCODE port fields, HS codes, EORI numbers and a GS1 global location number field on item attributes
  name: Kuehne+Nagel OrderTracking API
  slug: order-tracking
- description: Read cargo items and their telemetry readings for real-time visibility. Two GET operations, polled; no subscription or push channel is published.
  name: Kuehne+Nagel RealTimeVisibility-Tracking API
  slug: real-time-visibility-tracking
- description: 'A service for consumers to book an air shipment, optionally applying product prices supplied via the Airfreight Quote API. Carries IATA three-letter airport codes, air waybill and HAWB service types, '
  name: Kuehne+Nagel BookingAir API
  slug: booking-air
- description: A service for consumers to book road shipments, with master-data category lookups and a document upload operation alongside booking creation.
  name: Kuehne+Nagel BookingRoad API
  slug: booking-road
- description: Create and update order bookings by shipper's reference and poll a process state. Discriminated booking bodies for AIR, FCL and LCL, with UN/LOCODE-typed ports and airports.
  name: Kuehne+Nagel OrderBooking API
  slug: order-booking
- description: Create, patch, search and cancel purchase orders scoped to a Kuehne+Nagel customer code. UN/LOCODE ports, HS codes and EORI numbers appear on the order model.
  name: Kuehne+Nagel PurchaseOrderManagement API
  slug: purchase-order-management
- description: Read the purchase-order configuration for a given Kuehne+Nagel customer code. The devportal publishes only an internal gateway environment for this API; no external endpoint URL is advertised.
  name: Kuehne+Nagel eSOPPurchaseOrderConfiguration API
  slug: esop-purchase-order-configuration
- description: Lets service providers submit container equipment events for shipments booked with Kuehne+Nagel, following Digital Container Shipping Association (DCSA) standards. Inbound only — Kuehne+Nagel receives
  name: Kuehne+Nagel OceanEventInbox API
  slug: ocean-event-inbox
- description: Validates and accepts incoming shipment event entries from third parties. Inbound only; the specification names a third-party application as the intended publisher.
  name: Kuehne+Nagel ShipmentEventIntegration API
  slug: shipment-event-integration
- description: Upsert or delete an externally-sourced shipment against a Kuehne+Nagel customer code and shipment number — the surface through which non-Kuehne+Nagel shipments are fed into Kuehne+Nagel visibility.
  name: Kuehne+Nagel ExternalShipmentIntegration API
  slug: external-shipment-integration
- description: 'Carrier-facing pickup-and-delivery execution for sea intermodal legs — list assigned consignments, pull job documents, post job status, post GPS tracking and post proof of delivery per waypoint. Uses '
  name: Kuehne+Nagel IntermodalTransportExecution API
  slug: intermodal-transport-execution
- description: List, download, add and delete shipment-related documents against a Kuehne+Nagel unique shipment reference, plus a lookup of uploadable document types. The current version for new integrations.
  name: Kuehne+Nagel ShipmentDocumentManagement API v3
  slug: shipment-document-management-v3
- description: Legacy document management for shipment documents, limited to adding and downloading documents. Marked in the developer portal as legacy and intended for existing integrations only; v3 is directed for
  name: Kuehne+Nagel ShipmentDocumentManagement API v2
  slug: shipment-document-management-v2
- description: Described in the developer portal as being for bespoke customs integrations with customers. The published OpenAPI declares two POST operations, /order and /document, with no request schemas, no respon
  name: Kuehne+Nagel B2B-CustomsEDI API
  slug: b2b-customs-edi
- description: Published in the developer portal as B2B-OldKAIExtractAPI — extract structured information from documents, with workspace management, synchronous and asynchronous file and zip processing, prompt-drive
  name: Kuehne+Nagel KAI Document Extract API
  slug: kai-document-extract
artifact_total: 34
collections:
- collection_type: open
  name: B2B-CustomsEDI
  slug: open-kuehne-nagel-b2b-customs-edi-v1
- collection_type: open
  name: BookingAir
  slug: open-kuehne-nagel-booking-air-v2
- collection_type: open
  name: BookingRoad
  slug: open-kuehne-nagel-booking-road-v1
- collection_type: open
  name: ContainerTracking
  slug: open-kuehne-nagel-container-tracking-v2
- collection_type: open
  name: eSOPPurchaseOrderConfiguration
  slug: open-kuehne-nagel-esop-purchase-order-configuration-v1
- collection_type: open
  name: ExternalShipmentIntegration
  slug: open-kuehne-nagel-external-shipment-integration-v1
- collection_type: open
  name: IntermodalTransportExecution
  slug: open-kuehne-nagel-intermodal-transport-execution-v1
- collection_type: open
  name: B2B-OldKAIExtractAPI
  slug: open-kuehne-nagel-kai-document-extract-v0-1-0
- collection_type: open
  name: OceanEventInbox
  slug: open-kuehne-nagel-ocean-event-inbox-v1
- collection_type: open
  name: OrderBooking
  slug: open-kuehne-nagel-order-booking-v1
- collection_type: open
  name: OrderTracking
  slug: open-kuehne-nagel-order-tracking-v2
- collection_type: open
  name: PurchaseOrderManagement
  slug: open-kuehne-nagel-purchase-order-management-v3
- collection_type: open
  name: RealTimeVisibility-Tracking
  slug: open-kuehne-nagel-real-time-visibility-tracking-v1
- collection_type: open
  name: ShipmentDocumentManagement
  slug: open-kuehne-nagel-shipment-document-management-v2
- collection_type: open
  name: ShipmentDocumentManagement
  slug: open-kuehne-nagel-shipment-document-management-v3
- collection_type: open
  name: ShipmentEventIntegration
  slug: open-kuehne-nagel-shipment-event-integration-v1
- collection_type: open
  name: ShipmentTracking
  slug: open-kuehne-nagel-shipment-tracking-v2
common:
- group: company
  title: ''
  type: Website
  url: https://www.kuehne-nagel.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://portal.api.kuehne-nagel.com/devportal/
- group: docs
  title: ''
  type: Documentation
  url: https://www.kuehne-nagel.com/digital-services/data-integration
- group: docs
  title: ''
  type: Documentation
  url: https://mykn.kuehne-nagel.com/help-center/connectivity
- group: start
  title: ''
  type: Portal
  url: https://mykn.kuehne-nagel.com/
- group: start
  title: ''
  type: SignUp
  url: https://www.kuehne-nagel.com/contact/digital-data-integration
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/kuehne-nagel
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/kuehne-nagel
created: '2026-07-30'
description: 'Kuehne+Nagel International AG is a Swiss freight forwarder and contract logistics provider headquartered in Schindellegi, Switzerland, and one of the largest forwarders in the world across sea logistics, air logistics, road logistics and contract logistics. As a forwarder it sits in the intermediation layer of the supply chain — between shippers on one side and ocean carriers, airlines, hauliers, terminals and customs authorities on the other — and most of the data it exposes is carrier and terminal data it aggregates rather than originates. Its API posture is honest but conditional: a real WSO2-based developer portal at portal.api.kuehne-nagel.com lists 17 published APIs and serves every OpenAPI definition anonymously, but every subscription is customer-contract gated — a myKN account, a Kuehne+Nagel customer ID (CID) and an account manager who completes the "customer setup" are stated pre-requisites, so nobody outside a commercial relationship can call the gateway. Underneath
  the REST veneer the company''s own connectivity page still advertises EDIFACT, ANSI X.12, Tradacoms, RosettaNet, iDOC, GS1 and CargoImp over AS2, OFTP-2, (S)FTP and VAN as the primary integration path, and its one customs "EDI" API is an unschematized pass-through. One surface — OceanEventInbox v1 — is explicitly built to the DCSA equipment-event standard, which makes Kuehne+Nagel a non-member implementer of a carrier standards body; the other sixteen APIs are proprietary Kuehne+Nagel contracts.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/kuehne-nagel.png
layout: provider
modified: '2026-07-30'
name: Kuehne+Nagel
nav: Providers
network: true
overview: 'Kuehne+Nagel publishes 17 APIs on the [APIs.io](https://apis.io/) network, including ShipmentTracking API, ContainerTracking API, OrderTracking API, and 14 more. Tagged areas include Logistics, Supply Chain, Switzerland, Freight Forwarding, and Ocean Freight.


  Kuehne+Nagel''s developer surface includes documentation, developer portal, signup flow, and 5 more developer resources.'
random_paper: 12
score:
  band: emerging
  composite: 24.2
  delta: -2.1
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 51.5
    developer_ergonomics: 9.5
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 2.6
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 26.3
  provenance:
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 17
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kuehne-nagel/refs/heads/main/screenshots/kuehne-nagel-2026-08-07T171345.png
slug: kuehne-nagel
tags:
- Logistics
- Supply Chain
- Switzerland
- Freight Forwarding
- Ocean Freight
- Container Shipping
- Air Cargo
- Road Freight
- Customs
- Trade Compliance
- Track and Trace
- Contract Logistics
- Standards
website: https://www.kuehne-nagel.com/
---
