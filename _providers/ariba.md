---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 35.4
  scored_at: '2026-08-03'
api_count: 80
apis:
- description: Enables suppliers and buyers to exchange business documents and collaborate on the Ariba Network.
  name: Ariba Network API
  slug: ariba-network-api
- description: Access procurement data including requisitions, purchase orders, receipts, and payment information.
  name: Ariba Procurement API
  slug: ariba-procurement-api
- description: Manage sourcing projects, events, bids, and supplier responses for strategic sourcing activities.
  name: Ariba Sourcing API
  slug: ariba-sourcing-api
- description: Create, manage, and track contracts and contract workspaces throughout the contract lifecycle.
  name: Ariba Contracts API
  slug: ariba-contracts-api
- description: Access and manage supplier information, qualifications, performance data, and risk assessments.
  name: Ariba Supplier API
  slug: ariba-supplier-api
- description: Extract and analyze spend data, procurement metrics, and business intelligence from Ariba solutions.
  name: Ariba Analytics API
  slug: ariba-analytics-api
- description: Provides synchronous and asynchronous access to operational procurement data including requisitions, purchase orders, receipts, and invoices for reporting and analytics purposes.
  name: Operational Reporting API for Procurement
  slug: operational-reporting-api-for-procurement
- description: Enables extraction of operational sourcing data including sourcing projects, events, bids, and awards for reporting and business intelligence.
  name: Operational Reporting API for Strategic Sourcing
  slug: operational-reporting-api-for-strategic-sourcing
- description: Enables client applications to extract reportable data from reporting facts and dimensions for strategic procurement and operational procurement analytics.
  name: Analytical Reporting API for Strategic and Operational Procurement
  slug: analytical-reporting-api-for-strategic-and-operational-procurement
- description: Retrieves supplier data from SAP Ariba Supplier Lifecycle and Performance including supplier names, addresses, registration, qualification, preferred statuses, and questionnaire details with paginatio
  name: Supplier Data API with Pagination
  slug: supplier-data-api-with-pagination
- description: Provides access to supplier data from SAP Ariba Supplier Lifecycle and Performance or SAP Ariba Supplier Information and Performance Management solutions.
  name: Supplier Data API
  slug: supplier-data-api
- description: Extracts supplier information and data for integration with external systems and reporting tools.
  name: Supplier Data Extraction API
  slug: supplier-data-extraction-api
- description: Provides access to detailed supplier information including company profiles, certifications, and classifications.
  name: Supplier Information API
  slug: supplier-information-api
- description: Enables programmatic invitation of suppliers to register and participate on the SAP Ariba platform.
  name: Supplier Invite API
  slug: supplier-invite-api
- description: Manages supplier profile information on the Ariba Network including company details, capabilities, and certifications.
  name: Ariba Network Supplier Profile API
  slug: ariba-network-supplier-profile-api
- description: Enables creation and modification of procurement contract workspaces and their header information, as well as creation and retrieval of contract terms and contract requests.
  name: Contract Workspace Management APIs
  slug: contract-workspace-management-apis
- description: Retrieves contract workspace data and metadata for reporting and integration purposes.
  name: Contract Workspace Retrieval API
  slug: contract-workspace-retrieval-api
- description: Manages contract terms including creation, modification, and retrieval of contract term details within contract workspaces.
  name: Contract Terms Management API
  slug: contract-terms-management-api
- description: Provides access to contract compliance data to monitor and ensure adherence to contract terms and conditions.
  name: Contract Compliance API
  slug: contract-compliance-api
- description: Retrieves information about invoice and requisition changes and pending approvables in SAP Ariba for workflow automation.
  name: Document Approval API
  slug: document-approval-api
- description: Manages purchase order documents on the Ariba Network for buyers and suppliers including creation, retrieval, and status tracking.
  name: Ariba Network Purchase Orders API
  slug: ariba-network-purchase-orders-api
