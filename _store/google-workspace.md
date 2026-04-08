---
aid: google-workspace
url: https://raw.githubusercontent.com/api-evangelist/google-workspace/refs/heads/main/apis.yml
apis:
- name: Gmail API
  description: Send and read email, manage drafts and labels, and handle mailbox settings.
  image: https://www.gstatic.com/images/branding/product/2x/gmail_2020q4_48dp.png
  humanUrl: https://developers.google.com/gmail/api
  baseUrl: https://gmail.googleapis.com
  tags:
  - Email
  - Messaging
  properties:
  - type: Documentation
    url: https://developers.google.com/gmail/api/guides
  - type: OpenAPI
    url: https://gmail.googleapis.com/$discovery/rest?version=v1
  - type: Authentication
    url: https://developers.google.com/gmail/api/auth/about-auth
  - type: Pricing
    url: https://workspace.google.com/pricing
  - type: Reference
    url: https://developers.google.com/workspace/gmail/api/reference/rest
  - type: Quick Start
    url: https://developers.google.com/gmail/api/quickstart/python
- name: Google Drive API
  description: Store and synchronize files across devices, manage file metadata and permissions.
  image: https://www.gstatic.com/images/branding/product/2x/drive_2020q4_48dp.png
  humanUrl: https://developers.google.com/drive/api
  baseUrl: https://www.googleapis.com/drive/v3
  tags:
  - Cloud
  - Files
  - Storage
  properties:
  - type: Documentation
    url: https://developers.google.com/drive/api/guides/about-sdk
  - type: OpenAPI
    url: https://www.googleapis.com/discovery/v1/apis/drive/v3/rest
  - type: Quick Start
    url: https://developers.google.com/drive/api/quickstart/python
  - type: Authentication
    url: https://developers.google.com/drive/api/guides/about-auth
  - type: Reference
    url: https://developers.google.com/workspace/drive/api/reference/rest/v3
- name: Google Calendar API
  description: Create and manage calendars, events, and attendees.
  image: https://www.gstatic.com/images/branding/product/2x/calendar_2020q4_48dp.png
  humanUrl: https://developers.google.com/calendar/api
  baseUrl: https://www.googleapis.com/calendar/v3
  tags:
  - Calendar
  - Events
  - Scheduling
  properties:
  - type: Documentation
    url: https://developers.google.com/calendar/api/guides/overview
  - type: OpenAPI
    url: https://www.googleapis.com/discovery/v1/apis/calendar/v3/rest
  - type: Quick Start
    url: https://developers.google.com/calendar/api/quickstart/js
  - type: Samples
    url: https://developers.google.com/calendar/api/samples
  - type: Reference
    url: https://developers.google.com/workspace/calendar/api/reference/rest
  - type: Authentication
    url: https://developers.google.com/calendar/api/auth
- name: Google Meet REST API
  description: Create and manage video conferencing meetings, spaces, recordings, and transcripts.
  image: https://www.gstatic.com/images/branding/product/2x/meet_2020q4_48dp.png
  humanUrl: https://developers.google.com/meet
  baseUrl: https://meet.googleapis.com
  tags:
  - Conferencing
  - Meetings
  - Video
  properties:
  - type: Documentation
    url: https://developers.google.com/meet/api/guides/overview
  - type: Reference
    url: https://developers.google.com/workspace/meet/api/reference/rest/v2
  - type: OpenAPI
    url: https://meet.googleapis.com/$discovery/rest?version=v2
- name: Google Docs API
  description: Create and edit documents programmatically.
  image: https://www.gstatic.com/images/branding/product/2x/docs_2020q4_48dp.png
  humanUrl: https://developers.google.com/docs/api
  baseUrl: https://docs.googleapis.com
  tags:
  - Collaboration
  - Documents
  - Word Processing
  properties:
  - type: Documentation
    url: https://developers.google.com/docs/api/how-tos/overview
  - type: OpenAPI
    url: https://docs.googleapis.com/$discovery/rest?version=v1
  - type: Quick Start
    url: https://developers.google.com/docs/api/quickstart/python
  - type: Reference
    url: https://developers.google.com/workspace/docs/api/reference/rest
- name: Google Sheets API
  description: Read and write data in Google Sheets.
  image: https://www.gstatic.com/images/branding/product/2x/sheets_2020q4_48dp.png
  humanUrl: https://developers.google.com/sheets/api
  baseUrl: https://sheets.googleapis.com
  tags:
  - Analytics
  - Data
  - Spreadsheets
  properties:
  - type: Documentation
    url: https://developers.google.com/sheets/api/guides/concepts
  - type: OpenAPI
    url: https://sheets.googleapis.com/$discovery/rest?version=v4
  - type: Samples
    url: https://developers.google.com/sheets/api/samples
  - type: Quick Start
    url: https://developers.google.com/sheets/api/quickstart/python
  - type: Reference
    url: https://developers.google.com/workspace/sheets/api/reference/rest
