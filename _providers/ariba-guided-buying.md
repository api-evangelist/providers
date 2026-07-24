---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: true
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 54.8
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Ariba Guided Buying Agentic Access
  operation_count: 6
  slug: ariba-guided-buying-agentic-access
  summary_line: 6 operations · 1 acting
api_count: 2
apis:
- description: Asset requisition retrieval and update operations
  name: Ariba Guided Buying Requisitions API
  slug: ariba-guided-buying-requisitions-api
- description: Catalog shop search and retrieval operations
  name: Ariba Guided Buying Shops API
  slug: ariba-guided-buying-shops-api
arazzos:
- description: Find an in-progress asset requisition and assign a unique asset number to its line item.
  name: Ariba Guided Buying Assign Asset Numbers
  slug: ariba-guided-buying-assign-asset-numbers-workflow
- description: Open a shop, get a typeahead suggestion, then list the matching catalog items.
  name: Ariba Guided Buying Browse Shop Catalog
  slug: ariba-guided-buying-browse-shop-catalog-workflow
- description: Find a catalog item, locate an in-progress asset requisition, and assign an asset number.
  name: Ariba Guided Buying Catalog To Asset Assignment
  slug: ariba-guided-buying-catalog-to-asset-assignment-workflow
- description: Assign an asset number to an in-progress requisition, then re-count the remaining backlog.
  name: Ariba Guided Buying Complete And Verify Requisitions
  slug: ariba-guided-buying-complete-and-verify-requisitions-workflow
- description: Count then page through the in-progress asset requisitions in the Asset Workbench.
  name: Ariba Guided Buying Inventory Asset Requisitions
  slug: ariba-guided-buying-inventory-asset-requisitions-workflow
- description: Search a shop with items and facets expanded, then refine the item list by a search term.
  name: Ariba Guided Buying Search Shop With Facets
  slug: ariba-guided-buying-search-shop-with-facets-workflow
- description: Turn a partial search term into a suggestion, then list matching catalog items.
  name: Ariba Guided Buying Typeahead Catalog Search
  slug: ariba-guided-buying-typeahead-catalog-search-workflow
artifact_total: 76
collections:
- collection_type: postman
  name: Ariba Guided Buying - Asset Management API
  slug: postman-ariba-guided-buying-asset-management-api
- collection_type: postman
  name: Ariba Guided Buying - Public Catalogs Shop API
  slug: postman-ariba-guided-buying-catalog-shop-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/ariba-guided-buying-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/ariba-guided-buying-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ariba-guided-buying-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ariba-guided-buying-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/ariba-guided-buying-scopes.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/ariba-guided-buying/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/ariba-guided-buying-assign-asset-numbers-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/ariba-guided-buying-browse-shop-catalog-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/ariba-guided-buying-catalog-to-asset-assignment-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/ariba-guided-buying-complete-and-verify-requisitions-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/ariba-guided-buying-inventory-asset-requisitions-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/ariba-guided-buying-search-shop-with-facets-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/ariba-guided-buying-typeahead-catalog-search-workflow.yml
- group: company
  title: ''
  type: Website
  url: https://www.sap.com/products/spend-management/guided-buying.html
- group: docs
  title: ''
  type: Documentation
  url: https://help.sap.com/docs/ariba-apis
- group: start
  title: ''
  type: GettingStarted
  url: https://help.sap.com/docs/ariba-apis/help-for-sap-ariba-developer-portal/sap-ariba-developer-portal-quick-start-guide-for-developers
- group: start
  title: ''
  type: Portal
  url: https://developer.ariba.com
- group: auth
  title: ''
  type: Authentication
  url: https://help.sap.com/docs/ariba-apis/help-for-sap-ariba-developer-portal/sap-ariba-developer-portal-authentication
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.sap.com/corporate/en/legal/terms-of-use.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.sap.com/about/legal/privacy.html
- group: operate
  title: ''
  type: Support
  url: https://help.sap.com/ariba
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/SAP-samples
- group: build
  title: SAP Ariba Extensibility Samples
  type: CodeExamples
  url: https://github.com/SAP-samples/ariba-extensibility-samples
- group: design
  title: ''
  type: SpectralRules
  url: rules/ariba-guided-buying-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/ariba-guided-buying-vocabulary.yaml
- group: agent
  title: ''
  type: LlmsText
  url: https://developer.ariba.com/llms.txt
