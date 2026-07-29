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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 117
  human_in_the_loop: 9
  name: Couchbase Agentic Access
  operation_count: 219
  slug: couchbase-agentic-access
  summary_line: 219 operations · 117 acting · 9 human-in-the-loop
api_count: 54
apis:
- description: Endpoints for managing allowed IP addresses and CIDR ranges for cluster access.
  name: Couchbase Allowed CIDRs API
  slug: couchbase-allowed-cidrs-api
- description: Endpoints for administering and monitoring the Analytics service.
  name: Couchbase Analytics Admin API
  slug: couchbase-analytics-admin-api
- description: Endpoints for configuring Analytics nodes and clusters.
  name: Couchbase Analytics Configuration API
  slug: couchbase-analytics-configuration-api
- description: Endpoints for managing JavaScript libraries used for user-defined functions.
  name: Couchbase Analytics Library API
  slug: couchbase-analytics-library-api
- description: Endpoints for executing SQL++ analytics queries and retrieving results.
  name: Couchbase Analytics Query API
  slug: couchbase-analytics-query-api
- description: Endpoints for configuring Analytics service settings.
  name: Couchbase Analytics Settings API
  slug: couchbase-analytics-settings-api
- description: Endpoints for managing API keys used to authenticate with the Management API.
  name: Couchbase API Keys API
  slug: couchbase-api-keys-api
- description: Endpoints for user authentication and session management.
  name: Couchbase Authentication API
  slug: couchbase-authentication-api
- description: Endpoints for managing buckets within Capella clusters.
  name: Couchbase Buckets API
  slug: couchbase-buckets-api
- description: Endpoints for monitoring document changes and subscribing to change feeds.
  name: Couchbase Changes API
  slug: couchbase-changes-api
- description: Endpoints for managing cluster-level backup configuration.
  name: Couchbase Cluster API
  slug: couchbase-cluster-api
- description: Endpoints for managing remote cluster references used as XDCR targets.
  name: Couchbase Cluster References API
  slug: couchbase-cluster-references-api
- description: Endpoints for provisioning, managing, and scaling Capella database clusters.
  name: Couchbase Clusters API
  slug: couchbase-clusters-api
- description: Endpoints for managing auto-compaction settings and triggering compaction operations.
  name: Couchbase Compaction API
  slug: couchbase-compaction-api
- description: Endpoints for configuring Eventing Service settings.
  name: Couchbase Configuration API
  slug: couchbase-configuration-api
- description: Endpoints for triggering backup and restore data operations.
  name: Couchbase Data API
  slug: couchbase-data-api
- description: Endpoints for managing database configurations within App Services.
  name: Couchbase Database Administration API
  slug: couchbase-database-administration-api
- description: Endpoints for retrieving database information.
  name: Couchbase Database API
  slug: couchbase-database-api
- description: Endpoints for managing database access credentials for clusters.
  name: Couchbase Database Credentials API
  slug: couchbase-database-credentials-api
- description: Endpoints for creating, configuring, and managing databases.
  name: Couchbase Database Management API
  slug: couchbase-database-management-api
- description: Endpoints for creating, reading, updating, and deleting documents.
  name: Couchbase Documents API
  slug: couchbase-documents-api
- description: Endpoints for creating, retrieving, updating, and deleting Eventing Functions.
  name: Couchbase Functions API
  slug: couchbase-functions-api
- description: Endpoints for importing and exporting Eventing Function definitions.
  name: Couchbase Import Export API
  slug: couchbase-import-export-api
- description: Endpoints for managing the Global Secondary Index service.
  name: Couchbase Index Service API
  slug: couchbase-index-service-api
- description: Endpoints for deploying, undeploying, pausing, and resuming Eventing Functions.
  name: Couchbase Lifecycle API
  slug: couchbase-lifecycle-api
- description: Endpoints for managing local documents used by replication checkpoints.
  name: Couchbase Local Documents API
  slug: couchbase-local-documents-api
- description: Endpoints for retrieving Eventing Function application logs.
  name: Couchbase Logging API
  slug: couchbase-logging-api
- description: Endpoints for collecting and managing diagnostic logs.
  name: Couchbase Logs API
  slug: couchbase-logs-api
