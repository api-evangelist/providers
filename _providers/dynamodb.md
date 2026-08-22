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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 37.2
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 28
  human_in_the_loop: 1
  name: Dynamodb Agentic Access
  operation_count: 28
  slug: dynamodb-agentic-access
  summary_line: 28 operations · 28 acting · 1 human-in-the-loop
api_count: 14
apis:
- description: API for capturing and processing change data from DynamoDB tables in near real-time, providing time-ordered sequences of item-level modifications.
  name: Amazon DynamoDB Streams API
  slug: amazon-dynamodb-streams-api
- description: Operations for creating, describing, listing, and deleting on-demand backups
  name: Amazon DynamoDB Backups API
  slug: dynamodb-backups-api
- description: Operations for reading and writing multiple items in batch
  name: Amazon DynamoDB Batch Operations API
  slug: dynamodb-batch-operations-api
- description: Operations for exporting table data to Amazon S3
  name: Amazon DynamoDB Exports API
  slug: dynamodb-exports-api
- description: Operations for importing data from Amazon S3 into DynamoDB tables
  name: Amazon DynamoDB Imports API
  slug: dynamodb-imports-api
- description: Operations for reading and writing individual items in DynamoDB tables
  name: Amazon DynamoDB Items API
  slug: dynamodb-items-api
- description: 'The #ListTagsOfResource API from Amazon DynamoDB — 1 operation(s) for #listtagsofresource.'
  name: 'Amazon DynamoDB #ListTagsOfResource API'
  slug: dynamodb-listtagsofresource-api
- description: Execute SQL-compatible PartiQL statements against DynamoDB tables
  name: Amazon DynamoDB PartiQL API
  slug: dynamodb-partiql-api
- description: Operations for querying and scanning items in DynamoDB tables
  name: Amazon DynamoDB Queries API
  slug: dynamodb-queries-api
- description: Operations for creating, describing, updating, listing, and deleting DynamoDB tables
  name: Amazon DynamoDB Tables API
  slug: dynamodb-tables-api
- description: 'The #TagResource API from Amazon DynamoDB — 1 operation(s) for #tagresource.'
  name: 'Amazon DynamoDB #TagResource API'
  slug: dynamodb-tagresource-api
- description: Transactional read and write operations across multiple items and tables
  name: Amazon DynamoDB Transactions API
  slug: dynamodb-transactions-api
- description: Time to Live configuration for automatic item expiration
  name: Amazon DynamoDB TTL API
  slug: dynamodb-ttl-api
- description: 'The #UntagResource API from Amazon DynamoDB — 1 operation(s) for #untagresource.'
  name: 'Amazon DynamoDB #UntagResource API'
  slug: dynamodb-untagresource-api
artifact_total: 261
asyncapis:
- description: Amazon DynamoDB Streams captures a time-ordered sequence of item-level modifications in any DynamoDB table and stores this information in a log for up to 24 hours. Applications can access this log and
  name: Amazon DynamoDB Streams
  slug: dynamodb-streams-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Amazon DynamoDB Backups API
  slug: open-dynamodb-backups-api
- collection_type: open
  name: Amazon DynamoDB Backups Batch Operations API
  slug: open-dynamodb-batch-operations-api
- collection_type: open
  name: Amazon DynamoDB Backups Exports API
  slug: open-dynamodb-exports-api
- collection_type: open
  name: Amazon DynamoDB Backups Imports API
  slug: open-dynamodb-imports-api
- collection_type: open
  name: Amazon DynamoDB Backups Items API
  slug: open-dynamodb-items-api
- collection_type: open
  name: 'Amazon DynamoDB Backups #ListTagsOfResource API'
  slug: open-dynamodb-listtagsofresource-api
- collection_type: open
  name: Amazon DynamoDB Backups PartiQL API
  slug: open-dynamodb-partiql-api
- collection_type: open
  name: Amazon DynamoDB Backups Queries API
  slug: open-dynamodb-queries-api
- collection_type: open
  name: Amazon DynamoDB Backups Tables API
  slug: open-dynamodb-tables-api
