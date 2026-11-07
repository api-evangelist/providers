---
access_model:
  confidence: high
  label: Open source · Free On-Premise · Paid Cloud · Public demo instance
  onboarding: self-serve
  pricing: freemium
  public: true
  source:
  - plans
  - authentication
  - sandbox
  trial: true
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: templated
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 37.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Matomo Agentic Access
  operation_count: 560
  slug: matomo-agentic-access
  summary_line: 560 operations · 2 acting
api_count: 61
apis:
- baseURL: https://{matomo_host}/index.php
  baseurl_source: declared
  description: The single /index.php dispatch entrypoint through which every Matomo Reporting API method is invoked, by supplying module=API and method=Module.Action. This entry documents the entrypoint contract its
  name: Matomo Reporting API (index.php entrypoint)
  phrasing_intents:
  - id: API.getMatomoVersion
    intent: Get the installed Matomo version
    question: Which Matomo version is this server running?
  - id: API.getPhpVersion
    intent: Get the server's PHP version
    question: What PHP version is the analytics server using?
  - id: API.getIpFromHeader
    intent: See the IP address the server detects for me
    question: What IP address does the server think I'm calling from?
  - id: API.getSegmentsMetadata
    intent: List all available segment dimensions
    question: Which dimensions can I segment my reports by?
  - id: API.getMetadata
    intent: Describe a single API report method
    question: What metrics and dimensions does a specific report method return?
  - id: API.getReportMetadata
    intent: List metadata for all available reports
    question: What reports can I pull from this analytics instance?
  - id: API.getProcessedReport
    intent: Get a formatted report with metadata
    question: Can I fetch a report already formatted, with processed metrics and column labels?
  - id: API.getReportPagesMetadata
    intent: List the dashboard UI pages and their widgets
    question: Which pages does the reporting UI have, and what widgets sit on each?
  phrasing_ops: 19
  slug: matomo-index-php-api
- baseURL: https://{matomo_host}/matomo.php
  baseurl_source: declared
  description: The Matomo Tracking API — the server-side ingest entrypoint at /matomo.php that records pageviews, events, goals, ecommerce orders, site searches and content interactions. It is the counterpart to the
  name: Matomo Tracking API (matomo.php entrypoint)
  phrasing_intents:
  - id: trackEventGet
    intent: Record one tracking hit via the URL
    question: How do I record a pageview from my server by calling the tracking URL?
  - id: trackEventPost
    intent: Send tracking hits in bulk via POST
    question: Can I send hundreds of tracking requests in one HTTP call?
  phrasing_ops: 2
  slug: matomo-matomo-php-api
- baseURL: https://{matomo_host}/index.php
  baseurl_source: declared
  description: 'The Actions API lets you request reports for all your Visitor Actions: Page URLs, Page titles, Events, Content Tracking, File Downloads and Clicks on external websites. For example, "getPageTitles" wi'
  name: Matomo Actions API
  phrasing_intents:
  - id: Actions.get
    intent: Get overall action metrics for a period
    question: How many pageviews, downloads and outlinks did my site get last month?
  - id: Actions.getPageUrls
    intent: Report traffic per page URL
    question: Which pages on my site get the most pageviews?
  - id: Actions.getPageUrlsFollowingSiteSearch
    intent: Report page URLs visited after site search
    question: Which pages do people open right after using my site search?
  - id: Actions.getPageTitlesFollowingSiteSearch
    intent: Report page titles visited after site search
    question: Which page titles do visitors view immediately after searching my site?
  - id: Actions.getEntryPageUrls
    intent: Report entry page URLs
    question: Which URLs do visitors land on first when they arrive?
  - id: Actions.getExitPageUrls
    intent: Report exit page URLs
    question: Which page URLs do visitors leave my site from?
  - id: Actions.getPageUrl
    intent: Get metrics for one page URL
    question: How many views did one specific page URL get?
  - id: Actions.getPageTitles
    intent: Report traffic per page title
    question: Which page titles get the most views on my site?
  phrasing_ops: 18
  slug: matomo-actions-api
- baseURL: https://{matomo_host}/index.php
  baseurl_source: declared
  description: Exposes API endpoints for managing advertising conversion export configurations. These methods let users list, inspect, create, update, and delete configured exports and access tokens.
  name: Matomo Advertising Conversion Export API
  phrasing_intents:
  - id: AdvertisingConversionExport.getConversionExports
    intent: List advertising conversion exports
    question: Which ad conversion exports have been set up for my sites?
  - id: AdvertisingConversionExport.getConversionExport
    intent: Get one conversion export's configuration
    question: What settings does a specific conversion export use?
  - id: AdvertisingConversionExport.deleteConversionExport
    intent: Delete a conversion export
    question: How do I remove an ad conversion export I no longer need?
  - id: AdvertisingConversionExport.addConversionExport
    intent: Create an advertising conversion export
    question: How do I set up an export of conversions to upload to an ad platform?
  - id: AdvertisingConversionExport.regenerateAccessToken
    intent: Regenerate a conversion export's access token
    question: How do I invalidate the download link for a conversion export?
  - id: AdvertisingConversionExport.updateConversionExport
    intent: Update a conversion export
    question: How do I change the parameters of an existing conversion export?
  phrasing_ops: 6
  slug: matomo-advertisingconversionexport-api
- baseURL: https://{matomo_host}/index.php
  baseurl_source: declared
  description: Provides API methods to create, update, delete, and query annotations.
  name: Matomo Annotations API
  phrasing_intents:
  - id: Annotations.add
    intent: Add an annotation to a site's timeline
    question: How do I note a campaign launch on my traffic graph in Matomo?
  - id: Annotations.save
    intent: Edit an existing annotation
    question: Can I fix the text or date of an annotation I already added?
  - id: Annotations.delete
    intent: Delete one annotation
    question: How do I remove a single annotation from a site?
  - id: Annotations.deleteAll
    intent: Delete every annotation on a site
    question: Can I wipe all annotations for a website at once?
  - id: Annotations.get
    intent: Get a single annotation
    question: What does a specific annotation say?
  - id: Annotations.getAll
    intent: List annotations for a date range
    question: What annotations were added for my site last month?
  - id: Annotations.getAnnotationCountForDates
    intent: Count annotations per period
    question: How many annotations, and how many starred ones, exist for each day this month?
  phrasing_ops: 7
  slug: matomo-annotations-api
- baseURL: https://{matomo_host}/index.php
  baseurl_source: declared
  description: Exposes reporting API endpoints for aggregated bandwidth metrics.
  name: Matomo Bandwidth API
  phrasing_intents:
  - id: Bandwidth.get
    intent: Get bandwidth metrics for a site and period
    question: How much bandwidth did my site's pageviews and downloads use last month?
  phrasing_ops: 1
  slug: matomo-bandwidth-api
- baseURL: https://{matomo_host}/index.php
  baseurl_source: declared
  description: Exposes cohort reports grouped by the period of a visitor's first visit. These endpoints transform archived first-visit cohort data into table and chart responses for the Cohorts plugin.
  name: Matomo Cohorts API
  phrasing_intents:
  - id: Cohorts.getCohortsOverTime
    intent: Track chosen cohorts over a date range
    question: How did visitors who first arrived in January keep returning over the following months?
  - id: Cohorts.getCohorts
    intent: Get the cohort retention table for a period
    question: What does my visitor retention cohort table look like this month?
  phrasing_ops: 2
  slug: matomo-cohorts-api
- baseURL: https://{matomo_host}/index.php
  baseurl_source: declared
  description: The Contents API exposes content tracking reports grouped by content name and content piece.
  name: Matomo Contents API
  phrasing_intents:
  - id: Contents.getContentNames
    intent: Report content impressions by name
    question: How many impressions and interactions did each banner or content block get?
  - id: Contents.getContentPieces
    intent: Report content impressions by piece
    question: Which content pieces, like a specific image or ad creative, perform best?
  phrasing_ops: 2
  slug: matomo-contents-api
- baseURL: https://{matomo_host}/index.php
  baseurl_source: declared
  description: Provides administrative API methods for scheduling, archiving, tracking failures, and opt-out code generation.
  name: Matomo Core Admin Home API
  phrasing_intents:
  - id: CoreAdminHome.deleteAllTrackingFailures
    intent: Clear all tracking failures
    question: Can I clear every recorded tracking failure after fixing my setup?
  - id: CoreAdminHome.deleteTrackingFailure
    intent: Delete one tracking failure
    question: How do I dismiss a single tracking failure?
  - id: CoreAdminHome.getTrackingFailures
    intent: List tracking failures
    question: Are any tracking requests failing on my sites in Matomo?
  phrasing_ops: 3
  slug: matomo-coreadminhome-api
- baseURL: https://{matomo_host}/index.php
  baseurl_source: declared
  description: Exposes Crash Analytics endpoints for managing tracked crashes and querying crash reports. Includes summary, drill-down, historical, and realtime reporting APIs for a single site.
  name: Matomo Crash Analytics API
  phrasing_intents:
  - id: CrashAnalytics.mergeCrashes
    intent: Merge several crashes into one group
    question: Can I tell Matomo that several different crash entries are really the same bug?
  - id: CrashAnalytics.unmergeCrashGroup
    intent: Split a merged crash group apart
    question: How do I undo a crash merge I made by mistake?
  - id: CrashAnalytics.getCrashGroups
    intent: List merged crash groups for a site
    question: Which crashes have I already merged together on this site?
  - id: CrashAnalytics.getCrashTypes
    intent: List the distinct crash types tracked
    question: What kinds of crash types have been recorded for my site?
  - id: CrashAnalytics.setIgnoreCrash
    intent: Ignore or stop ignoring a crash
    question: Can I stop a noisy crash from being tracked anymore?
  - id: CrashAnalytics.getIgnoredCrashes
    intent: List crashes currently being ignored
    question: Which crashes have been muted from tracking on my site?
  - id: CrashAnalytics.getCrashSummary
    intent: Get details for a single crash
    question: What is the error message and source file behind a specific crash?
  - id: CrashAnalytics.getCrashVisitContext
    intent: See the visits that hit a crash
    question: What were users doing right before they hit a particular crash?
  phrasing_ops: 31
  slug: matomo-crashanalytics-api
