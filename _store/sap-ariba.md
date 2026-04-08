---
aid: sap-ariba
url: https://raw.githubusercontent.com/api-evangelist/sap-ariba/refs/heads/main/apis.yml
apis:
- name: SAP Ariba Procurement API
  description: Enables integration with procurement processes including requisitions, purchase orders, invoices, suppliers, and receipts across the SAP Business Network.
  image: https://api.ariba.com/procurement-icon.png
  humanURL: https://developer.ariba.com/api/procurement
  baseURL: https://openapi.ariba.com/api/procurement
  tags:
  - Invoices
  - Procurement
  - Purchase Orders
  - Requisitions
  - Suppliers
  properties:
  - type: Documentation
    url: https://developer.ariba.com/api/apis/procurement/overview
  - type: OpenAPI
    url: openapi/sap-ariba-procurement-api.yml
  - type: JSON Schema
    url: json-schema/sap-ariba-purchase-order-schema.json
  - type: JSON-LD Context
    url: json-ld/sap-ariba-context.jsonld
  - type: Authentication
    url: https://developer.ariba.com/api/authentication
  - type: SAP Business Accelerator Hub
    url: https://api.sap.com/package/SAPAribaOpenAPIs/rest
  - type: SAP Help Portal
    url: https://help.sap.com/docs/ariba-apis
- name: SAP Ariba Sourcing API
  description: Provides access to sourcing events, RFx processes, auctions, and bid management.
  image: https://api.ariba.com/sourcing-icon.png
  humanURL: https://developer.ariba.com/api/sourcing
  baseURL: https://openapi.ariba.com/api/sourcing
  tags:
  - Auctions
  - Bidding
  - RFx
  - Sourcing
  properties:
  - type: Documentation
    url: https://developer.ariba.com/api/apis/sourcing/overview
  - type: OpenAPI
    url: https://developer.ariba.com/api/sourcing/openapi.json
  - type: Sandbox
    url: https://sandbox.ariba.com/api/sourcing
  - type: SAP Business Accelerator Hub
    url: https://api.sap.com/package/SAPAribaOpenAPIs/rest
- name: SAP Ariba Supplier Management API
  description: Manages supplier lifecycle including onboarding, qualification, performance, and risk assessment.
  image: https://api.ariba.com/supplier-icon.png
  humanURL: https://developer.ariba.com/api/supplier
  baseURL: https://openapi.ariba.com/api/supplier
  tags:
  - Onboarding
  - Performance
  - Risk Management
  - Suppliers
  properties:
  - type: Documentation
    url: https://developer.ariba.com/api/apis/supplier/overview
  - type: OpenAPI
    url: https://developer.ariba.com/api/supplier/openapi.json
  - type: Postman Collection
    url: https://developer.ariba.com/api/supplier/postman
  - type: SAP Business Accelerator Hub
    url: https://api.sap.com/api/supplier_management/overview
- name: SAP Ariba Contract Management API
  description: Enables contract creation, management, compliance tracking, and renewal workflows.
  image: https://api.ariba.com/contract-icon.png
  humanURL: https://developer.ariba.com/api/contracts
  baseURL: https://openapi.ariba.com/api/contracts
  tags:
  - CLM
  - Compliance
  - Contracts
  properties:
  - type: Documentation
    url: https://developer.ariba.com/api/apis/contracts/overview
  - type: OpenAPI
    url: https://developer.ariba.com/api/contracts/openapi.json
  - type: SAP Business Accelerator Hub
    url: https://api.sap.com/package/SAPAribaOpenAPIs/rest
- name: SAP Ariba Analytical Reporting API
  description: Provides access to spend analytics, reporting data, and business intelligence metrics.
  image: https://api.ariba.com/analytics-icon.png
  humanURL: https://developer.ariba.com/api/analytics
  baseURL: https://openapi.ariba.com/api/analytics
  tags:
  - Analytics
  - Business Intelligence
  - Reporting
  - Spend Analysis
  properties:
  - type: Documentation
    url: https://developer.ariba.com/api/apis/analytics/overview
  - type: OpenAPI
    url: https://developer.ariba.com/api/analytics/openapi.json
  - type: Query Guide
    url: https://developer.ariba.com/api/analytics/query-guide
  - type: SAP Business Accelerator Hub
    url: https://api.sap.com/package/SAPAribaOpenAPIs/rest
- name: SAP Ariba Invoice Management API
  description: Manages invoice processing, approval workflows, and payment status tracking.
  image: https://api.ariba.com/invoice-icon.png
  humanURL: https://developer.ariba.com/api/invoices
  baseURL: https://openapi.ariba.com/api/invoices
  tags:
  - AP Automation
  - Invoices
  - Payments
  properties:
  - type: Documentation
    url: https://developer.ariba.com/api/apis/invoices/overview
  - type: OpenAPI
    url: https://developer.ariba.com/api/invoices/openapi.json
  - type: SAP Business Accelerator Hub
    url: https://api.sap.com/package/SAPAribaOpenAPIs/rest
- name: Ariba Network Purchase Orders Buyer API
  description: Allows buyers to create, manage, and track purchase orders across the SAP Ariba Network.
  image: https://api.ariba.com/po-buyer-icon.png
  humanURL: https://api.sap.com/api/purchase_orders/overview
  baseURL: https://openapi.ariba.com/api/purchase-orders-buyer
  tags:
  - Ariba Network
  - Buyers
  - Purchase Orders
  properties:
  - type: Documentation
    url: https://api.sap.com/api/purchase_orders/overview
  - type: SAP Business Accelerator Hub
    url: https://api.sap.com/api/purchase_orders/overview