- collection_type: open
  name: 'Amazon DynamoDB Backups #TagResource API'
  slug: open-dynamodb-tagresource-api
- collection_type: open
  name: Amazon DynamoDB Backups Transactions API
  slug: open-dynamodb-transactions-api
- collection_type: open
  name: Amazon DynamoDB Backups TTL API
  slug: open-dynamodb-ttl-api
- collection_type: open
  name: 'Amazon DynamoDB Backups #UntagResource API'
  slug: open-dynamodb-untagresource-api
- collection_type: open
  name: Amazon DynamoDB API
  slug: open-dynamodb
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/dynamodb-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/dynamodb-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/dynamodb-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dynamodb-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/dynamodb-authentication.yml
- group: company
  title: ''
  type: Blog
  url: https://aws.amazon.com/blogs/database/category/database/amazon-dynamodb/
- group: operate
  title: ''
  type: Support
  url: https://aws.amazon.com/premiumsupport/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aws.amazon.com/service-terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aws.amazon.com/privacy/
- group: other
  title: ''
  type: Resources
  url: https://aws.amazon.com/dynamodb/resources/
- group: design
  title: ''
  type: SpectralRules
  url: rules/dynamodb-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/dynamodb-vocabulary.yaml
created: '2024'
description: A fully managed NoSQL database service that provides fast and predictable performance with seamless scalability.
examples:
- key_count: 2
  name: Dynamodb Attribute Definition Example
  slug: dynamodb-attribute-definition-example
- key_count: 10
  name: Dynamodb Attribute Value Example
  slug: dynamodb-attribute-value-example
- key_count: 2
  name: Dynamodb Batch Execute Statement Input Example
  slug: dynamodb-batch-execute-statement-input-example
- key_count: 2
  name: Dynamodb Batch Execute Statement Output Example
  slug: dynamodb-batch-execute-statement-output-example
- key_count: 2
  name: Dynamodb Batch Get Item Input Example
  slug: dynamodb-batch-get-item-input-example
- key_count: 3
  name: Dynamodb Batch Get Item Output Example
  slug: dynamodb-batch-get-item-output-example
- key_count: 3
  name: Dynamodb Batch Write Item Input Example
  slug: dynamodb-batch-write-item-input-example
- key_count: 3
  name: Dynamodb Batch Write Item Output Example
  slug: dynamodb-batch-write-item-output-example
- key_count: 7
  name: Dynamodb Consumed Capacity Example
  slug: dynamodb-consumed-capacity-example
- key_count: 2
  name: Dynamodb Create Backup Input Example
  slug: dynamodb-create-backup-input-example
- key_count: 1
  name: Dynamodb Create Backup Output Example
  slug: dynamodb-create-backup-output-example
- key_count: 9
  name: Dynamodb Create Table Input Example
  slug: dynamodb-create-table-input-example
- key_count: 0
  name: Dynamodb Create Table Output Example
  slug: dynamodb-create-table-output-example
- key_count: 7
  name: Dynamodb Delete Item Input Example
  slug: dynamodb-delete-item-input-example
- key_count: 1
  name: Dynamodb Delete Item Output Example
  slug: dynamodb-delete-item-output-example
- key_count: 1
  name: Dynamodb Delete Table Input Example
  slug: dynamodb-delete-table-input-example
- key_count: 0
  name: Dynamodb Delete Table Output Example
  slug: dynamodb-delete-table-output-example
- key_count: 1
  name: Dynamodb Describe Continuous Backups Input Example
  slug: dynamodb-describe-continuous-backups-input-example
- key_count: 1
  name: Dynamodb Describe Continuous Backups Output Example
  slug: dynamodb-describe-continuous-backups-output-example
- key_count: 1
  name: Dynamodb Describe Table Input Example
  slug: dynamodb-describe-table-input-example
- key_count: 0
  name: Dynamodb Describe Table Output Example
  slug: dynamodb-describe-table-output-example
- key_count: 1
  name: Dynamodb Describe Time To Live Input Example
  slug: dynamodb-describe-time-to-live-input-example
- key_count: 1
  name: Dynamodb Describe Time To Live Output Example
  slug: dynamodb-describe-time-to-live-output-example
