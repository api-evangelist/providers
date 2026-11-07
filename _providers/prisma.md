---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - scopes
  - security
  - sandbox
  trial: false
  try_now: true
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
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: derived
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: mostly
    pagination_ratio: partial
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 54.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 91
  human_in_the_loop: 3
  name: Prisma Agentic Access
  operation_count: 175
  slug: prisma-agentic-access
  summary_line: 175 operations · 91 acting · 3 human-in-the-loop
api_count: 7
apis:
- baseURL: https://localhost:3000/api
  baseurl_source: spec
  description: Count, aggregate, and groupBy operations for analytics
  name: Prisma Aggregation API
  phrasing_intents:
  - id: count
    intent: Count records that match a filter
    question: How many rows in my User model match a given filter?
  - id: aggregate
    intent: Compute sums, averages, min and max on a model
    question: What's the average and total of a numeric column across my records?
  - id: groupBy
    intent: Group records and aggregate each group
    question: How do I group my orders by status and total each group?
  phrasing_ops: 3
  slug: prisma-aggregation-api
- baseURL: https://api.prisma.io/v1
  baseurl_source: declared
  description: Operations for managing API keys for platform resources
  name: Prisma API Keys API
  phrasing_intents:
  - id: listApiKeys
    intent: List API keys for an environment
    question: Which API keys exist for my production environment?
  - id: createApiKey
    intent: Create an API key for an environment
    question: How do I generate a new API key for an environment?
  - id: deleteApiKey
    intent: Revoke and delete an API key
    question: What happens to clients still using an API key after I delete it?
  phrasing_ops: 3
  slug: prisma-api-keys-api
- baseURL: https://localhost:3000/api
  baseurl_source: spec
  description: Batch operations for bulk create, update, and delete
  name: Prisma Batch API
  phrasing_intents:
  - id: createMany
    intent: Insert many records at once
    question: How do I insert many records in a single transaction?
  - id: updateMany
    intent: Update every record that matches a filter
    question: Can I update all records matching a filter in one request?
  - id: deleteMany
    intent: Delete every record that matches a filter
    question: What happens if I run a bulk delete without any filter?
  phrasing_ops: 3
  slug: prisma-batch-api
- baseURL: https://accelerate.prisma-data.net
  baseurl_source: declared
  description: Cache management and invalidation operations
  name: Prisma Cache API
  phrasing_intents:
  - id: invalidateCacheByTags
    intent: Invalidate cached queries by tag
    question: How do I invalidate Accelerate cached query results by tag?
  - id: invalidateAllCache
    intent: Clear the entire cache for an environment
    question: Can I clear the whole Accelerate cache for an environment at once?
  phrasing_ops: 2
  slug: prisma-cache-api
- baseURL: https://api.prisma.io/v1
  baseurl_source: declared
  description: Operations for managing database connection strings
  name: Prisma Connections API
  phrasing_intents:
  - id: getV1Connections
    intent: List connections I have access to
    question: Which database connections can my token see across all databases?
  - id: postV1Connections
    intent: Create a named connection for a database
    question: How do I create a named connection for a database with the v1 API?
  - id: getV1ConnectionsById
    intent: Get a connection by ID
    question: How do I look up one connection by its ID?
  - id: deleteV1ConnectionsById
    intent: Delete a connection
    question: Can I delete a connection by ID with the v1 API?
  - id: postV1ConnectionsByIdRotate
    intent: Rotate a connection's credentials
    question: How do I rotate credentials for a database connection?
  - id: listConnections
    intent: List a database's connection strings
    question: Where can I find the direct TCP connection details for a database?
  - id: createConnection
    intent: Generate a connection string for a database
    question: How do I generate a pooled connection string for a database?
  - id: deleteConnection
    intent: Revoke a database connection string
    question: Do clients lose database access as soon as a connection string is deleted?
  phrasing_ops: 8
  slug: prisma-connections-api
- baseURL: https://localhost:3000/api
  baseurl_source: spec
  description: Core create, read, update, and delete operations for database models
  name: Prisma CRUD API
  phrasing_intents:
  - id: findMany
    intent: Find records with filters, sorting and paging
    question: How do I query records with filters, sorting and pagination?
  - id: create
    intent: Create a new record
    question: How do I create a new record in a model?
  - id: findUnique
    intent: Get one record by its unique ID
    question: What's the way to fetch a single record by its ID?
  - id: update
    intent: Update a record by its ID
    question: Can I increment a numeric field atomically when updating a record?
  - id: deleteRecord
    intent: Delete one record by its ID
    question: Will deleting a record cascade to its related rows?
  - id: upsert
    intent: Create a record or update it if it exists
    question: Can I create a record only if it doesn't exist and update it otherwise?
  - id: findFirst
    intent: Get the first record that matches a filter
    question: Which call returns just the first record that matches a filter?
  phrasing_ops: 7
  slug: prisma-crud-api
- baseURL: https://api.prisma.io/v1
  baseurl_source: declared
  description: Operations for managing database backup and restore operations
  name: Prisma Database Backups API
  phrasing_intents:
  - id: getV1DatabasesByDatabaseIdBackups
    intent: List a database's backups (v1)
    question: Can I cap how many backups the v1 API returns for a database?
  - id: listDatabaseBackups
    intent: List automatic and manual backups
    question: How do I see all automatic and manual backups for a database with their size?
  - id: createDatabaseBackup
    intent: Take a manual database backup
    question: Can I trigger a manual backup of a database before a risky migration?
  - id: restoreDatabaseBackup
    intent: Restore a database from a backup
    question: What happens to current data when I restore a database from a backup?
  phrasing_ops: 4
  slug: prisma-database-backups-api