- description: Endpoints for monitoring App Services health and performance.
  name: Couchbase Monitoring API
  slug: couchbase-monitoring-api
- description: Endpoints for managing individual server nodes, including adding nodes, failover, recovery, and rebalance operations.
  name: Couchbase Nodes API
  slug: couchbase-nodes-api
- description: Endpoints for managing Capella organizations.
  name: Couchbase Organizations API
  slug: couchbase-organizations-api
- description: Endpoints for managing backup plans that define backup schedules and data retention policies.
  name: Couchbase Plans API
  slug: couchbase-plans-api
- description: Endpoints for creating, listing, updating, and deleting projects within an organization.
  name: Couchbase Projects API
  slug: couchbase-projects-api
- description: Endpoints for administrative operations on the Query service including monitoring active requests, completed requests, and prepared statements.
  name: Couchbase Query Admin API
  slug: couchbase-query-admin-api
- description: Endpoints for executing SQL++ queries and managing query results.
  name: Couchbase Query Execution API
  slug: couchbase-query-execution-api
- description: Endpoints for configuring Query service settings at the node and cluster level.
  name: Couchbase Query Settings API
  slug: couchbase-query-settings-api
- description: Endpoints for managing inter-Sync Gateway replications.
  name: Couchbase Replication API
  slug: couchbase-replication-api
- description: Endpoints for configuring replication-level and global XDCR settings.
  name: Couchbase Replication Settings API
  slug: couchbase-replication-settings-api
- description: Endpoints for monitoring replication progress and performance statistics.
  name: Couchbase Replication Statistics API
  slug: couchbase-replication-statistics-api
- description: Endpoints for creating, managing, and deleting XDCR replication streams.
  name: Couchbase Replications API
  slug: couchbase-replications-api
- description: Endpoints for creating, managing, and querying backup repositories.
  name: Couchbase Repositories API
  slug: couchbase-repositories-api
- description: Endpoints for managing roles and their channel assignments.
  name: Couchbase Role Management API
  slug: couchbase-role-management-api
- description: Endpoints for managing scopes and collections within Capella buckets.
  name: Couchbase Scopes and Collections API
  slug: couchbase-scopes-and-collections-api
- description: Endpoints for creating, retrieving, updating, and deleting Full Text Search index definitions.
  name: Couchbase Search Indexes API
  slug: couchbase-search-indexes-api
- description: Endpoints for monitoring search index statistics and service status.
  name: Couchbase Search Monitoring API
  slug: couchbase-search-monitoring-api
- description: Endpoints for executing full-text search queries against search indexes.
  name: Couchbase Search Queries API
  slug: couchbase-search-queries-api
- description: Endpoints for managing security settings, users, roles, certificates, and audit configurations.
  name: Couchbase Security API
  slug: couchbase-security-api
- description: Endpoints for managing the Sync Gateway server instance.
  name: Couchbase Server API
  slug: couchbase-server-api
- description: Endpoints for managing server groups for rack-zone awareness.
  name: Couchbase Server Groups API
  slug: couchbase-server-groups-api
- description: Endpoints for managing server-wide settings and configuration parameters.
  name: Couchbase Settings API
  slug: couchbase-settings-api
- description: Endpoints for monitoring Eventing Function execution statistics and status.
  name: Couchbase Statistics API
  slug: couchbase-statistics-api
- description: Endpoints for monitoring and managing backup and restore tasks.
  name: Couchbase Tasks API
  slug: couchbase-tasks-api
- description: Endpoints for managing users and their access permissions.
  name: Couchbase User Management API
  slug: couchbase-user-management-api
- description: Endpoints for managing users within a Capella organization.
  name: Couchbase Users API
  slug: couchbase-users-api
artifact_total: 174
collections:
- collection_type: open
  name: Couchbase Analytics Service REST API
  slug: open-couchbase-analytics-service-rest-api
- collection_type: open
  name: Couchbase Backup Service REST API
  slug: open-couchbase-backup-service-rest-api
- collection_type: open
  name: Couchbase Capella App Services Admin API
  slug: open-couchbase-capella-app-services-admin-api
- collection_type: open
  name: Couchbase Capella App Services Public API
  slug: open-couchbase-capella-app-services-public-api
- collection_type: open
  name: Couchbase Capella Management API
  slug: open-couchbase-capella-management-api