- key_count: 3
  name: Dynamodb Error Response Example
  slug: dynamodb-error-response-example
- key_count: 6
  name: Dynamodb Execute Statement Input Example
  slug: dynamodb-execute-statement-input-example
- key_count: 3
  name: Dynamodb Execute Statement Output Example
  slug: dynamodb-execute-statement-output-example
- key_count: 3
  name: Dynamodb Execute Transaction Input Example
  slug: dynamodb-execute-transaction-input-example
- key_count: 2
  name: Dynamodb Execute Transaction Output Example
  slug: dynamodb-execute-transaction-output-example
- key_count: 9
  name: Dynamodb Export Table To Point In Time Input Example
  slug: dynamodb-export-table-to-point-in-time-input-example
- key_count: 1
  name: Dynamodb Export Table To Point In Time Output Example
  slug: dynamodb-export-table-to-point-in-time-output-example
- key_count: 6
  name: Dynamodb Get Item Input Example
  slug: dynamodb-get-item-input-example
- key_count: 1
  name: Dynamodb Get Item Output Example
  slug: dynamodb-get-item-output-example
- key_count: 2
  name: Dynamodb Global Secondary Index Example
  slug: dynamodb-global-secondary-index-example
- key_count: 6
  name: Dynamodb Import Table Input Example
  slug: dynamodb-import-table-input-example
- key_count: 1
  name: Dynamodb Import Table Output Example
  slug: dynamodb-import-table-output-example
- key_count: 2
  name: Dynamodb Item Collection Metrics Example
  slug: dynamodb-item-collection-metrics-example
- key_count: 2
  name: Dynamodb Key Schema Element Example
  slug: dynamodb-key-schema-element-example
- key_count: 6
  name: Dynamodb List Backups Input Example
  slug: dynamodb-list-backups-input-example
- key_count: 2
  name: Dynamodb List Backups Output Example
  slug: dynamodb-list-backups-output-example
- key_count: 2
  name: Dynamodb List Tables Input Example
  slug: dynamodb-list-tables-input-example
- key_count: 2
  name: Dynamodb List Tables Output Example
  slug: dynamodb-list-tables-output-example
- key_count: 2
  name: Dynamodb List Tags Of Resource Input Example
  slug: dynamodb-list-tags-of-resource-input-example
- key_count: 2
  name: Dynamodb List Tags Of Resource Output Example
  slug: dynamodb-list-tags-of-resource-output-example
- key_count: 2
  name: Dynamodb Local Secondary Index Example
  slug: dynamodb-local-secondary-index-example
- key_count: 2
  name: Dynamodb Projection Example
  slug: dynamodb-projection-example
- key_count: 5
  name: Dynamodb Provisioned Throughput Description Example
  slug: dynamodb-provisioned-throughput-description-example
- key_count: 2
  name: Dynamodb Provisioned Throughput Example
  slug: dynamodb-provisioned-throughput-example
- key_count: 8
  name: Dynamodb Put Item Input Example
  slug: dynamodb-put-item-input-example
- key_count: 1
  name: Dynamodb Put Item Output Example
  slug: dynamodb-put-item-output-example
- key_count: 13
  name: Dynamodb Query Input Example
  slug: dynamodb-query-input-example
- key_count: 4
  name: Dynamodb Query Output Example
  slug: dynamodb-query-output-example
- key_count: 13
  name: Dynamodb Scan Input Example
  slug: dynamodb-scan-input-example
- key_count: 4
  name: Dynamodb Scan Output Example
  slug: dynamodb-scan-output-example
- key_count: 3
  name: Dynamodb Sse Specification Example
  slug: dynamodb-sse-specification-example
- key_count: 2
  name: Dynamodb Stream Specification Example
  slug: dynamodb-stream-specification-example
- key_count: 17
  name: Dynamodb Table Description Example
  slug: dynamodb-table-description-example
- key_count: 2
  name: Dynamodb Tag Example
  slug: dynamodb-tag-example
- key_count: 2
  name: Dynamodb Tag Resource Input Example
  slug: dynamodb-tag-resource-input-example
