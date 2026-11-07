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
  band: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: true
    idempotency: verified
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 65.4
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: First-party hosted MCP server exposing a Relevance AI project's agents, tools, workforces, knowledge tables, evals, analytics, folders and triggers to any MCP-compatible client (Claude, ChatGPT, Curso
  name: Relevance AI MCP Server
  slug: relevance-ai-mcp
- baseURL: https://api-{region}.stack.tryrelevance.com/latest
  baseurl_source: declared
  description: The Agent Debug Configs API from Relevance AI — 4 operation(s) for agent debug configs.
  name: Relevance AI Agent Debug Configs API
  phrasing_intents:
  - id: GetAgentDebugConfigs
    intent: Get one agent debug config document
    question: Can I fetch a single saved agent debug configuration by its document id?
  - id: DeleteAgentDebugConfigs
    intent: Delete an agent debug config document
    question: How do I remove an agent debug configuration I no longer need?
  - id: ListAgentDebugConfigs
    intent: List agent debug configs in a collection
    question: What agent debug configurations are stored in a collection?
  - id: UpsertAgentDebugConfigs
    intent: Create or update an agent debug config
    question: Can I create an agent debug config if it doesn't exist yet?
  phrasing_ops: 4
  slug: relevance-ai-agent-debug-configs-api
- baseURL: https://api-{region}.stack.tryrelevance.com/latest
  baseurl_source: declared
  description: The Agent Runtime Events API from Relevance AI — 4 operation(s) for agent runtime events.
  name: Relevance AI Agent Runtime Events API
  phrasing_intents:
  - id: GetAgentRuntimeEvent
    intent: Get one agent runtime event
    question: Can I look up a single agent runtime event by its document id?
  - id: DeleteAgentRuntimeEvent
    intent: Delete an agent runtime event
    question: How do I delete a recorded agent runtime event?
  - id: ListAgentRuntimeEvent
    intent: List agent runtime events in a collection
    question: What runtime events have my agents recorded in a collection?
  - id: UpsertAgentRuntimeEvent
    intent: Create or update an agent runtime event
    question: Can I write an agent runtime event record that is created if missing?
  phrasing_ops: 4
  slug: relevance-ai-agent-runtime-events-api
- baseURL: https://api-{region}.stack.tryrelevance.com/latest
  baseurl_source: declared
  description: The Agents API from Relevance AI — 7 operation(s) for agents.
  name: Relevance AI Agents API
  phrasing_intents:
  - id: DeleteAgentConversations
    intent: Delete several conversations for an agent
    question: Can I bulk-delete a batch of conversations from one agent?
  - id: DeleteAgentConversation
    intent: Delete a single agent conversation
    question: How do I delete one specific conversation with an agent?
  - id: UpsertUserAgentTag
    intent: Apply a tag to an agent
    question: Can I label an agent with one of my project tags?
  - id: DeleteUserAgentTag
    intent: Remove a tag from an agent
    question: How do I take a tag off an agent without deleting the tag itself?
  - id: ListUserTags
    intent: List tags in the current project
    question: What tags exist in my project for organizing agents?
  - id: UpsertUserTag
    intent: Create or update a project tag
    question: Can I create a new coloured tag for grouping agents?
  - id: DeleteUserTag
    intent: Delete a tag from the project
    question: How do I delete a tag from my project entirely?
  phrasing_ops: 7
  slug: relevance-ai-agents-api
- baseURL: https://api-{region}.stack.tryrelevance.com/latest
  baseurl_source: declared
  description: The alarms API from Relevance AI — 3 operation(s) for alarms.
  name: Relevance AI Alarms API
  phrasing_intents:
  - id: CreateAlarm
    intent: Create an alarm for an agent or workforce
    question: How do I get alerted when my agent starts failing?
  - id: ListAlarms
    intent: List alarms for an agent or workforce
    question: What alarms are configured on my workforce?
  - id: GetAlarm
    intent: Get an alarm's settings
    question: What condition and channels does a particular alarm use?
  - id: UpdateAlarm
    intent: Update an alarm
    question: Can I change the threshold or notification channels of an existing alarm?
  - id: DeleteAlarm
    intent: Delete an alarm
    question: How do I delete an alarm I no longer want?
  phrasing_ops: 5
  slug: relevance-ai-alarms-api
- baseURL: https://api-{region}.stack.tryrelevance.com/latest
  baseurl_source: declared
  description: The analytics API from Relevance AI — 23 operation(s) for analytics.
  name: Relevance AI Analytics API
  phrasing_intents:
  - id: GetMetrics
    intent: Get a metric as a time series with summary stats
    question: How do I chart a single metric over time with summary statistics?
  - id: GetAgentBreakdown
    intent: Break down agents by tasks, errors and top actions
    question: Which agents had the highest error rates last week?
  - id: GetActionBreakdown
    intent: Break down actions by executions and credits
    question: Which actions ran the most and burned the most credits?
  - id: GetWorkforceBreakdown
    intent: Break down workforces by tasks, errors and credits
    question: Which workforces are failing the most tasks?
  - id: GetAgentModelBreakdown
    intent: Break down agent usage by LLM model
    question: Which LLM models are my agents using, and how many tokens?
  - id: GetAgentErrors
    intent: List error messages from agents and tool runs
    question: What error messages did my agents hit yesterday?
  - id: GetErrorTimeSeries
    intent: Get detailed error records with execution context
    question: Where can I find full execution context for each error, not just the message?
  - id: GetTaskTimeline
    intent: Chart daily approval, escalated or errored tasks
    question: How many tasks were waiting for approval each day this month?
  phrasing_ops: 23
  slug: relevance-ai-analytics-api
