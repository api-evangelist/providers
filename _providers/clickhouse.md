---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: derived
    idempotency: false
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 58.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 81
  human_in_the_loop: 1
  name: Clickhouse Agentic Access
  operation_count: 153
  slug: clickhouse-agentic-access
  summary_line: 153 operations · 81 acting · 1 human-in-the-loop
api_count: 3
apis:
- description: HTTP interface (default port 8123, HTTPS 8443) for executing SQL queries against ClickHouse. Supports SELECT via GET, mutations via POST, multiple output formats (JSON, CSV, XML, TabSeparated), and au
  name: ClickHouse HTTP Interface
  slug: clickhouse-http-interface
- description: Native binary TCP protocol used by ClickHouse client libraries for maximum throughput between client and server (default port 9000).
  name: ClickHouse Native TCP Interface
  slug: clickhouse-native
- description: MySQL wire protocol compatibility allowing existing MySQL clients and BI tools to query ClickHouse without driver changes.
  name: ClickHouse MySQL Interface
  slug: clickhouse-mysql
- description: PostgreSQL wire protocol compatibility for connecting psql, JDBC and other PostgreSQL clients to ClickHouse.
  name: ClickHouse PostgreSQL Interface
  slug: clickhouse-postgresql
- description: gRPC interface defined by clickhouse_grpc.proto for efficient binary communication.
  name: ClickHouse gRPC Interface
  slug: clickhouse-grpc
- baseURL: https://{clickhouse-host}:8443
  baseurl_source: declared
  description: The ClickHouse HTTP Interface API from ClickHouse — 1 operation(s) for clickhouse http interface.
  name: ClickHouse HTTP Interface API
  phrasing_intents:
  - id: getRoot
    intent: Run a read-only SQL query over HTTP GET
    question: How do I run a SELECT against ClickHouse by putting the SQL in the URL?
  - id: postRoot
    intent: Execute SQL or insert data via HTTP POST
    question: How do I insert rows into a ClickHouse table over HTTP by streaming them in the request body?
  phrasing_ops: 2
  slug: clickhouse-clickhouse-http-interface-api
- baseURL: https://{clickhouse-host}:8443
  baseurl_source: declared
  description: The Ping API from ClickHouse — 1 operation(s) for ping.
  name: ClickHouse Ping API
  phrasing_intents:
  - id: getPing
    intent: Ping the server to check it is healthy
    question: Is my ClickHouse server up and responding?
  phrasing_ops: 1
  slug: clickhouse-ping-api
- baseURL: https://{clickhouse-host}:8443
  baseurl_source: declared
  description: The Play API from ClickHouse — 1 operation(s) for play.
  name: ClickHouse Play API
  phrasing_intents:
  - id: getPlay
    intent: Open the built-in Play web UI
    question: Where is the browser-based SQL console that ships with ClickHouse?
  phrasing_ops: 1
  slug: clickhouse-play-api
- baseURL: https://{clickhouse-host}:8443
  baseurl_source: declared
  description: The Replicas Status API from ClickHouse — 1 operation(s) for replicas status.
  name: ClickHouse Replicas Status API
  phrasing_intents:
  - id: getReplicasStatus
    intent: Check replica delay across the cluster
    question: Are any of my ClickHouse replicas lagging behind?
  phrasing_ops: 1
  slug: clickhouse-replicas-status-api
- baseURL: https://{clickhouse-host}:8443
  baseurl_source: declared
  description: The API keys API from ClickHouse — 2 operation(s) for api keys.
  name: ClickHouse API keys API
  phrasing_intents:
  - id: openapiKeyGetList
    intent: List an organization's API keys
    question: Which API keys exist in my ClickHouse Cloud organization?
  - id: openapiKeyCreate
    intent: Create a new API key
    question: How do I generate a new API key for automation?
  - id: openapiKeyGet
    intent: Get details of one API key
    question: What roles and expiry does a specific API key have?
  - id: openapiKeyUpdate
    intent: Update an existing API key
    question: How do I disable an existing API key without deleting it?
  - id: openapiKeyDelete
    intent: Delete an API key
    question: How do I permanently remove an API key we no longer use?
  phrasing_ops: 5
  slug: clickhouse-api-keys-api
