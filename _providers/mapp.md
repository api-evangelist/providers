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
  - scopes
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: platform
    openapi_examples: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 49.8
  scored_at: '2026-10-03'
api_count: 4
apis:
- baseURL: https://{engage-host}/api/rest/v19
  baseurl_source: declared
  description: The Address Attributes API from Mapp Marketing Cloud — 1 operation(s) for address attributes.
  name: Mapp Marketing Cloud Address Attributes API
  phrasing_intents:
  - id: list
    intent: List address attributes
    question: Which address attributes are available for contacts?
  phrasing_ops: 1
  slug: mapp-address-attributes-api
- baseURL: https://{engage-host}/api/rest/v19
  baseurl_source: declared
  description: Submit analysis and get data
  name: Mapp Marketing Cloud Analysis API
  phrasing_intents:
  - id: deleteAnalysisQueryByCorrelationId
    intent: Cancel a running analysis query
    question: Can I abort a single analysis query that is still running?
  - id: getAnalysisQueryByCorrelationId
    intent: Check a single analysis query's status
    question: Has my single analysis query finished calculating so I can fetch the result?
  - id: deleteReportAnalysis
    intent: Cancel a report calculation
    question: Can I stop a report calculation that's taking too long?
  - id: status
    intent: Check a report calculation's status
    question: Is my analytics report calculation finished yet?
  - id: postAnalysisQuery
    intent: Submit a single analysis calculation query
    question: How do I run one analysis query against my Mapp Intelligence data?
  - id: createReportQuery
    intent: Start a report calculation
    question: How do I request an analytics report for a date range?
  - id: getAnalysisResultByCalculationId
    intent: Retrieve calculated analysis data
    question: Where do I download the data once an analysis calculation succeeds?
  - id: getAnalysisUsageCurrent
    intent: Count this month's analysis usage
    question: How many analyses have we run so far this month?
  phrasing_ops: 8
  slug: mapp-analysis-api
- baseURL: https://{engage-host}/api/rest/v19
  baseurl_source: declared
  description: The Async API from Mapp Marketing Cloud — 8 operation(s) for async.
  name: Mapp Marketing Cloud Async API
  phrasing_intents:
  - id: getNextIndex
    intent: Get the next poll index for a topic
    question: How do I switch from managed polling to polling by my own index?
  - id: getPollCount
    intent: Count results already polled for a topic
    question: How many result items have been retrieved for a topic so far?
  - id: getSubmitCount
    intent: Count jobs submitted for a topic
    question: How many async jobs have been submitted for a topic?
  - id: pollByType
    intent: Poll events by event type
    question: Can I pull link click or read tracking events from the result queue by type?
  - id: pollByIndex
    intent: Poll topic results from an index
    question: Can I read queue results from an offset I manage myself?
  - id: pollByRange
    intent: Poll events within a time range
    question: Can I pull events of one type between two timestamps?
  - id: poll
    intent: Poll and consume results for a topic
    question: Are async results removed from the server once I poll them?
  - id: submit
    intent: Start an asynchronous API script job
    question: Can I run one of my custom API scripts asynchronously and collect results later?
  phrasing_ops: 8
  slug: mapp-async-api
- baseURL: https://{engage-host}/api/rest/v19
  baseurl_source: declared
  description: The Audit Log API from Mapp Marketing Cloud — 1 operation(s) for audit log.
  name: Mapp Marketing Cloud Audit Log API
  phrasing_intents:
  - id: auditLogEvents
    intent: List Log Tracker audit events
    question: Who changed what in my account over the last day?
  phrasing_ops: 1
  slug: mapp-audit-log-api
- baseURL: https://{engage-host}/api/rest/v19
  baseurl_source: declared
  description: Operations for obtaining or refreshing JWTs
  name: Mapp Marketing Cloud Authorization API
  phrasing_intents:
  - id: getOauthAuthorize
    intent: Start OAuth sign-in to get a grant code
    question: How do I begin the OAuth flow to get an access token?
  - id: postOauthToken
    intent: Exchange a grant code or refresh token for a JWT
    question: How do I swap my authorization code for an access token?
  phrasing_ops: 2
  slug: mapp-authorization-api
- baseURL: https://{engage-host}/api/rest/v19
  baseurl_source: declared
  description: The Automation API from Mapp Marketing Cloud — 3 operation(s) for automation.
  name: Mapp Marketing Cloud Automation API
  phrasing_intents:
  - id: find
    intent: Search automations
    question: Which time-based and event-based automations do we have?
  - id: getDetails
    intent: Get an automation's details
    question: What are the full settings of a specific automation?
  - id: runOnce
    intent: Run a time-based automation now
    question: Can I trigger a scheduled automation immediately without changing its schedule?
  phrasing_ops: 3
  slug: mapp-automation-api
- baseURL: https://{engage-host}/api/rest/v19
  baseurl_source: declared
  description: Get information about available objects you can use to build Analysis
  name: Mapp Marketing Cloud Available Objects API
  phrasing_intents:
  - id: getQueryObjects
    intent: List available dimensions and metrics
    question: Which dimensions and metrics can I use in an analytics query?
  - id: getDynamicTimefilters
    intent: List available dynamic time filters
    question: What relative time filters like last 7 days are available for analysis?
  - id: getSegments
    intent: List available segments
    question: Which saved segments can I apply to my Mapp Intelligence analyses?
  phrasing_ops: 3
  slug: mapp-available-objects-api
