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
    agent_card: flavored
    agent_skills: derived
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
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 69.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 89
  human_in_the_loop: 0
  name: Customer Io Agentic Access
  operation_count: 191
  slug: customer-io-agentic-access
  summary_line: 191 operations · 89 acting
api_count: 5
apis:
- baseURL: https://track.customer.io
  baseurl_source: declared
  description: The Customer.io Track API allows developers to send behavioral data and customer profile information into Customer.io. It provides endpoints for identifying customers, tracking events, managing device
  name: Customer.io Track API
  phrasing_intents:
  - id: track
    intent: Track an event for a person
    question: How do I record that a user completed a purchase in my app?
  phrasing_ops: 1
  slug: track-api
- baseURL: https://api.customer.io
  baseurl_source: declared
  description: Retrieve activity logs for your workspace.
  name: Customer.io Activities API
  phrasing_intents:
  - id: listActivities
    intent: List workspace activity history
    question: Where can I see a feed of recent activity across all my people, like the Activity Logs page?
  phrasing_ops: 1
  slug: customer-io-activities-api
- baseURL: https://cdp.customer.io/v1
  baseurl_source: declared
  description: Merge two user identities by creating an alias linking a new identity to an existing one.
  name: Customer.io Alias API
  phrasing_intents:
  - id: alias
    intent: Merge a previous identifier into a user
    question: How do I link an anonymous visitor's old ID to their new user ID for destinations like Mixpanel?
  phrasing_ops: 1
  slug: customer-io-alias-api
- baseURL: https://track.customer.io
  baseurl_source: declared
  description: Send multiple API calls in a single request for improved performance.
  name: Customer.io Batch API
  phrasing_intents:
  - id: batch
    intent: Send several tracking calls in one request
    question: How do I send identify, track and page calls together in a single request?
  phrasing_ops: 1
  slug: customer-io-batch-api
- baseURL: https://api.customer.io
  baseurl_source: declared
  description: Trigger API-triggered broadcasts to send messages to groups of people based on segments or filters.
  name: Customer.io Broadcasts API
  phrasing_intents:
  - id: broadcastErrors
    intent: Get validation errors for a broadcast trigger
    question: Why did my API-triggered broadcast fail validation?
  - id: listBroadcasts
    intent: List API-triggered broadcasts
    question: What API-triggered broadcasts do I have set up?
  - id: getBroadcast
    intent: Get a broadcast
    question: How do I look up the settings of one API-triggered broadcast?
  - id: broadcastStatus
    intent: Check the status of a broadcast trigger
    question: Did the broadcast I just triggered finish processing?
  - id: broadcastMetrics
    intent: Get broadcast delivery metrics over time
    question: How many emails did my broadcast deliver and open each day?
  - id: broadcastLinks
    intent: Get link click metrics for a broadcast
    question: Which links in my broadcast got the most clicks?
  - id: broadcastActions
    intent: List the actions in a broadcast
    question: What messages and steps make up a broadcast?
  - id: broadcastMessages
    intent: List deliveries sent by a broadcast
    question: Who received messages from my API-triggered broadcast?
  phrasing_ops: 15
  slug: customer-io-broadcasts-api
- baseURL: https://api.customer.io
  baseurl_source: declared
  description: Manage collections of data used in message personalization.
  name: Customer.io Collections API
  phrasing_intents:
  - id: addCollection
    intent: Create a collection
    question: How do I upload a lookup table of data I can reference in messages?
  - id: getCollections
    intent: List collections
    question: What data collections do I have for use in messages?
  - id: getCollection
    intent: Get a collection
    question: How do I look up one collection's name and schema?
  - id: deleteCollection
    intent: Delete a collection
    question: How do I remove a collection I no longer use?
  - id: updateCollection
    intent: Rename or replace a collection
    question: Can I rename a collection?
  - id: getCollectionContents
    intent: Get the rows in a collection
    question: How do I read the actual data rows stored in a collection?
  - id: updateCollectionContents
    intent: Replace the rows in a collection
    question: How do I overwrite a collection's data without changing its name?
  phrasing_ops: 7
  slug: customer-io-collections-api
- baseURL: https://track.customer.io
  baseurl_source: declared
  description: Look up customer profiles, search for customers, and retrieve customer attributes and activity data.
  name: Customer.io Customers API
  phrasing_intents:
  - id: getPeopleEmail
    intent: Find people by email address
    question: How do I find a person's profile when I only know their email?
  - id: getPeopleFilter
    intent: Search people by segment or attribute
    question: How do I find everyone in a segment whose plan attribute is premium?
  - id: getPersonAttributes
    intent: Get a person's attributes
    question: What attributes are stored on a person's profile?
  - id: getPersonRelationships
    intent: List objects a person is related to
    question: Which companies or accounts is a person linked to?
  - id: getPeopleById
    intent: Get attributes and devices for many people
    question: How do I fetch attributes and devices for a batch of people at once?
  - id: getPersonSegments
    intent: List a person's segments
    question: Which segments is a given person in?
  - id: getPersonMessages
    intent: List messages sent to a person
    question: What messages has a specific person received from us?
  - id: getPersonActivities
    intent: List a person's activity history
    question: What has a person done recently, like attribute changes and events?
  phrasing_ops: 9
  slug: customer-io-customers-api
- baseURL: https://api.customer.io
  baseurl_source: declared
  description: Export customer data, deliveries, and other information from your workspace.
  name: Customer.io Exports API
  phrasing_intents:
  - id: listExports
    intent: List exports
    question: What data exports have I run?
  - id: getExport
    intent: Check an export's status
    question: Is my export finished yet?
  - id: downloadExport
    intent: Get a download link for an export
    question: How do I download the file from a finished export?
  - id: exportPeopleData
    intent: Export people matching filters
    question: How do I export a CSV of people who match certain filters?
  - id: exportDeliveriesData
    intent: Export delivery data for messages
    question: How do I export delivery records for a newsletter or campaign?
  phrasing_ops: 5
  slug: customer-io-exports-api
