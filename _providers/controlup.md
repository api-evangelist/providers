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
    agentic_access: false
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
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 35.7
  scored_at: '2026-10-04'
api_count: 24
apis:
- description: Official Model Context Protocol server published by ControlUp as the npm package @controlup-ai/mcp. Runs locally over stdio via npx, authenticates with a ControlUp API key plus organization ID, and ex
  name: ControlUp MCP Server
  slug: controlup-mcp-server
- baseURL: https://api.controlup.com/v1
  baseurl_source: declared
  description: Alerts let you receive notifications or automatically run an action when certain conditions occur on a device.
  name: ControlUp Alerts API
  phrasing_intents:
  - id: get-alerts
    intent: List configured device alerts
    question: Which device alerts are configured in ControlUp for Desktops?
  - id: create-alert
    intent: Create a device alert
    question: How do I create an alert that fires when devices meet certain conditions?
  - id: get-alert
    intent: Get a device alert
    question: What conditions and actions does a specific device alert have?
  - id: edit-alert
    intent: Edit a device alert
    question: How do I change the severity or conditions of an existing device alert?
  - id: delete-alert
    intent: Delete a device alert
    question: How do I remove a device alert I no longer need?
  - id: AlertsConfigsController_getAll
    intent: List an organization's alert configurations
    question: What alert configurations are set up for my organization?
  - id: honeycomb.api.get_scout_alerts
    intent: List Scouts that triggered alerts
    question: Which Scouts have triggered an alert in the last 24 hours?
  - id: app.get_alert_for_scout
    intent: List alerts generated for a Scout
    question: What alerts has a particular Scout generated recently?
  phrasing_ops: 13
  slug: controlup-alerts-api
- baseURL: https://api.controlup.com/v1
  baseurl_source: declared
  description: The Alerts - Devices API from ControlUp — 2 operation(s) for alerts - devices.
  name: ControlUp Alerts - Devices API
  phrasing_intents:
  - id: AlertsDesktopController_getAlertById
    intent: Retrieve a Devices alert configuration
    question: How is a specific Devices alert configured?
  - id: AlertsDesktopController_updateAlertConfiguration
    intent: Update a Devices alert
    question: Can I change the severity of an existing device alert?
  - id: AlertsDesktopController_deleteAlertConfiguration
    intent: Delete a Devices alert
    question: Can I remove a Devices alert I no longer need?
  - id: AlertsDesktopController_createDesktopAlert
    intent: Create a Devices alert
    question: Can I set up a new alert when a device metric crosses a threshold several times?
  phrasing_ops: 4
  slug: controlup-alerts-devices-api
- baseURL: https://api.controlup.com/v1
  baseurl_source: declared
  description: Applications usage reports
  name: ControlUp Applications API
  phrasing_intents:
  - id: getAppUsageSingle
    intent: Get usage details for one application
    question: Which machines and users ran a specific application, and what was its peak concurrency?
  - id: getAppUsage
    intent: Get usage for all applications
    question: How many unique users and peak concurrent users did each application have?
  - id: getAppStats
    intent: Get weekly or monthly application resource statistics
    question: How much CPU and memory does each application version consume per week?
  phrasing_ops: 3
  slug: controlup-applications-api
- baseURL: https://api.controlup.com/v1
  baseurl_source: declared
  description: The Audit Log API from ControlUp — 1 operation(s) for audit log.
  name: ControlUp Audit Log API
  phrasing_intents:
  - id: OrgAuditLogPublicController_getAll
    intent: Get the organization audit log
    question: Who changed what in my ControlUp organization in the last 24 hours?
  phrasing_ops: 1
  slug: controlup-audit-log-api
- baseURL: https://api.controlup.com/v1
  baseurl_source: declared
  description: The Cloud providers API from ControlUp — 3 operation(s) for cloud providers.
  name: ControlUp Cloud providers API
  phrasing_intents:
  - id: GetProviders
    intent: List supported cloud providers
    question: Which cloud providers can ControlUp integrate with?
  - id: GetAllAuthTypes
    intent: List authentication types across all providers
    question: What authentication types are supported across every cloud provider?
  - id: GetProviderAuthTypes
    intent: List authentication types for one provider
    question: Which authentication types can I use for a particular cloud provider?
  phrasing_ops: 3
  slug: controlup-cloud-providers-api
- baseURL: https://api.controlup.com/v1
  baseurl_source: declared
  description: The DAL (data access layer) is an advanced way to get data from an index.
  name: ControlUp Dal API
  phrasing_intents:
  - id: get-scoped-data-index
    intent: Query a data index scoped to selected devices
    question: Can I read a data index but only for devices matching a device query?
  phrasing_ops: 1
  slug: controlup-dal-api
- baseURL: https://api.controlup.com/v1
  baseurl_source: declared
  description: These endpoints are for interacting with the raw data stored in data indices.
  name: ControlUp Data API
  phrasing_intents:
  - id: get-data-indices
    intent: List data indices
    question: Which data indices are available, and how big is each?
  - id: postData
    intent: Create a data index
    question: Can I create my own data index and load it with JSON data?
  - id: get-data-index
    intent: Read the rows of a data index
    question: Can I pull the contents of a data index, and what's the row cap?
  - id: get-data-index-mappings
    intent: Get field types of a data index
    question: Which fields and data types does a data index contain?
  - id: retrieve-document
    intent: Retrieve a document from a data index
    question: Can I fetch one document from a data index by ID?
  - id: list-custom-reports
    intent: List custom reports
    question: Which custom reports have been set up?
  - id: get-custom-report
    intent: Get a custom report's configuration
    question: How is a particular custom report configured?
  phrasing_ops: 7
  slug: controlup-data-api
- baseURL: https://api.controlup.com/v1
  baseurl_source: declared
  description: Get information about devices.
  name: ControlUp Devices API
  phrasing_intents:
  - id: getDevices
    intent: List compliance-managed devices
    question: Which of my devices have the worst compliance score?
  - id: getDeviceDetails
    intent: Get a device and its issue summary
    question: How many issues were detected on one specific device?
  - id: getDeviceVulnerabilities
    intent: List CVEs on a device
    question: Which CVEs were detected on a particular laptop?
  - id: getDevicePatches
    intent: List missing patches on a device
    question: What OS and application patches is this device missing?
  - id: getDeviceCompliance
    intent: List compliance issues on a device
    question: Which compliance-category issues does a device have?
  - id: getDeviceMisconfig
    intent: List misconfigurations on a device
    question: What misconfigurations were detected on a given device?
  - id: delete-devices
    intent: Delete devices
    question: Can I remove several retired devices from compliance monitoring at once?
  - id: list-device-tags
    intent: List device tags with usage counts
    question: Which device tags exist, and how many devices use each?
  phrasing_ops: 13
  slug: controlup-devices-api
- baseURL: https://api.controlup.com/v1
  baseurl_source: declared
  description: Dynamic SQL transformation and execution
  name: ControlUp Dynamic Query API
  phrasing_intents:
  - id: execute
    intent: Run a SQL query over ControlUp data
    question: Can I run my own SQL query against historical ControlUp data?
  - id: getSchema
    intent: Download the query database schema as CSV
    question: What tables and columns can I use in a dynamic SQL query?
  phrasing_ops: 2
  slug: controlup-dynamic-query-api-api
