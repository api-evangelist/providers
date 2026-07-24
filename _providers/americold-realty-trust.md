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
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 0.0
  scored_at: '2026-07-23'
api_count: 2
apis:
- description: i-3PL is Americold's customer-facing digital supply chain platform offering real-time inventory tracking, order management, dock appointment scheduling, customizable alerts, and 40+ reporting tools ac
  name: Americold i-3PL Platform
  slug: americold-i-3pl
- description: Americold provides Electronic Data Interchange (EDI) capabilities for automated data exchange between Americold and depositor (customer) systems, supporting orders, inventory, shipments, and other sup
  name: Americold EDI
  slug: americold-edi
artifact_total: 31
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/americold-realty-trust-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/showcase/americold-realty
- group: company
  title: ''
  type: Website
  url: https://www.americold.com
- group: start
  title: ''
  type: Portal
  url: https://www.i-3pl.com/login
- group: other
  title: ''
  type: TechnologyAutomation
  url: https://www.americold.com/technology-automation/
- group: other
  title: ''
  type: CustomerResources
  url: https://www.americold.com/customer-resources/
- group: operate
  title: ''
  type: Contact
  url: https://www.americold.com/contact-us/
- group: company
  title: ''
  type: Careers
  url: https://www.americold.com/careers/
- group: company
  title: ''
  type: InvestorRelations
  url: https://ir.americold.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.americold.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.americold.com/terms-of-use/
- group: design
  title: Americold Realty Trust JSON-LD Context
  type: JSONLD
  url: https://raw.githubusercontent.com/api-evangelist/americold-realty-trust/refs/heads/main/json-ld/americold-realty-trust-context.jsonld
- group: design
  title: Americold Realty Trust Vocabulary
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/americold-realty-trust/refs/heads/main/vocabulary/americold-realty-trust-vocabulary.yaml
- group: agent
  title: ''
  type: LlmsText
  url: https://americold.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://www.americold.com/news
created: '2026-05-04'
description: Americold Realty Trust is a global leader in temperature-controlled logistics, real estate, and value-added services, owning and operating one of the largest networks of cold storage warehouses in the world. The company serves food producers, retailers, and distributors with integrated logistics solutions, offering technology platforms such as i-3PL for customer-facing inventory and order visibility and EDI for system-to-system supply chain integration. While Americold provides customer-facing technology and integration capabilities, it does not currently publish a public developer-facing API portal with open OpenAPI documentation; integrations are established project-by-project through the Americold service desk and EDI onboarding process.
examples:
- key_count: 13
  name: Americold Edi Warehouse Shipping Advice Example
  slug: americold-edi-warehouse-shipping-advice-example
- key_count: 14
  name: Americold Edi Warehouse Shipping Order Example
  slug: americold-edi-warehouse-shipping-order-example
- key_count: 11
  name: Americold I 3Pl Inventory Snapshot Example
  slug: americold-i-3pl-inventory-snapshot-example
features:
- description: Americold owns and operates one of the largest networks of temperature-controlled warehouses worldwide, with facilities across North America, Europe, Australia, New Zealand, and South America serving food producers, processors, distributors, and retailers.
  name: Global Cold Storage Network
- description: Customer-facing digital platform delivering real-time inventory tracking, order management, dock appointment scheduling, customizable alerts, and over 40 reporting tools across the Americold network from phone, tablet, or desktop.
  name: i-3PL Customer Platform
- description: Standards-based X12 EDI exchange of warehousing transactions (940/943/944/945/947) and shipping/inventory transactions (856, 846) between Americold's WMS/TMS/LMS/WES and depositor ERP systems for real-time supply chain visibility.
  name: EDI Supply Chain Integration
- description: Item-lot granularity for receipts, holds, releases, and shipments enables food-safety traceability, recall readiness, and FSMA / HACCP compliance across the cold chain.
  name: Lot-Level Traceability
- description: Storage and handling across deep-frozen, frozen, refrigerated, cooler, and ambient temperature zones with documented temperature requirements and load-temperature recording on outbound shipments.
  name: Multi-Temperature Zones
- description: Blast freezing, pick and pack, labeling and relabeling, repacking, kitting, staging, cross-dock, sloughing/tempering, plus light assembly and food processing services provided alongside storage.
  name: Value-Added Services
