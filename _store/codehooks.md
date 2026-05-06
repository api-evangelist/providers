---
aid: codehooks
url: https://raw.githubusercontent.com/api-evangelist/codehooks/refs/heads/main/apis.yml
name: Codehooks
tags:
  - Backend
  - Database
  - Events
  - Hooks
  - JavaScript
  - NoSQL
  - Queues
  - Serverless
  - Webhooks
  - Workers
  - Workflows
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
x-type: company
created: '2025-02-08'
modified: '2026-04-26'
position: Consumer
description: Codehooks is a JavaScript-native serverless backend platform that bundles a NoSQL document database, key-value store, persistent queues with workers, CRON jobs, blob storage, frontend hosting, and an automatic CRUD REST API in a single CLI-deployable runtime. Developers write small Node.js handler files and Codehooks generates a secure REST API, OpenAPI documentation, and event hooks (onBefore/onAfter Create/Read/Update/Delete) without managing servers. The platform targets agent-native and AI backend use cases where simple, fast, MongoDB-style data access and event-driven automation matter.
apis:
  - aid: codehooks:codehooks-database-rest-api
    name: Codehooks Database REST API
    tags:
      - CRUD
      - Database
      - Documents
      - Key-Value
      - NoSQL
      - Queues
      - REST
    humanURL: https://codehooks.io/docs/
    baseURL: https://{projectId}.api.codehooks.io/{space}
    properties:
      - url: https://codehooks.io/docs/
        type: Documentation
      - url: https://codehooks.io/docs/restapi
        type: APIReference
      - url: openapi/codehooks-database-rest-api-openapi.yml
        type: OpenAPI
    description: Auto-generated, secure REST API for Codehooks NoSQL collections, the built-in key-value store, and queue topics. Supports MongoDB-style query operators ($gt, $lt, $in, $nin, $exists, $regex, $or, $and), pagination, sorting, field selection, bulk update/delete by query, counts, and increment/decrement on key-value entries. Authenticated via API key.
    x-features:
      - Automatic CRUD REST API via app.crudlify()
      - MongoDB-like query language with $gt/$lt/$in/$exists/$regex/$or/$and
      - Pagination, sort, field selection
      - Bulk updateByQuery and deleteByQuery
      - Key-value cache with TTL plus increment/decrement
      - Persistent queue API for asynchronous job processing
      - Auto-generated OpenAPI/Swagger from schema
      - Sub-5-second deploys via the codehooks CLI
    x-use-cases:
      - Internal CRUD apps and admin dashboards
      - Webhook receivers (Stripe, GitHub, Shopify) with persistent queues
      - Headless content backends for SPA/PWA hosting
      - AI agent state and memory backends
      - Lightweight microservices replacing custom Node.js + MongoDB stacks
  - aid: codehooks:codehooks-events
    name: Codehooks Events (AsyncAPI)
    tags:
      - Async
      - Events
      - Hooks
      - Lifecycle
      - Queues
      - Workers
    humanURL: https://codehooks.io/docs/hooks-and-workers
    properties:
      - url: https://codehooks.io/docs/hooks-and-workers
        type: Documentation
      - url: asyncapi/codehooks-events-asyncapi.yml
        type: AsyncAPI
    description: Asynchronous CRUD lifecycle hooks (onBeforeCreate, onAfterCreate, onBeforeRead, onAfterRead, onBeforeUpdate, onAfterUpdate, onBeforeDelete, onAfterDelete) and queue worker processing (onQueueJob) for serverless backend operations. AsyncAPI describes these as event-driven channels backed by an internal pub/sub and persistent queue runtime.
    x-features:
      - Eight CRUD lifecycle hooks (before/after for each verb)
      - Queue worker (onQueueJob) for deferred work
      - Automatic retry and persistent state on workers
      - CRON-triggered jobs with multi-schedule support
      - Stateful workflow orchestration
    x-use-cases:
      - Validation and transformation on writes
      - Audit logging and outbound webhooks
      - PDF/email generation deferred to a worker
      - AI inference pipelines triggered after document creation
      - Scheduled batch jobs (CRON)
common:
  - type: Website
    url: https://codehooks.io/
  - type: Documentation
    url: https://codehooks.io/docs/
  - type: GettingStarted
    url: https://codehooks.io/docs/quickstart-cli
  - type: Blog
    url: https://codehooks.io/blog
  - type: Pricing
    url: https://codehooks.io/#pricing
  - type: GitHub
    url: https://github.com/RestDB
  - type: NPMPackage
    url: https://www.npmjs.com/package/codehooks-js
  - type: TermsOfService
    url: https://codehooks.io/terms
  - type: PrivacyPolicy
    url: https://codehooks.io/privacy
  - url: json-ld/codehooks-context.jsonld
    type: JSON-LD
  - url: json-schema/codehooks-document-schema.json
    type: JSONSchema
  - url: json-schema/codehooks-key-value-schema.json
    type: JSONSchema
  - url: json-schema/codehooks-queue-job-schema.json
    type: JSONSchema
  - url: rules/codehooks-rules.yml
    type: Spectral
  - url: capabilities/codehooks-capabilities.yml
    type: NaftikoCapabilities
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
---
