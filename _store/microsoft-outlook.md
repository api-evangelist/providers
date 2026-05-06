---
aid: microsoft-outlook
name: Microsoft Outlook
description: Microsoft Outlook is a personal information manager and email client that is part of the Microsoft Office suite. It provides email, calendar, contact management, task management, and other productivity features.
image: https://www.microsoft.com/en-us/microsoft-365/blog/wp-content/uploads/sites/2/2019/11/Outlook-logo.png
created: '2024'
modified: '2026-04-18'
specificationVersion: '0.19'
url: https://outlook.office.com
apis:
  - name: Microsoft Graph Mail API
    description: API for accessing Outlook email messages, folders, and mail settings through Microsoft Graph.
    image: https://docs.microsoft.com/en-us/graph/images/microsoft-graph.png
    humanURL: https://learn.microsoft.com/en-us/graph/api/resources/mail-api-overview?view=graph-rest-1.0
    baseURL: https://graph.microsoft.com/v1.0
    tags:
      - Email
      - Folders
      - Mail
      - Messages
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/graph/api/resources/mail-api-overview?view=graph-rest-1.0
      - type: OpenAPI
        url: openapi/microsoft-graph-mail-api-openapi.yml
      - type: OpenAPI
        url: https://raw.githubusercontent.com/microsoftgraph/msgraph-metadata/master/openapi/v1.0/openapi.yaml
      - type: JSONSchema
        url: json-schema/microsoft-outlook-message-schema.json
      - type: JSONLD
        url: json-ld/microsoft-outlook-context.jsonld
      - type: Authentication
        url: https://learn.microsoft.com/en-us/graph/auth/
      - type: GettingStarted
        url: https://learn.microsoft.com/en-us/graph/outlook-mail-concept-overview
      - type: APIReference
        url: https://learn.microsoft.com/en-us/graph/api/overview?view=graph-rest-1.0
      - type: SDK
        url: https://learn.microsoft.com/en-us/graph/sdks/sdks-overview
      - type: ChangeLog
        url: https://developer.microsoft.com/en-us/graph/changelog
  - name: Microsoft Graph Calendar API
    description: API for accessing Outlook calendar events, calendars, and meeting scheduling through Microsoft Graph.
    image: https://docs.microsoft.com/en-us/graph/images/microsoft-graph.png
    humanURL: https://learn.microsoft.com/en-us/graph/api/resources/calendar?view=graph-rest-1.0
    baseURL: https://graph.microsoft.com/v1.0
    tags:
      - Calendar
      - Events
      - Meetings
      - Scheduling
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/graph/api/resources/calendar?view=graph-rest-1.0
      - type: OpenAPI
        url: https://raw.githubusercontent.com/microsoftgraph/msgraph-metadata/master/openapi/v1.0/openapi.yaml
      - type: Authentication
        url: https://learn.microsoft.com/en-us/graph/auth/
      - type: CodeExamples
        url: https://learn.microsoft.com/en-us/graph/api/resources/calendar?view=graph-rest-1.0#code-samples
      - type: GettingStarted
        url: https://learn.microsoft.com/en-us/graph/outlook-calendar-concept-overview
      - type: APIReference
        url: https://learn.microsoft.com/en-us/graph/api/resources/calendar-overview?view=graph-rest-1.0
      - type: SDK
        url: https://learn.microsoft.com/en-us/graph/sdks/sdks-overview
      - type: ChangeLog
        url: https://developer.microsoft.com/en-us/graph/changelog
  - name: Microsoft Graph Contacts API
    description: API for accessing Outlook contacts and contact folders through Microsoft Graph.
    image: https://docs.microsoft.com/en-us/graph/images/microsoft-graph.png
    humanURL: https://learn.microsoft.com/en-us/graph/api/resources/contact?view=graph-rest-1.0
    baseURL: https://graph.microsoft.com/v1.0
    tags:
      - Address Book
      - Contacts
      - People
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/graph/api/resources/contact?view=graph-rest-1.0
      - type: OpenAPI
        url: https://raw.githubusercontent.com/microsoftgraph/msgraph-metadata/master/openapi/v1.0/openapi.yaml
      - type: Authentication
        url: https://learn.microsoft.com/en-us/graph/auth/
      - type: GettingStarted
        url: https://learn.microsoft.com/en-us/graph/outlook-contacts-concept-overview
      - type: APIReference
        url: https://learn.microsoft.com/en-us/graph/api/overview?view=graph-rest-1.0
      - type: SDK
        url: https://learn.microsoft.com/en-us/graph/sdks/sdks-overview
      - type: ChangeLog
        url: https://developer.microsoft.com/en-us/graph/changelog
  - name: Microsoft Graph Tasks API
    description: API for accessing Outlook tasks and to-do items through Microsoft Graph.
    image: https://docs.microsoft.com/en-us/graph/images/microsoft-graph.png
    humanURL: https://learn.microsoft.com/en-us/graph/api/resources/todo-overview?view=graph-rest-1.0
    baseURL: https://graph.microsoft.com/v1.0
    tags:
      - Task Management
      - Tasks
      - To-Do
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/graph/api/resources/todo-overview?view=graph-rest-1.0
      - type: OpenAPI
        url: https://raw.githubusercontent.com/microsoftgraph/msgraph-metadata/master/openapi/v1.0/openapi.yaml
      - type: Authentication
        url: https://learn.microsoft.com/en-us/graph/auth/
      - type: GettingStarted
        url: https://learn.microsoft.com/en-us/graph/todo-concept-overview
      - type: APIReference
        url: https://learn.microsoft.com/en-us/graph/api/overview?view=graph-rest-1.0
      - type: SDK
        url: https://learn.microsoft.com/en-us/graph/sdks/sdks-overview
      - type: ChangeLog
        url: https://developer.microsoft.com/en-us/graph/changelog
  - name: Outlook Add-ins API
    description: JavaScript API for building Outlook add-ins that extend Outlook functionality with custom features, using the Office.js library and the Mailbox requirement set.
    image: https://docs.microsoft.com/en-us/graph/images/microsoft-graph.png
    humanURL: https://learn.microsoft.com/en-us/office/dev/add-ins/outlook/
    baseURL: https://appsforoffice.microsoft.com/lib/1/hosted/office.js
    tags:
      - Add-Ins
      - Extensions
      - Office.js
      - Plugins
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/office/dev/add-ins/outlook/
      - type: GettingStarted
        url: https://learn.microsoft.com/en-us/office/dev/add-ins/quickstarts/outlook-quickstart-yo
      - type: APIReference
        url: https://learn.microsoft.com/en-us/office/dev/add-ins/reference/javascript-api-for-office
      - type: Authentication
        url: https://learn.microsoft.com/en-us/office/dev/add-ins/outlook/microsoft-graph
      - type: GitHubOrganization
        url: https://github.com/OfficeDev/office-js
  - name: Microsoft Graph People API
    description: API for accessing people data relevant to the user, aggregating information from contacts, social networks, organization directory, and recent communications.
    image: https://docs.microsoft.com/en-us/graph/images/microsoft-graph.png
    humanURL: https://learn.microsoft.com/en-us/graph/people-insights-overview
    baseURL: https://graph.microsoft.com/v1.0
    tags:
      - Contacts
      - Directory
      - People
      - Social
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/graph/people-insights-overview
      - type: OpenAPI
        url: https://raw.githubusercontent.com/microsoftgraph/msgraph-metadata/master/openapi/v1.0/openapi.yaml
      - type: Authentication
        url: https://learn.microsoft.com/en-us/graph/auth/
      - type: SDK
        url: https://learn.microsoft.com/en-us/graph/sdks/sdks-overview
      - type: ChangeLog
        url: https://developer.microsoft.com/en-us/graph/changelog
  - name: Microsoft Graph Change Notifications API
    description: API for subscribing to changes in Outlook resources including mail, calendar events, and contacts via webhooks, enabling real-time notifications.
    image: https://docs.microsoft.com/en-us/graph/images/microsoft-graph.png
    humanURL: https://learn.microsoft.com/en-us/graph/outlook-change-notifications-overview
    baseURL: https://graph.microsoft.com/v1.0
    tags:
      - Events
      - Notifications
      - Subscriptions
      - Webhooks
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/graph/outlook-change-notifications-overview
      - type: GettingStarted
        url: https://learn.microsoft.com/en-us/graph/change-notifications-delivery-webhooks
      - type: APIReference
        url: https://learn.microsoft.com/en-us/graph/api/resources/change-notifications-api-overview?view=graph-rest-1.0
      - type: Authentication
        url: https://learn.microsoft.com/en-us/graph/auth/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/microsoftgraph/msgraph-metadata/master/openapi/v1.0/openapi.yaml
      - type: SDK
        url: https://learn.microsoft.com/en-us/graph/sdks/sdks-overview
      - type: ChangeLog
        url: https://developer.microsoft.com/en-us/graph/changelog
  - name: Microsoft Graph Focused Inbox API
    description: API for managing Focused Inbox overrides and message classification, allowing applications to control how incoming messages are categorized between Focused and Other tabs.
    image: https://docs.microsoft.com/en-us/graph/images/microsoft-graph.png
    humanURL: https://learn.microsoft.com/en-us/graph/api/resources/manage-focused-inbox?view=graph-rest-1.0
    baseURL: https://graph.microsoft.com/v1.0
    tags:
      - Classification
      - Email Organization
      - Focused Inbox
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/graph/api/resources/manage-focused-inbox?view=graph-rest-1.0
      - type: Authentication
        url: https://learn.microsoft.com/en-us/graph/auth/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/microsoftgraph/msgraph-metadata/master/openapi/v1.0/openapi.yaml
      - type: SDK
        url: https://learn.microsoft.com/en-us/graph/sdks/sdks-overview
  - name: Microsoft Graph Mail Rules API
    description: API for managing Outlook inbox rules that automatically process incoming messages based on conditions, enabling actions like moving messages to folders, assigning categories, and forwarding.
    image: https://docs.microsoft.com/en-us/graph/images/microsoft-graph.png
    humanURL: https://learn.microsoft.com/en-us/graph/api/resources/messagerule?view=graph-rest-1.0
    baseURL: https://graph.microsoft.com/v1.0
    tags:
      - Email Automation
      - Filters
      - Inbox Rules
      - Rules
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/graph/api/resources/messagerule?view=graph-rest-1.0
      - type: GettingStarted
        url: https://learn.microsoft.com/en-us/graph/outlook-organize-messages
      - type: Authentication
        url: https://learn.microsoft.com/en-us/graph/auth/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/microsoftgraph/msgraph-metadata/master/openapi/v1.0/openapi.yaml
      - type: SDK
        url: https://learn.microsoft.com/en-us/graph/sdks/sdks-overview
  - name: Microsoft Graph Categories API
    description: API for managing Outlook categories, allowing applications to create, read, update, and delete categories in a user's master category list for organizing messages, events, and contacts.
    image: https://docs.microsoft.com/en-us/graph/images/microsoft-graph.png
    humanURL: https://learn.microsoft.com/en-us/graph/api/resources/outlookcategory?view=graph-rest-1.0
    baseURL: https://graph.microsoft.com/v1.0
    tags:
      - Categories
      - Labels
      - Organization
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/graph/api/resources/outlookcategory?view=graph-rest-1.0
      - type: Authentication
        url: https://learn.microsoft.com/en-us/graph/auth/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/microsoftgraph/msgraph-metadata/master/openapi/v1.0/openapi.yaml
      - type: SDK
        url: https://learn.microsoft.com/en-us/graph/sdks/sdks-overview