- baseURL: https://api.controlup.com/v1
  baseurl_source: declared
  description: The System Events log reports important events and alerts in your ControlUp for Desktops environment.
  name: ControlUp Events API
  phrasing_intents:
  - id: get-system-events
    intent: List System Events log entries
    question: What alerts, actions and configuration changes appear in the System Events log?
  - id: get-system-events-query
    intent: Query System Events with an OpenSearch body
    question: Can I send an OpenSearch query in the request body to search system events?
  - id: EventsController_getEventsList
    intent: List organization events in a time range
    question: Which events happened in my organization during a specific time window?
  - id: EventsController_getTotalEvents
    intent: Count unique values of an event field
    question: How many distinct users or devices generated events in a time range?
  - id: EventsController_getEventByUUID
    intent: Retrieve a single event
    question: What are the full details of one specific event?
  phrasing_ops: 5
  slug: controlup-events-api
- baseURL: https://api.controlup.com/v1
  baseurl_source: declared
  description: The Features API from ControlUp — 2 operation(s) for features.
  name: ControlUp Features API
  phrasing_intents:
  - id: getFeatures
    intent: List all feature flags for my organization
    question: Which feature flags are switched on for my organization right now?
  - id: getFeaturesByFeature
    intent: Check whether one feature flag is enabled
    question: Is a specific feature flag turned on for my organization?
  phrasing_ops: 2
  slug: controlup-features-api
- baseURL: https://api.controlup.com/v1
  baseurl_source: declared
  description: The Health API from ControlUp — 3 operation(s) for health.
  name: ControlUp Health API
  phrasing_intents:
  - id: getHealth
    intent: Check API and dependency health
    question: Is the ControlUp API healthy, including its dependencies?
  - id: getHealthLive
    intent: Check that the API process is alive
    question: Is there a lightweight liveness probe that skips dependency checks?
  - id: getHealthInfo
    intent: Get the deployed build version
    question: Which build version of the API is currently deployed?
  phrasing_ops: 3
  slug: controlup-health-api
- baseURL: https://api.controlup.com/v1
  baseurl_source: declared
  description: Hives are the locations from which Scouts (tests) are initiated. Custom Hives allow you to test internal resources from within your network. They must be installed on a computer with access to your ne
  name: ControlUp Hives API
  phrasing_intents:
  - id: honeycomb.api.custom_hives
    intent: List Custom Hives
    question: Which Custom Hives has my organization set up?
  - id: honeycomb.api.cloud_hives
    intent: List Cloud Hives
    question: Which Cloud Hives can my Scouts test from?
  phrasing_ops: 2
  slug: controlup-hives-api
- baseURL: https://api.controlup.com/v1
  baseurl_source: declared
  description: Host usage reports
  name: ControlUp Host API
  phrasing_intents:
  - id: getHostMetrics
    intent: Get average host resource use per folder
    question: What was the average host CPU or memory consumption per folder last week?
  - id: getHostCounts
    intent: Get usage statistics per host
    question: What usage counts does each host report over a period?
  phrasing_ops: 2
  slug: controlup-host-api
- baseURL: https://api.controlup.com/v1
  baseurl_source: declared
  description: The Host pool cost API from ControlUp — 4 operation(s) for host pool cost.
  name: ControlUp Host pool cost API
  phrasing_intents:
  - id: GetHostPoolCost
    intent: Get a host pool's cost breakdown
    question: What did my host pool spend on compute, disk and network last month?
  - id: GetHostPoolSavings
    intent: Get autoscale savings for a host pool
    question: How much has autoscale saved compared with running the pool always-on?
  - id: GetHostPoolHostsCost
    intent: Get cost per session host
    question: Which session hosts in my pool cost the most?
  - id: GetHostPoolCostExport
    intent: Export host pool cost as CSV
    question: Can I download per-host daily cost records as a CSV?
  phrasing_ops: 4
  slug: controlup-host-pool-cost-api
- baseURL: https://api.controlup.com/v1
  baseurl_source: declared
  description: The Host pool deployments API from ControlUp — 1 operation(s) for host pool deployments.
  name: ControlUp Host pool deployments API
  phrasing_intents:
  - id: CreateHostPoolDeployment
    intent: Deploy a new AVD host pool
    question: Can I deploy a new Azure Virtual Desktop host pool with its app group and workspace in one job?
  phrasing_ops: 1
  slug: controlup-host-pool-deployments-api
- baseURL: https://api.controlup.com/v1
  baseurl_source: declared
  description: The Host pool scaling policies API from ControlUp — 2 operation(s) for host pool scaling policies.
  name: ControlUp Host pool scaling policies API
  phrasing_intents:
  - id: GetHostPoolScalingPolicy
    intent: Get a host pool's weekly autoscale schedule
    question: Which scaling profile is assigned to each time block in a host pool's week?
  - id: SaveHostPoolScalingPolicy
    intent: Save a host pool's autoscale schedule
    question: How do I set up an autoscale schedule with time blocks for a host pool?
  - id: DeleteHostPoolScalingPolicy
    intent: Remove a host pool's autoscale schedule
    question: How do I turn off autoscaling on a host pool by removing its policy?
  - id: GetHostPoolActiveScalingProfile
    intent: Get the scaling profile in effect right now
    question: Which scaling profile is active on a host pool at this moment?
  phrasing_ops: 4
  slug: controlup-host-pool-scaling-policies-api
- baseURL: https://api.controlup.com/v1
  baseurl_source: declared
  description: The Host pool session host deployments API from ControlUp — 1 operation(s) for host pool session host deployments.
  name: ControlUp Host pool session host deployments API
  phrasing_intents:
  - id: CreateSessionHostDeployment
    intent: Add session hosts to a host pool
    question: How do I add more session hosts to an existing host pool?
  phrasing_ops: 1
  slug: controlup-host-pool-session-host-deployments-api
- baseURL: https://api.controlup.com/v1
  baseurl_source: declared
  description: The Host pool session hosts API from ControlUp — 1 operation(s) for host pool session hosts.
  name: ControlUp Host pool session hosts API
  phrasing_intents:
  - id: GetSessionHosts
    intent: List session hosts in a host pool
    question: Which VMs make up my host pool, and are any in drain mode?
  phrasing_ops: 1
  slug: controlup-host-pool-session-hosts-api
- baseURL: https://api.controlup.com/v1
  baseurl_source: declared
  description: The Host pool user sessions API from ControlUp — 1 operation(s) for host pool user sessions.
  name: ControlUp Host pool user sessions API
  phrasing_intents:
  - id: GetHostPoolSessions
    intent: List users logged in to a host pool
    question: Who is currently logged in anywhere in a host pool?
  phrasing_ops: 1
  slug: controlup-host-pool-user-sessions-api
- baseURL: https://api.controlup.com/v1
  baseurl_source: declared
  description: The Host pool VM settings API from ControlUp — 2 operation(s) for host pool vm settings.
  name: ControlUp Host pool VM settings API
  phrasing_intents:
  - id: GetHostPoolVmSettings
    intent: Get a host pool's VM template
    question: What VM size and image will new session hosts in my pool use?
  - id: SaveHostPoolVmSettings
    intent: Save a host pool's VM template
    question: Can I set the VM size, image and network that future session hosts are built from?
  - id: DeleteHostPoolVmSettings
    intent: Delete a host pool's VM template
    question: Can I discard the stored VM template for a host pool?
  - id: ValidateHostPoolVmSettings
    intent: Validate VM settings without saving
    question: Can I check a VM settings payload for errors before committing it?
  phrasing_ops: 4
  slug: controlup-host-pool-vm-settings-api
