---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: true
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
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 47.9
  scored_at: '2026-10-03'
api_count: 78
apis:
- description: The Creative External API uploads creative assets and publishes ads to ad networks programmatically, bypassing the AppsFlyer Creative Dashboard UI. It is asynchronous — a batch is submitted for upload
  name: Creative External API
  slug: creative-external-api
- description: AppsFlyer's hosted Model Context Protocol server exposes AppsFlyer's unified marketing data to LLM clients and agents over an OAuth 2.1 authorization-code + PKCE flow with dynamic client registration,
  name: AppsFlyer MCP Server
  slug: appsflyer-mcp-server
- baseURL: https://hq1.appsflyer.com/api/
  baseurl_source: declared
  description: The Account connections API from AppsFlyer — 1 operation(s) for account connections.
  name: AppsFlyer Account connections API
  phrasing_intents:
  - id: getConnections
    intent: List the account's audience partner connections
    question: Which ad partners is my account connected to for sending audiences?
  phrasing_ops: 1
  slug: appsflyer-account-connections-api
- baseURL: https://hq1.appsflyer.com/api/
  baseurl_source: declared
  description: The Account Integration API from AppsFlyer — 1 operation(s) for account integration.
  name: AppsFlyer Account Integration API
  phrasing_intents:
  - id: getIntegrations
    intent: List the account's audience integrations
    question: What audience integrations are configured on my account?
  - id: postIntegrations
    intent: Set the account's audience integrations
    question: Can I add or change an audience partner integration from the API?
  phrasing_ops: 2
  slug: appsflyer-account-integration-api
- baseURL: https://hq1.appsflyer.com/api/
  baseurl_source: declared
  description: The Account splits API from AppsFlyer — 1 operation(s) for account splits.
  name: AppsFlyer Account splits API
  phrasing_intents:
  - id: getSplitSyncs
    intent: Get the account's audience split percentages
    question: How is my account splitting audiences across partners by percentage?
  phrasing_ops: 1
  slug: appsflyer-account-splits-api
- baseURL: https://hq1.appsflyer.com/api/
  baseurl_source: declared
  description: The Active audiences API from AppsFlyer — 1 operation(s) for active audiences.
  name: AppsFlyer Active audiences API
  phrasing_intents:
  - id: audience-external-active-audiences
    intent: List the account's active audiences
    question: Which audiences are currently active on my AppsFlyer account?
  phrasing_ops: 1
  slug: appsflyer-active-audiences-api
- baseURL: https://hq1.appsflyer.com/api/
  baseurl_source: declared
  description: The Active integrations API from AppsFlyer — 2 operation(s) for active integrations.
  name: AppsFlyer Active integrations API
  phrasing_intents:
  - id: getV1IntegrationsByAppid
    intent: Get active integration parameters for an app
    question: What parameters are set on the integration tab for each active partner of one app?
  - id: getV1Integrations
    intent: List active partner integrations by app
    question: Which partners are active across all my apps?
  phrasing_ops: 2
  slug: appsflyer-active-integrations-api
- baseURL: https://hq1.appsflyer.com/api/
  baseurl_source: declared
  description: The Ad Revenue raw data API from AppsFlyer — 3 operation(s) for ad revenue raw data.
  name: AppsFlyer Ad Revenue raw data API
  phrasing_intents:
  - id: getByAppIdAdRevenueOrganicRawV5
    intent: Pull organic ad revenue raw data
    question: How much ad revenue are my organic users generating, row by row?
  - id: getByAppIdAdRevenueRawRetargetV5
    intent: Pull retargeting ad revenue raw data
    question: What ad revenue did re-engaged users generate during the re-engagement window?
  - id: getByAppIdAdRevenueRawV5
    intent: Pull attributed ad revenue raw data
    question: Which media sources brought users who generate ad revenue?
  phrasing_ops: 3
  slug: appsflyer-ad-revenue-raw-data-api
- baseURL: https://hq1.appsflyer.com/api/
  baseurl_source: declared
  description: The Add excluded app API from AppsFlyer — 1 operation(s) for add excluded app.
  name: AppsFlyer Add excluded app API
  phrasing_intents:
  - id: click-signing-config-excluded-apps-add
    intent: Exclude an app from click signing
    question: Can I exempt one of my apps from click signature verification?
  phrasing_ops: 1
  slug: appsflyer-add-excluded-app-api
- baseURL: https://hq1.appsflyer.com/api/
  baseurl_source: declared
  description: The Aggregate (user acquisition and retargeting) API from AppsFlyer — 5 operation(s) for aggregate (user acquisition and retargeting).
  name: AppsFlyer Aggregate (user acquisition and retargeting) API
  phrasing_intents:
  - id: getByAppIdDailyReportV5
    intent: Get the daily aggregate performance report
    question: How do I get day-by-day installs and cost per campaign, without in-app events?
  - id: getByAppIdGeoByDateReportV5
    intent: Get the geo-by-date aggregate report
    question: Can I break down campaign performance by country for each day?
  - id: getByAppIdGeoReportV5
    intent: Get the geo aggregate report
    question: What is campaign performance per country across a whole date range?
  - id: getByAppIdPartnersByDateReportV5
    intent: Get the partners-by-date aggregate report
    question: How did each ad partner perform on each day of the period?
  - id: getByAppIdPartnersReportV5
    intent: Get the partners aggregate report
    question: Which media sources and campaigns delivered the best LTV overall?
  phrasing_ops: 5
  slug: appsflyer-aggregate-user-acquisition-and-retargeting-api
- baseURL: https://hq1.appsflyer.com/api/
  baseurl_source: declared
  description: The Allowed devices API from AppsFlyer — 2 operation(s) for allowed devices.
  name: AppsFlyer Allowed devices API
  phrasing_intents:
  - id: test-console-api-delete
    intent: Remove a test device from an app
    question: How do I take a registered test device off my app?
  - id: test-console-api-post
    intent: Register a test device for an app
    question: How do I register a phone as a test device for my app?
  phrasing_ops: 2
  slug: appsflyer-allowed-devices-api
- baseURL: https://hq1.appsflyer.com/api/
  baseurl_source: declared
  description: The Android deep linking request API from AppsFlyer — 1 operation(s) for android deep linking request.
  name: AppsFlyer Android deep linking request API
  phrasing_intents:
  - id: postAndroidByAppId
    intent: Resolve a deep link for an Android app open
    question: How do I get deep link data for an Android install without the SDK?
  phrasing_ops: 1
  slug: appsflyer-android-deep-linking-request-api
- baseURL: https://hq1.appsflyer.com/api/
  baseurl_source: declared
  description: The App management API from AppsFlyer — 2 operation(s) for app management.
  name: AppsFlyer App management API
  phrasing_intents:
  - id: app-mng-v2-delete
    intent: Delete an app from the account
    question: How do I remove an app from my AppsFlyer account?
  - id: app-mng-v2-put
    intent: Update an app's attribution settings
    question: How do I turn on IP masking for an existing app in AppsFlyer?
  - id: app-mng-v2-post
    intent: Add a new app to the account
    question: What call adds a brand-new app to my account?
  phrasing_ops: 3
  slug: appsflyer-app-management-api
