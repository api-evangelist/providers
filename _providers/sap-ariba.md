---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    rate_limit_signal: verified
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 42.4
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Sap Ariba Agentic Access
  operation_count: 19
  slug: sap-ariba-agentic-access
  summary_line: 19 operations · 8 acting
api_count: 78
apis:
- description: Allows buyers to create, manage, and track purchase orders across the SAP Ariba Network.
  name: Ariba Network Purchase Orders Buyer API
  slug: ariba-network-purchase-orders-buyer-api
- description: Enables suppliers to retrieve purchase order and line item information from buyers on the SAP Business Network.
  name: Ariba Network Purchase Orders Supplier API
  slug: ariba-network-purchase-orders-supplier-api
- description: Provides access to supplier profile details on the SAP Ariba Network.
  name: Ariba Network Supplier Profile API
  slug: ariba-network-supplier-profile-api
- description: Extracts invoice header information from the SAP Ariba Network for data analysis and integration.
  name: Ariba Network Invoice Header Data Extraction API
  slug: ariba-network-invoice-header-data-extraction-api
- description: Ensures contract compliance by validating procurement activities against contract terms and conditions.
  name: SAP Ariba Contract Compliance API
  slug: sap-ariba-contract-compliance-api
- description: Provides access to general supplier data including company information and classification details.
  name: SAP Ariba Supplier Data API
  slug: sap-ariba-supplier-data-api
- description: Retrieves supplier data with pagination support for handling large datasets.
  name: SAP Ariba Supplier Data API with Pagination
  slug: sap-ariba-supplier-data-api-with-pagination
- description: Extracts detailed supplier information for integration with external systems and analytics.
  name: SAP Ariba Supplier Data Extraction API
  slug: sap-ariba-supplier-data-extraction-api
- description: Provides supplier profile and related detail information for supplier lifecycle management.
  name: SAP Ariba Supplier Information API
  slug: sap-ariba-supplier-information-api
- description: Invites suppliers to participate in procurement transactions and network activities.
  name: SAP Ariba Supplier Invite API
  slug: sap-ariba-supplier-invite-api
- description: Analyzes and reports on supplier risk exposure across the supply chain.
  name: SAP Ariba Risk Exposure API
  slug: sap-ariba-risk-exposure-api
- description: Manages supplier risk engagement activities and assessment workflows.
  name: SAP Ariba Supplier Risk Engagements API
  slug: sap-ariba-supplier-risk-engagements-api
- description: Provides risk classification and category details for supplier risk exposure analysis.
  name: SAP Ariba Risk Category Information API
  slug: sap-ariba-risk-category-information-api
- description: Handles approval workflows for procurement documents including requisitions and purchase orders.
  name: SAP Ariba Document Approval API
  slug: sap-ariba-document-approval-api
- description: Enables external approval routing for sourcing events and supplier management processes.
  name: SAP Ariba External Approval API for Sourcing and Supplier Management
  slug: sap-ariba-external-approval-api-for-sourcing-and-supplier-management
- description: Enables applications to manage catalog content and get faceted catalog data based on specific attributes.
  name: SAP Ariba Catalog Content API
  slug: sap-ariba-catalog-content-api
- description: Controls catalog operations across the SAP Ariba Network including subscriptions and publishing.
  name: SAP Ariba Network Catalog Management API
  slug: sap-ariba-network-catalog-management-api
- description: Manages internal catalog shopping experiences for procurement users.
  name: SAP Ariba Internal Catalogs Shop API
  slug: sap-ariba-internal-catalogs-shop-api
- description: Manages public marketplace catalog experiences for procurement users.
  name: SAP Ariba Public Catalogs Shop API
  slug: sap-ariba-public-catalogs-shop-api
- description: Retrieves contract workspace information for contract lifecycle management.
  name: SAP Ariba Contract Workspace Retrieval API
  slug: sap-ariba-contract-workspace-retrieval-api
- description: Administers contract collaboration spaces including creation, updates, and lifecycle management.
  name: SAP Ariba Contract Workspace Management API
  slug: sap-ariba-contract-workspace-management-api
- description: Administers contract term definitions and clause libraries.
  name: SAP Ariba Contract Terms Management API
  slug: sap-ariba-contract-terms-management-api
- description: Delivers operational metrics and reporting data for procurement activities.
  name: SAP Ariba Operational Reporting API for Procurement
  slug: sap-ariba-operational-reporting-api-for-procurement
- description: Delivers operational metrics and reporting data for strategic sourcing activities.
  name: SAP Ariba Operational Reporting API for Strategic Sourcing
  slug: sap-ariba-operational-reporting-api-for-strategic-sourcing
- description: Delivers analytics across strategic and operational procurement domains including contracts, sourcing, spend analysis, and buying.
  name: SAP Ariba Analytical Reporting API for Strategic and Operational Procurement
  slug: sap-ariba-analytical-reporting-api-for-strategic-and-operational-procurement
