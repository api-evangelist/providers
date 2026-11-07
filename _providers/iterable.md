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
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
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
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: mostly
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 34.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 121
  human_in_the_loop: 1
  name: Iterable Agentic Access
  operation_count: 192
  slug: iterable-agentic-access
  summary_line: 192 operations · 121 acting · 1 human-in-the-loop
api_count: 2
apis:
- baseURL: https://api.iterable.com
  baseurl_source: declared
  description: The Iterable Export API enables developers to extract data from Iterable projects for analytics, reporting, and data warehousing purposes. It provides asynchronous export endpoints that allow bulk ret
  name: Iterable Export API
  phrasing_intents:
  - id: exportDataCsv
    intent: Export analytics data as CSV
    question: Can I download email sends or opens as a CSV for a date range?
  - id: exportDataJson
    intent: Export analytics data as JSON lines
    question: Can I export analytics data as JSON, one record per line?
  - id: getExportJobs
    intent: List recent export jobs
    question: Which export jobs have I run recently in this project?
  - id: startExport
    intent: Start a background data export
    question: How do I kick off a large export that runs in the background?
  - id: exportUserEvents
    intent: Export all events for one user
    question: Can I export every event for a single user, including custom events?
  - id: cancelExport
    intent: Cancel an export job
    question: Can I stop a queued or running export job?
  - id: getExportFiles
    intent: Get an export job's status and files
    question: How do I check whether my export job is done and get its files?
  phrasing_ops: 7
  slug: export-api
- description: The Iterable Web SDK enables developers to integrate Iterable's marketing automation capabilities directly into JavaScript and Node.js applications. It provides functions for tracking user events, man
  name: Iterable Web SDK
  slug: web-sdk
- description: The Iterable iOS SDK allows developers to integrate Iterable's marketing automation features into native iOS applications built with Swift or Objective-C. It supports push notifications, in-app messag
  name: Iterable iOS SDK
  slug: ios-sdk
- description: The Iterable Android SDK provides native integration between Android applications and the Iterable marketing automation platform. It supports push notifications, in-app messages, deep links, and Mobil
  name: Iterable Android SDK
  slug: android-sdk
- description: The Iterable React Native SDK enables developers to integrate Iterable's marketing automation capabilities into cross-platform mobile applications built with React Native. It wraps Iterable's native i
  name: Iterable React Native SDK
  slug: react-native-sdk
- baseURL: https://api.iterable.com
  baseurl_source: declared
  description: Create, retrieve, and manage marketing campaigns. Access campaign metrics and trigger campaign sends.
  name: Iterable Campaigns API
  phrasing_intents:
  - id: campaigns
    intent: Page through campaign metadata by state
    question: Can I page through all my campaigns and filter them by campaign state?
  - id: abortCampaign
    intent: Abort a running campaign
    question: How do I stop a blast campaign that is already sending?
  - id: activateTriggeredCampaign
    intent: Activate a triggered campaign
    question: Can I turn on a triggered campaign through the API?
  - id: archiveCampaigns
    intent: Archive one or more campaigns
    question: Can I archive several campaigns at once, like the archive button in the UI?
  - id: cancelCampaign
    intent: Cancel a scheduled or recurring campaign
    question: How do I cancel a campaign that is scheduled but hasn't sent yet?
  - id: createCampaign
    intent: Create a blast or triggered campaign from a template
    question: Can I create a campaign with labels, a send mode and a default time zone via the API?
  - id: DeactivateTriggeredCampaign
    intent: Deactivate a triggered campaign
    question: Can I pause a triggered campaign without archiving it?
  - id: metrics
    intent: Get metrics for campaigns in a date window
    question: What is the rate limit when pulling campaign metrics from the /api/campaigns endpoint?
  phrasing_ops: 16
  slug: iterable-campaigns-api
- baseURL: https://api.iterable.com
  baseurl_source: declared
  description: Manage product catalogs and catalog items used for personalization and recommendation in campaigns.
  name: Iterable Catalogs API
  phrasing_intents:
  - id: listCatalogs
    intent: List catalog names
    question: What catalogs exist in my Iterable project?
  - id: deleteCatalog
    intent: Delete a catalog and its collections
    question: Does deleting a catalog also remove the collections that reference it?
  - id: createCatalog
    intent: Create a new catalog
    question: How do I create a catalog for product data?
  - id: getFieldMappings
    intent: Get a catalog's field data types
    question: Which data types are mapped to the fields in my catalog?
  - id: updateFieldTypes
    intent: Set data types for catalog fields
    question: Can I change a catalog field's data type after it has been set?
  - id: bulkDeleteCatalogItems
    intent: Bulk delete catalog items
    question: Can I delete many catalog items at once by their IDs?
  - id: listCatalogItems
    intent: List catalog items with sorting
    question: Can I sort the items in a catalog by a field, ascending or descending?
  - id: bulkUpdateCatalogItems
    intent: Bulk create catalog items
    question: How many catalog items can I create in one request?
  phrasing_ops: 17
  slug: iterable-catalogs-api
