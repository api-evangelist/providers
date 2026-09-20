---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 31.5
  scored_at: '2026-09-19'
agentic_access:
- acting_count: 113
  human_in_the_loop: 0
  name: Scoutrfp Agentic Access
  operation_count: 208
  slug: scoutrfp-agentic-access
  summary_line: 208 operations · 113 acting
api_count: 11
apis:
- baseURL: https://api.us.workdayspend.com/services/suppliers/v1
  baseurl_source: declared
  description: 'Use the attachments API to create, update, and delete the attachments in Workday Strategic Sourcing. ## Working with Attachments Creating attachments for Workday Strategic Sourcing objects is a two-st'
  name: Scout RFP (Workday Strategic Sourcing) attachments API
  slug: scoutrfp-attachments-api
- baseURL: https://api.us.workdayspend.com/services/suppliers/v1
  baseurl_source: declared
  description: 'Use the Award Line Items API to query the Award Line Items in Workday Strategic Sourcing. Award Line Items are used for procurement. ## Award Line Item Object <SchemaDefinition schemaRef="#/components'
  name: Scout RFP (Workday Strategic Sourcing) award_line_items API
  slug: scoutrfp-award-line-items-api
- baseURL: https://api.us.workdayspend.com/services/suppliers/v1
  baseurl_source: declared
  description: 'Use the Awards API to query the Awards in Workday Strategic Sourcing. Awards are used for procurement. ## Award Object <SchemaDefinition schemaRef="#/components/schemas/Award" showReadOnly={true} show'
  name: Scout RFP (Workday Strategic Sourcing) awards API
  slug: scoutrfp-awards-api
- baseURL: https://api.us.workdayspend.com/services/suppliers/v1
  baseurl_source: declared
  description: 'Use the bid line items API to query the bid line items in Workday Strategic Sourcing. ## Bid Line Item Object <SchemaDefinition schemaRef="#/components/schemas/BidLineItem" exampleRef="#/components/ex'
  name: Scout RFP (Workday Strategic Sourcing) bid_line_items API
  slug: scoutrfp-bid-line-items-api
- baseURL: https://api.us.workdayspend.com/services/suppliers/v1
  baseurl_source: declared
  description: 'Use the bids API to query the bids in Workday Strategic Sourcing. Only bids for events of type `RFP` are supported. ## Bid Object <SchemaDefinition schemaRef="#/components/schemas/Bid" exampleRef="#/c'
  name: Scout RFP (Workday Strategic Sourcing) bids API
  slug: scoutrfp-bids-api
- baseURL: https://api.us.workdayspend.com/services/suppliers/v1
  baseurl_source: declared
  description: 'Use the contact types API to create, update, and query the contact types in Workday Strategic Sourcing. ## ContactType Object <SchemaDefinition schemaRef="#/components/schemas/ContactType" showReadOnl'
  name: Scout RFP (Workday Strategic Sourcing) contact_types API
  slug: scoutrfp-contact-types-api
- baseURL: https://api.us.workdayspend.com/services/suppliers/v1
  baseurl_source: declared
  description: This report returns a list of contract milestone report entries.
  name: Scout RFP (Workday Strategic Sourcing) contract_milestone_reports API
  slug: scoutrfp-contract-milestone-reports-api
- baseURL: https://api.us.workdayspend.com/services/suppliers/v1
  baseurl_source: declared
  description: This report returns a list of contract report entries.
  name: Scout RFP (Workday Strategic Sourcing) contract_reports API
  slug: scoutrfp-contract-reports-api
- baseURL: https://api.us.workdayspend.com/services/suppliers/v1
  baseurl_source: declared
  description: Use the contract types API to query the contract types in Workday Strategic Sourcing. Contract Types are used in the contract resource. On POST and PATCH related endpoints for this resource a contract
  name: Scout RFP (Workday Strategic Sourcing) contract_types API
  slug: scoutrfp-contract-types-api