- key_count: 2
  name: Dynamodb Transact Get Items Input Example
  slug: dynamodb-transact-get-items-input-example
- key_count: 2
  name: Dynamodb Transact Get Items Output Example
  slug: dynamodb-transact-get-items-output-example
- key_count: 4
  name: Dynamodb Transact Write Items Input Example
  slug: dynamodb-transact-write-items-input-example
- key_count: 2
  name: Dynamodb Transact Write Items Output Example
  slug: dynamodb-transact-write-items-output-example
- key_count: 2
  name: Dynamodb Untag Resource Input Example
  slug: dynamodb-untag-resource-input-example
- key_count: 9
  name: Dynamodb Update Item Input Example
  slug: dynamodb-update-item-input-example
- key_count: 1
  name: Dynamodb Update Item Output Example
  slug: dynamodb-update-item-output-example
- key_count: 6
  name: Dynamodb Update Table Input Example
  slug: dynamodb-update-table-input-example
- key_count: 0
  name: Dynamodb Update Table Output Example
  slug: dynamodb-update-table-output-example
- key_count: 2
  name: Dynamodb Update Time To Live Input Example
  slug: dynamodb-update-time-to-live-input-example
- key_count: 1
  name: Dynamodb Update Time To Live Output Example
  slug: dynamodb-update-time-to-live-output-example
features:
- description: Consistent low-latency reads and writes at any scale with SSD-backed storage.
  name: Single-Digit Millisecond Performance
- description: Multi-region, multi-active replication for globally distributed applications.
  name: Global Tables
- description: Automatically scale throughput capacity based on workload without capacity planning.
  name: On-Demand Capacity
- description: Capture item-level changes for real-time processing, replication, and event-driven architectures.
  name: DynamoDB Streams
- description: Continuous backups with restore to any second within the last 35 days.
  name: Point-in-Time Recovery
- description: ACID transactions across multiple items and tables for complex business logic.
  name: Transactions
- description: Execute SQL-compatible queries against DynamoDB tables using PartiQL language.
  name: PartiQL Support
finops:
- name: Dynamodb Finops
  service_category: Database
  slug: dynamodb-finops
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
json_schemas:
- name: AttributeDefinition
  property_count: 2
  slug: dynamodb-attribute-definition
- name: AttributeValue
  property_count: 10
  slug: dynamodb-attribute-value
- name: BatchExecuteStatementInput
  property_count: 2
  slug: dynamodb-batch-execute-statement-input
- name: BatchExecuteStatementOutput
  property_count: 2
  slug: dynamodb-batch-execute-statement-output
- name: BatchGetItemInput
  property_count: 2
  slug: dynamodb-batch-get-item-input
- name: BatchGetItemOutput
  property_count: 3
  slug: dynamodb-batch-get-item-output
- name: BatchWriteItemInput
  property_count: 3
  slug: dynamodb-batch-write-item-input
- name: BatchWriteItemOutput
  property_count: 3
  slug: dynamodb-batch-write-item-output
- name: ConsumedCapacity
  property_count: 7
  slug: dynamodb-consumed-capacity
- name: CreateBackupInput
  property_count: 2
  slug: dynamodb-create-backup-input
- name: CreateBackupOutput
  property_count: 1
  slug: dynamodb-create-backup-output
- name: CreateTableInput
  property_count: 9
  slug: dynamodb-create-table-input
- name: CreateTableOutput
  property_count: 0
  slug: dynamodb-create-table-output
- name: DeleteItemInput
  property_count: 7
  slug: dynamodb-delete-item-input
- name: DeleteItemOutput
  property_count: 1
  slug: dynamodb-delete-item-output
- name: DeleteTableInput
  property_count: 1
  slug: dynamodb-delete-table-input
- name: DeleteTableOutput
  property_count: 0
  slug: dynamodb-delete-table-output
- name: DescribeContinuousBackupsInput
  property_count: 1
  slug: dynamodb-describe-continuous-backups-input
- name: DescribeContinuousBackupsOutput
  property_count: 1
  slug: dynamodb-describe-continuous-backups-output
