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
    error_semantics: verified
    event_surface_described: true
    idempotency: documented
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 67.3
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 43
  human_in_the_loop: 1
  name: Cdata Agentic Access
  operation_count: 76
  slug: cdata-agentic-access
  summary_line: 76 operations · 43 acting · 1 human-in-the-loop
api_count: 7
apis:
- baseURL: https://mcp.cloud.cdata.com
  baseurl_source: declared
  description: 'A hosted, remote Model Context Protocol server that exposes every data source connected to a CData Connect AI account as MCP tools — catalog, schema, table, column and stored procedure discovery plus '
  name: CData Connect AI MCP Server
  phrasing_intents:
  - id: postMcp
    intent: Send an MCP request across all my connections
    question: How do I talk to the CData Connect AI MCP server from my own model-aware client?
  - id: postMcpConnectionsByConnectionId
    intent: Send an MCP request scoped to one connection
    question: Can I restrict an MCP session to a single data connection?
  phrasing_ops: 2
  slug: mcp
- baseURL: https://cloud.cdata.com/api
  baseurl_source: declared
  description: The Account API from CData — 5 operation(s) for account.
  name: CData Account API
  phrasing_intents:
  - id: listAccounts
    intent: List sub-accounts under the parent account
    question: How do I see every sub-account under my Connect AI Embed parent account?
  - id: getAccount
    intent: Look up one sub-account by Id or external Id
    question: Can I look up a sub-account using my own external Id instead of the Connect AI Id?
  - id: createAccount
    intent: Create a sub-account for an embedded customer
    question: How do I provision a new sub-account for a customer in Connect AI Embed?
  - id: updateAccount
    intent: Rename or re-key an existing sub-account
    question: How do I rename a sub-account after it has been created?
  - id: deleteAccount
    intent: Delete a sub-account
    question: How do I remove a customer's sub-account from Connect AI Embed?
  phrasing_ops: 5
  slug: cdata-account-api
- baseURL: https://cloud.cdata.com/api
  baseurl_source: declared
  description: The Cache API from CData — 2 operation(s) for cache.
  name: CData Cache API
  phrasing_intents:
  - id: updateCacheConnection
    intent: Set the PostgreSQL cache connection
    question: How do I point Connect AI caching at my own PostgreSQL database?
  - id: generateCacheConnectionURL
    intent: Get a form link for a user to set their cache DB
    question: Can I send a user to a hosted page where they enter their own PostgreSQL cache details?
  phrasing_ops: 2
  slug: cdata-cache-api
- baseURL: https://cloud.cdata.com/api
  baseurl_source: declared
  description: The Connection API from CData — 6 operation(s) for connection.
  name: CData Connection API
  phrasing_intents:
  - id: createConnection
    intent: Start the add-connection flow for a customer
    question: How do I send a customer to connect their Salesforce or Snowflake data through Connect AI Embed?
  - id: listConnections
    intent: List a sub-account's data connections
    question: Which data connections has this sub-account already set up?
  - id: listDataSources
    intent: List the data sources Connect AI Embed supports
    question: What data sources and connectors does Connect AI Embed support?
  - id: editConnection
    intent: Get a link for a user to edit an existing connection
    question: How do I let a customer fix the credentials on a connection they already created?
  - id: deleteConnection
    intent: Delete a sub-account's connection
    question: How do I permanently remove a data connection a customer no longer uses?
  - id: clearConnectionMetadata
    intent: Clear a connection's metadata cache
    question: A connection is loading slowly or showing stale tables, can I reset its metadata cache?
  phrasing_ops: 6
  slug: cdata-connection-api
- baseURL: https://cloud.cdata.com/api
  baseurl_source: declared
  description: The Data Explorer API from CData — 1 operation(s) for data explorer.
  name: CData Data Explorer API
  phrasing_intents:
  - id: generateDataExplorerURL
    intent: Get a link to the Data Explorer page
    question: How do I send a user into the Connect AI Data Explorer to browse their data?
  phrasing_ops: 1
  slug: cdata-data-explorer-api