- baseURL: https://api.iterable.com
  baseurl_source: declared
  description: Retrieve and manage messaging channels and message types used for organizing campaigns and templates.
  name: Iterable Channels API
  phrasing_intents:
  - id: channels
    intent: List message channels
    question: What message channels are set up in my project?
  - id: listChannels
    intent: List channels via the simple endpoint
    question: Which channels group my campaign templates, from the plain /channels path?
  phrasing_ops: 2
  slug: iterable-channels-api
- baseURL: https://api.iterable.com
  baseurl_source: declared
  description: Track purchase events, update cart data, and manage commerce-related user activity for revenue attribution.
  name: Iterable Commerce API
  phrasing_intents:
  - id: trackPurchase
    intent: Track a purchase and clear the cart
    question: Does tracking a purchase clear the user's shopping cart items?
  - id: updateCart
    intent: Replace a user's shopping cart items
    question: How do I update shoppingCartItems on a user profile?
  - id: postCommerceTrackPurchase
    intent: Track a purchase for revenue attribution
    question: Can I log a purchase for revenue attribution using the simple /commerce endpoint?
  - id: postCommerceUpdateCart
    intent: Update a cart for abandoned-cart campaigns
    question: How can I feed cart contents into abandoned cart campaigns?
  phrasing_ops: 4
  slug: iterable-commerce-api
- baseURL: https://api.iterable.com
  baseurl_source: declared
  description: Send transactional emails and manage email-specific delivery settings.
  name: Iterable Email API
  phrasing_intents:
  - id: cancel
    intent: Cancel a scheduled email to a user
    question: Can I cancel an email that's scheduled for a specific user?
  - id: target
    intent: Send a campaign email to an address
    question: How do I send an email to one address from an existing campaign?
  - id: viewInBrowser
    intent: View a previously sent email
    question: Can I see exactly how a sent email rendered for a user?
  - id: sendTransactionalEmail
    intent: Send a transactional email with attachments
    question: Can I attach files to a transactional email?
  phrasing_ops: 4
  slug: iterable-email-api
- baseURL: https://api.iterable.com
  baseurl_source: declared
  description: Track custom events, retrieve event data for users, and manage event metadata used for segmentation and campaign triggering.
  name: Iterable Events API
  phrasing_intents:
  - id: embedded-track-click
    intent: Track a click on an embedded message
    question: How do I record that a user clicked a button in an embedded message?
  - id: embedded-track-received
    intent: Track an embedded message received
    question: Can I log that an embedded message arrived on a user's device?
  - id: embedded-track-impression
    intent: Track an embedded session and impressions
    question: How do I report how long a user viewed embedded messages in a session?
  - id: UserEventsByUserId
    intent: Get a user's events by userId
    question: Can I pull the event history for a user identified by userId?
  - id: inAppConsume
    intent: Consume or delete an in-app message
    question: How do I remove an in-app message from a user's inbox without the mobile SDK?
  - id: track
    intent: Track a custom event
    question: Can I track a custom event and create new fields on the fly under /api/events?
  - id: trackBulk
    intent: Track many custom events at once
    question: Can I send a batch of events in one /api/events call?
  - id: trackInAppClick
    intent: Track an in-app message click
    question: How do I log a tap on a link inside an in-app message?
  phrasing_ops: 17
  slug: iterable-events-api
- baseURL: https://api.iterable.com
  baseurl_source: declared
  description: Retrieve experiment configurations and metrics for A/B tests running across campaigns.
  name: Iterable Experiments API
  phrasing_intents:
  - id: metrics
    intent: Get email experiment metrics by date range
    question: Can I export A/B test metrics for an experiment within a date range?
  - id: list
    intent: List experiments
    question: Which experiments are running for a given campaign?
  - id: get
    intent: Get one experiment
    question: How do I look up a single A/B experiment by its ID?
  - id: variants
    intent: List an experiment's variants
    question: What variants are being tested in my experiment?
  - id: getExperimentMetrics
    intent: Get A/B test metrics for many experiments
    question: How many experiment and campaign IDs can I query for metrics at once?
  phrasing_ops: 5
  slug: iterable-experiments-api