- name: Ariba Network Purchase Orders Supplier API
  description: Enables suppliers to retrieve purchase order and line item information from buyers on the SAP Business Network.
  image: https://api.ariba.com/po-supplier-icon.png
  humanURL: https://api.sap.com/api/purchase_orders_supplier/overview
  baseURL: https://openapi.ariba.com/api/purchase-orders-supplier
  tags:
  - Ariba Network
  - Purchase Orders
  - Suppliers
  properties:
  - type: Documentation
    url: https://api.sap.com/api/purchase_orders_supplier/overview
  - type: SAP Help
    url: https://help.sap.com/doc/3b0b2f4faaa242dda9004b9f337592bf/cloud/en-US/purchase_order_supplier_api.pdf
  - type: SAP Business Accelerator Hub
    url: https://api.sap.com/api/purchase_orders_supplier/overview
- name: Ariba Network Supplier Profile API
  description: Provides access to supplier profile details on the SAP Ariba Network.
  image: https://api.ariba.com/supplier-profile-icon.png
  humanURL: https://api.sap.com/api/supplier_management/overview
  baseURL: https://openapi.ariba.com/api/supplier-profile
  tags:
  - Ariba Network
  - Profiles
  - Suppliers
  properties:
  - type: Documentation
    url: https://api.sap.com/api/supplier_management/overview
  - type: SAP Business Accelerator Hub
    url: https://api.sap.com/api/supplier_management/overview
- name: Ariba Network Invoice Header Data Extraction API
  description: Extracts invoice header information from the SAP Ariba Network for data analysis and integration.
  image: https://api.ariba.com/invoice-extraction-icon.png
  humanURL: https://help.sap.com/docs/ariba-apis
  baseURL: https://openapi.ariba.com/api/invoice-extraction
  tags:
  - Ariba Network
  - Data Extraction
  - Invoices
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/ariba-apis
  - type: SAP Business Accelerator Hub
    url: https://api.sap.com/package/SAPAribaOpenAPIs/rest
- name: SAP Ariba Contract Compliance API
  description: Ensures contract compliance by validating procurement activities against contract terms and conditions.
  image: https://api.ariba.com/compliance-icon.png
  humanURL: https://help.sap.com/docs/ariba-apis
  baseURL: https://openapi.ariba.com/api/contract-compliance
  tags:
  - Compliance
  - Contracts
  - Procurement
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/ariba-apis
  - type: SAP Business Accelerator Hub
    url: https://api.sap.com/package/SAPAribaOpenAPIs/rest
- name: SAP Ariba Supplier Data API
  description: Provides access to general supplier data including company information and classification details.
  image: https://api.ariba.com/supplier-data-icon.png
  humanURL: https://help.sap.com/docs/ariba-apis
  baseURL: https://openapi.ariba.com/api/supplier-data
  tags:
  - Data
  - Master Data
  - Suppliers
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/ariba-apis
  - type: SAP Business Accelerator Hub
    url: https://api.sap.com/package/SAPAribaOpenAPIs/rest
- name: SAP Ariba Supplier Data API with Pagination
  description: Retrieves supplier data with pagination support for handling large datasets.
  image: https://api.ariba.com/supplier-data-paginated-icon.png
  humanURL: https://help.sap.com/docs/ariba-apis
  baseURL: https://openapi.ariba.com/api/supplier-data-paginated
  tags:
  - Data
  - Pagination
  - Suppliers
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/ariba-apis
  - type: SAP Business Accelerator Hub
    url: https://api.sap.com/package/SAPAribaOpenAPIs/rest
- name: SAP Ariba Supplier Data Extraction API
  description: Extracts detailed supplier information for integration with external systems and analytics.
  image: https://api.ariba.com/supplier-extraction-icon.png
  humanURL: https://help.sap.com/docs/ariba-apis
  baseURL: https://openapi.ariba.com/api/supplier-data-extraction
  tags:
  - Data Extraction
  - Integration
  - Suppliers
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/ariba-apis
  - type: SAP Business Accelerator Hub
    url: https://api.sap.com/package/SAPAribaOpenAPIs/rest
- name: SAP Ariba Supplier Information API
  description: Provides supplier profile and related detail information for supplier lifecycle management.
  image: https://api.ariba.com/supplier-info-icon.png
  humanURL: https://help.sap.com/docs/ariba-apis
  baseURL: https://openapi.ariba.com/api/supplier-information
  tags:
  - Lifecycle
  - Profiles
  - Suppliers
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/ariba-apis
  - type: SAP Business Accelerator Hub
    url: https://api.sap.com/package/SAPAribaOpenAPIs/rest
- name: SAP Ariba Supplier Invite API
  description: Invites suppliers to participate in procurement transactions and network activities.
  image: https://api.ariba.com/supplier-invite-icon.png
  humanURL: https://help.sap.com/docs/ariba-apis
  baseURL: https://openapi.ariba.com/api/supplier-invite
  tags:
  - Invitations
  - Onboarding
  - Suppliers
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/ariba-apis
  - type: SAP Business Accelerator Hub
    url: https://api.sap.com/package/SAPAribaOpenAPIs/rest
- name: SAP Ariba Risk Exposure API
  description: Analyzes and reports on supplier risk exposure across the supply chain.
  image: https://api.ariba.com/risk-exposure-icon.png
  humanURL: https://help.sap.com/docs/ariba-apis
  baseURL: https://openapi.ariba.com/api/risk-exposure
  tags:
  - Risk Management
  - Suppliers
  - Supply Chain
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/ariba-apis
  - type: SAP Business Accelerator Hub
    url: https://api.sap.com/package/SAPAribaOpenAPIs/rest