- baseURL: https://api-{region}.stack.tryrelevance.com/latest
  baseurl_source: declared
  description: The apify API from Relevance AI — 2 operation(s) for apify.
  name: Relevance AI Apify API
  phrasing_intents:
  - id: GetApifyActors
    intent: Browse available Apify actors
    question: Which Apify actors can I use from Relevance AI?
  - id: GetApifyActorSchema
    intent: Get the input schema of an Apify actor
    question: What inputs does a specific Apify actor expect?
  phrasing_ops: 2
  slug: relevance-ai-apify-api
- baseURL: https://api-{region}.stack.tryrelevance.com/latest
  baseurl_source: declared
  description: The auth API from Relevance AI — 52 operation(s) for auth.
  name: Relevance AI Auth API
  phrasing_intents:
  - id: CreateUser
    intent: Sign up a new user with an organization and project
    question: How do I create a new user account along with its first organization and project?
  - id: ListUsers
    intent: List users in the project
    question: Who are the users in my project?
  - id: ListAssetUserPermissions
    intent: List who has access to an asset
    question: Which users have access to a particular agent or tool, and with what role?
  - id: GetAssetUserCapability
    intent: Get my capabilities on an asset
    question: What am I allowed to do on a specific asset?
  - id: IsUserAuthorized
    intent: Check whether the caller holds given permissions
    question: Does my current key have a given set of permissions?
  - id: GetAuthHeaderInfo
    intent: Identify the user and key behind my credentials
    question: Which user and key id does my auth header belong to?
  - id: CreateProjectInvite
    intent: Invite someone to a project
    question: How do I invite a teammate to my project by email?
  - id: ListProjectInvites
    intent: List outstanding project invites
    question: Which project invites are still outstanding?
  phrasing_ops: 52
  slug: relevance-ai-auth-api
- baseURL: https://api-{region}.stack.tryrelevance.com/latest
  baseurl_source: declared
  description: The billing API from Relevance AI — 19 operation(s) for billing.
  name: Relevance AI Billing API
  phrasing_intents:
  - id: GetBillingTotals
    intent: Get an organization's total cost for a period
    question: How much has my organization spent over a given date range?
  - id: GetBillingFrontendLink
    intent: Get a link to the billing portal
    question: Where can I open the billing portal to manage my organization's payment details?
  - id: GetBillingCheckoutSession
    intent: Start a subscription checkout session
    question: How do I get a checkout page to pay for a subscription plan?
  - id: UpdateOrganizationBilling
    intent: Set an organization's plan and billing cycle
    question: Can I move my organization onto a different plan with annual billing?
  - id: SyncSubscription
    intent: Resync an organization's subscription state
    question: My plan looks out of date - can I resync the subscription from the payment processor?
  - id: DowngradeSubscription
    intent: Downgrade an organization's subscription
    question: How do I downgrade to a cheaper plan?
  - id: ChangeBillingSubscription
    intent: Change subscription plan, optionally with a coupon
    question: Can I switch my subscription to a new plan and apply a coupon code?
  - id: CancelDowngrade
    intent: Cancel a scheduled plan downgrade
    question: I scheduled a downgrade - can I undo it and stay on my current plan?
  phrasing_ops: 22
  slug: relevance-ai-billing-api
- baseURL: https://api-{region}.stack.tryrelevance.com/latest
  baseurl_source: declared
  description: The Branding Kit API from Relevance AI — 1 operation(s) for branding kit.
  name: Relevance AI Branding Kit API
  phrasing_intents:
  - id: GetBrandingKit
    intent: Get a single branding kit
    question: What logos, colors and fonts are in a particular branding kit?
  phrasing_ops: 1
  slug: relevance-ai-branding-kit-api
- baseURL: https://api-{region}.stack.tryrelevance.com/latest
  baseurl_source: declared
  description: The Branding Kits API from Relevance AI — 3 operation(s) for branding kits.
  name: Relevance AI Branding Kits API
  phrasing_intents:
  - id: CreateBrandingKit
    intent: Create a branding kit
    question: How do I set up a new branding kit with logos, colors and fonts?
  - id: ListBrandingKits
    intent: List all branding kits
    question: What branding kits do I have saved?
  - id: UpdateBrandingKit
    intent: Update an existing branding kit
    question: Can I change the colors on a branding kit I already made?
  - id: DeleteBrandingKit
    intent: Delete a branding kit
    question: How do I delete a branding kit?
  - id: GenerateBrandKitFromImages
    intent: Generate a branding kit from images
    question: Can a branding kit be generated automatically from a few images?
  phrasing_ops: 5
  slug: relevance-ai-branding-kits-api
