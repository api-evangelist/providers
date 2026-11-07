---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: true
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: verified
    mcp_server: platform
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: mostly
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 49.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 228
  human_in_the_loop: 25
  name: Treasure Data Agentic Access
  operation_count: 433
  slug: treasure-data-agentic-access
  summary_line: 433 operations · 228 acting · 25 human-in-the-loop
api_count: 7
apis:
- baseURL: https://api.treasuredata.com/v3/bulk_loads
  baseurl_source: declared
  description: REST API for configuring and managing bulk load sessions that import data from external sources into Treasure Data.
  name: Treasure Data Bulk Loads API
  phrasing_intents:
  - id: listBulkLoads
    intent: List bulk load sessions
    question: What bulk load sessions are configured?
  - id: getBulkLoad
    intent: Get a bulk load session
    question: How do I see the configuration of one bulk load session?
  - id: listBulkLoadJobs
    intent: List job history of a bulk load
    question: What jobs has a bulk load session run?
  phrasing_ops: 3
  slug: treasure-data-bulk-loads-api
- baseURL: https://api.treasuredata.com/v3/user
  baseurl_source: declared
  description: REST API for managing users, access control, and authentication within a Treasure Data account.
  name: Treasure Data User API
  phrasing_intents:
  - id: getApiUsersCurrent
    intent: Get the current user
    question: Who am I signed in as in the Treasure Data AI API?
  - id: getApiUsersCurrentSettings
    intent: Get the current user's settings
    question: What settings are applied to my user account?
  phrasing_ops: 2
  slug: treasure-data-user-api
- baseURL: https://api.treasuredata.com/v3/system
  baseurl_source: declared
  description: REST API for checking server health and infrastructure status of the Treasure Data platform.
  name: Treasure Data System API
  phrasing_intents:
  - id: getServerStatus
    intent: Check API server health
    question: Is the Treasure Data API up right now?
  phrasing_ops: 1
  slug: treasure-data-system-api
- baseURL: https://in.treasuredata.com
  baseurl_source: declared
  description: JSON-based event ingestion API for submitting data records to Treasure Data from systems that cannot use the JavaScript SDK.
  name: Treasure Data Postback API
  phrasing_intents:
  - id: postPostbackAPIv2
    intent: Send an event record into a table
    question: How do I stream a single event into a Treasure Data table over HTTP?
  phrasing_ops: 1
  slug: treasure-data-postback-api
- description: REST API for orchestrating and automating data workflows within the Treasure Data platform using Digdag-based workflow engine.
  name: Treasure Workflow API
  slug: treasure-workflow-api
- baseURL: https://api.treasuredata.com/v3
  baseurl_source: declared
  description: Bulk data import sessions
  name: Treasure Data Bulk Import API
  phrasing_intents:
  - id: listBulkImports
    intent: List bulk import sessions
    question: What bulk import sessions are open in my account?
  - id: createBulkImport
    intent: Start a bulk import session for a table
    question: How do I start a bulk import into a Treasure Data table?
  - id: showBulkImport
    intent: Get a bulk import session's details
    question: What state is my bulk import session in?
  - id: uploadBulkImportPart
    intent: Upload a msgpack.gz part to a bulk import
    question: How do I upload a msgpack.gz file into a bulk import session?
  - id: listBulkImportParts
    intent: List uploaded parts of a bulk import
    question: Which parts have already been uploaded to my bulk import?
  - id: performBulkImport
    intent: Run the bulk import job for a session
    question: How do I process the parts I've uploaded to a bulk import?
  - id: commitBulkImport
    intent: Commit a bulk import to make data available
    question: How do I finalize a bulk import so the data shows up in the table?
  - id: freezeBulkImport
    intent: Freeze a bulk import to block more uploads
    question: Can I stop further uploads to a bulk import session?
  phrasing_ops: 10
  slug: treasure-data-bulk-import-api
- baseURL: https://api.treasuredata.com/v3
  baseurl_source: declared
  description: Bulk load sessions from external sources
  name: Treasure Data Bulk Loads API
  phrasing_intents:
  - id: listBulkLoads
    intent: List bulk load sessions
    question: What bulk load sessions are configured?
  - id: getBulkLoad
    intent: Get a bulk load session
    question: How do I see the configuration of one bulk load session?
  - id: listBulkLoadJobs
    intent: List job history of a bulk load
    question: What jobs has a bulk load session run?
  phrasing_ops: 3
  slug: treasure-data-bulk-loads-api
- baseURL: https://api.treasuredata.com/v3
  baseurl_source: declared
  description: Manage output connectors
  name: Treasure Data Connectors API
  phrasing_intents:
  - id: listConnectors
    intent: List output connectors
    question: Which output connectors can I send query results to?
  phrasing_ops: 1
  slug: treasure-data-connectors-api
- baseURL: https://api.treasuredata.com/v3
  baseurl_source: declared
  description: Manage Treasure Data databases
  name: Treasure Data Databases API
  phrasing_intents:
  - id: listDatabases
    intent: List databases
    question: What databases are in my Treasure Data account?
  - id: getDatabaseByName
    intent: Get a database by name
    question: How do I see details about one database?
  - id: createDatabase
    intent: Create a database
    question: How do I create a new database?
  - id: deleteDatabase
    intent: Delete a database
    question: How do I delete a database I don't need anymore?
  phrasing_ops: 4
  slug: treasure-data-databases-api
- baseURL: https://api.treasuredata.com/v3
  baseurl_source: declared
  description: Submit and manage query jobs
  name: Treasure Data Jobs API
  phrasing_intents:
  - id: issuePrestoQuery
    intent: Run a Presto SQL query on a database
    question: How do I run a Presto SQL query against a Treasure Data database?
  - id: issueHiveQuery
    intent: Run a Hive query on a database
    question: How can I submit a Hive query instead of Presto?
  - id: getJobResult
    intent: Download the results of a finished query job
    question: How do I get the output rows of a query job once it's done?
  - id: getJobs
    intent: List query jobs in the account
    question: What jobs have been run in my account recently?
  - id: getJobById
    intent: Get details of a job
    question: How do I see the full details of a specific job, like its query and database?
  - id: getJobStatusById
    intent: Check a job's status by ID
    question: Is my query job still running or has it finished?
  - id: getJobStatusByDomainKey
    intent: Check a job's status by domain key
    question: Can I find a job's status using the domain key I assigned instead of its job ID?
  - id: getJobStatisticsById
    intent: Get a job's statistics
    question: How many records did a job insert?
  phrasing_ops: 12
  slug: treasure-data-jobs-api
- baseURL: https://api.treasuredata.com/v3
  baseurl_source: declared
  description: Identity federation and SSO settings
  name: Treasure Data SSO API
  phrasing_intents:
  - id: getSSOSetting
    intent: Get the account's SSO configuration
    question: Which identity provider is my Treasure Data account configured to use for SSO?
  - id: createSSOSetting
    intent: Configure SSO for the account for the first time
    question: How do I connect an identity provider to an account that has no SSO yet?
  - id: updateSSOSetting
    intent: Update the account's SSO configuration
    question: Can an admin change the identity provider details on an existing SSO setup?
  - id: deleteSSOSetting
    intent: Remove the account's SSO configuration
    question: How do I remove the identity provider from my account?
  - id: createUserWithSSO
    intent: Create a user who signs in with SSO
    question: Can an admin add a new user who authenticates through single sign-on?
  - id: enforceSSOForUser
    intent: Require a user to log in with SSO
    question: How do I make SSO mandatory for a specific user?
  - id: enableSSOForUser
    intent: Allow a user to log in with SSO
    question: Can I let a user choose single sign-on without making it required?
  - id: disableSSOForUser
    intent: Prohibit a user from logging in with SSO
    question: How do I block one user from signing in through single sign-on?
  phrasing_ops: 8
  slug: treasure-data-sso-api
- baseURL: https://api.treasuredata.com/v3
  baseurl_source: declared
  description: System health and status
  name: Treasure Data System API
  phrasing_intents:
  - id: getServerStatus
    intent: Check API server health
    question: Is the Treasure Data API up right now?
  phrasing_ops: 1
  slug: treasure-data-system-api
- baseURL: https://api.treasuredata.com/v3
  baseurl_source: declared
  description: Manage tables within databases
  name: Treasure Data Tables API
  phrasing_intents:
  - id: listTables
    intent: List the tables in a database
    question: Which tables exist inside one of my Treasure Data databases?
  - id: getTableByDatabaseNameAndTableName
    intent: Show the details of one table
    question: What schema, row count and settings does a specific table have?
  - id: deleteTable
    intent: Delete a table
    question: How do I drop a table I no longer need from a database?
  - id: createTableWithTableType
    intent: Create a table with an explicit table type
    question: Can I create a table and state its table type in the request path?
  - id: createTable
    intent: Create a table with the default log type
    question: How do I create a new table in a database without choosing a table type?
  - id: updateTable
    intent: Update a table's settings
    question: Can I change a table's description or data expiration after it was created?
  - id: renameTable
    intent: Rename a table
    question: How do I give an existing table a new name?
  - id: swapTables
    intent: Swap two tables in a database
    question: Can I swap two tables so each takes the other's name?
  phrasing_ops: 16
  slug: treasure-data-tables-api