- baseURL: https://api.controlup.com/v1
  baseurl_source: declared
  description: The Host pools API from ControlUp — 6 operation(s) for host pools.
  name: ControlUp Host pools API
  phrasing_intents:
  - id: GetHostPools
    intent: List host pools across subscriptions
    question: Which host pools do I have across all subscriptions?
  - id: GetHostPoolsStatistics
    intent: Get organization-wide host pool totals
    question: How many pooled versus personal host pools do I have?
  - id: GetHostPool
    intent: Get a host pool summary
    question: What are the host, session and CPU counts for one host pool?
  - id: DeleteHostPool
    intent: Stop managing a host pool, keeping it in Azure
    question: How do I remove a host pool from DaaS IQ without touching the Azure resource?
  - id: GetHostPoolDetails
    intent: Get a host pool's full configuration
    question: What load balancing, max sessions per host and drain mode is a host pool using?
  - id: GetHostPoolMetrics
    intent: Chart a host pool's metrics over time
    question: How have active sessions and CPU in a host pool changed over the past week?
  - id: HardDeleteHostPool
    intent: Tear down a host pool in Azure
    question: How do I delete a host pool and its session host VMs from Azure entirely?
  phrasing_ops: 7
  slug: controlup-host-pools-api
- baseURL: https://api.controlup.com/v1
  baseurl_source: declared
  description: The Integrations API from ControlUp — 1 operation(s) for integrations.
  name: ControlUp Integrations API
  phrasing_intents:
  - id: honeycomb.api.get_org_integrations
    intent: List alert notification integrations
    question: Which external integrations can receive my alert notifications?
  phrasing_ops: 1
  slug: controlup-integrations-api
- baseURL: https://api.controlup.com/v1
  baseurl_source: declared
  description: The Invitations API from ControlUp — 1 operation(s) for invitations.
  name: ControlUp Invitations API
  phrasing_intents:
  - id: OrgInvitationPublicController_create
    intent: Invite users to the organization
    question: Can I invite several people to ControlUp with specific roles in one request?
  - id: OrgInvitationPublicController_update
    intent: Resend an invitation email
    question: Someone lost their invite email — can I resend it?
  phrasing_ops: 2
  slug: controlup-invitations-api
- baseURL: https://api.controlup.com/v1
  baseurl_source: declared
  description: The IP Allowlist API from ControlUp — 2 operation(s) for ip allowlist.
  name: ControlUp IP Allowlist API
  phrasing_intents:
  - id: OrgIpAllowlistPublicController_getAll
    intent: List IP allowlist entries
    question: Which IP addresses and ranges are allowed to access my organization?
  - id: OrgIpAllowlistPublicController_create
    intent: Add an IP allowlist entry
    question: How do I allow a new office IP range to access ControlUp?
  - id: OrgIpAllowlistPublicController_update
    intent: Replace the IPs in an allowlist entry
    question: How do I change the IP ranges in an existing allowlist entry?
  - id: OrgIpAllowlistPublicController_delete
    intent: Delete an IP allowlist entry
    question: How do I remove an IP range from the allowlist?
  phrasing_ops: 4
  slug: controlup-ip-allowlist-api
- baseURL: https://api.controlup.com/v1
  baseurl_source: declared
  description: The Jobs API from ControlUp — 8 operation(s) for jobs.
  name: ControlUp Jobs API
  phrasing_intents:
  - id: GetJob
    intent: Get a background job's full record
    question: Why did a background job fail — what are its error details?
  - id: GetJobParameters
    intent: Get a job's input parameters
    question: What inputs was a background job created with?
  - id: GetJobs
    intent: List background jobs
    question: Which background jobs are running in my organization?
  - id: GetJobStatus
    intent: Poll a job's status
    question: What's the cheapest way to poll whether a job is finished?
  - id: CancelJob
    intent: Cancel a background job
    question: Can I stop a running background job?
  - id: RetryJob
    intent: Retry a failed job
    question: Can I rerun a failed job with the same parameters?
  - id: GetJobLogs
    intent: Get a job's structured logs
    question: Can I tail a job's log entries incrementally with a cursor?
  - id: GetJobLogsTranscript
    intent: Download a job's logs as text
    question: Can I download a job's logs as plain text?
  phrasing_ops: 8
  slug: controlup-jobs-api
- baseURL: https://api.controlup.com/v1
  baseurl_source: declared
  description: The License API from ControlUp — 1 operation(s) for license.
  name: ControlUp License API
  phrasing_intents:
  - id: getLicense
    intent: Get my organization's license and usage
    question: When does my organization's license expire, and what type is it?
  phrasing_ops: 1
  slug: controlup-license-api
- baseURL: https://api.controlup.com/v1
  baseurl_source: declared
  description: The License Usage API from ControlUp — 1 operation(s) for license usage.
  name: ControlUp License Usage API
  phrasing_intents:
  - id: OrgLicensePublicController_getLicenseUsage
    intent: Get license usage over a time range
    question: How many ControlUp licenses did my organization use last month?
  phrasing_ops: 1
  slug: controlup-license-usage-api
- baseURL: https://api.controlup.com/v1
  baseurl_source: declared
  description: Machine usage reports
  name: ControlUp Machine API
  phrasing_intents:
  - id: getMachineStatsByMachine
    intent: Get historical machine resource statistics
    question: What was each machine's peak CPU and memory usage last week?
  - id: getRecommendationVirtualization
    intent: Get VM sizing recommendations for virtual environments
    question: Are my on-prem virtual machines over- or under-provisioned?
  - id: getRecommendationAzure
    intent: Get Azure VM sizing recommendations
    question: Which Azure VM size would cost least for my machines in a given region?
  - id: getMachinesAggregated
    intent: Aggregate machine metrics by a dimension
    question: What's the average CPU usage per operating system across my fleet?
  phrasing_ops: 4
  slug: controlup-machine-api
- baseURL: https://api.controlup.com/v1
  baseurl_source: declared
  description: Endpoints to manage and query machines
  name: ControlUp Machines API
  phrasing_intents:
  - id: getMachines
    intent: List monitored machines
    question: Which machines does ControlUp know about in a given folder or site?
  - id: upsertMachines
    intent: Bulk create or update machines
    question: How do I add many machines at once, matched by computer and domain name?
  - id: deleteMachines
    intent: Bulk delete machines by FQDN
    question: How do I remove several machines at once by their FQDNs?
  - id: getMachine
    intent: Get a machine's details
    question: What are the full details of one machine?
  phrasing_ops: 4
  slug: controlup-machines-api
- baseURL: https://api.controlup.com/v1
  baseurl_source: declared
  description: The Master images API from ControlUp — 20 operation(s) for master images.
  name: ControlUp Master images API
  phrasing_intents:
  - id: ExecuteMasterImageAction
    intent: Start or stop a master image VM
    question: Can I power on a master image's VM from the API?
  - id: GetMasterImageRdpFile
    intent: Download an RDP file for a master image
    question: Can I get a .rdp file to connect to a master image VM?
  - id: GetOsFamilies
    intent: List supported master image OS families
    question: Which operating system families does Azure Virtual Desktop support for master images?
  - id: GetMarketplaceImages
    intent: List curated Marketplace images
    question: Which Azure Marketplace OS images can I deploy as a new master image?
  - id: ListMasterImages
    intent: List master images
    question: Which master images does my organization manage, and what's their power state?
  - id: GetMasterImage
    intent: Get a master image
    question: What region, OS and gallery does a specific master image use?
  - id: GetOperationState
    intent: Check a master image's in-flight operation
    question: Is there an operation currently running on my master image?
  - id: GetDecommissionPlan
    intent: Preview retiring a master image
    question: What would be deleted or kept if I retire a master image?
  phrasing_ops: 20
  slug: controlup-master-images-api
