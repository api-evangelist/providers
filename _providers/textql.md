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
  - scopes
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: true
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 62.2
  scored_at: '2026-11-06'
api_count: 8
apis:
- description: TextQL's hosted, remote Model Context Protocol server. Any MCP-compatible client — Claude, Claude Code, Cursor, Windsurf, ChatGPT, Microsoft Copilot — points at the endpoint, authorizes once over OAut
  name: Ana MCP Server
  slug: textql-ana-mcp-server
- baseURL: https://app.textql.com/v2
  baseurl_source: declared
  description: The AgentService API from TextQL — 13 operation(s) for agentservice.
  name: TextQL Agent Service API
  phrasing_intents:
  - id: AgentService_CreateAgent
    intent: Create an agent
    question: How do I set up a new TextQL agent with its own prompt?
  - id: AgentService_DeleteAgent
    intent: Delete an agent
    question: How do I remove an agent permanently?
  - id: AgentService_DuplicateAgent
    intent: Duplicate an agent
    question: Can I clone an existing agent with its configuration?
  - id: AgentService_GetAgent
    intent: Get an agent's configuration
    question: What prompt and schedule is an agent configured with?
  - id: AgentService_GetAgentDBSchema
    intent: Get the schema of an agent's database
    question: What tables does a stateful agent keep in its own database?
  - id: AgentService_GetAgentDBTablePreview
    intent: Preview rows in an agent's database table
    question: Can I peek at the rows an agent has saved in a table?
  - id: AgentService_GetAgentRun
    intent: Get a single agent run
    question: What happened during a particular agent run?
  - id: AgentService_ListAgentRuns
    intent: List an agent's runs
    question: When has my agent run, and did those runs succeed?
  phrasing_ops: 13
  slug: textql-agentservice-api
- baseURL: https://app.textql.com/v2
  baseurl_source: declared
  description: Mint and revoke scoped platform API keys
  name: TextQL API Keys API
  phrasing_intents:
  - id: v2.createApiKey
    intent: Create a role-scoped API key
    question: How do I mint a new API key limited to certain roles?
  - id: v2.listApiKeys
    intent: List platform API keys
    question: Which TextQL API keys exist in my organization?
  - id: v2.rotateApiKey
    intent: Rotate an API key
    question: How do I replace a leaked API key with a fresh secret but the same scope?
  - id: v2.revokeApiKey
    intent: Revoke an API key
    question: How do I permanently disable an API key?
  phrasing_ops: 4
  slug: textql-api-keys-api
- baseURL: https://app.textql.com/v2
  baseurl_source: declared
  description: 'AppService manages data apps: the generative app execution primitive. An app is agent-authored single-file HTML/JS/CSS executing in a CSP sandbox, fed a snapshot of its declared data sources. First-cl'
  name: TextQL App Service API
  phrasing_intents:
  - id: AppService_AppHeartbeat
    intent: Keep a viewed app's compute worker alive
    question: How do I keep a data app's compute worker warm while someone is viewing it?
  - id: AppService_CreateApp
    intent: Create a new data app
    question: How do I build a new data app in TextQL from code and data sources?
  - id: AppService_DeleteApp
    intent: Delete a data app
    question: How do I permanently remove an app I no longer need?
  - id: AppService_DuplicateApp
    intent: Duplicate an app into a copy I own
    question: Can I make my own copy of an app someone shared with me?
  - id: AppService_GetApp
    intent: Get a data app's details
    question: How do I look up the code and settings of a specific app?
  - id: AppService_GetAppDBSchema
    intent: Get the schema of an app's database
    question: Which tables and columns does my app's built-in database have?
  - id: AppService_GetAppDBTablePreview
    intent: Preview rows in an app database table
    question: Can I peek at the first rows of a table in my app's database?
  - id: AppService_GetAppMemberState
    intent: Read my saved per-member state for an app
    question: Does an app remember my own settings, and how do I read them back?
  phrasing_ops: 24
  slug: textql-appservice-api
- baseURL: https://app.textql.com/v2
  baseurl_source: declared
  description: The AuditLogService API from TextQL — 11 operation(s) for auditlogservice.
  name: TextQL Audit Log Service API
  phrasing_intents:
  - id: AuditLogService_ConfigureOtlpExport
    intent: Set up audit log export over OTLP
    question: How do I stream TextQL audit logs to my OpenTelemetry collector?
  - id: AuditLogService_ConfigureS3Export
    intent: Set up audit log export to S3
    question: How do I export audit logs to an S3 bucket?
  - id: AuditLogService_DeleteOtlpExportConfig
    intent: Remove the OTLP audit export config
    question: How do I stop sending audit logs to my OTLP collector?
  - id: AuditLogService_DeleteS3ExportConfig
    intent: Remove the S3 audit export config
    question: How do I stop exporting audit logs to S3?
  - id: AuditLogService_GetOtlpExportConfig
    intent: View the OTLP audit export config
    question: Where are my audit logs being sent over OTLP?
  - id: AuditLogService_GetS3ExportConfig
    intent: View the S3 audit export config
    question: Which S3 bucket are my audit logs exported to?
  - id: AuditLogService_ListAuditLogs
    intent: Search the audit log
    question: Who changed what in my organization, and when?
  - id: AuditLogService_TestOtlpExportConnection
    intent: Test an OTLP audit export endpoint
    question: Can I check that my OTLP collector is reachable before enabling audit export?
  phrasing_ops: 11
  slug: textql-auditlogservice-api
- baseURL: https://app.textql.com/v2
  baseurl_source: declared
  description: Review, approve, and deny Ontology changes
  name: TextQL Changes API
  phrasing_intents:
  - id: v2.listChanges
    intent: List Ontology changes
    question: What Ontology changes are open for review in my organization?
  - id: v2.getChange
    intent: Get an Ontology change with its diffs
    question: How do I see the file diffs in a single Ontology change?
  - id: v2.approveChange
    intent: Approve an Ontology change
    question: How do I approve a change so it merges into the Ontology?
  - id: v2.denyChange
    intent: Deny an Ontology change
    question: How do I reject a proposed Ontology change?
  - id: v2.restoreChange
    intent: Reopen a denied Ontology change
    question: Can I bring a denied Ontology change back to open?
  phrasing_ops: 5
  slug: textql-changes-api
