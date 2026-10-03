---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
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
  schema_version: '0.2'
  score: 39.2
  scored_at: '2026-10-03'
agentic_access:
- acting_count: 250
  human_in_the_loop: 29
  name: Tenable Agentic Access
  operation_count: 553
  slug: tenable-agentic-access
  summary_line: 553 operations · 250 acting · 29 human-in-the-loop
api_count: 8
apis:
- baseURL: https://cloud.tenable.com
  baseurl_source: declared
  description: Provide general information on Eridanis
  name: Tenable About API
  phrasing_intents:
  - id: getApiAbout
    intent: Get version info about the instance
    question: What version of Identity Exposure is this instance running?
  phrasing_ops: 1
  slug: tenable-about-api
- baseURL: https://cloud.tenable.com
  baseurl_source: declared
  description: The Access Control (API) API from Tenable — 1 operation(s) for access control (api).
  name: Tenable Access Control (API) API
  phrasing_intents:
  - id: vm-api-security-settings-list
    intent: List IP addresses allowed to use the API
    question: Which IP addresses are allowed to call my Tenable Vulnerability Management API?
  - id: vm-api-security-settings-update
    intent: Update the API IP allowlist
    question: How do I restrict API access to my office IP ranges?
  phrasing_ops: 2
  slug: tenable-access-control-api-api
- baseURL: https://cloud.tenable.com
  baseurl_source: declared
  description: The Access Control (Groups) API from Tenable — 4 operation(s) for access control (groups).
  name: Tenable Access Control (Groups) API
  phrasing_intents:
  - id: groups-create
    intent: Create a user group
    question: How do I create a new user group?
  - id: groups-list
    intent: List user groups
    question: What user groups exist in my Tenable container?
  - id: groups-edit
    intent: Rename or update a user group
    question: Can I rename an existing user group?
  - id: groups-delete
    intent: Delete a user group
    question: Why can't I delete a user group that still has members?
  - id: groups-list-users
    intent: List users in a group
    question: Who are the members of a particular user group?
  - id: groups-add-user
    intent: Add a user to a group
    question: How do I add someone to a user group?
  - id: groups-delete-user
    intent: Remove a user from a group
    question: How do I take a user out of a group without deleting the user?
  phrasing_ops: 7
  slug: tenable-access-control-groups-api
- baseURL: https://cloud.tenable.com
  baseurl_source: declared
  description: The Access Control (Permissions) API from Tenable — 5 operation(s) for access control (permissions).
  name: Tenable Access Control (Permissions) API
  phrasing_intents:
  - id: io-v3-access-control-permission-create
    intent: Create an access control permission
    question: How do I grant a user group the ability to scan a set of tagged assets?
  - id: io-v3-access-control-permissions-list
    intent: List all access control permissions
    question: What access control permissions are defined in my container?
  - id: io-v3-access-control-permissions-details
    intent: Get details of a permission
    question: Who does a specific permission apply to and what does it allow?
  - id: io-v3-access-control-permission-update
    intent: Overwrite an existing permission
    question: Do I have to send every field when I edit a permission?
  - id: io-v3-access-control-permission-delete
    intent: Delete a permission
    question: Can I revoke an access control permission entirely?
  - id: io-v3-access-control-permissions-user-list
    intent: List a user's permissions
    question: What permissions has a particular user been granted?
  - id: io-v3-access-control-permissions-user-group-list
    intent: List a user group's permissions
    question: What can members of a given user group access?
  - id: io-v3-access-control-permissions-current-user-list
    intent: Get my own permissions
    question: What am I personally allowed to see and scan?
  phrasing_ops: 8
  slug: tenable-access-control-permissions-api
- baseURL: https://cloud.tenable.com
  baseurl_source: declared
  description: The Access Control (Roles) API from Tenable — 3 operation(s) for access control (roles).
  name: Tenable Access Control (Roles) API
  phrasing_intents:
  - id: access-control-roles-create
    intent: Create a custom role
    question: How do I create a custom role with a specific set of privileges?
  - id: access-control-roles-list
    intent: List standard and custom roles
    question: What roles, standard and custom, are defined in my instance?
  - id: access-control-roles-details
    intent: Get a role's details
    question: Which privileges does a particular role grant?
  - id: access-control-roles-update
    intent: Update a custom role
    question: How do I add or remove privileges on an existing custom role?
  - id: access-control-roles-delete
    intent: Delete a custom role
    question: How do I delete a custom role we no longer need?
  - id: access-control-roles-list-permissions
    intent: List available role permission strings
    question: What privilege strings can I use when building a custom role?
  phrasing_ops: 6
  slug: tenable-access-control-roles-api
- baseURL: https://cloud.tenable.com
  baseurl_source: declared
  description: The Access Control (Users) API from Tenable — 10 operation(s) for access control (users).
  name: Tenable Access Control (Users) API
  phrasing_intents:
  - id: users-create
    intent: Create a user account
    question: How do I add a new person as a user with a username and password?
  - id: users-list
    intent: List users in the workspace
    question: Who has a user account in my Tenable Vulnerability Management instance?
  - id: users-details
    intent: Get a user's account details
    question: What account details are stored for one specific user?
  - id: users-edit
    intent: Update a user's profile and permissions
    question: How do I change an existing user's display name or email address?
  - id: users-delete
    intent: Delete a user account
    question: How do I permanently remove a user from the workspace?
  - id: access-control-users-role-list
    intent: Get the role assigned to a user
    question: Which role is currently assigned to a given user?
  - id: access-control-users-role-update
    intent: Change a user's role
    question: How do I move a user onto a different custom role?
  - id: users-password
    intent: Reset a user's password
    question: How do I reset a locked-out user's password?
  phrasing_ops: 15
  slug: tenable-access-control-users-api
- baseURL: https://cloud.tenable.com
  baseurl_source: declared
  description: The Access Groups v1 API from Tenable — 4 operation(s) for access groups v1.
  name: Tenable Access Groups v1 API
  phrasing_intents:
  - id: io-v1-access-groups-create
    intent: Create a legacy access group
    question: Can I still create an access group even though they are deprecated?
  - id: io-v1-access-groups-list
    intent: List legacy access groups
    question: Which legacy access groups still exist in my container?
  - id: io-v1-access-groups-edit
    intent: Overwrite a legacy access group
    question: Does editing a legacy access group overwrite all of its existing data?
  - id: io-v1-access-groups-delete
    intent: Delete a legacy access group
    question: Can I delete a legacy access group after migrating to access control?
  - id: io-v1-access-groups-details
    intent: Get a legacy access group's details
    question: What rules and users are in a particular legacy access group?
  - id: io-v1-access-groups-list-filters
    intent: List filters for searching access groups
    question: What filters can I use when listing legacy access groups?
  - id: io-v1-access-groups-list-rule-filters
    intent: List filters for access group asset rules
    question: What asset attributes can a legacy access group rule match on?
  phrasing_ops: 7
  slug: tenable-access-groups-v1-api
- baseURL: https://cloud.tenable.com
  baseurl_source: declared
  description: The Access Groups v2 API from Tenable — 4 operation(s) for access groups v2.
  name: Tenable Access Groups v2 API
  phrasing_intents:
  - id: io-v2-access-groups-create
    intent: Create an access group (deprecated)
    question: How do I create an access group that limits which assets users can see?
  - id: io-v2-access-groups-list
    intent: List access groups (deprecated)
    question: Which legacy access groups are still defined in my account?
  - id: io-v2-access-groups-edit
    intent: Update an access group (deprecated)
    question: Does updating an access group overwrite its existing rules?
  - id: io-v2-access-groups-delete
    intent: Delete an access group
    question: How do I delete an old access group?
  - id: io-v2-access-groups-details
    intent: Get an access group's details
    question: What rules and principals are in a particular access group?
  - id: io-v2-access-groups-list-filters
    intent: List filters for access groups
    question: Which filters can I use when listing access groups?
  - id: io-v2-access-groups-list-rule-filters
    intent: List filters for access group asset rules
    question: What asset attributes can an access group rule match on?
  phrasing_ops: 7
  slug: tenable-access-groups-v2-api
- baseURL: https://cloud.tenable.com
  baseurl_source: declared
  description: The Tenable Managed Security Service Provider (MSSP) Portal API provides a secure and accessible way for MSSP administrators to manage and maintain multiple customer instances of Tenable products. The
  name: Tenable Account Groups API
  phrasing_intents:
  - id: mssp-account-groups-create
    intent: Create an account group
    question: How do I group several customer accounts together?
  - id: mssp-account-groups-list
    intent: List MSSP account groups
    question: What account groups have I set up to organize my customer accounts?
  - id: mssp-account-groups-details-list
    intent: Get an account group's details
    question: Which customer accounts are in a specific account group?
  - id: mssp-account-groups-update
    intent: Update an account group
    question: Can I change which customer accounts belong to an account group?
  - id: mssp-account-groups-delete
    intent: Delete an account group
    question: Can I delete an account group I no longer need?
  phrasing_ops: 5
  slug: tenable-account-groups-api
- baseURL: https://cloud.tenable.com
  baseurl_source: declared
  description: The Tenable Managed Security Service Provider (MSSP) Portal API provides a secure and accessible way for MSSP administrators to manage and maintain multiple customer instances of Tenable products. Acc
  name: Tenable Accounts API
  phrasing_intents:
  - id: io-mssp-accounts-eval
    intent: Create an evaluation account (deprecated v1)
    question: Can I still spin up a trial customer account with just an email and country using the old v1 endpoint?
  - id: mssp-accounts-eval-v2
    intent: Create an evaluation account (v2)
    question: How do I create a trial account for a new MSSP customer with specific licensed apps?
  - id: mssp-accounts-quote
    intent: Create a quote for a customer
    question: Can I generate a quote for a new MSSP customer through the API?
  - id: io-mssp-accounts-list
    intent: List MSSP child accounts
    question: Which customer child accounts do I manage in the MSSP Portal?
  - id: io-mssp-accounts-details
    intent: Get a child account's details
    question: What license information does a specific customer child account have?
  - id: io-mssp-accounts-domains-list
    intent: List domains of a child account
    question: Which domains are registered to a given customer child account?
  phrasing_ops: 6
  slug: tenable-accounts-api
- baseURL: https://cloud.tenable.com
  baseurl_source: declared
  description: The Activity Log API from Tenable — 1 operation(s) for activity log.
  name: Tenable Activity Log API
  phrasing_intents:
  - id: audit-log-events
    intent: List activity log events
    question: Who did what in our Tenable Vulnerability Management account?
  phrasing_ops: 1
  slug: tenable-activity-log-api
- baseURL: https://cloud.tenable.com
  baseurl_source: declared
  description: Representation of an Active Directory Object
  name: Tenable AD object API
  phrasing_intents:
  - id: getApiAdObjects
    intent: List every AD object's latest state
    question: Can I pull the last known state of every Active Directory object at once?
  - id: getApiDirectoriesByDirectoryIdAdObjectsById
    intent: Get an AD object in a directory
    question: How do I look up one AD object by id within a directory?
  - id: getApiInfrastructuresByInfrastructureIdDirectoriesByDirectoryIdAdObjectsById
    intent: Get an AD object within a forest's directory
    question: Can I fetch an AD object by id when I know its forest and domain?
  - id: getApiProfilesByProfileIdCheckersByCheckerIdAdObjectsById
    intent: Get a deviant AD object for a checker
    question: How do I see why one AD object fails a specific indicator of exposure?
  - id: getApiInfrastructuresByInfrastructureIdDirectoriesByDirectoryIdEventsByEventIdAdObjectsById
    intent: Get an AD object as of an event
    question: Can I see what an AD object looked like at the time of a particular event?
  - id: getApiInfrastructuresByInfrastructureIdDirectoriesByDirectoryIdEventsByEventIdAdObjectsByIdChanges
    intent: See what changed on an AD object in an event
    question: Which attributes changed on an AD object between an event and the one before it?
  - id: postApiProfilesByProfileIdCheckersByCheckerIdAdObjectsSearch
    intent: Search AD objects deviant for a checker
    question: Can I search which AD objects have deviances for one checker within a date range?
  phrasing_ops: 7
  slug: tenable-ad-object-api
- baseURL: https://cloud.tenable.com
  baseurl_source: declared
  description: The Agent Config API from Tenable — 1 operation(s) for agent config.
  name: Tenable Agent Config API
  phrasing_intents:
  - id: agent-config-details
    intent: Get global agent settings
    question: Are agent software updates and auto-unlinking turned on?
  - id: agent-config-edit
    intent: Update global agent settings
    question: How do I turn on automatic unlinking of inactive agents?
  phrasing_ops: 2
  slug: tenable-agent-config-api
- baseURL: https://cloud.tenable.com
  baseurl_source: declared
  description: The Agent Exclusions API from Tenable — 2 operation(s) for agent exclusions.
  name: Tenable Agent Exclusions API
  phrasing_intents:
  - id: agent-exclusions-create
    intent: Create an agent exclusion window
    question: How do I stop agents from scanning during a maintenance window?
  - id: agent-exclusions-list
    intent: List agent exclusions
    question: Which blackout windows are set to stop agents from scanning?
  - id: agent-exclusions-details
    intent: Get an agent exclusion's details
    question: What schedule does a specific agent exclusion follow?
  - id: agent-exclusions-edit
    intent: Update an agent exclusion
    question: How do I change the timing of an existing agent blackout window?
  - id: agent-exclusions-delete
    intent: Delete an agent exclusion
    question: How do I delete an agent blackout window?
  phrasing_ops: 5
  slug: tenable-agent-exclusions-api
