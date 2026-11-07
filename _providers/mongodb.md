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
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: mostly
    pagination_ratio: partial
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 56.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 240
  human_in_the_loop: 9
  name: Mongodb Agentic Access
  operation_count: 468
  slug: mongodb-agentic-access
  summary_line: 468 operations · 240 acting · 9 human-in-the-loop
api_count: 2
apis:
- description: The Atlas Data API lets you read and write data in MongoDB Atlas with standard HTTPS requests, without the need for a MongoDB driver.
  name: MongoDB Atlas Data API
  slug: mongodb-atlas-data-api
- description: Admin API for MongoDB Atlas App Services (formerly Realm), used to manage applications, services, functions, and triggers.
  name: MongoDB Atlas App Services Admin API
  slug: mongodb-atlas-app-services-admin-api
- baseURL: https://cloud.mongodb.com/api/atlas/v2
  baseurl_source: declared
  description: Returns access logs for authentication attempts made to Atlas database deployments. To view database access history, you must have either the Project Owner or Organization Owner role.
  name: MongoDB Access Tracking API
  slug: mongodb-access-tracking-api
- baseURL: https://cloud.mongodb.com/api/atlas/v2
  baseurl_source: declared
  description: Returns pre-filtered activity feed links for projects and organizations. The returned links can be shared and opened to view the activity feed with the specified filters applied.
  name: MongoDB Activity Feed API
  slug: mongodb-activity-feed-api
- baseURL: https://cloud.mongodb.com/api/atlas/v2
  baseurl_source: declared
  description: Returns and edits the conditions that trigger alerts and how MongoDB Cloud notifies users. This collection remains under revision and may change.
  name: MongoDB Alert Configurations API
  slug: mongodb-alert-configurations-api
- baseURL: https://cloud.mongodb.com/api/atlas/v2
  baseurl_source: declared
  description: Returns and acknowledges alerts that MongoDB Cloud triggers based on the alert conditions that you define. This collection remains under revision and may change.
  name: MongoDB Alerts API
  slug: mongodb-alerts-api
- baseURL: https://cloud.mongodb.com/api/atlas/v2
  baseurl_source: declared
  description: Returns, adds, edits, and removes Atlas Search indexes for the specified cluster. Also returns and updates user-defined analyzers for the specified cluster.
  name: MongoDB Atlas Search API
  slug: mongodb-atlas-search-api
- baseURL: https://cloud.mongodb.com/api/atlas/v2
  baseurl_source: declared
  description: Returns and edits database auditing settings for MongoDB Cloud projects.
  name: MongoDB Auditing API
  slug: mongodb-auditing-api
- baseURL: https://cloud.mongodb.com/api/atlas/v2
  baseurl_source: declared
  description: Returns and edits custom DNS configurations for MongoDB Cloud database deployments on AWS. The resource requires your Project ID. If you use the VPC peering on AWS and you use your own DNS servers ins
  name: MongoDB AWS Clusters DNS API
  slug: mongodb-aws-clusters-dns-api
- baseURL: https://cloud.mongodb.com/api/atlas/v2
  baseurl_source: declared
  description: Manages Cloud Backup snapshots, snapshot export buckets, restore jobs, and schedules. This resource applies only to clusters that use Cloud Backups.
  name: MongoDB Cloud Backups API
  slug: mongodb-cloud-backups-api
- baseURL: https://cloud.mongodb.com/api/atlas/v2
  baseurl_source: declared
  description: Manages the Cloud Migration Service. Source organizations, projects, and MongoDB clusters reside on Cloud Manager or Ops Manager. Destination organizations, projects, and MongoDB clusters reside on Mo
  name: MongoDB Cloud Migration Service API
  slug: mongodb-cloud-migration-service-api
- baseURL: https://cloud.mongodb.com/api/atlas/v2
  baseurl_source: declared
  description: Returns, adds, authorizes, and removes AWS IAM roles in Atlas.
  name: MongoDB Cloud Provider Access API
  slug: mongodb-cloud-provider-access-api
- baseURL: https://cloud.mongodb.com/api/atlas/v2
  baseurl_source: declared
  description: Returns, starts, or ends a cluster outage simulation.
  name: MongoDB Cluster Outage Simulation API
  slug: mongodb-cluster-outage-simulation-api
- baseURL: https://cloud.mongodb.com/api/atlas/v2
  baseurl_source: declared
  description: Returns, adds, edits, and removes database deployments. Changes to cluster configurations can affect costs. This resource requires your Project ID.
  name: MongoDB Clusters API
  slug: mongodb-clusters-api
- baseURL: https://cloud.mongodb.com/api/atlas/v2
  baseurl_source: declared
  description: Returns, adds, and edits pinned namespaces for the specified cluster or process. Also returns collection level latency metric data.
  name: MongoDB Collection Level Metrics API
  slug: mongodb-collection-level-metrics-api
- baseURL: https://cloud.mongodb.com/api/atlas/v2
  baseurl_source: declared
  description: Returns, adds, edits, and removes custom database user privilege roles. Use custom roles to specify custom sets of actions that the MongoDB Cloud built-in roles can't describe. You define custom roles
  name: MongoDB Custom Database Roles API
  slug: mongodb-custom-database-roles-api
- baseURL: https://cloud.mongodb.com/api/atlas/v2
  baseurl_source: declared
  description: Returns, adds, edits, and removes Federated Database Instances. This resource requires your project ID. Changes to federated database instance configurations can affect costs.
  name: MongoDB Data Federation API
  slug: mongodb-data-federation-api
- baseURL: https://cloud.mongodb.com/api/atlas/v2
  baseurl_source: declared
  description: Returns, edits, and removes Atlas Data Lake Pipelines and associated runs.
  name: MongoDB Data Lake Pipelines API
  slug: mongodb-data-lake-pipelines-api
- baseURL: https://cloud.mongodb.com/api/atlas/v2
  baseurl_source: declared
  description: Returns, adds, edits, and removes database users.
  name: MongoDB Database Users API
  slug: mongodb-database-users-api
- baseURL: https://cloud.mongodb.com/api/atlas/v2
  baseurl_source: declared
  description: Returns and edits the Encryption at Rest using Customer Key Management configuration. MongoDB Cloud encrypts all storage whether or not you use your own key management.
  name: MongoDB Encryption at Rest using Customer Key Management API
  slug: mongodb-encryption-at-rest-using-customer-key-management-api
- baseURL: https://cloud.mongodb.com/api/atlas/v2
  baseurl_source: declared
  description: Returns events. This collection remains under revision and may change.
  name: MongoDB Events API
  slug: mongodb-events-api
- baseURL: https://cloud.mongodb.com/api/atlas/v2
  baseurl_source: declared
  description: Returns, adds, edits, and removes federation-related features such as role mappings and connected organization configurations.
  name: MongoDB Federated Authentication API
  slug: mongodb-federated-authentication-api