- baseURL: https://api.iterable.com
  baseurl_source: declared
  description: Create and manage subscriber lists. Subscribe and unsubscribe users from lists. Retrieve list metadata and membership.
  name: Iterable Lists API
  phrasing_intents:
  - id: getLists
    intent: List all lists in the project
    question: What lists do I have in my /api project, and what's the rate limit?
  - id: create
    intent: Create a static list with a description
    question: Can I create a static list and give it a description?
  - id: getUsers
    intent: Get all users in a list
    question: Can I export every member of a list?
  - id: getUsersPreview
    intent: Preview a random sample of list users
    question: Can I see a random sample of users in a list rather than all of them?
  - id: subscribe
    intent: Add subscribers to a list
    question: How do I add specific people to a list under /api/lists?
  - id: unsubscribe
    intent: Remove users from a list
    question: Can I remove users from a list and also unsubscribe them from the channel?
  - id: delete
    intent: Delete a list
    question: How do I delete a list I no longer need?
  - id: getListCount
    intent: Count users in a list
    question: How many users are on this list?
  phrasing_ops: 12
  slug: iterable-lists-api
- baseURL: https://api.iterable.com
  baseurl_source: declared
  description: Store and retrieve key-value metadata tables for use in personalization and campaign logic.
  name: Iterable Metadata API
  phrasing_intents:
  - id: listTables
    intent: List metadata tables
    question: What metadata tables exist in my project?
  - id: delete
    intent: Delete a metadata table asynchronously
    question: Is a metadata table deleted immediately or processed later?
  - id: list
    intent: List keys in a metadata table with paging
    question: Can I page through the keys of a metadata table with a marker?
  - id: deleteApiMetadataByTableByKey
    intent: Delete one metadata key asynchronously
    question: Can I delete just one key from a metadata table without dropping the table?
  - id: get
    intent: Get one metadata key's value
    question: How do I read the value stored under a key in a metadata table?
  - id: put
    intent: Create or replace a metadata value
    question: Can I overwrite the value of a key in a metadata table?
  - id: getMetadataTable
    intent: Get all keys in a table (simple)
    question: Is there a plain /metadata endpoint that returns every key in a table?
  - id: deleteMetadataTable
    intent: Delete a metadata table and entries (simple)
    question: Can I delete a metadata table and all its entries via the plain /metadata path?
  phrasing_ops: 11
  slug: iterable-metadata-api
- baseURL: https://api.iterable.com
  baseurl_source: declared
  description: Send push notifications and manage push notification delivery settings and tokens.
  name: Iterable Push API
  phrasing_intents:
  - id: cancel
    intent: Cancel a push notification to a user
    question: Can I cancel a push notification scheduled for one user?
  - id: target
    intent: Send a campaign push to a user
    question: Can I schedule a push to one user and attach metadata?
  - id: sendPushNotification
    intent: Send a push via the simple endpoint
    question: Is there a plain /push/target call that sends a templated push by email?
  phrasing_ops: 3
  slug: iterable-push-api
- baseURL: https://api.iterable.com
  baseurl_source: declared
  description: Send SMS messages and manage SMS-specific delivery settings.
  name: Iterable SMS API
  phrasing_intents:
  - id: cancel
    intent: Cancel an SMS to a user
    question: Can I cancel a text message scheduled for one user?
  - id: target
    intent: Send a campaign SMS to a user
    question: Can I send a transactional text to one user and schedule it?
  - id: sendSms
    intent: Send an SMS via the simple endpoint
    question: Is there a plain /sms/target call that sends a templated text by email?
  phrasing_ops: 3
  slug: iterable-sms-api
- baseURL: https://api.iterable.com
  baseurl_source: declared
  description: Manage email, push, SMS, and in-app message templates. Retrieve template content and metadata.
  name: Iterable Templates API
  phrasing_intents:
  - id: getTemplates
    intent: List project templates with filters
    question: Can I list only my SMS templates, or only blast templates?
  - id: bulkDeleteTemplates
    intent: Bulk delete base templates
    question: Can I delete several templates at once?
  - id: getEmailTemplate
    intent: Get an email template in a locale
    question: Can I fetch the Spanish version of an email template?
  - id: previewEmailTemplate
    intent: Render an email template preview with custom data
    question: Can I see the rendered HTML of an email template with sample data before sending?
  - id: emailProof
    intent: Send an email template proof
    question: How do I send myself a test email of a template?
  - id: updateEmailTemplate
    intent: Update an email template's full settings
    question: Can I change an email template's CC, BCC and reply-to addresses?
  - id: upsertEmailTemplate
    intent: Create or update an email template by client ID
    question: How do I create an email template that updates if it already exists?
  - id: getEmbeddedTemplate
    intent: Get an embedded message template
    question: Can I fetch an embedded message template by ID?
  phrasing_ops: 29
  slug: iterable-templates-api