created: '2024-01-01'
description: SAP Ariba Guided Buying provides a consumer-like shopping experience for enterprise procurement, enabling employees to find and purchase goods and services through an intuitive catalog-driven interface with built-in approval workflows and policy compliance.
examples:
- key_count: 5
  name: Asset Management Api Asset Line Item Example
  slug: asset-management-api-asset-line-item-example
- key_count: 3
  name: Asset Management Api Asset Line Item Update Example
  slug: asset-management-api-asset-line-item-update-example
- key_count: 1
  name: Asset Management Api Batch Asset Update Request Example
  slug: asset-management-api-batch-asset-update-request-example
- key_count: 3
  name: Asset Management Api Batch Update Response Example
  slug: asset-management-api-batch-update-response-example
- key_count: 1
  name: Asset Management Api Count Response Example
  slug: asset-management-api-count-response-example
- key_count: 6
  name: Asset Management Api Requisition Example
  slug: asset-management-api-requisition-example
- key_count: 2
  name: Asset Management Api Requisitions Response Example
  slug: asset-management-api-requisitions-response-example
- key_count: 1
  name: Catalog Shop Api Auto Complete Response Example
  slug: catalog-shop-api-auto-complete-response-example
- key_count: 8
  name: Catalog Shop Api Catalog Item Example
  slug: catalog-shop-api-catalog-item-example
- key_count: 2
  name: Catalog Shop Api Facet Example
  slug: catalog-shop-api-facet-example
- key_count: 2
  name: Catalog Shop Api Facet Value Example
  slug: catalog-shop-api-facet-value-example
- key_count: 1
  name: Catalog Shop Api Items Response Example
  slug: catalog-shop-api-items-response-example
- key_count: 3
  name: Catalog Shop Api Shop Response Example
  slug: catalog-shop-api-shop-response-example
features:
- description: Provides employees with an intuitive catalog-driven shopping interface similar to consumer e-commerce applications.
  name: Consumer-Like Shopping Experience
- description: Full-text search with typeahead autocomplete for finding catalog items from suppliers on SAP Business Network.
  name: Catalog Search and Typeahead
- description: Built-in procurement policy checks ensure purchases comply with organizational spending rules and approval workflows.
  name: Policy Compliance Enforcement
- description: Integrates with SAP ERP asset management to assign and track asset numbers on requisition line items.
  name: Asset Management Integration
- description: Secure API access using OAuth 2.0 client credentials flow with per-API credentials.
  name: OAuth 2.0 Authentication
- description: Retrieves filter facets alongside catalog items enabling refined product browsing and discovery.
  name: Faceted Search
finops:
- name: Ariba Guided Buying Finops
  service_category: API
  slug: ariba-guided-buying-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ariba-guided-buying.png
integrations:
- description: Integrates with SAP S/4HANA Cloud Public Edition for purchase request creation and order management.
  name: SAP S/4HANA Cloud
- description: Connects to SAP Business Network to access public supplier catalogs and pricing.
  name: SAP Business Network
- description: Integrates with SAP ERP systems for asset management and purchase order creation.
  name: SAP ERP
- description: Extends SAP Ariba functionality through SAP Integration Suite for custom workflows and data transformations.
  name: SAP Integration Suite
json_schemas:
- name: AssetLineItem
  property_count: 5
  slug: asset-management-api-asset-line-item
- name: AssetLineItemUpdate
  property_count: 3
  slug: asset-management-api-asset-line-item-update
- name: BatchAssetUpdateRequest
  property_count: 1
  slug: asset-management-api-batch-asset-update-request
- name: BatchUpdateResponse
  property_count: 3
  slug: asset-management-api-batch-update-response
- name: CountResponse
  property_count: 1
  slug: asset-management-api-count-response
- name: Requisition
  property_count: 6
  slug: asset-management-api-requisition
- name: RequisitionsResponse
  property_count: 2
  slug: asset-management-api-requisitions-response
- name: AutoCompleteResponse
  property_count: 1
  slug: catalog-shop-api-auto-complete-response
- name: CatalogItem
  property_count: 8
  slug: catalog-shop-api-catalog-item
- name: Facet
  property_count: 2
  slug: catalog-shop-api-facet
- name: FacetValue
  property_count: 2
  slug: catalog-shop-api-facet-value
- name: ItemsResponse
  property_count: 1
  slug: catalog-shop-api-items-response
- name: ShopResponse
  property_count: 3
  slug: catalog-shop-api-shop-response