- baseURL: https://cloud.mongodb.com/api/atlas/v2
  baseurl_source: declared
  description: Returns, adds, edits, and removes flex clusters.
  name: MongoDB Flex Clusters API
  slug: mongodb-flex-clusters-api
- baseURL: https://cloud.mongodb.com/api/atlas/v2
  baseurl_source: declared
  description: Returns and adds restore jobs for flex database deployments.
  name: MongoDB Flex Restore Jobs API
  slug: mongodb-flex-restore-jobs-api
- baseURL: https://cloud.mongodb.com/api/atlas/v2
  baseurl_source: declared
  description: Returns and requests to download flex database deployment snapshots.
  name: MongoDB Flex Snapshots API
  slug: mongodb-flex-snapshots-api
- baseURL: https://cloud.mongodb.com/api/atlas/v2
  baseurl_source: declared
  description: Returns, adds, and removes Global Cluster managed namespaces and custom zone mappings. Each collection in a Global Cluster is associated with a managed namespace. When you create a managed namespace f
  name: MongoDB Global Clusters API
  slug: mongodb-global-clusters-api
- baseURL: https://cloud.mongodb.com/api/atlas/v2
  baseurl_source: declared
  description: Returns invoices.
  name: MongoDB Invoices API
  slug: mongodb-invoices-api
- baseURL: https://cloud.mongodb.com/api/atlas/v2
  baseurl_source: declared
  description: Returns, edits, verifies, and removes LDAP configurations. An LDAP configuration defines settings for MongoDB Cloud to connect to your LDAP server over TLS for user authentication and authorization. Y
  name: MongoDB LDAP Configuration API
  slug: mongodb-ldap-configuration-api
- baseURL: https://cloud.mongodb.com/api/atlas/v2
  baseurl_source: declared
  description: Manages Legacy Backup snapshots, restore jobs, schedules and checkpoints.
  name: MongoDB Legacy Backup API
  slug: mongodb-legacy-backup-api
- baseURL: https://cloud.mongodb.com/api/atlas/v2
  baseurl_source: declared
  description: Returns, edits, and removes maintenance windows. The maintenance procedure that MongoDB Cloud performs requires at least one replica set election during the maintenance window per replica set. You can
  name: MongoDB Maintenance Windows API
  slug: mongodb-maintenance-windows-api
- baseURL: https://cloud.mongodb.com/api/atlas/v2
  baseurl_source: declared
  description: Returns, adds, and edits MongoDB Cloud users.
  name: MongoDB Cloud Users API
  slug: mongodb-mongodb-cloud-users-api
- baseURL: https://cloud.mongodb.com/api/atlas/v2
  baseurl_source: declared
  description: Returns database deployment monitoring and logging data.
  name: MongoDB Monitoring and Logs API
  slug: mongodb-monitoring-and-logs-api
- baseURL: https://cloud.mongodb.com/api/atlas/v2
  baseurl_source: declared
  description: 'Returns, adds, edits, and removes network peering containers and peering connections. When you deploy an M10+ dedicated cluster, Atlas creates a VPC for the selected provider and region or regions if '
  name: MongoDB Network Peering API
  slug: mongodb-network-peering-api
- baseURL: https://cloud.mongodb.com/api/atlas/v2
  baseurl_source: declared
  description: Returns, adds, edits, or removes an online archive.
  name: MongoDB Online Archive API
  slug: mongodb-online-archive-api
- baseURL: https://cloud.mongodb.com/api/atlas/v2
  baseurl_source: declared
  description: Returns, adds, and edits organizational units in MongoDB Cloud.
  name: MongoDB Organizations API
  slug: mongodb-organizations-api
- baseURL: https://cloud.mongodb.com/api/atlas/v2
  baseurl_source: declared
  description: Returns suggested indexes and slow query data for a database deployment. Also enables or disables MongoDB Cloud-managed slow operation thresholds. To view field values in a sample query, you must have
  name: MongoDB Performance Advisor API
  slug: mongodb-performance-advisor-api
- baseURL: https://cloud.mongodb.com/api/atlas/v2
  baseurl_source: declared
  description: Returns, adds, edits, and removes private endpoint services.
  name: MongoDB Private Endpoint Services API
  slug: mongodb-private-endpoint-services-api
- baseURL: https://cloud.mongodb.com/api/atlas/v2
  baseurl_source: declared
  description: 'Returns, adds, edits, and removes access tokens to use the MongoDB Cloud API. MongoDB Cloud applies these keys to organizations. These resources can return, assign, or revoke use of these keys within '
  name: MongoDB Programmatic API Keys API
  slug: mongodb-programmatic-api-keys-api
- baseURL: https://cloud.mongodb.com/api/atlas/v2
  baseurl_source: declared
  description: Returns, adds, edits, and removes network access limits to database deployments in Atlas. This resource replaces the whitelist resource. Atlas removed whitelists in July 2021. Update your applications
  name: MongoDB Project IP Access List API
  slug: mongodb-project-ip-access-list-api
- baseURL: https://cloud.mongodb.com/api/atlas/v2
  baseurl_source: declared
  description: Returns, adds, and edits collections of clusters and users in MongoDB Cloud.
  name: MongoDB Projects API
  slug: mongodb-projects-api
- baseURL: https://cloud.mongodb.com/api/atlas/v2
  baseurl_source: declared
  description: You can continually export mongod, mongos, and audit logs to an AWS S3 bucket. The new `/logIntegrations` API provides 1-minute log export on a best-effort basis. The existing `/pushBasedLogExport` AP
  name: MongoDB Push-Based Log Export API
  slug: mongodb-push-based-log-export-api
- baseURL: https://cloud.mongodb.com/api/atlas/v2
  baseurl_source: declared
  description: The Query Shape Insights API from MongoDB — 4 operation(s) for query shape insights.
  name: MongoDB Query Shape Insights API
  slug: mongodb-query-shape-insights-api
- baseURL: https://cloud.mongodb.com/api/atlas/v2
  baseurl_source: declared
  description: Returns details about rate limit policies for the Atlas Administration API.
  name: MongoDB Rate Limiting API
  slug: mongodb-rate-limiting-api
- baseURL: https://cloud.mongodb.com/api/atlas/v2
  baseurl_source: declared
  description: Configure and manage Atlas Resource Policies within your organization.
  name: MongoDB Resource Policies API
  slug: mongodb-resource-policies-api
- baseURL: https://cloud.mongodb.com/api/atlas/v2
  baseurl_source: declared
  description: Creates one index to a database deployment in a rolling manner. Rolling indexes build indexes on the applicable nodes sequentially and may reduce the performance impact of an index build if your deplo
  name: MongoDB Rolling Index API
  slug: mongodb-rolling-index-api
