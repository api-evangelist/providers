---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.6
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 51
  human_in_the_loop: 5
  name: Cockroachdb Agentic Access
  operation_count: 98
  slug: cockroachdb-agentic-access
  summary_line: 98 operations · 51 acting · 5 human-in-the-loop
api_count: 2
apis:
- baseURL: https://cockroachlabs.cloud
  baseurl_source: declared
  description: Manage API keys for programmatic access, including creation, retrieval, listing, updating, and deletion.
  name: CockroachDB APIKeys API
  slug: cockroachdb-apikeys-api
- baseURL: https://cockroachlabs.cloud
  baseurl_source: declared
  description: Retrieve audit log events for the organization to support compliance and security investigations.
  name: CockroachDB AuditLogs API
  slug: cockroachdb-auditlogs-api
- baseURL: https://cockroachlabs.cloud
  baseurl_source: declared
  description: Authenticate to the Cluster API by creating and terminating API sessions. Session tokens are passed via the X-Cockroach-API-Session header on subsequent requests.
  name: CockroachDB Auth API
  slug: cockroachdb-auth-api
- baseURL: https://cockroachlabs.cloud
  baseurl_source: declared
  description: Manage cluster backups, backup configurations, and restore operations for CockroachDB clusters.
  name: CockroachDB BackupRestore API
  slug: cockroachdb-backuprestore-api
- baseURL: https://cockroachlabs.cloud
  baseurl_source: declared
  description: Retrieve invoices and billing information for the CockroachDB Cloud organization.
  name: CockroachDB Billing API
  slug: cockroachdb-billing-api
- baseURL: https://cockroachlabs.cloud
  baseurl_source: declared
  description: Create, list, retrieve, update, and delete CockroachDB Serverless and Dedicated clusters within an organization.
  name: CockroachDB Clusters API
  slug: cockroachdb-clusters-api
- baseURL: https://cockroachlabs.cloud
  baseurl_source: declared
  description: Manage customer-managed encryption keys (CMEK) for encrypting cluster data at rest using customer-controlled keys.
  name: CockroachDB CMEK API
  slug: cockroachdb-cmek-api
- baseURL: https://cockroachlabs.cloud
  baseurl_source: declared
  description: Manage databases within a CockroachDB cluster, including creation, listing, updating, and deletion.
  name: CockroachDB Databases API
  slug: cockroachdb-databases-api
- baseURL: https://cockroachlabs.cloud
  baseurl_source: declared
  description: Configure egress traffic rules and egress private endpoints for outbound cluster network traffic.
  name: CockroachDB EgressRules API
  slug: cockroachdb-egressrules-api
- baseURL: https://cockroachlabs.cloud
  baseurl_source: declared
  description: Organize clusters and other resources into hierarchical folder structures within the organization.
  name: CockroachDB Folders API
  slug: cockroachdb-folders-api
- baseURL: https://cockroachlabs.cloud
  baseurl_source: declared
  description: Check the health and readiness of individual CockroachDB nodes. The health endpoint can report whether the node is live and fully operational for accepting SQL connections.
  name: CockroachDB Health API
  slug: cockroachdb-health-api
- baseURL: https://cockroachlabs.cloud
  baseurl_source: declared
  description: Configure IP allowlist entries to control network access to a cluster.
  name: CockroachDB IPAllowlists API
  slug: cockroachdb-ipallowlists-api
- baseURL: https://cockroachlabs.cloud
  baseurl_source: declared
  description: Manage JWT issuer configurations for external identity provider integrations.
  name: CockroachDB JWTIssuers API
  slug: cockroachdb-jwtissuers-api
- baseURL: https://cockroachlabs.cloud
  baseurl_source: declared
  description: Configure log export to external destinations such as AWS CloudWatch or GCP Cloud Logging.
  name: CockroachDB LogExport API
  slug: cockroachdb-logexport-api
- baseURL: https://cockroachlabs.cloud
  baseurl_source: declared
  description: Configure maintenance windows and blackout periods for cluster upgrade scheduling.
  name: CockroachDB MaintenanceWindows API
  slug: cockroachdb-maintenancewindows-api
