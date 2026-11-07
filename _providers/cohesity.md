---
access_model:
  confidence: high
  label: Enterprise · Requires approval
  onboarding: approval
  pricing: enterprise
  public: false
  source:
  - plans
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
    dry_run_mode: true
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: derived
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: mostly
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 43.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 357
  human_in_the_loop: 7
  name: Cohesity Agentic Access
  operation_count: 687
  slug: cohesity-agentic-access
  summary_line: 687 operations · 357 acting · 7 human-in-the-loop
api_count: 6
apis:
- baseURL: https://helios.cohesity.com/irisservices/api/v1/public/
  baseurl_source: declared
  description: The Alerts API from Cohesity — 8 operation(s) for alerts.
  name: Cohesity Alerts API
  phrasing_intents:
  - id: GetAlertCategories
    intent: List alert categories
    question: What categories do Cohesity cluster alerts fall into?
  - id: GetNotificationRules
    intent: List alert notification rules
    question: Who gets notified when an alert fires on my cluster?
  - id: UpdateNotificationRule
    intent: Update an alert notification rule
    question: How do I change the email addresses on an existing notification rule?
  - id: CreateNotificationRule
    intent: Create an alert notification rule
    question: How do I get emailed when critical alerts happen?
  - id: DeleteNotificationRule
    intent: Delete an alert notification rule
    question: How do I stop a notification rule from sending alerts?
  - id: GetResolutions
    intent: List alert resolutions
    question: Which alert resolutions have been recorded on my cluster?
  - id: CreateResolution
    intent: Resolve alerts with a new resolution
    question: How do I mark a batch of alerts as resolved with a note?
  - id: GetResolutionById
    intent: Get an alert resolution
    question: What did a particular alert resolution say?
  phrasing_ops: 12
  slug: cohesity-alerts-api
- baseURL: https://helios.cohesity.com/irisservices/api/v1/public/
  baseurl_source: declared
  description: The Analytics API from Cohesity — 17 operation(s) for analytics.
  name: Cohesity Analytics API
  phrasing_intents:
  - id: AnalyzeJar
    intent: Analyze an uploaded analytics jar
    question: What's inside the jar I just uploaded to the Analytics workbench?
  - id: GetApplications
    intent: List analytics applications
    question: Which analytics applications exist on my Cohesity cluster?
  - id: CreateApplication
    intent: Create an analytics application
    question: How do I define a new map-reduce application in the Analytics workbench?
  - id: GetApplicationById
    intent: Get one analytics application
    question: What mapper and reducer does a specific analytics application use?
  - id: UpdateApplication
    intent: Update an analytics application
    question: Can I change the mapper or reducer of an analytics app I already created?
  - id: DeleteApplication
    intent: Delete an analytics application
    question: How do I remove an analytics application I no longer need?
  - id: CancelMapReduceInstanceRun
    intent: Cancel a running map-reduce instance
    question: How do I stop a map-reduce instance run that is still in progress?
  - id: GetMappers
    intent: List map-reduce mappers
    question: Which mappers are available on my cluster for analytics apps?
  phrasing_ops: 28
  slug: cohesity-analytics-api
- baseURL: https://helios.cohesity.com/irisservices/api/v1/public/
  baseurl_source: declared
  description: The AntivirusServiceGroup API from Cohesity — 5 operation(s) for antivirusservicegroup.
  name: Cohesity Antivirus Service Group API
  phrasing_intents:
  - id: GetAntivirusServiceGroup
    intent: List antivirus service groups
    question: Which antivirus service groups are configured on my cluster?
  - id: UpdateAntivirusServiceGroup
    intent: Update an antivirus service group
    question: How do I add or change the antivirus services in a group?
  - id: CreateAntivirusServiceGroup
    intent: Create an antivirus service group
    question: How do I set up antivirus scanning for my file views?
  - id: AntivirusServiceGroupState
    intent: Enable or disable an antivirus group
    question: Can I turn off an antivirus service group temporarily?
  - id: DeleteAntivirusServiceGroup
    intent: Delete an antivirus service group
    question: How do I remove an antivirus service group?
  - id: GetIcapConnectionStatus
    intent: Check ICAP server connectivity
    question: Are my ICAP antivirus servers reachable from the cluster?
  - id: GetInfectedFiles
    intent: List infected files
    question: Which files did antivirus scanning flag as infected?
  - id: UpdateInfectedFiles
    intent: Change remediation state of infected files
    question: How do I quarantine or unquarantine infected files?
  phrasing_ops: 9
  slug: cohesity-antivirusservicegroup-api
- baseURL: https://helios.cohesity.com/irisservices/api/v1/public/
  baseurl_source: declared
  description: The App API from Cohesity — 2 operation(s) for app.
  name: Cohesity App API
  phrasing_intents:
  - id: GetApps
    intent: List available and installed apps
    question: Which marketplace apps are installed or available to install on my cluster?
  - id: UploadApp
    intent: Upload and install an app from an image
    question: Can I install an app by uploading its image file?
  - id: InstallApp
    intent: Install a purchased app version
    question: Can I install a specific version of a purchased app on the cluster?
  - id: UninstallApp
    intent: Uninstall an app version
    question: Can I uninstall an app version from the cluster?
  phrasing_ops: 4
  slug: cohesity-app-api
- baseURL: https://helios.cohesity.com/irisservices/api/v1/public/
  baseurl_source: declared
  description: The AppInstance API from Cohesity — 3 operation(s) for appinstance.
  name: Cohesity App Instance API
  phrasing_intents:
  - id: UpdateAppInstanceSettings
    intent: Update app instance settings
    question: How do I change the settings of a running app instance?
  - id: GetAppInstances
    intent: List app instances
    question: Which app instances are running or stopped on the cluster?
  - id: LaunchAppInstance
    intent: Launch an installed app
    question: How do I launch an app I installed on the cluster?
  - id: UpdateAppInstanceState
    intent: Change an app instance's state
    question: How do I stop or restart an app instance?
  phrasing_ops: 4
  slug: cohesity-appinstance-api
- baseURL: https://helios.cohesity.com/irisservices/api/v1/public/
  baseurl_source: declared
  description: The Applications API from Cohesity — 4 operation(s) for applications.
  name: Cohesity Applications API
  phrasing_intents:
  - id: SCCreateApp
    intent: Create a DR application
    question: How do I group objects, delays and scripts into an application for DR?
  - id: SCGetApps
    intent: List DR applications
    question: Which applications are defined for disaster recovery?
  - id: SCGetAppById
    intent: Get one DR application
    question: What objects and scripts make up a given application?
  - id: SCUpdateAppById
    intent: Update a DR application
    question: How do I change the objects or scripts in an existing application?
  - id: SCDeleteAppById
    intent: Delete a DR application
    question: How do I delete an application I no longer protect?
  - id: SCGetVersionsForApp
    intent: List versions of a DR application
    question: What versions has an application gone through?
  - id: SCGetSnapshotForAppId
    intent: List replicated snapshots for an application
    question: What's the latest replicated snapshot for each object in my application?
  phrasing_ops: 7
  slug: cohesity-applications-api
- baseURL: https://helios.cohesity.com/irisservices/api/v1/public/
  baseurl_source: declared
  description: The Artifacts API from Cohesity — 1 operation(s) for artifacts.
  name: Cohesity Artifacts API
  phrasing_intents:
  - id: GetArtifactForTask
    intent: Download a report artifact for a task
    question: How do I download the report a task generated?
  phrasing_ops: 1
  slug: cohesity-artifacts-api
- baseURL: https://helios.cohesity.com/irisservices/api/v1/public/
  baseurl_source: declared
  description: The Audit API from Cohesity — 3 operation(s) for audit.
  name: Cohesity Audit API
  phrasing_intents:
  - id: GetAuditLogsActions
    intent: List audit log actions (legacy public)
    question: Which action names can I use to filter the older public cluster audit logs?
  - id: GetAuditLogsCategories
    intent: List audit log categories
    question: Which categories are cluster audit logs grouped into?
  - id: SearchClusterAuditLogs
    intent: Search cluster audit logs (legacy public)
    question: Who logged in or paused a job on the cluster, per the older public audit log search?
  phrasing_ops: 3
  slug: cohesity-audit-api
- baseURL: https://helios.cohesity.com/irisservices/api/v1/public/
  baseurl_source: declared
  description: The Banner API from Cohesity — 1 operation(s) for banner.
  name: Cohesity Banner API
  phrasing_intents:
  - id: GetBanner
    intent: Show the cluster login banner
    question: What banner message is shown to users on the cluster?
  - id: UpdateBanner
    intent: Change the cluster login banner
    question: How do I change the banner message users see?
  phrasing_ops: 2
  slug: cohesity-banner-api
- baseURL: https://helios.cohesity.com/irisservices/api/v1/public/
  baseurl_source: declared
  description: The Certificates API from Cohesity — 2 operation(s) for certificates.
  name: Cohesity Certificates API
  phrasing_intents:
  - id: GetCertificateList
    intent: List host certificates generated by the cluster
    question: Which certificates has the cluster generated and deployed to hosts?
  - id: DeployHostCertificate
    intent: Generate and deploy host certificates
    question: Can I generate a certificate and push it to one or more hosts?
  - id: GetWebServerCertificate
    intent: Get the cluster web server certificate
    question: Which SSL certificate is the cluster's web server using right now?
  - id: UpdateWebServerCertificate
    intent: Replace the cluster web server certificate
    question: How do I install my own SSL certificate on the cluster web server?
  - id: DeleteWebServerCertificate
    intent: Delete the cluster web server certificate
    question: Can I remove the custom SSL certificate from the cluster?
  phrasing_ops: 5
  slug: cohesity-certificates-api
- baseURL: https://helios.cohesity.com/irisservices/api/v1/public/
  baseurl_source: declared
  description: The CloneRefreshTasks API from Cohesity — 1 operation(s) for clonerefreshtasks.
  name: Cohesity Clone Refresh Tasks API
  phrasing_intents:
  - id: CreateCloneRefreshTask
    intent: Refresh a cloned database with newer data
    question: How do I refresh a database clone with data from a later backup?
  phrasing_ops: 1
  slug: cohesity-clonerefreshtasks-api
- baseURL: https://helios.cohesity.com/irisservices/api/v1/public/
  baseurl_source: declared
  description: The Cluster API from Cohesity — 4 operation(s) for cluster.
  name: Cohesity Cluster API
  phrasing_intents:
  - id: GetBasicClusterInfo
    intent: Get basic cluster info without logging in
    question: What version and domains does a Cohesity cluster have, before I authenticate?
  - id: GetCluster
    intent: Get cluster configuration
    question: What is the full configuration of this Cohesity cluster?
  - id: UpdateCluster
    intent: Update cluster configuration
    question: How do I change the cluster's DNS servers or timezone?
  - id: GetAppSettings
    intent: Get cluster app settings
    question: How much CPU and memory is reserved for apps on the cluster?
  - id: UpdateAppSettings
    intent: Update cluster app settings
    question: Can I reserve more memory for apps running on the cluster?
  - id: GetClusterStatus
    intent: Get node status for the cluster
    question: Are all the nodes in my cluster healthy?
  phrasing_ops: 6
  slug: cohesity-cluster-api
- baseURL: https://helios.cohesity.com/irisservices/api/v1/public/
  baseurl_source: declared
  description: The ClusterPartitions API from Cohesity — 2 operation(s) for clusterpartitions.
  name: Cohesity Cluster Partitions API
  phrasing_intents:
  - id: GetClusterPartitions
    intent: List cluster partitions
    question: Which cluster partitions exist on my cluster?
  - id: GetClusterPartitionById
    intent: Get a cluster partition
    question: How do I see the details of a single cluster partition?
  phrasing_ops: 2
  slug: cohesity-clusterpartitions-api
