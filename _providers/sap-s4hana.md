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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.7
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Sap S4Hana Agentic Access
  operation_count: 15
  slug: sap-s4hana-agentic-access
  summary_line: 15 operations · 6 acting
api_count: 6
apis:
- description: Operations on header and item partner functions
  name: SAP S/4HANA Partners API
  slug: sap-s4hana-partners-api
- description: Operations on header and item pricing elements
  name: SAP S/4HANA Pricing Elements API
  slug: sap-s4hana-pricing-elements-api
- description: Operations on sales order line items
  name: SAP S/4HANA Sales Order Items API
  slug: sap-s4hana-sales-order-items-api
- description: Operations on sales order header records
  name: SAP S/4HANA Sales Orders API
  slug: sap-s4hana-sales-orders-api
- description: Operations on item schedule lines for delivery scheduling
  name: SAP S/4HANA Schedule Lines API
  slug: sap-s4hana-schedule-lines-api
- description: Operations on header and item text records
  name: SAP S/4HANA Text API
  slug: sap-s4hana-text-api
artifact_total: 96
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: SAP S/4HANA Sales Order Partners API
  slug: open-sap-s4hana-partners-api
- collection_type: open
  name: SAP S/4HANA Sales Order Partners Pricing Elements API
  slug: open-sap-s4hana-pricing-elements-api
- collection_type: open
  name: SAP S/4HANA Sales Order Partners Sales Order Items API
  slug: open-sap-s4hana-sales-order-items-api
- collection_type: open
  name: SAP S/4HANA Sales Order API
  slug: open-sap-s4hana-sales-order
- collection_type: open
  name: SAP S/4HANA Sales Order Partners Sales Orders API
  slug: open-sap-s4hana-sales-orders-api
- collection_type: open
  name: SAP S/4HANA Sales Order Partners Schedule Lines API
  slug: open-sap-s4hana-schedule-lines-api
- collection_type: open
  name: SAP S/4HANA Sales Order Partners Text API
  slug: open-sap-s4hana-text-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/sap-s4hana-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/sap-s4hana-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sap-s4hana-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/sap-s4hana-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/sap-s4hana-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/SAP
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/showcase/sap-s-4hana
- group: start
  title: ''
  type: Portal
  url: https://api.sap.com
- group: start
  title: ''
  type: GettingStarted
  url: https://help.sap.com/docs/SAP_S4HANA_CLOUD/0f69f8fb28ac4bf48d2b57b9637e81fa/1e45cfd73e814aa6b1a1118e2c1d3cec.html
- group: auth
  title: ''
  type: Authentication
  url: https://help.sap.com/docs/SAP_S4HANA_CLOUD/0f69f8fb28ac4bf48d2b57b9637e81fa/26f2b5aa3f3a4019b7d08978095b9e6a.html
- group: operate
  title: ''
  type: ChangeLog
  url: https://api.sap.com/releasenotes
- group: operate
  title: ''
  type: Support
  url: https://support.sap.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.sap.com/about/trust-center/agreements/cloud/cloud-services.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.sap.com/about/legal/privacy.html
- group: other
  title: ''
  type: API Catalog
  url: https://api.sap.com/products/SAPS4HANACloud/apis/all
- group: build
  title: ''
  type: API Packages
  url: https://api.sap.com/products/SAPS4HANACloud/apis/packages
- group: other
  title: ''
  type: OData V4 APIs
  url: https://api.sap.com/products/SAPS4HANACloud/apis/ODATAV4
- group: other
  title: ''
  type: REST APIs
  url: https://api.sap.com/products/SAPS4HANACloud/apis/REST
- group: other
  title: ''
  type: On-Premise API Catalog
  url: https://api.sap.com/products/SAPS4HANA/apis/all
- group: build
  title: ''
  type: On-Premise API Packages
  url: https://api.sap.com/products/SAPS4HANA/apis/packages
- group: other
  title: ''
  type: Private Edition APIs
  url: https://api.sap.com/products/SAPS4HANACloudPrivateEdition/apis/packages
- group: operate
  title: ''
  type: Community
  url: https://community.sap.com/t5/enterprise-resource-planning-blog-posts-by-sap/sap-s-4hana-apis-and-where-to-find-them/ba-p/13723939