- baseURL: https://cockroachlabs.cloud
  baseurl_source: declared
  description: Configure metric export integrations including AWS CloudWatch, Datadog, and Prometheus.
  name: CockroachDB MetricExport API
  slug: cockroachdb-metricexport-api
- baseURL: https://cockroachlabs.cloud
  baseurl_source: declared
  description: Retrieve information about all nodes in the cluster, including their status, address, locality, and operational metrics.
  name: CockroachDB Nodes API
  slug: cockroachdb-nodes-api
- baseURL: https://cockroachlabs.cloud
  baseurl_source: declared
  description: Retrieve information about the caller's CockroachDB Cloud organization.
  name: CockroachDB Organizations API
  slug: cockroachdb-organizations-api
- baseURL: https://cockroachlabs.cloud
  baseurl_source: declared
  description: Manage private endpoint services and connections for secure VPC-level access to clusters.
  name: CockroachDB PrivateEndpoints API
  slug: cockroachdb-privateendpoints-api
- baseURL: https://cockroachlabs.cloud
  baseurl_source: declared
  description: List and inspect range information for the cluster, including hot ranges by node and detailed information for specific range IDs.
  name: CockroachDB Ranges API
  slug: cockroachdb-ranges-api
- baseURL: https://cockroachlabs.cloud
  baseurl_source: declared
  description: Manage role-based access control, including assigning and removing roles for users across organization, folder, and cluster scopes.
  name: CockroachDB RoleManagement API
  slug: cockroachdb-rolemanagement-api
- baseURL: https://cockroachlabs.cloud
  baseurl_source: declared
  description: Retrieve alerting rules templates for use with Prometheus-compatible alerting systems.
  name: CockroachDB Rules API
  slug: cockroachdb-rules-api
- baseURL: https://cockroachlabs.cloud
  baseurl_source: declared
  description: Manage service accounts used for machine-to-machine authentication within the organization.
  name: CockroachDB ServiceAccounts API
  slug: cockroachdb-serviceaccounts-api
- baseURL: https://cockroachlabs.cloud
  baseurl_source: declared
  description: List active SQL sessions across all nodes of the cluster, with optional filtering by username.
  name: CockroachDB Sessions API
  slug: cockroachdb-sessions-api
- baseURL: https://cockroachlabs.cloud
  baseurl_source: declared
  description: Manage SQL users for a cluster, including creating users, listing users, and updating SQL user passwords.
  name: CockroachDB SQLUsers API
  slug: cockroachdb-sqlusers-api
- baseURL: https://cockroachlabs.cloud
  baseurl_source: declared
  description: Manage cluster version deferral policies to delay automatic CockroachDB version upgrades.
  name: CockroachDB VersionDeferral API
  slug: cockroachdb-versiondeferral-api
artifact_total: 207
asyncapis:
- description: AsyncAPI description of CockroachDB CHANGEFEED INTO sinks. CockroachDB Enterprise CHANGEFEEDs stream row-level change data to external systems. This document models the publicly documented sink target
  name: CockroachDB CHANGEFEED Sinks
  slug: cockroachdb-changefeed-asyncapi
collections:
- collection_type: postman
  name: CockroachDB Cloud APIKeys API
  slug: postman-cockroachdb-apikeys-api
- collection_type: postman
  name: CockroachDB Cloud APIKeys AuditLogs API
  slug: postman-cockroachdb-auditlogs-api
- collection_type: postman
  name: CockroachDB Cloud APIKeys Auth API
  slug: postman-cockroachdb-auth-api
- collection_type: postman
  name: CockroachDB Cloud APIKeys BackupRestore API
  slug: postman-cockroachdb-backuprestore-api
- collection_type: postman
  name: CockroachDB Cloud APIKeys Billing API
  slug: postman-cockroachdb-billing-api
- collection_type: postman
  name: CockroachDB Cloud APIKeys Clusters API
  slug: postman-cockroachdb-clusters-api
- collection_type: postman
  name: CockroachDB Cloud APIKeys CMEK API
  slug: postman-cockroachdb-cmek-api
- collection_type: postman
  name: CockroachDB Cloud APIKeys Databases API
  slug: postman-cockroachdb-databases-api
