---
access_model:
  confidence: high
  label: Self-serve signup with a 14-day free trial
  onboarding: self-serve
  pricing: paid
  public: true
  source:
  - https://www.lemlist.com/pricing
  - https://app.lemlist.com/create-account
  trial: true
  try_now: false
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
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: mostly
    pagination_ratio: partial
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 65.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 86
  human_in_the_loop: 0
  name: Lemlist Agentic Access
  operation_count: 153
  slug: lemlist-agentic-access
  summary_line: 153 operations · 86 acting
api_count: 2
apis:
- description: lemlist's hosted remote Model Context Protocol server. An MCP client POSTs to https://app.lemlist.com/mcp and authenticates with OAuth 2.1 (authorization code + PKCE, dynamic client registration) or a
  name: lemlist MCP Server
  slug: mcp-server
- baseURL: https://api.lemlist.com/api
  baseurl_source: declared
  description: Campaign CRUD and lifecycle - create, update, duplicate, start, pause, validation statutes, stats, reports and asynchronous exports.
  name: lemlist Campaigns API
  phrasing_intents:
  - id: getCampaigns
    intent: List my campaigns
    question: Which outreach campaigns do I have in lemlist right now?
  - id: postCampaigns
    intent: Create a new campaign
    question: How do I start a brand-new outreach campaign from scratch?
  - id: getCampaignsByCampaignId
    intent: Get one campaign's details
    question: Where can I see the full details of a single campaign?
  - id: patchCampaignsByCampaignId
    intent: Update a campaign's settings
    question: Can I make a campaign stop sending once a lead books a meeting?
  - id: postCampaignsByCampaignIdPause
    intent: Pause a running campaign
    question: How do I temporarily stop a campaign from sending?
  - id: getCampaignsByCampaignIdExportStart
    intent: Start an export of campaign stats
    question: How do I kick off an asynchronous export of a campaign's statistics?
  - id: getCampaignsByCampaignIdExportByExportIdStatus
    intent: Check the status of a campaign export
    question: Is my campaign stats export finished yet?
  - id: getCampaignsReports
    intent: Get reports for several campaigns
    question: Can I pull a summary report across multiple campaigns at once?
  phrasing_ops: 15
  slug: lemlist-campaigns-api
- baseURL: https://api.lemlist.com/api
  baseurl_source: declared
  description: Campaign sequences, their steps, and A/B test variants on email steps.
  name: lemlist Sequences API
  phrasing_intents:
  - id: getCampaignsByCampaignIdSequences
    intent: Get a campaign's sequences and steps
    question: What steps make up a campaign's outreach sequence?
  - id: postSequencesBySequenceIdSteps
    intent: Add a step to a sequence
    question: How do I add another follow-up step to a sequence?
  - id: patchSequencesBySequenceIdStepsByStepId
    intent: Edit a sequence step
    question: How do I change the content or delay of an existing step?
  - id: deleteSequencesBySequenceIdStepsByStepId
    intent: Delete a step from a sequence
    question: Can I remove one step from a campaign's sequence?
  - id: postSequencesBySequenceIdStepsByStepIdAbTest
    intent: Start an A/B test on an email step
    question: How do I split-test two versions of an email step?
  - id: getSequencesBySequenceIdStepsByStepIdAbTest
    intent: Get the B variant of an email A/B test
    question: What subject and message is variant B using in my A/B test?
  - id: patchSequencesBySequenceIdStepsByStepIdAbTest
    intent: Edit variant B of an A/B test
    question: Can I change the subject line of my A/B test's B version?
  - id: deleteSequencesBySequenceIdStepsByStepIdAbTest
    intent: End an A/B test by deleting a variant
    question: How do I stop an A/B test and keep only one version?
  phrasing_ops: 9
  slug: lemlist-sequences-api
