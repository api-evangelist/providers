---
aid: google-voice
name: Google Voice
description: Google Voice is a telecommunications service by Google that provides call forwarding, voicemail, text messaging, and voice calling for personal and Google Workspace business accounts. While Google Voice does not offer an official standalone REST API, voice services can be managed programmatically through the Google Workspace Admin SDK for provisioning users, assigning numbers, and managing locations. Google Voice integrates with Google Workspace for enterprise telephony management.
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/google-voice/refs/heads/main/apis.yml
created: '2026-03-13'
modified: '2026-04-28'
specificationVersion: '0.19'
type: Index
tags:
  - Google Voice
  - Messaging
  - Phone
  - Telecommunications
  - Voice
  - Voicemail
  - VoIP
apis:
  - name: Google Voice API
    description: Management API for Google Voice services through the Google Workspace Admin SDK, enabling user provisioning, number assignment, and location management for enterprise telephony.
    humanURL: https://voice.google.com
    baseURL: https://admin.googleapis.com
    properties:
      - type: Documentation
        url: https://developers.google.com/workspace/products/voice
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/google-voice/refs/heads/main/openapi/openapi.yml
      - type: Authentication
        url: https://developers.google.com/workspace/guides/auth-overview
      - type: Getting Started
        url: https://support.google.com/voice/answer/115061
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/google-voice/refs/heads/main/json-schema/google-voice.json
      - type: JSONLD
        url: https://raw.githubusercontent.com/api-evangelist/google-voice/refs/heads/main/json-ld/google-voice.jsonld
common:
  - type: Portal
    url: https://workspace.google.com/products/voice/
  - type: Getting Started
    url: https://support.google.com/voice/answer/115061
  - type: Documentation
    url: https://developers.google.com/workspace/products/voice
  - type: Authentication
    url: https://developers.google.com/workspace/guides/auth-overview
  - type: Pricing
    url: https://workspace.google.com/products/voice/
  - type: Terms of Service
    url: https://policies.google.com/terms
  - type: Privacy Policy
    url: https://policies.google.com/privacy
  - type: Status
    url: https://status.cloud.google.com/
  - type: Support
    url: https://support.google.com/voice
  - type: JSONLD
    url: https://raw.githubusercontent.com/api-evangelist/google-voice/refs/heads/main/json-ld/google-voice.jsonld
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