- baseURL: https://api.controlup.com/v1
  baseurl_source: declared
  description: Endpoints to manage and query metrics
  name: ControlUp Metrics API
  phrasing_intents:
  - id: query
    intent: Query realtime metrics
    question: Can I query realtime metrics from a table with filters and sorting?
  - id: getTables
    intent: List metric tables
    question: What realtime metric tables are available to query?
  - id: getTableFields
    intent: List fields of a metric table
    question: What fields does a given metric table have?
  phrasing_ops: 3
  slug: controlup-metrics-api
- baseURL: https://api.controlup.com/v1
  baseurl_source: declared
  description: Multi-factor authentication (MFA) is supported for gateway access on all EUC platforms except Citrix Storefront. Use this resource to retrieve the sets of usernames and phone numbers that have been co
  name: ControlUp MF As API
  phrasing_intents:
  - id: honeycomb.api.get_org_mfas
    intent: List MFA users for EUC gateway
    question: Which usernames have a phone number registered for MFA?
  phrasing_ops: 1
  slug: controlup-mfas-api
- baseURL: https://api.controlup.com/v1
  baseurl_source: declared
  description: Netscaler usage reports
  name: ControlUp Net Scaler API
  phrasing_intents:
  - id: getNetscalerUsageWithTimeSeries
    intent: Get NetScaler appliance metrics as a time series (v2)
    question: How did my NetScaler appliances perform over time, point by point, in the v2 report?
  - id: getLoadbalancerUsageWithTimeSeries
    intent: Get load balancer metrics as a time series (v2)
    question: How did each NetScaler load balancer's traffic trend over the period, as a time series?
  - id: getGatewayUsageTimeSeries
    intent: Get NetScaler Gateway metrics as a time series (v2)
    question: How did NetScaler Gateway usage trend over time during the period?
  - id: getNetscalerUsage
    intent: Get NetScaler appliance metrics (v1 summary)
    question: What were the summary performance metrics for each NetScaler appliance in a period, without a time series?
  - id: getLoadbalancerUsage
    intent: Get load balancer metrics (v1 summary)
    question: What were the v1 summary metrics for each NetScaler load balancer in a period?
  - id: getGatewayUsage
    intent: Get NetScaler Gateway metrics (v1 summary)
    question: What were the v1 summary metrics for each NetScaler Gateway in a period?
  phrasing_ops: 6
  slug: controlup-netscaler-api
- baseURL: https://api.controlup.com/v1
  baseurl_source: declared
  description: The Onboarding API from ControlUp — 5 operation(s) for onboarding.
  name: ControlUp Onboarding API
  phrasing_intents:
  - id: ListOnboardingFlows
    intent: List my onboarding flows
    question: Which onboarding flows do I have, and how far along am I?
  - id: GetOnboardingFlow
    intent: Get one onboarding flow
    question: What step am I on in a particular onboarding flow?
  - id: UpdateOnboardingFlow
    intent: Change an onboarding flow's display or active step
    question: Can I minimize an onboarding flow or jump to another step?
  - id: StartOnboardingFlow
    intent: Start an onboarding flow
    question: Can I begin an onboarding flow and initialise its steps?
  - id: UpdateOnboardingStep
    intent: Mark an onboarding step done or not
    question: Can I mark a single onboarding step as complete?
  - id: DismissOnboardingFlow
    intent: Dismiss an onboarding flow
    question: Can I skip and hide an onboarding flow I don't want?
  phrasing_ops: 6
  slug: controlup-onboarding-api
- baseURL: https://api.controlup.com/v1
  baseurl_source: declared
  description: The Organization Settings API from ControlUp — 1 operation(s) for organization settings.
  name: ControlUp Organization Settings API
  phrasing_intents:
  - id: OrgSettingsPublicController_getOneById
    intent: Get organization settings
    question: What login methods, MFA and session timeouts is my organization configured with?
  - id: OrgSettingsPublicController_update
    intent: Update organization settings
    question: How do I change the inactivity session timeout for my organization?
  phrasing_ops: 2
  slug: controlup-organization-settings-api
- baseURL: https://api.controlup.com/v1
  baseurl_source: declared
  description: The Organizations API from ControlUp — 2 operation(s) for organizations.
  name: ControlUp Organizations API
  phrasing_intents:
  - id: OrgPublicController_getTenantOrganizations
    intent: List tenants under a Tenant Manager
    question: Which tenant organizations do I manage as an MSP?
  - id: OrgPublicController_createTenantOrganization
    intent: Create a tenant organization
    question: How do I create a new customer tenant as an MSP?
  - id: OrgPublicController_copyEdgeTenantData
    intent: Copy Desktops scripts, alerts and dashboards between tenants
    question: How do I copy ControlUp for Desktops scripts and dashboards from one tenant to another?
  phrasing_ops: 3
  slug: controlup-organizations-api
- baseURL: https://api.controlup.com/v1
  baseurl_source: declared
  description: The Overview API from ControlUp — 11 operation(s) for overview.
  name: ControlUp Overview API
  phrasing_intents:
  - id: GetOverviewGraph
    intent: Get resource counts per hierarchy level
    question: How many subscriptions, host pools, session hosts and sessions do I have in total?
  - id: GetOverviewSubscriptions
    intent: Summarize cost and contents per subscription
    question: What does each subscription contain and cost?
  - id: GetOverviewRegions
    intent: Summarize onboarded resources per region
    question: Which regions hold onboarded resources, and what do they cost?
  - id: GetOverviewResourceGroups
    intent: Summarize onboarded resources per resource group
    question: Which resource groups hold my host pools, and what do they cost?
  - id: GetOverviewHostPools
    intent: Summarize cost and performance per host pool
    question: Which host pools cost the most, with their session counts and performance?
  - id: GetOverviewSessionHosts
    intent: Summarize every session host with cost and load
    question: Which session hosts anywhere are powered on and costing the most?
  - id: GetOverviewImages
    intent: Summarize images running in the estate
    question: Which images are my onboarded resources running, and how many consumers does each have?
  - id: GetOverviewMasterImages
    intent: Summarize managed master images
    question: How many versions does each DaaS IQ master image have?
  phrasing_ops: 11
  slug: controlup-overview-api
- baseURL: https://api.controlup.com/v1
  baseurl_source: declared
  description: Process usage reports
  name: ControlUp Processes API
  phrasing_intents:
  - id: getProcessUsageSingle
    intent: Get usage details for one process
    question: Which users and machines ran a particular application, and what was its peak concurrency?
  - id: getProcessUsageAll
    intent: Get daily usage across all processes
    question: What's the daily unique-user count across all processes?
  phrasing_ops: 2
  slug: controlup-processes-api
- baseURL: https://api.controlup.com/v1
  baseurl_source: declared
  description: The Public API API from ControlUp — 11 operation(s) for public api.
  name: ControlUp Public API
  phrasing_intents:
  - id: get_flows_workflows_v1_flows_get
    intent: List workflows in the organization
    question: Which automation workflows exist in my ControlUp organization?
  - id: get_flow_workflows_v1_flows__flowId__get
    intent: Get a workflow's details
    question: What does a specific workflow contain and how is it configured?
  - id: update_flow_status_workflows_v1_flows__flowId__patch
    intent: Enable or disable a workflow
    question: How do I pause a workflow without deleting it?
  - id: delete_flow_workflows_v1_flows__flowId__delete
    intent: Delete a workflow
    question: How do I permanently remove a workflow I no longer need?
  - id: get_flow_runs_workflows_v1_flows__flowId__runs_get
    intent: Get a workflow's run history and status
    question: Did the last runs of my workflow succeed or fail?
  - id: launch_flow_workflows_v1_flows_launch_post
    intent: Launch a workflow run
    question: How do I trigger a workflow to run right now?
  - id: get_all_forms_workflows_v1_forms_get
    intent: List workflow forms
    question: Which forms are set up in my organization's workflows?
  - id: get_form_workflows_v1_forms__formId__get
    intent: Get a workflow form's details
    question: What fields and settings does a particular form have?
  phrasing_ops: 15
  slug: controlup-public-api-api
