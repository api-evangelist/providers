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
  - scopes
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: derived
    agentic_access: true
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: true
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: true
    idempotency: verified
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 71.7
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Two remote Model Context Protocol servers. A public read-only documentation server at https://leadping.ai/docs/mcp answers anonymous tools/list with search, virtual-filesystem and feedback tools. An a
  name: Leadping MCP Servers
  slug: leadping-mcp-servers
- description: Outbound HTTPS webhook deliveries fired by Leadping automations, signed with the Standard Webhooks specification (HMAC-SHA256 over {webhook-id}.{webhook-timestamp}.{body}, whsec_ signing secret). Lead
  name: Leadping Webhook Events
  slug: leadping-webhook-events
- baseURL: https://api.leadping.ai
  baseurl_source: declared
  description: Provides lead, communication, conversion, and organization performance analytics. Use these endpoints to measure activity over time, compare outcomes, and power operational dashboards and reporting wo
  name: Leadping Analytics API
  phrasing_intents:
  - id: Analytics_GetCurrentOrganization
    intent: Get lead communication analytics
    question: What do my organization's lead response metrics look like in Leadping?
  phrasing_ops: 1
  slug: leadping-analytics-api
- baseURL: https://api.leadping.ai
  baseurl_source: declared
  description: 'Manages automated lead follow-up workflows and their execution history. Use these endpoints to configure SMS automation steps, preview eligible leads, run workflows, and inspect individual automation '
  name: Leadping Automations API
  phrasing_intents:
  - id: Automations_Create
    intent: Create a lead follow-up automation
    question: How do I set up an automation that follows up with new leads?
  - id: Automations_Update
    intent: Update a follow-up automation
    question: How do I change the triggers on an existing automation?
  - id: Automations_Get
    intent: Get a follow-up automation
    question: Which triggers and message steps does this automation use?
  - id: Automations_Delete
    intent: Delete a follow-up automation
    question: How do I permanently remove an automation so it stops scheduling follow-ups?
  - id: Automations_GetRuns
    intent: List an automation's recent runs
    question: How can I see the recent execution history of an automation?
  - id: Automations_GetRun
    intent: Get one automation run
    question: Can I inspect the console state of a single automation run?
  - id: Automations_GetAllForCurrentUser
    intent: List my follow-up automations
    question: Which follow-up automations do I have in Leadping?
  - id: Automations_Preview
    intent: Preview an automation on a sample lead
    question: Can I test what an automation would send before turning it on?
  phrasing_ops: 9
  slug: leadping-automations-api
- baseURL: https://api.leadping.ai
  baseurl_source: declared
  description: Provides call event records for auditing, diagnostics, and reporting. Use these endpoints to search and inspect lifecycle events emitted as Leadping calls are initiated, connected, completed, or fail.
  name: Leadping Call Events API
  phrasing_intents:
  - id: CallEvents_GetAllForCurrentUser
    intent: List my call event history
    question: What calls have I made or received across all my leads?
  - id: CallEvents_GetById
    intent: Get a call event
    question: How do I see the provider status and metadata for one call event?
  - id: CallEvents_GetByLeadId
    intent: List call events for a lead
    question: How many times have we called a specific lead and what happened?
  - id: CallEvents_GetByPhoneNumber
    intent: List call events for a phone number
    question: What call activity has a particular phone number had?
  phrasing_ops: 4
  slug: leadping-callevents-api
- baseURL: https://api.leadping.ai
  baseurl_source: declared
  description: Manages outbound Leadping calls and active call-control workflows. Use these endpoints to initiate or cancel a call, retrieve call state, and transfer an active call within supported telephony flows.
  name: Leadping Calls API
  phrasing_intents:
  - id: Calls_InitiateCall
    intent: Place a phone call to a lead
    question: How do I start an outbound phone call to a lead?
  - id: Calls_HangupCall
    intent: Hang up an active call
    question: How do I end a call that's still in progress?
  - id: Calls_GetCallStatus
    intent: Check a phone call's status
    question: Is my call still ringing, connected, or finished?
  - id: Calls_TransferCall
    intent: Transfer an active call
    question: How do I transfer a live call to another phone number?
  phrasing_ops: 4
  slug: leadping-calls-api