- baseURL: https://api.iterable.com
  baseurl_source: declared
  description: Manage user profiles, update user fields, bulk update users, get user data by email or userId, and delete users.
  name: Iterable Users API
  phrasing_intents:
  - id: InvalidateJWT
    intent: Invalidate a user's JWTs
    question: How do I revoke all JWTs issued to a user, say after a password reset?
  - id: bulkUpdateUser
    intent: Bulk update user profiles under /api
    question: Can I update many user profiles in one /api request without wiping omitted fields?
  - id: bulkUpdateSubscriptions
    intent: Bulk overwrite user subscriptions
    question: Can I update subscription preferences for many users at once?
  - id: getUserById
    intent: Get a user by userId as a query parameter
    question: Can I look up a user whose userId has slashes by passing it as a query parameter?
  - id: delete
    intent: Delete a user by userId
    question: Does deleting a user by userId stop future data collection about them?
  - id: getApiUsersByUserIdByUserId
    intent: Get a user by userId in the path
    question: How do I fetch a user's profile by userId with the userId in the /api URL path?
  - id: disableDevice
    intent: Disable push to a mobile device
    question: How do I stop push notifications to one of a user's devices?
  - id: forget
    intent: Forget a user for GDPR
    question: How do I honor a GDPR erasure request and stop collecting a user's data?
  phrasing_ops: 30
  slug: iterable-users-api
- baseURL: https://api.iterable.com
  baseurl_source: declared
  description: Trigger workflow enrollments and manage journey-based automation workflows.
  name: Iterable Workflows API
  phrasing_intents:
  - id: getJourneys
    intent: List journeys
    question: What journeys exist in my project?
  - id: triggerWorkflow
    intent: Trigger a journey for a user or list
    question: How do I start a journey for one user under /api/workflows?
  - id: postWorkflowsTriggerWorkflow
    intent: Enroll users in a workflow (simple)
    question: Is there a plain /workflows/triggerWorkflow call to enroll users in an activated workflow?
  phrasing_ops: 3
  slug: iterable-workflows-api
- baseURL: https://api.iterable.com
  baseurl_source: declared
  description: The Embedded Messaging API from Iterable — 1 operation(s) for embedded messaging.
  name: Iterable Embedded Messaging API
  phrasing_intents:
  - id: messages
    intent: Get a user's eligible embedded messages
    question: Which embedded messages is a user eligible to see, grouped by placement?
  phrasing_ops: 1
  slug: iterable-embedded-messaging-api
- baseURL: https://api.iterable.com
  baseurl_source: declared
  description: The In-app API from Iterable — 4 operation(s) for in-app.
  name: Iterable In App API
  phrasing_intents:
  - id: cancel
    intent: Cancel a scheduled in-app message
    question: Can I cancel an in-app message that's scheduled for one user?
  - id: getMessages
    intent: Get a user's mobile in-app messages
    question: How do I fetch a user's pending in-app messages including app-specific ones?
  - id: getPriorityMessage
    intent: Get a user's most relevant in-app message
    question: Which single in-app message should I show this user first?
  - id: target
    intent: Send an in-app notification to a user
    question: How do I send an in-app notification to one user from a campaign?
  - id: getInAppMessages
    intent: Get pending in-app messages for a user
    question: What in-app messages are waiting to be shown to a user?
  phrasing_ops: 5
  slug: iterable-in-app-api
- baseURL: https://api.iterable.com
  baseurl_source: declared
  description: The In-app-web API from Iterable — 1 operation(s) for in-app-web.
  name: Iterable In App Web API
  phrasing_intents:
  - id: getMessages
    intent: Get a user's web in-app messages
    question: How do I fetch in-app messages to show on my website for a user?
  phrasing_ops: 1
  slug: iterable-in-app-web-api
- baseURL: https://api.iterable.com
  baseurl_source: declared
  description: The snippets API from Iterable — 2 operation(s) for snippets.
  name: Iterable Snippets API
  phrasing_intents:
  - id: getSnippets
    intent: List all snippets
    question: What reusable snippets exist in my project?
  - id: createSnippet
    intent: Create a new snippet
    question: How do I create a reusable content snippet for templates?
  - id: deleteSnippet
    intent: Delete a snippet
    question: How do I delete a snippet I no longer use?
  - id: getSnippet
    intent: Get a snippet by ID or name
    question: Can I look up a snippet by its name instead of its numeric ID?
  - id: updateSnippet
    intent: Create or update a snippet by ID or name
    question: Will updating a snippet by name create it if it doesn't exist?
  phrasing_ops: 5
  slug: iterable-snippets-api
