---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: derived
    openapi_examples: documented
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 45.9
  scored_at: '2026-08-10'
api_count: 6
apis:
- description: 'SOAP web service for serialized operations: commissioning, aggregation, decommissioning, shipment and receipt orders, serial number verification, lot status, market release, sampling, and destruction.'
  name: TraceLink Serialized Operations Manager (SOAP)
  slug: serialized-operations-manager
- description: SOAP web service supporting Product Track pick-and-ship operations for US DSCSA serialized product movement. The WSDL is served publicly from the production API host and declares PickShip and PickShip
  name: TraceLink Product Track (SOAP)
  slug: product-track
- description: SOAP web service for requesting serial numbers from TraceLink Serial Number Exchange, used by packaging lines and contract manufacturers to obtain serial number ranges. The WSDL is served publicly fro
  name: TraceLink Serial Number Exchange (SOAP)
  slug: serial-number-exchange
- description: Synchronous JSON/REST API that acts as an event ledger for serial number observations across pharmacy, warehouse, and supply chain activities. Supports Set Event, Get Event, and Get Result messages wi
  name: TraceLink Smart Event Manager REST API
  slug: smart-event-manager
- description: 'The OPUS Platform exposes one /api/events endpoint per environment. Every operation is a POST to that endpoint carrying a JSON envelope of header (headerVersion, eventName, ownerId, processNetworkId, '
  name: TraceLink OPUS Platform Event API
  slug: opus-events
- description: 'GraphQL endpoint used by the Agile Process Teams app, exposing genericActionCall and genericGetObject fields that dispatch on an action name and a JSON payload. Introspection is authentication-gated; '
  name: TraceLink OPUS GraphQL API
  slug: opus-graphql
artifact_total: 49
asyncapis:
- description: ''
  name: Tracelink Event Surface
  slug: tracelink-event-surface
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/tracelink-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tracelink-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.tracelink.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://opus.tracelink.com/documentation/
- group: docs
  title: ''
  type: Documentation
  url: https://opus.tracelink.com/documentation/2026.1/en-US/som/Content/top_menu/api_guides.htm
- group: docs
  title: ''
  type: APIReference
  url: https://opus.tracelink.com/documentation/2026.1/en-US/api/smart-event-manager/pdfs/smart_event_manager_api_guide_2026.1.pdf
- group: start
  title: ''
  type: GettingStarted
  url: https://github.com/tracelink/code-samples/blob/main/python/Quickstart.MD
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tracelink
- group: operate
  title: ''
  type: Support
  url: https://www.tracelink.com/support
- group: company
  title: ''
  type: Blog
  url: https://www.tracelink.com/about/news-room
- group: commercial
  title: ''
  type: Pricing
  url: https://www.tracelink.com/multienterprise-information-network-tower-mint-pricing
- group: start
  title: ''
  type: Login
  url: https://opus.tracelink.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.tracelink.com/legal-and-trust/api-terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.tracelink.com/legal-and-trust/privacy-policy
- group: build
  title: ''
  type: Examples
  url: https://github.com/tracelink/code-samples
- group: agent
  title: ''
  type: WellKnown
  url: well-known/tracelink-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/tracelink-security.txt
- group: auth
  title: ''
  type: Security
  url: https://www.tracelink.com/legal-and-trust/vulnerability-disclosure-policy
- group: auth
  title: ''
  type: TrustCenter
  url: security/tracelink-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.tracelink.com/legal-and-trust/certifications-and-attestations
- group: design
  title: ''
  type: Conformance
  url: conformance/tracelink-conformance.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/tracelink-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/tracelink-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/tracelink-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/tracelink-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/tracelink-changelog.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/tracelink-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/tracelink-data-model.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/_index.yml
- group: other
  title: ''
  type: WSDL
  url: wsdl/_index.yml
- group: other
  title: ''
  type: EventSurface
  url: asyncapi/tracelink-event-surface.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/tracelink-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/tracelink-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-02'
description: 'TraceLink, Inc. is a Massachusetts-based supply chain digitalization company for the life sciences and healthcare industries, best known for pharmaceutical serialization and track-and-trace compliance (US DSCSA, EU FMD, and roughly two dozen national regimes) delivered on its multienterprise OPUS network platform. TraceLink exposes several distinct integration surfaces rather than one REST API: a set of publicly served SOAP/WSDL services on api.tracelink.com (Serialized Operations Manager, Product Track, Serial Number Exchange), a synchronous REST API for Smart Event Manager, an event-driven OPUS Platform API where every call is a POST to a single /api/events endpoint carrying a header/payload envelope keyed by a fully qualified eventName, a GraphQL endpoint at /api/graphql used by the Agile Process Teams app, and asynchronous B2B message exchange over AS2, SFTP, and HTTP POST using EPCIS, EDI ANSI X12, SAP IDoc, and TraceLink XML canonical documents. Its published API guides,
  canonical JSON Schemas, and code samples are the machine-readable surface catalogued here.'
image: https://www.tracelink.com/themes/custom/tracelink/logo.svg
json_schemas:
- name: Acknowledgment Response
  property_count: 5
  slug: b2b-transaction-processor_canonicalAcknowledgmentResponse_v1
- name: Processing Acknowledgment
  property_count: 5
  slug: b2b-transaction-processor_canonicalProcessingAcknowledgment_v1
- name: Report Sales Shipment
  property_count: 5
  slug: common-traceability-application_canonicalReportSalesShipment_v1
- name: Report Sales Shipment
  property_count: 5
  slug: common-traceability-application_canonicalReportSalesShipment_v3
- name: Serialized Shipment Notice
  property_count: 5
  slug: integrated-business-network_canonicalSerializedShipmentNotice_v1
