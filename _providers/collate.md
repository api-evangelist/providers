---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: true
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: mostly
    pagination_ratio: paginated
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 65.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 962
  human_in_the_loop: 16
  name: Collate Agentic Access
  operation_count: 1867
  slug: collate-agentic-access
  summary_line: 1867 operations · 962 acting · 16 human-in-the-loop
api_count: 1
apis:
- baseURL: https://sandbox.open-metadata.org/api/v1
  baseurl_source: declared
  description: Lightweight activity notifications for dashboards and feeds.
  name: Collate Activity Stream API
  slug: collate-activity-stream-api
- baseURL: https://sandbox.open-metadata.org/api/v1
  baseurl_source: declared
  description: '`Agent Executions` are time-series records of AI agent execution runs, capturing observability metrics, governance checks, and performance data.'
  name: Collate Agent Executions API
  slug: collate-agent-executions-api
- baseURL: https://sandbox.open-metadata.org/api/v1
  baseurl_source: declared
  description: '`AI Applications` are autonomous software entities that use LLM models to perform tasks, make decisions, and interact with data sources.'
  name: Collate AI Applications API
  slug: collate-ai-applications-api
- baseURL: https://sandbox.open-metadata.org/api/v1
  baseurl_source: declared
  description: Auto-generated audit packs (JSON/PDF evidence bundles) for AI governance. Submitted asynchronously and consumed by auditors and regulators.
  name: Collate AI Audit Reports API
  slug: collate-ai-audit-reports-api
- baseURL: https://sandbox.open-metadata.org/api/v1
  baseurl_source: declared
  description: 'Question-anchored AI context discovery: semantically search the company-knowledge layer (glossary terms, metrics, articles) and route each hit to the candidate data assets it points to. Asset-anchored'
  name: Collate AI Context API
  slug: collate-ai-context-api
- baseURL: https://sandbox.open-metadata.org/api/v1
  baseurl_source: declared
  description: Controls within an AI Governance Framework (e.g. EU AI Act Article 10).
  name: Collate AI Framework Controls API
  slug: collate-ai-framework-controls-api
- baseURL: https://sandbox.open-metadata.org/api/v1
  baseurl_source: declared
  description: 'Cross-asset AI governance endpoints: intake checks, submitForReview, approve, reject, shadow triage.'
  name: Collate AI Governance API
  slug: collate-ai-governance-api
- baseURL: https://sandbox.open-metadata.org/api/v1
  baseurl_source: declared
  description: Workspace-level AI governance frameworks (EU AI Act, NIST AI RMF, ISO/IEC 42001, custom). Enabled frameworks drive per-asset compliance assessments.
  name: Collate AI Governance Frameworks API
  slug: collate-ai-governance-frameworks-api
- baseURL: https://sandbox.open-metadata.org/api/v1
  baseurl_source: declared
  description: '`AI Governance Policies` define rules, compliance requirements, bias thresholds, and control measures for AI agents and models.'
  name: Collate AI Governance Policies API
  slug: collate-ai-governance-policies-api
- baseURL: https://sandbox.open-metadata.org/api/v1
  baseurl_source: declared
  description: Time-bound notifications for data assets
  name: Collate Announcements API
  slug: collate-announcements-api
- baseURL: https://sandbox.open-metadata.org/api/v1
  baseurl_source: declared
  description: A `API Collection` is an optional way of grouping API Endpoints that belong to a API Service.
  name: Collate API Collections API
  slug: collate-api-collections-api
- baseURL: https://sandbox.open-metadata.org/api/v1
  baseurl_source: declared
  description: A `API Endpoint` is a specific endpoint of an API that is part of an API Collection..
  name: Collate API Endpoint API
  slug: collate-api-endpoint-api
- baseURL: https://sandbox.open-metadata.org/api/v1
  baseurl_source: declared
  description: APIs related `API Service` entities, such as REST or MicroService.
  name: Collate API Services API
  slug: collate-api-services-api
- baseURL: https://sandbox.open-metadata.org/api/v1
  baseurl_source: declared
  description: Apps marketplace holds to application available for Open-metadata
  name: Collate Apps API
  slug: collate-apps-api
- baseURL: https://sandbox.open-metadata.org/api/v1
  baseurl_source: declared
  description: APIs related to uploading attachments.
  name: Collate Attachments API
  slug: collate-attachments-api
- baseURL: https://sandbox.open-metadata.org/api/v1
  baseurl_source: declared
  description: APIs for listing user initiated change events persisted for auditing
  name: Collate Audit Logs API
  slug: collate-audit-logs-api
- baseURL: https://sandbox.open-metadata.org/api/v1
  baseurl_source: declared
  description: A `Bot` automates tasks, such as ingesting metadata, and running data quality It performs this task as a special user in the system.
  name: Collate Bots API
  slug: collate-bots-api