- baseURL: https://{clickhouse-host}:8443
  baseurl_source: declared
  description: The Backup API from ClickHouse — 4 operation(s) for backup.
  name: ClickHouse Backup API
  phrasing_intents:
  - id: backupGetList
    intent: List a service's backups
    question: What backups exist for my ClickHouse service, newest first?
  - id: backupGet
    intent: Get details of one backup
    question: What are the details of one particular backup?
  - id: backupConfigurationGet
    intent: Get a service's backup schedule and retention
    question: How often is my service backed up and how long are backups kept?
  - id: backupConfigurationUpdate
    intent: Change a service's backup schedule and retention
    question: Can I take backups every 12 hours and keep them longer?
  - id: backupBucketGet
    intent: Get a service's custom backup bucket
    question: Which external bucket are my service's backups written to?
  - id: backupBucketCreate
    intent: Set up a custom backup bucket for a service
    question: How do I send my service's backups to a bucket in my own cloud account?
  - id: backupBucketUpdate
    intent: Update a service's custom backup bucket
    question: How do I rotate the credentials on my existing backup bucket?
  - id: backupBucketDelete
    intent: Remove a service's custom backup bucket
    question: How do I stop using my own bucket for a service's backups?
  phrasing_ops: 8
  slug: clickhouse-backup-api
- baseURL: https://{clickhouse-host}:8443
  baseurl_source: declared
  description: The Billing API from ClickHouse — 3 operation(s) for billing.
  name: ClickHouse Billing API
  phrasing_intents:
  - id: usageCostGet
    intent: Get daily usage costs for the organization
    question: How much did my ClickHouse Cloud organization spend last month, broken down by day?
  - id: activeBalancesGet
    intent: List prepaid balances (deprecated endpoint)
    question: What prepaid balances does my org have, using the older deprecated balances endpoint?
  - id: creditBalancesGet
    intent: Get the organization's remaining credits
    question: How many credits do we have left, and which balance expires first?
  phrasing_ops: 3
  slug: clickhouse-billing-api
- baseURL: https://{clickhouse-host}:8443
  baseurl_source: declared
  description: The ClickPipes API from ClickHouse — 10 operation(s) for clickpipes.
  name: ClickHouse Click Pipes API
  phrasing_intents:
  - id: clickPipeGetList
    intent: List a service's ClickPipes
    question: Which ClickPipes are ingesting data into my ClickHouse service?
  - id: clickPipeCreate
    intent: Create a ClickPipe to ingest data
    question: How do I start streaming data from a source into a ClickHouse table?
  - id: clickPipesServiceContextGet
    intent: Get a service's ClickPipes capabilities and identity
    question: Which GCP service account do I need to grant access to my source for ClickPipes?
  - id: clickPipeGet
    intent: Get details of one ClickPipe
    question: What is the current state and source of a specific ClickPipe?
  - id: clickPipeUpdate
    intent: Update a ClickPipe's name, source or mappings
    question: Which source fields can I still change after a pipe is created?
  - id: clickPipeDelete
    intent: Delete a ClickPipe
    question: How do I permanently remove an ingestion pipe I no longer need?
  - id: clickPipeSettingsGet
    intent: Get a ClickPipe's advanced settings
    question: What advanced tuning settings are applied to one of my ClickPipes?
  - id: clickPipeSettingsUpdate
    intent: Tune a ClickPipe's advanced settings
    question: Can I make a streaming pipe wait longer before inserting to batch bigger blocks?
  phrasing_ops: 18
  slug: clickhouse-clickpipes-api