- collection_type: postman
  name: CockroachDB Cloud APIKeys EgressRules API
  slug: postman-cockroachdb-egressrules-api
- collection_type: postman
  name: CockroachDB Cloud APIKeys Folders API
  slug: postman-cockroachdb-folders-api
- collection_type: postman
  name: CockroachDB Cloud APIKeys Health API
  slug: postman-cockroachdb-health-api
- collection_type: postman
  name: CockroachDB Cloud APIKeys IPAllowlists API
  slug: postman-cockroachdb-ipallowlists-api
- collection_type: postman
  name: CockroachDB Cloud APIKeys JWTIssuers API
  slug: postman-cockroachdb-jwtissuers-api
- collection_type: postman
  name: CockroachDB Cloud APIKeys LogExport API
  slug: postman-cockroachdb-logexport-api
- collection_type: postman
  name: CockroachDB Cloud APIKeys MaintenanceWindows API
  slug: postman-cockroachdb-maintenancewindows-api
- collection_type: postman
  name: CockroachDB Cloud APIKeys MetricExport API
  slug: postman-cockroachdb-metricexport-api
- collection_type: postman
  name: CockroachDB Cloud APIKeys Nodes API
  slug: postman-cockroachdb-nodes-api
- collection_type: postman
  name: CockroachDB Cloud APIKeys Organizations API
  slug: postman-cockroachdb-organizations-api
- collection_type: postman
  name: CockroachDB Cloud APIKeys PrivateEndpoints API
  slug: postman-cockroachdb-privateendpoints-api
- collection_type: postman
  name: CockroachDB Cloud APIKeys Ranges API
  slug: postman-cockroachdb-ranges-api
- collection_type: postman
  name: CockroachDB Cloud APIKeys RoleManagement API
  slug: postman-cockroachdb-rolemanagement-api
- collection_type: postman
  name: CockroachDB Cloud APIKeys Rules API
  slug: postman-cockroachdb-rules-api
- collection_type: postman
  name: CockroachDB Cloud APIKeys ServiceAccounts API
  slug: postman-cockroachdb-serviceaccounts-api
- collection_type: postman
  name: CockroachDB Cloud APIKeys Sessions API
  slug: postman-cockroachdb-sessions-api
- collection_type: postman
  name: CockroachDB Cloud APIKeys SQLUsers API
  slug: postman-cockroachdb-sqlusers-api
- collection_type: postman
  name: CockroachDB Cloud APIKeys VersionDeferral API
  slug: postman-cockroachdb-versiondeferral-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: CockroachDB Cloud APIKeys API
  slug: open-cockroachdb-apikeys-api
- collection_type: open
  name: CockroachDB Cloud APIKeys AuditLogs API
  slug: open-cockroachdb-auditlogs-api
- collection_type: open
  name: CockroachDB Cloud APIKeys Auth API
  slug: open-cockroachdb-auth-api
- collection_type: open
  name: CockroachDB Cloud APIKeys BackupRestore API
  slug: open-cockroachdb-backuprestore-api
- collection_type: open
  name: CockroachDB Cloud APIKeys Billing API
  slug: open-cockroachdb-billing-api
- collection_type: open
  name: CockroachDB Cloud API
  slug: open-cockroachdb-cloud-api
- collection_type: open
  name: CockroachDB Cluster API
  slug: open-cockroachdb-cluster-api
- collection_type: open
  name: CockroachDB Cloud APIKeys Clusters API
  slug: open-cockroachdb-clusters-api
- collection_type: open
  name: CockroachDB Cloud APIKeys CMEK API
  slug: open-cockroachdb-cmek-api
- collection_type: open
  name: CockroachDB Cloud APIKeys Databases API
  slug: open-cockroachdb-databases-api
- collection_type: open
  name: CockroachDB Cloud APIKeys EgressRules API
  slug: open-cockroachdb-egressrules-api
- collection_type: open
  name: CockroachDB Cloud APIKeys Folders API
  slug: open-cockroachdb-folders-api
- collection_type: open
  name: CockroachDB Cloud APIKeys Health API
  slug: open-cockroachdb-health-api
- collection_type: open
  name: CockroachDB Cloud APIKeys IPAllowlists API
  slug: open-cockroachdb-ipallowlists-api