- baseURL: https://sandbox.open-metadata.org/api/v1
  baseurl_source: declared
  description: APIs to retrieve change summary metadata for entities. Change summary tracks who changed each field, the source of the change (e.g., Suggested for AI-generated, Manual for user edits), and when the ch
  name: Collate Change Summary API
  slug: collate-changesummary-api
- baseURL: https://sandbox.open-metadata.org/api/v1
  baseurl_source: declared
  description: A `Chart` are computed from data presents data visually and can be part of `Dashboards`.
  name: Collate Charts API
  slug: collate-charts-api
- baseURL: https://sandbox.open-metadata.org/api/v1
  baseurl_source: declared
  description: These APIs are related to `Classification` and `Tags`. A `Classification` entity contains hierarchical terms called `Tags` used for categorizing and classifying data assets and other entities.
  name: Collate Classifications API
  slug: collate-classifications-api
- baseURL: https://sandbox.open-metadata.org/api/v1
  baseurl_source: declared
  description: Columns represent individual data fields within tables and dashboard data models. This API provides operations to update column metadata such as tags, glossary terms, descriptions, and other propertie
  name: Collate Columns API
  slug: collate-columns-api
- baseURL: https://sandbox.open-metadata.org/api/v1
  baseurl_source: declared
  description: A Container is an abstraction for any path(including the top level eg. bucket in S3) storing data in an Object store such as S3, GCP, Azure. It maps a tree-like structure, where each Container can hav
  name: Collate Containers API
  slug: collate-containers-api
- baseURL: https://sandbox.open-metadata.org/api/v1
  baseurl_source: declared
  description: APIs for managing files in the Context Center Drive.
  name: Collate Context Center Drive Files API
  slug: collate-context-center-drive-files-api
- baseURL: https://sandbox.open-metadata.org/api/v1
  baseurl_source: declared
  description: APIs for managing folders in the Context Center Drive.
  name: Collate Context Center Drive Folders API
  slug: collate-context-center-drive-folders-api
- baseURL: https://sandbox.open-metadata.org/api/v1
  baseurl_source: declared
  description: APIs related to Context Center pages (articles and quick links).
  name: Collate Context Center Pages API
  slug: collate-context-center-pages-api
- baseURL: https://sandbox.open-metadata.org/api/v1
  baseurl_source: declared
  description: APIs for managing reusable Context Center memories.
  name: Collate Context Memories API
  slug: collate-context-memories-api
- baseURL: https://sandbox.open-metadata.org/api/v1
  baseurl_source: declared
  description: CSV import and export metadata APIs.
  name: Collate CSV API
  slug: collate-csv-api
- baseURL: https://sandbox.open-metadata.org/api/v1
  baseurl_source: declared
  description: CSV import and export job status APIs.
  name: Collate CSV Async Jobs API
  slug: collate-csv-async-jobs-api
- baseURL: https://sandbox.open-metadata.org/api/v1
  baseurl_source: declared
  description: '`Data Models` are the schemas used to build dashboards, charts, or other data assets.'
  name: Collate Dashboard Data Models API
  slug: collate-dashboard-data-models-api
- baseURL: https://sandbox.open-metadata.org/api/v1
  baseurl_source: declared
  description: The Dashboard Services API from Collate — 14 operation(s) for dashboard services.
  name: Collate Dashboard Services API
  slug: collate-dashboard-services-api
- baseURL: https://sandbox.open-metadata.org/api/v1
  baseurl_source: declared
  description: Dashboards are computed from data and visually present data, metrics, and KPIs. They are typically updated in real-time and allow interactive data exploration.
  name: Collate Dashboards API
  slug: collate-dashboards-api
- baseURL: https://sandbox.open-metadata.org/api/v1
  baseurl_source: declared
  description: '`DataContract` defines the schema and quality guarantees for a data asset.'
  name: Collate Data Contracts API
  slug: collate-data-contracts-api
- baseURL: https://sandbox.open-metadata.org/api/v1
  baseurl_source: declared
  description: APIs to retrieve dimensional test case results data.
  name: Collate Data Quality API
  slug: collate-data-quality-api
- baseURL: https://sandbox.open-metadata.org/api/v1
  baseurl_source: declared
  description: A `Database Schema` is collection of tables, views, stored procedures, and other database objects.
  name: Collate Database Schemas API
  slug: collate-database-schemas-api
- baseURL: https://sandbox.open-metadata.org/api/v1
  baseurl_source: declared
  description: '`Database Service` is a service such as MySQL, BigQuery, Redshift, Postgres, or Snowflake. Alternative terms such as Database Cluster, Database Server instance are also used for database service.'
  name: Collate Database Services API
  slug: collate-database-services-api
- baseURL: https://sandbox.open-metadata.org/api/v1
  baseurl_source: declared
  description: A `Database` also referred to as `Database Catalog` is a collection of schemas.
  name: Collate Databases API
  slug: collate-databases-api
- baseURL: https://sandbox.open-metadata.org/api/v1
  baseurl_source: declared
  description: A `Directory` is a folder or organizational unit in a Drive Service that can contain files, spreadsheets, and other directories.
  name: Collate Directories API
  slug: collate-directories-api
