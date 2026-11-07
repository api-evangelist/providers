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
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: mostly
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 28.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 185
  human_in_the_loop: 1
  name: Trello Agentic Access
  operation_count: 362
  slug: trello-agentic-access
  summary_line: 362 operations · 185 acting · 1 human-in-the-loop
api_count: 2
apis:
- baseURL: https://api.trello.com
  baseurl_source: declared
  description: The Trello Webhooks API allows developers to receive real-time notifications when changes occur on Trello models such as boards, lists, and cards. Rather than polling the REST API for updates, webhook
  name: Trello Webhooks API
  slug: webhooks-api
- description: Trello Power-Ups are a framework for extending and integrating with the Trello platform. Power-Ups allow developers to add custom functionality to Trello boards, including custom fields, board buttons
  name: Trello Power-Ups
  slug: power-ups
- baseURL: https://api.trello.com
  baseurl_source: declared
  description: Operations for retrieving and managing actions, which represent activity events that occur on Trello objects such as boards, lists, and cards.
  name: trello Actions API
  phrasing_intents:
  - id: getAction
    intent: Get an activity event
    question: How do I look up a single Trello action, like a comment or card move, by its id?
  - id: updateAction
    intent: Edit the text of a comment action
    question: How do I edit a comment when I only have the action id?
  - id: deleteAction
    intent: Delete a comment action
    question: How do I delete a comment using its action id?
  - id: getActionField
    intent: Get one field of an action
    question: Can I read just the date or type of an action without the rest?
  - id: getActionBoard
    intent: Find the board an action happened on
    question: Which board did a given activity event happen on?
  - id: getActionCard
    intent: Find the card an action relates to
    question: Which card was an activity event about?
  - id: getActionList
    intent: Find the list an action relates to
    question: Which list was involved in an activity event?
  - id: getActionMember
    intent: Get the member an action was about
    question: Who was the subject of an activity event, such as the person added to a card?
  phrasing_ops: 18
  slug: trello-actions-api
- baseURL: https://api.trello.com
  baseurl_source: declared
  description: Operations for creating, retrieving, updating, and deleting boards, as well as managing board memberships, lists, cards, labels, and other board-level resources.
  name: trello Boards API
  phrasing_intents:
  - id: createBoard
    intent: Create a board
    question: How do I create a new Trello board with a name and description?
  - id: getBoard
    intent: Get a board's details
    question: How do I fetch a board along with its lists, cards and labels in one call?
  - id: updateBoard
    intent: Update a board's settings
    question: How do I rename a board or change its description?
  - id: deleteBoard
    intent: Permanently delete a board
    question: How do I permanently delete a board?
  - id: getBoardActions
    intent: List recent activity on a board
    question: How do I see the recent activity feed for a board?
  - id: getBoardCards
    intent: List all cards on a board
    question: How do I get every card on a board?
  - id: getBoardCardsFilter
    intent: List a board's cards by status
    question: How do I get only the open or only the archived cards on a board?
  - id: getBoardChecklists
    intent: List all checklists on a board
    question: How do I pull every checklist across a whole board?
  phrasing_ops: 43
  slug: trello-boards-api
- baseURL: https://api.trello.com
  baseurl_source: declared
  description: Operations for creating, retrieving, updating, and deleting cards, including managing card attachments, checklists, comments, labels, members, and stickers.
  name: trello Cards API
  phrasing_intents:
  - id: createCard
    intent: Create a card on a list
    question: How do I add a new card to a list on my Trello board?
  - id: getCard
    intent: Get a card's details
    question: How can I fetch everything about a single card, including its checklists and attachments?
  - id: updateCard
    intent: Update a card's fields
    question: How do I rename a card or change its description after it exists?
  - id: deleteCard
    intent: Permanently delete a card
    question: How do I permanently delete a card rather than archive it?
  - id: getCardActions
    intent: List activity on a card
    question: Where can I see the activity history of a card?
  - id: createCardComment
    intent: Comment on a card
    question: How do I post a comment on a card through the API?
  - id: getCardAttachments
    intent: List a card's attachments
    question: Which files and links are attached to a card?
  - id: createCardAttachment
    intent: Attach a file or link to a card
    question: How do I attach a URL or upload a file to a card?
  phrasing_ops: 45
  slug: trello-cards-api
