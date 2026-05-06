---
aid: blissfully
name: Blissfully
description: Blissfully was a SaaS management platform providing SaaS discovery, spend optimization, and workflow automation for IT and finance teams. Blissfully was acquired by Vendr in 2022 and integrated into the Vendr platform. Vendr is now a leading SaaS buying and management platform that helps companies control software spend through vendor negotiations, pricing intelligence, and procurement automation. The Vendr API provides access to software catalog data, pricing intelligence, and scope management capabilities.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Procurement
  - SaaS Discovery
  - SaaS Management
  - Software Procurement
  - Spend Optimization
  - Vendor Management
url: https://raw.githubusercontent.com/api-evangelist/blissfully/refs/heads/main/apis.yml
created: '2026-03-27'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: blissfully:vendr-catalog-api
    name: Vendr Catalog API
    description: Provides structured product catalog attributes derived from thousands of unstructured software quotes. Enables buyers to understand product breadth, available add-ons, pricing tiers, and feature comparisons across the Vendr software catalog.
    humanURL: https://developers.vendr.com
    tags:
      - Procurement
      - SaaS Management
      - Software Catalog
    properties:
      - type: Documentation
        url: https://developers.vendr.com
      - type: OpenAPI
        url: openapi/blissfully-vendr-catalog-api-openapi.yaml
  - aid: blissfully:vendr-pricing-api
    name: Vendr Pricing API
    description: Delivers actionable pricing insights including fair price predictions and negotiation guidance tailored to the buyer's specific requirements, contract size, and vendor relationship. Powered by Vendr's database of real software purchases and negotiated prices.
    humanURL: https://developers.vendr.com
    tags:
      - Pricing
      - Procurement
      - SaaS Management
    properties:
      - type: Documentation
        url: https://developers.vendr.com
  - aid: blissfully:vendr-scope-api
    name: Vendr Scope API
    description: Enables communication of detailed purchasing needs in text or file format, whether for complex enterprise software requirements or uploaded quotes from vendors. Supports both simple and complex procurement scope definitions.
    humanURL: https://developers.vendr.com
    tags:
      - Procurement
      - SaaS Management
      - Scope
    properties:
      - type: Documentation
        url: https://developers.vendr.com
  - aid: blissfully:vendr-webhooks-api
    name: Vendr Webhooks API
    description: Facilitates creation and management of webhooks for monitoring Vendr's data processing events, enabling integration with procurement workflows and notification systems.
    humanURL: https://developers.vendr.com
    tags:
      - Procurement
      - SaaS Management
      - Webhooks
    properties:
      - type: Documentation
        url: https://developers.vendr.com
common:
  - type: Website
    url: https://www.vendr.com
  - type: Documentation
    url: https://developers.vendr.com
  - type: SignUp
    url: https://www.vendr.com/demo
  - type: TermsOfService
    url: https://www.vendr.com/legal/terms-of-service
  - type: PrivacyPolicy
    url: https://www.vendr.com/legal/privacy-policy
  - type: Blog
    url: https://www.vendr.com/blog
  - type: RateLimits
    data:
      - name: Requests Per Minute
        description: Maximum 250 requests per minute
        limit: 250
        window: 1 minute
      - name: Daily Quota
        description: Maximum 150,000 requests per day
        limit: 150000
        window: 1 day
  - type: Authentication
    url: https://developers.vendr.com
  - type: Features
    data:
      - name: Catalog API
        description: Structured product catalog attributes derived from thousands of unstructured software quotes, covering product breadth, add-ons, and feature comparisons.
      - name: Pricing API
        description: Actionable pricing insights including fair price predictions and negotiation guidance tailored to specific buyer requirements and contract sizes.
      - name: Scope API
        description: Communication of detailed purchasing needs in text or file format for complex enterprise software procurement requirements.
      - name: Webhooks API
        description: Creation and management of webhooks for monitoring Vendr data processing events and integrating with procurement workflows.
      - name: MCP Integration
        description: Model Context Protocol (MCP) integration options including Claude Desktop extension, GitHub-based local setup, and custom AI app configuration.
      - name: SaaS Benchmarking
        description: Pricing benchmarks powered by Vendr's database of real software purchases across thousands of companies and vendors.
  - type: UseCases
    data:
      - name: Software Pricing Intelligence
        description: Procurement teams access fair price benchmarks and negotiation guidance before and during software vendor negotiations.
      - name: SaaS Spend Optimization
        description: Finance and IT teams gain visibility into software spend and identify optimization opportunities across the SaaS portfolio.
      - name: AI-Powered Procurement
        description: AI applications integrate Vendr catalog and pricing data via MCP or API to provide intelligent software procurement recommendations.
      - name: Vendor Management Integration
        description: Enterprise procurement platforms integrate Vendr data to enrich vendor records with pricing benchmarks and product catalog attributes.
      - name: Contract Renewal Automation
        description: Webhook integrations notify procurement workflows of contract renewal events and pricing change signals from the Vendr platform.
  - type: Integrations
    data:
      - name: Claude Desktop
        description: Native MCP extension for Claude Desktop enabling AI-assisted software procurement research directly in the Claude interface.
      - name: Slack
        description: Vendr integrates with Slack for procurement workflow notifications and team collaboration on software purchases.
      - name: Salesforce
        description: CRM integration enabling sales teams to access vendor and software catalog data within Salesforce.
      - name: NetSuite
        description: ERP integration for automated purchase order creation and financial tracking of SaaS spend through Vendr.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
