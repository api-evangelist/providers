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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 35.9
  scored_at: '2026-10-04'
agentic_access:
- acting_count: 294
  human_in_the_loop: 11
  name: Zendesk Agentic Access
  operation_count: 595
  slug: zendesk-agentic-access
  summary_line: 595 operations · 294 acting · 11 human-in-the-loop
api_count: 76
apis:
- description: The Zendesk Help Center Articles API lets you programmatically manage knowledge base articles in your Help Center. You can create, read, update, and delete articles, manage their translations, set use
  name: Zendesk Help Center Articles API
  slug: help-center-articles
- description: The Zendesk Help Center Sections API lets you create, read, update, and delete sections within your Help Center categories. Sections organize articles into logical groups and support multiple translat
  name: Zendesk Help Center Sections API
  slug: help-center-sections
- description: The Zendesk Help Center Categories API lets you programmatically manage the top-level organizational structure of your knowledge base. You can create, read, update, and delete categories, specify name
  name: Zendesk Help Center Categories API
  slug: help-center-categories
- description: The Zendesk Help Center Translations API lets you manage multilingual content for articles, sections, and categories. You can create, read, update, and delete translations for Help Center content, lis
  name: Zendesk Help Center Translations API
  slug: help-center-translations
- description: The Zendesk Help Center Article Attachments API lets you manage file attachments associated with Help Center articles. You can upload new attachments, list existing ones for an article, and delete att
  name: Zendesk Help Center Article Attachments API
  slug: help-center-article-attachments
- description: The Zendesk Help Center Article Comments API lets you manage comments on knowledge base articles. Users can provide feedback by adding comments to articles, and the API provides endpoints to list, cre
  name: Zendesk Help Center Article Comments API
  slug: help-center-article-comments
- description: The Zendesk Help Center Article Labels API lets you manage the labels applied to knowledge base articles. Labels help categorize and organize articles for easier discovery. You can list labels on an a
  name: Zendesk Help Center Article Labels API
  slug: help-center-article-labels
- description: The Zendesk Help Center Topics API lets you manage community discussion topics in your Help Center. A topic represents a collection of community posts on a subject. You can create, read, update, and d
  name: Zendesk Help Center Topics API
  slug: help-center-topics
- description: The Zendesk Help Center Posts API lets you manage community posts within Help Center topics. You can list all posts, all posts in a given topic, or all posts by a specific user. The API provides endpo
  name: Zendesk Help Center Posts API
  slug: help-center-posts
- description: The Zendesk Help Center Post Comments API lets you manage comments on community posts. You can list comments on a post, add new comments, update existing comments, and delete comments. This enables pr
  name: Zendesk Help Center Post Comments API
  slug: help-center-post-comments
- description: The Zendesk Help Center Votes API lets you access vote data for knowledge base and community content. You can list all votes cast by a given user, or all votes cast for a given article, article commen
  name: Zendesk Help Center Votes API
  slug: help-center-votes
- description: The Zendesk Help Center Content Subscriptions API lets users subscribe to sections, articles, community posts, and community topics to receive notifications when content is added or updated. Users are
  name: Zendesk Help Center Content Subscriptions API
  slug: help-center-content-subscriptions
- description: The Zendesk Help Center User Segments API lets you manage user segments that control access to Help Center content. User segments define groups of users who can view specific articles, sections, or to
  name: Zendesk Help Center User Segments API
  slug: help-center-user-segments
- description: The Zendesk Help Center Permission Groups API lets you manage which agents can create, update, archive, and publish articles. A management permission group consists of a set of privileges, each mapped
  name: Zendesk Help Center Permission Groups API
  slug: help-center-permission-groups
- description: The Zendesk Help Center Search API provides three different search endpoints for finding content in your knowledge base. The Search Articles and Search Posts endpoints enable you to search for article
  name: Zendesk Help Center Search API
  slug: help-center-search
- description: The Zendesk Talk API is the reference API for managing Zendesk voice capabilities. It provides endpoints for managing phone numbers, digital lines, greetings, greeting categories, IVRs, IVR routes and
  name: Zendesk Talk API
  slug: talk
- description: The Zendesk Talk Phone Numbers API lets you manage the phone numbers in your Zendesk voice account. You can list existing phone numbers, search for available numbers to purchase, and manage phone numb
  name: Zendesk Talk Phone Numbers API
  slug: talk-phone-numbers
- description: 'The Zendesk Talk Greetings API lets you manage the greetings used in your Zendesk voice account. Zendesk provides default greetings, but you can replace them with custom greetings by uploading mp3 or '
  name: Zendesk Talk Greetings API
  slug: talk-greetings
- description: 'The Zendesk Talk IVRs API lets you manage Interactive Voice Response systems that use keypad tones to route customers to the right agent or department, provide recorded responses for frequently asked '
  name: Zendesk Talk IVRs API
  slug: talk-ivrs
- description: The Zendesk Talk Recordings API lets you manage call recordings stored by Talk. Recordings are exposed in the corresponding ticket in a voice comment. The API provides endpoints to retrieve and delete
  name: Zendesk Talk Recordings API
  slug: talk-recordings
- description: The Zendesk Talk Stats API provides access to call statistics and current queue activity for your voice account. You can retrieve agent overview metrics including average talk time, available time, an
  name: Zendesk Talk Stats API
  slug: talk-stats
- description: The Zendesk Talk Availabilities API lets you manage and query agent availability for voice calls. It provides information about agent state, call status, and connection method, enabling real-time moni
  name: Zendesk Talk Availabilities API
  slug: talk-availabilities
- description: The Zendesk Talk Lines API lets you list the available lines, including both phone numbers and digital lines, in your Zendesk voice account. This provides a unified view of all voice communication cha
  name: Zendesk Talk Lines API
  slug: talk-lines
- description: The Zendesk Talk Digital Lines API lets you manage the digital lines in your Zendesk voice account. Digital lines enable browser-based calling without traditional phone numbers, providing an additiona
  name: Zendesk Talk Digital Lines API
  slug: talk-digital-lines
- description: The Zendesk Talk Voice Settings API lets you view and manage the account settings of your Zendesk voice account. It provides endpoints to retrieve and update configuration options that control how you
  name: Zendesk Talk Voice Settings API
  slug: talk-voice-settings
- description: The Zendesk Talk Partner Edition API includes a Standard Call Object with endpoints to save, read, and update call-related data in Zendesk. It enables telephony partners to integrate their calling sol
  name: Zendesk Talk Partner Edition API
  slug: talk-partner-edition
- description: The Zendesk Chat Accounts API lets you get or set account information for your Zendesk Chat instance. If you created your Zendesk Chat account in Zendesk Support, access to the Chat Accounts and Agent
  name: Zendesk Chat Accounts API
  slug: chat-accounts
- description: The Zendesk Chat Agents API lets you get or set agent information for your Zendesk Chat instance. If you created your Zendesk Chat account in Zendesk Support, access to the Agents API is restricted to
  name: Zendesk Chat Agents API
  slug: chat-agents
- description: The Zendesk Chat Visitors API lets you get or set visitor information for your Zendesk Chat instance. Visitors represent end users who initiate chat sessions through the Zendesk Chat widget on your we
  name: Zendesk Chat Visitors API
  slug: chat-visitors
- description: The Zendesk Chat Chats API provides access to individual chat records with information including agent IDs, agent names, department information, chat history, conversions, and goal attributions. You c
  name: Zendesk Chat Chats API
  slug: chat-chats
- description: The Zendesk Chat Departments API lets you get or set department information for your Chat instance. Departments enable you to route chats to specific groups of agents, configure operating hours, and o
  name: Zendesk Chat Departments API
  slug: chat-departments
- description: The Zendesk Chat Shortcuts API lets you manage canned responses that agents can use during live chat conversations. You can list all shortcuts for the account, create new ones, update existing shortcu
  name: Zendesk Chat Shortcuts API
  slug: chat-shortcuts
- description: The Zendesk Chat Triggers API lets you manage proactive chat triggers that automatically engage visitors based on specified conditions. You can list triggers, add new triggers, update, and delete them
  name: Zendesk Chat Triggers API
  slug: chat-triggers
- description: The Zendesk Chat Bans API lets you manage banned visitors in your Chat account. You can list banned visitors with cursor-based pagination, create new bans, and remove existing bans to control which vi
  name: Zendesk Chat Bans API
  slug: chat-bans
- description: 'The Zendesk Chat Roles API lets you manage agent roles and permissions within your Chat account. You can retrieve role definitions and manage role assignments to control what actions different agents '
  name: Zendesk Chat Roles API
  slug: chat-roles
- description: The Zendesk Chat Skills API lets you manage skills used for routing chats to qualified agents. You can get or set skill information, enabling skills-based routing where chats are directed to agents wi
  name: Zendesk Chat Skills API
  slug: chat-skills
- description: The Zendesk Chat Goals API lets you manage conversion goals for your Chat account. Goals track specific visitor actions such as page visits or purchases that occur during or after a chat session, enab
  name: Zendesk Chat Goals API
  slug: chat-goals
- description: The Zendesk Chat Routing Settings API lets you get or modify chat routing settings for your account. It controls how incoming chats are distributed to available agents based on configured rules and po
  name: Zendesk Chat Routing Settings API
  slug: chat-routing-settings
- description: The Zendesk Real-Time Chat API provides streaming access to real-time chat metrics and activity data. It enables building live dashboards and monitoring tools that display current chat volume, agent a
  name: Zendesk Real-Time Chat API
  slug: real-time-chat
- description: The Zendesk Chat Conversations API lets your application act as a Zendesk Chat agent and interact with customers. It is a GraphQL API that supports WebSocket connections for real-time message exchange
  name: Zendesk Chat Conversations API
  slug: chat-conversations
- baseURL: https://{subdomain}.zendesk.com
  baseurl_source: declared
  description: The Zendesk Webhooks API lets you create, manage, and monitor webhooks that send HTTP requests to specified URLs in response to events in Zendesk. It is the modern replacement for legacy targets, supp
  name: Zendesk Webhooks API
  slug: webhooks
- description: The Zendesk Sell Contacts API provides a simple interface to manage your contacts. A contact represents an individual or an organization. Each contact has customer_status and prospect_status fields de
  name: Zendesk Sell Contacts API
  slug: sell-contacts
- description: The Zendesk Sell Leads API provides a simple interface to manage leads. A lead represents an individual or organization that expresses interest in your goods or services. You can create, read, update,
  name: Zendesk Sell Leads API
  slug: sell-leads
- description: The Zendesk Sell Deals API provides a simple interface to manage deals. You can create, delete, and update deals, retrieve individual deals or lists of all deals. Every deal can have multiple associat
  name: Zendesk Sell Deals API
  slug: sell-deals
- description: The Zendesk Sell Pipelines API provides a read-only interface to your sales pipeline definitions. Sales pipelines consist of a sequence of stages that deals progress through as they move toward closin
  name: Zendesk Sell Pipelines API
  slug: sell-pipelines
- description: The Zendesk Sell Stages API provides read-only access to details of your sales pipeline stages. Stages are key components of a sales pipeline, and each stage can have any number of deals associated wi
  name: Zendesk Sell Stages API
  slug: sell-stages
- description: The Zendesk Sell Tasks API provides a simple interface to manage tasks. A task can be either floating (associated only with a user) or related (associated with a lead, contact, or deal). You can creat
  name: Zendesk Sell Tasks API
  slug: sell-tasks
- description: The Zendesk Sell Notes API provides a simple interface to manage notes. You can create, read, update, and delete notes associated with leads, contacts, and deals in your CRM.
  name: Zendesk Sell Notes API
  slug: sell-notes
- description: The Zendesk Sell Calls API lets you create, read, and delete call records in your CRM. Calls can be associated with leads, contacts, and deals to maintain a complete activity history for your sales te
  name: Zendesk Sell Calls API
  slug: sell-calls
- description: The Zendesk Sell Text Messages API provides read-only access to text messages sent and received within Zendesk Sell. You can retrieve individual messages and list all text messages for reporting and i
  name: Zendesk Sell Text Messages API
  slug: sell-text-messages
- description: The Zendesk Sell Products API lets you manage your product catalog. You can create, read, update, and delete products. To add products to a deal, create an Order and then populate it with Line Items r
  name: Zendesk Sell Products API
  slug: sell-products
- description: The Zendesk Sell Orders API provides a simple interface to manage orders. An order is a list of line items associated with a deal. You can create, read, update, and delete orders to track products and
  name: Zendesk Sell Orders API
  slug: sell-orders
- description: 'The Zendesk Sell Line Items API lets you manage individual line items within orders. Line items correspond to products in your catalog and include quantity, pricing, and currency information for each '
  name: Zendesk Sell Line Items API
  slug: sell-line-items
- description: The Zendesk Sell Collaborations API provides a simple interface to manage collaborations. You can create, read, and delete collaborations to enable team members to work together on leads, contacts, an
  name: Zendesk Sell Collaborations API
  slug: sell-collaborations
- description: The Zendesk Sell Sequences API provides a read-only interface to sequences. A sequence is a set of steps with timeliness of their execution, where each step can be either an automated email or a task,
  name: Zendesk Sell Sequences API
  slug: sell-sequences
- description: The Zendesk Sell Lead Sources API provides a simple interface to manage lead sources. You can create, read, update, and delete sources to track where your leads originate from.
  name: Zendesk Sell Lead Sources API
  slug: sell-lead-sources
- description: The Zendesk Sell Deal Sources API provides a simple interface to manage deal sources. You can create, read, update, and delete sources to track where your deals originate from.
  name: Zendesk Sell Deal Sources API
  slug: sell-deal-sources
- description: The Zendesk Sell Lead Conversions API provides a simple interface to manage lead conversions. You can create or read lead conversions that transform leads into contacts and optionally create associate
  name: Zendesk Sell Lead Conversions API
  slug: sell-lead-conversions
- description: The Zendesk Sell Tags API provides a simple interface to manage tags. You can create, read, update, and delete tags used to categorize and organize leads, contacts, and deals in your CRM.
  name: Zendesk Sell Tags API
  slug: sell-tags
- description: The Zendesk Sell Custom Fields API lets you manage custom fields for leads, contacts, and deals. You can assign any number of custom fields as key-value pairs. Custom fields must first be created in t
  name: Zendesk Sell Custom Fields API
  slug: sell-custom-fields
- description: The Zendesk Sunshine Conversations API is a messaging platform that lets you unify messages from every channel into a single conversation and build interactive experiences. You can programmatically ma
  name: Zendesk Sunshine Conversations API
  slug: sunshine-conversations
- description: The Zendesk Omnichannel API provides access to agent availability and status information across Zendesk channels. It includes unified and custom agent statuses, per-channel agent statuses, assigned wo
  name: Zendesk Omnichannel API
  slug: omnichannel
- description: The Zendesk Unified Agent Statuses API lets you manage and query unified agent statuses that span across all channels in omnichannel routing. It provides a single view of each agent's availability sta
  name: Zendesk Unified Agent Statuses API
  slug: unified-agent-statuses
- description: The Zendesk Omnichannel Engagements API provides access to engagement data for agents across all channels. It enables tracking and reporting on how agents interact with work items, including assignmen
  name: Zendesk Omnichannel Engagements API
  slug: omnichannel-engagements
- description: 'The Zendesk Apps API lets you manage apps installed on your Zendesk account. It lists all public apps on the Zendesk Marketplace, and for authenticated agents and admins, also lists private apps. You '
  name: Zendesk Apps API
  slug: apps
- description: The Zendesk Account Settings API lets you view and manage the configuration settings for your Zendesk Support account, including settings for tickets, agents, security, branding, and other account-wid
  name: Zendesk Account Settings API
  slug: account-settings
- description: The Zendesk Schedules API lets you manage business hour schedules that define when your support team is available. Schedules are used by SLA policies, triggers, automations, and other business rules t
  name: Zendesk Schedules API
  slug: schedules
- description: The Zendesk User Identities API lets you manage the email addresses, phone numbers, X (Twitter) handles, and other identities associated with a user. You can list, create, update, verify, and delete i
  name: Zendesk User Identities API
  slug: user-identities