- baseURL: https://sandbox.open-metadata.org/api/v1
  baseurl_source: declared
  description: A `Document` is an generic entity in OpenMetadata.
  name: Collate Document Store API
  slug: collate-document-store-api
- baseURL: https://sandbox.open-metadata.org/api/v1
  baseurl_source: declared
  description: A `Data Product` or `Data as a Product` is a logical unit that contains all components to process and store domain data for analytical or data-intensive use cases made available to data consumers.
  name: Collate Domains API
  slug: collate-domains-api
- baseURL: https://sandbox.open-metadata.org/api/v1
  baseurl_source: declared
  description: '`Drive Service` is a cloud file storage service such as Google Drive, OneDrive, SharePoint, Box, or Dropbox where documents, spreadsheets, and other files are stored.'
  name: Collate Drive Services API
  slug: collate-drive-services-api
- baseURL: https://sandbox.open-metadata.org/api/v1
  baseurl_source: declared
  description: The `Events` are changes to metadata and are sent when entities are created, modified, or updated. External systems can subscribe to events using event subscription API over Webhooks, Slack, or Micros
  name: Collate Events API
  slug: collate-events-api
- baseURL: https://sandbox.open-metadata.org/api/v1
  baseurl_source: declared
  description: Feeds API supports `Activity Feeds` and `Conversation Threads`.
  name: Collate Feeds API
  slug: collate-feeds-api
- baseURL: https://sandbox.open-metadata.org/api/v1
  baseurl_source: declared
  description: A `File` is a document or resource stored in a Drive Service.
  name: Collate Files API
  slug: collate-files-api
- baseURL: https://sandbox.open-metadata.org/api/v1
  baseurl_source: declared
  description: A `Glossary` is collection of hierarchical `GlossaryTerms`.
  name: Collate Glossaries API
  slug: collate-glossaries-api
- baseURL: https://sandbox.open-metadata.org/api/v1
  baseurl_source: declared
  description: APIs related pipelines/workflows created by the system to ingest metadata.
  name: Collate Ingestion Pipelines API
  slug: collate-ingestion-pipelines-api
- baseURL: https://sandbox.open-metadata.org/api/v1
  baseurl_source: declared
  description: An IntakeForm declares fields shown for a governance entity and which are required. Required fields are enforced at the API layer, layered on top of the entity's schema-required fields.
  name: Collate Intake Forms API
  slug: collate-intakeforms-api
- baseURL: https://sandbox.open-metadata.org/api/v1
  baseurl_source: declared
  description: Inline tutorials and expert content surfaced across OpenMetadata product surfaces.
  name: Collate Learning Resources API
  slug: collate-learning-resources-api
- baseURL: https://sandbox.open-metadata.org/api/v1
  baseurl_source: declared
  description: The `Lineage` for a given data asset, has information of the input datasets used and the ETL pipeline that created it.
  name: Collate Lineage API
  slug: collate-lineage-api
- baseURL: https://sandbox.open-metadata.org/api/v1
  baseurl_source: declared
  description: '`LLM Models` are Large Language Model instances such as GPT-4, Claude, Llama, or custom-trained models used for AI applications.'
  name: Collate LLM Models API
  slug: collate-llm-models-api
- baseURL: https://sandbox.open-metadata.org/api/v1
  baseurl_source: declared
  description: '`LLM Service` is a service for Large Language Model providers such as OpenAI, Anthropic, Azure OpenAI, AWS Bedrock, Google Vertex AI, or custom LLM deployments.'
  name: Collate LLM Services API
  slug: collate-llm-services-api
- baseURL: https://sandbox.open-metadata.org/api/v1
  baseurl_source: declared
  description: '`MCP Executions` are time-series records of MCP server execution sessions, capturing tool calls, resource accesses, data lineage, compliance checks, and audit trails for AI governance.'
  name: Collate MCP Executions API
  slug: collate-mcp-executions-api
- baseURL: https://sandbox.open-metadata.org/api/v1
  baseurl_source: declared
  description: '`MCP Servers` are Model Context Protocol servers that expose tools, resources, and prompts for AI applications. They enable AI governance including risk assessment, compliance tracking, and shadow AI '
  name: Collate MCP Servers API
  slug: collate-mcp-servers-api
- baseURL: https://sandbox.open-metadata.org/api/v1
  baseurl_source: declared
  description: '`MCP Service` is a service for discovering and managing MCP (Model Context Protocol) servers, their tools, resources, and prompts for AI governance.'
  name: Collate MCP Services API
  slug: collate-mcp-services-api
- baseURL: https://sandbox.open-metadata.org/api/v1
  baseurl_source: declared
  description: MCP tool-call usage counters and breakdowns.
  name: Collate MCP Usage API
  slug: collate-mcp-usage-api
- baseURL: https://sandbox.open-metadata.org/api/v1
  baseurl_source: declared
  description: The Messaging Services API from Collate — 14 operation(s) for messaging services.
  name: Collate Messaging Services API
  slug: collate-messaging-services-api
