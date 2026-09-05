---
access_model:
  confidence: medium
  label: Paid (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: true
  try_now: true
agent_readiness:
  band: agent-ready
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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 31.1
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 524
  human_in_the_loop: 28
  name: Delinea Agentic Access
  operation_count: 1037
  slug: delinea-agentic-access
  summary_line: 1037 operations · 524 acting · 28 human-in-the-loop
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
  description: View and maintain Active Directory
  name: Delinea ActiveDirectory API
  slug: delinea-activedirectory-api
- baseURL: https://your-secret-server-instance/api/v1
  baseurl_source: declared
  description: AdvancedConfigSettingsController
  name: Delinea AdvancedConfigSettings API
  slug: delinea-advancedconfigsettings-api
- baseURL: https://your-secret-server-instance/api/v1
  baseurl_source: declared
  description: API Token Generation
  name: Delinea ApiToken API
  slug: delinea-apitoken-api
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
  description: View Bulk Operations
  name: Delinea BulkOperations API
  slug: delinea-bulkoperations-api
- baseURL: https://your-secret-server-instance/api/v1
  baseurl_source: declared
  description: Create Bulk Secret Operations
  name: Delinea BulkSecretOperations API
  slug: delinea-bulksecretoperations-api
- baseURL: https://your-secret-server-instance/api/v1
  baseurl_source: declared
  description: Create Bulk User Operations
  name: Delinea BulkUserOperations API
  slug: delinea-bulkuseroperations-api
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
  description: View and maintain Directory Services integrations
  name: Delinea DirectoryServices API
  slug: delinea-directoryservices-api
- baseURL: https://your-secret-server-instance/api/v1
  baseurl_source: declared
  description: Disaster Recovery
  name: Delinea DisasterRecovery API
  slug: delinea-disasterrecovery-api
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
  description: EventSubscriptionsController
  name: Delinea EventSubscriptions API
  slug: delinea-eventsubscriptions-api
- baseURL: https://your-secret-server-instance/api/v1
  baseurl_source: declared
  description: Extended Fields provider
  name: Delinea ExtendedFields API
  slug: delinea-extendedfields-api
- baseURL: https://your-secret-server-instance/api/v1
  baseurl_source: declared
  description: FeatureFlagController
  name: Delinea FeatureFlag API
  slug: delinea-featureflag-api
- baseURL: https://your-secret-server-instance/api/v1
  baseurl_source: declared
  description: View and maintain secret folder permissions
  name: Delinea FolderPermissions API
  slug: delinea-folderpermissions-api
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
  description: HealthCheckController
  name: Delinea HealthCheck API
  slug: delinea-healthcheck-api
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
  description: View and configure Key Management settings
  name: Delinea KeyManagement API
  slug: delinea-keymanagement-api
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
  description: RolePermissionsController
  name: Delinea RolePermissions API
  slug: delinea-rolepermissions-api
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
  description: TicketSystemsController
  name: Delinea TicketSystems API
  slug: delinea-ticketsystems-api
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
  description: View and maintain Workflow Instances
  name: Delinea WorkflowInstances API
  slug: delinea-workflowinstances-api
- baseURL: https://your-secret-server-instance/api/v1
  baseurl_source: declared
  description: View and maintain Workflow Template Steps
  name: Delinea WorkflowStepTemplates API
  slug: delinea-workflowsteptemplates-api
- baseURL: https://your-secret-server-instance/api/v1
  baseurl_source: declared
  description: View and maintain Workflow Templates
  name: Delinea WorkflowTemplates API
  slug: delinea-workflowtemplates-api
artifact_total: 241
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
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
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/delinea-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/delinea-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/delinea-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/delinea-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/delinea-domain-security.yml
- group: auth
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
  title: ''
  type: Plans
  url: plans/delinea-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/delinea-rate-limits.yml
- group: commercial
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
- name: Delinea Finops
  service_category: ''
  slug: delinea-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/delinea.png
json_schemas:
- name: AuthenticationFailedResponse
  property_count: 1
  slug: authenticationfailedresponse
- name: BadRequestResponse
  property_count: 4
  slug: badrequestresponse
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
overview: 'Delinea publishes 99 APIs on the [APIs.io](https://apis.io/) network, including Activations API, ActiveDirectory API, AdvancedConfigSettings API, and 96 more. Tagged areas include Privileged Access Management, PAM, Secrets Management, Identity Security, and DevOps.


  The Delinea catalog on APIs.io includes 2 JSON-LD contexts and 1 Spectral governance ruleset.


  Delinea''s developer surface includes authentication, documentation, engineering blog, pricing, and 13 more developer resources.'
plans:
- name: Delinea Plans Pricing
  plan_count: 4
  slug: delinea-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 3
  name: Delinea Rate Limits
  slug: delinea-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Delinea API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: delinea-jsonschema-spectral-rules
score:
  band: developing
  composite: 49.5
  coverage:
    artifact_dirs: 16
    catalog_earned: 72.3
    catalog_earned_first_party: 0.0
    catalog_gap: 42.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 57.9
    commercial_clarity: 57.9
    contract_governance: 9.8
    contract_quality: 64.0
    developer_ergonomics: 38.1
    discoverability: 63.0
    governance: 9.8
    operational_transparency: 52.6
  previous_composite: 49.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 99
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/delinea/refs/heads/main/screenshots/delinea-2026-06-20T175854.png
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
slug: delinea
tags:
- Privileged Access Management
- PAM
- Secrets Management
- Identity Security
- DevOps
- Cybersecurity
website: https://delinea.com/
---