- collection_type: open
  name: Couchbase Eventing Service REST API
  slug: open-couchbase-eventing-service-rest-api
- collection_type: open
  name: Couchbase Query Service REST API
  slug: open-couchbase-query-service-rest-api
- collection_type: open
  name: Couchbase Search Service REST API
  slug: open-couchbase-search-service-rest-api
- collection_type: open
  name: Couchbase Server REST API
  slug: open-couchbase-server-rest-api
- collection_type: open
  name: Couchbase Sync Gateway Admin REST API
  slug: open-couchbase-sync-gateway-admin-rest-api
- collection_type: open
  name: Couchbase Sync Gateway Public REST API
  slug: open-couchbase-sync-gateway-public-rest-api
- collection_type: open
  name: Couchbase XDCR REST API
  slug: open-couchbase-xdcr-rest-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/couchbase-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/couchbase-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/couchbase-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/couchbase
- group: company
  title: ''
  type: Website
  url: https://www.couchbase.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.couchbase.com/
- group: other
  title: ''
  type: Capella
  url: https://www.couchbase.com/products/capella/
- group: other
  title: ''
  type: Server
  url: https://www.couchbase.com/products/server/
- group: other
  title: ''
  type: Mobile
  url: https://www.couchbase.com/products/mobile/
- group: start
  title: ''
  type: Login
  url: https://cloud.couchbase.com/sign-in
- group: commercial
  title: ''
  type: Pricing
  url: https://www.couchbase.com/pricing/
- group: company
  title: ''
  type: Blog
  url: https://www.couchbase.com/blog/
- group: operate
  title: ''
  type: Forums
  url: https://www.couchbase.com/forums/
- group: operate
  title: ''
  type: Support
  url: https://support.couchbase.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.couchbase.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/couchbase
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.couchbase.com/server/current/release-notes/relnotes.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.couchbase.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.couchbase.com/terms-of-use/
- group: design
  title: ''
  type: JSONLD
  url: json-ld/couchbase-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/couchbase-document-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/couchbase-bucket-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/couchbase-cluster-schema.json
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/couchbase-vocabulary.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.couchbase.com/llms.txt
created: '2025-03-01'
description: Couchbase is a distributed, document-oriented NoSQL cloud database platform that combines the flexibility of JSON, the power of SQL++ querying, and the performance of an in-memory key-value store. The Couchbase product line includes Couchbase Server (self-managed), Couchbase Capella (fully managed database-as-a-service across AWS, Azure, and Google Cloud), Sync Gateway and App Services for mobile and edge synchronization, and Couchbase Lite embedded databases. Couchbase exposes a comprehensive set of REST APIs covering cluster administration, SQL++ query execution, full-text and vector search, analytics, eventing, backup, cross data center replication, and Capella management.
features:
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
finops:
- name: Couchbase Finops
  service_category: NoSQL DBaaS
  slug: couchbase-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/couchbase.png
json_schemas:
- name: ActiveRequest
  property_count: 8
  slug: couchbase-activerequest
- name: AllDocsResponse
  property_count: 3
  slug: couchbase-alldocsresponse
- name: AllowedCIDR
  property_count: 6
  slug: couchbase-allowedcidr
- name: AllowedCIDRCreateRequest
  property_count: 3
  slug: couchbase-allowedcidrcreaterequest
- name: AnalyticsClusterStatus
  property_count: 2
  slug: couchbase-analyticsclusterstatus
- name: AnalyticsNodeConfig
  property_count: 3
  slug: couchbase-analyticsnodeconfig
- name: AnalyticsQueryRequest
  property_count: 7
  slug: couchbase-analyticsqueryrequest
- name: AnalyticsQueryResult
  property_count: 7
  slug: couchbase-analyticsqueryresult
- name: AnalyticsServiceConfig
  property_count: 9
  slug: couchbase-analyticsserviceconfig
- name: AnalyticsSettings
  property_count: 1
  slug: couchbase-analyticssettings
- name: ApiKeyCreateRequest
  property_count: 6
  slug: couchbase-apikeycreaterequest
- name: ApiKeyCreateResponse
  property_count: 2
  slug: couchbase-apikeycreateresponse
- name: AuditInfo
  property_count: 5
  slug: couchbase-auditinfo