- baseURL: https://app.textql.com/v2
  baseurl_source: declared
  description: Create and manage AI chat sessions
  name: TextQL Chat API
  phrasing_intents:
  - id: v2.listChats
    intent: List my API chats
    question: Which chats has my API key created?
  - id: v2.createChat
    intent: Ask a data question and wait for the answer
    question: How do I ask TextQL a question about my data and get the full answer back in one response?
  - id: v2.streamChat
    intent: Ask a data question and stream the answer
    question: Can I get the answer to a data question streamed back as it's generated?
  - id: v2.getChat
    intent: Get a chat with its messages
    question: How do I retrieve a chat along with its messages and generated assets?
  - id: v2.getChatCells
    intent: List the execution cells of a chat
    question: Can I see the SQL and Python the agent ran to produce an answer?
  - id: v2.getChatCell
    intent: Get one execution cell from a chat
    question: How do I fetch a single step from a chat by its cell ID?
  - id: v2.cancelStream
    intent: Cancel a streaming chat response
    question: How do I stop a REST chat stream that's taking too long?
  - id: v2.listModels
    intent: List models I can run chats on
    question: Which models is my organization allowed to use for chats?
  phrasing_ops: 8
  slug: textql-chat-api
- baseURL: https://app.textql.com/v2
  baseurl_source: declared
  description: The ChatService API from TextQL — 38 operation(s) for chatservice.
  name: TextQL Chat Service API
  phrasing_intents:
  - id: ChatService_ApproveContextPromptChange
    intent: Approve a proposed context prompt change
    question: Can I accept the context prompt edit the agent suggested in a chat, with my own tweaks?
  - id: ChatService_ApproveOntologyChange
    intent: Approve a proposed ontology change
    question: How do I accept an ontology change the agent proposed during a chat?
  - id: ChatService_AttachAgentToChat
    intent: Attach an agent to a chat
    question: Can I bring one of my saved agents into an existing chat conversation?
  - id: ChatService_AttachApp
    intent: Attach an app to a chat
    question: How do I add a TextQL app to a chat so the analysis can use it?
  - id: ChatService_AttachDashboard
    intent: Attach a dashboard to a chat
    question: Can I give a chat access to an existing dashboard as context?
  - id: ChatService_AttachDataset
    intent: Attach a dataset to a chat
    question: How do I make an uploaded dataset available inside a chat?
  - id: ChatService_BookmarkChat
    intent: Bookmark a chat
    question: Can I bookmark a chat so it's easy to find later?
  - id: ChatService_CancelStream
    intent: Stop a running chat response
    question: How do I stop the agent mid-answer through the Connect chat service?
  phrasing_ops: 38
  slug: textql-chatservice-api
- baseURL: https://app.textql.com/v2
  baseurl_source: declared
  description: List available data connectors
  name: TextQL Connectors API
  phrasing_intents:
  - id: v2.listConnectors
    intent: List data connectors
    question: Which data connectors does my organization have?
  - id: v2.createConnector
    intent: Create a data connector
    question: How do I connect a new database?
  - id: v2.listConnectorTypes
    intent: List supported connector types and fields
    question: What kinds of data sources can I connect?
  - id: v2.testConnector
    intent: Test a connector configuration
    question: Can I check a database connection works before saving the connector?
  - id: v2.updateConnector
    intent: Update a data connector
    question: Can I change a connector's settings without re-entering its password?
  - id: v2.deleteConnector
    intent: Delete a data connector
    question: How do I remove a data connector?
  - id: v2.getConnectorAccess
    intent: Get who can access a connector
    question: Who has access to a specific data connector?
  - id: v2.updateConnectorAccess
    intent: Replace a connector's access grants
    question: How do I share a connector with specific members, roles or groups?
  phrasing_ops: 8
  slug: textql-connectors-api
- baseURL: https://app.textql.com/v2
  baseurl_source: declared
  description: The ConnectorService API from TextQL — 17 operation(s) for connectorservice.
  name: TextQL Connector Service API
  phrasing_intents:
  - id: ConnectorService_CreateConnector
    intent: Create a data connector
    question: How do I connect TextQL to my data warehouse?
  - id: ConnectorService_DeleteConnector
    intent: Delete a data connector
    question: How do I remove a database connection I no longer use?
  - id: ConnectorService_DuplicateConnector
    intent: Duplicate a data connector
    question: Can I clone an existing connector to make a variant of it?
  - id: ConnectorService_ExecuteQuery
    intent: Run a SQL query on a connector
    question: How do I run raw SQL against one of my connected databases?
  - id: ConnectorService_GetConnector
    intent: Get a connector's details
    question: How do I look up the configuration of a single connector?
  - id: ConnectorService_GetConnectorCellDurations
    intent: Get query cell durations for a connector
    question: Which queries against a connector have been the slowest lately?
  - id: ConnectorService_GetConnectorChats
    intent: List chats that use a connector
    question: Which chats have queried a particular data connection?
  - id: ConnectorService_GetConnectorDashboards
    intent: List dashboards built on a connector
    question: Which dashboards depend on a given connector?
  phrasing_ops: 17
  slug: textql-connectorservice-api
- baseURL: https://app.textql.com/v2
  baseurl_source: declared
  description: The DashboardService API from TextQL — 24 operation(s) for dashboardservice.
  name: TextQL Dashboard Service API
  phrasing_intents:
  - id: DashboardService_CheckDashboardHealth
    intent: Check the health of dashboards
    question: Are any of my dashboards broken?
  - id: DashboardService_CreateDashboard
    intent: Create a dashboard
    question: How do I build a new dashboard?
  - id: DashboardService_CreateDashboardFolder
    intent: Create a dashboard folder
    question: Can I organize dashboards into folders?
  - id: DashboardService_DeleteDashboard
    intent: Delete a dashboard
    question: How do I delete a dashboard I no longer need?
  - id: DashboardService_DeleteDashboardFolder
    intent: Delete a dashboard folder
    question: Can I remove an empty dashboard folder?
  - id: DashboardService_DiscardDashboardChanges
    intent: Discard unpublished dashboard changes
    question: Can I throw away edits to a dashboard I haven't published yet?
  - id: DashboardService_DuplicateDashboard
    intent: Duplicate a dashboard
    question: Can I clone a dashboard as a starting point?
  - id: DashboardService_GetDashboard
    intent: Get a dashboard
    question: What's in a specific dashboard?
  phrasing_ops: 24
  slug: textql-dashboardservice-api
