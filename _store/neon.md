---
aid: neon
name: Neon
description: Neon is a serverless Postgres platform that provides fully managed, scalable PostgreSQL databases optimized for modern cloud and edge application development. Their developer platform offers management APIs, data APIs, authentication services, and serverless drivers for building and automating database-driven workflows.
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Databases
  - Serverless
  - Postgres
  - Infrastructure
  - Authentication
  - Edge
url: https://raw.githubusercontent.com/api-evangelist/neon/refs/heads/main/apis.yml
created: '2025-03-07'
modified: '2026-05-04'
specificationVersion: '0.19'
apis:
  - aid: neon:management-api
    name: Neon Management API
    description: The Neon Management API is a RESTful interface for programmatically managing Neon serverless Postgres resources. It allows developers to create and manage projects, branches, databases, roles, compute endpoints, and operations. The API uses bearer token authentication and supports everything available through the Neon Console, enabling automation of database infrastructure workflows. An OpenAPI 3.0 specification is available along with TypeScript, Python, and Go SDKs.
    humanURL: https://neon.com/docs/reference/api-reference
    baseURL: https://console.neon.tech/api/v2
    tags:
      - Databases
      - Serverless
      - Postgres
      - Projects
      - Branches
      - Compute
      - Infrastructure
    properties:
      - type: Documentation
        url: https://neon.com/docs/reference/api-reference
      - type: Documentation
        url: https://api-docs.neon.tech/reference/getting-started-with-neon-api
      - type: OpenAPI
        url: openapi/neon-management-api-openapi.yml
  - aid: neon:data-api
    name: Neon Data API
    description: The Neon Data API provides a secure, stateless HTTP interface to Neon Postgres databases, allowing developers to access and manage data directly from web browsers, serverless functions, and edge runtimes using standard HTTP methods. It is fully compatible with PostgREST, enabling querying via standard HTTP clients like Postman or cURL. The Data API supports JWT-based authentication and integrates with Row-Level Security policies, making it suitable for building secure client-facing applications without a traditional backend.
    humanURL: https://neon.com/docs/data-api/overview
    tags:
      - Databases
      - Serverless
      - Postgres
      - REST
      - Data
      - PostgREST
      - HTTP
    properties:
      - type: Documentation
        url: https://neon.com/docs/data-api/overview
      - type: Documentation
        url: https://neon.com/docs/data-api/get-started
  - aid: neon:serverless-driver
    name: Neon Serverless Driver
    description: 'The Neon Serverless Driver is a low-latency JavaScript and TypeScript driver that enables querying Neon Postgres databases from serverless and edge environments over HTTP or WebSockets in place of TCP. It supports two query modes: HTTP mode using the neon function for fast single non-interactive transactions, and WebSocket mode using Pool and Client constructors for session and transaction support with node-postgres compatibility. The driver is available as @neondatabase/serverless on npm and is optimized for deployment on platforms like Cloudflare Workers, Vercel Edge Functions, and AWS Lambda.'
    humanURL: https://neon.com/docs/serverless/serverless-driver
    tags:
      - Databases
      - Serverless
      - Postgres
      - JavaScript
      - TypeScript
      - WebSocket
      - Edge
      - Driver
    properties:
      - type: Documentation
        url: https://neon.com/docs/serverless/serverless-driver
  - aid: neon:auth
    name: Neon Auth
    description: Neon Auth is a managed authentication service built on Better Auth that connects directly to a Neon Postgres database. It stores authentication data including users, sessions, and OAuth configurations in the database's neon_auth schema. Neon Auth provides client and server SDKs, supports multiple OAuth providers, and integrates with the Neon Data API for automatic JWT validation. It enables Row-Level Security policies through the auth.uid() function, allowing developers to implement fine-grained data access control based on authenticated users.
    humanURL: https://neon.com/docs/auth/overview
    tags:
      - Authentication
      - Authorization
      - OAuth
      - JWT
      - Security
      - Identity
    properties:
      - type: Documentation
        url: https://neon.com/docs/auth/overview
      - type: Documentation
        url: https://neon.com/docs/neon-auth/api
      - type: AsyncAPI
        url: asyncapi/neon-auth-webhooks-asyncapi.yml
common:
  - type: Portal
    url: https://neon.com/docs
  - type: Blog
    url: https://neon.com/blog
  - type: Pricing
    url: https://neon.com/pricing
  - type: Login
    url: https://console.neon.tech
  - type: Sign Up
    url: https://console.neon.tech/signup
  - type: Support
    url: https://neon.com/docs/introduction/support
  - type: Status
    url: https://neonstatus.com
  - type: TermsOfService
    url: https://neon.com/terms-of-service
  - type: PrivacyPolicy
    url: https://neon.com/privacy-policy
  - type: Website
    url: https://neon.com
  - type: Features
    data:
      - 'Free: 100 CU-hours/project, 0.5 GB storage, 60K MAU'
      - 'Launch: $0.106/CU-hour, $0.35/GB-month, up to 16 CU autoscale'
      - 'Scale: $0.222/CU-hour, up to 56 CU fixed, HIPAA/SOC 2'
      - Postgres-compatible (latest versions supported)
      - Branching for safe schema changes
      - Bottomless storage (S3-backed)
      - Compute autoscale to zero
      - Read replicas
      - pgvector for embeddings
      - Neon Auth (Stack Auth integration)
      - 'Management API: 700 req/hour/org'
      - Connection pooling built-in (PgBouncer)
      - Time travel (restore to any point in window)
      - Private networking (VPC peering) on Scale
      - IP allow rules on Scale
      - Acquired by Databricks (Q4 2025)
    sources:
      - https://neon.com/pricing
    updated: '2026-05-04'
maintainers:
  - FN: API Evangelist
    email: info@apievangelist.com
---
