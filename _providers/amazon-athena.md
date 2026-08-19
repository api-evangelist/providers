---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 35.0
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 32
  human_in_the_loop: 1
  name: Amazon Athena Agentic Access
  operation_count: 32
  slug: amazon-athena-agentic-access
  summary_line: 32 operations · 32 acting · 1 human-in-the-loop
api_count: 8
apis:
- description: Operations for managing data catalogs
  name: Amazon Athena Data Catalogs API
  slug: amazon-athena-data-catalogs-api
- description: Operations for listing databases in a data catalog
  name: Amazon Athena Databases API
  slug: amazon-athena-databases-api
- description: Operations for creating and managing saved SQL queries
  name: Amazon Athena Named Queries API
  slug: amazon-athena-named-queries-api
- description: Operations for managing prepared SQL statements
  name: Amazon Athena Prepared Statements API
  slug: amazon-athena-prepared-statements-api
- description: Operations for running and managing SQL query executions
  name: Amazon Athena Query Executions API
  slug: amazon-athena-query-executions-api
- description: Operations for listing and getting table metadata
  name: Amazon Athena Table Metadata API
  slug: amazon-athena-table-metadata-api
- description: Operations for managing resource tags
  name: Amazon Athena Tags API
  slug: amazon-athena-tags-api
- description: Operations for managing Athena work groups
  name: Amazon Athena Work Groups API
  slug: amazon-athena-work-groups-api
artifact_total: 349
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Amazon Athena Data Catalogs API
  slug: open-amazon-athena-data-catalogs-api
- collection_type: open
  name: Amazon Athena Data Catalogs Databases API
  slug: open-amazon-athena-databases-api
- collection_type: open
  name: Amazon Athena Data Catalogs Named Queries API
  slug: open-amazon-athena-named-queries-api
- collection_type: open
  name: Amazon Athena Data Catalogs Prepared Statements API
  slug: open-amazon-athena-prepared-statements-api
- collection_type: open
  name: Amazon Athena Data Catalogs Query Executions API
  slug: open-amazon-athena-query-executions-api
- collection_type: open
  name: Amazon Athena Data Catalogs Table Metadata API
  slug: open-amazon-athena-table-metadata-api
- collection_type: open
  name: Amazon Athena Data Catalogs Tags API
  slug: open-amazon-athena-tags-api
- collection_type: open
  name: Amazon Athena Data Catalogs Work Groups API
  slug: open-amazon-athena-work-groups-api
- collection_type: open
  name: Amazon Athena API
  slug: open-amazon-athena
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/amazon-athena-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-athena-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amazon-athena-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/amazon-athena-authentication.yml
created: '2024-01-15'
description: Amazon Athena is an interactive query service that makes it easy to analyze data in Amazon S3 using standard SQL. Athena is serverless, so there is no infrastructure to manage, and you pay only for the queries that you run.
examples:
- key_count: 3
  name: Athena Athena Error Example
  slug: athena-athena-error-example
- key_count: 3
  name: Athena Batch Get Named Query Input Example
  slug: athena-batch-get-named-query-input-example
- key_count: 3
  name: Athena Batch Get Named Query Output Example
  slug: athena-batch-get-named-query-output-example
- key_count: 3
  name: Athena Batch Get Query Execution Input Example
  slug: athena-batch-get-query-execution-input-example
- key_count: 3
  name: Athena Batch Get Query Execution Output Example
  slug: athena-batch-get-query-execution-output-example
- key_count: 3
  name: Athena Column Example
  slug: athena-column-example
- key_count: 3
  name: Athena Column Info Example
  slug: athena-column-info-example
- key_count: 3
  name: Athena Create Data Catalog Input Example
  slug: athena-create-data-catalog-input-example
- key_count: 3
  name: Athena Create Data Catalog Output Example
  slug: athena-create-data-catalog-output-example
- key_count: 3
  name: Athena Create Named Query Input Example
  slug: athena-create-named-query-input-example
- key_count: 3
  name: Athena Create Named Query Output Example
  slug: athena-create-named-query-output-example
- key_count: 3
  name: Athena Create Prepared Statement Input Example
  slug: athena-create-prepared-statement-input-example
- key_count: 3
  name: Athena Create Prepared Statement Output Example
  slug: athena-create-prepared-statement-output-example
- key_count: 3
  name: Athena Create Work Group Input Example
  slug: athena-create-work-group-input-example
- key_count: 3
  name: Athena Create Work Group Output Example
  slug: athena-create-work-group-output-example
- key_count: 3
  name: Athena Data Catalog Example
  slug: athena-data-catalog-example
- key_count: 3
  name: Athena Data Catalog Summary Example
  slug: athena-data-catalog-summary-example
