---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
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
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 28.2
  scored_at: '2026-09-24'
agentic_access:
- acting_count: 300
  human_in_the_loop: 14
  name: Yugabyte Agentic Access
  operation_count: 522
  slug: yugabyte-agentic-access
  summary_line: 522 operations · 300 acting · 14 human-in-the-loop
api_count: 1
apis:
- description: Programmatic management API for YugabyteDB Aeon, the fully managed cloud DBaaS. Deploy and manage clusters and read replicas, schedule and run on-demand backups and restores, manage IP allow lists, co
  name: YugabyteDB Aeon REST API
  slug: yugabytedb-aeon-rest-api
- baseURL: https://cloud.yugabyte.com/api/public/v1
  baseurl_source: declared
  description: APIs for getting backup Details
  name: Yugabyte Backup Info API
  slug: yugabyte-backup-info-api
- baseURL: https://cloud.yugabyte.com/api/public/v1
  baseurl_source: declared
  description: APIs for cluster CRUD
  name: Yugabyte Cluster API
  slug: yugabyte-cluster-api
- baseURL: https://cloud.yugabyte.com/api/public/v1
  baseurl_source: declared
  description: APIs for getting information about an existing cluster
  name: Yugabyte Cluster Info API
  slug: yugabyte-cluster-info-api
- baseURL: https://cloud.yugabyte.com/api/public/v1
  baseurl_source: declared
  description: APIs for getting Point-in-Time Recovery (PITR) schedules
  name: Yugabyte Pitr Info API
  slug: yugabyte-pitr-info-api
- baseURL: https://cloud.yugabyte.com/api/public/v1
  baseurl_source: declared
  description: APIs for getting restore Details
  name: Yugabyte Restore Info API
  slug: yugabyte-restore-info-api
- baseURL: https://cloud.yugabyte.com/api/public/v1
  baseurl_source: declared
  description: APIs for getting information about Voyager migrations
  name: Yugabyte Voyager Info API
  slug: yugabyte-voyager-info-api
- baseURL: https://cloud.yugabyte.com/api/public/v1
  baseurl_source: declared
  description: APIs for getting Voyager data migrations metrics
  name: Yugabyte Voyager Metrics API
  slug: yugabyte-voyager-metrics-api
- baseURL: https://cloud.yugabyte.com/api/public/v1
  baseurl_source: declared
  description: The Xcluster Metrics API from Yugabyte — 1 operation(s) for xcluster metrics.
  name: Yugabyte Xcluster Metrics API
  slug: yugabyte-xcluster-metrics-api
- baseURL: https://cloud.yugabyte.com/api/public/v1
  baseurl_source: declared
  description: The Xcluster Namespace Details API from Yugabyte — 1 operation(s) for xcluster namespace details.
  name: Yugabyte Xcluster Namespace Details API
  slug: yugabyte-xcluster-namespace-details-api
- baseURL: https://cloud.yugabyte.com/api/public/v1
  baseurl_source: declared
  description: The Access Keys API from YugabyteDB — 3 operation(s) for access keys.
  name: YugabyteDB Access Keys API
  slug: yugabytedb-access-keys-api
- baseURL: https://cloud.yugabyte.com/api/public/v1
  baseurl_source: declared
  description: Retrieve account-level information for the authenticated user, including account ID and metadata used to scope all other API requests.
  name: YugabyteDB Accounts API
  slug: yugabytedb-accounts-api
- baseURL: https://cloud.yugabyte.com/api/public/v1
  baseurl_source: declared
  description: The Alerts API from YugabyteDB — 24 operation(s) for alerts.
  name: YugabyteDB Alerts API
  slug: yugabytedb-alerts-api
- baseURL: https://cloud.yugabyte.com/api/public/v1
  baseurl_source: declared
  description: The Asynchronous Replication API from YugabyteDB — 6 operation(s) for asynchronous replication.
  name: YugabyteDB Asynchronous Replication API
  slug: yugabytedb-asynchronous-replication-api
