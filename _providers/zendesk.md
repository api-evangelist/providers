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
  schema_version: 0.2
  score: 35.9
  scored_at: '2026-09-05'
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
  slug: zendesk-account-settings-api
- baseURL: https://{subdomain}.zendesk.com
  baseurl_source: declared
  description: The Activity Stream API from Zendesk — 3 operation(s) for activity stream.
  name: Zendesk Activity Stream API
  slug: zendesk-activity-stream-api
- baseURL: https://{subdomain}.zendesk.com
  baseurl_source: declared
  description: The Approval Requests API from Zendesk — 3 operation(s) for approval requests.
  name: Zendesk Approval Requests API
  slug: zendesk-approval-requests-api
- baseURL: https://{subdomain}.zendesk.com
  baseurl_source: declared
  description: The AssigneeFieldAssignableAgents API from Zendesk — 3 operation(s) for assigneefieldassignableagents.
  name: Zendesk AssigneeFieldAssignableAgents API
  slug: zendesk-assigneefieldassignableagents-api
- baseURL: https://{subdomain}.zendesk.com
  baseurl_source: declared
  description: The AssigneeFieldAssignableGroups API from Zendesk — 1 operation(s) for assigneefieldassignablegroups.
  name: Zendesk AssigneeFieldAssignableGroups API
  slug: zendesk-assigneefieldassignablegroups-api
- baseURL: https://{subdomain}.zendesk.com
  baseurl_source: declared
  description: The Attachments API from Zendesk — 4 operation(s) for attachments.
  name: Zendesk Attachments API
  slug: zendesk-attachments-api
- baseURL: https://{subdomain}.zendesk.com
  baseurl_source: declared
  description: The Audit Logs API from Zendesk — 3 operation(s) for audit logs.
  name: Zendesk Audit Logs API
  slug: zendesk-audit-logs-api
- baseURL: https://{subdomain}.zendesk.com
  baseurl_source: declared
  description: The Autocomplete API from Zendesk — 1 operation(s) for autocomplete.
  name: Zendesk Autocomplete API
  slug: zendesk-autocomplete-api
- baseURL: https://{subdomain}.zendesk.com
  baseurl_source: declared
  description: The Automations API from Zendesk — 6 operation(s) for automations.
  name: Zendesk Automations API
  slug: zendesk-automations-api
- baseURL: https://{subdomain}.zendesk.com
  baseurl_source: declared
  description: The Basics API from Zendesk — 3 operation(s) for basics.
  name: Zendesk Basics API
  slug: zendesk-basics-api
- baseURL: https://{subdomain}.zendesk.com
  baseurl_source: declared
  description: The Bookmarks API from Zendesk — 2 operation(s) for bookmarks.
  name: Zendesk Bookmarks API
  slug: zendesk-bookmarks-api
- baseURL: https://{subdomain}.zendesk.com
  baseurl_source: declared
  description: The Brand Agents API from Zendesk — 2 operation(s) for brand agents.
  name: Zendesk Brand Agents API
  slug: zendesk-brand-agents-api
- baseURL: https://{subdomain}.zendesk.com
  baseurl_source: declared
  description: The Brands API from Zendesk — 4 operation(s) for brands.
  name: Zendesk Brands API
  slug: zendesk-brands-api
- baseURL: https://{subdomain}.zendesk.com
  baseurl_source: declared
  description: The Channel Framework API from Zendesk — 3 operation(s) for channel framework.
  name: Zendesk Channel Framework API
  slug: zendesk-channel-framework-api
- baseURL: https://{subdomain}.zendesk.com
  baseurl_source: declared
  description: The Conversation Log API from Zendesk — 1 operation(s) for conversation log.
  name: Zendesk Conversation Log API
  slug: zendesk-conversation-log-api
- baseURL: https://{subdomain}.zendesk.com
  baseurl_source: declared
  description: The Custom Object Fields API from Zendesk — 4 operation(s) for custom object fields.
  name: Zendesk Custom Object Fields API
  slug: zendesk-custom-object-fields-api
