---
aid: cisco-webex-meetings
name: Cisco Webex Meetings
url: https://raw.githubusercontent.com/api-evangelist/cisco-webex-meetings/refs/heads/main/apis.yml
created: '2024-01-01'
modified: '2026-04-23'
type: Index
access: 3rd-Party
position: Consumer
specificationVersion: '0.19'
tags:
  - Collaboration
  - Communications
  - Enterprise
  - Meetings
  - Video Conferencing
description: Cisco Webex Meetings is the meetings-focused subset of the Webex collaboration platform, providing scheduling, hosting, recording, transcription, and meeting administration capabilities through the Webex REST API. Authentication uses OAuth 2.0 access tokens, personal access tokens, or service apps and all endpoints respond with JSON. The legacy XML API remains available for deep integrations and enterprise scenarios that pre-date the REST surface.
apis:
  - aid: cisco-webex-meetings:meetings-api
    name: Webex Meetings API
    tags:
      - Conferencing
      - Meetings
      - Scheduling
      - Video
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://webexapis.com/v1
    humanURL: https://developer.webex.com/docs/api/v1/meetings
    properties:
      - url: https://developer.webex.com/docs/api/v1/meetings
        type: Documentation
      - url: https://developer.webex.com/docs/getting-started#accounts-and-authentication
        type: Authentication
    description: The Webex Meetings API enables scheduling, updating, deleting, and listing of Webex meetings. Endpoints support recurring meetings, meeting templates, and host delegation. Authentication uses OAuth 2.0 bearer tokens or personal access tokens.
  - aid: cisco-webex-meetings:meeting-invitees-api
    name: Webex Meeting Invitees API
    tags:
      - Attendees
      - Invitees
      - Meetings
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://webexapis.com/v1
    humanURL: https://developer.webex.com/docs/api/v1/meeting-invitees
    properties:
      - url: https://developer.webex.com/docs/api/v1/meeting-invitees
        type: Documentation
    description: Manage invitee lists for scheduled Webex meetings. Endpoints support adding, updating, and removing meeting invitees and bulk-inviting attendees by email.
  - aid: cisco-webex-meetings:meeting-participants-api
    name: Webex Meeting Participants API
    tags:
      - Attendees
      - Participants
      - Real-Time
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://webexapis.com/v1
    humanURL: https://developer.webex.com/docs/api/v1/meeting-participants
    properties:
      - url: https://developer.webex.com/docs/api/v1/meeting-participants
        type: Documentation
    description: List and update participants in active or completed Webex meetings. Supports admin-mute, lobby admit, and participant removal operations during in-progress meetings.
  - aid: cisco-webex-meetings:meeting-preferences-api
    name: Webex Meeting Preferences API
    tags:
      - Personal Room
      - Preferences
      - Settings
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://webexapis.com/v1
    humanURL: https://developer.webex.com/docs/api/v1/meeting-preferences
    properties:
      - url: https://developer.webex.com/docs/api/v1/meeting-preferences
        type: Documentation
    description: Manage host meeting preferences including personal room URLs, audio defaults, scheduling templates, and site preferences.
  - aid: cisco-webex-meetings:recordings-api
    name: Webex Recordings API
    tags:
      - Compliance
      - Media
      - Recordings
      - Storage
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://webexapis.com/v1
    humanURL: https://developer.webex.com/docs/api/v1/recordings
    properties:
      - url: https://developer.webex.com/docs/api/v1/recordings
        type: Documentation
    description: List and manage meeting recordings. Provides access to recording details, download links, and metadata, with separate endpoints for admin and compliance officer access.
  - aid: cisco-webex-meetings:meeting-transcripts-api
    name: Webex Meeting Transcripts API
    tags:
      - Accessibility
      - AI
      - Captions
      - Transcripts
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://webexapis.com/v1
    humanURL: https://developer.webex.com/docs/api/v1/meeting-transcripts
    properties:
      - url: https://developer.webex.com/docs/api/v1/meeting-transcripts
        type: Documentation
    description: Retrieve and manage meeting transcripts including download endpoints for VTT and TXT transcript formats. Supports compliance officer access for governance workflows.
  - aid: cisco-webex-meetings:meeting-qa-api
    name: Webex Meeting Q and A API
    tags:
      - Engagement
      - Q and A
      - Webinars
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://webexapis.com/v1
    humanURL: https://developer.webex.com/docs/api/v1/meeting-qanda
    properties:
      - url: https://developer.webex.com/docs/api/v1/meeting-qanda
        type: Documentation
    description: Retrieve questions and answers from Webex meetings and webinars for engagement reporting and post-event follow-up workflows.
  - aid: cisco-webex-meetings:meeting-polls-api
    name: Webex Meeting Polls API
    tags:
      - Engagement
      - Polls
      - Surveys
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://webexapis.com/v1
    humanURL: https://developer.webex.com/docs/api/v1/meeting-polls
    properties:
      - url: https://developer.webex.com/docs/api/v1/meeting-polls
        type: Documentation
    description: Retrieve polls and poll responses from Webex meetings and webinars for engagement analytics and post-event reporting.
  - aid: cisco-webex-meetings:meeting-chats-api
    name: Webex Meeting Chats API
    tags:
      - Chat
      - Compliance
      - Meetings
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://webexapis.com/v1
    humanURL: https://developer.webex.com/docs/api/v1/meeting-chats
    properties:
      - url: https://developer.webex.com/docs/api/v1/meeting-chats
        type: Documentation
    description: Retrieve chat transcripts from completed Webex meetings for compliance and post-meeting reporting.
  - aid: cisco-webex-meetings:webex-xml-api
    name: Webex XML API
    tags:
      - Enterprise
      - Legacy
      - SOAP
      - XML
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://developer.cisco.com/docs/webex-xml-api-reference-guide/
    properties:
      - url: https://developer.cisco.com/docs/webex-xml-api-reference-guide/
        type: Documentation
    description: The Webex XML API is the legacy SOAP-style interface for deep integration with Webex Meetings. It supports site administration, user provisioning, and meeting management for scenarios that pre-date the REST API.
common:
  - type: Portal
    url: https://developer.webex.com/
  - type: Documentation
    url: https://developer.webex.com/docs/meetings
  - type: Getting Started
    url: https://developer.webex.com/docs/getting-started
  - type: Authentication
    url: https://developer.webex.com/docs/integrations
  - type: SDKs
    url: https://developer.webex.com/docs/sdks
  - type: Webhooks
    url: https://developer.webex.com/docs/webhooks
  - type: Rate Limits
    url: https://developer.webex.com/docs/api-rate-limits
  - type: Change Log
    url: https://developer.webex.com/docs/api/changelog
  - type: Status
    url: https://status.webex.com/
  - type: Support
    url: https://developer.webex.com/support
  - type: Blog
    url: https://developer.webex.com/blog
  - type: Community
    url: https://community.cisco.com/t5/webex-developers/bd-p/4416j-disc-dev-webex
  - type: Terms of Service
    url: https://www.cisco.com/c/en/us/about/legal/cloud-and-software/end-user-license-agreement.html
  - type: Privacy Policy
    url: https://www.cisco.com/c/en/us/about/legal/privacy-full.html
  - type: JSON-LD
    url: json-ld/cisco-webex-meetings-context.jsonld
  - type: Spectral
    url: rules/cisco-webex-meetings-rules.yml
  - type: Naftiko Capabilities
    url: capabilities/cisco-webex-meetings-capabilities.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