- baseURL: https://cloud.mongodb.com/api/atlas/v2
  baseurl_source: declared
  description: Returns details that describe the MongoDB Cloud build and the access token that requests this resource. This starts the MongoDB Cloud API.
  name: MongoDB Root API
  slug: mongodb-root-api
- baseURL: https://cloud.mongodb.com/api/atlas/v2
  baseurl_source: declared
  description: Returns, adds, edits, and removes serverless instances.
  name: MongoDB Serverless Instances API
  slug: mongodb-serverless-instances-api
- baseURL: https://cloud.mongodb.com/api/atlas/v2
  baseurl_source: declared
  description: Returns, adds, edits, and removes private endpoints for serverless instances. To learn more, see the Atlas Administration API tab on the following tutorial.
  name: MongoDB Serverless Private Endpoints API
  slug: mongodb-serverless-private-endpoints-api
- baseURL: https://cloud.mongodb.com/api/atlas/v2
  baseurl_source: declared
  description: Endpoints for managing Service Accounts and secrets. Service Accounts are used for programmatic access to the Atlas Admin API through the OAuth 2.0 Client Credentials flow.
  name: MongoDB Service Accounts API
  slug: mongodb-service-accounts-api
- baseURL: https://cloud.mongodb.com/api/atlas/v2
  baseurl_source: declared
  description: Returns, adds, edits, and removes Streams Workspaces. This resource requires your project ID.
  name: MongoDB Streams API
  slug: mongodb-streams-api
- baseURL: https://cloud.mongodb.com/api/atlas/v2
  baseurl_source: declared
  description: Returns, adds, edits, or removes teams.
  name: MongoDB Teams API
  slug: mongodb-teams-api
- baseURL: https://cloud.mongodb.com/api/atlas/v2
  baseurl_source: declared
  description: 'Returns, adds, edits, and removes third-party service integration configurations. MongoDB Cloud sends alerts to each third-party service that you configure. **IMPORTANT**: Each project can only have o'
  name: MongoDB Third-Party Integrations API
  slug: mongodb-third-party-integrations-api
- baseURL: https://cloud.mongodb.com/api/atlas/v2
  baseurl_source: declared
  description: Returns, edits, and removes user-managed X.509 configurations. Also returns and generates MongoDB Cloud-managed X.509 certificates for database users. The following resources help manage database user
  name: MongoDB X.509 Authentication API
  slug: mongodb-x-509-authentication-api
- baseURL: https://cloud.mongodb.com
  baseurl_source: declared
  description: Returns, adds, edits, and removes API Keys for your AI Models.
  name: MongoDB AI Model API Keys API
  slug: mongodb-ai-model-api-keys-api
- baseURL: https://cloud.mongodb.com
  baseurl_source: declared
  description: Returns, adds, edits, and removes Rate Limits for your AI Models.
  name: MongoDB AI Model Rate Limits API
  slug: mongodb-ai-model-rate-limits-api
- baseURL: https://cloud.mongodb.com
  baseurl_source: declared
  description: Returns, creates, updates, and removes metric integration configurations for a project.
  name: MongoDB Metric Integrations API
  slug: mongodb-metric-integrations-api
- baseURL: https://cloud.mongodb.com
  baseurl_source: declared
  description: Returns and starts overload protection simulations for a cluster.
  name: MongoDB Overload Protection Simulation API
  slug: mongodb-overload-protection-simulation-api
- baseURL: https://cloud.mongodb.com
  baseurl_source: declared
  description: Returns and manages Remote MCP configurations for organizations and projects.
  name: MongoDB Remote MCP Configurations API
  slug: mongodb-remote-mcp-configurations-api
artifact_total: 328
collections:
- collection_type: open
  name: MongoDB Atlas Administration Access Tracking API
  slug: open-mongodb-access-tracking-api
- collection_type: open
  name: MongoDB Atlas Administration Access Tracking Activity Feed API
  slug: open-mongodb-activity-feed-api
- collection_type: open
  name: MongoDB Atlas Administration Access Tracking Alert Configurations API
  slug: open-mongodb-alert-configurations-api
- collection_type: open
  name: MongoDB Atlas Administration Access Tracking Alerts API
  slug: open-mongodb-alerts-api
- collection_type: open
  name: MongoDB Atlas Administration Access Tracking Atlas Search API
  slug: open-mongodb-atlas-search-api
- collection_type: open
  name: MongoDB Atlas Administration Access Tracking Auditing API
  slug: open-mongodb-auditing-api
- collection_type: open
  name: MongoDB Atlas Administration Access Tracking AWS Clusters DNS API
  slug: open-mongodb-aws-clusters-dns-api
- collection_type: open
  name: MongoDB Atlas Administration Access Tracking Cloud Backups API
  slug: open-mongodb-cloud-backups-api
- collection_type: open
  name: MongoDB Atlas Administration Access Tracking Cloud Migration Service API
  slug: open-mongodb-cloud-migration-service-api
- collection_type: open
  name: MongoDB Atlas Administration Access Tracking Cloud Provider Access API
  slug: open-mongodb-cloud-provider-access-api
- collection_type: open
  name: MongoDB Atlas Administration Access Tracking Cluster Outage Simulation API
  slug: open-mongodb-cluster-outage-simulation-api
- collection_type: open
  name: MongoDB Atlas Administration Access Tracking Clusters API
  slug: open-mongodb-clusters-api
- collection_type: open
  name: MongoDB Atlas Administration Access Tracking Collection Level Metrics API
  slug: open-mongodb-collection-level-metrics-api
- collection_type: open
  name: MongoDB Atlas Administration Access Tracking Custom Database Roles API
  slug: open-mongodb-custom-database-roles-api
- collection_type: open
  name: MongoDB Atlas Administration Access Tracking Data Federation API
  slug: open-mongodb-data-federation-api
- collection_type: open
  name: MongoDB Atlas Administration Access Tracking Data Lake Pipelines API
  slug: open-mongodb-data-lake-pipelines-api
- collection_type: open
  name: MongoDB Atlas Administration Access Tracking Database Users API
  slug: open-mongodb-database-users-api
- collection_type: open
  name: MongoDB Atlas Administration Access Tracking Encryption at Rest using Customer Key Management API
  slug: open-mongodb-encryption-at-rest-using-customer-key-management-api
- collection_type: open
  name: MongoDB Atlas Administration Access Tracking Events API
  slug: open-mongodb-events-api
- collection_type: open
  name: MongoDB Atlas Administration Access Tracking Federated Authentication API
  slug: open-mongodb-federated-authentication-api
- collection_type: open
  name: MongoDB Atlas Administration Access Tracking Flex Clusters API
  slug: open-mongodb-flex-clusters-api