- baseURL: https://api.prisma.io/v1
  baseurl_source: declared
  description: Operations for retrieving database usage metrics and statistics
  name: Prisma Database Usage API
  phrasing_intents:
  - id: getV1DatabasesByDatabaseIdUsage
    intent: Get database usage metrics (v1)
    question: Can I pull usage metrics for a database through the v1 API?
  - id: getDatabaseUsage
    intent: Get storage, query and compute usage
    question: How much storage and compute is my database consuming?
  phrasing_ops: 2
  slug: prisma-database-usage-api
- baseURL: https://api.prisma.io/v1
  baseurl_source: declared
  description: Operations for provisioning and managing Prisma Postgres databases
  name: Prisma Databases API
  phrasing_intents:
  - id: getV1Databases
    intent: List databases my token can access
    question: Which databases can my token access across all projects?
  - id: postV1Databases
    intent: Create a database by passing its project
    question: Can I create a database and attach it to a git branch in one call?
  - id: getV1DatabasesByDatabaseId
    intent: Get a database by ID (v1)
    question: What does the v1 API return for a single database?
  - id: patchV1DatabasesByDatabaseId
    intent: Rename a database or move it to a branch
    question: Can I rename an existing database?
  - id: deleteV1DatabasesByDatabaseId
    intent: Delete a database (v1)
    question: Can I delete a database by ID with the v1 API?
  - id: postV1DatabasesByTargetDatabaseIdRestore
    intent: Overwrite a database with backup contents
    question: Are connections and credentials kept when I restore data into an existing database?
  - id: getV1ProjectsByProjectIdDatabases
    intent: List the databases in a project
    question: Which databases belong to one specific project?
  - id: postV1ProjectsByProjectIdDatabases
    intent: Create a database under a project path
    question: Can I create a new database in a project from an existing source?
  phrasing_ops: 11
  slug: prisma-databases-api
- baseURL: https://api.prisma.io/v1
  baseurl_source: declared
  description: Operations for managing project environments
  name: Prisma Environments API
  phrasing_intents:
  - id: listEnvironments
    intent: List a project's environments
    question: Which environments, like staging and production, does my project have?
  - id: createEnvironment
    intent: Create an environment in a project
    question: How do I add a staging environment to my project?
  - id: getEnvironment
    intent: Get an environment's configuration
    question: Can I check an environment's connection configuration and API key status?
  - id: deleteEnvironment
    intent: Delete an environment and its API keys
    question: Does deleting an environment also delete its API keys?
  phrasing_ops: 4
  slug: prisma-environments-api
- baseURL: https://pulse.prisma-data.net
  baseurl_source: declared
  description: Database change event retrieval and management
  name: Prisma Events API
  phrasing_intents:
  - id: getEvent
    intent: Get a database change event by ID
    question: Can I retrieve a specific database change event by its ULID?
  phrasing_ops: 1
  slug: prisma-events-api
- baseURL: https://accelerate.prisma-data.net
  baseurl_source: declared
  description: Service health and status checks
  name: Prisma Health API
  phrasing_intents:
  - id: getHealthStatus
    intent: Check Accelerate service health
    question: Is the Accelerate proxy service up right now?
  phrasing_ops: 1
  slug: prisma-health-api
- baseURL: https://api.prisma.io/v1
  baseurl_source: declared
  description: Operations for managing third-party integrations
  name: Prisma Integrations API
  phrasing_intents:
  - id: getV1Integrations
    intent: List integrations filtered by workspace
    question: Which integrations are connected to a workspace?
  - id: getV1IntegrationsById
    intent: Get an integration by ID
    question: What details are available for a single integration?
  - id: deleteV1IntegrationsById
    intent: Revoke an integration's tokens by ID
    question: Can I revoke an integration's tokens using its integration ID?
  - id: getV1WorkspacesByWorkspaceIdIntegrations
    intent: List a workspace's integrations
    question: What integrations does my workspace have, browsing from the workspace itself?
  - id: deleteV1WorkspacesByWorkspaceIdIntegrationsByClientId
    intent: Revoke integration tokens by client ID
    question: How do I revoke an integration's tokens when I only know its client ID?
  - id: listIntegrations
    intent: List configured third-party integrations
    question: Which third-party integrations are configured for my current project?
  phrasing_ops: 6
  slug: prisma-integrations-api
- baseURL: https://api.prisma.io/v1
  baseurl_source: declared
  description: Operations for managing workspace members and roles
  name: Prisma Members API
  phrasing_intents:
  - id: listWorkspaceMembers
    intent: List workspace members and roles
    question: Who are the members of my workspace and what roles do they have?
  phrasing_ops: 1
  slug: prisma-members-api
- baseURL: https://optimize.prisma-data.net
  baseurl_source: spec
  description: Performance metrics and statistics
  name: Prisma Metrics API
  phrasing_intents:
  - id: getSessionMetrics
    intent: Get performance metrics for a session
    question: What were the slowest queries in my Optimize recording session?
  phrasing_ops: 1
  slug: prisma-metrics-api
