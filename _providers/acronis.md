---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: verified
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 56.3
  scored_at: '2026-10-03'
agentic_access:
- acting_count: 167
  human_in_the_loop: 5
  name: Acronis Agentic Access
  operation_count: 320
  slug: acronis-agentic-access
  summary_line: 320 operations · 167 acting · 5 human-in-the-loop
api_count: 12
apis:
- baseURL: https://{datacenter}.acronis.com/api/2
  baseurl_source: declared
  description: Task activity and sub-operation tracking
  name: Acronis Activities API
  phrasing_intents:
  - id: FetchAListOfActivities
    intent: List task activities
    question: How do I see the activities that ran for a particular backup policy?
  - id: FetchAnActivity
    intent: Get an activity with detail level
    question: Can I fetch one activity at a chosen level of detail, including deleted ones?
  - id: getActivity
    intent: Get a task activity by ID
    question: What happened in a specific task activity?
  phrasing_ops: 3
  slug: acronis-activities-api
- baseURL: https://{datacenter}.acronis.com/api/2
  baseurl_source: declared
  description: Agent update configuration and execution
  name: Acronis Agent Updates API
  phrasing_intents:
  - id: forceAgentUpdate
    intent: Force-update agents now
    question: How do I push an agent update immediately, ignoring the maintenance window?
  - id: getAgentUpdateSettings
    intent: Get agent update settings
    question: What update channel and maintenance window are agents using?
  - id: updateAgentUpdateSettings
    intent: Change agent update settings
    question: How do I switch agents to a different update channel?
  phrasing_ops: 3
  slug: acronis-agent-updates-api
- baseURL: https://{datacenter}.acronis.com/api/agent_manager/v2
  baseurl_source: declared
  description: Acronis protection agent management
  name: Acronis Agents API
  phrasing_intents:
  - id: FetchAgents
    intent: List registered agents
    question: How do I list every protection agent registered under my tenant and its children?
  - id: DeleteAgents
    intent: Unregister agents
    question: Can I unregister agents and remove their service accounts in one call?
  - id: RunAgentUpdateNow
    intent: Update agents immediately
    question: How do I push an agent update right now, ignoring the maintenance window?
  - id: FetchAgent
    intent: Get one registered agent
    question: How can I see the details of a single agent?
  - id: DeleteAgent
    intent: Unregister one agent
    question: How do I unregister a single agent from the platform?
  phrasing_ops: 5
  slug: acronis-agents-api
- baseURL: https://{datacenter}.acronis.com/api/2
  baseurl_source: declared
  description: OAuth2 client credential management
  name: Acronis Clients API
  phrasing_intents:
  - id: CreateClient
    intent: Create an API client
    question: How do I create API client credentials for a tenant?
  - id: FetchClientsBatch
    intent: List API clients
    question: Which API clients exist for my tenant?
  - id: DeleteClient
    intent: Delete an API client
    question: How do I delete API client credentials?
  - id: UpdateClient
    intent: Update an API client
    question: How do I disable an API client?
  - id: FetchClient
    intent: Get an API client
    question: How do I look up one API client by ID?
  phrasing_ops: 5
  slug: acronis-clients-api
- baseURL: https://{datacenter}.acronis.com/api/2
  baseurl_source: declared
  description: Hardware node management
  name: Acronis Hardware Nodes API
  phrasing_intents:
  - id: FetchHardwareNodes
    intent: List hardware nodes
    question: Which hardware nodes are registered in my tenant and its child tenants?
  - id: FetchHardwareNode
    intent: Get one hardware node
    question: How do I look up a single hardware node's details?
  phrasing_ops: 2
  slug: acronis-hardware-nodes-api
- baseURL: https://{datacenter}.acronis.com/api/task_manager/v2
  baseurl_source: declared
  description: Backup and protection task monitoring
  name: Acronis Tasks API
  phrasing_intents:
  - id: Fetch a list of tasks
    intent: List tasks
    question: How do I list the backup tasks that failed today?
  - id: Fetch a task
    intent: Get a task with detail level
    question: Can I fetch one task at a chosen level of detail, including deleted ones?
  phrasing_ops: 2
  slug: acronis-tasks-api
- baseURL: https://{datacenter}.acronis.com/api/2
  baseurl_source: declared
  description: Tenant hierarchy management and configuration
  name: Acronis Tenants API
  phrasing_intents:
  - id: FetchTenantsBatch
    intent: Fetch several tenants or a tenant's children
    question: How do I pull details for a list of tenants by their UUIDs in one call?
  - id: CreateTenant
    intent: Create a new tenant
    question: How do I create a new customer tenant under my partner account?
  - id: FetchTenantsApplicationsBatch
    intent: List application IDs for several tenants
    question: Which applications are enabled for each of these tenants at once?
  - id: FetchTenantOfferingItemsBatch
    intent: Fetch offering items across a tenant tree
    question: How can I see offering items and quotas for every tenant below a given tenant?
  - id: FetchTenantsUsagesBatch
    intent: Fetch usage metrics for several tenants
    question: Can I get usage figures for a batch of tenants at the same time?
  - id: UpdateTenantsUsages
    intent: Report usage values for tenants
    question: How do I report usage values for my tenants from an external integration?
  - id: DeleteTenant
    intent: Delete a tenant
    question: How do I delete a customer tenant I no longer need?
  - id: UpdateTenant
    intent: Update a tenant's properties
    question: How do I rename a tenant or disable it?
  phrasing_ops: 36
  slug: acronis-tenants-api
- baseURL: https://{datacenter}.acronis.com/api/2
  baseurl_source: declared
  description: User account management within tenants
  name: Acronis Users API
  phrasing_intents:
  - id: FetchUsersBatch
    intent: List users in a tenant
    question: How do I list all users that belong to a tenant?
  - id: CreateUser
    intent: Create a user account
    question: How do I add a new user to a customer tenant?
  - id: CheckLoginNameAvailability
    intent: Check if a username is taken
    question: Is a particular login name still available?
  - id: CheckPassword
    intent: Check a password against breach data
    question: Has a password appeared in a known data breach?
  - id: FetchCurrentUserInfo
    intent: Get the signed-in user's profile
    question: Who am I authenticated as right now?
  - id: DeleteUser
    intent: Delete a user account
    question: How do I delete a user account?
  - id: UpdateUser
    intent: Update a user account
    question: How do I change a user's contact info or language?
  - id: FetchUser
    intent: Get a user by ID
    question: How do I look up a single user account by its ID?
  phrasing_ops: 15
  slug: acronis-users-api
- baseURL: https://{datacenter}.acronis.com/api
  baseurl_source: declared
  description: The Abgw Storages API from Acronis — 1 operation(s) for abgw storages.
  name: Acronis Abgw Storages API
  phrasing_intents:
  - id: UnregisterStorage
    intent: Unregister an on-premises storage
    question: How do I unregister a storage from the account server in an on-premises setup?
  phrasing_ops: 1
  slug: acronis-abgw-storages-api
- baseURL: https://{datacenter}.acronis.com/api
  baseurl_source: declared
  description: The Accounts API from Acronis — 1 operation(s) for accounts.
  name: Acronis Accounts API
  phrasing_intents:
  - id: GetForgotLink
    intent: Get a password reset link for a login
    question: How do I get a forgot-password link for a user's login?
  phrasing_ops: 1
  slug: acronis-accounts-api
- baseURL: https://{datacenter}.acronis.com/api
  baseurl_source: declared
  description: The Agent Update References API from Acronis — 1 operation(s) for agent update references.
  name: Acronis Agent Update References API
  phrasing_intents:
  - id: FetchAgentUpdateReferenceByAttributes
    intent: Find the agent update package for a platform
    question: Which agent installer package matches my OS and architecture?
  phrasing_ops: 1
  slug: acronis-agent-update-references-api
- baseURL: https://{datacenter}.acronis.com/api
  baseurl_source: declared
  description: The Agent Update Settings API from Acronis — 2 operation(s) for agent update settings.
  name: Acronis Agent Update Settings API
  phrasing_intents:
  - id: UploadAgentUpdateSettings
    intent: Save agent auto-update settings
    question: How do I configure unattended agent updates for my agents?
  - id: DeleteAgentUpdateSettingsCollection
    intent: Delete update settings for several agents
    question: Can I remove the auto-update settings for many agents in one call?
  - id: FetchAgentUpdateSettings
    intent: Get an agent's auto-update settings
    question: What unattended update settings apply to this agent?
  - id: DeleteAgentUpdateSettings
    intent: Delete one agent's update settings
    question: How do I delete the specific update settings of one agent?
  phrasing_ops: 4
  slug: acronis-agent-update-settings-api
