---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
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
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 37.7
  scored_at: '2026-10-03'
agentic_access:
- acting_count: 139
  human_in_the_loop: 9
  name: Anthropic Agentic Access
  operation_count: 258
  slug: anthropic-agentic-access
  summary_line: 258 operations · 139 acting · 9 human-in-the-loop
api_count: 6
apis:
- baseURL: https://api.anthropic.com/v1
  baseurl_source: declared
  description: Send a structured list of input messages with text and/or image content, and the model will generate the next message in the conversation. The Messages API supports text, images, tool use, extended th
  name: Anthropic Messages API
  phrasing_intents:
  - id: messages_post
    intent: Generate Claude's next message in a conversation
    question: How do I send a prompt to Claude and get a reply back?
  - id: message_batches_post
    intent: Submit a batch of message requests
    question: How do I run many Claude prompts at once asynchronously?
  - id: message_batches_list
    intent: List message batches in a workspace
    question: Which message batches have I submitted in this workspace, newest first?
  - id: message_batches_retrieve
    intent: Check a message batch's processing status
    question: Is my message batch done processing yet?
  - id: message_batches_delete
    intent: Delete a finished message batch
    question: Can I delete a message batch that's still processing?
  - id: message_batches_cancel
    intent: Cancel an in-progress message batch
    question: How do I stop a message batch before it finishes?
  - id: beta_message_batches_cancel
    intent: Cancel a message batch via the beta flag
    question: Can I cancel a running batch through the beta message batches endpoint?
  - id: message_batches_results
    intent: Download a message batch's results
    question: How do I get the responses back from a completed message batch?
  phrasing_ops: 16
  slug: anthropic-messages-api
- baseURL: https://api.anthropic.com/v1
  baseurl_source: declared
  description: List and inspect Claude models including Opus 4.7, Sonnet 4.6, and Haiku 4.5. The response includes max_input_tokens, max_tokens, and a capabilities object for every model so clients can discover mode
  name: Anthropic Models API
  phrasing_intents:
  - id: models_list
    intent: List available Claude models
    question: Which Claude models can I use with my API key right now?
  - id: models_get
    intent: Look up a model or resolve an alias
    question: What model ID does a model alias currently point to?
  - id: beta_models_get
    intent: Look up a model via the beta endpoint
    question: Can I resolve a model alias through the ?beta=true models endpoint?
  - id: beta_models_list
    intent: List models via the beta endpoint
    question: Which models does the ?beta=true model listing return?
  phrasing_ops: 4
  slug: anthropic-models-api
- baseURL: https://api.anthropic.com/v1
  baseurl_source: declared
  description: 'The Files API lets you upload and manage files for reuse across Messages, Batches, code execution, and Managed Agents without re-uploading content. 500 MB request limit; supports PDFs, images, Office '
  name: Anthropic Files API
  phrasing_intents:
  - id: upload_file_v1_files_post
    intent: Upload a file that expires
    question: How do I upload a file so I can reference it in later requests?
  - id: list_files_v1_files_get
    intent: List uploaded files on the plain endpoint
    question: Which files have I uploaded, listed without the beta query flag?
  - id: get_file_metadata_v1_files__file_id__get
    intent: Get a file's metadata on the plain endpoint
    question: What's the name, size and type of a file I uploaded?
  - id: delete_file_v1_files__file_id__delete
    intent: Delete a file on the plain endpoint
    question: How do I delete a file I uploaded, without the beta query flag?
  - id: download_file_v1_files__file_id__content_get
    intent: Download a file's content on the plain endpoint
    question: How do I download the actual contents of a stored file?
  - id: beta_download_file_v1_files__file_id__content_get
    intent: Download a file's content via the beta flag
    question: Can I download a file an agent produced through the beta files endpoint?
  - id: beta_get_file_metadata_v1_files__file_id__get
    intent: Get a file's metadata via the beta flag
    question: How do I read a file's metadata through the beta files endpoint?
  - id: beta_delete_file_v1_files__file_id__delete
    intent: Delete a file via the beta flag
    question: Can I delete an uploaded file through the beta files endpoint?
  phrasing_ops: 10
  slug: anthropic-files-api
- baseURL: https://api.anthropic.com/v1
  baseurl_source: declared
  description: Create and manage custom Agent Skills. Skills are filesystem-based directories of instructions, scripts, and resources that Claude loads on demand via progressive disclosure. Workspace-wide sharing. T
  name: Anthropic Skills API
  phrasing_intents:
  - id: create_skill_v1_skills_post
    intent: Upload a new skill with a display name
    question: How do I upload a new Agent Skill from a set of files?
  - id: list_skills_v1_skills_get
    intent: List skills on the plain skills endpoint
    question: Which Agent Skills are available to my account on /v1/skills without the beta flag?
  - id: get_skill_v1_skills__skill_id__get
    intent: Get a skill on the plain endpoint
    question: What details does the plain skills endpoint return for one skill?
  - id: delete_skill_v1_skills__skill_id__delete
    intent: Delete a skill on the plain endpoint
    question: How do I remove a custom skill using the non-beta-flag skills path?
  - id: create_skill_version_v1_skills__skill_id__versions_post
    intent: Publish a new version of a skill (plain endpoint)
    question: How do I publish updated files as a new version of an existing skill without the beta flag?
  - id: list_skill_versions_v1_skills__skill_id__versions_get
    intent: List a skill's versions on the plain endpoint
    question: Which versions of a skill exist, listed without the beta query flag?
  - id: get_skill_version_v1_skills__skill_id__versions__version__get
    intent: Get one skill version on the plain endpoint
    question: What does a specific version of a skill contain, read without the beta flag?
  - id: delete_skill_version_v1_skills__skill_id__versions__version__delete
    intent: Delete one skill version on the plain endpoint
    question: How do I delete an old version of a skill without the beta query flag?
  phrasing_ops: 17
  slug: anthropic-skills-api
- baseURL: https://api.anthropic.com/v1
  baseurl_source: declared
  description: Reusable, versioned agent configurations
  name: Anthropic Agents API
  phrasing_intents:
  - id: BetaArchiveAgent
    intent: Archive an agent (beta-flagged endpoint)
    question: Can I archive an agent through the ?beta=true agents endpoint?
  - id: BetaListAgentVersions
    intent: Page through an agent's versions
    question: Can I page through an agent's versions a few at a time?
  - id: BetaGetAgent
    intent: Retrieve a specific agent version
    question: Can I fetch an older version of an agent's configuration?
  - id: BetaUpdateAgent
    intent: Update an agent, version optional
    question: Can I update an agent's multiagent settings?
  - id: BetaCreateAgent
    intent: Create an agent (beta-flagged endpoint)
    question: Can I create an agent through the ?beta=true route with metadata attached?
  - id: BetaListAgents
    intent: List agents with date and archive filters
    question: Which agents were created in a given date range?
  - id: createAgent
    intent: Define a reusable, versioned agent
    question: How do I define a reusable agent with a system prompt and tools?
  - id: listAgents
    intent: List the workspace's agents
    question: What agents have been defined in my workspace?
  phrasing_ops: 12
  slug: anthropic-agents-api
