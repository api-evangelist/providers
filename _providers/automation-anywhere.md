---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
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
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 52.4
  scored_at: '2026-10-03'
agentic_access:
- acting_count: 42
  human_in_the_loop: 0
  name: Automation Anywhere Agentic Access
  operation_count: 69
  slug: automation-anywhere-agentic-access
  summary_line: 69 operations · 42 acting
api_count: 7
apis:
- description: The Automation Anywhere Package SDK is a Java-based development toolkit that enables developers to build custom action packages and triggers for the Automation 360 bot editor. Developers use the SDK i
  name: Automation Anywhere Package SDK
  slug: package-sdk
- baseURL: https://{controlRoomUrl}/orchestrator/v1/hotbot
  baseurl_source: declared
  description: Generate execution URLs and authorization tokens for API Tasks
  name: automation-anywhere AccessDetails API
  phrasing_intents:
  - id: generateApiTaskAccessDetails
    intent: Generate an execution URL and token for API Tasks
    question: Can I get a direct URL to invoke an API Task without the normal Control Room login?
  phrasing_ops: 1
  slug: automation-anywhere-accessdetails-api
- baseURL: https://{controlRoomUrl}/orchestrator/v1/hotbot
  baseurl_source: declared
  description: List and manage API Task allocations within the Control Room
  name: automation-anywhere Allocations API
  phrasing_intents:
  - id: listApiTaskAllocations
    intent: List API Tasks allocated for real-time execution
    question: Which API Tasks have been allocated for real-time execution in my Control Room?
  phrasing_ops: 1
  slug: automation-anywhere-allocations-api
- baseURL: https://{controlRoomUrl}/v2/botinsight/data/api
  baseurl_source: declared
  description: Retrieve Control Room audit trail data
  name: automation-anywhere AuditData API
  phrasing_intents:
  - id: getAuditTrailData
    intent: Export Control Room audit trail records
    question: Which user logins, bot deployments and role changes were recorded in the Control Room audit trail?
  phrasing_ops: 1
  slug: automation-anywhere-auditdata-api
- baseURL: https://{controlRoomUrl}
  baseurl_source: declared
  description: Generate, refresh, validate, and revoke JWT tokens for API access
  name: automation-anywhere Authentication API
  phrasing_intents:
  - id: authenticate
    intent: Log in and get a JWT for the Control Room API
    question: How do I get an access token to call the Automation Anywhere Control Room API?
  - id: validateToken
    intent: Check whether a JWT is still valid
    question: Is my current Control Room JWT still valid or has it expired?
  - id: logout
    intent: Log out and invalidate the current JWT
    question: Can I immediately invalidate my API token when my script finishes?
  phrasing_ops: 3
  slug: automation-anywhere-authentication-api
- baseURL: https://{controlRoomUrl}/v2/botinsight/data/api
  baseurl_source: declared
  description: Retrieve bot execution run data and performance metrics
  name: automation-anywhere BotRunData API
  phrasing_intents:
  - id: getBotRunData
    intent: Export bot execution run records
    question: Which bots ran on which devices, and did they succeed or fail, since a given date?
  phrasing_ops: 1
  slug: automation-anywhere-botrundata-api
- baseURL: https://{controlRoomUrl}/v2/credentialvault
  baseurl_source: declared
  description: Create, retrieve, update, delete, and search credentials
  name: automation-anywhere Credentials API
  phrasing_intents:
  - id: createCredential
    intent: Create a credential in the Credential Vault
    question: How do I add a new username and password credential to the Credential Vault?
  - id: listCredentials
    intent: Search credentials I own or can access
    question: Which credentials do I own or have access to through a Locker?
  - id: getCredential
    intent: Get a credential and its attributes
    question: What attributes and current values does a specific credential have?
  - id: updateCredential
    intent: Rename or redefine a credential
    question: Can I rename a credential or change its description after creating it?
  - id: deleteCredential
    intent: Delete a credential from the Credential Vault
    question: Can I permanently delete a credential and all its stored values?
  - id: updateCredentialOwner
    intent: Transfer a credential to a new owner
    question: Can I hand ownership of a credential over to another user?
  phrasing_ops: 6
  slug: automation-anywhere-credentials-api
- baseURL: https://{controlRoomUrl}/v4
  baseurl_source: declared
  description: Deploy bots to Bot Runner devices and monitor deployment status
  name: automation-anywhere Deployments API
  phrasing_intents:
  - id: deployBot
    intent: Deploy a bot to Bot Runner devices
    question: How do I run a bot from the public workspace on a Bot Runner through the API?
  phrasing_ops: 1
  slug: automation-anywhere-deployments-api
