---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 48.0
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 113
  human_in_the_loop: 0
  name: Scoutrfp Agentic Access
  operation_count: 208
  slug: scoutrfp-agentic-access
  summary_line: 208 operations · 113 acting
api_count: 46
apis:
- description: 'Use the attachments API to create, update, and delete the attachments in Workday Strategic Sourcing. ## Working with Attachments Creating attachments for Workday Strategic Sourcing objects is a two-st'
  name: Scout RFP (Workday Strategic Sourcing) attachments API
  slug: scoutrfp-attachments-api
- description: 'Use the Award Line Items API to query the Award Line Items in Workday Strategic Sourcing. Award Line Items are used for procurement. ## Award Line Item Object <SchemaDefinition schemaRef="#/components'
  name: Scout RFP (Workday Strategic Sourcing) award_line_items API
  slug: scoutrfp-award-line-items-api
- description: 'Use the Awards API to query the Awards in Workday Strategic Sourcing. Awards are used for procurement. ## Award Object <SchemaDefinition schemaRef="#/components/schemas/Award" showReadOnly={true} show'
  name: Scout RFP (Workday Strategic Sourcing) awards API
  slug: scoutrfp-awards-api
- description: 'Use the bid line items API to query the bid line items in Workday Strategic Sourcing. ## Bid Line Item Object <SchemaDefinition schemaRef="#/components/schemas/BidLineItem" exampleRef="#/components/ex'
  name: Scout RFP (Workday Strategic Sourcing) bid_line_items API
  slug: scoutrfp-bid-line-items-api
- description: 'Use the bids API to query the bids in Workday Strategic Sourcing. Only bids for events of type `RFP` are supported. ## Bid Object <SchemaDefinition schemaRef="#/components/schemas/Bid" exampleRef="#/c'
  name: Scout RFP (Workday Strategic Sourcing) bids API
  slug: scoutrfp-bids-api
- description: 'Use the contact types API to create, update, and query the contact types in Workday Strategic Sourcing. ## ContactType Object <SchemaDefinition schemaRef="#/components/schemas/ContactType" showReadOnl'
  name: Scout RFP (Workday Strategic Sourcing) contact_types API
  slug: scoutrfp-contact-types-api
- description: This report returns a list of contract milestone report entries.
  name: Scout RFP (Workday Strategic Sourcing) contract_milestone_reports API
  slug: scoutrfp-contract-milestone-reports-api
- description: This report returns a list of contract report entries.
  name: Scout RFP (Workday Strategic Sourcing) contract_reports API
  slug: scoutrfp-contract-reports-api
- description: Use the contract types API to query the contract types in Workday Strategic Sourcing. Contract Types are used in the contract resource. On POST and PATCH related endpoints for this resource a contract
  name: Scout RFP (Workday Strategic Sourcing) contract_types API
  slug: scoutrfp-contract-types-api
- description: 'Use the contracts API to create, update, and query the contracts in Workday Strategic Sourcing. ## Contract Object <SchemaDefinition schemaRef="#/components/schemas/Contract" exampleRef="#/components/'
  name: Scout RFP (Workday Strategic Sourcing) contracts API
  slug: scoutrfp-contracts-api
- description: Endpoints to facilitate discovery of SCIM service provider features
  name: Scout RFP (Workday Strategic Sourcing) discovery API
  slug: scoutrfp-discovery-api
- description: This report returns a list of event report entries.
  name: Scout RFP (Workday Strategic Sourcing) event_reports API
  slug: scoutrfp-event-reports-api
- description: Use the event supplier companies API to manage event suppliers.
  name: Scout RFP (Workday Strategic Sourcing) event_supplier_companies API
  slug: scoutrfp-event-supplier-companies-api
- description: 'Use the event supplier contacts API to manage event suppliers. This API provides 2 advantages over the event supplier companies APIs: - It allows specifying the supplier contact to be associated/remov'
  name: Scout RFP (Workday Strategic Sourcing) event_supplier_contacts API
  slug: scoutrfp-event-supplier-contacts-api
- description: 'Use the contract types API to query the event templates in Workday Strategic Sourcing. Event Templates are used as a blueprint for newly created events. ## Event Template Object <SchemaDefinition sche'
  name: Scout RFP (Workday Strategic Sourcing) event_templates API
  slug: scoutrfp-event-templates-api