- baseURL: https://api.iterable.com
  baseurl_source: declared
  description: The subscriptions API from Iterable — 4 operation(s) for subscriptions.
  name: Iterable Subscriptions API
  phrasing_intents:
  - id: subscribeSingleUserToDoubleOptIn
    intent: Start a double opt-in subscription
    question: How do I send a double opt-in confirmation before subscribing someone?
  - id: BulkSubscriptionAction
    intent: Subscribe or unsubscribe many users to a group
    question: Can I subscribe a batch of users to a subscription group in one call?
  - id: unsubscribeSingleUserByUserId
    intent: Unsubscribe one user by userId
    question: Can I unsubscribe a single userId from a subscription group?
  - id: subscribeSingleUserByUserId
    intent: Subscribe one user by userId
    question: How do I subscribe one userId to a message type or list?
  - id: unsubscribeSingleUser
    intent: Unsubscribe one user by email
    question: Can I unsubscribe one email address from a subscription group?
  - id: subscribeSingleUser
    intent: Subscribe one user by email
    question: How do I subscribe one email address to a list or message type?
  phrasing_ops: 6
  slug: iterable-subscriptions-api
- baseURL: https://api.iterable.com
  baseurl_source: declared
  description: The Verify API from Iterable — 2 operation(s) for verify.
  name: Iterable Verify API
  phrasing_intents:
  - id: beginSmsVerification
    intent: Send an SMS verification code
    question: How do I text a verification code to a phone number?
  - id: checkSmsVerification
    intent: Check an SMS verification code
    question: Is the code the user typed the right one for their phone?
  phrasing_ops: 2
  slug: iterable-verify-api
- baseURL: https://api.iterable.com
  baseurl_source: declared
  description: The webhooks API from Iterable — 1 operation(s) for webhooks.
  name: Iterable Webhooks API
  phrasing_intents:
  - id: getWebhooks
    intent: List webhooks
    question: What webhooks are configured in my project?
  - id: updateWebhook
    intent: Update a webhook
    question: Can I change a webhook's endpoint URL or disable it?
  phrasing_ops: 2
  slug: iterable-webhooks-api
- baseURL: https://api.iterable.com
  baseurl_source: declared
  description: The Message types API from Iterable — 2 operation(s) for message types.
  name: Iterable Message types API
  phrasing_intents:
  - id: messageTypes
    intent: List message types
    question: What message types exist in my project under /api?
  - id: listMessageTypes
    intent: List message types via the simple endpoint
    question: Which message types categorize my sends, from the plain /messageTypes path?
  phrasing_ops: 2
  slug: iterable-message-types-api
- baseURL: https://api.iterable.com
  baseurl_source: declared
  description: The Web Push API from Iterable — 3 operation(s) for web push.
  name: Iterable Web Push API
  phrasing_intents:
  - id: cancel
    intent: Cancel a web push to a user
    question: Can I cancel a browser push scheduled for one user?
  - id: target
    intent: Send a campaign web push to a user
    question: Can I schedule a browser push to one user for later?
  - id: sendWebPush
    intent: Send a web push via the simple endpoint
    question: Is there a plain /webPush/target call that sends a templated browser push by email?
  phrasing_ops: 3
  slug: iterable-web-push-api
- baseURL: https://api.iterable.com
  baseurl_source: declared
  description: The Whats App API from Iterable — 2 operation(s) for whats app.
  name: Iterable Whats App API
  phrasing_intents:
  - id: cancel
    intent: Cancel a scheduled WhatsApp message
    question: Can I cancel a WhatsApp message scheduled for one user?
  - id: target
    intent: Send a WhatsApp message to a user
    question: How do I send a WhatsApp message to one user from a campaign?
  phrasing_ops: 2
  slug: iterable-whats-app-api
artifact_total: 118
asyncapis:
- description: Iterable system webhooks send real-time event data from an Iterable project to external systems via HTTP POST requests whenever specified events occur. System webhooks can be configured to fire on ema
  name: Iterable System Webhooks
  slug: iterable-system-webhooks-asyncapi
collections:
- collection_type: postman
  name: Iterable Export Campaigns API
  slug: postman-iterable-campaigns-api
- collection_type: postman
  name: Iterable Export Campaigns Catalogs API
  slug: postman-iterable-catalogs-api
- collection_type: postman
  name: Iterable Export Campaigns Channels API
  slug: postman-iterable-channels-api
- collection_type: postman
  name: Iterable Export Campaigns Commerce API
  slug: postman-iterable-commerce-api
- collection_type: postman
  name: Iterable Export Campaigns Email API
  slug: postman-iterable-email-api
- collection_type: postman
  name: Iterable Export Campaigns Events API
  slug: postman-iterable-events-api
- collection_type: postman
  name: Iterable Export Campaigns ExperimentMetrics API
  slug: postman-iterable-experimentmetrics-api
- collection_type: postman
  name: Iterable Export Campaigns Experiments API
  slug: postman-iterable-experiments-api