- baseURL: https://api.leadping.ai
  baseurl_source: declared
  description: Accepts public contact and website inquiry submissions for Leadping. Use these endpoints to send a structured support or sales inquiry from an application or submit the Leadping website contact form.
  name: Leadping Contact API
  phrasing_intents:
  - id: Contact_Submit
    intent: Send a message to Leadping support
    question: How do I contact Leadping support without logging in?
  - id: Contact_SubmitWebsite
    intent: Submit a generated-website inquiry
    question: How does a visitor's inquiry on my generated website reach me?
  phrasing_ops: 2
  slug: leadping-contact-api
- baseURL: https://api.leadping.ai
  baseurl_source: declared
  description: Provides lead conversation timelines and inbox-oriented conversation views. Use these endpoints to list recent conversations and retrieve the cross-channel communication history associated with a lead
  name: Leadping Conversations API
  phrasing_intents:
  - id: Conversations_GetAllForCurrentUser
    intent: List my inbox conversations
    question: What conversations are in my inbox right now?
  - id: Conversations_MarkAsRead
    intent: Mark a conversation as read
    question: How do I clear the unread state on an inbox conversation?
  - id: Conversations_GetConversationsByLead
    intent: List conversations for a lead
    question: Which conversation threads exist for a particular lead?
  phrasing_ops: 3
  slug: leadping-conversations-api
- baseURL: https://api.leadping.ai
  baseurl_source: declared
  description: Provides a unified record of Leadping activity across communication channels. Use these endpoints to retrieve event timelines, search event history, inspect event details, and record supported applica
  name: Leadping Events API
  phrasing_intents:
  - id: Events_GetAllForCurrentUser
    intent: List my lead events
    question: What lead, SMS, call and automation events can I see?
  - id: Events_GetAllForOrganization
    intent: List an organization's event history
    question: How can an admin review every event across an organization?
  - id: Events_GetAllForConversation
    intent: List a conversation's events
    question: What notes, messages and calls happened in one conversation?
  - id: Events_GetAllForLead
    intent: List a lead's event history
    question: What has happened with a lead across routing, automation and messaging?
  - id: Events_GetById
    intent: Get an event summary
    question: How do I look up one event's type, timestamps and related records?
  - id: Events_GetDetailById
    intent: Get an event's full payload
    question: Can I see the raw JSON payload of an event for debugging?
  - id: Events_CreateNote
    intent: Add a note to a conversation
    question: How do I leave a handoff note on a conversation?
  phrasing_ops: 7
  slug: leadping-events-api
- baseURL: https://api.leadping.ai
  baseurl_source: declared
  description: Captures Leadping product feedback and supports administrative triage. Users can submit feedback, while authorized staff can search, inspect, classify, and update feedback throughout the review proces
  name: Leadping Feedback API
  phrasing_intents:
  - id: Feedback_Create
    intent: Send product feedback
    question: How do I send product feedback to the Leadping team?
  phrasing_ops: 1
  slug: leadping-feedback-api
- baseURL: https://api.leadping.ai
  baseurl_source: declared
  description: Manages lead intake, records, assignment, routing, and lifecycle operations. Use these endpoints to ingest leads from trusted sources, search and update lead records, manage ownership and tags, and ar
  name: Leadping Leads API
  phrasing_intents:
  - id: Leads_CreateExternal
    intent: Create a lead from an external source
    question: How do I push a lead captured on another system into Leadping with structured contact data?
  - id: Leads_CreateIntake
    intent: Create a lead from a flat intake payload
    question: How do I send a lead as a flat JSON intake body?
  - id: Leads_CreateIntakeFromQuery
    intent: Create a lead from query-string intake
    question: Can I post a lead just by putting its fields in a URL query string?
  - id: Leads_GetForCurrentUser
    intent: Get a lead
    question: How do I pull up everything about one lead?
  - id: Leads_Update
    intent: Update a lead's details
    question: How do I correct a lead's contact information?
  - id: Leads_Delete
    intent: Delete a lead
    question: How do I remove a lead so it disappears from my pipeline and inbox?
  - id: Leads_GetWorkflowStatusForCurrentUser
    intent: Check a lead's automation workflow status
    question: Is a lead currently in an active automation run or paused?
  - id: Leads_Archive
    intent: Archive a lead
    question: How do I take a lead out of my active pipeline without losing its history?
  phrasing_ops: 14
  slug: leadping-leads-api
