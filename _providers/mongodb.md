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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: partial
    rate_limit_signal: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 59.5
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 240
  human_in_the_loop: 9
  name: Mongodb Agentic Access
  operation_count: 468
  slug: mongodb-agentic-access
  summary_line: 468 operations · 240 acting · 9 human-in-the-loop
api_count: 53
apis:
- description: The Atlas Data API lets you read and write data in MongoDB Atlas with standard HTTPS requests, without the need for a MongoDB driver.
  name: MongoDB Atlas Data API
  slug: mongodb-atlas-data-api
- description: Admin API for MongoDB Atlas App Services (formerly Realm), used to manage applications, services, functions, and triggers.
  name: MongoDB Atlas App Services Admin API
  slug: mongodb-atlas-app-services-admin-api
- description: Returns access logs for authentication attempts made to Atlas database deployments. To view database access history, you must have either the Project Owner or Organization Owner role.
  name: MongoDB Access Tracking API
  slug: mongodb-access-tracking-api
- description: Returns pre-filtered activity feed links for projects and organizations. The returned links can be shared and opened to view the activity feed with the specified filters applied.
  name: MongoDB Activity Feed API
  slug: mongodb-activity-feed-api
- description: Returns and edits the conditions that trigger alerts and how MongoDB Cloud notifies users. This collection remains under revision and may change.
  name: MongoDB Alert Configurations API
  slug: mongodb-alert-configurations-api
- description: Returns and acknowledges alerts that MongoDB Cloud triggers based on the alert conditions that you define. This collection remains under revision and may change.
  name: MongoDB Alerts API
  slug: mongodb-alerts-api
- description: Returns, adds, edits, and removes Atlas Search indexes for the specified cluster. Also returns and updates user-defined analyzers for the specified cluster.
  name: MongoDB Atlas Search API
  slug: mongodb-atlas-search-api
- description: Returns and edits database auditing settings for MongoDB Cloud projects.
  name: MongoDB Auditing API
  slug: mongodb-auditing-api
- description: Returns and edits custom DNS configurations for MongoDB Cloud database deployments on AWS. The resource requires your Project ID. If you use the VPC peering on AWS and you use your own DNS servers ins
  name: MongoDB AWS Clusters DNS API
  slug: mongodb-aws-clusters-dns-api
- description: Manages Cloud Backup snapshots, snapshot export buckets, restore jobs, and schedules. This resource applies only to clusters that use Cloud Backups.
  name: MongoDB Cloud Backups API
  slug: mongodb-cloud-backups-api
- description: Manages the Cloud Migration Service. Source organizations, projects, and MongoDB clusters reside on Cloud Manager or Ops Manager. Destination organizations, projects, and MongoDB clusters reside on Mo
  name: MongoDB Cloud Migration Service API
  slug: mongodb-cloud-migration-service-api
- description: Returns, adds, authorizes, and removes AWS IAM roles in Atlas.
  name: MongoDB Cloud Provider Access API
  slug: mongodb-cloud-provider-access-api
- description: Returns, starts, or ends a cluster outage simulation.
  name: MongoDB Cluster Outage Simulation API
  slug: mongodb-cluster-outage-simulation-api
- description: Returns, adds, edits, and removes database deployments. Changes to cluster configurations can affect costs. This resource requires your Project ID.
  name: MongoDB Clusters API
  slug: mongodb-clusters-api
- description: Returns, adds, and edits pinned namespaces for the specified cluster or process. Also returns collection level latency metric data.
  name: MongoDB Collection Level Metrics API
  slug: mongodb-collection-level-metrics-api
- description: Returns, adds, edits, and removes custom database user privilege roles. Use custom roles to specify custom sets of actions that the MongoDB Cloud built-in roles can't describe. You define custom roles
  name: MongoDB Custom Database Roles API
  slug: mongodb-custom-database-roles-api