- baseURL: https://{subdomain}.zendesk.com
  baseurl_source: declared
  description: The Custom Object Records API from Zendesk — 7 operation(s) for custom object records.
  name: Zendesk Custom Object Records API
  slug: zendesk-custom-object-records-api
- baseURL: https://{subdomain}.zendesk.com
  baseurl_source: declared
  description: The Custom Objects API from Zendesk — 3 operation(s) for custom objects.
  name: Zendesk Custom Objects API
  slug: zendesk-custom-objects-api
- baseURL: https://{subdomain}.zendesk.com
  baseurl_source: declared
  description: The Custom Roles API from Zendesk — 2 operation(s) for custom roles.
  name: Zendesk Custom Roles API
  slug: zendesk-custom-roles-api
- baseURL: https://{subdomain}.zendesk.com
  baseurl_source: declared
  description: The Custom Ticket Statuses API from Zendesk — 4 operation(s) for custom ticket statuses.
  name: Zendesk Custom Ticket Statuses API
  slug: zendesk-custom-ticket-statuses-api
- baseURL: https://{subdomain}.zendesk.com
  baseurl_source: declared
  description: The Deletion Schedules API from Zendesk — 2 operation(s) for deletion schedules.
  name: Zendesk Deletion Schedules API
  slug: zendesk-deletion-schedules-api
- baseURL: https://{subdomain}.zendesk.com
  baseurl_source: declared
  description: The Dynamic Content API from Zendesk — 3 operation(s) for dynamic content.
  name: Zendesk Dynamic Content API
  slug: zendesk-dynamic-content-api
- baseURL: https://{subdomain}.zendesk.com
  baseurl_source: declared
  description: The Dynamic Content Item Variants API from Zendesk — 4 operation(s) for dynamic content item variants.
  name: Zendesk Dynamic Content Item Variants API
  slug: zendesk-dynamic-content-item-variants-api
- baseURL: https://{subdomain}.zendesk.com
  baseurl_source: declared
  description: The Email Notifications API from Zendesk — 3 operation(s) for email notifications.
  name: Zendesk Email Notifications API
  slug: zendesk-email-notifications-api
- baseURL: https://{subdomain}.zendesk.com
  baseurl_source: declared
  description: The Essentials Card API from Zendesk — 2 operation(s) for essentials card.
  name: Zendesk Essentials Card API
  slug: zendesk-essentials-card-api
- baseURL: https://{subdomain}.zendesk.com
  baseurl_source: declared
  description: The Global Clients API from Zendesk — 3 operation(s) for global clients.
  name: Zendesk Global Clients API
  slug: zendesk-global-clients-api
- baseURL: https://{subdomain}.zendesk.com
  baseurl_source: declared
  description: The Grant Type Tokens API from Zendesk — 1 operation(s) for grant type tokens.
  name: Zendesk Grant Type Tokens API
  slug: zendesk-grant-type-tokens-api
- baseURL: https://{subdomain}.zendesk.com
  baseurl_source: declared
  description: The Group Memberships API from Zendesk — 6 operation(s) for group memberships.
  name: Zendesk Group Memberships API
  slug: zendesk-group-memberships-api
- baseURL: https://{subdomain}.zendesk.com
  baseurl_source: declared
  description: The Group SLA Policies API from Zendesk — 4 operation(s) for group sla policies.
  name: Zendesk Group SLA Policies API
  slug: zendesk-group-sla-policies-api
- baseURL: https://{subdomain}.zendesk.com
  baseurl_source: declared
  description: The Groups API from Zendesk — 4 operation(s) for groups.
  name: Zendesk Groups API
  slug: zendesk-groups-api
- baseURL: https://{subdomain}.zendesk.com
  baseurl_source: declared
  description: The Incremental Export API from Zendesk — 7 operation(s) for incremental export.
  name: Zendesk Incremental Export API
  slug: zendesk-incremental-export-api