- baseURL: https://api.controlup.com/v1
  baseurl_source: declared
  description: The Roles API from ControlUp — 2 operation(s) for roles.
  name: ControlUp Roles API
  phrasing_intents:
  - id: OrgRolesPublicController_getAll
    intent: List roles in the organization
    question: Which roles exist in my ControlUp organization?
  - id: OrgRolesPublicController_create
    intent: Create a role
    question: How do I create a custom role with specific permissions?
  - id: OrgRolesPublicController_getOneById
    intent: Get a role's permissions and assignees
    question: What permissions does a specific role grant?
  - id: OrgRolesPublicController_update
    intent: Update a role
    question: How do I add or remove users from an existing role?
  - id: OrgRolesPublicController_delete
    intent: Delete a role
    question: What happens to users assigned a role when I delete it?
  phrasing_ops: 5
  slug: controlup-roles-api
- baseURL: https://api.controlup.com/v1
  baseurl_source: declared
  description: The SAML API from ControlUp — 2 operation(s) for saml.
  name: ControlUp SAML API
  phrasing_intents:
  - id: OrgSamlPublicController_getOneById
    intent: Get the SAML SSO configuration
    question: What SAML settings are currently saved for my organization?
  - id: OrgSamlPublicController_create
    intent: Set up SAML SSO, overwriting any existing
    question: Can I configure SAML SSO from scratch with my IdP's certificate and SSO URL?
  - id: OrgSamlPublicController_update
    intent: Update specific SAML settings
    question: Can I rotate just the SAML signing certificate?
  - id: OrgSamlPublicController_configureByIdp
    intent: Auto-configure SAML from an IdP integration
    question: Can SAML SSO be set up automatically from my Entra ID integration?
  phrasing_ops: 4
  slug: controlup-saml-api
- baseURL: https://api.controlup.com/v1
  baseurl_source: declared
  description: The Scaling profiles API from ControlUp — 3 operation(s) for scaling profiles.
  name: ControlUp Scaling profiles API
  phrasing_intents:
  - id: GetScalingProfiles
    intent: List autoscale scaling profiles
    question: Which reusable autoscale profiles are defined in my organization?
  - id: CreateScalingProfile
    intent: Create a scaling profile
    question: How do I define a new autoscale configuration I can assign to host pool schedules?
  - id: GetScalingProfile
    intent: Get a scaling profile's configuration
    question: What thresholds and host count rules does a scaling profile use?
  - id: UpdateScalingProfile
    intent: Replace a scaling profile's configuration
    question: How do I change the scaling strategy of an existing profile?
  - id: DeleteScalingProfile
    intent: Delete a scaling profile
    question: How do I remove a scaling profile I no longer use?
  - id: UpdateScalingProfileColor
    intent: Change a scaling profile's display color
    question: Can I change just the color a scaling profile shows on the schedule?
  phrasing_ops: 6
  slug: controlup-scaling-profiles-api
- baseURL: https://api.controlup.com/v1
  baseurl_source: declared
  description: 'Scouts are the proactive tests that you configure to monitor the availability and health of various resources. There are different types of Scouts, depending on the type of resource you want to test. '
  name: ControlUp Scouts API
  phrasing_intents:
  - id: app.get_scouts
    intent: List Scouts
    question: Which synthetic monitoring Scouts do I have running?
  - id: app.create_scout
    intent: Create a Scout
    question: Can I set up a Scout to test an EUC or network resource?
  - id: app.get_scout_by_id
    intent: Get a Scout and its test summary
    question: How has one Scout's testing performed over the last 24 hours?
  - id: app.edit_scout
    intent: Edit a Scout
    question: Can I change a Scout's settings without resending everything?
  - id: app.delete_scout
    intent: Delete a Scout
    question: Can I permanently delete a Scout and get its credits back?
  - id: app.disable_scout
    intent: Enable or disable a Scout
    question: Can I pause a Scout's tests without deleting it?
  phrasing_ops: 6
  slug: controlup-scouts-api
- baseURL: https://api.controlup.com/v1
  baseurl_source: declared
  description: The Scripts API from ControlUp — 1 operation(s) for scripts.
  name: ControlUp Scripts API
  phrasing_intents:
  - id: list-all-scripts
    intent: List all device scripts
    question: Which scripts are available to run on my devices?
  phrasing_ops: 1
  slug: controlup-scripts-api
- baseURL: https://api.controlup.com/v1
  baseurl_source: declared
  description: Session statistics report
  name: ControlUp Session API
  phrasing_intents:
  - id: getSessionsStatistics
    intent: Get user session statistics for a period
    question: What were each user's session statistics over the last week?
  - id: getSessionTimeline
    intent: Get a session's state-change timeline
    question: When did a particular session connect, disconnect and log off?
  - id: getSessionDetails
    intent: Get activity details of an individual session
    question: What happened during one specific user's session on a machine?
  - id: getSessionsAggregated
    intent: Aggregate session metrics by a dimension
    question: What is the average logon duration per delivery group?
  phrasing_ops: 4
  slug: controlup-session-api
- baseURL: https://api.controlup.com/v1
  baseurl_source: declared
  description: The Session hosts API from ControlUp — 2 operation(s) for session hosts.
  name: ControlUp Session hosts API
  phrasing_intents:
  - id: ExecuteSessionHostAction
    intent: Restart, stop, drain or remove a session host
    question: How do I put a session host into drain mode before maintenance?
  - id: GetSessionHostSessions
    intent: List users logged in to a session host
    question: Who is logged in to a specific session host right now?
  phrasing_ops: 2
  slug: controlup-session-hosts-api
- baseURL: https://api.controlup.com/v1
  baseurl_source: declared
  description: The SSO Groups API from ControlUp — 2 operation(s) for sso groups.
  name: ControlUp SSO Groups API
  phrasing_intents:
  - id: OrgSsoGroupsPublicController_getAll
    intent: List SSO groups
    question: Which SSO groups are defined in my organization?
  - id: OrgSsoGroupsPublicController_create
    intent: Create an SSO group
    question: Can I map an IdP group into ControlUp as a new SSO group?
  - id: OrgSsoGroupsPublicController_update
    intent: Update an SSO group
    question: Can I rename an existing SSO group?
  - id: OrgSsoGroupsPublicController_delete
    intent: Delete an SSO group
    question: Can I remove an SSO group from my organization?
  phrasing_ops: 4
  slug: controlup-sso-groups-api