- baseURL: https://api.trello.com
  baseurl_source: declared
  description: Operations for creating, retrieving, updating, and deleting checklists and their check items on cards.
  name: trello Checklists API
  phrasing_intents:
  - id: createChecklist
    intent: Add a checklist to a card
    question: How do I add a checklist to a Trello card?
  - id: getChecklist
    intent: Get a checklist with its items
    question: How do I fetch a whole checklist including its check items?
  - id: updateChecklist
    intent: Rename or reorder a checklist
    question: Can I rename a checklist on a card?
  - id: deleteChecklist
    intent: Delete a checklist
    question: How do I delete an entire checklist from a card?
  - id: getChecklistCheckItems
    intent: List the items on a checklist
    question: What items are on a checklist, and which are done?
  - id: createCheckItem
    intent: Add an item to a checklist
    question: How do I add a to-do item to an existing checklist?
  - id: getCheckItem
    intent: Get a single checklist item
    question: How do I check whether one specific checklist item is complete?
  - id: deleteCheckItem
    intent: Remove an item from a checklist
    question: How do I delete a single item from a checklist without deleting the checklist?
  phrasing_ops: 12
  slug: trello-checklists-api
- baseURL: https://api.trello.com
  baseurl_source: declared
  description: Operations for creating, retrieving, updating, and deleting labels on boards and cards.
  name: trello Labels API
  phrasing_intents:
  - id: createLabel
    intent: Create a label on a board
    question: How do I add a new colored label to a Trello board?
  - id: getLabel
    intent: Get a label
    question: How do I look up a label's name and color by its id?
  - id: updateLabel
    intent: Rename or recolor a label
    question: Can I change both a label's name and color in one request?
  - id: deleteLabel
    intent: Delete a label
    question: How do I delete a label from a board?
  - id: put-labels-id-field
    intent: Set a single field on a label
    question: Can I update one label field by naming it in the URL?
  phrasing_ops: 5
  slug: trello-labels-api
- baseURL: https://api.trello.com
  baseurl_source: declared
  description: Operations for creating, retrieving, updating, and archiving lists on boards.
  name: trello Lists API
  phrasing_intents:
  - id: createList
    intent: Create a list on a board
    question: How do I create a new list on a board by passing the board id?
  - id: getList
    intent: Get a list's details
    question: How do I look up one list by its id?
  - id: updateList
    intent: Update a list's name, position or status
    question: How do I change several things about a list at once, like its name and position?
  - id: getListActions
    intent: List activity on a list
    question: What has happened on a list recently?
  - id: getListBoard
    intent: Find the board a list belongs to
    question: Which board is a list on?
  - id: getListCards
    intent: List the cards in a list
    question: How do I get all the cards in one column?
  - id: archiveAllListCards
    intent: Archive every card in a list
    question: How do I archive all the cards in a list at once?
  - id: moveAllListCards
    intent: Move every card in a list elsewhere
    question: How do I move all the cards from one list to another?
  phrasing_ops: 11
  slug: trello-lists-api