- name: DescribeTableInput
  property_count: 1
  slug: dynamodb-describe-table-input
- name: DescribeTableOutput
  property_count: 0
  slug: dynamodb-describe-table-output
- name: DescribeTimeToLiveInput
  property_count: 1
  slug: dynamodb-describe-time-to-live-input
- name: DescribeTimeToLiveOutput
  property_count: 1
  slug: dynamodb-describe-time-to-live-output
- name: ErrorResponse
  property_count: 3
  slug: dynamodb-error-response
- name: ExecuteStatementInput
  property_count: 6
  slug: dynamodb-execute-statement-input
- name: ExecuteStatementOutput
  property_count: 3
  slug: dynamodb-execute-statement-output
- name: ExecuteTransactionInput
  property_count: 3
  slug: dynamodb-execute-transaction-input
- name: ExecuteTransactionOutput
  property_count: 2
  slug: dynamodb-execute-transaction-output
- name: ExportTableToPointInTimeInput
  property_count: 9
  slug: dynamodb-export-table-to-point-in-time-input
- name: ExportTableToPointInTimeOutput
  property_count: 1
  slug: dynamodb-export-table-to-point-in-time-output
- name: GetItemInput
  property_count: 6
  slug: dynamodb-get-item-input
- name: GetItemOutput
  property_count: 1
  slug: dynamodb-get-item-output
- name: GlobalSecondaryIndex
  property_count: 2
  slug: dynamodb-global-secondary-index
- name: ImportTableInput
  property_count: 6
  slug: dynamodb-import-table-input
- name: ImportTableOutput
  property_count: 1
  slug: dynamodb-import-table-output
- name: ItemCollectionMetrics
  property_count: 2
  slug: dynamodb-item-collection-metrics
- name: Amazon DynamoDB Item Schema
  property_count: 4
  slug: dynamodb-item
- name: KeySchemaElement
  property_count: 2
  slug: dynamodb-key-schema-element
- name: ListBackupsInput
  property_count: 6
  slug: dynamodb-list-backups-input
- name: ListBackupsOutput
  property_count: 2
  slug: dynamodb-list-backups-output
- name: ListTablesInput
  property_count: 2
  slug: dynamodb-list-tables-input
- name: ListTablesOutput
  property_count: 2
  slug: dynamodb-list-tables-output
- name: ListTagsOfResourceInput
  property_count: 2
  slug: dynamodb-list-tags-of-resource-input
- name: ListTagsOfResourceOutput
  property_count: 2
  slug: dynamodb-list-tags-of-resource-output
- name: LocalSecondaryIndex
  property_count: 2
  slug: dynamodb-local-secondary-index
- name: Projection
  property_count: 2
  slug: dynamodb-projection
- name: ProvisionedThroughputDescription
  property_count: 5
  slug: dynamodb-provisioned-throughput-description
- name: ProvisionedThroughput
  property_count: 2
  slug: dynamodb-provisioned-throughput
- name: PutItemInput
  property_count: 8
  slug: dynamodb-put-item-input
- name: PutItemOutput
  property_count: 1
  slug: dynamodb-put-item-output
- name: QueryInput
  property_count: 13
  slug: dynamodb-query-input
- name: QueryOutput
  property_count: 4
  slug: dynamodb-query-output
- name: ScanInput
  property_count: 13
  slug: dynamodb-scan-input
- name: ScanOutput
  property_count: 4
  slug: dynamodb-scan-output
- name: SSESpecification
  property_count: 3
  slug: dynamodb-sse-specification
- name: StreamSpecification
  property_count: 2
  slug: dynamodb-stream-specification
- name: TableDescription
  property_count: 17
  slug: dynamodb-table-description
- name: TagResourceInput
  property_count: 2
  slug: dynamodb-tag-resource-input
- name: Tag
  property_count: 2
  slug: dynamodb-tag
- name: TransactGetItemsInput
  property_count: 2
  slug: dynamodb-transact-get-items-input
- name: TransactGetItemsOutput
  property_count: 2
  slug: dynamodb-transact-get-items-output
