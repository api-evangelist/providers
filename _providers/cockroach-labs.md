---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: true
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
    error_semantics: derived
    event_surface_described: derived
    idempotency: verified
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: mostly
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 46.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 121
  human_in_the_loop: 7
  name: Cockroach Labs Agentic Access
  operation_count: 212
  slug: cockroach-labs-agentic-access
  summary_line: 212 operations · 121 acting · 7 human-in-the-loop
api_count: 3
apis:
- baseURL: https://cockroachlabs.cloud
  baseurl_source: declared
  description: Authenticate to the Cluster API by creating and terminating API sessions. Session tokens are passed via the X-Cockroach-API-Session header on subsequent requests.
  name: Cockroach Labs Auth API
  slug: cockroach-labs-auth-api
- baseURL: https://cockroachlabs.cloud
  baseurl_source: declared
  description: Retrieve invoices and billing information for the CockroachDB Cloud organization.
  name: Cockroach Labs Billing API
  slug: cockroach-labs-billing-api
- baseURL: https://cockroachlabs.cloud
  baseurl_source: declared
  description: Create, list, retrieve, update, and delete CockroachDB Serverless and Dedicated clusters within an organization.
  name: Cockroach Labs Clusters API
  slug: cockroach-labs-clusters-api
- baseURL: https://cockroachlabs.cloud
  baseurl_source: declared
  description: Manage customer-managed encryption keys (CMEK) for encrypting cluster data at rest using customer-controlled keys.
  name: Cockroach Labs CMEK API
  slug: cockroach-labs-cmek-api
- baseURL: https://cockroachlabs.cloud
  baseurl_source: declared
  description: Manage databases within a CockroachDB cluster, including creation, listing, updating, and deletion.
  name: Cockroach Labs Databases API
  slug: cockroach-labs-databases-api
- baseURL: https://cockroachlabs.cloud
  baseurl_source: declared
  description: Configure egress traffic rules and egress private endpoints for outbound cluster network traffic.
  name: Cockroach Labs EgressRules API
  slug: cockroach-labs-egressrules-api
- baseURL: https://cockroachlabs.cloud
  baseurl_source: declared
  description: Organize clusters and other resources into hierarchical folder structures within the organization.
  name: Cockroach Labs Folders API
  slug: cockroach-labs-folders-api
- baseURL: https://cockroachlabs.cloud
  baseurl_source: declared
  description: Check the health and readiness of individual CockroachDB nodes. The health endpoint can report whether the node is live and fully operational for accepting SQL connections.
  name: Cockroach Labs Health API
  slug: cockroach-labs-health-api
- baseURL: https://cockroachlabs.cloud
  baseurl_source: declared
  description: Configure IP allowlist entries to control network access to a cluster.
  name: Cockroach Labs IPAllowlists API
  slug: cockroach-labs-ipallowlists-api
- baseURL: https://cockroachlabs.cloud
  baseurl_source: declared
  description: Manage JWT issuer configurations for external identity provider integrations.
  name: Cockroach Labs JWTIssuers API
  slug: cockroach-labs-jwtissuers-api
- baseURL: https://cockroachlabs.cloud
  baseurl_source: declared
  description: Configure log export to external destinations such as AWS CloudWatch or GCP Cloud Logging.
  name: Cockroach Labs LogExport API
  slug: cockroach-labs-logexport-api
- baseURL: https://cockroachlabs.cloud
  baseurl_source: declared
  description: Configure metric export integrations including AWS CloudWatch, Datadog, and Prometheus.
  name: Cockroach Labs MetricExport API
  slug: cockroach-labs-metricexport-api
- baseURL: https://cockroachlabs.cloud
  baseurl_source: declared
  description: Retrieve information about all nodes in the cluster, including their status, address, locality, and operational metrics.
  name: Cockroach Labs Nodes API
  slug: cockroach-labs-nodes-api
- baseURL: https://cockroachlabs.cloud
  baseurl_source: declared
  description: Retrieve information about the caller's CockroachDB Cloud organization.
  name: Cockroach Labs Organizations API
  slug: cockroach-labs-organizations-api
- baseURL: https://cockroachlabs.cloud
  baseurl_source: declared
  description: List and inspect range information for the cluster, including hot ranges by node and detailed information for specific range IDs.
  name: Cockroach Labs Ranges API
  slug: cockroach-labs-ranges-api
- baseURL: https://cockroachlabs.cloud
  baseurl_source: declared
  description: Retrieve alerting rules templates for use with Prometheus-compatible alerting systems.
  name: Cockroach Labs Rules API
  slug: cockroach-labs-rules-api
- baseURL: https://cockroachlabs.cloud
  baseurl_source: declared
  description: List active SQL sessions across all nodes of the cluster, with optional filtering by username.
  name: Cockroach Labs Sessions API
  slug: cockroach-labs-sessions-api