- description: 'Use the events API to create, update, and query the events in Workday Strategic Sourcing. ## Event Object <SchemaDefinition schemaRef="#/components/schemas/Event" exampleRef="#/components/examples/Eve'
  name: Scout RFP (Workday Strategic Sourcing) events API
  slug: scoutrfp-events-api
- description: Use the fields API to create, update, and query the custom fields groups in Workday Strategic Sourcing. Custom field groups act as a collection of custom fields. Every newly made custom field with req
  name: Scout RFP (Workday Strategic Sourcing) field_groups API
  slug: scoutrfp-field-groups-api
- description: 'Use the fields API to create, update, and query the custom fields options in Workday Strategic Sourcing. Custom field options exist for single select and multiple select field types. ## Field Option O'
  name: Scout RFP (Workday Strategic Sourcing) field_options API
  slug: scoutrfp-field-options-api
- description: 'Use the fields API to create, update, and query the custom fields in Workday Strategic Sourcing. ## Field Object <SchemaDefinition schemaRef="#/components/schemas/Field" showReadOnly={true} showWriteO'
  name: Scout RFP (Workday Strategic Sourcing) fields API
  slug: scoutrfp-fields-api
- description: 'Use the line items API to create, update, and query the worksheet line items in Workday Strategic Sourcing. ## Line Item Object <SchemaDefinition schemaRef="#/components/schemas/LineItem" showReadOnly'
  name: Scout RFP (Workday Strategic Sourcing) line_items API
  slug: scoutrfp-line-items-api
- description: 'Use the payment currencies API to create, update, and query the payment currencies in Workday Strategic Sourcing. ## Payment Currency Object <SchemaDefinition schemaRef="#/components/schemas/PaymentCu'
  name: Scout RFP (Workday Strategic Sourcing) payment_currencies API
  slug: scoutrfp-payment-currencies-api
- description: 'Use the payment terms API to create, update, and query the payment terms in Workday Strategic Sourcing. ## Payment Term Object <SchemaDefinition schemaRef="#/components/schemas/PaymentTerm" showReadOn'
  name: Scout RFP (Workday Strategic Sourcing) payment_terms API
  slug: scoutrfp-payment-terms-api
- description: 'Use the payment types API to create, update, and query the payment types in Workday Strategic Sourcing. ## Payment Type Object <SchemaDefinition schemaRef="#/components/schemas/PaymentType" showReadOn'
  name: Scout RFP (Workday Strategic Sourcing) payment_types API
  slug: scoutrfp-payment-types-api
- description: This report returns a list of Performance Review Answer report entries.
  name: Scout RFP (Workday Strategic Sourcing) performance_review_answer_reports API
  slug: scoutrfp-performance-review-answer-reports-api
- description: This report returns a list of Performance Review report entries.
  name: Scout RFP (Workday Strategic Sourcing) performance_review_reports API
  slug: scoutrfp-performance-review-reports-api
- description: This report returns a list of Project Milestone report entries.
  name: Scout RFP (Workday Strategic Sourcing) project_milestone_reports API
  slug: scoutrfp-project-milestone-reports-api
- description: This report returns a list of Project report entries.
  name: Scout RFP (Workday Strategic Sourcing) project_reports API
  slug: scoutrfp-project-reports-api
- description: Use the project supplier companies API to manage project suppliers.
  name: Scout RFP (Workday Strategic Sourcing) project_supplier_companies API
  slug: scoutrfp-project-supplier-companies-api
- description: 'Use the project supplier contacts API to manage project suppliers. This API provides 2 advantages over the project supplier companies APIs: - It allows specifying the supplier contact to be associated'
  name: Scout RFP (Workday Strategic Sourcing) project_supplier_contacts API
  slug: scoutrfp-project-supplier-contacts-api
- description: Use the project types API to query the project types in Workday Strategic Sourcing. Project Types are used in the project resource. On POST and PATCH related endpoints for this resource a project_type
  name: Scout RFP (Workday Strategic Sourcing) project_types API
  slug: scoutrfp-project-types-api
- description: 'Use the projects API to create, update, and query the projects in Workday Strategic Sourcing. ## Project Object <SchemaDefinition schemaRef="#/components/schemas/Project" exampleRef="#/components/exam'
  name: Scout RFP (Workday Strategic Sourcing) projects API
  slug: scoutrfp-projects-api
- description: This report returns a list of Savings report entries.
  name: Scout RFP (Workday Strategic Sourcing) savings_reports API
  slug: scoutrfp-savings-reports-api