- baseURL: https://api.lemlist.com/api
  baseurl_source: declared
  description: Leads inside campaigns - create with optional enrichment, update, pause, resume, mark interested, custom variables, CRM import and unsubscribe.
  name: lemlist Leads API
  phrasing_intents:
  - id: postLeadsStartByLeadId
    intent: Resume a paused lead
    question: How do I let a paused lead continue through the campaign sequence?
  - id: postLeadsPauseByLeadId
    intent: Pause a lead's sequence
    question: Can I stop sending to one lead while the campaign keeps running?
  - id: postLeadsInterestedByLeadIdOrEmail
    intent: Mark a lead interested in all campaigns
    question: How do I flag a lead as interested across every campaign they're in?
  - id: postLeadsNotinterestedByLeadIdOrEmail
    intent: Mark a lead not interested in all campaigns
    question: How do I record that a prospect said no, across all campaigns?
  - id: postCampaignsByCampaignIdLeadsByLeadIdOrEmailInterested
    intent: Mark a lead interested in one campaign
    question: Can I mark a lead interested in just one campaign and not the others?
  - id: postCampaignsByCampaignIdLeadsByLeadIdOrEmailNotinterested
    intent: Mark a lead not interested in one campaign
    question: Can I mark a lead not interested for one campaign while keeping them in others?
  - id: getLeadsByEmail
    intent: Look up a lead by email in the path
    question: Which campaigns is a given email address enrolled in as a lead?
  - id: getLeads
    intent: Look up a lead by id or email query
    question: How do I retrieve a lead when I only have its lead id?
  phrasing_ops: 22
  slug: lemlist-leads-api
- baseURL: https://api.lemlist.com/api
  baseurl_source: declared
  description: Search the lemlist B2B people and company database, list its filters, and manage saved personas.
  name: lemlist People Database API
  phrasing_intents:
  - id: getDatabaseFilters
    intent: List the filters the People Database supports
    question: Which filter ids can I use when searching the lemlist People Database?
  - id: postDatabasePeople
    intent: Search the People Database for prospects
    question: How do I search for people matching my ideal customer profile?
  - id: getSchemaPeople
    intent: Get the field schema for people records
    question: What fields come back on a person record from the People Database?
  - id: postDatabaseCompanies
    intent: Search the database for companies
    question: How do I look up companies that match my target account criteria?
  - id: getSchemaCompanies
    intent: Get the field schema for company records
    question: What fields does a company record in the database contain?
  - id: listPersonas
    intent: List my team's saved personas
    question: Which personas has my team saved in the lemlist People Database?
  - id: createPersona
    intent: Save a new persona from database filters
    question: How do I save a set of People Database filters as a reusable persona?
  - id: deletePersona
    intent: Permanently delete a saved persona
    question: Can I remove a persona my team no longer uses?
  phrasing_ops: 8
  slug: lemlist-people-database-api
- baseURL: https://api.lemlist.com/api
  baseurl_source: declared
  description: Asynchronous enrichment - find and verify emails, phone numbers and LinkedIn data, single or in bulk, then poll for the result. Credit-metered.
  name: lemlist Enrich API
  phrasing_intents:
  - id: getEnrichByEnrichId
    intent: Get the result of an enrichment request
    question: Has my enrichment request finished, and what did it find?
  - id: postEnrich
    intent: Enrich a person who isn't a lead
    question: How do I find a verified email for someone from their name and company domain?
  - id: postLeadsByLeadIdEnrich
    intent: Enrich an existing campaign lead
    question: How do I find the phone number for a lead already in my campaign?
  - id: postV2EnrichmentsBulk
    intent: Enrich many people in one bulk request
    question: Can I submit a whole batch of people for enrichment at once?
  phrasing_ops: 4
  slug: lemlist-enrich-api