- baseURL: https://api.anthropic.com/v1
  baseurl_source: declared
  description: Monitor and manage API keys
  name: Anthropic Api Keys API
  phrasing_intents:
  - id: listApiKeys
    intent: List the organization's API keys
    question: Which API keys exist in my organization?
  - id: getApiKey
    intent: Look up an API key
    question: What details can I see about one API key?
  - id: updateApiKey
    intent: Rename or deactivate an API key
    question: How do I deactivate an API key without deleting it?
  phrasing_ops: 3
  slug: anthropic-api-keys-api
- baseURL: https://api.anthropic.com/v1
  baseurl_source: declared
  description: Service-level cost reporting
  name: Anthropic Cost API
  phrasing_intents:
  - id: getCostReport
    intent: Get the organization's cost report
    question: How much has my organization spent on Claude this month?
  phrasing_ops: 1
  slug: anthropic-cost-api
- baseURL: https://api.anthropic.com/v1
  baseurl_source: declared
  description: Container configuration for agent sessions
  name: Anthropic Environments API
  phrasing_intents:
  - id: beta_archive_environment_v1_environments__environment_id__archive_post
    intent: Archive an environment so no new sessions use it
    question: How do I stop an environment from being used for new agent sessions?
  - id: beta_poll_work_v1_environments__environment_id__work_poll_get
    intent: Poll an environment's queue for new work
    question: How does a self-hosted sandbox worker pick up the next piece of work for an environment?
  - id: beta_get_environment_stats_v1_environments__environment_id__work_stats_get
    intent: Get work queue statistics for an environment
    question: How backed up is the work queue for my sandbox environment?
  - id: beta_acknowledge_work_v1_environments__environment_id__work__work_id__ack_post
    intent: Acknowledge a work item a worker picked up
    question: How does a worker confirm it has claimed a work item from the environment queue?
  - id: beta_record_heartbeat_v1_environments__environment_id__work__work_id__heartbeat_post
    intent: Send a heartbeat to keep a work item leased
    question: How does a worker keep its lease on a long-running work item alive?
  - id: beta_stop_work_v1_environments__environment_id__work__work_id__stop_post
    intent: Stop a work item in an environment
    question: How do I halt a work item that's running in a self-hosted environment?
  - id: beta_get_work_v1_environments__environment_id__work__work_id__get
    intent: Get one work item from an environment
    question: What is the current state of a specific work item in my environment?
  - id: beta_update_work_v1_environments__environment_id__work__work_id__post
    intent: Update a work item's metadata
    question: Can I attach or change metadata on a work item in an environment queue?
  phrasing_ops: 19
  slug: anthropic-environments-api
- baseURL: https://api.anthropic.com/v1
  baseurl_source: declared
  description: User messages and tool results sent to a session
  name: Anthropic Events API
  phrasing_intents:
  - id: sendSessionEvents
    intent: Send user messages or interrupts to a session
    question: How do I send a user message or tool result to a running agent session?
  - id: streamSession
    intent: Stream a session's agent activity
    question: How can I watch an agent's messages and tool calls live as a session runs?
  phrasing_ops: 2
  slug: anthropic-events-api
- baseURL: https://api.anthropic.com/v1
  baseurl_source: declared
  description: Retrieve organization information and settings
  name: Anthropic Organization API
  phrasing_intents:
  - id: getCurrentOrganization
    intent: Get my current organization
    question: Which organization is my API key tied to?
  phrasing_ops: 1
  slug: anthropic-organization-api
- baseURL: https://api.anthropic.com/v1
  baseurl_source: declared
  description: Create and manage organization invitations
  name: Anthropic Organization Invites API
  phrasing_intents:
  - id: listOrganizationInvites
    intent: List pending organization invites
    question: Which invitations to my organization are still pending?
  - id: createOrganizationInvite
    intent: Invite someone to the organization
    question: How do I invite a new teammate to our Anthropic organization?
  - id: getOrganizationInvite
    intent: Look up an organization invite
    question: Has the person I invited accepted yet?
  - id: deleteOrganizationInvite
    intent: Revoke an organization invite
    question: Can I cancel an invitation before it's accepted?
  phrasing_ops: 4
  slug: anthropic-organization-invites-api
- baseURL: https://api.anthropic.com/v1
  baseurl_source: declared
  description: Manage organization members and their roles
  name: Anthropic Organization Members API
  phrasing_intents:
  - id: listOrganizationMembers
    intent: List members of the organization
    question: Who are the members of my organization?
  - id: getOrganizationMember
    intent: Get an organization member's details
    question: What role does a specific user have in my organization?
  - id: updateOrganizationMember
    intent: Change an organization member's role
    question: How do I promote or demote someone in my organization?
  - id: removeOrganizationMember
    intent: Remove a user from the organization
    question: How do I take someone out of my organization?
  phrasing_ops: 4
  slug: anthropic-organization-members-api
- baseURL: https://api.anthropic.com/v1
  baseurl_source: declared
  description: APIs for generating well-written prompts for specified tasks
  name: Anthropic Prompt Generation API
  phrasing_intents:
  - id: generatePrompt
    intent: Generate a prompt for a task
    question: Can Claude write a good prompt for me if I just describe the task?
  phrasing_ops: 1
  slug: anthropic-prompt-generation-api
- baseURL: https://api.anthropic.com/v1
  baseurl_source: declared
  description: APIs for enhancing existing prompts with feedback
  name: Anthropic Prompt Improvement API
  phrasing_intents:
  - id: improvePrompt
    intent: Improve a prompt based on feedback
    question: How can I get an existing prompt rewritten to work better?
  phrasing_ops: 1
  slug: anthropic-prompt-improvement-api
- baseURL: https://api.anthropic.com/v1
  baseurl_source: declared
  description: APIs for converting prompts into reusable templates with variables
  name: Anthropic Prompt Templatization API
  phrasing_intents:
  - id: templatizePrompt
    intent: Turn a prompt into a reusable template
    question: How can I pull the specific values out of a prompt into template variables?
  phrasing_ops: 1
  slug: anthropic-prompt-templatization-api
