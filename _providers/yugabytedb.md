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
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.9
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 571
  human_in_the_loop: 33
  name: Yugabytedb Agentic Access
  operation_count: 895
  slug: yugabytedb-agentic-access
  summary_line: 895 operations · 571 acting · 33 human-in-the-loop
api_count: 73
apis:
- description: The Access Keys API from YugabyteDB — 3 operation(s) for access keys.
  name: YugabyteDB Access Keys API
  slug: yugabytedb-access-keys-api
- description: Retrieve account-level information for the authenticated user, including account ID and metadata used to scope all other API requests.
  name: YugabyteDB Accounts API
  slug: yugabytedb-accounts-api
- description: The Alerts API from YugabyteDB — 24 operation(s) for alerts.
  name: YugabyteDB Alerts API
  slug: yugabytedb-alerts-api
- description: Manage IP allow lists that control which client IP addresses or CIDR ranges are permitted to connect to a cluster.
  name: YugabyteDB AllowLists API
  slug: yugabytedb-allowlists-api
- description: The Asynchronous Replication API from YugabyteDB — 6 operation(s) for asynchronous replication.
  name: YugabyteDB Asynchronous Replication API
  slug: yugabytedb-asynchronous-replication-api
- description: The Audit API from YugabyteDB — 3 operation(s) for audit.
  name: YugabyteDB Audit API
  slug: yugabytedb-audit-api
- description: Authentication operations on YBA
  name: YugabyteDB Authentication API
  slug: yugabytedb-authentication-api
- description: The Availability Zones API from YugabyteDB — 4 operation(s) for availability zones.
  name: YugabyteDB Availability Zones API
  slug: yugabytedb-availability-zones-api
- description: Operations related to universe backup and restore
  name: YugabyteDB Backup and Restore API
  slug: yugabytedb-backup-and-restore-api
- description: Manage backup schedules and trigger on-demand backups for YugabyteDB Aeon clusters. Backups are stored in the same region as the cluster.
  name: YugabyteDB Backups API
  slug: yugabytedb-backups-api
- description: The Certificate Info API from YugabyteDB — 7 operation(s) for certificate info.
  name: YugabyteDB Certificate Info API
  slug: yugabytedb-certificate-info-api
- description: The Cloud providers API from YugabyteDB — 8 operation(s) for cloud providers.
  name: YugabyteDB Cloud providers API
  slug: yugabytedb-cloud-providers-api
- description: Create, list, retrieve, update, pause, resume, and delete YugabyteDB clusters within an account and project. Supports both single-region and multi-region cluster configurations.
  name: YugabyteDB Clusters API
  slug: yugabytedb-clusters-api
- description: CRUD operations for Continuous YBA Backups
  name: YugabyteDB Continuous Backup API
  slug: yugabytedb-continuous-backup-api
- description: The Custom CA Certificates API from YugabyteDB — 4 operation(s) for custom ca certificates.
  name: YugabyteDB Custom CA Certificates API
  slug: yugabytedb-custom-ca-certificates-api
- description: The Customer Configuration API from YugabyteDB — 7 operation(s) for customer configuration.
  name: YugabyteDB Customer Configuration API
  slug: yugabytedb-customer-configuration-api
- description: The Customer management API from YugabyteDB — 4 operation(s) for customer management.
  name: YugabyteDB Customer management API
  slug: yugabytedb-customer-management-api
- description: The Customer Tasks API from YugabyteDB — 8 operation(s) for customer tasks.
  name: YugabyteDB Customer Tasks API
  slug: yugabytedb-customer-tasks-api
- description: The Disaster Recovery API from YugabyteDB — 15 operation(s) for disaster recovery.
  name: YugabyteDB Disaster Recovery API
  slug: yugabytedb-disaster-recovery-api
- description: The Encryption at rest API from YugabyteDB — 7 operation(s) for encryption at rest.
  name: YugabyteDB Encryption at rest API
  slug: yugabytedb-encryption-at-rest-api
- description: The Extract metadata from remote tarball API from YugabyteDB — 2 operation(s) for extract metadata from remote tarball.
  name: YugabyteDB Extract metadata from remote tarball API
  slug: yugabytedb-extract-metadata-from-remote-tarball-api
- description: The GFlags Validation APIs API from YugabyteDB — 3 operation(s) for gflags validation apis.
  name: YugabyteDB GFlags Validation APIs API
  slug: yugabytedb-gflags-validation-apis-api
- description: The Grafana Dashboard API from YugabyteDB — 1 operation(s) for grafana dashboard.
  name: YugabyteDB Grafana Dashboard API
  slug: yugabytedb-grafana-dashboard-api
- description: The HA API from YugabyteDB — 3 operation(s) for ha.
  name: YugabyteDB HA API
  slug: yugabytedb-ha-api
- description: The Instance types API from YugabyteDB — 5 operation(s) for instance types.
  name: YugabyteDB Instance types API
  slug: yugabytedb-instance-types-api
- description: The Internal HA API from YugabyteDB — 5 operation(s) for internal ha.
  name: YugabyteDB Internal HA API
  slug: yugabytedb-internal-ha-api
- description: Isolated backup/restore of YBA to local filesystem
  name: YugabyteDB Isolated Backup API
  slug: yugabytedb-isolated-backup-api
- description: Job Scheduler
  name: YugabyteDB Job Scheduler API
  slug: yugabytedb-job-scheduler-api
- description: The KubernetesOverridesController API from YugabyteDB — 1 operation(s) for kubernetesoverridescontroller.
  name: YugabyteDB KubernetesOverridesController API
  slug: yugabytedb-kubernetesoverridescontroller-api
- description: The LDAP Role management API from YugabyteDB — 1 operation(s) for ldap role management.
  name: YugabyteDB LDAP Role management API
  slug: yugabytedb-ldap-role-management-api
- description: The LDAPOIDC Role management API from YugabyteDB — 3 operation(s) for ldapoidc role management.
  name: YugabyteDB LDAPOIDC Role management API
  slug: yugabytedb-ldapoidc-role-management-api
- description: The License management API from YugabyteDB — 2 operation(s) for license management.
  name: YugabyteDB License management API
  slug: yugabytedb-license-management-api
- description: The LoggingConfig API from YugabyteDB — 2 operation(s) for loggingconfig.
  name: YugabyteDB LoggingConfig API
  slug: yugabytedb-loggingconfig-api
- description: The Maintenance windows API from YugabyteDB — 4 operation(s) for maintenance windows.
  name: YugabyteDB Maintenance windows API
  slug: yugabytedb-maintenance-windows-api
- description: Configure scheduled maintenance windows for clusters to control when Yugabyte applies software patches and infrastructure updates.
  name: YugabyteDB MaintenanceWindows API
  slug: yugabytedb-maintenancewindows-api