- baseURL: https://api.lemlist.com/api
  baseurl_source: declared
  description: The unified reply inbox - conversations, messages, drafts, labels and sending on email, LinkedIn and WhatsApp.
  name: lemlist Inbox API
  phrasing_intents:
  - id: getInbox
    intent: List my inbox conversations
    question: Which conversations are waiting in my lemlist unified inbox?
  - id: getInboxByContactId
    intent: Read the message thread with a contact
    question: How do I read the full conversation history with one contact?
  - id: postInboxEmail
    intent: Send an email to a contact from the inbox
    question: How do I send a one-off email reply to a lead from the inbox?
  - id: postInboxLinkedin
    intent: Send a LinkedIn message to a contact
    question: Can I send a LinkedIn DM to a lead through the API?
  - id: postInboxWhatsapp
    intent: Send a WhatsApp message to a contact
    question: Is it possible to text a prospect on WhatsApp from lemlist?
  - id: getInboxLabels
    intent: List my team's inbox labels
    question: What labels can I use to tag inbox conversations?
  - id: postInboxLabels
    intent: Create an inbox label
    question: How do I add a new label for sorting conversations?
  - id: getInboxLabelsByLabelId
    intent: Get details of one inbox label
    question: What's stored on a particular inbox label?
  phrasing_ops: 15
  slug: lemlist-inbox-api
- baseURL: https://api.lemlist.com/api
  baseurl_source: declared
  description: CRM-side contacts, contact lists, list membership and exports.
  name: lemlist Contacts API
  phrasing_intents:
  - id: getContactsByIdOrEmail
    intent: Look up one contact by id or email
    question: Can I pull up a single contact using just their email address?
  - id: deleteContactsByIdOrEmail
    intent: Delete a contact and everything tied to it
    question: What else gets removed when I delete a contact, like their leads and conversations?
  - id: getContacts
    intent: List all my contacts
    question: Which contacts are in my lemlist CRM?
  - id: postContacts
    intent: Create or update a contact
    question: How do I add a person, or update them if their email already exists?
  - id: getContactsLists
    intent: List my contact lists
    question: Which static and dynamic contact lists does my team have?
  - id: postContactsLists
    intent: Create a static contact list
    question: How do I make a new static list to group contacts?
  - id: postContactsListsByListIdEntities
    intent: Add or remove contacts in a static list
    question: How do I put existing contacts into a static list?
  - id: getContactsExport
    intent: Export a contact list as CSV
    question: How do I download a CRM list of contacts as a CSV file?
  phrasing_ops: 8
  slug: lemlist-contacts-api
- baseURL: https://api.lemlist.com/api
  baseurl_source: declared
  description: CRM-side companies and company notes.
  name: lemlist Companies API
  phrasing_intents:
  - id: getCompanies
    intent: List or search my companies
    question: Which companies are stored in my lemlist account?
  - id: postCompanies
    intent: Create or update a company
    question: How do I add a company, or update it if its domain already exists?
  - id: postCompaniesByCompanyIdNotes
    intent: Add a note to a company
    question: How do I attach a note to a company record?
  - id: getCompaniesByCompanyIdNotes
    intent: List a company's notes
    question: Where can I read the notes my team left on a company?
  - id: deleteCompaniesByCompanyId
    intent: Delete a company
    question: Can I delete a company that still has contacts attached to it?
  phrasing_ops: 5
  slug: lemlist-companies-api
- baseURL: https://api.lemlist.com/api
  baseurl_source: declared
  description: Signal Agents (watch lists) - create and configure watches, list the available signal types and filters, read detected signals, and push external signals.
  name: lemlist Signal Agents API
  phrasing_intents:
  - id: getWatchlistSignals
    intent: Get signals detected by my Signal Agents
    question: What buying signals have my Signal Agents picked up this week?
  - id: postWatchlistByWatchListIdExternalSignals
    intent: Push an external signal into a Signal Agent
    question: How do I feed signals from my own tools into a lemlist Signal Agent?
  - id: getWatchlist
    intent: List my Signal Agents
    question: Which Signal Agents has my team set up?
  - id: postWatchlist
    intent: Create a Signal Agent
    question: How do I set up an agent that watches for a particular buying signal?
  - id: patchWatchlist
    intent: Update a Signal Agent
    question: Can I rename a Signal Agent or change its emoji?
  - id: deleteWatchlist
    intent: Delete a Signal Agent
    question: How do I delete a Signal Agent I don't need anymore?
  - id: getWatchlistHistory
    intent: See a Signal Agent's configuration history
    question: Who changed my Signal Agent's settings, and when?
  - id: getWatchlistLibrary
    intent: List the signal types I can monitor
    question: What kinds of signals can a lemlist Signal Agent watch for?
  phrasing_ops: 10
  slug: lemlist-signal-agents-api