- baseURL: https://api.treasuredata.com/v3
  baseurl_source: declared
  description: User management
  name: Treasure Data Users API
  phrasing_intents:
  - id: listUsers
    intent: List users in the account
    question: Who are all the users on my Treasure Data account?
  - id: showCurrentUser
    intent: Show the authenticated user
    question: Which user does my API key belong to?
  - id: removeUser
    intent: Remove a user from the account
    question: How do I delete a user who has left the team?
  - id: createUserWithSSO
    intent: Create a user who signs in with SSO
    question: How can an admin add a new user that authenticates through SSO?
  - id: enforceSSOForUser
    intent: Require a user to sign in with SSO
    question: Can I make SSO mandatory for a specific user?
  - id: enableSSOForUser
    intent: Allow a user to sign in with SSO
    question: How do I permit a user to log in with SSO as an option?
  - id: disableSSOForUser
    intent: Prohibit a user from signing in with SSO
    question: Can I block a user from using SSO to log in?
  - id: promoteDelegatedAdmin
    intent: Make a user a delegated admin
    question: How do I give a user delegated admin rights?
  phrasing_ops: 9
  slug: treasure-data-users-api
- baseURL: https://api-workflow.treasuredata.com
  baseurl_source: declared
  description: Treasure Workflow — the Digdag-based orchestration API. 43 operations over projects, workflow definitions, revisions, schedules, sessions, attempts, tasks, logs, secrets and resource pools.
  name: Treasure Workflow API
  phrasing_intents:
  - id: getWorkflowDefinitions
    intent: List workflows across projects
    question: What workflows exist across all my projects?
  - id: getWorkflowDefinition
    intent: Get a workflow by ID
    question: How do I read a workflow definition when I know its ID?
  - id: getWorkflowTruncatedSessionTime
    intent: Truncate a time to a workflow's time zone
    question: How would a session time be truncated in a workflow's local time zone?
  phrasing_ops: 3
  slug: treasure-data-workflow-api
- baseURL: https://in.treasuredata.com
  baseurl_source: declared
  description: JSON event ingestion endpoint used by the JavaScript, iOS, Android, React Native and Cordova SDKs for small, frequent payloads.
  name: Treasure Data Postback API
  phrasing_intents:
  - id: postPostbackAPIv2
    intent: Send an event record into a table
    question: How do I stream a single event into a Treasure Data table over HTTP?
  phrasing_ops: 1
  slug: treasure-data-postback-api
- description: 'Two Model Context Protocol servers — the official @treasuredata/mcp-server (23 tools, local stdio, public preview) and a live remote documentation MCP endpoint on the docs host whose six tools return '
  name: Treasure Data MCP Servers
  slug: treasure-data-mcp
- baseURL: https://api.treasuredata.com/v3/bulk_loads
  baseurl_source: declared
  description: The Access Control - Permissions API from Treasure Data — 2 operation(s) for access control - permissions.
  name: Treasure Data Access Control - Permissions API
  phrasing_intents:
  - id: getColumnPermissionByPolicyId
    intent: Show a policy's column permissions
    question: Which columns can a given access control policy see?
  - id: updateColumnPermissionByPolicyId
    intent: Update a policy's column permissions
    question: Can I restrict which columns a policy can access?
  - id: gerPermissionByPolicyId
    intent: Show a policy's feature permissions
    question: What can a policy do across workflows, segments and databases?
  - id: updatePermissionByPolicyId
    intent: Update a policy's feature permissions
    question: Can I grant a policy access to specific databases or workflow projects?
  phrasing_ops: 4
  slug: treasure-data-access-control-permissions-api
- baseURL: https://api.treasuredata.com/v3/bulk_loads
  baseurl_source: declared
  description: The Access Control - Policies API from Treasure Data — 5 operation(s) for access control - policies.
  name: Treasure Data Access Control - Policies API
  phrasing_intents:
  - id: getAccessControlPolicies
    intent: List access control policies
    question: Which access control policies exist in my account?
  - id: createAccessControlPolicy
    intent: Create an access control policy
    question: How do I define a new access control policy in Treasure Data?
  - id: getAccessControlPolicyById
    intent: Get an access control policy
    question: What does a specific access control policy contain?
  - id: updateAccessControlPolicyById
    intent: Update an access control policy
    question: Can I edit the name or description of an existing policy?
  - id: deleteAccessControlPolicyById
    intent: Delete an access control policy
    question: How do I remove an access control policy entirely?
  - id: getAccessControlPoliciesByUserId
    intent: List the policies assigned to a user
    question: Which access control policies does a given user have?
  - id: updateAccessControlPoliciesByUserId
    intent: Replace a user's set of policies
    question: Can I set a user's full list of policies in one call?
  - id: attachUserAndPolicy
    intent: Attach a policy to a user (user path)
    question: Can I add a single policy to a user through the user's policies path?
  phrasing_ops: 11
  slug: treasure-data-access-control-policies-api
- baseURL: https://api.treasuredata.com/v3/bulk_loads
  baseurl_source: declared
  description: The Access Control - Policy Groups API from Treasure Data — 3 operation(s) for access control - policy groups.
  name: Treasure Data Access Control - Policy Groups API
  phrasing_intents:
  - id: getAccessControlPolicyGroups
    intent: List policy groups
    question: Which access control policy groups exist in my account?
  - id: createAccessControlPolicyGroup
    intent: Create a policy group
    question: How do I create a group to organize related access policies?
  - id: getAccessControlPolicyGroupById
    intent: Get a policy group
    question: What are the details of a particular policy group?
  - id: updateAccessControlPolicyGroupById
    intent: Rename or describe a policy group
    question: Can I rename a policy group or change its description?
  - id: deleteAccessControlPolicyGroupById
    intent: Delete a policy group
    question: How do I remove a policy group I no longer need?
  - id: getAccessControlPolicyGroupPoliciesById
    intent: List the policies in a policy group
    question: Which policies belong to a given policy group?
  - id: updateAccessControlPolicyGroupPolicies
    intent: Set the policies in a policy group
    question: How do I change which policies are attached to a policy group?
  phrasing_ops: 7
  slug: treasure-data-access-control-policy-groups-api
- baseURL: https://api.treasuredata.com/v3/bulk_loads
  baseurl_source: declared
  description: The Access Control - Users API from Treasure Data — 6 operation(s) for access control - users.
  name: Treasure Data Access Control - Users API
  phrasing_intents:
  - id: getAccessControlUsers
    intent: List users and their permissions
    question: Who are the users in my account and what permissions does each have?
  - id: getAccessControlUserById
    intent: Get one user's access control details
    question: What permissions does a specific user currently have?
  - id: updateAccessControlUserPermissions
    intent: Update a user's permissions
    question: How do I give a user access to workflow projects or segment folders?
  - id: getAccessControlUserProfileOptions
    intent: List a user's profile options
    question: Which profile options apply to a user and what are their resolved values?
  - id: getAccessControlUserProfileOption
    intent: Get one profile option for a user
    question: What value does a single profile option resolve to for a given user?
  - id: updateAccessControlUserProfileOption
    intent: Set a profile option for a user
    question: Can an admin override a profile option for one user?
  - id: deleteAccessControlUserProfileOption
    intent: Reset a user's profile option to the default
    question: How do I revert a user's profile option back to the account default?
  - id: getAccessControlPolicyUsers
    intent: List the users on a policy
    question: Which users are attached to a given access policy?
  phrasing_ops: 9
  slug: treasure-data-access-control-users-api
- baseURL: https://api.treasuredata.com/v3/bulk_loads
  baseurl_source: declared
  description: The Action API from Treasure Data — 2 operation(s) for action.
  name: Treasure Data Action API
  phrasing_intents:
  - id: getApiActions
    intent: List LLM actions
    question: Which actions are available to my LLM agents?
  - id: postApiActionsByIdSlack
    intent: Run an action from a Slack command
    question: Can a Slack slash command trigger one of my LLM actions?
  phrasing_ops: 2
  slug: treasure-data-action-api
- baseURL: https://api.treasuredata.com/v3/bulk_loads
  baseurl_source: declared
  description: Marketers find creating an activation challenging because they have to enter technical information they might not understand, which can lead to activations failing due to misconfigurations. Treasure D
  name: Treasure Data Activation Templates API
  phrasing_intents:
  - id: activation_templates#create
    intent: Create an activation template
    question: How do I save a reusable activation setup as a template?
  - id: activation_templates#show
    intent: Get an activation template
    question: What settings does a particular activation template hold?
  - id: activation_templates#update
    intent: Update an activation template
    question: Can I change the settings saved in an existing activation template?
  - id: activation_templates#delete
    intent: Delete an activation template
    question: How do I remove an activation template nobody uses?
  - id: getEntitiesParentSegmentsByParentSegmentIdActivationTemplates
    intent: List activation templates for a parent segment
    question: Which activation templates are available in a parent segment?
  phrasing_ops: 5
  slug: treasure-data-activation-templates-api