- baseURL: https://api.leadping.ai
  baseurl_source: declared
  description: Manages the auditable history of lead status transitions. Use these endpoints to change a lead's status, correct transition records, search status history, and export status activity for reporting.
  name: Leadping Lead Status Changes API
  phrasing_intents:
  - id: LeadStatusChanges_SetCurrent
    intent: Set a lead's current status
    question: How do I record an outcome like appointment set on a lead?
  - id: LeadStatusChanges_Update
    intent: Edit a status history entry
    question: Can I fix a status change that was logged with the wrong outcome?
  - id: LeadStatusChanges_Get
    intent: Get a status history entry
    question: How do I look at a single past status change and its notes?
  - id: LeadStatusChanges_Delete
    intent: Delete a status history entry
    question: How do I remove an outcome record that shouldn't show in reports?
  - id: LeadStatusChanges_GetAllForCurrentOrganization
    intent: List organization status history
    question: Which status changes happened across my whole organization?
  - id: LeadStatusChanges_GetByLeadId
    intent: List a lead's status history
    question: What outcomes has a single lead gone through over time?
  - id: LeadStatusChanges_ExportByLeadId
    intent: Export a lead's status history
    question: Can I export one lead's outcome history for a handoff?
  phrasing_ops: 7
  slug: leadping-leadstatuschanges-api
- baseURL: https://api.leadping.ai
  baseurl_source: declared
  description: Manages user notifications, announcements, and push-notification installations. Use these endpoints to retrieve notification feeds and unread counts, update read state, and register or remove client p
  name: Leadping Notifications API
  phrasing_intents:
  - id: Notifications_GetForCurrentUser
    intent: Get a notification
    question: How do I open one notification and see its content?
  - id: Notifications_GetAllForCurrentUser
    intent: List my notifications
    question: What alerts and updates have I received?
  - id: Notifications_GetUnreadCount
    intent: Count unread notifications
    question: How many unread notifications do I have?
  - id: Notifications_MarkAsRead
    intent: Mark a notification as read
    question: How do I mark one notification as read?
  - id: Notifications_MarkAllAsRead
    intent: Mark all notifications as read
    question: Is there a way to clear every unread notification at once?
  - id: Notifications_GetAnnouncements
    intent: List announcements
    question: Where can I see Leadping release notes and notices?
  - id: Notifications_RegisterPushInstallation
    intent: Register a device for push notifications
    question: How do I get push notifications on my phone?
  - id: Notifications_UnregisterPushInstallation
    intent: Stop push notifications to a device
    question: How do I stop getting push notifications on an old phone?
  phrasing_ops: 8
  slug: leadping-notifications-api
- baseURL: https://api.leadping.ai
  baseurl_source: declared
  description: Manages Leadping organizations, memberships, invitations, settings, and API credentials. Use these endpoints to maintain organization profiles and branding, manage members and invitations, configure o
  name: Leadping Organizations API
  phrasing_intents:
  - id: Organizations_GetForCurrentUser
    intent: Get my organization profile
    question: What settings does my current organization have?
  - id: Organizations_CreateForCurrentUser
    intent: Create a new organization
    question: How do I start a brand new organization account and become its owner?
  - id: Organizations_UpdateForCurrentUser
    intent: Update my organization profile
    question: How do I change my organization's name or website?
  - id: Organizations_GetSwitchOptions
    intent: List organizations I can switch to
    question: Which organizations do I belong to?
  - id: Organizations_SwitchCurrentOrganization
    intent: Switch my active organization
    question: How do I change which organization I'm working in?
  - id: Organizations_GetCurrentOrganizationMembers
    intent: List organization members
    question: Who are the members of my organization?
  - id: Organizations_AddCurrentOrganizationMember
    intent: Add an existing user to my organization
    question: How do I add an existing Leadping user to my organization directly?
  - id: Organizations_ChangeCurrentOrganizationMemberRole
    intent: Change a member's role
    question: How do I promote a teammate to admin?
  phrasing_ops: 21
  slug: leadping-organizations-api
- baseURL: https://api.leadping.ai
  baseurl_source: declared
  description: Reports outbound delivery pacing and sending capacity for the current organization. Use these endpoints to determine whether outbound communications can proceed and to understand active throttles, lim
  name: Leadping Outbound Delivery API
  phrasing_intents:
  - id: OutboundDelivery_GetCurrentOrganizationOverview
    intent: Get outbound delivery overview
    question: How much outbound messaging capacity does my organization have left?
  phrasing_ops: 1
  slug: leadping-outbounddelivery-api