- collection_type: open
  name: CockroachDB Cloud APIKeys JWTIssuers API
  slug: open-cockroachdb-jwtissuers-api
- collection_type: open
  name: CockroachDB Cloud APIKeys LogExport API
  slug: open-cockroachdb-logexport-api
- collection_type: open
  name: CockroachDB Cloud APIKeys MaintenanceWindows API
  slug: open-cockroachdb-maintenancewindows-api
- collection_type: open
  name: CockroachDB Cloud APIKeys MetricExport API
  slug: open-cockroachdb-metricexport-api
- collection_type: open
  name: CockroachDB Cloud APIKeys Nodes API
  slug: open-cockroachdb-nodes-api
- collection_type: open
  name: CockroachDB Cloud APIKeys Organizations API
  slug: open-cockroachdb-organizations-api
- collection_type: open
  name: CockroachDB Cloud APIKeys PrivateEndpoints API
  slug: open-cockroachdb-privateendpoints-api
- collection_type: open
  name: CockroachDB Cloud APIKeys Ranges API
  slug: open-cockroachdb-ranges-api
- collection_type: open
  name: CockroachDB Cloud APIKeys RoleManagement API
  slug: open-cockroachdb-rolemanagement-api
- collection_type: open
  name: CockroachDB Cloud APIKeys Rules API
  slug: open-cockroachdb-rules-api
- collection_type: open
  name: CockroachDB Cloud APIKeys ServiceAccounts API
  slug: open-cockroachdb-serviceaccounts-api
- collection_type: open
  name: CockroachDB Cloud APIKeys Sessions API
  slug: open-cockroachdb-sessions-api
- collection_type: open
  name: CockroachDB Cloud APIKeys SQLUsers API
  slug: open-cockroachdb-sqlusers-api
- collection_type: open
  name: CockroachDB Cloud APIKeys VersionDeferral API
  slug: open-cockroachdb-versiondeferral-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/cockroachdb-capability-edges.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/cockroachdb/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cockroachdb-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/cockroachdb-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/cockroachdb-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cockroachdb-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cockroachdb-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cockroach-labs
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/cockroachdb-cluster-schema.json
- group: design
  title: ''
  type: JSONLD
  url: json-ld/cockroachdb-context.jsonld
- group: design
  title: ''
  type: Spectral
  url: rules/cockroachdb-rules.yml
- group: company
  title: ''
  type: Website
  url: https://www.cockroachlabs.com/product/
- group: docs
  title: ''
  type: Documentation
  url: https://www.cockroachlabs.com/docs/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.cockroachlabs.com/pricing/
- group: start
  title: ''
  type: Console
  url: https://cockroachlabs.cloud/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/cockroachdb/cockroach
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cockroachlabs.cloud/
- group: company
  title: ''
  type: Blog
  url: https://cockroachlabs.com/rss.xml
created: '2024-11-24'
description: CockroachDB is a distributed SQL database with strong consistency, PostgreSQL compatibility, and a managed cloud offering. The Cloud API manages cluster lifecycle; the Cluster API exposes per-node operational state for monitoring and troubleshooting.
features:
- 'Basic free: 50M RUs + 10 GiB storage/mo, scales to zero'
- 'Standard from $0.18/hr (2 vCPUs): provisioned compute up to 200 vCPUs'
- 'Advanced from $0.60/hr (4 vCPUs): unlimited scale, CMEK, PCI/HIPAA'
- Multi-region across AWS/GCP/Azure
- Postgres wire-compatible SQL
- Strongly consistent multi-region writes
- Cloud API at 60 req/min/user
- Datadog metrics export (Standard+)
- Private connectivity (Standard+)
- Up to 99.999% availability (Advanced)
- Customer-managed encryption keys (CMEK) on Advanced
- Backup and PITR included
- Distributed SQL with horizontal scale
- JSONB and full-text search
- Geo-partitioned tables
- ACID transactions across regions
finops:
- name: Cockroachdb Finops
  service_category: Distributed SQL Database
  slug: cockroachdb-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cockroachdb.png
json_schemas:
- name: AddEgressRuleRequest
  property_count: 4
  slug: cockroachdb-addegressrulerequest