- baseURL: https://api.prisma.io/v1
  baseurl_source: declared
  description: Operations for managing projects within workspaces
  name: Prisma Projects API
  phrasing_intents:
  - id: listProjects
    intent: List projects in a workspace
    question: Which projects are in my workspace?
  - id: createProject
    intent: Create a project in a workspace
    question: How do I create a project inside a specific workspace?
  - id: getProject
    intent: Get a project with its environments
    question: Can I see a project's environments and database connections together?
  - id: deleteProject
    intent: Delete a project and its environments
    question: Does deleting a project remove all of its environments too?
  - id: getV1Projects
    intent: List projects my token can access
    question: Which projects can my token reach across workspaces?
  - id: postV1Projects
    intent: Create a project with a Postgres database
    question: How do I create a new project that comes with a Postgres database?
  - id: deleteV1ProjectsById
    intent: Delete a project (v1)
    question: Can I delete a project by ID through the v1 API?
  - id: getV1ProjectsById
    intent: Get a project by ID (v1)
    question: What does the v1 API return for one project?
  phrasing_ops: 10
  slug: prisma-projects-api
- baseURL: https://accelerate.prisma-data.net
  baseurl_source: declared
  description: Proxied database query operations routed through Accelerate with optional caching
  name: Prisma Queries API
  phrasing_intents:
  - id: executeQuery
    intent: Run a Prisma Client query through Accelerate
    question: How do I send a Prisma Client query through the Accelerate proxy?
  - id: listSessionQueries
    intent: List queries captured in a session
    question: Which queries were captured during my Optimize recording session?
  - id: getQueryDetails
    intent: Get SQL and execution plan for a query
    question: What SQL and execution plan did one recorded query produce?
  - id: ingestQueryData
    intent: Send query execution data to Optimize
    question: What endpoint does the Optimize extension report query data to?
  phrasing_ops: 4
  slug: prisma-queries-api
- baseURL: https://localhost:3000/api
  baseurl_source: spec
  description: Raw SQL query execution
  name: Prisma Raw API
  phrasing_intents:
  - id: queryRaw
    intent: Run a raw SQL SELECT query
    question: How do I run a raw SQL SELECT and get the rows back?
  - id: executeRaw
    intent: Execute a raw SQL write or DDL statement
    question: Can I run a raw INSERT, UPDATE, DELETE or DDL statement?
  phrasing_ops: 2
  slug: prisma-raw-api
- baseURL: https://optimize.prisma-data.net
  baseurl_source: spec
  description: AI-powered query optimization recommendations
  name: Prisma Recommendations API
  phrasing_intents:
  - id: listRecommendations
    intent: List query optimization recommendations
    question: What indexes or query changes does Optimize recommend for my session?
  phrasing_ops: 1
  slug: prisma-recommendations-api
- baseURL: https://optimize.prisma-data.net
  baseurl_source: spec
  description: Recording session management for query capture and analysis
  name: Prisma Sessions API
  phrasing_intents:
  - id: createSession
    intent: Start a query recording session
    question: How do I start recording Prisma Client queries for analysis?
  - id: listSessions
    intent: List Optimize recording sessions
    question: Which Optimize recording sessions exist in my environment?
  - id: getSession
    intent: Get a recording session's details
    question: What query statistics does a recording session have?
  - id: stopSession
    intent: Stop a recording session
    question: How do I stop capturing queries in a recording session?
  phrasing_ops: 4
  slug: prisma-sessions-api
- baseURL: https://pulse.prisma-data.net
  baseurl_source: declared
  description: Resumable event streams with at-least-once delivery and ordering guarantees. Requires event persistence to be enabled.
  name: Prisma Streams API
  phrasing_intents:
  - id: createStream
    intent: Create a resumable event stream for a model
    question: How do I create a resumable stream of change events for a model?
  - id: listStreams
    intent: List active named event streams
    question: Which named event streams are active in my environment?
  - id: consumeStreamEvents
    intent: Consume events from a named stream
    question: How do I read events from a named stream in order?
  - id: deleteStream
    intent: Delete a named event stream
    question: What happens to connected consumers when I delete a stream?
  phrasing_ops: 4
  slug: prisma-streams-api
- baseURL: https://pulse.prisma-data.net
  baseurl_source: declared
  description: Transient event subscriptions with at-most-once delivery. Missed events during downtime are not recovered.
  name: Prisma Subscriptions API
  phrasing_intents:
  - id: createSubscription
    intent: Subscribe to a model's change events
    question: Can I subscribe to live change events for a model without persistence?
  phrasing_ops: 1
  slug: prisma-subscriptions-api
- baseURL: https://api.prisma.io/v1
  baseurl_source: declared
  description: Operations for managing Prisma Data Platform workspaces
  name: Prisma Workspaces API
  phrasing_intents:
  - id: listWorkspaces
    intent: List all my workspaces
    question: Which workspaces do I have access to?
  - id: getWorkspace
    intent: Get a workspace's billing and projects
    question: What is the billing status of my workspace?
  - id: updateWorkspace
    intent: Rename a workspace
    question: How do I rename a workspace?
  - id: getV1Workspaces
    intent: List workspaces my token can access (v1)
    question: Which workspaces can my current token reach via the v1 API?
  - id: getV1WorkspacesById
    intent: Get a workspace by ID (v1)
    question: What does the v1 API return for one workspace?
  - id: getV1WorkspacesByIdSubscription
    intent: Get a workspace's subscription
    question: Which plan is my workspace subscribed to?
  phrasing_ops: 6
  slug: prisma-workspaces-api
- baseURL: https://api.prisma.io/v1
  baseurl_source: declared
  description: The Buckets API from Prisma — 4 operation(s) for buckets.
  name: Prisma Buckets API
  phrasing_intents:
  - id: getV1Buckets
    intent: List object-store buckets
    question: Which object-store buckets can my token access?
  - id: postV1Buckets
    intent: Create an object-store bucket
    question: How do I create an object storage bucket in a Prisma project?
  - id: getV1BucketsByBucketId
    intent: Get a bucket's details
    question: What details can I pull up for a single bucket by its ID?
  - id: deleteV1BucketsByBucketId
    intent: Delete a bucket and all its objects
    question: Does deleting a bucket also remove its objects and access keys?
  - id: getV1BucketsByBucketIdKeys
    intent: List a bucket's access keys
    question: Which access keys exist for a bucket?
  - id: postV1BucketsByBucketIdKeys
    intent: Create an access key for a bucket
    question: How do I create an access key for a bucket?
  - id: deleteV1BucketsByBucketIdKeysByKeyId
    intent: Revoke a bucket access key
    question: Can I revoke one bucket key without deleting the bucket?
  phrasing_ops: 7
  slug: prisma-buckets-api
