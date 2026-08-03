---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 44.1
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 14
  human_in_the_loop: 1
  name: Informatica Agentic Access
  operation_count: 28
  slug: informatica-agentic-access
  summary_line: 28 operations · 14 acting · 1 human-in-the-loop
api_count: 12
apis:
- description: The Data Integration REST API provides programmatic access to manage data integration assets and operations, including connections, mappings, mapping tasks, dynamic mapping tasks, taskflows, code task
  name: Informatica Data Integration REST API
  slug: data-integration-rest-api
- description: 'The Cloud Data Governance and Catalog API enables programmatic creation and management of assets, searching for assets, and viewing asset details within Informatica Data Governance and Catalog. Calls '
  name: Informatica Cloud Data Governance and Catalog API
  slug: cloud-data-governance-and-catalog-api
- description: The Cloud Data Profiling REST API allows interaction with the Data Profiling Service through API calls to create, delete, update, and run queries and profiles within your organization. Supports platfo
  name: Informatica Cloud Data Profiling REST API
  slug: cloud-data-profiling-rest-api
- description: The Cloud Address Verification API is a REST API-based solution for verifying and validating postal addresses in real time. You can integrate the Address Verification service API endpoints into your a
  name: Informatica Cloud Address Verification API
  slug: cloud-address-verification-api
- description: The B2B Gateway REST APIs enable running inbound and outbound partner flows, querying the status of events, and getting control numbers for outbound EDI X12 and EDIFACT messages through programmatic A
  name: Informatica B2B Gateway REST API
  slug: b2b-gateway-rest-api
- description: 'The Reference 360 REST API enables programmatic management of reference data, including exporting and importing reference data sets, managing code values and value mappings, retrieving asset details, '
  name: Informatica Reference 360 REST API
  slug: reference-360-rest-api
- description: Login and session management operations.
  name: Informatica Authentication API
  slug: informatica-authentication-api
- description: Manage connections to data sources and targets including databases, flat files, cloud applications, and SaaS services.
  name: Informatica Connections API
  slug: informatica-connections-api
- description: Start, stop, and monitor job execution for tasks, taskflows, and other runnable assets.
  name: Informatica Jobs API
  slug: informatica-jobs-api
- description: Create, retrieve, update, and delete mapping task configurations that execute mappings with specific runtime parameters.
  name: Informatica Mapping Tasks API
  slug: informatica-mapping-tasks-api
- description: Retrieve mapping definitions and metadata for data integration mappings within the organization.
  name: Informatica Mappings API
  slug: informatica-mappings-api
- description: Manage task execution schedules.
  name: Informatica Schedules API
  slug: informatica-schedules-api
artifact_total: 144
collections:
- collection_type: open
  name: Informatica IICS Platform REST API
  slug: open-informatica-platform-rest-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/informatica-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/informatica-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/informatica-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/informatica
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/informatica
- group: start
  title: ''
  type: Portal
  url: https://developer.informatica.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.informatica.com/
- group: other
  title: ''
  type: KnowledgeCenter
  url: https://knowledge.informatica.com/
- group: operate
  title: ''
  type: Support
  url: https://www.informatica.com/support.html
- group: operate
  title: Community
  type: Support
  url: https://network.informatica.com/
- group: start
  title: ''
  type: Login
  url: https://dm-us.informaticacloud.com/identity-service/home
- group: design
  title: ''
  type: SpectralRules
  url: rules/informatica-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/informatica-vocabulary.yaml
- group: company
  title: ''
  type: Blog
  url: https://www.informatica.com/blogs.html
created: '2025-01-08'
description: Collection of APIs for Informatica Intelligent Cloud Services (IICS) and Intelligent Data Management Cloud (IDMC), providing programmatic access to data integration, data governance, data quality, master data management, B2B gateway, and platform administration capabilities.
examples:
- key_count: 6
  name: Informatica Createconnection Example
  slug: informatica-createconnection-example