- description: The Zendesk Ticket Comments API lets you manage comments on support tickets. Comments are the public and internal messages exchanged between agents, end users, and collaborators on a ticket. You can l
  name: Zendesk Ticket Comments API
  slug: ticket-comments
- description: The Zendesk Skill-Based Routing API lets you manage skills and skill-based routing rules that match tickets to agents with the right expertise. You can define skills such as language fluency or produc
  name: Zendesk Skill-Based Routing API
  slug: skill-based-routing
- baseURL: https://{subdomain}.zendesk.com
  baseurl_source: declared
  description: The Account Settings API from Zendesk — 1 operation(s) for account settings.
  name: Zendesk Account Settings API
  phrasing_intents:
  - id: ShowAccountSettings
    intent: View account settings
    question: What settings are enabled on our Zendesk account?
  - id: UpdateAccountSettings
    intent: Change account settings
    question: How do I change an account-wide setting through the API?
  phrasing_ops: 2
  slug: zendesk-account-settings-api
- baseURL: https://{subdomain}.zendesk.com
  baseurl_source: declared
  description: The Activity Stream API from Zendesk — 3 operation(s) for activity stream.
  name: Zendesk Activity Stream API
  phrasing_intents:
  - id: ListActivities
    intent: List my recent ticket activities
    question: What ticket activity has affected me in the last 30 days?
  - id: ShowActivity
    intent: Get a ticket activity
    question: Can I look at the details of one activity in my stream?
  - id: CountActivities
    intent: Count my recent ticket activities
    question: How many ticket activities affected me in the last 30 days?
  phrasing_ops: 3
  slug: zendesk-activity-stream-api
- baseURL: https://{subdomain}.zendesk.com
  baseurl_source: declared
  description: The Approval Requests API from Zendesk — 3 operation(s) for approval requests.
  name: Zendesk Approval Requests API
  phrasing_intents:
  - id: ShowApprovalRequest
    intent: Get an approval request
    question: How do I view the details of an approval request assigned to me?
  - id: UpdateDecisionApprovalRequest
    intent: Approve or reject an approval request
    question: How do I approve or reject an approval request as the approver?
  - id: SearchApprovals
    intent: Search approvals in a workflow instance
    question: Which approval requests belong to one workflow instance?
  phrasing_ops: 3
  slug: zendesk-approval-requests-api
- baseURL: https://{subdomain}.zendesk.com
  baseurl_source: declared
  description: The AssigneeFieldAssignableAgents API from Zendesk — 3 operation(s) for assigneefieldassignableagents.
  name: Zendesk AssigneeFieldAssignableAgents API
  phrasing_intents:
  - id: ListAssigneeFieldAssignableGroupsAndAgentsSearch
    intent: Search assignable groups and agents
    question: Can I search assignable agents and groups by name?
  - id: ListAssigneeFieldAssignableGroups
    intent: List assignable groups
    question: Which groups can tickets be assigned to?
  - id: ListAssigneeFieldAssignableGroupAgents
    intent: List assignable agents in a group
    question: Which agents in a group can be assigned tickets?
  phrasing_ops: 3
  slug: zendesk-assigneefieldassignableagents-api
- baseURL: https://{subdomain}.zendesk.com
  baseurl_source: declared
  description: The AssigneeFieldAssignableGroups API from Zendesk — 1 operation(s) for assigneefieldassignablegroups.
  name: Zendesk AssigneeFieldAssignableGroups API
  phrasing_intents:
  - id: ListAssigneeFieldAssignableGroupsAndAgentsSearch
    intent: Search assignable groups and agents by name
    question: Which groups and agents can I assign a ticket to whose name matches what I typed?
  phrasing_ops: 1
  slug: zendesk-assigneefieldassignablegroups-api
- baseURL: https://{subdomain}.zendesk.com
  baseurl_source: declared
  description: The Attachments API from Zendesk — 4 operation(s) for attachments.
  name: Zendesk Attachments API
  phrasing_intents:
  - id: ShowAttachment
    intent: Get attachment details
    question: How do I get the details of a file attached to a ticket comment?
  - id: UpdateAttachment
    intent: Allow or restrict access to a malware attachment
    question: Can I let agents open an attachment that was flagged as malware?
  - id: RedactCommentAttachment
    intent: Permanently redact an attachment from a comment
    question: How do I permanently remove a sensitive file from a ticket comment?
  - id: UploadFiles
    intent: Upload a file for a ticket comment
    question: How do I upload a file so I can attach it to a ticket comment?
  - id: DeleteUpload
    intent: Delete an uploaded file by token
    question: Can I delete a file I uploaded before it gets attached to a comment?
  phrasing_ops: 5
  slug: zendesk-attachments-api
- baseURL: https://{subdomain}.zendesk.com
  baseurl_source: declared
  description: The Audit Logs API from Zendesk — 3 operation(s) for audit logs.
  name: Zendesk Audit Logs API
  phrasing_intents:
  - id: ListAuditLogs
    intent: List audit log entries
    question: Who changed settings in my account, and when?
  - id: ShowAuditLog
    intent: Show an audit log entry
    question: Can I view the full details of one audit log entry?
  - id: ExportAuditLogs
    intent: Export audit logs
    question: Can I export the audit log to a file for compliance review?
  phrasing_ops: 3
  slug: zendesk-audit-logs-api
- baseURL: https://{subdomain}.zendesk.com
  baseurl_source: declared
  description: The Autocomplete API from Zendesk — 1 operation(s) for autocomplete.
  name: Zendesk Autocomplete API
  phrasing_intents:
  - id: AutocompleteTags
    intent: Autocomplete tag names
    question: Which tags start with the letters I've typed?
  phrasing_ops: 1
  slug: zendesk-autocomplete-api
- baseURL: https://{subdomain}.zendesk.com
  baseurl_source: declared
  description: The Automations API from Zendesk — 6 operation(s) for automations.
  name: Zendesk Automations API
  phrasing_intents:
  - id: ListAutomations
    intent: List automations
    question: What automations are set up in my Zendesk account?
  - id: CreateAutomation
    intent: Create an automation
    question: Can I create a time-based automation through the API?
  - id: ShowAutomation
    intent: Get an automation
    question: How do I see the conditions and actions of a single automation?
  - id: UpdateAutomation
    intent: Update an automation
    question: Can I change the conditions of an existing automation?
  - id: DeleteAutomation
    intent: Delete an automation
    question: Can I delete a single automation?
  - id: ListActiveAutomations
    intent: List active automations
    question: Which automations are currently active?
  - id: BulkDeleteAutomations
    intent: Delete several automations at once
    question: Can I bulk delete a list of automations?
  - id: SearchAutomations
    intent: Search automations
    question: Can I search automations by title?
  phrasing_ops: 9
  slug: zendesk-automations-api
- baseURL: https://{subdomain}.zendesk.com
  baseurl_source: declared
  description: The Basics API from Zendesk — 3 operation(s) for basics.
  name: Zendesk Basics API
  phrasing_intents:
  - id: OpenTicketInAgentBrowser
    intent: Open a ticket in an agent's browser
    question: Can a phone system pop a ticket open on an agent's screen?
  - id: OpenUsersProfileInAgentBrowser
    intent: Open a user profile in an agent's browser
    question: Can I show a caller's profile to the agent answering the phone?
  - id: CreateTicketOrVoicemailTicket
    intent: Create a call or voicemail ticket
    question: Can a telephony partner create a ticket from a call or voicemail?
  phrasing_ops: 3
  slug: zendesk-basics-api
- baseURL: https://{subdomain}.zendesk.com
  baseurl_source: declared
  description: The Bookmarks API from Zendesk — 2 operation(s) for bookmarks.
  name: Zendesk Bookmarks API
  phrasing_intents:
  - id: ListBookmarks
    intent: List my ticket bookmarks
    question: Which tickets have I bookmarked as an agent?
  - id: CreateBookmark
    intent: Bookmark a ticket
    question: How do I bookmark a ticket so I can find it later?
  - id: DeleteBookmark
    intent: Remove a ticket bookmark
    question: Can I remove a bookmark I no longer need?
  phrasing_ops: 3
  slug: zendesk-bookmarks-api
- baseURL: https://{subdomain}.zendesk.com
  baseurl_source: declared
  description: The Brand Agents API from Zendesk — 2 operation(s) for brand agents.
  name: Zendesk Brand Agents API
  phrasing_intents:
  - id: ListBrandAgents
    intent: List brand agent memberships
    question: Which agents belong to which brands?
  - id: ShowBrandAgentById
    intent: Get a brand agent membership
    question: How do I look up one brand agent membership by id?
  phrasing_ops: 2
  slug: zendesk-brand-agents-api
- baseURL: https://{subdomain}.zendesk.com
  baseurl_source: declared
  description: The Brands API from Zendesk — 4 operation(s) for brands.
  name: Zendesk Brands API
  phrasing_intents:
  - id: ListBrands
    intent: List all brands
    question: What brands are set up in our Zendesk account?
  - id: CreateBrand
    intent: Create a brand
    question: How do I add a new brand for a separate product line?
  - id: ShowBrand
    intent: Get a brand's details
    question: How can I see one brand's settings, like its subdomain and logo?
  - id: UpdateBrand
    intent: Update a brand or its logo
    question: Can I upload a new logo image for a brand?
  - id: DeleteBrand
    intent: Delete a brand
    question: Can I delete a brand we've retired?
  - id: CheckHostMappingValidityForExistingBrand
    intent: Validate host mapping for an existing brand
    question: Is the custom domain on one of my existing brands set up correctly?
  - id: CheckHostMappingValidity
    intent: Validate a host mapping before creating a brand
    question: Before creating a brand, can I test whether a host mapping works for a subdomain?
  phrasing_ops: 7
  slug: zendesk-brands-api
- baseURL: https://{subdomain}.zendesk.com
  baseurl_source: declared
  description: The Channel Framework API from Zendesk — 3 operation(s) for channel framework.
  name: Zendesk Channel Framework API
  phrasing_intents:
  - id: ReportChannelbackError
    intent: Report a channelback error
    question: How do I report a failed channelback from my channel integration?
  - id: PushContentToSupport
    intent: Push channel content into Zendesk
    question: Can my channel integration push messages into Zendesk as tickets?
  - id: ValidateToken
    intent: Validate a channel integration token
    question: Can I check whether my channel integration token is valid?
  phrasing_ops: 3
  slug: zendesk-channel-framework-api
- baseURL: https://{subdomain}.zendesk.com
  baseurl_source: declared
  description: The Conversation Log API from Zendesk — 1 operation(s) for conversation log.
  name: Zendesk Conversation Log API
  phrasing_intents:
  - id: ListConversationLogForTicket
    intent: List a ticket's conversation log
    question: Can I see the full conversation log of events for a ticket?
  phrasing_ops: 1
  slug: zendesk-conversation-log-api
- baseURL: https://{subdomain}.zendesk.com
  baseurl_source: declared
  description: The Custom Object Fields API from Zendesk — 4 operation(s) for custom object fields.
  name: Zendesk Custom Object Fields API
  phrasing_intents:
  - id: ListCustomObjectFields
    intent: List fields of a custom object
    question: What fields are defined on one of my custom objects?
  - id: CreateCustomObjectField
    intent: Add a field to a custom object
    question: Can I add a lookup or dropdown field to a custom object?
  - id: ShowCustomObjectField
    intent: Get a custom object field
    question: Can I fetch a custom object field by its key or id?
  - id: UpdateCustomObjectField
    intent: Update a custom object field
    question: Can I change a custom object field's title after creating it?
  - id: DeleteCustomObjectField
    intent: Delete a custom object field
    question: Can I remove a field from a custom object?
  - id: ReorderCustomObjectFields
    intent: Reorder a custom object's fields
    question: Can I set the display order of a custom object's fields?
  - id: CustomObjectFieldsLimit
    intent: Check a custom object's field limit
    question: How many more fields can I add to a custom object?
  phrasing_ops: 7
  slug: zendesk-custom-object-fields-api
- baseURL: https://{subdomain}.zendesk.com
  baseurl_source: declared
  description: The Custom Object Records API from Zendesk — 7 operation(s) for custom object records.
  name: Zendesk Custom Object Records API
  phrasing_intents:
  - id: AutocompleteCustomObjectRecordSearch
    intent: Autocomplete custom object records by name
    question: Can I get record suggestions for a lookup field as an agent types a name?
  - id: CustomObjectRecordBulkJobs
    intent: Run a bulk job on custom object records
    question: Can I create, update or delete up to 100 custom object records in one background job?
  - id: ListCustomObjectRecords
    intent: List a custom object's records
    question: Where can I see all the undeleted records stored for one of my custom objects?
  - id: CreateCustomObjectRecord
    intent: Create a custom object record
    question: How do I add one new record to a custom object I defined?
  - id: UpsertCustomObjectRecordByExternalIdOrName
    intent: Upsert a custom object record by external ID or name
    question: Can I update a custom object record if it exists for an external ID and create it otherwise?
  - id: DeleteCustomObjectRecordByExternalIdOrName
    intent: Delete a custom object record by external ID or name
    question: Can I delete a custom object record using its external ID instead of the Zendesk ID?
  - id: ShowCustomObjectRecord
    intent: Show a custom object record
    question: Can I fetch a single custom object record by its record ID?
  - id: UpdateCustomObjectRecord
    intent: Update a custom object record
    question: Can I change the field values of an existing custom object record by its ID?
  phrasing_ops: 13
  slug: zendesk-custom-object-records-api
- baseURL: https://{subdomain}.zendesk.com
  baseurl_source: declared
  description: The Custom Objects API from Zendesk — 3 operation(s) for custom objects.
  name: Zendesk Custom Objects API
  phrasing_intents:
  - id: ListCustomObjects
    intent: List custom objects
    question: Which custom objects have been defined in my account?
  - id: CreateCustomObject
    intent: Create a custom object
    question: How do I define a new custom object type such as Assets or Contracts?
  - id: ShowCustomObject
    intent: Show a custom object
    question: Can I view the definition of a custom object by its key?
  - id: UpdateCustomObject
    intent: Update a custom object
    question: Can I rename or change the description of a custom object?
  - id: DeleteCustomObject
    intent: Delete a custom object
    question: Can I permanently delete a custom object I no longer need?
  - id: CustomObjectsLimit
    intent: Check the custom object limit
    question: How many custom objects can my account create in total?
  phrasing_ops: 6
  slug: zendesk-custom-objects-api
- baseURL: https://{subdomain}.zendesk.com
  baseurl_source: declared
  description: The Custom Roles API from Zendesk — 2 operation(s) for custom roles.
  name: Zendesk Custom Roles API
  phrasing_intents:
  - id: ListCustomRoles
    intent: List custom agent roles
    question: What custom roles are defined for agents?
  - id: CreateCustomRole
    intent: Create a custom agent role
    question: Can I create a role with limited permissions for contractors?
  - id: ShowCustomRoleById
    intent: Get a custom role
    question: Where can I see the permissions of one custom role?
  - id: UpdateCustomRoleById
    intent: Update a custom role
    question: Can I change the permissions of an existing custom role?
  - id: DeleteCustomRoleById
    intent: Delete a custom role
    question: Can I remove a custom role we no longer use?
  phrasing_ops: 5
  slug: zendesk-custom-roles-api
- baseURL: https://{subdomain}.zendesk.com
  baseurl_source: declared
  description: The Custom Ticket Statuses API from Zendesk — 4 operation(s) for custom ticket statuses.
  name: Zendesk Custom Ticket Statuses API
  phrasing_intents:
  - id: BulkUpdateDefaultCustomStatus
    intent: Set default custom statuses in bulk
    question: Can I change which custom status is the default for several categories at once?
  - id: ListCustomStatuses
    intent: List custom ticket statuses
    question: What custom ticket statuses does my account have?
  - id: CreateCustomStatus
    intent: Create a custom ticket status
    question: Can I add a status like Waiting on Vendor to tickets?
  - id: ShowCustomStatus
    intent: Get a custom ticket status
    question: Where can I see the details of one custom status?
  - id: UpdateCustomStatus
    intent: Update a custom ticket status
    question: Can I rename a custom ticket status?
  - id: CreateTicketFormStatusesForCustomStatus
    intent: Link a custom status to ticket forms
    question: Can I make a custom status available on specific ticket forms?
  phrasing_ops: 6
  slug: zendesk-custom-ticket-statuses-api