- baseURL: https://api.prisma.io/v1
  baseurl_source: declared
  description: The Databases Connections API from Prisma — 1 operation(s) for databases connections.
  name: Prisma Databases Connections API
  phrasing_intents:
  - id: getV1DatabasesByDatabaseIdConnections
    intent: List a database's connections
    question: Which connections exist for one database?
  - id: postV1DatabasesByDatabaseIdConnections
    intent: Create a connection string for a database
    question: How do I create a new connection string for a database?
  phrasing_ops: 2
  slug: prisma-databases-connections-api
- baseURL: https://api.prisma.io/v1
  baseurl_source: declared
  description: Experimental endpoints are in active development and may change at any time without notice.
  name: Prisma [Experimental] API
  phrasing_intents:
  - id: getV1Apps
    intent: List apps (deprecated, use services)
    question: Which legacy apps does my token have access to?
  - id: postV1Apps
    intent: Create an app (deprecated, use services)
    question: Is creating an app still supported now that apps are deprecated?
  - id: getV1AppsByAppId
    intent: Get an app (deprecated)
    question: Can I still look up a legacy app and its promoted deployment?
  - id: patchV1AppsByAppId
    intent: Rename an app (deprecated)
    question: Can I rename a legacy app?
  - id: deleteV1AppsByAppId
    intent: Delete an app (deprecated)
    question: Are an app's deployments removed when I delete the legacy app?
  - id: postV1AppsByAppIdPromote
    intent: Promote a deployment on an app (deprecated)
    question: Can I still make a running deployment live on a legacy app?
  - id: postV1AppsByAppIdRollback
    intent: Roll an app back to a deployment (deprecated)
    question: Can I roll a legacy app back to an earlier deployment without downtime?
  - id: getV1AppsByAppIdDomains
    intent: List an app's custom domains (deprecated)
    question: Which custom domains are attached to my legacy app?
  phrasing_ops: 70
  slug: prisma-experimental-api
- baseURL: https://api.prisma.io/v1
  baseurl_source: declared
  description: The Misc API from Prisma — 3 operation(s) for misc.
  name: Prisma Misc API
  phrasing_intents:
  - id: getV1Me
    intent: Show who the current token belongs to
    question: Which user and workspace does my current token represent?
  - id: getV1RegionsPostgres
    intent: List Prisma Postgres regions
    question: Which regions can I host a Prisma Postgres database in?
  - id: getV1RegionsAccelerate
    intent: List Prisma Accelerate regions
    question: Which regions does Accelerate run in?
  phrasing_ops: 3
  slug: prisma-misc-api
- baseURL: https://api.prisma.io/v1
  baseurl_source: declared
  description: The Regions API from Prisma — 1 operation(s) for regions.
  name: Prisma Regions API
  phrasing_intents:
  - id: getV1Regions
    intent: List available regions across products
    question: Which regions are available across all Prisma products?
  phrasing_ops: 1
  slug: prisma-regions-api
- baseURL: https://api.prisma.io/v1
  baseurl_source: declared
  description: The Service Tokens API from Prisma — 2 operation(s) for service tokens.
  name: Prisma Service Tokens API
  phrasing_intents:
  - id: getV1WorkspacesByWorkspaceIdService-tokens
    intent: List a workspace's service tokens
    question: Which service tokens exist for my workspace?
  - id: postV1WorkspacesByWorkspaceIdService-tokens
    intent: Create a workspace service token
    question: How do I create a service token for CI in my workspace?
  - id: deleteV1WorkspacesByWorkspaceIdService-tokensByServiceTokenId
    intent: Revoke a workspace service token
    question: How do I revoke a service token that is no longer needed?
  phrasing_ops: 3
  slug: prisma-service-tokens-api
arazzos:
- description: Run a cached query through the Accelerate proxy, then invalidate the cache entries tagged by that query.
  name: Prisma Accelerate Cached Query then Invalidate
  slug: prisma-accelerate-query-and-invalidate-workflow
- description: Count records matching a filter, then fetch the first page of matching records ordered and paginated.
  name: Prisma Client List and Count Records
  slug: prisma-client-list-and-count-records-workflow
- description: Look up a record by its unique key, then upsert it so it is created when missing or updated when present.
  name: Prisma Client Upsert a Record
  slug: prisma-client-upsert-record-workflow
- description: Open a query recording session, pull the slowest captured queries and recommendations, then stop the session.
  name: Prisma Optimize Record and Analyze a Session
  slug: prisma-optimize-record-and-analyze-workflow
- description: Create a project, add an environment, and mint an API key for it in the Data Platform.
  name: Prisma Data Platform Bootstrap a Project Environment
  slug: prisma-platform-bootstrap-environment-workflow
- description: Mint a fresh API key for an environment and revoke the previous one in a single zero-gap rotation.
  name: Prisma Data Platform Rotate an Environment API Key
  slug: prisma-platform-rotate-api-key-workflow
- description: Confirm a project exists, provision an additional Postgres database in it, and mint a connection string.
  name: Prisma Postgres Add a Database to a Project
  slug: prisma-postgres-add-database-to-project-workflow
