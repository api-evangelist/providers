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
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: true
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: verified
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: documented
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 51.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 835
  human_in_the_loop: 835
  name: Live Direct Marketing Online Agentic Access
  operation_count: 1500
  slug: live-direct-marketing-online-agentic-access
  summary_line: 1500 operations · 835 acting · 835 human-in-the-loop
api_count: 2
apis:
- description: Remote Streamable-HTTP MCP server at https://api.live-direct-marketing.online/mcp (protocol 2025-06-18, server ldm-delivery 0.6.1). An anonymous session exposes three bootstrap tools — ldm_health, ldm
  name: LDM MCP Server
  slug: ldm-mcp-server
- description: 'A2A 0.3.0-shaped agent card served at https://api.live-direct-marketing.online/.well-known/agent.json (237 curated skills of 1,270, ?full=1 for all; capabilities streaming + pushNotifications) with a '
  name: LDM.delivery A2A Agent
  slug: ldm-a2a-agent
- description: Outbound HTTPS webhook subscriptions for lead, dialog and task events (lead.created, lead.moved, lead.won, lead.lost, dialog.received, dialog.replied, task.completed, task.failed), signed with X-LDM-S
  name: LDM Webhook Events
  slug: ldm-webhook-events
- description: 'Remote Streamable-HTTP MCP server at https://check.live-direct-marketing.online/mcp requiring Authorization: Bearer icp_live_* (anonymous tools/list answers 401 Problem Details). Tools mirror the agen'
  name: Inbox Check MCP Server
  slug: inbox-check-mcp-server
- description: Provider-shaped agent card at https://check.live-direct-marketing.online/.well-known/agent.json listing 21 REST-bound skills with HTTP method, URL and input_schema. The provider states that A2A suppor
  name: Inbox Check A2A Agent Card
  slug: inbox-check-a2a-agent
- baseURL: https://api.live-direct-marketing.online
  baseurl_source: declared
  description: The A2A API from Live Direct Marketing — 1 operation(s) for a2a.
  name: Live Direct Marketing A2A API
  phrasing_intents:
  - id: A2AController_dispatch
    intent: Send an A2A JSON-RPC request
    question: Can an agent talk to Live Direct Marketing over the A2A protocol?
  phrasing_ops: 1
  slug: live-direct-marketing-online-a2a-api
- baseURL: https://api.live-direct-marketing.online
  baseurl_source: declared
  description: The account API from Live Direct Marketing — 4 operation(s) for account.
  name: Live Direct Marketing Account API
  phrasing_intents:
  - id: V1MeController_me
    intent: Check my API key's tier and usage
    question: How much of my daily and monthly quota have I used with this key?
  - id: AccountController_list
    intent: List my API keys
    question: Which API keys exist on my account?
  - id: AccountController_create
    intent: Create an API key
    question: How do I generate a new API key for my account?
  - id: AccountController_dashboard
    intent: View the account dashboard
    question: What does my portal dashboard show about usage and recent tests?
  - id: AccountController_revoke
    intent: Revoke an API key
    question: How do I revoke an API key I no longer trust?
  phrasing_ops: 5
  slug: live-direct-marketing-online-account-api
- baseURL: https://api.live-direct-marketing.online
  baseurl_source: declared
  description: The Activities API from Live Direct Marketing — 3 operation(s) for activities.
  name: Live Direct Marketing Activities API
  phrasing_intents:
  - id: ActivitiesController_feed
    intent: Browse the unified CRM event feed
    question: What has happened across my CRM lately, emails and activities together?
  - id: ActivitiesController_findAll
    intent: List activities for a lead, contact or company
    question: Which calls, tasks and notes are logged against a lead?
  - id: ActivitiesController_create
    intent: Log a call, task or note
    question: How do I log a call I just had with a contact?
  - id: ActivitiesController_update
    intent: Update or complete an activity
    question: How do I mark a task as done?
  - id: ActivitiesController_remove
    intent: Delete an activity
    question: Can I delete a note or task I logged by mistake?
  phrasing_ops: 5
  slug: live-direct-marketing-online-activities-api
- baseURL: https://api.live-direct-marketing.online
  baseurl_source: declared
  description: The admin API from Live Direct Marketing — 123 operation(s) for admin.
  name: Live Direct Marketing Admin API
  phrasing_intents:
  - id: AnalysisRefreshController_refresh
    intent: Re-run analysis of an inbox placement test
    question: Can I recompute the analysis of a test without losing its placement and delivery timestamps?
  - id: FeedbackAdminController_list
    intent: List user feedback submissions
    question: Where can an admin read the feedback users have submitted?
  - id: FeedbackAdminController_stats
    intent: Get feedback statistics
    question: How much user feedback has come in overall?
  - id: BetaSignupsAdminController_list
    intent: List beta program signups
    question: Who has signed up for the beta?
  - id: BetaSignupsAdminController_stats
    intent: Get beta signup statistics
    question: How many people have joined the beta so far?
  - id: ScreenshotOrdersAdminController_stats
    intent: Get screenshot order statistics
    question: How many screenshot orders were placed recently?
  - id: RecheckAdminController_list
    intent: List recheck jobs
    question: Which recheck jobs are queued or have failed?
  - id: RecheckAdminController_stats
    intent: Get recheck job statistics
    question: How are recheck jobs performing in aggregate?
  phrasing_ops: 139
  slug: live-direct-marketing-online-admin-api
- baseURL: https://api.live-direct-marketing.online
  baseurl_source: declared
  description: The Admin / Honeypot API from Live Direct Marketing — 5 operation(s) for admin / honeypot.
  name: Live Direct Marketing Admin / Honeypot API
  phrasing_intents:
  - id: HoneypotController_fakeAdminLoginGet
    intent: Serve the decoy admin login page
    question: What does a scanner see when it hits the fake admin login page?
  - id: HoneypotController_fakeAdminLoginPost
    intent: Capture a login attempt on the decoy admin page
    question: What happens when an attacker submits credentials to the fake admin login?
  - id: HoneypotController_fakeEnv
    intent: Serve the decoy .env file
    question: Is there a fake .env file that catches secrets scanners?
  - id: HoneypotController_fakeWpAdmin
    intent: Serve the decoy WordPress admin page
    question: Does the site log bots that go looking for a WordPress admin panel?
  - id: HoneypotController_fakePhpMyAdmin
    intent: Serve the decoy phpMyAdmin page
    question: Is there a trap for database scanners looking for phpMyAdmin?
  - id: HoneypotController_fakeActuator
    intent: Serve the decoy Spring Boot actuator
    question: Does the honeypot catch probes for a Spring Boot actuator endpoint?
  phrasing_ops: 6
  slug: live-direct-marketing-online-admin-honeypot-api
- baseURL: https://api.live-direct-marketing.online
  baseurl_source: declared
  description: The Admin RPA API from Live Direct Marketing — 11 operation(s) for admin rpa.
  name: Live Direct Marketing Admin RPA API
  phrasing_intents:
  - id: RpaAdminController_overview
    intent: Get the RPA admin overview
    question: Which RPA service keys and tenant opt-ins are configured right now?
  - id: RpaAdminController_create
    intent: Create an RPA service key
    question: How do I issue a dedicated key for an RPA worker?
  - id: RpaAdminController_rotate
    intent: Rotate an RPA service key
    question: Can I rotate an RPA key's secret if it may have leaked?
  - id: RpaAdminController_reveal
    intent: Reveal an RPA service key secret
    question: Can a super admin see the current secret of an RPA key again?
  - id: RpaAdminController_globalAccess
    intent: Allow an RPA key to work for all tenants
    question: Can one RPA key claim work on behalf of every active tenant user?
  - id: RpaAdminController_revoke
    intent: Revoke an RPA service key
    question: How do I cut off an RPA worker's access immediately?
  - id: RpaAdminController_trace
    intent: Toggle detailed tracing for an RPA key
    question: Can I turn on detailed heartbeat and poll tracing for an RPA key while debugging?
  - id: RpaAdminController_grant
    intent: Grant an RPA key to a tenant user
    question: How do I opt a specific tenant and user into an RPA service key?
  phrasing_ops: 11
  slug: live-direct-marketing-online-admin-rpa-api
- baseURL: https://api.live-direct-marketing.online
  baseurl_source: declared
  description: The Agency API from Live Direct Marketing — 3 operation(s) for agency.
  name: Live Direct Marketing Agency API
  phrasing_intents:
  - id: AgencyController_list
    intent: List agency sub-accounts
    question: Which client sub-accounts sit under my agency account?
  - id: AgencyController_create
    intent: Create a client sub-account
    question: How do I spin up a new sub-account for an agency client?
  - id: AgencyController_stats
    intent: Get stats per agency sub-account
    question: How is each of my agency's client accounts performing?
  - id: AgencyController_detach
    intent: Detach a sub-account from the agency
    question: How do I remove a client sub-account from my agency?
  phrasing_ops: 4
  slug: live-direct-marketing-online-agency-api
- baseURL: https://api.live-direct-marketing.online
  baseurl_source: declared
  description: The Agent Card API from Live Direct Marketing — 8 operation(s) for agent card.
  name: Live Direct Marketing Agent Card API
  phrasing_intents:
  - id: AgentGuideController_guide
    intent: Get the agent capability guide
    question: What can an MCP or A2A agent do on this platform and in what order?
  - id: AgentGuideController_context
    intent: Get the tenant's recent lists, briefs and tasks
    question: Which lists, briefs and tasks has my workspace worked on recently?
  - id: AgentGuideController_resume
    intent: Get a resume snapshot with the next step
    question: Where did my agent leave off and what should it do next?
  - id: AgentGuideController_campaignSenderCapability
    intent: Run the sender-assignment preflight for campaigns
    question: What do I need before an agent changes a campaign's sender config or send window?
  - id: AgentCardController_health
    intent: Check public v1 API health
    question: Is the public v1 API up?
  - id: AgentCardController_card
    intent: Get the proprietary agent card
    question: Where is the LDM agent card that lists the platform's capabilities?
  - id: AgentCardController_cardA2A
    intent: Get the A2A-compliant agent card
    question: Does this platform publish an A2A 0.2.5 agent card?
  - id: AgentCardController_oauthProtectedResource
    intent: Get OAuth protected resource metadata
    question: Does the API publish RFC 9728 protected resource metadata?
  phrasing_ops: 8
  slug: live-direct-marketing-online-agent-card-api
- baseURL: https://api.live-direct-marketing.online
  baseurl_source: declared
  description: The AI API from Live Direct Marketing — 8 operation(s) for ai.
  name: Live Direct Marketing AI API
  phrasing_intents:
  - id: AiController_generate
    intent: Generate an AI text completion
    question: Can I run a text completion through my configured AI provider?
  - id: AiController_getBalance
    intent: Check the balance of an AI provider
    question: How much credit is left on one of my AI providers?
  - id: AiController_getAllBalances
    intent: Check balances across all AI providers
    question: What are the balances on all my configured AI providers at once?
  - id: AiController_getUsage
    intent: Get AI usage statistics
    question: How much AI have I used over the last month?
  - id: AiController_getLogs
    intent: Read recent AI usage logs
    question: Where can I see the individual AI calls that were made recently?
  - id: AiController_getProviders
    intent: List AI providers and their status
    question: Which AI providers are available and are they working?
  - id: AiController_getModels
    intent: List AI models per provider
    question: Which AI models can I choose from for each provider?
  - id: AiController_checkBalance
    intent: Check AI balance against an alert threshold
    question: Is there a monitoring hook that checks whether my AI balance fell below a threshold?
  phrasing_ops: 8
  slug: live-direct-marketing-online-ai-api
- baseURL: https://api.live-direct-marketing.online
  baseurl_source: declared
  description: The Allowlist API from Live Direct Marketing — 4 operation(s) for allowlist.
  name: Live Direct Marketing Allowlist API
  phrasing_intents:
  - id: AllowlistController_list
    intent: List allowlist entries
    question: Which emails and domains are on my allowlist?
  - id: AllowlistController_create
    intent: Allowlist an email or domain
    question: How do I add a trusted email address or domain to the allowlist?
  - id: AllowlistController_check
    intent: Check if an email or domain is allowlisted
    question: Is this email address already on the allowlist?
  - id: AllowlistController_bulkCreate
    intent: Bulk-add allowlist entries
    question: Can I add many emails or domains to the allowlist at once?
  - id: AllowlistController_delete
    intent: Delete an allowlist entry
    question: Can I remove an email or domain from the allowlist?
  phrasing_ops: 5
  slug: live-direct-marketing-online-allowlist-api
- baseURL: https://api.live-direct-marketing.online
  baseurl_source: declared
  description: The amo-widget API from Live Direct Marketing — 7 operation(s) for amo-widget.
  name: Live Direct Marketing Amo Widget API
  phrasing_intents:
  - id: AmoWidgetController_listProviders
    intent: List providers available to the amoCRM widget
    question: Which providers can the amoCRM widget run a test against?
  - id: AmoWidgetController_log
    intent: Send a log entry from the amoCRM widget
    question: How does the amoCRM widget report its client-side logs?
  - id: AmoWidgetController_oauthInstall
    intent: Complete the amoCRM widget OAuth install
    question: How is the amoCRM widget installed through OAuth?
  - id: AmoWidgetController_uninstall
    intent: Handle the amoCRM widget uninstall webhook
    question: What happens when someone uninstalls the amoCRM widget?
  - id: AmoWidgetController_createTest
    intent: Start a test from an amoCRM record
    question: How do I start a test for an email address from inside an amoCRM lead or contact?
  - id: AmoWidgetController_pollTest
    intent: Check progress of an amoCRM widget test
    question: Has my amoCRM widget test finished yet?
  - id: AmoWidgetController_saveNote
    intent: Save widget test results as an amoCRM note
    question: Can I attach a widget test result to the amoCRM record as a note?
  phrasing_ops: 7
  slug: live-direct-marketing-online-amo-widget-api
- baseURL: https://api.live-direct-marketing.online
  baseurl_source: declared
  description: The API Keys (tenant-scoped) API from Live Direct Marketing — 6 operation(s) for api keys (tenant-scoped).
  name: Live Direct Marketing API Keys (tenant-scoped) API
  phrasing_intents:
  - id: ApiKeysController_list
    intent: List tenant API keys
    question: What API keys exist for my workspace?
  - id: ApiKeysController_create
    intent: Create a tenant API key
    question: How do I create an API key for an AI agent?
  - id: ApiKeysController_whoami
    intent: Check which key I'm using
    question: Are my current credentials valid, and which tenant are they connected to?
  - id: ApiKeysController_reveal
    intent: Reveal an API key's secret value
    question: Can I see the raw value of an API key I created earlier?
  - id: ApiKeysController_structuredScopes
    intent: Get the API key scope catalog
    question: Which scopes can I grant to an API key, and which are dangerous?
  - id: ApiKeysController_update
    intent: Toggle act-as-me on an API key
    question: Can I upgrade an existing key to act as me without changing its value?
  - id: ApiKeysController_remove
    intent: Permanently delete an API key
    question: How do I permanently delete an API key?
  - id: ApiKeysController_revoke
    intent: Revoke an API key
    question: Can I deactivate an API key but keep its record?
  phrasing_ops: 8
  slug: live-direct-marketing-online-api-keys-tenant-scoped-api
- baseURL: https://api.live-direct-marketing.online
  baseurl_source: declared
  description: The Audit API from Live Direct Marketing — 2 operation(s) for audit.
  name: Live Direct Marketing Audit API
  phrasing_intents:
  - id: AuditController_list
    intent: List audit events
    question: Who did what in my workspace, and can I filter by actor or action?
  - id: AuditController_manualWrite
    intent: Write an audit event manually
    question: Can an agent record its own actions in the audit log?
  - id: AuditController_aggregates
    intent: Count audit events over a date range
    question: How many audit events happened in my workspace over a period?
  phrasing_ops: 3
  slug: live-direct-marketing-online-audit-api
- baseURL: https://api.live-direct-marketing.online
  baseurl_source: declared
  description: The auth API from Live Direct Marketing — 8 operation(s) for auth.
  name: Live Direct Marketing Auth API
  phrasing_intents:
  - id: AuthController_register
    intent: Register a new account
    question: How do I sign up for a new account?
  - id: AuthController_verify
    intent: Verify an email address with a token
    question: How do I confirm my email address after signing up?
  - id: AuthController_resend
    intent: Resend the verification email
    question: I never got the verification email, can it be sent again?
  - id: AuthController_login
    intent: Log in with email and password
    question: How do I log in with my email and password?
  - id: AuthController_logout
    intent: Log out of the current session
    question: How do I end my session?
  - id: AuthController_me
    intent: Get the signed-in user
    question: Who am I logged in as?
  - id: EmailAccessController_request
    intent: Request an email sign-in link
    question: Can I get access sent to my email instead of using a password?
  - id: EmailAccessController_consume
    intent: Use an email access link to sign in
    question: What happens when I open the email access link I received?
  phrasing_ops: 8
  slug: live-direct-marketing-online-auth-api
- baseURL: https://api.live-direct-marketing.online
  baseurl_source: declared
  description: The Authentication API from Live Direct Marketing — 13 operation(s) for authentication.
  name: Live Direct Marketing Authentication API
  phrasing_intents:
  - id: AuthController_register
    intent: Register a new account
    question: How do I sign up for a new Live Direct Marketing account?
  - id: AuthController_verifyEmail
    intent: Confirm a signup email address
    question: What do I do with the token from my signup confirmation email?
  - id: AuthController_submitQuestionnaire
    intent: Submit the signup questionnaire for approval
    question: My signup was not auto-activated because I used a free mailbox; what extra information do I submit?
  - id: AuthController_exchangeOtc
    intent: Exchange a one-time sign-in code for a session
    question: After verifying my email I got a one-time code; how is it turned into a session?
  - id: AuthController_login
    intent: Log in with email and password
    question: Can I log in with my email and password and get access and refresh tokens?
  - id: AuthController_refresh
    intent: Refresh an access token
    question: My access token expired; can I get a new one without logging in again?
  - id: AuthController_logout
    intent: Log out and revoke a refresh token
    question: Can I end my session so the refresh token can no longer be used?
  - id: AuthController_forgotPassword
    intent: Request a password reset email
    question: I forgot my password; can I have a reset link emailed to me?
  phrasing_ops: 13
  slug: live-direct-marketing-online-authentication-api
- baseURL: https://api.live-direct-marketing.online
  baseurl_source: declared
  description: The Best Send Time API from Live Direct Marketing — 1 operation(s) for best send time.
  name: Live Direct Marketing Best Send Time API
  phrasing_intents:
  - id: BestSendTimeController_resolve
    intent: Recommend the best time to send to a contact
    question: When is the best time to email a particular contact?
  phrasing_ops: 1
  slug: live-direct-marketing-online-best-send-time-api
- baseURL: https://api.live-direct-marketing.online
  baseurl_source: declared
  description: The beta-signups API from Live Direct Marketing — 1 operation(s) for beta-signups.
  name: Live Direct Marketing Beta Signups API
  phrasing_intents:
  - id: BetaSignupsController_submit
    intent: Sign up for the beta
    question: How do I join the beta program?
  phrasing_ops: 1
  slug: live-direct-marketing-online-beta-signups-api
- baseURL: https://api.live-direct-marketing.online
  baseurl_source: declared
  description: The Billing API from Live Direct Marketing — 2 operation(s) for billing.
  name: Live Direct Marketing Billing API
  phrasing_intents:
  - id: BillingController_getBalance
    intent: Check account balance and operation prices
    question: How much money is left on my account balance?
  - id: BillingController_listLedger
    intent: List balance charges and credits
    question: What has been charged to my balance for a given campaign?
  phrasing_ops: 2
  slug: live-direct-marketing-online-billing-api