- baseURL: https://{subdomain}.zendesk.com
  baseurl_source: declared
  description: The Deletion Schedules API from Zendesk — 2 operation(s) for deletion schedules.
  name: Zendesk Deletion Schedules API
  phrasing_intents:
  - id: ListDeletionSchedules
    intent: List deletion schedules
    question: Which deletion schedules are set up to purge data automatically?
  - id: CreateDeletionSchedule
    intent: Create a deletion schedule
    question: Can I set up automatic deletion of old data?
  - id: GetDeletionSchedule
    intent: Get a deletion schedule
    question: How do I see the conditions of one deletion schedule?
  - id: UpdateDeletionSchedule
    intent: Update a deletion schedule
    question: Can I change the conditions of an existing deletion schedule?
  - id: DeleteDeletionSchedule
    intent: Delete a deletion schedule
    question: Can I remove a deletion schedule I no longer want?
  phrasing_ops: 5
  slug: zendesk-deletion-schedules-api
- baseURL: https://{subdomain}.zendesk.com
  baseurl_source: declared
  description: The Dynamic Content API from Zendesk — 3 operation(s) for dynamic content.
  name: Zendesk Dynamic Content API
  phrasing_intents:
  - id: ListDynamicContents
    intent: List dynamic content items
    question: What dynamic content items exist in my account?
  - id: CreateDynamicContent
    intent: Create a dynamic content item
    question: Can I create a dynamic content item with translations?
  - id: ShowDynamicContentItem
    intent: Get a dynamic content item
    question: How do I see one dynamic content item and its placeholder?
  - id: UpdateDynamicContentItem
    intent: Rename a dynamic content item
    question: Can I rename a dynamic content item?
  - id: DeleteDynamicContentItem
    intent: Delete a dynamic content item
    question: Can I delete a dynamic content item I no longer use?
  - id: ShowManyDynamicContents
    intent: Get several dynamic content items
    question: Can I fetch several dynamic content items by identifier at once?
  phrasing_ops: 6
  slug: zendesk-dynamic-content-api
- baseURL: https://{subdomain}.zendesk.com
  baseurl_source: declared
  description: The Dynamic Content Item Variants API from Zendesk — 4 operation(s) for dynamic content item variants.
  name: Zendesk Dynamic Content Item Variants API
  phrasing_intents:
  - id: DynamicContentListVariants
    intent: List a dynamic content item's variants
    question: Which language variants exist for a dynamic content item?
  - id: CreateDynamicContentVariant
    intent: Add a locale variant to dynamic content
    question: Can I add a translation for a new locale to a dynamic content item?
  - id: ShowDynamicContentVariant
    intent: Get a dynamic content variant
    question: How do I see the text of one specific dynamic content variant?
  - id: UpdateDynamicContentVariant
    intent: Update a dynamic content variant
    question: Can I change just the content of one variant?
  - id: DeleteDynamicContentVariant
    intent: Delete a dynamic content variant
    question: Can I remove one locale variant from a dynamic content item?
  - id: CreateManyDynamicContentVariants
    intent: Add several variants to dynamic content
    question: Can I add several locale variants to an item in one call?
  - id: UpdateManyDynamicContentVariants
    intent: Update several variants at once
    question: Can I update multiple variants of an item in one request?
  phrasing_ops: 7
  slug: zendesk-dynamic-content-item-variants-api
- baseURL: https://{subdomain}.zendesk.com
  baseurl_source: declared
  description: The Email Notifications API from Zendesk — 3 operation(s) for email notifications.
  name: Zendesk Email Notifications API
  phrasing_intents:
  - id: ListEmailNotifications
    intent: List email notifications with a filter
    question: Which outbound emails were sent for a particular ticket?
  - id: ShowEmailNotification
    intent: Show an email notification
    question: Can I see delivery details for one outbound email notification?
  - id: ShowManyEmailNotifications
    intent: Show many email notifications
    question: Can I look up several email notifications at once by ticket or comment IDs?
  phrasing_ops: 3
  slug: zendesk-email-notifications-api
- baseURL: https://{subdomain}.zendesk.com
  baseurl_source: declared
  description: The Essentials Card API from Zendesk — 2 operation(s) for essentials card.
  name: Zendesk Essentials Card API
  phrasing_intents:
  - id: ShowEssentialsCard
    intent: Get the essentials card for an object type
    question: What fields show on the essentials card for users?
  - id: UpdateEssentialsCard
    intent: Update an object type's essentials card
    question: Can I change which fields appear on the essentials card for organizations?
  - id: DeleteEssentialsCard
    intent: Delete an object type's essentials card
    question: Can I delete the custom essentials card for an object type?
  - id: ShowEssentialsCards
    intent: List all essentials cards
    question: Which essentials cards are configured across all object types?
  phrasing_ops: 4
  slug: zendesk-essentials-card-api
- baseURL: https://{subdomain}.zendesk.com
  baseurl_source: declared
  description: The Global Clients API from Zendesk — 3 operation(s) for global clients.
  name: Zendesk Global Clients API
  phrasing_intents:
  - id: ListGlobalOAuthClients
    intent: List authorized global OAuth clients
    question: Which global OAuth apps have my users authorized?
  - id: ShowGlobalClient
    intent: Get a global OAuth client
    question: Where can I see details of one global OAuth client?
  - id: GlobalOAuthClientsTokenSummary
    intent: Summarize tokens for global clients
    question: How many tokens has each global OAuth client been issued in my account?
  phrasing_ops: 3
  slug: zendesk-global-clients-api
- baseURL: https://{subdomain}.zendesk.com
  baseurl_source: declared
  description: The Grant Type Tokens API from Zendesk — 1 operation(s) for grant type tokens.
  name: Zendesk Grant Type Tokens API
  phrasing_intents:
  - id: CreateTokenForGrantType
    intent: Exchange a grant for an OAuth access token
    question: How do I exchange an authorization code for a Zendesk OAuth access token?
  phrasing_ops: 1
  slug: zendesk-grant-type-tokens-api
- baseURL: https://{subdomain}.zendesk.com
  baseurl_source: declared
  description: The Group Memberships API from Zendesk — 6 operation(s) for group memberships.
  name: Zendesk Group Memberships API
  phrasing_intents:
  - id: ListGroupMemberships
    intent: List group memberships
    question: Which agents belong to which groups?
  - id: CreateGroupMembership
    intent: Add an agent to a group
    question: Can I assign an agent to a support group?
  - id: ShowGroupMembershipById
    intent: Get a group membership
    question: Is a group membership id the same as a group id?
  - id: DeleteGroupMembership
    intent: Remove an agent from a group
    question: What happens to an agent's tickets when they leave a group?
  - id: ListAssignableGroupMemberships
    intent: List assignable group memberships
    question: Which group memberships can tickets actually be assigned to?
  - id: GroupMembershipBulkCreate
    intent: Add many agents to groups at once
    question: Can I assign up to 100 agents to groups in one request?
  - id: GroupMembershipBulkDelete
    intent: Remove many agents from groups
    question: Can I remove several agents from groups in one call?
  - id: GroupMembershipSetDefault
    intent: Set an agent's default group
    question: Can I choose which group is an agent's default?
  phrasing_ops: 8
  slug: zendesk-group-memberships-api
- baseURL: https://{subdomain}.zendesk.com
  baseurl_source: declared
  description: The Group SLA Policies API from Zendesk — 4 operation(s) for group sla policies.
  name: Zendesk Group SLA Policies API
  phrasing_intents:
  - id: ListGroupSLAPolicies
    intent: List group SLA policies
    question: What group SLA policies do we have configured?
  - id: CreateGroupSLAPolicy
    intent: Create a group SLA policy
    question: How do I set a time target for how long a ticket can sit with one group?
  - id: ShowGroupSLAPolicy
    intent: Get a group SLA policy
    question: How can I view the filters and targets of one group SLA policy?
  - id: UpdateGroupSLAPolicy
    intent: Update a group SLA policy
    question: Can I change the target time on an existing group SLA policy?
  - id: DeleteGroupSLAPolicy
    intent: Delete a group SLA policy
    question: Can I remove a group SLA policy we no longer need?
  - id: RetrieveGroupSLAPolicyFilterDefinitionItems
    intent: List filter options for group SLA policies
    question: Which ticket conditions can I use to filter a group SLA policy?
  - id: ReorderGroupSLAPolicies
    intent: Reorder group SLA policies
    question: Does the order of group SLA policies matter, and can I change it?
  phrasing_ops: 7
  slug: zendesk-group-sla-policies-api
- baseURL: https://{subdomain}.zendesk.com
  baseurl_source: declared
  description: The Groups API from Zendesk — 4 operation(s) for groups.
  name: Zendesk Groups API
  phrasing_intents:
  - id: ListGroups
    intent: List agent groups
    question: What agent groups exist in my help desk?
  - id: CreateGroup
    intent: Create an agent group
    question: How do I set up a new team of agents such as Billing or Tier 2?
  - id: ShowGroupById
    intent: Show a group
    question: Can I fetch the details of a single agent group?
  - id: UpdateGroup
    intent: Update a group
    question: Can I rename an existing agent group?
  - id: DeleteGroup
    intent: Delete a group
    question: Can I delete an agent group I no longer use?
  - id: ListAssignableGroups
    intent: List groups tickets can be assigned to
    question: Which groups can tickets actually be assigned to?
  - id: CountGroups
    intent: Count groups
    question: How many agent groups does my account have?
  phrasing_ops: 7
  slug: zendesk-groups-api
- baseURL: https://{subdomain}.zendesk.com
  baseurl_source: declared
  description: The Incremental Export API from Zendesk — 7 operation(s) for incremental export.
  name: Zendesk Incremental Export API
  phrasing_intents:
  - id: IncrementalSampleExport
    intent: Sample an incremental export
    question: Can I test the incremental export format before running a full export?
  - id: IncrementalOrganizationExport
    intent: Export organizations changed since a time
    question: Can I pull every organization that changed since my last sync?
  - id: IncrementalTicketEvents
    intent: Export a stream of ticket events
    question: Can I get a stream of field changes made to tickets?
  - id: IncrementalTicketExportTime
    intent: Export changed tickets by start time
    question: Can I export tickets changed since a timestamp using time-based paging?
  - id: IncrementalTicketExportCursor
    intent: Export changed tickets with a cursor
    question: Is there a cursor-based way to export tickets changed since a time?
  - id: IncrementalUserExportTime
    intent: Export changed users by start time
    question: Can I export users updated since a timestamp with time-based paging?
  - id: IncrementalUserExportCursor
    intent: Export changed users with a cursor
    question: Is there a cursor-based export for users that changed?
  phrasing_ops: 7
  slug: zendesk-incremental-export-api
- baseURL: https://{subdomain}.zendesk.com
  baseurl_source: declared
  description: The Incremental Skill Based Routing API from Zendesk — 3 operation(s) for incremental skill based routing.
  name: Zendesk Incremental Skill Based Routing API
  phrasing_intents:
  - id: IncrementalSkilBasedRoutingAttributeValuesExport
    intent: Export changes to routing skill values
    question: How do I sync every change made to routing skills into our data warehouse?
  - id: IncrementalSkilBasedRoutingAttributesExport
    intent: Export changes to routing attributes
    question: Is there an incremental feed of changes to routing attribute categories?
  - id: IncrementalSkilBasedRoutingInstanceValuesExport
    intent: Export skill assignment changes on agents and tickets
    question: How do I get a history of skills being added to or removed from agents and tickets?
  phrasing_ops: 3
  slug: zendesk-incremental-skill-based-routing-api
- baseURL: https://{subdomain}.zendesk.com
  baseurl_source: declared
  description: The Job Statuses API from Zendesk — 4 operation(s) for job statuses.
  name: Zendesk Job Statuses API
  phrasing_intents:
  - id: ListJobStatuses
    intent: List background job statuses
    question: Which background jobs have run recently in my account?
  - id: ShowJobStatus
    intent: Show a background job's status
    question: Has the bulk import job I queued finished yet?
  - id: ShowManyJobStatuses
    intent: Show the status of several jobs
    question: Can I check several background jobs in one request?
  - id: BulkSetAgentAttributeValuesJob
    intent: Bulk set routing attributes for agents
    question: Can I add or remove skills for up to 100 agents at once?
  phrasing_ops: 4
  slug: zendesk-job-statuses-api
- baseURL: https://{subdomain}.zendesk.com
  baseurl_source: declared
  description: The Locales API from Zendesk — 6 operation(s) for locales.
  name: Zendesk Locales API
  phrasing_intents:
  - id: ListLocales
    intent: List the account's translation locales
    question: Which languages are enabled for my help desk account?
  - id: ShowLocaleById
    intent: Show a locale
    question: Can I get the details of one locale by its ID?
  - id: ListLocalesForAgent
    intent: List locales localized for agents
    question: In which languages can agents use the agent interface on my account?
  - id: ShowCurrentLocale
    intent: Show my current locale
    question: What language locale is set for the user making the request?
  - id: DetectBestLocale
    intent: Detect the best locale
    question: Can the API pick the best matching language locale for a visitor?
  - id: ListAvailablePublicLocales
    intent: List public locales available to all accounts
    question: Which languages are available to every account?
  phrasing_ops: 6
  slug: zendesk-locales-api
- baseURL: https://{subdomain}.zendesk.com
  baseurl_source: declared
  description: The Lookup Relationships API from Zendesk — 2 operation(s) for lookup relationships.
  name: Zendesk Lookup Relationships API
  phrasing_intents:
  - id: GetSourcesByTarget
    intent: Find records that point at an object via a lookup field
    question: Which tickets name this user as their Success Manager in a lookup field?
  - id: GetRelationshipFilterDefinitions
    intent: Get lookup relationship filter definitions
    question: What filter options can I use when building a lookup field's relationship filter?
  phrasing_ops: 2
  slug: zendesk-lookup-relationships-api
- baseURL: https://{subdomain}.zendesk.com
  baseurl_source: declared
  description: The Macros API from Zendesk — 15 operation(s) for macros.
  name: Zendesk Macros API
  phrasing_intents:
  - id: ListMacroAttachments
    intent: List the attachments on a macro
    question: Which files are attached to one of my Zendesk macros?
  - id: CreateAssociatedMacroAttachment
    intent: Upload an attachment directly to a macro
    question: Can I upload a file and attach it to an existing macro in one step?
  - id: CreateMacroAttachment
    intent: Upload a macro attachment to link later
    question: Can I upload a macro attachment now and link it to a macro later?
  - id: ShowMacroAttachment
    intent: Get details of a macro attachment
    question: What properties does a single macro attachment have, like its file name and size?
  - id: ListMacros
    intent: List all macros available to me
    question: How do I get every shared and personal macro in my Zendesk account?
  - id: CreateMacro
    intent: Create a macro
    question: Can I create a new canned-response macro through the API?
  - id: ShowMacro
    intent: Get a single macro
    question: How can I see the actions and settings of one specific macro?
  - id: UpdateMacro
    intent: Update a macro
    question: Can I change the actions or title of a macro I already created?
  phrasing_ops: 19
  slug: zendesk-macros-api
- baseURL: https://{subdomain}.zendesk.com
  baseurl_source: declared
  description: The OAuth Clients API from Zendesk — 3 operation(s) for oauth clients.
  name: Zendesk OAuth Clients API
  phrasing_intents:
  - id: ListOAuthClients
    intent: List OAuth clients
    question: Which OAuth clients are registered on our Zendesk account?
  - id: CreateOAuthClient
    intent: Register an OAuth client
    question: How do I register a new OAuth client for my integration?
  - id: ShowClient
    intent: Get an OAuth client
    question: How can I view one OAuth client's identifier and redirect URIs?
  - id: UpdateClient
    intent: Update an OAuth client
    question: Can I change the redirect URIs on an existing OAuth client?
  - id: DeleteClient
    intent: Delete an OAuth client
    question: What happens when I delete an OAuth client that's no longer used?
  - id: ClientGenerateSecret
    intent: Regenerate an OAuth client secret
    question: How do I rotate the secret on an OAuth client?
  phrasing_ops: 6
  slug: zendesk-oauth-clients-api
