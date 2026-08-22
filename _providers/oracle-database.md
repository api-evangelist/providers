---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.3
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 70
  human_in_the_loop: 3
  name: Oracle Database Agentic Access
  operation_count: 156
  slug: oracle-database-agentic-access
  summary_line: 156 operations · 70 acting · 3 human-in-the-loop
api_count: 29
apis:
- description: MongoDB-compatible API for Oracle Database.
  name: Oracle Database API for MongoDB
  slug: oracle-database-api-for-mongodb
- description: Java Database Connectivity API for Oracle Database.
  name: Oracle Database JDBC
  slug: oracle-database-jdbc
- description: C/C++ API for Oracle Database access.
  name: Oracle Call Interface (OCI)
  slug: oracle-call-interface-oci
- description: RESTful services for Oracle SQL Developer.
  name: Oracle SQL Developer REST API
  slug: oracle-sql-developer-rest-api
- description: Kafka-compatible event streaming and message queuing built into Oracle Database.
  name: Oracle Transactional Event Queues (TxEventQ)
  slug: oracle-transactional-event-queues-txeventq
- description: Oracle APEX workspace and application management
  name: Oracle Database APEX API
  slug: oracle-database-apex-api
- description: Manage Oracle Autonomous Database instances
  name: Oracle Database Autonomous Databases API
  slug: oracle-database-autonomous-databases-api
- description: Manage database backups
  name: Oracle Database Backups API
  slug: oracle-database-backups-api
- description: Bulk insert, delete, and update operations
  name: Oracle Database Bulk Operations API
  slug: oracle-database-bulk-operations-api
- description: Collection management operations (create, list, delete)
  name: Oracle Database Collections API
  slug: oracle-database-collections-api
- description: Database tables, views, columns, indexes, and object metadata
  name: Oracle Database Data Dictionary API
  slug: oracle-database-data-dictionary-api
- description: Manage Data Guard associations for high availability
  name: Oracle Database Data Guard API
  slug: oracle-database-data-guard-api
- description: High-speed data and metadata export/import operations
  name: Oracle Database Data Pump API
  slug: oracle-database-data-pump-api
- description: Manage Oracle Database Home directories
  name: Oracle Database Database Homes API
  slug: oracle-database-database-homes-api
- description: Manage databases within DB Systems
  name: Oracle Database Databases API
  slug: oracle-database-databases-api
- description: Manage Oracle Database Cloud Service DB Systems
  name: Oracle Database DB Systems API
  slug: oracle-database-db-systems-api
- description: Document CRUD operations (get, insert, update, delete)
  name: Oracle Database Documents API
  slug: oracle-database-documents-api
- description: Core database instance status, version, and configuration services
  name: Oracle Database General API
  slug: oracle-database-general-api
- description: Collection index management
  name: Oracle Database Indexes API
  slug: oracle-database-indexes-api
- description: Collection metadata and catalog operations
  name: Oracle Database Metadata API
  slug: oracle-database-metadata-api
- description: Database session monitoring, locks, alerts, and wait metrics
  name: Oracle Database Monitoring API
  slug: oracle-database-monitoring-api
- description: Open Service Broker API compliant service provisioning
  name: Oracle Database Open Service Broker API
  slug: oracle-database-open-service-broker-api
- description: PDB snapshot carousel management
  name: Oracle Database PDB Snapshots API
  slug: oracle-database-pdb-snapshots-api
- description: SQL performance analysis, execution plans, and active session history
  name: Oracle Database Performance API
  slug: oracle-database-performance-api
- description: Manage pluggable databases in multitenant architecture
  name: Oracle Database Pluggable Databases API
  slug: oracle-database-pluggable-databases-api
- description: Query by Example (QBE) and filter operations
  name: Oracle Database Queries API
  slug: oracle-database-queries-api
- description: Knowledge graph management using W3C RDF, OWL, and SPARQL standards
  name: Oracle Database RDF Graph API
  slug: oracle-database-rdf-graph-api
- description: Custom REST API module, handler, and OAuth management
  name: Oracle Database REST Services API
  slug: oracle-database-rest-services-api
