---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - authentication
  - scopes
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: mostly
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 37.5
  scored_at: '2026-11-06'
api_count: 121
apis:
- description: The Lithium/Khoros Community platform API. Version 2 is driven by LiQL (Lithium Query Language), a SQL-like query language over community objects such as messages, users, boards and categories; the le
  name: Khoros Community API
  slug: community
- baseURL: https://community.khoros.com/api/2.0
  baseurl_source: declared
  description: The AccountSet API from Khoros — 1 operation(s) for accountset.
  name: Khoros Account Set API
  phrasing_intents:
  - id: accountSet
    intent: List my account sets through the v1 company API
    question: Which account sets and accounts am I a member of in an initiative?
  phrasing_ops: 1
  slug: khoros-ai-accountset-api
- baseURL: https://community.khoros.com/api/2.0
  baseurl_source: declared
  description: The Active API from Khoros — 1 operation(s) for active.
  name: Khoros Active API
  phrasing_intents:
  - id: active-1
    intent: List active work queue IDs
    question: Which work queues are active in Khoros Care?
  phrasing_ops: 1
  slug: khoros-ai-active-api
- baseURL: https://community.khoros.com/api/2.0
  baseurl_source: declared
  description: The Admin API from Khoros — 2 operation(s) for admin.
  name: Khoros Admin API
  phrasing_intents:
  - id: register-a-custom-crm
    intent: Register a custom CRM
    question: How do I connect our own CRM to Khoros?
  - id: register-a-custom-crm-1
    intent: Update a registered custom CRM
    question: Can I change the URL or credentials of a custom CRM I already registered?
  phrasing_ops: 2
  slug: khoros-ai-admin-api
- baseURL: https://community.khoros.com/api/2.0
  baseurl_source: declared
  description: The Asset API from Khoros — 1 operation(s) for asset.
  name: Khoros Asset API
  phrasing_intents:
  - id: get-an-asset
    intent: Get an asset by its path
    question: How do I fetch a stored asset when I know its path?
  phrasing_ops: 1
  slug: khoros-ai-asset-api
- baseURL: https://community.khoros.com/api/2.0
  baseurl_source: declared
  description: The Assets API from Khoros — 3 operation(s) for assets.
  name: Khoros Assets API
  phrasing_intents:
  - id: createAsset
    intent: Create a Content Center asset
    question: How do I create a Content Center asset record with a name, folder and entity type?
  - id: createMultiPartAsset
    intent: Upload a Content Center asset with a media file
    question: How do I upload an image or video file as a new asset in one request?
  - id: findAsset
    intent: Get a Content Center asset by ID
    question: How do I look up a Content Center asset and its content labels?
  - id: updateAsset
    intent: Update a Content Center asset
    question: Can I move an asset to another folder or rename it?
  phrasing_ops: 4
  slug: khoros-ai-assets-api
- baseURL: https://community.khoros.com/api/2.0
  baseurl_source: declared
  description: The Author Api V2 API from Khoros — 3 operation(s) for author api v2.
  name: Khoros Author Api V2 API
  phrasing_intents:
  - id: authorslswuuid
    intent: Get a Care author's details
    question: How do I look up a customer author's profile in Khoros Care?
  - id: authorslswuuid-1
    intent: Update or merge a Care author's handles
    question: Can I merge social handles into one existing Care author?
  - id: authors-1
    intent: Create a Care author from a CRM record
    question: How do I add a new author to Care and join it to a CRM record?
  - id: authors-2
    intent: Batch update records for one author
    question: Can I update several author records belonging to the same person in one call?
  - id: authors
    intent: List Care authors page by page
    question: How do I page through every customer author in Khoros Care?
  phrasing_ops: 5
  slug: khoros-ai-author-api-v2-api
- baseURL: https://community.khoros.com/api/2.0
  baseurl_source: declared
  description: The Authors API from Khoros — 2 operation(s) for authors.
  name: Khoros Authors API
  phrasing_intents:
  - id: author-put
    intent: Update an author's CRM and author attributes
    question: Can my bot update both the CRM attributes and the author attributes in one call?
  - id: authors-put
    intent: Update an author's metadata properties
    question: How does a bot update metadata properties on an author?
  phrasing_ops: 2
  slug: khoros-ai-authors-api
- baseURL: https://community.khoros.com/api/2.0
  baseurl_source: declared
  description: The Broadcast API from Khoros — 3 operation(s) for broadcast.
  name: Khoros Broadcast API
  phrasing_intents:
  - id: broadcast-to-msisdn
    intent: Broadcast a message to phone numbers
    question: How do I send a broadcast to specific mobile numbers?
  - id: broadcast-to-segments
    intent: Broadcast a message to audience segments
    question: How do I send a broadcast to a whole audience segment?
  - id: get-audience-segments
    intent: List audience segments
    question: Which audience segments can I broadcast to?
  phrasing_ops: 3
  slug: khoros-ai-broadcast-api
- baseURL: https://community.khoros.com/api/2.0
  baseurl_source: declared
  description: The BySourceDocumentId API from Khoros — 1 operation(s) for bysourcedocumentid.
  name: Khoros By Source Document ID API
  phrasing_intents:
  - id: get-conversation-details-by-document-source-id
    intent: Get a conversation by source document ID
    question: How do I find the conversation a specific social post belongs to?
  phrasing_ops: 1
  slug: khoros-ai-bysourcedocumentid-api
- baseURL: https://community.khoros.com/api/2.0
  baseurl_source: declared
  description: The Case API from Khoros — 2 operation(s) for case.
  name: Khoros Case API
  phrasing_intents:
  - id: createcase
    intent: Create a Care case with interactions
    question: How do I open a new case in Khoros Care from my own system?
  - id: lookupcase
    intent: Look up a Care case
    question: How do I fetch the details of one Care case by its ID?
  - id: updatecase
    intent: Update an existing Care case
    question: Can I change the title or add interactions to a case that already exists?
  phrasing_ops: 3
  slug: khoros-ai-case-api
- baseURL: https://community.khoros.com/api/2.0
  baseurl_source: declared
  description: The Changed API from Khoros — 1 operation(s) for changed.
  name: Khoros Changed API
  phrasing_intents:
  - id: authorschanged
    intent: List author records changed in a period
    question: Which Care author records changed today?
  phrasing_ops: 1
  slug: khoros-ai-changed-api
- baseURL: https://community.khoros.com/api/2.0
  baseurl_source: declared
  description: The Compare.json API from Khoros — 4 operation(s) for compare.json.
  name: Khoros Compare.json API
  phrasing_intents:
  - id: compare-stream-volumes
    intent: Compare volumes across streams
    question: How do I compare post volumes between several social streams?
  - id: get-percentage-towards-target
    intent: Get stream progress toward a target
    question: How close are my streams to a volume target?
  - id: get-specific-decimals-in-percent-return-1
    intent: Set decimals on target-progress percentages
    question: How many decimal places can a stream target percentage have?
  - id: get-specified-sort-order-1
    intent: Sort compared streams by percentage
    question: Can I order compared streams by percentage ascending or descending?
  phrasing_ops: 4
  slug: khoros-ai-compare-json-api
- baseURL: https://community.khoros.com/api/2.0
  baseurl_source: declared
  description: The Config API from Khoros — 1 operation(s) for config.
  name: Khoros Config API
  phrasing_intents:
  - id: configtimezones
    intent: List time zone IDs for exports
    question: Which time zone IDs can I use when formatting exports?
  phrasing_ops: 1
  slug: khoros-ai-config-api
- baseURL: https://community.khoros.com/api/2.0
  baseurl_source: declared
  description: The Control API from Khoros — 2 operation(s) for control.
  name: Khoros Control API
  phrasing_intents:
  - id: controlnetworknetworkkeyexternalidexternalidauthorauthorid-get
    intent: See whether a bot or agent controls a conversation
    question: Is a bot or a human agent currently in control of a customer's conversation?
  - id: control-put
    intent: Pass conversation control between bot and agent
    question: How does a bot hand a conversation over to a human agent?
  phrasing_ops: 2
  slug: khoros-ai-control-api