- collection_type: open
  name: MongoDB Atlas Administration Access Tracking Flex Restore Jobs API
  slug: open-mongodb-flex-restore-jobs-api
- collection_type: open
  name: MongoDB Atlas Administration Access Tracking Flex Snapshots API
  slug: open-mongodb-flex-snapshots-api
- collection_type: open
  name: MongoDB Atlas Administration Access Tracking Global Clusters API
  slug: open-mongodb-global-clusters-api
- collection_type: open
  name: MongoDB Atlas Administration Access Tracking Invoices API
  slug: open-mongodb-invoices-api
- collection_type: open
  name: MongoDB Atlas Administration Access Tracking LDAP Configuration API
  slug: open-mongodb-ldap-configuration-api
- collection_type: open
  name: MongoDB Atlas Administration Access Tracking Legacy Backup API
  slug: open-mongodb-legacy-backup-api
- collection_type: open
  name: MongoDB Atlas Administration Access Tracking Maintenance Windows API
  slug: open-mongodb-maintenance-windows-api
- collection_type: open
  name: MongoDB Atlas Administration Access Tracking MongoDB Cloud Users API
  slug: open-mongodb-mongodb-cloud-users-api
- collection_type: open
  name: MongoDB Atlas Administration Access Tracking Monitoring and Logs API
  slug: open-mongodb-monitoring-and-logs-api
- collection_type: open
  name: MongoDB Atlas Administration Access Tracking Network Peering API
  slug: open-mongodb-network-peering-api
- collection_type: open
  name: MongoDB Atlas Administration Access Tracking Online Archive API
  slug: open-mongodb-online-archive-api
- collection_type: open
  name: MongoDB Atlas Administration Access Tracking Organizations API
  slug: open-mongodb-organizations-api
- collection_type: open
  name: MongoDB Atlas Administration Access Tracking Performance Advisor API
  slug: open-mongodb-performance-advisor-api
- collection_type: open
  name: MongoDB Atlas Administration Access Tracking Private Endpoint Services API
  slug: open-mongodb-private-endpoint-services-api
- collection_type: open
  name: MongoDB Atlas Administration Access Tracking Programmatic API Keys API
  slug: open-mongodb-programmatic-api-keys-api
- collection_type: open
  name: MongoDB Atlas Administration Access Tracking Project IP Access List API
  slug: open-mongodb-project-ip-access-list-api
- collection_type: open
  name: MongoDB Atlas Administration Access Tracking Projects API
  slug: open-mongodb-projects-api
- collection_type: open
  name: MongoDB Atlas Administration Access Tracking Push-Based Log Export API
  slug: open-mongodb-push-based-log-export-api
- collection_type: open
  name: MongoDB Atlas Administration Access Tracking Query Shape Insights API
  slug: open-mongodb-query-shape-insights-api
- collection_type: open
  name: MongoDB Atlas Administration Access Tracking Rate Limiting API
  slug: open-mongodb-rate-limiting-api
- collection_type: open
  name: MongoDB Atlas Administration Access Tracking Resource Policies API
  slug: open-mongodb-resource-policies-api
- collection_type: open
  name: MongoDB Atlas Administration Access Tracking Rolling Index API
  slug: open-mongodb-rolling-index-api
- collection_type: open
  name: MongoDB Atlas Administration Access Tracking Root API
  slug: open-mongodb-root-api
- collection_type: open
  name: MongoDB Atlas Administration Access Tracking Serverless Instances API
  slug: open-mongodb-serverless-instances-api
- collection_type: open
  name: MongoDB Atlas Administration Access Tracking Serverless Private Endpoints API
  slug: open-mongodb-serverless-private-endpoints-api
- collection_type: open
  name: MongoDB Atlas Administration Access Tracking Service Accounts API
  slug: open-mongodb-service-accounts-api
- collection_type: open
  name: MongoDB Atlas Administration Access Tracking Streams API
  slug: open-mongodb-streams-api
- collection_type: open
  name: MongoDB Atlas Administration Access Tracking Teams API
  slug: open-mongodb-teams-api
- collection_type: open
  name: MongoDB Atlas Administration Access Tracking Third-Party Integrations API
  slug: open-mongodb-third-party-integrations-api
- collection_type: open
  name: MongoDB Atlas Administration Access Tracking X.509 Authentication API
  slug: open-mongodb-x-509-authentication-api
common:
- group: commercial
  href: https://artifacts.apis.io/mongodb/finops/mongodb-finops.yml
  title: ''
  type: FinOps
  url: finops/mongodb-finops.yml
- group: design
  href: https://artifacts.apis.io/mongodb/rules/mongodb-rules.yml
  title: ''
  type: Spectral
  url: rules/mongodb-rules.yml
- group: design
  href: https://artifacts.apis.io/mongodb/json-ld/mongodb-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/mongodb-context.jsonld
- group: design
  href: https://artifacts.apis.io/mongodb/vocabulary/mongodb-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/mongodb-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/mongodb/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/mongodb/data-model/mongodb-data-model.yml
  title: ''
  type: DataModel
  url: data-model/mongodb-data-model.yml
- group: build
  href: https://artifacts.apis.io/mongodb/cli/mongodb-cli.yml
  title: ''
  type: CLI
  url: cli/mongodb-cli.yml
- group: operate
  href: https://artifacts.apis.io/mongodb/changelog/mongodb-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/mongodb-changelog.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.mongodb.com/
- group: design
  href: https://artifacts.apis.io/mongodb/errors/mongodb-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/mongodb-problem-types.yml
- group: design
  href: https://artifacts.apis.io/mongodb/conformance/mongodb-conformance.yml
  title: ''
  type: Conformance
  url: conformance/mongodb-conformance.yml
- group: agent
  href: https://artifacts.apis.io/mongodb/llms/mongodb-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/mongodb-llms.txt
- group: agent
  href: https://artifacts.apis.io/mongodb/well-known/mongodb-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/mongodb-well-known.yml
- group: other
  href: https://artifacts.apis.io/mongodb/hosts/mongodb-hosts.yml
  title: ''
  type: Hosts
  url: hosts/mongodb-hosts.yml
- group: other
  href: https://artifacts.apis.io/mongodb/vendors/mongodb-vendors.yml
  title: ''
  type: Vendors
  url: vendors/mongodb-vendors.yml
- group: build
  href: https://artifacts.apis.io/mongodb/packages/mongodb-packages.yml
  title: ''
  type: SDKs
  url: packages/mongodb-packages.yml
- group: build
  href: https://artifacts.apis.io/mongodb/packages/mongodb-packages.yml
  title: ''
  type: Packages
  url: packages/mongodb-packages.yml
- group: auth
  title: ''
  type: Security
  url: https://www.mongodb.com/products/capabilities/security
- group: company
  title: ''
  type: Newsroom
  url: https://www.mongodb.com/company/newsroom