- baseURL: https://hq1.appsflyer.com/api/
  baseurl_source: declared
  description: The Audience connections API from AppsFlyer — 1 operation(s) for audience connections.
  name: AppsFlyer Audience connections API
  phrasing_intents:
  - id: getAudienceByAudienceIdConnections
    intent: List an audience's partner connections
    question: Which partners is this audience being sent to?
  - id: putAudienceByAudienceIdConnections
    intent: Connect an audience to existing partners
    question: How do I start sending an audience to partners I already connected?
  phrasing_ops: 2
  slug: appsflyer-audience-connections-api
- baseURL: https://hq1.appsflyer.com/api/
  baseurl_source: declared
  description: The Audience split API from AppsFlyer — 1 operation(s) for audience split.
  name: AppsFlyer Audience split API
  phrasing_intents:
  - id: getAudienceByAudienceIdSplitSyncs
    intent: Get an audience's split percentages
    question: What percentage of this audience goes to each partner?
  - id: putAudienceByAudienceIdSplitSyncs
    intent: Update an audience's split percentages
    question: How do I rebalance how an audience is divided between partners?
  phrasing_ops: 2
  slug: appsflyer-audience-split-api
- baseURL: https://hq1.appsflyer.com/api/
  baseurl_source: declared
  description: The Audience upload API from AppsFlyer — 1 operation(s) for audience upload.
  name: AppsFlyer Audience upload API
  phrasing_intents:
  - id: postAudienceByAudienceIdUploadNow
    intent: Upload an audience to partners now
    question: Can I push an audience to its partners immediately instead of waiting for the schedule?
  phrasing_ops: 1
  slug: appsflyer-audience-upload-api
- baseURL: https://hq1.appsflyer.com/api/
  baseurl_source: declared
  description: The Audiences User Attribution Import API API from AppsFlyer — 1 operation(s) for audiences user attribution import api.
  name: AppsFlyer Audiences User Attribution Import API
  phrasing_intents:
  - id: audiences-user-attr-import-post
    intent: Import user attributes for audiences
    question: How do I send custom user attributes into my audiences?
  phrasing_ops: 1
  slug: appsflyer-audiences-user-attribution-import-api-api
- baseURL: https://hq1.appsflyer.com/api/
  baseurl_source: declared
  description: The Audit logs API from AppsFlyer — 1 operation(s) for audit logs.
  name: AppsFlyer Audit logs API
  phrasing_intents:
  - id: audit-public-api-get
    intent: Read the account's audit logs
    question: Who changed settings in my AppsFlyer account last week?
  phrasing_ops: 1
  slug: appsflyer-audit-logs-api
- baseURL: https://hq1.appsflyer.com/api/
  baseurl_source: declared
  description: The Authentication Token API from AppsFlyer — 1 operation(s) for authentication token.
  name: AppsFlyer Authentication Token API
  phrasing_intents:
  - id: deleteTokensAppByAppId
    intent: Delete the Push API authentication token
    question: Can I remove the auth token from my app's Push API messages?
  - id: putTokensAppByAppId
    intent: Set the Push API authentication token
    question: How do I add an auth header to Push API messages sent to my endpoint?
  phrasing_ops: 2
  slug: appsflyer-authentication-token-api
- baseURL: https://hq1.appsflyer.com/api/
  baseurl_source: declared
  description: The Circuit breaker API from AppsFlyer — 1 operation(s) for circuit breaker.
  name: AppsFlyer Circuit breaker API
  phrasing_intents:
  - id: click-signing-config-circuit-breaker-put
    intent: Toggle the click signing circuit breaker
    question: Can I switch off click signing enforcement quickly if something breaks?
  phrasing_ops: 1
  slug: appsflyer-circuit-breaker-api
- baseURL: https://hq1.appsflyer.com/api/
  baseurl_source: declared
  description: The Click Engagement API from AppsFlyer — 1 operation(s) for click engagement.
  name: AppsFlyer Click Engagement API
  phrasing_intents:
  - id: getClickAppByPlatformByAppId
    intent: Report a click engagement via GET
    question: How do I send a click to AppsFlyer as a query-string GET request?
  - id: postClickAppByPlatformByAppId
    intent: Report a click engagement via POST body
    question: Can I report ad clicks server to server with a JSON body?
  phrasing_ops: 2
  slug: appsflyer-click-engagement-api
- baseURL: https://hq1.appsflyer.com/api/
  baseurl_source: declared
  description: The Cohort Report API from AppsFlyer — 1 operation(s) for cohort report.
  name: AppsFlyer Cohort Report API
  phrasing_intents:
  - id: postByAppId
    intent: Create a cohort report
    question: How do I measure retention and revenue by install cohort?
  phrasing_ops: 1
  slug: appsflyer-cohort-report-api
- baseURL: https://hq1.appsflyer.com/api/
  baseurl_source: declared
  description: The Conversion Data for SDK attribution testing API from AppsFlyer — 1 operation(s) for conversion data for sdk attribution testing.
  name: AppsFlyer Conversion Data for SDK attribution testing API
  slug: appsflyer-conversion-data-for-sdk-attribution-testing-api
- baseURL: https://hq1.appsflyer.com/api/
  baseurl_source: declared
  description: The Conversion value (CV) schema API from AppsFlyer — 1 operation(s) for conversion value (cv) schema.
  name: AppsFlyer Conversion value (CV) schema API
  phrasing_intents:
  - id: skan-pull-cs-api-get
    intent: Get an app's conversion value schema
    question: Where can I pull the conversion value schema configured for my app?
  phrasing_ops: 1
  slug: appsflyer-conversion-value-cv-schema-api
- baseURL: https://hq1.appsflyer.com/api/
  baseurl_source: declared
  description: The Create audience API from AppsFlyer — 1 operation(s) for create audience.
  name: AppsFlyer Create audience API
  phrasing_intents:
  - id: postAudience
    intent: Create an imported audience
    question: Can I create a new audience that I upload users into later?
  phrasing_ops: 1
  slug: appsflyer-create-audience-api
- baseURL: https://hq1.appsflyer.com/api/
  baseurl_source: declared
  description: The Event Types API from AppsFlyer — 1 operation(s) for event types.
  name: AppsFlyer Event Types API
  phrasing_intents:
  - id: getEventTypesByAttributingEntity
    intent: List Push API event types for an endpoint type
    question: Which event types can be pushed for a given attributing entity?
  phrasing_ops: 1
  slug: appsflyer-event-types-api
- baseURL: https://hq1.appsflyer.com/api/
  baseurl_source: declared
  description: The Events API from AppsFlyer — 1 operation(s) for events.
  name: AppsFlyer Events API
  phrasing_intents:
  - id: test-console-api-get
    intent: Retrieve events from a test device
    question: How do I see the in-app events a test device sent?
  phrasing_ops: 1
  slug: appsflyer-events-api