- baseURL: https://api-{region}.stack.tryrelevance.com/latest
  baseurl_source: declared
  description: The chat API from Relevance AI — 161 operation(s) for chat.
  name: Relevance AI Chat API
  phrasing_intents:
  - id: ListProjectPhoneNumbers
    intent: List phone numbers assigned to the project
    question: Which phone numbers are assigned to my Relevance AI project?
  - id: CloneAgent
    intent: Deep clone an agent with its tools and subagents
    question: How do I make a full copy of an agent including all its tools and subagents?
  - id: CloneAgentMarketplaceTemplate
    intent: Clone a marketplace agent template
    question: Can I copy an agent from a marketplace template into my own project?
  - id: UpsertAgent
    intent: Create or update an agent's configuration
    question: How do I create a new agent or update an existing one without overwriting it?
  - id: UpsertPresetAgent
    intent: Set up a preset agent such as a meeting notetaker
    question: How do I add a ready-made preset agent like the meeting notetaker to my project?
  - id: ListAgents
    intent: Search and filter agents in the project
    question: Can I search all agents in my project by keyword and filters?
  - id: ListMyAgents
    intent: List agents I created
    question: Which agents have I personally created?
  - id: GetAgent
    intent: Get an agent's details
    question: How do I fetch the full configuration of one agent?
  phrasing_ops: 171
  slug: relevance-ai-chat-api
- baseURL: https://api-{region}.stack.tryrelevance.com/latest
  baseurl_source: declared
  description: The evals API from Relevance AI — 22 operation(s) for evals.
  name: Relevance AI Evals API
  phrasing_intents:
  - id: CreateTestCase
    intent: Create a test case with a scenario and checks
    question: How do I write a new eval test case describing a scenario for my agent?
  - id: ListTestCases
    intent: List test cases for an agent or workforce
    question: What test cases have I written for my agent?
  - id: ListEvalBatchByResourceNew
    intent: List eval batches for an agent or workforce
    question: Which evaluation batches have been run against my agent?
  - id: CreateEvalRuleForResource
    intent: Create an evaluator rule
    question: How do I add a new evaluator rule that grades my agent's conversations?
  - id: ListEvalRulesForResource
    intent: List evaluator rules for an agent or workforce
    question: What evaluator rules are defined for my workforce?
  - id: ListEvalRunsForResource
    intent: List eval runs for an agent or workforce
    question: What individual eval runs have been done on my agent recently?
  - id: EvaluateResource
    intent: Run an evaluation on an agent or workforce
    question: How do I evaluate a set of my agent's past conversations?
  - id: GetEvalBatchSummaryForResource
    intent: Get the summary of an eval batch
    question: How did my agent score in a particular eval batch?
  phrasing_ops: 37
  slug: relevance-ai-evals-api
- baseURL: https://api-{region}.stack.tryrelevance.com/latest
  baseurl_source: declared
  description: The fal_ai API from Relevance AI — 3 operation(s) for fal_ai.
  name: Relevance AI Fal AI API
  phrasing_intents:
  - id: GetFalAiCategories
    intent: List fal.ai model categories
    question: What categories of fal.ai models are available?
  - id: GetFalAiModels
    intent: Browse available fal.ai models
    question: Which fal.ai models can my Relevance AI agents call?
  - id: GetFalAiModelSchema
    intent: Get the input schema of a fal.ai model
    question: What parameters does a particular fal.ai model accept?
  phrasing_ops: 3
  slug: relevance-ai-fal-ai-api
- baseURL: https://api-{region}.stack.tryrelevance.com/latest
  baseurl_source: declared
  description: The Folders API from Relevance AI — 1 operation(s) for folders.
  name: Relevance AI Folders API
  phrasing_intents:
  - id: ListFolders
    intent: List my folders
    question: What folders have I created to organize my work?
  phrasing_ops: 1
  slug: relevance-ai-folders-api
- baseURL: https://api-{region}.stack.tryrelevance.com/latest
  baseurl_source: declared
  description: The Integrations API from Relevance AI — 2 operation(s) for integrations.
  name: Relevance AI Integrations API
  phrasing_intents:
  - id: SlackEmailLookup
    intent: Look up and validate a Slack user's email
    question: Can I check whether an email belongs to a user in my connected Slack workspace?
  - id: SlackAgentsWebhook
    intent: List agents triggerable from a Slack channel
    question: Which agents can be triggered from a given Slack channel via slash command?
  phrasing_ops: 2
  slug: relevance-ai-integrations-api
- baseURL: https://api-{region}.stack.tryrelevance.com/latest
  baseurl_source: declared
  description: The inventor API from Relevance AI — 3 operation(s) for inventor.
  name: Relevance AI Inventor API
  phrasing_intents:
  - id: GetInventorBootstrap
    intent: Get the Inventor startup payload
    question: Which Inventor tools exist and how is each one classified?
  - id: GetInventorUserSettings
    intent: Get my Inventor settings
    question: What are my current Inventor settings?
  - id: UpdateInventorUserSettings
    intent: Update my Inventor settings
    question: How do I change my Inventor preferences?
  - id: GetInventorTaskUsage
    intent: Get credit usage for an Inventor task
    question: How many credits did an Inventor task use?
  phrasing_ops: 4
  slug: relevance-ai-inventor-api