- baseURL: https://app.textql.com/v2
  baseurl_source: declared
  description: The DatasetService API from TextQL — 14 operation(s) for datasetservice.
  name: TextQL Dataset Service API
  phrasing_intents:
  - id: DatasetService_CreateFolder
    intent: Create a dataset folder
    question: How do I organize my datasets into folders?
  - id: DatasetService_CreatePowerBIDataset
    intent: Create a dataset from Power BI
    question: Can I bring Power BI reports and datasets into TextQL as a dataset?
  - id: DatasetService_CreateTableauDataset
    intent: Create a dataset from Tableau
    question: Can I turn Tableau views or datasources into a dataset?
  - id: DatasetService_CreateUploadPresignUrl
    intent: Get an upload URL for a new dataset file
    question: How do I upload a CSV or spreadsheet as a dataset?
  - id: DatasetService_DeleteDataset
    intent: Delete a dataset
    question: How do I delete a dataset I uploaded?
  - id: DatasetService_ExportDataset
    intent: Export a dataset file
    question: How do I download a dataset in its original format?
  - id: DatasetService_GetDataset
    intent: Get a dataset's metadata
    question: How do I look up the metadata for one dataset?
  - id: DatasetService_GetDatasetStats
    intent: Get statistics for a dataset
    question: Can I see column statistics for a dataset?
  phrasing_ops: 14
  slug: textql-datasetservice-api
- baseURL: https://app.textql.com/v2
  baseurl_source: declared
  description: The MCPService API from TextQL — 7 operation(s) for mcpservice.
  name: TextQL MCP Service API
  phrasing_intents:
  - id: MCPService_ClearOAuthToken
    intent: Clear an MCP server's OAuth token
    question: How do I disconnect my OAuth login from an MCP server?
  - id: MCPService_DeleteMCPServer
    intent: Delete an MCP server
    question: How do I remove an MCP server from TextQL?
  - id: MCPService_GetMCPServers
    intent: List configured MCP servers
    question: Which MCP servers are connected to my workspace?
  - id: MCPService_HandleOAuthCallback
    intent: Complete an MCP server's OAuth flow
    question: What do I do with the code returned after authorizing an MCP server?
  - id: MCPService_InitiateOAuthFlow
    intent: Start OAuth for an MCP server
    question: How do I authorize TextQL to use an MCP server that needs OAuth?
  - id: MCPService_ToggleMCPServer
    intent: Enable or disable an MCP server
    question: Can I temporarily switch off an MCP server?
  - id: MCPService_UpsertMCPServers
    intent: Add or update MCP servers
    question: How do I add a new MCP server to TextQL?
  phrasing_ops: 7
  slug: textql-mcpservice-api
- baseURL: https://app.textql.com/v2
  baseurl_source: declared
  description: The Members API from TextQL — 5 operation(s) for members.
  name: TextQL Members API
  phrasing_intents:
  - id: v2.listMembers
    intent: List organization members
    question: Who are the people in my TextQL organization?
  - id: v2.inviteMember
    intent: Invite a member by email
    question: How do I invite a colleague to my organization?
  - id: v2.deleteMember
    intent: Remove a member from the organization
    question: How do I remove someone who left the company?
  - id: v2.getMemberRoles
    intent: List a member's roles
    question: What roles does a particular member have?
  - id: v2.assignMemberRole
    intent: Assign a role to a member
    question: How do I give a member an additional role?
  - id: v2.removeMemberRole
    intent: Remove a role from a member
    question: How do I take a role away from a member?
  phrasing_ops: 6
  slug: textql-members-api
- baseURL: https://app.textql.com/v2
  baseurl_source: declared
  description: The MetricsExportService API from TextQL — 5 operation(s) for metricsexportservice.
  name: TextQL Metrics Export Service API
  phrasing_intents:
  - id: MetricsExportService_ConfigureMetricsExport
    intent: Configure metrics export
    question: Can I send TextQL metrics to my own OpenTelemetry collector?
  - id: MetricsExportService_DeleteMetricsExportConfig
    intent: Delete the metrics export configuration
    question: How do I stop exporting metrics entirely?
  - id: MetricsExportService_GetMetricsExportConfig
    intent: Get the metrics export configuration
    question: Where are our metrics currently being exported?
  - id: MetricsExportService_TestMetricsExportConnection
    intent: Test an OTLP metrics export connection
    question: Can I verify my OTLP collector is reachable before saving?
  - id: MetricsExportService_TriggerMetricsPush
    intent: Push metrics immediately
    question: Can I force a metrics push right now instead of waiting for the interval?
  phrasing_ops: 5
  slug: textql-metricsexportservice-api
- baseURL: https://app.textql.com/v2
  baseurl_source: declared
  description: The ObservabilityService API from TextQL — 30 operation(s) for observabilityservice.
  name: TextQL Observability Service API
  phrasing_intents:
  - id: ObservabilityService_ActivateCustomTopic
    intent: Activate a custom topic
    question: How do I turn a custom topic on so new chats get tagged with it?
  - id: ObservabilityService_BackfillCustomTopic
    intent: Backfill a custom topic over past chats
    question: Can a new custom topic be applied to chats from before it existed?
  - id: ObservabilityService_BackfillThreadWarnings
    intent: Backfill warnings on past chat threads
    question: Can I generate thread warnings for older chats retroactively?
  - id: ObservabilityService_CreateCustomTopic
    intent: Create a custom topic for tagging chats
    question: How do I define a custom topic to track what people ask about?
  - id: ObservabilityService_DeactivateCustomTopic
    intent: Deactivate a custom topic
    question: Can I pause a custom topic without deleting it?
  - id: ObservabilityService_DeleteCustomTopic
    intent: Delete a custom topic
    question: How do I permanently remove a custom topic?
  - id: ObservabilityService_ExportObservabilityCsv
    intent: Export observability data as CSV
    question: Can I download observability data as a CSV?
  - id: ObservabilityService_FixCheckRecord
    intent: Fix a failed check record
    question: Can a flagged check record be fixed automatically?
  phrasing_ops: 30
  slug: textql-observabilityservice-api