- baseURL: https://api.trello.com
  baseurl_source: declared
  description: Operations for retrieving and updating member profiles, boards, organizations, and notification settings.
  name: trello Members API
  phrasing_intents:
  - id: getMember
    intent: Look up a Trello member profile
    question: How do I look up a Trello user's profile by their username?
  - id: updateMember
    intent: Update a member's profile name, initials or bio
    question: How do I change my full name on my Trello profile through the API?
  - id: getMemberBoards
    intent: List the boards a member can access
    question: Which boards does a given Trello user have access to?
  - id: getMemberCards
    intent: List the cards assigned to a member
    question: What cards is a particular person assigned to across all boards?
  - id: getMemberOrganizations
    intent: List the workspaces a member belongs to
    question: Which Workspaces is a user a member of?
  - id: get-members-id-field
    intent: Read a single profile field of a member
    question: Can I fetch just one property of a member, like their username, instead of the whole profile?
  - id: get-members-id-actions
    intent: List a member's activity actions
    question: How can I see the recent activity a Trello user has performed?
  - id: get-members-id-boardbackgrounds
    intent: List a member's board backgrounds
    question: Where can I see the board backgrounds a member has uploaded under boardBackgrounds?
  phrasing_ops: 45
  slug: trello-members-api
- baseURL: https://api.trello.com
  baseurl_source: declared
  description: Operations for retrieving and managing member notifications about activity on boards, cards, and other Trello objects.
  name: trello Notifications API
  phrasing_intents:
  - id: getMemberNotifications
    intent: List a member's notifications
    question: How do I list a person's Trello notifications?
  - id: getNotification
    intent: Get a single notification
    question: How do I fetch one notification by its id?
  - id: updateNotification
    intent: Update a notification's unread flag
    question: Can I update a notification object to flip whether it is unread?
  - id: markAllNotificationsRead
    intent: Mark all my notifications as read
    question: How do I clear all my Trello notifications at once?
  - id: get-notifications-id-field
    intent: Read one field of a notification
    question: Can I read just the type or date of a notification?
  - id: put-notifications-id-unread
    intent: Set a notification's read status
    question: Is there a dedicated unread endpoint to mark just one notification as read?
  - id: get-notifications-id-board
    intent: Get the board a notification is about
    question: Which board did this notification come from?
  - id: get-notifications-id-card
    intent: Get the card a notification is about
    question: Which card is this notification about?
  phrasing_ops: 12
  slug: trello-notifications-api
- baseURL: https://api.trello.com
  baseurl_source: declared
  description: Operations for creating, retrieving, updating, and deleting Trello workspaces (organizations), including managing workspace members and settings.
  name: trello Organizations API
  phrasing_intents:
  - id: createOrganization
    intent: Create a new Workspace
    question: How do I create a new Trello Workspace from code?
  - id: getOrganization
    intent: Get a Workspace's details
    question: How do I look up a Workspace by its id or short name?
  - id: updateOrganization
    intent: Update a Workspace's name, description or website
    question: Can I rename a Workspace or change its URL short name?
  - id: deleteOrganization
    intent: Permanently delete a Workspace
    question: What happens to the boards when I delete a Workspace?
  - id: getOrganizationBoards
    intent: List the boards in a Workspace
    question: Which boards live inside a given Workspace?
  - id: getOrganizationMembers
    intent: List the members of a Workspace
    question: Who belongs to a particular Trello Workspace?
  - id: put-organizations-id-members
    intent: Invite someone to a Workspace by email
    question: How do I add a new person to a Workspace using their email address?
  - id: updateOrganizationMember
    intent: Change a member's role in a Workspace
    question: How do I promote an existing Workspace member to admin?
  phrasing_ops: 26
  slug: trello-organizations-api
- baseURL: https://api.trello.com
  baseurl_source: declared
  description: Operations for managing Power-Up plugins, including listing, updating, and creating plugin marketplace listings.
  name: trello Plugins API
  phrasing_intents:
  - id: getPlugin
    intent: Get a Power-Up
    question: How do I look up my Power-Up's details by its id?
  - id: updatePlugin
    intent: Update a Power-Up
    question: How do I update my Power-Up's information?
  - id: createPluginListing
    intent: Create a marketplace listing for a Power-Up
    question: How do I publish a marketplace listing for my Power-Up?
  - id: get-plugins-id
    intent: Get a Power-Up (trailing-slash endpoint)
    question: Is there a trailing-slash plugins path variant for fetching a plugin?
  - id: put-plugins-id
    intent: Update a Power-Up (trailing-slash endpoint)
    question: Is there a trailing-slash plugins path variant for updating a plugin?
  - id: post-plugins-idplugin-listing
    intent: Add a localized listing for a Power-Up
    question: How do I add a listing for my Power-Up in another language?
  - id: get-plugins-id-compliance-memberprivacy
    intent: Check a Power-Up's member privacy compliance
    question: Which members has my Power-Up been asked to erase personal data for?
  - id: put-plugins-idplugin-listings-idlisting
    intent: Update a Power-Up's listing
    question: How do I edit an existing marketplace listing for my Power-Up?
  phrasing_ops: 8
  slug: trello-plugins-api