- baseURL: https://api.us.workdayspend.com/services/suppliers/v1
  baseurl_source: declared
  description: 'Use the contracts API to create, update, and query the contracts in Workday Strategic Sourcing. ## Contract Object <SchemaDefinition schemaRef="#/components/schemas/Contract" exampleRef="#/components/'
  name: Scout RFP (Workday Strategic Sourcing) contracts API
  slug: scoutrfp-contracts-api
- baseURL: https://api.us.workdayspend.com/services/suppliers/v1
  baseurl_source: declared
  description: Endpoints to facilitate discovery of SCIM service provider features
  name: Scout RFP (Workday Strategic Sourcing) discovery API
  slug: scoutrfp-discovery-api
- baseURL: https://api.us.workdayspend.com/services/suppliers/v1
  baseurl_source: declared
  description: This report returns a list of event report entries.
  name: Scout RFP (Workday Strategic Sourcing) event_reports API
  slug: scoutrfp-event-reports-api
- baseURL: https://api.us.workdayspend.com/services/suppliers/v1
  baseurl_source: declared
  description: Use the event supplier companies API to manage event suppliers.
  name: Scout RFP (Workday Strategic Sourcing) event_supplier_companies API
  slug: scoutrfp-event-supplier-companies-api
- baseURL: https://api.us.workdayspend.com/services/suppliers/v1
  baseurl_source: declared
  description: 'Use the event supplier contacts API to manage event suppliers. This API provides 2 advantages over the event supplier companies APIs: - It allows specifying the supplier contact to be associated/remov'
  name: Scout RFP (Workday Strategic Sourcing) event_supplier_contacts API
  slug: scoutrfp-event-supplier-contacts-api
- baseURL: https://api.us.workdayspend.com/services/suppliers/v1
  baseurl_source: declared
  description: 'Use the contract types API to query the event templates in Workday Strategic Sourcing. Event Templates are used as a blueprint for newly created events. ## Event Template Object <SchemaDefinition sche'
  name: Scout RFP (Workday Strategic Sourcing) event_templates API
  slug: scoutrfp-event-templates-api
- baseURL: https://api.us.workdayspend.com/services/suppliers/v1
  baseurl_source: declared
  description: 'Use the events API to create, update, and query the events in Workday Strategic Sourcing. ## Event Object <SchemaDefinition schemaRef="#/components/schemas/Event" exampleRef="#/components/examples/Eve'
  name: Scout RFP (Workday Strategic Sourcing) events API
  slug: scoutrfp-events-api
- baseURL: https://api.us.workdayspend.com/services/suppliers/v1
  baseurl_source: declared
  description: Use the fields API to create, update, and query the custom fields groups in Workday Strategic Sourcing. Custom field groups act as a collection of custom fields. Every newly made custom field with req
  name: Scout RFP (Workday Strategic Sourcing) field_groups API
  slug: scoutrfp-field-groups-api
- baseURL: https://api.us.workdayspend.com/services/suppliers/v1
  baseurl_source: declared
  description: 'Use the fields API to create, update, and query the custom fields options in Workday Strategic Sourcing. Custom field options exist for single select and multiple select field types. ## Field Option O'
  name: Scout RFP (Workday Strategic Sourcing) field_options API
  slug: scoutrfp-field-options-api
- baseURL: https://api.us.workdayspend.com/services/suppliers/v1
  baseurl_source: declared
  description: 'Use the fields API to create, update, and query the custom fields in Workday Strategic Sourcing. ## Field Object <SchemaDefinition schemaRef="#/components/schemas/Field" showReadOnly={true} showWriteO'
  name: Scout RFP (Workday Strategic Sourcing) fields API
  slug: scoutrfp-fields-api
- baseURL: https://api.us.workdayspend.com/services/suppliers/v1
  baseurl_source: declared
  description: 'Use the line items API to create, update, and query the worksheet line items in Workday Strategic Sourcing. ## Line Item Object <SchemaDefinition schemaRef="#/components/schemas/LineItem" showReadOnly'
  name: Scout RFP (Workday Strategic Sourcing) line_items API
  slug: scoutrfp-line-items-api
