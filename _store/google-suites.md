---
aid: google-suites
url: https://raw.githubusercontent.com/api-evangelist/google-suites/refs/heads/main/apis.yml
apis:
- name: Gmail API
  description: Access Gmail mailboxes and send mail.
  image: https://www.gstatic.com/images/branding/product/1x/gmail_48dp.png
  humanURL: https://developers.google.com/gmail/api
  baseURL: https://gmail.googleapis.com
  tags:
  - Email
  - Messaging
  properties:
  - type: OpenAPI
    url: https://gmail.googleapis.com/$discovery/rest?version=v1
  - type: Documentation
    url: https://developers.google.com/gmail/api/guides
  - type: Authentication
    url: https://developers.google.com/gmail/api/auth/about-auth
- name: Google Calendar API
  description: Manage calendars and events.
  image: https://www.gstatic.com/images/branding/product/1x/calendar_48dp.png
  humanURL: https://developers.google.com/calendar
  baseURL: https://www.googleapis.com/calendar/v3
  tags:
  - Calendar
  - Events
  - Scheduling
  properties:
  - type: OpenAPI
    url: https://www.googleapis.com/discovery/v1/apis/calendar/v3/rest
  - type: Documentation
    url: https://developers.google.com/calendar/api/guides/overview
  - type: Quickstart
    url: https://developers.google.com/calendar/api/quickstart
- name: Google Drive API
  description: Store and share files in the cloud.
  image: https://www.gstatic.com/images/branding/product/1x/drive_48dp.png
  humanURL: https://developers.google.com/drive
  baseURL: https://www.googleapis.com/drive/v3
  tags:
  - Cloud
  - Files
  - Storage
  properties:
  - type: OpenAPI
    url: https://www.googleapis.com/discovery/v1/apis/drive/v3/rest
  - type: Documentation
    url: https://developers.google.com/drive/api/guides/about-sdk
  - type: Pricing
    url: https://workspace.google.com/pricing
- name: Google Docs API
  description: Create and edit documents programmatically.
  image: https://www.gstatic.com/images/branding/product/1x/docs_48dp.png
  humanURL: https://developers.google.com/docs/api
  baseURL: https://docs.googleapis.com
  tags:
  - Documents
  - Word Processing
  properties:
  - type: OpenAPI
    url: https://docs.googleapis.com/$discovery/rest?version=v1
  - type: Documentation
    url: https://developers.google.com/docs/api/how-tos/overview
  - type: Samples
    url: https://developers.google.com/docs/api/samples
- name: Google Sheets API
  description: Read and write spreadsheet data.
  image: https://www.gstatic.com/images/branding/product/1x/sheets_48dp.png
  humanURL: https://developers.google.com/sheets/api
  baseURL: https://sheets.googleapis.com
  tags:
  - Data
  - Spreadsheets
  properties:
  - type: OpenAPI
    url: https://sheets.googleapis.com/$discovery/rest?version=v4
  - type: Documentation
    url: https://developers.google.com/sheets/api/guides/concepts
  - type: Quickstart
    url: https://developers.google.com/sheets/api/quickstart
- name: Google Slides API
  description: Create and edit presentations.
  image: https://www.gstatic.com/images/branding/product/1x/slides_48dp.png
  humanURL: https://developers.google.com/slides
  baseURL: https://slides.googleapis.com
  tags:
  - Presentations
  - Slides
  properties:
  - type: OpenAPI
    url: https://slides.googleapis.com/$discovery/rest?version=v1
  - type: Documentation
    url: https://developers.google.com/slides/how-tos/overview
- name: Google Meet API
  description: Manage video conferencing.
  image: https://www.gstatic.com/images/branding/product/1x/meet_48dp.png
  humanURL: https://developers.google.com/meet
  baseURL: https://meet.googleapis.com
  tags:
  - Meetings
  - Video Conferencing
  properties:
  - type: Documentation
    url: https://developers.google.com/meet/api
- name: Admin SDK Directory API
  description: Manage users, groups, and organizational units.
  humanURL: https://developers.google.com/admin-sdk/directory
  baseURL: https://admin.googleapis.com
  tags:
  - Administration
  - Groups
  - Users
  properties:
  - type: OpenAPI
    url: https://admin.googleapis.com/$discovery/rest?version=directory_v1
  - type: Documentation
    url: https://developers.google.com/admin-sdk/directory/reference/rest
name: Google Workspace APIs
tags:
- Cloud Storage
- Collaboration
- Email
- Office Suite
- Productivity
type: Contract
image: https://workspace.google.com/static/img/logo-workspace.svg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Collection of APIs for Google Workspace (formerly G Suite) services including Gmail, Calendar, Drive, Docs, Sheets, and more.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