- baseURL: https://{subdomain}.zendesk.com
  baseurl_source: declared
  description: The OAuth Tokens API from Zendesk — 2 operation(s) for oauth tokens.
  name: Zendesk OAuth Tokens API
  phrasing_intents:
  - id: ListOAuthTokens
    intent: List OAuth tokens
    question: Which OAuth tokens have been issued for my user?
  - id: CreateOAuthToken
    intent: Create an OAuth access token
    question: Can I generate an access token with a specific scope?
  - id: ShowToken
    intent: Get an OAuth token's properties
    question: What scopes and client does one token have?
  - id: RevokeOAuthToken
    intent: Revoke an OAuth token
    question: Can I revoke an access token that may be compromised?
  phrasing_ops: 4
  slug: zendesk-oauth-tokens-api
- baseURL: https://{subdomain}.zendesk.com
  baseurl_source: declared
  description: The Object Triggers API from Zendesk — 7 operation(s) for object triggers.
  name: Zendesk Object Triggers API
  phrasing_intents:
  - id: ListObjectTriggers
    intent: List a custom object's triggers
    question: Which triggers are set up on one of my custom objects?
  - id: CreateObjectTrigger
    intent: Create an object trigger
    question: How do I add a trigger that fires on changes to custom object records?
  - id: GetObjectTrigger
    intent: Show an object trigger
    question: Can I view the conditions and actions of one specific object trigger?
  - id: UpdateObjectTrigger
    intent: Update an object trigger
    question: Why did updating one condition clear the rest of my object trigger's actions?
  - id: DeleteObjectTrigger
    intent: Delete an object trigger
    question: Can I remove a single trigger from a custom object?
  - id: ListActiveObjectTriggers
    intent: List active object triggers
    question: Which triggers on my custom object are currently active?
  - id: ListObjectTriggersDefinitions
    intent: List object trigger condition and action definitions
    question: What conditions and actions are available when building a trigger for a custom object?
  - id: DeleteManyObjectTriggers
    intent: Bulk delete object triggers
    question: Can I delete several custom object triggers in one request?
  phrasing_ops: 10
  slug: zendesk-object-triggers-api
- baseURL: https://{subdomain}.zendesk.com
  baseurl_source: declared
  description: The Omnichannel Routing Queues API from Zendesk — 4 operation(s) for omnichannel routing queues.
  name: Zendesk Omnichannel Routing Queues API
  phrasing_intents:
  - id: ListQueues
    intent: List routing queues
    question: What omnichannel routing queues are active in my account?
  - id: CreateQueue
    intent: Create a routing queue
    question: Can I create a new omnichannel routing queue?
  - id: ShowQueueById
    intent: Get a routing queue
    question: How do I look up one routing queue's definition?
  - id: UpdateQueue
    intent: Update a routing queue
    question: Can I change the conditions or groups of a routing queue?
  - id: DeleteQueue
    intent: Delete a routing queue
    question: Can I delete a routing queue and its related records?
  - id: ListQueueDefinitions
    intent: Get queue condition definitions
    question: What conditions can a routing queue use?
  - id: ReorderQueues
    intent: Reorder routing queues
    question: Can I change the order routing queues are evaluated in?
  phrasing_ops: 7
  slug: zendesk-omnichannel-routing-queues-api
- baseURL: https://{subdomain}.zendesk.com
  baseurl_source: declared
  description: The Organization Fields API from Zendesk — 3 operation(s) for organization fields.
  name: Zendesk Organization Fields API
  phrasing_intents:
  - id: ListOrganizationFields
    intent: List custom organization fields
    question: What custom fields exist on organizations?
  - id: CreateOrganizationField
    intent: Create a custom organization field
    question: Can I add a field like contract tier to organizations?
  - id: ShowOrganizationField
    intent: Get a custom organization field
    question: Where can I see one organization field's configuration?
  - id: UpdateOrganizationField
    intent: Update a custom organization field
    question: Can I change dropdown options on an organization field?
  - id: DeleteOrganizationField
    intent: Delete a custom organization field
    question: Can I remove an organization field entirely?
  - id: ReorderOrganizationField
    intent: Reorder custom organization fields
    question: Can I change the order organization fields appear in?
  phrasing_ops: 6
  slug: zendesk-organization-fields-api
- baseURL: https://{subdomain}.zendesk.com
  baseurl_source: declared
  description: The Organization Memberships API from Zendesk — 7 operation(s) for organization memberships.
  name: Zendesk Organization Memberships API
  phrasing_intents:
  - id: ListOrganizationMemberships
    intent: List organization memberships
    question: Which organizations does each user in my account belong to?
  - id: CreateOrganizationMembership
    intent: Add a user to an organization
    question: How do I assign a user to an organization?
  - id: ShowOrganizationMembershipById
    intent: Show an organization membership
    question: Can I look up a single organization membership by its ID?
  - id: DeleteOrganizationMembership
    intent: Remove an organization membership
    question: What happens to a user's working tickets when I remove their organization membership?
  - id: CreateManyOrganizationMemberships
    intent: Bulk create organization memberships
    question: Can I add up to 100 users to organizations in one job?
  - id: DeleteManyOrganizationMemberships
    intent: Bulk remove organization memberships
    question: Can I remove several organization memberships in one request?
  - id: SetOrganizationMembershipAsDefault
    intent: Make a membership the user's default
    question: Can I choose which membership is a user's default using the membership ID?
  - id: UnassignOrganization
    intent: Remove a user from an organization
    question: Can I take a user out of a specific organization using the user and organization IDs?
  phrasing_ops: 9
  slug: zendesk-organization-memberships-api
- baseURL: https://{subdomain}.zendesk.com
  baseurl_source: declared
  description: The Organization Subscriptions API from Zendesk — 2 operation(s) for organization subscriptions.
  name: Zendesk Organization Subscriptions API
  phrasing_intents:
  - id: ListOrganizationSubscriptions
    intent: List organization subscriptions
    question: Who is subscribed to updates on organizations?
  - id: CreateOrganizationSubscription
    intent: Subscribe to an organization's tickets
    question: How do I follow an organization so I get notified about its tickets?
  - id: ShowOrganizationSubscription
    intent: Get an organization subscription
    question: How do I look up one organization subscription?
  - id: DeleteOrganizationSubscription
    intent: Unsubscribe from an organization
    question: How do I stop following an organization?
  phrasing_ops: 4
  slug: zendesk-organization-subscriptions-api
- baseURL: https://{subdomain}.zendesk.com
  baseurl_source: declared
  description: The Organizations API from Zendesk — 18 operation(s) for organizations.
  name: Zendesk Organizations API
  phrasing_intents:
  - id: AutocompleteOrganizations
    intent: Autocomplete organization names by prefix
    question: Can I get organizations whose names start with a few letters I typed, using the v2 autocomplete?
  - id: ShowOrganizationMerge
    intent: Check the status of an organization merge
    question: Did the organization merge I started finish, and which org won?
  - id: ListOrganizations
    intent: List all organizations with cursor pagination
    question: How do I page through every organization in my Zendesk account with cursor pagination?
  - id: CreateOrganization
    intent: Create an organization
    question: Does each new organization need a unique name when created through api/v2?
  - id: ShowOrganization
    intent: Get one organization's details
    question: How can I look up a single organization's details by its id in the v2 API?
  - id: UpdateOrganization
    intent: Update an organization
    question: Will updating an organization's domain_names in v2 overwrite the ones already there?
  - id: DeleteOrganization
    intent: Delete an organization
    question: Who is allowed to delete an organization through the v2 API?
  - id: CreateOrganizationMerge
    intent: Merge one organization into another
    question: How do I merge two duplicate organizations and move their users and tickets over?
  phrasing_ops: 24
  slug: zendesk-organizations-api
- baseURL: https://{subdomain}.zendesk.com
  baseurl_source: declared
  description: The Push Notification Devices API from Zendesk — 1 operation(s) for push notification devices.
  name: Zendesk Push Notification Devices API
  phrasing_intents:
  - id: PushNotificationDevices
    intent: Unregister push notification devices
    question: How can I stop push notifications going to certain mobile devices?
  phrasing_ops: 1
  slug: zendesk-push-notification-devices-api
- baseURL: https://{subdomain}.zendesk.com
  baseurl_source: declared
  description: The Requests API from Zendesk — 5 operation(s) for requests.
  name: Zendesk Requests API
  phrasing_intents:
  - id: ListRequests
    intent: List an end user's support requests
    question: As an end user, how do I see all the support requests I've submitted?
  - id: CreateRequest
    intent: Submit a support request as an end user
    question: How can a customer open a support request from our own app?
  - id: ShowRequest
    intent: Get one of my support requests
    question: How do I check the status of a request I submitted?
  - id: UpdateRequest
    intent: Comment on or solve my request
    question: Can an end user add a comment or cc someone on their existing request?
  - id: ListComments
    intent: List comments on a request
    question: How do I read the conversation on one of my requests?
  - id: ShowComment
    intent: Get one comment on a request
    question: How do I fetch a single comment from a request's thread?
  - id: SearchRequests
    intent: Search my support requests
    question: Can I search my requests for a keyword like printer?
  phrasing_ops: 7
  slug: zendesk-requests-api
- baseURL: https://{subdomain}.zendesk.com
  baseurl_source: declared
  description: The Reseller API from Zendesk — 2 operation(s) for reseller.
  name: Zendesk Reseller API
  phrasing_intents:
  - id: CreateTrialAccount
    intent: Create a trial account
    question: Can a reseller spin up a new trial help desk account?
  - id: VerifySubdomainAvailability
    intent: Check whether a subdomain is available
    question: Is a subdomain still free to use for a new account?
  phrasing_ops: 2
  slug: zendesk-reseller-api
- baseURL: https://{subdomain}.zendesk.com
  baseurl_source: declared
  description: The Resource Collections API from Zendesk — 2 operation(s) for resource collections.
  name: Zendesk Resource Collections API
  phrasing_intents:
  - id: ListResourceCollections
    intent: List resource collections
    question: What resource collections exist on our account?
  - id: CreateResourceCollection
    intent: Create a resource collection from a payload
    question: How do I create ticket fields, triggers and targets together from a requirements.json-style payload?
  - id: RetrieveResourceCollection
    intent: Get a resource collection
    question: How do I see what resources are in one resource collection?
  - id: UpdateResourceCollection
    intent: Update a resource collection
    question: Can I change the resources in a collection by sending a new payload?
  - id: DeleteResourceCollection
    intent: Delete a resource collection
    question: What happens to the resources when I delete a resource collection?
  phrasing_ops: 5
  slug: zendesk-resource-collections-api
- baseURL: https://{subdomain}.zendesk.com
  baseurl_source: declared
  description: The Satisfaction Ratings API from Zendesk — 4 operation(s) for satisfaction ratings.
  name: Zendesk Satisfaction Ratings API
  phrasing_intents:
  - id: ListSatisfactionRatings
    intent: List satisfaction ratings
    question: Which customers left good or bad CSAT ratings?
  - id: ShowSatisfactionRating
    intent: Get a satisfaction rating
    question: How do I look up one satisfaction rating by id?
  - id: CountSatisfactionRatings
    intent: Count satisfaction ratings
    question: How many satisfaction ratings are in my account?
  - id: CreateTicketSatisfactionRating
    intent: Rate a solved ticket
    question: Can a requester rate a solved ticket through the API?
  phrasing_ops: 4
  slug: zendesk-satisfaction-ratings-api
- baseURL: https://{subdomain}.zendesk.com
  baseurl_source: declared
  description: The Satisfaction Reasons API from Zendesk — 2 operation(s) for satisfaction reasons.
  name: Zendesk Satisfaction Reasons API
  phrasing_intents:
  - id: ListSatisfactionRatingReasons
    intent: List satisfaction rating reasons
    question: What reasons can customers pick when they give a bad satisfaction rating?
  - id: ShowSatisfactionRatings
    intent: Get one satisfaction reason
    question: How do I look up a single satisfaction reason by its id?
  phrasing_ops: 2
  slug: zendesk-satisfaction-reasons-api
- baseURL: https://{subdomain}.zendesk.com
  baseurl_source: declared
  description: The Search API from Zendesk — 3 operation(s) for search.
  name: Zendesk Search API
  phrasing_intents:
  - id: ListSearchResults
    intent: Search tickets, users and more
    question: How do I search across tickets, users and organizations?
  - id: CountSearchResults
    intent: Count search results
    question: How many items match a search without fetching them?
  - id: ExportSearchResults
    intent: Export large search results
    question: What if my search returns more than 1000 results?
  phrasing_ops: 3
  slug: zendesk-search-api
- baseURL: https://{subdomain}.zendesk.com
  baseurl_source: declared
  description: The Sessions API from Zendesk — 6 operation(s) for sessions.
  name: Zendesk Sessions API
  phrasing_intents:
  - id: ListSessions
    intent: List sessions
    question: Can an admin see every active session across the account?
  - id: BulkDeleteSessionsByUserId
    intent: End all of a user's sessions
    question: How do I sign a user out of every device at once?
  - id: ShowSession
    intent: Show a user's session
    question: Can I inspect one specific session of a user?
  - id: DeleteSession
    intent: End one of a user's sessions
    question: Can I terminate a single session without logging the user out elsewhere?
  - id: DeleteAuthenticatedSession
    intent: Log out the current session
    question: Can my Zendesk app log the current user out of their own session?
  - id: ShowCurrentlyAuthenticatedSession
    intent: Show the current session
    question: What session am I currently authenticated with?
  - id: RenewCurrentSession
    intent: Renew the current session
    question: Can I keep my session alive by renewing it?
  phrasing_ops: 7
  slug: zendesk-sessions-api
- baseURL: https://{subdomain}.zendesk.com
  baseurl_source: declared
  description: The Sharing Agreements API from Zendesk — 2 operation(s) for sharing agreements.
  name: Zendesk Sharing Agreements API
  phrasing_intents:
  - id: ListSharingAgreements
    intent: List ticket sharing agreements
    question: Which ticket sharing agreements does my account have with other accounts?
  - id: CreateSharingAgreement
    intent: Create a ticket sharing agreement
    question: How do I set up ticket sharing with another help desk account?
  - id: ShowSharingAgreement
    intent: Show a sharing agreement
    question: Can I view the details of a single sharing agreement?
  - id: UpdateSharingAgreement
    intent: Change a sharing agreement's status
    question: Can I accept or decline a pending sharing agreement?
  - id: DeleteSharingAgreement
    intent: Delete a sharing agreement
    question: Can I end ticket sharing by deleting the agreement?
  phrasing_ops: 5
  slug: zendesk-sharing-agreements-api
- baseURL: https://{subdomain}.zendesk.com
  baseurl_source: declared
  description: The Skill Based Routing API from Zendesk — 10 operation(s) for skill based routing.
  name: Zendesk Skill Based Routing API
  phrasing_intents:
  - id: ListAGentAttributeValues
    intent: List an agent's routing skills
    question: Which skills are assigned to a particular agent for routing?
  - id: SetAgentAttributeValues
    intent: Set or replace an agent's routing skills
    question: Does setting skills on an agent replace the ones they already have?
  - id: ListManyAgentsAttributeValues
    intent: Get skills for up to 100 agents
    question: Can I pull the routing skills for a whole team of agents in one call?
  - id: BulkSetAgentAttributeValuesJob
    intent: Bulk add, replace or remove agent skills
    question: How do I add a skill to 100 agents at once?
  - id: ListAccountAttributes
    intent: List routing attributes on the account
    question: What routing attributes, like Language or Product, are defined on our account?
  - id: CreateAttribute
    intent: Create a routing attribute
    question: How do I add a new skill category such as Language for routing?
  - id: ShowAttribute
    intent: Get a routing attribute
    question: How do I see the details of one routing attribute?
  - id: UpdateAttribute
    intent: Rename a routing attribute
    question: Can I rename an existing routing attribute?
  phrasing_ops: 18
  slug: zendesk-skill-based-routing-api