- baseURL: https://app.textql.com/v2
  baseurl_source: declared
  description: The OntologyManagementService API from TextQL — 69 operation(s) for ontologymanagementservice.
  name: TextQL Ontology Management Service API
  phrasing_intents:
  - id: OntologyManagementService_AddOntologySubmodule
    intent: Add a git submodule to the Ontology
    question: Can I pull another git repository into my TextQL Ontology as a submodule?
  - id: OntologyManagementService_ApprovePatch
    intent: Approve a pending Ontology patch
    question: What do I need to sign off on a patch someone proposed to the Ontology?
  - id: OntologyManagementService_ConfigureOntologyRemote
    intent: Connect the Ontology to a remote git repository
    question: How do I link my Ontology to a hosted git repo so changes sync both ways?
  - id: OntologyManagementService_CreateApprovalRule
    intent: Create an Ontology approval rule
    question: Can I require a certain number of reviewers before Ontology patches merge?
  - id: OntologyManagementService_CreateContextPatchAutoApproveRule
    intent: Create a rule that auto-approves context patches
    question: Can some context patches merge automatically without a human reviewer?
  - id: OntologyManagementService_CreateOntologyDirectory
    intent: Create a folder in the Ontology
    question: How do I add a new folder to the Ontology library?
  - id: OntologyManagementService_CreateOntologyFileUploadUrl
    intent: Get an upload URL for a new Ontology file
    question: How do I upload a large binary file into the Ontology?
  - id: OntologyManagementService_DeleteApprovalRule
    intent: Delete an Ontology approval rule
    question: How do I remove an approval rule that patches no longer need to satisfy?
  phrasing_ops: 69
  slug: textql-ontologymanagementservice-api
- baseURL: https://app.textql.com/v2
  baseurl_source: declared
  description: Create, configure, and run automated playbooks
  name: TextQL Playbooks API
  phrasing_intents:
  - id: v2.listPlaybooks
    intent: List playbooks
    question: Which scheduled playbooks do I have?
  - id: v2.createPlaybook
    intent: Create an empty playbook
    question: How do I start a new recurring report playbook?
  - id: v2.getPlaybook
    intent: Get a playbook and its recent reports
    question: How do I see a playbook's configuration and its latest reports?
  - id: v2.updatePlaybook
    intent: Update a playbook's prompt, schedule or delivery
    question: How do I change when a playbook runs?
  - id: v2.deletePlaybook
    intent: Delete a playbook
    question: How do I delete a playbook I no longer need?
  - id: v2.deployPlaybook
    intent: Deploy a playbook to its schedule
    question: How do I activate a playbook so it runs on schedule?
  - id: v2.runPlaybook
    intent: Run a playbook now
    question: Can I run a playbook immediately and get the report back?
  phrasing_ops: 7
  slug: textql-playbooks-api
- baseURL: https://app.textql.com/v2
  baseurl_source: declared
  description: The PlaybookService API from TextQL — 39 operation(s) for playbookservice.
  name: TextQL Playbook Service API
  phrasing_intents:
  - id: PlaybookService_AttachDashboard
    intent: Attach a dashboard to a playbook
    question: Can a playbook include one of my existing dashboards?
  - id: PlaybookService_AttachDataset
    intent: Attach a dataset to a playbook
    question: How do I give a playbook access to another dataset?
  - id: PlaybookService_CancelTemplateExecution
    intent: Cancel a playbook's template execution
    question: Can I stop a templated playbook run that is still executing?
  - id: PlaybookService_CreatePlaybook
    intent: Create a new playbook
    question: How do I start a new TextQL playbook?
  - id: PlaybookService_DeactivatePlaybook
    intent: Deactivate a playbook
    question: How can I pause a playbook so it stops running on its schedule?
  - id: PlaybookService_DeletePlaybook
    intent: Delete a playbook
    question: How do I permanently remove a playbook?
  - id: PlaybookService_DemoPlaybook
    intent: Generate a demo playbook for a prospect
    question: Can I build a demo playbook from a chat for a specific person and job title?
  - id: PlaybookService_DeployPlaybook
    intent: Deploy a playbook
    question: How do I take a draft playbook live?
  phrasing_ops: 39
  slug: textql-playbookservice-api
- baseURL: https://app.textql.com/v2
  baseurl_source: declared
  description: The PowerBIService API from TextQL — 10 operation(s) for powerbiservice.
  name: TextQL Power BI Service API
  phrasing_intents:
  - id: PowerBIService_ExportPowerBIReportImage
    intent: Export a Power BI report as an image
    question: Can I get a snapshot image of a Power BI report?
  - id: PowerBIService_GeneratePowerBIEmbedToken
    intent: Generate an embed token for a Power BI report
    question: How do I embed a Power BI report inside TextQL?
  - id: PowerBIService_GetPowerBIDatasetPreview
    intent: Preview rows from a Power BI dataset
    question: Can I see sample data from a Power BI dataset before syncing it?
  - id: PowerBIService_GetSyncedPowerBIItems
    intent: List Power BI items already synced
    question: Which Power BI reports and datasets have I already synced into TextQL?
  - id: PowerBIService_ListPowerBIDatasets
    intent: List datasets in a Power BI workspace
    question: What datasets live in a Power BI workspace?
  - id: PowerBIService_ListPowerBIReports
    intent: List reports in a Power BI workspace
    question: Which Power BI reports are available in a workspace?
  - id: PowerBIService_ListPowerBIWorkspaces
    intent: List Power BI workspaces for a connector
    question: Which Power BI workspaces can my connector access?
  - id: PowerBIService_SyncPowerBIItems
    intent: Sync Power BI reports and datasets into TextQL
    question: How do I bring selected Power BI reports and datasets into TextQL?
  phrasing_ops: 10
  slug: textql-powerbiservice-api