- baseURL: https://{subdomain}.zendesk.com
  baseurl_source: declared
  description: The Incremental Skill Based Routing API from Zendesk — 3 operation(s) for incremental skill based routing.
  name: Zendesk Incremental Skill Based Routing API
  slug: zendesk-incremental-skill-based-routing-api
- baseURL: https://{subdomain}.zendesk.com
  baseurl_source: declared
  description: The Job Statuses API from Zendesk — 4 operation(s) for job statuses.
  name: Zendesk Job Statuses API
  slug: zendesk-job-statuses-api
- baseURL: https://{subdomain}.zendesk.com
  baseurl_source: declared
  description: The Locales API from Zendesk — 6 operation(s) for locales.
  name: Zendesk Locales API
  slug: zendesk-locales-api
- baseURL: https://{subdomain}.zendesk.com
  baseurl_source: declared
  description: The Lookup Relationships API from Zendesk — 2 operation(s) for lookup relationships.
  name: Zendesk Lookup Relationships API
  slug: zendesk-lookup-relationships-api
- baseURL: https://{subdomain}.zendesk.com
  baseurl_source: declared
  description: The Macros API from Zendesk — 15 operation(s) for macros.
  name: Zendesk Macros API
  slug: zendesk-macros-api
- baseURL: https://{subdomain}.zendesk.com
  baseurl_source: declared
  description: The OAuth Clients API from Zendesk — 3 operation(s) for oauth clients.
  name: Zendesk OAuth Clients API
  slug: zendesk-oauth-clients-api
- baseURL: https://{subdomain}.zendesk.com
  baseurl_source: declared
  description: The OAuth Tokens API from Zendesk — 2 operation(s) for oauth tokens.
  name: Zendesk OAuth Tokens API
  slug: zendesk-oauth-tokens-api
- baseURL: https://{subdomain}.zendesk.com
  baseurl_source: declared
  description: The Object Triggers API from Zendesk — 7 operation(s) for object triggers.
  name: Zendesk Object Triggers API
  slug: zendesk-object-triggers-api
- baseURL: https://{subdomain}.zendesk.com
  baseurl_source: declared
  description: The Omnichannel Routing Queues API from Zendesk — 4 operation(s) for omnichannel routing queues.
  name: Zendesk Omnichannel Routing Queues API
  slug: zendesk-omnichannel-routing-queues-api
- baseURL: https://{subdomain}.zendesk.com
  baseurl_source: declared
  description: The Organization Fields API from Zendesk — 3 operation(s) for organization fields.
  name: Zendesk Organization Fields API
  slug: zendesk-organization-fields-api
- baseURL: https://{subdomain}.zendesk.com
  baseurl_source: declared
  description: The Organization Memberships API from Zendesk — 7 operation(s) for organization memberships.
  name: Zendesk Organization Memberships API
  slug: zendesk-organization-memberships-api
- baseURL: https://{subdomain}.zendesk.com
  baseurl_source: declared
  description: The Organization Subscriptions API from Zendesk — 2 operation(s) for organization subscriptions.
  name: Zendesk Organization Subscriptions API
  slug: zendesk-organization-subscriptions-api
- baseURL: https://{subdomain}.zendesk.com
  baseurl_source: declared
  description: The Organizations API from Zendesk — 18 operation(s) for organizations.
  name: Zendesk Organizations API
  slug: zendesk-organizations-api
- baseURL: https://{subdomain}.zendesk.com
  baseurl_source: declared
  description: The Push Notification Devices API from Zendesk — 1 operation(s) for push notification devices.
  name: Zendesk Push Notification Devices API
  slug: zendesk-push-notification-devices-api
- baseURL: https://{subdomain}.zendesk.com
  baseurl_source: declared
  description: The Requests API from Zendesk — 5 operation(s) for requests.
  name: Zendesk Requests API
  slug: zendesk-requests-api