- baseURL: https://community.khoros.com/api/2.0
  baseurl_source: declared
  description: The Conversation Api V2 API from Khoros — 1 operation(s) for conversation api v2.
  name: Khoros Conversation Api V2 API
  phrasing_intents:
  - id: lswuuid-1
    intent: Get a Care conversation's details
    question: How do I pull the details of one Care conversation by its unique ID?
  phrasing_ops: 1
  slug: khoros-ai-conversation-api-v2-api
- baseURL: https://community.khoros.com/api/2.0
  baseurl_source: declared
  description: The Conversations API from Khoros — 29 operation(s) for conversations.
  name: Khoros Conversations API
  phrasing_intents:
  - id: authors_lswuuid_conversations
    intent: List a Care author's conversation IDs for a day
    question: Which conversations did a specific Care author have during one 24-hour window?
  - id: accountset
    intent: List account sets and accounts for an initiative
    question: Which account sets and social accounts can I post to inside a marketing initiative?
  - id: assets-create-text-asset
    intent: Create a text asset in the Content Center
    question: How do I add a reusable text snippet to the Khoros Marketing Content Center?
  - id: assets-create-image-or-video
    intent: Upload an image or video asset to the Content Center
    question: Can I upload an image or video file as a Content Center asset?
  - id: assets-retrieve-a-content-center-asset-by-id
    intent: Get a Content Center asset by ID
    question: How can I see the details and content labels of one Content Center asset?
  - id: assets-update-existing-content-center-asset
    intent: Update an existing Content Center asset
    question: Can I rename or move an existing Content Center asset to another folder?
  - id: create-a-new-content-asset-folder
    intent: Create a Content Center asset folder
    question: How do I make a new custom folder to organize marketing assets?
  - id: retrieve-a-list-of-folders
    intent: List Content Center folders
    question: What asset folders exist in our Khoros Marketing Content Center?
  phrasing_ops: 39
  slug: khoros-ai-conversations-api
- baseURL: https://community.khoros.com/api/2.0
  baseurl_source: declared
  description: The Csv API from Khoros — 1 operation(s) for csv.
  name: Khoros CSV API
  phrasing_intents:
  - id: csvreportname-deprecated
    intent: Download a report as CSV (older endpoint)
    question: How do I get a CSV export of a named report from the older CSV endpoint?
  phrasing_ops: 1
  slug: khoros-ai-csv-api
- baseURL: https://community.khoros.com/api/2.0
  baseurl_source: declared
  description: The Csv Long API from Khoros — 1 operation(s) for csv long.
  name: Khoros Csv Long API
  phrasing_intents:
  - id: csv_longreportname-deprecated
    intent: Export a report as CSV for a date range
    question: How do I download a supervisor report as a CSV for certain dates?
  phrasing_ops: 1
  slug: khoros-ai-csv-long-api
- baseURL: https://community.khoros.com/api/2.0
  baseurl_source: declared
  description: The CurrentTAR API from Khoros — 1 operation(s) for currenttar.
  name: Khoros Current TAR API
  phrasing_intents:
  - id: currenttar
    intent: Get current time to agent response
    question: How long are customers waiting for an agent response right now?
  phrasing_ops: 1
  slug: khoros-ai-currenttar-api
- baseURL: https://community.khoros.com/api/2.0
  baseurl_source: declared
  description: The Customer API from Khoros — 4 operation(s) for customer.
  name: Khoros Customer API
  phrasing_intents:
  - id: bestmatchcustomers
    intent: Find the best-matching customer from social info
    question: How do I match a social profile to an existing customer record?
  - id: createcustomer
    intent: Create a customer record
    question: How do I add a new customer record in Khoros?
  - id: findcustomer
    intent: Get a customer by ID
    question: How do I pull up a specific customer's details?
  - id: updatecustomer
    intent: Update a customer's details
    question: Can I change the custom fields on an existing customer?
  - id: findcases
    intent: List a customer's cases
    question: Which support cases are linked to a customer?
  phrasing_ops: 5
  slug: khoros-ai-customer-api
- baseURL: https://community.khoros.com/api/2.0
  baseurl_source: declared
  description: The Customer (COPY) API from Khoros — 1 operation(s) for customer (copy).
  name: Khoros Customer (COPY) API
  phrasing_intents:
  - id: updatecustomer
    intent: Update a customer's details
    question: How do I update a customer's profile fields in Khoros Care?
  phrasing_ops: 1
  slug: khoros-ai-customer-copy-api
- baseURL: https://community.khoros.com/api/2.0
  baseurl_source: declared
  description: The Customers API from Khoros — 1 operation(s) for customers.
  name: Khoros Customers API
  phrasing_intents:
  - id: searchcustomers
    intent: Search customers by custom fields
    question: How do I find every customer matching a set of criteria?
  phrasing_ops: 1
  slug: khoros-ai-customers-api
- baseURL: https://community.khoros.com/api/2.0
  baseurl_source: declared
  description: The Data API from Khoros — 1 operation(s) for data.
  name: Khoros Data API
  phrasing_intents:
  - id: retrieve-subscription-events
    intent: Poll events for a subscription
    question: How do I fetch the events that arrived for one of my subscriptions?
  phrasing_ops: 1
  slug: khoros-ai-data-api
- baseURL: https://community.khoros.com/api/2.0
  baseurl_source: declared
  description: The Discussion API from Khoros — 1 operation(s) for discussion.
  name: Khoros Discussion API
  phrasing_intents:
  - id: integrationuuidmessages
    intent: Send message batches into a case
    question: How do I push batches of messages onto a case by reference message?
  phrasing_ops: 1
  slug: khoros-ai-discussion-api
- baseURL: https://community.khoros.com/api/2.0
  baseurl_source: declared
  description: The DisplayIds API from Khoros — 1 operation(s) for displayids.
  name: Khoros Display IDs API
  phrasing_intents:
  - id: displayidsdisplaynumber-1
    intent: Get conversations by display ID
    question: How do I look up a conversation using the display number agents see?
  phrasing_ops: 1
  slug: khoros-ai-displayids-api
- baseURL: https://community.khoros.com/api/2.0
  baseurl_source: declared
  description: The Email API from Khoros — 1 operation(s) for email.
  name: Khoros Email API
  phrasing_intents:
  - id: change-agent-state-by-email
    intent: Set an agent's state by email
    question: How do I change an agent's availability state using their email?
  phrasing_ops: 1
  slug: khoros-ai-email-api
- baseURL: https://community.khoros.com/api/2.0
  baseurl_source: declared
  description: The Entities.json API from Khoros — 1 operation(s) for entities.json.
  name: Khoros Entities.json API
  phrasing_intents:
  - id: get-specific-entities
    intent: Get specific approved items from a stream
    question: How do I fetch particular approved posts from a stream by their entity IDs?
  phrasing_ops: 1
  slug: khoros-ai-entities-json-api
- baseURL: https://community.khoros.com/api/2.0
  baseurl_source: declared
  description: The Export API from Khoros — 10 operation(s) for export.
  name: Khoros Export API
  phrasing_intents:
  - id: published-post
    intent: Export published posts and their metrics
    question: How do I export the posts we published along with their engagement metrics?
  - id: daily-account-level-metrics
    intent: Export daily account-level metrics
    question: How do I get daily performance metrics for each social account?
  - id: daily-post-summary
    intent: Export a daily summary of post metrics
    question: Is there an export that rolls up post metrics by day?
  - id: ads-net-values
    intent: Export ads with net metric values
    question: How do I export our ads and their net performance values?
  - id: stream-item-data
    intent: Export stream items for a date range
    question: How do I export the items that landed in my streams over some dates?
  - id: stream-item-action-data
    intent: Export actions taken on stream items
    question: How do I export what actions were taken on stream items?
  - id: custom-feedback
    intent: Export customer feedback responses
    question: How do I export the customer feedback responses we received?
  - id: profiles
    intent: Export social network profile details
    question: How do I export information about our social network profiles?
  phrasing_ops: 10
  slug: khoros-ai-export-api