- baseURL: https://api.treasuredata.com/v3/bulk_loads
  baseurl_source: declared
  description: 'Activation is the process that allows marketers to personalize communication to users interested in your brand. <br> <ul> <li> **Funnel activation** &mdash; Create a funnel activation for each funnel '
  name: Treasure Data Activations API
  phrasing_intents:
  - id: segment_folders#syndications
    intent: List activations under a segment folder
    question: Can I see every activation inside a segment folder, including its subfolders?
  - id: syndications#index
    intent: List activations of a segment (audience API)
    question: What activations are attached to this segment in my parent segment?
  - id: syndications#create
    intent: Create an activation for a segment
    question: How do I set up an activation that sends a segment to a destination connection in Treasure Data?
  - id: syndications#show
    intent: Get an activation of a segment by ID
    question: How can I look up the settings of a single activation on a parent-segment segment?
  - id: syndications#update
    intent: Update an activation's settings
    question: Can I change the schedule or columns of an existing activation?
  - id: syndications#delete
    intent: Delete an activation from a segment
    question: How do I remove an activation from a segment under a parent segment?
  - id: syndications#run
    intent: Run an activation now (legacy Audience Studio)
    question: How do I trigger an activation to run immediately in legacy Audience Studio?
  - id: audience_syndications#index
    intent: List all activations in a parent segment
    question: What activations exist across a whole parent segment and what are their statuses?
  phrasing_ops: 17
  slug: treasure-data-activations-api
- baseURL: https://api.treasuredata.com/v3/bulk_loads
  baseurl_source: declared
  description: The Agent API from Treasure Data — 2 operation(s) for agent.
  name: Treasure Data Agent API
  phrasing_intents:
  - id: getApiAgents
    intent: List LLM agents
    question: Which AI agents have been set up in my account?
  - id: postApiAgents
    intent: Create an LLM agent
    question: What is needed to create a new AI agent?
  - id: deleteApiAgentsById
    intent: Delete an LLM agent
    question: Can I delete an agent I no longer need?
  - id: getApiAgentsById
    intent: Get an LLM agent
    question: How is one particular agent configured?
  - id: patchApiAgentsById
    intent: Update an LLM agent
    question: Can I change an existing agent's settings?
  phrasing_ops: 5
  slug: treasure-data-agent-api
- baseURL: https://api.treasuredata.com/v3/bulk_loads
  baseurl_source: declared
  description: The AgentSchedule API from Treasure Data — 4 operation(s) for agentschedule.
  name: Treasure Data Agent Schedule API
  phrasing_intents:
  - id: getApiAgentSchedules
    intent: List agent schedules
    question: Which agents are set to run on a schedule?
  - id: postApiAgentSchedules
    intent: Schedule an agent
    question: Can I make an agent run automatically on a schedule?
  - id: deleteApiAgentSchedulesById
    intent: Delete an agent schedule
    question: Can I stop an agent from running on its schedule for good?
  - id: getApiAgentSchedulesById
    intent: Get an agent schedule
    question: When does a particular agent schedule run next, and what does it run?
  - id: patchApiAgentSchedulesById
    intent: Update an agent schedule
    question: Can I change when a scheduled agent runs?
  - id: postApiAgentSchedulesByIdCallback
    intent: Report a scheduled agent run's result
    question: How does a workflow report back that a scheduled agent run finished or failed?
  - id: postApiAgentSchedulesByIdExecute
    intent: Execute an agent schedule now
    question: Can I run a scheduled agent right away instead of waiting?
  phrasing_ops: 7
  slug: treasure-data-agentschedule-api
- baseURL: https://api.treasuredata.com/v3/bulk_loads
  baseurl_source: declared
  description: The Artifact API from Treasure Data — 1 operation(s) for artifact.
  name: Treasure Data Artifact API
  phrasing_intents:
  - id: getApiArtifacts
    intent: List chat artifacts
    question: What files or outputs has an agent chat produced?
  phrasing_ops: 1
  slug: treasure-data-artifact-api
- baseURL: https://api.treasuredata.com/v3/bulk_loads
  baseurl_source: declared
  description: The Attempt API from Treasure Data — 5 operation(s) for attempt.
  name: Treasure Data Attempt API
  phrasing_intents:
  - id: getAttempts
    intent: List workflow attempts
    question: Which workflow attempts have run recently in a given project?
  - id: startAttempt
    intent: Start or resume a workflow run
    question: How do I trigger a Treasure Data workflow to run right now?
  - id: getAttempt
    intent: Get a workflow attempt
    question: What is the status of a particular workflow attempt?
  - id: killAttempt
    intent: Cancel a running workflow attempt
    question: How do I stop a workflow attempt that is still running?
  - id: getAttemptRetries
    intent: List all attempts in the same session
    question: What retries were made in the same session as a given attempt?
  - id: getTasks
    intent: List the tasks of a workflow attempt
    question: Which task in a workflow attempt failed?
  phrasing_ops: 6
  slug: treasure-data-attempt-api
- baseURL: https://api.treasuredata.com/v3/bulk_loads
  baseurl_source: declared
  description: The Chat API from Treasure Data — 5 operation(s) for chat.
  name: Treasure Data Chat API
  phrasing_intents:
  - id: getApiChats
    intent: List agent chats
    question: Which conversations have I had with my agents?
  - id: postApiChats
    intent: Start a new agent chat
    question: Can I open a new conversation with an agent?
  - id: getApiChatsById
    intent: Get an agent chat
    question: Can I look up the details of one chat session?
  - id: postApiChatsByIdContinue
    intent: Send a follow-up message in a chat
    question: Can I keep talking to an agent in an existing chat?
  - id: postApiChatsByIdDownloadFiles
    intent: Download files from a chat
    question: Can I download the files an agent chat generated?
  - id: getApiChatsByIdHistory
    intent: Get a chat's message history
    question: What was said earlier in an agent conversation?
  phrasing_ops: 6
  slug: treasure-data-chat-api
- baseURL: https://api.treasuredata.com/v3/bulk_loads
  baseurl_source: declared
  description: The ChatAttachment API from Treasure Data — 2 operation(s) for chatattachment.
  name: Treasure Data Chat Attachment API
  phrasing_intents:
  - id: getApiChatAttachments
    intent: List chat attachments
    question: Which files were attached to my agent chats?
  - id: postApiChatAttachments
    intent: Upload a chat attachment
    question: Can I attach a file for an agent to use in a chat?
  - id: deleteApiChatAttachmentsById
    intent: Delete a chat attachment
    question: Can I remove a file I attached to a chat?
  - id: getApiChatAttachmentsById
    intent: Get a chat attachment
    question: Can I look up a single chat attachment by its ID?
  phrasing_ops: 4
  slug: treasure-data-chatattachment-api
- baseURL: https://api.treasuredata.com/v3/bulk_loads
  baseurl_source: declared
  description: The ChatInterface API from Treasure Data — 2 operation(s) for chatinterface.
  name: Treasure Data Chat Interface API
  phrasing_intents:
  - id: getApiChatInterfaces
    intent: List chat interfaces
    question: Which chat interfaces have been published for my agents?
  - id: postApiChatInterfaces
    intent: Create a chat interface
    question: Can I put a chat interface in front of an agent so others can use it?
  - id: deleteApiChatInterfacesById
    intent: Delete a chat interface
    question: Can I take down a chat interface nobody uses?
  - id: getApiChatInterfacesById
    intent: Get a chat interface
    question: How is one chat interface configured?
  - id: patchApiChatInterfacesById
    intent: Update a chat interface
    question: Can I rename or reconfigure an existing chat interface?
  phrasing_ops: 5
  slug: treasure-data-chatinterface-api
- baseURL: https://api.treasuredata.com/v3/bulk_loads
  baseurl_source: declared
  description: The Connections API from Treasure Data — 5 operation(s) for connections.
  name: Treasure Data Connections API
  phrasing_intents:
  - id: getConnections
    intent: List result output connections
    question: What result output connections have I set up?
  - id: createConnection
    intent: Create a result output connection
    question: How do I save a new connection for writing query results somewhere?
  - id: deleteConnection
    intent: Delete a result output connection
    question: How do I remove a saved connection?
  - id: getConnectionIdByName
    intent: Look up a connection's ID by name
    question: What's the ID of the connection I named a certain way?
  - id: validateConnectorConfig
    intent: Validate a connector configuration
    question: Can I check that connector settings are valid before saving them?
  phrasing_ops: 5
  slug: treasure-data-connections-api
