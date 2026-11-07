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
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: documented
    operation_distinctiveness: mostly
    pagination_ratio: partial
    protected_resource_metadata: verified
    rate_limit_signal: derived
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 50.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 512
  human_in_the_loop: 28
  name: Delinea Agentic Access
  operation_count: 1037
  slug: delinea-agentic-access
  summary_line: 1037 operations · 512 acting · 28 human-in-the-loop
api_count: 1
apis:
- description: REST API for Delinea Secret Server enabling programmatic management of privileged credentials, secrets, folders, permissions, and session recording. Supports Bearer token, OAuth 2.0, and Windows Integ
  name: Secret Server REST API
  slug: secret-server-api
- description: REST API for Delinea DevOps Secrets Vault (DSV), a cloud-native secrets management service for DevOps pipelines. Provides endpoints for secrets CRUD, token management, role-based access control, encry
  name: DevOps Secrets Vault API
  slug: devops-secrets-vault-api
- description: Platform-level REST API for Delinea's unified cloud platform enabling OAuth 2.0 authentication, role and group management, service account operations, and integration with Secret Server through the pl
  name: Delinea Platform API
  slug: platform-api
- baseURL: https://your-secret-server-instance/api/v1
  baseurl_source: declared
  description: Activate Licenses
  name: Delinea Activations API
  slug: delinea-activations-api
- baseURL: https://your-secret-server-instance/api/v1
  baseurl_source: declared
  description: AdvancedConfigSettingsController
  name: Delinea AdvancedConfigSettings API
  slug: delinea-advancedconfigsettings-api
- baseURL: https://your-secret-server-instance/api/v1
  baseurl_source: declared
  description: View and maintain app clients
  name: Delinea AppClients API
  slug: delinea-appclients-api
- baseURL: https://your-secret-server-instance/api/v1
  baseurl_source: declared
  description: View and maintain users
  name: Delinea ApplicationAccounts API
  slug: delinea-applicationaccounts-api
- baseURL: https://your-secret-server-instance/api/v1
  baseurl_source: declared
  description: ApplicationRequestController
  name: Delinea ApplicationRequest API
  slug: delinea-applicationrequest-api
- baseURL: https://your-secret-server-instance/api/v1
  baseurl_source: declared
  description: AppStateController
  name: Delinea AppState API
  slug: delinea-appstate-api
- baseURL: https://your-secret-server-instance/api/v1
  baseurl_source: declared
  description: Create Bulk Secret Operations
  name: Delinea BulkSecretOperations API
  slug: delinea-bulksecretoperations-api
- baseURL: https://your-secret-server-instance/api/v1
  baseurl_source: declared
  description: Export and Import Bundles
  name: Delinea Bundle API
  slug: delinea-bundle-api
- baseURL: https://your-secret-server-instance/api/v1
  baseurl_source: declared
  description: View and maintain lists of options
  name: Delinea CategorizedLists API
  slug: delinea-categorizedlists-api
- baseURL: https://your-secret-server-instance/api/v1
  baseurl_source: declared
  description: Character Sets used in password requirements
  name: Delinea CharacterSets API
  slug: delinea-charactersets-api
- baseURL: https://your-secret-server-instance/api/v1
  baseurl_source: declared
  description: View cloud diagnostics information
  name: Delinea CloudDiagnostics API
  slug: delinea-clouddiagnostics-api
- baseURL: https://your-secret-server-instance/api/v1
  baseurl_source: declared
  description: Secret Server Configuration
  name: Delinea Configuration API
  slug: delinea-configuration-api
- baseURL: https://your-secret-server-instance/api/v1
  baseurl_source: declared
  description: ConnectionManagerSettingsController
  name: Delinea ConnectionManagerSettings API
  slug: delinea-connectionmanagersettings-api
- baseURL: https://your-secret-server-instance/api/v1
  baseurl_source: declared
  description: DependencyChangerController
  name: Delinea DependencyChanger API
  slug: delinea-dependencychanger-api
- baseURL: https://your-secret-server-instance/api/v1
  baseurl_source: declared
  description: Manage secrets that are synced to DSV Tenants.
  name: Delinea DevOpsSecretsVaultSync API
  slug: delinea-devopssecretsvaultsync-api
- baseURL: https://your-secret-server-instance/api/v1
  baseurl_source: declared
  description: Manage the tenants SS can communicate with in DevOps Secrets Vault.
  name: Delinea DevOpsSecretsVaultTenant API
  slug: delinea-devopssecretsvaulttenant-api
- baseURL: https://your-secret-server-instance/api/v1
  baseurl_source: declared
  description: View diagnostics information
  name: Delinea Diagnostics API
  slug: delinea-diagnostics-api
- baseURL: https://your-secret-server-instance/api/v1
  baseurl_source: declared
  description: View diagnostics information
  name: Delinea DiagnosticsV2 API
  slug: delinea-diagnosticsv2-api
- baseURL: https://your-secret-server-instance/api/v1
  baseurl_source: declared
  description: DiscoveryController
  name: Delinea Discovery API
  slug: delinea-discovery-api
- baseURL: https://your-secret-server-instance/api/v1
  baseurl_source: declared
  description: View and maintain Distributed Engine integrations
  name: Delinea DistributedEngine API
  slug: delinea-distributedengine-api
- baseURL: https://your-secret-server-instance/api/v1
  baseurl_source: declared
  description: DomainNameIndexController
  name: Delinea DomainNameIndex API
  slug: delinea-domainnameindex-api
- baseURL: https://your-secret-server-instance/api/v1
  baseurl_source: declared
  description: View and maintain dual controls
  name: Delinea DualControls API
  slug: delinea-dualcontrols-api
- baseURL: https://your-secret-server-instance/api/v1
  baseurl_source: declared
  description: View enterprise related data
  name: Delinea Enterprise API
  slug: delinea-enterprise-api
- baseURL: https://your-secret-server-instance/api/v1
  baseurl_source: declared
  description: EventPipelineController
  name: Delinea EventPipeline API
  slug: delinea-eventpipeline-api
- baseURL: https://your-secret-server-instance/api/v1
  baseurl_source: declared
  description: EventPipelineAuditController
  name: Delinea EventPipelineAudit API
  slug: delinea-eventpipelineaudit-api
- baseURL: https://your-secret-server-instance/api/v1
  baseurl_source: declared
  description: EventPipelinePolicyController
  name: Delinea EventPipelinePolicy API
  slug: delinea-eventpipelinepolicy-api
- baseURL: https://your-secret-server-instance/api/v1
  baseurl_source: declared
  description: EventPipelineSettingsController
  name: Delinea EventPipelineSettings API
  slug: delinea-eventpipelinesettings-api
- baseURL: https://your-secret-server-instance/api/v1
  baseurl_source: declared
  description: EventPipelineTriggerController
  name: Delinea EventPipelineTrigger API
  slug: delinea-eventpipelinetrigger-api
- baseURL: https://your-secret-server-instance/api/v1
  baseurl_source: declared
  description: Extended Fields provider
  name: Delinea ExtendedFields API
  slug: delinea-extendedfields-api
- baseURL: https://your-secret-server-instance/api/v1
  baseurl_source: declared
  description: View and maintain secret folders
  name: Delinea Folders API
  slug: delinea-folders-api
- baseURL: https://your-secret-server-instance/api/v1
  baseurl_source: declared
  description: View and maintain user security groups
  name: Delinea Groups API
  slug: delinea-groups-api
- baseURL: https://your-secret-server-instance/api/v1
  baseurl_source: declared
  description: Secret Server HSM Configuration
  name: Delinea HsmConfiguration API
  slug: delinea-hsmconfiguration-api
- baseURL: https://your-secret-server-instance/api/v1
  baseurl_source: declared
  description: InboxController
  name: Delinea Inbox API
  slug: delinea-inbox-api
- baseURL: https://your-secret-server-instance/api/v1
  baseurl_source: declared
  description: InboxRulesController
  name: Delinea InboxRules API
  slug: delinea-inboxrules-api
- baseURL: https://your-secret-server-instance/api/v1
  baseurl_source: declared
  description: InstallController
  name: Delinea Install API
  slug: delinea-install-api
- baseURL: https://your-secret-server-instance/api/v1
  baseurl_source: declared
  description: View and maintain IP Address restrictions
  name: Delinea IpAddressRestrictions API
  slug: delinea-ipaddressrestrictions-api
- baseURL: https://your-secret-server-instance/api/v1
  baseurl_source: declared
  description: JumpboxRouteController
  name: Delinea JumpboxRoute API
  slug: delinea-jumpboxroute-api
- baseURL: https://your-secret-server-instance/api/v1
  baseurl_source: declared
  description: Manage Launcher Agents and Launcher Agent Collections for Advanced Session Recording
  name: Delinea LauncherAgents API
  slug: delinea-launcheragents-api
