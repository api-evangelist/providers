---
aid: sanity
name: Sanity
description: Sanity is a composable content platform providing a headless CMS with a real-time collaborative editor (Sanity Studio) and a powerful HTTP API for managing structured content. The Sanity Content Lake stores content as flexible documents queryable via GROQ (Graph-Relational Object Queries). Key API capabilities include document querying, mutations, real-time listening, asset management, project management, webhooks, scheduling, roles and permissions, vector embeddings, and AI-powered content agents.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Headless CMS
  - Content Management
  - GROQ
  - Real-Time
  - Structured Content
  - Developer Platform
created: '2026-05-02'
modified: '2026-05-02'
x-profiled: 2026-05
url: https://raw.githubusercontent.com/api-evangelist/sanity/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: sanity:sanity-query-api
    name: Sanity Query API
    description: The Sanity Query API enables querying Content Lake documents using GROQ (Graph-Relational Object Queries). Supports GET for queries under 11 KB and POST for larger queries. Available at both the standard API endpoint and a CDN endpoint for edge-cached results. Supports perspectives (drafts, published), result source maps, and query explain functionality.
    humanURL: https://www.sanity.io/docs/http-query
    tags:
      - GROQ
      - Query
      - Content Lake
      - CDN
    properties:
      - type: Documentation
        url: https://www.sanity.io/docs/http-query
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/sanity/refs/heads/main/openapi/sanity-openapi.yml
      - type: JSONSchema
        url: json-schema/sanity-document-schema.json
      - type: JSONSchema
        url: json-schema/sanity-webhook-schema.json
  - aid: sanity:sanity-mutation-api
    name: Sanity Mutation API
    description: The Sanity Mutation API enables creating, updating, patching, and deleting documents in Content Lake. Mutations are submitted as arrays of operations (create, createOrReplace, createIfNotExists, patch, delete) against a dataset endpoint.
    humanURL: https://www.sanity.io/docs/http-reference
    tags:
      - Mutation
      - Documents
      - CRUD
      - Content Lake
    properties:
      - type: Documentation
        url: https://www.sanity.io/docs/http-reference
  - aid: sanity:sanity-assets-api
    name: Sanity Assets API
    description: The Sanity Assets API handles uploading, retrieving, and managing file and image assets in Content Lake. Assets are stored as documents and referenced from content documents.
    humanURL: https://www.sanity.io/docs/http-reference
    tags:
      - Assets
      - Images
      - Files
      - Upload
    properties:
      - type: Documentation
        url: https://www.sanity.io/docs/http-reference
  - aid: sanity:sanity-projects-api
    name: Sanity Projects API
    description: The Sanity Projects API enables programmatic management of Sanity projects including creating projects, managing datasets, configuring CORS origins, managing access tokens, and checking user permissions. Authentication uses Bearer tokens.
    humanURL: https://www.sanity.io/docs/projects-api
    tags:
      - Projects
      - Datasets
      - Access Control
      - Tokens
    properties:
      - type: Documentation
        url: https://www.sanity.io/docs/projects-api
  - aid: sanity:sanity-webhooks-api
    name: Sanity Webhooks API
    description: The Sanity Webhooks API enables configuring event-driven notifications for content changes. Webhooks can be created to trigger on document create, update, delete, and publish events with customizable filter expressions.
    humanURL: https://www.sanity.io/docs/http-reference
    tags:
      - Webhooks
      - Events
      - Notifications
      - Real-Time
    properties:
      - type: Documentation
        url: https://www.sanity.io/docs/http-reference
  - aid: sanity:sanity-listen-api
    name: Sanity Listen API
    description: The Sanity Listen API provides real-time event streaming via Server-Sent Events (SSE) for content changes in a dataset. Clients can subscribe to a GROQ query and receive real-time notifications when matching documents change.
    humanURL: https://www.sanity.io/docs/http-reference
    tags:
      - Real-Time
      - SSE
      - Events
      - Streaming
    properties:
      - type: Documentation
        url: https://www.sanity.io/docs/http-reference
  - aid: sanity:sanity-roles-api
    name: Sanity Roles API
    description: The Sanity Roles API provides endpoints for managing user roles and permissions within Sanity projects. Supports predefined roles (Administrator, Read+Write, Read, Viewer) and custom role management.
    humanURL: https://www.sanity.io/docs/roles-reference
    tags:
      - Roles
      - Permissions
      - Access Control
      - Security
    properties:
      - type: Documentation
        url: https://www.sanity.io/docs/roles-reference
  - aid: sanity:sanity-scheduling-api
    name: Sanity Scheduling API
    description: The Sanity Scheduling API enables scheduling content for future publication or unpublication at specific times, supporting editorial workflows and content calendars.
    humanURL: https://www.sanity.io/docs/http-reference
    tags:
      - Scheduling
      - Publishing
      - Content Calendar
      - Workflow
    properties:
      - type: Documentation
        url: https://www.sanity.io/docs/http-reference
  - aid: sanity:sanity-embeddings-index-api
    name: Sanity Embeddings Index API
    description: The Sanity Embeddings Index API enables creating and managing vector embedding indexes for Content Lake documents, supporting semantic search and AI-powered content retrieval workflows.
    humanURL: https://www.sanity.io/docs/http-reference
    tags:
      - Embeddings
      - Vector Search
      - AI
      - Semantic Search
    properties:
      - type: Documentation
        url: https://www.sanity.io/docs/http-reference
common:
  - type: Website
    url: https://www.sanity.io
  - type: Documentation
    url: https://www.sanity.io/docs
  - type: HTTP API Reference
    url: https://www.sanity.io/docs/http-reference
  - type: Developer Portal
    url: https://www.sanity.io/docs
  - type: GitHub Organization
    url: https://github.com/sanity-io
  - type: Getting Started
    url: https://www.sanity.io/docs/getting-started-with-sanity
  - type: JavaScript SDK
    url: https://www.npmjs.com/package/@sanity/client
  - type: Pricing
    url: https://www.sanity.io/pricing
  - type: Community
    url: https://slack.sanity.io
  - type: Blog
    url: https://www.sanity.io/blog
  - type: Status
    url: https://status.sanity.io
  - type: Vocabulary
    url: vocabulary/sanity-vocabulary.yml
  - type: SpectralRules
    url: rules/sanity-rules.yml
  - type: Capabilities
    url: capabilities/content-management.yaml
  - type: JSONLD
    url: json-ld/sanity-context.jsonld
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
