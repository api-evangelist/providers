---
aid: dev-to
url: https://raw.githubusercontent.com/api-evangelist/dev-to/refs/heads/main/apis.yml
apis:
- aid: dev-to:forem-api
  name: Dev.to Forem API
  tags:
  - Articles
  - Blogging
  - Content Management
  - Developer Community
  - Social
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://dev.to/api
  humanURL: https://developers.forem.com/api/v1
  properties:
  - url: https://developers.forem.com/api/v1
    type: Documentation
  - url: openapi/dev-to-forem-api-openapi.yml
    type: OpenAPI
  description: The Dev.to Forem API (v1) is a RESTful API that provides programmatic access to the Dev.to developer community platform, which is built on the open-source Forem framework. The API enables developers to create, read, update, and manage articles (blog posts, discussions, help threads), comments, users, organizations, tags, followers, listings, and webhooks. It uses API key authentication, requires an accept header of application/vnd.forem.api-v1+json, and returns JSON responses.
- aid: dev-to:webhooks-api
  name: Dev.to Webhooks API
  tags:
  - Automation
  - Events
  - Notifications
  - Webhooks
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://dev.to/api
  humanURL: https://developers.forem.com/api/v1
  properties:
  - url: https://developers.forem.com/api/v1
    type: Documentation
  - url: asyncapi/dev-to-webhooks-asyncapi.yml
    type: AsyncAPI
  description: The Dev.to Webhooks API allows developers to subscribe to real-time notifications for events occurring on the Dev.to platform. By creating webhook subscriptions, applications can receive HTTP callbacks when specific events happen, such as new articles being published. This enables event-driven integrations and automation workflows that respond immediately to activity on the platform without the need to continuously poll the REST API for changes.
name: Dev To
tags:
- API
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Access Forem articles, users and other resources via API. For a real-world example of Forem in action, check out [DEV](https://www.dev.to). All endpoints can be accessed with the 'api-key' header and a accept header, but some of them are accessible publicly without authentication. Dates and date times, unless otherwise specified, must be in the [RFC 3339](https://tools.ietf.org/html/rfc3339) format.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