- name: SAP Ariba Supplier Risk Engagements API
  description: Manages supplier risk engagement activities and assessment workflows.
  image: https://api.ariba.com/risk-engagements-icon.png
  humanURL: https://help.sap.com/docs/ariba-apis
  baseURL: https://openapi.ariba.com/api/supplier-risk-engagements
  tags:
  - Assessments
  - Risk Management
  - Suppliers
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/ariba-apis
  - type: SAP Business Accelerator Hub
    url: https://api.sap.com/package/SAPAribaOpenAPIs/rest
- name: SAP Ariba Risk Category Information API
  description: Provides risk classification and category details for supplier risk exposure analysis.
  image: https://api.ariba.com/risk-category-icon.png
  humanURL: https://help.sap.com/docs/ariba-apis
  baseURL: https://openapi.ariba.com/api/risk-category
  tags:
  - Categories
  - Classification
  - Risk Management
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/ariba-apis
  - type: SAP Business Accelerator Hub
    url: https://api.sap.com/package/SAPAribaOpenAPIs/rest
- name: SAP Ariba Document Approval API
  description: Handles approval workflows for procurement documents including requisitions and purchase orders.
  image: https://api.ariba.com/approval-icon.png
  humanURL: https://help.sap.com/docs/ariba-apis
  baseURL: https://openapi.ariba.com/api/document-approval
  tags:
  - Approvals
  - Documents
  - Workflows
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/ariba-apis
  - type: SAP Business Accelerator Hub
    url: https://api.sap.com/package/SAPAribaOpenAPIs/rest
- name: SAP Ariba External Approval API for Sourcing and Supplier Management
  description: Enables external approval routing for sourcing events and supplier management processes.
  image: https://api.ariba.com/external-approval-icon.png
  humanURL: https://help.sap.com/docs/ariba-apis
  baseURL: https://openapi.ariba.com/api/external-approval
  tags:
  - Approvals
  - Sourcing
  - Supplier Management
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/ariba-apis
  - type: SAP Business Accelerator Hub
    url: https://api.sap.com/package/SAPAribaOpenAPIs/rest
- name: SAP Ariba Catalog Content API
  description: Enables applications to manage catalog content and get faceted catalog data based on specific attributes.
  image: https://api.ariba.com/catalog-content-icon.png
  humanURL: https://help.sap.com/docs/ariba-apis
  baseURL: https://openapi.ariba.com/api/catalog-content
  tags:
  - Catalogs
  - Content Management
  - Products
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/ariba-apis
  - type: SAP Business Accelerator Hub
    url: https://api.sap.com/package/SAPAribaOpenAPIs/rest
- name: SAP Ariba Network Catalog Management API
  description: Controls catalog operations across the SAP Ariba Network including subscriptions and publishing.
  image: https://api.ariba.com/catalog-mgmt-icon.png
  humanURL: https://help.sap.com/docs/ariba-apis
  baseURL: https://openapi.ariba.com/api/network-catalog
  tags:
  - Catalogs
  - Network
  - Publishing
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/ariba-apis
  - type: SAP Business Accelerator Hub
    url: https://api.sap.com/package/SAPAribaOpenAPIs/rest
- name: SAP Ariba Internal Catalogs Shop API
  description: Manages internal catalog shopping experiences for procurement users.
  image: https://api.ariba.com/internal-catalog-icon.png
  humanURL: https://help.sap.com/docs/ariba-apis
  baseURL: https://openapi.ariba.com/api/internal-catalogs
  tags:
  - Catalogs
  - Internal
  - Shopping
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/ariba-apis
  - type: SAP Business Accelerator Hub
    url: https://api.sap.com/package/SAPAribaOpenAPIs/rest
- name: SAP Ariba Public Catalogs Shop API
  description: Manages public marketplace catalog experiences for procurement users.
  image: https://api.ariba.com/public-catalog-icon.png
  humanURL: https://help.sap.com/docs/ariba-apis
  baseURL: https://openapi.ariba.com/api/public-catalogs
  tags:
  - Catalogs
  - Marketplace
  - Shopping
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/ariba-apis
  - type: SAP Business Accelerator Hub
    url: https://api.sap.com/package/SAPAribaOpenAPIs/rest
- name: SAP Ariba Contract Workspace Retrieval API
  description: Retrieves contract workspace information for contract lifecycle management.
  image: https://api.ariba.com/workspace-retrieval-icon.png
  humanURL: https://help.sap.com/docs/ariba-apis
  baseURL: https://openapi.ariba.com/api/contract-workspace-retrieval
  tags:
  - CLM
  - Contracts
  - Workspaces
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/ariba-apis
  - type: SAP Business Accelerator Hub
    url: https://api.sap.com/package/SAPAribaOpenAPIs/rest
- name: SAP Ariba Contract Workspace Management API
  description: Administers contract collaboration spaces including creation, updates, and lifecycle management.
  image: https://api.ariba.com/workspace-mgmt-icon.png
  humanURL: https://help.sap.com/docs/ariba-apis
  baseURL: https://openapi.ariba.com/api/contract-workspace-management
  tags:
  - Contracts
  - Management
  - Workspaces
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/ariba-apis
  - type: SAP Business Accelerator Hub
    url: https://api.sap.com/package/SAPAribaOpenAPIs/rest
