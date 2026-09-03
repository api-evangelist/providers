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
    agent_skills: true
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
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.8
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 33
  human_in_the_loop: 1
  name: Prisma Agentic Access
  operation_count: 67
  slug: prisma-agentic-access
  summary_line: 67 operations · 33 acting · 1 human-in-the-loop
api_count: 6
apis:
- baseURL: https://localhost:3000/api
  baseurl_source: spec
  description: Count, aggregate, and groupBy operations for analytics
  name: Prisma Aggregation API
  slug: prisma-aggregation-api
- baseURL: https://api.cloud.prisma.io
  baseurl_source: spec
  description: Operations for managing API keys for platform resources
  name: Prisma API Keys API
  slug: prisma-api-keys-api
- baseURL: https://localhost:3000/api
  baseurl_source: spec
  description: Batch operations for bulk create, update, and delete
  name: Prisma Batch API
  slug: prisma-batch-api
- baseURL: https://accelerate.prisma-data.net
  baseurl_source: spec
  description: Cache management and invalidation operations
  name: Prisma Cache API
  slug: prisma-cache-api
- baseURL: https://api.prisma.io/v1
  baseurl_source: spec
  description: Operations for managing database connection strings
  name: Prisma Connections API
  slug: prisma-connections-api
- baseURL: https://localhost:3000/api
  baseurl_source: spec
  description: Core create, read, update, and delete operations for database models
  name: Prisma CRUD API
  slug: prisma-crud-api
- baseURL: https://api.prisma.io/v1
  baseurl_source: spec
  description: Operations for managing database backup and restore operations
  name: Prisma Database Backups API
  slug: prisma-database-backups-api
- baseURL: https://api.prisma.io/v1
  baseurl_source: spec
  description: Operations for retrieving database usage metrics and statistics
  name: Prisma Database Usage API
  slug: prisma-database-usage-api
- baseURL: https://api.prisma.io/v1
  baseurl_source: spec
  description: Operations for provisioning and managing Prisma Postgres databases
  name: Prisma Databases API
  slug: prisma-databases-api
- baseURL: https://api.cloud.prisma.io
  baseurl_source: spec
  description: Operations for managing project environments
  name: Prisma Environments API
  slug: prisma-environments-api
- baseURL: https://pulse.prisma-data.net
  baseurl_source: spec
  description: Database change event retrieval and management
  name: Prisma Events API
  slug: prisma-events-api
- baseURL: https://accelerate.prisma-data.net
  baseurl_source: spec
  description: Service health and status checks
  name: Prisma Health API
  slug: prisma-health-api
- baseURL: https://api.prisma.io/v1
  baseurl_source: spec
  description: Operations for managing third-party integrations
  name: Prisma Integrations API
  slug: prisma-integrations-api
- baseURL: https://api.cloud.prisma.io
  baseurl_source: spec
  description: Operations for managing workspace members and roles
  name: Prisma Members API
  slug: prisma-members-api
- baseURL: https://optimize.prisma-data.net
  baseurl_source: spec
  description: Performance metrics and statistics
  name: Prisma Metrics API
  slug: prisma-metrics-api
- baseURL: https://api.cloud.prisma.io
  baseurl_source: spec
  description: Operations for managing projects within workspaces
  name: Prisma Projects API
  slug: prisma-projects-api
- baseURL: https://accelerate.prisma-data.net
  baseurl_source: spec
  description: Proxied database query operations routed through Accelerate with optional caching
  name: Prisma Queries API
  slug: prisma-queries-api
- baseURL: https://localhost:3000/api
  baseurl_source: spec
  description: Raw SQL query execution
  name: Prisma Raw API
  slug: prisma-raw-api
- baseURL: https://optimize.prisma-data.net
  baseurl_source: spec
  description: AI-powered query optimization recommendations
  name: Prisma Recommendations API
  slug: prisma-recommendations-api
- baseURL: https://optimize.prisma-data.net
  baseurl_source: spec
  description: Recording session management for query capture and analysis
  name: Prisma Sessions API
  slug: prisma-sessions-api
