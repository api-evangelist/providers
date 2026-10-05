---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
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
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 33.3
  scored_at: '2026-10-04'
agentic_access:
- acting_count: 56
  human_in_the_loop: 3
  name: Outsystems Agentic Access
  operation_count: 150
  slug: outsystems-agentic-access
  summary_line: 150 operations · 56 acting · 3 human-in-the-loop
api_count: 14
apis:
- description: Official OutSystems remote Model Context Protocol server (early alpha), exposed per tenant over streamable HTTP with OAuth Dynamic Client Registration. Tool domains cover Apps, the read-only Context S
  name: OutSystems Remote MCP Server
  slug: remote-mcp
- baseURL: https://{odc-portal-domain}/api/identity/v1
  baseurl_source: declared
  description: The Analysis Status API from OutSystems — 1 operation(s) for analysis status.
  name: OutSystems Analysis Status API
  phrasing_intents:
  - id: SyncControllerV_GetAnalysisStatus
    intent: Check Code Quality data sync status
    question: Is my OutSystems Code Quality data up to date with the latest analysis?
  phrasing_ops: 1
  slug: outsystems-analysis-status-api
- baseURL: https://{odc-portal-domain}/api/identity/v1
  baseurl_source: declared
  description: The application-roles API from OutSystems — 2 operation(s) for application-roles.
  name: OutSystems Application Roles API
  phrasing_intents:
  - id: ApplicationRole_QueryApplicationRoles
    intent: List application roles
    question: Which application roles exist across my ODC apps?
  - id: ApplicationRole_QueryUsersByApplicationRole
    intent: List users holding an application role
    question: Who are the end users assigned a particular application role?
  phrasing_ops: 2
  slug: outsystems-application-roles-api
- baseURL: https://{odc-portal-domain}/api/identity/v1
  baseurl_source: declared
  description: The Assets API from OutSystems — 19 operation(s) for assets.
  name: OutSystems Assets API
  phrasing_intents:
  - id: AssetRepository_CreateAssetRevision
    intent: Create an asset or a new asset revision
    question: How do I upload an OML or XIF file as a new revision of an app?
  - id: AssetRepository_ListAssets
    intent: List assets in the repository
    question: What apps, libraries and agents are in my ODC asset repository?
  - id: AssetRepository_DeleteAsset
    intent: Delete an asset permanently
    question: Can I permanently delete an app and all of its runtime data?
  - id: AssetRepository_GetAsset
    intent: Get an asset's details
    question: How do I look up a single asset's details by its key?
  - id: AssetRepository_GetApplicationHighestTagRevision
    intent: Get an asset's highest-tagged revision
    question: Which revision of my app carries the highest version tag?
  - id: AssetRepository_GetAssetLatestRevision
    intent: Get an asset's latest revision
    question: What is the newest revision saved for an asset, tagged or not?
  - id: AssetRepository_GetAssetRevision
    intent: Get a specific asset revision
    question: How do I retrieve one exact numbered revision of an asset?
  - id: AssetRepository_PatchVersion
    intent: Tag a revision or edit its release notes
    question: How do I set a version tag on an existing asset revision?
  phrasing_ops: 22
  slug: outsystems-assets-api
- baseURL: https://{odc-portal-domain}/api/identity/v1
  baseurl_source: declared
  description: The Assets Quality Metrics API from OutSystems — 1 operation(s) for assets quality metrics.
  name: OutSystems Assets Quality Metrics API
  phrasing_intents:
  - id: FindingsOverviewControllerV_GetAppsOverview
    intent: Get code quality metrics per asset
    question: Which of my apps have the lowest code quality scores?
  phrasing_ops: 1
  slug: outsystems-assets-quality-metrics-api
- baseURL: https://{odc-portal-domain}/api/identity/v1
  baseurl_source: declared
  description: The Build API from OutSystems — 4 operation(s) for build.
  name: OutSystems Build API
  phrasing_intents:
  - id: BuildV_GetBuild
    intent: Get details of an asset build
    question: How do I check the outcome of a build I started for an asset revision?
  - id: BuildV_GetBuildFeedback
    intent: Read an asset build's log messages
    question: Why did my asset build fail, according to its log?
  - id: BuildV_GetSourceCode
    intent: Download a build's packaged generated code
    question: Where do I get the generated code once its packaging has finished?
  - id: BuildV_StartSourceCodeProcess
    intent: Start packaging a build's generated code
    question: How do I ask ODC to package the generated code of a build so I can download it?
  - id: BuildV_ListBuilds
    intent: List builds for an asset revision
    question: What builds have been created for a given revision of my asset?
  - id: BuildV_StartNewBuildJob
    intent: Start a build of an asset revision
    question: How do I trigger a Release build for a particular revision of an asset?
  phrasing_ops: 6
  slug: outsystems-build-api
- baseURL: https://{odc-portal-domain}/api/identity/v1
  baseurl_source: declared
  description: The BuildOperations API from OutSystems — 5 operation(s) for buildoperations.
  name: OutSystems Build Operations API
  phrasing_intents:
  - id: GET_BuildOperations_Get
    intent: Get a native mobile build's details
    question: How do I check the status of a native mobile build I started?
  - id: GET_BuildOperations_GetMessages
    intent: Read progress messages of a native build
    question: Can I follow step-by-step progress of my native mobile build?
  - id: GET_BuildOperations_List
    intent: List native mobile builds
    question: Which native mobile builds have run for my app?
  - id: POST_BuildOperations_Post
    intent: Start a native mobile build
    question: How do I kick off a new iOS or Android build of my mobile app?
  - id: POST_BuildOperations_PostVersionSuggestions
    intent: Suggest the next mobile build version
    question: What version number and version code should my next mobile build use?
  - id: POST_BuildOperations_ValidateNativeBuild
    intent: Check whether a new native build is needed
    question: Are my iOS and Android build artifacts still up to date, or do I need to rebuild?
  phrasing_ops: 6
  slug: outsystems-buildoperations-api
- baseURL: https://{odc-portal-domain}/api/identity/v1
  baseurl_source: declared
  description: The Code Analyses API from OutSystems — 2 operation(s) for code analyses.
  name: OutSystems Code Analyses API
  phrasing_intents:
  - id: CodeAnalysisControllerV_GetAnalysisRequestStatus
    intent: Get the result of a code analysis request
    question: Has the code analysis I submitted finished, and what score did it get?
  - id: CodeAnalysisControllerV_SubmitCodeAnalysisRequest
    intent: Run a code analysis on an asset revision
    question: How do I request a code quality scan of one revision of my app?
  phrasing_ops: 2
  slug: outsystems-code-analyses-api