- baseURL: https://community.khoros.com/api/2.0
  baseurl_source: declared
  description: The Flow Rest Api API from Khoros — 2 operation(s) for flow rest api.
  name: Khoros Flow Rest API
  phrasing_intents:
  - id: trigger-an-event
    intent: Trigger a Flow event on a thread
    question: How do I trigger a Flow event for a specific conversation thread?
  - id: get-bot-status
    intent: Check whether a bot is paused on a thread
    question: Is my bot paused or active on this conversation thread?
  phrasing_ops: 2
  slug: khoros-ai-flow-rest-api-api
- baseURL: https://community.khoros.com/api/2.0
  baseurl_source: declared
  description: The Folder API from Khoros — 3 operation(s) for folder.
  name: Khoros Folder API
  phrasing_intents:
  - id: listFolders
    intent: List Content Center folders
    question: What folders do we have in Content Center?
  - id: createFolder
    intent: Create a Content Center asset folder
    question: How do I make a new folder to organize Content Center assets?
  - id: findFolder
    intent: Get a Content Center folder by ID
    question: How do I look up one Content Center folder's details by its ID?
  - id: updateFolder
    intent: Rename or update a Content Center folder
    question: Can I rename an existing Content Center folder?
  - id: deleteFolder
    intent: Delete a Content Center folder
    question: How do I delete an asset folder I no longer need?
  - id: listFolderAssets
    intent: List the assets inside a folder
    question: What assets are stored in a particular Content Center folder?
  phrasing_ops: 6
  slug: khoros-ai-folder-api
- baseURL: https://community.khoros.com/api/2.0
  baseurl_source: declared
  description: The Form API from Khoros — 1 operation(s) for form.
  name: Khoros Form API
  phrasing_intents:
  - id: send-a-bot-response-with-a-secure-form
    intent: Send a secure form as a bot reply
    question: How can a bot ask a customer to fill in a secure form?
  phrasing_ops: 1
  slug: khoros-ai-form-api
- baseURL: https://community.khoros.com/api/2.0
  baseurl_source: declared
  description: The GetForms API from Khoros — 1 operation(s) for getforms.
  name: Khoros Get Forms API
  phrasing_intents:
  - id: get-secure-forms
    intent: List secure forms
    question: What secure forms are available to send customers?
  phrasing_ops: 1
  slug: khoros-ai-getforms-api
- baseURL: https://community.khoros.com/api/2.0
  baseurl_source: declared
  description: The Handover API from Khoros — 1 operation(s) for handover.
  name: Khoros Handover API
  phrasing_intents:
  - id: handover-action
    intent: Hand a thread to an agent by pausing the bot
    question: How do I hand a Flow conversation over and pause the bot for a set time?
  phrasing_ops: 1
  slug: khoros-ai-handover-api
- baseURL: https://community.khoros.com/api/2.0
  baseurl_source: declared
  description: The Health API from Khoros — 1 operation(s) for health.
  name: Khoros Health API
  phrasing_intents:
  - id: healthappidappid
    intent: Check a bot's health
    question: Is my bot healthy according to the Automation Framework?
  phrasing_ops: 1
  slug: khoros-ai-health-api
- baseURL: https://community.khoros.com/api/2.0
  baseurl_source: declared
  description: The Initiatives API from Khoros — 2 operation(s) for initiatives.
  name: Khoros Initiatives API
  phrasing_intents:
  - id: listInitiatives
    intent: List initiatives through the v1 company API
    question: How do I list a company's initiatives using the v1 environment path?
  - id: getInitiative
    intent: Get an initiative through the v1 company API
    question: How do I fetch one initiative by ID using the v1 company path?
  phrasing_ops: 2
  slug: khoros-ai-initiatives-api
- baseURL: https://community.khoros.com/api/2.0
  baseurl_source: declared
  description: The Khorosapi API from Khoros — 1 operation(s) for khorosapi.
  name: Khoros Khorosapi API
  phrasing_intents:
  - id: tokenskhorosapiowneridownerid-get
    intent: Check whether an entity has a JWT
    question: Does this entity already have a JWT issued?
  - id: tokenskhorosapiowneridownerid-post
    intent: Generate a JWT for an entity
    question: How do I generate a JWT for an owner ID?
  phrasing_ops: 2
  slug: khoros-ai-khorosapi-api
- baseURL: https://community.khoros.com/api/2.0
  baseurl_source: declared
  description: The Labels API from Khoros — 1 operation(s) for labels.
  name: Khoros Labels API
  phrasing_intents:
  - id: findContentLabelsForCompany
    intent: List content labels through the v1 company API
    question: Which content labels exist in an initiative using the v1 company path?
  phrasing_ops: 1
  slug: khoros-ai-labels-api
- baseURL: https://community.khoros.com/api/2.0
  baseurl_source: declared
  description: The List API from Khoros — 2 operation(s) for list.
  name: Khoros List API
  phrasing_intents:
  - id: list-deprecated
    intent: List available supervisor report names
    question: Which supervisor reports can I run in Khoros Care?
  - id: list-a-specific-directory
    intent: List the assets in a directory
    question: How do I see what assets are in a specific directory?
  phrasing_ops: 2
  slug: khoros-ai-list-api
- baseURL: https://community.khoros.com/api/2.0
  baseurl_source: declared
  description: The Me API from Khoros — 2 operation(s) for me.
  name: Khoros Me API
  phrasing_intents:
  - id: me
    intent: List my companies with this app enabled (v1)
    question: Which of my companies have this app enabled on the v1 endpoint?
  - id: retrieve-a-list-companies-with-this-app-enabled
    intent: List companies I belong to for this app
    question: What companies is my signed-in user associated with for this app?
  phrasing_ops: 2
  slug: khoros-ai-me-api
- baseURL: https://community.khoros.com/api/2.0
  baseurl_source: declared
  description: The Messages API from Khoros — 10 operation(s) for messages.
  name: Khoros Messages API
  phrasing_intents:
  - id: integrationuuidmessagesvalidation
    intent: Validate an inbound messages payload
    question: How can I test whether my inbound message JSON is valid before sending it to Care?
  - id: integrationuuiddiscussion
    intent: Ingest inbound messages from a custom integration
    question: How do I push messages from my own channel into Khoros Care?
  - id: integrationuuidmessages-1
    intent: Delete inbound messages from an integration
    question: Can I remove messages that a custom integration previously sent into Care?
  - id: generate-a-thread-id
    intent: Generate a new Flow thread ID
    question: How do I get a thread ID to start a Flow conversation over REST?
  - id: create-a-text-message
    intent: Send a text message to a Flow thread
    question: How do I send a user's text message into a Flow bot thread?
  - id: get-a-list-of-messages
    intent: List the messages in a Flow thread
    question: How do I read back the messages in a Flow bot thread?
  - id: publishMessage
    intent: Publish a message through the company-scoped v1 API
    question: How do I publish a social message through the v1 company and environment endpoint?
  - id: getMessage
    intent: Get a message through the company-scoped v1 API
    question: How do I fetch one message using the v1 company-scoped path?
  phrasing_ops: 14
  slug: khoros-ai-messages-api
- baseURL: https://community.khoros.com/api/2.0
  baseurl_source: declared
  description: The Meta API from Khoros — 1 operation(s) for meta.
  name: Khoros Meta API
  phrasing_intents:
  - id: define-object-structures
    intent: Describe an object type's structure
    question: What fields make up a given object type?
  phrasing_ops: 1
  slug: khoros-ai-meta-api
- baseURL: https://community.khoros.com/api/2.0
  baseurl_source: declared
  description: The Meta.json API from Khoros — 18 operation(s) for meta.json.
  name: Khoros Meta.json API
  phrasing_intents:
  - id: get-entity-information
    intent: Get summary metadata for a stream
    question: What summary information can I get about the entities in a social stream?
  - id: get-minutes-of-activity
    intent: Get a stream's activity by the minute
    question: Can I see minute-by-minute activity for a stream?
  - id: get-minutes-of-activity-1
    intent: Get a stream's activity by the hour
    question: Can I get hourly activity counts for a stream?
  - id: get-days-of-activity
    intent: Get a stream's activity by the day
    question: Can I see daily activity totals for a stream over several days?
  - id: get-activity-and-count-props
    intent: Include activity and count totals in stream meta
    question: How do I make the stream meta response include activity and count properties?
  - id: get-last-item-of-activity
    intent: Set where a stream's activity data ends
    question: Can I make stream activity data stop at a specific point in time?
  - id: get-networks-in-meta-response-1
    intent: List the networks a stream covers
    question: Which social networks does a stream pull content from?
  - id: get-networks-in-meta-response
    intent: Get top retweets for specific hourly periods
    question: Can I get the top retweeted posts for particular hours in a stream?
  phrasing_ops: 18
  slug: khoros-ai-meta-json-api
