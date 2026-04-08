---
aid: microsoft-office-365
url: https://raw.githubusercontent.com/api-evangelist/microsoft-office-365/refs/heads/main/apis.yml
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
  - type: X-documentation
    url: https://docs.microsoft.com/en-us/graph/overview
  - type: X-openapi
    url: https://raw.githubusercontent.com/microsoftgraph/microsoft-graph-openapi/master/openapi/v1.0/openapi.yaml
  - type: X-openapi-local
    url: openapi/microsoft-graph-api-openapi.yml
  - type: X-json-ld-context
    url: json-ld/microsoft-office-365-context.jsonld
  - type: X-pricing
    url: https://azure.microsoft.com/en-us/pricing/details/active-directory/
  - type: X-authentication
    url: https://docs.microsoft.com/en-us/graph/auth/
  - type: X-postman-collection
    url: https://www.postman.com/microsoftgraph/workspace/microsoft-graph/overview
  - type: X-terms-of-service
    url: https://docs.microsoft.com/en-us/legal/microsoft-apis/terms-of-use
  - type: X-rate-limits
    url: https://docs.microsoft.com/en-us/graph/throttling
  - type: X-getting-started
    url: https://learn.microsoft.com/en-us/graph/use-the-api
  - type: X-sdks
    url: https://learn.microsoft.com/en-us/graph/sdks/sdks-overview
  - type: X-change-notifications
    url: https://learn.microsoft.com/en-us/graph/change-notifications-overview
  - type: X-versioning
    url: https://learn.microsoft.com/en-us/graph/versioning-and-support
  - type: X-graph-explorer
    url: https://developer.microsoft.com/en-us/graph/graph-explorer
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
  - type: X-documentation
    url: https://docs.microsoft.com/en-us/graph/api/resources/message
  - type: X-openapi
    url: https://raw.githubusercontent.com/microsoftgraph/microsoft-graph-openapi/master/openapi/v1.0/mail.yaml
  - type: X-openapi-local
    url: openapi/microsoft-graph-api-openapi.yml
  - type: X-change-notifications
    url: https://learn.microsoft.com/en-us/graph/outlook-change-notifications-overview
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
  - type: X-documentation
    url: https://docs.microsoft.com/en-us/graph/api/resources/event
  - type: X-openapi
    url: https://raw.githubusercontent.com/microsoftgraph/microsoft-graph-openapi/master/openapi/v1.0/calendar.yaml
  - type: X-openapi-local
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
  - type: X-documentation
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
  - type: X-documentation
    url: https://docs.microsoft.com/en-us/graph/api/resources/driveitem
  - type: X-openapi
    url: https://raw.githubusercontent.com/microsoftgraph/microsoft-graph-openapi/master/openapi/v1.0/files.yaml
  - type: X-getting-started
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
  - type: X-documentation
    url: https://docs.microsoft.com/en-us/graph/api/resources/site
  - type: X-openapi
    url: https://raw.githubusercontent.com/microsoftgraph/microsoft-graph-openapi/master/openapi/v1.0/sites.yaml
  - type: X-sharepoint-rest-v2
    url: https://learn.microsoft.com/en-us/sharepoint/dev/apis/sharepoint-rest-graph
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
  - type: X-documentation
    url: https://docs.microsoft.com/en-us/graph/api/resources/team
  - type: X-openapi
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
  - type: X-documentation
    url: https://docs.microsoft.com/en-us/graph/api/resources/user
  - type: X-openapi
    url: https://raw.githubusercontent.com/microsoftgraph/microsoft-graph-openapi/master/openapi/v1.0/users.yaml
  - type: X-json-schema
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
  - type: X-documentation
    url: https://docs.microsoft.com/en-us/graph/api/resources/planner-overview
  - type: X-openapi
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
  - type: X-documentation
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
  - type: X-documentation
    url: https://learn.microsoft.com/en-us/graph/api/resources/excel?view=graph-rest-1.0
  - type: X-best-practices
    url: https://learn.microsoft.com/en-us/graph/workbook-best-practice
  - type: X-sessions
    url: https://learn.microsoft.com/en-us/graph/excel-manage-sessions
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
  - type: X-documentation
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
  - type: X-documentation
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
  - type: X-documentation
    url: https://learn.microsoft.com/en-us/graph/api/resources/group?view=graph-rest-1.0
  - type: X-openapi-local
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
  - type: X-documentation
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
  - type: X-documentation
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
  - type: X-documentation
    url: https://learn.microsoft.com/en-us/office/dev/add-ins/
  - type: X-javascript-api-reference
    url: https://learn.microsoft.com/en-us/office/dev/add-ins/reference/javascript-api-for-office
  - type: X-getting-started
    url: https://learn.microsoft.com/en-us/office/dev/add-ins/overview/learning-path-beginner
  - type: X-development-guide
    url: https://learn.microsoft.com/en-us/office/dev/add-ins/develop/develop-overview
name: Microsoft Office 365
tags:
- Cloud
- Collaboration
- Enterprise
- Microsoft
- Productivity
type: Contract
image: https://www.microsoft.com/en-us/microsoft-365/blog/wp-content/uploads/sites/2/2020/04/Microsoft-365.png
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: A collection of APIs provided by Microsoft Office 365 for productivity, collaboration, and enterprise services.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

