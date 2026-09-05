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
  schema_version: 0.2
  score: 47.9
  scored_at: '2026-09-04'
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
  slug: appsflyer-account-connections-api
- baseURL: https://hq1.appsflyer.com/api/
  baseurl_source: declared
  description: The Account Integration API from AppsFlyer — 1 operation(s) for account integration.
  name: AppsFlyer Account Integration API
  slug: appsflyer-account-integration-api
- baseURL: https://hq1.appsflyer.com/api/
  baseurl_source: declared
  description: The Account splits API from AppsFlyer — 1 operation(s) for account splits.
  name: AppsFlyer Account splits API
  slug: appsflyer-account-splits-api
- baseURL: https://hq1.appsflyer.com/api/
  baseurl_source: declared
  description: The Active audiences API from AppsFlyer — 1 operation(s) for active audiences.
  name: AppsFlyer Active audiences API
  slug: appsflyer-active-audiences-api
- baseURL: https://hq1.appsflyer.com/api/
  baseurl_source: declared
  description: The Active integrations API from AppsFlyer — 2 operation(s) for active integrations.
  name: AppsFlyer Active integrations API
  slug: appsflyer-active-integrations-api
- baseURL: https://hq1.appsflyer.com/api/
  baseurl_source: declared
  description: The Ad Revenue raw data API from AppsFlyer — 3 operation(s) for ad revenue raw data.
  name: AppsFlyer Ad Revenue raw data API
  slug: appsflyer-ad-revenue-raw-data-api
- baseURL: https://hq1.appsflyer.com/api/
  baseurl_source: declared
  description: The Add excluded app API from AppsFlyer — 1 operation(s) for add excluded app.
  name: AppsFlyer Add excluded app API
  slug: appsflyer-add-excluded-app-api
- baseURL: https://hq1.appsflyer.com/api/
  baseurl_source: declared
  description: The Additional Identifiers Handling API from AppsFlyer — 1 operation(s) for additional identifiers handling.
  name: AppsFlyer Additional Identifiers Handling API
  slug: appsflyer-additional-identifiers-handling-api
- baseURL: https://hq1.appsflyer.com/api/
  baseurl_source: declared
  description: The Aggregate (user acquisition and retargeting) API from AppsFlyer — 5 operation(s) for aggregate (user acquisition and retargeting).
  name: AppsFlyer Aggregate (user acquisition and retargeting) API
  slug: appsflyer-aggregate-user-acquisition-and-retargeting-api
- baseURL: https://hq1.appsflyer.com/api/
  baseurl_source: declared
  description: The Allowed devices API from AppsFlyer — 2 operation(s) for allowed devices.
  name: AppsFlyer Allowed devices API
  slug: appsflyer-allowed-devices-api
- baseURL: https://hq1.appsflyer.com/api/
  baseurl_source: declared
  description: The Android deep linking request API from AppsFlyer — 1 operation(s) for android deep linking request.
  name: AppsFlyer Android deep linking request API
  slug: appsflyer-android-deep-linking-request-api
- baseURL: https://hq1.appsflyer.com/api/
  baseurl_source: declared
  description: The App management API from AppsFlyer — 2 operation(s) for app management.
  name: AppsFlyer App management API
  slug: appsflyer-app-management-api
- baseURL: https://hq1.appsflyer.com/api/
  baseurl_source: declared
  description: The Audience connections API from AppsFlyer — 1 operation(s) for audience connections.
  name: AppsFlyer Audience connections API
  slug: appsflyer-audience-connections-api
- baseURL: https://hq1.appsflyer.com/api/
  baseurl_source: declared
  description: The Audience split API from AppsFlyer — 1 operation(s) for audience split.
  name: AppsFlyer Audience split API
  slug: appsflyer-audience-split-api
- baseURL: https://hq1.appsflyer.com/api/
  baseurl_source: declared
  description: The Audience upload API from AppsFlyer — 1 operation(s) for audience upload.
  name: AppsFlyer Audience upload API
  slug: appsflyer-audience-upload-api
- baseURL: https://hq1.appsflyer.com/api/
  baseurl_source: declared
  description: The Audiences User Attribution Import API API from AppsFlyer — 1 operation(s) for audiences user attribution import api.
  name: AppsFlyer Audiences User Attribution Import API
  slug: appsflyer-audiences-user-attribution-import-api-api
