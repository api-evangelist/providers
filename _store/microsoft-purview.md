---
aid: microsoft-purview
name: Microsoft Purview
description: Microsoft Purview is a comprehensive data governance service that helps organizations discover, catalog, classify, and manage their data estate across on-premises, multi-cloud, and SaaS environments.
image: https://www.microsoft.com/en-us/microsoft-365/blog/wp-content/uploads/sites/2/2021/04/Microsoft-Purview-logo.png
url: https://www.microsoft.com/en-us/security/business/microsoft-purview
created: 2024-01-15T00:00:00.000Z
modified: '2026-04-28'
specificationVersion: '0.19'
tags:
  - Compliance
  - Data Catalog
  - Data Classification
  - Data Governance
  - Data Loss Prevention
  - Information Protection
apis:
  - name: Microsoft Purview Catalog API
    description: APIs for discovering, cataloging, and managing metadata for data assets across your data estate. The catalog is built on Apache Atlas and provides searchable inventory of data assets with classifications and glossary terms.
    image: https://www.microsoft.com/en-us/security/business/microsoft-purview
    humanURL: https://learn.microsoft.com/en-us/purview/catalog-api
    baseURL: https://{account-name}.purview.azure.com
    tags:
      - Classifications
      - Data Catalog
      - Data Discovery
      - Glossary
      - Metadata
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/purview/
      - type: OpenAPI
        url: openapi/microsoft-purview-catalog-openapi.yml
      - type: Authentication
        url: https://learn.microsoft.com/en-us/purview/tutorial-using-rest-apis
      - type: Pricing
        url: https://azure.microsoft.com/en-us/pricing/details/purview/
      - type: Getting Started
        url: https://learn.microsoft.com/en-us/purview/data-gov-api-create-assets
  - name: Microsoft Purview Scanning API
    description: APIs for configuring and managing scans of data sources to automatically discover and catalog data assets. Supports registering data sources and scheduling automated scans across your data estate.
    image: https://www.microsoft.com/en-us/security/business/microsoft-purview
    humanURL: https://learn.microsoft.com/en-us/purview/scanning-api
    baseURL: https://{account-name}.purview.azure.com
    tags:
      - Automated Discovery
      - Classification Rules
      - Data Scanning
      - Data Sources
      - Scan Triggers
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/purview/scanning
      - type: OpenAPI
        url: openapi/microsoft-purview-scanning-openapi.yml
      - type: Authentication
        url: https://learn.microsoft.com/en-us/purview/tutorial-using-rest-apis
      - type: Reference
        url: https://learn.microsoft.com/en-us/purview/data-map-data-sources
  - name: Microsoft Purview Account API
    description: APIs for managing Purview accounts, configurations, and administrative settings. Provides resource management operations for creating, updating, and deleting Purview accounts through Azure Resource Manager.
    image: https://www.microsoft.com/en-us/security/business/microsoft-purview
    humanURL: https://learn.microsoft.com/en-us/purview/account-api
    baseURL: https://management.azure.com
    tags:
      - Account Management
      - Administration
      - Configuration
      - Resource Manager
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/purview/account
      - type: OpenAPI
        url: openapi/microsoft-purview-account-openapi.yml
      - type: Authentication
        url: https://learn.microsoft.com/en-us/azure/active-directory/develop/v2-oauth2-client-creds-grant-flow
  - name: Microsoft Purview Data Map API
    description: APIs for accessing and managing the unified data map that provides a holistic view of your data estate. Supports entity management, lineage tracking, relationship mapping, and discovery queries across cataloged assets.
    image: https://www.microsoft.com/en-us/security/business/microsoft-purview
    humanURL: https://learn.microsoft.com/en-us/purview/data-map-api
    baseURL: https://{account-name}.purview.azure.com
    tags:
      - Data Discovery
      - Data Map
      - Entity Management
      - Lineage
      - Relationships
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/purview/datamap
      - type: OpenAPI
        url: openapi/microsoft-purview-data-map-openapi.yml
      - type: Authentication
        url: https://learn.microsoft.com/en-us/purview/tutorial-using-rest-apis
      - type: Getting Started
        url: https://learn.microsoft.com/en-us/purview/legacy/how-to-purview-custom-lineage-api-user-guide
  - name: Microsoft Purview Metadata Policies API
    description: APIs for creating and managing data access policies based on metadata attributes. Enables programmatic management of collection-level permissions and role assignments.
    image: https://www.microsoft.com/en-us/security/business/microsoft-purview
    humanURL: https://learn.microsoft.com/en-us/purview/metadata-policies
    baseURL: https://{account-name}.purview.azure.com
    tags:
      - Access Policies
      - Collections
      - Data Governance
      - Metadata
      - Role Assignments
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/purview/metadatapolicies
      - type: OpenAPI
        url: openapi/microsoft-purview-metadata-policies-openapi.yml
      - type: Authentication
        url: https://learn.microsoft.com/en-us/purview/tutorial-using-rest-apis
      - type: Getting Started
        url: https://learn.microsoft.com/en-us/purview/legacy/tutorial-metadata-policy-collections-apis
  - name: Microsoft Purview Workflow API
    description: APIs for managing workflows and approval processes for data governance tasks. Supports defining custom approval workflows for glossary term management and other governance operations.
    image: https://www.microsoft.com/en-us/security/business/microsoft-purview
    humanURL: https://learn.microsoft.com/en-us/purview/workflow-api
    baseURL: https://{account-name}.purview.azure.com
    tags:
      - Approvals
      - Automation
      - Governance Tasks
      - Workflows
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/purview/workflow
      - type: OpenAPI
        url: openapi/microsoft-purview-workflow-openapi.yml
      - type: Authentication
        url: https://learn.microsoft.com/en-us/purview/tutorial-using-rest-apis
  - name: Microsoft Purview Unified Catalog API
    description: APIs for programmatically integrating and managing the Microsoft Purview Unified Catalog. Supports operations on business domains, glossary terms, data products, OKRs, critical data elements, and data access policies.
    image: https://www.microsoft.com/en-us/security/business/microsoft-purview
    humanURL: https://learn.microsoft.com/en-us/rest/api/purview/unified-catalog-api-overview
    baseURL: https://{account-name}.purview.azure.com
    tags:
      - Business Domains
      - Data Governance
      - Data Products
      - Glossary Terms
      - Unified Catalog
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/purview/unified-catalog-api-overview
      - type: OpenAPI
        url: openapi/microsoft-purview-unified-catalog-openapi.yml
      - type: Authentication
        url: https://learn.microsoft.com/en-us/purview/data-gov-api-rest-data-plane
  - name: Microsoft Purview Data Quality API
    description: APIs for programmatically interacting with data quality rules, measuring data quality, and retrieving data quality scores for data assets. Supports data profiling, rule management, and quality assessment operations.
    image: https://www.microsoft.com/en-us/security/business/microsoft-purview
    humanURL: https://learn.microsoft.com/en-us/rest/api/purview/unified-catalog-data-quality
    baseURL: https://{account-name}.purview.azure.com
    tags:
      - Data Assessment
      - Data Profiling
      - Data Quality
      - Quality Rules
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/purview/unified-catalog-data-quality
      - type: OpenAPI
        url: openapi/microsoft-purview-data-quality-openapi.yml
      - type: Reference
        url: https://learn.microsoft.com/en-us/purview/unified-catalog-data-quality
      - type: Authentication
        url: https://learn.microsoft.com/en-us/purview/data-gov-api-rest-data-plane
  - name: Microsoft Purview eDiscovery API
    description: APIs for automating eDiscovery operations through Microsoft Graph, including managing cases, custodians, review sets, searches, and exports for litigation, investigation, and regulatory requests.
    image: https://www.microsoft.com/en-us/security/business/microsoft-purview
    humanURL: https://learn.microsoft.com/en-us/graph/api/resources/security-ediscovery-apioverview
    baseURL: https://graph.microsoft.com
    tags:
      - Compliance
      - eDiscovery
      - Investigations
      - Legal Hold
      - Litigation
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/graph/api/resources/security-ediscovery-apioverview?view=graph-rest-1.0
      - type: OpenAPI
        url: openapi/microsoft-purview-ediscovery-openapi.yml
      - type: Authentication
        url: https://learn.microsoft.com/en-us/graph/security-ediscovery-appauthsetup
      - type: Getting Started
        url: https://learn.microsoft.com/en-us/purview/edisc-ref-api-guide
  - name: Microsoft Purview Information Protection API
    description: APIs for accessing and managing sensitivity labels through Microsoft Graph. Enables applications to apply, update, and delete sensitivity labels, evaluate label actions, and enforce information protection policies programmatically.
    image: https://www.microsoft.com/en-us/security/business/microsoft-purview
    humanURL: https://learn.microsoft.com/en-us/graph/security-information-protection-overview
    baseURL: https://graph.microsoft.com
    tags:
      - Data Classification
      - Encryption
      - Information Protection
      - Rights Management
      - Sensitivity Labels
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/graph/security-information-protection-overview
      - type: OpenAPI
        url: openapi/microsoft-purview-information-protection-openapi.yml
      - type: Reference
        url: https://learn.microsoft.com/en-us/purview/sensitivity-labels
  - name: Microsoft Purview Data Security and Governance API
    description: APIs for integrating data loss prevention and compliance policy enforcement into applications through Microsoft Graph. Provides compute protection scopes and process content operations to evaluate and enforce DLP policies at runtime.
    image: https://www.microsoft.com/en-us/security/business/microsoft-purview
    humanURL: https://learn.microsoft.com/en-us/graph/security-datasecurityandgovernance-overview
    baseURL: https://graph.microsoft.com
    tags:
      - AI Security
      - Compliance
      - Data Loss Prevention
      - Data Security
      - Policy Enforcement
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/graph/security-datasecurityandgovernance-overview
      - type: OpenAPI
        url: openapi/microsoft-purview-data-security-governance-openapi.yml
      - type: Getting Started
        url: https://learn.microsoft.com/en-us/purview/developer/use-the-api
      - type: Reference
        url: https://learn.microsoft.com/en-us/purview/developer/
  - name: Microsoft Purview Records Management API
    description: APIs for managing retention labels, retention policies, and disposition review through Microsoft Graph. Helps organizations manage data retention and deletion to meet legal obligations and compliance regulations.
    image: https://www.microsoft.com/en-us/security/business/microsoft-purview
    humanURL: https://learn.microsoft.com/en-us/graph/api/resources/security-recordsmanagement-overview
    baseURL: https://graph.microsoft.com
    tags:
      - Compliance
      - Data Lifecycle
      - Records Management
      - Retention Labels
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/graph/api/resources/security-recordsmanagement-overview?view=graph-rest-1.0
      - type: OpenAPI
        url: openapi/microsoft-purview-records-management-openapi.yml
      - type: Reference
        url: https://learn.microsoft.com/en-us/graph/compliance-concept-overview