- description: Obtains master data for sourcing operations including commodity codes and regions.
  name: SAP Ariba Master Data Retrieval API for Sourcing
  slug: sap-ariba-master-data-retrieval-api-for-sourcing
- description: Retrieves procurement master data including cost centers, accounts, and units of measure.
  name: SAP Ariba Master Data Retrieval API for Procurement
  slug: sap-ariba-master-data-retrieval-api-for-procurement
- description: Oversees sourcing project workflows including event creation and management.
  name: SAP Ariba Sourcing Project Management API
  slug: sap-ariba-sourcing-project-management-api
- description: Manages sourcing events and their lifecycle including RFx and auction events.
  name: SAP Ariba Event Management API
  slug: sap-ariba-event-management-api
- description: Enables proxy bidding mechanisms for sourcing events on behalf of suppliers.
  name: SAP Ariba Surrogate Bid API
  slug: sap-ariba-surrogate-bid-api
- description: Manages order modification requests from the buyer perspective.
  name: SAP Ariba Order Change Requests API for Buyers
  slug: sap-ariba-order-change-requests-api-for-buyers
- description: Handles order change request processing from the supplier perspective.
  name: SAP Ariba Order Change Requests API for Suppliers
  slug: sap-ariba-order-change-requests-api-for-suppliers
- description: Receives and processes shipment notifications for buyers on the Ariba Network.
  name: SAP Ariba Ship Notice API for Buyers
  slug: sap-ariba-ship-notice-api-for-buyers
- description: Sends shipment notifications from suppliers to buyers on the Ariba Network.
  name: SAP Ariba Ship Notice API for Suppliers
  slug: sap-ariba-ship-notice-api-for-suppliers
- description: Validates service fulfillment and delivery for buyers in service procurement.
  name: SAP Ariba Proof of Service API for Buyers
  slug: sap-ariba-proof-of-service-api-for-buyers
- description: Validates service fulfillment and delivery for suppliers in service procurement.
  name: SAP Ariba Proof of Service API for Suppliers
  slug: sap-ariba-proof-of-service-api-for-suppliers
- description: Enables buyer-side planning and forecast collaboration with suppliers.
  name: SAP Ariba Planning Collaboration Buyer API
  slug: sap-ariba-planning-collaboration-buyer-api
- description: Enables supplier-side planning and forecast collaboration with buyers.
  name: SAP Ariba Planning Collaboration Supplier API
  slug: sap-ariba-planning-collaboration-supplier-api
- description: Imports item volume data for procurement planning and sourcing optimization.
  name: SAP Ariba Item Volume Import API
  slug: sap-ariba-item-volume-import-api
- description: Imports bill of materials structures for sourcing and procurement processes.
  name: SAP Ariba Bill of Materials Import API
  slug: sap-ariba-bill-of-materials-import-api
- description: Organizes product classification and category hierarchy structures.
  name: SAP Ariba Product Hierarchy Management API
  slug: sap-ariba-product-hierarchy-management-api
- description: Extracts and manages pricing data for product sourcing price information.
  name: SAP Ariba Pricing API for Product Sourcing
  slug: sap-ariba-pricing-api-for-product-sourcing
- description: Extracts cost component and cost breakdown information for analysis.
  name: SAP Ariba Cost Breakdown Data Extraction API
  slug: sap-ariba-cost-breakdown-data-extraction-api
- description: Searches and retrieves content across the SAP Ariba platform.
  name: SAP Ariba Content Lookup API
  slug: sap-ariba-content-lookup-api
- description: Provides audit trail search capabilities across procurement and sourcing activities.
  name: SAP Ariba Audit Search API
  slug: sap-ariba-audit-search-api
- description: Initiates and creates procurement workspace environments for project collaboration.
  name: SAP Ariba Create Procurement Workspace API
  slug: sap-ariba-create-procurement-workspace-api
- description: Extends workflow processing capabilities for custom procurement and sourcing processes.
  name: SAP Ariba Flow Extension API
  slug: sap-ariba-flow-extension-api
- description: Manages long-running asynchronous operations and their status tracking.
  name: SAP Ariba Asynchronous Requests Management API
  slug: sap-ariba-asynchronous-requests-management-api
- description: Monitors and queries integration events for procurement process tracking.
  name: SAP Ariba Integration Event Monitoring Query API for Procurement
  slug: sap-ariba-integration-event-monitoring-query-api-for-procurement
- description: Tracks integration health and performance for procurement system integrations.
  name: SAP Ariba Integration Monitoring API for Procurement
  slug: sap-ariba-integration-monitoring-api-for-procurement
- description: Tracks integration health and performance for strategic sourcing system integrations.
  name: SAP Ariba Integration Monitoring API for Strategic Sourcing
  slug: sap-ariba-integration-monitoring-api-for-strategic-sourcing
