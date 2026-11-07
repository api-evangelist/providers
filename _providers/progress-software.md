---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
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
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: mostly
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 47.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 298
  human_in_the_loop: 12
  name: Progress Software Agentic Access
  operation_count: 558
  slug: progress-software-agentic-access
  summary_line: 558 operations · 298 acting · 12 human-in-the-loop
api_count: 3
apis:
- description: The ShareFile API v3 is the OData-based REST interface of Progress ShareFile, covering Items, Folders, Accounts, Users, Groups, Shares, Access Controls, Capabilities, Connector Groups, Devices, Encryp
  name: ShareFile API v3
  slug: progress-software-sharefile
- description: Sitefinity CMS exposes its content as OData v4 web services under a configurable service route (by default /api/default) on the customer's own Sitefinity instance. The headless API serves content type
  name: Sitefinity CMS Headless OData Services
  slug: progress-software-sitefinity-odata
- baseURL: https://automate.chef.io
  baseurl_source: declared
  description: The AdHocTransferSettings API from Progress Software — 1 operation(s) for adhoctransfersettings.
  name: Progress Software Ad Hoc Transfer Settings API
  phrasing_intents:
  - id: GETapi/v1/settings/adhoctransfer/maintenance/agingexpiration-1.0
    intent: Get ad hoc transfer aging and expiration
    question: How long do ad hoc transfer packages last before they expire?
  phrasing_ops: 1
  slug: progress-software-adhoctransfersettings-api
- baseURL: https://automate.chef.io
  baseurl_source: declared
  description: The AppearanceSettings API from Progress Software — 1 operation(s) for appearancesettings.
  name: Progress Software Appearance Settings API
  phrasing_intents:
  - id: POSTapi/v1/settings/appearance/brand/logos-1.0
    intent: Update the organization's branding logos
    question: How do I upload a custom logo for my organization's web interface?
  phrasing_ops: 1
  slug: progress-software-appearancesettings-api
- baseURL: https://automate.chef.io
  baseurl_source: declared
  description: The ApplicationsService API from Progress Software — 2 operation(s) for applicationsservice.
  name: Progress Software Applications Service API
  phrasing_intents:
  - id: ApplicationsService_GetServicesUsageCount
    intent: Get the services usage count for telemetry
    question: How many application services are counted for telemetry?
  - id: ApplicationsService_UpdateTelemetryReported
    intent: Record when services telemetry was last reported
    question: How do I record the time services telemetry was last sent?
  phrasing_ops: 2
  slug: progress-software-applicationsservice-api
- baseURL: https://automate.chef.io
  baseurl_source: declared
  description: The Authentication API from Progress Software — 5 operation(s) for authentication.
  name: Progress Software Authentication API
  phrasing_intents:
  - id: GETapi/v1/auth/identityproviders?Page={Page}&PerPage={PerPage}&SortField={SortField}&SortDirection={SortDirection}&OrgId={OrgId}-1.0
    intent: List identity providers
    question: Which identity providers are configured for my organization?
  - id: POSTapi/v1/auth/actasadmin-1.0
    intent: Act as administrator in an organization
    question: How can a sysadmin act as administrator in a specific organization?
  - id: Auth_GetToken
    intent: Get an API access token
    question: How do I sign in and get an API token with a username and password?
  - id: Auth_RevokeToken
    intent: Revoke an API token
    question: How do I log out by revoking my API token?
  - id: Auth_SendOtp
    intent: Send a one-time password
    question: How do I get a one-time password sent during MFA sign-in?
  phrasing_ops: 5
  slug: progress-software-authentication-api
- baseURL: https://automate.chef.io
  baseurl_source: declared
  description: Introspection endpoints that allow clients to check which API actions are authorized for the current token or user.
  name: Progress Software Authorization API
  phrasing_intents:
  - id: Authorization_IntrospectAll
    intent: List all endpoints I'm allowed to call
    question: Which API endpoints does my current identity have access to?
  - id: Authorization_Introspect
    intent: Check my access to one endpoint
    question: Am I allowed to call a specific API path?
  - id: Authorization_IntrospectSome
    intent: Check my access to several endpoints
    question: Can I check access to a list of API paths in one call?
  phrasing_ops: 3
  slug: progress-software-authorization-api
- baseURL: https://automate.chef.io
  baseurl_source: declared
  description: The Cds API from Progress Software — 4 operation(s) for cds.
  name: Progress Software Cds API
  phrasing_intents:
  - id: Cds_SubmitCredentials
    intent: Submit cloud credentials to enable content
    question: How do I enable content downloads by submitting my cloud client ID and secret?
  - id: Cds_IsContentEnabled
    intent: Check whether content is enabled
    question: Is content enabled on this Automate instance?
  - id: Cds_InstallContentItem
    intent: Install a content item
    question: How do I install a content item by its ID?
  - id: Cds_ListContentItems
    intent: List available content items
    question: What content items are available and which are already installed?
  phrasing_ops: 4
  slug: progress-software-cds-api
- baseURL: https://automate.chef.io
  baseurl_source: declared
  description: The ChefIngester API from Progress Software — 6 operation(s) for chefingester.
  name: Progress Software Chef Ingester API
  phrasing_intents:
  - id: ChefIngester_ProcessChefAction
    intent: Ingest a Chef server action event
    question: How do I send a Chef server action, like a cookbook upload, into the event feed?
  - id: ChefIngester_ProcessLivenessPing
    intent: Ingest a node liveness ping
    question: How does a node report that it's still alive when it isn't running a full converge?
  - id: ChefIngester_ProcessMultipleNodeDeletes
    intent: Delete several ingested nodes at once
    question: How do I remove a batch of nodes from the infrastructure data in one call?
  - id: ChefIngester_ProcessNodeDelete
    intent: Delete one ingested node
    question: How do I delete a single node that's been decommissioned?
  - id: ChefIngester_ProcessChefRun
    intent: Ingest a Chef client run report
    question: How do I submit a Chef client run report with its resources and status?
  - id: ChefIngester_GetVersion
    intent: Get the ingest service version
    question: Which version of the ingest service is running?
  phrasing_ops: 6
  slug: progress-software-chefingester-api
- baseURL: https://automate.chef.io
  baseurl_source: declared
  description: The Comp_Assets API from Progress Software — 4 operation(s) for comp_assets.
  name: Progress Software Comp Assets API
  phrasing_intents:
  - id: ReportingService_SetAssetConfig
    intent: Set how many days before an asset counts as unreachable
    question: How do I change the number of days after which a compliance asset is treated as unreachable?
  - id: ReportingService_GetAssetConfig
    intent: Get the unreachable assets setting
    question: After how many days does Chef Automate consider a compliance asset unreachable?
  - id: ReportingService_AssetCount
    intent: Count reported and unreported compliance assets
    question: How many of my compliance assets have reported versus not reported?
  - id: ReportingService_ListAsset
    intent: List compliance assets by collection status
    question: Which compliance assets have stopped reporting?
  phrasing_ops: 4
  slug: progress-software-comp-assets-api
- baseURL: https://automate.chef.io
  baseurl_source: declared
  description: The ConfigMgmt API from Progress Software — 25 operation(s) for configmgmt.
  name: Progress Software Config Mgmt API
  phrasing_intents:
  - id: ConfigMgmt_CreateRollout
    intent: Record a policy rollout
    question: How can a CI job record that a new policy revision is being rolled out to a policy group?
  - id: ConfigMgmt_GetRolloutForChefRun
    intent: Find the rollout matching a policy revision
    question: Which rollout does a given policy name, policy group and revision belong to?
  - id: ConfigMgmt_GetRollouts
    intent: List policy rollouts
    question: What policy rollouts have been recorded so far?
  - id: ConfigMgmt_ListNodeSegmentsWithRolloutProgress
    intent: Show rollout progress by node segment
    question: How far along is each node segment in picking up the latest policy rollout?
  - id: ConfigMgmt_GetRolloutById
    intent: Get a rollout by ID
    question: What are the details of one specific rollout if I have its ID?
  - id: ConfigMgmt_CreateRolloutTest
    intent: Test rollout ingestion connectivity
    question: Is there a no-op call to check my CI client can reach the rollout endpoint with the right auth?
  - id: ConfigMgmt_GetErrors
    intent: List the most common Chef run errors
    question: What are the most common errors on my nodes' latest Chef Infra Client runs?
  - id: ConfigMgmt_GetNodeMetadataCounts
    intent: Count nodes by metadata field value
    question: How many of my infra nodes run each platform?
  phrasing_ops: 25
  slug: progress-software-configmgmt-api
- baseURL: https://automate.chef.io
  baseurl_source: declared
  description: The Contacts API from Progress Software — 2 operation(s) for contacts.
  name: Progress Software Contacts API
  phrasing_intents:
  - id: GETapi/v1/contacts?SearchString={SearchString}&OnBehalfOf={OnBehalfOf}&Page={Page}&PerPage={PerPage}&SortField={SortField}&SortDirection={SortDirection}-1.0
    intent: List and search address book contacts
    question: Which contacts are in my MOVEit Transfer address book?
  - id: POSTapi/v1/contacts-1.0
    intent: Add a new contact
    question: How do I add someone's email to my address book?
  - id: DELETEapi/v1/contacts/{Id}-1.0
    intent: Delete a contact
    question: How do I remove someone from my address book?
  - id: PATCHapi/v1/contacts/{Id}-1.0
    intent: Update a contact's name or email
    question: How do I fix the email address on an existing contact?
  phrasing_ops: 4
  slug: progress-software-contacts-api
- baseURL: https://automate.chef.io
  baseurl_source: declared
  description: The Credential API from Progress Software — 7 operation(s) for credential.
  name: Progress Software Credential API
  phrasing_intents:
  - id: Credential_Get
    intent: Get a credential from the library
    question: How do I look up one credential in the credential library?
  - id: Credential_UpdateCredential
    intent: Update a credential
    question: How do I rename a stored credential or change its properties?
  - id: Credential_DeleteCredential
    intent: Delete a credential from the library
    question: How do I remove a credential from the credential library entirely?
  - id: Credential_GetAssignments
    intent: List devices using a credential
    question: Which devices is a particular credential assigned to?
  - id: Credential_RemoveCredentialFromAllDevice
    intent: Unassign a credential from all devices
    question: How do I detach a credential from every device at once while keeping it in the library?
  - id: Credential_Find
    intent: Search the credential library
    question: What credentials are stored in my credential library?
  - id: Credential_AddCredential
    intent: Add a credential to the library
    question: How do I add a new credential for monitoring devices?
  - id: Credential_GetHelper
    intent: Get help building a Cisco Meraki credential
    question: What information do I need to build a Cisco Meraki credential from an organization API key?
  phrasing_ops: 12
  slug: progress-software-credential-api
