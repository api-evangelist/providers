---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: derived
    idempotency: false
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: verified
    rate_limit_signal: derived
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 45.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 226
  human_in_the_loop: 9
  name: Sumo Logic Agentic Access
  operation_count: 431
  slug: sumo-logic-agentic-access
  summary_line: 431 operations · 226 acting · 9 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.sumologic.com/api
  baseurl_source: declared
  description: Access Key management API. Access Keys allow you to securely register new Collectors and access Sumo Logic APIs. For more information, see [Access Keys](https://help.sumologic.com/?cid=6690).
  name: Sumo Logic Access Key Management API
  slug: sumo-logic-accesskeymanagement-api
- baseURL: https://api.sumologic.com/api
  baseurl_source: declared
  description: App installation API (V2). View and install Sumo Logic Applications that deliver out-of-the-box dashboards, saved searches, and field extraction for popular data sources. For more information, see [Su
  name: Sumo Logic App Management V2 API
  slug: sumo-logic-appmanagementv2-api
- baseURL: https://api.sumologic.com/api
  baseurl_source: declared
  description: Archive Ingestion Management API. Archive Ingestion allows you to ingest data from Archive destinations. You can use this API to ingest data from your Archive with an existing AWS S3 Archive Source. Y
  name: Sumo Logic Archive Management API
  slug: sumo-logic-archivemanagement-api
- baseURL: https://api.sumologic.com/api
  baseurl_source: declared
  description: Dashboard (New) management API. Dashboard (New) allows you to analyze metric and log data on the same dashboard, in a seamless view. This gives you control over the visual display of metric and log da
  name: Sumo Logic Dashboard Management API
  slug: sumo-logic-dashboardmanagement-api
- baseURL: https://api.sumologic.com/api
  baseurl_source: declared
  description: Data Deletion Rules (Beta) API. Data Deletion Rules allow creating and managing requests to delete log messages satisfying parameters ( query, timerange, etc...). For more information, see [Deletion R
  name: Sumo Logic Data Deletion Rules API
  slug: sumo-logic-datadeletionrules-api
- baseURL: https://api.sumologic.com/api
  baseurl_source: declared
  description: Data Masking Rules management API. Data Masking Rules allow you to define regex patterns that mask sensitive data in log messages at query time.
  name: Sumo Logic Data Masking Management API
  slug: sumo-logic-datamaskingmanagement-api
- baseURL: https://api.sumologic.com/api
  baseurl_source: declared
  description: Dynamic Parsing management API. Dynamic Parsing allows automatic field extraction from your log messages when you run a search. This allows you to view fields from logs without having to manually spec
  name: Sumo Logic Dynamic Parsing Rule Management API
  slug: sumo-logic-dynamicparsingrulemanagement-api
- baseURL: https://api.sumologic.com/api
  baseurl_source: declared
  description: 'Field Extraction Rule management API. Field Extraction Rules allow you to parse fields from your log messages at the time the messages are ingested eliminating the need to parse fields in your query. '
  name: Sumo Logic Extraction Rule Management API
  slug: sumo-logic-extractionrulemanagement-api
- baseURL: https://api.sumologic.com/api
  baseurl_source: declared
  description: Field management API. Fields allow you to reference log data based on meaningful associations. They act as metadata tags that are assigned to your logs so you can search with them. Each field contains
  name: Sumo Logic Field Management V1 API
  slug: sumo-logic-fieldmanagementv1-api
- baseURL: https://api.sumologic.com/api
  baseurl_source: declared
  description: Folder management API. You can add folders and subfolders to the Library in order to organize your content for easy access or to share content. For more information, see [Add Folders to the Library](h
  name: Sumo Logic Folder Management API
  slug: sumo-logic-foldermanagement-api
- baseURL: https://api.sumologic.com/api
  baseurl_source: declared
  description: 'Health Events management API. Health Events allow you to keep track of the health of your Collectors and Sources. You can use them to find and investigate common errors and warnings that are known to '
  name: Sumo Logic Health Events API
  slug: sumo-logic-healthevents-api
- baseURL: https://api.sumologic.com/api
  baseurl_source: declared
  description: Ingest Budget management API V2. Ingest Budgets V2 provide you the ability to create and assign budgets to your log data by Fields instead of using a Field Value. For more information, see [Metadata I
  name: Sumo Logic Ingest Budget Management V2 API
  slug: sumo-logic-ingestbudgetmanagementv2-api
- baseURL: https://api.sumologic.com/api
  baseurl_source: declared
  description: Logs Data Forwarding management API. Logs Data Forwarding allows you to forward log data from a Partition or Scheduled View to an S3 bucket. For more information, see [Forwarding Data to S3](https://h
  name: Sumo Logic Logs Data Forwarding Management API
  slug: sumo-logic-logsdataforwardingmanagement-api
- baseURL: https://api.sumologic.com/api
  baseurl_source: declared
  description: Log Search Estimated Usage API. Gets the estimated volume of data that would be scanned for a given log search in the Infrequent data tier, over a particular time range. In the Infrequent Data Tier, y
  name: Sumo Logic Log Searches Estimated Usage API
  slug: sumo-logic-logsearchesestimatedusage-api
- baseURL: https://api.sumologic.com/api
  baseurl_source: declared
  description: Log Searches Management API. Whether you are running ad hoc searches during a forensic investigation or running standard searches for health checks, you can save any search to run again later. When yo
  name: Sumo Logic Log Searches Management API
  slug: sumo-logic-logsearchesmanagement-api
- baseURL: https://api.sumologic.com/api
  baseurl_source: declared
  description: 'Lookup Table management API. A Lookup Table is a table of data hosted on Sumo Logic that you can use to enrich the log and event data received by Sumo Logic. You must create a table schema before you '
  name: Sumo Logic Lookup Management API
  slug: sumo-logic-lookupmanagement-api
- baseURL: https://api.sumologic.com/api
  baseurl_source: declared
  description: Macro Management APIs. Macros allow you to reference a predefined set of query language syntax across multiple queries. This enables reuse of commonly used logic, improves consistency, and reduces dup
  name: Sumo Logic Macro Management API
  slug: sumo-logic-macromanagement-api
- baseURL: https://api.sumologic.com/api
  baseurl_source: declared
  description: Metrics Query API. The Metrics Query API allows you to execute queries on various metrics and retrieve multiple time-series (data-points) over time range(s). For more information, see [Metrics - Class
  name: Sumo Logic Metrics Query API
  slug: sumo-logic-metricsquery-api
- baseURL: https://api.sumologic.com/api
  baseurl_source: declared
  description: Metrics Search management API. Save metrics searches in the content library and organize them in a folder hierarchy. Share useful queries with users in your organization. For more information, see [Sh
  name: Sumo Logic Metrics Searches Management API
  slug: sumo-logic-metricssearchesmanagement-api
- baseURL: https://api.sumologic.com/api
  baseurl_source: declared
  description: New Metrics Searches Management API. Save metrics searches in the content library and organize them in a folder hierarchy. Allows you to list metrics searches under your personal folder.
  name: Sumo Logic Metrics Searches Management V2 API
  slug: sumo-logic-metricssearchesmanagementv2-api
- baseURL: https://api.sumologic.com/api
  baseurl_source: declared
  description: Monitor Management API. Monitors continuously query your data to monitor and send notifications when specific events occur. For more information see [Monitors](https://help.sumologic.com/?cid=10020).
  name: Sumo Logic Monitors Library Management API
  slug: sumo-logic-monitorslibrarymanagement-api
- baseURL: https://api.sumologic.com/api
  baseurl_source: declared
  description: Muting Schedules Management API. Muting Schedule allows you to pause alert notifications from monitors. When a muting schedule is active on a monitor, the monitor will still generate alerts, but no no
  name: Sumo Logic Muting Schedules Library Management API
  slug: sumo-logic-mutingscheduleslibrarymanagement-api
- baseURL: https://api.sumologic.com/api
  baseurl_source: declared
  description: '** Only available to Beta customers. During Beta endpoints are subject to backwards incompatible changes. ** APIs to manage OAuth Clients'
  name: Sumo Logic OAUTH Management API
  slug: sumo-logic-oauthmanagement-api
- baseURL: https://api.sumologic.com/api
  baseurl_source: declared
  description: Organizations Management API.
  name: Sumo Logic Orgs Management API
  slug: sumo-logic-orgsmanagement-api
- baseURL: https://api.sumologic.com/api
  baseurl_source: declared
  description: OT Collector Management API External.
  name: Sumo Logic otCollectorManagementExternal API
  slug: sumo-logic-otcollectormanagementexternal-api
- baseURL: https://api.sumologic.com/api
  baseurl_source: declared
  description: Parsers Library Management API Customize the Parsers via this API. The Parsers Library contains the Parsers used in the "_parser" field for collector, FER or query. For more information on customizing
  name: Sumo Logic Parsers Library Management API
  slug: sumo-logic-parserslibrarymanagement-api
- baseURL: https://api.sumologic.com/api
  baseurl_source: declared
  description: Partition management API. Creating a Partition allows you to improve search performance by searching over a smaller number of messages. For more information, see [Manage Partitions](https://help.sumol
  name: Sumo Logic Partition Management API
  slug: sumo-logic-partitionmanagement-api
- baseURL: https://api.sumologic.com/api
  baseurl_source: declared
  description: Policies management API. Policies control the security and share settings of your organization. For more information, see [Security](https://help.sumologic.com/?cid=4041).
  name: Sumo Logic Policies Management API
  slug: sumo-logic-policiesmanagement-api
- baseURL: https://api.sumologic.com/api
  baseurl_source: declared
  description: 'Role management API (V2). Roles determine the functions that users are able to perform in Sumo Logic. It also allows to configure access on partitions. To manage roles, you must have an administrator '
  name: Sumo Logic Role Management V2 API
  slug: sumo-logic-rolemanagementv2-api
- baseURL: https://api.sumologic.com/api
  baseurl_source: declared
  description: SAML configuration management API Organizations with Enterprise accounts can provision Security Assertion Markup Language (SAML) 2.0 to enable Single Sign-On (SSO) for user access to Sumo Logic. For m
  name: Sumo Logic Saml Configuration Management API
  slug: sumo-logic-samlconfigurationmanagement-api
- baseURL: https://api.sumologic.com/api
  baseurl_source: declared
  description: Scheduled View management API. Scheduled Views speed the search process for small and historical subsets of your data by functioning as a pre-aggregated index. For more information, see [Manage Schedu
  name: Sumo Logic Scheduled View Management API
  slug: sumo-logic-scheduledviewmanagement-api
- baseURL: https://api.sumologic.com/api
  baseurl_source: declared
  description: Schema Base Management APIs.
  name: Sumo Logic Schema Base Management API
  slug: sumo-logic-schemabasemanagement-api
- baseURL: https://api.sumologic.com/api
  baseurl_source: declared
  description: APIs to manage service accounts
  name: Sumo Logic Service Account Management API
  slug: sumo-logic-serviceaccountmanagement-api
- baseURL: https://api.sumologic.com/api
  baseurl_source: declared
  description: Service Allowlist management API Service Allowlist Settings allow you to explicitly grant access to specific IP addresses and/or CIDR notations for logins, APIs, and dashboard access. For more informa
  name: Sumo Logic Service Allowlist Management API
  slug: sumo-logic-serviceallowlistmanagement-api
- baseURL: https://api.sumologic.com/api
  baseurl_source: declared
  description: Service Map API The Service Map API allows you to fetch a graph representation of the Services Map, which is a high-level view of your application environment, automatically derived from tracing data.
  name: Sumo Logic Service Map API
  slug: sumo-logic-servicemap-api
- baseURL: https://api.sumologic.com/api
  baseurl_source: declared
  description: SLO Management API. SLOs are used to monitor and alert on KPIs for your most important services or user experience.
  name: Sumo Logic Slos Library Management API
  slug: sumo-logic-sloslibrarymanagement-api
- baseURL: https://api.sumologic.com/api
  baseurl_source: declared
  description: Source Template Management APIs.
  name: Sumo Logic Source Template Management External API
  slug: sumo-logic-sourcetemplatemanagementexternal-api
- baseURL: https://api.sumologic.com/api
  baseurl_source: declared
  description: Span Analytics API The Span Analytics API allows you to browse spans collected in the system. You can execute queries to find individual spans matching provided search criteria as well as run aggregat
  name: Sumo Logic Span Analytics API
  slug: sumo-logic-spananalytics-api
- baseURL: https://api.sumologic.com/api
  baseurl_source: declared
  description: 'Threat Intel Datastore Management API The Threat Intel Datastore Management API allows you to: * Get information about the threat indicator datastore and sources. * Delete the threat indicator databas'
  name: Sumo Logic Threat Intel Ingest API
  slug: sumo-logic-threatintelingest-api
- baseURL: https://api.sumologic.com/api
  baseurl_source: declared
  description: 'Threat Intel Ingestion API The Threat Intel Ingestion API allows you to: * Upload threat intel indicators in STIX 2.x or Sumo normalized format. * Delete indicators by ID or source. For more informati'
  name: Sumo Logic Threat Intel Ingest Producer API
  slug: sumo-logic-threatintelingestproducer-api
- baseURL: https://api.sumologic.com/api
  baseurl_source: declared
  description: Tokens management API. Tokens are associated with your organization to authorize specific operations. Currently, we support collector registration tokens, which can be used to register Installed Colle
  name: Sumo Logic Tokens Library Management API
  slug: sumo-logic-tokenslibrarymanagement-api
- baseURL: https://api.sumologic.com/api
  baseurl_source: declared
  description: Traces API The Traces API allows you to browse traces collected in the system. You can execute queries to find traces matching provided search criteria as well as gather detailed information about ind
  name: Sumo Logic Traces API
  slug: sumo-logic-traces-api
- baseURL: https://api.sumologic.com/api
  baseurl_source: declared
  description: Transformation Rule management API. Metrics Transformation Rules allow you control how long raw metrics are retained. You can also aggregate metrics at collection time and specify a separate retention
  name: Sumo Logic Transformation Rule Management API
  slug: sumo-logic-transformationrulemanagement-api
- baseURL: https://api.sumologic.com/api
  baseurl_source: declared
  description: The Collectors API from Sumo Logic — 2 operation(s) for collectors.
  name: Sumo Logic Collectors API
  slug: sumo-logic-collectors-api
- baseURL: https://api.sumologic.com/api
  baseurl_source: declared
  description: The Content API from Sumo Logic — 2 operation(s) for content.
  name: Sumo Logic Content API
  slug: sumo-logic-content-api
- baseURL: https://api.sumologic.com/api
  baseurl_source: declared
  description: The Search Jobs API from Sumo Logic — 4 operation(s) for search jobs.
  name: Sumo Logic Search Jobs API
  slug: sumo-logic-search-jobs-api
- baseURL: https://api.sumologic.com/api
  baseurl_source: declared
  description: Account Management API. Manage the custom subdomain for the URL used to access your Sumo Logic account. For more information, see Manage Organization.
  name: Sumo Logic Account Management API
  slug: sumo-logic-account-management-api
- baseURL: https://api.sumologic.com/api
  baseurl_source: declared
  description: App installation API. View and install Sumo Logic Applications that deliver out-of-the-box dashboards, saved searches, and field extraction for popular data sources. For more information, see Sumo Log
  name: Sumo Logic App Management API
  slug: sumo-logic-app-management-api
- baseURL: https://api.sumologic.com/api
  baseurl_source: declared
  description: Budget Management API.
  name: Sumo Logic budget management API
  slug: sumo-logic-budget-management-api
- baseURL: https://api.sumologic.com/api
  baseurl_source: declared
  description: Connection management API. Set up connections to send alerts to other tools. For more information, see Connections and Integrations.
  name: Sumo Logic Connection Management API
  slug: sumo-logic-connection-management-api
- baseURL: https://api.sumologic.com/api
  baseurl_source: declared
  description: Content management API.
  name: Sumo Logic Content Management API
  slug: sumo-logic-content-management-api
- baseURL: https://api.sumologic.com/api
  baseurl_source: declared
  description: Content permissions API. You can share your folders, searches, and dashboards with specific users or roles. For more information, see Share Content. You can perform the request as a Content Administra
  name: Sumo Logic Content Permissions API
  slug: sumo-logic-content-permissions-api
- baseURL: https://api.sumologic.com/api
  baseurl_source: declared
  description: Event Analytics (Beta) API. APIs for interacting with events in Sumo Logic.
  name: Sumo Logic event analytics API
  slug: sumo-logic-event-analytics-api
- baseURL: https://api.sumologic.com/api
  baseurl_source: declared
  description: Password Policy Management API The password policy controls how user passwords are managed. The "Manage Password Policy" role capability is required to update the password policy. For more information
  name: Sumo Logic Password Policy API
  slug: sumo-logic-password-policy-api
- baseURL: https://api.sumologic.com/api
  baseurl_source: declared
  description: Role management API. Roles determine the functions that users are able to perform in Sumo Logic. To manage roles, you must have an administrator role or your role must have been assigned the manage us
  name: Sumo Logic Role Management API
  slug: sumo-logic-role-management-api
- baseURL: https://api.sumologic.com/api
  baseurl_source: declared
  description: APIs to manage scim based users.
  name: Sumo Logic SCIM User Management API
  slug: sumo-logic-scim-user-management-api
- baseURL: https://api.sumologic.com/api
  baseurl_source: declared
  description: User management API. To manage users, you must have the administrator role or your role must have been assigned the manage users and roles capability. For more information, see Manage Users.
  name: Sumo Logic User Management API
  slug: sumo-logic-user-management-api
artifact_total: 138
asyncapis:
- description: 'AsyncAPI description of Sumo Logic''s outbound webhook surfaces. Sumo Logic delivers alert and recovery notifications via HTTP POST to user-configured webhook connections. Each connection type targets '
  name: Sumo Logic Webhook Connections
  slug: sumo-logic-asyncapi
collections:
- collection_type: open
  name: Sumo Logic accessKeyManagement API
  slug: open-sumo-logic-accesskeymanagement-api
- collection_type: open
  name: Sumo Logic accessKeyManagement accountManagement API
  slug: open-sumo-logic-accountmanagement-api
- collection_type: open
  name: Sumo Logic accessKeyManagement appManagement API
  slug: open-sumo-logic-appmanagement-api
- collection_type: open
  name: Sumo Logic accessKeyManagement appManagementV2 API
  slug: open-sumo-logic-appmanagementv2-api
- collection_type: open
  name: Sumo Logic accessKeyManagement archiveManagement API
  slug: open-sumo-logic-archivemanagement-api
- collection_type: open
  name: Sumo Logic accessKeyManagement budgetManagement API
  slug: open-sumo-logic-budgetmanagement-api
- collection_type: open
  name: Sumo Logic REST Collectors API
  slug: open-sumo-logic-collectors-api
- collection_type: open
  name: Sumo Logic accessKeyManagement connectionManagement API
  slug: open-sumo-logic-connectionmanagement-api
- collection_type: open
  name: Sumo Logic REST Collectors Content API
  slug: open-sumo-logic-content-api
- collection_type: open
  name: Sumo Logic accessKeyManagement contentManagement API
  slug: open-sumo-logic-contentmanagement-api
- collection_type: open
  name: Sumo Logic accessKeyManagement contentPermissions API
  slug: open-sumo-logic-contentpermissions-api
- collection_type: open
  name: Sumo Logic accessKeyManagement dashboardManagement API
  slug: open-sumo-logic-dashboardmanagement-api
- collection_type: open
  name: Sumo Logic REST Collectors Dashboards API
  slug: open-sumo-logic-dashboards-api
- collection_type: open
  name: Sumo Logic accessKeyManagement dataDeletionRules API
  slug: open-sumo-logic-datadeletionrules-api
- collection_type: open
  name: Sumo Logic accessKeyManagement dataMaskingManagement API
  slug: open-sumo-logic-datamaskingmanagement-api
- collection_type: open
  name: Sumo Logic accessKeyManagement dynamicParsingRuleManagement API
  slug: open-sumo-logic-dynamicparsingrulemanagement-api
- collection_type: open
  name: Sumo Logic accessKeyManagement eventAnalytics API
  slug: open-sumo-logic-eventanalytics-api
- collection_type: open
  name: Sumo Logic accessKeyManagement extractionRuleManagement API
  slug: open-sumo-logic-extractionrulemanagement-api
- collection_type: open
  name: Sumo Logic accessKeyManagement fieldManagementV1 API
  slug: open-sumo-logic-fieldmanagementv1-api
- collection_type: open
  name: Sumo Logic accessKeyManagement folderManagement API
  slug: open-sumo-logic-foldermanagement-api
- collection_type: open
  name: Sumo Logic accessKeyManagement healthEvents API
  slug: open-sumo-logic-healthevents-api
- collection_type: open
  name: Sumo Logic accessKeyManagement ingestBudgetManagementV2 API
  slug: open-sumo-logic-ingestbudgetmanagementv2-api
- collection_type: open
  name: Sumo Logic accessKeyManagement logsDataForwardingManagement API
  slug: open-sumo-logic-logsdataforwardingmanagement-api
- collection_type: open
  name: Sumo Logic accessKeyManagement logSearchesEstimatedUsage API
  slug: open-sumo-logic-logsearchesestimatedusage-api
- collection_type: open
  name: Sumo Logic accessKeyManagement logSearchesManagement API
  slug: open-sumo-logic-logsearchesmanagement-api
- collection_type: open
  name: Sumo Logic accessKeyManagement lookupManagement API
  slug: open-sumo-logic-lookupmanagement-api
- collection_type: open
  name: Sumo Logic accessKeyManagement macroManagement API
  slug: open-sumo-logic-macromanagement-api
- collection_type: open
  name: Sumo Logic accessKeyManagement metricsQuery API
  slug: open-sumo-logic-metricsquery-api
- collection_type: open
  name: Sumo Logic accessKeyManagement metricsSearchesManagement API
  slug: open-sumo-logic-metricssearchesmanagement-api
- collection_type: open
  name: Sumo Logic accessKeyManagement metricsSearchesManagementV2 API
  slug: open-sumo-logic-metricssearchesmanagementv2-api
- collection_type: open
  name: Sumo Logic REST Collectors Monitors API
  slug: open-sumo-logic-monitors-api
- collection_type: open
  name: Sumo Logic accessKeyManagement monitorsLibraryManagement API
  slug: open-sumo-logic-monitorslibrarymanagement-api
- collection_type: open
  name: Sumo Logic accessKeyManagement mutingSchedulesLibraryManagement API
  slug: open-sumo-logic-mutingscheduleslibrarymanagement-api
- collection_type: open
  name: Sumo Logic accessKeyManagement oauthManagement API
  slug: open-sumo-logic-oauthmanagement-api
- collection_type: open
  name: Sumo Logic accessKeyManagement orgsManagement API
  slug: open-sumo-logic-orgsmanagement-api
- collection_type: open
  name: Sumo Logic accessKeyManagement otCollectorManagementExternal API
  slug: open-sumo-logic-otcollectormanagementexternal-api
- collection_type: open
  name: Sumo Logic accessKeyManagement parsersLibraryManagement API
  slug: open-sumo-logic-parserslibrarymanagement-api
- collection_type: open
  name: Sumo Logic accessKeyManagement partitionManagement API
  slug: open-sumo-logic-partitionmanagement-api
- collection_type: open
  name: Sumo Logic accessKeyManagement passwordPolicy API
  slug: open-sumo-logic-passwordpolicy-api
- collection_type: open
  name: Sumo Logic accessKeyManagement policiesManagement API
  slug: open-sumo-logic-policiesmanagement-api
- collection_type: open
  name: Sumo Logic accessKeyManagement roleManagement API
  slug: open-sumo-logic-rolemanagement-api
- collection_type: open
  name: Sumo Logic accessKeyManagement roleManagementV2 API
  slug: open-sumo-logic-rolemanagementv2-api
- collection_type: open
  name: Sumo Logic REST Collectors Roles API
  slug: open-sumo-logic-roles-api
- collection_type: open
  name: Sumo Logic accessKeyManagement samlConfigurationManagement API
  slug: open-sumo-logic-samlconfigurationmanagement-api
- collection_type: open
  name: Sumo Logic accessKeyManagement scheduledViewManagement API
  slug: open-sumo-logic-scheduledviewmanagement-api
- collection_type: open
  name: Sumo Logic accessKeyManagement schemaBaseManagement API
  slug: open-sumo-logic-schemabasemanagement-api
- collection_type: open
  name: Sumo Logic accessKeyManagement scimUserManagement API
  slug: open-sumo-logic-scimusermanagement-api
- collection_type: open
  name: Sumo Logic REST Collectors Search Jobs API
  slug: open-sumo-logic-search-jobs-api
- collection_type: open
  name: Sumo Logic accessKeyManagement serviceAccountManagement API
  slug: open-sumo-logic-serviceaccountmanagement-api
- collection_type: open
  name: Sumo Logic accessKeyManagement serviceAllowlistManagement API
  slug: open-sumo-logic-serviceallowlistmanagement-api
- collection_type: open
  name: Sumo Logic accessKeyManagement serviceMap API
  slug: open-sumo-logic-servicemap-api
- collection_type: open
  name: Sumo Logic accessKeyManagement slosLibraryManagement API
  slug: open-sumo-logic-sloslibrarymanagement-api
- collection_type: open
  name: Sumo Logic accessKeyManagement sourceTemplateManagementExternal API
  slug: open-sumo-logic-sourcetemplatemanagementexternal-api
- collection_type: open
  name: Sumo Logic accessKeyManagement spanAnalytics API
  slug: open-sumo-logic-spananalytics-api
- collection_type: open
  name: Sumo Logic accessKeyManagement threatIntelIngest API
  slug: open-sumo-logic-threatintelingest-api
- collection_type: open
  name: Sumo Logic accessKeyManagement threatIntelIngestProducer API
  slug: open-sumo-logic-threatintelingestproducer-api
- collection_type: open
  name: Sumo Logic accessKeyManagement tokensLibraryManagement API
  slug: open-sumo-logic-tokenslibrarymanagement-api
- collection_type: open
  name: Sumo Logic accessKeyManagement traces API
  slug: open-sumo-logic-traces-api
- collection_type: open
  name: Sumo Logic accessKeyManagement transformationRuleManagement API
  slug: open-sumo-logic-transformationrulemanagement-api
- collection_type: open
  name: Sumo Logic accessKeyManagement userManagement API
  slug: open-sumo-logic-usermanagement-api
- collection_type: open
  name: Sumo Logic REST Collectors Users API
  slug: open-sumo-logic-users-api
- collection_type: open
  name: Sumo Logic API
  slug: open-sumo-logic
- collection_type: open
  name: Sumo Logic REST API
  slug: open-sumologic
common:
- group: commercial
  title: ''
  type: Pricing
  url: https://www.sumologic.com/pricing
- group: other
  href: https://artifacts.apis.io/sumo-logic/capabilities/sumo-logic-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/sumo-logic-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/sumo-logic/agentic-access/sumo-logic-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/sumo-logic-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/sumo-logic/security/sumo-logic-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/sumo-logic-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/sumo-logic/security/sumo-logic-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/sumo-logic-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/sumo-logic/authentication/sumo-logic-authentication.yml
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
- group: build
  title: ''
  type: GitHub
  url: https://github.com/SumoLogic
- group: operate
  title: ''
  type: Status
  url: https://status.sumologic.com/
- group: commercial
  href: https://artifacts.apis.io/sumo-logic/plans/sumo-logic-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/sumo-logic-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/sumo-logic/rate-limits/sumo-logic-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/sumo-logic-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/sumo-logic/finops/sumo-logic-finops.yml
  title: ''
  type: FinOps
  url: finops/sumo-logic-finops.yml
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
- has_sources: true
  method: derived
  name: Sumo Logic Finops
  primary_unit: ''
  service_category: ''
  slug: sumo-logic-finops
  template: true
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
mcp_servers:
- description: Remote MCP server at mcp.sumologic.com over HTTP.
  name: Sumo Logic MCP Server
  slug: sumo-logic
modified: '2026-08-08'
name: Sumo Logic
nav: Providers
network: true
overview: 'Sumo Logic publishes 57 API contracts indexed on the [APIs.io](https://apis.io/) network, including Access Key Management API, App Management V2 API, Archive Management API, and 54 more. Tagged areas include Logging, Observability, Security, Monitoring, and Analytics.


  The Sumo Logic catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 3 Spectral governance rulesets.


  Sumo Logic''s developer surface includes pricing, authentication, developer portal, documentation, getting-started guide, engineering blog, GitHub presence, and 13 more developer resources.'
plans:
- name: Sumo Logic Plans Pricing
  plan_count: 2
  slug: sumo-logic-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 5
  name: Sumo Logic Rate Limits
  slug: sumo-logic-rate-limits
rules:
- authorship: generated
  effective_rule_count: 36
  extends:
  - spectral:asyncapi
  name: Sumo Logic — asyncapi rules
  rule_count: 9
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 7
  slug: sumo-logic-asyncapi-spectral-rules
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: Sumo Logic — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: sumo-logic-jsonschema-spectral-rules
- authorship: unmarked
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: Sumo Logic API Rules
  rule_count: 9
  severity_counts:
    error: 2
    hint: 0
    info: 2
    warn: 5
  slug: sumo-logic-rules
score:
  band: developing
  composite: 47.1
  coverage:
    artifact_dirs: 24
    catalog_earned: 60.5
    catalog_earned_first_party: 8.0
    catalog_gap: 54.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.0
  facets:
    access_clarity: 34.2
    contract_governance: 13.6
    contract_quality: 66.0
    developer_ergonomics: 52.4
    discoverability: 68.3
    operational_transparency: 26.3
  previous_composite: 48.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 57
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 21.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 11.1
screenshot: https://apis.io/screenshots/sumo-logic/sumo-logic-2026-06-20T194649.png
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
