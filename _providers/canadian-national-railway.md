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
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-26'
api_count: 5
apis:
- description: CN's Application Programming Interface (API) enables shippers to integrate CN data and operations into their own systems. The API supports automated shipment ordering, equipment release, real-time car
  name: CN Shipper API
  slug: cn-shipper-api
- description: CN supports Electronic Data Interchange (EDI) for high-volume shipping customers. EDI enables automated transmission of shipping instructions, status updates, waybills, and invoicing between CN and cu
  name: CN EDI Services
  slug: cn-edi
- description: 'The CN eBusiness portal provides shippers with web-based access to shipment ordering, cargo tracking, account management, billing, and customer support. Shippers can order or release equipment, track '
  name: CN eBusiness Portal
  slug: cn-ebusiness
- description: CN ONE is a consolidated mobile shipment tracking app for CN customers offering real-time cargo monitoring, shipment status, and notifications across the CN rail network.
  name: CN ONE Mobile App
  slug: cn-one-mobile-app
- description: CN eBill is the customer tool for managing rail freight invoices, account statements, and online bill payment. Integrated with the eBusiness portal for end-to-end shipping financial management.
  name: CN eBill
  slug: cn-ebill
artifact_total: 24
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/canadian-national-railway-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cn
- group: company
  title: ''
  type: Website
  url: https://www.cn.ca/
- group: start
  title: ''
  type: Portal
  url: https://ecprod.cn.ca/
- group: other
  title: ''
  type: CustomerCenter
  url: https://www.cn.ca/en/customer-centre/
- group: company
  title: ''
  type: InvestorRelations
  url: https://www.cn.ca/en/investors/
- group: other
  title: ''
  type: Sustainability
  url: https://www.cn.ca/en/sustainability/
created: '2026-05-05'
description: Canadian National Railway (CN) is the largest railway network in Canada and one of the largest in North America spanning over 20,000 route miles. CN transports goods across an integrated network linking the Atlantic and Pacific coasts with the Gulf of Mexico. CN offers shipper APIs, EDI integration, the eBusiness portal, and the CN ONE mobile app for shipment tracking, ordering, billing, and rate management.
features:
- description: Order rail and intermodal shipments via eTools, API, or EDI.
  name: Shipment Ordering
- description: Real-time monitoring of freight across CN's 20,000-mile network.
  name: Cargo Tracking
- description: Order, release, and manage private and CN-owned railcars.
  name: Equipment Management
- description: Manage invoices and payments through CN eBill.
  name: Electronic Billing
- description: Retrieve carload and intermodal pricing through interactive tools.
  name: Rate and Tariff Tools
- description: Automate shipment operations using CN's REST API.
  name: API Integration
- description: Exchange shipping data via Electronic Data Interchange standards.
  name: EDI Integration
- description: Estimate emissions for rail and intermodal shipments.
  name: Carbon Calculator
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/canadian-national-railway.png
integrations:
- description: Interconnection with BNSF, CSX, NS, UP and other North American Class I railroads.
  name: Class I Railroad Interchanges
- description: Intermodal interchange with steamship lines at Atlantic, Pacific, and Gulf ports.
  name: Ocean Carriers
- description: First-mile and last-mile trucking partnerships for door-to-door service.
  name: Trucking and Drayage
- description: Financing partnerships for shippers.
  name: TransUnion Eagle Capital
layout: provider
modified: '2026-07-25'
name: Canadian National Railway
nav: Providers
network: true
overview: 'Canadian National Railway publishes 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Rail, Freight, Transportation, Logistics, and Supply Chain.


  Canadian National Railway''s developer surface includes developer portal and 6 more developer resources.'
random_paper: 0
score:
  band: minimal
  composite: 10.3
  delta: 1.9
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 8.4
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/canadian-national-railway/refs/heads/main/screenshots/canadian-national-railway-2026-06-20T173917.png
security:
- kind: domain-security
  name: Canadian National Railway Domain Security
  slug: canadian-national-railway-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: canadian-national-railway
tags:
- Rail
- Freight
- Transportation
- Logistics
- Supply Chain
- Intermodal
use_cases:
- description: Move finished vehicles and automotive parts across North America.
  name: Automotive Supply Chain
- description: Move bulk grain from prairie origins to ports and processors.
  name: Grain Transportation
- description: Move international and domestic containers between ports and inland terminals.
  name: Intermodal Container Movement
- description: Move tank-car loads of crude, refined fuels, and chemicals.
  name: Petroleum and Chemicals
- description: Move lumber, pulp, and paper products from producers to consumers.
  name: Forest Products
- description: Move retail and consumer goods between distribution centers.
  name: Consumer Goods Distribution
website: https://www.cn.ca/
---