- baseURL: https://{controlRoomUrl}/v2/repository
  baseurl_source: declared
  description: Manage individual bot files and their dependencies in the repository
  name: automation-anywhere Files API
  phrasing_intents:
  - id: listFiles
    intent: Search bots and files across the repository
    question: Which bots and files are stored in the repository, and where are they?
  - id: downloadFile
    intent: Download a repository file's contents
    question: Can I download the raw contents of a bot file from the repository?
  - id: getFileDependencies
    intent: View the files a bot depends on
    question: What other bots and templates does this bot depend on before I export it?
  - id: updateFileDependencies
    intent: Set a bot's manual dependencies in a workspace
    question: Can I declare a bot's dependencies by hand when automatic detection misses some?
  - id: getFileParents
    intent: Find the parent folder of a file
    question: Which folder is a given bot file stored in?
  - id: deleteFile
    intent: Delete a file from the repository
    question: Can a deleted repository file be recovered through the API?
  - id: updatePackageVersions
    intent: Bulk-update package versions used by bots
    question: After a platform upgrade, can I update all my bots to the latest package versions at once?
  - id: assignVersionLabel
    intent: Mark a bot version as production
    question: Can I mark one version of a bot as the production-ready version?
  phrasing_ops: 9
  slug: automation-anywhere-files-api
- baseURL: https://{controlRoomUrl}/v2/repository
  baseurl_source: declared
  description: Create, update, list, and delete folders in the repository
  name: automation-anywhere Folders API
  phrasing_intents:
  - id: createFolder
    intent: Create a new folder in the repository
    question: How do I make a new subfolder under an existing repository folder?
  - id: updateFolder
    intent: Rename or redescribe a repository folder
    question: Can I rename an existing folder in the bot repository?
  - id: deleteFolder
    intent: Delete a folder and everything in it
    question: Does deleting a repository folder also delete all its subfolders and bots?
  - id: listFolderContents
    intent: List the files and subfolders in a folder
    question: What bots and subfolders are inside a specific repository folder?
  phrasing_ops: 4
  slug: automation-anywhere-folders-api
- baseURL: https://{controlRoomUrl}/v2/credentialvault
  baseurl_source: declared
  description: Manage roles with consumer access to locker credentials
  name: automation-anywhere LockerConsumers API
  phrasing_intents:
  - id: listLockerConsumers
    intent: List roles with consumer access to a locker
    question: Which roles can let bots use the credentials in a given Locker?
  - id: addLockerConsumer
    intent: Grant a role consumer access to a locker
    question: How do I let bots under a role retrieve credentials from a Locker?
  - id: removeLockerConsumer
    intent: Revoke a role's consumer access to a locker
    question: Can I stop a role's bots from pulling credentials out of a Locker?
  phrasing_ops: 3
  slug: automation-anywhere-lockerconsumers-api
- baseURL: https://{controlRoomUrl}/v2/credentialvault
  baseurl_source: declared
  description: Manage user membership within lockers
  name: automation-anywhere LockerMembers API
  phrasing_intents:
  - id: listLockerMembers
    intent: List the members of a locker
    question: Which users are members of a given Locker?
  - id: updateLockerMember
    intent: Add a locker member or change their permissions
    question: Can I add a user as a member of a Locker?
  - id: removeLockerMember
    intent: Remove a user from a locker's members
    question: Can I take away a user's ability to manage a Locker?
  phrasing_ops: 3
  slug: automation-anywhere-lockermembers-api
- baseURL: https://{controlRoomUrl}/v2/credentialvault
  baseurl_source: declared
  description: Create, retrieve, update, and delete credential lockers
  name: automation-anywhere Lockers API
  phrasing_intents:
  - id: createLocker
    intent: Create a locker in the Credential Vault
    question: How do I create a Locker to group credentials for bots?
  - id: listLockers
    intent: Search lockers I have access to
    question: Which Lockers do I have access to?
  - id: getLocker
    intent: Get a locker's details
    question: What are the name, description and configuration of a specific Locker?
  - id: updateLocker
    intent: Rename or redescribe a locker
    question: Can I rename an existing Locker?
  - id: deleteLocker
    intent: Delete a locker
    question: Are the credentials deleted when I delete their Locker?
  - id: listLockerCredentials
    intent: List the credentials inside a locker
    question: Which credentials are stored in a particular Locker?
  - id: updateLockerCredential
    intent: Change which credential attributes a locker exposes
    question: Can I limit which attributes of a credential are exposed to consumer roles through a Locker?
  - id: removeLockerCredential
    intent: Remove a credential from a locker
    question: Can I take a credential out of a Locker without deleting it from the vault?
  phrasing_ops: 8
  slug: automation-anywhere-lockers-api
- baseURL: https://{controlRoomUrl}/v2/repository
  baseurl_source: declared
  description: Manage role-based permissions on repository folders
  name: automation-anywhere Permissions API
  phrasing_intents:
  - id: getRolePermissionsForFolder
    intent: View a role's permissions on a folder
    question: 'What can a given role do in a specific repository folder: view, run, upload, delete?'
  - id: updateRolePermissions
    intent: Grant a role permissions on repository folders
    question: Can I give a role access to specific folders with fine-grained actions?
  phrasing_ops: 2
  slug: automation-anywhere-permissions-api
