---
aid: couchbase
name: Couchbase
x-type: company
description: Couchbase is a distributed, document-oriented NoSQL cloud database platform that combines the flexibility of JSON, the power of SQL++ querying, and the performance of an in-memory key-value store. The Couchbase product line includes Couchbase Server (self-managed), Couchbase Capella (fully managed database-as-a-service across AWS, Azure, and Google Cloud), Sync Gateway and App Services for mobile and edge synchronization, and Couchbase Lite embedded databases. Couchbase exposes a comprehensive set of REST APIs covering cluster administration, SQL++ query execution, full-text and vector search, analytics, eventing, backup, cross data center replication, and Capella management.
url: https://raw.githubusercontent.com/api-evangelist/couchbase/refs/heads/main/apis.yml
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
type: Index
access: Public
position: Provider
tags:
  - Analytics
  - App Services
  - Backup
  - Capella
  - Cloud
  - Database
  - DBaaS
  - Eventing
  - Full-Text Search
  - Gateway
  - JSON
  - Mobile
  - NoSQL
  - Replication
  - SQL++
  - Sync
  - Vector Search
  - XDCR
created: '2025-03-01'
modified: '2026-05-04'
specificationVersion: '0.20'
apis:
  - aid: couchbase:couchbase-server-rest-api
    name: Couchbase Server REST API
    description: The Couchbase Server REST API provides programmatic access to manage and configure Couchbase Server clusters. It includes endpoints for cluster management, bucket operations, node administration, security settings, and server configuration. The API enables automation of deployment, monitoring, and maintenance tasks for Couchbase Server instances across distributed environments.
    humanURL: https://docs.couchbase.com/server/current/rest-api/rest-intro.html
    baseURL: https://localhost:8091
    properties:
      - type: Documentation
        url: https://docs.couchbase.com/server/current/rest-api/rest-intro.html
      - type: OpenAPI
        url: openapi/couchbase-server-rest-api-openapi.yml
      - type: Rules
        url: rules/couchbase-server-rules.yml
      - type: Capabilities
        url: capabilities/couchbase-server-capabilities.yml
    tags:
      - Administration
      - Buckets
      - Clusters
      - Database
      - NoSQL
  - aid: couchbase:couchbase-query-service-rest-api
    name: Couchbase Query Service REST API
    description: The Couchbase Query Service REST API enables developers to execute SQL++ (formerly N1QL) queries against Couchbase Server and manage query service settings. It supports ad-hoc queries, prepared statements, and request-level parameter configuration. The API provides endpoints for query execution, monitoring active requests, and managing query service configuration across cluster nodes.
    humanURL: https://docs.couchbase.com/server/current/n1ql/n1ql-rest-api/index.html
    baseURL: https://localhost:8093
    properties:
      - type: Documentation
        url: https://docs.couchbase.com/server/current/n1ql/n1ql-rest-api/index.html
      - type: OpenAPI
        url: openapi/couchbase-query-service-rest-api-openapi.yml
      - type: Rules
        url: rules/couchbase-query-rules.yml
      - type: Capabilities
        url: capabilities/couchbase-query-capabilities.yml
    tags:
      - Database
      - N1QL
      - NoSQL
      - Query
      - SQL++
  - aid: couchbase:couchbase-analytics-service-rest-api
    name: Couchbase Analytics Service REST API
    description: The Couchbase Analytics Service REST API provides access to the Analytics service for running complex analytical queries on operational data without impacting performance of key-value operations. It supports SQL++ queries for analytics, management of links to external data sources, and configuration of user-defined libraries. The service enables real-time analytics on JSON data alongside transactional workloads.
    humanURL: https://docs.couchbase.com/server/current/analytics/rest-analytics.html
    baseURL: https://localhost:8095
    properties:
      - type: Documentation
        url: https://docs.couchbase.com/server/current/analytics/rest-analytics.html
      - type: OpenAPI
        url: openapi/couchbase-analytics-service-rest-api-openapi.yml
    tags:
      - Analytics
      - Database
      - NoSQL
      - SQL++
  - aid: couchbase:couchbase-search-service-rest-api
    name: Couchbase Search Service REST API
    description: The Couchbase Search Service REST API allows developers to create, manage, and query Full Text Indexes on Couchbase Server. It supports full-text search queries with features like fuzzy matching, faceted search, highlighting, and geospatial queries. The API provides endpoints for index definition, index management, and executing search queries across JSON documents stored in Couchbase buckets.
    humanURL: https://docs.couchbase.com/server/current/rest-api/rest-fts.html
    baseURL: https://localhost:8094
    properties:
      - type: Documentation
        url: https://docs.couchbase.com/server/current/rest-api/rest-fts.html
      - type: OpenAPI
        url: openapi/couchbase-search-service-rest-api-openapi.yml
      - type: Rules
        url: rules/couchbase-search-rules.yml
      - type: Capabilities
        url: capabilities/couchbase-search-capabilities.yml
    tags:
      - Database
      - Full-Text Search
      - Indexing
      - NoSQL
      - Vector Search
  - aid: couchbase:couchbase-eventing-service-rest-api
    name: Couchbase Eventing Service REST API
    description: The Couchbase Eventing Service REST API provides methods for deploying and managing Eventing Functions that respond to data changes in real time. Eventing Functions allow developers to write server-side JavaScript logic triggered by document mutations, timers, or external events.
    humanURL: https://docs.couchbase.com/server/current/eventing/eventing-api.html
    baseURL: https://localhost:8096
    properties:
      - type: Documentation
        url: https://docs.couchbase.com/server/current/eventing/eventing-api.html
      - type: OpenAPI
        url: openapi/couchbase-eventing-service-rest-api-openapi.yml
    tags:
      - Database
      - Eventing
      - NoSQL
      - Serverless Functions
  - aid: couchbase:couchbase-backup-service-rest-api
    name: Couchbase Backup Service REST API
    description: The Couchbase Backup Service REST API supports management of the Backup Service for Couchbase Server, providing endpoints for cluster configuration, repository management, backup plans, task scheduling, and data operations.
    humanURL: https://docs.couchbase.com/server/current/rest-api/backup-rest-api.html
    baseURL: https://localhost:8097
    properties:
      - type: Documentation
        url: https://docs.couchbase.com/server/current/rest-api/backup-rest-api.html
      - type: OpenAPI
        url: openapi/couchbase-backup-service-rest-api-openapi.yml
    tags:
      - Backup
      - Database
      - Disaster Recovery
      - NoSQL
  - aid: couchbase:couchbase-xdcr-rest-api
    name: Couchbase XDCR REST API
    description: The Couchbase XDCR (Cross Data Center Replication) REST API enables configuration and management of data replication between Couchbase clusters across different data centers. It provides endpoints for creating replication references, configuring replication streams, monitoring replication statistics, and managing replication settings.
    humanURL: https://docs.couchbase.com/server/current/rest-api/rest-xdcr-intro.html
    baseURL: https://localhost:8091
    properties:
      - type: Documentation
        url: https://docs.couchbase.com/server/current/rest-api/rest-xdcr-intro.html
      - type: OpenAPI
        url: openapi/couchbase-xdcr-rest-api-openapi.yml
    tags:
      - Cross Data Center
      - Database
      - NoSQL
      - Replication
  - aid: couchbase:couchbase-capella-management-api
    name: Couchbase Capella Management API
    description: The Couchbase Capella Management API is a REST API for provisioning, deploying, and configuring Couchbase Capella database-as-a-service deployments across AWS, Azure, and Google Cloud. It enables programmatic management of clusters, buckets, users, and organizations using API key authentication.
    humanURL: https://docs.couchbase.com/cloud/management-api-reference/index.html
    baseURL: https://cloudapi.cloud.couchbase.com
    properties:
      - type: Documentation
        url: https://docs.couchbase.com/cloud/management-api-reference/index.html
      - type: OpenAPI
        url: openapi/couchbase-capella-management-api-openapi.yml
      - type: Rules
        url: rules/couchbase-capella-management-rules.yml
      - type: Capabilities
        url: capabilities/couchbase-capella-management-capabilities.yml
    tags:
      - Capella
      - Cloud
      - Database
      - DBaaS
      - Management
      - NoSQL
  - aid: couchbase:couchbase-capella-app-services-public-api
    name: Couchbase Capella App Services Public API
    description: The Couchbase Capella App Services Public API provides REST endpoints for mobile and edge application data synchronization with Couchbase Capella. It enables developers to manage document access, handle user authentication, and synchronize data between mobile devices and the cloud database.
    humanURL: https://docs.couchbase.com/cloud/app-services/references/rest_api_public.html
    properties:
      - type: Documentation
        url: https://docs.couchbase.com/cloud/app-services/references/rest_api_public.html
      - type: OpenAPI
        url: openapi/couchbase-capella-app-services-public-api-openapi.yml
    tags:
      - App Services
      - Capella
      - Cloud
      - Mobile
      - NoSQL
      - Sync
  - aid: couchbase:couchbase-capella-app-services-admin-api
    name: Couchbase Capella App Services Admin API
    description: The Couchbase Capella App Services Admin API provides administrative REST endpoints for managing Sync Gateway configurations within Couchbase Capella. It enables administrators to manage databases, users, roles, sync functions, and replication settings for mobile data synchronization.
    humanURL: https://docs.couchbase.com/cloud/app-services/references/rest_api_admin.html
    properties:
      - type: Documentation
        url: https://docs.couchbase.com/cloud/app-services/references/rest_api_admin.html
      - type: OpenAPI
        url: openapi/couchbase-capella-app-services-admin-api-openapi.yml
    tags:
      - Administration
      - App Services
      - Capella
      - Cloud
      - Mobile
      - NoSQL
  - aid: couchbase:couchbase-sync-gateway-public-rest-api
    name: Couchbase Sync Gateway Public REST API
    description: The Couchbase Sync Gateway Public REST API provides endpoints for mobile and edge clients to synchronize data with Couchbase Server through the Sync Gateway middleware. It supports document CRUD operations, changes feeds for real-time data synchronization, and user authentication.
    humanURL: https://docs.couchbase.com/sync-gateway/current/rest-api.html
    baseURL: https://localhost:4984
    properties:
      - type: Documentation
        url: https://docs.couchbase.com/sync-gateway/current/rest-api.html
      - type: OpenAPI
        url: openapi/couchbase-sync-gateway-public-rest-api-openapi.yml
      - type: Rules
        url: rules/couchbase-sync-gateway-rules.yml
      - type: Capabilities
        url: capabilities/couchbase-sync-gateway-capabilities.yml
    tags:
      - Database
      - Gateway
      - Mobile
      - NoSQL
      - Sync
  - aid: couchbase:couchbase-sync-gateway-admin-rest-api
    name: Couchbase Sync Gateway Admin REST API
    description: The Couchbase Sync Gateway Admin REST API provides administrative endpoints for configuring and managing Sync Gateway instances. It supports database management, user and role administration, sync function configuration, and replication setup.
    humanURL: https://docs.couchbase.com/sync-gateway/current/rest-api-admin.html
    baseURL: https://localhost:4985
    properties:
      - type: Documentation
        url: https://docs.couchbase.com/sync-gateway/current/rest-api-admin.html
      - type: OpenAPI
        url: openapi/couchbase-sync-gateway-admin-rest-api-openapi.yml
    tags:
      - Administration
      - Database
      - Mobile
      - NoSQL
      - Sync
