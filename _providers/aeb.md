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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.6
  scored_at: '2026-08-10'
api_count: 11
apis:
- description: Electronic customs declaration filing for import, export and transit. Creates consignments and deliveries, transmits them to national customs systems (German ATLAS, EU AES/NCTS, UK CHIEF), and polls d
  name: AEB Customs Management API
  slug: aeb-customs-management-api
- description: Customs warehouse / bonded inventory management. Books goods receipts and issues against customs warehouse stock, tracks entries by MRN or ATLAS registration number, and reconciles inventory positions
  name: AEB Customs Inventory Management API
  slug: aeb-customs-inventory-management-api
- description: The broker-facing surface of AEB's customs platform. Lets a customs broker or forwarder retrieve broker instructions and declarations filed on behalf of a principal, send broker instruction events bac
  name: AEB Customs Broker Portal API
  slug: aeb-customs-broker-portal-api
- description: Assigns and validates commodity/tariff classification for materials — HS and national tariff numbers, classification profiles, classification proposals and value templates — and serves the resulting c
  name: AEB Product Classification API
  slug: aeb-product-classification-api
- description: Restricted/denied party screening, export control and risk assessment as an API. Screens addresses and transactions against sanctions lists, manages good-guy releases and match handling, runs export c
  name: AEB Trade Compliance Management API
  slug: aeb-trade-compliance-management-api
- description: Multi-carrier shipping API covering 300+ carriers and parcel services. Creates shipments, packages and items, produces labels and shipping documents, builds and manifests pickups (AEB sends the carrie
  name: AEB Carrier Connect API
  slug: aeb-carrier-connect-api
- description: Carrier selection and routing. Creates routing tasks for a shipment and returns the carrier, service and route determined from the customer's routing rules, rates and constraints.
  name: AEB Carrier Select API
  slug: aeb-carrier-select-api
- description: Track-and-trace event aggregation across carriers. Registers shipments, configures per-carrier tracking connections, and returns resolved status events by shipment or reference number, including proof
  name: AEB Carrier Event Service API
  slug: aeb-carrier-event-service-api
- description: Freight cost management and freight settlement. Exposes billing scenarios, services, rates, settlements, settlement items and invoices so freight charges can be calculated, accrued and reconciled agai
  name: AEB Logistics Cost Management API
  slug: aeb-logistics-cost-management-api
- description: Document and print output service for the AEB platform. Manages workstations, printers, output channels and document master data, and delivers the labels, customs papers and transport documents genera
  name: AEB Document Service API
  slug: aeb-document-service-api
- description: The bundled BSM (Business Solution Modules) HTTP API that AEB exposes for SAP and partner-system integration — one surface spanning BSM Carrier, AEB Delivery, BSM International Customs, Export Control
  name: AEB BSM API
  slug: aeb-bsm-api
artifact_total: 11
common:
- group: company
  title: ''
  type: Website
  url: https://www.aeb.com/
- group: docs
  title: ''
  type: Documentation
  url: https://customsmanagement.docs.developers.aeb.com/
- group: docs
  title: ''
  type: Documentation
  url: https://trade-compliance.docs.developers.aeb.com/
- group: docs
  title: ''
  type: Documentation
  url: https://transport-freight-management.docs.developers.aeb.com/
- group: docs
  title: ''
  type: Documentation
  url: https://sap-plugins.docs.developers.aeb.com/
- group: start
  title: ''
  type: SupportPortal
  url: https://service.aeb.com/hc/en-us
- group: operate
  title: ''
  type: ChangeLog
  url: https://customsmanagement.docs.developers.aeb.com/changelog
- group: auth
  title: ''
  type: TrustCenter
  url: https://www.aeb.com/en/trust-center/index.php
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AEB-labs
- group: company
  title: ''
  type: Blog
  url: https://www.aeb.com/en/magazine/index.php
- group: commercial
  title: ''
  type: Pricing
  url: https://www.aeb.com/en/carrier-connect/carrier-connect-api.php
- group: other
  title: ''
  type: SOAP
  url: https://customsmanagement.docs.developers.aeb.com/page/soap-api
created: '2026-07-30'
description: 'AEB SE is a German supply chain and global trade software company, headquartered in Stuttgart and 100% employee-owned, whose platform is used by 7,300+ companies for customs filing, trade compliance, multi-carrier shipping, transport and freight cost management, and warehouse management. In the logistics chain AEB sits at the intermediation layer of customs and trade tech: it is the certified filer between the shipper or forwarder and the customs authority (German ATLAS, EU AES/NCTS/ICS, EMCS, Intrastat, UK CHIEF), and the multi-carrier abstraction between the shipper and 300+ carriers, generating the carrier EDI so the customer never has to. Its API posture is unusually open for this tier: four public ReadMe developer hubs (Customs, Trade Compliance, Transport & Freight Management, SAP add-ons) publish machine-readable OpenAPI 3.0.1 for every product, served live and unauthenticated from AEB''s own test and demo instances, with shared try-it credentials in the docs. But the
  contract is entirely proprietary — a REST-over-RPC business-facade shape unique to AEB, with a legacy SOAP business facade still exposed beside it — and production access requires registering with AEB and licensing the products, so it is a documented, quotable, contract-gated API rather than a self-serve one.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/aeb.png
layout: provider
modified: '2026-07-30'
name: AEB
nav: Providers
network: true
overview: 'AEB publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Customs Management API, Customs Inventory Management API, Customs Broker Portal API, and 8 more. Tagged areas include Logistics, Supply Chain, Germany, Customs, and Trade Compliance.


  AEB''s developer surface includes documentation, changelog, engineering blog, pricing, and 8 more developer resources.'
random_paper: 64
score:
  band: thin
  composite: 28.4
  delta: 0.0
  facets:
    commercial_clarity: 18.4
    contract_quality: 49.4
    developer_ergonomics: 10.9
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 28.4
  provenance:
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/aeb/refs/heads/main/screenshots/aeb-2026-08-07T160936.png
slug: aeb
tags:
- Logistics
- Supply Chain
- Germany
- Customs
- Trade Compliance
- Freight Forwarding
- Multi-Carrier Shipping
- Parcel
- Track and Trace
- Export Control
- Sanctions Screening
- Warehouse Management
- Transportation Management
- SAP
website: https://www.aeb.com/
---
