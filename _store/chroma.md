---
aid: chroma
url: https://raw.githubusercontent.com/api-evangelist/chroma/refs/heads/main/apis.yml
apis:
- aid: chroma:server-api
  name: Chroma Server API
  tags:
  - AI
  - Embeddings
  - Machine Learning
  - Search
  - Vector Database
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.trychroma.com
  humanURL: https://docs.trychroma.com/reference/chroma-reference
  properties:
  - url: https://docs.trychroma.com/reference/chroma-reference
    type: Documentation
  - type: OpenAPI
    url: openapi/chroma-server-api-openapi.yml
  description: The Chroma Server API is a REST API that provides access to the Chroma open-source vector database. It enables developers to create and manage collections of embeddings, add documents with automatic tokenization and embedding, and perform vector similarity searches. The API supports metadata filtering, full-text search, and collection management operations. An OpenAPI specification is available at the server endpoint for client generation in various programming languages.
- aid: chroma:cloud-api
  name: Chroma Cloud API
  tags:
  - AI
  - Cloud
  - Embeddings
  - Serverless
  - Vector Database
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.trychroma.com
  humanURL: https://docs.trychroma.com/cloud/pricing
  properties:
  - url: https://docs.trychroma.com/cloud/sync/overview
    type: Documentation
  - type: OpenAPI
    url: openapi/chroma-cloud-api-openapi.yml
  description: Chroma Cloud is a managed, serverless vector database service that provides fast and scalable vector, full-text, and metadata search across terabytes of data. It is backed by Chroma's Apache 2.0 distributed database and offers usage-based pricing with starter and team plans. Developers can connect to Chroma Cloud using the Python or JavaScript client SDKs without needing to manage infrastructure.
- aid: chroma:python-client
  name: Chroma Python Client
  tags:
  - Embeddings
  - Python
  - SDK
  - Vector Database
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.example.com
  humanURL: https://docs.trychroma.com/reference/python/client
  properties:
  - url: https://docs.trychroma.com/reference/python/client
    type: Documentation
  description: The Chroma Python Client is a first-party SDK for interacting with both self-hosted Chroma servers and Chroma Cloud. It provides a simple, developer-friendly interface with a core API of just four functions for managing collections, adding documents, and querying embeddings. The client handles automatic tokenization, embedding, and indexing of documents, making it straightforward to build AI applications that require vector similarity search.
- aid: chroma:javascript-client
  name: Chroma JavaScript Client
  tags:
  - Embeddings
  - JavaScript
  - SDK
  - TypeScript
  - Vector Database
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.example.com
  humanURL: https://docs.trychroma.com/reference/js/client
  properties:
  - url: https://docs.trychroma.com/reference/js/client
    type: Documentation
  description: The Chroma JavaScript and TypeScript Client is a first-party SDK for interacting with Chroma from JavaScript or TypeScript applications. The v3 rewrite focused on reducing bundle size and improving developer experience, making it well-suited for deployment on serverless platforms like Vercel. It supports both self-hosted Chroma instances and Chroma Cloud via the CloudClient class, providing collection management, document ingestion, and vector similarity search capabilities.
name: Chroma
tags:
- API
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Chroma is an open-source AI-native embedding database designed to make it easy to build LLM applications by providing storage, retrieval, and management for vector embeddings.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

