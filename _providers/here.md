---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
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
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: false
    dry_run_mode: true
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: verified
    mcp_server: platform
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: mostly
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 55.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 318
  human_in_the_loop: 14
  name: Here Agentic Access
  operation_count: 743
  slug: here-agentic-access
  summary_line: 743 operations · 318 acting · 14 human-in-the-loop
api_count: 48
apis:
- description: Forward and reverse geocoding, address lookup, place discovery, browse, and details. Returns rich location data including addresses, places, categories, and geometry.
  name: HERE Geocoding and Search API
  slug: geocoding-search
- description: Type-ahead search returning place and address suggestions for partial queries, sharing the geocoding and search dataset.
  name: HERE Autosuggest API
  slug: autosuggest
- description: Vehicle routing problem (VRP) solver for fleets, with time windows, capacities, breaks, skills, multi-trip, and pickup-and-delivery constraints.
  name: HERE Tour Planning API
  slug: tour-planning
- description: Multi-modal public transit routing, station and stop lookup, departure boards, and next-departure data for transit-enabled apps.
  name: HERE Public Transit API
  slug: public-transit
- description: Current conditions, forecasts, and severe weather alerts at a coordinate or destination, intended to enrich routing, ETAs, and travel planning.
  name: HERE Destination Weather API
  slug: destination-weather
- description: Raster, vector, satellite, and hybrid map tiles served via tile and style endpoints, including the HERE Vector Tile API for client-side rendering.
  name: HERE Map Tile API
  slug: map-tile
- description: Renders static map images for a given location, route, or geometry as PNG/JPEG, with markers and overlays.
  name: HERE Map Image API
  slug: map-image
- description: 'Asset tracking platform: ingests positions and telemetry from devices, manages devices and projects, and exposes geofencing, history, and events through REST.'
  name: HERE Tracking API
  slug: tracking
- description: High-precision indoor and outdoor positioning using Wi-Fi, cellular, and Bluetooth signals.
  name: HERE Positioning API
  slug: positioning
- description: On-street and off-street parking availability, pricing, restrictions, and locations.
  name: HERE Parking API
  slug: parking
- description: Catalog, layer, and partition APIs for hosting and accessing location-centric data products on the HERE Platform / Workspace.
  name: HERE Platform Data API
  slug: platform-data
- description: High-definition map product for automated driving with road geometry, lanes, signs, hazards, and dynamic updates, distributed via the HERE Platform.
  name: HERE HD Live Map
  slug: hd-live-map
- description: Browser SDK for embedding interactive maps, routing, search, and traffic visualizations in web applications.
  name: HERE Maps API for JavaScript
  slug: maps-api-javascript
- description: Native iOS SDK with maps, routing, search, navigation, and offline capabilities for mobile applications.
  name: HERE SDK for iOS
  slug: sdk-ios
- description: Native Android SDK with maps, routing, search, navigation, and offline capabilities for mobile applications.
  name: HERE SDK for Android
  slug: sdk-android
- description: Flutter SDK wrapping HERE Mobile SDK capabilities for cross-platform mobile applications.
  name: HERE SDK for Flutter
  slug: sdk-flutter
- description: Web-based mapping studio for designing custom map styles, uploading and visualizing geospatial data, and publishing interactive map experiences on top of the HERE Platform.
  name: HERE Studio
  slug: studio
- baseURL: https://geocode.search.hereapi.com
  baseurl_source: declared
  description: The Batch Jobs API from HERE Technologies — 6 operation(s) for batch jobs.
  name: HERE Technologies Batch Jobs API
  phrasing_intents:
  - id: getJobs
    intent: List batch jobs filtered by status or tag
    question: Which of my batch jobs are still running?
  - id: postJob
    intent: Create a batch job for a service
    question: How do I submit a batch job against a HERE service?
  - id: deleteJobs
    intent: Delete all batch jobs matching a status
    question: Can I bulk delete every finished batch job at once?
  - id: getJob
    intent: Get a batch job's details
    question: What are the details of one of my batch jobs?
  - id: deleteJob
    intent: Delete one batch job
    question: Can I delete a single batch job by its ID?
  - id: getJobErrors
    intent: Download a batch job's errors
    question: Where do I get the errors from a batch job that finished with failures?
  - id: getJobResults
    intent: Download a batch job's results
    question: How can I download the output of a batch job that succeeded?
  - id: startJob
    intent: Start a batch job
    question: What happens if I start a batch job that's already running?
  phrasing_ops: 18
  slug: here-technologies-batch-jobs-api
- baseURL: https://geocode.search.hereapi.com
  baseurl_source: declared
  description: The Geocode API from HERE Technologies — 1 operation(s) for geocode.
  name: HERE Technologies Geocode API
  phrasing_intents:
  - id: getGeocode
    intent: Turn an address into coordinates
    question: How do I get latitude and longitude for a street address?
  phrasing_ops: 1
  slug: here-technologies-geocode-api
- baseURL: https://geocode.search.hereapi.com
  baseurl_source: declared
  description: The Notifications API from HERE Technologies — 1 operation(s) for notifications.
  name: HERE Technologies Notifications API
  phrasing_intents:
  - id: getNotifications
    intent: List notification subscriptions
    question: Which notification subscriptions do I currently have?
  - id: postNotifications
    intent: Subscribe to a notification event
    question: How do I get notified when a particular event happens?
  phrasing_ops: 2
  slug: here-technologies-notifications-api
- description: Optimizes the order of intermediate stops for a single vehicle route to minimize travel time or distance.
  name: HERE Waypoint Sequence API
  slug: waypoint-sequence
- baseURL: https://account.api.here.com
  baseurl_source: declared
  description: Manage access control boundaries for identities
  name: HERE Access Filters API
  phrasing_intents:
  - id: getAccessFilters
    intent: List access filters
    question: What access filters are defined in my realm?
  - id: createAccessFilter
    intent: Create an access filter
    question: How do I create an access filter to restrict what a user or app can reach?
  - id: getAccessFilter
    intent: Get an access filter's details
    question: How do I view the definition of one access filter?
  - id: updateAccessFilter
    intent: Update an access filter
    question: Can I change an existing access filter's definition?
  - id: deleteAccessFilter
    intent: Delete an access filter
    question: How do I delete an access filter I no longer need?
  - id: getAccessFilterMembers
    intent: List members assigned an access filter
    question: Which users and apps have a given access filter assigned?
  phrasing_ops: 6
  slug: here-access-filters-api
- baseURL: https://account.api.here.com
  baseurl_source: declared
  description: An alias is an arbitrary `type` - `externalId` pair, which can be associated with a `trackingId`. The `externalId` can be, for example, an external management system asset ID or a human-readable name.
  name: HERE Aliases API
  phrasing_intents:
  - id: getAliasesV2Health
    intent: Check the Aliases service health
    question: Is the HERE Tracking Aliases service up right now?
  - id: getAliasesV2Version
    intent: Get the Aliases service version
    question: What version of the Aliases service is deployed?
  - id: getAliasesV2
    intent: List all device aliases in a project
    question: Which aliases exist across all devices in my tracking project?
  - id: getAliasesV2ByTrackingId
    intent: List all aliases of one device
    question: What aliases does a specific tracked device have?
  - id: deleteAliasesV2ByTrackingId
    intent: Delete every alias of a device
    question: Can I wipe all aliases from a device in one call?
  - id: getAliasesV2ByTrackingIdByType
    intent: List a device's aliases of one type
    question: Which aliases of a particular type does a device have?
  - id: deleteAliasesV2ByTrackingIdByType
    intent: Delete a device's aliases of one type
    question: Can I remove only the aliases of a single type from a device?
  - id: getAliasesV2TrackingId
    intent: Find the device that owns an alias
    question: Which tracking ID does a given external ID map to?
  phrasing_ops: 11
  slug: here-aliases-api
- baseURL: https://account.api.here.com
  baseurl_source: declared
  description: The API Information API from HERE — 6 operation(s) for api information.
  name: HERE API Information API
  phrasing_intents:
  - id: CostManagementUsageAPIV2GetHealth
    intent: Check health of the cost management usage service
    question: Is the HERE cost management usage service up right now?
  - id: CostManagementUsageAPIV2GetApiVersion
    intent: Get the cost management usage API version
    question: Which version of the cost management usage API is deployed?
  - id: WeatherAPIV1WeatherIsAlive
    intent: Check that the weather service is alive
    question: Is the weather service working properly?
  - id: WeatherAPIV3GetOpenapi
    intent: Download the weather API specification
    question: Where can I get the OpenAPI definition for the weather API v3?
  - id: FuelPricesAPIV2FuelIsAlive
    intent: Check that the fuel prices service is alive
    question: Is the fuel prices service responding?
  - id: FuelPricesAPIV2FuelVersion
    intent: Get the fuel prices service version
    question: What version of the fuel prices service is running?
  phrasing_ops: 6
  slug: here-api-information-api
- baseURL: https://account.api.here.com
  baseurl_source: declared
  description: API Key Management APIs enable identities authorized to manage an application to create and maintain API keys. API Keys can be used to simplify the usage of HLS services by insecure clients.
  name: HERE API Key Management API
  phrasing_intents:
  - id: generateAPIKey
    intent: Generate a new API key for an app
    question: How do I create an API key to authenticate my app?
  - id: getAPIKeys
    intent: List an app's API keys
    question: Which API keys have been generated for my HERE app?
  - id: deleteAPIKey
    intent: Delete an app's API key permanently
    question: How do I permanently delete a leaked API key?
  - id: getAPIKeyByUser
    intent: Get one API key of an app
    question: What are the details of a specific API key on my app?
  - id: updateAPIKey
    intent: Rename an API key or change its expiry
    question: Can I rename an existing API key?
  - id: enableAPIKey
    intent: Enable a disabled API key
    question: How do I turn a disabled API key back on?
  - id: disableAPIKey
    intent: Disable an API key without deleting it
    question: Can I temporarily block an API key without deleting it?
  phrasing_ops: 7
  slug: here-api-key-management-api
- baseURL: https://account.api.here.com
  baseurl_source: declared
  description: For deprecated Applications, App Codes are available to authorized identities to via read-only APIs. App Codes can be used to access limited HLS services that still support them.
  name: HERE App Code Management API
  phrasing_intents:
  - id: getAppCode
    intent: Get an app's legacy App Code
    question: How do I look up the legacy App Code configured for my application?
  phrasing_ops: 1
  slug: here-app-code-management-api
- baseURL: https://account.api.here.com
  baseurl_source: declared
  description: These APIs enable authorized identities (user/another app) to manage access key credentials for the applications.
  name: HERE Application Access Key Management API
  phrasing_intents:
  - id: createAccessKey
    intent: Create a new access key for an app
    question: How do I generate a new access key for my application?
  - id: getAccessKeys
    intent: List an app's access keys
    question: Which access keys exist for my application?
  - id: deleteAccessKey
    intent: Delete an app's access key
    question: Can I permanently delete a leaked access key?
  - id: enableAccessKey
    intent: Enable an app's access key
    question: Can I turn a disabled access key back on?
  - id: disableAccessKey
    intent: Disable an app's access key
    question: Can I temporarily switch off an access key without deleting it?
  phrasing_ops: 5
  slug: here-application-access-key-management-api
- baseURL: https://account.api.here.com
  baseurl_source: declared
  description: Application Management APIs enable HERE users to create applications and authorized identities (user/another app) to manage such applications.
  name: HERE Application Management API
  phrasing_intents:
  - id: listApplications
    intent: List the apps I can manage
    question: Which HERE platform applications do I or my groups have access to?
  - id: createApplication
    intent: Register a new application
    question: How do I register a new app and get a client ID for it?
  - id: getApplication
    intent: View an application
    question: What are the settings of a specific application?
  - id: updateApplication
    intent: Update an application's settings
    question: How do I change the redirect URIs of an existing app?
  - id: deleteApplication
    intent: Delete an application
    question: How do I delete an app I no longer need?
  - id: getApplicationDefaultScope
    intent: View an app's default scope
    question: What default scope does an application's token get?
  - id: setApplicationDefaultScope
    intent: Set an app's default scope
    question: How do I make an app's tokens default to a particular project?
  - id: deleteApplicationDefaultScope
    intent: Remove an app's default scope
    question: How do I clear the default project scope from an application?
  phrasing_ops: 11
  slug: here-application-management-api
- baseURL: https://account.api.here.com
  baseurl_source: declared
  description: An association is a link between a device and a geofence, a sensor rule or a rule. Device events get generated for existing associations only.
  name: HERE Associations API
  phrasing_intents:
  - id: getAssociationsV3Health
    intent: Check the Associations service health
    question: Is the HERE Tracking Associations service up right now?
  - id: getAssociationsV3Version
    intent: Get the Associations service version
    question: What version of the Associations service is deployed?
  - id: getAssociationsV3SensorsBySensorRuleId
    intent: List devices linked to a sensor rule
    question: Which devices are using a particular sensor rule?
  - id: getAssociationsV3GeofencesByGeofenceId
    intent: List devices linked to a geofence
    question: Which devices are associated with a specific geofence?
  - id: getAssociationsV3RulesByRuleId
    intent: List devices linked to a rule
    question: Which devices are associated with a given tracking rule?
  - id: putAssociationsV3ByTrackingIdSensorsBySensorRuleId
    intent: Attach a sensor rule to a device
    question: How do I activate a sensor rule on a tracker?
  - id: deleteAssociationsV3ByTrackingIdSensorsBySensorRuleId
    intent: Detach a sensor rule from a device
    question: Can I stop a sensor rule from applying to one tracker?
  - id: putAssociationsV3ByTrackingIdGeofencesByGeofenceId
    intent: Attach a geofence to a device
    question: How do I get enter and exit events when a tracker crosses a geofence?
  phrasing_ops: 17
  slug: here-associations-api
- baseURL: https://account.api.here.com
  baseurl_source: declared
  description: Endpoints that support asynchronous request flows, allowing for delayed processing and responses to API requests.
  name: HERE Asynchronous API
  phrasing_intents:
  - id: submitProblemAsync
    intent: Submit a vehicle routing problem to solve
    question: How do I optimize delivery routes for my fleet asynchronously?
  - id: getStatus
    intent: Check an asynchronous tour planning request
    question: Is my submitted routing problem finished solving?
  - id: getSolution
    intent: Get the solution to a routing problem
    question: Where do I get the optimized tours after the solver finishes?
  - id: cancelProblem
    intent: Cancel a submitted routing problem
    question: Can I stop the solver working on a problem I submitted?
  - id: postMatrices
    intent: Upload a routing matrix for later problems
    question: Can I supply my own travel time and distance matrix for tour planning?
  phrasing_ops: 5
  slug: here-asynchronous-api
- baseURL: https://account.api.here.com
  baseurl_source: declared
  description: The Authorization Information API from HERE — 4 operation(s) for authorization information.
  name: HERE Authorization Information API
  phrasing_intents:
  - id: HereAccountV1APIsUserAuthorizationDetails
    intent: Get my user's roles and permissions
    question: What roles and permissions does my HERE user account have?
  - id: HereAccountV1APIsGetMyPermissions
    intent: List permissions assigned to me
    question: Which permissions am I, as a user, assigned?
  - id: HereAccountV1APIsIntrospectApplicationAuthorization
    intent: Introspect my application's authorization
    question: What authorization does the app I'm calling with currently have?
  - id: HereAccountV1APIsGetMyAppPermissions
    intent: List permissions assigned directly to my app
    question: Which permissions are directly assigned to my application?
  phrasing_ops: 4
  slug: here-authorization-information-api