- baseURL: https://your-secret-server-instance/api/v1
  baseurl_source: declared
  description: View available application launchers
  name: Delinea Launchers API
  slug: delinea-launchers-api
- baseURL: https://your-secret-server-instance/api/v1
  baseurl_source: declared
  description: LicenseController
  name: Delinea License API
  slug: delinea-license-api
- baseURL: https://your-secret-server-instance/api/v1
  baseurl_source: declared
  description: MetadataController
  name: Delinea Metadata API
  slug: delinea-metadata-api
- baseURL: https://your-secret-server-instance/api/v1
  baseurl_source: declared
  description: MobileController
  name: Delinea Mobile API
  slug: delinea-mobile-api
- baseURL: https://your-secret-server-instance/api/v1
  baseurl_source: declared
  description: Expire the current user session
  name: Delinea OAuthExpiration API
  slug: delinea-oauthexpiration-api
- baseURL: https://your-secret-server-instance/api/v1
  baseurl_source: declared
  description: View and maintain one time passwords
  name: Delinea OneTimePasswordCode API
  slug: delinea-onetimepasswordcode-api
- baseURL: https://your-secret-server-instance/api/v1
  baseurl_source: declared
  description: Password Requirements
  name: Delinea PasswordRequirements API
  slug: delinea-passwordrequirements-api
- baseURL: https://your-secret-server-instance/api/v1
  baseurl_source: declared
  description: View and configure Privilege Behavior Analytics
  name: Delinea PbaConfiguration API
  slug: delinea-pbaconfiguration-api
- baseURL: https://your-secret-server-instance/api/v1
  baseurl_source: declared
  description: View and maintain Platform integration
  name: Delinea Platform API
  slug: delinea-platform-api
- baseURL: https://your-secret-server-instance/api/v1
  baseurl_source: declared
  description: Retrieve and update SSH and RDP proxy configurations
  name: Delinea Proxy API
  slug: delinea-proxy-api
- baseURL: https://your-secret-server-instance/api/v1
  baseurl_source: declared
  description: View Password Changing Settings
  name: Delinea RemotePasswordChanging API
  slug: delinea-remotepasswordchanging-api
- baseURL: https://your-secret-server-instance/api/v1
  baseurl_source: declared
  description: View and maintain Reports
  name: Delinea Reports API
  slug: delinea-reports-api
- baseURL: https://your-secret-server-instance/api/v1
  baseurl_source: declared
  description: REST API Doc Services
  name: Delinea RestApiDocs API
  slug: delinea-restapidocs-api
- baseURL: https://your-secret-server-instance/api/v1
  baseurl_source: declared
  description: View User Role Audits
  name: Delinea RoleAudit API
  slug: delinea-roleaudit-api
- baseURL: https://your-secret-server-instance/api/v1
  baseurl_source: declared
  description: View and maintain User Roles
  name: Delinea Roles API
  slug: delinea-roles-api
- baseURL: https://your-secret-server-instance/api/v1
  baseurl_source: declared
  description: ScheduleController
  name: Delinea Schedule API
  slug: delinea-schedule-api
- baseURL: https://your-secret-server-instance/api/v1
  baseurl_source: declared
  description: View Scripts
  name: Delinea Script API
  slug: delinea-script-api
- baseURL: https://your-secret-server-instance/api/v1
  baseurl_source: declared
  description: View and maintain SDK Client Accounts
  name: Delinea SdkClientAccounts API
  slug: delinea-sdkclientaccounts-api
- baseURL: https://your-secret-server-instance/api/v1
  baseurl_source: declared
  description: View SDK Client Audits
  name: Delinea SdkClientAudits API
  slug: delinea-sdkclientaudits-api
- baseURL: https://your-secret-server-instance/api/v1
  baseurl_source: declared
  description: View and maintain SDK Client Rules
  name: Delinea SdkClientRules API
  slug: delinea-sdkclientrules-api
- baseURL: https://your-secret-server-instance/api/v1
  baseurl_source: declared
  description: SecretAccessRequestsController
  name: Delinea SecretAccessRequests API
  slug: delinea-secretaccessrequests-api
- baseURL: https://your-secret-server-instance/api/v1
  baseurl_source: declared
  description: View and maintain Secret Dependencies
  name: Delinea SecretDependencies API
  slug: delinea-secretdependencies-api
- baseURL: https://your-secret-server-instance/api/v1
  baseurl_source: declared
  description: SecretEraseRequestsController
  name: Delinea SecretEraseRequests API
  slug: delinea-secreteraserequests-api
- baseURL: https://your-secret-server-instance/api/v1
  baseurl_source: declared
  description: Specialized calls for Thycotic Secret Server Extensions. Thycotic may change the functionality or signatures under the secret-extensions route. Use at your own risk.
  name: Delinea SecretExtensions API
  slug: delinea-secretextensions-api
- baseURL: https://your-secret-server-instance/api/v1
  baseurl_source: declared
  description: SecretHealthController
  name: Delinea SecretHealth API
  slug: delinea-secrethealth-api
- baseURL: https://your-secret-server-instance/api/v1
  baseurl_source: declared
  description: View and maintain Secret hooks
  name: Delinea SecretHooks API
  slug: delinea-secrethooks-api
- baseURL: https://your-secret-server-instance/api/v1
  baseurl_source: declared
  description: View and maintain secret permissions
  name: Delinea SecretPermissions API
  slug: delinea-secretpermissions-api
- baseURL: https://your-secret-server-instance/api/v1
  baseurl_source: declared
  description: Retrieve and update Secret Policies
  name: Delinea SecretPolicy API
  slug: delinea-secretpolicy-api
- baseURL: https://your-secret-server-instance/api/v1
  baseurl_source: declared
  description: View and maintain Secrets
  name: Delinea Secrets API
  slug: delinea-secrets-api
- baseURL: https://your-secret-server-instance/api/v1
  baseurl_source: declared
  description: Secret Server Settings
  name: Delinea SecretServerSettings API
  slug: delinea-secretserversettings-api
- baseURL: https://your-secret-server-instance/api/v1
  baseurl_source: declared
  description: View recorded sessions
  name: Delinea SecretSessions API
  slug: delinea-secretsessions-api
- baseURL: https://your-secret-server-instance/api/v1
  baseurl_source: declared
  description: Secret Template Permissions
  name: Delinea SecretTemplatePermissions API
  slug: delinea-secrettemplatepermissions-api
- baseURL: https://your-secret-server-instance/api/v1
  baseurl_source: declared
  description: View secret templates
  name: Delinea SecretTemplates API
  slug: delinea-secrettemplates-api
- baseURL: https://your-secret-server-instance/api/v1
  baseurl_source: declared
  description: View Security Audit Logs
  name: Delinea SecurityAuditLogs API
  slug: delinea-securityauditlogs-api
- baseURL: https://your-secret-server-instance/api/v1
  baseurl_source: declared
  description: View nodes and update roles or readonly mode
  name: Delinea ServerNodes API
  slug: delinea-servernodes-api
- baseURL: https://your-secret-server-instance/api/v1
  baseurl_source: declared
  description: SitesController
  name: Delinea Sites API
  slug: delinea-sites-api
- baseURL: https://your-secret-server-instance/api/v1
  baseurl_source: declared
  description: SlackController
  name: Delinea Slack API
  slug: delinea-slack-api
- baseURL: https://your-secret-server-instance/api/v1
  baseurl_source: declared
  description: SshCipherSuiteController
  name: Delinea SshCipherSuite API
  slug: delinea-sshciphersuite-api
- baseURL: https://your-secret-server-instance/api/v1
  baseurl_source: declared
  description: View and maintain SSH Commands
  name: Delinea SshCommand API
  slug: delinea-sshcommand-api
- baseURL: https://your-secret-server-instance/api/v1
  baseurl_source: declared
  description: View and maintain SSH Command Blocklists
  name: Delinea SshCommandBlocklist API
  slug: delinea-sshcommandblocklist-api
- baseURL: https://your-secret-server-instance/api/v1
  baseurl_source: declared
  description: View and maintain SSH Command Menus
  name: Delinea SshCommandMenu API
  slug: delinea-sshcommandmenu-api
- baseURL: https://your-secret-server-instance/api/v1
  baseurl_source: declared
  description: SubscriptionsController
  name: Delinea Subscriptions API
  slug: delinea-subscriptions-api
- baseURL: https://your-secret-server-instance/api/v1
  baseurl_source: declared
  description: View and maintain user security teams
  name: Delinea Teams API
  slug: delinea-teams-api
- baseURL: https://your-secret-server-instance/api/v1
  baseurl_source: declared
  description: View and maintain users
  name: Delinea Users API
  slug: delinea-users-api