- baseURL: https://{clickhouse-host}:8443
  baseurl_source: declared
  description: The ClickStack API from ClickHouse — 13 operation(s) for clickstack.
  name: ClickHouse Click Stack API
  phrasing_intents:
  - id: clickStackListDashboards
    intent: List ClickStack dashboards
    question: Which observability dashboards exist in ClickStack for my service?
  - id: clickStackCreateDashboard
    intent: Create a ClickStack dashboard
    question: How do I build a new observability dashboard with chart tiles in ClickStack?
  - id: clickStackGetDashboard
    intent: Get one ClickStack dashboard
    question: What tiles and filters are on a specific ClickStack dashboard?
  - id: clickStackUpdateDashboard
    intent: Update an existing ClickStack dashboard
    question: How do I change the tiles on a dashboard I already built?
  - id: clickStackDeleteDashboard
    intent: Delete a ClickStack dashboard
    question: How do I remove a ClickStack dashboard nobody uses anymore?
  - id: clickStackValidateDashboard
    intent: Validate a dashboard definition without saving
    question: Can I check a dashboard definition is valid before applying it from Terraform?
  - id: clickStackListAlerts
    intent: List ClickStack alerts
    question: Which alerts are configured in ClickStack for my team?
  - id: clickStackCreateAlert
    intent: Create a ClickStack alert
    question: How do I get alerted when a saved search crosses a threshold?
  phrasing_ops: 30
  slug: clickhouse-clickstack-api
- baseURL: https://{clickhouse-host}:8443
  baseurl_source: declared
  description: The Organization API from ClickHouse — 9 operation(s) for organization.
  name: ClickHouse Organization API
  phrasing_intents:
  - id: organizationGetList
    intent: Find the organization tied to my API key
    question: Which ClickHouse Cloud organization does my API key belong to?
  - id: organizationGet
    intent: Get organization details
    question: What are the name and settings of my organization?
  - id: organizationUpdate
    intent: Rename or reconfigure the organization
    question: How do I rename our organization?
  - id: organizationQuotasGetList
    intent: List organization resource quotas and usage
    question: What resource limits apply to my organization and how close am I to them?
  - id: organizationQuotaGet
    intent: Get one organization quota by code
    question: What is the limit and current usage for one specific quota?
  - id: activityGetList
    intent: List the organization's activity log
    question: Who changed what in our organization over the last week?
  - id: activityGet
    intent: Get one organization activity entry
    question: What exactly happened in a particular audit log entry?
  - id: organizationPrivateEndpointConfigGetList
    intent: Get org private endpoint config for a region (deprecated)
    question: What private endpoint configuration applies to a cloud region at the organization level?
  phrasing_ops: 11
  slug: clickhouse-organization-api
- baseURL: https://{clickhouse-host}:8443
  baseurl_source: declared
  description: The Postgres API from ClickHouse — 12 operation(s) for postgres.
  name: ClickHouse Postgres API
  phrasing_intents:
  - id: postgresServiceCreate
    intent: Create a managed Postgres service
    question: How do I spin up a new managed Postgres database?
  - id: postgresServiceGetList
    intent: List managed Postgres services
    question: Which managed Postgres databases do we run in ClickHouse Cloud?
  - id: postgresServiceGet
    intent: Get a Postgres service's details
    question: What's the current status of one of my Postgres databases?
  - id: postgresServiceDelete
    intent: Delete a Postgres service
    question: How do I permanently delete a managed Postgres database?
  - id: postgresServicePatch
    intent: Rename or resize a Postgres service
    question: How do I resize an existing Postgres database?
  - id: postgresServiceCertsGet
    intent: Download a Postgres service's CA certificates
    question: Where do I get the CA certificate to connect to my Postgres database over TLS?
  - id: postgresInstanceRestore
    intent: Restore a Postgres service to a new service
    question: How do I restore my Postgres database to a specific point in time?
  - id: postgresServiceSetPassword
    intent: Reset a Postgres superuser password
    question: How do I reset the superuser password on my managed Postgres database?
  phrasing_ops: 17
  slug: clickhouse-postgres-api