- baseURL: https://api.anthropic.com/v1
  baseurl_source: declared
  description: Stateful agent execution instances
  name: Anthropic Sessions API
  phrasing_intents:
  - id: BetaArchiveSession
    intent: Archive an agent session
    question: How do I archive an agent session I no longer need so it drops out of my default list?
  - id: BetaStreamSessionEvents
    intent: Stream a session's events live
    question: How can I watch a running agent session's events as they happen?
  - id: BetaListEvents
    intent: List past events in a session
    question: Where can I page through the full event history of an agent session?
  - id: BetaSendEvents
    intent: Send events into an agent session
    question: How do I post a user message into an agent session with the beta sessions API?
  - id: BetaGetResource
    intent: Get a resource attached to a session
    question: How do I look up one resource that's mounted on an agent session?
  - id: BetaDeleteResource
    intent: Remove a resource from a session
    question: What is the way to detach a resource from an agent session?
  - id: BetaUpdateResource
    intent: Refresh a session resource's access token
    question: Need to rotate the authorization token on a resource already attached to a session?
  - id: BetaListResources
    intent: List resources attached to a session
    question: Which resources are currently mounted on my agent session?
  phrasing_ops: 25
  slug: anthropic-sessions-api
- baseURL: https://api.anthropic.com/v1
  baseurl_source: declared
  description: Token usage and consumption reporting
  name: Anthropic Usage API
  phrasing_intents:
  - id: getMessagesUsageReport
    intent: Report token usage by day, model and workspace
    question: How many tokens did my organization use each day last month?
  phrasing_ops: 1
  slug: anthropic-usage-api
- baseURL: https://api.anthropic.com/v1
  baseurl_source: declared
  description: Manage workspace membership and roles
  name: Anthropic Workspace Members API
  phrasing_intents:
  - id: listWorkspaceMembers
    intent: List a workspace's members
    question: Who has access to a particular workspace?
  - id: addWorkspaceMember
    intent: Add a user to a workspace
    question: How do I give a teammate access to a workspace?
  - id: getWorkspaceMember
    intent: Look up a user's workspace membership
    question: What role does a specific user have in this workspace?
  - id: updateWorkspaceMember
    intent: Change a member's workspace role
    question: How do I change someone's role in a workspace?
  - id: removeWorkspaceMember
    intent: Remove a user from a workspace
    question: How do I revoke a user's access to one workspace?
  phrasing_ops: 5
  slug: anthropic-workspace-members-api
- baseURL: https://api.anthropic.com/v1
  baseurl_source: declared
  description: Create and manage workspaces within an organization
  name: Anthropic Workspaces API
  phrasing_intents:
  - id: listWorkspaces
    intent: List the organization's workspaces
    question: Which workspaces exist in my organization?
  - id: createWorkspace
    intent: Create a workspace
    question: How do I add a new workspace to my organization?
  - id: getWorkspace
    intent: Get a workspace's details
    question: What settings does a particular workspace have?
  - id: updateWorkspace
    intent: Rename a workspace
    question: How do I rename a workspace?
  - id: archiveWorkspace
    intent: Archive a workspace and make it read-only
    question: What happens to a workspace when I archive it?
  phrasing_ops: 5
  slug: anthropic-workspaces-api
- baseURL: https://api.anthropic.com/v1
  baseurl_source: declared
  description: The Anthropic API API from Anthropic — 0 operation(s) for anthropic api.
  name: Anthropic API
  slug: anthropic-anthropic-api-api
- baseURL: https://api.anthropic.com/v1
  baseurl_source: declared
  description: The Complete API from Anthropic — 1 operation(s) for complete.
  name: Anthropic Complete API
  phrasing_intents:
  - id: complete_post
    intent: Generate a legacy text completion
    question: Is there still a legacy endpoint that completes a raw Human/Assistant prompt?
  phrasing_ops: 1
  slug: anthropic-complete-api
- baseURL: https://api.anthropic.com/v1
  baseurl_source: declared
  description: The Deployment Runs API from Anthropic — 1 operation(s) for deployment runs.
  name: Anthropic Deployment Runs API
  phrasing_intents:
  - id: BetaGetDeploymentRun
    intent: Get one run of a deployment
    question: What happened during a specific deployment run?
  - id: BetaListDeploymentRuns
    intent: List deployment runs and find failures
    question: Which runs has a deployment made recently?
  phrasing_ops: 2
  slug: anthropic-deployment-runs-api
- baseURL: https://api.anthropic.com/v1
  baseurl_source: declared
  description: The Deployments API from Anthropic — 5 operation(s) for deployments.
  name: Anthropic Deployments API
  phrasing_intents:
  - id: BetaArchiveDeployment
    intent: Archive an agent deployment
    question: How do I archive a deployment I don't need anymore?
  - id: BetaPauseDeployment
    intent: Pause a scheduled deployment
    question: How do I temporarily stop a deployment from running on its schedule?
  - id: BetaRunDeploymentNow
    intent: Trigger a deployment run immediately
    question: Can I kick off a deployment right away instead of waiting for its schedule?
  - id: BetaUnpauseDeployment
    intent: Resume a paused deployment
    question: How do I restart a deployment I paused earlier?
  - id: BetaGetDeployment
    intent: Get a deployment's configuration
    question: What agent, environment and schedule does a deployment use?
  - id: BetaUpdateDeployment
    intent: Change a deployment's schedule, agent or budget
    question: How do I change when a deployment runs?
  - id: BetaCreateDeployment
    intent: Create a scheduled agent deployment
    question: How do I set up an agent to run on a schedule?
  - id: BetaListDeployments
    intent: List deployments by agent or status
    question: Which deployments are set up for a given agent?
  phrasing_ops: 8
  slug: anthropic-deployments-api
- baseURL: https://api.anthropic.com/v1
  baseurl_source: declared
  description: The Dreams API from Anthropic — 3 operation(s) for dreams.
  name: Anthropic Dreams API
  phrasing_intents:
  - id: BetaArchiveDream
    intent: Archive a dream
    question: How do I archive a dream I no longer need?
  - id: BetaCancelDream
    intent: Cancel a running dream
    question: Can I stop a dream that's still running?
  - id: BetaGetDream
    intent: Check on a dream
    question: What's the status of a dream I started?
  - id: BetaCreateDream
    intent: Start a dream
    question: How do I start a new dream over a set of inputs?
  - id: BetaListDreams
    intent: List dreams
    question: Which dreams have I run recently?
  phrasing_ops: 5
  slug: anthropic-dreams-api
