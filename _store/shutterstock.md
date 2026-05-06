---
aid: shutterstock
name: Shutterstock
description: Shutterstock is a leading global technology company providing high-quality images, videos, audio tracks, sound effects, and editorial content to businesses, individuals, and organizations worldwide. With a library of over 350 million assets, Shutterstock offers royalty-free creative content for marketing campaigns, website designs, social media, and more. The Shutterstock API provides programmatic access to search, browse, license, and download media assets, manage collections, access computer vision features, and handle OAuth 2.0 authentication. It also includes contributor profile management and user account operations.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Images
  - Media
  - Photos
  - Stock Images
  - Videos
  - Audio
  - Licensing
  - Creative Content
url: https://raw.githubusercontent.com/api-evangelist/shutterstock/refs/heads/main/apis.yml
created: '2026-05-02'
modified: '2026-05-02'
specificationVersion: '0.19'
apis:
  - aid: shutterstock:shutterstock-api
    name: Shutterstock API
    description: The Shutterstock REST API v2 provides access to 350M+ images, videos, audio tracks, sound effects, and editorial content. It supports searching by keyword, color, category, and visual similarity (computer vision). Licensing operations support subscription and on-demand purchase models. Collections allow users to organize and save assets. OAuth 2.0 is required for licensed content operations; Basic Auth is available for search and browse endpoints.
    humanURL: https://www.shutterstock.com/developers
    baseURL: https://api.shutterstock.com
    tags:
      - Images
      - Videos
      - Audio
      - Stock Media
      - Licensing
      - Creative Content
      - Computer Vision
      - Editorial
    properties:
      - type: Documentation
        url: https://www.shutterstock.com/developers/documentation
      - type: ApiReference
        url: https://api-reference.shutterstock.com/
      - type: GettingStarted
        url: https://www.shutterstock.com/developers/documentation/getting-started
      - type: Authentication
        url: https://www.shutterstock.com/developers/documentation/authentication
      - type: Tutorial
        url: https://www.shutterstock.com/developers/documentation/tutorial
      - type: Plans
        url: https://www.shutterstock.com/api/pricing
      - type: SDK
        url: https://www.shutterstock.com/developers/documentation/javascript-sdk
      - type: GitHubOrganization
        url: https://github.com/shutterstock
      - type: OpenAPI
        url: openapi/shutterstock-openapi.yml
      - type: JSONSchema
        url: json-schema/shutterstock-image-schema.json
      - type: JSONSchema
        url: json-schema/shutterstock-video-schema.json
      - type: JSONStructure
        url: json-structure/shutterstock-image-structure.json
      - type: JSONLD
        url: json-ld/shutterstock-context.jsonld
      - type: SpectralRules
        url: rules/shutterstock-rules.yml
      - type: NaftikoCapabilities
        url: capabilities/media-search-and-licensing.yaml
      - type: Vocabulary
        url: vocabulary/shutterstock-vocabulary.yml
    contact:
      - FN: Shutterstock Developer Support
        url: https://www.shutterstock.com/developers/contact-us
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
