---
aid: apache-couchdb
name: Apache CouchDB
description: Apache CouchDB is an open-source distributed document-oriented NoSQL database governed by the Apache Software Foundation. It uses JSON for data storage, a RESTful HTTP/JSON API for all database operations, and the Couch Replication Protocol for multi-primary synchronization across servers, mobile devices, and browsers. CouchDB supports Mango queries, MapReduce views, and offline-first application architectures.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Apache
  - Database
  - Document Store
  - JSON
  - NoSQL
  - Open Source
  - Replication
  - REST
created: '2026-03-16'
modified: '2026-04-19'
url: https://raw.githubusercontent.com/api-evangelist/apache-couchdb/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: apache-couchdb:apache-couchdb-http-api
    name: Apache CouchDB HTTP API
    description: CouchDB exposes a complete RESTful HTTP/JSON API covering server and database management, document CRUD operations, bulk operations, design documents with MapReduce views, Mango (declarative JSON) query API, replication, changes feeds, authentication, and cluster administration.
    humanURL: https://docs.couchdb.org/en/stable/api/index.html
    tags:
      - Cluster
      - Database
      - Document
      - HTTP
      - JSON
      - Mango
      - NoSQL
      - Replication
      - REST
      - Views
    properties:
      - type: Documentation
        url: https://docs.couchdb.org/en/stable/api/index.html
      - type: GettingStarted
        url: https://docs.couchdb.org/en/stable/intro/index.html
      - type: APIReference
        url: https://docs.couchdb.org/en/stable/api/
      - type: GitHubRepository
        url: https://github.com/apache/couchdb
      - type: SDK
        url: https://www.npmjs.com/package/nano
        title: Node.js SDK (Nano)
      - type: SDK
        url: https://pypi.org/project/couchdb/
        title: Python SDK
      - type: SDK
        url: https://pypi.org/project/aiocouch/
        title: Python Async SDK (aiocouch)
      - type: Tools
        url: https://github.com/apache/couchdb-fauxton
        title: Fauxton Web UI
      - type: Tools
        url: https://github.com/apache/couchdb-docker
        title: Docker Images
      - type: Tools
        url: https://github.com/apache/couchdb-helm
        title: Helm Chart
      - type: SDK
        url: https://github.com/apache/pouchdb
        title: PouchDB (Browser/Mobile Sync)
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/apache-couchdb/refs/heads/main/openapi/apache-couchdb-http-api-openapi.yaml
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/apache-couchdb/refs/heads/main/json-schema/apache-couchdb-all-docs-response-schema.json
        title: All Docs Response
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/apache-couchdb/refs/heads/main/json-schema/apache-couchdb-bulk-docs-request-schema.json
        title: Bulk Docs Request
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/apache-couchdb/refs/heads/main/json-schema/apache-couchdb-change-row-schema.json
        title: Change Row
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/apache-couchdb/refs/heads/main/json-schema/apache-couchdb-changes-response-schema.json
        title: Changes Response
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/apache-couchdb/refs/heads/main/json-schema/apache-couchdb-cluster-setup-response-schema.json
        title: Cluster Setup Response
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/apache-couchdb/refs/heads/main/json-schema/apache-couchdb-create-index-request-schema.json
        title: Create Index Request
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/apache-couchdb/refs/heads/main/json-schema/apache-couchdb-create-index-response-schema.json
        title: Create Index Response
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/apache-couchdb/refs/heads/main/json-schema/apache-couchdb-database-info-schema.json
        title: Database Info
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/apache-couchdb/refs/heads/main/json-schema/apache-couchdb-doc-row-schema.json
        title: Doc Row
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/apache-couchdb/refs/heads/main/json-schema/apache-couchdb-document-input-schema.json
        title: Document Input
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/apache-couchdb/refs/heads/main/json-schema/apache-couchdb-document-schema.json
        title: Document
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/apache-couchdb/refs/heads/main/json-schema/apache-couchdb-error-response-schema.json
        title: Error Response
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/apache-couchdb/refs/heads/main/json-schema/apache-couchdb-find-request-schema.json
        title: Find Request
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/apache-couchdb/refs/heads/main/json-schema/apache-couchdb-find-response-schema.json
        title: Find Response
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/apache-couchdb/refs/heads/main/json-schema/apache-couchdb-indexes-response-schema.json
        title: Indexes Response
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/apache-couchdb/refs/heads/main/json-schema/apache-couchdb-keys-request-schema.json
        title: Keys Request
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/apache-couchdb/refs/heads/main/json-schema/apache-couchdb-ok-response-schema.json
        title: Ok Response
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/apache-couchdb/refs/heads/main/json-schema/apache-couchdb-replication-request-schema.json
        title: Replication Request
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/apache-couchdb/refs/heads/main/json-schema/apache-couchdb-replication-response-schema.json
        title: Replication Response
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/apache-couchdb/refs/heads/main/json-schema/apache-couchdb-server-info-schema.json
        title: Server Info
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/apache-couchdb/refs/heads/main/json-schema/apache-couchdb-session-info-schema.json
        title: Session Info
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/apache-couchdb/refs/heads/main/json-schema/apache-couchdb-session-request-schema.json
        title: Session Request
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/apache-couchdb/refs/heads/main/json-schema/apache-couchdb-view-response-schema.json
        title: View Response
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/apache-couchdb/refs/heads/main/json-schema/apache-couchdb-write-response-schema.json
        title: Write Response
      - type: JSONStructure
        url: https://raw.githubusercontent.com/api-evangelist/apache-couchdb/refs/heads/main/json-structure/apache-couchdb-all-docs-response-structure.json
      - type: JSONStructure
        url: https://raw.githubusercontent.com/api-evangelist/apache-couchdb/refs/heads/main/json-structure/apache-couchdb-bulk-docs-request-structure.json
      - type: JSONStructure
        url: https://raw.githubusercontent.com/api-evangelist/apache-couchdb/refs/heads/main/json-structure/apache-couchdb-change-row-structure.json
      - type: JSONStructure
        url: https://raw.githubusercontent.com/api-evangelist/apache-couchdb/refs/heads/main/json-structure/apache-couchdb-changes-response-structure.json
      - type: JSONStructure
        url: https://raw.githubusercontent.com/api-evangelist/apache-couchdb/refs/heads/main/json-structure/apache-couchdb-cluster-setup-response-structure.json
      - type: JSONStructure
        url: https://raw.githubusercontent.com/api-evangelist/apache-couchdb/refs/heads/main/json-structure/apache-couchdb-create-index-request-structure.json
      - type: JSONStructure
        url: https://raw.githubusercontent.com/api-evangelist/apache-couchdb/refs/heads/main/json-structure/apache-couchdb-create-index-response-structure.json
      - type: JSONStructure
        url: https://raw.githubusercontent.com/api-evangelist/apache-couchdb/refs/heads/main/json-structure/apache-couchdb-database-info-structure.json
      - type: JSONStructure
        url: https://raw.githubusercontent.com/api-evangelist/apache-couchdb/refs/heads/main/json-structure/apache-couchdb-doc-row-structure.json
      - type: JSONStructure
        url: https://raw.githubusercontent.com/api-evangelist/apache-couchdb/refs/heads/main/json-structure/apache-couchdb-document-input-structure.json
      - type: JSONStructure
        url: https://raw.githubusercontent.com/api-evangelist/apache-couchdb/refs/heads/main/json-structure/apache-couchdb-document-structure.json
      - type: JSONStructure
        url: https://raw.githubusercontent.com/api-evangelist/apache-couchdb/refs/heads/main/json-structure/apache-couchdb-error-response-structure.json
      - type: JSONStructure
        url: https://raw.githubusercontent.com/api-evangelist/apache-couchdb/refs/heads/main/json-structure/apache-couchdb-find-request-structure.json
      - type: JSONStructure
        url: https://raw.githubusercontent.com/api-evangelist/apache-couchdb/refs/heads/main/json-structure/apache-couchdb-find-response-structure.json
      - type: JSONStructure
        url: https://raw.githubusercontent.com/api-evangelist/apache-couchdb/refs/heads/main/json-structure/apache-couchdb-indexes-response-structure.json
      - type: JSONStructure
        url: https://raw.githubusercontent.com/api-evangelist/apache-couchdb/refs/heads/main/json-structure/apache-couchdb-keys-request-structure.json
      - type: JSONStructure
        url: https://raw.githubusercontent.com/api-evangelist/apache-couchdb/refs/heads/main/json-structure/apache-couchdb-ok-response-structure.json
      - type: JSONStructure
        url: https://raw.githubusercontent.com/api-evangelist/apache-couchdb/refs/heads/main/json-structure/apache-couchdb-replication-request-structure.json
      - type: JSONStructure
        url: https://raw.githubusercontent.com/api-evangelist/apache-couchdb/refs/heads/main/json-structure/apache-couchdb-replication-response-structure.json
      - type: JSONStructure
        url: https://raw.githubusercontent.com/api-evangelist/apache-couchdb/refs/heads/main/json-structure/apache-couchdb-server-info-structure.json
      - type: JSONStructure
        url: https://raw.githubusercontent.com/api-evangelist/apache-couchdb/refs/heads/main/json-structure/apache-couchdb-session-info-structure.json
      - type: JSONStructure
        url: https://raw.githubusercontent.com/api-evangelist/apache-couchdb/refs/heads/main/json-structure/apache-couchdb-session-request-structure.json
      - type: JSONStructure
        url: https://raw.githubusercontent.com/api-evangelist/apache-couchdb/refs/heads/main/json-structure/apache-couchdb-view-response-structure.json
      - type: JSONStructure
        url: https://raw.githubusercontent.com/api-evangelist/apache-couchdb/refs/heads/main/json-structure/apache-couchdb-write-response-structure.json
      - type: JSONLD
        url: https://raw.githubusercontent.com/api-evangelist/apache-couchdb/refs/heads/main/json-ld/apache-couchdb-http-api-context.jsonld
      - type: Example
        url: https://raw.githubusercontent.com/api-evangelist/apache-couchdb/refs/heads/main/examples/apache-couchdb-all-docs-response-example.json
      - type: Example
        url: https://raw.githubusercontent.com/api-evangelist/apache-couchdb/refs/heads/main/examples/apache-couchdb-bulk-docs-request-example.json
      - type: Example
        url: https://raw.githubusercontent.com/api-evangelist/apache-couchdb/refs/heads/main/examples/apache-couchdb-change-row-example.json
      - type: Example
        url: https://raw.githubusercontent.com/api-evangelist/apache-couchdb/refs/heads/main/examples/apache-couchdb-changes-response-example.json
      - type: Example
        url: https://raw.githubusercontent.com/api-evangelist/apache-couchdb/refs/heads/main/examples/apache-couchdb-cluster-setup-response-example.json
      - type: Example
        url: https://raw.githubusercontent.com/api-evangelist/apache-couchdb/refs/heads/main/examples/apache-couchdb-create-index-request-example.json
      - type: Example
        url: https://raw.githubusercontent.com/api-evangelist/apache-couchdb/refs/heads/main/examples/apache-couchdb-create-index-response-example.json
      - type: Example
        url: https://raw.githubusercontent.com/api-evangelist/apache-couchdb/refs/heads/main/examples/apache-couchdb-database-info-example.json
      - type: Example
        url: https://raw.githubusercontent.com/api-evangelist/apache-couchdb/refs/heads/main/examples/apache-couchdb-doc-row-example.json
      - type: Example
        url: https://raw.githubusercontent.com/api-evangelist/apache-couchdb/refs/heads/main/examples/apache-couchdb-document-example.json
      - type: Example
        url: https://raw.githubusercontent.com/api-evangelist/apache-couchdb/refs/heads/main/examples/apache-couchdb-document-input-example.json
      - type: Example
        url: https://raw.githubusercontent.com/api-evangelist/apache-couchdb/refs/heads/main/examples/apache-couchdb-error-response-example.json
      - type: Example
        url: https://raw.githubusercontent.com/api-evangelist/apache-couchdb/refs/heads/main/examples/apache-couchdb-find-request-example.json
      - type: Example
        url: https://raw.githubusercontent.com/api-evangelist/apache-couchdb/refs/heads/main/examples/apache-couchdb-find-response-example.json
      - type: Example
        url: https://raw.githubusercontent.com/api-evangelist/apache-couchdb/refs/heads/main/examples/apache-couchdb-indexes-response-example.json
      - type: Example
        url: https://raw.githubusercontent.com/api-evangelist/apache-couchdb/refs/heads/main/examples/apache-couchdb-keys-request-example.json
      - type: Example
        url: https://raw.githubusercontent.com/api-evangelist/apache-couchdb/refs/heads/main/examples/apache-couchdb-ok-response-example.json
      - type: Example
        url: https://raw.githubusercontent.com/api-evangelist/apache-couchdb/refs/heads/main/examples/apache-couchdb-replication-request-example.json
      - type: Example
        url: https://raw.githubusercontent.com/api-evangelist/apache-couchdb/refs/heads/main/examples/apache-couchdb-replication-response-example.json
      - type: Example
        url: https://raw.githubusercontent.com/api-evangelist/apache-couchdb/refs/heads/main/examples/apache-couchdb-server-info-example.json
      - type: Example
        url: https://raw.githubusercontent.com/api-evangelist/apache-couchdb/refs/heads/main/examples/apache-couchdb-session-info-example.json
      - type: Example
        url: https://raw.githubusercontent.com/api-evangelist/apache-couchdb/refs/heads/main/examples/apache-couchdb-session-request-example.json
      - type: Example
        url: https://raw.githubusercontent.com/api-evangelist/apache-couchdb/refs/heads/main/examples/apache-couchdb-view-response-example.json
      - type: Example
        url: https://raw.githubusercontent.com/api-evangelist/apache-couchdb/refs/heads/main/examples/apache-couchdb-write-response-example.json
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
common:
  - type: Portal
    url: https://couchdb.apache.org/
  - type: Documentation
    url: https://docs.couchdb.org/en/stable/
  - type: GettingStarted
    url: https://docs.couchdb.org/en/stable/intro/
  - type: Blog
    url: https://blog.couchdb.org/
  - type: ReleaseNotes
    url: https://docs.couchdb.org/en/stable/whatsnew/
  - type: Support
    url: https://couchdb.apache.org/#mailing-list
  - type: GitHubOrganization
    url: https://github.com/apache
  - type: StackOverflow
    url: https://stackoverflow.com/questions/tagged/couchdb
  - type: Features
    data:
      - name: RESTful HTTP/JSON API
        description: All database operations are performed via a clean HTTP API using JSON, making it accessible from any HTTP-capable client.
      - name: Multi-Primary Replication
        description: The Couch Replication Protocol enables seamless bidirectional synchronization across servers, mobile, and browser environments.
      - name: Offline-First Architecture
        description: Applications can operate fully offline and sync changes when connectivity is restored, enabled by conflict-aware replication.
      - name: Mango Query Language
        description: Declarative JSON-based query language for ad-hoc document queries with index support, similar to MongoDB query syntax.
      - name: MapReduce Views
        description: Persistent, incrementally updated secondary indexes defined via JavaScript MapReduce functions stored as design documents.
      - name: Changes Feed
        description: Real-time notification feed of all database changes, supporting long-polling, continuous, and event-source modes.
      - name: Cluster Support
        description: Built-in clustering with consistent hashing for horizontal scaling and high availability across multiple nodes.
      - name: MVCC and ACID
        description: Multi-Version Concurrency Control ensures non-blocking reads; document updates are ACID-compliant at the document level.
  - type: UseCases
    data:
      - name: Mobile Sync Applications
        description: Sync data between a CouchDB server and PouchDB in mobile/browser apps, supporting offline-first user experiences.
      - name: Content Management
        description: Store and retrieve rich JSON documents for CMS, blogs, catalogs, and document management systems.
      - name: IoT Data Collection
        description: Edge devices write data locally to CouchDB and replicate to central servers when connected.
      - name: Multi-Region Replication
        description: Replicate database contents across geographic regions for low-latency reads and disaster recovery.
      - name: User Data Storage
        description: Per-user database pattern for storing isolated user data with built-in CouchDB authentication.
      - name: Event Sourcing
        description: Use the changes feed as an event stream for event-driven architectures and audit logging.
  - type: Integrations
    data:
      - name: PouchDB
        description: Browser and Node.js database that syncs with CouchDB via the Couch Replication Protocol.
      - name: IBM Cloudant
        description: IBM Cloudant is a fully managed cloud database service based on Apache CouchDB, API-compatible.
      - name: Docker
        description: Official CouchDB Docker images for container-based deployments.
      - name: Kubernetes / Helm
        description: Official Helm chart for deploying CouchDB clusters on Kubernetes.
      - name: Apache Kafka
        description: CouchDB changes feed can be consumed and bridged to Kafka for event streaming pipelines.
      - name: Nginx / Load Balancers
        description: CouchDB clusters are typically fronted by Nginx or HAProxy for SSL termination and load balancing.
  - type: SpectralRules
    url: https://raw.githubusercontent.com/api-evangelist/apache-couchdb/refs/heads/main/rules/apache-couchdb-spectral-rules.yml
  - type: NaftikoCapability
    url: https://raw.githubusercontent.com/api-evangelist/apache-couchdb/refs/heads/main/capabilities/couchdb-document-management.yaml
    title: CouchDB Document Management
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/apache-couchdb/refs/heads/main/vocabulary/apache-couchdb-vocabulary.yaml
---