- baseURL: https://automate.chef.io
  baseurl_source: declared
  description: The DatafeedService API from Progress Software — 6 operation(s) for datafeedservice.
  name: Progress Software Datafeed Service API
  phrasing_intents:
  - id: DatafeedService_GlobalDataFeedConfig
    intent: Get the global data feed configuration
    question: What are the global data feed settings in Chef Automate?
  - id: DatafeedService_AddDestination
    intent: Add a data feed destination
    question: How do I send Automate node and compliance data to an external webhook URL?
  - id: DatafeedService_EnableDestination
    intent: Turn a data feed destination on or off
    question: How do I pause a data feed destination without deleting it?
  - id: DatafeedService_GetDestination
    intent: Get one data feed destination
    question: Where is a specific data feed destination sending data?
  - id: DatafeedService_DeleteDestination
    intent: Delete a data feed destination
    question: How do I remove a data feed destination entirely?
  - id: DatafeedService_UpdateDestination
    intent: Update a data feed destination
    question: How do I point an existing data feed destination at a new URL?
  - id: DatafeedService_ListDestinations
    intent: List all data feed destinations
    question: Which data feed destinations are configured?
  - id: DatafeedService_TestDestination
    intent: Test connectivity to a data feed destination
    question: Can I check that a webhook URL accepts data before adding it as a destination?
  phrasing_ops: 8
  slug: progress-software-datafeedservice-api
- baseURL: https://automate.chef.io
  baseurl_source: declared
  description: The DataLifecycle API from Progress Software — 15 operation(s) for datalifecycle.
  name: Progress Software Data Lifecycle API
  phrasing_intents:
  - id: DataLifecycle_SetComplianceConfig
    intent: Configure compliance data retention jobs
    question: How do I change how long compliance scan data is kept?
  - id: DataLifecycle_RunCompliance
    intent: Run compliance data lifecycle jobs now
    question: Can I trigger the compliance data cleanup immediately instead of waiting for the schedule?
  - id: DataLifecycle_GetComplianceStatus
    intent: Check compliance lifecycle job status
    question: When did the compliance data purge last run and when is it next?
  - id: DataLifecycle_SetConfig
    intent: Configure all data lifecycle jobs at once
    question: Is there one place to set retention for compliance, event feed, infra and services data together?
  - id: DataLifecycle_SetEventFeedConfig
    intent: Configure event feed data retention jobs
    question: How long are event feed entries retained, and can I change it?
  - id: DataLifecycle_RunEventFeed
    intent: Run event feed data lifecycle jobs now
    question: Can I purge old event feed data immediately?
  - id: DataLifecycle_GetEventFeedStatus
    intent: Check event feed lifecycle job status
    question: What's the status of the event feed purge scheduler?
  - id: DataLifecycle_SetInfraConfig
    intent: Configure infra node data retention jobs
    question: How do I control how long infra data is kept before it is purged?
  phrasing_ops: 15
  slug: progress-software-datalifecycle-api
- baseURL: https://automate.chef.io
  baseurl_source: declared
  description: The Deployment API from Progress Software — 2 operation(s) for deployment.
  name: Progress Software Deployment API
  phrasing_intents:
  - id: Deployment_ServiceVersions
    intent: List versions of each deployed service
    question: Which version of each internal service is my Automate deployment running?
  - id: Deployment_GetVersion
    intent: Get the Automate deployment version
    question: What overall version of Chef Automate is installed?
  phrasing_ops: 2
  slug: progress-software-deployment-api
- baseURL: https://automate.chef.io
  baseurl_source: declared
  description: The Device API from Progress Software — 39 operation(s) for device.
  name: Progress Software Device API
  phrasing_intents:
  - id: Device_GetAttribute
    intent: Get one custom attribute on a device
    question: What value does a single custom attribute hold on one of my WhatsUp Gold devices?
  - id: Device_UpdateAttribute
    intent: Change an existing device attribute
    question: How can I rename or change the value of an attribute already on a device?
  - id: Device_DeleteAttribute
    intent: Delete one attribute from a device
    question: How do I remove a single custom attribute from a device?
  - id: Device_FindAttributes
    intent: List a device's custom attributes
    question: Which custom attributes are set on this device?
  - id: Device_AddAttribute
    intent: Add a new custom attribute to a device
    question: How do I tag a device with a new name/value attribute?
  - id: Device_DeleteAllAttributes
    intent: Clear all or matching attributes from a device
    question: How do I wipe every custom attribute off a device at once?
  - id: Device_BatchAttributes
    intent: Add, change and remove device attributes in one call
    question: Can I add new attributes and delete old ones on a device in a single request?
  - id: Device_DeleteAssignedGroup
    intent: Remove a device from one static group
    question: How do I take a device out of a static device group?
  phrasing_ops: 63
  slug: progress-software-device-api
- baseURL: https://automate.chef.io
  baseurl_source: declared
  description: The DeviceGroupReport API from Progress Software — 12 operation(s) for devicegroupreport.
  name: Progress Software Device Group Report API
  phrasing_intents:
  - id: DeviceGroupReport_DeviceCpuUtilizationReport
    intent: Report CPU utilization for a device group
    question: Which devices in a group are running the hottest CPUs?
  - id: DeviceGroupReport_DeviceDiskFreeSpaceReport
    intent: Report free disk space for a device group
    question: Which servers in a group are running low on free disk space?
  - id: DeviceGroupReport_DeviceDiskUtilizationReport
    intent: Report disk utilization for a device group
    question: What percentage of disk capacity is used across a device group?
  - id: DeviceGroupReport_DeviceInterfaceDiscardsReport
    intent: Report interface discards for a device group
    question: Which interfaces in a group are discarding packets?
  - id: DeviceGroupReport_DeviceInterfaceErrorsReport
    intent: Report interface errors for a device group
    question: Which network interfaces in a group are logging errors?
  - id: DeviceGroupReport_DeviceInterfaceTrafficReport
    intent: Report interface traffic for a device group
    question: How much traffic is flowing through the interfaces in a device group?
  - id: DeviceGroupReport_DeviceInterfaceUtilizationReport
    intent: Report interface utilization for a device group
    question: Which links in a group are close to saturating their bandwidth?
  - id: DeviceGroupReport_DeviceMemoryUtilizationReport
    intent: Report memory utilization for a device group
    question: Which devices in a group are short on memory?
  phrasing_ops: 12
  slug: progress-software-devicegroupreport-api
- baseURL: https://automate.chef.io
  baseurl_source: declared
  description: The DeviceReport API from Progress Software — 11 operation(s) for devicereport.
  name: Progress Software Device Report API
  phrasing_intents:
  - id: DeviceReport_DeviceCpuUtilizationReport
    intent: Report a device's CPU utilization
    question: How busy has a device's CPU been today?
  - id: DeviceReport_DeviceDiskFreeSpaceReport
    intent: Report a device's free disk space
    question: How much free disk space is left on a server?
  - id: DeviceReport_DeviceDiskUtilizationReport
    intent: Report a device's disk utilization
    question: What percentage of each disk is used on a device?
  - id: DeviceReport_DeviceInterfaceDiscardsReport
    intent: Report packet discards on a device's interfaces
    question: Are any network interfaces on a switch discarding packets?
  - id: DeviceReport_DeviceInterfaceErrorsReport
    intent: Report errors on a device's interfaces
    question: Which interfaces on a router are logging errors?
  - id: DeviceReport_DeviceInterfaceTrafficReport
    intent: Report traffic volume on a device's interfaces
    question: How much traffic has gone through each port on a device this week?
  - id: DeviceReport_DeviceInterfaceUtilizationReport
    intent: Report interface utilization percentages on a device
    question: Which interfaces on a device are close to saturating their link capacity?
  - id: DeviceReport_DeviceMemoryUtilizationReport
    intent: Report a device's memory utilization
    question: How much RAM is a device using?
  phrasing_ops: 11
  slug: progress-software-devicereport-api
- baseURL: https://automate.chef.io
  baseurl_source: declared
  description: The DeviceRole API from Progress Software — 14 operation(s) for devicerole.
  name: Progress Software Device Role API
  phrasing_intents:
  - id: DeviceRole_GetSummaryTemplateById
    intent: Get a device role
    question: What does a specific device role in WhatsUp Gold contain?
  - id: DeviceRole_RemoveRoleById
    intent: Delete a device role from the library
    question: How do I remove a custom device role from the library?
  - id: DeviceRole_GetTemplateById
    intent: Get the config template of a device role
    question: Can I export one device role's configuration template for copying to another system?
  - id: DeviceRole_EnableRoleById
    intent: Enable a device role
    question: How do I turn a disabled device role back on?
  - id: DeviceRole_DisableRoleById
    intent: Disable a device role
    question: Can I stop a device role from being used without deleting it?
  - id: DeviceRole_RestoreSystemDefaultsById
    intent: Restore a system role to defaults
    question: How do I reset a built-in device role to its shipped defaults?
  - id: DeviceRole_RoleAssignmentsById
    intent: List devices assigned a role
    question: Which devices is a particular role assigned to?
  - id: DeviceRole_AllRoleAssignments
    intent: List all device role assignments
    question: What roles are assigned to every device across the system?
  phrasing_ops: 16
  slug: progress-software-devicerole-api
- baseURL: https://automate.chef.io
  baseurl_source: declared
  description: The DeviceScan API from Progress Software — 4 operation(s) for devicescan.
  name: Progress Software Device Scan API
  phrasing_intents:
  - id: DeviceScan_UpdatedDevices
    intent: List devices updated by a scan
    question: Which devices were added or changed by a discovery scan?
  - id: DeviceScan_Status
    intent: Get the status of a scan
    question: Is my device scan still running or has it finished?
  - id: DeviceScan_Cancel
    intent: Cancel an active scan
    question: How do I stop a device scan that's taking too long?
  - id: DeviceScan_ListStatus
    intent: List the status of all scans
    question: What device scans are in progress right now?
  phrasing_ops: 4
  slug: progress-software-devicescan-api
- baseURL: https://automate.chef.io
  baseurl_source: declared
  description: The Error API from Progress Software — 1 operation(s) for error.
  name: Progress Software Error API
  phrasing_intents:
  - id: Error_InduceError
    intent: Trigger a test error
    question: Can I deliberately trigger an error to test my client's error handling?
  phrasing_ops: 1
  slug: progress-software-error-api
- baseURL: https://automate.chef.io
  baseurl_source: declared
  description: The EventFeedService API from Progress Software — 4 operation(s) for eventfeedservice.
  name: Progress Software Event Feed Service API
  phrasing_intents:
  - id: EventFeedService_GetEventTaskCounts
    intent: Count create, update and delete actions in events
    question: How many create, update and delete actions happened in Chef Automate this week?
  - id: EventFeedService_GetEventTypeCounts
    intent: Count role, cookbook and organization events
    question: How many cookbook events versus role events were recorded?
  - id: EventFeedService_GetEventFeed
    intent: List recorded events
    question: What changed recently on my Chef Infra Server, like new cookbooks or policyfile updates?
  - id: EventFeedService_GetEventStringBuckets
    intent: Get hourly event summary buckets
    question: What data drives the event timeline graphic above the event feed?
  phrasing_ops: 4
  slug: progress-software-eventfeedservice-api
