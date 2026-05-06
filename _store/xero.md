---
aid: xero
name: Xero
description: Xero is a cloud-based accounting software platform that helps small and medium-sized businesses manage their finances. Xero provides a comprehensive developer platform with OAuth 2.0 APIs for accounting, payroll, assets, projects, files, bank feeds, and identity management. The Xero API enables third-party integrations to build custom accounting apps, automations, and business tools. Xero supports SDKs for .NET, Java, Node.js, PHP, Ruby, Python, and provides an MCP server for AI-assisted accounting workflows.
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Accounting
  - Bank Feeds
  - Finance
  - Financial Services
  - Invoicing
  - Payroll
  - Small Business
created: '2024-11-07'
modified: '2026-05-03'
url: https://raw.githubusercontent.com/api-evangelist/xero/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: xero:xero-accounting-api
    name: Xero Accounting API
    description: Core accounting API for the Xero platform. Supports creating and managing accounts, invoices, credit notes, bank transactions, contacts, payments, purchase orders, and financial reports. Provides comprehensive access to all accounting functions in Xero including chart of accounts, journal entries, tax rates, currencies, and tracking categories.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://developer.xero.com/documentation/api/accounting/overview
    baseURL: https://api.xero.com/api.xro/2.0
    tags:
      - Accounting
      - Finance
      - Invoicing
    properties:
      - type: Documentation
        url: https://developer.xero.com/documentation/api/accounting/overview
      - type: OpenAPI
        url: openapi/xero-accounting-openapi.yml
  - aid: xero:xero-assets-api
    name: Xero Assets API
    description: API for managing fixed assets in Xero. Supports registering and depreciating assets, managing asset types, and running depreciation calculations. Enables automated fixed asset lifecycle management integrated with Xero accounting.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://developer.xero.com/documentation/api/assets/overview
    baseURL: https://api.xero.com/assets.xro/1.0
    tags:
      - Assets
      - Depreciation
      - Finance
    properties:
      - type: Documentation
        url: https://developer.xero.com/documentation/api/assets/overview
      - type: OpenAPI
        url: openapi/xero-assets-openapi.yml
  - aid: xero:xero-bank-feeds-api
    name: Xero Bank Feeds API
    description: API for importing bank transaction data into Xero from financial institutions and fintech providers. Enables creation and management of bank feed connections and statement lines for automated bank reconciliation workflows.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://developer.xero.com/documentation/api/bank-feeds/overview
    baseURL: https://api.xero.com/bankfeeds.xro/1.0
    tags:
      - Bank Feeds
      - Banking
      - Reconciliation
    properties:
      - type: Documentation
        url: https://developer.xero.com/documentation/api/bank-feeds/overview
      - type: OpenAPI
        url: openapi/xero-bankfeeds-openapi.yml
  - aid: xero:xero-finance-api
    name: Xero Finance API
    description: API providing access to financial statements, balance sheets, profit and loss reports, and cash flow summaries for Xero organizations. Supports bank statement accounting, account usage, and lock history for financial analysis and reporting applications.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://developer.xero.com/documentation/api/finance/overview
    baseURL: https://api.xero.com/finance.xro/1.0
    tags:
      - Finance
      - Financial Reporting
      - Reports
    properties:
      - type: Documentation
        url: https://developer.xero.com/documentation/api/finance/overview
      - type: OpenAPI
        url: openapi/xero-finance-openapi.yml
  - aid: xero:xero-identity-api
    name: Xero Identity API
    description: OAuth 2.0 authentication and authorization API for the Xero platform. Manages connections to Xero organizations, user identity, and refresh token lifecycle. Required for all Xero API integrations to obtain and manage access tokens.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://developer.xero.com/documentation/guides/oauth2/overview/
    baseURL: https://identity.xero.com
    tags:
      - Authentication
      - Identity
      - OAuth 2.0
    properties:
      - type: Documentation
        url: https://developer.xero.com/documentation/guides/oauth2/overview/
      - type: OpenAPI
        url: openapi/xero-identity-openapi.yml
  - aid: xero:xero-payroll-australia-api
    name: Xero Payroll Australia API
    description: Payroll management API for Australian businesses using Xero. Supports managing employees, pay runs, pay slips, leave applications, payroll calendars, tax declarations, and superannuation. Compliant with Australian payroll regulations including Single Touch Payroll (STP).
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://developer.xero.com/documentation/api/payroll-au/overview
    baseURL: https://api.xero.com/payroll.xro/1.0
    tags:
      - Australia
      - Payroll
      - Superannuation
    properties:
      - type: Documentation
        url: https://developer.xero.com/documentation/api/payroll-au/overview
      - type: OpenAPI
        url: openapi/xero-payroll-au-openapi.yml
  - aid: xero:xero-payroll-new-zealand-api
    name: Xero Payroll New Zealand API
    description: Payroll management API for New Zealand businesses using Xero. Supports managing employees, pay runs, pay slips, leave management, and compliance with New Zealand payroll regulations including KiwiSaver and PAYE.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://developer.xero.com/documentation/api/payroll-nz/overview
    baseURL: https://api.xero.com/payroll.xro/1.0
    tags:
      - New Zealand
      - Payroll
    properties:
      - type: Documentation
        url: https://developer.xero.com/documentation/api/payroll-nz/overview
      - type: OpenAPI
        url: openapi/xero-payroll-nz-openapi.yml
  - aid: xero:xero-payroll-united-kingdom-api
    name: Xero Payroll United Kingdom API
    description: Payroll management API for UK businesses using Xero. Supports managing employees, pay runs, pay slips, leave, and compliance with UK payroll regulations including PAYE, national insurance, pensions, and Real Time Information (RTI) submissions to HMRC.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://developer.xero.com/documentation/api/payroll-uk/overview
    baseURL: https://api.xero.com/payroll.xro/1.0
    tags:
      - Payroll
      - United Kingdom
    properties:
      - type: Documentation
        url: https://developer.xero.com/documentation/api/payroll-uk/overview
      - type: OpenAPI
        url: openapi/xero-payroll-uk-openapi.yml
  - aid: xero:xero-projects-api
    name: Xero Projects API
    description: Project tracking and time management API for Xero. Supports creating and managing projects, tasks, time entries, and expenses. Enables integration of project-based billing with Xero accounting for professional services and project-based businesses.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://developer.xero.com/documentation/api/projects/overview
    baseURL: https://api.xero.com/projects.xro/2.0
    tags:
      - Projects
      - Time Tracking
    properties:
      - type: Documentation
        url: https://developer.xero.com/documentation/api/projects/overview
      - type: OpenAPI
        url: openapi/xero-projects-openapi.yml
  - aid: xero:xero-files-api
    name: Xero Files API
    description: File storage and management API for Xero. Supports uploading, organizing, and attaching files to accounting objects in Xero. Enables document management workflows integrated with accounting records for invoices, receipts, and other financial documents.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://developer.xero.com/documentation/api/files/overview
    baseURL: https://api.xero.com/files.xro/1.0
    tags:
      - Documents
      - Files
      - Storage
    properties:
      - type: Documentation
        url: https://developer.xero.com/documentation/api/files/overview
      - type: OpenAPI
        url: openapi/xero-files-openapi.yml
common:
  - type: Portal
    url: https://developer.xero.com/
  - type: Documentation
    url: https://developer.xero.com/documentation/
  - type: GettingStarted
    url: https://developer.xero.com/documentation/getting-started-guide/
  - type: Authentication
    url: https://developer.xero.com/documentation/guides/oauth2/overview/
  - type: SDKs
    url: https://developer.xero.com/documentation/sdks-and-tools/libraries/overview/
  - type: Webhooks
    url: https://developer.xero.com/documentation/guides/webhooks/overview/
  - type: Changelog
    url: https://developer.xero.com/changelog
  - type: Blog
    url: https://devblog.xero.com/
  - type: FAQ
    url: https://developer.xero.com/faq
  - type: TermsOfService
    url: https://developer.xero.com/xero-developer-platform-terms-conditions/
  - type: PrivacyPolicy
    url: https://www.xero.com/us/legal/privacy/
  - type: Status
    url: https://status.xero.com/
  - type: SignUp
    url: https://www.xero.com/us/signup/developers/
  - type: GitHubOrganization
    url: https://github.com/XeroAPI
  - type: MCPServer
    url: https://github.com/XeroAPI/xero-mcp-server
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