- baseURL: https://api-{region}.stack.tryrelevance.com/latest
  baseurl_source: declared
  description: The knowledge API from Relevance AI — 20 operation(s) for knowledge.
  name: Relevance AI Knowledge API
  phrasing_intents:
  - id: AddKnowledge
    intent: Add documents to a knowledge set
    question: How do I add new data to a Relevance AI knowledge base?
  - id: ChunkAndVectorizeKnowledge
    intent: Chunk and vectorize uploaded knowledge
    question: I uploaded knowledge with vectorizing turned off, how do I embed it now?
  - id: BulkUpdateKnowledge
    intent: Bulk update rows in a knowledge set
    question: How do I edit many existing knowledge rows at once?
  - id: ListKnowledge
    intent: List documents in a knowledge set
    question: What documents are stored in a knowledge set?
  - id: ListKnowledgeChunks
    intent: Search chunks in a knowledge set
    question: How do I run a vector search over the chunks of a knowledge set?
  - id: DeleteKnowledge
    intent: Delete documents from a knowledge set
    question: How do I delete specific documents from a knowledge set without removing the set?
  - id: DeleteKnowledgeSet
    intent: Delete an entire knowledge set
    question: How do I delete a whole knowledge set?
  - id: AggregateKnowledge
    intent: Aggregate rows within a knowledge set
    question: Can I group and count the rows inside a knowledge set?
  phrasing_ops: 20
  slug: relevance-ai-knowledge-api
- baseURL: https://api-{region}.stack.tryrelevance.com/latest
  baseurl_source: declared
  description: The marketplace API from Relevance AI — 28 operation(s) for marketplace.
  name: Relevance AI Marketplace API
  phrasing_intents:
  - id: DeleteMarketplaceListing
    intent: Delete a marketplace listing
    question: How do I take down a listing I put on the Relevance AI marketplace?
  - id: UpdateMarketplaceListing
    intent: Edit a marketplace listing
    question: How do I change the price or description of my marketplace listing?
  - id: ApproveMarketplaceListing
    intent: Approve a marketplace listing
    question: How does a reviewer approve a listing waiting for marketplace review?
  - id: RejectMarketplaceListing
    intent: Reject a marketplace listing
    question: How do I reject a submitted marketplace listing and say why?
  - id: CloneMarketplaceListing
    intent: Clone a marketplace listing into my project
    question: How do I copy an agent or tool from the marketplace into my own project?
  - id: SubmitMarketplaceListing
    intent: Submit a new listing to the marketplace
    question: How do I publish my agent or tool as a new marketplace listing?
  - id: CreateMarketplaceListingVersion
    intent: Publish a new version of a listing
    question: How do I push an updated version of my agent to an existing marketplace listing?
  - id: ListOwnMarketplaceListings
    intent: List my own marketplace listings
    question: Which marketplace listings has my project submitted?
  phrasing_ops: 32
  slug: relevance-ai-marketplace-api
- baseURL: https://api-{region}.stack.tryrelevance.com/latest
  baseurl_source: declared
  description: The Mas API from Relevance AI — 4 operation(s) for mas.
  name: Relevance AI Mas API
  phrasing_intents:
  - id: GetMAS
    intent: Get a multi-agent system record
    question: How do I look up one multi-agent system by its id?
  - id: DeleteMAS
    intent: Delete a multi-agent system
    question: How do I remove a multi-agent system I no longer need?
  - id: ListMAS
    intent: List multi-agent systems
    question: What multi-agent systems exist in my Relevance AI project?
  - id: UpsertMAS
    intent: Create or update a multi-agent system
    question: How do I save changes to a multi-agent system definition?
  phrasing_ops: 4
  slug: relevance-ai-mas-api
- baseURL: https://api-{region}.stack.tryrelevance.com/latest
  baseurl_source: declared
  description: The Mas Store API from Relevance AI — 4 operation(s) for mas store.
  name: Relevance AI Mas Store API
  phrasing_intents:
  - id: GetMASStore
    intent: Get one multi-agent system store item
    question: Can I read a single item from the multi-agent system store?
  - id: DeleteMASStore
    intent: Delete a multi-agent system store item
    question: How do I delete an item from the MAS store?
  - id: ListMASStore
    intent: List multi-agent system store items
    question: What items are saved in my multi-agent system store?
  - id: UpsertMASStore
    intent: Create or update a MAS store item
    question: Can I save data into the MAS store and have it created if it doesn't exist?
  phrasing_ops: 4
  slug: relevance-ai-mas-store-api
- baseURL: https://api-{region}.stack.tryrelevance.com/latest
  baseurl_source: declared
  description: The Mcp API from Relevance AI — 3 operation(s) for mcp.
  name: Relevance AI MCP API
  phrasing_intents:
  - id: AgentMCPAuthRequiredUserAccounts
    intent: Check which MCP servers need my login
    question: Which MCP servers used by an agent still need me to authenticate?
  - id: UpsertUserMCPAuth
    intent: Save my credentials for an MCP server
    question: How do I give an MCP server my API key or custom headers?
  - id: DeleteUserMCPAuth
    intent: Remove my credentials for an MCP server
    question: How do I disconnect my credentials from an MCP server?
  phrasing_ops: 3
  slug: relevance-ai-mcp-api