- baseURL: https://hq1.appsflyer.com/api/
  baseurl_source: declared
  description: The Events management API from AppsFlyer — 2 operation(s) for events management.
  name: AppsFlyer Events management API
  phrasing_intents:
  - id: web-s2s-api-event-post
    intent: Send a server-to-server web event
    question: How do I send a web event from my server for a site bundle?
  - id: web-s2s-api-setcuid-post
    intent: Link a customer user ID to a web user
    question: How do I match my own customer ID to a website visitor's AppsFlyer user ID?
  phrasing_ops: 2
  slug: appsflyer-events-management-api
- baseURL: https://hq1.appsflyer.com/api/
  baseurl_source: declared
  description: The Freshness Report API from AppsFlyer — 1 operation(s) for freshness report.
  name: AppsFlyer Freshness Report API
  phrasing_intents:
  - id: master-lastupdate
    intent: Check when report data was last updated
    question: How fresh is my report data right now?
  phrasing_ops: 1
  slug: appsflyer-freshness-report-api
- baseURL: https://hq1.appsflyer.com/api/
  baseurl_source: declared
  description: The Generate secret key API from AppsFlyer — 1 operation(s) for generate secret key.
  name: AppsFlyer Generate secret key API
  phrasing_intents:
  - id: click-signing-secret-post
    intent: Generate a click signing secret key
    question: How do I create a new secret key for signing clicks?
  phrasing_ops: 1
  slug: appsflyer-generate-secret-key-api
- baseURL: https://hq1.appsflyer.com/api/
  baseurl_source: declared
  description: The Get app list API from AppsFlyer — 1 operation(s) for get app list.
  name: AppsFlyer Get app list API
  phrasing_intents:
  - id: app-list-ad-nets-api-get
    intent: List apps integrated with the ad network
    question: Which advertiser apps am I integrated with as an ad network?
  phrasing_ops: 1
  slug: appsflyer-get-app-list-api
- baseURL: https://hq1.appsflyer.com/api/
  baseurl_source: declared
  description: The Get config API from AppsFlyer — 1 operation(s) for get config.
  name: AppsFlyer Get config API
  phrasing_intents:
  - id: click-signing-config-get
    intent: Get the click signing configuration
    question: What is my current click signing configuration?
  phrasing_ops: 1
  slug: appsflyer-get-config-api
- baseURL: https://hq1.appsflyer.com/api/
  baseurl_source: declared
  description: The Google Play install referrer API from AppsFlyer — 1 operation(s) for google play install referrer.
  name: AppsFlyer Google Play install referrer API
  phrasing_intents:
  - id: postV1IntegrationParams
    intent: Set the Google Play install referrer decryption key
    question: Where do I give AppsFlyer the install referrer decryption key for my Android app?
  phrasing_ops: 1
  slug: appsflyer-google-play-install-referrer-api
- baseURL: https://hq1.appsflyer.com/api/
  baseurl_source: declared
  description: The Import audience API from AppsFlyer — 1 operation(s) for import audience.
  name: AppsFlyer Import audience API
  phrasing_intents:
  - id: audience-import-post
    intent: Add, remove or overwrite devices in an audience
    question: How do I upload a list of device IDs into an audience?
  phrasing_ops: 1
  slug: appsflyer-import-audience-api
- baseURL: https://hq1.appsflyer.com/api/
  baseurl_source: declared
  description: The Impression Engagement API from AppsFlyer — 1 operation(s) for impression engagement.
  name: AppsFlyer Impression Engagement API
  phrasing_intents:
  - id: getImpressionAppByPlatformByAppId
    intent: Report an ad impression via GET
    question: How do I report an ad view to AppsFlyer as a query-string GET request?
  - id: postImpressionAppByPlatformByAppId
    intent: Report an ad impression via POST body
    question: Can I log view-through impressions server to server with a JSON body?
  phrasing_ops: 2
  slug: appsflyer-impression-engagement-api
- baseURL: https://hq1.appsflyer.com/api/
  baseurl_source: declared
  description: The Inapp Events API from AppsFlyer — 1 operation(s) for inapp events.
  name: AppsFlyer Inapp Events API
  phrasing_intents:
  - id: postInappeventByAppId
    intent: Send a server-side in-app event
    question: Can my server send purchases that happen outside the app to AppsFlyer?
  phrasing_ops: 1
  slug: appsflyer-inapp-events-api
- baseURL: https://hq1.appsflyer.com/api/
  baseurl_source: declared
  description: The InCost job status API from AppsFlyer — 1 operation(s) for incost job status.
  name: AppsFlyer InCost job status API
  phrasing_intents:
  - id: incost-jobstatus-get
    intent: Check the status of a cost upload job
    question: Did my cost data upload finish processing?
  phrasing_ops: 1
  slug: appsflyer-incost-job-status-api
- baseURL: https://hq1.appsflyer.com/api/
  baseurl_source: declared
  description: The InCost uploader API from AppsFlyer — 1 operation(s) for incost uploader.
  name: AppsFlyer InCost uploader API
  phrasing_intents:
  - id: incost-uploader-post
    intent: Upload ad cost data for an app
    question: How do I send my own ad spend data into AppsFlyer for an app?
  phrasing_ops: 1
  slug: appsflyer-incost-uploader-api
- baseURL: https://hq1.appsflyer.com/api/
  baseurl_source: declared
  description: The Integration settings API from AppsFlyer — 2 operation(s) for integration settings.
  name: AppsFlyer Integration settings API
  phrasing_intents:
  - id: postCopy
    intent: Copy integration settings (deprecated endpoint)
    question: Is the old copy endpoint for partner integration settings still available?
  - id: postV1Copy
    intent: Copy partner integration settings between apps
    question: Can I copy a partner's integration setup from one app to another on the same platform?
  phrasing_ops: 2
  slug: appsflyer-integration-settings-api
- baseURL: https://hq1.appsflyer.com/api/
  baseurl_source: declared
  description: The iOS deep linking request API from AppsFlyer — 1 operation(s) for ios deep linking request.
  name: AppsFlyer iOS deep linking request API
  phrasing_intents:
  - id: postIosByAppId
    intent: Resolve a deep link for an iOS app open
    question: How do I get deep link data for an iOS install without the SDK?
  phrasing_ops: 1
  slug: appsflyer-ios-deep-linking-request-api
- baseURL: https://hq1.appsflyer.com/api/
  baseurl_source: declared
  description: The Manage Push API configuration API from AppsFlyer — 1 operation(s) for manage push api configuration.
  name: AppsFlyer Manage Push API configuration API
  phrasing_intents:
  - id: getAppByAppId
    intent: View an app's Push API configuration
    question: Which endpoints is my app currently pushing raw attribution data to?
  - id: putAppByAppId
    intent: Update an app's Push API endpoints
    question: How do I change where AppsFlyer pushes real-time attribution messages for my app?
  phrasing_ops: 2
  slug: appsflyer-manage-push-api-configuration-api
