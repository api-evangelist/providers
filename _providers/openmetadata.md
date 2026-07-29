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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: true
    error_semantics: verified
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 44.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 848
  human_in_the_loop: 12
  name: Openmetadata Agentic Access
  operation_count: 1479
  slug: openmetadata-agentic-access
  summary_line: 1479 operations · 848 acting · 12 human-in-the-loop
api_count: 89
apis:
- description: '`Agent Executions` are time-series records of AI agent execution runs, capturing observability metrics, governance checks, and performance data.'
  name: OpenMetadata Agent Executions API
  slug: openmetadata-agent-executions-api
- description: '`AI Applications` are autonomous software entities that use LLM models to perform tasks, make decisions, and interact with data sources.'
  name: OpenMetadata AI Applications API
  slug: openmetadata-ai-applications-api
- description: '`AI Governance Policies` define rules, compliance requirements, bias thresholds, and control measures for AI agents and models.'
  name: OpenMetadata AI Governance Policies API
  slug: openmetadata-ai-governance-policies-api
- description: A `API Collection` is an optional way of grouping API Endpoints that belong to a API Service.
  name: OpenMetadata API Collections API
  slug: openmetadata-api-collections-api
- description: A `API Endpoint` is a specific endpoint of an API that is part of an API Collection..
  name: OpenMetadata API Endpoint API
  slug: openmetadata-api-endpoint-api
- description: APIs related `API Service` entities, such as REST or MicroService.
  name: OpenMetadata API Services API
  slug: openmetadata-api-services-api
- description: Apps marketplace holds to application available for Open-metadata
  name: OpenMetadata Apps API
  slug: openmetadata-apps-api
- description: APIs for listing user initiated change events persisted for auditing
  name: OpenMetadata Audit Logs API
  slug: openmetadata-audit-logs-api
- description: A `Bot` automates tasks, such as ingesting metadata, and running data quality It performs this task as a special user in the system.
  name: OpenMetadata Bots API
  slug: openmetadata-bots-api
- description: APIs to retrieve change summary metadata for entities. Change summary tracks who changed each field, the source of the change (e.g., Suggested for AI-generated, Manual for user edits), and when the ch
  name: OpenMetadata ChangeSummary API
  slug: openmetadata-changesummary-api
- description: A `Chart` are computed from data presents data visually and can be part of `Dashboards`.
  name: OpenMetadata Charts API
  slug: openmetadata-charts-api
- description: These APIs are related to `Classification` and `Tags`. A `Classification` entity contains hierarchical terms called `Tags` used for categorizing and classifying data assets and other entities.
  name: OpenMetadata Classifications API
  slug: openmetadata-classifications-api
- description: Columns represent individual data fields within tables and dashboard data models. This API provides operations to update column metadata such as tags, glossary terms, descriptions, and other propertie
  name: OpenMetadata Columns API
  slug: openmetadata-columns-api
- description: A Container is an abstraction for any path(including the top level eg. bucket in S3) storing data in an Object store such as S3, GCP, Azure. It maps a tree-like structure, where each Container can hav
  name: OpenMetadata Containers API
  slug: openmetadata-containers-api
- description: '`Data Models` are the schemas used to build dashboards, charts, or other data assets.'
  name: OpenMetadata Dashboard Data Models API
  slug: openmetadata-dashboard-data-models-api
- description: The Dashboard Services API from OpenMetadata — 12 operation(s) for dashboard services.
  name: OpenMetadata Dashboard Services API
  slug: openmetadata-dashboard-services-api
- description: Dashboards are computed from data and visually present data, metrics, and KPIs. They are typically updated in real-time and allow interactive data exploration.
  name: OpenMetadata Dashboards API
  slug: openmetadata-dashboards-api
- description: '`DataContract` defines the schema and quality guarantees for a data asset.'
  name: OpenMetadata Data Contracts API
  slug: openmetadata-data-contracts-api
- description: APIs to retrieve dimensional test case results data.
  name: OpenMetadata Data Quality API
  slug: openmetadata-data-quality-api
- description: A `Database Schema` is collection of tables, views, stored procedures, and other database objects.
  name: OpenMetadata Database Schemas API
  slug: openmetadata-database-schemas-api
- description: '`Database Service` is a service such as MySQL, BigQuery, Redshift, Postgres, or Snowflake. Alternative terms such as Database Cluster, Database Server instance are also used for database service.'
  name: OpenMetadata Database Services API
  slug: openmetadata-database-services-api