- baseURL: https://your-secret-server-instance/api/v1
  baseurl_source: declared
  description: Secret Server Version
  name: Delinea Version API
  slug: delinea-version-api
- baseURL: https://your-secret-server-instance/api/v1
  baseurl_source: declared
  description: View and maintain Workflow Template Steps
  name: Delinea WorkflowStepTemplates API
  slug: delinea-workflowsteptemplates-api
- baseURL: https://your-secret-server-instance/api/v1
  baseurl_source: declared
  description: View and maintain Active Directory
  name: Delinea Active Directory API
  slug: delinea-active-directory-api
- baseURL: https://your-secret-server-instance/api/v1
  baseurl_source: declared
  description: API Token Generation
  name: Delinea API Token API
  slug: delinea-api-token-api
- baseURL: https://your-secret-server-instance/api/v1
  baseurl_source: declared
  description: View Bulk Operations
  name: Delinea Bulk Operations API
  slug: delinea-bulk-operations-api
- baseURL: https://your-secret-server-instance/api/v1
  baseurl_source: declared
  description: Create Bulk User Operations
  name: Delinea Bulk User Operations API
  slug: delinea-bulk-user-operations-api
- baseURL: https://your-secret-server-instance/api/v1
  baseurl_source: declared
  description: View and maintain Directory Services integrations
  name: Delinea Directory Services API
  slug: delinea-directory-services-api
- baseURL: https://your-secret-server-instance/api/v1
  baseurl_source: declared
  description: Disaster Recovery
  name: Delinea Disaster Recovery API
  slug: delinea-disaster-recovery-api
- baseURL: https://your-secret-server-instance/api/v1
  baseurl_source: declared
  description: EventSubscriptionsController
  name: Delinea Event Subscriptions API
  slug: delinea-event-subscriptions-api
- baseURL: https://your-secret-server-instance/api/v1
  baseurl_source: declared
  description: FeatureFlagController
  name: Delinea Feature Flag API
  slug: delinea-feature-flag-api
- baseURL: https://your-secret-server-instance/api/v1
  baseurl_source: declared
  description: View and maintain secret folder permissions
  name: Delinea Folder Permissions API
  slug: delinea-folder-permissions-api
- baseURL: https://your-secret-server-instance/api/v1
  baseurl_source: declared
  description: HealthCheckController
  name: Delinea Health Check API
  slug: delinea-health-check-api
- baseURL: https://your-secret-server-instance/api/v1
  baseurl_source: declared
  description: View and configure Key Management settings
  name: Delinea Key Management API
  slug: delinea-key-management-api
- baseURL: https://your-secret-server-instance/api/v1
  baseurl_source: declared
  description: RolePermissionsController
  name: Delinea Role Permissions API
  slug: delinea-role-permissions-api
- baseURL: https://your-secret-server-instance/api/v1
  baseurl_source: declared
  description: TicketSystemsController
  name: Delinea Ticket Systems API
  slug: delinea-ticket-systems-api
- baseURL: https://your-secret-server-instance/api/v1
  baseurl_source: declared
  description: View and maintain Workflow Instances
  name: Delinea Workflow Instances API
  slug: delinea-workflow-instances-api
- baseURL: https://your-secret-server-instance/api/v1
  baseurl_source: declared
  description: View and maintain Workflow Templates
  name: Delinea Workflow Templates API
  slug: delinea-workflow-templates-api
artifact_total: 483
asyncapis:
- description: ''
  name: Delinea Webhooks
  slug: delinea-webhooks
collections:
- collection_type: open
  name: Secret Server Rest Activations API
  slug: open-delinea-activations-api
- collection_type: open
  name: Secret Server Rest Activations ActiveDirectory API
  slug: open-delinea-activedirectory-api
- collection_type: open
  name: Secret Server Rest Activations AdvancedConfigSettings API
  slug: open-delinea-advancedconfigsettings-api
- collection_type: open
  name: Secret Server Rest Activations ApiToken API
  slug: open-delinea-apitoken-api
- collection_type: open
  name: Secret Server Rest Activations AppClients API
  slug: open-delinea-appclients-api
- collection_type: open
  name: Secret Server Rest Activations ApplicationAccounts API
  slug: open-delinea-applicationaccounts-api
- collection_type: open
  name: Secret Server Rest Activations ApplicationRequest API
  slug: open-delinea-applicationrequest-api
- collection_type: open
  name: Secret Server Rest Activations AppState API
  slug: open-delinea-appstate-api
- collection_type: open
  name: Secret Server Rest Activations BulkOperations API
  slug: open-delinea-bulkoperations-api
- collection_type: open
  name: Secret Server Rest Activations BulkSecretOperations API
  slug: open-delinea-bulksecretoperations-api
- collection_type: open
  name: Secret Server Rest Activations BulkUserOperations API
  slug: open-delinea-bulkuseroperations-api
- collection_type: open
  name: Secret Server Rest Activations Bundle API
  slug: open-delinea-bundle-api
- collection_type: open
  name: Secret Server Rest Activations CategorizedLists API
  slug: open-delinea-categorizedlists-api
- collection_type: open
  name: Secret Server Rest Activations CharacterSets API
  slug: open-delinea-charactersets-api
- collection_type: open
  name: Secret Server Rest Activations CloudDiagnostics API
  slug: open-delinea-clouddiagnostics-api
- collection_type: open
  name: Secret Server Rest Activations Configuration API
  slug: open-delinea-configuration-api
- collection_type: open
  name: Secret Server Rest Activations ConnectionManagerSettings API
  slug: open-delinea-connectionmanagersettings-api
- collection_type: open
  name: Secret Server Rest Activations DependencyChanger API
  slug: open-delinea-dependencychanger-api
- collection_type: open
  name: Secret Server Rest Activations DevOpsSecretsVaultSync API
  slug: open-delinea-devopssecretsvaultsync-api
- collection_type: open
  name: Secret Server Rest Activations DevOpsSecretsVaultTenant API
  slug: open-delinea-devopssecretsvaulttenant-api
- collection_type: open
  name: Secret Server Rest Activations Diagnostics API
  slug: open-delinea-diagnostics-api
- collection_type: open
  name: Secret Server Rest Activations DiagnosticsV2 API
  slug: open-delinea-diagnosticsv2-api
- collection_type: open
  name: Secret Server Rest Activations DirectoryServices API
  slug: open-delinea-directoryservices-api
- collection_type: open
  name: Secret Server Rest Activations DisasterRecovery API
  slug: open-delinea-disasterrecovery-api
- collection_type: open
  name: Secret Server Rest Activations Discovery API
  slug: open-delinea-discovery-api
- collection_type: open
  name: Secret Server Rest Activations DistributedEngine API
  slug: open-delinea-distributedengine-api
- collection_type: open
  name: Secret Server Rest Activations DomainNameIndex API
  slug: open-delinea-domainnameindex-api
- collection_type: open
  name: Secret Server Rest Activations DualControls API
  slug: open-delinea-dualcontrols-api
- collection_type: open
  name: Secret Server Rest Activations Enterprise API
  slug: open-delinea-enterprise-api
- collection_type: open
  name: Secret Server Rest Activations EventPipeline API
  slug: open-delinea-eventpipeline-api
- collection_type: open
  name: Secret Server Rest Activations EventPipelineAudit API
  slug: open-delinea-eventpipelineaudit-api
- collection_type: open
  name: Secret Server Rest Activations EventPipelinePolicy API
  slug: open-delinea-eventpipelinepolicy-api
- collection_type: open
  name: Secret Server Rest Activations EventPipelineSettings API
  slug: open-delinea-eventpipelinesettings-api
- collection_type: open
  name: Secret Server Rest Activations EventPipelineTrigger API
  slug: open-delinea-eventpipelinetrigger-api
- collection_type: open
  name: Secret Server Rest Activations EventSubscriptions API
  slug: open-delinea-eventsubscriptions-api
- collection_type: open
  name: Secret Server Rest Activations ExtendedFields API
  slug: open-delinea-extendedfields-api
- collection_type: open
  name: Secret Server Rest Activations FeatureFlag API
  slug: open-delinea-featureflag-api
- collection_type: open
  name: Secret Server Rest Activations FolderPermissions API
  slug: open-delinea-folderpermissions-api
- collection_type: open
  name: Secret Server Rest Activations Folders API
  slug: open-delinea-folders-api
- collection_type: open
  name: Secret Server Rest Activations Groups API
  slug: open-delinea-groups-api
- collection_type: open
  name: Secret Server Rest Activations HealthCheck API
  slug: open-delinea-healthcheck-api
- collection_type: open
  name: Secret Server Rest Activations HsmConfiguration API
  slug: open-delinea-hsmconfiguration-api