- group: other
  title: ''
  type: Leadership
  url: https://www.mongodb.com/company/leadership
- group: docs
  title: ''
  type: Documentation
  url: https://www.mongodb.com/docs/
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.mongodb.com/docs/manual/release-notes/
- group: docs
  title: ''
  type: APIReference
  url: https://www.mongodb.com/docs/manual/reference/geojson/
- group: start
  title: ''
  type: SignUp
  url: https://www.mongodb.com/cloud/atlas/register
- group: operate
  href: https://artifacts.apis.io/mongodb/rate-limits/mongodb-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/mongodb-rate-limits.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://www.mongodb.com/pricing
- group: commercial
  href: https://artifacts.apis.io/mongodb/plans/mongodb-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/mongodb-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/mongodb/capabilities/mongodb-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/mongodb-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/mongodb/agentic-access/mongodb-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/mongodb-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/mongodb/security/mongodb-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/mongodb-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/mongodb/security/mongodb-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/mongodb-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/mongodb/security/mongodb-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/mongodb-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/mongodb/authentication/mongodb-authentication.yml
  title: ''
  type: Authentication
  url: authentication/mongodb-authentication.yml
- group: auth
  href: https://artifacts.apis.io/mongodb/scopes/mongodb-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/mongodb-scopes.yml
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/mongodb-js/mongodb-mcp-server
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/mongodbinc
- group: company
  title: ''
  type: Website
  url: https://www.mongodb.com
- group: start
  title: ''
  type: GettingStarted
  url: https://www.mongodb.com/docs/atlas/getting-started/
- group: company
  title: ''
  type: Blog
  url: https://www.mongodb.com/blog
- group: operate
  title: ''
  type: Support
  url: https://www.mongodb.com/support
- group: operate
  title: ''
  type: Community
  url: https://www.mongodb.com/community
- group: start
  title: ''
  type: Portal
  url: https://www.mongodb.com/developer/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.mongodb.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.mongodb.com/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.mongodb.com/legal/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/mongodb
- group: agent
  title: ''
  type: AgentSkills
  url: https://github.com/mongodb/agent-skills
- group: design
  title: ''
  type: SpectralRules
  url: https://github.com/mongodb/openapi/blob/e579b1476f09280be945ffc1872c92f5a7e84c61/tools/spectral/.spectral.yaml
created: '2024'
description: MongoDB provides a document‑model database platform that can be deployed on any cloud or on‑premises infrastructure. It offers services such as MongoDB Atlas for multi‑cloud data management, vector search, real‑time operational workloads, and tools like Compass for GUI access. The platform is used by developers and enterprises building applications that require scalable, searchable, and AI‑enabled data handling.
features:
- Atlas M0 Free shared cluster (512 MB, 100 ops/sec)
- Atlas Flex with $8-$30/month capped pricing
- Atlas Dedicated M10+ from ~$0.08/hr ($57/month)
- 'Atlas Serverless: $0.10/M reads, $1.00/M writes, $0.025/GB-month storage'
- Atlas Search and Atlas Vector Search
- Atlas Stream Processing
- Atlas Data Federation across S3 and Atlas
- Atlas Data API and GraphQL API
- Atlas App Services (formerly Realm)
- Atlas Admin API for programmatic cluster management
- Multi-cloud across AWS, Azure, GCP
- Multi-region clusters with global write zones
- BI Connector for SQL access
- Online archive for cold data tiering
- Backups with point-in-time restore
- VPC Peering and Private Endpoints
- LDAP, X.509, and AWS IAM authentication
finops:
- has_sources: true
  method: derived
  name: Mongodb Finops
  primary_unit: hour
  service_category: ''
  slug: mongodb-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mongodb.png
json_schemas:
- name: Acknowledge Alert
  property_count: 4
  slug: mongodb-acknowledge-alert
- name: ActivityFeedLinkResponse
  property_count: 2
  slug: mongodb-activity-feed-link-response
- name: AlertViewForNdsGroup
  property_count: 0
  slug: mongodb-alert-view-for-nds-group
- name: Toggle Request
  property_count: 1
  slug: mongodb-alerts-toggle
- name: ApiAtlasCheckpointView
  property_count: 9
  slug: mongodb-api-atlas-checkpoint-view
- name: ApiAtlasModifyEndpointServiceRequestView
  property_count: 2
  slug: mongodb-api-atlas-modify-endpoint-service-request-view
- name: ApiAtlasNonCompliantResourceView
  property_count: 5
  slug: mongodb-api-atlas-non-compliant-resource-view
- name: ApiAtlasResourcePolicyCreateView
  property_count: 3
  slug: mongodb-api-atlas-resource-policy-create-view
- name: ApiAtlasResourcePolicyEditView
  property_count: 3
  slug: mongodb-api-atlas-resource-policy-edit-view
- name: ApiAtlasResourcePolicyView
  property_count: 10
  slug: mongodb-api-atlas-resource-policy-view
- name: ApiAtlasSnapshotScheduleView
  property_count: 10
  slug: mongodb-api-atlas-snapshot-schedule-view
- name: ApiHostView_Atlas
  property_count: 12
  slug: mongodb-api-host-view-atlas
- name: ApiKeyUserDetails
  property_count: 6
  slug: mongodb-api-key-user-details
- name: ApiMeasurementsGeneralView_Atlas
  property_count: 10
  slug: mongodb-api-measurements-general-view-atlas
- name: ApiSearchDeploymentRequestView
  property_count: 1
  slug: mongodb-api-search-deployment-request-view
- name: ApiSearchDeploymentResponseView
  property_count: 5
  slug: mongodb-api-search-deployment-response-view
- name: AtlasOrganization
  property_count: 5
  slug: mongodb-atlas-organization
- name: Tenant Cluster Upgrade Request
  property_count: 36
  slug: mongodb-atlas-tenant-cluster-upgrade-request20240805
- name: AuditLog
  property_count: 4
  slug: mongodb-audit-log
- name: Federated Authentication Role Mapping
  property_count: 3
  slug: mongodb-auth-federation-role-mapping
- name: AWSCustomDNSEnabledView
  property_count: 1
  slug: mongodb-awscustom-dnsenabled-view
- name: BackupOnlineArchiveCreate
  property_count: 14
  slug: mongodb-backup-online-archive-create
- name: BackupRestoreJob
  property_count: 19
  slug: mongodb-backup-restore-job
- name: BackupSnapshot
  property_count: 12
  slug: mongodb-backup-snapshot
- name: BaseNetworkPeeringConnectionSettings
  property_count: 3
  slug: mongodb-base-network-peering-connection-settings
- name: BillingInvoice
  property_count: 18
  slug: mongodb-billing-invoice
- name: CloudAppUser
  property_count: 13
  slug: mongodb-cloud-app-user