- baseURL: https://api-{region}.stack.tryrelevance.com/latest
  baseurl_source: declared
  description: The Organizations API from Relevance AI — 55 operation(s) for organizations.
  name: Relevance AI Organizations API
  phrasing_intents:
  - id: BulkUpsertOrganizationIntegrationPermissionOverrides
    intent: Bulk set integration permission overrides
    question: Can I allow or block several integrations for my organization in one call?
  - id: UpdateOrganizationDefaultIntegrationPermission
    intent: Change the default integration permission
    question: How do I block all integrations by default for my organization?
  - id: GetOrganizationDefaultIntegrationPermission
    intent: Get the default integration permission
    question: Are integrations allowed by default in my organization?
  - id: ListOrganizationIntegrationProviders
    intent: List integration providers for an organization
    question: Which API key and OAuth integration providers are available to my organization?
  - id: SetOrganizationNativeApiKey
    intent: Set an organization-wide native API key
    question: How do I set a fallback API key for every project in my organization?
  - id: DeleteOrganizationNativeApiKey
    intent: Delete an organization native API key
    question: How do I remove an org-level native API key?
  - id: ListOrganizationNativeApiKeys
    intent: List organization native API keys
    question: Which native API keys are set at the organization level?
  - id: CreateOrganization
    intent: Create an organization
    question: How do I create a new organization in Relevance AI?
  phrasing_ops: 62
  slug: relevance-ai-organizations-api
- baseURL: https://api-{region}.stack.tryrelevance.com/latest
  baseurl_source: declared
  description: The projects API from Relevance AI — 30 operation(s) for projects.
  name: Relevance AI Projects API
  phrasing_intents:
  - id: CreateProject
    intent: Create a project in an organization
    question: How do I create a new project inside my organization?
  - id: UpdateProject
    intent: Update the current project's details
    question: Can I rename my current project or change its description?
  - id: ListProjects
    intent: List my projects
    question: Which projects do I have access to?
  - id: GetProjectsOrgInfo
    intent: Get the organization a project belongs to
    question: Which organization does my current project belong to?
  - id: ListProjectKeys
    intent: List keys configured on a project
    question: Which third-party keys have been set on my project?
  - id: ListProjectNativeApiKeysAvailability
    intent: Check API key availability incl. org fallbacks
    question: Are API keys available to this project from the organization level if not set on the project?
  - id: ListProjectKeyTypes
    intent: List valid project key types
    question: What kinds of keys can I store on a project?
  - id: SetProjectKey
    intent: Set a key on a project
    question: How do I store a third-party API key on my project?
  phrasing_ops: 33
  slug: relevance-ai-projects-api
- baseURL: https://api-{region}.stack.tryrelevance.com/latest
  baseurl_source: declared
  description: The replicate API from Relevance AI — 3 operation(s) for replicate.
  name: Relevance AI Replicate API
  phrasing_intents:
  - id: GetReplicateCollections
    intent: List available Replicate model collections
    question: Which Replicate collections can I pick models from?
  - id: GetReplicateCollectionModels
    intent: List models in a Replicate collection
    question: What models are inside a particular Replicate collection?
  - id: GetReplicateModelSchema
    intent: Get a Replicate model's input and output schema
    question: What inputs does a Replicate model expect and what does it return?
  phrasing_ops: 3
  slug: relevance-ai-replicate-api
- baseURL: https://api-{region}.stack.tryrelevance.com/latest
  baseurl_source: declared
  description: The services API from Relevance AI — 10 operation(s) for services.
  name: Relevance AI Services API
  phrasing_intents:
  - id: SlackInteractionsWebhook
    intent: Receive Slack approval interactions
    question: How are agent approvals clicked in Slack sent back to the platform?
  - id: GetDeliveryExternalId
    intent: Get the AWS delivery external ID for an org
    question: What external ID do I put in my AWS IAM trust policy for cross-account delivery?
  - id: ListGoogleCalendarEvents
    intent: List Google Calendar events in a time range
    question: What's on my connected Google Calendar this week?
  - id: GetConfigFlags
    intent: Get all config flags for the app
    question: Which feature flags are enabled for my signed-in app?
  - id: GetPublicConfigFlags
    intent: Get public config flags without signing in
    question: Which config flags can be read before a user logs in?
  - id: ShortUrlRedirect
    intent: Resolve a short URL
    question: Where does a Relevance AI short link point to?
  - id: GetFileUploadUrlsForDataset
    intent: Get upload URLs for files in a dataset
    question: How do I upload files into a dataset?
  - id: GetTemporaryPublicFileUploadUrl
    intent: Get a public one-hour file upload URL
    question: Can someone without an account upload a file temporarily?
  phrasing_ops: 10
  slug: relevance-ai-services-api