- baseURL: https://{engage-host}/api/rest/v19
  baseurl_source: declared
  description: The Blacklist API from Mapp Marketing Cloud — 6 operation(s) for blacklist.
  name: Mapp Marketing Cloud Blacklist API
  phrasing_intents:
  - id: createGroupEntries
    intent: Block addresses for one group
    question: How do I stop an email address or domain from receiving mail from one group?
  - id: createGroupEntriesHashed
    intent: Block hashed emails for one group
    question: Can I blacklist emails for a group using MD5 hashes instead of plain addresses?
  - id: createSystemEntriesHashed
    intent: Block hashed entries system-wide
    question: Can I add MD5-hashed emails or app aliases to the system-wide blacklist?
  - id: createSystemEntries
    intent: Block addresses system-wide
    question: How do I block an email, domain or phone number from every group at once?
  - id: deleteGroupEntries
    intent: Unblock addresses for one group
    question: How do I remove an email from a group's blacklist so they can get mail again?
  - id: deleteSystemEntries
    intent: Unblock addresses system-wide
    question: Can I take an address off the system-wide blacklist?
  phrasing_ops: 6
  slug: mapp-blacklist-api
- baseURL: https://{engage-host}/api/rest/v19
  baseurl_source: declared
  description: Endpoints for catalog metadata operations
  name: Mapp Marketing Cloud Catalog Metadata Operations API
  phrasing_intents:
  - id: getCatalogAttributes
    intent: List a catalog's active attributes
    question: Which attributes are assigned to a product catalog?
  - id: getCatalogMetadataByWorkspace
    intent: Get my workspace's catalog metadata
    question: Which product catalog is assigned to my workspace?
  phrasing_ops: 2
  slug: mapp-catalog-metadata-operations-api
- baseURL: https://{engage-host}/api/rest/v19
  baseurl_source: declared
  description: The CMS API from Mapp Marketing Cloud — 2 operation(s) for cms.
  name: Mapp Marketing Cloud CMS API
  phrasing_intents:
  - id: getMimeMessage
    intent: Download a CMS message in MIME format
    question: Can I get the raw MIME version of a CMS message?
  - id: getMessageDefinitions
    intent: List CMS message definitions
    question: Which CMS messages are saved in the system?
  phrasing_ops: 2
  slug: mapp-cms-api
- baseURL: https://{engage-host}/api/rest/v19
  baseurl_source: declared
  description: The Contact API from Mapp Marketing Cloud — 8 operation(s) for contact.
  name: Mapp Marketing Cloud Contact API
  phrasing_intents:
  - id: anonymize
    intent: Anonymize a contact's personal data (GDPR)
    question: How do I handle a GDPR erasure request for a contact?
  - id: checkUpdateVersion
    intent: Check whether a profile update was saved
    question: Has a specific contact profile update made it into the Data Store yet?
  - id: create
    intent: Create a contact
    question: How do I add a new contact with a first and last name?
  - id: delete
    intent: Delete a contact by identifier
    question: Can I delete a contact by passing its email or mobile identifier?
  - id: export
    intent: Export a contact's data (GDPR)
    question: How do I fulfil a GDPR data access request for a contact?
  - id: get
    intent: Get a contact by email or mobile identifier
    question: Can I fetch a contact by sending its email or mobile as an identifier object?
  - id: update
    intent: Update a contact
    question: Does updating a contact clear attributes I leave empty?
  - id: updateMultichannelContact
    intent: Update a multichannel contact and its mobile alias
    question: How do I update a contact that has both email and mobile channels?
  phrasing_ops: 8
  slug: mapp-contact-api
- baseURL: https://{engage-host}/api/rest/v19
  baseurl_source: declared
  description: The Content API from Mapp Marketing Cloud — 2 operation(s) for content.
  name: Mapp Marketing Cloud Content API
  phrasing_intents:
  - id: DeleteContent
    intent: Delete a Content Store element
    question: How do I delete an image or file from the Content Store?
  - id: store
    intent: Upload a file to the Content Store
    question: Can I upload an image for use in emails through the API?
  phrasing_ops: 2
  slug: mapp-content-api
- baseURL: https://{engage-host}/api/rest/v19
  baseurl_source: declared
  description: The Draft Message API from Mapp Marketing Cloud — 6 operation(s) for draft message.
  name: Mapp Marketing Cloud Draft Message API
  phrasing_intents:
  - id: CreateDraftMessage
    intent: Create a draft message
    question: How do I start a new email or SMS as a draft?
  - id: DeleteDraftMessage
    intent: Delete a draft message
    question: Can I throw away a draft message I no longer need?
  - id: FindDraftMessage
    intent: Search draft messages
    question: Which draft messages were created in the last week?
  - id: GetDraftMessage
    intent: Get a draft message
    question: What subject and body does a specific draft currently have?
  - id: saveAsPreparedMessage
    intent: Turn a draft into a prepared message
    question: How do I convert a draft into a prepared message for a group?
  - id: UpdateDraftMessage
    intent: Update a draft message
    question: Can I change the subject line of a draft I already created?
  phrasing_ops: 6
  slug: mapp-draft-message-api