- description: Returns, adds, edits, and removes Federated Database Instances. This resource requires your project ID. Changes to federated database instance configurations can affect costs.
  name: MongoDB Data Federation API
  slug: mongodb-data-federation-api
- description: Returns, edits, and removes Atlas Data Lake Pipelines and associated runs.
  name: MongoDB Data Lake Pipelines API
  slug: mongodb-data-lake-pipelines-api
- description: Returns, adds, edits, and removes database users.
  name: MongoDB Database Users API
  slug: mongodb-database-users-api
- description: Returns and edits the Encryption at Rest using Customer Key Management configuration. MongoDB Cloud encrypts all storage whether or not you use your own key management.
  name: MongoDB Encryption at Rest using Customer Key Management API
  slug: mongodb-encryption-at-rest-using-customer-key-management-api
- description: Returns events. This collection remains under revision and may change.
  name: MongoDB Events API
  slug: mongodb-events-api
- description: Returns, adds, edits, and removes federation-related features such as role mappings and connected organization configurations.
  name: MongoDB Federated Authentication API
  slug: mongodb-federated-authentication-api
- description: Returns, adds, edits, and removes flex clusters.
  name: MongoDB Flex Clusters API
  slug: mongodb-flex-clusters-api
- description: Returns and adds restore jobs for flex database deployments.
  name: MongoDB Flex Restore Jobs API
  slug: mongodb-flex-restore-jobs-api
- description: Returns and requests to download flex database deployment snapshots.
  name: MongoDB Flex Snapshots API
  slug: mongodb-flex-snapshots-api
- description: Returns, adds, and removes Global Cluster managed namespaces and custom zone mappings. Each collection in a Global Cluster is associated with a managed namespace. When you create a managed namespace f
  name: MongoDB Global Clusters API
  slug: mongodb-global-clusters-api
- description: Returns invoices.
  name: MongoDB Invoices API
  slug: mongodb-invoices-api
- description: Returns, edits, verifies, and removes LDAP configurations. An LDAP configuration defines settings for MongoDB Cloud to connect to your LDAP server over TLS for user authentication and authorization. Y
  name: MongoDB LDAP Configuration API
  slug: mongodb-ldap-configuration-api
- description: Manages Legacy Backup snapshots, restore jobs, schedules and checkpoints.
  name: MongoDB Legacy Backup API
  slug: mongodb-legacy-backup-api
- description: Returns, edits, and removes maintenance windows. The maintenance procedure that MongoDB Cloud performs requires at least one replica set election during the maintenance window per replica set. You can
  name: MongoDB Maintenance Windows API
  slug: mongodb-maintenance-windows-api
- description: Returns, adds, and edits MongoDB Cloud users.
  name: MongoDB MongoDB Cloud Users API
  slug: mongodb-mongodb-cloud-users-api
- description: Returns database deployment monitoring and logging data.
  name: MongoDB Monitoring and Logs API
  slug: mongodb-monitoring-and-logs-api
- description: 'Returns, adds, edits, and removes network peering containers and peering connections. When you deploy an M10+ dedicated cluster, Atlas creates a VPC for the selected provider and region or regions if '
  name: MongoDB Network Peering API
  slug: mongodb-network-peering-api
- description: Returns, adds, edits, or removes an online archive.
  name: MongoDB Online Archive API
  slug: mongodb-online-archive-api
- description: Returns, adds, and edits organizational units in MongoDB Cloud.
  name: MongoDB Organizations API
  slug: mongodb-organizations-api
- description: Returns suggested indexes and slow query data for a database deployment. Also enables or disables MongoDB Cloud-managed slow operation thresholds. To view field values in a sample query, you must have
  name: MongoDB Performance Advisor API
  slug: mongodb-performance-advisor-api
- description: Returns, adds, edits, and removes private endpoint services.
  name: MongoDB Private Endpoint Services API
  slug: mongodb-private-endpoint-services-api