- baseURL: https://account.api.here.com
  baseurl_source: declared
  description: The Authorization Server Metadata API from HERE — 2 operation(s) for authorization server metadata.
  name: HERE Authorization Server Metadata API
  phrasing_intents:
  - id: OAuth2.0AccessTokenGetAuthServerMetadata
    intent: Get OAuth authorization server metadata
    question: Where is the HERE OAuth token endpoint and which grant types does it support?
  - id: OAuth2.0AccessTokenGetMcpAuthServerMetadata
    intent: Get OAuth server metadata for MCP clients
    question: What authorization server metadata should an MCP client use to sign in?
  phrasing_ops: 2
  slug: here-authorization-server-metadata-api
- baseURL: https://account.api.here.com
  baseurl_source: declared
  description: The Authorization Share API from HERE — 4 operation(s) for authorization share.
  name: HERE Authorization Share API
  phrasing_intents:
  - id: HereAccountV1APIsShareUserAuthorization
    intent: Share permissions with a user
    question: How do I share access to a resource with another user?
  - id: HereAccountV1APIsShareAppAuthorization
    intent: Share permissions with an application
    question: How do I give an application access to one of my resources?
  - id: HereAccountV1APIsShareGroupAuthorization
    intent: Share permissions with a group
    question: How do I share access to a resource with everyone in a group?
  - id: HereAccountV1APIsRemovePermissionsByResource
    intent: Revoke shared permissions on a resource
    question: How do I take back all the permissions I shared on a resource from a user, app or group?
  phrasing_ops: 4
  slug: here-authorization-share-api
- baseURL: https://account.api.here.com
  baseurl_source: declared
  description: The Autosuggest API from HERE — 1 operation(s) for autosuggest.
  name: HERE Autosuggest API
  phrasing_intents:
  - id: getAutosuggest
    intent: Suggest places as a user types
    question: How do I show address suggestions while someone is typing?
  - id: postAutosuggest
    intent: Suggest places along a route (beta)
    question: Can I get typing suggestions for places along a long route polyline?
  phrasing_ops: 2
  slug: here-autosuggest-api
- baseURL: https://account.api.here.com
  baseurl_source: declared
  description: API for creating and managing notifications. E.g. webhooks.
  name: HERE Batch notifications (BETA) API
  phrasing_intents:
  - id: getNotifications
    intent: List batch job notifications
    question: Which batch job notifications have I configured?
  - id: postNotification
    intent: Create a batch job notification
    question: How do I get a webhook call when a batch job finishes?
  - id: getNotification
    intent: View a batch job notification
    question: What is configured on one of my batch notifications?
  - id: putNotification
    intent: Replace a batch job notification
    question: How do I change the webhook URL on an existing batch notification?
  - id: deleteNotification
    intent: Delete a batch job notification
    question: How do I stop getting notified about batch jobs on an endpoint?
  - id: testNotification
    intent: Send a test batch notification
    question: Can I check that my notification endpoint works without running a batch job?
  phrasing_ops: 6
  slug: here-batch-notifications-beta-api
- baseURL: https://account.api.here.com
  baseurl_source: declared
  description: Upload and retrieve large volumes of data
  name: HERE Blob API
  phrasing_intents:
  - id: BlobAPIV1GetBlob
    intent: Download a blob by data handle
    question: How do I download a partition's data blob using its data handle?
  - id: BlobAPIV1PutBlob
    intent: Publish a volatile data blob
    question: How do I write or overwrite data in a volatile layer?
  - id: BlobAPIV1DeleteBlob
    intent: Delete a blob from an index layer
    question: How do I delete a data blob from an index layer?
  - id: BlobAPIV1CheckBlobExists
    intent: Check that a data handle exists
    question: How can I tell whether a data handle already has a blob before uploading?
  - id: BlobAPIV1StartMultipartUpload
    intent: Start a multipart upload for a data handle
    question: How do I upload a very large blob to a data handle in parts?
  - id: BlobAPIV1GetMultipartUploadStatus
    intent: Check a data handle upload's status
    question: Has the multipart upload for my data handle finished?
  - id: BlobAPIV1CompleteMultipartUpload
    intent: Finish a data handle multipart upload
    question: How do I finalize a data handle upload once all its parts are sent?
  - id: BlobAPIV1CancelMultipartUpload
    intent: Cancel a data handle multipart upload
    question: How do I abort a partly finished upload for a data handle?
  phrasing_ops: 9
  slug: here-blob-api
- baseURL: https://account.api.here.com
  baseurl_source: declared
  description: The Browse API from HERE — 1 operation(s) for browse.
  name: HERE Browse API
  phrasing_intents:
  - id: getBrowse
    intent: Browse nearby places by category or name
    question: What restaurants or shops are closest to a given point?
  - id: postBrowse
    intent: Browse places along a route (beta)
    question: Can I browse places by category along a long route passed in the body?
  phrasing_ops: 2
  slug: here-browse-api
- baseURL: https://account.api.here.com
  baseurl_source: declared
  description: Upload and retrieve large volumes of data by key
  name: HERE By Key API
  phrasing_intents:
  - id: BlobAPIV2GetBlobMetadataByKey
    intent: Check that a key exists and read its metadata
    question: How can I tell whether a key exists in an object store layer without downloading it?
  - id: BlobAPIV2GetBlobByKey
    intent: Download a blob by key
    question: How do I download the object stored under a key in an object store layer?
  - id: BlobAPIV2PutBlobByKey
    intent: Upload or copy a blob under a key
    question: How do I upload a file of up to 192 MB under a key in one request?
  - id: BlobAPIV2DeleteBlobByKey
    intent: Delete a blob by key
    question: How do I delete the object stored under a key?
  - id: BlobAPIV2StartMultipartUploadByKey
    intent: Start a multipart upload for a key
    question: How do I upload a blob that is too big for a single request to a key?
  - id: BlobAPIV2GetMultipartUploadStatusByKey
    intent: Check a key-based multipart upload's status
    question: Did my multipart upload to an object store key finish?
  - id: BlobAPIV2CompleteMultipartUploadByKey
    intent: Finish a key-based multipart upload
    question: What call finalizes a multipart upload once every part of a keyed object is in?
  - id: BlobAPIV2CancelMultipartUploadByKey
    intent: Cancel a key-based multipart upload
    question: How do I abort a multipart upload to an object store key I started?
  phrasing_ops: 10
  slug: here-by-key-api
- baseURL: https://account.api.here.com
  baseurl_source: declared
  description: Endpoints to query charging location data
  name: HERE Charging Location Lookup API
  phrasing_intents:
  - id: HEREEVChargePointsAPIV3GetLocation
    intent: Get one EV charging location
    question: How do I get full details for a single EV charging station I already found?
  - id: HEREEVChargePointsAPIV3GetLocations
    intent: Get several EV charging locations
    question: Can I fetch details for several EV charging stations in one request?
  phrasing_ops: 2
  slug: here-charging-location-lookup-api
- baseURL: https://account.api.here.com
  baseurl_source: declared
  description: Endpoints to query charging location metadata, namely operators and e-Mobility Service Providers.
  name: HERE Charging Location Metadata API
  phrasing_intents:
  - id: HEREEVChargePointsAPIV3GetCountryMeta
    intent: Get EV charging metadata by country
    question: Which e-mobility service providers operate in a country?
  phrasing_ops: 1
  slug: here-charging-location-metadata-api
- baseURL: https://account.api.here.com
  baseurl_source: declared
  description: OAuth Relying Party - Client Registration
  name: HERE Client Registration API
  phrasing_intents:
  - id: OAuth2.0AccessTokenRegisterMcpClient
    intent: Register an MCP OAuth client
    question: How do I dynamically register an MCP client to use OAuth with PKCE?
  phrasing_ops: 1
  slug: here-client-registration-api
- baseURL: https://account.api.here.com
  baseurl_source: declared
  description: Manages catalogs and layers.
  name: HERE Config API
  phrasing_intents:
  - id: ConfigAPIV1GetCatalogs
    intent: List the data catalogs I can access
    question: Which HERE platform catalogs does my account have access to?
  - id: ConfigAPIV1CreateCatalog
    intent: Create a new data catalog
    question: How do I create a new catalog with layers on the HERE platform?
  - id: ConfigAPIV1GetCatalogsPage
    intent: Get the next page of a catalog listing
    question: What do I do when my catalog list comes back split across pages?
  - id: ConfigAPIV1GetCatalog
    intent: Get a catalog's full configuration
    question: How can I see the layer definitions configured in one catalog?
  - id: ConfigAPIV1CatalogExists
    intent: Check whether a catalog exists
    question: Is there a quick way to check if a catalog HRN exists?
  - id: ConfigAPIV1UpdateCatalog
    intent: Replace a catalog's configuration
    question: How do I replace a catalog's whole configuration with a new version?
  - id: ConfigAPIV1PatchCatalog
    intent: Change a few fields on a catalog
    question: Can I change just a catalog's description without resending everything?
  - id: ConfigAPIV1DeleteCatalog
    intent: Delete a catalog and its layers
    question: What happens to the layers when I delete a catalog?
  phrasing_ops: 22
  slug: here-config-api
- baseURL: https://account.api.here.com
  baseurl_source: declared
  description: Endpoints for Cross-Origin Resource Sharing (CORS)
  name: HERE CORS API
  phrasing_intents:
  - id: IngestAPIV1IngestDataCors
    intent: Check CORS for generic data ingestion
    question: Can a browser app send generic data to an ingest layer across origins?
  - id: IngestAPIV1IngestPartitionsCors
    intent: Check CORS for sending partitions to a stream
    question: Is CORS enabled for posting partition lists to a stream layer?
  - id: IngestAPIV1IngestSDIICors
    intent: Check CORS for sending SDII messages
    question: Can a web client send SDII message lists cross-origin?
  - id: optionsProblems
    intent: Check CORS for synchronous tour planning
    question: Can a browser app submit tour planning problems across origins?
  - id: optionsProblemsAsync
    intent: Check CORS for async tour planning submission
    question: Can a web app submit asynchronous tour planning problems cross-origin?
  - id: optionsStatusByStatusId
    intent: Check CORS for a tour planning status check
    question: Can a browser poll tour planning status cross-origin?
  - id: optionsProblemsByProblemIdSolution
    intent: Check CORS for fetching a tour solution
    question: Can a web app download a tour planning solution cross-origin?
  - id: optionsProblemsByProblemIdCancel
    intent: Check CORS for cancelling a tour problem
    question: Can a browser cancel a routing problem cross-origin?
  phrasing_ops: 9
  slug: here-cors-api
- baseURL: https://account.api.here.com
  baseurl_source: declared
  description: Cross Realm Trusts
  name: HERE Cross Realm Trusts API
  phrasing_intents:
  - id: getCrossRealmTrusts
    intent: List cross-realm trusts
    question: Which realms or projects is my realm trusting to share linkable resources?
  - id: createCrossRealmTrust
    intent: Create or update a cross-realm trust
    question: How do I allow another realm to share linkable resources into mine?
  - id: getCrossRealmTrust
    intent: Get one cross-realm trust
    question: Is there a trust set up between a specific source and target realm?
  - id: deleteCrossRealmTrust
    intent: Delete a cross-realm trust
    question: How do I stop another realm from offering resources into my realm?
  phrasing_ops: 4
  slug: here-cross-realm-trusts-api
- baseURL: https://account.api.here.com
  baseurl_source: declared
  description: The Device Token Management API from HERE — 1 operation(s) for device token management.
  name: HERE Device Token Management API
  phrasing_intents:
  - id: OAuth2.0AccessTokenDeleteDeviceToken
    intent: Revoke a device access token
    question: Is there a way to revoke a device token obtained through token exchange?
  phrasing_ops: 1
  slug: here-device-token-management-api
- baseURL: https://account.api.here.com
  baseurl_source: declared
  description: The Discover API from HERE — 1 operation(s) for discover.
  name: HERE Discover API
  phrasing_intents:
  - id: getDiscover
    intent: Search places and addresses by free text
    question: How do I search for a place by a free-form text query?
  - id: postDiscover
    intent: Search places by text along a route (beta)
    question: Can I run a free-text place search along a route sent in the request body?
  phrasing_ops: 2
  slug: here-discover-api
- baseURL: https://account.api.here.com
  baseurl_source: declared
  description: The EgressRules API from HERE — 3 operation(s) for egressrules.
  name: HERE Egress Rules API
  phrasing_intents:
  - id: listEgressRules
    intent: List a realm's egress rules
    question: Which outbound destinations are my pipelines allowed to reach?
  - id: createEgressRules
    intent: Create egress rules
    question: How do I allow my pipelines to call an external host by adding egress rules?
  - id: getEgressRule
    intent: Get an egress rule
    question: How do I view the details of one egress rule?
  - id: deleteEgressRule
    intent: Delete an egress rule
    question: How do I remove an egress rule so pipelines can no longer reach that host?
  - id: getEgressRulesAuditLog
    intent: View the egress rules audit log
    question: Who created or deleted egress rules in my realm, and when?
  phrasing_ops: 5
  slug: here-egressrules-api
- baseURL: https://account.api.here.com
  baseurl_source: declared
  description: Identify information about endpoints subject to rate limit rules on the platform
  name: HERE Endpoints API
  phrasing_intents:
  - id: RateLimitRulesAPIV1GetEndpoints
    intent: List endpoints subject to rate limits
    question: Which HERE platform endpoints are subject to rate limiting rules?
  - id: RateLimitRulesAPIV1GetEndpoint
    intent: Get rate-limit metadata for one endpoint
    question: How do I see the rate limiting metadata for a specific endpoint?
  phrasing_ops: 2
  slug: here-endpoints-api
- baseURL: https://account.api.here.com
  baseurl_source: declared
  description: The Events service manages device and shipment events. An event is created every time an associated rule or geofence is triggered by a device ingestion. A geofence event is created every time a device
  name: HERE Events API
  phrasing_intents:
  - id: getEventsV3Health
    intent: Check the Events service health
    question: Is the HERE Tracking Events service up right now?
  - id: getEventsV3Version
    intent: Get the Events service version
    question: What version of the Events service is deployed?
  - id: getEventsV3
    intent: List event history across a project
    question: What events have all my devices and shipments triggered recently?
  - id: getEventsV3ByTrackingId
    intent: List event history for one device or shipment
    question: What events has a single tracker or shipment triggered?
  - id: getEventsV3Statuses
    intent: Get the latest event state of each device
    question: What is the current event state of each of my devices?
  - id: getEventsV3StatusesDeviceCounts
    intent: Count devices in each event state
    question: How many devices are in each event state per rule?
  phrasing_ops: 6
  slug: here-events-api
- baseURL: https://account.api.here.com
  baseurl_source: declared
  description: Endpoints for managing feature groups
  name: HERE Feature Groups API
  phrasing_intents:
  - id: getFeatureGroups
    intent: List feature groups
    question: What feature groups are available, sorted by name?
  - id: getFeatureGroupWithFeatures
    intent: Get a feature group and its features
    question: Which features are included in a specific feature group?
  phrasing_ops: 2
  slug: here-feature-groups-api