- description: Enables suppliers to manage and respond to purchase orders received through the Ariba Network.
  name: Purchase Orders Supplier API
  slug: purchase-orders-supplier-api
- description: Allows buyers to create and manage purchase order change requests on the Ariba Network.
  name: Order Change Requests API for Buyers
  slug: order-change-requests-api-for-buyers
- description: Allows suppliers to create and manage purchase order change requests on the Ariba Network.
  name: Order Change Requests API for Suppliers
  slug: order-change-requests-api-for-suppliers
- description: Extracts invoice header data from the Ariba Network for reporting, reconciliation, and integration with financial systems.
  name: Ariba Network Invoice Header Data Extraction API
  slug: ariba-network-invoice-header-data-extraction-api
- description: Enables buyers to retrieve and manage advance ship notices (ASNs) received from suppliers on the Ariba Network.
  name: Ship Notice API for Buyers
  slug: ship-notice-api-for-buyers
- description: Enables suppliers to create and manage advance ship notices (ASNs) for orders on the Ariba Network.
  name: Ship Notice API for Suppliers
  slug: ship-notice-api-for-suppliers
- description: Manages sourcing projects including creation, configuration, and lifecycle management of sourcing events.
  name: Sourcing Project Management API
  slug: sourcing-project-management-api
- description: Enables submission of surrogate bids on behalf of suppliers in sourcing events.
  name: Surrogate Bid API
  slug: surrogate-bid-api
- description: Publishes RFx events from SAP Ariba to external marketplaces for broader supplier participation.
  name: Discovery RFx Publication TO External Marketplace API
  slug: discovery-rfx-publication-to-external-marketplace-api
- description: Publishes RFx events from an external marketplace into SAP Ariba Discovery for sourcing activities.
  name: Discovery RFx Publication FROM External Marketplace API
  slug: discovery-rfx-publication-from-external-marketplace-api
- description: Integrates external approval workflows with SAP Ariba sourcing and supplier management processes.
  name: External Approval API for Sourcing and Supplier Management
  slug: external-approval-api-for-sourcing-and-supplier-management
- description: Enriches processes and documents including purchase orders, invoices, ASNs, order confirmations, and receipts in Ariba Network with external data.
  name: Flow Extension API
  slug: flow-extension-api
- description: Manages catalog content including creation, updates, and maintenance of product and service catalogs.
  name: SAP Ariba Catalog Content API
  slug: sap-ariba-catalog-content-api
- description: Enables connectivity to external catalog systems for punchout and roundtrip catalog integration.
  name: Catalog Connectivity Service API
  slug: catalog-connectivity-service-api
- description: Provides access to internal catalog shopping functionality for procurement users to browse and select items.
  name: Internal Catalogs Shop API
  slug: internal-catalogs-shop-api
- description: Provides access to public catalog shopping functionality for browsing and selecting items from public supplier catalogs.
  name: Public Catalogs Shop API
  slug: public-catalogs-shop-api
- description: Manages catalogs on the Ariba Network including catalog subscriptions, publishing, and lifecycle management.
  name: Network Catalog Management API
  slug: network-catalog-management-api
- description: Looks up content data and references within SAP Ariba for integration and validation purposes.
  name: Content Lookup API
  slug: content-lookup-api
- description: Enables programmatic creation of procurement workspaces for managing procurement projects and activities.
  name: Create Procurement Workspace API
  slug: create-procurement-workspace-api
- description: Manages dynamic lookup tables used for validation, mapping, and custom data references in procurement workflows.
  name: Dynamic Lookup Table API
  slug: dynamic-lookup-table-api
- description: Provides access to supplier risk exposure data including risk scores, assessments, and risk indicators.
  name: Risk Exposure API
  slug: risk-exposure-api
- description: Retrieves risk category information used to classify and assess supplier risk exposure levels.
  name: Risk Category Information API for Supplier Risk Exposure
  slug: risk-category-information-api-for-supplier-risk-exposure
