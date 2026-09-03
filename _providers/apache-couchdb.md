---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 31.7
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 11
  human_in_the_loop: 0
  name: Apache Couchdb Agentic Access
  operation_count: 21
  slug: apache-couchdb-agentic-access
  summary_line: 21 operations · 11 acting
api_count: 9
apis:
- baseURL: http://localhost:5984
  baseurl_source: spec
  description: Session and authentication management
  name: Apache CouchDB Authentication API
  slug: apache-couchdb-authentication-api
- baseURL: http://localhost:5984
  baseurl_source: spec
  description: Database changes feed
  name: Apache CouchDB Changes API
  slug: apache-couchdb-changes-api
- baseURL: http://localhost:5984
  baseurl_source: spec
  description: Cluster membership and configuration
  name: Apache CouchDB Cluster API
  slug: apache-couchdb-cluster-api
- baseURL: http://localhost:5984
  baseurl_source: spec
  description: Database management operations
  name: Apache CouchDB Database API
  slug: apache-couchdb-database-api
- baseURL: http://localhost:5984
  baseurl_source: spec
  description: Design documents, views, and indexes
  name: Apache CouchDB Design Documents API
  slug: apache-couchdb-design-documents-api
- baseURL: http://localhost:5984
  baseurl_source: spec
  description: Document CRUD and bulk operations
  name: Apache CouchDB Documents API
  slug: apache-couchdb-documents-api
- baseURL: http://localhost:5984
  baseurl_source: spec
  description: Mango declarative JSON query API
  name: Apache CouchDB Mango API
  slug: apache-couchdb-mango-api
- baseURL: http://localhost:5984
  baseurl_source: spec
  description: Replication management
  name: Apache CouchDB Replication API
  slug: apache-couchdb-replication-api
- baseURL: http://localhost:5984
  baseurl_source: spec
  description: Server-level information and utilities
  name: Apache CouchDB Server API
  slug: apache-couchdb-server-api