- baseURL: https://hq1.appsflyer.com/api/
  baseurl_source: declared
  description: The Managing roles API from AppsFlyer — 1 operation(s) for managing roles.
  name: AppsFlyer Managing roles API
  phrasing_intents:
  - id: getRoles
    intent: List account roles and their users
    question: Who in my account has which role?
  phrasing_ops: 1
  slug: appsflyer-managing-roles-api
- baseURL: https://hq1.appsflyer.com/api/
  baseurl_source: declared
  description: The Managing users in bulk API from AppsFlyer — 2 operation(s) for managing users in bulk.
  name: AppsFlyer Managing users in bulk API
  phrasing_intents:
  - id: bulk-users-delete
    intent: Delete several account users at once
    question: How do I remove multiple team members from my account in one go?
  - id: bulk-users-get
    intent: List the account's users
    question: Who has access to my AppsFlyer account?
  - id: bulk-users-post
    intent: Create many account users at once
    question: What call lets me add a batch of new users to my account?
  phrasing_ops: 3
  slug: appsflyer-managing-users-in-bulk-api
- baseURL: https://hq1.appsflyer.com/api/
  baseurl_source: declared
  description: The Measure first app opens API from AppsFlyer — 1 operation(s) for measure first app opens.
  name: AppsFlyer Measure first app opens API
  phrasing_intents:
  - id: postFirstOpenAppByPlatformByAppId
    intent: Measure a first app open on a CTV device
    question: Can I report a first open of my connected TV app server to server?
  phrasing_ops: 1
  slug: appsflyer-measure-first-app-opens-api
- baseURL: https://hq1.appsflyer.com/api/
  baseurl_source: declared
  description: The Measure in-app events API from AppsFlyer — 1 operation(s) for measure in-app events.
  name: AppsFlyer Measure in-app events API
  phrasing_intents:
  - id: postInappAppByPlatformByAppId
    intent: Measure an in-app event on a CTV app
    question: Can a post-install event in my TV app be attributed to a campaign?
  phrasing_ops: 1
  slug: appsflyer-measure-in-app-events-api
- baseURL: https://hq1.appsflyer.com/api/
  baseurl_source: declared
  description: The Measure sessions API from AppsFlyer — 1 operation(s) for measure sessions.
  name: AppsFlyer Measure sessions API
  phrasing_intents:
  - id: postSessionAppByPlatformByAppId
    intent: Measure a session on a CTV app
    question: Can I report a post-install session for my connected TV app?
  phrasing_ops: 1
  slug: appsflyer-measure-sessions-api
- baseURL: https://hq1.appsflyer.com/api/
  baseurl_source: declared
  description: The Message Fields API from AppsFlyer — 1 operation(s) for message fields.
  name: AppsFlyer Message Fields API
  phrasing_intents:
  - id: getFieldsByPlatform
    intent: List Push API message fields for a platform
    question: Which fields can a Push API message include for iOS or Android?
  phrasing_ops: 1
  slug: appsflyer-message-fields-api
- baseURL: https://hq1.appsflyer.com/api/
  baseurl_source: declared
  description: The OneLink REST API v2.0 API from AppsFlyer — 4 operation(s) for onelink rest api v2.0.
  name: AppsFlyer OneLink REST API v2.0 API
  phrasing_intents:
  - id: delete-onelink-v2-link
    intent: Delete a OneLink short link
    question: How do I delete a OneLink short link I no longer need?
  - id: get-onelink-v2-link
    intent: Get a OneLink short link's data
    question: How do I look up the parameters behind an existing OneLink short link?
  - id: update-onelink-v2-link
    intent: Update an existing OneLink short link
    question: Can I change the parameters of a OneLink short link I already created?
  - id: get-onelink-v2-link-qr
    intent: Get a QR code for a OneLink short link
    question: Can I generate a QR code for one of my OneLink short links?
  - id: get-onelink-v2-link-quota
    intent: Check the account's short link quota
    question: How many OneLink short links do I have left in my quota?
  - id: onelink-v2-create-link
    intent: Create a OneLink short link
    question: How do I create a new OneLink short link from my template?
  phrasing_ops: 6
  slug: appsflyer-onelink-rest-api-v2-0-api
- baseURL: https://hq1.appsflyer.com/api/
  baseurl_source: declared
  description: The Pauses audience API from AppsFlyer — 1 operation(s) for pauses audience.
  name: AppsFlyer Pauses audience API
  phrasing_intents:
  - id: audience-external-pause
    intent: Pause one or more audiences
    question: How do I pause an audience so it stops syncing?
  phrasing_ops: 1
  slug: appsflyer-pauses-audience-api
- baseURL: https://hq1.appsflyer.com/api/
  baseurl_source: declared
  description: The Postbacks API from AppsFlyer — 4 operation(s) for postbacks.
  name: AppsFlyer Postbacks API
  phrasing_intents:
  - id: getByAppIdInAppEventsPostbacksV5
    intent: Pull in-app event postback records
    question: Which in-app event postbacks did AppsFlyer send to my ad networks?
  - id: getByAppIdPostbacksV5
    intent: Pull install postback records
    question: What install postbacks were sent to media sources for my app?
  - id: getByAppIdRetargetInAppEventsPostbacksV5
    intent: Pull retargeting in-app event postbacks
    question: Which event postbacks went out for users in a re-engagement window?
  - id: getByAppIdRetargetInstallPostbacksV5
    intent: Pull retargeting conversion postbacks
    question: Which retargeting conversion postbacks were sent to networks?
  phrasing_ops: 4
  slug: appsflyer-postbacks-api
- baseURL: https://hq1.appsflyer.com/api/
  baseurl_source: declared
  description: The Production API from AppsFlyer — 7 operation(s) for production.
  name: AppsFlyer Production API
  phrasing_intents:
  - id: cancel-opendsr-request
    intent: Cancel a pending OpenDSR request
    question: Can I cancel a GDPR request after submitting it?
  - id: get-opendsr-request-status
    intent: Check an OpenDSR request's status
    question: What is the status of the GDPR data subject request I submitted?
  - id: create-batch-opendsr-requests
    intent: Submit a batch of OpenDSR requests
    question: How do I submit many GDPR deletion requests in a single call?
  - id: create-opendsr-request
    intent: Submit a single OpenDSR request
    question: How do I submit a GDPR erasure request for one user?
  - id: discovery
    intent: Get OpenDSR discovery metadata
    question: Which subject identity types and request types does the GDPR API support?
  - id: download-report
    intent: Download a completed access request report
    question: Where do I download the report for a finished GDPR access request?
  - id: get-batch-status
    intent: Check statuses of an OpenDSR batch
    question: What is the status of each request in my GDPR batch?
  - id: get-certificate
    intent: Download the OpenDSR signing certificate
    question: How do I verify the signature on OpenDSR responses?
  phrasing_ops: 8
  slug: appsflyer-production-api