- baseURL: https://{engage-host}/api/rest/v19
  baseurl_source: declared
  description: The Ecommerce API from Mapp Marketing Cloud — 8 operation(s) for ecommerce.
  name: Mapp Marketing Cloud Ecommerce API
  phrasing_intents:
  - id: createWishlistItem
    intent: Add a wish list item for a customer
    question: Can I record a product a shopper added to their wish list?
  - id: createAbandonedBrowseItem
    intent: Record an abandoned browse item
    question: How do I log a product a shopper viewed but didn't buy?
  - id: createAbandonedCartItem
    intent: Record an abandoned cart item
    question: Can I record a product left in a shopper's cart to drive recovery emails?
  - id: removeTransaction
    intent: Delete a customer's transaction
    question: How do I delete an order I registered for a customer by mistake?
  - id: removeWishlistItem
    intent: Remove a wish list item
    question: How do I take a product off a customer's wish list?
  - id: removeAbandonedBrowseItem
    intent: Remove an abandoned browse item
    question: Can I clear a browsed product from a shopper's abandoned browse list?
  - id: removeAbandonedCartItem
    intent: Remove an abandoned cart item
    question: How do I drop a product from a shopper's abandoned cart once they buy it?
  - id: registerTransaction
    intent: Register an ecommerce purchase
    question: Can I send completed orders into Mapp Engage with line items and custom columns?
  phrasing_ops: 8
  slug: mapp-ecommerce-api
- baseURL: https://{engage-host}/api/rest/v19
  baseurl_source: declared
  description: The Group API from Mapp Marketing Cloud — 11 operation(s) for group.
  name: Mapp Marketing Cloud Group API
  phrasing_intents:
  - id: activate
    intent: Reactivate archived groups
    question: Can I bring archived groups back into active use?
  - id: archive
    intent: Archive groups and their subgroups
    question: What happens to subgroups when I archive a group?
  - id: clone
    intent: Clone an existing group
    question: Can I duplicate a group with its sendout settings but without its members?
  - id: CreateGroup
    intent: Create a new group
    question: How do I create a new mailing group in Mapp Engage?
  - id: findIdsByAttributes
    intent: Find groups by group attribute values
    question: Which groups have a particular group attribute value set?
  - id: GetGroup
    intent: Get a group's details
    question: What settings and details does a specific group have?
  - id: getAttributes
    intent: Get all attributes of a group
    question: What group attribute values are set on this group?
  - id: getAllGroupSettingsTemplates
    intent: List group settings templates
    question: Which group settings templates are defined in our system?
  phrasing_ops: 11
  slug: mapp-group-api
- baseURL: https://{engage-host}/api/rest/v19
  baseurl_source: declared
  description: The Group Attributes API from Mapp Marketing Cloud — 8 operation(s) for group attributes.
  name: Mapp Marketing Cloud Group Attributes API
  phrasing_intents:
  - id: create_2
    intent: Create a group attribute
    question: How do I add a new attribute definition to a group?
  - id: delete_4
    intent: Delete group attributes by name
    question: Can I delete several group attributes at once by name?
  - id: get_3
    intent: Get a group attribute by name
    question: What's the definition of one named attribute on a group?
  - id: importAttributes
    intent: Import group attributes from CSV
    question: Can I bulk load group attributes from a CSV file?
  - id: list_2
    intent: List a group's attribute definitions
    question: Which attribute definitions exist for a particular group?
  - id: export_2
    intent: Export a group's attributes to CSV
    question: Can I export a group's attribute definitions as a CSV?
  - id: update_2
    intent: Update a group attribute definition
    question: Can I change an existing group attribute definition?
  - id: validateName
    intent: Check a group attribute name is unique
    question: Is an attribute name already used within a group?
  phrasing_ops: 8
  slug: mapp-group-attributes-api
- baseURL: https://{engage-host}/api/rest/v19
  baseurl_source: declared
  description: Operations for retrieving recommendations or items related to one or more seed items
  name: Mapp Marketing Cloud Items API
  phrasing_intents:
  - id: getItemsId
    intent: Get details about a garment
    question: What information is available about a specific garment in the catalog?
  - id: getItemsTop
    intent: Get top personalized item picks for a user
    question: Which items should I show a shopper on the homepage based on their profile?
  - id: getItemsIdComplementary
    intent: Get items that complete a look with source items
    question: What products go well with the items a customer is viewing?
  - id: getItemsIdRelated
    intent: Get similar items or outfits for one garment
    question: Which similar products can I show on a product detail page?
  - id: getItemsBasket
    intent: Get recommendations based on a shopper's basket
    question: What should I recommend at checkout given what's in the cart?
  phrasing_ops: 5
  slug: mapp-items-api
- baseURL: https://{engage-host}/api/rest/v19
  baseurl_source: declared
  description: The Landing Page API from Mapp Marketing Cloud — 4 operation(s) for landing page.
  name: Mapp Marketing Cloud Landing Page API
  phrasing_intents:
  - id: deleteLandingPage
    intent: Delete an inactive landing page
    question: How do I delete a landing page that's no longer live?
  - id: deleteMany
    intent: Delete several inactive landing pages
    question: Can I bulk delete multiple inactive landing pages by ID?
  - id: FindLandingPage
    intent: Find landing pages
    question: How can I look up landing pages in Mapp Engage?
  - id: getStatus
    intent: Check a landing page's publishing status
    question: Is a landing page still published or has it gone inactive?
  phrasing_ops: 4
  slug: mapp-landing-page-api
