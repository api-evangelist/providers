---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - authentication
  - scopes
  - rate-limits
  - security
  trial: false
  try_now: false
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
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: mostly
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 56.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 172
  human_in_the_loop: 6
  name: Druva Agentic Access
  operation_count: 581
  slug: druva-agentic-access
  summary_line: 581 operations · 172 acting · 6 human-in-the-loop
api_count: 19
apis:
- description: Druva's first-party hosted Model Context Protocol server. MCP-compatible AI clients connect to a single global endpoint over streamable HTTP, authenticate with 3-legged OAuth 2.1 and PKCE, and reach t
  name: Druva MCP Server
  slug: mcp
- baseURL: https://apis.druva.com
  baseurl_source: declared
  description: Accounts in your CloudRanger Organization
  name: Druva Accounts API
  slug: druva-accounts-api
- baseURL: https://apis.druva.com
  baseurl_source: declared
  description: Lists the APIs to get information about the AD/LDAP Connectors configured for Endpoints & SaaS Apps.
  name: Druva AD/LDAP Management API
  slug: druva-ad-ldap-management-api
- baseURL: https://apis.druva.com
  baseurl_source: declared
  description: The Admin Roles API from Druva — 1 operation(s) for admin roles.
  name: Druva Admin Roles API
  slug: druva-admin-roles-api
- baseURL: https://apis.druva.com
  baseurl_source: declared
  description: The Administration API from Druva — 1 operation(s) for administration.
  name: Druva Administration API
  slug: druva-administration-api
- baseURL: https://apis.druva.com
  baseurl_source: declared
  description: The Administrators API from Druva — 4 operation(s) for administrators.
  name: Druva Administrators API
  slug: druva-administrators-api
- baseURL: https://apis.druva.com
  baseurl_source: declared
  description: Lists the APIs to get information about admins managed.
  name: Druva Admins API
  slug: druva-admins-api
- baseURL: https://apis.druva.com
  baseurl_source: declared
  description: The AHV API from Druva — 7 operation(s) for ahv.
  name: Druva AHV API
  slug: druva-ahv-api
- baseURL: https://apis.druva.com
  baseurl_source: declared
  description: The Alerts API from Druva — 3 operation(s) for alerts.
  name: Druva Alerts API
  slug: druva-alerts-api
- baseURL: https://apis.druva.com
  baseurl_source: declared
  description: Lists the APIs to get information and perform operations on M365 Apps managed in Druva SaaS Apps.
  name: Druva App Management API
  slug: druva-app-management-api
- baseURL: https://apis.druva.com
  baseurl_source: declared
  description: Audit specific API functions
  name: Druva Audit API
  slug: druva-audit-api
- baseURL: https://apis.druva.com
  baseurl_source: declared
  description: The Audit Trail API from Druva — 1 operation(s) for audit trail.
  name: Druva Audit Trail API
  slug: druva-audit-trail-api
- baseURL: https://apis.druva.com
  baseurl_source: declared
  description: Lists the APIs to get information about the Audit Trails generated in the Druva Console.
  name: Druva Audit Trail Management API
  slug: druva-audit-trail-management-api
- baseURL: https://apis.druva.com
  baseurl_source: declared
  description: The Auth API from Druva — 1 operation(s) for auth.
  name: Druva Auth API
  slug: druva-auth-api
- baseURL: https://apis.druva.com
  baseurl_source: declared
  description: AutoScalingGroups specific API functions
  name: Druva Auto Scaling Groups API
  slug: druva-autoscalinggroups-api
- baseURL: https://apis.druva.com
  baseurl_source: declared
  description: AWS Account specific functions
  name: Druva Aws API
  slug: druva-aws-api
- baseURL: https://apis.druva.com
  baseurl_source: declared
  description: The Azure API from Druva — 3 operation(s) for azure.
  name: Druva Azure API
  slug: druva-azure-api