- baseURL: https://cloud.yugabyte.com/api/public/v1
  baseurl_source: declared
  description: The Audit API from YugabyteDB — 3 operation(s) for audit.
  name: YugabyteDB Audit API
  slug: yugabytedb-audit-api
- baseURL: https://cloud.yugabyte.com/api/public/v1
  baseurl_source: declared
  description: Authentication operations on YBA
  name: YugabyteDB Authentication API
  slug: yugabytedb-authentication-api
- baseURL: https://cloud.yugabyte.com/api/public/v1
  baseurl_source: declared
  description: The Availability Zones API from YugabyteDB — 4 operation(s) for availability zones.
  name: YugabyteDB Availability Zones API
  slug: yugabytedb-availability-zones-api
- baseURL: https://cloud.yugabyte.com/api/public/v1
  baseurl_source: declared
  description: Operations related to universe backup and restore
  name: YugabyteDB Backup and Restore API
  slug: yugabytedb-backup-and-restore-api
- baseURL: https://cloud.yugabyte.com/api/public/v1
  baseurl_source: declared
  description: Manage backup schedules and trigger on-demand backups for YugabyteDB Aeon clusters. Backups are stored in the same region as the cluster.
  name: YugabyteDB Backups API
  slug: yugabytedb-backups-api
- baseURL: https://cloud.yugabyte.com/api/public/v1
  baseurl_source: declared
  description: The Certificate Info API from YugabyteDB — 7 operation(s) for certificate info.
  name: YugabyteDB Certificate Info API
  slug: yugabytedb-certificate-info-api
- baseURL: https://cloud.yugabyte.com/api/public/v1
  baseurl_source: declared
  description: The Cloud providers API from YugabyteDB — 8 operation(s) for cloud providers.
  name: YugabyteDB Cloud providers API
  slug: yugabytedb-cloud-providers-api
- baseURL: https://cloud.yugabyte.com/api/public/v1
  baseurl_source: declared
  description: Create, list, retrieve, update, pause, resume, and delete YugabyteDB clusters within an account and project. Supports both single-region and multi-region cluster configurations.
  name: YugabyteDB Clusters API
  slug: yugabytedb-clusters-api
- baseURL: https://cloud.yugabyte.com/api/public/v1
  baseurl_source: declared
  description: CRUD operations for Continuous YBA Backups
  name: YugabyteDB Continuous Backup API
  slug: yugabytedb-continuous-backup-api
- baseURL: https://cloud.yugabyte.com/api/public/v1
  baseurl_source: declared
  description: The Custom CA Certificates API from YugabyteDB — 4 operation(s) for custom ca certificates.
  name: YugabyteDB Custom CA Certificates API
  slug: yugabytedb-custom-ca-certificates-api
- baseURL: https://cloud.yugabyte.com/api/public/v1
  baseurl_source: declared
  description: The Customer Configuration API from YugabyteDB — 7 operation(s) for customer configuration.
  name: YugabyteDB Customer Configuration API
  slug: yugabytedb-customer-configuration-api
- baseURL: https://cloud.yugabyte.com/api/public/v1
  baseurl_source: declared
  description: The Customer management API from YugabyteDB — 4 operation(s) for customer management.
  name: YugabyteDB Customer management API
  slug: yugabytedb-customer-management-api
- baseURL: https://cloud.yugabyte.com/api/public/v1
  baseurl_source: declared
  description: The Customer Tasks API from YugabyteDB — 8 operation(s) for customer tasks.
  name: YugabyteDB Customer Tasks API
  slug: yugabytedb-customer-tasks-api
- baseURL: https://cloud.yugabyte.com/api/public/v1
  baseurl_source: declared
  description: The Disaster Recovery API from YugabyteDB — 15 operation(s) for disaster recovery.
  name: YugabyteDB Disaster Recovery API
  slug: yugabytedb-disaster-recovery-api
- baseURL: https://cloud.yugabyte.com/api/public/v1
  baseurl_source: declared
  description: The Encryption at rest API from YugabyteDB — 7 operation(s) for encryption at rest.
  name: YugabyteDB Encryption at rest API
  slug: yugabytedb-encryption-at-rest-api
