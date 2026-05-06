---
aid: microsoft-azure-cosmos-db
url: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-cosmos-db/refs/heads/main/apis.yml
apis:
  - aid: microsoft-azure-cosmos-db:azure-cosmos-db-api
    name: Azure Cosmos DB API
    tags:
      - NoSQL
      - Database
      - Global Distribution
      - Multi-Model
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://{account}.documents.azure.com/
    humanURL: https://learn.microsoft.com/en-us/rest/api/cosmos-db/
    properties:
      - url: https://learn.microsoft.com/en-us/rest/api/cosmos-db/
        type: Documentation
    description: The Azure Cosmos DB REST API provides data plane operations for documents, collections, databases, and stored procedures across multiple API models including NoSQL, MongoDB, Cassandra, Gremlin, and Table. The resource provider API enables account management, throughput configuration, and global distribution settings.
common:
  - type: Portal
    url: https://portal.azure.com/
  - type: Pricing
    url: https://azure.microsoft.com/en-us/pricing/
  - type: Documentation
    url: https://learn.microsoft.com/en-us/azure/
  - type: Terms of Service
    url: https://www.microsoft.com/en-us/legal/terms-of-use
  - type: Privacy Policy
    url: https://privacy.microsoft.com/en-us/privacystatement
  - type: Support
    url: https://support.microsoft.com/
modified: '2026-04-28'
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
description: Azure Cosmos DB is a globally distributed, multi-model database service offering guaranteed low latency, elastic scalability, and tunable consistency. This collection catalogs the REST APIs for data plane operations across NoSQL, MongoDB, Cassandra, Gremlin, and Table models alongside resource provider APIs for account and throughput management.
---