- baseURL: https://{matomo_host}/index.php
  baseurl_source: declared
  description: Exposes Custom Alerts API endpoints for managing alert definitions and reading triggered alert data. These methods let callers create, update, fetch, delete, and evaluate alerts for one or more sites.
  name: Matomo Custom Alerts API
  phrasing_intents:
  - id: CustomAlerts.getValuesForAlertInPast
    intent: Get an alert's computed value for a past period
    question: What value did my alert's metric have for each site in an earlier period?
  - id: CustomAlerts.getAlert
    intent: Get one custom alert
    question: What conditions is a specific custom alert set to trigger on?
  - id: CustomAlerts.getAlerts
    intent: List custom alerts for sites
    question: What custom alerts are configured on my websites?
  - id: CustomAlerts.addAlert
    intent: Create a custom alert
    question: How do I get emailed when visits drop by more than 20 percent?
  - id: CustomAlerts.editAlert
    intent: Update an existing custom alert
    question: How do I change the threshold on an alert I already created?
  - id: CustomAlerts.deleteAlert
    intent: Delete a custom alert
    question: How do I stop and remove an alert I no longer need?
  - id: CustomAlerts.getTriggeredAlerts
    intent: List alerts that have fired
    question: Which of my alerts have actually triggered recently?
  phrasing_ops: 7
  slug: matomo-customalerts-api
- baseURL: https://{matomo_host}/index.php
  baseurl_source: declared
  description: The Custom Dimensions API lets you manage and access reports for your configured Custom Dimensions.
  name: Matomo Custom Dimensions API
  phrasing_intents:
  - id: CustomDimensions.getCustomDimension
    intent: Get the report for a custom dimension
    question: What values did visitors have for my custom dimension, like membership tier, last month?
  - id: CustomDimensions.configureNewCustomDimension
    intent: Create a new custom dimension
    question: How do I add a custom dimension to track something like user type?
  - id: CustomDimensions.configureExistingCustomDimension
    intent: Update an existing custom dimension
    question: Do I need to resend every value when I update a custom dimension?
  - id: CustomDimensions.getConfiguredCustomDimensions
    intent: List configured custom dimensions
    question: Which custom dimensions are set up on my site?
  - id: CustomDimensions.getAvailableScopes
    intent: List scopes and remaining dimension slots
    question: How many custom dimension slots do I have left on a site?
  - id: CustomDimensions.getAvailableExtractionDimensions
    intent: List dimensions usable in extraction rules
    question: What can a custom dimension extract its value from, like the page URL?
  phrasing_ops: 6
  slug: matomo-customdimensions-api
- baseURL: https://{matomo_host}/index.php
  baseurl_source: declared
  description: Provides API methods for custom JavaScript tracker configuration.
  name: Matomo Custom Js Tracker API
  phrasing_intents:
  - id: CustomJsTracker.doesIncludePluginTrackersAutomatically
    intent: Check if plugin trackers auto-include in matomo.js
    question: Will plugin tracker code be bundled into matomo.js automatically?
  phrasing_ops: 1
  slug: matomo-customjstracker-api
- baseURL: https://{matomo_host}/index.php
  baseurl_source: declared
  description: The Dashboard API lets you manage user dashboards and retrieve their widget configurations.
  name: Matomo Dashboard API
  phrasing_intents:
  - id: Dashboard.getDashboards
    intent: List a user's dashboards and widgets
    question: Which dashboards does a user have, and what widgets are on them?
  - id: Dashboard.createNewDashboardForUser
    intent: Create a dashboard for a user
    question: How do I create a new dashboard for a teammate?
  - id: Dashboard.removeDashboard
    intent: Remove a dashboard
    question: Can I delete a dashboard I no longer use?
  - id: Dashboard.copyDashboardToUser
    intent: Copy a dashboard to another user
    question: Can I share one of my dashboards by copying it to a colleague?
  - id: Dashboard.resetDashboardLayout
    intent: Reset a dashboard to the default layout
    question: How do I restore a messy dashboard to its default widgets?
  phrasing_ops: 5
  slug: matomo-dashboard-api
- baseURL: https://{matomo_host}/index.php
  baseurl_source: declared
  description: The DevicePlugins API lets you access reports about device plugins such as browser plugins.
  name: Matomo Device Plugins API
  phrasing_intents:
  - id: DevicePlugins.getPlugin
    intent: Report browser plugins detected on visitors
    question: Which browser plugins do my visitors have installed?
  phrasing_ops: 1
  slug: matomo-deviceplugins-api
- baseURL: https://{matomo_host}/index.php
  baseurl_source: declared
  description: The DevicesDetection API lets you access reports about your visitors' device types, brands, models, operating systems, and browsers.
  name: Matomo Devices Detection API
  phrasing_intents:
  - id: DevicesDetection.getType
    intent: Report visits by device type
    question: How much of my traffic comes from phones versus desktops?
  - id: DevicesDetection.getBrand
    intent: Report visits by device brand
    question: Which device manufacturers do my visitors use most?
  - id: DevicesDetection.getModel
    intent: Report visits by device model
    question: Which specific phone models are visiting my site?
  - id: DevicesDetection.getOsFamilies
    intent: Report visits by operating system
    question: What operating systems do my visitors use?
  - id: DevicesDetection.getOsVersions
    intent: Report visits by OS version
    question: Which operating system versions are my visitors running?
  - id: DevicesDetection.getBrowsers
    intent: Report visits by browser
    question: Which browsers do my visitors use, ignoring version numbers?
  - id: DevicesDetection.getBrowserVersions
    intent: Report visits by browser version
    question: Which specific browser versions visit my site?
  - id: DevicesDetection.getBrowserEngines
    intent: Report visits by browser engine
    question: Which rendering engines like Blink, Gecko or WebKit do my visitors use?
  phrasing_ops: 8
  slug: matomo-devicesdetection-api
- baseURL: https://{matomo_host}/index.php
  baseurl_source: declared
  description: The Events API lets you request reports about your users' Custom Events. Events are tracked using the Javascript Tracker trackEvent() function, or using the [Tracking HTTP API](https://developer.matom
  name: Matomo Events API
  phrasing_intents:
  - id: Events.getCategory
    intent: Report events by category
    question: Which event categories were triggered most on my site?
  - id: Events.getAction
    intent: Report events by action
    question: Which event actions, like play or download, happen most often?
  - id: Events.getName
    intent: Report events by name
    question: Which event names were recorded most on my site?
  - id: Events.getActionFromCategoryId
    intent: Drill into the actions within an event category
    question: Which actions happened inside one particular event category?
  - id: Events.getNameFromCategoryId
    intent: Drill into the names within an event category
    question: Which event names were recorded inside one event category?
  - id: Events.getCategoryFromActionId
    intent: Drill into the categories for an event action
    question: Which event categories does a particular event action appear in?
  - id: Events.getNameFromActionId
    intent: Drill into the names for an event action
    question: Which event names were recorded with one particular action?
  - id: Events.getActionFromNameId
    intent: Drill into the actions for an event name
    question: Which actions were recorded with one particular event name?
  phrasing_ops: 9
  slug: matomo-events-api
- baseURL: https://{matomo_host}/index.php
  baseurl_source: declared
  description: Provides API methods for submitting product feedback and managing feedback reminders.
  name: Matomo Feedback API
  phrasing_intents:
  - id: Feedback.sendFeedbackForFeature
    intent: Send feedback about a feature
    question: How can I tell the Matomo team whether I like a particular feature?
  - id: Feedback.sendFeedbackForSurvey
    intent: Answer a feedback survey question
    question: How do I respond to an in-app survey question?
  - id: Feedback.updateFeedbackReminderDate
    intent: Postpone the feedback reminder
    question: Can I stop the feedback prompt from appearing for a while?
  phrasing_ops: 3
  slug: matomo-feedback-api
- baseURL: https://{matomo_host}/index.php
  baseurl_source: declared
  description: Exposes the Form Analytics API for managing tracked forms and retrieving form performance reports. Use these endpoints to create, update, archive, and delete configured forms, inspect form metadata, a
  name: Matomo Form Analytics API
  phrasing_intents:
  - id: FormAnalytics.addForm
    intent: Start tracking a new form
    question: How do I set up a new form to track in Matomo Form Analytics?
  - id: FormAnalytics.updateForm
    intent: Edit a tracked form's settings
    question: Can I rename a form I'm already tracking or change its matching rules?
  - id: FormAnalytics.getForm
    intent: Get one tracked form's configuration
    question: What rules and settings does a specific tracked form have?
  - id: FormAnalytics.getForms
    intent: List all tracked forms on a site
    question: Which forms are being tracked on my website?
  - id: FormAnalytics.getFormsByStatuses
    intent: List tracked forms by status
    question: Can I see only the archived forms, or only the running ones?
  - id: FormAnalytics.deleteForm
    intent: Delete a tracked form
    question: How do I delete a form I no longer want to track?
  - id: FormAnalytics.archiveForm
    intent: Archive a tracked form
    question: Can I archive a form to stop tracking it without deleting it?
  - id: FormAnalytics.get
    intent: Get the form overview report
    question: How are my forms performing overall in terms of starts, submissions and conversions?
  phrasing_ops: 26
  slug: matomo-formanalytics-api