- baseURL: https://apis.druva.com
  baseurl_source: declared
  description: The Azure SQL API from Druva — 4 operation(s) for azure sql.
  name: Druva Azure SQL API
  slug: druva-azure-sql-api
- baseURL: https://apis.druva.com
  baseurl_source: declared
  description: Backups in your CloudRanger Account
  name: Druva Backups API
  slug: druva-backups-api
- baseURL: https://apis.druva.com
  baseurl_source: declared
  description: The Buckets API from Druva — 1 operation(s) for buckets.
  name: Druva Buckets API
  slug: druva-buckets-api
- baseURL: https://apis.druva.com
  baseurl_source: declared
  description: Lists the APIs to get reports for Chargeback and Telemetry.
  name: Druva Chargeback and Telemetry Reports API
  slug: druva-chargeback-and-telemetry-reports-api
- baseURL: https://apis.druva.com
  baseurl_source: declared
  description: The CloudCache API from Druva — 1 operation(s) for cloudcache.
  name: Druva Cloud Cache API
  slug: druva-cloudcache-api
- baseURL: https://apis.druva.com
  baseurl_source: declared
  description: The Credential API from Druva — 1 operation(s) for credential.
  name: Druva Credential API
  slug: druva-credential-api
- baseURL: https://apis.druva.com
  baseurl_source: declared
  description: List of APIs to get information of and manage the Curated Snapshots for the resources managed in Druva Cloud.
  name: Druva Curated Snapshots API
  slug: druva-curated-snapshots-api
- baseURL: https://apis.druva.com
  baseurl_source: declared
  description: Lists the APIs to get information and perform operations on customers managed.
  name: Druva Customers API
  slug: druva-customers-api
- baseURL: https://apis.druva.com
  baseurl_source: declared
  description: Lists the APIs to get MSP Cyber Resilience reports data.
  name: Druva Cyber Resilience Reports API
  slug: druva-cyber-resilience-reports-api
- baseURL: https://apis.druva.com
  baseurl_source: declared
  description: View a list of the resources managed in Druva Cloud detected with Data Anomalies.
  name: Druva Data Anomalies API
  slug: druva-data-anomalies-api
- baseURL: https://apis.druva.com
  baseurl_source: declared
  description: The Data Protection API from Druva — 8 operation(s) for data protection.
  name: Druva Data Protection API
  slug: druva-data-protection-api
- baseURL: https://apis.druva.com
  baseurl_source: declared
  description: Disaster Recovery Plan specific API functions
  name: Druva Disaster Recovery Plans API
  slug: druva-disasterrecoveryplans-api
- baseURL: https://apis.druva.com
  baseurl_source: declared
  description: The DRaaS API from Druva — 2 operation(s) for draas.
  name: Druva D Raa S API
  slug: druva-draas-api
- baseURL: https://apis.druva.com
  baseurl_source: declared
  description: Lists the APIs to get information about devices managed in Druva inSync.
  name: Druva Endpoints API
  slug: druva-endpoints-api
- baseURL: https://apis.druva.com
  baseurl_source: declared
  description: Lists the APIs to get MSP Endpoints reports data.
  name: Druva Endpoints Reports API
  slug: druva-endpoints-reports-api
- baseURL: https://apis.druva.com
  baseurl_source: declared
  description: Lists the APIs to get MSP Enterprise Workload reports data.
  name: Druva Enterprise Workloads Reports API
  slug: druva-enterprise-workloads-reports-api
- baseURL: https://apis.druva.com
  baseurl_source: declared
  description: Environments specific API functions
  name: Druva Environments API
  slug: druva-environments-api
- baseURL: https://apis.druva.com
  baseurl_source: declared
  description: Lists the APIs to get information about the events generated in Druva inSync.
  name: Druva Event Management API
  slug: druva-event-management-api
- baseURL: https://apis.druva.com
  baseurl_source: declared
  description: Lists the APIs to get events for MSP and Customer.
  name: Druva Events API
  slug: druva-events-api