- baseURL: https://api.anthropic.com/v1
  baseurl_source: declared
  description: The Memory Stores API from Anthropic — 7 operation(s) for memory stores.
  name: Anthropic Memory Stores API
  phrasing_intents:
  - id: BetaArchiveMemoryStore
    intent: Archive a memory store
    question: How do I retire a memory store without deleting its contents?
  - id: BetaGetMemory
    intent: Read one memory from a store
    question: How can an app read back a single memory an agent saved?
  - id: BetaUpdateMemory
    intent: Edit or rename a memory
    question: Can I rename a memory's path without changing its content?
  - id: BetaDeleteMemory
    intent: Delete a memory
    question: How do I delete a single memory an agent wrote?
  - id: BetaCreateMemory
    intent: Write a new memory into a store
    question: How do I seed a memory store with a file before an agent runs?
  - id: BetaListMemories
    intent: Browse the memories in a store
    question: What memories has my agent saved in a store?
  - id: BetaRedactMemoryVersion
    intent: Redact a past memory version
    question: How do I scrub sensitive content from an old version of a memory?
  - id: BetaGetMemoryVersion
    intent: Retrieve a past memory version
    question: What did a memory look like at a specific earlier version?
  phrasing_ops: 14
  slug: anthropic-memory-stores-api
- baseURL: https://api.anthropic.com/v1
  baseurl_source: declared
  description: The Organizations API from Anthropic — 43 operation(s) for organizations.
  name: Anthropic Organizations API
  phrasing_intents:
  - id: beta_get_api_key_v1_organizations_api_keys__api_key_id__get
    intent: Look up an API key's details
    question: What can I see about one of my organization's API keys, like its name and status?
  - id: beta_update_api_key_v1_organizations_api_keys__api_key_id__post
    intent: Rename or deactivate an API key
    question: Can I rename an existing API key without rotating it?
  - id: beta_list_api_keys_v1_organizations_api_keys_get
    intent: List the organization's API keys
    question: Which API keys exist across my Anthropic organization?
  - id: beta_get_cost_report_v1_organizations_cost_report_get
    intent: Get the organization's cost report
    question: How much has my organization spent on the API since the start of the month?
  - id: beta_validate_external_key_v1_organizations_external_keys__external_key_id__validate_post
    intent: Test an external KMS key config
    question: How can I confirm that Anthropic can actually encrypt and decrypt with my KMS key?
  - id: beta_get_external_key_v1_organizations_external_keys__external_key_id__get
    intent: Retrieve an external key config
    question: Where can I see the settings of a customer-managed encryption key config?
  - id: beta_update_external_key_v1_organizations_external_keys__external_key_id__post
    intent: Edit an external key config
    question: Can I change the KMS provider config after a workspace already uses the key?
  - id: beta_delete_external_key_v1_organizations_external_keys__external_key_id__delete
    intent: Delete an external key config
    question: Why would deleting an external key config be rejected?
  phrasing_ops: 68
  slug: anthropic-organizations-api
- baseURL: https://api.anthropic.com/v1
  baseurl_source: declared
  description: The Tunnels API from Anthropic — 7 operation(s) for tunnels.
  name: Anthropic Tunnels API
  phrasing_intents:
  - id: BetaArchiveTunnel
    intent: Archive a tunnel permanently
    question: How do I permanently decommission an MCP tunnel?
  - id: BetaArchiveTunnelCertificate
    intent: Stop trusting a tunnel CA certificate
    question: How do I remove one CA certificate from the set Anthropic trusts for my tunnel?
  - id: BetaGetTunnelCertificate
    intent: Retrieve a tunnel certificate
    question: Can I look up one CA certificate registered on a tunnel?
  - id: BetaCreateTunnelCertificate
    intent: Register a CA certificate on a tunnel
    question: How do I let Anthropic verify my MCP gateway's server certificate?
  - id: BetaListTunnelCertificates
    intent: List a tunnel's certificates
    question: Which CA certificates are registered on my tunnel?
  - id: BetaRevealTunnelToken
    intent: Reveal a tunnel's connector token
    question: Where do I get the connector token my tunnel client needs?
  - id: BetaRotateTunnelToken
    intent: Rotate a tunnel's connector token
    question: What should I do if my tunnel's connector token leaked?
  - id: BetaGetTunnel
    intent: Retrieve a tunnel
    question: What hostname was allocated to one of my tunnels?
  phrasing_ops: 10
  slug: anthropic-tunnels-api
- baseURL: https://api.anthropic.com/v1
  baseurl_source: declared
  description: The User Profiles API from Anthropic — 2 operation(s) for user profiles.
  name: Anthropic User Profiles API
  phrasing_intents:
  - id: BetaCreateEnrollmentUrl
    intent: Create an enrollment link for a user profile
    question: How do I get a link that lets one of my end users enroll their profile?
  - id: BetaGetUserProfile
    intent: Get a user profile
    question: What details are stored on one of my user profiles?
  - id: BetaUpdateUserProfile
    intent: Update a user profile's name or access
    question: How do I change the access type on an existing user profile?
  - id: BetaCreateUserProfile
    intent: Create a user profile for an end user
    question: How do I register one of my end users as a user profile?
  - id: BetaListUserProfiles
    intent: List user profiles
    question: Which user profiles have I created?
  phrasing_ops: 5
  slug: anthropic-user-profiles-api
- baseURL: https://api.anthropic.com/v1
  baseurl_source: declared
  description: The Vaults API from Anthropic — 6 operation(s) for vaults.
  name: Anthropic Vaults API
  phrasing_intents:
  - id: BetaArchiveVault
    intent: Archive a credential vault
    question: How do I archive a vault I no longer want agents to use?
  - id: BetaArchiveCredential
    intent: Archive a credential in a vault
    question: Can I archive one credential in a vault instead of deleting it?
  - id: BetaValidateCredential
    intent: Validate an MCP OAuth credential
    question: How do I check that a stored MCP OAuth credential still works?
  - id: BetaGetCredential
    intent: Get a credential stored in a vault
    question: What details can I see about one credential stored in a vault?
  - id: BetaUpdateCredential
    intent: Update a vault credential's auth or name
    question: How do I replace the secret or auth details on an existing vault credential?
  - id: BetaDeleteCredential
    intent: Delete a credential from a vault
    question: How do I permanently delete a credential from a vault?
  - id: BetaCreateCredential
    intent: Store a new credential in a vault
    question: How do I add a new credential to a vault for my agents to use?
  - id: BetaListCredentials
    intent: List the credentials in a vault
    question: Which credentials are stored in my vault?
  phrasing_ops: 13
  slug: anthropic-vaults-api