- baseURL: https://api.us.workdayspend.com/services/suppliers/v1
  baseurl_source: declared
  description: 'Use the payment currencies API to create, update, and query the payment currencies in Workday Strategic Sourcing. ## Payment Currency Object <SchemaDefinition schemaRef="#/components/schemas/PaymentCu'
  name: Scout RFP (Workday Strategic Sourcing) payment_currencies API
  slug: scoutrfp-payment-currencies-api
- baseURL: https://api.us.workdayspend.com/services/suppliers/v1
  baseurl_source: declared
  description: 'Use the payment terms API to create, update, and query the payment terms in Workday Strategic Sourcing. ## Payment Term Object <SchemaDefinition schemaRef="#/components/schemas/PaymentTerm" showReadOn'
  name: Scout RFP (Workday Strategic Sourcing) payment_terms API
  slug: scoutrfp-payment-terms-api
- baseURL: https://api.us.workdayspend.com/services/suppliers/v1
  baseurl_source: declared
  description: 'Use the payment types API to create, update, and query the payment types in Workday Strategic Sourcing. ## Payment Type Object <SchemaDefinition schemaRef="#/components/schemas/PaymentType" showReadOn'
  name: Scout RFP (Workday Strategic Sourcing) payment_types API
  slug: scoutrfp-payment-types-api
- baseURL: https://api.us.workdayspend.com/services/suppliers/v1
  baseurl_source: declared
  description: This report returns a list of Performance Review Answer report entries.
  name: Scout RFP (Workday Strategic Sourcing) performance_review_answer_reports API
  slug: scoutrfp-performance-review-answer-reports-api
- baseURL: https://api.us.workdayspend.com/services/suppliers/v1
  baseurl_source: declared
  description: This report returns a list of Performance Review report entries.
  name: Scout RFP (Workday Strategic Sourcing) performance_review_reports API
  slug: scoutrfp-performance-review-reports-api
- baseURL: https://api.us.workdayspend.com/services/suppliers/v1
  baseurl_source: declared
  description: This report returns a list of Project Milestone report entries.
  name: Scout RFP (Workday Strategic Sourcing) project_milestone_reports API
  slug: scoutrfp-project-milestone-reports-api
- baseURL: https://api.us.workdayspend.com/services/suppliers/v1
  baseurl_source: declared
  description: This report returns a list of Project report entries.
  name: Scout RFP (Workday Strategic Sourcing) project_reports API
  slug: scoutrfp-project-reports-api
- baseURL: https://api.us.workdayspend.com/services/suppliers/v1
  baseurl_source: declared
  description: Use the project supplier companies API to manage project suppliers.
  name: Scout RFP (Workday Strategic Sourcing) project_supplier_companies API
  slug: scoutrfp-project-supplier-companies-api
- baseURL: https://api.us.workdayspend.com/services/suppliers/v1
  baseurl_source: declared
  description: 'Use the project supplier contacts API to manage project suppliers. This API provides 2 advantages over the project supplier companies APIs: - It allows specifying the supplier contact to be associated'
  name: Scout RFP (Workday Strategic Sourcing) project_supplier_contacts API
  slug: scoutrfp-project-supplier-contacts-api
- baseURL: https://api.us.workdayspend.com/services/suppliers/v1
  baseurl_source: declared
  description: Use the project types API to query the project types in Workday Strategic Sourcing. Project Types are used in the project resource. On POST and PATCH related endpoints for this resource a project_type
  name: Scout RFP (Workday Strategic Sourcing) project_types API
  slug: scoutrfp-project-types-api
- baseURL: https://api.us.workdayspend.com/services/suppliers/v1
  baseurl_source: declared
  description: 'Use the projects API to create, update, and query the projects in Workday Strategic Sourcing. ## Project Object <SchemaDefinition schemaRef="#/components/schemas/Project" exampleRef="#/components/exam'
  name: Scout RFP (Workday Strategic Sourcing) projects API
  slug: scoutrfp-projects-api