- baseURL: https://cdp.customer.io/v1
  baseurl_source: declared
  description: Associate people with groups or organizations.
  name: Customer.io Group API
  phrasing_intents:
  - id: group
    intent: Add a person to a group or company
    question: How do I associate a user with a company or account?
  phrasing_ops: 1
  slug: customer-io-group-api
- baseURL: https://cdp.customer.io/v1
  baseurl_source: declared
  description: Identify people and set their profile attributes. The identify call tells Customer.io who the current user is and assigns traits to them.
  name: Customer.io Identify API
  phrasing_intents:
  - id: identify
    intent: Identify a person and set traits
    question: How do I create or update a person with traits through Data Pipelines?
  phrasing_ops: 1
  slug: customer-io-identify-api
- baseURL: https://api.customer.io
  baseurl_source: declared
  description: Retrieve information about individual messages sent to customers.
  name: Customer.io Messages API
  phrasing_intents:
  - id: listMessages
    intent: List message deliveries in the workspace
    question: How do I see all the messages my workspace sent yesterday?
  - id: getMessage
    intent: Get a delivery and its metrics
    question: Was a specific message delivered and opened?
  - id: getArchivedMessage
    intent: Get the archived copy of a message
    question: How do I see exactly what content a person received in a message?
  phrasing_ops: 3
  slug: customer-io-messages-api
- baseURL: https://api.customer.io
  baseurl_source: declared
  description: Retrieve information about newsletters and newsletter variants.
  name: Customer.io Newsletters API
  phrasing_intents:
  - id: listNewsletters
    intent: List newsletters
    question: What newsletters have I created?
  - id: createNewsletter
    intent: Create and send or schedule a newsletter
    question: How do I create a newsletter and send it right away through the API?
  - id: getNewsletters
    intent: Get a newsletter
    question: How do I look up one newsletter's settings and status?
  - id: deleteNewsletters
    intent: Delete a newsletter
    question: How do I delete a newsletter I don't need anymore?
  phrasing_ops: 4
  slug: customer-io-newsletters-api
- baseURL: https://cdp.customer.io/v1
  baseurl_source: declared
  description: Record page views from web applications.
  name: Customer.io Page API
  phrasing_intents:
  - id: page
    intent: Track a web page view
    question: How do I record page views from a single-page app?
  phrasing_ops: 1
  slug: customer-io-page-api
- baseURL: https://cdp.customer.io/v1
  baseurl_source: declared
  description: Record screen views from mobile applications.
  name: Customer.io Screen API
  phrasing_intents:
  - id: screen
    intent: Track a mobile screen view
    question: How do I record which screens people view in my mobile app?
  phrasing_ops: 1
  slug: customer-io-screen-api
- baseURL: https://api.customer.io
  baseurl_source: declared
  description: Create and manage manual segments, and retrieve segment membership information.
  name: Customer.io Segments API
  phrasing_intents:
  - id: createManSegment
    intent: Create a manual segment
    question: How do I create an empty manual segment through the API?
  - id: listSegments
    intent: List segments
    question: What segments do I have in my workspace?
  - id: getSegment
    intent: Get a segment
    question: How do I look up one segment's details?
  - id: deleteManSegment
    intent: Delete a manual segment
    question: How do I delete a manual segment?
  - id: getSegmentDependencies
    intent: See which campaigns use a segment
    question: Which campaigns and newsletters use this segment?
  - id: getSegmentCount
    intent: Count people in a segment
    question: How many people are in a segment right now?
  - id: getSegmentMembership
    intent: List people in a segment
    question: Who exactly is in a given segment?
  phrasing_ops: 7
  slug: customer-io-segments-api
- baseURL: https://api.customer.io
  baseurl_source: declared
  description: Manage sender identities used for sending messages.
  name: Customer.io Sender Identities API
  phrasing_intents:
  - id: listSenders
    intent: List sender identities
    question: Which from addresses are set up in my workspace?
  - id: getSender
    intent: Get a sender identity
    question: How do I see the name and email of one sender?
  - id: getSenderUsage
    intent: See which campaigns use a sender
    question: Which campaigns and newsletters send from a given sender?
  phrasing_ops: 3
  slug: customer-io-sender-identities-api
- baseURL: https://api.customer.io
  baseurl_source: declared
  description: Manage reusable content snippets for use in messages.
  name: Customer.io Snippets API
  phrasing_intents:
  - id: listSnippets
    intent: List snippets
    question: What reusable snippets, like footers, do I have?
  - id: createSnippet
    intent: Create a new snippet
    question: How do I add a new reusable footer snippet?
  - id: updateSnippets
    intent: Create or update a snippet by name
    question: How do I change the value of an existing snippet?
  - id: deleteSnippet
    intent: Delete a snippet
    question: How do I delete a snippet?
  phrasing_ops: 4
  slug: customer-io-snippets-api
- baseURL: https://api.customer.io
  baseurl_source: declared
  description: Send transactional messages such as password resets, purchase receipts, and other important notifications triggered by user actions.
  name: Customer.io Transactional API
  phrasing_intents:
  - id: listTransactional
    intent: List transactional messages
    question: What transactional message templates do I have?
  - id: getTransactional
    intent: Get a transactional message
    question: How do I look up the settings of one transactional message?
  - id: listTransactionalVariants
    intent: List a transactional message's languages
    question: Which languages is my transactional message translated into?
  - id: updateTransactional
    intent: Overwrite a transactional message's content
    question: How do I update the body of a transactional email template?
  - id: getTransactionalVariant
    intent: Get a translation of a transactional message
    question: How do I see the Spanish version of a transactional email?
  - id: updateTransactionalVariant
    intent: Update a translation of a transactional message
    question: How do I edit the French translation of a transactional email?
  - id: transactionalMetrics
    intent: Get transactional message metrics
    question: How many password reset emails went out and were opened each day?
  - id: transactionalLinks
    intent: Get link clicks for a transactional message
    question: Which links in my transactional email were clicked?
  phrasing_ops: 9
  slug: customer-io-transactional-api
- description: Customer.io's first-party hosted Model Context Protocol server. It exposes the full Journeys App API and CDP Data Pipelines API to any MCP client through eight tools — a context primer, a schema brows
  name: Customer.io MCP
  slug: mcp