- baseURL: https://api.lemlist.com/api
  baseurl_source: declared
  description: Webhook subscription management - list, create with an optional shared secret, and delete. 76 event types are documented.
  name: lemlist Webhooks API
  phrasing_intents:
  - id: getHooks
    intent: List my webhooks
    question: Which webhooks are currently registered on my lemlist team?
  - id: postHooks
    intent: Register a webhook for activity events
    question: How do I get notified at my URL when a lead replies or opens an email?
  - id: deleteHooksByHookId
    intent: Delete a webhook
    question: How do I stop a webhook from sending events?
  phrasing_ops: 3
  slug: lemlist-webhooks-api
- baseURL: https://api.lemlist.com/api
  baseurl_source: declared
  description: Suppression management - unsubscribe and re-subscribe contacts and variables, list and export the suppression set, and the legacy email/domain surface.
  name: lemlist Unsubscribes API
  phrasing_intents:
  - id: getUnsubscribes
    intent: List unsubscribes via the trailing-slash route
    question: Is there an older trailing-slash route that lists unsubscribed emails?
  - id: getUnsubsExport
    intent: Export unsubscribes with the legacy export route
    question: Can I download my unsubscribe list through the original unsubs export?
  - id: getUnsubscribesJohnDoe@domainCom
    intent: Check the sample john.doe@domain.com unsubscribe
    question: What does the documentation example for checking john.doe@domain.com return?
  - id: postUnsubscribesJohnDoe@domainCom
    intent: Unsubscribe the sample john.doe@domain.com
    question: What happens when I call the documentation example that unsubscribes john.doe@domain.com?
  - id: deleteUnsubscribesJohnDoe@domainCom
    intent: Remove the sample john.doe@domain.com unsubscribe
    question: How does the documentation example for removing john.doe@domain.com from unsubscribes behave?
  - id: getUnsubscribes
    intent: List unsubscribed emails
    question: Which email addresses have unsubscribed from my campaigns?
  - id: getV2UnsubscribesVariables
    intent: List unsubscribed emails, domains, URLs and phones
    question: Which domains, LinkedIn URLs and phone numbers are on my do-not-contact list?
  - id: postV2UnsubscribesVariables
    intent: Bulk-unsubscribe up to 10,000 values
    question: How do I upload a big suppression list of emails and domains at once?
  phrasing_ops: 19
  slug: lemlist-unsubscribes-api
- baseURL: https://api.lemlist.com/api
  baseurl_source: declared
  description: Sending schedules - CRUD and association with campaigns.
  name: lemlist Schedules API
  phrasing_intents:
  - id: getSchedules
    intent: List my sending schedules
    question: Which sending schedules exist in my lemlist team?
  - id: postSchedules
    intent: Create a sending schedule
    question: How do I set up a schedule so emails only go out on weekdays during business hours?
  - id: getSchedulesByScheduleId
    intent: Get one sending schedule
    question: What hours and days does a particular schedule send on?
  - id: patchSchedulesByScheduleId
    intent: Edit a sending schedule
    question: How do I change the timezone of an existing schedule?
  - id: deleteSchedulesByScheduleId
    intent: Delete a sending schedule
    question: Can I delete a schedule I no longer use?
  - id: getCampaignsByCampaignIdSchedules
    intent: List the schedules used by a campaign
    question: Which sending schedule is a campaign using?
  - id: postCampaignsByCampaignIdSchedulesByScheduleId
    intent: Assign a schedule to a campaign
    question: How do I apply an existing schedule to one of my campaigns?
  phrasing_ops: 7
  slug: lemlist-schedules-api