- key_count: 3
  name: Athena Database Example
  slug: athena-database-example
- key_count: 3
  name: Athena Datum Example
  slug: athena-datum-example
- key_count: 3
  name: Athena Delete Data Catalog Input Example
  slug: athena-delete-data-catalog-input-example
- key_count: 3
  name: Athena Delete Data Catalog Output Example
  slug: athena-delete-data-catalog-output-example
- key_count: 3
  name: Athena Delete Named Query Input Example
  slug: athena-delete-named-query-input-example
- key_count: 3
  name: Athena Delete Named Query Output Example
  slug: athena-delete-named-query-output-example
- key_count: 3
  name: Athena Delete Prepared Statement Input Example
  slug: athena-delete-prepared-statement-input-example
- key_count: 3
  name: Athena Delete Prepared Statement Output Example
  slug: athena-delete-prepared-statement-output-example
- key_count: 3
  name: Athena Delete Work Group Input Example
  slug: athena-delete-work-group-input-example
- key_count: 3
  name: Athena Delete Work Group Output Example
  slug: athena-delete-work-group-output-example
- key_count: 3
  name: Athena Encryption Configuration Example
  slug: athena-encryption-configuration-example
- key_count: 3
  name: Athena Engine Version Example
  slug: athena-engine-version-example
- key_count: 3
  name: Athena Get Data Catalog Input Example
  slug: athena-get-data-catalog-input-example
- key_count: 3
  name: Athena Get Data Catalog Output Example
  slug: athena-get-data-catalog-output-example
- key_count: 3
  name: Athena Get Database Input Example
  slug: athena-get-database-input-example
- key_count: 3
  name: Athena Get Database Output Example
  slug: athena-get-database-output-example
- key_count: 3
  name: Athena Get Named Query Input Example
  slug: athena-get-named-query-input-example
- key_count: 3
  name: Athena Get Named Query Output Example
  slug: athena-get-named-query-output-example
- key_count: 3
  name: Athena Get Prepared Statement Input Example
  slug: athena-get-prepared-statement-input-example
- key_count: 3
  name: Athena Get Prepared Statement Output Example
  slug: athena-get-prepared-statement-output-example
- key_count: 3
  name: Athena Get Query Execution Input Example
  slug: athena-get-query-execution-input-example
- key_count: 3
  name: Athena Get Query Execution Output Example
  slug: athena-get-query-execution-output-example
- key_count: 3
  name: Athena Get Query Results Input Example
  slug: athena-get-query-results-input-example
- key_count: 3
  name: Athena Get Query Results Output Example
  slug: athena-get-query-results-output-example
- key_count: 3
  name: Athena Get Query Runtime Statistics Input Example
  slug: athena-get-query-runtime-statistics-input-example
- key_count: 3
  name: Athena Get Query Runtime Statistics Output Example
  slug: athena-get-query-runtime-statistics-output-example
- key_count: 3
  name: Athena Get Table Metadata Input Example
  slug: athena-get-table-metadata-input-example
- key_count: 3
  name: Athena Get Table Metadata Output Example
  slug: athena-get-table-metadata-output-example
- key_count: 3
  name: Athena Get Work Group Input Example
  slug: athena-get-work-group-input-example
- key_count: 3
  name: Athena Get Work Group Output Example
  slug: athena-get-work-group-output-example
- key_count: 3
  name: Athena List Data Catalogs Input Example
  slug: athena-list-data-catalogs-input-example
- key_count: 3
  name: Athena List Data Catalogs Output Example
  slug: athena-list-data-catalogs-output-example
- key_count: 3
  name: Athena List Databases Input Example
  slug: athena-list-databases-input-example
- key_count: 3
  name: Athena List Databases Output Example
  slug: athena-list-databases-output-example
- key_count: 3
  name: Athena List Named Queries Input Example
  slug: athena-list-named-queries-input-example
- key_count: 3
  name: Athena List Named Queries Output Example
  slug: athena-list-named-queries-output-example
- key_count: 3
  name: Athena List Prepared Statements Input Example
  slug: athena-list-prepared-statements-input-example
- key_count: 3
  name: Athena List Prepared Statements Output Example
  slug: athena-list-prepared-statements-output-example
- key_count: 3
  name: Athena List Query Executions Input Example
  slug: athena-list-query-executions-input-example
- key_count: 3
  name: Athena List Query Executions Output Example
  slug: athena-list-query-executions-output-example
- key_count: 3
  name: Athena List Table Metadata Input Example
  slug: athena-list-table-metadata-input-example
- key_count: 3
  name: Athena List Table Metadata Output Example
  slug: athena-list-table-metadata-output-example
