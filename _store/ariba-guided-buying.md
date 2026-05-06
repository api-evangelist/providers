---
aid: ariba-guided-buying
name: Ariba Guided Buying
description: SAP Ariba Guided Buying provides a consumer-like shopping experience for enterprise procurement, enabling employees to find and purchase goods and services through an intuitive catalog-driven interface with built-in approval workflows and policy compliance.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - B2B
  - Catalog
  - ERP
  - Procurement
  - Requisitions
  - SAP
  - Supply Chain
url: https://raw.githubusercontent.com/api-evangelist/ariba-guided-buying/refs/heads/main/apis.yml
created: '2024-01-01'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: ariba-guided-buying:ariba-guided-buying-catalog-shop-api
    name: Ariba Guided Buying - Public Catalogs Shop API
    description: The Public Catalogs Shop API enables applications to retrieve data related to catalog items, filter facets, and matching search suggestions from public catalogs on SAP Business Network. This API supports SAP Ariba Buying, base edition, integrated with SAP S/4HANA Cloud Public Edition.
    humanURL: https://help.sap.com/docs/ariba-apis
    baseURL: https://openapi.ariba.com/api/catalog-shop/v1/prod
    tags:
      - Catalog
      - Procurement
      - Shopping
    properties:
      - type: Documentation
        url: https://help.sap.com/doc/f2393ece78554efab2087b984c6fa90b/cloud/en-US/5e12bd6c87f24e0781a5fcdfb410ddc6.pdf
      - type: OpenAPI
        url: openapi/ariba-guided-buying-catalog-shop-api.yaml
      - type: JSONSchema
        url: json-schema/catalog-shop-api-shop-response-schema.json
      - type: JSONSchema
        url: json-schema/catalog-shop-api-catalog-item-schema.json
      - type: JSONSchema
        url: json-schema/catalog-shop-api-facet-schema.json
      - type: JSONSchema
        url: json-schema/catalog-shop-api-items-response-schema.json
      - type: JSONSchema
        url: json-schema/catalog-shop-api-auto-complete-response-schema.json
      - type: JSONStructure
        url: json-structure/catalog-shop-api-shop-response-structure.json
      - type: JSONStructure
        url: json-structure/catalog-shop-api-catalog-item-structure.json
      - type: JSON-LD
        url: json-ld/ariba-guided-buying-catalog-shop-api-context.jsonld
  - aid: ariba-guided-buying:ariba-guided-buying-asset-management-api
    name: Ariba Guided Buying - Asset Management API
    description: The Asset Management API enables developers to retrieve purchase requisitions consisting of asset items and update asset data on those requisitions. This API is applicable for SAP ERP-integrated sites that have enabled the asset management feature.
    humanURL: https://help.sap.com/docs/ariba-apis
    baseURL: https://openapi.ariba.com/api/asset-management/v1/prod
    tags:
      - Asset Management
      - ERP
      - Procurement
      - Requisitions
    properties:
      - type: Documentation
        url: https://help.sap.com/doc/16e046861d874557a33a1831b778d998/cloud/en-US/45d3c37cf5a643c38b9e26cc31c97470.pdf
      - type: OpenAPI
        url: openapi/ariba-guided-buying-asset-management-api.yaml
      - type: JSONSchema
        url: json-schema/asset-management-api-requisition-schema.json
      - type: JSONSchema
        url: json-schema/asset-management-api-asset-line-item-schema.json
      - type: JSONSchema
        url: json-schema/asset-management-api-batch-asset-update-request-schema.json
      - type: JSONStructure
        url: json-structure/asset-management-api-requisition-structure.json
      - type: JSONStructure
        url: json-structure/asset-management-api-asset-line-item-structure.json
      - type: JSON-LD
        url: json-ld/ariba-guided-buying-asset-management-api-context.jsonld
common:
  - type: Website
    url: https://www.sap.com/products/spend-management/guided-buying.html
  - type: Documentation
    url: https://help.sap.com/docs/ariba-apis
  - type: GettingStarted
    url: https://help.sap.com/docs/ariba-apis/help-for-sap-ariba-developer-portal/sap-ariba-developer-portal-quick-start-guide-for-developers
  - type: Portal
    url: https://developer.ariba.com
  - type: Authentication
    url: https://help.sap.com/docs/ariba-apis/help-for-sap-ariba-developer-portal/sap-ariba-developer-portal-authentication
  - type: TermsOfService
    url: https://www.sap.com/corporate/en/legal/terms-of-use.html
  - type: PrivacyPolicy
    url: https://www.sap.com/about/legal/privacy.html
  - type: Support
    url: https://help.sap.com/ariba
  - type: GitHubOrganization
    url: https://github.com/SAP-samples
  - type: CodeExamples
    url: https://github.com/SAP-samples/ariba-extensibility-samples
    title: SAP Ariba Extensibility Samples
  - type: SpectralRules
    url: rules/ariba-guided-buying-spectral-rules.yml
  - type: NaftikoCapability
    url: capabilities/procurement-operations.yaml
  - type: Vocabulary
    url: vocabulary/ariba-guided-buying-vocabulary.yaml
  - type: Features
    data:
      - name: Consumer-Like Shopping Experience
        description: Provides employees with an intuitive catalog-driven shopping interface similar to consumer e-commerce applications.
      - name: Catalog Search and Typeahead
        description: Full-text search with typeahead autocomplete for finding catalog items from suppliers on SAP Business Network.
      - name: Policy Compliance Enforcement
        description: Built-in procurement policy checks ensure purchases comply with organizational spending rules and approval workflows.
      - name: Asset Management Integration
        description: Integrates with SAP ERP asset management to assign and track asset numbers on requisition line items.
      - name: OAuth 2.0 Authentication
        description: Secure API access using OAuth 2.0 client credentials flow with per-API credentials.
      - name: Faceted Search
        description: Retrieves filter facets alongside catalog items enabling refined product browsing and discovery.
  - type: UseCases
    data:
      - name: Employee Self-Service Procurement
        description: Enable employees to browse and purchase approved goods from supplier catalogs without manual procurement processes.
      - name: ERP Asset Record Import
        description: Import asset records from SAP ERP and assign unique asset values to line items on approved requisitions.
      - name: Catalog Integration
        description: Integrate SAP Ariba Buying with SAP S/4HANA Cloud Public Edition to access public supplier catalogs on SAP Business Network.
      - name: Requisition Automation
        description: Automate retrieval and processing of asset-based requisitions through the Asset Workbench workflow.
  - type: Integrations
    data:
      - name: SAP S/4HANA Cloud
        description: Integrates with SAP S/4HANA Cloud Public Edition for purchase request creation and order management.
      - name: SAP Business Network
        description: Connects to SAP Business Network to access public supplier catalogs and pricing.
      - name: SAP ERP
        description: Integrates with SAP ERP systems for asset management and purchase order creation.
      - name: SAP Integration Suite
        description: Extends SAP Ariba functionality through SAP Integration Suite for custom workflows and data transformations.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
