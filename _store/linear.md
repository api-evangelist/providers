---
aid: linear
url: https://raw.githubusercontent.com/api-evangelist/linear/refs/heads/main/apis.yml
apis:
- aid: linear:linear-graphql-api
  name: Linear GraphQL API
  tags:
  - Agile
  - GraphQL
  - Issue Tracking
  - Project Management
  image: https://raw.githubusercontent.com/api-evangelist/linear/refs/heads/main/image.png
  humanURL: https://linear.app/developers/graphql
  baseURL: https://api.linear.app/graphql
  properties:
  - url: https://linear.app/developers/graphql
    type: Documentation
  - url: https://studio.apollographql.com/public/Linear-API/schema/reference?variant=current
    type: Reference
  - url: https://linear.app/developers/oauth-2-0-authentication
    type: Authentication
  - url: https://linear.app/developers/sdk
    type: Getting Started
  - url: https://linear.app/developers/rate-limiting
    type: Rate Limits
  - url: https://linear.app/developers/pagination
    type: Pagination
  - url: https://linear.app/developers/filtering
    type: Filtering
  - url: https://linear.app/developers/deprecations
    type: Deprecation Notice
  - url: https://raw.githubusercontent.com/api-evangelist/linear/refs/heads/main/openapi/linear-graphql-openapi.yml
    type: OpenAPI
  - url: https://raw.githubusercontent.com/api-evangelist/linear/refs/heads/main/json-schema/linear-issue-schema.json
    type: JSONSchema
  - url: https://raw.githubusercontent.com/api-evangelist/linear/refs/heads/main/json-ld/linear-context.jsonld
    type: JSONLDContext
  description: Linear's public GraphQL API provides full access to create, read, update, and query issues, projects, cycles, roadmaps, and teams. It is the same API Linear uses internally for its own applications, supporting pagination, filtering, attachments, and file uploads.
- aid: linear:linear-webhooks-api
  name: Linear Webhooks API
  tags:
  - Events
  - Real-Time
  - Webhooks
  image: https://raw.githubusercontent.com/api-evangelist/linear/refs/heads/main/image.png
  humanURL: https://linear.app/developers/webhooks
  baseURL: https://api.linear.app/graphql
  properties:
  - url: https://linear.app/developers/webhooks
    type: Documentation
  - url: https://linear.app/developers/sdk-webhooks
    type: Getting Started
  - url: https://raw.githubusercontent.com/api-evangelist/linear/refs/heads/main/asyncapi/linear-webhooks-asyncapi.yml
    type: AsyncAPI
  description: Linear webhooks deliver HTTP push notifications whenever data is created, updated, or removed. Webhooks are organization-scoped and can be configured for all public teams or a single team, enabling integrations that trigger CI builds, update external systems, or send messages based on issue activity.
name: Linear
tags:
- API
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Linear's public API is built using GraphQL. It's the same API we use internally for developing our applications. If you are new to GraphQL, Apollo has resources for beginners. The official GraphQL documentation is another good starting point.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

