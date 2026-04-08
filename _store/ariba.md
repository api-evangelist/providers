---
aid: ariba
url: https://raw.githubusercontent.com/api-evangelist/ariba/refs/heads/main/apis.yml
apis:
- name: Ariba Network API
  description: Enables suppliers and buyers to exchange business documents and collaborate on the Ariba Network.
  image: https://www.ariba.com/ariba-network-logo.png
  humanURL: https://developer.ariba.com/api/network
  baseURL: https://api.ariba.com/v2/network
  tags:
  - B2B
  - EDI
  - Invoicing
  - Procurement
  - Supply Chain
  properties:
  - type: Documentation
    url: https://developer.ariba.com/api/network/docs
  - type: OpenAPI
    url: https://developer.ariba.com/api/network/openapi.json
  - type: Authentication
    url: https://developer.ariba.com/api/network/authentication
  - type: Sandbox
    url: https://sandbox.api.ariba.com/v2/network
- name: Ariba Procurement API
  description: Access procurement data including requisitions, purchase orders, receipts, and payment information.
  image: https://www.ariba.com/ariba-procurement-logo.png
  humanURL: https://developer.ariba.com/api/procurement
  baseURL: https://api.ariba.com/v2/procurement
  tags:
  - Procurement
  - Purchase Orders
  - Requisitions
  - Spend Management
  properties:
  - type: Documentation
    url: https://developer.ariba.com/api/procurement/docs
  - type: OpenAPI
    url: https://developer.ariba.com/api/procurement/openapi.json
  - type: Authentication
    url: https://developer.ariba.com/api/procurement/authentication
  - type: Sandbox
    url: https://sandbox.api.ariba.com/v2/procurement
- name: Ariba Sourcing API
  description: Manage sourcing projects, events, bids, and supplier responses for strategic sourcing activities.
  image: https://www.ariba.com/ariba-sourcing-logo.png
  humanURL: https://developer.ariba.com/api/sourcing
  baseURL: https://api.ariba.com/v2/sourcing
  tags:
  - Auctions
  - RFx
  - Sourcing
  - Supplier Management
  properties:
  - type: Documentation
    url: https://developer.ariba.com/api/sourcing/docs
  - type: OpenAPI
    url: https://developer.ariba.com/api/sourcing/openapi.json
  - type: Authentication
    url: https://developer.ariba.com/api/sourcing/authentication
  - type: Sandbox
    url: https://sandbox.api.ariba.com/v2/sourcing
- name: Ariba Contracts API
  description: Create, manage, and track contracts and contract workspaces throughout the contract lifecycle.
  image: https://www.ariba.com/ariba-contracts-logo.png
  humanURL: https://developer.ariba.com/api/contracts
  baseURL: https://api.ariba.com/v2/contracts
  tags:
  - CLM
  - Compliance
  - Contract Management
  - Contracts
  properties:
  - type: Documentation
    url: https://developer.ariba.com/api/contracts/docs
  - type: OpenAPI
    url: https://developer.ariba.com/api/contracts/openapi.json
  - type: Authentication
    url: https://developer.ariba.com/api/contracts/authentication
  - type: Sandbox
    url: https://sandbox.api.ariba.com/v2/contracts
- name: Ariba Supplier API
  description: Access and manage supplier information, qualifications, performance data, and risk assessments.
  image: https://www.ariba.com/ariba-supplier-logo.png
  humanURL: https://developer.ariba.com/api/supplier
  baseURL: https://api.ariba.com/v2/supplier
  tags:
  - Performance
  - Risk Management
  - Supplier Information
  - Supplier Management
  properties:
  - type: Documentation
    url: https://developer.ariba.com/api/supplier/docs
  - type: OpenAPI
    url: https://developer.ariba.com/api/supplier/openapi.json
  - type: Authentication
    url: https://developer.ariba.com/api/supplier/authentication
  - type: Sandbox
    url: https://sandbox.api.ariba.com/v2/supplier