- name: CloudDatabaseUser
  property_count: 14
  slug: mongodb-cloud-database-user
- name: CloudProviderAccessRoleRequest
  property_count: 1
  slug: mongodb-cloud-provider-access-role-request
- name: CloudProviderAccessRoleRequestUpdate
  property_count: 1
  slug: mongodb-cloud-provider-access-role-request-update
- name: CloudProviderAccessRole
  property_count: 1
  slug: mongodb-cloud-provider-access-role
- name: CloudProviderAccessRoles
  property_count: 3
  slug: mongodb-cloud-provider-access-roles
- name: CloudProviderContainer
  property_count: 3
  slug: mongodb-cloud-provider-container
- name: CloudProviderEndpointServiceRequest
  property_count: 4
  slug: mongodb-cloud-provider-endpoint-service-request
- name: CloudSearchMetrics
  property_count: 6
  slug: mongodb-cloud-search-metrics
- name: ClusterDescriptionProcessArgs20240805
  property_count: 16
  slug: mongodb-cluster-description-process-args20240805
- name: ClusterDescription20240805
  property_count: 36
  slug: mongodb-cluster-description20240805
- name: ClusterOutageSimulation
  property_count: 7
  slug: mongodb-cluster-outage-simulation
- name: ClusterSearchIndex
  property_count: 8
  slug: mongodb-cluster-search-index
- name: CollStatsRankedNamespacesView
  property_count: 3
  slug: mongodb-coll-stats-ranked-namespaces-view
- name: ConnectedOrgConfig
  property_count: 8
  slug: mongodb-connected-org-config
- name: Control Plane IP Addresses
  property_count: 2
  slug: mongodb-control-plane-ipaddresses
- name: CostExplorerFilterRequestBody
  property_count: 8
  slug: mongodb-cost-explorer-filter-request-body
- name: CreateAtlasOrganizationApiKey
  property_count: 2
  slug: mongodb-create-atlas-organization-api-key
- name: CreateEndpointRequest
  property_count: 0
  slug: mongodb-create-endpoint-request
- name: CreateOrganizationRequest
  property_count: 6
  slug: mongodb-create-organization-request
- name: CreateOrganizationResponse
  property_count: 6
  slug: mongodb-create-organization-response
- name: CreatePushBasedLogExportProjectRequest
  property_count: 3
  slug: mongodb-create-push-based-log-export-project-request
- name: CustomZoneMappings
  property_count: 1
  slug: mongodb-custom-zone-mappings
- name: Limits
  property_count: 5
  slug: mongodb-data-federation-limit
- name: Data Federation Tenant-Level Query Limit
  property_count: 8
  slug: mongodb-data-federation-tenant-query-limit
- name: Data Lake Pipeline
  property_count: 10
  slug: mongodb-data-lake-ingestion-pipeline
- name: DataLakeTenant
  property_count: 8
  slug: mongodb-data-lake-tenant
- name: DataProtectionSettings20231001
  property_count: 14
  slug: mongodb-data-protection-settings20231001
- name: DatabaseRollingIndexRequest
  property_count: 5
  slug: mongodb-database-rolling-index-request
- name: DiskBackupApiPolicyItem
  property_count: 5
  slug: mongodb-disk-backup-api-policy-item
- name: Replica Set Snapshot
  property_count: 16
  slug: mongodb-disk-backup-replica-set
- name: Sharded Cluster Snapshot
  property_count: 16
  slug: mongodb-disk-backup-sharded-cluster-snapshot
- name: DiskBackupSnapshotRestoreJob
  property_count: 19
  slug: mongodb-disk-backup-snapshot-restore-job
- name: DiskBackupSnapshotSchedule20240805
  property_count: 20
  slug: mongodb-disk-backup-snapshot-schedule20240805
- name: DropIndexSuggestionsResponse
  property_count: 3
  slug: mongodb-drop-index-suggestions-response
- name: Encryption At Rest Private Endpoint
  property_count: 5
  slug: mongodb-earprivate-endpoint
- name: EndpointService
  property_count: 5
  slug: mongodb-endpoint-service
- name: EventViewForNdsGroup
  property_count: 0
  slug: mongodb-event-view-for-nds-group
- name: EventViewForOrg
  property_count: 0
  slug: mongodb-event-view-for-org
- name: FederationIdentityProvider
  property_count: 10
  slug: mongodb-federation-identity-provider
- name: FederationOidcIdentityProvider
  property_count: 14
  slug: mongodb-federation-oidc-identity-provider
- name: FederationOidcIdentityProviderUpdate
  property_count: 9
  slug: mongodb-federation-oidc-identity-provider-update
- name: Create Flex Backup Restore Job
  property_count: 14
  slug: mongodb-flex-backup-restore-job-create20241113
- name: Flex Backup Restore Job
  property_count: 14
  slug: mongodb-flex-backup-restore-job20241113
- name: Flex Backup Snapshot Download Create
  property_count: 2
  slug: mongodb-flex-backup-snapshot-download-create20241113
- name: Flex Backup Snapshot
  property_count: 8
  slug: mongodb-flex-backup-snapshot20241113
- name: Flex Cluster Description Create
  property_count: 5
  slug: mongodb-flex-cluster-description-create20241113
- name: Flex Cluster Description Update
  property_count: 3
  slug: mongodb-flex-cluster-description-update20241113
- name: Flex Cluster Description
  property_count: 14
  slug: mongodb-flex-cluster-description20241113
- name: GeoSharding20240805
  property_count: 3
  slug: mongodb-geo-sharding20240805
- name: GroupAlertsConfig
  property_count: 0
  slug: mongodb-group-alerts-config
- name: GroupInvitation
  property_count: 9
  slug: mongodb-group-invitation
- name: GroupMaintenanceWindow
  property_count: 7
  slug: mongodb-group-maintenance-window
- name: GroupMigrationRequest
  property_count: 3
  slug: mongodb-group-migration-request
- name: GroupPaginatedEventView
  property_count: 3
  slug: mongodb-group-paginated-event-view
- name: Group
  property_count: 9
  slug: mongodb-group
- name: GroupServiceAccount
  property_count: 6
  slug: mongodb-group-service-account
- name: GroupSettings
  property_count: 10
  slug: mongodb-group-settings
- name: GroupUserRequest
  property_count: 2
  slug: mongodb-group-user-request
- name: GroupUserResponse
  property_count: 4
  slug: mongodb-group-user-response
- name: Data Lake Pipeline Run
  property_count: 13
  slug: mongodb-ingestion-pipeline-run
- name: LDAPVerifyConnectivityJobRequestParams
  property_count: 7
  slug: mongodb-ldapverify-connectivity-job-request-params
- name: LDAPVerifyConnectivityJobRequest
  property_count: 6
  slug: mongodb-ldapverify-connectivity-job-request
