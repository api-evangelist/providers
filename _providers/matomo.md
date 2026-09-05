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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 37.8
  scored_at: '2026-09-04'
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
  slug: matomo-index-php-api
- baseURL: https://{matomo_host}/matomo.php
  baseurl_source: declared
  description: The Matomo Tracking API — the server-side ingest entrypoint at /matomo.php that records pageviews, events, goals, ecommerce orders, site searches and content interactions. It is the counterpart to the
  name: Matomo Tracking API (matomo.php entrypoint)
  slug: matomo-matomo-php-api
- baseURL: https://{matomo_host}/index.php
  baseurl_source: declared
  description: Exposes the AbTesting API for managing experiments, embedding experiment scripts, and reading experiment reports.
  name: Matomo Ab Testing API
  slug: matomo-abtesting-api
- baseURL: https://{matomo_host}/index.php
  baseurl_source: declared
  description: 'The Actions API lets you request reports for all your Visitor Actions: Page URLs, Page titles, Events, Content Tracking, File Downloads and Clicks on external websites. For example, "getPageTitles" wi'
  name: Matomo Actions API
  slug: matomo-actions-api
- baseURL: https://{matomo_host}/index.php
  baseurl_source: declared
  description: Exposes Activity Log API endpoints for listing activity entries, counting matches, and resolving the permitted date range for the current caller.
  name: Matomo Activity Log API
  slug: matomo-activitylog-api
- baseURL: https://{matomo_host}/index.php
  baseurl_source: declared
  description: Exposes API endpoints for managing advertising conversion export configurations. These methods let users list, inspect, create, update, and delete configured exports and access tokens.
  name: Matomo Advertising Conversion Export API
  slug: matomo-advertisingconversionexport-api
- baseURL: https://{matomo_host}/index.php
  baseurl_source: declared
  description: Provides API methods to create, update, delete, and query annotations.
  name: Matomo Annotations API
  slug: matomo-annotations-api
- baseURL: https://{matomo_host}/index.php
  baseurl_source: declared
  description: 'This API is the <a href=''https://matomo.org/docs/analytics-api/metadata/'' rel=''noreferrer'' target=''_blank''>Metadata API</a>: it gives information about all other available APIs methods, as well as pro'
  name: Matomo API
  slug: matomo-api-api
- baseURL: https://{matomo_host}/index.php
  baseurl_source: declared
  description: 'Provides Reporting API endpoints for reading OpenAPI plugin configuration and specifications. Exposes endpoints to return the effective plugin list for spec generation, read pre-generated spec files, '
  name: Matomo API Reference API
  slug: matomo-apireference-api
- baseURL: https://{matomo_host}/index.php
  baseurl_source: declared
  description: Exposes reporting API endpoints for aggregated bandwidth metrics.
  name: Matomo Bandwidth API
  slug: matomo-bandwidth-api
- baseURL: https://{matomo_host}/index.php
  baseurl_source: declared
  description: Exposes cohort reports grouped by the period of a visitor's first visit. These endpoints transform archived first-visit cohort data into table and chart responses for the Cohorts plugin.
  name: Matomo Cohorts API
  slug: matomo-cohorts-api
- baseURL: https://{matomo_host}/index.php
  baseurl_source: declared
  description: The Contents API exposes content tracking reports grouped by content name and content piece.
  name: Matomo Contents API
  slug: matomo-contents-api
- baseURL: https://{matomo_host}/index.php
  baseurl_source: declared
  description: Provides administrative API methods for scheduling, archiving, tracking failures, and opt-out code generation.
  name: Matomo Core Admin Home API
  slug: matomo-coreadminhome-api
- baseURL: https://{matomo_host}/index.php
  baseurl_source: declared
  description: Exposes Crash Analytics endpoints for managing tracked crashes and querying crash reports. Includes summary, drill-down, historical, and realtime reporting APIs for a single site.
  name: Matomo Crash Analytics API
  slug: matomo-crashanalytics-api
- baseURL: https://{matomo_host}/index.php
  baseurl_source: declared
  description: Exposes Custom Alerts API endpoints for managing alert definitions and reading triggered alert data. These methods let callers create, update, fetch, delete, and evaluate alerts for one or more sites.
  name: Matomo Custom Alerts API
  slug: matomo-customalerts-api