- baseURL: https://app.textql.com/v2
  baseurl_source: declared
  description: The Roles API from TextQL — 2 operation(s) for roles.
  name: TextQL Roles API
  phrasing_intents:
  - id: v2.listRoles
    intent: List roles in the organization
    question: Which roles exist in my organization, including built-in ones?
  - id: v2.createRole
    intent: Create a custom role
    question: How do I create a custom role for my team?
  - id: v2.updateRole
    intent: Update a role's name or model settings
    question: Can I restrict which models a role is allowed to use?
  phrasing_ops: 3
  slug: textql-roles-api
- baseURL: https://app.textql.com/v2
  baseurl_source: declared
  description: The SandboxAdminService API from TextQL — 9 operation(s) for sandboxadminservice.
  name: TextQL Sandbox Admin Service API
  slug: textql-sandboxadminservice-api
- baseURL: https://app.textql.com/v2
  baseurl_source: declared
  description: The SandboxCapabilityService API from TextQL — 6 operation(s) for sandboxcapabilityservice.
  name: TextQL Sandbox Capability Service API
  slug: textql-sandboxcapabilityservice-api
- baseURL: https://app.textql.com/v2
  baseurl_source: declared
  description: The SandboxExecService API from TextQL — 5 operation(s) for sandboxexecservice.
  name: TextQL Sandbox Exec Service API
  slug: textql-sandboxexecservice-api
- baseURL: https://app.textql.com/v2
  baseurl_source: declared
  description: The SandboxQueryService API from TextQL — 2 operation(s) for sandboxqueryservice.
  name: TextQL Sandbox Query Service API
  slug: textql-sandboxqueryservice-api
- baseURL: https://app.textql.com/v2
  baseurl_source: declared
  description: Manage Python sandbox environments for code execution
  name: TextQL Sandcastles API
  phrasing_intents:
  - id: v2.listSandboxes
    intent: List my organization's sandcastles
    question: Which Python sandcastles are running in my TextQL organization?
  - id: v2.startSandbox
    intent: Start or restart a sandcastle
    question: How do I spin up a fresh Python sandbox for running code?
  - id: v2.getSandboxStatus
    intent: Check a sandcastle's status and memory
    question: How much memory is my sandbox using right now?
  - id: v2.stopSandbox
    intent: Stop and destroy a sandcastle
    question: How do I shut down a sandcastle I'm done with?
  - id: v2.listSandboxExecutions
    intent: List executions run in a sandcastle
    question: What code has been run in my sandcastle so far?
  - id: v2.executeCode
    intent: Run Python code in a sandcastle
    question: How do I run Python in a sandcastle and get stdout back?
  - id: v2.loadConnectorData
    intent: Load connector data into a sandcastle dataframe
    question: How do I pull query results from a connector into a sandbox dataframe?
  - id: v2.listFiles
    intent: List files in a sandcastle directory
    question: What files are in my sandbox's working directory?
  phrasing_ops: 14
  slug: textql-sandcastles-api
- baseURL: https://app.textql.com/v2
  baseurl_source: declared
  description: The ScimService API from TextQL — 6 operation(s) for scimservice.
  name: TextQL SCIM Service API
  phrasing_intents:
  - id: ScimService_CreateScimOAuthClient
    intent: Create a SCIM OAuth client
    question: How do I set up an OAuth client for SCIM user provisioning?
  - id: ScimService_CreateScimToken
    intent: Create a SCIM bearer token
    question: What token does my identity provider need to provision users over SCIM?
  - id: ScimService_ListScimOAuthClients
    intent: List SCIM OAuth clients
    question: Which SCIM OAuth clients exist for my org?
  - id: ScimService_ListScimTokens
    intent: List SCIM tokens
    question: What SCIM tokens are currently issued?
  - id: ScimService_RevokeScimOAuthClient
    intent: Revoke a SCIM OAuth client
    question: How do I revoke a SCIM OAuth client I no longer use?
  - id: ScimService_RevokeScimToken
    intent: Revoke a SCIM token
    question: Can I revoke a leaked SCIM token?
  phrasing_ops: 6
  slug: textql-scimservice-api
- baseURL: https://app.textql.com/v2
  baseurl_source: declared
  description: The SecretService API from TextQL — 5 operation(s) for secretservice.
  name: TextQL Secret Service API
  phrasing_intents:
  - id: SecretService_DeleteSecret
    intent: Delete a secret
    question: How do I remove a stored secret?
  - id: SecretService_GetMembersWithSecrets
    intent: List members who have stored secrets
    question: Which teammates have stored secrets in TextQL?
  - id: SecretService_ListSecrets
    intent: List secrets
    question: What secrets do I have saved?
  - id: SecretService_PutSecret
    intent: Store a new secret
    question: How do I save an API key so TextQL can use it?
  - id: SecretService_UpdateSecret
    intent: Update an existing secret
    question: Can I rotate the value of a secret I already stored?
  phrasing_ops: 5
  slug: textql-secretservice-api
- baseURL: https://app.textql.com/v2
  baseurl_source: declared
  description: The SettingsService API from TextQL — 7 operation(s) for settingsservice.
  name: TextQL Settings Service API
  phrasing_intents:
  - id: SettingsService_CheckMemberStatus
    intent: Check my membership status
    question: Is my TextQL membership active?
  - id: SettingsService_DeleteOrganizationMember
    intent: Remove a member from the organization
    question: How do I remove someone from my organization?
  - id: SettingsService_GetOrganizationSettings
    intent: View organization settings
    question: What features and default models are configured for my organization?
  - id: SettingsService_InviteOrganizationMember
    intent: Invite someone to the organization
    question: How do I invite a coworker to my TextQL organization?
  - id: SettingsService_ListOrganizationMembers
    intent: List organization members
    question: Who are the members of my organization?
  - id: SettingsService_UpdateOrganizationModelSettings
    intent: Set which AI models the organization can use
    question: How do I change the default model for my whole organization?
  - id: SettingsService_UpdateOrganizationSettings
    intent: Update organization feature settings
    question: How do I turn dashboards or data apps on for my organization?
  phrasing_ops: 7
  slug: textql-settingsservice-api