- description: The Metrics API from YugabyteDB — 2 operation(s) for metrics.
  name: YugabyteDB Metrics API
  slug: yugabytedb-metrics-api
- description: The New Release management API from YugabyteDB — 2 operation(s) for new release management.
  name: YugabyteDB New Release management API
  slug: yugabytedb-new-release-management-api
- description: The Node Agents API from YugabyteDB — 5 operation(s) for node agents.
  name: YugabyteDB Node Agents API
  slug: yugabytedb-node-agents-api
- description: The Node instances API from YugabyteDB — 10 operation(s) for node instances.
  name: YugabyteDB Node instances API
  slug: yugabytedb-node-instances-api
- description: The PA Collector API from YugabyteDB — 4 operation(s) for pa collector.
  name: YugabyteDB PA Collector API
  slug: yugabytedb-pa-collector-api
- description: The PackagesController API from YugabyteDB — 1 operation(s) for packagescontroller.
  name: YugabyteDB PackagesController API
  slug: yugabytedb-packagescontroller-api
- description: The Performance Advisor API from YugabyteDB — 9 operation(s) for performance advisor.
  name: YugabyteDB Performance Advisor API
  slug: yugabytedb-performance-advisor-api
- description: The PITR management API from YugabyteDB — 5 operation(s) for pitr management.
  name: YugabyteDB PITR management API
  slug: yugabytedb-pitr-management-api
- description: The Platform Instance API from YugabyteDB — 4 operation(s) for platform instance.
  name: YugabyteDB Platform Instance API
  slug: yugabytedb-platform-instance-api
- description: The Platform Replication API from YugabyteDB — 4 operation(s) for platform replication.
  name: YugabyteDB Platform Replication API
  slug: yugabytedb-platform-replication-api
- description: The preview API from YugabyteDB — 2 operation(s) for preview.
  name: YugabyteDB preview API
  slug: yugabytedb-preview-api
- description: Manage projects within a YugabyteDB Aeon account. Projects provide organizational grouping for clusters, allow lists, and billing.
  name: YugabyteDB Projects API
  slug: yugabytedb-projects-api
- description: The RBAC management API from YugabyteDB — 5 operation(s) for rbac management.
  name: YugabyteDB RBAC management API
  slug: yugabytedb-rbac-management-api
- description: Manage read replicas for a cluster to serve low-latency read requests from remote regions without affecting the primary cluster workload.
  name: YugabyteDB ReadReplicas API
  slug: yugabytedb-readreplicas-api
- description: The Region management API from YugabyteDB — 5 operation(s) for region management.
  name: YugabyteDB Region management API
  slug: yugabytedb-region-management-api
- description: The Release management API from YugabyteDB — 3 operation(s) for release management.
  name: YugabyteDB Release management API
  slug: yugabytedb-release-management-api
- description: Restore a cluster from a previously created backup snapshot, enabling point-in-time recovery of database state.
  name: YugabyteDB Restores API
  slug: yugabytedb-restores-api
- description: The Runtime configuration API from YugabyteDB — 6 operation(s) for runtime configuration.
  name: YugabyteDB Runtime configuration API
  slug: yugabytedb-runtime-configuration-api
- description: The Schedule management API from YugabyteDB — 7 operation(s) for schedule management.
  name: YugabyteDB Schedule management API
  slug: yugabytedb-schedule-management-api
- description: The Session management API from YugabyteDB — 9 operation(s) for session management.
  name: YugabyteDB Session management API
  slug: yugabytedb-session-management-api
- description: The Support Bundle management API from YugabyteDB — 5 operation(s) for support bundle management.
  name: YugabyteDB Support Bundle management API
  slug: yugabytedb-support-bundle-management-api
- description: The Table management API from YugabyteDB — 8 operation(s) for table management.
  name: YugabyteDB Table management API
  slug: yugabytedb-table-management-api
- description: The Tablet server management API from YugabyteDB — 1 operation(s) for tablet server management.
  name: YugabyteDB Tablet server management API
  slug: yugabytedb-tablet-server-management-api
- description: The Telemetry Provider API from YugabyteDB — 3 operation(s) for telemetry provider.
  name: YugabyteDB Telemetry Provider API
  slug: yugabytedb-telemetry-provider-api
- description: The Universe actions API from YugabyteDB — 1 operation(s) for universe actions.
  name: YugabyteDB Universe actions API
  slug: yugabytedb-universe-actions-api
- description: CRUD operations for a Universe
  name: YugabyteDB Universe API
  slug: yugabytedb-universe-api
- description: The Universe CDC Management API from YugabyteDB — 3 operation(s) for universe cdc management.
  name: YugabyteDB Universe CDC Management API
  slug: yugabytedb-universe-cdc-management-api
- description: The Universe database management API from YugabyteDB — 6 operation(s) for universe database management.
  name: YugabyteDB Universe database management API
  slug: yugabytedb-universe-database-management-api
- description: The Universe information API from YugabyteDB — 11 operation(s) for universe information.
  name: YugabyteDB Universe information API
  slug: yugabytedb-universe-information-api
- description: The Universe management API from YugabyteDB — 11 operation(s) for universe management.
  name: YugabyteDB Universe management API
  slug: yugabytedb-universe-management-api
- description: The Universe node metadata (metamaster) API from YugabyteDB — 6 operation(s) for universe node metadata (metamaster).
  name: YugabyteDB Universe node metadata (metamaster) API
  slug: yugabytedb-universe-node-metadata-metamaster-api
- description: The Universe performance suggestions API from YugabyteDB — 3 operation(s) for universe performance suggestions.
  name: YugabyteDB Universe performance suggestions API
  slug: yugabytedb-universe-performance-suggestions-api
- description: The Universe Upgrades Management API from YugabyteDB — 20 operation(s) for universe upgrades management.
  name: YugabyteDB Universe Upgrades Management API
  slug: yugabytedb-universe-upgrades-management-api
- description: The UniverseClusterMutations API from YugabyteDB — 4 operation(s) for universeclustermutations.
  name: YugabyteDB UniverseClusterMutations API
  slug: yugabytedb-universeclustermutations-api
- description: The Upload Release packages API from YugabyteDB — 2 operation(s) for upload release packages.
  name: YugabyteDB Upload Release packages API
  slug: yugabytedb-upload-release-packages-api
- description: The User management API from YugabyteDB — 6 operation(s) for user management.
  name: YugabyteDB User management API
  slug: yugabytedb-user-management-api
- description: YBA Instance operations
  name: YugabyteDB YBA Instance API
  slug: yugabytedb-yba-instance-api
