---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - '{''url'': ''https://www.ariba.com/'', ''status'': 301, ''note'': ''declared website redirects to https://www.sap.com/products/spend-management.html?src=ariba — a different registrable domain (ariba.com -> sap.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
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
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.4
  scored_at: '2026-09-05'
api_count: 74
apis:
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
artifact_total: 81
asyncapis:
- description: ''
  name: Ariba Event Surface
  slug: ariba-event-surface
common:
- group: company
  title: ''
  type: Website
  url: https://www.ariba.com/
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
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.ariba.com/api/home
- group: docs
  title: ''
  type: Documentation
  url: https://help.sap.com/docs/ariba-apis
- group: docs
  title: ''
  type: APIReference
  url: https://api.sap.com/package/SAPAribaOpenAPIs/overview
- group: operate
  title: ''
  type: Support
  url: https://help.ariba.com/
- group: start
  title: ''
  type: SignUp
  url: https://developer.ariba.com/api/registration
- group: start
  title: ''
  type: Login
  url: https://developer.ariba.com/api/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developer.ariba.com/api/termsofuse
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://developer.ariba.com/api/privacystatement
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/SAP-samples
- group: agent
  title: ''
  type: WellKnown
  url: well-known/ariba-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/ariba-security.txt
- group: auth
  title: ''
  type: Security
  url: security/ariba-vulnerability-disclosure.yml
- group: build
  title: ''
  type: Packages
  url: packages/ariba-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ariba-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/ariba-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/ariba-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/ariba-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/ariba-lifecycle.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ariba-authentication.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/ariba-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/ariba-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/ariba-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/ariba-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/ariba-event-surface.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/ariba-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/ariba-rate-limits.yml
- group: other
  title: ''
  type: WebServiceCatalog
  url: wsdl/ariba-soap-services.yml
- group: other
  title: ''
  type: ProviderAPIInventory
  url: catalog/ariba-api-catalog.yml
created: '2024-01-01'
description: 'SAP Ariba is the procurement and supply-chain collaboration business of SAP: strategic sourcing, contract management, procure-to-pay, supplier lifecycle and performance, supplier risk, catalog management, and the SAP Business Network that connects buyers and suppliers. Its API surface is one of the largest enterprise contract estates in the catalog - 114 REST APIs published in the SAP Business Accelerator Hub package SAPAribaOpenAPIs, plus 144 SOAP web services - all routed through the openapi.ariba.com gateway behind OAuth 2.0 client credentials, an application key, and a per-realm authorization grant. Ariba also authored cXML, the Commerce XML interchange standard the wider procurement market still runs on. The catalog metadata is anonymously readable; the specifications themselves are not - every OpenAPI download redirects to an SAP ID login.'
finops:
- name: Ariba Finops
  service_category: API
  slug: ariba-finops
layout: provider
modified: '2026-08-29'
name: Ariba
nav: Providers
network: true
overview: 'Ariba publishes 74 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include B2B, Catalog Management, Compliance, Contracts, and Enterprise.


  The Ariba catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Ariba''s developer surface includes getting-started guide, code examples, engineering blog, documentation, API reference, support, signup flow, and 39 more developer resources.'
plans:
- name: Ariba Plans Pricing
  plan_count: 0
  slug: ariba-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 11
  name: Ariba Rate Limits
  slug: ariba-rate-limits
score:
  band: developing
  composite: 39.3
  coverage:
    artifact_dirs: 21
    catalog_earned: 45.0
    catalog_earned_first_party: 12.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 14.5
    commercial_clarity: 14.5
    contract_governance: 18.2
    contract_quality: 48.1
    developer_ergonomics: 26.2
    discoverability: 70.4
    governance: 18.2
    operational_transparency: 76.3
  previous_composite: 39.3
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ariba/refs/heads/main/screenshots/ariba-2026-06-20T172425.png
security:
- kind: authentication
  name: Ariba Authentication
  slug: ariba-authentication
  summary_line: 4 schemes
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
website: https://www.ariba.com/
---