- baseURL: https://{matomo_host}/index.php
  baseurl_source: declared
  description: The Custom Dimensions API lets you manage and access reports for your configured Custom Dimensions.
  name: Matomo Custom Dimensions API
  slug: matomo-customdimensions-api
- baseURL: https://{matomo_host}/index.php
  baseurl_source: declared
  description: Provides API methods for custom JavaScript tracker configuration.
  name: Matomo Custom Js Tracker API
  slug: matomo-customjstracker-api
- baseURL: https://{matomo_host}/index.php
  baseurl_source: declared
  description: Exposes Custom Reports configuration and reporting endpoints. Use it to create, duplicate, manage, and query custom report definitions and their archived data.
  name: Matomo Custom Reports API
  slug: matomo-customreports-api
- baseURL: https://{matomo_host}/index.php
  baseurl_source: declared
  description: The Dashboard API lets you manage user dashboards and retrieve their widget configurations.
  name: Matomo Dashboard API
  slug: matomo-dashboard-api
- baseURL: https://{matomo_host}/index.php
  baseurl_source: declared
  description: The DevicePlugins API lets you access reports about device plugins such as browser plugins.
  name: Matomo Device Plugins API
  slug: matomo-deviceplugins-api
- baseURL: https://{matomo_host}/index.php
  baseurl_source: declared
  description: The DevicesDetection API lets you access reports about your visitors' device types, brands, models, operating systems, and browsers.
  name: Matomo Devices Detection API
  slug: matomo-devicesdetection-api
- baseURL: https://{matomo_host}/index.php
  baseurl_source: declared
  description: The Events API lets you request reports about your users' Custom Events. Events are tracked using the Javascript Tracker trackEvent() function, or using the [Tracking HTTP API](https://developer.matom
  name: Matomo Events API
  slug: matomo-events-api
- baseURL: https://{matomo_host}/index.php
  baseurl_source: declared
  description: Provides API methods for submitting product feedback and managing feedback reminders.
  name: Matomo Feedback API
  slug: matomo-feedback-api
- baseURL: https://{matomo_host}/index.php
  baseurl_source: declared
  description: Exposes the Form Analytics API for managing tracked forms and retrieving form performance reports. Use these endpoints to create, update, archive, and delete configured forms, inspect form metadata, a
  name: Matomo Form Analytics API
  slug: matomo-formanalytics-api
- baseURL: https://{matomo_host}/index.php
  baseurl_source: declared
  description: Exposes the Funnels reporting and management API for funnel analytics configuration. Includes endpoints for funnel reports, funnel definitions, and pattern validation helpers.
  name: Matomo Funnels API
  slug: matomo-funnels-api
- baseURL: https://{matomo_host}/index.php
  baseurl_source: declared
  description: Goals API lets you Manage existing goals, via "updateGoal" and "deleteGoal", create new Goals via "addGoal", or list existing Goals for one or several websites via "getGoals" If you are <a href='https
  name: Matomo Goals API
  slug: matomo-goals-api
- baseURL: https://{matomo_host}/index.php
  baseurl_source: declared
  description: 'Exposes the Heatmap & Session Recording API endpoints for managing configurations and retrieving recorded activity. Heatmap coordinates use relative values: X and Y positions range from 0 to 2000, whe'
  name: Matomo Heatmap Session Recording API
  slug: matomo-heatmapsessionrecording-api
- baseURL: https://{matomo_host}/index.php
  baseurl_source: declared
  description: 'The ImageGraph.get API call lets you generate beautiful static PNG Graphs for any existing Matomo report. Supported graph types are: line plot, 2D/3D pie chart and vertical bar chart. A few notes abou'
  name: Matomo Image Graph API
  slug: matomo-imagegraph-api
- baseURL: https://{matomo_host}/index.php
  baseurl_source: declared
  description: Provides API methods for insight and mover/shaker comparisons between report periods.
  name: Matomo Insights API
  slug: matomo-insights-api
- baseURL: https://{matomo_host}/index.php
  baseurl_source: declared
  description: The LanguagesManager API lets you access existing Matomo translations, and change Users languages preferences. "getTranslationsForLanguage" will return all translation strings for a given language, so
  name: Matomo Languages Manager API
  slug: matomo-languagesmanager-api