- baseURL: https://helios.cohesity.com/irisservices/api/v1/public/
  baseurl_source: declared
  description: The Clusters API from Cohesity — 14 operation(s) for clusters.
  name: Cohesity Clusters API
  phrasing_intents:
  - id: GetBackgroundActivitySchedule
    intent: Show the background activity throttling schedule
    question: When does the cluster throttle background tasks like garbage collection?
  - id: UpdateBackgroundActivitySchedule
    intent: Change the background activity throttling schedule
    question: Can I move background maintenance work to off-hours so it doesn't slow backups?
  - id: GetClusterKeys
    intent: List the cluster's public keys
    question: Where can I find the public keys my cluster uses?
  - id: DestroyCluster
    intent: Destroy a Cohesity cluster
    question: Is it possible to completely tear down a cluster and wipe its nodes?
  - id: CreateCloudCluster
    intent: Create a Cloud Edition cluster
    question: How do I stand up a new Cloud Edition cluster on cloud VMs?
  - id: ExpandCloudCluster
    intent: Add nodes to a Cloud Edition cluster
    question: Can I grow an existing Cloud Edition cluster by adding more cloud nodes?
  - id: GetClusterCreationProgress
    intent: Check cluster creation progress
    question: How far along is my new cluster's creation, and how long is left?
  - id: GetIoPreferentialTier
    intent: Show the IO preferential storage tiers
    question: Which storage tiers does the cluster prefer for random versus sequential IO?
  phrasing_ops: 18
  slug: cohesity-clusters-api
- baseURL: https://helios.cohesity.com/irisservices/api/v1/public/
  baseurl_source: declared
  description: The Components API from Cohesity — 4 operation(s) for components.
  name: Cohesity Components API
  phrasing_intents:
  - id: GetComponents
    intent: List report components
    question: Which report components can I access?
  - id: GetComponentById
    intent: Get one report component
    question: What does a particular report component contain?
  - id: GetComponentsPreview
    intent: Preview several report components
    question: Can I preview the data for several report components before building a report?
  - id: GetComponentPreview
    intent: Preview a single report component
    question: What data would one report component show right now?
  phrasing_ops: 4
  slug: cohesity-components-api
- baseURL: https://helios.cohesity.com/irisservices/api/v1/public/
  baseurl_source: declared
  description: The Connectors API from Cohesity — 4 operation(s) for connectors.
  name: Cohesity Connectors API
  phrasing_intents:
  - id: GetBifrostConnector
    intent: List Bifrost (hybrid extender) connectors
    question: Which Bifrost hybrid extender connectors are set up on the cluster?
  - id: CreateBifrostConnector
    intent: Create a Bifrost connector
    question: How do I add a Bifrost hybrid extender connector for a tenant?
  - id: GetBifrostConnectorById
    intent: Get a Bifrost connector
    question: What are the details of one Bifrost connector?
  - id: UpdateBifrostConnector
    intent: Update a Bifrost connector
    question: Can I rename a Bifrost connector or point it at another connection?
  - id: DeleteBifrostConnector
    intent: Delete a Bifrost connector
    question: Can I remove a Bifrost hybrid extender connector I no longer need?
  - id: GetRigelConnector
    intent: List Rigel connectors
    question: Which Rigel connectors are configured on the cluster?
  - id: CreateRigelConnector
    intent: Create a Rigel connector
    question: What do I need to create a Rigel connector, including its certificate version?
  - id: GetRigelConnectorById
    intent: Get a Rigel connector
    question: What are the details of one Rigel connector?
  phrasing_ops: 10
  slug: cohesity-connectors-api
- baseURL: https://helios.cohesity.com/irisservices/api/v1/public/
  baseurl_source: declared
  description: The CustomReporting API from Cohesity — 1 operation(s) for customreporting.
  name: Cohesity Custom Reporting API
  phrasing_intents:
  - id: GetPostgres
    intent: List nodes running the reporting Postgres database
    question: Which cluster nodes are running the Postgres database for custom reporting?
  phrasing_ops: 1
  slug: cohesity-customreporting-api
- baseURL: https://helios.cohesity.com/irisservices/api/v1/public/
  baseurl_source: declared
  description: The Dashboard API from Cohesity — 1 operation(s) for dashboard.
  name: Cohesity Dashboard API
  phrasing_intents:
  - id: GetDashboard
    intent: Get the cluster dashboard
    question: What does the dashboard for my cluster show right now?
  phrasing_ops: 1
  slug: cohesity-dashboard-api
- baseURL: https://helios.cohesity.com/irisservices/api/v1/public/
  baseurl_source: declared
  description: The Data Tiering API from Cohesity — 11 operation(s) for data tiering.
  name: Cohesity Data Tiering API
  phrasing_intents:
  - id: GetDataTieringAnalysisGroups
    intent: List data tiering analysis groups
    question: Which data tiering analysis groups are set up on my cluster?
  - id: CreateDataTieringAnalysisGroup
    intent: Create a data tiering analysis group
    question: How do I set up analysis to see which data could be tiered?
  - id: UpdateDataTieringAnalysisGroupsState
    intent: Pause or resume analysis groups
    question: Can I pause data tiering analysis for several sources at once?
  - id: GetDataTieringAnalysisGroupById
    intent: Get a data tiering analysis group
    question: What are the settings of one tiering analysis group?
  - id: DeleteDataTieringAnalysisGroup
    intent: Delete a data tiering analysis group
    question: How do I remove a data tiering analysis group?
  - id: UpdateDataTieringAnalysisGroupTagsConfig
    intent: Update an analysis group's tag config
    question: Can I change the tags used by a data tiering analysis group?
  - id: CreateDataTieringAnalysisGroupRun
    intent: Run a data tiering analysis
    question: How do I start an analysis run to find cold data?
  - id: CancelDataTieringAnalysisGroupRun
    intent: Cancel a data tiering analysis run
    question: How do I stop an analysis run that's in progress?
  phrasing_ops: 16
  slug: cohesity-data-tiering-api
- baseURL: https://helios.cohesity.com/irisservices/api/v1/public/
  baseurl_source: declared
  description: The DMaaSTenantCertificate API from Cohesity — 2 operation(s) for dmaastenantcertificate.
  name: Cohesity D Maa S Tenant Certificate API
  phrasing_intents:
  - id: GetDmaasTenantCerts
    intent: List DMaaS tenant certificates
    question: Which DMaaS tenant certificates are installed on the cluster?
  - id: AddDmaasTenantCert
    intent: Add a DMaaS tenant certificate
    question: How do I install a tenant certificate for DMaaS on the cluster?
  - id: DeleteDmaasTenantCert
    intent: Delete a DMaaS tenant certificate
    question: How do I remove a tenant's DMaaS certificate?
  phrasing_ops: 3
  slug: cohesity-dmaastenantcertificate-api
- baseURL: https://helios.cohesity.com/irisservices/api/v1/public/
  baseurl_source: declared
  description: The DRPlan API from Cohesity — 6 operation(s) for drplan.
  name: Cohesity DR Plan API
  phrasing_intents:
  - id: SCCreateDRPlan
    intent: Create a disaster recovery plan
    question: How do I set up a DR plan that pairs a primary site with a recovery site?
  - id: SCGetDrPlans
    intent: List disaster recovery plans
    question: Which DR plans are currently violating their SLA?
  - id: SCGetDRPlanById
    intent: Get a disaster recovery plan
    question: How do I see the full configuration of one DR plan?
  - id: SCDeleteDRPlanById
    intent: Delete a disaster recovery plan
    question: How do I remove a DR plan I no longer need?
  - id: SCUpdateDRPlanById
    intent: Update a disaster recovery plan
    question: Can I change the RPO on an existing DR plan?
  - id: SCPerformActionOnDRPlan
    intent: Fail over, fail back or test a DR plan
    question: How do I trigger a failover to the DR site for one of my plans?
  - id: SCGetActions
    intent: List actions taken on DR plans
    question: Which failovers or failbacks have run on my DR plans this week?
  - id: SCGetActionById
    intent: Get a DR plan action
    question: How do I check the status of one failover action?
  phrasing_ops: 9
  slug: cohesity-drplan-api
- baseURL: https://helios.cohesity.com/irisservices/api/v1/public/
  baseurl_source: declared
  description: The Failover API from Cohesity — 9 operation(s) for failover.
  name: Cohesity Failover API
  phrasing_intents:
  - id: PollPlannedRuns
    intent: Check whether failover planned runs are scheduled
    question: Has the planned run for my failover been scheduled yet?
  - id: GetViewFailover
    intent: Get failover tasks of a View
    question: What failover tasks have run against a particular View?
  - id: CreateViewFailover
    intent: Start a View failover
    question: Can I fail over a View to its replica, either planned or unplanned?
  - id: CancelViewFailover
    intent: Cancel an in-progress View failover
    question: Can I abort a View failover that's still running?
  - id: InitFailover
    intent: Initiate a failover request
    question: How do I kick off a failover workflow between a source and replication cluster?
  - id: ReplicationBackupActivation
    intent: Activate backups on the replication cluster
    question: After failover, can I start backing up the failed-over objects on the replication cluster?
  - id: SourceBackupDeactivation
    intent: Deactivate backups on the source cluster
    question: During failover, can I stop backups of the failed-over objects on the source cluster?
  - id: CancelFailover
    intent: Cancel a failover workflow
    question: Can I cancel a failover workflow before backup activation or deactivation has been called?
  phrasing_ops: 10
  slug: cohesity-failover-api
- baseURL: https://helios.cohesity.com/irisservices/api/v1/public/
  baseurl_source: declared
  description: The Filters API from Cohesity — 1 operation(s) for filters.
  name: Cohesity Filters API
  phrasing_intents:
  - id: GetResources
    intent: Get discovered resources for filtering
    question: What resources has Helios discovered that I can use as filter options?
  phrasing_ops: 1
  slug: cohesity-filters-api
- baseURL: https://helios.cohesity.com/irisservices/api/v1/public/
  baseurl_source: declared
  description: The FleetInstance API from Cohesity — 1 operation(s) for fleetinstance.
  name: Cohesity Fleet Instance API
  phrasing_intents:
  - id: UpdateFleetEnvInfo
    intent: Set AWS fleet environment info
    question: What AWS settings does a Cloud Edition cluster need to launch fleet instances?
  phrasing_ops: 1
  slug: cohesity-fleetinstance-api
- baseURL: https://helios.cohesity.com/irisservices/api/v1/public/
  baseurl_source: declared
  description: The Groups API from Cohesity — 1 operation(s) for groups.
  name: Cohesity Groups API
  phrasing_intents:
  - id: GetGroups
    intent: List cluster groups
    question: Which user groups are set up on the cluster?
  - id: UpdateGroup
    intent: Update a cluster group
    question: How do I change the roles assigned to an existing group?
  - id: CreateGroup
    intent: Add a group to the cluster
    question: How do I bring an Active Directory group onto the cluster with a role?
  - id: DeleteGroups
    intent: Delete groups from the cluster
    question: Can I remove several groups from the same domain at once?
  phrasing_ops: 4
  slug: cohesity-groups-api
- baseURL: https://helios.cohesity.com/irisservices/api/v1/public/
  baseurl_source: declared
  description: The HeliosRegistration API from Cohesity — 3 operation(s) for heliosregistration.
  name: Cohesity Helios Registration API
  phrasing_intents:
  - id: HeliosClaim
    intent: Register the cluster to Helios
    question: How do I claim my cluster into Helios?
  - id: GetHeliosRegConfig
    intent: View the Helios registration config
    question: Is my cluster registered with Helios?
  - id: GetRigelClaimLogs
    intent: Get Rigel cluster creation and claim logs
    question: Why did my Rigel cluster claim fail?
  phrasing_ops: 3
  slug: cohesity-heliosregistration-api