- baseURL: https://{controlRoomUrl}/v4/wlm
  baseurl_source: declared
  description: Create and manage work item queues and their members
  name: automation-anywhere Queues API
  phrasing_intents:
  - id: getQueue
    intent: Get a work item queue's details
    question: What is the configuration and status of a specific work item queue?
  - id: addQueueConsumer
    intent: Add a role as a queue consumer
    question: How do I let bots under a role process work items from a queue?
  - id: addOrUpdateQueueMember
    intent: Add or change a queue member
    question: Can I make a user an owner or member of a work item queue?
  - id: addQueueParticipant
    intent: Add a participant to a queue
    question: Can I give someone view-only style access to a queue's status and work items?
  phrasing_ops: 4
  slug: automation-anywhere-queues-api
- baseURL: https://{controlRoomUrl}
  baseurl_source: declared
  description: Create, list, retrieve, update, and delete user roles
  name: automation-anywhere Roles API
  phrasing_intents:
  - id: createRole
    intent: Create a Control Room role
    question: How do I create a new role with its own set of permissions?
  - id: listRoles
    intent: List Control Room roles
    question: Which roles exist in my Control Room?
  - id: getRole
    intent: Get a role's details and members
    question: What permissions does a specific role grant?
  - id: updateRole
    intent: Update a role's name or permissions
    question: Can I change the permissions of an existing role?
  - id: deleteRole
    intent: Delete a Control Room role
    question: Can I delete a custom role, and what happens to its users?
  phrasing_ops: 5
  slug: automation-anywhere-roles-api
- baseURL: https://{controlRoomUrl}
  baseurl_source: declared
  description: Create, list, retrieve, update, and delete Control Room users
  name: automation-anywhere Users API
  phrasing_intents:
  - id: createUser
    intent: Create a Control Room user
    question: How do I add a new user to the Control Room through the API?
  - id: listUsers
    intent: List Control Room users
    question: Which users are in my Control Room and what roles do they have?
  - id: getUser
    intent: Get a user's details
    question: What roles, licenses and account status does a particular user have?
  - id: updateUser
    intent: Update a user's details, roles or status
    question: Can I disable a user account without deleting it?
  - id: deleteUser
    intent: Delete a Control Room user
    question: Can a deleted user account be restored?
  phrasing_ops: 5
  slug: automation-anywhere-users-api
- baseURL: https://{controlRoomUrl}/v4/wlm
  baseurl_source: declared
  description: Create and retrieve work item data models defining queue schema
  name: automation-anywhere WorkItemModels API
  phrasing_intents:
  - id: createWorkItemModel
    intent: Create a work item model
    question: How do I define the data schema for work items in a queue?
  - id: getWorkItemModel
    intent: Get a work item model's schema
    question: What attributes make up an existing work item model?
  phrasing_ops: 2
  slug: automation-anywhere-workitemmodels-api
- baseURL: https://{controlRoomUrl}/v2/repository
  baseurl_source: declared
  description: List and manage content across public and private workspaces
  name: automation-anywhere Workspaces API
  phrasing_intents:
  - id: listWorkspaceFiles
    intent: List files in the public or private workspace
    question: Which bots are in my private workspace versus the shared public one?
  phrasing_ops: 1
  slug: automation-anywhere-workspaces-api
- baseURL: https://{controlRoomUrl}
  baseurl_source: declared
  description: Manage credential attribute values for individual credentials
  name: Automation Anywhere Attribute Values API
  phrasing_intents:
  - id: listCredentialAttributeValues
    intent: List a credential's attribute values
    question: What values are currently stored on each attribute of a Credential Vault credential?
  - id: createCredentialAttributeValues
    intent: Set new attribute values on a credential
    question: Where do I store the actual password or secret for a credential's attribute definitions?
  - id: updateCredentialAttributeValue
    intent: Rotate one stored attribute value on a credential
    question: Can I rotate a password on an existing credential without changing its structure?
  - id: deleteCredentialAttributeValue
    intent: Remove a stored attribute value from a credential
    question: Can I wipe one stored secret from a credential but keep the attribute definition?
  phrasing_ops: 4
  slug: automation-anywhere-attribute-values-api
- baseURL: https://{controlRoomUrl}
  baseurl_source: declared
  description: Retrieve task metadata, variable profiles, and task-level logs
  name: Automation Anywhere Task Data API
  phrasing_intents:
  - id: getTaskMetadata
    intent: Get a bot task's analytics metadata
    question: Which KPI variables and dimensions are configured for a bot task in Bot Insight?
  - id: getTaskVariableProfile
    intent: Get aggregated KPI values for a bot task
    question: What were the aggregated KPI values for a bot task over a date range?
  - id: getTaskLogData
    intent: Export per-run log data for a bot task
    question: Can I extract raw per-run KPI values for a bot task into my data warehouse?
  phrasing_ops: 3
  slug: automation-anywhere-task-data-api