common:
  - type: Website
    url: https://www.couchbase.com/
  - type: Documentation
    url: https://docs.couchbase.com/
  - type: Capella
    url: https://www.couchbase.com/products/capella/
  - type: Server
    url: https://www.couchbase.com/products/server/
  - type: Mobile
    url: https://www.couchbase.com/products/mobile/
  - type: Login
    url: https://cloud.couchbase.com/sign-in
  - type: Pricing
    url: https://www.couchbase.com/pricing/
  - type: Blog
    url: https://www.couchbase.com/blog/
  - type: Forums
    url: https://www.couchbase.com/forums/
  - type: Support
    url: https://support.couchbase.com/
  - type: Status
    url: https://status.couchbase.com/
  - type: GitHubOrganization
    url: https://github.com/couchbase
  - type: ChangeLog
    url: https://docs.couchbase.com/server/current/release-notes/relnotes.html
  - type: PrivacyPolicy
    url: https://www.couchbase.com/privacy-policy/
  - type: TermsOfService
    url: https://www.couchbase.com/terms-of-use/
  - type: JSONLD
    url: json-ld/couchbase-context.jsonld
  - type: JSONSchema
    url: json-schema/couchbase-document-schema.json
  - type: JSONSchema
    url: json-schema/couchbase-bucket-schema.json
  - type: JSONSchema
    url: json-schema/couchbase-cluster-schema.json
  - type: Vocabulary
    url: vocabulary/couchbase-vocabulary.yml
  - type: Features
    data:
      - 'Free: 1 node, 8 GB capacity'
      - 'Basic from $0.15/hr/node: single AZ, 24h backup'
      - 'Developer Pro from $0.35/hr/node: multi-AZ 3 nodes, 99.99% SLA'
      - 'Enterprise from $0.49/hr/node: CMEK, 30-min response'
      - 'Backup: $0.06-$0.07/GB monthly'
      - Data transfer fees typically <10% of billing
      - SQL++ (N1QL) query language
      - Full-text search built-in
      - Mobile sync via Sync Gateway
      - 'Multi-cloud: AWS, GCP, Azure'
      - 'Management API: 600 req/min/org'
      - App Services for embedded apps
      - Eventing service for triggers
      - Analytics service for ad-hoc queries
      - Multi-document ACID transactions
      - Built-in caching (Memcached compatible)
    sources:
      - https://www.couchbase.com/pricing/
    updated: '2026-05-04'
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