- collection_type: postman
  name: Iterable Campaigns Export API
  slug: postman-iterable-export-api
- collection_type: postman
  name: Iterable Export Campaigns InApp API
  slug: postman-iterable-inapp-api
- collection_type: postman
  name: Iterable Export Campaigns Lists API
  slug: postman-iterable-lists-api
- collection_type: postman
  name: Iterable Export Campaigns MessageTypes API
  slug: postman-iterable-messagetypes-api
- collection_type: postman
  name: Iterable Export Campaigns Metadata API
  slug: postman-iterable-metadata-api
- collection_type: postman
  name: Iterable Export Campaigns Push API
  slug: postman-iterable-push-api
- collection_type: postman
  name: Iterable Export Campaigns SMS API
  slug: postman-iterable-sms-api
- collection_type: postman
  name: Iterable Export Campaigns Templates API
  slug: postman-iterable-templates-api
- collection_type: postman
  name: Iterable Export Campaigns Users API
  slug: postman-iterable-users-api
- collection_type: postman
  name: Iterable Export Campaigns WebPush API
  slug: postman-iterable-webpush-api
- collection_type: postman
  name: Iterable Export Campaigns Workflows API
  slug: postman-iterable-workflows-api
- collection_type: open
  name: Iterable Export Campaigns API
  slug: open-iterable-campaigns-api
- collection_type: open
  name: Iterable Export Campaigns Catalogs API
  slug: open-iterable-catalogs-api
- collection_type: open
  name: Iterable Export Campaigns Channels API
  slug: open-iterable-channels-api
- collection_type: open
  name: Iterable Export Campaigns Commerce API
  slug: open-iterable-commerce-api
- collection_type: open
  name: Iterable Export Campaigns Email API
  slug: open-iterable-email-api
- collection_type: open
  name: Iterable Export Campaigns Events API
  slug: open-iterable-events-api
- collection_type: open
  name: Iterable Export Campaigns ExperimentMetrics API
  slug: open-iterable-experimentmetrics-api
- collection_type: open
  name: Iterable Export Campaigns Experiments API
  slug: open-iterable-experiments-api
- collection_type: open
  name: Iterable Campaigns Export API
  slug: open-iterable-export-api
- collection_type: open
  name: Iterable Export Campaigns InApp API
  slug: open-iterable-inapp-api
- collection_type: open
  name: Iterable Export Campaigns Lists API
  slug: open-iterable-lists-api
- collection_type: open
  name: Iterable Export Campaigns MessageTypes API
  slug: open-iterable-messagetypes-api
- collection_type: open
  name: Iterable Export Campaigns Metadata API
  slug: open-iterable-metadata-api
- collection_type: open
  name: Iterable Export Campaigns Push API
  slug: open-iterable-push-api
- collection_type: open
  name: Iterable REST API
  slug: open-iterable-rest-api
- collection_type: open
  name: Iterable Export Campaigns SMS API
  slug: open-iterable-sms-api
- collection_type: open
  name: Iterable Export Campaigns Templates API
  slug: open-iterable-templates-api
- collection_type: open
  name: Iterable Export Campaigns Users API
  slug: open-iterable-users-api
- collection_type: open
  name: Iterable Export Campaigns WebPush API
  slug: open-iterable-webpush-api
- collection_type: open
  name: Iterable Export Campaigns Workflows API
  slug: open-iterable-workflows-api
common:
- group: commercial
  href: https://artifacts.apis.io/iterable/plans/iterable-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/iterable-plans-pricing.yml
- group: commercial
  href: https://artifacts.apis.io/iterable/finops/iterable-finops.yml
  title: ''
  type: FinOps
  url: finops/iterable-finops.yml
- group: other
  href: https://artifacts.apis.io/iterable/overlays/iterable-inapp-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/iterable-inapp-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/iterable/overlays/iterable-messagetypes-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/iterable-messagetypes-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/iterable/overlays/iterable-webpush-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/iterable-webpush-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/iterable/capabilities/iterable-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/iterable-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/iterable/overlays/iterable-experimentmetrics-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/iterable-experimentmetrics-api-overlay.yaml
- group: docs
  href: https://artifacts.apis.io/iterable/openapi/_original/iterable-api-openapi.json
  title: ''
  type: OpenAPI
  url: openapi/_original/iterable-api-openapi.json
- group: build
  href: https://artifacts.apis.io/iterable/packages/iterable-packages.yml
  title: ''
  type: Packages
  url: packages/iterable-packages.yml
- group: build
  href: https://artifacts.apis.io/iterable/packages/iterable-packages.yml
  title: ''
  type: SDKs
  url: packages/iterable-packages.yml
- group: build
  href: https://artifacts.apis.io/iterable/cli/iterable-cli.yml
  title: ''
  type: CLI
  url: cli/iterable-cli.yml