- baseURL: https://cloud.tenable.com
  baseurl_source: declared
  description: The Agent Groups API from Tenable — 3 operation(s) for agent groups.
  name: Tenable Agent Groups API
  phrasing_intents:
  - id: agent-groups-create
    intent: Create an agent group
    question: How do I create a new group to organize agents?
  - id: agent-groups-list
    intent: List agent groups
    question: Which agent groups have been set up?
  - id: agent-groups-details
    intent: Get an agent group with its agents
    question: What are the details of an agent group, including its member agents?
  - id: agent-groups-configure
    intent: Rename an agent group
    question: How do I rename an agent group?
  - id: agent-groups-delete
    intent: Delete an agent group
    question: How do I delete an agent group?
  - id: agent-groups-add-agent
    intent: Add an agent to a group
    question: How do I put a single agent into an agent group?
  - id: agent-groups-delete-agent
    intent: Remove an agent from a group
    question: How do I take an agent out of a group without unlinking it?
  phrasing_ops: 7
  slug: tenable-agent-groups-api
- baseURL: https://cloud.tenable.com
  baseurl_source: declared
  description: The Agent Tasks API from Tenable — 10 operation(s) for agent tasks.
  name: Tenable Agent Tasks API
  phrasing_intents:
  - id: bulk-task-agent-status
    intent: Check status of a bulk agent task
    question: Has my asynchronous bulk agent task finished yet?
  - id: bulk-task-agent-group-status
    intent: Check status of a bulk agent group task
    question: Is the bulk add or remove I started on an agent group done?
  - id: bulk-add-agents
    intent: Add agents to an agent group in bulk
    question: How do I add many agents to an agent group at once?
  - id: bulk-remove-agents
    intent: Remove agents from an agent group in bulk
    question: Can I pull a batch of agents out of an agent group in one request?
  - id: io-agent-bulk-operations-add-to-network
    intent: Move agents into a custom network
    question: How do I assign a set of agents to a custom network?
  - id: io-agent-bulk-operations-remove-from-network
    intent: Remove agents from a custom network
    question: Where do agents go when I take them out of a custom network?
  - id: agent-bulk-operations-profile
    intent: Assign or remove agents from a profile
    question: Can I assign a batch of agents to an agent profile?
  - id: io-agent-bulk-operations-directive
    intent: Send restart or settings instructions to agents
    question: Can I tell a set of agents to restart remotely?
  phrasing_ops: 10
  slug: tenable-agent-tasks-api
- baseURL: https://cloud.tenable.com
  baseurl_source: declared
  description: The Agents API from Tenable — 4 operation(s) for agents.
  name: Tenable Agents API
  phrasing_intents:
  - id: agents-list
    intent: List linked agents
    question: Which Nessus agents are linked to my account?
  - id: agent-group-list-agents
    intent: List the agents in a group
    question: Which agents belong to a specific agent group?
  - id: agents-get-safe-mode-summary
    intent: Summarize agents in safe mode
    question: How many of my agents are running in safe mode?
  - id: agents-get
    intent: Get an agent's details
    question: What platform, version and status does a particular agent report?
  - id: io-agents-rename
    intent: Rename an agent
    question: Can I give an agent a friendlier name?
  - id: agents-delete
    intent: Unlink an agent
    question: How do I unlink an agent from my account?
  phrasing_ops: 6
  slug: tenable-agents-api
- baseURL: https://cloud.tenable.com
  baseurl_source: declared
  description: New deviances alert
  name: Tenable Alert API
  phrasing_intents:
  - id: getApiAlertsById
    intent: Get an alert
    question: How do I open the details of a single alert?
  - id: patchApiAlertsById
    intent: Mark one alert read or archived
    question: Can I mark just one alert as read?
  - id: getApiProfilesByProfileIdAlerts
    intent: List alerts for a profile
    question: What alerts are open for my security profile?
  - id: patchApiProfilesByProfileIdAlerts
    intent: Bulk-mark a profile's alerts
    question: How do I mark every alert in a profile as read at once?
  phrasing_ops: 4
  slug: tenable-alert-api
- baseURL: https://cloud.tenable.com
  baseurl_source: declared
  description: Token to programmatically access Eridanis
  name: Tenable API key API
  phrasing_intents:
  - id: getApiApiKey
    intent: Show my current API key
    question: Where can I see the API key assigned to my user?
  - id: postApiApiKey
    intent: Create or renew my API key
    question: How do I rotate my Identity Exposure API key?
  phrasing_ops: 2
  slug: tenable-api-key-api
- baseURL: https://cloud.tenable.com
  baseurl_source: declared
  description: Tenable.ad global configuration
  name: Tenable Application setting API
  phrasing_intents:
  - id: getApiApplicationSettings
    intent: View application settings
    question: What SMTP server and activity log retention are configured?
  - id: patchApiApplicationSettings
    intent: Change application settings
    question: How do I point Identity Exposure at a different SMTP server?
  phrasing_ops: 2
  slug: tenable-application-setting-api