- baseURL: https://hq1.appsflyer.com/api/
  baseurl_source: declared
  description: The Protect360 fraud API from AppsFlyer — 6 operation(s) for protect360 fraud.
  name: AppsFlyer Protect360 fraud API
  phrasing_intents:
  - id: getByAppIdBlockedClicksReportV5
    intent: Pull clicks blocked by Protect360
    question: Which clicks did Protect360 block as fraud?
  - id: getByAppIdBlockedInAppEventsReportV5
    intent: Pull in-app events blocked as fraud
    question: Which in-app events were flagged fraudulent and blocked?
  - id: getByAppIdBlockedInstallPostbacksV5
    intent: Pull postbacks for blocked installs
    question: What postbacks were sent to networks about installs we blocked?
  - id: getByAppIdBlockedInstallsReportV5
    intent: Pull installs blocked as fraud
    question: How many installs were blocked as fraud and left unattributed?
  - id: getByAppIdDetectionV5
    intent: Pull post-attribution fraud installs
    question: Which installs were attributed first and later found to be fraudulent?
  - id: getByAppIdFraudPostInappsV5
    intent: Pull post-attribution fraud in-app events
    question: Which in-app events belong to installs judged fraudulent after attribution?
  phrasing_ops: 6
  slug: appsflyer-protect360-fraud-api
- baseURL: https://hq1.appsflyer.com/api/
  baseurl_source: declared
  description: The Raw data reports (non-organic) API from AppsFlyer — 4 operation(s) for raw data reports (non-organic).
  name: AppsFlyer Raw data reports (non-organic) API
  phrasing_intents:
  - id: getByAppIdInAppEventsReportV5
    intent: Pull non-organic in-app events raw data
    question: What in-app events did users from paid media sources perform?
  - id: getByAppIdInstallsReportV5
    intent: Pull non-organic installs raw data
    question: Which installs came from paid media sources, user by user?
  - id: getByAppIdReinstallsV5
    intent: Pull non-organic reinstalls raw data
    question: Which users reinstalled after engaging with a user acquisition campaign?
  - id: getByAppIdUninstallEventsReportV5
    intent: Pull non-organic uninstalls raw data
    question: How many users from paid campaigns uninstalled my app?
  phrasing_ops: 4
  slug: appsflyer-raw-data-reports-non-organic-api
- baseURL: https://hq1.appsflyer.com/api/
  baseurl_source: declared
  description: The Raw data reports (organic) API from AppsFlyer — 4 operation(s) for raw data reports (organic).
  name: AppsFlyer Raw data reports (organic) API
  phrasing_intents:
  - id: getByAppIdOrganicInAppEventsReportV5
    intent: Pull organic in-app events raw data
    question: What in-app events did organic users perform?
  - id: getByAppIdOrganicInstallsReportV5
    intent: Pull organic installs raw data
    question: Which installs came without any media source?
  - id: getByAppIdOrganicUninstallEventsReportV5
    intent: Pull organic uninstalls raw data
    question: How many organic users uninstalled my app?
  - id: getByAppIdReinstallsOrganicV5
    intent: Pull organic reinstalls raw data
    question: Which organic users uninstalled and later installed again?
  phrasing_ops: 4
  slug: appsflyer-raw-data-reports-organic-api
- baseURL: https://hq1.appsflyer.com/api/
  baseurl_source: declared
  description: The Remove excluded app API from AppsFlyer — 1 operation(s) for remove excluded app.
  name: AppsFlyer Remove excluded app API
  phrasing_intents:
  - id: click-signing-config-excluded-apps-delete
    intent: Remove an app from the click signing exclusions
    question: How do I put an excluded app back under click signature verification?
  phrasing_ops: 1
  slug: appsflyer-remove-excluded-app-api
- baseURL: https://hq1.appsflyer.com/api/
  baseurl_source: declared
  description: The Report API from AppsFlyer — 1 operation(s) for report.
  name: AppsFlyer Report API
  phrasing_intents:
  - id: click-signing-report-get
    intent: Get a click signing report
    question: How many clicks passed or failed signature checks in a given window?
  phrasing_ops: 1
  slug: appsflyer-report-api
- baseURL: https://hq1.appsflyer.com/api/
  baseurl_source: declared
  description: The Retargeting API from AppsFlyer — 2 operation(s) for retargeting.
  name: AppsFlyer Retargeting API
  phrasing_intents:
  - id: getByAppIdInAppEventsRetargetV5
    intent: Pull retargeting in-app events raw data
    question: What did re-engaged users do in the app during the re-engagement window?
  - id: getByAppIdInstallsRetargetV5
    intent: Pull retargeting conversions raw data
    question: How many users re-engaged or reinstalled from a retargeting campaign?
  phrasing_ops: 2
  slug: appsflyer-retargeting-api
- baseURL: https://hq1.appsflyer.com/api/
  baseurl_source: declared
  description: The Revoke secret key API from AppsFlyer — 1 operation(s) for revoke secret key.
  name: AppsFlyer Revoke secret key API
  phrasing_intents:
  - id: click-signing-secret-delete
    intent: Revoke a click signing secret key
    question: How do I revoke a click signing secret that leaked?
  phrasing_ops: 1
  slug: appsflyer-revoke-secret-key-api
- baseURL: https://hq1.appsflyer.com/api/
  baseurl_source: declared
  description: The SKAN conversion studio API API from AppsFlyer — 1 operation(s) for skan conversion studio api.
  name: AppsFlyer SKAN conversion studio API
  phrasing_intents:
  - id: skan-studio-duplicate-config
    intent: Copy a SKAN schema between apps
    question: Can I reuse one app's SKAN conversion value schema on another app?
  - id: skan-studio-read-config
    intent: Get an app's SKAN conversion schema
    question: What SKAN conversion schema have I configured for this app?
  phrasing_ops: 2
  slug: appsflyer-skan-conversion-studio-api-api
- baseURL: https://hq1.appsflyer.com/api/
  baseurl_source: declared
  description: The SKAN CV schema API for ad networks API from AppsFlyer — 2 operation(s) for skan cv schema api for ad networks.
  name: AppsFlyer SKAN CV schema API for ad networks API
  phrasing_intents:
  - id: get-conversion-value-mapping-schema
    intent: Get SKAN 3 conversion value schemas
    question: As an ad network, how do I fetch advertisers' SKAN 3 conversion value mappings?
  - id: get-conversion-value-mapping-schema-v2
    intent: Get SKAN 4 conversion value schemas
    question: Where do I get the SKAN 4 conversion value schema with its postback windows?
  phrasing_ops: 2
  slug: appsflyer-skan-cv-schema-api-for-ad-networks-api
- baseURL: https://hq1.appsflyer.com/api/
  baseurl_source: declared
  description: The SKAN performance report API from AppsFlyer — 1 operation(s) for skan performance report.
  name: AppsFlyer SKAN performance report API
  phrasing_intents:
  - id: skan-agg-performance-report-api-get
    intent: Get a SKAN aggregated performance report
    question: How do my SKAdNetwork installs perform over a date range?
  phrasing_ops: 1
  slug: appsflyer-skan-performance-report-api