artifact_total: 132
asyncapis:
- description: AsyncAPI 2.6 description of the Apache CouchDB database `_changes` feed. CouchDB exposes a per-database, append-only stream of document mutations at `GET /{db}/_changes` (and `POST /{db}/_changes` for
  name: Apache CouchDB _changes Feed
  slug: apache-couchdb-changes-feed-asyncapi
collections:
- collection_type: postman
  name: Apache CouchDB HTTP Authentication API
  slug: postman-apache-couchdb-authentication-api
- collection_type: postman
  name: Apache CouchDB HTTP Authentication Changes API
  slug: postman-apache-couchdb-changes-api
- collection_type: postman
  name: Apache CouchDB HTTP Authentication Cluster API
  slug: postman-apache-couchdb-cluster-api
- collection_type: postman
  name: Apache CouchDB HTTP Authentication Database API
  slug: postman-apache-couchdb-database-api
- collection_type: postman
  name: Apache CouchDB HTTP Authentication Design Documents API
  slug: postman-apache-couchdb-design-documents-api
- collection_type: postman
  name: Apache CouchDB HTTP Authentication Documents API
  slug: postman-apache-couchdb-documents-api
- collection_type: postman
  name: Apache CouchDB HTTP Authentication Mango API
  slug: postman-apache-couchdb-mango-api
- collection_type: postman
  name: Apache CouchDB HTTP Authentication Replication API
  slug: postman-apache-couchdb-replication-api
- collection_type: postman
  name: Apache CouchDB HTTP Authentication Server API
  slug: postman-apache-couchdb-server-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Apache CouchDB HTTP Authentication API
  slug: open-apache-couchdb-authentication-api
- collection_type: open
  name: Apache CouchDB HTTP Authentication Changes API
  slug: open-apache-couchdb-changes-api
- collection_type: open
  name: Apache CouchDB HTTP Authentication Cluster API
  slug: open-apache-couchdb-cluster-api
- collection_type: open
  name: Apache CouchDB HTTP Authentication Database API
  slug: open-apache-couchdb-database-api
- collection_type: open
  name: Apache CouchDB HTTP Authentication Design Documents API
  slug: open-apache-couchdb-design-documents-api
- collection_type: open
  name: Apache CouchDB HTTP Authentication Documents API
  slug: open-apache-couchdb-documents-api
- collection_type: open
  name: Apache CouchDB HTTP Authentication Mango API
  slug: open-apache-couchdb-mango-api
- collection_type: open
  name: Apache CouchDB HTTP Authentication Replication API
  slug: open-apache-couchdb-replication-api
- collection_type: open
  name: Apache CouchDB HTTP Authentication Server API
  slug: open-apache-couchdb-server-api
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/apache/couchdb/issues
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/apache/.github/blob/main/.github/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/apache/couchdb/blob/main/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/apache/couchdb/blob/main/LICENSE
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/apache-couchdb/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/apache-couchdb-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/apache-couchdb-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/apache-couchdb-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/apache-couchdb-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/apache-couchdb
- group: start
  title: ''
  type: Portal
  url: https://couchdb.apache.org/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.couchdb.org/en/stable/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.couchdb.org/en/stable/intro/
- group: company
  title: ''
  type: Blog
  url: https://blog.couchdb.org/
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://docs.couchdb.org/en/stable/whatsnew/
- group: operate
  title: ''
  type: Support
  url: https://couchdb.apache.org/#mailing-list
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/apache
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/couchdb
- group: design
  title: ''
  type: SpectralRules
  url: https://raw.githubusercontent.com/api-evangelist/apache-couchdb/refs/heads/main/rules/apache-couchdb-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/apache-couchdb/refs/heads/main/vocabulary/apache-couchdb-vocabulary.yaml
created: '2026-03-16'
description: Apache CouchDB is an open-source distributed document-oriented NoSQL database governed by the Apache Software Foundation. It uses JSON for data storage, a RESTful HTTP/JSON API for all database operations, and the Couch Replication Protocol for multi-primary synchronization across servers, mobile devices, and browsers. CouchDB supports Mango queries, MapReduce views, and offline-first application architectures.
examples:
- key_count: 3
  name: Apache Couchdb All Docs Response Example
  slug: apache-couchdb-all-docs-response-example
- key_count: 2
  name: Apache Couchdb Bulk Docs Request Example
  slug: apache-couchdb-bulk-docs-request-example
- key_count: 5
  name: Apache Couchdb Change Row Example
  slug: apache-couchdb-change-row-example
- key_count: 3
  name: Apache Couchdb Changes Response Example
  slug: apache-couchdb-changes-response-example
- key_count: 1
  name: Apache Couchdb Cluster Setup Response Example
  slug: apache-couchdb-cluster-setup-response-example
- key_count: 4
  name: Apache Couchdb Create Index Request Example
  slug: apache-couchdb-create-index-request-example
- key_count: 3
  name: Apache Couchdb Create Index Response Example
  slug: apache-couchdb-create-index-response-example
- key_count: 5
  name: Apache Couchdb Database Info Example
  slug: apache-couchdb-database-info-example
- key_count: 4
  name: Apache Couchdb Doc Row Example
  slug: apache-couchdb-doc-row-example
- key_count: 3
  name: Apache Couchdb Document Example
  slug: apache-couchdb-document-example
- key_count: 2
  name: Apache Couchdb Document Input Example
  slug: apache-couchdb-document-input-example
- key_count: 2
  name: Apache Couchdb Error Response Example
  slug: apache-couchdb-error-response-example
- key_count: 6
  name: Apache Couchdb Find Request Example
  slug: apache-couchdb-find-request-example
- key_count: 3
  name: Apache Couchdb Find Response Example
  slug: apache-couchdb-find-response-example
- key_count: 2
  name: Apache Couchdb Indexes Response Example
  slug: apache-couchdb-indexes-response-example
- key_count: 1
  name: Apache Couchdb Keys Request Example
  slug: apache-couchdb-keys-request-example
- key_count: 3
  name: Apache Couchdb Ok Response Example
  slug: apache-couchdb-ok-response-example
- key_count: 6
  name: Apache Couchdb Replication Request Example
  slug: apache-couchdb-replication-request-example
- key_count: 4
  name: Apache Couchdb Replication Response Example
  slug: apache-couchdb-replication-response-example
- key_count: 5
  name: Apache Couchdb Server Info Example
  slug: apache-couchdb-server-info-example
- key_count: 3
  name: Apache Couchdb Session Info Example
  slug: apache-couchdb-session-info-example
- key_count: 2
  name: Apache Couchdb Session Request Example
  slug: apache-couchdb-session-request-example
- key_count: 3
  name: Apache Couchdb View Response Example
  slug: apache-couchdb-view-response-example
- key_count: 3
  name: Apache Couchdb Write Response Example
  slug: apache-couchdb-write-response-example
features:
- description: All database operations are performed via a clean HTTP API using JSON, making it accessible from any HTTP-capable client.
  name: RESTful HTTP/JSON API
- description: The Couch Replication Protocol enables seamless bidirectional synchronization across servers, mobile, and browser environments.
  name: Multi-Primary Replication
- description: Applications can operate fully offline and sync changes when connectivity is restored, enabled by conflict-aware replication.
  name: Offline-First Architecture
- description: Declarative JSON-based query language for ad-hoc document queries with index support, similar to MongoDB query syntax.
  name: Mango Query Language
- description: Persistent, incrementally updated secondary indexes defined via JavaScript MapReduce functions stored as design documents.
  name: MapReduce Views
- description: Real-time notification feed of all database changes, supporting long-polling, continuous, and event-source modes.
  name: Changes Feed
- description: Built-in clustering with consistent hashing for horizontal scaling and high availability across multiple nodes.
  name: Cluster Support
- description: Multi-Version Concurrency Control ensures non-blocking reads; document updates are ACID-compliant at the document level.
  name: MVCC and ACID
finops:
- name: Apache Couchdb Finops
  service_category: API
  slug: apache-couchdb-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/apache-couchdb.png
integrations:
- description: Browser and Node.js database that syncs with CouchDB via the Couch Replication Protocol.
  name: PouchDB
- description: IBM Cloudant is a fully managed cloud database service based on Apache CouchDB, API-compatible.
  name: IBM Cloudant
- description: Official CouchDB Docker images for container-based deployments.
  name: Docker
- description: Official Helm chart for deploying CouchDB clusters on Kubernetes.
  name: Kubernetes / Helm
- description: CouchDB changes feed can be consumed and bridged to Kafka for event streaming pipelines.
  name: Apache Kafka
- description: CouchDB clusters are typically fronted by Nginx or HAProxy for SSL termination and load balancing.
  name: Nginx / Load Balancers
json_schemas:
- name: AllDocsResponse
  property_count: 3
  slug: apache-couchdb-all-docs-response
- name: BulkDocsRequest
  property_count: 2
  slug: apache-couchdb-bulk-docs-request
- name: ChangeRow
  property_count: 5
  slug: apache-couchdb-change-row
- name: ChangesResponse
  property_count: 3
  slug: apache-couchdb-changes-response
- name: ClusterSetupResponse
  property_count: 1
  slug: apache-couchdb-cluster-setup-response
- name: CreateIndexRequest
  property_count: 4
  slug: apache-couchdb-create-index-request
- name: CreateIndexResponse
  property_count: 3
  slug: apache-couchdb-create-index-response
- name: DatabaseInfo
  property_count: 5
  slug: apache-couchdb-database-info
- name: DocRow
  property_count: 4
  slug: apache-couchdb-doc-row
- name: DocumentInput
  property_count: 2
  slug: apache-couchdb-document-input
- name: Document
  property_count: 3
  slug: apache-couchdb-document
- name: ErrorResponse
  property_count: 2
  slug: apache-couchdb-error-response
- name: FindRequest
  property_count: 6
  slug: apache-couchdb-find-request
- name: FindResponse
  property_count: 3
  slug: apache-couchdb-find-response
- name: IndexesResponse
  property_count: 2
  slug: apache-couchdb-indexes-response
- name: KeysRequest
  property_count: 1
  slug: apache-couchdb-keys-request
- name: OkResponse
  property_count: 3
  slug: apache-couchdb-ok-response
- name: ReplicationRequest
  property_count: 6
  slug: apache-couchdb-replication-request
- name: ReplicationResponse
  property_count: 4
  slug: apache-couchdb-replication-response
- name: ServerInfo
  property_count: 5
  slug: apache-couchdb-server-info
- name: SessionInfo
  property_count: 3
  slug: apache-couchdb-session-info
- name: SessionRequest
  property_count: 2
  slug: apache-couchdb-session-request
- name: ViewResponse
  property_count: 3
  slug: apache-couchdb-view-response
- name: WriteResponse
  property_count: 3
  slug: apache-couchdb-write-response
json_structures:
- name: Apache Couchdb All Docs Response Structure
  property_count: 3
  slug: apache-couchdb-all-docs-response-structure
- name: Apache Couchdb Bulk Docs Request Structure
  property_count: 2
  slug: apache-couchdb-bulk-docs-request-structure
- name: Apache Couchdb Change Row Structure
  property_count: 5
  slug: apache-couchdb-change-row-structure
- name: Apache Couchdb Changes Response Structure
  property_count: 3
  slug: apache-couchdb-changes-response-structure
- name: Apache Couchdb Cluster Setup Response Structure
  property_count: 1
  slug: apache-couchdb-cluster-setup-response-structure
- name: Apache Couchdb Create Index Request Structure
  property_count: 4
  slug: apache-couchdb-create-index-request-structure
- name: Apache Couchdb Create Index Response Structure
  property_count: 3
  slug: apache-couchdb-create-index-response-structure
- name: Apache Couchdb Database Info Structure
  property_count: 5
  slug: apache-couchdb-database-info-structure
- name: Apache Couchdb Doc Row Structure
  property_count: 4
  slug: apache-couchdb-doc-row-structure
- name: Apache Couchdb Document Input Structure
  property_count: 2
  slug: apache-couchdb-document-input-structure
- name: Apache Couchdb Document Structure
  property_count: 3
  slug: apache-couchdb-document-structure
- name: Apache Couchdb Error Response Structure
  property_count: 2
  slug: apache-couchdb-error-response-structure
- name: Apache Couchdb Find Request Structure
  property_count: 6
  slug: apache-couchdb-find-request-structure
- name: Apache Couchdb Find Response Structure
  property_count: 3
  slug: apache-couchdb-find-response-structure
- name: Apache Couchdb Indexes Response Structure
  property_count: 2
  slug: apache-couchdb-indexes-response-structure
- name: Apache Couchdb Keys Request Structure
  property_count: 1
  slug: apache-couchdb-keys-request-structure
- name: Apache Couchdb Ok Response Structure
  property_count: 3
  slug: apache-couchdb-ok-response-structure
- name: Apache Couchdb Replication Request Structure
  property_count: 6
  slug: apache-couchdb-replication-request-structure
- name: Apache Couchdb Replication Response Structure
  property_count: 4
  slug: apache-couchdb-replication-response-structure
- name: Apache Couchdb Server Info Structure
  property_count: 5
  slug: apache-couchdb-server-info-structure
- name: Apache Couchdb Session Info Structure
  property_count: 3
  slug: apache-couchdb-session-info-structure
- name: Apache Couchdb Session Request Structure
  property_count: 2
  slug: apache-couchdb-session-request-structure
- name: Apache Couchdb View Response Structure
  property_count: 3
  slug: apache-couchdb-view-response-structure
- name: Apache Couchdb Write Response Structure
  property_count: 3
  slug: apache-couchdb-write-response-structure
jsonld:
- class_count: 26
  name: Apache Couchdb Http Api Context
  property_count: 62
  slug: apache-couchdb-http-api-context
layout: provider
modified: '2026-05-29'
name: Apache CouchDB
nav: Providers
network: true
overview: 'Apache CouchDB publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Changes API, Cluster API, and 6 more. Tagged areas include Apache, Database, Document Store, JSON, and NoSQL.


  The Apache CouchDB catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 3 Spectral governance rulesets.


  Apache CouchDB''s developer surface includes authentication, developer portal, documentation, getting-started guide, engineering blog, release notes, support, and 13 more developer resources.'
plans:
- name: Apache Couchdb Plans Pricing
  plan_count: 3
  slug: apache-couchdb-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 5
  name: Apache Couchdb Rate Limits
  slug: apache-couchdb-rate-limits
rules:
- effective_rule_count: 36
  extends:
  - spectral:asyncapi
  name: Apache CouchDB API Rules
  rule_count: 9
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 7
  slug: apache-couchdb-asyncapi-spectral-rules
- effective_rule_count: 5
  extends: []
  name: Apache CouchDB API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: apache-couchdb-jsonschema-spectral-rules
- effective_rule_count: 74
  extends:
  - spectral:oas
  name: Apache CouchDB API Rules
  rule_count: 33
  severity_counts:
    error: 10
    hint: 0
    info: 2
    warn: 21
  slug: apache-couchdb-spectral-rules
score:
  band: thin
  composite: 39.0
  coverage:
    artifact_dirs: 18
    catalog_gap: 48.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 13.6
    contract_quality: 37.9
    developer_ergonomics: 76.2
    discoverability: 59.3
    governance: 13.6
    operational_transparency: 26.3
  open_source:
    applies: true
    score: 40.0
  previous_composite: 39.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 10
      marker_coverage: 100.0
      total: 10
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/apache-couchdb/refs/heads/main/screenshots/apache-couchdb-2026-06-20T172052.png
security:
- kind: authentication
  name: Apache Couchdb Authentication
  slug: apache-couchdb-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Apache Couchdb Domain Security
  slug: apache-couchdb-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Apache Couchdb Vulnerability Disclosure
  slug: apache-couchdb-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: apache-couchdb
tags:
- Apache
- Database
- Document Store
- JSON
- NoSQL
- Open-Source
- Replication
- REST
use_cases:
- description: Sync data between a CouchDB server and PouchDB in mobile/browser apps, supporting offline-first user experiences.
  name: Mobile Sync Applications
- description: Store and retrieve rich JSON documents for CMS, blogs, catalogs, and document management systems.
  name: Content Management
- description: Edge devices write data locally to CouchDB and replicate to central servers when connected.
  name: IoT Data Collection
- description: Replicate database contents across geographic regions for low-latency reads and disaster recovery.
  name: Multi-Region Replication
- description: Per-user database pattern for storing isolated user data with built-in CouchDB authentication.
  name: User Data Storage
- description: Use the changes feed as an event stream for event-driven architectures and audit logging.
  name: Event Sourcing
website: https://couchdb.apache.org/
---