- baseURL: https://cloud.tenable.com
  baseurl_source: declared
  description: With the WAS Applications API, you can create web application assets. For more information, see the [Targets](https://docs.tenable.com/web-app-scanning/Content/WAS/Scans/BasicSettings.htm#Targets) sec
  name: Tenable Applications API
  phrasing_intents:
  - id: was-v2-add-application
    intent: Add a web application asset
    question: Can I manually define a web application target by FQDN, port, protocol and path?
  phrasing_ops: 1
  slug: tenable-applications-api
- baseURL: https://cloud.tenable.com
  baseurl_source: declared
  description: The Asset Attributes API from Tenable — 4 operation(s) for asset attributes.
  name: Tenable Asset Attributes API
  phrasing_intents:
  - id: io-v3-asset-attributes-create
    intent: Create custom asset attributes
    question: How do I define a new custom attribute like owner or cost center for assets?
  - id: io-v3-asset-attributes-list
    intent: List custom asset attributes
    question: What custom asset attributes are defined in my container?
  - id: io-v3-asset-attributes-update
    intent: Update a custom attribute's description
    question: Can I change the description of a custom asset attribute definition?
  - id: io-v3-asset-attributes-delete
    intent: Delete a custom attribute definition
    question: Does deleting a custom attribute definition remove it from all assets?
  - id: io-v3-asset-attributes-assign
    intent: Assign several custom attributes to an asset
    question: Can I set several custom attribute values on an asset in one request?
  - id: io-v3-asset-attributes-assigned-list
    intent: List custom attributes on an asset
    question: Which custom attribute values are set on a specific asset?
  - id: io-v3-asset-attributes-assigned-delete
    intent: Clear all custom attributes from an asset
    question: Can I wipe every custom attribute value from one asset at once?
  - id: io-v3-asset-attributes-single-update
    intent: Set one custom attribute on an asset
    question: Can I set just one custom attribute value on an asset without touching the others?
  phrasing_ops: 9
  slug: tenable-asset-attributes-api
- baseURL: https://cloud.tenable.com
  baseurl_source: declared
  description: The Assets API from Tenable — 8 operation(s) for assets.
  name: Tenable Assets API
  phrasing_intents:
  - id: assets-list-assets
    intent: List assets
    question: What assets does Tenable know about on my network?
  - id: assets-asset-info
    intent: Get an asset's details
    question: What does Tenable know about one specific asset?
  - id: assets-bulk-update-acr
    intent: Override Asset Criticality Ratings
    question: How do I change the Asset Criticality Rating Tenable assigned to some assets?
  - id: assets-bulk-move
    intent: Move assets to another network
    question: How do I move assets out of the default network into a network I created?
  - id: assets-bulk-delete
    intent: Bulk delete assets matching a query
    question: How do I delete many assets at once that match a query?
  - id: assets-import
    intent: Import asset records
    question: How do I import asset records from my own inventory in JSON?
  - id: assets-list-import-jobs
    intent: List asset import jobs
    question: Which asset imports have I run recently?
  - id: assets-import-job-info
    intent: Check an asset import job
    question: Did my asset import job finish, and how many assets did it process?
  phrasing_ops: 8
  slug: tenable-assets-api
- baseURL: https://cloud.tenable.com
  baseurl_source: declared
  description: With the Attachments API, you can download auxiliary files generated by plugins during a scan. These attachments provide forensic evidence and deeper context for identified vulnerabilities. For more i
  name: Tenable Attachments API
  phrasing_intents:
  - id: was-v2-attachments-download
    intent: Download a web app vulnerability attachment
    question: How do I download the evidence attachment for a web app vulnerability?
  phrasing_ops: 1
  slug: tenable-attachments-api
- baseURL: https://cloud.tenable.com
  baseurl_source: declared
  description: Attacks as detected by Tenable.ad
  name: Tenable Attack API
  phrasing_intents:
  - id: getApiProfilesByProfileIdAttacks
    intent: List detected attacks
    question: Which attacks has Identity Exposure detected against a given host or domain?
  - id: getApiProfilesByProfileIdAttacksExport
    intent: Export attacks as CSV
    question: How do I download detected attacks as a CSV file?
  phrasing_ops: 2
  slug: tenable-attack-api
- baseURL: https://cloud.tenable.com
  baseurl_source: declared
  description: 'The Tenable Attack Path API enables users to retrieve details about attack path findings and attack path vectors. A Finding is an attack technique that exists in one or more attack paths that lead to '
  name: Tenable Attack Path API
  phrasing_intents:
  - id: apa-attack-paths-search
    intent: Search top attack paths
    question: What are the top attack paths leading to my critical assets?
  - id: apa-attack-techniques-search
    intent: Search top attack techniques
    question: Which attack techniques are most prevalent in my organization?
  phrasing_ops: 2
  slug: tenable-attack-path-api
- baseURL: https://cloud.tenable.com
  baseurl_source: declared
  description: The Tenable Attack Path Exports API enables users to export top attack paths, attack technique data, and MITRE ATT&CK heatmap data in JSON or CSV format. MITRE heatmap exports in JSON conform to the M
  name: Tenable Attack Path Exports API
  phrasing_intents:
  - id: apa-export-attack-path
    intent: Export top attack paths
    question: How do I export the top attack paths to a file?
  - id: apa-export-attack-technique
    intent: Export attack techniques
    question: Can I export the attack techniques found in my environment?
  - id: apa-export-mitre-heatmap
    intent: Export a MITRE ATT&CK heatmap
    question: Can I export a MITRE ATT&CK heatmap that I can load into ATT&CK Navigator?
  - id: apa-export-status
    intent: Check an attack path export's status
    question: Is my attack path or heatmap export ready?
  - id: apa-export-download
    intent: Download an attack path export
    question: How do I download a completed attack path export?
  phrasing_ops: 5
  slug: tenable-attack-path-exports-api
- baseURL: https://cloud.tenable.com
  baseurl_source: declared
  description: Attack types
  name: Tenable Attack type API
  phrasing_intents:
  - id: getApiAttackTypes
    intent: List attack types
    question: Which kinds of attacks can Identity Exposure detect?
  phrasing_ops: 1
  slug: tenable-attack-type-api
- baseURL: https://cloud.tenable.com
  baseurl_source: declared
  description: The attack type per directory configuration
  name: Tenable Attack type configuration API
  phrasing_intents:
  - id: getApiAttackTypeConfiguration
    intent: View attack type configuration
    question: Which attack types are enabled on which domains right now?
  - id: patchApiAttackTypeConfiguration
    intent: Change attack type configuration
    question: How do I enable an attack type for additional domains?
  phrasing_ops: 2
  slug: tenable-attack-type-configuration-api
- baseURL: https://cloud.tenable.com
  baseurl_source: declared
  description: Security profile options relative to attack types (Indicator of Attacks)
  name: Tenable Attack type option API
  phrasing_intents:
  - id: getApiProfilesByProfileIdAttackTypesByAttackTypeIdAttackTypeOptions
    intent: List an attack type's options
    question: What tuning options are set for an attack type in my profile?
  - id: postApiProfilesByProfileIdAttackTypesByAttackTypeIdAttackTypeOptions
    intent: Set options on an attack type
    question: How do I tune an attack type's options for one profile?
  phrasing_ops: 2
  slug: tenable-attack-type-option-api
- baseURL: https://cloud.tenable.com
  baseurl_source: declared
  description: After you submit a scan to Tenable for ASV review, you can use the Tenable PCI ASV API to retrieve a list of your attestations and see your current attestation request status. For more information, se
  name: Tenable Attestations API
  phrasing_intents:
  - id: pci-attestations-list
    intent: List PCI ASV attestations
    question: What PCI ASV attestations do I have and what state are they in?
  - id: pci-attestations-details
    intent: Get a PCI attestation's details
    question: What are the details of a specific PCI attestation?
  - id: pci-attestations-disputes-list
    intent: List disputes on a PCI attestation
    question: Which failures have been disputed on a PCI attestation?
  - id: pci-attestations-failures-list
    intent: List undisputed failures on an attestation
    question: Which PCI scan failures are still undisputed on my attestation?
  - id: pci-attestations-assets-list
    intent: List assets covered by an attestation
    question: Which assets are included in a given PCI attestation?
  phrasing_ops: 5
  slug: tenable-attestations-api
- baseURL: https://cloud.tenable.com
  baseurl_source: declared
  description: A checker's category
  name: Tenable Category API
  phrasing_intents:
  - id: getApiCategories
    intent: List checker categories
    question: What categories are indicators grouped into?
  - id: getApiCategoriesById
    intent: Get a category
    question: How do I look up one category by its id?
  phrasing_ops: 2
  slug: tenable-category-api
- baseURL: https://cloud.tenable.com
  baseurl_source: declared
  description: Checkers are the implementations of the state of the art of AD security
  name: Tenable Checker API
  phrasing_intents:
  - id: getApiCheckers
    intent: List indicators of exposure
    question: Which indicators of exposure does Identity Exposure check?
  - id: getApiCheckersById
    intent: Get an indicator of exposure
    question: How do I read the description of one checker?
  phrasing_ops: 2
  slug: tenable-checker-api
- baseURL: https://cloud.tenable.com
  baseurl_source: declared
  description: Security profile options relative to checkers (Indicator of Exposure)
  name: Tenable Checker option API
  phrasing_intents:
  - id: getApiProfilesByProfileIdCheckersByCheckerIdCheckerOptions
    intent: List a checker's options
    question: What thresholds are configured for an indicator of exposure in my profile?
  - id: postApiProfilesByProfileIdCheckersByCheckerIdCheckerOptions
    intent: Set options on a checker
    question: How do I change an indicator of exposure's thresholds for a profile?
  phrasing_ops: 2
  slug: tenable-checker-option-api
- baseURL: https://cloud.tenable.com
  baseurl_source: declared
  description: The Tenable Managed Security Service Provider (MSSP) Portal API provides a secure and accessible way for MSSP administrators to manage and maintain multiple customer instances of Tenable products. Chi
  name: Tenable Child Containers API
  phrasing_intents:
  - id: io-mssp-child-containers-generate-keys
    intent: Generate API keys for a child container
    question: How do I get an access key and secret key for a customer's child container?
  - id: io-mssp-child-containers-list
    intent: List a user's child containers
    question: Which MSSP child containers can a given user access?
  - id: io-mssp-child-containers-history
    intent: Get child container history for an account
    question: What changes have happened to the child containers under a parent account?
  phrasing_ops: 3
  slug: tenable-child-containers-api
- baseURL: https://cloud.tenable.com
  baseurl_source: declared
  description: The Cloud Connectors API from Tenable — 6 operation(s) for cloud connectors.
  name: Tenable Cloud Connectors API
  phrasing_intents:
  - id: io-connectors-create
    intent: Create a cloud connector
    question: How do I connect a cloud account so its assets are discovered automatically?
  - id: io-connectors-list
    intent: List cloud connectors
    question: Which cloud connectors are set up in my account?
  - id: io-connectors-details
    intent: Get a cloud connector's details
    question: What is the configuration and last status of one cloud connector?
  - id: io-connectors-update
    intent: Update a cloud connector
    question: Can I change a connector's name, service accounts or schedule?
  - id: io-connectors-delete
    intent: Delete a cloud connector
    question: How do I remove a cloud connector I no longer need?
  - id: io-connectors-get-arm-template
    intent: Download an Azure ARM template for a connector
    question: Where do I get the ARM template for an Azure Frictionless Assessment connector?
  - id: io-connectors-get-cft-template
    intent: Download an AWS CloudFormation template
    question: How do I get the CloudFormation template for an AWS Frictionless Assessment connector?
  - id: io-connectors-get-aws-cloudtrails
    intent: List available AWS CloudTrails
    question: Which AWS CloudTrails can I use when creating an AWS connector?
  phrasing_ops: 9
  slug: tenable-cloud-connectors-api
- baseURL: https://cloud.tenable.com
  baseurl_source: declared
  description: Attributes sent to tenable cloud statistics
  name: Tenable Cloud statistics API
  phrasing_intents:
  - id: getApiCloudStatistics
    intent: Get cloud statistics user info
    question: What user info does Identity Exposure send with cloud statistics?
  phrasing_ops: 1
  slug: tenable-cloud-statistics-api
- baseURL: https://cloud.tenable.com
  baseurl_source: declared
  description: With the Configurations API, you can create and maintain reusable scan settings. These endpoints allow you to perform standard CRUD operations on configuration objects to standardize scanning across y
  name: Tenable Configurations API
  phrasing_intents:
  - id: was-v2-config-create
    intent: Create a web app scan configuration
    question: How do I set up a new web application scan configuration?
  - id: was-v3-config-remediation
    intent: Get a remediation scan config for a web vuln
    question: How do I get a ready-made scan configuration to retest a web app vulnerability?
  - id: was-v2-config-search
    intent: Search web app scan configurations
    question: Which web application scan configurations exist in my account?
  - id: was-v2-config-details
    intent: Get a web app scan configuration
    question: What targets and settings are defined in a particular WAS scan config?
  - id: was-v2-config-upsert
    intent: Create or replace a web app scan configuration
    question: Can I update a web app scan configuration, or create it if the ID doesn't exist yet?
  - id: was-v2-config-move
    intent: Move a web app scan configuration to a folder
    question: Can I move a web app scan configuration into a different folder?
  - id: was-v2-config-delete
    intent: Delete a web app scan configuration
    question: How do I delete a WAS scan configuration along with its scan history?
  - id: was-v2-config-status
    intent: Check a web app scan config's processing status
    question: Has my WAS scan configuration finished being created or updated?
  phrasing_ops: 9
  slug: tenable-configurations-api
- baseURL: https://cloud.tenable.com
  baseurl_source: declared
  description: The Credentials API from Tenable — 4 operation(s) for credentials.
  name: Tenable Credentials API
  phrasing_intents:
  - id: credentials-create
    intent: Create a managed credential
    question: How do I store an SSH or Windows login once and reuse it across scans?
  - id: credentials-list
    intent: List managed credentials
    question: Which managed credentials can I use in my scans?
  - id: credentials-details
    intent: Get a managed credential's details
    question: What settings and sharing does a specific managed credential have?
  - id: credentials-update
    intent: Update a managed credential
    question: Can I rotate the password inside an existing managed credential?
  - id: credentials-delete
    intent: Delete a managed credential
    question: What happens to scans using a managed credential when I delete it?
  - id: credentials-list-credential-types
    intent: List supported credential types
    question: What kinds of managed credentials are supported for scanning?
  - id: credentials-file-upload
    intent: Upload a file for a managed credential
    question: How do I upload an SSH private key file for a credential?
  phrasing_ops: 7
  slug: tenable-credentials-api
- baseURL: https://cloud.tenable.com
  baseurl_source: declared
  description: A widget container
  name: Tenable Dashboard API
  phrasing_intents:
  - id: getApiDashboards
    intent: List dashboards
    question: Which dashboards exist in my Identity Exposure workspace?
  - id: postApiDashboards
    intent: Create a dashboard
    question: How do I add a new dashboard?
  - id: getApiDashboardsById
    intent: Get a dashboard
    question: How do I fetch a single dashboard by id?
  - id: patchApiDashboardsById
    intent: Rename or reorder a dashboard
    question: Can I rename an existing dashboard?
  - id: deleteApiDashboardsById
    intent: Delete a dashboard and its widgets
    question: Does deleting a dashboard also remove its widgets?
  phrasing_ops: 5
  slug: tenable-dashboard-api
- baseURL: https://cloud.tenable.com
  baseurl_source: declared
  description: The Tenable Managed Security Service Provider (MSSP) Portal API provides a secure and accessible way for MSSP administrators to manage and maintain multiple customer instances of Tenable products. Das
  name: Tenable Dashboards API
  phrasing_intents:
  - id: io-mssp-dashboard-details
    intent: Get data for an MSSP dashboard widget
    question: What data does a specific MSSP Portal dashboard widget show?
  phrasing_ops: 1
  slug: tenable-dashboards-api
- baseURL: https://cloud.tenable.com
  baseurl_source: declared
  description: Security deviance items
  name: Tenable Deviance API
  phrasing_intents:
  - id: getApiDeviancesChanged
    intent: List deviances created or resolved since an event
    question: Which deviances appeared or got resolved since the last event I processed?
  - id: getApiDirectoriesByDirectoryIdDeviancesById
    intent: Get a deviance history entry in a directory
    question: How do I look up one deviance history record by id within a directory?
  - id: getApiExportProfilesByProfileIdCheckersByCheckerId
    intent: Export a checker's deviant objects as CSV
    question: Can I download all AD objects failing an indicator as CSV?
  - id: getApiInfrastructuresByInfrastructureIdDirectoriesByDirectoryIdDeviances
    intent: List deviances in a directory
    question: Which deviances exist across one domain, regardless of checker?
  - id: getApiInfrastructuresByInfrastructureIdDirectoriesByDirectoryIdDeviancesById
    intent: Get a deviance history entry in a forest
    question: How do I read one deviance record when I know its forest and domain?
  - id: patchApiInfrastructuresByInfrastructureIdDirectoriesByDirectoryIdDeviancesById
    intent: Ignore one deviance until a date
    question: Can I snooze a single deviance until a certain date?
  - id: getApiProfilesByProfileIdInfrastructuresByInfrastructureIdDirectoriesByDirectoryIdCheckersByCheckerIdDeviances
    intent: List a checker's deviances in one directory
    question: Which deviances does one indicator raise in a single domain?
  - id: patchApiProfilesByProfileIdCheckersByCheckerIdDeviances
    intent: Ignore all deviances of a checker
    question: Can I ignore every deviance from one indicator until a date?
  phrasing_ops: 12
  slug: tenable-deviance-api
- baseURL: https://cloud.tenable.com
  baseurl_source: declared
  description: Represents an Active directory
  name: Tenable Directory API
  phrasing_intents:
  - id: getApiDirectories
    intent: List all monitored directories
    question: Which AD domains is Identity Exposure monitoring across all forests?
  - id: postApiDirectories
    intent: Add a directory to monitor
    question: How do I start monitoring a new Active Directory domain?
  - id: getApiDirectoriesById
    intent: Get a directory
    question: How do I fetch a domain's settings by directory id alone?
  - id: getApiInfrastructuresByInfrastructureIdDirectories
    intent: List directories in a forest
    question: Which domains belong to a given forest?
  - id: getApiInfrastructuresByInfrastructureIdDirectoriesById
    intent: Get a directory within a forest
    question: How do I look up a domain through its forest?
  - id: patchApiInfrastructuresByInfrastructureIdDirectoriesById
    intent: Update a directory's connection
    question: Can I change the domain controller IP for a directory?
  - id: deleteApiInfrastructuresByInfrastructureIdDirectoriesById
    intent: Stop monitoring a directory
    question: How do I remove a domain from Identity Exposure?
  phrasing_ops: 7
  slug: tenable-directory-api
- baseURL: https://cloud.tenable.com
  baseurl_source: declared
  description: The Tenable Managed Security Service Provider (MSSP) Portal API provides a secure and accessible way for MSSP administrators to manage and maintain multiple customer instances of Tenable products. Dom
  name: Tenable Domains API
  phrasing_intents:
  - id: io-mssp-domains-add
    intent: Add a domain to a container
    question: How do I add a domain to a customer container once I have the activation code?
  - id: io-mssp-domains-list
    intent: List child containers and their domains
    question: Which domains are attached to my MSSP child containers?
  - id: io-mssp-domains-details-list
    intent: Get domains for a customer account
    question: Which domains belong to a particular customer account?
  - id: io-mssp-domains-update
    intent: Update a customer account's domain
    question: How do I change a domain's status on a customer account?
  - id: io-mssp-domains-verification
    intent: Send a domain activation code
    question: How do I get the verification code needed to add a domain to a container?
  phrasing_ops: 5
  slug: tenable-domains-api
- baseURL: https://cloud.tenable.com
  baseurl_source: declared
  description: The Downloads API enables customers to access and download installation and update files for available Tenable products. You can use the API endpoints to list product pages, list downloads available f
  name: Tenable Downloads API
  phrasing_intents:
  - id: getPages
    intent: List downloadable product pages
    question: Which Tenable products can I download installers for?
  - id: getPagesBySlug
    intent: List files for a product
    question: What installer files are available for Nessus?
  - id: getPagesBySlugFilesByFile
    intent: Download a product file
    question: How do I download the latest Nessus installer?
  phrasing_ops: 3
  slug: tenable-downloads-api
- baseURL: https://cloud.tenable.com
  baseurl_source: declared
  description: The Editor API from Tenable — 5 operation(s) for editor.
  name: Tenable Editor API
  phrasing_intents:
  - id: editor-details
    intent: Get a scan or policy's editor configuration
    question: How can I see the full editable configuration of a scan or policy?
  - id: editor-list-templates
    intent: List Tenable scan or policy templates
    question: Which Tenable-provided scan templates can I create a scan from?
  - id: editor-template-details
    intent: Get details of a scan template
    question: What options does a particular scan template expose?
  - id: editor-plugin-description
    intent: Get a plugin's details within a policy
    question: What does a plugin enabled in my scan policy actually do?
  - id: editor-audits
    intent: Download a custom audit file
    question: How do I download the custom audit file attached to a scan or policy?
  phrasing_ops: 5
  slug: tenable-editor-api
- baseURL: https://cloud.tenable.com
  baseurl_source: declared
  description: An email notification about new deviances
  name: Tenable Email notifier API
  phrasing_intents:
  - id: getApiEmailNotifiers
    intent: List email alert notifiers
    question: Who receives email alerts from Identity Exposure?
  - id: postApiEmailNotifiers
    intent: Create an email notifier
    question: How do I set up email alerts for a new recipient?
  - id: getApiEmailNotifiersById
    intent: Get an email notifier
    question: What thresholds and directories does one email notifier cover?
  - id: patchApiEmailNotifiersById
    intent: Update an email notifier
    question: Can I change the address an email notifier sends to?
  - id: deleteApiEmailNotifiersById
    intent: Delete an email notifier
    question: How do I stop sending email alerts to someone?
  - id: getApiEmailNotifiersTestMessageById
    intent: Send a test email for a saved notifier
    question: How do I check that an existing email notifier actually delivers?
  - id: postApiEmailNotifiersTestMessage
    intent: Send a test email before saving
    question: Can I test email alert settings before creating the notifier?
  phrasing_ops: 7
  slug: tenable-email-notifier-api
- baseURL: https://cloud.tenable.com
  baseurl_source: declared
  description: A change in the Active Directory
  name: Tenable Event API
  phrasing_intents:
  - id: getApiDirectoriesByDirectoryIdEventsById
    intent: Get an AD event in a directory
    question: How do I look up one AD change event by id in a domain?
  - id: getApiInfrastructuresByInfrastructureIdDirectoriesByDirectoryIdEventsById
    intent: Get an AD event within a forest
    question: Can I fetch an event using its forest and domain ids?
  - id: postApiEventsSearch
    intent: Search AD change events
    question: How do I search AD change events across domains in a time window?
  phrasing_ops: 3
  slug: tenable-event-api
- baseURL: https://cloud.tenable.com
  baseurl_source: declared
  description: The Exclusions API from Tenable — 3 operation(s) for exclusions.
  name: Tenable Exclusions API
  phrasing_intents:
  - id: exclusions-create
    intent: Create a scan exclusion
    question: How do I stop certain IP ranges from being scanned?
  - id: exclusions-list
    intent: List scan exclusions
    question: Which hosts are excluded from my vulnerability scans?
  - id: exclusions-import
    intent: Import scan exclusions from a file
    question: Can I bulk import scan exclusions from a file?
  - id: exclusions-details
    intent: Get a scan exclusion
    question: What hosts and schedule are in a particular exclusion?
  - id: exclusions-edit
    intent: Update a scan exclusion
    question: Can I change the hosts covered by an existing exclusion?
  - id: exclusions-delete
    intent: Delete a scan exclusion
    question: How do I delete an exclusion so those hosts get scanned again?
  phrasing_ops: 6
  slug: tenable-exclusions-api
- baseURL: https://cloud.tenable.com
  baseurl_source: declared
  description: With the Exports API, you can manage asynchronous finding exports. Use these endpoints to initiate export jobs, monitor status, and download results in chunks for integration with external workflow ma
  name: Tenable Exports API
  phrasing_intents:
  - id: was-export-findings
    intent: Start a web app findings export
    question: How do I export my Web App Scanning findings in bulk?
  - id: was-export-findings-status
    intent: Check a web app findings export's status
    question: Is my web app findings export ready to download?
  - id: was-export-findings-jobs-list
    intent: List web app findings export jobs
    question: What web app findings exports have been run recently?
  - id: was-export-findings-download-chunk
    intent: Download a chunk of web app findings
    question: Can I download one chunk of my web app findings export as JSON?
  - id: was-export-findings-cancel
    intent: Cancel a web app findings export
    question: Can I cancel a web app findings export I started by mistake?
  phrasing_ops: 5
  slug: tenable-exports-api
- baseURL: https://cloud.tenable.com
  baseurl_source: declared
  description: The Exports (Assets) API from Tenable — 6 operation(s) for exports (assets).
  name: Tenable Exports (Assets) API
  phrasing_intents:
  - id: export-assets-v1
    intent: Start an asset export (v1)
    question: Can I still bulk export assets with the original v1 export endpoint?
  - id: export-assets-v2
    intent: Start an asset export including web apps (v2)
    question: How do I export all my assets including Web App Scanning assets?
  - id: exports-assets-export-status
    intent: Check an asset export's status
    question: Which chunks of my asset export are ready to download?
  - id: exports-assets-export-status-recent
    intent: List recent asset export jobs
    question: What asset export jobs have been run recently?
  - id: exports-assets-download-chunk
    intent: Download one chunk of an asset export
    question: How long are exported asset chunks available to download?
  - id: exports-assets-export-cancel
    intent: Cancel an asset export
    question: Can I stop an asset export that's taking too long?
  phrasing_ops: 6
  slug: tenable-exports-assets-api
- baseURL: https://cloud.tenable.com
  baseurl_source: declared
  description: The Exports (Compliance Data) API from Tenable — 5 operation(s) for exports (compliance data).
  name: Tenable Exports (Compliance Data) API
  phrasing_intents:
  - id: io-exports-compliance-create
    intent: Start a compliance data export
    question: How do I export compliance audit results for all my assets?
  - id: io-exports-compliance-status
    intent: Check a compliance export's status
    question: Is my compliance export finished, and which chunks are ready?
  - id: exports-compliance-status-list
    intent: List recent compliance export jobs
    question: Which compliance exports have been requested recently?
  - id: io-exports-compliance-download
    intent: Download a compliance export chunk
    question: How do I download one chunk of a finished compliance export?
  - id: io-exports-compliance-cancel
    intent: Cancel a compliance export
    question: Can I stop a compliance export that is still processing?
  phrasing_ops: 5
  slug: tenable-exports-compliance-data-api
- baseURL: https://cloud.tenable.com
  baseurl_source: declared
  description: The Exports (Vulnerabilities) API from Tenable — 5 operation(s) for exports (vulnerabilities).
  name: Tenable Exports (Vulnerabilities) API
  phrasing_intents:
  - id: exports-vulns-request-export
    intent: Start a bulk vulnerability export
    question: How do I export all my vulnerability data in bulk?
  - id: exports-vulns-export-status
    intent: Check a vulnerability export's status
    question: Which chunks of my vulnerability export are ready?
  - id: exports-vulns-export-status-recent
    intent: List recent vulnerability export jobs
    question: What vulnerability export jobs have run recently?
  - id: exports-vulns-download-chunk
    intent: Download a vulnerability export chunk
    question: How do I download a chunk of a vulnerability export?
  - id: exports-vulns-export-cancel
    intent: Cancel a vulnerability export
    question: Can I cancel a vulnerability export that's taking too long?
  phrasing_ops: 5
  slug: tenable-exports-vulnerabilities-api
- baseURL: https://cloud.tenable.com
  baseurl_source: declared
  description: The Tenable Exposure View API enables users to search Tenable Exposure view for their organization's cards or retrieve the details for a specified card. For more information about Exposure View, see [
  name: Tenable Exposure View API
  phrasing_intents:
  - id: exposure-view-cards-search
    intent: Search exposure view cards
    question: Which exposure view cards match a keyword?
  - id: exposure-view-card-details
    intent: Get an exposure card's trend and SLA data
    question: What's the SLA efficiency and exposure trend for a specific card?
  phrasing_ops: 2
  slug: tenable-exposure-view-api
- baseURL: https://cloud.tenable.com
  baseurl_source: declared
  description: The File API from Tenable — 1 operation(s) for file.
  name: Tenable File API
  phrasing_intents:
  - id: file-upload
    intent: Upload a file
    question: How do I upload a file, such as a .nessus policy, so I can import it later?
  phrasing_ops: 1
  slug: tenable-file-api
- baseURL: https://cloud.tenable.com
  baseurl_source: declared
  description: The Tenable Managed Security Service Provider (MSSP) Portal API provides a secure and accessible way for MSSP administrators to manage and maintain multiple customer instances of Tenable products. Fil
  name: Tenable Filters API
  phrasing_intents:
  - id: io-mssp-filters-account-list
    intent: List filters for MSSP customer accounts
    question: Which fields can I filter MSSP customer account lists by?
  - id: io-filters-agents-list
    intent: List filters for agent records
    question: What fields can I filter and sort Nessus agents by?
  - id: io-filters-assets-list
    intent: List asset workbench filters
    question: Which filters can I apply in the assets workbench?
  - id: io-filters-assets-list-v2
    intent: List asset workbench filters scoped to tags
    question: Can I get the asset workbench filters that apply to assets with specific tags?
  - id: io-filters-credentials-list
    intent: List filters for scan credentials
    question: What can I filter my stored scan credentials by?
  - id: vm-filters-reports-list
    intent: List filters for report exports
    question: Which filters and allowed values can I use when exporting a report?
  - id: io-filters-scan-list
    intent: List filters for vulnerability scan records
    question: What fields can I filter my vulnerability management scan results by?
  - id: io-filters-scan-history-list
    intent: List filters for scan history records
    question: Can I filter a scan's past runs, and by which fields?
  phrasing_ops: 15
  slug: tenable-filters-api
- baseURL: https://cloud.tenable.com
  baseurl_source: declared
  description: The Folders API from Tenable — 4 operation(s) for folders.
  name: Tenable Folders API
  phrasing_intents:
  - id: folders-create
    intent: Create a vulnerability management scan folder
    question: How do I create a new folder to organise my network scans?
  - id: folders-list
    intent: List vulnerability management scan folders
    question: What scan folders do I have in Vulnerability Management?
  - id: folders-edit
    intent: Rename a vulnerability management scan folder
    question: Can I rename one of my network scan folders?
  - id: folders-delete
    intent: Delete a vulnerability management scan folder
    question: What happens to the scans in a network scan folder when I delete it?
  - id: was-v2-folders-create
    intent: Create a web app scanning folder
    question: How do I create a folder for my web application scans?
  - id: was-v2-folders-list
    intent: List web app scanning folders
    question: Which custom folders do I have in Web App Scanning?
  - id: was-v2-folders-update
    intent: Rename a web app scanning folder
    question: Can I rename a folder in Web App Scanning?
  - id: was-v2-folders-delete
    intent: Delete a web app scanning folder
    question: How do I delete a Web App Scanning folder?
  phrasing_ops: 8
  slug: tenable-folders-api
- baseURL: https://cloud.tenable.com
  baseurl_source: declared
  description: A groupment of directories
  name: Tenable Infrastructure API
  phrasing_intents:
  - id: getApiInfrastructures
    intent: List forests
    question: Which AD forests are configured in Identity Exposure?
  - id: postApiInfrastructures
    intent: Add a forest
    question: How do I add a new Active Directory forest?
  - id: getApiInfrastructuresById
    intent: Get a forest
    question: How do I view one forest's settings?
  - id: patchApiInfrastructuresById
    intent: Update a forest's name or credentials
    question: Can I rotate the service account password for a forest?
  - id: deleteApiInfrastructuresById
    intent: Delete a forest
    question: How do I remove a forest from monitoring?
  phrasing_ops: 5
  slug: tenable-infrastructure-api
- baseURL: https://cloud.tenable.com
  baseurl_source: declared
  description: The Tenable Inventory API enables users to search for their organization's assets and the software installed on those assets. Additionally, API endpoints are provided to retrieve a list of asset and s
  name: Tenable Inventory API
  phrasing_intents:
  - id: inventory-assets-search
    intent: Search the asset inventory
    question: Which assets in my organization match a given set of criteria?
  - id: inventory-findings-search
    intent: Search security findings
    question: What findings across my organization match certain criteria?
  - id: inventory-software-search
    intent: Search installed software
    question: Which software is installed across my assets?
  - id: inventory-asset-properties-list
    intent: List filterable asset properties
    question: Which asset properties can I use as filters in an asset search?
  - id: inventory-finding-properties-list
    intent: List filterable finding properties
    question: What finding properties are available as search filters?
  - id: inventory-software-properties-list
    intent: List filterable software properties
    question: Which software properties can I filter a software search by?
  phrasing_ops: 6
  slug: tenable-inventory-api
- baseURL: https://cloud.tenable.com
  baseurl_source: declared
  description: The Tenable Inventory Exports API enables users to export inventory assets and findings in JSON or CSV format. For more information about exporting assets and findings from Tenable Exposure Management
  name: Tenable Inventory Exports API
  phrasing_intents:
  - id: inventory-export-assets
    intent: Export inventory assets
    question: How do I export my Tenable One asset inventory to CSV or JSON?
  - id: inventory-export-findings
    intent: Export inventory findings
    question: Can I export findings from the inventory that match a search?
  - id: inventory-export-assets-jobs
    intent: List recent asset export jobs
    question: Which inventory asset exports have I run in the last few days?
  - id: inventory-export-findings-jobs
    intent: List recent findings export jobs
    question: Which inventory findings exports were submitted recently?
  - id: inventory-export-status
    intent: Get an inventory export's status
    question: Is my inventory export finished and which chunks are ready?
  - id: inventory-export-download
    intent: Download an inventory export chunk
    question: How do I download one chunk of an inventory export?
  phrasing_ops: 6
  slug: tenable-inventory-exports-api
- baseURL: https://cloud.tenable.com
  baseurl_source: declared
  description: Configuration of LDAP for authentication purposes.
  name: Tenable LDAP configuration API
  phrasing_intents:
  - id: getApiLdapConfiguration
    intent: View LDAP sign-in configuration
    question: Is LDAP authentication turned on for Identity Exposure?
  - id: patchApiLdapConfiguration
    intent: Update LDAP sign-in configuration
    question: How do I enable LDAP sign-in?
  phrasing_ops: 2
  slug: tenable-ldap-configuration-api
- baseURL: https://cloud.tenable.com
  baseurl_source: declared
  description: Product license
  name: Tenable License API
  phrasing_intents:
  - id: getApiLicense
    intent: Check the Identity Exposure license
    question: Which license is installed on my Identity Exposure instance?
  - id: postApiLicense
    intent: Install a new Identity Exposure license
    question: How do I upload a new license key to Identity Exposure?
  - id: getApiLicenseProductAssociation
    intent: See which product the license is tied to
    question: Which product is my Identity Exposure license associated with?
  - id: io-mssp-license-details
    intent: Get account license details
    question: What does my Tenable license cover for this account?
  phrasing_ops: 4
  slug: tenable-license-api
- baseURL: https://cloud.tenable.com
  baseurl_source: declared
  description: Configuration of the mechanism that locks out user accounts after multiple failed login attempts.
  name: Tenable Lockout policy API
  phrasing_intents:
  - id: getApiLockoutPolicy
    intent: View the account lockout policy
    question: How many failed logins lock an account?
  - id: patchApiLockoutPolicy
    intent: Change the account lockout policy
    question: Can I lengthen how long accounts stay locked out?
  phrasing_ops: 2
  slug: tenable-lockout-policy-api
- baseURL: https://cloud.tenable.com
  baseurl_source: declared
  description: 'The Tenable Managed Security Service Provider (MSSP) Portal API provides a secure and accessible way for MSSP administrators to manage the logos of their customer''s instances. By default, the Tenable '
  name: Tenable Logos API
  phrasing_intents:
  - id: io-mssp-logos-create
    intent: Upload a new logo
    question: How do I upload a logo to the MSSP Portal for customer branding?
  - id: io-mssp-logos-list
    intent: List logos in the MSSP Portal
    question: Which logos have I uploaded to the MSSP Portal?
  - id: io-mssp-logos-details
    intent: Get details of a logo
    question: What metadata is stored for a specific uploaded logo?
  - id: io-mssp-logos-update
    intent: Replace an existing logo
    question: Can I swap out the image of a logo I already uploaded?
  - id: io-mssp-logos-delete
    intent: Delete a logo
    question: Can I remove a logo I no longer use from the portal?
  - id: io-mssp-logos-assign
    intent: Assign a logo to customer accounts
    question: How do I brand several customer accounts with the same logo?
  - id: io-mssp-logos-png-download
    intent: Download a logo as PNG
    question: Can I download an uploaded logo as a PNG image?
  - id: io-mssp-logos-base64-download
    intent: Download a logo as Base64
    question: Can I get a portal logo as a Base64 string to embed in HTML?
  phrasing_ops: 8
  slug: tenable-logos-api
- baseURL: https://cloud.tenable.com
  baseurl_source: declared
  description: The Metrics API from Tenable — 1 operation(s) for metrics.
  name: Tenable Metrics API
  phrasing_intents:
  - id: getApiMetrics
    intent: Collect platform health metrics
    question: Is the Eridanis service and SQL Server healthy?
  phrasing_ops: 1
  slug: tenable-metrics-api
- baseURL: https://cloud.tenable.com
  baseurl_source: declared
  description: The Networks API from Tenable — 6 operation(s) for networks.
  name: Tenable Networks API
  phrasing_intents:
  - id: networks-create
    intent: Create a network object
    question: How do I create a network to separate overlapping IP ranges?
  - id: networks-list
    intent: List network objects
    question: What network objects are set up in my Tenable organization?
  - id: networks-details
    intent: Get details of a network
    question: What settings does a specific network object have?
  - id: networks-update
    intent: Update a network's name or settings
    question: Can I rename an existing network object?
  - id: networks-delete
    intent: Delete a network object
    question: What should I do with assets before deleting a network?
  - id: io-networks-asset-count-details
    intent: Count stale assets in a network
    question: How many assets in a network haven't been seen in the last 30 days?
  - id: networks-assign-scanner
    intent: Assign one scanner to a network
    question: How do I put a single scanner or scanner group into a custom network?
  - id: networks-list-scanners
    intent: List scanners in a network
    question: Which scanners and scanner groups belong to a given network?
  phrasing_ops: 10
  slug: tenable-networks-api
- baseURL: https://cloud.tenable.com
  baseurl_source: declared
  description: The OT Connectors API from Tenable — 4 operation(s) for ot connectors.
  name: Tenable OT Connectors API
  phrasing_intents:
  - id: sensors-ot-create
    intent: Create an OT connector
    question: How do I connect a Tenable OT Security instance to Vulnerability Management?
  - id: sensors-ot-list
    intent: List OT connectors
    question: Which OT connectors are linked to my account?
  - id: sensors-ot-details
    intent: Get an OT connector's details
    question: What's the status and configuration of a specific OT connector?
  - id: sensors-ot-update
    intent: Update or toggle an OT connector
    question: Can I disable an OT connector without deleting it?
  - id: sensors-ot-delete
    intent: Delete an OT connector
    question: Can I remove an OT connector I decommissioned?
  - id: sensors-ot-linking-key-generate
    intent: Generate a linking key for OT connectors
    question: How long is an OT connector linking key valid?
  phrasing_ops: 6
  slug: tenable-ot-connectors-api
- baseURL: https://cloud.tenable.com
  baseurl_source: declared
  description: 'The Tenable Managed Security Service Provider (MSSP) Portal API provides a secure and accessible way for MSSP administrators to manage their partner information. Partner endpoints in the Tenable MSSP '
  name: Tenable Partners API
  phrasing_intents:
  - id: mssp-partner-details
    intent: Get my MSSP partner details
    question: What partner details are associated with my API credentials?
  phrasing_ops: 1
  slug: tenable-partners-api
- baseURL: https://cloud.tenable.com
  baseurl_source: declared
  description: The Permissions API from Tenable — 1 operation(s) for permissions.
  name: Tenable Permissions API
  phrasing_intents:
  - id: permissions-list
    intent: Get an object's permissions
    question: Who can use a particular scanner or agent group?
  - id: permissions-change
    intent: Update an object's permissions
    question: How do I grant a user access to a specific scanner?
  phrasing_ops: 2
  slug: tenable-permissions-api
- baseURL: https://cloud.tenable.com
  baseurl_source: declared
  description: The Plugins API from Tenable — 7 operation(s) for plugins.
  name: Tenable Plugins API
  phrasing_intents:
  - id: io-plugins-list
    intent: List vulnerability management plugins
    question: How do I get the full list of Tenable plugins with their details?
  - id: io-plugins-details
    intent: Get a vulnerability management plugin
    question: What does a specific Nessus plugin check for?
  - id: io-plugins-families-list
    intent: List plugin families
    question: What plugin families are available?
  - id: io-plugins-family-details-id
    intent: List plugins in a family by ID
    question: Which plugins belong to a plugin family when I have its ID?
  - id: io-plugins-family-details-name
    intent: List plugins in a family by name
    question: Can I look up the plugins in a family using the family name instead of its ID?
  - id: was-v2-plugins-list
    intent: List web app scanning plugins
    question: Which plugins does Web App Scanning use?
  - id: was-v2-plugins-details
    intent: Get a web app scanning plugin
    question: What does a particular web application scanning plugin detect?
  phrasing_ops: 7
  slug: tenable-plugins-api
- baseURL: https://cloud.tenable.com
  baseurl_source: declared
  description: The Policies API from Tenable — 5 operation(s) for policies.
  name: Tenable Policies API
  phrasing_intents:
  - id: policies-create
    intent: Create a scan policy
    question: How do I create a new scan template from one of the built-in templates?
  - id: policies-list
    intent: List scan policies
    question: Which scan templates (policies) have we saved?
  - id: policies-copy
    intent: Copy a scan policy
    question: Can I duplicate an existing scan template to tweak it?
  - id: policies-import
    intent: Import a .nessus scan policy
    question: How do I import a scan policy from a .nessus file I uploaded?
  - id: policies-export
    intent: Export a scan policy as .nessus
    question: Can I export a scan template to a .nessus file?
  - id: policies-details
    intent: Get a scan policy's settings
    question: What settings and plugins are configured in a given scan template?
  - id: policies-configure
    intent: Update a scan policy
    question: How do I change the settings of an existing scan template?
  - id: policies-delete
    intent: Delete a scan policy
    question: How do I delete a scan template I no longer use?
  phrasing_ops: 8
  slug: tenable-policies-api
- baseURL: https://cloud.tenable.com
  baseurl_source: declared
  description: A user's preferences
  name: Tenable Preference API
  phrasing_intents:
  - id: getApiPreferences
    intent: View my preferences
    question: What language and default profile are set for my account?
  - id: patchApiPreferences
    intent: Update my preferences
    question: How do I switch the interface language?
  phrasing_ops: 2
  slug: tenable-preference-api
- baseURL: https://cloud.tenable.com
  baseurl_source: declared
  description: A set of Checker option value
  name: Tenable Profile API
  phrasing_intents:
  - id: getApiProfiles
    intent: List security profiles
    question: Which security profiles exist?
  - id: postApiProfiles
    intent: Create a security profile
    question: How do I create a new blank security profile?
  - id: getApiProfilesById
    intent: Get a security profile
    question: How do I view one profile's settings?
  - id: patchApiProfilesById
    intent: Rename or rescope a profile
    question: Can I rename a security profile?
  - id: deleteApiProfilesById
    intent: Delete a security profile
    question: How do I remove a profile I no longer need?
  - id: postApiProfilesFromByFromId
    intent: Copy a profile into a new one
    question: Can I clone an existing profile as a starting point?
  - id: postApiProfilesByIdUnstage
    intent: Discard a profile's staged changes
    question: How do I throw away uncommitted changes on a profile?
  - id: postApiProfilesByIdCommit
    intent: Commit a profile's staged changes
    question: How do I apply staged changes to a profile?
  phrasing_ops: 8
  slug: tenable-profile-api
- baseURL: https://cloud.tenable.com
  baseurl_source: declared
  description: The Profiles API from Tenable — 4 operation(s) for profiles.
  name: Tenable Profiles API
  phrasing_intents:
  - id: profiles-create
    intent: Create an agent or scanner profile
    question: How do I create a new profile to pin agents to a plugin set?
  - id: profiles-list
    intent: List agent or scanner profiles
    question: Which agent profiles or scanner profiles do I have?
  - id: profiles-details
    intent: Get a profile's details
    question: What configuration does a particular agent profile have?
  - id: profiles-update
    intent: Update a profile
    question: How do I change the name or configuration of an existing profile?
  - id: profiles-delete
    intent: Delete a profile
    question: How do I delete an agent or scanner profile?
  - id: profiles-clone
    intent: Clone a profile
    question: Can I make a copy of an existing profile under a new name?
  - id: profiles-feed-versions
    intent: List recent plugin sets for profiles
    question: Which plugin sets were released to the feed in the last 30 days?
  phrasing_ops: 7
  slug: tenable-profiles-api
- baseURL: https://cloud.tenable.com
  baseurl_source: declared
  description: The reason why a AD object is marked as deviant
  name: Tenable Reason API
  phrasing_intents:
  - id: getApiReasons
    intent: List deviance reasons
    question: What reasons can a deviance be raised for?
  - id: getApiReasonsById
    intent: Get a deviance reason
    question: How do I look up what one reason id means?
  - id: getApiProfilesByProfileIdCheckersByCheckerIdReasons
    intent: List reasons with deviances for a checker
    question: Which reasons are actually producing deviances for one indicator?
  - id: getApiProfilesByProfileIdInfrastructuresByInfrastructureIdDirectoriesByDirectoryIdEventsByEventIdReasons
    intent: List reasons with deviances for an event
    question: Which reasons explain the deviances a specific event created?
  phrasing_ops: 4
  slug: tenable-reason-api
- baseURL: https://cloud.tenable.com
  baseurl_source: declared
  description: The Recast Rules API from Tenable — 4 operation(s) for recast rules.
  name: Tenable Recast Rules API
  phrasing_intents:
  - id: recast-rules-create
    intent: Create a recast or accept rule
    question: How do I recast the severity of a vulnerability across matching findings?
  - id: recast-rules-search
    intent: Search recast and accept rules
    question: Which recast or accept rules apply to web app findings?
  - id: recast-rules-details
    intent: Get a recast rule's details
    question: What filter and action does a specific recast rule use?
  - id: recast-rules-update
    intent: Update a recast or accept rule
    question: How do I change the filter or expiry of an existing recast rule?
  - id: recast-rules-delete
    intent: Delete a recast or accept rule
    question: How do I delete a recast rule so findings go back to their original severity?
  - id: recast-rules-filters-list
    intent: List properties for filtering recast rules
    question: Which properties and operators can I use to filter recast rules?
  phrasing_ops: 6
  slug: tenable-recast-rules-api
- baseURL: https://cloud.tenable.com
  baseurl_source: declared
  description: Configure relays that make AD queries for Ceti
  name: Tenable Relay API
  phrasing_intents:
  - id: getApiRelaysLinkingKey
    intent: Get the relay linking key
    question: What key do I need to link a new relay?
  phrasing_ops: 1
  slug: tenable-relay-api
- baseURL: https://cloud.tenable.com
  baseurl_source: declared
  description: The Remediation Scans API from Tenable — 1 operation(s) for remediation scans.
  name: Tenable Remediation Scans API
  phrasing_intents:
  - id: io-scans-remediation-create
    intent: Create a remediation scan
    question: How do I create a scan that verifies a vulnerability has been fixed?
  - id: io-scans-remediation-list
    intent: List remediation scans
    question: Which remediation scans exist in my account?
  phrasing_ops: 2
  slug: tenable-remediation-scans-api
- baseURL: https://cloud.tenable.com
  baseurl_source: declared
  description: Token to access the reports download
  name: Tenable Report access token API
  phrasing_intents:
  - id: getApiReportAccessToken
    intent: Get the reporting access token
    question: What token does reporting use to pull data from Tenable Cloud?
  - id: postApiReportAccessTokenRefresh
    intent: Rotate the reporting access token
    question: How do I refresh the report access token?
  phrasing_ops: 2
  slug: tenable-report-access-token-api
- baseURL: https://cloud.tenable.com
  baseurl_source: declared
  description: The Reports API from Tenable — 3 operation(s) for reports.
  name: Tenable Reports API
  phrasing_intents:
  - id: vm-reports-create
    intent: Generate a PDF report
    question: How do I generate a PDF vulnerability report from a template?
  - id: vm-reports-status
    intent: Check a report's generation status
    question: Is my PDF report finished generating?
  - id: vm-reports-download
    intent: Download a generated PDF report
    question: Can I download the PDF once my report is ready?
  phrasing_ops: 3
  slug: tenable-reports-api
- baseURL: https://cloud.tenable.com
  baseurl_source: declared
  description: The Tenable Managed Security Service Provider (MSSP) Portal API provides a secure and accessible way for MSSP administrators to manage and maintain multiple customer instances of Tenable products. Res
  name: Tenable Resource Links API
  phrasing_intents:
  - id: io-mssp-resource-links-bulk
    intent: Add resource links to many customer accounts
    question: How do I push the same resource links to several customer accounts at once?
  - id: io-mssp-resource-links-add
    intent: Add resource links to one customer account
    question: How do I add or change resource links on a single customer account?
  - id: io-mssp-resource-links-list
    intent: List a customer account's resource links
    question: Which resource links are configured for a given customer account?
  phrasing_ops: 3
  slug: tenable-resource-links-api
- baseURL: https://cloud.tenable.com
  baseurl_source: declared
  description: Groupment of permissions that may be assigned to several users
  name: Tenable Role API
  phrasing_intents:
  - id: getApiRoles
    intent: List roles
    question: Which roles exist in Identity Exposure?
  - id: postApiRoles
    intent: Create a role
    question: How do I create a new empty role?
  - id: getApiRolesUserCreationDefaults
    intent: Get default roles for new users
    question: Which roles do new users get by default?
  - id: getApiRolesById
    intent: Get a role
    question: How do I view one role's description?
  - id: patchApiRolesById
    intent: Rename or redescribe a role
    question: Can I rename a role?
  - id: deleteApiRolesById
    intent: Delete a role
    question: How do I remove a role?
  - id: postApiRolesFromByFromId
    intent: Copy a role into a new one
    question: Can I clone an existing role?
  - id: putApiRolesByIdPermissions
    intent: Replace a role's permissions
    question: How do I set exactly which permissions a role grants?
  phrasing_ops: 8
  slug: tenable-role-api
- baseURL: https://cloud.tenable.com
  baseurl_source: declared
  description: Authentification configuration with SAML
  name: Tenable SAML configuration API
  phrasing_intents:
  - id: getApiSamlConfiguration
    intent: View SAML single sign-on configuration
    question: Is SAML single sign-on enabled?
  - id: patchApiSamlConfiguration
    intent: Update SAML single sign-on configuration
    question: How do I turn on SAML sign-in?
  - id: getApiSamlConfigurationGenerateCertificate
    intent: Generate a SAML certificate
    question: How do I generate a certificate for SAML setup?
  phrasing_ops: 3
  slug: tenable-saml-configuration-api
- baseURL: https://cloud.tenable.com
  baseurl_source: declared
  description: The Scan Control API from Tenable — 5 operation(s) for scan control.
  name: Tenable Scan Control API
  phrasing_intents:
  - id: scans-launch
    intent: Launch a scan
    question: How do I start a vulnerability scan right now?
  - id: scans-pause
    intent: Pause a running scan
    question: Can I pause a scan that's currently running?
  - id: scans-resume
    intent: Resume a paused scan
    question: How do I continue a scan I paused earlier?
  - id: scans-stop
    intent: Stop a scan
    question: Can I stop a scan that's pending or running?
  - id: vm-scans-stop-force
    intent: Force stop a stuck scan
    question: Can I force a scan to abort and cancel its incomplete tasks?
  phrasing_ops: 5
  slug: tenable-scan-control-api
- baseURL: https://cloud.tenable.com
  baseurl_source: declared
  description: The Scan Exports API from Tenable — 4 operation(s) for scan exports.
  name: Tenable Scan Exports API
  phrasing_intents:
  - id: scans-export-request
    intent: Export a scan's results to a file
    question: How do I export a scan's results as a PDF, CSV or Nessus file?
  - id: scans-export-list
    intent: List recent scan exports
    question: Which scan exports have been generated in the past 30 days?
  - id: scans-export-status
    intent: Check a scan export's status
    question: Is my exported scan file ready to download?
  - id: scans-export-download
    intent: Download a scan export file
    question: How do I download an exported scan file?
  phrasing_ops: 4
  slug: tenable-scan-exports-api
- baseURL: https://cloud.tenable.com
  baseurl_source: declared
  description: The Scan History API from Tenable — 2 operation(s) for scan history.
  name: Tenable Scan History API
  phrasing_intents:
  - id: scans-history
    intent: List a scan's run history
    question: How many times has a scan run and when?
  - id: scans-history-details
    intent: Get details of a past scan run
    question: What did a specific past run of my scan find?
  - id: scans-delete-history
    intent: Delete a past scan run
    question: Can I delete the results of one old scan run?
  phrasing_ops: 3
  slug: tenable-scan-history-api
- baseURL: https://cloud.tenable.com
  baseurl_source: declared
  description: The Scan Results API from Tenable — 3 operation(s) for scan results.
  name: Tenable Scan Results API
  phrasing_intents:
  - id: scans-host-details
    intent: Get a host's results from a scan
    question: What vulnerabilities did a scan find on a specific host?
  - id: scans-plugin-output
    intent: Get a plugin's output on a host (deprecated)
    question: Can I see the raw output a specific plugin produced on a host in a scan?
  - id: scans-attachments
    intent: Download a scan attachment file
    question: Can I download a file attached to a scan result?
  phrasing_ops: 3
  slug: tenable-scan-results-api
- baseURL: https://cloud.tenable.com
  baseurl_source: declared
  description: The Scan Status API from Tenable — 3 operation(s) for scan status.
  name: Tenable Scan Status API
  phrasing_intents:
  - id: scans-get-latest-status
    intent: Get a scan's latest status
    question: Is my scan still running, completed or aborted?
  - id: scans-read-status
    intent: Mark a scan as read or unread
    question: Can I mark a scan's results as read so it stops showing as new?
  - id: io-vm-scans-progress-get
    intent: Get a scan's progress
    question: How far along is a running scan, as a percentage?
  phrasing_ops: 3
  slug: tenable-scan-status-api
- baseURL: https://cloud.tenable.com
  baseurl_source: declared
  description: The Scan Tasks API from Tenable — 7 operation(s) for scan tasks.
  name: Tenable Scan Tasks API
  phrasing_intents:
  - id: scans-schedule
    intent: Enable or disable a scan schedule
    question: Can I pause a recurring scan's schedule without deleting the scan?
  - id: scans-copy
    intent: Copy a scan
    question: Can I duplicate an existing scan configuration?
  - id: io-scans-credentials-convert
    intent: Convert scan credentials to managed ones
    question: Can I turn a credential stored inside a scan into a reusable managed credential?
  - id: scans-import
    intent: Import a previously uploaded scan
    question: How do I import a .nessus file I already uploaded?
  - id: io-scans-count
    intent: Count scans in the container
    question: How many scans exist in my container?
  - id: scans-timezones
    intent: List timezones for scan schedules
    question: Which timezone values are valid for a recurring scan schedule?
  - id: io-scans-check-auto-targets
    intent: Test which scanner groups route targets
    question: Which scanner groups would pick up these targets under my scan routing?
  phrasing_ops: 7
  slug: tenable-scan-tasks-api
- baseURL: https://cloud.tenable.com
  baseurl_source: declared
  description: The Scanner Config API from Tenable — 1 operation(s) for scanner config.
  name: Tenable Scanner Config API
  phrasing_intents:
  - id: scanner-config-details
    intent: Get global scanner configuration
    question: What are my global scanner settings, like concurrent update limits?
  - id: scanner-config-edit
    intent: Update global scanner configuration
    question: Can I change how many scanners update concurrently?
  phrasing_ops: 2
  slug: tenable-scanner-config-api
- baseURL: https://cloud.tenable.com
  baseurl_source: declared
  description: The Scanner Groups API from Tenable — 5 operation(s) for scanner groups.
  name: Tenable Scanner Groups API
  phrasing_intents:
  - id: scanner-groups-create
    intent: Create a scanner group
    question: How do I create a new group to pool several scanners together?
  - id: scanner-groups-list
    intent: List scanner groups
    question: Which scanner groups exist in my Tenable Vulnerability Management instance?
  - id: scanner-groups-details
    intent: Get scanner group details
    question: What are the details of one particular scanner group?
  - id: scanner-groups-edit
    intent: Rename a scanner group
    question: How do I rename an existing scanner group?
  - id: scanner-groups-delete
    intent: Delete a scanner group
    question: How do I remove a scanner group I no longer use?
  - id: scanner-groups-list-scanners
    intent: List the scanners in a scanner group
    question: Which scanners belong to a given scanner group?
  - id: scanner-groups-add-scanner
    intent: Add a scanner to a scanner group
    question: How do I put a scanner into an existing scanner group?
  - id: scanner-groups-delete-scanner
    intent: Remove a scanner from a scanner group
    question: How do I take a scanner out of a scanner group without deleting the group?
  phrasing_ops: 10
  slug: tenable-scanner-groups-api
- baseURL: https://cloud.tenable.com
  baseurl_source: declared
  description: The Scanner Profiles API from Tenable — 2 operation(s) for scanner profiles.
  name: Tenable Scanner Profiles API
  phrasing_intents:
  - id: scanner-profile-assign-bulk
    intent: Assign scanners to a scanner profile
    question: How do I assign several scanners to a scanner profile at once?
  - id: scanner-profile-remove-bulk
    intent: Remove scanners from a scanner profile
    question: Can I remove multiple scanners from a scanner profile in one call?
  - id: scanner-task-status
    intent: Check a bulk scanner task's status
    question: Did my bulk scanner profile assignment finish?
  phrasing_ops: 3
  slug: tenable-scanner-profiles-api
- baseURL: https://cloud.tenable.com
  baseurl_source: declared
  description: The Scanner Tasks API from Tenable — 4 operation(s) for scanner tasks.
  name: Tenable Scanner Tasks API
  phrasing_intents:
  - id: io-scanners-directive
    intent: Send an instruction to one scanner
    question: Can I tell a single scanner to restart or change a setting remotely?
  - id: io-scanners-directive-bulk
    intent: Send an instruction to many scanners
    question: Can I send the same instruction to all my scanners at once?
  - id: scanners-control-scans
    intent: Control a scan running on a scanner
    question: Can I pause or stop a scan from the scanner it's running on?
  - id: scanners-toggle-link-state
    intent: Link or unlink a scanner
    question: Can I disable a scanner's link without deleting it?
  phrasing_ops: 4
  slug: tenable-scanner-tasks-api
- baseURL: https://cloud.tenable.com
  baseurl_source: declared
  description: The Scanners API from Tenable — 5 operation(s) for scanners.
  name: Tenable Scanners API
  phrasing_intents:
  - id: scanners-list
    intent: List scanners
    question: Which Nessus scanners are linked to my account?
  - id: scanners-details
    intent: Get a scanner's details
    question: What version and status is a particular scanner running?
  - id: scanners-edit
    intent: Update a scanner
    question: Can I force a scanner to update its plugins right away?
  - id: scanners-delete
    intent: Delete and unlink a scanner
    question: How do I unlink a scanner I've decommissioned?
  - id: scanners-get-scanner-key
    intent: Get a scanner's key
    question: Where do I find the key for a specific scanner?
  - id: scanners-get-aws-targets
    intent: List AWS targets of a scanner
    question: Which AWS instances can my AWS scanner target?
  - id: scanners-get-scans
    intent: List scans running on a scanner
    question: What scans are running on a particular scanner right now?
  phrasing_ops: 7
  slug: tenable-scanners-api
- baseURL: https://cloud.tenable.com
  baseurl_source: declared
  description: The Scans API from Tenable — 11 operation(s) for scans.
  name: Tenable Scans API
  phrasing_intents:
  - id: pci-scans-list
    intent: List PCI ASV scans
    question: Where can I see all of my PCI ASV compliance scans?
  - id: scans-create
    intent: Create a vulnerability scan configuration
    question: How do I create a new network vulnerability scan from a template?
  - id: scans-list
    intent: List vulnerability management scans
    question: Which vulnerability management scans can I view in my account?
  - id: scans-details
    intent: Get results of a vulnerability scan
    question: How can I see the results from the latest run of a scan?
  - id: scans-configure
    intent: Update a vulnerability scan's configuration
    question: Can I change the targets or schedule of an existing network scan?
  - id: scans-delete
    intent: Delete a vulnerability scan
    question: How do I delete a network scan I no longer need?
  - id: was-v2-scans-launch
    intent: Launch a web app scan from a configuration
    question: How do I start a web application scan from a saved scan configuration?
  - id: was-v3-scans-import
    intent: Import a previously exported web app scan
    question: Can I import a web app scan that I exported earlier as JSON?
  phrasing_ops: 17
  slug: tenable-scans-api
- baseURL: https://cloud.tenable.com
  baseurl_source: declared
  description: The directories' scores
  name: Tenable Score API
  phrasing_intents:
  - id: getApiProfilesByProfileIdScores
    intent: Get directory security scores
    question: What is the security score of each of my domains?
  phrasing_ops: 1
  slug: tenable-score-api
- baseURL: https://cloud.tenable.com
  baseurl_source: declared
  description: The Server API from Tenable — 2 operation(s) for server.
  name: Tenable Server API
  phrasing_intents:
  - id: server-status
    intent: Check server status
    question: Is the Tenable Vulnerability Management server up and ready?
  - id: server-properties
    intent: Get server version and properties
    question: Which server version am I connected to?
  phrasing_ops: 2
  slug: tenable-server-api
- baseURL: https://cloud.tenable.com
  baseurl_source: declared
  description: The Shared Collections API from Tenable — 5 operation(s) for shared collections.
  name: Tenable Shared Collections API
  phrasing_intents:
  - id: shared-collections-create
    intent: Create a shared collection
    question: How do I create a shared collection to group scans for other users?
  - id: shared-collections-list
    intent: List shared collections
    question: Which shared scan collections do I have access to?
  - id: shared-collections-details
    intent: Get a shared collection by ID
    question: What are the details and permissions of one shared collection?
  - id: shared-collections-update
    intent: Update a shared collection
    question: Can I rename a shared collection or change who it is shared with?
  - id: shared-collections-delete
    intent: Delete a shared collection
    question: How do I delete a shared collection I no longer use?
  - id: shared-collections-details-by-name
    intent: Look up a shared collection by name
    question: Can I find a shared collection if I only know its name?
  - id: shared-collections-job-status
    intent: Check a shared collection job's status
    question: Did my shared collection create, update or delete job finish?
  - id: shared-collections-config-add
    intent: Add scan configs to a shared collection
    question: How do I add scans to an existing shared collection?
  phrasing_ops: 10
  slug: tenable-shared-collections-api
- baseURL: https://cloud.tenable.com
  baseurl_source: declared
  description: A syslog alert
  name: Tenable Syslog API
  phrasing_intents:
  - id: getApiSyslogs
    intent: List syslog forwarders
    question: Where is Identity Exposure forwarding syslog alerts?
  - id: postApiSyslogs
    intent: Create a syslog forwarder
    question: How do I send alerts to my SIEM over syslog?
  - id: getApiSyslogsById
    intent: Get a syslog forwarder
    question: What host and port does a syslog forwarder send to?
  - id: patchApiSyslogsById
    intent: Update a syslog forwarder
    question: Can I change the IP and port a syslog forwarder targets?
  - id: deleteApiSyslogsById
    intent: Delete a syslog forwarder
    question: How do I stop forwarding to a syslog server?
  - id: getApiSyslogsTestMessageById
    intent: Send a test syslog for a saved forwarder
    question: How do I confirm an existing syslog forwarder reaches my SIEM?
  - id: postApiSyslogsTestMessage
    intent: Send a test syslog before saving
    question: Can I test syslog settings before creating the forwarder?
  phrasing_ops: 7
  slug: tenable-syslog-api
- baseURL: https://cloud.tenable.com
  baseurl_source: declared
  description: The Tenable Exposure Management tags API enables users to search for their organization's tags. Additionally, API endpoints are provided to retrieve a list of asset and tag properties that can be used
  name: Tenable Tags API
  phrasing_intents:
  - id: inventory-tag-search
    intent: Search tags with filters
    question: Can I search my organization's tags using filters and a text query?
  - id: inventory-tag-properties-list
    intent: List tag properties usable as search filters
    question: What tag properties can I filter on when searching tags?
  - id: tags-create-tag-category
    intent: Create a tag category
    question: How do I create a new category to group my asset tags?
  - id: tags-list-tag-categories
    intent: List tag categories
    question: What tag categories exist in my Tenable Vulnerability Management account?
  - id: tags-tag-category-details
    intent: Get details of one tag category
    question: What details are stored for a specific tag category?
  - id: tags-edit-tag-category
    intent: Rename or redescribe a tag category
    question: Can I rename an existing tag category?
  - id: tags-delete-tag-category
    intent: Delete a tag category and its values
    question: What happens to tag values and assets when I delete a whole tag category?
  - id: tags-create-tag-value
    intent: Create a tag value in a category
    question: How do I add a new tag value under a category?
  phrasing_ops: 17
  slug: tenable-tags-api
- baseURL: https://cloud.tenable.com
  baseurl_source: declared
  description: The Target Groups API from Tenable — 3 operation(s) for target groups.
  name: Tenable Target Groups API
  phrasing_intents:
  - id: target-groups-create
    intent: Create a target group (deprecated)
    question: Can I still create a target group of hosts to scan, even though they are deprecated?
  - id: target-groups-list
    intent: List target groups (deprecated)
    question: Which legacy target groups do I still have before migrating to tags?
  - id: target-groups-details
    intent: Get a target group's details (deprecated)
    question: Which hosts are in a specific legacy target group?
  - id: target-groups-edit
    intent: Update a target group (deprecated)
    question: How do I change the hosts in an existing target group?
  - id: target-groups-delete
    intent: Delete a target group (deprecated)
    question: How do I delete an old target group after moving to tags?
  phrasing_ops: 5
  slug: tenable-target-groups-api
- baseURL: https://cloud.tenable.com
  baseurl_source: declared
  description: With the Templates API, you can manage scan and user templates. Use these endpoints to retrieve default settings or create custom templates based on organizational policies. Templates serve as the blu
  name: Tenable Templates API
  phrasing_intents:
  - id: was-v2-templates-list
    intent: List Tenable-provided web app scan templates
    question: Which built-in templates can I base a web app scan configuration on?
  - id: was-v2-templates-details
    intent: Get a Tenable-provided web app scan template
    question: What settings does a built-in web app scan template include?
  - id: was-v2-user-templates-search
    intent: Search user-defined web app scan templates
    question: Which custom web app scan templates have users in my org created?
  - id: was-v2-user-templates-details
    intent: Get a user-defined web app scan template
    question: What's configured in one of our custom web app scan templates?
  - id: was-v2-user-templates-update
    intent: Update a user-defined web app scan template
    question: Can I change the settings or permissions of a custom web app scan template?
  - id: was-v2-user-templates-delete
    intent: Delete a user-defined web app scan template
    question: Why can't I delete a custom web app scan template?
  phrasing_ops: 6
  slug: tenable-templates-api
- baseURL: https://cloud.tenable.com
  baseurl_source: declared
  description: A graph to represent the trust relationships between different Active Directories
  name: Tenable Topology API
  phrasing_intents:
  - id: getApiProfilesByProfileIdTopology
    intent: Get the AD topology map
    question: How are my forests, domains and trusts connected?
  phrasing_ops: 1
  slug: tenable-topology-api
- baseURL: https://cloud.tenable.com
  baseurl_source: declared
  description: A Tenable.ad user
  name: Tenable User API
  phrasing_intents:
  - id: getApiUsers
    intent: List users
    question: Who has an account on Identity Exposure?
  - id: postApiUsers
    intent: Create a user
    question: How do I add a new user account?
  - id: getApiUsersWhoami
    intent: Show the signed-in user
    question: Which user am I authenticated as?
  - id: getApiUsersById
    intent: Get a user
    question: How do I look up a user by id?
  - id: patchApiUsersById
    intent: Update a user's profile or status
    question: Can I unlock a user who is locked out?
  - id: deleteApiUsersById
    intent: Delete a user
    question: How do I remove someone's account?
  - id: patchApiUsersPassword
    intent: Change my password
    question: How do I change my own password?
  - id: postApiLogin
    intent: Log in with email and password
    question: How do I sign in to Identity Exposure with my email?
  phrasing_ops: 10
  slug: tenable-user-api
- baseURL: https://cloud.tenable.com
  baseurl_source: declared
  description: The Vulnerabilities API from Tenable — 4 operation(s) for vulnerabilities.
  name: Tenable Vulnerabilities API
  phrasing_intents:
  - id: vulnerabilities-import
    intent: Import vulnerabilities (v1)
    question: How do I push third-party vulnerability findings into Vulnerability Management?
  - id: vulnerabilities-import-v2
    intent: Import vulnerabilities (v2)
    question: Can I import vulnerability data while naming the vendor and product that found it?
  - id: was-v2-vulns-details
    intent: Get a web app vulnerability instance
    question: What are the details of one specific web application vulnerability?
  - id: was-v2-vulns-search
    intent: Search web app vulnerabilities
    question: Which vulnerabilities have my web app scans found across all applications?
  phrasing_ops: 4
  slug: tenable-vulnerabilities-api
- baseURL: https://cloud.tenable.com
  baseurl_source: declared
  description: Contains a serie of data
  name: Tenable Widget API
  phrasing_intents:
  - id: getApiDashboardsByDashboardIdWidgets
    intent: List a dashboard's widgets
    question: Which widgets are on a dashboard?
  - id: postApiDashboardsByDashboardIdWidgets
    intent: Add a widget to a dashboard
    question: How do I place a new widget on a dashboard?
  - id: getApiDashboardsByDashboardIdWidgetsById
    intent: Get a widget
    question: How do I fetch one widget's layout?
  - id: patchApiDashboardsByDashboardIdWidgetsById
    intent: Move, resize or retitle a widget
    question: Can I resize a widget on a dashboard?
  - id: deleteApiDashboardsByDashboardIdWidgetsById
    intent: Delete a widget
    question: How do I remove a widget from a dashboard?
  - id: getApiDashboardsByDashboardIdWidgetsByIdOptions
    intent: Get a widget's data options
    question: What data series and filters does a widget display?
  - id: putApiDashboardsByDashboardIdWidgetsByIdOptions
    intent: Set a widget's data options
    question: How do I choose what data a widget charts?
  phrasing_ops: 7
  slug: tenable-widget-api
- baseURL: https://cloud.tenable.com
  baseurl_source: declared
  description: The Workbenches API from Tenable — 14 operation(s) for workbenches.
  name: Tenable Workbenches API
  phrasing_intents:
  - id: workbenches-vulnerabilities
    intent: List vulnerabilities in the workbench
    question: What vulnerabilities have been recorded across my environment?
  - id: workbenches-vulnerability-info
    intent: Get workbench details for a plugin
    question: What does the workbench know about a specific vulnerability plugin across my assets?
  - id: workbenches-vulnerability-output
    intent: List plugin outputs across assets
    question: Where can I see the raw plugin output a vulnerability check produced on my hosts?
  - id: workbenches-assets
    intent: List assets in the workbench
    question: Which assets does my vulnerability management workbench know about?
  - id: workbenches-assets-vulnerabilities
    intent: List assets that have vulnerabilities
    question: Which of my assets currently have vulnerabilities and how many?
  - id: workbenches-asset-info
    intent: Get information about an asset
    question: What does Tenable know about a specific asset, like its IPs and operating system?
  - id: workbenches-assets-activity
    intent: Get an asset's activity log
    question: When was an asset discovered, last seen or tagged?
  - id: workbenches-asset-vulnerabilities
    intent: List vulnerabilities on an asset
    question: What vulnerabilities are recorded on a particular host?
  phrasing_ops: 14
  slug: tenable-workbenches-api
artifact_total: 224
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Downloads About API
  slug: open-tenable-about-api
- collection_type: open
  name: Downloads About Access Control (API) API
  slug: open-tenable-access-control-api-api
- collection_type: open
  name: Downloads About Access Control (Groups) API
  slug: open-tenable-access-control-groups-api
- collection_type: open
  name: Downloads About Access Control (Permissions) API
  slug: open-tenable-access-control-permissions-api
- collection_type: open
  name: Downloads About Access Control (Roles) API
  slug: open-tenable-access-control-roles-api
- collection_type: open
  name: Downloads About Access Control (Users) API
  slug: open-tenable-access-control-users-api
- collection_type: open
  name: Downloads About Access Groups v1 API
  slug: open-tenable-access-groups-v1-api
- collection_type: open
  name: Downloads About Access Groups v2 API
  slug: open-tenable-access-groups-v2-api
- collection_type: open
  name: Downloads About Account Groups API
  slug: open-tenable-account-groups-api
- collection_type: open
  name: Downloads About Accounts API
  slug: open-tenable-accounts-api
- collection_type: open
  name: Downloads About Activity Log API
  slug: open-tenable-activity-log-api
- collection_type: open
  name: Downloads About AD object API
  slug: open-tenable-ad-object-api
- collection_type: open
  name: Downloads About Agent Config API
  slug: open-tenable-agent-config-api
- collection_type: open
  name: Downloads About Agent Exclusions API
  slug: open-tenable-agent-exclusions-api
- collection_type: open
  name: Downloads About Agent Groups API
  slug: open-tenable-agent-groups-api
- collection_type: open
  name: Downloads About Agent Tasks API
  slug: open-tenable-agent-tasks-api
- collection_type: open
  name: Downloads About Agents API
  slug: open-tenable-agents-api
- collection_type: open
  name: Downloads About Alert API
  slug: open-tenable-alert-api
- collection_type: open
  name: Downloads About API key API
  slug: open-tenable-api-key-api
- collection_type: open
  name: Downloads About Application setting API
  slug: open-tenable-application-setting-api
- collection_type: open
  name: Downloads About Applications API
  slug: open-tenable-applications-api
- collection_type: open
  name: Downloads About Asset Attributes API
  slug: open-tenable-asset-attributes-api
- collection_type: open
  name: Downloads About Assets API
  slug: open-tenable-assets-api
- collection_type: open
  name: Downloads About Attachments API
  slug: open-tenable-attachments-api
- collection_type: open
  name: Downloads About Attack API
  slug: open-tenable-attack-api
- collection_type: open
  name: Downloads About Attack Path API
  slug: open-tenable-attack-path-api
- collection_type: open
  name: Downloads About Attack Path Exports API
  slug: open-tenable-attack-path-exports-api
- collection_type: open
  name: Downloads About Attack type API
  slug: open-tenable-attack-type-api
- collection_type: open
  name: Downloads About Attack type configuration API
  slug: open-tenable-attack-type-configuration-api
- collection_type: open
  name: Downloads About Attack type option API
  slug: open-tenable-attack-type-option-api
- collection_type: open
  name: Downloads About Attestations API
  slug: open-tenable-attestations-api
- collection_type: open
  name: Downloads About Category API
  slug: open-tenable-category-api
- collection_type: open
  name: Downloads About Checker API
  slug: open-tenable-checker-api
- collection_type: open
  name: Downloads About Checker option API
  slug: open-tenable-checker-option-api
- collection_type: open
  name: Downloads About Child Containers API
  slug: open-tenable-child-containers-api
- collection_type: open
  name: Downloads About Cloud Connectors API
  slug: open-tenable-cloud-connectors-api
- collection_type: open
  name: Downloads About Cloud statistics API
  slug: open-tenable-cloud-statistics-api
- collection_type: open
  name: Downloads About Configurations API
  slug: open-tenable-configurations-api
- collection_type: open
  name: Downloads About Credentials API
  slug: open-tenable-credentials-api
- collection_type: open
  name: Downloads About Dashboard API
  slug: open-tenable-dashboard-api
- collection_type: open
  name: Downloads About Dashboards API
  slug: open-tenable-dashboards-api
- collection_type: open
  name: Downloads About Deviance API
  slug: open-tenable-deviance-api
- collection_type: open
  name: Downloads About Directory API
  slug: open-tenable-directory-api
- collection_type: open
  name: Downloads About Domains API
  slug: open-tenable-domains-api
- collection_type: open
  name: About Downloads API
  slug: open-tenable-downloads-api
- collection_type: open
  name: Downloads About Editor API
  slug: open-tenable-editor-api
- collection_type: open
  name: Downloads About Email notifier API
  slug: open-tenable-email-notifier-api
- collection_type: open
  name: Downloads About Event API
  slug: open-tenable-event-api
- collection_type: open
  name: Downloads About Exclusions API
  slug: open-tenable-exclusions-api
- collection_type: open
  name: Downloads About Exports API
  slug: open-tenable-exports-api
- collection_type: open
  name: Downloads About Exports (Assets) API
  slug: open-tenable-exports-assets-api
- collection_type: open
  name: Downloads About Exports (Compliance Data) API
  slug: open-tenable-exports-compliance-data-api
- collection_type: open
  name: Downloads About Exports (Vulnerabilities) API
  slug: open-tenable-exports-vulnerabilities-api
- collection_type: open
  name: Downloads About Exposure View API
  slug: open-tenable-exposure-view-api
- collection_type: open
  name: Downloads About File API
  slug: open-tenable-file-api
- collection_type: open
  name: Downloads About Filters API
  slug: open-tenable-filters-api
- collection_type: open
  name: Downloads About Folders API
  slug: open-tenable-folders-api
- collection_type: open
  name: Downloads About Infrastructure API
  slug: open-tenable-infrastructure-api
- collection_type: open
  name: Downloads About Inventory API
  slug: open-tenable-inventory-api
- collection_type: open
  name: Downloads About Inventory Exports API
  slug: open-tenable-inventory-exports-api
- collection_type: open
  name: Downloads About LDAP configuration API
  slug: open-tenable-ldap-configuration-api
- collection_type: open
  name: Downloads About License API
  slug: open-tenable-license-api
- collection_type: open
  name: Downloads About Lockout policy API
  slug: open-tenable-lockout-policy-api
- collection_type: open
  name: Downloads About Logos API
  slug: open-tenable-logos-api
- collection_type: open
  name: Downloads About Metrics API
  slug: open-tenable-metrics-api
- collection_type: open
  name: Downloads About Networks API
  slug: open-tenable-networks-api
- collection_type: open
  name: Downloads About OT Connectors API
  slug: open-tenable-ot-connectors-api
- collection_type: open
  name: Downloads About Partners API
  slug: open-tenable-partners-api
- collection_type: open
  name: Downloads About Permissions API
  slug: open-tenable-permissions-api
- collection_type: open
  name: Downloads About Plugins API
  slug: open-tenable-plugins-api
- collection_type: open
  name: Downloads About Policies API
  slug: open-tenable-policies-api
- collection_type: open
  name: Downloads About Preference API
  slug: open-tenable-preference-api
- collection_type: open
  name: Downloads About Profile API
  slug: open-tenable-profile-api
- collection_type: open
  name: Downloads About Profiles API
  slug: open-tenable-profiles-api
- collection_type: open
  name: Downloads About Reason API
  slug: open-tenable-reason-api
- collection_type: open
  name: Downloads About Recast Rules API
  slug: open-tenable-recast-rules-api
- collection_type: open
  name: Downloads About Relay API
  slug: open-tenable-relay-api
- collection_type: open
  name: Downloads About Remediation Scans API
  slug: open-tenable-remediation-scans-api
- collection_type: open
  name: Downloads About Report access token API
  slug: open-tenable-report-access-token-api
- collection_type: open
  name: Downloads About Reports API
  slug: open-tenable-reports-api
- collection_type: open
  name: Downloads About Resource Links API
  slug: open-tenable-resource-links-api
- collection_type: open
  name: Downloads About Role API
  slug: open-tenable-role-api
- collection_type: open
  name: Downloads About SAML configuration API
  slug: open-tenable-saml-configuration-api
- collection_type: open
  name: Downloads About Scan Control API
  slug: open-tenable-scan-control-api
- collection_type: open
  name: Downloads About Scan Exports API
  slug: open-tenable-scan-exports-api
- collection_type: open
  name: Downloads About Scan History API
  slug: open-tenable-scan-history-api
- collection_type: open
  name: Downloads About Scan Results API
  slug: open-tenable-scan-results-api
- collection_type: open
  name: Downloads About Scan Status API
  slug: open-tenable-scan-status-api
- collection_type: open
  name: Downloads About Scan Tasks API
  slug: open-tenable-scan-tasks-api
- collection_type: open
  name: Downloads About Scanner Config API
  slug: open-tenable-scanner-config-api
- collection_type: open
  name: Downloads About Scanner Groups API
  slug: open-tenable-scanner-groups-api
- collection_type: open
  name: Downloads About Scanner Profiles API
  slug: open-tenable-scanner-profiles-api
- collection_type: open
  name: Downloads About Scanner Tasks API
  slug: open-tenable-scanner-tasks-api
- collection_type: open
  name: Downloads About Scanners API
  slug: open-tenable-scanners-api
- collection_type: open
  name: Downloads About Scans API
  slug: open-tenable-scans-api
- collection_type: open
  name: Downloads About Score API
  slug: open-tenable-score-api
- collection_type: open
  name: Downloads About Server API
  slug: open-tenable-server-api
- collection_type: open
  name: Downloads About Shared Collections API
  slug: open-tenable-shared-collections-api
- collection_type: open
  name: Downloads About Syslog API
  slug: open-tenable-syslog-api
- collection_type: open
  name: Downloads About Tags API
  slug: open-tenable-tags-api
- collection_type: open
  name: Downloads About Target Groups API
  slug: open-tenable-target-groups-api
- collection_type: open
  name: Downloads About Templates API
  slug: open-tenable-templates-api
- collection_type: open
  name: Downloads About Topology API
  slug: open-tenable-topology-api
- collection_type: open
  name: Downloads About User API
  slug: open-tenable-user-api
- collection_type: open
  name: Downloads About Vulnerabilities API
  slug: open-tenable-vulnerabilities-api
- collection_type: open
  name: Downloads About Widget API
  slug: open-tenable-widget-api
- collection_type: open
  name: Downloads About Workbenches API
  slug: open-tenable-workbenches-api
common:
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/tenable/refs/heads/main/rate-limits/tenable-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/tenable-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/tenable/refs/heads/main/plans/tenable-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/tenable-plans-pricing.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/tenable/refs/heads/main/capabilities/tenable-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/tenable-capability-edges.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/tenable/refs/heads/main/overlays/tenable-downloads-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/tenable-downloads-api-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.tenable.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.tenable.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.tenable.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.tenable.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.tenable.com/docs/welcome
- group: operate
  title: ''
  type: Support
  url: https://www.tenable.com/support
- group: company
  title: ''
  type: Blog
  url: https://www.tenable.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tenable
- group: commercial
  title: ''
  type: Pricing
  url: https://www.tenable.com/buy
- group: start
  title: ''
  type: SignUp
  url: https://www.tenable.com/evaluate
- group: start
  title: ''
  type: Login
  url: https://cloud.tenable.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.tenable.com/legal
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.tenable.com/privacy-policy
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/tenable/refs/heads/main/changelog/tenable-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/tenable-changelog.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.tenable.com
- group: operate
  title: ''
  type: Deprecation
  url: https://developer.tenable.com/changelog
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/tenable/refs/heads/main/lifecycle/tenable-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/tenable-lifecycle.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/tenable/refs/heads/main/authentication/tenable-authentication.yml
  title: ''
  type: Authentication
  url: authentication/tenable-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/tenable/refs/heads/main/conventions/tenable-conventions.yml
  title: ''
  type: Conventions
  url: conventions/tenable-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/tenable/refs/heads/main/errors/tenable-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/tenable-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/tenable/refs/heads/main/data-model/tenable-data-model.yml
  title: ''
  type: DataModel
  url: data-model/tenable-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/tenable/refs/heads/main/conformance/tenable-conformance.yml
  title: ''
  type: Conformance
  url: conformance/tenable-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.tenable.com/trust/assurance
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/tenable/refs/heads/main/security/tenable-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/tenable-trust-center.yml
- group: auth
  title: ''
  type: Security
  url: https://www.tenable.com/security/report
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/tenable/refs/heads/main/security/tenable-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/tenable-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/tenable/refs/heads/main/security/tenable-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/tenable-domain-security.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/tenable/refs/heads/main/well-known/tenable-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/tenable-well-known.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/tenable/refs/heads/main/packages/tenable-packages.yml
  title: ''
  type: Packages
  url: packages/tenable-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/tenable/refs/heads/main/packages/tenable-packages.yml
  title: ''
  type: SDKs
  url: packages/tenable-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/tenable/refs/heads/main/mcp/tenable-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/tenable-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/tenable/refs/heads/main/llms/tenable-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/tenable-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/tenable/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/tenable/refs/heads/main/agentic-access/tenable-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/tenable-agentic-access.yml
created: '2026-07-17'
description: Tenable is a cybersecurity and exposure-management company, maker of Nessus and the Tenable One platform, providing vulnerability management, web application scanning, cloud security, identity exposure, attack surface management and OT security. Its developer platform (developer.tenable.com) exposes eight OpenAPI 3 REST APIs on cloud.tenable.com covering Vulnerability Management, Web App Scanning, Exposure Management, Platform & Settings, PCI ASV, MSSP, Identity Exposure and Downloads, all authenticated with X-ApiKeys access/secret keys, plus the official pyTenable SDK and a Tenable-hosted Hexa AI MCP server.
image: https://www.tenable.com/sites/all/themes/tenable/logo.svg
layout: provider
mcp_servers:
- description: Tenable-hosted remote MCP server exposing ~90 structured tools from Tenable's Exposure Data Fabric to any MCP-compatible client (Claude Desktop, Claude Code, Cursor). Lets an AI assistant search asset
  name: Tenable Hexa AI MCP Server
  slug: tenable-hexa-ai-mcp-server
modified: '2026-07-21'
name: Tenable
nav: Providers
network: true
overview: 'Tenable publishes 107 APIs on the [APIs.io](https://apis.io/) network, including About API, Access Control (API) API, Access Control (Groups) API, and 104 more. Tagged areas include Company, Enterprise, Cybersecurity, Vulnerability Management, and Exposure Management.


  Tenable''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 31 more developer resources.'
plans:
- name: Tenable Plans Pricing
  plan_count: 15
  slug: tenable-plans-pricing
- name: Tenable Price Estimates
  plan_count: 0
  slug: tenable-price-estimates
random_paper: 5
rate_limits:
- limit_count: 8
  name: Tenable Rate Limits
  slug: tenable-rate-limits
score:
  band: exemplar
  composite: 67.5
  coverage:
    artifact_dirs: 23
    catalog_earned: 64.0
    catalog_earned_first_party: 24.0
    catalog_gap: 51.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 92.1
    contract_governance: 4.5
    contract_quality: 53.6
    developer_ergonomics: 61.3
    discoverability: 80.0
    operational_transparency: 80.3
  previous_composite: 67.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 107
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: US
      standard: fedramp
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 35.3
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  trend: flat
  upsert:
    applies: true
    score: 22.2
screenshot: https://raw.githubusercontent.com/api-evangelist/tenable/refs/heads/main/screenshots/tenable-2026-08-17T082310.png
security:
- kind: authentication
  name: Tenable Authentication
  slug: tenable-authentication
  summary_line: apiKey · 3 schemes
- kind: domain-security
  name: Tenable Domain Security
  slug: tenable-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Tenable Vulnerability Disclosure
  slug: tenable-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Tenable Trust Center
  slug: tenable-trust-center
  summary_line: SOC 2, ISO/IEC 27001:2022, FedRAMP (Tenable One VM + Web App Scanning, ATO 2021), StateRAMP (Tenable One VM, Authorized), CSA STAR, NIAP (Security Center, Nessus Manager, Nessus Network Monitor, Nessus Agent), Privacy Shield Framework
slug: tenable
tags:
- Company
- Enterprise
- Cybersecurity
- Vulnerability Management
- Exposure Management
- Security
- Cloud Security
- Attack Surface Management
website: https://www.tenable.com
---