- baseURL: https://api-{region}.stack.tryrelevance.com/latest
  baseurl_source: declared
  description: The studios API from Relevance AI — 45 operation(s) for studios.
  name: Relevance AI Studios API
  phrasing_intents:
  - id: UpsertOAuthAccountToolLink
    intent: Link a connected OAuth account to a tool
    question: How do I attach one of my connected OAuth accounts to a specific tool?
  - id: DeleteOAuthAccountToolLink
    intent: Unlink an OAuth account from a tool
    question: Can I detach a connected OAuth account from a tool so it stops using those credentials?
  - id: PopulateApiSelector
    intent: Populate options for an API selector field
    question: Which options are available to fill an API selector input in a tool?
  - id: ListStudios
    intent: List the tools in my project
    question: What tools have I built in my Relevance AI project?
  - id: ListStudiosView
    intent: Browse tools in a sortable list view
    question: Can I get my tools as a paged, sorted view like the tools page shows?
  - id: ListStudiosFoldersAwareView
    intent: Browse tools in a folder-aware list view
    question: Can I list my tools grouped by the folders they're organized into?
  - id: ListStudiosRunHistory
    intent: List the run history of my tools
    question: Where can I see past runs of my tools?
  - id: ListBulkInProgressStudios
    intent: List tools with bulk runs in progress
    question: Which of my tools currently have bulk runs still in progress?
  phrasing_ops: 46
  slug: relevance-ai-studios-api
- baseURL: https://api-{region}.stack.tryrelevance.com/latest
  baseurl_source: declared
  description: The Sync API from Relevance AI — 8 operation(s) for sync.
  name: Relevance AI Sync API
  phrasing_intents:
  - id: DeleteSyncTemplate
    intent: Delete a sync template
    question: How do I delete a sync template I set up?
  - id: ListSyncConfigs
    intent: List sync configs
    question: What sync configs are set up in my account?
  - id: ListSyncTemplates
    intent: List a project's sync templates
    question: Which sync templates does this project have?
  - id: InviteUsersToAgentTrigger
    intent: Invite users to connect accounts to an agent trigger
    question: How do I ask teammates to connect their own accounts to an agent trigger?
  - id: GetSyncTemplateInviteStatus
    intent: Check invite status for a sync template
    question: Have the people I invited to a sync template connected their accounts yet?
  - id: GetPendingInvites
    intent: Get my pending sync invites
    question: Do I have any pending invites to connect my accounts to an agent trigger?
  - id: CancelSyncInvite
    intent: Cancel a pending sync invite
    question: Can I withdraw a sync invite I sent before it's accepted?
  - id: RejectSyncInvite
    intent: Reject a sync invite I received
    question: How do I decline an invite to connect my account to someone's agent trigger?
  phrasing_ops: 8
  slug: relevance-ai-sync-api
- baseURL: https://api-{region}.stack.tryrelevance.com/latest
  baseurl_source: declared
  description: The Sync Items API from Relevance AI — 8 operation(s) for sync items.
  name: Relevance AI Sync Items API
  phrasing_intents:
  - id: GetSyncItems
    intent: Get an item in a sync collection
    question: How do I look up one synced item in a collection?
  - id: DeleteSyncItems
    intent: Delete an item from a sync collection
    question: How do I remove a single synced item from a collection?
  - id: ListSyncItems
    intent: List items in a sync collection
    question: What items are in a given sync collection?
  - id: UpsertSyncItems
    intent: Create or update a sync item's data
    question: How do I write data into a sync item?
  - id: TriggerSyncItem
    intent: Run a sync for one item only
    question: Can I re-run a sync for just one item rather than the whole collection?
  - id: UpdateSyncItemStatus
    intent: Set a sync item's status
    question: How do I mark a sync item as failed with an error message?
  - id: UpdateSelectedSyncItemFields
    intent: Update selected fields of a sync item
    question: How do I change just a few fields on a sync item without a full upsert?
  - id: BulkPostponeUpcomingSyncItems
    intent: Postpone upcoming sync items in bulk
    question: Can I push back every upcoming sync item in a collection at once?
  phrasing_ops: 8
  slug: relevance-ai-sync-items-api
- baseURL: https://api-{region}.stack.tryrelevance.com/latest
  baseurl_source: declared
  description: The Syncs API from Relevance AI — 5 operation(s) for syncs.
  name: Relevance AI Syncs API
  phrasing_intents:
  - id: GetSyncs
    intent: Get a sync configuration
    question: How do I look up one sync by its id?
  - id: DeleteSyncs
    intent: Delete a sync
    question: How do I delete a sync I set up?
  - id: ListSyncs
    intent: List syncs
    question: What syncs are configured in my Relevance AI project?
  - id: UpsertSyncs
    intent: Create or update a sync
    question: How do I change the settings of an existing sync?
  - id: TriggerSync
    intent: Run a sync now
    question: How do I kick off a whole sync manually instead of waiting for its schedule?
  phrasing_ops: 5
  slug: relevance-ai-syncs-api
- baseURL: https://api-{region}.stack.tryrelevance.com/latest
  baseurl_source: declared
  description: The user-memory API from Relevance AI — 3 operation(s) for user-memory.
  name: Relevance AI User Memory API
  phrasing_intents:
  - id: UpsertUserMemory
    intent: Save or update a memory about me for an agent
    question: How do I make an agent remember something about me?
  - id: DeleteUserMemory
    intent: Delete a user memory
    question: How do I make an agent forget something it remembered about me?
  - id: ListUserMemories
    intent: List what an agent remembers about me
    question: What does an agent remember about me?
  phrasing_ops: 3
  slug: relevance-ai-user-memory-api
