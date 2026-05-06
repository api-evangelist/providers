---
name: Google Keep
description: The Google Keep API provides programmatic access to Google Keep notes for enterprise administrators. It enables creating, listing, retrieving, and deleting notes, downloading note attachments, and managing note permissions. The API is designed for enterprise use cases where administrators need to manage Keep notes across their organization.
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/google-keep/refs/heads/main/apis.yml
created: '2026-03-13'
modified: '2026-04-28'
specificationVersion: '0.18'
tags:
  - Google
  - Google Workspace
  - Notes
  - Organization
  - Productivity
apis:
  - name: Google Keep API
    description: The Google Keep API enables enterprise administrators to manage Google Keep notes, including creating, listing, deleting, downloading note attachments, and managing permissions on notes.
    humanURL: https://developers.google.com/workspace/keep/api/guides
    baseURL: https://keep.googleapis.com
    properties:
      - type: OpenAPI
        url: openapi/openapi.yml
      - type: JSONSchema
        url: json-schema/json-schema.yml
      - type: JSONLD
        url: json-ld/json-ld.jsonld
      - type: Spectral Rules
        url: rules/google-keep-spectral-rules.yml
    tags:
      - Attachments
      - Notes
      - Permissions
common:
  - type: GettingStarted
    url: https://developers.google.com/workspace/keep/api/guides
  - type: Pricing
    url: https://workspace.google.com/pricing
  - type: JSONLD
    url: json-ld/json-ld.jsonld
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