- name: TransactWriteItemsInput
  property_count: 4
  slug: dynamodb-transact-write-items-input
- name: TransactWriteItemsOutput
  property_count: 2
  slug: dynamodb-transact-write-items-output
- name: UntagResourceInput
  property_count: 2
  slug: dynamodb-untag-resource-input
- name: UpdateItemInput
  property_count: 9
  slug: dynamodb-update-item-input
- name: UpdateItemOutput
  property_count: 1
  slug: dynamodb-update-item-output
- name: UpdateTableInput
  property_count: 6
  slug: dynamodb-update-table-input
- name: UpdateTableOutput
  property_count: 0
  slug: dynamodb-update-table-output
- name: UpdateTimeToLiveInput
  property_count: 2
  slug: dynamodb-update-time-to-live-input
- name: UpdateTimeToLiveOutput
  property_count: 1
  slug: dynamodb-update-time-to-live-output
json_structures:
- name: Dynamodb Attribute Definition Structure
  property_count: 2
  slug: dynamodb-attribute-definition-structure
- name: Dynamodb Attribute Value Structure
  property_count: 10
  slug: dynamodb-attribute-value-structure
- name: Dynamodb Batch Execute Statement Input Structure
  property_count: 2
  slug: dynamodb-batch-execute-statement-input-structure
- name: Dynamodb Batch Execute Statement Output Structure
  property_count: 2
  slug: dynamodb-batch-execute-statement-output-structure
- name: Dynamodb Batch Get Item Input Structure
  property_count: 2
  slug: dynamodb-batch-get-item-input-structure
- name: Dynamodb Batch Get Item Output Structure
  property_count: 3
  slug: dynamodb-batch-get-item-output-structure
- name: Dynamodb Batch Write Item Input Structure
  property_count: 3
  slug: dynamodb-batch-write-item-input-structure
- name: Dynamodb Batch Write Item Output Structure
  property_count: 3
  slug: dynamodb-batch-write-item-output-structure
- name: Dynamodb Consumed Capacity Structure
  property_count: 7
  slug: dynamodb-consumed-capacity-structure
- name: Dynamodb Create Backup Input Structure
  property_count: 2
  slug: dynamodb-create-backup-input-structure
- name: Dynamodb Create Backup Output Structure
  property_count: 1
  slug: dynamodb-create-backup-output-structure
- name: Dynamodb Create Table Input Structure
  property_count: 9
  slug: dynamodb-create-table-input-structure
- name: Dynamodb Create Table Output Structure
  property_count: 0
  slug: dynamodb-create-table-output-structure
- name: Dynamodb Delete Item Input Structure
  property_count: 7
  slug: dynamodb-delete-item-input-structure
- name: Dynamodb Delete Item Output Structure
  property_count: 1
  slug: dynamodb-delete-item-output-structure
- name: Dynamodb Delete Table Input Structure
  property_count: 1
  slug: dynamodb-delete-table-input-structure
- name: Dynamodb Delete Table Output Structure
  property_count: 0
  slug: dynamodb-delete-table-output-structure
- name: Dynamodb Describe Continuous Backups Input Structure
  property_count: 1
  slug: dynamodb-describe-continuous-backups-input-structure
- name: Dynamodb Describe Continuous Backups Output Structure
  property_count: 1
  slug: dynamodb-describe-continuous-backups-output-structure
- name: Dynamodb Describe Table Input Structure
  property_count: 1
  slug: dynamodb-describe-table-input-structure
- name: Dynamodb Describe Table Output Structure
  property_count: 0
  slug: dynamodb-describe-table-output-structure
- name: Dynamodb Describe Time To Live Input Structure
  property_count: 1
  slug: dynamodb-describe-time-to-live-input-structure
- name: Dynamodb Describe Time To Live Output Structure
  property_count: 1
  slug: dynamodb-describe-time-to-live-output-structure
- name: Dynamodb Error Response Structure
  property_count: 3
  slug: dynamodb-error-response-structure
- name: Dynamodb Execute Statement Input Structure
  property_count: 6
  slug: dynamodb-execute-statement-input-structure