- description: Observes and reports on transaction activities and processing status.
  name: SAP Ariba Transaction Monitoring API
  slug: sap-ariba-transaction-monitoring-api
- description: Exports non-disclosure agreement data for compliance and record keeping.
  name: SAP Ariba NDA Data Export API
  slug: sap-ariba-nda-data-export-api
- description: Connects to external catalog systems for punchout and roundtrip catalog integration.
  name: SAP Ariba Catalog Connectivity Service API
  slug: sap-ariba-catalog-connectivity-service-api
- description: Manages trading partner certifications and compliance documentation.
  name: SAP Ariba Trading Partner Profile Certification API
  slug: sap-ariba-trading-partner-profile-certification-api
- description: Validates user eligibility and qualifications for procurement processes.
  name: SAP Ariba User Qualification API
  slug: sap-ariba-user-qualification-api
- description: Implements System for Cross-domain Identity Management for user provisioning and management.
  name: SAP Ariba SCIM API
  slug: sap-ariba-scim-api
- description: Creates and manages custom form definitions for procurement and sourcing workflows.
  name: SAP Ariba Custom Forms API
  slug: sap-ariba-custom-forms-api
- description: Manages dynamic reference and lookup tables for configurable procurement data.
  name: SAP Ariba Dynamic Lookup Table API
  slug: sap-ariba-dynamic-lookup-table-api
- description: Manages guided buying documentation and functional purchase request workflows.
  name: SAP Ariba Guided Buying Functional Documents API
  slug: sap-ariba-guided-buying-functional-documents-api
- description: Manages asset lifecycle and inventory tracking for procurement-related assets.
  name: SAP Ariba Asset Management API
  slug: sap-ariba-asset-management-api
- description: Reviews and manages system configuration parameters for Ariba solutions.
  name: SAP Ariba Configuration Parameter Review API
  slug: sap-ariba-configuration-parameter-review-api
- description: Organizes and manages project-related documents within sourcing and procurement projects.
  name: SAP Ariba Project Document Management API
  slug: sap-ariba-project-document-management-api
- description: Exports public procurement announcements and tender notices.
  name: SAP Ariba Public Procurement Notices Export API
  slug: sap-ariba-public-procurement-notices-export-api
- description: Manages electronic tendering announcements and notice lifecycle.
  name: SAP Ariba ETendering Notice Management API
  slug: sap-ariba-etendering-notice-management-api
- description: Publishes RFx opportunities to external marketplaces for broader supplier discovery.
  name: SAP Ariba Discovery RFx Publication TO External Marketplace API
  slug: sap-ariba-discovery-rfx-publication-to-external-marketplace-api
- description: Imports RFx opportunities from external marketplaces into SAP Ariba.
  name: SAP Ariba Discovery RFx Publication FROM External Marketplace API
  slug: sap-ariba-discovery-rfx-publication-from-external-marketplace-api
- description: Manages tagging and classification for materials and bill of materials entries.
  name: SAP Ariba Materials and BOM Tag Management API
  slug: sap-ariba-materials-and-bom-tag-management-api
- description: Monitors data replication status across multi-ERP configurations.
  name: SAP Ariba Data Replication Status API
  slug: sap-ariba-data-replication-status-api
- description: Tracks master data synchronization job status for operational procurement.
  name: SAP Ariba Master Data Integration Job Status API
  slug: sap-ariba-master-data-integration-job-status-api
- description: Imports external risk assessment responses for supplier engagement risk evaluation.
  name: SAP Ariba Engagement Risk Assessment External Response Import API
  slug: sap-ariba-engagement-risk-assessment-external-response-import-api
- description: Integrates risk findings and event collaboration for supplier risk management.
  name: SAP Ariba Finding and Event Collaboration Integration API for Supplier Risk
  slug: sap-ariba-finding-and-event-collaboration-integration-api-for-supplier-risk
- description: Process and manage invoices including creation, approval workflows, status tracking, and payment reconciliation.
  name: SAP Ariba Invoices API
  slug: sap-ariba-invoices-api
- description: Manage individual line items within purchase orders including quantities, pricing, delivery schedules, and accounting assignments.
  name: SAP Ariba Purchase Order Line Items API
  slug: sap-ariba-purchase-order-line-items-api
- description: Create, retrieve, update, and manage purchase orders across the SAP Ariba Network. Supports standard and service purchase orders including new, change, cancel, and close operations.
  name: SAP Ariba Purchase Orders API
  slug: sap-ariba-purchase-orders-api
- description: Record goods receipts and service confirmations against purchase orders to support three-way matching.
  name: SAP Ariba Receipts API
  slug: sap-ariba-receipts-api
- description: Create and manage purchase requisitions that initiate the procurement process and flow into purchase orders upon approval.
  name: SAP Ariba Requisitions API
  slug: sap-ariba-requisitions-api