- baseURL: https://apis.druva.com
  baseurl_source: declared
  description: Quickly find backed-up files and emails of end-users using metadata attributes.
  name: Druva Federated Search API
  slug: druva-federated-search-api
- baseURL: https://apis.druva.com
  baseurl_source: declared
  description: The File Server API from Druva — 13 operation(s) for file server.
  name: Druva File Server API
  slug: druva-file-server-api
- baseURL: https://apis.druva.com
  baseurl_source: declared
  description: File Level Search specific API functions
  name: Druva File Level Search API
  slug: druva-filelevelsearch-api
- baseURL: https://apis.druva.com
  baseurl_source: declared
  description: Lists the APIs to get MSP Google Workspace reports data.
  name: Druva Google Workspace Reports API
  slug: druva-google-workspace-reports-api
- baseURL: https://apis.druva.com
  baseurl_source: declared
  description: The Hyper-V API from Druva — 8 operation(s) for hyper-v.
  name: Druva Hyper V API
  slug: druva-hyper-v-api
- baseURL: https://apis.druva.com
  baseurl_source: declared
  description: Jobs in your CloudRanger Account
  name: Druva Jobs API
  slug: druva-jobs-api
- baseURL: https://apis.druva.com
  baseurl_source: declared
  description: Lists the APIs to get information about the legal hold policies, manage users on legal hold and new APIs for eDiscovery Download Client.
  name: Druva Legal Hold API
  slug: druva-legal-hold-api
- baseURL: https://apis.druva.com
  baseurl_source: declared
  description: Lists the APIs to get MSP Microsoft 365 reports data.
  name: Druva Microsoft 365 Reports API
  slug: druva-microsoft-365-reports-api
- baseURL: https://apis.druva.com
  baseurl_source: declared
  description: The NAS API from Druva — 18 operation(s) for nas.
  name: Druva NAS API
  slug: druva-nas-api
- baseURL: https://apis.druva.com
  baseurl_source: declared
  description: The New Endpoint API from Druva — 1 operation(s) for new endpoint.
  name: Druva New Endpoint API
  slug: druva-new-endpoint-api
- baseURL: https://apis.druva.com
  baseurl_source: declared
  description: The Onboarding API from Druva — 2 operation(s) for onboarding.
  name: Druva Onboarding API
  slug: druva-onboarding-api
- baseURL: https://apis.druva.com
  baseurl_source: declared
  description: The OracleDTC API from Druva — 12 operation(s) for oracledtc.
  name: Druva Oracle DTC API
  slug: druva-oracledtc-api
- baseURL: https://apis.druva.com
  baseurl_source: declared
  description: Your CloudRanger Organization and how to authenticate API Calls
  name: Druva Organization API
  slug: druva-organization-api
- baseURL: https://apis.druva.com
  baseurl_source: declared
  description: The PBS API from Druva — 6 operation(s) for pbs.
  name: Druva PBS API
  slug: druva-pbs-api
- baseURL: https://apis.druva.com
  baseurl_source: declared
  description: Lists the APIs to get information about the profiles configured in Druva inSync.
  name: Druva Profile Management API
  slug: druva-profile-management-api
- baseURL: https://apis.druva.com
  baseurl_source: declared
  description: Lists the APIs to get and manage quota configurations and warning thresholds.
  name: Druva Quota API
  slug: druva-quota-api
- baseURL: https://apis.druva.com
  baseurl_source: declared
  description: List of APIs to get information and perform operations on ransomware affected resources managed in Druva Cloud.
  name: Druva Ransomware Recovery API
  slug: druva-ransomware-recovery-api
- baseURL: https://apis.druva.com
  baseurl_source: declared
  description: List of APIs to get information of Events of Realize product in Druva Cloud.
  name: Druva Realize Events API
  slug: druva-realize-events-api
