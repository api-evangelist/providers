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
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: true
    idempotency: verified
    mcp_server: verified
    openapi_examples: verified
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 67.8
  scored_at: '2026-10-04'
api_count: 30
apis:
- description: Hosted, OAuth-secured Model Context Protocol server that lets AI assistants build campaign drafts, author content, create and count segments, read and analyze flows, browse dashboards, search campaign
  name: MoEngage MCP Server
  slug: moengage-mcp-server
- baseURL: https://api-01.moengage.com/v1
  baseurl_source: declared
  description: Operations for importing users and events in bulk.
  name: MoEngage Bulk API
  phrasing_intents:
  - id: postTransitionByWorkspaceID
    intent: Bulk import users and events in one batch
    question: How do I send many user profiles and events to MoEngage in a single request?
  phrasing_ops: 1
  slug: moengage-bulk-api
- baseURL: https://api-01.moengage.com/v1
  baseurl_source: declared
  description: Manage and trigger business events.
  name: MoEngage Business Events API
  phrasing_intents:
  - id: createBusinessEvent
    intent: Define a new business event
    question: How do I set up a business event in MoEngage that campaigns can be triggered by?
  - id: triggerBusinessEvent
    intent: Fire a business event to start campaigns
    question: How do I fire a business event so the campaigns listening for it go out?
  - id: searchBusinessEvents
    intent: Look up business events by ID or name
    question: Which business events have I already defined, looked up by their IDs?
  phrasing_ops: 3
  slug: moengage-business-events-api
- baseURL: https://api-01.moengage.com/v1
  baseurl_source: declared
  description: Download campaign report files.
  name: MoEngage Campaign Reports API
  phrasing_intents:
  - id: downloadCampaignReport
    intent: Download a campaign report file
    question: How do I download a MoEngage campaign report for a date range?
  phrasing_ops: 1
  slug: moengage-campaign-reports-api
- baseURL: https://api-01.moengage.com/v1
  baseurl_source: declared
  description: Operations related to fetching and deleting user cards.
  name: MoEngage Cards API
  phrasing_intents:
  - id: fetchCards
    intent: Fetch a user's active cards
    question: How do I get all the active cards a specific user should see in their inbox?
  - id: deleteCards
    intent: Delete a user's cards from campaigns
    question: How do I remove cards from a user's inbox for specific campaigns?
  phrasing_ops: 2
  slug: moengage-cards-api
- baseURL: https://api-01.moengage.com/v1
  baseurl_source: declared
  description: Operations related to creating and managing catalog schemas (attributes).
  name: MoEngage Catalog API
  phrasing_intents:
  - id: createCatalog
    intent: Create a product catalog
    question: How do I create a product catalog in MoEngage for recommendations?
  - id: addCatalogAttributes
    intent: Add attributes to an existing catalog
    question: How do I add new fields to a catalog I already created?
  phrasing_ops: 2
  slug: moengage-catalog-api
- baseURL: https://api-01.moengage.com/v1
  baseurl_source: declared
  description: Operations to synchronize cohorts (custom segments) with MoEngage.
  name: MoEngage Cohort Sync API
  phrasing_intents:
  - id: postV1IntegrationsCohortsync
    intent: Add or remove users in a partner cohort
    question: How do I sync a partner's cohort of users into a custom segment?
  phrasing_ops: 1
  slug: moengage-cohort-sync-api
- baseURL: https://api-01.moengage.com/v1
  baseurl_source: declared
  description: Use these operations to programmatically fetch, create, and update reusable content blocks.
  name: MoEngage Content Blocks API
  phrasing_intents:
  - id: postContentBlocks
    intent: Create a new content block
    question: How do I create a reusable content block for campaigns?
  - id: putContentBlocks
    intent: Update an existing content block
    question: How do I edit the HTML of a content block that already exists?
  - id: postContentBlocksGetByIds
    intent: Fetch specific content blocks by ID
    question: How do I fetch several content blocks when I already know their IDs?
  - id: postContentBlocksSearch
    intent: Search content blocks
    question: Which content blocks exist in my MoEngage account?
  phrasing_ops: 4
  slug: moengage-content-blocks-api
- baseURL: https://api-01.moengage.com/v1
  baseurl_source: declared
  description: Operations related to uploading coupon codes via files and checking/managing file processing status.
  name: MoEngage Coupon Files API
  phrasing_intents:
  - id: uploadCouponFile
    intent: Upload coupon codes into a coupon list
    question: How do I replenish a coupon list that's running low on codes?
  - id: fetchAllCouponFiles
    intent: List the files in a coupon list
    question: How do I see every file that was uploaded into a coupon list?
  - id: fetchCouponFile
    intent: Get one coupon file's status
    question: What's the processing status of a single coupon file I uploaded?
  - id: deleteCouponFile
    intent: Remove a coupon file from a coupon list
    question: How do I remove a test file I uploaded to a coupon list by mistake?
  phrasing_ops: 4
  slug: moengage-coupon-files-api