- baseURL: https://{matomo_host}/index.php
  baseurl_source: declared
  description: Exposes the Funnels reporting and management API for funnel analytics configuration. Includes endpoints for funnel reports, funnel definitions, and pattern validation helpers.
  name: Matomo Funnels API
  phrasing_intents:
  - id: Funnels.getMetrics
    intent: Get summary metrics for a funnel
    question: What was the overall conversion rate of my checkout funnel last month?
  - id: Funnels.getFunnelsSummary
    intent: Compare all activated funnels on a site
    question: Which of my funnels converts best on this site?
  - id: Funnels.getFunnelsSummaryTotals
    intent: Get combined totals across all funnels
    question: What are the total funnel conversions across all my funnels combined?
  - id: Funnels.getFunnelFlow
    intent: Get step-by-step flow metrics for a funnel
    question: At which step of my signup funnel do most visitors drop off?
  - id: Funnels.getFunnelFlowTable
    intent: Get the funnel flow as a data table
    question: Can I get the funnel flow report in the standard table layout used by other reports?
  - id: Funnels.getFunnelStepSubtable
    intent: Drill into the rows of one funnel step
    question: What detail rows sit underneath a single step of my funnel?
  - id: Funnels.getFunnelEntries
    intent: See where visitors entered a funnel
    question: Which pages do visitors come from when they enter my funnel?
  - id: Funnels.getFunnelExits
    intent: See where visitors left a funnel
    question: Where do people go after abandoning my funnel?
  phrasing_ops: 19
  slug: matomo-funnels-api
- baseURL: https://{matomo_host}/index.php
  baseurl_source: declared
  description: Goals API lets you Manage existing goals, via "updateGoal" and "deleteGoal", create new Goals via "addGoal", or list existing Goals for one or several websites via "getGoals" If you are <a href='https
  name: Matomo Goals API
  phrasing_intents:
  - id: Goals.getGoal
    intent: Get a single goal
    question: What pattern and revenue are set on one particular goal?
  - id: Goals.getGoals
    intent: List goals for websites
    question: Which conversion goals are set up on my website?
  - id: Goals.addGoal
    intent: Create a conversion goal
    question: How do I track a conversion when someone visits a thank-you page?
  - id: Goals.updateGoal
    intent: Update an existing goal
    question: Will editing a goal reprocess conversions that were already recorded?
  - id: Goals.deleteGoal
    intent: Delete a goal
    question: How do I remove a goal I no longer track?
  - id: Goals.getItemsSku
    intent: Report ecommerce sales by product SKU
    question: Which product SKUs sold the most last month?
  - id: Goals.getItemsName
    intent: Report ecommerce sales by product name
    question: What are my best-selling products by name?
  - id: Goals.getItemsCategory
    intent: Report ecommerce sales by product category
    question: Which product categories bring in the most revenue?
  phrasing_ops: 11
  slug: matomo-goals-api
- baseURL: https://{matomo_host}/index.php
  baseurl_source: declared
  description: 'Exposes the Heatmap & Session Recording API endpoints for managing configurations and retrieving recorded activity. Heatmap coordinates use relative values: X and Y positions range from 0 to 2000, whe'
  name: Matomo Heatmap Session Recording API
  phrasing_intents:
  - id: HeatmapSessionRecording.addHeatmap
    intent: Create a new heatmap
    question: How do I start collecting a click heatmap for a landing page?
  - id: HeatmapSessionRecording.duplicateHeatmap
    intent: Copy a heatmap to other sites
    question: Can I reuse an existing heatmap setup on my other websites?
  - id: HeatmapSessionRecording.updateHeatmap
    intent: Change an existing heatmap's settings
    question: How do I change the page rules on a heatmap I already set up?
  - id: HeatmapSessionRecording.deleteHeatmapScreenshot
    intent: Delete a heatmap's stored screenshot
    question: How do I force a fresh screenshot for a heatmap after a page redesign?
  - id: HeatmapSessionRecording.addSessionRecording
    intent: Create a new session recording
    question: How do I start recording visitor sessions on my site?
  - id: HeatmapSessionRecording.updateSessionRecording
    intent: Change an existing session recording
    question: Can I turn keystroke capture on or off for a session recording I already created?
  - id: HeatmapSessionRecording.getHeatmap
    intent: Get one heatmap's configuration
    question: What page rules and sampling is a particular heatmap using?
  - id: HeatmapSessionRecording.getSessionRecording
    intent: Get one session recording's configuration
    question: What settings is a specific session recording configured with?
  phrasing_ops: 31
  slug: matomo-heatmapsessionrecording-api
- baseURL: https://{matomo_host}/index.php
  baseurl_source: declared
  description: 'The ImageGraph.get API call lets you generate beautiful static PNG Graphs for any existing Matomo report. Supported graph types are: line plot, 2D/3D pie chart and vertical bar chart. A few notes abou'
  name: Matomo Image Graph API
  phrasing_intents:
  - id: ImageGraph.get
    intent: Render a report as a static graph image
    question: Can I get a PNG chart of a report to embed in an email or slide?
  phrasing_ops: 1
  slug: matomo-imagegraph-api
- baseURL: https://{matomo_host}/index.php
  baseurl_source: declared
  description: Provides API methods for insight and mover/shaker comparisons between report periods.
  name: Matomo Insights API
  phrasing_intents:
  - id: Insights.canGenerateInsights
    intent: Check if insights can run for a period
    question: Can insights be generated for a yearly period, or only shorter ones?
  - id: Insights.getInsightsOverview
    intent: Get an insights overview across reports
    question: What notable changes happened across my main reports this week in Matomo?
  - id: Insights.getMoversAndShakersOverview
    intent: Get movers and shakers across reports
    question: Which pages, referrers or countries moved the needle most across all reports?
  - id: Insights.getMoversAndShakers
    intent: Find movers and shakers in one report
    question: In a single report, which rows changed far more than the site average?
  - id: Insights.getInsights
    intent: Compare a report against another period
    question: Which rows of a report grew by more than 20% versus the previous period?
  phrasing_ops: 5
  slug: matomo-insights-api
- baseURL: https://{matomo_host}/index.php
  baseurl_source: declared
  description: The LanguagesManager API lets you access existing Matomo translations, and change Users languages preferences. "getTranslationsForLanguage" will return all translation strings for a given language, so
  name: Matomo Languages Manager API
  phrasing_intents:
  - id: LanguagesManager.isLanguageAvailable
    intent: Check whether a language code is available
    question: Is a given language code supported in my Matomo instance?
  - id: LanguagesManager.getAvailableLanguages
    intent: List available language codes
    question: Which language codes can the interface be shown in?
  - id: LanguagesManager.getAvailableLanguagesInfo
    intent: Get translation coverage per language
    question: How complete is the translation for each available language?
  - id: LanguagesManager.getAvailableLanguageNames
    intent: List languages with native and English names
    question: What are the localized and English names of each available language?
  - id: LanguagesManager.getTranslationsForLanguage
    intent: Get all translation strings for a language
    question: Can I download every translation string for one language?
  - id: LanguagesManager.getLanguageForUser
    intent: Get a user's language preference
    question: What interface language has a particular user chosen?
  - id: LanguagesManager.setLanguageForUser
    intent: Set a user's language preference
    question: How do I change the interface language for another user?
  - id: LanguagesManager.uses12HourClockForUser
    intent: Check if a user prefers a 12-hour clock
    question: Does a given user see times in 12-hour AM/PM format?
  phrasing_ops: 9
  slug: matomo-languagesmanager-api
- baseURL: https://{matomo_host}/index.php
  baseurl_source: declared
  description: The Live! API lets you access complete visit level information about your visitors. Combined with the power of <a href='https://matomo.org/docs/analytics-api/segmentation/' target='_blank'>Segmentatio
  name: Matomo Live API
  phrasing_intents:
  - id: Live.getCounters
    intent: Get live visitor counters
    question: How many people are on my website right now in Matomo?
  - id: Live.isVisitorProfileEnabled
    intent: Check if visitor profiles are enabled
    question: Are individual visitor profiles turned on for my site?
  - id: Live.getLastVisitsDetails
    intent: Get the latest visits in detail
    question: Who visited my site most recently, and what did they do?
  - id: Live.getVisitorProfile
    intent: Get a visitor's profile
    question: What has one returning visitor done across all their visits?
  - id: Live.getMostRecentVisitorId
    intent: Get the ID of the latest visitor
    question: What's the visitor ID of whoever visited last?
  - id: Live.getMostRecentVisitsDateTime
    intent: Get when the site was last visited
    question: When was the last time anyone did something on my site?
  phrasing_ops: 6
  slug: matomo-live-api
- baseURL: https://{matomo_host}/index.php
  baseurl_source: declared
  description: Provides API methods for login-related administration tasks.
  name: Matomo Login API
  phrasing_intents:
  - id: Login.unblockBruteForceIPs
    intent: Unblock IPs blocked by brute-force protection
    question: I got locked out after too many login attempts, how can the block be lifted?
  phrasing_ops: 1
  slug: matomo-login-api
- baseURL: https://{matomo_host}/index.php
  baseurl_source: declared
  description: Exposes reporting API endpoints for marketing campaign dimensions and drill-down reports. Includes campaign IDs, names, keywords, source and medium dimensions, and hierarchical subtables.
  name: Matomo Marketing Campaigns Reporting API
  phrasing_intents:
  - id: MarketingCampaignsReporting.getId
    intent: Report campaign performance by campaign ID
    question: How are my campaigns performing when grouped by campaign ID?
  - id: MarketingCampaignsReporting.getName
    intent: Report campaign performance by campaign name
    question: Which marketing campaign brought the most visits last month in Matomo?
  - id: MarketingCampaignsReporting.getKeywordContentFromNameId
    intent: Drill into one campaign's keywords and content
    question: For one specific campaign, which keywords and ad content drove traffic?
  - id: MarketingCampaignsReporting.getKeyword
    intent: Report campaign performance by keyword
    question: Which campaign keywords (utm_term) bring the best traffic across all campaigns?
  - id: MarketingCampaignsReporting.getSource
    intent: Report campaign performance by source
    question: Which campaign sources like newsletter or facebook send the most visitors?
  - id: MarketingCampaignsReporting.getMedium
    intent: Report campaign performance by medium
    question: Does email or cpc perform better as a campaign medium?
  - id: MarketingCampaignsReporting.getContent
    intent: Report campaign performance by content
    question: Which ad variation or link (utm_content) got the most clicks across campaigns?
  - id: MarketingCampaignsReporting.getGroup
    intent: Report campaign performance by group
    question: How do my campaign groups compare against each other?
  phrasing_ops: 11
  slug: matomo-marketingcampaignsreporting-api