- baseURL: https://cloud.yugabyte.com/api/public/v1
  baseurl_source: declared
  description: The Extract metadata from remote tarball API from YugabyteDB — 2 operation(s) for extract metadata from remote tarball.
  name: YugabyteDB Extract metadata from remote tarball API
  slug: yugabytedb-extract-metadata-from-remote-tarball-api
- baseURL: https://cloud.yugabyte.com/api/public/v1
  baseurl_source: declared
  description: The GFlags Validation APIs API from YugabyteDB — 3 operation(s) for gflags validation apis.
  name: YugabyteDB GFlags Validation APIs API
  slug: yugabytedb-gflags-validation-apis-api
- baseURL: https://cloud.yugabyte.com/api/public/v1
  baseurl_source: declared
  description: The Grafana Dashboard API from YugabyteDB — 1 operation(s) for grafana dashboard.
  name: YugabyteDB Grafana Dashboard API
  slug: yugabytedb-grafana-dashboard-api
- baseURL: https://cloud.yugabyte.com/api/public/v1
  baseurl_source: declared
  description: The HA API from YugabyteDB — 3 operation(s) for ha.
  name: YugabyteDB HA API
  slug: yugabytedb-ha-api
- baseURL: https://cloud.yugabyte.com/api/public/v1
  baseurl_source: declared
  description: The Instance types API from YugabyteDB — 5 operation(s) for instance types.
  name: YugabyteDB Instance types API
  slug: yugabytedb-instance-types-api
- baseURL: https://cloud.yugabyte.com/api/public/v1
  baseurl_source: declared
  description: The Internal HA API from YugabyteDB — 5 operation(s) for internal ha.
  name: YugabyteDB Internal HA API
  slug: yugabytedb-internal-ha-api
- baseURL: https://cloud.yugabyte.com/api/public/v1
  baseurl_source: declared
  description: Isolated backup/restore of YBA to local filesystem
  name: YugabyteDB Isolated Backup API
  slug: yugabytedb-isolated-backup-api
- baseURL: https://cloud.yugabyte.com/api/public/v1
  baseurl_source: declared
  description: Job Scheduler
  name: YugabyteDB Job Scheduler API
  slug: yugabytedb-job-scheduler-api
- baseURL: https://cloud.yugabyte.com/api/public/v1
  baseurl_source: declared
  description: The KubernetesOverridesController API from YugabyteDB — 1 operation(s) for kubernetesoverridescontroller.
  name: YugabyteDB KubernetesOverridesController API
  slug: yugabytedb-kubernetesoverridescontroller-api
- baseURL: https://cloud.yugabyte.com/api/public/v1
  baseurl_source: declared
  description: The LDAP Role management API from YugabyteDB — 1 operation(s) for ldap role management.
  name: YugabyteDB LDAP Role management API
  slug: yugabytedb-ldap-role-management-api
- baseURL: https://cloud.yugabyte.com/api/public/v1
  baseurl_source: declared
  description: The LDAPOIDC Role management API from YugabyteDB — 3 operation(s) for ldapoidc role management.
  name: YugabyteDB LDAPOIDC Role management API
  slug: yugabytedb-ldapoidc-role-management-api
- baseURL: https://cloud.yugabyte.com/api/public/v1
  baseurl_source: declared
  description: The License management API from YugabyteDB — 2 operation(s) for license management.
  name: YugabyteDB License management API
  slug: yugabytedb-license-management-api
- baseURL: https://cloud.yugabyte.com/api/public/v1
  baseurl_source: declared
  description: The LoggingConfig API from YugabyteDB — 2 operation(s) for loggingconfig.
  name: YugabyteDB LoggingConfig API
  slug: yugabytedb-loggingconfig-api
- baseURL: https://cloud.yugabyte.com/api/public/v1
  baseurl_source: declared
  description: The Maintenance windows API from YugabyteDB — 4 operation(s) for maintenance windows.
  name: YugabyteDB Maintenance windows API
  slug: yugabytedb-maintenance-windows-api