- baseURL: https://account.api.here.com
  baseurl_source: declared
  description: Search fuel stations
  name: HERE Fuel stations API
  phrasing_intents:
  - id: FuelPricesAPIV2FuelStationsSearch
    intent: Find fuel stations with the v2 fuel search
    question: Where are the cheapest diesel stations near me using the older v2 fuel prices search?
  - id: FuelPricesAPIV2FuelStationDetail
    intent: Get a fuel station's details (v2)
    question: How do I get prices and details for one station on the v2 fuel API?
  - id: FuelPricesAPIV3FuelStationsSearch
    intent: Find fuel stations and prices in an area
    question: Where is the cheapest diesel within a few kilometres of me?
  - id: FuelPricesAPIV3FuelStationsCorridorSearch
    intent: Find fuel stations along a route
    question: What fuel stations are along my planned route?
  - id: FuelPricesAPIV3FuelStationDetail
    intent: Get one fuel station's data
    question: What are the current prices at a specific fuel station?
  - id: FuelPricesAPIV3FuelStationBulk
    intent: Get several fuel stations by ID
    question: Can I fetch prices for a list of fuel stations in one call?
  - id: FuelPricesAPIV3FuelStationsCount
    intent: Count fuel stations in an area
    question: How many fuel stations are there in a given area?
  phrasing_ops: 7
  slug: here-fuel-stations-api
- baseURL: https://account.api.here.com
  baseurl_source: declared
  description: Get available fuel types and brands
  name: HERE Fuel types and brands API
  phrasing_intents:
  - id: FuelPricesAPIV2FuelTypes
    intent: List fuel types (v2)
    question: Which fuel type IDs can I use in the v2 fuel station search?
  - id: FuelPricesAPIV2FuelBrands
    intent: List fuel station brands (v2)
    question: Which station brand names does the v2 fuel search accept?
  - id: FuelPricesAPIV3FuelTypes
    intent: List available fuel types
    question: What fuel types, like diesel or LPG, can I search stations by?
  - id: FuelPricesAPIV3FuelBrands
    intent: List fuel station brands by country
    question: Which fuel station brands operate in a given country?
  phrasing_ops: 4
  slug: here-fuel-types-and-brands-api
- baseURL: https://account.api.here.com
  baseurl_source: declared
  description: The Geofences service creates and manages geofences. A geofence is an area boundary that users can define and associate with their devices. The area that the geofence encloses can be defined using geo
  name: HERE Geofences API
  phrasing_intents:
  - id: getGeofencesV2Health
    intent: Check the Geofences service health
    question: Is the HERE Tracking Geofences service up right now?
  - id: getGeofencesV2Version
    intent: Get the Geofences service version
    question: What version of the Geofences service is deployed?
  - id: postGeofencesV2
    intent: Create a geofence
    question: How do I draw a circular or polygon geofence?
  - id: getGeofencesV2
    intent: List all geofences in a project
    question: Which geofences have I defined in my tracking project?
  - id: deleteGeofencesV2
    intent: Delete every geofence in a project
    question: Can I wipe all geofences in a project at once?
  - id: getGeofencesV2ByGeofenceId
    intent: Get one geofence's details
    question: What is the shape and definition of a specific geofence?
  - id: putGeofencesV2ByGeofenceId
    intent: Replace a geofence's definition
    question: Can I change an existing geofence's shape or name?
  - id: deleteGeofencesV2ByGeofenceId
    intent: Delete one geofence
    question: Can I remove a single geofence and keep the others?
  phrasing_ops: 10
  slug: here-geofences-api
- baseURL: https://account.api.here.com
  baseurl_source: declared
  description: The HERE Geofencing API can geofence asset positions against HERE Map objects or custom fence objects
  name: HERE Geofencing V8 API
  phrasing_intents:
  - id: GeofencingAPIGeofence
    intent: Check which geofences contain a point
    question: Is a given location inside any of my geofence polygons?
  - id: GeofencingAPIGeofencePost
    intent: Check geofences for many asset positions
    question: How do I check many vehicle positions against geofences in one request?
  - id: GeofencingAPIV8UploadPost
    intent: Upload geofence geometries from WKT or a shapefile
    question: How do I upload my own geofence polygons?
  - id: GeofencingAPIV8ModifyPost
    intent: Append, update or delete geometries in a layer
    question: Can I add new shapes to an existing geofence layer?
  - id: GeofencingAPIV8DeleteMapsLayers
    intent: Delete geofence layers or a whole map
    question: How do I delete a geofence layer I uploaded?
  - id: GeofencingAPIGeofenceAttributes
    intent: Read the attributes of my geofence geometries
    question: Can I list the custom attributes stored on my geofence shapes?
  phrasing_ops: 6
  slug: here-geofencing-v8-api
- baseURL: https://account.api.here.com
  baseurl_source: declared
  description: Assisted GNSS (A-GNSS) data and predicted GNSS navigation models
  name: HERE GNSS Data API
  phrasing_intents:
  - id: HEREGNSSDataAPIV2GetAssistance
    intent: Get real-time A-GNSS assistance data
    question: How can a device get a faster satellite fix using real-time assistance data?
  - id: HEREGNSSDataAPIV2GetPrediction
    intent: Get predicted GNSS navigation models
    question: Can I download predicted satellite orbits for the coming days instead of live data?
  phrasing_ops: 2
  slug: here-gnss-data-api
- baseURL: https://account.api.here.com
  baseurl_source: declared
  description: Manage resource access by external users
  name: HERE Grants API
  phrasing_intents:
  - id: listGrants
    intent: List who has access to a resource
    question: Which users, apps or groups have permissions on this resource?
  - id: getGrants
    intent: Get an entity's permissions on a resource
    question: What permissions does a specific user have on a resource?
  - id: getGrant
    intent: Check one action grant for an entity
    question: Is a user allowed to take a particular action on a resource?
  - id: addGrant
    intent: Grant an entity permission on a resource
    question: How do I give a user permission to read a catalog?
  - id: removeGrant
    intent: Revoke an entity's permission on a resource
    question: Can I take away one action a user has on a resource?
  phrasing_ops: 5
  slug: here-grants-api
- baseURL: https://account.api.here.com
  baseurl_source: declared
  description: Group and Group Membership Management
  name: HERE Groups API
  phrasing_intents:
  - id: getGroupRoles
    intent: List the roles tied to a group
    question: Which roles are associated with a particular group?
  - id: getGroups
    intent: Find groups in my realm
    question: What groups exist in my HERE organization realm?
  - id: createGroup
    intent: Create a new group
    question: How do I create a group to share access among several users and apps?
  - id: getGroup
    intent: View a single group
    question: What is the name and description of a specific group?
  - id: updateGroup
    intent: Rename or redescribe a group
    question: How do I rename an existing group?
  - id: deleteGroup
    intent: Delete a group
    question: How do I delete a group we no longer use?
  - id: getGroupPolicies
    intent: List policies attached to a group
    question: Which policies are attached to this group?
  - id: getGroupPolicyPermissions
    intent: List permissions in a group's policy
    question: What unscoped permissions does one specific policy give a group?
  phrasing_ops: 15
  slug: here-groups-api
- baseURL: https://account.api.here.com
  baseurl_source: declared
  description: The Icons API from HERE — 1 operation(s) for icons.
  name: HERE Icons API
  phrasing_intents:
  - id: getIcon
    intent: Render a road shield or map icon
    question: How do I get a highway shield icon with a route number for a given country?
  phrasing_ops: 1
  slug: here-icons-api
- baseURL: https://account.api.here.com
  baseurl_source: declared
  description: Endpoints to request images
  name: HERE Images API
  phrasing_intents:
  - id: getImage
    intent: Render a static map image
    question: How do I get a static map picture of an area at a given size and format?
  - id: postImage
    intent: Render a map image with a large overlay via POST
    question: What if my overlay or GeoJSON is too large to fit in the static map URL?
  phrasing_ops: 2
  slug: here-images-api
- baseURL: https://account.api.here.com
  baseurl_source: declared
  description: Manages index layer (create, update and query indices)
  name: HERE Index API
  phrasing_intents:
  - id: IndexAPIV1PerformQuery
    intent: Query partitions in an index layer
    question: How do I find index layer partitions that match a query, such as by time window or tile?
  - id: IndexAPIV1PerformUpdate
    intent: Add and remove index layer partitions
    question: How do I add and remove index entries in an index layer in a single request?
  - id: IndexAPIV1InsertIndexes
    intent: Insert index data into an index layer
    question: How do I publish index records for a data blob to an index layer?
  - id: IndexAPIV1PerformDelete
    intent: Delete index partitions matching a query
    question: How do I delete all index layer partitions that match a condition?
  - id: IndexAPIV1GetDeleteRequestStatus
    intent: Check the status of an index delete request
    question: Has my index layer delete request finished, failed, or is it still processing?
  - id: IndexAPIV1GetParts
    intent: Get part IDs for parallel index queries
    question: How do I split an index layer into parts so I can query it in parallel?
  phrasing_ops: 6
  slug: here-index-api