- baseURL: https://{controlRoomUrl}
  baseurl_source: declared
  description: Add, update, and manage individual work items within queues
  name: Automation Anywhere Work Items API
  phrasing_intents:
  - id: updateWorkItem
    intent: Update a work item's status or result
    question: Can I mark a work item in a queue as complete, failed or deferred?
  - id: createWorkItemsFromFile
    intent: Bulk-create work items from a CSV or Excel file
    question: Can I load many work items into a queue from a spreadsheet?
  phrasing_ops: 2
  slug: automation-anywhere-work-items-api
artifact_total: 169
asyncapis:
- description: ''
  name: Automation Anywhere Webhooks
  slug: automation-anywhere-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Automation Anywhere API Task Execution AccessDetails API
  slug: open-automation-anywhere-accessdetails-api
- collection_type: open
  name: Automation Anywhere API Task Execution AccessDetails Allocations API
  slug: open-automation-anywhere-allocations-api
- collection_type: open
  name: Automation Anywhere API Task Execution API
  slug: open-automation-anywhere-api-task-execution
- collection_type: open
  name: Automation Anywhere API Task Execution AccessDetails AttributeValues API
  slug: open-automation-anywhere-attributevalues-api
- collection_type: open
  name: Automation Anywhere API Task Execution AccessDetails AuditData API
  slug: open-automation-anywhere-auditdata-api
- collection_type: open
  name: Automation Anywhere API Task Execution AccessDetails Authentication API
  slug: open-automation-anywhere-authentication-api
- collection_type: open
  name: Automation Anywhere Bot Deploy API
  slug: open-automation-anywhere-bot-deploy
- collection_type: open
  name: Automation Anywhere Bot Insight API
  slug: open-automation-anywhere-bot-insight
- collection_type: open
  name: Automation Anywhere API Task Execution AccessDetails BotRunData API
  slug: open-automation-anywhere-botrundata-api
- collection_type: open
  name: Automation Anywhere Control Room API
  slug: open-automation-anywhere-control-room
- collection_type: open
  name: Automation Anywhere Credential Vault API
  slug: open-automation-anywhere-credential-vault
- collection_type: open
  name: Automation Anywhere API Task Execution AccessDetails Credentials API
  slug: open-automation-anywhere-credentials-api
- collection_type: open
  name: Automation Anywhere API Task Execution AccessDetails Deployments API
  slug: open-automation-anywhere-deployments-api
- collection_type: open
  name: Automation Anywhere API Task Execution AccessDetails Files API
  slug: open-automation-anywhere-files-api
- collection_type: open
  name: Automation Anywhere API Task Execution AccessDetails Folders API
  slug: open-automation-anywhere-folders-api
- collection_type: open
  name: Automation Anywhere API Task Execution AccessDetails LockerConsumers API
  slug: open-automation-anywhere-lockerconsumers-api
- collection_type: open
  name: Automation Anywhere API Task Execution AccessDetails LockerMembers API
  slug: open-automation-anywhere-lockermembers-api
- collection_type: open
  name: Automation Anywhere API Task Execution AccessDetails Lockers API
  slug: open-automation-anywhere-lockers-api
- collection_type: open
  name: Automation Anywhere API Task Execution AccessDetails Permissions API
  slug: open-automation-anywhere-permissions-api
- collection_type: open
  name: Automation Anywhere API Task Execution AccessDetails Queues API
  slug: open-automation-anywhere-queues-api
- collection_type: open
  name: Automation Anywhere Repository Management API
  slug: open-automation-anywhere-repository-management
- collection_type: open
  name: Automation Anywhere API Task Execution AccessDetails Roles API
  slug: open-automation-anywhere-roles-api
- collection_type: open
  name: Automation Anywhere API Task Execution AccessDetails TaskData API
  slug: open-automation-anywhere-taskdata-api
- collection_type: open
  name: Automation Anywhere API Task Execution AccessDetails Users API
  slug: open-automation-anywhere-users-api
- collection_type: open
  name: Automation Anywhere API Task Execution AccessDetails WorkItemModels API
  slug: open-automation-anywhere-workitemmodels-api
- collection_type: open
  name: Automation Anywhere API Task Execution AccessDetails WorkItems API
  slug: open-automation-anywhere-workitems-api
- collection_type: open
  name: Automation Anywhere Workload Management API
  slug: open-automation-anywhere-workload-management
- collection_type: open
  name: Automation Anywhere API Task Execution AccessDetails Workspaces API
  slug: open-automation-anywhere-workspaces-api
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/automation-anywhere/refs/heads/main/overlays/automation-anywhere-attribute-values-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/automation-anywhere-attribute-values-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/automation-anywhere/refs/heads/main/overlays/automation-anywhere-task-data-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/automation-anywhere-task-data-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/automation-anywhere/refs/heads/main/overlays/automation-anywhere-work-items-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/automation-anywhere-work-items-api-overlay.yaml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/automation-anywhere/refs/heads/main/rules/automation-anywhere-jsonschema-spectral-rules.yml
  title: ''
  type: Rules
  url: rules/automation-anywhere-jsonschema-spectral-rules.yml
- group: operate
  title: ''
  type: SLA
  url: https://www.automationanywhere.com/legal/uptime-availability-sla