- baseURL: https://track.customer.io
  baseurl_source: declared
  description: Manage file assets such as images and PDFs and organize them into folders.
  name: Customer.io Assets API
  phrasing_intents:
  - id: listAssets
    intent: List file assets
    question: How do I see all the images and PDFs uploaded to my asset library?
  - id: createAsset
    intent: Upload a file asset
    question: How do I upload an image or PDF to the asset library through the API?
  - id: getAsset
    intent: Get a file asset
    question: How do I look up the details of one uploaded file asset?
  - id: updateAsset
    intent: Rename or move a file asset
    question: Can I rename an uploaded file asset without re-uploading it?
  - id: deleteAsset
    intent: Delete a file asset
    question: How do I remove an uploaded image from my asset library?
  - id: listAssetFolders
    intent: List asset folders
    question: What folders exist in my file asset library?
  - id: createAssetFolder
    intent: Create an asset folder
    question: How do I create a folder to organize my uploaded files?
  - id: getAssetFolder
    intent: Get an asset folder
    question: How do I look up one folder in my asset library by ID?
  phrasing_ops: 10
  slug: customer-io-assets-api
- baseURL: https://track.customer.io
  baseurl_source: declared
  description: Update descriptions for attributes and events in your workspace. This helps improve AI-generated content and segments.
  name: Customer.io Data Index API
  phrasing_intents:
  - id: updateAttributeMetadata
    intent: Add or update attribute definitions
    question: How do I register new customer attributes in my workspace's data index?
  - id: updateEventMetadata
    intent: Add or update event definitions
    question: How do I register new event names in my workspace's data index?
  phrasing_ops: 2
  slug: customer-io-data-index-api
- baseURL: https://track.customer.io
  baseurl_source: declared
  description: If you use Customer.io as your email service provider (ESP), these endpoints help you retrieve information about email addresses suppressed directly by the ESP. ESP-based suppressions are different fr
  name: Customer.io ESP Suppression API
  phrasing_intents:
  - id: getSuppression
    intent: Check whether an email is ESP-suppressed
    question: Why isn't a particular address receiving our emails, is it suppressed?
  - id: getSuppressionByType
    intent: List ESP-suppressed emails by reason
    question: Which addresses have bounced or reported us as spam?
  - id: getDomainSuppressionsByType
    intent: List ESP suppressions for a sending domain
    question: Which addresses were suppressed on one of my sending domains?
  - id: deleteSuppression
    intent: Remove an address from ESP suppression
    question: How do I un-suppress an email address that bounced?
  - id: postSuppression
    intent: Suppress an email address at the ESP
    question: How do I stop the email provider from sending to a specific address?
  phrasing_ops: 5
  slug: customer-io-esp-suppression-api
- baseURL: https://track.customer.io
  baseurl_source: declared
  description: Connect forms to your workspace to identify people, apply form responses to people, and trigger campaigns for people who fill out forms on your website or in your app.
  name: Customer.io Forms API
  phrasing_intents:
  - id: submitForm
    intent: Submit a form response
    question: How do I send form submissions from my own website into the platform?
  phrasing_ops: 1
  slug: customer-io-forms-api
- baseURL: https://track.customer.io
  baseurl_source: declared
  description: APIs to upload CSV files containing lists of people. These endpoints provide a convenient way to add and update people without having to make an `identify` call for each individual person.
  name: Customer.io Imports API
  phrasing_intents:
  - id: import
    intent: Import people or events from a CSV
    question: How do I bulk upload people, events or objects from a CSV file?
  - id: getImport
    intent: Check a bulk import
    question: Did my CSV import finish, and how many rows failed?
  phrasing_ops: 2
  slug: customer-io-imports-api
- baseURL: https://track.customer.io
  baseurl_source: declared
  description: Returns the list of addresses used by Customer.io. You must add add these addresses to your allowlist when using a custom SMTP provider and blocking unknown IP addresses.
  name: Customer.io Info API
  phrasing_intents:
  - id: getCioAllowlist
    intent: List IP addresses to allowlist
    question: Which IP addresses do I need to allowlist in my firewall?
  phrasing_ops: 1
  slug: customer-io-info-api
- baseURL: https://track.customer.io
  baseurl_source: declared
  description: 'Start, update, and end live notifications—real-time activities on the iOS Lock Screen and Dynamic Island, and in the Android notification shade. Your server drives the activity''s content; Customer.io '
  name: Customer.io Live Notifications API
  phrasing_intents:
  - id: startLiveNotification
    intent: Start a live notification
    question: How do I start a Live Activity on someone's iPhone lock screen?
  - id: updateLiveNotification
    intent: Update a running live notification
    question: How do I push a new state to a Live Activity that's already running?
  - id: endLiveNotification
    intent: End a live notification
    question: How do I end a Live Activity and dismiss it from the lock screen?
  - id: getLiveNotification
    intent: Get a live notification's status
    question: Is a live notification still running, and was its last update delivered?
  phrasing_ops: 4
  slug: customer-io-live-notifications-api
- baseURL: https://track.customer.io
  baseurl_source: declared
  description: 'Newsletter metrics include metrics for translations, A/B tests, and links. These endpoints return information about newsletter metrics including metrics for translations and A/B tests. You can update '
  name: Customer.io Newsletter Metrics API
  phrasing_intents:
  - id: getNewsletterMetrics
    intent: Get newsletter metrics over time
    question: How many opens and clicks did my newsletter get each day?
  - id: getNewsletterLinks
    intent: Get link click metrics for a newsletter
    question: Which links in my newsletter were clicked the most?
  - id: getNewsletterMsgMeta
    intent: List deliveries sent by a newsletter
    question: Who received my newsletter and did they open it?
  - id: getVariantMetrics
    intent: Get metrics for a newsletter variant
    question: How did variant B of my newsletter A/B test perform?
  - id: getVariantLinks
    intent: Get link clicks for a newsletter variant
    question: Which links were clicked in one A/B test variant of my newsletter?
  phrasing_ops: 5
  slug: customer-io-newsletter-metrics-api