common:
  - type: Portal
    url: https://developer.microsoft.com/en-us/graph
  - type: GettingStarted
    url: https://learn.microsoft.com/en-us/graph/overview
  - type: Documentation
    url: https://learn.microsoft.com/en-us/outlook/
  - type: Authentication
    url: https://learn.microsoft.com/en-us/graph/auth/
  - type: SDK
    url: https://learn.microsoft.com/en-us/graph/sdks/sdks-overview
  - type: ChangeLog
    url: https://developer.microsoft.com/en-us/graph/changelog
  - type: APIReference
    url: https://learn.microsoft.com/en-us/graph/api/overview?view=graph-rest-1.0
  - type: Blog
    url: https://devblogs.microsoft.com/microsoft365dev/tag/outlook/
  - type: GitHubOrganization
    url: https://github.com/microsoftgraph
  - type: SignUp
    url: https://developer.microsoft.com/en-us/microsoft-365/dev-program
  - type: Login
    url: https://portal.azure.com
  - type: TermsOfService
    url: https://learn.microsoft.com/en-us/legal/microsoft-apis/terms-of-use
  - type: PrivacyPolicy
    url: https://privacy.microsoft.com/en-us/privacystatement
  - type: Support
    url: https://developer.microsoft.com/en-us/graph/support
  - type: StatusPage
    url: https://status.cloud.microsoft/
  - type: StackOverflow
    url: https://stackoverflow.com/questions/tagged/microsoft-graph
  - type: Quickstart
    url: https://developer.microsoft.com/en-us/graph/quick-start
  - type: Training
    url: https://learn.microsoft.com/en-us/training/paths/m365-msgraph-fundamentals/
  - type: Features
    data:
      - Email management with full CRUD operations on messages
      - Calendar scheduling with meeting invitations and RSVPs
      - Contact management across personal and organizational directories
      - Task and to-do list management
      - Focused Inbox classification and mail rules
      - Real-time change notifications via webhooks
      - Rich attachment handling with large file support
      - Categories for organizing messages, events, and contacts
      - People insights aggregated across multiple sources
      - Outlook add-in extensibility via Office.js
  - type: UseCases
    data:
      - Building email client integrations and automation workflows
      - Scheduling meetings and managing calendars programmatically
      - Syncing contacts between systems
      - Creating automated email processing pipelines
      - Building productivity dashboards with mail and calendar data
      - Extending Outlook with custom add-ins
  - type: Integrations
    data:
      - Microsoft Teams
      - Microsoft Power Automate
      - Microsoft Power Apps
      - SharePoint
      - OneDrive
      - Azure Active Directory
      - Microsoft To Do
properties:
  - type: Capabilities
    url: capabilities/email-productivity.yaml
    title: Email Productivity Capability
  - type: Capabilities
    url: capabilities/shared/graph-mail.yaml
    title: Graph Mail API Shared Definition
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
    url: https://apievangelist.com
tags:
  - Calendar
  - Contacts
  - Email
  - Enterprise
  - Microsoft
  - Office 365
  - Productivity
---