- baseURL: https://api.leadping.ai
  baseurl_source: declared
  description: Sends and manages SMS and MMS communications through Leadping. Use these endpoints to send messages, upload MMS media, and cancel eligible scheduled messages while preserving conversation and delivery
  name: Leadping Sms API
  phrasing_intents:
  - id: Sms_Send
    intent: Send a text message to a lead
    question: How do I text a lead from Leadping?
  - id: Sms_UploadMedia
    intent: Upload an MMS attachment
    question: How do I upload an image to include in an MMS?
  - id: Sms_CancelScheduled
    intent: Cancel a scheduled text
    question: How do I stop a scheduled text before it's delivered?
  phrasing_ops: 3
  slug: leadping-sms-api
- baseURL: https://api.leadping.ai
  baseurl_source: declared
  description: 'Provides SMS and MMS event records for delivery tracking and diagnostics. Use these endpoints to search and inspect message lifecycle events, including outbound delivery updates and inbound messaging '
  name: Leadping Sms Events API
  phrasing_intents:
  - id: SmsEvents_GetAllForCurrentUser
    intent: List my SMS history
    question: What text messages have I sent and received across all leads?
  - id: SmsEvents_GetById
    intent: Get an SMS event
    question: How do I check the delivery status of one text message?
  - id: SmsEvents_GetByLeadId
    intent: List text messages for a lead
    question: What texts have gone to a particular lead, including scheduled ones?
  - id: SmsEvents_GetByPhoneNumber
    intent: List SMS events for a phone number
    question: How much texting has one phone number done?
  phrasing_ops: 4
  slug: leadping-smsevents-api
- baseURL: https://api.leadping.ai
  baseurl_source: declared
  description: 'Manages lead sources, intake credentials, routing defaults, and attribution. Use these endpoints to create and configure sources, search source records, inspect source activity, rotate intake access, '
  name: Leadping Sources API
  phrasing_intents:
  - id: Sources_Create
    intent: Create a lead intake source
    question: How do I set up a new lead source for a vendor sending me leads?
  - id: Sources_Update
    intent: Update a lead source
    question: How do I change which states an existing source accepts?
  - id: Sources_Get
    intent: Get a lead source
    question: How do I check the intake settings of one lead source?
  - id: Sources_Delete
    intent: Delete a lead source
    question: How do I stop a source from sending me any more leads?
  - id: Sources_RotateApiKey
    intent: Rotate a source's intake credential
    question: How do I rotate the credential a vendor uses to post leads?
  - id: Sources_GetAllForCurrentUser
    intent: List my lead sources
    question: Which lead sources are configured for my account?
  - id: Sources_GetMetrics
    intent: Get a lead source's metrics
    question: How many leads from a source were accepted, rejected or duplicates?
  phrasing_ops: 7
  slug: leadping-sources-api
- baseURL: https://api.leadping.ai
  baseurl_source: declared
  description: Manages recipient suppression state for compliant Leadping communication workflows. Use these endpoints to check contact eligibility, record or release suppressions, and review suppression history bef
  name: Leadping Suppressions API
  phrasing_intents:
  - id: Suppressions_Suppress
    intent: Block a recipient from outreach
    question: How do I stop contacting someone who asked to opt out?
  - id: Suppressions_Release
    intent: Release a recipient suppression
    question: How do I allow a previously opted-out contact to be messaged again?
  - id: Suppressions_Check
    intent: Check if a recipient is suppressed
    question: Am I allowed to text this phone number, or is it suppressed?
  - id: Suppressions_GetAllForCurrentOrganization
    intent: List suppressed recipients
    question: Who is on my organization's do-not-contact list?
  - id: Suppressions_Get
    intent: Get a suppression entry
    question: Why and when was a particular recipient suppressed?
  phrasing_ops: 5
  slug: leadping-suppressions-api
- baseURL: https://api.leadping.ai
  baseurl_source: declared
  description: Manages organization-defined tags for categorizing and routing leads. Use these endpoints to list, create, update, and archive reusable tags that support lead filtering, automation, assignment, and re
  name: Leadping Tags API
  phrasing_intents:
  - id: Tags_GetAllForCurrentOrganization
    intent: List lead tags
    question: What tags does my organization use for leads?
  - id: Tags_Create
    intent: Create a lead tag
    question: How do I create a new label for segmenting leads?
  - id: Tags_Update
    intent: Update a lead tag
    question: How do I rename an existing tag?
  - id: Tags_Archive
    intent: Archive a lead tag
    question: How do I retire a tag so nobody uses it on new leads?
  phrasing_ops: 4
  slug: leadping-tags-api
