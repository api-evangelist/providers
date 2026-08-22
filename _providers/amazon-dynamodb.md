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
- acting_count: 15
  human_in_the_loop: 0
  name: Amazon Dynamodb Agentic Access
  operation_count: 15
  slug: amazon-dynamodb-agentic-access
  summary_line: 15 operations · 15 acting
api_count: 5
apis:
- description: Operations for batch reading and writing multiple items
  name: Amazon DynamoDB Batch API
  slug: amazon-dynamodb-batch-api
- description: Operations for putting, getting, updating, and deleting individual items
  name: Amazon DynamoDB Items API
  slug: amazon-dynamodb-items-api
- description: Operations for querying and scanning table data
  name: Amazon DynamoDB Queries API
  slug: amazon-dynamodb-queries-api
- description: Operations for creating, describing, updating, listing, and deleting DynamoDB tables
  name: Amazon DynamoDB Tables API
  slug: amazon-dynamodb-tables-api
- description: Operations for transactional reads and writes across multiple items
  name: Amazon DynamoDB Transactions API
  slug: amazon-dynamodb-transactions-api
arazzos:
- description: Bulk-write a set of items and read them back in a single batch.
  name: Amazon DynamoDB Batch Write Then Batch Get
  slug: amazon-dynamodb-batch-write-then-batch-get-workflow
- description: Read an item, then update it only when it already exists.
  name: Amazon DynamoDB Conditional Update of an Existing Item
  slug: amazon-dynamodb-conditional-update-item-workflow
- description: Add a global secondary index to a table and poll until ACTIVE.
  name: Amazon DynamoDB Add a Global Secondary Index and Wait
  slug: amazon-dynamodb-create-index-and-wait-workflow
- description: Scan a table, batch-delete its items, then drop the table.
  name: Amazon DynamoDB Drain and Delete a Table
  slug: amazon-dynamodb-drain-and-delete-table-workflow
- description: Create a table, wait until ACTIVE, write a seed item, then read it back.
  name: Amazon DynamoDB Provision Table and Seed First Item
  slug: amazon-dynamodb-provision-table-and-seed-workflow
- description: Create a DynamoDB table and poll until it becomes ACTIVE.
  name: Amazon DynamoDB Provision a Table
  slug: amazon-dynamodb-provision-table-workflow
- description: Write an item and immediately query the partition it belongs to.
  name: Amazon DynamoDB Put Item Then Query
  slug: amazon-dynamodb-put-then-query-workflow
- description: Scan a table and page through results until the table is exhausted.
  name: Amazon DynamoDB Scan With Pagination
  slug: amazon-dynamodb-scan-paginate-workflow
- description: Atomically write a group of items, then atomically read them back.
  name: Amazon DynamoDB Transactional Write Then Transactional Read
  slug: amazon-dynamodb-transaction-write-then-read-workflow
artifact_total: 151
collections:
- collection_type: postman
  name: Amazon DynamoDB API
  slug: postman-amazon-dynamodb
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Amazon DynamoDB Batch API
  slug: open-amazon-dynamodb-batch-api
- collection_type: open
  name: Amazon DynamoDB Batch Items API
  slug: open-amazon-dynamodb-items-api
- collection_type: open
  name: Amazon DynamoDB Batch Queries API
  slug: open-amazon-dynamodb-queries-api
- collection_type: open
  name: Amazon DynamoDB Batch Tables API
  slug: open-amazon-dynamodb-tables-api
- collection_type: open
  name: Amazon DynamoDB Batch Transactions API
  slug: open-amazon-dynamodb-transactions-api
- collection_type: open
  name: Amazon DynamoDB API
  slug: open-amazon-dynamodb
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/amazon-dynamodb-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/amazon-dynamodb-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-dynamodb-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amazon-dynamodb-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/amazon-dynamodb-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/amazon-dynamodb/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-dynamodb-batch-write-then-batch-get-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-dynamodb-conditional-update-item-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-dynamodb-create-index-and-wait-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-dynamodb-drain-and-delete-table-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-dynamodb-provision-table-and-seed-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-dynamodb-provision-table-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-dynamodb-put-then-query-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-dynamodb-scan-paginate-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-dynamodb-transaction-write-then-read-workflow.yml
- group: start
  title: ''
  type: Portal
  url: https://aws.amazon.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://aws.amazon.com/dynamodb/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/dynamodb/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aws.amazon.com/service-terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aws.amazon.com/privacy/
- group: operate
  title: ''
  type: Support
  url: https://aws.amazon.com/premiumsupport/