- baseURL: https://apis.druva.com
  baseurl_source: declared
  description: The Reports API from Druva — 12 operation(s) for reports.
  name: Druva Reports API
  slug: druva-reports-api
- baseURL: https://apis.druva.com
  baseurl_source: declared
  description: Resource specific API functions
  name: Druva Resources API
  slug: druva-resources-api
- baseURL: https://apis.druva.com
  baseurl_source: declared
  description: The Restore OneDrive/Exchange Online data API from Druva — 4 operation(s) for restore onedrive/exchange online data.
  name: Druva Restore OneDrive/Exchange Online data API
  slug: druva-restore-onedrive-exchange-online-data-api
- baseURL: https://apis.druva.com
  baseurl_source: declared
  description: List of APIs to get information and perform operations of Restore scans on the resources managed in Druva Cloud.
  name: Druva Restore scans API
  slug: druva-restore-scans-api
- baseURL: https://apis.druva.com
  baseurl_source: declared
  description: The Restore SharePoint Online data API from Druva — 3 operation(s) for restore sharepoint online data.
  name: Druva Restore SharePoint Online data API
  slug: druva-restore-sharepoint-online-data-api
- baseURL: https://apis.druva.com
  baseurl_source: declared
  description: Restores in your CloudRanger Account
  name: Druva Restores API
  slug: druva-restores-api
- baseURL: https://apis.druva.com
  baseurl_source: declared
  description: Lists the APIs to get MSP Salesforce reports data.
  name: Druva Salesforce Reports API
  slug: druva-salesforce-reports-api
- baseURL: https://apis.druva.com
  baseurl_source: declared
  description: Schedules in your CloudRanger Account
  name: Druva Schedules API
  slug: druva-schedules-api
- baseURL: https://apis.druva.com
  baseurl_source: declared
  description: The Scripts API from Druva — 7 operation(s) for scripts.
  name: Druva Scripts API
  slug: druva-scripts-api
- baseURL: https://apis.druva.com
  baseurl_source: declared
  description: Lists of APIs to get information and perform operations on Sensitive Data Governance.
  name: Druva Sensitive Data Governance API
  slug: druva-sensitive-data-governance-api
- baseURL: https://apis.druva.com
  baseurl_source: declared
  description: Servers in your CloudRanger Account
  name: Druva Servers API
  slug: druva-servers-api
- baseURL: https://apis.druva.com
  baseurl_source: declared
  description: Lists the APIs to get MSP Service Monitoring reports data.
  name: Druva Service Monitoring Reports API
  slug: druva-service-monitoring-reports-api
- baseURL: https://apis.druva.com
  baseurl_source: declared
  description: Lists the APIs to get information about service plans managed.
  name: Druva Service Plans API
  slug: druva-service-plans-api
- baseURL: https://apis.druva.com
  baseurl_source: declared
  description: The SQLServer API from Druva — 15 operation(s) for sqlserver.
  name: Druva SQL Server API
  slug: druva-sqlserver-api
- baseURL: https://apis.druva.com
  baseurl_source: declared
  description: The Storage API from Druva — 1 operation(s) for storage.
  name: Druva Storage API
  slug: druva-storage-api
- baseURL: https://apis.druva.com
  baseurl_source: declared
  description: Lists the APIs to get information about the storages and inSync CloudCache Servers configured in Druva inSync.
  name: Druva Storage Management API
  slug: druva-storage-management-api
- baseURL: https://apis.druva.com
  baseurl_source: declared
  description: Lists the APIs to get information about Storage Regions.
  name: Druva Storage Regions API
  slug: druva-storage-regions-api
- baseURL: https://apis.druva.com
  baseurl_source: declared
  description: Task specific API functions
  name: Druva Tasks API
  slug: druva-tasks-api
- baseURL: https://apis.druva.com
  baseurl_source: declared
  description: Lists the APIs to get information and perform operations on tenants managed.
  name: Druva Tenants API
  slug: druva-tenants-api