- name: AddJWTIssuerRequest
  property_count: 2
  slug: cockroachdb-addjwtissuerrequest
- name: AddPrivateEndpointConnectionRequest
  property_count: 1
  slug: cockroachdb-addprivateendpointconnectionrequest
- name: Address
  property_count: 2
  slug: cockroachdb-address
- name: AllowlistEntry
  property_count: 5
  slug: cockroachdb-allowlistentry
- name: ApiKey
  property_count: 4
  slug: cockroachdb-apikey
- name: AvailableRegion
  property_count: 3
  slug: cockroachdb-availableregion
- name: BackupConfiguration
  property_count: 3
  slug: cockroachdb-backupconfiguration
- name: BuildInfo
  property_count: 9
  slug: cockroachdb-buildinfo
- name: CloudWatchMetricExportInfo
  property_count: 3
  slug: cockroachdb-cloudwatchmetricexportinfo
- name: CockroachDB Cluster
  property_count: 24
  slug: cockroachdb-cluster
- name: ClusterConfig
  property_count: 2
  slug: cockroachdb-clusterconfig
- name: ClusterNode
  property_count: 3
  slug: cockroachdb-clusternode
- name: ClusterVersionDeferral
  property_count: 1
  slug: cockroachdb-clusterversiondeferral
- name: CMEKClusterInfo
  property_count: 3
  slug: cockroachdb-cmekclusterinfo
- name: CMEKClusterSpecification
  property_count: 1
  slug: cockroachdb-cmekclusterspecification
- name: CreateApiKeyRequest
  property_count: 2
  slug: cockroachdb-createapikeyrequest
- name: CreateApiKeyResponse
  property_count: 2
  slug: cockroachdb-createapikeyresponse
- name: CreateClusterRequest
  property_count: 5
  slug: cockroachdb-createclusterrequest
- name: CreateDatabaseRequest
  property_count: 1
  slug: cockroachdb-createdatabaserequest
- name: CreateFolderRequest
  property_count: 2
  slug: cockroachdb-createfolderrequest
- name: CreateRestoreRequest
  property_count: 2
  slug: cockroachdb-createrestorerequest
- name: CreateServiceAccountRequest
  property_count: 2
  slug: cockroachdb-createserviceaccountrequest
- name: CreateSQLUserRequest
  property_count: 2
  slug: cockroachdb-createsqluserrequest
- name: Database
  property_count: 2
  slug: cockroachdb-database
- name: DatadogMetricExportInfo
  property_count: 3
  slug: cockroachdb-datadogmetricexportinfo
- name: DedicatedClusterConfig
  property_count: 5
  slug: cockroachdb-dedicatedclusterconfig
- name: EditEgressRuleRequest
  property_count: 3
  slug: cockroachdb-editegressrulerequest
- name: EgressRule
  property_count: 5
  slug: cockroachdb-egressrule
- name: EnableCloudWatchMetricExportRequest
  property_count: 2
  slug: cockroachdb-enablecloudwatchmetricexportrequest
- name: EnableDatadogMetricExportRequest
  property_count: 2
  slug: cockroachdb-enabledatadogmetricexportrequest
- name: EnableLogExportRequest
  property_count: 3
  slug: cockroachdb-enablelogexportrequest
- name: Error
  property_count: 3
  slug: cockroachdb-error
- name: Folder
  property_count: 4
  slug: cockroachdb-folder
- name: GetAllRolesForUserResponse
  property_count: 1
  slug: cockroachdb-getallrolesforuserresponse
- name: GetConnectionStringResponse
  property_count: 1
  slug: cockroachdb-getconnectionstringresponse
- name: GetPersonUsersByEmailResponse
  property_count: 1
  slug: cockroachdb-getpersonusersbyemailresponse
- name: HealthResponse
  property_count: 2
  slug: cockroachdb-healthresponse
- name: HotRange
  property_count: 7
  slug: cockroachdb-hotrange
- name: Invoice
  property_count: 5
  slug: cockroachdb-invoice
- name: JWTIssuer
  property_count: 3
  slug: cockroachdb-jwtissuer