- group: company
  title: ''
  type: Blog
  url: https://aws.amazon.com/blogs/database/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- group: start
  title: ''
  type: Console
  url: https://console.aws.amazon.com/dynamodbv2/
- group: start
  title: ''
  type: Signup
  url: https://signin.aws.amazon.com/signup?request_type=register
- group: start
  title: ''
  type: Login
  url: https://aws.amazon.com/console/
- group: operate
  title: ''
  type: StatusPage
  url: https://health.aws.amazon.com/health/status
- group: other
  title: ''
  type: KnowledgeCenter
  url: https://repost.aws/knowledge-center
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/user/AmazonWebServices
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/amazon-dynamodb
- group: operate
  title: ''
  type: Contact
  url: https://aws.amazon.com/contact-us/
- group: auth
  title: ''
  type: Security
  url: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/security.html
- group: auth
  title: ''
  type: Compliance
  url: https://aws.amazon.com/compliance/
- group: design
  title: ''
  type: SpectralRules
  url: rules/amazon-dynamodb-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/amazon-dynamodb-vocabulary.yaml
created: '2024-01-15'
description: Amazon DynamoDB is a fully managed NoSQL database service that provides fast and predictable performance with seamless scalability, allowing you to store and retrieve any amount of data and serve any level of request traffic using key-value and document data models.
examples:
- key_count: 3
  name: Amazon Dynamodb Table Example
  slug: amazon-dynamodb-table-example
- key_count: 2
  name: Dynamodb Openapi Attribute Definition Example
  slug: dynamodb-openapi-attribute-definition-example
- key_count: 3
  name: Dynamodb Openapi Attribute Value Example
  slug: dynamodb-openapi-attribute-value-example
- key_count: 1
  name: Dynamodb Openapi Batch Get Item Input Example
  slug: dynamodb-openapi-batch-get-item-input-example
- key_count: 2
  name: Dynamodb Openapi Batch Get Item Output Example
  slug: dynamodb-openapi-batch-get-item-output-example
- key_count: 1
  name: Dynamodb Openapi Batch Write Item Input Example
  slug: dynamodb-openapi-batch-write-item-input-example
- key_count: 1
  name: Dynamodb Openapi Batch Write Item Output Example
  slug: dynamodb-openapi-batch-write-item-output-example
- key_count: 3
  name: Dynamodb Openapi Create Table Input Example
  slug: dynamodb-openapi-create-table-input-example
- key_count: 1
  name: Dynamodb Openapi Create Table Output Example
  slug: dynamodb-openapi-create-table-output-example
- key_count: 3
  name: Dynamodb Openapi Delete Item Input Example
  slug: dynamodb-openapi-delete-item-input-example
- key_count: 1
  name: Dynamodb Openapi Delete Item Output Example
  slug: dynamodb-openapi-delete-item-output-example
- key_count: 1
  name: Dynamodb Openapi Describe Table Output Example
  slug: dynamodb-openapi-describe-table-output-example
- key_count: 3
  name: Dynamodb Openapi Get Item Input Example
  slug: dynamodb-openapi-get-item-input-example
- key_count: 1
  name: Dynamodb Openapi Get Item Output Example
  slug: dynamodb-openapi-get-item-output-example
- key_count: 3
  name: Dynamodb Openapi Global Secondary Index Example
  slug: dynamodb-openapi-global-secondary-index-example
- key_count: 2
  name: Dynamodb Openapi Key Schema Element Example
  slug: dynamodb-openapi-key-schema-element-example
- key_count: 3
  name: Dynamodb Openapi Local Secondary Index Example
  slug: dynamodb-openapi-local-secondary-index-example
- key_count: 2
  name: Dynamodb Openapi Projection Example
  slug: dynamodb-openapi-projection-example
- key_count: 3
  name: Dynamodb Openapi Provisioned Throughput Description Example
  slug: dynamodb-openapi-provisioned-throughput-description-example
- key_count: 2
  name: Dynamodb Openapi Provisioned Throughput Example
  slug: dynamodb-openapi-provisioned-throughput-example
- key_count: 3
  name: Dynamodb Openapi Put Item Input Example
  slug: dynamodb-openapi-put-item-input-example
- key_count: 1
  name: Dynamodb Openapi Put Item Output Example
  slug: dynamodb-openapi-put-item-output-example
- key_count: 3
  name: Dynamodb Openapi Query Input Example
  slug: dynamodb-openapi-query-input-example
- key_count: 3
  name: Dynamodb Openapi Query Output Example
  slug: dynamodb-openapi-query-output-example