- baseURL: https://cloud.yugabyte.com/api/public/v1
  baseurl_source: declared
  description: The Metrics API from YugabyteDB — 2 operation(s) for metrics.
  name: YugabyteDB Metrics API
  slug: yugabytedb-metrics-api
- baseURL: https://cloud.yugabyte.com/api/public/v1
  baseurl_source: declared
  description: The New Release management API from YugabyteDB — 2 operation(s) for new release management.
  name: YugabyteDB New Release management API
  slug: yugabytedb-new-release-management-api
- baseURL: https://cloud.yugabyte.com/api/public/v1
  baseurl_source: declared
  description: The Node Agents API from YugabyteDB — 5 operation(s) for node agents.
  name: YugabyteDB Node Agents API
  slug: yugabytedb-node-agents-api
- baseURL: https://cloud.yugabyte.com/api/public/v1
  baseurl_source: declared
  description: The Node instances API from YugabyteDB — 10 operation(s) for node instances.
  name: YugabyteDB Node instances API
  slug: yugabytedb-node-instances-api
- baseURL: https://cloud.yugabyte.com/api/public/v1
  baseurl_source: declared
  description: The PA Collector API from YugabyteDB — 4 operation(s) for pa collector.
  name: YugabyteDB PA Collector API
  slug: yugabytedb-pa-collector-api
- baseURL: https://cloud.yugabyte.com/api/public/v1
  baseurl_source: declared
  description: The PackagesController API from YugabyteDB — 1 operation(s) for packagescontroller.
  name: YugabyteDB PackagesController API
  slug: yugabytedb-packagescontroller-api
- baseURL: https://cloud.yugabyte.com/api/public/v1
  baseurl_source: declared
  description: The Performance Advisor API from YugabyteDB — 9 operation(s) for performance advisor.
  name: YugabyteDB Performance Advisor API
  slug: yugabytedb-performance-advisor-api
- baseURL: https://cloud.yugabyte.com/api/public/v1
  baseurl_source: declared
  description: The PITR management API from YugabyteDB — 5 operation(s) for pitr management.
  name: YugabyteDB PITR management API
  slug: yugabytedb-pitr-management-api
- baseURL: https://cloud.yugabyte.com/api/public/v1
  baseurl_source: declared
  description: The Platform Instance API from YugabyteDB — 4 operation(s) for platform instance.
  name: YugabyteDB Platform Instance API
  slug: yugabytedb-platform-instance-api
- baseURL: https://cloud.yugabyte.com/api/public/v1
  baseurl_source: declared
  description: The Platform Replication API from YugabyteDB — 4 operation(s) for platform replication.
  name: YugabyteDB Platform Replication API
  slug: yugabytedb-platform-replication-api
- baseURL: https://cloud.yugabyte.com/api/public/v1
  baseurl_source: declared
  description: The preview API from YugabyteDB — 2 operation(s) for preview.
  name: YugabyteDB preview API
  slug: yugabytedb-preview-api
- baseURL: https://cloud.yugabyte.com/api/public/v1
  baseurl_source: declared
  description: Manage projects within a YugabyteDB Aeon account. Projects provide organizational grouping for clusters, allow lists, and billing.
  name: YugabyteDB Projects API
  slug: yugabytedb-projects-api
- baseURL: https://cloud.yugabyte.com/api/public/v1
  baseurl_source: declared
  description: The RBAC management API from YugabyteDB — 5 operation(s) for rbac management.
  name: YugabyteDB RBAC management API
  slug: yugabytedb-rbac-management-api
- baseURL: https://cloud.yugabyte.com/api/public/v1
  baseurl_source: declared
  description: The Region management API from YugabyteDB — 5 operation(s) for region management.
  name: YugabyteDB Region management API
  slug: yugabytedb-region-management-api
