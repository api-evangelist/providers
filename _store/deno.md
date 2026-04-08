---
aid: deno
url: https://raw.githubusercontent.com/api-evangelist/deno/refs/heads/main/apis.yml
apis:
- aid: deno:runtime-api
  name: Deno Runtime API
  tags:
  - JavaScript
  - Runtime
  - TypeScript
  - WebAssembly
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.example.com
  humanURL: https://docs.deno.com/api/deno/
  properties:
  - url: https://docs.deno.com/api/deno/
    type: Documentation
  - url: json-schema/deno-deployment-schema.json
    type: JSONSchema
  description: The Deno Runtime API is the built-in namespace of globals and modules available to all programs running on the Deno JavaScript and TypeScript runtime. It provides access to filesystem operations, networking, process management, cryptography, subprocesses, permissions, and environment variables via the Deno.* namespace. The runtime natively supports TypeScript without additional tooling and implements Web Platform APIs such as fetch, WebSocket, URL, and Web Crypto.
- aid: deno:kv-api
  name: Deno KV API
  tags:
  - Database
  - Edge
  - Key-Value
  - Storage
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.deno.com
  humanURL: https://docs.deno.com/deploy/kv/
  properties:
  - url: https://docs.deno.com/deploy/kv/
    type: Documentation
  - url: https://docs.deno.com/api/deno/~/Deno.Kv
    type: Documentation
  - url: json-schema/deno-kv-database-schema.json
    type: JSONSchema
  description: Deno KV is a key-value database built directly into the Deno runtime and available as a globally distributed store on Deno Deploy. It is accessed via the Deno.Kv namespace and supports get, set, delete, list, and atomic transaction operations. Keys are ordered tuples that support hierarchical data modeling, and values can be any structured-serializable JavaScript value including the special Deno.KvU64 type for 64-bit unsigned integers.
- aid: deno:deploy-rest-api
  name: Deno Deploy REST API
  tags:
  - Deployment
  - Edge
  - Management
  - Serverless
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.deno.com/v1
  humanURL: https://docs.deno.com/deploy/api/rest/
  properties:
  - url: https://docs.deno.com/deploy/api/rest/
    type: Documentation
  - url: https://apidocs.deno.com/
    type: Documentation
  - url: openapi/deno-deploy-rest-api-openapi.yml
    type: OpenAPI
  description: The Deno Deploy REST API provides programmatic access to manage projects and deployments on the Deno Deploy serverless edge platform. It exposes endpoints for creating and managing organizations, projects, deployments, domains, and KV databases, as well as retrieving analytics and usage metrics. The API base URL is https://api.deno.com/v1 and uses HTTP Bearer token authentication. An OpenAPI specification is published and can be used with OpenAPI-compatible tooling.
- aid: deno:deploy-v2-api
  name: Deno Deploy API V2
  tags:
  - Deployment
  - Edge
  - Management
  - Serverless
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.deno.com/v2
  humanURL: https://api.deno.com/v2/docs
  properties:
  - url: https://api.deno.com/v2/docs
    type: Documentation
  - url: openapi/deno-deploy-v2-api-openapi.yml
    type: OpenAPI
  description: 'The Deno Deploy API v2 is the current generation REST API for managing applications, revisions, layers, and configuration on the Deno Deploy serverless edge platform. It replaces the v1 API (sunsetting July 20, 2026) with a revised resource model: Apps replace Projects, Revisions replace Deployments, and Layers provide reusable shared configuration across many apps.'
- aid: deno:subhosting-api
  name: Deno Subhosting API
  tags:
  - Deployment
  - Multi-Tenant
  - Serverless
  - Subhosting
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.deno.com/v1
  humanURL: https://docs.deno.com/subhosting/api/
  properties:
  - url: https://docs.deno.com/subhosting/api/
    type: Documentation
  - url: https://docs.deno.com/subhosting/manual/
    type: Documentation
  - url: openapi/deno-subhosting-api-openapi.yml
    type: OpenAPI
  description: The Deno Subhosting API enables platforms and SaaS products to run untrusted, user-submitted JavaScript and TypeScript code securely on Deno Deploy infrastructure. It shares the same base URL (https://api.deno.com/v1) and Bearer token authentication as the Deploy REST API but is scoped to subhosting use cases such as provisioning isolated projects per tenant, creating deployments, and managing custom domains and KV databases on behalf of end users.
- aid: deno:standard-library
  name: Deno Standard Library
  tags:
  - Modules
  - Standard Library
  - TypeScript
  - Utilities
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.example.com
  humanURL: https://docs.deno.com/runtime/fundamentals/standard_library/
  properties:
  - url: https://docs.deno.com/runtime/fundamentals/standard_library/
    type: Documentation
  - url: https://jsr.io/@std
    type: Documentation
  description: The Deno Standard Library is a collection of audited TypeScript modules maintained by the Deno core team and published on JSR under the @std scope. It provides common utilities including HTTP server helpers, path manipulation, assertions, CSV and JSON parsing, hashing, encoding, streams, date formatting, and more. All modules are guaranteed to work with the current stable Deno release and do not rely on third-party dependencies.
name: Deno
tags:
- API
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: A guide to Deno's built-in runtime APIs. Learn about file system operations, network functionality, permissions management, and other core capabilities available through the global Deno namespace.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