- description: Access and manage supplier profiles, onboarding, qualifications, performance, and risk assessments on the SAP Ariba Network.
  name: SAP Ariba Suppliers API
  slug: sap-ariba-suppliers-api
artifact_total: 250
collections:
- collection_type: postman
  name: SAP Ariba Procurement Invoices API
  slug: postman-sap-ariba-invoices-api
- collection_type: postman
  name: SAP Ariba Procurement Invoices Purchase Order Line Items API
  slug: postman-sap-ariba-purchase-order-line-items-api
- collection_type: postman
  name: SAP Ariba Procurement Invoices Purchase Orders API
  slug: postman-sap-ariba-purchase-orders-api
- collection_type: postman
  name: SAP Ariba Procurement Invoices Receipts API
  slug: postman-sap-ariba-receipts-api
- collection_type: postman
  name: SAP Ariba Procurement Invoices Requisitions API
  slug: postman-sap-ariba-requisitions-api
- collection_type: postman
  name: SAP Ariba Procurement Invoices Suppliers API
  slug: postman-sap-ariba-suppliers-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: SAP Ariba Procurement Invoices API
  slug: open-sap-ariba-invoices-api
- collection_type: open
  name: SAP Ariba Procurement API
  slug: open-sap-ariba-procurement-api
- collection_type: open
  name: SAP Ariba Procurement Invoices Purchase Order Line Items API
  slug: open-sap-ariba-purchase-order-line-items-api
- collection_type: open
  name: SAP Ariba Procurement Invoices Purchase Orders API
  slug: open-sap-ariba-purchase-orders-api
- collection_type: open
  name: SAP Ariba Procurement Invoices Receipts API
  slug: open-sap-ariba-receipts-api
- collection_type: open
  name: SAP Ariba Procurement Invoices Requisitions API
  slug: open-sap-ariba-requisitions-api
- collection_type: open
  name: SAP Ariba Procurement Invoices Suppliers API
  slug: open-sap-ariba-suppliers-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/sap-ariba/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/sap-ariba-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/sap-ariba-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sap-ariba-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/sap-ariba-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/sap-ariba-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ariba
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.ariba.com
- group: auth
  title: ''
  type: Authentication
  url: https://developer.ariba.com/api/authentication
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.ariba.com/api/getting-started
- group: operate
  title: ''
  type: StatusPage
  url: https://status.ariba.com
- group: operate
  title: ''
  type: Support
  url: https://help.sap.com/ariba
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ariba.com/legal/terms-of-use
- group: operate
  title: ''
  type: RateLimits
  url: https://developer.ariba.com/api/rate-limits
- group: build
  title: ''
  type: SDKs
  url: https://developer.ariba.com/tools/sdks
- group: operate
  title: ''
  type: Community
  url: https://community.ariba.com
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://developer.ariba.com/api/release-notes
- group: other
  title: ''
  type: Hub
  url: https://api.sap.com/package/SAPAribaOpenAPIs/overview
- group: other
  title: REST APIs
  type: Hub
  url: https://api.sap.com/package/SAPAribaOpenAPIs/rest
- group: other
  title: Documents
  type: Hub
  url: https://api.sap.com/package/SAPAribaOpenAPIs/documents
- group: start
  title: ''
  type: Portal
  url: https://api.sap.com/products/SAPAriba/apis/packages
- group: docs
  title: ''
  type: Documentation
  url: https://help.sap.com/docs/ariba-apis
- group: start
  title: ''
  type: GettingStarted
  url: https://help.sap.com/docs/ariba-apis/help-for-sap-ariba-developer-portal/sap-ariba-developer-portal-quick-start-guide-for-developers
- group: start
  title: Steps to Start Using APIs
  type: GettingStarted
  url: https://help.sap.com/docs/ariba-apis/help-for-sap-ariba-developer-portal/steps-to-start-using-sap-ariba-apis
- group: auth
  title: ''
  type: Authentication
  url: https://help.sap.com/docs/ariba-apis/help-for-sap-ariba-developer-portal/sap-ariba-developer-portal-authentication
- group: other
  title: SAP Community
  type: Resources
  url: https://community.sap.com
- group: other
  title: ''
  type: Marketplace
  url: https://www.sap.com/products/spend-management/ariba-network.html
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/SAP-samples/ariba-extensibility-samples
- group: company
  title: ''
  type: Blog
  url: https://community.sap.com/t5/spend-management-blog-posts-by-sap/sap-ariba-api-faq-and-best-practice-on-developer-portal-and-gateway/ba-p/13512565
created: '2024'
description: SAP Ariba is a cloud-based procurement and supply chain collaboration platform that connects buyers and suppliers. It offers APIs for procurement, sourcing, contract management, supplier management, and spend analysis.
examples:
- key_count: 8
  name: Sap Ariba Procurement Accounting Info Example
  slug: sap-ariba-procurement-accounting-info-example