- name: Google Slides API
  description: Create and modify presentations.
  image: https://www.gstatic.com/images/branding/product/2x/slides_2020q4_48dp.png
  humanUrl: https://developers.google.com/slides/api
  baseUrl: https://slides.googleapis.com
  tags:
  - Presentations
  - Slides
  properties:
  - type: Documentation
    url: https://developers.google.com/slides/api/guides/concepts
  - type: OpenAPI
    url: https://slides.googleapis.com/$discovery/rest?version=v1
  - type: Reference
    url: https://developers.google.com/workspace/slides/api/reference/rest
  - type: Quick Start
    url: https://developers.google.com/slides/api/quickstart/python
- name: Admin SDK Directory API
  description: Manage users, groups, organizational units, and devices in a Google Workspace domain.
  humanUrl: https://developers.google.com/admin-sdk/directory
  baseUrl: https://admin.googleapis.com
  tags:
  - Admin
  - Groups
  - Management
  - Users
  properties:
  - type: Documentation
    url: https://developers.google.com/admin-sdk/directory/reference/rest
  - type: OpenAPI
    url: https://admin.googleapis.com/$discovery/rest?version=directory_v1
  - type: OpenAPI
    url: openapi/admin-sdk-directory-api.yml
  - type: JSONSchema
    url: json-schema/google-workspace-user-schema.json
  - type: JSON-LD
    url: json-ld/google-workspace-context.jsonld
  - type: Reference
    url: https://developers.google.com/workspace/admin/directory/reference/rest
  - type: Quick Start
    url: https://developers.google.com/admin-sdk/directory/v1/quickstart/python
  - type: Overview
    url: https://developers.google.com/workspace/admin/directory/v1/guides
- name: Google Chat API
  description: Build bots and integrations for Google Chat.
  image: https://www.gstatic.com/images/branding/product/2x/chat_2020q4_48dp.png
  humanUrl: https://developers.google.com/chat
  baseUrl: https://chat.googleapis.com
  tags:
  - Chat
  - Collaboration
  - Messaging
  properties:
  - type: Documentation
    url: https://developers.google.com/chat/api/guides/overview
  - type: Reference
    url: https://developers.google.com/chat/api/reference/rest
  - type: OpenAPI
    url: https://chat.googleapis.com/$discovery/rest?version=v1
- name: Admin SDK Reports API
  description: View audit and usage reports for a Google Workspace domain including user activity and admin actions.
  humanUrl: https://developers.google.com/admin-sdk/reports
  baseUrl: https://admin.googleapis.com
  tags:
  - Admin
  - Audit
  - Reports
  - Usage
  properties:
  - type: Documentation
    url: https://developers.google.com/workspace/admin/reports/v1/get-start/overview
  - type: Reference
    url: https://developers.google.com/workspace/admin/reports/reference/rest
  - type: OpenAPI
    url: https://admin.googleapis.com/$discovery/rest?version=reports_v1
  - type: Authentication
    url: https://developers.google.com/admin-sdk/reports/auth
- name: Google Forms API
  description: Create and modify forms and quizzes, retrieve form responses and quiz grades.
  humanUrl: https://developers.google.com/workspace/forms/api
  baseUrl: https://forms.googleapis.com
  tags:
  - Forms
  - Quizzes
  - Surveys
  properties:
  - type: Documentation
    url: https://developers.google.com/workspace/forms/api/guides
  - type: Reference
    url: https://developers.google.com/workspace/forms/api/reference/rest
  - type: Quick Start
    url: https://developers.google.com/workspace/forms/api/quickstart/python
- name: Google Tasks API
  description: Search, read, and update Google Tasks content and metadata.
  humanUrl: https://developers.google.com/tasks
  baseUrl: https://tasks.googleapis.com
  tags:
  - Productivity
  - Tasks
  - To-Do
  properties:
  - type: Documentation
    url: https://developers.google.com/workspace/tasks/overview
  - type: Reference
    url: https://developers.google.com/workspace/tasks/reference/rest
  - type: OpenAPI
    url: https://www.googleapis.com/discovery/v1/apis/tasks/v1/rest
  - type: Quick Start
    url: https://developers.google.com/tasks/quickstart/js
