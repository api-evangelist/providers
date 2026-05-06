---
aid: qdrant
name: Qdrant
description: Qdrant is a vector similarity search engine that provides a production-ready service with a convenient API to store, search, and manage points (i.e. vectors) with an additional payload. You can think of the payloads as additional pieces of information that can help you hone in on your search and also receive useful information that you can give to your users.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - AI
  - Artificial Intelligence
  - Vector Databases
url: https://raw.githubusercontent.com/api-evangelist/qdrant/refs/heads/main/apis.yml
created: '2024-06-18'
modified: '2026-05-04'
specificationVersion: '0.19'
apis:
  - aid: qdrant:qdrant-api
    name: Qdrant API
    tags:
      - AI
      - Artificial Intelligence
      - Vector Databases
    humanURL: https://qdrant.tech/documentation/
    properties:
      - url: https://qdrant.tech/documentation/
        type: Documentation
      - url: openapi/qdrant-openapi-original.json
        type: OpenAPI
    description: 'Qdrant (read: quadrant) is a vector similarity search engine. Use our documentation to develop a production-ready service with a convenient API to store, search, and manage vectors with an additional payload. Qdrant''s expanding features allow for all sorts of neural network or semantic-based matching, faceted search, and other applications.'
common:
  - url: https://qdrant.tech/documentation/quick-start/
    type: GettingStarted
  - url: https://qdrant.tech/documentation/concepts/
    type: Documentation
  - url: https://qdrant.tech/documentation/tutorials/
    type: Tutorials
  - url: https://qdrant.tech/pricing/
    type: Pricing
  - url: https://qdrant.tech/blog/
    type: Blog
  - url: https://qdrant.tech
    type: Website
  - type: Features
    data:
      - 'Free Tier: single-node 0.5 vCPU / 1 GB RAM / 4 GB disk'
      - 'Standard: usage-based dedicated resources, 99.5% SLA'
      - 'Premium: SSO, private VPC, 99.9% SLA'
      - 'Hybrid Cloud: runs on your infra, managed via Qdrant Cloud'
      - 'Private Cloud: dedicated isolated deployment'
      - REST and gRPC APIs
      - Throughput scales with cluster resources
      - Batch upsert up to 10,000 points/request
      - Sparse vectors and hybrid search
      - Quantization (scalar, binary, product)
      - Snapshot backup / restore
      - Multi-tenancy via collections + payload filtering
      - Distributed deployment with sharding
      - Web UI for collection management
      - Cloud Inference for embeddings (selected models free)
      - Open-source self-hosted alternative
    sources:
      - https://qdrant.tech/pricing/
    updated: '2026-05-04'
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