- baseURL: https://sandbox.open-metadata.org/api/v1
  baseurl_source: declared
  description: These APIs are for managing custom property definitions in OpenMetadata. Use these APIs to create custom properties with predefined data types (String, Integer, Date, etc.) that extend entity metadata
  name: Collate Metadata API
  slug: collate-metadata-api
- baseURL: https://sandbox.open-metadata.org/api/v1
  baseurl_source: declared
  description: APIs related to creating and managing other Metadata Services that OpenMetadata integrates with such as `Apache Atlas`, `Amundsen`, etc.
  name: Collate Metadata Services API
  slug: collate-metadata-services-api
- baseURL: https://sandbox.open-metadata.org/api/v1
  baseurl_source: declared
  description: '`Metrics` are measurements computed from data such as `Monthly Active Users`. Some of the metrics that measures used to determine performance against an objective are called KPIs or Key Performance In'
  name: Collate Metrics API
  slug: collate-metrics-api
- baseURL: https://sandbox.open-metadata.org/api/v1
  baseurl_source: declared
  description: The ML Model Services API from Collate — 14 operation(s) for ml model services.
  name: Collate ML Model Services API
  slug: collate-ml-model-services-api
- baseURL: https://sandbox.open-metadata.org/api/v1
  baseurl_source: declared
  description: '`Machine Learning Models` are algorithms trained on data to find patterns or make predictions.'
  name: Collate ML Models API
  slug: collate-ml-models-api
- baseURL: https://sandbox.open-metadata.org/api/v1
  baseurl_source: declared
  description: Notification templates for customizing event notifications
  name: Collate Notification Templates API
  slug: collate-notification-templates-api
- baseURL: https://sandbox.open-metadata.org/api/v1
  baseurl_source: declared
  description: APIs related `Object Store Service` entities, such as S3, GCS or AZURE.
  name: Collate Object Store Services API
  slug: collate-object-store-services-api
- baseURL: https://sandbox.open-metadata.org/api/v1
  baseurl_source: declared
  description: OpenLineage API for receiving lineage events from external systems like Spark, Airflow, etc.
  name: Collate Open Lineage API
  slug: collate-openlineage-api
- baseURL: https://sandbox.open-metadata.org/api/v1
  baseurl_source: declared
  description: The OpenMetadata APIs API from Collate — 1 operation(s) for openmetadata apis.
  name: Collate OpenMetadata APIs API
  slug: collate-openmetadata-apis-api
- baseURL: https://sandbox.open-metadata.org/api/v1
  baseurl_source: declared
  description: APIs related to getting access permission for a User.
  name: Collate Permissions API
  slug: collate-permissions-api
- baseURL: https://sandbox.open-metadata.org/api/v1
  baseurl_source: declared
  description: A `Persona` is to represent job function a user does. OpenMetadata uses Persona to define customizable experience in the UI.
  name: Collate Personas API
  slug: collate-personas-api
- baseURL: https://sandbox.open-metadata.org/api/v1
  baseurl_source: declared
  description: The Pipeline Services API from Collate — 13 operation(s) for pipeline services.
  name: Collate Pipeline Services API
  slug: collate-pipeline-services-api
- baseURL: https://sandbox.open-metadata.org/api/v1
  baseurl_source: declared
  description: A `Pipeline` enables the flow of data from source to destination through a series of processing steps. ETL is a type of pipeline where the series of steps Extract, Transform and Load the data.
  name: Collate Pipelines API
  slug: collate-pipelines-api
- baseURL: https://sandbox.open-metadata.org/api/v1
  baseurl_source: declared
  description: A `Policy` defines control that needs to be applied across different Data Entities.
  name: Collate Policies API
  slug: collate-policies-api
- baseURL: https://sandbox.open-metadata.org/api/v1
  baseurl_source: declared
  description: '`Prompt Templates` are reusable, parameterized templates for LLM interactions that ensure consistent and effective prompting across AI agents.'
  name: Collate Prompt Templates API
  slug: collate-prompt-templates-api
- baseURL: https://sandbox.open-metadata.org/api/v1
  baseurl_source: declared
  description: A `Query` entity represents a SQL query associated with data assets it is run against.
  name: Collate Queries API
  slug: collate-queries-api
- baseURL: https://sandbox.open-metadata.org/api/v1
  baseurl_source: declared
  description: APIs to query cost records from usage workflow.
  name: Collate Query Cost Record Manager API
  slug: collate-query-cost-record-manager-api
- baseURL: https://sandbox.open-metadata.org/api/v1
  baseurl_source: declared
  description: APIs for RDF and SPARQL operations
  name: Collate RDF API
  slug: collate-rdf-api
- baseURL: https://sandbox.open-metadata.org/api/v1
  baseurl_source: declared
  description: APIs related to RDF reindexing failures and status.
  name: Collate RDF Reindex API
  slug: collate-rdf-reindex-api