- baseURL: https://{matomo_host}/index.php
  baseurl_source: declared
  description: The Marketplace API lets you manage your license key so you can download & install in one-click <a target="_blank" rel="noreferrer" href="https://matomo.org/recommends/premium-plugins/">paid premium p
  name: Matomo Marketplace API
  phrasing_intents:
  - id: Marketplace.deleteLicenseKey
    intent: Remove the Marketplace license key
    question: Is it possible to remove the license key from this installation?
  - id: Marketplace.saveLicenseKey
    intent: Save a Marketplace license key
    question: How do I activate premium plugins with my Matomo Marketplace license key?
  phrasing_ops: 2
  slug: matomo-marketplace-api
- baseURL: https://{matomo_host}/index.php
  baseurl_source: declared
  description: Exposes Media Analytics reports for video and audio plays, engagement, resources, and player usage. Includes real-time endpoints for recent activity and archive-backed endpoints for aggregated media r
  name: Matomo Media Analytics API
  phrasing_intents:
  - id: MediaAnalytics.get
    intent: Get the media analytics overview
    question: How many video and audio plays did my site get last week?
  - id: MediaAnalytics.getCurrentNumPlays
    intent: Count media plays in the last few minutes
    question: How many videos or audio files are being played on my site right now?
  - id: MediaAnalytics.getCurrentSumTimeSpent
    intent: Get total watch time in the last few minutes
    question: How much total time have visitors spent watching media in the last hour?
  - id: MediaAnalytics.getCurrentMostPlays
    intent: List the most played media right now
    question: Which videos are trending on my site in the last few minutes?
  - id: MediaAnalytics.getVideoResources
    intent: Report on video resource URLs
    question: Which video file URLs were played most on my site?
  - id: MediaAnalytics.getAudioResources
    intent: Report on audio resource URLs
    question: Which audio file URLs were played most on my site?
  - id: MediaAnalytics.getVideoTitles
    intent: Report video performance by title
    question: Which video titles got the most plays and engagement?
  - id: MediaAnalytics.getAudioTitles
    intent: Report audio performance by title
    question: Which audio titles or podcast episodes got the most listens?
  phrasing_ops: 14
  slug: matomo-mediaanalytics-api
- baseURL: https://{matomo_host}/index.php
  baseurl_source: declared
  description: The MobileMessaging API lets you manage SMS credentials, phone number verification, and SMS account settings.
  name: Matomo Mobile Messaging API
  phrasing_intents:
  - id: MobileMessaging.areSMSAPICredentialProvided
    intent: Check whether SMS credentials are set
    question: Have I configured SMS API credentials yet for text alerts?
  - id: MobileMessaging.getSMSProvider
    intent: Show the configured SMS provider
    question: Which SMS provider is my account using for text messages?
  - id: MobileMessaging.setSMSAPICredential
    intent: Save SMS provider credentials
    question: How do I connect an SMS provider so Matomo can text me reports?
  - id: MobileMessaging.addPhoneNumber
    intent: Add a phone number for SMS
    question: How do I add my mobile number to receive SMS reports?
  - id: MobileMessaging.resendVerificationCode
    intent: Resend a phone verification code
    question: I never got the SMS verification code, can it be sent again?
  - id: MobileMessaging.getCreditLeft
    intent: Check remaining SMS credit
    question: How much SMS credit do I have left?
  - id: MobileMessaging.getPhoneNumbers
    intent: List my phone numbers
    question: Which phone numbers are set up on my account for SMS?
  - id: MobileMessaging.removePhoneNumber
    intent: Remove a phone number
    question: How do I stop SMS going to an old phone number?
  phrasing_ops: 12
  slug: matomo-mobilemessaging-api
- baseURL: https://{matomo_host}/index.php
  baseurl_source: declared
  description: The MultiSites API lets you request the key metrics (visits, page views, revenue) for all Websites in Matomo.
  name: Matomo Multi Sites API
  phrasing_intents:
  - id: MultiSites.getAll
    intent: Compare visits and revenue across all sites
    question: Which of my websites got the most visits and revenue this month?
  - id: MultiSites.getOne
    intent: Get all-websites metrics for one site
    question: What are one website's total visits, actions and revenue with their trend?
  - id: MultiSites.getAllWithGroups
    intent: Get the grouped all-websites dashboard data
    question: Can I get the all-websites dashboard data grouped the way the widget shows it?
  phrasing_ops: 3
  slug: matomo-multisites-api
- baseURL: https://{matomo_host}/index.php
  baseurl_source: declared
  description: The Overlay API exposes translation data and overlay-specific page transition reports.
  name: Matomo Overlay API
  phrasing_intents:
  - id: Overlay.getTranslations
    intent: Get the Overlay UI translations
    question: What translation strings does the page overlay client use?
  - id: Overlay.getFollowingPages
    intent: List pages reached after a page URL
    question: Which links on a page do visitors follow to reach other pages?
  phrasing_ops: 2
  slug: matomo-overlay-api
- baseURL: https://{matomo_host}/index.php
  baseurl_source: declared
  description: Provides reporting API methods for aggregated page performance metrics.
  name: Matomo Page Performance API
  phrasing_intents:
  - id: PagePerformance.get
    intent: Get page load performance metrics
    question: How fast are my pages loading for visitors?
  phrasing_ops: 1
  slug: matomo-pageperformance-api
- baseURL: https://{matomo_host}/index.php
  baseurl_source: declared
  description: The PrivacyManager API lets you manage GDPR workflows, anonymization settings, and privacy compliance controls.
  name: Matomo Privacy Manager API
  phrasing_intents:
  - id: PrivacyManager.deleteDataSubjects
    intent: Erase a data subject's visit data
    question: How do I honor a GDPR right-to-erasure request for a visitor?
  - id: PrivacyManager.exportDataSubjects
    intent: Export a data subject's visit data
    question: How do I give a visitor a copy of the data tracked about them?
  - id: PrivacyManager.findDataSubjects
    intent: Find a visitor's data by segment
    question: How do I locate all visits belonging to a person who made a GDPR request?
  - id: PrivacyManager.anonymizeSomeRawData
    intent: Anonymize past raw visit data
    question: Can I retroactively anonymize IP addresses in data already tracked?
  - id: PrivacyManager.getAvailableVisitColumnsToAnonymize
    intent: List visit columns that can be anonymized
    question: Which visit-level fields can I wipe when anonymizing old data?
  - id: PrivacyManager.getAvailableLinkVisitActionColumnsToAnonymize
    intent: List action columns that can be anonymized
    question: Which per-action fields can be cleared when anonymizing data?
  phrasing_ops: 6
  slug: matomo-privacymanager-api
- baseURL: https://{matomo_host}/index.php
  baseurl_source: declared
  description: The Referrers API lets you access reports about websites, search engines, keywords, social networks, AI assistants, and campaigns used to access your website. For example, "getKeywords" returns all se
  name: Matomo Referrers API
  phrasing_intents:
  - id: Referrers.get
    intent: Get the referrer overview report
    question: How many distinct referrers sent traffic to my site last month?
  - id: Referrers.getReferrerType
    intent: Report visits by referrer channel type
    question: How much of my traffic comes from search versus direct entry versus websites?
  - id: Referrers.getAll
    intent: Get all referrers merged in one flat table
    question: Can I get every referrer, across search, sites, social and campaigns, in one flat list?
  - id: Referrers.getKeywords
    intent: Report search keywords that brought visits
    question: Which search keywords are people using to find my website?
  - id: Referrers.getSearchEnginesFromKeywordId
    intent: Get search engines for one keyword
    question: Which search engines sent visits for one particular keyword?
  - id: Referrers.getSearchEngines
    intent: Report search engines that referred visits
    question: Which search engines send me the most visitors?
  - id: Referrers.getKeywordsFromSearchEngineId
    intent: Get keywords for one search engine
    question: What keywords did visitors from one specific search engine type?
  - id: Referrers.getCampaigns
    intent: Report marketing campaigns that drove visits
    question: Which marketing campaigns drove traffic to my site?
  phrasing_ops: 23
  slug: matomo-referrers-api
- baseURL: https://{matomo_host}/index.php
  baseurl_source: declared
  description: Provides API methods for screen resolution and device configuration reports.
  name: Matomo Resolution API
  phrasing_intents:
  - id: Resolution.getResolution
    intent: Report visitors' screen resolutions
    question: What screen resolutions do my visitors use?
  - id: Resolution.getConfiguration
    intent: Report visitors' device configurations
    question: What combinations of operating system, browser and resolution do visitors have?
  phrasing_ops: 2
  slug: matomo-resolution-api
- baseURL: https://{matomo_host}/index.php
  baseurl_source: declared
  description: Provides API endpoints for managing roll-up websites and their source site assignments. Use these methods to create roll-ups, update their configuration, and list the configured roll-up sites with the
  name: Matomo Roll Up Reporting API
  phrasing_intents:
  - id: RollUpReporting.addRollUp
    intent: Create a roll-up website
    question: How do I combine several websites into one aggregated report?
  - id: RollUpReporting.updateRollUp
    intent: Change a roll-up website
    question: How do I add another site to an existing roll-up?
  - id: RollUpReporting.getRollUps
    intent: List roll-up websites
    question: Which roll-up websites have been set up?
  phrasing_ops: 3
  slug: matomo-rollupreporting-api