- baseURL: https://{datacenter}.acronis.com/api
  baseurl_source: declared
  description: The Alerts API from Acronis — 3 operation(s) for alerts.
  name: Acronis Alerts API
  phrasing_intents:
  - id: CreateAnAlert
    intent: Raise a new alert
    question: How do I create and activate a custom alert?
  - id: FetchAllAlerts
    intent: List alerts
    question: How do I see all active alerts in my tenant?
  - id: DismissTheAlertsByFilter
    intent: Dismiss alerts matching a filter
    question: How do I dismiss every alert of a certain type at once?
  - id: FetchAnAlertByID
    intent: Get one alert
    question: How do I look up a single alert's details by ID?
  - id: DismissAnAlertByID
    intent: Dismiss a single alert
    question: How do I dismiss one specific alert?
  - id: MarkAlertAsFalsePositive
    intent: Mark an alert as a false positive
    question: How do I flag an alert as a false positive?
  phrasing_ops: 6
  slug: acronis-alerts-api
- baseURL: https://{datacenter}.acronis.com/api
  baseurl_source: declared
  description: The Antimalware Scan Stats API from Acronis — 1 operation(s) for antimalware scan stats.
  name: Acronis Antimalware Scan Stats API
  phrasing_intents:
  - id: FetchAntimalwareScanStats
    intent: Get antimalware backup scan counts
    question: How many of my backups have been scanned for malware?
  phrasing_ops: 1
  slug: acronis-antimalware-scan-stats-api
- baseURL: https://{datacenter}.acronis.com/api
  baseurl_source: declared
  description: The Applications API from Acronis — 4 operation(s) for applications.
  name: Acronis Applications API
  phrasing_intents:
  - id: FetchApplications
    intent: List all registered applications
    question: Which applications are registered on the platform?
  - id: FetchApplication
    intent: Get an application's details
    question: How do I look up one application by its ID?
  - id: TurnOnTenantApplication
    intent: Enable an application for a tenant
    question: How do I switch on an application for one of my customer tenants?
  - id: TurnOffTenantApplication
    intent: Disable an application for a tenant
    question: How do I turn off an application for a tenant?
  - id: DeleteTenantApplicationSetting
    intent: Reset a tenant's application setting to inherited
    question: How do I clear a tenant's own setting so it inherits from its parent again?
  - id: UpdateTenantApplicationSetting
    intent: Change an application setting for a tenant
    question: How do I set an application setting for a tenant and stop children overriding it?
  - id: FetchTenantApplicationSetting
    intent: Read an application setting for a tenant
    question: What value does a tenant have for a particular application setting?
  phrasing_ops: 7
  slug: acronis-applications-api
- baseURL: https://{datacenter}.acronis.com/api
  baseurl_source: declared
  description: The Archives API from Acronis — 2 operation(s) for archives.
  name: Acronis Archives API
  phrasing_intents:
  - id: FetchArchives
    intent: List backup archives
    question: How do I list the backup archives for a machine?
  - id: DeleteArchives
    intent: Delete archives for a resource
    question: How do I delete all backup archives of a resource?
  - id: FetchArchiveBackups
    intent: List backups within an archive
    question: What backup points are inside this archive?
  phrasing_ops: 3
  slug: acronis-archives-api
- baseURL: https://{datacenter}.acronis.com/api
  baseurl_source: declared
  description: The Audit Log API from Acronis — 1 operation(s) for audit log.
  name: Acronis Audit Log API
  phrasing_intents:
  - id: GetAuditLogEntriesList
    intent: List audit log entries
    question: Who accessed or changed files in Sync & Share recently?
  phrasing_ops: 1
  slug: acronis-audit-log-api
- baseURL: https://{datacenter}.acronis.com/api
  baseurl_source: declared
  description: The Backed Up Resources API from Acronis — 1 operation(s) for backed up resources.
  name: Acronis Backed Up Resources API
  phrasing_intents:
  - id: FetchBackedUpResources
    intent: List backed-up resources
    question: Which machines and resources have backups stored?
  phrasing_ops: 1
  slug: acronis-backed-up-resources-api
- baseURL: https://{datacenter}.acronis.com/api
  baseurl_source: declared
  description: The Backups API from Acronis — 1 operation(s) for backups.
  name: Acronis Backups API
  phrasing_intents:
  - id: FetchBackups
    intent: List backups across vaults
    question: How do I see all backups for a machine across every vault?
  - id: DeleteBackups
    intent: Delete all backups of a resource
    question: How do I delete every backup containing a particular machine?
  phrasing_ops: 2
  slug: acronis-backups-api
- baseURL: https://{datacenter}.acronis.com/api
  baseurl_source: declared
  description: The Call API from Acronis — 1 operation(s) for call.
  name: Acronis Call API
  phrasing_intents:
  - id: CreateTicket
    intent: Open a support ticket
    question: How do I open a new service desk ticket for a customer?
  - id: FetchTicket
    intent: Get a support ticket
    question: How do I look up a PSA ticket by its ID?
  phrasing_ops: 2
  slug: acronis-call-api
- baseURL: https://{datacenter}.acronis.com/api
  baseurl_source: declared
  description: The Categories API from Acronis — 1 operation(s) for categories.
  name: Acronis Categories API
  phrasing_intents:
  - id: FetchCategories
    intent: List alert categories
    question: What alert categories are enabled?
  phrasing_ops: 1
  slug: acronis-categories-api
- baseURL: https://{datacenter}.acronis.com/api
  baseurl_source: declared
  description: The ContractPart API from Acronis — 1 operation(s) for contractpart.
  name: Acronis Contract Part API
  phrasing_intents:
  - id: CreateOrUpdateAContractPart
    intent: Create or update a contract part
    question: How do I add a billable line to a customer contract?
  - id: FetchContractPart
    intent: Get a contract part
    question: How do I look up the contract part attached to a contract?
  - id: DeleteContractPart
    intent: Delete a contract part
    question: How do I remove a line from a contract?
  phrasing_ops: 3
  slug: acronis-contractpart-api
- baseURL: https://{datacenter}.acronis.com/api
  baseurl_source: declared
  description: The Contracts API from Acronis — 1 operation(s) for contracts.
  name: Acronis Contracts API
  phrasing_intents:
  - id: CreateOrUpdateContract
    intent: Create or update a customer contract
    question: How do I set up a new billing contract for a customer?
  - id: FetchesContractsByCustomerID
    intent: List a customer's contracts
    question: How do I see all the contracts for one customer?
  phrasing_ops: 2
  slug: acronis-contracts-api
- baseURL: https://{datacenter}.acronis.com/api
  baseurl_source: declared
  description: The Count API from Acronis — 1 operation(s) for count.
  name: Acronis Count API
  phrasing_intents:
  - id: FetchAlertCounters
    intent: Count alerts by tenant, type or severity
    question: How many alerts do I have, broken down by severity?
  phrasing_ops: 1
  slug: acronis-count-api
- baseURL: https://{datacenter}.acronis.com/api
  baseurl_source: declared
  description: The Customer Alerts API from Acronis — 1 operation(s) for customer alerts.
  name: Acronis Customer Alerts API
  phrasing_intents:
  - id: FetchAlertsGroupedPerCustomer
    intent: List alerts per customer
    question: How do I see alerts for each of my customer tenants?
  phrasing_ops: 1
  slug: acronis-customer-alerts-api
- baseURL: https://{datacenter}.acronis.com/api
  baseurl_source: declared
  description: The Customer Alerts Count API from Acronis — 1 operation(s) for customer alerts count.
  name: Acronis Customer Alerts Count API
  phrasing_intents:
  - id: FetchPartner'sCustomerAlertsCount
    intent: Count alerts per customer
    question: Which of my customers have open alerts, and how many each?
  phrasing_ops: 1
  slug: acronis-customer-alerts-count-api