- baseURL: https://apis.druva.com
  baseurl_source: declared
  description: List of APIs to get information and perform operations on the resources managed in Druva Cloud for threat hunt.
  name: Druva Threat Hunting API
  slug: druva-threat-hunting-api
- baseURL: https://apis.druva.com
  baseurl_source: declared
  description: List of APIs to view details and manage IOC Sets in the IOC library.
  name: Druva Threat Intel API
  slug: druva-threat-intel-api
- baseURL: https://apis.druva.com
  baseurl_source: declared
  description: List of APIs that helps to retrieve information and perform operations on Threat Watch. Threat Watch is an automated continuous monitoring feature that scans resources for threats every 8 hours.
  name: Druva Threat Watch API
  slug: druva-threat-watch-api
- baseURL: https://apis.druva.com
  baseurl_source: declared
  description: The Token API from Druva — 1 operation(s) for token.
  name: Druva Token API
  slug: druva-token-api
- baseURL: https://apis.druva.com
  baseurl_source: declared
  description: User specific API functions
  name: Druva User API
  slug: druva-user-api
- baseURL: https://apis.druva.com
  baseurl_source: declared
  description: Lists the APIs to get information and perform operations on users managed in Druva inSync.
  name: Druva User Management API
  slug: druva-user-management-api
- baseURL: https://apis.druva.com
  baseurl_source: declared
  description: The VMware API from Druva — 11 operation(s) for vmware.
  name: Druva V Mware API
  slug: druva-vmware-api
- baseURL: https://apis.druva.com
  baseurl_source: declared
  description: AWS Volume specific API functions
  name: Druva Volumes API
  slug: druva-volumes-api
- baseURL: https://mcp.druva.com/mcp
  baseurl_source: declared
  description: VPC specific API functions
  name: Druva VP Cs API
  slug: druva-vpcs-api
- baseURL: https://mcp.druva.com/mcp
  baseurl_source: declared
  description: Backup Policies specific API functions
  name: Druva Backup Policies API
  slug: druva-backup-policies-api
- baseURL: https://mcp.druva.com/mcp
  baseurl_source: declared
  description: The Notification Settings API from Druva — 1 operation(s) for notification settings.
  name: Druva Notification Settings API
  slug: druva-notification-settings-api
- baseURL: https://mcp.druva.com/mcp
  baseurl_source: declared
  description: The Report Subscriptions API from Druva — 4 operation(s) for report subscriptions.
  name: Druva Report Subscriptions API
  slug: druva-report-subscriptions-api
- baseURL: https://mcp.druva.com/mcp
  baseurl_source: declared
  description: The Report Templates API from Druva — 2 operation(s) for report templates.
  name: Druva Report Templates API
  slug: druva-report-templates-api
artifact_total: 101
common:
- group: other
  href: https://artifacts.apis.io/druva/capabilities/druva-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/druva-capability-edges.yml
- group: auth
  href: https://artifacts.apis.io/druva/scopes/druva-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/druva-scopes.yml
- group: agent
  href: https://artifacts.apis.io/druva/agentic-access/druva-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/druva-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/druva/security/druva-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/druva-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/druva/security/druva-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/druva-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/druva/authentication/druva-authentication.yml
  title: ''
  type: Authentication
  url: authentication/druva-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/druva
- group: company
  title: ''
  type: Website
  url: https://www.druva.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.druva.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.druva.com
- group: docs
  title: ''
  type: APIReference
  url: https://developer.druva.com/reference
- group: operate
  title: ''
  type: Support
  url: https://support.druva.com
- group: build
  title: ''
  type: GitHub
  url: https://github.com/druvainc
- group: agent
  title: ''
  type: LlmsText
  url: https://developer.druva.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://www.druva.com/blog
- group: agent
  href: https://artifacts.apis.io/druva/well-known/druva-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/druva-well-known.yml