- baseURL: https://sandbox.open-metadata.org/api/v1
  baseurl_source: declared
  description: Execute SQL queries over RDF data
  name: Collate RDF SQL API
  slug: collate-rdf-sql-api
- baseURL: https://sandbox.open-metadata.org/api/v1
  baseurl_source: declared
  description: '`Reports` are static information computed from data periodically that includes data in text, table, and visual form.'
  name: Collate Reports (beta) API
  slug: collate-reports-beta-api
- baseURL: https://sandbox.open-metadata.org/api/v1
  baseurl_source: declared
  description: A `Role` is a collection of `Policies` that provides access control. A user or a team can be assigned one or multiple roles that provide privileges to a user and members of a team to perform the job f
  name: Collate Roles API
  slug: collate-roles-api
- baseURL: https://sandbox.open-metadata.org/api/v1
  baseurl_source: declared
  description: SCIM 2.0 compliant user and group provisioning endpoints.
  name: Collate SCIM API
  slug: collate-scim-api
- baseURL: https://sandbox.open-metadata.org/api/v1
  baseurl_source: declared
  description: APIs related to search and suggest.
  name: Collate Search API
  slug: collate-search-api
- baseURL: https://sandbox.open-metadata.org/api/v1
  baseurl_source: declared
  description: APIs related to search reindexing failures and status.
  name: Collate Search Reindex API
  slug: collate-search-reindex-api
- baseURL: https://sandbox.open-metadata.org/api/v1
  baseurl_source: declared
  description: APIs related `Search Service` entities, such as ElasticSearch, OpenSearch.
  name: Collate Search Services API
  slug: collate-search-services-api
- baseURL: https://sandbox.open-metadata.org/api/v1
  baseurl_source: declared
  description: APIs related to Security Service entities, such as Apache Ranger.
  name: Collate Security Services API
  slug: collate-security-services-api
- baseURL: https://sandbox.open-metadata.org/api/v1
  baseurl_source: declared
  description: Cross-service-type APIs spanning every kind of service in one request.
  name: Collate Services API
  slug: collate-services-api
- baseURL: https://sandbox.open-metadata.org/api/v1
  baseurl_source: declared
  description: A `Spreadsheet` is a file format for organizing data in a tabular format, like Google Sheets or Excel files.
  name: Collate Spreadsheets API
  slug: collate-spreadsheets-api
- baseURL: https://sandbox.open-metadata.org/api/v1
  baseurl_source: declared
  description: A `StoredProcedure` entity that contains the set of code statements with an assigned name .
  name: Collate Stored Procedures API
  slug: collate-stored-procedures-api
- baseURL: https://sandbox.open-metadata.org/api/v1
  baseurl_source: declared
  description: The Swagger.json API from Collate — 1 operation(s) for swagger.json.
  name: Collate Swagger.json API
  slug: collate-swagger-json-api
- baseURL: https://sandbox.open-metadata.org/api/v1
  baseurl_source: declared
  description: The Swagger.yaml API from Collate — 1 operation(s) for swagger.yaml.
  name: Collate Swagger.yaml API
  slug: collate-swagger-yaml-api
- baseURL: https://sandbox.open-metadata.org/api/v1
  baseurl_source: declared
  description: System diagnostics providing a performance snapshot for load test correlation
  name: Collate System API
  slug: collate-system-api
- baseURL: https://sandbox.open-metadata.org/api/v1
  baseurl_source: declared
  description: '`Table` organizes data in rows and columns and is defined in a `Database Schema`.'
  name: Collate Tables API
  slug: collate-tables-api
- baseURL: https://sandbox.open-metadata.org/api/v1
  baseurl_source: declared
  description: Form schemas for task types
  name: Collate Task Form Schemas API
  slug: collate-task-form-schemas-api
- baseURL: https://sandbox.open-metadata.org/api/v1
  baseurl_source: declared
  description: Tasks for data governance workflows
  name: Collate Tasks API
  slug: collate-tasks-api
- baseURL: https://sandbox.open-metadata.org/api/v1
  baseurl_source: declared
  description: A `Team` is a group of zero or more users and/or other teams. Teams can own zero or more data assets. Hierarchical teams are supported `Organization` -> `BusinessUnit` -> `Division` -> `Department`.
  name: Collate Teams API
  slug: collate-teams-api
- baseURL: https://sandbox.open-metadata.org/api/v1
  baseurl_source: declared
  description: APIs to test case incident status from incident manager.
  name: Collate Test Case Incident Manager API
  slug: collate-test-case-incident-manager-api
- baseURL: https://sandbox.open-metadata.org/api/v1
  baseurl_source: declared
  description: Test case results are the results of running a test case on a dataset. This resource provides APIs to manage test case results.
  name: Collate Test Case Results API
  slug: collate-test-case-results-api
- baseURL: https://sandbox.open-metadata.org/api/v1
  baseurl_source: declared
  description: Test case is a test definition to capture data quality tests against tables, columns, and other data assets.
  name: Collate Test Cases API
  slug: collate-test-cases-api