- baseURL: https://{clickhouse-host}:8443
  baseurl_source: declared
  description: The Prometheus API from ClickHouse — 5 operation(s) for prometheus.
  name: ClickHouse Prometheus API
  phrasing_intents:
  - id: organizationPrometheusGet
    intent: Get org-wide Prometheus metrics (deprecated)
    question: Can I still scrape all my services' metrics from the older single org-wide Prometheus endpoint?
  - id: organizationPrometheusDiscoveryGet
    intent: List Prometheus scrape targets for every service
    question: How do I point Prometheus http_sd service discovery at all my ClickHouse services?
  - id: instancePrometheusGet
    intent: Get Prometheus metrics for one ClickHouse service
    question: How do I scrape Prometheus metrics from a single ClickHouse service?
  - id: postgresOrgPrometheusGet
    intent: Get Prometheus metrics for all Postgres services
    question: How do I scrape metrics for every managed Postgres service in my org at once?
  - id: postgresInstancePrometheusGet
    intent: Get Prometheus metrics for one Postgres service
    question: How do I scrape Prometheus metrics from a single managed Postgres service?
  phrasing_ops: 5
  slug: clickhouse-prometheus-api
- baseURL: https://{clickhouse-host}:8443
  baseurl_source: declared
  description: The Role Management API from ClickHouse — 2 operation(s) for role management.
  name: ClickHouse Role Management API
  phrasing_intents:
  - id: organizationRolesGetList
    intent: List the organization's roles
    question: Which system and custom roles are available in my ClickHouse Cloud organization?
  - id: organizationRolePost
    intent: Create a custom organization role
    question: How do I create a custom role with its own permission policies?
  - id: organizationRoleGet
    intent: Get a role's policies and actors
    question: What permissions does a particular role grant?
  - id: organizationRolePatch
    intent: Update a custom organization role
    question: How do I add or remove actors from an existing custom role?
  - id: organizationRoleDelete
    intent: Delete a custom organization role
    question: How do I delete a custom role and all its policies?
  phrasing_ops: 5
  slug: clickhouse-role-management-api
- baseURL: https://{clickhouse-host}:8443
  baseurl_source: declared
  description: The Service API from ClickHouse — 15 operation(s) for service.
  name: ClickHouse Service API
  phrasing_intents:
  - id: serviceProfilesList
    intent: List instance profiles available in a region
    question: Which custom instance profiles can I use for a new service in a region?
  - id: instanceGetList
    intent: List ClickHouse services in the organization
    question: What ClickHouse services are running in my organization?
  - id: instanceCreate
    intent: Create a new ClickHouse service
    question: How do I spin up a new ClickHouse Cloud service?
  - id: instanceGet
    intent: Get a ClickHouse service's details
    question: What state is my ClickHouse service in right now?
  - id: instanceUpdate
    intent: Rename a service or change its IP access list
    question: How do I rename a ClickHouse service?
  - id: instanceDelete
    intent: Delete a stopped ClickHouse service
    question: How do I permanently delete a ClickHouse service?
  - id: instancePrivateEndpointConfigGet
    intent: Get the info needed to set up a private endpoint
    question: What endpoint service name do I need to set up PrivateLink to my ClickHouse service?
  - id: instanceQueryEndpointGet
    intent: Get a service's query-over-API endpoint config
    question: Is the query API endpoint enabled on my ClickHouse service?
  phrasing_ops: 26
  slug: clickhouse-service-api