- baseURL: https://app.textql.com/v2
  baseurl_source: declared
  description: The SlackService API from TextQL — 8 operation(s) for slackservice.
  name: TextQL Slack Service API
  phrasing_intents:
  - id: SlackService_CreateSlackUuid
    intent: Start linking a Slack workspace
    question: How do I begin installing the TextQL app into Slack?
  - id: SlackService_DeleteInstallation
    intent: Uninstall from a Slack workspace
    question: How do I disconnect a Slack workspace?
  - id: SlackService_GetCurrentUser
    intent: Get my linked Slack user
    question: Which Slack user is linked to my account?
  - id: SlackService_HandleSlackOAuthCallback
    intent: Complete the Slack OAuth install
    question: How do I finish a Slack install after the OAuth redirect?
  - id: SlackService_ListChannels
    intent: List Slack channels
    question: Which Slack channels can TextQL post reports to?
  - id: SlackService_ListInstallations
    intent: List Slack installations
    question: Which Slack workspaces are connected to my organization?
  - id: SlackService_ListUsers
    intent: List Slack users
    question: Which Slack users can I tag on a report?
  - id: SlackService_SyncWorkspace
    intent: Sync a Slack workspace
    question: How do I refresh the channels and users from my Slack workspace?
  phrasing_ops: 8
  slug: textql-slackservice-api
- baseURL: https://app.textql.com/v2
  baseurl_source: declared
  description: The TableauService API from TextQL — 13 operation(s) for tableauservice.
  name: TextQL Tableau Service API
  phrasing_intents:
  - id: TableauService_GenerateEmbedToken
    intent: Generate a token to embed a Tableau view
    question: How do I embed a Tableau view inside TextQL?
  - id: TableauService_GetCollectionThumbnail
    intent: Get a Tableau collection's thumbnail
    question: Can I show a preview image for a Tableau collection?
  - id: TableauService_GetConnectedAppStatus
    intent: Check a Tableau connected app's status
    question: Is the Tableau connected app set up correctly for my connector?
  - id: TableauService_GetStarredTableauItems
    intent: List my starred Tableau items
    question: Which Tableau workbooks and views have I starred?
  - id: TableauService_ListTableauDatasources
    intent: List Tableau datasources
    question: What published datasources are on my Tableau site?
  - id: TableauService_ListTableauProjects
    intent: List Tableau projects
    question: Which Tableau projects can I browse?
  - id: TableauService_ListTableauViews
    intent: List views in a Tableau workbook
    question: What sheets and views are inside a Tableau workbook?
  - id: TableauService_ListTableauWorkbooks
    intent: List Tableau workbooks in a project
    question: Which Tableau workbooks are in a given project?
  phrasing_ops: 13
  slug: textql-tableauservice-api
- baseURL: https://app.textql.com/v2
  baseurl_source: declared
  description: The TeamsService API from TextQL — 8 operation(s) for teamsservice.
  name: TextQL Teams Service API
  phrasing_intents:
  - id: TeamsService_CreateTeamsUuid
    intent: Create a linking ID for a Teams install
    question: How do I start connecting TextQL to Microsoft Teams?
  - id: TeamsService_DeleteInstallation
    intent: Remove a Teams installation
    question: How do I disconnect a Teams tenant from TextQL?
  - id: TeamsService_GetCurrentUser
    intent: Get my linked Teams user
    question: Which Teams account is linked to my TextQL login?
  - id: TeamsService_HandleTeamsOAuthCallback
    intent: Complete the Teams OAuth sign-in
    question: After Teams redirects back, how do I finish the OAuth connection?
  - id: TeamsService_ListChannels
    intent: List Teams channels available to TextQL
    question: Which Teams channels can TextQL post into?
  - id: TeamsService_ListInstallations
    intent: List Teams installations
    question: Which Teams tenants have the TextQL app installed?
  - id: TeamsService_ListUsers
    intent: List users from the connected Teams workspace
    question: Which Teams users has TextQL synced?
  - id: TeamsService_SyncWorkspace
    intent: Sync users and channels from a Teams tenant
    question: How do I refresh the users and channels TextQL knows from Teams?
  phrasing_ops: 8
  slug: textql-teamsservice-api
- baseURL: https://app.textql.com/v2
  baseurl_source: declared
  description: Platform Agent Service - External API for triggering agent webhooks
  name: TextQL Textql.rpc.platform.Agent Service API
  phrasing_intents:
  - id: textql.rpc.platform.AgentService.TriggerAgentWebhook
    intent: Trigger an agent run from a webhook
    question: How do I kick off a TextQL agent run from an external webhook?
  phrasing_ops: 1
  slug: textql-textql-rpc-platform-agentservice-api
- baseURL: https://app.textql.com/v2
  baseurl_source: declared
  description: Platform API Access Key Service - External API for managing API access keys
  name: TextQL Textql.rpc.platform.Api Access Key Service API
  phrasing_intents:
  - id: textql.rpc.platform.ApiAccessKeyService.CreateApiAccessKey
    intent: Store a credential for an external API
    question: How do I give the agent a credential to call a third-party API?
  - id: textql.rpc.platform.ApiAccessKeyService.DeleteApiAccessKey
    intent: Delete a stored API credential
    question: How do I remove an external API credential the agent was using?
  - id: textql.rpc.platform.ApiAccessKeyService.ListApiAccessKeys
    intent: List stored API credentials
    question: Which external API credentials have been stored?
  - id: textql.rpc.platform.ApiAccessKeyService.ListApiProviders
    intent: List supported external API providers
    question: Which external API providers can I store credentials for?
  - id: textql.rpc.platform.ApiAccessKeyService.UpdateApiAccessKey
    intent: Update a stored API credential
    question: How do I change which hosts an existing API credential applies to?
  phrasing_ops: 5
  slug: textql-textql-rpc-platform-apiaccesskeyservice-api