- baseURL: https://automate.chef.io
  baseurl_source: declared
  description: The Files API from Progress Software — 9 operation(s) for files.
  name: Progress Software Files API
  phrasing_intents:
  - id: GETapi/v1/files/{Id}-1.0
    intent: Get a file's details
    question: How do I see the details of a file stored on the transfer server?
  - id: DELETEapi/v1/files/{Id}-1.0
    intent: Delete a file
    question: How do I delete a file from a folder on the transfer server?
  - id: PATCHapi/v1/files/{Id}-1.0
    intent: Rename a file or change its new flag
    question: How do I rename a file that's already uploaded?
  - id: GETapi/v1/files/{Id}/download-1.0
    intent: Download a file
    question: How do I download the contents of a file from the transfer server?
  - id: GETapi/v1/files/{Id}/newstates?Page={Page}&PerPage={PerPage}&SortField={SortField}&SortDirection={SortDirection}-1.0
    intent: See which users still see a file as new
    question: Which users haven't opened a file yet, so it still shows as new to them?
  - id: POSTapi/v1/files/{Id}/newstates-1.0
    intent: Mark a file as new for a user
    question: How do I flag a file as new again for a specific user?
  - id: GETapi/v1/files?Page={Page}&PerPage={PerPage}&SortField={SortField}&SortDirection={SortDirection}&NewOnly={NewOnly}&SinceDate={SinceDate}-1.0
    intent: List files I can view
    question: What files do I have access to on the transfer server?
  - id: GETapi/v1/files/detailed?PathMask={PathMask}&FileMask={FileMask}&Recursive={Recursive}&NewOnly={NewOnly}&SortField={SortField}&SortDirection={SortDirection}&SinceDate={SinceDate}-1.0
    intent: Find files by wildcard path and file mask
    question: How do I find every *.csv file under a folder path using wildcards?
  phrasing_ops: 12
  slug: progress-software-files-api
- baseURL: https://automate.chef.io
  baseurl_source: declared
  description: The FolderContent API from Progress Software — 6 operation(s) for foldercontent.
  name: Progress Software Folder Content API
  phrasing_intents:
  - id: GETapi/v1/folders/{folderId}/files/{fileId}-1.0
    intent: Get details of a file in a folder
    question: What are the details of a file stored in a folder?
  - id: GETapi/v1/folders/{folderId}/files/{fileId}/download-1.0
    intent: Download a file from a folder
    question: How do I download a file from a folder?
  - id: GETapi/v1/folders/{parentId}/subfolders/{subfolderId}-1.0
    intent: Get subfolder details
    question: What are the details of a subfolder inside a parent folder?
  - id: DELETEapi/v1/folders/{parentId}/subfolders/{subfolderId}-1.0
    intent: Delete a subfolder
    question: How do I delete a subfolder from its parent?
  - id: GETapi/v1/folders/{Id}/subfolders?Page={Page}&PerPage={PerPage}&SortField={SortField}&SortDirection={SortDirection}&Name={Name}-1.0
    intent: List subfolders of a folder
    question: Which subfolders are inside a folder?
  - id: POSTapi/v1/folders/{Id}/subfolders-1.0
    intent: Create a subfolder
    question: How do I create a new folder inside an existing one?
  - id: GETapi/v1/folders/{Id}/files?Page={Page}&PerPage={PerPage}&SortField={SortField}&SortDirection={SortDirection}&Name={Name}&NewOnly={NewOnly}-1.0
    intent: List files in a folder
    question: What files are in a folder?
  - id: POSTapi/v1/folders/{Id}/files?UploadType={UploadType}&PathHash={PathHash}-1.0
    intent: Upload a file into a folder
    question: How do I upload a file to a MOVEit folder?
  phrasing_ops: 9
  slug: progress-software-foldercontent-api
- baseURL: https://automate.chef.io
  baseurl_source: declared
  description: The Folders API from Progress Software — 11 operation(s) for folders.
  name: Progress Software Folders API
  phrasing_intents:
  - id: GETapi/v1/folders-1.0
    intent: List folders I can view
    question: Which MOVEit folders do I have access to?
  - id: GETapi/v1/folders/{Id}?SkipCounts={SkipCounts}&SkipFilesSize={SkipFilesSize}&PathHash={PathHash}-1.0
    intent: Get folder details
    question: What are the settings and size of a specific folder?
  - id: DELETEapi/v1/folders/{Id}?PathHash={PathHash}-1.0
    intent: Delete a folder
    question: How do I delete an entire folder?
  - id: PATCHapi/v1/folders/{Id}-1.0
    intent: Rename or describe a folder
    question: How can I rename a folder or change its description?
  - id: GETapi/v1/folders/{Id}/acls?Page={Page}&PerPage={PerPage}&SortField={SortField}&SortDirection={SortDirection}&PathHash={PathHash}-1.0
    intent: List a folder's access controls
    question: Who has permissions on a particular folder?
  - id: PUTapi/v1/folders/{Id}/acls-1.0
    intent: Change a folder access control entry
    question: Can I change permissions on a folder and override inherited behaviour?
  - id: POSTapi/v1/folders/{Id}/acls-1.0
    intent: Grant access to a folder
    question: How do I give a user or group access to a folder?
  - id: DELETEapi/v1/folders/{Id}/acls-1.0
    intent: Revoke access to a folder
    question: How do I remove someone's access to a folder?
  phrasing_ops: 16
  slug: progress-software-folders-api
- baseURL: https://automate.chef.io
  baseurl_source: declared
  description: The Gateway API from Progress Software — 2 operation(s) for gateway.
  name: Progress Software Gateway API
  phrasing_intents:
  - id: Gateway_GetHealth
    intent: Check the gateway's health
    question: Is the Chef Automate gateway healthy?
  - id: Gateway_GetVersion
    intent: Get the gateway version
    question: Which version of the gateway is running?
  phrasing_ops: 2
  slug: progress-software-gateway-api
- baseURL: https://automate.chef.io
  baseurl_source: declared
  description: The Groups API from Progress Software — 3 operation(s) for groups.
  name: Progress Software Groups API
  phrasing_intents:
  - id: GETapi/v1/groups?Page={Page}&PerPage={PerPage}-1.0
    intent: List user groups I can view
    question: Which MOVEit Transfer user groups can I see?
  - id: POSTapi/v1/groups-1.0
    intent: Create a user group
    question: How do I create a new group to organize users?
  - id: GETapi/v1/groups/{Id}/members?Page={Page}&PerPage={PerPage}-1.0
    intent: List the members of a group
    question: Who is in a particular group?
  - id: POSTapi/v1/groups/{Id}/members-1.0
    intent: Add users to a group
    question: How do I add several users to a group at once?
  - id: DELETEapi/v1/groups/{Id}/members/{UserId}-1.0
    intent: Remove a user from a group
    question: How do I take a user out of a group?
  phrasing_ops: 5
  slug: progress-software-groups-api
- baseURL: https://automate.chef.io
  baseurl_source: declared
  description: The InfraProxy API from Progress Software — 36 operation(s) for infraproxy.
  name: Progress Software Infra Proxy API
  phrasing_intents:
  - id: InfraProxy_GetServers
    intent: List registered infra servers
    question: Which Chef Infra Servers have been added to Automate's infra proxy?
  - id: InfraProxy_CreateServer
    intent: Register a new infra server
    question: How do I add a new Chef Infra Server so Automate can manage it?
  - id: InfraProxy_GetServerStatus
    intent: Check an infra server's reachability status
    question: Is my Chef Infra Server at a given FQDN up and reachable?
  - id: InfraProxy_GetServer
    intent: Get one infra server's details
    question: What FQDN and IP address are stored for a particular infra server?
  - id: InfraProxy_UpdateServer
    intent: Update an infra server's connection details
    question: How do I change the FQDN of an infra server I already registered?
  - id: InfraProxy_DeleteServer
    intent: Remove an infra server
    question: How do I remove an infra server from Automate's infra proxy?
  - id: InfraProxy_GetOrgs
    intent: List organizations on an infra server
    question: Which Chef organizations are attached to a given infra server?
  - id: InfraProxy_CreateOrg
    intent: Add an organization to an infra server
    question: How do I connect a Chef organization to an infra server in Automate?
  phrasing_ops: 57
  slug: progress-software-infraproxy-api
- baseURL: https://automate.chef.io
  baseurl_source: declared
  description: The JobsService API from Progress Software — 4 operation(s) for jobsservice.
  name: Progress Software Jobs Service API
  phrasing_intents:
  - id: JobsService_Create
    intent: Create a compliance scan job
    question: How do I schedule an InSpec scan of my nodes against compliance profiles?
  - id: JobsService_Read
    intent: Get a scan job's details
    question: What nodes and profiles does a specific scan job target?
  - id: JobsService_Update
    intent: Update a scan job
    question: How do I change the profiles or recurrence of an existing scan job?
  - id: JobsService_Delete
    intent: Delete a scan job
    question: How do I delete a scan job I no longer need?
  - id: JobsService_Rerun
    intent: Rerun an existing scan job
    question: Can I run a scan job again right now without creating a new one?
  - id: JobsService_List
    intent: Search and list scan jobs
    question: Which compliance scan jobs exist, and which ones failed?
  phrasing_ops: 6
  slug: progress-software-jobsservice-api
- baseURL: https://automate.chef.io
  baseurl_source: declared
  description: The LegacyDataCollector API from Progress Software — 1 operation(s) for legacydatacollector.
  name: Progress Software Legacy Data Collector API
  phrasing_intents:
  - id: LegacyDataCollector_Status
    intent: Check the legacy data collector endpoint
    question: How does a Chef server check that Automate's data collector is reachable?
  phrasing_ops: 1
  slug: progress-software-legacydatacollector-api
- baseURL: https://automate.chef.io
  baseurl_source: declared
  description: The License API from Progress Software — 3 operation(s) for license.
  name: Progress Software License API
  phrasing_intents:
  - id: License_ApplyLicense
    intent: Apply a license
    question: How do I install a license key in Chef Automate?
  - id: License_RequestLicense
    intent: Request a trial license
    question: How do I request a trial license with my name and email?
  - id: License_GetStatus
    intent: Get license status
    question: What's the status of my current license?
  phrasing_ops: 3
  slug: progress-software-license-api
- baseURL: https://automate.chef.io
  baseurl_source: declared
  description: The Logs API from Progress Software — 2 operation(s) for logs.
  name: Progress Software Logs API
  phrasing_intents:
  - id: GETapi/v1/logs/{Id}-1.0
    intent: Get one audit log entry
    question: What are the full details of a single log entry?
  - id: GETapi/v1/logs?Page={Page}&PerPage={PerPage}&SortField={SortField}&SortDirection={SortDirection}&StartDateTime={StartDateTime}&EndDateTime={EndDateTime}&Action={Action}&UserNameContains={UserNameContains}&UserId={UserId}&FileIdContains={FileIdContains}&FileNameContains={FileNameContains}&SizeComparison={SizeComparison}&Size={Size}&FolderId={FolderId}&FolderPathContains={FolderPathContains}&IpContains={IpContains}&AgentBrandContains={AgentBrandContains}&SuccessFailure={SuccessFailure}&SuppressSigns={SuppressSigns}&SuppressEmailNotes={SuppressEmailNotes}&SuppressLogViews={SuppressLogViews}-1.0
    intent: Search the audit logs
    question: Who downloaded a particular file from MOVEit Transfer last week?
  phrasing_ops: 2
  slug: progress-software-logs-api