- collection_type: open
  name: Secret Server Rest Activations Inbox API
  slug: open-delinea-inbox-api
- collection_type: open
  name: Secret Server Rest Activations InboxRules API
  slug: open-delinea-inboxrules-api
- collection_type: open
  name: Secret Server Rest Activations Install API
  slug: open-delinea-install-api
- collection_type: open
  name: Secret Server Rest Activations IpAddressRestrictions API
  slug: open-delinea-ipaddressrestrictions-api
- collection_type: open
  name: Secret Server Rest Activations JumpboxRoute API
  slug: open-delinea-jumpboxroute-api
- collection_type: open
  name: Secret Server Rest Activations KeyManagement API
  slug: open-delinea-keymanagement-api
- collection_type: open
  name: Secret Server Rest Activations LauncherAgents API
  slug: open-delinea-launcheragents-api
- collection_type: open
  name: Secret Server Rest Activations Launchers API
  slug: open-delinea-launchers-api
- collection_type: open
  name: Secret Server Rest Activations License API
  slug: open-delinea-license-api
- collection_type: open
  name: Secret Server Rest Activations Metadata API
  slug: open-delinea-metadata-api
- collection_type: open
  name: Secret Server Rest Activations Mobile API
  slug: open-delinea-mobile-api
- collection_type: open
  name: Secret Server Rest Activations OAuthExpiration API
  slug: open-delinea-oauthexpiration-api
- collection_type: open
  name: Secret Server Rest Activations OneTimePasswordCode API
  slug: open-delinea-onetimepasswordcode-api
- collection_type: open
  name: Secret Server Rest Activations PasswordRequirements API
  slug: open-delinea-passwordrequirements-api
- collection_type: open
  name: Secret Server Rest Activations PbaConfiguration API
  slug: open-delinea-pbaconfiguration-api
- collection_type: open
  name: Secret Server Rest Activations Platform API
  slug: open-delinea-platform-api
- collection_type: open
  name: Secret Server Rest Activations Proxy API
  slug: open-delinea-proxy-api
- collection_type: open
  name: Secret Server Rest Activations RemotePasswordChanging API
  slug: open-delinea-remotepasswordchanging-api
- collection_type: open
  name: Secret Server Rest Activations Reports API
  slug: open-delinea-reports-api
- collection_type: open
  name: Secret Server Rest Activations RestApiDocs API
  slug: open-delinea-restapidocs-api
- collection_type: open
  name: Secret Server Rest Activations RoleAudit API
  slug: open-delinea-roleaudit-api
- collection_type: open
  name: Secret Server Rest Activations RolePermissions API
  slug: open-delinea-rolepermissions-api
- collection_type: open
  name: Secret Server Rest Activations Roles API
  slug: open-delinea-roles-api
- collection_type: open
  name: Secret Server Rest Activations Schedule API
  slug: open-delinea-schedule-api
- collection_type: open
  name: Secret Server Rest Activations Script API
  slug: open-delinea-script-api
- collection_type: open
  name: Secret Server Rest Activations SdkClientAccounts API
  slug: open-delinea-sdkclientaccounts-api
- collection_type: open
  name: Secret Server Rest Activations SdkClientAudits API
  slug: open-delinea-sdkclientaudits-api
- collection_type: open
  name: Secret Server Rest Activations SdkClientRules API
  slug: open-delinea-sdkclientrules-api
- collection_type: open
  name: Secret Server Rest Activations SecretAccessRequests API
  slug: open-delinea-secretaccessrequests-api
- collection_type: open
  name: Secret Server Rest Activations SecretDependencies API
  slug: open-delinea-secretdependencies-api
- collection_type: open
  name: Secret Server Rest Activations SecretEraseRequests API
  slug: open-delinea-secreteraserequests-api
- collection_type: open
  name: Secret Server Rest Activations SecretExtensions API
  slug: open-delinea-secretextensions-api
- collection_type: open
  name: Secret Server Rest Activations SecretHealth API
  slug: open-delinea-secrethealth-api
- collection_type: open
  name: Secret Server Rest Activations SecretHooks API
  slug: open-delinea-secrethooks-api
- collection_type: open
  name: Secret Server Rest Activations SecretPermissions API
  slug: open-delinea-secretpermissions-api
- collection_type: open
  name: Secret Server Rest Activations SecretPolicy API
  slug: open-delinea-secretpolicy-api
- collection_type: open
  name: Secret Server Rest Activations Secrets API
  slug: open-delinea-secrets-api
- collection_type: open
  name: Secret Server Rest Activations SecretServerSettings API
  slug: open-delinea-secretserversettings-api
- collection_type: open
  name: Secret Server Rest Activations SecretSessions API
  slug: open-delinea-secretsessions-api
- collection_type: open
  name: Secret Server Rest Activations SecretTemplatePermissions API
  slug: open-delinea-secrettemplatepermissions-api
- collection_type: open
  name: Secret Server Rest Activations SecretTemplates API
  slug: open-delinea-secrettemplates-api
- collection_type: open
  name: Secret Server Rest Activations SecurityAuditLogs API
  slug: open-delinea-securityauditlogs-api
- collection_type: open
  name: Secret Server Rest Activations ServerNodes API
  slug: open-delinea-servernodes-api
- collection_type: open
  name: Secret Server Rest Activations Sites API
  slug: open-delinea-sites-api
- collection_type: open
  name: Secret Server Rest Activations Slack API
  slug: open-delinea-slack-api
- collection_type: open
  name: Secret Server Rest Activations SshCipherSuite API
  slug: open-delinea-sshciphersuite-api
- collection_type: open
  name: Secret Server Rest Activations SshCommand API
  slug: open-delinea-sshcommand-api
- collection_type: open
  name: Secret Server Rest Activations SshCommandBlocklist API
  slug: open-delinea-sshcommandblocklist-api
- collection_type: open
  name: Secret Server Rest Activations SshCommandMenu API
  slug: open-delinea-sshcommandmenu-api
- collection_type: open
  name: Secret Server Rest Activations Subscriptions API
  slug: open-delinea-subscriptions-api
- collection_type: open
  name: Secret Server Rest Activations Teams API
  slug: open-delinea-teams-api
- collection_type: open
  name: Secret Server Rest Activations TicketSystems API
  slug: open-delinea-ticketsystems-api
- collection_type: open
  name: Secret Server Rest Activations Users API
  slug: open-delinea-users-api
- collection_type: open
  name: Secret Server Rest Activations Version API
  slug: open-delinea-version-api
- collection_type: open
  name: Secret Server Rest Activations WorkflowInstances API
  slug: open-delinea-workflowinstances-api
- collection_type: open
  name: Secret Server Rest Activations WorkflowStepTemplates API
  slug: open-delinea-workflowsteptemplates-api
- collection_type: open
  name: Secret Server Rest Activations WorkflowTemplates API
  slug: open-delinea-workflowtemplates-api
common:
- group: design
  href: https://artifacts.apis.io/delinea/rules/delinea-rules.yml
  title: ''
  type: Spectral
  url: rules/delinea-rules.yml
- group: design
  href: https://artifacts.apis.io/delinea/rules/delinea-jsonschema-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/delinea-jsonschema-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/delinea/json-ld/delinea-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/delinea-context.jsonld
- group: design
  href: https://artifacts.apis.io/delinea/vocabulary/delinea-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/delinea-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/delinea/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/delinea/asyncapi/delinea-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/delinea-webhooks.yml
- group: design
  href: https://artifacts.apis.io/delinea/data-model/delinea-data-model.yml
  title: ''
  type: DataModel
  url: data-model/delinea-data-model.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.delinea.com/
- group: auth
  title: ''
  type: Security
  url: https://trust.delinea.com/?itemUid=56583ca0-6561-4cf3-a150-8c0c45d214cf
- group: design
  href: https://artifacts.apis.io/delinea/errors/delinea-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/delinea-problem-types.yml
- group: design
  href: https://artifacts.apis.io/delinea/conformance/delinea-conformance.yml
  title: ''
  type: Conformance
  url: conformance/delinea-conformance.yml
- group: agent
  href: https://artifacts.apis.io/delinea/llms/delinea-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/delinea-llms.txt
- group: auth
  href: https://artifacts.apis.io/delinea/well-known/delinea-your-tenant-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/delinea-your-tenant-security.txt
- group: auth
  href: https://artifacts.apis.io/delinea/well-known/delinea-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/delinea-status-security.txt
- group: auth
  href: https://artifacts.apis.io/delinea/well-known/delinea-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/delinea-security.txt
- group: auth
  href: https://artifacts.apis.io/delinea/well-known/delinea-api-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/delinea-api-security.txt
- group: agent
  href: https://artifacts.apis.io/delinea/well-known/delinea-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/delinea-well-known.yml