- baseURL: https://{odc-portal-domain}/api/identity/v1
  baseurl_source: declared
  description: The Deletion Analyses API from OutSystems — 2 operation(s) for deletion analyses.
  name: OutSystems Deletion Analyses API
  phrasing_intents:
  - id: DeletionAnalysis_GetResult
    intent: Get a deletion impact report
    question: What would break if I deleted this asset, according to the finished analysis?
  - id: DeletionAnalysis_LaunchDeletionAnalysis
    intent: Analyze the impact of deleting an asset
    question: Before deleting an app, can I check what impact removing it would have?
  phrasing_ops: 2
  slug: outsystems-deletion-analyses-api
- baseURL: https://{odc-portal-domain}/api/identity/v1
  baseurl_source: declared
  description: The deployed-assets API from OutSystems — 1 operation(s) for deployed-assets.
  name: OutSystems Deployed Assets API
  phrasing_intents:
  - id: DeployedAssets_ListAssets
    intent: List deployed assets and their URLs
    question: Which assets are deployed to each stage, and what URLs do they run at?
  phrasing_ops: 1
  slug: outsystems-deployed-assets-api
- baseURL: https://{odc-portal-domain}/api/identity/v1
  baseurl_source: declared
  description: The Deployment Analyses API from OutSystems — 2 operation(s) for deployment analyses.
  name: OutSystems Deployment Analyses API
  phrasing_intents:
  - id: DeploymentAnalysis_GetResult
    intent: Get a deployment impact report
    question: Is the deployment analysis finished, and what impacts did it find?
  - id: DeploymentAnalysis_LaunchDeploymentAnalysis
    intent: Analyze the impact of promoting an asset
    question: Before promoting an app to another stage, can I check the impact on its consumers?
  phrasing_ops: 2
  slug: outsystems-deployment-analyses-api
- baseURL: https://{odc-portal-domain}/api/identity/v1
  baseurl_source: declared
  description: The deployment-operations API from OutSystems — 3 operation(s) for deployment-operations.
  name: OutSystems Deployment Operations API
  phrasing_intents:
  - id: DeploymentOperations_Filter
    intent: List deployments
    question: Which deployments ran in a given stage recently?
  - id: DeploymentOperations_Post
    intent: Deploy, undeploy or apply configs
    question: How do I deploy an app revision to a stage through the API?
  - id: DeploymentOperations_Get
    intent: Get one deployment
    question: How do I check the status of a single deployment by its key?
  - id: DeploymentOperations_GetMessages
    intent: Read a deployment's log messages
    question: Why did my deployment fail, according to its log?
  phrasing_ops: 4
  slug: outsystems-deployment-operations-api
- baseURL: https://{odc-portal-domain}/api/identity/v1
  baseurl_source: declared
  description: Manage custom domains for environments.
  name: OutSystems Domains API
  phrasing_intents:
  - id: Domains_Delete
    intent: Remove a custom domain from a stage
    question: Can I remove a custom domain I no longer use from a stage?
  - id: Domains_Get
    intent: Get one custom domain of a stage
    question: How do I look up the details of one custom domain configured in a stage?
  - id: Domains_Patch
    intent: Set the default app for a custom domain
    question: How do I change which app a custom domain opens by default?
  - id: getEnvironmentsByEnvironmentKeyDomains
    intent: List custom domains in a stage
    question: What custom domains are configured for my production stage?
  - id: Domains_Post
    intent: Add a custom domain to a stage
    question: How do I add my own hostname as a custom domain in an ODC stage?
  - id: EnvironmentConfigurations_Get
    intent: Get a stage's default domain
    question: Which domain is set as the default for a given stage?
  - id: EnvironmentConfigurations_Patch
    intent: Change a stage's default domain
    question: Can I switch the default domain of a stage to one of my custom domains?
  phrasing_ops: 7
  slug: outsystems-domains-api
- baseURL: https://{odc-portal-domain}/api/identity/v1
  baseurl_source: declared
  description: The Environments API from OutSystems — 12 operation(s) for environments.
  name: OutSystems Environments API
  phrasing_intents:
  - id: AssetConfiguration_GetAgentDeployedConfiguration
    intent: Get a deployed agent's configurations
    question: What settings and timers is my deployed agent currently running with?
  - id: AssetConfiguration_GetAgentRevisionConfiguration
    intent: Get configurations of an agent revision
    question: How do I see the configurations for a specific revision of an agent, not the deployed one?
  - id: AssetConfiguration_GetApplicationDeployedConfiguration
    intent: Get a deployed app's configurations
    question: What site settings and integrations is my deployed app using in a stage?
  - id: AssetConfiguration_GetApplicationRevisionConfiguration
    intent: Get configurations of an app revision
    question: How do I see an app's configurations for a revision that isn't deployed yet?
  - id: AssetConfiguration_PatchAgent
    intent: Update an agent's configurations
    question: How do I change settings or timers for an agent in a stage?
  - id: AssetConfiguration_PatchApplication
    intent: Update an app's configurations
    question: How do I change an app's settings or integration endpoints in one stage?
  - id: EnvironmentConfiguration_Get
    intent: Get a stage's default system configurations
    question: What default system configurations apply to every app in a stage?
  - id: EnvironmentConfiguration_Patch
    intent: Update a stage's default system configurations
    question: How do I change the default system configurations for a whole stage?
  phrasing_ops: 14
  slug: outsystems-environments-api
- baseURL: https://{odc-portal-domain}/api/identity/v1
  baseurl_source: declared
  description: The Findings API from OutSystems — 1 operation(s) for findings.
  name: OutSystems Findings API
  phrasing_intents:
  - id: FindingsControllerV_GetFindings
    intent: List code quality findings
    question: What code quality findings does OutSystems report for my apps?
  phrasing_ops: 1
  slug: outsystems-findings-api
- baseURL: https://{odc-portal-domain}/api/identity/v1
  baseurl_source: declared
  description: The Findings Summary API from OutSystems — 1 operation(s) for findings summary.
  name: OutSystems Findings Summary API
  phrasing_intents:
  - id: FindingsOverviewControllerV_GetFindingsSummary
    intent: Summarize findings by category or severity
    question: How many code quality findings do I have in each category?
  phrasing_ops: 1
  slug: outsystems-findings-summary-api
- baseURL: https://{odc-portal-domain}/api/identity/v1
  baseurl_source: declared
  description: The Findings Trend API from OutSystems — 1 operation(s) for findings trend.
  name: OutSystems Findings Trend API
  phrasing_intents:
  - id: FindingsOverviewControllerV_GetFindingsTrend
    intent: Show the trend of findings over time
    question: How has my code quality score changed across analyses over time?
  phrasing_ops: 1
  slug: outsystems-findings-trend-api