- name: SAP Ariba Contract Terms Management API
  description: Administers contract term definitions and clause libraries.
  image: https://api.ariba.com/contract-terms-icon.png
  humanURL: https://help.sap.com/docs/ariba-apis
  baseURL: https://openapi.ariba.com/api/contract-terms
  tags:
  - Clauses
  - Contracts
  - Terms
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/ariba-apis
  - type: SAP Business Accelerator Hub
    url: https://api.sap.com/package/SAPAribaOpenAPIs/rest
- name: SAP Ariba Operational Reporting API for Procurement
  description: Delivers operational metrics and reporting data for procurement activities.
  image: https://api.ariba.com/ops-reporting-procurement-icon.png
  humanURL: https://help.sap.com/docs/ariba-apis/operational-reporting-api-for-procurement/operational-reporting-api-for-procurement
  baseURL: https://openapi.ariba.com/api/operational-reporting-procurement
  tags:
  - Operations
  - Procurement
  - Reporting
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/ariba-apis/operational-reporting-api-for-procurement/operational-reporting-api-for-procurement
  - type: SAP Business Accelerator Hub
    url: https://api.sap.com/package/SAPAribaOpenAPIs/rest
- name: SAP Ariba Operational Reporting API for Strategic Sourcing
  description: Delivers operational metrics and reporting data for strategic sourcing activities.
  image: https://api.ariba.com/ops-reporting-sourcing-icon.png
  humanURL: https://help.sap.com/docs/ariba-apis
  baseURL: https://openapi.ariba.com/api/operational-reporting-sourcing
  tags:
  - Operations
  - Reporting
  - Sourcing
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/ariba-apis
  - type: SAP Business Accelerator Hub
    url: https://api.sap.com/package/SAPAribaOpenAPIs/rest
- name: SAP Ariba Analytical Reporting API for Strategic and Operational Procurement
  description: Delivers analytics across strategic and operational procurement domains including contracts, sourcing, spend analysis, and buying.
  image: https://api.ariba.com/analytical-reporting-icon.png
  humanURL: https://help.sap.com/docs/ariba-apis
  baseURL: https://openapi.ariba.com/api/analytical-reporting
  tags:
  - Analytics
  - Operational Procurement
  - Reporting
  - Strategic Procurement
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/ariba-apis
  - type: SAP Business Accelerator Hub
    url: https://api.sap.com/package/SAPAribaOpenAPIs/rest
- name: SAP Ariba Master Data Retrieval API for Sourcing
  description: Obtains master data for sourcing operations including commodity codes and regions.
  image: https://api.ariba.com/master-data-sourcing-icon.png
  humanURL: https://help.sap.com/docs/ariba-apis
  baseURL: https://openapi.ariba.com/api/master-data-sourcing
  tags:
  - Master Data
  - Reference Data
  - Sourcing
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/ariba-apis
  - type: SAP Business Accelerator Hub
    url: https://api.sap.com/package/SAPAribaOpenAPIs/rest
- name: SAP Ariba Master Data Retrieval API for Procurement
  description: Retrieves procurement master data including cost centers, accounts, and units of measure.
  image: https://api.ariba.com/master-data-procurement-icon.png
  humanURL: https://help.sap.com/docs/ariba-apis
  baseURL: https://openapi.ariba.com/api/master-data-procurement
  tags:
  - Master Data
  - Procurement
  - Reference Data
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/ariba-apis
  - type: SAP Business Accelerator Hub
    url: https://api.sap.com/package/SAPAribaOpenAPIs/rest
- name: SAP Ariba Sourcing Project Management API
  description: Oversees sourcing project workflows including event creation and management.
  image: https://api.ariba.com/sourcing-project-icon.png
  humanURL: https://help.sap.com/docs/ariba-apis
  baseURL: https://openapi.ariba.com/api/sourcing-project
  tags:
  - Events
  - Projects
  - Sourcing
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/ariba-apis
  - type: SAP Business Accelerator Hub
    url: https://api.sap.com/package/SAPAribaOpenAPIs/rest
- name: SAP Ariba Event Management API
  description: Manages sourcing events and their lifecycle including RFx and auction events.
  image: https://api.ariba.com/event-mgmt-icon.png
  humanURL: https://help.sap.com/docs/ariba-apis
  baseURL: https://openapi.ariba.com/api/event-management
  tags:
  - Auctions
  - Events
  - RFx
  - Sourcing
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/ariba-apis
  - type: SAP Business Accelerator Hub
    url: https://api.sap.com/package/SAPAribaOpenAPIs/rest
- name: SAP Ariba Surrogate Bid API
  description: Enables proxy bidding mechanisms for sourcing events on behalf of suppliers.
  image: https://api.ariba.com/surrogate-bid-icon.png
  humanURL: https://help.sap.com/docs/ariba-apis
  baseURL: https://openapi.ariba.com/api/surrogate-bid
  tags:
  - Bidding
  - Proxy
  - Sourcing
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/ariba-apis
  - type: SAP Business Accelerator Hub
    url: https://api.sap.com/package/SAPAribaOpenAPIs/rest
- name: SAP Ariba Order Change Requests API for Buyers
  description: Manages order modification requests from the buyer perspective.
  image: https://api.ariba.com/order-change-buyer-icon.png
  humanURL: https://help.sap.com/docs/ariba-apis
  baseURL: https://openapi.ariba.com/api/order-change-buyer
  tags:
  - Buyers
  - Change Requests
  - Purchase Orders
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/ariba-apis
  - type: SAP Business Accelerator Hub
    url: https://api.sap.com/package/SAPAribaOpenAPIs/rest