- baseURL: https://community.khoros.com/api/2.0
  baseurl_source: declared
  description: The MultiChannelMessages API from Khoros — 1 operation(s) for multichannelmessages.
  name: Khoros Multi Channel Messages API
  phrasing_intents:
  - id: getMultiChannelMessage
    intent: Get a multi-channel message
    question: How do I look up a multi-channel message in an initiative?
  phrasing_ops: 1
  slug: khoros-ai-multichannelmessages-api
- baseURL: https://community.khoros.com/api/2.0
  baseurl_source: declared
  description: The Networks API from Khoros — 16 operation(s) for networks.
  name: Khoros Networks API
  phrasing_intents:
  - id: authorsnetworksnetworktypeidsnetworkid
    intent: Get an author by social network ID
    question: How do I look up a Khoros Care author from their Facebook or Instagram user ID?
  - id: authorsnetworksnetworktypeidsnetworkid-1
    intent: Update an author by social network ID
    question: Can I update an author record using their network ID on a single-instance network?
  - id: authorsnetworksnetworktypeinstancesnetworkinstanceidsnetworkid-1
    intent: Get an author by network ID on an instance
    question: How do I find an author by network ID when we have several instances of that network?
  - id: authorsnetworksnetworktypeinstancesnetworkinstanceidsnetworkid-2
    intent: Update an author by network ID on an instance
    question: Can I update an author on a specific instance of a network?
  - id: authorsnetworks_networktype_handles_networkhandle
    intent: Find authors by social handle
    question: How do I find an author by their social media handle?
  - id: authorsnetworksnetworktypeinstancesnetworkinstancehandlesnetworkhandle
    intent: Find authors by handle on a network instance
    question: Can I search for an author handle within one specific network instance?
  - id: authorsnetworksnetworktypeidsnetworkidconversations
    intent: List an author's conversation IDs by network ID
    question: Which conversations did an author have on a given day, looked up by network ID?
  - id: authorsnetworksnetworktypeinstancesnetworkinstanceidsnetworkidconversations
    intent: List an author's conversation IDs per instance
    question: How do I get one day of an author's conversation IDs on a specific network instance by user ID?
  phrasing_ops: 21
  slug: khoros-ai-networks-api
- baseURL: https://community.khoros.com/api/2.0
  baseurl_source: declared
  description: The Note API from Khoros — 1 operation(s) for note.
  name: Khoros Note API
  phrasing_intents:
  - id: note-put
    intent: Add an internal note to a bot conversation
    question: How can a bot leave an internal note on the current conversation?
  phrasing_ops: 1
  slug: khoros-ai-note-api
- baseURL: https://community.khoros.com/api/2.0
  baseurl_source: declared
  description: The Pause API from Khoros — 1 operation(s) for pause.
  name: Khoros Pause API
  phrasing_intents:
  - id: pause-a-bot
    intent: Pause the bot on a thread
    question: How do I stop a Flow bot from replying in one conversation thread?
  - id: resume-a-bot
    intent: Resume the bot on a paused thread
    question: How do I turn a paused Flow bot back on for a thread?
  phrasing_ops: 2
  slug: khoros-ai-pause-api
- baseURL: https://community.khoros.com/api/2.0
  baseurl_source: declared
  description: The Permissions API from Khoros — 1 operation(s) for permissions.
  name: Khoros Permissions API
  phrasing_intents:
  - id: getPrivileges
    intent: List my permissions in a company
    question: What permissions do I have in the current company?
  phrasing_ops: 1
  slug: khoros-ai-permissions-api
- baseURL: https://community.khoros.com/api/2.0
  baseurl_source: declared
  description: The Plans API from Khoros — 1 operation(s) for plans.
  name: Khoros Plans API
  phrasing_intents:
  - id: listPlans
    intent: List plans through the v1 company API
    question: What plans exist in an initiative using the v1 company path?
  phrasing_ops: 1
  slug: khoros-ai-plans-api
- baseURL: https://community.khoros.com/api/2.0
  baseurl_source: declared
  description: The Priority API from Khoros — 1 operation(s) for priority.
  name: Khoros Priority API
  phrasing_intents:
  - id: priority-put
    intent: Change a conversation's priority
    question: How does a bot raise or lower a conversation's priority?
  phrasing_ops: 1
  slug: khoros-ai-priority-api
- baseURL: https://community.khoros.com/api/2.0
  baseurl_source: declared
  description: The Projects API from Khoros — 1 operation(s) for projects.
  name: Khoros Projects API
  phrasing_intents:
  - id: list-all-flows
    intent: List the flows in a project
    question: Which bot flows are in my Flow project?
  phrasing_ops: 1
  slug: khoros-ai-projects-api
- baseURL: https://community.khoros.com/api/2.0
  baseurl_source: declared
  description: The Registrations API from Khoros — 4 operation(s) for registrations.
  name: Khoros Registrations API
  phrasing_intents:
  - id: botsv3registrations
    intent: List all bot registrations
    question: Which bots are registered with the Automation Framework?
  - id: registrations-post
    intent: Register a bot with Khoros Care
    question: How do I register a new bot with Khoros Care and the Automation Framework?
  - id: registrations-put
    intent: Edit a bot registration
    question: Can I change the settings of a bot that is already registered?
  - id: registrationsnetworknetworkkeyexternalidexternalid-get
    intent: List bot registrations for a source channel
    question: Which bots are registered on one network channel?
  - id: networknetworkkeyexternalidexternalidappidappid-get
    intent: Get one bot registration's details
    question: How do I see the details of a single bot registration by its app ID?
  - id: registrations-delete
    intent: Delete a bot registration
    question: How do I unregister a bot from the Automation Framework?
  - id: registrationsnetworknetworkkeyexternalidexternalidappidappidmodemode-put
    intent: Switch a bot between live and maintenance mode
    question: Can I put a bot into maintenance mode while I update it?
  phrasing_ops: 7
  slug: khoros-ai-registrations-api
- baseURL: https://community.khoros.com/api/2.0
  baseurl_source: declared
  description: The Report API from Khoros — 1 operation(s) for report.
  name: Khoros Report API
  phrasing_intents:
  - id: reportsreportworkflowidrunidstatus
    intent: Check an export job's status
    question: How do I know if a Care export job has finished running?
  phrasing_ops: 1
  slug: khoros-ai-report-api
- baseURL: https://community.khoros.com/api/2.0
  baseurl_source: declared
  description: The Reports API from Khoros — 16 operation(s) for reports.
  name: Khoros Reports API
  phrasing_intents:
  - id: jobs
    intent: Check the status of a legacy report job
    question: How do I check whether my older Care report job has finished?
  - id: reportsreportconversation_actions
    intent: Generate a conversation actions report via GET
    question: How do I pull a conversation actions report with query parameters only?
  - id: reportsreportconversation_actions-1
    intent: Generate a conversation actions export via POST
    question: Can I send conversation actions export settings in a JSON body instead of the URL?
  - id: reportsreportuser-get
    intent: Generate a user export via GET
    question: How do I export agent user data with a simple GET request?
  - id: reportsreportuser-post
    intent: Generate a user export via POST
    question: Can I request a user export with the settings in a request body?
  - id: reportworkflowidruniddownload
    intent: Download a finished Care export
    question: How do I download an export once its run has completed?
  - id: reportsreportauthor
    intent: Generate a raw author export
    question: How do I export raw data about the authors who contacted us?
  - id: reportsreportcombined
    intent: Generate a raw combined export
    question: Is there a single export that combines raw conversation data sets?
  phrasing_ops: 18
  slug: khoros-ai-reports-api