- baseURL: https://helios.cohesity.com/irisservices/api/v1/public/
  baseurl_source: declared
  description: The Idps API from Cohesity — 4 operation(s) for idps.
  name: Cohesity Idps API
  phrasing_intents:
  - id: AddActiveIdpPrincipals
    intent: Add IdP users or groups with roles
    question: How do I give SSO users from my identity provider access to the cluster?
  - id: GetIdps
    intent: List identity provider configurations
    question: Which SAML identity providers are configured on the cluster?
  - id: CreateIdp
    intent: Configure a SAML identity provider
    question: How do I set up SAML single sign-on for the cluster?
  - id: IdpLogin
    intent: Log in through an identity provider
    question: How do I sign in to the cluster using SSO?
  - id: UpdateIdp
    intent: Update an identity provider configuration
    question: Can I rotate the certificate on an existing SAML IdP?
  - id: DeleteIdp
    intent: Delete an identity provider configuration
    question: How do I remove a SAML IdP from the cluster?
  phrasing_ops: 6
  slug: cohesity-idps-api
- baseURL: https://helios.cohesity.com/irisservices/api/v1/public/
  baseurl_source: declared
  description: The Interface API from Cohesity — 1 operation(s) for interface.
  name: Cohesity Interface API
  phrasing_intents:
  - id: ListInterface
    intent: List network interfaces
    question: Which network interfaces does each node have?
  - id: UpdateInterface
    intent: Update a network interface
    question: Can I change the network parameters of a node interface?
  phrasing_ops: 2
  slug: cohesity-interface-api
- baseURL: https://helios.cohesity.com/irisservices/api/v1/public/
  baseurl_source: declared
  description: The Internal API from Cohesity — 1 operation(s) for internal.
  name: Cohesity Internal API
  phrasing_intents:
  - id: RefreshBulletinBoard
    intent: Refresh the bulletin board from Helios
    question: How do I pull the latest bulletin board messages from Helios?
  phrasing_ops: 1
  slug: cohesity-internal-api
- baseURL: https://helios.cohesity.com/irisservices/api/v1/public/
  baseurl_source: declared
  description: The Ip API from Cohesity — 1 operation(s) for ip.
  name: Cohesity Ip API
  phrasing_intents:
  - id: ConfigureIp
    intent: Configure IP settings on cluster nodes
    question: How do I assign IP addresses to an interface on cluster nodes?
  - id: UnconfigureIp
    intent: Remove IP settings from cluster nodes
    question: How do I remove the IP configuration from an interface?
  phrasing_ops: 2
  slug: cohesity-ip-api
- baseURL: https://helios.cohesity.com/irisservices/api/v1/public/
  baseurl_source: declared
  description: The Kerberos Providers API from Cohesity — 4 operation(s) for kerberos providers.
  name: Cohesity Kerberos Providers API
  phrasing_intents:
  - id: GetKerberosProviders
    intent: List Kerberos providers
    question: Which Kerberos realms are registered on my cluster?
  - id: RegisterKerberosProvider
    intent: Register a Kerberos provider
    question: How do I connect the cluster to a Kerberos realm?
  - id: UnregisterKerberosProvider
    intent: Unregister a Kerberos provider
    question: How do I disconnect the cluster from a Kerberos realm?
  - id: GetKerberosProviderById
    intent: Get a Kerberos provider
    question: What realm and KDCs does a specific Kerberos provider use?
  - id: UpdateKerberosProvider
    intent: Update a Kerberos provider registration
    question: Can I change the KDC servers on an existing Kerberos registration?
  phrasing_ops: 5
  slug: cohesity-kerberos-providers-api
- baseURL: https://helios.cohesity.com/irisservices/api/v1/public/
  baseurl_source: declared
  description: The Keystone API from Cohesity — 2 operation(s) for keystone.
  name: Cohesity Keystone API
  phrasing_intents:
  - id: GetKeystones
    intent: List Keystone configurations
    question: Which OpenStack Keystone configurations are set up on my cluster?
  - id: CreateKeystone
    intent: Create a Keystone configuration
    question: How do I add a Keystone identity configuration to the cluster?
  - id: GetKeystonesById
    intent: Get one Keystone configuration
    question: What settings does a specific Keystone config have?
  - id: UpdateKeystone
    intent: Update a Keystone configuration
    question: How do I change an existing Keystone configuration?
  - id: DeleteKeystone
    intent: Delete a Keystone configuration
    question: How do I delete a Keystone configuration?
  phrasing_ops: 5
  slug: cohesity-keystone-api
- baseURL: https://helios.cohesity.com/irisservices/api/v1/public/
  baseurl_source: declared
  description: The KmsConfigurationResponse API from Cohesity — 1 operation(s) for kmsconfigurationresponse.
  name: Cohesity Kms Configuration Response API
  phrasing_intents:
  - id: GetKmsConfig
    intent: List KMS configurations
    question: Which key management servers is my cluster configured to use?
  phrasing_ops: 1
  slug: cohesity-kmsconfigurationresponse-api
- baseURL: https://helios.cohesity.com/irisservices/api/v1/public/
  baseurl_source: declared
  description: The KmsUpdateRequestParameters API from Cohesity — 1 operation(s) for kmsupdaterequestparameters.
  name: Cohesity Kms Update Request Parameters API
  phrasing_intents:
  - id: UpdateKmsConfig
    intent: Update a key management server configuration
    question: How do I change the settings of a KMS server the cluster uses for encryption keys?
  phrasing_ops: 1
  slug: cohesity-kmsupdaterequestparameters-api
- baseURL: https://helios.cohesity.com/irisservices/api/v1/public/
  baseurl_source: declared
  description: The LdapProvider API from Cohesity — 3 operation(s) for ldapprovider.
  name: Cohesity Ldap Provider API
  phrasing_intents:
  - id: GetLdapProvider
    intent: List LDAP providers
    question: Which LDAP providers are configured on the cluster?
  - id: UpdateLdapProvider
    intent: Update an LDAP provider
    question: How do I change the bind credentials an LDAP provider uses?
  - id: CreateLdapProvider
    intent: Add an LDAP provider
    question: How do I connect the cluster to an LDAP directory?
  - id: DeleteLdapProvider
    intent: Delete an LDAP provider
    question: How do I remove an LDAP provider from the cluster?
  - id: GetLdapProviderStatus
    intent: Check an LDAP provider's connection status
    question: Is the cluster able to reach its LDAP servers?
  phrasing_ops: 5
  slug: cohesity-ldapprovider-api
- baseURL: https://helios.cohesity.com/irisservices/api/v1/public/
  baseurl_source: declared
  description: The License API from Cohesity — 1 operation(s) for license.
  name: Cohesity License API
  phrasing_intents:
  - id: LicenseUsage
    intent: Get cluster license usage
    question: How much of my licensed capacity is the cluster using?
  phrasing_ops: 1
  slug: cohesity-license-api
- baseURL: https://helios.cohesity.com/irisservices/api/v1/public/
  baseurl_source: declared
  description: The Miscellaneous API from Cohesity — 1 operation(s) for miscellaneous.
  name: Cohesity Miscellaneous API
  phrasing_intents:
  - id: FilterObjects
    intent: Filter SQL objects by regex or wildcard
    question: Can I filter SQL databases using wildcards or regular expressions?
  phrasing_ops: 1
  slug: cohesity-miscellaneous-api
- baseURL: https://helios.cohesity.com/irisservices/api/v1/public/
  baseurl_source: declared
  description: The Monitoring API from Cohesity — 3 operation(s) for monitoring.
  name: Cohesity Monitoring API
  phrasing_intents:
  - id: GetJobRunInfo
    intent: Get details of a single job run
    question: What happened during one particular backup job run?
  - id: GetAllJobRuns
    intent: List job runs in a time range
    question: Which jobs ran on the cluster between two points in time?
  - id: GetRunObjectsDetails
    intent: List objects processed in a job run
    question: Which objects were backed up in a given job run, and how did each do?
  phrasing_ops: 3
  slug: cohesity-monitoring-api
- baseURL: https://helios.cohesity.com/irisservices/api/v1/public/
  baseurl_source: declared
  description: The Network API from Cohesity — 3 operation(s) for network.
  name: Cohesity Network API
  phrasing_intents:
  - id: CreateBond
    intent: Create a network bond on a node
    question: How do I bond network interfaces on a node before it joins a cluster?
  - id: DeleteBond
    intent: Delete a network bond
    question: How do I remove a network bond from a node?
  - id: ListHosts
    intent: List entries in the cluster hosts file
    question: What's currently in the cluster's /etc/hosts file?
  - id: EditHosts
    intent: Edit existing hosts file entries
    question: How do I change the IP of a hostname already in the cluster hosts file?
  - id: AppendHosts
    intent: Add new hosts file entries
    question: How do I add a new hostname mapping to the cluster's /etc/hosts?
  - id: DeleteHosts
    intent: Remove hosts file entries by IP
    question: How do I delete entries from the cluster hosts file?
  phrasing_ops: 6
  slug: cohesity-network-api
- baseURL: https://helios.cohesity.com/irisservices/api/v1/public/
  baseurl_source: declared
  description: The Network Information Service (NIS) API from Cohesity — 4 operation(s) for network information service (nis).
  name: Cohesity Network Information Service (NIS) API
  phrasing_intents:
  - id: GetNisNetgroups
    intent: List NIS netgroups
    question: Which NIS netgroups are configured on my cluster?
  - id: CreateNisNetgroup
    intent: Create an NIS netgroup
    question: How do I add an NIS netgroup to control NFS access?
  - id: GetNisNetgroupByName
    intent: Get one NIS netgroup
    question: What NFS access does a specific netgroup grant?
  - id: UpdateNisNetgroupByName
    intent: Update an NIS netgroup
    question: How do I change the NFS access level of an existing netgroup?
  - id: DeleteNisNetgroupByName
    intent: Delete an NIS netgroup
    question: How do I remove an NIS netgroup from the cluster?
  - id: GetNisProviders
    intent: List NIS providers
    question: Which NIS servers is my cluster configured to use?
  - id: CreateNisProvider
    intent: Add an NIS provider
    question: How do I connect my cluster to an NIS domain?
  - id: GetNisProviderByDomainName
    intent: Get an NIS provider by domain
    question: Which master server is set for a given NIS domain?
  phrasing_ops: 10
  slug: cohesity-network-information-service-nis-api
- baseURL: https://helios.cohesity.com/irisservices/api/v1/public/
  baseurl_source: declared
  description: The network-reset API from Cohesity — 2 operation(s) for network-reset.
  name: Cohesity Network Reset API
  phrasing_intents:
  - id: ResetNodesNetwork
    intent: Reset node networking to factory state
    question: How do I reset all cluster nodes' networking back to factory defaults?
  - id: GetNetworkResetStates
    intent: Check node network reset status
    question: Which nodes have finished their network reset?
  phrasing_ops: 2
  slug: cohesity-network-reset-api
- baseURL: https://helios.cohesity.com/irisservices/api/v1/public/
  baseurl_source: declared
  description: The Nodes API from Cohesity — 5 operation(s) for nodes.
  name: Cohesity Nodes API
  phrasing_intents:
  - id: ListFreeNodes
    intent: List free nodes on the network
    question: Which unclustered Cohesity nodes are available on the network to add?
  - id: GetNodeStatus
    intent: Get the status of a node
    question: Is the node I'm talking to healthy and what state is it in?
  - id: GetNodes
    intent: List cluster nodes
    question: Which nodes make up my Cohesity cluster?
  - id: UpgradeNode
    intent: Upgrade node software
    question: Can I upgrade a node to a specific software version?
  - id: GetNodeById
    intent: Get one node's details
    question: What are the details of a specific node in the cluster?
  phrasing_ops: 5
  slug: cohesity-nodes-api
