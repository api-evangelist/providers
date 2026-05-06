---
aid: amberflo
name: Amberflo
description: Amberflo is a cloud metering, usage-based billing, and AI cost management platform. It provides real-time event ingestion, customer billing automation, AI gateway capabilities, and FinOps visibility for API-driven and AI-powered businesses. The platform supports usage-based, token-based, seat-based, and outcome-based pricing models with automated invoicing and embeddable billing dashboards.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Usage-Based Billing
  - Metering
  - FinOps
  - AI Cost Management
  - Billing
  - Monetization
url: https://raw.githubusercontent.com/api-evangelist/amberflo/refs/heads/main/apis.yml
created: '2026-03-27'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: amberflo:metering-api
    name: Amberflo Metering API
    description: The Amberflo Metering API provides meter definition management, high-throughput event ingestion, usage queries, raw event queries, and filtering rules. It supports real-time metering for API calls, tokens, and custom events with automatic aggregation and deduplication.
    humanURL: https://docs.amberflo.io/reference/ingest-meters
    baseURL: https://app.amberflo.io
    tags:
      - Metering
      - Event Ingestion
      - Usage Tracking
    properties:
      - type: Documentation
        url: https://docs.amberflo.io/reference/ingest-meters
      - type: APIReference
        url: https://docs.amberflo.io/reference/ingest-meters
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/amberflo/refs/heads/main/openapi/amberflo-metering-openapi.yaml
  - aid: amberflo:billing-api
    name: Amberflo Billing API
    description: The Amberflo Billing API manages customers, pricing plans, invoices, prepaid orders, promotions, commitments, and billing analysis. It supports usage-based monetization workflows including revenue recognition, chargeback management, and customer cost visibility.
    humanURL: https://docs.amberflo.io/reference/customers
    baseURL: https://app.amberflo.io
    tags:
      - Billing
      - Customers
      - Invoicing
      - Pricing Plans
    properties:
      - type: Documentation
        url: https://docs.amberflo.io/reference/customers
      - type: APIReference
        url: https://docs.amberflo.io/reference/customers
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/amberflo/refs/heads/main/openapi/amberflo-billing-openapi.yaml
  - aid: amberflo:cost-tracking-api
    name: Amberflo Cost Tracking API
    description: The Amberflo Cost Tracking API provides AI and cloud cost management capabilities including cloud provider integrations, business unit management, cost allocation rules, budget management, and cost query analytics. It enables FinOps workflows with per-unit costs, showbacks, chargebacks, and margin analysis per customer.
    humanURL: https://docs.amberflo.io/reference/cloud-cost-tracking
    baseURL: https://app.amberflo.io
    tags:
      - Cost Tracking
      - FinOps
      - Cloud Cost Management
      - Budgets
    properties:
      - type: Documentation
        url: https://docs.amberflo.io/reference/cloud-cost-tracking
      - type: APIReference
        url: https://docs.amberflo.io/reference/cloud-cost-tracking
  - aid: amberflo:ai-gateway-api
    name: Amberflo AI Gateway API
    description: The Amberflo AI Gateway provides a unified API for routing requests to 1,500+ LLM models with intelligent model routing, cost optimization, built-in fallbacks, and MCP server traffic monitoring. It tracks LLM model rates and metrics for AI cost governance.
    humanURL: https://docs.amberflo.io/docs/ai-gateway
    baseURL: https://app.amberflo.io
    tags:
      - AI Gateway
      - LLM
      - Model Routing
      - AI Cost Management
    properties:
      - type: Documentation
        url: https://docs.amberflo.io/docs/ai-gateway