- baseURL: https://api-{region}.stack.tryrelevance.com/latest
  baseurl_source: declared
  description: The Warmup API from Relevance AI — 4 operation(s) for warmup.
  name: Relevance AI Warmup API
  phrasing_intents:
  - id: CreateEmailWarmupInbox
    intent: Add an email inbox for warmup
    question: How do I set up a new email address for warmup?
  - id: GetEmailWarmupStats
    intent: Get warmup stats for an email
    question: How is the warmup going for one of my email addresses?
  - id: StartEmailWarmup
    intent: Start warming up an email address
    question: Can I resume warmup on an address that was paused?
  - id: StopEmailWarmup
    intent: Stop warming up an email address
    question: How do I pause warmup for an email address?
  phrasing_ops: 4
  slug: relevance-ai-warmup-api
artifact_total: 53
asyncapis:
- description: ''
  name: Relevance Ai Events
  slug: relevance-ai-events
common:
- group: other
  href: https://artifacts.apis.io/relevance-ai/capabilities/relevance-ai-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/relevance-ai-capability-edges.yml
- group: company
  title: ''
  type: Website
  url: https://relevanceai.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://relevanceai.com/docs
- group: docs
  title: ''
  type: Documentation
  url: https://relevanceai.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://api-f1db6c.stack.tryrelevance.com/latest/documentation
- group: start
  title: ''
  type: GettingStarted
  url: https://relevanceai.com/docs/get-started/quick-start-guide
- group: operate
  title: ''
  type: Support
  url: https://relevanceai.com/docs/get-started/support
- group: company
  title: ''
  type: Blog
  url: https://relevanceai.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/RelevanceAI
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/relevanceai
- group: commercial
  title: ''
  type: Pricing
  url: https://relevanceai.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://relevanceai.com/signup
- group: start
  title: ''
  type: Login
  url: https://app.relevanceai.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://relevanceai.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://relevanceai.com/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.relevanceai.com/
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.relevanceai.com/
- group: auth
  href: https://artifacts.apis.io/relevance-ai/security/relevance-ai-trust-center.yml
  title: ''
  type: Compliance
  url: security/relevance-ai-trust-center.yml
- group: design
  href: https://artifacts.apis.io/relevance-ai/conformance/relevance-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/relevance-ai-conformance.yml
- group: operate
  href: https://artifacts.apis.io/relevance-ai/changelog/relevance-ai-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/relevance-ai-changelog.yml
- group: design
  href: https://artifacts.apis.io/relevance-ai/lifecycle/relevance-ai-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/relevance-ai-lifecycle.yml
- group: auth
  href: https://artifacts.apis.io/relevance-ai/authentication/relevance-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/relevance-ai-authentication.yml
- group: auth
  href: https://artifacts.apis.io/relevance-ai/scopes/relevance-ai-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/relevance-ai-scopes.yml
- group: design
  href: https://artifacts.apis.io/relevance-ai/conventions/relevance-ai-conventions.yml
  title: ''
  type: Conventions
  url: conventions/relevance-ai-conventions.yml
- group: design
  href: https://artifacts.apis.io/relevance-ai/conventions/relevance-ai-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/relevance-ai-conventions.yml
- group: design
  href: https://artifacts.apis.io/relevance-ai/errors/relevance-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/relevance-ai-problem-types.yml
- group: build
  href: https://artifacts.apis.io/relevance-ai/packages/relevance-ai-packages.yml
  title: ''
  type: Packages
  url: packages/relevance-ai-packages.yml
- group: build
  href: https://artifacts.apis.io/relevance-ai/packages/relevance-ai-packages.yml
  title: ''
  type: SDKs
  url: packages/relevance-ai-packages.yml
- group: design
  href: https://artifacts.apis.io/relevance-ai/components/relevance-ai-components.yml
  title: ''
  type: Components
  url: components/relevance-ai-components.yml
- group: agent
  href: https://artifacts.apis.io/relevance-ai/mcp/relevance-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/relevance-ai-mcp.yml
- group: build
  href: https://artifacts.apis.io/relevance-ai/mcp/relevance-ai-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/relevance-ai-tool-crosswalk.yml
- group: other
  href: https://artifacts.apis.io/relevance-ai/a2a/relevance-ai-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/relevance-ai-a2a.yml
- group: agent
  href: https://artifacts.apis.io/relevance-ai/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/relevance-ai/llms/relevance-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/relevance-ai-llms.txt
- group: agent
  href: https://artifacts.apis.io/relevance-ai/well-known/relevance-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/relevance-ai-well-known.yml
- group: design
  href: https://artifacts.apis.io/relevance-ai/asyncapi/relevance-ai-events.yml
  title: ''
  type: Webhooks
  url: asyncapi/relevance-ai-events.yml
- group: other
  href: https://artifacts.apis.io/relevance-ai/overlays/relevance-ai-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/relevance-ai-openapi-overlay.yaml
- group: design
  href: https://artifacts.apis.io/relevance-ai/data-model/relevance-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/relevance-ai-data-model.yml
