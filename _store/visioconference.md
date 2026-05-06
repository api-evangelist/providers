---
aid: visioconference
name: Visioconference
description: Visioconference (video conferencing) is a category of communication technology enabling real-time visual and audio communication between remote participants. This repository profiles the video conferencing API ecosystem including leading providers such as Zoom, Microsoft Teams, Google Meet, Webex, Digital Samba, VideoSDK, Daily.co, and others offering REST APIs for embedding and managing video conferencing functionality. The term "visioconference" is commonly used in French-speaking contexts.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Audio
  - Chat
  - Collaboration
  - Communication
  - Conferencing
  - Live Streaming
  - Real-Time
  - Remote Work
  - Screen Sharing
  - Video
  - WebRTC
created: '2024-01-15'
modified: '2026-05-03'
url: https://raw.githubusercontent.com/api-evangelist/visioconference/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: visioconference:zoom-api
    name: Zoom API
    description: The Zoom REST API provides access to Zoom meetings, webinars, users, cloud recordings, and phone services for building Zoom integrations.
    humanURL: https://developers.zoom.us/
    tags:
      - Video Conferencing
      - Meetings
      - Webinars
    properties:
      - type: Documentation
        url: https://developers.zoom.us/docs/api/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/zoom/api/master/openapi/zoom-api.yaml
  - aid: visioconference:microsoft-teams-api
    name: Microsoft Teams API
    description: Microsoft Graph API for Teams provides access to teams, channels, meetings, calls, and messaging in Microsoft Teams.
    humanURL: https://learn.microsoft.com/en-us/graph/teams-concept-overview
    tags:
      - Video Conferencing
      - Meetings
      - Collaboration
      - Microsoft
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/graph/teams-concept-overview
  - aid: visioconference:google-meet-api
    name: Google Meet REST API
    description: Google Meet REST API allows developers to create and manage Meet spaces and retrieve recording artifacts.
    humanURL: https://developers.google.com/meet/api
    tags:
      - Video Conferencing
      - Meetings
      - Google
    properties:
      - type: Documentation
        url: https://developers.google.com/meet/api
  - aid: visioconference:cisco-webex-api
    name: Cisco Webex API
    description: Cisco Webex REST API for meetings, messaging, calling, and device management. Supports webhooks for event-driven integrations.
    humanURL: https://developer.webex.com/
    tags:
      - Video Conferencing
      - Meetings
      - Cisco
    properties:
      - type: Documentation
        url: https://developer.webex.com/docs/api/getting-started
  - aid: visioconference:daily-co-api
    name: Daily.co API
    description: Daily.co REST API for creating and managing video call rooms, recording, and participant management using WebRTC.
    humanURL: https://docs.daily.co/reference
    tags:
      - Video Conferencing
      - WebRTC
      - Rooms
    properties:
      - type: Documentation
        url: https://docs.daily.co/reference
  - aid: visioconference:digital-samba-api
    name: Digital Samba Embedded API
    description: European-hosted video conferencing REST API for creating rooms, managing access, and embedding video calls. GDPR-compliant with data stored in Europe.
    humanURL: https://digitalsamba.com/
    tags:
      - Video Conferencing
      - WebRTC
      - GDPR
      - European
    properties:
      - type: Documentation
        url: https://digitalsamba.com/video-api
common:
  - type: Website
    url: https://en.wikipedia.org/wiki/Videotelephony
  - type: JSONSchema
    url: json-schema/visioconference-meeting-schema.json
  - type: JSON-LD
    url: json-ld/visioconference-context.jsonld
  - type: Vocabulary
    url: vocabulary/visioconference-vocabulary.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