- description: Manages supplier risk engagement processes including risk assessments and mitigation activities.
  name: Supplier Risk Engagements API
  slug: supplier-risk-engagements-api
- description: Imports external risk assessment responses into SAP Ariba for supplier risk engagement evaluations.
  name: Engagement Risk Assessment External Response Import API
  slug: engagement-risk-assessment-external-response-import-api
- description: Integrates finding and event collaboration data for supplier risk management across systems.
  name: Finding and Event Collaboration Integration API for Supplier Risk
  slug: finding-and-event-collaboration-integration-api-for-supplier-risk
- description: Extracts pricing data for product sourcing including price benchmarks and market pricing information.
  name: Pricing API for Product Sourcing Price Information
  slug: pricing-api-for-product-sourcing-price-information
- description: Provides audit trail search capabilities for tracking changes and actions across SAP Ariba processes.
  name: Audit Search API
  slug: audit-search-api
- description: Retrieves master data used in operational procurement processes including commodity codes, units of measure, and accounting information.
  name: Master Data Retrieval API for Procurement
  slug: master-data-retrieval-api-for-procurement
- description: Retrieves master data used in strategic sourcing processes including commodity codes, regions, and organizational structures.
  name: Master Data Retrieval API for Sourcing
  slug: master-data-retrieval-api-for-sourcing
- description: Monitors the status of master data integration jobs for operational procurement data synchronization.
  name: Master Data Integration Job Status API for Operational Procurement
  slug: master-data-integration-job-status-api-for-operational-procurement
- description: Enables buyers to manage proof of service documents for service-based procurement and receipt confirmations.
  name: Proof of Service API for Buyers
  slug: proof-of-service-api-for-buyers
- description: Enables suppliers to submit and manage proof of service documents for service delivery confirmation.
  name: Proof of Service API for Suppliers
  slug: proof-of-service-api-for-suppliers
- description: Manages asset-related data within SAP Ariba for tracking and maintaining procurement-related assets.
  name: Asset Management API
  slug: asset-management-api
- description: Imports bill of materials data into SAP Ariba for use in sourcing projects and procurement activities.
  name: Bill of Materials Import API
  slug: bill-of-materials-import-api
- description: Manages material classifications and bill of materials tags for organizing and categorizing procurement items.
  name: Materials and BOM Tag Management API
  slug: materials-and-bom-tag-management-api
- description: Imports item volume data into SAP Ariba for sourcing analysis and demand aggregation.
  name: Item Volume Import API
  slug: item-volume-import-api
- description: Manages product category hierarchies used for organizing and classifying procurement items and spend categories.
  name: Product Hierarchy Management API
  slug: product-hierarchy-management-api
- description: Manages user qualifications and permissions within SAP Ariba for access control and role management.
  name: User Qualification API
  slug: user-qualification-api
- description: Enables creation and management of custom forms for extending procurement and sourcing processes with additional data capture.
  name: SAP Ariba Custom Forms API
  slug: sap-ariba-custom-forms-api
- description: Implements the System for Cross-domain Identity Management standard for user provisioning and identity management in SAP Ariba.
  name: SAP Ariba SCIM API
  slug: sap-ariba-scim-api
- description: Manages events and event-driven processes within SAP Ariba for tracking procurement and sourcing activities.
  name: Event Management API
  slug: event-management-api
- description: Queries integration event data for monitoring and troubleshooting procurement integration processes.
  name: Integration Event Monitoring Query API for Procurement
  slug: integration-event-monitoring-query-api-for-procurement
- description: Monitors integration processes and data flows for procurement operations between SAP Ariba and connected systems.
  name: Integration Monitoring API for Procurement
  slug: integration-monitoring-api-for-procurement
- description: Monitors integration processes and data flows for strategic sourcing operations between SAP Ariba and connected systems.
  name: Integration Monitoring API for Strategic Sourcing
  slug: integration-monitoring-api-for-strategic-sourcing
- description: Monitors transaction processing status and details across SAP Ariba procurement and sourcing workflows.
  name: Transaction Monitoring API
  slug: transaction-monitoring-api
