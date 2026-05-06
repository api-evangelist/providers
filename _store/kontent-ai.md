---
aid: kontent-ai
name: Kontent AI
description: Kontent.ai is a headless content management system providing REST and GraphQL APIs for delivering, managing, and synchronizing content across digital channels, plus image transformation and subscription management.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - CMS
  - Content
  - GraphQL
  - Headless CMS
url: https://raw.githubusercontent.com/api-evangelist/kontent-ai/refs/heads/main/apis.yml
access: 3rd-Party
position: Consumer
created: '2025-01-08'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: kontent-ai:delivery-api
    name: Kontent.ai Delivery REST API
    description: Read-only REST API for retrieving published content and previewing the latest content from a Kontent.ai environment.
    humanURL: https://kontent.ai/learn/docs/apis/delivery-api
    tags:
      - Content Delivery
      - REST
    properties:
      - type: Documentation
        url: https://kontent.ai/learn/docs/apis/delivery-api
  - aid: kontent-ai:delivery-graphql-api
    name: Kontent.ai Delivery GraphQL API
    description: GraphQL API providing the same content delivery capabilities as the Delivery REST API with GraphQL query semantics.
    humanURL: https://kontent.ai/learn/docs/apis/delivery-graphql-api
    tags:
      - Content Delivery
      - GraphQL
    properties:
      - type: Documentation
        url: https://kontent.ai/learn/docs/apis/delivery-graphql-api
  - aid: kontent-ai:image-transformation-api
    name: Kontent.ai Image Transformation API
    description: API for transforming and optimizing images served via the Delivery API, including resizing, cropping, and format conversion.
    humanURL: https://kontent.ai/learn/docs/apis/image-transformation-api
    tags:
      - Images
      - Transformation
    properties:
      - type: Documentation
        url: https://kontent.ai/learn/docs/apis/image-transformation-api
  - aid: kontent-ai:management-api-v2
    name: Kontent.ai Management API v2
    description: REST API for managing content, content models, taxonomy, assets, and environment settings programmatically.
    humanURL: https://kontent.ai/learn/docs/apis/management-api-v2
    tags:
      - Content Management
      - REST
    properties:
      - type: Documentation
        url: https://kontent.ai/learn/docs/apis/management-api-v2
  - aid: kontent-ai:sync-api
    name: Kontent.ai Sync API v2
    description: Read-only REST API for checking recent content item changes and keeping consuming applications synchronized with content updates.
    humanURL: https://kontent.ai/learn/docs/apis/sync-api-v2
    tags:
      - Sync
      - Content
    properties:
      - type: Documentation
        url: https://kontent.ai/learn/docs/apis/sync-api-v2
  - aid: kontent-ai:subscription-api
    name: Kontent.ai Subscription API
    description: REST API for managing users, projects, and environments within a Kontent.ai subscription.
    humanURL: https://kontent.ai/learn/docs/apis/subscription-api
    tags:
      - Subscription
      - Users
    properties:
      - type: Documentation
        url: https://kontent.ai/learn/docs/apis/subscription-api
common:
  - type: Website
    url: https://kontent.ai
  - type: Documentation
    url: https://kontent.ai/learn/docs
  - type: API Reference
    url: https://kontent.ai/learn/docs/apis
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