- baseURL: https://automate.chef.io
  baseurl_source: declared
  description: The Mailboxes API from Progress Software — 6 operation(s) for mailboxes.
  name: Progress Software Mailboxes API
  phrasing_intents:
  - id: GETapi/v1/mailboxes-1.0
    intent: List my mailboxes
    question: Which MOVEit Transfer mailboxes do I have, like inbox, sent and trash?
  - id: GETapi/v1/mailboxes/{Id}-1.0
    intent: Get details of one mailbox
    question: What information is available about a single mailbox?
  - id: GETapi/v1/mailboxes/{Id}/packages-1.0
    intent: List the packages in a mailbox
    question: What packages are sitting in my inbox?
  - id: POSTapi/v1/mailboxes/{Id}/packages-1.0
    intent: Move a package to another mailbox
    question: How do I move a package from my inbox into another mailbox?
  - id: GETapi/v1/mailboxes/{Id}/packages/{PackageId}?Action={Action}-1.0
    intent: Get a package's details
    question: What files and message does a specific package contain?
  - id: DELETEapi/v1/mailboxes/{Id}/packages/{packageId}-1.0
    intent: Remove a package from a mailbox
    question: How do I delete a package from my mailbox?
  - id: PATCHapi/v1/mailboxes/{Id}/packages/{packageId}-1.0
    intent: Recall a package or mark it read or unread
    question: How do I recall a package I already sent?
  - id: DELETEapi/v1/mailboxes/trash-1.0
    intent: Empty the trash mailbox
    question: How do I permanently empty my trash?
  phrasing_ops: 8
  slug: progress-software-mailboxes-api
- baseURL: https://automate.chef.io
  baseurl_source: declared
  description: The MiscellaneousSettings API from Progress Software — 1 operation(s) for miscellaneoussettings.
  name: Progress Software Miscellaneous Settings API
  phrasing_intents:
  - id: POSTapi/v1/settings/miscellaneous/aging/logs-1.0
    intent: Change audit log retention and archiving
    question: How long are MOVEit Transfer audit logs kept, and can I change it?
  phrasing_ops: 1
  slug: progress-software-miscellaneoussettings-api
- baseURL: https://automate.chef.io
  baseurl_source: declared
  description: The Monitor API from Progress Software — 7 operation(s) for monitor.
  name: Progress Software Monitor API
  phrasing_intents:
  - id: Monitor_MonitorAssignmentsById
    intent: List the devices one monitor is assigned to
    question: Which devices is a specific monitor currently assigned to?
  - id: Monitor_DeleteMonitorAssignmentsById
    intent: Unassign one monitor from its devices
    question: How do I remove a monitor from every device it's assigned to without deleting the monitor itself?
  - id: Monitor_MonitorAssignments
    intent: List monitor assignments across all monitors
    question: What monitor assignments are active across all my devices?
  - id: Monitor_DeleteMonitorAssignmentsByQuery
    intent: Bulk-remove monitor assignments by search
    question: How can I strip every assignment for monitors matching a search term in one call?
  - id: Monitor_GetById
    intent: Get one monitor from the library
    question: What is configured on a specific monitor in WhatsUp Gold's library?
  - id: Monitor_UpdateMonitorById
    intent: Update a monitor's configuration
    question: How do I change the configuration properties of an existing monitor?
  - id: Monitor_DeleteMonitorById
    intent: Delete a monitor from the library
    question: How do I delete one monitor from the library?
  - id: Monitor_GetAll
    intent: List monitors in the library
    question: Which monitors are in my library, and can I include device-specific ones?
  phrasing_ops: 15
  slug: progress-software-monitor-api
- baseURL: https://automate.chef.io
  baseurl_source: declared
  description: The NodeManagerService API from Progress Software — 9 operation(s) for nodemanagerservice.
  name: Progress Software Node Manager Service API
  phrasing_intents:
  - id: NodeManagerService_Create
    intent: Create a node manager
    question: How do I connect a cloud account to Chef Automate as a node manager?
  - id: NodeManagerService_Read
    intent: View a node manager's details
    question: What type and status does a given node manager have?
  - id: NodeManagerService_Update
    intent: Replace a node manager's settings
    question: How do I rotate the credential a node manager uses?
  - id: NodeManagerService_Delete
    intent: Delete a node manager and keep its nodes
    question: What happens to nodes when I delete their node manager?
  - id: NodeManagerService_DeleteWithNodeStateStopped
    intent: Delete a node manager and mark its nodes stopped
    question: Can I delete a node manager and set all its nodes to stopped?
  - id: NodeManagerService_DeleteWithNodeStateTerminated
    intent: Delete a node manager and mark its nodes terminated
    question: Can I delete a node manager and flag all its nodes as terminated?
  - id: NodeManagerService_DeleteWithNodes
    intent: Delete a node manager and all of its nodes
    question: How do I delete a node manager together with every node it manages?
  - id: NodeManagerService_SearchNodeFields
    intent: Look up field values across a node manager's nodes
    question: What distinct values does a field like region take across a node manager's nodes?
  phrasing_ops: 11
  slug: progress-software-nodemanagerservice-api
- baseURL: https://automate.chef.io
  baseurl_source: declared
  description: The NodesService API from Progress Software — 7 operation(s) for nodesservice.
  name: Progress Software Nodes Service API
  phrasing_intents:
  - id: NodesService_Create
    intent: Add a node to Chef Automate
    question: How do I register a single server as a node in Chef Automate?
  - id: NodesService_BulkCreate
    intent: Add many nodes in one request
    question: Can I add a list of hosts as nodes all at once?
  - id: NodesService_BulkDelete
    intent: Delete all nodes matching a filter
    question: How do I delete every node from a particular node manager?
  - id: NodesService_BulkDeleteById
    intent: Delete several nodes by ID
    question: Can I delete a specific list of nodes by their IDs?
  - id: NodesService_Read
    intent: Show a node's details
    question: What platform, status and last contact time does a node have?
  - id: NodesService_Update
    intent: Replace a node's details
    question: How do I change a node's name or connection settings?
  - id: NodesService_Delete
    intent: Delete a single node
    question: How do I remove one node from Chef Automate?
  - id: NodesService_Rerun
    intent: Recheck whether a node is reachable
    question: How do I re-test whether a node is reachable?
  phrasing_ops: 9
  slug: progress-software-nodesservice-api
- baseURL: https://automate.chef.io
  baseurl_source: declared
  description: The Notifications API from Progress Software — 4 operation(s) for notifications.
  name: Progress Software Notifications API
  phrasing_intents:
  - id: Notifications_ListRules
    intent: List notification rules
    question: What notification rules are set up in Chef Automate?
  - id: Notifications_AddRule
    intent: Create a notification rule
    question: How do I set up a notification for failed runs or compliance failures?
  - id: Notifications_GetRule
    intent: Get a notification rule
    question: What does a specific notification rule do?
  - id: Notifications_UpdateRule
    intent: Update a notification rule
    question: How do I change an existing notification rule?
  - id: Notifications_DeleteRule
    intent: Delete a notification rule
    question: How do I stop an alert from firing permanently?
  - id: Notifications_Version
    intent: Get the notifications service version
    question: What version of the notifications service is running?
  - id: Notifications_ValidateWebhook
    intent: Test a notification webhook
    question: Can I check that a webhook URL works before using it in a rule?
  phrasing_ops: 7
  slug: progress-software-notifications-api
- baseURL: https://automate.chef.io
  baseurl_source: declared
  description: The Organizations API from Progress Software — 7 operation(s) for organizations.
  name: Progress Software Organizations API
  phrasing_intents:
  - id: GETapi/v1/organizations/{OrgId}-1.0
    intent: Get an organization's details
    question: How do I see the full settings of one organization on the transfer server?
  - id: GETapi/v1/organizations?Page={Page}&PerPage={PerPage}&SortField={SortField}&SortDirection={SortDirection}-1.0
    intent: List organizations
    question: Which organizations exist on the transfer server?
  - id: POSTapi/v1/organizations-1.0
    intent: Create an organization
    question: How do I create a new organization with its own passphrase?
  - id: POSTapi/v1/organizations/{orgId}/maxusercounts-1.0
    intent: Set an organization's maximum user counts
    question: How do I cap the number of users an organization can have?
  - id: POSTapi/v1/organizations/{orgId}/packageaccess-1.0
    intent: Set administrator package access for an org
    question: Can administrators read users' packages in an organization, and how do I change that?
  - id: POSTapi/v1/organizations/{orgId}/passwordreset-1.0
    intent: Toggle admin password reset for an org
    question: How do I let administrators reset their own passwords in an organization?
  - id: POSTapi/v1/organizations/{orgId}/interfaceconfiguration-1.0
    intent: Configure which UI features an org shows
    question: How do I hide files and folders from users in an organization's web interface?
  - id: PATCHapi/v1/organizations/{orgId}-1.0
    intent: Edit an organization's general info
    question: How do I rename an organization or change its short name?
  phrasing_ops: 8
  slug: progress-software-organizations-api
- baseURL: https://automate.chef.io
  baseurl_source: declared
  description: The Packages API from Progress Software — 7 operation(s) for packages.
  name: Progress Software Packages API
  phrasing_intents:
  - id: GETapi/v1/packages-1.0
    intent: List packages I can view
    question: Which secure packages have been sent to me or that I've sent?
  - id: POSTapi/v1/packages-1.0
    intent: Send or save a secure package
    question: How do I send a secure package with file attachments to a recipient?
  - id: GETapi/v1/packages/requirements-1.0
    intent: Get the rules a new package must meet
    question: What requirements must a package satisfy before I can send it?
  - id: GETapi/v1/packages/{Id}/recipients?MailboxId={MailboxId}-1.0
    intent: Get a package's recipients
    question: Who was a package sent to?
  - id: GETapi/v1/packages/{Id}?Action={Action}&MailboxId={MailboxId}-1.0
    intent: Get a package's details
    question: How do I open a package and see its subject, note and attachments?
  - id: DELETEapi/v1/packages/{Id}?MailboxId={MailboxId}-1.0
    intent: Remove a package from my mailboxes
    question: How do I delete a package from my mailbox?
  - id: PATCHapi/v1/packages/{Id}-1.0
    intent: Recall a package or change its new flag
    question: Can I recall a package I sent by mistake?
  - id: GETapi/v1/packages/{Id}/notification?IncludeImages={IncludeImages}&MailboxId={MailboxId}-1.0
    intent: Get a package's notification message
    question: What does the notification email for a package look like?
  phrasing_ops: 10
  slug: progress-software-packages-api