- key_count: 8
  name: Sap Ariba Procurement Address Example
  slug: sap-ariba-procurement-address-example
- key_count: 3
  name: Sap Ariba Procurement Buyer Reference Example
  slug: sap-ariba-procurement-buyer-reference-example
- key_count: 3
  name: Sap Ariba Procurement Commodity Code Example
  slug: sap-ariba-procurement-commodity-code-example
- key_count: 5
  name: Sap Ariba Procurement Contact Info Example
  slug: sap-ariba-procurement-contact-info-example
- key_count: 1
  name: Sap Ariba Procurement Error Response Example
  slug: sap-ariba-procurement-error-response-example
- key_count: 7
  name: Sap Ariba Procurement Invoice Create Example
  slug: sap-ariba-procurement-invoice-create-example
- key_count: 15
  name: Sap Ariba Procurement Invoice Example
  slug: sap-ariba-procurement-invoice-example
- key_count: 9
  name: Sap Ariba Procurement Invoice Line Item Example
  slug: sap-ariba-procurement-invoice-line-item-example
- key_count: 4
  name: Sap Ariba Procurement Invoice List Response Example
  slug: sap-ariba-procurement-invoice-list-response-example
- key_count: 0
  name: Sap Ariba Procurement Invoice Status Example
  slug: sap-ariba-procurement-invoice-status-example
- key_count: 4
  name: Sap Ariba Procurement Line Item List Response Example
  slug: sap-ariba-procurement-line-item-list-response-example
- key_count: 2
  name: Sap Ariba Procurement Money Example
  slug: sap-ariba-procurement-money-example
- key_count: 5
  name: Sap Ariba Procurement Payment Terms Example
  slug: sap-ariba-procurement-payment-terms-example
- key_count: 9
  name: Sap Ariba Procurement Purchase Order Create Example
  slug: sap-ariba-procurement-purchase-order-create-example
- key_count: 16
  name: Sap Ariba Procurement Purchase Order Example
  slug: sap-ariba-procurement-purchase-order-example
- key_count: 17
  name: Sap Ariba Procurement Purchase Order Line Item Example
  slug: sap-ariba-procurement-purchase-order-line-item-example
- key_count: 4
  name: Sap Ariba Procurement Purchase Order List Response Example
  slug: sap-ariba-procurement-purchase-order-list-response-example
- key_count: 0
  name: Sap Ariba Procurement Purchase Order Status Example
  slug: sap-ariba-procurement-purchase-order-status-example
- key_count: 2
  name: Sap Ariba Procurement Purchase Order Update Example
  slug: sap-ariba-procurement-purchase-order-update-example
- key_count: 3
  name: Sap Ariba Procurement Receipt Create Example
  slug: sap-ariba-procurement-receipt-create-example
- key_count: 8
  name: Sap Ariba Procurement Receipt Example
  slug: sap-ariba-procurement-receipt-example
- key_count: 4
  name: Sap Ariba Procurement Receipt List Response Example
  slug: sap-ariba-procurement-receipt-list-response-example
- key_count: 5
  name: Sap Ariba Procurement Requisition Create Example
  slug: sap-ariba-procurement-requisition-create-example
- key_count: 13
  name: Sap Ariba Procurement Requisition Example
  slug: sap-ariba-procurement-requisition-example
- key_count: 4
  name: Sap Ariba Procurement Requisition List Response Example
  slug: sap-ariba-procurement-requisition-list-response-example
- key_count: 0
  name: Sap Ariba Procurement Requisition Status Example
  slug: sap-ariba-procurement-requisition-status-example
- key_count: 15
  name: Sap Ariba Procurement Supplier Example
  slug: sap-ariba-procurement-supplier-example
- key_count: 4
  name: Sap Ariba Procurement Supplier List Response Example
  slug: sap-ariba-procurement-supplier-list-response-example
- key_count: 0
  name: Sap Ariba Procurement Supplier Qualification Status Example
  slug: sap-ariba-procurement-supplier-qualification-status-example
- key_count: 3
  name: Sap Ariba Procurement Supplier Reference Example
  slug: sap-ariba-procurement-supplier-reference-example
- key_count: 4
  name: Sap Ariba Procurement Tax Detail Example
  slug: sap-ariba-procurement-tax-detail-example
- key_count: 2
  name: Sap Ariba Procurement Unit Of Measure Example
  slug: sap-ariba-procurement-unit-of-measure-example
features:
- description: End-to-end automation from requisition through purchase order, receipt, and invoice processing.
  name: Procure-to-Pay Automation
- description: Access to millions of suppliers on the SAP Business Network for discovery and collaboration.
  name: Supplier Network
- description: Automated matching of purchase orders, receipts, and invoices for payment approval.
  name: Three-Way Matching
- description: Full contract creation, compliance tracking, and renewal workflow management.
  name: Contract Lifecycle Management