- baseURL: https://{engage-host}/api/rest/v19
  baseurl_source: declared
  description: The Member Attributes API from Mapp Marketing Cloud — 6 operation(s) for member attributes.
  name: Mapp Marketing Cloud Member Attributes API
  phrasing_intents:
  - id: create_3
    intent: Create a member attribute for a group
    question: How do I define a new group-specific attribute for members?
  - id: delete_2
    intent: Delete a member attribute from a group
    question: How do I remove a member attribute definition from a group?
  - id: get_4
    intent: Get one member attribute definition
    question: What are the settings of a single member attribute in a group?
  - id: list_3
    intent: List a group's member attributes
    question: Which member attributes are defined for a group?
  - id: update_3
    intent: Update a member attribute definition
    question: Can I rename or change a member attribute definition in a group?
  - id: validateName_2
    intent: Check a member attribute name is free
    question: Is a member attribute name already taken in a group?
  phrasing_ops: 6
  slug: mapp-member-attributes-api
- baseURL: https://{engage-host}/api/rest/v19
  baseurl_source: declared
  description: The Membership API from Mapp Marketing Cloud — 16 operation(s) for membership.
  name: Mapp Marketing Cloud Membership API
  phrasing_intents:
  - id: CreateMembership
    intent: Add a contact to a group silently
    question: Can I put a contact into a group in Mapp Engage without sending them a subscription notification?
  - id: DeleteMembership
    intent: Remove a contact from a group silently
    question: Is there a way to drop someone from a group without them getting an unsubscribe notice?
  - id: findAllByEmail
    intent: List every group a contact belongs to by email
    question: Which groups is a given email address a member of?
  - id: findAll
    intent: List every group a contact belongs to by user ID
    question: What groups is user ID 12345 a member of?
  - id: getByEmail
    intent: Check a contact's membership in one group by email
    question: Is this email address a member of a specific group, and what does the membership look like?
  - id: GetMembership
    intent: Check a contact's membership in one group by ID
    question: What does the membership record look like for one user ID in one group?
  - id: getAttributesByEmail
    intent: Read a contact's member attributes by email
    question: What group-specific attribute values are stored for an email address in a group?
  - id: GetMembershipAttributes
    intent: Read a contact's member attributes by ID
    question: Which member attribute values does a user ID have within a given group?
  phrasing_ops: 16
  slug: mapp-membership-api
- baseURL: https://{engage-host}/api/rest/v19
  baseurl_source: declared
  description: The Message API from Mapp Marketing Cloud — 14 operation(s) for message.
  name: Mapp Marketing Cloud Message API
  phrasing_intents:
  - id: FindMessage
    intent: Search sent and prepared messages
    question: Which messages went out to a group between two sendout dates?
  - id: getHistorical
    intent: See a message exactly as a contact received it
    question: Can I view a message as it was sent to one contact, with personalization filled in?
  - id: getStatisticsByExternalMessageId
    intent: Get sendout stats by external message ID
    question: How did a message perform if I only have my own external message ID for it?
  - id: getStatistics
    intent: Get sendout stats for a message
    question: What are the send statistics for a message I already sent?
  - id: getTimeDistributionByExternalMessageId
    intent: Get message time distribution via external-ID route
    question: Is there an external-ID variant of the time distribution report for a sent message?
  - id: getTimeDistribution
    intent: Get a message's activity over time
    question: When did recipients engage with a sent message, broken down hour by hour?
  - id: getUsedPersonalizations
    intent: List personalization fields a message uses
    question: Which user and group attributes does a prepared message reference in its placeholders?
  - id: getManyUsedPersonalizations
    intent: List personalization fields for several messages
    question: Can I check the personalization attributes of several prepared messages in one call?
  phrasing_ops: 14
  slug: mapp-message-api
- baseURL: https://{engage-host}/api/rest/v19
  baseurl_source: declared
  description: The Meta API from Mapp Marketing Cloud — 13 operation(s) for meta.
  name: Mapp Marketing Cloud Meta API
  phrasing_intents:
  - id: activateAttributeDefinitions
    intent: Reactivate archived custom attributes
    question: How do I bring an archived custom attribute back so it shows in the personalization builder?
  - id: archiveAttributeDefinitions
    intent: Archive custom attributes
    question: Can I hide a custom attribute from message creation without deleting its data?
  - id: attachTags
    intent: Attach tags to an entity
    question: How do I tag a message or other entity in Mapp Engage?
  - id: createAttributeDefinitions
    intent: Create custom user attributes
    question: How do I add a new custom data field to store information about users?
  - id: createLinkCategories
    intent: Create link categories
    question: Can I group links for reporting by matching them with a regex pattern?
  - id: deleteLinkCategory
    intent: Delete a link category
    question: How do I remove a link category I no longer need?
  - id: detachTags
    intent: Remove tags from an entity
    question: Can I take specific tags off an entity without touching the others?
  - id: findByTags
    intent: Find entities by tag
    question: Which entities carry a given tag?
  phrasing_ops: 13
  slug: mapp-meta-api
