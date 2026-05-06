---
aid: google-workspace
name: Google Workspace
description: A collection of productivity and collaboration tools from Google including Gmail, Drive, Calendar, Meet, and more.
image: https://workspace.google.com/static/img/logo.svg
url: https://raw.githubusercontent.com/api-evangelist/google-workspace/refs/heads/main/apis.yml
created: '2024-01-01'
modified: '2026-04-18'
specificationVersion: '0.19'
type: Index
access: 3rd-Party
tags:
  - Calendar
  - Collaboration
  - Email
  - Productivity
  - Storage
  - Video Conferencing
apis:
  - aid: google-workspace:gmail
    name: Gmail API
    description: Send and read email, manage drafts and labels, and handle mailbox settings.
    image: https://www.gstatic.com/images/branding/product/2x/gmail_2020q4_48dp.png
    humanURL: https://developers.google.com/gmail/api
    baseURL: https://gmail.googleapis.com
    tags:
      - Email
      - Messaging
    properties:
      - type: Documentation
        url: https://developers.google.com/gmail/api/guides
      - type: Authentication
        url: https://developers.google.com/gmail/api/auth/about-auth
      - type: Pricing
        url: https://workspace.google.com/pricing
      - type: APIReference
        url: https://developers.google.com/workspace/gmail/api/reference/rest
      - type: Quickstart
        url: https://developers.google.com/gmail/api/quickstart/python
  - aid: google-workspace:drive
    name: Google Drive API
    description: Store and synchronize files across devices, manage file metadata and permissions.
    image: https://www.gstatic.com/images/branding/product/2x/drive_2020q4_48dp.png
    humanURL: https://developers.google.com/drive/api
    baseURL: https://www.googleapis.com/drive/v3
    tags:
      - Cloud
      - Files
      - Storage
    properties:
      - type: Documentation
        url: https://developers.google.com/drive/api/guides/about-sdk
      - type: Quickstart
        url: https://developers.google.com/drive/api/quickstart/python
      - type: Authentication
        url: https://developers.google.com/drive/api/guides/about-auth
      - type: APIReference
        url: https://developers.google.com/workspace/drive/api/reference/rest/v3
  - aid: google-workspace:calendar
    name: Google Calendar API
    description: Create and manage calendars, events, and attendees.
    image: https://www.gstatic.com/images/branding/product/2x/calendar_2020q4_48dp.png
    humanURL: https://developers.google.com/calendar/api
    baseURL: https://www.googleapis.com/calendar/v3
    tags:
      - Calendar
      - Events
      - Scheduling
    properties:
      - type: Documentation
        url: https://developers.google.com/calendar/api/guides/overview
      - type: CodeExamples
        url: https://developers.google.com/calendar/api/samples
      - type: APIReference
        url: https://developers.google.com/workspace/calendar/api/reference/rest
      - type: Authentication
        url: https://developers.google.com/calendar/api/auth
  - aid: google-workspace:meet
    name: Google Meet REST API
    description: Create and manage video conferencing meetings, spaces, recordings, and transcripts.
    image: https://www.gstatic.com/images/branding/product/2x/meet_2020q4_48dp.png
    humanURL: https://developers.google.com/meet
    baseURL: https://meet.googleapis.com
    tags:
      - Conferencing
      - Meetings
      - Video
    properties:
      - type: Documentation
        url: https://developers.google.com/meet/api/guides/overview
      - type: APIReference
        url: https://developers.google.com/workspace/meet/api/reference/rest/v2
  - aid: google-workspace:docs
    name: Google Docs API
    description: Create and edit documents programmatically.
    image: https://www.gstatic.com/images/branding/product/2x/docs_2020q4_48dp.png
    humanURL: https://developers.google.com/docs/api
    baseURL: https://docs.googleapis.com
    tags:
      - Collaboration
      - Documents
      - Word Processing
    properties:
      - type: Documentation
        url: https://developers.google.com/docs/api/how-tos/overview
      - type: Quickstart
        url: https://developers.google.com/docs/api/quickstart/python
      - type: APIReference
        url: https://developers.google.com/workspace/docs/api/reference/rest
  - aid: google-workspace:sheets
    name: Google Sheets API
    description: Read and write data in Google Sheets.
    image: https://www.gstatic.com/images/branding/product/2x/sheets_2020q4_48dp.png
    humanURL: https://developers.google.com/sheets/api
    baseURL: https://sheets.googleapis.com
    tags:
      - Analytics
      - Data
      - Spreadsheets
    properties:
      - type: Documentation
        url: https://developers.google.com/sheets/api/guides/concepts
      - type: CodeExamples
        url: https://developers.google.com/sheets/api/samples
      - type: Quickstart
        url: https://developers.google.com/sheets/api/quickstart/python
      - type: APIReference
        url: https://developers.google.com/workspace/sheets/api/reference/rest
  - aid: google-workspace:slides
    name: Google Slides API
    description: Create and modify presentations.
    image: https://www.gstatic.com/images/branding/product/2x/slides_2020q4_48dp.png
    humanURL: https://developers.google.com/slides/api
    baseURL: https://slides.googleapis.com
    tags:
      - Presentations
      - Slides
    properties:
      - type: Documentation
        url: https://developers.google.com/slides/api/guides/concepts
      - type: APIReference
        url: https://developers.google.com/workspace/slides/api/reference/rest
      - type: Quickstart
        url: https://developers.google.com/slides/api/quickstart/python
  - aid: google-workspace:admin-directory
    name: Admin SDK Directory API
    description: Manage users, groups, organizational units, and devices in a Google Workspace domain.
    humanURL: https://developers.google.com/admin-sdk/directory
    baseURL: https://admin.googleapis.com
    tags:
      - Admin
      - Groups
      - Management
      - Users
    properties:
      - type: Documentation
        url: https://developers.google.com/admin-sdk/directory/reference/rest
      - type: OpenAPI
        url: openapi/admin-sdk-directory-api.yml
      - type: JSONSchema
        url: json-schema/google-workspace-user-schema.json
      - type: JSONLD
        url: json-ld/google-workspace-context.jsonld
      - type: APIReference
        url: https://developers.google.com/workspace/admin/directory/reference/rest
      - type: Quickstart
        url: https://developers.google.com/admin-sdk/directory/v1/quickstart/python
  - aid: google-workspace:chat
    name: Google Chat API
    description: Build bots and integrations for Google Chat.
    image: https://www.gstatic.com/images/branding/product/2x/chat_2020q4_48dp.png
    humanURL: https://developers.google.com/chat
    baseURL: https://chat.googleapis.com
    tags:
      - Chat
      - Collaboration
      - Messaging
    properties:
      - type: Documentation
        url: https://developers.google.com/chat/api/guides/overview
      - type: APIReference
        url: https://developers.google.com/chat/api/reference/rest
  - aid: google-workspace:admin-reports
    name: Admin SDK Reports API
    description: View audit and usage reports for a Google Workspace domain including user activity and admin actions.
    humanURL: https://developers.google.com/admin-sdk/reports
    baseURL: https://admin.googleapis.com
    tags:
      - Admin
      - Audit
      - Reports
      - Usage
    properties:
      - type: Documentation
        url: https://developers.google.com/workspace/admin/reports/v1/get-start/overview
      - type: APIReference
        url: https://developers.google.com/workspace/admin/reports/reference/rest
      - type: Authentication
        url: https://developers.google.com/admin-sdk/reports/auth
  - aid: google-workspace:forms
    name: Google Forms API
    description: Create and modify forms and quizzes, retrieve form responses and quiz grades.
    humanURL: https://developers.google.com/workspace/forms/api
    baseURL: https://forms.googleapis.com
    tags:
      - Forms
      - Quizzes
      - Surveys
    properties:
      - type: Documentation
        url: https://developers.google.com/workspace/forms/api/guides
      - type: APIReference
        url: https://developers.google.com/workspace/forms/api/reference/rest
      - type: Quickstart
        url: https://developers.google.com/workspace/forms/api/quickstart/python
  - aid: google-workspace:tasks
    name: Google Tasks API
    description: Search, read, and update Google Tasks content and metadata.
    humanURL: https://developers.google.com/tasks
    baseURL: https://tasks.googleapis.com
    tags:
      - Productivity
      - Tasks
      - To-Do
    properties:
      - type: Documentation
        url: https://developers.google.com/workspace/tasks/overview
      - type: APIReference
        url: https://developers.google.com/workspace/tasks/reference/rest
      - type: Quickstart
        url: https://developers.google.com/tasks/quickstart/js
  - aid: google-workspace:keep
    name: Google Keep API
    description: Manage Google Keep notes including creating, listing, and deleting notes and managing permissions.
    humanURL: https://developers.google.com/workspace/keep
    baseURL: https://keep.googleapis.com
    tags:
      - Notes
      - Productivity
    properties:
      - type: Documentation
        url: https://developers.google.com/workspace/keep/api/guides
      - type: APIReference
        url: https://developers.google.com/workspace/keep/api/reference/rest
  - aid: google-workspace:vault
    name: Google Vault API
    description: Manage eDiscovery for your organization including matters, holds, and exports across Google Workspace services.
    humanURL: https://developers.google.com/workspace/vault
    baseURL: https://vault.googleapis.com
    tags:
      - Compliance
      - Ediscovery
      - Legal
    properties:
      - type: Documentation
        url: https://developers.google.com/workspace/vault/guides
      - type: APIReference
        url: https://developers.google.com/workspace/vault/reference/rest
  - aid: google-workspace:classroom
    name: Google Classroom API
    description: Manage classes, rosters, invitations, and coursework in Google Classroom.
    humanURL: https://developers.google.com/workspace/classroom
    baseURL: https://classroom.googleapis.com
    tags:
      - Classroom
      - Education
      - Learning
    properties:
      - type: Documentation
        url: https://developers.google.com/workspace/classroom/guides/get-started
      - type: APIReference
        url: https://developers.google.com/workspace/classroom/reference/rest
  - aid: google-workspace:people
    name: People API
    description: Read and manage the authenticated user contacts and profiles, and search the directory.
    humanURL: https://developers.google.com/people
    baseURL: https://people.googleapis.com
    tags:
      - Contacts
      - Directory
      - People
    properties:
      - type: Documentation
        url: https://developers.google.com/people
      - type: APIReference
        url: https://developers.google.com/people/api/rest
  - aid: google-workspace:cloud-search
    name: Google Cloud Search API
    description: Index non-Google Workspace data and search across all organizational data sources.
    humanURL: https://developers.google.com/workspace/cloud-search
    baseURL: https://cloudsearch.googleapis.com
    tags:
      - Enterprise Search
      - Indexing
      - Search
    properties:
      - type: Documentation
        url: https://developers.google.com/workspace/cloud-search/docs/guides/project-setup
      - type: APIReference
        url: https://developers.google.com/workspace/cloud-search/docs/reference/rest
  - aid: google-workspace:drive-activity
    name: Drive Activity API
    description: Retrieve information about changes made to objects within a user Google Drive.
    humanURL: https://developers.google.com/drive/activity/v2
    baseURL: https://driveactivity.googleapis.com
    tags:
      - Activity
      - Audit
      - Drive
    properties:
      - type: Documentation
        url: https://developers.google.com/drive/activity/v2
      - type: APIReference
        url: https://developers.google.com/workspace/drive/activity/v2/reference/rest
  - aid: google-workspace:drive-labels
    name: Drive Labels API
    description: Create and manage labels to organize and classify files in Google Drive.
    humanURL: https://developers.google.com/workspace/drive/labels/guides/overview
    baseURL: https://drivelabels.googleapis.com
    tags:
      - Drive
      - Labels
      - Metadata
    properties:
      - type: Documentation
        url: https://developers.google.com/workspace/drive/labels/guides/overview
      - type: APIReference
        url: https://developers.google.com/workspace/drive/labels/reference/rest/v2
  - aid: google-workspace:alert-center
    name: Alert Center API
    description: Manage alerts on issues affecting your Google Workspace domain including security and compliance warnings.
    humanURL: https://developers.google.com/workspace/admin/alertcenter/guides
    baseURL: https://alertcenter.googleapis.com
    tags:
      - Admin
      - Alerts
      - Security
    properties:
      - type: Documentation
        url: https://developers.google.com/workspace/admin/alertcenter/guides
      - type: APIReference
        url: https://developers.google.com/workspace/admin/alertcenter/reference/rest
      - type: Authentication
        url: https://developers.google.com/workspace/admin/alertcenter/guides/auth
  - aid: google-workspace:groups-settings
    name: Groups Settings API
    description: Update and retrieve settings for existing Google Groups including permissions and access controls.
    humanURL: https://developers.google.com/admin-sdk/groups-settings/concepts
    baseURL: https://www.googleapis.com/groups/v1
    tags:
      - Admin
      - Groups
      - Settings
    properties:
      - type: Documentation
        url: https://developers.google.com/admin-sdk/groups-settings/concepts
      - type: APIReference
        url: https://developers.google.com/admin-sdk/groups-settings/v1/reference
  - aid: google-workspace:groups-migration
    name: Groups Migration API
    description: Migrate shared emails from public folders and distribution lists to Google Groups discussion archives.
    humanURL: https://developers.google.com/workspace/admin/groups-migration/v1/guides/overview
    baseURL: https://groupsmigration.googleapis.com
    tags:
      - Admin
      - Groups
      - Migration
    properties:
      - type: Documentation
        url: https://developers.google.com/workspace/admin/groups-migration/v1/guides/overview
      - type: Authentication
        url: https://developers.google.com/workspace/admin/groups-migration/v1/guides/authorizing
  - aid: google-workspace:data-transfer
    name: Admin SDK Data Transfer API
    description: Transfer ownership of user data from one user to another within a domain.
    humanURL: https://developers.google.com/workspace/admin/data-transfer
    baseURL: https://admin.googleapis.com
    tags:
      - Admin
      - Data Transfer
      - Migration
    properties:
      - type: Documentation
        url: https://developers.google.com/workspace/admin/data-transfer
      - type: APIReference
        url: https://developers.google.com/workspace/admin/data-transfer/reference/rest
  - aid: google-workspace:license-manager
    name: Enterprise License Manager API
    description: Manage Google Workspace and related product licenses for all users of a customer.
    humanURL: https://developers.google.com/admin-sdk/licensing
    baseURL: https://licensing.googleapis.com
    tags:
      - Admin
      - Licensing
      - Management
    properties:
      - type: Documentation
        url: https://developers.google.com/admin-sdk/licensing/v1/how-tos/using
      - type: APIReference
        url: https://developers.google.com/workspace/admin/licensing/reference/rest
      - type: Authentication
        url: https://developers.google.com/admin-sdk/licensing/v1/how-tos/authorizing
  - aid: google-workspace:reseller
    name: Google Workspace Reseller API
    description: Perform common reseller functions at scale including placing orders and managing customer subscriptions.
    humanURL: https://developers.google.com/workspace/admin/reseller/v1/how-tos/concepts
    baseURL: https://reseller.googleapis.com
    tags:
      - Admin
      - Reseller
      - Subscriptions
    properties:
      - type: Documentation
        url: https://developers.google.com/workspace/admin/reseller/v1/how-tos/concepts
      - type: APIReference
        url: https://developers.google.com/workspace/admin/reseller/reference/rest
      - type: Authentication
        url: https://developers.google.com/workspace/admin/reseller/v1/how-tos/authorize
  - aid: google-workspace:postmaster
    name: Gmail Postmaster Tools API
    description: Gather statistics on bulk emails sent to Gmail users including spam reports and delivery errors.
    humanURL: https://developers.google.com/workspace/gmail/postmaster
    baseURL: https://gmailpostmastertools.googleapis.com
    tags:
      - Deliverability
      - Email
      - Postmaster
    properties:
      - type: Documentation
        url: https://developers.google.com/workspace/gmail/postmaster
      - type: APIReference
        url: https://developers.google.com/workspace/gmail/postmaster/reference/rest
  - aid: google-workspace:marketplace
    name: Google Workspace Marketplace API
    description: Manage customer and user license status for Google Workspace Marketplace applications.
    humanURL: https://developers.google.com/workspace/marketplace/overview
    baseURL: https://appsmarket.googleapis.com
    tags:
      - Apps
      - Licensing
      - Marketplace
    properties:
      - type: Documentation
        url: https://developers.google.com/workspace/marketplace/overview
      - type: APIReference
        url: https://developers.google.com/workspace/marketplace/reference/rest
      - type: Authentication
        url: https://developers.google.com/workspace/marketplace/authorizing