- baseURL: https://hq1.appsflyer.com/api/
  baseurl_source: declared
  description: The Store commission rates API from AppsFlyer — 2 operation(s) for store commission rates.
  name: AppsFlyer Store commission rates API
  phrasing_intents:
  - id: deleteStoreCommissionRatesAppByAppIds
    intent: Reset store commission rates to defaults
    question: How do I remove a custom store commission rate and go back to the default?
  - id: getStoreCommissionRatesAppByAppIds
    intent: Get store commission rates for apps
    question: What store commission rate is applied to my apps' revenue?
  - id: postStoreCommissionRates
    intent: Create or update store commission rates
    question: Can I set a different store commission rate per app based on its store program?
  phrasing_ops: 3
  slug: appsflyer-store-commission-rates-api
- baseURL: https://hq1.appsflyer.com/api/
  baseurl_source: declared
  description: The Stub & Testing API from AppsFlyer — 7 operation(s) for stub & testing.
  name: AppsFlyer Stub & Testing API
  slug: appsflyer-stub-testing-api
- baseURL: https://hq1.appsflyer.com/api/
  baseurl_source: declared
  description: The Tax rate rules API from AppsFlyer — 1 operation(s) for tax rate rules.
  name: AppsFlyer Tax rate rules API
  phrasing_intents:
  - id: getTaxRatesAppByAppId
    intent: Look up an app's tax rate catalog
    question: Which tax rates apply to my app's revenue in a given country?
  - id: postTaxRatesAppByAppId
    intent: Create custom tax rate rules for an app
    question: How do I set my own tax rate for an app in a specific country?
  phrasing_ops: 2
  slug: appsflyer-tax-rate-rules-api
- baseURL: https://hq1.appsflyer.com/api/
  baseurl_source: declared
  description: The Test API from AppsFlyer — 1 operation(s) for test.
  name: AppsFlyer Test API
  phrasing_intents:
  - id: click-signing-test-post
    intent: Test a signed click URL
    question: How can I check whether a signed click URL passes verification?
  phrasing_ops: 1
  slug: appsflyer-test-api
- baseURL: https://hq1.appsflyer.com/api/
  baseurl_source: declared
  description: The Unique partner integration parameters API from AppsFlyer — 1 operation(s) for unique partner integration parameters.
  name: AppsFlyer Unique partner integration parameters API
  phrasing_intents:
  - id: getV1PartnerParamsByPidByPlatform
    intent: List a partner's unique integration parameters
    question: What unique parameters does a partner need for an integration on a platform?
  phrasing_ops: 1
  slug: appsflyer-unique-partner-integration-parameters-api
- baseURL: https://hq1.appsflyer.com/api/
  baseurl_source: declared
  description: The Update config API from AppsFlyer — 1 operation(s) for update config.
  name: AppsFlyer Update config API
  phrasing_intents:
  - id: click-signing-config-update-put
    intent: Set the click signing mode for a signature version
    question: How do I change the click signing verification mode for one signature version?
  phrasing_ops: 1
  slug: appsflyer-update-config-api
- baseURL: https://hq1.appsflyer.com/api/
  baseurl_source: declared
  description: The URL Validation API from AppsFlyer — 1 operation(s) for url validation.
  name: AppsFlyer URL Validation API
  phrasing_intents:
  - id: postValidateUrl
    intent: Validate a Push API endpoint URL
    question: Can I test whether my endpoint is reachable before using it for Push API?
  phrasing_ops: 1
  slug: appsflyer-url-validation-api
artifact_total: 115
asyncapis:
- description: ''
  name: Appsflyer Push Api Webhooks
  slug: appsflyer-push-api-webhooks
collections:
- collection_type: open
  name: Additional Identifiers API
  slug: open-appsflyer-additional-identifiers-api
- collection_type: open
  name: AdRevenue Account Integrations API
  slug: open-appsflyer-adrevenue-account-integrations-api
- collection_type: open
  name: Aggregate Pull API V1 Token
  slug: open-appsflyer-aggregate-pull-api-v1-token
- collection_type: open
  name: Aggregate Pull API V2 Token
  slug: open-appsflyer-aggregate-pull-api-v2-token
- collection_type: open
  name: App list API
  slug: open-appsflyer-app-list-api
- collection_type: open
  name: App management API V2.0
  slug: open-appsflyer-app-management-api-v20
- collection_type: open
  name: Audience External API
  slug: open-appsflyer-audience-external-api
- collection_type: open
  name: Audience Import API
  slug: open-appsflyer-audience-import-api
- collection_type: open
  name: Audiences User Attribution Import API
  slug: open-appsflyer-audiences-user-attribution-import-api
- collection_type: open
  name: Audit Public API
  slug: open-appsflyer-audit-public-api
- collection_type: open
  name: Click Signing API
  slug: open-appsflyer-click-signing-api
- collection_type: open
  name: Cohort API
  slug: open-appsflyer-cohort-api
- collection_type: open
  name: Deep linking REST API
  slug: open-appsflyer-deep-linking-rest-api
- collection_type: open
  name: Engagements API
  slug: open-appsflyer-engagements-api
- collection_type: open
  name: GCD API for SDK attribution testing
  slug: open-appsflyer-gcd-api-for-sdk-attribution-testing-1
- collection_type: open
  name: InCost API
  slug: open-appsflyer-incost-api-1
- collection_type: open
  name: '[Legacy] Server-to-server events API (for mobile)'
  slug: open-appsflyer-legacy-server-to-server-events-api-for-mobile
- collection_type: open
  name: Master API
  slug: open-appsflyer-master-api
- collection_type: open
  name: Master freshness API
  slug: open-appsflyer-master-freshness-api
- collection_type: open
  name: OneLink API v2.0
  slug: open-appsflyer-onelink-api-v20
- collection_type: open
  name: OpenDSR API
  slug: open-appsflyer-opendsr-api
- collection_type: open
  name: Partner integration settings API
  slug: open-appsflyer-partner-integration-settings-api
- collection_type: open
  name: PC/Console/CTV Client-app Events API
  slug: open-appsflyer-pcconsolectv-client-app-events-api
- collection_type: open
  name: PC/Console/CTV Events API
  slug: open-appsflyer-pcconsolectv-events-api
- collection_type: open
  name: Preload C2S Measurement API
  slug: open-appsflyer-preload-c2s-measurement-api
- collection_type: open
  name: Preload Measurement API
  slug: open-appsflyer-preload-measurement-api-1
- collection_type: open
  name: Push API Configuration API
  slug: open-appsflyer-push-api-configuration-api
- collection_type: open
  name: Raw Data Pull API V1 Token
  slug: open-appsflyer-raw-data-pull-api-v1-token