arazzos:
- description: Create a batch, request cancellation, then poll until it leaves the canceling state.
  name: Anthropic Cancel a Message Batch and Confirm
  slug: anthropic-batch-cancel-and-confirm-workflow
- description: Submit a message batch, poll until processing ends, then fetch the JSONL results.
  name: Anthropic Create Batch, Poll, and Retrieve Results
  slug: anthropic-batch-create-poll-results-workflow
- description: Estimate input token usage for a prompt, then send the message only when it fits a budget.
  name: Anthropic Count Tokens Then Create Message
  slug: anthropic-count-tokens-then-message-workflow
- description: Create a workspace, add a user to it, then confirm the member appears in the roster.
  name: Anthropic Create Workspace and Add a Member
  slug: anthropic-create-workspace-and-add-member-workflow
- description: List available models, confirm a chosen model exists, then create a message with it.
  name: Anthropic Discover a Model and Send a Message
  slug: anthropic-discover-model-and-message-workflow
- description: Send an organization invite, then read it back and branch on whether it is still pending.
  name: Anthropic Invite an Org Member and Confirm
  slug: anthropic-invite-org-member-and-confirm-workflow
- description: List message batches, inspect the most recent one, and pull its results if it has ended.
  name: Anthropic List Batches and Fetch Latest Results
  slug: anthropic-list-batches-and-fetch-latest-results-workflow
- description: Find an org member by email, create a workspace, and add that member to it.
  name: Anthropic Onboard an Org Member into a Workspace
  slug: anthropic-onboard-member-to-workspace-workflow
- description: Create a workspace, add a member as a developer, then promote them to workspace admin.
  name: Anthropic Provision and Promote a Workspace Member
  slug: anthropic-provision-and-promote-workspace-member-workflow
- description: Upload a file, confirm it appears in the file list, then delete it to clean up.
  name: Anthropic Upload, List, and Clean Up a File
  slug: anthropic-upload-list-and-cleanup-file-workflow
- description: Upload a file, read back its metadata, and download its content when it is downloadable.
  name: Anthropic Upload, Verify, and Download a File
  slug: anthropic-upload-verify-download-file-workflow
artifact_total: 121
asyncapis:
- description: 'AsyncAPI specification modeling the Server-Sent Events (SSE) stream produced by Anthropic''s Messages API when `"stream": true` is set on a POST to `/v1/messages`. Transport: HTTP/1.1 with `Content-Typ'
  name: Anthropic Messages Streaming API
  slug: anthropic-asyncapi
- description: ''
  name: Anthropic Webhooks
  slug: anthropic-webhooks
collections:
- collection_type: postman
  name: Anthropic Admin API
  slug: postman-anthropic-admin-api
- collection_type: postman
  name: Anthropic Claude Code Analytics API
  slug: postman-anthropic-claude-code-analytics-api
- collection_type: postman
  name: Anthropic Files API
  slug: postman-anthropic-files-api
- collection_type: postman
  name: Anthropic Managed Agents API
  slug: postman-anthropic-managed-agents-api
- collection_type: postman
  name: Anthropic Message Batches API
  slug: postman-anthropic-message-batches-api
- collection_type: postman
  name: Anthropic Messages API
  slug: postman-anthropic-messages-api
- collection_type: postman
  name: Anthropic Models API
  slug: postman-anthropic-models-api
- collection_type: postman
  name: Anthropic Prompt Tools API
  slug: postman-anthropic-prompts-api
- collection_type: postman
  name: Anthropic Skills API
  slug: postman-anthropic-skills-api
- collection_type: postman
  name: Anthropic Token Counting API
  slug: postman-anthropic-token-counting-api
- collection_type: postman
  name: Anthropic Usage and Cost API
  slug: postman-anthropic-usage-cost-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Anthropic Admin API
  slug: open-anthropic-admin-api
- collection_type: open
  name: Anthropic Admin Agents API
  slug: open-anthropic-agents-api
- collection_type: open
  name: Anthropic Admin Agents Api Keys API
  slug: open-anthropic-api-keys-api
- collection_type: open
  name: Anthropic Admin Agents Claude Code Analytics API
  slug: open-anthropic-claude-code-analytics-api
- collection_type: open
  name: Anthropic Admin Agents Cost API
  slug: open-anthropic-cost-api
- collection_type: open
  name: Anthropic Admin Agents Environments API
  slug: open-anthropic-environments-api
- collection_type: open
  name: Anthropic Admin Agents Events API
  slug: open-anthropic-events-api
- collection_type: open
  name: Anthropic Admin Agents Files API
  slug: open-anthropic-files-api
- collection_type: open
  name: Anthropic Managed Agents API
  slug: open-anthropic-managed-agents-api
- collection_type: open
  name: Anthropic Admin Agents Message Batches API
  slug: open-anthropic-message-batches-api
- collection_type: open
  name: Anthropic Admin Agents Messages API
  slug: open-anthropic-messages-api
- collection_type: open
  name: Anthropic Admin Agents Models API
  slug: open-anthropic-models-api
- collection_type: open
  name: Anthropic Admin Agents Organization API
  slug: open-anthropic-organization-api
- collection_type: open
  name: Anthropic Admin Agents Organization Invites API
  slug: open-anthropic-organization-invites-api
- collection_type: open
  name: Anthropic Admin Agents Organization Members API
  slug: open-anthropic-organization-members-api
- collection_type: open
  name: Anthropic Admin Agents Prompt Generation API
  slug: open-anthropic-prompt-generation-api
- collection_type: open
  name: Anthropic Admin Agents Prompt Improvement API
  slug: open-anthropic-prompt-improvement-api
- collection_type: open
  name: Anthropic Admin Agents Prompt Templatization API
  slug: open-anthropic-prompt-templatization-api
- collection_type: open
  name: Anthropic Prompt Tools API
  slug: open-anthropic-prompts-api
- collection_type: open
  name: Anthropic Admin Agents Sessions API
  slug: open-anthropic-sessions-api
- collection_type: open
  name: Anthropic Admin Agents Skill Versions API
  slug: open-anthropic-skill-versions-api
- collection_type: open
  name: Anthropic Admin Agents Skills API
  slug: open-anthropic-skills-api
- collection_type: open
  name: Anthropic Admin Agents Token Counting API
  slug: open-anthropic-token-counting-api
- collection_type: open
  name: Anthropic Admin Agents Tokens API
  slug: open-anthropic-tokens-api
- collection_type: open
  name: Anthropic Admin Agents Usage API
  slug: open-anthropic-usage-api
- collection_type: open
  name: Anthropic Usage and Cost API
  slug: open-anthropic-usage-cost-api