- description: Manages asynchronous API request jobs including submission, status tracking, and result retrieval for long-running operations.
  name: Asynchronous Requests Management API
  slug: asynchronous-requests-management-api
- description: Reviews and retrieves configuration parameters for SAP Ariba solutions to support administration and integration.
  name: Configuration Parameter Review API
  slug: configuration-parameter-review-api
- description: Monitors data replication status across multi-ERP configurations connected to SAP Ariba.
  name: Data Replication Status for Multi-ERP Configurations
  slug: data-replication-status-for-multi-erp-configurations
- description: Manages trading partner profile certifications on the Ariba Network for partner validation and compliance.
  name: Trading Partner Profile Certification API
  slug: trading-partner-profile-certification-api
- description: Extracts cost breakdown and cost analysis data from sourcing events and projects for spend visibility.
  name: Cost Breakdown Data Extraction API
  slug: cost-breakdown-data-extraction-api
- description: Exports non-disclosure agreement data from SAP Ariba for compliance tracking and legal management.
  name: NDA Data Export API
  slug: nda-data-export-api
- description: Exports public procurement notices for publishing tender opportunities to external portals and regulatory systems.
  name: Public Procurement Notices Export API
  slug: public-procurement-notices-export-api
- description: Manages functional documents within the SAP Ariba Guided Buying experience for streamlined procurement.
  name: Guided Buying Functional Documents API
  slug: guided-buying-functional-documents-api
- description: Enables buyers to manage planning collaboration processes including demand forecasts and supply plans with trading partners.
  name: Planning Collaboration Buyer API
  slug: planning-collaboration-buyer-api
- description: Enables suppliers to participate in planning collaboration processes including responding to demand forecasts and sharing supply commitments.
  name: Planning Collaboration Supplier API
  slug: planning-collaboration-supplier-api
- description: Manages project documents within SAP Ariba sourcing and procurement projects including upload, retrieval, and version control.
  name: Project Document Management API
  slug: project-document-management-api
- description: Manages electronic tendering notices for public sector and regulated procurement processes.
  name: ETendering Notice Management API
  slug: etendering-notice-management-api
- description: Provides content delivery and management for SAP Build Work Zone integration with SAP Ariba sourcing capabilities.
  name: SAP Build Work Zone CDM Content API for Sourcing
  slug: sap-build-work-zone-cdm-content-api-for-sourcing
- description: Provides content delivery and management for SAP Build Work Zone integration with SAP Ariba procurement capabilities.
  name: SAP Build Work Zone CDM Content API for Procurement
  slug: sap-build-work-zone-cdm-content-api-for-procurement
artifact_total: 107
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/ariba-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ariba-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ariba
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.ariba.com/getting-started
- group: auth
  title: ''
  type: Authentication
  url: https://developer.ariba.com/authentication
- group: start
  title: ''
  type: Console
  url: https://developer.ariba.com/console
- group: build
  title: ''
  type: SDKs
  url: https://developer.ariba.com/sdks
- group: operate
  title: ''
  type: Support
  url: https://developer.ariba.com/support
- group: operate
  title: ''
  type: StatusPage
  url: https://status.ariba.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ariba.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ariba.com/privacy
- group: operate
  title: ''
  type: RateLimits
  url: https://developer.ariba.com/rate-limits
- group: design
  title: ''
  type: Webhooks
  url: https://developer.ariba.com/webhooks
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.ariba.com/changelog
- group: other
  title: ''
  type: SAP Business Accelerator Hub
  url: https://api.sap.com/products/SAPAriba
- group: build
  title: ''
  type: SAP Ariba Open APIs Package
  url: https://api.sap.com/package/SAPAribaOpenAPIs/overview
- group: other
  title: ''
  type: SAP Ariba REST APIs
  url: https://api.sap.com/package/SAPAribaOpenAPIs/rest