- collection_type: open
  name: Raw Data Pull API V2 Token
  slug: open-appsflyer-raw-data-pull-api-v2-token
- collection_type: open
  name: ROI360 Net Revenue API (v2.0)
  slug: open-appsflyer-roi360-net-revenue-api-v20
- collection_type: open
  name: Server-to-server events API (for mobile)
  slug: open-appsflyer-server-to-server-events-api-for-mobile
- collection_type: open
  name: SKAN aggregated performance report API
  slug: open-appsflyer-skan-aggregated-performance-report-api
- collection_type: open
  name: SKAN aggregated postback by arrival date API
  slug: open-appsflyer-skan-aggregated-postback-by-arrival-date-api
- collection_type: open
  name: SKAN conversion studio API
  slug: open-appsflyer-skan-conversion-studio-api
- collection_type: open
  name: SKAN CV schema API for ad networks
  slug: open-appsflyer-skan-cv-schema-api-for-ad-networks-2
- collection_type: open
  name: SKAN CV Schema API for Advertisers
  slug: open-appsflyer-skan-cv-schema-api-for-advertisers-1
- collection_type: open
  name: Test Console API
  slug: open-appsflyer-test-console-api
- collection_type: open
  name: User management
  slug: open-appsflyer-user-management
- collection_type: open
  name: WEB Server-TO-Server API
  slug: open-appsflyer-web-server-to-server-api
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/appsflyer/refs/heads/main/capabilities/appsflyer-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/appsflyer-capability-edges.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/appsflyer/refs/heads/main/overlays/appsflyer-raw-data-pull-api-v2-token-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/appsflyer-raw-data-pull-api-v2-token-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/appsflyer/refs/heads/main/overlays/appsflyer-raw-data-pull-api-v1-token-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/appsflyer-raw-data-pull-api-v1-token-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/appsflyer/refs/heads/main/overlays/appsflyer-aggregate-pull-api-v2-token-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/appsflyer-aggregate-pull-api-v2-token-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/appsflyer/refs/heads/main/overlays/appsflyer-aggregate-pull-api-v1-token-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/appsflyer-aggregate-pull-api-v1-token-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/appsflyer/refs/heads/main/overlays/appsflyer-master-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/appsflyer-master-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/appsflyer/refs/heads/main/overlays/appsflyer-master-freshness-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/appsflyer-master-freshness-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/appsflyer/refs/heads/main/overlays/appsflyer-cohort-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/appsflyer-cohort-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/appsflyer/refs/heads/main/overlays/appsflyer-server-to-server-events-api-for-mobile-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/appsflyer-server-to-server-events-api-for-mobile-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/appsflyer/refs/heads/main/overlays/appsflyer-legacy-server-to-server-events-api-for-mobile-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/appsflyer-legacy-server-to-server-events-api-for-mobile-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/appsflyer/refs/heads/main/overlays/appsflyer-web-server-to-server-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/appsflyer-web-server-to-server-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/appsflyer/refs/heads/main/overlays/appsflyer-pcconsolectv-events-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/appsflyer-pcconsolectv-events-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/appsflyer/refs/heads/main/overlays/appsflyer-pcconsolectv-client-app-events-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/appsflyer-pcconsolectv-client-app-events-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/appsflyer/refs/heads/main/overlays/appsflyer-engagements-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/appsflyer-engagements-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/appsflyer/refs/heads/main/overlays/appsflyer-deep-linking-rest-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/appsflyer-deep-linking-rest-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/appsflyer/refs/heads/main/overlays/appsflyer-preload-measurement-api-1-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/appsflyer-preload-measurement-api-1-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/appsflyer/refs/heads/main/overlays/appsflyer-preload-c2s-measurement-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/appsflyer-preload-c2s-measurement-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/appsflyer/refs/heads/main/overlays/appsflyer-gcd-api-for-sdk-attribution-testing-1-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/appsflyer-gcd-api-for-sdk-attribution-testing-1-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/appsflyer/refs/heads/main/overlays/appsflyer-app-management-api-v20-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/appsflyer-app-management-api-v20-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/appsflyer/refs/heads/main/overlays/appsflyer-app-list-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/appsflyer-app-list-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/appsflyer/refs/heads/main/overlays/appsflyer-user-management-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/appsflyer-user-management-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/appsflyer/refs/heads/main/overlays/appsflyer-audit-public-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/appsflyer-audit-public-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/appsflyer/refs/heads/main/overlays/appsflyer-partner-integration-settings-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/appsflyer-partner-integration-settings-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/appsflyer/refs/heads/main/overlays/appsflyer-adrevenue-account-integrations-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/appsflyer-adrevenue-account-integrations-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/appsflyer/refs/heads/main/overlays/appsflyer-incost-api-1-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/appsflyer-incost-api-1-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/appsflyer/refs/heads/main/overlays/appsflyer-test-console-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/appsflyer-test-console-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/appsflyer/refs/heads/main/overlays/appsflyer-push-api-configuration-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/appsflyer-push-api-configuration-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/appsflyer/refs/heads/main/overlays/appsflyer-audience-external-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/appsflyer-audience-external-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/appsflyer/refs/heads/main/overlays/appsflyer-audience-import-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/appsflyer-audience-import-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/appsflyer/refs/heads/main/overlays/appsflyer-audiences-user-attribution-import-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/appsflyer-audiences-user-attribution-import-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/appsflyer/refs/heads/main/overlays/appsflyer-additional-identifiers-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/appsflyer-additional-identifiers-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/appsflyer/refs/heads/main/overlays/appsflyer-onelink-api-v20-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/appsflyer-onelink-api-v20-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/appsflyer/refs/heads/main/overlays/appsflyer-skan-aggregated-performance-report-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/appsflyer-skan-aggregated-performance-report-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/appsflyer/refs/heads/main/overlays/appsflyer-skan-aggregated-postback-by-arrival-date-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/appsflyer-skan-aggregated-postback-by-arrival-date-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/appsflyer/refs/heads/main/overlays/appsflyer-skan-cv-schema-api-for-advertisers-1-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/appsflyer-skan-cv-schema-api-for-advertisers-1-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/appsflyer/refs/heads/main/overlays/appsflyer-skan-cv-schema-api-for-ad-networks-2-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/appsflyer-skan-cv-schema-api-for-ad-networks-2-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/appsflyer/refs/heads/main/overlays/appsflyer-skan-conversion-studio-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/appsflyer-skan-conversion-studio-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/appsflyer/refs/heads/main/overlays/appsflyer-opendsr-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/appsflyer-opendsr-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/appsflyer/refs/heads/main/overlays/appsflyer-click-signing-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/appsflyer-click-signing-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/appsflyer/refs/heads/main/overlays/appsflyer-roi360-net-revenue-api-v20-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/appsflyer-roi360-net-revenue-api-v20-overlay.yaml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/appsflyer/refs/heads/main/security/appsflyer-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/appsflyer-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/appsflyer/refs/heads/main/authentication/appsflyer-authentication.yml
  title: ''
  type: Authentication
  url: authentication/appsflyer-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.appsflyer.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dev.appsflyer.com/hc