- baseURL: https://api-01.moengage.com/v1
  baseurl_source: declared
  description: Operations related to defining, managing status (active/archive), and modifying coupon list metadata.
  name: MoEngage Coupon Lists API
  phrasing_intents:
  - id: createCouponList
    intent: Create a coupon list
    question: How do I create a list of single-use coupon codes for campaigns?
  - id: fetchAllCouponLists
    intent: List coupon lists in a workspace
    question: What coupon lists exist in my MoEngage workspace?
  - id: fetchCouponList
    intent: Get a coupon list's details and counts
    question: How many coupons are still available in a specific coupon list?
  - id: updateCouponList
    intent: Edit a coupon list's settings
    question: Can I rename a coupon list or push back its expiry date?
  - id: activateCouponList
    intent: Reactivate an archived coupon list
    question: How do I bring an archived coupon list back into use?
  - id: archiveCouponList
    intent: Archive a coupon list
    question: What happens to the coupon codes when I archive a coupon list?
  phrasing_ops: 6
  slug: moengage-coupon-lists-api
- baseURL: https://api-01.moengage.com/v1
  baseurl_source: declared
  description: The Create Campaigns API from MoEngage — 3 operation(s) for create campaigns.
  name: MoEngage Create Campaigns API
  phrasing_intents:
  - id: create_draft_campaign_v5
    intent: Create a Push or Email campaign draft (V5)
    question: How do I start a campaign as a draft with the V5 API and fill it in later?
  - id: validate_draft_campaign_v5
    intent: Check a draft campaign is ready to publish
    question: How do I check whether a draft campaign would pass publish validation without changing it?
  - id: create_campaign
    intent: Create and launch a campaign (legacy)
    question: How do I create a complete Push or Email campaign in one call with the older campaigns endpoint?
  phrasing_ops: 3
  slug: moengage-create-campaigns-api
- baseURL: https://api-01.moengage.com/v1
  baseurl_source: declared
  description: Read custom dashboards and their chart data.
  name: MoEngage Dashboards API
  phrasing_intents:
  - id: listDashboards
    intent: List custom analytics dashboards
    question: What custom analytics dashboards does my workspace have?
  - id: getDashboardCharts
    intent: List the charts on a dashboard
    question: Which charts are on a particular dashboard, and who owns it?
  - id: getChartData
    intent: Get the data behind a chart
    question: How do I pull the underlying rows for a single dashboard chart?
  phrasing_ops: 3
  slug: moengage-dashboards-api
- baseURL: https://api-01.moengage.com/v1
  baseurl_source: declared
  description: Operations for managing user devices.
  name: MoEngage Device API
  phrasing_intents:
  - id: postDeviceByAppId
    intent: Add or update a user's device properties
    question: How do I register a new device for an existing user?
  - id: postDevicesManage
    intent: Block or unblock a device from push notifications
    question: How do I stop push notifications reaching a stolen phone?
  phrasing_ops: 2
  slug: moengage-device-api
- baseURL: https://api-01.moengage.com/v1
  baseurl_source: declared
  description: Manage email templates in MoEngage.
  name: MoEngage Email Templates API
  phrasing_intents:
  - id: createEmailTemplate
    intent: Upload an email template (V1)
    question: How do I upload HTML email templates built outside MoEngage using the original V1 endpoint?
  - id: getAllTemplates
    intent: List all email templates
    question: What email templates are in my MoEngage account?
  - id: getTemplateById
    intent: Get an email template by ID
    question: How do I fetch one email template's content by its template ID?
  - id: updateTemplateById
    intent: Replace an email template by its ID
    question: How do I overwrite an email template's HTML using its MoEngage template ID?
  - id: bulkCreateUpdateTemplates
    intent: Create or update many email templates at once
    question: Can I create or update up to 50 email templates in a single request?
  - id: postCustomTemplatesEmail
    intent: Upload an editable email template (V2)
    question: How do I upload an email template that can be edited in the Froala editor on the dashboard?
  - id: updateEmailTemplate
    intent: Update an email template by external ID
    question: How do I update an email template using my own external template ID?
  - id: searchEmailTemplate
    intent: Search custom email templates
    question: How do I search email templates by name or creator?
  phrasing_ops: 8
  slug: moengage-email-templates-api
- baseURL: https://api-01.moengage.com/v1
  baseurl_source: declared
  description: Operations for tracking user events.
  name: MoEngage Event API
  phrasing_intents:
  - id: postEventByWorkspaceID
    intent: Track a user's actions as events
    question: How do I record an action a user took, like a purchase, as an event?
  phrasing_ops: 1
  slug: moengage-event-api
- baseURL: https://api-01.moengage.com/v1
  baseurl_source: declared
  description: API endpoints for reporting impressions and clicks.
  name: MoEngage Events API
  phrasing_intents:
  - id: reportExperienceEvents
    intent: Track experience impressions and clicks
    question: How do I report that a personalization experience was shown to a user?
  phrasing_ops: 1
  slug: moengage-events-api
- baseURL: https://api-01.moengage.com/v1
  baseurl_source: declared
  description: API endpoints for fetching experiences and metadata.
  name: MoEngage Experiences API
  phrasing_intents:
  - id: fetchExperience
    intent: Get the right experience variation for a user
    question: How do I fetch which personalization variation a user should see server-side?
  - id: getMetadata
    intent: List active, scheduled and paused experiences
    question: What personalization experiences are currently live in my workspace?
  phrasing_ops: 2
  slug: moengage-experiences-api