- baseURL: https://helios.cohesity.com/irisservices/api/v1/public/
  baseurl_source: declared
  description: The Notifications API from Cohesity — 1 operation(s) for notifications.
  name: Cohesity Notifications API
  phrasing_intents:
  - id: GetNotifications
    intent: List my notifications
    question: What notifications are waiting for me on the cluster?
  - id: UpdateNotifications
    intent: Dismiss or act on my notifications
    question: How do I dismiss notifications I have already seen?
  phrasing_ops: 2
  slug: cohesity-notifications-api
- baseURL: https://helios.cohesity.com/irisservices/api/v1/public/
  baseurl_source: declared
  description: The Objects API from Cohesity — 21 operation(s) for objects.
  name: Cohesity Objects API
  phrasing_intents:
  - id: GetProtectedObjectsOfAnyType
    intent: List object protection configurations
    question: Which objects are protected on my cluster and by which policies?
  - id: ObjectsActions
    intent: Link or unlink multiple objects
    question: Can I perform a bulk action across several objects at once?
  - id: GetObjectsLastRun
    intent: Get the last protection run of objects
    question: When was each object last backed up?
  - id: CancelObjectRuns
    intent: Cancel object-based protection runs
    question: How do I cancel backup runs for specific objects?
  - id: GetProtectedObjectOfAnyTypeById
    intent: Get one object's protection configuration
    question: What is the protection configuration of a single object?
  - id: PerformActionOnObject
    intent: Perform an action on one object
    question: What actions can I take on a single object depending on its environment?
  - id: GetPITRangesForProtectedObject
    intent: Get point-in-time restore ranges
    question: Which time ranges can a protected object be restored to at any point in time?
  - id: GetObjectRuns
    intent: List protection runs for an object
    question: What backup runs have happened for a particular object?
  phrasing_ops: 21
  slug: cohesity-objects-api
- baseURL: https://helios.cohesity.com/irisservices/api/v1/public/
  baseurl_source: declared
  description: The Packages API from Cohesity — 2 operation(s) for packages.
  name: Cohesity Packages API
  phrasing_intents:
  - id: ListPackages
    intent: List installed software packages
    question: Which software packages are installed on my cluster?
  - id: DownloadPackage
    intent: Download a software package to the cluster
    question: How do I get an upgrade package onto the cluster from a URL?
  phrasing_ops: 2
  slug: cohesity-packages-api
- baseURL: https://helios.cohesity.com/irisservices/api/v1/public/
  baseurl_source: declared
  description: The Patches API from Cohesity — 4 operation(s) for patches.
  name: Cohesity Patches API
  phrasing_intents:
  - id: GetAppliedPatches
    intent: List patches currently applied
    question: Which patches are running on my cluster right now?
  - id: RevertPatches
    intent: Revert an applied patch
    question: How do I roll back a patch that caused problems?
  - id: GetAvailablePatches
    intent: List patches ready to apply
    question: What patches have been imported and are ready to install?
  - id: ImportPatches
    intent: Upload a patch or hotfix
    question: How do I upload a hotfix file to the cluster?
  - id: ApplyPatches
    intent: Apply available patches
    question: How do I install the patch for one service along with its dependencies?
  - id: GetPatchOperationStatus
    intent: Check patch operation progress
    question: Is a patch install still running, and did the last one succeed?
  - id: GetPatchesHistory
    intent: View patch management history
    question: What patches have been applied or reverted on the cluster over time?
  phrasing_ops: 7
  slug: cohesity-patches-api
- baseURL: https://helios.cohesity.com/irisservices/api/v1/public/
  baseurl_source: declared
  description: The Platform API from Cohesity — 26 operation(s) for platform.
  name: Cohesity Platform API
  phrasing_intents:
  - id: GetAlertSummary
    intent: Summarize cluster alerts by category
    question: What does the alert summary for my Cohesity cluster look like, grouped by category?
  - id: GetChassis
    intent: List the chassis in the cluster
    question: Which hardware chassis are part of my cluster?
  - id: GetChassisById
    intent: Get details of one chassis
    question: What hardware model and serial number does a particular chassis have?
  - id: UpdateChassisById
    intent: Update a chassis's name or rack assignment
    question: How do I rename a chassis in my cluster?
  - id: GetCluster
    intent: Get the cluster configuration summary
    question: What is the current configuration of my Cohesity cluster?
  - id: UpdateCluster
    intent: Update an existing cluster's configuration
    question: How do I change the name or description of an existing cluster?
  - id: CreateCluster
    intent: Create a new cluster
    question: How do I create a new physical, virtual or cloud cluster?
  - id: GetAMQPTargetConfig
    intent: View the cluster's AMQP target config
    question: Which AMQP server is my cluster sending messages to?
  phrasing_ops: 47
  slug: cohesity-platform-api
- baseURL: https://helios.cohesity.com/irisservices/api/v1/public/
  baseurl_source: declared
  description: The Preferences API from Cohesity — 1 operation(s) for preferences.
  name: Cohesity Preferences API
  phrasing_intents:
  - id: GetUserPreferences
    intent: Show my user preferences
    question: What preferences are saved for my logged-in user?
  - id: UpdateUserPreferences
    intent: Replace all my user preferences
    question: Can I overwrite my whole set of user preferences at once?
  - id: PatchUserPreferences
    intent: Change specific user preferences
    question: Can I change just one preference without touching the others?
  phrasing_ops: 3
  slug: cohesity-preferences-api
- baseURL: https://helios.cohesity.com/irisservices/api/v1/public/
  baseurl_source: declared
  description: The Principals API from Cohesity — 10 operation(s) for principals.
  name: Cohesity Principals API
  phrasing_intents:
  - id: ListSourcesForPrincipals
    intent: See which sources and views principals can access
    question: Which protection sources and views can a given user or group access?
  - id: UpdateSourcesForPrincipals
    intent: Grant principals access to sources and views
    question: How do I give an Active Directory group access to specific VMs and views?
  - id: SearchPrincipals
    intent: Search users and groups in a domain
    question: Can I find Active Directory users or groups whose names contain a substring?
  - id: GetSessionUser
    intent: Get the logged-in user
    question: Who am I logged in as on the Cohesity cluster?
  - id: GetUsers
    intent: List cluster users
    question: Which users have accounts on my cluster?
  - id: UpdateUser
    intent: Update a cluster user's settings
    question: How do I change a user's roles on the cluster without touching Active Directory?
  - id: CreateUser
    intent: Add a user to the cluster
    question: How do I add an Active Directory user to my Cohesity cluster?
  - id: DeleteUsers
    intent: Delete users from the cluster
    question: Does removing a user from the cluster also delete them in Active Directory?
  phrasing_ops: 17
  slug: cohesity-principals-api
- baseURL: https://helios.cohesity.com/irisservices/api/v1/public/
  baseurl_source: declared
  description: The Privileges API from Cohesity — 1 operation(s) for privileges.
  name: Cohesity Privileges API
  phrasing_intents:
  - id: GetPrivileges
    intent: List privileges on the cluster
    question: What privileges exist that I can assign to roles?
  phrasing_ops: 1
  slug: cohesity-privileges-api
- baseURL: https://helios.cohesity.com/irisservices/api/v1/public/
  baseurl_source: declared
  description: The Protected Objects API from Cohesity — 3 operation(s) for protected objects.
  name: Cohesity Protected Objects API
  phrasing_intents:
  - id: ProtectObjectsOfAnyType
    intent: Back up objects of any type
    question: Can I protect any kind of object with object-level backup?
  - id: PerformActionOnProtectObjects
    intent: Pause, resume, run or unprotect objects
    question: Can I pause or resume backups on protected objects in bulk?
  - id: UpdateProtectedObjectsOfAnyType
    intent: Update an object backup configuration
    question: Can I change the backup settings of one protected object by its id?
  phrasing_ops: 3
  slug: cohesity-protected-objects-api
- baseURL: https://helios.cohesity.com/irisservices/api/v1/public/
  baseurl_source: declared
  description: The ProtectionJobs API from Cohesity — 6 operation(s) for protectionjobs.
  name: Cohesity Protection Jobs API
  phrasing_intents:
  - id: ChangeProtectionJobState
    intent: Pause or resume a protection job
    question: How do I pause a backup job so no new runs start?
  - id: GetProtectionJobs
    intent: List protection jobs
    question: Which backup jobs on the cluster protect VMware workloads?
  - id: CreateProtectionJob
    intent: Create a protection job
    question: How do I set up a new backup job for a set of VMs?
  - id: RunProtectionJob
    intent: Run a protection job now
    question: Can I kick off a backup immediately instead of waiting for the schedule?
  - id: UpdateProtectionJobsState
    intent: Pause, resume or deactivate many jobs at once
    question: How do I pause every backup job in a list with a single request?
  - id: GetProtectionJobById
    intent: Get a protection job
    question: What sources and policy does a specific protection job use?
  - id: UpdateProtectionJob
    intent: Update a protection job
    question: How do I switch an existing backup job to a different policy?
  - id: DeleteProtectionJob
    intent: Delete a protection job
    question: When I delete a backup job, are its snapshots deleted too?
  phrasing_ops: 9
  slug: cohesity-protectionjobs-api
- baseURL: https://helios.cohesity.com/irisservices/api/v1/public/
  baseurl_source: declared
  description: The ProtectionObjects API from Cohesity — 2 operation(s) for protectionobjects.
  name: Cohesity Protection Objects API
  phrasing_intents:
  - id: UpdateProtectionObject
    intent: Update a protected object's settings
    question: Can I pause backups for a single protected object?
  - id: ProtectObject
    intent: Protect objects under an RPO policy
    question: How do I start protecting a VM or server with an RPO policy?
  - id: UnprotectObject
    intent: Unprotect an object from an RPO policy
    question: Can I stop protecting an object and also delete its existing snapshots?
  - id: GetProtectionObjectSummary
    intent: Get a protected object's job summary
    question: Which protection job is backing up a given object, and how is it protected?
  phrasing_ops: 4
  slug: cohesity-protectionobjects-api
- baseURL: https://helios.cohesity.com/irisservices/api/v1/public/
  baseurl_source: declared
  description: The ProtectionRuns API from Cohesity — 3 operation(s) for protectionruns.
  name: Cohesity Protection Runs API
  phrasing_intents:
  - id: GetProtectionRuns
    intent: List protection job runs
    question: Which backup job runs happened recently on my cluster?
  - id: UpdateProtectionRuns
    intent: Change retention of protection job runs
    question: How do I extend how long a backup run's snapshots are kept?
  - id: CancelProtectionJobRun
    intent: Cancel a protection job run
    question: How do I cancel a backup job run that's in progress?
  - id: GetProtectionRunErrors
    intent: List errors from a protection job run task
    question: Why did a backup job run task fail?
  phrasing_ops: 4
  slug: cohesity-protectionruns-api
- baseURL: https://helios.cohesity.com/irisservices/api/v1/public/
  baseurl_source: declared
  description: The ProtectionSources API from Cohesity — 26 operation(s) for protectionsources.
  name: Cohesity Protection Sources API
  phrasing_intents:
  - id: DownloadPhysicalAgent
    intent: Download the backup agent installer for a host
    question: Where can I get the Cohesity agent installer for a Linux or Windows server?
  - id: UpgradePhysicalAgents
    intent: Upgrade agents on physical servers
    question: After upgrading the cluster, how do I bring the agents on my physical servers up to the same release?
  - id: ListProtectionSources
    intent: Browse registered sources and their object trees
    question: How can I see every registered source along with the VMs, folders and databases underneath it?
  - id: ListApplicationServers
    intent: List application servers registered under a source
    question: Which SQL or Exchange application servers are registered under my vCenter source?
  - id: UpdateApplicationServers
    intent: Change application server registration settings
    question: How do I change the credentials Cohesity uses for an already registered SQL host?
  - id: RegisterApplicationServers
    intent: Register a host as running SQL or Exchange
    question: How do I tell Cohesity that a protected host is running Microsoft SQL Server so it can back up the databases?
  - id: UnregisterApplicationServers
    intent: Unregister application servers from a source
    question: Why would unregistering the SQL application on a host fail while a backup is running?
  - id: ListDataStoreInformation
    intent: Show datastores used by a VMware VM
    question: Which VMware datastores does a particular virtual machine live on?
  phrasing_ops: 32
  slug: cohesity-protectionsources-api