- baseURL: https://api.controlup.com/v1
  baseurl_source: declared
  description: The Subscriptions API from ControlUp — 27 operation(s) for subscriptions.
  name: ControlUp Subscriptions API
  phrasing_intents:
  - id: VerifySubscriptionCredentials
    intent: Verify a subscription's cloud credentials (deprecated)
    question: Can I check whether the stored cloud credentials on a subscription still work using the older subscription-level endpoint?
  - id: VerifySubscriptionCredentialsTranscript
    intent: Get a step-by-step credential check transcript (deprecated)
    question: Can I get a detailed transcript of each permission check when verifying a subscription's credentials?
  - id: getCloudSubscriptionsByIdCredentialsVerifyStream
    intent: Stream subscription credential check over WebSocket
    question: Is there an old WebSocket stream that shows live progress while a subscription's cloud credentials are verified?
  - id: postCloudSubscriptionsByIdCredentialsVerifySse
    intent: Stream subscription credential check over SSE
    question: Can I get server-sent events while my subscription's cloud credentials are being verified?
  - id: GetRegions
    intent: List regions a subscription can deploy into
    question: Which Azure regions can my subscription deploy session hosts into?
  - id: GetRegionMetadata
    intent: Get one region's metadata and availability zones
    question: What availability zones does a specific region offer for my subscription?
  - id: GetVmSizes
    intent: List VM sizes offered in a region
    question: Which VM sizes can I pick in a given region, with their CPU and memory specs?
  - id: GetOsDisks
    intent: List OS disk size options for a region
    question: What OS disk sizes can I choose for session hosts in a region?
  phrasing_ops: 31
  slug: controlup-subscriptions-api
- baseURL: https://api.controlup.com/v1
  baseurl_source: declared
  description: Provides an additional information about customer's data
  name: ControlUp Support endpoint API
  phrasing_intents:
  - id: getStartUploadDate
    intent: Get when historical data upload began
    question: When did the first historical data upload start?
  phrasing_ops: 1
  slug: controlup-support-endpoint-api
- baseURL: https://api.controlup.com/v1
  baseurl_source: declared
  description: These endpoints are for interacting with Employee Sentiment surveys.
  name: ControlUp Surveys API
  phrasing_intents:
  - id: get-surveys
    intent: List user sentiment surveys
    question: What user sentiment surveys have we run?
  - id: publish-survey
    intent: Publish a new survey
    question: Can I publish a new user sentiment survey through the API?
  - id: get-survey
    intent: Get a survey
    question: What are the details of a specific survey?
  - id: delete-survey
    intent: Delete a survey
    question: Can I delete a survey I no longer need?
  - id: pause-survey
    intent: Pause a survey
    question: Can I temporarily pause a running survey?
  - id: resume-survey
    intent: Resume a paused survey
    question: Can I restart a survey that I paused?
  - id: complete-survey
    intent: Complete a survey
    question: Can I close out a survey and mark it complete?
  - id: get-survey-results
    intent: Get survey open, start and completion events
    question: How many users opened, started or completed a survey?
  phrasing_ops: 9
  slug: controlup-surveys-api
- baseURL: https://api.controlup.com/v1
  baseurl_source: declared
  description: The Tags API from ControlUp — 2 operation(s) for tags.
  name: ControlUp Tags API
  phrasing_intents:
  - id: OrgTagsPublicController_getAll
    intent: List organization tags
    question: Which tags are defined in my ControlUp organization?
  - id: OrgTagsPublicController_create
    intent: Create an organization tag
    question: Can I create a new tag key with a set of allowed values?
  - id: OrgTagsPublicController_getOneById
    intent: Retrieve an organization tag
    question: What values does a specific org tag have?
  - id: OrgTagsPublicController_update
    intent: Update an organization tag
    question: Can I add new values to an existing org tag?
  - id: OrgTagsPublicController_delete
    intent: Delete an organization tag
    question: Can I remove a tag from my organization?
  phrasing_ops: 5
  slug: controlup-tags-api
- baseURL: https://api.controlup.com/v1
  baseurl_source: declared
  description: The Tenants API from ControlUp — 23 operation(s) for tenants.
  name: ControlUp Tenants API
  phrasing_intents:
  - id: GetTenantCredentials
    intent: List the credentials in a tenant pool
    question: Which service principals are in my cloud tenant's credential pool?
  - id: AddTenantCredential
    intent: Add a credential to a tenant pool
    question: Can I add another service principal to a tenant to spread API calls for load balancing?
  - id: GetTenantCredential
    intent: Get one tenant credential configuration
    question: What auth type and enabled flag does a specific tenant credential have?
  - id: UpdateTenantCredential
    intent: Replace a tenant credential's auth details
    question: Can I fully replace the authentication details of an existing tenant credential?
  - id: PatchTenantCredential
    intent: Partially update a tenant credential
    question: Can I change just the client secret on a credential without resending everything?
  - id: DeleteTenantCredential
    intent: Delete a tenant credential
    question: What happens to the default when I delete a tenant's default credential?
  - id: EnableTenantCredential
    intent: Enable a credential in the pool
    question: How do I put a disabled tenant credential back into round-robin rotation?
  - id: DisableTenantCredential
    intent: Disable a credential in the pool
    question: Can I take a credential out of rotation without deleting it?
  phrasing_ops: 31
  slug: controlup-tenants-api
- baseURL: https://api.controlup.com/v1
  baseurl_source: declared
  description: The output of the scout tests
  name: ControlUp Tests API
  phrasing_intents:
  - id: app.get_tests
    intent: List Scout test results
    question: What were the results of my Scout tests over the last day?
  phrasing_ops: 1
  slug: controlup-tests-api
- baseURL: https://api.controlup.com/v1
  baseurl_source: declared
  description: The Triggers API from ControlUp — 2 operation(s) for triggers.
  name: ControlUp Triggers API
  phrasing_intents:
  - id: getV1Triggers
    intent: List the organization's triggers
    question: Which alert triggers are set up in my organization, and which are disabled?
  - id: getV1TriggersByTriggerId
    intent: Get full details of one trigger
    question: What actions, scope and schedule does a specific trigger have?
  phrasing_ops: 2
  slug: controlup-triggers-api
- baseURL: https://api.controlup.com/v1
  baseurl_source: declared
  description: The TriggerSchedules API from ControlUp — 2 operation(s) for triggerschedules.
  name: ControlUp Trigger Schedules API
  phrasing_intents:
  - id: getV1TriggerSchedules
    intent: List trigger schedules
    question: Which schedules are available for my triggers?
  - id: getV1TriggerSchedulesByScheduleId
    intent: Get one trigger schedule and its usage
    question: What does a specific trigger schedule contain, and which triggers use it?
  phrasing_ops: 2
  slug: controlup-triggerschedules-api
- baseURL: https://api.controlup.com/v1
  baseurl_source: declared
  description: User activity reports
  name: ControlUp User API
  phrasing_intents:
  - id: getUserActivity
    intent: Get user activity status over time
    question: Was a given user active or idle during each five-minute window yesterday?
  phrasing_ops: 1
  slug: controlup-user-api
- baseURL: https://api.controlup.com/v1
  baseurl_source: declared
  description: The User sessions API from ControlUp — 1 operation(s) for user sessions.
  name: ControlUp User sessions API
  phrasing_intents:
  - id: ExecuteUserSessionAction
    intent: Message, sign out or disconnect a user session
    question: How do I send a warning message to a user before maintenance?
  phrasing_ops: 1
  slug: controlup-user-sessions-api
- baseURL: https://api.controlup.com/v1
  baseurl_source: declared
  description: The Users API from ControlUp — 4 operation(s) for users.
  name: ControlUp Users API
  phrasing_intents:
  - id: getUsersUserInfo
    intent: Get the signed-in user's own identity
    question: Who am I signed in as, and which organization does my token belong to?
  - id: OrgUsersPublicController_getAll
    intent: List users in the organization
    question: Who are the users in my ControlUp organization, including pending invitations?
  - id: OrgUsersPublicController_getOneById
    intent: Get a user's details
    question: What are the details of a specific user account?
  - id: OrgUsersPublicController_update
    intent: Update a user's roles, login and MFA
    question: How do I change which roles a user has?
  - id: OrgUsersPublicController_delete
    intent: Delete a user
    question: How do I remove someone from my organization?
  - id: OrgUsersPublicController_revoke
    intent: Revoke all of a user's API keys
    question: How do I cut off every API key a departing user created?
  phrasing_ops: 6
  slug: controlup-users-api