- key_count: 3
  name: Dynamodb Openapi Scan Input Example
  slug: dynamodb-openapi-scan-input-example
- key_count: 3
  name: Dynamodb Openapi Scan Output Example
  slug: dynamodb-openapi-scan-output-example
- key_count: 3
  name: Dynamodb Openapi Table Description Example
  slug: dynamodb-openapi-table-description-example
- key_count: 2
  name: Dynamodb Openapi Tag Example
  slug: dynamodb-openapi-tag-example
- key_count: 1
  name: Dynamodb Openapi Transact Get Items Input Example
  slug: dynamodb-openapi-transact-get-items-input-example
- key_count: 1
  name: Dynamodb Openapi Transact Get Items Output Example
  slug: dynamodb-openapi-transact-get-items-output-example
- key_count: 2
  name: Dynamodb Openapi Transact Write Items Input Example
  slug: dynamodb-openapi-transact-write-items-input-example
- key_count: 1
  name: Dynamodb Openapi Transact Write Items Output Example
  slug: dynamodb-openapi-transact-write-items-output-example
- key_count: 3
  name: Dynamodb Openapi Update Item Input Example
  slug: dynamodb-openapi-update-item-input-example
- key_count: 1
  name: Dynamodb Openapi Update Item Output Example
  slug: dynamodb-openapi-update-item-output-example
- key_count: 3
  name: Dynamodb Openapi Update Table Input Example
  slug: dynamodb-openapi-update-table-input-example
features:
- description: Fully managed, no server provisioning, patching, or capacity management required.
  name: Serverless Architecture
- description: Consistent performance at any scale with single-digit millisecond response times.
  name: Single-Digit Millisecond Performance
- description: Multi-Region, active-active replication with up to 99.999% availability and zero RPO.
  name: Global Tables
- description: On-demand mode automatically adapts to application throughput without capacity planning.
  name: Automatic Scaling
- description: ACID transactions across multiple items and tables with conditional operations.
  name: Transactions
- description: DynamoDB Streams captures a time-ordered sequence of changes to items for event-driven architectures.
  name: Streams
- description: Enables continuous backups with point-in-time recovery to any second over the last 35 days.
  name: Point-in-Time Recovery
- description: Time to Live automatically deletes expired items to reduce storage costs.
  name: TTL
finops:
- name: Amazon Dynamodb Finops
  service_category: API
  slug: amazon-dynamodb-finops
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
json_schemas:
- name: Amazon DynamoDB Table
  property_count: 16
  slug: amazon-dynamodb-table
- name: AttributeDefinition
  property_count: 2
  slug: dynamodb-openapi-attribute-definition
- name: AttributeValue
  property_count: 10
  slug: dynamodb-openapi-attribute-value
- name: BatchGetItemInput
  property_count: 1
  slug: dynamodb-openapi-batch-get-item-input
- name: BatchGetItemOutput
  property_count: 2
  slug: dynamodb-openapi-batch-get-item-output
- name: BatchWriteItemInput
  property_count: 1
  slug: dynamodb-openapi-batch-write-item-input
- name: BatchWriteItemOutput
  property_count: 1
  slug: dynamodb-openapi-batch-write-item-output
- name: CreateTableInput
  property_count: 8
  slug: dynamodb-openapi-create-table-input
- name: CreateTableOutput
  property_count: 1
  slug: dynamodb-openapi-create-table-output
- name: DeleteItemInput
  property_count: 6
  slug: dynamodb-openapi-delete-item-input
- name: DeleteItemOutput
  property_count: 1
  slug: dynamodb-openapi-delete-item-output
- name: DescribeTableOutput
  property_count: 1
  slug: dynamodb-openapi-describe-table-output
- name: GetItemInput
  property_count: 5
  slug: dynamodb-openapi-get-item-input
- name: GetItemOutput
  property_count: 1
  slug: dynamodb-openapi-get-item-output
- name: GlobalSecondaryIndex
  property_count: 4
  slug: dynamodb-openapi-global-secondary-index
- name: KeySchemaElement
  property_count: 2
  slug: dynamodb-openapi-key-schema-element
- name: LocalSecondaryIndex
  property_count: 3
  slug: dynamodb-openapi-local-secondary-index
- name: Projection
  property_count: 2
  slug: dynamodb-openapi-projection
- name: ProvisionedThroughputDescription
  property_count: 5
  slug: dynamodb-openapi-provisioned-throughput-description
- name: ProvisionedThroughput
  property_count: 2
  slug: dynamodb-openapi-provisioned-throughput
- name: PutItemInput
  property_count: 6
  slug: dynamodb-openapi-put-item-input