- baseURL: https://{subdomain}.zendesk.com
  baseurl_source: declared
  description: The SLA Policies API from Zendesk — 4 operation(s) for sla policies.
  name: Zendesk SLA Policies API
  phrasing_intents:
  - id: ListSLAPolicies
    intent: List SLA policies
    question: What service level agreements are set up in my account?
  - id: CreateSLAPolicy
    intent: Create an SLA policy
    question: Can I set a first reply target for urgent tickets?
  - id: ShowSLAPolicy
    intent: Get an SLA policy
    question: Where can I see the targets and filter of one SLA policy?
  - id: UpdateSLAPolicy
    intent: Update an SLA policy
    question: Can I change the response targets of an existing SLA?
  - id: DeleteSLAPolicy
    intent: Delete an SLA policy
    question: Can I remove an SLA policy we no longer use?
  - id: RetrieveSLAPolicyFilterDefinitionItems
    intent: List SLA policy filter definitions
    question: What conditions can I use to decide which tickets an SLA applies to?
  - id: ReorderSLAPolicies
    intent: Reorder SLA policies
    question: Can I change which SLA policy takes precedence?
  phrasing_ops: 7
  slug: zendesk-sla-policies-api
- baseURL: https://{subdomain}.zendesk.com
  baseurl_source: declared
  description: The Support Addresses API from Zendesk — 3 operation(s) for support addresses.
  name: Zendesk Support Addresses API
  phrasing_intents:
  - id: ListSupportAddresses
    intent: List support addresses
    question: Which email addresses receive support requests in my account?
  - id: CreateSupportAddress
    intent: Add a support address
    question: Can I add a new Zendesk or external support email address?
  - id: ShowSupportAddress
    intent: Get a support address
    question: How do I check the forwarding status of one support address?
  - id: UpdateSupportAddress
    intent: Update a support address
    question: Can I change the name or brand of a support address?
  - id: DeleteRecipientAddress
    intent: Delete a support address
    question: Can I remove a support address I don't use?
  - id: VerifySupportAddressForwarding
    intent: Verify support address forwarding
    question: How can I check that email forwarding works for an external support address?
  phrasing_ops: 6
  slug: zendesk-support-addresses-api
- baseURL: https://{subdomain}.zendesk.com
  baseurl_source: declared
  description: The Suspended Tickets API from Zendesk — 7 operation(s) for suspended tickets.
  name: Zendesk Suspended Tickets API
  phrasing_intents:
  - id: SuspendedTicketsAttachments
    intent: Copy a suspended ticket's attachments
    question: Can I keep the attachments from a suspended ticket when I recover it manually?
  - id: ListSuspendedTickets
    intent: List suspended tickets
    question: Which incoming emails were suspended instead of becoming tickets?
  - id: ShowSuspendedTickets
    intent: Get a suspended ticket
    question: Why was a particular ticket suspended?
  - id: DeleteSuspendedTicket
    intent: Delete a suspended ticket
    question: Can I delete a single suspended ticket that's spam?
  - id: RecoverSuspendedTicket
    intent: Recover a suspended ticket
    question: Can I turn a suspended ticket back into a normal ticket?
  - id: DeleteSuspendedTickets
    intent: Delete many suspended tickets
    question: Can I bulk delete up to 100 suspended tickets?
  - id: ExportSuspendedTickets
    intent: Export suspended tickets to CSV
    question: Can I export the suspended tickets list to a CSV file?
  - id: RecoverSuspendedTickets
    intent: Recover many suspended tickets
    question: Can I recover a batch of suspended tickets at once?
  phrasing_ops: 8
  slug: zendesk-suspended-tickets-api
- baseURL: https://{subdomain}.zendesk.com
  baseurl_source: declared
  description: The Tags API from Zendesk — 2 operation(s) for tags.
  name: Zendesk Tags API
  phrasing_intents:
  - id: ListTags
    intent: List popular tags
    question: What are the most popular tags in my account?
  - id: CountTags
    intent: Count tags
    question: How many tags are in my account?
  phrasing_ops: 2
  slug: zendesk-tags-api
- baseURL: https://{subdomain}.zendesk.com
  baseurl_source: declared
  description: The Target Failures API from Zendesk — 2 operation(s) for target failures.
  name: Zendesk Target Failures API
  phrasing_intents:
  - id: ListTargetFailures
    intent: List recent target failures
    question: Why are my notification targets failing to deliver?
  - id: ShowTargetFailure
    intent: Show a target failure
    question: Can I see the full response details for one target failure?
  phrasing_ops: 2
  slug: zendesk-target-failures-api
- baseURL: https://{subdomain}.zendesk.com
  baseurl_source: declared
  description: The Targets API from Zendesk — 2 operation(s) for targets.
  name: Zendesk Targets API
  phrasing_intents:
  - id: ListTargets
    intent: List notification targets
    question: What external targets are configured for notifications?
  - id: CreateTarget
    intent: Create a notification target
    question: Can I add an external target that triggers can notify?
  - id: ShowTarget
    intent: Get a notification target
    question: Where can I see how one target is configured?
  - id: UpdateTarget
    intent: Update a notification target
    question: Can I change the address or settings of an existing target?
  - id: DeleteTarget
    intent: Delete a notification target
    question: Can I remove a target I no longer need?
  phrasing_ops: 5
  slug: zendesk-targets-api
- baseURL: https://{subdomain}.zendesk.com
  baseurl_source: declared
  description: The Ticket Audits API from Zendesk — 5 operation(s) for ticket audits.
  name: Zendesk Ticket Audits API
  phrasing_intents:
  - id: ListTicketAudits
    intent: List ticket audits across the account
    question: Can I pull the audit trail for all tickets in my account?
  - id: ListAuditsForTicket
    intent: List the audits for one ticket
    question: What changes have been made to a specific ticket?
  - id: ShowTicketAudit
    intent: Get a ticket audit
    question: How do I look up one audit on a ticket?
  - id: MakeTicketCommentPrivateFromAudits
    intent: Make an audit's comment private
    question: Can I make a comment private using its audit id?
  - id: CountAuditsForTicket
    intent: Count a ticket's audits
    question: How many audits does a ticket have?
  phrasing_ops: 5
  slug: zendesk-ticket-audits-api
- baseURL: https://{subdomain}.zendesk.com
  baseurl_source: declared
  description: The Ticket Comments API from Zendesk — 7 operation(s) for ticket comments.
  name: Zendesk Ticket Comments API
  phrasing_intents:
  - id: RedactChatCommentAttachment
    intent: Redact attachments from a chat ticket
    question: Can I permanently remove a file shared in a chat ticket?
  - id: RedactChatComment
    intent: Redact text from a chat ticket comment
    question: Can I scrub a credit card number someone typed into a chat?
  - id: RedactTicketCommentInAgentWorkspace
    intent: Redact content from a ticket comment
    question: Can I remove sensitive text or attachments from a comment in the Agent Workspace?
  - id: ListTicketComments
    intent: List a ticket's comments
    question: How do I read all the comments on a ticket?
  - id: MakeTicketCommentPrivate
    intent: Make a ticket comment private
    question: Can I hide a public reply so the requester can't see it?
  - id: RedactStringInComment
    intent: Redact a string from a ticket comment
    question: Can I remove a specific string like a social security number from a comment?
  - id: CountTicketComments
    intent: Count a ticket's comments
    question: How many comments does a ticket have?
  phrasing_ops: 7
  slug: zendesk-ticket-comments-api
- baseURL: https://{subdomain}.zendesk.com
  baseurl_source: declared
  description: The Ticket Content Pins API from Zendesk — 2 operation(s) for ticket content pins.
  name: Zendesk Ticket Content Pins API
  phrasing_intents:
  - id: ListTicketContentPins
    intent: List a ticket's content pins
    question: Which articles have been pinned to a ticket for quick access?
  - id: CreateTicketContentPin
    intent: Pin content to a ticket
    question: How do I pin a help center article to a ticket?
  - id: DeleteTicketContentPin
    intent: Remove a content pin from a ticket
    question: Can I unpin an article from a ticket?
  phrasing_ops: 3
  slug: zendesk-ticket-content-pins-api
- baseURL: https://{subdomain}.zendesk.com
  baseurl_source: declared
  description: The Ticket Fields API from Zendesk — 6 operation(s) for ticket fields.
  name: Zendesk Ticket Fields API
  phrasing_intents:
  - id: ListTicketFields
    intent: List system and custom ticket fields
    question: What custom ticket fields do we have in Zendesk?
  - id: CreateTicketField
    intent: Create a custom ticket field
    question: How do I add a drop-down custom field to tickets?
  - id: ShowTicketfield
    intent: Get one ticket field
    question: How can I see the settings of one specific ticket field?
  - id: UpdateTicketField
    intent: Update a ticket field or its options
    question: Can I add or remove drop-down options by updating the whole ticket field?
  - id: DeleteTicketField
    intent: Delete a custom ticket field
    question: Can I delete a custom ticket field we no longer use?
  - id: ListTicketFieldOptions
    intent: List options of a drop-down ticket field
    question: What choices are in a drop-down ticket field?
  - id: CreateOrUpdateTicketFieldOption
    intent: Add or edit one drop-down field option
    question: How do I add a single new choice to a drop-down field without resending the rest?
  - id: ShowTicketFieldOption
    intent: Get one drop-down field option
    question: How do I look up a single option on a drop-down ticket field?
  phrasing_ops: 11
  slug: zendesk-ticket-fields-api
- baseURL: https://{subdomain}.zendesk.com
  baseurl_source: declared
  description: The Ticket Form Statuses API from Zendesk — 5 operation(s) for ticket form statuses.
  name: Zendesk Ticket Form Statuses API
  phrasing_intents:
  - id: CreateTicketFormStatusesForCustomStatus
    intent: Link a custom status to ticket forms
    question: How do I make a custom status available on several ticket forms at once?
  - id: ListTicketFormStatuses
    intent: List all ticket form status associations
    question: Which custom statuses are enabled on which ticket forms across the account?
  - id: ShowManyTicketFormStatuses
    intent: Get several ticket form statuses by id
    question: Can I fetch specific ticket form status associations by a list of ids?
  - id: TicketFormTicketFormStatuses
    intent: List statuses enabled on one ticket form
    question: Which custom statuses can agents pick on a particular ticket form?
  - id: CreateTicketFormStatuses
    intent: Add statuses to a ticket form
    question: How do I enable new custom statuses on a specific ticket form?
  - id: UpdateTicketFormStatuses
    intent: Bulk add and remove statuses on a form
    question: Can I add and remove several statuses on a ticket form in a single call?
  - id: DeleteTicketFormStatuses
    intent: Remove statuses from a ticket form
    question: Can I remove several status associations from a form by id?
  - id: UpdateTicketFormStatusById
    intent: Update one form status association
    question: Can I change a single ticket form status association by its id?
  phrasing_ops: 9
  slug: zendesk-ticket-form-statuses-api
- baseURL: https://{subdomain}.zendesk.com
  baseurl_source: declared
  description: The Ticket Forms API from Zendesk — 7 operation(s) for ticket forms.
  name: Zendesk Ticket Forms API
  phrasing_intents:
  - id: ListTicketForms
    intent: List ticket forms
    question: What ticket forms exist in my Zendesk account?
  - id: CreateTicketForm
    intent: Create a ticket form
    question: Can I create a new ticket form with its own set of fields?
  - id: ShowTicketForm
    intent: Get a ticket form
    question: How do I see the fields and settings of one ticket form?
  - id: UpdateTicketForm
    intent: Update a ticket form
    question: Can I change the name or fields of an existing ticket form?
  - id: DeleteTicketForm
    intent: Delete a ticket form
    question: Can I delete a ticket form I don't use anymore?
  - id: CloneTicketForm
    intent: Clone a ticket form
    question: Can I duplicate an existing ticket form as a starting point?
  - id: TicketFormTicketFormStatuses
    intent: List a ticket form's status associations
    question: Which ticket statuses are associated with a ticket form?
  - id: CreateTicketFormStatuses
    intent: Link statuses to a ticket form
    question: How can I associate new ticket statuses with a form?
  phrasing_ops: 12
  slug: zendesk-ticket-forms-api
- baseURL: https://{subdomain}.zendesk.com
  baseurl_source: declared
  description: The Ticket Import API from Zendesk — 2 operation(s) for ticket import.
  name: Zendesk Ticket Import API
  phrasing_intents:
  - id: TicketImport
    intent: Import a historical ticket
    question: Can I import an old ticket from another system with its original dates?
  - id: TicketBulkImport
    intent: Import up to 100 historical tickets
    question: Can I import a batch of legacy tickets at once?
  phrasing_ops: 2
  slug: zendesk-ticket-import-api
- baseURL: https://{subdomain}.zendesk.com
  baseurl_source: declared
  description: The Ticket Metric Events API from Zendesk — 1 operation(s) for ticket metric events.
  name: Zendesk Ticket Metric Events API
  phrasing_intents:
  - id: ListTicketMetricEvents
    intent: List ticket metric events since a time
    question: Can I get SLA and reply-time metric events since a timestamp?
  phrasing_ops: 1
  slug: zendesk-ticket-metric-events-api
- baseURL: https://{subdomain}.zendesk.com
  baseurl_source: declared
  description: The Ticket Metrics API from Zendesk — 2 operation(s) for ticket metrics.
  name: Zendesk Ticket Metrics API
  phrasing_intents:
  - id: ListTicketMetrics
    intent: List ticket metrics across tickets
    question: How do I pull reply times and resolution times for all our tickets?
  - id: ShowTicketMetrics
    intent: Get metrics for one ticket
    question: How long did it take us to first reply on a specific ticket?
  phrasing_ops: 2
  slug: zendesk-ticket-metrics-api
- baseURL: https://{subdomain}.zendesk.com
  baseurl_source: declared
  description: The Ticket Skips API from Zendesk — 2 operation(s) for ticket skips.
  name: Zendesk Ticket Skips API
  phrasing_intents:
  - id: RecordNewSkip
    intent: Record a ticket skip
    question: Can I record that I skipped a ticket?
  - id: ListTicketSkips
    intent: List a user's ticket skips
    question: Which tickets has an agent skipped?
  phrasing_ops: 2
  slug: zendesk-ticket-skips-api
- baseURL: https://{subdomain}.zendesk.com
  baseurl_source: declared
  description: The Tickets API from Zendesk — 26 operation(s) for tickets.
  name: Zendesk Tickets API
  phrasing_intents:
  - id: AutocompleteProblems
    intent: Find problem tickets by subject text
    question: Which problem tickets have a subject containing a word I type?
  - id: ListDeletedTickets
    intent: List soft-deleted tickets
    question: Where can I see tickets that were deleted but not yet purged?
  - id: DeleteTicketPermanently
    intent: Permanently delete a soft-deleted ticket
    question: Can I erase a ticket that is already in the deleted view for GDPR reasons?
  - id: RestoreDeletedTicket
    intent: Restore a deleted ticket
    question: Can I bring back a ticket someone deleted by mistake?
  - id: BulkPermanentlyDeleteTickets
    intent: Permanently delete many soft-deleted tickets
    question: Can I purge up to 100 already-deleted tickets in one request?
  - id: BulkRestoreDeletedTickets
    intent: Restore many deleted tickets at once
    question: Can I undelete a whole batch of tickets in a single call?
  - id: ListTicketProblems
    intent: List problem tickets
    question: Which tickets are marked as problems in my help desk?
  - id: ListResourceTags
    intent: List a ticket's tags
    question: What tags are currently on a particular ticket?
  phrasing_ops: 35
  slug: zendesk-tickets-api