- baseURL: https://api.leadping.ai
  baseurl_source: declared
  description: Provides shared authentication and bootstrap data for Leadping telephony clients. Use this endpoint to obtain the scoped credentials and configuration required to initialize supported calling experien
  name: Leadping Telephony API
  phrasing_intents:
  - id: Telephony_Login
    intent: Get a WebRTC calling token
    question: How does my browser softphone get credentials to place calls?
  phrasing_ops: 1
  slug: leadping-telephony-api
- baseURL: https://api.leadping.ai
  baseurl_source: declared
  description: Provides organization wallet and billing transaction records. Use these endpoints to search transaction history, inspect individual charges or credits, review transaction summaries, and issue administ
  name: Leadping Transactions API
  phrasing_intents:
  - id: Transactions_GetForCurrentUser
    intent: Get a billing transaction
    question: How do I see the amount and status of one transaction?
  - id: Transactions_GetAllForCurrentUser
    intent: List my billing transactions
    question: What wallet charges and top-ups have I had?
  phrasing_ops: 2
  slug: leadping-transactions-api
- baseURL: https://api.leadping.ai
  baseurl_source: declared
  description: Provides billable usage records for Leadping services. Use these endpoints to review messaging and calling consumption, inspect usage summaries, and reconcile provider activity for an organization.
  name: Leadping Usage API
  phrasing_intents:
  - id: Usage_GetAllForCurrentOrganization
    intent: List usage ledger entries
    question: What individual messaging charges show up on my usage ledger?
  - id: Usage_GetSummaryForCurrentOrganization
    intent: Get a usage summary
    question: How much have we spent on messaging this billing period?
  phrasing_ops: 2
  slug: leadping-usage-api
- baseURL: https://api.leadping.ai
  baseurl_source: declared
  description: Creates and delivers user-requested exports of Leadping account data. Use these endpoints to request an export, monitor its preparation status, and download the completed archive through a time-limite
  name: Leadping User Data Exports API
  phrasing_intents:
  - id: UserDataExports_RequestCurrentUser
    intent: Request a data export
    question: How do I get a copy of all my account, lead and event data?
  - id: UserDataExports_GetCurrentUserExport
    intent: Check a data export's status
    question: Is my data export ready to download yet?
  - id: UserDataExports_Download
    intent: Download a data export
    question: How do I download the file from a finished data export?
  phrasing_ops: 3
  slug: leadping-userdataexports-api
- baseURL: https://api.leadping.ai
  baseurl_source: declared
  description: Manages the current Leadping user's profile, preferences, setup, and account workflows. Use these endpoints to retrieve and update user data, configure communication and compliance preferences, comple
  name: Leadping Users API
  phrasing_intents:
  - id: Users_GetPaymentMethodForCurrentUser
    intent: Get my default payment method
    question: Which card is my default for billing?
  - id: Users_GetForCurrentUser
    intent: Get my user profile
    question: What does my Leadping user profile contain?
  - id: Users_UpdateForCurrentUser
    intent: Update my user profile
    question: How do I change my name or phone on my profile?
  - id: Users_UpdateNotificationPreferencesForCurrentUser
    intent: Update my notification preferences
    question: How do I get texted when a new lead comes in?
  - id: Users_ChangeBillingPlan
    intent: Change my billing plan
    question: How do I upgrade or downgrade my Leadping plan?
  - id: Users_UpdateCompliance
    intent: Update my compliance settings
    question: How do I update the compliance info needed to send messages?
  phrasing_ops: 6
  slug: leadping-users-api
- baseURL: https://api.leadping.ai
  baseurl_source: declared
  description: Manages organization wallet balances, funding, and credit activity. Use these endpoints to inspect wallet state and history, configure wallet behavior, add funds, and record credits or adjustments.
  name: Leadping Wallets API
  phrasing_intents:
  - id: Wallets_Get
    intent: Get a wallet by ID
    question: How do I check the balance of a specific wallet?
  - id: Wallets_GetForCurrentOrganization
    intent: Get my organization's wallet balance
    question: How much money is left in my organization's wallet?
  phrasing_ops: 2
  slug: leadping-wallets-api
- baseURL: https://api.leadping.ai/mcp
  baseurl_source: declared
  description: Provides published Leadping blog content. Use these endpoints to list published articles and retrieve an individual article by its public slug.
  name: Leadping Blog Articles API
  phrasing_intents:
  - id: BlogArticles_GetPublished
    intent: List published blog articles
    question: What articles are published on the Leadping blog?
  - id: BlogArticles_GetPublishedBySlug
    intent: Get a blog article by slug
    question: How do I fetch one blog article using its URL slug?
  phrasing_ops: 2
  slug: leadping-blogarticles-api