- baseURL: https://community.khoros.com/api/2.0
  baseurl_source: declared
  description: The Request API from Khoros — 2 operation(s) for request.
  name: Khoros Request API
  phrasing_intents:
  - id: requestrequestid
    intent: Monitor a single bot request
    question: How do I check what happened to one request my bot sent?
  - id: requestappidappid
    intent: Monitor bot requests by date, state and origin
    question: How do I see all the requests my bot app made since a date?
  phrasing_ops: 2
  slug: khoros-ai-request-api
- baseURL: https://community.khoros.com/api/2.0
  baseurl_source: declared
  description: The Requests API from Khoros — 2 operation(s) for requests.
  name: Khoros Requests API
  phrasing_intents:
  - id: requests
    intent: Submit a GDPR erasure request for an author
    question: How do I handle a GDPR deletion request for a customer in Khoros Care?
  - id: requestsrequestuuid
    intent: Check a GDPR request's status
    question: How do I find out whether a GDPR request has finished?
  phrasing_ops: 2
  slug: khoros-ai-requests-api
- baseURL: https://community.khoros.com/api/2.0
  baseurl_source: declared
  description: The Resolve API from Khoros — 2 operation(s) for resolve.
  name: Khoros Resolve API
  phrasing_intents:
  - id: resolve-put
    intent: Have a bot resolve a conversation
    question: How does a Bot v3 bot mark a conversation resolved?
  - id: resolve-action
    intent: Send a resolve action for a Flow thread
    question: How do I resolve a Flow thread by its thread ID?
  phrasing_ops: 2
  slug: khoros-ai-resolve-api
- baseURL: https://community.khoros.com/api/2.0
  baseurl_source: declared
  description: The Respond API from Khoros — 1 operation(s) for respond.
  name: Khoros Respond API
  phrasing_intents:
  - id: respond-post
    intent: Send a bot reply to an incoming message
    question: How does a bot reply to a customer's incoming message on a channel?
  phrasing_ops: 1
  slug: khoros-ai-respond-api
- baseURL: https://community.khoros.com/api/2.0
  baseurl_source: declared
  description: The SsoId API from Khoros — 1 operation(s) for ssoid.
  name: Khoros SSO ID API
  phrasing_intents:
  - id: change-agent-state-by-sso-id
    intent: Set an agent's state by SSO ID
    question: How do I change an agent's state using their SSO ID?
  phrasing_ops: 1
  slug: khoros-ai-ssoid-api
- baseURL: https://community.khoros.com/api/2.0
  baseurl_source: declared
  description: The Stream Api API from Khoros — 25 operation(s) for stream api.
  name: Khoros Stream API
  phrasing_intents:
  - id: retrieve-streams-approved-content
    intent: Retrieve a stream's approved content
    question: What content has been approved in one of my Khoros streams?
  - id: specify-amount-of-content-to-pull
    intent: Pull a set number of approved stream items
    question: Can I cap how many approved items a stream returns in one call?
  - id: gather-content-after-specific-entity
    intent: Get newest stream items after a given entity
    question: How do I poll a stream for only the newest items approved after one I already have, favoring real-time?
  - id: gather-content-after-included-entity
    intent: Page through stream items after an entity, no gaps
    question: Can I fetch everything approved after a specific entity without skipping any items?
  - id: gather-content-after-included-entity-1
    intent: Get stream items approved before an entity
    question: How do I page backwards through older approved items in a stream?
  - id: enable-jsonp-support
    intent: Get stream content wrapped as JSONP
    question: Can a stream response be wrapped in a JavaScript callback for JSONP?
  - id: enable-geohinting-data
    intent: Get stream items with geohint data
    question: Can stream items include geohinting location data?
  - id: enable-product-hinting-for-each-entity
    intent: Get stream items with product page links
    question: Can each stream entity come back with product hinting links attached?
  phrasing_ops: 25
  slug: khoros-ai-stream-api-api
- baseURL: https://community.khoros.com/api/2.0
  baseurl_source: declared
  description: The Streams API from Khoros — 1 operation(s) for streams.
  name: Khoros Streams API
  phrasing_intents:
  - id: list-all-available-streams-for-a-company
    intent: List a company's analytics streams
    question: Which analytics streams are available for our company?
  phrasing_ops: 1
  slug: khoros-ai-streams-api
- baseURL: https://community.khoros.com/api/2.0
  baseurl_source: declared
  description: The Subscription API from Khoros — 3 operation(s) for subscription.
  name: Khoros Subscription API
  phrasing_intents:
  - id: list-subscriptions
    intent: List event subscriptions
    question: Which event subscriptions are registered for my company?
  - id: create-a-subscription
    intent: Subscribe to an event
    question: How do I get notified when a specific marketing event happens?
  - id: retrieve-subscription-details
    intent: Get an event subscription
    question: How do I check the settings and status of one subscription?
  - id: delete-a-subscription
    intent: Delete an event subscription
    question: How do I stop and remove an event subscription for good?
  - id: update-a-subscription
    intent: Pause, disable or reactivate a subscription
    question: Can I pause an event subscription instead of deleting it?
  phrasing_ops: 5
  slug: khoros-ai-subscription-api
- baseURL: https://community.khoros.com/api/2.0
  baseurl_source: declared
  description: The Surveys API from Khoros — 1 operation(s) for surveys.
  name: Khoros Surveys API
  phrasing_intents:
  - id: surveys-list-all-survey-data-for-a-set-of-streams
    intent: List survey data for streams
    question: What survey data is available for a set of streams?
  phrasing_ops: 1
  slug: khoros-ai-surveys-api
- baseURL: https://community.khoros.com/api/2.0
  baseurl_source: declared
  description: The Tag API from Khoros — 2 operation(s) for tag.
  name: Khoros Tag API
  phrasing_intents:
  - id: tag-put
    intent: Tag a message with a Care tag
    question: How can a bot tag a customer message with an existing Care tag?
  - id: untag-message-by-care-tag-id
    intent: Remove a Care tag from a message
    question: How does a bot take a Care tag off a message?
  phrasing_ops: 2
  slug: khoros-ai-tag-api
- baseURL: https://community.khoros.com/api/2.0
  baseurl_source: declared
  description: The Teams API from Khoros — 1 operation(s) for teams.
  name: Khoros Teams API
  phrasing_intents:
  - id: teams
    intent: List team IDs for analytics
    question: How do I get the team IDs for Care analytics reports?
  phrasing_ops: 1
  slug: khoros-ai-teams-api
- baseURL: https://community.khoros.com/api/2.0
  baseurl_source: declared
  description: The Threads API from Khoros — 1 operation(s) for threads.
  name: Khoros Threads API
  phrasing_intents:
  - id: get-a-list-of-threads
    intent: List Flow conversation threads
    question: How do I list the conversation threads in my Flow project?
  phrasing_ops: 1
  slug: khoros-ai-threads-api
- baseURL: https://community.khoros.com/api/2.0
  baseurl_source: declared
  description: The Tokens API from Khoros — 1 operation(s) for tokens.
  name: Khoros Tokens API
  phrasing_intents:
  - id: tokensappid-put
    intent: Refresh a bot's JWT
    question: How do I refresh the JWT my bot uses?
  - id: tokensappid-delete
    intent: Invalidate a bot's JWT
    question: How do I revoke the JWT for a bot app?
  phrasing_ops: 2
  slug: khoros-ai-tokens-api
- baseURL: https://community.khoros.com/api/2.0
  baseurl_source: declared
  description: The Trigger API from Khoros — 1 operation(s) for trigger.
  name: Khoros Trigger API
  phrasing_intents:
  - id: get-a-list-of-events
    intent: List trigger events
    question: Which trigger events are available in my Flow project?
  phrasing_ops: 1
  slug: khoros-ai-trigger-api
- baseURL: https://community.khoros.com/api/2.0
  baseurl_source: declared
  description: The Users API from Khoros — 1 operation(s) for users.
  name: Khoros Users API
  phrasing_intents:
  - id: publishers
    intent: List Conversations publishers in an initiative
    question: Which users can publish in a given initiative?
  phrasing_ops: 1
  slug: khoros-ai-users-api
