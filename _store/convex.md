---
aid: convex
url: https://raw.githubusercontent.com/api-evangelist/convex/refs/heads/main/apis.yml
apis:
- aid: convex:http-api
  name: Convex HTTP API
  tags:
  - Backend
  - Functions
  - Real-Time
  - Serverless
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.example.com
  humanURL: https://docs.convex.dev/http-api/
  properties:
  - url: https://docs.convex.dev/http-api/
    type: Documentation
  - url: openapi/convex-http-api-openapi.yml
    type: OpenAPI
  description: The Convex HTTP API is a REST interface for executing backend functions deployed on a Convex backend. It provides endpoints for invoking query, mutation, and action functions using POST requests to paths such as /api/query, /api/mutation, /api/action, and the unified /api/run/{functionIdentifier} endpoint. Each deployment has its own base URL found in the Convex dashboard settings, typically in the format https://{deployment-name}.convex.cloud.
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
  description: The Convex Management API is a REST API for provisioning and managing Convex projects and deployments programmatically. It enables developers and platform integrations to create projects, list deployments, and perform team-level operations without using the Convex dashboard. The API uses Bearer token authentication, supporting both Team Access Tokens and OAuth Application Tokens for third-party integrations.
- aid: convex:deployment-platform-api
  name: Convex Deployment Platform API
  tags:
  - Administration
  - Configuration
  - Deployment
  - Environment Variables
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.example.com
  humanURL: https://docs.convex.dev/deployment-platform-api
  properties:
  - url: https://docs.convex.dev/deployment-platform-api
    type: Documentation
  - url: openapi/convex-deployment-platform-api-openapi.yml
    type: OpenAPI
  description: The Convex Deployment Platform API is a deployment-scoped administrative API for configuring individual Convex deployments. It exposes private endpoints accessible only to deployment administrators, supporting operations such as managing environment variables and other deployment configuration settings. Each deployment has its own endpoint in the format https://{deployment-name}.convex.cloud/api/v1/.
- aid: convex:javascript-sdk
  name: Convex JavaScript SDK
  tags:
  - Client Library
  - JavaScript
  - SDK
  - TypeScript
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.example.com
  humanURL: https://docs.convex.dev/api/
  properties:
  - url: https://docs.convex.dev/api/
    type: Documentation
  description: The Convex JavaScript SDK is a collection of TypeScript/JavaScript packages for building applications on the Convex backend platform. It includes convex/server for defining backend functions and database schemas, convex/react for React hooks and the ConvexReactClient, convex/browser for the ConvexHttpClient in non-React browser environments, convex/values for working with Convex-stored data types, and framework integrations for Next.js, React Native, and other environments.
- aid: convex:server-sdk
  name: Convex Server SDK
  tags:
  - Backend
  - Database
  - Serverless Functions
  - TypeScript
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.example.com
  humanURL: https://docs.convex.dev/functions
  properties:
  - url: https://docs.convex.dev/functions
    type: Documentation
  description: The Convex Server SDK (convex/server) is the TypeScript library for defining backend logic deployed on Convex. It provides primitives for writing query functions for read-only database access, mutation functions for transactional writes, and action functions for general-purpose server-side operations including calling external services.
name: Convex
tags:
- API
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Connecting to Convex directly with HTTP.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