- name: SAP Ariba Order Change Requests API for Suppliers
  description: Handles order change request processing from the supplier perspective.
  image: https://api.ariba.com/order-change-supplier-icon.png
  humanURL: https://help.sap.com/docs/ariba-apis
  baseURL: https://openapi.ariba.com/api/order-change-supplier
  tags:
  - Change Requests
  - Purchase Orders
  - Suppliers
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/ariba-apis
  - type: SAP Business Accelerator Hub
    url: https://api.sap.com/package/SAPAribaOpenAPIs/rest
- name: SAP Ariba Ship Notice API for Buyers
  description: Receives and processes shipment notifications for buyers on the Ariba Network.
  image: https://api.ariba.com/ship-notice-buyer-icon.png
  humanURL: https://help.sap.com/docs/ariba-apis
  baseURL: https://openapi.ariba.com/api/ship-notice-buyer
  tags:
  - Buyers
  - Notifications
  - Shipping
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/ariba-apis
  - type: SAP Business Accelerator Hub
    url: https://api.sap.com/package/SAPAribaOpenAPIs/rest
- name: SAP Ariba Ship Notice API for Suppliers
  description: Sends shipment notifications from suppliers to buyers on the Ariba Network.
  image: https://api.ariba.com/ship-notice-supplier-icon.png
  humanURL: https://help.sap.com/docs/ariba-apis
  baseURL: https://openapi.ariba.com/api/ship-notice-supplier
  tags:
  - Notifications
  - Shipping
  - Suppliers
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/ariba-apis
  - type: SAP Business Accelerator Hub
    url: https://api.sap.com/package/SAPAribaOpenAPIs/rest
- name: SAP Ariba Proof of Service API for Buyers
  description: Validates service fulfillment and delivery for buyers in service procurement.
  image: https://api.ariba.com/pos-buyer-icon.png
  humanURL: https://help.sap.com/docs/ariba-apis
  baseURL: https://openapi.ariba.com/api/proof-of-service-buyer
  tags:
  - Buyers
  - Proof of Service
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/ariba-apis
  - type: SAP Business Accelerator Hub
    url: https://api.sap.com/package/SAPAribaOpenAPIs/rest
- name: SAP Ariba Proof of Service API for Suppliers
  description: Validates service fulfillment and delivery for suppliers in service procurement.
  image: https://api.ariba.com/pos-supplier-icon.png
  humanURL: https://help.sap.com/docs/ariba-apis
  baseURL: https://openapi.ariba.com/api/proof-of-service-supplier
  tags:
  - Proof of Service
  - Suppliers
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/ariba-apis
  - type: SAP Business Accelerator Hub
    url: https://api.sap.com/package/SAPAribaOpenAPIs/rest
- name: SAP Ariba Planning Collaboration Buyer API
  description: Enables buyer-side planning and forecast collaboration with suppliers.
  image: https://api.ariba.com/planning-buyer-icon.png
  humanURL: https://help.sap.com/docs/ariba-apis
  baseURL: https://openapi.ariba.com/api/planning-collaboration-buyer
  tags:
  - Buyers
  - Collaboration
  - Forecasting
  - Planning
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/ariba-apis
  - type: SAP Business Accelerator Hub
    url: https://api.sap.com/package/SAPAribaOpenAPIs/rest
- name: SAP Ariba Planning Collaboration Supplier API
  description: Enables supplier-side planning and forecast collaboration with buyers.
  image: https://api.ariba.com/planning-supplier-icon.png
  humanURL: https://help.sap.com/docs/ariba-apis
  baseURL: https://openapi.ariba.com/api/planning-collaboration-supplier
  tags:
  - Collaboration
  - Forecasting
  - Planning
  - Suppliers
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/ariba-apis
  - type: SAP Business Accelerator Hub
    url: https://api.sap.com/package/SAPAribaOpenAPIs/rest
- name: SAP Ariba Item Volume Import API
  description: Imports item volume data for procurement planning and sourcing optimization.
  image: https://api.ariba.com/item-volume-icon.png
  humanURL: https://help.sap.com/docs/ariba-apis
  baseURL: https://openapi.ariba.com/api/item-volume-import
  tags:
  - Import
  - Planning
  - Volume
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/ariba-apis
  - type: SAP Business Accelerator Hub
    url: https://api.sap.com/package/SAPAribaOpenAPIs/rest
- name: SAP Ariba Bill of Materials Import API
  description: Imports bill of materials structures for sourcing and procurement processes.
  image: https://api.ariba.com/bom-icon.png
  humanURL: https://help.sap.com/docs/ariba-apis
  baseURL: https://openapi.ariba.com/api/bom-import
  tags:
  - BOM
  - Import
  - Materials
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/ariba-apis
  - type: SAP Business Accelerator Hub
    url: https://api.sap.com/package/SAPAribaOpenAPIs/rest
- name: SAP Ariba Product Hierarchy Management API
  description: Organizes product classification and category hierarchy structures.
  image: https://api.ariba.com/product-hierarchy-icon.png
  humanURL: https://help.sap.com/docs/ariba-apis
  baseURL: https://openapi.ariba.com/api/product-hierarchy
  tags:
  - Classification
  - Hierarchy
  - Products
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/ariba-apis
  - type: SAP Business Accelerator Hub
    url: https://api.sap.com/package/SAPAribaOpenAPIs/rest