- name: AutoCompactionSettings
  property_count: 3
  slug: couchbase-autocompactionsettings
- name: BackupClusterInfo
  property_count: 3
  slug: couchbase-backupclusterinfo
- name: BackupPlan
  property_count: 5
  slug: couchbase-backupplan
- name: BackupRepository
  property_count: 6
  slug: couchbase-backuprepository
- name: BackupRepositoryCreateRequest
  property_count: 3
  slug: couchbase-backuprepositorycreaterequest
- name: BackupTask
  property_count: 6
  slug: couchbase-backuptask
- name: Couchbase Bucket Configuration
  property_count: 13
  slug: couchbase-bucket
- name: BucketCreateRequest
  property_count: 7
  slug: couchbase-bucketcreaterequest
- name: BucketUpdateRequest
  property_count: 3
  slug: couchbase-bucketupdaterequest
- name: CapellaBucket
  property_count: 10
  slug: couchbase-capellabucket
- name: CapellaBucketCreateRequest
  property_count: 8
  slug: couchbase-capellabucketcreaterequest
- name: CapellaBucketUpdateRequest
  property_count: 5
  slug: couchbase-capellabucketupdaterequest
- name: CapellaScope
  property_count: 2
  slug: couchbase-capellascope
- name: ChangesResponse
  property_count: 3
  slug: couchbase-changesresponse
- name: Couchbase Cluster Configuration
  property_count: 7
  slug: couchbase-cluster
- name: ClusterCreateRequest
  property_count: 7
  slug: couchbase-clustercreaterequest
- name: ClusterUpdateRequest
  property_count: 4
  slug: couchbase-clusterupdaterequest
- name: CompletedRequest
  property_count: 8
  slug: couchbase-completedrequest
- name: DatabaseConfig
  property_count: 9
  slug: couchbase-databaseconfig
- name: DatabaseCredential
  property_count: 4
  slug: couchbase-databasecredential
- name: DatabaseCredentialCreateRequest
  property_count: 3
  slug: couchbase-databasecredentialcreaterequest
- name: DatabaseInfo
  property_count: 6
  slug: couchbase-databaseinfo
- name: Couchbase Document
  property_count: 6
  slug: couchbase-document
- name: DocumentResponse
  property_count: 3
  slug: couchbase-documentresponse
- name: DocumentWriteResponse
  property_count: 3
  slug: couchbase-documentwriteresponse
- name: EventingConfig
  property_count: 2
  slug: couchbase-eventingconfig
- name: EventingFunction
  property_count: 5
  slug: couchbase-eventingfunction
- name: EventingFunctionStats
  property_count: 3
  slug: couchbase-eventingfunctionstats
- name: EventingStatus
  property_count: 2
  slug: couchbase-eventingstatus
- name: IndexSettings
  property_count: 5
  slug: couchbase-indexsettings
- name: Node
  property_count: 8
  slug: couchbase-node
- name: NodesInfo
  property_count: 1
  slug: couchbase-nodesinfo
- name: Organization
  property_count: 5
  slug: couchbase-organization
- name: PaginatedResponse
  property_count: 2
  slug: couchbase-paginatedresponse
- name: PoolDetails
  property_count: 5
  slug: couchbase-pooldetails
- name: Pools
  property_count: 6
  slug: couchbase-pools
- name: PreparedStatement
  property_count: 4
  slug: couchbase-preparedstatement
- name: Project
  property_count: 4
  slug: couchbase-project
- name: ProjectCreateRequest
  property_count: 2
  slug: couchbase-projectcreaterequest
- name: QueryRequest
  property_count: 10
  slug: couchbase-queryrequest
- name: QueryResult
  property_count: 8
  slug: couchbase-queryresult
- name: QuerySettings
  property_count: 12
  slug: couchbase-querysettings
- name: QueryVitals
  property_count: 15
  slug: couchbase-queryvitals
- name: RemoteClusterCreateRequest
  property_count: 7
  slug: couchbase-remoteclustercreaterequest
- name: RemoteClusterReference
  property_count: 8
  slug: couchbase-remoteclusterreference
- name: ReplicationConfig
  property_count: 11
  slug: couchbase-replicationconfig
- name: ReplicationCreateRequest
  property_count: 7
  slug: couchbase-replicationcreaterequest