- group: other
  href: https://artifacts.apis.io/delinea/hosts/delinea-hosts.yml
  title: ''
  type: Hosts
  url: hosts/delinea-hosts.yml
- group: other
  href: https://artifacts.apis.io/delinea/vendors/delinea-vendors.yml
  title: ''
  type: Vendors
  url: vendors/delinea-vendors.yml
- group: build
  href: https://artifacts.apis.io/delinea/packages/delinea-packages.yml
  title: ''
  type: Packages
  url: packages/delinea-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://community.delinea.com/site/terms
- group: operate
  title: ''
  type: Support
  url: https://support.delinea.com/s/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://delinea.com/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://delinea.com/news
- group: other
  title: ''
  type: Leadership
  url: https://delinea.com/leadership
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.delinea.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.delinea.com/changelog
- group: docs
  title: ''
  type: APIReference
  url: https://developer.delinea.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.delinea.com/reference/post_quickstart-getstate
- group: other
  href: https://artifacts.apis.io/delinea/capabilities/delinea-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/delinea-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/delinea/agentic-access/delinea-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/delinea-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/delinea/security/delinea-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/delinea-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/delinea/security/delinea-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/delinea-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/delinea/security/delinea-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/delinea-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/delinea/authentication/delinea-authentication.yml
  title: ''
  type: Authentication
  url: authentication/delinea-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://delinea.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.delinea.com/online-help/library/start.htm
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/DelineaXPM
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/delinea/
- group: company
  title: ''
  type: Blog
  url: https://delinea.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://delinea.com/products/delinea-platform-bundles
- group: operate
  title: ''
  type: StatusPage
  url: https://status.delinea.com/
- group: other
  title: ''
  type: X
  url: https://x.com/DelineaInc
- group: commercial
  href: https://artifacts.apis.io/delinea/plans/delinea-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/delinea-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/delinea/rate-limits/delinea-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/delinea-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/delinea/finops/delinea-finops.yml
  title: ''
  type: FinOps
  url: finops/delinea-finops.yml
created: '2026-06-13'
description: Delinea is a privileged access management (PAM) platform providing REST APIs for Secret Server, DevOps Secrets Vault, Privilege Manager, and Cloud Suite. It enables organizations to manage, rotate, and audit privileged credentials, sessions, and access policies across on-premises and cloud infrastructure.
examples:
- key_count: 3
  name: Configuration
  slug: configuration
- key_count: 3
  name: Directoryservices
  slug: directoryservices
- key_count: 3
  name: Folders
  slug: folders
- key_count: 3
  name: Groups
  slug: groups
- key_count: 3
  name: Platform
  slug: platform
- key_count: 3
  name: Recorded Sessions
  slug: recorded-sessions
- key_count: 3
  name: Reports
  slug: reports
- key_count: 3
  name: Secret Templates
  slug: secret-templates
- key_count: 3
  name: Secrets
  slug: secrets
- key_count: 3
  name: Users
  slug: users
- key_count: 3
  name: Workflows
  slug: workflows
finops:
- has_sources: true
  method: derived
  name: Delinea Finops
  primary_unit: ''
  service_category: ''
  slug: delinea-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/delinea.png
json_schemas:
- name: AuthenticationFailedResponse
  property_count: 1
  slug: authenticationfailedresponse
- name: BadRequestResponse
  property_count: 4
  slug: badrequestresponse
- name: AppClientCreateArgs
  property_count: 1
  slug: delinea-app-client-create-args
- name: AppClientModel
  property_count: 3
  slug: delinea-app-client-model
- name: AppClientUpdateArgs
  property_count: 2
  slug: delinea-app-client-update-args
- name: AppSettingModel
  property_count: 2
  slug: delinea-app-setting-model
- name: AppStateModel
  property_count: 3
  slug: delinea-app-state-model
- name: ApplicationAccessRequestUpdateArgs
  property_count: 1
  slug: delinea-application-access-request-update-args
- name: ApplicationAccessRequestViewModel
  property_count: 4
  slug: delinea-application-access-request-view-model
- name: BundleSettingsModel
  property_count: 10
  slug: delinea-bundle-settings-model
- name: CharacterSetCreateArgs
  property_count: 1
  slug: delinea-character-set-create-args
- name: CharacterSetModel
  property_count: 7
  slug: delinea-character-set-model
- name: CharacterSetPatchArgs
  property_count: 1
  slug: delinea-character-set-patch-args
- name: ClearLogCollectionResultModel
  property_count: 1
  slug: delinea-clear-log-collection-result-model
- name: CollectLogCollectionResultModel
  property_count: 1
  slug: delinea-collect-log-collection-result-model
- name: ConfigurationAdvancedCreateArgs
  property_count: 2
  slug: delinea-configuration-advanced-create-args
- name: ConfigurationAdvancedModel
  property_count: 3
  slug: delinea-configuration-advanced-model
- name: ConfigurationAdvancedUpdateArgs
  property_count: 2
  slug: delinea-configuration-advanced-update-args
- name: ConfigurationApplicationSettingsModel
  property_count: 30
  slug: delinea-configuration-application-settings-model
- name: ConfigurationLocalUserPasswordsModel
  property_count: 17
  slug: delinea-configuration-local-user-passwords-model
- name: ConfigurationSamlIdentityProviderModel
  property_count: 38
  slug: delinea-configuration-saml-identity-provider-model
- name: ConfigurationSecurityModel
  property_count: 25
  slug: delinea-configuration-security-model
- name: ConfigurationSessionRecordingModel
  property_count: 22
  slug: delinea-configuration-session-recording-model
- name: ConfigurationUserExperienceModel
  property_count: 16
  slug: delinea-configuration-user-experience-model
- name: ConnectionManagerSettingsModel
  property_count: 5
  slug: delinea-connection-manager-settings-model
- name: CreateInitialUserArgs
  property_count: 1
  slug: delinea-create-initial-user-args
- name: CreateInitialUserResponseModel
  property_count: 1
  slug: delinea-create-initial-user-response-model
- name: CustomCommandModel
  property_count: 8
  slug: delinea-custom-command-model
- name: DeletedModel
  property_count: 3
  slug: delinea-deleted-model
- name: DependencyChangerCreateArgs
  property_count: 1
  slug: delinea-dependency-changer-create-args
- name: DependencyChangerModel
  property_count: 14
  slug: delinea-dependency-changer-model
- name: DependencyChangerScanTemplateFieldModel
  property_count: 10
  slug: delinea-dependency-changer-scan-template-field-model
- name: DependencyScriptModel
  property_count: 7
  slug: delinea-dependency-script-model
- name: DevOpsSecretsVaultCreateTenantArgs
  property_count: 1
  slug: delinea-dev-ops-secrets-vault-create-tenant-args
- name: DevOpsSecretsVaultSyncSecretsArgs
  property_count: 1
  slug: delinea-dev-ops-secrets-vault-sync-secrets-args
- name: DevOpsSecretsVaultSyncStatusModel
  property_count: 10
  slug: delinea-dev-ops-secrets-vault-sync-status-model
- name: DevOpsSecretsVaultSyncStatusViewModel
  property_count: 10
  slug: delinea-dev-ops-secrets-vault-sync-status-view-model
- name: DevOpsSecretsVaultTenantModel
  property_count: 8
  slug: delinea-dev-ops-secrets-vault-tenant-model
- name: DevOpsSecretsVaultUpdateTenantArgs
  property_count: 1
  slug: delinea-dev-ops-secrets-vault-update-tenant-args
- name: DiagnosticsSummary
  property_count: 37
  slug: delinea-diagnostics-summary
- name: DisableHideLauncherPasswordForSecretsArgs
  property_count: 1
  slug: delinea-disable-hide-launcher-password-for-secrets-args
- name: DisableRequireViewCommentSecretsArgs
  property_count: 1
  slug: delinea-disable-require-view-comment-secrets-args
- name: DiscoveryNetworkComputerItemDetail
  property_count: 22
  slug: delinea-discovery-network-computer-item-detail
- name: DiscoveryNetworkDirectoryAccountItemDetail
  property_count: 25
  slug: delinea-discovery-network-directory-account-item-detail
- name: DiscoveryNetworkPublicKeyItemDetail
  property_count: 24
  slug: delinea-discovery-network-public-key-item-detail
- name: DiscoveryRuleAccountDetail
  property_count: 39
  slug: delinea-discovery-rule-account-detail
- name: DiscoveryScannerModel
  property_count: 26
  slug: delinea-discovery-scanner-model
- name: DiscoveryStatusModel
  property_count: 14
  slug: delinea-discovery-status-model
- name: DistributedEngineConfigurationModel
  property_count: 16
  slug: delinea-distributed-engine-configuration-model