- baseURL: https://pulse.prisma-data.net
  baseurl_source: spec
  description: Resumable event streams with at-least-once delivery and ordering guarantees. Requires event persistence to be enabled.
  name: Prisma Streams API
  slug: prisma-streams-api
- baseURL: https://pulse.prisma-data.net
  baseurl_source: spec
  description: Transient event subscriptions with at-most-once delivery. Missed events during downtime are not recovered.
  name: Prisma Subscriptions API
  slug: prisma-subscriptions-api
- baseURL: https://api.cloud.prisma.io
  baseurl_source: spec
  description: Operations for managing Prisma Data Platform workspaces
  name: Prisma Workspaces API
  slug: prisma-workspaces-api
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
artifact_total: 149
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
  name: API Collection
  slug: open-.refine-report
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
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/prisma-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/prisma-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/prisma-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/prisma-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/prisma/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/prisma-accelerate-query-and-invalidate-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/prisma-client-list-and-count-records-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/prisma-client-upsert-record-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/prisma-optimize-record-and-analyze-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/prisma-platform-bootstrap-environment-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/prisma-platform-rotate-api-key-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/prisma-postgres-add-database-to-project-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/prisma-postgres-backup-and-restore-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/prisma-postgres-find-and-delete-project-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/prisma-postgres-provision-project-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/prisma-postgres-rotate-connection-workflow.yml
- group: design
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
  url: https://www.prisma.io/docs/management-api/authentication
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
  title: ''
  type: JSONLDContext
  url: json-ld/prisma-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/prisma-workspace-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/prisma-project-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/prisma-database-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/prisma-cache-strategy-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/prisma-pulse-event-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/prisma-query-recommendation-schema.json
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/prisma/mcp
- group: agent
  title: ''
  type: AgentSkills
  url: https://github.com/prisma/skills
created: '2024'
description: Prisma is a next-generation ORM that helps developers build applications faster and with fewer errors. It provides a type-safe database client, migrations system, and visual database browser.
finops:
- name: Prisma Finops
  service_category: Database + Developer Tools
  slug: prisma-finops
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
  property_count: 0
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
  property_count: 0
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
  property_count: 0
  slug: prisma-projectwithdatabase
- name: Prisma Pulse Database Event
  property_count: 0
  slug: prisma-pulse-event
- name: PulseCreateEvent
  property_count: 0
  slug: prisma-pulsecreateevent
- name: PulseDeleteEvent
  property_count: 0
  slug: prisma-pulsedeleteevent
- name: PulseError
  property_count: 3
  slug: prisma-pulseerror
- name: PulseEvent
  property_count: 3
  slug: prisma-pulseevent
- name: PulseUpdateEvent
  property_count: 0
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
  name: MCP Server
  slug: mcp-server
modified: '2026-05-19'
name: Prisma
nav: Providers
network: true
overview: 'Prisma publishes 23 APIs on the [APIs.io](https://apis.io/) network, including Aggregation API, API Keys API, Batch API, and 20 more.


  The Prisma catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Prisma''s developer surface includes authentication, developer portal, documentation, getting-started guide, engineering blog, changelog, pricing, and 38 more developer resources.'
plans:
- name: Prisma Plans Pricing
  plan_count: 5
  slug: prisma-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 3
  name: Prisma Rate Limits
  slug: prisma-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: Prisma API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: prisma-jsonschema-spectral-rules
score:
  band: developing
  composite: 53.0
  coverage:
    artifact_dirs: 19
    catalog_gap: 74.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 9.8
    contract_quality: 63.3
    developer_ergonomics: 85.7
    discoverability: 38.9
    governance: 9.8
    operational_transparency: 42.1
  previous_composite: 53.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 82.6
      derived: 0
      marker_coverage: 0.0
      total: 23
  regulatory:
    note: provider declares no identity tags; regime could not be determined
    undetermined: true
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/prisma/refs/heads/main/screenshots/prisma-2026-08-17T124858.png
security:
- kind: authentication
  name: Prisma Authentication
  slug: prisma-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Prisma Domain Security
  slug: prisma-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Prisma Vulnerability Disclosure
  slug: prisma-vulnerability-disclosure
  summary_line: security.txt · contact published
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
website: https://www.prisma.io
---