- baseURL: https://{subdomain}.zendesk.com
  baseurl_source: declared
  description: The Reseller API from Zendesk — 2 operation(s) for reseller.
  name: Zendesk Reseller API
  slug: zendesk-reseller-api
- baseURL: https://{subdomain}.zendesk.com
  baseurl_source: declared
  description: The Resource Collections API from Zendesk — 2 operation(s) for resource collections.
  name: Zendesk Resource Collections API
  slug: zendesk-resource-collections-api
- baseURL: https://{subdomain}.zendesk.com
  baseurl_source: declared
  description: The Satisfaction Ratings API from Zendesk — 4 operation(s) for satisfaction ratings.
  name: Zendesk Satisfaction Ratings API
  slug: zendesk-satisfaction-ratings-api
- baseURL: https://{subdomain}.zendesk.com
  baseurl_source: declared
  description: The Satisfaction Reasons API from Zendesk — 2 operation(s) for satisfaction reasons.
  name: Zendesk Satisfaction Reasons API
  slug: zendesk-satisfaction-reasons-api
- baseURL: https://{subdomain}.zendesk.com
  baseurl_source: declared
  description: The Search API from Zendesk — 3 operation(s) for search.
  name: Zendesk Search API
  slug: zendesk-search-api
- baseURL: https://{subdomain}.zendesk.com
  baseurl_source: declared
  description: The Sessions API from Zendesk — 6 operation(s) for sessions.
  name: Zendesk Sessions API
  slug: zendesk-sessions-api
- baseURL: https://{subdomain}.zendesk.com
  baseurl_source: declared
  description: The Sharing Agreements API from Zendesk — 2 operation(s) for sharing agreements.
  name: Zendesk Sharing Agreements API
  slug: zendesk-sharing-agreements-api
- baseURL: https://{subdomain}.zendesk.com
  baseurl_source: declared
  description: The Skill Based Routing API from Zendesk — 10 operation(s) for skill based routing.
  name: Zendesk Skill Based Routing API
  slug: zendesk-skill-based-routing-api
- baseURL: https://{subdomain}.zendesk.com
  baseurl_source: declared
  description: The SLA Policies API from Zendesk — 4 operation(s) for sla policies.
  name: Zendesk SLA Policies API
  slug: zendesk-sla-policies-api
- baseURL: https://{subdomain}.zendesk.com
  baseurl_source: declared
  description: The Support Addresses API from Zendesk — 3 operation(s) for support addresses.
  name: Zendesk Support Addresses API
  slug: zendesk-support-addresses-api
- baseURL: https://{subdomain}.zendesk.com
  baseurl_source: declared
  description: The Suspended Tickets API from Zendesk — 7 operation(s) for suspended tickets.
  name: Zendesk Suspended Tickets API
  slug: zendesk-suspended-tickets-api
- baseURL: https://{subdomain}.zendesk.com
  baseurl_source: declared
  description: The Tags API from Zendesk — 2 operation(s) for tags.
  name: Zendesk Tags API
  slug: zendesk-tags-api
- baseURL: https://{subdomain}.zendesk.com
  baseurl_source: declared
  description: The Target Failures API from Zendesk — 2 operation(s) for target failures.
  name: Zendesk Target Failures API
  slug: zendesk-target-failures-api
- baseURL: https://{subdomain}.zendesk.com
  baseurl_source: declared
  description: The Targets API from Zendesk — 2 operation(s) for targets.
  name: Zendesk Targets API
  slug: zendesk-targets-api
- baseURL: https://{subdomain}.zendesk.com
  baseurl_source: declared
  description: The Ticket Audits API from Zendesk — 5 operation(s) for ticket audits.
  name: Zendesk Ticket Audits API
  slug: zendesk-ticket-audits-api
- baseURL: https://{subdomain}.zendesk.com
  baseurl_source: declared
  description: The Ticket Comments API from Zendesk — 7 operation(s) for ticket comments.
  name: Zendesk Ticket Comments API
  slug: zendesk-ticket-comments-api