- name: PutItemOutput
  property_count: 1
  slug: dynamodb-openapi-put-item-output
- name: QueryInput
  property_count: 12
  slug: dynamodb-openapi-query-input
- name: QueryOutput
  property_count: 4
  slug: dynamodb-openapi-query-output
- name: ScanInput
  property_count: 12
  slug: dynamodb-openapi-scan-input
- name: ScanOutput
  property_count: 4
  slug: dynamodb-openapi-scan-output
- name: TableDescription
  property_count: 13
  slug: dynamodb-openapi-table-description
- name: Tag
  property_count: 2
  slug: dynamodb-openapi-tag
- name: TransactGetItemsInput
  property_count: 1
  slug: dynamodb-openapi-transact-get-items-input
- name: TransactGetItemsOutput
  property_count: 1
  slug: dynamodb-openapi-transact-get-items-output
- name: TransactWriteItemsInput
  property_count: 2
  slug: dynamodb-openapi-transact-write-items-input
- name: TransactWriteItemsOutput
  property_count: 1
  slug: dynamodb-openapi-transact-write-items-output
- name: UpdateItemInput
  property_count: 7
  slug: dynamodb-openapi-update-item-input
- name: UpdateItemOutput
  property_count: 1
  slug: dynamodb-openapi-update-item-output
- name: UpdateTableInput
  property_count: 4
  slug: dynamodb-openapi-update-table-input
json_structures:
- name: Amazon Dynamodb Table Structure
  property_count: 16
  slug: amazon-dynamodb-table-structure
- name: Dynamodb Openapi Attribute Definition Structure
  property_count: 2
  slug: dynamodb-openapi-attribute-definition-structure
- name: Dynamodb Openapi Attribute Value Structure
  property_count: 10
  slug: dynamodb-openapi-attribute-value-structure
- name: Dynamodb Openapi Batch Get Item Input Structure
  property_count: 1
  slug: dynamodb-openapi-batch-get-item-input-structure
- name: Dynamodb Openapi Batch Get Item Output Structure
  property_count: 2
  slug: dynamodb-openapi-batch-get-item-output-structure
- name: Dynamodb Openapi Batch Write Item Input Structure
  property_count: 1
  slug: dynamodb-openapi-batch-write-item-input-structure
- name: Dynamodb Openapi Batch Write Item Output Structure
  property_count: 1
  slug: dynamodb-openapi-batch-write-item-output-structure
- name: Dynamodb Openapi Create Table Input Structure
  property_count: 8
  slug: dynamodb-openapi-create-table-input-structure
- name: Dynamodb Openapi Create Table Output Structure
  property_count: 1
  slug: dynamodb-openapi-create-table-output-structure
- name: Dynamodb Openapi Delete Item Input Structure
  property_count: 6
  slug: dynamodb-openapi-delete-item-input-structure
- name: Dynamodb Openapi Delete Item Output Structure
  property_count: 1
  slug: dynamodb-openapi-delete-item-output-structure
- name: Dynamodb Openapi Describe Table Output Structure
  property_count: 1
  slug: dynamodb-openapi-describe-table-output-structure
- name: Dynamodb Openapi Get Item Input Structure
  property_count: 5
  slug: dynamodb-openapi-get-item-input-structure
- name: Dynamodb Openapi Get Item Output Structure
  property_count: 1
  slug: dynamodb-openapi-get-item-output-structure
- name: Dynamodb Openapi Global Secondary Index Structure
  property_count: 4
  slug: dynamodb-openapi-global-secondary-index-structure
- name: Dynamodb Openapi Key Schema Element Structure
  property_count: 2
  slug: dynamodb-openapi-key-schema-element-structure
- name: Dynamodb Openapi Local Secondary Index Structure
  property_count: 3
  slug: dynamodb-openapi-local-secondary-index-structure
- name: Dynamodb Openapi Projection Structure
  property_count: 2
  slug: dynamodb-openapi-projection-structure
- name: Dynamodb Openapi Provisioned Throughput Description Structure
  property_count: 5
  slug: dynamodb-openapi-provisioned-throughput-description-structure
- name: Dynamodb Openapi Provisioned Throughput Structure
  property_count: 2
  slug: dynamodb-openapi-provisioned-throughput-structure
- name: Dynamodb Openapi Put Item Input Structure
  property_count: 6
  slug: dynamodb-openapi-put-item-input-structure
- name: Dynamodb Openapi Put Item Output Structure
  property_count: 1
  slug: dynamodb-openapi-put-item-output-structure