- baseURL: https://api-01.moengage.com/v1
  baseurl_source: declared
  description: The File Import API from MoEngage — 3 operation(s) for file import.
  name: MoEngage File Import API
  phrasing_intents:
  - id: postFileimportsTriggerByScheduleId
    intent: Trigger a scheduled file import to run now
    question: How do I make a scheduled file import run right away?
  - id: postFileimportsImportStatus
    intent: Get the status of file imports
    question: What is the status of my file imports?
  - id: postFileimportsImportRunHistory
    intent: Get per-file run history for an import
    question: How do I see the processing status of each file inside an import?
  phrasing_ops: 3
  slug: moengage-file-import-api
- baseURL: https://api-01.moengage.com/v1
  baseurl_source: declared
  description: If you need to create segments by importing a large number of users, we recommend utilising the File segment API. This API allows you to easily generate a file segment by initiating a call to the file
  name: MoEngage File Segments API
  phrasing_intents:
  - id: createFileSegment
    intent: Create a segment from a CSV file
    question: How do I build a user segment from a CSV file of user IDs?
  - id: addUsersToFileSegment
    intent: Add users from a CSV to a file segment
    question: How do I append more users to an existing file segment?
  - id: removeUsersFromFileSegment
    intent: Remove users listed in a CSV from a file segment
    question: How do I take specific users out of a file segment using a CSV?
  - id: replaceUsersInFileSegment
    intent: Replace all users in a file segment
    question: How do I swap out a file segment's entire membership with a fresh CSV?
  phrasing_ops: 4
  slug: moengage-file-segments-api
- baseURL: https://api-01.moengage.com/v1
  baseurl_source: declared
  description: If you need to create a segment based on the events or actions performed by your users on your application or website, the recommended approach is to use the filter segment API. With this API, you can
  name: MoEngage Filter Segments API
  phrasing_intents:
  - id: listCustomSegments
    intent: List user segments
    question: What custom segments exist in my MoEngage workspace?
  - id: createFilterSegment
    intent: Create a segment from filter conditions
    question: How do I create a segment of users who match a set of filters?
  - id: getCustomSegment
    intent: Get a segment by ID
    question: How do I look up one segment's details by its ID?
  - id: updateFilterSegment
    intent: Change a filter segment's conditions
    question: How do I change the filter conditions of an existing filter segment?
  phrasing_ops: 4
  slug: moengage-filter-segments-api
- baseURL: https://api-01.moengage.com/v1
  baseurl_source: declared
  description: The Flows API from MoEngage — 4 operation(s) for flows.
  name: MoEngage Flows API
  phrasing_intents:
  - id: searchFlows
    intent: Search journey flows
    question: How do I find flows by status, tag or name?
  - id: getFlow
    intent: Get a flow's full structure
    question: How do I see a flow's settings, targeting and stage-by-stage structure?
  - id: getFlowVersion
    intent: Get a past version of a flow by version ID
    question: How do I audit what a flow looked like before a recent change, using its version ID?
  - id: updateFlowStatus
    intent: Change a flow's lifecycle state
    question: How do I pause, resume or stop a flow through the API?
  phrasing_ops: 4
  slug: moengage-flows-api
- baseURL: https://api-01.moengage.com/v1
  baseurl_source: declared
  description: Manage user data requests for GDPR and CCPA compliance.
  name: MoEngage GDPR API
  phrasing_intents:
  - id: submitGdprRequest
    intent: Submit a GDPR or CCPA data request
    question: How do I erase a user's personal data in MoEngage for GDPR?
  phrasing_ops: 1
  slug: moengage-gdpr-api
- baseURL: https://api-01.moengage.com/v1
  baseurl_source: declared
  description: The Get Campaign Details API from MoEngage — 6 operation(s) for get campaign details.
  name: MoEngage Get Campaign Details API
  phrasing_intents:
  - id: get_single_campaign_v5
    intent: Get one campaign's configuration (V5)
    question: How do I get the full configuration and current status of a single campaign?
  - id: search_campaigns_v5
    intent: Search campaigns with full payloads (V5)
    question: How do I search campaigns by channel, status or tag and get their full V5 details?
  - id: get_campaign_meta_v5
    intent: Get lightweight campaign metadata (V5)
    question: Can I get just summary metadata for campaigns without their full configuration?
  - id: search_campaigns
    intent: Search Push, Email or SMS campaigns (legacy)
    question: How do I search SMS campaigns along with Push and Email on the older search endpoint?
  - id: get_campaign_meta
    intent: Get scheduled campaign reachability (legacy)
    question: How do I see reachability for my scheduled campaigns?
  - id: get_child_campaigns
    intent: List executions of a recurring campaign
    question: How do I see each run of a periodic campaign?
  phrasing_ops: 6
  slug: moengage-get-campaign-details-api
