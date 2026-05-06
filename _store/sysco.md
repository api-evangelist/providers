---
aid: sysco
name: Sysco
description: Sysco is the global leader in selling, marketing, and distributing food products to restaurants, healthcare and educational facilities, lodging establishments, and other foodservice customers. Sysco's APIC Developer Portal provides REST APIs for product catalog browsing, order management, delivery tracking, account management, and pricing integration, enabling partners and customers to automate their food distribution workflows.
url: https://raw.githubusercontent.com/api-evangelist/sysco/refs/heads/main/apis.yml
created: '2026-05-03'
modified: '2026-05-03'
tags:
  - Food Distribution
  - Food Service
  - Supply Chain
  - Fortune 100
  - Wholesale
apis:
  - aid: sysco:food-distribution-api
    name: Sysco Food Distribution API
    description: The Sysco Food Distribution API provides programmatic access to Sysco's food distribution platform for product catalog browsing, order management, delivery tracking, account management, and pricing. Available through the Sysco APIC Developer Portal, the APIs enable partners, restaurants, and food service operators to integrate with Sysco's ordering systems, browse product catalogs with over 30 data fields, track deliveries, and manage their food supply chain operations.
    humanURL: https://apic-devportal.sysco.com/
    baseURL: https://api.sysco.com
    tags:
      - Food Distribution
      - Ordering
      - Restaurant
      - Supply Chain
      - Product Catalog
      - Delivery Tracking
    properties:
      - type: Documentation
        url: https://apic-devportal.sysco.com/
      - type: OpenAPI
        url: openapi/sysco-food-distribution-api-openapi.yml
common:
  - type: Website
    url: https://www.sysco.com
  - type: DeveloperPortal
    url: https://apic-devportal.sysco.com/
  - type: GitHubOrg
    url: https://github.com/SyscoCorporation
  - type: GraphQL
    url: https://www.apollographql.com/customers/sysco
  - type: JSONLDContext
    url: json-ld/sysco-context.jsonld
  - type: Vocabulary
    url: vocabulary/sysco-vocabulary.yml
features:
  - Product Catalog with 30+ Data Fields
  - Real-Time Stock Status
  - Order Management
  - Delivery Tracking
  - Contract Pricing
  - Account Management
  - GraphQL API (Apollo)
  - Staging and Production Environments
useCases:
  - Food Service Ordering Automation
  - Product Catalog Integration
  - Delivery Schedule Management
  - Supply Chain Visibility
  - ERP Integration
  - Restaurant Management System Integration
integrations:
  - type: ApolloGraphQL
    description: Sysco uses Apollo's graph-based API orchestration with domain subgraphs
  - type: Portable
    url: https://portable.io/connectors/sysco/postgresql
solutions:
  - Restaurant Technology Integration
  - Healthcare Food Service
  - Education Food Service
  - Hospitality Supply Chain
---