- group: start
  title: ''
  type: DeveloperPortal
  url: https://pathfinder.automationanywhere.com/
- group: operate
  title: ''
  type: Community
  url: https://apeople.automationanywhere.com/
- group: start
  title: ''
  type: SignUp
  url: https://www.automationanywhere.com/products/enterprise/community-edition
- group: start
  title: ''
  type: GettingStarted
  url: https://ai-kb.automationanywhere.com/getting-started/create-first-agent
- group: docs
  title: ''
  type: APIReference
  url: https://docs.automationanywhere.com/r/control-room-apis/cloud-control-room-apis
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/automation-anywhere/refs/heads/main/vocabulary/automation-anywhere-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/automation-anywhere-vocabulary.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/automation-anywhere/refs/heads/main/finops/automation-anywhere-finops.yml
  title: ''
  type: FinOps
  url: finops/automation-anywhere-finops.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/automation-anywhere/refs/heads/main/rate-limits/automation-anywhere-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/automation-anywhere-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/automation-anywhere/refs/heads/main/plans/automation-anywhere-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/automation-anywhere-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/automation-anywhere/refs/heads/main/asyncapi/automation-anywhere-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/automation-anywhere-webhooks.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/automation-anywhere/refs/heads/main/data-model/automation-anywhere-data-model.yml
  title: ''
  type: DataModel
  url: data-model/automation-anywhere-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/automation-anywhere/refs/heads/main/components/automation-anywhere-components.yml
  title: ''
  type: Components
  url: components/automation-anywhere-components.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/automation-anywhere/refs/heads/main/sandbox/automation-anywhere-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/automation-anywhere-sandbox.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/automation-anywhere/refs/heads/main/scopes/automation-anywhere-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/automation-anywhere-scopes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/automation-anywhere/refs/heads/main/conventions/automation-anywhere-conventions.yml
  title: ''
  type: Conventions
  url: conventions/automation-anywhere-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/automation-anywhere/refs/heads/main/errors/automation-anywhere-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/automation-anywhere-problem-types.yml
- group: auth
  title: ''
  type: Security
  url: https://www.automationanywhere.com/legal/vulnerability-disclosure-policy
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/automation-anywhere/refs/heads/main/security/automation-anywhere-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/automation-anywhere-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/automation-anywhere/refs/heads/main/security/automation-anywhere-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/automation-anywhere-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.automationanywhere.com/compliance-portal
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/automation-anywhere/refs/heads/main/conformance/automation-anywhere-conformance.yml
  title: ''
  type: Conformance
  url: conformance/automation-anywhere-conformance.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/automation-anywhere/refs/heads/main/changelog/automation-anywhere-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/automation-anywhere-changelog.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://ai-kb.automationanywhere.com/changelogs/feature-deprecations/deprecations-overview
- group: operate
  title: ''
  type: StatusPage
  url: https://status.automationanywhere.digital/
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/automation-anywhere/refs/heads/main/lifecycle/automation-anywhere-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/automation-anywhere-lifecycle.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/automation-anywhere/refs/heads/main/packages/automation-anywhere-packages.yml
  title: ''
  type: Packages
  url: packages/automation-anywhere-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/automation-anywhere/refs/heads/main/packages/automation-anywhere-packages.yml
  title: ''
  type: SDKs
  url: packages/automation-anywhere-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/automation-anywhere/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/automation-anywhere/refs/heads/main/well-known/automation-anywhere-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/automation-anywhere-well-known.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/automation-anywhere/refs/heads/main/mcp/automation-anywhere-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/automation-anywhere-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/automation-anywhere/refs/heads/main/mcp/automation-anywhere-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/automation-anywhere-mcp.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/automation-anywhere/refs/heads/main/a2a/automation-anywhere-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/automation-anywhere-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/automation-anywhere/refs/heads/main/llms/automation-anywhere-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/automation-anywhere-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/automation-anywhere/refs/heads/main/llms/automation-anywhere-ekb-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/automation-anywhere-ekb-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/automation-anywhere/refs/heads/main/agentic-access/automation-anywhere-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/automation-anywhere-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/automation-anywhere/refs/heads/main/security/automation-anywhere-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/automation-anywhere-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/automation-anywhere/refs/heads/main/authentication/automation-anywhere-authentication.yml
  title: ''
  type: Authentication
  url: authentication/automation-anywhere-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AutomationAnywhere
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/automation-anywhere
- group: start
  title: ''
  type: Portal
  url: https://developer.automationanywhere.com
- group: company
  title: ''
  type: Website
  url: https://www.automationanywhere.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.automationanywhere.com
- group: auth
  title: ''
  type: Authentication
  url: https://docs.automationanywhere.com/bundle/enterprise-v2019/page/enterprise-cloud/topics/control-room/control-room-api/cloud-authentication.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.automationanywhere.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.automationanywhere.com/legal/privacy
- group: operate
  title: ''
  type: Support
  url: https://apeople.automationanywhere.com/
