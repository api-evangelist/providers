---
aid: paragon
url: https://raw.githubusercontent.com/api-evangelist/paragon/refs/heads/main/apis.yml
apis:
  - aid: paragon:proxy-api
    name: Proxy API
    tags:
      - Embedded SaaS
      - Integrations
    humanURL: https://docs.useparagon.com/apis/making-api-requests
    properties:
      - url: https://docs.useparagon.com/apis/making-api-requests
        type: Documentation
      - url: openapi/paragon-proxy-api-openapi.yml
        type: OpenAPI
      - url: json-ld/paragon-context.jsonld
        type: JSONLD
    description: "Once your users have connected their third-party app accounts in the Connect Portal, you can access their app account via the Proxy API. The Proxy API allows you to directly access any of the third-party provider\x19s API methods. With the SDK, you can use paragon.request to send an API request to a third-party app on behalf of one of your Connected Users. Along with Workflows, the Proxy API is one of two primary ways to build integrations with Paragon."
  - aid: paragon:users-api
    name: Users API
    tags:
      - Embedded SaaS
      - Integrations
    humanURL: https://docs.useparagon.com/apis/users
    properties:
      - url: https://docs.useparagon.com/apis/users
        type: Documentation
      - url: openapi/paragon-users-api-openapi.yml
        type: OpenAPI
      - url: json-schema/user.json
        type: JSONSchema
      - url: json-schema/integration.json
        type: JSONSchema
      - url: json-schema/credential.json
        type: JSONSchema
      - url: json-ld/paragon-context.jsonld
        type: JSONLD
    description: The Users API allows you to query and modify the state of your Connected Users and their integrations. The API includes REST endpoints (and matching SDK functions) for identifying what integrations your user has enabled, disconnecting integrations, and disabling workflows. The API also allows your application to associate metadata with a Connected User.
  - aid: paragon:task-history-api
    name: Task History API
    tags:
      - Embedded SaaS
      - Integrations
    humanURL: https://docs.useparagon.com/apis/task-history
    properties:
      - url: https://docs.useparagon.com/apis/task-history
        type: Documentation
      - url: openapi/paragon-task-history-api-openapi.yml
        type: OpenAPI
      - url: json-schema/workflow-execution.json
        type: JSONSchema
      - url: json-schema/workflow-execution-list.json
        type: JSONSchema
      - url: json-ld/paragon-context.jsonld
        type: JSONLD
    description: "The Task History API allows you to query your users\x19 usage of integration workflows and access data from historical workflow executions. The Task History API can be used to analyze integration usage or pull information about historical workflow executions into your application."