- description: Take a manual database backup, poll until it completes, then restore the database from it.
  name: Prisma Postgres Backup and Restore
  slug: prisma-postgres-backup-and-restore-workflow
- description: Locate a project by name within a workspace and permanently delete it when found.
  name: Prisma Postgres Find and Delete a Project
  slug: prisma-postgres-find-and-delete-project-workflow
- description: Create a project with a managed Postgres database, take a first backup, and mint a connection string.
  name: Prisma Postgres Provision a Project
  slug: prisma-postgres-provision-project-workflow
- description: Confirm a database is active, mint a fresh connection string, then revoke the previous one.
  name: Prisma Postgres Rotate a Database Connection String
  slug: prisma-postgres-rotate-connection-workflow
- description: Create a resumable named event stream, read its cursor position, and fetch the last persisted event by ULID.
  name: Prisma Pulse Create and Resume a Named Stream
  slug: prisma-pulse-named-stream-resume-workflow
artifact_total: 158
collections:
- collection_type: postman
  name: Prisma Accelerate API
  slug: postman-prisma-accelerate
- collection_type: postman
  name: Prisma Client API
  slug: postman-prisma-client
- collection_type: postman
  name: Prisma Data Platform API
  slug: postman-prisma-data-platform
- collection_type: postman
  name: Prisma Optimize API
  slug: postman-prisma-optimize
- collection_type: postman
  name: Prisma Postgres Management API
  slug: postman-prisma-postgres-management
- collection_type: postman
  name: Prisma Pulse API
  slug: postman-prisma-pulse
- collection_type: open
  name: Prisma Accelerate API
  slug: open-prisma-accelerate
- collection_type: open
  name: Prisma Accelerate Aggregation API
  slug: open-prisma-aggregation-api
- collection_type: open
  name: Prisma Accelerate Aggregation API Keys API
  slug: open-prisma-api-keys-api
- collection_type: open
  name: Prisma Accelerate Aggregation Batch API
  slug: open-prisma-batch-api
- collection_type: open
  name: Prisma Accelerate Aggregation Cache API
  slug: open-prisma-cache-api
- collection_type: open
  name: Prisma Client API
  slug: open-prisma-client
- collection_type: open
  name: Prisma Accelerate Aggregation Connections API
  slug: open-prisma-connections-api
- collection_type: open
  name: Prisma Accelerate Aggregation CRUD API
  slug: open-prisma-crud-api
- collection_type: open
  name: Prisma Data Platform API
  slug: open-prisma-data-platform
- collection_type: open
  name: Prisma Accelerate Aggregation Database Backups API
  slug: open-prisma-database-backups-api
- collection_type: open
  name: Prisma Accelerate Aggregation Database Usage API
  slug: open-prisma-database-usage-api
- collection_type: open
  name: Prisma Accelerate Aggregation Databases API
  slug: open-prisma-databases-api
- collection_type: open
  name: Prisma Accelerate Aggregation Environments API
  slug: open-prisma-environments-api
- collection_type: open
  name: Prisma Accelerate Aggregation Events API
  slug: open-prisma-events-api
- collection_type: open
  name: Prisma Accelerate Aggregation Health API
  slug: open-prisma-health-api
- collection_type: open
  name: Prisma Accelerate Aggregation Integrations API
  slug: open-prisma-integrations-api
- collection_type: open
  name: Prisma Accelerate Aggregation Members API
  slug: open-prisma-members-api
- collection_type: open
  name: Prisma Accelerate Aggregation Metrics API
  slug: open-prisma-metrics-api
- collection_type: open
  name: Prisma Optimize API
  slug: open-prisma-optimize
- collection_type: open
  name: Prisma Postgres Management API
  slug: open-prisma-postgres-management
- collection_type: open
  name: Prisma Accelerate Aggregation Projects API
  slug: open-prisma-projects-api
- collection_type: open
  name: Prisma Pulse API
  slug: open-prisma-pulse
- collection_type: open
  name: Prisma Accelerate Aggregation Queries API
  slug: open-prisma-queries-api
- collection_type: open
  name: Prisma Accelerate Aggregation Raw API
  slug: open-prisma-raw-api
- collection_type: open
  name: Prisma Accelerate Aggregation Recommendations API
  slug: open-prisma-recommendations-api
- collection_type: open
  name: Prisma Accelerate Aggregation Sessions API
  slug: open-prisma-sessions-api
- collection_type: open
  name: Prisma Accelerate Aggregation Streams API
  slug: open-prisma-streams-api
- collection_type: open
  name: Prisma Accelerate Aggregation Subscriptions API
  slug: open-prisma-subscriptions-api
- collection_type: open
  name: Prisma Accelerate Aggregation Workspaces API
  slug: open-prisma-workspaces-api
common:
- group: commercial
  href: https://artifacts.apis.io/prisma/finops/prisma-finops.yml
  title: ''
  type: FinOps
  url: finops/prisma-finops.yml
- group: other
  href: https://artifacts.apis.io/prisma/capabilities/prisma-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/prisma-capability-edges.yml
- group: auth
  href: https://artifacts.apis.io/prisma/scopes/prisma-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/prisma-scopes.yml
- group: agent
  href: https://artifacts.apis.io/prisma/agentic-access/prisma-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/prisma-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/prisma/security/prisma-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/prisma-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/prisma/security/prisma-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/prisma-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/prisma/authentication/prisma-authentication.yml
  title: ''
  type: Authentication
  url: authentication/prisma-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/prisma/overview