- baseURL: https://{matomo_host}/index.php
  baseurl_source: declared
  description: Provides SearchEngineKeywordsPerformance API endpoints for imported keyword and crawl-performance reports. Exposes combined and provider-specific reports for Google, Bing, and Yandex search data. \Plu
  name: Matomo Search Engine Keywords Performance API
  phrasing_intents:
  - id: SearchEngineKeywordsPerformance.getKeywords
    intent: Get search keyword performance from all sources
    question: Which search keywords brought visitors to my site, combining every source?
  - id: SearchEngineKeywordsPerformance.getKeywordsImported
    intent: Get keywords imported from search engines
    question: What keyword data has been imported from the connected search engine consoles?
  - id: SearchEngineKeywordsPerformance.getKeywordsGoogle
    intent: Get keyword performance from Google
    question: What Google search queries is my site getting clicks and impressions for?
  - id: SearchEngineKeywordsPerformance.getKeywordsBing
    intent: Get keyword performance from Bing and Yahoo
    question: Which Bing and Yahoo searches send traffic to my site?
  - id: SearchEngineKeywordsPerformance.getKeywordsYandex
    intent: Get keyword performance from Yandex
    question: Which Yandex searches send traffic to my site?
  - id: SearchEngineKeywordsPerformance.getKeywordsGoogleWeb
    intent: Get Google web search keyword performance
    question: What regular Google web search queries is my site ranking for?
  - id: SearchEngineKeywordsPerformance.getKeywordsGoogleImage
    intent: Get Google image search keyword performance
    question: Which Google Images searches lead people to my pictures?
  - id: SearchEngineKeywordsPerformance.getKeywordsGoogleVideo
    intent: Get Google video search keyword performance
    question: Which Google video search queries surface my content?
  phrasing_ops: 12
  slug: matomo-searchenginekeywordsperformance-api
- baseURL: https://{matomo_host}/index.php
  baseurl_source: declared
  description: The SegmentEditor API lets you add, update, delete custom Segments, and list saved segments.
  name: Matomo Segment Editor API
  phrasing_intents:
  - id: SegmentEditor.isUserCanAddNewSegment
    intent: Check if I'm allowed to create segments
    question: Do I have permission to save a new segment?
  - id: SegmentEditor.delete
    intent: Delete a saved segment
    question: How do I delete a saved segment I no longer use?
  - id: SegmentEditor.update
    intent: Edit a saved segment
    question: Can I change the conditions of a segment I already saved?
  - id: SegmentEditor.add
    intent: Save a new segment
    question: How do I save a new visitor segment, like mobile users from France, in Matomo?
  - id: SegmentEditor.star
    intent: Star a saved segment
    question: Can I mark a segment as a favorite so it shows at the top?
  - id: SegmentEditor.unstar
    intent: Unstar a saved segment
    question: How do I remove the star from a segment?
  - id: SegmentEditor.get
    intent: Get a saved segment by ID
    question: What's the definition of a specific saved segment?
  - id: SegmentEditor.getAll
    intent: List all saved segments
    question: Which segments have been saved so far?
  phrasing_ops: 9
  slug: matomo-segmenteditor-api
- baseURL: https://{matomo_host}/index.php
  baseurl_source: declared
  description: 'The SEO API lets you access a list of SEO metrics for the specified URL: Bing indexed pages and age of the Domain name.'
  name: Matomo SEO API
  phrasing_intents:
  - id: SEO.getRank
    intent: Get SEO statistics for a URL
    question: What SEO stats can I get for my homepage URL?
  phrasing_ops: 1
  slug: matomo-seo-api
- baseURL: https://{matomo_host}/index.php
  baseurl_source: declared
  description: 'The SitesManager API gives you full control on Websites in Matomo (create, update and delete), and many methods to retrieve websites based on various attributes. This API lets you create websites via '
  name: Matomo Sites Manager API
  phrasing_intents:
  - id: SitesManager.getJavascriptTag
    intent: Get the JavaScript tracking tag for a website
    question: Where do I get the JavaScript tracking snippet to paste into my website?
  - id: SitesManager.getImageTrackingCode
    intent: Get image pixel tracking code for a website
    question: How can I track visits on pages where JavaScript can't run, like in an email?
  - id: SitesManager.getSitesFromGroup
    intent: List the websites in a site group
    question: Which of my tracked websites belong to a particular group?
  - id: SitesManager.getSitesGroups
    intent: List website group names
    question: What website groups exist in my Matomo instance?
  - id: SitesManager.getSiteFromId
    intent: Get the details of one website
    question: What timezone and currency is a specific tracked website configured with?
  - id: SitesManager.getSiteUrlsFromId
    intent: List all URLs registered for a website
    question: Which alias URLs are registered on a website besides its main URL?
  - id: SitesManager.getAllSites
    intent: List all websites with their details
    question: How do I get a full list of every website tracked in Matomo with its settings?
  - id: SitesManager.getAllSitesId
    intent: List the IDs of all websites
    question: What are the numeric IDs of all the websites registered?
  phrasing_ops: 53
  slug: matomo-sitesmanager-api
- baseURL: https://{matomo_host}/index.php
  baseurl_source: declared
  description: Provides API methods for Tour challenges and engagement levels.
  name: Matomo Tour API
  phrasing_intents:
  - id: Tour.getChallenges
    intent: List onboarding tour challenges
    question: What onboarding challenges are left for me to complete?
  - id: Tour.skipChallenge
    intent: Skip an onboarding challenge
    question: Can I skip a tour challenge I don't care about?
  - id: Tour.getLevel
    intent: Get my onboarding tour level
    question: What level have I reached in the onboarding tour?
  phrasing_ops: 3
  slug: matomo-tour-api
- baseURL: https://{matomo_host}/index.php
  baseurl_source: declared
  description: Provides API methods for transition reports around a specific page action.
  name: Matomo Transitions API
  phrasing_intents:
  - id: Transitions.getTransitionsForPageTitle
    intent: See traffic flow around a page title
    question: Where do visitors come from and go next around a page with a given title?
  - id: Transitions.getTransitionsForPageUrl
    intent: See traffic flow around a page URL
    question: Which pages do visitors view before and after a specific URL?
  - id: Transitions.getTransitionsForAction
    intent: See traffic flow around any action
    question: Can I get transitions for an action by its name and type rather than a URL or title?
  - id: Transitions.isPeriodAllowed
    intent: Check if a period is allowed for transitions
    question: Is a yearly period allowed for the transitions report?
  phrasing_ops: 4
  slug: matomo-transitions-api
- baseURL: https://{matomo_host}/index.php
  baseurl_source: declared
  description: The UserCountry API lets you access reports about your visitors' Countries and Continents.
  name: Matomo User Country API
  phrasing_intents:
  - id: UserCountry.getCountry
    intent: Report visits by country
    question: Which countries do most of my visitors come from?
  - id: UserCountry.getContinent
    intent: Report visits by continent
    question: How is my traffic split between Europe, Asia and the Americas?
  - id: UserCountry.getRegion
    intent: Report visits by region
    question: Which states or provinces send me the most visitors?
  - id: UserCountry.getCity
    intent: Report visits by city
    question: Which cities are my visitors located in?
  - id: UserCountry.getCountryCodeMapping
    intent: Map ISO country codes to country names
    question: Can I get a lookup of ISO country codes to translated country names?
  - id: UserCountry.getLocationFromIP
    intent: Geolocate an IP address
    question: Where in the world is a particular IP address located?
  - id: UserCountry.setLocationProvider
    intent: Set the active geolocation provider
    question: How do I switch which geolocation provider is used for visitor locations?
  - id: UserCountry.getNumberOfDistinctCountries
    intent: Count distinct visitor countries in a period
    question: How many different countries did visitors come from this month?
  phrasing_ops: 8
  slug: matomo-usercountry-api
- baseURL: https://{matomo_host}/index.php
  baseurl_source: declared
  description: Provides API methods for User ID reports.
  name: Matomo User ID API
  phrasing_intents:
  - id: UserId.getUsers
    intent: Report activity per logged-in User ID
    question: Which of my logged-in users visited most this month?
  phrasing_ops: 1
  slug: matomo-userid-api
- baseURL: https://{matomo_host}/index.php
  baseurl_source: declared
  description: The UserLanguage API lets you access reports about your Visitors language setting
  name: Matomo User Language API
  phrasing_intents:
  - id: UserLanguage.getLanguage
    intent: Report visitors by browser language
    question: What languages do my visitors speak, grouped as English, German and so on?
  - id: UserLanguage.getLanguageCode
    intent: Report visitors by full locale code
    question: Can I tell en-US visitors apart from en-GB visitors?
  phrasing_ops: 2
  slug: matomo-userlanguage-api
- baseURL: https://{matomo_host}/index.php
  baseurl_source: declared
  description: The UsersManager API lets you Manage Users and their permissions to access specific websites. You can create users via "addUser", update existing users via "updateUser" and delete users via "deleteUse
  name: Matomo Users Manager API
  phrasing_intents:
  - id: UsersManager.getAvailableRoles
    intent: List the roles a user can be given
    question: What roles can I assign to users in Matomo?
  - id: UsersManager.getAvailableCapabilities
    intent: List the capabilities that can be granted
    question: Which extra capabilities can be layered on top of a user's role?
  - id: UsersManager.setUserPreference
    intent: Set a preference for a user
    question: Can I change a user's saved preference, like their default report, through the API?
  - id: UsersManager.getUserPreference
    intent: Read a user's preference value
    question: What value does a user currently have stored for a given preference?
  - id: UsersManager.getUsersPlusRole
    intent: List a site's users with their roles
    question: Who has access to this website and what role does each person have?
  - id: UsersManager.getUsers
    intent: List users visible to me
    question: Which user accounts can I see with my access?
  - id: UsersManager.getUsersLogin
    intent: List the login names of visible users
    question: Can I get just the usernames of everyone, without their full details?
  - id: UsersManager.getUsersSitesFromAccess
    intent: Map users to sites for one access level
    question: For each user, which sites do they hold admin access on?
  phrasing_ops: 32
  slug: matomo-usersmanager-api