name: Paragon
tags:
  - Embedded iPaaS
  - Integrations
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
common:
  - url: https://github.com/useparagon
    name: GitHub Organization
    type: GitHubOrganization
  - url: https://www.useparagon.com/integrations
    name: Paragon | Embedded Integration Platform for Developers
    type: Integrations
    description: 'null'
  - url: https://docs.useparagon.com/overview
    name: Paragon Documentation
    type: Documentation
    description: 'null'
  - url: https://www.useparagon.com/blog
    name: Paragon Embedded iPaaS | Blog
    type: Blog
    description: 'null'
  - url: https://status.useparagon.com/
    name: Paragon Status
    type: Status
    description: 'null'
  - url: https://www.useparagon.com/use-case/library
    name: Powered by Paragon | Embedded iPaaS
    type: UseCases
    description: 'null'
  - url: https://docs.useparagon.com/getting-started/installing-the-connect-sdk
    name: Installing the SDK - Paragon Documentation
    type: SDKs
    description: 'null'
  - url: https://docs.useparagon.com/connect-portal/overview
    name: Overview - Paragon Documentation
    type: Authentication
    description: 'null'
  - url: https://docs.useparagon.com/resources/custom-webhooks
    name: Custom Webhooks - Paragon Documentation
    type: Webhooks
    description: 'null'
  - url: https://docs.useparagon.com/managing-account/role-based-access-control
    name: Role Based Access Control - Paragon Documentation
    type: RBAC
    description: 'null'
  - url: https://docs.useparagon.com/billing/concurrency-limits
    name: Concurrency SLA - Paragon Documentation
    type: ServiceLevelAgreement
    description: 'null'
  - url: https://docs.useparagon.com/security/security
    name: Security - Paragon Documentation
    type: Security
    description: 'null'
  - url: https://security.useparagon.com/
    name: Trust Center - Paragon
    type: Trust
    description: 'null'
  - url: https://docs.useparagon.com/security/gdpr
    name: GDPR - Paragon Documentation
    type: GDPR
    description: 'null'
  - url: https://docs.useparagon.com/support/contacting-support
    name: Contacting Support - Paragon Documentation
    type: Support
    description: 'null'
  - url: https://docs.useparagon.com/support/contacting-support
    name: Contacting Support - Paragon Documentation
    type: Support
    description: 'null'
  - url: https://docs.useparagon.com/workflows/overview
    name: Overview - Paragon Documentation
    type: Workflows
    description: 'null'
  - url: https://docs.useparagon.com/resources/integrations
    data:
      - name: Activecampaign
      - name: Adobe Acrobat Sign
      - name: Adobe Commerce
      - name: Adobe Experience Manager
      - name: Adp Workforce Now
      - name: Airtable
      - name: Amazon S3
      - name: Amplitude
      - name: apollo.io
      - name: Applicant Tracking System
      - name: Asana
      - name: Azure DevOps
      - name: Bamboohr
      - name: Bigquery
      - name: Box
      - name: Business Intelligence
      - name: Calendly
      - name: chorus.ai
      - name: Clickup
      - name: Close
      - name: Coda
      - name: Confluence
      - name: Content Management System
      - name: Copper
      - name: Docusign
      - name: Dropbox
      - name: Dropbox Sign
      - name: Dynamics 365 Business Central
      - name: Dynamics 365 Finance
      - name: Excel
      - name: Facebook Ads
      - name: Facebook Pages
      - name: Figma
      - name: Freshdesk
      - name: Freshsales
      - name: Front
      - name: Gainsight
      - name: Github
      - name: Gmail
      - name: Gong
      - name: Google Ad Manager
      - name: Google Ads
      - name: Google Analytics
      - name: Google Analytics GA4
      - name: Google Calendar
      - name: Google Campaign Manager
      - name: Google Docs
      - name: Google Drive
      - name: Google Search Console
      - name: Google Sheets
      - name: Greenhouse
      - name: Gusto
      - name: Heap
      - name: Hive
      - name: Hubspot
      - name: Imanage
      - name: Insightly
      - name: Intercom
      - name: Jira
      - name: Keap
      - name: Klaviyo
      - name: Lever
      - name: Linear
      - name: LinkedIn
      - name: Magento
      - name: Mailchimp
      - name: Marketo
      - name: Microsoft Dynamics 365 Sales
      - name: Microsoft Outlook
      - name: Microsoft Sharepoint
      - name: Microsoft Teams
      - name: Miro
      - name: Mixpanel
      - name: monday.com
      - name: Netsuite
      - name: Notion
      - name: Onedrive
      - name: Onenote
      - name: OpenAI
      - name: Oracle Eloqua
      - name: Oracle Financials Cloud
      - name: Outreach
      - name: Pagerduty
      - name: Pandadoc
      - name: Pardot
      - name: Pipedrive
      - name: Power Bi
      - name: Productboard
      - name: Quickbooks
      - name: Quip
      - name: Sage Accounting
      - name: Sage Intacct
      - name: Sailthru
      - name: Salesforce
      - name: Salesloft
      - name: Sap S/4HANA
      - name: Sap Success Factors
      - name: Segment
      - name: Servicenow
      - name: Shopify
      - name: Shortcut
      - name: Slack
      - name: Snowflake
      - name: Stack Overflow for Teams
      - name: Stripe
      - name: Tableau
      - name: TikTok Ads
      - name: Todoist
      - name: Trello
      - name: Typeform
      - name: Vanta
      - name: Whatsapp
      - name: Woocommerce
      - name: WordPress
      - name: Workable
      - name: Workday
      - name: Xero
      - name: Zendesk
      - name: Zendesk Sell
      - name: Zoho CRM
      - name: Zoho People
      - name: Zoom
    name: Overview - Paragon Documentation
    type: Integrations
  - url: https://docs.useparagon.com/changelog/product-updates
    name: Product Updates - Paragon Documentation
    type: ChangeLog
    description: 'null'
  - url: https://dashboard.useparagon.com/signup
    name: Paragon
    type: SignUp
    description: 'null'
  - url: https://dashboard.useparagon.com/login
    name: Paragon
    type: Login
    description: 'null'
  - url: https://www.useparagon.com/terms-of-service
    name: Paragon Embedded iPaaS | Terms of Service
    type: TermsOfService
    description: 'null'
  - url: https://www.useparagon.com/customers
    name: Paragon Embedded iPaaS | Customer Stories
    type: Customers
    description: 'null'
  - url: https://www.useparagon.com/pricing
    name: Paragon | Embedded Integration Platform for Developers
    type: Pricing
    description: 'null'
  - url: https://www.useparagon.com/use-case/library
    data:
      - name: Agentic Actions Across Integrations
      - name: Embedded Workflow Builder Actions
      - name: File Upload via 3rd-Party Picker
      - name: Ingest All Files From File Storage
      - name: Ingest Permissions for Rag and AI
      - name: Real-Time Bidirectional CRM Sync
      - name: Send Slack / Teams Notifications
    name: Use Cases
    type: UseCases
  - url: https://www.useparagon.com/use-case/library
    data:
      - 'Platform: custom pricing by Connected Users'
      - 'Enterprise: self-host / forward-deploy, dedicated support'
      - Unlimited integrations
      - Fully managed authentication (OAuth, API key, custom)
      - Managed Sync for incremental data syncs
      - ActionKit for one-shot operations
      - Workflows for multi-step orchestration
      - Embedded UX or Headless SDK
      - Event Logs for debugging
      - 'Connect API: 600 req/min/workspace'
      - 'ActionKit API: 50 req/sec/workspace'
      - OAuth + workspace tokens
      - Bring Your Own Connector (BYOC)
      - 200+ pre-built integrations
      - Dynamic Field Mapping (Enterprise)
      - SOC 2 Type 2 + GDPR-ready
    name: Features
    type: Features
    sources:
      - https://www.useparagon.com/pricing
    updated: '2026-05-04'
created: '2025-06-05T00:00:00.000Z'
modified: '2026-05-04'
position: Consuming
description: Paragon enables companies to build products that integrate with the SaaS ecosystem. With Paragon, software companies can integrate with hundreds of different SaaS apps in minutes while providing their customers with a seamless, unified integration experience.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
---