- name: Dynamodb Execute Statement Output Structure
  property_count: 3
  slug: dynamodb-execute-statement-output-structure
- name: Dynamodb Execute Transaction Input Structure
  property_count: 3
  slug: dynamodb-execute-transaction-input-structure
- name: Dynamodb Execute Transaction Output Structure
  property_count: 2
  slug: dynamodb-execute-transaction-output-structure
- name: Dynamodb Export Table To Point In Time Input Structure
  property_count: 9
  slug: dynamodb-export-table-to-point-in-time-input-structure
- name: Dynamodb Export Table To Point In Time Output Structure
  property_count: 1
  slug: dynamodb-export-table-to-point-in-time-output-structure
- name: Dynamodb Get Item Input Structure
  property_count: 6
  slug: dynamodb-get-item-input-structure
- name: Dynamodb Get Item Output Structure
  property_count: 1
  slug: dynamodb-get-item-output-structure
- name: Dynamodb Global Secondary Index Structure
  property_count: 2
  slug: dynamodb-global-secondary-index-structure
- name: Dynamodb Import Table Input Structure
  property_count: 6
  slug: dynamodb-import-table-input-structure
- name: Dynamodb Import Table Output Structure
  property_count: 1
  slug: dynamodb-import-table-output-structure
- name: Dynamodb Item Collection Metrics Structure
  property_count: 2
  slug: dynamodb-item-collection-metrics-structure
- name: Dynamodb Key Schema Element Structure
  property_count: 2
  slug: dynamodb-key-schema-element-structure
- name: Dynamodb List Backups Input Structure
  property_count: 6
  slug: dynamodb-list-backups-input-structure
- name: Dynamodb List Backups Output Structure
  property_count: 2
  slug: dynamodb-list-backups-output-structure
- name: Dynamodb List Tables Input Structure
  property_count: 2
  slug: dynamodb-list-tables-input-structure
- name: Dynamodb List Tables Output Structure
  property_count: 2
  slug: dynamodb-list-tables-output-structure
- name: Dynamodb List Tags Of Resource Input Structure
  property_count: 2
  slug: dynamodb-list-tags-of-resource-input-structure
- name: Dynamodb List Tags Of Resource Output Structure
  property_count: 2
  slug: dynamodb-list-tags-of-resource-output-structure
- name: Dynamodb Local Secondary Index Structure
  property_count: 2
  slug: dynamodb-local-secondary-index-structure
- name: Dynamodb Projection Structure
  property_count: 2
  slug: dynamodb-projection-structure
- name: Dynamodb Provisioned Throughput Description Structure
  property_count: 5
  slug: dynamodb-provisioned-throughput-description-structure
- name: Dynamodb Provisioned Throughput Structure
  property_count: 2
  slug: dynamodb-provisioned-throughput-structure
- name: Dynamodb Put Item Input Structure
  property_count: 8
  slug: dynamodb-put-item-input-structure
- name: Dynamodb Put Item Output Structure
  property_count: 1
  slug: dynamodb-put-item-output-structure
- name: Dynamodb Query Input Structure
  property_count: 13
  slug: dynamodb-query-input-structure
- name: Dynamodb Query Output Structure
  property_count: 4
  slug: dynamodb-query-output-structure
- name: Dynamodb Scan Input Structure
  property_count: 13
  slug: dynamodb-scan-input-structure
- name: Dynamodb Scan Output Structure
  property_count: 4
  slug: dynamodb-scan-output-structure
- name: Dynamodb Sse Specification Structure
  property_count: 3
  slug: dynamodb-sse-specification-structure
- name: Dynamodb Stream Specification Structure
  property_count: 2
  slug: dynamodb-stream-specification-structure
- name: Dynamodb Table Description Structure
  property_count: 17
  slug: dynamodb-table-description-structure
- name: Dynamodb Tag Resource Input Structure
  property_count: 2
  slug: dynamodb-tag-resource-input-structure
- name: Dynamodb Tag Structure
  property_count: 2
  slug: dynamodb-tag-structure
- name: Dynamodb Transact Get Items Input Structure
  property_count: 2
  slug: dynamodb-transact-get-items-input-structure