common:
  - type: Website
    url: https://www.amberflo.io/
  - type: Documentation
    url: https://docs.amberflo.io/
  - type: DeveloperPortal
    url: https://docs.amberflo.io/
  - type: GettingStarted
    url: https://docs.amberflo.io/docs/quick-start
  - type: APIReference
    url: https://docs.amberflo.io/reference/
  - type: SignUp
    url: https://ui.amberflo.io/cGxnLXNpZ251cA==
  - type: Login
    url: https://ui.amberflo.io/login
  - type: Pricing
    url: https://www.amberflo.io/pricing
  - type: Blog
    url: https://www.amberflo.io/resources/blog
  - type: TermsOfService
    url: https://www.amberflo.io/legal/terms-and-condition
  - type: PrivacyPolicy
    url: https://www.amberflo.io/legal/privacy-policy
  - type: Compliance
    url: https://trust.amberflo.io/
  - type: TrustCenter
    url: https://trust.amberflo.io/
  - type: GitHubOrganization
    url: https://github.com/amberflo
  - type: SDK
    url: https://pypi.org/project/amberflo-metering-python/
    title: Python SDK
  - type: SDK
    url: https://github.com/amberflo/metering-typescript
    title: TypeScript SDK
  - type: SDK
    url: https://github.com/amberflo/metering-go
    title: Go SDK
  - type: SpectralRules
    url: https://raw.githubusercontent.com/api-evangelist/amberflo/refs/heads/main/rules/amberflo-spectral-rules.yml
  - type: NaftikoCapability
    url: https://raw.githubusercontent.com/api-evangelist/amberflo/refs/heads/main/capabilities/usage-based-monetization.yaml
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/amberflo/refs/heads/main/vocabulary/amberflo-vocabulary.yaml
  - type: Features
    data:
      - name: Real-Time Event Ingestion
        description: Ingest millions to billions of high-cardinality usage events in real time with idempotency, deduplication, and automatic aggregation.
      - name: AI Cost Management
        description: Unified LLM access and control across 1,500+ models with per-unit costs, rollups, budgets, Cost Guards, and margin analysis per customer.
      - name: AI Gateway and Model Routing
        description: Single API for multiple LLM providers with intelligent cost optimization, automatic retries, fallbacks, and MCP server traffic monitoring.
      - name: Usage-Based Billing
        description: Flexible billing models including usage-based, token-based, seat-based, fixed fee, and outcome-based pricing with multi-currency support and automated invoicing.
      - name: Embeddable Billing Dashboards
        description: Customer-facing billing portals and dashboards via a React.js UI Kit with custom domain support and SSO integration.
      - name: Revenue Operations
        description: Revenue recognition automation, RevRec ledger tracking, tax management, and integrations with Stripe and NetSuite.
      - name: Budget Management
        description: Spending limits, threshold alerts, Cost Guards, and automated notifications for cloud and AI cost governance.
      - name: Chargeback and Showback
        description: Chargeback rates, quotes, and invoices for internal cost allocation and showback reporting across business units.
  - type: UseCases
    data:
      - name: API Monetization
        description: Meter API usage and automatically bill customers based on calls, tokens, or custom events with flexible pricing models.
      - name: AI Cost Governance
        description: Track and govern LLM spending across teams and customers with budgets, alerts, and per-customer cost attribution.
      - name: SaaS Billing Automation
        description: Automate end-to-end billing for SaaS products with usage-based pricing plans, invoicing, and customer portals.
      - name: Cloud FinOps
        description: Allocate and showback cloud costs to business units and customers using automated cost allocation rules and chargeback workflows.
      - name: Customer Cost Transparency
        description: Provide customers with real-time visibility into their usage and costs via embedded dashboards and billing portals.
      - name: Usage Analytics and Reporting
        description: Query and analyze usage data in real time with batch and sparse query modes, raw event queries, and revenue calculation analytics.
  - type: Integrations
    data:
      - name: Stripe
        description: Native integration with Stripe for payment processing and revenue operations workflows.
      - name: NetSuite
        description: Integration with NetSuite for revenue recognition and financial reporting.
      - name: Kong
        description: Official Kong plugin for metering API requests handled by Kong instances and monetizing APIs.
      - name: AWS SaaS Builder Toolkit
        description: Integration with AWS SaaS Builder Toolkit for SaaS billing and metering best practices on AWS.
      - name: LiteLLM
        description: Logging callback for LiteLLM to meter LLM usage and monitor AI costs.
      - name: AWS Lambda
        description: Examples and utilities for metering AWS Lambda function invocations.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