- baseURL: https://cloud.yugabyte.com/api/public/v1
  baseurl_source: declared
  description: The Release management API from YugabyteDB — 3 operation(s) for release management.
  name: YugabyteDB Release management API
  slug: yugabytedb-release-management-api
- baseURL: https://cloud.yugabyte.com/api/public/v1
  baseurl_source: declared
  description: Restore a cluster from a previously created backup snapshot, enabling point-in-time recovery of database state.
  name: YugabyteDB Restores API
  slug: yugabytedb-restores-api
- baseURL: https://cloud.yugabyte.com/api/public/v1
  baseurl_source: declared
  description: The Runtime configuration API from YugabyteDB — 6 operation(s) for runtime configuration.
  name: YugabyteDB Runtime configuration API
  slug: yugabytedb-runtime-configuration-api
- baseURL: https://cloud.yugabyte.com/api/public/v1
  baseurl_source: declared
  description: The Schedule management API from YugabyteDB — 7 operation(s) for schedule management.
  name: YugabyteDB Schedule management API
  slug: yugabytedb-schedule-management-api
- baseURL: https://cloud.yugabyte.com/api/public/v1
  baseurl_source: declared
  description: The Session management API from YugabyteDB — 9 operation(s) for session management.
  name: YugabyteDB Session management API
  slug: yugabytedb-session-management-api
- baseURL: https://cloud.yugabyte.com/api/public/v1
  baseurl_source: declared
  description: The Support Bundle management API from YugabyteDB — 5 operation(s) for support bundle management.
  name: YugabyteDB Support Bundle management API
  slug: yugabytedb-support-bundle-management-api
- baseURL: https://cloud.yugabyte.com/api/public/v1
  baseurl_source: declared
  description: The Table management API from YugabyteDB — 8 operation(s) for table management.
  name: YugabyteDB Table management API
  slug: yugabytedb-table-management-api
- baseURL: https://cloud.yugabyte.com/api/public/v1
  baseurl_source: declared
  description: The Tablet server management API from YugabyteDB — 1 operation(s) for tablet server management.
  name: YugabyteDB Tablet server management API
  slug: yugabytedb-tablet-server-management-api
- baseURL: https://cloud.yugabyte.com/api/public/v1
  baseurl_source: declared
  description: The Telemetry Provider API from YugabyteDB — 3 operation(s) for telemetry provider.
  name: YugabyteDB Telemetry Provider API
  slug: yugabytedb-telemetry-provider-api
- baseURL: https://cloud.yugabyte.com/api/public/v1
  baseurl_source: declared
  description: The Universe actions API from YugabyteDB — 1 operation(s) for universe actions.
  name: YugabyteDB Universe actions API
  slug: yugabytedb-universe-actions-api
- baseURL: https://cloud.yugabyte.com/api/public/v1
  baseurl_source: declared
  description: CRUD operations for a Universe
  name: YugabyteDB Universe API
  slug: yugabytedb-universe-api
- baseURL: https://cloud.yugabyte.com/api/public/v1
  baseurl_source: declared
  description: The Universe CDC Management API from YugabyteDB — 3 operation(s) for universe cdc management.
  name: YugabyteDB Universe CDC Management API
  slug: yugabytedb-universe-cdc-management-api
- baseURL: https://cloud.yugabyte.com/api/public/v1
  baseurl_source: declared
  description: The Universe database management API from YugabyteDB — 6 operation(s) for universe database management.
  name: YugabyteDB Universe database management API
  slug: yugabytedb-universe-database-management-api
- baseURL: https://cloud.yugabyte.com/api/public/v1
  baseurl_source: declared
  description: The Universe information API from YugabyteDB — 11 operation(s) for universe information.
  name: YugabyteDB Universe information API
  slug: yugabytedb-universe-information-api
- baseURL: https://cloud.yugabyte.com/api/public/v1
  baseurl_source: declared
  description: The Universe management API from YugabyteDB — 11 operation(s) for universe management.
  name: YugabyteDB Universe management API
  slug: yugabytedb-universe-management-api