common:
  - type: Portal
    url: https://purview.microsoft.com
  - type: Documentation
    url: https://learn.microsoft.com/en-us/purview/
  - type: Getting Started
    url: https://learn.microsoft.com/en-us/purview/use-azure-purview-studio
  - type: Authentication
    url: https://learn.microsoft.com/en-us/purview/data-gov-api-rest-data-plane
  - type: Reference
    url: https://learn.microsoft.com/en-us/rest/api/purview/
  - type: SDKs
    url: https://learn.microsoft.com/en-us/purview/data-gov-python-sdk
  - type: Best Practices
    url: https://learn.microsoft.com/en-us/purview/concept-best-practices-accounts
  - type: Change Log
    url: https://learn.microsoft.com/en-us/purview/whats-new
  - type: Blog
    url: https://techcommunity.microsoft.com/t5/microsoft-purview-blog/bg-p/MicrosoftPurviewBlog
  - type: Support
    url: https://learn.microsoft.com/en-us/answers/topics/azure-purview.html
  - type: Status
    url: https://status.azure.com/
  - type: Terms of Service
    url: https://azure.microsoft.com/en-us/support/legal/
  - type: Privacy Policy
    url: https://privacy.microsoft.com/en-us/privacystatement
  - type: GitHub Organization
    url: https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/purview
  - type: Community
    url: https://techcommunity.microsoft.com/t5/microsoft-purview/ct-p/MicrosoftPurview
  - type: Website
    url: https://www.microsoft.com/en-us/security/business/microsoft-purview
  - type: Login
    url: https://purview.microsoft.com
  - type: Sign Up
    url: https://azure.microsoft.com/en-us/products/purview/
  - type: JSON-LD
    url: json-ld/microsoft-purview-context.jsonld
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