- description: Use the Spend Categories API to create, update, and query the Spend Categories in Workday Strategic Sourcing. Spend Categories are used in both the project and contract resources. On POST and PATCH re
  name: Scout RFP (Workday Strategic Sourcing) spend_categories API
  slug: scoutrfp-spend-categories-api
- description: 'Use the supplier categories API to create, update, and query the supplier categories in Workday Strategic Sourcing. ## Supplier Category Object <SchemaDefinition schemaRef="#/components/schemas/Suppli'
  name: Scout RFP (Workday Strategic Sourcing) supplier_categories API
  slug: scoutrfp-supplier-categories-api
- description: '## Supplier Classification Object <SchemaDefinition schemaRef="#/components/schemas/SupplierClassification" exampleRef="#/components/examples/SupplierClassification" showReadOnly={true} showWriteOnly='
  name: Scout RFP (Workday Strategic Sourcing) supplier_classifications API
  slug: scoutrfp-supplier-classifications-api
- description: 'Use the supplier companies API to create, update, and query the suppliers in Workday Strategic Sourcing. ## Supplier Company Object <SchemaDefinition schemaRef="#/components/schemas/SupplierCompany" e'
  name: Scout RFP (Workday Strategic Sourcing) supplier_companies API
  slug: scoutrfp-supplier-companies-api
- description: 'Use the supplier company risks API to create, update, and query the supplier company risks in Workday Strategic Sourcing. ## Supplier Company Risk Object <SchemaDefinition schemaRef="#/components/sche'
  name: Scout RFP (Workday Strategic Sourcing) supplier_company_risks API
  slug: scoutrfp-supplier-company-risks-api
- description: 'Use the supplier company segmentation statuses API to create, update, and query the supplier company segmentation statuses in Workday Strategic Sourcing. ## Supplier Company Segmentation Status Object'
  name: Scout RFP (Workday Strategic Sourcing) supplier_company_segmentation_statuses API
  slug: scoutrfp-supplier-company-segmentation-statuses-api
- description: 'Use the supplier company segmentations API to create, update, and query the supplier company segmentations in Workday Strategic Sourcing. ## Supplier Company Segmentation Object <SchemaDefinition sche'
  name: Scout RFP (Workday Strategic Sourcing) supplier_company_segmentations API
  slug: scoutrfp-supplier-company-segmentations-api
- description: '## Supplier Contact Object <SchemaDefinition schemaRef="#/components/schemas/SupplierContact" exampleRef="#/components/examples/SupplierContact" showReadOnly={true} showWriteOnly={true} />'
  name: Scout RFP (Workday Strategic Sourcing) supplier_contacts API
  slug: scoutrfp-supplier-contacts-api
- description: 'Use the supplier groups API to create, update, and query the supplier groups in Workday Strategic Sourcing. ## Supplier Group Object <SchemaDefinition schemaRef="#/components/schemas/SupplierGroup" sh'
  name: Scout RFP (Workday Strategic Sourcing) supplier_groups API
  slug: scoutrfp-supplier-groups-api
- description: This report returns a list of Supplier report entries.
  name: Scout RFP (Workday Strategic Sourcing) supplier_reports API
  slug: scoutrfp-supplier-reports-api
- description: This report returns a list of Supplier Review report entries.
  name: Scout RFP (Workday Strategic Sourcing) supplier_review_reports API
  slug: scoutrfp-supplier-review-reports-api
- description: This report returns a list of Suppliers.
  name: Scout RFP (Workday Strategic Sourcing) suppliers API
  slug: scoutrfp-suppliers-api
- description: 'Use the users API to create, update, and query the users in Workday Strategic Sourcing. ## User Object <SchemaDefinition schemaRef="#/components/schemas/UserResource" exampleRef="#/components/examples'
  name: Scout RFP (Workday Strategic Sourcing) user API
  slug: scoutrfp-user-api
- description: 'Use the worksheets API to create, update, and query the worksheets in Workday Strategic Sourcing. ## Worksheet Object <SchemaDefinition schemaRef="#/components/schemas/WorksheetModel" showReadOnly={tr'
  name: Scout RFP (Workday Strategic Sourcing) worksheets API
  slug: scoutrfp-worksheets-api
artifact_total: 52
common:
- group: company
  title: ''
  type: Website
  url: https://www.workday.com/en-us/products/spend-management/strategic-sourcing.html
