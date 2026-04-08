---
aid: couchbase
url: https://raw.githubusercontent.com/api-evangelist/couchbase/refs/heads/main/apis.yml
apis:
- aid: couchbase:server-rest-api
  name: Couchbase Server REST API
  tags:
  - Administration
  - Buckets
  - Clusters
  - Database
  - NoSQL
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://localhost:8091
  humanURL: https://docs.couchbase.com/server/current/rest-api/rest-intro.html
  properties:
  - url: https://docs.couchbase.com/server/current/rest-api/rest-intro.html
    type: Documentation
  - url: openapi/couchbase-server-rest-api-openapi.yml
    type: OpenAPI
  description: The Couchbase Server REST API provides programmatic access to manage and configure Couchbase Server clusters. It includes endpoints for cluster management, bucket operations, node administration, security settings, and server configuration. The API enables automation of deployment, monitoring, and maintenance tasks for Couchbase Server instances across distributed environments.
- aid: couchbase:query-service-rest-api
  name: Couchbase Query Service REST API
  tags:
  - Database
  - N1QL
  - NoSQL
  - Query
  - SQL++
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://localhost:8093
  humanURL: https://docs.couchbase.com/server/current/n1ql/n1ql-rest-api/index.html
  properties:
  - url: https://docs.couchbase.com/server/current/n1ql/n1ql-rest-api/index.html
    type: Documentation
  - url: openapi/couchbase-query-service-rest-api-openapi.yml
    type: OpenAPI
  description: The Couchbase Query Service REST API enables developers to execute SQL++ (formerly N1QL) queries against Couchbase Server and manage query service settings. It supports ad-hoc queries, prepared statements, and request-level parameter configuration. The API provides endpoints for query execution, monitoring active requests, and managing query service configuration across cluster nodes.
- aid: couchbase:analytics-service-rest-api
  name: Couchbase Analytics Service REST API
  tags:
  - Analytics
  - Database
  - NoSQL
  - SQL++
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://localhost:8095
  humanURL: https://docs.couchbase.com/server/current/analytics/rest-analytics.html
  properties:
  - url: https://docs.couchbase.com/server/current/analytics/rest-analytics.html
    type: Documentation
  - url: openapi/couchbase-analytics-service-rest-api-openapi.yml
    type: OpenAPI
  description: The Couchbase Analytics Service REST API provides access to the Analytics service for running complex analytical queries on operational data without impacting performance of key-value operations. It supports SQL++ queries for analytics, management of links to external data sources, and configuration of user-defined libraries. The service enables real-time analytics on JSON data alongside transactional workloads.
- aid: couchbase:search-service-rest-api
  name: Couchbase Search Service REST API
  tags:
  - Database
  - Full-Text Search
  - Indexing
  - NoSQL
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://localhost:8094
  humanURL: https://docs.couchbase.com/server/current/rest-api/rest-fts.html
  properties:
  - url: https://docs.couchbase.com/server/current/rest-api/rest-fts.html
    type: Documentation
  - url: openapi/couchbase-search-service-rest-api-openapi.yml
    type: OpenAPI
  description: The Couchbase Search Service REST API allows developers to create, manage, and query Full Text Indexes on Couchbase Server. It supports full-text search queries with features like fuzzy matching, faceted search, highlighting, and geospatial queries. The API provides endpoints for index definition, index management, and executing search queries across JSON documents stored in Couchbase buckets.
- aid: couchbase:eventing-service-rest-api
  name: Couchbase Eventing Service REST API
  tags:
  - Database
  - Eventing
  - NoSQL
  - Serverless Functions
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://localhost:8096
  humanURL: https://docs.couchbase.com/server/current/eventing/eventing-api.html
  properties:
  - url: https://docs.couchbase.com/server/current/eventing/eventing-api.html
    type: Documentation
  - url: openapi/couchbase-eventing-service-rest-api-openapi.yml
    type: OpenAPI
  description: The Couchbase Eventing Service REST API provides methods for deploying and managing Eventing Functions that respond to data changes in real time. Eventing Functions allow developers to write server-side JavaScript logic triggered by document mutations, timers, or external events. The API supports creating, deploying, pausing, and undeploying functions, as well as monitoring their execution status and statistics.
- aid: couchbase:backup-service-rest-api
  name: Couchbase Backup Service REST API
  tags:
  - Backup
  - Database
  - Disaster Recovery
  - NoSQL
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://localhost:8097
  humanURL: https://docs.couchbase.com/server/current/rest-api/backup-rest-api.html
  properties:
  - url: https://docs.couchbase.com/server/current/rest-api/backup-rest-api.html
    type: Documentation
  - url: openapi/couchbase-backup-service-rest-api-openapi.yml
    type: OpenAPI
  description: The Couchbase Backup Service REST API supports management of the Backup Service for Couchbase Server, providing endpoints for cluster configuration, repository management, backup plans, task scheduling, and data operations. It enables automated backup and restore workflows for Couchbase data, allowing administrators to define backup policies, monitor backup tasks, and manage backup repositories programmatically.