- baseURL: https://hq1.appsflyer.com/api/
  baseurl_source: declared
  description: The Audit logs API from AppsFlyer — 1 operation(s) for audit logs.
  name: AppsFlyer Audit logs API
  slug: appsflyer-audit-logs-api
- baseURL: https://hq1.appsflyer.com/api/
  baseurl_source: declared
  description: The Authentication Token API from AppsFlyer — 1 operation(s) for authentication token.
  name: AppsFlyer Authentication Token API
  slug: appsflyer-authentication-token-api
- baseURL: https://hq1.appsflyer.com/api/
  baseurl_source: declared
  description: The Circuit breaker API from AppsFlyer — 1 operation(s) for circuit breaker.
  name: AppsFlyer Circuit breaker API
  slug: appsflyer-circuit-breaker-api
- baseURL: https://hq1.appsflyer.com/api/
  baseurl_source: declared
  description: The Click Engagement API from AppsFlyer — 1 operation(s) for click engagement.
  name: AppsFlyer Click Engagement API
  slug: appsflyer-click-engagement-api
- baseURL: https://hq1.appsflyer.com/api/
  baseurl_source: declared
  description: The Cohort Report API from AppsFlyer — 1 operation(s) for cohort report.
  name: AppsFlyer Cohort Report API
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
  slug: appsflyer-conversion-value-cv-schema-api
- baseURL: https://hq1.appsflyer.com/api/
  baseurl_source: declared
  description: The Create audience API from AppsFlyer — 1 operation(s) for create audience.
  name: AppsFlyer Create audience API
  slug: appsflyer-create-audience-api
- baseURL: https://hq1.appsflyer.com/api/
  baseurl_source: declared
  description: The Download Events API from AppsFlyer — 1 operation(s) for download events.
  name: AppsFlyer Download Events API
  slug: appsflyer-download-events-api
- baseURL: https://hq1.appsflyer.com/api/
  baseurl_source: declared
  description: The Event Types API from AppsFlyer — 1 operation(s) for event types.
  name: AppsFlyer Event Types API
  slug: appsflyer-event-types-api
- baseURL: https://hq1.appsflyer.com/api/
  baseurl_source: declared
  description: The Events API from AppsFlyer — 1 operation(s) for events.
  name: AppsFlyer Events API
  slug: appsflyer-events-api
- baseURL: https://hq1.appsflyer.com/api/
  baseurl_source: declared
  description: The Events management API from AppsFlyer — 2 operation(s) for events management.
  name: AppsFlyer Events management API
  slug: appsflyer-events-management-api
- baseURL: https://hq1.appsflyer.com/api/
  baseurl_source: declared
  description: The Freshness Report API from AppsFlyer — 1 operation(s) for freshness report.
  name: AppsFlyer Freshness Report API
  slug: appsflyer-freshness-report-api
- baseURL: https://hq1.appsflyer.com/api/
  baseurl_source: declared
  description: The Generate secret key API from AppsFlyer — 1 operation(s) for generate secret key.
  name: AppsFlyer Generate secret key API
  slug: appsflyer-generate-secret-key-api
- baseURL: https://hq1.appsflyer.com/api/
  baseurl_source: declared
  description: The Get app list API from AppsFlyer — 1 operation(s) for get app list.
  name: AppsFlyer Get app list API
  slug: appsflyer-get-app-list-api
- baseURL: https://hq1.appsflyer.com/api/
  baseurl_source: declared
  description: The Get config API from AppsFlyer — 1 operation(s) for get config.
  name: AppsFlyer Get config API
  slug: appsflyer-get-config-api
- baseURL: https://hq1.appsflyer.com/api/
  baseurl_source: declared
  description: The Google Play install referrer API from AppsFlyer — 1 operation(s) for google play install referrer.
  name: AppsFlyer Google Play install referrer API
  slug: appsflyer-google-play-install-referrer-api
- baseURL: https://hq1.appsflyer.com/api/
  baseurl_source: declared
  description: The Import audience API from AppsFlyer — 1 operation(s) for import audience.
  name: AppsFlyer Import audience API
  slug: appsflyer-import-audience-api
- baseURL: https://hq1.appsflyer.com/api/
  baseurl_source: declared
  description: The Impression Engagement API from AppsFlyer — 1 operation(s) for impression engagement.
  name: AppsFlyer Impression Engagement API
  slug: appsflyer-impression-engagement-api
