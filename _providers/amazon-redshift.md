---
access_model:
  confidence: high
  label: Paid (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: true
  try_now: true
agent_readiness:
  band: agent-aware
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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.5
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 10
  human_in_the_loop: 0
  name: Amazon Redshift Agentic Access
  operation_count: 10
  slug: amazon-redshift-agentic-access
  summary_line: 10 operations · 10 acting
api_count: 5
apis:
- description: The Amazon Redshift Serverless API for managing serverless data warehouse workgroups, namespaces, and capacity without provisioning clusters.
  name: Amazon Redshift Serverless API
  slug: amazon-redshift-serverless-api
- description: List databases, schemas, and tables in a Redshift data warehouse
  name: Amazon Redshift Metadata API
  slug: amazon-redshift-metadata-api
- description: Retrieve results from completed SQL statement executions
  name: Amazon Redshift Result Retrieval API
  slug: amazon-redshift-result-retrieval-api
- description: Execute SQL statements against Amazon Redshift clusters or serverless workgroups
  name: Amazon Redshift Statement Execution API
  slug: amazon-redshift-statement-execution-api
- description: Describe, list, and cancel SQL statement executions
  name: Amazon Redshift Statement Management API
  slug: amazon-redshift-statement-management-api
artifact_total: 129
collections:
- collection_type: postman
  name: Amazon Redshift Data Metadata API
  slug: postman-amazon-redshift-metadata-api
- collection_type: postman
  name: Amazon Redshift Data Metadata Result Retrieval API
  slug: postman-amazon-redshift-result-retrieval-api
- collection_type: postman
  name: Amazon Redshift Data Metadata Statement Execution API
  slug: postman-amazon-redshift-statement-execution-api
- collection_type: postman
  name: Amazon Redshift Data Metadata Statement Management API
  slug: postman-amazon-redshift-statement-management-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Amazon Redshift Data API
  slug: open-amazon-redshift-data-api
- collection_type: open
  name: Amazon Redshift Data Metadata API
  slug: open-amazon-redshift-metadata-api
- collection_type: open
  name: Amazon Redshift Data Metadata Result Retrieval API
  slug: open-amazon-redshift-result-retrieval-api
- collection_type: open
  name: Amazon Redshift Data Metadata Statement Execution API
  slug: open-amazon-redshift-statement-execution-api
- collection_type: open
  name: Amazon Redshift Data Metadata Statement Management API
  slug: open-amazon-redshift-statement-management-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/amazon-redshift/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/amazon-redshift-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/amazon-redshift-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-redshift-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amazon-redshift-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/amazon-redshift-authentication.yml
- group: company
  title: ''
  type: Blog
  url: https://aws.amazon.com/blogs/big-data/category/database/amazon-redshift/
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
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/redshift/
- group: start
  title: ''
  type: GettingStarted
  url: https://aws.amazon.com/redshift/getting-started/
- group: operate
  title: ''
  type: FAQ
  url: https://aws.amazon.com/redshift/faqs/
- group: commercial
  title: ''
  type: Pricing
  url: https://aws.amazon.com/redshift/pricing/
- group: start
  title: ''
  type: Console
  url: https://console.aws.amazon.com/redshift/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.aws.amazon.com/
created: '2024-01-01'
description: Amazon Redshift is a fast, fully managed cloud data warehouse that makes it simple and cost-effective to analyze all your data using standard SQL and your existing Business Intelligence (BI) tools.
examples:
- key_count: 1
  name: Amazon Redshift Data Active Statements Exceeded Exception Example
  slug: amazon-redshift-data-active-statements-exceeded-exception-example
- key_count: 9
  name: Amazon Redshift Data Batch Execute Statement Request Example
  slug: amazon-redshift-data-batch-execute-statement-request-example
- key_count: 7
  name: Amazon Redshift Data Batch Execute Statement Response Example
  slug: amazon-redshift-data-batch-execute-statement-response-example
- key_count: 1
  name: Amazon Redshift Data Cancel Statement Request Example
  slug: amazon-redshift-data-cancel-statement-request-example
- key_count: 1
  name: Amazon Redshift Data Cancel Statement Response Example
  slug: amazon-redshift-data-cancel-statement-response-example
- key_count: 13
  name: Amazon Redshift Data Column Metadata Example
  slug: amazon-redshift-data-column-metadata-example
- key_count: 1
  name: Amazon Redshift Data Describe Statement Request Example
  slug: amazon-redshift-data-describe-statement-request-example
- key_count: 19
  name: Amazon Redshift Data Describe Statement Response Example
  slug: amazon-redshift-data-describe-statement-response-example
- key_count: 9
  name: Amazon Redshift Data Describe Table Request Example
  slug: amazon-redshift-data-describe-table-request-example
- key_count: 3
  name: Amazon Redshift Data Describe Table Response Example
  slug: amazon-redshift-data-describe-table-response-example
- key_count: 10
  name: Amazon Redshift Data Execute Statement Request Example
  slug: amazon-redshift-data-execute-statement-request-example
- key_count: 7
  name: Amazon Redshift Data Execute Statement Response Example
  slug: amazon-redshift-data-execute-statement-response-example
- key_count: 6
  name: Amazon Redshift Data Field Example
  slug: amazon-redshift-data-field-example
- key_count: 2
  name: Amazon Redshift Data Get Statement Result Request Example
  slug: amazon-redshift-data-get-statement-result-request-example
- key_count: 4
  name: Amazon Redshift Data Get Statement Result Response Example
  slug: amazon-redshift-data-get-statement-result-response-example
- key_count: 1
  name: Amazon Redshift Data Internal Server Exception Example
  slug: amazon-redshift-data-internal-server-exception-example
- key_count: 7
  name: Amazon Redshift Data List Databases Request Example
  slug: amazon-redshift-data-list-databases-request-example
- key_count: 2
  name: Amazon Redshift Data List Databases Response Example
  slug: amazon-redshift-data-list-databases-response-example
- key_count: 8
  name: Amazon Redshift Data List Schemas Request Example
  slug: amazon-redshift-data-list-schemas-request-example
- key_count: 2
  name: Amazon Redshift Data List Schemas Response Example
  slug: amazon-redshift-data-list-schemas-response-example
- key_count: 5
  name: Amazon Redshift Data List Statements Request Example
  slug: amazon-redshift-data-list-statements-request-example
- key_count: 2
  name: Amazon Redshift Data List Statements Response Example
  slug: amazon-redshift-data-list-statements-response-example
- key_count: 9
  name: Amazon Redshift Data List Tables Request Example
  slug: amazon-redshift-data-list-tables-request-example
- key_count: 2
  name: Amazon Redshift Data List Tables Response Example
  slug: amazon-redshift-data-list-tables-response-example
- key_count: 2
  name: Amazon Redshift Data Resource Not Found Exception Example
  slug: amazon-redshift-data-resource-not-found-exception-example
- key_count: 2
  name: Amazon Redshift Data Sql Parameter Example
  slug: amazon-redshift-data-sql-parameter-example
- key_count: 12
  name: Amazon Redshift Data Statement Data Example
  slug: amazon-redshift-data-statement-data-example
- key_count: 11
  name: Amazon Redshift Data Sub Statement Data Example
  slug: amazon-redshift-data-sub-statement-data-example
- key_count: 3
  name: Amazon Redshift Data Table Member Example
  slug: amazon-redshift-data-table-member-example
- key_count: 1
  name: Amazon Redshift Data Validation Exception Example
  slug: amazon-redshift-data-validation-exception-example
features:
- description: Distributed query execution across multiple nodes for petabyte-scale analytics with sub-second response times.
  name: Massively Parallel Processing
- description: Auto-scaling compute capacity without cluster provisioning, paying only for compute used during queries.
  name: Serverless Data Warehouse
- description: Run SQL statements without managing database connections using IAM-based authentication and asynchronous execution.
  name: Data API
- description: Query data across Amazon RDS, Aurora, and S3 data lakes without moving data using federated query capabilities.
  name: Federated Query
- description: Build, train, and deploy ML models directly in Redshift using SQL with Amazon SageMaker integration.
  name: Machine Learning Integration
- description: Automatically add transient capacity to handle bursts of concurrent queries without performance degradation.
  name: Concurrency Scaling
finops:
- name: Amazon Redshift Finops
  service_category: Analytics / Data Warehouse
  slug: amazon-redshift-finops
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
json_schemas:
- name: Amazon Redshift Cluster
  property_count: 32
  slug: amazon-redshift-cluster
- name: ActiveStatementsExceededException
  property_count: 1
  slug: amazon-redshift-data-active-statements-exceeded-exception
- name: BatchExecuteStatementRequest
  property_count: 9
  slug: amazon-redshift-data-batch-execute-statement-request
- name: BatchExecuteStatementResponse
  property_count: 7
  slug: amazon-redshift-data-batch-execute-statement-response
- name: CancelStatementRequest
  property_count: 1
  slug: amazon-redshift-data-cancel-statement-request
- name: CancelStatementResponse
  property_count: 1
  slug: amazon-redshift-data-cancel-statement-response
- name: ColumnMetadata
  property_count: 13
  slug: amazon-redshift-data-column-metadata
- name: DescribeStatementRequest
  property_count: 1
  slug: amazon-redshift-data-describe-statement-request
- name: DescribeStatementResponse
  property_count: 19
  slug: amazon-redshift-data-describe-statement-response
- name: DescribeTableRequest
  property_count: 9
  slug: amazon-redshift-data-describe-table-request
- name: DescribeTableResponse
  property_count: 3
  slug: amazon-redshift-data-describe-table-response
- name: ExecuteStatementRequest
  property_count: 10
  slug: amazon-redshift-data-execute-statement-request
- name: ExecuteStatementResponse
  property_count: 7
  slug: amazon-redshift-data-execute-statement-response
- name: Field
  property_count: 6
  slug: amazon-redshift-data-field
- name: GetStatementResultRequest
  property_count: 2
  slug: amazon-redshift-data-get-statement-result-request
- name: GetStatementResultResponse
  property_count: 4
  slug: amazon-redshift-data-get-statement-result-response
- name: InternalServerException
  property_count: 1
  slug: amazon-redshift-data-internal-server-exception
- name: ListDatabasesRequest
  property_count: 7
  slug: amazon-redshift-data-list-databases-request
- name: ListDatabasesResponse
  property_count: 2
  slug: amazon-redshift-data-list-databases-response
- name: ListSchemasRequest
  property_count: 8
  slug: amazon-redshift-data-list-schemas-request
- name: ListSchemasResponse
  property_count: 2
  slug: amazon-redshift-data-list-schemas-response
- name: ListStatementsRequest
  property_count: 5
  slug: amazon-redshift-data-list-statements-request
- name: ListStatementsResponse
  property_count: 2
  slug: amazon-redshift-data-list-statements-response
- name: ListTablesRequest
  property_count: 9
  slug: amazon-redshift-data-list-tables-request
- name: ListTablesResponse
  property_count: 2
  slug: amazon-redshift-data-list-tables-response
- name: ResourceNotFoundException
  property_count: 2
  slug: amazon-redshift-data-resource-not-found-exception
- name: SqlParameter
  property_count: 2
  slug: amazon-redshift-data-sql-parameter
- name: StatementData
  property_count: 12
  slug: amazon-redshift-data-statement-data
- name: SubStatementData
  property_count: 11
  slug: amazon-redshift-data-sub-statement-data
- name: TableMember
  property_count: 3
  slug: amazon-redshift-data-table-member
- name: ValidationException
  property_count: 1
  slug: amazon-redshift-data-validation-exception
json_structures:
- name: Amazon Redshift Data Active Statements Exceeded Exception Structure
  property_count: 1
  slug: amazon-redshift-data-active-statements-exceeded-exception-structure
- name: Amazon Redshift Data Batch Execute Statement Request Structure
  property_count: 9
  slug: amazon-redshift-data-batch-execute-statement-request-structure
- name: Amazon Redshift Data Batch Execute Statement Response Structure
  property_count: 7
  slug: amazon-redshift-data-batch-execute-statement-response-structure
- name: Amazon Redshift Data Cancel Statement Request Structure
  property_count: 1
  slug: amazon-redshift-data-cancel-statement-request-structure
- name: Amazon Redshift Data Cancel Statement Response Structure
  property_count: 1
  slug: amazon-redshift-data-cancel-statement-response-structure
- name: Amazon Redshift Data Column Metadata Structure
  property_count: 13
  slug: amazon-redshift-data-column-metadata-structure
- name: Amazon Redshift Data Describe Statement Request Structure
  property_count: 1
  slug: amazon-redshift-data-describe-statement-request-structure
- name: Amazon Redshift Data Describe Statement Response Structure
  property_count: 19
  slug: amazon-redshift-data-describe-statement-response-structure
- name: Amazon Redshift Data Describe Table Request Structure
  property_count: 9
  slug: amazon-redshift-data-describe-table-request-structure
- name: Amazon Redshift Data Describe Table Response Structure
  property_count: 3
  slug: amazon-redshift-data-describe-table-response-structure
- name: Amazon Redshift Data Execute Statement Request Structure
  property_count: 10
  slug: amazon-redshift-data-execute-statement-request-structure
- name: Amazon Redshift Data Execute Statement Response Structure
  property_count: 7
  slug: amazon-redshift-data-execute-statement-response-structure
- name: Amazon Redshift Data Field Structure
  property_count: 6
  slug: amazon-redshift-data-field-structure
- name: Amazon Redshift Data Get Statement Result Request Structure
  property_count: 2
  slug: amazon-redshift-data-get-statement-result-request-structure
- name: Amazon Redshift Data Get Statement Result Response Structure
  property_count: 4
  slug: amazon-redshift-data-get-statement-result-response-structure
- name: Amazon Redshift Data Internal Server Exception Structure
  property_count: 1
  slug: amazon-redshift-data-internal-server-exception-structure
- name: Amazon Redshift Data List Databases Request Structure
  property_count: 7
  slug: amazon-redshift-data-list-databases-request-structure
- name: Amazon Redshift Data List Databases Response Structure
  property_count: 2
  slug: amazon-redshift-data-list-databases-response-structure
- name: Amazon Redshift Data List Schemas Request Structure
  property_count: 8
  slug: amazon-redshift-data-list-schemas-request-structure
- name: Amazon Redshift Data List Schemas Response Structure
  property_count: 2
  slug: amazon-redshift-data-list-schemas-response-structure
- name: Amazon Redshift Data List Statements Request Structure
  property_count: 5
  slug: amazon-redshift-data-list-statements-request-structure
- name: Amazon Redshift Data List Statements Response Structure
  property_count: 2
  slug: amazon-redshift-data-list-statements-response-structure
- name: Amazon Redshift Data List Tables Request Structure
  property_count: 9
  slug: amazon-redshift-data-list-tables-request-structure
- name: Amazon Redshift Data List Tables Response Structure
  property_count: 2
  slug: amazon-redshift-data-list-tables-response-structure
- name: Amazon Redshift Data Resource Not Found Exception Structure
  property_count: 2
  slug: amazon-redshift-data-resource-not-found-exception-structure
- name: Amazon Redshift Data Sql Parameter Structure
  property_count: 2
  slug: amazon-redshift-data-sql-parameter-structure
- name: Amazon Redshift Data Statement Data Structure
  property_count: 12
  slug: amazon-redshift-data-statement-data-structure
- name: Amazon Redshift Data Sub Statement Data Structure
  property_count: 11
  slug: amazon-redshift-data-sub-statement-data-structure
- name: Amazon Redshift Data Table Member Structure
  property_count: 3
  slug: amazon-redshift-data-table-member-structure
- name: Amazon Redshift Data Validation Exception Structure
  property_count: 1
  slug: amazon-redshift-data-validation-exception-structure
jsonld:
- class_count: 0
  name: Amazon Redshift Context
  property_count: 6
  slug: amazon-redshift-context
- class_count: 0
  name: Amazon Redshift Data Context
  property_count: 0
  slug: amazon-redshift-data-context
layout: provider
modified: '2026-05-19'
name: Amazon Redshift
nav: Providers
network: true
overview: 'Amazon Redshift publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Metadata API, Result Retrieval API, Statement Execution API, and 1 more. Tagged areas include Analytics, Big Data, Cloud, Data Lake, and Data Warehouse.


  The Amazon Redshift catalog on APIs.io includes 2 JSON-LD contexts and 2 Spectral governance rulesets.


  Amazon Redshift''s developer surface includes authentication, engineering blog, support, documentation, getting-started guide, FAQ, pricing, and 9 more developer resources.'
plans:
- name: Amazon Redshift Plans Pricing
  plan_count: 3
  slug: amazon-redshift-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 5
  name: Amazon Redshift Rate Limits
  slug: amazon-redshift-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: Amazon Redshift API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: amazon-redshift-jsonschema-spectral-rules
- effective_rule_count: 56
  extends:
  - spectral:oas
  name: Amazon Redshift API Rules
  rule_count: 15
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 6
  slug: amazon-redshift-spectral-rules
score:
  band: strong
  composite: 58.0
  delta: 9.6
  facets:
    access_clarity: 55.3
    commercial_clarity: 55.3
    contract_governance: 13.6
    contract_quality: 62.6
    developer_ergonomics: 83.3
    discoverability: 64.8
    governance: 13.6
    operational_transparency: 50.0
  previous_composite: 48.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/amazon-redshift/refs/heads/main/screenshots/amazon-redshift-2026-06-20T171811.png
security:
- kind: authentication
  name: Amazon Redshift Authentication
  slug: amazon-redshift-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Amazon Redshift Domain Security
  slug: amazon-redshift-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amazon Redshift Vulnerability Disclosure
  slug: amazon-redshift-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Amazon Redshift Trust Center
  slug: amazon-redshift-trust-center
  summary_line: PCI DSS, HIPAA, FedRAMP, GDPR, FIPS 140
slug: amazon-redshift
tags:
- Analytics
- Big Data
- Cloud
- Data Lake
- Data Warehouse
- ETL
- Machine-Learning
- Serverless
- SQL
use_cases:
- description: Run complex analytical queries across petabytes of structured data for BI dashboards and reporting.
  name: Business Intelligence Analytics
- description: Query data directly in Amazon S3 using Redshift Spectrum without loading it into the warehouse.
  name: Data Lake Analytics
- description: Ingest streaming data and run near-real-time analytics on operational data for instant insights.
  name: Real-Time Analytics
- description: Transform and load large datasets using SQL-based ETL operations within the data warehouse.
  name: ETL Pipeline Processing
- description: Run on-demand analytical queries without provisioning clusters using Redshift Serverless and Data API.
  name: Serverless Ad-Hoc Queries
---