- description: Oracle Scheduler job management
  name: Oracle Database Scheduler API
  slug: oracle-database-scheduler-api
artifact_total: 226
asyncapis:
- description: Oracle Transactional Event Queues provide Kafka-compatible event streaming and message queuing capabilities built into Oracle Database. TxEventQ enables event-driven architectures with transactional g
  name: Oracle Transactional Event Queues (TxEventQ) API
  slug: oracle-database-txeventq-asyncapi
collections:
- collection_type: postman
  name: Oracle Database Oracle Cloud Infrastructure Database APEX API
  slug: postman-oracle-database-apex-api
- collection_type: postman
  name: Oracle Database Oracle Cloud Infrastructure Database APEX Autonomous Databases API
  slug: postman-oracle-database-autonomous-databases-api
- collection_type: postman
  name: Oracle Database Oracle Cloud Infrastructure Database APEX Backups API
  slug: postman-oracle-database-backups-api
- collection_type: postman
  name: Oracle Database Oracle Cloud Infrastructure Database APEX Bulk Operations API
  slug: postman-oracle-database-bulk-operations-api
- collection_type: postman
  name: Oracle Database Oracle Cloud Infrastructure Database APEX Collections API
  slug: postman-oracle-database-collections-api
- collection_type: postman
  name: Oracle Database Oracle Cloud Infrastructure Database APEX Data Dictionary API
  slug: postman-oracle-database-data-dictionary-api
- collection_type: postman
  name: Oracle Database Oracle Cloud Infrastructure Database APEX Data Guard API
  slug: postman-oracle-database-data-guard-api
- collection_type: postman
  name: Oracle Database Oracle Cloud Infrastructure Database APEX Data Pump API
  slug: postman-oracle-database-data-pump-api
- collection_type: postman
  name: Oracle Database Oracle Cloud Infrastructure Database APEX Database Homes API
  slug: postman-oracle-database-database-homes-api
- collection_type: postman
  name: Oracle Database Oracle Cloud Infrastructure Database APEX Databases API
  slug: postman-oracle-database-databases-api
- collection_type: postman
  name: Oracle Database Oracle Cloud Infrastructure Database APEX DB Systems API
  slug: postman-oracle-database-db-systems-api
- collection_type: postman
  name: Oracle Database Oracle Cloud Infrastructure Database APEX Documents API
  slug: postman-oracle-database-documents-api
- collection_type: postman
  name: Oracle Database Oracle Cloud Infrastructure Database APEX General API
  slug: postman-oracle-database-general-api
- collection_type: postman
  name: Oracle Database Oracle Cloud Infrastructure Database APEX Indexes API
  slug: postman-oracle-database-indexes-api
- collection_type: postman
  name: Oracle Database Oracle Cloud Infrastructure Database APEX Metadata API
  slug: postman-oracle-database-metadata-api
- collection_type: postman
  name: Oracle Database Oracle Cloud Infrastructure Database APEX Monitoring API
  slug: postman-oracle-database-monitoring-api
- collection_type: postman
  name: Oracle Database Oracle Cloud Infrastructure Database APEX Open Service Broker API
  slug: postman-oracle-database-open-service-broker-api
- collection_type: postman
  name: Oracle Database Oracle Cloud Infrastructure Database APEX PDB Snapshots API
  slug: postman-oracle-database-pdb-snapshots-api
- collection_type: postman
  name: Oracle Database Oracle Cloud Infrastructure Database APEX Performance API
  slug: postman-oracle-database-performance-api
- collection_type: postman
  name: Oracle Database Oracle Cloud Infrastructure Database APEX Pluggable Databases API
  slug: postman-oracle-database-pluggable-databases-api
- collection_type: postman
  name: Oracle Database Oracle Cloud Infrastructure Database APEX Queries API
  slug: postman-oracle-database-queries-api
- collection_type: postman
  name: Oracle Database Oracle Cloud Infrastructure Database APEX RDF Graph API
  slug: postman-oracle-database-rdf-graph-api
- collection_type: postman
  name: Oracle Database Oracle Cloud Infrastructure Database APEX REST Services API
  slug: postman-oracle-database-rest-services-api