- group: docs
  title: ''
  type: Documentation
  url: https://dev.appsflyer.com/hc/docs
- group: docs
  title: ''
  type: APIReference
  url: https://dev.appsflyer.com/hc/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://dev.appsflyer.com/hc/docs/getting-started
- group: operate
  title: ''
  type: Support
  url: https://support.appsflyer.com/hc/en-us
- group: operate
  title: ''
  type: HelpCenter
  url: https://support.appsflyer.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://www.appsflyer.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AppsFlyerSDK
- group: commercial
  title: ''
  type: Pricing
  url: https://www.appsflyer.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://www.appsflyer.com/start/
- group: start
  title: ''
  type: Login
  url: https://hq1.appsflyer.com/auth/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.appsflyer.com/legal/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.appsflyer.com/legal/services-privacy-policy/
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.appsflyer.com/product-news/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.appsflyer.com/
- group: auth
  title: ''
  type: TrustCenter
  url: https://www.appsflyer.com/trust/
- group: auth
  title: ''
  type: Compliance
  url: https://www.appsflyer.com/trust/security/
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/appsflyer/refs/heads/main/packages/appsflyer-packages.yml
  title: ''
  type: Packages
  url: packages/appsflyer-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/appsflyer/refs/heads/main/packages/appsflyer-packages.yml
  title: ''
  type: SDKs
  url: packages/appsflyer-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/appsflyer/refs/heads/main/well-known/appsflyer-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/appsflyer-well-known.yml
- group: other
  title: ''
  type: APICatalog
  url: https://dev.appsflyer.com/.well-known/api-catalog
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/appsflyer/refs/heads/main/mcp/appsflyer-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/appsflyer-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/appsflyer/refs/heads/main/mcp/appsflyer-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/appsflyer-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/appsflyer/refs/heads/main/llms/appsflyer-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/appsflyer-llms.txt
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/appsflyer/refs/heads/main/conformance/appsflyer-conformance.yml
  title: ''
  type: Conformance
  url: conformance/appsflyer-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/appsflyer/refs/heads/main/errors/appsflyer-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/appsflyer-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/appsflyer/refs/heads/main/lifecycle/appsflyer-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/appsflyer-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/appsflyer/refs/heads/main/conventions/appsflyer-conventions.yml
  title: ''
  type: Conventions
  url: conventions/appsflyer-conventions.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/appsflyer/refs/heads/main/sandbox/appsflyer-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/appsflyer-sandbox.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/appsflyer/refs/heads/main/changelog/appsflyer-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/appsflyer-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/appsflyer/refs/heads/main/components/appsflyer-components.yml
  title: ''
  type: Components
  url: components/appsflyer-components.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/appsflyer/refs/heads/main/data-model/appsflyer-data-model.yml
  title: ''
  type: DataModel
  url: data-model/appsflyer-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/appsflyer/refs/heads/main/asyncapi/appsflyer-push-api-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/appsflyer-push-api-webhooks.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/appsflyer/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/appsflyer/refs/heads/main/security/appsflyer-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/appsflyer-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/appsflyer/refs/heads/main/security/appsflyer-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/appsflyer-trust-center.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/appsflyer/refs/heads/main/plans/appsflyer-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/appsflyer-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/appsflyer/refs/heads/main/rate-limits/appsflyer-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/appsflyer-rate-limits.yml
created: '2026-07-31'
description: 'AppsFlyer is a mobile marketing analytics and attribution platform used by app marketers to measure, attribute and optimize user acquisition across mobile, web, CTV, console and PC. Its developer surface spans mobile and platform SDKs (iOS, Android, Unity, React Native, Flutter, Cordova, Unreal, Roku, Tizen, webOS) and a large REST API estate published on the AppsFlyer developer hub: Pull APIs for raw and aggregate report export, the Master and Cohort reporting APIs, server-to-server and client-to-server event ingestion APIs, the OneLink deep-linking API, audience import/activation APIs, SKAdNetwork conversion-value and postback APIs, app and user management APIs, the Protect360 click-signing anti-fraud API, the ROI360 net-revenue API, and an OpenDSR privacy-request API. AppsFlyer also runs a Push API webhook surface for real-time postbacks and a hosted Model Context Protocol (MCP) server for agent access.'
image: https://www.appsflyer.com/wp-content/uploads/2020/08/appsflyer-logo.svg
layout: provider
mcp_servers:
- description: ''
  name: AppsFlyer MCP Server
  slug: appsflyer-mcp-server
modified: '2026-08-13'
name: AppsFlyer
nav: Providers
network: true
overview: 'AppsFlyer publishes 68 APIs on the [APIs.io](https://apis.io/) network, including Account connections API, Account Integration API, Account splits API, and 65 more. Tagged areas include Company, Mobile Attribution, Marketing Analytics, Mobile Measurement, and Deep Linking.


  The AppsFlyer catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  AppsFlyer''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 74 more developer resources.'
plans:
- name: Appsflyer Plans Pricing
  plan_count: 3
  slug: appsflyer-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 11
  name: Appsflyer Rate Limits
  slug: appsflyer-rate-limits
score:
  band: exemplar
  composite: 67.7
  coverage:
    artifact_dirs: 25
    catalog_earned: 64.0
    catalog_earned_first_party: 24.0
    catalog_gap: 51.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.5
  facets:
    access_clarity: 92.1
    contract_governance: 4.5
    contract_quality: 56.1
    developer_ergonomics: 58.9
    discoverability: 89.3
    operational_transparency: 73.7
  previous_composite: 67.2
  provenance:
    conformance: derived
    contracts:
      callable: 98.5
      derived: 0
      marker_coverage: 0.0
      total: 66
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: ccpa
    - jurisdiction: US
      standard: coppa
    jurisdictions_satisfied: 2
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 35.3
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  trend: flat
  upsert:
    applies: true
    score: 22.2
screenshot: https://raw.githubusercontent.com/api-evangelist/appsflyer/refs/heads/main/screenshots/appsflyer-2026-08-07T161507.png
security:
- kind: authentication
  name: Appsflyer Authentication
  slug: appsflyer-authentication
  summary_line: apiKey/http · 4 schemes
- kind: domain-security
  name: Appsflyer Domain Security
  slug: appsflyer-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Appsflyer Vulnerability Disclosure
  slug: appsflyer-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Appsflyer Trust Center
  slug: appsflyer-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, ISO 27032, ISO 27701, CSA STAR, TrustArc Enterprise Privacy Certification, PRIVO (GDPR + COPPA), EU-US Data Privacy Framework
slug: appsflyer
tags:
- Company
- Mobile Attribution
- Marketing Analytics
- Mobile Measurement
- Deep Linking
- Audiences
- Ad Fraud Prevention
- SKAdNetwork
- Privacy
- AdTech
- Mobile SDK
- AI Agents
website: https://www.appsflyer.com/
---
