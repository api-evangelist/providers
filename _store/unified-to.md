---
aid: unified-to
url: https://raw.githubusercontent.com/api-evangelist/unified-to/refs/heads/main/apis.yml
apis:
  - aid: unified-to:unified-to
    name: Unified.to
    tags:
      - Integrations
      - Unified API
    humanURL: https://unified.to/
    properties:
      - url: https://unified.to/
        type: Documentation
    description: Unified APIs for HR, ATS, CRM & Authentication. One API to access 360+ integrations across 22 categories with real-time pass-through architecture.
  - aid: unified-to:accounting-api
    name: Unified.to Accounting API
    tags:
      - Accounting
      - Financial
      - Invoices
      - Payments
    humanURL: https://unified.to/accounting
    properties:
      - url: https://unified.to/accounting
        type: Documentation
      - url: https://docs.unified.to/accounting/overview
        type: Documentation
      - url: https://raw.githubusercontent.com/api-evangelist/unified-to/refs/heads/main/openapi/unified-to-accounting-openapi.yaml
        type: OpenAPI
      - url: https://raw.githubusercontent.com/api-evangelist/unified-to/refs/heads/main/json-schema/unified-to-accounting-account-schema.json
        type: JSONSchema
      - url: https://raw.githubusercontent.com/api-evangelist/unified-to/refs/heads/main/json-schema/unified-to-accounting-invoice-schema.json
        type: JSONSchema
      - url: https://raw.githubusercontent.com/api-evangelist/unified-to/refs/heads/main/json-schema/unified-to-accounting-transaction-schema.json
        type: JSONSchema
    description: Unified accounting API providing real-time access to accounting data across 41 integrations including QuickBooks, Xero, FreshBooks, and more.
  - aid: unified-to:ads-api
    name: Unified.to Advertising API
    tags:
      - Ads
      - Advertising
      - Marketing
    humanURL: https://unified.to/ads
    properties:
      - url: https://unified.to/ads
        type: Documentation
      - url: https://docs.unified.to/ads/overview
        type: Documentation
      - url: https://raw.githubusercontent.com/api-evangelist/unified-to/refs/heads/main/openapi/unified-to-marketing-openapi.yaml
        type: OpenAPI
    description: Unified advertising API providing real-time access to advertising platform data across 13 integrations.
  - aid: unified-to:assessment-api
    name: Unified.to Assessment API
    tags:
      - Assessment
      - Evaluation
      - Testing
    humanURL: https://unified.to/assessment
    properties:
      - url: https://unified.to/assessment
        type: Documentation
      - url: https://raw.githubusercontent.com/api-evangelist/unified-to/refs/heads/main/openapi/unified-to-hr-talent-openapi.yaml
        type: OpenAPI
    description: Unified assessment API providing real-time access to assessment and evaluation data across 6 integrations.
  - aid: unified-to:ats-api
    name: Unified.to ATS API
    tags:
      - Applicant Tracking
      - ATS
      - Hiring
      - Recruiting
    humanURL: https://unified.to/ats
    properties:
      - url: https://unified.to/ats
        type: Documentation
      - url: https://docs.unified.to/ats/overview
        type: Documentation
      - url: https://raw.githubusercontent.com/api-evangelist/unified-to/refs/heads/main/openapi/unified-to-ats-openapi.yaml
        type: OpenAPI
      - url: https://raw.githubusercontent.com/api-evangelist/unified-to/refs/heads/main/json-schema/unified-to-ats-job-schema.json
        type: JSONSchema
      - url: https://raw.githubusercontent.com/api-evangelist/unified-to/refs/heads/main/json-schema/unified-to-ats-candidate-schema.json
        type: JSONSchema
      - url: https://raw.githubusercontent.com/api-evangelist/unified-to/refs/heads/main/json-schema/unified-to-ats-application-schema.json
        type: JSONSchema
      - url: https://raw.githubusercontent.com/api-evangelist/unified-to/refs/heads/main/examples/unified-to-list-ats-jobs-example.json
        type: Example
    description: Unified ATS API providing real-time access to recruiting data including jobs, candidates, applications, interviews, and hiring decisions across 73 integrations.
  - aid: unified-to:auth-api
    name: Unified.to Authentication API
    tags:
      - Authentication
      - Identity
      - Login
      - OAuth
    humanURL: https://unified.to/auth
    properties:
      - url: https://docs.unified.to/auth/overview
        type: Documentation
      - url: https://docs.unified.to/auth/integrations
        type: Documentation
    description: Unified authentication API supporting OAuth 2 OpenID with 140+ identity provider integrations for adding user logins and signups.
  - aid: unified-to:calendar-api
    name: Unified.to Calendar & Meetings API
    tags:
      - Calendar
      - Meetings
      - Scheduling
    humanURL: https://unified.to/calendar
    properties:
      - url: https://unified.to/calendar
        type: Documentation
      - url: https://raw.githubusercontent.com/api-evangelist/unified-to/refs/heads/main/openapi/unified-to-productivity-openapi.yaml
        type: OpenAPI
      - url: https://raw.githubusercontent.com/api-evangelist/unified-to/refs/heads/main/json-schema/unified-to-calendar-event-schema.json
        type: JSONSchema
    description: Unified calendar and meetings API providing real-time access to calendar and scheduling data across 27 integrations.
  - aid: unified-to:call-center-api
    name: Unified.to Call Center API
    tags:
      - Call Center
      - Communications
      - Voice
    humanURL: https://unified.to/uc
    properties:
      - url: https://unified.to/uc
        type: Documentation
      - url: https://raw.githubusercontent.com/api-evangelist/unified-to/refs/heads/main/openapi/unified-to-it-ops-openapi.yaml
        type: OpenAPI
    description: Unified call center API providing real-time access to calls, contacts, recordings, and voice activity data across 16 integrations.
  - aid: unified-to:crm-api
    name: Unified.to CRM API
    tags:
      - Contacts
      - CRM
      - Deals
      - Sales
    humanURL: https://unified.to/crm
    properties:
      - url: https://unified.to/crm
        type: Documentation
      - url: https://docs.unified.to/crm/overview
        type: Documentation
      - url: https://raw.githubusercontent.com/api-evangelist/unified-to/refs/heads/main/openapi/unified-to-crm-openapi.yaml
        type: OpenAPI
      - url: https://raw.githubusercontent.com/api-evangelist/unified-to/refs/heads/main/json-schema/unified-to-crm-contact-schema.json
        type: JSONSchema
      - url: https://raw.githubusercontent.com/api-evangelist/unified-to/refs/heads/main/json-schema/unified-to-crm-company-schema.json
        type: JSONSchema
      - url: https://raw.githubusercontent.com/api-evangelist/unified-to/refs/heads/main/json-schema/unified-to-crm-deal-schema.json
        type: JSONSchema
      - url: https://raw.githubusercontent.com/api-evangelist/unified-to/refs/heads/main/examples/unified-to-list-crm-contacts-example.json
        type: Example
    description: Unified CRM API providing real-time access to customer relationship data including contacts, companies, deals, pipelines, leads, and activities across 47 integrations.
  - aid: unified-to:ecommerce-api
    name: Unified.to E-Commerce API
    tags:
      - E-Commerce
      - Orders
      - Products
      - Shopping
    humanURL: https://unified.to/ecommerce
    properties:
      - url: https://unified.to/ecommerce
        type: Documentation
      - url: https://raw.githubusercontent.com/api-evangelist/unified-to/refs/heads/main/openapi/unified-to-commerce-openapi.yaml
        type: OpenAPI
      - url: https://raw.githubusercontent.com/api-evangelist/unified-to/refs/heads/main/json-schema/unified-to-commerce-item-schema.json
        type: JSONSchema
      - url: https://raw.githubusercontent.com/api-evangelist/unified-to/refs/heads/main/json-schema/unified-to-commerce-review-schema.json
        type: JSONSchema
    description: Unified e-commerce API providing real-time access to e-commerce data across 30 integrations.
  - aid: unified-to:hris-api
    name: Unified.to HR & Directory API
    tags:
      - Directory
      - HR
      - HRIS
      - Payroll
    humanURL: https://unified.to/hris
    properties:
      - url: https://unified.to/hris
        type: Documentation
      - url: https://docs.unified.to/hris/overview
        type: Documentation
      - url: https://raw.githubusercontent.com/api-evangelist/unified-to/refs/heads/main/openapi/unified-to-hris-openapi.yaml
        type: OpenAPI
      - url: https://raw.githubusercontent.com/api-evangelist/unified-to/refs/heads/main/json-schema/unified-to-hris-employee-schema.json
        type: JSONSchema
      - url: https://raw.githubusercontent.com/api-evangelist/unified-to/refs/heads/main/examples/unified-to-create-hris-employee-example.json
        type: Example
    description: Unified HR and directory API providing real-time access to HR, payroll, and employee directory data across 223 integrations.
  - aid: unified-to:messaging-api
    name: Unified.to Messaging API
    tags:
      - Chat
      - Communication
      - Messaging
    humanURL: https://unified.to/messaging
    properties:
      - url: https://unified.to/messaging
        type: Documentation
      - url: https://raw.githubusercontent.com/api-evangelist/unified-to/refs/heads/main/openapi/unified-to-productivity-openapi.yaml
        type: OpenAPI
    description: Unified messaging API providing real-time access to messaging and chat data across 17 integrations.
  - aid: unified-to:payment-api
    name: Unified.to Payments API
    tags:
      - Billing
      - Payments
      - Transactions
    humanURL: https://unified.to/payment
    properties:
      - url: https://unified.to/payment
        type: Documentation
      - url: https://docs.unified.to/payment/overview
        type: Documentation
      - url: https://raw.githubusercontent.com/api-evangelist/unified-to/refs/heads/main/openapi/unified-to-it-ops-openapi.yaml
        type: OpenAPI
    description: Unified payments API providing real-time access to transaction, refund, payout, and subscription data across 16 integrations.
  - aid: unified-to:ticketing-api
    name: Unified.to Ticketing API
    tags:
      - Help Desk
      - Support
      - Ticketing
    humanURL: https://unified.to/ticketing
    properties:
      - url: https://unified.to/ticketing
        type: Documentation
      - url: https://docs.unified.to/ticketing/overview
        type: Documentation
      - url: https://raw.githubusercontent.com/api-evangelist/unified-to/refs/heads/main/openapi/unified-to-it-ops-openapi.yaml
        type: OpenAPI
    description: Unified ticketing API providing real-time access to support ticket and issue resolution data across 7 integrations.