- baseURL: https://api.leadping.ai/mcp
  baseurl_source: declared
  description: The Leadping API API from Leadping — 2 operation(s) for leadping api.
  name: Leadping Leadping API
  phrasing_intents:
  - id: A2A_GetAgentCard
    intent: Get the A2A agent card
    question: What skills and authentication does Leadping's A2A agent card advertise?
  - id: A2A_HandleRequest
    intent: Send an A2A JSON-RPC request
    question: How do I call Leadping's agent operations over A2A JSON-RPC?
  phrasing_ops: 2
  slug: leadping-leadping-api-api
- baseURL: https://api.leadping.ai/mcp
  baseurl_source: declared
  description: Manages the lead statuses used to classify and track leads throughout their lifecycle. Use these endpoints to list, create, update, and archive organization-specific lead statuses for consistent pipel
  name: Leadping Lead Statuses API
  phrasing_intents:
  - id: LeadStatuses_GetAll
    intent: List lead statuses
    question: What lead statuses has my organization defined?
  - id: LeadStatuses_Create
    intent: Create a lead status
    question: How do I add a new pipeline stage for leads?
  - id: LeadStatuses_Update
    intent: Update a lead status
    question: How do I rename an existing pipeline stage?
  - id: LeadStatuses_Archive
    intent: Archive a lead status
    question: How do I retire a pipeline stage without losing lead history?
  phrasing_ops: 4
  slug: leadping-lead-statuses-api
- baseURL: https://api.leadping.ai/mcp
  baseurl_source: declared
  description: Manages organization payment methods and billing invoices. Use these endpoints to add, confirm, inspect, and remove payment methods or retrieve invoices associated with the current organization's bill
  name: Leadping Payment Methods API
  phrasing_intents:
  - id: PaymentMethods_GetAll
    intent: List payment methods
    question: What payment methods does my organization have on file?
  - id: PaymentMethods_GetInvoices
    intent: List invoices
    question: Where can I see my past invoices and whether they were paid?
  - id: PaymentMethods_GetInvoicePdfAccess
    intent: Get a link to an invoice PDF
    question: How do I download a PDF copy of an invoice?
  - id: PaymentMethods_Get
    intent: Get a payment method
    question: How do I see the card details of one payment method?
  - id: PaymentMethods_Delete
    intent: Delete a payment method
    question: How do I remove an old card from my account?
  - id: PaymentMethods_MakeDefault
    intent: Set the default payment method
    question: How do I choose which card pays future invoices?
  phrasing_ops: 6
  slug: leadping-payment-methods-api
- baseURL: https://api.leadping.ai/mcp
  baseurl_source: declared
  description: Manages phone-number discovery, purchasing, assignment, configuration, and compliance. Use these endpoints to search available numbers, manage owned numbers and caller identity, configure messaging or
  name: Leadping Phone Numbers API
  phrasing_intents:
  - id: PhoneNumbers_Search
    intent: Search phone numbers to buy
    question: What phone numbers are available to purchase in my area?
  - id: PhoneNumbers_GetAllForCurrentOrganization
    intent: List my organization's phone numbers
    question: Which phone numbers does my organization own?
  - id: PhoneNumbers_GetOutgoingForConversation
    intent: Pick the sender number for a conversation
    question: Which of my numbers will be used to reply in an existing conversation?
  - id: PhoneNumbers_GetOutgoingForNewOutbound
    intent: Pick the sender number for a new lead
    question: Which number will be used when I text a new lead for the first time?
  - id: PhoneNumbers_ValidateManualOverride
    intent: Validate a sender number override
    question: Can I check if a number is allowed as a manual sender before using it?
  - id: PhoneNumbers_SetConversationOverride
    intent: Pin a sender number to a conversation
    question: How do I force a conversation to always use one specific number?
  - id: PhoneNumbers_ClearConversationOverride
    intent: Clear a conversation's sender override
    question: How do I go back to automatic number selection for a conversation?
  - id: PhoneNumbers_Get
    intent: Get a phone number's details
    question: How do I see the assignment and messaging status of one of my numbers?
  phrasing_ops: 14
  slug: leadping-phone-numbers-api
artifact_total: 48
asyncapis:
- description: ''
  name: Leadping Webhooks
  slug: leadping-webhooks