- key_count: 3
  name: Athena List Tags For Resource Input Example
  slug: athena-list-tags-for-resource-input-example
- key_count: 3
  name: Athena List Tags For Resource Output Example
  slug: athena-list-tags-for-resource-output-example
- key_count: 3
  name: Athena List Work Groups Input Example
  slug: athena-list-work-groups-input-example
- key_count: 3
  name: Athena List Work Groups Output Example
  slug: athena-list-work-groups-output-example
- key_count: 3
  name: Athena Named Query Example
  slug: athena-named-query-example
- key_count: 3
  name: Athena Prepared Statement Example
  slug: athena-prepared-statement-example
- key_count: 3
  name: Athena Prepared Statement Summary Example
  slug: athena-prepared-statement-summary-example
- key_count: 3
  name: Athena Query Execution Context Example
  slug: athena-query-execution-context-example
- key_count: 3
  name: Athena Query Execution Example
  slug: athena-query-execution-example
- key_count: 3
  name: Athena Query Execution Statistics Example
  slug: athena-query-execution-statistics-example
- key_count: 3
  name: Athena Query Execution Status Example
  slug: athena-query-execution-status-example
- key_count: 3
  name: Athena Query Runtime Statistics Example
  slug: athena-query-runtime-statistics-example
- key_count: 3
  name: Athena Query Runtime Statistics Rows Example
  slug: athena-query-runtime-statistics-rows-example
- key_count: 3
  name: Athena Query Runtime Statistics Timeline Example
  slug: athena-query-runtime-statistics-timeline-example
- key_count: 3
  name: Athena Query Stage Example
  slug: athena-query-stage-example
- key_count: 3
  name: Athena Query Stage Plan Node Example
  slug: athena-query-stage-plan-node-example
- key_count: 3
  name: Athena Result Configuration Example
  slug: athena-result-configuration-example
- key_count: 3
  name: Athena Result Configuration Updates Example
  slug: athena-result-configuration-updates-example
- key_count: 3
  name: Athena Result Set Example
  slug: athena-result-set-example
- key_count: 3
  name: Athena Result Set Metadata Example
  slug: athena-result-set-metadata-example
- key_count: 3
  name: Athena Row Example
  slug: athena-row-example
- key_count: 3
  name: Athena Start Query Execution Input Example
  slug: athena-start-query-execution-input-example
- key_count: 3
  name: Athena Start Query Execution Output Example
  slug: athena-start-query-execution-output-example
- key_count: 3
  name: Athena Stop Query Execution Input Example
  slug: athena-stop-query-execution-input-example
- key_count: 3
  name: Athena Stop Query Execution Output Example
  slug: athena-stop-query-execution-output-example
- key_count: 3
  name: Athena Table Metadata Example
  slug: athena-table-metadata-example
- key_count: 3
  name: Athena Tag Example
  slug: athena-tag-example
- key_count: 3
  name: Athena Tag Resource Input Example
  slug: athena-tag-resource-input-example
- key_count: 3
  name: Athena Tag Resource Output Example
  slug: athena-tag-resource-output-example
- key_count: 3
  name: Athena Unprocessed Named Query Id Example
  slug: athena-unprocessed-named-query-id-example
- key_count: 3
  name: Athena Unprocessed Query Execution Id Example
  slug: athena-unprocessed-query-execution-id-example
- key_count: 3
  name: Athena Untag Resource Input Example
  slug: athena-untag-resource-input-example
- key_count: 3
  name: Athena Untag Resource Output Example
  slug: athena-untag-resource-output-example
- key_count: 3
  name: Athena Update Work Group Input Example
  slug: athena-update-work-group-input-example
- key_count: 3
  name: Athena Update Work Group Output Example
  slug: athena-update-work-group-output-example
- key_count: 3
  name: Athena Work Group Configuration Example
  slug: athena-work-group-configuration-example
- key_count: 3
  name: Athena Work Group Configuration Updates Example
  slug: athena-work-group-configuration-updates-example
- key_count: 3
  name: Athena Work Group Example
  slug: athena-work-group-example
- key_count: 3
  name: Athena Work Group Summary Example
  slug: athena-work-group-summary-example
features:
- Serverless SQL query execution against Amazon S3 data
- Pay-per-query pricing with no infrastructure management
- Support for standard ANSI SQL with complex joins and window functions
- Integration with AWS Glue Data Catalog for schema management
- Named queries for saving and reusing SQL statements
- Work groups for query isolation and cost management
- Prepared statements for parameterized query execution
- Multiple data format support including Parquet, ORC, JSON, CSV
- Query result caching for improved performance and cost reduction
- Fine-grained access control with IAM and Lake Formation
finops:
- name: Amazon Athena Finops
  service_category: API
  slug: amazon-athena-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/amazon-athena.png