- group: operate
  title: ''
  type: StatusPage
  url: https://www.sap.com/about/cloud-trust-center/cloud-service-status.html
created: '2024-01-15'
description: Collection of SAP S/4HANA Cloud and On-Premise APIs for enterprise resource planning.
examples:
- key_count: 1
  name: Sap S4Hana Sales Order O Data Error Example
  slug: sap-s4hana-sales-order-o-data-error-example
- key_count: 20
  name: Sap S4Hana Sales Order Sales Order Create Example
  slug: sap-s4hana-sales-order-sales-order-create-example
- key_count: 59
  name: Sap S4Hana Sales Order Sales Order Example
  slug: sap-s4hana-sales-order-sales-order-example
- key_count: 6
  name: Sap S4Hana Sales Order Sales Order Header Partner Example
  slug: sap-s4hana-sales-order-sales-order-header-partner-example
- key_count: 29
  name: Sap S4Hana Sales Order Sales Order Header Prcg Elmnt Example
  slug: sap-s4hana-sales-order-sales-order-header-prcg-elmnt-example
- key_count: 20
  name: Sap S4Hana Sales Order Sales Order Item Create Example
  slug: sap-s4hana-sales-order-sales-order-item-create-example
- key_count: 55
  name: Sap S4Hana Sales Order Sales Order Item Example
  slug: sap-s4hana-sales-order-sales-order-item-example
- key_count: 5
  name: Sap S4Hana Sales Order Sales Order Item Partner Example
  slug: sap-s4hana-sales-order-sales-order-item-partner-example
- key_count: 19
  name: Sap S4Hana Sales Order Sales Order Item Prcg Elmnt Example
  slug: sap-s4hana-sales-order-sales-order-item-prcg-elmnt-example
- key_count: 5
  name: Sap S4Hana Sales Order Sales Order Item Text Example
  slug: sap-s4hana-sales-order-sales-order-item-text-example
- key_count: 11
  name: Sap S4Hana Sales Order Sales Order Item Update Example
  slug: sap-s4hana-sales-order-sales-order-item-update-example
- key_count: 13
  name: Sap S4Hana Sales Order Sales Order Schedule Line Example
  slug: sap-s4hana-sales-order-sales-order-schedule-line-example
- key_count: 4
  name: Sap S4Hana Sales Order Sales Order Text Example
  slug: sap-s4hana-sales-order-sales-order-text-example
- key_count: 11
  name: Sap S4Hana Sales Order Sales Order Update Example
  slug: sap-s4hana-sales-order-sales-order-update-example
features:
- description: RESTful APIs following OData protocol for standardized CRUD operations and query capabilities.
  name: OData V2 and V4 APIs
- description: Create complex documents with header and dependent entities in a single API request.
  name: Deep Insert
- description: ETag-based concurrency control to prevent conflicting updates to business documents.
  name: Optimistic Concurrency
- description: Synchronous API access to live ERP data for real-time business process integration.
  name: Real-Time Integration
- description: APIs spanning finance, sales, procurement, logistics, manufacturing, and HR modules.
  name: Multi-Module Coverage
finops:
- name: Sap S4Hana Finops
  service_category: ERP
  slug: sap-s4hana-finops
image: https://www.sap.com/dam/application/shared/logos/sap-logo.svg
integrations:
- description: Native integration with SAP BTP for extensions, analytics, and AI/ML capabilities.
  name: SAP Business Technology Platform
- description: Pre-built integration flows for connecting S/4HANA with third-party applications.
  name: SAP Integration Suite
- description: Integration with Excel and Outlook for business data analysis and communication workflows.
  name: Microsoft Office
json_schemas:
- name: ODataError
  property_count: 1
  slug: sap-s4hana-odataerror
- name: ODataError
  property_count: 1
  slug: sap-s4hana-sales-order-o-data-error
- name: SalesOrderCreate
  property_count: 20
  slug: sap-s4hana-sales-order-sales-order-create
- name: SalesOrderHeaderPartner
  property_count: 6
  slug: sap-s4hana-sales-order-sales-order-header-partner