- baseURL: https://{odc-portal-domain}/api/identity/v1
  baseurl_source: declared
  description: The GenerationOperations API from OutSystems — 4 operation(s) for generationoperations.
  name: OutSystems Generation Operations API
  phrasing_intents:
  - id: GenerationOperations_CreateGenerationOperation
    intent: Generate an external library from code
    question: How do I turn a high-code package into an external library?
  - id: GenerationOperations_GetGenerationOperations
    intent: List external library generation operations
    question: Which external library generation operations have run in my tenant?
  - id: GenerationOperations_DeleteGenerationOperationByOperationKey
    intent: Delete a library generation operation
    question: Can I delete a generation operation along with its logs?
  - id: GenerationOperations_GetGenerationOperationByOperationKey
    intent: Get a library generation's details
    question: Has my external library generation finished?
  - id: GenerationOperations_GetGenerationOperationContents
    intent: List actions and structures in a generation
    question: Which actions and structures were found in my high-code package?
  - id: GenerationOperations_GetGenerationOperationLogMessages
    intent: Read validation messages of a generation
    question: Why did my external library generation fail validation?
  phrasing_ops: 6
  slug: outsystems-generationoperations-api
- baseURL: https://{odc-portal-domain}/api/identity/v1
  baseurl_source: declared
  description: The groups API from OutSystems — 5 operation(s) for groups.
  name: OutSystems Groups API
  phrasing_intents:
  - id: Group_AddOrRemoveUsersFromGroup
    intent: Add or remove group members
    question: How do I add several users to a group in one request?
  - id: Group_QueryUsersFromGroup
    intent: List members of a group
    question: Who belongs to a given end-user group?
  - id: Group_CreateGroup
    intent: Create an end-user group
    question: How do I create a new group of end users in a stage?
  - id: Group_QueryGroups
    intent: List end-user groups
    question: What end-user groups exist in my ODC organization?
  - id: Group_DeleteGroup
    intent: Delete a group
    question: Can I delete an end-user group I no longer need?
  - id: Group_ReadGroup
    intent: Get a group's details
    question: What's the name, description and stage of a particular group?
  - id: Group_UpdateGroup
    intent: Rename or redescribe a group
    question: How do I rename an existing group?
  - id: Group_ModifyGroupApplicationRoles
    intent: Add or remove a group's application roles
    question: How do I give a whole group a new application role?
  phrasing_ops: 10
  slug: outsystems-groups-api
- baseURL: https://{odc-portal-domain}/api/identity/v1
  baseurl_source: declared
  description: The identity-providers API from OutSystems — 2 operation(s) for identity-providers.
  name: OutSystems Identity Providers API
  phrasing_intents:
  - id: IdentityProvider_QueryIdentityProviders
    intent: List identity providers
    question: Which identity providers are configured for my ODC organization?
  - id: IdentityProvider_ReadIdentityProvider
    intent: Get an identity provider
    question: How do I see the details of one identity provider?
  phrasing_ops: 2
  slug: outsystems-identity-providers-api
- baseURL: https://{odc-portal-domain}/api/identity/v1
  baseurl_source: declared
  description: Create, update, and delete IP filter groups and rules.
  name: OutSystems IP filters API
  phrasing_intents:
  - id: IpFilterGroups_Delete
    intent: Delete an IP filter group
    question: Can I remove an IP filter group from a stage?
  - id: IpFilterGroups_Get
    intent: Get one IP filter group
    question: What IP rules are in a specific IP filter group?
  - id: IpFilterGroups_Patch
    intent: Update an IP filter group
    question: How do I add new IP ranges to an existing IP filter group?
  - id: IpFilterGroups_List
    intent: List IP filter groups in a stage
    question: What IP filter groups restrict access in my stage?
  - id: IpFilterGroups_Post
    intent: Create an IP filter group
    question: How do I restrict app access to certain IP addresses in a stage?
  phrasing_ops: 5
  slug: outsystems-ip-filters-api
- baseURL: https://{odc-portal-domain}/api/identity/v1
  baseurl_source: declared
  description: The Libraries API from OutSystems — 1 operation(s) for libraries.
  name: OutSystems Libraries API
  phrasing_intents:
  - id: Libraries_ListLibraries
    intent: List libraries in the portfolio
    question: What libraries are available in my ODC tenant?
  phrasing_ops: 1
  slug: outsystems-libraries-api
- baseURL: https://{odc-portal-domain}/api/identity/v1
  baseurl_source: declared
  description: The NativeBuilderVersions API from OutSystems — 1 operation(s) for nativebuilderversions.
  name: OutSystems Native Builder Versions API
  phrasing_intents:
  - id: GET_NativeBuilderVersions_List
    intent: List native builder versions
    question: Which native builder versions can I choose for mobile builds?
  phrasing_ops: 1
  slug: outsystems-nativebuilderversions-api
- baseURL: https://{odc-portal-domain}/api/identity/v1
  baseurl_source: declared
  description: The NativeBuildExtensibilitySettings API from OutSystems — 1 operation(s) for nativebuildextensibilitysettings.
  name: OutSystems Native Build Extensibility Settings API
  phrasing_intents:
  - id: GET_NativeBuildExtensibilitySettings_Get
    intent: Get an app's native extensibility settings
    question: What native build extensibility settings does my mobile app use?
  - id: PATCH_NativeBuildExtensibilitySettings_Patch
    intent: Update an app's native extensibility settings
    question: How do I change the native build extensibility settings of an app?
  phrasing_ops: 2
  slug: outsystems-nativebuildextensibilitysettings-api
- baseURL: https://{odc-portal-domain}/api/identity/v1
  baseurl_source: declared
  description: The NativeMobileConfigurations API from OutSystems — 2 operation(s) for nativemobileconfigurations.
  name: OutSystems Native Mobile Configurations API
  phrasing_intents:
  - id: GET_NativeBuildConfigurations_GetAndroidMobileConfiguration
    intent: Get an app's Android native configuration
    question: What keystore and Android settings are deployed for my mobile app?
  - id: PATCH_NativeBuildConfigurations_UpdateMobileAndroidConfiguration
    intent: Update an app's Android native configuration
    question: How do I upload a new Android keystore for my mobile app?
  - id: GET_NativeBuildConfigurations_GetIosMobileConfiguration
    intent: Get an app's iOS native configuration
    question: What certificates and provisioning profiles are deployed for my iOS app?
  - id: PATCH_NativeBuildConfigurations_UpdateMobileIosConfiguration
    intent: Update an app's iOS native configuration
    question: How do I replace an expiring iOS certificate for my mobile app?
  phrasing_ops: 4
  slug: outsystems-nativemobileconfigurations-api
- baseURL: https://{odc-portal-domain}/api/identity/v1
  baseurl_source: declared
  description: The Organization API from OutSystems — 3 operation(s) for organization.
  name: OutSystems Organization API
  phrasing_intents:
  - id: Subscription_GetOrganizationConfigurations
    intent: Get organization configurations
    question: What organization-level settings are configured in ODC?
  - id: Subscription_PatchOrganizationConfigurations
    intent: Update organization email domain settings
    question: How do I mark certain email domains as internal to my organization?
  - id: Subscription_GetOrganizationEntitlements
    intent: Get the organization's entitlements
    question: What does my OutSystems subscription entitle my whole organization to?
  - id: Subscription_GetOrganizationUsage
    intent: Get organization-wide entitlement usage
    question: How much of our entitlements has the organization used this month?
  phrasing_ops: 4
  slug: outsystems-organization-api