- baseURL: https://api.live-direct-marketing.online
  baseurl_source: declared
  description: The Branding API from Live Direct Marketing — 1 operation(s) for branding.
  name: Live Direct Marketing Branding API
  phrasing_intents:
  - id: BrandingController_get
    intent: Get the workspace's white-label branding
    question: What white-label branding is applied to my workspace?
  - id: BrandingController_update
    intent: Update white-label branding
    question: How do I change the logo or colors of my white-labelled workspace?
  - id: BrandingController_reset
    intent: Reset white-label branding to defaults
    question: How do I throw away my custom branding and go back to the defaults?
  phrasing_ops: 3
  slug: live-direct-marketing-online-branding-api
- baseURL: https://api.live-direct-marketing.online
  baseurl_source: declared
  description: The Briefs API from Live Direct Marketing — 23 operation(s) for briefs.
  name: Live Direct Marketing Briefs API
  phrasing_intents:
  - id: BriefsController_getSchemas
    intent: Get the available brief JSON schemas
    question: What JSON schemas can a brief's content follow?
  - id: BriefsController_intake
    intent: Get the intake email address for a brief
    question: What email address do I forward material to so it lands on a specific brief?
  - id: BriefsController_listIntakeItems
    intent: List incoming intake messages
    question: Which messages have arrived in the brief intake inbox?
  - id: BriefsController_getIntakeItem
    intent: Read one intake item with its provenance
    question: Can I see the full original intake message with its attachments and work log?
  - id: BriefsController_transitionIntakeItem
    intent: Change an intake item's review status
    question: How do I mark an intake message as ignored or rejected?
  - id: BriefsController_linkIntakeItem
    intent: Link an intake item to a brief
    question: How do I attach an incoming intake message and its files to a brief?
  - id: BriefsController_logIntakeWork
    intent: Log agent work on an intake item
    question: How does an agent record what it did with an intake message?
  - id: BriefsController_findAll
    intent: List briefs
    question: Which campaign briefs exist in my workspace?
  phrasing_ops: 27
  slug: live-direct-marketing-online-briefs-api
- baseURL: https://api.live-direct-marketing.online
  baseurl_source: declared
  description: The Browser Queue API from Live Direct Marketing — 6 operation(s) for browser queue.
  name: Live Direct Marketing Browser Queue API
  phrasing_intents:
  - id: BrowserQueueController_getStats
    intent: View browser queue stats
    question: How busy is the browser job queue right now?
  - id: BrowserQueueController_getJobs
    intent: List browser queue jobs by status
    question: Which browser jobs are failed or still waiting?
  - id: BrowserQueueController_cancelJob
    intent: Cancel a browser queue job
    question: Can I cancel a stuck browser job?
  - id: BrowserQueueController_retryJob
    intent: Retry a failed browser job
    question: Can I rerun a browser job that failed?
  - id: BrowserQueueController_pause
    intent: Pause the browser queue
    question: How do I stop the browser queue from picking up new jobs?
  - id: BrowserQueueController_resume
    intent: Resume the browser queue
    question: Can I restart a paused browser queue?
  phrasing_ops: 6
  slug: live-direct-marketing-online-browser-queue-api
- baseURL: https://api.live-direct-marketing.online
  baseurl_source: declared
  description: The Campaign Groups API from Live Direct Marketing — 3 operation(s) for campaign groups.
  name: Live Direct Marketing Campaign Groups API
  phrasing_intents:
  - id: CampaignGroupsController_findAll
    intent: List campaign groups
    question: What campaign groups (folders) do I have?
  - id: CampaignGroupsController_create
    intent: Create a campaign group
    question: How do I create a folder to organize campaigns?
  - id: CampaignGroupsController_reorder
    intent: Reorder campaign groups
    question: How do I change the order my campaign groups appear in?
  - id: CampaignGroupsController_update
    intent: Update a campaign group
    question: How do I rename or recolor a campaign group?
  - id: CampaignGroupsController_remove
    intent: Delete a campaign group
    question: What happens to campaigns inside a group when I delete it?
  phrasing_ops: 5
  slug: live-direct-marketing-online-campaign-groups-api
- baseURL: https://api.live-direct-marketing.online
  baseurl_source: declared
  description: The Campaigns API from Live Direct Marketing — 38 operation(s) for campaigns.
  name: Live Direct Marketing Campaigns API
  phrasing_intents:
  - id: CampaignsController_createTestTask
    intent: Create a test send task for a campaign
    question: Can I send a test of a campaign to one intended recipient before launching it?
  - id: CampaignsController_getTestTask
    intent: Check a campaign test-send task
    question: What happened to the test send I queued for my campaign?
  - id: CampaignsController_conveyorHealth
    intent: Check campaign conveyor health
    question: Which of my campaigns have due emails ready but aren't actually sending?
  - id: CampaignsController_list
    intent: List campaigns
    question: How do I see all my email campaigns page by page?
  - id: CampaignsController_create
    intent: Create an email campaign
    question: How do I set up a new outreach campaign?
  - id: CampaignsController_backfillHistoricUnsubscribes
    intent: Backfill historic unsubscribes into campaigns
    question: Can I mark campaign recipients as unsubscribed if their address is already on the suppression list?
  - id: CampaignsController_overview
    intent: Get a campaigns overview for the dashboard
    question: What does the mailings widget summary look like for my campaigns?
  - id: CampaignsController_get
    intent: Get a campaign
    question: How do I pull up the full settings of one campaign?
  phrasing_ops: 41
  slug: live-direct-marketing-online-campaigns-api
- baseURL: https://api.live-direct-marketing.online
  baseurl_source: declared
  description: The Canvas API from Live Direct Marketing — 4 operation(s) for canvas.
  name: Live Direct Marketing Canvas API
  phrasing_intents:
  - id: CanvasController_getFlow
    intent: Get a campaign's canvas flow
    question: What does the step-by-step flow of a canvas campaign look like?
  - id: CanvasController_putFlow
    intent: Replace a campaign's canvas flow
    question: How do I save a redesigned canvas flow for a campaign?
  - id: CanvasController_stats
    intent: Get per-step canvas stats
    question: How many recipients are at each step of a canvas campaign?
  - id: CanvasController_enrollments
    intent: List contacts enrolled in a canvas
    question: Who is enrolled in a canvas campaign right now?
  - id: CanvasController_tick
    intent: Advance a canvas by one orchestrator tick
    question: How do I manually push canvas recipients forward to their next step?
  phrasing_ops: 5
  slug: live-direct-marketing-online-canvas-api
- baseURL: https://api.live-direct-marketing.online
  baseurl_source: declared
  description: The Cohort Metrics API from Live Direct Marketing — 3 operation(s) for cohort metrics.
  name: Live Direct Marketing Cohort Metrics API
  phrasing_intents:
  - id: CohortMetricsController_funnel
    intent: Get a sequence's conversion funnel
    question: How many prospects moved from sent to opened to replied in my sequence?
  - id: CohortMetricsController_latency
    intent: Get reply latency for a sequence
    question: How long do prospects take to reply to my sequence?
  - id: CohortMetricsController_cohorts
    intent: Break a sequence down by cohort
    question: How do different enrollment cohorts of a sequence compare?
  phrasing_ops: 3
  slug: live-direct-marketing-online-cohort-metrics-api
- baseURL: https://api.live-direct-marketing.online
  baseurl_source: declared
  description: The Companies API from Live Direct Marketing — 19 operation(s) for companies.
  name: Live Direct Marketing Companies API
  phrasing_intents:
  - id: CompaniesController_getStats
    intent: Get company statistics
    question: How many companies do I have in my CRM and how are they broken down?
  - id: CompaniesController_findAll
    intent: List and filter companies
    question: Can I page through my companies and search them by name or domain?
  - id: CompaniesController_create
    intent: Create a company record
    question: How do I add a new company to my CRM?
  - id: CompaniesController_findDuplicates
    intent: Find duplicate companies
    question: Do I have duplicate companies in my workspace?
  - id: CompaniesController_findById
    intent: Get a company by id
    question: What details do I have stored for a specific company?
  - id: CompaniesController_update
    intent: Update a company's details
    question: Can I change the website, phone or LinkedIn of an existing company?
  - id: CompaniesController_softDelete
    intent: Move a company to the trash
    question: How do I delete a company but keep the option to restore it?
  - id: CompaniesController_getTimeline
    intent: View a company's activity timeline
    question: What has happened with a company recently?
  phrasing_ops: 23
  slug: live-direct-marketing-online-companies-api
- baseURL: https://api.live-direct-marketing.online
  baseurl_source: declared
  description: The Companies / Custom Fields API from Live Direct Marketing — 4 operation(s) for companies / custom fields.
  name: Live Direct Marketing Companies / Custom Fields API
  phrasing_intents:
  - id: CompanyCustomFieldController_getDefinitions
    intent: List company, contact or lead custom fields
    question: Which custom fields are defined on companies?
  - id: CompanyCustomFieldController_createDefinition
    intent: Create a company custom field
    question: How do I add a new custom field to company records?
  - id: CompanyCustomFieldController_reorder
    intent: Reorder company custom fields
    question: How do I change the order company custom fields appear in?
  - id: CompanyCustomFieldController_getValues
    intent: Get a company's custom field values
    question: What custom field values are filled in for a particular company?
  - id: CompanyCustomFieldController_setValues
    intent: Set a company's custom field values
    question: How do I fill in several custom fields on a company at once?
  - id: CompanyCustomFieldController_updateDefinition
    intent: Update a company custom field definition
    question: How do I change the label or options of a company custom field?
  - id: CompanyCustomFieldController_deleteDefinition
    intent: Delete a company custom field definition
    question: How do I delete a company custom field?
  phrasing_ops: 7
  slug: live-direct-marketing-online-companies-custom-fields-api
- baseURL: https://api.live-direct-marketing.online
  baseurl_source: declared
  description: The Companies / Duplicates API from Live Direct Marketing — 5 operation(s) for companies / duplicates.
  name: Live Direct Marketing Companies / Duplicates API
  phrasing_intents:
  - id: DuplicatesController_getFields
    intent: List fields usable for duplicate matching
    question: Which company fields can I match on when looking for duplicates?
  - id: DuplicatesController_scan
    intent: Scan companies for duplicates
    question: How do I find duplicate company records in my database?
  - id: DuplicatesController_merge
    intent: Merge duplicate company records
    question: How do I combine duplicate companies into a single record?
  - id: DuplicatesController_deleteDuplicates
    intent: Delete duplicate company records
    question: Can I just delete the extra copies of companies found by the duplicate scan?
  - id: DuplicatesController_moveToList
    intent: Move duplicate companies into a list
    question: Can I put duplicate companies into a separate list for manual review?
  phrasing_ops: 5
  slug: live-direct-marketing-online-companies-duplicates-api
- baseURL: https://api.live-direct-marketing.online
  baseurl_source: declared
  description: The Company List Groups API from Live Direct Marketing — 3 operation(s) for company list groups.
  name: Live Direct Marketing Company List Groups API
  phrasing_intents:
  - id: CompanyListGroupsController_findAll
    intent: List company list groups
    question: How are my company lists grouped into folders?
  - id: CompanyListGroupsController_create
    intent: Create a company list group
    question: How do I create a folder to organize company lists?
  - id: CompanyListGroupsController_reorder
    intent: Reorder company list groups
    question: Can I change the order company list groups appear in?
  - id: CompanyListGroupsController_update
    intent: Update a company list group
    question: Can I rename or recolor a company list group?
  - id: CompanyListGroupsController_remove
    intent: Delete a company list group
    question: What happens to the lists inside a company list group when I delete it?
  phrasing_ops: 5
  slug: live-direct-marketing-online-company-list-groups-api
- baseURL: https://api.live-direct-marketing.online
  baseurl_source: declared
  description: The Company Lists API from Live Direct Marketing — 7 operation(s) for company lists.
  name: Live Direct Marketing Company Lists API
  phrasing_intents:
  - id: CompanyListsController_findAll
    intent: List company lists
    question: Which company lists do I have in my workspace?
  - id: CompanyListsController_create
    intent: Create a company list
    question: How do I create a new list to group target companies?
  - id: CompanyListsController_contactsCounts
    intent: Count contacts behind each company list
    question: How many contacts belong to the companies in each of my lists?
  - id: CompanyListsController_update
    intent: Update a company list
    question: Can I rename a company list or pin it to the top?
  - id: CompanyListsController_remove
    intent: Delete a company list
    question: Can I delete a company list I no longer use?
  - id: CompanyListsController_reorder
    intent: Reorder company lists
    question: Can I change the order my company lists appear in?
  - id: CompanyListsController_addCompanies
    intent: Add companies to a list
    question: How do I put specific companies into one of my lists?
  - id: CompanyListsController_removeCompanies
    intent: Remove companies from a list
    question: Can I take companies out of a list without deleting them?
  phrasing_ops: 10
  slug: live-direct-marketing-online-company-lists-api
- baseURL: https://api.live-direct-marketing.online
  baseurl_source: declared
  description: The Connectors API from Live Direct Marketing — 2 operation(s) for connectors.
  name: Live Direct Marketing Connectors API
  phrasing_intents:
  - id: ConnectorsController_tildaWebhook
    intent: Receive Tilda form submissions as leads
    question: Can Tilda website form submissions flow into my sales pipeline?
  - id: ConnectorsController_dadataName
    intent: Normalize a Russian full name
    question: Can I clean up a Russian person's full name into surname, first name and patronymic?
  phrasing_ops: 2
  slug: live-direct-marketing-online-connectors-api
- baseURL: https://api.live-direct-marketing.online
  baseurl_source: declared
  description: The Contact List Groups API from Live Direct Marketing — 3 operation(s) for contact list groups.
  name: Live Direct Marketing Contact List Groups API
  phrasing_intents:
  - id: ContactListGroupsController_findAll
    intent: List contact list groups
    question: How are my contact lists organized into groups?
  - id: ContactListGroupsController_create
    intent: Create a contact list group
    question: How do I make a folder to organize my contact lists?
  - id: ContactListGroupsController_reorder
    intent: Reorder contact list groups
    question: Can I change the order my contact list groups appear in?
  - id: ContactListGroupsController_update
    intent: Update a contact list group
    question: Can I rename a contact list group or change its color?
  - id: ContactListGroupsController_remove
    intent: Delete a contact list group
    question: What happens to the lists inside a group when I delete the group?
  phrasing_ops: 5
  slug: live-direct-marketing-online-contact-list-groups-api
- baseURL: https://api.live-direct-marketing.online
  baseurl_source: declared
  description: The Contact Lists API from Live Direct Marketing — 8 operation(s) for contact lists.
  name: Live Direct Marketing Contact Lists API
  phrasing_intents:
  - id: ContactListsController_findAll
    intent: List contact lists
    question: What contact lists do I have?
  - id: ContactListsController_create
    intent: Create a contact list
    question: How do I create a new contact list?
  - id: ContactListsController_update
    intent: Update a contact list
    question: Can I rename a contact list or pin it to the top?
  - id: ContactListsController_remove
    intent: Delete a contact list
    question: Can I delete a contact list I no longer need?
  - id: ContactListsController_reorder
    intent: Reorder contact lists
    question: Can I change the order my contact lists appear in?
  - id: ContactListsController_addContacts
    intent: Add contacts to a list
    question: How do I put contacts into an existing list?
  - id: ContactListsController_removeContacts
    intent: Remove contacts from a list
    question: Can I take contacts out of a list without deleting them?
  - id: ContactListsController_duplicate
    intent: Duplicate a contact list
    question: Can I copy a contact list to start a new one?
  phrasing_ops: 11
  slug: live-direct-marketing-online-contact-lists-api
- baseURL: https://api.live-direct-marketing.online
  baseurl_source: declared
  description: The Contacts API from Live Direct Marketing — 19 operation(s) for contacts.
  name: Live Direct Marketing Contacts API
  phrasing_intents:
  - id: ContactsController_getStats
    intent: Get contact statistics
    question: How many contacts do I have, and can I break the stats down for one list?
  - id: ContactsController_findAllDuplicates
    intent: Find duplicate contacts across the workspace
    question: Which contacts across my whole workspace look like duplicates?
  - id: ContactsController_findAll
    intent: List and search contacts
    question: Can I search my contacts and filter them by list, company or email validation status?
  - id: ContactsController_create
    intent: Create a new contact
    question: How do I add a new person to my contacts?
  - id: ContactsController_findById
    intent: Get a contact's details
    question: What details are stored for a particular contact?
  - id: ContactsController_update
    intent: Update a contact's details
    question: Can I change the name, job title or company on an existing contact?
  - id: ContactsController_softDelete
    intent: Move a contact to the trash
    question: Can I delete a contact but still be able to restore it later?
  - id: ContactsController_getTimeline
    intent: Get a contact's activity timeline
    question: What has happened with a contact over time, event by event?
  phrasing_ops: 24
  slug: live-direct-marketing-online-contacts-api
- baseURL: https://api.live-direct-marketing.online
  baseurl_source: declared
  description: The Content Analyzer API from Live Direct Marketing — 1 operation(s) for content analyzer.
  name: Live Direct Marketing Content Analyzer API
  phrasing_intents:
  - id: ContentAnalyzerController_check
    intent: Score an email for spam triggers
    question: Will my email subject and body trigger spam filters?
  phrasing_ops: 1
  slug: live-direct-marketing-online-content-analyzer-api
- baseURL: https://api.live-direct-marketing.online
  baseurl_source: declared
  description: The Creatives API from Live Direct Marketing — 90 operation(s) for creatives.
  name: Live Direct Marketing Creatives API
  phrasing_intents:
  - id: CreativesController_findAll
    intent: List and search creatives
    question: What email creatives and templates do I have in my workspace?
  - id: CreativesController_create
    intent: Create a new creative
    question: How do I create a new email template with a subject and HTML body?
  - id: CreativesController_aiGenerate
    intent: Draft a creative with AI
    question: Can AI write a first draft of a cold email for me from a short prompt?
  - id: CreativesController_createAutopilotV2
    intent: Create an Autopilot v2 creative
    question: How do I start a new creative on the Autopilot v2 engine?
  - id: CreativesController_pdfStatus
    intent: Check the PDF generation queue
    question: How busy is the PDF generation queue right now?
  - id: CreativesController_servePdf
    intent: Download a generated PDF by filename
    question: Where can I download a PDF that was generated from a creative if I know its file name?
  - id: CreativesController_getAvailableVariables
    intent: List template variables I can use
    question: Which merge variables can I put into a template from my contact lists and companies?
  - id: CreativesController_findById
    intent: Get a creative
    question: What subject, body and settings does a specific creative have?
  phrasing_ops: 104
  slug: live-direct-marketing-online-creatives-api
- baseURL: https://api.live-direct-marketing.online
  baseurl_source: declared
  description: The Creatives / On-Demand API from Live Direct Marketing — 6 operation(s) for creatives / on-demand.
  name: Live Direct Marketing Creatives / On-Demand API
  phrasing_intents:
  - id: OnDemandController_generate
    intent: Generate a personalized creative for a contact
    question: How do I generate a personalized version of a creative for one contact?
  - id: OnDemandController_getRequest
    intent: Get an on-demand generation request
    question: Has my on-demand creative generation finished yet?
  - id: OnDemandController_cancel
    intent: Cancel an in-flight generation request
    question: Can I cancel an on-demand creative generation that is still running?
  - id: OnDemandController_list
    intent: List on-demand requests for a creative
    question: Which on-demand generations have been run for a creative?
  - id: OnDemandController_stats
    intent: Get on-demand generation stats for a creative
    question: How many personalized generations has a creative produced over a period?
  - id: OnDemandController_getQcConfig
    intent: Get a creative's quality-control settings
    question: What quality checks run on generated versions of a creative?
  - id: OnDemandController_putQcConfig
    intent: Set a creative's quality-control rules
    question: Can I define my own two-tier quality checks for a creative's generations?
  - id: OnDemandController_resetQcConfig
    intent: Reset a creative's QC settings to defaults
    question: How do I throw away custom QC rules and go back to the defaults?
  phrasing_ops: 8
  slug: live-direct-marketing-online-creatives-on-demand-api