- collection_type: postman
  name: Oracle Database Oracle Cloud Infrastructure Database APEX Scheduler API
  slug: postman-oracle-database-scheduler-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Oracle Database Oracle Cloud Infrastructure Database APEX API
  slug: open-oracle-database-apex-api
- collection_type: open
  name: Oracle Database Oracle Cloud Infrastructure Database APEX Autonomous Databases API
  slug: open-oracle-database-autonomous-databases-api
- collection_type: open
  name: Oracle Database Oracle Cloud Infrastructure Database APEX Backups API
  slug: open-oracle-database-backups-api
- collection_type: open
  name: Oracle Database Oracle Cloud Infrastructure Database APEX Bulk Operations API
  slug: open-oracle-database-bulk-operations-api
- collection_type: open
  name: Oracle Database Oracle Cloud Infrastructure Database APEX Collections API
  slug: open-oracle-database-collections-api
- collection_type: open
  name: Oracle Database Oracle Cloud Infrastructure Database APEX Data Dictionary API
  slug: open-oracle-database-data-dictionary-api
- collection_type: open
  name: Oracle Database Oracle Cloud Infrastructure Database APEX Data Guard API
  slug: open-oracle-database-data-guard-api
- collection_type: open
  name: Oracle Database Oracle Cloud Infrastructure Database APEX Data Pump API
  slug: open-oracle-database-data-pump-api
- collection_type: open
  name: Oracle Database Oracle Cloud Infrastructure Database APEX Database Homes API
  slug: open-oracle-database-database-homes-api
- collection_type: open
  name: Oracle Database Oracle Cloud Infrastructure Database APEX Databases API
  slug: open-oracle-database-databases-api
- collection_type: open
  name: Oracle Database Oracle Cloud Infrastructure Database APEX DB Systems API
  slug: open-oracle-database-db-systems-api
- collection_type: open
  name: Oracle Database Oracle Cloud Infrastructure Database APEX Documents API
  slug: open-oracle-database-documents-api
- collection_type: open
  name: Oracle Database Oracle Cloud Infrastructure Database APEX General API
  slug: open-oracle-database-general-api
- collection_type: open
  name: Oracle Database Oracle Cloud Infrastructure Database APEX Indexes API
  slug: open-oracle-database-indexes-api
- collection_type: open
  name: Oracle Database Oracle Cloud Infrastructure Database APEX Metadata API
  slug: open-oracle-database-metadata-api
- collection_type: open
  name: Oracle Database Oracle Cloud Infrastructure Database APEX Monitoring API
  slug: open-oracle-database-monitoring-api
- collection_type: open
  name: Oracle Database Oracle Cloud Infrastructure Database API
  slug: open-oracle-database-oci
- collection_type: open
  name: Oracle Database Oracle Cloud Infrastructure Database APEX Open Service Broker API
  slug: open-oracle-database-open-service-broker-api
- collection_type: open
  name: Oracle Database Oracle REST Data Services (ORDS) API
  slug: open-oracle-database-ords
- collection_type: open
  name: Oracle Database Oracle Cloud Infrastructure Database APEX PDB Snapshots API
  slug: open-oracle-database-pdb-snapshots-api
- collection_type: open
  name: Oracle Database Oracle Cloud Infrastructure Database APEX Performance API
  slug: open-oracle-database-performance-api
- collection_type: open
  name: Oracle Database Oracle Cloud Infrastructure Database APEX Pluggable Databases API
  slug: open-oracle-database-pluggable-databases-api
- collection_type: open
  name: Oracle Database Oracle Cloud Infrastructure Database APEX Queries API
  slug: open-oracle-database-queries-api
- collection_type: open
  name: Oracle Database Oracle Cloud Infrastructure Database APEX RDF Graph API
  slug: open-oracle-database-rdf-graph-api
- collection_type: open
  name: Oracle Database Oracle Cloud Infrastructure Database APEX REST Services API
  slug: open-oracle-database-rest-services-api
- collection_type: open
  name: Oracle Database Oracle Cloud Infrastructure Database APEX Scheduler API
  slug: open-oracle-database-scheduler-api