- baseURL: https://api.trello.com
  baseurl_source: declared
  description: Operations for searching across Trello boards, cards, members, and organizations using query strings.
  name: trello Search API
  phrasing_intents:
  - id: search
    intent: Search boards, cards, members and workspaces
    question: How do I search across all my Trello boards and cards for a keyword?
  - id: searchMembers
    intent: Search for people by name
    question: How do I find a Trello user by name or username?
  - id: get-search-members
    intent: Search members (trailing-slash endpoint)
    question: Is there a /search/members/ endpoint with a trailing slash for member lookup?
  phrasing_ops: 3
  slug: trello-search-api
- baseURL: https://api.trello.com
  baseurl_source: declared
  description: Operations for retrieving and deleting API tokens and their associated webhooks.
  name: trello Tokens API
  phrasing_intents:
  - id: getToken
    intent: Inspect an API token
    question: How do I check what permissions and expiry an API token has?
  - id: deleteToken
    intent: Revoke an API token and its webhooks
    question: How do I revoke a Trello API token?
  - id: getTokenWebhooks
    intent: List webhooks created by a token
    question: Which webhooks has my token registered?
  - id: createTokenWebhook
    intent: Create a webhook under a token
    question: How do I get notified when a board or card changes?
  - id: get-tokens-token-member
    intent: Find who owns a token
    question: Which member does an API token belong to?
  - id: get-tokens-token-webhooks-idwebhook
    intent: Get one webhook created by a token
    question: How do I see the callback URL and model for one of my token's webhooks?
  - id: delete-tokens-token-webhooks-idwebhook
    intent: Delete a webhook created by a token
    question: How do I stop a webhook from sending callbacks?
  - id: tokenstokenwebhooks-1
    intent: Update a webhook created by a token
    question: How do I point an existing webhook at a new callback URL?
  phrasing_ops: 9
  slug: trello-tokens-api
- baseURL: https://api.trello.com
  baseurl_source: declared
  description: Operations for creating, retrieving, updating, and deleting webhooks that deliver real-time notifications when Trello models change.
  name: trello Webhooks API
  phrasing_intents:
  - id: createWebhook
    intent: Create a webhook on a Trello model
    question: How do I get notified at my URL whenever a board changes?
  - id: getWebhook
    intent: Get a webhook's configuration
    question: How do I check which URL and model a webhook is pointed at?
  - id: updateWebhook
    intent: Change a webhook's URL, model or active state
    question: Can I point an existing webhook at a new callback URL?
  - id: deleteWebhook
    intent: Delete a webhook
    question: How do I stop Trello from sending events to my endpoint for good?
  - id: post-webhooks
    intent: Create a webhook via the trailing-slash endpoint
    question: Does POST /webhooks/ with the trailing slash create a webhook the same way?
  - id: webhooksidfield
    intent: Read one field of a webhook
    question: Can I read just the callback URL field of a webhook?
  phrasing_ops: 6
  slug: trello-webhooks-api
- baseURL: https://api.trello.com
  baseurl_source: declared
  description: The Applications API from Trello — 1 operation(s) for applications.
  name: Trello Applications API
  phrasing_intents:
  - id: applications-key-compliance
    intent: Get an application's compliance data
    question: How do I check data compliance obligations for my Trello app?
  phrasing_ops: 1
  slug: trello-applications-api
