---
aid: google-suite
url: https://raw.githubusercontent.com/api-evangelist/google-suite/refs/heads/main/apis.yml
apis:
- name: Gmail API
  description: The Gmail API lets you view and manage Gmail mailbox data like threads, messages, and labels.
  image: https://www.gstatic.com/images/branding/product/2x/gmail_64dp.png
  humanURL: https://developers.google.com/gmail/api
  baseURL: https://gmail.googleapis.com
  tags:
  - Email
  - Messaging
  - Productivity
  properties:
  - type: Documentation
    url: https://developers.google.com/gmail/api/guides
  - type: OpenAPI
    url: https://gmail.googleapis.com/$discovery/rest?version=v1
  - type: Authentication
    url: https://developers.google.com/gmail/api/auth/about-auth
  - type: Pricing
    url: https://developers.google.com/gmail/api/reference/quota
  contact:
  - type: Support
    url: https://developers.google.com/gmail/api/support
- name: Google Calendar API
  description: The Google Calendar API lets you integrate your app with Google Calendar, creating new ways for users to engage with their calendars.
  image: https://www.gstatic.com/images/branding/product/2x/calendar_64dp.png
  humanURL: https://developers.google.com/calendar
  baseURL: https://www.googleapis.com/calendar/v3
  tags:
  - Calendar
  - Events
  - Productivity
  - Scheduling
  properties:
  - type: Documentation
    url: https://developers.google.com/calendar/api/guides/overview
  - type: OpenAPI
    url: https://www.googleapis.com/discovery/v1/apis/calendar/v3/rest
  - type: Authentication
    url: https://developers.google.com/calendar/api/guides/auth
  - type: Quickstart
    url: https://developers.google.com/calendar/api/quickstart/python
- name: Google Drive API
  description: The Google Drive API allows you to create apps that leverage Google Drive cloud storage.
  image: https://www.gstatic.com/images/branding/product/2x/drive_64dp.png
  humanURL: https://developers.google.com/drive
  baseURL: https://www.googleapis.com/drive/v3
  tags:
  - Cloud
  - Collaboration
  - Files
  - Storage
  properties:
  - type: Documentation
    url: https://developers.google.com/drive/api/guides/about-sdk
  - type: OpenAPI
    url: https://www.googleapis.com/discovery/v1/apis/drive/v3/rest
  - type: Authentication
    url: https://developers.google.com/drive/api/guides/about-auth
  - type: Pricing
    url: https://developers.google.com/drive/api/guides/limits
- name: Google Docs API
  description: The Google Docs API lets you create and modify documents programmatically.
  image: https://www.gstatic.com/images/branding/product/2x/docs_64dp.png
  humanURL: https://developers.google.com/docs/api
  baseURL: https://docs.googleapis.com/v1
  tags:
  - Collaboration
  - Documents
  - Productivity
  - Word-Processing
  properties:
  - type: Documentation
    url: https://developers.google.com/docs/api/how-tos/overview
  - type: OpenAPI
    url: https://docs.googleapis.com/$discovery/rest?version=v1
  - type: Quickstart
    url: https://developers.google.com/docs/api/quickstart/python
- name: Google Sheets API
  description: The Google Sheets API lets you read, write, and format Google Sheets data with your preferred programming language.
  image: https://www.gstatic.com/images/branding/product/2x/sheets_64dp.png
  humanURL: https://developers.google.com/sheets/api
  baseURL: https://sheets.googleapis.com/v4
  tags:
  - Collaboration
  - Data
  - Productivity
  - Spreadsheets
  properties:
  - type: Documentation
    url: https://developers.google.com/sheets/api/guides/concepts
  - type: OpenAPI
    url: https://sheets.googleapis.com/$discovery/rest?version=v4
  - type: Authentication
    url: https://developers.google.com/sheets/api/guides/authorizing
  - type: Samples
    url: https://developers.google.com/sheets/api/samples
- name: Google Slides API
  description: The Google Slides API lets you create and modify Google Slides presentations programmatically.
  image: https://www.gstatic.com/images/branding/product/2x/slides_64dp.png
  humanURL: https://developers.google.com/slides
  baseURL: https://slides.googleapis.com/v1
  tags:
  - Collaboration
  - Presentations
  - Productivity
  properties:
  - type: Documentation
    url: https://developers.google.com/slides/how-tos/overview
  - type: OpenAPI
    url: https://slides.googleapis.com/$discovery/rest?version=v1
  - type: Samples
    url: https://developers.google.com/slides/samples
- name: Google Meet API
  description: The Google Meet API allows developers to build applications that integrate with Google Meet.
  image: https://www.gstatic.com/images/branding/product/2x/meet_64dp.png
  humanURL: https://developers.google.com/meet
  baseURL: https://meet.googleapis.com/v2
  tags:
  - Collaboration
  - Communication
  - Meetings
  - Video-Conferencing
  properties:
  - type: Documentation
    url: https://developers.google.com/meet/api/guides/overview
  - type: Reference
    url: https://developers.google.com/meet/api/reference/rest
- name: Google Chat API
  description: The Google Chat API allows you to build Chat apps that bring your services into Google Chat.
  image: https://www.gstatic.com/images/branding/product/2x/chat_64dp.png
  humanURL: https://developers.google.com/chat
  baseURL: https://chat.googleapis.com/v1
  tags:
  - Bots
  - Collaboration
  - Communication
  - Messaging
  properties:
  - type: Documentation
    url: https://developers.google.com/chat/api/guides/overview
  - type: OpenAPI
    url: https://chat.googleapis.com/$discovery/rest?version=v1
  - type: Concepts
    url: https://developers.google.com/chat/api/guides/concepts
- name: Google Admin SDK
  description: The Admin SDK lets administrators of Google Workspace domains programmatically manage users, groups, and resources.
  image: https://www.gstatic.com/images/branding/product/2x/admin_64dp.png
  humanURL: https://developers.google.com/admin-sdk
  baseURL: https://admin.googleapis.com
  tags:
  - Administration
  - Groups
  - Management
  - Users
  properties:
  - type: Documentation
    url: https://developers.google.com/admin-sdk/directory/v1/guides
  - type: Directory API
    url: https://developers.google.com/admin-sdk/directory
  - type: Reports API
    url: https://developers.google.com/admin-sdk/reports
  - type: OpenAPI
    url: https://admin.googleapis.com/$discovery/rest?version=directory_v1
- name: Google Forms API
  description: The Google Forms API provides programmatic access to create, modify, and retrieve form content and responses.
  image: https://www.gstatic.com/images/branding/product/2x/forms_64dp.png
  humanURL: https://developers.google.com/forms/api
  baseURL: https://forms.googleapis.com/v1
  tags:
  - Data-Collection
  - Forms
  - Productivity
  - Surveys
  properties:
  - type: Documentation
    url: https://developers.google.com/forms/api/guides
  - type: Reference
    url: https://developers.google.com/forms/api/reference/rest
name: Google Workspace (G Suite)
tags:
- Cloud
- Collaboration
- Enterprise
- Google
- Productivity
- Workspace
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Google Workspace (formerly G Suite) is a collection of cloud computing, productivity and collaboration tools, software and products developed and marketed by Google.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