- baseURL: https://{engage-host}/api/rest/v19
  baseurl_source: declared
  description: The Mobile Push API from Mapp Marketing Cloud — 9 operation(s) for mobile push.
  name: Mapp Marketing Cloud Mobile Push API
  phrasing_intents:
  - id: cancelPushSend
    intent: Cancel a scheduled push send
    question: How do I stop a push notification send that's already scheduled?
  - id: createAndSchedulePushMessage
    intent: Create and schedule a push message
    question: Can I create a push notification for an app and schedule it in one call?
  - id: deletePushMessage
    intent: Delete a prepared push message
    question: How do I delete a prepared push message I won't send?
  - id: getPushMessage
    intent: Get a prepared push message
    question: What's in a prepared push message, such as its title and app?
  - id: pausePushSend
    intent: Pause a push send
    question: Can I temporarily halt a push notification sendout in progress?
  - id: resumePushSend
    intent: Resume a paused push send
    question: How do I restart a push sendout I paused?
  - id: SendSingleMobilePush
    intent: Send a push to one recipient
    question: Can I send a single mobile push notification to one recipient from a campaign?
  - id: MultiTenantSendSingleMobilePush
    intent: Send a push personalized from child users
    question: Can I send one push notification personalized with child user data across tenants?
  phrasing_ops: 9
  slug: mapp-mobile-push-api
- baseURL: https://{engage-host}/api/rest/v19
  baseurl_source: declared
  description: The Prepared Message API from Mapp Marketing Cloud — 4 operation(s) for prepared message.
  name: Mapp Marketing Cloud Prepared Message API
  phrasing_intents:
  - id: FindPreparedMessage
    intent: Search prepared messages by date
    question: Which prepared messages were created or updated in the last month?
  - id: GetPreparedMessage
    intent: Preview a prepared message for a contact
    question: Can I see a prepared message personalized for a specific contact?
  - id: send
    intent: Schedule a prepared message sendout
    question: Can I schedule a prepared message to go out at a set date and time?
  - id: UpdatePreparedMessage
    intent: Update a prepared message
    question: Can I edit a prepared message's settings, including tracking override?
  phrasing_ops: 4
  slug: mapp-prepared-message-api
- baseURL: https://{engage-host}/api/rest/v19
  baseurl_source: declared
  description: The Process API from Mapp Marketing Cloud — 3 operation(s) for process.
  name: Mapp Marketing Cloud Process API
  phrasing_intents:
  - id: applyAction
    intent: Change the status of a process
    question: Can I pause or resume a running process?
  - id: getProcessDetails
    intent: Get details of a process
    question: What's the current state of a particular process?
  - id: getProcessList
    intent: List processes
    question: Which processes have failed recently?
  phrasing_ops: 3
  slug: mapp-process-api
- baseURL: https://{engage-host}/api/rest/v19
  baseurl_source: declared
  description: Endpoints for product data operations
  name: Mapp Marketing Cloud Product Data Operations API
  phrasing_intents:
  - id: listVariants
    intent: List a product's variants
    question: Which variants like sizes and colours belong to a product in our catalog?
  phrasing_ops: 1
  slug: mapp-product-data-operations-api
- baseURL: https://{engage-host}/api/rest/v19
  baseurl_source: declared
  description: The Profile Attributes API from Mapp Marketing Cloud — 14 operation(s) for profile attributes.
  name: Mapp Marketing Cloud Profile Attributes API
  phrasing_intents:
  - id: archive_2
    intent: Archive profile attributes
    question: Can I retire profile attributes we no longer use without deleting them?
  - id: create_4
    intent: Create a profile attribute
    question: How do I add a new custom field to every contact's profile?
  - id: get_5
    intent: Get one profile attribute definition
    question: What data type and settings does a specific profile attribute have?
  - id: getAvailableChannels
    intent: List channels a profile attribute can be assigned to
    question: Which channels can I assign a profile attribute to?
  - id: getMarked
    intent: Get recipient statistics attribute settings
    question: Which profile attributes are currently flagged for recipient statistics?
  - id: getCapacity
    intent: Check remaining profile attribute capacity
    question: How many more profile attributes of each data type can I still create?
  - id: getTechnical
    intent: List technical system attributes
    question: What built-in system attributes does every profile have?
  - id: list_4
    intent: List custom profile attributes
    question: Which custom profile attributes have we defined?
  phrasing_ops: 14
  slug: mapp-profile-attributes-api
- baseURL: https://{engage-host}/api/rest/v19
  baseurl_source: declared
  description: Operations about recommendations
  name: Mapp Marketing Cloud Recommendations API
  phrasing_intents:
  - id: postRecommendationsFacetted
    intent: Get filterable garment recommendations for a user
    question: Can I get a user's most recommended garments filtered by category or colour?
  - id: getRecommendationsThemed
    intent: Get themed garment recommendations for a user
    question: Can I show a shopper recommended garments for a theme like summer holidays?
  phrasing_ops: 2
  slug: mapp-recommendations-api
- baseURL: https://{engage-host}/api/rest/v19
  baseurl_source: declared
  description: The Related Data API from Mapp Marketing Cloud — 4 operation(s) for related data.
  name: Mapp Marketing Cloud Related Data API
  phrasing_intents:
  - id: createRecord
    intent: Add a record to a related data set
    question: How do I add one row of data to a related data set for a contact?
  - id: deleteRecords
    intent: Delete related data records
    question: Can I delete only the related data rows that match a filter?
  - id: getRecordsByKey
    intent: Get related data records for a key
    question: What related data rows are stored for a particular customer?
  - id: updateRecords
    intent: Update related data records for a key
    question: Does updating related data without a filter delete and re-add all rows for the key?
  phrasing_ops: 4
  slug: mapp-related-data-api