- collection_type: open
  name: Anthropic Admin Agents Workspace Members API
  slug: open-anthropic-workspace-members-api
- collection_type: open
  name: Anthropic Admin Agents Workspaces API
  slug: open-anthropic-workspaces-api
common:
- group: company
  title: ''
  type: Website
  url: https://www.anthropic.com/
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/anthropic/refs/heads/main/capabilities/anthropic-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/anthropic-capability-edges.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/anthropic/refs/heads/main/agentic-access/anthropic-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/anthropic-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/anthropic/refs/heads/main/security/anthropic-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/anthropic-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/anthropic/refs/heads/main/authentication/anthropic-authentication.yml
  title: ''
  type: Authentication
  url: authentication/anthropic-authentication.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/anthropic/refs/heads/main/packages/anthropic-packages.yml
  title: ''
  type: Packages
  url: packages/anthropic-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/anthropic/refs/heads/main/well-known/anthropic-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/anthropic-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/anthropic/refs/heads/main/well-known/anthropic-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/anthropic-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/anthropic/refs/heads/main/mcp/anthropic-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/anthropic-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/anthropic/refs/heads/main/llms/anthropic-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/anthropic-llms.txt
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/anthropic/refs/heads/main/conformance/anthropic-conformance.yml
  title: ''
  type: Conformance
  url: conformance/anthropic-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/anthropic/refs/heads/main/errors/anthropic-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/anthropic-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/anthropic/refs/heads/main/lifecycle/anthropic-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/anthropic-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/anthropic/refs/heads/main/conventions/anthropic-conventions.yml
  title: ''
  type: Conventions
  url: conventions/anthropic-conventions.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/anthropic/refs/heads/main/changelog/anthropic-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/anthropic-changelog.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/anthropic/refs/heads/main/cli/anthropic-cli.yml
  title: ''
  type: CLI
  url: cli/anthropic-cli.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/anthropic/refs/heads/main/data-model/anthropic-data-model.yml
  title: ''
  type: DataModel
  url: data-model/anthropic-data-model.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/anthropic/refs/heads/main/security/anthropic-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/anthropic-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/anthropic/refs/heads/main/security/anthropic-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/anthropic-trust-center.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/anthropic/refs/heads/main/overlays/anthropic-messages-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/anthropic-messages-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/anthropic/refs/heads/main/overlays/anthropic-models-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/anthropic-models-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/anthropic/refs/heads/main/overlays/anthropic-message-batches-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/anthropic-message-batches-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/anthropic/refs/heads/main/overlays/anthropic-files-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/anthropic-files-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/anthropic/refs/heads/main/overlays/anthropic-admin-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/anthropic-admin-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/anthropic/refs/heads/main/overlays/anthropic-prompts-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/anthropic-prompts-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/anthropic/refs/heads/main/overlays/anthropic-token-counting-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/anthropic-token-counting-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/anthropic/refs/heads/main/overlays/anthropic-skills-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/anthropic-skills-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/anthropic/refs/heads/main/overlays/anthropic-usage-cost-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/anthropic-usage-cost-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/anthropic/refs/heads/main/overlays/anthropic-claude-code-analytics-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/anthropic-claude-code-analytics-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/anthropic/refs/heads/main/overlays/anthropic-managed-agents-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/anthropic-managed-agents-overlay.yaml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/anthropic/overview
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/anthropic/refs/heads/main/arazzo/anthropic-batch-cancel-and-confirm-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/anthropic-batch-cancel-and-confirm-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/anthropic/refs/heads/main/arazzo/anthropic-batch-create-poll-results-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/anthropic-batch-create-poll-results-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/anthropic/refs/heads/main/arazzo/anthropic-count-tokens-then-message-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/anthropic-count-tokens-then-message-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/anthropic/refs/heads/main/arazzo/anthropic-create-workspace-and-add-member-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/anthropic-create-workspace-and-add-member-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/anthropic/refs/heads/main/arazzo/anthropic-discover-model-and-message-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/anthropic-discover-model-and-message-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/anthropic/refs/heads/main/arazzo/anthropic-invite-org-member-and-confirm-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/anthropic-invite-org-member-and-confirm-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/anthropic/refs/heads/main/arazzo/anthropic-list-batches-and-fetch-latest-results-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/anthropic-list-batches-and-fetch-latest-results-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/anthropic/refs/heads/main/arazzo/anthropic-onboard-member-to-workspace-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/anthropic-onboard-member-to-workspace-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/anthropic/refs/heads/main/arazzo/anthropic-provision-and-promote-workspace-member-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/anthropic-provision-and-promote-workspace-member-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/anthropic/refs/heads/main/arazzo/anthropic-upload-list-and-cleanup-file-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/anthropic-upload-list-and-cleanup-file-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/anthropic/refs/heads/main/arazzo/anthropic-upload-verify-download-file-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/anthropic-upload-verify-download-file-workflow.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/anthropicresearch
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/anthropics/anthropic-quickstarts
- group: start
  title: ''
  type: Portal
  url: https://platform.claude.com/docs/en/home
- group: docs
  title: ''
  type: Documentation
  url: https://docs.anthropic.com/en/api/messages
- group: operate
  title: ''
  type: StatusPage
  url: https://status.anthropic.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://platform.claude.com/docs/en/release-notes/overview
- group: docs
  title: ''
  type: Documentation
  url: https://platform.claude.com/login
- group: operate
  title: ''
  type: RateLimits
  url: https://docs.anthropic.com/en/api/rate-limits
- group: other
  title: ''
  type: Tiers
  url: https://docs.anthropic.com/en/api/service-tiers
- group: design
  title: ''
  type: ErrorCodes
  url: https://docs.anthropic.com/en/api/errors
- group: docs
  title: ''
  type: Documentation
  url: https://docs.anthropic.com/en/api/client-sdks
- group: design
  title: ''
  type: Versioning
  url: https://docs.anthropic.com/en/api/versioning
- group: other
  title: ''
  type: Regions
  url: https://docs.anthropic.com/en/api/supported-regions
- group: operate
  title: ''
  type: Support
  url: https://support.claude.com/en/collections/4078531-api
- group: commercial
  title: ''
  type: Plans
  url: https://www.anthropic.com/pricing
- group: commercial
  title: ''
  type: Pricing
  url: https://www.anthropic.com/pricing#api
- group: start
  title: ''
  type: Portal
  url: https://www.anthropic.com/api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.anthropic.com/en/docs/get-started
- group: other
  title: ''
  type: Glossary
  url: https://docs.anthropic.com/en/docs/about-claude/glossary