- baseURL: https://{odc-portal-domain}/api/identity/v1
  baseurl_source: declared
  description: The organization-roles API from OutSystems — 3 operation(s) for organization-roles.
  name: OutSystems Organization Roles API
  phrasing_intents:
  - id: OrganizationRole_CreateOrganizationRole
    intent: Create an organization role
    question: How do I create a custom organization role with specific permissions?
  - id: OrganizationRole_QueryOrganizationRoles
    intent: List organization roles
    question: What organization roles are defined for ODC members?
  - id: OrganizationRole_DeleteOrganizationRole
    intent: Delete an organization role
    question: Can I delete a custom organization role?
  - id: OrganizationRole_ReadOrganizationRole
    intent: Get an organization role
    question: Which permissions does a particular organization role include?
  - id: OrganizationRole_UpdateOrganizationRole
    intent: Update an organization role
    question: How do I change the permissions granted by an organization role?
  - id: OrganizationRole_QueryUsersByRole
    intent: List members holding an organization role
    question: Who in my organization has a particular organization role?
  phrasing_ops: 6
  slug: outsystems-organization-roles-api
- baseURL: https://{odc-portal-domain}/api/identity/v1
  baseurl_source: declared
  description: The Patterns API from OutSystems — 2 operation(s) for patterns.
  name: OutSystems Patterns API
  phrasing_intents:
  - id: PatternsControllerV_GetPatterns
    intent: List code quality patterns
    question: Which code patterns can the OutSystems code analysis detect?
  - id: PatternsControllerV_GetPatternsById
    intent: Get a code quality pattern
    question: What does a specific code pattern detect, and how severe is it?
  phrasing_ops: 2
  slug: outsystems-patterns-api
- baseURL: https://{odc-portal-domain}/api/identity/v1
  baseurl_source: declared
  description: The permissions API from OutSystems — 2 operation(s) for permissions.
  name: OutSystems Permissions API
  phrasing_intents:
  - id: Permission_QueryPermissions
    intent: List available permissions
    question: What permissions can be assigned to roles in ODC?
  - id: Permission_ReadPermission
    intent: Get a permission's details
    question: What exactly does a particular permission allow?
  phrasing_ops: 2
  slug: outsystems-permissions-api
- baseURL: https://{odc-portal-domain}/api/identity/v1
  baseurl_source: declared
  description: The Portfolios API from OutSystems — 2 operation(s) for portfolios.
  name: OutSystems Portfolios API
  phrasing_intents:
  - id: Portfolios_ListPortfolios
    intent: List portfolios
    question: What portfolios exist in my ODC organization?
  - id: Portfolios_PatchPortfolio
    intent: Rename a portfolio
    question: How do I rename a portfolio?
  phrasing_ops: 2
  slug: outsystems-portfolios-api
- baseURL: https://{odc-portal-domain}/api/identity/v1
  baseurl_source: declared
  description: Activate, deactivate, and manage private gateways.
  name: OutSystems Private gateways API
  phrasing_intents:
  - id: PrivateGateway_Activation
    intent: Activate a stage's private gateway
    question: How do I turn on the Private Gateway for a stage?
  - id: PrivateGateway_Deactivation
    intent: Deactivate a stage's private gateway
    question: Can I switch off the Private Gateway for a stage?
  - id: PrivateGateway_Get
    intent: Get a stage's private gateway status
    question: Is the Private Gateway active in my stage?
  - id: PrivateGateway_KeyRotation
    intent: Rotate a private gateway key
    question: How do I rotate the key used by my Private Gateway?
  phrasing_ops: 4
  slug: outsystems-private-gateways-api
- baseURL: https://{odc-portal-domain}/api/identity/v1
  baseurl_source: declared
  description: The Public Elements API from OutSystems — 1 operation(s) for public elements.
  name: OutSystems Public Elements API
  phrasing_intents:
  - id: DependencyManagement_SearchPublicElements
    intent: Search public elements across assets
    question: Which reusable public actions and elements can I reference from other assets?
  phrasing_ops: 1
  slug: outsystems-public-elements-api
- baseURL: https://{odc-portal-domain}/api/identity/v1
  baseurl_source: declared
  description: The publish-operations API from OutSystems — 3 operation(s) for publish-operations.
  name: OutSystems Publish Operations API
  phrasing_intents:
  - id: PublishOperations_Filter
    intent: List publications
    question: Which publish operations ran for my assets recently?
  - id: PublishOperations_Post
    intent: Publish an asset revision
    question: How do I publish an asset revision to a stage through the API?
  - id: PublishOperations_Get
    intent: Get one publication
    question: How do I check the status of a single publication?
  - id: PublishOperations_GetMessages
    intent: Read a publication's log messages
    question: Why did my publication fail, according to its log?
  phrasing_ops: 4
  slug: outsystems-publish-operations-api
- baseURL: https://{odc-portal-domain}/api/identity/v1
  baseurl_source: declared
  description: The SourceCodeDownload API from OutSystems — 2 operation(s) for sourcecodedownload.
  name: OutSystems Source Code Download API
  phrasing_intents:
  - id: SourceCodeDownload_CreateDownloadOperation
    intent: Start a source download of an external library
    question: How do I download the source code of a published external library?
  - id: SourceCodeDownload_GetDownloadUri
    intent: Get the source download link when ready
    question: Is my external library source download ready, and where is the link?
  phrasing_ops: 2
  slug: outsystems-sourcecodedownload-api
- baseURL: https://{odc-portal-domain}/api/identity/v1
  baseurl_source: declared
  description: The Upload API from OutSystems — 1 operation(s) for upload.
  name: OutSystems Upload API
  phrasing_intents:
  - id: Upload_UploadOperation
    intent: Get an upload URL for library source
    question: Where do I upload external library source code before generating a library?
  phrasing_ops: 1
  slug: outsystems-upload-api
- baseURL: https://{odc-portal-domain}/api/identity/v1
  baseurl_source: declared
  description: The Uploads API from OutSystems — 1 operation(s) for uploads.
  name: OutSystems Uploads API
  phrasing_intents:
  - id: Uploads_CreateUpload
    intent: Create a pre-signed file upload URL
    question: How do I upload an OML file before creating an asset revision?
  phrasing_ops: 1
  slug: outsystems-uploads-api