- baseURL: https://community.khoros.com/api/2.0
  baseurl_source: declared
  description: The Uuid API from Khoros — 1 operation(s) for uuid.
  name: Khoros Uuid API
  phrasing_intents:
  - id: change-agent-state-by-uuid
    intent: Set an agent's availability state
    question: How do I switch an agent to a different state like away or available?
  phrasing_ops: 1
  slug: khoros-ai-uuid-api
- baseURL: https://community.khoros.com/api/2.0
  baseurl_source: declared
  description: The Business Hours API from Khoros — 1 operation(s) for business hours.
  name: Khoros Business Hours API
  phrasing_intents:
  - id: business-hours
    intent: List configured business hours
    question: What business hours are configured for my Flow project?
  phrasing_ops: 1
  slug: khoros-ai-business-hours-api
- baseURL: https://community.khoros.com/api/2.0
  baseurl_source: declared
  description: The Work Queue API from Khoros — 1 operation(s) for work queue.
  name: Khoros Work Queue API
  phrasing_intents:
  - id: workqueue-put
    intent: Move a conversation to a work queue
    question: How does a bot route a conversation to a specific work queue?
  phrasing_ops: 1
  slug: khoros-ai-work-queue-api
- baseURL: https://community.khoros.com/api/2.0
  baseurl_source: declared
  description: The Work Queues API from Khoros — 1 operation(s) for work queues.
  name: Khoros Work Queues API
  phrasing_intents:
  - id: workqueues
    intent: Get work queue details
    question: What work queues exist in Khoros Care and how are they set up?
  phrasing_ops: 1
  slug: khoros-ai-work-queues-api
artifact_total: 187
asyncapis:
- description: ''
  name: Lithium Webhooks
  slug: lithium-webhooks
collections:
- collection_type: open
  name: agent-states-api-v2 AccountSet API
  slug: open-lithium-accountset-api
- collection_type: open
  name: agent-states-api-v2 AccountSet Active API
  slug: open-lithium-active-api
- collection_type: open
  name: agent-states-api-v2 AccountSet Admin API
  slug: open-lithium-admin-api
- collection_type: open
  name: agent-states-api-v2 AccountSet Agent States Api V2 API
  slug: open-lithium-agent-states-api-v2-api
- collection_type: open
  name: agent-states-api-v2 AccountSet Asset API
  slug: open-lithium-asset-api
- collection_type: open
  name: agent-states-api-v2 AccountSet Assets API
  slug: open-lithium-assets-api
- collection_type: open
  name: agent-states-api-v2 AccountSet Author Api V2 API
  slug: open-lithium-author-api-v2-api
- collection_type: open
  name: agent-states-api-v2 AccountSet Authors API
  slug: open-lithium-authors-api
- collection_type: open
  name: agent-states-api-v2 AccountSet Broadcast API
  slug: open-lithium-broadcast-api
- collection_type: open
  name: agent-states-api-v2 AccountSet Businesshours API
  slug: open-lithium-businesshours-api
- collection_type: open
  name: agent-states-api-v2 AccountSet BySourceDocumentId API
  slug: open-lithium-bysourcedocumentid-api
- collection_type: open
  name: agent-states-api-v2 AccountSet Case API
  slug: open-lithium-case-api
- collection_type: open
  name: agent-states-api-v2 AccountSet Changed API
  slug: open-lithium-changed-api
- collection_type: open
  name: agent-states-api-v2 AccountSet Compare.json?streams API
  slug: open-lithium-compare-json-streams-api
- collection_type: open
  name: agent-states-api-v2 AccountSet Compare.json?streams={content}&sort API
  slug: open-lithium-compare-json-streams-content-sort-api
- collection_type: open
  name: agent-states-api-v2 AccountSet Compare.json?streams={content}&target API
  slug: open-lithium-compare-json-streams-content-target-api
- collection_type: open
  name: agent-states-api-v2 AccountSet Compare.json?streams={content}&target={number}&precision API
  slug: open-lithium-compare-json-streams-content-target-number-precision-api
- collection_type: open
  name: agent-states-api-v2 AccountSet Config API
  slug: open-lithium-config-api
- collection_type: open
  name: agent-states-api-v2 AccountSet Control API
  slug: open-lithium-control-api
- collection_type: open
  name: agent-states-api-v2 AccountSet Conversation Api V2 API
  slug: open-lithium-conversation-api-v2-api
- collection_type: open
  name: agent-states-api-v2 AccountSet Conversation Tag Rules V2 API
  slug: open-lithium-conversation-tag-rules-v2-api
- collection_type: open
  name: agent-states-api-v2 AccountSet Conversations API
  slug: open-lithium-conversations-api
- collection_type: open
  name: agent-states-api-v2 AccountSet Csv API
  slug: open-lithium-csv-api
- collection_type: open
  name: agent-states-api-v2 AccountSet Csv Long API
  slug: open-lithium-csv-long-api
- collection_type: open
  name: agent-states-api-v2 AccountSet CurrentTAR API
  slug: open-lithium-currenttar-api
- collection_type: open
  name: agent-states-api-v2 AccountSet Customer API
  slug: open-lithium-customer-api
- collection_type: open
  name: agent-states-api-v2 AccountSet Customer (COPY) API
  slug: open-lithium-customer-copy-api
- collection_type: open
  name: agent-states-api-v2 AccountSet Customers API
  slug: open-lithium-customers-api
- collection_type: open
  name: agent-states-api-v2 AccountSet Data API
  slug: open-lithium-data-api
- collection_type: open
  name: 'agent-states-api-v2 AccountSet # API'
  slug: open-lithium-default-api
- collection_type: open
  name: agent-states-api-v2 AccountSet Discussion API
  slug: open-lithium-discussion-api
- collection_type: open
  name: agent-states-api-v2 AccountSet DisplayIds API
  slug: open-lithium-displayids-api
- collection_type: open
  name: agent-states-api-v2 AccountSet Email API
  slug: open-lithium-email-api
- collection_type: open
  name: agent-states-api-v2 AccountSet Entities.json?entity Ids API
  slug: open-lithium-entities-json-entity-ids-api
- collection_type: open
  name: agent-states-api-v2 AccountSet Export API
  slug: open-lithium-export-api
- collection_type: open
  name: agent-states-api-v2 AccountSet Flow Rest Api API
  slug: open-lithium-flow-rest-api-api
- collection_type: open
  name: agent-states-api-v2 AccountSet Folder API
  slug: open-lithium-folder-api
- collection_type: open
  name: agent-states-api-v2 AccountSet Form API
  slug: open-lithium-form-api
- collection_type: open
  name: agent-states-api-v2 AccountSet GetForms API
  slug: open-lithium-getforms-api
- collection_type: open
  name: agent-states-api-v2 AccountSet Handover API
  slug: open-lithium-handover-api
- collection_type: open
  name: agent-states-api-v2 AccountSet Health API
  slug: open-lithium-health-api
- collection_type: open
  name: agent-states-api-v2 AccountSet Initiatives API
  slug: open-lithium-initiatives-api
- collection_type: open
  name: agent-states-api-v2 AccountSet Introspection Api API
  slug: open-lithium-introspection-api-api
- collection_type: open
  name: agent-states-api-v2 AccountSet Khorosapi API
  slug: open-lithium-khorosapi-api
- collection_type: open
  name: agent-states-api-v2 AccountSet Labels API
  slug: open-lithium-labels-api
- collection_type: open
  name: agent-states-api-v2 AccountSet Labelsets Api API
  slug: open-lithium-labelsets-api-api
- collection_type: open
  name: agent-states-api-v2 AccountSet List API
  slug: open-lithium-list-api
- collection_type: open
  name: agent-states-api-v2 AccountSet Me API
  slug: open-lithium-me-api
- collection_type: open
  name: agent-states-api-v2 AccountSet Messages API
  slug: open-lithium-messages-api
- collection_type: open
  name: agent-states-api-v2 AccountSet Meta API
  slug: open-lithium-meta-api
- collection_type: open
  name: agent-states-api-v2 AccountSet Meta.json?activity API
  slug: open-lithium-meta-json-activity-api