- baseURL: https://{subdomain}.zendesk.com
  baseurl_source: declared
  description: The Trigger Categories API from Zendesk — 3 operation(s) for trigger categories.
  name: Zendesk Trigger Categories API
  phrasing_intents:
  - id: ListTriggerCategories
    intent: List ticket trigger categories
    question: What categories are my ticket triggers organized into?
  - id: CreateTriggerCategory
    intent: Create a ticket trigger category
    question: How do I add a new category to group my ticket triggers?
  - id: ShowTriggerCategoryById
    intent: Show a ticket trigger category
    question: Can I view a single trigger category by its ID?
  - id: UpdateTriggerCategory
    intent: Rename or reposition a trigger category
    question: Can I rename an existing ticket trigger category?
  - id: DeleteTriggerCategory
    intent: Delete a ticket trigger category
    question: Can I remove a trigger category I no longer use?
  - id: BatchOperateTriggerCategories
    intent: Batch update trigger categories and triggers
    question: Can I reorder several trigger categories in a single job?
  phrasing_ops: 6
  slug: zendesk-trigger-categories-api
- baseURL: https://{subdomain}.zendesk.com
  baseurl_source: declared
  description: The Triggers API from Zendesk — 10 operation(s) for triggers.
  name: Zendesk Triggers API
  phrasing_intents:
  - id: SearchTriggers
    intent: Search ticket triggers
    question: Can I search my ticket triggers by a keyword?
  - id: ListTriggers
    intent: List all ticket triggers
    question: What ticket triggers exist in my account, active or not?
  - id: CreateTrigger
    intent: Create a ticket trigger
    question: Can I set up a rule that fires automatically when a ticket changes?
  - id: GetTrigger
    intent: Get a ticket trigger
    question: Where can I see the conditions and actions of one trigger?
  - id: UpdateTrigger
    intent: Update a ticket trigger
    question: If I change one condition on a trigger, do I lose the existing actions?
  - id: DeleteTrigger
    intent: Delete a ticket trigger
    question: Can I remove a single trigger I no longer need?
  - id: ListTriggerRevisions
    intent: List a trigger's revision history
    question: Can I see who changed a trigger and when?
  - id: TriggerRevision
    intent: Get one revision of a trigger
    question: What did a trigger look like at a specific earlier revision?
  phrasing_ops: 13
  slug: zendesk-triggers-api
- baseURL: https://{subdomain}.zendesk.com
  baseurl_source: declared
  description: The User Fields API from Zendesk — 5 operation(s) for user fields.
  name: Zendesk User Fields API
  phrasing_intents:
  - id: ListUserFields
    intent: List custom user fields
    question: What custom fields exist on user profiles?
  - id: CreateUserField
    intent: Create a custom user field
    question: Can I add a dropdown or date field to user profiles?
  - id: ShowUserField
    intent: Get a custom user field
    question: Where can I see the settings of one user field?
  - id: UpdateUserField
    intent: Update a custom user field
    question: Can I change the dropdown choices of a user field?
  - id: DeleteUserField
    intent: Delete a custom user field
    question: Can an admin remove a custom user field entirely?
  - id: ListUserFieldOptions
    intent: List options of a dropdown user field
    question: What choices does a dropdown user field offer?
  - id: CreateOrUpdateUserFieldOption
    intent: Create or update a user field option
    question: Can I add a new choice to a user dropdown field?
  - id: ShowUserFieldOption
    intent: Get one option of a user field
    question: Can I look up a single choice in a user dropdown field?
  phrasing_ops: 10
  slug: zendesk-user-fields-api
- baseURL: https://{subdomain}.zendesk.com
  baseurl_source: declared
  description: The User Identities API from Zendesk — 5 operation(s) for user identities.
  name: Zendesk User Identities API
  phrasing_intents:
  - id: ListUserIdentities
    intent: List a user's identities
    question: Which emails, phone numbers and social accounts are attached to a user?
  - id: CreateUserIdentity
    intent: Add an identity to a user
    question: How do I add a second email address or phone number to a user's profile?
  - id: ShowUserIdentity
    intent: Show a user identity
    question: Can I view one specific identity on a user's profile?
  - id: UpdateUserIdentity
    intent: Update or unverify a user identity
    question: Can I change the value of an existing email identity?
  - id: DeleteUserIdentity
    intent: Delete a user identity
    question: Can I remove an old email or phone identity from a user?
  - id: MakeUserIdentityPrimary
    intent: Make an identity primary
    question: How do I change which email is a user's primary identity?
  - id: RequestUserVerfication
    intent: Send a verification email for an identity
    question: Can I send a user an email asking them to confirm they own an address?
  - id: VerifyUserIdentity
    intent: Mark an identity as verified
    question: Can an agent mark a user's identity verified without sending an email?
  phrasing_ops: 8
  slug: zendesk-user-identities-api
- baseURL: https://{subdomain}.zendesk.com
  baseurl_source: declared
  description: The User Passwords API from Zendesk — 2 operation(s) for user passwords.
  name: Zendesk User Passwords API
  phrasing_intents:
  - id: SetUserPassword
    intent: Set another user's password as admin
    question: Can an admin set a new password for another user?
  - id: ChangeOwnPassword
    intent: Change your own password
    question: Can I change my password if I know the current one?
  - id: GetUserPasswordRequirements
    intent: Get password requirements
    question: What rules must a new password meet?
  phrasing_ops: 3
  slug: zendesk-user-passwords-api
- baseURL: https://{subdomain}.zendesk.com
  baseurl_source: declared
  description: The Users API from Zendesk — 23 operation(s) for users.
  name: Zendesk Users API
  phrasing_intents:
  - id: AutocompleteUsers
    intent: Autocomplete users by the start of their name
    question: Can I get user suggestions as someone types the first letters of a name?
  - id: ListDeletedUsers
    intent: List deleted users
    question: Where can I see every user that has been deleted from my Zendesk account?
  - id: ShowDeletedUser
    intent: Show a soft-deleted user
    question: Can I look up the details of one user that was deleted but not yet permanently removed?
  - id: PermanentlyDeleteUser
    intent: Permanently delete a deleted user
    question: How do I permanently erase a user's personal data after they have already been deleted?
  - id: CountDeletedUsers
    intent: Count deleted users
    question: How many users have been deleted from my account so far?
  - id: SearchUsers
    intent: Search users by query or external ID
    question: Can I search the agents and end users in my help desk with a search query?
  - id: ListUsers
    intent: List all users in the account
    question: What is the recommended way to page through every user in my account?
  - id: CreateUser
    intent: Create a user
    question: How do I add a new single user through the api/v2 users endpoint?
  phrasing_ops: 30
  slug: zendesk-users-api
- baseURL: https://{subdomain}.zendesk.com
  baseurl_source: declared
  description: The Views API from Zendesk — 16 operation(s) for views.
  name: Zendesk Views API
  phrasing_intents:
  - id: SearchViews
    intent: Search views by title
    question: Can I find a Zendesk view by searching its title?
  - id: ListTicketsFromView
    intent: List the tickets in a view
    question: Which tickets are currently sitting in a particular view?
  - id: ListViews
    intent: List views
    question: How do I get all shared and personal views I can use?
  - id: CreateView
    intent: Create a view
    question: Can I create a new ticket view with my own conditions?
  - id: ShowView
    intent: Get a view
    question: Where can I see the conditions and columns of one view?
  - id: UpdateView
    intent: Update a view
    question: Can I change the conditions of an existing view?
  - id: DeleteView
    intent: Delete a view
    question: Can I delete a single view I no longer need?
  - id: GetViewCount
    intent: Count tickets in one view
    question: How many tickets are in a specific view right now?
  phrasing_ops: 19
  slug: zendesk-views-api
- baseURL: https://{subdomain}.zendesk.com
  baseurl_source: declared
  description: The Workspaces API from Zendesk — 4 operation(s) for workspaces.
  name: Zendesk Workspaces API
  phrasing_intents:
  - id: ListWorkspaces
    intent: List contextual workspaces
    question: What contextual workspaces are configured for our agents?
  - id: CreateWorkspace
    intent: Create a contextual workspace
    question: How do I set up a workspace that shows certain macros and apps for billing tickets?
  - id: ShowWorkspace
    intent: Get a contextual workspace
    question: How do I view one workspace's conditions and macros?
  - id: UpdateWorkspace
    intent: Update a contextual workspace
    question: Can I change the conditions or apps on an existing workspace?
  - id: DeleteWorkspace
    intent: Delete a contextual workspace
    question: Can I delete a single workspace we don't use anymore?
  - id: DestroyManyWorkspaces
    intent: Delete several workspaces at once
    question: Can I bulk delete multiple workspaces by id?
  - id: ReorderWorkspaces
    intent: Reorder contextual workspaces
    question: Does workspace order decide which one applies first, and can I change it?
  phrasing_ops: 7
  slug: zendesk-workspaces-api
- baseURL: https://{subdomain}.zendesk.com
  baseurl_source: declared
  description: The X Channel API from Zendesk — 4 operation(s) for x channel.
  name: Zendesk X Channel API
  phrasing_intents:
  - id: ListMonitoredTwitterHandles
    intent: List monitored X handles
    question: Which X (Twitter) handles is my help desk monitoring?
  - id: ShowMonitoredTwitterHandle
    intent: Show a monitored X handle
    question: Can I view the settings of one monitored X handle?
  - id: CreateTicketFromTweet
    intent: Turn a tweet into a ticket
    question: How do I create a support ticket from a customer's tweet?
  - id: GettingTwicketStatus
    intent: Get the tweet status of a ticket's comments
    question: Can I see the X status of the tweets behind a ticket's comments?
  phrasing_ops: 4
  slug: zendesk-x-channel-api
arazzos:
- description: Confirm a ticket exists, then append a public or private comment to it.
  name: Zendesk Add Comment to Ticket
  slug: zendesk-add-comment-to-ticket-workflow
- description: Preview the changes a macro would make to a ticket, then commit them.
  name: Zendesk Apply Macro to Ticket
  slug: zendesk-apply-macro-to-ticket-workflow
- description: Find an organization by name, then attach a ticket to it for shared visibility.
  name: Zendesk Assign Organization to Ticket
  slug: zendesk-assign-organization-ticket-workflow
- description: Create a custom ticket field, then confirm it appears in the account's field list.
  name: Zendesk Create and Verify Custom Ticket Field
  slug: zendesk-create-custom-ticket-field-workflow
- description: Create a macro, then preview the changes it would make to a sample ticket.
  name: Zendesk Create Macro and Preview on Ticket
  slug: zendesk-create-macro-and-preview-workflow
- description: Create an organization, then create an end user that belongs to it.
  name: Zendesk Create Organization and User
  slug: zendesk-create-organization-and-user-workflow
- description: Look up a support group by name, then open a ticket assigned to that group.
  name: Zendesk Create Ticket and Assign Group
  slug: zendesk-create-ticket-assign-group-workflow
- description: Create an end user, then open a support ticket with that user as the requester.
  name: Zendesk Create User and Open Ticket
  slug: zendesk-create-user-and-ticket-workflow
- description: Load a ticket and escalate it by raising priority, opening it, and adding a note.
  name: Zendesk Escalate Ticket
  slug: zendesk-escalate-ticket-workflow
- description: Search macros by text, preview the match against a ticket, then commit the changes.
  name: Zendesk Find Macro and Apply to Ticket
  slug: zendesk-find-macro-and-apply-workflow
- description: Search for an existing user, then open a ticket requested by that user.
  name: Zendesk Find User and Open Ticket
  slug: zendesk-find-user-and-open-ticket-workflow
- description: Find a duplicate organization by name, then merge it into a winning organization.
  name: Zendesk Merge Duplicate Organizations
  slug: zendesk-merge-duplicate-organizations-workflow
- description: Create an organization, add a user to it, and open their first support ticket.
  name: Zendesk Onboard New Customer
  slug: zendesk-onboard-customer-workflow
- description: Find an agent by name or email, then reassign a ticket to that agent.
  name: Zendesk Reassign Ticket to Agent
  slug: zendesk-reassign-ticket-to-agent-workflow
- description: Search for a ticket, then solve it with a closing public comment.
  name: Zendesk Solve Ticket from Search
  slug: zendesk-solve-ticket-from-search-workflow
- description: Open a ticket, set tags on it, then raise its priority and status.
  name: Zendesk Tag and Prioritize New Ticket
  slug: zendesk-tag-and-prioritize-ticket-workflow
- description: List the tickets in a view and update the first one to assign and prioritize it.
  name: Zendesk Triage Tickets from a View
  slug: zendesk-triage-tickets-from-view-workflow
- description: Find an organization by exact name and update it if found, otherwise create it.
  name: Zendesk Upsert Organization by Name
  slug: zendesk-upsert-organization-by-name-workflow
- description: Find a user by email and update them if found, otherwise create a new user.
  name: Zendesk Upsert User by Email
  slug: zendesk-upsert-user-by-email-workflow
artifact_total: 405
asyncapis:
- description: Zendesk Webhooks allow you to receive real-time HTTP notifications when events occur in your Zendesk account. Webhooks are the modern replacement for legacy targets and support event types for tickets
  name: Zendesk Webhooks
  slug: zendesk-webhooks-asyncapi
collections:
- collection_type: postman
  name: Zendesk Account
  slug: postman-account-openapi-original
- collection_type: postman
  name: Zendesk Accounts
  slug: postman-accounts-openapi-original
- collection_type: postman
  name: Zendesk Activities
  slug: postman-activities-openapi-original
- collection_type: postman
  name: Zendesk Any Channel
  slug: postman-any-channel-openapi-original
- collection_type: postman
  name: Zendesk Approval Workflow Instances
  slug: postman-approval-workflow-instances-openapi-original
- collection_type: postman
  name: Zendesk Assignables
  slug: postman-assignables-openapi-original
- collection_type: postman
  name: Zendesk Attachments
  slug: postman-attachments-openapi-original
- collection_type: postman
  name: Zendesk Audit Logs
  slug: postman-audit-logs-openapi-original
- collection_type: postman
  name: Zendesk Automations
  slug: postman-automations-openapi-original
- collection_type: postman
  name: Zendesk Bookmarks
  slug: postman-bookmarks-openapi-original
- collection_type: postman
  name: Zendesk Brand Agents
  slug: postman-brand-agents-openapi-original
- collection_type: postman
  name: Zendesk Brands
  slug: postman-brands-openapi-original
- collection_type: postman
  name: Zendesk Channels
  slug: postman-channels-openapi-original
- collection_type: postman
  name: Zendesk Chat File Redactions
  slug: postman-chat-file-redactions-openapi-original
- collection_type: postman
  name: Zendesk Chat Redactions
  slug: postman-chat-redactions-openapi-original
- collection_type: postman
  name: Zendesk Comment Redactions
  slug: postman-comment-redactions-openapi-original
- collection_type: postman
  name: Zendesk Custom Objects
  slug: postman-custom-objects-openapi-original
- collection_type: postman
  name: Zendesk Custom Roles
  slug: postman-custom-roles-openapi-original
- collection_type: postman
  name: Zendesk Custom Status
  slug: postman-custom-status-openapi-original
- collection_type: postman
  name: Zendesk Custom Statuses
  slug: postman-custom-statuses-openapi-original
- collection_type: postman
  name: Zendesk Deleted Tickets
  slug: postman-deleted-tickets-openapi-original
- collection_type: postman
  name: Zendesk Deleted Users
  slug: postman-deleted-users-openapi-original
- collection_type: postman
  name: Zendesk Deletion Schedules
  slug: postman-deletion-schedules-openapi-original
- collection_type: postman
  name: Zendesk Dynamic Content
  slug: postman-dynamic-content-openapi-original
- collection_type: postman
  name: Zendesk Email Notifications
  slug: postman-email-notifications-openapi-original
- collection_type: postman
  name: Zendesk Group Memberships
  slug: postman-group-memberships-openapi-original
- collection_type: postman
  name: Zendesk Group Slas
  slug: postman-group-slas-openapi-original
- collection_type: postman
  name: Zendesk Groups
  slug: postman-groups-openapi-original
- collection_type: postman
  name: Zendesk Imports
  slug: postman-imports-openapi-original
- collection_type: postman
  name: Zendesk Incremental
  slug: postman-incremental-openapi-original
- collection_type: postman
  name: Zendesk Job Statuses
  slug: postman-job-statuses-openapi-original
- collection_type: postman
  name: Zendesk Locales
  slug: postman-locales-openapi-original
