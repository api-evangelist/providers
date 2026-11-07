---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: true
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 31.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 300
  human_in_the_loop: 14
  name: Yugabyte Agentic Access
  operation_count: 522
  slug: yugabyte-agentic-access
  summary_line: 522 operations · 300 acting · 14 human-in-the-loop
api_count: 73
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
  description: The Access Keys API from Yugabyte — 3 operation(s) for access keys.
  name: Yugabyte Access Keys API
  slug: yugabyte-access-keys-api
- baseURL: https://cloud.yugabyte.com/api/public/v1
  baseurl_source: declared
  description: Retrieve account-level information for the authenticated user, including account ID and metadata used to scope all other API requests.
  name: Yugabyte Accounts API
  slug: yugabyte-accounts-api
- baseURL: https://cloud.yugabyte.com/api/public/v1
  baseurl_source: declared
  description: The Alerts API from Yugabyte — 24 operation(s) for alerts.
  name: Yugabyte Alerts API
  slug: yugabyte-alerts-api
- baseURL: https://cloud.yugabyte.com/api/public/v1
  baseurl_source: declared
  description: Manage IP allow lists that control which client IP addresses or CIDR ranges are permitted to connect to a cluster.
  name: Yugabyte Allow Lists API
  slug: yugabyte-allow-lists-api
- baseURL: https://cloud.yugabyte.com/api/public/v1
  baseurl_source: declared
  description: The Asynchronous Replication API from Yugabyte — 6 operation(s) for asynchronous replication.
  name: Yugabyte Asynchronous Replication API
  slug: yugabyte-asynchronous-replication-api
- baseURL: https://cloud.yugabyte.com/api/public/v1
  baseurl_source: declared
  description: The Audit API from Yugabyte — 3 operation(s) for audit.
  name: Yugabyte Audit API
  slug: yugabyte-audit-api
- baseURL: https://cloud.yugabyte.com/api/public/v1
  baseurl_source: declared
  description: Authentication operations on YBA
  name: Yugabyte Authentication API
  slug: yugabyte-authentication-api
- baseURL: https://cloud.yugabyte.com/api/public/v1
  baseurl_source: declared
  description: The Availability Zones API from Yugabyte — 4 operation(s) for availability zones.
  name: Yugabyte Availability Zones API
  slug: yugabyte-availability-zones-api
- baseURL: https://cloud.yugabyte.com/api/public/v1
  baseurl_source: declared
  description: Operations related to universe backup and restore
  name: Yugabyte Backup And Restore API
  slug: yugabyte-backup-and-restore-api
- baseURL: https://cloud.yugabyte.com/api/public/v1
  baseurl_source: declared
  description: The Backups API from Yugabyte — 23 operation(s) for backups.
  name: Yugabyte Backups API
  slug: yugabyte-backups-api
- baseURL: https://cloud.yugabyte.com/api/public/v1
  baseurl_source: declared
  description: The Certificate Info API from Yugabyte — 7 operation(s) for certificate info.
  name: Yugabyte Certificate Info API
  slug: yugabyte-certificate-info-api
- baseURL: https://cloud.yugabyte.com/api/public/v1
  baseurl_source: declared
  description: The Cloud Providers API from Yugabyte — 8 operation(s) for cloud providers.
  name: Yugabyte Cloud Providers API
  slug: yugabyte-cloud-providers-api
- baseURL: https://cloud.yugabyte.com/api/public/v1
  baseurl_source: declared
  description: Create, list, retrieve, update, pause, resume, and delete YugabyteDB clusters within an account and project. Supports both single-region and multi-region cluster configurations.
  name: Yugabyte Clusters API
  slug: yugabyte-clusters-api
- baseURL: https://cloud.yugabyte.com/api/public/v1
  baseurl_source: declared
  description: CRUD operations for Continuous YBA Backups
  name: Yugabyte Continuous Backup API
  slug: yugabyte-continuous-backup-api
- baseURL: https://cloud.yugabyte.com/api/public/v1
  baseurl_source: declared
  description: The Custom CA Certificates API from Yugabyte — 4 operation(s) for custom ca certificates.
  name: Yugabyte Custom CA Certificates API
  slug: yugabyte-custom-ca-certificates-api
- baseURL: https://cloud.yugabyte.com/api/public/v1
  baseurl_source: declared
  description: The Customer Configuration API from Yugabyte — 7 operation(s) for customer configuration.
  name: Yugabyte Customer Configuration API
  slug: yugabyte-customer-configuration-api