- baseURL: https://account.api.here.com
  baseurl_source: declared
  description: A generic data endpoint to send any kind of data to stream layers. See [Publish Data to a Stream layer](href="https://www.here.com/docs/bundle/data-api-developer-guide/page/rest/publishing-data-stream
  name: HERE Ingestion API
  phrasing_intents:
  - id: IngestAPIV1IngestData
    intent: Stream raw data into a stream layer
    question: How do I send streaming data into a layer on the HERE platform?
  - id: IngestAPIV1IngestPartitions
    intent: Send a list of partitions to a stream layer
    question: Can I push a batch of partitions into a stream layer in one request?
  - id: IngestAPIV1IngestSDII
    intent: Send SDII vehicle sensor messages to a stream layer
    question: How do I upload SDII sensor messages from vehicles?
  - id: getV2Health
    intent: Check the v2 tracking ingestion service health
    question: Is the v2 device ingestion service up?
  - id: getV2Version
    intent: Get the v2 tracking ingestion service version
    question: What version of the v2 ingestion service is running?
  - id: getV2Timestamp
    intent: Get the server time for device clock sync
    question: What is the tracking server's current time for signing OAuth 1.0 requests?
  - id: postV2Token
    intent: Get a device access token
    question: How does a device authenticate and get an access token for sending telemetry?
  - id: postV2
    intent: Ingest device telemetry via the v2 endpoint
    question: Can devices still send telemetry to the older v2 ingestion endpoint?
  phrasing_ops: 12
  slug: here-ingestion-api
- baseURL: https://account.api.here.com
  baseurl_source: declared
  description: The Isoline API from HERE — 1 operation(s) for isoline.
  name: HERE Isoline API
  phrasing_intents:
  - id: IsolineRoutingAPIV8CalculateIsolines
    intent: Calculate a reachable area from a point
    question: What area can I reach within 15 minutes of driving from a location?
  - id: IsolineRoutingAPIV8CalculateIsolinesPost
    intent: Calculate reachable areas with avoid rules in the body
    question: Can I send large avoid areas in a POST body when calculating isolines?
  phrasing_ops: 2
  slug: here-isoline-api
- baseURL: https://account.api.here.com
  baseurl_source: declared
  description: 'The Labels service creates and manages labels. A label is a key-value pair that can be associated to the following resources: * device * geofence * sensor * rule * location * shipment One can list lab'
  name: HERE Labels API
  phrasing_intents:
  - id: getLabelsV4Health
    intent: Check the Labels service health
    question: Is the HERE Tracking Labels service up right now?
  - id: getLabelsV4Version
    intent: Get the Labels service version
    question: What version of the Labels service is deployed?
  - id: getLabelsV4ByResourceType
    intent: List labels across a resource type
    question: What labels are used on all my devices or geofences?
  - id: getLabelsV4ByResourceTypeKeys
    intent: List label keys for a resource type
    question: Which label keys exist for a resource type?
  - id: getLabelsV4ByResourceTypeKeysByKeyValues
    intent: List values used for a label key
    question: What values has a particular label key been given?
  - id: getLabelsV4ByResourceTypeByResourceId
    intent: List labels on one resource
    question: Which labels are attached to a specific device?
  - id: deleteLabelsV4ByResourceTypeByResourceId
    intent: Remove every label from a resource
    question: Can I strip all labels from a resource in one call?
  - id: deleteLabelsV4ByResourceTypeByResourceIdByKey
    intent: Remove a resource's labels with one key
    question: Can I remove all labels with a given key from a resource?
  phrasing_ops: 11
  slug: here-labels-api
- baseURL: https://account.api.here.com
  baseurl_source: declared
  description: The Largedata service is used for storing large data blobs from devices to HERE Tracking and retrieving the resulting assembled data from HERE Tracking by the users. The data upload from a device foll
  name: HERE Largedata API
  phrasing_intents:
  - id: getLargedataV4Health
    intent: Check the Largedata service health
    question: Is the HERE Tracking Largedata service up right now?
  - id: getLargedataV4Version
    intent: Get the Largedata service version
    question: What version of the Largedata service is deployed?
  - id: postLargedataV4
    intent: Start a multipart large data upload
    question: How do I start a new multipart upload for a large file from a tracking device?
  - id: putLargedataV4ByDataIdPartsByPartNumber
    intent: Upload one part of a large data object
    question: What limits apply to part numbers and part sizes in a large data upload?
  - id: postLargedataV4ByDataId
    intent: Complete or abort a large data upload
    question: How do I finish a multipart upload once every part is sent?
  - id: deleteLargedataV4ByDataId
    intent: Delete a large data object
    question: Can I delete an uploaded large data object?
  - id: getLargedataV4ByDataIdData
    intent: Download bytes of a large data object
    question: How do I download a stored large data object?
  - id: getLargedataV4ByDataIdMetadata
    intent: Get metadata of a large data object
    question: What is the size and status of a large data object?
  phrasing_ops: 10
  slug: here-largedata-api
- baseURL: https://account.api.here.com
  baseurl_source: declared
  description: List the Apps that have the specified Identity Provider attached.
  name: HERE List Apps for an Identity Provider API
  phrasing_intents:
  - id: listAppsForProvider
    intent: List apps using an identity provider
    question: Which applications have attached a particular identity provider in my realm?
  phrasing_ops: 1
  slug: here-list-apps-for-an-identity-provider-api
- baseURL: https://account.api.here.com
  baseurl_source: declared
  description: Supported predefined profiles for calculating matrices with routes of arbitrary length.
  name: HERE List Profiles API
  phrasing_intents:
  - id: getProfiles
    intent: List predefined routing profiles
    question: Which predefined profiles can I use for a matrix calculation?
  phrasing_ops: 1
  slug: here-list-profiles-api
- baseURL: https://account.api.here.com
  baseurl_source: declared
  description: Obtain location information using radio measurements
  name: HERE Location API
  phrasing_intents:
  - id: HERENetworkPositioningAPIV2PostLocate
    intent: Locate a device from cell and Wi-Fi signals
    question: Can I get a device's coordinates from nearby cell towers and Wi-Fi without GPS?
  phrasing_ops: 1
  slug: here-location-api
- baseURL: https://account.api.here.com
  baseurl_source: declared
  description: The Locations service creates and manages locations. Locations are geographical points of interest users may store in HERE Tracking. Locations are used as building blocks for shipments.
  name: HERE Locations API
  phrasing_intents:
  - id: getLocationsV4Health
    intent: Check the Locations service health
    question: Is the HERE Tracking Locations service up right now?
  - id: getLocationsV4Version
    intent: Get the Locations service version
    question: What version of the Locations service is deployed?
  - id: postLocationsV4
    intent: Save a new location
    question: How do I save a warehouse or customer site as a location?
  - id: getLocationsV4
    intent: List saved locations in a project
    question: Which locations have I saved in my tracking project?
  - id: deleteLocationsV4
    intent: Delete every location in a project
    question: Can I remove all saved locations from a project at once?
  - id: getLocationsV4ByLocationId
    intent: Get one saved location
    question: What are the details of one saved location?
  - id: putLocationsV4ByLocationId
    intent: Replace a saved location's details
    question: Can I change the address or coordinates of a saved location?
  - id: deleteLocationsV4ByLocationId
    intent: Delete one saved location
    question: Can I delete a location that a shipment still refers to?
  phrasing_ops: 8
  slug: here-locations-api
- baseURL: https://account.api.here.com
  baseurl_source: declared
  description: The Lookup API from HERE — 1 operation(s) for lookup.
  name: HERE Lookup API
  phrasing_intents:
  - id: getLookup
    intent: Look up a place by its HERE ID
    question: How do I get the full details of a place when I have its HERE ID?
  phrasing_ops: 1
  slug: here-lookup-api
- baseURL: https://account.api.here.com
  baseurl_source: declared
  description: The Manage Changesets API from HERE — 2 operation(s) for manage changesets.
  name: HERE Manage Changesets API
  phrasing_intents:
  - id: InteractiveMapAPIV1GetChangesets
    intent: Browse a map layer's change history
    question: How do I see the history of edits made to an interactive map layer?
  - id: InteractiveMapAPIV1DeleteChangesets
    intent: Delete old changesets from a layer
    question: How do I prune older versions from a map layer's history?
  - id: InteractiveMapAPIV1GetChangeset
    intent: View one changeset by version
    question: What features were modified in a particular write to my layer?
  phrasing_ops: 3
  slug: here-manage-changesets-api
- baseURL: https://account.api.here.com
  baseurl_source: declared
  description: APIs to Manage Device Accounts.
  name: HERE Manage Device Accounts API
  phrasing_intents:
  - id: listDevices
    intent: List device accounts in a realm
    question: Which devices are registered in my HERE realm?
  - id: deleteDevices
    intent: Delete a device by identity provider and external ID
    question: How do I delete a device when I only know its external ID?
  - id: getDevice
    intent: Get a device by HRN
    question: What are the details of a device account given its HRN?
  - id: updateDevice
    intent: Enable or disable a device
    question: Can I disable a device without deleting it?
  - id: deleteDevice
    intent: Delete a device by HRN
    question: How do I delete a device account using its HRN?
  - id: listProjectDevices
    intent: List devices in a project
    question: Which devices belong to a specific project?
  phrasing_ops: 6
  slug: here-manage-device-accounts-api
- baseURL: https://account.api.here.com
  baseurl_source: declared
  description: APIs to manage Identity Providers trusted in a Realm.
  name: HERE Manage Identity Providers for a Realm API
  phrasing_intents:
  - id: addIdentityProvider
    intent: Add a trusted OpenID Connect provider to a realm
    question: Is there a limit on how many new identity providers I can add to a realm?
  - id: listIdentityProviders
    intent: List a realm's trusted identity providers
    question: Which OpenID Connect identity providers does my realm trust?
  - id: getIdentityProvider
    intent: Get a realm's trusted identity provider
    question: What is configured for one trusted identity provider in my realm?
  - id: updateIdentityProvider
    intent: Rename or redescribe a realm identity provider
    question: Can I change the name or description of an identity provider?
  - id: deleteIdentityProvider
    intent: Remove a trusted identity provider from a realm
    question: How do I stop my realm trusting an identity provider?
  - id: listIdentityProviderIssuerAttachments
    intent: List issuer URLs on an identity provider
    question: Which issuer URLs are attached to my identity provider?
  - id: createIdentityProviderIssuerAttachment
    intent: Attach an issuer URL to an identity provider
    question: How many issuer URLs can one identity provider have?
  - id: getIdentityProviderIssuerAttachment
    intent: Get one issuer on an identity provider
    question: Is a particular issuer URL attached to my identity provider?
  phrasing_ops: 10
  slug: here-manage-identity-providers-for-a-realm-api
- baseURL: https://account.api.here.com
  baseurl_source: declared
  description: APIs to manage Identity Providers attached to an App.
  name: HERE Manage Identity Providers for an App API
  phrasing_intents:
  - id: listAppIdentityProviders
    intent: List trusted OpenID Connect providers for an app
    question: Which OpenID Connect identity providers does my app trust?
  - id: createAppIdentityProviderAttachment
    intent: Attach a trusted OpenID Connect provider to an app
    question: How do I let my app accept tokens from an external OpenID Connect provider?
  - id: getAppIdentityProviderAttachment
    intent: Get a trusted OpenID Connect provider for an app
    question: Is a particular OpenID Connect provider trusted by my app, and is it enabled?
  - id: updateAppIdentityProviderAttachment
    intent: Enable or disable an app's OpenID Connect provider
    question: Can I pause an app's trust in an identity provider without detaching it?
  - id: deleteAppIdentityProviderAttachment
    intent: Detach an OpenID Connect provider from an app
    question: How do I stop my app from trusting an OpenID Connect provider?
  phrasing_ops: 5
  slug: here-manage-identity-providers-for-an-app-api
- baseURL: https://account.api.here.com
  baseurl_source: declared
  description: APIs to manage mTLS Identity Provider Certificate Authorities in a Realm.
  name: HERE Manage mTLS Identity Providers API
  phrasing_intents:
  - id: createMtlsIdentityProvider
    intent: Create an mTLS identity provider
    question: How do I let devices authenticate with client certificates from my own CA?
  - id: getMtlsIdentityProviders
    intent: List mTLS identity providers in a realm
    question: Which mTLS identity providers are configured for my HERE realm?
  - id: getMtlsIdentityProvider
    intent: Get an mTLS identity provider
    question: What certificate authority is behind a specific mTLS identity provider?
  - id: updateMtlsIdentityProvider
    intent: Update an mTLS identity provider's CA chain
    question: How do I rotate the certificate chain on an existing mTLS identity provider?
  - id: deleteMtlsIdentityProvider
    intent: Remove an mTLS identity provider
    question: How do I stop trusting a certificate authority for mTLS in my realm?
  - id: listMtlsAuthenticatorsForIdp
    intent: List authenticators for an mTLS identity provider
    question: Which mTLS authenticator checks certificates for a given identity provider?
  - id: getMtlsAuthenticatorForIdp
    intent: Get an mTLS authenticator
    question: Is a particular mTLS authenticator enabled?
  - id: updateMtlsAuthenticatorForIdp
    intent: Enable or disable an mTLS authenticator
    question: How do I temporarily turn off certificate authentication for an mTLS provider?
  phrasing_ops: 9
  slug: here-manage-mtls-identity-providers-api
- baseURL: https://account.api.here.com
  baseurl_source: declared
  description: APIs to manage SAML Identity Providers for a Realm.
  name: HERE Manage SAML identity providers API
  phrasing_intents:
  - id: createIdpConfig
    intent: Add a SAML identity provider to a realm
    question: How do I set up single sign-on by adding a SAML identity provider to my realm?
  - id: getIdpConfigs
    intent: List a realm's SAML identity providers
    question: Which SAML identity providers are configured for my realm?
  - id: enableIdpConfig
    intent: Enable a SAML identity provider for login
    question: How do I switch my realm to log in through a SAML identity provider?
  - id: disableIdpConfig
    intent: Disable a SAML identity provider
    question: How do I turn off SAML sign-on for my realm?
  - id: getIdpConfig
    intent: Get a SAML identity provider's configuration
    question: What entity ID and SSO login URL are set on a SAML identity provider?
  - id: updateIdpConfig
    intent: Update a SAML identity provider
    question: How do I update the metadata of an existing SAML identity provider?
  - id: deleteIdpConfig
    intent: Delete a SAML identity provider
    question: How do I permanently remove a SAML identity provider from my realm?
  phrasing_ops: 7
  slug: here-manage-saml-identity-providers-api
- baseURL: https://account.api.here.com
  baseurl_source: declared
  description: Read and write endpoints for tags.
  name: HERE Manage Tags API
  phrasing_intents:
  - id: InteractiveMapAPIV1ListTags
    intent: List version tags on a map layer
    question: Which version tags exist on my interactive map layer?
  - id: InteractiveMapAPIV1CreateTag
    intent: Tag a version of a map layer
    question: How do I bookmark a specific version of a layer with a tag?
  - id: InteractiveMapAPIV1UpdateTag
    intent: Move a tag to another layer version
    question: How do I point an existing tag at a newer version of the layer?
  - id: InteractiveMapAPIV1GetTag
    intent: View a layer version tag
    question: Which layer version does a particular tag reference?
  - id: InteractiveMapAPIV1DeleteTag
    intent: Delete a layer version tag
    question: How do I remove a tag from a map layer?
  phrasing_ops: 5
  slug: here-manage-tags-api
- baseURL: https://account.api.here.com
  baseurl_source: declared
  description: The Map Attributes V8 API from HERE — 20 operation(s) for map attributes v8.
  name: HERE Map Attributes V8 API
  phrasing_intents:
  - id: MapAttributesAPIV8GetMapAttributes
    intent: Search map content layers for geometries
    question: How can I pull HERE map content attributes for road links inside a bounding box?
  - id: MapAttributesAPIV8GetMapAttributes_1
    intent: Search map layers for geometries via POST
    question: Is there a POST version of the map layer search for when my spatial filter is too long for a URL?
  - id: MapAttributesAPIV8GetMapAttributesForMultiSegment
    intent: Enrich separate road segments with map attributes
    question: How do I look up map attributes for a handful of unconnected road segments?
  - id: MapAttributesAPIV8GetMapAttributesForMultiSegmentPost
    intent: Enrich many road segments with attributes via POST
    question: What's the recommended way to enrich a large batch of segment references with map attributes?
  - id: MapAttributesAPIV8UploadPost
    intent: Upload WKT or Shapefile geometries to a layer
    question: How do I import my own polygons or points in WKT format into a custom map layer?
  - id: MapAttributesAPIV8ModifyPost
    intent: Modify geometries in an uploaded layer
    question: How do I append or replace geometries in a custom layer I already uploaded?
  - id: MapAttributesAPISearchRouteIsolineV8
    intent: Find POIs reachable within a detour of a route
    question: How can I find points of interest within a 10-minute detour along my driving route?
  - id: MapAttributesAPIV8MapsListJSON
    intent: List map regions and releases as JSON
    question: Which map regions and releases are available to my app, in JSON?
  phrasing_ops: 23
  slug: here-map-attributes-v8-api
- baseURL: https://account.api.here.com
  baseurl_source: declared
  description: 'Calculation of routing matrices in one of the following modes: * Flexible * Region * Profile The values of the `regionDefinition` and `profile` parameters determine which mode is used. The following t'
  name: HERE Matrix Calculation API
  phrasing_intents:
  - id: postMatrix
    intent: Calculate a routing matrix
    question: How do I calculate travel times and distances between many origins and destinations?
  - id: getMatrixStatus
    intent: Check an async matrix calculation's status
    question: Is my submitted matrix calculation finished yet?
  - id: getMatrix
    intent: Download a completed matrix result
    question: Where do I download the result of a completed routing matrix?
  phrasing_ops: 3
  slug: here-matrix-calculation-api
- baseURL: https://account.api.here.com
  baseurl_source: declared
  description: Get information about catalogs, layers, and partitions
  name: HERE Metadata API
  phrasing_intents:
  - id: MetadataAPIV1GetLayersVersion
    intent: Get layer versions for a catalog version
    question: Which version of each layer was part of a given catalog version?
  - id: MetadataAPIV1GetChanges
    intent: Get partition changes in a version or time range
    question: Which partitions in a versioned layer changed between two catalog versions?
  - id: MetadataAPIV1GetChangesParts
    intent: Split a layer's change query into parallel parts
    question: How can I fetch layer changes in parallel instead of one big query?
  - id: MetadataAPIV1GetPartitions
    intent: Get metadata for all partitions in a layer
    question: What partitions exist in a layer of my HERE catalog?
  - id: MetadataAPIV1GetPartitionsParts
    intent: Split a layer's partition listing into parallel parts
    question: How do I list every partition of a huge layer using parallel requests?
  - id: MetadataAPIV1ListVersions
    intent: List catalog versions
    question: What versions does my catalog have between two version numbers?
  - id: MetadataAPIV1CompatibleVersions
    intent: Find catalog versions compatible with dependencies
    question: Which versions of this catalog were built against the same dependency versions I use?
  - id: MetadataAPIV1LatestVersion
    intent: Get the latest catalog version
    question: What is the newest version of my HERE catalog?
  phrasing_ops: 29
  slug: here-metadata-api
- baseURL: https://account.api.here.com
  baseurl_source: declared
  description: The Multi Revgeocode API from HERE — 1 operation(s) for multi revgeocode.
  name: HERE Multi Revgeocode API
  phrasing_intents:
  - id: postMultiRevgeocode
    intent: Reverse geocode many coordinates at once
    question: Can I get addresses for a whole list of coordinates in one request?
  phrasing_ops: 1
  slug: here-multi-revgeocode-api
- baseURL: https://account.api.here.com
  baseurl_source: declared
  description: The Next Departures API from HERE — 1 operation(s) for next departures.
  name: HERE Next Departures API
  phrasing_intents:
  - id: PublicTransitAPIV8GetDepartures
    intent: List upcoming public transit departures
    question: When do the next buses and trains leave from a given station?
  phrasing_ops: 1
  slug: here-next-departures-api
- baseURL: https://account.api.here.com
  baseurl_source: declared
  description: The Notification API v2 API from HERE — 2 operation(s) for notification api v2.
  name: HERE Notification API v2 API
  phrasing_intents:
  - id: NotificationAPISubscribe
    intent: Subscribe to catalog change notifications
    question: How do I get notified when a catalog changes?
  - id: NotificationAPIGetSubscriptions
    intent: List notification subscriptions for a layer
    question: Which catalog change subscriptions feed a given notification layer?
  - id: NotificationAPIDeleteSubscriptions
    intent: Delete notification subscriptions for a layer
    question: Can I delete just some catalog change subscriptions by ID?
  phrasing_ops: 3
  slug: here-notification-api-v2-api
- baseURL: https://account.api.here.com
  baseurl_source: declared
  description: The OAuth 2.0 Access Token Endpoint API from HERE — 1 operation(s) for oauth 2.0 access token endpoint.
  name: HERE OAuth 2.0 Access Token Endpoint API
  phrasing_intents:
  - id: OAuth2.0AccessTokenGetOAuth2AccessToken
    intent: Get an OAuth 2.0 access token
    question: How do I get an access token for my app using client credentials?
  phrasing_ops: 1
  slug: here-oauth-2-0-access-token-endpoint-api
- baseURL: https://account.api.here.com
  baseurl_source: declared
  description: The Packages API from HERE — 1 operation(s) for packages.
  name: HERE Packages API
  phrasing_intents:
  - id: createPackage
    intent: Upload a pipeline code package
    question: How do I upload the jar file containing my pipeline code?
  phrasing_ops: 1
  slug: here-packages-api
- baseURL: https://account.api.here.com
  baseurl_source: declared
  description: The Pipelines API from HERE — 3 operation(s) for pipelines.
  name: HERE Pipelines API
  phrasing_intents:
  - id: listPipelines
    intent: List data processing pipelines
    question: What data processing pipelines are defined on the HERE platform for me?
  - id: createPipeline
    intent: Create a pipeline
    question: How do I create a new pipeline before adding any versions to it?
  - id: getPipeline
    intent: View a pipeline
    question: What are the details of one pipeline?
  - id: updatePipeline
    intent: Update a pipeline's metadata
    question: How do I rename a pipeline or change its description?
  - id: deletePipeline
    intent: Delete a pipeline and its versions
    question: How do I delete a pipeline along with all its versions?
  - id: getPipelineHrn
    intent: Get a pipeline's HRN
    question: What is the HERE Resource Name of my pipeline?
  phrasing_ops: 6
  slug: here-pipelines-api
- baseURL: https://account.api.here.com
  baseurl_source: declared
  description: Lookup of platform-wide, general APIs
  name: HERE Platform API
  phrasing_intents:
  - id: APILookupServiceV1PlatformAPIList
    intent: List the HERE platform APIs
    question: Which platform APIs are available and where are their base URLs?
  - id: APILookupServiceV1PlatformAPI
    intent: Look up one platform API version
    question: What is the base URL for a specific platform API version?
  phrasing_ops: 2
  slug: here-platform-api
- baseURL: https://account.api.here.com
  baseurl_source: declared
  description: Platform Pricing Terms APIs
  name: HERE Platform Pricing Terms API
  phrasing_intents:
  - id: acceptRealmPlatformPricingTerms
    intent: Accept the platform pricing terms
    question: How do I accept the HERE platform pricing terms for my organization?
  - id: getRealmPlatformPricingTerms
    intent: Check whether pricing terms were accepted
    question: Has my organization accepted the platform pricing terms yet?
  phrasing_ops: 2
  slug: here-platform-pricing-terms-api
- baseURL: https://account.api.here.com
  baseurl_source: declared
  description: Platform Service Terms APIs
  name: HERE Platform Service Terms API
  phrasing_intents:
  - id: getPlatformServiceTerms
    intent: Read the current Platform Service Terms
    question: What are the current HERE Platform Service Terms?
  - id: acceptRealmPlatformServiceTerms
    intent: Accept the Platform Service Terms for a realm
    question: How do I accept the Platform Service Terms on behalf of my organization?
  - id: getRealmPlatformServiceTerms
    intent: Check a realm's service terms acceptance
    question: Has my organization accepted the Platform Service Terms?
  - id: getRealmPlatformServiceTermsHistory
    intent: Get a realm's service terms acceptance history
    question: When did my organization accept past versions of the service terms?
  phrasing_ops: 4
  slug: here-platform-service-terms-api
- baseURL: https://account.api.here.com
  baseurl_source: declared
  description: The Profile Mode API from HERE — 1 operation(s) for profile mode.
  name: HERE Profile Mode API
  phrasing_intents:
  - id: getProfile
    intent: Get a routing profile definition
    question: What settings does a predefined profile contain?
  phrasing_ops: 1
  slug: here-profile-mode-api
- baseURL: https://account.api.here.com
  baseurl_source: declared
  description: Project Access and Membership Management
  name: HERE Project Access Management API
  phrasing_intents:
  - id: addProjectMember
    intent: Add a user, app or group to a project
    question: How do I add a user, app or group as a member of a project?
  - id: getProjectMember
    intent: Look up one member of a project
    question: Can I check whether a specific user, app or group belongs to a HERE platform project?
  - id: deleteProjectMember
    intent: Remove a member from a project
    question: How do I kick someone else out of a project I manage?
  - id: leaveProject
    intent: Leave a project yourself
    question: How do I leave a project I no longer work on?
  - id: listProjectMembers
    intent: List the members of a project
    question: Who are all the members of this project?
  - id: createProjectPolicy
    intent: Create a custom project policy
    question: How do I define my own policy with a custom set of permissions in a project?
  - id: getProjectPolicyList
    intent: List policies available in a project
    question: Which policies can I attach to members of my project?
  - id: updateProjectPolicy
    intent: Update a custom project policy
    question: How do I change the permissions inside a custom policy I already created?
  phrasing_ops: 26
  slug: here-project-access-management-api
- baseURL: https://account.api.here.com
  baseurl_source: declared
  description: Project Management
  name: HERE Project Management API
  phrasing_intents:
  - id: createProject
    intent: Create a project
    question: How do I set up a new project in my realm?
  - id: getAllProjectList
    intent: List all projects in the organization
    question: What projects exist across my entire HERE organization?
  - id: getProjectList
    intent: List projects I belong to or manage
    question: Which projects am I a member of?
  - id: getProject
    intent: Get a project
    question: What are the details of a specific project?
  - id: checkProjectExistance
    intent: Check whether a project exists
    question: Is there already a project with this HRN in my realm?
  - id: patchProject
    intent: Rename or redescribe a project
    question: Can I rename an existing project?
  - id: deleteProject
    intent: Delete a project
    question: How do I delete a project that is no longer used?
  phrasing_ops: 7
  slug: here-project-management-api
- baseURL: https://account.api.here.com
  baseurl_source: declared
  description: Project Resource Management
  name: HERE Project Resource Management API
  phrasing_intents:
  - id: listProjectResources
    intent: List the resources in a project
    question: Which catalogs and pipelines belong to or are linked into my project?
  - id: addProjectResourceRelations
    intent: Add several resources to a project
    question: How do I add multiple resources to a project at once?
  - id: getProjectResource
    intent: Get one resource in a project
    question: Is a particular resource homed in or linked to my project?
  - id: addProjectResourceRelation
    intent: Add one resource to a project as home or link
    question: How do I link a single catalog into my project?
  - id: deleteProjectResourceReference
    intent: Remove a resource from a project
    question: Can I unlink a resource from my project?
  phrasing_ops: 5
  slug: here-project-resource-management-api
- baseURL: https://account.api.here.com
  baseurl_source: declared
  description: Manage the publishing of data to a catalog. Supports publish to `versioned`, and `volatile` layer types. To publish to 'stream' layer please use Ingest API. See Data API Developer’s Guide in the Docum
  name: HERE Publish API
  phrasing_intents:
  - id: PublishAPIV2InitPublication
    intent: Start a new publication to catalog layers
    question: How do I begin publishing new data to layers in my HERE catalog?
  - id: PublishAPIV2GetPublication
    intent: Get the state of a publication
    question: Did my publication succeed, fail or expire?
  - id: PublishAPIV2SubmitPublication
    intent: Submit a publication for processing
    question: How do I finalize a publication once all partitions are uploaded?
  - id: PublishAPIV2CancelPublication
    intent: Cancel an unsubmitted publication
    question: Can I abandon a publication I haven't submitted yet?
  - id: PublishAPIV2UploadPartitions
    intent: Upload partition metadata into a publication
    question: How do I add partitions to a layer as part of an open publication?
  phrasing_ops: 5
  slug: here-publish-api
- baseURL: https://account.api.here.com
  baseurl_source: declared
  description: Get metadata for catalogs, partitions, and indexes
  name: HERE Query API
  phrasing_intents:
  - id: QueryAPIV1GetChangesById
    intent: See recent changes to specific partitions
    question: Which of my partitions changed between two catalog versions?
  - id: QueryAPIV1GetPartitionsById
    intent: Get metadata for chosen partitions
    question: How do I look up the data handle and version of specific partitions by ID?
  - id: QueryAPIV1QuadTreeIndex
    intent: Query tile index metadata in a versioned layer
    question: How do I find which HERE tile partitions exist under a quadkey in a versioned layer?
  - id: QueryAPIV1QuadTreeIndexVolatile
    intent: Query tile index metadata in a volatile layer
    question: How do I find the partitions under a quadkey in a volatile layer?
  phrasing_ops: 4
  slug: here-query-api
- baseURL: https://account.api.here.com
  baseurl_source: declared
  description: Access and manage rate limit rules for API endpoints on the platform
  name: HERE Rate Limit Rules API
  phrasing_intents:
  - id: RateLimitRulesAPIV1GetRateLimitRulesMe
    intent: List the rate limits enforced on me
    question: What rate limits currently apply to my own identity?
  - id: RateLimitRulesAPIV1GetRateLimitRulesDefault
    intent: List my realm's default rate limits
    question: What are the default rate limits for identities in my realm?
  - id: RateLimitRulesAPIV1GetRateLimitRulesIdentity
    intent: List rate limits for a specific identity
    question: What rate limits are enforced on a particular app or user?
  - id: RateLimitRulesAPIV1GetRateLimitRuleCaller
    intent: Get one rate limit rule applied to me
    question: What exactly does one of my own rate limit rules allow?
  - id: RateLimitRulesAPIV1GetRateLimitRuleDefault
    intent: Get one default rate limit rule for my realm
    question: What does a specific realm default rate limit rule allow?
  - id: RateLimitRulesAPIV1GetRateLimitRuleIdentity
    intent: Get one rate limit rule for an identity
    question: Is a specific rate limit rule enforced on a given app?
  phrasing_ops: 6
  slug: here-rate-limit-rules-api
- baseURL: https://account.api.here.com
  baseurl_source: declared
  description: Read only endpoints for features.
  name: HERE Read Features API
  phrasing_intents:
  - id: InteractiveMapAPIV1GetFeatures
    intent: Get several map features by their IDs
    question: How do I fetch a list of features by ID from an interactive map layer?
  - id: InteractiveMapAPIV1GetFeature
    intent: Get one map feature by ID
    question: Can I retrieve a single feature from a layer by its identifier?
  - id: InteractiveMapAPIV1GetStatistics
    intent: Get statistics about a map layer
    question: What statistics can I see about an interactive map layer?
  - id: InteractiveMapAPIV1GetFeaturesByBBox
    intent: Get map features inside a bounding box
    question: Which features fall inside a rectangular area of my map layer?
  - id: InteractiveMapAPIV1GetFeaturesByTile
    intent: Get map features in a tile
    question: How do I load layer features for one map tile?
  - id: InteractiveMapAPIV1GetFeaturesBySpatial
    intent: Find map features within a radius of a point
    question: Which features are within 500 meters of a coordinate?
  - id: InteractiveMapAPIV1GetFeaturesBySpatialPost
    intent: Find map features intersecting a posted geometry
    question: Can I send my own polygon and get back the features it intersects?
  - id: InteractiveMapAPIV1SearchFeatures
    intent: Search a map layer's features by property
    question: Can I search features by their property values in a layer?
  phrasing_ops: 9
  slug: here-read-features-api
- baseURL: https://account.api.here.com
  baseurl_source: declared
  description: The Real-Time Traffic API from HERE — 3 operation(s) for real-time traffic.
  name: HERE Real-Time Traffic API
  phrasing_intents:
  - id: TrafficAPIV7GetFlow
    intent: Get real-time traffic flow for an area
    question: How do I get live traffic speeds and jam factors for a city bounding box?
  - id: TrafficAPIV7GetFlowWithBodyParams
    intent: Get traffic flow for a complex area via POST
    question: Can I send a long corridor or polygon in a POST body to get traffic flow?
  - id: TrafficAPIV7GetIncidents
    intent: List traffic incidents in an area
    question: What accidents and road closures are happening right now in a given area?
  - id: TrafficAPIV7GetIncidentsWithBodyParams
    intent: List traffic incidents for a large area via POST
    question: Is there a POST form of the incidents search for large polygons or corridors?
  - id: TrafficAPIV7GetIncidentsById
    intent: Get a traffic incident by its ID
    question: How do I look up the current details of one traffic incident by its ID?
  - id: TrafficAPIV7GetIncidentsByIdWithBodyParams
    intent: Get a traffic incident by ID via POST
    question: Can I fetch a single incident by ID with the options in a POST body?
  phrasing_ops: 6
  slug: here-real-time-traffic-api
- baseURL: https://account.api.here.com
  baseurl_source: declared
  description: Realms and Realm Membership Management
  name: HERE Realms API
  phrasing_intents:
  - id: resendRealmMemberInvite
    intent: Resend an existing realm invitation unchanged
    question: Someone lost their invitation email to our realm, can it be sent again as-is?
  - id: sendUpdatedRealmMemberInvite
    intent: Update and resend a pending realm invitation
    question: Can I fix the email address on an invitation I already sent to my HERE organization and send it again?
  - id: cancelRealmMemberInvite
    intent: Cancel a pending realm invitation
    question: How do I revoke an invitation I sent to the wrong person for my realm?
  - id: searchRealmMemberInvites
    intent: Search invitations in a realm
    question: Which invitations to my HERE realm are still outstanding?
  - id: createRealmMemberInvite
    intent: Invite a new user to a realm
    question: How do I invite a colleague to join my HERE platform organization?
  - id: getRealmMemberInviteTargets
    intent: List invite targets available for a realm
    question: Which applications can an invitation email send new members to in my realm?
  - id: getRealmLimits
    intent: Get the limits configured for a realm
    question: What limits apply to my HERE organization's realm?
  - id: getRealmMembers
    intent: List members of a realm
    question: Who are all the users and apps in my HERE realm?
  phrasing_ops: 37
  slug: here-realms-api
- baseURL: https://account.api.here.com
  baseurl_source: declared
  description: The Registry service is used for provisioning and claiming devices.
  name: HERE Registry API
  phrasing_intents:
  - id: getRegistryV2Health
    intent: Check the Registry service health
    question: Is the HERE Tracking Registry service up right now?
  - id: getRegistryV2Version
    intent: Get the Registry service version
    question: What version of the Registry service is deployed?
  - id: getRegistryV2ByAppIdDevices
    intent: List devices provisioned under an app
    question: Which device licenses have I provisioned for a project app?
  - id: postRegistryV2ByAppIdDevices
    intent: Provision licenses for many devices in a batch job
    question: How do I create device licenses for a whole fleet at once?
  - id: postRegistryV2ByAppIdOneDevice
    intent: Provision a license for one physical device
    question: How do I get a device ID and secret for a single tracker?
  - id: getRegistryV2ByAppIdLicenseCount
    intent: Count device licenses provisioned under an app
    question: How many device licenses has my project provisioned?
  - id: getRegistryV2ByJobIdStatus
    intent: Check a bulk device license job's progress
    question: Is my bulk device provisioning job finished yet?
  - id: getRegistryV2ByJobIdResults
    intent: Get the licenses a bulk job created
    question: Where do I get the device credentials a batch license job produced?
  phrasing_ops: 17
  slug: here-registry-api
- baseURL: https://account.api.here.com
  baseurl_source: declared
  description: Resource Management and Information
  name: HERE Resource Info and Management API
  phrasing_intents:
  - id: getResources
    intent: List resources of a type I can see
    question: Which catalogs or pipelines am I allowed to see on the platform?
  - id: listRealmResources
    intent: List every resource in my realm
    question: How do I see all resources across my whole realm?
  - id: getRealmExternalResources
    intent: List external resources shared into my realm
    question: Which resources were made available to my realm through plans or policies?
  - id: getResourceTypeActionList
    intent: List the actions for a resource type
    question: What actions can be granted on a catalog resource type?
  - id: getResource
    intent: Get a single resource
    question: How can I look up one resource by its HRN?
  - id: getResourceSettings
    intent: Get a resource's policy settings
    question: Is my resource available to be added to resource policies?
  - id: updateResourceSettings
    intent: Set a resource's policy availability
    question: Can I stop a resource from being added to resource policies?
  - id: getResourceProjects
    intent: List projects a resource belongs to or is linked in
    question: Which projects is this resource home to or linked into?
  phrasing_ops: 13
  slug: here-resource-info-and-management-api
- baseURL: https://account.api.here.com
  baseurl_source: declared
  description: Resource Policy Management
  name: HERE Resource Policies API
  phrasing_intents:
  - id: createResourcePolicy
    intent: Create a resource policy
    question: How do I package resources so they can be made linkable to other realms?
  - id: getResourcePolicies
    intent: List resource policies
    question: Which resource policies exist in my HERE realm?
  - id: getResourcePolicy
    intent: Get a resource policy
    question: What are the details of one specific resource policy?
  - id: deleteResourcePolicy
    intent: Delete a resource policy
    question: How do I remove a resource policy I no longer need?
  - id: updateResourcePolicy
    intent: Rename or redescribe a resource policy
    question: Can I rename an existing resource policy?
  - id: addResourcesToResourcePolicy
    intent: Batch-add resources to a resource policy
    question: How do I add many resources to a resource policy in one request?
  - id: getAllResourcesInResourcePolicy
    intent: List resources in a resource policy
    question: Which resources are included in a resource policy?
  - id: getResourcePolicyResourcesStatus
    intent: Check the status of a batch resource addition
    question: Did my batch of resources finish being added to the resource policy?
  phrasing_ops: 11
  slug: here-resource-policies-api
- baseURL: https://account.api.here.com
  baseurl_source: declared
  description: Lookup of APIs related to resources identified by an HRN
  name: HERE Resources API
  phrasing_intents:
  - id: APILookupServiceV1ResourceAPIList
    intent: List the APIs available for a resource
    question: Which API base URLs should I call for a given catalog HRN?
  - id: APILookupServiceV1ResourceAPI
    intent: Get one API's endpoint for a resource
    question: What is the base URL for one specific API version on a catalog?
  phrasing_ops: 2
  slug: here-resources-api
- baseURL: https://account.api.here.com
  baseurl_source: declared
  description: The Revgeocode API from HERE — 1 operation(s) for revgeocode.
  name: HERE Revgeocode API
  phrasing_intents:
  - id: getRevgeocode
    intent: Find the address at a coordinate
    question: What is the nearest address to a latitude and longitude?
  phrasing_ops: 1
  slug: here-revgeocode-api
- baseURL: https://account.api.here.com
  baseurl_source: declared
  description: Role and Role Membership Management
  name: HERE Roles API
  phrasing_intents:
  - id: getRoles
    intent: List roles in the realm
    question: What roles exist in my HERE platform realm?
  - id: getMyRoles
    intent: List the roles assigned to me
    question: Which roles have been assigned to my own user or app?
  - id: getRole
    intent: Get a role by its HRN
    question: How do I look up the details of a single role from its HRN?
  - id: getRolePermissions
    intent: List the permissions granted by a role
    question: What permissions does a role grant?
  - id: getRolePermission
    intent: Get one permission of a role
    question: How do I check a single permission on a role?
  - id: getRoleAccessFilter
    intent: Get the access filter attached to a role
    question: Is there an access filter attached to this role?
  - id: getRoleEntities
    intent: List users and apps assigned a role
    question: Who has been assigned a given role?
  - id: getRoleEntity
    intent: Check whether an entity holds a role
    question: How do I confirm a specific user or app has been assigned a role?
  phrasing_ops: 10
  slug: here-roles-api
- baseURL: https://account.api.here.com
  baseurl_source: declared
  description: Match GPS traces onto the most probably driven path
  name: HERE Route Matching V8 API
  phrasing_intents:
  - id: HERERouteMatchingV8APIMatchRouteV8compatibilityToV2GET
    intent: Match a short GPS trace to roads via query string
    question: How can I snap a handful of GPS waypoints to the road network with a simple GET?
  - id: HERERouteMatchingV8APIMatchRouteV8compatibilityToV2POST
    intent: Match an uploaded GPS trace to the driven path
    question: How do I match a large GPS trace file to the path a truck actually drove?
  - id: HERERouteMatchingV8APIOverlayUploadV8
    intent: Upload a custom overlay map for route matching
    question: Can I block or add road links privately so route matching uses my changes?
  phrasing_ops: 3
  slug: here-route-matching-v8-api
- baseURL: https://account.api.here.com
  baseurl_source: declared
  description: The Routing API from HERE — 3 operation(s) for routing.
  name: HERE Routing API
  phrasing_intents:
  - id: PublicTransitAPIV8GetRoutes
    intent: Plan a public transit trip
    question: How do I find a bus or train connection between two coordinates for a given departure time?
  - id: RoutingAPIV8CalculateRoutesPost
    intent: Calculate a car, truck or walking route
    question: How do I calculate a driving route while avoiding a long list of areas I can't fit in the URL?
  - id: RoutingAPIV8GetRoutesByHandle
    intent: Recall a calculated route from its handle
    question: How do I get a previously calculated route back from its route handle?
  - id: RoutingAPIV8GetRoutesByHandlePost
    intent: Recall a route handle with a POST body
    question: How do I decode a route handle when my avoid-areas list is too long for the query string?
  - id: RoutingAPIV8ImportRoute
    intent: Build a route from a GPS trace
    question: How do I turn a recorded GPS track into a route with travel time and distance?
  phrasing_ops: 5
  slug: here-routing-api
- baseURL: https://account.api.here.com
  baseurl_source: declared
  description: 'The Rules service creates and manages rules. Rules generate events and notifications when get triggered by a device behaviour. The following rule types are supported: * dwelling * detention * utilizat'
  name: HERE Rules API
  phrasing_intents:
  - id: getRulesV4Health
    intent: Check the Rules service health
    question: Is the HERE Tracking Rules service up right now?
  - id: getRulesV4Version
    intent: Get the Rules service version
    question: What version of the Rules service is deployed?
  - id: postRulesV4
    intent: Create a tracking rule
    question: How do I set up a detention rule with a time threshold?
  - id: getRulesV4
    intent: List all tracking rules
    question: Which detention or dwelling rules are defined in my project?
  - id: deleteRulesV4
    intent: Delete every rule in a project
    question: Can I remove all tracking rules at once?
  - id: getRulesV4ByRuleId
    intent: Get one rule's definition
    question: What is the threshold of a specific rule?
  - id: putRulesV4ByRuleId
    intent: Update a rule's name or threshold
    question: Can I change the threshold of an existing rule?
  - id: deleteRulesV4ByRuleId
    intent: Delete one rule
    question: Can I delete a single rule and keep the others?
  phrasing_ops: 8
  slug: here-rules-api
- baseURL: https://account.api.here.com
  baseurl_source: declared
  description: The RuntimeEnvironments API from HERE — 1 operation(s) for runtimeenvironments.
  name: HERE Runtime Environments API
  phrasing_intents:
  - id: listRuntimeEnvironments
    intent: List available pipeline runtime environments
    question: Which runtime environments can my pipelines run on?
  phrasing_ops: 1
  slug: here-runtimeenvironments-api
- baseURL: https://account.api.here.com
  baseurl_source: declared
  description: List of supported SAML Identity Provider templates.
  name: HERE SAML Identity Provider Templates API
  phrasing_intents:
  - id: listOfIdpTemplates
    intent: List supported SAML identity provider templates
    question: Which SAML identity provider templates are supported for single sign-on setup?
  phrasing_ops: 1
  slug: here-saml-identity-provider-templates-api
- baseURL: https://account.api.here.com
  baseurl_source: declared
  description: Secret Management APIs enable authorized identities to securely upload and manage third-party credentials for use in the platform.
  name: HERE Secret Management API
  phrasing_intents:
  - id: createSecret
    intent: Store a new secret for platform runtimes
    question: How do I store third-party credentials such as AWS keys for my pipelines to use?
  - id: listSecrets
    intent: List my stored secrets
    question: What secrets have I stored for use in platform pipelines?
  - id: getSecret
    intent: View a secret
    question: What are the settings of one stored secret?
  - id: updateSecret
    intent: Update a secret's contents or settings
    question: How do I rotate the contents of a secret I already stored?
  - id: deleteSecret
    intent: Delete a secret permanently
    question: How do I permanently delete a secret?
  - id: enableSecret
    intent: Enable a secret
    question: How do I turn a disabled secret back on?
  - id: disableSecret
    intent: Disable a secret
    question: How do I temporarily stop a secret being used without deleting it?
  phrasing_ops: 7
  slug: here-secret-management-api
- baseURL: https://account.api.here.com
  baseurl_source: declared
  description: The Sensors service creates and manages sensor rules. The sensor rules generate events and notifications when get triggered by a reported device sensor reading. The following sensor rule types are sup
  name: HERE Sensors API
  phrasing_intents:
  - id: getSensorsV3Health
    intent: Check the Sensors service health
    question: Is the HERE Tracking Sensors service up right now?
  - id: getSensorsV3Version
    intent: Get the Sensors service version
    question: What version of the Sensors service is deployed?
  - id: postSensorsV3
    intent: Create a sensor rule
    question: How do I alert when a tracker's temperature leaves a range?
  - id: getSensorsV3
    intent: List all sensor rules
    question: Which temperature, humidity or battery sensor rules exist in my project?
  - id: deleteSensorsV3
    intent: Delete every sensor rule in a project
    question: Can I wipe all sensor rules from a project at once?
  - id: getSensorsV3BySensorRuleId
    intent: Get one sensor rule
    question: What range or threshold does a specific sensor rule use?
  - id: putSensorsV3BySensorRuleId
    intent: Update a sensor rule's range or threshold
    question: Can I change the temperature range of an existing sensor rule?
  - id: deleteSensorsV3BySensorRuleId
    intent: Delete one sensor rule
    question: Can I delete a single sensor rule?
  phrasing_ops: 8
  slug: here-sensors-api
- baseURL: https://account.api.here.com
  baseurl_source: declared
  description: Service discovery and management
  name: HERE Services API
  phrasing_intents:
  - id: getServiceInfoById
    intent: Look up a platform service by ID
    question: What actions and resource types does one specific platform service, looked up by its ID, define?
  - id: getServiceInfo
    intent: Look up a platform service by alias
    question: How do I find a service when I only know its short alias like data or pipeline?
  - id: getResourceTypes
    intent: List resource types across services
    question: What resource types exist across all platform services?
  phrasing_ops: 3
  slug: here-services-api
- baseURL: https://account.api.here.com
  baseurl_source: declared
  description: The Shadows service provides an effective way to manage configurations for devices that are only intermittently online. The device shadow contains `reported` and `desired` state objects of a device, r
  name: HERE Shadows API
  phrasing_intents:
  - id: getShadowsV2Health
    intent: Check the Shadows service health
    question: Is the HERE Tracking Shadows service up right now?
  - id: getShadowsV2Version
    intent: Get the Shadows service version
    question: What version of the Shadows service is deployed?
  - id: putShadowsV2ByTrackingId
    intent: Set a device's desired shadow
    question: How do I push new configuration to a device through its shadow?
  - id: getShadowsV2ByTrackingId
    intent: Get a device's full shadow
    question: What is the last reported and desired state of a device?
  - id: deleteShadowsV2ByTrackingId
    intent: Clear a device's shadow
    question: Can I clear only the desired part of a device shadow?
  - id: postShadowsV2Batch
    intent: Get shadows for many devices at once
    question: Can I fetch shadows for up to 100 devices in one request?
  - id: getShadowsV2ByTrackingIdByState
    intent: Get a device's reported or desired state
    question: Can I fetch just the reported state of a device?
  - id: getShadowsV2ByTrackingIdByStateBySelector
    intent: Read one property from a device shadow
    question: Can I read a single property like battery level from a device shadow?
  phrasing_ops: 9
  slug: here-shadows-api
- baseURL: https://account.api.here.com
  baseurl_source: declared
  description: The Shipments service manages shipments. A shipment describes a structure of a multimodal logistics journey. Shipments are useful when the lifetime of an asset one is tracking spans across multiple de
  name: HERE Shipments API
  phrasing_intents:
  - id: getShipmentsV4Health
    intent: Check the Shipments service health
    question: Is the HERE Tracking Shipments service up right now?
  - id: getShipmentsV4Version
    intent: Get the Shipments service version
    question: What version of the Shipments service is deployed?
  - id: postShipmentsV4
    intent: Create a shipment with segments
    question: How do I set up a multi-leg shipment with a tracker on each leg?
  - id: getShipmentsV4
    intent: List shipments in a project
    question: Which shipments are currently in progress?
  - id: deleteShipmentsV4
    intent: Delete every shipment in a project
    question: Can I delete all shipments in a project at once?
  - id: getShipmentsV4ByShipmentId
    intent: Get one shipment's details
    question: What is the status of a particular shipment?
  - id: patchShipmentsV4ByShipmentId
    intent: Update a shipment's details
    question: Can I change a shipment's name or status after creating it?
  - id: deleteShipmentsV4ByShipmentId
    intent: Delete one shipment and its data
    question: Does deleting a shipment also remove its events and associations?
  phrasing_ops: 11
  slug: here-shipments-api
- baseURL: https://account.api.here.com
  baseurl_source: declared
  description: The Signals API from HERE — 1 operation(s) for signals.
  name: HERE Signals API
  phrasing_intents:
  - id: postSignals
    intent: Send search interaction feedback
    question: Can I report which search result a user picked to improve future results?
  phrasing_ops: 1
  slug: here-signals-api
- baseURL: https://account.api.here.com
  baseurl_source: declared
  description: The Snapshots API from HERE — 2 operation(s) for snapshots.
  name: HERE Snapshots API
  phrasing_intents:
  - id: listSnapshots
    intent: List recent snapshots of a pipeline
    question: What snapshots has my data pipeline taken recently?
  - id: getSnapshot
    intent: Get a pipeline snapshot
    question: What are the details of one specific pipeline snapshot?
  phrasing_ops: 2
  slug: here-snapshots-api
- baseURL: https://account.api.here.com
  baseurl_source: declared
  description: The Station Search API from HERE — 1 operation(s) for station search.
  name: HERE Station Search API
  phrasing_intents:
  - id: PublicTransitAPIV8GetStations
    intent: Find public transit stations
    question: Which public transit stations are wheelchair accessible?
  phrasing_ops: 1
  slug: here-station-search-api
- baseURL: https://account.api.here.com
  baseurl_source: declared
  description: Consume data from stream layers
  name: HERE Stream API
  phrasing_intents:
  - id: StreamAPIV2Subscribe
    intent: Subscribe to a stream layer
    question: How do I start consuming messages from a stream layer?
  - id: StreamAPIV2DeleteSubscription
    intent: Delete a stream layer subscription
    question: How do I unsubscribe from a stream layer when I'm done?
  - id: StreamAPIV2ConsumeData
    intent: Read messages from a stream layer
    question: How do I read the latest messages from a stream layer I subscribed to?
  - id: StreamAPIV2Endpoint
    intent: Get Kafka consumer endpoint details for a layer
    question: Can I consume a stream layer directly from Kafka brokers?
  - id: StreamAPIV2EndpointByConsumer
    intent: Get Kafka producer or consumer settings for a layer
    question: Where do I get the Kafka settings to produce data into a stream layer?
  - id: StreamAPIV2CommitOffsets
    intent: Commit the offsets of messages I've read
    question: Why should I commit offsets after reading stream data?
  - id: StreamAPIV2SeekToOffset
    intent: Move the read pointer to a chosen offset
    question: Can I replay a stream layer from an earlier offset?
  phrasing_ops: 7
  slug: here-stream-api
- baseURL: https://account.api.here.com
  baseurl_source: declared
  description: Manages subscriptions.
  name: HERE Subscription API
  phrasing_intents:
  - id: ConfigAPIV1ListSubscriptions
    intent: List an organization's subscriptions
    question: Which catalog subscriptions does my account have access to?
  - id: ConfigAPIV1CreateSubscription
    intent: Create a catalog-to-catalog subscription
    question: How do I subscribe a target catalog layer to a source layer?
  - id: ConfigAPIV1GetSubscription
    intent: View a subscription's configuration
    question: What source and target does a particular subscription connect?
  - id: ConfigAPIV1CheckSubscriptionExists
    intent: Check that a subscription exists
    question: Is there a quick existence check for a subscription HRN?
  - id: ConfigAPIV1DeleteSubscription
    intent: Delete a subscription
    question: How do I stop and remove a catalog subscription?
  - id: ConfigAPIV1GetSubscriptionStatus
    intent: Track a subscription create or delete
    question: How do I know when my subscription creation or deletion has finished?
  - id: ConfigAPIV1BatchCreateSubscriptions
    intent: Create many subscriptions at once
    question: Can I create several catalog subscriptions in a single request?
  - id: ConfigAPIV1BatchGetSubscriptionStatus
    intent: Track a batch subscription creation
    question: Has my batch of subscriptions finished being created?
  phrasing_ops: 8
  slug: here-subscription-api
- baseURL: https://account.api.here.com
  baseurl_source: declared
  description: Endpoints for managing subscriptions
  name: HERE Subscriptions API
  phrasing_intents:
  - id: updateSubscriptionById
    intent: Update a subscription by its ID
    question: How do I link a subscription to its Zuora billing subscription using the subscription ID?
  - id: getSubscriptionByKey
    intent: Look up a subscription by its key
    question: How do I get subscription details if I only have the subscription key?
  - id: updateSubscriptionByKey
    intent: Update a subscription by its key
    question: Can I update a subscription's Zuora link using the subscription key instead of the ID?
  - id: getActiveSubscriptions
    intent: List an organization's active subscriptions
    question: Which subscriptions are currently active for my organization?
  - id: createSubscriptionKeysPublic
    intent: Create new subscription keys
    question: How do I generate a batch of new subscription keys with certain feature groups?
  - id: addFeatureGroupToSubscription
    intent: Add a feature group to a subscription by ID
    question: How do I add a feature group to a subscription using its subscription ID and feature group ID?
  - id: removeFeatureGroupFromSubscription
    intent: Remove a feature group from a subscription by ID
    question: How do I take a feature group off a subscription when I have the subscription ID?
  - id: addFeatureGroupToSubscription_1
    intent: Add a feature group to a subscription by key
    question: Can I add a feature group by its ID to a subscription I only know by key?
  phrasing_ops: 15
  slug: here-subscriptions-api
- baseURL: https://account.api.here.com
  baseurl_source: declared
  description: Manage Account Executive support access
  name: HERE Support Access API
  phrasing_intents:
  - id: getSupportAccess
    intent: Get the realm's support access entry
    question: Is Account Executive support access enabled for my realm?
  - id: registerSupportAccessUser
    intent: Grant support access to users
    question: How do I let a HERE account executive log in to my realm for support?
  - id: deleteSupportAccess
    intent: Revoke support access to the realm
    question: How do I remove support access and log out any support users?
  phrasing_ops: 3
  slug: here-support-access-api
- baseURL: https://account.api.here.com
  baseurl_source: declared
  description: Endpoints that support synchronous request flows, allowing for immediate processing and responses to API requests.
  name: HERE Synchronous API
  phrasing_intents:
  - id: postProblems
    intent: Solve a vehicle routing problem synchronously
    question: Can I get optimized delivery tours back in the same request?
  phrasing_ops: 1
  slug: here-synchronous-api
- baseURL: https://account.api.here.com
  baseurl_source: declared
  description: Endpoints to retrieve service information, including service version and health status.
  name: HERE System API
  phrasing_intents:
  - id: getVersion
    intent: Get the tour planning service version
    question: Which version of the tour planning service is currently deployed?
  - id: getHealth
    intent: Check the tour planning service health
    question: Is the tour planning service up and healthy right now?
  phrasing_ops: 2
  slug: here-system-api
- baseURL: https://account.api.here.com
  baseurl_source: declared
  description: Endpoints to request tiles
  name: HERE Tiles API
  phrasing_intents:
  - id: getTile
    intent: Get a rendered raster map tile
    question: How do I fetch a rendered map tile image for a given zoom level, column and row?
  - id: TrafficVectorTileAPIV2GetTile
    intent: Get a traffic vector tile
    question: How do I get traffic flow and incidents as protobuf vector tiles?
  phrasing_ops: 2
  slug: here-tiles-api
- baseURL: https://account.api.here.com
  baseurl_source: declared
  description: The Traces service allows users querying device traces based on time ranges. A device trace is a device-ingested telemetry along with the ingestion timestamp and the device current position. > **NOTE*
  name: HERE Traces API
  phrasing_intents:
  - id: getTracesV2Health
    intent: Check the Traces service health
    question: Is the HERE Tracking Traces service up right now?
  - id: getTracesV2Version
    intent: Get the Traces service version
    question: What version of the Traces service is deployed?
  - id: deleteTracesV2ByTrackingId
    intent: Delete a device's traces and events
    question: Can I erase a device's location history?
  - id: getTracesV2ByTrackingId
    intent: Get a device's location history
    question: Where has a device been over the past day?
  phrasing_ops: 4
  slug: here-traces-api
- baseURL: https://account.api.here.com
  baseurl_source: declared
  description: Trusted Domain Management APIs enable authorized identities to manage URIs to register with an appliication
  name: HERE Trusted Domain Management API
  phrasing_intents:
  - id: enableTrustedDomains
    intent: Turn on Trusted Domains for an app
    question: How do I turn on Trusted Domains for an application?
  - id: disableTrustedDomains
    intent: Turn off Trusted Domains for an app
    question: How do I switch off Trusted Domains for an app?
  - id: getTrustedDomainsEnabled
    intent: Check if Trusted Domains is enabled for an app
    question: Is Trusted Domains switched on for my app?
  - id: addTrustedDomain
    intent: Add a single trusted domain to an app
    question: How do I add one website domain to my app's trusted list?
  - id: getTrustedDomain
    intent: Get one trusted domain of an app
    question: Is a specific domain on my app's trusted list?
  - id: deleteTrustedDomain
    intent: Remove a single trusted domain from an app
    question: How do I remove one domain from my app's trusted domains?
  - id: addManyTrustedDomains
    intent: Add several trusted domains to an app at once
    question: How do I add a batch of trusted domains to an application in one call?
  - id: listTrustedDomains
    intent: List an app's trusted domains
    question: Which domains are currently trusted for my app?
  phrasing_ops: 9
  slug: here-trusted-domain-management-api
- baseURL: https://account.api.here.com
  baseurl_source: declared
  description: Usage
  name: HERE Usage API
  phrasing_intents:
  - id: CostManagementUsageAPIV2GetUsageByRealm
    intent: Get billable usage for an organization
    question: How much billable HERE usage did my organization rack up last month?
  - id: CostManagementUsageAPIV2GetUsageCsvByRealm
    intent: Export organization usage as CSV
    question: Can I download my organization's usage as a CSV file for a spreadsheet?
  - id: CostManagementUsageAPIV2CreateUsageReport
    intent: Request a usage report for partner subaccounts
    question: How do I generate a usage report covering my partner subaccounts?
  - id: CostManagementUsageAPIV2GetAllUsageReportRequestsStatus
    intent: List the status of all usage report requests
    question: Which usage reports have I requested and are any ready to download?
  - id: CostManagementUsageAPIV2GetUsageReportRequestStatus
    intent: Check the status of one usage report request
    question: Is the usage report I requested finished yet?
  - id: CostManagementUsageAPIV2FetchCreatedReport
    intent: Download a completed usage report
    question: How do I download a finished usage report?
  phrasing_ops: 6
  slug: here-usage-api
- baseURL: https://account.api.here.com
  baseurl_source: declared
  description: User Account Management APIs
  name: HERE User Account Management API
  phrasing_intents:
  - id: activateUserAccount
    intent: Activate a user account
    question: How do I reactivate a user account that was deactivated?
  - id: deactivateUserAccount
    intent: Deactivate a user account
    question: How do I suspend a user's account and invalidate their access tokens?
  - id: deleteUserAccount
    intent: Delete a user account
    question: How do I permanently delete a user account?
  - id: getUserManagedApps
    intent: List apps a user can act on
    question: Which apps does a user have a given permission over, directly or through a group?
  phrasing_ops: 4
  slug: here-user-account-management-api
- baseURL: https://account.api.here.com
  baseurl_source: declared
  description: Endpoints for tracking users
  name: HERE User Tracking API
  phrasing_intents:
  - id: getOrganizationTrackingReport
    intent: Get the user tracking report for my organization
    question: Can I get a tracking report covering every user in my organization?
  phrasing_ops: 1
  slug: here-user-tracking-api
- baseURL: https://account.api.here.com
  baseurl_source: declared
  description: The Users service provides HERE Tracking user authentication and authorization.
  name: HERE Users API
  phrasing_intents:
  - id: getUsersV2Health
    intent: Check the Users service health
    question: Is the HERE Tracking Users service up right now?
  - id: getUsersV2Version
    intent: Get the Users service version
    question: What version of the Users service is deployed?
  - id: getUsersV2Devices
    intent: List devices claimed by a project
    question: Which devices has my project claimed?
  - id: postUsersV2Login
    intent: Log a user in and get an access token
    question: How do I get a user access token with an email and password?
  - id: postUsersV2Refresh
    intent: Refresh an expired user access token
    question: My user access token expired; can I renew it without logging in again?
  - id: postUsersV2TokenExchange
    intent: Exchange a user token for a project-scoped one
    question: How do I get a user token scoped to one project?
  phrasing_ops: 6
  slug: here-users-api
- baseURL: https://account.api.here.com
  baseurl_source: declared
  description: Upload and retrieve large volumes of data
  name: HERE Volatile Blob API
  phrasing_intents:
  - id: VolatileBlobAPIV1GetVolatileBlob
    intent: Download a volatile data blob
    question: How do I read the data stored under a handle in a volatile layer?
  - id: VolatileBlobAPIV1CheckHandleExists
    intent: Check whether a volatile blob exists
    question: How can I check if data exists for a handle without downloading it?
  - id: VolatileBlobAPIV1PatchVolatileBlob
    intent: Change a volatile blob's time-to-live
    question: Can I extend how long a volatile blob is kept without re-uploading it?
  - id: VolatileBlobAPIV1PutVolatileBlob
    intent: Publish a volatile data blob
    question: How do I write or overwrite data in a volatile layer?
  - id: VolatileBlobAPIV1DeleteVolatileBlob
    intent: Delete a volatile data blob
    question: How do I remove data stored under a handle in a volatile layer?
  phrasing_ops: 5
  slug: here-volatile-blob-api
- baseURL: https://account.api.here.com
  baseurl_source: declared
  description: Compute best Sequence for Waypoints (Travelling Salesman Problem)
  name: HERE Waypoints Sequence API
  phrasing_intents:
  - id: WaypointsSequenceAPIFindSequenceGET
    intent: Find the best order to visit waypoints
    question: What is the fastest order to visit a list of delivery stops?
  - id: WaypointsSequenceAPIFindSequencePOST
    intent: Sequence many waypoints with a form-encoded POST
    question: How do I sequence a large number of waypoints that won't fit in a URL?
  phrasing_ops: 2
  slug: here-waypoints-sequence-api
- baseURL: https://account.api.here.com
  baseurl_source: declared
  description: Weather alerts.
  name: HERE Weather Alerts API
  phrasing_intents:
  - id: WeatherAPIV1WeatherAlert
    intent: Get weather alerts around a car's location
    question: Are there any severe weather alerts near a vehicle's current position?
  - id: WeatherAPIV1WeatherRouteAlert
    intent: Get weather alerts along a route (v1)
    question: What weather alerts are along my route using the v1 weather API?
  - id: WeatherAPIV3WeatherAlert
    intent: Get weather alerts for a route or location
    question: Which severe weather warnings affect my trip or a single point?
  phrasing_ops: 3
  slug: here-weather-alerts-api
- baseURL: https://account.api.here.com
  baseurl_source: declared
  description: Dopler radar images.
  name: HERE Weather Radar API
  phrasing_intents:
  - id: WeatherAPIV1WeatherRadarImage
    intent: Get a radar map tile from weather API v1
    question: How do I fetch a Doppler radar tile from the older weather 2.0 tile path?
  - id: WeatherAPIV3WeatherRadarImage
    intent: Get a radar or precipitation tile from weather API v3
    question: How do I get a global precipitation or radar tile from the v3 weather API?
  phrasing_ops: 2
  slug: here-weather-radar-api
- baseURL: https://account.api.here.com
  baseurl_source: declared
  description: Destination weather report.
  name: HERE Weather Report API
  phrasing_intents:
  - id: WeatherAPIV1WeatherReport
    intent: Get a weather report (legacy v1 endpoint)
    question: How do I get current weather for a city by name from the older 1.0 weather report endpoint?
  - id: WeatherAPIV3WeatherReport
    intent: Get weather observations, forecasts and alerts
    question: What is the weather forecast for an address I can type as free text?
  phrasing_ops: 2
  slug: here-weather-report-api
- baseURL: https://account.api.here.com
  baseurl_source: declared
  description: Write endpoints for features.
  name: HERE Write Features API
  phrasing_intents:
  - id: InteractiveMapAPIV1PutFeatures
    intent: Create or replace many map features
    question: How do I upload a GeoJSON FeatureCollection into an interactive map layer, replacing any existing features with the same IDs?
  - id: InteractiveMapAPIV1PostFeatures
    intent: Create or patch many features
    question: How do I merge changes into several features at once instead of replacing them?
  - id: InteractiveMapAPIV1DeleteFeatures
    intent: Delete several features or wipe a layer
    question: How do I delete a list of features by ID from a map layer?
  - id: InteractiveMapAPIV1PutFeature
    intent: Create or replace a single feature
    question: How do I write one feature with a known ID into a layer, replacing it entirely if it exists?
  - id: InteractiveMapAPIV1PatchFeature
    intent: Partially update one feature
    question: How do I change just some properties of an existing feature without resending all of it?
  - id: InteractiveMapAPIV1DeleteFeature
    intent: Delete one feature
    question: How do I remove a single feature from a map layer?
  phrasing_ops: 6
  slug: here-write-features-api
- baseURL: https://geocode.search.hereapi.com
  baseurl_source: declared
  description: The Pipeline Templates API from HERE — 3 operation(s) for pipeline templates.
  name: HERE Pipeline Templates API
  phrasing_intents:
  - id: listPipelineTemplates
    intent: List pipeline templates
    question: What pipeline templates have been defined?
  - id: createPipelineTemplate
    intent: Create a pipeline template
    question: How do I create a reusable pipeline template from my uploaded package?
  - id: getPipelineTemplate
    intent: Get a pipeline template
    question: How do I see the package and entry point behind a pipeline template?
  - id: deletePipelineTemplate
    intent: Delete a pipeline template
    question: How do I delete a pipeline template I don't use anymore?
  - id: getPipelineTemplateHrn
    intent: Get a pipeline template's HRN
    question: Where do I find the HRN of a pipeline template?
  phrasing_ops: 5
  slug: here-pipeline-templates-api
- baseURL: https://geocode.search.hereapi.com
  baseurl_source: declared
  description: The Pipeline Versions API from HERE — 13 operation(s) for pipeline versions.
  name: HERE Pipeline Versions API
  phrasing_intents:
  - id: listPipelineVersions
    intent: List the versions of a pipeline
    question: How do I see every version defined for one of my HERE data pipelines?
  - id: createPipelineVersion
    intent: Create a new version of a pipeline
    question: How do I define a new pipeline version with its template and input and output catalogs?
  - id: getPipelineVersion
    intent: Get details of a pipeline version
    question: What state is a particular pipeline version in right now?
  - id: deletePipelineVersion
    intent: Delete a pipeline version
    question: How do I delete a pipeline version I no longer need?
  - id: listPipelineVersionJobs
    intent: List jobs run by a pipeline version
    question: Which jobs has a pipeline version run, and is one running right now?
  - id: getLoggingConfiguration
    intent: Get a pipeline version's logging configuration
    question: What log level is currently configured for my pipeline version?
  - id: updateLoggingConfiguration
    intent: Change a pipeline version's logging configuration
    question: Can I change the log level of a pipeline version while a job is running?
  - id: listOperations
    intent: List operations on a pipeline version
    question: What activate, pause or cancel operations are pending on a pipeline version?
  phrasing_ops: 17
  slug: here-pipeline-versions-api
- baseURL: https://geocode.search.hereapi.com
  baseurl_source: declared
  description: The Resource Profiles API from HERE — 1 operation(s) for resource profiles.
  name: HERE Resource Profiles API
  phrasing_intents:
  - id: listResourceProfiles
    intent: List resource profiles enabled for my organization
    question: Which pipeline resource profiles can my organization use?
  phrasing_ops: 1
  slug: here-resource-profiles-api
artifact_total: 155
asyncapis:
- description: ''
  name: Here Event Surface
  slug: here-event-surface
common:
- group: other
  href: https://artifacts.apis.io/here/capabilities/here-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/here-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/here/overlays/here-account-v1-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/here-account-v1-overlay.yaml
- group: other
  href: https://artifacts.apis.io/here/overlays/here-api-lookup-v1-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/here-api-lookup-v1-overlay.yaml
- group: other
  href: https://artifacts.apis.io/here/overlays/here-authentication-v1-1-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/here-authentication-v1-1-overlay.yaml
- group: other
  href: https://artifacts.apis.io/here/overlays/here-authorization-v1-1-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/here-authorization-v1-1-overlay.yaml
- group: other
  href: https://artifacts.apis.io/here/overlays/here-cost-management-usage-v2-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/here-cost-management-usage-v2-overlay.yaml
- group: other
  href: https://artifacts.apis.io/here/overlays/here-data-blob-v1-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/here-data-blob-v1-overlay.yaml
- group: other
  href: https://artifacts.apis.io/here/overlays/here-data-blob-v2-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/here-data-blob-v2-overlay.yaml
- group: other
  href: https://artifacts.apis.io/here/overlays/here-data-config-v1-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/here-data-config-v1-overlay.yaml
- group: other
  href: https://artifacts.apis.io/here/overlays/here-data-index-v1-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/here-data-index-v1-overlay.yaml
- group: other
  href: https://artifacts.apis.io/here/overlays/here-data-ingest-v1-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/here-data-ingest-v1-overlay.yaml
- group: other
  href: https://artifacts.apis.io/here/overlays/here-data-metadata-v1-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/here-data-metadata-v1-overlay.yaml
- group: other
  href: https://artifacts.apis.io/here/overlays/here-data-notification-v1-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/here-data-notification-v1-overlay.yaml
- group: other
  href: https://artifacts.apis.io/here/overlays/here-data-publish-v2-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/here-data-publish-v2-overlay.yaml
- group: other
  href: https://artifacts.apis.io/here/overlays/here-data-query-v1-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/here-data-query-v1-overlay.yaml
- group: other
  href: https://artifacts.apis.io/here/overlays/here-data-stream-v2-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/here-data-stream-v2-overlay.yaml
- group: other
  href: https://artifacts.apis.io/here/overlays/here-data-volatile-blob-v1-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/here-data-volatile-blob-v1-overlay.yaml
- group: other
  href: https://artifacts.apis.io/here/overlays/here-destination-weather-v1-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/here-destination-weather-v1-overlay.yaml
- group: other
  href: https://artifacts.apis.io/here/overlays/here-destination-weather-v3-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/here-destination-weather-v3-overlay.yaml
- group: other
  href: https://artifacts.apis.io/here/overlays/here-ev-charge-points-v3-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/here-ev-charge-points-v3-overlay.yaml
- group: other
  href: https://artifacts.apis.io/here/overlays/here-fuel-prices-v2-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/here-fuel-prices-v2-overlay.yaml
- group: other
  href: https://artifacts.apis.io/here/overlays/here-fuel-prices-v3-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/here-fuel-prices-v3-overlay.yaml
- group: other
  href: https://artifacts.apis.io/here/overlays/here-geocoding-and-search-v7-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/here-geocoding-and-search-v7-overlay.yaml
- group: other
  href: https://artifacts.apis.io/here/overlays/here-geocoding-batch-v7-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/here-geocoding-batch-v7-overlay.yaml
- group: other
  href: https://artifacts.apis.io/here/overlays/here-geofencing-v1-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/here-geofencing-v1-overlay.yaml
- group: other
  href: https://artifacts.apis.io/here/overlays/here-gnss-data-v2-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/here-gnss-data-v2-overlay.yaml
- group: other
  href: https://artifacts.apis.io/here/overlays/here-indoor-routing-v1-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/here-indoor-routing-v1-overlay.yaml
- group: other
  href: https://artifacts.apis.io/here/overlays/here-interactive-map-v1-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/here-interactive-map-v1-overlay.yaml
- group: other
  href: https://artifacts.apis.io/here/overlays/here-intermodal-routing-v8-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/here-intermodal-routing-v8-overlay.yaml
- group: other
  href: https://artifacts.apis.io/here/overlays/here-isoline-routing-v8-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/here-isoline-routing-v8-overlay.yaml
- group: other
  href: https://artifacts.apis.io/here/overlays/here-map-attributes-v1-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/here-map-attributes-v1-overlay.yaml
- group: other
  href: https://artifacts.apis.io/here/overlays/here-map-image-v3-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/here-map-image-v3-overlay.yaml
- group: other
  href: https://artifacts.apis.io/here/overlays/here-matrix-routing-v8-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/here-matrix-routing-v8-overlay.yaml
- group: other
  href: https://artifacts.apis.io/here/overlays/here-network-positioning-v1-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/here-network-positioning-v1-overlay.yaml
- group: other
  href: https://artifacts.apis.io/here/overlays/here-network-positioning-v2-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/here-network-positioning-v2-overlay.yaml
- group: other
  href: https://artifacts.apis.io/here/overlays/here-oauth2-token-v1-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/here-oauth2-token-v1-overlay.yaml
- group: other
  href: https://artifacts.apis.io/here/overlays/here-pipeline-management-v2-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/here-pipeline-management-v2-overlay.yaml
- group: other
  href: https://artifacts.apis.io/here/overlays/here-public-transit-v8-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/here-public-transit-v8-overlay.yaml
- group: other
  href: https://artifacts.apis.io/here/overlays/here-raster-tile-v3-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/here-raster-tile-v3-overlay.yaml
- group: other
  href: https://artifacts.apis.io/here/overlays/here-rate-limit-rules-v1-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/here-rate-limit-rules-v1-overlay.yaml
- group: other
  href: https://artifacts.apis.io/here/overlays/here-route-matching-v8-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/here-route-matching-v8-overlay.yaml
- group: other
  href: https://artifacts.apis.io/here/overlays/here-routing-v8-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/here-routing-v8-overlay.yaml
- group: other
  href: https://artifacts.apis.io/here/overlays/here-tour-planning-v3-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/here-tour-planning-v3-overlay.yaml
- group: other
  href: https://artifacts.apis.io/here/overlays/here-tracking-v2-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/here-tracking-v2-overlay.yaml
- group: other
  href: https://artifacts.apis.io/here/overlays/here-traffic-raster-tile-v3-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/here-traffic-raster-tile-v3-overlay.yaml
- group: other
  href: https://artifacts.apis.io/here/overlays/here-traffic-v7-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/here-traffic-v7-overlay.yaml
- group: other
  href: https://artifacts.apis.io/here/overlays/here-traffic-vector-tile-v2-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/here-traffic-vector-tile-v2-overlay.yaml
- group: other
  href: https://artifacts.apis.io/here/overlays/here-waypoints-sequence-v1-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/here-waypoints-sequence-v1-overlay.yaml
- group: other
  href: https://artifacts.apis.io/here/overlays/here-wego-user-service-v1-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/here-wego-user-service-v1-overlay.yaml
- group: commercial
  href: https://artifacts.apis.io/here/finops/here-finops.yml
  title: ''
  type: FinOps
  url: finops/here-finops.yml
- group: build
  title: ''
  type: GitHub
  url: https://github.com/heremaps
- group: company
  title: ''
  type: Website
  url: https://www.here.com/
- group: agent
  href: https://artifacts.apis.io/here/agentic-access/here-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/here-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/here/security/here-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/here-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/here/authentication/here-authentication.yml
  title: ''
  type: Authentication
  url: authentication/here-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/heremaps
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/here
- group: start
  title: ''
  type: SignUp
  url: https://platform.here.com/sign-up
- group: start
  title: ''
  type: Login
  url: https://platform.here.com/portal/
- group: company
  title: ''
  type: Blog
  url: https://www.here.com/company/blog?type=developer
- group: other
  title: ''
  type: Knowledge
  url: https://knowledge.here.com/csm_kb
- group: operate
  title: ''
  type: StatusPage
  url: https://status.here.com/status
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://legal.here.com/privacy/policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://legal.here.com/terms/serviceterms
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.here.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.here.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.here.com/geocoding-and-search/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://www.here.com/get-started
- group: operate
  title: ''
  type: Support
  url: https://knowledge.here.com/csm_kb
- group: commercial
  title: ''
  type: Pricing
  url: https://www.here.com/get-started/pricing
- group: build
  href: https://artifacts.apis.io/here/packages/here-packages.yml
  title: ''
  type: SDKs
  url: packages/here-packages.yml
- group: build
  href: https://artifacts.apis.io/here/packages/here-packages.yml
  title: ''
  type: Packages
  url: packages/here-packages.yml
- group: build
  href: https://artifacts.apis.io/here/cli/here-cli.yml
  title: ''
  type: CLI
  url: cli/here-cli.yml
- group: design
  href: https://artifacts.apis.io/here/components/here-components.yml
  title: ''
  type: Components
  url: components/here-components.yml
- group: start
  title: ''
  type: Console
  url: https://platform.here.com/portal/
- group: agent
  href: https://artifacts.apis.io/here/llms/here-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/here-llms.txt
- group: agent
  href: https://artifacts.apis.io/here/well-known/here-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/here-well-known.yml
- group: other
  title: ''
  type: APICatalog
  url: https://docs.here.com/.well-known/api-catalog
- group: agent
  href: https://artifacts.apis.io/here/mcp/here-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/here-mcp.yml
- group: build
  href: https://artifacts.apis.io/here/mcp/here-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/here-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/here/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/here/conventions/here-conventions.yml
  title: ''
  type: Conventions
  url: conventions/here-conventions.yml
- group: design
  href: https://artifacts.apis.io/here/errors/here-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/here-problem-types.yml
- group: design
  href: https://artifacts.apis.io/here/data-model/here-data-model.yml
  title: ''
  type: DataModel
  url: data-model/here-data-model.yml
- group: design
  href: https://artifacts.apis.io/here/lifecycle/here-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/here-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.here.com/policies/docs/product-lifecycle-policy
- group: operate
  href: https://artifacts.apis.io/here/changelog/here-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/here-changelog.yml
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://www.here.com/learn/blog?type=developer&category=release-notes
- group: design
  href: https://artifacts.apis.io/here/conformance/here-conformance.yml
  title: ''
  type: Conformance
  url: conformance/here-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://legal.here.com/en-gb/certifications-and-attestations
- group: auth
  href: https://artifacts.apis.io/here/security/here-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/here-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/here/security/here-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/here-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://legal.here.com/en-gb/security
- group: design
  href: https://artifacts.apis.io/here/asyncapi/here-event-surface.yml
  title: ''
  type: Webhooks
  url: asyncapi/here-event-surface.yml
- group: other
  href: https://artifacts.apis.io/here/grpc/_index.yml
  title: ''
  type: Protobuf
  url: grpc/_index.yml
- group: operate
  href: https://artifacts.apis.io/here/rate-limits/here-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/here-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/here/plans/here-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/here-plans-pricing.yml
- group: operate
  title: ''
  type: SLA
  url: https://docs.here.com/policies/docs/here-service-level-agreement
created: 2023/11/13
description: As global mobility becomes increasingly connected, electrified and automated, HERE Technologies is leading the way to a safer, greener future. Our location platform is integrated into more than 160 million vehicles across the planet, using fresh and accurate data that we have been building for over 35 years - and continue to refresh daily. Our experience in mapmaking has made HERE one of the leading innovators in location technology and spatial intelligence.
finops:
- has_sources: true
  method: derived
  name: Here Finops
  primary_unit: ''
  service_category: ''
  slug: here-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/here.png
layout: provider
mcp_servers:
- description: Remote MCP server at docs.here.com over streamable HTTP; 7 tools listed.
  name: HERE Technologies Documentation | HERE Docs
  slug: here-technologies-documentation-here-docs
modified: '2026-09-13'
name: HERE
nav: Providers
network: true
overview: 'HERE publishes 139 API contracts indexed on the [APIs.io](https://apis.io/) network, including Technologies Batch Jobs API, Technologies Geocode API, Technologies Notifications API, and 136 more. Tagged areas include Location, Mapping, Maps, Spatial, and Geocoding.


  The HERE catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  HERE''s developer surface includes GitHub presence, authentication, signup flow, engineering blog, documentation, API reference, getting-started guide, and 91 more developer resources.'
plans:
- name: Here Plans Pricing
  plan_count: 1
  slug: here-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 6
  name: Here Rate Limits
  slug: here-rate-limits
rules:
- authorship: generated
  effective_rule_count: 102
  extends:
  - spectral:oas
  name: HERE API Rules
  rule_count: 61
  severity_counts:
    error: 37
    hint: 0
    info: 6
    warn: 18
  slug: here-rules
score:
  band: exemplar
  composite: 77.6
  coverage:
    artifact_dirs: 35
    catalog_earned: 64.5
    catalog_earned_first_party: 20.0
    catalog_gap: 50.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 2.5
  facets:
    access_clarity: 81.6
    contract_governance: 31.8
    contract_quality: 55.4
    developer_ergonomics: 70.8
    discoverability: 90.0
    operational_transparency: 92.1
  previous_composite: 75.1
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 47.1
      derived: 13
      marker_coverage: 10.7
      total: 121
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 35.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 61.1
screenshot: https://apis.io/screenshots/here/here-2026-06-20T182640.png
security:
- kind: authentication
  name: Here Authentication
  slug: here-authentication
  summary_line: apiKey/http · 5 schemes
- kind: domain-security
  name: Here Domain Security
  slug: here-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Here Vulnerability Disclosure
  slug: here-vulnerability-disclosure
  summary_line: no policy recorded
- kind: trust-center
  name: Here Trust Center
  slug: here-trust-center
  summary_line: ISO/IEC 42001:2023, ISO/IEC 27001:2022, ISO/IEC 27017:2015, ISO/IEC 27018:2019, ISO/IEC 27701:2019, SOC 2, TISAX, HITRUST r2, CSA STAR
skill_count: 5
skills:
- name: here-authenticate
  slug: here-authenticate
- name: here-calculate-a-route
  slug: here-calculate-a-route
- name: here-geocode-and-search
  slug: here-geocode-and-search
- name: here-read-live-traffic
  slug: here-read-live-traffic
- name: here-run-a-batch-geocoding-job
  slug: here-run-a-batch-geocoding-job
slug: here
tags:
- Location
- Mapping
- Maps
- Spatial
- Geocoding
- Routing
- Traffic
- Navigation
- Geospatial
- Transit
- Weather
- Positioning
- Fleet Management
- Automotive
- Location Intelligence
- Mobility
website: https://www.here.com/
---