- collection_type: open
  name: Oracle Database Oracle SODA (Simple Oracle Document Access) REST API
  slug: open-oracle-database-soda
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/oracle-database/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/oracle-database-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/oracle-database-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/oracle-database-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/oracle-database-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/showcase/oracleautonomousdatabase
- group: start
  title: ''
  type: Portal
  url: https://www.oracle.com/database/technologies/appdev.html
- group: docs
  title: ''
  type: Documentation
  url: https://docs.oracle.com/en/database/oracle/oracle-database/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.oracle.com/database/technologies/appdev/quickstartsandtutorials.html
- group: operate
  title: ''
  type: Support
  url: https://www.oracle.com/support/
- group: operate
  title: ''
  type: StatusPage
  url: https://ocistatus.oraclecloud.com/
- group: company
  title: ''
  type: Blog
  url: https://blogs.oracle.com/database/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.oracle.com/legal/terms.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.oracle.com/legal/privacy/
- group: company
  title: ''
  type: Website
  url: https://www.oracle.com/database/
- group: start
  title: ''
  type: Console
  url: https://cloud.oracle.com/
- group: start
  title: ''
  type: Signup
  url: https://signup.cloud.oracle.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/oracle
- group: operate
  title: ''
  type: Community
  url: https://forums.oracle.com/ords/apexds/domain/dev-community
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/oracle
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/user/Oracle
- group: commercial
  title: ''
  type: Pricing
  url: https://www.oracle.com/database/technologies/oracle-database-pricing.html
created: '2024-01-20'
description: APIs and interfaces for Oracle Database management, querying, and administration.
finops:
- name: Oracle Database Finops
  service_category: Database
  slug: oracle-database-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/oracle-database.png
json_schemas:
- name: ActiveSessionHistoryList
  property_count: 1
  slug: oracle-database-activesessionhistorylist
- name: ActiveSessionWaitList
  property_count: 1
  slug: oracle-database-activesessionwaitlist
- name: AddDataGuardDatabaseRequest
  property_count: 2
  slug: oracle-database-adddataguarddatabaserequest
- name: AlertList
  property_count: 1
  slug: oracle-database-alertlist
- name: AlertSummaryList
  property_count: 1
  slug: oracle-database-alertsummarylist
- name: APEXApplicationList
  property_count: 1
  slug: oracle-database-apexapplicationlist
- name: APEXApplicationRequest
  property_count: 2
  slug: oracle-database-apexapplicationrequest
- name: APEXOverview
  property_count: 3
  slug: oracle-database-apexoverview
- name: APEXWorkspace
  property_count: 3
  slug: oracle-database-apexworkspace
- name: APEXWorkspaceList
  property_count: 1
  slug: oracle-database-apexworkspacelist
- name: Oracle Autonomous Database
  property_count: 27
  slug: oracle-database-autonomous-database
- name: AutonomousDatabase
  property_count: 20
  slug: oracle-database-autonomousdatabase
- name: AutonomousDatabaseBackup
  property_count: 9
  slug: oracle-database-autonomousdatabasebackup
- name: AutonomousDatabaseBackupSummary
  property_count: 7
  slug: oracle-database-autonomousdatabasebackupsummary
- name: AutonomousDatabaseSummary
  property_count: 10
  slug: oracle-database-autonomousdatabasesummary
- name: AutoRESTRequest
  property_count: 4
  slug: oracle-database-autorestrequest
- name: AutoSnapshotConfig
  property_count: 3
  slug: oracle-database-autosnapshotconfig
- name: Backup
  property_count: 8
  slug: oracle-database-backup
- name: BackupSummary
  property_count: 6
  slug: oracle-database-backupsummary
- name: BulkDeleteResponse
  property_count: 2
  slug: oracle-database-bulkdeleteresponse
- name: BulkInsertResponse
  property_count: 2
  slug: oracle-database-bulkinsertresponse
- name: BulkUpdateRequest
  property_count: 1
  slug: oracle-database-bulkupdaterequest
- name: BulkUpdateResponse
  property_count: 2
  slug: oracle-database-bulkupdateresponse
- name: CatalogResponse
  property_count: 2
  slug: oracle-database-catalogresponse
- name: Oracle SODA Collection
  property_count: 3
  slug: oracle-database-collection
