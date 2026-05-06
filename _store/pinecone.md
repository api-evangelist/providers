---
aid: pinecone
name: Pinecone
description: With its vector database at the core, Pinecone is the leading knowledge platform for building accurate, secure, and scalable AI applications. The Pinecone APIs cover Database (vector storage and search), Inference (embeddings and reranking), Assistant (RAG over documents), and Admin (organization and project management).
type: Contract
position: Consumer
access: 3rd-Party
image: https://kinlane-productions2.s3.amazonaws.com/apis-json-icons/introduction-pinecone-docs.png
tags:
  - Vector Databases
  - AI
  - Embeddings
  - RAG
created: '2024-07-02'
modified: '2026-05-04'
url: https://raw.githubusercontent.com/api-evangelist/pinecone/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: pinecone:pinecone-database-control
    name: Pinecone Database Control API
    description: Use the Database Control API to manage indexes, collections, and backups in Pinecone Database. The control plane handles lifecycle and configuration of vector storage resources.
    humanURL: https://docs.pinecone.io/reference/api/introduction
    baseURL: https://api.pinecone.io
    tags:
      - Vector Databases
      - Indexes
      - Control Plane
    properties:
      - type: Documentation
        url: https://docs.pinecone.io/reference/api/introduction
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/pinecone/refs/heads/main/openapi/pinecone-db-control-openapi.yaml
  - aid: pinecone:pinecone-database-data
    name: Pinecone Database Data API
    description: Use the Database Data API to upsert, query, fetch, update, and delete vector records in Pinecone indexes. The data plane is the high-throughput interface for real-time vector search.
    humanURL: https://docs.pinecone.io/reference/api/introduction
    baseURL: https://{index_host}
    tags:
      - Vector Databases
      - Vectors
      - Data Plane
    properties:
      - type: Documentation
        url: https://docs.pinecone.io/reference/api/introduction
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/pinecone/refs/heads/main/openapi/pinecone-db-data-openapi.yaml
  - aid: pinecone:pinecone-inference
    name: Pinecone Inference API
    description: Use the Inference API to generate vector embeddings and rerank results using models hosted on Pinecone's infrastructure.
    humanURL: https://docs.pinecone.io/reference/api/introduction#inference-api
    baseURL: https://api.pinecone.io
    tags:
      - Embeddings
      - Reranking
      - AI
    properties:
      - type: Documentation
        url: https://docs.pinecone.io/reference/api/introduction#inference-api
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/pinecone/refs/heads/main/openapi/pinecone-inference-openapi.yaml
  - aid: pinecone:pinecone-assistant-control
    name: Pinecone Assistant Control API
    description: Use the Assistant Control API to create and manage Pinecone Assistants for retrieval-augmented generation (RAG) over your documents.
    humanURL: https://docs.pinecone.io/reference/api/introduction#assistant-api
    baseURL: https://api.pinecone.io
    tags:
      - Assistants
      - RAG
      - Control Plane
    properties:
      - type: Documentation
        url: https://docs.pinecone.io/reference/api/introduction#assistant-api
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/pinecone/refs/heads/main/openapi/pinecone-assistant-control-openapi.yaml
  - aid: pinecone:pinecone-assistant-data
    name: Pinecone Assistant Data API
    description: Use the Assistant Data API to upload documents to a Pinecone Assistant, ask questions, and receive responses grounded in those documents.
    humanURL: https://docs.pinecone.io/reference/api/introduction#assistant-api
    baseURL: https://prod-1-data.ke.pinecone.io
    tags:
      - Assistants
      - RAG
      - Data Plane
    properties:
      - type: Documentation
        url: https://docs.pinecone.io/reference/api/introduction#assistant-api
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/pinecone/refs/heads/main/openapi/pinecone-assistant-data-openapi.yaml
  - aid: pinecone:pinecone-admin
    name: Pinecone Admin API
    description: Use the Admin API to manage Pinecone organizations, projects, API keys, and service accounts at the platform level.
    humanURL: https://docs.pinecone.io/reference/api/introduction
    baseURL: https://api.pinecone.io
    tags:
      - Admin
      - Organizations
      - Projects
    properties:
      - type: Documentation
        url: https://docs.pinecone.io/reference/api/introduction
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/pinecone/refs/heads/main/openapi/pinecone-admin-openapi.yaml
common:
  - type: Website
    url: https://www.pinecone.io/
  - type: Pricing
    url: https://www.pinecone.io/pricing/
  - type: Blog
    url: https://www.pinecone.io/blog/
  - type: Newsroom
    url: https://www.pinecone.io/newsroom/news/
  - type: Documentation
    url: https://docs.pinecone.io/guides/get-started/overview
  - type: GettingStarted
    url: https://docs.pinecone.io/guides/get-started/overview
  - type: Features
    url: https://docs.pinecone.io/guides/get-started/key-features
    data:
      - 'Starter free: 2 GB, 2M writes, 1M reads'
      - 'Builder at $20/mo flat: 10 GB, 5M writes, 2M reads'
      - 'Standard $50/mo min: $0.33/GB, $4-$4.50/M writes, $16-$18/M reads'
      - 'Enterprise $500/mo min: $6-$6.75/M writes, $24-$27/M reads, 99.95% SLA'
      - Serverless indexes (auto-scaling)
      - Pod-based (legacy) for reserved capacity
      - REST and gRPC APIs
      - OpenAPI spec available
      - Hybrid search (dense + sparse vectors)
      - Namespaces for multi-tenancy
      - Bulk import from S3/GCS/Azure
      - Up to 1,000 vectors per upsert request
      - Dedicated Read Nodes for QPS isolation
      - Backup/restore on Standard+
      - SAML SSO and audit logs (Enterprise)
      - Inference API for embeddings + reranking
    sources:
      - https://www.pinecone.io/pricing/
    updated: '2026-05-04'
  - type: Glossary
    url: https://docs.pinecone.io/guides/get-started/glossary
  - type: Examples
    url: https://docs.pinecone.io/examples/notebooks
  - type: Integrations
    url: https://docs.pinecone.io/integrations/overview
  - type: ChangeLog
    url: https://docs.pinecone.io/release-notes/2024
  - type: Status
    url: https://status.pinecone.io/
  - type: Login
    url: https://app.pinecone.io
  - type: Security
    url: https://www.pinecone.io/security/
  - type: TermsOfService
    url: https://www.pinecone.io/legal/
  - type: PrivacyPolicy
    url: https://www.pinecone.io/privacy/
  - type: SDKs
    url: https://docs.pinecone.io/reference/pinecone-sdks
  - type: Repository
    url: https://github.com/pinecone-io/pinecone-api
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