- baseURL: https://sandbox.open-metadata.org/api/v1
  baseurl_source: declared
  description: '`Test Definition` is a definition of a type of test using which test cases are created that run against data to capture data quality.'
  name: Collate Test Definitions API
  slug: collate-test-definitions-api
- baseURL: https://sandbox.open-metadata.org/api/v1
  baseurl_source: declared
  description: '`TestSuite` is a set of test cases grouped together to capture data quality.'
  name: Collate Test Suites API
  slug: collate-test-suites-api
- baseURL: https://sandbox.open-metadata.org/api/v1
  baseurl_source: declared
  description: Admin-only read-only search introspection for tests
  name: Collate Test Support API
  slug: collate-testsupport-api
- baseURL: https://sandbox.open-metadata.org/api/v1
  baseurl_source: declared
  description: A `Topic` is a feed or an event stream in a `Messaging Service` into which publishers publish messages and consumed by consumers.
  name: Collate Topics API
  slug: collate-topics-api
- baseURL: https://sandbox.open-metadata.org/api/v1
  baseurl_source: declared
  description: APIs related usage of data assets.
  name: Collate Usage API
  slug: collate-usage-api
- baseURL: https://sandbox.open-metadata.org/api/v1
  baseurl_source: declared
  description: 'A `User` represents a user of OpenMetadata. A user can be part of 0 or more teams. A special type of user called Bot is used for automation. A user can be an owner of zero or more data assets. A user '
  name: Collate Users API
  slug: collate-users-api
- baseURL: https://sandbox.open-metadata.org/api/v1
  baseurl_source: declared
  description: APIs for vector-based semantic search.
  name: Collate Vector Search API
  slug: collate-vector-search-api
- baseURL: https://sandbox.open-metadata.org/api/v1
  baseurl_source: declared
  description: A `Workflow Definition` is a configured workflow setup for a given governance task.
  name: Collate Workflow Definitions API
  slug: collate-workflow-definitions-api
- baseURL: https://sandbox.open-metadata.org/api/v1
  baseurl_source: declared
  description: A Workflow Instance State is a specific state of a Workflow Instance.
  name: Collate Workflow Instance States API
  slug: collate-workflow-instance-states-api
- baseURL: https://sandbox.open-metadata.org/api/v1
  baseurl_source: declared
  description: A Workflow Instance is a specific instance of a Workflow Definition.
  name: Collate Workflow Instances API
  slug: collate-workflow-instances-api
- baseURL: https://sandbox.open-metadata.org/api/v1
  baseurl_source: declared
  description: A `Worksheet` is an individual sheet or tab within a Spreadsheet.
  name: Collate Worksheets API
  slug: collate-worksheets-api
- baseURL: https://sandbox.open-metadata.org/api/v1
  baseurl_source: declared
  description: A `SearchIndex` is a index mapping for indexing documents in a `Search Service`.
  name: Collate Search Index API
  slug: collate-search-index-api
artifact_total: 176
asyncapis:
- description: ''
  name: Collate Webhooks
  slug: collate-webhooks
collections:
- collection_type: open
  name: OpenMetadata APIs
  slug: open-collate-openmetadata
common:
- group: agent
  href: https://artifacts.apis.io/collate/agentic-access/collate-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/collate-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/collate/rules/collate-rules.yml
  title: ''
  type: Spectral
  url: rules/collate-rules.yml
- group: design
  href: https://artifacts.apis.io/collate/json-ld/collate-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/collate-context.jsonld
- group: design
  href: https://artifacts.apis.io/collate/vocabulary/collate-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/collate-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/collate/errors/collate-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/collate-problem-types.yml
- group: other
  href: https://artifacts.apis.io/collate/a2a/collate-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/collate-a2a.yml
- group: other
  href: https://artifacts.apis.io/collate/hosts/collate-hosts.yml
  title: ''
  type: Hosts
  url: hosts/collate-hosts.yml
- group: other
  href: https://artifacts.apis.io/collate/vendors/collate-vendors.yml
  title: ''
  type: Vendors
  url: vendors/collate-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.collate.com/
- group: other
  href: https://artifacts.apis.io/collate/capabilities/collate-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/collate-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/collate/overlays/collate-openmetadata-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/collate-openmetadata-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://collate.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.open-metadata.org/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.open-metadata.org/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.open-metadata.org/latest/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.open-metadata.org/latest/quick-start
- group: auth
  href: https://artifacts.apis.io/collate/authentication/collate-authentication.yml
  title: ''
  type: Authentication
  url: authentication/collate-authentication.yml
- group: company
  title: ''
  type: Blog
  url: https://blog.open-metadata.org/
- group: operate
  title: ''
  type: Support
  url: https://open-metadata.org/community
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/open-metadata
- group: start
  title: ''
  type: SignUp
  url: https://collate.com/#demo-request
- group: commercial
  title: ''
  type: TermsOfService
  url: https://collate.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://collate.com/legal/privacy