common:
- group: other
  href: https://artifacts.apis.io/leadping/capabilities/leadping-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/leadping-capability-edges.yml
- group: company
  title: ''
  type: Website
  url: https://leadping.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://leadping.ai/docs/developers/overview
- group: docs
  title: ''
  type: Documentation
  url: https://leadping.ai/docs
- group: docs
  title: ''
  type: APIReference
  url: https://leadping.ai/docs/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://leadping.ai/docs/get-started
- group: operate
  title: ''
  type: Support
  url: https://leadping.ai/contact
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/leadpingai
- group: commercial
  title: ''
  type: Pricing
  url: https://leadping.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://leadping.ai/authentication/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://leadping.ai/docs/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://leadping.ai/docs/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.leadping.ai
- group: operate
  href: https://artifacts.apis.io/leadping/changelog/leadping-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/leadping-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://api.leadping.ai/changelog.json
- group: design
  href: https://artifacts.apis.io/leadping/lifecycle/leadping-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/leadping-lifecycle.yml
- group: auth
  href: https://artifacts.apis.io/leadping/authentication/leadping-authentication.yml
  title: ''
  type: Authentication
  url: authentication/leadping-authentication.yml
- group: design
  href: https://artifacts.apis.io/leadping/conventions/leadping-conventions.yml
  title: ''
  type: Conventions
  url: conventions/leadping-conventions.yml
- group: design
  href: https://artifacts.apis.io/leadping/conventions/leadping-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/leadping-conventions.yml
- group: design
  href: https://artifacts.apis.io/leadping/errors/leadping-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/leadping-problem-types.yml
- group: design
  href: https://artifacts.apis.io/leadping/data-model/leadping-data-model.yml
  title: ''
  type: DataModel
  url: data-model/leadping-data-model.yml
- group: operate
  href: https://artifacts.apis.io/leadping/rate-limits/leadping-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/leadping-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/leadping/plans/leadping-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/leadping-plans-pricing.yml
- group: commercial
  href: https://artifacts.apis.io/leadping/finops/leadping-finops.json
  title: ''
  type: FinOps
  url: finops/leadping-finops.json
- group: design
  href: https://artifacts.apis.io/leadping/vocabulary/leadping-vocabulary.json
  title: ''
  type: Vocabulary
  url: vocabulary/leadping-vocabulary.json
- group: build
  href: https://artifacts.apis.io/leadping/packages/leadping-packages.yml
  title: ''
  type: Packages
  url: packages/leadping-packages.yml
- group: build
  href: https://artifacts.apis.io/leadping/packages/leadping-packages.yml
  title: ''
  type: SDKs
  url: packages/leadping-packages.yml
- group: build
  title: ''
  type: SDKs
  url: https://leadping.ai/docs/sdks/overview
- group: agent
  href: https://artifacts.apis.io/leadping/mcp/leadping-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/leadping-mcp.yml
- group: build
  href: https://artifacts.apis.io/leadping/mcp/leadping-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/leadping-tool-crosswalk.yml
- group: design
  href: https://artifacts.apis.io/leadping/asyncapi/leadping-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/leadping-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/leadping/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/leadping/llms/leadping-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/leadping-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://leadping.ai/llms.txt
- group: agent
  href: https://artifacts.apis.io/leadping/well-known/leadping-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/leadping-well-known.yml
- group: other
  title: ''
  type: APICatalog
  url: https://leadping.ai/.well-known/api-catalog
- group: auth
  href: https://artifacts.apis.io/leadping/well-known/leadping-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/leadping-security.txt
- group: auth
  href: https://artifacts.apis.io/leadping/security/leadping-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/leadping-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/leadping/security/leadping-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/leadping-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/leadping/security/leadping-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/leadping-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/leadping/security/leadping-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/leadping-trust-center.yml
- group: design
  href: https://artifacts.apis.io/leadping/conformance/leadping-conformance.yml
  title: ''
  type: Conformance
  url: conformance/leadping-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://leadping.ai/docs/compliance
- group: other
  href: https://artifacts.apis.io/leadping/overlays/leadping-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/leadping-api-overlay.yaml
- group: other
  title: ''
  type: APIsJSON
  url: https://api.leadping.ai/apis.json
- group: other
  href: https://artifacts.apis.io/leadping/a2a/leadping-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/leadping-a2a.yml
- group: auth
  href: https://artifacts.apis.io/leadping/scopes/leadping-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/leadping-scopes.yml
- group: company
  title: ''
  type: Blog
  url: https://leadping.ai/blog