- group: design
  href: https://artifacts.apis.io/prisma/arazzo/prisma-accelerate-query-and-invalidate-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/prisma-accelerate-query-and-invalidate-workflow.yml
- group: design
  href: https://artifacts.apis.io/prisma/arazzo/prisma-client-list-and-count-records-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/prisma-client-list-and-count-records-workflow.yml
- group: design
  href: https://artifacts.apis.io/prisma/arazzo/prisma-client-upsert-record-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/prisma-client-upsert-record-workflow.yml
- group: design
  href: https://artifacts.apis.io/prisma/arazzo/prisma-optimize-record-and-analyze-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/prisma-optimize-record-and-analyze-workflow.yml
- group: design
  href: https://artifacts.apis.io/prisma/arazzo/prisma-platform-bootstrap-environment-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/prisma-platform-bootstrap-environment-workflow.yml
- group: design
  href: https://artifacts.apis.io/prisma/arazzo/prisma-platform-rotate-api-key-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/prisma-platform-rotate-api-key-workflow.yml
- group: design
  href: https://artifacts.apis.io/prisma/arazzo/prisma-postgres-add-database-to-project-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/prisma-postgres-add-database-to-project-workflow.yml
- group: design
  href: https://artifacts.apis.io/prisma/arazzo/prisma-postgres-backup-and-restore-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/prisma-postgres-backup-and-restore-workflow.yml
- group: design
  href: https://artifacts.apis.io/prisma/arazzo/prisma-postgres-find-and-delete-project-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/prisma-postgres-find-and-delete-project-workflow.yml
- group: design
  href: https://artifacts.apis.io/prisma/arazzo/prisma-postgres-provision-project-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/prisma-postgres-provision-project-workflow.yml
- group: design
  href: https://artifacts.apis.io/prisma/arazzo/prisma-postgres-rotate-connection-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/prisma-postgres-rotate-connection-workflow.yml
- group: design
  href: https://artifacts.apis.io/prisma/arazzo/prisma-pulse-named-stream-resume-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/prisma-pulse-named-stream-resume-workflow.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/prisma-io
- group: start
  title: ''
  type: Portal
  url: https://console.prisma.io/login
- group: docs
  title: ''
  type: Documentation
  url: https://www.prisma.io/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://www.prisma.io/docs/getting-started
- group: auth
  title: ''
  type: Authentication
  url: https://www.prisma.io/docs/rest-api/authentication
- group: company
  title: ''
  type: Blog
  url: https://www.prisma.io/blog
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.prisma.io/changelog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/prisma
- group: operate
  title: ''
  type: Community
  url: https://www.prisma.io/community
- group: operate
  title: ''
  type: Discord
  url: https://pris.ly/discord
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/prisma
- group: commercial
  title: ''
  type: Pricing
  url: https://www.prisma.io/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://www.prisma-status.com
- group: operate
  title: ''
  type: Support
  url: https://www.prisma.io/support
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.prisma.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.prisma.io/privacy
- group: company
  title: ''
  type: Website
  url: https://www.prisma.io
- group: start
  title: ''
  type: Login
  url: https://console.prisma.io/login
- group: start
  title: ''
  type: Signup
  url: https://console.prisma.io/sign-up
- group: design
  href: https://artifacts.apis.io/prisma/json-ld/prisma-context.jsonld
  title: ''
  type: JSONLDContext
  url: json-ld/prisma-context.jsonld
- group: docs
  href: https://artifacts.apis.io/prisma/json-schema/prisma-workspace-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/prisma-workspace-schema.json
- group: docs
  href: https://artifacts.apis.io/prisma/json-schema/prisma-project-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/prisma-project-schema.json
- group: docs
  href: https://artifacts.apis.io/prisma/json-schema/prisma-database-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/prisma-database-schema.json
- group: docs
  href: https://artifacts.apis.io/prisma/json-schema/prisma-cache-strategy-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/prisma-cache-strategy-schema.json
- group: docs
  href: https://artifacts.apis.io/prisma/json-schema/prisma-pulse-event-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/prisma-pulse-event-schema.json
- group: docs
  href: https://artifacts.apis.io/prisma/json-schema/prisma-query-recommendation-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/prisma-query-recommendation-schema.json
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/prisma/mcp
- group: agent
  title: ''
  type: AgentSkill
  url: https://github.com/prisma/skills
- group: build
  href: https://artifacts.apis.io/prisma/packages/prisma-packages.yml
  title: ''
  type: Packages
  url: packages/prisma-packages.yml
- group: build
  href: https://artifacts.apis.io/prisma/packages/prisma-packages.yml
  title: ''
  type: SDKs
  url: packages/prisma-packages.yml
- group: agent
  href: https://artifacts.apis.io/prisma/well-known/prisma-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/prisma-well-known.yml
- group: auth
  href: https://artifacts.apis.io/prisma/well-known/prisma-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/prisma-security.txt
- group: auth
  href: https://artifacts.apis.io/prisma/security/prisma-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/prisma-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/prisma/security/prisma-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/prisma-trust-center.yml
- group: auth
  title: ''
  type: Trust
  url: https://trust.prisma.io
- group: agent
  href: https://artifacts.apis.io/prisma/mcp/prisma-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/prisma-mcp.yml
- group: build
  href: https://artifacts.apis.io/prisma/mcp/prisma-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/prisma-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/prisma/llms/prisma-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/prisma-llms.txt
- group: other
  href: https://artifacts.apis.io/prisma/overlays/prisma-postgres-management-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/prisma-postgres-management-api-overlay.yaml
- group: design
  href: https://artifacts.apis.io/prisma/conformance/prisma-conformance.yml
  title: ''
  type: Conformance
  url: conformance/prisma-conformance.yml