- group: agent
  href: https://artifacts.apis.io/iterable/mcp/iterable-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/iterable-mcp.yml
- group: build
  href: https://artifacts.apis.io/iterable/mcp/iterable-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/iterable-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/iterable/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/iterable/llms/iterable-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/iterable-llms.txt
- group: design
  href: https://artifacts.apis.io/iterable/conventions/iterable-conventions.yml
  title: ''
  type: Conventions
  url: conventions/iterable-conventions.yml
- group: design
  href: https://artifacts.apis.io/iterable/errors/iterable-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/iterable-error-codes.yml
- group: design
  href: https://artifacts.apis.io/iterable/errors/iterable-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/iterable-problem-types.yml
- group: operate
  href: https://artifacts.apis.io/iterable/rate-limits/iterable-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/iterable-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/iterable/data-model/iterable-data-model.yml
  title: ''
  type: DataModel
  url: data-model/iterable-data-model.yml
- group: design
  href: https://artifacts.apis.io/iterable/lifecycle/iterable-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/iterable-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.iterable.com/
- group: operate
  title: ''
  type: Deprecation
  url: https://support.iterable.com/hc/en-us/articles/360046136171-SDK-Support-Policy
- group: design
  href: https://artifacts.apis.io/iterable/conformance/iterable-conformance.yml
  title: ''
  type: Conformance
  url: conformance/iterable-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.iterable.com/
- group: operate
  href: https://artifacts.apis.io/iterable/changelog/iterable-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/iterable-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://support.iterable.com/hc/en-us/articles/44900665796628-2026-Release-Notes
- group: design
  title: ''
  type: Webhooks
  url: https://support.iterable.com/hc/en-us/articles/208013936-System-Webhooks
- group: design
  href: https://artifacts.apis.io/iterable/vocabulary/iterable-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/iterable-vocabulary.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://support.iterable.com/hc/en-us/categories/360002288712
- group: docs
  title: ''
  type: APIReference
  url: https://api.iterable.com/api/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://support.iterable.com/hc/en-us/articles/41044692130196-Getting-Started-with-Iterable-s-API
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Iterable
- group: operate
  title: ''
  type: Community
  url: https://community.iterable.com/
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/iterable/overview
- group: agent
  href: https://artifacts.apis.io/iterable/agentic-access/iterable-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/iterable-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/iterable/security/iterable-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/iterable-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/iterable/security/iterable-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/iterable-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/iterable/authentication/iterable-authentication.yml
  title: ''
  type: Authentication
  url: authentication/iterable-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/iterable
- group: docs
  href: https://artifacts.apis.io/iterable/asyncapi/iterable-system-webhooks-asyncapi.yml
  title: ''
  type: AsyncAPI
  url: asyncapi/iterable-system-webhooks-asyncapi.yml
- group: design
  href: https://artifacts.apis.io/iterable/json-ld/iterable-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/iterable-context.jsonld
- group: docs
  href: https://artifacts.apis.io/iterable/json-schema/iterable-user-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/iterable-user-schema.json
- group: docs
  href: https://artifacts.apis.io/iterable/json-schema/iterable-campaign-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/iterable-campaign-schema.json
- group: docs
  href: https://artifacts.apis.io/iterable/json-schema/iterable-event-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/iterable-event-schema.json
- group: docs
  href: https://artifacts.apis.io/iterable/json-schema/iterable-commerce-item-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/iterable-commerce-item-schema.json
- group: company
  title: ''
  type: Website
  url: https://iterable.com/
- group: docs
  title: ''
  type: Documentation
  url: https://api.iterable.com/api/docs
- group: operate
  title: ''
  type: Support
  url: https://support.iterable.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://iterable.com/blog/
- group: start
  title: ''
  type: Login
  url: https://app.iterable.com/login
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://iterable.com/trust/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://iterable.com/legal/terms/
created: '2026-03-20'
description: Iterable is an AI customer engagement platform that powers unified cross-channel marketing experiences and empowers marketers to create, optimize, and measure relevant interactions across email, push, SMS, in-app, and web channels. Their developer platform provides REST APIs, export APIs, AsyncAPI webhooks, and native SDKs for web, iOS, Android, and React Native.
features:
- 'Growth: $3K-$5K/mo for 10K-50K MAUs'
- 'Premier: $6K-$15K/mo for 50K-200K MAUs'
- 'Enterprise: $20K+/mo for 200K+ MAUs'
- Multi-year + volume discounts
- Email + Push + SMS + In-App + Web Push + Direct Mail channels
- Workflow Studio for journey orchestration
- AI Optimization for send-time and channel selection (Premier+)
- REST API at api.iterable.com
- Default 30 req/sec; bulk endpoints up to 1K events/req
- OAuth + API keys (project-scoped)
- Webhooks for events and campaign data
- User profile and event tracking
- Cross-channel campaigns
- Smart Ingest for data lake/warehouse loading
- Real-time event triggers
- Iterable AI for content suggestions
finops:
- has_sources: true
  method: generated
  name: Iterable Finops
  primary_unit: ''
  service_category: Marketing Automation
  slug: iterable-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/iterable.png