- group: start
  href: https://artifacts.apis.io/leadping/sandbox/leadping-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/leadping-sandbox.yml
- group: start
  title: ''
  type: Console
  url: https://leadping.ai/docs/api-reference
created: '2026-08-18'
description: Leadping is a lead-management and responsible-outreach platform for teams that need to move a new inbound lead from source to first touch without stitching together separate tools. It captures leads from approved sources, routes and assigns them, runs follow-up automations, sends SMS and MMS, places and transfers calls, keeps conversation and event history together, enforces recipient suppression and opt-out handling, tracks A2P 10DLC carrier registration and phone-number warmup, requires TrustedForm consent evidence where a source needs it, and reports usage, billing and analytics. The 137-operation REST API is published as an OpenAPI 3.1.1 contract with six Kiota-generated first-party SDKs, two remote MCP servers, Standard Webhooks signing, and an unusually complete machine-readable discovery surface including APIs.json, an RFC 9727 API catalog, RFC 9728 protected-resource metadata, llms.txt and an agent-skill index.
finops:
- has_sources: true
  method: derived
  name: Leadping Finops
  primary_unit: workspace
  service_category: ''
  slug: leadping-finops
  template: false
image: https://leadping.ai/img/favicon/leadpinglogo1024x1024.png
layout: provider
mcp_servers:
- description: 'Leadping operates TWO remote MCP servers: a public read-only documentation server at https://leadping.ai/docs/mcp (Mintlify-hosted, anonymous tools/list succeeds) and an authenticated organization-too'
  name: Leadping MCP Server
  slug: leadping-mcp-yml
- description: ''
  name: Leadping MCP Server
  slug: mcp
modified: '2026-09-03'
name: Leadping
nav: Providers
network: true
overview: 'Leadping publishes 31 API contracts indexed on the [APIs.io](https://apis.io/) network, including Analytics API, Automations API, Call Events API, and 28 more. Tagged areas include Lead Management, Sales & marketing automation, SMS Messaging, A2P 10DLC, and CPaaS.


  The Leadping catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Leadping''s developer surface includes documentation, API reference, getting-started guide, support, pricing, signup flow, changelog, and 43 more developer resources.'
plans:
- name: Leadping Plans Pricing
  plan_count: 9
  slug: leadping-plans-pricing
- name: Leadping Price Estimates
  plan_count: 0
  slug: leadping-price-estimates
random_paper: 20
rate_limits:
- limit_count: 4
  name: Leadping Rate Limits
  slug: leadping-rate-limits
rules:
- authorship: generated
  effective_rule_count: 121
  extends:
  - spectral:oas
  name: Leadping API Rules
  rule_count: 80
  severity_counts:
    error: 57
    hint: 0
    info: 4
    warn: 19
  slug: leadping-rules
scopes:
- name: Leadping Scopes
  scope_count: 4
  slug: leadping-scopes
  summary_line: 4 scopes
score:
  band: exemplar
  composite: 82.1
  coverage:
    artifact_dirs: 33
    catalog_earned: 73.0
    catalog_earned_first_party: 24.0
    catalog_gap: 42.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.4
  facets:
    access_clarity: 100.0
    contract_governance: 45.5
    contract_quality: 69.2
    developer_ergonomics: 73.2
    discoverability: 85.0
    operational_transparency: 76.3
  previous_composite: 80.7
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 89.7
      total: 29
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 48.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 27.8
screenshot: https://apis.io/screenshots/leadping/leadping-2026-09-02T150226.png
security:
- kind: authentication
  name: Leadping Authentication
  slug: leadping-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Leadping Domain Security
  slug: leadping-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Leadping Vulnerability Disclosure
  slug: leadping-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Leadping Trust Center
  slug: leadping-trust-center
  summary_line: trust center published
skill_count: 4
skills:
- name: leadping-first-response-sms
  slug: leadping-first-response-sms
- name: leadping-lead-intake
  slug: leadping-lead-intake
- name: leadping-lead-lifecycle
  slug: leadping-lead-lifecycle
- name: leadping-suppression-optout
  slug: leadping-suppression-optout
slug: leadping
tags:
- Lead Management
- Sales & marketing automation
- SMS Messaging
- A2P 10DLC
- CPaaS
- Communications
- Voice/calling
- Compliance & consent
- Agent-Native
- MCP
- Lead intake
- Conversations
- Automation
- Suppression & opt-out
- Webhook
- A2A
website: https://leadping.ai/
---