- key_count: 6
  name: Informatica Createmappingtask Example
  slug: informatica-createmappingtask-example
- key_count: 6
  name: Informatica Createschedule Example
  slug: informatica-createschedule-example
- key_count: 6
  name: Informatica Deleteconnection Example
  slug: informatica-deleteconnection-example
- key_count: 6
  name: Informatica Deletemappingtask Example
  slug: informatica-deletemappingtask-example
- key_count: 6
  name: Informatica Getactivitylog Example
  slug: informatica-getactivitylog-example
- key_count: 6
  name: Informatica Getconnection Example
  slug: informatica-getconnection-example
- key_count: 6
  name: Informatica Getconnectionbyname Example
  slug: informatica-getconnectionbyname-example
- key_count: 6
  name: Informatica Getmapping Example
  slug: informatica-getmapping-example
- key_count: 6
  name: Informatica Getmappingbyname Example
  slug: informatica-getmappingbyname-example
- key_count: 6
  name: Informatica Getmappingtask Example
  slug: informatica-getmappingtask-example
- key_count: 6
  name: Informatica Getmappingtaskbyname Example
  slug: informatica-getmappingtaskbyname-example
- key_count: 6
  name: Informatica Getschedule Example
  slug: informatica-getschedule-example
- key_count: 6
  name: Informatica Listconnections Example
  slug: informatica-listconnections-example
- key_count: 6
  name: Informatica Listmappings Example
  slug: informatica-listmappings-example
- key_count: 6
  name: Informatica Listmappingtasks Example
  slug: informatica-listmappingtasks-example
- key_count: 6
  name: Informatica Listschedules Example
  slug: informatica-listschedules-example
- key_count: 6
  name: Informatica Login Example
  slug: informatica-login-example
- key_count: 6
  name: Informatica Logout Example
  slug: informatica-logout-example
- key_count: 20
  name: Informatica Platform Rest Activity Log Entry Example
  slug: informatica-platform-rest-activity-log-entry-example
- key_count: 15
  name: Informatica Platform Rest Connection Create Request Example
  slug: informatica-platform-rest-connection-create-request-example
- key_count: 22
  name: Informatica Platform Rest Connection Example
  slug: informatica-platform-rest-connection-example
- key_count: 13
  name: Informatica Platform Rest Connection Update Request Example
  slug: informatica-platform-rest-connection-update-request-example
- key_count: 5
  name: Informatica Platform Rest Error Response Example
  slug: informatica-platform-rest-error-response-example
- key_count: 6
  name: Informatica Platform Rest Job Start Request Example
  slug: informatica-platform-rest-job-start-request-example
- key_count: 3
  name: Informatica Platform Rest Job Start Response Example
  slug: informatica-platform-rest-job-start-response-example
- key_count: 5
  name: Informatica Platform Rest Job Stop Request Example
  slug: informatica-platform-rest-job-stop-request-example
- key_count: 3
  name: Informatica Platform Rest Login Request Example
  slug: informatica-platform-rest-login-request-example
- key_count: 16
  name: Informatica Platform Rest Login Response Example
  slug: informatica-platform-rest-login-response-example
- key_count: 23
  name: Informatica Platform Rest Mapping Example
  slug: informatica-platform-rest-mapping-example
- key_count: 10
  name: Informatica Platform Rest Mapping In Out Parameter Example
  slug: informatica-platform-rest-mapping-in-out-parameter-example
- key_count: 6
  name: Informatica Platform Rest Mapping Parameter Example
  slug: informatica-platform-rest-mapping-parameter-example
- key_count: 11
  name: Informatica Platform Rest Mapping Task Create Request Example
  slug: informatica-platform-rest-mapping-task-create-request-example
- key_count: 19
  name: Informatica Platform Rest Mapping Task Example
  slug: informatica-platform-rest-mapping-task-example