json_structures:
- name: Asset Management Api Asset Line Item Structure
  property_count: 5
  slug: asset-management-api-asset-line-item-structure
- name: Asset Management Api Asset Line Item Update Structure
  property_count: 3
  slug: asset-management-api-asset-line-item-update-structure
- name: Asset Management Api Batch Asset Update Request Structure
  property_count: 1
  slug: asset-management-api-batch-asset-update-request-structure
- name: Asset Management Api Batch Update Response Structure
  property_count: 3
  slug: asset-management-api-batch-update-response-structure
- name: Asset Management Api Count Response Structure
  property_count: 1
  slug: asset-management-api-count-response-structure
- name: Asset Management Api Requisition Structure
  property_count: 6
  slug: asset-management-api-requisition-structure
- name: Asset Management Api Requisitions Response Structure
  property_count: 2
  slug: asset-management-api-requisitions-response-structure
- name: Catalog Shop Api Auto Complete Response Structure
  property_count: 1
  slug: catalog-shop-api-auto-complete-response-structure
- name: Catalog Shop Api Catalog Item Structure
  property_count: 8
  slug: catalog-shop-api-catalog-item-structure
- name: Catalog Shop Api Facet Structure
  property_count: 2
  slug: catalog-shop-api-facet-structure
- name: Catalog Shop Api Facet Value Structure
  property_count: 2
  slug: catalog-shop-api-facet-value-structure
- name: Catalog Shop Api Items Response Structure
  property_count: 1
  slug: catalog-shop-api-items-response-structure
- name: Catalog Shop Api Shop Response Structure
  property_count: 3
  slug: catalog-shop-api-shop-response-structure
jsonld:
- class_count: 8
  name: Ariba Guided Buying Asset Management Api Context
  property_count: 17
  slug: ariba-guided-buying-asset-management-api-context
- class_count: 7
  name: Ariba Guided Buying Catalog Shop Api Context
  property_count: 15
  slug: ariba-guided-buying-catalog-shop-api-context
layout: provider
modified: '2026-05-19'
name: Ariba Guided Buying
nav: Providers
network: true
overview: 'Ariba Guided Buying publishes 2 APIs on the [APIs.io](https://apis.io/) network: Requisitions API and Shops API. Tagged areas include B2B, Catalog, ERP, Procurement, and Requisitions.


  The Ariba Guided Buying catalog on APIs.io includes 2 JSON-LD contexts and 2 Spectral governance rulesets.


  Ariba Guided Buying''s developer surface includes authentication, documentation, getting-started guide, developer portal, support, code examples, and 20 more developer resources.'
plans:
- name: Ariba Guided Buying Plans Pricing
  plan_count: 3
  slug: ariba-guided-buying-plans-pricing
random_paper: 45
rate_limits:
- limit_count: 5
  name: Ariba Guided Buying Rate Limits
  slug: ariba-guided-buying-rate-limits
rules:
- name: Ariba Guided Buying API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: ariba-guided-buying-jsonschema-spectral-rules
- name: Ariba Guided Buying API Rules
  rule_count: 39
  severity_counts:
    error: 16
    hint: 0
    info: 4
    warn: 19
  slug: ariba-guided-buying-spectral-rules
scopes:
- name: Ariba Guided Buying Scopes
  scope_count: 0
  slug: ariba-guided-buying-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 60.8
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 71.7
    developer_ergonomics: 47.8
    discoverability: 60.0
    governance: 86.8
    operational_transparency: 36.8
  previous_composite: 60.8
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Ariba Guided Buying Authentication
  slug: ariba-guided-buying-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Ariba Guided Buying Domain Security
  slug: ariba-guided-buying-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Ariba Guided Buying Vulnerability Disclosure
  slug: ariba-guided-buying-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: ariba-guided-buying
tags:
- B2B
- Catalog
- ERP
- Procurement
- Requisitions
- SAP
- Supply Chain
use_cases:
- description: Enable employees to browse and purchase approved goods from supplier catalogs without manual procurement processes.
  name: Employee Self-Service Procurement
- description: Import asset records from SAP ERP and assign unique asset values to line items on approved requisitions.
  name: ERP Asset Record Import
- description: Integrate SAP Ariba Buying with SAP S/4HANA Cloud Public Edition to access public supplier catalogs on SAP Business Network.
  name: Catalog Integration
- description: Automate retrieval and processing of asset-based requisitions through the Asset Workbench workflow.
  name: Requisition Automation
website: https://www.sap.com/products/spend-management/guided-buying.html
---