- name: SAP Ariba Pricing API for Product Sourcing
  description: Extracts and manages pricing data for product sourcing price information.
  image: https://api.ariba.com/pricing-icon.png
  humanURL: https://help.sap.com/docs/ariba-apis
  baseURL: https://openapi.ariba.com/api/pricing
  tags:
  - Pricing
  - Products
  - Sourcing
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/ariba-apis
  - type: SAP Business Accelerator Hub
    url: https://api.sap.com/package/SAPAribaOpenAPIs/rest
- name: SAP Ariba Cost Breakdown Data Extraction API
  description: Extracts cost component and cost breakdown information for analysis.
  image: https://api.ariba.com/cost-breakdown-icon.png
  humanURL: https://help.sap.com/docs/ariba-apis
  baseURL: https://openapi.ariba.com/api/cost-breakdown
  tags:
  - Cost Analysis
  - Data Extraction
  - Sourcing
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/ariba-apis
  - type: SAP Business Accelerator Hub
    url: https://api.sap.com/package/SAPAribaOpenAPIs/rest
- name: SAP Ariba Content Lookup API
  description: Searches and retrieves content across the SAP Ariba platform.
  image: https://api.ariba.com/content-lookup-icon.png
  humanURL: https://help.sap.com/docs/ariba-apis
  baseURL: https://openapi.ariba.com/api/content-lookup
  tags:
  - Content
  - Lookup
  - Search
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/ariba-apis
  - type: SAP Business Accelerator Hub
    url: https://api.sap.com/package/SAPAribaOpenAPIs/rest
- name: SAP Ariba Audit Search API
  description: Provides audit trail search capabilities across procurement and sourcing activities.
  image: https://api.ariba.com/audit-icon.png
  humanURL: https://help.sap.com/docs/ariba-apis
  baseURL: https://openapi.ariba.com/api/audit-search
  tags:
  - Audit
  - Compliance
  - Search
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/ariba-apis
  - type: SAP Business Accelerator Hub
    url: https://api.sap.com/package/SAPAribaOpenAPIs/rest
- name: SAP Ariba Create Procurement Workspace API
  description: Initiates and creates procurement workspace environments for project collaboration.
  image: https://api.ariba.com/procurement-workspace-icon.png
  humanURL: https://help.sap.com/docs/ariba-apis
  baseURL: https://openapi.ariba.com/api/procurement-workspace
  tags:
  - Collaboration
  - Procurement
  - Workspaces
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/ariba-apis
  - type: SAP Business Accelerator Hub
    url: https://api.sap.com/package/SAPAribaOpenAPIs/rest
- name: SAP Ariba Flow Extension API
  description: Extends workflow processing capabilities for custom procurement and sourcing processes.
  image: https://api.ariba.com/flow-extension-icon.png
  humanURL: https://help.sap.com/docs/ariba-apis
  baseURL: https://openapi.ariba.com/api/flow-extension
  tags:
  - Customization
  - Extensions
  - Workflows
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/ariba-apis
  - type: SAP Business Accelerator Hub
    url: https://api.sap.com/package/SAPAribaOpenAPIs/rest
- name: SAP Ariba Asynchronous Requests Management API
  description: Manages long-running asynchronous operations and their status tracking.
  image: https://api.ariba.com/async-requests-icon.png
  humanURL: https://help.sap.com/docs/ariba-apis
  baseURL: https://openapi.ariba.com/api/async-requests
  tags:
  - Async
  - Management
  - Operations
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/ariba-apis
  - type: SAP Business Accelerator Hub
    url: https://api.sap.com/package/SAPAribaOpenAPIs/rest
- name: SAP Ariba Integration Event Monitoring Query API for Procurement
  description: Monitors and queries integration events for procurement process tracking.
  image: https://api.ariba.com/event-monitoring-icon.png
  humanURL: https://help.sap.com/docs/ariba-apis
  baseURL: https://openapi.ariba.com/api/integration-event-monitoring
  tags:
  - Events
  - Integration
  - Monitoring
  - Procurement
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/ariba-apis
  - type: SAP Business Accelerator Hub
    url: https://api.sap.com/package/SAPAribaOpenAPIs/rest
- name: SAP Ariba Integration Monitoring API for Procurement
  description: Tracks integration health and performance for procurement system integrations.
  image: https://api.ariba.com/integration-monitoring-procurement-icon.png
  humanURL: https://help.sap.com/docs/ariba-apis
  baseURL: https://openapi.ariba.com/api/integration-monitoring-procurement
  tags:
  - Integration
  - Monitoring
  - Procurement
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/ariba-apis
  - type: SAP Business Accelerator Hub
    url: https://api.sap.com/package/SAPAribaOpenAPIs/rest
- name: SAP Ariba Integration Monitoring API for Strategic Sourcing
  description: Tracks integration health and performance for strategic sourcing system integrations.
  image: https://api.ariba.com/integration-monitoring-sourcing-icon.png
  humanURL: https://help.sap.com/docs/ariba-apis
  baseURL: https://openapi.ariba.com/api/integration-monitoring-sourcing
  tags:
  - Integration
  - Monitoring
  - Sourcing
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/ariba-apis
  - type: SAP Business Accelerator Hub
    url: https://api.sap.com/package/SAPAribaOpenAPIs/rest
- name: SAP Ariba Transaction Monitoring API
  description: Observes and reports on transaction activities and processing status.
  image: https://api.ariba.com/transaction-monitoring-icon.png
  humanURL: https://help.sap.com/docs/ariba-apis
  baseURL: https://openapi.ariba.com/api/transaction-monitoring
  tags:
  - Monitoring
  - Operations
  - Transactions
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/ariba-apis
  - type: SAP Business Accelerator Hub
    url: https://api.sap.com/package/SAPAribaOpenAPIs/rest