- group: start
  href: https://artifacts.apis.io/collate/sandbox/collate-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/collate-sandbox.yml
- group: agent
  href: https://artifacts.apis.io/collate/mcp/collate-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/collate-mcp.yml
- group: agent
  href: https://artifacts.apis.io/collate/well-known/collate-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/collate-well-known.yml
- group: auth
  href: https://artifacts.apis.io/collate/well-known/collate-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/collate-security.txt
- group: auth
  href: https://artifacts.apis.io/collate/security/collate-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/collate-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/collate/security/collate-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/collate-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/collate/security/collate-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/collate-domain-security.yml
- group: build
  href: https://artifacts.apis.io/collate/packages/collate-packages.yml
  title: ''
  type: Packages
  url: packages/collate-packages.yml
- group: build
  href: https://artifacts.apis.io/collate/packages/collate-packages.yml
  title: ''
  type: SDKs
  url: packages/collate-packages.yml
- group: build
  href: https://artifacts.apis.io/collate/cli/collate-cli.yml
  title: ''
  type: CLI
  url: cli/collate-cli.yml
- group: operate
  href: https://artifacts.apis.io/collate/changelog/collate-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/collate-changelog.yml
- group: design
  href: https://artifacts.apis.io/collate/lifecycle/collate-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/collate-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/collate/conventions/collate-conventions.yml
  title: ''
  type: Conventions
  url: conventions/collate-conventions.yml
- group: design
  href: https://artifacts.apis.io/collate/conformance/collate-conformance.yml
  title: ''
  type: Conformance
  url: conformance/collate-conformance.yml
- group: design
  href: https://artifacts.apis.io/collate/data-model/collate-data-model.yml
  title: ''
  type: DataModel
  url: data-model/collate-data-model.yml
- group: design
  href: https://artifacts.apis.io/collate/errors/collate-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/collate-error-codes.yml
- group: design
  href: https://artifacts.apis.io/collate/asyncapi/collate-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/collate-webhooks.yml
created: '2026-07-17'
description: Collate is the commercial company behind OpenMetadata, the open-source unified metadata platform and data catalog for data and AI. OpenMetadata provides a single place to discover, govern, observe, and collaborate on data assets — databases, tables, dashboards, pipelines, ML models, topics, containers, and API collections/endpoints — with a JSON-schema-first metadata standard, 90+ ingestion connectors, data quality and profiling, lineage, glossary, and role-based access control. Everything in the product is driven by a comprehensive JWT-authenticated REST API (plus Python and Java SDKs, a `metadata` CLI, webhook change-events, and a hosted MCP server), making the metadata layer fully programmable for humans, AI assistants, and agents. Collate offers a managed, enterprise SaaS edition of OpenMetadata. Backed by CRV and Redpoint Ventures.
image: https://avatars.githubusercontent.com/u/74767841
json_schemas:
- name: ActivityEventList
  property_count: 5
  slug: collate-activity-event-list
- name: ActivityEvent
  property_count: 13
  slug: collate-activity-event
- name: AgentExecutionList
  property_count: 5
  slug: collate-agent-execution-list
- name: AgentExecution
  property_count: 21
  slug: collate-agent-execution
- name: AIApplicationList
  property_count: 5
  slug: collate-aiapplication-list
- name: AIApplication
  property_count: 54
  slug: collate-aiapplication
- name: AIGovernanceBulkTriageRequest
  property_count: 3
  slug: collate-aigovernance-bulk-triage-request
- name: AIGovernancePolicyList
  property_count: 5
  slug: collate-aigovernance-policy-list
- name: AIGovernancePolicy
  property_count: 47
  slug: collate-aigovernance-policy
- name: AIGovernanceTransitionRequest
  property_count: 1
  slug: collate-aigovernance-transition-request
- name: AnnouncementList
  property_count: 5
  slug: collate-announcement-list
- name: Announcement
  property_count: 39
  slug: collate-announcement
- name: ApiService
  property_count: 37
  slug: collate-api-service
- name: APICollectionList
  property_count: 5
  slug: collate-apicollection-list
- name: APICollection
  property_count: 35
  slug: collate-apicollection
- name: APIEndpointList
  property_count: 5
  slug: collate-apiendpoint-list
- name: APIEndpoint
  property_count: 38
  slug: collate-apiendpoint
- name: APIServiceList
  property_count: 5
  slug: collate-apiservice-list
- name: AppMarketPlaceDefinition
  property_count: 55
  slug: collate-app-market-place-definition
- name: AppRunRecord
  property_count: 15
  slug: collate-app-run-record
- name: App
  property_count: 60
  slug: collate-app
- name: AssetKey
  property_count: 2
  slug: collate-asset-key
- name: AssetKnowledge
  property_count: 3
  slug: collate-asset-knowledge
- name: BotList
  property_count: 5
  slug: collate-bot-list
- name: Bot
  property_count: 33
  slug: collate-bot