- baseURL: https://cloud.yugabyte.com/api/public/v1
  baseurl_source: declared
  description: The Customer Management API from Yugabyte — 4 operation(s) for customer management.
  name: Yugabyte Customer Management API
  slug: yugabyte-customer-management-api
- baseURL: https://cloud.yugabyte.com/api/public/v1
  baseurl_source: declared
  description: The Customer Tasks API from Yugabyte — 8 operation(s) for customer tasks.
  name: Yugabyte Customer Tasks API
  slug: yugabyte-customer-tasks-api
- baseURL: https://cloud.yugabyte.com/api/public/v1
  baseurl_source: declared
  description: The Disaster Recovery API from Yugabyte — 15 operation(s) for disaster recovery.
  name: Yugabyte Disaster Recovery API
  slug: yugabyte-disaster-recovery-api
- baseURL: https://cloud.yugabyte.com/api/public/v1
  baseurl_source: declared
  description: The Encryption at rest API from Yugabyte — 7 operation(s) for encryption at rest.
  name: Yugabyte Encryption at rest API
  slug: yugabyte-encryption-at-rest-api
- baseURL: https://cloud.yugabyte.com/api/public/v1
  baseurl_source: declared
  description: The Extract metadata from remote tarball API from Yugabyte — 2 operation(s) for extract metadata from remote tarball.
  name: Yugabyte Extract metadata from remote tarball API
  slug: yugabyte-extract-metadata-from-remote-tarball-api
- baseURL: https://cloud.yugabyte.com/api/public/v1
  baseurl_source: declared
  description: The GFlags Validation APIs API from Yugabyte — 3 operation(s) for gflags validation apis.
  name: Yugabyte GFlags Validation APIs API
  slug: yugabyte-gflags-validation-apis-api
- baseURL: https://cloud.yugabyte.com/api/public/v1
  baseurl_source: declared
  description: The Grafana Dashboard API from Yugabyte — 1 operation(s) for grafana dashboard.
  name: Yugabyte Grafana Dashboard API
  slug: yugabyte-grafana-dashboard-api
- baseURL: https://cloud.yugabyte.com/api/public/v1
  baseurl_source: declared
  description: The HA API from Yugabyte — 3 operation(s) for ha.
  name: Yugabyte HA API
  slug: yugabyte-ha-api
- baseURL: https://cloud.yugabyte.com/api/public/v1
  baseurl_source: declared
  description: The Instance Types API from Yugabyte — 5 operation(s) for instance types.
  name: Yugabyte Instance Types API
  slug: yugabyte-instance-types-api
- baseURL: https://cloud.yugabyte.com/api/public/v1
  baseurl_source: declared
  description: The Internal HA API from Yugabyte — 5 operation(s) for internal ha.
  name: Yugabyte Internal HA API
  slug: yugabyte-internal-ha-api
- baseURL: https://cloud.yugabyte.com/api/public/v1
  baseurl_source: declared
  description: Isolated backup/restore of YBA to local filesystem
  name: Yugabyte Isolated Backup API
  slug: yugabyte-isolated-backup-api
- baseURL: https://cloud.yugabyte.com/api/public/v1
  baseurl_source: declared
  description: Job Scheduler
  name: Yugabyte Job Scheduler API
  slug: yugabyte-job-scheduler-api
- baseURL: https://cloud.yugabyte.com/api/public/v1
  baseurl_source: declared
  description: The KubernetesOverridesController API from Yugabyte — 1 operation(s) for kubernetesoverridescontroller.
  name: Yugabyte Kubernetes Overrides Controller API
  slug: yugabyte-kubernetesoverridescontroller-api
- baseURL: https://cloud.yugabyte.com/api/public/v1
  baseurl_source: declared
  description: The LDAP Role management API from Yugabyte — 1 operation(s) for ldap role management.
  name: Yugabyte LDAP Role management API
  slug: yugabyte-ldap-role-management-api
- baseURL: https://cloud.yugabyte.com/api/public/v1
  baseurl_source: declared
  description: The LDAPOIDC Role management API from Yugabyte — 3 operation(s) for ldapoidc role management.
  name: Yugabyte LDAPOIDC Role management API
  slug: yugabyte-ldapoidc-role-management-api
- baseURL: https://cloud.yugabyte.com/api/public/v1
  baseurl_source: declared
  description: The License Management API from Yugabyte — 2 operation(s) for license management.
  name: Yugabyte License Management API
  slug: yugabyte-license-management-api