- baseURL: https://app.textql.com/v2
  baseurl_source: declared
  description: Platform Chat Service - External API for chat management
  name: TextQL Textql.rpc.platform.Chat Service API
  phrasing_intents:
  - id: textql.rpc.platform.ChatService.CancelStream
    intent: Cancel a streaming chat response
    question: Can I stop an answer that's still streaming?
  - id: textql.rpc.platform.ChatService.Chat
    intent: Ask TextQL a question
    question: How do I ask a question about my data in plain English?
  - id: textql.rpc.platform.ChatService.GetChat
    intent: Get a chat conversation
    question: Can I retrieve a past chat and its answers?
  - id: textql.rpc.platform.ChatService.ListChats
    intent: List and search chats
    question: Which chats have I had recently?
  phrasing_ops: 4
  slug: textql-textql-rpc-platform-chatservice-api
- baseURL: https://app.textql.com/v2
  baseurl_source: declared
  description: Platform Connector Service - External API for connector management
  name: TextQL Textql.rpc.platform.Connector Service API
  phrasing_intents:
  - id: textql.rpc.platform.ConnectorService.ListConnectors
    intent: List my organization's connectors
    question: Which data connectors does my organization have?
  phrasing_ops: 1
  slug: textql-textql-rpc-platform-connectorservice-api
- baseURL: https://app.textql.com/v2
  baseurl_source: declared
  description: Platform Playbook Service - External API for playbook management
  name: TextQL Textql.rpc.platform.Playbook Service API
  phrasing_intents:
  - id: textql.rpc.platform.PlaybookService.CreatePlaybook
    intent: Create a playbook via the platform API
    question: How do I create a playbook through the v1 platform endpoint?
  - id: textql.rpc.platform.PlaybookService.DeletePlaybook
    intent: Delete a playbook
    question: How do I delete a playbook using the platform API?
  - id: textql.rpc.platform.PlaybookService.DeployPlaybook
    intent: Deploy a playbook
    question: How do I take a playbook live from the platform API?
  - id: textql.rpc.platform.PlaybookService.GetPlaybook
    intent: Get a playbook's details
    question: What's configured on one playbook?
  - id: textql.rpc.platform.PlaybookService.ListPlaybooks
    intent: List and search playbooks
    question: Which playbooks exist in my organization?
  - id: textql.rpc.platform.PlaybookService.RunPlaybook
    intent: Run a playbook now
    question: Can I trigger a playbook on demand?
  - id: textql.rpc.platform.PlaybookService.UpdatePlaybook
    intent: Update a playbook
    question: Can I change a playbook's prompt, schedule or model?
  phrasing_ops: 7
  slug: textql-textql-rpc-platform-playbookservice-api
- baseURL: https://app.textql.com/v2
  baseurl_source: declared
  description: Platform Sandbox Service - External API for creating and managing Python sandbox environments
  name: TextQL Textql.rpc.platform.Sandbox Service API
  slug: textql-textql-rpc-platform-sandboxservice-api
- baseURL: https://app.textql.com/mcp
  baseurl_source: declared
  description: RBAC service for managing roles, permissions, and access control
  name: TextQL RBAC Service API
  phrasing_intents:
  - id: RBACService_ApproveAccessRequest
    intent: Approve an access request
    question: How do I grant a teammate's pending request to access a chat or dashboard?
  - id: RBACService_AssignPermissionToRole
    intent: Add a single permission to a role
    question: How do I give a role one extra permission?
  - id: RBACService_AssignRoleToMember
    intent: Assign a role to a member over RPC
    question: How do I give a member a role through the RBAC service?
  - id: RBACService_CreateApiKey
    intent: Create an API key for a member
    question: How do I issue an API key on behalf of another member?
  - id: RBACService_CreatePersonalApiKey
    intent: Create a personal API key
    question: How do I create an API key for myself?
  - id: RBACService_CreateRole
    intent: Create a role over RPC
    question: How do I define a new custom role through the RBAC service?
  - id: RBACService_CreateServiceAccount
    intent: Create a service account
    question: How do I set up a non-human service account for automation?
  - id: RBACService_CreateServiceAccountApiKey
    intent: Create an API key for a service account
    question: How do I generate credentials for a service account?
  phrasing_ops: 37
  slug: textql-rbac-service-api
artifact_total: 55
asyncapis:
- description: ''
  name: Textql Webhooks
  slug: textql-webhooks
common:
- group: other
  href: https://artifacts.apis.io/textql/capabilities/textql-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/textql-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/textql/overlays/textql-v2-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/textql-v2-overlay.yaml
- group: other
  href: https://artifacts.apis.io/textql/overlays/textql-v1-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/textql-v1-overlay.yaml
- group: other
  href: https://artifacts.apis.io/textql/overlays/textql-platform-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/textql-platform-api-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://textql.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.textql.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.textql.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.textql.com/api-reference/v2/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.textql.com/core/get-started/quickstart
- group: company
  title: ''
  type: Blog
  url: https://textql.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/TextQLLabs
- group: commercial
  title: ''
  type: Pricing
  url: https://textql.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.textql.com/
- group: start
  title: ''
  type: Login
  url: https://app.textql.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.textql.com/
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.textql.com/
- group: auth
  href: https://artifacts.apis.io/textql/security/textql-trust-center.yml
  title: ''
  type: Compliance
  url: security/textql-trust-center.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.textql.com/product/changelog
- group: other
  href: https://artifacts.apis.io/textql/a2a/textql-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/textql-a2a.yml
- group: agent
  href: https://artifacts.apis.io/textql/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/textql/llms/textql-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/textql-llms.txt
- group: agent
  href: https://artifacts.apis.io/textql/well-known/textql-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/textql-well-known.yml
- group: other
  href: https://artifacts.apis.io/textql/well-known/textql-openid-configuration.json
  title: ''
  type: OpenIDConnectDiscovery
  url: well-known/textql-openid-configuration.json
- group: build
  href: https://artifacts.apis.io/textql/packages/textql-packages.yml
  title: ''
  type: Packages
  url: packages/textql-packages.yml
- group: build
  href: https://artifacts.apis.io/textql/packages/textql-packages.yml
  title: ''
  type: SDKs
  url: packages/textql-packages.yml