- description: 'Returns, adds, edits, and removes access tokens to use the MongoDB Cloud API. MongoDB Cloud applies these keys to organizations. These resources can return, assign, or revoke use of these keys within '
  name: MongoDB Programmatic API Keys API
  slug: mongodb-programmatic-api-keys-api
- description: Returns, adds, edits, and removes network access limits to database deployments in Atlas. This resource replaces the whitelist resource. Atlas removed whitelists in July 2021. Update your applications
  name: MongoDB Project IP Access List API
  slug: mongodb-project-ip-access-list-api
- description: Returns, adds, and edits collections of clusters and users in MongoDB Cloud.
  name: MongoDB Projects API
  slug: mongodb-projects-api
- description: You can continually export mongod, mongos, and audit logs to an AWS S3 bucket. The new `/logIntegrations` API provides 1-minute log export on a best-effort basis. The existing `/pushBasedLogExport` AP
  name: MongoDB Push-Based Log Export API
  slug: mongodb-push-based-log-export-api
- description: The Query Shape Insights API from MongoDB — 4 operation(s) for query shape insights.
  name: MongoDB Query Shape Insights API
  slug: mongodb-query-shape-insights-api
- description: Returns details about rate limit policies for the Atlas Administration API.
  name: MongoDB Rate Limiting API
  slug: mongodb-rate-limiting-api
- description: Configure and manage Atlas Resource Policies within your organization.
  name: MongoDB Resource Policies API
  slug: mongodb-resource-policies-api
- description: Creates one index to a database deployment in a rolling manner. Rolling indexes build indexes on the applicable nodes sequentially and may reduce the performance impact of an index build if your deplo
  name: MongoDB Rolling Index API
  slug: mongodb-rolling-index-api
- description: Returns details that describe the MongoDB Cloud build and the access token that requests this resource. This starts the MongoDB Cloud API.
  name: MongoDB Root API
  slug: mongodb-root-api
- description: Returns, adds, edits, and removes serverless instances.
  name: MongoDB Serverless Instances API
  slug: mongodb-serverless-instances-api
- description: Returns, adds, edits, and removes private endpoints for serverless instances. To learn more, see the Atlas Administration API tab on the following tutorial.
  name: MongoDB Serverless Private Endpoints API
  slug: mongodb-serverless-private-endpoints-api
- description: Endpoints for managing Service Accounts and secrets. Service Accounts are used for programmatic access to the Atlas Admin API through the OAuth 2.0 Client Credentials flow.
  name: MongoDB Service Accounts API
  slug: mongodb-service-accounts-api
- description: Returns, adds, edits, and removes Streams Workspaces. This resource requires your project ID.
  name: MongoDB Streams API
  slug: mongodb-streams-api
- description: Returns, adds, edits, or removes teams.
  name: MongoDB Teams API
  slug: mongodb-teams-api
- description: 'Returns, adds, edits, and removes third-party service integration configurations. MongoDB Cloud sends alerts to each third-party service that you configure. **IMPORTANT**: Each project can only have o'
  name: MongoDB Third-Party Integrations API
  slug: mongodb-third-party-integrations-api
- description: Returns, edits, and removes user-managed X.509 configurations. Also returns and generates MongoDB Cloud-managed X.509 certificates for database users. The following resources help manage database user
  name: MongoDB X.509 Authentication API
  slug: mongodb-x-509-authentication-api
artifact_total: 89
common:
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


  MongoDB''s developer surface includes authentication, getting-started guide, engineering blog, support, developer portal, and 14 more developer resources.'
plans:
- name: Mongodb Plans Pricing
  plan_count: 4
  slug: mongodb-plans-pricing
random_paper: 64
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
  composite: 49.8
  delta: 0.0
  facets:
    commercial_clarity: 68.4
    contract_quality: 57.5
    developer_ergonomics: 45.7
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 52.6
  previous_composite: 49.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 51
  schema_version: 0.9.1
  scored_at: '2026-08-06'
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