- baseURL: https://{odc-portal-domain}/api/identity/v1
  baseurl_source: declared
  description: The users API from OutSystems — 10 operation(s) for users.
  name: OutSystems Users API
  phrasing_intents:
  - id: BulkUserProfile_CreateBulkUserProfilesOperation
    intent: Create users in bulk
    question: How do I create up to 100 users in one request?
  - id: BulkUserProfile_GetBulkUserProfileOperationStatus
    intent: Check a bulk user creation's status
    question: Did my bulk user import finish, and which records failed?
  - id: UserApplicationRoles_GrantApplicationRoleToUser
    intent: Grant an application role to a user
    question: How do I give one user an application role?
  - id: UserApplicationRoles_RevokeApplicationRoleForUser
    intent: Revoke an application role from a user
    question: How do I take an application role away from a user?
  - id: UserApplicationRoles_QueryUserApplicationRoles
    intent: List a user's application roles
    question: Which application roles does a given user have?
  - id: UserOrganizationRoles_GetUserOrganizationRoles
    intent: List a user's organization roles
    question: What organization roles does a team member hold?
  - id: UserOrganizationRoles_GrantOrganizationRoleToUser
    intent: Grant an organization role to a user
    question: How do I give a member an organization role?
  - id: UserOrganizationRoles_RevokeOrganizationRoleForUser
    intent: Revoke an organization role from a user
    question: How do I remove an organization role from a member?
  phrasing_ops: 15
  slug: outsystems-users-api
- baseURL: https://{tenant}.outsystems.dev/mcp
  baseurl_source: declared
  description: The /applications API from OutSystems — 6 operation(s) for /applications.
  name: OutSystems /applications API
  slug: outsystems-applications-api
- baseURL: https://{tenant}.outsystems.dev/mcp
  baseurl_source: declared
  description: The /auth API from OutSystems — 1 operation(s) for /auth.
  name: OutSystems /auth API
  slug: outsystems-auth-api
- baseURL: https://{tenant}.outsystems.dev/mcp
  baseurl_source: declared
  description: The /deployments API from OutSystems — 6 operation(s) for /deployments.
  name: OutSystems /deployments API
  slug: outsystems-deployments-api
- baseURL: https://{tenant}.outsystems.dev/mcp
  baseurl_source: declared
  description: The /modules API from OutSystems — 4 operation(s) for /modules.
  name: OutSystems /modules API
  slug: outsystems-modules-api
- baseURL: https://{tenant}.outsystems.dev/mcp
  baseurl_source: declared
  description: The /roles API from OutSystems — 3 operation(s) for /roles.
  name: OutSystems /roles API
  slug: outsystems-roles-api
- baseURL: https://{tenant}.outsystems.dev/mcp
  baseurl_source: declared
  description: The /teams API from OutSystems — 6 operation(s) for /teams.
  name: OutSystems /teams API
  slug: outsystems-teams-api
artifact_total: 196
asyncapis:
- description: ''
  name: Outsystems Webhooks
  slug: outsystems-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Code Quality Analysis Status API
  slug: open-outsystems-analysis-status-api
- collection_type: open
  name: User and Access Management Application Roles API
  slug: open-outsystems-application-roles-api
- collection_type: open
  name: Outsystems Assets API
  slug: open-outsystems-assets-api
- collection_type: open
  name: Code Quality Assets Quality Metrics API
  slug: open-outsystems-assets-quality-metrics-api
- collection_type: open
  name: Operations Build API
  slug: open-outsystems-build-api
- collection_type: open
  name: Native Mobile Build Build Operations API
  slug: open-outsystems-buildoperations-api
- collection_type: open
  name: Code Quality Code Analyses API
  slug: open-outsystems-code-analyses-api
- collection_type: open
  name: Dependency Management Deletion Analyses API
  slug: open-outsystems-deletion-analyses-api
- collection_type: open
  name: Outsystems Deployed Assets API
  slug: open-outsystems-deployed-assets-api
- collection_type: open
  name: Dependency Management Deployment Analyses API
  slug: open-outsystems-deployment-analyses-api
- collection_type: open
  name: Deployments Deployment Operations API
  slug: open-outsystems-deployment-operations-api
- collection_type: open
  name: Environment Configurations Domains API
  slug: open-outsystems-domains-api
- collection_type: open
  name: Outsystems Environments API
  slug: open-outsystems-environments-api
- collection_type: open
  name: Code Quality Findings API
  slug: open-outsystems-findings-api
- collection_type: open
  name: Code Quality Findings Summary API
  slug: open-outsystems-findings-summary-api
- collection_type: open
  name: Code Quality Findings Trend API
  slug: open-outsystems-findings-trend-api
- collection_type: open
  name: External Library Generation Service Generation Operations API
  slug: open-outsystems-generationoperations-api
- collection_type: open
  name: User and Access Management Groups API
  slug: open-outsystems-groups-api
- collection_type: open
  name: User and Access Management Identity Providers API
  slug: open-outsystems-identity-providers-api
- collection_type: open
  name: Environment Configurations IP filters API
  slug: open-outsystems-ip-filters-api
- collection_type: open
  name: Portfolio Libraries API
  slug: open-outsystems-libraries-api
- collection_type: open
  name: Native Mobile Build Native Builder Versions API
  slug: open-outsystems-nativebuilderversions-api
- collection_type: open
  name: Native Mobile Build Native Build Extensibility Settings API
  slug: open-outsystems-nativebuildextensibilitysettings-api
- collection_type: open
  name: Native Mobile Build Native Mobile Configurations API
  slug: open-outsystems-nativemobileconfigurations-api
- collection_type: open
  name: Subscription Organization API
  slug: open-outsystems-organization-api
- collection_type: open
  name: User and Access Management Organization Roles API
  slug: open-outsystems-organization-roles-api
- collection_type: open
  name: Code Quality Patterns API
  slug: open-outsystems-patterns-api
- collection_type: open
  name: User and Access Management Permissions API
  slug: open-outsystems-permissions-api
- collection_type: open
  name: Portfolio Portfolios API
  slug: open-outsystems-portfolios-api
- collection_type: open
  name: Environment Configurations Private gateways API
  slug: open-outsystems-private-gateways-api
- collection_type: open
  name: Dependency Management Public Elements API
  slug: open-outsystems-public-elements-api
- collection_type: open
  name: Deployments Publish Operations API
  slug: open-outsystems-publish-operations-api
- collection_type: open
  name: External Library Generation Service Source Code Download API
  slug: open-outsystems-sourcecodedownload-api
- collection_type: open
  name: External Library Generation Service Upload API
  slug: open-outsystems-upload-api
- collection_type: open
  name: Asset Repository Uploads API
  slug: open-outsystems-uploads-api