- baseURL: https://api.live-direct-marketing.online
  baseurl_source: declared
  description: The Custom Events API from Live Direct Marketing — 3 operation(s) for custom events.
  name: Live Direct Marketing Custom Events API
  phrasing_intents:
  - id: CustomEventsController_track
    intent: Track a single custom event
    question: How do I record that a lead attended a webinar as a custom event?
  - id: CustomEventsController_list
    intent: List tracked custom events
    question: Which custom events were recorded for a particular contact?
  - id: CustomEventsController_bulkTrack
    intent: Track custom events in bulk
    question: What is the maximum number of custom events I can send in one batch?
  - id: CustomEventsController_aggregates
    intent: Count custom events over a date range
    question: How many custom events of each type happened last month?
  phrasing_ops: 4
  slug: live-direct-marketing-online-custom-events-api
- baseURL: https://api.live-direct-marketing.online
  baseurl_source: declared
  description: The Custom Extract API from Live Direct Marketing — 2 operation(s) for custom extract.
  name: Live Direct Marketing Custom Extract API
  phrasing_intents:
  - id: CustomExtractController_run
    intent: Extract data with a keyword, regex or prompt
    question: Can I pull specific information out of text I already have using a regex?
  - id: CustomExtractController_getStatus
    intent: Get a prompt extraction job result
    question: Has my AI prompt extraction job finished?
  phrasing_ops: 2
  slug: live-direct-marketing-online-custom-extract-api
- baseURL: https://api.live-direct-marketing.online
  baseurl_source: declared
  description: The Custom Fields API from Live Direct Marketing — 6 operation(s) for custom fields.
  name: Live Direct Marketing Custom Fields API
  phrasing_intents:
  - id: CustomFieldsController_findAll
    intent: List custom field definitions for an entity
    question: Which custom fields are defined for my contacts or leads?
  - id: CustomFieldsController_create
    intent: Define a new custom field
    question: How do I add a new custom field to a record type?
  - id: CustomFieldsController_inventory
    intent: Report custom field storage divergence
    question: Are my custom field values out of sync between JSON and table storage?
  - id: CustomFieldsController_update
    intent: Update a custom field definition
    question: How do I rename or relabel an existing custom field?
  - id: CustomFieldsController_remove
    intent: Delete a custom field definition
    question: How do I remove a custom field I no longer need?
  - id: CustomFieldsController_reorder
    intent: Reorder custom field definitions
    question: How do I change the order custom fields appear in?
  - id: CustomFieldsController_getValues
    intent: Get custom field values for a record
    question: What custom field values are stored on a particular contact or lead?
  - id: CustomFieldsController_setValue
    intent: Set one custom field value on a record
    question: How do I fill in a custom field on a specific record?
  phrasing_ops: 10
  slug: live-direct-marketing-online-custom-fields-api
- baseURL: https://api.live-direct-marketing.online
  baseurl_source: declared
  description: The Custom Objects API from Live Direct Marketing — 4 operation(s) for custom objects.
  name: Live Direct Marketing Custom Objects API
  phrasing_intents:
  - id: CustomObjectsController_listDefs
    intent: List custom object definitions
    question: Which custom object types have we defined?
  - id: CustomObjectsController_createDef
    intent: Define a new custom object type
    question: How do I add a new custom object type to the CRM?
  - id: CustomObjectsController_getDef
    intent: Get a custom object definition
    question: What fields does a custom object type have?
  - id: CustomObjectsController_updateDef
    intent: Update a custom object definition
    question: How do I add a field to an existing custom object type?
  - id: CustomObjectsController_deleteDef
    intent: Delete a custom object definition
    question: How do I remove a custom object type I no longer use?
  - id: CustomObjectsController_listRecords
    intent: List records of a custom object
    question: What records exist for one of my custom object types?
  - id: CustomObjectsController_createRecord
    intent: Add a record to a custom object
    question: How do I add a new entry to a custom object?
  - id: CustomObjectsController_getRecord
    intent: Get a custom object record
    question: How do I fetch one custom object record by its id?
  phrasing_ops: 10
  slug: live-direct-marketing-online-custom-objects-api
- baseURL: https://api.live-direct-marketing.online
  baseurl_source: declared
  description: The Deliverability API from Live Direct Marketing — 11 operation(s) for deliverability.
  name: Live Direct Marketing Deliverability API
  phrasing_intents:
  - id: DeliverabilityController_startRelayReach
    intent: Probe whether a relay can reach mail providers
    question: Can my sending relay deliver to Gmail and other mailbox providers at all?
  - id: DeliverabilityController_startCreativeThroughRelay
    intent: Probe whether a creative reaches the inbox
    question: Does a specific email creative land in the inbox through my relay?
  - id: DeliverabilityController_getMatrix
    intent: Get the deliverability matrix
    question: Which relays can reach which mailbox providers right now?
  - id: DeliverabilityController_startCreativeTune
    intent: Auto-tune a creative until it reaches the inbox
    question: Can the system rewrite my creative to get past spam filters?
  - id: DeliverabilityController_startFullPipeline
    intent: Run the full deliverability probe pipeline
    question: Can I test every relay against every provider and auto-tune creatives in one go?
  - id: DeliverabilityController_promoteTunedVariant
    intent: Promote a tuned variant to a new creative
    question: How do I save a tuned email variant as a real creative I can use?
  - id: DeliverabilityController_getJobStatus
    intent: Check the status of a probe batch
    question: Has my deliverability probe batch finished?
  - id: DeliverabilityController_cancelProbeJob
    intent: Cancel pending probes in a batch
    question: Can I stop a deliverability probe batch that's still running?
  phrasing_ops: 13
  slug: live-direct-marketing-online-deliverability-api
- baseURL: https://api.live-direct-marketing.online
  baseurl_source: declared
  description: The deploy API from Live Direct Marketing — 2 operation(s) for deploy.
  name: Live Direct Marketing Deploy API
  phrasing_intents:
  - id: DeployController_enqueue
    intent: Queue a new deploy
    question: How do I trigger a deploy from the admin API?
  - id: DeployController_list
    intent: List deploy jobs
    question: Which admin deploys have been run recently?
  - id: DeployController_status
    intent: Check a deploy job's status
    question: Has my deploy job finished or failed?
  phrasing_ops: 3
  slug: live-direct-marketing-online-deploy-api
- baseURL: https://api.live-direct-marketing.online
  baseurl_source: declared
  description: The Development Pipeline API from Live Direct Marketing — 13 operation(s) for development pipeline.
  name: Live Direct Marketing Development Pipeline API
  phrasing_intents:
  - id: DevelopmentPipelineController_board
    intent: View the development delivery board
    question: Which issues are in queue, with agents, in merge or deploying right now?
  - id: DevelopmentPipelineController_attentionSnapshot
    intent: See what in the pipeline needs an owner
    question: Which red tasks, failed deploys or agent questions need my attention?
  - id: DevelopmentPipelineController_prodCounter
    intent: Count issues shipped to production
    question: How many issues have actually shipped to prod with a green smoke check?
  - id: DevelopmentPipelineController_ciRunsPerMerge
    intent: Measure CI runs per merge
    question: How many CI runs does each merge take on average?
  - id: DevelopmentPipelineController_journalSnapshot
    intent: Read the tester journal
    question: What rules, roles and findings are in the tester journal?
  - id: DevelopmentPipelineController_createIssueFromFinding
    intent: Open an issue from a journal finding
    question: How do I turn a tester journal finding into a tracked issue?
  - id: DevelopmentPipelineController_appendJournalFinding
    intent: Add a finding to the tester journal
    question: How do I append a new finding line to the tester journal?
  - id: DevelopmentPipelineController_setPaused
    intent: Pause or unpause a development issue
    question: How do I stop agents from picking up an issue for now?
  phrasing_ops: 13
  slug: live-direct-marketing-online-development-pipeline-api
- baseURL: https://api.live-direct-marketing.online
  baseurl_source: declared
  description: The Development Pipeline — Conveyor Bridge API from Live Direct Marketing — 5 operation(s) for development pipeline — conveyor bridge.
  name: Live Direct Marketing Development Pipeline — Conveyor Bridge API
  phrasing_intents:
  - id: ConveyorBridgeController_createIssue
    intent: Create a conveyor development task
    question: How do I file a new task on the development conveyor?
  - id: ConveyorBridgeController_setPriority
    intent: Set a conveyor task's priority
    question: Can I bump a conveyor task to P1?
  - id: ConveyorBridgeController_setPaused
    intent: Pause or unpause a conveyor task
    question: Can I pause a conveyor task from the console?
  - id: ConveyorBridgeController_issueAction
    intent: Retry or cancel a stuck conveyor task
    question: Can I retry a conveyor task that's blocked or failed?
  - id: ConveyorBridgeController_getTemplate
    intent: Get the conveyor task template and rules
    question: What rules and template does the development conveyor expect?
  phrasing_ops: 5
  slug: live-direct-marketing-online-development-pipeline-conveyor-bridge-api
- baseURL: https://api.live-direct-marketing.online
  baseurl_source: declared
  description: The Dialog Linker API from Live Direct Marketing — 6 operation(s) for dialog linker.
  name: Live Direct Marketing Dialog Linker API
  phrasing_intents:
  - id: DialogLinkerController_relink
    intent: Re-run CRM linking for one dialog
    question: Can I re-run the linker on one conversation that was matched wrong?
  - id: DialogLinkerController_backfill
    intent: Backfill dialog linking across the tenant
    question: Can an admin link every old conversation in the workspace in one run?
  - id: DialogLinkerController_getStats
    intent: Get dialog linker statistics
    question: How many conversations are linked, pending or failed?
  - id: DialogLinkerController_getFailureSummary
    intent: Summarize dialog linking failures
    question: Why are conversations failing to link to contacts?
  - id: DialogLinkerController_getLogs
    intent: Get linker logs for one dialog
    question: What did the linker try when matching a specific conversation?
  - id: DialogLinkerController_getAllLogs
    intent: Get the full dialog linker log
    question: Is there an admin technical log of every linker run across the tenant?
  phrasing_ops: 6
  slug: live-direct-marketing-online-dialog-linker-api
- baseURL: https://api.live-direct-marketing.online
  baseurl_source: declared
  description: The Dialogs API from Live Direct Marketing — 44 operation(s) for dialogs.
  name: Live Direct Marketing Dialogs API
  phrasing_intents:
  - id: DialogsController_findAll
    intent: List email dialogs with filters
    question: Can I filter my inbox dialogs by channel, status or folder?
  - id: DialogsController_getStats
    intent: Get aggregate dialog statistics
    question: How many dialogs do I have in total across my inbox?
  - id: DialogsController_getBadges
    intent: Get dialog badges for a set of leads
    question: Can I fetch dialog badges for many leads in one call?
  - id: DialogsController_getAccounts
    intent: List email accounts used in dialogs
    question: Which mailbox accounts are my dialogs coming through?
  - id: DialogsController_getFolders
    intent: List dialog folders
    question: What folders are my dialogs organized into?
  - id: DialogsController_getThread
    intent: Get a full dialog thread
    question: How do I see every message in an email thread at once?
  - id: DialogsController_bulk
    intent: Apply a bulk action to many dialogs
    question: Can I apply one action to many dialogs at the same time?
  - id: DialogsController_imapMove
    intent: Move dialogs to an IMAP folder
    question: Can I move conversations into a different folder on the mail server?
  phrasing_ops: 49
  slug: live-direct-marketing-online-dialogs-api
- baseURL: https://api.live-direct-marketing.online
  baseurl_source: declared
  description: The domain-watch API from Live Direct Marketing — 7 operation(s) for domain-watch.
  name: Live Direct Marketing Domain Watch API
  phrasing_intents:
  - id: DomainWatchController_start
    intent: Start domain watch for a domain
    question: Where do I begin setting up monitoring for one of my sending domains?
  - id: DomainWatchController_request
    intent: Request a domain watch confirmation email
    question: How do I get the confirmation email needed before domain monitoring starts?
  - id: DomainWatchController_confirmView
    intent: View the domain watch consent page
    question: Will clicking the domain watch confirmation link subscribe my mailbox automatically?
  - id: DomainWatchController_confirm
    intent: Confirm consent and activate domain watch
    question: How do I give explicit consent so monitoring of my domain actually starts?
  - id: DomainWatchController_manage
    intent: Open the domain watch management page
    question: Where can I manage an existing domain watch subscription from my email link?
  - id: DomainWatchController_access
    intent: Request access to manage domain watch
    question: I lost my link; can I request access to manage my domain watch again?
  - id: DomainWatchController_stop
    intent: Stop domain watch monitoring
    question: Can I turn off monitoring for a domain I am watching?
  - id: DomainWatchController_unsubscribeView
    intent: View the domain watch unsubscribe page
    question: What does the unsubscribe link in a domain watch email open?
  phrasing_ops: 9
  slug: live-direct-marketing-online-domain-watch-api
- baseURL: https://api.live-direct-marketing.online
  baseurl_source: declared
  description: The DomainObservations API from Live Direct Marketing — 6 operation(s) for domainobservations.
  name: Live Direct Marketing Domain Observations API
  phrasing_intents:
  - id: DomainObservationsController_lookup
    intent: Look up observations for a domain
    question: Are there any recorded observations for a given domain?
  - id: DomainObservationsController_request
    intent: Request domain observations
    question: How do I ask for a domain to start being observed?
  - id: DomainObservationsController_page
    intent: Get a domain's observation page for a date range
    question: What was observed about a domain between two dates?
  - id: DomainObservationsController_fallback
    intent: Get the domain observations fallback page
    question: What is shown when no specific domain observation page is available?
  - id: DomainObservationsController_data
    intent: Get raw observation data for a domain
    question: Can I get the underlying observation data for a domain rather than the page?
  - id: DomainObservationsController_catalog
    intent: Browse the catalog of observed domains
    question: Which domains are in the observations catalog?
  phrasing_ops: 6
  slug: live-direct-marketing-online-domainobservations-api
- baseURL: https://api.live-direct-marketing.online
  baseurl_source: declared
  description: The Domains API from Live Direct Marketing — 2 operation(s) for domains.
  name: Live Direct Marketing Domains API
  phrasing_intents:
  - id: DomainsController_check
    intent: Check DNS health for a domain
    question: Is my sending domain's DNS set up correctly?
  - id: DomainsController_bulk
    intent: Check DNS health for many domains at once
    question: Can I check DNS health for a batch of domains together?
  phrasing_ops: 2
  slug: live-direct-marketing-online-domains-api
- baseURL: https://api.live-direct-marketing.online
  baseurl_source: declared
  description: The DomainWatchPlacement API from Live Direct Marketing — 1 operation(s) for domainwatchplacement.
  name: Live Direct Marketing Domain Watch Placement API
  phrasing_intents:
  - id: DomainWatchPlacementController_get
    intent: Get domain-watch placement results
    question: Where did my watched domain's email land in the placement check?
  - id: DomainWatchPlacementController_start
    intent: Start a domain-watch placement check
    question: Can I start an inbox placement check for a watched domain?
  phrasing_ops: 2
  slug: live-direct-marketing-online-domainwatchplacement-api
- baseURL: https://api.live-direct-marketing.online
  baseurl_source: declared
  description: The DSAR API from Live Direct Marketing — 3 operation(s) for dsar.
  name: Live Direct Marketing DSAR API
  phrasing_intents:
  - id: DsarController_create
    intent: Submit a data-subject request
    question: How does someone ask for their personal data to be erased?
  - id: DsarController_list
    intent: List data-subject requests
    question: Which GDPR data-subject requests are still open?
  - id: DsarController_lookup
    intent: Look up a data subject by email
    question: Is a given email address globally suppressed?
  - id: DsarController_resolve
    intent: Resolve a data-subject request
    question: How do I mark a data-subject request as handled?
  phrasing_ops: 4
  slug: live-direct-marketing-online-dsar-api
- baseURL: https://api.live-direct-marketing.online
  baseurl_source: declared
  description: The Email Accounts API from Live Direct Marketing — 34 operation(s) for email accounts.
  name: Live Direct Marketing Email Accounts API
  phrasing_intents:
  - id: EmailAccountsController_lookupProvider
    intent: Look up SMTP/IMAP settings for an address
    question: What SMTP and IMAP server settings should I use for a given email address?
  - id: EmailAccountsController_testUnsaved
    intent: Test mailbox credentials before saving
    question: Can I check SMTP and IMAP credentials work before I save a new mailbox?
  - id: EmailAccountsController_findAll
    intent: List sending email accounts
    question: Which email accounts do I have connected for sending?
  - id: EmailAccountsController_create
    intent: Add a new email account
    question: How do I add a new mailbox for sending campaigns?
  - id: EmailAccountsController_getStats
    intent: Get totals across all email accounts
    question: What are the aggregated stats across all my email accounts?
  - id: EmailAccountsController_checkDuplicate
    intent: Check if an email address is already added
    question: Is this email address already registered as a mailbox?
  - id: EmailAccountsController_relayHealthSummary
    intent: Summarize relay health across the tenant
    question: How many of my relays are sending right now and how many dropped out?
  - id: EmailAccountsController_relayAttention
    intent: List relays that need a human to fix
    question: Which relays has automation given up recovering?
  phrasing_ops: 40
  slug: live-direct-marketing-online-email-accounts-api
- baseURL: https://api.live-direct-marketing.online
  baseurl_source: declared
  description: The Email Accounts — Deliverability API from Live Direct Marketing — 3 operation(s) for email accounts — deliverability.
  name: Live Direct Marketing Email Accounts — Deliverability API
  phrasing_intents:
  - id: EmailAccountDeliverabilityController_getAccountSnapshot
    intent: View a mailbox's deliverability snapshot
    question: Is my sending mailbox landing in the inbox at each mail provider?
  - id: EmailAccountDeliverabilityController_probeAccount
    intent: Run a deliverability probe on a mailbox
    question: Can I test a mailbox's deliverability right now instead of waiting?
  - id: EmailAccountDeliverabilityController_unblockProvider
    intent: Unblock a mail provider for a mailbox
    question: Can I lift the block that stops my mailbox sending to one provider?
  phrasing_ops: 3
  slug: live-direct-marketing-online-email-accounts-deliverability-api
- baseURL: https://api.live-direct-marketing.online
  baseurl_source: declared
  description: The Email Accounts / GAS Webhook API from Live Direct Marketing — 1 operation(s) for email accounts / gas webhook.
  name: Live Direct Marketing Email Accounts / GAS Webhook API
  phrasing_intents:
  - id: GasWebhookController_handleWebhook
    intent: Receive an Apps Script mail push
    question: How does a Google Apps Script mailbox notify the platform of new mail?
  phrasing_ops: 1
  slug: live-direct-marketing-online-email-accounts-gas-webhook-api