- name: Cluster Description
  property_count: 44
  slug: mongodb-legacy-atlas-cluster
- name: Tenant Cluster Upgrade Request
  property_count: 44
  slug: mongodb-legacy-atlas-tenant-cluster-upgrade-request
- name: LiveImportAvailableProject
  property_count: 4
  slug: mongodb-live-import-available-project
- name: LiveImportValidation
  property_count: 5
  slug: mongodb-live-import-validation
- name: LiveMigrationRequest20240530
  property_count: 7
  slug: mongodb-live-migration-request20240530
- name: LiveMigrationResponse
  property_count: 5
  slug: mongodb-live-migration-response
- name: Log Export Integration Request
  property_count: 2
  slug: mongodb-log-integration-request
- name: Log Integration Response
  property_count: 3
  slug: mongodb-log-integration-response
- name: ManagedNamespaces
  property_count: 7
  slug: mongodb-managed-namespaces
- name: MatcherFieldView
  property_count: 0
  slug: mongodb-matcher-field-view
- name: MeasurementsCollStatsLatencyCluster
  property_count: 11
  slug: mongodb-measurements-coll-stats-latency-cluster
- name: MeasurementsCollStatsLatencyHost
  property_count: 9
  slug: mongodb-measurements-coll-stats-latency-host
- name: MeasurementsIndexes
  property_count: 10
  slug: mongodb-measurements-indexes
- name: MeasurementsNonIndex
  property_count: 8
  slug: mongodb-measurements-non-index
- name: MongoDBAccessLogsList
  property_count: 1
  slug: mongodb-mongo-dbaccess-logs-list
- name: NamespacesRequest
  property_count: 1
  slug: mongodb-namespaces-request
- name: Namespaces
  property_count: 1
  slug: mongodb-namespaces
- name: NetworkPermissionEntry
  property_count: 7
  slug: mongodb-network-permission-entry
- name: NetworkPermissionEntryStatus
  property_count: 1
  slug: mongodb-network-permission-entry-status
- name: Organization Federation Settings
  property_count: 5
  slug: mongodb-org-federation-settings
- name: OrgPaginatedEventView
  property_count: 3
  slug: mongodb-org-paginated-event-view
- name: OrgServiceAccountRequest
  property_count: 4
  slug: mongodb-org-service-account-request
- name: OrgServiceAccount
  property_count: 6
  slug: mongodb-org-service-account
- name: OrgUserResponse
  property_count: 5
  slug: mongodb-org-user-response
- name: OrganizationInvitationRequest
  property_count: 4
  slug: mongodb-organization-invitation-request
- name: OrganizationInvitation
  property_count: 11
  slug: mongodb-organization-invitation
- name: OrganizationSettings
  property_count: 8
  slug: mongodb-organization-settings
- name: PaginatedAlertConfigView
  property_count: 3
  slug: mongodb-paginated-alert-config-view
- name: PaginatedAlertView
  property_count: 3
  slug: mongodb-paginated-alert-view
- name: PaginatedApiApiUserView
  property_count: 3
  slug: mongodb-paginated-api-api-user-view
- name: PaginatedApiAtlasCheckpointView
  property_count: 3
  slug: mongodb-paginated-api-atlas-checkpoint-view
- name: PaginatedApiAtlasDatabaseUserView
  property_count: 3
  slug: mongodb-paginated-api-atlas-database-user-view
- name: PaginatedApiAtlasFlexBackupRestoreJob20241113View
  property_count: 3
  slug: mongodb-paginated-api-atlas-flex-backup-restore-job20241113-view
- name: PaginatedApiAtlasFlexBackupSnapshot20241113View
  property_count: 3
  slug: mongodb-paginated-api-atlas-flex-backup-snapshot20241113-view
- name: PaginatedApiInvoiceMetadataView
  property_count: 3
  slug: mongodb-paginated-api-invoice-metadata-view
- name: PaginatedApiInvoiceView
  property_count: 3
  slug: mongodb-paginated-api-invoice-view
- name: PaginatedApiSKUView
  property_count: 3
  slug: mongodb-paginated-api-skuview
- name: PaginatedApiUserAccessListResponseView
  property_count: 3
  slug: mongodb-paginated-api-user-access-list-response-view
- name: PaginatedBackupSnapshotView
  property_count: 3
  slug: mongodb-paginated-backup-snapshot-view
- name: Network Peering
  property_count: 3
  slug: mongodb-paginated-cloud-provider-container-view
- name: PaginatedContainerPeerView
  property_count: 3
  slug: mongodb-paginated-container-peer-view
- name: PaginatedDiskPartitionView
  property_count: 3
  slug: mongodb-paginated-disk-partition-view
- name: PaginatedEventTypeDetailsResponse
  property_count: 3
  slug: mongodb-paginated-event-type-details-response
- name: PaginatedFlexClusters20241113
  property_count: 3
  slug: mongodb-paginated-flex-clusters20241113
- name: PaginatedGroupUserView
  property_count: 3
  slug: mongodb-paginated-group-user-view
- name: PaginatedLogIntegrationResponse
  property_count: 3
  slug: mongodb-paginated-log-integration-response
- name: PaginatedNetworkAccessView
  property_count: 3
  slug: mongodb-paginated-network-access-view
- name: PaginatedOrgUserView
  property_count: 3
  slug: mongodb-paginated-org-user-view
- name: PaginatedPipelineRunView
  property_count: 3
  slug: mongodb-paginated-pipeline-run-view
- name: PaginatedPrivateNetworkEndpointIdEntryView
  property_count: 3
  slug: mongodb-paginated-private-network-endpoint-id-entry-view
- name: PaginatedPublicApiUsageDetailsLineItemView
  property_count: 3
  slug: mongodb-paginated-public-api-usage-details-line-item-view
- name: PaginatedQueryShapes
  property_count: 3
  slug: mongodb-paginated-query-shapes
- name: PaginatedRateLimitEndpointSets
  property_count: 3
  slug: mongodb-paginated-rate-limit-endpoint-sets
- name: PaginatedRestoreJobView
  property_count: 3
  slug: mongodb-paginated-restore-job-view
- name: PaginatedServerlessInstanceDescriptionView
  property_count: 3
  slug: mongodb-paginated-serverless-instance-description-view
- name: PerformanceAdvisorResponse
  property_count: 2
  slug: mongodb-performance-advisor-response
- name: PerformanceAdvisorSlowQueryList
  property_count: 1
  slug: mongodb-performance-advisor-slow-query-list
- name: PinnedNamespaces
  property_count: 3
  slug: mongodb-pinned-namespaces
- name: PrivateIPModeView
  property_count: 1
  slug: mongodb-private-ipmode-view