- baseURL: https://api.treasuredata.com/v3/bulk_loads
  baseurl_source: declared
  description: The Data Connector Restrictions API from Treasure Data — 1 operation(s) for data connector restrictions.
  name: Treasure Data Connector Restrictions API
  phrasing_intents:
  - id: getDataConnectorRestrictions
    intent: Get data connector restrictions
    question: Which data connectors are restricted on my account?
  phrasing_ops: 1
  slug: treasure-data-data-connector-restrictions-api
- baseURL: https://api.treasuredata.com/v3/bulk_loads
  baseurl_source: declared
  description: The Dwh API from Treasure Data — 6 operation(s) for dwh.
  name: Treasure Data Dwh API
  phrasing_intents:
  - id: getV1Dwh
    intent: List data warehouse integrations
    question: Which data warehouse integrations have I set up?
  - id: postV1Dwh
    intent: Create a data warehouse integration
    question: Can I schedule a recurring import from my data warehouse into Treasure Data?
  - id: getV1DwhByDwhId
    intent: Get a data warehouse integration
    question: Can I look up one warehouse integration by its ID?
  - id: putV1DwhByDwhId
    intent: Update a data warehouse integration
    question: Can I change the schedule or filters of an existing warehouse integration?
  - id: deleteV1DwhByDwhId
    intent: Delete a data warehouse integration
    question: What gets removed when I delete a warehouse integration?
  - id: getV1DwhByDwhIdBulkloadSessions
    intent: List a warehouse integration's bulkload sessions
    question: Which bulkload sessions did a warehouse integration generate?
  - id: getV1DwhByDwhIdConfigs
    intent: Get a warehouse integration's configuration
    question: What connection and output configuration does a warehouse integration use?
  - id: putV1DwhByDwhIdRunWorkflow
    intent: Run a warehouse integration now
    question: Can I trigger a warehouse import immediately instead of waiting for its schedule?
  phrasing_ops: 9
  slug: treasure-data-dwh-api
- baseURL: https://api.treasuredata.com/v3/bulk_loads
  baseurl_source: declared
  description: Folders are containers in which you can organize information. Nested folders offer flexible organization controls. Large volumes of data and application assets can be organized into multi-nested folde
  name: Treasure Data Folders API
  phrasing_intents:
  - id: postAudiencesByAudienceIdFolders
    intent: Create a segment folder in a parent segment
    question: Can I organize segments into a new folder under a parent segment?
  - id: getAudiencesByAudienceIdFoldersByFolderId
    intent: Get a segment folder in a parent segment
    question: Can I look up one segment folder within a parent segment?
  - id: patchAudiencesByAudienceIdFoldersByFolderId
    intent: Update a segment folder (legacy)
    question: Can I rename a segment folder in legacy Audience Studio?
  - id: deleteAudiencesByAudienceIdFoldersByFolderId
    intent: Delete a segment folder (legacy)
    question: Can I delete a segment folder in legacy Audience Studio?
  - id: postAudiencesByAudienceIdFoldersByFolderIdPutIn
    intent: Move segments into a folder (legacy)
    question: Can I move existing segments into a folder in legacy Audience Studio?
  - id: getEntitiesByFolderByFolderId
    intent: List everything under a folder
    question: What segments, funnels, models and tokens live under a folder?
  - id: postEntitiesFolders
    intent: Create a folder via the entities API
    question: Can I create a folder in the current Audience Studio through the entities API?
  - id: getEntitiesFoldersById
    intent: Get a folder by entity ID
    question: Can I fetch a folder using only its entity ID?
  phrasing_ops: 10
  slug: treasure-data-folders-api
- baseURL: https://api.treasuredata.com/v3/bulk_loads
  baseurl_source: declared
  description: The FormInterface API from Treasure Data — 2 operation(s) for forminterface.
  name: Treasure Data Form Interface API
  phrasing_intents:
  - id: getApiFormInterfaces
    intent: List form interfaces for AI agents
    question: Which form interfaces exist in my Treasure Data AI projects?
  - id: postApiFormInterfaces
    intent: Create a form interface
    question: Can I build a form front end that feeds inputs to an AI agent?
  - id: deleteApiFormInterfacesById
    intent: Delete a form interface
    question: How do I remove a form interface I no longer use?
  - id: getApiFormInterfacesById
    intent: Get one form interface
    question: What is configured on a specific form interface?
  - id: patchApiFormInterfacesById
    intent: Update a form interface
    question: Can I change the fields on an existing form interface?
  phrasing_ops: 5
  slug: treasure-data-forminterface-api
- baseURL: https://api.treasuredata.com/v3/bulk_loads
  baseurl_source: declared
  description: One of the challenges of targeting customers with relevant campaigns is understanding where they are in their customer journey. Many organizations use the traditional marketing funnel to understand wh
  name: Treasure Data Funnels API
  phrasing_intents:
  - id: funnels#index
    intent: List funnels in a parent segment
    question: What funnels are defined on my parent segment?
  - id: funnels#create
    intent: Create a funnel (legacy Audience Studio)
    question: How do I build a new funnel with stages in legacy Audience Studio?
  - id: funnels#show
    intent: Get a funnel by ID
    question: How do I look at a single funnel's stages?
  - id: funnels#update
    intent: Update a funnel (legacy Audience Studio)
    question: Can I change the stages of an existing funnel?
  - id: funnels#delete
    intent: Delete a funnel (legacy Audience Studio)
    question: How do I delete a funnel I no longer use?
  - id: funnels#clone
    intent: Clone a funnel
    question: Can I copy an existing funnel as a starting point for a new one?
  - id: funnels#statistics
    intent: Get a funnel's daily population history
    question: How many profiles were in each funnel stage over time?
  - id: postEntitiesFunnels
    intent: Create a funnel via the entities API
    question: Can I create a funnel in the current Audience Studio without a parent segment path?
  phrasing_ops: 13
  slug: treasure-data-funnels-api
- baseURL: https://api.treasuredata.com/v3/bulk_loads
  baseurl_source: declared
  description: The Guess API from Treasure Data — 1 operation(s) for guess.
  name: Treasure Data Guess API
  phrasing_intents:
  - id: postV1Guess
    intent: Guess a data warehouse integration configuration
    question: Can Treasure Data work out the full data warehouse integration config from a few basic settings?
  phrasing_ops: 1
  slug: treasure-data-guess-api
- baseURL: https://api.treasuredata.com/v3/bulk_loads
  baseurl_source: declared
  description: The ImageGenerator API from Treasure Data — 2 operation(s) for imagegenerator.
  name: Treasure Data Image Generator API
  phrasing_intents:
  - id: postApiImageGenerators
    intent: Create an image generator tool
    question: Can I give an AI agent the ability to generate images?
  - id: deleteApiImageGeneratorsById
    intent: Delete an image generator
    question: How do I remove an image generator from my agents?
  - id: getApiImageGeneratorsById
    intent: Get an image generator
    question: How is a particular image generator configured?
  - id: patchApiImageGeneratorsById
    intent: Update an image generator
    question: Can I change the settings of an existing image generator?
  phrasing_ops: 4
  slug: treasure-data-imagegenerator-api
- baseURL: https://api.treasuredata.com/v3/bulk_loads
  baseurl_source: declared
  description: The Integration API from Treasure Data — 2 operation(s) for integration.
  name: Treasure Data Integration API
  phrasing_intents:
  - id: getApiIntegrations
    intent: List AI agent integrations
    question: Which integrations are set up for my Treasure Data AI agents?
  - id: postApiIntegrations
    intent: Create an integration
    question: How do I connect a new integration to my AI agents?
  - id: deleteApiIntegrationsById
    intent: Delete an integration
    question: How do I disconnect and remove an integration?
  - id: getApiIntegrationsById
    intent: Get an integration
    question: What are the details of one specific integration?
  - id: patchApiIntegrationsById
    intent: Update an integration
    question: Can I change the configuration of an existing integration?
  phrasing_ops: 5
  slug: treasure-data-integration-api
- baseURL: https://api.treasuredata.com/v3/bulk_loads
  baseurl_source: declared
  description: In Audience Studio, a journey represents a timeline of events that can help you motivate a customer’s behavior about your product. After marketers create journey stages, they can further analyze and r
  name: Treasure Data Journeys API
  phrasing_intents:
  - id: getEntitiesJourneys
    intent: List journeys in a folder
    question: Which customer journeys are stored in a particular folder?
  - id: postEntitiesJourneys
    intent: Create a customer journey
    question: What does it take to build a brand-new customer journey from scratch?
  - id: getEntitiesJourneysByJourneyId
    intent: Get a journey's summary
    question: Where can I see the overall summary and setup of one journey?
  - id: patchEntitiesJourneysByJourneyId
    intent: Update a journey
    question: Can I rename a journey or change its settings after it is created?
  - id: deleteEntitiesJourneysByJourneyId
    intent: Delete a journey
    question: Can I permanently remove a journey I no longer need?
  - id: postEntitiesJourneysByJourneyIdDetail
    intent: Update a draft journey's meta field
    question: Can I edit the meta details of a journey while it is still a draft?
  - id: postEntitiesJourneysByJourneyIdAvailableBehaviorsForStep
    intent: List behavior tables available to a journey step
    question: Which behavior tables can I use in a given step of my journey?
  - id: postEntitiesJourneysByJourneyIdActivationTemplatesForStep
    intent: List activation templates usable in a journey step
    question: Which activation templates can I apply to a step in my journey?
  phrasing_ops: 32
  slug: treasure-data-journeys-api