integrations:
- Amazon S3
- AWS Glue
- Amazon QuickSight
- AWS Lake Formation
- Amazon CloudWatch
- AWS IAM
- Amazon DynamoDB
- AWS Step Functions
- Amazon SageMaker
- Apache Spark
json_schemas:
- name: Amazon Athena Query Execution
  property_count: 11
  slug: amazon-athena
- name: AthenaError
  property_count: 0
  slug: athena-athena-error
- name: BatchGetNamedQueryInput
  property_count: 0
  slug: athena-batch-get-named-query-input
- name: BatchGetNamedQueryOutput
  property_count: 0
  slug: athena-batch-get-named-query-output
- name: BatchGetQueryExecutionInput
  property_count: 0
  slug: athena-batch-get-query-execution-input
- name: BatchGetQueryExecutionOutput
  property_count: 0
  slug: athena-batch-get-query-execution-output
- name: ColumnInfo
  property_count: 0
  slug: athena-column-info
- name: Column
  property_count: 0
  slug: athena-column
- name: CreateDataCatalogInput
  property_count: 0
  slug: athena-create-data-catalog-input
- name: CreateDataCatalogOutput
  property_count: 0
  slug: athena-create-data-catalog-output
- name: CreateNamedQueryInput
  property_count: 0
  slug: athena-create-named-query-input
- name: CreateNamedQueryOutput
  property_count: 0
  slug: athena-create-named-query-output
- name: CreatePreparedStatementInput
  property_count: 0
  slug: athena-create-prepared-statement-input
- name: CreatePreparedStatementOutput
  property_count: 0
  slug: athena-create-prepared-statement-output
- name: CreateWorkGroupInput
  property_count: 0
  slug: athena-create-work-group-input
- name: CreateWorkGroupOutput
  property_count: 0
  slug: athena-create-work-group-output
- name: DataCatalog
  property_count: 0
  slug: athena-data-catalog
- name: DataCatalogSummary
  property_count: 0
  slug: athena-data-catalog-summary
- name: Database
  property_count: 0
  slug: athena-database
- name: Datum
  property_count: 0
  slug: athena-datum
- name: DeleteDataCatalogInput
  property_count: 0
  slug: athena-delete-data-catalog-input
- name: DeleteDataCatalogOutput
  property_count: 0
  slug: athena-delete-data-catalog-output
- name: DeleteNamedQueryInput
  property_count: 0
  slug: athena-delete-named-query-input
- name: DeleteNamedQueryOutput
  property_count: 0
  slug: athena-delete-named-query-output
- name: DeletePreparedStatementInput
  property_count: 0
  slug: athena-delete-prepared-statement-input
- name: DeletePreparedStatementOutput
  property_count: 0
  slug: athena-delete-prepared-statement-output
- name: DeleteWorkGroupInput
  property_count: 0
  slug: athena-delete-work-group-input
- name: DeleteWorkGroupOutput
  property_count: 0
  slug: athena-delete-work-group-output
- name: EncryptionConfiguration
  property_count: 0
  slug: athena-encryption-configuration
- name: EngineVersion
  property_count: 0
  slug: athena-engine-version
- name: GetDataCatalogInput
  property_count: 0
  slug: athena-get-data-catalog-input
- name: GetDataCatalogOutput
  property_count: 0
  slug: athena-get-data-catalog-output
- name: GetDatabaseInput
  property_count: 0
  slug: athena-get-database-input
- name: GetDatabaseOutput
  property_count: 0
  slug: athena-get-database-output
- name: GetNamedQueryInput
  property_count: 0
  slug: athena-get-named-query-input
- name: GetNamedQueryOutput
  property_count: 0
  slug: athena-get-named-query-output
- name: GetPreparedStatementInput
  property_count: 0
  slug: athena-get-prepared-statement-input
- name: GetPreparedStatementOutput
  property_count: 0
  slug: athena-get-prepared-statement-output
- name: GetQueryExecutionInput
  property_count: 0
  slug: athena-get-query-execution-input
- name: GetQueryExecutionOutput
  property_count: 0
  slug: athena-get-query-execution-output
- name: GetQueryResultsInput
  property_count: 0
  slug: athena-get-query-results-input
- name: GetQueryResultsOutput
  property_count: 0
  slug: athena-get-query-results-output
- name: GetQueryRuntimeStatisticsInput
  property_count: 0
  slug: athena-get-query-runtime-statistics-input