- baseURL: https://api.lemlist.com/api
  baseurl_source: declared
  description: Manual tasks - list, create, update and ignore.
  name: lemlist Tasks API
  phrasing_intents:
  - id: getTasks
    intent: List my tasks
    question: What manual tasks are waiting for me in lemlist?
  - id: postTasks
    intent: Create a task for a lead
    question: How do I create a follow-up task tied to a specific lead?
  - id: patchTasks
    intent: Update existing tasks
    question: Can I mark a task as done or change its due date?
  - id: postTasksIgnore
    intent: Ignore tasks
    question: Is there a way to skip tasks I don't intend to do?
  phrasing_ops: 4
  slug: lemlist-tasks-api
- baseURL: https://api.lemlist.com/api
  baseurl_source: declared
  description: The activity history feed, and deletion of call recordings and transcripts.
  name: lemlist Activities API
  phrasing_intents:
  - id: getActivities
    intent: Retrieve activities with the original v1 endpoint
    question: Can I still pull campaign activities through the older v1 activities endpoint?
  - id: getActivities
    intent: Get campaign activities within a date range
    question: How do I see every email open, reply and click logged in lemlist between two dates?
  - id: deleteActivitiesByActivityIdRecordingTranscript
    intent: Delete a call recording and its transcript
    question: Can I remove the recording and transcript attached to a call activity?
  phrasing_ops: 3
  slug: lemlist-activities-api
- baseURL: https://api.lemlist.com/api
  baseurl_source: declared
  description: Team-level endpoints - team information, senders, remaining credits and CRM users.
  name: lemlist Team API
  phrasing_intents:
  - id: getTeam
    intent: Get my team's details
    question: What team is my lemlist API key attached to?
  - id: getTeamSenders
    intent: List senders and their campaigns
    question: Which teammates are sending which campaigns?
  - id: getTeamCredits
    intent: Check my team's remaining credits
    question: How many enrichment credits does my team have left?
  - id: getTeamCrmUsers
    intent: List team members' connected CRMs
    question: Which CRMs have my teammates connected to lemlist?
  phrasing_ops: 4
  slug: lemlist-team-api
- baseURL: https://api.lemlist.com/api
  baseurl_source: declared
  description: User endpoints - user detail and the connected channels available to the authenticated user.
  name: lemlist Users API
  phrasing_intents:
  - id: getUsersByUserId
    intent: Get a user's profile
    question: How can I look up a teammate's lemlist user record by id?
  - id: getUserChannels
    intent: List my connected outreach channels
    question: Which channels like email, LinkedIn or WhatsApp have I connected?
  phrasing_ops: 2
  slug: lemlist-users-api
- baseURL: https://api.lemlist.com/api
  baseurl_source: declared
  description: Connect, test and disconnect custom SMTP/IMAP sending accounts.
  name: lemlist Email Accounts API
  phrasing_intents:
  - id: postUserEmailAccounts
    intent: Connect an SMTP/IMAP email account
    question: How do I connect a custom mailbox to lemlist using SMTP and IMAP settings?
  - id: deleteUserEmailAccountsByEmailAccountId
    intent: Disconnect an email account
    question: How do I disconnect a mailbox I no longer send from?
  - id: postUserEmailAccountsByEmailAccountIdTest
    intent: Test a connected email account
    question: Is my connected mailbox's SMTP and IMAP connection still working?
  phrasing_ops: 3
  slug: lemlist-email-accounts-api