- baseURL: https://{datacenter}.acronis.com/api
  baseurl_source: declared
  description: The Devices API from Acronis — 2 operation(s) for devices.
  name: Acronis Devices API
  phrasing_intents:
  - id: GetDevicesList
    intent: List devices
    question: How do I list all devices in a tenant?
  - id: GetDeviceInformation
    intent: Get a device's details
    question: What information is recorded for this device?
  - id: UpdateDevice
    intent: Update a device
    question: How do I change a device's details?
  - id: DeleteDevice
    intent: Delete a device
    question: How do I remove a device?
  phrasing_ops: 4
  slug: acronis-devices-api
- baseURL: https://{datacenter}.acronis.com/api
  baseurl_source: declared
  description: The DownloadInvoice API from Acronis — 1 operation(s) for downloadinvoice.
  name: Acronis Download Invoice API
  phrasing_intents:
  - id: DownloadInvoice
    intent: Download an invoice
    question: How do I download an invoice file?
  phrasing_ops: 1
  slug: acronis-downloadinvoice-api
- baseURL: https://{datacenter}.acronis.com/api
  baseurl_source: declared
  description: The Effective Price Lists API from Acronis — 1 operation(s) for effective price lists.
  name: Acronis Effective Price Lists API
  phrasing_intents:
  - id: FetchTenant'sPriceLists
    intent: Get a tenant's price lists
    question: What prices apply to a tenant in a given month?
  phrasing_ops: 1
  slug: acronis-effective-price-lists-api
- baseURL: https://{datacenter}.acronis.com/api
  baseurl_source: declared
  description: The EmailUpdates API from Acronis — 1 operation(s) for emailupdates.
  name: Acronis Email Updates API
  phrasing_intents:
  - id: FetchEmailAttachment
    intent: Get a ticket email attachment
    question: How do I get an attachment that came in on a ticket email?
  phrasing_ops: 1
  slug: acronis-emailupdates-api
- baseURL: https://{datacenter}.acronis.com/api
  baseurl_source: declared
  description: The Events API from Acronis — 1 operation(s) for events.
  name: Acronis Events API
  phrasing_intents:
  - id: FetchEvents
    intent: Consume a batch of events
    question: How do I read events from my event subscription?
  phrasing_ops: 1
  slug: acronis-events-api
- baseURL: https://{datacenter}.acronis.com/api
  baseurl_source: declared
  description: The ExportInvoice API from Acronis — 1 operation(s) for exportinvoice.
  name: Acronis Export Invoice API
  phrasing_intents:
  - id: ExportInvoices
    intent: Export invoices as XML or CSV
    question: How do I export several invoices to CSV for my accounting system?
  phrasing_ops: 1
  slug: acronis-exportinvoice-api
- baseURL: https://{datacenter}.acronis.com/api
  baseurl_source: declared
  description: The Idp API from Acronis — 9 operation(s) for idp.
  name: Acronis Idp API
  phrasing_intents:
  - id: RequestTokens
    intent: Get an access token
    question: How do I get an access token for the Acronis API with my client credentials?
  - id: RevokeToken
    intent: Revoke an access or refresh token
    question: How do I revoke a token so it can no longer be used?
  - id: IntrospectToken
    intent: Check whether a token is active
    question: How can I tell if an access token is still valid?
  - id: RequestOneTimeToken
    intent: Issue a one-time login token for a user
    question: How do I sign a user into the console from my own portal without their password?
  - id: LogInWithOneTimeToken
    intent: Log in with a one-time token
    question: How do I exchange a one-time token for a platform session cookie?
  - id: Logout
    intent: Log out of the platform
    question: How do I end my current platform session?
  - id: postIdpDeviceAuthorization
    intent: Start a device authorization request
    question: How does a headless device get a user code so someone can sign it in?
  - id: DeviceAuthorizationApproval_0
    intent: Look up a pending device authorization
    question: What device is asking for authorization with this user code?
  phrasing_ops: 10
  slug: acronis-idp-api
- baseURL: https://{datacenter}.acronis.com/api
  baseurl_source: declared
  description: The Incidents API from Acronis — 5 operation(s) for incidents.
  name: Acronis Incidents API
  phrasing_intents:
  - id: getIncidents
    intent: List security incidents for customers
    question: How do I pull all incidents for my customers into my MDR backend?
  - id: postIncidentsInvestigationState
    intent: Update investigation state on many incidents
    question: How do I set the investigation state of several incidents in one call?
  - id: getIncidentsByIncidentId
    intent: Get one incident's details
    question: What detections and activities make up a specific incident?
  - id: postIncidentsByIncidentIdInvestigationState
    intent: Update one incident's investigation state
    question: How do I move a single incident to a new investigation state with a comment?
  - id: postIncidentsByIncidentIdResponseAction
    intent: Run a response action on an incident
    question: How do I isolate a compromised workload from an incident?
  - id: getIncidentsByIncidentIdResponseAction
    intent: Check the status of a response action
    question: Did the isolation action I started on an incident finish?
  phrasing_ops: 6
  slug: acronis-incidents-api
- baseURL: https://{datacenter}.acronis.com/api
  baseurl_source: declared
  description: The Infra API from Acronis — 2 operation(s) for infra.
  name: Acronis Infra API
  phrasing_intents:
  - id: FetchInfrastructuresBatch
    intent: Fetch several infrastructure components
    question: Can I get details of several infrastructure components by UUID at once?
  - id: RegisterInfrastructure
    intent: Register an infrastructure component
    question: How do I register a new storage infrastructure component?
  - id: UnregisterInfrastructure
    intent: Unregister an infrastructure component
    question: How do I unregister an infrastructure component?
  - id: UpdateInfrastructure
    intent: Update an infrastructure component
    question: How do I change the URL or name of an infrastructure component?
  - id: FetchInfrastructure
    intent: Get an infrastructure component
    question: What are the settings of this infrastructure component?
  phrasing_ops: 5
  slug: acronis-infra-api
- baseURL: https://{datacenter}.acronis.com/api
  baseurl_source: declared
  description: The InvoiceOverview API from Acronis — 1 operation(s) for invoiceoverview.
  name: Acronis Invoice Overview API
  phrasing_intents:
  - id: UpdateInvoice
    intent: Update an invoice or confirm its payment
    question: How do I mark an invoice as paid?
  - id: FetchInvoice
    intent: Browse the invoice overview
    question: How do I list a customer's invoices a page at a time?
  phrasing_ops: 2
  slug: acronis-invoiceoverview-api
- baseURL: https://{datacenter}.acronis.com/api
  baseurl_source: declared
  description: The Ledger API from Acronis — 1 operation(s) for ledger.
  name: Acronis Ledger API
  phrasing_intents:
  - id: CreateLedger
    intent: Create a ledger account
    question: How do I add a new ledger account for bookkeeping?
  - id: FetchLedger
    intent: Look up ledger accounts
    question: How do I find the ledger accounts set up in PSA?
  phrasing_ops: 2
  slug: acronis-ledger-api
- baseURL: https://{datacenter}.acronis.com/api
  baseurl_source: declared
  description: The Ledgers API from Acronis — 1 operation(s) for ledgers.
  name: Acronis Ledgers API
  phrasing_intents:
  - id: FetchLedgers
    intent: List ledgers
    question: Which ledgers are set up in my billing?
  phrasing_ops: 1
  slug: acronis-ledgers-api
- baseURL: https://{datacenter}.acronis.com/api
  baseurl_source: declared
  description: The Locations API from Acronis — 3 operation(s) for locations.
  name: Acronis Locations API
  phrasing_intents:
  - id: FetchInfrastructuresLocationsBatch
    intent: Fetch several infrastructure locations
    question: Can I look up several infrastructure locations by UUID at once?
  - id: CreateInfrastructuresLocation
    intent: Create an infrastructure location
    question: How do I add a new data center location for my tenant?
  - id: DeleteInfrastructuresLocation
    intent: Delete an infrastructure location
    question: How do I remove an infrastructure location I no longer use?
  - id: UpdateInfrastructuresLocation
    intent: Rename an infrastructure location
    question: How do I rename an infrastructure location?
  - id: FetchInfrastructuresLocation
    intent: Get an infrastructure location
    question: What are the details of this one infrastructure location?
  - id: FetchLocationInfrastructures
    intent: List infrastructure components at a location
    question: Which infrastructure components are deployed at this location?
  phrasing_ops: 6
  slug: acronis-locations-api
