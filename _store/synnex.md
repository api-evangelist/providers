---
aid: synnex
name: Synnex
description: SYNNEX Corporation (now TD SYNNEX) is a Fortune 100 global IT distribution company and solutions aggregator that connects technology vendors with resellers, system integrators, and enterprise customers. The company provides comprehensive API access through its StreamOne ION platform for managing cloud subscriptions, product catalogs, customer accounts, and orders. TD SYNNEX was formed in 2021 through the merger of Synnex Corporation and Tech Data.
url: https://raw.githubusercontent.com/api-evangelist/synnex/refs/heads/main/apis.yml
created: '2026-05-03'
modified: '2026-05-03'
tags:
  - Technology Distribution
  - IT Distribution
  - Cloud Marketplace
  - Fortune 100
  - Supply Chain
apis:
  - aid: synnex:streamone-ion
    name: TD SYNNEX StreamOne ION API
    description: The StreamOne ION API is TD SYNNEX's interface for cloud vendors and reseller partners to manage cloud subscriptions, product catalogs, end customers, and orders through a unified platform. The API supports end customer management, product operations, order management, subscription lifecycle, shopping cart workflows, and reporting via OAuth 2.0 authentication.
    humanURL: https://www.tdsynnex.com/ion/api/
    baseURL: https://ion.tdsynnex.com/api/v3
    tags:
      - Cloud Marketplace
      - IT Distribution
      - Subscription Management
      - Order Management
      - Partner API
    properties:
      - type: Documentation
        url: https://docs.streamone.cloud/
      - type: OpenAPI
        url: openapi/synnex-streamone-ion-openapi.yml
  - aid: synnex:digital-bridge
    name: TD SYNNEX Digital Bridge API
    description: The Digital Bridge Developer Portal gives engineering teams direct access to REST APIs for products, pricing, orders, renewals, and cloud services. Partners can get sandbox API keys, test endpoints, and integrate live TD SYNNEX data into any workflow or system.
    humanURL: https://www.tdsynnex.com/na/us/digital-bridge/
    baseURL: https://api.tdsynnex.com
    tags:
      - IT Distribution
      - Products
      - Pricing
      - Orders
      - Partner Integration
    properties:
      - type: Documentation
        url: https://www.tdsynnex.com/na/us/digital-bridge/
      - type: DeveloperPortal
        url: https://www.tdsynnex.com/na/us/digital-bridge/
common:
  - type: Website
    url: https://www.tdsynnex.com
  - type: DeveloperPortal
    url: https://www.tdsynnex.com/ion/api/
  - type: APIDocumentation
    url: https://docs.streamone.cloud/
  - type: GitHubOrg
    url: https://github.com/cloudmindsab/td-synnex
  - type: JSONLDContext
    url: json-ld/synnex-context.jsonld
  - type: Vocabulary
    url: vocabulary/synnex-vocabulary.yml
features:
  - OAuth 2.0 Authentication
  - End Customer Management
  - Product and SKU Catalog
  - Order Management
  - Subscription Lifecycle Management
  - Shopping Cart Operations
  - Cloud Provider Account Management
  - Reporting and Data Export
  - Swagger/OpenAPI Testing Interface
  - Sandbox Environment
  - Multi-Currency and Multi-Language Support
useCases:
  - Cloud Subscription Reselling
  - IT Product Distribution
  - Reseller Partner Integration
  - Subscription Lifecycle Automation
  - Product Catalog Synchronization
  - Order Automation
integrations:
  - type: Microsoft
    description: Microsoft CSP and Azure cloud products
  - type: Google
    description: Google Workspace and GCP products
solutions:
  - Cloud Marketplace Operations
  - Reseller Partner Enablement
  - IT Distribution Automation
---