- name: CollectionList
  property_count: 2
  slug: oracle-database-collectionlist
- name: CollectionMetadata
  property_count: 5
  slug: oracle-database-collectionmetadata
- name: CollectionSchema
  property_count: 4
  slug: oracle-database-collectionschema
- name: ColumnList
  property_count: 0
  slug: oracle-database-columnlist
- name: ColumnMetadata
  property_count: 7
  slug: oracle-database-columnmetadata
- name: ComponentList
  property_count: 1
  slug: oracle-database-componentlist
- name: CreateAutonomousDatabaseBackupDetails
  property_count: 4
  slug: oracle-database-createautonomousdatabasebackupdetails
- name: CreateAutonomousDatabaseDetails
  property_count: 13
  slug: oracle-database-createautonomousdatabasedetails
- name: CreateBackupDetails
  property_count: 2
  slug: oracle-database-createbackupdetails
- name: CreateDatabaseDetails
  property_count: 6
  slug: oracle-database-createdatabasedetails
- name: CreateDataGuardConfigRequest
  property_count: 2
  slug: oracle-database-createdataguardconfigrequest
- name: CreateDbHomeDetails
  property_count: 3
  slug: oracle-database-createdbhomedetails
- name: CreateOAuthClientRequest
  property_count: 4
  slug: oracle-database-createoauthclientrequest
- name: CreatePDBRequest
  property_count: 5
  slug: oracle-database-createpdbrequest
- name: CreatePluggableDatabaseDetails
  property_count: 5
  slug: oracle-database-createpluggabledatabasedetails
- name: CreatePrivilegeRequest
  property_count: 4
  slug: oracle-database-createprivilegerequest
- name: CreateRESTHandlerRequest
  property_count: 3
  slug: oracle-database-createresthandlerrequest
- name: CreateRESTModuleRequest
  property_count: 4
  slug: oracle-database-createrestmodulerequest
- name: CreateRoleRequest
  property_count: 2
  slug: oracle-database-createrolerequest
- name: Database
  property_count: 11
  slug: oracle-database-database
- name: DatabaseLink
  property_count: 5
  slug: oracle-database-databaselink
- name: DatabaseLinkList
  property_count: 1
  slug: oracle-database-databaselinklist
- name: DatabaseParameter
  property_count: 7
  slug: oracle-database-databaseparameter
- name: DatabaseStatus
  property_count: 5
  slug: oracle-database-databasestatus
- name: DatabaseSummary
  property_count: 6
  slug: oracle-database-databasesummary
- name: DatabaseVersion
  property_count: 3
  slug: oracle-database-databaseversion
- name: DatafileList
  property_count: 1
  slug: oracle-database-datafilelist
- name: DataGuardAssociationSummary
  property_count: 11
  slug: oracle-database-dataguardassociationsummary
- name: DataGuardConfiguration
  property_count: 4
  slug: oracle-database-dataguardconfiguration
- name: DataGuardDatabase
  property_count: 5
  slug: oracle-database-dataguarddatabase
- name: DataGuardDatabaseList
  property_count: 1
  slug: oracle-database-dataguarddatabaselist
- name: DataPumpExportRequest
  property_count: 6
  slug: oracle-database-datapumpexportrequest
- name: DataPumpImportRequest
  property_count: 5
  slug: oracle-database-datapumpimportrequest
- name: DataPumpJob
  property_count: 7
  slug: oracle-database-datapumpjob
- name: DataPumpJobList
  property_count: 1
  slug: oracle-database-datapumpjoblist
- name: DbHome
  property_count: 7
  slug: oracle-database-dbhome
- name: DbHomeSummary
  property_count: 5
  slug: oracle-database-dbhomesummary
- name: DbSystem
  property_count: 18
  slug: oracle-database-dbsystem
- name: DbSystemSummary
  property_count: 8
  slug: oracle-database-dbsystemsummary
- name: Document
  property_count: 7
  slug: oracle-database-document
- name: Oracle SODA Document
  property_count: 7
  slug: oracle-database-document
- name: DocumentList
  property_count: 7
  slug: oracle-database-documentlist
- name: DocumentMetadata
  property_count: 4
  slug: oracle-database-documentmetadata