- description: The Ybc Management API from YugabyteDB — 5 operation(s) for ybc management.
  name: YugabyteDB Ybc Management API
  slug: yugabytedb-ybc-management-api
arazzos:
- description: Add a read replica to a cluster and confirm it becomes ACTIVE.
  name: YugabyteDB Aeon Add Read Replica
  slug: yugabytedb-add-read-replica-workflow
- description: Take an on-demand backup, poll until it succeeds, then restore the cluster from it.
  name: YugabyteDB Aeon Backup and Restore
  slug: yugabytedb-backup-and-restore-workflow
- description: Create an IP allow list in a project and confirm its CIDR entries.
  name: YugabyteDB Aeon Configure IP Allow List
  slug: yugabytedb-configure-allow-list-workflow
- description: Read the current maintenance window for a cluster, then update its schedule.
  name: YugabyteDB Aeon Configure Maintenance Window
  slug: yugabytedb-configure-maintenance-window-workflow
- description: Resolve the active account and project, then enumerate the clusters within it.
  name: YugabyteDB Aeon Discover Account Clusters
  slug: yugabytedb-discover-account-clusters-workflow
- description: Pause or resume a cluster to control compute billing, then confirm the new state.
  name: YugabyteDB Aeon Pause or Resume Cluster
  slug: yugabytedb-pause-resume-cluster-workflow
- description: Create a cluster, poll until it becomes ACTIVE, then read its connection endpoints.
  name: YugabyteDB Aeon Provision Cluster
  slug: yugabytedb-provision-cluster-workflow
- description: Read a cluster, submit an updated specification, and poll until it returns to ACTIVE.
  name: YugabyteDB Aeon Scale Cluster
  slug: yugabytedb-scale-cluster-workflow
artifact_total: 273
collections:
- collection_type: postman
  name: YugabyteDB Aeon REST Access Keys API
  slug: postman-yugabytedb-access-keys-api
- collection_type: postman
  name: YugabyteDB Aeon REST Access Keys Accounts API
  slug: postman-yugabytedb-accounts-api
- collection_type: postman
  name: YugabyteDB Aeon REST Access Keys Alerts API
  slug: postman-yugabytedb-alerts-api
- collection_type: postman
  name: YugabyteDB Aeon REST Access Keys AllowLists API
  slug: postman-yugabytedb-allowlists-api
- collection_type: postman
  name: YugabyteDB Aeon REST Access Keys Asynchronous Replication API
  slug: postman-yugabytedb-asynchronous-replication-api
- collection_type: postman
  name: YugabyteDB Aeon REST Access Keys Audit API
  slug: postman-yugabytedb-audit-api
- collection_type: postman
  name: YugabyteDB Aeon REST Access Keys Authentication API
  slug: postman-yugabytedb-authentication-api
- collection_type: postman
  name: YugabyteDB Aeon REST Access Keys Availability Zones API
  slug: postman-yugabytedb-availability-zones-api
- collection_type: postman
  name: YugabyteDB Aeon REST Access Keys Backup and Restore API
  slug: postman-yugabytedb-backup-and-restore-api
- collection_type: postman
  name: YugabyteDB Aeon REST Access Keys Backups API
  slug: postman-yugabytedb-backups-api
- collection_type: postman
  name: YugabyteDB Aeon REST Access Keys Certificate Info API
  slug: postman-yugabytedb-certificate-info-api
- collection_type: postman
  name: YugabyteDB Aeon REST Access Keys Cloud providers API
  slug: postman-yugabytedb-cloud-providers-api
- collection_type: postman
  name: YugabyteDB Aeon REST Access Keys Clusters API
  slug: postman-yugabytedb-clusters-api
- collection_type: postman
  name: YugabyteDB Aeon REST Access Keys Continuous Backup API
  slug: postman-yugabytedb-continuous-backup-api
- collection_type: postman
  name: YugabyteDB Aeon REST Access Keys Custom CA Certificates API
  slug: postman-yugabytedb-custom-ca-certificates-api
- collection_type: postman
  name: YugabyteDB Aeon REST Access Keys Customer Configuration API
  slug: postman-yugabytedb-customer-configuration-api
- collection_type: postman
  name: YugabyteDB Aeon REST Access Keys Customer management API
  slug: postman-yugabytedb-customer-management-api
- collection_type: postman
  name: YugabyteDB Aeon REST Access Keys Customer Tasks API
  slug: postman-yugabytedb-customer-tasks-api
- collection_type: postman
  name: YugabyteDB Aeon REST Access Keys Disaster Recovery API
  slug: postman-yugabytedb-disaster-recovery-api
- collection_type: postman
  name: YugabyteDB Aeon REST Access Keys Encryption at rest API
  slug: postman-yugabytedb-encryption-at-rest-api
- collection_type: postman
  name: YugabyteDB Aeon REST Access Keys Extract metadata from remote tarball API
  slug: postman-yugabytedb-extract-metadata-from-remote-tarball-api
- collection_type: postman
  name: YugabyteDB Aeon REST Access Keys GFlags Validation APIs API
  slug: postman-yugabytedb-gflags-validation-apis-api
- collection_type: postman
  name: YugabyteDB Aeon REST Access Keys Grafana Dashboard API
  slug: postman-yugabytedb-grafana-dashboard-api
- collection_type: postman
  name: YugabyteDB Aeon REST Access Keys HA API
  slug: postman-yugabytedb-ha-api
- collection_type: postman
  name: YugabyteDB Aeon REST Access Keys Instance types API
  slug: postman-yugabytedb-instance-types-api
- collection_type: postman
  name: YugabyteDB Aeon REST Access Keys Internal HA API
  slug: postman-yugabytedb-internal-ha-api
- collection_type: postman
  name: YugabyteDB Aeon REST Access Keys Isolated Backup API
  slug: postman-yugabytedb-isolated-backup-api
- collection_type: postman
  name: YugabyteDB Aeon REST Access Keys Job Scheduler API
  slug: postman-yugabytedb-job-scheduler-api
- collection_type: postman
  name: YugabyteDB Aeon REST Access Keys KubernetesOverridesController API
  slug: postman-yugabytedb-kubernetesoverridescontroller-api
- collection_type: postman
  name: YugabyteDB Aeon REST Access Keys LDAP Role management API
  slug: postman-yugabytedb-ldap-role-management-api
- collection_type: postman
  name: YugabyteDB Aeon REST Access Keys LDAPOIDC Role management API
  slug: postman-yugabytedb-ldapoidc-role-management-api
- collection_type: postman
  name: YugabyteDB Aeon REST Access Keys License management API
  slug: postman-yugabytedb-license-management-api
- collection_type: postman
  name: YugabyteDB Aeon REST Access Keys LoggingConfig API
  slug: postman-yugabytedb-loggingconfig-api
