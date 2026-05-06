---
aid: trustwell
url: https://raw.githubusercontent.com/api-evangelist/trustwell/refs/heads/main/apis.yml
name: Trustwell
description: 'Trustwell is a food industry software company formed from the merger of ESHA Research and FoodLogiQ in 2023, providing the food and beverage industry with an integrated platform covering product formulation, nutrition labeling, regulatory compliance, supply chain management, traceability, quality assurance, and recall management. The Trustwell Connect Platform offers two primary APIs: the Genesis Foods GraphQL API for nutrition analysis, food formulation, and label generation (with support for US, Canadian, EU, Mexican, and Australian regulatory standards), and the FoodLogiQ API for supply chain visibility, compliance management, supplier relationships, and FSMA 204-compliant traceability. Both APIs require X-API-KEY authentication. The platform serves food manufacturers, retailers, restaurants, and distributors across the global food supply chain.'
type: Index
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Food Industry
  - Food Safety
  - Nutrition
  - Supply Chain
  - Food Labeling
  - Traceability
  - Compliance
  - Food Technology
access: 3rd-Party
created: '2026-03-16'
modified: '2026-05-03'
specificationVersion: '0.19'
apis:
  - aid: trustwell:trustwell-genesis-foods-graphql-api
    name: Trustwell Genesis Foods GraphQL API
    tags:
      - Food Formulation
      - Nutrition Labeling
      - Regulatory Compliance
      - Food Industry
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.trustwell.com/genesis
    humanURL: https://docs.trustwell.com/genesis/api/
    properties:
      - url: https://docs.trustwell.com/genesis/api/
        type: Documentation
      - url: https://www.trustwell.com/products/genesis/food-formulation-and-labeling/
        type: Documentation
    description: The Trustwell Genesis Foods GraphQL API provides programmatic access to food formulation, nutrition analysis, and label generation capabilities. The GraphQL endpoint at api.trustwell.com/genesis supports 16 query types (foods, labels, nutrients, allergens, products, suppliers, regulations, documents, and more), 6 mutation categories (foods with 50+ sub-operations, label, documents, products, suppliers, tags), and 2 subscription types (documentEvents, tenantEvents) for real-time monitoring. The API supports 600+ schema types covering US, Canadian, EU, Mexican, and Australian/New Zealand regulatory standards for nutrition labeling. Authentication uses the X-API-KEY header. The API connects nutrition analysis data to ERP, PLM, POS, and website systems.
  - aid: trustwell:trustwell-foodlogiq-api
    name: Trustwell FoodLogiQ API
    tags:
      - Food Safety
      - Supply Chain
      - Traceability
      - Compliance
      - Quality Management
      - Recall Management
      - Food Industry
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.trustwell.com/foodlogiq
    humanURL: https://www.trustwell.com/products/foodlogiq/
    properties:
      - url: https://www.trustwell.com/products/foodlogiq/
        type: Documentation
      - url: https://www.trustwell.com/products/foodlogiq/product-management/
        type: Documentation
      - url: https://raw.githubusercontent.com/api-evangelist/trustwell/refs/heads/main/openapi/trustwell-foodlogiq-openapi.yml
        type: OpenAPI
    description: The Trustwell FoodLogiQ API is an open REST API that enables enterprise food brands to integrate supply chain data with their existing systems. The API supports supplier relationship management, compliance documentation, quality incident management, product specification management, FSMA 204-compliant traceability (farm-to-fork tracking), and recall management workflows. The Q3 2025 release introduced role-based API tokens with scoped permissions for fine-grained access control. The API is documented within the FoodLogiQ Connect platform Resource Center and supports integration with ERP, WMS, and third-party food safety systems.
  - aid: trustwell:trustwell-genesis-supplements-api
    name: Trustwell Genesis Supplements API
    tags:
      - Supplement Formulation
      - Nutrition Labeling
      - Regulatory Compliance
      - Food Industry
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.trustwell.com/genesis
    humanURL: https://www.trustwell.com/products/genesis/
    properties:
      - url: https://www.trustwell.com/products/genesis/
        type: Documentation
      - url: https://docs.trustwell.com/genesis/api/
        type: Documentation
    description: The Trustwell Genesis Supplements API provides formulation and regulatory compliance capabilities for dietary supplement manufacturers. Built on the same Genesis Foods GraphQL endpoint, it supports Supplement Facts label generation, ingredient declaration, allergen statements, and compliance with FDA dietary supplement regulations. The API enables integration of supplement formulation data into ERP and PLM systems.
common:
  - url: https://www.trustwell.com/
    name: Trustwell Website
    type: Website
  - url: https://docs.trustwell.com/
    name: Developer Documentation
    type: Documentation
  - url: https://docs.trustwell.com/genesis/api/
    name: Genesis API Documentation
    type: Documentation
  - url: https://www.trustwell.com/platform/
    name: Trustwell Connect Platform
    type: Portal
  - url: https://www.trustwell.com/products/
    name: Products
    type: Products
  - url: https://blog.trustwell.com/
    name: Trustwell Blog
    type: Blog
  - url: https://www.trustwell.com/news-and-press/
    name: News and Press
    type: News
  - url: https://www.trustwell.com/privacy-policy/
    name: Privacy Policy
    type: PrivacyPolicy
  - url: https://www.trustwell.com/terms-of-service/
    name: Terms of Service
    type: TermsOfService
  - url: https://www.linkedin.com/company/trustwell-llc
    name: Trustwell on LinkedIn
    type: LinkedIn
  - url: https://raw.githubusercontent.com/api-evangelist/trustwell/refs/heads/main/rules/trustwell-rules.yml
    name: Spectral Rules
    type: SpectralRules
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