- name: Error
  property_count: 2
  slug: oracle-database-error
- name: Oracle Transactional Event Queue Message
  property_count: 8
  slug: oracle-database-event-message
- name: ExecutionPlan
  property_count: 3
  slug: oracle-database-executionplan
- name: FeatureUsageList
  property_count: 1
  slug: oracle-database-featureusagelist
- name: ForeignKeyList
  property_count: 1
  slug: oracle-database-foreignkeylist
- name: FunctionList
  property_count: 1
  slug: oracle-database-functionlist
- name: FunctionMetadata
  property_count: 5
  slug: oracle-database-functionmetadata
- name: GenerateAutonomousDatabaseWalletDetails
  property_count: 2
  slug: oracle-database-generateautonomousdatabasewalletdetails
- name: IndexList
  property_count: 1
  slug: oracle-database-indexlist
- name: IndexMetadata
  property_count: 6
  slug: oracle-database-indexmetadata
- name: IndexSpecification
  property_count: 6
  slug: oracle-database-indexspecification
- name: InsertResponse
  property_count: 2
  slug: oracle-database-insertresponse
- name: JsonPatchOperation
  property_count: 4
  slug: oracle-database-jsonpatchoperation
- name: LaunchDbSystemDetails
  property_count: 14
  slug: oracle-database-launchdbsystemdetails
- name: Link
  property_count: 2
  slug: oracle-database-link
- name: OAuthClientList
  property_count: 1
  slug: oracle-database-oauthclientlist
- name: ORDSPropertyList
  property_count: 1
  slug: oracle-database-ordspropertylist
- name: ORDSPropertyValue
  property_count: 1
  slug: oracle-database-ordspropertyvalue
- name: PaginatedResponse
  property_count: 6
  slug: oracle-database-paginatedresponse
- name: ParameterList
  property_count: 0
  slug: oracle-database-parameterlist
- name: PDB
  property_count: 6
  slug: oracle-database-pdb
- name: PDBList
  property_count: 1
  slug: oracle-database-pdblist
- name: Oracle Pluggable Database
  property_count: 14
  slug: oracle-database-pluggable-database
- name: PluggableDatabase
  property_count: 8
  slug: oracle-database-pluggabledatabase
- name: PluggableDatabaseSummary
  property_count: 6
  slug: oracle-database-pluggabledatabasesummary
- name: ProvisionRequest
  property_count: 3
  slug: oracle-database-provisionrequest
- name: QBEFilter
  property_count: 0
  slug: oracle-database-qbefilter
- name: RDFModelList
  property_count: 1
  slug: oracle-database-rdfmodellist
- name: RDFNetwork
  property_count: 2
  slug: oracle-database-rdfnetwork
- name: RDFNetworkList
  property_count: 1
  slug: oracle-database-rdfnetworklist
- name: RESTHandlerList
  property_count: 1
  slug: oracle-database-resthandlerlist
- name: RESTModule
  property_count: 5
  slug: oracle-database-restmodule
- name: RESTModuleList
  property_count: 1
  slug: oracle-database-restmodulelist
- name: SchedulerJob
  property_count: 8
  slug: oracle-database-schedulerjob
- name: SchedulerJobList
  property_count: 1
  slug: oracle-database-schedulerjoblist
- name: ServiceCatalog
  property_count: 1
  slug: oracle-database-servicecatalog
- name: SessionDetail
  property_count: 10
  slug: oracle-database-sessiondetail
- name: SessionlessTransaction
  property_count: 1
  slug: oracle-database-sessionlesstransaction
- name: SessionLimitList
  property_count: 1
  slug: oracle-database-sessionlimitlist
- name: SessionList
  property_count: 0
  slug: oracle-database-sessionlist
- name: SessionLockList
  property_count: 1
  slug: oracle-database-sessionlocklist
- name: Snapshot
  property_count: 4
  slug: oracle-database-snapshot
- name: SnapshotList
  property_count: 1
  slug: oracle-database-snapshotlist
- name: SnapshotMode
  property_count: 1
  slug: oracle-database-snapshotmode
- name: SPARQLResults
  property_count: 2
  slug: oracle-database-sparqlresults