- baseURL: https://{engage-host}/api/rest/v19
  baseurl_source: declared
  description: The Segmentation API from Mapp Marketing Cloud — 10 operation(s) for segmentation.
  name: Mapp Marketing Cloud Segmentation API
  phrasing_intents:
  - id: create_5
    intent: Create a selection plan
    question: How do I build a new audience segment as a selection plan?
  - id: delete_3
    intent: Delete a selection plan
    question: Can I undo deleting a selection plan?
  - id: find_2
    intent: Search selection plans
    question: Which selection plans do we have, page by page?
  - id: getCount
    intent: Get the size of a segment
    question: How many contacts are in a published segment?
  - id: get_2
    intent: Get a selection plan in full
    question: Can I fetch a selection plan with every node and selector setting so I can edit it?
  - id: schema
    intent: Get the selection plan JSON schema
    question: What node types and selectors can a selection plan use?
  - id: preview
    intent: Preview a selection plan's structure
    question: Can I get a lightweight summary of a segment's criteria without full configuration?
  - id: publish
    intent: Publish a selection plan
    question: How do I make a draft segment live and get a selection term ID?
  phrasing_ops: 10
  slug: mapp-segmentation-api
- baseURL: https://{engage-host}/api/rest/v19
  baseurl_source: declared
  description: The System API from Mapp Marketing Cloud — 2 operation(s) for system.
  name: Mapp Marketing Cloud System API
  phrasing_intents:
  - id: getApiVersion
    intent: Get the API version in use
    question: Which REST API version is my Mapp Engage system running?
  - id: getEcmVersion
    intent: Get the Engage build version
    question: What build of the Engage platform is my system on?
  phrasing_ops: 2
  slug: mapp-system-api
- baseURL: https://{engage-host}/api/rest/v19
  baseurl_source: declared
  description: The System User API from Mapp Marketing Cloud — 5 operation(s) for system user.
  name: Mapp Marketing Cloud System User API
  phrasing_intents:
  - id: createSystemUser
    intent: Create a system user account
    question: How do I give a new colleague access to Mapp Engage?
  - id: deleteSystemUser
    intent: Delete a system user account
    question: How do I remove a colleague's login when they leave?
  - id: getSystemUser
    intent: Look up a system user account
    question: What role and language does a given system user have?
  - id: updatePassword
    intent: Set a system user's password
    question: How do I reset a colleague's login password?
  - id: updateSystemUser
    intent: Update a system user's details
    question: Can I change a system user's name or messaging role?
  phrasing_ops: 5
  slug: mapp-system-user-api
- baseURL: https://{engage-host}/api/rest/v19
  baseurl_source: declared
  description: The Usage Statistics API from Mapp Marketing Cloud — 2 operation(s) for usage statistics.
  name: Mapp Marketing Cloud Usage Statistics API
  phrasing_intents:
  - id: ExportGetUsageStatistics
    intent: Export account usage statistics
    question: Can I get our API usage statistics emailed as an export file?
  - id: getUsageStatistics
    intent: Get account usage statistics
    question: How many API calls did we make last month?
  phrasing_ops: 2
  slug: mapp-usage-statistics-api
- baseURL: https://{engage-host}/api/rest/v19
  baseurl_source: declared
  description: The User API from Mapp Marketing Cloud — 18 operation(s) for user.
  name: Mapp Marketing Cloud User API
  phrasing_intents:
  - id: createUser
    intent: Create a user by email or mobile number
    question: How do I add a new user to Mapp Engage?
  - id: deleteByEmail
    intent: Delete a user by email address
    question: Can I delete a user if I only know their email address?
  - id: deleteByMobileNumber
    intent: Delete a user by mobile number
    question: Is there a way to delete a user using just their phone number?
  - id: deleteUser
    intent: Delete a user by user ID
    question: How do I delete a user when I have their internal user ID?
  - id: getUserByEmail
    intent: Look up a user by email
    question: How can I find a user's ID from their email address?
  - id: getByIdentifier
    intent: Look up a user by profile identifier
    question: Can I find a user by our own custom identifier instead of email?
  - id: getByMobileNumber
    intent: Look up a user by mobile number
    question: How do I find a user record from a phone number?
  - id: getMessageHistory
    intent: Get the messages sent to a user
    question: Which messages did a particular recipient receive last month?
  phrasing_ops: 18
  slug: mapp-user-api
- baseURL: https://{engage-host}/api/rest/v19
  baseurl_source: declared
  description: Endpoints for variant data bulk operations
  name: Mapp Marketing Cloud Variant Data Bulk Operations API
  phrasing_intents:
  - id: bulkAddVariants
    intent: Add many variants without overwriting
    question: Can I bulk load variants while keeping values that already exist?
  - id: bulkDeleteVariants
    intent: Delete many variants at once
    question: How do I delete a batch of variants from a catalog in one call?
  - id: bulkPartialUpdateVariants
    intent: Change selected fields on many variants
    question: Can I update just the prices on hundreds of variants at once?
  - id: bulkUpsertVariants
    intent: Create or replace many variants at once
    question: Can I fully overwrite up to 1000 variants in one request?
  phrasing_ops: 4
  slug: mapp-variant-data-bulk-operations-api