- baseURL: https://automate.chef.io
  baseurl_source: declared
  description: A policy defines permissions for who may perform what action on which resources, based on the project. The 'who' is a user, a team, or a system. A policy has three components, the agent, the action, a
  name: Progress Software Policies API
  phrasing_intents:
  - id: Policies_ListPolicies
    intent: List IAM policies
    question: Which IAM policies exist in my Chef Automate install?
  - id: Policies_CreatePolicy
    intent: Create a custom IAM policy
    question: How do I create a policy that grants a team a role on specific projects?
  - id: Policies_GetPolicy
    intent: Get one IAM policy
    question: What statements and members are on a specific policy?
  - id: Policies_UpdatePolicy
    intent: Overwrite a custom IAM policy
    question: How do I change the statements on an existing custom policy?
  - id: Policies_DeletePolicy
    intent: Delete a custom IAM policy
    question: How do I delete a custom access policy?
  - id: Policies_ListPolicyMembers
    intent: List the members of a policy
    question: Which users, teams and tokens are members of a given policy?
  - id: Policies_ReplacePolicyMembers
    intent: Replace a policy's entire member list
    question: How do I swap out the whole member list of a policy in one call?
  - id: Policies_AddPolicyMembers
    intent: Add members to a policy
    question: How do I grant a new team access by adding it to an existing policy?
  phrasing_ops: 10
  slug: progress-software-policies-api
- baseURL: https://automate.chef.io
  baseurl_source: declared
  description: The Pollers API from Progress Software — 3 operation(s) for pollers.
  name: Progress Software Pollers API
  phrasing_intents:
  - id: Pollers_GetAllPollers
    intent: List pollers and their status
    question: Which pollers are configured and are they healthy?
  - id: Pollers_CreatePoller
    intent: Create a poller
    question: How do I add a new poller and assign devices to it?
  - id: Pollers_GetPollerById
    intent: Get one poller
    question: What devices and subnets is a specific poller handling?
  - id: Pollers_UpdatePoller
    intent: Update a poller's configuration
    question: How do I move devices onto an existing poller?
  - id: deleteApiV1PollersByPollerId
    intent: Remove a poller
    question: How do I delete a poller I no longer need?
  - id: Pollers_CreatePollerWithName
    intent: Get or create a poller by name
    question: Is there a way to ensure a poller with a given name exists without creating a duplicate?
  phrasing_ops: 6
  slug: progress-software-pollers-api
- baseURL: https://automate.chef.io
  baseurl_source: declared
  description: The Product API from Progress Software — 5 operation(s) for product.
  name: Progress Software Product API
  phrasing_intents:
  - id: Product_ApiVersion
    intent: Get the API version
    question: What version of the WhatsUp Gold REST API am I talking to?
  - id: Product_ProductVersion
    intent: Get the product version
    question: Which product version is installed on the server?
  - id: Product_WhoAmI
    intent: Get the current user
    question: Which user am I authenticated as?
  - id: Product_InstallationId
    intent: Get the installation ID
    question: Is there an ID that uniquely identifies this install?
  - id: Product_GetLocalTimezone
    intent: Get the server's local time zone
    question: What time zone is the server set to?
  phrasing_ops: 5
  slug: progress-software-product-api
- baseURL: https://automate.chef.io
  baseurl_source: declared
  description: The ProfilesService API from Progress Software — 7 operation(s) for profilesservice.
  name: Progress Software Profiles Service API
  phrasing_intents:
  - id: ProfilesService_ReadFromMarket
    intent: Show an available market compliance profile
    question: What controls are in a compliance profile I haven't installed yet?
  - id: Create
    intent: Upload or install a compliance profile
    question: How do I upload my own InSpec profile tarball to Chef Automate?
  - id: ProfilesService_MetaSearch
    intent: Check which profiles lack stored metadata
    question: Which of these profile checksums are missing metadata in the backend?
  - id: ProfilesService_Read
    intent: Show an installed compliance profile
    question: What does a profile I've already installed contain?
  - id: ProfilesService_List
    intent: List compliance profiles
    question: Which compliance profiles are available in the market?
  - id: ReadTar
    intent: Download a compliance profile as a tarball
    question: How do I download a profile to my workstation as a tarball?
  - id: ProfilesService_Delete
    intent: Uninstall a compliance profile
    question: How do I uninstall a profile from a user's namespace?
  phrasing_ops: 7
  slug: progress-software-profilesservice-api
- baseURL: https://automate.chef.io
  baseurl_source: declared
  description: Projects are used to group and permission Chef Automate resources as well as ingested data, specifically Compliance reports, Chef Infra Server events, and Infrastructure nodes.
  name: Progress Software Projects API
  phrasing_intents:
  - id: Policies_ListProjects
    intent: List IAM projects
    question: Which IAM projects exist for scoping permissions?
  - id: Policies_CreateProject
    intent: Create an IAM project
    question: How do I create a project to scope resources in my IAM policies?
  - id: Policies_GetProject
    intent: Get an IAM project
    question: How do I look up a single IAM project's details?
  - id: Policies_UpdateProject
    intent: Rename an IAM project
    question: How do I rename an existing IAM project?
  - id: Policies_DeleteProject
    intent: Delete an IAM project
    question: What happens to policies and resources when I delete a project?
  phrasing_ops: 5
  slug: progress-software-projects-api
- baseURL: https://automate.chef.io
  baseurl_source: declared
  description: The PublicOrganizationInfo API from Progress Software — 1 operation(s) for publicorganizationinfo.
  name: Progress Software Public Organization Info API
  phrasing_intents:
  - id: GETapi/v1/info?orgId={orgId}&language={language}-1.0
    intent: Get an organization's public info
    question: What public details does a MOVEit Transfer organization expose before sign-in?
  phrasing_ops: 1
  slug: progress-software-publicorganizationinfo-api
- baseURL: https://automate.chef.io
  baseurl_source: declared
  description: The ReportingService API from Progress Software — 14 operation(s) for reportingservice.
  name: Progress Software Reporting Service API
  phrasing_intents:
  - id: ReportingService_ListControlItems
    intent: List compliance controls from last run
    question: Which compliance controls ran in the latest scans?
  - id: ReportingService_ListControlItemsRange
    intent: Search control summaries over a date range
    question: Can I get control summaries across a date range instead of just the last run?
  - id: Export
    intent: Export compliance reports
    question: How do I export all compliance reports as CSV?
  - id: NodeExport
    intent: Export one node's compliance history
    question: Can I export the historical compliance reports for a single node?
  - id: ReportingService_ReadNodeHeader
    intent: Show node header info for a report
    question: What node and metadata details are attached to a given compliance report?
  - id: ReportingService_ReadNode
    intent: Show a compliance node by ID
    question: What does compliance know about one specific node?
  - id: ReportingService_ListNodes
    intent: List compliance-scanned nodes
    question: Which nodes have compliance scan results?
  - id: ReportingService_ListProfiles
    intent: List compliance profiles in use
    question: Which compliance profiles are being used in scans?
  phrasing_ops: 14
  slug: progress-software-reportingservice-api
- baseURL: https://automate.chef.io
  baseurl_source: declared
  description: The ReportManagerService API from Progress Software — 1 operation(s) for reportmanagerservice.
  name: Progress Software Report Manager Service API
  phrasing_intents:
  - id: ReportManagerService_ListDownloadReportRequests
    intent: List my report download requests
    question: What report download requests have I placed?
  phrasing_ops: 1
  slug: progress-software-reportmanagerservice-api
- baseURL: https://automate.chef.io
  baseurl_source: declared
  description: The Reports API from Progress Software — 3 operation(s) for reports.
  name: Progress Software Reports API
  phrasing_intents:
  - id: GETapi/v1/reports/{Id}/results/download?Format={Format}-1.0
    intent: Download a report's run results
    question: How do I download the results of a report run?
  - id: GETapi/v1/reports?Page={Page}&PerPage={PerPage}&SortField={SortField}&SortDirection={SortDirection}-1.0
    intent: List reports I can view
    question: Which reports am I allowed to view?
  - id: POSTapi/v1/reports/import-1.0
    intent: Import a custom report from a file
    question: How do I create a custom report by uploading a report definition file?
  phrasing_ops: 3
  slug: progress-software-reports-api
- baseURL: https://automate.chef.io
  baseurl_source: declared
  description: The retention API from Progress Software — 4 operation(s) for retention.
  name: Progress Software Retention API
  phrasing_intents:
  - id: ApplicationsService_GetDeleteDisconnectedServicesConfig
    intent: Show the delete-disconnected-services job config
    question: After how long are disconnected services automatically deleted?
  - id: ApplicationsService_UpdateDeleteDisconnectedServicesConfig
    intent: Change the delete-disconnected-services job config
    question: How do I change how long disconnected services stay before they're deleted?
  - id: ApplicationsService_RunDeleteDisconnectedServicesJob
    intent: Run the delete-disconnected-services job now
    question: Can I run the scheduled cleanup of disconnected services right now?
  - id: ApplicationsService_GetDisconnectedServicesConfig
    intent: Show the mark-disconnected-services job config
    question: How long can a service go without reporting before it's marked disconnected?
  - id: ApplicationsService_UpdateDisconnectedServicesConfig
    intent: Change the mark-disconnected-services job config
    question: How do I change the period after which silent services are marked disconnected?
  - id: ApplicationsService_RunDisconnectedServicesJob
    intent: Run the mark-disconnected-services job now
    question: Can I run the check that marks services as disconnected right away?
  phrasing_ops: 6
  slug: progress-software-retention-api
- baseURL: https://automate.chef.io
  baseurl_source: declared
  description: A role encapsulates a list of actions. Chef Automate provides several default Chef-managed roles that cannot be altered but you may also define and use your own Custom roles.
  name: Progress Software Roles API
  phrasing_intents:
  - id: Policies_ListRoles
    intent: List IAM roles
    question: Which roles exist in Chef Automate, both built-in and custom?
  - id: Policies_CreateRole
    intent: Create a custom IAM role
    question: How do I define a custom role with a specific set of actions?
  - id: Policies_GetRole
    intent: Get one IAM role
    question: What actions does a particular role grant?
  - id: Policies_UpdateRole
    intent: Replace a custom role's actions or name
    question: How do I change the actions a custom role allows?
  - id: Policies_DeleteRole
    intent: Delete a custom IAM role
    question: How do I delete a custom role I created?
  phrasing_ops: 5
  slug: progress-software-roles-api
- baseURL: https://automate.chef.io
  baseurl_source: declared
  description: Project rules define lists of one or more conditions that an ingested resource must meet in order to be assigned to a project.
  name: Progress Software Rules API
  phrasing_intents:
  - id: Rules_ApplyRulesStatus
    intent: Check the progress of a project update
    question: How far along is the project update that applies my rule changes?
  - id: Rules_ApplyRulesStart
    intent: Apply staged project rule changes
    question: How do I make my staged project rule edits take effect?
  - id: Rules_ApplyRulesCancel
    intent: Cancel an in-progress project update
    question: Can I stop a project update I just started because I forgot a rule change?
  - id: Rules_ListRulesForProject
    intent: List a project's ingest rules
    question: Which rules decide what resources land in a given project?
  - id: Rules_CreateRule
    intent: Create a project rule
    question: How do I automatically move nodes from a certain Chef server into a project?
  - id: Rules_GetRule
    intent: Get one project rule
    question: What conditions does a specific project rule use?
  - id: Rules_UpdateRule
    intent: Update a project rule's name and conditions
    question: How do I change the conditions on an existing project rule?
  - id: Rules_DeleteRule
    intent: Delete a project rule
    question: How do I delete a project rule that's misrouting resources?
  phrasing_ops: 8
  slug: progress-software-rules-api