- group: other
  href: https://artifacts.apis.io/druva/well-known/druva-api-catalog.json
  title: ''
  type: APICatalog
  url: well-known/druva-api-catalog.json
- group: agent
  href: https://artifacts.apis.io/druva/mcp/druva-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/druva-mcp.yml
- group: build
  href: https://artifacts.apis.io/druva/mcp/druva-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/druva-tool-crosswalk.yml
- group: build
  href: https://artifacts.apis.io/druva/packages/druva-packages.yml
  title: ''
  type: Packages
  url: packages/druva-packages.yml
- group: agent
  href: https://artifacts.apis.io/druva/llms/druva-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/druva-llms.txt
- group: design
  href: https://artifacts.apis.io/druva/conformance/druva-conformance.yml
  title: ''
  type: Conformance
  url: conformance/druva-conformance.yml
- group: auth
  href: https://artifacts.apis.io/druva/security/druva-trust-center.yml
  title: ''
  type: Compliance
  url: security/druva-trust-center.yml
- group: design
  href: https://artifacts.apis.io/druva/errors/druva-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/druva-problem-types.yml
- group: design
  href: https://artifacts.apis.io/druva/lifecycle/druva-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/druva-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://support.druva.com/s/druvacloudstatus
- group: operate
  title: ''
  type: Deprecation
  url: https://developer.druva.com/docs/migration-process
- group: operate
  href: https://artifacts.apis.io/druva/changelog/druva-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/druva-changelog.yml
- group: design
  href: https://artifacts.apis.io/druva/conventions/druva-conventions.yml
  title: ''
  type: Conventions
  url: conventions/druva-conventions.yml
- group: design
  href: https://artifacts.apis.io/druva/data-model/druva-data-model.yml
  title: ''
  type: DataModel
  url: data-model/druva-data-model.yml
- group: commercial
  href: https://artifacts.apis.io/druva/plans/druva-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/druva-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/druva/rate-limits/druva-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/druva-rate-limits.yml
- group: agent
  href: https://artifacts.apis.io/druva/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  href: https://artifacts.apis.io/druva/finops/druva-finops.yml
  title: ''
  type: FinOps
  url: finops/druva-finops.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://www.druva.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://login.druva.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.druva.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.druva.com/privacy-policy
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.druva.com/docs/introduction
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/druvainc
- group: other
  href: https://artifacts.apis.io/druva/overlays/druva-aws-native-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/druva-aws-native-overlay.yaml
- group: other
  href: https://artifacts.apis.io/druva/overlays/druva-cloudranger-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/druva-cloudranger-overlay.yaml
- group: other
  href: https://artifacts.apis.io/druva/overlays/druva-cyber-resilience-govcloud-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/druva-cyber-resilience-govcloud-overlay.yaml
- group: other
  href: https://artifacts.apis.io/druva/overlays/druva-cyber-resilience-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/druva-cyber-resilience-overlay.yaml
- group: other
  href: https://artifacts.apis.io/druva/overlays/druva-insync-cloud-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/druva-insync-cloud-overlay.yaml
- group: other
  href: https://artifacts.apis.io/druva/overlays/druva-insync-govcloud-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/druva-insync-govcloud-overlay.yaml
- group: other
  href: https://artifacts.apis.io/druva/overlays/druva-microsoft-365-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/druva-microsoft-365-overlay.yaml
- group: build
  href: https://artifacts.apis.io/druva/packages/druva-packages.yml
  title: ''
  type: SDKs
  url: packages/druva-packages.yml
- group: start
  title: ''
  type: Console
  url: https://login.druva.com/