- baseURL: https://helios.cohesity.com/irisservices/api/v1/public/
  baseurl_source: declared
  description: The Recoveries API from Cohesity — 8 operation(s) for recoveries.
  name: Cohesity Recoveries API
  phrasing_intents:
  - id: GetRecoveries
    intent: List recoveries
    question: Which recoveries ran on the cluster in the last week, and did they succeed?
  - id: CreateRecovery
    intent: Start a recovery
    question: How do I start a recovery from a snapshot with the data-protect API?
  - id: CreateDownloadFilesAndFoldersRecovery
    intent: Create a download recovery for files
    question: Can I prepare specific files and folders from a backup for download as a recovery?
  - id: GetRecoveryById
    intent: Get a recovery
    question: What is the status of a specific recovery?
  - id: CancelRecoveryById
    intent: Cancel a recovery
    question: Can I stop a recovery that's still running?
  - id: GetRecoveryDebugLogs
    intent: Get debug logs for a recovery
    question: Where can I find debug logs to troubleshoot a failed recovery?
  - id: DownloadFilesFromRecovery
    intent: Download files from a download recovery
    question: Once a download recovery is ready, how do I fetch the files?
  - id: TearDownRecoveryById
    intent: Tear down a recovery
    question: Can I clean up mounts and clones left behind by a finished recovery?
  phrasing_ops: 9
  slug: cohesity-recoveries-api
- baseURL: https://helios.cohesity.com/irisservices/api/v1/public/
  baseurl_source: declared
  description: The RemoteCluster API from Cohesity — 3 operation(s) for remotecluster.
  name: Cohesity Remote Cluster API
  phrasing_intents:
  - id: GetRemoteClusters
    intent: List registered remote clusters
    question: Which remote clusters is this cluster paired with for replication?
  - id: CreateRemoteCluster
    intent: Register a remote cluster for replication
    question: How do I pair two Cohesity clusters so one can replicate snapshots to the other?
  - id: GetRemoteClusterById
    intent: Get a registered remote cluster
    question: What are the connection settings for one paired remote cluster?
  - id: UpdateRemoteCluster
    intent: Update a remote cluster's connection settings
    question: How do I change the IPs or password used to reach a paired remote cluster?
  - id: DeleteRemoteCluster
    intent: Unregister a remote cluster
    question: How do I unpair a remote cluster from this one?
  - id: GetReplicationEncryptionKey
    intent: Get the replication encryption key
    question: What encryption key does this cluster use for replication traffic?
  phrasing_ops: 6
  slug: cohesity-remotecluster-api
- baseURL: https://helios.cohesity.com/irisservices/api/v1/public/
  baseurl_source: declared
  description: The RemoteRestore API from Cohesity — 5 operation(s) for remoterestore.
  name: Cohesity Remote Restore API
  phrasing_intents:
  - id: UploadVaultEncryptionKeys
    intent: Upload encryption keys for a remote vault
    question: How do I give the cluster the encryption keys needed to restore from a remote vault?
  - id: ListRemoteVaultRestoreTasks
    intent: List remote vault restore tasks
    question: Which CloudRetrieve restores from remote vaults are running or done?
  - id: CreateRemoteVaultRestoreTask
    intent: Restore archived data from a remote vault
    question: After searching a remote vault, how do I restore the indexes and snapshots it found?
  - id: GetRemoteVaultSearchJobResults
    intent: Get job runs found by a vault search
    question: Which protection job runs did my remote vault search find?
  - id: ListRemoteVaultSearchJobs
    intent: List searches of remote vaults
    question: What remote vault searches have been run on this cluster?
  - id: CreateRemoteVaultSearchJob
    intent: Search a remote vault for archived jobs
    question: How do I find protection jobs archived to a vault so I can restore them elsewhere?
  - id: StopRemoteVaultSearchJob
    intent: Stop a remote vault search
    question: How do I cancel a vault search that's taking too long?
  - id: ListRemoteVaultSearchJobById
    intent: Get one remote vault search
    question: What's the status of a specific remote vault search?
  phrasing_ops: 8
  slug: cohesity-remoterestore-api
- baseURL: https://helios.cohesity.com/irisservices/api/v1/public/
  baseurl_source: declared
  description: The Reports API from Cohesity — 12 operation(s) for reports.
  name: Cohesity Reports API
  phrasing_intents:
  - id: GetAgentDeploymentReport
    intent: Report on installed agents and their health
    question: Which Cohesity agents are unhealthy or need an upgrade?
  - id: GetDataTransferFromVaultsReportRequest
    intent: Report data pulled back from vaults
    question: How much data has been transferred from my cloud vaults back to the cluster?
  - id: GetDataTransferToVaultsReportRequest
    intent: Report data sent to vaults
    question: How much data has the cluster archived out to each external target?
  - id: GetGdprReport
    intent: Get the GDPR access report
    question: Which users can access objects that hold personal data?
  - id: GetProtectedObjectsTrendsReportRequest
    intent: Report protection trends over time
    question: How has protection of my objects trended week over week?
  - id: GetProtectionSourcesJobRunsReportRequest
    intent: Report backup snapshots for specific objects
    question: Which snapshots exist for a particular VM, and were they successful?
  - id: GetProtectionSourcesJobsSummaryReportRequest
    intent: Summarize snapshot stats per protected object
    question: Which objects have failed backups several times in a row?
  - id: GetReportType
    intent: Describe a report type's properties
    question: What properties does a given report type expose?
  phrasing_ops: 12
  slug: cohesity-reports-api
- baseURL: https://helios.cohesity.com/irisservices/api/v1/public/
  baseurl_source: declared
  description: The RestoreTasks API from Cohesity — 27 operation(s) for restoretasks.
  name: Cohesity Restore Tasks API
  phrasing_intents:
  - id: GetAdDomainRootTopology
    intent: Get the root topology of an AD domain restore
    question: What does the root topology of the Active Directory domain look like in my AD restore task?
  - id: CompareAdObjects
    intent: Compare AD object attributes snapshot vs production
    question: Which attributes of an Active Directory object differ between the backup snapshot and production AD?
  - id: SearchAdObjects
    intent: Browse AD objects in snapshot and production
    question: Which AD objects under a given base DN are missing from production compared to the snapshot?
  - id: SearchProductionAdObjects
    intent: Look up production AD objects by GUID, SAM or DN
    question: Can I look up live production AD objects by their object GUIDs or SAM account names?
  - id: GetAdObjects
    intent: Search backed-up AD objects to recover
    question: Which backed-up Active Directory users or groups can I recover, searching by name or email?
  - id: AdObjectsRestoreStatus
    intent: Check restore status of recovered AD objects
    question: Did the AD objects I restored from the snapshot make it back into production?
  - id: CreateApplicationsCloneTask
    intent: Clone an application such as a SQL database
    question: Can I clone a backed-up SQL Server database onto a host for test or dev use?
  - id: CreateApplicationsRecoverTask
    intent: Recover an application such as a SQL database
    question: How do I restore a SQL Server database from a Cohesity backup back to its host?
  phrasing_ops: 30
  slug: cohesity-restoretasks-api
- baseURL: https://helios.cohesity.com/irisservices/api/v1/public/
  baseurl_source: declared
  description: The Roles API from Cohesity — 2 operation(s) for roles.
  name: Cohesity Roles API
  phrasing_intents:
  - id: GetRoles
    intent: List roles on the cluster
    question: What roles are defined on my Cohesity cluster and what privileges do they carry?
  - id: CreateRole
    intent: Create a custom role
    question: How do I create a custom role with a specific set of privileges?
  - id: DeleteRoles
    intent: Delete custom roles
    question: How do I delete custom roles I no longer need?
  - id: UpdateRole
    intent: Update a custom role
    question: How do I change the privileges assigned to a custom role?
  phrasing_ops: 4
  slug: cohesity-roles-api
- baseURL: https://helios.cohesity.com/irisservices/api/v1/public/
  baseurl_source: declared
  description: The Routes API from Cohesity — 1 operation(s) for routes.
  name: Cohesity Routes API
  phrasing_intents:
  - id: GetRoutes
    intent: List static routes
    question: Which static routes are configured on the cluster?
  - id: AddRoute
    intent: Add a static route
    question: How do I add a static route to a destination network?
  - id: DeleteRoute
    intent: Delete a static route
    question: How do I remove a static route from the cluster?
  phrasing_ops: 3
  slug: cohesity-routes-api
- baseURL: https://helios.cohesity.com/irisservices/api/v1/public/
  baseurl_source: declared
  description: The Scheduler API from Cohesity — 1 operation(s) for scheduler.
  name: Cohesity Scheduler API
  phrasing_intents:
  - id: GetSchedulerJobs
    intent: List scheduled email reports
    question: Which reports are scheduled to be emailed automatically?
  - id: UpdateSchedulerJob
    intent: Update a scheduled email report
    question: How do I change how often a scheduled report is emailed?
  - id: CreateSchedulerJob
    intent: Schedule a report to be emailed
    question: Can I have a backup report emailed to my team every week?
  - id: DeleteSchedulerJobs
    intent: Delete scheduled email reports
    question: How do I unschedule and delete email report jobs?
  phrasing_ops: 4
  slug: cohesity-scheduler-api
- baseURL: https://helios.cohesity.com/irisservices/api/v1/public/
  baseurl_source: declared
  description: The Schedules API from Cohesity — 4 operation(s) for schedules.
  name: Cohesity Schedules API
  phrasing_intents:
  - id: GetSchedules
    intent: List report schedules
    question: Which report schedules are currently active?
  - id: CreateSchedule
    intent: Schedule a report for delivery
    question: How do I get a report emailed to my team every week?
  - id: GetScheduleById
    intent: Get a report schedule
    question: How do I see the details of one report schedule?
  - id: UpdateSchedule
    intent: Change a report schedule
    question: Can I change who receives a scheduled report?
  - id: DeleteSchedule
    intent: Delete a report schedule
    question: How do I stop a report from being sent permanently?
  - id: RunScheduleOnDemand
    intent: Send a scheduled report now
    question: Can I trigger a scheduled report immediately instead of waiting?
  - id: UpdateSchedulesState
    intent: Activate or deactivate report schedules
    question: Can I pause several report schedules at once?
  phrasing_ops: 7
  slug: cohesity-schedules-api
- baseURL: https://helios.cohesity.com/irisservices/api/v1/public/
  baseurl_source: declared
  description: The Search API from Cohesity — 5 operation(s) for search.
  name: Cohesity Search API
  phrasing_intents:
  - id: SearchProtectionRuns
    intent: Find an object's latest snapshot across targets
    question: Where is the latest snapshot of an object stored across all targets?
  - id: SearchProtectionSources
    intent: Search registered protection sources
    question: Which registered sources match a name, and are they protected?
  - id: SearchIndexedObjects
    intent: Search indexed files, emails and folders
    question: How do I find a specific file or email inside my backups?
  - id: SearchObjects
    intent: Search objects across sources
    question: Which VMs or databases match a name, protected or not?
  - id: SearchProtectedObjects
    intent: Search protected objects and their snapshots
    question: Which protected objects match a name and what snapshots do they have?
  phrasing_ops: 5
  slug: cohesity-search-api
