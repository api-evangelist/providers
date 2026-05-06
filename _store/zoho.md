---
aid: zoho
name: Zoho
segments:
  - Workflows
description: Zoho is a comprehensive cloud software suite offering 55+ integrated business applications for sales, marketing, customer service, finance, HR, collaboration, and custom solutions, trusted by over 130 million users worldwide.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Analytics
  - Collaboration
  - CRM
  - Customer Service
  - Email
  - Finance
  - Human Resources
  - Project Management
created: '2025-02-08'
modified: '2026-05-04'
url: https://raw.githubusercontent.com/api-evangelist/zoho/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: zoho:zoho-inventory
    name: Zoho Inventory
    description: The Zoho Inventory API allows you to perform all the operations that you do with our web client. It is built using REST principles which ensures predictable URLs for accessing resources, and uses HTTP response codes to indicate API errors.
    humanURL: https://www.zoho.com/inventory/api/v1/introduction/
    tags:
      - Inventory
      - Stock
      - Warehouse
    properties:
      - type: Documentation
        url: https://www.zoho.com/inventory/api/v1/introduction/
  - aid: zoho:zoho-crm
    name: Zoho CRM
    description: The Zoho CRM API provides REST endpoints and client libraries for Java, PHP, Python, and Node.js, allowing developers to integrate CRM data with third-party applications. It includes asynchronous APIs for bulk data operations and CRM Object Query Language (COQL) for SQL-style queries.
    humanURL: https://www.zoho.com/crm/developer/docs/api/
    tags:
      - Contacts
      - CRM
      - Leads
      - Sales
    properties:
      - type: Documentation
        url: https://www.zoho.com/crm/developer/docs/api/
      - type: APIReference
        url: https://www.zoho.com/crm/developer/docs/api/v8/
      - type: GettingStarted
        url: https://www.zoho.com/crm/developer/docs/
      - type: OpenAPI
        url: https://github.com/zoho/crm-oas
        title: OpenAPI 3.1 Specifications (v8.0)
      - type: SDK
        url: https://packagist.org/packages/zohocrm/php-sdk-8.0
        title: PHP SDK (v8.0)
      - type: SDK
        url: https://pypi.org/project/zohocrmsdk8-0/
        title: Python SDK (v8.0)
      - type: SDK
        url: https://www.nuget.org/packages/ZOHOCRMSDK-8.0/
        title: C# SDK (v8.0)
      - type: SDK
        url: https://github.com/zoho/zohocrm-java-sdk-8.0
        title: Java SDK (v8.0)
      - type: SDK
        url: https://www.npmjs.com/package/@zohocrm/nodejs-sdk-8.0
        title: Node.js SDK (v8.0)
      - type: SDK
        url: https://www.npmjs.com/package/@zohocrm/typescript-sdk-8.0
        title: TypeScript SDK (v8.0)
      - type: SDK
        url: https://rubygems.org/gems/ZOHOCRMSDK8_0
        title: Ruby SDK (v8.0)
      - type: SDK
        url: https://github.com/zoho/zohocrm-javascript-sdk-8.0
        title: JavaScript SDK (v8.0)
      - type: SDK
        url: https://github.com/zoho/zohocrm-scala-sdk-8.0
        title: Scala SDK (v8.0)
      - type: SDK
        url: https://cocoapods.org/pods/ZCRMiOS
        title: iOS SDK
  - aid: zoho:zoho-books
    name: Zoho Books
    description: The Zoho Books API allows you to perform all the operations that you do with the web client. It is built using REST principles which ensures predictable URLs for accessing resources, and uses HTTP response codes to indicate API errors.
    humanURL: https://www.zoho.com/books/api/v3/introduction/
    tags:
      - Accounting
      - Books
      - Finance
      - Invoices
    properties:
      - type: Documentation
        url: https://www.zoho.com/books/api/v3/introduction/
      - type: PostmanCollection
        url: https://www.zoho.com/books/api/v3/apicollection/
      - type: CodeExamples
        url: https://github.com/zoho/zohofinance-automation-samples
        title: Custom Functions Samples
  - aid: zoho:zoho-invoice
    name: Zoho Invoice
    description: The Zoho Invoice API allows you to perform all the operations that you do with the web client. It is built using REST principles and supports managing invoices, customers, items, and payments programmatically.
    humanURL: https://www.zoho.com/invoice/api/v3/introduction/
    tags:
      - Billing
      - Finance
      - Invoicing
    properties:
      - type: Documentation
        url: https://www.zoho.com/invoice/api/v3/introduction/
  - aid: zoho:zoho-billing
    name: Zoho Billing
    description: The Zoho Billing API allows you to perform all operations from the web client and is built using REST principles. It supports managing subscriptions, plans, customers, invoices, and payment processing programmatically.
    humanURL: https://www.zoho.com/billing/api/v1/introduction/
    tags:
      - Billing
      - Payments
      - Subscriptions
    properties:
      - type: Documentation
        url: https://www.zoho.com/billing/api/v1/introduction/
      - type: Authentication
        url: https://www.zoho.com/billing/api/v1/oauth/
      - type: PostmanCollection
        url: https://www.zoho.com/billing/api/v1/apicollection/
      - type: SDK
        url: https://github.com/zoho/subscriptions-java-client
        title: Java Client (Subscriptions)
      - type: CodeExamples
        url: https://github.com/zoho/subscriptions-workflow-samples
        title: Workflow Samples
      - type: Tools
        url: https://github.com/zoho/zoho-billing-mcp
        title: MCP Server
  - aid: zoho:zoho-expense
    name: Zoho Expense
    description: The Zoho Expense API allows you to manage expenses, expense reports, receipts, trips, and users programmatically. It is built using REST principles and supports integration with third-party applications.
    humanURL: https://www.zoho.com/expense/api/v1/introduction/
    tags:
      - Expense Management
      - Receipts
      - Trips
    properties:
      - type: Documentation
        url: https://www.zoho.com/expense/api/v1/introduction/
      - type: Authentication
        url: https://www.zoho.com/expense/api/v1/authentication/
  - aid: zoho:zoho-desk
    name: Zoho Desk
    description: The Zoho Desk API provides REST endpoints to integrate your help desk with third-party applications. It supports managing tickets, contacts, accounts, and includes webhook support for event-driven notifications.
    humanURL: https://desk.zoho.com/DeskAPIDocument
    tags:
      - Customer Support
      - Help Desk
      - Tickets
    properties:
      - type: Documentation
        url: https://desk.zoho.com/DeskAPIDocument
      - type: DeveloperPortal
        url: https://www.zoho.com/desk/developers/
      - type: OpenAPI
        url: https://github.com/zoho/zohodesk-oas
        title: OpenAPI Specifications (v1.0)
      - type: SDK
        url: https://github.com/zoho/ZohoDeskPortalSDK
        title: iOS Portal SDK
      - type: SDK
        url: https://github.com/zoho/react-native-zohodesk-portal-sdk
        title: React Native Portal SDK
      - type: SDK
        url: https://github.com/zoho/zdesk-asap-flutter
        title: Flutter ASAP SDK
      - type: SDK
        url: https://github.com/zoho/cordova-plugin-zohodesk-portal
        title: Cordova Portal SDK
      - type: CodeExamples
        url: https://github.com/zoho/ZohoDesk-PortalSDK-Sample-apps-iOS
        title: iOS Portal SDK Samples
      - type: CodeExamples
        url: https://github.com/zoho/ZohoDesk-PortalSDK-sample-apps-android
        title: Android Portal SDK Samples
      - type: CodeExamples
        url: https://github.com/zoho/ZohoDesk-PortalSDK-sample-apps-flutter
        title: Flutter Portal SDK Samples
      - type: CodeExamples
        url: https://github.com/zoho/ZohoDesk-PortalSDK-sample-apps-reactnative
        title: React Native Portal SDK Samples
      - type: CodeExamples
        url: https://github.com/zoho/Zoho-Desk-ASAP-Mobile-SDK-API-Samples
        title: ASAP Mobile SDK API Samples
  - aid: zoho:zoho-people
    name: Zoho People
    description: The Zoho People API allows you to integrate HR modules with third-party applications, extracting employee data and form data in XML or JSON format. It is independent of programming languages and available in Essential HR, Professional, Premium, and Enterprise plans.
    humanURL: https://www.zoho.com/people/api/overview.html
    tags:
      - Employees
      - HR
      - Human Resources
    properties:
      - type: Documentation
        url: https://www.zoho.com/people/api/overview.html
  - aid: zoho:zoho-recruit
    name: Zoho Recruit
    description: The Zoho Recruit API provides REST endpoints with JSON format and OAuth2.0 authentication for integrating recruitment modules with third-party applications. It supports managing candidates, job openings, contacts, interviews, and assessments, with asynchronous APIs for bulk operations.
    humanURL: https://www.zoho.com/recruit/developer-guide/apiv2/
    tags:
      - Candidates
      - Hiring
      - HR
      - Recruitment
    properties:
      - type: Documentation
        url: https://www.zoho.com/recruit/developer-guide/apiv2/
  - aid: zoho:zoho-projects
    name: Zoho Projects
    description: The Zoho Projects API allows you to understand and integrate Zoho Projects service with third-party applications, managing projects, tasks, time tracking, documents, and more programmatically through REST endpoints.
    humanURL: https://projects.zoho.com/api-docs
    tags:
      - Project Management
      - Tasks
      - Time Tracking
    properties:
      - type: Documentation
        url: https://projects.zoho.com/api-docs
      - type: GettingStarted
        url: https://www.zoho.com/projects/help/rest-api/projects-api.html
      - type: SDK
        url: https://github.com/zoho/projects-java-wrappers
        title: Java Wrappers
      - type: SDK
        url: https://github.com/zoho/projects-dotnet-wrappers
        title: .NET Wrappers
      - type: SDK
        url: https://github.com/zoho/projects-ruby-wrappers
        title: Ruby Wrappers
  - aid: zoho:zoho-mail
    name: Zoho Mail
    description: The Zoho Mail REST API allows developers to fetch email conversations and integrate Zoho Mail into applications, managing accounts, folders, labels, messages, signatures, threads, and organizational policies.
    humanURL: https://www.zoho.com/mail/help/api/overview.html
    tags:
      - Email
      - Mail
      - Messaging
    properties:
      - type: Documentation
        url: https://www.zoho.com/mail/help/api/overview.html
      - type: APIReference
        url: https://www.zoho.com/mail/help/api/
      - type: GettingStarted
        url: https://www.zoho.com/mail/help/api/getting-started-with-api.html
  - aid: zoho:zoho-sign
    name: Zoho Sign
    description: The Zoho Sign API helps developers integrate document signing capabilities within applications, enabling users to send, sign, and manage documents programmatically through REST endpoints.
    humanURL: https://www.zoho.com/sign/api/
    tags:
      - Documents
      - E-Signatures
      - Signing
    properties:
      - type: Documentation
        url: https://www.zoho.com/sign/api/
      - type: SDK
        url: https://packagist.org/packages/zoho-sign/php-sdk
        title: PHP SDK
      - type: SDK
        url: https://github.com/zoho/zsign-nodejs-sdk
        title: Node.js SDK
      - type: SDK
        url: https://github.com/zoho/ZohoSignSDK-iOS
        title: iOS SDK
  - aid: zoho:zoho-analytics
    name: Zoho Analytics
    description: The Zoho Analytics API is built using REST principles and provides programmatic access to data, reports, and dashboards. It supports data import, export in multiple formats, and offers SDKs for Java, C#, Python, PHP, Go, and Node.js.
    humanURL: https://www.zoho.com/analytics/api/v2/introduction.html
    tags:
      - Analytics
      - Business Intelligence
      - Reporting
    properties:
      - type: Documentation
        url: https://www.zoho.com/analytics/api/v2/introduction.html
      - type: APIReference
        url: https://www.zoho.com/analytics/api/v2/
      - type: OpenAPI
        url: https://github.com/zoho/analytics-oas
        title: OpenAPI Specifications (v2.0)
      - type: CodeExamples
        url: https://github.com/zoho/analytics-codestudio
        title: Code Studio Samples
      - type: Tools
        url: https://github.com/zoho/analytics-mcp-server
        title: MCP Server
      - type: Integrations
        url: https://github.com/zoho/analytics-dataiku-import-plugin
        title: Dataiku Import Plugin
      - type: Integrations
        url: https://github.com/zoho/analytics-dataiku-export-plugin
        title: Dataiku Export Plugin
  - aid: zoho:zoho-campaigns
    name: Zoho Campaigns
    description: The Zoho Campaigns API provides programmatic access to email marketing capabilities, allowing integration with Zoho CRM and third-party applications for managing campaigns, contacts, and marketing automation.
    humanURL: https://www.zoho.com/campaigns/help/developers/
    tags:
      - Campaigns
      - Email Marketing
      - Marketing Automation
    properties:
      - type: Documentation
        url: https://www.zoho.com/campaigns/help/developers/
      - type: CodeExamples
        url: https://github.com/zoho/zohocampaigns-emailapi-smtp
        title: Email API and SMTP Samples
  - aid: zoho:zoho-salesiq
    name: Zoho SalesIQ
    description: The Zoho SalesIQ API provides JavaScript APIs for customizing chat widgets and REST APIs for integrating live chat and visitor tracking with third-party applications. It uses OAuth 2.0 for authentication and offers mobile SDKs for iOS and Android.
    humanURL: https://www.zoho.com/salesiq/help/developer-section/
    tags:
      - Live Chat
      - Sales
      - Visitor Tracking
    properties:
      - type: Documentation
        url: https://www.zoho.com/salesiq/help/developer-section/
      - type: APIReference
        url: https://www.zoho.com/salesiq/help/developer-section/rest-api-v2.html
      - type: SDK
        url: https://github.com/zoho/SalesIQ-Mobilisten-iOS
        title: iOS SDK (Mobilisten)
      - type: SDK
        url: https://github.com/zoho/SalesIQ-Mobilisten-iOS-SP
        title: iOS Swift Package (Mobilisten)
      - type: SDK
        url: https://github.com/zoho/SalesIQ-Mobilisten-ReactNative
        title: React Native SDK (Mobilisten)
      - type: SDK
        url: https://github.com/zoho/salesiq-mobilisten-flutter
        title: Flutter SDK (Mobilisten)
      - type: SDK
        url: https://github.com/zoho/SalesIQ-Mobilisten-Cordova
        title: Cordova SDK (Mobilisten)
      - type: CodeExamples
        url: https://github.com/zoho/salesiq-mobilisten-android-sample
        title: Android Sample App
  - aid: zoho:zoho-creator
    name: Zoho Creator
    description: The Zoho Creator API provides RESTful endpoints to interface with Zoho Creator applications, allowing you to fetch, add, update, and delete data, as well as manage forms and reports programmatically.
    humanURL: https://www.zoho.com/creator/help/api/v2.1/
    tags:
      - Application Development
      - Custom Apps
      - Low-Code
    properties:
      - type: Documentation
        url: https://www.zoho.com/creator/help/api/v2.1/
      - type: SDK
        url: https://github.com/zoho/ZohoCreator-IOS-frameworks
        title: iOS Frameworks
  - aid: zoho:zoho-cliq
    name: Zoho Cliq
    description: The Zoho Cliq REST API v2 allows developers to extend their web applications by programmatically managing channels, messages, and bots, with OAuth token-based authentication.
    humanURL: https://www.zoho.com/cliq/help/restapi/v2/
    tags:
      - Collaboration
      - Messaging
      - Team Chat
    properties:
      - type: Documentation
        url: https://www.zoho.com/cliq/help/restapi/v2/
      - type: DeveloperPortal
        url: https://www.zoho.com/cliq/help/developers.html
  - aid: zoho:zoho-meeting
    name: Zoho Meeting
    description: The Zoho Meeting API allows you to integrate online meeting and webinar capabilities with third-party applications and websites. It is based on REST and provides JSON responses for managing meetings programmatically.
    humanURL: https://www.zoho.com/meeting/api-integration.html
    tags:
      - Meetings
      - Video Conferencing
      - Webinars
    properties:
      - type: Documentation
        url: https://www.zoho.com/meeting/api-integration.html
      - type: SDK
        url: https://www.zoho.com/meeting/api-integration/sdk.html
  - aid: zoho:zoho-connect
    name: Zoho Connect
    description: The Zoho Connect API allows users and developers to extend web applications by programmatically fetching and editing data from different modules in Connect, including feeds, tasks, and groups.
    humanURL: https://www.zoho.com/connect/api/intro.html
    tags:
      - Collaboration
      - Social Intranet
      - Team Communication
    properties:
      - type: Documentation
        url: https://www.zoho.com/connect/api/intro.html
      - type: Authentication
        url: https://www.zoho.com/connect/api/authentication.html
  - aid: zoho:zoho-workdrive
    name: Zoho WorkDrive
    description: The Zoho WorkDrive API provides programmatic access to cloud file management, allowing developers to manage files, folders, team folders, and sharing capabilities through REST endpoints.
    humanURL: https://workdrive.zoho.com/apidocs/v1/
    tags:
      - Cloud Storage
      - Document Management
      - File Management
    properties:
      - type: Documentation
        url: https://workdrive.zoho.com/apidocs/v1/
  - aid: zoho:zoho-sprints
    name: Zoho Sprints
    description: The Zoho Sprints API allows developers to extend web applications and push or pull data to and from Zoho Sprints, supporting agile project management workflows including sprints, backlogs, and epics.
    humanURL: https://sprints.zoho.com/apidoc.html
    tags:
      - Agile
      - Scrum
      - Sprints
    properties:
      - type: Documentation
        url: https://sprints.zoho.com/apidoc.html
  - aid: zoho:zoho-bookings
    name: Zoho Bookings
    description: The Zoho Bookings API allows developers to integrate online scheduling and appointment management with third-party applications, supporting booking, fetching, and updating appointments programmatically.
    humanURL: https://www.zoho.com/bookings/help/api/v1/generate-accesstoken.html
    tags:
      - Appointments
      - Bookings
      - Scheduling
    properties:
      - type: Documentation
        url: https://www.zoho.com/bookings/help/api/v1/generate-accesstoken.html
  - aid: zoho:zoho-commerce
    name: Zoho Commerce
    description: The Zoho Commerce API allows you to perform operations with your web client and is built using REST principles. It supports managing products, orders, customers, and e-commerce workflows programmatically.
    humanURL: https://www.zoho.com/commerce/api/introduction.html
    tags:
      - E-Commerce
      - Online Store
      - Shopping
    properties:
      - type: Documentation
        url: https://www.zoho.com/commerce/api/introduction.html
  - aid: zoho:zoho-assist
    name: Zoho Assist
    description: The Zoho Assist API allows you to integrate remote support and screen sharing capabilities with third-party applications. It is based on REST with JSON responses and supports creating, scheduling, and managing remote support sessions programmatically.
    humanURL: https://www.zoho.com/assist/api/introduction.html
    tags:
      - Remote Access
      - Remote Support
      - Screen Sharing
    properties:
      - type: Documentation
        url: https://www.zoho.com/assist/api/introduction.html
      - type: Authentication
        url: https://www.zoho.com/assist/api/authentication.html
      - type: SDK
        url: https://github.com/zoho/AssistSDK
        title: iOS SDK
      - type: CodeExamples
        url: https://github.com/zoho/Assist-Customer-Android-SDK-Demo
        title: Android Customer SDK Demo
  - aid: zoho:zoho-bugtracker
    name: Zoho BugTracker
    description: The Zoho BugTracker API uses OAuth 2.0 for authentication and provides REST endpoints for managing bugs, projects, timesheets, documents, and tags programmatically for issue tracking workflows.
    humanURL: https://www.zoho.com/projects/help/rest-api/bugtracker-api.html
    tags:
      - Bug Tracking
      - Issue Tracking
      - QA
    properties:
      - type: Documentation
        url: https://www.zoho.com/projects/help/rest-api/bugtracker-api.html
  - aid: zoho:zoho-writer
    name: Zoho Writer
    description: The Zoho Writer API provides endpoints to create add-ons that interact with document content and metadata, allowing you to get, create, upload, delete, and download documents programmatically.
    humanURL: https://www.zoho.com/writer/help/api/v1/getting-started.html
    tags:
      - Documents
      - Word Processing
      - Writing
    properties:
      - type: Documentation
        url: https://www.zoho.com/writer/help/api/v1/getting-started.html
      - type: APIReference
        url: https://www.zoho.com/writer/help/api/v1/document-api.html
  - aid: zoho:zoho-sheet
    name: Zoho Sheet
    description: The Zoho Sheet Data API provides programmatic access to read or update spreadsheets in Zoho Sheet, allowing integration with third-party applications for spreadsheet management and data manipulation.
    humanURL: https://www.zoho.com/sheet/help/api/v2/
    tags:
      - Collaboration
      - Data
      - Spreadsheets
    properties:
      - type: Documentation
        url: https://www.zoho.com/sheet/help/api/v2/
      - type: DeveloperPortal
        url: https://www.zoho.com/sheet/developers.html
  - aid: zoho:zoho-calendar
    name: Zoho Calendar
    description: The Zoho Calendar API provides REST endpoints to customize calendar features, allowing you to manage calendars, events, and sharing capabilities programmatically with OAuth 2.0 authentication.
    humanURL: https://www.zoho.com/calendar/help/api/introduction.html
    tags:
      - Calendar
      - Events
      - Scheduling
    properties:
      - type: Documentation
        url: https://www.zoho.com/calendar/help/api/introduction.html
      - type: Authentication
        url: https://www.zoho.com/calendar/help/api/oauth2-user-guide.html
  - aid: zoho:zoho-vault
    name: Zoho Vault
    description: The Zoho Vault API provides REST endpoints to integrate password management functionality within your application, supporting secret management, password retrieval, and secure data operations with OAuth 2.0 authentication.
    humanURL: https://www.zoho.com/vault/api/
    tags:
      - Password Management
      - Secrets
      - Security
    properties:
      - type: Documentation
        url: https://www.zoho.com/vault/api/
      - type: DeveloperPortal
        url: https://www.zoho.com/vault/developers.html
  - aid: zoho:zoho-catalyst
    name: Zoho Catalyst
    description: The Zoho Catalyst API provides programmatic access to serverless application development features, including data store operations, file storage management, and function execution for building and deploying cloud applications.
    humanURL: https://docs.catalyst.zoho.com/en/api/introduction/overview-and-prerequisites/
    tags:
      - Application Development
      - Cloud Platform
      - Serverless
    properties:
      - type: Documentation
        url: https://docs.catalyst.zoho.com/en/api/introduction/overview-and-prerequisites/
      - type: CodeExamples
        url: https://github.com/zoho/Catalyst-iOS-SDK-Sample-App
        title: iOS SDK Sample App
  - aid: zoho:zoho-bigin
    name: Zoho Bigin
    description: The Zoho Bigin API provides REST endpoints for building integrations with Bigin by Zoho CRM. It supports managing contacts, deals, products, activities, and pipelines with OAuth 2.0 authentication, and offers asynchronous APIs for bulk data operations.
    humanURL: https://www.bigin.com/developer/docs/apis/v2/
    tags:
      - CRM
      - Pipelines
      - Small Business
    properties:
      - type: Documentation
        url: https://www.bigin.com/developer/docs/apis/v2/
      - type: DeveloperPortal
        url: https://www.bigin.com/developer-center.html
      - type: OpenAPI
        url: https://github.com/zoho/bigin-oas
        title: OpenAPI Specifications
  - aid: zoho:zoho-zeptomail
    name: Zoho ZeptoMail
    description: The Zoho ZeptoMail API provides REST endpoints for sending transactional emails such as OTPs, password resets, invoices, and more from your application. It supports template-based and batch email sending with client libraries for multiple languages.
    humanURL: https://www.zoho.com/zeptomail/help/api-home.html
    tags:
      - Email Delivery
      - SMTP
      - Transactional Email
    properties:
      - type: Documentation
        url: https://www.zoho.com/zeptomail/help/api-home.html
      - type: APIReference
        url: https://www.zoho.com/zeptomail/help/api-index.html
  - aid: zoho:zoho-office-integrator
    name: Zoho Office Integrator
    description: The Zoho Office Integrator API allows you to embed Zoho's document editors for Writer, Sheet, and Show into third-party web applications and services, providing collaborative document editing capabilities.
    humanURL: https://www.zoho.com/officeintegrator/api/v1/
    tags:
      - Document Editing
      - Embed
      - Office Suite
    properties:
      - type: Documentation
        url: https://www.zoho.com/officeintegrator/api/v1/
      - type: SDK
        url: https://packagist.org/packages/zohocorporation/office-integrator-sdk
        title: PHP SDK
      - type: SDK
        url: https://pypi.org/project/office-integrator-sdk/
        title: Python SDK
      - type: SDK
        url: https://www.npmjs.com/package/@zoho-corp/office-integrator-sdk
        title: Node.js SDK
      - type: SDK
        url: https://github.com/zoho/office-integrator-csharp-sdk
        title: C# SDK
      - type: CodeExamples
        url: https://github.com/zoho/office-integrator-php-sdk-examples
        title: PHP SDK Examples
      - type: CodeExamples
        url: https://github.com/zoho/office-integrator-python-sdk-examples
        title: Python SDK Examples
      - type: CodeExamples
        url: https://github.com/zoho/office-integrator-nodejs-sdk-examples
        title: Node.js SDK Examples
      - type: CodeExamples
        url: https://github.com/zoho/office-integrator-csharp-sdk-examples
        title: C# SDK Examples
      - type: CodeExamples
        url: https://github.com/zoho/office-integrator-java-sdk-examples
        title: Java SDK Examples
  - aid: zoho:zoho-pdf-editor
    name: Zoho PDF Editor
    description: The Zoho PDF Editor API provides REST endpoints for inserting images, splitting pages, extracting specific pages from PDF documents, and uploading PDF documents for online editing with OAuth 2.0 authentication.
    humanURL: https://www.zoho.com/pdfeditor/help/api/getting-started.html
    tags:
      - Document Editing
      - PDF
      - PDF Management
    properties:
      - type: Documentation
        url: https://www.zoho.com/pdfeditor/help/api/getting-started.html
      - type: APIReference
        url: https://www.zoho.com/pdfeditor/help/api/v1/pdf-api.html