- baseURL: https://api.live-direct-marketing.online
  baseurl_source: declared
  description: The Email Accounts / Inbox Ingest API from Live Direct Marketing — 1 operation(s) for email accounts / inbox ingest.
  name: Live Direct Marketing Email Accounts / Inbox Ingest API
  phrasing_intents:
  - id: InboxIngestController_mailArrived
    intent: Signal new mail and trigger an IMAP fetch
    question: How can an internal service tell the platform new mail just arrived?
  phrasing_ops: 1
  slug: live-direct-marketing-online-email-accounts-inbox-ingest-api
- baseURL: https://api.live-direct-marketing.online
  baseurl_source: declared
  description: The Email Verification API from Live Direct Marketing — 2 operation(s) for email verification.
  name: Live Direct Marketing Email Verification API
  phrasing_intents:
  - id: EmailVerificationController_verifyOne
    intent: Verify a single email address
    question: Is this email address valid and deliverable?
  - id: EmailVerificationController_verifyBatch
    intent: Verify a batch of email addresses
    question: Can I validate a whole list of email addresses in one request?
  phrasing_ops: 2
  slug: live-direct-marketing-online-email-verification-api
- baseURL: https://api.live-direct-marketing.online
  baseurl_source: declared
  description: The Enrichment API from Live Direct Marketing — 2 operation(s) for enrichment.
  name: Live Direct Marketing Enrichment API
  phrasing_intents:
  - id: EnrichmentController_company
    intent: Enrich a company profile
    question: Can I get company details from just a domain?
  - id: EnrichmentController_findEmail
    intent: Find a person's email address
    question: How do I find someone's email from their name and company domain?
  phrasing_ops: 2
  slug: live-direct-marketing-online-enrichment-api
- baseURL: https://api.live-direct-marketing.online
  baseurl_source: declared
  description: The Exports API from Live Direct Marketing — 4 operation(s) for exports.
  name: Live Direct Marketing Exports API
  phrasing_intents:
  - id: ExportsController_getColumns
    intent: List exportable columns for an entity
    question: Which columns can I include when exporting contacts?
  - id: ExportsController_create
    intent: Start a data export job
    question: How do I export my data to a file?
  - id: ExportsController_list
    intent: List my export jobs
    question: What exports have I requested?
  - id: ExportsController_status
    intent: Check an export job's status
    question: Is my export finished yet?
  - id: ExportsController_download
    intent: Download a finished export file
    question: Where do I get the file once my export is done?
  phrasing_ops: 5
  slug: live-direct-marketing-online-exports-api
- baseURL: https://api.live-direct-marketing.online
  baseurl_source: declared
  description: The feedback API from Live Direct Marketing — 1 operation(s) for feedback.
  name: Live Direct Marketing Feedback API
  phrasing_intents:
  - id: FeedbackController_submit
    intent: Send product feedback
    question: How do I send feedback about the product?
  phrasing_ops: 1
  slug: live-direct-marketing-online-feedback-api
- baseURL: https://api.live-direct-marketing.online
  baseurl_source: declared
  description: The Files API from Live Direct Marketing — 15 operation(s) for files.
  name: Live Direct Marketing Files API
  phrasing_intents:
  - id: FilesController_importImages
    intent: Import images from an attachment into storage
    question: Can I pull the images out of an attachment into my creative image storage?
  - id: FilesController_uploadImage
    intent: Upload a creative image
    question: How do I upload an image to use in my email creatives?
  - id: FilesController_listImages
    intent: List uploaded creative images
    question: Which creative images have I already uploaded?
  - id: FilesController_deleteImage
    intent: Delete a creative image
    question: Can I remove an uploaded creative image I no longer need?
  - id: FilesController_uploadAsset
    intent: Upload a signature or PDF photo asset
    question: How do I upload a signature image or a photo for personal PDFs?
  - id: FilesController_listAssets
    intent: List tenant assets like signatures
    question: Where can I see the signature and PDF photo assets stored for my account?
  - id: FilesController_getAssetsQuota
    intent: Check tenant asset storage quota
    question: How much of my asset storage quota have I used?
  - id: FilesController_deleteAsset
    intent: Delete a tenant asset
    question: Can I delete an old signature or photo asset?
  phrasing_ops: 19
  slug: live-direct-marketing-online-files-api
- baseURL: https://api.live-direct-marketing.online
  baseurl_source: declared
  description: The Files / Serve API from Live Direct Marketing — 4 operation(s) for files / serve.
  name: Live Direct Marketing Files / Serve API
  phrasing_intents:
  - id: FileServeController_serveImage
    intent: Serve an uploaded creative image
    question: What URL serves an uploaded creative image for a tenant?
  - id: FileServeController_serveTenantAsset
    intent: Serve a tenant signature or photo asset
    question: How do I load a tenant's signature image or PDF photo?
  - id: FileServeController_serveDialogAttachment
    intent: Download an inbound email attachment
    question: How do I download an attachment that came in on a reply?
  - id: FileServeController_serveAvatar
    intent: Serve a user avatar
    question: Where are user avatar images served from?
  phrasing_ops: 4
  slug: live-direct-marketing-online-files-serve-api
- baseURL: https://api.live-direct-marketing.online
  baseurl_source: declared
  description: The health API from Live Direct Marketing — 2 operation(s) for health.
  name: Live Direct Marketing Health API
  phrasing_intents:
  - id: HealthController_check
    intent: Check service health
    question: Is the core service up and responding?
  - id: HealthController_capacity
    intent: Check resource capacity before taking load
    question: Does the service have capacity to accept more work right now?
  phrasing_ops: 2
  slug: live-direct-marketing-online-health-api
- baseURL: https://api.live-direct-marketing.online
  baseurl_source: declared
  description: The ICP Extension / API API from Live Direct Marketing — 17 operation(s) for icp extension / api.
  name: Live Direct Marketing ICP Extension / API
  phrasing_intents:
  - id: IcpExtApiController_authorize
    intent: Authorize the Chrome extension with a project key
    question: How does the Chrome extension get authorized to my project?
  - id: IcpExtApiController_getNextItem
    intent: Get the next ICP review item
    question: Which company is next in my ICP review queue in the extension?
  - id: IcpExtApiController_analyzeAi
    intent: Analyze an ICP review item with AI
    question: Can AI judge whether the company I'm reviewing fits my ideal customer profile?
  - id: IcpExtApiController_enrich
    intent: Enrich a company card from the visited site
    question: Can the extension fill in a company card from the website I'm on?
  - id: IcpExtApiController_complete
    intent: Mark an ICP review item as completed
    question: How do I finish an ICP review item so the next one appears?
  - id: IcpExtApiController_getFormAssistConfig
    intent: Get form assist configuration
    question: What settings does the extension use to help fill in contact forms?
  - id: IcpExtApiController_lookupCompany
    intent: Look up a CRM company by site host
    question: Is the website I'm on already a company in my CRM?
  - id: IcpExtApiController_getFormAssistProfile
    intent: Get profile values for manual form fill
    question: Which saved profile values can I paste into a form from the right-click menu?
  phrasing_ops: 17
  slug: live-direct-marketing-online-icp-extension-api-api
- baseURL: https://api.live-direct-marketing.online
  baseurl_source: declared
  description: The ICP Extension API from Live Direct Marketing — 14 operation(s) for icp extension.
  name: Live Direct Marketing ICP Extension API
  phrasing_intents:
  - id: IcpExtensionController_findAll
    intent: List ICP tasks
    question: Which ICP tasks do I have, and can I filter them by status?
  - id: IcpExtensionController_create
    intent: Create an ICP task
    question: How do I set up a new ideal customer profile task?
  - id: IcpExtensionController_scrapePreview
    intent: Preview website crawl coverage for a company list
    question: Before crawling, how many companies in a list actually have a website domain filled in?
  - id: IcpExtensionController_getScrapeStatus
    intent: Check a company website crawl's progress
    question: How far along is my company website crawl?
  - id: IcpExtensionController_cancelScrape
    intent: Cancel a company website crawl
    question: Can I abort a site crawl that is running on my companies?
  - id: IcpExtensionController_findById
    intent: Get an ICP task
    question: What are the settings of one specific ICP task?
  - id: IcpExtensionController_update
    intent: Update an ICP task
    question: Can I rename an ICP task or change its status and config?
  - id: IcpExtensionController_remove
    intent: Delete an ICP task
    question: Can I delete an ICP task I no longer need?
  phrasing_ops: 17
  slug: live-direct-marketing-online-icp-extension-api
- baseURL: https://api.live-direct-marketing.online
  baseurl_source: declared
  description: The IMAP Orchestrator API from Live Direct Marketing — 24 operation(s) for imap orchestrator.
  name: Live Direct Marketing IMAP Orchestrator API
  phrasing_intents:
  - id: ImapOrchestratorController_getStats
    intent: Show the IMAP orchestrator dashboard stats
    question: What do the overall inbox-fetching dashboard numbers look like right now?
  - id: ImapOrchestratorController_getJobs
    intent: List recent IMAP fetch jobs
    question: Which IMAP fetch jobs ran recently for one of my mailboxes?
  - id: ImapOrchestratorController_fetchAccount
    intent: Fetch new mail for one email account now
    question: Can I force an immediate IMAP fetch for a single mailbox instead of waiting for the schedule?
  - id: ImapOrchestratorController_getAttention
    intent: List mailboxes that need manual attention
    question: Which of my email accounts are stuck and need someone to fix them by hand?
  - id: ImapOrchestratorController_getSyncHealth
    intent: Check inbound mail sync health and quarantine
    question: Is any inbound mail stuck in staging or quarantine for one of my mailboxes?
  - id: ImapOrchestratorController_retryStagedMessage
    intent: Retry a failed or quarantined inbound message
    question: Can I retry an inbound message that failed to sync or got stuck in quarantine?
  - id: ImapOrchestratorController_heal
    intent: Auto-heal stuck mailbox locks in my workspace
    question: Can I automatically unstick frozen GAS accounts and IMAP locks for just my workspace?
  - id: ImapOrchestratorController_healAll
    intent: Auto-heal stuck IMAP state across all tenants
    question: Is there a platform-wide action to heal stuck IMAP and GAS state for every tenant?
  phrasing_ops: 28
  slug: live-direct-marketing-online-imap-orchestrator-api
- baseURL: https://api.live-direct-marketing.online
  baseurl_source: declared
  description: The Import API from Live Direct Marketing — 10 operation(s) for import.
  name: Live Direct Marketing Import API
  phrasing_intents:
  - id: ImportController_getTemplates
    intent: List import templates
    question: Which import templates are available for CSV uploads?
  - id: ImportController_detectTemplate
    intent: Detect the best import template from CSV headers
    question: Can the system guess which import template fits my spreadsheet columns?
  - id: ImportController_applyTemplate
    intent: Map CSV headers with an import template
    question: How do my CSV columns map to fields when I apply a specific template?
  - id: ImportController_createTask
    intent: Start an import of contacts or companies
    question: How do I import contacts from a spreadsheet into a new list?
  - id: ImportController_importFromUrl
    intent: Fetch an import file from a link
    question: Can I import a list straight from a Google Sheets link?
  - id: ImportController_getTask
    intent: Get an import task's status
    question: Is my import finished, and how many rows succeeded?
  - id: ImportController_getLog
    intent: Read an import's row-level log
    question: Which rows in my import failed, and why?
  - id: ImportController_getLogCsv
    intent: Download an import log as CSV
    question: Can I export an import's row log to a CSV file?
  phrasing_ops: 10
  slug: live-direct-marketing-online-import-api
- baseURL: https://api.live-direct-marketing.online
  baseurl_source: declared
  description: The Inbound Rules API from Live Direct Marketing — 7 operation(s) for inbound rules.
  name: Live Direct Marketing Inbound Rules API
  phrasing_intents:
  - id: InboundRulesController_findAll
    intent: List inbound rules
    question: Which inbound email rules are set up to turn messages into leads?
  - id: InboundRulesController_create
    intent: Create an inbound lead rule
    question: How do I automatically create a lead when an email matching certain keywords arrives?
  - id: InboundRulesController_listAutomationEvents
    intent: List inbound-rule automation events
    question: What have my inbound rules done recently?
  - id: InboundRulesController_findById
    intent: Get an inbound rule
    question: How is a specific inbound rule configured?
  - id: InboundRulesController_update
    intent: Update an inbound rule
    question: Can I change the keywords or target stage of an existing inbound rule?
  - id: InboundRulesController_delete
    intent: Delete an inbound rule
    question: Can I delete an inbound rule I no longer use?
  - id: InboundRulesController_reorder
    intent: Reorder inbound rules
    question: Can I change which inbound rule is evaluated first?
  - id: InboundRulesController_toggle
    intent: Turn an inbound rule on or off
    question: Can I temporarily disable an inbound rule without deleting it?
  phrasing_ops: 10
  slug: live-direct-marketing-online-inbound-rules-api
- baseURL: https://api.live-direct-marketing.online
  baseurl_source: declared
  description: The Jobs API from Live Direct Marketing — 1 operation(s) for jobs.
  name: Live Direct Marketing Jobs API
  phrasing_intents:
  - id: JobsController_getJob
    intent: Check any background job's status
    question: Is my background job done yet, whatever queue it ran on?
  phrasing_ops: 1
  slug: live-direct-marketing-online-jobs-api
- baseURL: https://api.live-direct-marketing.online
  baseurl_source: declared
  description: The Landing API from Live Direct Marketing — 1 operation(s) for landing.
  name: Live Direct Marketing Landing API
  phrasing_intents:
  - id: LandingController_apply
    intent: Submit a landing-page application form
    question: How do I submit the public application form from the landing page?
  phrasing_ops: 1
  slug: live-direct-marketing-online-landing-api
- baseURL: https://api.live-direct-marketing.online
  baseurl_source: declared
  description: The Leads API from Live Direct Marketing — 21 operation(s) for leads.
  name: Live Direct Marketing Leads API
  phrasing_intents:
  - id: LeadsController_findAll
    intent: List leads
    question: Which leads are in a given pipeline stage?
  - id: LeadsController_create
    intent: Create a lead
    question: How do I add a new sales lead?
  - id: LeadsController_getStats
    intent: Get lead statistics
    question: How many leads do I have overall?
  - id: LeadsController_kanban
    intent: Show a pipeline's kanban board
    question: What does the kanban board look like for one of my pipelines?
  - id: LeadsController_kanbanStageMore
    intent: Load more leads in one kanban column
    question: How do I load the next batch of leads in a single board column?
  - id: LeadsController_stages
    intent: List a pipeline's stages for lead filtering
    question: Which stages can I filter leads by in a given pipeline?
  - id: LeadsController_findDuplicates
    intent: Find duplicate leads across the workspace
    question: Do I have duplicate leads anywhere in my workspace?
  - id: LeadsController_findById
    intent: Get a lead
    question: What are the details of a specific lead?
  phrasing_ops: 27
  slug: live-direct-marketing-online-leads-api
- baseURL: https://api.live-direct-marketing.online
  baseurl_source: declared
  description: The Legal API from Live Direct Marketing — 8 operation(s) for legal.
  name: Live Direct Marketing Legal API
  phrasing_intents:
  - id: LegalController_getTerms
    intent: Read the current terms of service
    question: What do the current terms of service say?
  - id: LegalController_updateTerms
    intent: Edit the terms of service text
    question: How does a super admin change the terms of service wording?
  - id: LegalController_listDocuments
    intent: List the public legal documents
    question: Which legal documents are published, like privacy policy or acceptable use?
  - id: LegalController_getDocument
    intent: Read one legal document
    question: Can I read the privacy policy or the DPA?
  - id: LegalController_publishVersion
    intent: Publish a new version of a legal document
    question: How do I publish a new version of the privacy policy?
  - id: LegalController_listVersions
    intent: List versions of a legal document
    question: What earlier versions of a legal document exist?
  - id: LegalController_recordAcceptance
    intent: Record my acceptance of a legal document
    question: How do I record that I accepted a specific legal document?
  - id: LegalController_listAcceptances
    intent: Search the legal acceptance registry
    question: Who accepted which version of a legal document, and when?
  phrasing_ops: 10
  slug: live-direct-marketing-online-legal-api
- baseURL: https://api.live-direct-marketing.online
  baseurl_source: declared
  description: The LinkedIn / Extension API API from Live Direct Marketing — 6 operation(s) for linkedin / extension api.
  name: Live Direct Marketing LinkedIn / Extension API
  phrasing_intents:
  - id: LinkedinExtApiController_session
    intent: Upload LinkedIn session cookies from the extension
    question: How does the browser extension hand over an authorized LinkedIn session?
  - id: LinkedinExtApiController_next
    intent: Claim the next due LinkedIn action
    question: What LinkedIn action should the extension perform next?
  - id: LinkedinExtApiController_report
    intent: Report the outcome of a LinkedIn action
    question: How does the extension report whether a LinkedIn action succeeded?
  - id: LinkedinExtApiController_events
    intent: Send LinkedIn widget events
    question: How are accepted invites and replies on LinkedIn sent back to the platform?
  - id: LinkedinExtApiController_config
    intent: Get LinkedIn extension config and guard-rails
    question: Which toggles and safety limits apply to the LinkedIn extension?
  - id: LinkedinExtApiController_heartbeat
    intent: Send a LinkedIn extension heartbeat
    question: How does the LinkedIn widget show it is still alive?
  phrasing_ops: 6
  slug: live-direct-marketing-online-linkedin-extension-api-api
- baseURL: https://api.live-direct-marketing.online
  baseurl_source: declared
  description: The Mail Agent API from Live Direct Marketing — 7 operation(s) for mail agent.
  name: Live Direct Marketing Mail Agent API
  phrasing_intents:
  - id: MailAgentController_getStatus
    intent: Check the mail agent connection
    question: Is my mail agent connected and sending right now?
  - id: MailAgentController_getSettings
    intent: View mail agent settings
    question: What are my current mail agent settings?
  - id: MailAgentController_toggleEnabled
    intent: Turn the mail agent on or off
    question: How do I enable or disable the mail agent?
  - id: MailAgentController_regenerateToken
    intent: Regenerate the mail agent token
    question: Can I issue a new auth token for the mail agent?
  - id: MailAgentController_resetStats
    intent: Reset mail agent statistics
    question: Can I zero out the mail agent's sending counters?
  - id: MailAgentController_disconnect
    intent: Disconnect the mail agent
    question: How do I disconnect the mail agent session from my account?
  - id: MailAgentController_downloadWindows
    intent: Download the Windows mail agent
    question: Where do I download the mail agent for Windows?
  - id: MailAgentController_getQr
    intent: Get the Android mail agent pairing QR
    question: How do I pair the Android mail agent with my account?
  phrasing_ops: 8
  slug: live-direct-marketing-online-mail-agent-api
- baseURL: https://api.live-direct-marketing.online
  baseurl_source: declared
  description: The Mail Agent / Update API from Live Direct Marketing — 1 operation(s) for mail agent / update.
  name: Live Direct Marketing Mail Agent / Update API
  phrasing_intents:
  - id: MailAgentUpdateController_check
    intent: Check for a newer mail agent version
    question: Is there a newer version of the desktop mail agent available?
  phrasing_ops: 1
  slug: live-direct-marketing-online-mail-agent-update-api