- baseURL: https://{matomo_host}/index.php
  baseurl_source: declared
  description: VisitFrequency API lets you access a list of metrics related to Returning Visitors.
  name: Matomo Visit Frequency API
  phrasing_intents:
  - id: VisitFrequency.get
    intent: Compare new and returning visitors
    question: How many of my visitors are returning versus new?
  phrasing_ops: 1
  slug: matomo-visitfrequency-api
- baseURL: https://{matomo_host}/index.php
  baseurl_source: declared
  description: VisitorInterest API lets you access visitor engagement distribution reports, including visits by pages viewed, visit duration, days since last visit, and visit count.
  name: Matomo Visitor Interest API
  phrasing_intents:
  - id: VisitorInterest.getNumberOfVisitsPerVisitDuration
    intent: Report visits by visit duration
    question: How long do visitors typically stay on my site?
  - id: VisitorInterest.getNumberOfVisitsPerPage
    intent: Report visits by pages viewed
    question: How many pages do visitors usually look at per visit?
  - id: VisitorInterest.getNumberOfVisitsByDaysSinceLast
    intent: Report visits by days since previous visit
    question: How many days pass before returning visitors come back?
  - id: VisitorInterest.getNumberOfVisitsByVisitCount
    intent: Report visits by lifetime visit count
    question: How many of my visitors are on their first, second or tenth visit?
  phrasing_ops: 4
  slug: matomo-visitorinterest-api