- baseURL: https://api.trello.com
  baseurl_source: declared
  description: The Batch API from Trello — 1 operation(s) for batch.
  name: Trello Batch API
  phrasing_intents:
  - id: get-batch
    intent: Run up to 10 GET requests in one call
    question: How can I combine several Trello GET requests into one API call?
  phrasing_ops: 1
  slug: trello-batch-api
- baseURL: https://api.trello.com
  baseurl_source: declared
  description: The Emoji API from Trello — 1 operation(s) for emoji.
  name: Trello Emoji API
  phrasing_intents:
  - id: emoji
    intent: List available emoji
    question: Which emoji can I use for reactions in Trello?
  phrasing_ops: 1
  slug: trello-emoji-api
- baseURL: https://api.trello.com
  baseurl_source: declared
  description: The Enterprises API from Trello — 19 operation(s) for enterprises.
  name: Trello Enterprises API
  phrasing_intents:
  - id: get-enterprises-id
    intent: Get an Enterprise's details
    question: How do I fetch the details of our Trello Enterprise account?
  - id: get-enterprises-id-auditlog
    intent: Get an Enterprise's audit log
    question: Where can I pull the audit log of admin actions in our Enterprise?
  - id: get-enterprises-id-admins
    intent: List an Enterprise's admins
    question: Who are the admins of our Enterprise?
  - id: get-enterprises-id-signupurl
    intent: Get an Enterprise's signup URL
    question: How do I get the link people use to sign up to our Enterprise?
  - id: get-users-id
    intent: Query an Enterprise's users by license and activity
    question: Which enterprise users are licensed versus board guests only?
  - id: get-enterprises-id-members
    intent: List an Enterprise's members
    question: How do I list every member of our Enterprise with sorting and paging?
  - id: get-enterprises-id-members-idmember
    intent: Get one member of an Enterprise
    question: How do I look up a single person inside our Enterprise?
  - id: get-enterprises-id-transferrable-organization-idOrganization
    intent: Check if one Workspace can move to an Enterprise
    question: Can this particular Workspace be transferred into our Enterprise?
  phrasing_ops: 21
  slug: trello-enterprises-api
- baseURL: https://api.trello.com
  baseurl_source: declared
  description: Operations for creating, retrieving, updating, and deleting custom field definitions and their values on boards and cards.
  name: Trello Custom Fields API
  phrasing_intents:
  - id: createCustomField
    intent: Create a custom field on a board
    question: How do I add a new custom field, like a dropdown or number, to a board?
  - id: getCustomField
    intent: Get a custom field definition
    question: How do I look up a custom field's type and name?
  - id: updateCustomField
    intent: Rename or reposition a custom field
    question: Can I rename a custom field after it's been created?
  - id: deleteCustomField
    intent: Delete a custom field and its values
    question: What happens to card values when I delete a custom field?
  - id: getCardCustomFieldItems
    intent: Get the custom field values on a card
    question: Which custom field values are filled in on a card?
  - id: updateCardCustomFieldItem
    intent: Set a custom field value on a card
    question: How do I fill in a custom field value on a specific card?
  - id: get-customfields-id-options
    intent: Add an option to a dropdown custom field
    question: How do I add a new choice to an existing dropdown field?
  - id: post-customfields-id-options
    intent: List the options of a dropdown custom field
    question: What choices are available in a dropdown custom field?
  phrasing_ops: 10
  slug: trello-custom-fields-api
artifact_total: 75
asyncapis:
- description: The Trello Webhooks API delivers real-time notifications when changes occur on Trello models such as boards, lists, cards, and members. Rather than polling the REST API for updates, webhooks push even
  name: Trello Webhooks Events
  slug: trello-webhooks-asyncapi
collections:
- collection_type: open
  name: Trello REST Actions API
  slug: open-trello-actions-api
- collection_type: open
  name: Trello REST Actions Boards API
  slug: open-trello-boards-api