- baseURL: https://api.treasuredata.com/v3/bulk_loads
  baseurl_source: declared
  description: The Log API from Treasure Data — 2 operation(s) for log.
  name: Treasure Data Log API
  phrasing_intents:
  - id: getFileHandles
    intent: List the log files of a workflow attempt
    question: Which log files were produced by a workflow attempt?
  - id: getFile
    intent: Download a workflow log file
    question: How do I download a specific log file to see why a task failed?
  phrasing_ops: 2
  slug: treasure-data-log-api
- baseURL: https://api.treasuredata.com/v3/bulk_loads
  baseurl_source: declared
  description: Defining a data model for customer data is done by defining parent segments. Parent segments give you an ability to build a single view of a customer, including capturing all interactions, such as att
  name: Treasure Data Parent Segment Configurations API
  phrasing_intents:
  - id: audiences#index
    intent: List parent segment configurations
    question: Which parent segments are configured in my Treasure Data account?
  - id: audiences#create
    intent: Create a parent segment configuration
    question: How do I set up a new parent segment for building audiences?
  - id: audiences#show
    intent: Get one parent segment configuration
    question: What is configured on a specific parent segment?
  - id: audiences#update
    intent: Update a parent segment configuration
    question: Can I rename an existing parent segment without touching its attributes and behaviors?
  - id: audiences#delete
    intent: Delete a parent segment configuration
    question: How do I remove a parent segment I no longer use?
  - id: audience_attributes#index
    intent: List a parent segment's attributes
    question: Which customer attributes are defined on a parent segment?
  - id: audience_behaviors#index
    intent: List a parent segment's behaviors
    question: What behavior tables are attached to a parent segment?
  - id: audiences#run
    intent: Regenerate a parent segment
    question: How do I refresh a parent segment so it picks up new data?
  phrasing_ops: 12
  slug: treasure-data-parent-segment-configurations-api
- baseURL: https://api.treasuredata.com/v3/bulk_loads
  baseurl_source: declared
  description: After you have created the parent segment, you can view data about the parent segment, such as details about a single segment, audience data, the list of segment folders it contains, or a list of pare
  name: Treasure Data Parent Segments API
  phrasing_intents:
  - id: getAudiencesByAudienceIdFolders
    intent: List segment folders in a parent segment
    question: What segment folders exist under a parent segment?
  - id: getMasterSegments
    intent: List audiences whose data I can view
    question: Which audiences am I allowed to see segments, profiles and activations for?
  - id: getEntitiesParentSegments
    intent: List parent segments
    question: What parent segments are defined in my Treasure Data CDP?
  - id: getEntitiesParentSegmentsById
    intent: Get a parent segment
    question: What is configured on one particular parent segment?
  phrasing_ops: 4
  slug: treasure-data-parent-segments-api
- baseURL: https://api.treasuredata.com/v3/bulk_loads
  baseurl_source: declared
  description: The Personalization Service API from Treasure Data — 1 operation(s) for personalization service.
  name: Treasure Data Personalization Service API
  phrasing_intents:
  - id: personalize
    intent: Get real-time personalization offers for an event
    question: How do I send an event and get personalized offers back in real time?
  phrasing_ops: 1
  slug: treasure-data-personalization-service-api
- baseURL: https://api.treasuredata.com/v3/bulk_loads
  baseurl_source: declared
  description: The PlazmaQueryTool API from Treasure Data — 2 operation(s) for plazmaquerytool.
  name: Treasure Data Plazma Query Tool API
  phrasing_intents:
  - id: postApiPlazmaQueryTools
    intent: Create a Plazma query tool
    question: Can I let an AI agent run queries against my Plazma data?
  - id: deleteApiPlazmaQueryToolsById
    intent: Delete a Plazma query tool
    question: How do I remove a Plazma query tool from my agents?
  - id: getApiPlazmaQueryToolsById
    intent: Get a Plazma query tool
    question: How is a particular Plazma query tool set up?
  - id: patchApiPlazmaQueryToolsById
    intent: Update a Plazma query tool
    question: Can I change the settings of an existing Plazma query tool?
  phrasing_ops: 4
  slug: treasure-data-plazmaquerytool-api
- baseURL: https://api.treasuredata.com/v3/bulk_loads
  baseurl_source: declared
  description: The Policy Group Tags API from Treasure Data — 2 operation(s) for policy group tags.
  name: Treasure Data Policy Group Tags API
  phrasing_intents:
  - id: getPolicyGroupTagsDelegatedAdmins
    intent: List the delegated admins of a policy group
    question: Who are the delegated admins allowed to manage a policy group?
  - id: updatePolicyGroupTagsDelegatedAdmins
    intent: Set the delegated admins of a policy group
    question: How do I let certain users manage a policy group as delegated admins?
  - id: getPolicyGroupTagsUsers
    intent: List the users tagged with a policy group
    question: Which users are tagged with a particular policy group?
  - id: updatePolicyGroupTagsUsers
    intent: Tag users with a policy group
    question: How do I put a set of users under a policy group?
  phrasing_ops: 4
  slug: treasure-data-policy-group-tags-api
- baseURL: https://api.treasuredata.com/v3/bulk_loads
  baseurl_source: declared
  description: The Pool API from Treasure Data — 4 operation(s) for pool.
  name: Treasure Data Pool API
  phrasing_intents:
  - id: getPoolRules
    intent: List pool rules
    question: Which rules decide what pool a workflow attempt runs in?
  - id: createPoolRule
    intent: Create a rule that routes attempts to a pool
    question: How do I send certain workflow attempts to a dedicated pool?
  - id: deletePoolRule
    intent: Delete a pool rule
    question: How do I remove a pool routing rule?
  - id: getPoolRule
    intent: Get a pool rule
    question: What conditions and priority does a specific pool rule have?
  - id: updatePoolRule
    intent: Update a pool rule
    question: Can I change the priority of an existing pool rule?
  - id: getPools
    intent: List workflow pools
    question: What pools do I have and what are their concurrency limits?
  - id: createPool
    intent: Create a pool with a concurrency limit
    question: How do I reserve concurrency for a group of workflows with a new pool?
  - id: deletePool
    intent: Delete a pool
    question: Why can't I delete a pool that still has queued attempts?
  phrasing_ops: 10
  slug: treasure-data-pool-api
- baseURL: https://api.treasuredata.com/v3/bulk_loads
  baseurl_source: declared
  description: Using Treasure Data’s predictive scoring model, based on predictive segments, marketers can predict profile behavior such as who is likely to churn, purchase, click, or convert in the near future. <br
  name: Treasure Data Predictive Segments API
  phrasing_intents:
  - id: predictive_segments#index
    intent: List predictive scoring models
    question: What predictive scoring models exist on my parent segment?
  - id: predictive_segments#create
    intent: Create a predictive scoring model (legacy)
    question: How do I set up a predictive scoring model in legacy Audience Studio?
  - id: getAudiencesByAudienceIdPredictiveSegmentsByPredictiveSegmentId
    intent: Get a predictive model's statistics (legacy)
    question: Where can I see the accuracy statistics of a predictive model in legacy Audience Studio?
  - id: predictive_segments#update
    intent: Update a predictive scoring model (legacy)
    question: Can I change the grade thresholds on a predictive model?
  - id: predictive_segments#destroy
    intent: Delete a predictive scoring model (legacy)
    question: How do I delete a predictive scoring model?
  - id: getAudiencesByAudienceIdPredictiveSegmentsByPredictiveSegmentIdExecutions
    intent: List a predictive model's runs (legacy)
    question: Did the last training run of my legacy predictive model succeed?
  - id: getAudiencesByAudienceIdPredictiveSegmentsGuessRuleAsync
    intent: Get guessed rules for a segment (legacy)
    question: Can Treasure Data suggest segment rules for a predictive model in legacy Audience Studio?
  - id: getAudiencesByAudienceIdPredictiveSegmentsByPredictiveSegmentIdModelColumns
    intent: List columns of a predictive model (legacy)
    question: Which columns does a legacy predictive model read from the parent segment?
  phrasing_ops: 21
  slug: treasure-data-predictive-segments-api
- baseURL: https://api.treasuredata.com/v3/bulk_loads
  baseurl_source: declared
  description: The PresentationArtifactTool API from Treasure Data — 2 operation(s) for presentationartifacttool.
  name: Treasure Data Presentation Artifact Tool API
  phrasing_intents:
  - id: postApiPresentationArtifactTools
    intent: Create a presentation artifact tool
    question: Can an AI agent produce presentation artifacts with a dedicated tool?
  - id: deleteApiPresentationArtifactToolsById
    intent: Delete a presentation artifact tool
    question: How do I remove a presentation artifact tool?
  - id: getApiPresentationArtifactToolsById
    intent: Get a presentation artifact tool
    question: How is a given presentation artifact tool configured?
  - id: patchApiPresentationArtifactToolsById
    intent: Update a presentation artifact tool
    question: Can I change the settings of an existing presentation artifact tool?
  phrasing_ops: 4
  slug: treasure-data-presentationartifacttool-api