- baseURL: https://{matomo_host}/index.php
  baseurl_source: declared
  description: VisitsSummary API lets you access the core web analytics metrics (visits, unique visitors, count of actions (page views & downloads & clicks on outlinks), time on site, bounces and converted visits.
  name: Matomo Visits Summary API
  phrasing_intents:
  - id: VisitsSummary.get
    intent: Get the visits overview report
    question: What does my site's traffic overview look like for last month?
  - id: VisitsSummary.getVisits
    intent: Count visits in a period
    question: How many visits did my website get yesterday?
  - id: VisitsSummary.getUniqueVisitors
    intent: Count unique visitors in a period
    question: How many unique visitors came to my site this month?
  - id: VisitsSummary.getUsers
    intent: Count logged-in users in a period
    question: How many users with a User ID visited my site?
  - id: VisitsSummary.getActions
    intent: Count actions in a period
    question: How many total actions did visitors take on my site?
  - id: VisitsSummary.getMaxActions
    intent: Get the most actions in one visit
    question: What is the highest number of actions anyone took in a single visit?
  - id: VisitsSummary.getBounceCount
    intent: Count bounced visits
    question: How many visitors left after viewing only one page?
  - id: VisitsSummary.getVisitsConverted
    intent: Count visits that converted
    question: How many visits converted a goal this month?
  phrasing_ops: 10
  slug: matomo-visitssummary-api
- baseURL: https://{matomo_host}/index.php
  baseurl_source: declared
  description: VisitTime API lets you access reports by Hour (Server time), and by Hour Local Time of your visitors.
  name: Matomo Visit Time API
  phrasing_intents:
  - id: VisitTime.getVisitInformationPerLocalTime
    intent: Show visits by the visitor's local hour
    question: At what time of day in their own timezone do visitors come to my site?
  - id: VisitTime.getVisitInformationPerServerTime
    intent: Show visits by the site's hour of day
    question: Which hours in my site's timezone get the most traffic?
  - id: VisitTime.getByDayOfWeek
    intent: Show visits by day of the week
    question: Which day of the week gets the most visitors?
  phrasing_ops: 3
  slug: matomo-visittime-api
- baseURL: https://{matomo_host}/index.php
  baseurl_source: declared
  description: Exposes super-user OAuth2 client management endpoints for Matomo. This API lists configured scopes and lets administrators create, inspect, update, rotate, activate, and delete OAuth2 clients.
  name: Matomo O Auth2 API
  phrasing_intents:
  - id: OAuth2.getClients
    intent: List OAuth2 clients
    question: Which OAuth2 client applications are configured in my Matomo?
  - id: OAuth2.getClient
    intent: Get one OAuth2 client
    question: What grant types and redirect URIs does a specific OAuth client have?
  - id: OAuth2.getScopes
    intent: List the OAuth2 scopes available to clients
    question: What scopes can I grant to an OAuth2 client?
  - id: OAuth2.createClient
    intent: Create an OAuth2 client
    question: How do I register a new OAuth2 app so it can call the Matomo API?
  - id: OAuth2.updateClient
    intent: Update an OAuth2 client
    question: How do I change the redirect URIs or scope on an existing OAuth client?
  - id: OAuth2.rotateSecret
    intent: Rotate an OAuth2 client's secret
    question: How do I generate a new secret for an OAuth client whose secret leaked?
  - id: OAuth2.setClientActive
    intent: Activate or deactivate an OAuth2 client
    question: Can I temporarily disable an OAuth client without deleting it?
  - id: OAuth2.deleteClient
    intent: Delete an OAuth2 client and its tokens
    question: What happens to access and refresh tokens when I delete an OAuth client?
  phrasing_ops: 8
  slug: matomo-oauth2-api
- baseURL: https://{matomo_host}/index.php
  baseurl_source: declared
  description: Exposes the AbTesting API for managing experiments, embedding experiment scripts, and reading experiment reports.
  name: Matomo Ab Testing API
  slug: matomo-ab-testing-api
- baseURL: https://{matomo_host}/index.php
  baseurl_source: declared
  description: Exposes Activity Log API endpoints for listing activity entries, counting matches, and resolving the permitted date range for the current caller.
  name: Matomo Activity Log API
  phrasing_intents:
  - id: ActivityLog.getEntries
    intent: List activity log entries
    question: Who changed settings in our analytics instance recently?
  - id: ActivityLog.getEntryCount
    intent: Count activity log entries
    question: How many audit log entries were recorded last month?
  - id: ActivityLog.getAllActivityTypes
    intent: List the available activity types
    question: What kinds of activities can appear in the audit log?
  phrasing_ops: 3
  slug: matomo-activity-log-api
- baseURL: https://{matomo_host}/index.php
  baseurl_source: declared
  description: 'Provides Reporting API endpoints for reading OpenAPI plugin configuration and specifications. Exposes endpoints to return the effective plugin list for spec generation, read pre-generated spec files, '
  name: Matomo API Reference API
  phrasing_intents:
  - id: ApiReference.getAllowedPlugins
    intent: List plugins included in the API reference
    question: Which plugins have OpenAPI specs generated for the API reference?
  - id: ApiReference.getAllowedPluginMetadata
    intent: Get metadata for API reference plugins
    question: What details are available about each plugin in the API reference?
  - id: ApiReference.getOpenApiSpec
    intent: Download a plugin's OpenAPI spec
    question: How do I get the OpenAPI specification for a specific Matomo plugin?
  phrasing_ops: 3
  slug: matomo-api-reference-api
- baseURL: https://{matomo_host}/index.php
  baseurl_source: declared
  description: Exposes Custom Reports configuration and reporting endpoints. Use it to create, duplicate, manage, and query custom report definitions and their archived data.
  name: Matomo Custom Reports API
  phrasing_intents:
  - id: CustomReports.duplicateCustomReport
    intent: Copy a custom report to other sites
    question: Can I copy a custom report I built to my other websites?
  - id: CustomReports.addCustomReport
    intent: Create a new custom report
    question: How do I build my own report combining the dimensions and metrics I choose in Matomo?
  - id: CustomReports.updateCustomReport
    intent: Edit an existing custom report
    question: Can I add a metric to a custom report I already created?
  - id: CustomReports.getConfiguredReports
    intent: List all custom report definitions on a site
    question: Which custom reports have been set up for my site?
  - id: CustomReports.getConfiguredReport
    intent: Get one custom report's definition
    question: What dimensions and metrics make up a given custom report?
  - id: CustomReports.deleteCustomReport
    intent: Delete a custom report
    question: How do I get rid of a custom report I no longer need?
  - id: CustomReports.pauseCustomReport
    intent: Pause a custom report
    question: Can I temporarily stop a custom report from processing data?
  - id: CustomReports.resumeCustomReport
    intent: Resume a paused custom report
    question: How do I turn a paused custom report back on?
  phrasing_ops: 13
  slug: matomo-custom-reports-api
- baseURL: https://{matomo_host}/index.php
  baseurl_source: declared
  description: The ScheduledReports API lets you manage Scheduled Email reports, as well as generate, download or email any existing report.
  name: Matomo Scheduled Reports API
  phrasing_intents:
  - id: ScheduledReports.addReport
    intent: Schedule a new email report
    question: How do I get a weekly PDF of my analytics emailed to me automatically?
  - id: ScheduledReports.updateReport
    intent: Update a scheduled report
    question: How do I change the delivery time of a report I already scheduled?
  - id: ScheduledReports.deleteReport
    intent: Delete a scheduled report
    question: How do I stop a scheduled email report from being sent?
  - id: ScheduledReports.getReports
    intent: List scheduled reports
    question: Which email reports are scheduled for my website?
  - id: ScheduledReports.generateReport
    intent: Generate a scheduled report's output
    question: Can I produce the contents of a scheduled report for a past date without emailing it?
  - id: ScheduledReports.sendReport
    intent: Send a scheduled report immediately
    question: How do I send a scheduled report right now instead of waiting for its next run?
  phrasing_ops: 6
  slug: matomo-scheduled-reports-api
- baseURL: https://{matomo_host}/index.php
  baseurl_source: declared
  description: Exposes the Tag Manager API for managing containers, versions, tags, triggers, and variables. The endpoints also provide installation metadata, publishing workflows, preview controls, and import/expor
  name: Matomo Tag Manager API
  phrasing_intents:
  - id: TagManager.getAvailableContexts
    intent: List contexts that support tag types
    question: Which container contexts, like web or Android, does Tag Manager currently support?
  - id: TagManager.getAvailableEnvironments
    intent: List environments for container releases
    question: Which release environments exist for publishing Tag Manager containers?
  - id: TagManager.getAvailableEnvironmentsWithPublishCapability
    intent: List environments I can publish to for a site
    question: Which environments am I personally allowed to publish containers to on this site?
  - id: TagManager.getAvailableTagFireLimits
    intent: List the fire limit options for tags
    question: What fire limit options can I set so a tag only fires once per page or once ever?
  - id: TagManager.getAvailableComparisons
    intent: List comparison operators for trigger conditions
    question: Which comparison operators, like contains or starts with, can trigger conditions use?
  - id: TagManager.getAvailableTagTypesInContext
    intent: List tag templates for a context
    question: What tag types can I add to a web container?
  - id: TagManager.getAvailableTriggerTypesInContext
    intent: List trigger templates for a context
    question: What trigger types, like page view or click, are available in a web container?
  - id: TagManager.getAvailableVariableTypesInContext
    intent: List variable templates for a context
    question: Which variable types can I create manually in a web container?
  phrasing_ops: 47
  slug: matomo-tag-manager-api
- baseURL: https://{matomo_host}/index.php
  baseurl_source: declared
  description: Provides API methods for managing two-factor authentication.
  name: Matomo Two Factor Auth API
  phrasing_intents:
  - id: TwoFactorAuth.resetTwoFactorAuth
    intent: Reset two-factor authentication for a user
    question: A user lost their authenticator app; can I turn off their two-factor login?
  phrasing_ops: 1
  slug: matomo-two-factor-auth-api
artifact_total: 81
collections:
- collection_type: open
  name: Matomo Reporting Index.php API
  slug: open-matomo-index-php-api
- collection_type: open
  name: Matomo Reporting Index.php Matomo.php API
  slug: open-matomo-matomo-php-api
- collection_type: open
  name: Matomo Tracking API
  slug: open-matomo-tracking
- collection_type: open
  name: Matomo Reporting API
  slug: open-matomo
common:
- group: other
  href: https://artifacts.apis.io/matomo/capabilities/matomo-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/matomo-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/matomo/overlays/matomo-live-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/matomo-live-overlay.yaml
- group: other
  href: https://artifacts.apis.io/matomo/overlays/matomo-goals-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/matomo-goals-overlay.yaml
- group: other
  href: https://artifacts.apis.io/matomo/overlays/matomo-segment-editor-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/matomo-segment-editor-overlay.yaml
- group: other
  href: https://artifacts.apis.io/matomo/overlays/matomo-sites-manager-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/matomo-sites-manager-overlay.yaml
- group: other
  href: https://artifacts.apis.io/matomo/overlays/matomo-tag-manager-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/matomo-tag-manager-overlay.yaml
- group: other
  href: https://artifacts.apis.io/matomo/overlays/matomo-users-manager-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/matomo-users-manager-overlay.yaml
- group: other
  href: https://artifacts.apis.io/matomo/overlays/matomo-crash-analytics-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/matomo-crash-analytics-overlay.yaml
- group: other
  href: https://artifacts.apis.io/matomo/overlays/matomo-heatmap-session-recording-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/matomo-heatmap-session-recording-overlay.yaml
- group: other
  href: https://artifacts.apis.io/matomo/overlays/matomo-form-analytics-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/matomo-form-analytics-overlay.yaml
- group: other
  href: https://artifacts.apis.io/matomo/overlays/matomo-referrers-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/matomo-referrers-overlay.yaml
- group: other
  href: https://artifacts.apis.io/matomo/overlays/matomo-funnels-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/matomo-funnels-overlay.yaml
- group: other
  href: https://artifacts.apis.io/matomo/overlays/matomo-actions-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/matomo-actions-overlay.yaml
- group: other
  href: https://artifacts.apis.io/matomo/overlays/matomo-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/matomo-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/matomo/overlays/matomo-ab-testing-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/matomo-ab-testing-overlay.yaml
- group: other
  href: https://artifacts.apis.io/matomo/overlays/matomo-media-analytics-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/matomo-media-analytics-overlay.yaml
- group: other
  href: https://artifacts.apis.io/matomo/overlays/matomo-custom-reports-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/matomo-custom-reports-overlay.yaml
- group: other
  href: https://artifacts.apis.io/matomo/overlays/matomo-mobile-messaging-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/matomo-mobile-messaging-overlay.yaml
- group: other
  href: https://artifacts.apis.io/matomo/overlays/matomo-search-engine-keywords-performance-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/matomo-search-engine-keywords-performance-overlay.yaml
- group: other
  href: https://artifacts.apis.io/matomo/overlays/matomo-marketing-campaigns-reporting-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/matomo-marketing-campaigns-reporting-overlay.yaml
- group: other
  href: https://artifacts.apis.io/matomo/overlays/matomo-visits-summary-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/matomo-visits-summary-overlay.yaml
- group: other
  href: https://artifacts.apis.io/matomo/overlays/matomo-events-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/matomo-events-overlay.yaml
- group: other
  href: https://artifacts.apis.io/matomo/overlays/matomo-languages-manager-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/matomo-languages-manager-overlay.yaml
- group: other
  href: https://artifacts.apis.io/matomo/overlays/matomo-devices-detection-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/matomo-devices-detection-overlay.yaml
- group: other
  href: https://artifacts.apis.io/matomo/overlays/matomo-oauth2-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/matomo-oauth2-overlay.yaml
- group: other
  href: https://artifacts.apis.io/matomo/overlays/matomo-user-country-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/matomo-user-country-overlay.yaml
- group: other
  href: https://artifacts.apis.io/matomo/overlays/matomo-annotations-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/matomo-annotations-overlay.yaml
- group: other
  href: https://artifacts.apis.io/matomo/overlays/matomo-custom-alerts-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/matomo-custom-alerts-overlay.yaml
- group: other
  href: https://artifacts.apis.io/matomo/overlays/matomo-advertising-conversion-export-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/matomo-advertising-conversion-export-overlay.yaml
- group: other
  href: https://artifacts.apis.io/matomo/overlays/matomo-custom-dimensions-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/matomo-custom-dimensions-overlay.yaml
- group: other
  href: https://artifacts.apis.io/matomo/overlays/matomo-privacy-manager-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/matomo-privacy-manager-overlay.yaml
- group: other
  href: https://artifacts.apis.io/matomo/overlays/matomo-scheduled-reports-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/matomo-scheduled-reports-overlay.yaml
- group: other
  href: https://artifacts.apis.io/matomo/overlays/matomo-dashboard-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/matomo-dashboard-overlay.yaml
- group: other
  href: https://artifacts.apis.io/matomo/overlays/matomo-insights-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/matomo-insights-overlay.yaml
- group: other
  href: https://artifacts.apis.io/matomo/overlays/matomo-transitions-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/matomo-transitions-overlay.yaml
- group: other
  href: https://artifacts.apis.io/matomo/overlays/matomo-visitor-interest-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/matomo-visitor-interest-overlay.yaml
- group: other
  href: https://artifacts.apis.io/matomo/overlays/matomo-activity-log-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/matomo-activity-log-overlay.yaml
- group: other
  href: https://artifacts.apis.io/matomo/overlays/matomo-api-reference-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/matomo-api-reference-overlay.yaml
- group: other
  href: https://artifacts.apis.io/matomo/overlays/matomo-core-admin-home-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/matomo-core-admin-home-overlay.yaml
- group: other
  href: https://artifacts.apis.io/matomo/overlays/matomo-feedback-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/matomo-feedback-overlay.yaml
- group: other
  href: https://artifacts.apis.io/matomo/overlays/matomo-multi-sites-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/matomo-multi-sites-overlay.yaml
- group: other
  href: https://artifacts.apis.io/matomo/overlays/matomo-roll-up-reporting-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/matomo-roll-up-reporting-overlay.yaml
- group: other
  href: https://artifacts.apis.io/matomo/overlays/matomo-tour-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/matomo-tour-overlay.yaml
- group: other
  href: https://artifacts.apis.io/matomo/overlays/matomo-visit-time-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/matomo-visit-time-overlay.yaml
- group: other
  href: https://artifacts.apis.io/matomo/overlays/matomo-cohorts-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/matomo-cohorts-overlay.yaml
- group: other
  href: https://artifacts.apis.io/matomo/overlays/matomo-contents-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/matomo-contents-overlay.yaml
- group: other
  href: https://artifacts.apis.io/matomo/overlays/matomo-marketplace-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/matomo-marketplace-overlay.yaml
- group: other
  href: https://artifacts.apis.io/matomo/overlays/matomo-overlay-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/matomo-overlay-overlay.yaml
- group: other
  href: https://artifacts.apis.io/matomo/overlays/matomo-resolution-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/matomo-resolution-overlay.yaml
- group: other
  href: https://artifacts.apis.io/matomo/overlays/matomo-user-language-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/matomo-user-language-overlay.yaml
- group: other
  href: https://artifacts.apis.io/matomo/overlays/matomo-bandwidth-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/matomo-bandwidth-overlay.yaml
- group: other
  href: https://artifacts.apis.io/matomo/overlays/matomo-custom-js-tracker-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/matomo-custom-js-tracker-overlay.yaml
- group: other
  href: https://artifacts.apis.io/matomo/overlays/matomo-device-plugins-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/matomo-device-plugins-overlay.yaml
- group: other
  href: https://artifacts.apis.io/matomo/overlays/matomo-image-graph-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/matomo-image-graph-overlay.yaml
- group: other
  href: https://artifacts.apis.io/matomo/overlays/matomo-login-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/matomo-login-overlay.yaml
- group: other
  href: https://artifacts.apis.io/matomo/overlays/matomo-page-performance-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/matomo-page-performance-overlay.yaml
- group: other
  href: https://artifacts.apis.io/matomo/overlays/matomo-seo-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/matomo-seo-overlay.yaml
- group: other
  href: https://artifacts.apis.io/matomo/overlays/matomo-two-factor-auth-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/matomo-two-factor-auth-overlay.yaml
- group: other
  href: https://artifacts.apis.io/matomo/overlays/matomo-user-id-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/matomo-user-id-overlay.yaml
- group: other
  href: https://artifacts.apis.io/matomo/overlays/matomo-visit-frequency-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/matomo-visit-frequency-overlay.yaml
- group: docs
  href: https://artifacts.apis.io/matomo/openapi/
  title: ''
  type: OpenAPI
  url: openapi/
- group: agent
  href: https://artifacts.apis.io/matomo/mcp/matomo-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/matomo-mcp.yml
- group: build
  href: https://artifacts.apis.io/matomo/mcp/matomo-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/matomo-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/matomo/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/matomo/agentic-access/matomo-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/matomo-agentic-access.yml
- group: agent
  href: https://artifacts.apis.io/matomo/llms/matomo-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/matomo-llms.txt
- group: build
  href: https://artifacts.apis.io/matomo/packages/matomo-packages.yml
  title: ''
  type: Packages
  url: packages/matomo-packages.yml
- group: build
  href: https://artifacts.apis.io/matomo/packages/matomo-packages.yml
  title: ''
  type: SDKs
  url: packages/matomo-packages.yml
- group: agent
  href: https://artifacts.apis.io/matomo/well-known/matomo-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/matomo-well-known.yml
- group: auth
  href: https://artifacts.apis.io/matomo/authentication/matomo-authentication.yml
  title: ''
  type: Authentication
  url: authentication/matomo-authentication.yml
- group: auth
  href: https://artifacts.apis.io/matomo/scopes/matomo-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/matomo-scopes.yml
- group: design
  href: https://artifacts.apis.io/matomo/conventions/matomo-conventions.yml
  title: ''
  type: Conventions
  url: conventions/matomo-conventions.yml
- group: design
  href: https://artifacts.apis.io/matomo/errors/matomo-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/matomo-problem-types.yml
- group: design
  href: https://artifacts.apis.io/matomo/data-model/matomo-data-model.yml
  title: ''
  type: DataModel
  url: data-model/matomo-data-model.yml
- group: design
  href: https://artifacts.apis.io/matomo/conformance/matomo-conformance.yml
  title: ''
  type: Conformance
  url: conformance/matomo-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://matomo.org/security/
- group: design
  href: https://artifacts.apis.io/matomo/lifecycle/matomo-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/matomo-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.matomo.cloud/
- group: operate
  href: https://artifacts.apis.io/matomo/changelog/matomo-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/matomo-changelog.yml
- group: build
  href: https://artifacts.apis.io/matomo/cli/matomo-cli.yml
  title: ''
  type: CLI
  url: cli/matomo-cli.yml
- group: design
  href: https://artifacts.apis.io/matomo/components/matomo-components.yml
  title: ''
  type: Components
  url: components/matomo-components.yml
- group: start
  href: https://artifacts.apis.io/matomo/sandbox/matomo-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/matomo-sandbox.yml
- group: commercial
  href: https://artifacts.apis.io/matomo/plans/matomo-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/matomo-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/matomo/rate-limits/matomo-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/matomo-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/matomo/finops/matomo-finops.yml
  title: ''
  type: FinOps
  url: finops/matomo-finops.yml
- group: auth
  title: ''
  type: Security
  url: https://matomo.org/security/
- group: auth
  href: https://artifacts.apis.io/matomo/security/matomo-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/matomo-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/matomo/security/matomo-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/matomo-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/matomo/security/matomo-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/matomo-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.matomo.org
- group: docs
  title: ''
  type: Documentation
  url: https://developer.matomo.org
- group: docs
  title: ''
  type: APIReference
  url: https://developer.matomo.org/api-reference/api
- group: docs
  title: ''
  type: APIDocumentation
  url: https://developer.matomo.org/api-reference/reporting-api
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.matomo.org/guides/getting-started-part-1
- group: operate
  title: ''
  type: Roadmap
  url: https://matomo.org/roadmap/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/matomo-org
- group: build
  title: ''
  type: GitHub
  url: https://github.com/matomo-org/matomo
- group: company
  title: ''
  type: Website
  url: https://matomo.org
- group: company
  title: ''
  type: Blog
  url: https://matomo.org/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://matomo.org/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://matomo.org/start-free-analytics-trial
- group: start
  title: ''
  type: Login
  url: https://matomo.org/login
- group: operate
  title: ''
  type: Support
  url: https://matomo.org/support
- group: operate
  title: ''
  type: Forums
  url: https://forum.matomo.org
- group: other
  title: ''
  type: Marketplace
  url: https://plugins.matomo.org
- group: other
  title: ''
  type: SelfHosted
  url: https://matomo.org/matomo-on-premise
- group: start
  title: ''
  type: Demo
  url: https://demo.matomo.cloud
- group: commercial
  title: ''
  type: TermsOfService
  url: https://matomo.org/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://matomo.org/privacy-policy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/matomo
created: '2026-03-26'
description: 'Matomo is an open source web analytics platform — self-hosted (Matomo On-Premise) or vendor-hosted (Matomo Cloud) — that gives an organisation complete ownership of its analytics data. Formerly Piwik, it is the leading privacy-first alternative to Google Analytics, with GDPR tooling, data residency in Frankfurt for Cloud, and no data sampling. Its API surface is substantial and unusual: 556 documented operations across 59 plugin modules, every one dispatched through a single /index.php RPC entrypoint on the customer''s own deployment rather than a vendor host, plus a separate tracking entrypoint at /matomo.php. Matomo generates its own OpenAPI 3.1.0 documents through a first-party ApiReference plugin, and ships a first-party Model Context Protocol server exposing 19 agent tools over an authenticated HTTP endpoint.'
finops:
- has_sources: true
  method: derived
  name: Matomo Finops
  primary_unit: month (excl. tax)
  service_category: ''
  slug: matomo-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/matomo.png
layout: provider
mcp_servers:
- description: Remote MCP server at {matomo_host} over HTTP requiring OAuth; 19 tools listed.
  name: Matomo MCP Server
  slug: matomo
modified: '2026-08-13'
name: Matomo
nav: Providers
network: true
overview: 'Matomo publishes 60 API contracts indexed on the [APIs.io](https://apis.io/) network, including Reporting API (index.php entrypoint), Tracking API (matomo.php entrypoint), Actions API, and 57 more. Tagged areas include Analytics, Web Analytics, Open Source, Privacy, and DataOwnership.


  The Matomo catalog on APIs.io includes 1 Spectral governance ruleset.


  Matomo''s developer surface includes authentication, changelog, CLI, sandbox, documentation, API reference, getting-started guide, and 103 more developer resources.'
plans:
- name: Matomo Plans Pricing
  plan_count: 10
  slug: matomo-plans-pricing
- name: Matomo Price Estimates
  plan_count: 0
  slug: matomo-price-estimates
random_paper: 5
rate_limits:
- limit_count: 4
  name: Matomo Rate Limits
  slug: matomo-rate-limits
rules:
- authorship: generated
  effective_rule_count: 104
  extends:
  - spectral:oas
  name: Matomo API Rules
  rule_count: 63
  severity_counts:
    error: 42
    hint: 0
    info: 2
    warn: 19
  slug: matomo-rules
scopes:
- name: Matomo Scopes
  scope_count: 3
  slug: matomo-scopes
  summary_line: 3 scopes · authorizationCode/clientCredentials/refreshToken
score:
  band: exemplar
  composite: 72.2
  coverage:
    artifact_dirs: 33
    catalog_earned: 71.5
    catalog_earned_first_party: 24.0
    catalog_gap: 43.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 100.0
    contract_governance: 18.2
    contract_quality: 49.0
    developer_ergonomics: 80.4
    discoverability: 73.3
    operational_transparency: 81.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - new-zealand
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 72.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 60
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
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 45.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/matomo/matomo-2026-06-20T185037.png
security:
- kind: authentication
  name: Matomo Authentication
  slug: matomo-authentication
  summary_line: apiKey/http/oauth2 · 4 schemes
- kind: domain-security
  name: Matomo Domain Security
  slug: matomo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Matomo Vulnerability Disclosure
  slug: matomo-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Matomo Trust Center
  slug: matomo-trust-center
  summary_line: ISO 27001, GDPR
skill_count: 5
skills:
- name: Connect an agent to Matomo over MCP
  slug: matomo-connect-an-agent-over-mcp
- name: Create a saved segment and report against it
  slug: matomo-create-and-apply-a-segment
- name: Discover a Matomo instance's actual API surface
  slug: matomo-discover-the-api-surface
- name: Onboard a new site and get its tracking code
  slug: matomo-onboard-a-new-site
- name: Pull a traffic report for a date range
  slug: matomo-pull-a-traffic-report
slug: matomo
tags:
- Analytics
- Web Analytics
- Open Source
- Privacy
- DataOwnership
- Self-Hosted
- GDPR
- Tag Management
- Conversion Optimization
- MCP
website: https://matomo.org
---