- baseURL: https://cloud.yugabyte.com/api/public/v1
  baseurl_source: declared
  description: The Universe node metadata (metamaster) API from YugabyteDB — 6 operation(s) for universe node metadata (metamaster).
  name: YugabyteDB Universe node metadata (metamaster) API
  slug: yugabytedb-universe-node-metadata-metamaster-api
- baseURL: https://cloud.yugabyte.com/api/public/v1
  baseurl_source: declared
  description: The Universe performance suggestions API from YugabyteDB — 3 operation(s) for universe performance suggestions.
  name: YugabyteDB Universe performance suggestions API
  slug: yugabytedb-universe-performance-suggestions-api
- baseURL: https://cloud.yugabyte.com/api/public/v1
  baseurl_source: declared
  description: The Universe Upgrades Management API from YugabyteDB — 20 operation(s) for universe upgrades management.
  name: YugabyteDB Universe Upgrades Management API
  slug: yugabytedb-universe-upgrades-management-api
- baseURL: https://cloud.yugabyte.com/api/public/v1
  baseurl_source: declared
  description: The UniverseClusterMutations API from YugabyteDB — 4 operation(s) for universeclustermutations.
  name: YugabyteDB UniverseClusterMutations API
  slug: yugabytedb-universeclustermutations-api
- baseURL: https://cloud.yugabyte.com/api/public/v1
  baseurl_source: declared
  description: The Upload Release packages API from YugabyteDB — 2 operation(s) for upload release packages.
  name: YugabyteDB Upload Release packages API
  slug: yugabytedb-upload-release-packages-api
- baseURL: https://cloud.yugabyte.com/api/public/v1
  baseurl_source: declared
  description: The User management API from YugabyteDB — 6 operation(s) for user management.
  name: YugabyteDB User management API
  slug: yugabytedb-user-management-api
- baseURL: https://cloud.yugabyte.com/api/public/v1
  baseurl_source: declared
  description: YBA Instance operations
  name: YugabyteDB YBA Instance API
  slug: yugabytedb-yba-instance-api
- baseURL: https://cloud.yugabyte.com/api/public/v1
  baseurl_source: declared
  description: The Ybc Management API from YugabyteDB — 5 operation(s) for ybc management.
  name: YugabyteDB Ybc Management API
  slug: yugabytedb-ybc-management-api
- baseURL: https://cloud.yugabyte.com/api/public/v1
  baseurl_source: declared
  description: Manage IP allow lists that control which client IP addresses or CIDR ranges are permitted to connect to a cluster.
  name: YugabyteDB Allow Lists API
  slug: yugabytedb-allow-lists-api
- baseURL: https://cloud.yugabyte.com/api/public/v1
  baseurl_source: declared
  description: Manage read replicas for a cluster to serve low-latency read requests from remote regions without affecting the primary cluster workload.
  name: YugabyteDB Read Replicas API
  slug: yugabytedb-read-replicas-api
artifact_total: 96
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Yugabyte Cloud backup-info API
  slug: open-yugabyte-backup-info-api
- collection_type: open
  name: Yugabyte Cloud backup-info cluster API
  slug: open-yugabyte-cluster-api
- collection_type: open
  name: Yugabyte Cloud backup-info cluster-info API
  slug: open-yugabyte-cluster-info-api
- collection_type: open
  name: Yugabyte Cloud backup-info pitr-info API
  slug: open-yugabyte-pitr-info-api
- collection_type: open
  name: Yugabyte Cloud backup-info restore-info API
  slug: open-yugabyte-restore-info-api
- collection_type: open
  name: Yugabyte Cloud backup-info voyager-info API
  slug: open-yugabyte-voyager-info-api
- collection_type: open
  name: Yugabyte Cloud backup-info voyager-metrics API
  slug: open-yugabyte-voyager-metrics-api
- collection_type: open
  name: Yugabyte Cloud backup-info Xcluster Metrics API
  slug: open-yugabyte-xcluster-metrics-api
- collection_type: open
  name: Yugabyte Cloud backup-info Xcluster Namespace Details API
  slug: open-yugabyte-xcluster-namespace-details-api