- baseURL: https://{engage-host}/api/rest/v19
  baseurl_source: declared
  description: Endpoints for variant data operations
  name: Mapp Marketing Cloud Variant Data Operations API
  phrasing_intents:
  - id: addVariant
    intent: Add a variant without overwriting data
    question: Can I add a product variant and only fill in fields that are missing?
  - id: getPaginatedVariants
    intent: List catalog variants page by page
    question: How do I page through every variant in a product catalog?
  - id: upsertVariant
    intent: Create or fully replace a variant
    question: How do I completely overwrite a variant's data with a new payload?
  - id: deleteVariant
    intent: Delete one variant
    question: How do I remove a single variant, including its enriched data?
  - id: getVariant
    intent: Get one variant from a catalog
    question: What data does the catalog hold for a single variant ID?
  - id: partialUpdateVariant
    intent: Change selected fields on a variant
    question: Can I change just the price of one variant and leave the rest untouched?
  - id: deleteAllCatalogData
    intent: Wipe every variant from a catalog
    question: Is there a way to clear an entire product catalog's contents?
  - id: deleteVariantAttributes
    intent: Remove named attributes from a variant
    question: Can I strip a few attributes off a variant without deleting it?
  phrasing_ops: 8
  slug: mapp-variant-data-operations-api
- baseURL: https://{engage-host}/api/rest/v19
  baseurl_source: declared
  description: The Whiteboard API from Mapp Marketing Cloud — 8 operation(s) for whiteboard.
  name: Mapp Marketing Cloud Whiteboard API
  phrasing_intents:
  - id: save
    intent: Create or update a whiteboard
    question: How do I save a customer journey whiteboard in the Audience Interaction Planner?
  - id: delete_5
    intent: Delete a whiteboard
    question: What gets removed along with a whiteboard when I delete it?
  - id: publish_2
    intent: Publish a whiteboard
    question: How do I make a whiteboard journey live?
  - id: get_6
    intent: Get a whiteboard with all versions
    question: Can I see every version of a specific whiteboard?
  - id: listTemplates
    intent: List whiteboard templates
    question: What starter templates are available for new whiteboards?
  - id: find_3
    intent: Search whiteboards
    question: Which whiteboards have we created, most recently updated first?
  - id: schema_2
    intent: Get the whiteboard JSON schema
    question: What JSON structure does a whiteboard need to follow?
  - id: validate_2
    intent: Validate a whiteboard without saving
    question: Can I check a whiteboard for errors before saving or publishing it?
  phrasing_ops: 8
  slug: mapp-whiteboard-api
artifact_total: 50
asyncapis:
- description: ''
  name: Mapp Data Streams
  slug: mapp-data-streams
collections:
- collection_type: open
  name: Mapp Engage public API
  slug: open-mapp-engage
- collection_type: open
  name: Mapp Fashion API
  slug: open-mapp-fashion
- collection_type: open
  name: Analytics API
  slug: open-mapp-intelligence-analytics
- collection_type: open
  name: Product Catalog - Public API
  slug: open-mapp-product-catalog
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/mapp/refs/heads/main/capabilities/mapp-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/mapp-capability-edges.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/mapp/refs/heads/main/overlays/mapp-engage-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/mapp-engage-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/mapp/refs/heads/main/overlays/mapp-intelligence-analytics-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/mapp-intelligence-analytics-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/mapp/refs/heads/main/overlays/mapp-product-catalog-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/mapp-product-catalog-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/mapp/refs/heads/main/overlays/mapp-fashion-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/mapp-fashion-overlay.yaml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/mapp/refs/heads/main/security/mapp-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/mapp-trust-center.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/mapp/refs/heads/main/packages/mapp-packages.yml
  title: ''
  type: Packages
  url: packages/mapp-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/mapp/refs/heads/main/packages/mapp-packages.yml
  title: ''
  type: SDKs
  url: packages/mapp-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/mapp/refs/heads/main/well-known/mapp-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/mapp-well-known.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/mapp/refs/heads/main/mcp/mapp-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/mapp-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/mapp/refs/heads/main/mcp/mapp-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/mapp-tool-crosswalk.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/mapp/refs/heads/main/conformance/mapp-conformance.yml
  title: ''
  type: Conformance
  url: conformance/mapp-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/mapp/refs/heads/main/errors/mapp-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/mapp-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/mapp/refs/heads/main/lifecycle/mapp-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/mapp-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.mapp.com/docs/news
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/mapp/refs/heads/main/conventions/mapp-conventions.yml
  title: ''
  type: Conventions
  url: conventions/mapp-conventions.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/mapp/refs/heads/main/changelog/mapp-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/mapp-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/mapp/refs/heads/main/data-model/mapp-data-model.yml
  title: ''
  type: DataModel
  url: data-model/mapp-data-model.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/mapp/refs/heads/main/plans/mapp-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/mapp-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/mapp/refs/heads/main/rate-limits/mapp-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/mapp-rate-limits.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/mapp/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/mapp/refs/heads/main/asyncapi/mapp-data-streams.yml
  title: ''
  type: Events
  url: asyncapi/mapp-data-streams.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/mapp/refs/heads/main/asyncapi/mapp-data-streams.yml
  title: ''
  type: StreamingEndpoint
  url: asyncapi/mapp-data-streams.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/mapp/refs/heads/main/security/mapp-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/mapp-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/mapp/refs/heads/main/scopes/mapp-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/mapp-scopes.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/mapp/refs/heads/main/authentication/mapp-authentication.yml
  title: ''
  type: Authentication
  url: authentication/mapp-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://mapp.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.mapp.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.mapp.com/docs/api-documentation