- baseURL: https://track.customer.io
  baseurl_source: declared
  description: A newsletter variant is a translation or an A/B test. You can create, update, or delete variants in newsletters from these endpoints. You can also create a new A/B test group. If your newsletters incl
  name: Customer.io Newsletter Variants API
  phrasing_intents:
  - id: listNewsletterVariants
    intent: List a newsletter's content variants
    question: What language and A/B test variants does my newsletter have?
  - id: getNewsletterVariant
    intent: Get one newsletter variant by content ID
    question: How do I read the content of one specific newsletter variant?
  - id: updateNewsletterVariant
    intent: Update a newsletter variant by content ID
    question: How do I change the body or subject of a newsletter variant?
  - id: createNewsletterLanguageVariant
    intent: Add a translation to a newsletter
    question: How do I add a French translation to my newsletter?
  - id: getNewsletterVariantTranslation
    intent: Get a newsletter translation
    question: How do I see the German version of a newsletter without A/B tests?
  - id: updateNewsletterVariantTranslation
    intent: Update a newsletter translation
    question: How do I edit the Spanish translation of a newsletter that has no A/B test?
  - id: deleteNewsletterLanguageVariant
    intent: Delete a newsletter translation
    question: How do I remove a language from my newsletter?
  - id: getNewsletterTestGroups
    intent: List a newsletter's A/B test groups
    question: What A/B test groups does my newsletter have?
  phrasing_ops: 13
  slug: customer-io-newsletter-variants-api
- baseURL: https://track.customer.io
  baseurl_source: declared
  description: Objects are "groups" that you can relate people to in Customer.io—like the companies they work for, the online classes they take, and so on. These APIs help you find objects, their attributes, the peo
  name: Customer.io Objects API
  phrasing_intents:
  - id: getObjectTypes
    intent: List object types
    question: What object types, like companies or accounts, exist in my workspace?
  - id: getObjectsFilter
    intent: Find objects matching a filter
    question: How do I find all accounts whose plan attribute is enterprise?
  - id: getObjectRelationships
    intent: List people related to an object
    question: Which people belong to a given company or account object?
  - id: getObjectAttributes
    intent: Get an object's attributes
    question: What attributes are stored on a particular account object?
  phrasing_ops: 4
  slug: customer-io-objects-api
- baseURL: https://track.customer.io
  baseurl_source: declared
  description: The Opt-outs API from Customer.io — 2 operation(s) for opt-outs.
  name: Customer.io Opt Outs API
  phrasing_intents:
  - id: getOptouts
    intent: List opt-outs across the workspace
    question: Who has opted out of SMS or WhatsApp messages in my workspace?
  - id: getPersonOptouts
    intent: Get a person's opt-outs
    question: Which senders and channels has a person opted out of?
  - id: updatePersonOptouts
    intent: Opt a person out of or back into senders
    question: How do I opt someone out of WhatsApp messages from one sender?
  phrasing_ops: 3
  slug: customer-io-opt-outs-api
- baseURL: https://track.customer.io
  baseurl_source: declared
  description: Set up webhooks to inform an external service about Customer.io events. Webhooks can notify you immediately when immediately when customer attributes change or when people open your messages.
  name: Customer.io Reporting Webhooks API
  phrasing_intents:
  - id: createWebhook
    intent: Create a reporting webhook
    question: How do I get message events like opens and clicks sent to my own URL?
  - id: listWebhooks
    intent: List reporting webhooks
    question: What reporting webhooks are configured in my workspace?
  - id: getWebhook
    intent: Get a reporting webhook
    question: Which events does a particular reporting webhook send?
  - id: updateWebhook
    intent: Update a reporting webhook
    question: How do I change the URL a reporting webhook posts to?
  - id: deleteWebhook
    intent: Delete a reporting webhook
    question: How do I stop and remove a reporting webhook?
  phrasing_ops: 5
  slug: customer-io-reporting-webhooks-api
- baseURL: https://track.customer.io
  baseurl_source: declared
  description: Use these endpoints to send broadcasts or transactional messages to your audience. They use the same authentication method, but review the limits for both types of workflows to make sure you'll succes
  name: Customer.io Send Messages API
  phrasing_intents:
  - id: triggerBroadcast
    intent: Trigger an API-triggered broadcast
    question: How do I kick off an API-triggered broadcast with custom data?
  - id: sendNewsletter
    intent: Send a draft newsletter now
    question: How do I send a draft newsletter immediately?
  - id: scheduleNewsletter
    intent: Schedule a draft newsletter
    question: How do I schedule a newsletter to go out at a specific time?
  - id: sendEmail
    intent: Send a transactional email
    question: How do I send a password reset email to one person?
  - id: sendInApp
    intent: Send a transactional in-app message
    question: How do I show a one-off in-app message to a specific user?
  - id: sendInboxMessage
    intent: Send a transactional inbox message
    question: How do I deliver a notification to a user's in-app inbox?
  - id: sendPush
    intent: Send a transactional push notification
    question: How do I send a one-off push notification to a person's devices?
  - id: sendSMS
    intent: Send a transactional SMS
    question: How do I text a verification code to a phone number?
  phrasing_ops: 8
  slug: customer-io-send-messages-api
- baseURL: https://track.customer.io
  baseurl_source: declared
  description: 'A subscription center differentiates the types of messages available for your product. Your audience sets subscription preferences by name, but we record subscription preferences by topic ID. You can '
  name: Customer.io Subscription Center API
  phrasing_intents:
  - id: getTopics
    intent: List subscription topics
    question: What subscription topics can people opt into?
  - id: getSubscriptionCenterToken
    intent: Generate a subscription center link
    question: How do I give someone a link to manage their email preferences?
  - id: getChannels
    intent: List subscription channels
    question: Which channels, like email or SMS, can people subscribe to?
  phrasing_ops: 3
  slug: customer-io-subscription-center-api