- baseURL: https://api.us.workdayspend.com/services/suppliers/v1
  baseurl_source: declared
  description: This report returns a list of Savings report entries.
  name: Scout RFP (Workday Strategic Sourcing) savings_reports API
  slug: scoutrfp-savings-reports-api
- baseURL: https://api.us.workdayspend.com/services/suppliers/v1
  baseurl_source: declared
  description: Use the Spend Categories API to create, update, and query the Spend Categories in Workday Strategic Sourcing. Spend Categories are used in both the project and contract resources. On POST and PATCH re
  name: Scout RFP (Workday Strategic Sourcing) spend_categories API
  slug: scoutrfp-spend-categories-api
- baseURL: https://api.us.workdayspend.com/services/suppliers/v1
  baseurl_source: declared
  description: 'Use the supplier categories API to create, update, and query the supplier categories in Workday Strategic Sourcing. ## Supplier Category Object <SchemaDefinition schemaRef="#/components/schemas/Suppli'
  name: Scout RFP (Workday Strategic Sourcing) supplier_categories API
  slug: scoutrfp-supplier-categories-api
- baseURL: https://api.us.workdayspend.com/services/suppliers/v1
  baseurl_source: declared
  description: '## Supplier Classification Object <SchemaDefinition schemaRef="#/components/schemas/SupplierClassification" exampleRef="#/components/examples/SupplierClassification" showReadOnly={true} showWriteOnly='
  name: Scout RFP (Workday Strategic Sourcing) supplier_classifications API
  slug: scoutrfp-supplier-classifications-api
- baseURL: https://api.us.workdayspend.com/services/suppliers/v1
  baseurl_source: declared
  description: 'Use the supplier companies API to create, update, and query the suppliers in Workday Strategic Sourcing. ## Supplier Company Object <SchemaDefinition schemaRef="#/components/schemas/SupplierCompany" e'
  name: Scout RFP (Workday Strategic Sourcing) supplier_companies API
  slug: scoutrfp-supplier-companies-api
- baseURL: https://api.us.workdayspend.com/services/suppliers/v1
  baseurl_source: declared
  description: 'Use the supplier company risks API to create, update, and query the supplier company risks in Workday Strategic Sourcing. ## Supplier Company Risk Object <SchemaDefinition schemaRef="#/components/sche'
  name: Scout RFP (Workday Strategic Sourcing) supplier_company_risks API
  slug: scoutrfp-supplier-company-risks-api
- baseURL: https://api.us.workdayspend.com/services/suppliers/v1
  baseurl_source: declared
  description: 'Use the supplier company segmentation statuses API to create, update, and query the supplier company segmentation statuses in Workday Strategic Sourcing. ## Supplier Company Segmentation Status Object'
  name: Scout RFP (Workday Strategic Sourcing) supplier_company_segmentation_statuses API
  slug: scoutrfp-supplier-company-segmentation-statuses-api
- baseURL: https://api.us.workdayspend.com/services/suppliers/v1
  baseurl_source: declared
  description: 'Use the supplier company segmentations API to create, update, and query the supplier company segmentations in Workday Strategic Sourcing. ## Supplier Company Segmentation Object <SchemaDefinition sche'
  name: Scout RFP (Workday Strategic Sourcing) supplier_company_segmentations API
  slug: scoutrfp-supplier-company-segmentations-api
- baseURL: https://api.us.workdayspend.com/services/suppliers/v1
  baseurl_source: declared
  description: '## Supplier Contact Object <SchemaDefinition schemaRef="#/components/schemas/SupplierContact" exampleRef="#/components/examples/SupplierContact" showReadOnly={true} showWriteOnly={true} />'
  name: Scout RFP (Workday Strategic Sourcing) supplier_contacts API
  slug: scoutrfp-supplier-contacts-api