- baseURL: https://api-01.moengage.com/v1
  baseurl_source: declared
  description: Operations to manage In-app templates.
  name: MoEngage In-app Templates API
  phrasing_intents:
  - id: postCustomTemplatesInapp
    intent: Create an in-app message template
    question: How do I upload an in-app template designed outside MoEngage?
  - id: putCustomTemplatesInapp
    intent: Update an in-app message template
    question: How do I change an in-app template I already uploaded?
  - id: postCustomTemplatesInappSearch
    intent: Search in-app message templates
    question: Which in-app templates exist in my account?
  phrasing_ops: 3
  slug: moengage-in-app-templates-api
- baseURL: https://api-01.moengage.com/v1
  baseurl_source: declared
  description: Operations related to ingesting, updating, and deleting items within a catalog.
  name: MoEngage Items API
  phrasing_intents:
  - id: ingestCatalogItems
    intent: Add items to a catalog
    question: How do I load products into an existing catalog?
  - id: updateCatalogItems
    intent: Update item attributes in a catalog
    question: How do I change the price or title of products already in a catalog?
  - id: deleteCatalogItems
    intent: Delete items from a catalog
    question: How do I remove discontinued products from a catalog?
  - id: getItemDetails
    intent: Look up catalog items by ID
    question: How do I get the title, price and link of specific catalog items by their IDs?
  phrasing_ops: 4
  slug: moengage-items-api
- baseURL: https://api-01.moengage.com/v1
  baseurl_source: declared
  description: Operations to manage broadcast Live Activities for iOS.
  name: MoEngage Live Activities API
  phrasing_intents:
  - id: postLiveActivityBroadcastStart
    intent: Start a broadcast Live Activity
    question: How do I start an iOS Live Activity for a big audience, like a live match?
  - id: postLiveActivityBroadcastUpdate
    intent: Push an update to a running broadcast Live Activity
    question: How do I push a new score to a Live Activity that is already running?
  - id: postLiveActivityBroadcastEnd
    intent: End a broadcast Live Activity
    question: How do I end a broadcast Live Activity on all devices when the event is over?
  phrasing_ops: 3
  slug: moengage-live-activities-api
- baseURL: https://api-01.moengage.com/v1
  baseurl_source: declared
  description: Archiving and unarchiving through APIs makes it easy to retrieve and reuse segments whenever required for purposes such as A/B testing, maintaining regulatory compliance, and improving system performa
  name: MoEngage Manage Segments API
  phrasing_intents:
  - id: archiveCustomSegment
    intent: Archive a segment
    question: How do I archive a segment I'm not using right now?
  - id: unarchiveCustomSegment
    intent: Restore an archived segment
    question: How do I make an archived segment active again?
  phrasing_ops: 2
  slug: moengage-manage-segments-api
- baseURL: https://api-01.moengage.com/v1
  baseurl_source: declared
  description: Retrieve archived message content.
  name: MoEngage Message Archival API
  phrasing_intents:
  - id: viewArchivedMessage
    intent: View a message sent to a customer
    question: How do I look up the exact message a customer was sent by a campaign?
  phrasing_ops: 1
  slug: moengage-message-archival-api
- baseURL: https://api-01.moengage.com/v1
  baseurl_source: declared
  description: Update user email opt-in status and category preferences in MoEngage.
  name: MoEngage Opt-in Management API
  phrasing_intents:
  - id: updateEmailOptinPreferences
    intent: Update a user's email opt-in status
    question: How do I record that a user confirmed their double opt-in for email?
  phrasing_ops: 1
  slug: moengage-opt-in-management-api
- baseURL: https://api-01.moengage.com/v1
  baseurl_source: declared
  description: Operations to manage On-Site Messaging (OSM) templates.
  name: MoEngage OSM Templates API
  phrasing_intents:
  - id: postCustomTemplatesOsm
    intent: Create an on-site messaging template
    question: How do I upload an on-site messaging template built outside MoEngage?
  - id: putCustomTemplatesOsm
    intent: Update an on-site messaging template
    question: How do I edit an on-site messaging (OSM) template I already uploaded?
  - id: postCustomTemplatesOsmSearch
    intent: Search on-site messaging templates
    question: Which OSM templates are in my account?
  phrasing_ops: 3
  slug: moengage-osm-templates-api
- baseURL: https://api-01.moengage.com/v1
  baseurl_source: declared
  description: The Personalized Preview API from MoEngage — 1 operation(s) for personalized preview.
  name: MoEngage Personalized Preview API
  phrasing_intents:
  - id: preview_personalized_content_v5
    intent: Preview campaign content as a user sees it (V5)
    question: How do I see exactly how personalized campaign content will render for one user?
  phrasing_ops: 1
  slug: moengage-personalized-preview-api
- baseURL: https://api-01.moengage.com/v1
  baseurl_source: declared
  description: The Public Offerings API from MoEngage — 3 operation(s) for public offerings.
  name: MoEngage Public Offerings API
  phrasing_intents:
  - id: listPublicOfferings
    intent: List offerings
    question: What offerings exist in my workspace?
  - id: createPublicOffering
    intent: Create an offering
    question: How do I create a new offer with targeting, scheduling and content?
  - id: updatePublicOffering
    intent: Modify an existing offering
    question: How do I change the priority or schedule of an offer that's already set up?
  - id: listPublicOfferTemplates
    intent: List offer personalization templates
    question: What personalization templates can I use when building offers?
  phrasing_ops: 4
  slug: moengage-public-offerings-api
