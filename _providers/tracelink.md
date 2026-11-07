---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: documented
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 27.3
  scored_at: '2026-11-06'
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
artifact_total: 55
asyncapis:
- description: ''
  name: Tracelink Event Surface
  slug: tracelink-event-surface
common:
- group: commercial
  href: https://artifacts.apis.io/tracelink/plans/tracelink-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/tracelink-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/tracelink/hosts/tracelink-hosts.yml
  title: ''
  type: Hosts
  url: hosts/tracelink-hosts.yml
- group: build
  href: https://artifacts.apis.io/tracelink/integrations/tracelink-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/tracelink-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/tracelink/vendors/tracelink-vendors.yml
  title: ''
  type: Vendors
  url: vendors/tracelink-vendors.yml
- group: company
  title: ''
  type: BlogRSS
  url: https://www.tracelink.com/rss.xml
- group: auth
  href: https://artifacts.apis.io/tracelink/security/tracelink-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/tracelink-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/tracelink/security/tracelink-domain-security.yml
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
  href: https://artifacts.apis.io/tracelink/well-known/tracelink-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/tracelink-well-known.yml
- group: auth
  href: https://artifacts.apis.io/tracelink/well-known/tracelink-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/tracelink-security.txt
- group: auth
  title: ''
  type: Security
  url: https://www.tracelink.com/legal-and-trust/vulnerability-disclosure-policy
- group: auth
  href: https://artifacts.apis.io/tracelink/security/tracelink-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/tracelink-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.tracelink.com/legal-and-trust/certifications-and-attestations
- group: design
  href: https://artifacts.apis.io/tracelink/conformance/tracelink-conformance.yml
  title: ''
  type: Conformance
  url: conformance/tracelink-conformance.yml
- group: auth
  href: https://artifacts.apis.io/tracelink/authentication/tracelink-authentication.yml
  title: ''
  type: Authentication
  url: authentication/tracelink-authentication.yml
- group: design
  href: https://artifacts.apis.io/tracelink/conventions/tracelink-conventions.yml
  title: ''
  type: Conventions
  url: conventions/tracelink-conventions.yml
- group: design
  href: https://artifacts.apis.io/tracelink/errors/tracelink-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/tracelink-problem-types.yml
- group: design
  href: https://artifacts.apis.io/tracelink/lifecycle/tracelink-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/tracelink-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/tracelink/changelog/tracelink-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/tracelink-changelog.yml
- group: start
  href: https://artifacts.apis.io/tracelink/sandbox/tracelink-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/tracelink-sandbox.yml
- group: design
  href: https://artifacts.apis.io/tracelink/data-model/tracelink-data-model.yml
  title: ''
  type: DataModel
  url: data-model/tracelink-data-model.yml
- group: docs
  href: https://artifacts.apis.io/tracelink/json-schema/_index.yml
  title: ''
  type: JSONSchema
  url: json-schema/_index.yml
- group: other
  href: https://artifacts.apis.io/tracelink/asyncapi/tracelink-event-surface.yml
  title: ''
  type: EventSurface
  url: asyncapi/tracelink-event-surface.yml
- group: agent
  href: https://artifacts.apis.io/tracelink/llms/tracelink-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/tracelink-llms.txt
- group: agent
  href: https://artifacts.apis.io/tracelink/mcp/tracelink-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/tracelink-mcp.yml
- group: agent
  href: https://artifacts.apis.io/tracelink/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
coverage:
  detail: the company publishes developer documentation but serves no machine-readable contract from it
  evidence:
  - status: 200
    url: https://www.tracelink.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-08-02'
description: 'TraceLink, Inc. is a Massachusetts-based supply chain digitalization company for the life sciences and healthcare industries, best known for pharmaceutical serialization and track-and-trace compliance (US DSCSA, EU FMD, and roughly two dozen national regimes) delivered on its multienterprise OPUS network platform. TraceLink exposes several distinct integration surfaces rather than one REST API: a set of publicly served SOAP/WSDL services on api.tracelink.com (Serialized Operations Manager, Product Track, Serial Number Exchange), a synchronous REST API for Smart Event Manager, an event-driven OPUS Platform API where every call is a POST to a single /api/events endpoint carrying a header/payload envelope keyed by a fully qualified eventName, a GraphQL endpoint at /api/graphql used by the Agile Process Teams app, and asynchronous B2B message exchange over AS2, SFTP, and HTTP POST using EPCIS, EDI ANSI X12, SAP IDoc, and TraceLink XML canonical documents. Its published API guides,
  canonical JSON Schemas, and code samples are the machine-readable surface catalogued here.'
finops:
- has_sources: true
  method: derived
  name: Tracelink Finops
  primary_unit: mint link
  service_category: ''
  slug: tracelink-finops
  template: false
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
modified: '2026-10-06'
name: TraceLink
nav: Providers
network: true
overview: 'TraceLink is listed with 6 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Supply Chain, Pharmaceuticals, Life Sciences, and Serialization.


  The TraceLink catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  TraceLink''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, code examples, and 31 more developer resources.'
plans:
- name: Tracelink Plans Pricing
  plan_count: 3
  slug: tracelink-plans-pricing
- name: Tracelink Price Estimates
  plan_count: 0
  slug: tracelink-price-estimates
random_paper: 21
rate_limits:
- limit_count: 0
  name: Tracelink Rate Limits
  slug: tracelink-rate-limits
score:
  band: strong
  composite: 57.5
  coverage:
    artifact_dirs: 26
    catalog_earned: 55.0
    catalog_earned_first_party: 12.0
    catalog_gap: 60.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 93.4
    contract_governance: 18.2
    contract_quality: 45.3
    developer_ergonomics: 56.5
    discoverability: 78.6
    operational_transparency: 28.9
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 57.5
  provenance:
    conformance: first-party
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 28.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/tracelink/tracelink-2026-08-17T082418.png
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
skill_count: 3
skills:
- name: tracelink-open-supplier-incident
  slug: tracelink-open-supplier-incident
- name: tracelink-record-serialized-shipment
  slug: tracelink-record-serialized-shipment
- name: tracelink-verify-serial-number
  slug: tracelink-verify-serial-number
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