- baseURL: https://{datacenter}.acronis.com/api
  baseurl_source: declared
  description: The Policy Management API from Acronis — 21 operation(s) for policy management.
  name: Acronis Policy Management API
  phrasing_intents:
  - id: FetchAListOfPolicies
    intent: List protection policies
    question: How do I list all the protection policies in a tenant?
  - id: CreateAPolicy
    intent: Create a protection policy
    question: How do I create a new protection policy?
  - id: DeletePolicies
    intent: Delete several policies at once
    question: Can I bulk-delete policies by ID?
  - id: ModifyPoliciesFavoriteOrderAndProperties
    intent: Reorder favorite policies
    question: Can I change the order of my favorite policies?
  - id: FetchAPolicy
    intent: Get a single policy
    question: How do I view a policy's settings by its ID?
  - id: DeleteAPolicy
    intent: Delete one policy
    question: How do I delete a single protection policy?
  - id: UpdateAPolicy
    intent: Update a policy
    question: How do I change the settings of an existing policy?
  - id: postPolicyManagementV4Drafts
    intent: Open a policy draft
    question: How do I start a draft so I can edit a policy composite before committing it?
  phrasing_ops: 28
  slug: acronis-policy-management-api
- baseURL: https://{datacenter}.acronis.com/api
  baseurl_source: declared
  description: The Priorities API from Acronis — 1 operation(s) for priorities.
  name: Acronis Priorities API
  phrasing_intents:
  - id: FetchTicketPriorities
    intent: List ticket priorities
    question: What priority levels can a ticket have?
  phrasing_ops: 1
  slug: acronis-priorities-api
- baseURL: https://{datacenter}.acronis.com/api
  baseurl_source: declared
  description: The Product API from Acronis — 1 operation(s) for product.
  name: Acronis Product API
  phrasing_intents:
  - id: CreateProduct
    intent: Create a product
    question: How do I add a new billable product with a price?
  - id: FetchProducts
    intent: List products
    question: Which products do I have set up for billing?
  phrasing_ops: 2
  slug: acronis-product-api
- baseURL: https://{datacenter}.acronis.com/api
  baseurl_source: declared
  description: The Registration Tokens API from Acronis — 2 operation(s) for registration tokens.
  name: Acronis Registration Tokens API
  phrasing_intents:
  - id: FetchRegistrationTokens_0
    intent: List registration tokens (deprecated)
    question: Where is the older, deprecated endpoint that lists all registration tokens?
  - id: CreateRegistrationToken_0
    intent: Create a registration token (deprecated)
    question: Can I still create a registration token with the older deprecated endpoint?
  - id: DeleteRegistrationToken
    intent: Delete a registration token
    question: How do I revoke an agent registration token so nobody can use it?
  phrasing_ops: 3
  slug: acronis-registration-tokens-api
- baseURL: https://{datacenter}.acronis.com/api
  baseurl_source: declared
  description: The Reports API from Acronis — 4 operation(s) for reports.
  name: Acronis Reports API
  phrasing_intents:
  - id: CreateReport
    intent: Create a usage report
    question: How do I set up a scheduled usage report that emails recipients?
  - id: DeleteReport
    intent: Delete a usage report
    question: How do I delete a usage report I no longer need?
  - id: UpdateReport
    intent: Change a scheduled usage report
    question: How do I change the recipients of a scheduled report?
  - id: FetchReport
    intent: Get a usage report's configuration
    question: How do I see how a usage report is configured?
  - id: FetchStoredReports
    intent: List generated copies of a report
    question: Which past runs of a usage report are stored?
  - id: DownloadStoredReport
    intent: Download a generated report
    question: How do I download the data of a report that already ran?
  phrasing_ops: 6
  slug: acronis-reports-api
- baseURL: https://{datacenter}.acronis.com/api
  baseurl_source: declared
  description: The Resource Management API from Acronis — 6 operation(s) for resource management.
  name: Acronis Resource Management API
  phrasing_intents:
  - id: FetchAListOfAllResources
    intent: List protected resources
    question: How do I list all the machines and workloads registered as resources?
  - id: DeleteResources
    intent: Delete resources
    question: How do I remove resources that an agent no longer reports?
  - id: CreateAResource
    intent: Register a new resource
    question: How do I register a new resource or group for protection?
  - id: PostMultipleResourcesInOneRequestFromASingleAgent
    intent: Submit many resources from one agent
    question: Can an agent report many resources in a single batch request?
  - id: FetchACountOfAllResourcesThatMatchFilterParameters
    intent: Count resources matching filters
    question: How many resources are registered in a tenant?
  - id: FetchAResourceByID
    intent: Get one resource
    question: How do I look up a resource by its internal or external ID?
  - id: FetchAListOfResource'sAttributes
    intent: List a resource's attributes
    question: What attributes are stored for a resource across all namespaces?
  - id: FetchTheProtectionStatusOfResources
    intent: Check resources' protection status
    question: Which of my resources are protected and which are not?
  phrasing_ops: 8
  slug: acronis-resource-management-api
- baseURL: https://{datacenter}.acronis.com/api
  baseurl_source: declared
  description: The Resource Status API from Acronis — 1 operation(s) for resource status.
  name: Acronis Resource Status API
  phrasing_intents:
  - id: FetchResourcesContainingTheHighestSeverityAlerts
    intent: Get resources' worst alert severity
    question: What is the most severe alert on each of my resources?
  phrasing_ops: 1
  slug: acronis-resource-status-api
- baseURL: https://{datacenter}.acronis.com/api
  baseurl_source: declared
  description: The SalesItems API from Acronis — 1 operation(s) for salesitems.
  name: Acronis Sales Items API
  phrasing_intents:
  - id: FetchSalesItems
    intent: List sales items
    question: How do I find sales items for a customer?
  - id: CreateSalesItem
    intent: Create a sales item
    question: How do I record a sale for a customer?
  - id: DeleteSalesItem
    intent: Delete a sales item
    question: How do I delete a sales item that was entered by mistake?
  phrasing_ops: 3
  slug: acronis-salesitems-api
- baseURL: https://{datacenter}.acronis.com/api
  baseurl_source: declared
  description: The SchedulerTickets API from Acronis — 1 operation(s) for schedulertickets.
  name: Acronis Scheduler Tickets API
  phrasing_intents:
  - id: UpdateTicket
    intent: Add an update note to a ticket
    question: How do I add a note to an existing ticket?
  - id: FetchTicketUpdates
    intent: List updates on a scheduled ticket
    question: What updates have been logged on a ticket over a date range?
  phrasing_ops: 2
  slug: acronis-schedulertickets-api
- baseURL: https://{datacenter}.acronis.com/api
  baseurl_source: declared
  description: The Search API from Acronis — 1 operation(s) for search.
  name: Acronis Search API
  phrasing_intents:
  - id: Search
    intent: Search tenants and users
    question: How do I find a tenant or user by name or email?
  phrasing_ops: 1
  slug: acronis-search-api
- baseURL: https://{datacenter}.acronis.com/api
  baseurl_source: declared
  description: The Search Index Size Stats API from Acronis — 1 operation(s) for search index size stats.
  name: Acronis Search Index Size Stats API
  phrasing_intents:
  - id: FetchArchiveSearchIndexSizeStats
    intent: Get archive search index sizes for a tenant
    question: How large are the search indexes for a tenant's archives?
  phrasing_ops: 1
  slug: acronis-search-index-size-stats-api
- baseURL: https://{datacenter}.acronis.com/api
  baseurl_source: declared
  description: The Servers API from Acronis — 5 operation(s) for servers.
  name: Acronis Servers API
  phrasing_intents:
  - id: FetchCloudServers
    intent: List disaster recovery cloud servers
    question: Which cloud servers do I have for disaster recovery?
  - id: FetchCloudServerByUUID
    intent: Get a cloud server
    question: How do I check the details of one cloud server?
  - id: StartProductionFailoverOnCloudServer
    intent: Start a production failover
    question: How do I fail over production to a cloud recovery server?
  - id: StartTestFailoverOnCloudServer
    intent: Start a test failover
    question: How do I run a test failover without affecting production?
  - id: StopFailoverOnCloudServer
    intent: Stop a running failover
    question: How do I stop a failover that is running on a cloud server?
  phrasing_ops: 5
  slug: acronis-servers-api