- baseURL: https://{clickhouse-host}:8443
  baseurl_source: declared
  description: The UDF API from ClickHouse — 7 operation(s) for udf.
  name: ClickHouse UDF API
  phrasing_intents:
  - id: udfUploadSessionCreate
    intent: Get a presigned URL to upload UDF code
    question: Where do I upload the zip archive containing my UDF source code?
  - id: udfList
    intent: List the organization's UDFs
    question: What user-defined functions exist in my ClickHouse Cloud organization?
  - id: udfCreate
    intent: Create a new UDF
    question: How do I create a brand-new user-defined function in ClickHouse Cloud?
  - id: udfDelete
    intent: Delete a UDF and all its versions
    question: How do I delete a user-defined function everywhere it's used?
  - id: udfGet
    intent: Get the latest version of a UDF
    question: What is the latest version of a particular user-defined function?
  - id: udfAttachmentList
    intent: List the services a UDF is attached to
    question: Which services is a given user-defined function attached to?
  - id: udfDetach
    intent: Detach a UDF from a service
    question: How do I remove a user-defined function from just one service?
  - id: udfAttachmentGet
    intent: Check a UDF's attachment to one service
    question: Which version of a user-defined function is attached to a particular service?
  phrasing_ops: 12
  slug: clickhouse-udf-api
- baseURL: https://{clickhouse-host}:8443
  baseurl_source: declared
  description: The User management API from ClickHouse — 4 operation(s) for user management.
  name: ClickHouse User management API
  phrasing_intents:
  - id: memberGetList
    intent: List organization members
    question: Who are the members of my ClickHouse Cloud organization?
  - id: memberGet
    intent: Get one member's details
    question: What role does a specific member have in our organization?
  - id: memberUpdate
    intent: Change a member's role
    question: How do I promote a member to admin?
  - id: memberDelete
    intent: Remove a member from the organization
    question: How do I remove someone who left the company from our organization?
  - id: invitationGetList
    intent: List pending organization invitations
    question: Which invitations to our organization are still outstanding?
  - id: invitationCreate
    intent: Invite someone to the organization
    question: How do I invite a teammate to our ClickHouse Cloud org by email?
  - id: invitationGet
    intent: Get one invitation's details
    question: What email and role is a specific invitation for?
  - id: invitationDelete
    intent: Cancel an organization invitation
    question: How do I cancel an invite I sent to the wrong email address?
  phrasing_ops: 8
  slug: clickhouse-user-management-api
- baseURL: https://api.clickhouse.cloud
  baseurl_source: declared
  description: The Notifications API from ClickHouse — 2 operation(s) for notifications.
  name: ClickHouse Notifications API
  slug: clickhouse-notifications-api
- baseURL: https://api.clickhouse.cloud
  baseurl_source: declared
  description: The Query API endpoints API from ClickHouse — 2 operation(s) for query api endpoints.
  name: ClickHouse Query API endpoints API
  slug: clickhouse-query-api-endpoints-api
- baseURL: https://api.clickhouse.cloud
  baseurl_source: declared
  description: The Saved queries API from ClickHouse — 2 operation(s) for saved queries.
  name: ClickHouse Saved queries API
  slug: clickhouse-saved-queries-api
- baseURL: https://api.clickhouse.cloud
  baseurl_source: declared
  description: The Snapshot API from ClickHouse — 3 operation(s) for snapshot.
  name: ClickHouse Snapshot API
  slug: clickhouse-snapshot-api
artifact_total: 61
asyncapis:
- description: AsyncAPI description of the documented streaming surface that ClickHouse offers through the Kafka table engine. ClickHouse itself does NOT publish a public WebSocket, Server-Sent Events, or push-style
  name: ClickHouse Kafka Table Engine (Consumer-Side Streaming)
  slug: clickhouse-kafka-engine-asyncapi
- description: ''
  name: Clickhouse Webhooks
  slug: clickhouse-webhooks
collections:
- collection_type: postman
  name: ClickHouse HTTP Interface API
  slug: postman-clickhouse-clickhouse-http-interface-api
- collection_type: postman
  name: ClickHouse HTTP Interface Ping API
  slug: postman-clickhouse-ping-api
- collection_type: postman
  name: ClickHouse HTTP Interface Play API
  slug: postman-clickhouse-play-api