- key_count: 10
  name: Informatica Platform Rest Mapping Task Update Request Example
  slug: informatica-platform-rest-mapping-task-update-request-example
- key_count: 8
  name: Informatica Platform Rest Schedule Create Request Example
  slug: informatica-platform-rest-schedule-create-request-example
- key_count: 18
  name: Informatica Platform Rest Schedule Example
  slug: informatica-platform-rest-schedule-example
- key_count: 6
  name: Informatica Searchconnections Example
  slug: informatica-searchconnections-example
- key_count: 6
  name: Informatica Searchmappings Example
  slug: informatica-searchmappings-example
- key_count: 6
  name: Informatica Startjob Example
  slug: informatica-startjob-example
- key_count: 6
  name: Informatica Stopjob Example
  slug: informatica-stopjob-example
- key_count: 6
  name: Informatica Testconnection Example
  slug: informatica-testconnection-example
- key_count: 6
  name: Informatica Updateconnection Example
  slug: informatica-updateconnection-example
- key_count: 6
  name: Informatica Updatemappingtask Example
  slug: informatica-updatemappingtask-example
- key_count: 6
  name: Informatica Updateschedule Example
  slug: informatica-updateschedule-example
features:
- description: Connect, transform, and move data across cloud and on-premises environments using visual mapping interfaces.
  name: Data Integration
- description: Discover, catalog, and govern data assets with automated classification and lineage tracking.
  name: Data Governance
- description: Profile, cleanse, standardize, and validate data to ensure accuracy and consistency.
  name: Data Quality
- description: Create and manage golden records for critical business entities across the enterprise.
  name: Master Data Management
- description: Validate and standardize postal addresses globally in real time.
  name: Address Verification
- description: Exchange EDI documents with trading partners using X12, EDIFACT, and other B2B protocols.
  name: B2B Gateway
- description: Manage code lists, crosswalks, and hierarchies for standardized reference data across systems.
  name: Reference Data Management
- description: Build and manage API-led integrations connecting SaaS, cloud, and on-premises applications.
  name: API and Application Integration
finops:
- name: Informatica Finops
  service_category: Data Integration + Management
  slug: informatica-finops
image: https://companieslogo.com/img/orig/INFA-3e1d4e5a.png
integrations:
- description: Native connectors for bidirectional data integration with Salesforce CRM and platform.
  name: Salesforce
- description: Pre-built connectors for SAP ERP, S/4HANA, and SAP BW data integration.
  name: SAP
- description: Optimized connectors for loading, transforming, and managing data in Snowflake.
  name: Snowflake
- description: Native connectors for S3, Redshift, DynamoDB, and other AWS data services.
  name: Amazon Web Services
- description: Connectors for Azure SQL, Blob Storage, Synapse Analytics, and other Azure services.
  name: Microsoft Azure
- description: Connectors for BigQuery, Cloud Storage, and other GCP data services.
  name: Google Cloud Platform
- description: Pre-built connectors for Workday HCM and financial data integration.
  name: Workday
- description: Connectors for ServiceNow ITSM and platform data integration.
  name: ServiceNow
json_schemas:
- name: ActivityLogEntry
  property_count: 20
  slug: informatica-activitylogentry
- name: Informatica IICS Connection
  property_count: 22
  slug: informatica-connection
- name: ConnectionCreateRequest
  property_count: 15
  slug: informatica-connectioncreaterequest
- name: ConnectionUpdateRequest
  property_count: 13
  slug: informatica-connectionupdaterequest
- name: ErrorResponse
  property_count: 5
  slug: informatica-errorresponse
- name: JobStartRequest
  property_count: 6
  slug: informatica-jobstartrequest
- name: JobStartResponse
  property_count: 3
  slug: informatica-jobstartresponse
- name: JobStopRequest
  property_count: 5
  slug: informatica-jobstoprequest
- name: LoginRequest
  property_count: 3
  slug: informatica-loginrequest
