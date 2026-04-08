---
aid: google-photos
url: https://raw.githubusercontent.com/api-evangelist/google-photos/refs/heads/main/apis.yml
apis:
- name: Google Photos Library API v1
  description: The Google Photos Library API provides programmatic access to Google Photos for managing media items and albums. Supports uploading, searching, listing, and sharing photos and videos.
  humanURL: https://developers.google.com/photos
  baseURL: https://photoslibrary.googleapis.com/v1
  properties:
  - type: OpenAPI
    url: openapi/photos.yml
  - type: JSONSchema
    url: json-schema/photos.json
  overlays: []
name: Google Photos Library
tags:
- Albums
- Google
- Images
- Media
- Photos
- Sharing
- Storage
type: Contract
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: The Google Photos Library API allows you to manage photos, videos, and albums in Google Photos. You can create and manage albums, upload and retrieve media items, search through your photo library, and share albums with other users. The API uses OAuth 2.0 for authentication and requires a Google account.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