- baseURL: https://{subdomain}.zendesk.com
  baseurl_source: declared
  description: The Ticket Content Pins API from Zendesk — 2 operation(s) for ticket content pins.
  name: Zendesk Ticket Content Pins API
  slug: zendesk-ticket-content-pins-api
- baseURL: https://{subdomain}.zendesk.com
  baseurl_source: declared
  description: The Ticket Fields API from Zendesk — 6 operation(s) for ticket fields.
  name: Zendesk Ticket Fields API
  slug: zendesk-ticket-fields-api
- baseURL: https://{subdomain}.zendesk.com
  baseurl_source: declared
  description: The Ticket Form Statuses API from Zendesk — 5 operation(s) for ticket form statuses.
  name: Zendesk Ticket Form Statuses API
  slug: zendesk-ticket-form-statuses-api
- baseURL: https://{subdomain}.zendesk.com
  baseurl_source: declared
  description: The Ticket Forms API from Zendesk — 7 operation(s) for ticket forms.
  name: Zendesk Ticket Forms API
  slug: zendesk-ticket-forms-api
- baseURL: https://{subdomain}.zendesk.com
  baseurl_source: declared
  description: The Ticket Import API from Zendesk — 2 operation(s) for ticket import.
  name: Zendesk Ticket Import API
  slug: zendesk-ticket-import-api
- baseURL: https://{subdomain}.zendesk.com
  baseurl_source: declared
  description: The Ticket Metric Events API from Zendesk — 1 operation(s) for ticket metric events.
  name: Zendesk Ticket Metric Events API
  slug: zendesk-ticket-metric-events-api
- baseURL: https://{subdomain}.zendesk.com
  baseurl_source: declared
  description: The Ticket Metrics API from Zendesk — 2 operation(s) for ticket metrics.
  name: Zendesk Ticket Metrics API
  slug: zendesk-ticket-metrics-api
- baseURL: https://{subdomain}.zendesk.com
  baseurl_source: declared
  description: The Ticket Skips API from Zendesk — 2 operation(s) for ticket skips.
  name: Zendesk Ticket Skips API
  slug: zendesk-ticket-skips-api
- baseURL: https://{subdomain}.zendesk.com
  baseurl_source: declared
  description: The Tickets API from Zendesk — 26 operation(s) for tickets.
  name: Zendesk Tickets API
  slug: zendesk-tickets-api
- baseURL: https://{subdomain}.zendesk.com
  baseurl_source: declared
  description: The Trigger Categories API from Zendesk — 3 operation(s) for trigger categories.
  name: Zendesk Trigger Categories API
  slug: zendesk-trigger-categories-api
- baseURL: https://{subdomain}.zendesk.com
  baseurl_source: declared
  description: The Triggers API from Zendesk — 10 operation(s) for triggers.
  name: Zendesk Triggers API
  slug: zendesk-triggers-api
- baseURL: https://{subdomain}.zendesk.com
  baseurl_source: declared
  description: The User Fields API from Zendesk — 5 operation(s) for user fields.
  name: Zendesk User Fields API
  slug: zendesk-user-fields-api
- baseURL: https://{subdomain}.zendesk.com
  baseurl_source: declared
  description: The User Identities API from Zendesk — 5 operation(s) for user identities.
  name: Zendesk User Identities API
  slug: zendesk-user-identities-api
- baseURL: https://{subdomain}.zendesk.com
  baseurl_source: declared
  description: The User Passwords API from Zendesk — 2 operation(s) for user passwords.
  name: Zendesk User Passwords API
  slug: zendesk-user-passwords-api
- baseURL: https://{subdomain}.zendesk.com
  baseurl_source: declared
  description: The Users API from Zendesk — 23 operation(s) for users.
  name: Zendesk Users API
  slug: zendesk-users-api