- baseURL: https://api.us.workdayspend.com/services/suppliers/v1
  baseurl_source: declared
  description: 'Use the supplier groups API to create, update, and query the supplier groups in Workday Strategic Sourcing. ## Supplier Group Object <SchemaDefinition schemaRef="#/components/schemas/SupplierGroup" sh'
  name: Scout RFP (Workday Strategic Sourcing) supplier_groups API
  slug: scoutrfp-supplier-groups-api
- baseURL: https://api.us.workdayspend.com/services/suppliers/v1
  baseurl_source: declared
  description: This report returns a list of Supplier report entries.
  name: Scout RFP (Workday Strategic Sourcing) supplier_reports API
  slug: scoutrfp-supplier-reports-api
- baseURL: https://api.us.workdayspend.com/services/suppliers/v1
  baseurl_source: declared
  description: This report returns a list of Supplier Review report entries.
  name: Scout RFP (Workday Strategic Sourcing) supplier_review_reports API
  slug: scoutrfp-supplier-review-reports-api
- baseURL: https://api.us.workdayspend.com/services/suppliers/v1
  baseurl_source: declared
  description: This report returns a list of Suppliers.
  name: Scout RFP (Workday Strategic Sourcing) suppliers API
  slug: scoutrfp-suppliers-api
- baseURL: https://api.us.workdayspend.com/services/suppliers/v1
  baseurl_source: declared
  description: 'Use the users API to create, update, and query the users in Workday Strategic Sourcing. ## User Object <SchemaDefinition schemaRef="#/components/schemas/UserResource" exampleRef="#/components/examples'
  name: Scout RFP (Workday Strategic Sourcing) user API
  slug: scoutrfp-user-api
- baseURL: https://api.us.workdayspend.com/services/suppliers/v1
  baseurl_source: declared
  description: 'Use the worksheets API to create, update, and query the worksheets in Workday Strategic Sourcing. ## Worksheet Object <SchemaDefinition schemaRef="#/components/schemas/WorksheetModel" showReadOnly={tr'
  name: Scout RFP (Workday Strategic Sourcing) worksheets API
  slug: scoutrfp-worksheets-api
- description: Manage sourcing events including RFPs, RFIs, and reverse auctions. Supports creating events from templates, updating event details, managing supplier invitations, worksheets, line items, and bid colle
  name: Events API
  slug: events-api
- description: Manage contracts within the strategic sourcing platform, including creation, retrieval, and updates. Version 1.1 of the API.
  name: Contracts API
  slug: contracts-api
- description: Manage sourcing award decisions for completed events, tracking supplier selection outcomes and award values. Version 1.1.
  name: Awards API
  slug: awards-api
- description: Upload and manage file attachments associated with sourcing events, contracts, and other procurement objects. Version 1.0.
  name: Attachments API
  slug: attachments-api
- description: Manage payment records associated with procurement transactions and contract fulfillment. Version 1.0.
  name: Payments API
  slug: payments-api
- description: Manage procurement projects that organize and group related sourcing events and activities. Version 1.0.
  name: Projects API
  slug: projects-api
- description: Access procurement analytics and reporting data from the Workday Strategic Sourcing platform. Version 1.0.
  name: Reports API
  slug: reports-api
- description: Manage users in the Workday Strategic Sourcing platform using the SCIM 2.0 standard, enabling integration with identity providers for automated user provisioning and deprovisioning.
  name: SCIM Users API
  slug: scim-api
- description: Manage spend category taxonomies used to classify procurement spending within the Workday Strategic Sourcing platform. Version 1.0.
  name: Spend Categories API
  slug: spend-categories-api
- description: The Bids API from Scout RFP — 5 operation(s) for bids.
  name: Scout RFP Bids API
  slug: scout-rfp-bids-api
- description: The Event Suppliers API from Scout RFP — 2 operation(s) for event suppliers.
  name: Scout RFP Event Suppliers API
  slug: scout-rfp-event-suppliers-api
- description: The Event Templates API from Scout RFP — 2 operation(s) for event templates.
  name: Scout RFP Event Templates API
  slug: scout-rfp-event-templates-api
- description: The Events API from Scout RFP — 3 operation(s) for events.
  name: Scout RFP Events API
  slug: scout-rfp-events-api