- name: ListAllowlistEntriesResponse
  property_count: 2
  slug: cockroachdb-listallowlistentriesresponse
- name: ListApiKeysResponse
  property_count: 2
  slug: cockroachdb-listapikeysresponse
- name: ListAuditLogsResponse
  property_count: 1
  slug: cockroachdb-listauditlogsresponse
- name: ListAvailableRegionsResponse
  property_count: 2
  slug: cockroachdb-listavailableregionsresponse
- name: ListBackupsResponse
  property_count: 2
  slug: cockroachdb-listbackupsresponse
- name: ListClusterNodesResponse
  property_count: 2
  slug: cockroachdb-listclusternodesresponse
- name: ListClustersResponse
  property_count: 2
  slug: cockroachdb-listclustersresponse
- name: ListDatabasesResponse
  property_count: 2
  slug: cockroachdb-listdatabasesresponse
- name: ListEgressRulesResponse
  property_count: 2
  slug: cockroachdb-listegressrulesresponse
- name: ListFolderContentsResponse
  property_count: 1
  slug: cockroachdb-listfoldercontentsresponse
- name: ListFoldersResponse
  property_count: 2
  slug: cockroachdb-listfoldersresponse
- name: ListHotRangesResponse
  property_count: 2
  slug: cockroachdb-listhotrangesresponse
- name: ListInvoicesResponse
  property_count: 1
  slug: cockroachdb-listinvoicesresponse
- name: ListJWTIssuersResponse
  property_count: 2
  slug: cockroachdb-listjwtissuersresponse
- name: ListMajorClusterVersionsResponse
  property_count: 1
  slug: cockroachdb-listmajorclusterversionsresponse
- name: ListNodeRangesResponse
  property_count: 2
  slug: cockroachdb-listnoderangesresponse
- name: ListNodesResponse
  property_count: 2
  slug: cockroachdb-listnodesresponse
- name: ListPrivateEndpointConnectionsResponse
  property_count: 1
  slug: cockroachdb-listprivateendpointconnectionsresponse
- name: ListPrivateEndpointServicesResponse
  property_count: 1
  slug: cockroachdb-listprivateendpointservicesresponse
- name: ListRestoresResponse
  property_count: 2
  slug: cockroachdb-listrestoresresponse
- name: ListRoleGrantsResponse
  property_count: 2
  slug: cockroachdb-listrolegrantsresponse
- name: ListServiceAccountsResponse
  property_count: 2
  slug: cockroachdb-listserviceaccountsresponse
- name: ListSessionsResponse
  property_count: 3
  slug: cockroachdb-listsessionsresponse
- name: ListSQLUsersResponse
  property_count: 2
  slug: cockroachdb-listsqlusersresponse
- name: Locality
  property_count: 1
  slug: cockroachdb-locality
- name: LogExportClusterInfo
  property_count: 3
  slug: cockroachdb-logexportclusterinfo
- name: LoginRequest
  property_count: 2
  slug: cockroachdb-loginrequest
- name: LoginResponse
  property_count: 1
  slug: cockroachdb-loginresponse
- name: LogoutResponse
  property_count: 1
  slug: cockroachdb-logoutresponse
- name: MaintenanceWindow
  property_count: 2
  slug: cockroachdb-maintenancewindow
- name: NodeDescriptor
  property_count: 9
  slug: cockroachdb-nodedescriptor
- name: NodeStatus
  property_count: 9
  slug: cockroachdb-nodestatus
- name: Organization
  property_count: 4
  slug: cockroachdb-organization
- name: PaginationResponse
  property_count: 3
  slug: cockroachdb-paginationresponse
- name: PrivateEndpointConnection
  property_count: 5
  slug: cockroachdb-privateendpointconnection
- name: PrometheusMetricExportInfo
  property_count: 2
  slug: cockroachdb-prometheusmetricexportinfo
- name: RangeDescriptor
  property_count: 4
  slug: cockroachdb-rangedescriptor
- name: RangeInfo
  property_count: 8
  slug: cockroachdb-rangeinfo
- name: RangeResponse
  property_count: 2
  slug: cockroachdb-rangeresponse
- name: Region
  property_count: 3
  slug: cockroachdb-region
- name: Restore
  property_count: 4
  slug: cockroachdb-restore