common:
  - type: Console
    url: https://console.cloud.google.com
  - type: Authentication
    url: https://developers.google.com/identity/protocols/oauth2
  - type: TermsOfService
    url: https://workspace.google.com/terms/service-terms/
  - type: Support
    url: https://support.google.com/workspace
  - type: StatusPage
    url: https://www.google.com/appsstatus/dashboard/
  - type: DeveloperPortal
    url: https://developers.google.com/workspace
  - type: Pricing
    url: https://workspace.google.com/pricing
  - type: Blog
    url: https://workspaceupdates.googleblog.com
  - type: ReleaseNotes
    url: https://developers.google.com/workspace/release-notes
  - type: GettingStarted
    url: https://developers.google.com/workspace/guides/get-started
  - type: SDK
    url: https://developers.google.com/workspace/guides/libraries
  - type: NaftikoCapability
    url: capabilities/shared/admin-directory.yaml
    title: Admin SDK Directory API Shared Definition
  - type: NaftikoCapability
    url: capabilities/domain-administration.yaml
    title: Domain Administration Workflow
  - type: Features
    data:
      - name: Email and Communication
        description: Send, receive, and manage email with Gmail API, build chat bots with Chat API, and host video meetings with Meet API.
      - name: Document Collaboration
        description: Create and edit documents, spreadsheets, presentations, and forms programmatically across Google Workspace apps.
      - name: File Storage and Management
        description: Store, sync, and manage files with Drive API including permissions, metadata, labels, and activity tracking.
      - name: Directory and User Management
        description: Manage users, groups, organizational units, and devices across a Google Workspace domain with Admin SDK.
      - name: Calendar and Scheduling
        description: Create and manage calendars, events, and attendees with automatic conflict detection and resource booking.
      - name: Security and Compliance
        description: Monitor security alerts, manage eDiscovery holds, and generate audit reports for compliance requirements.
      - name: Enterprise Search
        description: Index and search across Google Workspace and external data sources with Cloud Search API.
      - name: Task and Note Management
        description: Manage tasks and notes programmatically with Tasks API and Keep API for productivity workflows.
  - type: UseCases
    data:
      - name: Automated Onboarding
        description: Provision user accounts, assign groups and licenses, and configure organizational units for new employee onboarding.
      - name: Document Workflow Automation
        description: Automate document creation, approval workflows, and distribution using Docs, Sheets, and Drive APIs.
      - name: Meeting Management
        description: Schedule meetings, manage recordings and transcripts, and integrate video conferencing into custom applications.
      - name: Security Monitoring
        description: Monitor security alerts, audit user activity, and enforce compliance policies across the Google Workspace domain.
      - name: Customer Communication
        description: Automate email campaigns, manage support inboxes, and integrate Gmail with CRM and helpdesk systems.
  - type: Integrations
    data:
      - name: Salesforce
        description: Sync contacts, calendar events, and emails between Google Workspace and Salesforce CRM.
      - name: Slack
        description: Bridge Google Workspace content and notifications with Slack channels for unified collaboration.
      - name: Microsoft 365
        description: Interoperability support for document sharing and calendar synchronization with Microsoft Office apps.
      - name: Jira
        description: Link Google Drive files, create documents from Jira issues, and sync calendar events with project timelines.
      - name: Zapier
        description: Connect Google Workspace apps with thousands of services through Zapier automation workflows.
      - name: Asana
        description: Integrate Google Drive attachments, Calendar events, and Gmail notifications with Asana project management.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