- group: docs
  title: ''
  type: Documentation
  url: https://www.anthropic.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.anthropic.com/legal/privacy
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.claude.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.anthropic.com
- group: company
  title: ''
  type: Blog
  url: https://www.anthropic.com/news
- group: company
  title: ''
  type: Blog
  url: https://www.anthropic.com/engineering
- group: start
  title: ''
  type: Signup
  url: https://console.anthropic.com/
- group: start
  title: ''
  type: Signup
  url: https://platform.claude.com/
- group: start
  title: ''
  type: Sandbox
  url: https://platform.claude.com/playground
- group: docs
  title: ''
  type: Documentation
  url: https://docs.anthropic.com/en/api/beta-headers
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.anthropic.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.anthropic.com/legal/aup
- group: docs
  title: ''
  type: Documentation
  url: https://docs.anthropic.com/en/api/administration-api
- group: docs
  title: ''
  type: Documentation
  url: https://docs.anthropic.com/en/api/usage-cost-api
- group: docs
  title: ''
  type: Documentation
  url: https://docs.anthropic.com/en/api/claude-code-analytics-api
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/anthropics
- group: build
  title: ''
  type: SDKs
  url: https://github.com/anthropics/anthropic-sdk-python
- group: build
  title: ''
  type: SDKs
  url: https://github.com/anthropics/anthropic-sdk-typescript
- group: build
  title: ''
  type: SDKs
  url: https://github.com/anthropics/anthropic-sdk-java
- group: build
  title: ''
  type: SDKs
  url: https://github.com/anthropics/anthropic-sdk-go
- group: build
  title: ''
  type: SDKs
  url: https://github.com/anthropics/anthropic-sdk-ruby
- group: build
  title: ''
  type: SDKs
  url: https://github.com/anthropics/anthropic-sdk-csharp
- group: build
  title: ''
  type: SDKs
  url: https://github.com/anthropics/anthropic-sdk-php
- group: build
  title: ''
  type: SDKs
  url: https://github.com/anthropics/claude-agent-sdk-python
- group: build
  title: ''
  type: Tools
  url: https://github.com/anthropics/claude-code
- group: build
  title: ''
  type: Tools
  url: https://github.com/anthropics/claude-code-action
- group: build
  title: ''
  type: Tools
  url: https://github.com/anthropics/skills
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/anthropics/claude-cookbooks
- group: learn
  title: ''
  type: Courses
  url: https://github.com/anthropics/courses
- group: learn
  title: ''
  type: Courses
  url: https://github.com/anthropics/prompt-eng-interactive-tutorial
- group: build
  title: ''
  type: Plugins
  url: https://github.com/anthropics/claude-plugins-official
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/anthropics/financial-services
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/anthropics/claude-for-legal
- group: build
  title: ''
  type: Plugins
  url: https://github.com/anthropics/knowledge-work-plugins
- group: learn
  title: ''
  type: Training
  url: https://www.anthropic.com/learn
- group: operate
  title: ''
  type: Forums
  url: https://discord.com/invite/6PPFFzqPDZ
- group: docs
  title: ''
  type: Documentation
  url: https://www.postman.com/postman/anthropic-apis/overview
- group: docs
  title: ''
  type: Documentation
  url: https://docs.anthropic.com/en/docs/build-with-claude/token-counting
- group: docs
  title: ''
  type: Documentation
  url: https://docs.anthropic.com/en/docs/build-with-claude/data-residency
- group: docs
  title: ''
  type: Documentation
  url: https://docs.anthropic.com/en/api/messages-streaming
- group: docs
  title: ''
  type: Documentation
  url: https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/overview
- group: docs
  title: ''
  type: Documentation
  url: https://docs.anthropic.com/en/docs/agents-and-tools/computer-use
- group: docs
  title: ''
  type: Documentation
  url: https://docs.anthropic.com/en/docs/build-with-claude/extended-thinking
- group: docs
  title: ''
  type: Documentation
  url: https://docs.anthropic.com/en/docs/build-with-claude/citations
- group: docs
  title: ''
  type: Documentation
  url: https://docs.anthropic.com/en/docs/build-with-claude/prompt-caching
- group: docs
  title: ''
  type: Documentation
  url: https://docs.anthropic.com/en/docs/build-with-claude/batch-processing
- group: docs
  title: ''
  type: Documentation
  url: https://docs.anthropic.com/en/build-with-claude/compaction
- group: docs
  title: ''
  type: Documentation
  url: https://docs.anthropic.com/en/agents-and-tools/agent-skills/overview
- group: docs
  title: ''
  type: Documentation
  url: https://docs.anthropic.com/en/agents-and-tools/tool-use/memory-tool
- group: docs
  title: ''
  type: Documentation
  url: https://docs.anthropic.com/en/api/openai-sdk
- group: docs
  title: ''
  type: Documentation
  url: https://docs.anthropic.com/en/api/claude-on-amazon-bedrock
- group: docs
  title: ''
  type: Documentation
  url: https://docs.anthropic.com/en/api/claude-on-vertex-ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.anthropic.com/en/build-with-claude/claude-platform-on-aws
- group: docs
  title: ''
  type: Documentation
  url: https://docs.anthropic.com/en/build-with-claude/claude-in-microsoft-foundry
- group: other
  title: ''
  type: Models
  url: https://docs.anthropic.com/en/docs/about-claude/models/all-models
- group: build
  title: ''
  type: SDKs
  url: https://docs.anthropic.com/en/docs/claude-code/sdk
- group: build
  title: ''
  type: SDKs
  url: https://docs.anthropic.com/en/api/sdks/cli
- group: docs
  title: ''
  type: Documentation
  url: https://modelcontextprotocol.io
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/modelcontextprotocol
- group: docs
  title: ''
  type: Documentation
  url: https://platform.claude.com/docs/en/build-with-claude/structured-outputs
- group: docs
  title: ''
  type: Documentation
  url: https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview
- group: start
  title: ''
  type: Portal
  url: https://www.anthropic.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.anthropic.com/
- group: docs
  title: ''
  type: Documentation
  url: https://platform.claude.com/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.anthropic.com/en/api/getting-started
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/anthropic/refs/heads/main/plans/anthropic-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/anthropic-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/anthropic/refs/heads/main/rate-limits/anthropic-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/anthropic-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/anthropic/refs/heads/main/finops/anthropic-finops.yml
  title: ''
  type: FinOps
  url: finops/anthropic-finops.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/anthropic/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/anthropic/refs/heads/main/mcp/anthropic-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/anthropic-tool-crosswalk.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/anthropic/refs/heads/main/sandbox/anthropic-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/anthropic-sandbox.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/anthropic/refs/heads/main/asyncapi/anthropic-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/anthropic-webhooks.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: https://docs.anthropic.com/llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/anthropic/refs/heads/main/security/anthropic-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/anthropic-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/anthropic/refs/heads/main/security/anthropic-trust-center.yml
  title: ''
  type: Compliance
  url: security/anthropic-trust-center.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/anthropic/refs/heads/main/lifecycle/anthropic-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/anthropic-lifecycle.yml