- description: Comprehensive reporting and analytics across procurement, sourcing, and supplier management.
  name: Spend Analytics
finops:
- name: Sap Ariba Finops
  service_category: Procurement / B2B Network
  slug: sap-ariba-finops
image: https://www.ariba.com/ariba-logo.png
integrations:
- description: Native integration with SAP ERP for purchase order, invoice, and master data synchronization.
  name: SAP S/4HANA
- description: Connect buyers and suppliers for electronic document exchange across the network.
  name: SAP Business Network
- description: Integration with non-SAP ERP systems through standardized APIs and data replication.
  name: External ERP Systems
json_schemas:
- name: AccountingInfo
  property_count: 9
  slug: sap-ariba-accountinginfo
- name: Address
  property_count: 8
  slug: sap-ariba-address
- name: BuyerReference
  property_count: 3
  slug: sap-ariba-buyerreference
- name: CommodityCode
  property_count: 3
  slug: sap-ariba-commoditycode
- name: ContactInfo
  property_count: 5
  slug: sap-ariba-contactinfo
- name: ErrorResponse
  property_count: 1
  slug: sap-ariba-errorresponse
- name: Invoice
  property_count: 24
  slug: sap-ariba-invoice
- name: InvoiceCreate
  property_count: 14
  slug: sap-ariba-invoicecreate
- name: InvoiceLineItem
  property_count: 14
  slug: sap-ariba-invoicelineitem
- name: InvoiceListResponse
  property_count: 4
  slug: sap-ariba-invoicelistresponse
- name: InvoiceStatus
  property_count: 0
  slug: sap-ariba-invoicestatus
- name: LineItemListResponse
  property_count: 4
  slug: sap-ariba-lineitemlistresponse
- name: Money
  property_count: 2
  slug: sap-ariba-money
- name: PaymentTerms
  property_count: 5
  slug: sap-ariba-paymentterms
- name: AccountingInfo
  property_count: 8
  slug: sap-ariba-procurement-accounting-info
- name: Address
  property_count: 8
  slug: sap-ariba-procurement-address
- name: BuyerReference
  property_count: 3
  slug: sap-ariba-procurement-buyer-reference
- name: CommodityCode
  property_count: 3
  slug: sap-ariba-procurement-commodity-code
- name: ContactInfo
  property_count: 5
  slug: sap-ariba-procurement-contact-info
- name: ErrorResponse
  property_count: 1
  slug: sap-ariba-procurement-error-response
- name: InvoiceCreate
  property_count: 7
  slug: sap-ariba-procurement-invoice-create
- name: InvoiceLineItem
  property_count: 9
  slug: sap-ariba-procurement-invoice-line-item
- name: InvoiceListResponse
  property_count: 4
  slug: sap-ariba-procurement-invoice-list-response
- name: Invoice
  property_count: 15
  slug: sap-ariba-procurement-invoice
- name: InvoiceStatus
  property_count: 0
  slug: sap-ariba-procurement-invoice-status
- name: LineItemListResponse
  property_count: 4
  slug: sap-ariba-procurement-line-item-list-response
- name: Money
  property_count: 2
  slug: sap-ariba-procurement-money
- name: PaymentTerms
  property_count: 5
  slug: sap-ariba-procurement-payment-terms
- name: PurchaseOrderCreate
  property_count: 9
  slug: sap-ariba-procurement-purchase-order-create
- name: PurchaseOrderLineItem
  property_count: 17
  slug: sap-ariba-procurement-purchase-order-line-item
- name: PurchaseOrderListResponse
  property_count: 4
  slug: sap-ariba-procurement-purchase-order-list-response
- name: PurchaseOrder
  property_count: 16
  slug: sap-ariba-procurement-purchase-order
- name: PurchaseOrderStatus
  property_count: 0
  slug: sap-ariba-procurement-purchase-order-status
- name: PurchaseOrderUpdate
  property_count: 2
  slug: sap-ariba-procurement-purchase-order-update
- name: ReceiptCreate
  property_count: 3
  slug: sap-ariba-procurement-receipt-create
- name: ReceiptListResponse
  property_count: 4
  slug: sap-ariba-procurement-receipt-list-response
- name: Receipt
  property_count: 8
  slug: sap-ariba-procurement-receipt
- name: RequisitionCreate
  property_count: 5
  slug: sap-ariba-procurement-requisition-create
- name: RequisitionListResponse
  property_count: 4
  slug: sap-ariba-procurement-requisition-list-response
- name: Requisition
  property_count: 13
  slug: sap-ariba-procurement-requisition
- name: RequisitionStatus
  property_count: 0
  slug: sap-ariba-procurement-requisition-status
- name: SupplierListResponse
  property_count: 4
  slug: sap-ariba-procurement-supplier-list-response
- name: SupplierQualificationStatus
  property_count: 0
  slug: sap-ariba-procurement-supplier-qualification-status