- name: SalesOrderHeaderPrcgElmnt
  property_count: 29
  slug: sap-s4hana-sales-order-sales-order-header-prcg-elmnt
- name: SalesOrderItemCreate
  property_count: 20
  slug: sap-s4hana-sales-order-sales-order-item-create
- name: SalesOrderItemPartner
  property_count: 5
  slug: sap-s4hana-sales-order-sales-order-item-partner
- name: SalesOrderItemPrcgElmnt
  property_count: 19
  slug: sap-s4hana-sales-order-sales-order-item-prcg-elmnt
- name: SalesOrderItem
  property_count: 55
  slug: sap-s4hana-sales-order-sales-order-item
- name: SalesOrderItemText
  property_count: 5
  slug: sap-s4hana-sales-order-sales-order-item-text
- name: SalesOrderItemUpdate
  property_count: 11
  slug: sap-s4hana-sales-order-sales-order-item-update
- name: SalesOrderScheduleLine
  property_count: 13
  slug: sap-s4hana-sales-order-sales-order-schedule-line
- name: SalesOrder
  property_count: 59
  slug: sap-s4hana-sales-order-sales-order
- name: SalesOrderText
  property_count: 4
  slug: sap-s4hana-sales-order-sales-order-text
- name: SalesOrderUpdate
  property_count: 11
  slug: sap-s4hana-sales-order-sales-order-update
- name: SAP S/4HANA Sales Order
  property_count: 1
  slug: sap-s4hana-sales-order
- name: SalesOrder
  property_count: 59
  slug: sap-s4hana-salesorder
- name: SalesOrderCreate
  property_count: 20
  slug: sap-s4hana-salesordercreate
- name: SalesOrderHeaderPartner
  property_count: 6
  slug: sap-s4hana-salesorderheaderpartner
- name: SalesOrderHeaderPrcgElmnt
  property_count: 29
  slug: sap-s4hana-salesorderheaderprcgelmnt
- name: SalesOrderItem
  property_count: 55
  slug: sap-s4hana-salesorderitem
- name: SalesOrderItemCreate
  property_count: 20
  slug: sap-s4hana-salesorderitemcreate
- name: SalesOrderItemPartner
  property_count: 5
  slug: sap-s4hana-salesorderitempartner
- name: SalesOrderItemPrcgElmnt
  property_count: 19
  slug: sap-s4hana-salesorderitemprcgelmnt
- name: SalesOrderItemText
  property_count: 5
  slug: sap-s4hana-salesorderitemtext
- name: SalesOrderItemUpdate
  property_count: 11
  slug: sap-s4hana-salesorderitemupdate
- name: SalesOrderScheduleLine
  property_count: 13
  slug: sap-s4hana-salesorderscheduleline
- name: SalesOrderText
  property_count: 4
  slug: sap-s4hana-salesordertext
- name: SalesOrderUpdate
  property_count: 11
  slug: sap-s4hana-salesorderupdate
json_structures:
- name: Sap S4Hana Sales Order O Data Error Structure
  property_count: 1
  slug: sap-s4hana-sales-order-o-data-error-structure
- name: Sap S4Hana Sales Order Sales Order Create Structure
  property_count: 20
  slug: sap-s4hana-sales-order-sales-order-create-structure
- name: Sap S4Hana Sales Order Sales Order Header Partner Structure
  property_count: 6
  slug: sap-s4hana-sales-order-sales-order-header-partner-structure
- name: Sap S4Hana Sales Order Sales Order Header Prcg Elmnt Structure
  property_count: 29
  slug: sap-s4hana-sales-order-sales-order-header-prcg-elmnt-structure
- name: Sap S4Hana Sales Order Sales Order Item Create Structure
  property_count: 20
  slug: sap-s4hana-sales-order-sales-order-item-create-structure
- name: Sap S4Hana Sales Order Sales Order Item Partner Structure
  property_count: 5
  slug: sap-s4hana-sales-order-sales-order-item-partner-structure
- name: Sap S4Hana Sales Order Sales Order Item Prcg Elmnt Structure
  property_count: 19
  slug: sap-s4hana-sales-order-sales-order-item-prcg-elmnt-structure