- name: Google Keep API
  description: Manage Google Keep notes including creating, listing, and deleting notes and managing permissions.
  humanUrl: https://developers.google.com/workspace/keep
  baseUrl: https://keep.googleapis.com
  tags:
  - Notes
  - Productivity
  properties:
  - type: Documentation
    url: https://developers.google.com/workspace/keep/api/guides
  - type: Reference
    url: https://developers.google.com/workspace/keep/api/reference/rest
  - type: OpenAPI
    url: https://keep.googleapis.com/$discovery/rest?version=v1
- name: Google Vault API
  description: Manage eDiscovery for your organization including matters, holds, and exports across Google Workspace services.
  humanUrl: https://developers.google.com/workspace/vault
  baseUrl: https://vault.googleapis.com
  tags:
  - Compliance
  - Ediscovery
  - Legal
  properties:
  - type: Documentation
    url: https://developers.google.com/workspace/vault/guides
  - type: Reference
    url: https://developers.google.com/workspace/vault/reference/rest
  - type: OpenAPI
    url: https://vault.googleapis.com/$discovery/rest?version=v1
- name: Google Classroom API
  description: Manage classes, rosters, invitations, and coursework in Google Classroom.
  humanUrl: https://developers.google.com/workspace/classroom
  baseUrl: https://classroom.googleapis.com
  tags:
  - Classroom
  - Education
  - Learning
  properties:
  - type: Documentation
    url: https://developers.google.com/workspace/classroom/guides/get-started
  - type: Reference
    url: https://developers.google.com/workspace/classroom/reference/rest
  - type: OpenAPI
    url: https://classroom.googleapis.com/$discovery/rest?version=v1
- name: People API
  description: Read and manage the authenticated user contacts and profiles, and search the directory.
  humanUrl: https://developers.google.com/people
  baseUrl: https://people.googleapis.com
  tags:
  - Contacts
  - Directory
  - People
  properties:
  - type: Documentation
    url: https://developers.google.com/people
  - type: Reference
    url: https://developers.google.com/people/api/rest
- name: Google Cloud Search API
  description: Index non-Google Workspace data and search across all organizational data sources.
  humanUrl: https://developers.google.com/workspace/cloud-search
  baseUrl: https://cloudsearch.googleapis.com
  tags:
  - Enterprise Search
  - Indexing
  - Search
  properties:
  - type: Documentation
    url: https://developers.google.com/workspace/cloud-search/docs/guides/project-setup
  - type: Reference
    url: https://developers.google.com/workspace/cloud-search/docs/reference/rest
  - type: OpenAPI
    url: https://cloudsearch.googleapis.com/$discovery/rest?version=v1
- name: Drive Activity API
  description: Retrieve information about changes made to objects within a user Google Drive.
  humanUrl: https://developers.google.com/drive/activity/v2
  baseUrl: https://driveactivity.googleapis.com
  tags:
  - Activity
  - Audit
  - Drive
  properties:
  - type: Documentation
    url: https://developers.google.com/drive/activity/v2
  - type: Reference
    url: https://developers.google.com/workspace/drive/activity/v2/reference/rest
  - type: OpenAPI
    url: https://driveactivity.googleapis.com/$discovery/rest?version=v2
- name: Drive Labels API
  description: Create and manage labels to organize and classify files in Google Drive.
  humanUrl: https://developers.google.com/workspace/drive/labels/guides/overview
  baseUrl: https://drivelabels.googleapis.com
  tags:
  - Drive
  - Labels
  - Metadata
  properties:
  - type: Documentation
    url: https://developers.google.com/workspace/drive/labels/guides/overview
  - type: Reference
    url: https://developers.google.com/workspace/drive/labels/reference/rest/v2
  - type: OpenAPI
    url: https://drivelabels.googleapis.com/$discovery/rest?version=v2
- name: Alert Center API
  description: Manage alerts on issues affecting your Google Workspace domain including security and compliance warnings.
  humanUrl: https://developers.google.com/workspace/admin/alertcenter/guides
  baseUrl: https://alertcenter.googleapis.com
  tags:
  - Admin
  - Alerts
  - Security
  properties:
  - type: Documentation
    url: https://developers.google.com/workspace/admin/alertcenter/guides
  - type: Reference
    url: https://developers.google.com/workspace/admin/alertcenter/reference/rest
  - type: OpenAPI
    url: https://alertcenter.googleapis.com/$discovery/rest?version=v1beta1
  - type: Authentication
    url: https://developers.google.com/workspace/admin/alertcenter/guides/auth