- baseURL: https://cockroachlabs.cloud
  baseurl_source: declared
  description: Manage SQL users for a cluster, including creating users, listing users, and updating SQL user passwords.
  name: Cockroach Labs SQLUsers API
  slug: cockroach-labs-sqlusers-api
- baseURL: https://cockroachlabs.cloud
  baseurl_source: declared
  description: Manage cluster version deferral policies to delay automatic CockroachDB version upgrades.
  name: Cockroach Labs VersionDeferral API
  slug: cockroach-labs-versiondeferral-api
- baseURL: https://cockroachlabs.cloud
  baseurl_source: declared
  description: Manage API keys for programmatic access, including creation, retrieval, listing, updating, and deletion.
  name: Cockroach Labs API Keys API
  slug: cockroach-labs-api-keys-api
- baseURL: https://cockroachlabs.cloud
  baseurl_source: declared
  description: Retrieve audit log events for the organization to support compliance and security investigations.
  name: Cockroach Labs Audit Logs API
  slug: cockroach-labs-audit-logs-api
- baseURL: https://cockroachlabs.cloud
  baseurl_source: declared
  description: Manage cluster backups, backup configurations, and restore operations for CockroachDB clusters.
  name: Cockroach Labs Backup Restore API
  slug: cockroach-labs-backup-restore-api
- baseURL: https://cockroachlabs.cloud
  baseurl_source: declared
  description: Configure maintenance windows and blackout periods for cluster upgrade scheduling.
  name: Cockroach Labs Maintenance Windows API
  slug: cockroach-labs-maintenance-windows-api
- baseURL: https://cockroachlabs.cloud
  baseurl_source: declared
  description: Manage role-based access control, including assigning and removing roles for users across organization, folder, and cluster scopes.
  name: Cockroach Labs Role Management API
  slug: cockroach-labs-role-management-api
- baseURL: https://cockroachlabs.cloud
  baseurl_source: declared
  description: Manage service accounts used for machine-to-machine authentication within the organization.
  name: Cockroach Labs Service Accounts API
  slug: cockroach-labs-service-accounts-api
- baseURL: https://cockroachlabs.cloud
  baseurl_source: declared
  description: The Blackout Windows API from Cockroach Labs — 2 operation(s) for blackout windows.
  name: Cockroach Labs Blackout Windows API
  slug: cockroach-labs-blackout-windows-api
- baseURL: https://cockroachlabs.cloud
  baseurl_source: declared
  description: The Client CA Certificates API from Cockroach Labs — 1 operation(s) for client ca certificates.
  name: Cockroach Labs Client CA Certificates API
  slug: cockroach-labs-client-ca-certificates-api
- baseURL: https://cockroachlabs.cloud
  baseurl_source: declared
  description: The Cluster Disruption API from Cockroach Labs — 1 operation(s) for cluster disruption.
  name: Cockroach Labs Cluster Disruption API
  slug: cockroach-labs-cluster-disruption-api
- baseURL: https://cockroachlabs.cloud
  baseurl_source: declared
  description: The Customer-managed Encryption Keys API from Cockroach Labs — 1 operation(s) for customer-managed encryption keys.
  name: Cockroach Labs Customer-managed Encryption Keys API
  slug: cockroach-labs-customer-managed-encryption-keys-api
- baseURL: https://cockroachlabs.cloud
  baseurl_source: declared
  description: The Egress Private Endpoints API from Cockroach Labs — 3 operation(s) for egress private endpoints.
  name: Cockroach Labs Egress Private Endpoints API
  slug: cockroach-labs-egress-private-endpoints-api
- baseURL: https://cockroachlabs.cloud
  baseurl_source: declared
  description: The Egress Rules API from Cockroach Labs — 3 operation(s) for egress rules.
  name: Cockroach Labs Egress Rules API
  slug: cockroach-labs-egress-rules-api
- baseURL: https://cockroachlabs.cloud
  baseurl_source: declared
  description: The IP Allowlists API from Cockroach Labs — 2 operation(s) for ip allowlists.
  name: Cockroach Labs IP Allowlists API
  slug: cockroach-labs-ip-allowlists-api
- baseURL: https://cockroachlabs.cloud
  baseurl_source: declared
  description: The JWT Issuers API from Cockroach Labs — 2 operation(s) for jwt issuers.
  name: Cockroach Labs JWT Issuers API
  slug: cockroach-labs-jwt-issuers-api
- baseURL: https://cockroachlabs.cloud
  baseurl_source: declared
  description: The Log Export API from Cockroach Labs — 1 operation(s) for log export.
  name: Cockroach Labs Log Export API
  slug: cockroach-labs-log-export-api
- baseURL: https://cockroachlabs.cloud
  baseurl_source: declared
  description: The Metric Export API from Cockroach Labs — 3 operation(s) for metric export.
  name: Cockroach Labs Metric Export API
  slug: cockroach-labs-metric-export-api