- baseURL: https://automate.chef.io
  baseurl_source: declared
  description: The SecretsService API from Progress Software — 3 operation(s) for secretsservice.
  name: Progress Software Secrets Service API
  phrasing_intents:
  - id: SecretsService_Create
    intent: Store a new credential secret
    question: How do I save SSH credentials so compliance scans can log into nodes?
  - id: SecretsService_Read
    intent: Get a secret's metadata
    question: Can I view a stored secret's name and type?
  - id: SecretsService_Delete
    intent: Delete a secret
    question: How do I delete stored credentials?
  - id: SecretsService_Update
    intent: Update part of a secret
    question: How do I change just the password on a stored credential?
  - id: SecretsService_List
    intent: Search and list secrets
    question: Which credentials are stored, and can I filter them by type?
  phrasing_ops: 5
  slug: progress-software-secretsservice-api
- baseURL: https://automate.chef.io
  baseurl_source: declared
  description: The service_groups API from Progress Software — 9 operation(s) for service_groups.
  name: Progress Software Service Groups API
  phrasing_intents:
  - id: ApplicationsService_DeleteDisconnectedServices
    intent: Delete disconnected services past a threshold
    question: How do I remove services that have been disconnected longer than a set number of seconds?
  - id: ApplicationsService_DeleteServicesByID
    intent: Delete specific services by ID
    question: How do I delete particular services from the applications view by their IDs?
  - id: ApplicationsService_GetDisconnectedServices
    intent: Mark services disconnected after a threshold
    question: How do I flag services as disconnected when they haven't reported within some seconds?
  - id: ApplicationsService_GetServiceGroups
    intent: List service groups with health
    question: Which service groups are running and how healthy are they?
  - id: ApplicationsService_GetServicesBySG
    intent: List the services in a service group
    question: What services make up a particular service group?
  - id: ApplicationsService_GetServiceGroupsHealthCounts
    intent: Count service groups by health status
    question: How many service groups are critical, warning, ok or unknown?
  - id: ApplicationsService_GetServices
    intent: List all services with health
    question: What is the health status of every service across all groups?
  - id: ApplicationsService_GetServicesDistinctValues
    intent: List possible filter values for a service field
    question: What values can I filter services by for a given field, like environment?
  phrasing_ops: 9
  slug: progress-software-service-groups-api
- baseURL: https://automate.chef.io
  baseurl_source: declared
  description: The StatsService API from Progress Software — 6 operation(s) for statsservice.
  name: Progress Software Stats Service API
  phrasing_intents:
  - id: StatsService_ReadFailures
    intent: Get the top compliance failures
    question: Which platforms or environments are failing compliance the most?
  - id: StatsService_GetNodesUsageCount
    intent: Count unique nodes for telemetry
    question: How many unique nodes have run since compliance telemetry was last sent?
  - id: StatsService_UpdateTelemetryReported
    intent: Record when compliance telemetry was reported
    question: How do I acknowledge that compliance telemetry was sent?
  - id: StatsService_ReadProfiles
    intent: Get compliance stats per profile
    question: How are my compliance profiles performing across scanned nodes?
  - id: StatsService_ReadSummary
    intent: Get a compliance report summary
    question: What's the overall compliance summary across my nodes?
  - id: StatsService_ReadTrend
    intent: Get compliance trend over time
    question: Is compliance on my nodes getting better or worse over time?
  phrasing_ops: 6
  slug: progress-software-statsservice-api
- baseURL: https://automate.chef.io
  baseurl_source: declared
  description: Teams are used to group local users for policy membership.
  name: Progress Software Teams API
  phrasing_intents:
  - id: Teams_ListTeams
    intent: List local teams
    question: What local teams exist in Chef Automate?
  - id: Teams_CreateTeam
    intent: Create a local team
    question: How do I create a team to group users for IAM policies?
  - id: Teams_GetTeam
    intent: Get a team
    question: What are the details of a specific team?
  - id: Teams_UpdateTeam
    intent: Update a local team
    question: How do I rename a team?
  - id: Teams_DeleteTeam
    intent: Delete a local team
    question: Does deleting a team remove it from policies?
  - id: Teams_GetTeamMembership
    intent: List a team's members
    question: Who is on a particular team?
  - id: Teams_AddTeamMembers
    intent: Add users to a team
    question: How do I add users to a team?
  - id: Teams_RemoveTeamMembers
    intent: Remove users from a team
    question: How do I take users off a team?
  phrasing_ops: 9
  slug: progress-software-teams-api
- baseURL: https://automate.chef.io
  baseurl_source: declared
  description: The Telemetry API from Progress Software — 1 operation(s) for telemetry.
  name: Progress Software Telemetry API
  phrasing_intents:
  - id: Telemetry_GetTelemetryConfiguration
    intent: Get the telemetry configuration
    question: Is telemetry enabled on my Chef Automate install?
  phrasing_ops: 1
  slug: progress-software-telemetry-api
- baseURL: https://automate.chef.io
  baseurl_source: declared
  description: Tokens are used for API access to Automate endpoints as well as by systems (e.g. Chef Infra Servers) to communicate with Automate.
  name: Progress Software Tokens API
  phrasing_intents:
  - id: Tokens_ListTokens
    intent: List API tokens
    question: What API tokens exist, including admin ones?
  - id: Tokens_CreateToken
    intent: Create an API token
    question: How do I create a non-admin API token?
  - id: Tokens_GetToken
    intent: Get an API token
    question: What are the details of a specific token?
  - id: Tokens_UpdateToken
    intent: Update an API token
    question: How do I deactivate a token without deleting it?
  - id: Tokens_DeleteToken
    intent: Delete an API token
    question: Can I permanently delete a token and remove it from policies?
  phrasing_ops: 5
  slug: progress-software-tokens-api
- baseURL: https://automate.chef.io
  baseurl_source: declared
  description: The TransferStatus API from Progress Software — 1 operation(s) for transferstatus.
  name: Progress Software Transfer Status API
  phrasing_intents:
  - id: GETapi/v1/xferstatus-1.0
    intent: Check the status of file transfers
    question: Which file transfers are running right now on MOVEit Transfer?
  phrasing_ops: 1
  slug: progress-software-transferstatus-api
- baseURL: https://automate.chef.io
  baseurl_source: declared
  description: IAM local users are not attached to external identity providers. They can be members of IAM teams and IAM policies.
  name: Progress Software Users API
  phrasing_intents:
  - id: Users_UpdateSelf
    intent: Update my own IAM display name or password
    question: How do I change my own password as a local IAM user?
  - id: Users_ListUsers
    intent: List local IAM users
    question: Which local IAM users exist in Automate?
  - id: Users_CreateUser
    intent: Create a local IAM user
    question: How do I create a local IAM user who can sign in and be added to policies?
  - id: Users_GetUser
    intent: Get a local IAM user
    question: How do I look up the details of one local IAM user by ID?
  - id: Users_UpdateUser
    intent: Update another local IAM user's name or password
    question: As an admin, how do I reset a local IAM user's password without their old one?
  - id: Users_DeleteUser
    intent: Delete a local IAM user
    question: How do I delete a local IAM user who has left?
  - id: GETapi/v1/users/self-1.0
    intent: Get my own transfer account details
    question: Who am I signed in as on the file transfer server?
  - id: GETapi/v1/users/{Id}-1.0
    intent: Get a transfer user's details
    question: How do I look up a file transfer user's account by ID?
  phrasing_ops: 19
  slug: progress-software-users-api
- baseURL: https://automate.chef.io
  baseurl_source: declared
  description: The UserSettingsService API from Progress Software — 5 operation(s) for usersettingsservice.
  name: Progress Software User Settings Service API
  phrasing_intents:
  - id: UserSettingsService_RequestAdminAuditLogs
    intent: Request audit logs for selected users
    question: As an admin, how do I generate audit logs for specific users?
  - id: UserSettingsService_DownloadAuditLogs
    intent: Download a generated audit log file
    question: How do I download the audit log file after it's generated?
  - id: UserSettingsService_RequestSelfAuditLogs
    intent: Request my own audit logs
    question: Can I generate an audit log of my own activity?
  - id: UserSettingsService_GetAuditLogsRequestStatus
    intent: Check audit log request status
    question: Is my audit log request finished yet?
  - id: UserSettingsService_GetUserSettings
    intent: Get a user's preferences
    question: What preferences are saved for a given user?
  - id: UserSettingsService_PutUserSettings
    intent: Save a user's preferences
    question: How do I update all of a user's preferences at once?
  - id: UserSettingsService_DeleteUserSettings
    intent: Delete a user's preferences
    question: Can I wipe all saved settings for a user?
  phrasing_ops: 7
  slug: progress-software-usersettingsservice-api
- baseURL: https://{subdomain}.sf-api.com/sf/v3
  baseurl_source: declared
  description: The Device Group API from Progress Software — 18 operation(s) for device group.
  name: Progress Software Device Group API
  phrasing_intents:
  - id: DeviceGroup_ListGroups
    intent: List device groups
    question: What device groups are set up in my network monitoring?
  - id: DeviceGroup_GetDeviceGroup
    intent: Get a device group's summary
    question: How do I look up the summary details of one device group?
  - id: DeviceGroup_DeleteDeviceGroup
    intent: Delete a device group
    question: How do I delete a device group I no longer need?
  - id: DeviceGroup_GetDeviceGroupDefinition
    intent: Get a device group's definition
    question: Where can I see how a device group is defined, including its dynamic or layer 2 rules?
  - id: DeviceGroup_UpdateDeviceGroupDefinition
    intent: Update a device group's definition
    question: How do I rename a device group or change its description?
  - id: DeviceGroup_AddDeviceGroup
    intent: Create a child device group
    question: How do I create a new subgroup under an existing device group?
  - id: DeviceGroup_SearchChildren
    intent: List a device group's child groups
    question: Which subgroups sit underneath a given device group?
  - id: DeviceGroup_PollNow
    intent: Poll every device in a group immediately
    question: How do I force all devices in a group to be polled right now instead of waiting for the interval?
  phrasing_ops: 23
  slug: progress-software-device-group-api
- baseURL: https://{subdomain}.sf-api.com/sf/v3
  baseurl_source: declared
  description: The Job Scheduler API from Progress Software — 4 operation(s) for job scheduler.
  name: Progress Software Job Scheduler API
  phrasing_intents:
  - id: JobScheduler_ConfigureDeleteNodesScheduler
    intent: Configure the delete-nodes retention job
    question: How do I change how often Automate runs the job that deletes nodes?
  - id: JobScheduler_ConfigureMissingNodesForDeletionScheduler
    intent: Configure deletion of nodes that stay missing
    question: How long can a node stay missing before Automate deletes it?
  - id: JobScheduler_ConfigureNodesMissingScheduler
    intent: Configure when nodes are marked missing
    question: After how long without a check-in does a node get marked missing?
  - id: JobScheduler_GetStatusJobScheduler
    intent: Get the status of node retention jobs
    question: What are the current settings and run state of the node retention jobs?
  phrasing_ops: 4
  slug: progress-software-job-scheduler-api