- collection_type: open
  name: Trello REST Actions Cards API
  slug: open-trello-cards-api
- collection_type: open
  name: Trello REST Actions Checklists API
  slug: open-trello-checklists-api
- collection_type: open
  name: Trello REST Actions CustomFields API
  slug: open-trello-customfields-api
- collection_type: open
  name: Trello REST Actions Labels API
  slug: open-trello-labels-api
- collection_type: open
  name: Trello REST Actions Lists API
  slug: open-trello-lists-api
- collection_type: open
  name: Trello REST Actions Members API
  slug: open-trello-members-api
- collection_type: open
  name: Trello REST Actions Notifications API
  slug: open-trello-notifications-api
- collection_type: open
  name: Trello REST Actions Organizations API
  slug: open-trello-organizations-api
- collection_type: open
  name: Trello REST Actions Plugins API
  slug: open-trello-plugins-api
- collection_type: open
  name: Trello REST API
  slug: open-trello-rest-api
- collection_type: open
  name: Trello REST Actions Search API
  slug: open-trello-search-api
- collection_type: open
  name: Trello REST Actions Tokens API
  slug: open-trello-tokens-api
- collection_type: open
  name: Trello REST Actions Webhooks API
  slug: open-trello-webhooks-api
common:
- group: other
  href: https://artifacts.apis.io/trello/capabilities/trello-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/trello-capability-edges.yml
- group: company
  title: ''
  type: Website
  url: https://trello.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.atlassian.com/cloud/trello/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.atlassian.com/cloud/trello/rest/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.atlassian.com/cloud/trello/rest/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.atlassian.com/cloud/trello/guides/rest-api/api-introduction/
- group: operate
  title: ''
  type: Support
  url: https://support.atlassian.com/trello/
- group: operate
  title: ''
  type: Community
  url: https://community.developer.atlassian.com/c/trello/
- group: company
  title: ''
  type: Blog
  url: https://www.atlassian.com/blog/trello
- group: operate
  title: ''
  type: Roadmap
  url: https://www.atlassian.com/roadmap/cloud?products=trello
- group: commercial
  title: ''
  type: Pricing
  url: https://trello.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://trello.com/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.atlassian.com/legal/cloud-terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.atlassian.com/legal/privacy-policy
- group: commercial
  href: https://artifacts.apis.io/trello/plans/trello-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/trello-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/trello/rate-limits/trello-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/trello-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/trello/finops/trello-finops.yml
  title: ''
  type: FinOps
  url: finops/trello-finops.yml
- group: build
  href: https://artifacts.apis.io/trello/packages/trello-packages.yml
  title: ''
  type: Packages
  url: packages/trello-packages.yml
- group: build
  href: https://artifacts.apis.io/trello/packages/trello-packages.yml
  title: ''
  type: SDKs
  url: packages/trello-packages.yml
- group: design
  href: https://artifacts.apis.io/trello/components/trello-components.yml
  title: ''
  type: Components
  url: components/trello-components.yml
- group: agent
  href: https://artifacts.apis.io/trello/well-known/trello-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/trello-well-known.yml
- group: auth
  href: https://artifacts.apis.io/trello/well-known/trello-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/trello-security.txt
- group: auth
  href: https://artifacts.apis.io/trello/security/trello-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/trello-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/trello/conformance/trello-conformance.yml
  title: ''
  type: Compliance
  url: conformance/trello-conformance.yml
- group: design
  href: https://artifacts.apis.io/trello/conformance/trello-conformance.yml
  title: ''
  type: Conformance
  url: conformance/trello-conformance.yml
- group: design
  href: https://artifacts.apis.io/trello/lifecycle/trello-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/trello-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://trello.status.atlassian.com/
- group: operate
  href: https://artifacts.apis.io/trello/lifecycle/trello-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/trello-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/trello/changelog/trello-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/trello-changelog.yml
- group: design
  href: https://artifacts.apis.io/trello/conventions/trello-conventions.yml
  title: ''
  type: Conventions
  url: conventions/trello-conventions.yml