- name: SQLHistoryList
  property_count: 1
  slug: oracle-database-sqlhistorylist
- name: SQLStatementDetail
  property_count: 8
  slug: oracle-database-sqlstatementdetail
- name: SQLStatementList
  property_count: 0
  slug: oracle-database-sqlstatementlist
- name: SQLText
  property_count: 2
  slug: oracle-database-sqltext
- name: StorageInfo
  property_count: 3
  slug: oracle-database-storageinfo
- name: Oracle Database Table
  property_count: 14
  slug: oracle-database-table
- name: TableList
  property_count: 0
  slug: oracle-database-tablelist
- name: TableMetadata
  property_count: 7
  slug: oracle-database-tablemetadata
- name: Tablespace
  property_count: 7
  slug: oracle-database-tablespace
- name: TablespaceList
  property_count: 1
  slug: oracle-database-tablespacelist
- name: UpdateAutonomousDatabaseDetails
  property_count: 7
  slug: oracle-database-updateautonomousdatabasedetails
- name: UpdateDatabaseDetails
  property_count: 2
  slug: oracle-database-updatedatabasedetails
- name: UpdateDataGuardConfigRequest
  property_count: 2
  slug: oracle-database-updatedataguardconfigrequest
- name: UpdateDataGuardDatabaseRequest
  property_count: 1
  slug: oracle-database-updatedataguarddatabaserequest
- name: UpdateDbSystemDetails
  property_count: 5
  slug: oracle-database-updatedbsystemdetails
- name: UpdatePDBRequest
  property_count: 2
  slug: oracle-database-updatepdbrequest
- name: UpdatePluggableDatabaseDetails
  property_count: 2
  slug: oracle-database-updatepluggabledatabasedetails
- name: UserList
  property_count: 1
  slug: oracle-database-userlist
- name: WaitClassMetricList
  property_count: 1
  slug: oracle-database-waitclassmetriclist
- name: WaitClassTotalList
  property_count: 1
  slug: oracle-database-waitclasstotallist
json_structures:
- name: Oracle Database Structure
  property_count: 0
  slug: oracle-database-structure
jsonld:
- class_count: 12
  name: Oracle Database Context
  property_count: 30
  slug: oracle-database-context
layout: provider
modified: '2026-05-19'
name: Oracle Database
nav: Providers
network: true
overview: 'Oracle Database publishes 25 APIs on the [APIs.io](https://apis.io/) network, including Oracle Transactional Event Queues (TxEventQ), APEX API, Autonomous Databases API, and 22 more. Tagged areas include Cloud, Database, Enterprise, Oracle, and REST API.


  The Oracle Database catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 2 Spectral governance rulesets.


  Oracle Database''s developer surface includes authentication, developer portal, documentation, getting-started guide, support, engineering blog, developer console, and 15 more developer resources.'
plans:
- name: Oracle Database Plans Pricing
  plan_count: 6
  slug: oracle-database-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 4
  name: Oracle Database Rate Limits
  slug: oracle-database-rate-limits
rules:
- effective_rule_count: 33
  extends:
  - spectral:asyncapi
  name: Oracle Database API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: oracle-database-asyncapi-spectral-rules
- effective_rule_count: 5
  extends: []
  name: Oracle Database API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: oracle-database-jsonschema-spectral-rules
scopes:
- name: Oracle Database Scopes
  scope_count: 0
  slug: oracle-database-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 48.3
  delta: -10.5
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 13.6
    contract_quality: 82.2
    developer_ergonomics: 42.9
    discoverability: 40.7
    governance: 13.6
    operational_transparency: 26.3
  previous_composite: 58.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 24
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/oracle-database/refs/heads/main/screenshots/oracle-database-2026-06-20T191126.png
security:
- kind: authentication
  name: Oracle Database Authentication
  slug: oracle-database-authentication
  summary_line: http/oauth2 · 4 schemes
- kind: domain-security
  name: Oracle Database Domain Security
  slug: oracle-database-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: oracle-database
tags:
- Cloud
- Database
- Enterprise
- Oracle
- REST API
- SQL
website: https://www.oracle.com/database/
---