- baseURL: https://cockroachlabs.cloud
  baseurl_source: declared
  description: The Migration Assistant API from Cockroach Labs — 2 operation(s) for migration assistant.
  name: Cockroach Labs Migration Assistant API
  slug: cockroach-labs-migration-assistant-api
- baseURL: https://cockroachlabs.cloud
  baseurl_source: declared
  description: The Physical Cluster Replication API from Cockroach Labs — 2 operation(s) for physical cluster replication.
  name: Cockroach Labs Physical Cluster Replication API
  slug: cockroach-labs-physical-cluster-replication-api
- baseURL: https://cockroachlabs.cloud
  baseurl_source: declared
  description: The Private Endpoint Services API from Cockroach Labs — 7 operation(s) for private endpoint services.
  name: Cockroach Labs Private Endpoint Services API
  slug: cockroach-labs-private-endpoint-services-api
- baseURL: https://cockroachlabs.cloud
  baseurl_source: declared
  description: The Runtime Scanning API from Cockroach Labs — 1 operation(s) for runtime scanning.
  name: Cockroach Labs Runtime Scanning API
  slug: cockroach-labs-runtime-scanning-api
- baseURL: https://cockroachlabs.cloud
  baseurl_source: declared
  description: The SCIM API from Cockroach Labs — 13 operation(s) for scim.
  name: Cockroach Labs SCIM API
  slug: cockroach-labs-scim-api
- baseURL: https://cockroachlabs.cloud
  baseurl_source: declared
  description: The SQL Users API from Cockroach Labs — 3 operation(s) for sql users.
  name: Cockroach Labs SQL Users API
  slug: cockroach-labs-sql-users-api
- baseURL: https://cockroachlabs.cloud
  baseurl_source: declared
  description: The Version Deferral API from Cockroach Labs — 1 operation(s) for version deferral.
  name: Cockroach Labs Version Deferral API
  slug: cockroach-labs-version-deferral-api
- baseURL: https://cockroachlabs.cloud
  baseurl_source: declared
  description: The Virtual Cluster Workspaces API from Cockroach Labs — 4 operation(s) for virtual cluster workspaces.
  name: Cockroach Labs Virtual Cluster Workspaces API
  slug: cockroach-labs-virtual-cluster-workspaces-api
- baseURL: https://cockroachlabs.cloud
  baseurl_source: declared
  description: Manage private endpoint services and connections for secure VPC-level access to clusters.
  name: Cockroach Labs Private Endpoints API
  slug: cockroach-labs-private-endpoints-api
- description: Event-driven description of CockroachDB Enterprise CHANGEFEED INTO sinks (Kafka, Google Cloud Pub/Sub, webhook) streaming row-level change data, modeled from the documented envelope shapes and webhook
  name: Cockroach Labs CockroachDB CHANGEFEED Sinks
  slug: cockroach-labs-changefeed-sinks
artifact_total: 209
asyncapis:
- description: AsyncAPI description of CockroachDB CHANGEFEED INTO sinks. CockroachDB Enterprise CHANGEFEEDs stream row-level change data to external systems. This document models the publicly documented sink target
  name: CockroachDB CHANGEFEED Sinks
  slug: cockroach-labs-changefeed-asyncapi
collections:
- collection_type: postman
  name: CockroachDB Cloud APIKeys API
  slug: postman-cockroach-labs-apikeys-api
- collection_type: postman
  name: CockroachDB Cloud APIKeys AuditLogs API
  slug: postman-cockroach-labs-auditlogs-api
- collection_type: postman
  name: CockroachDB Cloud APIKeys Auth API
  slug: postman-cockroach-labs-auth-api
- collection_type: postman
  name: CockroachDB Cloud APIKeys BackupRestore API
  slug: postman-cockroach-labs-backuprestore-api
- collection_type: postman
  name: CockroachDB Cloud APIKeys Billing API
  slug: postman-cockroach-labs-billing-api
- collection_type: postman
  name: CockroachDB Cloud APIKeys Clusters API
  slug: postman-cockroach-labs-clusters-api
- collection_type: postman
  name: CockroachDB Cloud APIKeys CMEK API
  slug: postman-cockroach-labs-cmek-api
- collection_type: postman
  name: CockroachDB Cloud APIKeys Databases API
  slug: postman-cockroach-labs-databases-api
- collection_type: postman
  name: CockroachDB Cloud APIKeys EgressRules API
  slug: postman-cockroach-labs-egressrules-api
- collection_type: postman
  name: CockroachDB Cloud APIKeys Folders API
  slug: postman-cockroach-labs-folders-api
- collection_type: postman
  name: CockroachDB Cloud APIKeys Health API
  slug: postman-cockroach-labs-health-api
- collection_type: postman
  name: CockroachDB Cloud APIKeys IPAllowlists API
  slug: postman-cockroach-labs-ipallowlists-api
- collection_type: postman
  name: CockroachDB Cloud APIKeys JWTIssuers API
  slug: postman-cockroach-labs-jwtissuers-api