- baseURL: https://cloud.cdata.com/api
  baseurl_source: declared
  description: The Job API from CData — 7 operation(s) for job.
  name: CData Job API
  phrasing_intents:
  - id: listJobs
    intent: List a sub-account's jobs
    question: Which caching jobs are set up for this sub-account?
  - id: getJob
    intent: Get the details of a job
    question: How do I check the schedule and settings of one specific job?
  - id: createJob
    intent: Create a scheduled caching job
    question: How do I schedule a caching job that runs every few hours?
  - id: updateJob
    intent: Change an existing job's schedule or settings
    question: How do I change how often an existing caching job runs?
  - id: deleteJob
    intent: Delete a job
    question: How do I permanently remove a caching job I no longer need?
  - id: runJob
    intent: Queue a job to run now
    question: Can I trigger a caching job immediately instead of waiting for its schedule?
  - id: stopJob
    intent: Stop a running job
    question: How do I halt a job that is currently running?
  phrasing_ops: 7
  slug: cdata-job-api
- baseURL: https://cloud.cdata.com/api
  baseurl_source: declared
  description: The Jobs API from CData — 1 operation(s) for jobs.
  name: CData Jobs API
  phrasing_intents:
  - id: generateJobsURL
    intent: Get a link to the Jobs page
    question: How do I send a user to the Connect AI Jobs page to manage their scheduled jobs?
  phrasing_ops: 1
  slug: cdata-jobs-api
- baseURL: https://cloud.cdata.com/api
  baseurl_source: declared
  description: The Log API from CData — 3 operation(s) for log.
  name: CData Log API
  phrasing_intents:
  - id: listQueryLog
    intent: List query logs for the account
    question: Which queries ran against my Connect AI account in a given time window?
  - id: getQueryLog
    intent: Download the log file for one query
    question: How do I download the detailed log file for a query that failed?
  - id: listAuditLog
    intent: List audit log entries for the account
    question: Who changed what in our account, and can I see an audit trail for it?
  phrasing_ops: 3
  slug: cdata-log-api
- baseURL: https://cloud.cdata.com/api
  baseurl_source: declared
  description: The Metadata API from CData — 10 operation(s) for metadata.
  name: CData Metadata API
  phrasing_intents:
  - id: getCatalogs
    intent: List the catalogs (connections) in my account
    question: Which data connections show up as catalogs in my CData Connect AI account?
  - id: getSchemas
    intent: List the schemas in a catalog
    question: What schemas does one of my connected catalogs contain?
  - id: getTables
    intent: List tables and views in a schema
    question: Which tables and views are available in a schema of my connection?
  - id: getColumns
    intent: List the columns of a table or view
    question: What columns does a given table or view have?
  - id: getPrimaryKeys
    intent: List a table's primary keys
    question: Which columns make up the primary key of a table?
  - id: getImportedKeys
    intent: List the keys a table's foreign keys reference
    question: Which other tables does this table point to through its foreign keys?
  - id: getExportedKeys
    intent: List foreign keys that reference a table
    question: Which other tables hold foreign keys pointing at this table's primary key?
  - id: getIndexes
    intent: List the indexes on a table
    question: What indexes exist on a table in my connection?
  phrasing_ops: 10
  slug: cdata-metadata-api
- baseURL: https://cloud.cdata.com/api
  baseurl_source: declared
  description: The Query API from CData — 3 operation(s) for query.
  name: CData Query API
  phrasing_intents:
  - id: postQuery
    intent: Run a SQL query against my data sources
    question: How do I run a SQL SELECT across the data sources in my CData Connect AI account?
  - id: postBatch
    intent: Run batch inserts, updates or deletes
    question: Can I insert many rows in one request instead of one query per row?
  - id: postExec
    intent: Execute a stored procedure
    question: How do I call a stored procedure on one of my connected data sources?
  phrasing_ops: 3
  slug: cdata-query-api