- baseURL: https://api.live-direct-marketing.online
  baseurl_source: declared
  description: The Mail Routing Rules API from Live Direct Marketing — 4 operation(s) for mail routing rules.
  name: Live Direct Marketing Mail Routing Rules API
  phrasing_intents:
  - id: MailRoutingController_findAll
    intent: List all mail routing rules
    question: What mail routing rules do I have set up for incoming email?
  - id: MailRoutingController_create
    intent: Create a mail routing rule
    question: How do I automatically move emails from a certain domain into a folder?
  - id: MailRoutingController_findById
    intent: Get a mail routing rule
    question: What conditions and action does a specific routing rule have?
  - id: MailRoutingController_update
    intent: Update a mail routing rule
    question: How do I change the target folder of an existing routing rule?
  - id: MailRoutingController_delete
    intent: Delete a mail routing rule
    question: How do I permanently remove a mail routing rule I no longer need?
  - id: MailRoutingController_toggle
    intent: Turn a mail routing rule on or off
    question: How do I temporarily pause a routing rule without deleting it?
  - id: MailRoutingController_testRules
    intent: Dry-run an email against routing rules
    question: Which of my active routing rules would catch a given email?
  phrasing_ops: 7
  slug: live-direct-marketing-online-mail-routing-rules-api
- baseURL: https://api.live-direct-marketing.online
  baseurl_source: declared
  description: The Mail Transport API from Live Direct Marketing — 1 operation(s) for mail transport.
  name: Live Direct Marketing Mail Transport API
  phrasing_intents:
  - id: MailTransportController_stats
    intent: Break down sent mail by transport
    question: Which mail transports are actually being used to send?
  phrasing_ops: 1
  slug: live-direct-marketing-online-mail-transport-api
- baseURL: https://api.live-direct-marketing.online
  baseurl_source: declared
  description: The Mailing API from Live Direct Marketing — 39 operation(s) for mailing.
  name: Live Direct Marketing Mailing API
  phrasing_intents:
  - id: MailingController_getOverview
    intent: Get an overview of all mailing campaigns
    question: Where can I see every mailing campaign at once on an admin dashboard?
  - id: MailingController_getBounceOverview
    intent: Get global bounce statistics
    question: What are my bounce rates across all mailings, split into hard and soft bounces?
  - id: MailingController_getWarmupOverview
    intent: List email accounts in warmup
    question: Which of my email accounts are currently warming up?
  - id: MailingController_getPendingApprovals
    intent: List campaigns awaiting approval
    question: Which mailing campaigns are waiting for admin approval?
  - id: MailingController_approveCampaign
    intent: Approve a pending mailing campaign
    question: How do I approve a mailing campaign that is waiting for review?
  - id: MailingController_rejectCampaign
    intent: Reject a pending mailing campaign
    question: Can an admin turn down a mailing campaign submitted for approval?
  - id: MailingController_getCreativePreview
    intent: Preview a creative for approval
    question: Can I see what a campaign's email creative looks like before approving it?
  - id: MailingController_getConfig
    intent: Get a campaign's mailing configuration
    question: Where can I check how a mailing campaign is configured?
  phrasing_ops: 41
  slug: live-direct-marketing-online-mailing-api
- baseURL: https://api.live-direct-marketing.online
  baseurl_source: declared
  description: The Marking API from Live Direct Marketing — 5 operation(s) for marking.
  name: Live Direct Marketing Marking API
  phrasing_intents:
  - id: MarkingController_listPatterns
    intent: List message marking patterns
    question: Which patterns are used to auto-mark incoming replies?
  - id: MarkingController_createPattern
    intent: Create a marking pattern
    question: How do I add a new rule for automatically marking replies?
  - id: MarkingController_togglePattern
    intent: Enable or disable a marking pattern
    question: Can I switch off a marking pattern without deleting it?
  - id: MarkingController_deletePattern
    intent: Delete a marking pattern
    question: How do I permanently remove a marking pattern?
  - id: MarkingController_classify
    intent: Classify a message text against marking patterns
    question: Which marking pattern would a given message text match?
  - id: MarkingController_classifyDialog
    intent: Classify a dialog against marking patterns
    question: How would an existing conversation be marked by my patterns?
  phrasing_ops: 6
  slug: live-direct-marketing-online-marking-api
- baseURL: https://api.live-direct-marketing.online
  baseurl_source: declared
  description: The mcp-transport API from Live Direct Marketing — 2 operation(s) for mcp-transport.
  name: Live Direct Marketing MCP Transport API
  phrasing_intents:
  - id: McpController_handle_get
    intent: Open the MCP stream at the root endpoint
    question: Can my MCP client open a server-sent event stream with a GET on the root /api/mcp endpoint?
  - id: McpController_handle_post
    intent: Post a JSON-RPC message to the MCP root
    question: How do I send MCP JSON-RPC messages like initialize or tools/call to the root endpoint?
  - id: McpController_handle_put
    intent: Send a PUT to the root MCP endpoint
    question: Does the root /api/mcp endpoint accept PUT requests?
  - id: McpController_handle_delete
    intent: End an MCP session at the root endpoint
    question: How do I terminate my MCP session on the root endpoint when I'm done?
  - id: McpController_handle_patch
    intent: Send a PATCH to the root MCP endpoint
    question: Is PATCH routed to the same handler on the root /api/mcp endpoint?
  - id: McpController_handle_options
    intent: Run a CORS preflight on the MCP root
    question: Will a browser-based MCP client pass the CORS preflight on /api/mcp?
  - id: McpController_handle_head
    intent: Check the root MCP endpoint with HEAD
    question: Can I probe whether the root MCP endpoint is reachable without a body?
  - id: getApiMcpByPath
    intent: Open the MCP stream on a sub-path
    question: Can my MCP client open its event stream with a GET on a path under /api/mcp/?
  phrasing_ops: 14
  slug: live-direct-marketing-online-mcp-transport-api
- baseURL: https://api.live-direct-marketing.online
  baseurl_source: declared
  description: The monitoring API from Live Direct Marketing — 16 operation(s) for monitoring.
  name: Live Direct Marketing Monitoring API
  phrasing_intents:
  - id: MonitoringController_list
    intent: List monitored domains in my account
    question: Which domains am I monitoring from my account dashboard?
  - id: MonitoringController_add
    intent: Add a domain to account monitoring
    question: How do I start monitoring a domain from my account dashboard?
  - id: MonitoringController_updateDomain
    intent: Change checks or interval for a monitored domain
    question: Can I change how often a monitored domain gets checked?
  - id: MonitoringController_remove
    intent: Remove a domain from account monitoring
    question: Can I stop watching a domain from my account dashboard?
  - id: MonitoringController_pause
    intent: Pause account monitoring for a domain
    question: Can I temporarily pause checks on a domain in my account dashboard?
  - id: MonitoringController_resume
    intent: Resume account monitoring for a domain
    question: How do I restart checks on a paused domain in my account?
  - id: MonitoringController_run
    intent: Run a domain check now from my account
    question: Can I trigger a domain check right now from my account dashboard?
  - id: MonitoringController_history
    intent: Get a domain's check history in my account
    question: What past check results does my account hold for a monitored domain?
  phrasing_ops: 21
  slug: live-direct-marketing-online-monitoring-api
- baseURL: https://api.live-direct-marketing.online
  baseurl_source: declared
  description: The monitoring-enrollment API from Live Direct Marketing — 1 operation(s) for monitoring-enrollment.
  name: Live Direct Marketing Monitoring Enrollment API
  phrasing_intents:
  - id: MonitoringEnrollmentController_enroll
    intent: Enroll in monitoring
    question: How do I sign up for monitoring?
  phrasing_ops: 1
  slug: live-direct-marketing-online-monitoring-enrollment-api
- baseURL: https://api.live-direct-marketing.online
  baseurl_source: declared
  description: The Nalog ID API from Live Direct Marketing — 2 operation(s) for nalog id.
  name: Live Direct Marketing Nalog ID API
  phrasing_intents:
  - id: NalogIdController_lookup
    intent: Look up Russian tax registry data for a company
    question: Can I find a Russian company's tax registration details from what I know about it?
  - id: NalogIdController_test
    intent: Debug a Nalog lookup with query parameters
    question: Is there a test endpoint to try a Nalog company search with a city and domain?
  phrasing_ops: 2
  slug: live-direct-marketing-online-nalog-id-api
- baseURL: https://api.live-direct-marketing.online
  baseurl_source: declared
  description: The Names API from Live Direct Marketing — 2 operation(s) for names.
  name: Live Direct Marketing Names API
  phrasing_intents:
  - id: NamesController_decline
    intent: Decline a Russian full name by case
    question: Can I get a Russian full name in the dative or genitive case for an email greeting?
  - id: NamesController_ping
    intent: Check the names service health
    question: Is the name declension service up?
  phrasing_ops: 2
  slug: live-direct-marketing-online-names-api
- baseURL: https://api.live-direct-marketing.online
  baseurl_source: declared
  description: The Notifications API from Live Direct Marketing — 10 operation(s) for notifications.
  name: Live Direct Marketing Notifications API
  phrasing_intents:
  - id: NotificationsController_pushPublicKey
    intent: Get the Web Push VAPID public key
    question: What VAPID public key do I need to subscribe a browser to push notifications?
  - id: NotificationsController_pushSubscribe
    intent: Register a browser for push notifications
    question: How do I turn on browser push notifications for my account?
  - id: NotificationsController_pushUnsubscribe
    intent: Remove a browser push subscription
    question: How do I stop push notifications in a browser?
  - id: NotificationsController_findAll
    intent: List my notifications
    question: What notifications do I have?
  - id: NotificationsController_unreadCount
    intent: Get my unread notification count
    question: How many unread notifications do I have?
  - id: NotificationsController_readAll
    intent: Mark all notifications as read
    question: Can I clear every unread notification at once?
  - id: NotificationsController_markRead
    intent: Mark one notification as read
    question: How do I mark a single notification as read?
  - id: NotificationsController_dismiss
    intent: Dismiss one notification
    question: Can I hide one notification from the widget?
  phrasing_ops: 10
  slug: live-direct-marketing-online-notifications-api
- baseURL: https://api.live-direct-marketing.online
  baseurl_source: declared
  description: The oauth API from Live Direct Marketing — 10 operation(s) for oauth.
  name: Live Direct Marketing OAuth API
  phrasing_intents:
  - id: OAuthController_authorizePage
    intent: Open the OAuth authorization page
    question: How does a third-party app start the OAuth authorization flow?
  - id: OAuthController_authorizeSubmit
    intent: Sign in and grant an OAuth client access
    question: What happens when a user submits their login on the OAuth consent form?
  - id: OAuthController_token
    intent: Exchange a code or refresh token for an access token
    question: How does my app exchange an authorization code for an access token?
  - id: OAuthController_me
    intent: Get the user behind an OAuth token
    question: Which user does my OAuth access token belong to?
  - id: OAuthController_connectPage
    intent: Open the public mailbox connect page
    question: Is there a public page for connecting mailboxes through the anti-detect browser flow?
  - id: OAuthController_connectRedirect
    intent: Redirect to OAuth consent for one mailbox
    question: Can I send someone straight to the consent screen for one specific mailbox?
  - id: OAuthController_getAuthUrl
    intent: Get the OAuth consent URL for a mailbox
    question: Where do I get the consent URL to connect a mailbox with OAuth?
  - id: OAuthController_callback
    intent: Handle the mail provider's OAuth callback
    question: Which endpoint does the mail provider redirect back to after consent?
  phrasing_ops: 11
  slug: live-direct-marketing-online-oauth-api
- baseURL: https://api.live-direct-marketing.online
  baseurl_source: declared
  description: The oauth-tests API from Live Direct Marketing — 2 operation(s) for oauth-tests.
  name: Live Direct Marketing OAUTH Tests API
  phrasing_intents:
  - id: V1OAuthTestsController_list
    intent: List my completed deliverability tests
    question: Which deliverability tests have I finished, newest first?
  - id: V1OAuthTestsController_create
    intent: Start a deliverability test
    question: How do I start an inbox placement test for an email I'm about to send?
  - id: V1OAuthTestsController_get
    intent: Get one deliverability test result
    question: Where did my test email land for each mailbox provider?
  phrasing_ops: 3
  slug: live-direct-marketing-online-oauth-tests-api
- baseURL: https://api.live-direct-marketing.online
  baseurl_source: declared
  description: The Observability / API Monitor API from Live Direct Marketing — 6 operation(s) for observability / api monitor.
  name: Live Direct Marketing Observability / API Monitor API
  phrasing_intents:
  - id: ApiMonitorController_list
    intent: Browse the platform API request log
    question: Which API requests failed with server errors across all tenants yesterday?
  - id: ApiMonitorController_aggregates
    intent: Get API traffic and latency aggregates
    question: What is the platform's requests per second and latency percentiles right now?
  - id: ApiMonitorController_mcpTools
    intent: Break down MCP tool usage
    question: Which MCP tools are called most and how often do they error?
  - id: ApiMonitorController_mcpKeys
    intent: Break down MCP usage per bearer key
    question: Which bearer keys are generating the most MCP traffic?
  - id: ApiMonitorController_mcpTimeseries
    intent: Chart MCP requests over time
    question: How has MCP request volume changed hour by hour?
  - id: ApiMonitorSelfController_calls
    intent: Read my own API and MCP call journal
    question: What API and MCP calls has my own account made recently, and what did they cost?
  phrasing_ops: 6
  slug: live-direct-marketing-online-observability-api-monitor-api
- baseURL: https://api.live-direct-marketing.online
  baseurl_source: declared
  description: The Observability / API Tests API from Live Direct Marketing — 4 operation(s) for observability / api tests.
  name: Live Direct Marketing Observability / API Tests API
  phrasing_intents:
  - id: ApiTestsController_catalog
    intent: List synthetic API test suites
    question: Which synthetic API test suites are available?
  - id: ApiTestsController_run
    intent: Run a synthetic API test suite
    question: How does a super admin kick off a synthetic API test suite?
  - id: ApiTestsController_list
    intent: List recent API test runs
    question: Did the last synthetic API test runs pass?
  - id: ApiTestsController_get
    intent: Get one API test run
    question: Which checks failed in a specific synthetic test run?
  phrasing_ops: 4
  slug: live-direct-marketing-online-observability-api-tests-api
- baseURL: https://api.live-direct-marketing.online
  baseurl_source: declared
  description: The Phantom Browser API from Live Direct Marketing — 28 operation(s) for phantom browser.
  name: Live Direct Marketing Phantom Browser API
  phrasing_intents:
  - id: PhantomBrowserController_listProfiles
    intent: List Phantom browser profiles
    question: Which Phantom browser profiles do I have set up?
  - id: PhantomBrowserController_createProfile
    intent: Create a Phantom browser profile
    question: How do I add a new browser profile for the Phantom client?
  - id: PhantomBrowserController_syncProfiles
    intent: Resync profiles to the Phantom client
    question: My Phantom desktop client is missing profiles, can I push the list to it again?
  - id: PhantomBrowserController_getProfile
    intent: Get one Phantom browser profile
    question: What settings does a specific Phantom browser profile have?
  - id: PhantomBrowserController_updateProfile
    intent: Update a Phantom browser profile
    question: Can I edit the settings of an existing Phantom browser profile?
  - id: PhantomBrowserController_deleteProfile
    intent: Delete a Phantom browser profile
    question: How do I remove a Phantom browser profile I no longer use?
  - id: PhantomBrowserController_getClientStatus
    intent: Check Phantom desktop client connection
    question: Is my Phantom desktop client connected right now?
  - id: PhantomBrowserController_regenerateToken
    intent: Regenerate the Phantom client token
    question: How do I rotate the auth token my Phantom desktop client uses?
  phrasing_ops: 38
  slug: live-direct-marketing-online-phantom-browser-api
- baseURL: https://api.live-direct-marketing.online
  baseurl_source: declared
  description: The Phantom Browser / Download API from Live Direct Marketing — 5 operation(s) for phantom browser / download.
  name: Live Direct Marketing Phantom Browser / Download API
  phrasing_intents:
  - id: PhantomBrowserDownloadController_syncByToken
    intent: Sync Phantom desktop profiles with a token
    question: How does the Phantom desktop client sync its browser profiles?
  - id: PhantomBrowserDownloadController_updateCheck
    intent: Check for a Phantom client update
    question: Is there a newer version of the Phantom client available?
  - id: PhantomBrowserDownloadController_updateBundle
    intent: Download the Phantom update bundle
    question: Where do I get the gzipped update bundle for the Phantom client?
  - id: PhantomBrowserDownloadController_download
    intent: Download the Phantom client installer
    question: How do I download the Phantom browser for my operating system?
  - id: PhantomBrowserDownloadController_receiveLogs
    intent: Upload logs from the Phantom client
    question: How does the Phantom desktop client report its logs?
  phrasing_ops: 5
  slug: live-direct-marketing-online-phantom-browser-download-api
- baseURL: https://api.live-direct-marketing.online
  baseurl_source: declared
  description: The Pipeline Events API from Live Direct Marketing — 9 operation(s) for pipeline events.
  name: Live Direct Marketing Pipeline Events API
  phrasing_intents:
  - id: PipelineController_events
    intent: Ingest a conveyor event from the orchestrator
    question: How does the orchestrator report task and step progress to the conveyor?
  - id: PipelineController_getSummary
    intent: Summarise conveyor tasks by status
    question: How many conveyor tasks are in each status right now?
  - id: PipelineController_getSpeed
    intent: Get conveyor lead time and throughput
    question: What's the 7-day and 30-day lead time for conveyor tasks?
  - id: PipelineController_getStageTasks
    intent: List tasks in one conveyor stage
    question: Which tasks are sitting longest in a particular conveyor stage?
  - id: PipelineController_listTasks
    intent: List conveyor tasks
    question: Which conveyor tasks are currently in progress?
  - id: PipelineController_getTask
    intent: Get a conveyor task with its steps
    question: What steps has a particular conveyor task gone through?
  - id: PipelineController_getStageTimeline
    intent: Show a task's per-stage timeline
    question: How long did one task spend in each stage from queued to prod?
  - id: PipelineController_getStepLogs
    intent: Read a conveyor step's logs
    question: What did a particular conveyor step log while it ran?
  phrasing_ops: 9
  slug: live-direct-marketing-online-pipeline-events-api
- baseURL: https://api.live-direct-marketing.online
  baseurl_source: declared
  description: The Pipelines API from Live Direct Marketing — 11 operation(s) for pipelines.
  name: Live Direct Marketing Pipelines API
  phrasing_intents:
  - id: PipelinesController_findAll
    intent: List sales pipelines
    question: Which sales pipelines are set up in my workspace?
  - id: PipelinesController_create
    intent: Create a sales pipeline
    question: How do I set up a new sales pipeline?
  - id: PipelinesController_getAllAutomationLogs
    intent: View automation logs across all pipelines
    question: What have stage automations done across all my pipelines recently?
  - id: PipelinesController_findById
    intent: Get a pipeline
    question: How is a particular pipeline configured?
  - id: PipelinesController_update
    intent: Update a pipeline's settings
    question: How do I rename a pipeline or change its currency?
  - id: PipelinesController_remove
    intent: Delete a pipeline
    question: How do I remove a pipeline I no longer use?
  - id: PipelinesController_createStage
    intent: Add a stage to a pipeline
    question: How do I add a new stage to a sales pipeline?
  - id: PipelinesController_reorderStages
    intent: Reorder a pipeline's stages
    question: How do I change the order of stages in a pipeline?
  phrasing_ops: 17
  slug: live-direct-marketing-online-pipelines-api
- baseURL: https://api.live-direct-marketing.online
  baseurl_source: declared
  description: The presend API from Live Direct Marketing — 2 operation(s) for presend.
  name: Live Direct Marketing Presend API
  phrasing_intents:
  - id: PresendController_create
    intent: Submit an email for pre-send checks
    question: Can I check my email for spam problems before I send it?
  - id: PresendController_get
    intent: Get pre-send check results
    question: Is my pre-send analysis done, and what did it find?
  - id: PresendController_delete
    intent: Delete a pre-send check
    question: Can I delete a pre-send check and its email content?
  phrasing_ops: 3
  slug: live-direct-marketing-online-presend-api
