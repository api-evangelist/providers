---
aid: merge
url: https://raw.githubusercontent.com/api-evangelist/merge/refs/heads/main/apis.yml
apis:
  - aid: merge:merge
    name: Merge
    tags:
      - Integrations
      - Platform
      - Unified API
    humanURL: ' https://www.merge.dev/'
    properties:
      - url: ' https://www.merge.dev/'
        type: Documentation
    description: Merge is the leading provider of customer-facing integrations for frontier LLMs, Fortune 500 organizations, and thousands of other B2B SaaS companies.
  - aid: merge:hris-api
    name: Merge HRIS API
    tags:
      - Directory
      - HRIS
      - Human Resources
      - Payroll
      - Unified API
    humanURL: https://www.merge.dev/categories/hr-payroll-api
    properties:
      - url: https://www.merge.dev/categories/hr-payroll-api
        type: Website
      - url: https://docs.merge.dev/hris/
        type: Documentation
      - url: openapi/merge-hris-api-openapi.yaml
        type: OpenAPI
      - url: json-schema/hris-api-employee-schema.json
        type: JSONSchema
      - url: json-structure/hris-api-employee-structure.json
        type: JSONStructure
      - url: json-ld/merge-hris-api-context.jsonld
        type: JSONLD
      - url: examples/hris-api-employee-example.json
        type: Example
    description: Merge HRIS API provides a unified interface to integrate every HR, payroll, and SCIM directory system with one API. It normalizes data across 80+ HR platforms including Workday, BambooHR, Gusto, Rippling, ADP, and many more, enabling developers to deliver integrations in days instead of quarters.
  - aid: merge:ats-api
    name: Merge ATS API
    tags:
      - Applicant Tracking
      - ATS
      - Recruiting
      - Unified API
    humanURL: https://www.merge.dev/categories/ats-recruiting-api
    properties:
      - url: https://www.merge.dev/categories/ats-recruiting-api
        type: Website
      - url: https://docs.merge.dev/ats/
        type: Documentation
      - url: openapi/merge-ats-api-openapi.yaml
        type: OpenAPI
      - url: json-schema/ats-api-candidate-schema.json
        type: JSONSchema
      - url: json-schema/ats-api-application-schema.json
        type: JSONSchema
      - url: json-structure/ats-api-candidate-structure.json
        type: JSONStructure
      - url: json-ld/merge-ats-api-context.jsonld
        type: JSONLD
      - url: examples/ats-api-candidate-example.json
        type: Example
      - url: examples/ats-api-application-example.json
        type: Example
    description: Merge ATS API enables connection to every applicant tracking system with one API. It provides standardized data schemas for candidates, applications, interviews, and job postings across 50+ recruiting platforms including Greenhouse, Lever, Workday, iCIMS, and Jobvite.
  - aid: merge:accounting-api
    name: Merge Accounting API
    tags:
      - Accounting
      - Finance
      - Unified API
    humanURL: https://www.merge.dev/categories/accounting-api
    properties:
      - url: https://www.merge.dev/categories/accounting-api
        type: Website
      - url: https://docs.merge.dev/accounting/overview/
        type: Documentation
      - url: openapi/merge-accounting-api-openapi.yaml
        type: OpenAPI
      - url: json-schema/accounting-api-invoice-schema.json
        type: JSONSchema
      - url: json-structure/accounting-api-invoice-structure.json
        type: JSONStructure
      - url: json-ld/merge-accounting-api-context.jsonld
        type: JSONLD
      - url: examples/accounting-api-invoice-example.json
        type: Example
    description: Merge Accounting API provides a unified API for accounting integrations, enabling read and write access to financial data across major accounting systems including QuickBooks Online, Xero, NetSuite, and Sage Intacct. It supports journal entries, payments, invoices, and other financial transaction data.
  - aid: merge:ticketing-api
    name: Merge Ticketing API
    tags:
      - Project Management
      - Ticketing
      - Unified API
    humanURL: https://www.merge.dev/categories/ticketing-api
    properties:
      - url: https://www.merge.dev/categories/ticketing-api
        type: Website
      - url: https://docs.merge.dev/ticketing/overview/
        type: Documentation
      - url: openapi/merge-ticketing-api-openapi.yaml
        type: OpenAPI
      - url: json-schema/ticketing-api-ticket-schema.json
        type: JSONSchema
      - url: json-structure/ticketing-api-ticket-structure.json
        type: JSONStructure
      - url: json-ld/merge-ticketing-api-context.jsonld
        type: JSONLD
      - url: examples/ticketing-api-ticket-example.json
        type: Example
    description: Merge Ticketing API provides unified access to 30+ ticketing and project management systems including Jira, Asana, Linear, Zendesk, Freshdesk, GitHub Issues, and ServiceNow. It normalizes ticketing data objects including tickets, comments, attachments, contacts, teams, and tags with read and write capabilities.
  - aid: merge:crm-api
    name: Merge CRM API
    tags:
      - CRM
      - Customer Relationship Management
      - Unified API
    humanURL: https://www.merge.dev/categories/crm-api
    properties:
      - url: https://www.merge.dev/categories/crm-api
        type: Website
      - url: https://docs.merge.dev/crm/overview/
        type: Documentation
      - url: openapi/merge-crm-api-openapi.yaml
        type: OpenAPI
      - url: json-schema/crm-api-opportunity-schema.json
        type: JSONSchema
      - url: json-structure/crm-api-opportunity-structure.json
        type: JSONStructure
      - url: json-ld/merge-crm-api-context.jsonld
        type: JSONLD
      - url: examples/crm-api-opportunity-example.json
        type: Example
    description: Merge CRM API provides unified access to 20+ CRM platforms including Salesforce, HubSpot, Pipedrive, and Zoho CRM. It offers read and write capabilities for standardized CRM data objects such as Accounts, Contacts, Leads, Opportunities, and Engagements, along with custom object support.
  - aid: merge:file-storage-api
    name: Merge File Storage API
    tags:
      - Documents
      - File Storage
      - Unified API
    humanURL: https://www.merge.dev/categories/file-storage-api
    properties:
      - url: https://www.merge.dev/categories/file-storage-api
        type: Website
      - url: https://docs.merge.dev/filestorage/
        type: Documentation
      - url: openapi/merge-file-storage-api-openapi.yaml
        type: OpenAPI
      - url: json-schema/file-storage-api-file-schema.json
        type: JSONSchema
      - url: json-structure/file-storage-api-file-structure.json
        type: JSONStructure
      - url: json-ld/merge-file-storage-api-context.jsonld
        type: JSONLD
      - url: examples/file-storage-api-file-example.json
        type: Example
    description: Merge File Storage API provides unified access to file storage platforms including Box, Dropbox, Google Drive, OneDrive, and SharePoint. It normalizes access to Drives, Files, Folders, Groups, and Users with a built-in File Picker component for browsing connected storage accounts.
  - aid: merge:knowledge-base-api
    name: Merge Knowledge Base API
    tags:
      - Content Management
      - Knowledge Base
      - Unified API
    humanURL: https://www.merge.dev/categories/knowledge-base
    properties:
      - url: https://www.merge.dev/categories/knowledge-base
        type: Website
      - url: https://docs.merge.dev/knowledgebase/overview/
        type: Documentation
    description: Merge Knowledge Base API provides unified access to knowledge base platforms including Confluence and Notion. It normalizes access to Articles, Attachments, Containers, Groups, and Users, with ACL management that maps users, groups, and company-level permissions across platforms for enterprise AI context and search.
  - aid: merge:chat-api
    name: Merge Chat API
    tags:
      - Chat
      - Messaging
      - Unified API
    humanURL: https://www.merge.dev/categories/chat
    properties:
      - url: https://www.merge.dev/categories/chat
        type: Website
    description: Merge Chat Unified API provides real-time, normalized access to chat and messaging platforms including Microsoft Teams, with Slack on the roadmap. It normalizes five core object types including Messages, Conversations, Users, Groups, and Members, enabling enterprise search, context-aware AI agents, and near-real-time insights.
  - aid: merge:agent-handler
    name: Merge Agent Handler
    tags:
      - AI Agents
      - Integrations
      - MCP
      - Tool Use
    humanURL: https://www.merge.dev/merge-agent-handler
    properties:
      - url: https://www.merge.dev/merge-agent-handler
        type: Website
      - url: https://docs.ah.merge.dev/Overview/Agent-Handler-intro
        type: Documentation
      - url: https://help.ah.merge.dev/
        type: Support
    description: Merge Agent Handler enables AI agents to connect with thousands of pre-built tools for taking real-time actions. It manages authentication, rate limits, error handling, and provides security controls that scan tool inputs and responses for sensitive data to prevent data misuse.