- group: docs
  title: ''
  type: APIReference
  url: https://platform.claude.com/docs/en/api/overview
- group: start
  title: ''
  type: DeveloperPortal
  url: https://platform.claude.com/docs/en/home
created: '2025-08-14T00:00:00.000Z'
description: 'Anthropic is an AI safety company and the creator of the Claude family of large language models (Opus, Sonnet, Haiku, and the Fable/Mythos frontier line). The Claude Developer Platform exposes them through a single REST API at api.anthropic.com: the Messages API for text, vision, tool use, thinking, streaming and structured outputs; Message Batches for asynchronous work at half price; Files, Token Counting, Models, and experimental Prompt Tools; Managed Agents with sessions, environments, memory stores, vaults and scheduled deployments; a Skills API; and an Admin API for organizations, workspaces, members, invites and API keys. Authentication is x-api-key with a required anthropic-version date header and dated anthropic-beta opt-ins. Anthropic also authors two of the open standards the agent ecosystem runs on — the Model Context Protocol and the Agent Skills specification — and ships Claude Code, the terminal agentic coding tool, which doubles as a first-party stdio MCP server.'
features:
- Claude Opus 4.7 — most capable generally available model for complex reasoning and agentic coding
- Claude Sonnet 4.6 — balanced model combining speed and intelligence with 1M context window
- Claude Haiku 4.5 — fastest model with near-frontier intelligence
- Messages API with text, vision, tool use, extended thinking, streaming, structured outputs
- Prompt caching with automatic and manual breakpoints, 5-minute and 1-hour TTLs, cache reads at 10% of input price
- Server-side compaction API for effectively infinite conversations on Opus 4.6/4.7 and Sonnet 4.6
- Memory tool (client-side) for cross-conversation persistence with ZDR support
- Message Batches API with 50% discount on both input and output tokens
- Files API for upload-once / reuse-many content across Messages and Managed Agents
- Agent Skills API (beta) — packaged domain expertise with progressive disclosure
- Claude Managed Agents (beta) — Agents, Sessions, Environments with SSE streaming and managed sandboxes
- Web Search tool ($10/1,000 searches) and Web Fetch tool (free)
- Code Execution tool — Python + Bash + filesystem in sandbox; 1,550 free container-hours/month
- Computer Use tool for browser and desktop automation (beta)
- Advisor tool (beta) for pairing executor and high-intelligence advisor models
- Tool Search tool and Programmatic Tool Calling
- Token-bucket rate limiting with cache-aware ITPM (cache reads excluded on most models)
- Five usage tiers (Tier 1-4 plus Monthly Invoicing) with automatic advancement
- Usage & Cost Admin API and Claude Code Analytics Admin API for FinOps reporting
- Rate Limits API for programmatic limit inspection
- Workload Identity Federation for short-lived bearer tokens
- Data residency controls (US-only inference at 1.1x pricing for models after Feb 2026)
- Available via Claude API, Claude Platform on AWS, Microsoft Foundry, AWS Bedrock, and Google Vertex AI
- Official SDKs: Python, TypeScript, Java, Go, Ruby, C#, PHP plus the `ant` CLI
- Claude Code (terminal agent) and Claude Code GitHub Action
- Open MCP specification stewardship via modelcontextprotocol.io
finops:
- name: Anthropic Finops
  service_category: AI and Machine Learning
  slug: anthropic-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/anthropic.png
json_schemas:
- name: Anthropic Message
  property_count: 0
  slug: anthropic-message
- name: Anthropic Tool Use
  property_count: 0
  slug: anthropic-tool-use
jsonld:
- class_count: 0
  name: Anthropic Context
  property_count: 18
  slug: anthropic-context
layout: provider
modified: '2026-09-16'
name: Anthropic
nav: Providers
network: true
overview: 'Anthropic publishes 29 APIs on the [APIs.io](https://apis.io/) network, including Messages API, Models API, Files API, and 26 more. Tagged areas include LLM, Anthropic, Artificial Intelligence, Claude, and Foundation Models.


  The Anthropic catalog on APIs.io includes 2 event-driven AsyncAPI specifications, 1 JSON-LD context, and 2 Spectral governance rulesets.


  Anthropic''s developer surface includes authentication, changelog, CLI, documentation, developer portal, support, pricing, and 132 more developer resources.'
plans:
- name: Anthropic Plans Pricing
  plan_count: 5
  slug: anthropic-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 12
  name: Anthropic Rate Limits
  slug: anthropic-rate-limits
rules:
- effective_rule_count: 33
  extends:
  - spectral:asyncapi
  name: Anthropic API Rules
  rule_count: 6
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 5
  slug: anthropic-asyncapi-spectral-rules
- effective_rule_count: 6
  extends: []
  name: Anthropic API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: anthropic-jsonschema-spectral-rules
score:
  band: exemplar
  composite: 78.8
  coverage:
    artifact_dirs: 32
    catalog_earned: 70.5
    catalog_earned_first_party: 0.0
    catalog_gap: 44.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.9
  facets:
    access_clarity: 76.3
    contract_governance: 31.8
    contract_quality: 70.3
    developer_ergonomics: 96.4
    discoverability: 78.6
    operational_transparency: 71.1
  previous_composite: 77.9
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 34
    mcp: derived
    skills: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 2
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 32.7
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  trend: flat
  upsert:
    applies: true
    score: 38.9
screenshot: https://raw.githubusercontent.com/api-evangelist/anthropic/refs/heads/main/screenshots/anthropic-2026-06-20T172029.png
security:
- kind: authentication
  name: Anthropic Authentication
  slug: anthropic-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Anthropic Domain Security
  slug: anthropic-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Anthropic Vulnerability Disclosure
  slug: anthropic-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Anthropic Trust Center
  slug: anthropic-trust-center
  summary_line: SOC 2 Type I, SOC 2 Type II, ISO 27001:2022, ISO/IEC 42001:2023, HIPAA
slug: anthropic
tags:
- LLM
- Anthropic
- Artificial Intelligence
- Claude
- Foundation Models
- Machine Learning
- MCP
- Agents
website: https://www.anthropic.com/
---