- baseURL: https://api.live-direct-marketing.online
  baseurl_source: declared
  description: The PresendAdmin API from Live Direct Marketing — 1 operation(s) for presendadmin.
  name: Live Direct Marketing Presend Admin API
  phrasing_intents:
  - id: PresendAdminController_stats
    intent: Get pre-send check statistics
    question: What do the admin pre-send statistics look like recently?
  phrasing_ops: 1
  slug: live-direct-marketing-online-presendadmin-api
- baseURL: https://api.live-direct-marketing.online
  baseurl_source: declared
  description: The Profi Orders API from Live Direct Marketing — 3 operation(s) for profi orders.
  name: Live Direct Marketing Profi Orders API
  phrasing_intents:
  - id: ProfiOrdersController_list
    intent: Browse the Profi.ru order feed
    question: What new Profi.ru orders match my keyword?
  - id: ProfiOrdersController_status
    intent: Check the Profi.ru monitor status
    question: When did the Profi.ru monitor last ingest orders?
  - id: ProfiOrdersController_ingest
    intent: Push orders from the Profi.ru monitor
    question: How does the external monitor send scraped Profi.ru orders in?
  phrasing_ops: 3
  slug: live-direct-marketing-online-profi-orders-api
- baseURL: https://api.live-direct-marketing.online
  baseurl_source: declared
  description: The Project Templates API from Live Direct Marketing — 10 operation(s) for project templates.
  name: Live Direct Marketing Project Templates API
  phrasing_intents:
  - id: ProjectTemplatesController_findRun
    intent: Get a project run with steps and totals
    question: How is one of my project runs going, step by step?
  - id: ProjectTemplatesController_updateRun
    intent: Update a project run's name, status or notes
    question: Can I mark a project run as a test or change its status?
  - id: ProjectTemplatesController_removeRun
    intent: Delete a project run
    question: Can I delete a project run I started by mistake?
  - id: ProjectTemplatesController_updateRunStep
    intent: Record facts and issues on a run step
    question: How do I log the actual result for a step in a project run?
  - id: ProjectTemplatesController_findAll
    intent: List project templates
    question: What project templates do I have?
  - id: ProjectTemplatesController_create
    intent: Create a project template
    question: How do I create a reusable project template?
  - id: ProjectTemplatesController_findOne
    intent: Get a project template with steps and runs
    question: What steps and past runs belong to a template?
  - id: ProjectTemplatesController_update
    intent: Update or archive a project template
    question: Can I archive a template instead of deleting it?
  phrasing_ops: 16
  slug: live-direct-marketing-online-project-templates-api
- baseURL: https://api.live-direct-marketing.online
  baseurl_source: declared
  description: The Prompt Templates API from Live Direct Marketing — 3 operation(s) for prompt templates.
  name: Live Direct Marketing Prompt Templates API
  phrasing_intents:
  - id: PromptTemplatesController_list
    intent: List prompt templates
    question: Which AI prompt templates do I have, and which are active?
  - id: PromptTemplatesController_create
    intent: Create a prompt template
    question: How do I save a new reusable AI prompt template?
  - id: PromptTemplatesController_get
    intent: Get a prompt template
    question: Can I view the text of one prompt template?
  - id: PromptTemplatesController_update
    intent: Update a prompt template
    question: How do I edit an existing prompt template?
  - id: PromptTemplatesController_delete
    intent: Delete a prompt template
    question: Can I delete a prompt template I no longer use?
  - id: PromptTemplatesController_render
    intent: Render a prompt template with variables
    question: Can I fill in a prompt template's variables to see the final prompt?
  phrasing_ops: 6
  slug: live-direct-marketing-online-prompt-templates-api
- baseURL: https://api.live-direct-marketing.online
  baseurl_source: declared
  description: The Provider Config API from Live Direct Marketing — 6 operation(s) for provider config.
  name: Live Direct Marketing Provider Config API
  phrasing_intents:
  - id: ProviderConfigController_list
    intent: List email provider configurations
    question: Which mailbox provider settings are configured?
  - id: ProviderConfigController_resolve
    intent: Find the email provider for an address
    question: Which mail provider handles a given email address's domain?
  - id: ProviderConfigController_getOne
    intent: Get one email provider configuration
    question: What settings are stored for a particular mail provider?
  - id: ProviderConfigController_upsert
    intent: Create or update a provider configuration
    question: How do I add or change settings for a mail provider?
  - id: ProviderConfigController_remove
    intent: Delete a provider configuration
    question: Can I remove a mail provider configuration entirely?
  - id: ProviderConfigController_toggle
    intent: Enable or disable a provider configuration
    question: Can I switch a mail provider configuration off without deleting it?
  - id: ProviderConfigController_addDomain
    intent: Map a domain to a provider configuration
    question: Can I tell the system that a custom email domain is hosted by a certain provider?
  - id: ProviderConfigController_removeDomain
    intent: Remove a domain mapping from a provider
    question: Can I unmap a domain pattern from a mail provider?
  phrasing_ops: 8
  slug: live-direct-marketing-online-provider-config-api
- baseURL: https://api.live-direct-marketing.online
  baseurl_source: declared
  description: The providers API from Live Direct Marketing — 2 operation(s) for providers.
  name: Live Direct Marketing Providers API
  phrasing_intents:
  - id: ProvidersPublicController_list
    intent: List providers (public, unversioned)
    question: Is there a public unversioned list of providers I can read without the v1 API?
  - id: V1ProvidersController_list
    intent: List deliverability providers my key can use
    question: Which deliverability providers can my API key use, and why are some unavailable?
  phrasing_ops: 2
  slug: live-direct-marketing-online-providers-api
- baseURL: https://api.live-direct-marketing.online
  baseurl_source: declared
  description: The Public API from Live Direct Marketing — 1 operation(s) for public.
  name: Live Direct Marketing Public API
  phrasing_intents:
  - id: PublicPricingController_pricing
    intent: Get public platform pricing
    question: How much does an inbox placement test cost on Live Direct Marketing Online?
  phrasing_ops: 1
  slug: live-direct-marketing-online-public-api
- baseURL: https://api.live-direct-marketing.online
  baseurl_source: declared
  description: The recheck API from Live Direct Marketing — 2 operation(s) for recheck.
  name: Live Direct Marketing Recheck API
  phrasing_intents:
  - id: RecheckController_schedule
    intent: Schedule an inbox placement recheck
    question: Can I ask for my deliverability test to be checked again?
  - id: RecheckController_schedule24h
    intent: Schedule a 24-hour placement recheck
    question: Can I rescan the same test message a day later without sending a new one?
  - id: RecheckController_status24h
    intent: Get the 24-hour placement recheck results
    question: Did my email's inbox placement change after 24 hours?
  - id: RecheckController_cancel24h
    intent: Cancel a scheduled 24-hour recheck
    question: How do I call off the next-day recheck I scheduled?
  phrasing_ops: 4
  slug: live-direct-marketing-online-recheck-api
- baseURL: https://api.live-direct-marketing.online
  baseurl_source: declared
  description: The reports API from Live Direct Marketing — 11 operation(s) for reports.
  name: Live Direct Marketing Reports API
  phrasing_intents:
  - id: ReportsController_getReport
    intent: Open a published report by its public token
    question: What does someone see when they open a public report link?
  - id: ReportsController_getReportPdf
    intent: Get a public report as a PDF
    question: Can I get a shared report as a PDF file?
  - id: ReportsController_list
    intent: List reports and storage quota
    question: Which reports have been saved in my workspace?
  - id: ReportsController_create
    intent: Create a report from base64 content
    question: How can an agent save a file as a report without a multipart upload?
  - id: ReportsController_limits
    intent: Check report storage limits and usage
    question: How much report storage have I used so far?
  - id: ReportsController_upload
    intent: Upload a report file
    question: Can I upload a spreadsheet or PDF as a report from my computer?
  - id: ReportsController_fromExport
    intent: Save a finished export as a report
    question: Can a completed export be kept as a report?
  - id: ReportsController_getOne
    intent: Get one report
    question: Can I view the details of one of my saved reports?
  phrasing_ops: 14
  slug: live-direct-marketing-online-reports-api
- baseURL: https://api.live-direct-marketing.online
  baseurl_source: declared
  description: The RPA API from Live Direct Marketing — 7 operation(s) for rpa.
  name: Live Direct Marketing RPA API
  phrasing_intents:
  - id: RpaController_poll
    intent: Poll for RPA work on the legacy queue
    question: How does a legacy RPA bot find queued jobs or unprocessed contacts?
  - id: RpaController_jobStatus
    intent: Check a legacy RPA job's status
    question: Is my RPA job ready yet?
  - id: RpaController_jobReport
    intent: Report a legacy RPA send job result
    question: How does a legacy RPA bot report the result of a send job?
  - id: RpaController_systemReport
    intent: Report a process-level RPA error
    question: Can an RPA bot report an error that isn't tied to any job?
  - id: RpaController_systemStatus
    intent: Get RPA system health
    question: Is the RPA system healthy, or are mailings paused?
  - id: RpaController_taskStatus
    intent: Get a legacy RPA mailing's status
    question: How many items in a legacy RPA mailing have been processed?
  - id: RpaController_report
    intent: Submit a legacy batch RPA report
    question: How does a legacy RPA bot submit a batch of item send results?
  phrasing_ops: 7
  slug: live-direct-marketing-online-rpa-api
- baseURL: https://api.live-direct-marketing.online
  baseurl_source: declared
  description: The RPA service protocol API from Live Direct Marketing — 16 operation(s) for rpa service protocol.
  name: Live Direct Marketing RPA service protocol API
  phrasing_intents:
  - id: RpaOutboxController_queueReadiness
    intent: Read RPA queue and campaign readiness
    question: Can an RPA worker see what's queued without claiming any task?
  - id: RpaOutboxController_heartbeat
    intent: Send an RPA worker heartbeat
    question: How does an RPA worker signal it is still alive?
  - id: RpaOutboxController_claim
    intent: Claim the next RPA send task
    question: How does an RPA worker pick up its next email send task?
  - id: RpaOutboxController_start
    intent: Start a claimed RPA send operation
    question: How does a worker confirm the send gates still pass before sending a claimed task?
  - id: RpaOutboxController_current
    intent: Re-read the current RPA task and lease
    question: After a control report, how does a worker re-read its current task without a second claim?
  - id: RpaOutboxController_renew
    intent: Renew an RPA task lease
    question: How do I extend a live RPA task lease by another hour?
  - id: RpaOutboxController_refresh
    intent: Refresh attachment links for an RPA task
    question: My attachment links on an RPA task expired — can I refresh them?
  - id: RpaOutboxController_report
    intent: Report the outcome of an RPA send
    question: How does a worker report that a CONTROL or REAL send went through?
  phrasing_ops: 16
  slug: live-direct-marketing-online-rpa-service-protocol-api
- baseURL: https://api.live-direct-marketing.online
  baseurl_source: declared
  description: The Rules / Creative API from Live Direct Marketing — 4 operation(s) for rules / creative.
  name: Live Direct Marketing Rules / Creative API
  phrasing_intents:
  - id: CreativeRulesController_get
    intent: Get a creative's rules document
    question: What rules are set on a particular email creative?
  - id: CreativeRulesController_patch
    intent: Change a creative's rules
    question: Can I edit just part of a creative's rules without replacing them all?
  - id: CreativeRulesController_getSchema
    intent: Get the JSON Schema for creative rules
    question: What fields are allowed in a creative rules document?
  - id: CreativeRulesController_context
    intent: Get context used to evaluate creative rules
    question: What supporting data is used when a creative's rules are evaluated?
  - id: CreativeRulesController_history
    intent: Get the change history of creative rules
    question: Who changed a creative's rules and when?
  phrasing_ops: 5
  slug: live-direct-marketing-online-rules-creative-api
- baseURL: https://api.live-direct-marketing.online
  baseurl_source: declared
  description: The Rules / Creative Bootstrap API from Live Direct Marketing — 2 operation(s) for rules / creative bootstrap.
  name: Live Direct Marketing Rules / Creative Bootstrap API
  phrasing_intents:
  - id: CreativeBootstrapController_bootstrap
    intent: Get a creative's bootstrap snapshot
    question: Can I load everything needed to render a creative's page in one call?
  - id: CreativeBootstrapController_updateMeta
    intent: Update a creative's meta fields
    question: How do I change a creative's non-rule meta fields?
  phrasing_ops: 2
  slug: live-direct-marketing-online-rules-creative-bootstrap-api
- baseURL: https://api.live-direct-marketing.online
  baseurl_source: declared
  description: The Rules / Discovery API from Live Direct Marketing — 2 operation(s) for rules / discovery.
  name: Live Direct Marketing Rules / Discovery API
  phrasing_intents:
  - id: DiscoveryController_discovery
    intent: Get the agent discovery document
    question: What resources and endpoints can an AI agent discover on this platform?
  - id: DiscoveryController_contract
    intent: Get the agent contract version
    question: Which version of the agent contract is the platform running?
  phrasing_ops: 2
  slug: live-direct-marketing-online-rules-discovery-api
- baseURL: https://api.live-direct-marketing.online
  baseurl_source: declared
  description: The Rules / Sub-resource API from Live Direct Marketing — 4 operation(s) for rules / sub-resource.
  name: Live Direct Marketing Rules / Sub-resource API
  phrasing_intents:
  - id: SubResourceRulesController_listSubResources
    intent: List a creative's autopilot rule sections
    question: Which autopilot rule sub-resources can I configure on a creative?
  - id: SubResourceRulesController_get
    intent: Get a creative's autopilot rules section
    question: What are the current autopilot rules in one section of a creative?
  - id: SubResourceRulesController_patch
    intent: Patch a creative's autopilot rules section
    question: Can I change just one section of a creative's autopilot rules?
  - id: SubResourceRulesController_getSchema
    intent: Get the JSON Schema for an autopilot rules section
    question: What shape must an autopilot rules section follow?
  - id: SubResourceRulesController_history
    intent: Get change history of an autopilot rules section
    question: Who changed a creative's autopilot rules, and when?
  phrasing_ops: 5
  slug: live-direct-marketing-online-rules-sub-resource-api
- baseURL: https://api.live-direct-marketing.online
  baseurl_source: declared
  description: The RUM API from Live Direct Marketing — 1 operation(s) for rum.
  name: Live Direct Marketing RUM API
  phrasing_intents:
  - id: RumController_vitals
    intent: Report Core Web Vitals from a browser
    question: How do I send Core Web Vitals measurements from a page anonymously?
  phrasing_ops: 1
  slug: live-direct-marketing-online-rum-api
- baseURL: https://api.live-direct-marketing.online
  baseurl_source: declared
  description: The Saved Views API from Live Direct Marketing — 2 operation(s) for saved views.
  name: Live Direct Marketing Saved Views API
  phrasing_intents:
  - id: SavedViewsController_findAll
    intent: List my saved views for a table
    question: Which saved views do I have for contacts or other tables?
  - id: SavedViewsController_create
    intent: Save a new view
    question: How do I save my current filters and columns as a view?
  - id: SavedViewsController_update
    intent: Update a saved view
    question: Can I rename a saved view or make it my default?
  - id: SavedViewsController_remove
    intent: Delete a saved view
    question: Can I delete a saved view I created?
  phrasing_ops: 4
  slug: live-direct-marketing-online-saved-views-api
- baseURL: https://api.live-direct-marketing.online
  baseurl_source: declared
  description: The screenshots API from Live Direct Marketing — 1 operation(s) for screenshots.
  name: Live Direct Marketing Screenshots API
  phrasing_intents:
  - id: ScreenshotOrdersController_track
    intent: Track a screenshot order
    question: How do I record a screenshot order?
  phrasing_ops: 1
  slug: live-direct-marketing-online-screenshots-api
- baseURL: https://api.live-direct-marketing.online
  baseurl_source: declared
  description: The Search API from Live Direct Marketing — 1 operation(s) for search.
  name: Live Direct Marketing Search API
  phrasing_intents:
  - id: SearchController_search
    intent: Search contacts, companies and leads
    question: Can I search across contacts, companies and leads with one query?
  phrasing_ops: 1
  slug: live-direct-marketing-online-search-api
- baseURL: https://api.live-direct-marketing.online
  baseurl_source: declared
  description: The SelfControl API from Live Direct Marketing — 2 operation(s) for selfcontrol.
  name: Live Direct Marketing Self Control API
  phrasing_intents:
  - id: SelfControlController_history
    intent: View self-control check history
    question: Where can admins see past self-control check runs?
  - id: SelfControlController_run
    intent: Run a self-control check
    question: How does an admin trigger a self-control check now?
  phrasing_ops: 2
  slug: live-direct-marketing-online-selfcontrol-api
- baseURL: https://api.live-direct-marketing.online
  baseurl_source: declared
  description: The sender-links API from Live Direct Marketing — 5 operation(s) for sender-links.
  name: Live Direct Marketing Sender Links API
  phrasing_intents:
  - id: SenderLinksController_unsubscribeGet
    intent: Unsubscribe from sender-link reports
    question: How do I stop getting sender-link email reports from the unsubscribe link?
  - id: SenderLinksController_unsubscribePost
    intent: One-click unsubscribe from sender reports
    question: Does one-click unsubscribe work for sender-link reports?
  - id: SenderLinksController_get
    intent: Open a public sender-link page
    question: What seed addresses should I add to my sends for a sender link?
  - id: SenderLinksController_revoke
    intent: Revoke a sender link
    question: Can I shut down a sender link so its page stops working?
  - id: SenderLinksController_setReports
    intent: Turn sender-link email reports on or off
    question: Can I enable email reports for a sender link?
  - id: SenderLinksController_reactivate
    intent: Reactivate a dormant sender link
    question: My sender link went dormant; can I wake it up?
  - id: getSenderLink
    intent: Get a permanent sender page via API
    question: Can I fetch a sender page's seeds, recent runs and report setting through the v1 API?
  phrasing_ops: 7
  slug: live-direct-marketing-online-sender-links-api
- baseURL: https://api.live-direct-marketing.online
  baseurl_source: declared
  description: The SEO Index API from Live Direct Marketing — 12 operation(s) for seo index.
  name: Live Direct Marketing SEO Index API
  phrasing_intents:
  - id: SeoIndexController_overview
    intent: Summarize Google search performance
    question: How are my site's search clicks and impressions trending over the last 28 days?
  - id: SeoIndexController_segments
    intent: Break down search metrics by site section
    question: Which sections of my site bring in the most search clicks?
  - id: SeoIndexController_sitemaps
    intent: Check Google sitemap status
    question: Are my sitemaps submitted and showing errors in Google Search Console?
  - id: SeoIndexController_pages
    intent: List top pages by search clicks
    question: Which pages on my site get the most clicks from search?
  - id: SeoIndexController_queries
    intent: List top Google search queries
    question: What search terms are people using to find my site on Google?
  - id: SeoIndexController_history
    intent: Chart daily search metrics
    question: Can I get a day-by-day series of clicks and impressions to chart?
  - id: SeoIndexController_coverage
    intent: Compare sitemap URLs to pages with impressions
    question: How many of my sitemap URLs actually show up in search impressions?
  - id: SeoIndexController_indexCoverage
    intent: Count sitemap pages per surface
    question: How many sitemap pages does each surface like landing, blog or check have?
  phrasing_ops: 13
  slug: live-direct-marketing-online-seo-index-api