- name: ServerlessClusterConfig
  property_count: 3
  slug: cockroachdb-serverlessclusterconfig
- name: ServiceAccount
  property_count: 5
  slug: cockroachdb-serviceaccount
- name: Session
  property_count: 11
  slug: cockroachdb-session
- name: SetRolesForUserRequest
  property_count: 1
  slug: cockroachdb-setrolesforuserrequest
- name: SQLUser
  property_count: 1
  slug: cockroachdb-sqluser
- name: UpdateApiKeySpecification
  property_count: 1
  slug: cockroachdb-updateapikeyspecification
- name: UpdateBackupConfigurationSpec
  property_count: 2
  slug: cockroachdb-updatebackupconfigurationspec
- name: UpdateClusterSpecification
  property_count: 3
  slug: cockroachdb-updateclusterspecification
- name: UpdateCMEKStatusRequest
  property_count: 1
  slug: cockroachdb-updatecmekstatusrequest
- name: UpdateDatabaseRequest
  property_count: 1
  slug: cockroachdb-updatedatabaserequest
- name: UpdateFolderSpecification
  property_count: 2
  slug: cockroachdb-updatefolderspecification
- name: UpdateJWTIssuerRequest
  property_count: 2
  slug: cockroachdb-updatejwtissuerrequest
- name: UpdateServiceAccountSpecification
  property_count: 2
  slug: cockroachdb-updateserviceaccountspecification
- name: UpdateSQLUserPasswordRequest
  property_count: 1
  slug: cockroachdb-updatesqluserpasswordrequest
json_structures:
- name: Cockroachdb Structure
  property_count: 0
  slug: cockroachdb-structure
jsonld:
- class_count: 0
  name: Cockroachdb Context
  property_count: 14
  slug: cockroachdb-context
layout: provider
modified: '2026-05-19'
name: CockroachDB
nav: Providers
network: true
overview: 'CockroachDB publishes 26 APIs on the [APIs.io](https://apis.io/) network, including APIKeys API, AuditLogs API, Auth API, and 23 more. Tagged areas include Cluster Management, Cloud, Database, Distributed SQL, and Infrastructure.


  The CockroachDB catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 3 Spectral governance rulesets.


  CockroachDB''s developer surface includes authentication, documentation, pricing, developer console, GitHub presence, engineering blog, and 12 more developer resources.'
plans:
- name: Cockroachdb Plans Pricing
  plan_count: 3
  slug: cockroachdb-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 3
  name: Cockroachdb Rate Limits
  slug: cockroachdb-rate-limits
rules:
- effective_rule_count: 33
  extends:
  - spectral:asyncapi
  name: CockroachDB API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 6
  slug: cockroachdb-asyncapi-spectral-rules
- effective_rule_count: 6
  extends: []
  name: CockroachDB API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: cockroachdb-jsonschema-spectral-rules
- effective_rule_count: 51
  extends:
  - spectral:oas
  name: CockroachDB API Rules
  rule_count: 10
  severity_counts:
    error: 3
    hint: 0
    info: 3
    warn: 4
  slug: cockroachdb-rules
score:
  band: developing
  composite: 44.4
  coverage:
    artifact_dirs: 19
    catalog_gap: 56.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 13.6
    contract_quality: 72.8
    developer_ergonomics: 35.7
    discoverability: 68.5
    governance: 13.6
    operational_transparency: 28.9
  previous_composite: 44.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 76.9
      derived: 0
      marker_coverage: 0.0
      total: 26
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cockroachdb/refs/heads/main/screenshots/cockroachdb-2026-06-20T174648.png
security:
- kind: authentication
  name: Cockroachdb Authentication
  slug: cockroachdb-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Cockroachdb Domain Security
  slug: cockroachdb-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Cockroachdb Vulnerability Disclosure
  slug: cockroachdb-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Cockroachdb Trust Center
  slug: cockroachdb-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, HIPAA, FIPS 140
slug: cockroachdb
tags:
- Cluster Management
- Cloud
- Database
- Distributed SQL
- Infrastructure
- PostgreSQL Compatible
- SQL
website: https://www.cockroachlabs.com/product/
---