- group: docs
  title: ''
  type: APIReference
  url: https://docs.mapp.com/apidocs/engage-api-calls
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.mapp.com/apidocs/getting-started-with-engage-api
- group: operate
  title: ''
  type: Support
  url: https://support.mapp.com/
- group: operate
  title: ''
  type: HelpCenter
  url: https://mapp.com/technical-support/
- group: company
  title: ''
  type: Blog
  url: https://mapp.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/mapp-digital
- group: commercial
  title: ''
  type: Pricing
  url: https://mapp.com/mapp-marketing-cloud-pricing/
- group: start
  title: ''
  type: SignUp
  url: https://mapp.com/request-demo/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://mapp.com/legal/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://mapp.com/privacy-mapp-cloud/
- group: auth
  title: ''
  type: TrustCenter
  url: https://mapp.com/trust/
- group: auth
  title: ''
  type: Compliance
  url: https://mapp.com/trust/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.webtrekk.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.mapp.com/docs/news
- group: build
  title: ''
  type: Postman
  url: https://docs.mapp.com/apidocs/postman
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/mapp/refs/heads/main/llms/mapp-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/mapp-llms.txt
created: '2026-08-12'
description: 'Mapp is a German-headquartered marketing technology vendor whose Mapp Marketing Cloud combines cross-channel campaign execution (Mapp Engage), digital analytics and customer intelligence (Mapp Intelligence, formerly Webtrekk), product catalog management, and AI fashion/retail recommendations (Mapp Fashion, formerly Dressipi). The platform is API-addressable across four public surfaces: the Mapp Engage REST API (REST 2.0 / v19, HTTP Basic auth, ~196 documented operations covering contacts, memberships, groups, messages, mobile push, segmentation, whiteboards, attributes, e-commerce events and audit logs), the Mapp Intelligence Analytics API (OAuth2 client-credentials on api.mapp.com/api/analytics), the Product Catalog Public API, and the Mapp Fashion recommendation API. Mapp publishes machine-readable OpenAPI fragments for every endpoint on docs.mapp.com, an llms.txt documentation index, published list pricing, and an ISO 27001/27017/27018/27701/22301 trust center.'
image: https://mapp.com/wp-content/uploads/2026/05/mapp-default-open-graph-image-square.png
layout: provider
mcp_servers:
- description: ''
  name: Mapp Marketing Cloud MCP Server
  slug: mapp-marketing-cloud-mcp-server
modified: '2026-08-12'
name: Mapp Marketing Cloud
nav: Providers
network: true
overview: 'Mapp Marketing Cloud publishes 37 APIs on the [APIs.io](https://apis.io/) network, including Address Attributes API, Analysis API, Async API, and 34 more. Tagged areas include Company, Marketing, Marketing Automation, Email, and Analytics.


  The Mapp Marketing Cloud catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Mapp Marketing Cloud''s developer surface includes changelog, authentication, documentation, API reference, getting-started guide, support, engineering blog, and 38 more developer resources.'
plans:
- name: Mapp Plans Pricing
  plan_count: 3
  slug: mapp-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 1
  name: Mapp Rate Limits
  slug: mapp-rate-limits
scopes:
- name: Mapp Scopes
  scope_count: 2
  slug: mapp-scopes
  summary_line: 2 scopes · clientCredentials
score:
  band: exemplar
  composite: 70.4
  coverage:
    artifact_dirs: 24
    catalog_earned: 60.0
    catalog_earned_first_party: 20.0
    catalog_gap: 55.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 92.1
    contract_governance: 18.2
    contract_quality: 53.4
    developer_ergonomics: 70.8
    discoverability: 80.0
    operational_transparency: 63.2
  previous_composite: 70.4
  provenance:
    conformance: first-party
    contracts:
      callable: 16.2
      derived: 0
      marker_coverage: 100.0
      total: 37
    mcp: site-plugin
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: dora
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: EU
      standard: nis2
    - jurisdiction: US
      standard: ccpa
    jurisdictions_satisfied: 2
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 43.3
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  trend: flat
  upsert:
    applies: true
    score: 33.3
screenshot: https://raw.githubusercontent.com/api-evangelist/mapp/refs/heads/main/screenshots/mapp-2026-08-17T080404.png
security:
- kind: authentication
  name: Mapp Authentication
  slug: mapp-authentication
  summary_line: http/oauth2 · 3 schemes
- kind: domain-security
  name: Mapp Domain Security
  slug: mapp-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Mapp Vulnerability Disclosure
  slug: mapp-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Mapp Trust Center
  slug: mapp-trust-center
  summary_line: ISO 27001, ISO 27017, ISO 27018, ISO 27701, ISO 22301, GDPR, CCPA, NIS-2, DORA, Certified Sender Alliance
slug: mapp
tags:
- Company
- Marketing
- Marketing Automation
- Email
- Analytics
- Customer Data
- Personalization
- Push Notifications
- SMS
- E-Commerce
- Digital Analytics
- Recommendations
website: https://mapp.com/
---