- description: The Line Items API from Scout RFP — 3 operation(s) for line items.
  name: Scout RFP Line Items API
  slug: scout-rfp-line-items-api
- description: The Worksheets API from Scout RFP — 2 operation(s) for worksheets.
  name: Scout RFP Worksheets API
  slug: scout-rfp-worksheets-api
artifact_total: 110
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Workday Strategic Sourcing attachments API
  slug: open-scoutrfp-attachments-api
- collection_type: open
  name: Workday Strategic Sourcing attachments award_line_items API
  slug: open-scoutrfp-award-line-items-api
- collection_type: open
  name: Workday Strategic Sourcing attachments awards API
  slug: open-scoutrfp-awards-api
- collection_type: open
  name: Workday Strategic Sourcing attachments bid_line_items API
  slug: open-scoutrfp-bid-line-items-api
- collection_type: open
  name: Workday Strategic Sourcing attachments bids API
  slug: open-scoutrfp-bids-api
- collection_type: open
  name: Workday Strategic Sourcing attachments contact_types API
  slug: open-scoutrfp-contact-types-api
- collection_type: open
  name: Workday Strategic Sourcing attachments contract_milestone_reports API
  slug: open-scoutrfp-contract-milestone-reports-api
- collection_type: open
  name: Workday Strategic Sourcing attachments contract_reports API
  slug: open-scoutrfp-contract-reports-api
- collection_type: open
  name: Workday Strategic Sourcing attachments contract_types API
  slug: open-scoutrfp-contract-types-api
- collection_type: open
  name: Workday Strategic Sourcing attachments contracts API
  slug: open-scoutrfp-contracts-api
- collection_type: open
  name: Workday Strategic Sourcing attachments discovery API
  slug: open-scoutrfp-discovery-api
- collection_type: open
  name: Workday Strategic Sourcing attachments event_reports API
  slug: open-scoutrfp-event-reports-api
- collection_type: open
  name: Workday Strategic Sourcing attachments event_supplier_companies API
  slug: open-scoutrfp-event-supplier-companies-api
- collection_type: open
  name: Workday Strategic Sourcing attachments event_supplier_contacts API
  slug: open-scoutrfp-event-supplier-contacts-api
- collection_type: open
  name: Workday Strategic Sourcing attachments event_templates API
  slug: open-scoutrfp-event-templates-api
- collection_type: open
  name: Workday Strategic Sourcing attachments events API
  slug: open-scoutrfp-events-api
- collection_type: open
  name: Workday Strategic Sourcing attachments field_groups API
  slug: open-scoutrfp-field-groups-api
- collection_type: open
  name: Workday Strategic Sourcing attachments field_options API
  slug: open-scoutrfp-field-options-api
- collection_type: open
  name: Workday Strategic Sourcing attachments fields API
  slug: open-scoutrfp-fields-api
- collection_type: open
  name: Workday Strategic Sourcing attachments line_items API
  slug: open-scoutrfp-line-items-api
- collection_type: open
  name: Workday Strategic Sourcing attachments payment_currencies API
  slug: open-scoutrfp-payment-currencies-api
- collection_type: open
  name: Workday Strategic Sourcing attachments payment_terms API
  slug: open-scoutrfp-payment-terms-api
- collection_type: open
  name: Workday Strategic Sourcing attachments payment_types API
  slug: open-scoutrfp-payment-types-api
- collection_type: open
  name: Workday Strategic Sourcing attachments project_milestone_reports API
  slug: open-scoutrfp-project-milestone-reports-api
- collection_type: open
  name: Workday Strategic Sourcing attachments project_reports API
  slug: open-scoutrfp-project-reports-api
- collection_type: open
  name: Workday Strategic Sourcing attachments project_supplier_companies API
  slug: open-scoutrfp-project-supplier-companies-api
- collection_type: open
  name: Workday Strategic Sourcing attachments project_supplier_contacts API
  slug: open-scoutrfp-project-supplier-contacts-api