- baseURL: https://api-01.moengage.com/v1
  baseurl_source: declared
  description: Operations related to fetching recommendation configurations and results.
  name: MoEngage Recommendations API
  phrasing_intents:
  - id: fetchRecommendationMetadata
    intent: Get a recommendation setup's details
    question: What model type and status does a recommendation setup use?
  - id: fetchRecommendationResults
    intent: Get recommended items for a user
    question: How do I get the products recommended for a specific user?
  phrasing_ops: 2
  slug: moengage-recommendations-api
- baseURL: https://api-01.moengage.com/v1
  baseurl_source: declared
  description: Operations related to generating usage reports for coupon lists.
  name: MoEngage Reports API
  phrasing_intents:
  - id: generateUsageReport
    intent: Email a coupon list usage report
    question: How do I find out which user received which coupon from a coupon list?
  phrasing_ops: 1
  slug: moengage-reports-api
- baseURL: https://api-01.moengage.com/v1
  baseurl_source: declared
  description: Resubscribe users who previously unsubscribed, and optionally update the ESP suppression list.
  name: MoEngage Resubscribe API
  phrasing_intents:
  - id: bulkResubscribeUsers
    intent: Resubscribe unsubscribed email users
    question: How do I resubscribe users who previously unsubscribed from email?
  phrasing_ops: 1
  slug: moengage-resubscribe-api
- baseURL: https://api-01.moengage.com/v1
  baseurl_source: declared
  description: Operations to manage SMS templates.
  name: MoEngage SMS Templates API
  phrasing_intents:
  - id: postCustomTemplatesSms
    intent: Create an SMS template
    question: How do I upload an SMS template written outside MoEngage?
  - id: putCustomTemplatesSms
    intent: Update an SMS template
    question: How do I change the text of an SMS template I uploaded?
  - id: postCustomTemplatesSmsSearch
    intent: Search SMS templates
    question: Which SMS templates do I have in my account?
  phrasing_ops: 3
  slug: moengage-sms-templates-api
- baseURL: https://api-01.moengage.com/v1
  baseurl_source: declared
  description: Fetch detailed, real-time campaign statistics.
  name: MoEngage Stats API
  phrasing_intents:
  - id: getCampaignStats
    intent: Get campaign performance stats
    question: How do I get delivery and engagement stats for my campaigns over a date range?
  phrasing_ops: 1
  slug: moengage-stats-api
- baseURL: https://api-01.moengage.com/v1
  baseurl_source: declared
  description: Manage user email subscription preferences.
  name: MoEngage Subscription Preferences API
  phrasing_intents:
  - id: getSubscriptionPreferences
    intent: Get a user's category subscriptions
    question: How do I show a user their current email category preferences on my landing page?
  - id: updateSubscriptionPreferences
    intent: Save one user's category subscriptions
    question: How do I save the categories a user picked after clicking through from an email?
  - id: bulkUpdateSubscriptionPreferences
    intent: Bulk update users' category subscriptions
    question: How do I sync subscription preferences for a large number of users at once?
  phrasing_ops: 3
  slug: moengage-subscription-preferences-api
- baseURL: https://api-01.moengage.com/v1
  baseurl_source: declared
  description: The Templates API from MoEngage — 2 operation(s) for templates.
  name: MoEngage Templates API
  phrasing_intents:
  - id: createPushTemplate
    intent: Create a push notification template
    question: How do I create a reusable push notification template for Android and iOS?
  - id: updatePushTemplate
    intent: Update a push notification template
    question: How do I update a push template, creating a new version?
  - id: searchPushTemplates
    intent: Search push notification templates
    question: How do I find push templates by name or platform?
  phrasing_ops: 3
  slug: moengage-templates-api
- baseURL: https://api-01.moengage.com/v1
  baseurl_source: declared
  description: The Test Campaigns API from MoEngage — 3 operation(s) for test campaigns.
  name: MoEngage Test Campaigns API
  phrasing_intents:
  - id: test_campaign_v5
    intent: Send a test of a campaign (V5)
    question: How do I send a V5 test message to a few users before publishing?
  - id: test_campaign
    intent: Send a test of an API-created campaign (legacy)
    question: Can I send a test of a campaign on the legacy endpoint before launching it to everyone?
  - id: personalized_preview
    intent: Preview personalized content (legacy)
    question: How do I preview a personalized SMS before sending it?
  phrasing_ops: 3
  slug: moengage-test-campaigns-api
- baseURL: https://api-01.moengage.com/v1
  baseurl_source: declared
  description: Endpoints for tracking attribution and installs.
  name: MoEngage Tracking API
  phrasing_intents:
  - id: getInstallInfo
    intent: Record install attribution for an app install
    question: How do I send app install attribution data from my attribution partner?
  phrasing_ops: 1
  slug: moengage-tracking-api
- baseURL: https://api-01.moengage.com/v1
  baseurl_source: declared
  description: Send transactional alerts using pre-configured templates.
  name: MoEngage Transactional Alerts API
  phrasing_intents:
  - id: postAlertsSend
    intent: Send a transactional alert to a user
    question: How do I send an order confirmation alert to a customer across channels?
  phrasing_ops: 1
  slug: moengage-transactional-alerts-api