- baseURL: https://helios.cohesity.com/irisservices/api/v1/public/
  baseurl_source: declared
  description: The Security API from Cohesity — 10 operation(s) for security.
  name: Cohesity Security API
  phrasing_intents:
  - id: CreateClientcsr
    intent: Create client and server CSR pair
    question: How do I generate both a client and a server certificate signing request at once?
  - id: ImportCertificateByClientcsr
    intent: Import signed client and server certificates
    question: Once my CA signs the client/server CSR pair, how do I load both certificates back?
  - id: GetCsrList
    intent: List certificate signing requests
    question: Which certificate signing requests are pending on the cluster?
  - id: CreateCsr
    intent: Create a single certificate signing request
    question: How do I generate one CSR for a cluster service's certificate?
  - id: UpdateCertificateByCsr
    intent: Install a signed certificate for a CSR
    question: Where do I upload the certificate my CA returned for a single CSR?
  - id: GetCsrById
    intent: Get a certificate signing request
    question: Can I view the contents of one CSR so I can send it to my CA?
  - id: DeleteCsr
    intent: Delete a certificate signing request
    question: How do I discard a CSR so I can create a new one for the same service?
  - id: GetSecurityConfig
    intent: Get cluster security settings
    question: What password strength and lockout rules are set on my cluster?
  phrasing_ops: 16
  slug: cohesity-security-api
- baseURL: https://helios.cohesity.com/irisservices/api/v1/public/
  baseurl_source: declared
  description: The Sites API from Cohesity — 2 operation(s) for sites.
  name: Cohesity Sites API
  phrasing_intents:
  - id: SCGetSites
    intent: List DR sites
    question: Which disaster recovery sites are available?
  - id: SCCreateSite
    intent: Create a DR site
    question: How do I add a new on-prem site for a cluster?
  - id: SCGetSiteById
    intent: Get one DR site
    question: What location and type does a particular site have?
  - id: SCDeleteSiteById
    intent: Delete a DR site
    question: How do I delete a site I no longer use?
  - id: SCUpdateSiteById
    intent: Rename or relocate a DR site
    question: How do I rename an existing site?
  phrasing_ops: 5
  slug: cohesity-sites-api
- baseURL: https://helios.cohesity.com/irisservices/api/v1/public/
  baseurl_source: declared
  description: The SMBFileOpens API from Cohesity — 1 operation(s) for smbfileopens.
  name: Cohesity SMB File Opens API
  phrasing_intents:
  - id: GetSmbFileOpens
    intent: List active SMB file opens
    question: Which files are currently open over SMB on my views?
  - id: CloseSmbFileOpen
    intent: Close an active SMB file open
    question: Can I force-close a file someone has locked over SMB?
  phrasing_ops: 2
  slug: cohesity-smbfileopens-api
- baseURL: https://helios.cohesity.com/irisservices/api/v1/public/
  baseurl_source: declared
  description: The Statistics API from Cohesity — 6 operation(s) for statistics.
  name: Cohesity Statistics API
  phrasing_intents:
  - id: GetEntities
    intent: List entities for a statistics schema
    question: Which disks or nodes can I pull metrics for under a given schema?
  - id: GetEntitiesSchema
    intent: List statistics entity schemas
    question: What metric schemas does the cluster track?
  - id: GetEntitySchemaByName
    intent: Get one statistics entity schema
    question: What attributes and metrics are defined for a specific schema?
  - id: GetTimeSeriesSchema
    intent: Get the time series schema for an entity
    question: Which time series data points are available for a particular node or cluster entity?
  - id: GetTimeSeriesStats
    intent: Get metric time series for an entity
    question: What was disk latency on a node over the last day?
  - id: GetTasks
    intent: Check progress of cluster tasks
    question: What background tasks is the cluster working on and how far along are they?
  phrasing_ops: 6
  slug: cohesity-statistics-api
- baseURL: https://helios.cohesity.com/irisservices/api/v1/public/
  baseurl_source: declared
  description: The Stats API from Cohesity — 17 operation(s) for stats.
  name: Cohesity Stats API
  phrasing_intents:
  - id: GetActiveAlertsStats
    intent: Get statistics on active alerts
    question: How many active alerts did my cluster raise over the past week?
  - id: GetConsumerStats
    intent: Get storage consumption by consumer
    question: Which protection jobs or views are consuming the most storage?
  - id: GetFileDistributionStats
    intent: Get file distribution statistics
    question: What does the file size and type distribution look like on my cluster?
  - id: GetProtectionRunsStats
    intent: Count protection runs by status (v1 public)
    question: How many protection runs failed in a given window, using the older public stats endpoint?
  - id: GetLastProtectionRunStats
    intent: Get stats on each job's last protection run
    question: How did the most recent run of every protection job go?
  - id: GetProtectedObjectsSummary
    intent: Summarize protected objects on the cluster
    question: How many objects on my cluster are protected versus unprotected?
  - id: GetRestoreStats
    intent: Get statistics on restore tasks
    question: How many restores ran on my cluster this month?
  - id: GetStorageStats
    intent: Get cluster storage statistics
    question: How much storage capacity is used and free on my cluster?
  phrasing_ops: 17
  slug: cohesity-stats-api
- baseURL: https://helios.cohesity.com/irisservices/api/v1/public/
  baseurl_source: declared
  description: The StorageDomains API from Cohesity — 1 operation(s) for storagedomains.
  name: Cohesity Storage Domains API
  phrasing_intents:
  - id: DeleteStorageDomain
    intent: Delete a storage domain
    question: How do I delete a storage domain I no longer need?
  phrasing_ops: 1
  slug: cohesity-storagedomains-api
- baseURL: https://helios.cohesity.com/irisservices/api/v1/public/
  baseurl_source: declared
  description: The Tags API from Cohesity — 4 operation(s) for tags.
  name: Cohesity Tags API
  phrasing_intents:
  - id: ApplyTags
    intent: Apply tags to backed-up objects
    question: Can I tag files or snapshots from a backup job run so they are easier to find?
  - id: RemoveTags
    intent: Remove tags from backed-up objects
    question: Can I take tags off backed-up files or snapshots?
  - id: GetTags
    intent: List tags
    question: Which tags are defined on the cluster, by name or namespace?
  - id: CreateTag
    intent: Create a tag
    question: How do I define a new tag with a namespace and color?
  - id: GetTagById
    intent: Get a tag
    question: What are the details of one tag?
  - id: UpdateTag
    intent: Update a tag
    question: Can I rename an existing tag or change its color?
  - id: DeleteTag
    intent: Delete a tag
    question: Can I delete a tag I no longer use?
  phrasing_ops: 7
  slug: cohesity-tags-api
- baseURL: https://helios.cohesity.com/irisservices/api/v1/public/
  baseurl_source: declared
  description: The Tasks API from Cohesity — 3 operation(s) for tasks.
  name: Cohesity Tasks API
  phrasing_intents:
  - id: GetProgressTasks
    intent: Get progress of tasks by id
    question: How far along are my running cluster tasks?
  - id: GetTasks
    intent: List report tasks
    question: Which report generation tasks ran for a schedule?
  - id: GetTaskById
    intent: Get one report task
    question: What's the status of a specific report task?
  phrasing_ops: 3
  slug: cohesity-tasks-api
- baseURL: https://helios.cohesity.com/irisservices/api/v1/public/
  baseurl_source: declared
  description: The Tenant API from Cohesity — 14 operation(s) for tenant.
  name: Cohesity Tenant API
  phrasing_intents:
  - id: GetTenants
    intent: List tenants
    question: Which tenants exist on my multitenant Cohesity cluster?
  - id: UpdateTenant
    intent: Update a tenant's details
    question: Can I rename a tenant or change its description and alert email subscription?
  - id: CreateTenant
    intent: Create a tenant
    question: How do I add a new tenant for a service-provider customer on the cluster?
  - id: DeleteTenant
    intent: Delete a tenant
    question: Can I remove a tenant from the cluster entirely?
  - id: UpdateTenantActiveDirectory
    intent: Assign AD domains to a tenant
    question: Can I give a tenant its own Active Directory domains?
  - id: UpdateTenantEntity
    intent: Grant a tenant access to source entities
    question: Can I give a tenant permission over specific protection source entities?
  - id: UpdateTenantGroups
    intent: Assign groups to a tenant
    question: Can I move existing groups into a tenant?
  - id: UpdateTenantLdapProvider
    intent: Assign LDAP providers to a tenant
    question: Can a tenant use its own LDAP providers?
  phrasing_ops: 17
  slug: cohesity-tenant-api
- baseURL: https://helios.cohesity.com/irisservices/api/v1/public/
  baseurl_source: declared
  description: The Tenants API from Cohesity — 3 operation(s) for tenants.
  name: Cohesity Tenants API
  phrasing_intents:
  - id: GetTenantSwift
    intent: Get a tenant's Swift configuration
    question: What Swift object storage settings does a tenant have?
  - id: UpdateTenantSwift
    intent: Update a tenant's Swift configuration
    question: Can I change which Keystone a tenant's Swift service uses?
  - id: RegisterSwift
    intent: Register a tenant's Swift service with Keystone
    question: How do I register Swift for a tenant on a Keystone server?
  - id: UnregisterSwift
    intent: Unregister a tenant's Swift service from Keystone
    question: How do I remove a tenant's Swift service from Keystone?
  phrasing_ops: 4
  slug: cohesity-tenants-api
- baseURL: https://helios.cohesity.com/irisservices/api/v1/public/
  baseurl_source: declared
  description: The Test Data Management API from Cohesity — 6 operation(s) for test data management.
  name: Cohesity Test Data Management API
  phrasing_intents:
  - id: GetTdmObjects
    intent: List test data management objects
    question: Which databases are being managed for test data cloning?
  - id: GetTdmObjectById
    intent: Get a test data management object
    question: How do I see details for one TDM clone object?
  - id: GetTdmTimelineEventsByObjectId
    intent: Show the timeline of a TDM object
    question: What has happened to a test data clone over time, like snapshots and refreshes?
  - id: UpdateTdmSnapshotById
    intent: Relabel a TDM snapshot
    question: Can I give a test data snapshot a friendlier label?
  - id: DeleteTdmSnapshotById
    intent: Delete a TDM snapshot
    question: How do I delete a test data snapshot I don't need anymore?
  - id: GetTdmTasks
    intent: List test data management tasks
    question: Which test data clone or refresh tasks ran in the last day?
  - id: CreateTdmTask
    intent: Start a test data management task
    question: How do I kick off a clone or refresh of test data?
  - id: GetTdmTaskById
    intent: Get a test data management task
    question: How do I check on one TDM task I started?
  phrasing_ops: 8
  slug: cohesity-test-data-management-api
- baseURL: https://helios.cohesity.com/irisservices/api/v1/public/
  baseurl_source: declared
  description: The Users API from Cohesity — 2 operation(s) for users.
  name: Cohesity Users API
  phrasing_intents:
  - id: GetSecurityPrincipals
    intent: Look up security principals by SID
    question: Which user or group does a given SID belong to?
  - id: CreateSession
    intent: Log in and create a user session
    question: How do I log in to the cluster API with a username and password?
  - id: DeleteSession
    intent: Sign out user sessions
    question: How do I force a user to be logged out everywhere?
  phrasing_ops: 3
  slug: cohesity-users-api