- name: DomainNameIndexCreateArgs
  property_count: 1
  slug: delinea-domain-name-index-create-args
- name: DomainNameIndexExpireUpdateArgs
  property_count: 1
  slug: delinea-domain-name-index-expire-update-args
- name: DomainNameIndexModel
  property_count: 9
  slug: delinea-domain-name-index-model
- name: DomainNameIndexUpdateArgs
  property_count: 1
  slug: delinea-domain-name-index-update-args
- name: DualControlCreateArgs
  property_count: 4
  slug: delinea-dual-control-create-args
- name: DualControlModel
  property_count: 7
  slug: delinea-dual-control-model
- name: DualControlTypeModel
  property_count: 2
  slug: delinea-dual-control-type-model
- name: DualControlUpdateArgs
  property_count: 5
  slug: delinea-dual-control-update-args
- name: EnableHideLauncherPasswordSecretsArgs
  property_count: 1
  slug: delinea-enable-hide-launcher-password-secrets-args
- name: EnableInheritPermissionsSecretsArgs
  property_count: 1
  slug: delinea-enable-inherit-permissions-secrets-args
- name: EnableRequireViewCommentSecretsArgs
  property_count: 1
  slug: delinea-enable-require-view-comment-secrets-args
- name: EnterpriseSearchRequestArgs
  property_count: 1
  slug: delinea-enterprise-search-request-args
- name: EnterpriseSearchRequestModel
  property_count: 1
  slug: delinea-enterprise-search-request-model
- name: EnterpriseSearchResultModel
  property_count: 3
  slug: delinea-enterprise-search-result-model
- name: EventPipelineFilterSettingMapSummary
  property_count: 8
  slug: delinea-event-pipeline-filter-setting-map-summary
- name: EventPipelineFilterSummary
  property_count: 7
  slug: delinea-event-pipeline-filter-summary
- name: EventPipelineModel
  property_count: 15
  slug: delinea-event-pipeline-model
- name: EventPipelinePolicyMapModel
  property_count: 4
  slug: delinea-event-pipeline-policy-map-model
- name: EventPipelinePolicyMap
  property_count: 4
  slug: delinea-event-pipeline-policy-map
- name: EventPipelinePolicyModel
  property_count: 10
  slug: delinea-event-pipeline-policy-model
- name: EventPipelinePolicyRunActivityViewModel
  property_count: 18
  slug: delinea-event-pipeline-policy-run-activity-view-model
- name: EventPipeline
  property_count: 12
  slug: delinea-event-pipeline
- name: EventPipelineTaskSettingMapSummary
  property_count: 8
  slug: delinea-event-pipeline-task-setting-map-summary
- name: EventPipelineTaskSummary
  property_count: 8
  slug: delinea-event-pipeline-task-summary
- name: EventPipelineTrigger
  property_count: 7
  slug: delinea-event-pipeline-trigger
- name: EventPipelineTriggerSummary
  property_count: 6
  slug: delinea-event-pipeline-trigger-summary
- name: ExportBundleArgs
  property_count: 1
  slug: delinea-export-bundle-args
- name: FolderBasicModel
  property_count: 12
  slug: delinea-folder-basic-model
- name: FolderModel
  property_count: 10
  slug: delinea-folder-model
- name: GroupIpAddressRestrictionModel
  property_count: 5
  slug: delinea-group-ip-address-restriction-model
- name: GroupModel
  property_count: 18
  slug: delinea-group-model
- name: InboxMessageSummary
  property_count: 9
  slug: delinea-inbox-message-summary
- name: InboxResourceUploadArgs
  property_count: 4
  slug: delinea-inbox-resource-upload-args
- name: InboxRuleConditionDetailModel
  property_count: 10
  slug: delinea-inbox-rule-condition-detail-model
- name: InboxRuleConditionSummary
  property_count: 10
  slug: delinea-inbox-rule-condition-summary
- name: InboxRuleDetailModel
  property_count: 15
  slug: delinea-inbox-rule-detail-model
- name: InitialUserSettingsModel
  property_count: 5
  slug: delinea-initial-user-settings-model
- name: JumpboxRouteLevelSummaryModel
  property_count: 4
  slug: delinea-jumpbox-route-level-summary-model
- name: JumpboxRouteModel
  property_count: 5
  slug: delinea-jumpbox-route-model
- name: JumpboxRouteSummaryModel
  property_count: 4
  slug: delinea-jumpbox-route-summary-model
- name: LaunchedSecretModel
  property_count: 8
  slug: delinea-launched-secret-model
- name: LauncherAgentAudit
  property_count: 12
  slug: delinea-launcher-agent-audit
- name: LauncherAgentCollectionAudit
  property_count: 11
  slug: delinea-launcher-agent-collection-audit
- name: LauncherAgentCollectionUpdateArgs
  property_count: 5
  slug: delinea-launcher-agent-collection-update-args
- name: LauncherAgentModel
  property_count: 10
  slug: delinea-launcher-agent-model
- name: LauncherModel
  property_count: 8
  slug: delinea-launcher-model
- name: LauncherTypeModelV2
  property_count: 18
  slug: delinea-launcher-type-model-v2
- name: LogCollectionSummaryModel
  property_count: 2
  slug: delinea-log-collection-summary-model
- name: LongRunningTaskClearResult
  property_count: 1
  slug: delinea-long-running-task-clear-result
- name: LongRunningTaskModel
  property_count: 4
  slug: delinea-long-running-task-model
- name: MetadataFieldSectionSummaryModel
  property_count: 6
  slug: delinea-metadata-field-section-summary-model
- name: MetadataModel
  property_count: 20
  slug: delinea-metadata-model
- name: MobileConfigurationModel
  property_count: 1
  slug: delinea-mobile-configuration-model
- name: NotificationStatusModel
  property_count: 7
  slug: delinea-notification-status-model
- name: OneTimePasswordCodeModel
  property_count: 3
  slug: delinea-one-time-password-code-model
- name: OnlineActivationArgs
  property_count: 3
  slug: delinea-online-activation-args
- name: PagingOfApplicationAccessRequestAuditViewModel
  property_count: 14
  slug: delinea-paging-of-application-access-request-audit-view-model
- name: PagingOfApplicationAccessRequestViewModel
  property_count: 14
  slug: delinea-paging-of-application-access-request-view-model
- name: PagingOfCategorizedListAuditModel
  property_count: 14
  slug: delinea-paging-of-categorized-list-audit-model
- name: PagingOfCategorizedListItemModel
  property_count: 14
  slug: delinea-paging-of-categorized-list-item-model
- name: PagingOfCategorizedListItemViewModel
  property_count: 14
  slug: delinea-paging-of-categorized-list-item-view-model
- name: PagingOfCategorizedListSummary
  property_count: 14
  slug: delinea-paging-of-categorized-list-summary
- name: PagingOfCharacterSetAuditSummary
  property_count: 14
  slug: delinea-paging-of-character-set-audit-summary
- name: PagingOfCharacterSetSummary
  property_count: 14
  slug: delinea-paging-of-character-set-summary
- name: PagingOfConfigurationAdvancedSummary
  property_count: 14
  slug: delinea-paging-of-configuration-advanced-summary
- name: PagingOfCustomCommandModel
  property_count: 14
  slug: delinea-paging-of-custom-command-model
- name: PagingOfDependencyChangerSettingSummaryModel
  property_count: 14
  slug: delinea-paging-of-dependency-changer-setting-summary-model
- name: PagingOfDependencyChangerSummaryModel
  property_count: 14
  slug: delinea-paging-of-dependency-changer-summary-model
- name: PagingOfDevOpsSecretsVaultSyncStatusSummary
  property_count: 14
  slug: delinea-paging-of-dev-ops-secrets-vault-sync-status-summary
- name: PagingOfDevOpsSecretsVaultTenantAuditSummary
  property_count: 14
  slug: delinea-paging-of-dev-ops-secrets-vault-tenant-audit-summary
- name: PagingOfDevOpsSecretsVaultTenantSummary
  property_count: 14
  slug: delinea-paging-of-dev-ops-secrets-vault-tenant-summary
- name: PagingOfDomainNameIndexSummary
  property_count: 14
  slug: delinea-paging-of-domain-name-index-summary
- name: PagingOfDualControlSummary
  property_count: 14
  slug: delinea-paging-of-dual-control-summary
- name: PagingOfEngineAuditSummary
  property_count: 14
  slug: delinea-paging-of-engine-audit-summary
- name: PagingOfEngineSummaryModel
  property_count: 14
  slug: delinea-paging-of-engine-summary-model
- name: PagingOfEventPipelinePolicyAuditSummary
  property_count: 14
  slug: delinea-paging-of-event-pipeline-policy-audit-summary