- name: SAP Ariba NDA Data Export API
  description: Exports non-disclosure agreement data for compliance and record keeping.
  image: https://api.ariba.com/nda-icon.png
  humanURL: https://help.sap.com/docs/ariba-apis
  baseURL: https://openapi.ariba.com/api/nda-export
  tags:
  - Compliance
  - Export
  - NDA
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/ariba-apis
  - type: SAP Business Accelerator Hub
    url: https://api.sap.com/package/SAPAribaOpenAPIs/rest
- name: SAP Ariba Catalog Connectivity Service API
  description: Connects to external catalog systems for punchout and roundtrip catalog integration.
  image: https://api.ariba.com/catalog-connectivity-icon.png
  humanURL: https://help.sap.com/docs/ariba-apis
  baseURL: https://openapi.ariba.com/api/catalog-connectivity
  tags:
  - Catalogs
  - Integration
  - Punchout
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/ariba-apis
  - type: SAP Business Accelerator Hub
    url: https://api.sap.com/package/SAPAribaOpenAPIs/rest
- name: SAP Ariba Trading Partner Profile Certification API
  description: Manages trading partner certifications and compliance documentation.
  image: https://api.ariba.com/trading-partner-icon.png
  humanURL: https://help.sap.com/docs/ariba-apis
  baseURL: https://openapi.ariba.com/api/trading-partner-certification
  tags:
  - Certification
  - Compliance
  - Trading Partners
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/ariba-apis
  - type: SAP Business Accelerator Hub
    url: https://api.sap.com/package/SAPAribaOpenAPIs/rest
- name: SAP Ariba User Qualification API
  description: Validates user eligibility and qualifications for procurement processes.
  image: https://api.ariba.com/user-qualification-icon.png
  humanURL: https://help.sap.com/docs/ariba-apis
  baseURL: https://openapi.ariba.com/api/user-qualification
  tags:
  - Access
  - Qualifications
  - Users
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/ariba-apis
  - type: SAP Business Accelerator Hub
    url: https://api.sap.com/package/SAPAribaOpenAPIs/rest
- name: SAP Ariba SCIM API
  description: Implements System for Cross-domain Identity Management for user provisioning and management.
  image: https://api.ariba.com/scim-icon.png
  humanURL: https://help.sap.com/docs/ariba-apis
  baseURL: https://openapi.ariba.com/api/scim
  tags:
  - Identity
  - Provisioning
  - SCIM
  - User Management
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/ariba-apis
  - type: SAP Business Accelerator Hub
    url: https://api.sap.com/package/SAPAribaOpenAPIs/rest
- name: SAP Ariba Custom Forms API
  description: Creates and manages custom form definitions for procurement and sourcing workflows.
  image: https://api.ariba.com/custom-forms-icon.png
  humanURL: https://help.sap.com/docs/ariba-apis
  baseURL: https://openapi.ariba.com/api/custom-forms
  tags:
  - Customization
  - Forms
  - Workflows
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/ariba-apis
  - type: SAP Business Accelerator Hub
    url: https://api.sap.com/package/SAPAribaOpenAPIs/rest
- name: SAP Ariba Dynamic Lookup Table API
  description: Manages dynamic reference and lookup tables for configurable procurement data.
  image: https://api.ariba.com/lookup-table-icon.png
  humanURL: https://help.sap.com/docs/ariba-apis
  baseURL: https://openapi.ariba.com/api/dynamic-lookup-table
  tags:
  - Configuration
  - Lookup Tables
  - Reference Data
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/ariba-apis
  - type: SAP Business Accelerator Hub
    url: https://api.sap.com/package/SAPAribaOpenAPIs/rest
- name: SAP Ariba Guided Buying Functional Documents API
  description: Manages guided buying documentation and functional purchase request workflows.
  image: https://api.ariba.com/guided-buying-icon.png
  humanURL: https://help.sap.com/docs/ariba-apis
  baseURL: https://openapi.ariba.com/api/guided-buying
  tags:
  - Documents
  - Guided Buying
  - Procurement
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/ariba-apis
  - type: SAP Business Accelerator Hub
    url: https://api.sap.com/package/SAPAribaOpenAPIs/rest
- name: SAP Ariba Asset Management API
  description: Manages asset lifecycle and inventory tracking for procurement-related assets.
  image: https://api.ariba.com/asset-mgmt-icon.png
  humanURL: https://help.sap.com/docs/ariba-apis
  baseURL: https://openapi.ariba.com/api/asset-management
  tags:
  - Assets
  - Inventory
  - Lifecycle
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/ariba-apis
  - type: SAP Business Accelerator Hub
    url: https://api.sap.com/package/SAPAribaOpenAPIs/rest
- name: SAP Ariba Configuration Parameter Review API
  description: Reviews and manages system configuration parameters for Ariba solutions.
  image: https://api.ariba.com/config-review-icon.png
  humanURL: https://help.sap.com/docs/ariba-apis
  baseURL: https://openapi.ariba.com/api/configuration-review
  tags:
  - Administration
  - Configuration
  - Parameters
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/ariba-apis
  - type: SAP Business Accelerator Hub
    url: https://api.sap.com/package/SAPAribaOpenAPIs/rest