- name: Dynamodb Transact Get Items Output Structure
  property_count: 2
  slug: dynamodb-transact-get-items-output-structure
- name: Dynamodb Transact Write Items Input Structure
  property_count: 4
  slug: dynamodb-transact-write-items-input-structure
- name: Dynamodb Transact Write Items Output Structure
  property_count: 2
  slug: dynamodb-transact-write-items-output-structure
- name: Dynamodb Untag Resource Input Structure
  property_count: 2
  slug: dynamodb-untag-resource-input-structure
- name: Dynamodb Update Item Input Structure
  property_count: 9
  slug: dynamodb-update-item-input-structure
- name: Dynamodb Update Item Output Structure
  property_count: 1
  slug: dynamodb-update-item-output-structure
- name: Dynamodb Update Table Input Structure
  property_count: 6
  slug: dynamodb-update-table-input-structure
- name: Dynamodb Update Table Output Structure
  property_count: 0
  slug: dynamodb-update-table-output-structure
- name: Dynamodb Update Time To Live Input Structure
  property_count: 2
  slug: dynamodb-update-time-to-live-input-structure
- name: Dynamodb Update Time To Live Output Structure
  property_count: 1
  slug: dynamodb-update-time-to-live-output-structure
jsonld:
- class_count: 0
  name: Dynamodb Context
  property_count: 0
  slug: dynamodb-context
layout: provider
modified: '2026-05-19'
name: Amazon DynamoDB
nav: Providers
network: true
overview: 'Amazon DynamoDB publishes 14 APIs on the [APIs.io](https://apis.io/) network, including Streams API, Backups API, Batch Operations API, and 11 more. Tagged areas include Cloud, Database, Document Store, Key-Value, and Managed Service.


  The Amazon DynamoDB catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 3 Spectral governance rulesets.


  Amazon DynamoDB''s developer surface includes authentication, engineering blog, support, and 9 more developer resources.'
plans:
- name: Dynamodb Plans Pricing
  plan_count: 4
  slug: dynamodb-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 11
  name: Dynamodb Rate Limits
  slug: dynamodb-rate-limits
rules:
- effective_rule_count: 35
  extends:
  - spectral:asyncapi
  name: Amazon DynamoDB API Rules
  rule_count: 8
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 6
  slug: dynamodb-asyncapi-spectral-rules
- effective_rule_count: 6
  extends: []
  name: Amazon DynamoDB API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: dynamodb-jsonschema-spectral-rules
- effective_rule_count: 56
  extends:
  - spectral:oas
  name: Amazon DynamoDB API Rules
  rule_count: 15
  severity_counts:
    error: 8
    hint: 0
    info: 0
    warn: 7
  slug: dynamodb-spectral-rules
score:
  band: developing
  composite: 43.0
  delta: -3.9
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 28.8
    contract_quality: 74.1
    developer_ergonomics: 19.0
    discoverability: 72.2
    governance: 28.8
    operational_transparency: 7.9
  previous_composite: 46.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 13
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dynamodb/refs/heads/main/screenshots/dynamodb-2026-06-20T180405.png
security:
- kind: authentication
  name: Dynamodb Authentication
  slug: dynamodb-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Dynamodb Domain Security
  slug: dynamodb-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Dynamodb Vulnerability Disclosure
  slug: dynamodb-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Dynamodb Trust Center
  slug: dynamodb-trust-center
  summary_line: PCI DSS, HIPAA, FedRAMP, GDPR, FIPS 140
slug: dynamodb
tags:
- Cloud
- Database
- Document Store
- Key-Value
- Managed Service
- NoSQL
- Serverless
use_cases:
- description: Use as the data layer for serverless architectures with Lambda and API Gateway.
  name: Serverless Application Backend
- description: Store and query player data, session state, and leaderboards with consistent low latency.
  name: Gaming Leaderboards
- description: Ingest and query high-volume time-series data from IoT devices at scale.
  name: IoT Data Storage
- description: Store shopping cart and session data with high availability and automatic scaling.
  name: E-Commerce Shopping Cart
website: https://aws.amazon.com/dynamodb/
---