- baseURL: https://{subdomain}.zendesk.com
  baseurl_source: declared
  description: The Views API from Zendesk — 16 operation(s) for views.
  name: Zendesk Views API
  slug: zendesk-views-api
- baseURL: https://{subdomain}.zendesk.com
  baseurl_source: declared
  description: The Workspaces API from Zendesk — 4 operation(s) for workspaces.
  name: Zendesk Workspaces API
  slug: zendesk-workspaces-api
- baseURL: https://{subdomain}.zendesk.com
  baseurl_source: declared
  description: The X Channel API from Zendesk — 4 operation(s) for x channel.
  name: Zendesk X Channel API
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
artifact_total: 404
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
  title: ''
  type: CapabilityMap
  url: capabilities/zendesk-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/zendesk-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/zendesk-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/zendesk-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/zendesk-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/zendesk-scopes.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/zendesk-trust-center.yml
- group: build
  title: ''
  type: Packages
  url: packages/zendesk-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/zendesk-well-known.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/zendesk-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/zendesk-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/zendesk-support-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/zendesk-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/zendesk-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/zendesk-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/zendesk-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/zendesk-changelog.yml
- group: build
  title: ''
  type: CLI
  url: cli/zendesk-cli.yml
- group: design
  title: ''
  type: Components
  url: components/zendesk-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/zendesk-data-model.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/zendesk/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/zendesk-add-comment-to-ticket-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/zendesk-apply-macro-to-ticket-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/zendesk-assign-organization-ticket-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/zendesk-create-custom-ticket-field-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/zendesk-create-macro-and-preview-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/zendesk-create-organization-and-user-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/zendesk-create-ticket-assign-group-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/zendesk-create-user-and-ticket-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/zendesk-escalate-ticket-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/zendesk-find-macro-and-apply-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/zendesk-find-user-and-open-ticket-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/zendesk-merge-duplicate-organizations-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/zendesk-onboard-customer-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/zendesk-reassign-ticket-to-agent-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/zendesk-solve-ticket-from-search-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/zendesk-tag-and-prioritize-ticket-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/zendesk-triage-tickets-from-view-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/zendesk-upsert-organization-by-name-workflow.yml
- group: design
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
  url: https://www.zendesk.com/help-center-closed/?utm_source=helpcenter-closed&utm_medium=poweredbyzendesk&utm_campaign=text&utm_content=developerblog.zendesk.com
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
  url: https://training.zendesk.com/?_gl=1*bjm8lh*_gcl_au*NzkzMDYzNTc4LjE3NTQzMzc4ODI.*_ga*ODQ3OTgwMzk0LjE3NTQzMzc4NDA.*_ga_FBP7C61M6Z*czE3NTQzMzc4ODkkbzEkZzEkdDE3NTQzMzgwODckajQ0JGwwJGgw
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
overview: 'Zendesk publishes 81 APIs on the [APIs.io](https://apis.io/) network, including Webhooks API, Account Settings API, Activity Stream API, and 78 more. Tagged areas include Chat, CRM, Help Center, Sell, and Support.


  The Zendesk catalog on APIs.io includes 1 event-driven AsyncAPI specification, 2 JSON-LD contexts, and 3 Spectral governance rulesets.


  Zendesk''s developer surface includes authentication, changelog, CLI, engineering blog, pricing, signup flow, training material, and 60 more developer resources.'
plans:
- name: Zendesk Plans Pricing
  plan_count: 7
  slug: zendesk-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 17
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
  band: strong
  composite: 55.7
  coverage:
    artifact_dirs: 36
    catalog_earned: 55.5
    catalog_earned_first_party: 0.0
    catalog_gap: 59.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 68.4
    commercial_clarity: 68.4
    contract_governance: 18.2
    contract_quality: 56.6
    developer_ergonomics: 58.3
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 55.3
  previous_composite: 55.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 80
    mcp: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
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
- Tickets
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
website: https://developer.zendesk.com/documentation
---