- baseURL: https://hq1.appsflyer.com/api/
  baseurl_source: declared
  description: The Inapp Events API from AppsFlyer — 1 operation(s) for inapp events.
  name: AppsFlyer Inapp Events API
  slug: appsflyer-inapp-events-api
- baseURL: https://hq1.appsflyer.com/api/
  baseurl_source: declared
  description: The InCost job status API from AppsFlyer — 1 operation(s) for incost job status.
  name: AppsFlyer InCost job status API
  slug: appsflyer-incost-job-status-api
- baseURL: https://hq1.appsflyer.com/api/
  baseurl_source: declared
  description: The InCost uploader API from AppsFlyer — 1 operation(s) for incost uploader.
  name: AppsFlyer InCost uploader API
  slug: appsflyer-incost-uploader-api
- baseURL: https://hq1.appsflyer.com/api/
  baseurl_source: declared
  description: The Integration settings API from AppsFlyer — 2 operation(s) for integration settings.
  name: AppsFlyer Integration settings API
  slug: appsflyer-integration-settings-api
- baseURL: https://hq1.appsflyer.com/api/
  baseurl_source: declared
  description: The iOS deep linking request API from AppsFlyer — 1 operation(s) for ios deep linking request.
  name: AppsFlyer iOS deep linking request API
  slug: appsflyer-ios-deep-linking-request-api
- baseURL: https://hq1.appsflyer.com/api/
  baseurl_source: declared
  description: The Manage Push API configuration API from AppsFlyer — 1 operation(s) for manage push api configuration.
  name: AppsFlyer Manage Push API configuration API
  slug: appsflyer-manage-push-api-configuration-api
- baseURL: https://hq1.appsflyer.com/api/
  baseurl_source: declared
  description: The Managing roles API from AppsFlyer — 1 operation(s) for managing roles.
  name: AppsFlyer Managing roles API
  slug: appsflyer-managing-roles-api
- baseURL: https://hq1.appsflyer.com/api/
  baseurl_source: declared
  description: The Managing users in bulk API from AppsFlyer — 2 operation(s) for managing users in bulk.
  name: AppsFlyer Managing users in bulk API
  slug: appsflyer-managing-users-in-bulk-api
- baseURL: https://hq1.appsflyer.com/api/
  baseurl_source: declared
  description: The Master Report API from AppsFlyer — 1 operation(s) for master report.
  name: AppsFlyer Master Report API
  slug: appsflyer-master-report-api
- baseURL: https://hq1.appsflyer.com/api/
  baseurl_source: declared
  description: The Measure first app opens API from AppsFlyer — 1 operation(s) for measure first app opens.
  name: AppsFlyer Measure first app opens API
  slug: appsflyer-measure-first-app-opens-api
- baseURL: https://hq1.appsflyer.com/api/
  baseurl_source: declared
  description: The Measure in-app events API from AppsFlyer — 1 operation(s) for measure in-app events.
  name: AppsFlyer Measure in-app events API
  slug: appsflyer-measure-in-app-events-api
- baseURL: https://hq1.appsflyer.com/api/
  baseurl_source: declared
  description: The Measure sessions API from AppsFlyer — 1 operation(s) for measure sessions.
  name: AppsFlyer Measure sessions API
  slug: appsflyer-measure-sessions-api
- baseURL: https://hq1.appsflyer.com/api/
  baseurl_source: declared
  description: The Message Fields API from AppsFlyer — 1 operation(s) for message fields.
  name: AppsFlyer Message Fields API
  slug: appsflyer-message-fields-api
- baseURL: https://hq1.appsflyer.com/api/
  baseurl_source: declared
  description: The OneLink REST API v2.0 API from AppsFlyer — 4 operation(s) for onelink rest api v2.0.
  name: AppsFlyer OneLink REST API v2.0 API
  slug: appsflyer-onelink-rest-api-v2-0-api
- baseURL: https://hq1.appsflyer.com/api/
  baseurl_source: declared
  description: The Pauses audience API from AppsFlyer — 1 operation(s) for pauses audience.
  name: AppsFlyer Pauses audience API
  slug: appsflyer-pauses-audience-api
- baseURL: https://hq1.appsflyer.com/api/
  baseurl_source: declared
  description: The Postbacks API from AppsFlyer — 4 operation(s) for postbacks.
  name: AppsFlyer Postbacks API
  slug: appsflyer-postbacks-api