- name: GetQueryRuntimeStatisticsOutput
  property_count: 0
  slug: athena-get-query-runtime-statistics-output
- name: GetTableMetadataInput
  property_count: 0
  slug: athena-get-table-metadata-input
- name: GetTableMetadataOutput
  property_count: 0
  slug: athena-get-table-metadata-output
- name: GetWorkGroupInput
  property_count: 0
  slug: athena-get-work-group-input
- name: GetWorkGroupOutput
  property_count: 0
  slug: athena-get-work-group-output
- name: ListDataCatalogsInput
  property_count: 0
  slug: athena-list-data-catalogs-input
- name: ListDataCatalogsOutput
  property_count: 0
  slug: athena-list-data-catalogs-output
- name: ListDatabasesInput
  property_count: 0
  slug: athena-list-databases-input
- name: ListDatabasesOutput
  property_count: 0
  slug: athena-list-databases-output
- name: ListNamedQueriesInput
  property_count: 0
  slug: athena-list-named-queries-input
- name: ListNamedQueriesOutput
  property_count: 0
  slug: athena-list-named-queries-output
- name: ListPreparedStatementsInput
  property_count: 0
  slug: athena-list-prepared-statements-input
- name: ListPreparedStatementsOutput
  property_count: 0
  slug: athena-list-prepared-statements-output
- name: ListQueryExecutionsInput
  property_count: 0
  slug: athena-list-query-executions-input
- name: ListQueryExecutionsOutput
  property_count: 0
  slug: athena-list-query-executions-output
- name: ListTableMetadataInput
  property_count: 0
  slug: athena-list-table-metadata-input
- name: ListTableMetadataOutput
  property_count: 0
  slug: athena-list-table-metadata-output
- name: ListTagsForResourceInput
  property_count: 0
  slug: athena-list-tags-for-resource-input
- name: ListTagsForResourceOutput
  property_count: 0
  slug: athena-list-tags-for-resource-output
- name: ListWorkGroupsInput
  property_count: 0
  slug: athena-list-work-groups-input
- name: ListWorkGroupsOutput
  property_count: 0
  slug: athena-list-work-groups-output
- name: NamedQuery
  property_count: 0
  slug: athena-named-query
- name: PreparedStatement
  property_count: 0
  slug: athena-prepared-statement
- name: PreparedStatementSummary
  property_count: 0
  slug: athena-prepared-statement-summary
- name: QueryExecutionContext
  property_count: 0
  slug: athena-query-execution-context
- name: QueryExecution
  property_count: 0
  slug: athena-query-execution
- name: QueryExecutionStatistics
  property_count: 0
  slug: athena-query-execution-statistics
- name: QueryExecutionStatus
  property_count: 0
  slug: athena-query-execution-status
- name: QueryRuntimeStatisticsRows
  property_count: 0
  slug: athena-query-runtime-statistics-rows
- name: QueryRuntimeStatistics
  property_count: 0
  slug: athena-query-runtime-statistics
- name: QueryRuntimeStatisticsTimeline
  property_count: 0
  slug: athena-query-runtime-statistics-timeline
- name: QueryStagePlanNode
  property_count: 0
  slug: athena-query-stage-plan-node
- name: QueryStage
  property_count: 0
  slug: athena-query-stage
- name: ResultConfiguration
  property_count: 0
  slug: athena-result-configuration
- name: ResultConfigurationUpdates
  property_count: 0
  slug: athena-result-configuration-updates
- name: ResultSetMetadata
  property_count: 0
  slug: athena-result-set-metadata
- name: ResultSet
  property_count: 0
  slug: athena-result-set
- name: Row
  property_count: 0
  slug: athena-row
- name: StartQueryExecutionInput
  property_count: 0
  slug: athena-start-query-execution-input
- name: StartQueryExecutionOutput
  property_count: 0
  slug: athena-start-query-execution-output
- name: StopQueryExecutionInput
  property_count: 0
  slug: athena-stop-query-execution-input
- name: StopQueryExecutionOutput
  property_count: 0
  slug: athena-stop-query-execution-output
- name: TableMetadata
  property_count: 0
  slug: athena-table-metadata
- name: TagResourceInput
  property_count: 0
  slug: athena-tag-resource-input
- name: TagResourceOutput
  property_count: 0
  slug: athena-tag-resource-output
- name: Tag
  property_count: 0
  slug: athena-tag
- name: UnprocessedNamedQueryId
  property_count: 0
  slug: athena-unprocessed-named-query-id
- name: UnprocessedQueryExecutionId
  property_count: 0
  slug: athena-unprocessed-query-execution-id
- name: UntagResourceInput
  property_count: 0
  slug: athena-untag-resource-input