- description: A `Database` also referred to as `Database Catalog` is a collection of schemas.
  name: OpenMetadata Databases API
  slug: openmetadata-databases-api
- description: A `Directory` is a folder or organizational unit in a Drive Service that can contain files, spreadsheets, and other directories.
  name: OpenMetadata Directories API
  slug: openmetadata-directories-api
- description: A `Document` is an generic entity in OpenMetadata.
  name: OpenMetadata Document Store API
  slug: openmetadata-document-store-api
- description: A `Data Product` or `Data as a Product` is a logical unit that contains all components to process and store domain data for analytical or data-intensive use cases made available to data consumers.
  name: OpenMetadata Domains API
  slug: openmetadata-domains-api
- description: '`Drive Service` is a cloud file storage service such as Google Drive, OneDrive, SharePoint, Box, or Dropbox where documents, spreadsheets, and other files are stored.'
  name: OpenMetadata Drive Services API
  slug: openmetadata-drive-services-api
- description: The `Events` are changes to metadata and are sent when entities are created, modified, or updated. External systems can subscribe to events using event subscription API over Webhooks, Slack, or Micros
  name: OpenMetadata Events API
  slug: openmetadata-events-api
- description: Feeds API supports `Activity Feeds` and `Conversation Threads`.
  name: OpenMetadata Feeds API
  slug: openmetadata-feeds-api
- description: A `File` is a document or resource stored in a Drive Service.
  name: OpenMetadata Files API
  slug: openmetadata-files-api
- description: A `Glossary` is collection of hierarchical `GlossaryTerms`.
  name: OpenMetadata Glossaries API
  slug: openmetadata-glossaries-api
- description: APIs related pipelines/workflows created by the system to ingest metadata.
  name: OpenMetadata Ingestion Pipelines API
  slug: openmetadata-ingestion-pipelines-api
- description: The ingestionPipelines API from OpenMetadata — 1 operation(s) for ingestionpipelines.
  name: OpenMetadata ingestionPipelines API
  slug: openmetadata-ingestionpipelines-api
- description: Inline tutorials and expert content surfaced across OpenMetadata product surfaces.
  name: OpenMetadata Learning Resources API
  slug: openmetadata-learning-resources-api
- description: The `Lineage` for a given data asset, has information of the input datasets used and the ETL pipeline that created it.
  name: OpenMetadata Lineage API
  slug: openmetadata-lineage-api
- description: '`LLM Models` are Large Language Model instances such as GPT-4, Claude, Llama, or custom-trained models used for AI applications.'
  name: OpenMetadata LLM Models API
  slug: openmetadata-llm-models-api
- description: '`LLM Service` is a service for Large Language Model providers such as OpenAI, Anthropic, Azure OpenAI, AWS Bedrock, Google Vertex AI, or custom LLM deployments.'
  name: OpenMetadata LLM Services API
  slug: openmetadata-llm-services-api
- description: '`MCP Executions` are time-series records of MCP server execution sessions, capturing tool calls, resource accesses, data lineage, compliance checks, and audit trails for AI governance.'
  name: OpenMetadata MCP Executions API
  slug: openmetadata-mcp-executions-api
- description: '`MCP Servers` are Model Context Protocol servers that expose tools, resources, and prompts for AI applications. They enable AI governance including risk assessment, compliance tracking, and shadow AI '
  name: OpenMetadata MCP Servers API
  slug: openmetadata-mcp-servers-api
- description: '`MCP Service` is a service for discovering and managing MCP (Model Context Protocol) servers, their tools, resources, and prompts for AI governance.'
  name: OpenMetadata MCP Services API
  slug: openmetadata-mcp-services-api
- description: MCP tool-call usage counters and breakdowns.
  name: OpenMetadata MCP Usage API
  slug: openmetadata-mcp-usage-api
- description: The Messaging Services API from OpenMetadata — 12 operation(s) for messaging services.
  name: OpenMetadata Messaging Services API
  slug: openmetadata-messaging-services-api
- description: These APIs are for managing custom property definitions in OpenMetadata. Use these APIs to create custom properties with predefined data types (String, Integer, Date, etc.) that extend entity metadata
  name: OpenMetadata Metadata API
  slug: openmetadata-metadata-api
- description: APIs related to creating and managing other Metadata Services that OpenMetadata integrates with such as `Apache Atlas`, `Amundsen`, etc.
  name: OpenMetadata Metadata Services API
  slug: openmetadata-metadata-services-api