- baseURL: https://hq1.appsflyer.com/api/
  baseurl_source: declared
  description: The Production API from AppsFlyer — 7 operation(s) for production.
  name: AppsFlyer Production API
  slug: appsflyer-production-api
- baseURL: https://hq1.appsflyer.com/api/
  baseurl_source: declared
  description: The Protect360 fraud API from AppsFlyer — 6 operation(s) for protect360 fraud.
  name: AppsFlyer Protect360 fraud API
  slug: appsflyer-protect360-fraud-api
- baseURL: https://hq1.appsflyer.com/api/
  baseurl_source: declared
  description: The Raw data reports (non-organic) API from AppsFlyer — 4 operation(s) for raw data reports (non-organic).
  name: AppsFlyer Raw data reports (non-organic) API
  slug: appsflyer-raw-data-reports-non-organic-api
- baseURL: https://hq1.appsflyer.com/api/
  baseurl_source: declared
  description: The Raw data reports (organic) API from AppsFlyer — 4 operation(s) for raw data reports (organic).
  name: AppsFlyer Raw data reports (organic) API
  slug: appsflyer-raw-data-reports-organic-api
- baseURL: https://hq1.appsflyer.com/api/
  baseurl_source: declared
  description: The Remove excluded app API from AppsFlyer — 1 operation(s) for remove excluded app.
  name: AppsFlyer Remove excluded app API
  slug: appsflyer-remove-excluded-app-api
- baseURL: https://hq1.appsflyer.com/api/
  baseurl_source: declared
  description: The Report API from AppsFlyer — 1 operation(s) for report.
  name: AppsFlyer Report API
  slug: appsflyer-report-api
- baseURL: https://hq1.appsflyer.com/api/
  baseurl_source: declared
  description: The Retargeting API from AppsFlyer — 2 operation(s) for retargeting.
  name: AppsFlyer Retargeting API
  slug: appsflyer-retargeting-api
- baseURL: https://hq1.appsflyer.com/api/
  baseurl_source: declared
  description: The Revoke secret key API from AppsFlyer — 1 operation(s) for revoke secret key.
  name: AppsFlyer Revoke secret key API
  slug: appsflyer-revoke-secret-key-api
- baseURL: https://hq1.appsflyer.com/api/
  baseurl_source: declared
  description: The SKAN conversion studio API API from AppsFlyer — 1 operation(s) for skan conversion studio api.
  name: AppsFlyer SKAN conversion studio API
  slug: appsflyer-skan-conversion-studio-api-api
- baseURL: https://hq1.appsflyer.com/api/
  baseurl_source: declared
  description: The SKAN CV schema API for ad networks API from AppsFlyer — 2 operation(s) for skan cv schema api for ad networks.
  name: AppsFlyer SKAN CV schema API for ad networks API
  slug: appsflyer-skan-cv-schema-api-for-ad-networks-api
- baseURL: https://hq1.appsflyer.com/api/
  baseurl_source: declared
  description: The SKAN performance report API from AppsFlyer — 1 operation(s) for skan performance report.
  name: AppsFlyer SKAN performance report API
  slug: appsflyer-skan-performance-report-api
- baseURL: https://hq1.appsflyer.com/api/
  baseurl_source: declared
  description: The SKAN postbacks API from AppsFlyer — 1 operation(s) for skan postbacks.
  name: AppsFlyer SKAN postbacks API
  slug: appsflyer-skan-postbacks-api
- baseURL: https://hq1.appsflyer.com/api/
  baseurl_source: declared
  description: The Store commission rates API from AppsFlyer — 2 operation(s) for store commission rates.
  name: AppsFlyer Store commission rates API
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
  slug: appsflyer-tax-rate-rules-api
- baseURL: https://hq1.appsflyer.com/api/
  baseurl_source: declared
  description: The Test API from AppsFlyer — 1 operation(s) for test.
  name: AppsFlyer Test API
  slug: appsflyer-test-api
- baseURL: https://hq1.appsflyer.com/api/
  baseurl_source: declared
  description: The Unique partner integration parameters API from AppsFlyer — 1 operation(s) for unique partner integration parameters.
  name: AppsFlyer Unique partner integration parameters API
  slug: appsflyer-unique-partner-integration-parameters-api