- baseURL: https://helios.cohesity.com/irisservices/api/v1/public/
  baseurl_source: declared
  description: The Vaults API from Cohesity — 5 operation(s) for vaults.
  name: Cohesity Vaults API
  phrasing_intents:
  - id: GetVaults
    intent: List external targets (vaults)
    question: Which external targets are registered on my Cohesity cluster?
  - id: CreateVault
    intent: Register an external target (vault)
    question: How do I add a cloud archive target to the cluster?
  - id: GetArchiveMediaInfo
    intent: Get archive media info for a tape archive
    question: What tape media does a QStar archive job use?
  - id: GetBandwidthSettings
    intent: Get external target bandwidth limits
    question: What upload and download bandwidth limits apply to my external targets?
  - id: UpdateBandwidthSettings
    intent: Update external target bandwidth limits
    question: How do I throttle upload bandwidth to my archive targets?
  - id: GetVaultEncryptionKey
    intent: Get a vault's encryption key
    question: How do I get the encryption key needed to restore archive data to another cluster?
  - id: GetVaultById
    intent: Get one external target
    question: What are the settings of a specific vault?
  - id: UpdateVault
    intent: Update an external target
    question: Can I change the compression or dedup settings of an existing vault?
  phrasing_ops: 9
  slug: cohesity-vaults-api
- baseURL: https://helios.cohesity.com/irisservices/api/v1/public/
  baseurl_source: declared
  description: The ViewBoxes API from Cohesity — 2 operation(s) for viewboxes.
  name: Cohesity View Boxes API
  phrasing_intents:
  - id: GetViewBoxes
    intent: List storage domains
    question: Which storage domains (View Boxes) exist on my cluster?
  - id: CreateViewBox
    intent: Create a storage domain
    question: How do I create a new storage domain with its own dedup and compression settings?
  - id: GetViewBoxById
    intent: Get a storage domain
    question: What are the settings and quotas of one storage domain?
  - id: UpdateViewBox
    intent: Update a storage domain
    question: How do I raise the physical quota on an existing storage domain?
  - id: DeleteViewBox
    intent: Delete a storage domain (View Box endpoint)
    question: How do I delete a View Box through the public viewBoxes endpoint?
  phrasing_ops: 5
  slug: cohesity-viewboxes-api
- baseURL: https://helios.cohesity.com/irisservices/api/v1/public/
  baseurl_source: declared
  description: The Views API from Cohesity — 24 operation(s) for views.
  name: Cohesity Views API
  phrasing_intents:
  - id: ListNlmLocks
    intent: List NLM file locks on the cluster
    question: Which NLM locks are currently held on files in my Cohesity views?
  - id: ClearNlmLocks
    intent: Clear stuck NLM file locks
    question: How do I release NLM locks a crashed NFS client left behind on a view?
  - id: GetQoSPolicies
    intent: Look up view QoS policies
    question: What Quality of Service policies can a view be assigned?
  - id: GetViewsByShareName
    intent: Find shares by share name
    question: Which SMB or NFS shares on the cluster have a name containing a given string?
  - id: GetSmbConnections
    intent: Check SMB connections to a view
    question: Who is currently connected over SMB to my views?
  - id: UpdateViewAlias
    intent: Change settings on an existing view alias
    question: Can I turn on SMB encryption for a view alias that already exists?
  - id: CreateViewAlias
    intent: Create a view alias for a directory
    question: How can I let users mount a subdirectory of a view without typing the full path?
  - id: DeleteViewAlias
    intent: Delete a view alias
    question: Can I remove a view alias without touching the view it points to?
  phrasing_ops: 43
  slug: cohesity-views-api
- baseURL: https://helios.cohesity.com/irisservices/api/v1/public/
  baseurl_source: declared
  description: The Vlan API from Cohesity — 2 operation(s) for vlan.
  name: Cohesity Vlan API
  phrasing_intents:
  - id: GetVlans
    intent: List the cluster's VLANs
    question: Which VLANs are configured on my cluster?
  - id: CreateVlan
    intent: Create a VLAN
    question: How do I add a new VLAN with its own subnet and gateway?
  - id: GetVlanById
    intent: Get a single VLAN
    question: How do I see the details of one VLAN, by id or interface group name?
  - id: UpdateVlan
    intent: Update an existing VLAN
    question: Can I change the gateway or IP range of a VLAN that already exists?
  - id: RemoveVlan
    intent: Remove a VLAN
    question: How do I delete a VLAN from the cluster?
  phrasing_ops: 5
  slug: cohesity-vlan-api
- baseURL: https://helios.cohesity.com/irisservices/api/v1/public/
  baseurl_source: declared
  description: The Access Tokens API from Cohesity — 1 operation(s) for access tokens.
  name: Cohesity Access Tokens API
  phrasing_intents:
  - id: GenerateAccessToken
    intent: Get an API access token
    question: How do I authenticate to the Cohesity REST API?
  phrasing_ops: 1
  slug: cohesity-access-tokens-api
- baseURL: https://helios.cohesity.com/irisservices/api/v1/public/
  baseurl_source: declared
  description: The Active Directory API from Cohesity — 13 operation(s) for active directory.
  name: Cohesity Active Directory API
  phrasing_intents:
  - id: GetActiveDirectoryEntry
    intent: List AD domains the cluster has joined (legacy)
    question: Which Active Directory domains is my Cohesity cluster joined to, using the older public endpoint?
  - id: CreateActiveDirectoryEntry
    intent: Join the cluster to an AD domain (legacy)
    question: Can I join the cluster to an Active Directory domain through the older public API so domain users can log in?
  - id: DeleteActiveDirectoryEntry
    intent: Leave an AD domain (legacy)
    question: What happens to domain users' access if the cluster leaves an Active Directory domain?
  - id: ListCentrifyZones
    intent: List Centrify zones of an AD domain
    question: Which Centrify zones exist in my Active Directory domain?
  - id: GetActiveDirectoryDomainControllers
    intent: List a joined domain's controllers (legacy)
    question: Which domain controllers does the cluster see for a joined domain via the public endpoint?
  - id: SearchActiveDirectoryPrincipals
    intent: Search AD users and groups
    question: Can I search Active Directory for a user or group by part of their name?
  - id: AddActiveDirectoryPrincipals
    intent: Add AD users or groups with Cohesity roles
    question: How do I give an Active Directory group access to the cluster with a specific Cohesity role?
  - id: EnableTrustedDomainDiscovery
    intent: Turn trusted domain discovery on or off
    question: Can I stop the cluster from discovering trusted domains of a joined AD domain?
  phrasing_ops: 19
  slug: cohesity-active-directory-api
- baseURL: https://helios.cohesity.com/irisservices/api/v1/public/
  baseurl_source: declared
  description: The Audit Log API from Cohesity — 4 operation(s) for audit log.
  name: Cohesity Audit Log API
  phrasing_intents:
  - id: GetAuditLogs
    intent: Search cluster audit logs (v2)
    question: Who changed what on the cluster yesterday, according to the audit-logs API?
  - id: GetAuditLogsActions
    intent: List audit log actions (v2)
    question: Which action values can I filter the audit-logs endpoint by?
  - id: GetAuditLogsEntityTypes
    intent: List audit log entity types
    question: Which entity types appear in cluster audit logs?
  - id: GetFilerAuditLogConfigs
    intent: Get filer audit log configs
    question: Where are filer audit logs written, and over which SMB or NFS mount paths?
  - id: UpdateFilerAuditLogConfigs
    intent: Update filer audit log configs
    question: Can I change the NFS or SMB mount paths for filer audit logs?
  phrasing_ops: 5
  slug: cohesity-audit-log-api
- baseURL: https://helios.cohesity.com/irisservices/api/v1/public/
  baseurl_source: declared
  description: The External Connection API from Cohesity — 4 operation(s) for external connection.
  name: Cohesity External Connection API
  phrasing_intents:
  - id: GetBifrostConnection
    intent: List Bifrost connections
    question: Which Bifrost connections are configured on the cluster?
  - id: CreateBifrostConnection
    intent: Create a Bifrost connection
    question: How do I set up a Bifrost connection for a tenant?
  - id: GetBifrostConnectionById
    intent: Get a Bifrost connection
    question: What are the settings of one Bifrost connection?
  - id: UpdateBifrostConnection
    intent: Update a Bifrost connection
    question: Can I change the subnet of an existing Bifrost connection?
  - id: DeleteBifrostConnection
    intent: Delete a Bifrost connection
    question: How do I remove a Bifrost connection I no longer use?
  - id: GetRigelConnection
    intent: List Rigel connections
    question: Which Rigel connections exist on the cluster?
  - id: CreateRigelConnection
    intent: Create a Rigel connection
    question: How do I register a Rigel connection for a tenant?
  - id: GetRigelConnectionById
    intent: Get a Rigel connection
    question: What does a single Rigel connection look like?
  phrasing_ops: 10
  slug: cohesity-external-connection-api
- baseURL: https://helios.cohesity.com/irisservices/api/v1/public/
  baseurl_source: declared
  description: The Health Checks API from Cohesity — 1 operation(s) for health checks.
  name: Cohesity Health Checks API
  phrasing_intents:
  - id: SCInitiateHealthCheck
    intent: Run an on-demand DR plan health check
    question: Can I run a health check on my DR plans on demand?
  phrasing_ops: 1
  slug: cohesity-health-checks-api
- baseURL: https://helios.cohesity.com/irisservices/api/v1/public/
  baseurl_source: declared
  description: The Interface group API from Cohesity — 2 operation(s) for interface group.
  name: Cohesity Interface group API
  phrasing_intents:
  - id: GetInterfaceGroups
    intent: List network interface groups
    question: Which network interface groups exist on the cluster?
  - id: UpdateInterfaceGroup
    intent: Update a network interface group
    question: Can I change which interfaces belong to an existing interface group?
  - id: CreateInterfaceGroup
    intent: Create a network interface group
    question: How do I create a new interface group for a product model's NICs?
  - id: DeleteInterfaceGroup
    intent: Delete a network interface group
    question: How do I remove an interface group I set up by mistake?
  phrasing_ops: 4
  slug: cohesity-interface-group-api
- baseURL: https://helios.cohesity.com/irisservices/api/v1/public/
  baseurl_source: declared
  description: The KMS Configuration API from Cohesity — 1 operation(s) for kms configuration.
  name: Cohesity KMS Configuration API
  phrasing_intents:
  - id: CreateKmsConfig
    intent: Configure a key management server
    question: How do I connect my cluster to an external KMS for encryption keys?
  phrasing_ops: 1
  slug: cohesity-kms-configuration-api
- baseURL: https://helios.cohesity.com/irisservices/api/v1/public/
  baseurl_source: declared
  description: The Node Groups API from Cohesity — 2 operation(s) for node groups.
  name: Cohesity Node Groups API
  phrasing_intents:
  - id: GetNodeGroups
    intent: List node groups
    question: What node groups are configured on the cluster?
  - id: CreateNodeGroup
    intent: Create a node group
    question: How do I group a set of nodes together with their own subnet and DNS settings?
  - id: GetNodeGroupByName
    intent: Get a node group by name
    question: How do I look up one node group and the nodes in it?
  - id: UpdateNodeGroup
    intent: Update a node group
    question: Can I add or remove nodes from an existing node group?
  - id: DeleteNodeGroup
    intent: Delete a node group
    question: How do I remove a node group I no longer use?
  phrasing_ops: 5
  slug: cohesity-node-groups-api