- group: design
  href: https://artifacts.apis.io/trello/errors/trello-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/trello-problem-types.yml
- group: design
  href: https://artifacts.apis.io/trello/data-model/trello-data-model.yml
  title: ''
  type: DataModel
  url: data-model/trello-data-model.yml
- group: agent
  href: https://artifacts.apis.io/trello/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/trello/llms/trello-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/trello-llms.txt
- group: other
  href: https://artifacts.apis.io/trello/overlays/trello-rest-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/trello-rest-api-overlay.yaml
- group: docs
  href: https://artifacts.apis.io/trello/asyncapi/trello-webhooks-asyncapi.yml
  title: ''
  type: AsyncAPI
  url: asyncapi/trello-webhooks-asyncapi.yml
- group: design
  title: ''
  type: Webhooks
  url: https://developer.atlassian.com/cloud/trello/guides/rest-api/webhooks/
- group: build
  href: https://artifacts.apis.io/trello/examples/trello-get-board-cards-example.json
  title: ''
  type: Examples
  url: examples/trello-get-board-cards-example.json
- group: auth
  href: https://artifacts.apis.io/trello/scopes/trello-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/trello-scopes.yml
- group: agent
  href: https://artifacts.apis.io/trello/agentic-access/trello-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/trello-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/trello/security/trello-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/trello-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/trello/security/trello-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/trello-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/trello/security/trello-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/trello-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/trello/authentication/trello-authentication.yml
  title: ''
  type: Authentication
  url: authentication/trello-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/trello
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/atlassian
- group: design
  href: https://artifacts.apis.io/trello/json-ld/trello-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/trello-context.jsonld
- group: docs
  href: https://artifacts.apis.io/trello/json-schema/trello-board-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/trello-board-schema.json
- group: docs
  href: https://artifacts.apis.io/trello/json-schema/trello-card-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/trello-card-schema.json
- group: docs
  href: https://artifacts.apis.io/trello/json-schema/trello-webhook-payload-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/trello-webhook-payload-schema.json
- group: design
  href: https://artifacts.apis.io/trello/json-structure/trello-board-structure.json
  title: ''
  type: JSONStructure
  url: json-structure/trello-board-structure.json
- group: design
  href: https://artifacts.apis.io/trello/json-structure/trello-card-structure.json
  title: ''
  type: JSONStructure
  url: json-structure/trello-card-structure.json
- group: design
  href: https://artifacts.apis.io/trello/rules/trello-spectral-rules.yml
  title: ''
  type: SpectralRules
  url: rules/trello-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/trello/vocabulary/trello-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/trello-vocabulary.yml
created: '2026-05-03'
description: Trello is a web-based, kanban-style, list-making application from Atlassian that lets teams organize tasks, projects and workflows as boards, lists and cards. Its public REST API v1 at https://api.trello.com/1 exposes 261 operations across boards, lists, cards, checklists, labels, custom fields, attachments, members, workspaces, enterprises, actions, notifications, search, webhooks, tokens and Power-Up plugins, with a first-party OpenAPI 3.0.0 definition published by Atlassian. Authorization is an API key plus user token, or OAuth 2.0 3LO with ten granular scopes, generally available since 15 September 2026. Trello also ships a webhook surface signed with HMAC-SHA1, a browser client library (client.js), and the Power-Ups framework for extending the Trello board UI. The platform publishes no MCP server and no A2A agent card, no idempotency mechanism and no rate-limit response headers.
features:
- 'Free: up to 10 boards per workspace, unlimited cards'
- 'Standard at $5/user/mo: unlimited boards, AI quick capture, custom fields'
- 'Premium at $10/user/mo: AI, multiple views (Timeline/Calendar/Table)'
- 'Enterprise at $17.50/user/mo: org-wide permissions, SSO via Atlassian Guard'
- REST API at api.trello.com/1
- 'Per API key: 300 req/10s'
- 'Per token: 100 req/10s'
- 'Search: 50 req/min'
- 'Webhook deliveries: 600 events/min'
- Power-Ups for board extensions
- Butler automation (rules, buttons, scheduled commands)
- Card mirroring (Standard+)
- OAuth 1.0a + API key/token
- Webhooks for board, list, card, member events
- Atlassian-owned (Confluence/Jira ecosystem)
- iOS, Android, desktop apps
finops:
- has_sources: true
  method: derived
  name: Trello Finops
  primary_unit: user
  service_category: ''
  slug: trello-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/trello.png