- name: UntagResourceOutput
  property_count: 0
  slug: athena-untag-resource-output
- name: UpdateWorkGroupInput
  property_count: 0
  slug: athena-update-work-group-input
- name: UpdateWorkGroupOutput
  property_count: 0
  slug: athena-update-work-group-output
- name: WorkGroupConfiguration
  property_count: 0
  slug: athena-work-group-configuration
- name: WorkGroupConfigurationUpdates
  property_count: 0
  slug: athena-work-group-configuration-updates
- name: WorkGroup
  property_count: 0
  slug: athena-work-group
- name: WorkGroupSummary
  property_count: 0
  slug: athena-work-group-summary
json_structures:
- name: Athena Athena Error Structure
  property_count: 0
  slug: athena-athena-error-structure
- name: Athena Batch Get Named Query Input Structure
  property_count: 0
  slug: athena-batch-get-named-query-input-structure
- name: Athena Batch Get Named Query Output Structure
  property_count: 0
  slug: athena-batch-get-named-query-output-structure
- name: Athena Batch Get Query Execution Input Structure
  property_count: 0
  slug: athena-batch-get-query-execution-input-structure
- name: Athena Batch Get Query Execution Output Structure
  property_count: 0
  slug: athena-batch-get-query-execution-output-structure
- name: Athena Column Info Structure
  property_count: 0
  slug: athena-column-info-structure
- name: Athena Column Structure
  property_count: 0
  slug: athena-column-structure
- name: Athena Create Data Catalog Input Structure
  property_count: 0
  slug: athena-create-data-catalog-input-structure
- name: Athena Create Data Catalog Output Structure
  property_count: 0
  slug: athena-create-data-catalog-output-structure
- name: Athena Create Named Query Input Structure
  property_count: 0
  slug: athena-create-named-query-input-structure
- name: Athena Create Named Query Output Structure
  property_count: 0
  slug: athena-create-named-query-output-structure
- name: Athena Create Prepared Statement Input Structure
  property_count: 0
  slug: athena-create-prepared-statement-input-structure
- name: Athena Create Prepared Statement Output Structure
  property_count: 0
  slug: athena-create-prepared-statement-output-structure
- name: Athena Create Work Group Input Structure
  property_count: 0
  slug: athena-create-work-group-input-structure
- name: Athena Create Work Group Output Structure
  property_count: 0
  slug: athena-create-work-group-output-structure
- name: Athena Data Catalog Structure
  property_count: 0
  slug: athena-data-catalog-structure
- name: Athena Data Catalog Summary Structure
  property_count: 0
  slug: athena-data-catalog-summary-structure
- name: Athena Database Structure
  property_count: 0
  slug: athena-database-structure
- name: Athena Datum Structure
  property_count: 0
  slug: athena-datum-structure
- name: Athena Delete Data Catalog Input Structure
  property_count: 0
  slug: athena-delete-data-catalog-input-structure
- name: Athena Delete Data Catalog Output Structure
  property_count: 0
  slug: athena-delete-data-catalog-output-structure
- name: Athena Delete Named Query Input Structure
  property_count: 0
  slug: athena-delete-named-query-input-structure
- name: Athena Delete Named Query Output Structure
  property_count: 0
  slug: athena-delete-named-query-output-structure
- name: Athena Delete Prepared Statement Input Structure
  property_count: 0
  slug: athena-delete-prepared-statement-input-structure
- name: Athena Delete Prepared Statement Output Structure
  property_count: 0
  slug: athena-delete-prepared-statement-output-structure
- name: Athena Delete Work Group Input Structure
  property_count: 0
  slug: athena-delete-work-group-input-structure
- name: Athena Delete Work Group Output Structure
  property_count: 0
  slug: athena-delete-work-group-output-structure
- name: Athena Encryption Configuration Structure
  property_count: 0
  slug: athena-encryption-configuration-structure
- name: Athena Engine Version Structure
  property_count: 0
  slug: athena-engine-version-structure
- name: Athena Get Data Catalog Input Structure
  property_count: 0
  slug: athena-get-data-catalog-input-structure
- name: Athena Get Data Catalog Output Structure
  property_count: 0
  slug: athena-get-data-catalog-output-structure
- name: Athena Get Database Input Structure
  property_count: 0
  slug: athena-get-database-input-structure
- name: Athena Get Database Output Structure
  property_count: 0
  slug: athena-get-database-output-structure
- name: Athena Get Named Query Input Structure
  property_count: 0
  slug: athena-get-named-query-input-structure
- name: Athena Get Named Query Output Structure
  property_count: 0
  slug: athena-get-named-query-output-structure