- name: Dynamodb Openapi Query Input Structure
  property_count: 12
  slug: dynamodb-openapi-query-input-structure
- name: Dynamodb Openapi Query Output Structure
  property_count: 4
  slug: dynamodb-openapi-query-output-structure
- name: Dynamodb Openapi Scan Input Structure
  property_count: 12
  slug: dynamodb-openapi-scan-input-structure
- name: Dynamodb Openapi Scan Output Structure
  property_count: 4
  slug: dynamodb-openapi-scan-output-structure
- name: Dynamodb Openapi Table Description Structure
  property_count: 13
  slug: dynamodb-openapi-table-description-structure
- name: Dynamodb Openapi Tag Structure
  property_count: 2
  slug: dynamodb-openapi-tag-structure
- name: Dynamodb Openapi Transact Get Items Input Structure
  property_count: 1
  slug: dynamodb-openapi-transact-get-items-input-structure
- name: Dynamodb Openapi Transact Get Items Output Structure
  property_count: 1
  slug: dynamodb-openapi-transact-get-items-output-structure
- name: Dynamodb Openapi Transact Write Items Input Structure
  property_count: 2
  slug: dynamodb-openapi-transact-write-items-input-structure
- name: Dynamodb Openapi Transact Write Items Output Structure
  property_count: 1
  slug: dynamodb-openapi-transact-write-items-output-structure
- name: Dynamodb Openapi Update Item Input Structure
  property_count: 7
  slug: dynamodb-openapi-update-item-input-structure
- name: Dynamodb Openapi Update Item Output Structure
  property_count: 1
  slug: dynamodb-openapi-update-item-output-structure
- name: Dynamodb Openapi Update Table Input Structure
  property_count: 4
  slug: dynamodb-openapi-update-table-input-structure
jsonld:
- class_count: 32
  name: Amazon Dynamodb Context
  property_count: 92
  slug: amazon-dynamodb-context
layout: provider
modified: '2026-05-19'
name: Amazon DynamoDB
nav: Providers
network: true
overview: 'Amazon DynamoDB publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Batch API, Items API, Queries API, and 2 more. Tagged areas include Database, Document Store, Key-Value, NoSQL, and Serverless.


  The Amazon DynamoDB catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Amazon DynamoDB''s developer surface includes authentication, developer portal, documentation, support, engineering blog, developer console, signup flow, and 28 more developer resources.'
plans:
- name: Amazon Dynamodb Plans Pricing
  plan_count: 3
  slug: amazon-dynamodb-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 5
  name: Amazon Dynamodb Rate Limits
  slug: amazon-dynamodb-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: Amazon DynamoDB API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: amazon-dynamodb-jsonschema-spectral-rules
- effective_rule_count: 75
  extends:
  - spectral:oas
  name: Amazon DynamoDB API Rules
  rule_count: 34
  severity_counts:
    error: 11
    hint: 0
    info: 4
    warn: 19
  slug: amazon-dynamodb-spectral-rules
score:
  band: strong
  composite: 56.6
  delta: -6.8
  facets:
    access_clarity: 59.2
    commercial_clarity: 59.2
    contract_governance: 25.0
    contract_quality: 75.5
    developer_ergonomics: 50.0
    discoverability: 81.5
    governance: 25.0
    operational_transparency: 36.8
  previous_composite: 63.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/amazon-dynamodb/refs/heads/main/screenshots/amazon-dynamodb-2026-06-20T171630.png
security:
- kind: authentication
  name: Amazon Dynamodb Authentication
  slug: amazon-dynamodb-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Amazon Dynamodb Domain Security
  slug: amazon-dynamodb-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amazon Dynamodb Vulnerability Disclosure
  slug: amazon-dynamodb-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Amazon Dynamodb Trust Center
  slug: amazon-dynamodb-trust-center
  summary_line: PCI DSS, HIPAA, FedRAMP, GDPR, FIPS 140
slug: amazon-dynamodb
tags:
- Database
- Document Store
- Key-Value
- NoSQL
- Serverless
use_cases:
- description: Fraud detection, digital onboarding, and regulatory compliance workloads requiring consistent low latency.
  name: Financial Services
- description: Player profiles, leaderboards, session state, and game data with high-throughput requirements.
  name: Gaming Applications
- description: Shopping carts, inventory tracking, order management, and customer data platforms.
  name: E-Commerce
- description: High-volume telemetry data ingestion and time-series storage from IoT devices.
  name: IoT Data Storage
- description: Metadata storage and content indexing for media streaming and publishing platforms.
  name: Content Management
website: https://aws.amazon.com/dynamodb/
---
