---
aid: convex
url: https://raw.githubusercontent.com/api-evangelist/convex/refs/heads/main/apis.yml
name: Convex
x-type: company
description: Convex is a serverless backend platform that provides a real-time database, cloud functions, and infrastructure for building modern web and mobile applications. It offers a TypeScript-first developer experience with reactive queries, transactional mutations, and integrated file storage, all accessible through a suite of HTTP, management, and deployment APIs alongside JavaScript and server SDKs for full-stack application development. The platform is SOC 2 Type II, HIPAA, and GDPR compliant.
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Backend
  - Database
  - Functions
  - Real-Time
  - Reactive
  - Serverless
  - TypeScript
created: '2026-03-21'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: convex:http-api
    name: Convex HTTP API
    tags:
      - Backend
      - Functions
      - Real-Time
      - Serverless
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://{deployment-name}.convex.cloud
    humanURL: https://docs.convex.dev/http-api/
    properties:
      - url: https://docs.convex.dev/http-api/
        type: Documentation
      - url: openapi/convex-http-api-openapi.yml
        type: OpenAPI
    description: The Convex HTTP API is a REST interface for executing backend functions deployed on a Convex backend. It provides endpoints for invoking query, mutation, and action functions using POST requests to paths such as /api/query, /api/mutation, /api/action, and the unified /api/run/{functionIdentifier} endpoint. Each deployment has its own base URL found in the Convex dashboard settings, typically in the format https://{deployment-name}.convex.cloud.
    x-features:
      - POST /api/query for reactive read-only function execution
      - POST /api/mutation for transactional database writes
      - POST /api/action for general-purpose server-side operations
      - POST /api/run/{functionIdentifier} unified function invocation
      - Optional bearer token auth for end users, Convex scheme for admin
    x-useCases:
      - Calling Convex functions from non-JavaScript backends
      - Server-to-server orchestration of Convex queries and mutations
      - Webhook handlers that trigger Convex actions
      - Lightweight scripts that execute one-off function calls
      - Testing deployed Convex functions from curl or HTTPie
  - aid: convex:management-api
    name: Convex Management API
    tags:
      - Administration
      - Deployments
      - Management
      - Projects
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.convex.dev/v1
    humanURL: https://docs.convex.dev/management-api
    properties:
      - url: https://docs.convex.dev/management-api
        type: Documentation
      - url: https://api.convex.dev/v1/openapi.json
        type: OpenAPI
      - url: openapi/convex-management-api-openapi.yml
        type: OpenAPI
    description: The Convex Management API is a REST API for provisioning and managing Convex projects and deployments programmatically. It enables developers and platform integrations to create projects, list deployments, manage deploy keys, configure custom domains, and perform team-level operations without using the Convex dashboard. The API uses Bearer token authentication, supporting both Team Access Tokens and OAuth Application Tokens for third-party integrations.
    x-features:
      - Projects and deployments lifecycle management
      - Deploy key and preview deploy key issuance
      - Personal access tokens and team access tokens
      - Custom domain attachment for production deployments
      - Default environment variables and team membership management
      - Published OpenAPI spec at https://api.convex.dev/v1/openapi.json
    x-useCases:
      - Building Convex platform integrations and CI/CD pipelines
      - Provisioning preview deployments per pull request
      - Automating environment variable configuration for new projects
      - Inviting team members and rotating credentials programmatically
      - Listing all deployments for governance and inventory tooling
  - aid: convex:deployment-platform-api
    name: Convex Deployment Platform API
    tags:
      - Administration
      - Configuration
      - Deployment
      - Environment Variables
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://{deployment-name}.convex.cloud/api/v1
    humanURL: https://docs.convex.dev/deployment-platform-api
    properties:
      - url: https://docs.convex.dev/deployment-platform-api
        type: Documentation
      - url: openapi/convex-deployment-platform-api-openapi.yml
        type: OpenAPI
    description: The Convex Deployment Platform API is a deployment-scoped administrative API for configuring individual Convex deployments. It exposes private endpoints accessible only to deployment administrators, supporting operations such as managing environment variables and other deployment configuration settings. Each deployment has its own endpoint in the format https://{deployment-name}.convex.cloud/api/v1/.
    x-features:
      - Deployment-scoped administrative access
      - Environment variable configuration management
      - Bearer token Authorization with the Convex scheme
      - Beta API surface intended for platform integrations
    x-useCases:
      - Pushing environment variable updates from CI/CD pipelines
      - Reading deployment configuration for IaC drift detection
      - Building admin tooling that targets a specific deployment
      - Synchronizing config across multiple Convex deployments
  - aid: convex:javascript-sdk
    name: Convex JavaScript SDK
    tags:
      - Client Library
      - JavaScript
      - SDK
      - TypeScript
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://docs.convex.dev/api/
    properties:
      - url: https://docs.convex.dev/api/
        type: Documentation
      - url: https://www.npmjs.com/package/convex
        type: Package
    description: The Convex JavaScript SDK is a collection of TypeScript/JavaScript packages for building applications on the Convex backend platform. It includes convex/server for defining backend functions and database schemas, convex/react for React hooks and the ConvexReactClient, convex/browser for the ConvexHttpClient in non-React browser environments, convex/values for working with Convex-stored data types, and framework integrations for Next.js, React Native, and other environments.
    x-features:
      - ConvexReactClient with reactive useQuery, useMutation hooks
      - ConvexHttpClient for non-React JavaScript runtimes
      - Strongly typed client generated from project schema
      - Authentication helpers for Clerk, Auth0, and custom providers
      - Framework integrations for Next.js, React Native, and Svelte
    x-useCases:
      - Building real-time React applications backed by Convex
      - Embedding Convex queries in Next.js server components
      - Server-rendered apps that read Convex data on the server
      - Cross-platform mobile apps using React Native and Convex
  - aid: convex:server-sdk
    name: Convex Server SDK
    tags:
      - Backend
      - Database
      - Serverless Functions
      - TypeScript
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://docs.convex.dev/functions
    properties:
      - url: https://docs.convex.dev/functions
        type: Documentation
      - url: https://docs.convex.dev/database/schemas
        type: Documentation
    description: The Convex Server SDK (convex/server) is the TypeScript library for defining backend logic deployed on Convex. It provides primitives for writing query functions for read-only database access, mutation functions for transactional writes, and action functions for general-purpose server-side operations including calling external services. The SDK supports schema definition, full-text search indexes, vector search indexes, file storage, scheduled functions, cron jobs, and HTTP routing via the HttpRouter class.
    x-features:
      - query, mutation, and action function primitives
      - defineSchema and defineTable for typed database modeling
      - Full-text and vector search indexes
      - Cron jobs and scheduled function execution
      - HttpRouter for custom HTTP endpoints
      - File storage with signed URL generation
    x-useCases:
      - Authoring Convex backend functions in TypeScript
      - Modeling reactive database schemas with type safety
      - Implementing AI workflows with vector search
      - Scheduling recurring background work with cron jobs
      - Building HTTP webhook handlers inside Convex deployments
common:
  - type: Portal
    url: https://www.convex.dev/developers
  - type: Documentation
    url: https://docs.convex.dev/
  - type: Website
    url: https://www.convex.dev
  - type: Login
    url: https://dashboard.convex.dev/
  - type: Blog
    url: https://stack.convex.dev/
  - type: GitHub
    url: https://github.com/get-convex
  - type: Discord
    url: https://convex.dev/community
  - type: TermsOfService
    url: https://www.convex.dev/legal/terms
  - type: PrivacyPolicy
    url: https://www.convex.dev/legal/privacy
  - type: JSONSchema
    url: json-schema/convex-function-schema.json
  - type: JSONSchema
    url: json-schema/convex-deployment-schema.json
  - type: JSON-LD
    url: json-ld/convex-context.jsonld
  - type: Vocabulary
    url: vocabulary/convex-vocabulary.yml
maintainers:
  - FN: API Evangelist
    email: info@apievangelist.com
---
