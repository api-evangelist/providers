---
aid: microsoft-office-365
name: Microsoft Office 365
description: A collection of APIs provided by Microsoft Office 365 for productivity, collaboration, and enterprise services.
image: https://www.microsoft.com/en-us/microsoft-365/blog/wp-content/uploads/sites/2/2020/04/Microsoft-365.png
url: https://www.microsoft.com/en-us/microsoft-365
created: '2024-01-15'
modified: '2026-04-18'
specificationVersion: '0.19'
tags:
  - Cloud
  - Collaboration
  - Enterprise
  - Microsoft
  - Productivity
apis:
  - name: Microsoft Graph API
    description: Unified API endpoint to access data, intelligence, and insights from Microsoft 365, Windows, and Enterprise Mobility + Security.
    image: https://docs.microsoft.com/en-us/graph/images/microsoft-graph.png
    humanURL: https://developer.microsoft.com/en-us/graph
    baseURL: https://graph.microsoft.com
    tags:
      - Calendar
      - Graph
      - Groups
      - Mail
      - Unified
      - Users
    properties:
      - type: Documentation
        url: https://docs.microsoft.com/en-us/graph/overview
      - type: OpenAPI
        url: https://raw.githubusercontent.com/microsoftgraph/microsoft-graph-openapi/master/openapi/v1.0/openapi.yaml
      - type: OpenAPI
        url: openapi/microsoft-graph-api-openapi.yml
      - type: JSONLD
        url: json-ld/microsoft-office-365-context.jsonld
      - type: Pricing
        url: https://azure.microsoft.com/en-us/pricing/details/active-directory/
      - type: Authentication
        url: https://docs.microsoft.com/en-us/graph/auth/
      - type: Documentation
        url: https://www.postman.com/microsoftgraph/workspace/microsoft-graph/overview
        title: Postman Collection
      - type: TermsOfService
        url: https://docs.microsoft.com/en-us/legal/microsoft-apis/terms-of-use
      - type: RateLimits
        url: https://docs.microsoft.com/en-us/graph/throttling
      - type: GettingStarted
        url: https://learn.microsoft.com/en-us/graph/use-the-api
      - type: SDK
        url: https://learn.microsoft.com/en-us/graph/sdks/sdks-overview
      - type: Documentation
        url: https://learn.microsoft.com/en-us/graph/change-notifications-overview
        title: Change Notifications
      - type: Versioning
        url: https://learn.microsoft.com/en-us/graph/versioning-and-support
      - type: Console
        url: https://developer.microsoft.com/en-us/graph/graph-explorer
        title: Graph Explorer
  - name: Outlook Mail API
    description: Access to Outlook email, including reading, sending, and managing messages.
    humanURL: https://docs.microsoft.com/en-us/graph/api/resources/mail-api-overview
    baseURL: https://graph.microsoft.com/v1.0/me/messages
    tags:
      - Email
      - Mail
      - Messages
      - Outlook
    properties:
      - type: Documentation
        url: https://docs.microsoft.com/en-us/graph/api/resources/message
      - type: OpenAPI
        url: https://raw.githubusercontent.com/microsoftgraph/microsoft-graph-openapi/master/openapi/v1.0/mail.yaml
      - type: OpenAPI
        url: openapi/microsoft-graph-api-openapi.yml
      - type: Documentation
        url: https://learn.microsoft.com/en-us/graph/outlook-change-notifications-overview
        title: Change Notifications
  - name: Outlook Calendar API
    description: Access to Outlook calendar events, scheduling, and meeting management.
    humanURL: https://docs.microsoft.com/en-us/graph/api/resources/calendar
    baseURL: https://graph.microsoft.com/v1.0/me/calendar
    tags:
      - Calendar
      - Events
      - Meetings
      - Scheduling
    properties:
      - type: Documentation
        url: https://docs.microsoft.com/en-us/graph/api/resources/event
      - type: OpenAPI
        url: https://raw.githubusercontent.com/microsoftgraph/microsoft-graph-openapi/master/openapi/v1.0/calendar.yaml
      - type: OpenAPI
        url: openapi/microsoft-graph-api-openapi.yml
  - name: Outlook Contacts API
    description: Access to Outlook personal contacts for managing contact information, creating contact folders, and organizing people data.
    humanURL: https://learn.microsoft.com/en-us/graph/outlook-contacts-concept-overview
    baseURL: https://graph.microsoft.com/v1.0/me/contacts
    tags:
      - Address-Book
      - Contacts
      - Outlook
      - People
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/graph/api/resources/contact?view=graph-rest-1.0
  - name: OneDrive API
    description: Access to OneDrive file storage, sharing, and collaboration features.
    humanURL: https://docs.microsoft.com/en-us/graph/api/resources/onedrive
    baseURL: https://graph.microsoft.com/v1.0/me/drive
    tags:
      - Files
      - Onedrive
      - Sharing
      - Storage
    properties:
      - type: Documentation
        url: https://docs.microsoft.com/en-us/graph/api/resources/driveitem
      - type: OpenAPI
        url: https://raw.githubusercontent.com/microsoftgraph/microsoft-graph-openapi/master/openapi/v1.0/files.yaml
      - type: GettingStarted
        url: https://learn.microsoft.com/en-us/onedrive/developer/rest-api/?view=odsp-graph-online
  - name: SharePoint API
    description: Access to SharePoint sites, lists, and document libraries.
    humanURL: https://docs.microsoft.com/en-us/graph/api/resources/sharepoint
    baseURL: https://graph.microsoft.com/v1.0/sites
    tags:
      - Collaboration
      - Lists
      - Sharepoint
      - Sites
    properties:
      - type: Documentation
        url: https://docs.microsoft.com/en-us/graph/api/resources/site
      - type: OpenAPI
        url: https://raw.githubusercontent.com/microsoftgraph/microsoft-graph-openapi/master/openapi/v1.0/sites.yaml
      - type: Documentation
        url: https://learn.microsoft.com/en-us/sharepoint/dev/apis/sharepoint-rest-graph
        title: SharePoint REST v2
  - name: Microsoft Teams API
    description: Access to Microsoft Teams channels, messages, and collaboration features.
    humanURL: https://docs.microsoft.com/en-us/graph/api/resources/teams-api-overview
    baseURL: https://graph.microsoft.com/v1.0/teams
    tags:
      - Channels
      - Chat
      - Collaboration
      - Teams
    properties:
      - type: Documentation
        url: https://docs.microsoft.com/en-us/graph/api/resources/team
      - type: OpenAPI
        url: https://raw.githubusercontent.com/microsoftgraph/microsoft-graph-openapi/master/openapi/v1.0/teams.yaml
  - name: Office 365 Users API
    description: Manage Office 365 users, profiles, and organizational information.
    humanURL: https://docs.microsoft.com/en-us/graph/api/resources/user
    baseURL: https://graph.microsoft.com/v1.0/users
    tags:
      - Directory
      - Identity
      - Profiles
      - Users
    properties:
      - type: Documentation
        url: https://docs.microsoft.com/en-us/graph/api/resources/user
      - type: OpenAPI
        url: https://raw.githubusercontent.com/microsoftgraph/microsoft-graph-openapi/master/openapi/v1.0/users.yaml
      - type: JSONSchema
        url: json-schema/microsoft-office-365-user-schema.json
  - name: Planner API
    description: Access to Microsoft Planner tasks, plans, and project management features.
    humanURL: https://docs.microsoft.com/en-us/graph/api/resources/planner-overview
    baseURL: https://graph.microsoft.com/v1.0/planner
    tags:
      - Planner
      - Planning
      - Projects
      - Tasks
    properties:
      - type: Documentation
        url: https://docs.microsoft.com/en-us/graph/api/resources/planner-overview
      - type: OpenAPI
        url: https://raw.githubusercontent.com/microsoftgraph/microsoft-graph-openapi/master/openapi/v1.0/planner.yaml
  - name: OneNote API
    description: Access to OneNote notebooks, sections, and pages for creating and managing notes and structured content.
    humanURL: https://learn.microsoft.com/en-us/graph/integrate-with-onenote
    baseURL: https://graph.microsoft.com/v1.0/me/onenote
    tags:
      - Notebooks
      - Notes
      - Onenote
      - Pages
      - Sections
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/graph/api/resources/onenote-api-overview?view=graph-rest-1.0
  - name: Excel Workbooks and Charts API
    description: Read and modify Excel workbooks stored in OneDrive and SharePoint, including managing worksheets, tables, charts, ranges, and sessions.
    humanURL: https://learn.microsoft.com/en-us/graph/excel-concept-overview
    baseURL: https://graph.microsoft.com/v1.0/me/drive/items/{id}/workbook
    tags:
      - Charts
      - Excel
      - Spreadsheets
      - Tables
      - Workbooks
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/graph/api/resources/excel?view=graph-rest-1.0
      - type: BestPractices
        url: https://learn.microsoft.com/en-us/graph/workbook-best-practice
      - type: Documentation
        url: https://learn.microsoft.com/en-us/graph/excel-manage-sessions
        title: Session Management
  - name: Microsoft To Do API
    description: Manage tasks and task lists across To Do clients, Outlook, and Teams for personal task management and day planning.
    humanURL: https://learn.microsoft.com/en-us/graph/todo-concept-overview
    baseURL: https://graph.microsoft.com/v1.0/me/todo
    tags:
      - Productivity
      - Task-Lists
      - Tasks
      - Todo
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/graph/todo-concept-overview
  - name: Microsoft Bookings API
    description: Manage customer bookings, appointment scheduling, business services, and staff information for enterprise and small business owners.
    humanURL: https://learn.microsoft.com/en-us/graph/booking-concept-overview
    baseURL: https://graph.microsoft.com/v1.0/solutions/bookingBusinesses
    tags:
      - Appointments
      - Bookings
      - Business
      - Scheduling
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/graph/api/resources/booking-api-overview?view=graph-rest-1.0
  - name: Office 365 Groups API
    description: Manage Microsoft 365 groups, group membership, conversations, and group-related resources for collaboration.
    humanURL: https://learn.microsoft.com/en-us/graph/api/resources/groups-overview?view=graph-rest-1.0
    baseURL: https://graph.microsoft.com/v1.0/groups
    tags:
      - Collaboration
      - Groups
      - Membership
      - Teams
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/graph/api/resources/group?view=graph-rest-1.0
      - type: OpenAPI
        url: openapi/microsoft-graph-api-openapi.yml
  - name: Microsoft Graph Security API
    description: Connect security products, services, and partners to streamline security operations and improve threat protection, detection, and response.
    humanURL: https://learn.microsoft.com/en-us/graph/security-concept-overview
    baseURL: https://graph.microsoft.com/v1.0/security
    tags:
      - Alerts
      - Compliance
      - Security
      - Threats
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/graph/api/resources/security-api-overview?view=graph-rest-1.0
  - name: Microsoft Graph Communications API
    description: Create and join online meetings, manage call records, and enable cloud communications capabilities for applications.
    humanURL: https://learn.microsoft.com/en-us/graph/cloud-communications-online-meetings
    baseURL: https://graph.microsoft.com/v1.0/communications
    tags:
      - Calls
      - Communications
      - Meetings
      - Online-Meetings
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/graph/cloud-communications-online-meetings
  - name: Office Add-ins Platform
    description: Platform for building solutions that extend Office applications including Excel, Outlook, Word, PowerPoint, and OneNote using web technologies and the Office JavaScript API.
    humanURL: https://learn.microsoft.com/en-us/office/dev/add-ins/overview/office-add-ins
    tags:
      - Add-Ins
      - Excel
      - Extensions
      - Office-Js
      - Outlook
      - Powerpoint
      - Word
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/office/dev/add-ins/
      - type: APIReference
        url: https://learn.microsoft.com/en-us/office/dev/add-ins/reference/javascript-api-for-office
        title: JavaScript API Reference
      - type: GettingStarted
        url: https://learn.microsoft.com/en-us/office/dev/add-ins/overview/learning-path-beginner
      - type: Documentation
        url: https://learn.microsoft.com/en-us/office/dev/add-ins/develop/develop-overview
        title: Development Guide
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
    url: https://apievangelist.com