- collection_type: postman
  name: YugabyteDB Aeon REST Access Keys Maintenance windows API
  slug: postman-yugabytedb-maintenance-windows-api
- collection_type: postman
  name: YugabyteDB Aeon REST Access Keys MaintenanceWindows API
  slug: postman-yugabytedb-maintenancewindows-api
- collection_type: postman
  name: YugabyteDB Aeon REST Access Keys Metrics API
  slug: postman-yugabytedb-metrics-api
- collection_type: postman
  name: YugabyteDB Aeon REST Access Keys New Release management API
  slug: postman-yugabytedb-new-release-management-api
- collection_type: postman
  name: YugabyteDB Aeon REST Access Keys Node Agents API
  slug: postman-yugabytedb-node-agents-api
- collection_type: postman
  name: YugabyteDB Aeon REST Access Keys Node instances API
  slug: postman-yugabytedb-node-instances-api
- collection_type: postman
  name: YugabyteDB Aeon REST Access Keys PA Collector API
  slug: postman-yugabytedb-pa-collector-api
- collection_type: postman
  name: YugabyteDB Aeon REST Access Keys PackagesController API
  slug: postman-yugabytedb-packagescontroller-api
- collection_type: postman
  name: YugabyteDB Aeon REST Access Keys Performance Advisor API
  slug: postman-yugabytedb-performance-advisor-api
- collection_type: postman
  name: YugabyteDB Aeon REST Access Keys PITR management API
  slug: postman-yugabytedb-pitr-management-api
- collection_type: postman
  name: YugabyteDB Aeon REST Access Keys Platform Instance API
  slug: postman-yugabytedb-platform-instance-api
- collection_type: postman
  name: YugabyteDB Aeon REST Access Keys Platform Replication API
  slug: postman-yugabytedb-platform-replication-api
- collection_type: postman
  name: YugabyteDB Aeon REST Access Keys preview API
  slug: postman-yugabytedb-preview-api
- collection_type: postman
  name: YugabyteDB Aeon REST Access Keys Projects API
  slug: postman-yugabytedb-projects-api
- collection_type: postman
  name: YugabyteDB Aeon REST Access Keys RBAC management API
  slug: postman-yugabytedb-rbac-management-api
- collection_type: postman
  name: YugabyteDB Aeon REST Access Keys ReadReplicas API
  slug: postman-yugabytedb-readreplicas-api
- collection_type: postman
  name: YugabyteDB Aeon REST Access Keys Region management API
  slug: postman-yugabytedb-region-management-api
- collection_type: postman
  name: YugabyteDB Aeon REST Access Keys Release management API
  slug: postman-yugabytedb-release-management-api
- collection_type: postman
  name: YugabyteDB Aeon REST Access Keys Restores API
  slug: postman-yugabytedb-restores-api
- collection_type: postman
  name: YugabyteDB Aeon REST Access Keys Runtime configuration API
  slug: postman-yugabytedb-runtime-configuration-api
- collection_type: postman
  name: YugabyteDB Aeon REST Access Keys Schedule management API
  slug: postman-yugabytedb-schedule-management-api
- collection_type: postman
  name: YugabyteDB Aeon REST Access Keys Session management API
  slug: postman-yugabytedb-session-management-api
- collection_type: postman
  name: YugabyteDB Aeon REST Access Keys Support Bundle management API
  slug: postman-yugabytedb-support-bundle-management-api
- collection_type: postman
  name: YugabyteDB Aeon REST Access Keys Table management API
  slug: postman-yugabytedb-table-management-api
- collection_type: postman
  name: YugabyteDB Aeon REST Access Keys Tablet server management API
  slug: postman-yugabytedb-tablet-server-management-api
- collection_type: postman
  name: YugabyteDB Aeon REST Access Keys Telemetry Provider API
  slug: postman-yugabytedb-telemetry-provider-api
- collection_type: postman
  name: YugabyteDB Aeon REST Access Keys Universe actions API
  slug: postman-yugabytedb-universe-actions-api
- collection_type: postman
  name: YugabyteDB Aeon REST Access Keys Universe API
  slug: postman-yugabytedb-universe-api
- collection_type: postman
  name: YugabyteDB Aeon REST Access Keys Universe CDC Management API
  slug: postman-yugabytedb-universe-cdc-management-api
- collection_type: postman
  name: YugabyteDB Aeon REST Access Keys Universe database management API
  slug: postman-yugabytedb-universe-database-management-api
- collection_type: postman
  name: YugabyteDB Aeon REST Access Keys Universe information API
  slug: postman-yugabytedb-universe-information-api
- collection_type: postman
  name: YugabyteDB Aeon REST Access Keys Universe management API
  slug: postman-yugabytedb-universe-management-api
- collection_type: postman
  name: YugabyteDB Aeon REST Access Keys Universe node metadata (metamaster) API
  slug: postman-yugabytedb-universe-node-metadata-metamaster-api
- collection_type: postman
  name: YugabyteDB Aeon REST Access Keys Universe performance suggestions API
  slug: postman-yugabytedb-universe-performance-suggestions-api
- collection_type: postman
  name: YugabyteDB Aeon REST Access Keys Universe Upgrades Management API
  slug: postman-yugabytedb-universe-upgrades-management-api
- collection_type: postman
  name: YugabyteDB Aeon REST Access Keys UniverseClusterMutations API
  slug: postman-yugabytedb-universeclustermutations-api
- collection_type: postman
  name: YugabyteDB Aeon REST Access Keys Upload Release packages API
  slug: postman-yugabytedb-upload-release-packages-api
- collection_type: postman
  name: YugabyteDB Aeon REST Access Keys User management API
  slug: postman-yugabytedb-user-management-api
- collection_type: postman
  name: YugabyteDB Aeon REST Access Keys YBA Instance API
  slug: postman-yugabytedb-yba-instance-api
- collection_type: postman
  name: YugabyteDB Aeon REST Access Keys Ybc Management API
  slug: postman-yugabytedb-ybc-management-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: YugabyteDB Aeon REST Access Keys API
  slug: open-yugabytedb-access-keys-api
- collection_type: open
  name: YugabyteDB Aeon REST Access Keys Accounts API
  slug: open-yugabytedb-accounts-api
- collection_type: open
  name: YugabyteDB Aeon REST API
  slug: open-yugabytedb-aeon
- collection_type: open
  name: YugabyteDB Aeon REST Access Keys Alerts API
  slug: open-yugabytedb-alerts-api
- collection_type: open
  name: YugabyteDB Aeon REST Access Keys AllowLists API
  slug: open-yugabytedb-allowlists-api