- name: PagingOfEventPipelinePolicySummary
  property_count: 14
  slug: delinea-paging-of-event-pipeline-policy-summary
- name: PagingOfEventPipelineRunViewModel
  property_count: 14
  slug: delinea-paging-of-event-pipeline-run-view-model
- name: PagingOfEventPipelineSummaryModel
  property_count: 14
  slug: delinea-paging-of-event-pipeline-summary-model
- name: PagingOfEventPipelineTask
  property_count: 14
  slug: delinea-paging-of-event-pipeline-task
- name: PagingOfEventPipelineViewModel
  property_count: 14
  slug: delinea-paging-of-event-pipeline-view-model
- name: PagingOfFolderAuditSummary
  property_count: 14
  slug: delinea-paging-of-folder-audit-summary
- name: PagingOfFolderLookup
  property_count: 14
  slug: delinea-paging-of-folder-lookup
- name: PagingOfFolderSummary
  property_count: 14
  slug: delinea-paging-of-folder-summary
- name: PagingOfGroupIpAddressRestrictionModel
  property_count: 14
  slug: delinea-paging-of-group-ip-address-restriction-model
- name: PagingOfHsmConfigurationAuditViewModel
  property_count: 14
  slug: delinea-paging-of-hsm-configuration-audit-view-model
- name: PagingOfInboxMessageSummary
  property_count: 14
  slug: delinea-paging-of-inbox-message-summary
- name: PagingOfInboxResourceSummary
  property_count: 14
  slug: delinea-paging-of-inbox-resource-summary
- name: PagingOfInboxRuleLogSummary
  property_count: 14
  slug: delinea-paging-of-inbox-rule-log-summary
- name: PagingOfInboxRuleSubscriberSummary
  property_count: 14
  slug: delinea-paging-of-inbox-rule-subscriber-summary
- name: PagingOfInboxRuleSummary
  property_count: 14
  slug: delinea-paging-of-inbox-rule-summary
- name: PagingOfInboxTemplateModel
  property_count: 14
  slug: delinea-paging-of-inbox-template-model
- name: PagingOfIpAddressRestrictionSummary
  property_count: 14
  slug: delinea-paging-of-ip-address-restriction-summary
- name: PagingOfJumpboxRouteAuditModel
  property_count: 14
  slug: delinea-paging-of-jumpbox-route-audit-model
- name: PagingOfJumpboxRouteLevelViewModel
  property_count: 14
  slug: delinea-paging-of-jumpbox-route-level-view-model
- name: PagingOfJumpboxRouteSummaryModel
  property_count: 14
  slug: delinea-paging-of-jumpbox-route-summary-model
- name: PagingOfLauncherAgentCollectionSummary
  property_count: 14
  slug: delinea-paging-of-launcher-agent-collection-summary
- name: PagingOfLauncherAgentSummary
  property_count: 14
  slug: delinea-paging-of-launcher-agent-summary
- name: PagingOfLauncherDetailsV2
  property_count: 14
  slug: delinea-paging-of-launcher-details-v2
- name: PagingOfLauncherLookup
  property_count: 14
  slug: delinea-paging-of-launcher-lookup
- name: PagingOfLauncherSummary
  property_count: 14
  slug: delinea-paging-of-launcher-summary
- name: PagingOfMetadataFieldSectionSummaryModel
  property_count: 14
  slug: delinea-paging-of-metadata-field-section-summary-model
- name: PagingOfMetadataFieldSummaryModel
  property_count: 14
  slug: delinea-paging-of-metadata-field-summary-model
- name: PagingOfMetadataHistorySummaryModel
  property_count: 14
  slug: delinea-paging-of-metadata-history-summary-model
- name: PagingOfMetadataSummaryModel
  property_count: 14
  slug: delinea-paging-of-metadata-summary-model
- name: PagingOfPasswordRequirementAuditModel
  property_count: 14
  slug: delinea-paging-of-password-requirement-audit-model
- name: PagingOfPasswordRequirementsSummary
  property_count: 14
  slug: delinea-paging-of-password-requirements-summary
- name: PagingOfPasswordTypeSummary
  property_count: 14
  slug: delinea-paging-of-password-type-summary
- name: PagingOfPinnedFolderModel
  property_count: 14
  slug: delinea-paging-of-pinned-folder-model
- name: PagingOfPlatformDirectorySummary
  property_count: 14
  slug: delinea-paging-of-platform-directory-summary
- name: PagingOfPlatformUserAndGroupSearchSummary
  property_count: 14
  slug: delinea-paging-of-platform-user-and-group-search-summary
- name: PagingOfProxyAuditModel
  property_count: 14
  slug: delinea-paging-of-proxy-audit-model
- name: PagingOfProxyClientHistorySummaryAndSshProxyClientHistoryFilterQuery
  property_count: 15
  slug: delinea-paging-of-proxy-client-history-summary-and-ssh-proxy-client-history-filter-query
- name: PagingOfProxyClientSummaryAndSshProxyClientsFilterQuery
  property_count: 15
  slug: delinea-paging-of-proxy-client-summary-and-ssh-proxy-clients-filter-query
- name: PagingOfReportAuditSummary
  property_count: 14
  slug: delinea-paging-of-report-audit-summary
- name: PagingOfReportLookup
  property_count: 14
  slug: delinea-paging-of-report-lookup
- name: PagingOfReportSummary
  property_count: 14
  slug: delinea-paging-of-report-summary
- name: PagingOfRoleAuditSummary
  property_count: 14
  slug: delinea-paging-of-role-audit-summary
- name: PagingOfRoleGroupSummaryAndGroupMembershipFilter
  property_count: 15
  slug: delinea-paging-of-role-group-summary-and-group-membership-filter
- name: PagingOfRoleModel
  property_count: 14
  slug: delinea-paging-of-role-model
- name: PagingOfRolePermissionModel
  property_count: 14
  slug: delinea-paging-of-role-permission-model
- name: PagingOfScriptAuditSummary
  property_count: 14
  slug: delinea-paging-of-script-audit-summary
- name: PagingOfScriptCategorySummary
  property_count: 14
  slug: delinea-paging-of-script-category-summary
- name: PagingOfScriptSummaryModel
  property_count: 14
  slug: delinea-paging-of-script-summary-model
- name: PagingOfScriptUsageSummary
  property_count: 14
  slug: delinea-paging-of-script-usage-summary
- name: PagingOfSdkClientAccountSummaryAndSdkClientAccountFilter
  property_count: 15
  slug: delinea-paging-of-sdk-client-account-summary-and-sdk-client-account-filter
- name: PagingOfSdkClientAuditSummaryAndSdkClientAuditFilter
  property_count: 15
  slug: delinea-paging-of-sdk-client-audit-summary-and-sdk-client-audit-filter
- name: PagingOfSdkClientRuleSummaryAndSdkClientRuleFilter
  property_count: 15
  slug: delinea-paging-of-sdk-client-rule-summary-and-sdk-client-rule-filter
- name: PagingOfSecretAccessModel
  property_count: 14
  slug: delinea-paging-of-secret-access-model
- name: PagingOfSecretAccessRequestHistoryModel
  property_count: 14
  slug: delinea-paging-of-secret-access-request-history-model
- name: PagingOfSecretPolicyViewModel
  property_count: 14
  slug: delinea-paging-of-secret-policy-view-model
- name: PagingOfSimpleCategorizedList
  property_count: 14
  slug: delinea-paging-of-simple-categorized-list
- name: PagingOfSiteConnectorSummaryModel
  property_count: 14
  slug: delinea-paging-of-site-connector-summary-model
- name: PagingOfSiteLogSummaryModel
  property_count: 14
  slug: delinea-paging-of-site-log-summary-model
- name: PagingOfString
  property_count: 14
  slug: delinea-paging-of-string
- name: PagingOfSystemLogSummaryModel
  property_count: 14
  slug: delinea-paging-of-system-log-summary-model
- name: PagingOfUserIpAddressRestrictionModel
  property_count: 14
  slug: delinea-paging-of-user-ip-address-restriction-model
- name: PagingOfUserLookup
  property_count: 14
  slug: delinea-paging-of-user-lookup
- name: PasswordRequirementCreateArgs
  property_count: 1
  slug: delinea-password-requirement-create-args
- name: PasswordRequirementModel
  property_count: 15
  slug: delinea-password-requirement-model
- name: PasswordRequirementPatchArgs
  property_count: 1
  slug: delinea-password-requirement-patch-args
- name: PasswordRequirementRuleUpdateArgs
  property_count: 1
  slug: delinea-password-requirement-rule-update-args
- name: PasswordTypeCreateArgs
  property_count: 5
  slug: delinea-password-type-create-args
- name: PasswordTypeModel
  property_count: 34
  slug: delinea-password-type-model