common:
  - type: DeveloperPortal
    url: https://www.zoho.com/developer/
  - type: Authentication
    url: https://www.zoho.com/developer/rest-api.html
  - type: GettingStarted
    url: https://www.zoho.com/developer/help/extensions/getting-started.html
  - type: SignUp
    url: https://www.zoho.com/developer/signup.html
  - type: Blog
    url: https://www.zoho.com/blog/developer
  - type: StatusPage
    url: https://zohostatus.com/
  - type: PrivacyPolicy
    url: https://www.zoho.com/privacy.html
  - type: TermsOfService
    url: https://www.zoho.com/terms.html
  - type: GitHubOrganization
    url: https://github.com/zoho
  - type: Pricing
    url: https://www.zoho.com/one/pricing/
  - type: Tools
    url: https://github.com/zoho/embeddedApp-js-sdk
    title: Embedded App JS SDK
  - type: Tools
    url: https://github.com/zoho/hawking
    title: Hawking - Natural Language Date Parser
  - type: Integrations
    url: https://github.com/zoho/moodle-local_zohoflow
    title: Zoho Flow Connector for Moodle
  - type: Integrations
    url: https://github.com/zoho/zoho_tables_n8n
    title: Zoho Tables n8n Node
  - type: Features
    data:
      - 'Zoho CRM Standard: ₹800/user/mo (~$10)'
      - 'Zoho CRM Professional: ₹1,400/user/mo (CPQ, inventory)'
      - 'Zoho CRM Enterprise: ₹2,400/user/mo (Zia AI)'
      - 'Zoho CRM Ultimate: ₹2,600/user/mo'
      - 'Zoho One (45+ apps bundle): ~$37/user/mo annual all-employee'
      - REST API v2/v8 for CRM, Books, Mail, etc.
      - 'API credits scale with tier: 5K (Std), 10K (Pro), 25K (Ent), 50K (Ult) per day'
      - Per-user 10 concurrent calls
      - OAuth 2.0 + self-client tokens
      - Webhooks for record changes
      - Zia AI assistant (Enterprise+)
      - Deluge custom scripting language
      - Marketplace extensions
      - Multi-region data centers (US, EU, IN, AU, JP, CA)
      - GDPR + HIPAA + SOC 2
      - 'Bundles: Zoho One (full suite), Workplace, CRM Plus, Finance Plus, etc.'
    sources:
      - https://www.zoho.com/crm/zohocrm-pricing.html
    updated: '2026-05-04'
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