- baseURL: https://{matomo_host}/index.php
  baseurl_source: declared
  description: The Live! API lets you access complete visit level information about your visitors. Combined with the power of <a href='https://matomo.org/docs/analytics-api/segmentation/' target='_blank'>Segmentatio
  name: Matomo Live API
  slug: matomo-live-api
- baseURL: https://{matomo_host}/index.php
  baseurl_source: declared
  description: Provides API methods for login-related administration tasks.
  name: Matomo Login API
  slug: matomo-login-api
- baseURL: https://{matomo_host}/index.php
  baseurl_source: declared
  description: Exposes reporting API endpoints for marketing campaign dimensions and drill-down reports. Includes campaign IDs, names, keywords, source and medium dimensions, and hierarchical subtables.
  name: Matomo Marketing Campaigns Reporting API
  slug: matomo-marketingcampaignsreporting-api
- baseURL: https://{matomo_host}/index.php
  baseurl_source: declared
  description: The Marketplace API lets you manage your license key so you can download & install in one-click <a target="_blank" rel="noreferrer" href="https://matomo.org/recommends/premium-plugins/">paid premium p
  name: Matomo Marketplace API
  slug: matomo-marketplace-api
- baseURL: https://{matomo_host}/index.php
  baseurl_source: declared
  description: Exposes Media Analytics reports for video and audio plays, engagement, resources, and player usage. Includes real-time endpoints for recent activity and archive-backed endpoints for aggregated media r
  name: Matomo Media Analytics API
  slug: matomo-mediaanalytics-api
- baseURL: https://{matomo_host}/index.php
  baseurl_source: declared
  description: The MobileMessaging API lets you manage SMS credentials, phone number verification, and SMS account settings.
  name: Matomo Mobile Messaging API
  slug: matomo-mobilemessaging-api
- baseURL: https://{matomo_host}/index.php
  baseurl_source: declared
  description: The MultiSites API lets you request the key metrics (visits, page views, revenue) for all Websites in Matomo.
  name: Matomo Multi Sites API
  slug: matomo-multisites-api
- baseURL: https://{matomo_host}/index.php
  baseurl_source: declared
  description: Exposes super-user OAuth2 client management endpoints for Matomo. This API lists configured scopes and lets administrators create, inspect, update, rotate, activate, and delete OAuth2 clients.
  name: Matomo O Auth2 API
  slug: matomo-oauth2-api
- baseURL: https://{matomo_host}/index.php
  baseurl_source: declared
  description: The Overlay API exposes translation data and overlay-specific page transition reports.
  name: Matomo Overlay API
  slug: matomo-overlay-api
- baseURL: https://{matomo_host}/index.php
  baseurl_source: declared
  description: Provides reporting API methods for aggregated page performance metrics.
  name: Matomo Page Performance API
  slug: matomo-pageperformance-api
- baseURL: https://{matomo_host}/index.php
  baseurl_source: declared
  description: The PrivacyManager API lets you manage GDPR workflows, anonymization settings, and privacy compliance controls.
  name: Matomo Privacy Manager API
  slug: matomo-privacymanager-api
- baseURL: https://{matomo_host}/index.php
  baseurl_source: declared
  description: The Referrers API lets you access reports about websites, search engines, keywords, social networks, AI assistants, and campaigns used to access your website. For example, "getKeywords" returns all se
  name: Matomo Referrers API
  slug: matomo-referrers-api
- baseURL: https://{matomo_host}/index.php
  baseurl_source: declared
  description: Provides API methods for screen resolution and device configuration reports.
  name: Matomo Resolution API
  slug: matomo-resolution-api
- baseURL: https://{matomo_host}/index.php
  baseurl_source: declared
  description: Provides API endpoints for managing roll-up websites and their source site assignments. Use these methods to create roll-ups, update their configuration, and list the configured roll-up sites with the
  name: Matomo Roll Up Reporting API
  slug: matomo-rollupreporting-api