- name: Ariba Analytics API
  description: Extract and analyze spend data, procurement metrics, and business intelligence from Ariba solutions.
  image: https://www.ariba.com/ariba-analytics-logo.png
  humanURL: https://developer.ariba.com/api/analytics
  baseURL: https://api.ariba.com/v2/analytics
  tags:
  - Analytics
  - Business Intelligence
  - Reporting
  - Spend Analysis
  properties:
  - type: Documentation
    url: https://developer.ariba.com/api/analytics/docs
  - type: OpenAPI
    url: https://developer.ariba.com/api/analytics/openapi.json
  - type: Authentication
    url: https://developer.ariba.com/api/analytics/authentication
  - type: Sandbox
    url: https://sandbox.api.ariba.com/v2/analytics
- name: Operational Reporting API for Procurement
  description: Provides synchronous and asynchronous access to operational procurement data including requisitions, purchase orders, receipts, and invoices for reporting and analytics purposes.
  humanURL: https://help.sap.com/docs/ariba-apis/operational-reporting-api-for-procurement/operational-reporting-api-for-procurement
  tags:
  - Operational Data
  - Procurement
  - Purchase Orders
  - Reporting
  - Requisitions
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/ariba-apis/operational-reporting-api-for-procurement/operational-reporting-api-for-procurement
- name: Operational Reporting API for Strategic Sourcing
  description: Enables extraction of operational sourcing data including sourcing projects, events, bids, and awards for reporting and business intelligence.
  humanURL: https://help.sap.com/docs/ariba-apis
  tags:
  - Bids
  - Events
  - Operational Data
  - Reporting
  - Strategic Sourcing
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/ariba-apis
- name: Analytical Reporting API for Strategic and Operational Procurement
  description: Enables client applications to extract reportable data from reporting facts and dimensions for strategic procurement and operational procurement analytics.
  humanURL: https://help.sap.com/docs/ariba-apis
  tags:
  - Analytics
  - Business Intelligence
  - Operational Procurement
  - Reporting
  - Strategic Procurement
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/ariba-apis
- name: Supplier Data API with Pagination
  description: Retrieves supplier data from SAP Ariba Supplier Lifecycle and Performance including supplier names, addresses, registration, qualification, preferred statuses, and questionnaire details with pagination support.
  humanURL: https://help.sap.com/docs/ariba-apis/supplier-data-api-with-pagination/about-supplier-data-api-with-pagination
  tags:
  - Pagination
  - Performance
  - Supplier Data
  - Supplier Lifecycle
  - Suppliers
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/ariba-apis/supplier-data-api-with-pagination/about-supplier-data-api-with-pagination
- name: Supplier Data API
  description: Provides access to supplier data from SAP Ariba Supplier Lifecycle and Performance or SAP Ariba Supplier Information and Performance Management solutions.
  humanURL: https://help.sap.com/docs/ariba-apis
  tags:
  - Supplier Data
  - Supplier Lifecycle
  - Suppliers
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/ariba-apis
- name: Supplier Data Extraction API
  description: Extracts supplier information and data for integration with external systems and reporting tools.
  humanURL: https://help.sap.com/docs/ariba-apis
  tags:
  - Data Extraction
  - Integration
  - Suppliers
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/ariba-apis
- name: Supplier Information API
  description: Provides access to detailed supplier information including company profiles, certifications, and classifications.
  humanURL: https://help.sap.com/docs/ariba-apis
  tags:
  - Profiles
  - Supplier Information
  - Suppliers
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/ariba-apis
- name: Supplier Invite API
  description: Enables programmatic invitation of suppliers to register and participate on the SAP Ariba platform.
  humanURL: https://help.sap.com/docs/ariba-apis
  tags:
  - Invitations
  - Onboarding
  - Suppliers
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/ariba-apis
- name: Ariba Network Supplier Profile API
  description: Manages supplier profile information on the Ariba Network including company details, capabilities, and certifications.
  humanURL: https://api.sap.com/api/supplier_management/overview
  tags:
  - Ariba Network
  - Certifications
  - Profiles
  - Suppliers
  properties:
  - type: Documentation
    url: https://api.sap.com/api/supplier_management/overview