- group: start
  title: ''
  type: DeveloperPortal
  url: https://apidocs.workdayspend.com/
- group: docs
  title: ''
  type: Documentation
  url: https://apidocs.workdayspend.com/
- group: docs
  title: ''
  type: APIReference
  url: https://apidocs.workdayspend.com/services/suppliers/v1.html
- group: start
  title: ''
  type: GettingStarted
  url: https://apidocs.workdayspend.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://apidocs.workdayspend.com/services/suppliers/v1.html
- group: auth
  title: ''
  type: Authentication
  url: authentication/scoutrfp-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/scoutrfp-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/scoutrfp-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/scoutrfp-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/scoutrfp-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/scoutrfp-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/scoutrfp-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://security.workday.com/
- group: auth
  title: ''
  type: TrustCenter
  url: security/scoutrfp-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/scoutrfp-domain-security.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/scoutrfp-data-model.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/scoutrfp-agentic-access.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/scoutrfp-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/scoutrfp-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/scoutrfp-run-sourcing-event.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/scoutrfp-onboard-supplier.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/scoutrfp-provision-users-scim.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/scoutrfp-manage-contract.md
- group: other
  title: ''
  type: Overlay
  url: overlays/scoutrfp-suppliers-v1-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/scoutrfp-events-v1-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/scoutrfp-contracts-v1-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/scoutrfp-projects-v1-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/scoutrfp-payments-v1-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/scoutrfp-scim-v2-overlay.yaml
created: '2026-07-17'
description: Scout RFP is a strategic sourcing and supplier engagement platform founded in 2014 and acquired by Workday in 2019, where it now ships as Workday Strategic Sourcing. The product covers sourcing events (RFPs/RFIs/RFQs and auctions), supplier management, contracts, projects, spend categories, awards, and supplier payments. Its public developer platform exposes a JSON:API-conformant REST API across eleven versioned services — Suppliers, Events, Reports, Contracts, Projects, Payments, Fields, Awards, Attachments, and Spend Categories — plus a SCIM 2.0 user-provisioning API. Authentication is by company API key plus a per-user personal token, all calls are HTTPS/JSON:API, cursor paginated, and rate limited to five requests per second. The legacy v3 API on api.scoutrfp.com was sunset April 18, 2025 in favor of the versioned services on api.us.workdayspend.com (with EU and CA regional hosts).
image: https://www.workday.com/content/dam/web/en-us/images/social/workday-og-image.png
layout: provider
mcp_servers:
- description: ''
  name: scoutrfp-mcp.yml
  slug: scoutrfp-mcpyml
modified: '2026-07-21'
name: Scout RFP (Workday Strategic Sourcing)
nav: Providers
network: true
overview: 'Scout RFP (Workday Strategic Sourcing) publishes 46 APIs on the [APIs.io](https://apis.io/) network, including attachments API, award_line_items API, awards API, and 43 more. Tagged areas include Company, Enterprise, Procurement, Strategic Sourcing, and Supplier Management.


  Scout RFP (Workday Strategic Sourcing)''s developer surface includes documentation, API reference, getting-started guide, changelog, authentication, and 25 more developer resources.'
random_paper: 95
rate_limits:
- limit_count: 1
  name: Scoutrfp Rate Limits
  slug: scoutrfp-rate-limits
score:
  band: developing
  composite: 42.4
  delta: 0.0
  facets:
    commercial_clarity: 15.8
    contract_quality: 63.5
    developer_ergonomics: 49.5
    discoverability: 63.0
    governance: 11.5
    operational_transparency: 44.7
  previous_composite: 42.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 46
    mcp: derived
    skills: derived
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
security:
- kind: authentication
  name: Scoutrfp Authentication
  slug: scoutrfp-authentication
  summary_line: apiKey/http · 4 schemes
- kind: domain-security
  name: Scoutrfp Domain Security
  slug: scoutrfp-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Scoutrfp Trust Center
  slug: scoutrfp-trust-center
  summary_line: SOC 2, ISO 27001, FedRAMP, GDPR
slug: scoutrfp
tags:
- Company
- Enterprise
- Procurement
- Strategic Sourcing
- Supplier Management
- Spend Management
- RFP
- Contracts
- SCIM
- JSON:API
website: https://www.workday.com/en-us/products/spend-management/strategic-sourcing.html
---