- name: Athena Get Prepared Statement Input Structure
  property_count: 0
  slug: athena-get-prepared-statement-input-structure
- name: Athena Get Prepared Statement Output Structure
  property_count: 0
  slug: athena-get-prepared-statement-output-structure
- name: Athena Get Query Execution Input Structure
  property_count: 0
  slug: athena-get-query-execution-input-structure
- name: Athena Get Query Execution Output Structure
  property_count: 0
  slug: athena-get-query-execution-output-structure
- name: Athena Get Query Results Input Structure
  property_count: 0
  slug: athena-get-query-results-input-structure
- name: Athena Get Query Results Output Structure
  property_count: 0
  slug: athena-get-query-results-output-structure
- name: Athena Get Query Runtime Statistics Input Structure
  property_count: 0
  slug: athena-get-query-runtime-statistics-input-structure
- name: Athena Get Query Runtime Statistics Output Structure
  property_count: 0
  slug: athena-get-query-runtime-statistics-output-structure
- name: Athena Get Table Metadata Input Structure
  property_count: 0
  slug: athena-get-table-metadata-input-structure
- name: Athena Get Table Metadata Output Structure
  property_count: 0
  slug: athena-get-table-metadata-output-structure
- name: Athena Get Work Group Input Structure
  property_count: 0
  slug: athena-get-work-group-input-structure
- name: Athena Get Work Group Output Structure
  property_count: 0
  slug: athena-get-work-group-output-structure
- name: Athena List Data Catalogs Input Structure
  property_count: 0
  slug: athena-list-data-catalogs-input-structure
- name: Athena List Data Catalogs Output Structure
  property_count: 0
  slug: athena-list-data-catalogs-output-structure
- name: Athena List Databases Input Structure
  property_count: 0
  slug: athena-list-databases-input-structure
- name: Athena List Databases Output Structure
  property_count: 0
  slug: athena-list-databases-output-structure
- name: Athena List Named Queries Input Structure
  property_count: 0
  slug: athena-list-named-queries-input-structure
- name: Athena List Named Queries Output Structure
  property_count: 0
  slug: athena-list-named-queries-output-structure
- name: Athena List Prepared Statements Input Structure
  property_count: 0
  slug: athena-list-prepared-statements-input-structure
- name: Athena List Prepared Statements Output Structure
  property_count: 0
  slug: athena-list-prepared-statements-output-structure
- name: Athena List Query Executions Input Structure
  property_count: 0
  slug: athena-list-query-executions-input-structure
- name: Athena List Query Executions Output Structure
  property_count: 0
  slug: athena-list-query-executions-output-structure
- name: Athena List Table Metadata Input Structure
  property_count: 0
  slug: athena-list-table-metadata-input-structure
- name: Athena List Table Metadata Output Structure
  property_count: 0
  slug: athena-list-table-metadata-output-structure
- name: Athena List Tags For Resource Input Structure
  property_count: 0
  slug: athena-list-tags-for-resource-input-structure
- name: Athena List Tags For Resource Output Structure
  property_count: 0
  slug: athena-list-tags-for-resource-output-structure
- name: Athena List Work Groups Input Structure
  property_count: 0
  slug: athena-list-work-groups-input-structure
- name: Athena List Work Groups Output Structure
  property_count: 0
  slug: athena-list-work-groups-output-structure
- name: Athena Named Query Structure
  property_count: 0
  slug: athena-named-query-structure
- name: Athena Prepared Statement Structure
  property_count: 0
  slug: athena-prepared-statement-structure
- name: Athena Prepared Statement Summary Structure
  property_count: 0
  slug: athena-prepared-statement-summary-structure
- name: Athena Query Execution Context Structure
  property_count: 0
  slug: athena-query-execution-context-structure
- name: Athena Query Execution Statistics Structure
  property_count: 0
  slug: athena-query-execution-statistics-structure
- name: Athena Query Execution Status Structure
  property_count: 0
  slug: athena-query-execution-status-structure
- name: Athena Query Execution Structure
  property_count: 0
  slug: athena-query-execution-structure
- name: Athena Query Runtime Statistics Rows Structure
  property_count: 0
  slug: athena-query-runtime-statistics-rows-structure
- name: Athena Query Runtime Statistics Structure
  property_count: 0
  slug: athena-query-runtime-statistics-structure
- name: Athena Query Runtime Statistics Timeline Structure
  property_count: 0
  slug: athena-query-runtime-statistics-timeline-structure
- name: Athena Query Stage Plan Node Structure
  property_count: 0
  slug: athena-query-stage-plan-node-structure
- name: Athena Query Stage Structure
  property_count: 0
  slug: athena-query-stage-structure
