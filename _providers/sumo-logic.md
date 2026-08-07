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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.8
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 228
  human_in_the_loop: 9
  name: Sumo Logic Agentic Access
  operation_count: 419
  slug: sumo-logic-agentic-access
  summary_line: 419 operations · 228 acting · 9 human-in-the-loop
api_count: 54
apis:
- description: Access Key management API. Access Keys allow you to securely register new Collectors and access Sumo Logic APIs. For more information, see [Access Keys](https://help.sumologic.com/?cid=6690).
  name: Sumo Logic accessKeyManagement API
  slug: sumo-logic-accesskeymanagement-api
- description: Account Management API. Manage the custom subdomain for the URL used to access your Sumo Logic account. For more information, see [Manage Organization](https://help.sumologic.com/docs/manage/manage-su
  name: Sumo Logic accountManagement API
  slug: sumo-logic-accountmanagement-api
- description: App installation API. View and install Sumo Logic Applications that deliver out-of-the-box dashboards, saved searches, and field extraction for popular data sources. For more information, see [Sumo Lo
  name: Sumo Logic appManagement API
  slug: sumo-logic-appmanagement-api
- description: App installation API (V2). View and install Sumo Logic Applications that deliver out-of-the-box dashboards, saved searches, and field extraction for popular data sources. For more information, see [Su
  name: Sumo Logic appManagementV2 API
  slug: sumo-logic-appmanagementv2-api
- description: Archive Ingestion Management API. Archive Ingestion allows you to ingest data from Archive destinations. You can use this API to ingest data from your Archive with an existing AWS S3 Archive Source. Y
  name: Sumo Logic archiveManagement API
  slug: sumo-logic-archivemanagement-api
- description: Budget Management API.
  name: Sumo Logic budgetManagement API
  slug: sumo-logic-budgetmanagement-api
- description: Connection management API. Set up connections to send alerts to other tools. For more information, see [Connections and Integrations](https://help.sumologic.com/?cid=1044).
  name: Sumo Logic connectionManagement API
  slug: sumo-logic-connectionmanagement-api
- description: Content management API. You can export, import, delete and copy content in your organization’s Library. For more information, see [Library](https://help.sumologic.com/?cid=5173). You can perform the r
  name: Sumo Logic contentManagement API
  slug: sumo-logic-contentmanagement-api
- description: 'Content permissions API. You can share your folders, searches, and dashboards with specific users or roles. For more information, see [Share Content](https://help.sumologic.com/?cid=8675309). You can '
  name: Sumo Logic contentPermissions API
  slug: sumo-logic-contentpermissions-api
- description: Dashboard (New) management API. Dashboard (New) allows you to analyze metric and log data on the same dashboard, in a seamless view. This gives you control over the visual display of metric and log da
  name: Sumo Logic dashboardManagement API
  slug: sumo-logic-dashboardmanagement-api
- description: Data Deletion Rules (Beta) API. Data Deletion Rules allow creating and managing requests to delete log messages satisfying parameters ( query, timerange, etc...). For more information, see [Deletion R
  name: Sumo Logic dataDeletionRules API
  slug: sumo-logic-datadeletionrules-api
- description: Data Masking Rules management API. Data Masking Rules allow you to define regex patterns that mask sensitive data in log messages at query time.
  name: Sumo Logic dataMaskingManagement API
  slug: sumo-logic-datamaskingmanagement-api
- description: Dynamic Parsing management API. Dynamic Parsing allows automatic field extraction from your log messages when you run a search. This allows you to view fields from logs without having to manually spec
  name: Sumo Logic dynamicParsingRuleManagement API
  slug: sumo-logic-dynamicparsingrulemanagement-api
- description: Event Analytics (Beta) API. APIs for interacting with events in Sumo Logic.
  name: Sumo Logic eventAnalytics API
  slug: sumo-logic-eventanalytics-api
- description: 'Field Extraction Rule management API. Field Extraction Rules allow you to parse fields from your log messages at the time the messages are ingested eliminating the need to parse fields in your query. '
  name: Sumo Logic extractionRuleManagement API
  slug: sumo-logic-extractionrulemanagement-api
- description: Field management API. Fields allow you to reference log data based on meaningful associations. They act as metadata tags that are assigned to your logs so you can search with them. Each field contains
  name: Sumo Logic fieldManagementV1 API
  slug: sumo-logic-fieldmanagementv1-api
- description: Folder management API. You can add folders and subfolders to the Library in order to organize your content for easy access or to share content. For more information, see [Add Folders to the Library](h
  name: Sumo Logic folderManagement API
  slug: sumo-logic-foldermanagement-api
- description: 'Health Events management API. Health Events allow you to keep track of the health of your Collectors and Sources. You can use them to find and investigate common errors and warnings that are known to '
  name: Sumo Logic healthEvents API
  slug: sumo-logic-healthevents-api
- description: Ingest Budget management API V2. Ingest Budgets V2 provide you the ability to create and assign budgets to your log data by Fields instead of using a Field Value. For more information, see [Metadata I
  name: Sumo Logic ingestBudgetManagementV2 API
  slug: sumo-logic-ingestbudgetmanagementv2-api
- description: Logs Data Forwarding management API. Logs Data Forwarding allows you to forward log data from a Partition or Scheduled View to an S3 bucket. For more information, see [Forwarding Data to S3](https://h
  name: Sumo Logic logsDataForwardingManagement API
  slug: sumo-logic-logsdataforwardingmanagement-api
- description: Log Search Estimated Usage API. Gets the estimated volume of data that would be scanned for a given log search in the Infrequent data tier, over a particular time range. In the Infrequent Data Tier, y
  name: Sumo Logic logSearchesEstimatedUsage API
  slug: sumo-logic-logsearchesestimatedusage-api
- description: Log Searches Management API. Whether you are running ad hoc searches during a forensic investigation or running standard searches for health checks, you can save any search to run again later. When yo
  name: Sumo Logic logSearchesManagement API
  slug: sumo-logic-logsearchesmanagement-api
- description: 'Lookup Table management API. A Lookup Table is a table of data hosted on Sumo Logic that you can use to enrich the log and event data received by Sumo Logic. You must create a table schema before you '
  name: Sumo Logic lookupManagement API
  slug: sumo-logic-lookupmanagement-api
- description: Macro Management APIs. Macros allow you to reference a predefined set of query language syntax across multiple queries. This enables reuse of commonly used logic, improves consistency, and reduces dup
  name: Sumo Logic macroManagement API
  slug: sumo-logic-macromanagement-api
- description: Metrics Query API. The Metrics Query API allows you to execute queries on various metrics and retrieve multiple time-series (data-points) over time range(s). For more information, see [Metrics - Class
  name: Sumo Logic metricsQuery API
  slug: sumo-logic-metricsquery-api
- description: Metrics Search management API. Save metrics searches in the content library and organize them in a folder hierarchy. Share useful queries with users in your organization. For more information, see [Sh
  name: Sumo Logic metricsSearchesManagement API
  slug: sumo-logic-metricssearchesmanagement-api
- description: New Metrics Searches Management API. Save metrics searches in the content library and organize them in a folder hierarchy. Allows you to list metrics searches under your personal folder.
  name: Sumo Logic metricsSearchesManagementV2 API
  slug: sumo-logic-metricssearchesmanagementv2-api
- description: Monitor Management API. Monitors continuously query your data to monitor and send notifications when specific events occur. For more information see [Monitors](https://help.sumologic.com/?cid=10020).
  name: Sumo Logic monitorsLibraryManagement API
  slug: sumo-logic-monitorslibrarymanagement-api
- description: Muting Schedules Management API. Muting Schedule allows you to pause alert notifications from monitors. When a muting schedule is active on a monitor, the monitor will still generate alerts, but no no
  name: Sumo Logic mutingSchedulesLibraryManagement API
  slug: sumo-logic-mutingscheduleslibrarymanagement-api
- description: '** Only available to Beta customers. During Beta endpoints are subject to backwards incompatible changes. ** APIs to manage OAuth Clients'
  name: Sumo Logic oauthManagement API
  slug: sumo-logic-oauthmanagement-api
- description: Organizations Management API.
  name: Sumo Logic orgsManagement API
  slug: sumo-logic-orgsmanagement-api
- description: OT Collector Management API External.
  name: Sumo Logic otCollectorManagementExternal API
  slug: sumo-logic-otcollectormanagementexternal-api
- description: Parsers Library Management API Customize the Parsers via this API. The Parsers Library contains the Parsers used in the "_parser" field for collector, FER or query. For more information on customizing
  name: Sumo Logic parsersLibraryManagement API
  slug: sumo-logic-parserslibrarymanagement-api
- description: Partition management API. Creating a Partition allows you to improve search performance by searching over a smaller number of messages. For more information, see [Manage Partitions](https://help.sumol
  name: Sumo Logic partitionManagement API
  slug: sumo-logic-partitionmanagement-api
- description: Password Policy Management API The password policy controls how user passwords are managed. The "Manage Password Policy" role capability is required to update the password policy. For more information
  name: Sumo Logic passwordPolicy API
  slug: sumo-logic-passwordpolicy-api
- description: Policies management API. Policies control the security and share settings of your organization. For more information, see [Security](https://help.sumologic.com/?cid=4041).
  name: Sumo Logic policiesManagement API
  slug: sumo-logic-policiesmanagement-api
- description: Role management API. Roles determine the functions that users are able to perform in Sumo Logic. To manage roles, you must have an administrator role or your role must have been assigned the manage us
  name: Sumo Logic roleManagement API
  slug: sumo-logic-rolemanagement-api
- description: 'Role management API (V2). Roles determine the functions that users are able to perform in Sumo Logic. It also allows to configure access on partitions. To manage roles, you must have an administrator '
  name: Sumo Logic roleManagementV2 API
  slug: sumo-logic-rolemanagementv2-api
- description: SAML configuration management API Organizations with Enterprise accounts can provision Security Assertion Markup Language (SAML) 2.0 to enable Single Sign-On (SSO) for user access to Sumo Logic. For m
  name: Sumo Logic samlConfigurationManagement API
  slug: sumo-logic-samlconfigurationmanagement-api
- description: Scheduled View management API. Scheduled Views speed the search process for small and historical subsets of your data by functioning as a pre-aggregated index. For more information, see [Manage Schedu
  name: Sumo Logic scheduledViewManagement API
  slug: sumo-logic-scheduledviewmanagement-api
- description: Schema Base Management APIs.
  name: Sumo Logic schemaBaseManagement API
  slug: sumo-logic-schemabasemanagement-api
- description: APIs to manage scim based users.
  name: Sumo Logic scimUserManagement API
  slug: sumo-logic-scimusermanagement-api
- description: APIs to manage service accounts
  name: Sumo Logic serviceAccountManagement API
  slug: sumo-logic-serviceaccountmanagement-api
- description: Service Allowlist management API Service Allowlist Settings allow you to explicitly grant access to specific IP addresses and/or CIDR notations for logins, APIs, and dashboard access. For more informa
  name: Sumo Logic serviceAllowlistManagement API
  slug: sumo-logic-serviceallowlistmanagement-api
- description: Service Map API The Service Map API allows you to fetch a graph representation of the Services Map, which is a high-level view of your application environment, automatically derived from tracing data.
  name: Sumo Logic serviceMap API
  slug: sumo-logic-servicemap-api
- description: SLO Management API. SLOs are used to monitor and alert on KPIs for your most important services or user experience.
  name: Sumo Logic slosLibraryManagement API
  slug: sumo-logic-sloslibrarymanagement-api
- description: Source Template Management APIs.
  name: Sumo Logic sourceTemplateManagementExternal API
  slug: sumo-logic-sourcetemplatemanagementexternal-api
- description: Span Analytics API The Span Analytics API allows you to browse spans collected in the system. You can execute queries to find individual spans matching provided search criteria as well as run aggregat
  name: Sumo Logic spanAnalytics API
  slug: sumo-logic-spananalytics-api
- description: 'Threat Intel Datastore Management API The Threat Intel Datastore Management API allows you to: * Get information about the threat indicator datastore and sources. * Delete the threat indicator databas'
  name: Sumo Logic threatIntelIngest API
  slug: sumo-logic-threatintelingest-api
- description: 'Threat Intel Ingestion API The Threat Intel Ingestion API allows you to: * Upload threat intel indicators in STIX 2.x or Sumo normalized format. * Delete indicators by ID or source. For more informati'
  name: Sumo Logic threatIntelIngestProducer API
  slug: sumo-logic-threatintelingestproducer-api
- description: Tokens management API. Tokens are associated with your organization to authorize specific operations. Currently, we support collector registration tokens, which can be used to register Installed Colle
  name: Sumo Logic tokensLibraryManagement API
  slug: sumo-logic-tokenslibrarymanagement-api
- description: Traces API The Traces API allows you to browse traces collected in the system. You can execute queries to find traces matching provided search criteria as well as gather detailed information about ind
  name: Sumo Logic traces API
  slug: sumo-logic-traces-api
- description: Transformation Rule management API. Metrics Transformation Rules allow you control how long raw metrics are retained. You can also aggregate metrics at collection time and specify a separate retention
  name: Sumo Logic transformationRuleManagement API
  slug: sumo-logic-transformationrulemanagement-api
- description: User management API. To manage users, you must have the administrator role or your role must have been assigned the manage users and roles capability. For more information, see [Manage Users](https://
  name: Sumo Logic userManagement API
  slug: sumo-logic-usermanagement-api
artifact_total: 71
collections:
- collection_type: open
  name: Sumo Logic API
  slug: open-sumo-logic
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/sumo-logic-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/sumo-logic-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sumo-logic-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/sumo-logic-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/sumologic
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/sumo-logic
- group: start
  title: ''
  type: Portal
  url: https://developer.sumologic.com/
- group: docs
  title: ''
  type: Documentation
  url: https://help.sumologic.com/docs/api/
- group: docs
  title: ''
  type: Reference
  url: https://api.sumologic.com/docs/
- group: company
  title: ''
  type: Website
  url: https://www.sumologic.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://help.sumologic.com/docs/api/about-apis/getting-started/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.sumologic.com
- group: company
  title: ''
  type: Blog
  url: https://www.sumologic.com/blog/
created: '2025-01-08'
description: Sumo Logic is a cloud-native, machine data analytics platform delivering real-time, continuous intelligence for operations, security, and business insights. It provides a comprehensive REST API with 289 endpoints spanning log analytics, dashboards, monitors, roles, users, metrics, traces, and more.
examples:
- key_count: 4
  name: Sumo Logic Create Monitor Example
  slug: sumo-logic-create-monitor-example
- key_count: 4
  name: Sumo Logic List Users Example
  slug: sumo-logic-list-users-example
finops:
- name: Sumo Logic Finops
  service_category: API
  slug: sumo-logic-finops
graphqls:
- description: This directory contains a conceptual GraphQL schema for the Sumo Logic cloud logging and monitoring platform, derived from the [Sumo Logic REST API v1](https://api.sumologic.com/docs/).
  name: Sumo Logic GraphQL Schema
  slug: sumo-logic-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sumo-logic.png
json_schemas:
- name: Sumo Logic Monitor
  property_count: 13
  slug: sumo-logic-monitor
- name: Sumo Logic User
  property_count: 13
  slug: sumo-logic-user
json_structures:
- name: Sumo Logic User Structure
  property_count: 0
  slug: sumo-logic-user-structure
jsonld:
- class_count: 18
  name: Sumo Logic Context
  property_count: 8
  slug: sumo-logic-context
layout: provider
modified: '2026-05-19'
name: Sumo Logic
nav: Providers
network: true
overview: 'Sumo Logic publishes 54 APIs on the [APIs.io](https://apis.io/) network, including accessKeyManagement API, accountManagement API, appManagement API, and 51 more. Tagged areas include Logging, Observability, Security, Monitoring, and Analytics.


  The Sumo Logic catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Sumo Logic''s developer surface includes authentication, developer portal, documentation, getting-started guide, engineering blog, and 8 more developer resources.'
plans:
- name: Sumo Logic Plans Pricing
  plan_count: 3
  slug: sumo-logic-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 5
  name: Sumo Logic Rate Limits
  slug: sumo-logic-rate-limits
rules:
- name: Sumo Logic API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: sumo-logic-jsonschema-spectral-rules
- name: Sumo Logic API Rules
  rule_count: 9
  severity_counts:
    error: 2
    hint: 0
    info: 2
    warn: 5
  slug: sumo-logic-rules
score:
  band: strong
  composite: 56.2
  delta: 0.0
  facets:
    commercial_clarity: 47.4
    contract_quality: 65.8
    developer_ergonomics: 47.8
    discoverability: 68.5
    governance: 58.3
    operational_transparency: 52.6
  previous_composite: 56.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 54
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sumo-logic/refs/heads/main/screenshots/sumo-logic-2026-06-20T194649.png
security:
- kind: authentication
  name: Sumo Logic Authentication
  slug: sumo-logic-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Sumo Logic Domain Security
  slug: sumo-logic-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Sumo Logic Trust Center
  slug: sumo-logic-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, HIPAA, FedRAMP, GDPR, CSA STAR
slug: sumo-logic
tags:
- Logging
- Observability
- Security
- Monitoring
- Analytics
- DevOps
- SIEM
website: https://www.sumologic.com/
---
