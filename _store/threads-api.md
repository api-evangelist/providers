---
aid: threads-api
name: Threads
description: The Meta Threads API enables developers to build integrations for the Threads social media platform. It supports publishing text, image, video, carousel, and quote posts, reading and managing replies, accessing profile information, retrieving media insights, and managing account settings. Authentication uses OAuth 2.0 with scoped access tokens.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Social
  - Social Networks
  - Meta
  - Publishing
  - Media
created: '2024-11-16'
modified: '2026-05-03'
url: https://raw.githubusercontent.com/api-evangelist/threads-api/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: threads-api:threads-api
    name: Threads API
    description: The Threads API enables developers to build their own unique integrations, and helps creators and brands manage their Threads presence at scale. Supports single and carousel post publishing, reply management, profile retrieval, media insights, account insights, and publishing quota management. Requires OAuth 2.0 user access tokens with appropriate scopes.
    humanURL: https://developers.facebook.com/docs/threads/
    baseURL: https://graph.threads.net
    tags:
      - Social Networks
      - Publishing
      - Media
      - Insights
      - Replies
    properties:
      - type: Documentation
        url: https://developers.facebook.com/docs/threads/
      - type: OpenAPI
        url: openapi/threads-api-openapi.yml
      - type: PostmanCollection
        url: https://www.postman.com/meta/threads/collection/dht3nzz/threads-api?action=share&creator=35240
      - type: GettingStarted
        url: https://developers.facebook.com/docs/threads/get-started
      - type: Authentication
        url: https://developers.facebook.com/docs/threads/get-started/get-access-tokens-and-permissions
      - type: Webhooks
        url: https://developers.facebook.com/docs/threads/webhooks
      - type: ChangeLog
        url: https://developers.facebook.com/docs/threads/changelog
      - type: PostmanWorkspace
        url: https://www.postman.com/meta/threads/overview
      - type: JSONSchema
        url: json-schema/threads-api-thread-schema.json
common:
  - type: Website
    url: https://www.threads.net/
  - type: DeveloperPortal
    url: https://developers.facebook.com/docs/threads/
  - type: GettingStarted
    url: https://developers.facebook.com/docs/threads/get-started
  - type: Authentication
    url: https://developers.facebook.com/docs/threads/get-started/get-access-tokens-and-permissions
  - type: ChangeLog
    url: https://developers.facebook.com/docs/threads/changelog
  - type: Webhooks
    url: https://developers.facebook.com/docs/threads/webhooks
  - type: PostmanWorkspace
    url: https://www.postman.com/meta/threads/overview
  - type: TermsOfService
    url: https://developers.facebook.com/terms/
  - type: PrivacyPolicy
    url: https://www.facebook.com/privacy/policy/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