created: '2026-03-27'
description: Druva is a cloud data protection and management company running the Druva Resilience Cloud, a fully managed SaaS platform for backup, disaster recovery, cyber resilience and data governance across endpoints, data centres, AWS and Azure workloads, and SaaS applications including Microsoft 365, Google Workspace, Salesforce, Dynamics 365, Entra ID and Okta. Druva publishes 19 first-party OpenAPI and Swagger definitions covering roughly 970 operations from its developer portal, advertised in an RFC 9727 API catalog document, spanning Endpoints and Data Governance, Enterprise Workloads, Cyber Resilience, AWS Native Workloads and CloudRanger, MSP tenant management, Platform administration and job management - each with a separate GovCloud contract where one exists. Authentication is OAuth 2.0 client credentials against a per-cloud token endpoint, and Druva also runs a first-party hosted MCP server at mcp.druva.com for AI agents.
finops:
- has_sources: true
  method: derived
  name: Druva Finops
  primary_unit: ''
  service_category: ''
  slug: druva-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/druva.png
layout: provider
mcp_servers:
- description: 'Druva publishes a first-party hosted MCP server that connects MCP-compatible AI clients (Claude Desktop, Cursor, VS Code, Microsoft Copilot) to the Druva Resilience Cloud under the caller''s own Druva '
  name: Druva MCP Server
  slug: druva-mcp-server
modified: '2026-09-06'
name: Druva
nav: Providers
network: true
overview: 'Druva publishes 86 API contracts indexed on the [APIs.io](https://apis.io/) network, including Accounts API, AD/LDAP Management API, Admin Roles API, and 83 more. Tagged areas include Backup, Cyber Resilience, Data Protection, Disaster Recovery, and SaaS Backup.


  The Druva catalog on APIs.io includes 1 Spectral governance ruleset.


  Druva''s developer surface includes authentication, documentation, API reference, support, GitHub presence, engineering blog, changelog, and 42 more developer resources.'
plans:
- name: Druva Plans Pricing
  plan_count: 0
  slug: druva-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 0
  name: Druva Rate Limits
  slug: druva-rate-limits
rules:
- authorship: generated
  effective_rule_count: 99
  extends:
  - spectral:oas
  name: Druva API Rules
  rule_count: 58
  severity_counts:
    error: 31
    hint: 0
    info: 9
    warn: 18
  slug: druva-rules
scopes:
- name: Druva Scopes
  scope_count: 1
  slug: druva-scopes
  summary_line: 1 scope · clientCredentials
score:
  band: strong
  composite: 57.4
  coverage:
    artifact_dirs: 29
    catalog_earned: 44.5
    catalog_earned_first_party: 0.0
    catalog_gap: 70.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 2.0
  facets:
    access_clarity: 47.4
    contract_governance: 18.2
    contract_quality: 56.4
    developer_ergonomics: 62.5
    discoverability: 80.0
    operational_transparency: 42.1
  previous_composite: 55.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 74.1
      total: 85
    mcp: first-party
    skills: derived
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
    score: 27.8
screenshot: https://apis.io/screenshots/druva/druva-2026-06-20T180253.png
security:
- kind: authentication
  name: Druva Authentication
  slug: druva-authentication
  summary_line: apiKey/http/oauth2 · 4 schemes
- kind: domain-security
  name: Druva Domain Security
  slug: druva-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Druva Trust Center
  slug: druva-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, HIPAA, FedRAMP, GDPR, CSA STAR, FIPS 140
skill_count: 5
skills:
- name: druva-authenticate
  slug: druva-authenticate
- name: druva-msp-provision-tenant
  slug: druva-msp-provision-tenant
- name: druva-on-demand-backup
  slug: druva-on-demand-backup
- name: druva-restore-workload
  slug: druva-restore-workload
- name: druva-threat-intel-ioc
  slug: druva-threat-intel-ioc
slug: druva
tags:
- Backup
- Cyber Resilience
- Data Protection
- Disaster Recovery
- SaaS Backup
- Ransomware Recovery
- Data Governance
- Enterprise Workloads
- MSP
- Legal Hold
- GovCloud
- MCP
website: https://www.druva.com
---