json_schemas:
- name: Iterable Campaign
  property_count: 15
  slug: iterable-campaign
- name: CampaignCreateRequest
  property_count: 6
  slug: iterable-campaigncreaterequest
- name: Channel
  property_count: 4
  slug: iterable-channel
- name: Iterable Commerce Item
  property_count: 10
  slug: iterable-commerce-item
- name: CommerceItem
  property_count: 10
  slug: iterable-commerceitem
- name: EmailTemplate
  property_count: 11
  slug: iterable-emailtemplate
- name: EmailTemplateUpdate
  property_count: 8
  slug: iterable-emailtemplateupdate
- name: ErrorResponse
  property_count: 2
  slug: iterable-errorresponse
- name: Iterable Event
  property_count: 7
  slug: iterable-event
- name: ExportedEvent
  property_count: 15
  slug: iterable-exportedevent
- name: IterableResponse
  property_count: 3
  slug: iterable-iterableresponse
- name: List
  property_count: 5
  slug: iterable-list
- name: PurchaseRequest
  property_count: 7
  slug: iterable-purchaserequest
- name: TrackEventRequest
  property_count: 7
  slug: iterable-trackeventrequest
- name: Iterable User
  property_count: 10
  slug: iterable-user
- name: UserResponse
  property_count: 1
  slug: iterable-userresponse
- name: UserUpdateRequest
  property_count: 5
  slug: iterable-userupdaterequest
json_structures:
- name: Iterable Structure
  property_count: 0
  slug: iterable-structure
jsonld:
- class_count: 0
  name: Iterable Context
  property_count: 8
  slug: iterable-context
layout: provider
mcp_servers:
- description: 'Iterable publishes a first-party MCP server as the npm package @iterable/mcp (repo github.com/Iterable/mcp-server). It is a LOCAL STDIO server: a developer installs and runs it with npx, and it calls '
  name: Iterable MCP Server (@iterable/mcp, local stdio)
  slug: iterable
modified: '2026-08-13'
name: Iterable
nav: Providers
network: true
overview: 'Iterable publishes 29 API contracts indexed on the [APIs.io](https://apis.io/) network, including Export API, Campaigns API, Catalogs API, and 26 more. Tagged areas include Cross-Channel Messaging, Customer Engagement, Email, Marketing Automation, and Push Notifications.


  The Iterable catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 2 Spectral governance rulesets.


  Iterable''s developer surface includes CLI, changelog, API reference, getting-started guide, authentication, documentation, support, and 46 more developer resources.'
plans:
- name: Iterable Plans Pricing
  plan_count: 3
  slug: iterable-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 54
  name: Iterable Rate Limits
  slug: iterable-rate-limits
rules:
- authorship: generated
  effective_rule_count: 35
  extends:
  - spectral:asyncapi
  name: Iterable — asyncapi rules
  rule_count: 8
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 6
  slug: iterable-asyncapi-spectral-rules
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: Iterable — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: iterable-jsonschema-spectral-rules
score:
  band: exemplar
  composite: 67.9
  coverage:
    artifact_dirs: 36
    catalog_earned: 66.0
    catalog_earned_first_party: 12.0
    catalog_gap: 49.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.4
  facets:
    access_clarity: 57.9
    contract_governance: 31.8
    contract_quality: 61.8
    developer_ergonomics: 79.8
    discoverability: 71.7
    operational_transparency: 81.6
  previous_composite: 67.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 30.8
      total: 26
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 25.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 33.3
screenshot: https://apis.io/screenshots/iterable/iterable-2026-06-20T183630.png
security:
- kind: authentication
  name: Iterable Authentication
  slug: iterable-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Iterable Domain Security
  slug: iterable-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Iterable Trust Center
  slug: iterable-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, GDPR
skill_count: 4
skills:
- name: iterable-android
  slug: iterable-android-sdk
- name: Export Iterable project data
  slug: iterable-export-project-data
- name: Send a transactional message from a template
  slug: iterable-send-transactional-message
- name: Track a user event and trigger a journey
  slug: iterable-track-event-and-trigger-journey
slug: iterable
tags:
- Cross-Channel Messaging
- Customer Engagement
- Email
- Marketing Automation
- Push Notifications
- SMS
website: https://iterable.com/
---