common:
- group: company
  title: ''
  type: Website
  url: https://www.yugabyte.com/
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/yugabyte/refs/heads/main/overlays/yugabyte-yugabyted-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/yugabyte-yugabyted-overlay.yaml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.yugabyte.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.yugabyte.com/
- group: docs
  title: ''
  type: APIReference
  url: https://api-docs.yugabyte.com/docs/managed-apis/9u5yqnccbe8lk-yugabyte-db-aeon-rest-api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.yugabyte.com/stable/quick-start/
- group: operate
  title: ''
  type: Support
  url: https://forum.yugabyte.com/
- group: company
  title: ''
  type: Blog
  url: https://www.yugabyte.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/yugabyte
- group: commercial
  title: ''
  type: Pricing
  url: https://www.yugabyte.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://cloud.yugabyte.com/signup
- group: start
  title: ''
  type: Login
  url: https://cloud.yugabyte.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.yugabyte.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.yugabyte.com/privacy-policy/
- group: operate
  title: ''
  type: StatusPage
  url: https://yugabytedb.statuspage.io/
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.yugabyte.com/stable/releases/
- group: auth
  title: ''
  type: TrustCenter
  url: https://compliance.yugabyte.com/
- group: auth
  title: ''
  type: Compliance
  url: https://www.yugabyte.com/compliance/
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/yugabyte/refs/heads/main/packages/yugabyte-packages.yml
  title: ''
  type: Packages
  url: packages/yugabyte-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/yugabyte/refs/heads/main/packages/yugabyte-packages.yml
  title: ''
  type: SDKs
  url: packages/yugabyte-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/yugabyte/refs/heads/main/cli/yugabyte-cli.yml
  title: ''
  type: CLI
  url: cli/yugabyte-cli.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/yugabyte/refs/heads/main/authentication/yugabyte-authentication.yml
  title: ''
  type: Authentication
  url: authentication/yugabyte-authentication.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/yugabyte/refs/heads/main/mcp/yugabyte-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/yugabyte-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/yugabyte/refs/heads/main/llms/yugabyte-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/yugabyte-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/yugabyte/refs/heads/main/well-known/yugabyte-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/yugabyte-well-known.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/yugabyte/refs/heads/main/errors/yugabyte-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/yugabyte-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/yugabyte/refs/heads/main/conventions/yugabyte-conventions.yml
  title: ''
  type: Conventions
  url: conventions/yugabyte-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/yugabyte/refs/heads/main/lifecycle/yugabyte-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/yugabyte-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/yugabyte/refs/heads/main/lifecycle/yugabyte-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/yugabyte-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/yugabyte/refs/heads/main/conformance/yugabyte-conformance.yml
  title: ''
  type: Conformance
  url: conformance/yugabyte-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/yugabyte/refs/heads/main/data-model/yugabyte-data-model.yml
  title: ''
  type: DataModel
  url: data-model/yugabyte-data-model.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/yugabyte/refs/heads/main/changelog/yugabyte-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/yugabyte-changelog.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/yugabyte/refs/heads/main/security/yugabyte-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/yugabyte-domain-security.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/yugabyte/refs/heads/main/agentic-access/yugabyte-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/yugabyte-agentic-access.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/yugabyte/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
crds:
- name: yugabytedb backup schedule
  url: https://raw.githubusercontent.com/api-evangelist/yugabyte/refs/heads/main/crd/yugabytedb-backup-schedule.yaml
- name: yugabytedb backup
  url: https://raw.githubusercontent.com/api-evangelist/yugabyte/refs/heads/main/crd/yugabytedb-backup.yaml
- name: yugabytedb dr config
  url: https://raw.githubusercontent.com/api-evangelist/yugabyte/refs/heads/main/crd/yugabytedb-dr-config.yaml
- name: yugabytedb pitr config
  url: https://raw.githubusercontent.com/api-evangelist/yugabyte/refs/heads/main/crd/yugabytedb-pitr-config.yaml