- collection_type: postman
  name: Zendesk Macros
  slug: postman-macros-openapi-original
- collection_type: postman
  name: Zendesk Oauth
  slug: postman-oauth-openapi-original
- collection_type: postman
  name: Zendesk Object Layouts
  slug: postman-object-layouts-openapi-original
- collection_type: postman
  name: Zendesk Organization Fields
  slug: postman-organization-fields-openapi-original
- collection_type: postman
  name: Zendesk Organization Memberships
  slug: postman-organization-memberships-openapi-original
- collection_type: postman
  name: Zendesk Organization Merges
  slug: postman-organization-merges-openapi-original
- collection_type: postman
  name: Zendesk Organization Subscriptions
  slug: postman-organization-subscriptions-openapi-original
- collection_type: postman
  name: Zendesk Organizations
  slug: postman-organizations-openapi-original
- collection_type: postman
  name: Zendesk Problems
  slug: postman-problems-openapi-original
- collection_type: postman
  name: Zendesk Push Notification Devices
  slug: postman-push-notification-devices-openapi-original
- collection_type: postman
  name: Zendesk Queues
  slug: postman-queues-openapi-original
- collection_type: postman
  name: Zendesk Recipient Addresses
  slug: postman-recipient-addresses-openapi-original
- collection_type: postman
  name: Zendesk Relationships
  slug: postman-relationships-openapi-original
- collection_type: postman
  name: Zendesk Requests
  slug: postman-requests-openapi-original
- collection_type: postman
  name: Zendesk Resource Collections
  slug: postman-resource-collections-openapi-original
- collection_type: postman
  name: Zendesk Routing
  slug: postman-routing-openapi-original
- collection_type: postman
  name: Zendesk Satisfaction Ratings
  slug: postman-satisfaction-ratings-openapi-original
- collection_type: postman
  name: Zendesk Satisfaction Reasons
  slug: postman-satisfaction-reasons-openapi-original
- collection_type: postman
  name: Zendesk Search
  slug: postman-search-openapi-original
- collection_type: postman
  name: Zendesk Sessions
  slug: postman-sessions-openapi-original
- collection_type: postman
  name: Zendesk Sharing Agreements
  slug: postman-sharing-agreements-openapi-original
- collection_type: postman
  name: Zendesk Skips
  slug: postman-skips-openapi-original
- collection_type: postman
  name: Zendesk Slas
  slug: postman-slas-openapi-original
- collection_type: postman
  name: Zendesk Suspended Tickets
  slug: postman-suspended-tickets-openapi-original
- collection_type: postman
  name: Zendesk Tags
  slug: postman-tags-openapi-original
- collection_type: postman
  name: Zendesk Target Failures
  slug: postman-target-failures-openapi-original
- collection_type: postman
  name: Zendesk Target Type
  slug: postman-target-type-openapi-original
- collection_type: postman
  name: Zendesk Targets
  slug: postman-targets-openapi-original
- collection_type: postman
  name: Zendesk Ticket Audits
  slug: postman-ticket-audits-openapi-original
- collection_type: postman
  name: Zendesk Ticket Content Pins
  slug: postman-ticket-content-pins-openapi-original
- collection_type: postman
  name: Zendesk Ticket Fields
  slug: postman-ticket-fields-openapi-original
- collection_type: postman
  name: Zendesk Ticket Form Statuses
  slug: postman-ticket-form-statuses-openapi-original
- collection_type: postman
  name: Zendesk Ticket Forms
  slug: postman-ticket-forms-openapi-original
- collection_type: postman
  name: Zendesk Ticket Metrics
  slug: postman-ticket-metrics-openapi-original
- collection_type: postman
  name: Zendesk Tickets
  slug: postman-tickets-openapi-original
- collection_type: postman
  name: Zendesk Trigger Categories
  slug: postman-trigger-categories-openapi-original
- collection_type: postman
  name: Zendesk Triggers
  slug: postman-triggers-openapi-original
- collection_type: postman
  name: Zendesk Uploads
  slug: postman-uploads-openapi-original
- collection_type: postman
  name: Zendesk User Fields
  slug: postman-user-fields-openapi-original
- collection_type: postman
  name: Zendesk Users
  slug: postman-users-openapi-original
- collection_type: postman
  name: Zendesk Views
  slug: postman-views-openapi-original
- collection_type: postman
  name: Zendesk Workspaces
  slug: postman-workspaces-openapi-original
- collection_type: postman
  name: Zendesk Support API
  slug: postman-zendesk-support
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Zendesk Account Account Settings API
  slug: open-zendesk-account-settings-api
- collection_type: open
  name: Zendesk Account Account Settings Activity Stream API
  slug: open-zendesk-activity-stream-api
- collection_type: open
  name: Zendesk Account Account Settings Approval Requests API
  slug: open-zendesk-approval-requests-api
- collection_type: open
  name: Zendesk Account Account Settings AssigneeFieldAssignableAgents API
  slug: open-zendesk-assigneefieldassignableagents-api
- collection_type: open
  name: Zendesk Account Account Settings AssigneeFieldAssignableGroups API
  slug: open-zendesk-assigneefieldassignablegroups-api
- collection_type: open
  name: Zendesk Account Account Settings Attachments API
  slug: open-zendesk-attachments-api
- collection_type: open
  name: Zendesk Account Account Settings Audit Logs API
  slug: open-zendesk-audit-logs-api
- collection_type: open
  name: Zendesk Account Account Settings Autocomplete API
  slug: open-zendesk-autocomplete-api
- collection_type: open
  name: Zendesk Account Account Settings Automations API
  slug: open-zendesk-automations-api
- collection_type: open
  name: Zendesk Account Account Settings Basics API
  slug: open-zendesk-basics-api
- collection_type: open
  name: Zendesk Account Account Settings Bookmarks API
  slug: open-zendesk-bookmarks-api
- collection_type: open
  name: Zendesk Account Account Settings Brand Agents API
  slug: open-zendesk-brand-agents-api
- collection_type: open
  name: Zendesk Account Account Settings Brands API
  slug: open-zendesk-brands-api
- collection_type: open
  name: Zendesk Account Account Settings Channel Framework API
  slug: open-zendesk-channel-framework-api
- collection_type: open
  name: Zendesk Account Account Settings Conversation Log API
  slug: open-zendesk-conversation-log-api
- collection_type: open
  name: Zendesk Account Account Settings Custom Object Fields API
  slug: open-zendesk-custom-object-fields-api
- collection_type: open
  name: Zendesk Account Account Settings Custom Object Records API
  slug: open-zendesk-custom-object-records-api
- collection_type: open
  name: Zendesk Account Account Settings Custom Objects API
  slug: open-zendesk-custom-objects-api
- collection_type: open
  name: Zendesk Account Account Settings Custom Roles API
  slug: open-zendesk-custom-roles-api
- collection_type: open
  name: Zendesk Account Account Settings Custom Ticket Statuses API
  slug: open-zendesk-custom-ticket-statuses-api
- collection_type: open
  name: Zendesk Account Account Settings Deletion Schedules API
  slug: open-zendesk-deletion-schedules-api
- collection_type: open
  name: Zendesk Account Account Settings Dynamic Content API
  slug: open-zendesk-dynamic-content-api
- collection_type: open
  name: Zendesk Account Account Settings Dynamic Content Item Variants API
  slug: open-zendesk-dynamic-content-item-variants-api
- collection_type: open
  name: Zendesk Account Account Settings Email Notifications API
  slug: open-zendesk-email-notifications-api
- collection_type: open
  name: Zendesk Account Account Settings Essentials Card API
  slug: open-zendesk-essentials-card-api
- collection_type: open
  name: Zendesk Account Account Settings Global Clients API
  slug: open-zendesk-global-clients-api
- collection_type: open
  name: Zendesk Account Account Settings Grant Type Tokens API
  slug: open-zendesk-grant-type-tokens-api
- collection_type: open
  name: Zendesk Account Account Settings Group Memberships API
  slug: open-zendesk-group-memberships-api
- collection_type: open
  name: Zendesk Account Account Settings Group SLA Policies API
  slug: open-zendesk-group-sla-policies-api
- collection_type: open
  name: Zendesk Account Account Settings Groups API
  slug: open-zendesk-groups-api
- collection_type: open
  name: Zendesk Account Account Settings Incremental Export API
  slug: open-zendesk-incremental-export-api
- collection_type: open
  name: Zendesk Account Account Settings Incremental Skill Based Routing API
  slug: open-zendesk-incremental-skill-based-routing-api
- collection_type: open
  name: Zendesk Account Account Settings Job Statuses API
  slug: open-zendesk-job-statuses-api
- collection_type: open
  name: Zendesk Account Account Settings Locales API
  slug: open-zendesk-locales-api
- collection_type: open
  name: Zendesk Account Account Settings Lookup Relationships API
  slug: open-zendesk-lookup-relationships-api
- collection_type: open
  name: Zendesk Account Account Settings Macros API
  slug: open-zendesk-macros-api
- collection_type: open
  name: Zendesk Account Account Settings OAuth Clients API
  slug: open-zendesk-oauth-clients-api
- collection_type: open
  name: Zendesk Account Account Settings OAuth Tokens API
  slug: open-zendesk-oauth-tokens-api
- collection_type: open
  name: Zendesk Account Account Settings Object Triggers API
  slug: open-zendesk-object-triggers-api
- collection_type: open
  name: Zendesk Account Account Settings Omnichannel Routing Queues API
  slug: open-zendesk-omnichannel-routing-queues-api
- collection_type: open
  name: Zendesk Account Account Settings Organization Fields API
  slug: open-zendesk-organization-fields-api
- collection_type: open
  name: Zendesk Account Account Settings Organization Memberships API
  slug: open-zendesk-organization-memberships-api
- collection_type: open
  name: Zendesk Account Account Settings Organization Subscriptions API
  slug: open-zendesk-organization-subscriptions-api
- collection_type: open
  name: Zendesk Account Account Settings Organizations API
  slug: open-zendesk-organizations-api
- collection_type: open
  name: Zendesk Account Account Settings Push Notification Devices API
  slug: open-zendesk-push-notification-devices-api
- collection_type: open
  name: Zendesk Account Account Settings Requests API
  slug: open-zendesk-requests-api
- collection_type: open
  name: Zendesk Account Account Settings Reseller API
  slug: open-zendesk-reseller-api
- collection_type: open
  name: Zendesk Account Account Settings Resource Collections API
  slug: open-zendesk-resource-collections-api
- collection_type: open
  name: Zendesk Account Account Settings Satisfaction Ratings API
  slug: open-zendesk-satisfaction-ratings-api
- collection_type: open
  name: Zendesk Account Account Settings Satisfaction Reasons API
  slug: open-zendesk-satisfaction-reasons-api
- collection_type: open
  name: Zendesk Account Account Settings Search API
  slug: open-zendesk-search-api
- collection_type: open
  name: Zendesk Account Account Settings Sessions API
  slug: open-zendesk-sessions-api
- collection_type: open
  name: Zendesk Account Account Settings Sharing Agreements API
  slug: open-zendesk-sharing-agreements-api
- collection_type: open
  name: Zendesk Account Account Settings Skill Based Routing API
  slug: open-zendesk-skill-based-routing-api
- collection_type: open
  name: Zendesk Account Account Settings SLA Policies API
  slug: open-zendesk-sla-policies-api
- collection_type: open
  name: Zendesk Account Account Settings Support Addresses API
  slug: open-zendesk-support-addresses-api
- collection_type: open
  name: Zendesk Support API
  slug: open-zendesk-support
- collection_type: open
  name: Zendesk Account Account Settings Suspended Tickets API
  slug: open-zendesk-suspended-tickets-api
- collection_type: open
  name: Zendesk Account Account Settings Tags API
  slug: open-zendesk-tags-api
- collection_type: open
  name: Zendesk Account Account Settings Target Failures API
  slug: open-zendesk-target-failures-api
- collection_type: open
  name: Zendesk Account Account Settings Targets API
  slug: open-zendesk-targets-api
- collection_type: open
  name: Zendesk Account Account Settings Ticket Audits API
  slug: open-zendesk-ticket-audits-api
- collection_type: open
  name: Zendesk Account Account Settings Ticket Comments API
  slug: open-zendesk-ticket-comments-api
- collection_type: open
  name: Zendesk Account Account Settings Ticket Content Pins API
  slug: open-zendesk-ticket-content-pins-api
- collection_type: open
  name: Zendesk Account Account Settings Ticket Fields API
  slug: open-zendesk-ticket-fields-api
- collection_type: open
  name: Zendesk Account Account Settings Ticket Form Statuses API
  slug: open-zendesk-ticket-form-statuses-api
- collection_type: open
  name: Zendesk Account Account Settings Ticket Forms API
  slug: open-zendesk-ticket-forms-api
- collection_type: open
  name: Zendesk Account Account Settings Ticket Import API
  slug: open-zendesk-ticket-import-api
- collection_type: open
  name: Zendesk Account Account Settings Ticket Metric Events API
  slug: open-zendesk-ticket-metric-events-api
- collection_type: open
  name: Zendesk Account Account Settings Ticket Metrics API
  slug: open-zendesk-ticket-metrics-api
- collection_type: open
  name: Zendesk Account Account Settings Ticket Skips API
  slug: open-zendesk-ticket-skips-api
- collection_type: open
  name: Zendesk Account Account Settings Tickets API
  slug: open-zendesk-tickets-api
- collection_type: open
  name: Zendesk Account Account Settings Trigger Categories API
  slug: open-zendesk-trigger-categories-api
- collection_type: open
  name: Zendesk Account Account Settings Triggers API
  slug: open-zendesk-triggers-api
- collection_type: open
  name: Zendesk Account Account Settings User Fields API
  slug: open-zendesk-user-fields-api
- collection_type: open
  name: Zendesk Account Account Settings User Identities API
  slug: open-zendesk-user-identities-api
- collection_type: open
  name: Zendesk Account Account Settings User Passwords API
  slug: open-zendesk-user-passwords-api
- collection_type: open
  name: Zendesk Account Account Settings Users API
  slug: open-zendesk-users-api
- collection_type: open
  name: Zendesk Account Account Settings Views API
  slug: open-zendesk-views-api
- collection_type: open
  name: Zendesk Account Account Settings Workspaces API
  slug: open-zendesk-workspaces-api