- baseURL: https://api.treasuredata.com/v3/bulk_loads
  baseurl_source: declared
  description: The Project API from Treasure Data — 10 operation(s) for project.
  name: Treasure Data Project API
  phrasing_intents:
  - id: getApiProjects
    intent: List LLM projects
    question: Which LLM projects exist in my account?
  - id: postApiProjects
    intent: Create an LLM project
    question: Can I set up a new project to hold agents and interfaces?
  - id: putProject
    intent: Upload a workflow project archive
    question: How do I push a workflow project archive as a new revision?
  - id: deleteApiProjectsById
    intent: Delete an LLM project
    question: Can I delete an LLM project I no longer use?
  - id: getApiProjectsById
    intent: Get an LLM project
    question: What settings and related resources does one LLM project hold?
  - id: patchApiProjectsById
    intent: Update an LLM project
    question: Can I rename or reconfigure an existing LLM project?
  - id: getArchive
    intent: Download a project archive
    question: How do I download the archive of a workflow project revision?
  - id: getRevisions
    intent: List revisions of a project
    question: What revisions has a workflow project gone through?
  phrasing_ops: 15
  slug: treasure-data-project-api
- baseURL: https://api.treasuredata.com/v3/bulk_loads
  baseurl_source: declared
  description: The Prompt API from Treasure Data — 2 operation(s) for prompt.
  name: Treasure Data Prompt API
  phrasing_intents:
  - id: getApiPrompts
    intent: List prompts
    question: Which prompts are saved for my Treasure Data AI agents?
  - id: postApiPrompts
    intent: Create a prompt
    question: How do I save a new reusable prompt?
  - id: deleteApiPromptsById
    intent: Delete a prompt
    question: How do I remove a prompt I no longer use?
  - id: getApiPromptsById
    intent: Get a prompt
    question: What does a specific saved prompt contain?
  - id: patchApiPromptsById
    intent: Update a prompt
    question: Can I edit the wording of an existing prompt?
  phrasing_ops: 5
  slug: treasure-data-prompt-api
- baseURL: https://api.treasuredata.com/v3/bulk_loads
  baseurl_source: declared
  description: The Realtime Journeys API from Treasure Data — 21 operation(s) for realtime journeys.
  name: Treasure Data Realtime Journeys API
  phrasing_intents:
  - id: getAudiencesByAudienceIdRealtimeSetting
    intent: Get an audience's realtime setting
    question: Is realtime enabled for my audience, and how is it configured?
  - id: patchAudiencesByAudienceIdRealtimeSetting
    intent: Update an audience's realtime setting
    question: How do I change which event tables feed realtime for an audience?
  - id: getAudiencesByAudienceIdRealtimeAttributes
    intent: List an audience's realtime attributes
    question: What realtime attributes are defined on an audience?
  - id: postAudiencesByAudienceIdRealtimeAttributes
    intent: Create a realtime attribute
    question: How do I add a new realtime attribute to an audience?
  - id: getAudiencesByAudienceIdRealtimeAttributesByRealtimeAttributeId
    intent: Get a realtime attribute
    question: How is one specific realtime attribute defined?
  - id: patchAudiencesByAudienceIdRealtimeAttributesByRealtimeAttributeId
    intent: Update a realtime attribute
    question: Can I change the time window or aggregations of a realtime attribute?
  - id: deleteAudiencesByAudienceIdRealtimeAttributesByRealtimeAttributeId
    intent: Delete a realtime attribute
    question: How do I remove a realtime attribute from an audience?
  - id: postAudiencesByAudienceIdRealtimeImportedAttributesBulkUpdate
    intent: Bulk update imported realtime attributes
    question: Can I update many imported attributes for realtime in one call?
  phrasing_ops: 32
  slug: treasure-data-realtime-journeys-api
- baseURL: https://api.treasuredata.com/v3/bulk_loads
  baseurl_source: declared
  description: The Realtime Personalization API from Treasure Data — 7 operation(s) for realtime personalization.
  name: Treasure Data Realtime Personalization API
  phrasing_intents:
  - id: getAudiencesByAudienceIdRealtimePersonalizationServices
    intent: List realtime personalization services
    question: Which realtime personalization services are set up for an audience?
  - id: postAudiencesByAudienceIdRealtimePersonalizationServices
    intent: Create a realtime personalization service
    question: How do I stand up a realtime personalization service for an audience?
  - id: getAudiencesByAudienceIdRealtimePersonalizationServicesByRealtimePersonalizationServiceId
    intent: Get a realtime personalization service
    question: What is configured on one personalization service?
  - id: patchAudiencesByAudienceIdRealtimePersonalizationServicesByRealtimePersonalizationServiceId
    intent: Edit a realtime personalization service
    question: Can I rename a personalization service or change its description?
  - id: deleteAudiencesByAudienceIdRealtimePersonalizationServicesByRealtimePersonalizationServiceId
    intent: Delete a realtime personalization service
    question: How do I shut down and remove a personalization service?
  - id: postAudiencesByAudienceIdRealtimePersonalizationServicesByRealtimePersonalizationServiceIdTokens
    intent: Create a personalization token
    question: How do I issue an access token for a personalization service?
  - id: deleteAudiencesByAudienceIdRealtimePersonalizationServicesByRealtimePersonalizationServiceIdTokensByTokenId
    intent: Delete a personalization token
    question: How do I revoke a personalization token that leaked?
  - id: postEntitiesRealtimePersonalizations
    intent: Create a realtime personalization
    question: Can I define a new realtime personalization that returns profile data in real time?
  phrasing_ops: 12
  slug: treasure-data-realtime-personalization-api
- baseURL: https://api.treasuredata.com/v3/bulk_loads
  baseurl_source: declared
  description: The Schedule API from Treasure Data — 6 operation(s) for schedule.
  name: Treasure Data Schedule API
  phrasing_intents:
  - id: getSchedules
    intent: List workflow schedules
    question: What workflow schedules are set up in my account?
  - id: getSchedule
    intent: Get a workflow schedule
    question: When is a particular schedule set to run next?
  - id: backfillSchedule
    intent: Backfill sessions for past schedule times
    question: How do I rerun a workflow for schedule times it missed in the past?
  - id: disableSchedule
    intent: Pause a workflow schedule
    question: How do I stop a schedule from starting new sessions?
  - id: enableSchedule
    intent: Re-enable a disabled schedule
    question: How do I turn a paused schedule back on?
  - id: skipSchedule
    intent: Skip upcoming sessions of a schedule
    question: Can I skip the next few runs of a workflow schedule?
  phrasing_ops: 6
  slug: treasure-data-schedule-api
- baseURL: https://api.treasuredata.com/v3/bulk_loads
  baseurl_source: declared
  description: The Schedules API from Treasure Data — 6 operation(s) for schedules.
  name: Treasure Data Schedules API
  phrasing_intents:
  - id: getSchedules
    intent: List scheduled queries
    question: Which scheduled queries are set up in my account?
  - id: createSchedule
    intent: Create a scheduled query
    question: How do I run a query on a recurring cron schedule?
  - id: deleteScheduleByName
    intent: Delete a scheduled query
    question: How do I stop and remove a recurring query schedule?
  - id: updateSchedule
    intent: Update a scheduled query
    question: Can I change the cron timing of an existing scheduled query?
  - id: runSchedule
    intent: Run a scheduled query for a given time
    question: How do I manually trigger a scheduled query for a specific scheduled time?
  - id: getScheduleExecutionHistoryByName
    intent: Get a schedule's execution history
    question: When did a scheduled query last run and did it succeed?
  phrasing_ops: 6
  slug: treasure-data-schedules-api
- baseURL: https://api.treasuredata.com/v3/bulk_loads
  baseurl_source: declared
  description: In marketing, a segment is a container that groups profiles (usually people) who share one or more common characteristics. In Treasure Data, the parent segment is your total population of people, acco
  name: Treasure Data Segments API
  phrasing_intents:
  - id: segments#index
    intent: List segments in a parent segment
    question: What segments exist in my parent segment?
  - id: segments#create
    intent: Create a segment
    question: How do I create a new customer segment with a rule in Treasure Data?
  - id: segment_folders#segments
    intent: List segments in a folder
    question: Which segments are stored in one particular segment folder?
  - id: segments#query
    intent: Generate the SQL for a segment rule
    question: Can I see the SQL that a segment rule translates to?
  - id: segments#new_query
    intent: Count profiles matching segment rules
    question: How many profiles would a set of segment rules match before I save it?
  - id: segments#show
    intent: Get a segment by ID
    question: How do I see a segment's rule and settings?
  - id: segments#update
    intent: Update a segment
    question: Can I change the rule of a segment that already exists?
  - id: segments#delete
    intent: Delete a segment (legacy Audience Studio)
    question: How do I delete a segment in legacy Audience Studio?
  phrasing_ops: 16
  slug: treasure-data-segments-api