- description: '`Metrics` are measurements computed from data such as `Monthly Active Users`. Some of the metrics that measures used to determine performance against an objective are called KPIs or Key Performance In'
  name: OpenMetadata Metrics API
  slug: openmetadata-metrics-api
- description: The ML Model Services API from OpenMetadata — 12 operation(s) for ml model services.
  name: OpenMetadata ML Model Services API
  slug: openmetadata-ml-model-services-api
- description: '`Machine Learning Models` are algorithms trained on data to find patterns or make predictions.'
  name: OpenMetadata ML Models API
  slug: openmetadata-ml-models-api
- description: Notification templates for customizing event notifications
  name: OpenMetadata Notification Templates API
  slug: openmetadata-notification-templates-api
- description: APIs related `Object Store Service` entities, such as S3, GCS or AZURE.
  name: OpenMetadata Object Store Services API
  slug: openmetadata-object-store-services-api
- description: OpenLineage API for receiving lineage events from external systems like Spark, Airflow, etc.
  name: OpenMetadata OpenLineage API
  slug: openmetadata-openlineage-api
- description: The OpenMetadata APIs API from OpenMetadata — 1 operation(s) for openmetadata apis.
  name: OpenMetadata OpenMetadata APIs API
  slug: openmetadata-openmetadata-apis-api
- description: APIs related to getting access permission for a User.
  name: OpenMetadata Permissions API
  slug: openmetadata-permissions-api
- description: A `Persona` is to represent job function a user does. OpenMetadata uses Persona to define customizable experience in the UI.
  name: OpenMetadata Personas API
  slug: openmetadata-personas-api
- description: The Pipeline Services API from OpenMetadata — 11 operation(s) for pipeline services.
  name: OpenMetadata Pipeline Services API
  slug: openmetadata-pipeline-services-api
- description: A `Pipeline` enables the flow of data from source to destination through a series of processing steps. ETL is a type of pipeline where the series of steps Extract, Transform and Load the data.
  name: OpenMetadata Pipelines API
  slug: openmetadata-pipelines-api
- description: A `Policy` defines control that needs to be applied across different Data Entities.
  name: OpenMetadata Policies API
  slug: openmetadata-policies-api
- description: '`Prompt Templates` are reusable, parameterized templates for LLM interactions that ensure consistent and effective prompting across AI agents.'
  name: OpenMetadata Prompt Templates API
  slug: openmetadata-prompt-templates-api
- description: A `Query` entity represents a SQL query associated with data assets it is run against.
  name: OpenMetadata Queries API
  slug: openmetadata-queries-api
- description: APIs to query cost records from usage workflow.
  name: OpenMetadata Query Cost Record Manager API
  slug: openmetadata-query-cost-record-manager-api
- description: APIs for RDF and SPARQL operations
  name: OpenMetadata RDF API
  slug: openmetadata-rdf-api
- description: Execute SQL queries over RDF data
  name: OpenMetadata RDF SQL API
  slug: openmetadata-rdf-sql-api
- description: '`Reports` are static information computed from data periodically that includes data in text, table, and visual form.'
  name: OpenMetadata Reports (beta) API
  slug: openmetadata-reports-beta-api
- description: A `Role` is a collection of `Policies` that provides access control. A user or a team can be assigned one or multiple roles that provide privileges to a user and members of a team to perform the job f
  name: OpenMetadata Roles API
  slug: openmetadata-roles-api
- description: SCIM 2.0 compliant user and group provisioning endpoints.
  name: OpenMetadata SCIM API
  slug: openmetadata-scim-api
- description: APIs related to search and suggest.
  name: OpenMetadata Search API
  slug: openmetadata-search-api
- description: APIs related to search reindexing failures and status.
  name: OpenMetadata Search Reindex API
  slug: openmetadata-search-reindex-api
- description: APIs related `Search Service` entities, such as ElasticSearch, OpenSearch.
  name: OpenMetadata Search Services API
  slug: openmetadata-search-services-api
- description: A `SearchIndex` is a index mapping for indexing documents in a `Search Service`.
  name: OpenMetadata SearchIndex API
  slug: openmetadata-searchindex-api
- description: APIs related to Security Service entities, such as Apache Ranger.
  name: OpenMetadata Security Services API
  slug: openmetadata-security-services-api
- description: A `Spreadsheet` is a file format for organizing data in a tabular format, like Google Sheets or Excel files.
  name: OpenMetadata Spreadsheets API
  slug: openmetadata-spreadsheets-api
- description: A `StoredProcedure` entity that contains the set of code statements with an assigned name .
  name: OpenMetadata Stored Procedures API
  slug: openmetadata-stored-procedures-api