- name: LoginResponse
  property_count: 16
  slug: informatica-loginresponse
- name: Mapping
  property_count: 23
  slug: informatica-mapping
- name: MappingInOutParameter
  property_count: 10
  slug: informatica-mappinginoutparameter
- name: MappingParameter
  property_count: 6
  slug: informatica-mappingparameter
- name: MappingTask
  property_count: 19
  slug: informatica-mappingtask
- name: MappingTaskCreateRequest
  property_count: 11
  slug: informatica-mappingtaskcreaterequest
- name: MappingTaskUpdateRequest
  property_count: 10
  slug: informatica-mappingtaskupdaterequest
- name: ActivityLogEntry
  property_count: 20
  slug: informatica-platform-rest-activity-log-entry
- name: ConnectionCreateRequest
  property_count: 15
  slug: informatica-platform-rest-connection-create-request
- name: Connection
  property_count: 22
  slug: informatica-platform-rest-connection
- name: ConnectionUpdateRequest
  property_count: 13
  slug: informatica-platform-rest-connection-update-request
- name: ErrorResponse
  property_count: 5
  slug: informatica-platform-rest-error-response
- name: JobStartRequest
  property_count: 6
  slug: informatica-platform-rest-job-start-request
- name: JobStartResponse
  property_count: 3
  slug: informatica-platform-rest-job-start-response
- name: JobStopRequest
  property_count: 5
  slug: informatica-platform-rest-job-stop-request
- name: LoginRequest
  property_count: 3
  slug: informatica-platform-rest-login-request
- name: LoginResponse
  property_count: 16
  slug: informatica-platform-rest-login-response
- name: MappingInOutParameter
  property_count: 10
  slug: informatica-platform-rest-mapping-in-out-parameter
- name: MappingParameter
  property_count: 6
  slug: informatica-platform-rest-mapping-parameter
- name: Mapping
  property_count: 23
  slug: informatica-platform-rest-mapping
- name: MappingTaskCreateRequest
  property_count: 11
  slug: informatica-platform-rest-mapping-task-create-request
- name: MappingTask
  property_count: 19
  slug: informatica-platform-rest-mapping-task
- name: MappingTaskUpdateRequest
  property_count: 10
  slug: informatica-platform-rest-mapping-task-update-request
- name: ScheduleCreateRequest
  property_count: 8
  slug: informatica-platform-rest-schedule-create-request
- name: Schedule
  property_count: 18
  slug: informatica-platform-rest-schedule
- name: Schedule
  property_count: 18
  slug: informatica-schedule
- name: ScheduleCreateRequest
  property_count: 8
  slug: informatica-schedulecreaterequest
json_structures:
- name: Informatica Platform Rest Activity Log Entry Structure
  property_count: 20
  slug: informatica-platform-rest-activity-log-entry-structure
- name: Informatica Platform Rest Connection Create Request Structure
  property_count: 15
  slug: informatica-platform-rest-connection-create-request-structure
- name: Informatica Platform Rest Connection Structure
  property_count: 22
  slug: informatica-platform-rest-connection-structure
- name: Informatica Platform Rest Connection Update Request Structure
  property_count: 13
  slug: informatica-platform-rest-connection-update-request-structure
- name: Informatica Platform Rest Error Response Structure
  property_count: 5
  slug: informatica-platform-rest-error-response-structure
- name: Informatica Platform Rest Job Start Request Structure
  property_count: 6
  slug: informatica-platform-rest-job-start-request-structure
- name: Informatica Platform Rest Job Start Response Structure
  property_count: 3
  slug: informatica-platform-rest-job-start-response-structure
- name: Informatica Platform Rest Job Stop Request Structure
  property_count: 5
  slug: informatica-platform-rest-job-stop-request-structure
- name: Informatica Platform Rest Login Request Structure
  property_count: 3
  slug: informatica-platform-rest-login-request-structure