- name: PasswordTypeUpdateArgs
  property_count: 22
  slug: delinea-password-type-update-args
- name: PbaConfigurationModel
  property_count: 25
  slug: delinea-pba-configuration-model
- name: PbaConfirmPairModel
  property_count: 2
  slug: delinea-pba-confirm-pair-model
- name: PbaHistoricalImportArgs
  property_count: 3
  slug: delinea-pba-historical-import-args
- name: PbaHistoricalImportStatusResponseMessage
  property_count: 2
  slug: delinea-pba-historical-import-status-response-message
- name: PbaHistoricalImportViewModel
  property_count: 2
  slug: delinea-pba-historical-import-view-model
- name: PlatformProvisionStatus
  property_count: 3
  slug: delinea-platform-provision-status
- name: PlatformSynchronizationStatus
  property_count: 8
  slug: delinea-platform-synchronization-status
- name: ProvisionPlatformRequestArgs
  property_count: 5
  slug: delinea-provision-platform-request-args
- name: ProxySiteViewModel
  property_count: 9
  slug: delinea-proxy-site-view-model
- name: QuartzTrigger
  property_count: 6
  slug: delinea-quartz-trigger
- name: RdpProxyConfigurationViewModel
  property_count: 10
  slug: delinea-rdp-proxy-configuration-view-model
- name: RecurringScheduleCreateArgs
  property_count: 1
  slug: delinea-recurring-schedule-create-args
- name: RecurringScheduleModel
  property_count: 9
  slug: delinea-recurring-schedule-model
- name: RecurringScheduleUpdateArgs
  property_count: 1
  slug: delinea-recurring-schedule-update-args
- name: RecycleBackgroundProcessesResultModel
  property_count: 1
  slug: delinea-recycle-background-processes-result-model
- name: RegexValuesSummary
  property_count: 1
  slug: delinea-regex-values-summary
- name: ReportExecuteArgs
  property_count: 14
  slug: delinea-report-execute-args
- name: ReportExportArgs
  property_count: 17
  slug: delinea-report-export-args
- name: ReportScheduleModel
  property_count: 14
  slug: delinea-report-schedule-model
- name: RestApiDocSummary
  property_count: 3
  slug: delinea-rest-api-doc-summary
- name: RoleCreateArgs
  property_count: 2
  slug: delinea-role-create-args
- name: RoleModel
  property_count: 5
  slug: delinea-role-model
- name: RolePermissionsAssignmentRequest
  property_count: 1
  slug: delinea-role-permissions-assignment-request
- name: ScriptModelV2
  property_count: 11
  slug: delinea-script-model-v2
- name: SdkClientAccountCreateArgs
  property_count: 5
  slug: delinea-sdk-client-account-create-args
- name: SdkClientAccountModel
  property_count: 8
  slug: delinea-sdk-client-account-model
- name: SdkClientAccountUpdateArgs
  property_count: 2
  slug: delinea-sdk-client-account-update-args
- name: SdkClientRuleCreateArgs
  property_count: 4
  slug: delinea-sdk-client-rule-create-args
- name: SdkClientRuleModel
  property_count: 6
  slug: delinea-sdk-client-rule-model
- name: SdkClientRuleUpdateArgs
  property_count: 4
  slug: delinea-sdk-client-rule-update-args
- name: SecretAccessActionResultModel
  property_count: 23
  slug: delinea-secret-access-action-result-model
- name: SecretAccessModel
  property_count: 22
  slug: delinea-secret-access-model
- name: SecretAccessOptionsModel
  property_count: 10
  slug: delinea-secret-access-options-model
- name: SecretAccessPendingRequestModel
  property_count: 24
  slug: delinea-secret-access-pending-request-model
- name: SecretDependencyCreateArgs
  property_count: 17
  slug: delinea-secret-dependency-create-args
- name: SecretDependencyModel
  property_count: 20
  slug: delinea-secret-dependency-model
- name: SecretDependencyUpdateArgs
  property_count: 18
  slug: delinea-secret-dependency-update-args
- name: SiteBasicModel
  property_count: 18
  slug: delinea-site-basic-model
- name: SshProxyConfigurationViewModel
  property_count: 25
  slug: delinea-ssh-proxy-configuration-view-model
- name: TestIntegrationResponse
  property_count: 4
  slug: delinea-test-integration-response
- name: TestRemoteScriptPsResponseModel
  property_count: 5
  slug: delinea-test-remote-script-ps-response-model
- name: ThreadInformation
  property_count: 6
  slug: delinea-thread-information
- name: UpdatePasswordRequirementForSecretsArgs
  property_count: 1
  slug: delinea-update-password-requirement-for-secrets-args
- name: UserIpAddressRestrictionModel
  property_count: 6
  slug: delinea-user-ip-address-restriction-model
- name: ValidLicenseModel
  property_count: 3
  slug: delinea-valid-license-model
- name: FolderCreateArgs
  property_count: 6
  slug: foldercreateargs
- name: FolderModel
  property_count: 10
  slug: foldermodel
- name: FolderUpdateArgs
  property_count: 7
  slug: folderupdateargs
- name: GroupCreateArgs
  property_count: 12
  slug: groupcreateargs
- name: GroupModel
  property_count: 18
  slug: groupmodel
- name: RoleCreateArgs
  property_count: 2
  slug: rolecreateargs
- name: RoleModel
  property_count: 5
  slug: rolemodel
- name: SecretCreateArgs
  property_count: 21
  slug: secretcreateargs
- name: SecretModel
  property_count: 41
  slug: secretmodel
- name: SecretPolicyModel
  property_count: 4
  slug: secretpolicymodel
- name: SecretSummary
  property_count: 29
  slug: secretsummary
- name: SecretUpdateArgs
  property_count: 30
  slug: secretupdateargs
- name: UserCreateArgs
  property_count: 15
  slug: usercreateargs
- name: UserModel
  property_count: 39
  slug: usermodel
- name: UserUpdateArgs
  property_count: 19
  slug: userupdateargs
jsonld:
- class_count: 25
  name: Delinea Context
  property_count: 7
  slug: delinea-context
- class_count: 0
  name: Delinea Graph Context
  property_count: 0
  slug: delinea-graph
layout: provider
modified: '2026-06-13'
name: Delinea
nav: Providers
network: true
overview: 'Delinea publishes 102 API contracts indexed on the [APIs.io](https://apis.io/) network, including Activations API, AdvancedConfigSettings API, AppClients API, and 99 more. Tagged areas include Privileged Access Management, Secrets Management, Identity Security, DevOps, and Cybersecurity.


  The Delinea catalog on APIs.io includes 1 event-driven AsyncAPI specification, 2 JSON-LD contexts, and 2 Spectral governance rulesets.


  Delinea''s developer surface includes support, changelog, API reference, getting-started guide, authentication, documentation, engineering blog, and 39 more developer resources.'
plans:
- name: Delinea Plans Pricing
  plan_count: 3
  slug: delinea-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 3
  name: Delinea Rate Limits
  slug: delinea-rate-limits
rules:
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: Delinea — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: delinea-jsonschema-spectral-rules
- authorship: generated
  effective_rule_count: 56
  extends:
  - spectral:oas
  name: Delinea API Rules
  rule_count: 15
  severity_counts:
    error: 13
    hint: 0
    info: 1
    warn: 1
  slug: delinea-rules
score:
  band: strong
  composite: 63.0
  coverage:
    artifact_dirs: 31
    catalog_earned: 74.8
    catalog_earned_first_party: 12.0
    catalog_gap: 40.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.8
  facets:
    access_clarity: 68.4
    contract_governance: 22.0
    contract_quality: 70.7
    developer_ergonomics: 55.4
    discoverability: 75.0
    operational_transparency: 50.0
  previous_composite: 69.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 99
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 31.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 22.2
screenshot: https://apis.io/screenshots/delinea/delinea-2026-06-20T175854.png
security:
- kind: authentication
  name: Delinea Authentication
  slug: delinea-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Delinea Domain Security
  slug: delinea-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Delinea Vulnerability Disclosure
  slug: delinea-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Delinea Trust Center
  slug: delinea-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, GDPR
skill_count: 4
skills:
- name: delinea-create-and-get-sdk-client-account
  slug: delinea-create-and-get-sdk-client-account
- name: delinea-create-and-retrieve-workflow-template
  slug: delinea-create-and-retrieve-workflow-template
- name: delinea-event-subscriptions-create
  slug: delinea-event-subscriptions-create
- name: delinea-workflow-step-create-and-retrieve
  slug: delinea-workflow-step-create-and-retrieve
slug: delinea
tags:
- Privileged Access Management
- Secrets Management
- Identity Security
- DevOps
- Cybersecurity
website: https://delinea.com/
---