- baseURL: https://api.controlup.com/v1
  baseurl_source: declared
  description: Windows Event Log Monitoring history
  name: ControlUp Windows Events API
  phrasing_intents:
  - id: getWindowsEvents
    intent: Search monitored Windows event log entries
    question: Which Windows error events hit a particular machine in the last month?
  phrasing_ops: 1
  slug: controlup-windowsevents-api
artifact_total: 130
asyncapis:
- description: ''
  name: Controlup Webhooks
  slug: controlup-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Controlup Alerts API
  slug: open-controlup-alerts-api
- collection_type: open
  name: Dex Alerts Alerts - Devices API
  slug: open-controlup-alerts-devices-api
- collection_type: open
  name: VDI & DAAS Applications API
  slug: open-controlup-applications-api
- collection_type: open
  name: Dex Audit Log API
  slug: open-controlup-audit-log-api
- collection_type: open
  name: DaaS IQ Cloud providers API
  slug: open-controlup-cloud-providers-api
- collection_type: open
  name: ControlUp for Desktops Dal API
  slug: open-controlup-dal-api
- collection_type: open
  name: ControlUp for Desktops Data API
  slug: open-controlup-data-api
- collection_type: open
  name: Controlup Devices API
  slug: open-controlup-devices-api
- collection_type: open
  name: VDI & DAAS Dynamic Query API API
  slug: open-controlup-dynamic-query-api-api
- collection_type: open
  name: Controlup Events API
  slug: open-controlup-events-api
- collection_type: open
  name: DaaS IQ Features API
  slug: open-controlup-features-api
- collection_type: open
  name: DaaS IQ Health API
  slug: open-controlup-health-api
- collection_type: open
  name: Synthetic Monitoring Hives API
  slug: open-controlup-hives-api
- collection_type: open
  name: VDI & DAAS Host API
  slug: open-controlup-host-api
- collection_type: open
  name: DaaS IQ Host pool cost API
  slug: open-controlup-host-pool-cost-api
- collection_type: open
  name: DaaS IQ Host pool deployments API
  slug: open-controlup-host-pool-deployments-api
- collection_type: open
  name: DaaS IQ Host pool scaling policies API
  slug: open-controlup-host-pool-scaling-policies-api
- collection_type: open
  name: DaaS IQ Host pool session host deployments API
  slug: open-controlup-host-pool-session-host-deployments-api
- collection_type: open
  name: DaaS IQ Host pool session hosts API
  slug: open-controlup-host-pool-session-hosts-api
- collection_type: open
  name: DaaS IQ Host pool user sessions API
  slug: open-controlup-host-pool-user-sessions-api
- collection_type: open
  name: DaaS IQ Host pool VM settings API
  slug: open-controlup-host-pool-vm-settings-api
- collection_type: open
  name: DaaS IQ Host pools API
  slug: open-controlup-host-pools-api
- collection_type: open
  name: Synthetic Monitoring Integrations API
  slug: open-controlup-integrations-api
- collection_type: open
  name: Dex Invitations API
  slug: open-controlup-invitations-api
- collection_type: open
  name: Dex IP Allowlist API
  slug: open-controlup-ip-allowlist-api
- collection_type: open
  name: DaaS IQ Jobs API
  slug: open-controlup-jobs-api
- collection_type: open
  name: DaaS IQ License API
  slug: open-controlup-license-api
- collection_type: open
  name: Dex License Usage API
  slug: open-controlup-license-usage-api
- collection_type: open
  name: VDI & DAAS Machine API
  slug: open-controlup-machine-api
- collection_type: open
  name: VDI & DaaS Configuration Machines API
  slug: open-controlup-machines-api
- collection_type: open
  name: DaaS IQ Master images API
  slug: open-controlup-master-images-api
- collection_type: open
  name: VDI & DaaS Realtime Metrics API
  slug: open-controlup-metrics-api
- collection_type: open
  name: Synthetic Monitoring MF As API
  slug: open-controlup-mfas-api
- collection_type: open
  name: VDI & DAAS Net Scaler API
  slug: open-controlup-netscaler-api
- collection_type: open
  name: DaaS IQ Onboarding API
  slug: open-controlup-onboarding-api
- collection_type: open
  name: Dex Organization Settings API
  slug: open-controlup-organization-settings-api
- collection_type: open
  name: Dex Organizations API
  slug: open-controlup-organizations-api
- collection_type: open
  name: DaaS IQ Overview API
  slug: open-controlup-overview-api
- collection_type: open
  name: VDI & DAAS Processes API
  slug: open-controlup-processes-api
- collection_type: open
  name: Flow3 Public Public API API
  slug: open-controlup-public-api-api
- collection_type: open
  name: Dex Roles API
  slug: open-controlup-roles-api
- collection_type: open
  name: Dex SAML API
  slug: open-controlup-saml-api
- collection_type: open
  name: DaaS IQ Scaling profiles API
  slug: open-controlup-scaling-profiles-api
- collection_type: open
  name: Synthetic Monitoring Scouts API
  slug: open-controlup-scouts-api
- collection_type: open
  name: ControlUp for Desktops Scripts API
  slug: open-controlup-scripts-api
- collection_type: open
  name: VDI & DAAS Session API
  slug: open-controlup-session-api
- collection_type: open
  name: DaaS IQ Session hosts API
  slug: open-controlup-session-hosts-api
- collection_type: open
  name: Dex SSO Groups API
  slug: open-controlup-sso-groups-api
- collection_type: open
  name: DaaS IQ Subscriptions API
  slug: open-controlup-subscriptions-api
- collection_type: open
  name: VDI & DAAS Support endpoint API
  slug: open-controlup-support-endpoint-api
- collection_type: open
  name: ControlUp for Desktops Surveys API
  slug: open-controlup-surveys-api
- collection_type: open
  name: Dex Tags API
  slug: open-controlup-tags-api
- collection_type: open
  name: DaaS IQ Tenants API
  slug: open-controlup-tenants-api
- collection_type: open
  name: Synthetic Monitoring Tests API
  slug: open-controlup-tests-api
- collection_type: open
  name: VDI & DaaS Configuration Triggers API
  slug: open-controlup-triggers-api
- collection_type: open
  name: VDI & DaaS Configuration Trigger Schedules API
  slug: open-controlup-triggerschedules-api
- collection_type: open
  name: VDI & DAAS User API
  slug: open-controlup-user-api
- collection_type: open
  name: DaaS IQ User sessions API
  slug: open-controlup-user-sessions-api
- collection_type: open
  name: Controlup Users API
  slug: open-controlup-users-api
- collection_type: open
  name: VDI & DAAS Windows Events API
  slug: open-controlup-windowsevents-api
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/controlup/refs/heads/main/plans/controlup-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/controlup-plans-pricing.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/controlup/refs/heads/main/capabilities/controlup-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/controlup-capability-edges.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/controlup/refs/heads/main/security/controlup-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/controlup-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/controlup/refs/heads/main/authentication/controlup-authentication.yml
  title: ''
  type: Authentication
  url: authentication/controlup-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.controlup.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.controlup.io/
- group: docs
  title: ''
  type: Documentation
  url: https://support.controlup.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://api.controlup.io/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://api.controlup.io/reference/how-to-make-api-requests-1