- name: SupplierReference
  property_count: 3
  slug: sap-ariba-procurement-supplier-reference
- name: Supplier
  property_count: 15
  slug: sap-ariba-procurement-supplier
- name: TaxDetail
  property_count: 4
  slug: sap-ariba-procurement-tax-detail
- name: UnitOfMeasure
  property_count: 2
  slug: sap-ariba-procurement-unit-of-measure
- name: SAP Ariba Purchase Order
  property_count: 28
  slug: sap-ariba-purchase-order
- name: PurchaseOrder
  property_count: 25
  slug: sap-ariba-purchaseorder
- name: PurchaseOrderCreate
  property_count: 13
  slug: sap-ariba-purchaseordercreate
- name: PurchaseOrderLineItem
  property_count: 23
  slug: sap-ariba-purchaseorderlineitem
- name: PurchaseOrderListResponse
  property_count: 4
  slug: sap-ariba-purchaseorderlistresponse
- name: PurchaseOrderStatus
  property_count: 0
  slug: sap-ariba-purchaseorderstatus
- name: PurchaseOrderUpdate
  property_count: 4
  slug: sap-ariba-purchaseorderupdate
- name: Receipt
  property_count: 8
  slug: sap-ariba-receipt
- name: ReceiptCreate
  property_count: 3
  slug: sap-ariba-receiptcreate
- name: ReceiptListResponse
  property_count: 4
  slug: sap-ariba-receiptlistresponse
- name: Requisition
  property_count: 15
  slug: sap-ariba-requisition
- name: RequisitionCreate
  property_count: 5
  slug: sap-ariba-requisitioncreate
- name: RequisitionListResponse
  property_count: 4
  slug: sap-ariba-requisitionlistresponse
- name: RequisitionStatus
  property_count: 0
  slug: sap-ariba-requisitionstatus
- name: Supplier
  property_count: 19
  slug: sap-ariba-supplier
- name: SupplierListResponse
  property_count: 4
  slug: sap-ariba-supplierlistresponse
- name: SupplierQualificationStatus
  property_count: 0
  slug: sap-ariba-supplierqualificationstatus
- name: SupplierReference
  property_count: 3
  slug: sap-ariba-supplierreference
- name: TaxDetail
  property_count: 6
  slug: sap-ariba-taxdetail
- name: UnitOfMeasure
  property_count: 2
  slug: sap-ariba-unitofmeasure
json_structures:
- name: Sap Ariba Procurement Accounting Info Structure
  property_count: 8
  slug: sap-ariba-procurement-accounting-info-structure
- name: Sap Ariba Procurement Address Structure
  property_count: 8
  slug: sap-ariba-procurement-address-structure
- name: Sap Ariba Procurement Buyer Reference Structure
  property_count: 3
  slug: sap-ariba-procurement-buyer-reference-structure
- name: Sap Ariba Procurement Commodity Code Structure
  property_count: 3
  slug: sap-ariba-procurement-commodity-code-structure
- name: Sap Ariba Procurement Contact Info Structure
  property_count: 5
  slug: sap-ariba-procurement-contact-info-structure
- name: Sap Ariba Procurement Error Response Structure
  property_count: 1
  slug: sap-ariba-procurement-error-response-structure
- name: Sap Ariba Procurement Invoice Create Structure
  property_count: 7
  slug: sap-ariba-procurement-invoice-create-structure
- name: Sap Ariba Procurement Invoice Line Item Structure
  property_count: 9
  slug: sap-ariba-procurement-invoice-line-item-structure
- name: Sap Ariba Procurement Invoice List Response Structure
  property_count: 4
  slug: sap-ariba-procurement-invoice-list-response-structure
- name: Sap Ariba Procurement Invoice Status Structure
  property_count: 0
  slug: sap-ariba-procurement-invoice-status-structure
- name: Sap Ariba Procurement Invoice Structure
  property_count: 15
  slug: sap-ariba-procurement-invoice-structure
- name: Sap Ariba Procurement Line Item List Response Structure
  property_count: 4
  slug: sap-ariba-procurement-line-item-list-response-structure
- name: Sap Ariba Procurement Money Structure
  property_count: 2
  slug: sap-ariba-procurement-money-structure
- name: Sap Ariba Procurement Payment Terms Structure
  property_count: 5
  slug: sap-ariba-procurement-payment-terms-structure
- name: Sap Ariba Procurement Purchase Order Create Structure
  property_count: 9
  slug: sap-ariba-procurement-purchase-order-create-structure
- name: Sap Ariba Procurement Purchase Order Line Item Structure
  property_count: 17
  slug: sap-ariba-procurement-purchase-order-line-item-structure
- name: Sap Ariba Procurement Purchase Order List Response Structure
  property_count: 4
  slug: sap-ariba-procurement-purchase-order-list-response-structure
- name: Sap Ariba Procurement Purchase Order Status Structure
  property_count: 0
  slug: sap-ariba-procurement-purchase-order-status-structure
