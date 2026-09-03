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
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 44.8
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 240
  human_in_the_loop: 9
  name: Mongodb Agentic Access
  operation_count: 468
  slug: mongodb-agentic-access
  summary_line: 468 operations · 240 acting · 9 human-in-the-loop
api_count: 1
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
  name: MongoDB MongoDB Cloud Users API
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
artifact_total: 141
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
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
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/mongodb-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/mongodb-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/mongodb-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/mongodb-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mongodb-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/mongodb-authentication.yml
- group: auth
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
created: '2024'
description: MongoDB is a source-available cross-platform document-oriented database program. Classified as a NoSQL database, MongoDB uses JSON-like documents with optional schemas.
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
- name: Mongodb Finops
  service_category: Database-as-a-Service
  slug: mongodb-finops
graphqls:
- description: ''
  name: MongoDB GraphQL API
  slug: mongodb-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mongodb.png
layout: provider
mcp_servers:
- description: MongoDB MCP Server for natural-language queries, aggregations, and Atlas management; runs via npx with connection-string or Atlas API auth and read-only / disabled-tools flags.
  name: MCP Server
  slug: mcp-server
modified: '2026-05-19'
name: MongoDB
nav: Providers
network: true
overview: 'MongoDB publishes 51 APIs on the [APIs.io](https://apis.io/) network, including Access Tracking API, Activity Feed API, Alert Configurations API, and 48 more. Tagged areas include Cloud Database, Database, Document Database, and NoSQL.


  MongoDB''s developer surface includes authentication, getting-started guide, engineering blog, support, developer portal, and 15 more developer resources.'
plans:
- name: Mongodb Plans Pricing
  plan_count: 4
  slug: mongodb-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 5
  name: Mongodb Rate Limits
  slug: mongodb-rate-limits
scopes:
- name: Mongodb Scopes
  scope_count: 0
  slug: mongodb-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 46.1
  coverage:
    artifact_dirs: 14
    catalog_gap: 82.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 0.0
    contract_quality: 60.5
    developer_ergonomics: 57.1
    discoverability: 51.9
    governance: 0.0
    operational_transparency: 42.1
  previous_composite: 46.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 51
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mongodb/refs/heads/main/screenshots/mongodb-2026-06-20T185729.png
security:
- kind: authentication
  name: Mongodb Authentication
  slug: mongodb-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Mongodb Domain Security
  slug: mongodb-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Mongodb Vulnerability Disclosure
  slug: mongodb-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
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
website: https://www.mongodb.com
---