- name: Contract Workspace Management APIs
  description: Enables creation and modification of procurement contract workspaces and their header information, as well as creation and retrieval of contract terms and contract requests.
  humanURL: https://help.sap.com/docs/ariba-apis/contract-workspace-management-apis/contract-workspace-management-apis
  tags:
  - Contract Requests
  - Contract Terms
  - Contract Workspaces
  - Contracts
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/ariba-apis/contract-workspace-management-apis/contract-workspace-management-apis
- name: Contract Workspace Retrieval API
  description: Retrieves contract workspace data and metadata for reporting and integration purposes.
  humanURL: https://help.sap.com/docs/ariba-apis
  tags:
  - Contract Workspaces
  - Contracts
  - Data Retrieval
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/ariba-apis
- name: Contract Terms Management API
  description: Manages contract terms including creation, modification, and retrieval of contract term details within contract workspaces.
  humanURL: https://help.sap.com/docs/ariba-apis
  tags:
  - Contract Terms
  - Contracts
  - Management
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/ariba-apis
- name: Contract Compliance API
  description: Provides access to contract compliance data to monitor and ensure adherence to contract terms and conditions.
  humanURL: https://help.sap.com/docs/ariba-apis
  tags:
  - Compliance
  - Contracts
  - Monitoring
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/ariba-apis
- name: Document Approval API
  description: Retrieves information about invoice and requisition changes and pending approvables in SAP Ariba for workflow automation.
  humanURL: https://help.sap.com/docs/ariba-apis
  tags:
  - Approvals
  - Invoices
  - Requisitions
  - Workflow
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/ariba-apis
- name: Ariba Network Purchase Orders API
  description: Manages purchase order documents on the Ariba Network for buyers and suppliers including creation, retrieval, and status tracking.
  humanURL: https://help.sap.com/docs/ariba-apis
  tags:
  - Ariba Network
  - Buyers
  - Purchase Orders
  - Suppliers
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/ariba-apis
- name: Purchase Orders Supplier API
  description: Enables suppliers to manage and respond to purchase orders received through the Ariba Network.
  humanURL: https://help.sap.com/docs/ariba-apis
  tags:
  - Order Management
  - Purchase Orders
  - Suppliers
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/ariba-apis
- name: Order Change Requests API for Buyers
  description: Allows buyers to create and manage purchase order change requests on the Ariba Network.
  humanURL: https://help.sap.com/docs/ariba-apis
  tags:
  - Buyers
  - Change Requests
  - Purchase Orders
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/ariba-apis
- name: Order Change Requests API for Suppliers
  description: Allows suppliers to create and manage purchase order change requests on the Ariba Network.
  humanURL: https://help.sap.com/docs/ariba-apis
  tags:
  - Change Requests
  - Purchase Orders
  - Suppliers
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/ariba-apis
- name: Ariba Network Invoice Header Data Extraction API
  description: Extracts invoice header data from the Ariba Network for reporting, reconciliation, and integration with financial systems.
  humanURL: https://help.sap.com/docs/ariba-apis
  tags:
  - Ariba Network
  - Data Extraction
  - Finance
  - Invoices
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/ariba-apis
- name: Ship Notice API for Buyers
  description: Enables buyers to retrieve and manage advance ship notices (ASNs) received from suppliers on the Ariba Network.
  humanURL: https://help.sap.com/docs/ariba-apis
  tags:
  - ASN
  - Buyers
  - Logistics
  - Ship Notices
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/ariba-apis
- name: Ship Notice API for Suppliers
  description: Enables suppliers to create and manage advance ship notices (ASNs) for orders on the Ariba Network.
  humanURL: https://help.sap.com/docs/ariba-apis
  tags:
  - ASN
  - Logistics
  - Ship Notices
  - Suppliers
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/ariba-apis
- name: Sourcing Project Management API
  description: Manages sourcing projects including creation, configuration, and lifecycle management of sourcing events.
  humanURL: https://help.sap.com/docs/ariba-apis
  tags:
  - Events
  - Project Management
  - Sourcing
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/ariba-apis
- name: Surrogate Bid API
  description: Enables submission of surrogate bids on behalf of suppliers in sourcing events.
  humanURL: https://help.sap.com/docs/ariba-apis
  tags:
  - Bidding
  - Sourcing
  - Suppliers
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/ariba-apis
- name: Discovery RFx Publication TO External Marketplace API
  description: Publishes RFx events from SAP Ariba to external marketplaces for broader supplier participation.
  humanURL: https://help.sap.com/docs/ariba-apis
  tags:
  - Discovery
  - Marketplace
  - RFx
  - Supplier Participation
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/ariba-apis
- name: Discovery RFx Publication FROM External Marketplace API
  description: Publishes RFx events from an external marketplace into SAP Ariba Discovery for sourcing activities.
  humanURL: https://help.sap.com/docs/ariba-apis
  tags:
  - Discovery
  - Marketplace
  - RFx
  - Sourcing
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/ariba-apis
- name: External Approval API for Sourcing and Supplier Management
  description: Integrates external approval workflows with SAP Ariba sourcing and supplier management processes.
  humanURL: https://help.sap.com/docs/ariba-apis
  tags:
  - Approvals
  - Sourcing
  - Supplier Management
  - Workflow
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/ariba-apis
- name: Flow Extension API
  description: Enriches processes and documents including purchase orders, invoices, ASNs, order confirmations, and receipts in Ariba Network with external data.
  humanURL: https://help.sap.com/docs/ariba-apis
  tags:
  - Ariba Network
  - Extensions
  - Integration
  - Workflow
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/ariba-apis
- name: SAP Ariba Catalog Content API
  description: Manages catalog content including creation, updates, and maintenance of product and service catalogs.
  humanURL: https://help.sap.com/docs/ariba-apis
  tags:
  - Catalogs
  - Content Management
  - Products
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/ariba-apis
- name: Catalog Connectivity Service API
  description: Enables connectivity to external catalog systems for punchout and roundtrip catalog integration.
  humanURL: https://help.sap.com/docs/ariba-apis
  tags:
  - Catalogs
  - Integration
  - Punchout
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/ariba-apis
- name: Internal Catalogs Shop API
  description: Provides access to internal catalog shopping functionality for procurement users to browse and select items.
  humanURL: https://help.sap.com/docs/ariba-apis
  tags:
  - Catalogs
  - Procurement
  - Shopping
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/ariba-apis
- name: Public Catalogs Shop API
  description: Provides access to public catalog shopping functionality for browsing and selecting items from public supplier catalogs.
  humanURL: https://help.sap.com/docs/ariba-apis
  tags:
  - Catalogs
  - Public Catalogs
  - Shopping
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/ariba-apis
- name: Network Catalog Management API
  description: Manages catalogs on the Ariba Network including catalog subscriptions, publishing, and lifecycle management.
  humanURL: https://help.sap.com/docs/ariba-apis
  tags:
  - Ariba Network
  - Catalog Management
  - Catalogs
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/ariba-apis
- name: Content Lookup API
  description: Looks up content data and references within SAP Ariba for integration and validation purposes.
  humanURL: https://help.sap.com/docs/ariba-apis
  tags:
  - Content
  - Integration
  - Lookup
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/ariba-apis
- name: Create Procurement Workspace API
  description: Enables programmatic creation of procurement workspaces for managing procurement projects and activities.
  humanURL: https://help.sap.com/docs/ariba-apis
  tags:
  - Procurement
  - Project Management
  - Workspaces
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/ariba-apis
- name: Dynamic Lookup Table API
  description: Manages dynamic lookup tables used for validation, mapping, and custom data references in procurement workflows.
  humanURL: https://help.sap.com/docs/ariba-apis
  tags:
  - Configuration
  - Data Management
  - Lookup Tables
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/ariba-apis
- name: Risk Exposure API
  description: Provides access to supplier risk exposure data including risk scores, assessments, and risk indicators.
  humanURL: https://help.sap.com/docs/ariba-apis
  tags:
  - Risk Exposure
  - Risk Management
  - Suppliers
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/ariba-apis
- name: Risk Category Information API for Supplier Risk Exposure
  description: Retrieves risk category information used to classify and assess supplier risk exposure levels.
  humanURL: https://help.sap.com/docs/ariba-apis
  tags:
  - Risk Categories
  - Risk Management
  - Suppliers
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/ariba-apis
- name: Supplier Risk Engagements API
  description: Manages supplier risk engagement processes including risk assessments and mitigation activities.
  humanURL: https://help.sap.com/docs/ariba-apis
  tags:
  - Engagements
  - Risk Management
  - Suppliers
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/ariba-apis
- name: Engagement Risk Assessment External Response Import API
  description: Imports external risk assessment responses into SAP Ariba for supplier risk engagement evaluations.
  humanURL: https://help.sap.com/docs/ariba-apis
  tags:
  - Assessments
  - External Data
  - Risk Management
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/ariba-apis
- name: Finding and Event Collaboration Integration API for Supplier Risk
  description: Integrates finding and event collaboration data for supplier risk management across systems.
  humanURL: https://help.sap.com/docs/ariba-apis
  tags:
  - Collaboration
  - Events
  - Risk Management
  - Suppliers
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/ariba-apis
- name: Pricing API for Product Sourcing Price Information
  description: Extracts pricing data for product sourcing including price benchmarks and market pricing information.
  humanURL: https://help.sap.com/docs/ariba-apis
  tags:
  - Pricing
  - Products
  - Sourcing
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/ariba-apis
- name: Audit Search API
  description: Provides audit trail search capabilities for tracking changes and actions across SAP Ariba processes.
  humanURL: https://help.sap.com/docs/ariba-apis
  tags:
  - Audit
  - Compliance
  - Tracking
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/ariba-apis
- name: Master Data Retrieval API for Procurement
  description: Retrieves master data used in operational procurement processes including commodity codes, units of measure, and accounting information.
  humanURL: https://help.sap.com/docs/ariba-apis
  tags:
  - Data Retrieval
  - Master Data
  - Procurement
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/ariba-apis
- name: Master Data Retrieval API for Sourcing
  description: Retrieves master data used in strategic sourcing processes including commodity codes, regions, and organizational structures.
  humanURL: https://help.sap.com/docs/ariba-apis
  tags:
  - Data Retrieval
  - Master Data
  - Sourcing
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/ariba-apis
- name: Master Data Integration Job Status API for Operational Procurement
  description: Monitors the status of master data integration jobs for operational procurement data synchronization.
  humanURL: https://help.sap.com/docs/ariba-apis
  tags:
  - Integration
  - Job Status
  - Master Data
  - Procurement
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/ariba-apis
- name: Proof of Service API for Buyers
  description: Enables buyers to manage proof of service documents for service-based procurement and receipt confirmations.
  humanURL: https://help.sap.com/docs/ariba-apis
  tags:
  - Buyers
  - Proof of Service
  - Receipts
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/ariba-apis
- name: Proof of Service API for Suppliers
  description: Enables suppliers to submit and manage proof of service documents for service delivery confirmation.
  humanURL: https://help.sap.com/docs/ariba-apis
  tags:
  - Delivery
  - Proof of Service
  - Suppliers
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/ariba-apis
- name: Asset Management API
  description: Manages asset-related data within SAP Ariba for tracking and maintaining procurement-related assets.
  humanURL: https://help.sap.com/docs/ariba-apis
  tags:
  - Assets
  - Management
  - Procurement
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/ariba-apis
- name: Bill of Materials Import API
  description: Imports bill of materials data into SAP Ariba for use in sourcing projects and procurement activities.
  humanURL: https://help.sap.com/docs/ariba-apis
  tags:
  - Bill of Materials
  - Import
  - Sourcing
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/ariba-apis
- name: Materials and BOM Tag Management API
  description: Manages material classifications and bill of materials tags for organizing and categorizing procurement items.
  humanURL: https://help.sap.com/docs/ariba-apis
  tags:
  - Bill of Materials
  - Classification
  - Materials
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/ariba-apis
- name: Item Volume Import API
  description: Imports item volume data into SAP Ariba for sourcing analysis and demand aggregation.
  humanURL: https://help.sap.com/docs/ariba-apis
  tags:
  - Import
  - Items
  - Sourcing
  - Volume
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/ariba-apis
- name: Product Hierarchy Management API
  description: Manages product category hierarchies used for organizing and classifying procurement items and spend categories.
  humanURL: https://help.sap.com/docs/ariba-apis
  tags:
  - Categories
  - Classification
  - Hierarchy
  - Products
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/ariba-apis
- name: User Qualification API
  description: Manages user qualifications and permissions within SAP Ariba for access control and role management.
  humanURL: https://help.sap.com/docs/ariba-apis
  tags:
  - Access Control
  - Qualifications
  - Users
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/ariba-apis
- name: SAP Ariba Custom Forms API
  description: Enables creation and management of custom forms for extending procurement and sourcing processes with additional data capture.
  humanURL: https://help.sap.com/docs/ariba-apis
  tags:
  - Custom Forms
  - Extensions
  - Procurement
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/ariba-apis
- name: SAP Ariba SCIM API
  description: Implements the System for Cross-domain Identity Management standard for user provisioning and identity management in SAP Ariba.
  humanURL: https://help.sap.com/docs/ariba-apis
  tags:
  - Identity Management
  - SCIM
  - User Provisioning
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/ariba-apis
- name: Event Management API
  description: Manages events and event-driven processes within SAP Ariba for tracking procurement and sourcing activities.
  humanURL: https://help.sap.com/docs/ariba-apis
  tags:
  - Events
  - Management
  - Tracking
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/ariba-apis
- name: Integration Event Monitoring Query API for Procurement
  description: Queries integration event data for monitoring and troubleshooting procurement integration processes.
  humanURL: https://help.sap.com/docs/ariba-apis
  tags:
  - Events
  - Integration
  - Monitoring
  - Procurement
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/ariba-apis
- name: Integration Monitoring API for Procurement
  description: Monitors integration processes and data flows for procurement operations between SAP Ariba and connected systems.
  humanURL: https://help.sap.com/docs/ariba-apis
  tags:
  - Integration
  - Monitoring
  - Procurement
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/ariba-apis
- name: Integration Monitoring API for Strategic Sourcing
  description: Monitors integration processes and data flows for strategic sourcing operations between SAP Ariba and connected systems.
  humanURL: https://help.sap.com/docs/ariba-apis
  tags:
  - Integration
  - Monitoring
  - Strategic Sourcing
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/ariba-apis
- name: Transaction Monitoring API
  description: Monitors transaction processing status and details across SAP Ariba procurement and sourcing workflows.
  humanURL: https://help.sap.com/docs/ariba-apis
  tags:
  - Monitoring
  - Transactions
  - Workflow
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/ariba-apis
- name: Asynchronous Requests Management API
  description: Manages asynchronous API request jobs including submission, status tracking, and result retrieval for long-running operations.
  humanURL: https://help.sap.com/docs/ariba-apis
  tags:
  - Asynchronous
  - Integration
  - Job Management
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/ariba-apis
- name: Configuration Parameter Review API
  description: Reviews and retrieves configuration parameters for SAP Ariba solutions to support administration and integration.
  humanURL: https://help.sap.com/docs/ariba-apis
  tags:
  - Administration
  - Configuration
  - Parameters
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/ariba-apis
- name: Data Replication Status for Multi-ERP Configurations
  description: Monitors data replication status across multi-ERP configurations connected to SAP Ariba.
  humanURL: https://help.sap.com/docs/ariba-apis
  tags:
  - Data Replication
  - Integration
  - Monitoring
  - Multi-ERP
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/ariba-apis
- name: Trading Partner Profile Certification API
  description: Manages trading partner profile certifications on the Ariba Network for partner validation and compliance.
  humanURL: https://help.sap.com/docs/ariba-apis
  tags:
  - Ariba Network
  - Certification
  - Compliance
  - Trading Partners
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/ariba-apis
- name: Cost Breakdown Data Extraction API
  description: Extracts cost breakdown and cost analysis data from sourcing events and projects for spend visibility.
  humanURL: https://help.sap.com/docs/ariba-apis
  tags:
  - Cost Analysis
  - Data Extraction
  - Sourcing
  - Spend
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/ariba-apis
- name: NDA Data Export API
  description: Exports non-disclosure agreement data from SAP Ariba for compliance tracking and legal management.
  humanURL: https://help.sap.com/docs/ariba-apis
  tags:
  - Compliance
  - Data Export
  - Legal
  - NDA
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/ariba-apis
- name: Public Procurement Notices Export API
  description: Exports public procurement notices for publishing tender opportunities to external portals and regulatory systems.
  humanURL: https://help.sap.com/docs/ariba-apis
  tags:
  - Export
  - Notices
  - Public Procurement
  - Tenders
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/ariba-apis
- name: Guided Buying Functional Documents API
  description: Manages functional documents within the SAP Ariba Guided Buying experience for streamlined procurement.
  humanURL: https://help.sap.com/docs/ariba-apis
  tags:
  - Documents
  - Guided Buying
  - Procurement
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/ariba-apis
- name: Planning Collaboration Buyer API
  description: Enables buyers to manage planning collaboration processes including demand forecasts and supply plans with trading partners.
  humanURL: https://help.sap.com/docs/ariba-apis
  tags:
  - Buyers
  - Collaboration
  - Planning
  - Supply Chain
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/ariba-apis
- name: Planning Collaboration Supplier API
  description: Enables suppliers to participate in planning collaboration processes including responding to demand forecasts and sharing supply commitments.
  humanURL: https://help.sap.com/docs/ariba-apis
  tags:
  - Collaboration
  - Planning
  - Suppliers
  - Supply Chain
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/ariba-apis
- name: Project Document Management API
  description: Manages project documents within SAP Ariba sourcing and procurement projects including upload, retrieval, and version control.
  humanURL: https://help.sap.com/docs/ariba-apis
  tags:
  - Documents
  - Project Management
  - Version Control
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/ariba-apis
- name: ETendering Notice Management API
  description: Manages electronic tendering notices for public sector and regulated procurement processes.
  humanURL: https://help.sap.com/docs/ariba-apis
  tags:
  - eTendering
  - Notices
  - Procurement
  - Public Sector
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/ariba-apis
- name: SAP Build Work Zone CDM Content API for Sourcing
  description: Provides content delivery and management for SAP Build Work Zone integration with SAP Ariba sourcing capabilities.
  humanURL: https://help.sap.com/docs/ariba-apis
  tags:
  - Content
  - Integration
  - SAP Build Work Zone
  - Sourcing
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/ariba-apis
- name: SAP Build Work Zone CDM Content API for Procurement
  description: Provides content delivery and management for SAP Build Work Zone integration with SAP Ariba procurement capabilities.
  humanURL: https://help.sap.com/docs/ariba-apis
  tags:
  - Content
  - Integration
  - Procurement
  - SAP Build Work Zone
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/ariba-apis
name: Ariba
tags:
- B2B
- Catalog Management
- Compliance
- Contracts
- Enterprise
- Integration
- Invoicing
- Procurement
- Risk Management
- SAP
- Sourcing
- Spend Analysis
- Supplier Lifecycle
- Suppliers
- Supply Chain
type: Contract
image: https://www.ariba.com/ariba-logo.png
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: SAP Ariba provides cloud-based procurement and supply chain collaboration solutions. These APIs enable integration with Ariba's procurement, sourcing, contract management, and supplier management capabilities.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