- baseURL: https://api.treasuredata.com/v3/bulk_loads
  baseurl_source: declared
  description: The Session API from Treasure Data — 3 operation(s) for session.
  name: Treasure Data Session API
  phrasing_intents:
  - id: getSessions
    intent: List workflow sessions
    question: What workflow sessions have run in my account recently?
  - id: getSession
    intent: Get a workflow session
    question: What is the state of a specific workflow session?
  - id: getSessionAttempts
    intent: List the attempts of a workflow session
    question: How many times was a particular session attempted?
  phrasing_ops: 3
  slug: treasure-data-session-api
- baseURL: https://api.treasuredata.com/v3/bulk_loads
  baseurl_source: declared
  description: The TextKnowledgeBase API from Treasure Data — 2 operation(s) for textknowledgebase.
  name: Treasure Data Text Knowledge Base API
  phrasing_intents:
  - id: postApiTextKnowledgeBases
    intent: Create a text knowledge base
    question: Can I build a knowledge base from plain text for an AI agent?
  - id: deleteApiTextKnowledgeBasesById
    intent: Delete a text knowledge base
    question: How do I remove a text knowledge base?
  - id: getApiTextKnowledgeBasesById
    intent: Get a text knowledge base
    question: What is in a particular text knowledge base?
  - id: patchApiTextKnowledgeBasesById
    intent: Update a text knowledge base
    question: Can I change the text in an existing text knowledge base?
  phrasing_ops: 4
  slug: treasure-data-textknowledgebase-api
- baseURL: https://api.treasuredata.com/v3/bulk_loads
  baseurl_source: declared
  description: The TextResource API from Treasure Data — 2 operation(s) for textresource.
  name: Treasure Data Text Resource API
  phrasing_intents:
  - id: getApiTextResources
    intent: List text resources
    question: Which text resources are available to my Treasure Data AI agents?
  - id: postApiTextResources
    intent: Create a text resource
    question: How do I add a block of reference text for my agents to use?
  - id: deleteApiTextResourcesById
    intent: Delete a text resource
    question: How do I remove a text resource?
  - id: getApiTextResourcesById
    intent: Get a text resource
    question: What does one particular text resource contain?
  - id: patchApiTextResourcesById
    intent: Update a text resource
    question: Can I edit the content of an existing text resource?
  phrasing_ops: 5
  slug: treasure-data-textresource-api
- baseURL: https://api.treasuredata.com/v3/bulk_loads
  baseurl_source: declared
  description: The Profiles API Token enables your ability to increase personalized content based on detailed customer information. This REST API returns customer data in real-time and updates your segment informati
  name: Treasure Data Tokens API
  phrasing_intents:
  - id: tokens#index
    intent: List Profiles API tokens for a parent segment
    question: Which Profiles API tokens exist for a parent segment?
  - id: tokens#create
    intent: Create a Profiles API token (legacy)
    question: How do I create a token for looking up customer profiles in legacy Audience Studio?
  - id: tokens#show
    intent: Get a Profiles API token
    question: What columns and segments does a specific Profiles API token expose?
  - id: tokens#update
    intent: Update a Profiles API token (legacy)
    question: Can I change which attribute columns an existing profile token returns?
  - id: tokens#delete
    intent: Delete a Profiles API token (legacy)
    question: How do I revoke a profile lookup token so it stops working?
  - id: postEntitiesTokens
    intent: Create a Profiles API token via the entities API
    question: Can I create a Profiles API token in the current Audience Studio by entity?
  - id: getEntitiesTokensById
    intent: Get a Profiles API token by entity ID
    question: Can I look up a Profiles API token using only its entity ID?
  - id: patchEntitiesTokensById
    intent: Update a Profiles API token via the entities API
    question: Can I patch a Profiles API token's attributes by entity ID?
  phrasing_ops: 9
  slug: treasure-data-tokens-api
- baseURL: https://api.treasuredata.com/v3/bulk_loads
  baseurl_source: declared
  description: The ToolTarget API from Treasure Data — 2 operation(s) for tooltarget.
  name: Treasure Data Tool Target API
  phrasing_intents:
  - id: getApiToolTargets
    intent: List tool targets
    question: Which tool targets can my Treasure Data AI agents call?
  - id: getApiToolTargetsById
    intent: Get a tool target
    question: What are the details of one specific tool target?
  phrasing_ops: 2
  slug: treasure-data-tooltarget-api
- baseURL: https://api.treasuredata.com/v3/bulk_loads
  baseurl_source: declared
  description: The User API from Treasure Data — 2 operation(s) for user.
  name: Treasure Data User API
  phrasing_intents:
  - id: getApiUsersCurrent
    intent: Get the current user
    question: Who am I signed in as in the Treasure Data AI API?
  - id: getApiUsersCurrentSettings
    intent: Get the current user's settings
    question: What settings are applied to my user account?
  phrasing_ops: 2
  slug: treasure-data-user-api
- baseURL: https://api.treasuredata.com/v3/bulk_loads
  baseurl_source: declared
  description: The Util API from Treasure Data — 1 operation(s) for util.
  name: Treasure Data Util API
  phrasing_intents:
  - id: postApiUtilConvertSegmentRule
    intent: Convert a simplified rule into a segment rule
    question: Can I turn a simplified rule into a full Treasure Data segment rule?
  phrasing_ops: 1
  slug: treasure-data-util-api
- baseURL: https://api.treasuredata.com/v3/bulk_loads
  baseurl_source: declared
  description: The WebSearchTool API from Treasure Data — 2 operation(s) for websearchtool.
  name: Treasure Data Web Search Tool API
  phrasing_intents:
  - id: postApiWebSearchTools
    intent: Create a web search tool
    question: Can I let an AI agent search the web?
  - id: deleteApiWebSearchToolsById
    intent: Delete a web search tool
    question: How do I remove a web search tool from my agents?
  - id: getApiWebSearchToolsById
    intent: Get a web search tool
    question: How is a particular web search tool configured?
  - id: patchApiWebSearchToolsById
    intent: Update a web search tool
    question: Can I change the settings of an existing web search tool?
  phrasing_ops: 4
  slug: treasure-data-websearchtool-api
- baseURL: https://api.treasuredata.com/v3/bulk_loads
  baseurl_source: declared
  description: The WorkflowExecutor API from Treasure Data — 1 operation(s) for workflowexecutor.
  name: Treasure Data Workflow Executor API
  phrasing_intents:
  - id: getApiWorkflowExecutorsById
    intent: Get a workflow executor
    question: How is a particular workflow executor configured for my AI agents?
  phrasing_ops: 1
  slug: treasure-data-workflowexecutor-api
- baseURL: https://api.treasuredata.com/v3/bulk_loads
  baseurl_source: declared
  description: The Knowledge Base API from Treasure Data — 3 operation(s) for knowledge base.
  name: Treasure Data Knowledge Base API
  phrasing_intents:
  - id: getApiKnowledgeBases
    intent: List knowledge bases
    question: Which knowledge bases do my Treasure Data AI agents have?
  - id: postApiKnowledgeBases
    intent: Create a knowledge base
    question: How do I give an AI agent a knowledge base backed by my data?
  - id: deleteApiKnowledgeBasesById
    intent: Delete a knowledge base
    question: How do I remove a knowledge base I no longer need?
  - id: getApiKnowledgeBasesById
    intent: Get a knowledge base
    question: How is a particular knowledge base configured?
  - id: patchApiKnowledgeBasesById
    intent: Update a knowledge base
    question: Can I change the settings of an existing knowledge base?
  - id: postApiKnowledgeBasesByIdQuery
    intent: Query a knowledge base
    question: Can I run a query against a knowledge base directly?
  phrasing_ops: 6
  slug: treasure-data-knowledge-base-api
artifact_total: 98
asyncapis:
- description: ''
  name: Treasure Data Webhooks
  slug: treasure-data-webhooks
collections:
- collection_type: open
  name: Treasure Data TD Bulk Import API
  slug: open-treasure-data-bulk-import-api
- collection_type: open
  name: Treasure Data TD Bulk Import Bulk Loads API
  slug: open-treasure-data-bulk-loads-api
- collection_type: open
  name: Treasure Data TD Bulk Import Connectors API
  slug: open-treasure-data-connectors-api
- collection_type: open
  name: Treasure Data TD Bulk Import Databases API
  slug: open-treasure-data-databases-api
- collection_type: open
  name: Treasure Data TD Bulk Import Jobs API
  slug: open-treasure-data-jobs-api
- collection_type: open
  name: Treasure Data TD Bulk Import SSO API
  slug: open-treasure-data-sso-api
- collection_type: open
  name: Treasure Data TD Bulk Import System API
  slug: open-treasure-data-system-api
