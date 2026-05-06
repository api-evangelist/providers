---
aid: microsoft-stream
name: Microsoft Stream
description: Microsoft Stream is an intelligent video service for enterprise video management. Videos are stored in OneDrive and SharePoint with video-specific capabilities accessible through Microsoft Graph and SharePoint APIs.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Microsoft
  - Microsoft 365
  - Streaming
  - Video
url: https://raw.githubusercontent.com/api-evangelist/microsoft-stream/refs/heads/main/apis.yml
created: '2024-01-01'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: microsoft-stream:graph-video-api
    name: Microsoft Graph Stream Video API
    tags:
      - Microsoft Graph
      - SharePoint
      - Streaming
      - Video
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://graph.microsoft.com/v1.0/
    humanURL: https://learn.microsoft.com/en-us/stream/
    properties:
      - url: https://learn.microsoft.com/en-us/stream/
        type: Documentation
      - url: https://learn.microsoft.com/en-us/graph/auth/
        type: Authentication
    description: Microsoft Stream (on SharePoint) provides video management capabilities through Microsoft Graph and SharePoint APIs. Videos are stored in OneDrive and SharePoint, enabling developers to upload, manage, share, and embed enterprise videos using existing Graph drive and file APIs with video-specific metadata and playback support.
common:
  - type: Portal
    url: https://www.microsoft365.com/
  - type: Website
    url: https://www.microsoft.com/en-us/microsoft-365/microsoft-stream
  - type: Documentation
    url: https://learn.microsoft.com/en-us/stream/
  - type: Authentication
    url: https://learn.microsoft.com/en-us/graph/auth/
  - type: Terms of Service
    url: https://www.microsoft.com/en-us/legal/terms-of-use
  - type: Privacy Policy
    url: https://privacy.microsoft.com/en-us/privacystatement
  - type: Support
    url: https://support.microsoft.com/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