- collection_type: postman
  name: ClickHouse HTTP Interface Replicas Status API
  slug: postman-clickhouse-replicas-status-api
- collection_type: open
  name: ClickHouse HTTP Interface API
  slug: open-clickhouse-clickhouse-http-interface-api
- collection_type: open
  name: ClickHouse HTTP Interface Ping API
  slug: open-clickhouse-ping-api
- collection_type: open
  name: ClickHouse HTTP Interface Play API
  slug: open-clickhouse-play-api
- collection_type: open
  name: ClickHouse HTTP Interface Replicas Status API
  slug: open-clickhouse-replicas-status-api
- collection_type: open
  name: ClickHouse HTTP Interface
  slug: open-clickhouse
common:
- group: commercial
  href: https://artifacts.apis.io/clickhouse/finops/clickhouse-finops.yml
  title: ''
  type: FinOps
  url: finops/clickhouse-finops.yml
- group: other
  href: https://artifacts.apis.io/clickhouse/capabilities/clickhouse-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/clickhouse-capability-edges.yml
- group: auth
  href: https://artifacts.apis.io/clickhouse/security/clickhouse-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/clickhouse-vulnerability-disclosure.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/clickhouse/overview
- group: agent
  href: https://artifacts.apis.io/clickhouse/agentic-access/clickhouse-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/clickhouse-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/clickhouse/security/clickhouse-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/clickhouse-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/clickhouse/security/clickhouse-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/clickhouse-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/clickhouse/authentication/clickhouse-authentication.yml
  title: ''
  type: Authentication
  url: authentication/clickhouse-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/clickhouseinc
- group: company
  title: ''
  type: Website
  url: https://clickhouse.com/
- group: docs
  title: ''
  type: Documentation
  url: https://clickhouse.com/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://clickhouse.com/docs/quick-start
- group: build
  title: ''
  type: GitHub
  url: https://github.com/ClickHouse/ClickHouse
- group: company
  title: ''
  type: Blog
  url: https://clickhouse.com/blog
- group: operate
  title: ''
  type: Community
  url: https://clickhouse.com/community
- group: operate
  title: ''
  type: Slack
  url: https://clickhouse.com/slack
- group: commercial
  title: ''
  type: Pricing
  url: https://clickhouse.com/pricing
- group: operate
  title: ''
  type: Support
  url: https://clickhouse.com/support
- group: operate
  title: ''
  type: StatusPage
  url: https://status.clickhouse.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://clickhouse.com/legal/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://clickhouse.com/legal/clickhouse-general-terms-and-conditions
- group: design
  href: https://artifacts.apis.io/clickhouse/json-ld/clickhouse-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/clickhouse-context.jsonld
- group: design
  href: https://artifacts.apis.io/clickhouse/rules/clickhouse-rules.yml
  title: ''
  type: Spectral
  url: rules/clickhouse-rules.yml
- group: other
  href: https://artifacts.apis.io/clickhouse/ai-catalog/clickhouse-ai-catalog.yml
  title: ''
  type: AICatalog
  url: ai-catalog/clickhouse-ai-catalog.yml
- group: build
  href: https://artifacts.apis.io/clickhouse/packages/clickhouse-packages.yml
  title: ''
  type: Packages
  url: packages/clickhouse-packages.yml
- group: build
  href: https://artifacts.apis.io/clickhouse/packages/clickhouse-packages.yml
  title: ''
  type: SDKs
  url: packages/clickhouse-packages.yml
- group: build
  href: https://artifacts.apis.io/clickhouse/cli/clickhouse-cli.yml
  title: ''
  type: CLI
  url: cli/clickhouse-cli.yml
- group: agent
  href: https://artifacts.apis.io/clickhouse/well-known/clickhouse-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/clickhouse-well-known.yml
- group: auth
  href: https://artifacts.apis.io/clickhouse/well-known/clickhouse-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/clickhouse-security.txt
