---
aid: togai
name: Togai
description: Togai is a metering and billing platform for software and SaaS products, purpose-built for consumption-based and usage-based pricing models. The Togai API provides programmatic access to customers, accounts, event ingestion, usage meters, price plans, invoices, credits, entitlements, and financial reporting. Supports real-time billing orchestration across cloud infrastructure, generative AI services, and SaaS applications.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Billing
  - Metering
  - Usage-Based Pricing
  - Revenue Management
  - SaaS
  - Fintech
created: '2025-02-10'
modified: '2026-05-03'
url: https://raw.githubusercontent.com/api-evangelist/togai/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: togai:togai-api
    name: Togai API
    description: The Togai API provides full programmatic access to the Togai usage-based billing platform. Resources include customers, accounts, event schemas, usage meters, price plans, pricing rules, invoices, credits, entitlements, wallet, licenses, and reports. Supports both production and sandbox environments.
    humanURL: https://docs.togai.com/api-reference/getting-started
    baseURL: https://api.togai.com
    tags:
      - Billing
      - Metering
      - Usage-Based Pricing
      - Revenue Management
      - Customers
      - Invoices
    properties:
      - type: Documentation
        url: https://docs.togai.com/api-reference/getting-started
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/togai/refs/heads/main/openapi/togai-openapi.yml
      - type: Getting Started
        url: https://docs.togai.com/docs/introduction
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/togai/refs/heads/main/json-schema/togai-customer-schema.json
      - type: NaftikoCapabilities
        url: https://raw.githubusercontent.com/api-evangelist/togai/refs/heads/main/capabilities/usage-based-billing.yaml
      - type: SpectralRules
        url: https://raw.githubusercontent.com/api-evangelist/togai/refs/heads/main/rules/togai-rules.yml
      - type: Vocabulary
        url: https://raw.githubusercontent.com/api-evangelist/togai/refs/heads/main/vocabulary/togai-vocabulary.yml
features:
  - Usage-based metering and rating
  - Price plan creation and management
  - Customer and account lifecycle management
  - Invoice generation and management
  - Credits and wallet management
  - Entitlements and feature gating
  - Metrics and financial reporting
  - Webhook notifications
  - Price experimentation
  - Sandbox environment
useCases:
  - Cloud infrastructure metering
  - Generative AI usage billing
  - SaaS consumption pricing
  - API monetization
  - Enterprise billing automation
solutions:
  - Revenue operations
  - Developer platform monetization
  - Usage-based pricing transformation
integrations:
  - Stripe
  - Salesforce
  - QuickBooks
  - NetSuite
  - HubSpot
  - Chargebee
  - Zuora
common:
  - type: Website
    url: https://www.togai.com/
  - type: Developer Portal
    url: https://docs.togai.com/
  - type: Documentation
    url: https://docs.togai.com/docs
  - type: API Reference
    url: https://docs.togai.com/api-reference/getting-started
  - type: Sign Up
    url: https://app.togai.com/auth/signup
  - type: Pricing
    url: https://www.togai.com/pricing/
  - type: Blog
    url: https://www.togai.com/blog/
  - type: Changelog
    url: https://docs.togai.com/changelog/change-log
  - type: GitHub Organization
    url: https://github.com/TogaiHQ
  - type: Sandbox
    url: https://sandbox-api.togai.com/
  - type: Postman Collection
    url: https://docs.togai.com/api-reference/getting-started
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