- name: Advance Ship Notice
  property_count: 5
  slug: multienterprise-process-connect_canonicalAdvanceShipNotice_v1
- name: Advance Ship Notice
  property_count: 5
  slug: multienterprise-process-connect_canonicalAdvanceShipNotice_v4
- name: Batch Master
  property_count: 5
  slug: multienterprise-process-connect_canonicalBatchMaster_v1
- name: Credit Debit Adjustment
  property_count: 5
  slug: multienterprise-process-connect_canonicalCreditDebitAdjustment_v1
- name: Forecast Plan Response
  property_count: 5
  slug: multienterprise-process-connect_canonicalForecastPlanResponse_v1
- name: Forecast Plan
  property_count: 5
  slug: multienterprise-process-connect_canonicalForecastPlan_v1
- name: Forecast Plan
  property_count: 5
  slug: multienterprise-process-connect_canonicalForecastPlan_v2
- name: Inventory Balance
  property_count: 5
  slug: multienterprise-process-connect_canonicalInventoryBalance_v1
- name: Inventory Balance
  property_count: 5
  slug: multienterprise-process-connect_canonicalInventoryBalance_v2
- name: Inventory Update
  property_count: 5
  slug: multienterprise-process-connect_canonicalInventoryUpdate_v1
- name: Inventory Update
  property_count: 5
  slug: multienterprise-process-connect_canonicalInventoryUpdate_v2
- name: Invoice
  property_count: 5
  slug: multienterprise-process-connect_canonicalInvoice_v1
- name: Invoice
  property_count: 5
  slug: multienterprise-process-connect_canonicalInvoice_v2
- name: Invoice
  property_count: 5
  slug: multienterprise-process-connect_canonicalInvoice_v4
- name: Payment Remittance
  property_count: 5
  slug: multienterprise-process-connect_canonicalPaymentRemittance_v1
- name: Payment Remittance
  property_count: 5
  slug: multienterprise-process-connect_canonicalPaymentRemittance_v2
- name: Price Sales Catalog
  property_count: 5
  slug: multienterprise-process-connect_canonicalPriceSalesCatalog_v1
- name: Price Sales Catalog
  property_count: 5
  slug: multienterprise-process-connect_canonicalPriceSalesCatalog_v2
- name: canonical Product Activity
  property_count: 5
  slug: multienterprise-process-connect_canonicalProductActivity_v1
- name: Purchase Order Acknowledgement
  property_count: 5
  slug: multienterprise-process-connect_canonicalPurchaseOrderAcknowledgement_v3
- name: Purchase Order
  property_count: 5
  slug: multienterprise-process-connect_canonicalPurchaseOrder_v3
- name: Purchase Order
  property_count: 5
  slug: multienterprise-process-connect_canonicalPurchaseOrder_v4
- name: Return Authorization
  property_count: 5
  slug: multienterprise-process-connect_canonicalReturnAuthorization_v1
- name: Serialized Shipment Notice
  property_count: 5
  slug: multienterprise-process-connect_canonicalSerializedShipmentNotice_v3
- name: Warehouse Ship Advice
  property_count: 5
  slug: multienterprise-process-connect_canonicalWarehouseShipAdvice_v1
- name: Warehouse Ship Advice
  property_count: 5
  slug: multienterprise-process-connect_canonicalWarehouseShipAdvice_v3
- name: Warehouse Ship Order
  property_count: 5
  slug: multienterprise-process-connect_canonicalWarehouseShipOrder_v1
- name: Warehouse Stock Transfer Receipt Advice
  property_count: 5
  slug: multienterprise-process-connect_canonicalWarehouseStockTransferReceiptAdvice_v1
- name: Warehouse Stock Transfer Receipt Advice
  property_count: 5
  slug: multienterprise-process-connect_canonicalWarehouseStockTransferReceiptAdvice_v2
- name: Warehouse Stock Transfer Receipt Advice
  property_count: 5
  slug: multienterprise-process-connect_canonicalWarehouseStockTransferReceiptAdvice_v3
- name: Warehouse Stock Transfer Ship Advice
  property_count: 5
  slug: multienterprise-process-connect_canonicalWarehouseStockTransferShipAdvice_v1
- name: Warehouse Stock Transfer Ship Advice
  property_count: 5
  slug: multienterprise-process-connect_canonicalWarehouseStockTransferShipAdvice_v3
layout: provider
mcp_servers:
- description: ''
  name: tracelink-mcp.yml
  slug: tracelink-mcpyml
modified: '2026-08-02'
name: TraceLink
nav: Providers
network: true
overview: 'TraceLink publishes 6 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Supply Chain, Pharmaceuticals, Life Sciences, and Serialization.


  The TraceLink catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  TraceLink''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, code examples, and 27 more developer resources.'
random_paper: 29
score:
  band: developing
  composite: 51.3
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 51.6
    developer_ergonomics: 62.5
    discoverability: 92.6
    governance: 12.5
    operational_transparency: 31.6
  previous_composite: 51.3
  provenance:
    conformance: first-party
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 45.0
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
security:
- kind: authentication
  name: Tracelink Authentication
  slug: tracelink-authentication
  summary_line: http · 4 schemes
- kind: domain-security
  name: Tracelink Domain Security
  slug: tracelink-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Tracelink Vulnerability Disclosure
  slug: tracelink-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Tracelink Trust Center
  slug: tracelink-trust-center
  summary_line: ISO/IEC 27001:2022, ISO/IEC 27017:2015, ISO 9001:2015, SOC 2 Type II, ISAE 3000 Type II, CyberVadis
slug: tracelink
tags:
- Company
- Supply Chain
- Pharmaceuticals
- Life Sciences
- Serialization
- Track and Trace
- Compliance
- Healthcare
- EPCIS
- Logistics
- B2B Integration
website: https://www.tracelink.com/
---
