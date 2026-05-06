---
aid: google-drive
name: Google Drive
description: The Google Drive API allows developers to integrate with Google Drive to create, read, update, and delete files and folders stored in Google Drive. The v3 REST API supports file metadata operations, content upload and download, folder hierarchies, sharing and permissions, and search across a user's Drive.
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/google-drive/refs/heads/main/apis.yml
created: '2024-01-15'
modified: '2026-05-04'
specificationVersion: '0.19'
type: Index
tags:
  - Cloud Storage
  - Collaboration
  - Document Management
  - Drive
  - Files
  - Google
  - Storage
apis:
  - name: Google Drive API v3
    description: REST API for managing files and folders in Google Drive. Supports file metadata operations, content upload and download, sharing and permissions, revisions, comments, and changes feeds.
    image: https://www.gstatic.com/images/branding/product/2x/drive_48dp.png
    humanURL: https://developers.google.com/drive/api/v3/about-sdk
    baseURL: https://www.googleapis.com/drive/v3
    tags:
      - Cloud
      - Collaboration
      - Files
      - Storage
    properties:
      - type: Documentation
        url: https://developers.google.com/drive/api/v3/reference
      - type: OpenAPI
        url: openapi/google-drive-openapi.yml
      - type: JSONSchema
        url: json-schema/google-drive-file-schema.json
      - type: Authentication
        url: https://developers.google.com/drive/api/v3/about-auth
      - type: Quickstart
        url: https://developers.google.com/drive/api/v3/quickstart/python
      - type: Pricing
        url: https://workspace.google.com/pricing
      - type: Terms of Service
        url: https://developers.google.com/terms
      - type: OAuth Scopes
        url: https://developers.google.com/drive/api/v3/about-auth#OAuth2Authorizing
    contact:
      - type: Support
        url: https://developers.google.com/drive/api/v3/support
common:
  - type: Portal
    url: https://console.cloud.google.com/
  - type: Getting Started
    url: https://developers.google.com/drive/api/v3/enable-drive-api
  - type: Authentication
    url: https://developers.google.com/identity/protocols/oauth2
  - type: Change Log
    url: https://developers.google.com/drive/api/v3/releases
  - type: Rate Limits
    url: https://developers.google.com/drive/api/v3/handle-errors#rate-limit-exceeded
  - type: Status
    url: https://www.google.com/appsstatus
  - type: JSON-LD
    url: json-ld/google-drive-context.jsonld
  - type: Features
    data:
      - 'Google Drive (and Workspace): hundreds of services across File Storage and Productivity'
      - 'Detailed pricing: see https://workspace.google.com/pricing.html'
      - 'Service: Drive API v3'
      - 'Service: Drive Activity API'
      - 'Service: Docs API'
      - 'Service: Sheets API'
      - 'Service: Slides API'
      - 'Service: Forms API'
      - 'Service: Apps Script'
      - 'Service: Workspace Marketplace API'
      - 'Service: Drive Labels API'
    sources:
      - https://workspace.google.com/pricing.html
      - https://focus.finops.org/
    updated: '2026-05-04'
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