- name: Informatica Platform Rest Login Response Structure
  property_count: 16
  slug: informatica-platform-rest-login-response-structure
- name: Informatica Platform Rest Mapping In Out Parameter Structure
  property_count: 10
  slug: informatica-platform-rest-mapping-in-out-parameter-structure
- name: Informatica Platform Rest Mapping Parameter Structure
  property_count: 6
  slug: informatica-platform-rest-mapping-parameter-structure
- name: Informatica Platform Rest Mapping Structure
  property_count: 23
  slug: informatica-platform-rest-mapping-structure
- name: Informatica Platform Rest Mapping Task Create Request Structure
  property_count: 11
  slug: informatica-platform-rest-mapping-task-create-request-structure
- name: Informatica Platform Rest Mapping Task Structure
  property_count: 19
  slug: informatica-platform-rest-mapping-task-structure
- name: Informatica Platform Rest Mapping Task Update Request Structure
  property_count: 10
  slug: informatica-platform-rest-mapping-task-update-request-structure
- name: Informatica Platform Rest Schedule Create Request Structure
  property_count: 8
  slug: informatica-platform-rest-schedule-create-request-structure
- name: Informatica Platform Rest Schedule Structure
  property_count: 18
  slug: informatica-platform-rest-schedule-structure
- name: Informatica Structure
  property_count: 0
  slug: informatica-structure
jsonld:
- class_count: 0
  name: Informatica Context
  property_count: 7
  slug: informatica-context
- class_count: 0
  name: Informatica Platform Rest Context
  property_count: 0
  slug: informatica-platform-rest-context
layout: provider
modified: '2026-05-19'
name: Informatica
nav: Providers
network: true
overview: 'Informatica publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Connections API, Jobs API, and 3 more. Tagged areas include Address Verification, B2B Gateway, Cloud Services, Data Governance, and Data Integration.


  The Informatica catalog on APIs.io includes 2 JSON-LD contexts and 2 Spectral governance rulesets.


  Informatica''s developer surface includes authentication, developer portal, documentation, support, engineering blog, and 9 more developer resources.'
plans:
- name: Informatica Plans Pricing
  plan_count: 3
  slug: informatica-plans-pricing
random_paper: 25
rate_limits:
- limit_count: 2
  name: Informatica Rate Limits
  slug: informatica-rate-limits
rules:
- name: Informatica API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: informatica-jsonschema-spectral-rules
- name: Informatica API Rules
  rule_count: 16
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 7
  slug: informatica-spectral-rules
score:
  band: developing
  composite: 54.0
  delta: 0.0
  facets:
    commercial_clarity: 52.6
    contract_quality: 79.3
    developer_ergonomics: 34.8
    discoverability: 50.0
    governance: 68.8
    operational_transparency: 26.3
  previous_composite: 54.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/informatica/refs/heads/main/screenshots/informatica-2026-06-20T183340.png
security:
- kind: authentication
  name: Informatica Authentication
  slug: informatica-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Informatica Domain Security
  slug: informatica-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: informatica
tags:
- Address Verification
- B2B Gateway
- Cloud Services
- Data Governance
- Data Integration
- Data Profiling
- Data Quality
- Enterprise Software
- ETL
- IDMC
- IICS
- Master Data Management
- Reference Data Management
use_cases:
- description: Extract data from multiple sources and load into cloud data warehouses like Snowflake, Redshift, or BigQuery.
  name: Cloud Data Warehouse Loading
- description: Synchronize data across CRM, ERP, and marketing platforms in real time using change data capture.
  name: Real-Time Data Synchronization
- description: Migrate data between legacy systems and modern cloud platforms with automated mapping and transformation.
  name: Data Migration
- description: Ensure data quality and governance standards to meet GDPR, CCPA, and industry-specific regulations.
  name: Regulatory Compliance
- description: Create unified customer profiles by integrating and matching data from multiple source systems.
  name: Customer 360
website: https://developer.informatica.com/
---