- collection_type: open
  name: Workday Strategic Sourcing attachments project_types API
  slug: open-scoutrfp-project-types-api
- collection_type: open
  name: Workday Strategic Sourcing attachments projects API
  slug: open-scoutrfp-projects-api
- collection_type: open
  name: Workday Strategic Sourcing attachments savings_reports API
  slug: open-scoutrfp-savings-reports-api
- collection_type: open
  name: Workday Strategic Sourcing attachments spend_categories API
  slug: open-scoutrfp-spend-categories-api
- collection_type: open
  name: Workday Strategic Sourcing attachments supplier_categories API
  slug: open-scoutrfp-supplier-categories-api
- collection_type: open
  name: Workday Strategic Sourcing attachments supplier_classifications API
  slug: open-scoutrfp-supplier-classifications-api
- collection_type: open
  name: Workday Strategic Sourcing attachments supplier_companies API
  slug: open-scoutrfp-supplier-companies-api
- collection_type: open
  name: Workday Strategic Sourcing attachments supplier_company_risks API
  slug: open-scoutrfp-supplier-company-risks-api
- collection_type: open
  name: Workday Strategic Sourcing attachments supplier_company_segmentation_statuses API
  slug: open-scoutrfp-supplier-company-segmentation-statuses-api
- collection_type: open
  name: Workday Strategic Sourcing attachments supplier_company_segmentations API
  slug: open-scoutrfp-supplier-company-segmentations-api
- collection_type: open
  name: Workday Strategic Sourcing attachments supplier_contacts API
  slug: open-scoutrfp-supplier-contacts-api
- collection_type: open
  name: Workday Strategic Sourcing attachments supplier_groups API
  slug: open-scoutrfp-supplier-groups-api
- collection_type: open
  name: Workday Strategic Sourcing attachments supplier_reports API
  slug: open-scoutrfp-supplier-reports-api
- collection_type: open
  name: Workday Strategic Sourcing attachments suppliers API
  slug: open-scoutrfp-suppliers-api
- collection_type: open
  name: Workday Strategic Sourcing attachments user API
  slug: open-scoutrfp-user-api
- collection_type: open
  name: Workday Strategic Sourcing attachments worksheets API
  slug: open-scoutrfp-worksheets-api
