---
aid: td-synnex
name: TD SYNNEX
description: TD SYNNEX is one of the world's largest IT distributors and solutions aggregators, serving over 150,000 resellers, retailers, and other customers in more than 100 countries. The company provides technology distribution, integration, and solutions services. TD SYNNEX offers the StreamOne Ion platform with REST APIs that enable partners to manage cloud subscriptions, customers, orders, and billing through a unified interface supporting multiple cloud vendors. Named NVIDIA EMEA Distributor of the Year 2026.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Technology Distribution
  - IT Distribution
  - Cloud
  - Reseller
  - StreamOne
  - Fortune 100
  - B2B
created: '2026-03-24'
modified: '2026-05-03'
url: https://raw.githubusercontent.com/api-evangelist/td-synnex/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: td-synnex:streamone-ion
    name: TD SYNNEX StreamOne Ion API
    description: The StreamOne Ion Partner API provides partners with programmatic access to TD SYNNEX cloud distribution services. Enables management of end customers, product catalogs, orders, subscriptions, shopping carts, and reporting through a unified REST interface supporting multiple cloud vendors. Uses OAuth 2.0 authentication with refresh token flow.
    humanURL: https://docs.streamone.cloud/
    baseURL: https://ion.tdsynnex.com
    tags:
      - Cloud Distribution
      - Subscription Management
      - Order Management
      - Customer Management
      - Reporting
    properties:
      - type: Documentation
        url: https://docs.streamone.cloud/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/td-synnex/refs/heads/main/openapi/td-synnex-streamone-ion-openapi.yml
    contact:
      - FN: TD SYNNEX Support
        url: https://www.tdsynnex.com/ion/api/
common:
  - type: Website
    url: https://www.tdsynnex.com/na/us/
  - type: Documentation
    name: StreamOne Ion API Documentation
    description: Official API documentation for the StreamOne Ion Partner API.
    url: https://docs.streamone.cloud/
  - type: Portal
    name: StreamOne Ion API Portal
    description: Developer portal for StreamOne Ion API access.
    url: https://www.tdsynnex.com/ion/api/
  - type: OpenAPI
    name: TD SYNNEX StreamOne Ion OpenAPI Specification
    url: https://raw.githubusercontent.com/api-evangelist/td-synnex/refs/heads/main/openapi/td-synnex-streamone-ion-openapi.yml
  - type: Vocabulary
    name: TD SYNNEX Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/td-synnex/refs/heads/main/vocabulary/td-synnex-vocabulary.yml
  - type: JSONSchema
    name: Customer Schema
    url: https://raw.githubusercontent.com/api-evangelist/td-synnex/refs/heads/main/json-schema/td-synnex-customer-schema.json
  - type: JSONSchema
    name: Order Schema
    url: https://raw.githubusercontent.com/api-evangelist/td-synnex/refs/heads/main/json-schema/td-synnex-order-schema.json
  - type: JSONLDContext
    name: TD SYNNEX JSON-LD Context
    url: https://raw.githubusercontent.com/api-evangelist/td-synnex/refs/heads/main/json-ld/td-synnex-context.jsonld
  - type: SpectralRules
    name: TD SYNNEX Spectral Rules
    url: https://raw.githubusercontent.com/api-evangelist/td-synnex/refs/heads/main/rules/td-synnex-rules.yml
  - type: NaftikoCapabilities
    name: TD SYNNEX Cloud Distribution Capability
    url: https://raw.githubusercontent.com/api-evangelist/td-synnex/refs/heads/main/capabilities/cloud-distribution.yaml
features:
  - name: Customer Management
    description: Create, retrieve, update, and manage end customer accounts.
  - name: Product Catalog
    description: Browse and query available technology products from multiple vendors.
  - name: Order Management
    description: Create, update, and manage technology product orders.
  - name: Subscription Management
    description: Track and manage cloud software subscriptions for customers.
  - name: Shopping Cart
    description: Create and manage shopping carts for streamlined ordering workflows.
  - name: Cloud Provider Integration
    description: Link and manage customer accounts with cloud providers.
  - name: Reporting
    description: Access business intelligence reports and export data in CSV format.
  - name: Provisioning Templates
    description: Vendor-specific provisioning configuration templates.
  - name: OAuth 2.0 Authentication
    description: Secure API access via OAuth 2.0 with token-based authentication.
  - name: Multi-Vendor Support
    description: Single interface for managing multiple cloud vendor subscriptions.
useCases:
  - name: MSP Subscription Management
    description: Managed service providers automate cloud subscription billing and management.
  - name: Reseller Order Automation
    description: Technology resellers automate product ordering workflows.
  - name: Cloud Marketplace Integration
    description: Integrate TD SYNNEX cloud marketplace into custom partner portals.
  - name: Customer Lifecycle Management
    description: Manage end customer provisioning from account creation to subscription management.
  - name: Business Intelligence
    description: Pull reporting data into custom dashboards and business analytics tools.
integrations:
  - name: Microsoft Azure
    description: Cloud provider integration for Microsoft Azure subscriptions.
  - name: AWS
    description: Amazon Web Services subscription management through StreamOne Ion.
  - name: Google Cloud
    description: Google Cloud Platform subscription management.
  - name: Rewst
    description: TD Synnex Stellr integration for workflow automation.
    url: https://docs.rewst.help/documentation/configuration/integrations/integration-guides/synnex-integration-setup
solutions:
  - name: MSP Cloud Distribution
    description: Streamlined cloud subscription management for managed service providers.
  - name: Technology Reseller Automation
    description: API-driven automation for technology product distribution workflows.
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
---