- collection_type: open
  name: Zendesk Account Account Settings X Channel API
  slug: open-zendesk-x-channel-api
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/zendesk/refs/heads/main/vendor-facets/zendesk-vendor-facets.yml
  title: ''
  type: VendorFacets
  url: vendor-facets/zendesk-vendor-facets.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/zendesk/refs/heads/main/rate-limits/zendesk-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/zendesk-rate-limits.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://www.zendesk.com/pricing/
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/zendesk/refs/heads/main/plans/zendesk-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/zendesk-plans-pricing.yml
- group: company
  title: ''
  type: Website
  url: https://www.zendesk.com/
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/zendesk/refs/heads/main/capabilities/zendesk-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/zendesk-capability-edges.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/zendesk/refs/heads/main/agentic-access/zendesk-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/zendesk-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/zendesk/refs/heads/main/security/zendesk-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/zendesk-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/zendesk/refs/heads/main/security/zendesk-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/zendesk-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/zendesk/refs/heads/main/authentication/zendesk-authentication.yml
  title: ''
  type: Authentication
  url: authentication/zendesk-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/zendesk/refs/heads/main/scopes/zendesk-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/zendesk-scopes.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/zendesk/refs/heads/main/security/zendesk-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/zendesk-trust-center.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/zendesk/refs/heads/main/packages/zendesk-packages.yml
  title: ''
  type: Packages
  url: packages/zendesk-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/zendesk/refs/heads/main/well-known/zendesk-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/zendesk-well-known.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/zendesk/refs/heads/main/mcp/zendesk-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/zendesk-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/zendesk/refs/heads/main/llms/zendesk-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/zendesk-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/zendesk/refs/heads/main/overlays/zendesk-support-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/zendesk-support-overlay.yaml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/zendesk/refs/heads/main/conformance/zendesk-conformance.yml
  title: ''
  type: Conformance
  url: conformance/zendesk-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/zendesk/refs/heads/main/errors/zendesk-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/zendesk-error-codes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/zendesk/refs/heads/main/lifecycle/zendesk-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/zendesk-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/zendesk/refs/heads/main/conventions/zendesk-conventions.yml
  title: ''
  type: Conventions
  url: conventions/zendesk-conventions.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/zendesk/refs/heads/main/changelog/zendesk-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/zendesk-changelog.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/zendesk/refs/heads/main/cli/zendesk-cli.yml
  title: ''
  type: CLI
  url: cli/zendesk-cli.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/zendesk/refs/heads/main/components/zendesk-components.yml
  title: ''
  type: Components
  url: components/zendesk-components.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/zendesk/refs/heads/main/data-model/zendesk-data-model.yml
  title: ''
  type: DataModel
  url: data-model/zendesk-data-model.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/zendesk/overview
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/zendesk/refs/heads/main/arazzo/zendesk-add-comment-to-ticket-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/zendesk-add-comment-to-ticket-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/zendesk/refs/heads/main/arazzo/zendesk-apply-macro-to-ticket-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/zendesk-apply-macro-to-ticket-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/zendesk/refs/heads/main/arazzo/zendesk-assign-organization-ticket-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/zendesk-assign-organization-ticket-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/zendesk/refs/heads/main/arazzo/zendesk-create-custom-ticket-field-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/zendesk-create-custom-ticket-field-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/zendesk/refs/heads/main/arazzo/zendesk-create-macro-and-preview-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/zendesk-create-macro-and-preview-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/zendesk/refs/heads/main/arazzo/zendesk-create-organization-and-user-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/zendesk-create-organization-and-user-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/zendesk/refs/heads/main/arazzo/zendesk-create-ticket-assign-group-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/zendesk-create-ticket-assign-group-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/zendesk/refs/heads/main/arazzo/zendesk-create-user-and-ticket-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/zendesk-create-user-and-ticket-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/zendesk/refs/heads/main/arazzo/zendesk-escalate-ticket-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/zendesk-escalate-ticket-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/zendesk/refs/heads/main/arazzo/zendesk-find-macro-and-apply-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/zendesk-find-macro-and-apply-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/zendesk/refs/heads/main/arazzo/zendesk-find-user-and-open-ticket-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/zendesk-find-user-and-open-ticket-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/zendesk/refs/heads/main/arazzo/zendesk-merge-duplicate-organizations-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/zendesk-merge-duplicate-organizations-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/zendesk/refs/heads/main/arazzo/zendesk-onboard-customer-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/zendesk-onboard-customer-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/zendesk/refs/heads/main/arazzo/zendesk-reassign-ticket-to-agent-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/zendesk-reassign-ticket-to-agent-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/zendesk/refs/heads/main/arazzo/zendesk-solve-ticket-from-search-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/zendesk-solve-ticket-from-search-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/zendesk/refs/heads/main/arazzo/zendesk-tag-and-prioritize-ticket-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/zendesk-tag-and-prioritize-ticket-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/zendesk/refs/heads/main/arazzo/zendesk-triage-tickets-from-view-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/zendesk-triage-tickets-from-view-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/zendesk/refs/heads/main/arazzo/zendesk-upsert-organization-by-name-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/zendesk-upsert-organization-by-name-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/zendesk/refs/heads/main/arazzo/zendesk-upsert-user-by-email-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/zendesk-upsert-user-by-email-workflow.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/zendesk
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.zendesk.com/company/agreements-and-terms/privacy-notice/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.zendesk.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.zendesk.com/company/agreements-and-terms/zendesk-customer-agreement/
- group: company
  title: ''
  type: Blog
  url: https://www.zendesk.com/help-center-closed/
- group: other
  title: ''
  type: Marketplace
  url: https://www.zendesk.com/marketplace/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.zendesk.com/pricing/featured/?variant=518&targetRedirect=true
- group: start
  title: ''
  type: Signup
  url: https://www.zendesk.com/register/
- group: auth
  title: ''
  type: Security
  url: https://www.zendesk.com/trust-center/
- group: company
  title: ''
  type: Blog
  url: https://www.zendesk.com/blog/
- group: learn
  title: ''
  type: Training
  url: https://training.zendesk.com/
- group: company
  title: ''
  type: Partners
  url: https://www.zendesk.com/partner/
- group: docs
  title: ''
  type: Documentation
  url: https://www.zendesk.com/
- group: operate
  title: ''
  type: Support
  url: https://support.zendesk.com/hc/en-us/community/topics
- group: docs
  title: ''
  type: Documentation
  url: https://developer.zendesk.com/documentation/webhooks/
- group: start
  title: ''
  type: Portal
  url: https://developer.zendesk.com/documentation
- group: docs
  title: ''
  type: Documentation
  url: https://developer.zendesk.com/api-reference/
- group: start
  title: ''
  type: Login
  url: https://www.zendesk.com/login/
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.zendesk.com/api-reference/changelog/changelog/
- group: operate
  title: ''
  type: RateLimits
  url: https://developer.zendesk.com/api-reference/introduction/rate-limits/
- group: auth
  title: ''
  type: Authentication
  url: https://developer.zendesk.com/api-reference/introduction/security-and-auth/
- group: operate
  title: ''
  type: Support
  url: https://support.zendesk.com/hc/en-us
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.zendesk.com/documentation/api-basics/getting-started/zendesk-api-resources/
- group: docs
  title: ''
  type: Documentation
  url: https://www.postman.com/zendesk-redback/zendesk-public-api/overview
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/zendesk
- group: build
  title: ''
  type: CLI
  url: https://github.com/zendesk/zcli
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/zendesk/sunshine-conversations-api-spec
created: 2025-01-08 00:00:00+00:00
description: Zendesk provides customer service and engagement software that helps businesses manage support tickets, automate workflows, and offer multi-channel supportincluding email, chat, social media, and phonethrough a unified platform.
examples:
- key_count: 6
  name: Zendesk Support Attachment Example
  slug: zendesk-support-attachment-example
- key_count: 9
  name: Zendesk Support Comment Example
  slug: zendesk-support-comment-example
- key_count: 2
  name: Zendesk Support Custom Field Example
  slug: zendesk-support-custom-field-example
- key_count: 3
  name: Zendesk Support Error Example
  slug: zendesk-support-error-example
- key_count: 10
  name: Zendesk Support Organization Create Example
  slug: zendesk-support-organization-create-example
- key_count: 14
  name: Zendesk Support Organization Example
  slug: zendesk-support-organization-example
- key_count: 10
  name: Zendesk Support Organization Update Example
  slug: zendesk-support-organization-update-example
- key_count: 20
  name: Zendesk Support Ticket Create Example
  slug: zendesk-support-ticket-create-example
- key_count: 37
  name: Zendesk Support Ticket Example
  slug: zendesk-support-ticket-example
- key_count: 15
  name: Zendesk Support Ticket Update Example
  slug: zendesk-support-ticket-update-example
- key_count: 16
  name: Zendesk Support User Create Example
  slug: zendesk-support-user-create-example
- key_count: 36
  name: Zendesk Support User Example
  slug: zendesk-support-user-example
- key_count: 16
  name: Zendesk Support User Update Example
  slug: zendesk-support-user-update-example
- key_count: 2
  name: Zendesk Support Via Example
  slug: zendesk-support-via-example
features:
- description: Unified ticket management across email, chat, phone, social media, and messaging channels in a single workspace.
  name: Omnichannel Ticketing
- description: Self-service help center with articles, sections, categories, community topics, and full-text search.
  name: Help Center and Knowledge Base
- description: Real-time chat with visitors and customers including proactive triggers, routing, departments, and chat history.
  name: Live Chat and Messaging
- description: Time-based automations and event-driven triggers to route, escalate, and resolve tickets without manual intervention.
  name: Automations and Triggers
- description: Sales CRM with contacts, leads, deals, pipelines, sequences, and activity tracking for sales teams.
  name: CRM with Zendesk Sell
- description: Cloud-based call center with IVR, call recording, voicemail, phone number management, and real-time analytics.
  name: Talk Voice Support
- description: Extend the data model with custom objects, fields, and relationships to fit unique business requirements.
  name: Custom Objects and Fields
- description: Event-driven webhooks and a marketplace of integrations for connecting Zendesk with third-party tools.
  name: Webhooks and Integrations
finops:
- name: Zendesk Finops
  service_category: Customer Service / Support
  slug: zendesk-finops
graphqls:
- description: The Zendesk Chat Conversations API lets your application act as a Zendesk Chat agent and interact with customers. It is a GraphQL API that supports WebSocket connections for real-time message exchange
  name: Zendesk GraphQL API
  slug: zendesk-graphql
image: /assets/icons/zendesk.png
integrations:
- description: Bidirectional sync between Zendesk Support and Salesforce CRM for unified customer data.
  name: Salesforce
- description: Create and manage Zendesk tickets directly from Slack channels with real-time notifications.
  name: Slack
- description: Link Zendesk tickets to Jira issues for seamless collaboration between support and engineering teams.
  name: Jira
- description: View customer order data and manage e-commerce support directly within the Zendesk agent workspace.
  name: Shopify
- description: Ecosystem of over 1,000 pre-built apps and integrations available through the Zendesk Marketplace.
  name: Zendesk Marketplace
json_schemas:
- name: Attachment
  property_count: 6
  slug: zendesk-support-attachment
- name: Comment
  property_count: 9
  slug: zendesk-support-comment
- name: CustomField
  property_count: 2
  slug: zendesk-support-custom-field
- name: Error
  property_count: 3
  slug: zendesk-support-error
- name: OrganizationCreate
  property_count: 10
  slug: zendesk-support-organization-create
- name: Organization
  property_count: 14
  slug: zendesk-support-organization
- name: OrganizationUpdate
  property_count: 10
  slug: zendesk-support-organization-update
- name: TicketCreate
  property_count: 20
  slug: zendesk-support-ticket-create
- name: Ticket
  property_count: 37
  slug: zendesk-support-ticket
- name: TicketUpdate
  property_count: 15
  slug: zendesk-support-ticket-update
- name: UserCreate
  property_count: 16
  slug: zendesk-support-user-create
- name: User
  property_count: 36
  slug: zendesk-support-user
- name: UserUpdate
  property_count: 16
  slug: zendesk-support-user-update
- name: Via
  property_count: 2
  slug: zendesk-support-via
- name: Zendesk Ticket
  property_count: 37
  slug: zendesk-ticket
- name: Zendesk User
  property_count: 36
  slug: zendesk-user
json_structures:
- name: Zendesk Support Attachment Structure
  property_count: 6
  slug: zendesk-support-attachment-structure
- name: Zendesk Support Comment Structure
  property_count: 9
  slug: zendesk-support-comment-structure
- name: Zendesk Support Custom Field Structure
  property_count: 2
  slug: zendesk-support-custom-field-structure
- name: Zendesk Support Error Structure
  property_count: 3
  slug: zendesk-support-error-structure
- name: Zendesk Support Organization Create Structure
  property_count: 10
  slug: zendesk-support-organization-create-structure
- name: Zendesk Support Organization Structure
  property_count: 14
  slug: zendesk-support-organization-structure
- name: Zendesk Support Organization Update Structure
  property_count: 10
  slug: zendesk-support-organization-update-structure
- name: Zendesk Support Ticket Create Structure
  property_count: 20
  slug: zendesk-support-ticket-create-structure
- name: Zendesk Support Ticket Structure
  property_count: 37
  slug: zendesk-support-ticket-structure
- name: Zendesk Support Ticket Update Structure
  property_count: 15
  slug: zendesk-support-ticket-update-structure
- name: Zendesk Support User Create Structure
  property_count: 16
  slug: zendesk-support-user-create-structure
- name: Zendesk Support User Structure
  property_count: 36
  slug: zendesk-support-user-structure
- name: Zendesk Support User Update Structure
  property_count: 16
  slug: zendesk-support-user-update-structure
- name: Zendesk Support Via Structure
  property_count: 2
  slug: zendesk-support-via-structure
jsonld:
- class_count: 0
  name: Zendesk Context
  property_count: 5
  slug: zendesk-context
- class_count: 0
  name: Zendesk Support Context
  property_count: 0
  slug: zendesk-support-context
layout: provider
modified: '2026-06-20'
name: Zendesk
nav: Providers
network: true
overview: 'Zendesk publishes 150 APIs on the [APIs.io](https://apis.io/) network, including Webhooks API, Account Settings API, Activity Stream API, and 147 more. Tagged areas include Chat, CRM, Help Center, Sell, and Support.


  The Zendesk catalog on APIs.io includes 1 event-driven AsyncAPI specification, 2 JSON-LD contexts, and 3 Spectral governance rulesets.


  Zendesk''s developer surface includes pricing, authentication, changelog, CLI, engineering blog, signup flow, training material, and 65 more developer resources.'
plans:
- name: Zendesk Plans Pricing
  plan_count: 7
  slug: zendesk-plans-pricing
- name: Zendesk Price Estimates
  plan_count: 0
  slug: zendesk-price-estimates
random_paper: 8
rate_limits:
- limit_count: 22
  name: Zendesk Rate Limits
  slug: zendesk-rate-limits
rules:
- effective_rule_count: 35
  extends:
  - spectral:asyncapi
  name: Zendesk API Rules
  rule_count: 8
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 7
  slug: zendesk-asyncapi-spectral-rules
- effective_rule_count: 5
  extends: []
  name: Zendesk API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: zendesk-jsonschema-spectral-rules
- effective_rule_count: 57
  extends:
  - spectral:oas
  name: Zendesk API Rules
  rule_count: 16
  severity_counts:
    error: 8
    hint: 0
    info: 0
    warn: 8
  slug: zendesk-spectral-rules
scopes:
- name: Zendesk Scopes
  scope_count: 0
  slug: zendesk-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: exemplar
  composite: 72.7
  coverage:
    artifact_dirs: 38
    catalog_earned: 76.5
    catalog_earned_first_party: 24.0
    catalog_gap: 38.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.5
  facets:
    access_clarity: 92.1
    contract_governance: 18.2
    contract_quality: 53.0
    developer_ergonomics: 58.3
    discoverability: 71.4
    operational_transparency: 78.9
  previous_composite: 72.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 3.8
      derived: 0
      marker_coverage: 0.0
      total: 80
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 45.1
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  trend: flat
  upsert:
    applies: true
    score: 61.1
screenshot: https://raw.githubusercontent.com/api-evangelist/zendesk/refs/heads/main/screenshots/zendesk-2026-06-20T165936.png
security:
- kind: authentication
  name: Zendesk Authentication
  slug: zendesk-authentication
  summary_line: http/oauth2 · 3 schemes
- kind: domain-security
  name: Zendesk Domain Security
  slug: zendesk-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Zendesk Vulnerability Disclosure
  slug: zendesk-vulnerability-disclosure
  summary_line: Bugcrowd · security.txt · contact published
- kind: trust-center
  name: Zendesk Trust Center
  slug: zendesk-trust-center
  summary_line: SOC 2 Type II, ISO 27001, ISO 27018, ISO 27701, ISO 42001, Cyber Essentials Plus, FedRAMP (LI-SaaS), HIPAA (via BAA, add-on), PCI DSS, GDPR, CCPA/CPRA
slug: zendesk
tags:
- Chat
- CRM
- Help Center
- Sell
- Support
- T1
- Talk
- Ticketing
- Zendesk
- Customer Service
- Help Desk
use_cases:
- description: Manage the full lifecycle of customer support tickets from creation through resolution across all channels.
  name: Customer Support Operations
- description: Build and maintain a searchable knowledge base for customers and agents to reduce ticket volume.
  name: Self-Service Knowledge Management
- description: Track leads, contacts, and deals through customizable sales pipelines with activity logging and forecasting.
  name: Sales Pipeline Management
- description: Route tickets to the right agents based on skills, availability, and workload using skill-based routing rules.
  name: Workforce Routing and Optimization
- description: Redact sensitive information from tickets and chats, manage audit logs, and enforce data retention policies.
  name: Compliance and Data Privacy
website: https://www.zendesk.com/
---