- collection_type: open
  name: User and Access Management Users API
  slug: open-outsystems-users-api
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/outsystems/refs/heads/main/rules/outsystems-rules.yml
  title: ''
  type: Spectral
  url: rules/outsystems-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/outsystems/refs/heads/main/json-ld/outsystems-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/outsystems-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/outsystems/refs/heads/main/vocabulary/outsystems-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/outsystems-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/outsystems/refs/heads/main/asyncapi/outsystems-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/outsystems-webhooks.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/outsystems/refs/heads/main/hosts/outsystems-hosts.yml
  title: ''
  type: Hosts
  url: hosts/outsystems-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/outsystems/refs/heads/main/vendors/outsystems-vendors.yml
  title: ''
  type: Vendors
  url: vendors/outsystems-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.outsystems.com/news
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/outsystems/refs/heads/main/plans/outsystems-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/outsystems-plans-pricing.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/outsystems/refs/heads/main/capabilities/outsystems-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/outsystems-capability-edges.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/outsystems/refs/heads/main/overlays/outsystems-asset-configurations-api-v1-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/outsystems-asset-configurations-api-v1-overlay.yaml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/outsystems/refs/heads/main/security/outsystems-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/outsystems-trust-center.yml
- group: company
  title: ''
  type: Website
  url: https://www.outsystems.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.outsystems.com/community/
- group: docs
  title: ''
  type: Documentation
  url: https://success.outsystems.com/documentation/outsystems_developer_cloud/
- group: docs
  title: ''
  type: APIReference
  url: https://success.outsystems.com/documentation/outsystems_developer_cloud/odc_rest_apis/api_references/
- group: start
  title: ''
  type: GettingStarted
  url: https://success.outsystems.com/documentation/outsystems_developer_cloud/getting_started/
- group: operate
  title: ''
  type: Support
  url: https://success.outsystems.com/support/home/
- group: company
  title: ''
  type: Blog
  url: https://www.outsystems.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/OutSystems
- group: commercial
  title: ''
  type: Pricing
  url: https://www.outsystems.com/pricing-and-editions/
- group: start
  title: ''
  type: SignUp
  url: https://www.outsystems.com/free-edition/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.outsystems.com/legal/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.outsystems.com/legal/
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/outsystems-official/outsystems-11-platform-apis
- group: operate
  title: ''
  type: StatusPage
  url: https://status.outsystems.com/
- group: auth
  title: ''
  type: Security
  url: https://www.outsystems.com/security/report-a-vulnerability
- group: auth
  title: ''
  type: Compliance
  url: https://security.outsystems.com/
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/outsystems/refs/heads/main/packages/outsystems-packages.yml
  title: ''
  type: Packages
  url: packages/outsystems-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/outsystems/refs/heads/main/packages/outsystems-packages.yml
  title: ''
  type: SDKs
  url: packages/outsystems-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/outsystems/refs/heads/main/cli/outsystems-cli.yml
  title: ''
  type: CLI
  url: cli/outsystems-cli.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/outsystems/refs/heads/main/components/outsystems-components.yml
  title: ''
  type: Components
  url: components/outsystems-components.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/outsystems/refs/heads/main/well-known/outsystems-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/outsystems-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/outsystems/refs/heads/main/well-known/outsystems-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/outsystems-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/outsystems/refs/heads/main/llms/outsystems-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/outsystems-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/outsystems/refs/heads/main/authentication/outsystems-authentication.yml
  title: ''
  type: Authentication
  url: authentication/outsystems-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/outsystems/refs/heads/main/scopes/outsystems-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/outsystems-scopes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/outsystems/refs/heads/main/conventions/outsystems-conventions.yml
  title: ''
  type: Conventions
  url: conventions/outsystems-conventions.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/outsystems/refs/heads/main/rate-limits/outsystems-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/outsystems-rate-limits.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/outsystems/refs/heads/main/errors/outsystems-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/outsystems-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/outsystems/refs/heads/main/lifecycle/outsystems-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/outsystems-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/outsystems/refs/heads/main/lifecycle/outsystems-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/outsystems-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/outsystems/refs/heads/main/changelog/outsystems-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/outsystems-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/outsystems/refs/heads/main/conformance/outsystems-conformance.yml
  title: ''
  type: Conformance
  url: conformance/outsystems-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/outsystems/refs/heads/main/data-model/outsystems-data-model.yml
  title: ''
  type: DataModel
  url: data-model/outsystems-data-model.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/outsystems/refs/heads/main/security/outsystems-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/outsystems-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/outsystems/refs/heads/main/security/outsystems-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/outsystems-vulnerability-disclosure.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/outsystems/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/outsystems/refs/heads/main/agentic-access/outsystems-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/outsystems-agentic-access.yml
created: '2026-08-02'
description: OutSystems is an enterprise low-code and AI-assisted application development platform company, founded in 2001 and headquartered in Boston, Massachusetts with engineering in Lisbon, Portugal. Its two product lines are OutSystems 11 (O11), the self-managed/PaaS platform, and OutSystems Developer Cloud (ODC), the cloud-native successor. ODC publishes a documented set of public REST APIs covering user and access management, portfolio, asset repository, asset and environment configurations, build operations, deployments, dependency and impact analysis, code quality, native mobile builds, external library generation, and subscription/entitlement usage. All ODC REST APIs authenticate with OAuth 2.0 client-credentials via a per-tenant OIDC discovery document, use offset/limit pagination, and are rate limited per API domain. OutSystems also ships a remote MCP server (early alpha) that exposes app inspection, the Mentor OML editing session, publishing, deployments, external libraries
  and environments to AI coding agents.
image: https://www.outsystems.com/favicon.ico
json_schemas:
- name: CodeAnalysisRequest
  property_count: 2
  slug: outsystems-adhoc-analysis-request-v1
- name: AgentConfigPatch
  property_count: 6
  slug: outsystems-agent-config-patch
- name: AgentConfigResult
  property_count: 9
  slug: outsystems-agent-config-result
- name: AndroidBuildConfigurationRequest
  property_count: 9
  slug: outsystems-android-build-configuration-request
- name: AndroidBuildConfigurationResult
  property_count: 9
  slug: outsystems-android-build-configuration-result
- name: ApplicationConfigPatch
  property_count: 7
  slug: outsystems-application-config-patch
- name: ApplicationConfigResult
  property_count: 10
  slug: outsystems-application-config-result
- name: ApplicationRoleApiResponsePaginatedResponseApi
  property_count: 2
  slug: outsystems-application-role-api-response-paginated-response-api
- name: ApplicationVersion
  property_count: 34
  slug: outsystems-application-version
- name: AppsOverviewResponseV1PagedListResponse
  property_count: 2
  slug: outsystems-apps-overview-response-v1-paged-list-response
- name: AssetMetadata
  property_count: 10
  slug: outsystems-asset-metadata
- name: AssetRevisionV1
  property_count: 16
  slug: outsystems-asset-revision-v1
- name: AssetSignature
  property_count: 3
  slug: outsystems-asset-signature
- name: AssetVersionCreationRequest
  property_count: 7
  slug: outsystems-asset-version-creation-request
- name: AssetVersionPatchRequest
  property_count: 3
  slug: outsystems-asset-version-patch-request
- name: BaseIpFilterGroup
  property_count: 5
  slug: outsystems-base-ip-filter-group