- baseURL: https://{datacenter}.acronis.com/api
  baseurl_source: declared
  description: The Settings API from Acronis — 5 operation(s) for settings.
  name: Acronis Settings API
  phrasing_intents:
  - id: GetPurgingPoliciesSettings
    intent: Get file purging policy settings
    question: How long are deleted files kept before being purged?
  - id: UpdatePurgingPoliciesSettings
    intent: Change file purging policies
    question: How do I change how long deleted files are retained before purging?
  - id: GetServerSettings
    intent: Get server settings
    question: What are the current server settings?
  - id: UpdateServerSettings
    intent: Change server settings
    question: How do I update the server configuration?
  - id: GetAuditLogSettings
    intent: Get audit log settings
    question: How is audit logging configured?
  - id: UpdateAuditLogSettings
    intent: Change audit log settings
    question: How do I change what the audit log records?
  - id: GetSecuritySettings
    intent: Get security settings
    question: What security settings are in effect?
  - id: UpdateSecuritySettings
    intent: Change security settings
    question: How do I tighten the security settings?
  phrasing_ops: 10
  slug: acronis-settings-api
- baseURL: https://{datacenter}.acronis.com/api
  baseurl_source: declared
  description: The Sites API from Acronis — 2 operation(s) for sites.
  name: Acronis Sites API
  phrasing_intents:
  - id: FetchDisasterRecoverySites
    intent: List disaster recovery sites
    question: Which disaster recovery sites do I have?
  - id: FetchDisasterRecoverySiteByUUID
    intent: Get a disaster recovery site
    question: What are the details of this disaster recovery site?
  phrasing_ops: 2
  slug: acronis-sites-api
- baseURL: https://{datacenter}.acronis.com/api
  baseurl_source: declared
  description: The SLA API from Acronis — 1 operation(s) for sla.
  name: Acronis SLA API
  phrasing_intents:
  - id: FetchServiceLevelAgreements(SLA)
    intent: List service level agreements
    question: What SLAs are defined in PSA?
  phrasing_ops: 1
  slug: acronis-sla-api
- baseURL: https://{datacenter}.acronis.com/api
  baseurl_source: declared
  description: The Stats API from Acronis — 1 operation(s) for stats.
  name: Acronis Stats API
  phrasing_intents:
  - id: GetCountOfActiveAlertsAndLastModificationTime
    intent: Get active alert count and last change
    question: How many active alerts are there right now?
  phrasing_ops: 1
  slug: acronis-stats-api
- baseURL: https://{datacenter}.acronis.com/api
  baseurl_source: declared
  description: The Status API from Acronis — 1 operation(s) for status.
  name: Acronis Status API
  phrasing_intents:
  - id: FetchAlertsGroupedByScope
    intent: Get most critical alerts by scope
    question: What is the most critical alert for each machine or plan?
  phrasing_ops: 1
  slug: acronis-status-api
- baseURL: https://{datacenter}.acronis.com/api
  baseurl_source: declared
  description: The Statuses API from Acronis — 1 operation(s) for statuses.
  name: Acronis Statuses API
  phrasing_intents:
  - id: FetchStatuses
    intent: List statuses
    question: What statuses are available in the service desk?
  phrasing_ops: 1
  slug: acronis-statuses-api
- baseURL: https://{datacenter}.acronis.com/api
  baseurl_source: declared
  description: The Storage Dirs API from Acronis — 2 operation(s) for storage dirs.
  name: Acronis Storage Dirs API
  phrasing_intents:
  - id: FetchStorageFolders
    intent: List top-level folders on a storage
    question: What top-level folders exist on an on-premises storage?
  - id: FetchStorageFoldersInPath
    intent: List folders under a storage path
    question: How do I browse subfolders at a specific path on a storage?
  phrasing_ops: 2
  slug: acronis-storage-dirs-api
- baseURL: https://{datacenter}.acronis.com/api
  baseurl_source: declared
  description: The Storage Nodes API from Acronis — 3 operation(s) for storage nodes.
  name: Acronis Storage Nodes API
  phrasing_intents:
  - id: FetchRegisteredStorageNodes
    intent: List registered storage nodes
    question: Which storage nodes are registered in my on-premises install?
  - id: RegisterStorageNode_1
    intent: Register a storage node
    question: How do I add a new storage node to an on-premises deployment?
  - id: CheckUserAccess
    intent: Test credentials on a storage node
    question: Can a given user account access a storage node?
  - id: FindVaultByPath
    intent: Find a vault by path on a storage node
    question: Is there already a vault at a given path on a storage node?
  phrasing_ops: 4
  slug: acronis-storage-nodes-api
- baseURL: https://{datacenter}.acronis.com/api
  baseurl_source: declared
  description: The Storage Usage Stats API from Acronis — 1 operation(s) for storage usage stats.
  name: Acronis Storage Usage Stats API
  phrasing_intents:
  - id: FetchStorageUsageStats
    intent: Get storage usage per tenant
    question: How much storage is each tenant using?
  phrasing_ops: 1
  slug: acronis-storage-usage-stats-api
- baseURL: https://{datacenter}.acronis.com/api
  baseurl_source: declared
  description: The Subscriptions API from Acronis — 2 operation(s) for subscriptions.
  name: Acronis Subscriptions API
  phrasing_intents:
  - id: CreateEventSubscription
    intent: Subscribe to platform events
    question: How do I subscribe to events on a topic for my tenant tree?
  - id: FetchSubscriptionOffset
    intent: Get a subscription's acknowledged offset
    question: How far has my event subscriber acknowledged events?
  phrasing_ops: 2
  slug: acronis-subscriptions-api
- baseURL: https://{datacenter}.acronis.com/api
  baseurl_source: declared
  description: The Sync And Share Nodes API from Acronis — 14 operation(s) for sync and share nodes.
  name: Acronis Sync And Share Nodes API
  phrasing_intents:
  - id: CreateFolder
    intent: Create a Sync & Share folder
    question: How do I create a new folder in Sync & Share by name or path?
  - id: GetFileOrFolderInformation
    intent: Get details of a file or folder
    question: How do I look up the metadata of a single file or folder?
  - id: UpdateFileOrFolder
    intent: Rename or change a file or folder
    question: How do I rename a file or folder in Sync & Share?
  - id: DeleteFileOrFolder
    intent: Delete a file or folder
    question: How do I delete a file or folder from Sync & Share?
  - id: GetFilesAndFoldersList
    intent: List what's inside a folder
    question: What files and subfolders are inside a given folder?
  - id: GetFileOrFolderRevisionsList
    intent: List revisions of a file or folder
    question: What earlier versions of a file are available?
  - id: RestoreFileRevision
    intent: Restore an earlier file revision
    question: How do I roll a file back to a previous version?
  - id: GetFileOrFolderContents
    intent: Download a file or folder
    question: How do I download a file from Sync & Share?
  phrasing_ops: 21
  slug: acronis-sync-and-share-nodes-api
- baseURL: https://{datacenter}.acronis.com/api
  baseurl_source: declared
  description: The Sync API from Acronis — 11 operation(s) for sync.
  name: Acronis Sync API
  phrasing_intents:
  - id: FetchArchivesSyncInfo
    intent: Get archive sync state for an agent
    question: How do I find which archives an agent still needs to sync to the Vault Manager?
  - id: UpdateArchivesBatch
    intent: Sync a batch of archives to the vault database
    question: Can I add and remove many archive records in one sync call?
  - id: FetchBackupsSyncInfo
    intent: Get backup sync state for an agent
    question: Which backups has an agent synced, and which changed since my last USN?
  - id: UpdateBackupsBatch
    intent: Sync a batch of backups to the vault database
    question: How do I push new, patched and deleted backup records in one sync batch?
  - id: FetchVaultsSyncInfo
    intent: Get vault sync state
    question: Which vaults does a managing agent have registered in the Vault Manager?
  - id: AddVaultsBatch
    intent: Add a batch of vaults
    question: Can I register several vaults with the Vault Manager in one request?
  - id: RegisterOrUpdateVault
    intent: Register or update a single vault
    question: How do I register one vault or update its configuration?
  - id: SoftDeleteVault
    intent: Mark a vault as deleted
    question: How do I remove a vault from the Vault Manager without destroying its data?
  phrasing_ops: 19
  slug: acronis-sync-api