- group: company
  title: ''
  type: Blog
  url: https://www.automationanywhere.com/blog
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/automation-anywhere/refs/heads/main/json-ld/automation-anywhere-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/automation-anywhere-context.jsonld
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/automation-anywhere/refs/heads/main/json-schema/automation-anywhere-bot-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/automation-anywhere-bot-schema.json
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/automation-anywhere/refs/heads/main/json-schema/automation-anywhere-deployment-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/automation-anywhere-deployment-schema.json
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/automation-anywhere/refs/heads/main/json-schema/automation-anywhere-work-item-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/automation-anywhere-work-item-schema.json
created: '2026-05-04'
description: Automation Anywhere is an enterprise robotic process automation (RPA) platform that enables organizations to automate business processes using software bots. Their developer platform, centered around the Automation 360 Control Room, provides a comprehensive suite of REST APIs for managing bot deployment, workload queues, credentials, repositories, and analytics, as well as an SDK for building custom action packages.
features:
- description: All Control Room APIs use JWT-based authentication. Tokens are obtained via the Authentication API and passed in the X-Authorization or Authorization Bearer header. OAuth 2.0 is supported from v.27 onwards.
  name: JWT Authentication
- description: APIs are versioned (v1, v2, v3, v4) with backwards compatibility maintained for at least two years. Deprecated endpoints are announced with at least one additional year of availability.
  name: Versioned API Endpoints
- description: Each Control Room instance exposes a Swagger UI at /swagger/ for interactive API exploration and testing with live credentials.
  name: Swagger UI Explorer
- description: API Tasks allow RPA bots to be exposed as synchronous REST endpoints, enabling external applications to call bots as microservices with input/output parameter exchange.
  name: API Task Execution
- description: Work item queues allow high-volume data to be fed into RPA pipelines from ERP, CRM, and BPM systems with status tracking and result retrieval.
  name: Workload Queuing
finops:
- name: Automation Anywhere Finops
  service_category: RPA / Intelligent Automation
  slug: automation-anywhere-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/automation-anywhere.png
json_schemas:
- name: AccessDetailsRequest
  property_count: 1
  slug: automation-anywhere-accessdetailsrequest
- name: AccessDetailsResponse
  property_count: 2
  slug: automation-anywhere-accessdetailsresponse
- name: ApiTaskAccessDetail
  property_count: 2
  slug: automation-anywhere-apitaskaccessdetail
- name: ApiTaskAllocation
  property_count: 5
  slug: automation-anywhere-apitaskallocation
- name: ApiTaskHeaders
  property_count: 1
  slug: automation-anywhere-apitaskheaders
- name: AssignLabelRequest
  property_count: 2
  slug: automation-anywhere-assignlabelrequest
- name: AttendedRequest
  property_count: 1
  slug: automation-anywhere-attendedrequest
- name: AuditRecord
  property_count: 13
  slug: automation-anywhere-auditrecord
- name: AuditTrailResponse
  property_count: 2
  slug: automation-anywhere-audittrailresponse
- name: AuthenticationRequest
  property_count: 4
  slug: automation-anywhere-authenticationrequest
- name: AuthenticationResponse
  property_count: 2
  slug: automation-anywhere-authenticationresponse
- name: Automation Anywhere Bot
  property_count: 17
  slug: automation-anywhere-bot
- name: BotInputVariable
  property_count: 6
  slug: automation-anywhere-botinputvariable
- name: BotRunDataResponse
  property_count: 2
  slug: automation-anywhere-botrundataresponse
- name: BotRunRecord
  property_count: 14
  slug: automation-anywhere-botrunrecord
- name: CallbackInfo
  property_count: 2
  slug: automation-anywhere-callbackinfo
- name: CreateRoleRequest
  property_count: 3
  slug: automation-anywhere-createrolerequest
- name: CreateUserRequest
  property_count: 8
  slug: automation-anywhere-createuserrequest
- name: Credential
  property_count: 9
  slug: automation-anywhere-credential
- name: CredentialAttribute
  property_count: 5
  slug: automation-anywhere-credentialattribute
- name: CredentialAttributePost
  property_count: 4
  slug: automation-anywhere-credentialattributepost
- name: CredentialAttributeValue
  property_count: 5
  slug: automation-anywhere-credentialattributevalue
- name: CredentialAttributeValueList
  property_count: 1
  slug: automation-anywhere-credentialattributevaluelist
- name: CredentialAttributeValuePost
  property_count: 3
  slug: automation-anywhere-credentialattributevaluepost
- name: CredentialAttributeValuePostList
  property_count: 1
  slug: automation-anywhere-credentialattributevaluepostlist
- name: CredentialAttributeValuePut
  property_count: 1
  slug: automation-anywhere-credentialattributevalueput
- name: CredentialFilterResponse
  property_count: 2
  slug: automation-anywhere-credentialfilterresponse
- name: CredentialPost
  property_count: 3
  slug: automation-anywhere-credentialpost
- name: DependencyUpdateRequest
  property_count: 1
  slug: automation-anywhere-dependencyupdaterequest