- name: yugabytedb release
  url: https://raw.githubusercontent.com/api-evangelist/yugabyte/refs/heads/main/crd/yugabytedb-release.yaml
- name: yugabytedb restore job
  url: https://raw.githubusercontent.com/api-evangelist/yugabyte/refs/heads/main/crd/yugabytedb-restore-job.yaml
- name: yugabytedb storage config
  url: https://raw.githubusercontent.com/api-evangelist/yugabyte/refs/heads/main/crd/yugabytedb-storage-config.yaml
- name: yugabytedb support bundle
  url: https://raw.githubusercontent.com/api-evangelist/yugabyte/refs/heads/main/crd/yugabytedb-support-bundle.yaml
- name: yugabytedb ybcertificate
  url: https://raw.githubusercontent.com/api-evangelist/yugabyte/refs/heads/main/crd/yugabytedb-ybcertificate.yaml
- name: yugabytedb ybplatform
  url: https://raw.githubusercontent.com/api-evangelist/yugabyte/refs/heads/main/crd/yugabytedb-ybplatform.yaml
- name: yugabytedb ybprovider
  url: https://raw.githubusercontent.com/api-evangelist/yugabyte/refs/heads/main/crd/yugabytedb-ybprovider.yaml
- name: yugabytedb ybuniverse
  url: https://raw.githubusercontent.com/api-evangelist/yugabyte/refs/heads/main/crd/yugabytedb-ybuniverse.yaml
created: '2026-07-17'
description: 'Yugabyte is the company behind YugabyteDB, an open source (Apache 2.0), PostgreSQL-compatible distributed SQL database built for cloud-native and mission-critical applications. It pairs PostgreSQL wire-compatibility (the YSQL API) and a Cassandra-inspired API (YCQL) with horizontal scalability, built-in resilience, automatic sharding, and automatic failover across multi-region and multi-cloud deployments. Yugabyte ships the database in three form factors: self-managed YugabyteDB, YugabyteDB Anywhere for private and hybrid clouds, and YugabyteDB Aeon, a fully managed database-as-a-service. Developers integrate through PostgreSQL-compatible smart drivers, the YugabyteDB Aeon REST management API, the open source ybm CLI, a Terraform provider, and the yugabyted local admin API.'
image: https://github.com/yugabyte.png
layout: provider
modified: '2026-07-21'
name: Yugabyte
nav: Providers
network: true
overview: 'Yugabyte publishes 81 APIs on the [APIs.io](https://apis.io/) network, including Backup Info API, Cluster API, Cluster Info API, and 78 more. Tagged areas include Company, Database, Distributed SQL, PostgreSQL, and Cloud.


  Yugabyte''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 28 more developer resources.'
random_paper: 16
score:
  band: strong
  composite: 57.1
  coverage:
    artifact_dirs: 22
    catalog_earned: 34.0
    catalog_earned_first_party: 0.0
    catalog_gap: 81.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 5.1
  facets:
    access_clarity: 60.5
    contract_governance: 4.5
    contract_quality: 47.8
    developer_ergonomics: 73.2
    discoverability: 70.4
    operational_transparency: 42.1
  previous_composite: 52.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 11.1
      derived: 6
      marker_coverage: 7.4
      total: 81
    mcp: derived
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-24'
  trend: rising
  upsert:
    applies: true
    score: 61.1
screenshot: https://raw.githubusercontent.com/api-evangelist/yugabyte/refs/heads/main/screenshots/yugabyte-2026-08-17T083024.png
security:
- kind: authentication
  name: Yugabyte Authentication
  slug: yugabyte-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Yugabyte Domain Security
  slug: yugabyte-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Yugabyte Trust Center
  slug: yugabyte-trust-center
  summary_line: SOC 2 Type II, SOC 3, ISO 27001, PCI DSS Level 1
slug: yugabyte
tags:
- Company
- Database
- Distributed SQL
- PostgreSQL
- Cloud
- Database-as-a-Service
- Open Source
- SQL
- Data
- Infrastructure
website: https://www.yugabyte.com/
---
