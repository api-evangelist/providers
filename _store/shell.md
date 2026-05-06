---
aid: shell
url: https://raw.githubusercontent.com/api-evangelist/shell/refs/heads/main/apis.yml
apis:
  - aid: shell:b2b-mobility-card-management
    name: Shell B2B Mobility Card Management API
    tags:
      - B2B
      - Cards
      - Fleet
      - Mobility
    humanURL: https://developer.shell.com/api-catalog
    properties:
      - url: https://developer.shell.com/api-catalog
        type: Documentation
      - url: openapi/shell-b2b-mobility-openapi.yml
        type: OpenAPI
      - url: json-schema/shell-fuel-card-schema.json
        type: JSONSchema
      - url: json-schema/shell-transaction-schema.json
        type: JSONSchema
      - url: rules/shell-rules.yml
        type: SpectralRules
      - url: capabilities/fleet-management.yaml
        type: NaftikoCapabilities
    description: The Shell B2B Mobility Card Management API enables fleet operators and business customers to manage fuel cards, control spending limits, restrict usage by fuel type, location, or time, and monitor card status. Supports card issuance, updates, and lifecycle management for corporate fuel card programs.
  - aid: shell:b2b-mobility-card-transaction-data
    name: Shell B2B Mobility Card Transaction Data API
    tags:
      - B2B
      - Fleet
      - Mobility
      - Transactions
    humanURL: https://developer.shell.com/api-catalog/v2.1.0/b2b-mobility-card-transaction-data
    properties:
      - url: https://developer.shell.com/api-catalog/v2.1.0/b2b-mobility-card-transaction-data
        type: Documentation
      - url: openapi/shell-b2b-mobility-openapi.yml
        type: OpenAPI
    description: Provides access to fuel card transaction data for B2B customers. Enables retrieval of transaction history, spend analytics, fuel type breakdowns, and location-based purchase data for corporate fleet management and expense reporting.
  - aid: shell:b2b-mobility-invoice
    name: Shell B2B Mobility Invoice API
    tags:
      - B2B
      - Finance
      - Fleet
      - Invoices
    humanURL: https://developer.shell.com/api-catalog
    properties:
      - url: https://developer.shell.com/api-catalog
        type: Documentation
      - url: openapi/shell-b2b-mobility-openapi.yml
        type: OpenAPI
    description: Enables business customers to retrieve and manage invoices for Shell fuel card programs. Supports invoice download, payment status queries, and reconciliation workflows for fleet finance teams.
  - aid: shell:loyalty-catalogue
    name: Shell Loyalty Catalogue API
    tags:
      - Loyalty
      - Rewards
      - Retail
    humanURL: https://developer.shell.com/api-catalog/v1.0.2/loyalty-catalogue
    properties:
      - url: https://developer.shell.com/api-catalog/v1.0.2/loyalty-catalogue
        type: Documentation
      - url: openapi/shell-loyalty-openapi.yml
        type: OpenAPI
      - url: capabilities/loyalty-program.yaml
        type: NaftikoCapabilities
    description: The Shell Loyalty Catalogue API provides access to the Shell Go+ loyalty program product and rewards catalogue. Partners can retrieve available rewards, offers, and redemption options to display within their applications and loyalty program integrations.
  - aid: shell:loyalty-account-management
    name: Shell Loyalty Account Management API
    tags:
      - Loyalty
      - Rewards
      - Accounts
    humanURL: https://developer.shell.com/use-cases/shell-loyalty-api-partners
    properties:
      - url: https://developer.shell.com/use-cases/shell-loyalty-api-partners
        type: Documentation
      - url: openapi/shell-loyalty-openapi.yml
        type: OpenAPI
    description: Enables partners to manage Shell loyalty accounts, including enrolment, profile management, points balance queries, and account status updates. Integrates Shell Go+ loyalty program into partner digital platforms.
  - aid: shell:loyalty-points-balance
    name: Shell Loyalty Points Balance API
    tags:
      - Loyalty
      - Points
      - Rewards
    humanURL: https://developer.shell.com/api-catalog
    properties:
      - url: https://developer.shell.com/api-catalog
        type: Documentation
      - url: openapi/shell-loyalty-openapi.yml
        type: OpenAPI
    description: Provides real-time query access to Shell loyalty points balances for program members. Enables partners to display current points, tier status, and points expiry information within their applications.
  - aid: shell:loyalty-points-redemption
    name: Shell Loyalty Points Redemption API
    tags:
      - Loyalty
      - Points
      - Redemption
    humanURL: https://developer.shell.com/api-catalog
    properties:
      - url: https://developer.shell.com/api-catalog
        type: Documentation
      - url: openapi/shell-loyalty-openapi.yml
        type: OpenAPI
    description: Enables partners to process loyalty points redemptions within Shell Go+ loyalty program. Supports redeeming points for fuel savings, partner rewards, and gift cards through the Shell Loyalty platform.
  - aid: shell:lubricants-order-management
    name: Shell Lubricants Order Management API
    tags:
      - Lubricants
      - Oil
      - Orders
      - B2B
    humanURL: https://developer.shell.com/api-catalog
    properties:
      - url: https://developer.shell.com/api-catalog
        type: Documentation
      - url: openapi/shell-lubricants-openapi.yml
        type: OpenAPI
    description: The Shell Lubricants Order Management API enables business customers and distributors to place and manage orders for Shell lubricants products. Supports order creation, status tracking, delivery scheduling, and product catalogue queries.
  - aid: shell:aviation-fuel-reseller
    name: Shell Aviation Fuel Reseller API
    tags:
      - Aviation
      - Fuel
      - B2B
    humanURL: https://developer.shell.com/api-catalog
    properties:
      - url: https://developer.shell.com/api-catalog
        type: Documentation
    description: The Shell Aviation Fuel Reseller API enables aviation fuel resellers and operators to manage fuel procurement, pricing queries, order placement, and delivery logistics for Shell Aviation fuel products at airports and FBOs worldwide.
  - aid: shell:b2b-mobility-sites
    name: Shell B2B Mobility Sites API
    tags:
      - B2B
      - Fleet
      - Locations
      - Mobility
    humanURL: https://developer.shell.com/api-catalog/b2b-mobility-sites/quick-start-guide
    properties:
      - url: https://developer.shell.com/api-catalog/b2b-mobility-sites/quick-start-guide
        type: Documentation
      - url: openapi/shell-b2b-mobility-openapi.yml
        type: OpenAPI
    description: Provides access to the Shell network of fuel and EV charging sites for B2B mobility customers. Enables applications to query site locations, available fuel types, EV charging availability, amenities, and opening hours across the Shell station network.