- baseURL: https://cloud.yugabyte.com/api/public/v1
  baseurl_source: declared
  description: The LoggingConfig API from Yugabyte — 2 operation(s) for loggingconfig.
  name: Yugabyte Logging Config API
  slug: yugabyte-loggingconfig-api
- baseURL: https://cloud.yugabyte.com/api/public/v1
  baseurl_source: declared
  description: The Maintenance Windows API from Yugabyte — 5 operation(s) for maintenance windows.
  name: Yugabyte Maintenance Windows API
  slug: yugabyte-maintenance-windows-api
- baseURL: https://cloud.yugabyte.com/api/public/v1
  baseurl_source: declared
  description: CRUD operations for YBA metrics
  name: Yugabyte Metrics API
  slug: yugabyte-metrics-api
- baseURL: https://cloud.yugabyte.com/api/public/v1
  baseurl_source: declared
  description: The New Release management API from Yugabyte — 2 operation(s) for new release management.
  name: Yugabyte New Release management API
  slug: yugabyte-new-release-management-api
- baseURL: https://cloud.yugabyte.com/api/public/v1
  baseurl_source: declared
  description: The Node Agents API from Yugabyte — 5 operation(s) for node agents.
  name: Yugabyte Node Agents API
  slug: yugabyte-node-agents-api
- baseURL: https://cloud.yugabyte.com/api/public/v1
  baseurl_source: declared
  description: The Node instances API from Yugabyte — 10 operation(s) for node instances.
  name: Yugabyte Node instances API
  slug: yugabyte-node-instances-api
- baseURL: https://cloud.yugabyte.com/api/public/v1
  baseurl_source: declared
  description: The PA Collector API from Yugabyte — 4 operation(s) for pa collector.
  name: Yugabyte PA Collector API
  slug: yugabyte-pa-collector-api
- baseURL: https://cloud.yugabyte.com/api/public/v1
  baseurl_source: declared
  description: The PackagesController API from Yugabyte — 1 operation(s) for packagescontroller.
  name: Yugabyte Packages Controller API
  slug: yugabyte-packagescontroller-api
- baseURL: https://cloud.yugabyte.com/api/public/v1
  baseurl_source: declared
  description: The Performance Advisor API from Yugabyte — 9 operation(s) for performance advisor.
  name: Yugabyte Performance Advisor API
  slug: yugabyte-performance-advisor-api
- baseURL: https://cloud.yugabyte.com/api/public/v1
  baseurl_source: declared
  description: The PITR management API from Yugabyte — 5 operation(s) for pitr management.
  name: Yugabyte PITR management API
  slug: yugabyte-pitr-management-api
- baseURL: https://cloud.yugabyte.com/api/public/v1
  baseurl_source: declared
  description: The Platform Instance API from Yugabyte — 4 operation(s) for platform instance.
  name: Yugabyte Platform Instance API
  slug: yugabyte-platform-instance-api
- baseURL: https://cloud.yugabyte.com/api/public/v1
  baseurl_source: declared
  description: The Platform Replication API from Yugabyte — 4 operation(s) for platform replication.
  name: Yugabyte Platform Replication API
  slug: yugabyte-platform-replication-api
- baseURL: https://cloud.yugabyte.com/api/public/v1
  baseurl_source: declared
  description: The Preview API from Yugabyte — 2 operation(s) for preview.
  name: Yugabyte Preview API
  slug: yugabyte-preview-api
- baseURL: https://cloud.yugabyte.com/api/public/v1
  baseurl_source: declared
  description: Manage projects within a YugabyteDB Aeon account. Projects provide organizational grouping for clusters, allow lists, and billing.
  name: Yugabyte Projects API
  slug: yugabyte-projects-api
- baseURL: https://cloud.yugabyte.com/api/public/v1
  baseurl_source: declared
  description: The RBAC management API from Yugabyte — 5 operation(s) for rbac management.
  name: Yugabyte RBAC management API
  slug: yugabyte-rbac-management-api
- baseURL: https://cloud.yugabyte.com/api/public/v1
  baseurl_source: declared
  description: Manage read replicas for a cluster to serve low-latency read requests from remote regions without affecting the primary cluster workload.
  name: Yugabyte Read Replicas API
  slug: yugabyte-read-replicas-api
- baseURL: https://cloud.yugabyte.com/api/public/v1
  baseurl_source: declared
  description: The Region management API from Yugabyte — 5 operation(s) for region management.
  name: Yugabyte Region management API
  slug: yugabyte-region-management-api