- baseURL: https://api-01.moengage.com/v1
  baseurl_source: declared
  description: Operations to create and send push notification campaigns.
  name: MoEngage Transactional API
  phrasing_intents:
  - id: postTransactionSendpush
    intent: Send a push campaign via the original endpoint
    question: How do I send a push campaign with the older sendpush endpoint that takes appId and signature in the body?
  - id: send_push_v2_1
    intent: Send a push notification campaign
    question: How do I send a push notification to one user by a unique attribute?
  phrasing_ops: 2
  slug: moengage-transactional-api
- baseURL: https://api-01.moengage.com/v1
  baseurl_source: declared
  description: The Update Campaigns API from MoEngage — 5 operation(s) for update campaigns.
  name: MoEngage Update Campaigns API
  phrasing_intents:
  - id: patch_draft_campaign_v5
    intent: Edit a campaign draft (V5)
    question: How do I change the content or audience of a draft campaign with the V5 API?
  - id: change_campaign_status_v5
    intent: Pause, resume or stop a published campaign (V5)
    question: How do I pause a published email campaign with the V5 API?
  - id: update_campaign
    intent: Update an API-created campaign (legacy)
    question: How do I update a campaign I created through the API on the legacy endpoint?
  - id: change_campaign_status
    intent: Stop, pause or resume several campaigns (legacy)
    question: Can I pause several API-created campaigns at once?
  - id: update_global_control_group
    intent: Add or remove users in the Global Control Group
    question: How do I add users to the Global Control Group so they're held out of campaigns?
  phrasing_ops: 5
  slug: moengage-update-campaigns-api
- baseURL: https://api-01.moengage.com/v1
  baseurl_source: declared
  description: Operations for creating, updating, retrieving, and managing user profiles.
  name: MoEngage User API
  phrasing_intents:
  - id: postCustomerByAppId
    intent: Create or update a user profile
    question: How do I create a new user or update their profile attributes?
  - id: postCustomersExport
    intent: Look up users by their IDs
    question: How do I fetch a user's profile details by their ID?
  - id: postCustomerMerge
    intent: Merge duplicate user profiles
    question: How do I combine two profiles that belong to the same person?
  - id: postCustomerDelete
    intent: Permanently delete a user
    question: How do I permanently delete a user from MoEngage?
  phrasing_ops: 4
  slug: moengage-user-api
- baseURL: https://api-01.moengage.com/v1
  baseurl_source: declared
  description: Utility endpoints for testing connections.
  name: MoEngage Utilities API
  phrasing_intents:
  - id: postIntegrationsAuthentication
    intent: Test an integration's connection credentials
    question: How do I check that my workspace ID and data key are valid before connecting?
  phrasing_ops: 1
  slug: moengage-utilities-api
artifact_total: 84
asyncapis:
- description: ''
  name: Moengage Webhooks
  slug: moengage-webhooks
collections:
- collection_type: open
  name: MoEngage Analytics Dashboard and Chart API
  slug: open-moengage-analytics
- collection_type: open
  name: MoEngage Business Events API
  slug: open-moengage-business-events
- collection_type: open
  name: MoEngage Campaigns API
  slug: open-moengage-campaign-draft
- collection_type: open
  name: MoEngage Campaigns API
  slug: open-moengage-campaigns
- collection_type: open
  name: MoEngage Cards API
  slug: open-moengage-cards
- collection_type: open
  name: MoEngage Catalog API
  slug: open-moengage-catalog
- collection_type: open
  name: Cohort Sync API
  slug: open-moengage-cohort-audience
- collection_type: open
  name: MoEngage Content Block API
  slug: open-moengage-content-blocks
- collection_type: open
  name: Coupon List API 🏷️
  slug: open-moengage-coupons
- collection_type: open
  name: MoEngage Segments API
  slug: open-moengage-custom-segments
- collection_type: open
  name: MoEngage Email Subscription Management APIs
  slug: open-moengage-email-subscription
- collection_type: open
  name: Email Templates API V1
  slug: open-moengage-email-templates-1
- collection_type: open
  name: Email Templates API V2
  slug: open-moengage-email-templates-2
- collection_type: open
  name: Flows
  slug: open-moengage-flows
- collection_type: open
  name: MoEngage GDPR / CCPA API
  slug: open-moengage-gdpr-ccpa
- collection_type: open
  name: MoEngage In-app Template API
  slug: open-moengage-in-app-templates
- collection_type: open
  name: MoEngage Inform API
  slug: open-moengage-inform
- collection_type: open
  name: MoEngage Broadcast Live Activities API
  slug: open-moengage-live-activities
- collection_type: open
  name: MoEngage Message Archival API
  slug: open-moengage-message-archival
- collection_type: open
  name: Offer Decisioning Public API - v5
  slug: open-moengage-offerings
- collection_type: open
  name: MoEngage On-Site Messaging (OSM) Template API
  slug: open-moengage-osm-templates
- collection_type: open
  name: Personalize APIs
  slug: open-moengage-personalize-experience
