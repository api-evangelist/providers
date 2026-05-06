---
aid: riverside
name: Riverside
description: Riverside is a professional podcast and video recording platform that enables remote studio-quality recording, AI-powered editing, and publishing. The Riverside Business API provides programmatic access to recordings, productions, studios, projects, exports, transcriptions, and webinar management for enterprise podcast production workflows. API access is available on Business plan only.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Podcast
  - Video Recording
  - Media
  - Content Creation
  - Audio
url: https://raw.githubusercontent.com/api-evangelist/riverside/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-05-02'
specificationVersion: '0.19'
apis:
  - aid: riverside:riverside-business-api
    name: Riverside Business API
    description: The Riverside Business API provides access to recording management, production workflows, studio and project organization, file downloads, transcription retrieval, export management, and webinar registration. Authentication uses API key bearer tokens available on Business plan. Base URL is https://platform.riverside.fm with v2 and v3 versioned paths.
    humanURL: https://docs.riverside.fm/
    baseURL: https://platform.riverside.fm
    tags:
      - Podcast
      - Recording
      - Media
      - Video
      - Audio
      - Transcription
    properties:
      - url: https://docs.riverside.fm/endpoints-reference/v3/
        type: Documentation
      - url: https://support.riverside.fm/hc/en-us/articles/9068592900381-Riverside-Business-API
        type: GettingStarted
      - url: https://raw.githubusercontent.com/api-evangelist/riverside/refs/heads/main/openapi/riverside-business-openapi.yml
        type: OpenAPI
      - url: https://raw.githubusercontent.com/api-evangelist/riverside/refs/heads/main/rules/riverside-business-rules.yml
        type: SpectralRules
      - url: https://raw.githubusercontent.com/api-evangelist/riverside/refs/heads/main/capabilities/podcast-production.yaml
        type: NaftikoCapabilities
      - url: https://raw.githubusercontent.com/api-evangelist/riverside/refs/heads/main/json-schema/riverside-recording-schema.json
        type: JSONSchema
    contact:
      - FN: Riverside Support
        url: https://support.riverside.fm
    features:
      - Recording Management
      - Production Organization
      - Studio and Project Hierarchy
      - File Downloads
      - Transcription Access
      - Export Management
      - Webinar Registration
      - AI Editing Tools
    useCases:
      - Enterprise podcast production
      - Remote video recording management
      - Automated transcription retrieval
      - Webinar content archiving
      - Media asset management
    solutions:
      - Podcast Production
      - Video Recording
      - Content Creation Platform
common:
  - type: Website
    url: https://riverside.fm
  - type: Documentation
    url: https://docs.riverside.fm/
  - type: Support
    url: https://support.riverside.fm
  - type: Pricing
    url: https://riverside.fm/pricing
  - type: Blog
    url: https://riverside.fm/blog
  - type: PrivacyPolicy
    url: https://riverside.fm/privacy-policy
  - type: TermsOfService
    url: https://riverside.fm/terms-of-service
  - type: SignUp
    url: https://riverside.fm/signup
  - type: Login
    url: https://riverside.fm/login
  - type: JSONLDContext
    url: https://raw.githubusercontent.com/api-evangelist/riverside/refs/heads/main/json-ld/riverside-context.jsonld
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/riverside/refs/heads/main/vocabulary/riverside-vocabulary.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