- baseURL: https://{matomo_host}/index.php
  baseurl_source: declared
  description: The ScheduledReports API lets you manage Scheduled Email reports, as well as generate, download or email any existing report. "generateReport" will generate the requested report (for a specific date r
  name: Matomo Scheduled Reports API
  slug: matomo-scheduledreports-api
- baseURL: https://{matomo_host}/index.php
  baseurl_source: declared
  description: Provides SearchEngineKeywordsPerformance API endpoints for imported keyword and crawl-performance reports. Exposes combined and provider-specific reports for Google, Bing, and Yandex search data. \Plu
  name: Matomo Search Engine Keywords Performance API
  slug: matomo-searchenginekeywordsperformance-api
- baseURL: https://{matomo_host}/index.php
  baseurl_source: declared
  description: The SegmentEditor API lets you add, update, delete custom Segments, and list saved segments.
  name: Matomo Segment Editor API
  slug: matomo-segmenteditor-api
- baseURL: https://{matomo_host}/index.php
  baseurl_source: declared
  description: 'The SEO API lets you access a list of SEO metrics for the specified URL: Bing indexed pages and age of the Domain name.'
  name: Matomo SEO API
  slug: matomo-seo-api
- baseURL: https://{matomo_host}/index.php
  baseurl_source: declared
  description: 'The SitesManager API gives you full control on Websites in Matomo (create, update and delete), and many methods to retrieve websites based on various attributes. This API lets you create websites via '
  name: Matomo Sites Manager API
  slug: matomo-sitesmanager-api
- baseURL: https://{matomo_host}/index.php
  baseurl_source: declared
  description: Exposes the Tag Manager API for managing containers, versions, tags, triggers, and variables. The endpoints also provide installation metadata, publishing workflows, preview controls, and import/expor
  name: Matomo Tag Manager API
  slug: matomo-tagmanager-api
- baseURL: https://{matomo_host}/index.php
  baseurl_source: declared
  description: Provides API methods for Tour challenges and engagement levels.
  name: Matomo Tour API
  slug: matomo-tour-api
- baseURL: https://{matomo_host}/index.php
  baseurl_source: declared
  description: Provides API methods for transition reports around a specific page action.
  name: Matomo Transitions API
  slug: matomo-transitions-api
- baseURL: https://{matomo_host}/index.php
  baseurl_source: declared
  description: Provides API methods for managing two-factor authentication.
  name: Matomo Two Factor Auth API
  slug: matomo-twofactorauth-api
- baseURL: https://{matomo_host}/index.php
  baseurl_source: declared
  description: The UserCountry API lets you access reports about your visitors' Countries and Continents.
  name: Matomo User Country API
  slug: matomo-usercountry-api
- baseURL: https://{matomo_host}/index.php
  baseurl_source: declared
  description: Provides API methods for User ID reports.
  name: Matomo User ID API
  slug: matomo-userid-api
- baseURL: https://{matomo_host}/index.php
  baseurl_source: declared
  description: The UserLanguage API lets you access reports about your Visitors language setting
  name: Matomo User Language API
  slug: matomo-userlanguage-api
- baseURL: https://{matomo_host}/index.php
  baseurl_source: declared
  description: The UsersManager API lets you Manage Users and their permissions to access specific websites. You can create users via "addUser", update existing users via "updateUser" and delete users via "deleteUse
  name: Matomo Users Manager API
  slug: matomo-usersmanager-api
- baseURL: https://{matomo_host}/index.php
  baseurl_source: declared
  description: VisitFrequency API lets you access a list of metrics related to Returning Visitors.
  name: Matomo Visit Frequency API
  slug: matomo-visitfrequency-api
- baseURL: https://{matomo_host}/index.php
  baseurl_source: declared
  description: VisitorInterest API lets you access visitor engagement distribution reports, including visits by pages viewed, visit duration, days since last visit, and visit count.
  name: Matomo Visitor Interest API
  slug: matomo-visitorinterest-api
- baseURL: https://{matomo_host}/index.php
  baseurl_source: declared
  description: VisitsSummary API lets you access the core web analytics metrics (visits, unique visitors, count of actions (page views & downloads & clicks on outlinks), time on site, bounces and converted visits.
  name: Matomo Visits Summary API
  slug: matomo-visitssummary-api
- baseURL: https://{matomo_host}/index.php
  baseurl_source: declared
  description: VisitTime API lets you access reports by Hour (Server time), and by Hour Local Time of your visitors.
  name: Matomo Visit Time API
  slug: matomo-visittime-api
artifact_total: 76
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
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
  title: ''
  type: CapabilityMap
  url: capabilities/matomo-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/matomo-live-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/matomo-goals-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/matomo-segment-editor-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/matomo-sites-manager-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/matomo-tag-manager-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/matomo-users-manager-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/matomo-crash-analytics-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/matomo-heatmap-session-recording-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/matomo-form-analytics-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/matomo-referrers-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/matomo-funnels-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/matomo-actions-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/matomo-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/matomo-ab-testing-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/matomo-media-analytics-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/matomo-custom-reports-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/matomo-mobile-messaging-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/matomo-search-engine-keywords-performance-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/matomo-marketing-campaigns-reporting-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/matomo-visits-summary-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/matomo-events-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/matomo-languages-manager-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/matomo-devices-detection-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/matomo-oauth2-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/matomo-user-country-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/matomo-annotations-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/matomo-custom-alerts-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/matomo-advertising-conversion-export-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/matomo-custom-dimensions-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/matomo-privacy-manager-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/matomo-scheduled-reports-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/matomo-dashboard-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/matomo-insights-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/matomo-transitions-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/matomo-visitor-interest-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/matomo-activity-log-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/matomo-api-reference-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/matomo-core-admin-home-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/matomo-feedback-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/matomo-multi-sites-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/matomo-roll-up-reporting-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/matomo-tour-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/matomo-visit-time-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/matomo-cohorts-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/matomo-contents-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/matomo-marketplace-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/matomo-overlay-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/matomo-resolution-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/matomo-user-language-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/matomo-bandwidth-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/matomo-custom-js-tracker-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/matomo-device-plugins-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/matomo-image-graph-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/matomo-login-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/matomo-page-performance-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/matomo-seo-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/matomo-two-factor-auth-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/matomo-user-id-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/matomo-visit-frequency-overlay.yaml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/
- group: agent
  title: ''
  type: MCPServer
  url: mcp/matomo-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/matomo-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/matomo-agentic-access.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/matomo-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/matomo-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/matomo-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/matomo-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/matomo-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/matomo-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/matomo-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/matomo-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/matomo-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/matomo-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://matomo.org/security/
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/matomo-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.matomo.cloud/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/matomo-changelog.yml
- group: build
  title: ''
  type: CLI
  url: cli/matomo-cli.yml
- group: design
  title: ''
  type: Components
  url: components/matomo-components.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/matomo-sandbox.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/matomo-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/matomo-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/matomo-finops.yml
- group: auth
  title: ''
  type: Security
  url: https://matomo.org/security/
- group: auth
  title: ''
  type: TrustCenter
  url: security/matomo-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/matomo-vulnerability-disclosure.yml
- group: auth
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
- name: Matomo Finops
  service_category: API
  slug: matomo-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/matomo.png
layout: provider
mcp_servers:
- description: ''
  name: Matomo MCP Server
  slug: matomo-mcp-server
modified: '2026-08-13'
name: Matomo
nav: Providers
network: true
overview: 'Matomo publishes 61 APIs on the [APIs.io](https://apis.io/) network, including Reporting API (index.php entrypoint), Tracking API (matomo.php entrypoint), Ab Testing API, and 58 more. Tagged areas include Analytics, Web Analytics, Open-Source, Privacy, and Data Ownership.


  Matomo''s developer surface includes authentication, changelog, CLI, sandbox, documentation, API reference, getting-started guide, and 103 more developer resources.'
plans:
- name: Matomo Plans Pricing
  plan_count: 7
  slug: matomo-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 4
  name: Matomo Rate Limits
  slug: matomo-rate-limits
scopes:
- name: Matomo Scopes
  scope_count: 3
  slug: matomo-scopes
  summary_line: 3 scopes · authorizationCode/clientCredentials/refreshToken
score:
  band: exemplar
  composite: 67.4
  coverage:
    artifact_dirs: 27
    catalog_earned: 64.0
    catalog_earned_first_party: 24.0
    catalog_gap: 51.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 100.0
    commercial_clarity: 100.0
    contract_governance: 4.5
    contract_quality: 50.4
    developer_ergonomics: 80.4
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 81.6
  previous_composite: 67.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 61
    mcp: first-party
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/matomo/refs/heads/main/screenshots/matomo-2026-06-20T185037.png
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
slug: matomo
tags:
- Analytics
- Web Analytics
- Open-Source
- Privacy
- Data Ownership
- Self-Hosted
- GDPR
- Tag Management
- Conversion Optimization
- MCP
website: https://matomo.org
---