- name: BuildDetails
  property_count: 9
  slug: outsystems-build-details
- name: BuildFeedbackDetailsResponse
  property_count: 1
  slug: outsystems-build-feedback-details-response
- name: BuildOperationDetails
  property_count: 3
  slug: outsystems-build-operation-details
- name: BuildOperationRequest
  property_count: 7
  slug: outsystems-build-operation-request
- name: BuildOperationResult
  property_count: 23
  slug: outsystems-build-operation-result
- name: BuildOperationValidationRequest
  property_count: 5
  slug: outsystems-build-operation-validation-request
- name: BuildOperationValidationResponse
  property_count: 1
  slug: outsystems-build-operation-validation-response
- name: BuildResponse
  property_count: 2
  slug: outsystems-build-response
- name: BulkUserProfileOperationApiRecordBulkApiResponse
  property_count: 5
  slug: outsystems-bulk-user-profile-operation-api-record-bulk-api-response
- name: CodeAnalysisResponse
  property_count: 2
  slug: outsystems-code-analysis-response-v1
- name: CodeAnalysisStatusResponse
  property_count: 5
  slug: outsystems-code-analysis-status-response-v1
- name: DependenciesPublicElementFilter
  property_count: 10
  slug: outsystems-dependencies-public-element-filter
- name: DeployedAssetPagedListResponse
  property_count: 2
  slug: outsystems-deployed-asset-paged-list-response
- name: DeploymentOperationRequest
  property_count: 5
  slug: outsystems-deployment-operation-request
- name: DeploymentOperationResponse
  property_count: 11
  slug: outsystems-deployment-operation-response
- name: DomainPagedListResponse
  property_count: 2
  slug: outsystems-domain-paged-list-response
- name: DomainPatchRequest
  property_count: 2
  slug: outsystems-domain-patch-request
- name: DomainPatchResponse
  property_count: 1
  slug: outsystems-domain-patch-response
- name: DomainRequest
  property_count: 2
  slug: outsystems-domain-request
- name: Domain
  property_count: 9
  slug: outsystems-domain
- name: EntitlementUsageItemListResponse
  property_count: 1
  slug: outsystems-entitlement-usage-item-list-response
- name: EnvironmentEntitlements
  property_count: 2
  slug: outsystems-environment-entitlements
- name: ExtensibilitySettingsRequest
  property_count: 2
  slug: outsystems-extensibility-settings-request
- name: ExtensibilitySettingsResponse
  property_count: 2
  slug: outsystems-extensibility-settings-response
- name: FindingsResponseV1PagedListResponse
  property_count: 2
  slug: outsystems-findings-response-v1-paged-list-response
- name: FindingsSummaryResponse
  property_count: 2
  slug: outsystems-findings-summary-response-v1
- name: FindingsTrendResponseV1ResultsResponse
  property_count: 1
  slug: outsystems-findings-trend-response-v1-results-response
- name: GeneratedCodePackageResponse
  property_count: 3
  slug: outsystems-generated-code-package-response
- name: GeneratedCodePackagingResponse
  property_count: 1
  slug: outsystems-generated-code-packaging-response
- name: GrantDetailsRequest
  property_count: 3
  slug: outsystems-grant-details-request
- name: GroupApiResponse
  property_count: 7
  slug: outsystems-group-api-response
- name: GroupCreateRequest
  property_count: 5
  slug: outsystems-group-create-request
- name: IdentityProviderResponsePaginatedResponseApi
  property_count: 2
  slug: outsystems-identity-provider-response-paginated-response-api
- name: IdentityProviderResponse
  property_count: 12
  slug: outsystems-identity-provider-response
- name: Int32NullableDeploymentOperationResponsePagedListResponse
  property_count: 2
  slug: outsystems-int32-nullable-deployment-operation-response-paged-list-response
- name: Int32NullablePublishOperationResponsePagedListResponse
  property_count: 2
  slug: outsystems-int32-nullable-publish-operation-response-paged-list-response
- name: IosBuildConfigurationRequest
  property_count: 9
  slug: outsystems-ios-build-configuration-request
- name: IosBuildConfigurationResult
  property_count: 9
  slug: outsystems-ios-build-configuration-result
- name: IpFilterGroupKey
  property_count: 1
  slug: outsystems-ip-filter-group-key
- name: IpFilterGroup
  property_count: 6
  slug: outsystems-ip-filter-group
- name: IpFilterGroups
  property_count: 1
  slug: outsystems-ip-filter-groups
- name: LibraryPagedListResponse
  property_count: 2
  slug: outsystems-library-paged-list-response
- name: NativeBuildVersions
  property_count: 3
  slug: outsystems-native-build-versions
- name: NativeBuilderVersionListResponse
  property_count: 1
  slug: outsystems-native-builder-version-list-response
- name: OrganizationConfigurations
  property_count: 2
  slug: outsystems-organization-configurations
- name: OrganizationEntitlements
  property_count: 8
  slug: outsystems-organization-entitlements
- name: OrganizationRoleApiResponsePaginatedResponseApi
  property_count: 2
  slug: outsystems-organization-role-api-response-paginated-response-api
- name: OrganizationRoleApiResponse
  property_count: 4
  slug: outsystems-organization-role-api-response
- name: OrganizationRoleByUserApiResponsePaginatedResponseApi
  property_count: 2
  slug: outsystems-organization-role-by-user-api-response-paginated-response-api
- name: OrganizationRoleCreateRequest
  property_count: 2
  slug: outsystems-organization-role-create-request
- name: OrganizationRoleCreateResponse
  property_count: 1
  slug: outsystems-organization-role-create-response
- name: OrganizationRoleUpdateRequest
  property_count: 2
  slug: outsystems-organization-role-update-request
- name: OutSystems.ExternalLibraryGeneration.Service.V1Beta1.Controllers.DataObjects.CreationOperationResponse
  property_count: 1
  slug: outsystems-out-systems-external-library-generation-service-v1-beta1-controllers-data-objects-creation-operation-response
- name: OutSystems.ExternalLibraryGeneration.Service.V1Beta1.Controllers.DataObjects.GenerationOperationContentsResponse
  property_count: 2
  slug: outsystems-out-systems-external-library-generation-service-v1-beta1-controllers-data-objects-generation-operation-contents-response
- name: OutSystems.ExternalLibraryGeneration.Service.V1Beta1.Controllers.DataObjects.GenerationOperationListResponse
  property_count: 1
  slug: outsystems-out-systems-external-library-generation-service-v1-beta1-controllers-data-objects-generation-operation-list-response
- name: OutSystems.ExternalLibraryGeneration.Service.V1Beta1.Controllers.DataObjects.GenerationOperationLogMessagesResponse
  property_count: 2
  slug: outsystems-out-systems-external-library-generation-service-v1-beta1-controllers-data-objects-generation-operation-log-messages-response