image: https://www.americold.com/favicon.ico
integrations:
- description: SPS Commerce provides pre-built EDI connections used by depositors and 3PL trading partners to exchange warehousing transaction sets with Americold over a managed network.
  name: SPS Commerce
- description: Stedi's API-first EDI platform is used by modern engineering teams to translate, validate, and exchange X12 warehouse transactions with Americold programmatically.
  name: Stedi
- description: Cleo provides AS2, SFTP, and API integration tooling commonly used to connect depositor ERP systems to 3PL warehouse partners like Americold.
  name: Cleo Integration Cloud
- description: Americold integrates with leading enterprise ERP systems via EDI for orders, inventory, and shipping reconciliation across the depositor's order-to-cash and procure-to-pay processes.
  name: SAP and Oracle ERP
- description: Americold can integrate its supply chain management systems (WMS, LMS, TMS, WES) with a customer's ERP system for seamless information flow.
  name: Customer ERP Systems
json_schemas:
- name: AmericoldEdiWarehouseShippingAdvice
  property_count: 13
  slug: americold-edi-warehouse-shipping-advice
- name: AmericoldEdiWarehouseShippingOrder
  property_count: 14
  slug: americold-edi-warehouse-shipping-order
- name: AmericoldI3plInventorySnapshot
  property_count: 11
  slug: americold-i-3pl-inventory-snapshot
json_structures:
- name: Americold Edi Warehouse Shipping Advice Structure
  property_count: 13
  slug: americold-edi-warehouse-shipping-advice-structure
- name: Americold Edi Warehouse Shipping Order Structure
  property_count: 14
  slug: americold-edi-warehouse-shipping-order-structure
- name: Americold I 3Pl Inventory Snapshot Structure
  property_count: 11
  slug: americold-i-3pl-inventory-snapshot-structure
jsonld:
- class_count: 8
  name: Americold Realty Trust Context
  property_count: 52
  slug: americold-realty-trust-context
layout: provider
modified: '2026-05-05'
name: Americold Realty Trust
nav: Providers
network: true
overview: 'Americold Realty Trust publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Cold Storage, Logistics, Supply Chain, Warehousing, and Real Estate.


  The Americold Realty Trust catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Americold Realty Trust''s developer surface includes developer portal, engineering blog, and 13 more developer resources.'
random_paper: 25
rules:
- name: Americold Realty Trust API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: americold-realty-trust-jsonschema-spectral-rules
score:
  band: thin
  composite: 35.2
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 39.6
    developer_ergonomics: 10.9
    discoverability: 85.0
    governance: 86.8
    operational_transparency: 0.0
  previous_composite: 35.2
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/americold-realty-trust/refs/heads/main/screenshots/americold-realty-trust-2026-06-20T171923.png
security:
- kind: domain-security
  name: Americold Realty Trust Domain Security
  slug: americold-realty-trust-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: americold-realty-trust
tags:
- Cold Storage
- Logistics
- Supply Chain
- Warehousing
- Real Estate
- Temperature-Controlled
- Cold Chain
- EDI
- 3PL
use_cases:
- description: A depositor sends a 940 Warehouse Shipping Order to an Americold facility; Americold picks, stages, and ships product; a 945 Warehouse Shipping Advice returns to the depositor for ERP reconciliation.
  name: Cold Chain Outbound Fulfillment
- description: Frozen and refrigerated food manufacturers monitor on-hand, available, committed, and held inventory across Americold facilities using i-3PL snapshots, dashboards, and reports.
  name: Inventory Visibility for Food Manufacturers
- description: Carriers and depositor logistics teams book, modify, and cancel dock appointments at Americold facilities through i-3PL to optimize throughput and reduce dwell time.
  name: Dock Appointment Scheduling
- description: Quality assurance and food safety teams trace a lot from receipt through every shipment to support recalls and regulatory holds.
  name: Lot Traceability and Recall
- description: Move inventory between Americold facilities using 943/944 transfer transactions to balance network inventory and meet regional demand.
  name: Stock Transfer Between Facilities
- description: Connect SAP, Oracle, NetSuite, Microsoft Dynamics, and other ERP systems to Americold's WMS through EDI and managed integration partners.
  name: ERP-to-WMS Integration
website: https://www.americold.com
---