- collection_type: open
  name: YugabyteDB Aeon REST Access Keys Asynchronous Replication API
  slug: open-yugabytedb-asynchronous-replication-api
- collection_type: open
  name: YugabyteDB Aeon REST Access Keys Audit API
  slug: open-yugabytedb-audit-api
- collection_type: open
  name: YugabyteDB Aeon REST Access Keys Authentication API
  slug: open-yugabytedb-authentication-api
- collection_type: open
  name: YugabyteDB Aeon REST Access Keys Availability Zones API
  slug: open-yugabytedb-availability-zones-api
- collection_type: open
  name: YugabyteDB Aeon REST Access Keys Backup and Restore API
  slug: open-yugabytedb-backup-and-restore-api
- collection_type: open
  name: YugabyteDB Aeon REST Access Keys Backups API
  slug: open-yugabytedb-backups-api
- collection_type: open
  name: YugabyteDB Aeon REST Access Keys Certificate Info API
  slug: open-yugabytedb-certificate-info-api
- collection_type: open
  name: YugabyteDB Aeon REST Access Keys Cloud providers API
  slug: open-yugabytedb-cloud-providers-api
- collection_type: open
  name: YugabyteDB Aeon REST Access Keys Clusters API
  slug: open-yugabytedb-clusters-api
- collection_type: open
  name: YugabyteDB Aeon REST Access Keys Continuous Backup API
  slug: open-yugabytedb-continuous-backup-api
- collection_type: open
  name: YugabyteDB Aeon REST Access Keys Custom CA Certificates API
  slug: open-yugabytedb-custom-ca-certificates-api
- collection_type: open
  name: YugabyteDB Aeon REST Access Keys Customer Configuration API
  slug: open-yugabytedb-customer-configuration-api
- collection_type: open
  name: YugabyteDB Aeon REST Access Keys Customer management API
  slug: open-yugabytedb-customer-management-api
- collection_type: open
  name: YugabyteDB Aeon REST Access Keys Customer Tasks API
  slug: open-yugabytedb-customer-tasks-api
- collection_type: open
  name: YugabyteDB Aeon REST Access Keys Disaster Recovery API
  slug: open-yugabytedb-disaster-recovery-api
- collection_type: open
  name: YugabyteDB Aeon REST Access Keys Encryption at rest API
  slug: open-yugabytedb-encryption-at-rest-api
- collection_type: open
  name: YugabyteDB Aeon REST Access Keys Extract metadata from remote tarball API
  slug: open-yugabytedb-extract-metadata-from-remote-tarball-api
- collection_type: open
  name: YugabyteDB Aeon REST Access Keys GFlags Validation APIs API
  slug: open-yugabytedb-gflags-validation-apis-api
- collection_type: open
  name: YugabyteDB Aeon REST Access Keys Grafana Dashboard API
  slug: open-yugabytedb-grafana-dashboard-api
- collection_type: open
  name: YugabyteDB Aeon REST Access Keys HA API
  slug: open-yugabytedb-ha-api
- collection_type: open
  name: YugabyteDB Aeon REST Access Keys Instance types API
  slug: open-yugabytedb-instance-types-api
- collection_type: open
  name: YugabyteDB Aeon REST Access Keys Internal HA API
  slug: open-yugabytedb-internal-ha-api
- collection_type: open
  name: YugabyteDB Aeon REST Access Keys Isolated Backup API
  slug: open-yugabytedb-isolated-backup-api
- collection_type: open
  name: YugabyteDB Aeon REST Access Keys Job Scheduler API
  slug: open-yugabytedb-job-scheduler-api
- collection_type: open
  name: YugabyteDB Aeon REST Access Keys KubernetesOverridesController API
  slug: open-yugabytedb-kubernetesoverridescontroller-api
- collection_type: open
  name: YugabyteDB Aeon REST Access Keys LDAP Role management API
  slug: open-yugabytedb-ldap-role-management-api
- collection_type: open
  name: YugabyteDB Aeon REST Access Keys LDAPOIDC Role management API
  slug: open-yugabytedb-ldapoidc-role-management-api
- collection_type: open
  name: YugabyteDB Aeon REST Access Keys License management API
  slug: open-yugabytedb-license-management-api
- collection_type: open
  name: YugabyteDB Aeon REST Access Keys LoggingConfig API
  slug: open-yugabytedb-loggingconfig-api
- collection_type: open
  name: YugabyteDB Aeon REST Access Keys Maintenance windows API
  slug: open-yugabytedb-maintenance-windows-api
- collection_type: open
  name: YugabyteDB Aeon REST Access Keys MaintenanceWindows API
  slug: open-yugabytedb-maintenancewindows-api
- collection_type: open
  name: YugabyteDB Aeon REST Access Keys Metrics API
  slug: open-yugabytedb-metrics-api
- collection_type: open
  name: YugabyteDB Aeon REST Access Keys New Release management API
  slug: open-yugabytedb-new-release-management-api
- collection_type: open
  name: YugabyteDB Aeon REST Access Keys Node Agents API
  slug: open-yugabytedb-node-agents-api
- collection_type: open
  name: YugabyteDB Aeon REST Access Keys Node instances API
  slug: open-yugabytedb-node-instances-api
- collection_type: open
  name: YugabyteDB Aeon REST Access Keys PA Collector API
  slug: open-yugabytedb-pa-collector-api
- collection_type: open
  name: YugabyteDB Aeon REST Access Keys PackagesController API
  slug: open-yugabytedb-packagescontroller-api
- collection_type: open
  name: YugabyteDB Aeon REST Access Keys Performance Advisor API
  slug: open-yugabytedb-performance-advisor-api
- collection_type: open
  name: YugabyteDB Aeon REST Access Keys PITR management API
  slug: open-yugabytedb-pitr-management-api
- collection_type: open
  name: YugabyteDB Aeon REST Access Keys Platform Instance API
  slug: open-yugabytedb-platform-instance-api
- collection_type: open
  name: YugabyteDB Aeon REST Access Keys Platform Replication API
  slug: open-yugabytedb-platform-replication-api
- collection_type: open
  name: YugabyteDB Aeon REST Access Keys Projects API
  slug: open-yugabytedb-projects-api
- collection_type: open
  name: YugabyteDB Aeon REST Access Keys RBAC management API
  slug: open-yugabytedb-rbac-management-api
- collection_type: open
  name: YugabyteDB Aeon REST Access Keys ReadReplicas API
  slug: open-yugabytedb-readreplicas-api
- collection_type: open
  name: YugabyteDB Aeon REST Access Keys Region management API
  slug: open-yugabytedb-region-management-api
- collection_type: open
  name: YugabyteDB Aeon REST Access Keys Release management API
  slug: open-yugabytedb-release-management-api