- baseURL: https://track.customer.io
  baseurl_source: declared
  description: Add, modify, suppress, or unsuppress people (referred to as "customers" in our APIs). You can also use these endpoints to set attributes on people.
  name: Customer.io Track Customers API
  phrasing_intents:
  - id: identify
    intent: Add or update a person
    question: How do I create or update a person's profile with the Track API?
  - id: delete
    intent: Delete a person
    question: How do I delete a person and all their data?
  - id: add_device
    intent: Add or update a person's device
    question: How do I register an iOS or Android push token for a person?
  - id: delete_device
    intent: Remove a device from a person
    question: How do I remove an old device from a person's profile?
  - id: suppress
    intent: Suppress a person permanently
    question: How do I delete a person and block them from being re-added?
  - id: unsuppress
    intent: Unsuppress a person
    question: How do I allow a suppressed person to be added again?
  - id: unsubscribe
    intent: Unsubscribe a person from a delivery link
    question: How do I handle unsubscribes from my own custom unsubscribe page?
  - id: merge
    intent: Merge two duplicate people
    question: How do I merge two duplicate profiles into one?
  phrasing_ops: 8
  slug: customer-io-track-customers-api
- baseURL: https://track.customer.io
  baseurl_source: declared
  description: Use customer events to trigger campaigns or add users to segments. You can attribute events directly to customers or send anonymous events and associate them with users later when you identify them.
  name: Customer.io Track Events API
  phrasing_intents:
  - id: track
    intent: Track an event for an identified person
    question: How do I send an event for a person I've already identified?
  - id: trackAnonymous
    intent: Track an event for an anonymous visitor
    question: How do I record events for visitors who haven't signed up yet?
  - id: metrics
    intent: Report delivery metrics from any channel
    question: How do I report opens or clicks from a channel you don't natively support?
  - id: pushMetrics
    intent: Report push notification metrics (legacy)
    question: How do I report push opens with the older push events endpoint?
  phrasing_ops: 4
  slug: customer-io-track-events-api
- baseURL: https://track.customer.io
  baseurl_source: declared
  description: Manual segments are lists of people that you incorporate using the API or by uploading CSVs. You can add people to, or remove people from, manual segments with these endpoints. These endpoints do _not
  name: Customer.io Track Segments API
  phrasing_intents:
  - id: add_to_segment
    intent: Add people to a manual segment
    question: How do I add a list of people to a manual segment?
  - id: remove_from_segment
    intent: Remove people from a manual segment
    question: How do I take people out of a manual segment?
  phrasing_ops: 2
  slug: customer-io-track-segments-api
- baseURL: https://track.customer.io
  baseurl_source: declared
  description: 'This version of our edge API has only two endpoints, but supports the majority of our traditional v1 track operations and then some based on the `type` and `action` keys that you set in your request. '
  name: Customer.io Track V2 API
  phrasing_intents:
  - id: entity
    intent: Create, update or delete one person or object
    question: How do I update a single person or object with the v2 Track API?
  - id: batch
    intent: Send many person and object operations at once
    question: How do I send updates for lots of people and objects in one v2 request?
  phrasing_ops: 2
  slug: customer-io-track-v2-api