- description: Suggestions API supports ability to add suggestion for descriptions or tag labels for Entities.
  name: OpenMetadata Suggestions API
  slug: openmetadata-suggestions-api
- description: The Swagger.json API from OpenMetadata — 1 operation(s) for swagger.json.
  name: OpenMetadata Swagger.json API
  slug: openmetadata-swagger-json-api
- description: The Swagger.yaml API from OpenMetadata — 1 operation(s) for swagger.yaml.
  name: OpenMetadata Swagger.yaml API
  slug: openmetadata-swagger-yaml-api
- description: System diagnostics providing a performance snapshot for load test correlation
  name: OpenMetadata System API
  slug: openmetadata-system-api
- description: '`Table` organizes data in rows and columns and is defined in a `Database Schema`.'
  name: OpenMetadata Tables API
  slug: openmetadata-tables-api
- description: A `Team` is a group of zero or more users and/or other teams. Teams can own zero or more data assets. Hierarchical teams are supported `Organization` -> `BusinessUnit` -> `Division` -> `Department`.
  name: OpenMetadata Teams API
  slug: openmetadata-teams-api
- description: APIs to test case incident status from incident manager.
  name: OpenMetadata Test Case Incident Manager API
  slug: openmetadata-test-case-incident-manager-api
- description: Test case results are the results of running a test case on a dataset. This resource provides APIs to manage test case results.
  name: OpenMetadata Test Case Results API
  slug: openmetadata-test-case-results-api
- description: Test case is a test definition to capture data quality tests against tables, columns, and other data assets.
  name: OpenMetadata Test Cases API
  slug: openmetadata-test-cases-api
- description: '`Test Definition` is a definition of a type of test using which test cases are created that run against data to capture data quality.'
  name: OpenMetadata Test Definitions API
  slug: openmetadata-test-definitions-api
- description: '`TestSuite` is a set of test cases grouped together to capture data quality.'
  name: OpenMetadata Test Suites API
  slug: openmetadata-test-suites-api
- description: A `Topic` is a feed or an event stream in a `Messaging Service` into which publishers publish messages and consumed by consumers.
  name: OpenMetadata Topics API
  slug: openmetadata-topics-api
- description: APIs related usage of data assets.
  name: OpenMetadata Usage API
  slug: openmetadata-usage-api
- description: 'A `User` represents a user of OpenMetadata. A user can be part of 0 or more teams. A special type of user called Bot is used for automation. A user can be an owner of zero or more data assets. A user '
  name: OpenMetadata Users API
  slug: openmetadata-users-api
- description: APIs for vector-based semantic search.
  name: OpenMetadata Vector Search API
  slug: openmetadata-vector-search-api
- description: A `Workflow Definition` is a configured workflow setup for a given governance task.
  name: OpenMetadata Workflow Definitions API
  slug: openmetadata-workflow-definitions-api
- description: A Workflow Instance State is a specific state of a Workflow Instance.
  name: OpenMetadata Workflow Instance States API
  slug: openmetadata-workflow-instance-states-api
- description: A Workflow Instance is a specific instance of a Workflow Definition.
  name: OpenMetadata Workflow Instances API
  slug: openmetadata-workflow-instances-api
- description: A `Worksheet` is an individual sheet or tab within a Spreadsheet.
  name: OpenMetadata Worksheets API
  slug: openmetadata-worksheets-api
artifact_total: 129
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/openmetadata-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/openmetadata-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/openmetadata-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://open-metadata.org
- group: docs
  title: ''
  type: Documentation
  url: https://docs.open-metadata.org
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/open-metadata
- group: build
  title: ''
  type: GitHub
  url: https://github.com/open-metadata/OpenMetadata
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/openmetadata
- group: company
  title: ''
  type: Blog
  url: https://blog.open-metadata.org
- group: other
  title: ''
  type: X
  url: https://twitter.com/open_metadata
- group: commercial
  title: ''
  type: Pricing
  url: https://www.getcollate.io/pricing
- group: operate
  title: ''
  type: Slack
  url: https://slack.open-metadata.org
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@OpenMetadataChannel
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://open-metadata.org/product-updates
- group: build
  title: ''
  type: SDKs
  url: https://github.com/open-metadata/openmetadata-sdk
- group: build
  title: ''
  type: PythonSDK
  url: https://pypi.org/project/openmetadata-ingestion/
- group: commercial
  title: ''
  type: Plans
  url: plans/openmetadata-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/openmetadata-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/openmetadata-finops.yml