- baseURL: https://cloud.yugabyte.com/api/public/v1
  baseurl_source: declared
  description: The Release management API from Yugabyte — 3 operation(s) for release management.
  name: Yugabyte Release management API
  slug: yugabyte-release-management-api
- baseURL: https://cloud.yugabyte.com/api/public/v1
  baseurl_source: declared
  description: Restore a cluster from a previously created backup snapshot, enabling point-in-time recovery of database state.
  name: Yugabyte Restores API
  slug: yugabyte-restores-api
- baseURL: https://cloud.yugabyte.com/api/public/v1
  baseurl_source: declared
  description: The Runtime configuration API from Yugabyte — 6 operation(s) for runtime configuration.
  name: Yugabyte Runtime configuration API
  slug: yugabyte-runtime-configuration-api
- baseURL: https://cloud.yugabyte.com/api/public/v1
  baseurl_source: declared
  description: The Schedule management API from Yugabyte — 7 operation(s) for schedule management.
  name: Yugabyte Schedule management API
  slug: yugabyte-schedule-management-api
- baseURL: https://cloud.yugabyte.com/api/public/v1
  baseurl_source: declared
  description: The Session Management API from Yugabyte — 9 operation(s) for session management.
  name: Yugabyte Session Management API
  slug: yugabyte-session-management-api
- baseURL: https://cloud.yugabyte.com/api/public/v1
  baseurl_source: declared
  description: The Support Bundle management API from Yugabyte — 5 operation(s) for support bundle management.
  name: Yugabyte Support Bundle management API
  slug: yugabyte-support-bundle-management-api
- baseURL: https://cloud.yugabyte.com/api/public/v1
  baseurl_source: declared
  description: The Table Management API from Yugabyte — 8 operation(s) for table management.
  name: Yugabyte Table Management API
  slug: yugabyte-table-management-api
- baseURL: https://cloud.yugabyte.com/api/public/v1
  baseurl_source: declared
  description: The Tablet server management API from Yugabyte — 1 operation(s) for tablet server management.
  name: Yugabyte Tablet server management API
  slug: yugabyte-tablet-server-management-api
- baseURL: https://cloud.yugabyte.com/api/public/v1
  baseurl_source: declared
  description: Operations for Telemetry Providers
  name: Yugabyte Telemetry Provider API
  slug: yugabyte-telemetry-provider-api
- baseURL: https://cloud.yugabyte.com/api/public/v1
  baseurl_source: declared
  description: The Universe actions API from Yugabyte — 1 operation(s) for universe actions.
  name: Yugabyte Universe actions API
  slug: yugabyte-universe-actions-api
- baseURL: https://cloud.yugabyte.com/api/public/v1
  baseurl_source: declared
  description: CRUD operations for a Universe
  name: Yugabyte Universe API
  slug: yugabyte-universe-api
- baseURL: https://cloud.yugabyte.com/api/public/v1
  baseurl_source: declared
  description: The Universe CDC Management API from Yugabyte — 3 operation(s) for universe cdc management.
  name: Yugabyte Universe CDC Management API
  slug: yugabyte-universe-cdc-management-api
- baseURL: https://cloud.yugabyte.com/api/public/v1
  baseurl_source: declared
  description: The Universe database management API from Yugabyte — 6 operation(s) for universe database management.
  name: Yugabyte Universe database management API
  slug: yugabyte-universe-database-management-api
- baseURL: https://cloud.yugabyte.com/api/public/v1
  baseurl_source: declared
  description: The Universe information API from Yugabyte — 11 operation(s) for universe information.
  name: Yugabyte Universe information API
  slug: yugabyte-universe-information-api
- baseURL: https://cloud.yugabyte.com/api/public/v1
  baseurl_source: declared
  description: The Universe management API from Yugabyte — 11 operation(s) for universe management.
  name: Yugabyte Universe management API
  slug: yugabyte-universe-management-api
- baseURL: https://cloud.yugabyte.com/api/public/v1
  baseurl_source: declared
  description: The Universe node metadata (metamaster) API from Yugabyte — 6 operation(s) for universe node metadata (metamaster).
  name: Yugabyte Universe node metadata (metamaster) API
  slug: yugabyte-universe-node-metadata-metamaster-api