- name: SAP Ariba Project Document Management API
  description: Organizes and manages project-related documents within sourcing and procurement projects.
  image: https://api.ariba.com/project-docs-icon.png
  humanURL: https://help.sap.com/docs/ariba-apis
  baseURL: https://openapi.ariba.com/api/project-documents
  tags:
  - Documents
  - Management
  - Projects
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/ariba-apis
  - type: SAP Business Accelerator Hub
    url: https://api.sap.com/package/SAPAribaOpenAPIs/rest
- name: SAP Ariba Public Procurement Notices Export API
  description: Exports public procurement announcements and tender notices.
  image: https://api.ariba.com/public-notices-icon.png
  humanURL: https://help.sap.com/docs/ariba-apis
  baseURL: https://openapi.ariba.com/api/public-procurement-notices
  tags:
  - Notices
  - Public Procurement
  - Tenders
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/ariba-apis
  - type: SAP Business Accelerator Hub
    url: https://api.sap.com/package/SAPAribaOpenAPIs/rest
- name: SAP Ariba ETendering Notice Management API
  description: Manages electronic tendering announcements and notice lifecycle.
  image: https://api.ariba.com/etendering-icon.png
  humanURL: https://help.sap.com/docs/ariba-apis
  baseURL: https://openapi.ariba.com/api/etendering
  tags:
  - eTendering
  - Notices
  - Public Procurement
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/ariba-apis
  - type: SAP Business Accelerator Hub
    url: https://api.sap.com/package/SAPAribaOpenAPIs/rest
- name: SAP Ariba Discovery RFx Publication TO External Marketplace API
  description: Publishes RFx opportunities to external marketplaces for broader supplier discovery.
  image: https://api.ariba.com/discovery-to-external-icon.png
  humanURL: https://help.sap.com/docs/ariba-apis
  baseURL: https://openapi.ariba.com/api/discovery-rfx-to-external
  tags:
  - Discovery
  - Marketplace
  - RFx
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/ariba-apis
  - type: SAP Business Accelerator Hub
    url: https://api.sap.com/package/SAPAribaOpenAPIs/rest
- name: SAP Ariba Discovery RFx Publication FROM External Marketplace API
  description: Imports RFx opportunities from external marketplaces into SAP Ariba.
  image: https://api.ariba.com/discovery-from-external-icon.png
  humanURL: https://help.sap.com/docs/ariba-apis
  baseURL: https://openapi.ariba.com/api/discovery-rfx-from-external
  tags:
  - Discovery
  - Marketplace
  - RFx
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/ariba-apis
  - type: SAP Business Accelerator Hub
    url: https://api.sap.com/package/SAPAribaOpenAPIs/rest
- name: SAP Ariba Materials and BOM Tag Management API
  description: Manages tagging and classification for materials and bill of materials entries.
  image: https://api.ariba.com/materials-tag-icon.png
  humanURL: https://help.sap.com/docs/ariba-apis
  baseURL: https://openapi.ariba.com/api/materials-bom-tags
  tags:
  - BOM
  - Classification
  - Materials
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/ariba-apis
  - type: SAP Business Accelerator Hub
    url: https://api.sap.com/package/SAPAribaOpenAPIs/rest
- name: SAP Ariba Data Replication Status API
  description: Monitors data replication status across multi-ERP configurations.
  image: https://api.ariba.com/replication-status-icon.png
  humanURL: https://help.sap.com/docs/ariba-apis
  baseURL: https://openapi.ariba.com/api/data-replication-status
  tags:
  - Integration
  - Multi-ERP
  - Replication
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/ariba-apis
  - type: SAP Business Accelerator Hub
    url: https://api.sap.com/package/SAPAribaOpenAPIs/rest
- name: SAP Ariba Master Data Integration Job Status API
  description: Tracks master data synchronization job status for operational procurement.
  image: https://api.ariba.com/master-data-job-icon.png
  humanURL: https://help.sap.com/docs/ariba-apis
  baseURL: https://openapi.ariba.com/api/master-data-job-status
  tags:
  - Integration
  - Jobs
  - Master Data
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/ariba-apis
  - type: SAP Business Accelerator Hub
    url: https://api.sap.com/package/SAPAribaOpenAPIs/rest
- name: SAP Ariba Engagement Risk Assessment External Response Import API
  description: Imports external risk assessment responses for supplier engagement risk evaluation.
  image: https://api.ariba.com/risk-assessment-icon.png
  humanURL: https://help.sap.com/docs/ariba-apis
  baseURL: https://openapi.ariba.com/api/risk-assessment-import
  tags:
  - Assessments
  - Import
  - Risk Management
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/ariba-apis
  - type: SAP Business Accelerator Hub
    url: https://api.sap.com/package/SAPAribaOpenAPIs/rest
- name: SAP Ariba Finding and Event Collaboration Integration API for Supplier Risk
  description: Integrates risk findings and event collaboration for supplier risk management.
  image: https://api.ariba.com/risk-collaboration-icon.png
  humanURL: https://help.sap.com/docs/ariba-apis
  baseURL: https://openapi.ariba.com/api/risk-collaboration
  tags:
  - Collaboration
  - Findings
  - Risk Management
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/ariba-apis
  - type: SAP Business Accelerator Hub
    url: https://api.sap.com/package/SAPAribaOpenAPIs/rest
name: SAP Ariba
tags:
- B2B
- Contract Management
- Procurement
- Sourcing
- Spend Analysis
- Supplier Management
- Supply Chain
type: Contract
image: https://www.ariba.com/ariba-logo.png
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: SAP Ariba is a cloud-based procurement and supply chain collaboration platform that connects buyers and suppliers. It offers APIs for procurement, sourcing, contract management, supplier management, and spend analysis.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