created: 2026-06-13
description: OpenMetadata is an open-source data catalog and metadata platform providing a comprehensive REST API for managing tables, dashboards, pipelines, data quality, lineage, and governance policies. It serves as an open context layer for data and AI, unifying technical metadata, business semantics, and organizational memory into a unified graph for both human and AI decision-making.
examples:
- key_count: 5
  name: Createglossaryterm Example
  slug: createglossaryterm-example
- key_count: 5
  name: Createtable Example
  slug: createtable-example
- key_count: 5
  name: Createtestcase Example
  slug: createtestcase-example
- key_count: 5
  name: Getdashboardbyfqn Example
  slug: getdashboardbyfqn-example
- key_count: 5
  name: Getlineage Example
  slug: getlineage-example
- key_count: 5
  name: Gettablebyfqn Example
  slug: gettablebyfqn-example
- key_count: 5
  name: Listdashboards Example
  slug: listdashboards-example
- key_count: 5
  name: Listtables Example
  slug: listtables-example
- key_count: 5
  name: Listteams Example
  slug: listteams-example
- key_count: 5
  name: Listtestcases Example
  slug: listtestcases-example
- key_count: 5
  name: Listusers Example
  slug: listusers-example
finops:
- name: Openmetadata Finops
  service_category: ''
  slug: openmetadata-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/openmetadata.png
json_schemas:
- name: Changeevent
  property_count: 14
  slug: changeevent
- name: Chart
  property_count: 36
  slug: chart
- name: Classification
  property_count: 36
  slug: classification
- name: Container
  property_count: 43
  slug: container
- name: Dashboard
  property_count: 38
  slug: dashboard
- name: Database
  property_count: 39
  slug: database
- name: Databaseschema
  property_count: 38
  slug: databaseschema
- name: Dataqualityreport
  property_count: 2
  slug: dataqualityreport
- name: Entityreference
  property_count: 9
  slug: entityreference
- name: Glossaryterm
  property_count: 41
  slug: glossaryterm
- name: Mlmodel
  property_count: 41
  slug: mlmodel
- name: Pipeline
  property_count: 42
  slug: pipeline
- name: Policy
  property_count: 39
  slug: policy
- name: Searchindex
  property_count: 37
  slug: searchindex
- name: Storedprocedure
  property_count: 40
  slug: storedprocedure
- name: Table
  property_count: 58
  slug: table
- name: Tag
  property_count: 40
  slug: tag
- name: Team
  property_count: 45
  slug: team
- name: Testcase
  property_count: 47
  slug: testcase
- name: Topic
  property_count: 44
  slug: topic
- name: User
  property_count: 52
  slug: user
jsonld:
- class_count: 36
  name: Openmetadata Context
  property_count: 31
  slug: openmetadata-context
layout: provider
modified: 2026-06-13
name: OpenMetadata
nav: Providers
network: true
overview: 'OpenMetadata publishes 89 APIs on the [APIs.io](https://apis.io/) network, including Agent Executions API, AI Applications API, AI Governance Policies API, and 86 more. Tagged areas include Data Catalog, Metadata, Data Governance, Data Lineage, and Data Quality.


  The OpenMetadata catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  OpenMetadata''s developer surface includes authentication, documentation, GitHub presence, engineering blog, pricing, YouTube channel, release notes, and 12 more developer resources.'
plans:
- name: Openmetadata Plans Pricing
  plan_count: 5
  slug: openmetadata-plans-pricing
random_paper: 35
rate_limits:
- limit_count: 0
  name: Openmetadata Rate Limits
  slug: openmetadata-rate-limits
rules:
- name: OpenMetadata API Rules
  rule_count: 4
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 3
  slug: openmetadata-jsonschema-spectral-rules
score:
  band: developing
  composite: 45.6
  delta: -5.5
  facets:
    commercial_clarity: 50.0
    contract_quality: 53.6
    developer_ergonomics: 28.3
    discoverability: 68.5
    governance: 58.3
    operational_transparency: 21.1
  previous_composite: 51.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 89
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/openmetadata/refs/heads/main/screenshots/openmetadata-2026-06-20T191017.png
security:
- kind: authentication
  name: Openmetadata Authentication
  slug: openmetadata-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Openmetadata Domain Security
  slug: openmetadata-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: openmetadata
tags:
- Data Catalog
- Metadata
- Data Governance
- Data Lineage
- Data Quality
- Open Source
- Data Discovery
- Data Observability
website: https://open-metadata.org
---