- baseURL: https://track.customer.io
  baseurl_source: declared
  description: Determine whether your account and data are hosted in the US or EU data center using your [Track API Key](https://fly.customer.io/settings/api_credentials).
  name: Customer.io Track Region API
  phrasing_intents:
  - id: getRegion
    intent: Find your account's data region
    question: Is my account in the US or EU region?
  phrasing_ops: 1
  slug: customer-io-trackregion-api
- baseURL: https://track.customer.io
  baseurl_source: declared
  description: An API to retrieve information about your workspaces in your account. You can use this to look up counts for messages sent, monthly billable emails sent, people, and objects.
  name: Customer.io Workspaces API
  phrasing_intents:
  - id: listWorkspaces
    intent: List workspaces in the account
    question: What workspaces are in my account?
  phrasing_ops: 1
  slug: customer-io-workspaces-api
- baseURL: https://track.customer.io
  baseurl_source: declared
  description: An automation, sometimes referred to as a campaign, is a workflow that people in your audience trigger and traverse. The items that happen within the workflow—messages, attribute changes, webhooks, et
  name: Customer.io Automations API
  slug: customer-io-automations-api
- baseURL: https://track.customer.io
  baseurl_source: declared
  description: Custom components are reusable blocks of content that you build once and reference from any email. Use these endpoints to list, create, update, and delete custom components. Updating a component throu
  name: Customer.io Components API
  slug: customer-io-components-api
- baseURL: https://track.customer.io
  baseurl_source: declared
  description: The Customer.io Journeys API Reference API from Customer.io — 0 operation(s) for customer.io journeys api reference.
  name: Customer.io Customer.io Journeys API Reference API
  slug: customer-io-customer-io-journeys-api-reference-api
- baseURL: https://track.customer.io
  baseurl_source: declared
  description: A Design Studio email doesn't send anything on its own. You [link](/integrations/api/design-studio/tag/email-email-link-and-publish/linkEmail/) it to a single workflow, like an email action in an auto
  name: Customer.io Email link and publish API
  slug: customer-io-email-link-and-publish-api
- baseURL: https://track.customer.io
  baseurl_source: declared
  description: Check an email before you publish or send it. - [Render](/integrations/api/design-studio/tag/email-testing/renderEmail/) returns the compiled HTML with liquid left intact. - [Preview](/integrations/ap
  name: Customer.io Email testing API
  slug: customer-io-email-testing-api
- baseURL: https://track.customer.io
  baseurl_source: declared
  description: Create and manage the emails you build in Design Studio, along with their translations and versions. - **Emails** hold the content, envelope details, and transformers for the default language. - **Tra
  name: Customer.io Emails API
  slug: customer-io-emails-api
- baseURL: https://track.customer.io
  baseurl_source: declared
  description: Folders organize your Design Studio files. Use these endpoints to list, create, rename, move, and delete folders. Folders hold emails, SMS, and components, but these endpoints return folders only; lis
  name: Customer.io Folders API
  slug: customer-io-folders-api
- baseURL: https://track.customer.io
  baseurl_source: declared
  description: Create and manage the SMS messages you write in Design Studio. These endpoints only work if your workspace writes SMS in Design Studio. Workspaces that set up SMS on or after July 30, 2026 do. If your
  name: Customer.io SMS API
  slug: customer-io-sms-api
- baseURL: https://track.customer.io
  baseurl_source: declared
  description: A Design Studio SMS doesn't send anything on its own. After you [create](/integrations/api/design-studio/tag/sms/createSms/) an SMS, you [link](/integrations/api/design-studio/tag/sms-link-and-publish
  name: Customer.io SMS link and publish API
  slug: customer-io-sms-link-and-publish-api
artifact_total: 136
asyncapis:
- description: Customer.io Reporting Webhooks send real-time message activity events as JSON payloads via HTTP POST to a configured endpoint. These events include message sends, deliveries, opens, clicks, bounces, u
  name: Customer.io Reporting Webhooks
  slug: customer-io-reporting-webhooks-asyncapi
collections:
- collection_type: open
  name: Customer.io App Activities API
  slug: open-customer-io-activities-api
- collection_type: open
  name: Customer.io App Activities Alias API
  slug: open-customer-io-alias-api
- collection_type: open
  name: Customer.io App API
  slug: open-customer-io-app-api
- collection_type: open
  name: Customer.io App Activities Batch API
  slug: open-customer-io-batch-api
- collection_type: open
  name: Customer.io App Activities Broadcasts API
  slug: open-customer-io-broadcasts-api
- collection_type: open
  name: Customer.io App Activities Campaigns API
  slug: open-customer-io-campaigns-api
- collection_type: open
  name: Customer.io App Activities Collections API
  slug: open-customer-io-collections-api
- collection_type: open
  name: Customer.io App Activities Customers API
  slug: open-customer-io-customers-api
- collection_type: open
  name: Customer.io App Activities Devices API
  slug: open-customer-io-devices-api
- collection_type: open
  name: Customer.io App Activities Entity API
  slug: open-customer-io-entity-api
- collection_type: open
  name: Customer.io App Activities Events API
  slug: open-customer-io-events-api
- collection_type: open
  name: Customer.io App Activities Exports API
  slug: open-customer-io-exports-api
- collection_type: open
  name: Customer.io App Activities Group API
  slug: open-customer-io-group-api
- collection_type: open
  name: Customer.io App Activities Identify API
  slug: open-customer-io-identify-api
- collection_type: open
  name: Customer.io App Activities Merge API
  slug: open-customer-io-merge-api
- collection_type: open
  name: Customer.io App Activities Messages API
  slug: open-customer-io-messages-api
- collection_type: open
  name: Customer.io App Activities Newsletters API
  slug: open-customer-io-newsletters-api
- collection_type: open
  name: Customer.io App Activities Page API
  slug: open-customer-io-page-api
- collection_type: open
  name: Customer.io Pipelines API
  slug: open-customer-io-pipelines-api
- collection_type: open
  name: Customer.io App Activities Screen API
  slug: open-customer-io-screen-api
- collection_type: open
  name: Customer.io App Activities Segments API
  slug: open-customer-io-segments-api
- collection_type: open
  name: Customer.io App Activities Sender Identities API
  slug: open-customer-io-sender-identities-api
- collection_type: open
  name: Customer.io App Activities Snippets API
  slug: open-customer-io-snippets-api
- collection_type: open
  name: Customer.io App Activities Track API
  slug: open-customer-io-track-api
- collection_type: open
  name: Customer.io App Activities Transactional API
  slug: open-customer-io-transactional-api
common:
- group: design
  href: https://artifacts.apis.io/customer-io/rules/customer-io-rules.yml
  title: ''
  type: Spectral
  url: rules/customer-io-rules.yml
- group: design
  href: https://artifacts.apis.io/customer-io/rules/customer-io-jsonschema-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/customer-io-jsonschema-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/customer-io/rules/customer-io-asyncapi-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/customer-io-asyncapi-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/customer-io/asyncapi/customer-io-reporting-webhooks-asyncapi.yml
  title: ''
  type: Webhooks
  url: asyncapi/customer-io-reporting-webhooks-asyncapi.yml
- group: operate
  href: https://artifacts.apis.io/customer-io/lifecycle/customer-io-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/customer-io-lifecycle.yml
- group: other
  href: https://artifacts.apis.io/customer-io/hosts/customer-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/customer-io-hosts.yml
- group: build
  href: https://artifacts.apis.io/customer-io/integrations/customer-io-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/customer-io-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/customer-io/vendors/customer-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/customer-io-vendors.yml
- group: other
  href: https://artifacts.apis.io/customer-io/capabilities/customer-io-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/customer-io-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/customer-io/overlays/customer-io-pipelines-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/customer-io-pipelines-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/customer-io/overlays/customer-io-reporting-webhooks-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/customer-io-reporting-webhooks-overlay.yaml
- group: commercial
  href: https://artifacts.apis.io/customer-io/plans/customer-io-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/customer-io-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/customer-io/rate-limits/customer-io-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/customer-io-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/customer-io/finops/customer-io-finops.yml
  title: ''
  type: FinOps
  url: finops/customer-io-finops.yml
- group: agent
  href: https://artifacts.apis.io/customer-io/agentic-access/customer-io-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/customer-io-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/customer-io/security/customer-io-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/customer-io-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/customer-io/security/customer-io-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/customer-io-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/customer-io/security/customer-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/customer-io-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/customer-io/authentication/customer-io-authentication.yml
  title: ''
  type: Authentication
  url: authentication/customer-io-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/customerio
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/customer-io
- group: company
  title: ''
  type: Website
  url: https://customer.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.customer.io
- group: docs
  href: https://artifacts.apis.io/customer-io/asyncapi/customer-io-reporting-webhooks-asyncapi.yml
  title: ''
  type: AsyncAPI
  url: asyncapi/customer-io-reporting-webhooks-asyncapi.yml
- group: docs
  href: https://artifacts.apis.io/customer-io/json-schema/customer-io-customer-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/customer-io-customer-schema.json
- group: docs
  href: https://artifacts.apis.io/customer-io/json-schema/customer-io-event-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/customer-io-event-schema.json
- group: docs
  href: https://artifacts.apis.io/customer-io/json-schema/customer-io-webhook-payload-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/customer-io-webhook-payload-schema.json
- group: design
  href: https://artifacts.apis.io/customer-io/json-ld/customer-io-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/customer-io-context.jsonld
- group: design
  href: https://artifacts.apis.io/customer-io/vocabulary/customer-io-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/customer-io-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/customer-io/rules/customer-io-rules.yml
  title: ''
  type: Rules
  url: rules/customer-io-rules.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.customer.io/llms.txt
- group: build
  href: https://artifacts.apis.io/customer-io/packages/customer-io-packages.yml
  title: ''
  type: Packages
  url: packages/customer-io-packages.yml
- group: build
  href: https://artifacts.apis.io/customer-io/packages/customer-io-packages.yml
  title: ''
  type: SDKs
  url: packages/customer-io-packages.yml
- group: build
  href: https://artifacts.apis.io/customer-io/cli/customer-io-cli.yml
  title: ''
  type: CLI
  url: cli/customer-io-cli.yml
- group: agent
  href: https://artifacts.apis.io/customer-io/mcp/customer-io-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/customer-io-mcp.yml
- group: build
  href: https://artifacts.apis.io/customer-io/mcp/customer-io-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/customer-io-tool-crosswalk.yml
- group: other
  href: https://artifacts.apis.io/customer-io/a2a/customer-io-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/customer-io-a2a.yml
- group: agent
  href: https://artifacts.apis.io/customer-io/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/customer-io/well-known/customer-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/customer-io-well-known.yml
- group: agent
  href: https://artifacts.apis.io/customer-io/llms/customer-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/customer-io-llms.txt
- group: auth
  href: https://artifacts.apis.io/customer-io/scopes/customer-io-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/customer-io-scopes.yml
- group: design
  href: https://artifacts.apis.io/customer-io/conventions/customer-io-conventions.yml
  title: ''
  type: Conventions
  url: conventions/customer-io-conventions.yml
- group: design
  href: https://artifacts.apis.io/customer-io/errors/customer-io-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/customer-io-problem-types.yml
- group: design
  href: https://artifacts.apis.io/customer-io/lifecycle/customer-io-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/customer-io-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.customerio.com
- group: operate
  href: https://artifacts.apis.io/customer-io/changelog/customer-io-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/customer-io-changelog.yml
- group: design
  href: https://artifacts.apis.io/customer-io/conformance/customer-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/customer-io-conformance.yml
- group: auth
  href: https://artifacts.apis.io/customer-io/conformance/customer-io-conformance.yml
  title: ''
  type: Compliance
  url: conformance/customer-io-conformance.yml
- group: auth
  title: ''
  type: Security
  url: https://customer.io/legal/reporting-vulnerability
- group: design
  href: https://artifacts.apis.io/customer-io/data-model/customer-io-data-model.yml
  title: ''
  type: DataModel
  url: data-model/customer-io-data-model.yml
- group: start
  href: https://artifacts.apis.io/customer-io/sandbox/customer-io-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/customer-io-sandbox.yml
- group: design
  href: https://artifacts.apis.io/customer-io/openapi/_original/customer-io-reporting-webhooks-openapi.json
  title: ''
  type: Webhooks
  url: openapi/_original/customer-io-reporting-webhooks-openapi.json
- group: other
  href: https://artifacts.apis.io/customer-io/overlays/customer-io-app-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/customer-io-app-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/customer-io/well-known/customer-io-api-catalog.json
  title: ''
  type: APICatalog
  url: well-known/customer-io-api-catalog.json
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.customer.io/integrations/api/customerio-apis/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.customer.io/integrations/api/customerio-apis/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.customer.io/get-started/
- group: operate
  title: ''
  type: Support
  url: https://customer.io/contact
- group: company
  title: ''
  type: Blog
  url: https://customer.io/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://customer.io/pricing
- group: start
  title: ''
  type: SignUp
  url: https://fly.customer.io/signup
- group: start
  title: ''
  type: Login
  url: https://fly.customer.io/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://customer.io/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://customer.io/legal/privacy-policy
- group: learn
  title: ''
  type: Academy
  url: https://academy.customer.io/pages/get-started
- group: operate
  title: ''
  type: Contact
  url: mailto:press@customer.io
created: '2024-01-01'
description: Customer.io is a customer engagement platform that combines a customer data platform, marketing automation, and messaging delivery to send behavior-triggered email, push, SMS, and in-app messages. Its API surface includes the Track API for sending behavioral data and customer profile updates, the App API for managing workspace resources and sending transactional and broadcast messages, the Pipelines API which is a Segment-spec data ingestion interface, and outbound reporting webhooks that deliver message lifecycle events.
finops:
- has_sources: true
  method: derived
  name: Customer Io Finops
  primary_unit: subscription
  service_category: ''
  slug: customer-io-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/customer-io.png
json_schemas:
- name: activityObject
  property_count: 10
  slug: customer-io-activity-object
- name: alias
  property_count: 3
  slug: customer-io-alias
- name: anonymousEventsRequest
  property_count: 0
  slug: customer-io-anonymous-events-request
- name: anonymous_id
  property_count: 0
  slug: customer-io-anonymous-id
- name: batch
  property_count: 3
  slug: customer-io-batch
- name: campaignObject
  property_count: 0
  slug: customer-io-campaign-object
- name: campaignRequest
  property_count: 0
  slug: customer-io-campaign-request
- name: cio_id
  property_count: 0
  slug: customer-io-cio-id
- name: Email
  property_count: 16
  slug: customer-io-create-email-newsletter
- name: In-App
  property_count: 10
  slug: customer-io-create-in-app-newsletter
- name: Inbox message
  property_count: 10
  slug: customer-io-create-inbox-newsletter
- name: Push
  property_count: 11
  slug: customer-io-create-push-newsletter
- name: SMS
  property_count: 10
  slug: customer-io-create-sms-newsletter
- name: Webhook
  property_count: 12
  slug: customer-io-create-webhook-newsletter
- name: customer_id
  property_count: 0
  slug: customer-io-customer-id
- name: Customer.io Customer
  property_count: 8
  slug: customer-io-customer
- name: 'Delivery: Event'
  property_count: 5
  slug: customer-io-delivery-operations
- name: device_object
  property_count: 4
  slug: customer-io-device-object
- name: email_address
  property_count: 0
  slug: customer-io-email-address
- name: Customer.io Event
  property_count: 7
  slug: customer-io-event
- name: eventsRequest
  property_count: 0
  slug: customer-io-events-request
- name: group
  property_count: 0
  slug: customer-io-group
- name: 'Person: Identify'
  property_count: 6
  slug: customer-io-identify-person
- name: identify
  property_count: 0
  slug: customer-io-identify
- name: newsletterObject
  property_count: 18
  slug: customer-io-newsletter-object
- name: not_nullable_customer_id
  property_count: 0
  slug: customer-io-not-nullable-customer-id
- name: not_nullable_email_address
  property_count: 0
  slug: customer-io-not-nullable-email-address
- name: page
  property_count: 0
  slug: customer-io-page
- name: 'Person: Event'
  property_count: 7
  slug: customer-io-person-event
- name: 'Person: Merge'
  property_count: 4
  slug: customer-io-person-merge
- name: 'Person: Page view'
  property_count: 7
  slug: customer-io-person-page
- name: 'Person: Screen view'
  property_count: 7
  slug: customer-io-person-screen
- name: screen
  property_count: 0
  slug: customer-io-screen
- name: track-metrics
  property_count: 2
  slug: customer-io-track-metrics
- name: track
  property_count: 0
  slug: customer-io-track
- name: Transformers
  property_count: 8
  slug: customer-io-transformers
- name: Email
  property_count: 10
  slug: customer-io-update-email-content
- name: Inbox message
  property_count: 3
  slug: customer-io-update-inbox-content
- name: Push
  property_count: 4
  slug: customer-io-update-push-content
- name: SMS
  property_count: 3
  slug: customer-io-update-sms-content
- name: Webhook
  property_count: 4
  slug: customer-io-update-webhook-content
- name: v1_cio_relationships
  property_count: 2
  slug: customer-io-v1-cio-relationships
- name: Customer.io Reporting Webhook Payload
  property_count: 4
  slug: customer-io-webhook-payload
jsonld:
- class_count: 0
  name: Customer Io Context
  property_count: 11
  slug: customer-io-context
layout: provider
mcp_servers:
- description: 'Customer.io operates a first-party, hosted Model Context Protocol server that exposes the full Journeys App API and the CDP Data Pipelines API to any MCP client. It is a remote HTTP endpoint an agent '
  name: Customer.io MCP
  slug: customer-io-mcp
modified: '2026-09-16'
name: Customer.io
nav: Providers
network: true
overview: 'Customer.io publishes 48 API contracts indexed on the [APIs.io](https://apis.io/) network, including Track API, Activities API, Alias API, and 45 more. Tagged areas include Behavioral Data, Broadcast, Campaigns, CDP, and Customer Data.


  The Customer.io catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 3 Spectral governance rulesets.


  Customer.io''s developer surface includes authentication, documentation, CLI, changelog, sandbox, API reference, getting-started guide, and 59 more developer resources.'
plans:
- name: Customer Io Plans Pricing
  plan_count: 3
  slug: customer-io-plans-pricing
- name: Customer Io Price Estimates
  plan_count: 0
  slug: customer-io-price-estimates
random_paper: 15
rate_limits:
- limit_count: 4
  name: Customer Io Rate Limits
  slug: customer-io-rate-limits
rules:
- authorship: generated
  effective_rule_count: 35
  extends:
  - spectral:asyncapi
  name: Customer.io — asyncapi rules
  rule_count: 8
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 7
  slug: customer-io-asyncapi-spectral-rules
- authorship: generated
  effective_rule_count: 6
  extends: []
  name: Customer.io — jsonschema rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: customer-io-jsonschema-spectral-rules
- authorship: unmarked
  effective_rule_count: 47
  extends:
  - spectral:oas
  name: Customer.io API Rules
  rule_count: 6
  severity_counts:
    error: 3
    hint: 0
    info: 0
    warn: 3
  slug: customer-io-rules
scopes:
- name: Customer Io Scopes
  scope_count: 5
  slug: customer-io-scopes
  summary_line: 5 scopes
score:
  band: exemplar
  composite: 86.9
  coverage:
    artifact_dirs: 39
    catalog_earned: 89.8
    catalog_earned_first_party: 24.0
    catalog_gap: 25.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.2
  facets:
    access_clarity: 93.4
    contract_governance: 35.6
    contract_quality: 75.8
    developer_ergonomics: 80.4
    discoverability: 80.0
    operational_transparency: 92.1
  previous_composite: 85.7
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 88.2
      total: 51
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 44.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 61.1
screenshot: https://apis.io/screenshots/customer-io/customer-io-2026-06-20T175348.png
security:
- kind: authentication
  name: Customer Io Authentication
  slug: customer-io-authentication
  summary_line: http/oauth2 · 5 schemes
- kind: domain-security
  name: Customer Io Domain Security
  slug: customer-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Customer Io Vulnerability Disclosure
  slug: customer-io-vulnerability-disclosure
  summary_line: no policy recorded
- kind: trust-center
  name: Customer Io Trust Center
  slug: customer-io-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, GDPR
skill_count: 4
skills:
- name: customer-io-consume-reporting-webhooks
  slug: customer-io-consume-reporting-webhooks
- name: customer-io-ingest-people-and-events
  slug: customer-io-ingest-people-and-events
- name: customer-io-send-transactional-email
  slug: customer-io-send-transactional-email
- name: customer-io-trigger-broadcast
  slug: customer-io-trigger-broadcast
slug: customer-io
tags:
- Behavioral Data
- Broadcast
- Campaigns
- CDP
- Customer Data
- Customer Data Platform
- Data Ingestion
- Email
- Event Tracking
- Marketing Automation
- Messaging
- Push Notifications
- Segments
- SMS
- Transactional Email
- A2A
website: https://customer.io
---