- collection_type: open
  name: Push Templates API
  slug: open-moengage-push-templates
- collection_type: open
  name: MoEngage Push API
  slug: open-moengage-push-v2-1
- collection_type: open
  name: MoEngage Push API
  slug: open-moengage-push
- collection_type: open
  name: MoEngage Recommendation API
  slug: open-moengage-recommendations
- collection_type: open
  name: MoEngage SMS Template API
  slug: open-moengage-sms-templates
- collection_type: open
  name: MoEngage Campaign Stats and Reports API
  slug: open-moengage-stats-report
- collection_type: open
  name: MoEngage Subscription Categories API
  slug: open-moengage-subscription-categories
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/moengage/refs/heads/main/capabilities/moengage-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/moengage-capability-edges.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/moengage/refs/heads/main/overlays/moengage-data-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/moengage-data-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/moengage/refs/heads/main/overlays/moengage-gdpr-ccpa-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/moengage-gdpr-ccpa-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/moengage/refs/heads/main/overlays/moengage-business-events-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/moengage-business-events-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/moengage/refs/heads/main/overlays/moengage-cohort-audience-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/moengage-cohort-audience-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/moengage/refs/heads/main/overlays/moengage-campaign-draft-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/moengage-campaign-draft-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/moengage/refs/heads/main/overlays/moengage-campaigns-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/moengage-campaigns-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/moengage/refs/heads/main/overlays/moengage-stats-report-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/moengage-stats-report-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/moengage/refs/heads/main/overlays/moengage-message-archival-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/moengage-message-archival-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/moengage/refs/heads/main/overlays/moengage-push-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/moengage-push-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/moengage/refs/heads/main/overlays/moengage-push-v2-1-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/moengage-push-v2-1-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/moengage/refs/heads/main/overlays/moengage-custom-segments-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/moengage-custom-segments-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/moengage/refs/heads/main/overlays/moengage-email-templates-1-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/moengage-email-templates-1-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/moengage/refs/heads/main/overlays/moengage-email-templates-2-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/moengage-email-templates-2-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/moengage/refs/heads/main/overlays/moengage-push-templates-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/moengage-push-templates-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/moengage/refs/heads/main/overlays/moengage-sms-templates-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/moengage-sms-templates-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/moengage/refs/heads/main/overlays/moengage-in-app-templates-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/moengage-in-app-templates-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/moengage/refs/heads/main/overlays/moengage-osm-templates-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/moengage-osm-templates-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/moengage/refs/heads/main/overlays/moengage-content-blocks-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/moengage-content-blocks-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/moengage/refs/heads/main/overlays/moengage-catalog-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/moengage-catalog-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/moengage/refs/heads/main/overlays/moengage-recommendations-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/moengage-recommendations-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/moengage/refs/heads/main/overlays/moengage-coupons-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/moengage-coupons-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/moengage/refs/heads/main/overlays/moengage-email-subscription-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/moengage-email-subscription-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/moengage/refs/heads/main/overlays/moengage-subscription-categories-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/moengage-subscription-categories-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/moengage/refs/heads/main/overlays/moengage-analytics-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/moengage-analytics-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/moengage/refs/heads/main/overlays/moengage-flows-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/moengage-flows-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/moengage/refs/heads/main/overlays/moengage-inform-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/moengage-inform-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/moengage/refs/heads/main/overlays/moengage-cards-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/moengage-cards-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/moengage/refs/heads/main/overlays/moengage-live-activities-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/moengage-live-activities-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/moengage/refs/heads/main/overlays/moengage-personalize-experience-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/moengage-personalize-experience-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/moengage/refs/heads/main/overlays/moengage-offerings-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/moengage-offerings-overlay.yaml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/moengage/refs/heads/main/security/moengage-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/moengage-vulnerability-disclosure.yml
- group: company
  title: ''
  type: Website
  url: https://www.moengage.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.moengage.com/docs/
- group: docs
  title: ''
  type: Documentation
  url: https://www.moengage.com/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://www.moengage.com/docs/api/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://www.moengage.com/docs/developer-guide/introduction
- group: operate
  title: ''
  type: Support
  url: https://help.moengage.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://www.moengage.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/moengage
- group: commercial
  title: ''
  type: Pricing
  url: https://www.moengage.com/plans-and-pricing/
- group: start
  title: ''
  type: SignUp
  url: https://www.moengage.com/request-demo/