- baseURL: https://hq1.appsflyer.com/api/
  baseurl_source: declared
  description: The Update config API from AppsFlyer — 1 operation(s) for update config.
  name: AppsFlyer Update config API
  slug: appsflyer-update-config-api
- baseURL: https://hq1.appsflyer.com/api/
  baseurl_source: declared
  description: The URL Validation API from AppsFlyer — 1 operation(s) for url validation.
  name: AppsFlyer URL Validation API
  slug: appsflyer-url-validation-api
artifact_total: 119
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
  title: ''
  type: CapabilityMap
  url: capabilities/appsflyer-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/appsflyer-raw-data-pull-api-v2-token-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/appsflyer-raw-data-pull-api-v1-token-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/appsflyer-aggregate-pull-api-v2-token-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/appsflyer-aggregate-pull-api-v1-token-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/appsflyer-master-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/appsflyer-master-freshness-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/appsflyer-cohort-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/appsflyer-server-to-server-events-api-for-mobile-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/appsflyer-legacy-server-to-server-events-api-for-mobile-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/appsflyer-web-server-to-server-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/appsflyer-pcconsolectv-events-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/appsflyer-pcconsolectv-client-app-events-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/appsflyer-engagements-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/appsflyer-deep-linking-rest-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/appsflyer-preload-measurement-api-1-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/appsflyer-preload-c2s-measurement-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/appsflyer-gcd-api-for-sdk-attribution-testing-1-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/appsflyer-app-management-api-v20-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/appsflyer-app-list-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/appsflyer-user-management-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/appsflyer-audit-public-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/appsflyer-partner-integration-settings-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/appsflyer-adrevenue-account-integrations-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/appsflyer-incost-api-1-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/appsflyer-test-console-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/appsflyer-push-api-configuration-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/appsflyer-audience-external-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/appsflyer-audience-import-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/appsflyer-audiences-user-attribution-import-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/appsflyer-additional-identifiers-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/appsflyer-onelink-api-v20-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/appsflyer-skan-aggregated-performance-report-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/appsflyer-skan-aggregated-postback-by-arrival-date-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/appsflyer-skan-cv-schema-api-for-advertisers-1-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/appsflyer-skan-cv-schema-api-for-ad-networks-2-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/appsflyer-skan-conversion-studio-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/appsflyer-opendsr-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/appsflyer-click-signing-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/appsflyer-roi360-net-revenue-api-v20-overlay.yaml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/appsflyer-domain-security.yml
- group: auth
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
  title: ''
  type: Packages
  url: packages/appsflyer-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/appsflyer-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/appsflyer-well-known.yml
- group: other
  title: ''
  type: APICatalog
  url: https://dev.appsflyer.com/.well-known/api-catalog
- group: agent
  title: ''
  type: MCPServer
  url: mcp/appsflyer-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/appsflyer-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/appsflyer-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/appsflyer-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/appsflyer-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/appsflyer-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/appsflyer-conventions.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/appsflyer-sandbox.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/appsflyer-changelog.yml
- group: design
  title: ''
  type: Components
  url: components/appsflyer-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/appsflyer-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/appsflyer-push-api-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/appsflyer-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/appsflyer-trust-center.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/appsflyer-plans-pricing.yml
- group: operate
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
overview: 'AppsFlyer publishes 70 APIs on the [APIs.io](https://apis.io/) network, including Account connections API, Account Integration API, Account splits API, and 67 more. Tagged areas include Company, Mobile Attribution, Marketing Analytics, Mobile Measurement, and Deep Linking.


  The AppsFlyer catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  AppsFlyer''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 74 more developer resources.'
plans:
- name: Appsflyer Plans Pricing
  plan_count: 3
  slug: appsflyer-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 11
  name: Appsflyer Rate Limits
  slug: appsflyer-rate-limits
score:
  band: strong
  composite: 64.0
  coverage:
    artifact_dirs: 24
    catalog_earned: 61.0
    catalog_earned_first_party: 24.0
    catalog_gap: 54.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 92.1
    commercial_clarity: 92.1
    contract_governance: 4.5
    contract_quality: 60.1
    developer_ergonomics: 58.9
    discoverability: 87.0
    governance: 4.5
    operational_transparency: 73.7
  previous_composite: 64.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 70
    mcp: first-party
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
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
- Advertising Technology
- Mobile SDK
- Agentic AI
website: https://www.appsflyer.com/
---