- group: docs
  title: ''
  type: SAP Ariba API Documentation
  url: https://api.sap.com/package/SAPAribaOpenAPIs/documents
- group: start
  title: ''
  type: SAP Help Portal - API Reference
  url: https://help.sap.com/docs/ariba-apis
- group: start
  title: ''
  type: Developer Portal Help
  url: https://help.sap.com/docs/ariba-apis/help-for-sap-ariba-developer-portal/help-for-sap-ariba-developer-portal
- group: start
  title: ''
  type: GettingStarted
  url: https://help.sap.com/docs/ariba-apis/help-for-sap-ariba-developer-portal/sap-ariba-developer-portal-quick-start-guide-for-developers
- group: other
  title: ''
  type: SAP Ariba Web Services (SOAP)
  url: https://api.sap.com/package/SAPAribaWebServices
- group: operate
  title: ''
  type: SAP Community
  url: https://community.sap.com/t5/c-khhcw49343/SAP+Ariba+Procurement/pd-p/73554900100700001921
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/SAP-samples/ariba-extensibility-samples
- group: company
  title: ''
  type: Blog
  url: https://community.sap.com/t5/spend-management-blog-posts-by-sap/sap-ariba-api-faq-and-best-practice-on-developer-portal-and-gateway/ba-p/13512565
- group: other
  title: ''
  type: Central Invoice Management
  url: https://api.sap.com/package/CentralInvoiceManagement
- group: build
  title: ''
  type: Contracts Integration
  url: https://api.sap.com/package/SAPAribaContractsIntegration
- group: commercial
  title: ''
  type: Procurement Planning
  url: https://api.sap.com/package/ProcurementPlanning/overview
- group: agent
  title: ''
  type: LlmsText
  url: https://developer.ariba.com/llms.txt
created: '2024'
description: SAP Ariba provides cloud-based procurement and supply chain collaboration solutions. These APIs enable integration with Ariba's procurement, sourcing, contract management, and supplier management capabilities.
features:
- Cloud-based procurement and sourcing
- Supplier lifecycle and performance management
- Contract workspace and compliance management
- Ariba Network B2B document exchange
- Spend analytics and business intelligence
- Catalog management and punchout
- Risk assessment and monitoring
- Planning collaboration for supply chain
finops:
- name: Ariba Finops
  service_category: API
  slug: ariba-finops
image: https://www.ariba.com/ariba-logo.png
integrations:
- SAP S/4HANA
- SAP ERP Central Component
- SAP Business Technology Platform
- SAP Build Work Zone
- SAP Integration Suite
- Oracle ERP
- Microsoft Dynamics
- Coupa
layout: provider
modified: '2026-04-18'
name: Ariba
nav: Providers
network: true
overview: 'Ariba publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Network API, Procurement API, Sourcing API, and 3 more. Tagged areas include B2B, Catalog Management, Compliance, Contracts, and Enterprise.


  Ariba''s developer surface includes getting-started guide, authentication, developer console, support, changelog, code examples, engineering blog, and 22 more developer resources.'
plans:
- name: Ariba Plans Pricing
  plan_count: 3
  slug: ariba-plans-pricing
random_paper: 36
rate_limits:
- limit_count: 5
  name: Ariba Rate Limits
  slug: ariba-rate-limits
score:
  band: developing
  composite: 44.3
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 32.3
    developer_ergonomics: 41.3
    discoverability: 66.7
    governance: 0.0
    operational_transparency: 71.1
  previous_composite: 44.3
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ariba/refs/heads/main/screenshots/ariba-2026-06-20T172425.png
security:
- kind: domain-security
  name: Ariba Domain Security
  slug: ariba-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Ariba Vulnerability Disclosure
  slug: ariba-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: ariba
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
use_cases:
- Procurement workflow automation
- Supplier onboarding and qualification
- Contract lifecycle management
- Spend analysis and visibility
- Purchase order and invoice processing
- Strategic sourcing and e-tendering
website: https://developer.ariba.com
---