json_schemas:
- name: Trello Board
  property_count: 17
  slug: trello-board
- name: Trello Card
  property_count: 24
  slug: trello-card
- name: Trello Webhook Payload
  property_count: 2
  slug: trello-webhook-payload
json_structures:
- name: Trello Board Structure
  property_count: 0
  slug: trello-board-structure
- name: Trello Card Structure
  property_count: 0
  slug: trello-card-structure
jsonld:
- class_count: 0
  name: Trello Context
  property_count: 13
  slug: trello-context
layout: provider
modified: '2026-09-17'
name: Trello
nav: Providers
network: true
overview: 'Trello publishes 20 API contracts indexed on the [APIs.io](https://apis.io/) network, including Webhooks API, Actions API, Boards API, and 17 more. Tagged areas include Project Management, Kanban, Task Management, Collaboration, and Productivity.


  The Trello catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 3 Spectral governance rulesets.


  Trello''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 47 more developer resources.'
plans:
- name: Trello Plans Pricing
  plan_count: 4
  slug: trello-plans-pricing
- name: Trello Price Estimates
  plan_count: 0
  slug: trello-price-estimates
random_paper: 10
rate_limits:
- limit_count: 5
  name: Trello Rate Limits
  slug: trello-rate-limits
rules:
- authorship: generated
  effective_rule_count: 35
  extends:
  - spectral:asyncapi
  name: Trello — asyncapi rules
  rule_count: 8
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 7
  slug: trello-asyncapi-spectral-rules
- authorship: generated
  effective_rule_count: 6
  extends: []
  name: Trello — jsonschema rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: trello-jsonschema-spectral-rules
- authorship: generated
  effective_rule_count: 61
  extends:
  - spectral:oas
  name: Trello API Rules
  rule_count: 20
  severity_counts:
    error: 4
    hint: 0
    info: 2
    warn: 14
  slug: trello-spectral-rules
scopes:
- name: Trello Scopes
  scope_count: 10
  slug: trello-scopes
  summary_line: 10 scopes · authorizationCode
score:
  band: exemplar
  composite: 75.6
  coverage:
    artifact_dirs: 37
    catalog_earned: 81.0
    catalog_earned_first_party: 24.0
    catalog_gap: 34.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.7
  facets:
    access_clarity: 84.2
    contract_governance: 45.5
    contract_quality: 69.4
    developer_ergonomics: 66.1
    discoverability: 66.1
    operational_transparency: 97.4
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 74.9
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 61.1
      total: 18
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 43.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/trello/trello-2026-06-20T195704.png
security:
- kind: authentication
  name: Trello Authentication
  slug: trello-authentication
  summary_line: apiKey/oauth2 · 3 schemes
- kind: domain-security
  name: Trello Domain Security
  slug: trello-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Trello Vulnerability Disclosure
  slug: trello-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Trello Trust Center
  slug: trello-trust-center
  summary_line: FedRAMP
skill_count: 4
skills:
- name: trello-archive-and-restore
  slug: trello-archive-and-restore
- name: trello-provision-board
  slug: trello-provision-board
- name: trello-subscribe-webhooks
  slug: trello-subscribe-webhooks
- name: trello-triage-card
  slug: trello-triage-card
slug: trello
tags:
- Project Management
- Kanban
- Task Management
- Collaboration
- Productivity
- Workflows
- Boards
- Atlassian
website: https://trello.com/
---