- collection_type: postman
  name: CockroachDB Cloud APIKeys LogExport API
  slug: postman-cockroach-labs-logexport-api
- collection_type: postman
  name: CockroachDB Cloud APIKeys MaintenanceWindows API
  slug: postman-cockroach-labs-maintenancewindows-api
- collection_type: postman
  name: CockroachDB Cloud APIKeys MetricExport API
  slug: postman-cockroach-labs-metricexport-api
- collection_type: postman
  name: CockroachDB Cloud APIKeys Nodes API
  slug: postman-cockroach-labs-nodes-api
- collection_type: postman
  name: CockroachDB Cloud APIKeys Organizations API
  slug: postman-cockroach-labs-organizations-api
- collection_type: postman
  name: CockroachDB Cloud APIKeys PrivateEndpoints API
  slug: postman-cockroach-labs-privateendpoints-api
- collection_type: postman
  name: CockroachDB Cloud APIKeys Ranges API
  slug: postman-cockroach-labs-ranges-api
- collection_type: postman
  name: CockroachDB Cloud APIKeys RoleManagement API
  slug: postman-cockroach-labs-rolemanagement-api
- collection_type: postman
  name: CockroachDB Cloud APIKeys Rules API
  slug: postman-cockroach-labs-rules-api
- collection_type: postman
  name: CockroachDB Cloud APIKeys ServiceAccounts API
  slug: postman-cockroach-labs-serviceaccounts-api
- collection_type: postman
  name: CockroachDB Cloud APIKeys Sessions API
  slug: postman-cockroach-labs-sessions-api
- collection_type: postman
  name: CockroachDB Cloud APIKeys SQLUsers API
  slug: postman-cockroach-labs-sqlusers-api
- collection_type: postman
  name: CockroachDB Cloud APIKeys VersionDeferral API
  slug: postman-cockroach-labs-versiondeferral-api
- collection_type: open
  name: CockroachDB Cloud APIKeys API
  slug: open-cockroach-labs-apikeys-api
- collection_type: open
  name: CockroachDB Cloud APIKeys AuditLogs API
  slug: open-cockroach-labs-auditlogs-api
- collection_type: open
  name: CockroachDB Cloud APIKeys Auth API
  slug: open-cockroach-labs-auth-api
- collection_type: open
  name: CockroachDB Cloud APIKeys BackupRestore API
  slug: open-cockroach-labs-backuprestore-api
- collection_type: open
  name: CockroachDB Cloud APIKeys Billing API
  slug: open-cockroach-labs-billing-api
- collection_type: open
  name: CockroachDB Cloud API
  slug: open-cockroach-labs-cloud-api
- collection_type: open
  name: CockroachDB Cluster API
  slug: open-cockroach-labs-cluster-api
- collection_type: open
  name: CockroachDB Cloud APIKeys Clusters API
  slug: open-cockroach-labs-clusters-api
- collection_type: open
  name: CockroachDB Cloud APIKeys CMEK API
  slug: open-cockroach-labs-cmek-api
- collection_type: open
  name: CockroachDB Cloud APIKeys Databases API
  slug: open-cockroach-labs-databases-api
- collection_type: open
  name: CockroachDB Cloud APIKeys EgressRules API
  slug: open-cockroach-labs-egressrules-api
- collection_type: open
  name: CockroachDB Cloud APIKeys Folders API
  slug: open-cockroach-labs-folders-api
- collection_type: open
  name: CockroachDB Cloud APIKeys Health API
  slug: open-cockroach-labs-health-api
- collection_type: open
  name: CockroachDB Cloud APIKeys IPAllowlists API
  slug: open-cockroach-labs-ipallowlists-api
- collection_type: open
  name: CockroachDB Cloud APIKeys JWTIssuers API
  slug: open-cockroach-labs-jwtissuers-api
- collection_type: open
  name: CockroachDB Cloud APIKeys LogExport API
  slug: open-cockroach-labs-logexport-api
- collection_type: open
  name: CockroachDB Cloud APIKeys MaintenanceWindows API
  slug: open-cockroach-labs-maintenancewindows-api
- collection_type: open
  name: CockroachDB Cloud APIKeys MetricExport API
  slug: open-cockroach-labs-metricexport-api
- collection_type: open
  name: CockroachDB Cloud APIKeys Nodes API
  slug: open-cockroach-labs-nodes-api
- collection_type: open
  name: CockroachDB Cloud APIKeys Organizations API
  slug: open-cockroach-labs-organizations-api
- collection_type: open
  name: CockroachDB Cloud APIKeys PrivateEndpoints API
  slug: open-cockroach-labs-privateendpoints-api
- collection_type: open
  name: CockroachDB Cloud APIKeys Ranges API
  slug: open-cockroach-labs-ranges-api
- collection_type: open
  name: CockroachDB Cloud APIKeys RoleManagement API
  slug: open-cockroach-labs-rolemanagement-api