- baseURL: https://cloud.cdata.com/api
  baseurl_source: declared
  description: Full lifecycle management for machine identities (CI/CD pipelines, IaC tooling, Terraform automation). Service accounts are not SCIM-owned and authenticate via OAuth 2.0 client credentials using the `
  name: CData Service Accounts API
  phrasing_intents:
  - id: createServiceAccount
    intent: Create a service account for automation
    question: How do I create a machine identity for my Terraform or CI/CD pipeline?
  - id: listServiceAccounts
    intent: List the organization's service accounts
    question: Which machine identities, like CI/CD service accounts, exist in our Connect AI organization?
  - id: getServiceAccount
    intent: Get one service account and its permissions
    question: How do I look up a single service account's details and direct permissions?
  - id: updateServiceAccount
    intent: Rename or deactivate a service account
    question: Does deactivating a service account revoke its personal access tokens right away?
  - id: deleteServiceAccount
    intent: Deprovision a service account
    question: What happens to a service account's tokens and roles when I delete it?
  - id: assignServiceAccountRole
    intent: Grant the account-wide admin role to a service account
    question: How do I make a service account an organization-wide admin?
  - id: listServiceAccountRoles
    intent: List roles held by a service account
    question: Which roles does a service account have across the organization, and where did each come from?
  - id: removeServiceAccountRole
    intent: Remove an account-level role from a service account
    question: How do I take the admin role away from a service account?
  phrasing_ops: 14
  slug: cdata-service-accounts-api
- baseURL: https://cloud.cdata.com/api
  baseurl_source: declared
  description: 'Lifecycle management for human users: create, update, deprovision, and manage direct role assignments, workspace-scoped roles, and direct resource permissions. SCIM handles group-based provisioning an'
  name: CData Users API
  phrasing_intents:
  - id: createUser
    intent: Create a single user outside SCIM
    question: How do I add a contractor or break-glass user when we don't use SCIM?
  - id: listUsers
    intent: List the organization's human users
    question: Which people have user accounts in our Connect AI organization?
  - id: batchCreateUsers
    intent: Bulk create or update up to 500 users
    question: Can I import hundreds of users in one request?
  - id: getUser
    intent: Get one user and their direct permissions
    question: How do I look up a single user's profile and directly assigned permissions?
  - id: updateUser
    intent: Update a user's name or status
    question: Why can't I change the name of a user that comes from our identity provider?
  - id: deleteUser
    intent: Deprovision a user
    question: What happens to a user's direct roles and permissions when I delete them?
  - id: assignUserRole
    intent: Grant the account-wide admin role to a user
    question: How do I make a person an organization-wide admin?
  - id: listUserRoles
    intent: List all roles a user holds, however inherited
    question: Which roles does a person have across all workspaces, including ones from groups?
  phrasing_ops: 15
  slug: cdata-users-api
- baseURL: https://mcp.cloud.cdata.com
  baseurl_source: declared
  description: The OData API from CData — 3 operation(s) for odata.
  name: CData O Data API
  phrasing_intents:
  - id: getByWorkspaceName
    intent: Get a workspace's OData service root
    question: What OData resources does a CData Connect AI workspace expose?
  - id: getByWorkspaceName$metadata
    intent: Get the OData $metadata document for a workspace
    question: How do I download the OData $metadata describing a workspace's entity types?
  - id: getByWorkspaceNameByResourcePath
    intent: Query records from an OData resource
    question: How do I read rows from a table through the OData endpoint?
  - id: deleteByWorkspaceNameByResourcePath
    intent: Delete a record through OData
    question: How do I remove a record from a connected source using OData?
  - id: postByWorkspaceNameByResourcePath
    intent: Create a record through OData
    question: How do I insert a new record into a table using OData?
  - id: patchByWorkspaceNameByResourcePath
    intent: Update a record through OData
    question: How do I change fields on an existing record via OData?
  phrasing_ops: 6
  slug: cdata-odata-api
- baseURL: https://mcp.cloud.cdata.com
  baseurl_source: declared
  description: The Open API API from CData — 1 operation(s) for open api.
  name: CData Open API
  phrasing_intents:
  - id: getByVersionByWorkspaceName
    intent: Download an OpenAPI document for a workspace
    question: Can I export an OpenAPI description of my CData Connect AI workspace for a low-code tool?
  phrasing_ops: 1
  slug: cdata-open-api-api
artifact_total: 356
asyncapis:
- description: ''
  name: Cdata Audit Event Forwarding
  slug: cdata-audit-event-forwarding
common:
- group: commercial
  href: https://artifacts.apis.io/cdata/finops/cdata-finops.yml
  title: ''
  type: FinOps
  url: finops/cdata-finops.yml
- group: design
  href: https://artifacts.apis.io/cdata/rules/cdata-rules.yml
  title: ''
  type: Spectral
  url: rules/cdata-rules.yml
- group: design
  href: https://artifacts.apis.io/cdata/json-ld/cdata-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/cdata-context.jsonld
- group: design
  href: https://artifacts.apis.io/cdata/vocabulary/cdata-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/cdata-vocabulary.yml
- group: operate
  href: https://artifacts.apis.io/cdata/lifecycle/cdata-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/cdata-lifecycle.yml
- group: agent
  href: https://artifacts.apis.io/cdata/llms/cdata-www-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cdata-www-llms.txt
- group: other
  href: https://artifacts.apis.io/cdata/hosts/cdata-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cdata-hosts.yml
- group: other
  href: https://artifacts.apis.io/cdata/vendors/cdata-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cdata-vendors.yml
- group: other
  href: https://artifacts.apis.io/cdata/overlays/cdata-odata-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/cdata-odata-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/cdata/overlays/cdata-openapi-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/cdata-openapi-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/cdata/overlays/cdata-rest-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/cdata-rest-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/cdata/overlays/cdata-rest-api-embedded-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/cdata-rest-api-embedded-overlay.yaml
- group: other
  href: https://artifacts.apis.io/cdata/overlays/cdata-management-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/cdata-management-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/cdata/overlays/cdata-mcp-api-embedded-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/cdata-mcp-api-embedded-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.cdata.com/
- group: auth
  href: https://artifacts.apis.io/cdata/scopes/cdata-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/cdata-scopes.yml
- group: agent
  href: https://artifacts.apis.io/cdata/agentic-access/cdata-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/cdata-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/cdata/security/cdata-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/cdata-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/cdata/security/cdata-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cdata-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/cdata/authentication/cdata-authentication.yml
  title: ''
  type: Authentication
  url: authentication/cdata-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cdatasoftware
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cdatasoftware
- group: company
  title: ''
  type: About
  url: https://www.cdata.com/company/
- group: company
  title: ''
  type: Partners
  url: https://www.cdata.com/embedded/customers/
- group: other
  title: ''
  type: CaseStudies
  url: https://www.cdata.com/case-study/
- group: operate
  title: ''
  type: Support
  url: https://www.cdata.com/support/
- group: other
  title: ''
  type: Knowledgebase
  url: https://www.cdata.com/kb/
- group: company
  title: ''
  type: Blog
  url: https://www.cdata.com/blog/
- group: other
  title: ''
  type: WhitePapers
  url: https://www.cdata.com/resources/
- group: learn
  title: ''
  type: Webinars
  url: https://www.cdata.com/resources/
- group: other
  title: ''
  type: Events
  url: https://www.cdata.com/events/
- group: start
  title: ''
  type: Portal
  url: https://www.cdata.com/developers/
- group: other
  title: ''
  type: Glossary
  url: https://www.cdata.com/glossary/
- group: learn
  title: ''
  type: Videos
  url: https://www.cdata.com/kb/video/
- group: operate
  title: ''
  type: PressReleases
  url: https://www.cdata.com/company/press.aspx
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cdata.com/company/legal/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cdata.com/company/legal/privacy/
- group: auth
  title: ''
  type: Security
  url: https://www.cdata.com/security/
- group: auth
  title: ''
  type: Compliance
  url: https://www.cdata.com/security/
- group: other
  title: ''
  type: AWSMarketplace
  url: https://aws.amazon.com/marketplace/pp/prodview-jizwvan7n7sn6
- group: build
  href: https://artifacts.apis.io/cdata/packages/cdata-packages.yml
  title: ''
  type: Packages
  url: packages/cdata-packages.yml
- group: build
  href: https://artifacts.apis.io/cdata/packages/cdata-packages.yml
  title: ''
  type: SDKs
  url: packages/cdata-packages.yml
- group: agent
  href: https://artifacts.apis.io/cdata/well-known/cdata-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cdata-well-known.yml
- group: other
  href: https://artifacts.apis.io/cdata/a2a/cdata-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/cdata-a2a.yml
- group: agent
  href: https://artifacts.apis.io/cdata/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/cdata/llms/cdata-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cdata-llms.txt
- group: agent
  href: https://artifacts.apis.io/cdata/mcp/cdata-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/cdata-mcp.yml
- group: build
  href: https://artifacts.apis.io/cdata/mcp/cdata-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/cdata-tool-crosswalk.yml
- group: design
  href: https://artifacts.apis.io/cdata/conformance/cdata-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cdata-conformance.yml
- group: design
  href: https://artifacts.apis.io/cdata/lifecycle/cdata-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/cdata-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cdata.com/
- group: design
  href: https://artifacts.apis.io/cdata/conventions/cdata-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/cdata-conventions.yml
- group: design
  href: https://artifacts.apis.io/cdata/conventions/cdata-conventions.yml
  title: ''
  type: Conventions
  url: conventions/cdata-conventions.yml
- group: operate
  href: https://artifacts.apis.io/cdata/changelog/cdata-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/cdata-changelog.yml
- group: build
  href: https://artifacts.apis.io/cdata/cli/cdata-cli.yml
  title: ''
  type: CLI
  url: cli/cdata-cli.yml
- group: design
  href: https://artifacts.apis.io/cdata/components/cdata-components.yml
  title: ''
  type: Components
  url: components/cdata-components.yml
- group: start
  href: https://artifacts.apis.io/cdata/sandbox/cdata-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/cdata-sandbox.yml
- group: design
  href: https://artifacts.apis.io/cdata/data-model/cdata-data-model.yml
  title: ''
  type: DataModel
  url: data-model/cdata-data-model.yml
- group: design
  href: https://artifacts.apis.io/cdata/errors/cdata-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/cdata-problem-types.yml
- group: commercial
  href: https://artifacts.apis.io/cdata/plans/cdata-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/cdata-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/cdata/rate-limits/cdata-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/cdata-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/cdata/asyncapi/cdata-audit-event-forwarding.yml
  title: ''
  type: Webhooks
  url: asyncapi/cdata-audit-event-forwarding.yml
- group: docs
  title: ''
  type: Documentation
  url: https://docs.cloud.cdata.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.cloud.cdata.com/en/API/API
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.cdata.com/developers/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.cdata.com/developers/ai/quickstart/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.cdata.com/ai/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://cloud.cdata.com/developer
- group: operate
  title: ''
  type: Community
  url: https://community.cdata.com/
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://docs.cloud.cdata.com/en/ReleaseNotes
- group: other
  href: https://artifacts.apis.io/cdata/capabilities/cdata-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/cdata-capability-edges.yml
created: '2025-06-05'
description: CData Software is a leading provider of data access and connectivity solutions. Our standards-based connectors streamline data access and insulate customers from the complexities of integrating with on-premise or cloud databases, SaaS, APIs, NoSQL, and Big Data.
features:
- name: SQL
- name: ODBC
- name: JDBC
- name: ADO.NET
- name: Excel
- name: SSIS
- name: EDI
- name: FTP
- name: X12
- name: EDIFact
- name: HL7 FHIR
- name: CSV
- name: XML
- name: ETL
- name: ELT
- name: SOC
- name: SOC2
- name: GDPR
- name: Data Quality
- name: Data Security
- name: Data Compliance
- name: Data Transformation
- name: SQL Normalization
- name: Metadata Caching
- name: Data Modeling
- name: Data Governance
- name: Data Replication
- name: Data Backups
- name: API Server
- name: Embedded Integrations
- name: Streaming
- name: Kafka
- name: Data Lakehouse
- name: Data Warehouse
- name: Security
- name: Authentication
- name: Hybrid-Cloud
- name: Multi-Cloud
- name: Semantic Layer
- name: Analytical Queries
- name: Data Intensive Workloads
- name: No-Code
- name: Low-Code
- name: Virtual Datasets
- name: Dashboards
- name: Reports
- name: Insights
- name: Intelligence
- name: Automation
- name: Webhooks
finops:
- has_sources: true
  method: derived
  name: Cdata Finops
  primary_unit: source
  service_category: ''
  slug: cdata-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cdata.png
integrations:
- name: Access
- name: Act CRM
- name: Act-On
- name: Active Directory
- name: ActiveCampaign
- name: Acumatica
- name: Adobe Analytics
- name: Adobe Commerce
- name: ADP
- name: Airtable
- name: AlloyDB
- name: Amazon Athena
- name: Amazon DynamoDB
- name: Amazon Marketplace
- name: Amazon S3
- name: Asana
- name: Authorize.Net
- name: Avalara AvaTax
- name: Avro
- name: Azure Active Directory
- name: Azure Analysis Services
- name: Azure Data Catalog
- name: Azure Data Lake Storage
- name: Azure DevOps
- name: Azure Synapse
- name: Azure Table
- name: Basecamp
- name: BigCommerce
- name: BigQuery
- name: Bing Ads
- name: Bing Search
- name: Bitbucket
- name: Blackbaud FE NXT
- name: Box
- name: Bullhorn CRM
- name: Cassandra
- name: Certinia
- name: Cloudant
- name: CockroachDB
- name: Confluence
- name: Cosmos DB
- name: Couchbase
- name: CouchDB
- name: CSV
- name: Cvent
- name: Databricks
- name: DB2
- name: DocuSign
- name: Dropbox
- name: Dynamics 365
- name: Dynamics 365 Business Central
- name: Dynamics CRM
- name: Dynamics GP
- name: Dynamics NAV
- name: eBay
- name: eBay Analytics
- name: Elasticsearch
- name: Email
- name: EnterpriseDB
- name: Epicor Kinetic
- name: Exact Online
- name: Excel
- name: Excel Online
- name: Facebook
- name: Facebook Ads
- name: FHIR
- name: Freshdesk
- name: FTP
- name: GitHub
- name: Gmail
- name: Google Ad Manager
- name: Google Ads
- name: Google Analytics
- name: Google Calendar
- name: Google Campaign Manager 360
- name: Google Cloud Storage
- name: Google Contacts
- name: Google Data Catalog
- name: Google Directory
- name: Google Drive
- name: Google Search
- name: Google Sheets
- name: Google Spanner
- name: GraphQL
- name: Greenhouse
- name: Greenplum
- name: HarperDB
- name: HBase
- name: HCL Domino
- name: HDFS
- name: Highrise
- name: Hive
- name: HubDB
- name: HubSpot
- name: IBM Cloud Data Engine
- name: IBM Cloud Object Storage
- name: IBM Informix
- name: Impala
- name: Instagram
- name: JDBC-ODBC Bridge
- name: Jira
- name: Jira Assets
- name: Jira Service Management
- name: JSON
- name: Kafka
- name: Kintone
- name: LDAP
- name: LinkedIn
- name: LinkedIn Ads
- name: MailChimp
- name: MariaDB
- name: Marketo
- name: MarkLogic
- name: Microsoft Dataverse
- name: Microsoft Entra ID
- name: Microsoft Exchange
- name: Microsoft OneDrive
- name: Microsoft Planner
- name: Microsoft Project
- name: Microsoft Teams
- name: Monday.com
- name: MongoDB
- name: MYOB AccountRight
- name: MySQL
- name: nCino
- name: Neo4J
- name: NetSuite
- name: OData
- name: Odoo
- name: Office 365
- name: Okta
- name: OneNote
- name: Oracle
- name: Oracle Eloqua
- name: Oracle Financials Cloud
- name: Oracle HCM Cloud
- name: Oracle Sales
- name: Oracle SCM
- name: Oracle Service Cloud
- name: Outreach.io
- name: Parquet
- name: Paylocity
- name: PayPal
- name: Phoenix
- name: PingOne
- name: Pinterest
- name: Pipedrive
- name: PostgreSQL
- name: Power BI XMLA
- name: Presto
- name: Quickbase
- name: QuickBooks
- name: QuickBooks Online
- name: QuickBooks Time
- name: Raisers Edge NXT
- name: Reckon
- name: Reckon Accounts Hosted
- name: Redis
- name: Redshift
- name: REST
- name: RSS
- name: Sage 200
- name: Sage 300
- name: Sage 50 UK
- name: Sage Cloud Accounting
- name: Sage Intacct
- name: Salesforce
- name: Salesforce Data Cloud
- name: Salesforce Financial Service Cloud
- name: Salesforce Marketing
- name: Salesforce Marketing Cloud Account Engagement
- name: Salesforce Pardot
- name: Salesloft
- name: SAP
- name: SAP Ariba Procurement
- name: SAP Ariba Source
- name: SAP Business One
- name: SAP BusinessObjects BI
- name: SAP ByDesign
- name: SAP Concur
- name: SAP Fieldglass
- name: SAP HANA
- name: SAP HANA XS Advanced
- name: SAP Hybris C4C
- name: SAP Netweaver Gateway
- name: SAP SuccessFactors
- name: SAS Data Sets
- name: SAS xpt
- name: SendGrid
- name: ServiceNow
- name: SFTP
- name: SharePoint
- name: SharePoint Excel Services
- name: ShipStation
- name: Shopify
- name: SingleStore
- name: Slack
- name: Smartsheet
- name: Snapchat Ads
- name: Snowflake
- name: Spark
- name: Splunk
- name: SQL Analysis Services
- name: SQL Server
- name: SQLite
- name: Square
- name: Stripe
- name: Sugar CRM
- name: SuiteCRM
- name: SurveyMonkey
- name: Sybase
- name: Sybase IQ
- name: Tableau CRM Analytics
- name: Tally
- name: TaxJar
- name: Teradata
- name: Tier1
- name: TigerGraph
- name: Trello
- name: Trino
- name: Twilio
- name: Twitter
- name: Twitter Ads
- name: Veeva CRM
- name: Veeva Vault
- name: Wave Financial
- name: WooCommerce
- name: WordPress
- name: Workday
- name: xBase
- name: Xero
- name: XML
- name: YouTube Analytics
- name: Zendesk
- name: Zoho Books
- name: Zoho Creator
- name: Zoho CRM
- name: Zoho Inventory
- name: Zoho Projects
- name: Zuora
json_schemas:
- name: AccountInfo
  property_count: 4
  slug: cdata-account-info
- name: AccountListResult
  property_count: 1
  slug: cdata-account-list-result
- name: AssignPermissionRequest
  property_count: 3
  slug: cdata-assign-permission-request
- name: AuditSearchResult
  property_count: 1
  slug: cdata-audit-search-result
- name: BatchCreateUsersResponse
  property_count: 4
  slug: cdata-batch-create-users-response
- name: BatchRequest
  property_count: 5
  slug: cdata-batch-request
- name: CacheConnectionRequest
  property_count: 1
  slug: cdata-cache-connection-request
- name: ConnectionListResult
  property_count: 1
  slug: cdata-connection-list-result
- name: CreateAccountRequest
  property_count: 2
  slug: cdata-create-account-request
- name: CreateAccountResult
  property_count: 3
  slug: cdata-create-account-result
- name: CreateConnectionRequest
  property_count: 5
  slug: cdata-create-connection-request
- name: CreateJobRequest
  property_count: 7
  slug: cdata-create-job-request
- name: CreateServiceAccountRequest
  property_count: 3
  slug: cdata-create-service-account-request
- name: CreateUserRequest
  property_count: 4
  slug: cdata-create-user-request
- name: DataSourceListResult
  property_count: 1
  slug: cdata-data-source-list-result
- name: EditConnectionRequest
  property_count: 3
  slug: cdata-edit-connection-request
- name: ExecRequest
  property_count: 5
  slug: cdata-exec-request
- name: JobInfo
  property_count: 12
  slug: cdata-job-info
- name: JobListResult
  property_count: 1
  slug: cdata-job-list-result
- name: JsonRpcRequest
  property_count: 4
  slug: cdata-json-rpc-request
- name: JsonRpcResponse
  property_count: 4
  slug: cdata-json-rpc-response
- name: QueryRequest
  property_count: 6
  slug: cdata-query-request
- name: QueryResult
  property_count: 2
  slug: cdata-query-result
- name: QuerySearchCriteria
  property_count: 3
  slug: cdata-query-search-criteria
- name: QuerySearchResult
  property_count: 1
  slug: cdata-query-search-result
- name: RedirectURLResponse
  property_count: 1
  slug: cdata-redirect-urlresponse
- name: ServiceAccountPermissionAssignment
  property_count: 7
  slug: cdata-service-account-permission-assignment
- name: ServiceAccountRoleAssignment
  property_count: 8
  slug: cdata-service-account-role-assignment
- name: ServiceAccount
  property_count: 8
  slug: cdata-service-account
- name: ServiceAccountWorkspaceRoleAssignment
  property_count: 8
  slug: cdata-service-account-workspace-role-assignment
- name: UpdateAccountRequest
  property_count: 2
  slug: cdata-update-account-request
- name: UpdateJobRequest
  property_count: 7
  slug: cdata-update-job-request
- name: UserPermissionAssignment
  property_count: 7
  slug: cdata-user-permission-assignment
- name: UserRoleAssignment
  property_count: 8
  slug: cdata-user-role-assignment
- name: User
  property_count: 9
  slug: cdata-user
- name: UserWorkspaceRoleAssignment
  property_count: 8
  slug: cdata-user-workspace-role-assignment
jsonld:
- class_count: 63
  name: Cdata Context
  property_count: 126
  slug: cdata-context
layout: provider
mcp_servers:
- description: 'CData Connect AI ships a hosted, remote MCP server that exposes every configured data source connection as MCP tools. Two servers are published: a data server at /mcp (catalog/schema/table/column disc'
  name: CData Connect AI MCP
  slug: cdata-connect-ai-mcp
modified: '2026-09-05'
name: CData
nav: Providers
network: true
overview: 'CData publishes 14 API contracts indexed on the [APIs.io](https://apis.io/) network, including Connect AI MCP Server, Account API, Cache API, and 11 more. Tagged areas include Data, Data Access, Data Connectivity, Database, and NoSQL.


  The CData catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  CData''s developer surface includes authentication, support, engineering blog, developer portal, changelog, CLI, sandbox, and 64 more developer resources.'
plans:
- name: Cdata Plans Pricing
  plan_count: 8
  slug: cdata-plans-pricing
- name: Cdata Price Estimates
  plan_count: 0
  slug: cdata-price-estimates
random_paper: 5
rate_limits:
- limit_count: 3
  name: Cdata Rate Limits
  slug: cdata-rate-limits
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: CData API Rules
  rule_count: 13
  severity_counts:
    error: 8
    hint: 0
    info: 2
    warn: 3
  slug: cdata-rules
scopes:
- name: Cdata Scopes
  scope_count: 4
  slug: cdata-scopes
  summary_line: 4 scopes · clientCredentials
score:
  band: exemplar
  composite: 83.8
  coverage:
    artifact_dirs: 39
    catalog_earned: 92.8
    catalog_earned_first_party: 24.0
    catalog_gap: 22.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 86.8
    contract_governance: 35.6
    contract_quality: 69.8
    developer_ergonomics: 83.3
    discoverability: 81.7
    operational_transparency: 92.1
  previous_composite: 83.8
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 7.1
      derived: 0
      marker_coverage: 0.0
      total: 14
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 39.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 50.0
screenshot: https://apis.io/screenshots/cdata/cdata-2026-06-20T174101.png
security:
- kind: authentication
  name: Cdata Authentication
  slug: cdata-authentication
  summary_line: http/oauth2 · 3 schemes
- kind: domain-security
  name: Cdata Domain Security
  slug: cdata-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Cdata Trust Center
  slug: cdata-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, GDPR
skill_count: 3
skills:
- name: connect-ai-base
  slug: cdata-connect-ai-base
- name: connect-ai-onboarding-claude-code
  slug: cdata-connect-ai-onboarding-claude-code
- name: cdata-connect-ai-published-skill
  slug: cdata-connect-ai-published-skill
slug: cdata
tags:
- Data
- Data Access
- Data Connectivity
- Database
- NoSQL
- SQL
- A2A
website: https://www.cdata.com/
---