- baseURL: https://{datacenter}.acronis.com/api
  baseurl_source: declared
  description: The Taxes API from Acronis — 1 operation(s) for taxes.
  name: Acronis Taxes API
  phrasing_intents:
  - id: CreateTax
    intent: Create or save a single tax
    question: How do I add a new tax rate to my billing setup?
  - id: CreateTaxes
    intent: Create taxes from a tax object
    question: Is there a POST endpoint for submitting tax definitions?
  - id: FetchTax
    intent: Get a tax rate
    question: How do I look up a tax rate by its ID?
  - id: DeleteTax
    intent: Delete a tax
    question: How do I remove a tax rate I no longer charge?
  phrasing_ops: 4
  slug: acronis-taxes-api
- baseURL: https://{datacenter}.acronis.com/api
  baseurl_source: declared
  description: The Topics API from Acronis — 2 operation(s) for topics.
  name: Acronis Topics API
  phrasing_intents:
  - id: FetchTopics
    intent: List event topics
    question: Which event topics can my client publish or subscribe to?
  - id: FetchTopicOffsets
    intent: Get a topic's stream offset
    question: What is the latest offset in an event topic?
  phrasing_ops: 2
  slug: acronis-topics-api
- baseURL: https://{datacenter}.acronis.com/api
  baseurl_source: declared
  description: The Types API from Acronis — 2 operation(s) for types.
  name: Acronis Types API
  phrasing_intents:
  - id: FetchAllAlertTypes
    intent: List registered alert types
    question: What kinds of alerts are registered for an operating system?
  - id: RegisterNewAlertType
    intent: Register a new alert type
    question: How do I define a new type of alert?
  - id: FetchAnAlertTypeByID
    intent: Get an alert type
    question: How do I see the definition of one alert type?
  - id: UnregisterAnAlertTypeByID
    intent: Unregister an alert type
    question: How do I remove an alert type I no longer need?
  phrasing_ops: 4
  slug: acronis-types-api
- baseURL: https://{datacenter}.acronis.com/api
  baseurl_source: declared
  description: The UploadedFiles API from Acronis — 1 operation(s) for uploadedfiles.
  name: Acronis Uploaded Files API
  phrasing_intents:
  - id: FetchHelpdeskAttachment
    intent: List attachments on a helpdesk ticket
    question: What attachments are on this helpdesk ticket?
  phrasing_ops: 1
  slug: acronis-uploadedfiles-api
- baseURL: https://{datacenter}.acronis.com/api
  baseurl_source: declared
  description: The Vaults API from Acronis — 22 operation(s) for vaults.
  name: Acronis Vaults API
  phrasing_intents:
  - id: FetchVaults
    intent: List backup vaults
    question: How do I see every backup vault registered on a given host?
  - id: CreateOrAttachVault
    intent: Create or attach a backup vault
    question: How do I add a new backup location as a vault?
  - id: RefreshVaults
    intent: Refresh vault contents on agents
    question: How do I make agents rescan my vaults so new archives show up?
  - id: FetchVault
    intent: Get one backup vault
    question: How do I look up the details of a single vault by its ID?
  - id: DeleteVault
    intent: Remove or detach a backup vault
    question: How do I detach a vault I no longer want to back up to?
  - id: FetchVaultArchives
    intent: List archives in a vault
    question: What backup archives are stored in a particular vault?
  - id: DeleteVaultArchives
    intent: Delete archives from a vault
    question: How do I permanently remove whole archives from a vault?
  - id: RefreshVaultArchives
    intent: Refresh specific archives in a vault
    question: How do I rescan just a few archives in a vault instead of the whole vault?
  phrasing_ops: 28
  slug: acronis-vaults-api
- baseURL: https://{datacenter}.acronis.com/api
  baseurl_source: declared
  description: The .well Known API from Acronis — 1 operation(s) for .well known.
  name: Acronis .well Known API
  phrasing_intents:
  - id: FetchOpenIDConfiguration
    intent: Get OpenID Connect discovery document
    question: Where is the OpenID Connect configuration for the platform?
  phrasing_ops: 1
  slug: acronis-well-known-api
- baseURL: https://{datacenter}.acronis.com/api/2
  baseurl_source: declared
  description: The Dashboard Data API from Acronis — 1 operation(s) for dashboard data.
  name: Acronis Dashboard Data API
  phrasing_intents:
  - id: FetchDashboardData
    intent: Get PSA dashboard data
    question: What ticket figures appear on my PSA dashboard?
  phrasing_ops: 1
  slug: acronis-dashboard-data-api
- baseURL: https://{datacenter}.acronis.com/api/2
  baseurl_source: declared
  description: The Health Check API from Acronis — 1 operation(s) for health check.
  name: Acronis Health Check API
  phrasing_intents:
  - id: HealthCheck
    intent: Check service health
    question: Is the service up and responding?
  phrasing_ops: 1
  slug: acronis-health-check-api
artifact_total: 211
asyncapis:
- description: ''
  name: Acronis Events Webhooks
  slug: acronis-events-webhooks
collections:
- collection_type: postman
  name: Acronis Account Management Activities API
  slug: postman-acronis-activities-api
- collection_type: postman
  name: Acronis Account Management Activities Agent Updates API
  slug: postman-acronis-agent-updates-api
- collection_type: postman
  name: Acronis Account Management Activities Agents API
  slug: postman-acronis-agents-api
- collection_type: postman
  name: Acronis Account Management Activities Authentication API
  slug: postman-acronis-authentication-api
- collection_type: postman
  name: Acronis Account Management Activities Clients API
  slug: postman-acronis-clients-api
- collection_type: postman
  name: Acronis Account Management Activities Hardware Nodes API
  slug: postman-acronis-hardware-nodes-api
- collection_type: postman
  name: Acronis Account Management Activities Licensing API
  slug: postman-acronis-licensing-api
- collection_type: postman
  name: Acronis Account Management Activities Tasks API
  slug: postman-acronis-tasks-api
- collection_type: postman
  name: Acronis Account Management Activities Tenants API
  slug: postman-acronis-tenants-api
- collection_type: postman
  name: Acronis Account Management Activities Usage API
  slug: postman-acronis-usage-api
- collection_type: postman
  name: Acronis Account Management Activities Users API
  slug: postman-acronis-users-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Acronis Account Management Activities API
  slug: open-acronis-activities-api
- collection_type: open
  name: Acronis Account Management Activities Agent Updates API
  slug: open-acronis-agent-updates-api
- collection_type: open
  name: Acronis Account Management Activities Agents API
  slug: open-acronis-agents-api
- collection_type: open
  name: Acronis Account Management Activities Authentication API
  slug: open-acronis-authentication-api
- collection_type: open
  name: Acronis Account Management Activities Clients API
  slug: open-acronis-clients-api
- collection_type: open
  name: Acronis Account Management Activities Hardware Nodes API
  slug: open-acronis-hardware-nodes-api
- collection_type: open
  name: Acronis Account Management Activities Licensing API
  slug: open-acronis-licensing-api
- collection_type: open
  name: Acronis Account Management Activities Tasks API
  slug: open-acronis-tasks-api
- collection_type: open
  name: Acronis Account Management Activities Tenants API
  slug: open-acronis-tenants-api
- collection_type: open
  name: Acronis Account Management Activities Usage API
  slug: open-acronis-usage-api
- collection_type: open
  name: Acronis Account Management Activities Users API
  slug: open-acronis-users-api
common:
- group: company
  title: ''
  type: Website
  url: https://www.acronis.com/
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/acronis/overview
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/acronis/refs/heads/main/agentic-access/acronis-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/acronis-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/acronis/refs/heads/main/security/acronis-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/acronis-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/acronis/refs/heads/main/security/acronis-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/acronis-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/acronis/refs/heads/main/authentication/acronis-authentication.yml
  title: ''
  type: Authentication
  url: authentication/acronis-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/acronis
- group: start
  title: ''
  type: Portal
  url: https://developer.acronis.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.acronis.com/doc/outbound/apis/getting-started/index.html
- group: auth
  title: ''
  type: Authentication
  url: https://developer.acronis.com/doc/outbound/apis/authentication/index.html