- name: OutSystems.ExternalLibraryGeneration.Service.V1Beta1.Controllers.DataObjects.GenerationOperationResponse
  property_count: 10
  slug: outsystems-out-systems-external-library-generation-service-v1-beta1-controllers-data-objects-generation-operation-response
- name: OutSystems.ExternalLibraryGeneration.Service.V1Beta1.Controllers.DataObjects.SourceCodeDownload
  property_count: 6
  slug: outsystems-out-systems-external-library-generation-service-v1-beta1-controllers-data-objects-source-code-download
- name: OutSystems.ExternalLibraryGeneration.Service.V1Beta1.Controllers.DataObjects.UploadResponse
  property_count: 2
  slug: outsystems-out-systems-external-library-generation-service-v1-beta1-controllers-data-objects-upload-response
- name: OutSystems.ExternalLibraryGeneration.Service.V1Beta1.Models.GenerationOperationCreationRequest
  property_count: 2
  slug: outsystems-out-systems-external-library-generation-service-v1-beta1-models-generation-operation-creation-request
- name: PatchDefaultDomainRequest
  property_count: 1
  slug: outsystems-patch-default-domain-request
- name: PatchGroupApplicationRolesRequest
  property_count: 2
  slug: outsystems-patch-group-application-roles-request
- name: PatchIpFilterGroup
  property_count: 5
  slug: outsystems-patch-ip-filter-group
- name: PatchPortfolioRequest
  property_count: 1
  slug: outsystems-patch-portfolio-request
- name: PatchUsersByGroupRequest
  property_count: 2
  slug: outsystems-patch-users-by-group-request
- name: PatternsResponsePagedListResponse
  property_count: 2
  slug: outsystems-patterns-response-paged-list-response
- name: PermissionResponsePaginatedResponseApi
  property_count: 2
  slug: outsystems-permission-response-paginated-response-api
- name: PermissionResponse
  property_count: 11
  slug: outsystems-permission-response
- name: PortfolioPagedListResponse
  property_count: 2
  slug: outsystems-portfolio-paged-list-response
- name: PublicDeletionAnalysisReportPublicAnalysisResult
  property_count: 8
  slug: outsystems-public-deletion-analysis-report-public-analysis-result
- name: PublicDeploymentAnalysisReportPublicAnalysisResult
  property_count: 8
  slug: outsystems-public-deployment-analysis-report-public-analysis-result
- name: PublicElementStringTypesPagedListResponse
  property_count: 2
  slug: outsystems-public-element-string-types-paged-list-response
- name: PublicLaunchDeletionAnalysisRequest
  property_count: 1
  slug: outsystems-public-launch-deletion-analysis-request
- name: PublicLaunchDeploymentAnalysisRequest
  property_count: 3
  slug: outsystems-public-launch-deployment-analysis-request
- name: PublishOperationRequest
  property_count: 4
  slug: outsystems-publish-operation-request
- name: PublishOperationResponse
  property_count: 10
  slug: outsystems-publish-operation-response
- name: ReferenceKeyResponse
  property_count: 1
  slug: outsystems-reference-key-response
- name: RoleUserResponsePaginatedResponseApi
  property_count: 2
  slug: outsystems-role-user-response-paginated-response-api
- name: SecureGateway
  property_count: 4
  slug: outsystems-secure-gateway
- name: SecureGatewayToken
  property_count: 1
  slug: outsystems-secure-gateway-token
- name: StatusAnalysisResponse
  property_count: 1
  slug: outsystems-status-sync-response-v1
- name: StringMessageDetailsV1TaskProgressMessagePagedListResponse
  property_count: 2
  slug: outsystems-string-message-details-v1-task-progress-message-paged-list-response
- name: UnifiedEntitlementByAssetBlockPagedListResponse
  property_count: 2
  slug: outsystems-unified-entitlement-by-asset-block-paged-list-response
- name: UploadsResponse
  property_count: 1
  slug: outsystems-uploads-response
- name: UserApplicationRoleApiResponsePaginatedResponseApi
  property_count: 2
  slug: outsystems-user-application-role-api-response-paginated-response-api
- name: UserProfileApiResponse
  property_count: 11
  slug: outsystems-user-profile-api-response
- name: UserProfileCreateApiRequest
  property_count: 8
  slug: outsystems-user-profile-create-api-request
- name: VersionSuggestionsRequest
  property_count: 3
  slug: outsystems-version-suggestions-request
jsonld:
- class_count: 120
  name: Outsystems Context
  property_count: 217
  slug: outsystems-context
layout: provider
mcp_servers:
- description: Remote MCP server at {tenant}.outsystems.dev over HTTP.
  name: OutSystems MCP Server
  slug: outsystems
modified: '2026-08-02'
name: OutSystems
nav: Providers
network: true
overview: 'OutSystems publishes 43 APIs on the [APIs.io](https://apis.io/) network, including Analysis Status API, Application Roles API, Assets API, and 40 more. Tagged areas include Company, Low-Code, Application Development, Platform-as-a-Service, and DevOps.


  The OutSystems catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  OutSystems'' developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 41 more developer resources.'
plans:
- name: Outsystems Plans Pricing
  plan_count: 2
  slug: outsystems-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 12
  name: Outsystems Rate Limits
  slug: outsystems-rate-limits
rules:
- effective_rule_count: 55
  extends:
  - spectral:oas
  name: OutSystems API Rules
  rule_count: 14
  severity_counts:
    error: 12
    hint: 0
    info: 1
    warn: 1
  slug: outsystems-rules
scopes:
- name: Outsystems Scopes
  scope_count: 0
  slug: outsystems-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: exemplar
  composite: 75.8
  coverage:
    artifact_dirs: 34
    catalog_earned: 85.8
    catalog_earned_first_party: 20.0
    catalog_gap: 29.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 10.9
  facets:
    access_clarity: 81.6
    contract_governance: 22.0
    contract_quality: 69.3
    developer_ergonomics: 75.6
    discoverability: 80.4
    operational_transparency: 92.1
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 64.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 42
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 41.8
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  trend: rising
  upsert:
    applies: true
    score: 11.1
screenshot: https://raw.githubusercontent.com/api-evangelist/outsystems/refs/heads/main/screenshots/outsystems-2026-08-17T124448.png
security:
- kind: authentication
  name: Outsystems Authentication
  slug: outsystems-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Outsystems Domain Security
  slug: outsystems-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Outsystems Vulnerability Disclosure
  slug: outsystems-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Outsystems Trust Center
  slug: outsystems-trust-center
  summary_line: ISO 27001, ISO 27017, ISO 27018, FedRAMP, GDPR
slug: outsystems
tags:
- Company
- Low-Code
- Application Development
- Platform-as-a-Service
- DevOps
- Deployment
- Identity and Access Management
- Artificial Intelligence
- Enterprise Software
- Mobile Development
website: https://www.outsystems.com/
---