- collection_type: open
  name: CockroachDB Cloud APIKeys Rules API
  slug: open-cockroach-labs-rules-api
- collection_type: open
  name: CockroachDB Cloud APIKeys ServiceAccounts API
  slug: open-cockroach-labs-serviceaccounts-api
- collection_type: open
  name: CockroachDB Cloud APIKeys Sessions API
  slug: open-cockroach-labs-sessions-api
- collection_type: open
  name: CockroachDB Cloud APIKeys SQLUsers API
  slug: open-cockroach-labs-sqlusers-api
- collection_type: open
  name: CockroachDB Cloud APIKeys VersionDeferral API
  slug: open-cockroach-labs-versiondeferral-api
common:
- group: auth
  href: https://artifacts.apis.io/cockroach-labs/well-known/cockroach-labs-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/cockroach-labs-status-security.txt
- group: other
  href: https://artifacts.apis.io/cockroach-labs/capabilities/cockroach-labs-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/cockroach-labs-capability-edges.yml
- group: build
  href: https://artifacts.apis.io/cockroach-labs/integrations/cockroach-labs-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/cockroach-labs-integration-edges.yml
- group: commercial
  href: https://artifacts.apis.io/cockroach-labs/finops/cockroach-labs-finops.yml
  title: ''
  type: FinOps
  url: finops/cockroach-labs-finops.yml
- group: operate
  href: https://artifacts.apis.io/cockroach-labs/rate-limits/cockroach-labs-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/cockroach-labs-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/cockroach-labs/plans/cockroach-labs-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/cockroach-labs-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/cockroach-labs/rules/cockroach-labs-jsonschema-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/cockroach-labs-jsonschema-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/cockroach-labs/vocabulary/cockroach-labs-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/cockroach-labs-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/cockroach-labs/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/cockroach-labs/data-model/cockroach-labs-data-model.yml
  title: ''
  type: DataModel
  url: data-model/cockroach-labs-data-model.yml
- group: build
  href: https://artifacts.apis.io/cockroach-labs/cli/cockroach-labs-cli.yml
  title: ''
  type: CLI
  url: cli/cockroach-labs-cli.yml
- group: design
  href: https://artifacts.apis.io/cockroach-labs/conventions/cockroach-labs-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/cockroach-labs-conventions.yml
- group: design
  href: https://artifacts.apis.io/cockroach-labs/conventions/cockroach-labs-conventions.yml
  title: ''
  type: Conventions
  url: conventions/cockroach-labs-conventions.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.cockroachlabs.com/security/
- group: design
  href: https://artifacts.apis.io/cockroach-labs/errors/cockroach-labs-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/cockroach-labs-problem-types.yml
- group: design
  href: https://artifacts.apis.io/cockroach-labs/conformance/cockroach-labs-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cockroach-labs-conformance.yml
- group: agent
  href: https://artifacts.apis.io/cockroach-labs/llms/cockroach-labs-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cockroach-labs-llms.txt
- group: other
  href: https://artifacts.apis.io/cockroach-labs/a2a/cockroach-labs-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/cockroach-labs-a2a.yml
- group: build
  href: https://artifacts.apis.io/cockroach-labs/mcp/cockroach-labs-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/cockroach-labs-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/cockroach-labs/mcp/cockroach-labs-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/cockroach-labs-mcp.yml
- group: agent
  href: https://artifacts.apis.io/cockroach-labs/well-known/cockroach-labs-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cockroach-labs-well-known.yml
- group: other
  href: https://artifacts.apis.io/cockroach-labs/hosts/cockroach-labs-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cockroach-labs-hosts.yml
- group: other
  href: https://artifacts.apis.io/cockroach-labs/vendors/cockroach-labs-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cockroach-labs-vendors.yml
- group: start
  title: ''
  type: SignUp
  url: https://www.cockroachlabs.com/partners/signup/
- group: company
  title: ''
  type: Newsroom
  url: https://www.cockroachlabs.com/press
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.cockroachlabs.com/developers
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.cockroachlabs.com/docs/releases
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.cockroachlabs.com/docs/continuum/tutorial-quickstart
- group: docs
  title: ''
  type: APIReference
  url: https://docs.cockroachlabs.com/
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/cockroach-labs/overview
- group: agent
  href: https://artifacts.apis.io/cockroach-labs/agentic-access/cockroach-labs-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/cockroach-labs-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/cockroach-labs/security/cockroach-labs-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/cockroach-labs-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/cockroach-labs/security/cockroach-labs-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/cockroach-labs-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/cockroach-labs/security/cockroach-labs-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cockroach-labs-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/cockroach-labs/authentication/cockroach-labs-authentication.yml
  title: ''
  type: Authentication
  url: authentication/cockroach-labs-authentication.yml
- group: agent
  title: ''
  type: AgentSkills
  url: https://github.com/cockroachlabs/cockroachdb-skills
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cockroach-labs
- group: company
  title: ''
  type: Website
  url: https://www.cockroachlabs.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.cockroachlabs.com/docs/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.cockroachlabs.com/pricing/