- baseURL: https://{subdomain}.sf-api.com/sf/v3
  baseurl_source: declared
  description: The Security Settings API from Progress Software — 8 operation(s) for security settings.
  name: Progress Software Security Settings API
  phrasing_intents:
  - id: GETapi/v1/settings/security/ipwhitelist?Page={Page}&PerPage={PerPage}&SortField={SortField}&SortDirection={SortDirection}-1.0
    intent: List IP whitelist entries
    question: Which IP addresses are on my organization's whitelist?
  - id: POSTapi/v1/settings/security/ipwhitelist-1.0
    intent: Add an IP whitelist entry
    question: How do I allow a new IP address through the whitelist?
  - id: GETapi/v1/settings/security/password/aging/policies?Page={Page}&PerPage={PerPage}&SortField={SortField}&SortDirection={SortDirection}-1.0
    intent: List password aging policies
    question: What password aging policies are defined?
  - id: POSTapi/v1/settings/security/password/aging/policies-1.0
    intent: Create a password aging policy
    question: How do I make passwords expire after a set time?
  - id: GETapi/v1/settings/security/userauth/expiration/policies?Page={Page}&PerPage={PerPage}&SortField={SortField}&SortDirection={SortDirection}-1.0
    intent: List user auth expiration policies
    question: What account expiration policies exist for users?
  - id: POSTapi/v1/settings/security/userauth/expiration/policies-1.0
    intent: Create a user auth expiration policy
    question: How do I make user accounts expire after inactivity?
  - id: PUTapi/v1/settings/security/ipwhitelist/{entryId}-1.0
    intent: Replace an IP whitelist entry
    question: Can I change the IP address on an existing whitelist entry?
  - id: DELETEapi/v1/settings/security/ipwhitelist/{entryId}-1.0
    intent: Remove an IP whitelist entry
    question: How do I take an IP off the whitelist?
  phrasing_ops: 12
  slug: progress-software-security-settings-api
- baseURL: https://{subdomain}.sf-api.com/sf/v3
  baseurl_source: declared
  description: The Server Info API from Progress Software — 1 operation(s) for server info.
  name: Progress Software Server Info API
  phrasing_intents:
  - id: GETapi/v1/serverinfo-1.0
    intent: Get information about the server
    question: What version is the file transfer server running?
  phrasing_ops: 1
  slug: progress-software-server-info-api
artifact_total: 144
asyncapis:
- description: ''
  name: Progress Software Sharefile Webhooks
  slug: progress-software-sharefile-webhooks
common:
- group: agent
  href: https://artifacts.apis.io/progress-software/agentic-access/progress-software-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/progress-software-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/progress-software/finops/progress-software-finops.yml
  title: ''
  type: FinOps
  url: finops/progress-software-finops.yml
- group: design
  href: https://artifacts.apis.io/progress-software/rules/progress-software-rules.yml
  title: ''
  type: Spectral
  url: rules/progress-software-rules.yml
- group: design
  href: https://artifacts.apis.io/progress-software/json-ld/progress-software-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/progress-software-context.jsonld
- group: design
  href: https://artifacts.apis.io/progress-software/vocabulary/progress-software-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/progress-software-vocabulary.yml
- group: other
  href: https://artifacts.apis.io/progress-software/hosts/progress-software-hosts.yml
  title: ''
  type: Hosts
  url: hosts/progress-software-hosts.yml
- group: build
  href: https://artifacts.apis.io/progress-software/integrations/progress-software-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/progress-software-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/progress-software/vendors/progress-software-vendors.yml
  title: ''
  type: Vendors
  url: vendors/progress-software-vendors.yml
- group: start
  title: ''
  type: Sandbox
  url: https://www.progress.com/sitefinity-cms/try-now/sandbox/expired-link
- group: other
  title: ''
  type: Leadership
  url: https://www.progress.com/company/leadership
- group: other
  href: https://artifacts.apis.io/progress-software/capabilities/progress-software-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/progress-software-capability-edges.yml
- group: auth
  href: https://artifacts.apis.io/progress-software/security/progress-software-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/progress-software-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/progress-software/security/progress-software-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/progress-software-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/progress-software/security/progress-software-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/progress-software-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/progress-software/authentication/progress-software-authentication.yml
  title: ''
  type: Authentication
  url: authentication/progress-software-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.progress.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.progress.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.progress.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.chef.io/automate/api/
- group: start
  title: ''
  type: GettingStarted
  url: https://api.sharefile.com/gettingstarted/quickstart
- group: operate
  title: ''
  type: Support
  url: https://www.progress.com/support
- group: operate
  title: ''
  type: HelpCenter
  url: https://community.progress.com/s/knowledge-base
- group: company
  title: ''
  type: Blog
  url: https://www.progress.com/blogs
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/progress
- group: commercial
  title: ''
  type: Pricing
  url: https://www.telerik.com/purchase.aspx
- group: start
  title: ''
  type: SignUp
  url: https://www.progress.com/trials
- group: start
  title: ''
  type: Login
  url: https://www.progress.com/support/customer-portal
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.progress.com/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.progress.com/legal/privacy-center
- group: docs
  href: https://artifacts.apis.io/progress-software/openapi/_original/progress-software-chef-automate-openapi-original.json
  title: ''
  type: OpenAPI
  url: openapi/_original/progress-software-chef-automate-openapi-original.json
- group: docs
  href: https://artifacts.apis.io/progress-software/openapi/_original/progress-software-moveit-transfer-openapi-original.json
  title: ''
  type: OpenAPI
  url: openapi/_original/progress-software-moveit-transfer-openapi-original.json
- group: docs
  href: https://artifacts.apis.io/progress-software/openapi/_original/progress-software-whatsup-gold-openapi-original.json
  title: ''
  type: OpenAPI
  url: openapi/_original/progress-software-whatsup-gold-openapi-original.json
- group: build
  href: https://artifacts.apis.io/progress-software/packages/progress-software-packages.yml
  title: ''
  type: Packages
  url: packages/progress-software-packages.yml
- group: build
  href: https://artifacts.apis.io/progress-software/packages/progress-software-packages.yml
  title: ''
  type: SDKs
  url: packages/progress-software-packages.yml
- group: agent
  href: https://artifacts.apis.io/progress-software/well-known/progress-software-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/progress-software-well-known.yml
- group: agent
  href: https://artifacts.apis.io/progress-software/mcp/progress-software-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/progress-software-mcp.yml
- group: build
  href: https://artifacts.apis.io/progress-software/mcp/progress-software-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/progress-software-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/progress-software/llms/progress-software-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/progress-software-llms.txt
- group: other
  href: https://artifacts.apis.io/progress-software/overlays/progress-software-chef-automate-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/progress-software-chef-automate-overlay.yaml
- group: other
  href: https://artifacts.apis.io/progress-software/overlays/progress-software-moveit-transfer-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/progress-software-moveit-transfer-overlay.yaml
- group: other
  href: https://artifacts.apis.io/progress-software/overlays/progress-software-whatsup-gold-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/progress-software-whatsup-gold-overlay.yaml
- group: design
  href: https://artifacts.apis.io/progress-software/conformance/progress-software-conformance.yml
  title: ''
  type: Conformance
  url: conformance/progress-software-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.progress.com/
- group: design
  href: https://artifacts.apis.io/progress-software/errors/progress-software-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/progress-software-problem-types.yml
- group: design
  href: https://artifacts.apis.io/progress-software/lifecycle/progress-software-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/progress-software-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.chef.io/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.sharefile.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.moveitcloud.com/
- group: operate
  title: ''
  type: Deprecation
  url: https://www.progress.com/support/maintenance-and-support-policy
- group: auth
  title: ''
  type: Security
  url: https://www.progress.com/security/vulnerability-reporting-policy
- group: design
  href: https://artifacts.apis.io/progress-software/conventions/progress-software-conventions.yml
  title: ''
  type: Conventions
  url: conventions/progress-software-conventions.yml
- group: operate
  href: https://artifacts.apis.io/progress-software/changelog/progress-software-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/progress-software-changelog.yml
- group: build
  href: https://artifacts.apis.io/progress-software/cli/progress-software-cli.yml
  title: ''
  type: CLI
  url: cli/progress-software-cli.yml
- group: design
  href: https://artifacts.apis.io/progress-software/components/progress-software-components.yml
  title: ''
  type: Components
  url: components/progress-software-components.yml
- group: design
  href: https://artifacts.apis.io/progress-software/data-model/progress-software-data-model.yml
  title: ''
  type: DataModel
  url: data-model/progress-software-data-model.yml
- group: design
  href: https://artifacts.apis.io/progress-software/asyncapi/progress-software-sharefile-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/progress-software-sharefile-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/progress-software/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  href: https://artifacts.apis.io/progress-software/plans/progress-software-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/progress-software-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/progress-software/rate-limits/progress-software-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/progress-software-rate-limits.yml
created: '2026-09-13'
description: 'Progress Software Corporation (NASDAQ: PRGS) is a Burlington, Massachusetts enterprise software company that builds and acquires infrastructure and digital-experience products. Its portfolio spans application development and data (OpenEdge, MarkLogic, Semaphore, DataDirect, Corticon, Nuclia agentic RAG), digital experience (Sitefinity CMS, Sitefinity Insight), developer tooling and UI components (Telerik, Kendo UI, Fiddler, Test Studio), secure file transfer and collaboration (MOVEit, ShareFile), infrastructure automation and monitoring (Chef, WhatsUp Gold, Flowmon, LoadMaster by Kemp). Most of its API surface is shipped inside self-hosted products — MOVEit Transfer, WhatsUp Gold and Chef Automate each publish a full Swagger 2.0 contract against the customer''s own installation — alongside SaaS surfaces such as the ShareFile OData API and Sitefinity''s headless OData services.'
finops:
- has_sources: true
  method: derived
  name: Progress Software Finops
  primary_unit: developer
  service_category: ''
  slug: progress-software-finops
  template: false
image: https://www.progress.com/images/default-source/default-album/progress-album/images-album/social-image.png
json_schemas:
- name: ActAsAdminDto
  property_count: 2
  slug: progress-software-act-as-admin-dto
- name: AdHocTransferAgingExpirationModel
  property_count: 4
  slug: progress-software-ad-hoc-transfer-aging-expiration-model
- name: chef.automate.api.applications.GetServicesUsageCountResponse
  property_count: 2
  slug: progress-software-chef-automate-api-applications-get-services-usage-count-response
- name: Telemetry
  property_count: 1
  slug: progress-software-chef-automate-api-applications-update-telemetry-reported-request
- name: chef.automate.api.applications.UpdateTelemetryReportedResponse
  property_count: 0
  slug: progress-software-chef-automate-api-applications-update-telemetry-reported-response
- name: chef.automate.api.cds.request.Credentials
  property_count: 3
  slug: progress-software-chef-automate-api-cds-request-credentials