name: Merge
tags:
  - Integrations
  - Platform
  - Unified API
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2025-06-05'
modified: '2026-05-04'
position: Consuming
segments:
  - Unified_API
description: Merge is a Unified API that offers developers the ability to embed customer-facing API integrations in their products without the need to configure on a per-integration basis. With this integration, you can build and manage the integration with Recruitee in Merge's developer portal.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
common:
  - name: Merge - One Unified API for all HR, Payroll, Accounting, Ticketing, CRM, ATS, and File Storage Integrations.
    description: 'null'
    url: https://www.merge.dev/
    type: Website
  - name: Security At Merge
    description: 'null'
    url: https://www.merge.dev/security
    type: Security
  - name: Merge Case Studies
    description: 'null'
    url: https://www.merge.dev/case-studies
    type: Customers
  - name: The Merge Blog
    description: 'null'
    url: https://www.merge.dev/blog
    type: Blog
  - name: Resources
    description: 'null'
    url: https://www.merge.dev/resources?content-type=Ebooks
    type: eBooks
  - name: Merge Help Center
    description: 'null'
    url: https://help.merge.dev/
    type: Support
  - name: Merge Changelog
    description: 'null'
    url: https://www.merge.dev/changelog
    type: ChangeLog
  - name: Resources
    description: 'null'
    url: https://www.merge.dev/resources?content-type=Webinars
    type: Webinars
  - name: Merge Pricing
    description: 'null'
    url: https://www.merge.dev/pricing
    type: Pricing
  - name: Merge Docs
    description: 'null'
    url: https://docs.merge.dev/?_gl=1*1llee1i*_gcl_au*MTY4MjQ4NzcxMy4xNzUyNjE4Mjgw*_ga*MTY0NjYzNTAyLjE3NTI2MTgyODA.*_ga_S6X9VBDBJN*czE3NTI2MTgyODAkbzEkZzEkdDE3NTI2MTg0NTMkajI3JGwwJGgw
    type: Documentation
  - name: Terms of Use
    description: 'null'
    url: https://www.merge.dev/legal/terms
    type: TermsOfService
  - name: Privacy Policy
    description: 'null'
    url: https://www.merge.dev/legal/privacy-policy
    type: PrivacyPolicy
  - name: 'Merge for EU: Build integrations while complying with GDPR'
    description: 'null'
    url: https://www.merge.dev/eu
    type: GDPR
  - name: Merge
    description: 'null'
    url: https://app.merge.dev/login?_gl=1*6bfh40*_gcl_au*MTY4MjQ4NzcxMy4xNzUyNjE4Mjgw*_ga*MTY0NjYzNTAyLjE3NTI2MTgyODA.*_ga_S6X9VBDBJN*czE3NTI2MTgyODAkbzEkZzEkdDE3NTI2MTg2MjEkajMyJGwwJGgw
    type: Login
  - name: Merge
    description: 'null'
    url: https://app.merge.dev/signup
    type: SignUp
  - name: Features
    type: Features
    data:
      - 'Launch: 3 free production accounts; $650/mo for 10; $65/extra'
      - 'Professional: contract pricing, custom fields, 400 req/min'
      - 'Enterprise: 600 req/min, audit trail, 90+ day log retention'
      - 200+ unified integrations across HRIS, ATS, CRM, Accounting, Ticketing, FileStorage
      - Unified Schema (read + write)
      - Field Mappings for custom field handling
      - Merge Link UI for end-customer authorization
      - Magic Link (no-code auth)
      - 'Sync frequencies: 1, 3, 6, 12, 24 hours (Pro+) '
      - Field-level scopes for data minimization (Pro+)
      - Webhooks for record changes
      - Bearer token auth + linked account tokens
      - OAuth + API key + custom auth flows handled per integration
      - Audit Trail (Enterprise)
      - 60-day or unlimited sandbox access
      - SOC 2 Type 2, GDPR, HIPAA-ready
    sources:
      - https://www.merge.dev/pricing
    updated: '2026-05-04'
  - name: Use Cases
    type: UseCases
    data:
      - name: Power AI features
      - name: Auto-provision
      - name: Knowledge base
      - name: Financial analysis
      - name: Candidate sourcing
      - name: Project analysis
      - name: Source leads
      - name: Reconcile vendor payments
      - name: Reconcile customer payments
      - name: Enterprise search
      - name: Customer support monitoring
      - name: Document management
  - name: Merge Status Page
    description: 'null'
    url: https://status.merge.dev/
    type: StatusPage
  - name: Merge Trust Center
    description: 'null'
    url: https://trust.merge.dev/
    type: Trust
  - name: Merge GitHub Organization
    description: 'null'
    url: https://github.com/merge-api
    type: GitHubOrg
  - name: Merge Python SDK
    description: 'null'
    url: https://github.com/merge-api/merge-python-client
    type: PythonSDK
  - name: Merge Node SDK
    description: 'null'
    url: https://github.com/merge-api/merge-sdk-typescript
    type: NodeSDK
  - name: Merge Go SDK
    description: 'null'
    url: https://github.com/merge-api/merge-go-client
    type: GoSDK
  - name: Merge Java SDK
    description: 'null'
    url: https://github.com/merge-api/merge-java-client
    type: JavaSDK
  - name: Merge SDKs Documentation
    description: 'null'
    url: https://docs.merge.dev/sdk/
    type: SDKs
  - name: Merge Postman Workspace
    description: 'null'
    url: https://www.postman.com/mergeapi/workspace/merge-public-workspace/overview
    type: PostmanWorkspace
  - name: Merge Integrations Directory
    description: 'null'
    url: https://www.merge.dev/integrations
    type: IntegrationDirectory
  - name: Merge Developer Tools
    description: 'null'
    url: https://www.merge.dev/features/developer-tools
    type: DeveloperTools
  - name: Merge Integration Observability
    description: 'null'
    url: https://www.merge.dev/features/integration-observability
    type: Observability
  - name: Merge Integrations Management
    description: 'null'
    url: https://www.merge.dev/features/integrations-management
    type: IntegrationManagement
  - name: Merge Authentication Guide
    description: 'null'
    url: https://docs.merge.dev/basics/authentication/
    type: Authentication
  - name: Merge Postman Testing Guide
    description: 'null'
    url: https://docs.merge.dev/guides/testing-via-postman/
    type: GettingStarted
  - name: Merge Unified API Overview
    description: 'null'
    url: https://docs.merge.dev/get-started/unified-api/
    type: GettingStarted
  - type: SpectralRules
    url: rules/merge-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/merge-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/talent-management.yaml
    title: Talent Management Workflow
  - type: Integrations
    data:
      - name: Workday
        description: HR platform integration via HRIS unified API.
      - name: BambooHR
        description: HR and payroll integration via HRIS unified API.
      - name: Greenhouse
        description: ATS integration for recruiting workflows.
      - name: Lever
        description: ATS integration for candidate management.
      - name: QuickBooks Online
        description: Accounting integration for financial data.
      - name: Xero
        description: Accounting integration for invoicing and payments.
      - name: Jira
        description: Ticketing integration for project management.
      - name: Salesforce
        description: CRM integration for sales data.
      - name: HubSpot
        description: CRM integration for marketing and sales.
      - name: Box
        description: File storage integration for document management.
      - name: Google Drive
        description: File storage integration for cloud files.
      - name: Slack
        description: Chat integration for messaging (roadmap).
      - name: Microsoft Teams
        description: Chat integration for enterprise messaging.
      - name: Confluence
        description: Knowledge base integration for enterprise content.
  - type: Solutions
    data:
      - name: Unified HRIS
        description: Single API for 80+ HR and payroll platforms.
      - name: Unified ATS
        description: Single API for 50+ applicant tracking systems.
      - name: Unified Accounting
        description: Single API for major accounting platforms.
      - name: Unified Ticketing
        description: Single API for 30+ ticketing and project management systems.
      - name: Unified CRM
        description: Single API for 20+ CRM platforms.
      - name: Unified File Storage
        description: Single API for file storage platforms with File Picker.
      - name: Agent Handler
        description: AI agent tool orchestration for thousands of pre-built integrations.
---