- name: Automation Anywhere Bot Deployment
  property_count: 13
  slug: automation-anywhere-deployment
- name: DeploymentRequest
  property_count: 12
  slug: automation-anywhere-deploymentrequest
- name: DeploymentResponse
  property_count: 1
  slug: automation-anywhere-deploymentresponse
- name: Error
  property_count: 2
  slug: automation-anywhere-error
- name: ErrorMessage
  property_count: 2
  slug: automation-anywhere-errormessage
- name: FileDependencyResponse
  property_count: 1
  slug: automation-anywhere-filedependencyresponse
- name: FileListResponse
  property_count: 2
  slug: automation-anywhere-filelistresponse
- name: FileParentsResponse
  property_count: 1
  slug: automation-anywhere-fileparentsresponse
- name: FilterExpression
  property_count: 2
  slug: automation-anywhere-filterexpression
- name: FilterOperand
  property_count: 2
  slug: automation-anywhere-filteroperand
- name: FilterRequest
  property_count: 4
  slug: automation-anywhere-filterrequest
- name: FolderRequest
  property_count: 2
  slug: automation-anywhere-folderrequest
- name: HeadlessRequest
  property_count: 1
  slug: automation-anywhere-headlessrequest
- name: ListAllocationsRequest
  property_count: 1
  slug: automation-anywhere-listallocationsrequest
- name: ListAllocationsResponse
  property_count: 2
  slug: automation-anywhere-listallocationsresponse
- name: Locker
  property_count: 8
  slug: automation-anywhere-locker
- name: LockerConsumer
  property_count: 2
  slug: automation-anywhere-lockerconsumer
- name: LockerConsumerList
  property_count: 1
  slug: automation-anywhere-lockerconsumerlist
- name: LockerConsumerPost
  property_count: 1
  slug: automation-anywhere-lockerconsumerpost
- name: LockerCredentialList
  property_count: 1
  slug: automation-anywhere-lockercredentiallist
- name: LockerCredentialUpdate
  property_count: 1
  slug: automation-anywhere-lockercredentialupdate
- name: LockerListResponse
  property_count: 2
  slug: automation-anywhere-lockerlistresponse
- name: LockerMember
  property_count: 3
  slug: automation-anywhere-lockermember
- name: LockerMemberList
  property_count: 1
  slug: automation-anywhere-lockermemberlist
- name: LockerMemberUpdate
  property_count: 1
  slug: automation-anywhere-lockermemberupdate
- name: LockerPost
  property_count: 2
  slug: automation-anywhere-lockerpost
- name: ObjectPermission
  property_count: 6
  slug: automation-anywhere-objectpermission
- name: PackageVersionUpdateRequest
  property_count: 3
  slug: automation-anywhere-packageversionupdaterequest
- name: PageInfo
  property_count: 3
  slug: automation-anywhere-pageinfo
- name: PageRequest
  property_count: 2
  slug: automation-anywhere-pagerequest
- name: Permission
  property_count: 4
  slug: automation-anywhere-permission
- name: PermissionsUpdateRequest
  property_count: 1
  slug: automation-anywhere-permissionsupdaterequest
- name: Queue
  property_count: 17
  slug: automation-anywhere-queue
- name: QueueConsumer
  property_count: 2
  slug: automation-anywhere-queueconsumer
- name: QueueConsumerRequest
  property_count: 1
  slug: automation-anywhere-queueconsumerrequest
- name: QueueExpiry
  property_count: 3
  slug: automation-anywhere-queueexpiry
- name: QueueMember
  property_count: 2
  slug: automation-anywhere-queuemember
- name: QueueMemberRequest
  property_count: 1
  slug: automation-anywhere-queuememberrequest
- name: QueueParticipantRequest
  property_count: 1
  slug: automation-anywhere-queueparticipantrequest
- name: RecoverRequest
  property_count: 2
  slug: automation-anywhere-recoverrequest
- name: RepositoryObject
  property_count: 13
  slug: automation-anywhere-repositoryobject
- name: RepositoryPermissions
  property_count: 2
  slug: automation-anywhere-repositorypermissions
- name: RoleListResponse
  property_count: 2
  slug: automation-anywhere-rolelistresponse
- name: RoleRef
  property_count: 2
  slug: automation-anywhere-roleref
- name: RoleResponse
  property_count: 8
  slug: automation-anywhere-roleresponse
- name: RunAsUser
  property_count: 1
  slug: automation-anywhere-runasuser
- name: SortCriteria
  property_count: 2
  slug: automation-anywhere-sortcriteria
- name: TaskLogDataResponse
  property_count: 2
  slug: automation-anywhere-tasklogdataresponse
- name: TaskLogRecord
  property_count: 4
  slug: automation-anywhere-tasklogrecord
- name: TaskMetadataResponse
  property_count: 2
  slug: automation-anywhere-taskmetadataresponse
- name: TaskVariable
  property_count: 3
  slug: automation-anywhere-taskvariable
- name: TaskVariableProfileResponse
  property_count: 4
  slug: automation-anywhere-taskvariableprofileresponse