- group: commercial
  href: https://artifacts.apis.io/relevance-ai/plans/relevance-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/relevance-ai-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/relevance-ai/rate-limits/relevance-ai-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/relevance-ai-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/relevance-ai/finops/relevance-ai-finops.yml
  title: ''
  type: FinOps
  url: finops/relevance-ai-finops.yml
- group: auth
  href: https://artifacts.apis.io/relevance-ai/security/relevance-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/relevance-ai-domain-security.yml
- group: operate
  title: ''
  type: Contact
  url: mailto:support@relevanceai.com
created: '2026-03-27'
description: 'Relevance AI is an agent platform for building, testing and running specialist AI agents and multi-agent "workforces" — teams of agents that coordinate on a shared goal. Domain experts build agents in a no-code visual builder, hold them to pass/fail quality bars with a built-in evals system, and connect them to 1,000+ integrations across sales, marketing, customer success, operations and HR. Developers reach the same platform three ways: a 566-operation REST API served from regional hosts in the US, EU and Australia; a first-party JavaScript/TypeScript SDK on npm and JSR; and a hosted, OAuth-protected MCP server at mcp.relevanceai.com that exposes agents, tools, workforces, knowledge tables, evals and analytics to any MCP client. Enterprise governance covers RBAC, human-in-the-loop approvals, SSO/SAML, PII masking, version control with rollback, multi-region data residency, and OpenTelemetry audit-log and trace streaming to the customer''s own S3 bucket. Operated by OnSearch
  Pty Ltd T/A Relevance AI; SOC 2 Type II and GDPR compliant.'
finops:
- has_sources: true
  method: derived
  name: Relevance Ai Finops
  primary_unit: subscription
  service_category: ''
  slug: relevance-ai-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/relevance-ai.png
layout: provider
mcp_servers:
- description: 'Relevance AI runs a first-party remote MCP server that exposes a project''s agents, tools, workforces, knowledge tables, evals, analytics and triggers to any MCP-compatible client. It is a hosted HTTP '
  name: Relevance AI MCP Server
  slug: relevance-ai-mcp-server
modified: '2026-08-29'
name: Relevance AI
nav: Providers
network: true
overview: 'Relevance AI publishes 32 API contracts indexed on the [APIs.io](https://apis.io/) network, including Agent Debug Configs API, Agent Runtime Events API, Agents API, and 29 more. Tagged areas include AI Agents, AI Automation, Multi-Agent Systems, Agent Platform, and MCP.


  The Relevance AI catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Relevance AI''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 36 more developer resources.'
plans:
- name: Relevance Ai Plans Pricing
  plan_count: 4
  slug: relevance-ai-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 10
  name: Relevance Ai Rate Limits
  slug: relevance-ai-rate-limits
rules:
- authorship: generated
  effective_rule_count: 96
  extends:
  - spectral:oas
  name: Relevance AI API Rules
  rule_count: 55
  severity_counts:
    error: 47
    hint: 0
    info: 2
    warn: 6
  slug: relevance-ai-rules
scopes:
- name: Relevance Ai Scopes
  scope_count: 0
  slug: relevance-ai-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: exemplar
  composite: 81.4
  coverage:
    artifact_dirs: 31
    catalog_earned: 68.5
    catalog_earned_first_party: 24.0
    catalog_gap: 46.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.2
  facets:
    access_clarity: 100.0
    contract_governance: 31.8
    contract_quality: 57.3
    developer_ergonomics: 71.4
    discoverability: 75.0
    operational_transparency: 65.8
  previous_composite: 80.2
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 96.8
      total: 31
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 39.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 100.0
screenshot: https://apis.io/screenshots/relevance-ai/relevance-ai-2026-06-20T192832.png
security:
- kind: authentication
  name: Relevance Ai Authentication
  slug: relevance-ai-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Relevance Ai Domain Security
  slug: relevance-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Relevance Ai Trust Center
  slug: relevance-ai-trust-center
  summary_line: SOC 2 Type II, GDPR
skill_count: 11
skills:
- name: managing-relevance-agents
  slug: relevance-ai-managing-relevance-agents
- name: managing-relevance-folders
  slug: relevance-ai-managing-relevance-folders
- name: managing-relevance-knowledge
  slug: relevance-ai-managing-relevance-knowledge
- name: managing-relevance-tools
  slug: relevance-ai-managing-relevance-tools
- name: managing-relevance-workforces
  slug: relevance-ai-managing-relevance-workforces
- name: relevance-ai
  slug: relevance-ai-relevance-ai
- name: relevance-analytics
  slug: relevance-ai-relevance-analytics
- name: relevance-diagnostics
  slug: relevance-ai-relevance-diagnostics
- name: relevance-evals
  slug: relevance-ai-relevance-evals
- name: relevance-slide-builder
  slug: relevance-ai-relevance-slide-builder
- name: relevance-task-ops
  slug: relevance-ai-relevance-task-ops
slug: relevance-ai
tags:
- AI Agents
- AI Automation
- Multi-Agent Systems
- Agent Platform
- MCP
- Agent-Native
- Workflow Automation
- LLM Orchestration
- Knowledge Management
- Observability
- Sales Automation
- GTM Engineering
- A2A
website: https://relevanceai.com
---