- group: other
  href: https://artifacts.apis.io/clickhouse/well-known/clickhouse-api-catalog.json
  title: ''
  type: APICatalog
  url: well-known/clickhouse-api-catalog.json
- group: auth
  href: https://artifacts.apis.io/clickhouse/security/clickhouse-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/clickhouse-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/clickhouse/security/clickhouse-trust-center.yml
  title: ''
  type: Compliance
  url: security/clickhouse-trust-center.yml
- group: agent
  href: https://artifacts.apis.io/clickhouse/mcp/clickhouse-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/clickhouse-mcp.yml
- group: build
  href: https://artifacts.apis.io/clickhouse/mcp/clickhouse-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/clickhouse-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/clickhouse/llms/clickhouse-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/clickhouse-llms.txt
- group: other
  href: https://artifacts.apis.io/clickhouse/grpc/clickhouse-grpc.proto
  title: ''
  type: Protobuf
  url: grpc/clickhouse-grpc.proto
- group: design
  href: https://artifacts.apis.io/clickhouse/conformance/clickhouse-conformance.yml
  title: ''
  type: Conformance
  url: conformance/clickhouse-conformance.yml
- group: design
  href: https://artifacts.apis.io/clickhouse/errors/clickhouse-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/clickhouse-problem-types.yml
- group: design
  href: https://artifacts.apis.io/clickhouse/lifecycle/clickhouse-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/clickhouse-lifecycle.yml
- group: auth
  href: https://artifacts.apis.io/clickhouse/scopes/clickhouse-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/clickhouse-scopes.yml
- group: design
  href: https://artifacts.apis.io/clickhouse/conventions/clickhouse-conventions.yml
  title: ''
  type: Conventions
  url: conventions/clickhouse-conventions.yml
- group: start
  href: https://artifacts.apis.io/clickhouse/sandbox/clickhouse-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/clickhouse-sandbox.yml
- group: operate
  href: https://artifacts.apis.io/clickhouse/changelog/clickhouse-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/clickhouse-changelog.yml
- group: design
  href: https://artifacts.apis.io/clickhouse/data-model/clickhouse-data-model.yml
  title: ''
  type: DataModel
  url: data-model/clickhouse-data-model.yml
- group: design
  href: https://artifacts.apis.io/clickhouse/asyncapi/clickhouse-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/clickhouse-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/clickhouse/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  href: https://artifacts.apis.io/clickhouse/plans/clickhouse-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/clickhouse-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/clickhouse/rate-limits/clickhouse-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/clickhouse-rate-limits.yml
- group: other
  href: https://artifacts.apis.io/clickhouse/overlays/clickhouse-cloud-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/clickhouse-cloud-api-overlay.yaml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://clickhouse.com/docs/cloud/manage/api/api-overview
- group: docs
  title: ''
  type: APIReference
  url: https://clickhouse.com/docs/products/cloud/api-reference/organization/get-list-of-available-organizations
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ClickHouse
- group: start
  title: ''
  type: SignUp
  url: https://console.clickhouse.cloud/signUp
- group: start
  title: ''
  type: Quickstart
  url: https://clickhouse.com/docs/quick-start
- group: other
  title: ''
  type: Playground
  url: https://sql.clickhouse.com
created: '2024-01-01'
description: ClickHouse is a fast open-source column-oriented database management system that enables real-time analytical reporting using SQL. ClickHouse exposes multiple interfaces - an HTTP interface for SQL queries, native TCP, MySQL and PostgreSQL wire-compatible interfaces, and a gRPC interface - and the ClickHouse Cloud management plane offers a public OpenAPI-described REST API for provisioning and managing services, organizations, members, API keys, backups, and private endpoints.
finops:
- has_sources: true
  method: derived
  name: Clickhouse Finops
  primary_unit: compute unit / hr
  service_category: ''
  slug: clickhouse-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/clickhouse.png