- name: Groups Settings API
  description: Update and retrieve settings for existing Google Groups including permissions and access controls.
  humanUrl: https://developers.google.com/admin-sdk/groups-settings/concepts
  baseUrl: https://www.googleapis.com/groups/v1
  tags:
  - Admin
  - Groups
  - Settings
  properties:
  - type: Documentation
    url: https://developers.google.com/admin-sdk/groups-settings/concepts
  - type: Reference
    url: https://developers.google.com/admin-sdk/groups-settings/v1/reference
- name: Groups Migration API
  description: Migrate shared emails from public folders and distribution lists to Google Groups discussion archives.
  humanUrl: https://developers.google.com/workspace/admin/groups-migration/v1/guides/overview
  baseUrl: https://groupsmigration.googleapis.com
  tags:
  - Admin
  - Groups
  - Migration
  properties:
  - type: Documentation
    url: https://developers.google.com/workspace/admin/groups-migration/v1/guides/overview
  - type: Authentication
    url: https://developers.google.com/workspace/admin/groups-migration/v1/guides/authorizing
- name: Admin SDK Data Transfer API
  description: Transfer ownership of user data from one user to another within a domain.
  humanUrl: https://developers.google.com/workspace/admin/data-transfer
  baseUrl: https://admin.googleapis.com
  tags:
  - Admin
  - Data Transfer
  - Migration
  properties:
  - type: Documentation
    url: https://developers.google.com/workspace/admin/data-transfer
  - type: Reference
    url: https://developers.google.com/workspace/admin/data-transfer/reference/rest
  - type: OpenAPI
    url: https://admin.googleapis.com/$discovery/rest?version=datatransfer_v1
- name: Enterprise License Manager API
  description: Manage Google Workspace and related product licenses for all users of a customer.
  humanUrl: https://developers.google.com/admin-sdk/licensing
  baseUrl: https://licensing.googleapis.com
  tags:
  - Admin
  - Licensing
  - Management
  properties:
  - type: Documentation
    url: https://developers.google.com/admin-sdk/licensing/v1/how-tos/using
  - type: Reference
    url: https://developers.google.com/workspace/admin/licensing/reference/rest
  - type: Authentication
    url: https://developers.google.com/admin-sdk/licensing/v1/how-tos/authorizing
- name: Google Workspace Reseller API
  description: Perform common reseller functions at scale including placing orders and managing customer subscriptions.
  humanUrl: https://developers.google.com/workspace/admin/reseller/v1/how-tos/concepts
  baseUrl: https://reseller.googleapis.com
  tags:
  - Admin
  - Reseller
  - Subscriptions
  properties:
  - type: Documentation
    url: https://developers.google.com/workspace/admin/reseller/v1/how-tos/concepts
  - type: Reference
    url: https://developers.google.com/workspace/admin/reseller/reference/rest
  - type: OpenAPI
    url: https://reseller.googleapis.com/$discovery/rest?version=v1
  - type: Authentication
    url: https://developers.google.com/workspace/admin/reseller/v1/how-tos/authorize
- name: Gmail Postmaster Tools API
  description: Gather statistics on bulk emails sent to Gmail users including spam reports and delivery errors.
  humanUrl: https://developers.google.com/workspace/gmail/postmaster
  baseUrl: https://gmailpostmastertools.googleapis.com
  tags:
  - Deliverability
  - Email
  - Postmaster
  properties:
  - type: Documentation
    url: https://developers.google.com/workspace/gmail/postmaster
  - type: Reference
    url: https://developers.google.com/workspace/gmail/postmaster/reference/rest
  - type: OpenAPI
    url: https://gmailpostmastertools.googleapis.com/$discovery/rest?version=v1
- name: Google Workspace Marketplace API
  description: Manage customer and user license status for Google Workspace Marketplace applications.
  humanUrl: https://developers.google.com/workspace/marketplace/overview
  baseUrl: https://appsmarket.googleapis.com
  tags:
  - Apps
  - Licensing
  - Marketplace
  properties:
  - type: Documentation
    url: https://developers.google.com/workspace/marketplace/overview
  - type: Reference
    url: https://developers.google.com/workspace/marketplace/reference/rest
  - type: Authentication
    url: https://developers.google.com/workspace/marketplace/authorizing
name: Google Workspace
tags:
- Calendar
- Collaboration
- Email
- Productivity
- Storage
- Video Conferencing
type: Contract
image: https://workspace.google.com/static/img/logo.svg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: A collection of productivity and collaboration tools from Google including Gmail, Drive, Calendar, Meet, and more.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