- baseURL: https://api.lemlist.com/api
  baseurl_source: declared
  description: lemwarm mailbox warm-up - start, pause, and read or update warm-up settings per mailbox.
  name: lemlist Lemwarm API
  phrasing_intents:
  - id: postLemwarmByUserMailboxIdStart
    intent: Start lemwarm on a mailbox
    question: How do I turn on email warm-up for a new mailbox?
  - id: postLemwarmByUserMailboxIdPause
    intent: Pause lemwarm on a mailbox
    question: Can I temporarily stop warm-up emails from a mailbox?
  - id: getLemwarmByUserMailboxIdSettings
    intent: Get a mailbox's lemwarm settings
    question: How many warm-up emails per day is my mailbox set to send?
  - id: patchLemwarmByUserMailboxIdSettings
    intent: Change a mailbox's lemwarm volume
    question: Can I raise the daily maximum of warm-up emails on a mailbox?
  phrasing_ops: 4
  slug: lemlist-lemwarm-api
- baseURL: https://api.lemlist.com/api
  baseurl_source: declared
  description: Threshold alerts on deliverability metrics - create, read, update and delete.
  name: lemlist Deliverability Alerts API
  phrasing_intents:
  - id: getDeliverabilityAlerts
    intent: List my deliverability alerts
    question: Which deliverability alerts have I configured for my mailboxes?
  - id: postDeliverabilityAlerts
    intent: Create a deliverability alert
    question: How do I get notified when a mailbox's bounce rate crosses a threshold?
  - id: getDeliverabilityAlertsByAlertId
    intent: Get one deliverability alert
    question: What exactly does a particular deliverability alert check for?
  - id: patchDeliverabilityAlertsByAlertId
    intent: Update or pause a deliverability alert
    question: How do I change the threshold on an existing deliverability alert?
  - id: deleteDeliverabilityAlertsByAlertId
    intent: Delete a deliverability alert
    question: Can I get rid of a deliverability alert I no longer need?
  phrasing_ops: 5
  slug: lemlist-deliverability-alerts-api
- baseURL: https://api.lemlist.com/api
  baseurl_source: declared
  description: The custom field definitions available on leads, contacts and companies.
  name: lemlist Fields API
  phrasing_intents:
  - id: getFields
    intent: List available custom and standard fields
    question: Which fields can I store on contacts and companies in lemlist?
  phrasing_ops: 1
  slug: lemlist-fields-api
- baseURL: https://app.lemlist.com/mcp
  baseurl_source: declared
  description: The Stats API from lemlist — 2 operation(s) for stats.
  name: lemlist Stats API
  phrasing_intents:
  - id: getCampaignsByCampaignIdStats
    intent: Get a campaign's stats (original version)
    question: Can I still get campaign stats from the original v1 endpoint with a timezone?
  - id: getV2CampaignsByCampaignIdStats
    intent: Get a campaign's stats by channel and A/B version
    question: How do I break down a campaign's v2 stats by sender or channel?
  phrasing_ops: 2
  slug: lemlist-stats-api
artifact_total: 43
asyncapis:
- description: ''
  name: Lemlist Webhooks
  slug: lemlist-webhooks
collections:
- collection_type: open
  name: lemlist Campaigns API
  slug: open-lemlist-campaigns-api
- collection_type: open
  name: lemlist Campaigns Team API
  slug: open-lemlist-team-api
- collection_type: open
  name: lemlist Campaigns Users API
  slug: open-lemlist-users-api
- collection_type: open
  name: lemlist API
  slug: open-lemlist
common:
- group: other
  href: https://artifacts.apis.io/lemlist/capabilities/lemlist-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/lemlist-capability-edges.yml
- group: company
  title: ''
  type: Website
  url: https://www.lemlist.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.lemlist.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.lemlist.com
- group: docs
  title: ''
  type: APIReference
  url: https://developer.lemlist.com/api-reference/getting-started/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.lemlist.com/api-reference/getting-started/overview