- name: PrivateLinkEndpoint
  property_count: 3
  slug: mongodb-private-link-endpoint
- name: PrivateNetworkEndpointIdEntry
  property_count: 10
  slug: mongodb-private-network-endpoint-id-entry
- name: ProjectSettingItemView
  property_count: 1
  slug: mongodb-project-setting-item-view
- name: PushBasedLogExportProject
  property_count: 6
  slug: mongodb-push-based-log-export-project
- name: QueryShapeResponse
  property_count: 5
  slug: mongodb-query-shape-response
- name: QueryShapeUpdateRequest
  property_count: 1
  slug: mongodb-query-shape-update-request
- name: QueryStatsDetailsResponse
  property_count: 3
  slug: mongodb-query-stats-details-response
- name: QueryStatsSummaryListResponse
  property_count: 1
  slug: mongodb-query-stats-summary-list-response
- name: RateLimitEndpointSetResponse
  property_count: 7
  slug: mongodb-rate-limit-endpoint-set-response
- name: RequestAccepted
  property_count: 0
  slug: mongodb-request-accepted
- name: SampleDatasetStatus
  property_count: 6
  slug: mongodb-sample-dataset-status
- name: SchemaAdvisorResponse
  property_count: 1
  slug: mongodb-schema-advisor-response
- name: SearchIndexCreateRequest
  property_count: 4
  slug: mongodb-search-index-create-request
- name: Search Index Response
  property_count: 10
  slug: mongodb-search-index-response
- name: Search Index Update Request
  property_count: 1
  slug: mongodb-search-index-update-request
- name: ServerlessBackupRestoreJob
  property_count: 17
  slug: mongodb-serverless-backup-restore-job
- name: Serverless Instance Description
  property_count: 12
  slug: mongodb-serverless-instance-description
- name: ServerlessTenantCreateRequest
  property_count: 1
  slug: mongodb-serverless-tenant-create-request
- name: ServerlessTenantEndpoint
  property_count: 6
  slug: mongodb-serverless-tenant-endpoint
- name: ServerlessTenantEndpointUpdate
  property_count: 2
  slug: mongodb-serverless-tenant-endpoint-update
- name: ServiceAccountIPAccessListEntry
  property_count: 6
  slug: mongodb-service-account-ipaccess-list-entry
- name: ServiceAccountSecret
  property_count: 6
  slug: mongodb-service-account-secret
- name: SystemStatus
  property_count: 5
  slug: mongodb-system-status
- name: TargetOrgRequest
  property_count: 1
  slug: mongodb-target-org-request
- name: TargetOrg
  property_count: 1
  slug: mongodb-target-org
- name: TriggerIngestionPipelineRequest
  property_count: 2
  slug: mongodb-trigger-ingestion-pipeline-request
- name: UpdateCustomDBRole
  property_count: 2
  slug: mongodb-update-custom-dbrole
- name: UserAccessListRequest
  property_count: 2
  slug: mongodb-user-access-list-request
- name: UserAccessListResponse
  property_count: 7
  slug: mongodb-user-access-list-response
- name: UserCustomDBRole
  property_count: 3
  slug: mongodb-user-custom-dbrole
- name: UserSecurity
  property_count: 3
  slug: mongodb-user-security
jsonld:
- class_count: 120
  name: Mongodb Context
  property_count: 59
  slug: mongodb-context
layout: provider
mcp_servers:
- description: MongoDB MCP Server for natural-language queries, aggregations, and Atlas management; runs via npx with connection-string or Atlas API auth and read-only / disabled-tools flags.
  name: MCP Server
  slug: mcp-server
- description: Remote MCP server at mcp.mongodb.com over HTTP.
  name: MongoDB MCP Server
  slug: mongodb
modified: '2026-09-16'
name: MongoDB
nav: Providers
network: true
overview: 'MongoDB publishes 58 API contracts indexed on the [APIs.io](https://apis.io/) network, including Access Tracking API, Activity Feed API, Alert Configurations API, and 55 more. Tagged areas include Cloud Database, Database, Document Database, NoSQL, and MongoDB.


  The MongoDB catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  MongoDB''s developer surface includes CLI, changelog, documentation, API reference, signup flow, pricing, authentication, and 41 more developer resources.'
plans:
- name: Mongodb Plans Pricing
  plan_count: 6
  slug: mongodb-plans-pricing
- name: Mongodb Price Estimates
  plan_count: 1
  slug: mongodb-price-estimates
random_paper: 22
rate_limits:
- limit_count: 12
  name: Mongodb Rate Limits
  slug: mongodb-rate-limits
rules:
- authorship: provider
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: MongoDB — openapi rules
  rule_count: 10
  severity_counts:
    error: 10
    hint: 0
    info: 0
    warn: 0
  slug: mongodb-openapi-spectral-rules
- authorship: generated
  effective_rule_count: 59
  extends:
  - spectral:oas
  name: MongoDB API Rules
  rule_count: 18
  severity_counts:
    error: 14
    hint: 0
    info: 1
    warn: 3
  slug: mongodb-rules
scopes:
- name: Mongodb Scopes
  scope_count: 1
  slug: mongodb-scopes
  summary_line: 1 scope · clientCredentials
score:
  band: exemplar
  composite: 77.8
  coverage:
    artifact_dirs: 32
    catalog_earned: 89.8
    catalog_earned_first_party: 24.0
    catalog_gap: 25.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.8
  facets:
    access_clarity: 96.1
    contract_governance: 22.0
    contract_quality: 68.7
    developer_ergonomics: 69.6
    discoverability: 83.3
    operational_transparency: 71.1
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 80.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 56
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 42.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 38.9
screenshot: https://apis.io/screenshots/mongodb/mongodb-2026-06-20T185729.png
security:
- kind: authentication
  name: Mongodb Authentication
  slug: mongodb-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Mongodb Domain Security
  slug: mongodb-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Mongodb Vulnerability Disclosure
  slug: mongodb-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Mongodb Trust Center
  slug: mongodb-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, PCI DSS, HIPAA, FedRAMP, GDPR, CSA STAR
skill_count: 8
skills:
- name: mongodb-atlas-stream-processing
  slug: mongodb-atlas-stream-processing
- name: mongodb-connection
  slug: mongodb-connection
- name: mongodb-mcp-setup
  slug: mongodb-mcp-setup
- name: mongodb-natural-language-querying
  slug: mongodb-natural-language-querying
- name: mongodb-query-optimizer
  slug: mongodb-query-optimizer
- name: mongodb-schema-design
  slug: mongodb-schema-design
- name: mongodb-search-and-ai
  slug: mongodb-search-and-ai
- name: review-skill
  slug: review-skill
slug: mongodb
tags:
- Cloud Database
- Database
- Document Database
- NoSQL
- MongoDB
website: https://www.mongodb.com
---
