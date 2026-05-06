---
aid: lightroom
name: Adobe Lightroom
description: APIs for Adobe Lightroom cloud services, enabling developers to access and manipulate photos, albums, and metadata programmatically. The Lightroom APIs are also available as part of Adobe Firefly Services for AI-powered image editing operations such as auto tone, auto straighten, and preset application.
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Cloud Storage
  - Image Editing
  - Metadata
  - Photo Management
  - Photography
url: https://raw.githubusercontent.com/api-evangelist/lightroom/refs/heads/main/apis.yml
created: '2024-01-01'
modified: '2026-04-18'
specificationVersion: '0.19'
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
      - type: OpenAPI
        url: openapi/lightroom-services-openapi.yml
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
      - type: OpenAPI
        url: openapi/lightroom-firefly-services-openapi.yml
common:
  - url: https://developer.adobe.com/firefly-services/docs/lightroom/
    type: Features
  - url: https://developer.adobe.com/lightroom/lightroom-api-docs/
    type: UseCases
  - url: https://developer.adobe.com/firefly-services/docs/lightroom/
    type: Integrations
  - url: https://developer.adobe.com/lightroom/lightroom-api-docs/
    type: Documentation
  - url: https://developer.adobe.com/developer-console/docs/guides/authentication/
    type: Authentication
  - url: https://developer.adobe.com/console
    type: Console
  - url: https://developer.adobe.com/console
    type: SignUp
  - url: https://status.adobe.com/
    type: StatusPage
  - url: https://blog.developer.adobe.com/
    type: Blog
  - url: https://developer.adobe.com/lightroom/lightroom-api-docs/release-notes/
    type: ChangeLog
  - url: https://www.adobe.com/legal/terms.html
    type: TermsOfService
  - url: https://www.adobe.com/privacy/policy.html
    type: PrivacyPolicy
  - url: https://github.com/AdobeDocs/lightroom-public-apis
    type: GitHubRepository
  - url: https://github.com/AdobeDocs
    type: GitHubOrganization
  - url: https://developer.adobe.com/firefly-services/docs/lightroom/
    type: SDK
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