- group: operate
  title: ''
  type: Support
  url: https://help.lemlist.com
- group: company
  title: ''
  type: Blog
  url: https://www.lemlist.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/l3mpire
- group: commercial
  title: ''
  type: Pricing
  url: https://www.lemlist.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.lemlist.com/create-account
- group: start
  title: ''
  type: Login
  url: https://app.lemlist.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.lemlist.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.lemlist.com/legal/privacy-policy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/lemlist
- group: commercial
  href: https://artifacts.apis.io/lemlist/plans/lemlist-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/lemlist-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/lemlist/rate-limits/lemlist-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/lemlist-rate-limits.yml
- group: auth
  href: https://artifacts.apis.io/lemlist/authentication/lemlist-authentication.yml
  title: ''
  type: Authentication
  url: authentication/lemlist-authentication.yml
- group: auth
  href: https://artifacts.apis.io/lemlist/scopes/lemlist-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/lemlist-scopes.yml
- group: design
  href: https://artifacts.apis.io/lemlist/conventions/lemlist-conventions.yml
  title: ''
  type: Conventions
  url: conventions/lemlist-conventions.yml
- group: design
  href: https://artifacts.apis.io/lemlist/errors/lemlist-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/lemlist-problem-types.yml
- group: design
  href: https://artifacts.apis.io/lemlist/data-model/lemlist-data-model.yml
  title: ''
  type: DataModel
  url: data-model/lemlist-data-model.yml
- group: build
  href: https://artifacts.apis.io/lemlist/examples/lemlist-examples.yml
  title: ''
  type: Examples
  url: examples/lemlist-examples.yml
- group: other
  href: https://artifacts.apis.io/lemlist/overlays/lemlist-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/lemlist-api-overlay.yaml
- group: design
  href: https://artifacts.apis.io/lemlist/lifecycle/lemlist-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/lemlist-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.lemlist.com
- group: operate
  title: ''
  type: Deprecation
  url: https://developer.lemlist.com/api-reference/getting-started/version
- group: design
  href: https://artifacts.apis.io/lemlist/conformance/lemlist-conformance.yml
  title: ''
  type: Conformance
  url: conformance/lemlist-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.lemlist.com/
- group: auth
  href: https://artifacts.apis.io/lemlist/security/lemlist-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/lemlist-trust-center.yml
- group: auth
  title: ''
  type: Security
  url: https://hackerone.com/lemlist
- group: auth
  href: https://artifacts.apis.io/lemlist/security/lemlist-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/lemlist-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/lemlist/security/lemlist-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/lemlist-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/lemlist/well-known/lemlist-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/lemlist-well-known.yml
- group: design
  href: https://artifacts.apis.io/lemlist/asyncapi/lemlist-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/lemlist-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/lemlist/mcp/lemlist-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/lemlist-mcp.yml
- group: other
  href: https://artifacts.apis.io/lemlist/a2a/lemlist-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/lemlist-a2a.yml
- group: agent
  href: https://artifacts.apis.io/lemlist/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/lemlist/agentic-access/lemlist-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/lemlist-agentic-access.yml
- group: build
  href: https://artifacts.apis.io/lemlist/packages/lemlist-packages.yml
  title: ''
  type: Packages
  url: packages/lemlist-packages.yml
- group: build
  href: https://artifacts.apis.io/lemlist/packages/lemlist-packages.yml
  title: ''
  type: SDKs
  url: packages/lemlist-packages.yml
- group: build
  href: https://artifacts.apis.io/lemlist/cli/lemlist-cli.yml
  title: ''
  type: CLI
  url: cli/lemlist-cli.yml
- group: agent
  href: https://artifacts.apis.io/lemlist/llms/lemlist-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/lemlist-llms.txt
- group: agent
  title: ''
  type: LlmsText
  url: https://developer.lemlist.com/llms.txt