- name: BulkColumnUpdateRequest
  property_count: 11
  slug: collate-bulk-column-update-request
- name: BulkOperationResult
  property_count: 8
  slug: collate-bulk-operation-result
- name: ChangeEvent
  property_count: 15
  slug: collate-change-event
- name: ChartList
  property_count: 5
  slug: collate-chart-list
- name: Chart
  property_count: 36
  slug: collate-chart
- name: Classification
  property_count: 37
  slug: collate-classification
- name: Column
  property_count: 18
  slug: collate-column
- name: CreateAIApplication
  property_count: 30
  slug: collate-create-aiapplication
- name: CreateAIFrameworkControl
  property_count: 14
  slug: collate-create-aiframework-control
- name: CreateAIGovernanceFramework
  property_count: 19
  slug: collate-create-aigovernance-framework
- name: CreateAIGovernancePolicy
  property_count: 20
  slug: collate-create-aigovernance-policy
- name: CreateAnnouncement
  property_count: 7
  slug: collate-create-announcement
- name: CreateApiService
  property_count: 13
  slug: collate-create-api-service
- name: CreateAPICollection
  property_count: 14
  slug: collate-create-apicollection
- name: CreateAPIEndpoint
  property_count: 17
  slug: collate-create-apiendpoint
- name: CreateAppMarketPlaceDefinitionReq
  property_count: 33
  slug: collate-create-app-market-place-definition-req
- name: CreateApp
  property_count: 16
  slug: collate-create-app
- name: CreateAuditReport
  property_count: 16
  slug: collate-create-audit-report
- name: CreateBot
  property_count: 13
  slug: collate-create-bot
- name: CreateChart
  property_count: 15
  slug: collate-create-chart
- name: CreateClassification
  property_count: 13
  slug: collate-create-classification
- name: CreateTag
  property_count: 19
  slug: collate-create-tag
- name: CSVExportResponse
  property_count: 2
  slug: collate-csvexport-response
- name: EntityHistory
  property_count: 2
  slug: collate-entity-history
- name: ForkAIGovernanceFrameworkRequest
  property_count: 2
  slug: collate-fork-aigovernance-framework-request
- name: FormDataContentDisposition
  property_count: 8
  slug: collate-form-data-content-disposition
- name: FoundContext
  property_count: 3
  slug: collate-found-context
- name: IntakeChecksResponse
  property_count: 1
  slug: collate-intake-checks-response
- name: JsonPatch
  property_count: 0
  slug: collate-json-patch
- name: RecognizerFeedback
  property_count: 13
  slug: collate-recognizer-feedback
- name: Response
  property_count: 17
  slug: collate-response
- name: RestoreEntity
  property_count: 1
  slug: collate-restore-entity
- name: ResultList
  property_count: 5
  slug: collate-result-list
- name: Tag
  property_count: 41
  slug: collate-tag
- name: TestConnectionResult
  property_count: 3
  slug: collate-test-connection-result
jsonld:
- class_count: 120
  name: Collate Context
  property_count: 478
  slug: collate-context
layout: provider
mcp_servers:
- description: OpenMetadata (the product Collate commercializes) ships a hosted, remote MCP (Model Context Protocol) server. The public sandbox exposes it at https://sandbox.open-metadata.org/mcp and advertises a fu
  name: Collate MCP Server
  slug: openmetadata
modified: '2026-07-18'
name: Collate
nav: Providers
network: true
overview: 'Collate publishes 107 API contracts indexed on the [APIs.io](https://apis.io/) network, including Activity Stream API, Agent Executions API, AI Applications API, and 104 more. Tagged areas include Company, Data, Metadata, Data Catalog, and Data Governance.


  The Collate catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Collate''s developer surface includes documentation, API reference, getting-started guide, authentication, engineering blog, support, signup flow, and 33 more developer resources.'
random_paper: 20
rules:
- authorship: generated
  effective_rule_count: 104
  extends:
  - spectral:oas
  name: Collate API Rules
  rule_count: 63
  severity_counts:
    error: 45
    hint: 0
    info: 5
    warn: 13
  slug: collate-rules
score:
  band: strong
  composite: 64.8
  coverage:
    artifact_dirs: 32
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 6.9
  facets:
    access_clarity: 27.6
    contract_governance: 35.6
    contract_quality: 69.2
    developer_ergonomics: 78.6
    discoverability: 75.0
    operational_transparency: 52.6
  previous_composite: 57.9
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 99.1
      total: 108
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: rising
  upsert:
    applies: true
    score: 61.1
screenshot: https://apis.io/screenshots/collate/collate-2026-07-25T210043.png
security:
- kind: authentication
  name: Collate Authentication
  slug: collate-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Collate Domain Security
  slug: collate-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Collate Vulnerability Disclosure
  slug: collate-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: collate
tags:
- Company
- Data
- Metadata
- Data Catalog
- Data Governance
- Data Discovery
- Data Quality
- Data Lineage
- Open Source
website: https://collate.com/
---
