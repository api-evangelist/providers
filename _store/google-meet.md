---
name: Google Meet
description: The Google Meet API provides programmatic access to Google Meet video conferencing functionality. It enables applications to create and manage meeting spaces, retrieve conference records including participant details, access recordings and transcripts, and end active conferences. The API supports building integrations that automate meeting workflows and extract meeting data.
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/google-meet/refs/heads/main/apis.yml
created: '2026-03-13'
modified: '2026-04-28'
specificationVersion: '0.18'
tags:
  - Google
  - Google Workspace
  - Meetings
  - Recordings
  - Transcripts
  - Video Conferencing
apis:
  - name: Google Meet API
    description: The Google Meet REST API enables creating and managing meeting spaces, retrieving conference records with participant and session data, accessing meeting recordings and transcripts, and controlling active conferences.
    humanURL: https://developers.google.com/workspace/meet/api/guides/overview
    baseURL: https://meet.googleapis.com
    properties:
      - type: OpenAPI
        url: openapi/openapi.yml
      - type: JSONSchema
        url: json-schema/json-schema.yml
      - type: JSONLD
        url: json-ld/json-ld.jsonld
    tags:
      - Meetings
      - Recordings
      - Transcripts
      - Video Conferencing
common:
  - type: GettingStarted
    url: https://developers.google.com/workspace/meet/api/guides/overview
  - type: Pricing
    url: https://cloud.google.com/meet/pricing
  - type: JSONLD
    url: json-ld/json-ld.jsonld
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