- group: auth
  href: https://artifacts.apis.io/prisma/conformance/prisma-conformance.yml
  title: ''
  type: Compliance
  url: conformance/prisma-conformance.yml
- group: design
  href: https://artifacts.apis.io/prisma/errors/prisma-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/prisma-problem-types.yml
- group: design
  href: https://artifacts.apis.io/prisma/errors/prisma-error-codes.yml
  title: ''
  type: ErrorCodes
  url: errors/prisma-error-codes.yml
- group: design
  href: https://artifacts.apis.io/prisma/lifecycle/prisma-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/prisma-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/prisma/conventions/prisma-conventions.yml
  title: ''
  type: Conventions
  url: conventions/prisma-conventions.yml
- group: design
  href: https://artifacts.apis.io/prisma/conventions/prisma-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/prisma-conventions.yml
- group: operate
  href: https://artifacts.apis.io/prisma/changelog/prisma-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/prisma-changelog.yml
- group: build
  href: https://artifacts.apis.io/prisma/cli/prisma-cli.yml
  title: ''
  type: CLI
  url: cli/prisma-cli.yml
- group: design
  href: https://artifacts.apis.io/prisma/components/prisma-components.yml
  title: ''
  type: Components
  url: components/prisma-components.yml
- group: design
  href: https://artifacts.apis.io/prisma/data-model/prisma-data-model.yml
  title: ''
  type: DataModel
  url: data-model/prisma-data-model.yml
- group: agent
  href: https://artifacts.apis.io/prisma/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  href: https://artifacts.apis.io/prisma/plans/prisma-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/prisma-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/prisma/rate-limits/prisma-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/prisma-rate-limits.yml
- group: start
  title: ''
  type: Console
  url: https://console.prisma.io
- group: docs
  title: ''
  type: APIReference
  url: https://www.prisma.io/docs/rest-api
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.prisma.io/docs
- group: start
  title: ''
  type: Quickstart
  url: https://www.prisma.io/docs/getting-started
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.prisma.io/support
created: '2024-01-01'
description: Prisma gives TypeScript and Node.js teams a type-safe ORM, managed serverless Postgres, and Compute for deploying apps and AI agents next to their database. The product line is Prisma ORM, Prisma Postgres, Prisma Compute, Prisma Composer, Prisma Studio, Object Store buckets and Query Insights, wired together by one CLI, a REST Management API at api.prisma.io/v1, and a hosted MCP server at mcp.prisma.io. Accelerate, Pulse and Optimize have left the advertised line.
finops:
- has_sources: true
  method: derived
  name: Prisma Finops
  primary_unit: subscription
  service_category: ''
  slug: prisma-finops
  template: false
image: https://www.prisma.io/images/prisma-logo.svg
json_schemas:
- name: AccelerateError
  property_count: 3
  slug: prisma-accelerateerror
- name: AccelerateInfo
  property_count: 5
  slug: prisma-accelerateinfo
- name: AggregateResult
  property_count: 5
  slug: prisma-aggregateresult
- name: ApiKey
  property_count: 5
  slug: prisma-apikey
- name: ApiKeyCreate
  property_count: 1
  slug: prisma-apikeycreate
- name: ApiKeyWithValue
  property_count: 1
  slug: prisma-apikeywithvalue
- name: BackupCreate
  property_count: 1
  slug: prisma-backupcreate
- name: BatchPayload
  property_count: 1
  slug: prisma-batchpayload
- name: Prisma Accelerate Cache Strategy
  property_count: 3
  slug: prisma-cache-strategy
- name: CacheInvalidationRequest
  property_count: 1
  slug: prisma-cacheinvalidationrequest
- name: CacheInvalidationResponse
  property_count: 2
  slug: prisma-cacheinvalidationresponse
- name: CacheStrategy
  property_count: 3
  slug: prisma-cachestrategy
- name: Connection
  property_count: 5
  slug: prisma-connection
- name: ConnectionCreate
  property_count: 2
  slug: prisma-connectioncreate
- name: ConnectionWithCredentials
  property_count: 1
  slug: prisma-connectionwithcredentials
- name: CreateInput
  property_count: 3
  slug: prisma-createinput
- name: CreateManyInput
  property_count: 2
  slug: prisma-createmanyinput
- name: Prisma Postgres Database
  property_count: 14
  slug: prisma-database
- name: DatabaseApiKey
  property_count: 2
  slug: prisma-databaseapikey
- name: DatabaseBackup
  property_count: 7
  slug: prisma-databasebackup
- name: DatabaseCreate
  property_count: 2
  slug: prisma-databasecreate
- name: DatabaseUsage
  property_count: 5
  slug: prisma-databaseusage
- name: DirectConnection
  property_count: 5
  slug: prisma-directconnection
- name: Environment
  property_count: 6
  slug: prisma-environment
- name: EnvironmentCreate
  property_count: 2
  slug: prisma-environmentcreate
- name: Error
  property_count: 1
  slug: prisma-error
- name: EventFilter
  property_count: 3
  slug: prisma-eventfilter
- name: GroupByResult
  property_count: 0
  slug: prisma-groupbyresult
- name: HealthStatus
  property_count: 3
  slug: prisma-healthstatus
- name: Integration
  property_count: 5
  slug: prisma-integration
- name: PrismaError
  property_count: 3
  slug: prisma-prismaerror
- name: Prisma Project
  property_count: 7
  slug: prisma-project
- name: ProjectCreate
  property_count: 1
  slug: prisma-projectcreate
- name: ProjectWithDatabase
  property_count: 1
  slug: prisma-projectwithdatabase