- name: Sap S4Hana Sales Order Sales Order Item Structure
  property_count: 55
  slug: sap-s4hana-sales-order-sales-order-item-structure
- name: Sap S4Hana Sales Order Sales Order Item Text Structure
  property_count: 5
  slug: sap-s4hana-sales-order-sales-order-item-text-structure
- name: Sap S4Hana Sales Order Sales Order Item Update Structure
  property_count: 11
  slug: sap-s4hana-sales-order-sales-order-item-update-structure
- name: Sap S4Hana Sales Order Sales Order Schedule Line Structure
  property_count: 13
  slug: sap-s4hana-sales-order-sales-order-schedule-line-structure
- name: Sap S4Hana Sales Order Sales Order Structure
  property_count: 59
  slug: sap-s4hana-sales-order-sales-order-structure
- name: Sap S4Hana Sales Order Sales Order Text Structure
  property_count: 4
  slug: sap-s4hana-sales-order-sales-order-text-structure
- name: Sap S4Hana Sales Order Sales Order Update Structure
  property_count: 11
  slug: sap-s4hana-sales-order-sales-order-update-structure
- name: Sap S4Hana Structure
  property_count: 0
  slug: sap-s4hana-structure
jsonld:
- class_count: 10
  name: Sap S4Hana Context
  property_count: 14
  slug: sap-s4hana-context
- class_count: 0
  name: Sap S4Hana Sales Order Context
  property_count: 0
  slug: sap-s4hana-sales-order-context
layout: provider
modified: '2026-05-19'
name: SAP S/4HANA
nav: Providers
network: true
overview: 'SAP S/4HANA publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Partners API, Pricing Elements API, Sales Order Items API, and 3 more. Tagged areas include Business Applications, Cloud, Enterprise Resource Planning, ERP, and Finance.


  The SAP S/4HANA catalog on APIs.io includes 2 JSON-LD contexts and 2 Spectral governance rulesets.


  SAP S/4HANA''s developer surface includes authentication, developer portal, getting-started guide, changelog, support, and 18 more developer resources.'
plans:
- name: Sap S4Hana Plans Pricing
  plan_count: 1
  slug: sap-s4hana-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 1
  name: Sap S4Hana Rate Limits
  slug: sap-s4hana-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: SAP S/4HANA API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: sap-s4hana-jsonschema-spectral-rules
- effective_rule_count: 58
  extends:
  - spectral:oas
  name: SAP S/4HANA API Rules
  rule_count: 17
  severity_counts:
    error: 8
    hint: 0
    info: 0
    warn: 9
  slug: sap-s4hana-spectral-rules
scopes:
- name: Sap S4Hana Scopes
  scope_count: 1
  slug: sap-s4hana-scopes
  summary_line: 1 scope · clientCredentials
score:
  band: thin
  composite: 39.1
  delta: 1.9
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 13.6
    contract_quality: 72.1
    developer_ergonomics: 23.8
    discoverability: 48.1
    governance: 13.6
    operational_transparency: 23.7
  previous_composite: 37.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sap-s4hana/refs/heads/main/screenshots/sap-s4hana-2026-06-20T193430.png
security:
- kind: authentication
  name: Sap S4Hana Authentication
  slug: sap-s4hana-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Sap S4Hana Domain Security
  slug: sap-s4hana-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Sap S4Hana Vulnerability Disclosure
  slug: sap-s4hana-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: sap-s4hana
tags:
- Business Applications
- Cloud
- Enterprise Resource Planning
- ERP
- Finance
- Human Resources
- Inventory
- Logistics
- Manufacturing
- Plant Maintenance
- Procurement
- S/4HANA
- Sales
- SAP
use_cases:
- description: Automate the sales process from sales order creation through delivery and billing.
  name: Order-to-Cash
- description: Streamline procurement from purchase requisition through purchase order, receipt, and invoice.
  name: Procure-to-Pay
- description: Automate journal entries, cost center reporting, and GL account management for period close.
  name: Financial Close
- description: Track inbound and outbound deliveries, inventory movements, and material documents in real time.
  name: Supply Chain Visibility
website: https://api.sap.com
---