- group: company
  title: ''
  type: Blog
  url: https://www.acronis.com/en-us/blog/
- group: operate
  title: ''
  type: Support
  url: https://www.acronis.com/en-us/support/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.acronis.com/en-us/products/cloud/cyber-protect/pricing/
- group: company
  title: ''
  type: Partners
  url: https://www.acronis.com/en-us/partners/
- group: other
  title: ''
  type: CaseStudies
  url: https://www.acronis.com/en-us/resource-center/category/case-studies/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/acronis
- group: design
  title: ''
  type: SpectralRules
  url: https://raw.githubusercontent.com/api-evangelist/acronis/refs/heads/main/rules/acronis-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/acronis/refs/heads/main/vocabulary/acronis-vocabulary.yaml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.acronis.com/en-us/legal/
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/acronis/refs/heads/main/changelog/acronis-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/acronis-changelog.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/acronis/refs/heads/main/packages/acronis-packages.yml
  title: ''
  type: Packages
  url: packages/acronis-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/acronis/refs/heads/main/packages/acronis-packages.yml
  title: ''
  type: SDKs
  url: packages/acronis-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/acronis/refs/heads/main/well-known/acronis-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/acronis-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/acronis/refs/heads/main/well-known/acronis-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/acronis-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/acronis/refs/heads/main/mcp/acronis-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/acronis-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/acronis/refs/heads/main/mcp/acronis-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/acronis-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/acronis/refs/heads/main/llms/acronis-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/acronis-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/acronis/refs/heads/main/overlays/acronis-account-management-v2-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/acronis-account-management-v2-overlay.yaml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/acronis/refs/heads/main/conformance/acronis-conformance.yml
  title: ''
  type: Conformance
  url: conformance/acronis-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/acronis/refs/heads/main/conformance/acronis-conformance.yml
  title: ''
  type: Compliance
  url: conformance/acronis-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/acronis/refs/heads/main/errors/acronis-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/acronis-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/acronis/refs/heads/main/lifecycle/acronis-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/acronis-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.acronis.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/acronis/refs/heads/main/scopes/acronis-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/acronis-scopes.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/acronis/refs/heads/main/security/acronis-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/acronis-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/acronis/refs/heads/main/security/acronis-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/acronis-vulnerability-disclosure.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/acronis/refs/heads/main/sandbox/acronis-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/acronis-sandbox.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/acronis/refs/heads/main/conventions/acronis-conventions.yml
  title: ''
  type: Conventions
  url: conventions/acronis-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/acronis/refs/heads/main/conventions/acronis-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/acronis-conventions.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/acronis/refs/heads/main/cli/acronis-cli.yml
  title: ''
  type: CLI
  url: cli/acronis-cli.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/acronis/refs/heads/main/components/acronis-components.yml
  title: ''
  type: Components
  url: components/acronis-components.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/acronis/refs/heads/main/data-model/acronis-data-model.yml
  title: ''
  type: DataModel
  url: data-model/acronis-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/acronis/refs/heads/main/asyncapi/acronis-events-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/acronis-events-webhooks.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/acronis/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: docs
  title: ''
  type: APIReference
  url: https://developer.acronis.com/doc/outbound/apis/index.html
- group: docs
  title: ''
  type: Documentation
  url: https://developer.acronis.com/doc/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.acronis.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.acronis.com/en-us/company/privacy/
- group: start
  title: ''
  type: SignUp
  url: https://www.acronis.com/en-us/my/
- group: start
  title: ''
  type: Login
  url: https://cloud.acronis.com/login
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/kinlaneapi/acronis/overview
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/acronis/refs/heads/main/plans/acronis-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/acronis-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/acronis/refs/heads/main/rate-limits/acronis-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/acronis-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/acronis/refs/heads/main/finops/acronis-finops.yml
  title: ''
  type: FinOps
  url: finops/acronis-finops.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://dl.acronis.com/u/baas/rn/API_change_log/en-US/AcronisCyberCloud_API_change_log.pdf
created: '2025-02-17'
description: Acronis is a leading provider of cyber protection solutions that deliver innovative technology to protect data, applications, and systems from the ever-evolving threats of today's digital world. They offer a comprehensive suite of products, including backup and disaster recovery solutions, file sync and share services, and anti-malware protection.
examples:
- key_count: 6
  name: Account Management Client Example
  slug: account-management-client-example
- key_count: 7
  name: Account Management Contact Example
  slug: account-management-contact-example
- key_count: 5
  name: Account Management Offering Item Example
  slug: account-management-offering-item-example
- key_count: 3
  name: Account Management Quota Example
  slug: account-management-quota-example
- key_count: 3
  name: Account Management Report Example
  slug: account-management-report-example
- key_count: 2
  name: Account Management Search Results Example
  slug: account-management-search-results-example
- key_count: 10
  name: Account Management Tenant Example
  slug: account-management-tenant-example
- key_count: 5
  name: Account Management Token Response Example
  slug: account-management-token-response-example
- key_count: 4
  name: Account Management Usage Item Example
  slug: account-management-usage-item-example
- key_count: 8
  name: Account Management User Example
  slug: account-management-user-example
- key_count: 6
  name: Acronis Createtenant Example
  slug: acronis-createtenant-example
- key_count: 6
  name: Acronis Getagent Example
  slug: acronis-getagent-example
- key_count: 6
  name: Acronis Gettask Example
  slug: acronis-gettask-example
- key_count: 6
  name: Acronis Listagents Example
  slug: acronis-listagents-example
- key_count: 6
  name: Acronis Listtasks Example
  slug: acronis-listtasks-example
- key_count: 6
  name: Acronis Listtenants Example
  slug: acronis-listtenants-example
- key_count: 8
  name: Agent Management Agent Example
  slug: agent-management-agent-example
- key_count: 4
  name: Agent Management Agent O S Example
  slug: agent-management-agent-o-s-example
- key_count: 3
  name: Agent Management Agent Update Settings Example
  slug: agent-management-agent-update-settings-example
- key_count: 5
  name: Agent Management Hardware Node Example
  slug: agent-management-hardware-node-example
- key_count: 10
  name: Task Manager Activity Example
  slug: task-manager-activity-example
- key_count: 14
  name: Task Manager Task Example
  slug: task-manager-task-example
features:
- description: Multi-tier tenant management for MSPs, partners, and customers with offering item quotas.
  name: Tenant Hierarchy Management
- description: Remote management of Acronis backup agents across Windows, Linux, macOS, and cloud workloads.
  name: Agent Management
- description: Real-time monitoring of backup and protection tasks with state, result, and activity tracking.
  name: Backup Task Monitoring
- description: Automated usage metrics collection and report generation for billing and capacity planning.
  name: Usage Reporting
- description: Programmatic creation and application of protection policies to resources.
  name: Policy Management
- description: Automated failover and recovery orchestration for business continuity.
  name: Disaster Recovery API
- description: EDR capabilities for threat detection, investigation, and response via API.
  name: Endpoint Detection and Response
finops:
- name: Acronis Finops
  service_category: Cyber Protection / Backup / Endpoint Security
  slug: acronis-finops
image: /assets/icons/acronis.png
integrations:
- description: Integration with ConnectWise, Autotask, and other PSA platforms for MSP billing and ticketing.
  name: PSA Platforms
- description: Event streaming to SIEM platforms via Event Manager API for security monitoring.
  name: SIEM Systems
- description: Integration with RMM platforms for agent deployment and backup policy management.
  name: RMM Tools
- description: Usage data export for automated billing via usage and offering item APIs.
  name: Billing Systems
json_schemas:
- name: Client
  property_count: 6
  slug: account-management-client
- name: Contact
  property_count: 7
  slug: account-management-contact
- name: OfferingItem
  property_count: 5
  slug: account-management-offering-item
- name: Quota
  property_count: 3
  slug: account-management-quota
- name: Report
  property_count: 3
  slug: account-management-report
- name: SearchResults
  property_count: 2
  slug: account-management-search-results
- name: Tenant
  property_count: 10
  slug: account-management-tenant
- name: TokenResponse
  property_count: 5
  slug: account-management-token-response
- name: UsageItem
  property_count: 4
  slug: account-management-usage-item
- name: User
  property_count: 8
  slug: account-management-user