- group: operate
  title: ''
  type: Support
  url: https://support.controlup.com/
- group: company
  title: ''
  type: Blog
  url: https://www.controlup.com/resources/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/controlup
- group: operate
  title: ''
  type: Roadmap
  url: https://support.controlup.com/docs/submit-and-vote-on-feature-requests
- group: commercial
  title: ''
  type: Pricing
  url: https://www.controlup.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://www.controlup.com/free-trial/
- group: start
  title: ''
  type: Login
  url: https://app.controlup.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.controlup.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.controlup.com/privacy-policy/controlup-privacy-policy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.controlup.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://support.controlup.com/docs/release-notes
- group: auth
  title: ''
  type: TrustCenter
  url: https://trustcenter.controlup.com/
- group: auth
  title: ''
  type: Compliance
  url: https://trustcenter.controlup.com/
- group: auth
  title: ''
  type: Security
  url: https://trustcenter.controlup.com/
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/controlup/refs/heads/main/well-known/controlup-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/controlup-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/controlup/refs/heads/main/well-known/controlup-api-catalog.json
  title: ''
  type: APICatalog
  url: well-known/controlup-api-catalog.json
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/controlup/refs/heads/main/mcp/controlup-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/controlup-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/controlup/refs/heads/main/mcp/controlup-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/controlup-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/controlup/refs/heads/main/llms/controlup-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/controlup-llms.txt
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/controlup/refs/heads/main/packages/controlup-packages.yml
  title: ''
  type: Packages
  url: packages/controlup-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/controlup/refs/heads/main/packages/controlup-packages.yml
  title: ''
  type: SDKs
  url: packages/controlup-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/controlup/refs/heads/main/cli/controlup-cli.yml
  title: ''
  type: CLI
  url: cli/controlup-cli.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/controlup/refs/heads/main/conventions/controlup-conventions.yml
  title: ''
  type: Conventions
  url: conventions/controlup-conventions.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/controlup/refs/heads/main/rate-limits/controlup-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/controlup-rate-limits.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/controlup/refs/heads/main/errors/controlup-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/controlup-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/controlup/refs/heads/main/data-model/controlup-data-model.yml
  title: ''
  type: DataModel
  url: data-model/controlup-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/controlup/refs/heads/main/lifecycle/controlup-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/controlup-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://support.controlup.com/docs/controlup-product-version-lifecycle-quick-guide
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/controlup/refs/heads/main/changelog/controlup-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/controlup-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/controlup/refs/heads/main/conformance/controlup-conformance.yml
  title: ''
  type: Conformance
  url: conformance/controlup-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/controlup/refs/heads/main/security/controlup-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/controlup-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/controlup/refs/heads/main/security/controlup-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/controlup-trust-center.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/controlup/refs/heads/main/asyncapi/controlup-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/controlup-webhooks.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/controlup/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/controlup/refs/heads/main/overlays/controlup-dex-platform-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/controlup-dex-platform-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/controlup/refs/heads/main/overlays/controlup-dex-alerts-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/controlup-dex-alerts-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/controlup/refs/heads/main/overlays/controlup-dex-events-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/controlup-dex-events-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/controlup/refs/heads/main/overlays/controlup-desktops-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/controlup-desktops-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/controlup/refs/heads/main/overlays/controlup-compliance-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/controlup-compliance-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/controlup/refs/heads/main/overlays/controlup-vdi-daas-historical-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/controlup-vdi-daas-historical-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/controlup/refs/heads/main/overlays/controlup-vdi-daas-realtime-metrics-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/controlup-vdi-daas-realtime-metrics-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/controlup/refs/heads/main/overlays/controlup-vdi-daas-configuration-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/controlup-vdi-daas-configuration-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/controlup/refs/heads/main/overlays/controlup-vdi-config-triggers-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/controlup-vdi-config-triggers-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/controlup/refs/heads/main/overlays/controlup-daas-iq-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/controlup-daas-iq-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/controlup/refs/heads/main/overlays/controlup-synthetic-monitoring-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/controlup-synthetic-monitoring-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/controlup/refs/heads/main/overlays/controlup-workflows-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/controlup-workflows-overlay.yaml
created: '2026-08-04'
description: ControlUp is a Digital Employee Experience (DEX) and Autonomous Endpoint Management (AEM) platform that monitors, scores and remediates the end-user computing estate — physical desktops and laptops, VDI and DaaS (Citrix CVAD / Citrix Cloud, Omnissa Horizon, Azure Virtual Desktop, Windows 365, Parallels RAS), the applications and sessions running on them, and the network path in between. The ControlUp ONE platform spans ControlUp for Desktops, for VDI, for Apps, for Frontline Workers and for Compliance, plus Synthetic Monitoring (Scouts and Hives), Workflows, and Pulse AI. It publishes a public REST API surface at api.controlup.com documented on a ReadMe hub at api.controlup.io, an RFC 9727 /.well-known/api-catalog linkset enumerating twelve OpenAPI definitions, an official Model Context Protocol server on npm (@controlup-ai/mcp) exposing 106 tools across six product domains, PowerShell cmdlets for monitor and agent automation, and llms.txt indexes on both the documentation and
  API hosts.
image: https://www.controlup.com/wp-content/uploads/controlup_prev.webp
layout: provider
mcp_servers:
- description: Local (stdio) MCP server; 106 tools listed.
  name: ControlUp MCP Server
  slug: controlup
modified: '2026-09-16'
name: ControlUp
nav: Providers
network: true
overview: 'ControlUp publishes 61 APIs on the [APIs.io](https://apis.io/) network, including Alerts API, Alerts - Devices API, Applications API, and 58 more. Tagged areas include Digital Employee Experience, Endpoint Management, VDI, DaaS, and Virtual Desktop.


  The ControlUp catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  ControlUp''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 48 more developer resources.'
plans:
- name: Controlup Plans Pricing
  plan_count: 6
  slug: controlup-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 6
  name: Controlup Rate Limits
  slug: controlup-rate-limits
score:
  band: exemplar
  composite: 75.6
  coverage:
    artifact_dirs: 24
    catalog_earned: 64.0
    catalog_earned_first_party: 24.0
    catalog_gap: 51.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.6
  facets:
    access_clarity: 92.1
    contract_governance: 4.5
    contract_quality: 63.8
    developer_ergonomics: 58.9
    discoverability: 78.6
    operational_transparency: 97.4
  previous_composite: 75.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 60
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 35.3
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  trend: flat
  upsert:
    applies: true
    score: 61.1
screenshot: https://raw.githubusercontent.com/api-evangelist/controlup/refs/heads/main/screenshots/controlup-2026-08-07T163802.png
security:
- kind: authentication
  name: Controlup Authentication
  slug: controlup-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Controlup Domain Security
  slug: controlup-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Controlup Vulnerability Disclosure
  slug: controlup-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Controlup Trust Center
  slug: controlup-trust-center
  summary_line: ISO/IEC 27001:2022, ISO/IEC 27017:2015, ISO/IEC 27018:2019, ISO/IEC 27701:2019, SOC 2 Type 2, SOC 3, FIPS 140-2 Level 1, CSA STAR Level 1, GDPR
slug: controlup
tags:
- Digital Employee Experience
- Endpoint Management
- VDI
- DaaS
- Virtual Desktop
- Observability
- Monitoring
- Synthetic Monitoring
- Device Management
- Compliance
- Vulnerability Management
- Workflow Automation
- Citrix
- Azure Virtual Desktop
- MCP
- Agent-Native
website: https://www.controlup.com/
---