- baseURL: https://api.live-direct-marketing.online
  baseurl_source: declared
  description: The Sequences API from Live Direct Marketing — 12 operation(s) for sequences.
  name: Live Direct Marketing Sequences API
  phrasing_intents:
  - id: SequencesController_list
    intent: List email sequences
    question: What email sequences do I have set up?
  - id: SequencesController_create
    intent: Create an email sequence
    question: How do I build a new multi-step email sequence?
  - id: SequencesController_get
    intent: Get an email sequence
    question: What steps and settings does one of my sequences have?
  - id: SequencesController_update
    intent: Update an email sequence
    question: Can I rename or change the status of an existing sequence?
  - id: SequencesController_delete
    intent: Delete an email sequence
    question: How do I permanently remove an email sequence?
  - id: SequencesController_addStep
    intent: Add a step to an email sequence
    question: How do I add another follow-up email to a sequence?
  - id: SequencesController_updateStep
    intent: Update a step in an email sequence
    question: How do I change the content or delay of one sequence step?
  - id: SequencesController_deleteStep
    intent: Delete a step from an email sequence
    question: Can I remove one follow-up email from a sequence?
  phrasing_ops: 18
  slug: live-direct-marketing-online-sequences-api
- baseURL: https://api.live-direct-marketing.online
  baseurl_source: declared
  description: The Settings API from Live Direct Marketing — 37 operation(s) for settings.
  name: Live Direct Marketing Settings API
  phrasing_intents:
  - id: SettingsController_getSettings
    intent: Get the full workspace settings document
    question: Where can I see every setting for my workspace in one response?
  - id: SettingsController_updateAiProviders
    intent: Update AI provider keys and defaults
    question: How do I change which AI provider my workspace uses by default?
  - id: SettingsController_requestLdmAi
    intent: Request LDM AI access or a balance increase
    question: How do I ask an admin to turn on LDM AI for my workspace?
  - id: SettingsController_updateNotifications
    intent: Update push and email notification preferences
    question: How do I turn email notifications on or off for my account?
  - id: SettingsController_updateWorkspace
    intent: Rename a workspace or change its currency and language
    question: How do I rename my workspace?
  - id: SettingsController_getProfile
    intent: Get the current user's profile
    question: What name is on my user profile right now?
  - id: SettingsController_updateProfile
    intent: Change the current user's name
    question: How do I change the first and last name on my profile?
  - id: SettingsController_getUiPreferences
    intent: Get my dashboard and menu layout preferences
    question: Which dashboard blocks and left-menu items have I configured?
  phrasing_ops: 55
  slug: live-direct-marketing-online-settings-api
- baseURL: https://api.live-direct-marketing.online
  baseurl_source: declared
  description: The Share Links API from Live Direct Marketing — 2 operation(s) for share links.
  name: Live Direct Marketing Share Links API
  phrasing_intents:
  - id: ShareLinksController_create
    intent: Create a share link for a record
    question: How do I create a link to share a record with someone outside?
  - id: ShareLinksController_findByEntity
    intent: List share links for a record
    question: Which share links exist for a particular record?
  - id: ShareLinksController_revoke
    intent: Revoke a share link
    question: Can I stop a share link from working?
  phrasing_ops: 3
  slug: live-direct-marketing-online-share-links-api
- baseURL: https://api.live-direct-marketing.online
  baseurl_source: declared
  description: The Share Public API from Live Direct Marketing — 3 operation(s) for share public.
  name: Live Direct Marketing Share Public API
  phrasing_intents:
  - id: SharePublicController_getOgHtml
    intent: Render link-preview meta tags for a share code
    question: What social preview HTML do crawlers see for a shared short link?
  - id: SharePublicController_getByShortCode
    intent: Open a shared item by short code
    question: Can someone without an account open a shared item from its short link?
  - id: SharePublicController_getShared
    intent: Open a shared item by legacy full token
    question: Do the old long share links with a full token still work?
  phrasing_ops: 3
  slug: live-direct-marketing-online-share-public-api
- baseURL: https://api.live-direct-marketing.online
  baseurl_source: declared
  description: The Site Enrichment API from Live Direct Marketing — 17 operation(s) for site enrichment.
  name: Live Direct Marketing Site Enrichment API
  phrasing_intents:
  - id: SiteEnrichmentController_detectFormsRoute
    intent: Detect contact forms in page HTML
    question: Can I check whether a web page has a contact-us form from its HTML?
  - id: SiteEnrichmentController_create
    intent: Start a website crawl to enrich companies
    question: How do I crawl my companies' websites to collect contact details?
  - id: SiteEnrichmentController_findAll
    intent: List site-crawl tasks
    question: Which website crawl tasks have I run, and which are still going?
  - id: SiteEnrichmentController_preview
    intent: Preview a list's crawl coverage
    question: Before crawling, how many companies in my list actually have a website filled in?
  - id: SiteEnrichmentController_findOne
    intent: Get a site-crawl task's status
    question: Is my website crawl finished yet?
  - id: SiteEnrichmentController_listEvents
    intent: Read a crawl task's event log
    question: Can I follow the state transitions of a crawl task as they happen?
  - id: SiteEnrichmentController_addAgentNote
    intent: Add an agent note to a crawl journal
    question: Can an agent leave a note in a crawl task's journal?
  - id: SiteEnrichmentController_reasonSummary
    intent: Summarize why crawl sites failed
    question: Why did sites fail in my crawl task, grouped by reason?
  phrasing_ops: 19
  slug: live-direct-marketing-online-site-enrichment-api
- baseURL: https://api.live-direct-marketing.online
  baseurl_source: declared
  description: The Stop List API from Live Direct Marketing — 9 operation(s) for stop list.
  name: Live Direct Marketing Stop List API
  phrasing_intents:
  - id: StopListController_list
    intent: List my stop list entries
    question: Which emails and domains are on my workspace's do-not-contact list?
  - id: StopListController_add
    intent: Add an entry to my stop list
    question: How do I stop emailing one particular address or domain?
  - id: StopListController_stats
    intent: Get my stop list statistics
    question: How many entries are on my own stop list?
  - id: StopListController_addBulk
    intent: Bulk-add entries to my stop list
    question: Can I upload many unsubscribed addresses to my stop list at once?
  - id: StopListController_remove
    intent: Remove an entry from my stop list
    question: Can I take someone off my do-not-contact list?
  - id: StopListController_check
    intent: Check emails against the stop list
    question: Are any of these addresses blocked before I send a campaign?
  - id: StopListController_globalList
    intent: List platform-wide stop list entries
    question: As a super admin, which entries are on the global stop list for every tenant?
  - id: StopListController_globalAdd
    intent: Add an entry to the global stop list
    question: How does a super admin block an address for all tenants?
  phrasing_ops: 11
  slug: live-direct-marketing-online-stop-list-api
- baseURL: https://api.live-direct-marketing.online
  baseurl_source: declared
  description: The subscriptions API from Live Direct Marketing — 3 operation(s) for subscriptions.
  name: Live Direct Marketing Subscriptions API
  phrasing_intents:
  - id: SubscriptionsController_subscribe
    intent: Subscribe to updates
    question: How do I sign up for email updates?
  - id: SubscriptionsController_verify
    intent: Confirm a subscription
    question: What does the confirmation link in a signup email do?
  - id: SubscriptionsController_unsubscribeGet
    intent: Unsubscribe via an email link
    question: What happens when someone clicks the unsubscribe link in an email?
  - id: SubscriptionsController_unsubscribePost
    intent: Unsubscribe with a one-click POST
    question: Is there a one-click POST unsubscribe that mail clients can call?
  phrasing_ops: 4
  slug: live-direct-marketing-online-subscriptions-api
- baseURL: https://api.live-direct-marketing.online
  baseurl_source: declared
  description: The SubscriptionsAdmin API from Live Direct Marketing — 2 operation(s) for subscriptionsadmin.
  name: Live Direct Marketing Subscriptions Admin API
  phrasing_intents:
  - id: SubscriptionsAdminController_list
    intent: List subscriptions as admin
    question: Which subscriptions exist across the platform?
  - id: SubscriptionsAdminController_stats
    intent: Get subscription statistics
    question: How many subscriptions are active overall?
  phrasing_ops: 2
  slug: live-direct-marketing-online-subscriptionsadmin-api
- baseURL: https://api.live-direct-marketing.online
  baseurl_source: declared
  description: The Support API from Live Direct Marketing — 6 operation(s) for support.
  name: Live Direct Marketing Support API
  phrasing_intents:
  - id: SupportController_getThread
    intent: Get my support thread
    question: Where can I read my conversation with support?
  - id: SupportController_unreadCount
    intent: Count unread support replies
    question: Do I have any unread replies from support?
  - id: SupportController_sendMessage
    intent: Send a message to support
    question: How do I contact support from inside the app?
  - id: SupportController_serveAttachment
    intent: Download a support attachment
    question: Can I open an image attached to my support thread?
  - id: SupportController_markRead
    intent: Mark support replies as read
    question: How do I clear the unread badge on support replies?
  - id: SupportController_setStatus
    intent: Close or reopen my support ticket
    question: Can I close my support ticket once my issue is solved?
  phrasing_ops: 6
  slug: live-direct-marketing-online-support-api
- baseURL: https://api.live-direct-marketing.online
  baseurl_source: declared
  description: The Suppression API from Live Direct Marketing — 6 operation(s) for suppression.
  name: Live Direct Marketing Suppression API
  phrasing_intents:
  - id: SuppressionController_list
    intent: List suppressed email addresses
    question: Which email addresses are on my do-not-send suppression list?
  - id: SuppressionController_add
    intent: Suppress a single email address
    question: How do I stop all sending to one specific email address?
  - id: SuppressionController_addBulk
    intent: Bulk-add emails to the suppression list
    question: Can I upload many email addresses to the suppression list in one request?
  - id: SuppressionController_check
    intent: Check emails against the suppression list
    question: Before a send, can I check which of these emails are suppressed?
  - id: SuppressionController_remove
    intent: Remove an email from the suppression list
    question: Can I take an email address off the suppression list so they can be emailed again?
  - id: SuppressionController_listDomains
    intent: List suppressed domains
    question: Which whole domains are blocked from receiving my emails?
  - id: SuppressionController_addDomain
    intent: Suppress an entire domain
    question: Can I block sending to every address at a particular domain?
  - id: SuppressionController_removeDomain
    intent: Remove a domain from the suppression list
    question: Can I unblock a domain I suppressed earlier?
  phrasing_ops: 8
  slug: live-direct-marketing-online-suppression-api
- baseURL: https://api.live-direct-marketing.online
  baseurl_source: declared
  description: The System API from Live Direct Marketing — 2 operation(s) for system.
  name: Live Direct Marketing System API
  phrasing_intents:
  - id: SystemController_getVersion
    intent: Get the deployed build version
    question: Which version of the platform is deployed right now?
  - id: SystemController_getOperator
    intent: Get the operator's legal entity details
    question: Who is the legal entity operating this service?
  phrasing_ops: 2
  slug: live-direct-marketing-online-system-api
- baseURL: https://api.live-direct-marketing.online
  baseurl_source: declared
  description: The SystemBriefIntake API from Live Direct Marketing — 2 operation(s) for systembriefintake.
  name: Live Direct Marketing System Brief Intake API
  phrasing_intents:
  - id: SystemBriefIntakeController_limits
    intent: Get the brief intake limits
    question: What limits apply to submitting briefs through the internal intake?
  - id: SystemBriefIntakeController_receive
    intent: Submit a brief to the internal intake
    question: How does a system send a brief into the intake queue?
  phrasing_ops: 2
  slug: live-direct-marketing-online-systembriefintake-api
- baseURL: https://api.live-direct-marketing.online
  baseurl_source: declared
  description: The Tags API from Live Direct Marketing — 8 operation(s) for tags.
  name: Live Direct Marketing Tags API
  phrasing_intents:
  - id: TagsController_findAll
    intent: List workspace tags
    question: What tags exist in my workspace?
  - id: TagsController_create
    intent: Create a tag
    question: How do I make a new tag for organizing records?
  - id: TagsController_update
    intent: Rename or recolor a tag
    question: Can I rename a tag I already created?
  - id: TagsController_remove
    intent: Delete a tag
    question: Can I delete a tag from the workspace entirely?
  - id: TagsController_attachToCompany
    intent: Tag a company
    question: How do I apply a tag to a company?
  - id: TagsController_detachFromCompany
    intent: Remove a tag from a company
    question: Can I take a tag off a company without deleting the tag?
  - id: TagsController_attachToContact
    intent: Tag a contact
    question: Can I add a tag to an individual contact?
  - id: TagsController_detachFromContact
    intent: Remove a tag from a contact
    question: How do I remove a tag from one contact?
  phrasing_ops: 10
  slug: live-direct-marketing-online-tags-api
- baseURL: https://api.live-direct-marketing.online
  baseurl_source: declared
  description: The Tasks API from Live Direct Marketing — 31 operation(s) for tasks.
  name: Live Direct Marketing Tasks API
  phrasing_intents:
  - id: TasksController_findAll
    intent: List tasks with status and method filters
    question: Which of my tasks are currently active?
  - id: TasksController_create
    intent: Create a new processing task
    question: How do I set up a site-scoring task that pulls its companies from a company list?
  - id: TasksController_findById
    intent: Get a task's details and progress
    question: How far along is my task — how many items has it processed out of the total?
  - id: TasksController_update
    intent: Update a task's description, config or schedule
    question: Can I change the description or source list on a task I already created?
  - id: TasksController_remove
    intent: Delete a task
    question: How do I permanently remove a task I no longer need?
  - id: TasksController_listBranches
    intent: List a task's sub-sequence branches
    question: What sub-sequence branches hang off my task?
  - id: TasksController_createBranch
    intent: Create a sub-sequence branch off a task
    question: Can I branch contacts off a task into an ICP review when a certain event happens?
  - id: TasksController_enrollInBranch
    intent: Enroll contacts into a task branch
    question: How do I manually put specific contacts into a task's branch?
  phrasing_ops: 41
  slug: live-direct-marketing-online-tasks-api
- baseURL: https://api.live-direct-marketing.online
  baseurl_source: declared
  description: The telegram API from Live Direct Marketing — 3 operation(s) for telegram.
  name: Live Direct Marketing Telegram API
  phrasing_intents:
  - id: TelegramController_webhook
    intent: Receive a Telegram bot webhook update
    question: Where does Telegram deliver bot updates for this platform?
  - id: TelegramController_loginLink
    intent: Get a Telegram login link
    question: How do I sign in with Telegram?
  - id: TelegramController_linkToken
    intent: Create a token to link a Telegram account
    question: How do I connect my Telegram account to my user?
  phrasing_ops: 3
  slug: live-direct-marketing-online-telegram-api
- baseURL: https://api.live-direct-marketing.online
  baseurl_source: declared
  description: The tests API from Live Direct Marketing — 13 operation(s) for tests.
  name: Live Direct Marketing Tests API
  phrasing_intents:
  - id: TestsController_create
    intent: Start an inbox placement test from the web
    question: How do I run a free inbox placement test for my email address?
  - id: TestsController_get
    intent: Get a web placement test by token
    question: Where do I see the results of a placement test I started on the website?
  - id: TestsController_deleteTest
    intent: Delete a web placement test
    question: Can I remove a placement test I ran on the website?
  - id: TestsSseController_stream
    intent: Stream live results of a test
    question: Can I watch placement results arrive in real time?
  - id: TrackController_click
    intent: Record a tracked click
    question: Is there an endpoint that records link clicks for tracking?
  - id: WarmupController_finish
    intent: Finish a check and get its partial report
    question: Can I end a placement check early and keep what's been found so far?
  - id: WarmupController_warmup
    intent: Move spam-placed test emails to inbox
    question: Can I move my test emails that landed in spam back to the inbox as a not-spam signal?
  - id: WarmupController_repoll
    intent: Re-poll a test by public token
    question: My web test email arrived late; can I make the seeds re-check without an API key?
  phrasing_ops: 16
  slug: live-direct-marketing-online-tests-api
- baseURL: https://api.live-direct-marketing.online
  baseurl_source: declared
  description: The TlsRpt API from Live Direct Marketing — 1 operation(s) for tlsrpt.
  name: Live Direct Marketing Tls Rpt API
  phrasing_intents:
  - id: TlsRptController_list
    intent: List TLS-RPT reports
    question: Which TLS reporting (TLS-RPT) reports have we received about mail delivery encryption?
  phrasing_ops: 1
  slug: live-direct-marketing-online-tlsrpt-api
- baseURL: https://api.live-direct-marketing.online
  baseurl_source: declared
  description: The Tracking API from Live Direct Marketing — 14 operation(s) for tracking.
  name: Live Direct Marketing Tracking API
  phrasing_intents:
  - id: TrackingController_pixelOpen
    intent: Serve the open-tracking pixel and log an open
    question: How are email opens recorded when a recipient loads the image?
  - id: TrackingController_clickRedirect
    intent: Follow a tracked campaign click and log it
    question: How does a clicked link in a campaign email get logged before redirecting?
  - id: TrackingController_legacyRedirect
    intent: Follow a short redirect link without logging
    question: Where does a short /r/ link I created directly send people?
  - id: TrackingController_createLink
    intent: Create a tracking link
    question: How do I create a short tracking link without sending a campaign?
  - id: TrackingController_getLinkInfo
    intent: Look up a tracking link
    question: Where does a given tracking link point and is it cloaked?
  - id: TrackingController_updateLink
    intent: Change a tracking link's target or cloaking
    question: How do I change where an existing tracking link redirects?
  - id: TrackingController_deleteLink
    intent: Delete a tracking link
    question: How do I remove a tracking link I no longer need?
  - id: TrackingController_simulateClick
    intent: Test a link's cloaking decision without logging
    question: Would a given user agent be sent to the target, the decoy or a captcha?
  phrasing_ops: 17
  slug: live-direct-marketing-online-tracking-api
- baseURL: https://api.live-direct-marketing.online
  baseurl_source: declared
  description: The Tracking / Bot List API from Live Direct Marketing — 4 operation(s) for tracking / bot list.
  name: Live Direct Marketing Tracking / Bot List API
  phrasing_intents:
  - id: BotListController_stats
    intent: Get global bot-list stats
    question: How many bot feeds and custom IP ranges are on the global bot list?
  - id: BotListController_refresh
    intent: Reload external bot feeds now
    question: Can I force the bot feeds to reload instead of waiting for the schedule?
  - id: BotListController_addCidr
    intent: Add an IP range to the global bot list
    question: How do I flag clicks from a whole IP range as bot traffic?
  - id: BotListController_removeCidr
    intent: Remove an IP range from the global bot list
    question: How do I stop treating an IP range as bot traffic?
  - id: BotListController_addUa
    intent: Add a user-agent pattern to the bot list
    question: Can I mark clicks from a specific crawler's user agent as bots?
  - id: BotListController_removeUa
    intent: Remove a user-agent pattern from the bot list
    question: How do I unflag a user agent I previously marked as a bot?
  phrasing_ops: 6
  slug: live-direct-marketing-online-tracking-bot-list-api