- group: start
  title: ''
  type: Login
  url: https://dashboard.moengage.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.moengage.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.moengage.com/privacy-policy/
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/moengage-dev/api-docs/documentation/p593wcu/moengage-data-apis
- group: operate
  title: ''
  type: StatusPage
  url: https://status.moengage.com/
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.moengage.com/
- group: auth
  title: ''
  type: Compliance
  url: https://trust.moengage.com/
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/moengage/refs/heads/main/changelog/moengage-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/moengage-changelog.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/moengage/refs/heads/main/llms/moengage-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/moengage-llms.txt
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/moengage/refs/heads/main/packages/moengage-packages.yml
  title: ''
  type: Packages
  url: packages/moengage-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/moengage/refs/heads/main/packages/moengage-packages.yml
  title: ''
  type: SDKs
  url: packages/moengage-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/moengage/refs/heads/main/well-known/moengage-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/moengage-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/moengage/refs/heads/main/authentication/moengage-authentication.yml
  title: ''
  type: Authentication
  url: authentication/moengage-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/moengage/refs/heads/main/scopes/moengage-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/moengage-scopes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/moengage/refs/heads/main/conventions/moengage-conventions.yml
  title: ''
  type: Conventions
  url: conventions/moengage-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/moengage/refs/heads/main/conventions/moengage-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/moengage-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/moengage/refs/heads/main/errors/moengage-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/moengage-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/moengage/refs/heads/main/lifecycle/moengage-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/moengage-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/moengage/refs/heads/main/conformance/moengage-conformance.yml
  title: ''
  type: Conformance
  url: conformance/moengage-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/moengage/refs/heads/main/data-model/moengage-data-model.yml
  title: ''
  type: DataModel
  url: data-model/moengage-data-model.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/moengage/refs/heads/main/rate-limits/moengage-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/moengage-rate-limits.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/moengage/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/moengage/refs/heads/main/security/moengage-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/moengage-domain-security.yml
- group: auth
  title: ''
  type: Security
  url: https://www.moengage.com/responsible-disclosure/
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/moengage/refs/heads/main/mcp/moengage-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/moengage-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/moengage/refs/heads/main/mcp/moengage-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/moengage-tool-crosswalk.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/moengage/refs/heads/main/sandbox/moengage-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/moengage-sandbox.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/moengage/refs/heads/main/plans/moengage-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/moengage-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/moengage/refs/heads/main/asyncapi/moengage-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/moengage-webhooks.yml
created: '2026-08-01'
description: MoEngage is an insights-led customer engagement and cross-channel marketing automation platform used by consumer brands to unify customer data, segment audiences, and orchestrate personalized messaging across push notifications, email, SMS, WhatsApp, in-app messages, on-site messaging, app inbox cards, and web push. The platform exposes a broad REST API surface across seven regional data centers (DC-01 through DC-06 and DC-101) covering user and event ingestion, bulk import, business events, GDPR/CCPA data requests, campaign creation and lifecycle management, file- and filter-based segments, cohort sync, content blocks and channel templates, product catalogs, recommendations, coupon lists, offer decisioning, subscription and opt-in preferences, transactional alerts (Inform), iOS Live Activities, personalization experiences, campaign statistics, message archival, and custom analytics dashboards. MoEngage also ships native mobile and web SDKs for Android, iOS, Web, React Native,
  Flutter, Unity, Cordova and Capacitor, and operates a hosted, OAuth-secured Model Context Protocol (MCP) server so AI assistants can draft campaigns, manage segments and flows, and analyze performance conversationally.
image: https://www.moengage.com/wp-content/uploads/2023/03/MoEngage-Logo.svg
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.moengage.com; 44 tools listed.
  name: MoEngage MCP Server
  slug: moengage-mcp-yml
modified: '2026-08-14'
name: MoEngage
nav: Providers
network: true
overview: 'MoEngage publishes 46 APIs on the [APIs.io](https://apis.io/) network, including Bulk API, Business Events API, Campaign Reports API, and 43 more. Tagged areas include Customer Engagement, Marketing Automation, Customer Data Platform, Push Notifications, and Email.


  The MoEngage catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  MoEngage''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 64 more developer resources.'
plans:
- name: Moengage Plans Pricing
  plan_count: 4
  slug: moengage-plans-pricing
random_paper: 21
rate_limits:
- limit_count: 0
  name: Moengage Rate Limits
  slug: moengage-rate-limits
scopes:
- name: Moengage Scopes
  scope_count: 5
  slug: moengage-scopes
  summary_line: 5 scopes
score:
  band: exemplar
  composite: 69.0
  coverage:
    artifact_dirs: 25
    catalog_earned: 52.0
    catalog_earned_first_party: 12.0
    catalog_gap: 63.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.6
  facets:
    access_clarity: 92.1
    contract_governance: 18.2
    contract_quality: 62.0
    developer_ergonomics: 75.6
    discoverability: 80.0
    operational_transparency: 52.6
  previous_composite: 73.6
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 45
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: ccpa
    jurisdictions_satisfied: 2
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 44.2
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/moengage/refs/heads/main/screenshots/moengage-2026-08-07T184040.png
security:
- kind: authentication
  name: Moengage Authentication
  slug: moengage-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Moengage Domain Security
  slug: moengage-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Moengage Vulnerability Disclosure
  slug: moengage-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Moengage Trust Center
  slug: moengage-trust-center
  summary_line: SOC 2 Type 2, CSA STAR Level 2, ISO/IEC 27001:2022, ISO/IEC 27701:2019, ISO 22301:2019, HIPAA, GDPR, CCPA
slug: moengage
tags:
- Customer Engagement
- Marketing Automation
- Customer Data Platform
- Push Notifications
- Email
- SMS
- WhatsApp
- In-App Messaging
- Segmentation
- Personalization
- Campaign Management
- Analytics
- Mobile SDK
- MCP
- MarTech
website: https://www.moengage.com/
---