jsonld:
- class_count: 0
  name: Clickhouse Context
  property_count: 5
  slug: clickhouse-context
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.clickhouse.cloud requiring OAuth; 13 tools listed.
  name: ClickHouse MCP Server
  slug: clickhouse-mcp-yml
modified: '2026-09-16'
name: ClickHouse
nav: Providers
network: true
overview: 'ClickHouse publishes 25 API contracts indexed on the [APIs.io](https://apis.io/) network, including HTTP Interface API, Ping API, Play API, and 22 more. Tagged areas include ClickHouse, Analytics, Cloud Database, Column-Oriented, and Database.


  The ClickHouse catalog on APIs.io includes 2 event-driven AsyncAPI specifications, 1 JSON-LD context, and 2 Spectral governance rulesets.


  ClickHouse''s developer surface includes authentication, documentation, getting-started guide, GitHub presence, engineering blog, pricing, support, and 48 more developer resources.'
plans:
- name: Clickhouse Plans Pricing
  plan_count: 5
  slug: clickhouse-plans-pricing
- name: Clickhouse Price Estimates
  plan_count: 0
  slug: clickhouse-price-estimates
random_paper: 10
rate_limits:
- limit_count: 1
  name: Clickhouse Rate Limits
  slug: clickhouse-rate-limits
rules:
- authorship: generated
  effective_rule_count: 30
  extends:
  - spectral:asyncapi
  name: ClickHouse — asyncapi rules
  rule_count: 3
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 3
  slug: clickhouse-asyncapi-spectral-rules
- authorship: unmarked
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: ClickHouse API Rules
  rule_count: 9
  severity_counts:
    error: 4
    hint: 0
    info: 0
    warn: 5
  slug: clickhouse-rules
scopes:
- name: Clickhouse Scopes
  scope_count: 5
  slug: clickhouse-scopes
  summary_line: 5 scopes
score:
  band: exemplar
  composite: 76.9
  coverage:
    artifact_dirs: 37
    catalog_earned: 66.8
    catalog_earned_first_party: 20.0
    catalog_gap: 48.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 86.8
    contract_governance: 15.9
    contract_quality: 61.9
    developer_ergonomics: 83.3
    discoverability: 71.7
    operational_transparency: 73.7
  previous_composite: 76.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 33
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 45.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 50.0
screenshot: https://apis.io/screenshots/clickhouse/clickhouse-2026-06-20T174515.png
security:
- kind: authentication
  name: Clickhouse Authentication
  slug: clickhouse-authentication
  summary_line: http/apiKey/oauth2 · 0 schemes
- kind: domain-security
  name: Clickhouse Domain Security
  slug: clickhouse-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Clickhouse Vulnerability Disclosure
  slug: clickhouse-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Clickhouse Trust Center
  slug: clickhouse-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, HIPAA, GDPR
skill_count: 11
skills:
- name: clickhouse-architecture-advisor
  slug: clickhouse-architecture-advisor
- name: clickhouse-best-practices
  slug: clickhouse-best-practices
- name: chdb-datastore
  slug: clickhouse-chdb-datastore
- name: chdb-sql
  slug: clickhouse-chdb-sql
- name: clickstack-otel-collector
  slug: clickhouse-clickstack-otel-collector
- name: infra-clickhouse
  slug: clickhouse-infra-clickhouse
- name: infra-postgres
  slug: clickhouse-infra-postgres
- name: clickhouse-js-node-coding
  slug: clickhouse-js-node-coding
- name: clickhouse-js-node-rowbinary
  slug: clickhouse-js-node-rowbinary
- name: clickhouse-js-node-troubleshooting
  slug: clickhouse-js-node-troubleshooting
- name: clickhouse-managed-postgres-rca
  slug: clickhouse-managed-postgres-rca
slug: clickhouse
tags:
- ClickHouse
- Analytics
- Cloud Database
- Column-Oriented
- Database
- OLAP
- Open Source
- Real-Time
- SQL
website: https://clickhouse.com/
---