- collection_type: open
  name: YugabyteDB Aeon REST Access Keys Restores API
  slug: open-yugabytedb-restores-api
- collection_type: open
  name: YugabyteDB Aeon REST Access Keys Runtime configuration API
  slug: open-yugabytedb-runtime-configuration-api
- collection_type: open
  name: YugabyteDB Aeon REST Access Keys Schedule management API
  slug: open-yugabytedb-schedule-management-api
- collection_type: open
  name: YugabyteDB Aeon REST Access Keys Session management API
  slug: open-yugabytedb-session-management-api
- collection_type: open
  name: YugabyteDB Aeon REST Access Keys Support Bundle management API
  slug: open-yugabytedb-support-bundle-management-api
- collection_type: open
  name: YugabyteDB Aeon REST Access Keys Table management API
  slug: open-yugabytedb-table-management-api
- collection_type: open
  name: YugabyteDB Aeon REST Access Keys Tablet server management API
  slug: open-yugabytedb-tablet-server-management-api
- collection_type: open
  name: YugabyteDB Aeon REST Access Keys Telemetry Provider API
  slug: open-yugabytedb-telemetry-provider-api
- collection_type: open
  name: YugabyteDB Aeon REST Access Keys Universe actions API
  slug: open-yugabytedb-universe-actions-api
- collection_type: open
  name: YugabyteDB Aeon REST Access Keys Universe API
  slug: open-yugabytedb-universe-api
- collection_type: open
  name: YugabyteDB Aeon REST Access Keys Universe CDC Management API
  slug: open-yugabytedb-universe-cdc-management-api
- collection_type: open
  name: YugabyteDB Aeon REST Access Keys Universe database management API
  slug: open-yugabytedb-universe-database-management-api
- collection_type: open
  name: YugabyteDB Aeon REST Access Keys Universe information API
  slug: open-yugabytedb-universe-information-api
- collection_type: open
  name: YugabyteDB Aeon REST Access Keys Universe management API
  slug: open-yugabytedb-universe-management-api
- collection_type: open
  name: YugabyteDB Aeon REST Access Keys Universe node metadata (metamaster) API
  slug: open-yugabytedb-universe-node-metadata-metamaster-api
- collection_type: open
  name: YugabyteDB Aeon REST Access Keys Universe performance suggestions API
  slug: open-yugabytedb-universe-performance-suggestions-api
- collection_type: open
  name: YugabyteDB Aeon REST Access Keys Universe Upgrades Management API
  slug: open-yugabytedb-universe-upgrades-management-api
- collection_type: open
  name: YugabyteDB Aeon REST Access Keys UniverseClusterMutations API
  slug: open-yugabytedb-universeclustermutations-api
- collection_type: open
  name: YugabyteDB Aeon REST Access Keys Upload Release packages API
  slug: open-yugabytedb-upload-release-packages-api
- collection_type: open
  name: YugabyteDB Aeon REST Access Keys User management API
  slug: open-yugabytedb-user-management-api
- collection_type: open
  name: YugabyteDB Aeon REST Access Keys YBA Instance API
  slug: open-yugabytedb-yba-instance-api
- collection_type: open
  name: YugabyteDB Aeon REST Access Keys Ybc Management API
  slug: open-yugabytedb-ybc-management-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/yugabytedb/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/yugabytedb-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/yugabytedb-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/yugabytedb-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/yugabytedb-authentication.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/yugabytedb-add-read-replica-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/yugabytedb-backup-and-restore-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/yugabytedb-configure-allow-list-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/yugabytedb-configure-maintenance-window-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/yugabytedb-discover-account-clusters-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/yugabytedb-pause-resume-cluster-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/yugabytedb-provision-cluster-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/yugabytedb-scale-cluster-workflow.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/yugabyte
- group: company
  title: ''
  type: Website
  url: https://www.yugabyte.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.yugabyte.com/
- group: docs
  title: ''
  type: APIReference
  url: https://api-docs.yugabyte.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.yugabyte.com/stable/quick-start-yugabytedb-managed/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.yugabyte.com/stable/develop/
- group: start
  title: ''
  type: Console
  url: https://cloud.yugabyte.com/
- group: start
  title: ''
  type: Signup
  url: https://cloud.yugabyte.com/signup
- group: start
  title: ''
  type: Login
  url: https://cloud.yugabyte.com/login
- group: commercial
  title: ''
  type: Pricing
  url: https://www.yugabyte.com/pricing/
- group: company
  title: ''
  type: Blog
  url: https://www.yugabyte.com/blog/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.yugabyte.com/yugabytedb-managed-service-terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.yugabyte.com/privacy-policy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.yugabyte.com/
- group: operate
  title: ''
  type: Support
  url: https://support.yugabyte.com/
- group: operate
  title: ''
  type: Support
  url: https://forum.yugabyte.com/
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://docs.yugabyte.com/stable/releases/
- group: learn
  title: ''
  type: Academy
  url: https://university.yugabyte.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/yugabyte
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/yugabyte/yugabyte-db
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/yugabytedb
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/c/yugabyte
- group: docs
  title: ''
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/yugabytedb/refs/heads/main/json-schema/yugabytedb-cluster-schema.json
- group: design
  title: ''
  type: JSONLD
  url: https://raw.githubusercontent.com/api-evangelist/yugabytedb/refs/heads/main/json-ld/yugabytedb-context.jsonld
- group: build
  title: MCP Server
  type: SDKs
  url: https://github.com/yugabyte/yugabytedb-mcp-server
- group: build
  title: AI Agent Skills
  type: SDKs
  url: https://github.com/yugabyte/yugabytedb-skills
- group: build
  title: Java YSQL Smart Driver
  type: SDKs
  url: https://search.maven.org/artifact/com.yugabyte/jdbc-yugabytedb
- group: build
  title: Go YSQL Smart Driver
  type: SDKs
  url: https://github.com/yugabyte/pgx
- group: build
  title: Python Django Backend
  type: SDKs
  url: https://pypi.org/project/django-yugabytedb/
- group: build
  title: Python SQLAlchemy Dialect
  type: SDKs
  url: https://github.com/yugabyte/sqlalchemy-yugabytedb
- group: build
  title: Ruby ActiveRecord Adapter
  type: SDKs
  url: https://rubygems.org/gems/activerecord-yugabytedb-adapter
- group: build
  title: Node.js Sequelize Package
  type: SDKs
  url: https://www.npmjs.com/package/sequelize-yugabytedb
- group: build
  title: Go GORM Driver
  type: SDKs
  url: https://github.com/yugabyte/gorm-yugabytedb
- group: build
  title: Java R2DBC YSQL Driver
  type: SDKs
  url: https://github.com/yugabyte/r2dbc-yugabytedb