- group: company
  title: ''
  type: Blog
  url: https://www.cockroachlabs.com/blog/
- group: other
  title: ''
  type: Glossary
  url: https://www.cockroachlabs.com/docs/stable/architecture/glossary
- group: start
  title: ''
  type: Console
  url: https://cockroachlabs.cloud/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cockroachlabs.cloud/
- group: operate
  title: ''
  type: Support
  url: https://www.cockroachlabs.com/support/
- group: company
  title: ''
  type: Partners
  url: https://www.cockroachlabs.com/partners/
- group: auth
  title: ''
  type: Security
  url: https://www.cockroachlabs.com/security/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/cockroachdb
- group: other
  title: ''
  type: TerraformProvider
  url: https://registry.terraform.io/providers/cockroachdb/cockroach/latest
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cockroachlabs.com/privacy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cockroachlabs.com/cloud-terms-and-conditions/
- group: design
  href: https://artifacts.apis.io/cockroach-labs/json-ld/cockroach-labs-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/cockroach-labs-context.jsonld
- group: docs
  href: https://artifacts.apis.io/cockroach-labs/json-schema/cockroach-labs-cluster-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/cockroach-labs-cluster-schema.json
- group: design
  href: https://artifacts.apis.io/cockroach-labs/rules/cockroach-labs-rules.yml
  title: ''
  type: Spectral
  url: rules/cockroach-labs-rules.yml
created: '2024-11-24'
description: 'Cockroach Labs is the New York-based software company that builds CockroachDB, a cloud-native, distributed, PostgreSQL-compatible SQL database. CockroachDB is offered as Cockroach Labs'' fully managed cloud service (Basic, Standard, and Advanced plans) and as self-hosted software. The company provides two primary developer APIs: the CockroachDB Cloud API for managing the lifecycle of cloud-hosted clusters, and the CockroachDB Cluster API exposed by every node for cluster health, monitoring, and operational status. CockroachDB is used in production by banking, retail, gaming, and media companies including Bose, Hard Rock Digital, DoorDash, and Netflix.'
finops:
- has_sources: true
  method: derived
  name: Cockroach Labs Finops
  primary_unit: vcpu-hour
  service_category: ''
  slug: cockroach-labs-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cockroach-labs.png
json_schemas:
- name: AddEgressRuleRequest
  property_count: 4
  slug: cockroach-labs-add-egress-rule-request
- name: AddJWTIssuerRequest
  property_count: 2
  slug: cockroach-labs-add-jwtissuer-request
- name: AddPrivateEndpointConnectionRequest
  property_count: 1
  slug: cockroach-labs-add-private-endpoint-connection-request
- name: AllowlistEntry
  property_count: 5
  slug: cockroach-labs-allowlist-entry
- name: ApiKey
  property_count: 4
  slug: cockroach-labs-api-key
- name: BackupConfiguration
  property_count: 3
  slug: cockroach-labs-backup-configuration
- name: CloudWatchMetricExportInfo
  property_count: 3
  slug: cockroach-labs-cloud-watch-metric-export-info
- name: CockroachDB Cluster
  property_count: 24
  slug: cockroach-labs-cluster
- name: ClusterVersionDeferral
  property_count: 1
  slug: cockroach-labs-cluster-version-deferral
- name: CMEKClusterInfo
  property_count: 3
  slug: cockroach-labs-cmekcluster-info
- name: CMEKClusterSpecification
  property_count: 1
  slug: cockroach-labs-cmekcluster-specification
- name: CreateApiKeyRequest
  property_count: 2
  slug: cockroach-labs-create-api-key-request
- name: CreateApiKeyResponse
  property_count: 2
  slug: cockroach-labs-create-api-key-response
- name: CreateClusterRequest
  property_count: 5
  slug: cockroach-labs-create-cluster-request
- name: CreateDatabaseRequest
  property_count: 1
  slug: cockroach-labs-create-database-request
- name: CreateFolderRequest
  property_count: 2
  slug: cockroach-labs-create-folder-request
- name: CreateServiceAccountRequest
  property_count: 2
  slug: cockroach-labs-create-service-account-request
- name: CreateSQLUserRequest
  property_count: 2
  slug: cockroach-labs-create-sqluser-request
- name: Database
  property_count: 2
  slug: cockroach-labs-database
- name: DatadogMetricExportInfo
  property_count: 3
  slug: cockroach-labs-datadog-metric-export-info
- name: EditEgressRuleRequest
  property_count: 3
  slug: cockroach-labs-edit-egress-rule-request
- name: EgressRule
  property_count: 5
  slug: cockroach-labs-egress-rule
- name: EnableCloudWatchMetricExportRequest
  property_count: 2
  slug: cockroach-labs-enable-cloud-watch-metric-export-request