- name: ReplicationSettings
  property_count: 12
  slug: couchbase-replicationsettings
- name: RestoreRequest
  property_count: 8
  slug: couchbase-restorerequest
- name: Role
  property_count: 4
  slug: couchbase-role
- name: RoleConfig
  property_count: 2
  slug: couchbase-roleconfig
- name: RoleInfo
  property_count: 3
  slug: couchbase-roleinfo
- name: ScopesList
  property_count: 2
  slug: couchbase-scopeslist
- name: SearchIndexDefinition
  property_count: 8
  slug: couchbase-searchindexdefinition
- name: SearchIndexList
  property_count: 2
  slug: couchbase-searchindexlist
- name: SearchIndexResponse
  property_count: 2
  slug: couchbase-searchindexresponse
- name: SearchQueryRequest
  property_count: 9
  slug: couchbase-searchqueryrequest
- name: SearchQueryResult
  property_count: 6
  slug: couchbase-searchqueryresult
- name: ServerGroups
  property_count: 1
  slug: couchbase-servergroups
- name: ServerStatus
  property_count: 4
  slug: couchbase-serverstatus
- name: ServiceGroup
  property_count: 3
  slug: couchbase-servicegroup
- name: SessionResponse
  property_count: 3
  slug: couchbase-sessionresponse
- name: User
  property_count: 4
  slug: couchbase-user
- name: UserConfig
  property_count: 6
  slug: couchbase-userconfig
- name: UserInfo
  property_count: 7
  slug: couchbase-userinfo
json_structures:
- name: Couchbase Structure
  property_count: 0
  slug: couchbase-structure
jsonld:
- class_count: 0
  name: Couchbase Context
  property_count: 14
  slug: couchbase-context
layout: provider
modified: '2026-05-19'
name: Couchbase
nav: Providers
network: true
overview: 'Couchbase publishes 54 APIs on the [APIs.io](https://apis.io/) network, including Allowed CIDRs API, Analytics Admin API, Analytics Configuration API, and 51 more. Tagged areas include Analytics, App Services, Backup, Capella, and Cloud.


  The Couchbase catalog on APIs.io includes 1 JSON-LD context and 6 Spectral governance rulesets.


  Couchbase''s developer surface includes authentication, documentation, pricing, engineering blog, support, changelog, and 19 more developer resources.'
plans:
- name: Couchbase Plans Pricing
  plan_count: 4
  slug: couchbase-plans-pricing
random_paper: 72
rate_limits:
- limit_count: 3
  name: Couchbase Rate Limits
  slug: couchbase-rate-limits
rules:
- name: Couchbase API Rules
  rule_count: 5
  severity_counts:
    error: 3
    hint: 0
    info: 0
    warn: 2
  slug: couchbase-capella-management-rules
- name: Couchbase API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: couchbase-jsonschema-spectral-rules
- name: Couchbase API Rules
  rule_count: 4
  severity_counts:
    error: 3
    hint: 0
    info: 0
    warn: 1
  slug: couchbase-query-rules
- name: Couchbase API Rules
  rule_count: 4
  severity_counts:
    error: 3
    hint: 0
    info: 0
    warn: 1
  slug: couchbase-search-rules
- name: Couchbase API Rules
  rule_count: 5
  severity_counts:
    error: 4
    hint: 0
    info: 0
    warn: 1
  slug: couchbase-server-rules
- name: Couchbase API Rules
  rule_count: 4
  severity_counts:
    error: 3
    hint: 0
    info: 0
    warn: 1
  slug: couchbase-sync-gateway-rules
score:
  band: strong
  composite: 56.1
  delta: -3.7
  facets:
    commercial_clarity: 84.2
    contract_quality: 61.8
    developer_ergonomics: 26.1
    discoverability: 59.3
    governance: 31.3
    operational_transparency: 68.4
  previous_composite: 59.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 54
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/couchbase/refs/heads/main/screenshots/couchbase-2026-06-20T175100.png
security:
- kind: authentication
  name: Couchbase Authentication
  slug: couchbase-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Couchbase Domain Security
  slug: couchbase-domain-security
  summary_line: TLSv1.3 · DMARC
slug: couchbase
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
website: https://www.couchbase.com/
---