- group: build
  title: Python LangChain Integration
  type: SDKs
  url: https://pypi.org/project/langchain-yugabytedb/
- group: build
  title: C++ YCQL Driver
  type: SDKs
  url: https://github.com/yugabyte/cassandra-cpp-driver
- group: build
  title: Java YCQL Driver
  type: SDKs
  url: https://github.com/yugabyte/cassandra-java-driver
- group: build
  title: Python YCQL Driver
  type: SDKs
  url: https://github.com/yugabyte/cassandra-python-driver
- group: build
  title: Node.js YCQL Driver
  type: SDKs
  url: https://github.com/yugabyte/cassandra-nodejs-driver
- group: build
  title: C# YCQL Driver
  type: SDKs
  url: https://github.com/yugabyte/cassandra-csharp-driver
- group: build
  title: Go YCQL Driver
  type: SDKs
  url: https://github.com/yugabyte/gocql
- group: build
  title: Java Spring Data Module
  type: SDKs
  url: https://github.com/yugabyte/spring-data-yugabytedb
- group: build
  title: Database Migration Tool (yb-voyager)
  type: CLI
  url: https://github.com/yugabyte/yb-voyager
- group: build
  title: YCQL Shell (cqlsh)
  type: CLI
  url: https://github.com/yugabyte/cqlsh
- group: auth
  title: ''
  type: Compliance
  url: https://github.com/yugabyte/yuga-bench
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/yugabyte/yugabytedb-pgcompare
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/yugabyte/yugabyte-prometheus-sizing-calculator
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/yugabyte/yb-log-analyzer-py
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/yugabyte/cbo_stat_dump
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/yugabyte/yb-tools
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/yugabyte/yugabyte-db-action
- group: build
  title: Workload Generator (Java)
  type: CodeExamples
  url: https://github.com/yugabyte/yb-sample-apps
- group: build
  title: Blog Demonstrations
  type: CodeExamples
  url: https://github.com/yugabyte/blog-examples
- group: build
  title: CDC Connector Examples
  type: CodeExamples
  url: https://github.com/yugabyte/cdc-examples
- group: build
  title: Spring Boot Samples
  type: CodeExamples
  url: https://github.com/yugabyte/spring-boot-sample-apps
- group: build
  title: Spring Data Sample
  type: CodeExamples
  url: https://github.com/yugabyte/spring-data-yugabytedb-example
- group: build
  title: Microservices Demo (Hipster Shop fork)
  type: CodeExamples
  url: https://github.com/yugabyte/microservices-demo
- group: build
  title: Yugastore E-Commerce App
  type: CodeExamples
  url: https://github.com/yugabyte/yugastore
- group: build
  title: IoT Fleet Management Sample
  type: CodeExamples
  url: https://github.com/yugabyte/yb-iot-fleet-management
- group: build
  title: ORM Examples
  type: CodeExamples
  url: https://github.com/YugabyteDB-Samples/orm-examples
- group: build
  title: Workload Simulator
  type: CodeExamples
  url: https://github.com/YugabyteDB-Samples/yb-workload-simulator
- group: learn
  title: Distributed SQL Lessons
  type: Tutorials
  url: https://github.com/yugabyte/learn-yugabyte
- group: learn
  title: Code Labs
  type: Tutorials
  url: https://github.com/yugabyte/codelabs
- group: build
  title: Helm Charts
  type: SDKs
  url: https://github.com/yugabyte/charts
- group: build
  title: Terraform AWS Module
  type: SDKs
  url: https://github.com/yugabyte/terraform-aws-yugabyte
- group: build
  title: Terraform Azure Module
  type: SDKs
  url: https://github.com/yugabyte/terraform-azure-yugabyte
- group: build
  title: Terraform GCP Module
  type: SDKs
  url: https://github.com/yugabyte/terraform-gcp-yugabyte
- group: build
  title: AWS CloudFormation Template
  type: SDKs
  url: https://github.com/yugabyte/aws-cloudformation
- group: build
  title: Azure Resource Manager Template
  type: SDKs
  url: https://github.com/yugabyte/azure-resource-manager
- group: build
  title: GCP Deployment Manager
  type: SDKs
  url: https://github.com/yugabyte/gcp-deployment-manager
- group: build
  title: Flyway Plugin
  type: SDKs
  url: https://github.com/yugabyte/flyway-tests
- group: build
  title: HashiCorp Vault Plugin
  type: SDKs
  url: https://github.com/yugabyte/hashicorp-vault-ysql-plugin
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/yugabyte/cloud-resource-cleanup
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/yugabyte/yugabytedb-mcp-server
- group: agent
  title: ''
  type: AgentSkills
  url: https://github.com/yugabyte/yugabytedb-skills
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.yugabyte.com/llms.txt
crds:
- name: yugabytedb backup schedule
  url: https://raw.githubusercontent.com/api-evangelist/yugabytedb/refs/heads/main/crd/yugabytedb-backup-schedule.yaml
- name: yugabytedb backup
  url: https://raw.githubusercontent.com/api-evangelist/yugabytedb/refs/heads/main/crd/yugabytedb-backup.yaml
- name: yugabytedb dr config
  url: https://raw.githubusercontent.com/api-evangelist/yugabytedb/refs/heads/main/crd/yugabytedb-dr-config.yaml
- name: yugabytedb pitr config
  url: https://raw.githubusercontent.com/api-evangelist/yugabytedb/refs/heads/main/crd/yugabytedb-pitr-config.yaml
- name: yugabytedb release
  url: https://raw.githubusercontent.com/api-evangelist/yugabytedb/refs/heads/main/crd/yugabytedb-release.yaml
- name: yugabytedb restore job
  url: https://raw.githubusercontent.com/api-evangelist/yugabytedb/refs/heads/main/crd/yugabytedb-restore-job.yaml
- name: yugabytedb storage config
  url: https://raw.githubusercontent.com/api-evangelist/yugabytedb/refs/heads/main/crd/yugabytedb-storage-config.yaml
- name: yugabytedb support bundle
  url: https://raw.githubusercontent.com/api-evangelist/yugabytedb/refs/heads/main/crd/yugabytedb-support-bundle.yaml
- name: yugabytedb ybcertificate
  url: https://raw.githubusercontent.com/api-evangelist/yugabytedb/refs/heads/main/crd/yugabytedb-ybcertificate.yaml
- name: yugabytedb ybplatform
  url: https://raw.githubusercontent.com/api-evangelist/yugabytedb/refs/heads/main/crd/yugabytedb-ybplatform.yaml
- name: yugabytedb ybprovider
  url: https://raw.githubusercontent.com/api-evangelist/yugabytedb/refs/heads/main/crd/yugabytedb-ybprovider.yaml
