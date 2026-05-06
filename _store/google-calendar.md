---
aid: google-calendar
name: Google Calendar
description: The Google Calendar API provides RESTful access to Google Calendar data, enabling applications to create, view, and manage calendar events, access control lists, and user settings. It supports creating and managing multiple calendars, querying free/busy information, setting up push notifications for changes, and integrating calendar functionality into third-party applications.
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/google-calendar/refs/heads/main/apis.yml
created: '2026-03-13'
modified: '2026-04-28'
specificationVersion: '0.19'
type: Index
tags:
  - Availability
  - Calendar
  - Events
  - Google
  - Google Workspace
  - Scheduling
apis:
  - name: Google Calendar API
    description: The Google Calendar API lets you manage calendars, events, access control, settings, and free/busy information. It supports creating events, subscribing to calendars, querying availability, and receiving push notifications for changes.
    humanURL: https://developers.google.com/workspace/calendar/api/guides/overview
    baseURL: https://www.googleapis.com/calendar/v3
    properties:
      - type: Documentation
        url: https://developers.google.com/workspace/calendar/api/guides/overview
      - type: OpenAPI
        url: openapi/openapi.yml
      - type: Authentication
        url: https://developers.google.com/workspace/calendar/api/auth
      - type: Getting Started
        url: https://developers.google.com/workspace/calendar/api/quickstart/python
      - type: JSONSchema
        url: json-schema/json-schema.yml
      - type: JSONLD
        url: json-ld/json-ld.jsonld
    tags:
      - Availability
      - Calendar
      - Events
      - Scheduling
common:
  - type: Portal
    url: https://developers.google.com/workspace/calendar
  - type: Getting Started
    url: https://developers.google.com/workspace/calendar/api/guides/overview
  - type: Documentation
    url: https://developers.google.com/workspace/calendar/api/reference/rest
  - type: Authentication
    url: https://developers.google.com/identity/protocols/oauth2
  - type: Pricing
    url: https://developers.google.com/workspace/calendar/api/guides/quota
  - type: Terms of Service
    url: https://developers.google.com/terms
  - type: Privacy Policy
    url: https://policies.google.com/privacy
  - type: Status
    url: https://www.google.com/appsstatus/dashboard/
  - type: Support
    url: https://developers.google.com/workspace/calendar/api/support
  - type: Blog
    url: https://workspaceupdates.googleblog.com/
  - type: JSONLD
    url: json-ld/json-ld.jsonld
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