- baseURL: https://api.live-direct-marketing.online
  baseurl_source: declared
  description: The Tracking / Domain API from Live Direct Marketing — 7 operation(s) for tracking / domain.
  name: Live Direct Marketing Tracking / Domain API
  phrasing_intents:
  - id: TrackingDomainController_findAll
    intent: List tracking domains
    question: Which click-tracking domains have I set up?
  - id: TrackingDomainController_create
    intent: Add a tracking domain
    question: How do I set up my own branded domain for link tracking?
  - id: TrackingDomainController_getStats
    intent: Get tracking domain statistics
    question: How many of my tracking domains are active versus pending?
  - id: TrackingDomainController_findOne
    intent: Get a tracking domain
    question: What's the status and CNAME target of one tracking domain?
  - id: TrackingDomainController_update
    intent: Update a tracking domain
    question: Can I change the settings on an existing tracking domain?
  - id: TrackingDomainController_remove
    intent: Delete a tracking domain
    question: How do I remove a tracking domain I no longer use?
  - id: TrackingDomainController_healthCheck
    intent: Verify a tracking domain's DNS and SSL
    question: Is my tracking domain's CNAME and SSL set up correctly?
  - id: TrackingDomainController_setDefault
    intent: Make a tracking domain the default
    question: Which tracking domain serves the email open pixel?
  phrasing_ops: 10
  slug: live-direct-marketing-online-tracking-domain-api
- baseURL: https://api.live-direct-marketing.online
  baseurl_source: declared
  description: The Tracking / Redirect Source API from Live Direct Marketing — 3 operation(s) for tracking / redirect source.
  name: Live Direct Marketing Tracking / Redirect Source API
  phrasing_intents:
  - id: RedirectSourceController_findAll
    intent: List redirect sources
    question: Which redirect sources do I have for link tracking?
  - id: RedirectSourceController_create
    intent: Create a redirect source
    question: How do I add a new redirect source for tracked links?
  - id: RedirectSourceController_getStats
    intent: Get redirect source statistics
    question: What are the overall stats for my redirect sources?
  - id: RedirectSourceController_findOne
    intent: Get a redirect source
    question: Can I view the details of one redirect source?
  - id: RedirectSourceController_update
    intent: Update a redirect source
    question: Can I change an existing redirect source?
  - id: RedirectSourceController_remove
    intent: Delete a redirect source
    question: How do I remove a redirect source I no longer use?
  phrasing_ops: 6
  slug: live-direct-marketing-online-tracking-redirect-source-api
- baseURL: https://api.live-direct-marketing.online
  baseurl_source: declared
  description: The Unsubscribe API from Live Direct Marketing — 1 operation(s) for unsubscribe.
  name: Live Direct Marketing Unsubscribe API
  phrasing_intents:
  - id: UnsubscribeController_handleUnsubscribe
    intent: Process an unsubscribe link click
    question: What happens when a recipient clicks the unsubscribe link in an email?
  - id: UnsubscribeController_oneClickUnsubscribe
    intent: Handle an RFC 8058 one-click unsubscribe
    question: Does the platform support RFC 8058 one-click unsubscribe from mail clients?
  phrasing_ops: 2
  slug: live-direct-marketing-online-unsubscribe-api
- baseURL: https://api.live-direct-marketing.online
  baseurl_source: declared
  description: The User Settings API from Live Direct Marketing — 2 operation(s) for user settings.
  name: Live Direct Marketing User Settings API
  phrasing_intents:
  - id: UserSettingsController_get
    intent: Get my user settings
    question: What are my current personal settings in the app?
  - id: UserSettingsController_update
    intent: Update my user settings
    question: How do I change my personal preferences?
  - id: UserSettingsController_availableTransports
    intent: List transports enabled by the admin
    question: Which sending transports has my admin enabled for me to choose?
  phrasing_ops: 3
  slug: live-direct-marketing-online-user-settings-api
- baseURL: https://api.live-direct-marketing.online
  baseurl_source: declared
  description: The Users API from Live Direct Marketing — 12 operation(s) for users.
  name: Live Direct Marketing Users API
  phrasing_intents:
  - id: UsersController_acceptTerms
    intent: Accept the legal terms as the current user
    question: How do I accept the terms of service for my user?
  - id: UsersController_findAll
    intent: List platform users
    question: Which users are registered on the platform?
  - id: UsersController_createUser
    intent: Create a user
    question: How does a super admin create a new user?
  - id: UsersController_systemStats
    intent: Get system resource stats
    question: What are the current system stats for the platform server?
  - id: UsersController_killProcess
    intent: Kill a system process
    question: Can a super admin kill a stuck process on the server?
  - id: UsersController_cleanupOrphans
    intent: Clean up orphaned system resources
    question: Can I clean up orphaned resources left on the system?
  - id: UsersController_findById
    intent: Get a user
    question: What details does the platform hold for a specific user?
  - id: UsersController_deleteUser
    intent: Delete a user and clean up their tenants
    question: What happens to a user's tenants when I delete the user?
  phrasing_ops: 15
  slug: live-direct-marketing-online-users-api
- baseURL: https://api.live-direct-marketing.online
  baseurl_source: declared
  description: The Utils API from Live Direct Marketing — 2 operation(s) for utils.
  name: Live Direct Marketing Utils API
  phrasing_intents:
  - id: UtilsController_listTimezones
    intent: List timezones with cities and offsets
    question: Which timezones can I pick from, with their cities and UTC offsets?
  - id: UtilsController_lookupTimezone
    intent: Find the timezone for a city or country
    question: What timezone is a given city in?
  phrasing_ops: 2
  slug: live-direct-marketing-online-utils-api
- baseURL: https://api.live-direct-marketing.online
  baseurl_source: declared
  description: The Variable Resolver API from Live Direct Marketing — 2 operation(s) for variable resolver.
  name: Live Direct Marketing Variable Resolver API
  phrasing_intents:
  - id: VariableResolverController_resolve
    intent: Resolve template variables for a contact
    question: What values will my email template variables take for a specific contact?
  - id: VariableResolverController_getAvailableVariables
    intent: List available template variables
    question: Which merge variables can I use in my email templates?
  phrasing_ops: 2
  slug: live-direct-marketing-online-variable-resolver-api
- baseURL: https://api.live-direct-marketing.online
  baseurl_source: declared
  description: The Webhooks API from Live Direct Marketing — 5 operation(s) for webhooks.
  name: Live Direct Marketing Webhooks API
  phrasing_intents:
  - id: WebhooksController_list
    intent: List webhook endpoints
    question: Which webhook endpoints have I registered?
  - id: WebhooksController_create
    intent: Create a webhook endpoint
    question: How do I start receiving event notifications at my own URL?
  - id: WebhooksController_update
    intent: Update a webhook endpoint
    question: Can I change the settings of an existing webhook endpoint?
  - id: WebhooksController_remove
    intent: Delete a webhook endpoint
    question: How do I stop sending events to a webhook URL for good?
  - id: WebhooksController_deliveries
    intent: List a webhook's delivery history
    question: Did my webhook deliveries succeed or fail?
  - id: WebhooksController_retry
    intent: Retry one webhook delivery
    question: Can I resend a single failed webhook delivery?
  - id: WebhooksController_retrigger
    intent: Retrigger recent deliveries for a webhook
    question: Can I replay the last several deliveries to a webhook endpoint?
  phrasing_ops: 7
  slug: live-direct-marketing-online-webhooks-api
- baseURL: https://api.live-direct-marketing.online
  baseurl_source: declared
  description: The workers API from Live Direct Marketing — 5 operation(s) for workers.
  name: Live Direct Marketing Workers API
  phrasing_intents:
  - id: WorkersController_claim
    intent: Claim the next worker job
    question: How does a worker pick up its next job from the queue?
  - id: WorkersController_heartbeat
    intent: Send a heartbeat for a running worker job
    question: How does a worker show a long job is still running?
  - id: WorkersController_uploadScreenshot
    intent: Upload a screenshot for a worker job
    question: How does a worker attach a screenshot to a job?
  - id: WorkersController_complete
    intent: Mark a worker job complete
    question: How does a worker report that a job finished successfully?
  - id: WorkersController_fail
    intent: Mark a worker job failed
    question: How does a worker report that a job failed?
  phrasing_ops: 5
  slug: live-direct-marketing-online-workers-api
- baseURL: https://api.live-direct-marketing.online/mcp
  baseurl_source: declared
  description: The Linked In API from Live Direct Marketing — 9 operation(s) for linked in.
  name: Live Direct Marketing Linked In API
  phrasing_intents:
  - id: LinkedinController_getIntegration
    intent: Check the LinkedIn integration status
    question: Is the LinkedIn outreach module turned on for my workspace?
  - id: LinkedinController_updateIntegration
    intent: Enable, disable or kill-switch LinkedIn outreach
    question: How do I switch off all LinkedIn activity at once with the kill-switch?
  - id: LinkedinController_listAccounts
    intent: List connected LinkedIn accounts
    question: Which LinkedIn accounts are connected for outreach?
  - id: LinkedinController_getAccount
    intent: Get one LinkedIn account
    question: What limits and sending windows are set on one LinkedIn account?
  - id: LinkedinController_patchAccount
    intent: Change a LinkedIn account's limits or pause it
    question: Can I lower the daily action limits on a LinkedIn account?
  - id: LinkedinController_disconnect
    intent: Disconnect a LinkedIn account session
    question: How do I revoke a LinkedIn session and erase its stored cookies?
  - id: LinkedinController_listCampaigns
    intent: List LinkedIn campaigns
    question: What LinkedIn outreach campaigns are running?
  - id: LinkedinController_createCampaign
    intent: Create a LinkedIn campaign
    question: How do I start a new LinkedIn outreach campaign?
  phrasing_ops: 13
  slug: live-direct-marketing-online-linked-in-api
artifact_total: 165
asyncapis:
- description: ''
  name: Live Direct Marketing Online Webhooks
  slug: live-direct-marketing-online-webhooks
common:
- group: other
  href: https://artifacts.apis.io/live-direct-marketing-online/capabilities/live-direct-marketing-online-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/live-direct-marketing-online-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/live-direct-marketing-online/overlays/live-direct-marketing-online-ldm-v3-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/live-direct-marketing-online-ldm-v3-overlay.yaml
- group: other
  href: https://artifacts.apis.io/live-direct-marketing-online/overlays/live-direct-marketing-online-inbox-check-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/live-direct-marketing-online-inbox-check-overlay.yaml
- group: auth
  href: https://artifacts.apis.io/live-direct-marketing-online/security/live-direct-marketing-online-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/live-direct-marketing-online-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://developers.live-direct-marketing.online/legal/security
- group: auth
  href: https://artifacts.apis.io/live-direct-marketing-online/security/live-direct-marketing-online-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/live-direct-marketing-online-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/live-direct-marketing-online/agentic-access/live-direct-marketing-online-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/live-direct-marketing-online-agentic-access.yml
- group: company
  title: ''
  type: Website
  url: https://live-direct-marketing.online/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.live-direct-marketing.online/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.live-direct-marketing.online/
- group: docs
  title: ''
  type: APIReference
  url: https://developers.live-direct-marketing.online/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.live-direct-marketing.online/quickstart
- group: operate
  title: ''
  type: Support
  url: https://live-direct-marketing.online/contact
- group: company
  title: ''
  type: Blog
  url: https://live-direct-marketing.online/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/live-direct-marketing
- group: commercial
  title: ''
  type: Pricing
  url: https://developers.live-direct-marketing.online/pricing
- group: start
  title: ''
  type: SignUp
  url: https://developers.live-direct-marketing.online/signup
- group: start
  title: ''
  type: Login
  url: https://app.live-direct-marketing.online/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://live-direct-marketing.online/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://live-direct-marketing.online/policy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/101983165/
- group: operate
  title: ''
  type: ChangeLog
  url: https://developers.live-direct-marketing.online/changelog
- group: operate
  href: https://artifacts.apis.io/live-direct-marketing-online/changelog/live-direct-marketing-online-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/live-direct-marketing-online-changelog.yml
- group: agent
  href: https://artifacts.apis.io/live-direct-marketing-online/llms/live-direct-marketing-online-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/live-direct-marketing-online-llms.txt
- group: agent
  href: https://artifacts.apis.io/live-direct-marketing-online/llms/live-direct-marketing-online-developers-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/live-direct-marketing-online-developers-llms.txt
- group: agent
  href: https://artifacts.apis.io/live-direct-marketing-online/llms/live-direct-marketing-online-inbox-check-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/live-direct-marketing-online-inbox-check-llms.txt
- group: build
  href: https://artifacts.apis.io/live-direct-marketing-online/packages/live-direct-marketing-online-packages.yml
  title: ''
  type: Packages
  url: packages/live-direct-marketing-online-packages.yml
- group: build
  href: https://artifacts.apis.io/live-direct-marketing-online/packages/live-direct-marketing-online-packages.yml
  title: ''
  type: SDKs
  url: packages/live-direct-marketing-online-packages.yml
- group: agent
  href: https://artifacts.apis.io/live-direct-marketing-online/well-known/live-direct-marketing-online-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/live-direct-marketing-online-well-known.yml
- group: auth
  href: https://artifacts.apis.io/live-direct-marketing-online/well-known/live-direct-marketing-online-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/live-direct-marketing-online-security.txt
- group: other
  href: https://artifacts.apis.io/live-direct-marketing-online/a2a/live-direct-marketing-online-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/live-direct-marketing-online-a2a.yml
- group: agent
  href: https://artifacts.apis.io/live-direct-marketing-online/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/live-direct-marketing-online/conformance/live-direct-marketing-online-conformance.yml
  title: ''
  type: Conformance
  url: conformance/live-direct-marketing-online-conformance.yml
- group: design
  href: https://artifacts.apis.io/live-direct-marketing-online/errors/live-direct-marketing-online-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/live-direct-marketing-online-problem-types.yml
- group: design
  href: https://artifacts.apis.io/live-direct-marketing-online/lifecycle/live-direct-marketing-online-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/live-direct-marketing-online-lifecycle.yml
- group: auth
  href: https://artifacts.apis.io/live-direct-marketing-online/authentication/live-direct-marketing-online-authentication.yml
  title: ''
  type: Authentication
  url: authentication/live-direct-marketing-online-authentication.yml
- group: auth
  href: https://artifacts.apis.io/live-direct-marketing-online/scopes/live-direct-marketing-online-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/live-direct-marketing-online-scopes.yml
- group: design
  href: https://artifacts.apis.io/live-direct-marketing-online/conventions/live-direct-marketing-online-conventions.yml
  title: ''
  type: Conventions
  url: conventions/live-direct-marketing-online-conventions.yml
- group: design
  href: https://artifacts.apis.io/live-direct-marketing-online/conventions/live-direct-marketing-online-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/live-direct-marketing-online-conventions.yml
- group: start
  href: https://artifacts.apis.io/live-direct-marketing-online/sandbox/live-direct-marketing-online-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/live-direct-marketing-online-sandbox.yml
- group: commercial
  href: https://artifacts.apis.io/live-direct-marketing-online/plans/live-direct-marketing-online-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/live-direct-marketing-online-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/live-direct-marketing-online/rate-limits/live-direct-marketing-online-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/live-direct-marketing-online-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/live-direct-marketing-online/asyncapi/live-direct-marketing-online-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/live-direct-marketing-online-webhooks.yml
- group: design
  href: https://artifacts.apis.io/live-direct-marketing-online/data-model/live-direct-marketing-online-data-model.yml
  title: ''
  type: DataModel
  url: data-model/live-direct-marketing-online-data-model.yml
- group: other
  href: https://artifacts.apis.io/live-direct-marketing-online/regulatory/live-direct-marketing-online-regulatory-posture.yml
  title: ''
  type: DataSubjectRequest
  url: regulatory/live-direct-marketing-online-regulatory-posture.yml
created: '2026-09-19'
description: 'Live Direct Marketing (LDM) is a B2B outreach and CRM platform built to be operated by AI agents: the same Bearer-authenticated HTTPS surface serves the web UI, MCP clients and A2A peers. The LDM v3 API publishes an OpenAPI 3.0 contract with 1,304 operations across 119 tags (companies, contacts, leads, pipelines, campaigns, creatives, mailboxes, deliverability probes, suppression and stop-lists, webhooks, billing, DSAR) and a remote Streamable-HTTP MCP server with an anonymous bootstrap (ldm_terms / ldm_register) that mints a scoped ldm_* key without a human. A second product, Inbox Check, is a free inbox-placement test with its own 196-operation OpenAPI, a remote MCP server and an A2A agent card at check.live-direct-marketing.online. Billing is per confirmed inbox delivery ($0.015 managed / $0.005 BYOC), read from a public pricing endpoint. The operator is a Russian entity (OOO LDM, Yaroslavl); legal documents are drafts pending lawyer review.'
finops:
- has_sources: true
  method: derived
  name: Live Direct Marketing Online Finops
  primary_unit: prepaid balance
  service_category: ''
  slug: live-direct-marketing-online-finops
  template: false
image: https://live-direct-marketing.online/img/logo.png
layout: provider
mcp_servers:
- description: Live Direct Marketing operates TWO remote Streamable-HTTP MCP servers and ships TWO stdio packages. The LDM.delivery server at https://api.live-direct-marketing.online/mcp accepted an anonymous initia
  name: Live Direct Marketing MCP Server
  slug: live-direct-marketing-online-mcp-yml
- description: ''
  name: Remote endpoint (Streamable HTTP)
  slug: remote-endpoint-streamable-http
modified: '2026-09-19'
name: Live Direct Marketing
nav: Providers
network: true
overview: 'Live Direct Marketing publishes 150 API contracts indexed on the [APIs.io](https://apis.io/) network, including A2A API, Account API, Activities API, and 147 more. Tagged areas include Company, Email, Email Deliverability, Sales & marketing automation, and CRM.


  The Live Direct Marketing catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Live Direct Marketing''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 38 more developer resources.'
plans:
- name: Live Direct Marketing Online Plans Pricing
  plan_count: 2
  slug: live-direct-marketing-online-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 8
  name: Live Direct Marketing Online Rate Limits
  slug: live-direct-marketing-online-rate-limits
rules:
- authorship: generated
  effective_rule_count: 92
  extends:
  - spectral:oas
  name: Live Direct Marketing API Rules
  rule_count: 51
  severity_counts:
    error: 40
    hint: 0
    info: 1
    warn: 10
  slug: live-direct-marketing-online-rules
scopes:
- name: Live Direct Marketing Online Scopes
  scope_count: 0
  slug: live-direct-marketing-online-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 56.5
  coverage:
    artifact_dirs: 33
    catalog_earned: 64.5
    catalog_earned_first_party: 20.0
    catalog_gap: 50.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -12.8
  facets:
    access_clarity: 51.3
    contract_governance: 31.8
    contract_quality: 49.8
    developer_ergonomics: 50.0
    discoverability: 75.0
    operational_transparency: 55.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - russia
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 69.3
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 82.1
      derived: 0
      marker_coverage: 0.0
      total: 145
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 40.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 22.2
screenshot: https://apis.io/screenshots/live-direct-marketing-online/live-direct-marketing-online-2026-10-11T110532.png
security:
- kind: authentication
  name: Live Direct Marketing Online Authentication
  slug: live-direct-marketing-online-authentication
  summary_line: http bearer/apiKey (header)/cookie session · 6 schemes
- kind: domain-security
  name: Live Direct Marketing Online Domain Security
  slug: live-direct-marketing-online-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Live Direct Marketing Online Vulnerability Disclosure
  slug: live-direct-marketing-online-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 3
skills:
- name: live-direct-marketing-online-agent-bootstrap
  slug: live-direct-marketing-online-agent-bootstrap
- name: live-direct-marketing-online-domain-monitoring
  slug: live-direct-marketing-online-domain-monitoring
- name: live-direct-marketing-online-inbox-placement-test
  slug: live-direct-marketing-online-inbox-placement-test
slug: live-direct-marketing-online
tags:
- Company
- Email
- Email Deliverability
- Sales & marketing automation
- CRM
- Lead Management
- Cold Outreach
- Agent-Native
- MCP
- A2A
- Webhook
- B2B
website: https://live-direct-marketing.online/
---