- baseURL: https://cloud.yugabyte.com/api/public/v1
  baseurl_source: declared
  description: The Universe performance suggestions API from Yugabyte — 3 operation(s) for universe performance suggestions.
  name: Yugabyte Universe performance suggestions API
  slug: yugabyte-universe-performance-suggestions-api
- baseURL: https://cloud.yugabyte.com/api/public/v1
  baseurl_source: declared
  description: The Universe Upgrades Management API from Yugabyte — 20 operation(s) for universe upgrades management.
  name: Yugabyte Universe Upgrades Management API
  slug: yugabyte-universe-upgrades-management-api
- baseURL: https://cloud.yugabyte.com/api/public/v1
  baseurl_source: declared
  description: The UniverseClusterMutations API from Yugabyte — 4 operation(s) for universeclustermutations.
  name: Yugabyte Universe Cluster Mutations API
  slug: yugabyte-universeclustermutations-api
- baseURL: https://cloud.yugabyte.com/api/public/v1
  baseurl_source: declared
  description: The Upload Release packages API from Yugabyte — 2 operation(s) for upload release packages.
  name: Yugabyte Upload Release packages API
  slug: yugabyte-upload-release-packages-api
- baseURL: https://cloud.yugabyte.com/api/public/v1
  baseurl_source: declared
  description: The User Management API from Yugabyte — 6 operation(s) for user management.
  name: Yugabyte User Management API
  slug: yugabyte-user-management-api
- baseURL: https://cloud.yugabyte.com/api/public/v1
  baseurl_source: declared
  description: YBA Instance operations
  name: Yugabyte YBA Instance API
  slug: yugabyte-yba-instance-api
- baseURL: https://cloud.yugabyte.com/api/public/v1
  baseurl_source: declared
  description: The Ybc Management API from Yugabyte — 5 operation(s) for ybc management.
  name: Yugabyte Ybc Management API
  slug: yugabyte-ybc-management-api
artifact_total: 100
collections:
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
- group: commercial
  href: https://artifacts.apis.io/yugabyte/plans/yugabyte-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/yugabyte-plans-pricing.yml
- group: company
  title: ''
  type: Website
  url: https://www.yugabyte.com/
- group: other
  href: https://artifacts.apis.io/yugabyte/overlays/yugabyte-yugabyted-overlay.yaml
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
  href: https://artifacts.apis.io/yugabyte/packages/yugabyte-packages.yml
  title: ''
  type: Packages
  url: packages/yugabyte-packages.yml
- group: build
  href: https://artifacts.apis.io/yugabyte/packages/yugabyte-packages.yml
  title: ''
  type: SDKs
  url: packages/yugabyte-packages.yml
- group: build
  href: https://artifacts.apis.io/yugabyte/cli/yugabyte-cli.yml
  title: ''
  type: CLI
  url: cli/yugabyte-cli.yml
- group: auth
  href: https://artifacts.apis.io/yugabyte/authentication/yugabyte-authentication.yml
  title: ''
  type: Authentication
  url: authentication/yugabyte-authentication.yml
- group: agent
  href: https://artifacts.apis.io/yugabyte/mcp/yugabyte-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/yugabyte-mcp.yml
- group: agent
  href: https://artifacts.apis.io/yugabyte/llms/yugabyte-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/yugabyte-llms.txt
- group: agent
  href: https://artifacts.apis.io/yugabyte/well-known/yugabyte-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/yugabyte-well-known.yml
- group: design
  href: https://artifacts.apis.io/yugabyte/errors/yugabyte-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/yugabyte-problem-types.yml
- group: design
  href: https://artifacts.apis.io/yugabyte/conventions/yugabyte-conventions.yml
  title: ''
  type: Conventions
  url: conventions/yugabyte-conventions.yml
- group: design
  href: https://artifacts.apis.io/yugabyte/lifecycle/yugabyte-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/yugabyte-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/yugabyte/lifecycle/yugabyte-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/yugabyte-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/yugabyte/conformance/yugabyte-conformance.yml
  title: ''
  type: Conformance
  url: conformance/yugabyte-conformance.yml
- group: design
  href: https://artifacts.apis.io/yugabyte/data-model/yugabyte-data-model.yml
  title: ''
  type: DataModel
  url: data-model/yugabyte-data-model.yml
- group: operate
  href: https://artifacts.apis.io/yugabyte/changelog/yugabyte-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/yugabyte-changelog.yml
- group: auth
  href: https://artifacts.apis.io/yugabyte/security/yugabyte-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/yugabyte-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/yugabyte/agentic-access/yugabyte-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/yugabyte-agentic-access.yml