- name: Prisma Pulse Database Event
  property_count: 0
  slug: prisma-pulse-event
- name: PulseCreateEvent
  property_count: 2
  slug: prisma-pulsecreateevent
- name: PulseDeleteEvent
  property_count: 2
  slug: prisma-pulsedeleteevent
- name: PulseError
  property_count: 3
  slug: prisma-pulseerror
- name: PulseEvent
  property_count: 3
  slug: prisma-pulseevent
- name: PulseUpdateEvent
  property_count: 3
  slug: prisma-pulseupdateevent
- name: Prisma Optimize Query Recommendation
  property_count: 9
  slug: prisma-query-recommendation
- name: QueryIngestPayload
  property_count: 2
  slug: prisma-queryingestpayload
- name: QueryRequest
  property_count: 3
  slug: prisma-queryrequest
- name: QueryResponse
  property_count: 3
  slug: prisma-queryresponse
- name: RawQueryInput
  property_count: 2
  slug: prisma-rawqueryinput
- name: Recommendation
  property_count: 8
  slug: prisma-recommendation
- name: Record
  property_count: 0
  slug: prisma-record
- name: RecordedQuery
  property_count: 8
  slug: prisma-recordedquery
- name: Session
  property_count: 8
  slug: prisma-session
- name: SessionCreate
  property_count: 2
  slug: prisma-sessioncreate
- name: SessionMetrics
  property_count: 9
  slug: prisma-sessionmetrics
- name: StreamCreateRequest
  property_count: 3
  slug: prisma-streamcreaterequest
- name: StreamInfo
  property_count: 5
  slug: prisma-streaminfo
- name: SubscriptionRequest
  property_count: 2
  slug: prisma-subscriptionrequest
- name: UpdateInput
  property_count: 3
  slug: prisma-updateinput
- name: UpdateManyInput
  property_count: 2
  slug: prisma-updatemanyinput
- name: UpsertInput
  property_count: 5
  slug: prisma-upsertinput
- name: Prisma Workspace
  property_count: 7
  slug: prisma-workspace
- name: WorkspaceMember
  property_count: 6
  slug: prisma-workspacemember
- name: WorkspaceUpdate
  property_count: 1
  slug: prisma-workspaceupdate
json_structures:
- name: Prisma Structure
  property_count: 0
  slug: prisma-structure
jsonld:
- class_count: 6
  name: Prisma Context
  property_count: 16
  slug: prisma-context
layout: provider
mcp_servers:
- description: ''
  name: MCP server (provider repository)
  slug: mcp-server-provider-repository
- description: Remote MCP server at mcp.prisma.io over streamable HTTP requiring OAuth; 19 tools listed.
  name: Prisma MCP Server
  slug: prisma
modified: '2026-09-17'
name: Prisma
nav: Providers
network: true
overview: 'Prisma publishes 29 API contracts indexed on the [APIs.io](https://apis.io/) network, including Aggregation API, API Keys API, Batch API, and 26 more. Tagged areas include Database, PostgreSQL, ORM, Developer Tools, and Application Hosting.


  The Prisma catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Prisma''s developer surface includes authentication, developer portal, documentation, getting-started guide, engineering blog, changelog, pricing, and 71 more developer resources.'
plans:
- name: Prisma Plans Pricing
  plan_count: 5
  slug: prisma-plans-pricing
- name: Prisma Price Estimates
  plan_count: 0
  slug: prisma-price-estimates
random_paper: 4
rate_limits:
- limit_count: 0
  name: Prisma Rate Limits
  slug: prisma-rate-limits
rules:
- authorship: generated
  effective_rule_count: 6
  extends: []
  name: Prisma — jsonschema rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: prisma-jsonschema-spectral-rules
scopes:
- name: Prisma Scopes
  scope_count: 2
  slug: prisma-scopes
  summary_line: 2 scopes · authorizationCode
score:
  band: exemplar
  composite: 73.6
  coverage:
    artifact_dirs: 40
    catalog_earned: 59.3
    catalog_earned_first_party: 12.0
    catalog_gap: 55.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.3
  facets:
    access_clarity: 86.8
    contract_governance: 28.0
    contract_quality: 60.4
    developer_ergonomics: 89.3
    discoverability: 70.0
    operational_transparency: 44.7
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - germany
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 73.3
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 76.0
      derived: 0
      marker_coverage: 20.7
      total: 29
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
    score: 33.3
screenshot: https://apis.io/screenshots/prisma/prisma-2026-08-17T124858.png
security:
- kind: authentication
  name: Prisma Authentication
  slug: prisma-authentication
  summary_line: apiKey/http/oauth2 · 3 schemes
- kind: domain-security
  name: Prisma Domain Security
  slug: prisma-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Prisma Vulnerability Disclosure
  slug: prisma-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Prisma Trust Center
  slug: prisma-trust-center
  summary_line: trust center published
skill_count: 7
skills:
- name: prisma-cli
  slug: prisma-cli
- name: prisma-client-api
  slug: prisma-client-api
- name: prisma-database-setup
  slug: prisma-database-setup
- name: prisma-driver-adapter-implementation
  slug: prisma-driver-adapter-implementation
- name: prisma-postgres-setup
  slug: prisma-postgres-setup
- name: prisma-postgres
  slug: prisma-postgres
- name: prisma-upgrade-v7
  slug: prisma-upgrade-v7
slug: prisma
tags:
- Database
- PostgreSQL
- ORM
- Developer Tools
- Application Hosting
- Serverless
- Object Storage
- TypeScript
- MCP
- AI Agents
- Provisioning
- Data Platform
website: https://www.prisma.io
---