- name: EnableDatadogMetricExportRequest
  property_count: 2
  slug: cockroach-labs-enable-datadog-metric-export-request
- name: EnableLogExportRequest
  property_count: 3
  slug: cockroach-labs-enable-log-export-request
- name: Folder
  property_count: 4
  slug: cockroach-labs-folder
- name: GetAllRolesForUserResponse
  property_count: 1
  slug: cockroach-labs-get-all-roles-for-user-response
- name: GetPersonUsersByEmailResponse
  property_count: 1
  slug: cockroach-labs-get-person-users-by-email-response
- name: HealthResponse
  property_count: 2
  slug: cockroach-labs-health-response
- name: Invoice
  property_count: 5
  slug: cockroach-labs-invoice
- name: JWTIssuer
  property_count: 3
  slug: cockroach-labs-jwtissuer
- name: ListAllowlistEntriesResponse
  property_count: 2
  slug: cockroach-labs-list-allowlist-entries-response
- name: ListApiKeysResponse
  property_count: 2
  slug: cockroach-labs-list-api-keys-response
- name: ListAuditLogsResponse
  property_count: 1
  slug: cockroach-labs-list-audit-logs-response
- name: ListAvailableRegionsResponse
  property_count: 2
  slug: cockroach-labs-list-available-regions-response
- name: ListClustersResponse
  property_count: 2
  slug: cockroach-labs-list-clusters-response
- name: ListDatabasesResponse
  property_count: 2
  slug: cockroach-labs-list-databases-response
- name: ListEgressRulesResponse
  property_count: 2
  slug: cockroach-labs-list-egress-rules-response
- name: ListFolderContentsResponse
  property_count: 1
  slug: cockroach-labs-list-folder-contents-response
- name: ListFoldersResponse
  property_count: 2
  slug: cockroach-labs-list-folders-response
- name: ListHotRangesResponse
  property_count: 2
  slug: cockroach-labs-list-hot-ranges-response
- name: ListInvoicesResponse
  property_count: 1
  slug: cockroach-labs-list-invoices-response
- name: ListJWTIssuersResponse
  property_count: 2
  slug: cockroach-labs-list-jwtissuers-response
- name: ListMajorClusterVersionsResponse
  property_count: 1
  slug: cockroach-labs-list-major-cluster-versions-response
- name: ListNodeRangesResponse
  property_count: 2
  slug: cockroach-labs-list-node-ranges-response
- name: ListNodesResponse
  property_count: 2
  slug: cockroach-labs-list-nodes-response
- name: ListPrivateEndpointConnectionsResponse
  property_count: 1
  slug: cockroach-labs-list-private-endpoint-connections-response
- name: ListPrivateEndpointServicesResponse
  property_count: 1
  slug: cockroach-labs-list-private-endpoint-services-response
- name: ListRoleGrantsResponse
  property_count: 2
  slug: cockroach-labs-list-role-grants-response
- name: ListServiceAccountsResponse
  property_count: 2
  slug: cockroach-labs-list-service-accounts-response
- name: ListSessionsResponse
  property_count: 3
  slug: cockroach-labs-list-sessions-response
- name: ListSQLUsersResponse
  property_count: 2
  slug: cockroach-labs-list-sqlusers-response
- name: LogExportClusterInfo
  property_count: 3
  slug: cockroach-labs-log-export-cluster-info
- name: LoginRequest
  property_count: 2
  slug: cockroach-labs-login-request
- name: LoginResponse
  property_count: 1
  slug: cockroach-labs-login-response
- name: LogoutResponse
  property_count: 1
  slug: cockroach-labs-logout-response
- name: MaintenanceWindow
  property_count: 2
  slug: cockroach-labs-maintenance-window
- name: Organization
  property_count: 4
  slug: cockroach-labs-organization
- name: PrivateEndpointConnection
  property_count: 5
  slug: cockroach-labs-private-endpoint-connection
- name: PrometheusMetricExportInfo
  property_count: 2
  slug: cockroach-labs-prometheus-metric-export-info
- name: RangeResponse
  property_count: 2
  slug: cockroach-labs-range-response
- name: Restore
  property_count: 4
  slug: cockroach-labs-restore
- name: ServiceAccount
  property_count: 5
  slug: cockroach-labs-service-account
- name: SetRolesForUserRequest
  property_count: 1
  slug: cockroach-labs-set-roles-for-user-request
- name: SQLUser
  property_count: 1
  slug: cockroach-labs-sqluser
- name: UpdateApiKeySpecification
  property_count: 1
  slug: cockroach-labs-update-api-key-specification
- name: UpdateClusterSpecification
  property_count: 3
  slug: cockroach-labs-update-cluster-specification
- name: UpdateCMEKStatusRequest
  property_count: 1
  slug: cockroach-labs-update-cmekstatus-request
- name: UpdateDatabaseRequest
  property_count: 1
  slug: cockroach-labs-update-database-request