- group: agent
  href: https://artifacts.apis.io/yugabyte/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
crds:
- name: yugabytedb backup schedule
  url: https://artifacts.apis.io/yugabyte/crd/yugabytedb-backup-schedule.yaml
- name: yugabytedb backup
  url: https://artifacts.apis.io/yugabyte/crd/yugabytedb-backup.yaml
- name: yugabytedb dr config
  url: https://artifacts.apis.io/yugabyte/crd/yugabytedb-dr-config.yaml
- name: yugabytedb pitr config
  url: https://artifacts.apis.io/yugabyte/crd/yugabytedb-pitr-config.yaml
- name: yugabytedb release
  url: https://artifacts.apis.io/yugabyte/crd/yugabytedb-release.yaml
- name: yugabytedb restore job
  url: https://artifacts.apis.io/yugabyte/crd/yugabytedb-restore-job.yaml
- name: yugabytedb storage config
  url: https://artifacts.apis.io/yugabyte/crd/yugabytedb-storage-config.yaml
- name: yugabytedb support bundle
  url: https://artifacts.apis.io/yugabyte/crd/yugabytedb-support-bundle.yaml
- name: yugabytedb ybcertificate
  url: https://artifacts.apis.io/yugabyte/crd/yugabytedb-ybcertificate.yaml
- name: yugabytedb ybplatform
  url: https://artifacts.apis.io/yugabyte/crd/yugabytedb-ybplatform.yaml
- name: yugabytedb ybprovider
  url: https://artifacts.apis.io/yugabyte/crd/yugabytedb-ybprovider.yaml
- name: yugabytedb ybuniverse
  url: https://artifacts.apis.io/yugabyte/crd/yugabytedb-ybuniverse.yaml
created: '2026-07-17'
description: 'Yugabyte is the company behind YugabyteDB, an open source (Apache 2.0), PostgreSQL-compatible distributed SQL database built for cloud-native and mission-critical applications. It pairs PostgreSQL wire-compatibility (the YSQL API) and a Cassandra-inspired API (YCQL) with horizontal scalability, built-in resilience, automatic sharding, and automatic failover across multi-region and multi-cloud deployments. Yugabyte ships the database in three form factors: self-managed YugabyteDB, YugabyteDB Anywhere for private and hybrid clouds, and YugabyteDB Aeon, a fully managed database-as-a-service. Developers integrate through PostgreSQL-compatible smart drivers, the YugabyteDB Aeon REST management API, the open source ybm CLI, a Terraform provider, and the yugabyted local admin API.'
finops:
- has_sources: true
  method: derived
  name: Yugabyte Finops
  primary_unit: gb
  service_category: ''
  slug: yugabyte-finops
  template: false
image: https://github.com/yugabyte.png
layout: provider
modified: '2026-07-21'
name: Yugabyte
nav: Providers
network: true
overview: 'Yugabyte publishes 82 API contracts indexed on the [APIs.io](https://apis.io/) network, including Backup Info API, Cluster API, Cluster Info API, and 79 more. Tagged areas include Company, Database, Distributed SQL, PostgreSQL, and Cloud.


  The Yugabyte catalog on APIs.io includes 1 Spectral governance ruleset.


  Yugabyte''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 29 more developer resources.'
plans:
- name: Yugabyte Plans Pricing
  plan_count: 12
  slug: yugabyte-plans-pricing
random_paper: 10
rules:
- authorship: generated
  effective_rule_count: 104
  extends:
  - spectral:oas
  name: Yugabyte API Rules
  rule_count: 63
  severity_counts:
    error: 36
    hint: 0
    info: 7
    warn: 20
  slug: yugabyte-rules
score:
  band: exemplar
  composite: 69.3
  coverage:
    artifact_dirs: 30
    catalog_earned: 59.5
    catalog_earned_first_party: 12.0
    catalog_gap: 55.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 100.0
    contract_governance: 18.2
    contract_quality: 46.2
    developer_ergonomics: 73.2
    discoverability: 78.6
    operational_transparency: 42.1
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 69.3
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
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 29.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 61.1
screenshot: https://apis.io/screenshots/yugabyte/yugabyte-2026-08-17T083024.png
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
skill_count: 2
skills:
- name: Diagnose YugabyteDB query performance
  slug: yugabyte-diagnose-query-performance
- name: Inspect YugabyteDB cluster health
  slug: yugabyte-inspect-cluster-health
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