- collection_type: open
  name: Treasure Data TD Bulk Import Tables API
  slug: open-treasure-data-tables-api
- collection_type: open
  name: Treasure Data TD Bulk Import Users API
  slug: open-treasure-data-users-api
common:
- group: other
  href: https://artifacts.apis.io/treasure-data/capabilities/treasure-data-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/treasure-data-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/treasure-data/overlays/treasure-data-td-api-v3-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/treasure-data-td-api-v3-overlay.yaml
- group: other
  href: https://artifacts.apis.io/treasure-data/overlays/treasure-data-cdp-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/treasure-data-cdp-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/treasure-data/overlays/treasure-data-llm-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/treasure-data-llm-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/treasure-data/overlays/treasure-data-dwh-integration-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/treasure-data-dwh-integration-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/treasure-data/overlays/treasure-data-personalization-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/treasure-data-personalization-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/treasure-data/overlays/treasure-data-postback-api-v2-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/treasure-data-postback-api-v2-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/treasure-data/agentic-access/treasure-data-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/treasure-data-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/treasure-data/security/treasure-data-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/treasure-data-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/treasure-data/security/treasure-data-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/treasure-data-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/treasure-data/authentication/treasure-data-authentication.yml
  title: ''
  type: Authentication
  url: authentication/treasure-data-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.treasure.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.treasure.ai/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/treasure-data-inc-
- group: company
  title: ''
  type: Blog
  url: https://www.treasure.ai/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.treasure.ai/product/pricing/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.treasure.ai/
- group: other
  title: ''
  type: X
  url: https://twitter.com/TreasureData
- group: commercial
  href: https://artifacts.apis.io/treasure-data/plans/treasure-data-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/treasure-data-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/treasure-data/rate-limits/treasure-data-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/treasure-data-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/treasure-data/finops/treasure-data-finops.yml
  title: ''
  type: FinOps
  url: finops/treasure-data-finops.yml
- group: build
  href: https://artifacts.apis.io/treasure-data/packages/treasure-data-packages.yml
  title: ''
  type: Packages
  url: packages/treasure-data-packages.yml
- group: build
  href: https://artifacts.apis.io/treasure-data/packages/treasure-data-packages.yml
  title: ''
  type: SDKs
  url: packages/treasure-data-packages.yml
- group: build
  href: https://artifacts.apis.io/treasure-data/cli/treasure-data-cli.yml
  title: ''
  type: CLI
  url: cli/treasure-data-cli.yml
- group: agent
  href: https://artifacts.apis.io/treasure-data/mcp/treasure-data-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/treasure-data-mcp.yml
- group: build
  href: https://artifacts.apis.io/treasure-data/mcp/treasure-data-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/treasure-data-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/treasure-data/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/treasure-data/llms/treasure-data-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/treasure-data-llms.txt
- group: agent
  href: https://artifacts.apis.io/treasure-data/well-known/treasure-data-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/treasure-data-well-known.yml
- group: auth
  href: https://artifacts.apis.io/treasure-data/scopes/treasure-data-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/treasure-data-scopes.yml
- group: design
  href: https://artifacts.apis.io/treasure-data/conventions/treasure-data-conventions.yml
  title: ''
  type: Conventions
  url: conventions/treasure-data-conventions.yml
- group: design
  href: https://artifacts.apis.io/treasure-data/conventions/treasure-data-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/treasure-data-conventions.yml
- group: design
  href: https://artifacts.apis.io/treasure-data/errors/treasure-data-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/treasure-data-problem-types.yml
- group: design
  href: https://artifacts.apis.io/treasure-data/lifecycle/treasure-data-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/treasure-data-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/treasure-data/changelog/treasure-data-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/treasure-data-changelog.yml
- group: design
  href: https://artifacts.apis.io/treasure-data/conformance/treasure-data-conformance.yml
  title: ''
  type: Conformance
  url: conformance/treasure-data-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.treasure.ai/security/
- group: design
  href: https://artifacts.apis.io/treasure-data/data-model/treasure-data-data-model.yml
  title: ''
  type: DataModel
  url: data-model/treasure-data-data-model.yml
- group: design
  href: https://artifacts.apis.io/treasure-data/asyncapi/treasure-data-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/treasure-data-webhooks.yml
- group: start
  href: https://artifacts.apis.io/treasure-data/sandbox/treasure-data-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/treasure-data-sandbox.yml
- group: design
  href: https://artifacts.apis.io/treasure-data/vocabulary/treasure-data-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/treasure-data-vocabulary.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.treasure.ai/apis
- group: docs
  title: ''
  type: APIReference
  url: https://docs.treasure.ai/apis/td_api_v3-public
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.treasure.ai/apis/td-api
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://docs.treasure.ai/release-notes
- group: start
  title: ''
  type: Login
  url: https://console.treasuredata.com/users/sign_in
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.treasure.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.treasure.ai/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/treasure-data
created: '2026-06-13'
description: 'Treasure Data — rebranded Treasure AI in April 2026 — is an enterprise customer data platform that unifies first-party customer data and activates it across marketing, service and AI agent workloads. It publishes eight OpenAPI descriptions covering 405 operations: the Treasure Data API v3 for databases, tables, query jobs, schedules and access control; the CDP (Audience) API for parent segments, segments, journeys, funnels, predictive segments and activations; the LLM API for AI agents, chats and knowledge bases; Treasure Workflow for Digdag orchestration; a Data Warehouse Integration API for Snowflake and Databricks; the Personalization Service for real-time offers; and Postback v1 and v2 for event ingestion. Queries run on Trino/Presto and Hive. An official MCP server exposes 23 tools over stdio and the documentation site serves a live remote MCP endpoint.'
examples:
- key_count: 10
  name: Bulk Import Session
  slug: bulk-import-session
- key_count: 3
  name: Issue Job Response
  slug: issue-job-response
- key_count: 1
  name: List Databases Response
  slug: list-databases-response
- key_count: 1
  name: User List Response
  slug: user-list-response
finops:
- has_sources: true
  method: derived
  name: Treasure Data Finops
  primary_unit: ''
  service_category: ''
  slug: treasure-data-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/treasure-data.png
json_schemas:
- name: BulkImport
  property_count: 10
  slug: bulk-import
- name: Database
  property_count: 5
  slug: database
- name: Job
  property_count: 14
  slug: job
- name: User
  property_count: 14
  slug: user
jsonld:
- class_count: 38
  name: Treasure Data Context
  property_count: 2
  slug: treasure-data-context
layout: provider
mcp_servers:
- description: 'Treasure Data ships two distinct Model Context Protocol servers. The official product server, @treasuredata/mcp-server, is a local stdio server run with npx that exposes 23 tools over the TD API, the '
  name: Treasure Data MCP Servers
  slug: treasure-data-mcp-servers
modified: '2026-09-16'
name: Treasure Data
nav: Providers
network: true
overview: 'Treasure Data publishes 67 API contracts indexed on the [APIs.io](https://apis.io/) network, including Bulk Loads API, User API, System API, and 64 more. Tagged areas include Customer Data Platform, CDP, Big Data, Data Warehouse, and Hive.


  The Treasure Data catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Treasure Data''s developer surface includes authentication, documentation, engineering blog, pricing, CLI, changelog, sandbox, and 42 more developer resources.'
plans:
- name: Treasure Data Plans Pricing
  plan_count: 3
  slug: treasure-data-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 17
  name: Treasure Data Rate Limits
  slug: treasure-data-rate-limits
rules:
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: Treasure Data — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: treasure-data-jsonschema-spectral-rules
scopes:
- name: Treasure Data Scopes
  scope_count: 4
  slug: treasure-data-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: exemplar
  composite: 75.2
  coverage:
    artifact_dirs: 36
    catalog_earned: 79.8
    catalog_earned_first_party: 24.0
    catalog_gap: 35.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 85.5
    contract_governance: 41.7
    contract_quality: 62.8
    developer_ergonomics: 81.0
    discoverability: 80.0
    operational_transparency: 73.7
  previous_composite: 75.2
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 61
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 36.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 11.1
screenshot: https://apis.io/screenshots/treasure-data/treasure-data-2026-06-20T195643.png
security:
- kind: authentication
  name: Treasure Data Authentication
  slug: treasure-data-authentication
  summary_line: apiKey/http/openIdConnect · 8 schemes
- kind: domain-security
  name: Treasure Data Domain Security
  slug: treasure-data-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Treasure Data Trust Center
  slug: treasure-data-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, HIPAA, GDPR, CSA STAR
skill_count: 2
skills:
- name: td-javascript-sdk
  slug: treasure-data-sdk-skills-javascript
- name: pytd
  slug: treasure-data-sdk-skills-python
slug: treasure-data
tags:
- Customer Data Platform
- CDP
- Big Data
- Data Warehouse
- Hive
- Presto
- Enterprise
- Artificial Intelligence
- Marketing
- Analytics
website: https://www.treasure.ai/
---
