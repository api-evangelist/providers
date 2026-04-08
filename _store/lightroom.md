---
aid: lightroom
url: https://raw.githubusercontent.com/api-evangelist/lightroom/refs/heads/main/apis.yml
apis:
- aid: lightroom:lightroom-services-api
  name: Lightroom Services API
  description: Core partner API for accessing Lightroom cloud catalog data, albums, and assets. Partner applications authenticate Lightroom customers through Adobe Identity Management System using a standard OAuth 2.0 workflow.
  humanURL: https://developer.adobe.com/lightroom/lightroom-api-docs/
  tags:
  - Albums
  - Assets
  - Catalogs
  - Photos
  properties:
  - type: Documentation
    url: https://developer.adobe.com/lightroom/lightroom-api-docs/api/
  - type: Authentication
    url: https://developer.adobe.com/developer-console/docs/guides/authentication/
  - type: GettingStarted
    url: https://developer.adobe.com/lightroom/lightroom-api-docs/getting-started/
  - type: ChangeLog
    url: https://developer.adobe.com/lightroom/lightroom-api-docs/release-notes/
- aid: lightroom:lightroom-firefly-services-api
  name: Adobe Lightroom API (Firefly Services)
  description: AI-powered image editing API available through Adobe Firefly Services. Provides auto tone, auto straighten, preset application, and programmatic editing capabilities using REST endpoints.
  humanURL: https://developer.adobe.com/firefly-services/docs/lightroom/
  tags:
  - AI
  - Auto Tone
  - Image Editing
  - Presets
  properties:
  - type: Documentation
    url: https://developer.adobe.com/firefly-services/docs/lightroom/
  - type: GettingStarted
    url: https://developer.adobe.com/firefly-services/docs/lightroom/getting_started/
name: Adobe Lightroom
tags:
- Cloud Storage
- Image Editing
- Metadata
- Photo Management
- Photography
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: APIs for Adobe Lightroom cloud services, enabling developers to access and manipulate photos, albums, and metadata programmatically. The Lightroom APIs are also available as part of Adobe Firefly Services for AI-powered image editing operations such as auto tone, auto straighten, and preset application.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