created: '2026-05-11'
description: lemlist is a sales engagement and cold outreach platform from lempire that helps sales teams build prospect lists, personalize multichannel campaigns across email, LinkedIn, phone, SMS and WhatsApp, and automate follow-ups to book more meetings. It includes a 650M+ record B2B lead database, credit-metered email and phone enrichment, Signal Agents that watch for buying triggers, a unified reply inbox, and lemwarm deliverability warm-up. The developer surface is unusually agent-forward for its category - a 143-operation REST API documented with a published OpenAPI, a hosted remote MCP server at app.lemlist.com/mcp with OAuth 2.1 and dynamic client registration, an official OpenAPI-generated CLI on npm, an llms.txt index, a published Agent Skill, and a 76-event webhook catalog.
examples:
- key_count: 143
  name: Lemlist Examples
  slug: lemlist-examples
finops:
- has_sources: true
  method: derived
  name: Lemlist Finops
  primary_unit: unlimited users
  service_category: ''
  slug: lemlist-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/lemlist.png
layout: provider
mcp_servers:
- description: Remote MCP server at app.lemlist.com over HTTP requiring OAuth; 30 tools listed.
  name: lemlist MCP Server
  slug: lemlist
modified: '2026-08-13'
name: lemlist
nav: Providers
network: true
overview: 'lemlist publishes 22 API contracts indexed on the [APIs.io](https://apis.io/) network, including Campaigns API, Sequences API, Leads API, and 19 more. Tagged areas include Email Outreach, Sales Engagement, Cold Email, Sales Automation, and LinkedIn Outreach.


  The lemlist catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  lemlist''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 37 more developer resources.'
plans:
- name: Lemlist Plans Pricing
  plan_count: 5
  slug: lemlist-plans-pricing
- name: Lemlist Price Estimates
  plan_count: 0
  slug: lemlist-price-estimates
random_paper: 18
rate_limits:
- limit_count: 1
  name: Lemlist Rate Limits
  slug: lemlist-rate-limits
rules:
- authorship: generated
  effective_rule_count: 89
  extends:
  - spectral:oas
  name: lemlist API Rules
  rule_count: 48
  severity_counts:
    error: 34
    hint: 0
    info: 1
    warn: 13
  slug: lemlist-rules
scopes:
- name: Lemlist Scopes
  scope_count: 14
  slug: lemlist-scopes
  summary_line: 14 scopes · authorizationCode
score:
  band: exemplar
  composite: 76.0
  coverage:
    artifact_dirs: 33
    catalog_earned: 64.5
    catalog_earned_first_party: 20.0
    catalog_gap: 50.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 93.4
    contract_governance: 31.8
    contract_quality: 55.9
    developer_ergonomics: 78.6
    discoverability: 75.0
    operational_transparency: 57.9
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - france
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 76.0
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 21
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
    score: 45.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 50.0
screenshot: https://apis.io/screenshots/lemlist/lemlist-2026-06-20T184417.png
security:
- kind: authentication
  name: Lemlist Authentication
  slug: lemlist-authentication
  summary_line: http/apiKey/oauth2/openIdConnect · 4 schemes
- kind: domain-security
  name: Lemlist Domain Security
  slug: lemlist-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Lemlist Vulnerability Disclosure
  slug: lemlist-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Lemlist Trust Center
  slug: lemlist-trust-center
  summary_line: SOC 2 Type 2
skill_count: 3
skills:
- name: lemlist-enrich-and-sync
  slug: lemlist-enrich-and-sync
- name: lemlist-launch-campaign
  slug: lemlist-launch-campaign
- name: lemlist-monitor-and-reply
  slug: lemlist-monitor-and-reply
slug: lemlist
tags:
- Email Outreach
- Sales Engagement
- Cold Email
- Sales Automation
- LinkedIn Outreach
- Lead Generation
- Data Enrichment
- Deliverability
- CRM
- Multichannel Messaging
- Webhook
- MCP
- A2A
website: https://www.lemlist.com
---