- name: Athena Result Configuration Structure
  property_count: 0
  slug: athena-result-configuration-structure
- name: Athena Result Configuration Updates Structure
  property_count: 0
  slug: athena-result-configuration-updates-structure
- name: Athena Result Set Metadata Structure
  property_count: 0
  slug: athena-result-set-metadata-structure
- name: Athena Result Set Structure
  property_count: 0
  slug: athena-result-set-structure
- name: Athena Row Structure
  property_count: 0
  slug: athena-row-structure
- name: Athena Start Query Execution Input Structure
  property_count: 0
  slug: athena-start-query-execution-input-structure
- name: Athena Start Query Execution Output Structure
  property_count: 0
  slug: athena-start-query-execution-output-structure
- name: Athena Stop Query Execution Input Structure
  property_count: 0
  slug: athena-stop-query-execution-input-structure
- name: Athena Stop Query Execution Output Structure
  property_count: 0
  slug: athena-stop-query-execution-output-structure
- name: Athena Table Metadata Structure
  property_count: 0
  slug: athena-table-metadata-structure
- name: Athena Tag Resource Input Structure
  property_count: 0
  slug: athena-tag-resource-input-structure
- name: Athena Tag Resource Output Structure
  property_count: 0
  slug: athena-tag-resource-output-structure
- name: Athena Tag Structure
  property_count: 0
  slug: athena-tag-structure
- name: Athena Unprocessed Named Query Id Structure
  property_count: 0
  slug: athena-unprocessed-named-query-id-structure
- name: Athena Unprocessed Query Execution Id Structure
  property_count: 0
  slug: athena-unprocessed-query-execution-id-structure
- name: Athena Untag Resource Input Structure
  property_count: 0
  slug: athena-untag-resource-input-structure
- name: Athena Untag Resource Output Structure
  property_count: 0
  slug: athena-untag-resource-output-structure
- name: Athena Update Work Group Input Structure
  property_count: 0
  slug: athena-update-work-group-input-structure
- name: Athena Update Work Group Output Structure
  property_count: 0
  slug: athena-update-work-group-output-structure
- name: Athena Work Group Configuration Structure
  property_count: 0
  slug: athena-work-group-configuration-structure
- name: Athena Work Group Configuration Updates Structure
  property_count: 0
  slug: athena-work-group-configuration-updates-structure
- name: Athena Work Group Structure
  property_count: 0
  slug: athena-work-group-structure
- name: Athena Work Group Summary Structure
  property_count: 0
  slug: athena-work-group-summary-structure
jsonld:
- class_count: 11
  name: Amazon Athena Context
  property_count: 0
  slug: amazon-athena-context
layout: provider
modified: '2026-05-19'
name: Amazon Athena
nav: Providers
network: true
overview: 'Amazon Athena publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Data Catalogs API, Databases API, Named Queries API, and 5 more. Tagged areas include Amazon Athena, SQL, Analytics, and Serverless.


  The Amazon Athena catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Amazon Athena''s developer surface includes authentication and 3 more developer resources.'
plans:
- name: Amazon Athena Plans Pricing
  plan_count: 1
  slug: amazon-athena-plans-pricing
random_paper: 124
rate_limits:
- limit_count: 2
  name: Amazon Athena Rate Limits
  slug: amazon-athena-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: Amazon Athena API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: amazon-athena-jsonschema-spectral-rules
- effective_rule_count: 67
  extends:
  - spectral:oas
  name: Amazon Athena API Rules
  rule_count: 26
  severity_counts:
    error: 13
    hint: 0
    info: 0
    warn: 13
  slug: amazon-athena-spectral-rules
score:
  band: thin
  composite: 36.9
  delta: -6.3
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 9.8
    contract_quality: 73.4
    developer_ergonomics: 11.9
    discoverability: 64.8
    governance: 9.8
    operational_transparency: 21.1
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
  previous_composite: 43.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/amazon-athena/refs/heads/main/screenshots/amazon-athena-2026-06-20T171608.png
security:
- kind: authentication
  name: Amazon Athena Authentication
  slug: amazon-athena-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Amazon Athena Domain Security
  slug: amazon-athena-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amazon Athena Vulnerability Disclosure
  slug: amazon-athena-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: amazon-athena
tags:
- Amazon Athena
- SQL
- Analytics
- Serverless
use_cases:
- Analyze log files and clickstream data stored in S3
- Run ad-hoc SQL queries on data lake without ETL
- Build serverless data pipelines and reporting solutions
- Query AWS service logs including CloudTrail, ELB, and VPC Flow Logs
- Perform cost analysis on AWS Cost and Usage Reports
- Enable self-service analytics for business intelligence teams
---