name: Unified.to
tags:
  - Integrations
  - Unified API
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-01-02'
modified: '2026-05-04'
position: Consuming
segments:
  - Unified_API
description: Unified is a real-time unified API platform that provides access to over 360 integrations across 22 categories for B2B SaaS and AI-native products. Unlike traditional integration platforms that cache or sync data periodically, Unified operates with a pass-through architecture where every request hits the source API live, ensuring no stale data and eliminating the need for storage of customer information.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
common:
  - name: Unified.to — Unified APIs for HR, ATS, CRM & Authentication
    url: https://unified.to/
    type: Website
  - name: Blog | Unified.to
    url: https://unified.to/blog
    type: Blog
  - name: Unified.to Security
    url: https://unified.to/security
    type: Security
  - name: Changelog | Unified.to
    url: https://unified.to/changelog
    type: ChangeLog
  - name: Pricing | Unified.to
    url: https://unified.to/pricing
    type: Pricing
  - name: Unified.to Documentation
    url: https://docs.unified.to/intro
    type: Documentation
  - name: About Unified.to
    url: https://unified.to/about
    type: About
  - name: Unified.to Getting Started
    url: https://docs.unified.to/quick-start
    type: GettingStarted
  - name: Unified.to How-to Guides
    url: https://docs.unified.to/guides
    type: Guides
  - name: Unified.to Login
    url: https://app.unified.to/login
    type: Login
  - name: Unified.to Sign Up
    url: https://app.unified.to
    type: SignUp
  - name: Unified.to Integrations
    url: https://unified.to/integrations
    type: Integrations
  - name: Unified.to Status Page
    url: https://status.unified.to
    type: StatusPage
  - name: Unified.to Privacy Policy
    url: https://unified.to/privacy
    type: PrivacyPolicy
  - name: Unified.to Terms of Service
    url: https://unified.to/tos
    type: TermsOfService
  - name: Unified.to Support
    url: https://unified.to/support
    type: Support
  - name: Unified.to Trust Center
    url: https://app.mycroft.io/trust/unified-to
    type: TrustCenter
  - name: Unified.to Full OpenAPI Specification (YAML)
    url: https://api.unified.to/openapi.yaml
    type: OpenAPI
  - name: Unified.to Full OpenAPI Specification (JSON)
    url: https://api.unified.to/openapi.json
    type: OpenAPI
  - name: Unified.to Swagger 2.0 Specification
    url: https://api.unified.to/swagger.json
    type: Swagger
  - name: Unified.to Postman Collection
    url: https://api.unified.to/collection.json
    type: PostmanCollection
  - name: Unified.to TypeScript SDK
    url: https://www.npmjs.com/package/@unified-api/typescript-sdk
    type: SDK
  - name: Unified.to Python SDK
    url: https://github.com/unified-to/unified-python-sdk
    type: SDK
  - name: Unified.to PHP SDK
    url: https://github.com/unified-to/unified-php-sdk
    type: SDK
  - name: Unified.to Java SDK
    url: https://central.sonatype.com/artifact/to.unified/unified-java-sdk
    type: SDK
  - name: Unified.to Go SDK
    url: https://github.com/unified-to/unified-go-sdk
    type: SDK
  - name: Unified.to C# SDK
    url: https://www.nuget.org/packages/UnifiedTo
    type: SDK
  - name: Unified.to Ruby SDK
    url: https://github.com/unified-to/unified-ruby-sdk
    type: SDK
  - name: Unified.to GitHub Organization
    url: https://github.com/unified-to
    type: GitHubOrganization
  - name: Unified.to Discord Community
    url: https://discord.gg/85z7HF7JbD
    type: Discord
  - name: Unified.to LinkedIn
    url: https://www.linkedin.com/company/unified-to/
    type: LinkedIn
  - name: Unified.to YouTube Channel
    url: https://www.youtube.com/@unified_api
    type: YouTube
  - name: Unified.to MCP Server
    url: https://unified.to/mcp
    type: MCP
  - name: Unified.to CLI
    url: https://github.com/unified-to/unified-cli
    type: CLI
  - name: Unified.to Spectral Rules
    url: https://raw.githubusercontent.com/api-evangelist/unified-to/refs/heads/main/rules/unified-to-spectral-rules.yml
    type: SpectralRules
  - name: Unified.to Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/unified-to/refs/heads/main/vocabulary/unified-to-vocabulary.yaml
    type: Vocabulary
  - name: Unified.to Sales and CRM Capability
    url: https://raw.githubusercontent.com/api-evangelist/unified-to/refs/heads/main/capabilities/sales-and-crm.yaml
    type: NaftikoCapability
  - name: Unified.to HR and Talent Capability
    url: https://raw.githubusercontent.com/api-evangelist/unified-to/refs/heads/main/capabilities/hr-and-talent.yaml
    type: NaftikoCapability
  - name: Unified.to Financial Operations Capability
    url: https://raw.githubusercontent.com/api-evangelist/unified-to/refs/heads/main/capabilities/financial-operations.yaml
    type: NaftikoCapability
  - name: Unified.to JSON-LD Context
    url: https://raw.githubusercontent.com/api-evangelist/unified-to/refs/heads/main/json-ld/unified-to-context.jsonld
    type: JSON-LD
  - name: Unified.to Features
    type: Features
    data:
      - 'Grow $750/mo: 750K API calls, unlimited customer connections'
      - 'Pro $1,250/mo: 1.25M API calls, SAML SSO, secrets manager'
      - 'Scale $3,000/mo: 6M API calls, $0.50/1K overages, 24/7 support, HIPAA BAA'
      - 'Enterprise custom: single-tenant / private cloud'
      - 445+ integrations across 26+ unified APIs
      - Virtual webhooks + database sync
      - 'Categories: HRIS, ATS, CRM, Accounting, Storage, Ticketing, Commerce, Marketing, Auth, Email, Calendar, Messaging, etc.'
      - 'REST API: 100 req/sec/workspace'
      - 'Webhook deliveries: 50 req/sec/endpoint'
      - 'Bulk: 100 items/request'
      - 365+ day log retention on Scale
      - API CNAME (Grow+) and Auth CNAME (Pro+)
      - OAuth handled per integration
      - Bearer token + workspace API keys
      - SOC 2 Type 2
      - Self-hosted option (Enterprise)
    sources:
      - https://www.unified.to/pricing
    updated: '2026-05-04'
  - name: Unified.to Use Cases
    type: UseCases
    data:
      - name: CRM Integration
        description: Sync contacts, companies, and deals across 47 CRM platforms with a single API integration.
      - name: HR System Integration
        description: Read and write employee, payroll, and organizational data across 223 HRIS and directory integrations.
      - name: Recruiting Automation
        description: Automate ATS workflows — publish jobs, track applications, and schedule interviews across 73 ATS platforms.
      - name: Accounting Automation
        description: Create invoices, sync transactions, and manage chart of accounts across 41 accounting platforms.
      - name: AI Agent Integration
        description: Provide AI agents with access to customer CRM, HR, accounting, and support data via the MCP server.
  - name: Unified.to Integrations
    type: Integrations
    data:
      - name: Salesforce
        description: CRM integration for contacts, companies, and deals via unified CRM API
      - name: HubSpot
        description: CRM and marketing automation integration
      - name: Workday
        description: HRIS integration for employee and organizational data
      - name: BambooHR
        description: HR management platform integration
      - name: Greenhouse
        description: ATS integration for jobs, candidates, and applications
      - name: QuickBooks
        description: Accounting integration for invoices, transactions, and chart of accounts
      - name: Xero
        description: Accounting integration for financial management
      - name: Shopify
        description: E-commerce integration for orders, products, and inventory
---