- name: chef.automate.api.cds.request.InstallContentItem
  property_count: 2
  slug: progress-software-chef-automate-api-cds-request-install-content-item
- name: chef.automate.api.cds.response.ContentEnabled
  property_count: 1
  slug: progress-software-chef-automate-api-cds-response-content-enabled
- name: chef.automate.api.cds.response.ContentItems
  property_count: 1
  slug: progress-software-chef-automate-api-cds-response-content-items
- name: chef.automate.api.cds.response.Credentials
  property_count: 0
  slug: progress-software-chef-automate-api-cds-response-credentials
- name: chef.automate.api.cds.response.InstallContentItem
  property_count: 0
  slug: progress-software-chef-automate-api-cds-response-install-content-item
- name: chef.automate.api.cfgmgmt.request.CreateRollout
  property_count: 15
  slug: progress-software-chef-automate-api-cfgmgmt-request-create-rollout
- name: chef.automate.api.cfgmgmt.request.ReportExport
  property_count: 5
  slug: progress-software-chef-automate-api-cfgmgmt-request-report-export
- name: chef.automate.api.cfgmgmt.response.NodeAttribute
  property_count: 13
  slug: progress-software-chef-automate-api-cfgmgmt-response-node-attribute
- name: NodeSegmentsWithRolloutProgress
  property_count: 1
  slug: progress-software-chef-automate-api-cfgmgmt-response-node-segments-with-rollout-progress
- name: chef.automate.api.cfgmgmt.response.Rollout
  property_count: 18
  slug: progress-software-chef-automate-api-cfgmgmt-response-rollout
- name: chef.automate.api.cfgmgmt.response.Run
  property_count: 48
  slug: progress-software-chef-automate-api-cfgmgmt-response-run
- name: chef.automate.api.common.version.VersionInfo
  property_count: 4
  slug: progress-software-chef-automate-api-common-version-version-info
- name: chef.automate.api.compliance.reporting.v1.AssetListRequest
  property_count: 5
  slug: progress-software-chef-automate-api-compliance-reporting-v1-asset-list-request
- name: chef.automate.api.compliance.reporting.v1.AssetListResponse
  property_count: 1
  slug: progress-software-chef-automate-api-compliance-reporting-v1-asset-list-response
- name: chef.automate.api.compliance.reporting.v1.AssetSummary
  property_count: 3
  slug: progress-software-chef-automate-api-compliance-reporting-v1-asset-summary
- name: ComplianceConfigRequest to update no of days in the config
  property_count: 1
  slug: progress-software-chef-automate-api-compliance-reporting-v1-compliance-config-request
- name: ComplianceConfigResponse to get the policy name and no of days
  property_count: 2
  slug: progress-software-chef-automate-api-compliance-reporting-v1-compliance-config-response
- name: chef.automate.api.compliance.reporting.v1.ListFilters
  property_count: 1
  slug: progress-software-chef-automate-api-compliance-reporting-v1-list-filters
- name: chef.automate.api.data_lifecycle.GetStatusResponse
  property_count: 4
  slug: progress-software-chef-automate-api-data-lifecycle-get-status-response
- name: chef.automate.api.data_lifecycle.SetComplianceConfigRequest
  property_count: 1
  slug: progress-software-chef-automate-api-data-lifecycle-set-compliance-config-request
- name: chef.automate.api.data_lifecycle.SetConfigRequest
  property_count: 4
  slug: progress-software-chef-automate-api-data-lifecycle-set-config-request
- name: chef.automate.api.data_lifecycle.SetEventFeedConfigRequest
  property_count: 1
  slug: progress-software-chef-automate-api-data-lifecycle-set-event-feed-config-request
- name: chef.automate.api.data_lifecycle.SetInfraConfigRequest
  property_count: 1
  slug: progress-software-chef-automate-api-data-lifecycle-set-infra-config-request
- name: chef.automate.api.datafeed.AddDestinationRequest
  property_count: 8
  slug: progress-software-chef-automate-api-datafeed-add-destination-request
- name: chef.automate.api.datafeed.AddDestinationResponse
  property_count: 8
  slug: progress-software-chef-automate-api-datafeed-add-destination-response
- name: chef.automate.api.datafeed.DeleteDestinationResponse
  property_count: 8
  slug: progress-software-chef-automate-api-datafeed-delete-destination-response
- name: chef.automate.api.datafeed.GetDestinationResponse
  property_count: 8
  slug: progress-software-chef-automate-api-datafeed-get-destination-response
- name: chef.automate.api.datafeed.UpdateDestinationResponse
  property_count: 8
  slug: progress-software-chef-automate-api-datafeed-update-destination-response
- name: chef.automate.api.datafeed.URLValidationRequest
  property_count: 6
  slug: progress-software-chef-automate-api-datafeed-urlvalidation-request
- name: chef.automate.api.iam.v2.IntrospectReq
  property_count: 2
  slug: progress-software-chef-automate-api-iam-v2-introspect-req
- name: chef.automate.api.iam.v2.IntrospectResp
  property_count: 1
  slug: progress-software-chef-automate-api-iam-v2-introspect-resp
- name: chef.automate.api.iam.v2.IntrospectSomeReq
  property_count: 1
  slug: progress-software-chef-automate-api-iam-v2-introspect-some-req
- name: chef.automate.api.ingest.request.Action
  property_count: 21
  slug: progress-software-chef-automate-api-ingest-request-action
- name: chef.automate.api.ingest.request.Delete
  property_count: 6
  slug: progress-software-chef-automate-api-ingest-request-delete
- name: chef.automate.api.ingest.request.Liveness
  property_count: 7
  slug: progress-software-chef-automate-api-ingest-request-liveness
- name: chef.automate.api.ingest.request.MultipleNodeDeleteRequest
  property_count: 1
  slug: progress-software-chef-automate-api-ingest-request-multiple-node-delete-request
- name: chef.automate.api.ingest.request.Run
  property_count: 24
  slug: progress-software-chef-automate-api-ingest-request-run
- name: ContactAddModel
  property_count: 2
  slug: progress-software-contact-add-model
- name: ContactModel
  property_count: 4
  slug: progress-software-contact-model
- name: ContactUpdateModel
  property_count: 2
  slug: progress-software-contact-update-model
- name: CountedSuccessResult
  property_count: 7
  slug: progress-software-counted-success-result
- name: CredentialAdd
  property_count: 4
  slug: progress-software-credential-add
- name: CredentialModify
  property_count: 3
  slug: progress-software-credential-modify
- name: CredentialTemplateBatch
  property_count: 3
  slug: progress-software-credential-template-batch
- name: LogosModel
  property_count: 4
  slug: progress-software-logos-model
- name: OrgRequest
  property_count: 1
  slug: progress-software-org-request
- name: PageResult_Credential
  property_count: 2
  slug: progress-software-page-result-credential
- name: PageResult_List_Credential
  property_count: 2
  slug: progress-software-page-result-list-credential
- name: PagedModelOfContactModel
  property_count: 3
  slug: progress-software-paged-model-of-contact-model
- name: PagedModelOfPublicIdPInformationModel
  property_count: 3
  slug: progress-software-paged-model-of-public-id-pinformation-model
- name: RevokeTokenResponse
  property_count: 1
  slug: progress-software-revoke-token-response
- name: SendOtpResponseModel
  property_count: 1
  slug: progress-software-send-otp-response-model
- name: TokenAcquiredModel
  property_count: 6
  slug: progress-software-token-acquired-model
- name: Void
  property_count: 0
  slug: progress-software-void
jsonld:
- class_count: 120
  name: Progress Software Context
  property_count: 275
  slug: progress-software-context
layout: provider
mcp_servers:
- description: ''
  name: Progress Software MCP Server
  slug: progress-software-mcp-yml
modified: '2026-09-16'
name: Progress Software
nav: Providers
network: true
overview: 'Progress Software publishes 66 API contracts indexed on the [APIs.io](https://apis.io/) network, including Ad Hoc Transfer Settings API, Appearance Settings API, Applications Service API, and 63 more. Tagged areas include Company, Enterprise Software, Managed File Transfer, Infrastructure Automation, and Network Monitoring.


  The Progress Software catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Progress Software''s developer surface includes sandbox, authentication, documentation, API reference, getting-started guide, support, engineering blog, and 52 more developer resources.'
plans:
- name: Progress Software Plans Pricing
  plan_count: 24
  slug: progress-software-plans-pricing
- name: Progress Software Price Estimates
  plan_count: 0
  slug: progress-software-price-estimates
random_paper: 5
rate_limits:
- limit_count: 0
  name: Progress Software Rate Limits
  slug: progress-software-rate-limits
rules:
- authorship: generated
  effective_rule_count: 104
  extends:
  - spectral:oas
  name: Progress Software API Rules
  rule_count: 63
  severity_counts:
    error: 43
    hint: 0
    info: 3
    warn: 17
  slug: progress-software-rules
scopes:
- name: Progress Software Scopes
  scope_count: 0
  slug: progress-software-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: exemplar
  composite: 78.1
  coverage:
    artifact_dirs: 37
    catalog_earned: 80.8
    catalog_earned_first_party: 12.0
    catalog_gap: 34.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 5.4
  facets:
    access_clarity: 92.1
    contract_governance: 22.0
    contract_quality: 64.3
    developer_ergonomics: 80.4
    discoverability: 78.3
    operational_transparency: 60.5
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 72.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 76.1
      derived: 0
      marker_coverage: 0.0
      total: 64
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 40.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: rising
  upsert:
    applies: true
    score: 61.1
screenshot: https://apis.io/screenshots/progress-software/progress-software-2026-10-11T112908.png
security:
- kind: authentication
  name: Progress Software Authentication
  slug: progress-software-authentication
  summary_line: apiKey/oauth2 · 3 schemes
- kind: domain-security
  name: Progress Software Domain Security
  slug: progress-software-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Progress Software Vulnerability Disclosure
  slug: progress-software-vulnerability-disclosure
  summary_line: Bugcrowd · security.txt · contact published
- kind: trust-center
  name: Progress Software Trust Center
  slug: progress-software-trust-center
  summary_line: SOC 1, SOC 2 Type I, SOC 2 Type II, SOC 3, ISO 27001, ISO 27017, ISO 27018, PCI DSS, HIPAA, FedRAMP, CSA STAR, TISAX, GDPR
skill_count: 4
skills:
- name: Chef Automate — mint a scoped token and pull a compliance report
  slug: progress-software-chef-automate-compliance-report
- name: MOVEit Transfer — authenticate and move a file
  slug: progress-software-moveit-authenticate-and-transfer
- name: MOVEit Transfer — send an ad-hoc secure package
  slug: progress-software-moveit-send-package
- name: WhatsUp Gold — inspect a device and manage its monitors
  slug: progress-software-whatsup-gold-monitor-a-device
slug: progress-software
tags:
- Company
- Enterprise Software
- Managed File Transfer
- Infrastructure Automation
- Network Monitoring
- Content Management
- Developer Tools
- Data Platform
- Application Development
- DevOps
- Agentic RAG
- File Sharing
website: https://www.progress.com/
---