- name: UpdateFolderSpecification
  property_count: 2
  slug: cockroach-labs-update-folder-specification
- name: UpdateJWTIssuerRequest
  property_count: 2
  slug: cockroach-labs-update-jwtissuer-request
- name: UpdateServiceAccountSpecification
  property_count: 2
  slug: cockroach-labs-update-service-account-specification
- name: UpdateSQLUserPasswordRequest
  property_count: 1
  slug: cockroach-labs-update-sqluser-password-request
jsonld:
- class_count: 0
  name: Cockroach Labs Context
  property_count: 14
  slug: cockroach-labs-context
layout: provider
mcp_servers:
- description: Remote MCP server at cockroachlabs.cloud requiring OAuth.
  name: Cockroach Labs MCP Server
  slug: cockroach-labs-mcp-yml
modified: '2026-05-19'
name: Cockroach Labs
nav: Providers
network: true
overview: 'Cockroach Labs publishes 45 API contracts indexed on the [APIs.io](https://apis.io/) network, including Auth API, Billing API, Clusters API, and 42 more. Tagged areas include Cluster Management, Cloud, Database, Distributed SQL, and Infrastructure.


  The Cockroach Labs catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 2 Spectral governance rulesets.


  Cockroach Labs'' developer surface includes CLI, signup flow, changelog, getting-started guide, API reference, authentication, documentation, and 47 more developer resources.'
plans:
- name: Cockroach Labs Plans Pricing
  plan_count: 5
  slug: cockroach-labs-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 5
  name: Cockroach Labs Rate Limits
  slug: cockroach-labs-rate-limits
rules:
- authorship: generated
  effective_rule_count: 6
  extends: []
  name: Cockroach Labs — jsonschema rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: cockroach-labs-jsonschema-spectral-rules
- authorship: unmarked
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: Cockroach Labs API Rules
  rule_count: 10
  severity_counts:
    error: 3
    hint: 0
    info: 3
    warn: 4
  slug: cockroach-labs-rules
score:
  band: exemplar
  composite: 74.3
  coverage:
    artifact_dirs: 35
    catalog_earned: 80.8
    catalog_earned_first_party: 12.0
    catalog_gap: 34.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.5
  facets:
    access_clarity: 93.4
    contract_governance: 22.0
    contract_quality: 76.1
    developer_ergonomics: 56.5
    discoverability: 80.8
    operational_transparency: 47.4
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 77.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 84.1
      total: 44
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 35.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 61.1
screenshot: https://apis.io/screenshots/cockroach-labs/cockroach-labs-2026-06-20T174648.png
security:
- kind: authentication
  name: Cockroach Labs Authentication
  slug: cockroach-labs-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Cockroach Labs Domain Security
  slug: cockroach-labs-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Cockroach Labs Vulnerability Disclosure
  slug: cockroach-labs-vulnerability-disclosure
  summary_line: no policy recorded
- kind: trust-center
  name: Cockroach Labs Trust Center
  slug: cockroach-labs-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, HIPAA, FIPS 140
skill_count: 33
skills:
- name: analyzing-range-distribution
  slug: analyzing-range-distribution
- name: analyzing-schema-change-storage-risk
  slug: analyzing-schema-change-storage-risk
- name: auditing-cloud-cluster-security
  slug: auditing-cloud-cluster-security
- name: auditing-table-statistics
  slug: auditing-table-statistics
- name: benchmarking-transaction-patterns
  slug: benchmarking-transaction-patterns
- name: cockroachdb-sql
  slug: cockroachdb-sql
- name: configuring-audit-logging
  slug: configuring-audit-logging
- name: configuring-ip-allowlists
  slug: configuring-ip-allowlists
- name: configuring-log-export
  slug: configuring-log-export
- name: configuring-private-connectivity
  slug: configuring-private-connectivity
- name: configuring-sso-and-scim
  slug: configuring-sso-and-scim
- name: designing-application-transactions
  slug: designing-application-transactions
- name: designing-multi-region-applications
  slug: designing-multi-region-applications
- name: enabling-cmek-encryption
  slug: enabling-cmek-encryption
- name: enforcing-password-policies
  slug: enforcing-password-policies
- name: hardening-user-privileges
  slug: hardening-user-privileges
- name: managing-certificates-and-encryption
  slug: managing-certificates-and-encryption
- name: managing-cluster-capacity
  slug: managing-cluster-capacity
- name: managing-cluster-settings
  slug: managing-cluster-settings
- name: managing-tls-certificates
  slug: managing-tls-certificates
- name: molt-fetch
  slug: molt-fetch
- name: molt-replicator
  slug: molt-replicator
- name: molt-verify
  slug: molt-verify
- name: monitoring-background-jobs
  slug: monitoring-background-jobs
slug: cockroach-labs
tags:
- Cluster Management
- Cloud
- Database
- Distributed SQL
- Infrastructure
- PostgreSQL Compatible
- SQL
website: https://www.cockroachlabs.com/
---