- name: yugabytedb ybuniverse
  url: https://raw.githubusercontent.com/api-evangelist/yugabytedb/refs/heads/main/crd/yugabytedb-ybuniverse.yaml
created: '2026-05-03'
description: YugabyteDB is a distributed PostgreSQL-compatible SQL database for cloud-native and mission-critical applications. It is delivered as open-source YugabyteDB Core, the fully managed YugabyteDB Aeon DBaaS, and the self-managed YugabyteDB Anywhere control plane, with REST APIs for programmatic management of accounts, projects, clusters, universes, backups, restores, read replicas, allow lists, and maintenance windows.
features:
- description: Wire-compatible YSQL API supporting PostgreSQL drivers, ORMs, stored procedures, triggers, and extensions.
  name: PostgreSQL Compatibility
- description: ACID transactions, automatic sharding, and horizontal scaling across nodes, zones, and regions.
  name: Distributed SQL
- description: Geo-distributed clusters with synchronous and asynchronous replication for disaster recovery and data residency.
  name: Multi-Region Deployments
- description: Fully managed YugabyteDB Aeon clusters across AWS, Azure, and Google Cloud regions.
  name: Cloud Database as a Service
- description: YugabyteDB Anywhere for deploying and operating universes on customer infrastructure and Kubernetes.
  name: Self-Managed Control Plane
- description: On-demand and scheduled backups, point-in-time recovery, and cross-region restore.
  name: Backups and Restores
- description: Asynchronous read replicas for low-latency reads in additional regions.
  name: Read Replicas
- description: Vector search capabilities for retrieval-augmented generation (RAG) and GenAI workloads.
  name: Vector Indexing
- description: Cassandra-compatible API for wide-column workloads alongside the PostgreSQL-compatible YSQL API.
  name: YCQL API
- description: Built-in connection pooling and load balancing for distributed workloads.
  name: Connection Management
finops:
- name: Yugabytedb Finops
  service_category: API
  slug: yugabytedb-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/yugabytedb.png
integrations:
- description: Helm charts and a Kubernetes Operator for deploying YugabyteDB on Kubernetes clusters.
  name: Kubernetes
- description: Terraform Provider for YugabyteDB Anywhere for infrastructure-as-code management of universes.
  name: Terraform
- description: Open-source migration tool for moving schema and data from PostgreSQL, Oracle, and MySQL to YugabyteDB.
  name: YugabyteDB Voyager
- description: Native deployment targets for YugabyteDB Aeon and Anywhere across major public clouds.
  name: AWS, Azure, and Google Cloud
- description: Compatibility with standard PostgreSQL drivers, ORMs, and tooling via the YSQL API.
  name: PostgreSQL Drivers and ORMs
- description: Bearer-token authenticated REST APIs for both Aeon and Anywhere control planes.
  name: REST API
json_schemas:
- name: YugabyteDB Cluster
  property_count: 14
  slug: yugabytedb-cluster
jsonld:
- class_count: 0
  name: Yugabytedb Context
  property_count: 15
  slug: yugabytedb-context
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
modified: '2026-05-19'
name: YugabyteDB
nav: Providers
network: true
overview: 'YugabyteDB publishes 73 APIs on the [APIs.io](https://apis.io/) network, including Access Keys API, Accounts API, Alerts API, and 70 more. Tagged areas include Cloud Database, Database, Database-as-a-Service, Distributed SQL, and PostgreSQL.


  The YugabyteDB catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  YugabyteDB''s developer surface includes authentication, documentation, API reference, getting-started guide, developer console, signup flow, pricing, and 82 more developer resources.'
plans:
- name: Yugabytedb Plans Pricing
  plan_count: 3
  slug: yugabytedb-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 5
  name: Yugabytedb Rate Limits
  slug: yugabytedb-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: YugabyteDB API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: yugabytedb-jsonschema-spectral-rules
- effective_rule_count: 114
  extends:
  - spectral:oas
  name: YugabyteDB API Rules
  rule_count: 73
  severity_counts:
    error: 17
    hint: 0
    info: 21
    warn: 35
  slug: yugabytedb-spectral-rules
score:
  band: developing
  composite: 51.0
  delta: 0.0
  facets:
    access_clarity: 65.8
    commercial_clarity: 65.8
    contract_governance: 13.6
    contract_quality: 24.4
    developer_ergonomics: 83.3
    discoverability: 75.9
    governance: 13.6
    operational_transparency: 44.7
  previous_composite: 51.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 73
      marker_coverage: 100.0
      total: 73
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/yugabytedb/refs/heads/main/screenshots/yugabytedb-2026-06-20T201754.png
security:
- kind: authentication
  name: Yugabytedb Authentication
  slug: yugabytedb-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Yugabytedb Domain Security
  slug: yugabytedb-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Yugabytedb Trust Center
  slug: yugabytedb-trust-center
  summary_line: SOC 2, ISO 27001
skill_count: 5
skills:
- name: explain-plan-analyzer
  slug: explain-plan-analyzer
- name: operator
  slug: operator
- name: yba-api
  slug: yba-api
- name: ycql
  slug: ycql
- name: ysql
  slug: ysql
slug: yugabytedb
solutions:
- description: Open-source distributed SQL database available under the Apache 2.0 license.
  name: YugabyteDB Core
- description: Fully managed cloud database service operated by Yugabyte.
  name: YugabyteDB Aeon
- description: Self-managed control plane for operating YugabyteDB universes on customer infrastructure.
  name: YugabyteDB Anywhere
- description: Database migration service and tooling for moving to YugabyteDB.
  name: YugabyteDB Voyager
tags:
- Cloud Database
- Database
- Database-as-a-Service
- Distributed SQL
- PostgreSQL
use_cases:
- description: Replace legacy monolithic RDBMS systems with a horizontally scalable, PostgreSQL-compatible alternative.
  name: Database Modernization
- description: Power Kubernetes-deployed and microservices applications with a resilient distributed SQL backend.
  name: Cloud-Native Applications
- description: Operate global SaaS platforms with low-latency reads and disaster-recovery-ready writes.
  name: Multi-Region SaaS
- description: Run mission-critical transaction systems requiring strong consistency and high availability.
  name: Financial Services
- description: Handle high-throughput product catalogs, inventory, and orders across regions.
  name: Retail and eCommerce
- description: Support subscriber, billing, and session data at carrier scale.
  name: Telecommunications
- description: Store embeddings and metadata for retrieval-augmented generation pipelines.
  name: GenAI and RAG
- description: Provide a durable distributed SQL store for edge and streaming application data.
  name: Edge and Streaming
website: https://www.yugabyte.com/
---