common:
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/workday/
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/scoutrfp/refs/heads/main/capabilities/scoutrfp-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/scoutrfp-capability-edges.yml
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
  href: https://raw.githubusercontent.com/api-evangelist/scoutrfp/refs/heads/main/authentication/scoutrfp-authentication.yml
  title: ''
  type: Authentication
  url: authentication/scoutrfp-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/scoutrfp/refs/heads/main/conventions/scoutrfp-conventions.yml
  title: ''
  type: Conventions
  url: conventions/scoutrfp-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/scoutrfp/refs/heads/main/errors/scoutrfp-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/scoutrfp-problem-types.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/scoutrfp/refs/heads/main/rate-limits/scoutrfp-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/scoutrfp-rate-limits.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/scoutrfp/refs/heads/main/lifecycle/scoutrfp-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/scoutrfp-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/scoutrfp/refs/heads/main/lifecycle/scoutrfp-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/scoutrfp-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/scoutrfp/refs/heads/main/conformance/scoutrfp-conformance.yml
  title: ''
  type: Conformance
  url: conformance/scoutrfp-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://security.workday.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/scoutrfp/refs/heads/main/security/scoutrfp-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/scoutrfp-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/scoutrfp/refs/heads/main/security/scoutrfp-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/scoutrfp-domain-security.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/scoutrfp/refs/heads/main/data-model/scoutrfp-data-model.yml
  title: ''
  type: DataModel
  url: data-model/scoutrfp-data-model.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/scoutrfp/refs/heads/main/agentic-access/scoutrfp-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/scoutrfp-agentic-access.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/scoutrfp/refs/heads/main/mcp/scoutrfp-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/scoutrfp-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/scoutrfp/refs/heads/main/llms/scoutrfp-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/scoutrfp-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/scoutrfp/refs/heads/main/skills/scoutrfp-run-sourcing-event.md
  title: ''
  type: AgentSkill
  url: skills/scoutrfp-run-sourcing-event.md
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/scoutrfp/refs/heads/main/skills/scoutrfp-onboard-supplier.md
  title: ''
  type: AgentSkill
  url: skills/scoutrfp-onboard-supplier.md
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/scoutrfp/refs/heads/main/skills/scoutrfp-provision-users-scim.md
  title: ''
  type: AgentSkill
  url: skills/scoutrfp-provision-users-scim.md
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/scoutrfp/refs/heads/main/skills/scoutrfp-manage-contract.md
  title: ''
  type: AgentSkill
  url: skills/scoutrfp-manage-contract.md
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/scoutrfp/refs/heads/main/overlays/scoutrfp-suppliers-v1-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/scoutrfp-suppliers-v1-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/scoutrfp/refs/heads/main/overlays/scoutrfp-events-v1-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/scoutrfp-events-v1-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/scoutrfp/refs/heads/main/overlays/scoutrfp-contracts-v1-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/scoutrfp-contracts-v1-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/scoutrfp/refs/heads/main/overlays/scoutrfp-projects-v1-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/scoutrfp-projects-v1-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/scoutrfp/refs/heads/main/overlays/scoutrfp-payments-v1-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/scoutrfp-payments-v1-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/scoutrfp/refs/heads/main/overlays/scoutrfp-scim-v2-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/scoutrfp-scim-v2-overlay.yaml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ScoutRFP
created: '2026-07-17'
description: Scout RFP is a strategic sourcing and supplier engagement platform founded in 2014 and acquired by Workday in 2019, where it now ships as Workday Strategic Sourcing. The product covers sourcing events (RFPs/RFIs/RFQs and auctions), supplier management, contracts, projects, spend categories, awards, and supplier payments. Its public developer platform exposes a JSON:API-conformant REST API across eleven versioned services — Suppliers, Events, Reports, Contracts, Projects, Payments, Fields, Awards, Attachments, and Spend Categories — plus a SCIM 2.0 user-provisioning API. Authentication is by company API key plus a per-user personal token, all calls are HTTPS/JSON:API, cursor paginated, and rate limited to five requests per second. The legacy v3 API on api.scoutrfp.com was sunset April 18, 2025 in favor of the versioned services on api.us.workdayspend.com (with EU and CA regional hosts).
image: https://www.workday.com/content/dam/web/en-us/images/social/workday-og-image.png
layout: provider
modified: '2026-07-21'
name: Scout RFP (Workday Strategic Sourcing)
nav: Providers
network: true
overview: 'Scout RFP (Workday Strategic Sourcing) publishes 52 APIs on the [APIs.io](https://apis.io/) network, including attachments API, award_line_items API, awards API, and 49 more. Tagged areas include Company, Enterprise, Procurement, Strategic Sourcing, and Supplier Management.


  Scout RFP (Workday Strategic Sourcing)''s developer surface includes documentation, API reference, getting-started guide, changelog, authentication, and 28 more developer resources.'
random_paper: 6
rate_limits:
- limit_count: 1
  name: Scoutrfp Rate Limits
  slug: scoutrfp-rate-limits
score:
  band: developing
  composite: 43.7
  coverage:
    artifact_dirs: 17
    catalog_earned: 38.0
    catalog_earned_first_party: 8.0
    catalog_gap: 77.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.1
  facets:
    access_clarity: 7.9
    contract_governance: 4.5
    contract_quality: 66.6
    developer_ergonomics: 51.8
    discoverability: 63.0
    operational_transparency: 47.4
  previous_composite: 45.8
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
  schema_version: 0.22.0
  scored_at: '2026-09-19'
  trend: flat
  upsert:
    applies: true
    score: 27.8
screenshot: https://raw.githubusercontent.com/api-evangelist/scoutrfp/refs/heads/main/screenshots/scoutrfp-2026-09-02T154558.png
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