- name: TokenValidationResponse
  property_count: 1
  slug: automation-anywhere-tokenvalidationresponse
- name: UnattendedRequest
  property_count: 2
  slug: automation-anywhere-unattendedrequest
- name: UpdateRoleRequest
  property_count: 3
  slug: automation-anywhere-updaterolerequest
- name: UpdateUserRequest
  property_count: 7
  slug: automation-anywhere-updateuserrequest
- name: UpdateWorkItemRequest
  property_count: 6
  slug: automation-anywhere-updateworkitemrequest
- name: UserListResponse
  property_count: 2
  slug: automation-anywhere-userlistresponse
- name: UserResponse
  property_count: 12
  slug: automation-anywhere-userresponse
- name: UserSummary
  property_count: 4
  slug: automation-anywhere-usersummary
- name: VariableProfile
  property_count: 3
  slug: automation-anywhere-variableprofile
- name: Automation Anywhere Work Item
  property_count: 27
  slug: automation-anywhere-work-item
- name: WorkItem
  property_count: 20
  slug: automation-anywhere-workitem
- name: WorkItemAttribute
  property_count: 4
  slug: automation-anywhere-workitemattribute
- name: WorkItemModel
  property_count: 10
  slug: automation-anywhere-workitemmodel
json_structures:
- name: Automation Anywhere Structure
  property_count: 0
  slug: automation-anywhere-structure
jsonld:
- class_count: 0
  name: Automation Anywhere Context
  property_count: 10
  slug: automation-anywhere-context
layout: provider
mcp_servers:
- description: ''
  name: Automation Anywhere MCP servers
  slug: automation-anywhere-mcp-servers
modified: '2026-09-17'
name: Automation Anywhere
nav: Providers
network: true
overview: 'Automation Anywhere publishes 22 APIs on the [APIs.io](https://apis.io/) network, including automation-anywhere AccessDetails API, automation-anywhere Allocations API, automation-anywhere AuditData API, and 19 more. Tagged areas include RPA, Intelligent Automation, Agentic Process Automation, AI Agents, and Workflow Automation.


  The Automation Anywhere catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Automation Anywhere''s developer surface includes signup flow, getting-started guide, API reference, sandbox, changelog, authentication, developer portal, and 49 more developer resources.'
plans:
- name: Automation Anywhere Plans Pricing
  plan_count: 4
  slug: automation-anywhere-plans-pricing
random_paper: 21
rate_limits:
- limit_count: 2
  name: Automation Anywhere Rate Limits
  slug: automation-anywhere-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: Automation Anywhere API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: automation-anywhere-jsonschema-spectral-rules
scopes:
- name: Automation Anywhere Scopes
  scope_count: 0
  slug: automation-anywhere-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: exemplar
  composite: 76.1
  coverage:
    artifact_dirs: 33
    catalog_earned: 78.8
    catalog_earned_first_party: 8.0
    catalog_gap: 36.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.5
  facets:
    access_clarity: 65.8
    contract_governance: 41.7
    contract_quality: 70.5
    developer_ergonomics: 78.6
    discoverability: 80.0
    operational_transparency: 81.6
  previous_composite: 75.6
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 21
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
    score: 22.2
screenshot: https://raw.githubusercontent.com/api-evangelist/automation-anywhere/refs/heads/main/screenshots/automation-anywhere-2026-06-20T172657.png
security:
- kind: authentication
  name: Automation Anywhere Authentication
  slug: automation-anywhere-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Automation Anywhere Domain Security
  slug: automation-anywhere-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Automation Anywhere Vulnerability Disclosure
  slug: automation-anywhere-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Automation Anywhere Trust Center
  slug: automation-anywhere-trust-center
  summary_line: ISO 27001, ISO 9001, ISO 42001, ISO 22301, SOC 1, SOC 2, HIPAA, HITRUST, Cyber Essentials
slug: automation-anywhere
tags:
- RPA
- Intelligent Automation
- Agentic Process Automation
- AI Agents
- Workflow Automation
- Document Automation
- Process Orchestration
- Enterprise Automation
- Bots
- A2A
use_cases:
- description: Automate bot deployment across dev, test, and production environments using the Bot Deploy and Repository Management APIs in CI/CD pipelines.
  name: DevOps Bot Pipeline
- description: Connect ERP, CRM, and BPM systems to RPA workload queues to distribute and process high-volume transactional data with Automation Anywhere bots.
  name: Enterprise System Integration
- description: Feed Bot Insight API data into Tableau, Power BI, or Splunk for real-time RPA operational dashboards and business KPI tracking.
  name: Bot Performance Monitoring
- description: Programmatically provision and rotate bot credentials in the Credential Vault from enterprise secrets management systems like CyberArk or HashiCorp Vault.
  name: Credential Governance
- description: Build proprietary Java action packages using the Package SDK to extend Automation 360 with custom connectors for legacy or specialized systems.
  name: Custom Action Packages
website: https://www.automationanywhere.com
---