common:
  - type: DeveloperPortal
    url: https://developer.microsoft.com/en-us/microsoft-365
  - type: StatusPage
    url: https://status.office365.com/
  - type: Support
    url: https://developer.microsoft.com/en-us/graph/support
  - type: Blog
    url: https://developer.microsoft.com/en-us/graph/blogs/
  - type: GitHubOrganization
    url: https://github.com/microsoftgraph
  - type: PrivacyPolicy
    url: https://privacy.microsoft.com/en-us/privacystatement
  - type: Console
    url: https://developer.microsoft.com/en-us/graph/graph-explorer
    title: Graph Explorer
  - type: SDK
    url: https://learn.microsoft.com/en-us/graph/sdks/sdks-overview
  - type: ChangeLog
    url: https://developer.microsoft.com/en-us/graph/changelog
  - type: ReleaseNotes
    url: https://learn.microsoft.com/en-us/graph/whats-new-overview
    title: What's New
  - type: Authentication
    url: https://learn.microsoft.com/en-us/graph/auth/
  - type: TermsOfService
    url: https://docs.microsoft.com/en-us/legal/microsoft-apis/terms-of-use
  - type: RateLimits
    url: https://learn.microsoft.com/en-us/graph/throttling
  - type: Documentation
    url: https://learn.microsoft.com/en-us/graph/change-notifications-delivery-webhooks
    title: Webhooks
  - type: Quickstart
    url: https://developer.microsoft.com/en-us/graph/quick-start
  - type: APIReference
    url: https://learn.microsoft.com/en-us/graph/api/overview?view=graph-rest-1.0
  - type: Compliance
    url: https://learn.microsoft.com/en-us/graph/compliance-concept-overview
  - type: SpectralRules
    url: rules/microsoft-office-365-spectral-rules.yml
  - type: NaftikoCapability
    url: capabilities/shared/graph-api.yaml
    title: Microsoft Graph API Shared Definition
  - type: NaftikoCapability
    url: capabilities/productivity-and-collaboration.yaml
    title: Productivity and Collaboration Workflow
  - type: Features
    url: https://developer.microsoft.com/en-us/graph
    data:
      - name: Unified API Endpoint
        description: Access Microsoft 365 data through a single REST endpoint at graph.microsoft.com covering mail, calendar, files, users, and groups.
      - name: Real-Time Notifications
        description: Subscribe to change notifications via webhooks to receive real-time updates when data changes across Microsoft 365 services.
      - name: Batch Requests
        description: Combine multiple API requests into a single HTTP call to reduce network overhead and improve performance.
      - name: Delta Queries
        description: Track incremental changes to resources efficiently using delta links without polling entire datasets.
      - name: Rich Mail Management
        description: Read, send, reply, forward, and organize email messages with full attachment and folder support.
      - name: Calendar and Scheduling
        description: Create events, manage calendars, check free/busy availability, and handle meeting responses programmatically.
      - name: File Storage and Sharing
        description: Access OneDrive and SharePoint files with upload, download, sharing, and real-time collaboration capabilities.
      - name: Team Collaboration
        description: Manage Microsoft Teams channels, messages, tabs, and apps for team communication and collaboration.
      - name: User and Group Management
        description: Create, update, and manage users, groups, and organizational directory resources.
  - type: UseCases
    url: https://developer.microsoft.com/en-us/graph
    data:
      - name: Enterprise Productivity Integration
        description: Build applications that integrate email, calendar, and file management into unified productivity workflows.
      - name: Automated Reporting
        description: Generate automated reports by pulling data from mail, calendar, and user profiles across the organization.
      - name: Identity and Access Management
        description: Manage user provisioning, group membership, and directory synchronization for enterprise identity workflows.
      - name: Team Communication Automation
        description: Automate team notifications, channel management, and messaging workflows across Microsoft Teams.
      - name: Document Collaboration
        description: Enable multi-user document editing, sharing, and version tracking through OneDrive and SharePoint APIs.
  - type: Integrations
    url: https://developer.microsoft.com/en-us/graph
    data:
      - name: Azure Active Directory
        description: Integrate with Azure AD for user authentication, authorization, and directory management.
      - name: Microsoft Teams
        description: Build bots, tabs, and messaging extensions that integrate with Microsoft Teams collaboration platform.
      - name: Power Automate
        description: Connect Microsoft Graph data to Power Automate flows for no-code/low-code automation.
      - name: Power BI
        description: Feed Microsoft 365 data into Power BI dashboards for business intelligence and reporting.
      - name: SharePoint
        description: Access SharePoint sites, lists, and document libraries for enterprise content management.
      - name: Outlook
        description: Integrate with Outlook mail, calendar, and contacts for personal and shared mailbox management.
---