- name: Activity
  property_count: 10
  slug: acronis-activity
- name: ActivityList
  property_count: 2
  slug: acronis-activitylist
- name: Agent
  property_count: 8
  slug: acronis-agent
- name: AgentList
  property_count: 2
  slug: acronis-agentlist
- name: AgentOS
  property_count: 4
  slug: acronis-agentos
- name: AgentUpdateSettings
  property_count: 3
  slug: acronis-agentupdatesettings
- name: Client
  property_count: 6
  slug: acronis-client
- name: ClientList
  property_count: 1
  slug: acronis-clientlist
- name: ClientRequest
  property_count: 3
  slug: acronis-clientrequest
- name: Contact
  property_count: 7
  slug: acronis-contact
- name: Error
  property_count: 3
  slug: acronis-error
- name: HardwareNode
  property_count: 5
  slug: acronis-hardwarenode
- name: HardwareNodeList
  property_count: 1
  slug: acronis-hardwarenodelist
- name: MaintenanceWindow
  property_count: 3
  slug: acronis-maintenancewindow
- name: OfferingItem
  property_count: 5
  slug: acronis-offeringitem
- name: OfferingItemList
  property_count: 1
  slug: acronis-offeringitemlist
- name: OfferingItemUpdateRequest
  property_count: 1
  slug: acronis-offeringitemupdaterequest
- name: Paging
  property_count: 1
  slug: acronis-paging
- name: Quota
  property_count: 3
  slug: acronis-quota
- name: Report
  property_count: 3
  slug: acronis-report
- name: ReportRequest
  property_count: 2
  slug: acronis-reportrequest
- name: SearchResults
  property_count: 2
  slug: acronis-searchresults
- name: Task
  property_count: 14
  slug: acronis-task
- name: TaskList
  property_count: 2
  slug: acronis-tasklist
- name: Tenant
  property_count: 10
  slug: acronis-tenant
- name: TenantList
  property_count: 2
  slug: acronis-tenantlist
- name: TenantRequest
  property_count: 5
  slug: acronis-tenantrequest
- name: TokenResponse
  property_count: 5
  slug: acronis-tokenresponse
- name: UsageItem
  property_count: 4
  slug: acronis-usageitem
- name: UsageList
  property_count: 1
  slug: acronis-usagelist
- name: User
  property_count: 8
  slug: acronis-user
- name: UserList
  property_count: 2
  slug: acronis-userlist
- name: AgentOS
  property_count: 4
  slug: agent-management-agent-o-s
- name: Agent
  property_count: 8
  slug: agent-management-agent
- name: AgentUpdateSettings
  property_count: 3
  slug: agent-management-agent-update-settings
- name: HardwareNode
  property_count: 5
  slug: agent-management-hardware-node
- name: Activity
  property_count: 10
  slug: task-manager-activity
- name: Task
  property_count: 14
  slug: task-manager-task
json_structures:
- name: Account Management Client Structure
  property_count: 6
  slug: account-management-client-structure
- name: Account Management Contact Structure
  property_count: 7
  slug: account-management-contact-structure
- name: Account Management Offering Item Structure
  property_count: 5
  slug: account-management-offering-item-structure
- name: Account Management Quota Structure
  property_count: 3
  slug: account-management-quota-structure
- name: Account Management Report Structure
  property_count: 3
  slug: account-management-report-structure
- name: Account Management Search Results Structure
  property_count: 2
  slug: account-management-search-results-structure
- name: Account Management Tenant Structure
  property_count: 10
  slug: account-management-tenant-structure
- name: Account Management Token Response Structure
  property_count: 5
  slug: account-management-token-response-structure
- name: Account Management Usage Item Structure
  property_count: 4
  slug: account-management-usage-item-structure
- name: Account Management User Structure
  property_count: 8
  slug: account-management-user-structure
- name: Acronis Structure
  property_count: 0
  slug: acronis-structure
- name: Agent Management Agent O S Structure
  property_count: 4
  slug: agent-management-agent-o-s-structure
- name: Agent Management Agent Structure
  property_count: 8
  slug: agent-management-agent-structure
- name: Agent Management Agent Update Settings Structure
  property_count: 3
  slug: agent-management-agent-update-settings-structure
- name: Agent Management Hardware Node Structure
  property_count: 5
  slug: agent-management-hardware-node-structure
- name: Task Manager Activity Structure
  property_count: 10
  slug: task-manager-activity-structure
- name: Task Manager Task Structure
  property_count: 14
  slug: task-manager-task-structure
jsonld:
- class_count: 18
  name: Acronis Context
  property_count: 61
  slug: acronis-context
layout: provider
mcp_servers:
- description: Provides Acronis Cyber Protect Cloud platform APIs as MCP tools — tenant and user provisioning, service and quota management, backup policy configuration, resource protection, agent management, and mo
  name: Acronis API MCP
  slug: acronis-api-mcp
modified: '2026-08-30'
name: Acronis
nav: Providers
network: true
overview: 'Acronis publishes 71 APIs on the [APIs.io](https://apis.io/) network, including Activities API, Agent Updates API, Agents API, and 68 more. Tagged areas include Cybersecurity, Data Protection, Endpoint Management, Backup and Recovery, and Disaster Recovery.


  The Acronis catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 2 Spectral governance rulesets.


  Acronis'' developer surface includes authentication, developer portal, getting-started guide, engineering blog, support, pricing, changelog, and 48 more developer resources.'
plans:
- name: Acronis Plans Pricing
  plan_count: 4
  slug: acronis-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 5
  name: Acronis Rate Limits
  slug: acronis-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Acronis API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: acronis-jsonschema-spectral-rules
- effective_rule_count: 79
  extends:
  - spectral:oas
  name: Acronis API Rules
  rule_count: 38
  severity_counts:
    error: 15
    hint: 0
    info: 7
    warn: 16
  slug: acronis-spectral-rules
scopes:
- name: Acronis Scopes
  scope_count: 0
  slug: acronis-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: exemplar
  composite: 84.4
  coverage:
    artifact_dirs: 35
    catalog_earned: 87.0
    catalog_earned_first_party: 24.0
    catalog_gap: 28.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.5
  facets:
    access_clarity: 100.0
    contract_governance: 45.5
    contract_quality: 61.5
    developer_ergonomics: 86.3
    discoverability: 76.7
    operational_transparency: 76.3
  previous_composite: 83.9
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 4
      marker_coverage: 5.4
      total: 74
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 45.1
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  trend: flat
  upsert:
    applies: true
    score: 50.0
screenshot: https://raw.githubusercontent.com/api-evangelist/acronis/refs/heads/main/screenshots/acronis-2026-06-20T164007.png
security:
- kind: authentication
  name: Acronis Authentication
  slug: acronis-authentication
  summary_line: oauth2/openIdConnect/http · 4 schemes
- kind: domain-security
  name: Acronis Domain Security
  slug: acronis-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Acronis Vulnerability Disclosure
  slug: acronis-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Acronis Trust Center
  slug: acronis-trust-center
  summary_line: ISO/IEC 27001:2022, ISO/IEC 27017:2015, ISO/IEC 27018:2019, ISO 9001, SOC 2, PCI DSS, IEC 62443-4-1, IT-Grundschutz, Cyber Essentials, ENS, Cloud Italia, FIPS 140-2, UAE IAR, HIPAA, PHIPA, HDS, NEN 7510, 2G3M, EU-US Data Privacy Framework, CSA STAR Level 1
slug: acronis
tags:
- Cybersecurity
- Data Protection
- Endpoint Management
- Backup and Recovery
- Disaster Recovery
- Managed Service Providers
- Endpoint Detection and Response
- Cloud Storage
use_cases:
- description: Automate tenant provisioning, licensing management, and usage reporting for managed service providers.
  name: MSP Platform Automation
- description: Build custom dashboards tracking backup task status, failures, and completion rates.
  name: Backup Monitoring Dashboard
- description: Monitor agent online status, version compliance, and update management across endpoints.
  name: Agent Health Monitoring
- description: Generate automated reports on data protection status for compliance and audit requirements.
  name: Compliance Reporting
- description: Trigger and monitor DR failover workflows programmatically for RTO/RPO compliance.
  name: Disaster Recovery Automation
website: https://www.acronis.com/
---