- baseURL: https://helios.cohesity.com/irisservices/api/v1/public/
  baseurl_source: declared
  description: The Protection Groups API from Cohesity — 11 operation(s) for protection groups.
  name: Cohesity Protection Groups API
  phrasing_intents:
  - id: GetProtectionGroups
    intent: List protection groups
    question: Which protection groups had their last backup fail?
  - id: CreateProtectionGroup
    intent: Create a protection group
    question: How do I set up a new backup group for my VMware VMs with a given policy?
  - id: UpdateProtectionGroupsState
    intent: Pause, resume or deactivate protection groups in bulk
    question: Can I pause several backup groups at once during a maintenance window?
  - id: GetProtectionGroupById
    intent: Get a protection group
    question: How do I look at a single protection group's configuration and last run?
  - id: UpdateProtectionGroup
    intent: Update a protection group's settings
    question: Can I switch an existing protection group to a different policy?
  - id: DeleteProtectionGroup
    intent: Delete a protection group
    question: If I delete a backup group, are its snapshots kept?
  - id: GetProtectionGroupRuns
    intent: List runs of a protection group
    question: What were the last backup runs for one protection group and did they succeed?
  - id: UpdateProtectionGroupRun
    intent: Change retention or resync runs of a group
    question: Can I extend how long snapshots from a past backup run are kept?
  phrasing_ops: 16
  slug: cohesity-protection-groups-api
- baseURL: https://helios.cohesity.com/irisservices/api/v1/public/
  baseurl_source: declared
  description: The Protection Policies API from Cohesity — 7 operation(s) for protection policies.
  name: Cohesity Protection Policies API
  phrasing_intents:
  - id: GetProtectionPolicies
    intent: List protection policies (v1 public API)
    question: How do I list protection policies with the older v1 public API?
  - id: CreateProtectionPolicy
    intent: Create a protection policy (v1 public API)
    question: How do I create a backup policy with the v1 public API, setting days to keep?
  - id: GetProtectionPolicyById
    intent: Get one protection policy (v1 public API)
    question: How do I fetch a single policy's details from the v1 public API?
  - id: UpdateProtectionPolicy
    intent: Update a protection policy (v1 public API)
    question: How do I change retention days on a policy using the v1 public API?
  - id: DeleteProtectionPolicy
    intent: Delete a protection policy (v1 public API)
    question: How do I delete a policy through the v1 public API?
  - id: GetProtectionPolicySummary
    intent: Summarize runs for a protection policy
    question: How are the jobs that use a given policy performing?
  - id: getDataProtectPolicies
    intent: List protection policies (v2 data-protect)
    question: Which data-protect policies exist on my cluster?
  - id: postDataProtectPolicies
    intent: Create a protection policy (v2 data-protect)
    question: How do I create a data-protect backup policy with a blackout window?
  phrasing_ops: 13
  slug: cohesity-protection-policies-api
artifact_total: 107
asyncapis:
- description: ''
  name: Cohesity Webhooks
  slug: cohesity-webhooks
common:
- group: commercial
  href: https://artifacts.apis.io/cohesity/finops/cohesity-finops.yml
  title: ''
  type: FinOps
  url: finops/cohesity-finops.yml
- group: other
  href: https://artifacts.apis.io/cohesity/capabilities/cohesity-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/cohesity-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/cohesity/overlays/cohesity-cluster-v1-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/cohesity-cluster-v1-overlay.yaml
- group: other
  href: https://artifacts.apis.io/cohesity/overlays/cohesity-helios-reporting-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/cohesity-helios-reporting-overlay.yaml
- group: other
  href: https://artifacts.apis.io/cohesity/overlays/cohesity-site-continuity-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/cohesity-site-continuity-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/cohesity/agentic-access/cohesity-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/cohesity-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/cohesity/authentication/cohesity-authentication.yml
  title: ''
  type: Authentication
  url: authentication/cohesity-authentication.yml
- group: auth
  href: https://artifacts.apis.io/cohesity/security/cohesity-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cohesity-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cohesity
- group: company
  title: ''
  type: Website
  url: https://www.cohesity.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.cohesity.com/
- group: start
  title: ''
  type: Portal
  url: https://developers.cohesity.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.cohesity.com/apidocs/versions/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/cohesity
- group: docs
  title: ''
  type: Documentation
  url: https://docs.cohesity.com/
- group: operate
  title: ''
  type: Support
  url: https://www.cohesity.com/support/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cohesity.com/
- group: agent
  title: ''
  type: LlmsText
  url: https://developers.cohesity.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://www.cohesity.com/feed/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cohesity.com/agreements/privacy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cohesity.com/agreements/
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.cohesity.com/docs/getting-started
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cohesity
- group: commercial
  title: ''
  type: Pricing
  url: https://www.cohesity.com/buy/cohesity-data-cloud-packaging/
- group: start
  title: ''
  type: SignUp
  url: https://www.cohesity.com/free-trial/
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/cohesity/
- group: docs
  href: https://artifacts.apis.io/cohesity/openapi/_original/cohesity-cluster-v1-openapi.yml
  title: ''
  type: OpenAPI
  url: openapi/_original/cohesity-cluster-v1-openapi.yml
- group: docs
  href: https://artifacts.apis.io/cohesity/openapi/_original/cohesity-cluster-v2-openapi.yml
  title: ''
  type: OpenAPI
  url: openapi/_original/cohesity-cluster-v2-openapi.yml
- group: docs
  href: https://artifacts.apis.io/cohesity/openapi/_original/cohesity-helios-reporting-openapi.yml
  title: ''
  type: OpenAPI
  url: openapi/_original/cohesity-helios-reporting-openapi.yml
- group: docs
  href: https://artifacts.apis.io/cohesity/openapi/_original/cohesity-site-continuity-openapi.yml
  title: ''
  type: OpenAPI
  url: openapi/_original/cohesity-site-continuity-openapi.yml
- group: build
  href: https://artifacts.apis.io/cohesity/packages/cohesity-packages.yml
  title: ''
  type: Packages
  url: packages/cohesity-packages.yml
- group: build
  href: https://artifacts.apis.io/cohesity/packages/cohesity-packages.yml
  title: ''
  type: SDKs
  url: packages/cohesity-packages.yml
- group: agent
  href: https://artifacts.apis.io/cohesity/mcp/cohesity-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/cohesity-mcp.yml
- group: build
  href: https://artifacts.apis.io/cohesity/mcp/cohesity-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/cohesity-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/cohesity/llms/cohesity-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cohesity-llms.txt
- group: other
  href: https://artifacts.apis.io/cohesity/overlays/cohesity-cluster-v2-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/cohesity-cluster-v2-overlay.yaml
- group: design
  href: https://artifacts.apis.io/cohesity/conformance/cohesity-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cohesity-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.cohesity.com/trust/
- group: design
  href: https://artifacts.apis.io/cohesity/errors/cohesity-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/cohesity-problem-types.yml
- group: design
  href: https://artifacts.apis.io/cohesity/lifecycle/cohesity-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/cohesity-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://developer.cohesity.com/docs/whats-new-65
- group: operate
  href: https://artifacts.apis.io/cohesity/changelog/cohesity-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/cohesity-changelog.yml
- group: auth
  href: https://artifacts.apis.io/cohesity/scopes/cohesity-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/cohesity-scopes.yml
- group: agent
  href: https://artifacts.apis.io/cohesity/well-known/cohesity-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cohesity-well-known.yml
- group: auth
  href: https://artifacts.apis.io/cohesity/security/cohesity-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/cohesity-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.cohesity.com/trust/security-profile/
- group: auth
  href: https://artifacts.apis.io/cohesity/security/cohesity-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/cohesity-trust-center.yml
- group: design
  href: https://artifacts.apis.io/cohesity/conventions/cohesity-conventions.yml
  title: ''
  type: Conventions
  url: conventions/cohesity-conventions.yml
- group: design
  href: https://artifacts.apis.io/cohesity/data-model/cohesity-data-model.yml
  title: ''
  type: DataModel
  url: data-model/cohesity-data-model.yml
- group: design
  href: https://artifacts.apis.io/cohesity/asyncapi/cohesity-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/cohesity-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/cohesity/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  href: https://artifacts.apis.io/cohesity/plans/cohesity-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/cohesity-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/cohesity/rate-limits/cohesity-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/cohesity-rate-limits.yml
created: '2025-03-01'
description: Cohesity is a data security and management company providing backup, disaster recovery, archive, and cyber resilience capabilities across on-premises, cloud, and SaaS workloads. Following the merger with Veritas, the combined company protects enterprise data while powering automation, orchestration, and AI- driven recovery. The Cohesity developer surface centers on the Cohesity REST API, exposed both per-cluster (DataProtect/cluster API) and via the Helios global control plane, with versioned v1 and v2 endpoints, API-key authentication, and SDKs for Python, PowerShell, Ansible, Terraform, and ServiceNow.
finops:
- has_sources: true
  method: derived
  name: Cohesity Finops
  primary_unit: ''
  service_category: ''
  slug: cohesity-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cohesity.png
layout: provider
mcp_servers:
- description: Remote MCP server over HTTP requiring an API key; 4 tools listed.
  name: Cohesity Gaia MCP
  slug: cohesity-gaia-mcp
modified: '2026-09-16'
name: Cohesity
nav: Providers
network: true
overview: 'Cohesity publishes 91 API contracts indexed on the [APIs.io](https://apis.io/) network, including Alerts API, Analytics API, Antivirus Service Group API, and 88 more. Tagged areas include Automation, Backup, Cyber Resilience, Data Management, and Data Protection.


  The Cohesity catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Cohesity''s developer surface includes authentication, developer portal, API reference, GitHub presence, documentation, support, engineering blog, and 46 more developer resources.'
plans:
- name: Cohesity Plans Pricing
  plan_count: 2
  slug: cohesity-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 1
  name: Cohesity Rate Limits
  slug: cohesity-rate-limits
rules:
- authorship: generated
  effective_rule_count: 95
  extends:
  - spectral:oas
  name: Cohesity API Rules
  rule_count: 54
  severity_counts:
    error: 31
    hint: 0
    info: 4
    warn: 19
  slug: cohesity-rules
scopes:
- name: Cohesity Scopes
  scope_count: 6
  slug: cohesity-scopes
  summary_line: 6 scopes · authorizationCode
score:
  band: exemplar
  composite: 70.1
  coverage:
    artifact_dirs: 30
    catalog_earned: 60.5
    catalog_earned_first_party: 16.0
    catalog_gap: 54.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 81.6
    contract_governance: 31.8
    contract_quality: 50.4
    developer_ergonomics: 70.8
    discoverability: 76.7
    operational_transparency: 81.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 70.1
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 13.2
      derived: 0
      marker_coverage: 0.0
      total: 91
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 45.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 11.1
screenshot: https://apis.io/screenshots/cohesity/cohesity-2026-06-20T174720.png
security:
- kind: authentication
  name: Cohesity Authentication
  slug: cohesity-authentication
  summary_line: apiKey/oauth2/openIdConnect/http · 4 schemes
- kind: domain-security
  name: Cohesity Domain Security
  slug: cohesity-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Cohesity Vulnerability Disclosure
  slug: cohesity-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Cohesity Trust Center
  slug: cohesity-trust-center
  summary_line: SOC 2 Type II, ISO/IEC 27001:2022, FedRAMP Moderate, GovRAMP, HIPAA, Common Criteria EAL2+ (ALC_FLR.1), NIST FIPS 140-2 Level 1, USGv6, Trade Agreements Act (TAA)
skill_count: 4
skills:
- name: Subscribe to Cohesity alerts via webhook
  slug: cohesity-alert-webhooks
- name: Pull Cohesity Helios reports
  slug: cohesity-helios-reporting
- name: Protect a workload with Cohesity
  slug: cohesity-protect-a-workload
- name: Recover data with Cohesity and reverse it if wrong
  slug: cohesity-recover-and-reverse
slug: cohesity
tags:
- Automation
- Backup
- Cyber Resilience
- Data Management
- Data Protection
- Data Security
- DataProtect
- Disaster Recovery
- Helios
- Orchestration
- Ransomware Recovery
- Site Continuity
- Reporting
- MCP
- Enterprise Storage
website: https://www.cohesity.com/
---
