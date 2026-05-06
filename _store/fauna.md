---
aid: fauna
url: https://raw.githubusercontent.com/api-evangelist/fauna/refs/heads/main/apis.yml
modified: '2026-04-28'
apis:
  - aid: fauna:core-http-api
    name: Fauna Core HTTP API
    tags:
      - Database
      - Document Database
      - NoSQL
      - Queries
      - Serverless
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://db.fauna.com
    humanURL: https://docs.fauna.com/fauna/current/reference/http/reference/core-api/
    properties:
      - url: https://docs.fauna.com/fauna/current/reference/http/reference/core-api/
        type: Documentation
      - url: openapi/fauna-core-http-api-openapi.yml
        type: OpenAPI
    description: The Fauna Core HTTP API provides direct access to the Fauna serverless document database through HTTPS endpoints. It allows developers to execute Fauna Query Language (FQL) queries, manage databases, and perform CRUD operations on documents. The API uses token-based authentication and supports features such as transactions, indexes, and set operations. It serves as the foundation upon which Fauna's client drivers and SDKs are built.
  - aid: fauna:event-streaming-api
    name: Fauna Event Streaming API
    tags:
      - Change Data Capture
      - Database
      - Events
      - Real-Time
      - Streaming
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://db.fauna.com
    humanURL: https://docs.fauna.com/fauna/current/reference/streaming/
    properties:
      - url: https://docs.fauna.com/fauna/current/reference/streaming/
        type: Documentation
      - url: asyncapi/fauna-event-streaming-asyncapi.yml
        type: AsyncAPI
    description: The Fauna Event Streaming API enables real-time change data capture by maintaining an open connection to the Fauna database and pushing events to clients as they occur. Developers can subscribe to document or set changes and receive add, remove, and update events in real time. The API supports reconnection with a start timestamp to avoid missing events during disconnections. It is accessible via the /stream/1 HTTP endpoint with token-based authentication.
  - aid: fauna:event-feeds-api
    name: Fauna Event Feeds API
    tags:
      - Change Data Capture
      - Database
      - Events
      - Polling
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://db.fauna.com
    humanURL: https://docs.fauna.com/fauna/current/learn/cdc/
    properties:
      - url: https://docs.fauna.com/fauna/current/learn/cdc/
        type: Documentation
    description: The Fauna Event Feeds API provides a polling-based approach to change data capture, complementing the real-time Event Streaming API. Event feeds allow developers to retrieve batches of change events at their own pace rather than maintaining a persistent connection. This is useful for scheduled synchronization tasks, batch processing workflows, and scenarios where a pull-based model is preferred over push-based streaming. Event feeds track the same add, remove, and update events as streams.
  - aid: fauna:graphql-api
    name: Fauna GraphQL API
    tags:
      - Database
      - GraphQL
      - Query Language
      - Serverless
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://graphql.fauna.com
    humanURL: https://docs.fauna.com/fauna/current/
    properties:
      - url: https://docs.fauna.com/fauna/current/
        type: Documentation
      - url: openapi/fauna-graphql-api-openapi.yml
        type: OpenAPI
    description: The Fauna GraphQL API allows developers to interact with their Fauna databases using standard GraphQL queries and mutations. By uploading a GraphQL schema, Fauna automatically generates the necessary collections, indexes, and resolvers. This API can be used from any programming language or HTTP client without requiring a dedicated Fauna driver. It provides an alternative to FQL for developers who prefer the GraphQL query paradigm and ecosystem tooling.
  - aid: fauna:javascript-driver
    name: Fauna JavaScript Driver
    tags:
      - Driver
      - JavaScript
      - Node.js
      - SDK
      - TypeScript
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://docs.fauna.com/fauna/current/
    properties:
      - url: https://docs.fauna.com/fauna/current/
        type: Documentation
    description: The Fauna JavaScript Driver is the official client SDK for interacting with Fauna from JavaScript and TypeScript applications. It provides template-based FQL query interpolation with type safety and a secure wire protocol that prevents injection vulnerabilities. The driver supports both Node.js server environments and browser-based applications, and includes built-in support for event streaming with automatic reconnection handling.
  - aid: fauna:python-driver
    name: Fauna Python Driver
    tags:
      - Driver
      - Python
      - SDK
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://docs.fauna.com/fauna/current/
    properties:
      - url: https://docs.fauna.com/fauna/current/
        type: Documentation
    description: The Fauna Python Driver is the official client SDK for accessing Fauna from Python applications. It provides idiomatic Python interfaces for composing and executing FQL v10 queries, managing authentication tokens, and handling pagination. The driver includes support for event streaming and event feeds, allowing Python developers to build real-time and batch-oriented data processing pipelines against Fauna databases.
  - aid: fauna:dotnet-driver
    name: Fauna .NET Driver
    tags:
      - .NET
      - C#
      - Driver
      - SDK
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://github.com/fauna/fauna-dotnet
    properties:
      - url: https://github.com/fauna/fauna-dotnet
        type: Documentation
    description: The Fauna .NET Driver is the official client SDK for interacting with Fauna from C# and .NET applications. It is designed for use with FQL v10 and provides strongly-typed query construction and response handling. The driver enables .NET developers to perform document operations, run queries, and manage database resources using familiar C# patterns and conventions.
common:
  - type: JSON-LD
    url: json-ld/fauna-context.jsonld
  - type: JSONSchema
    url: json-schema/fauna-document-schema.json
  - type: JSONSchema
    url: json-schema/fauna-event-schema.json
  - type: JSONSchema
    url: json-schema/fauna-query-schema.json
description: Fauna is a distributed document-relational database delivered as a cloud API that combines the relational query power of SQL with the flexibility of documents and global serverless distribution.
---