- aid: couchbase:xdcr-rest-api
  name: Couchbase XDCR REST API
  tags:
  - Cross Data Center
  - Database
  - NoSQL
  - Replication
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://localhost:8091
  humanURL: https://docs.couchbase.com/server/current/rest-api/rest-xdcr-intro.html
  properties:
  - url: https://docs.couchbase.com/server/current/rest-api/rest-xdcr-intro.html
    type: Documentation
  - url: openapi/couchbase-xdcr-rest-api-openapi.yml
    type: OpenAPI
  description: The Couchbase XDCR (Cross Data Center Replication) REST API enables configuration and management of data replication between Couchbase clusters across different data centers. It provides endpoints for creating replication references, configuring replication streams, monitoring replication statistics, and managing replication settings. XDCR supports both unidirectional and bidirectional replication for high availability and disaster recovery scenarios.
- aid: couchbase:capella-management-api
  name: Couchbase Capella Management API
  tags:
  - Cloud
  - Database
  - DBaaS
  - Management
  - NoSQL
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://cloudapi.cloud.couchbase.com
  humanURL: https://docs.couchbase.com/cloud/management-api-reference/index.html
  properties:
  - url: https://docs.couchbase.com/cloud/management-api-reference/index.html
    type: Documentation
  - url: openapi/couchbase-capella-management-api-openapi.yml
    type: OpenAPI
  description: The Couchbase Capella Management API is a REST API for provisioning, deploying, and configuring Couchbase Capella database-as-a-service deployments across AWS, Azure, and Google Cloud. It enables programmatic management of clusters, buckets, users, and organizations using API key authentication. The API supports automation of cloud database operations including scaling, configuration changes, and access management, with requests limited to 100 per minute per API key.
- aid: couchbase:capella-app-services-public-api
  name: Couchbase Capella App Services Public API
  tags:
  - Cloud
  - Database
  - Mobile
  - NoSQL
  - Sync
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.example.com
  humanURL: https://docs.couchbase.com/cloud/app-services/references/rest_api_public.html
  properties:
  - url: https://docs.couchbase.com/cloud/app-services/references/rest_api_public.html
    type: Documentation
  - url: openapi/couchbase-capella-app-services-public-api-openapi.yml
    type: OpenAPI
  description: The Couchbase Capella App Services Public API provides REST endpoints for mobile and edge application data synchronization with Couchbase Capella. It enables developers to manage document access, handle user authentication, and synchronize data between mobile devices and the cloud database. The API supports operations for reading and writing documents through Sync Gateway, managing changes feeds, and handling replication for offline-first mobile applications.
- aid: couchbase:capella-app-services-admin-api
  name: Couchbase Capella App Services Admin API
  tags:
  - Administration
  - Cloud
  - Database
  - Mobile
  - NoSQL
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.example.com
  humanURL: https://docs.couchbase.com/cloud/app-services/references/rest_api_admin.html
  properties:
  - url: https://docs.couchbase.com/cloud/app-services/references/rest_api_admin.html
    type: Documentation
  - url: openapi/couchbase-capella-app-services-admin-api-openapi.yml
    type: OpenAPI
  description: The Couchbase Capella App Services Admin API provides administrative REST endpoints for managing Sync Gateway configurations within Couchbase Capella. It enables administrators to manage databases, users, roles, sync functions, and replication settings for mobile data synchronization. The API supports full administrative control over App Services deployments, including user provisioning, access control, and monitoring of sync operations.
- aid: couchbase:sync-gateway-public-rest-api
  name: Couchbase Sync Gateway Public REST API
  tags:
  - Database
  - Gateway
  - Mobile
  - NoSQL
  - Sync
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://localhost:4984
  humanURL: https://docs.couchbase.com/sync-gateway/current/rest-api.html
  properties:
  - url: https://docs.couchbase.com/sync-gateway/current/rest-api.html
    type: Documentation
  - url: openapi/couchbase-sync-gateway-public-rest-api-openapi.yml
    type: OpenAPI
  description: The Couchbase Sync Gateway Public REST API provides endpoints for mobile and edge clients to synchronize data with Couchbase Server through the Sync Gateway middleware. It supports document CRUD operations, changes feeds for real-time data synchronization, and user authentication. The API enables offline-first mobile applications to replicate data bidirectionally between Couchbase Lite embedded databases and Couchbase Server clusters.
- aid: couchbase:sync-gateway-admin-rest-api
  name: Couchbase Sync Gateway Admin REST API
  tags:
  - Administration
  - Database
  - Mobile
  - NoSQL
  - Sync
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://localhost:4985
  humanURL: https://docs.couchbase.com/sync-gateway/current/rest-api-admin.html
  properties:
  - url: https://docs.couchbase.com/sync-gateway/current/rest-api-admin.html
    type: Documentation
  - url: openapi/couchbase-sync-gateway-admin-rest-api-openapi.yml
    type: OpenAPI
  description: The Couchbase Sync Gateway Admin REST API provides administrative endpoints for configuring and managing Sync Gateway instances. It supports database management, user and role administration, sync function configuration, and replication setup. The API is intended for server-side administration and is typically bound to localhost for security, enabling full control over Sync Gateway behavior, access control policies, and data synchronization rules.
name: Couchbase
tags:
- API
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: The REST API supports the management of Couchbase-Server clusters.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