- name: Sap Ariba Procurement Purchase Order Structure
  property_count: 16
  slug: sap-ariba-procurement-purchase-order-structure
- name: Sap Ariba Procurement Purchase Order Update Structure
  property_count: 2
  slug: sap-ariba-procurement-purchase-order-update-structure
- name: Sap Ariba Procurement Receipt Create Structure
  property_count: 3
  slug: sap-ariba-procurement-receipt-create-structure
- name: Sap Ariba Procurement Receipt List Response Structure
  property_count: 4
  slug: sap-ariba-procurement-receipt-list-response-structure
- name: Sap Ariba Procurement Receipt Structure
  property_count: 8
  slug: sap-ariba-procurement-receipt-structure
- name: Sap Ariba Procurement Requisition Create Structure
  property_count: 5
  slug: sap-ariba-procurement-requisition-create-structure
- name: Sap Ariba Procurement Requisition List Response Structure
  property_count: 4
  slug: sap-ariba-procurement-requisition-list-response-structure
- name: Sap Ariba Procurement Requisition Status Structure
  property_count: 0
  slug: sap-ariba-procurement-requisition-status-structure
- name: Sap Ariba Procurement Requisition Structure
  property_count: 13
  slug: sap-ariba-procurement-requisition-structure
- name: Sap Ariba Procurement Supplier List Response Structure
  property_count: 4
  slug: sap-ariba-procurement-supplier-list-response-structure
- name: Sap Ariba Procurement Supplier Qualification Status Structure
  property_count: 0
  slug: sap-ariba-procurement-supplier-qualification-status-structure
- name: Sap Ariba Procurement Supplier Reference Structure
  property_count: 3
  slug: sap-ariba-procurement-supplier-reference-structure
- name: Sap Ariba Procurement Supplier Structure
  property_count: 15
  slug: sap-ariba-procurement-supplier-structure
- name: Sap Ariba Procurement Tax Detail Structure
  property_count: 4
  slug: sap-ariba-procurement-tax-detail-structure
- name: Sap Ariba Procurement Unit Of Measure Structure
  property_count: 2
  slug: sap-ariba-procurement-unit-of-measure-structure
- name: Sap Ariba Structure
  property_count: 0
  slug: sap-ariba-structure
jsonld:
- class_count: 0
  name: Sap Ariba Context
  property_count: 14
  slug: sap-ariba-context
- class_count: 0
  name: Sap Ariba Procurement Context
  property_count: 0
  slug: sap-ariba-procurement-context
layout: provider
modified: '2026-05-19'
name: SAP Ariba
nav: Providers
network: true
overview: 'SAP Ariba publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Invoices API, Purchase Order Line Items API, Purchase Orders API, and 3 more. Tagged areas include B2B, Contract Management, Procurement, Sourcing, and Spend Analysis.


  The SAP Ariba catalog on APIs.io includes 2 JSON-LD contexts and 2 Spectral governance rulesets.


  SAP Ariba''s developer surface includes authentication, getting-started guide, support, release notes, developer portal, documentation, code examples, and 22 more developer resources.'
plans:
- name: Sap Ariba Plans Pricing
  plan_count: 1
  slug: sap-ariba-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 1
  name: Sap Ariba Rate Limits
  slug: sap-ariba-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: SAP Ariba API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: sap-ariba-jsonschema-spectral-rules
- effective_rule_count: 61
  extends:
  - spectral:oas
  name: SAP Ariba API Rules
  rule_count: 20
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 11
  slug: sap-ariba-spectral-rules
scopes:
- name: Sap Ariba Scopes
  scope_count: 0
  slug: sap-ariba-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 37.7
  delta: -14.1
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 9.8
    contract_quality: 64.3
    developer_ergonomics: 26.2
    discoverability: 66.7
    governance: 9.8
    operational_transparency: 28.9
  previous_composite: 51.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/sap-ariba/refs/heads/main/screenshots/sap-ariba-2026-06-20T193415.png
security:
- kind: authentication
  name: Sap Ariba Authentication
  slug: sap-ariba-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Sap Ariba Domain Security
  slug: sap-ariba-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Sap Ariba Vulnerability Disclosure
  slug: sap-ariba-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: sap-ariba
tags:
- B2B
- Contract Management
- Procurement
- Sourcing
- Spend Analysis
- Supplier Management
- Supply Chain
use_cases:
- description: Run RFx events, auctions, and supplier evaluations to optimize procurement decisions.
  name: Strategic Sourcing
- description: Automate invoice submission, approval workflows, and payment reconciliation.
  name: Invoice Automation
- description: Monitor supplier risk exposure and manage risk assessment engagements.
  name: Supplier Risk Management
- description: Manage internal and external catalogs for guided buying experiences.
  name: Catalog Management
website: https://developer.ariba.com
---