- collection_type: open
  name: agent-states-api-v2 AccountSet Meta.json?all Topics API
  slug: open-lithium-meta-json-all-topics-api
- collection_type: open
  name: agent-states-api-v2 AccountSet Meta.json API
  slug: open-lithium-meta-json-api
- collection_type: open
  name: agent-states-api-v2 AccountSet Meta.json?disregard API
  slug: open-lithium-meta-json-disregard-api
- collection_type: open
  name: agent-states-api-v2 AccountSet Meta.json?finish API
  slug: open-lithium-meta-json-finish-api
- collection_type: open
  name: agent-states-api-v2 AccountSet Meta.json? Networks API
  slug: open-lithium-meta-json-networks-api
- collection_type: open
  name: agent-states-api-v2 AccountSet Meta.json?num Contributors API
  slug: open-lithium-meta-json-num-contributors-api
- collection_type: open
  name: agent-states-api-v2 AccountSet Meta.json?num Days API
  slug: open-lithium-meta-json-num-days-api
- collection_type: open
  name: agent-states-api-v2 AccountSet Meta.json?num Hashtags API
  slug: open-lithium-meta-json-num-hashtags-api
- collection_type: open
  name: agent-states-api-v2 AccountSet Meta.json?num Hours API
  slug: open-lithium-meta-json-num-hours-api
- collection_type: open
  name: agent-states-api-v2 AccountSet Meta.json?num Minutes API
  slug: open-lithium-meta-json-num-minutes-api
- collection_type: open
  name: agent-states-api-v2 AccountSet Meta.json?num Trends API
  slug: open-lithium-meta-json-num-trends-api
- collection_type: open
  name: agent-states-api-v2 AccountSet Meta.json?percent API
  slug: open-lithium-meta-json-percent-api
- collection_type: open
  name: agent-states-api-v2 AccountSet Meta.json?precision API
  slug: open-lithium-meta-json-precision-api
- collection_type: open
  name: agent-states-api-v2 AccountSet Meta.json?sort API
  slug: open-lithium-meta-json-sort-api
- collection_type: open
  name: agent-states-api-v2 AccountSet Meta.json?top Count API
  slug: open-lithium-meta-json-top-count-api
- collection_type: open
  name: agent-states-api-v2 AccountSet Meta.json?top Periods API
  slug: open-lithium-meta-json-top-periods-api
- collection_type: open
  name: agent-states-api-v2 AccountSet Meta.json?top Periods Relative API
  slug: open-lithium-meta-json-top-periods-relative-api
- collection_type: open
  name: agent-states-api-v2 AccountSet MultiChannelMessages API
  slug: open-lithium-multichannelmessages-api
- collection_type: open
  name: agent-states-api-v2 AccountSet Networks API
  slug: open-lithium-networks-api
- collection_type: open
  name: agent-states-api-v2 AccountSet Note API
  slug: open-lithium-note-api
- collection_type: open
  name: agent-states-api-v2 AccountSet Pause API
  slug: open-lithium-pause-api
- collection_type: open
  name: agent-states-api-v2 AccountSet Permissions API
  slug: open-lithium-permissions-api
- collection_type: open
  name: agent-states-api-v2 AccountSet Plans API
  slug: open-lithium-plans-api
- collection_type: open
  name: agent-states-api-v2 AccountSet Priority API
  slug: open-lithium-priority-api
- collection_type: open
  name: agent-states-api-v2 AccountSet Projects API
  slug: open-lithium-projects-api
- collection_type: open
  name: agent-states-api-v2 AccountSet Registrations API
  slug: open-lithium-registrations-api
- collection_type: open
  name: agent-states-api-v2 AccountSet Report API
  slug: open-lithium-report-api
- collection_type: open
  name: agent-states-api-v2 AccountSet Reports API
  slug: open-lithium-reports-api
- collection_type: open
  name: agent-states-api-v2 AccountSet Request API
  slug: open-lithium-request-api
- collection_type: open
  name: agent-states-api-v2 AccountSet Requests API
  slug: open-lithium-requests-api
- collection_type: open
  name: agent-states-api-v2 AccountSet Resolve API
  slug: open-lithium-resolve-api
- collection_type: open
  name: agent-states-api-v2 AccountSet Respond API
  slug: open-lithium-respond-api
- collection_type: open
  name: agent-states-api-v2 AccountSet Smart Views Api V2 API
  slug: open-lithium-smart-views-api-v2-api
- collection_type: open
  name: agent-states-api-v2 AccountSet SsoId API
  slug: open-lithium-ssoid-api
- collection_type: open
  name: agent-states-api-v2 AccountSet Stream Api API
  slug: open-lithium-stream-api-api
- collection_type: open
  name: agent-states-api-v2 AccountSet Streams API
  slug: open-lithium-streams-api
- collection_type: open
  name: agent-states-api-v2 AccountSet Subscription API
  slug: open-lithium-subscription-api
- collection_type: open
  name: agent-states-api-v2 AccountSet Surveys API
  slug: open-lithium-surveys-api
- collection_type: open
  name: agent-states-api-v2 AccountSet Tag Api V2 API
  slug: open-lithium-tag-api-v2-api
- collection_type: open
  name: agent-states-api-v2 AccountSet Tag API
  slug: open-lithium-tag-api
- collection_type: open
  name: agent-states-api-v2 AccountSet Teams API
  slug: open-lithium-teams-api
- collection_type: open
  name: agent-states-api-v2 AccountSet Threads API
  slug: open-lithium-threads-api
- collection_type: open
  name: agent-states-api-v2 AccountSet Tokens API
  slug: open-lithium-tokens-api
- collection_type: open
  name: agent-states-api-v2 AccountSet Trigger API
  slug: open-lithium-trigger-api
- collection_type: open
  name: agent-states-api-v2 AccountSet Users API
  slug: open-lithium-users-api
- collection_type: open
  name: agent-states-api-v2 AccountSet Uuid API
  slug: open-lithium-uuid-api
- collection_type: open
  name: agent-states-api-v2 AccountSet Workqueue API
  slug: open-lithium-workqueue-api
- collection_type: open
  name: agent-states-api-v2 AccountSet Workqueues API
  slug: open-lithium-workqueues-api
common:
- group: other
  href: https://artifacts.apis.io/khoros-ai/capabilities/khoros-ai-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/khoros-ai-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/khoros-ai/vendor-facets/khoros-ai-vendor-facets.yml
  title: ''
  type: VendorFacets
  url: vendor-facets/khoros-ai-vendor-facets.yml
- group: operate
  title: ''
  type: Community
  url: https://community.khoros.com/
- group: company
  title: ''
  type: BlogRSS
  url: https://khoros.ai/feed/
- group: other
  href: https://artifacts.apis.io/khoros-ai/capabilities/lithium-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/lithium-capability-edges.yml
- group: auth
  href: https://artifacts.apis.io/khoros-ai/security/lithium-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/lithium-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/khoros-ai/scopes/lithium-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/lithium-scopes.yml
- group: auth
  href: https://artifacts.apis.io/khoros-ai/authentication/lithium-authentication.yml
  title: ''
  type: Authentication
  url: authentication/lithium-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://khoros.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://khoros.ai/developer/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.khoros.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.khoros.com/khoroscaredevdocs/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.khoros.com/khoroscaredevdocs/docs/khoros-care-integration-overview
- group: operate
  title: ''
  type: Support
  url: https://community.khoros.com/t5/Developer-Discussion/bd-p/studio
- group: company
  title: ''
  type: Blog
  url: https://community.khoros.com/t5/Developer-Blog/bg-p/developer-blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/lithiumtech
- group: commercial
  title: ''
  type: Pricing
  url: https://khoros.ai/lets-connect/
- group: start
  title: ''
  type: SignUp
  url: https://khoros.ai/lets-connect/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://khoros.ai/website-terms-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://khoros.ai/privacy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.khoros.com/
- group: auth
  title: ''
  type: TrustCenter
  url: https://khoros.ai/trust-center/
- group: auth
  title: ''
  type: Compliance
  url: https://khoros.ai/khoros-security/
- group: auth
  title: ''
  type: Security
  url: https://khoros.ai/khoros-security/
