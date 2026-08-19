---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: Punchout / roundtrip integration that connects a customer's ERP or third-party procurement system to shop.dnow.com using cXML or OCI. DNOW configures the connection so buyers can browse the DNOW catal
  name: DigitalNOW ERP Punchout (cXML / OCI)
  slug: digitalnow-erp-punchout
artifact_total: 19
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/now-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.dnow.com
- group: start
  title: ''
  type: Portal
  url: https://shop.dnow.com/
- group: other
  title: ''
  type: Overview
  url: https://www.dnow.com/digital-solutions
- group: other
  title: ''
  type: Company
  url: https://www.dnow.com/company
- group: company
  title: ''
  type: InvestorRelations
  url: https://ir.dnow.com/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/dnowinc
- group: other
  title: ''
  type: StockTicker
  url: https://www.nyse.com/quote/XNYS:DNOW
- group: other
  title: ''
  type: Absences
  url: ''
- group: other
  title: ''
  type: ProductPage
  url: https://www.dnow.com/ecommerce
created: '2026-05-23'
description: 'DNOW Inc. (NYSE: DNOW), formerly NOW Inc. and operating as DistributionNOW, is a Houston-headquartered Fortune 1000 distributor of pipe, valves, fittings (PVF), pumps and packaged, engineered process and production equipment serving the upstream, midstream, downstream energy, and industrial sectors. Spun off from National Oilwell Varco in 2014 and built on a heritage that spans more than 160 years, DNOW combines a global network of distribution branches and engineering facilities with the DigitalNOW platform — shop.dnow.com B2B eCommerce, cXML/OCI ERP punchout integrations, the eSpec product configurator, the AccessNOW automated inventory control system, and a library of customer-facing mobile applications. DNOW does not publish a public developer portal, OpenAPI specifications, or a self-serve API program; customer integrations are delivered through configured cXML/OCI punchout sessions tied to enterprise ERP systems. In June 2025 DNOW announced a definitive merger agreement
  to acquire MRC Global in an all-stock transaction valued at approximately $1.5 billion.'
features:
- description: Distributor of pipe, valves, fittings (PVF), pumps and packaged, engineered process and production equipment to upstream, midstream, downstream energy, and industrial customers worldwide.
  name: Energy and Industrial Distribution
- description: Umbrella platform spanning shop.dnow.com B2B eCommerce, cXML/OCI ERP punchout, the eSpec configurator, AccessNOW automated inventory control, and a library of customer mobile applications, marketed as using AI, machine learning, mobile, and IoT.
  name: DigitalNOW Platform
- description: Online eCatalog covering more than 160,000 SKUs with real-time, account-specific contract pricing, approvals, and invoicing; broader inventory referenced as 300,000 stocked SKUs across the company.
  name: shop.dnow.com Catalog Scale
- description: Customer ERP and third-party procurement systems integrate to shop.dnow.com via cXML or OCI punchout / roundtrip with automated PO creation, approval, invoice generation, and shipment notifications.
  name: ERP Punchout Integration
- description: 24/7 secured tool-crib and stockroom access via badge, keypad, or facial recognition with barcode/RFID check-in and check-out and cloud-based transaction data.
  name: AccessNOW IoT Inventory
- description: In-house engineering, design, and fabrication of pump packages, measurement skids, and other engineered process and production equipment for energy and industrial customers.
  name: Engineering, Design and Fabrication
- description: DNOW and MRC Global announced a definitive all-stock merger agreement on June 26, 2025 valued at approximately $1.5 billion, which will materially expand DNOW's PVF distribution footprint.
  name: Pending MRC Global Merger
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/now.png
integrations:
- description: shop.dnow.com integrates to customer ERP and procurement platforms (e.g. SAP, Oracle, Ariba, Coupa, SciQuest-class systems) via cXML or OCI punchout / roundtrip configured per customer.
  name: Customer ERP Systems (cXML / OCI)
- description: Badge readers, keypads, facial-recognition units, barcode scanners, and RFID readers feed inventory transactions into DNOW's cloud-based inventory and replenishment systems.
  name: AccessNOW Devices
- description: Customer-facing iOS and Android apps synchronize cart, order, and history data with the shop.dnow.com eCommerce account.
  name: DNOW Mobile Apps
- description: Pending all-stock merger announced June 26, 2025; once closed, MRC Global's PVF distribution and digital surfaces are expected to be combined with DNOW's DigitalNOW platform.
  name: MRC Global (Pending Merger)
layout: provider
modified: '2026-07-25'
name: DNOW
nav: Providers
network: true
overview: 'DNOW publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Energy, Industrial Distribution, Pipe Valves And Fittings, PVF, and Supply Chain.


  DNOW''s developer surface includes developer portal and 8 more developer resources.'
random_paper: 42
score:
  band: minimal
  composite: 6.1
  delta: -1.6
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 7.7
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 8.1
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/now/refs/heads/main/screenshots/now-2026-06-20T190441.png
security:
- kind: domain-security
  name: Now Domain Security
  slug: now-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: now
tags:
- Energy
- Industrial Distribution
- Pipe Valves And Fittings
- PVF
- Supply Chain
- Procurement
- eCommerce
- cXML
- OCI
- Punchout
- IoT
- Inventory Management
- Mobile Apps
- Engineered Equipment
use_cases:
- description: Drilling, completions, artificial lift, and production operators source PVF, valves, pumps, and instrumentation through DNOW branches and the DigitalNOW eCommerce platform.
  name: Upstream Oil and Gas Procurement
- description: Pipelines, gas processing plants, refineries, and chemical plants source pipe, valves, fittings, electrical, and instrumentation supplies.
  name: Midstream and Downstream Supply
- description: Industrial and manufacturing customers procure tools, safety / PPE, paint and coatings, electrical, and facilities supplies through DNOW branches and shop.dnow.com.
  name: Industrial MRO and Facilities
- description: Enterprise buyers using SAP, Oracle, Ariba, Coupa, or similar procurement systems punch out to shop.dnow.com via cXML / OCI and round carts back into their ERP for PO automation.
  name: ERP-Driven Procurement
- description: Operators specify and order pump packages, measurement and production skids, and other engineered equipment using the eSpec configurator and DNOW engineering services.
  name: Engineered Equipment Packaging
- description: Site operators deploy AccessNOW units to control 24/7 access to consumables, tools, and safety equipment with cloud-based transaction visibility.
  name: Vendor-Managed Tool Cribs
website: https://www.dnow.com
---
