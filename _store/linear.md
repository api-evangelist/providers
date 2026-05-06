---
aid: linear
url: https://raw.githubusercontent.com/api-evangelist/linear/refs/heads/main/apis.yml
modified: '2026-05-04'
maintainer:
  name: Kin Lane
  email: kin@apievangelist.com
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
common:
  - url: https://linear.app/developers
    type: Portal
  - url: https://linear.app/developers/graphql
    type: Getting Started
  - url: https://linear.app/developers/oauth-2-0-authentication
    type: Authentication
  - url: https://linear.app/developers/rate-limiting
    type: Rate Limits
  - url: https://linear.app/changelog
    type: Change Log
  - url: https://linear.app/developers/deprecations
    type: Deprecation Notice
  - url: https://linear.app/developers/migrating-from-1-x-to-2-x
    type: Migration Guide
  - url: https://linear.app/contact/support
    type: Support
  - url: https://linear.app
    type: Website
  - url: https://www.npmjs.com/package/@linear/sdk
    type: SDKs
  - url: https://github.com/linear/linear
    type: GitHub Organization
  - url: https://github.com/linear/linear/tree/master/packages/sdk
    type: GitHubRepository
  - url: https://linear.app/developers/integration-directory
    type: Developer Tools
  - url: https://raw.githubusercontent.com/api-evangelist/linear/refs/heads/main/openapi/linear-graphql-openapi.yml
    type: OpenAPI
  - url: https://raw.githubusercontent.com/api-evangelist/linear/refs/heads/main/asyncapi/linear-webhooks-asyncapi.yml
    type: AsyncAPI
  - url: https://raw.githubusercontent.com/api-evangelist/linear/refs/heads/main/json-schema/linear-issue-schema.json
    type: JSONSchema
  - url: https://raw.githubusercontent.com/api-evangelist/linear/refs/heads/main/json-ld/linear-context.jsonld
    type: JSONLDContext
  - type: Features
    data:
      - 'Free plan: 2 teams, 250 issues, unlimited members'
      - 'Basic at $10/user/mo: 5 teams, unlimited issues'
      - 'Business at $16/user/mo: unlimited teams, Triage Intelligence, Linear Insights'
      - 'Enterprise: SAML/SCIM, granular admin'
      - GraphQL API at api.linear.app/graphql
      - 'API key rate limit: 1,500 req/hr'
      - 'OAuth per-user rate limit: 1,200 req/hr'
      - 'Complexity-based query budget: 250k points/hr'
      - Webhooks for issue, comment, project events
      - Linear Agent platform for AI automations
      - OAuth 2.0 with granular scopes
      - Subscriptions for real-time updates over WebSocket
      - GitHub, GitLab, Slack, Sentry integrations
      - Triage Intelligence for incoming issue routing
      - Asks for converting Slack messages to issues
      - SCIM and SAML on Enterprise
    sources:
      - https://linear.app/pricing
    updated: '2026-05-04'
description: Linear's public API is built using GraphQL. It's the same API we use internally for developing our applications. If you are new to GraphQL, Apollo has resources for beginners. The official GraphQL documentation is another good starting point.
---