- group: operate
  title: ''
  type: SLA
  url: https://khoros.ai/customer-agreements/
- group: learn
  title: ''
  type: Training
  url: https://khoros.ai/training/
- group: agent
  href: https://artifacts.apis.io/khoros-ai/llms/lithium-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/lithium-llms.txt
- group: build
  href: https://artifacts.apis.io/khoros-ai/packages/lithium-packages.yml
  title: ''
  type: Packages
  url: packages/lithium-packages.yml
- group: build
  href: https://artifacts.apis.io/khoros-ai/packages/lithium-packages.yml
  title: ''
  type: SDKs
  url: packages/lithium-packages.yml
- group: build
  href: https://artifacts.apis.io/khoros-ai/cli/lithium-cli.yml
  title: ''
  type: CLI
  url: cli/lithium-cli.yml
- group: design
  href: https://artifacts.apis.io/khoros-ai/components/lithium-components.yml
  title: ''
  type: Components
  url: components/lithium-components.yml
- group: design
  href: https://artifacts.apis.io/khoros-ai/conventions/lithium-conventions.yml
  title: ''
  type: Conventions
  url: conventions/lithium-conventions.yml
- group: operate
  href: https://artifacts.apis.io/khoros-ai/changelog/lithium-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/lithium-changelog.yml
- group: design
  href: https://artifacts.apis.io/khoros-ai/lifecycle/lithium-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/lithium-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/khoros-ai/conformance/lithium-conformance.yml
  title: ''
  type: Conformance
  url: conformance/lithium-conformance.yml
- group: design
  href: https://artifacts.apis.io/khoros-ai/errors/lithium-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/lithium-problem-types.yml
- group: design
  href: https://artifacts.apis.io/khoros-ai/data-model/lithium-data-model.yml
  title: ''
  type: DataModel
  url: data-model/lithium-data-model.yml
- group: agent
  href: https://artifacts.apis.io/khoros-ai/well-known/lithium-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/lithium-well-known.yml
- group: design
  href: https://artifacts.apis.io/khoros-ai/asyncapi/lithium-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/lithium-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/khoros-ai/mcp/lithium-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/lithium-mcp.yml
- group: agent
  href: https://artifacts.apis.io/khoros-ai/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  href: https://artifacts.apis.io/khoros-ai/overlays/_index.yml
  title: ''
  type: Overlay
  url: overlays/_index.yml
- group: operate
  href: https://artifacts.apis.io/khoros-ai/rate-limits/lithium-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/lithium-rate-limits.yml
- group: auth
  href: https://artifacts.apis.io/khoros-ai/security/lithium-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/lithium-vulnerability-disclosure.yml
- group: commercial
  href: https://artifacts.apis.io/khoros-ai/plans/lithium-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/lithium-plans-pricing.yml
- group: other
  title: ''
  type: APICatalog
  url: https://developer.khoros.com/.well-known/api-catalog
- group: agent
  href: https://artifacts.apis.io/khoros-ai/skills/lithium-register-and-run-a-care-bot.md
  title: ''
  type: AgentSkill
  url: skills/lithium-register-and-run-a-care-bot.md
- group: agent
  href: https://artifacts.apis.io/khoros-ai/skills/lithium-look-up-a-care-author.md
  title: ''
  type: AgentSkill
  url: skills/lithium-look-up-a-care-author.md
- group: agent
  href: https://artifacts.apis.io/khoros-ai/skills/lithium-subscribe-to-marketing-events.md
  title: ''
  type: AgentSkill
  url: skills/lithium-subscribe-to-marketing-events.md
- group: agent
  href: https://artifacts.apis.io/khoros-ai/skills/lithium-handle-a-flow-conversation.md
  title: ''
  type: AgentSkill
  url: skills/lithium-handle-a-flow-conversation.md
- group: agent
  href: https://artifacts.apis.io/khoros-ai/skills/lithium-process-a-gdpr-request.md
  title: ''
  type: AgentSkill
  url: skills/lithium-process-a-gdpr-request.md
created: '2026-07-17'
description: 'Khoros is the enterprise online-community and social-customer-engagement platform formed when Lithium Technologies merged with Spredfast in 2018; the combined company rebranded as Khoros in 2019 and is today operated by IgniteTech. This record was listed as Lithium until 2026-09-24, and it also carries the Spredfast product line (Khoros Marketing). The Lithium name is still load-bearing in the live platform: the Khoros Care APIs are served from *.response.lithium.com and api.app.lithium.com, the Community plugin SDK and CLI ship on npm as lithium-sdk (the `li` command), and the public GitHub organization is still github.com/lithiumtech. The platform exposes four public developer surfaces documented at developer.khoros.com — Khoros Care (agent, author, conversation, bot, work-queue, analytics and GDPR APIs on the Lithium hosts), Khoros Marketing (the Spredfast-lineage Conversations, CRM, Stream, label-set and notification APIs on api.spredfast.com), Khoros Flow (the flow.ai
  bot and messaging REST API), and Khoros Community (the LiQL-powered Community v2 API plus the legacy v1 REST API), with the newer Aurora community platform adding a GraphQL API behind a login.'
finops:
- has_sources: true
  method: derived
  name: Khoros Ai Finops
  primary_unit: ''
  service_category: ''
  slug: khoros-ai-finops
  template: true
image: https://avatars.githubusercontent.com/u/4430799?v=4
layout: provider
modified: '2026-09-16'
name: Khoros
nav: Providers
network: true
overview: 'Khoros publishes 73 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account Set API, Active API, Admin API, and 70 more. Tagged areas include Lithium, Company, MarTech, Community, and Social Media.


  The Khoros catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Khoros'' developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 44 more developer resources.'
plans:
- name: Lithium Plans Pricing
  plan_count: 0
  slug: lithium-plans-pricing
random_paper: 21
rate_limits:
- limit_count: 3
  name: Lithium Rate Limits
  slug: lithium-rate-limits
rules:
- authorship: generated
  effective_rule_count: 98
  extends:
  - spectral:oas
  name: Khoros API Rules
  rule_count: 57
  severity_counts:
    error: 37
    hint: 0
    info: 9
    warn: 11
  slug: khoros-ai-rules
scopes:
- name: Lithium Scopes
  scope_count: 1
  slug: lithium-scopes
  summary_line: 1 scope · clientCredentials/authorizationCode
score:
  band: exemplar
  composite: 67.9
  coverage:
    artifact_dirs: 32
    catalog_earned: 56.5
    catalog_earned_first_party: 12.0
    catalog_gap: 58.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.1
  facets:
    access_clarity: 60.5
    contract_governance: 31.8
    contract_quality: 60.3
    developer_ergonomics: 54.2
    discoverability: 89.3
    operational_transparency: 84.2
  previous_composite: 72.0
  provenance:
    conformance: first-party
    contracts:
      callable: 87.0
      derived: 0
      marker_coverage: 0.0
      total: 72
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 45.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 27.8
screenshot: https://apis.io/screenshots/khoros-ai/lithium-2026-07-25T225335.png
security:
- kind: authentication
  name: Lithium Authentication
  slug: lithium-authentication
  summary_line: http/oauth2 · 3 schemes
- kind: domain-security
  name: Lithium Domain Security
  slug: lithium-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Lithium Vulnerability Disclosure
  slug: lithium-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Lithium Trust Center
  slug: lithium-trust-center
  summary_line: ISO 27001, SOC 2 Type II, FedRAMP, FISMA
skill_count: 5
skills:
- name: Handle a Khoros Flow conversation
  slug: lithium-handle-a-flow-conversation
- name: Look up a Khoros Care author and their conversations
  slug: lithium-look-up-a-care-author
- name: Process a GDPR data-subject request in Khoros Care
  slug: lithium-process-a-gdpr-request
- name: Register and run a Khoros Care bot
  slug: lithium-register-and-run-a-care-bot
- name: Subscribe to Khoros Marketing events
  slug: lithium-subscribe-to-marketing-events
slug: khoros-ai
tags:
- Lithium
- Company
- MarTech
- Community
- Social Media
- Customer Engagement
- Customer Service
- Chatbots
- Messaging
- Analytics
- Marketing
website: https://khoros.ai/
---