- group: design
  href: https://artifacts.apis.io/textql/lifecycle/textql-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/textql-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/textql/lifecycle/textql-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/textql-lifecycle.yml
- group: auth
  href: https://artifacts.apis.io/textql/security/textql-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/textql-domain-security.yml
- group: commercial
  href: https://artifacts.apis.io/textql/plans/textql-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/textql-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/textql/rate-limits/textql-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/textql-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/textql/conformance/textql-conformance.yml
  title: ''
  type: Conformance
  url: conformance/textql-conformance.yml
- group: operate
  href: https://artifacts.apis.io/textql/changelog/textql-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/textql-changelog.yml
- group: design
  href: https://artifacts.apis.io/textql/components/textql-components.yml
  title: ''
  type: Components
  url: components/textql-components.yml
- group: build
  href: https://artifacts.apis.io/textql/cli/textql-cli.yml
  title: ''
  type: CLI
  url: cli/textql-cli.yml
- group: design
  href: https://artifacts.apis.io/textql/conventions/textql-conventions.yml
  title: ''
  type: Conventions
  url: conventions/textql-conventions.yml
- group: design
  href: https://artifacts.apis.io/textql/data-model/textql-data-model.yml
  title: ''
  type: DataModel
  url: data-model/textql-data-model.yml
- group: auth
  href: https://artifacts.apis.io/textql/authentication/textql-authentication.yml
  title: ''
  type: Authentication
  url: authentication/textql-authentication.yml
- group: auth
  href: https://artifacts.apis.io/textql/scopes/textql-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/textql-scopes.yml
- group: design
  href: https://artifacts.apis.io/textql/errors/textql-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/textql-problem-types.yml
- group: agent
  href: https://artifacts.apis.io/textql/mcp/textql-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/textql-mcp.yml
- group: build
  href: https://artifacts.apis.io/textql/mcp/textql-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/textql-tool-crosswalk.yml
- group: design
  href: https://artifacts.apis.io/textql/asyncapi/textql-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/textql-webhooks.yml
- group: operate
  title: ''
  type: Support
  url: mailto:support@textql.com
created: '2026-08-30'
description: TextQL is an enterprise AI data platform built around Ana, an AI data scientist that connects to a company's warehouses, databases, BI tools and SaaS APIs and answers questions in plain language. Ana writes SQL, runs Python in a managed gVisor sandbox, searches the web, and produces charts, dashboards, scheduled reports (Playbooks) and long-running monitors (Agents) on top of a governed Ontology semantic layer. TextQL ships a public REST platform API in two generations — a v1 Connect-RPC surface and a REST-native v2 — plus an OAuth-authorized remote MCP server that exposes Ana to Claude, Cursor, ChatGPT, Copilot and any MCP-compatible client. First-party TypeScript and Python SDKs, embeddable iframe surfaces for Ana, dashboards and data apps, SAML/OIDC single sign-on with SCIM 2.0 provisioning, and self-hosted Helm deployment into a customer VPC round out the developer surface.
finops:
- has_sources: true
  method: derived
  name: Textql Finops
  primary_unit: subscription
  service_category: ''
  slug: textql-finops
  template: false
image: https://raw.githubusercontent.com/api-evangelist/textql/main/images/textql-og-card.png
layout: provider
mcp_servers:
- description: Remote MCP server at app.textql.com requiring OAuth; 6 tools listed.
  name: Ana MCP Server
  slug: ana-mcp-server
modified: '2026-08-30'
name: TextQL
nav: Providers
network: true
overview: 'TextQL publishes 39 API contracts indexed on the [APIs.io](https://apis.io/) network, including Agent Service API, API Keys API, App Service API, and 36 more. Tagged areas include Company, Artificial Intelligence, Analytics, Business Intelligence, and Data.


  The TextQL catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  TextQL''s developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, signup flow, changelog, and 36 more developer resources.'
plans:
- name: Textql Plans Pricing
  plan_count: 3
  slug: textql-plans-pricing
- name: Textql Price Estimates
  plan_count: 0
  slug: textql-price-estimates
random_paper: 2
rate_limits:
- limit_count: 0
  name: Textql Rate Limits
  slug: textql-rate-limits
rules:
- authorship: generated
  effective_rule_count: 95
  extends:
  - spectral:oas
  name: TextQL API Rules
  rule_count: 54
  severity_counts:
    error: 33
    hint: 0
    info: 3
    warn: 18
  slug: textql-rules
scopes:
- name: Textql Scopes
  scope_count: 34
  slug: textql-scopes
  summary_line: 34 scopes
score:
  band: exemplar
  composite: 73.3
  coverage:
    artifact_dirs: 33
    catalog_earned: 59.5
    catalog_earned_first_party: 12.0
    catalog_gap: 55.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 78.9
    contract_governance: 31.8
    contract_quality: 52.3
    developer_ergonomics: 78.6
    discoverability: 80.0
    operational_transparency: 42.1
  previous_composite: 73.3
  provenance:
    conformance: first-party
    contracts:
      callable: 84.2
      derived: 0
      marker_coverage: 0.0
      total: 38
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 29.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 100.0
screenshot: https://apis.io/screenshots/textql/textql-2026-09-02T163306.png
security:
- kind: authentication
  name: Textql Authentication
  slug: textql-authentication
  summary_line: apiKey/http/oauth2/openIdConnect · 5 schemes
- kind: domain-security
  name: Textql Domain Security
  slug: textql-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Textql Vulnerability Disclosure
  slug: textql-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Textql Trust Center
  slug: textql-trust-center
  summary_line: SOC 2 Type II, HIPAA, GDPR, SOX
skill_count: 4
skills:
- name: textql-govern-an-ontology-change
  slug: textql-govern-an-ontology-change
- name: textql-run-an-analysis
  slug: textql-run-an-analysis
- name: textql-schedule-a-playbook
  slug: textql-schedule-a-playbook
- name: Textql
  slug: textql-textql-skill
slug: textql
tags:
- Company
- Artificial Intelligence
- Analytics
- Business Intelligence
- Data
- Agents
- MCP
- Semantic Layer
- Text-to-SQL
- Data Warehouse
- Enterprise
- A2A
website: https://textql.com/
---