name: Shell
tags:
  - Aviation
  - Electric Vehicle Charging
  - Energy
  - Fleet Management
  - Fuel
  - Gas
  - Loyalty
  - Lubricants
  - Mobility
  - Oil and Gas
  - Renewable Energy
type: Contract
image: https://www.shell.com/etc/designs/shell/clientlib-main/img/shell-logo.png
access: 3rd-Party
created: '2025-03-01'
modified: '2026-05-02'
position: Consumer
description: Royal Dutch Shell plc is a global energy company operating across oil, gas, renewable energy, lubricants, aviation fuel, and mobility sectors. The Shell Developer Portal provides APIs for B2B mobility card management, loyalty programs, lubricants ordering, aviation fuel reselling, and fleet management. SDKs are available in Java, .NET, TypeScript, PHP, Python, and Ruby.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
  - FN: Shell Digital Services
    email: api-maintainers@shell.com
    X-twitter: shell
specificationVersion: '0.19'
common:
  - url: https://developer.shell.com
    type: Developer Portal
  - url: https://developer.shell.com/api-catalog
    type: API Catalog
  - url: https://developer.shell.com/docs/welcome-shell-developer-portal
    type: Getting Started
  - url: https://developer.shell.com/signup
    type: API Key Registration
  - url: https://developer.shell.com/docs/authentication
    type: Authentication
  - url: https://www.shell.com/terms-and-conditions
    type: Terms of Service
  - url: https://www.shell.com/privacy
    type: Privacy Policy
  - url: https://developer.shell.com/support
    type: Support
  - url: https://developer.shell.com/support/api-status
    type: Status Page
  - url: https://developer.shell.com/latest-updates
    type: Blog
  - url: https://github.com/shell
    type: GitHub Organization
  - url: https://www.shell.com
    type: Website
  - url: json-ld/shell-context.jsonld
    type: JSONLD
  - url: vocabulary/shell-vocabulary.yml
    type: Vocabulary
---
