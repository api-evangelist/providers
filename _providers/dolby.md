---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
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
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: documented
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 41.7
  scored_at: '2026-11-06'
api_count: 8
apis:
- description: 'Cross-platform video playback (formerly THEOplayer) for web, Android/Fire TV, iOS/tvOS, Roku, React Native and Flutter, with DRM, ad and analytics connectors. A client-side SDK surface: there is no pu'
  name: Dolby OptiView Player
  slug: optiview-player
- baseURL: https://api.theo.live/v2
  baseurl_source: declared
  description: The ABR Ladders API from Dolby — 1 operation(s) for abr ladders.
  name: Dolby ABR Ladders API
  phrasing_intents:
  - id: get-abr-ladders
    intent: List the organization's ABR ladders
    question: Which adaptive bitrate ladders are available to my organization?
  phrasing_ops: 1
  slug: dolby-abr-ladders-api
- baseURL: https://api.theo.live/v2
  baseurl_source: declared
  description: The Account API from Dolby — 9 operation(s) for account.
  name: Dolby Account API
  phrasing_intents:
  - id: Account_UpdateExpirationRules
    intent: Change media asset expiration rules
    question: Can I make recordings expire after a different number of days account-wide?
  - id: Account_GetExpirationRules
    intent: View media asset expiration rules
    question: How long are my recordings and clips kept before they expire?
  - id: Account_ListStorageProfiles
    intent: List cloud storage profiles
    question: Which cloud storage profiles have I set up for media delivery?
  - id: Account_CreateStorageProfile
    intent: Create a cloud storage profile
    question: How do I send finished recordings to my own S3 or Google Cloud Storage bucket?
  - id: Account_DeleteStorageProfile
    intent: Delete a storage profile
    question: How do I remove a storage profile I no longer use?
  - id: Account_GetStorageProfile
    intent: Get one storage profile
    question: What settings does a particular storage profile have?
  - id: Account_UpdateStorageProfile
    intent: Update a storage profile
    question: Can I rename a storage profile or change its bucket options?
  - id: Account_ValidateThirdPartyStorage
    intent: Validate third-party storage permissions
    question: Can I check that my bucket gives Dolby.io permission to upload media?
  phrasing_ops: 17
  slug: dolby-account-api
- baseURL: https://api.theo.live/v2
  baseurl_source: declared
  description: The Ad Engine API from Dolby — 7 operation(s) for ad engine.
  name: Dolby Ad Engine API
  phrasing_intents:
  - id: create-ad-profile
    intent: Create an ad encoding profile
    question: How do I define a new encoding profile that ads get conformed to?
  - id: get-ad-profile
    intent: Get an ad encoding profile
    question: What encoding settings does one of my ad profiles use?
  - id: update-ad-profile
    intent: Update an ad encoding profile
    question: How do I change the encode settings on an existing ad profile?
  - id: delete-ad-profile
    intent: Delete an ad encoding profile
    question: How do I remove an ad profile I no longer use?
  - id: list-ad-profiles
    intent: List all ad encoding profiles
    question: Which ad encoding profiles do I currently have?
  - id: conform-ad
    intent: Conform a single ad to an encoding profile
    question: How do I make one ad creative match my encoding profile?
  - id: conform-ad-pod
    intent: Conform an ad pod to an encoding profile
    question: Can I conform several ads in an ad pod in one request?
  - id: cloud-preview-codemill
    intent: Generate an Accurate Player preview template
    question: How can I preview a cloud media asset in the Codemill Accurate Player?
  phrasing_ops: 10
  slug: dolby-ad-engine-api
- baseURL: https://api.theo.live/v2
  baseurl_source: declared
  description: Viewer connection analytics records
  name: Dolby Analytics API
  phrasing_intents:
  - id: Records_GetViewerRecords
    intent: Look up viewer connection records
    question: Who connected to my streams, and how long did each viewer session last?
  - id: Analytics_AccountTotal
    intent: Get total account usage for a date range
    question: How much streaming usage did my whole account rack up last month?
  - id: Analytics_AccountSeries
    intent: Chart account usage over time
    question: How did my account's usage trend day by day across a date range?
  - id: Analytics_AccountGeoTotal
    intent: Get account bandwidth and duration by country
    question: Which countries used the most bandwidth and watch duration on my account?
  - id: Analytics_AccountGeoSeries
    intent: Chart account usage per country over time
    question: How did publishes and views per country change over time on my account?
  - id: Analytics_StreamsTotal
    intent: Get total usage for specific streams
    question: How much usage did a particular stream name generate over a date range?
  - id: Analytics_StreamsSeries
    intent: Chart usage over time for specific streams
    question: How did usage of one stream trend over time at an hourly or daily resolution?
  - id: Analytics_StreamsGeoTotal
    intent: Get stream bandwidth and duration by country
    question: Which countries consumed the most bandwidth and duration on a specific stream?
  phrasing_ops: 23
  slug: dolby-analytics-api
- baseURL: https://api.theo.live/v2
  baseurl_source: declared
  description: Viewer connection analytics records, including reconnection history
  name: Dolby Analytics V2 API
  phrasing_intents:
  - id: RecordsV2_GetViewerRecords
    intent: Get raw viewer connection rows (v2)
    question: How can I see each reconnect of a viewer session as its own row?
  phrasing_ops: 1
  slug: dolby-analytics-v2-api
- baseURL: https://api.theo.live/v2
  baseurl_source: declared
  description: The Beta API from Dolby — 10 operation(s) for beta.
  name: Dolby Beta API
  phrasing_intents:
  - id: RecordFilesV2_ListMediaAssets
    intent: List media assets (legacy v2 record files)
    question: Which full recordings and clips do I have, through the older v2 record-files listing?
  - id: RecordFilesV2_ReadMediaAsset
    intent: Get a media asset and its download link (legacy)
    question: How do I get a download link for one recording through the v2 record-files endpoint?
  - id: RecordFilesV2_DeleteMediaAssets
    intent: Delete several media assets (legacy v2)
    question: Can I delete multiple media assets in one call with the legacy v2 endpoint?
  - id: RecordFiles_CreateRecordClip
    intent: Clip a recording between two times
    question: How do I cut a clip from a live stream recording with start and stop times?
  - id: RecordFiles_GetClipRequest
    intent: Check the status of a clip request
    question: Has my clip request finished processing?
  - id: RecordFiles_DeleteClipRequestLive
    intent: Delete a clip request and its media
    question: Can I delete a clip request along with every media asset it produced?
  - id: RecordFiles_ListClipRequests
    intent: List live clip requests
    question: What clip requests have been made against my live streams?
  - id: RecordFiles_ListAvailableClipSources
    intent: List streams and time frames available to clip
    question: Which streams and time ranges can I still create clips from?
  phrasing_ops: 13
  slug: dolby-beta-api
- baseURL: https://api.theo.live/v2
  baseurl_source: declared
  description: The Channels API from Dolby — 44 operation(s) for channels.
  name: Dolby Channels API
  phrasing_intents:
  - id: getApiV1Channels
    intent: List OptiView Ads channels
    question: Which ad-break channels do I have configured in OptiView Ads?
  - id: postApiV1Channels
    intent: Create an OptiView Ads channel
    question: How do I set up a channel for scheduling ad breaks in OptiView Ads?
  - id: getApiV1ChannelsByChannelId
    intent: Get one OptiView Ads channel
    question: What timebase and polling intervals does one of my ads channels use?
  - id: patchApiV1ChannelsByChannelId
    intent: Update an OptiView Ads channel
    question: Can I change how far ahead breaks are prefetched on an existing ads channel?
  - id: deleteApiV1ChannelsByChannelId
    intent: Delete an OptiView Ads channel
    question: How do I remove an ad-break channel I no longer use?
  - id: postApiV1ChannelsByChannelIdDetectionEnable
    intent: Turn on automatic ad-break detection
    question: How do I start automatic ad-break detection on a channel?
  - id: postApiV1ChannelsByChannelIdDetectionDisable
    intent: Turn off automatic ad-break detection
    question: How do I stop a channel from detecting ad breaks automatically?
  - id: getApiV1ChannelsByChannelIdBreaks
    intent: List ad breaks on a channel
    question: What ad breaks are scheduled on my channel?
  phrasing_ops: 71
  slug: dolby-channels-api
- baseURL: https://api.theo.live/v2
  baseurl_source: declared
  description: The Cloud Preview API from Dolby — 5 operation(s) for cloud preview.
  name: Dolby Cloud Preview API
  phrasing_intents:
  - id: media-info
    intent: Inspect a cloud media file's technical info
    question: What codec, duration and track details does a media file in cloud storage have?
  - id: image
    intent: Grab a still frame from a cloud video
    question: Can I pull a thumbnail frame from a video sitting in cloud storage?
  - id: cloud-preview-codemill
    intent: Generate an Accurate Player preview template
    question: How can I preview a cloud asset in the Codemill Accurate Player?
  - id: cloud-preview-omakase
    intent: Generate an Omakase Player session template
    question: How do I open a cloud asset in an Omakase Player session?
  - id: cloud-preview-hls
    intent: Generate an HLS preview template
    question: Can I get an HLS preview of a cloud asset without transcoding it myself?
  phrasing_ops: 5
  slug: dolby-cloud-preview-api
- baseURL: https://api.theo.live/v2
  baseurl_source: declared
  description: The Cluster API from Dolby — 1 operation(s) for cluster.
  name: Dolby Cluster API
  phrasing_intents:
  - id: Cluster_GetClustersInfo
    intent: List clusters and the default
    question: Which streaming clusters are available to my account?
  - id: Cluster_UpdateClusterInfo
    intent: Change the default cluster
    question: How do I change the default cluster for my account?
  phrasing_ops: 2
  slug: dolby-cluster-api
- baseURL: https://api.theo.live/v2
  baseurl_source: declared
  description: The Custom Endpoints API from Dolby — 2 operation(s) for custom endpoints.
  name: Dolby Custom Endpoints API
  phrasing_intents:
  - id: create-custom-endpoint
    intent: Add a custom endpoint to a channel
    question: How do I add a custom endpoint with my own CDN to a channel?
  - id: get-channel-custom-endpoints
    intent: List a channel's custom endpoints
    question: Which custom endpoints are configured on a channel?
  - id: get-custom-endpoint
    intent: Get a custom endpoint
    question: What is the configuration of a single custom endpoint?
  - id: update-custom-endpoint
    intent: Update a custom endpoint
    question: Can I change the CDN or priority of an existing custom endpoint?
  - id: delete-custom-endpoint
    intent: Delete a custom endpoint
    question: How do I remove a custom endpoint I no longer need?
  phrasing_ops: 5
  slug: dolby-custom-endpoints-api
- baseURL: https://api.theo.live/v2
  baseurl_source: declared
  description: The Director API from Dolby — 2 operation(s) for director.
  name: Dolby Director API
  phrasing_intents:
  - id: Director_Publish
    intent: Get a URL and auth to publish a stream
    question: How does a broadcaster get the URL and authorization to start publishing a stream?
  - id: Director_Subscribe
    intent: Get a URL and auth to watch a stream
    question: How does a viewer get the URL and authorization to watch a stream?
  phrasing_ops: 2
  slug: dolby-director-api
- baseURL: https://api.theo.live/v2
  baseurl_source: declared
  description: The Distributions API from Dolby — 13 operation(s) for distributions.
  name: Dolby Distributions API
  phrasing_intents:
  - id: get-channel-distributions
    intent: List a channel's distributions
    question: Which distributions are set up on my channel?
  - id: create-channel-distribution
    intent: Create a distribution for a channel
    question: How do I add a new distribution to a live channel?
  - id: get-distribution
    intent: Get a distribution's details
    question: What settings does a specific distribution have?
  - id: update-distribution
    intent: Update a distribution's settings
    question: Can I disable an existing distribution without deleting it?
  - id: delete-distribution
    intent: Delete a distribution
    question: How do I remove a distribution I no longer need?
  - id: get-distribution-security-keys
    intent: List a distribution's security keys
    question: What security keys are attached to my distribution?
  - id: create-distribution-security-key
    intent: Add a security key to a distribution
    question: How do I add a new security key to a distribution?
  - id: delete-all-distribution-security-keys
    intent: Remove all security keys from a distribution
    question: Can I wipe every security key off a distribution at once?
  phrasing_ops: 19
  slug: dolby-distributions-api
- baseURL: https://api.theo.live/v2
  baseurl_source: declared
  description: The DrmLicence API from Dolby — 2 operation(s) for drmlicence.
  name: Dolby Drm Licence API
  phrasing_intents:
  - id: DrmLicence_GetDrmLicence
    intent: Request a DRM license for an asset
    question: Can my player obtain a DRM license for a protected asset through the proxy?
  - id: DrmLicence_GetFairplayCertificate
    intent: Get the FairPlay certificate
    question: Where do I get the FairPlay certificate for Apple playback?
  phrasing_ops: 2
  slug: dolby-drmlicence-api
- baseURL: https://api.theo.live/v2
  baseurl_source: declared
  description: The EncoderProfile API from Dolby — 1 operation(s) for encoderprofile.
  name: Dolby Encoder Profile API
  phrasing_intents:
  - id: EncoderProfile_GetAccountEncoderProfiles
    intent: List account encoder profiles
    question: Which encoder profiles are available on my account?
  phrasing_ops: 1
  slug: dolby-encoderprofile-api
- baseURL: https://api.theo.live/v2
  baseurl_source: declared
  description: The Engines API from Dolby — 6 operation(s) for engines.
  name: Dolby Engines API
  phrasing_intents:
  - id: get-channel-engines
    intent: List a channel's engines
    question: Which encoding engines are attached to my channel?
  - id: create-channel-engine
    intent: Create an engine for a channel
    question: How do I add an encoding engine to a channel in a specific region?
  - id: get-engine
    intent: Get an engine's details
    question: What region and quality is a particular engine configured for?
  - id: update-engine
    intent: Update an engine's settings
    question: Can I change the quality or region of an existing engine?
  - id: delete-engine
    intent: Delete an engine
    question: How do I remove an engine I no longer need?
  - id: start-engine
    intent: Start an engine
    question: How do I start encoding on an engine?
  - id: stop-engine
    intent: Stop a running engine
    question: How do I stop an engine that's currently running?
  - id: get-engine-last-run
    intent: Get an engine's most recent run
    question: When did an engine last run, and how did that run go?
  phrasing_ops: 9
  slug: dolby-engines-api
- baseURL: https://api.theo.live/v2
  baseurl_source: declared
  description: The Image API from Dolby — 1 operation(s) for image.
  name: Dolby Image API
  phrasing_intents:
  - id: image
    intent: Grab a still frame from a cloud video
    question: Can I extract a thumbnail image from a video stored in the cloud?
  phrasing_ops: 1
  slug: dolby-image-api
- baseURL: https://api.theo.live/v2
  baseurl_source: declared
  description: The Ingests API from Dolby — 3 operation(s) for ingests.
  name: Dolby Ingests API
  phrasing_intents:
  - id: get-channel-ingests
    intent: List a channel's ingests
    question: Which ingest sources feed my channel?
  - id: create-channel-ingest
    intent: Create an ingest for a channel
    question: How do I add a new input source to a channel?
  - id: get-ingest
    intent: Get an ingest's details
    question: What type and source URL does a particular ingest use?
  - id: update-ingest
    intent: Update an ingest's settings
    question: Can I change the source URL of an existing ingest?
  - id: delete-ingest
    intent: Delete an ingest
    question: How do I remove an ingest source from my setup?
  - id: get-ingest-engines
    intent: List engines fed by an ingest
    question: Which engines are consuming a given ingest?
  - id: create-ingest-engine
    intent: Create an engine for an ingest
    question: How do I attach a new encoding engine directly to an ingest?
  phrasing_ops: 7
  slug: dolby-ingests-api
- baseURL: https://api.theo.live/v2
  baseurl_source: declared
  description: The Media Info API from Dolby — 1 operation(s) for media info.
  name: Dolby Media Info API
  phrasing_intents:
  - id: media-info
    intent: Inspect a media file's technical info
    question: Can I read the codec and stream details of a media file from its URL?
  phrasing_ops: 1
  slug: dolby-media-info-api
- baseURL: https://api.theo.live/v2
  baseurl_source: declared
  description: The MediaDistributions API from Dolby — 4 operation(s) for mediadistributions.
  name: Dolby Media Distributions API
  phrasing_intents:
  - id: MediaDistributions_CreateMediaDistribution
    intent: Create a media distribution
    question: How do I set up a distribution for viewing HLS media assets?
  - id: MediaDistributions_ListMediaDistribution
    intent: List media distributions
    question: Which media distributions do I have for HLS playback?
  - id: MediaDistributions_ReadMediaDistribution
    intent: Get a media distribution
    question: What settings does a media distribution have?
  - id: MediaDistributions_UpdateMediaDistribution
    intent: Update a media distribution
    question: Can I rename a media distribution?
  - id: MediaDistributions_DeleteMediaDistribution
    intent: Delete a media distribution
    question: How do I delete a media distribution?
  - id: MediaDistributions_GetSecurityKeys
    intent: List a media distribution's security keys
    question: Which security keys protect a media distribution?
  - id: MediaDistributions_CreateSecurityKey
    intent: Add a security key to a media distribution
    question: How many security keys can a media distribution have?
  - id: MediaDistributions_DeleteSecurityKey
    intent: Delete a media distribution security key
    question: How do I revoke a security key on a media distribution?
  phrasing_ops: 8
  slug: dolby-mediadistributions-api
- baseURL: https://api.theo.live/v2
  baseurl_source: declared
  description: The Monetized-Stream API from Dolby — 7 operation(s) for monetized-stream.
  name: Dolby Monetized Stream API
  phrasing_intents:
  - id: GetMonetizedStreams
    intent: List all monetized streams
    question: Which monetized streams have I deployed?
  - id: CreateMonetizedStream
    intent: Deploy a new monetized stream
    question: How do I set up ad insertion for a live stream?
  - id: GetMonetizedStream
    intent: Get one monetized stream
    question: What is the configuration of one monetized stream?
  - id: UpdateMonetizedStream
    intent: Update a monetized stream
    question: Can I change the origin or backdrop of an existing monetized stream?
  - id: DeleteMonetizedStream
    intent: Delete a monetized stream
    question: How do I tear down a monetized stream's signaling service?
  - id: UpdateMonetizedStreamLayout
    intent: Change a monetized stream's default layout
    question: How do I switch only the default ad layout on a monetized stream?
  - id: CreateMonetizedStreamBreak
    intent: Schedule an ad break
    question: How do I insert an ad break into a live monetized stream?
  - id: GetMonetizedStreamBreaks
    intent: List all ad breaks on a monetized stream
    question: Which ad breaks are scheduled on a monetized stream?
  phrasing_ops: 13
  slug: dolby-monetized-stream-api
- baseURL: https://api.theo.live/v2
  baseurl_source: declared
  description: The Monetized-Stream-V2 API from Dolby — 3 operation(s) for monetized-stream-v2.
  name: Dolby Monetized Stream V2 API
  phrasing_intents:
  - id: GetMonetizedStreamsPaginated
    intent: Page through monetized streams
    question: Can I page through my monetized streams with a limit and skip?
  - id: GetMonetizedStreamBreaksPaginated
    intent: Page through a stream's ad breaks
    question: Can I paginate the ad breaks on a monetized stream?
  - id: GetMonetizedStreamOverlaysPaginated
    intent: Page through a stream's overlays
    question: Can I paginate the overlay ads on a monetized stream?
  phrasing_ops: 3
  slug: dolby-monetized-stream-v2-api
- baseURL: https://api.theo.live/v2
  baseurl_source: declared
  description: The Monitoring API from Dolby — 9 operation(s) for monitoring.
  name: Dolby Monitoring API
  phrasing_intents:
  - id: Monitoring_ListRecentStreams
    intent: List live and recent streams in detail
    question: Which streams are live right now or ended in the last hour?
  - id: Monitoring_GetStream
    intent: Get full monitoring details of a stream
    question: What are the full feed details of a stream I'm monitoring?
  - id: Monitoring_ListStreamSummary
    intent: List a lightweight summary of streams
    question: Can I get a quick summary list of active and recently ended streams?
  - id: Monitoring_GetStreamSummary
    intent: Get a lightweight summary of one stream
    question: Can I get a stream's summary without all the feed details?
  - id: get-channel-monitoring
    intent: Get health status of a channel
    question: Are a channel's ingests, engines and distributions healthy right now?
  - id: get-ingest-monitoring
    intent: Get metrics for one ingest
    question: What packet loss and round-trip time is one ingest seeing?
  - id: get-engine-monitoring
    intent: Get rendition metrics for one engine
    question: How are the renditions of a single engine performing?
  - id: get-channel-ingests-monitoring
    intent: Get metrics for all ingests of a channel
    question: How are all the ingests on a channel performing together?
  phrasing_ops: 9
  slug: dolby-monitoring-api
- baseURL: https://api.theo.live/v2
  baseurl_source: declared
  description: The MultiTrackVideo API from Dolby — 1 operation(s) for multitrackvideo.
  name: Dolby Multi Track Video API
  phrasing_intents:
  - id: MultiTrackVideo_Configuration
    intent: Get multi-track video config for OBS
    question: How does OBS get its multi-track video configuration for streaming?
  phrasing_ops: 1
  slug: dolby-multitrackvideo-api
- baseURL: https://api.theo.live/v2
  baseurl_source: declared
  description: The Organizations API from Dolby — 3 operation(s) for organizations.
  name: Dolby Organizations API
  phrasing_intents:
  - id: getApiV1OrganizationsIntegrations
    intent: List organization ad integrations
    question: Which ad-system integrations are configured for my whole organization?
  - id: postApiV1OrganizationsIntegrations
    intent: Create an organization ad integration
    question: How do I connect my Google Ad Manager network to OptiView Ads?
  - id: getApiV1OrganizationsIntegrationsByOrganizationIntegrationId
    intent: Get one organization integration
    question: What network code is stored on a particular organization integration?
  - id: patchApiV1OrganizationsIntegrationsByOrganizationIntegrationId
    intent: Update an organization integration
    question: Can I rotate the service account credentials on an existing integration?
  - id: deleteApiV1OrganizationsIntegrationsByOrganizationIntegrationId
    intent: Delete an organization integration
    question: How do I disconnect my organization from its ad server integration?
  - id: postApiV1OrganizationsIntegrationsByOrganizationIntegrationIdVerify
    intent: Verify integration credentials
    question: How can I check that my stored service account credentials actually work?
  phrasing_ops: 6
  slug: dolby-organizations-api
- baseURL: https://api.theo.live/v2
  baseurl_source: declared
  description: The PublishTokenV1 API from Dolby — 9 operation(s) for publishtokenv1.
  name: Dolby Publish Token V1 API
  phrasing_intents:
  - id: PublishTokenV1_ReadToken
    intent: Get a publish token
    question: What settings does a specific publish token have?
  - id: PublishTokenV1_DeleteToken
    intent: Delete a publish token
    question: How do I permanently delete a publish token?
  - id: PublishTokenV1_UpdateToken
    intent: Update a publish token (v1)
    question: Can I turn on recording for an existing publish token?
  - id: PublishTokenV1_ListTokens
    intent: List publish tokens
    question: Which publish tokens exist on my account?
  - id: PublishTokenV1_ListTokensByName
    intent: Find publish tokens by name
    question: Can I find publish tokens by token label or stream name?
  - id: PublishTokenV1_ListTokensByCluster
    intent: List publish tokens in a cluster
    question: Which publish tokens are tied to a particular cluster region?
  - id: PublishTokenV1_CreateToken
    intent: Create a publish token
    question: How do I create a token so a broadcaster can publish a stream?
  - id: PublishTokenV1_GetActiveTokenByStreamId
    intent: Find the publish token of a live stream
    question: Which publish token is a live stream currently using?
  phrasing_ops: 11
  slug: dolby-publishtokenv1-api
- baseURL: https://api.theo.live/v2
  baseurl_source: declared
  description: The PublishTokenV2 API from Dolby — 1 operation(s) for publishtokenv2.
  name: Dolby Publish Token V2 API
  phrasing_intents:
  - id: PublishTokenV2_UpdateToken
    intent: Update a publish token (v2)
    question: Can I update a publish token through the v2 endpoint?
  phrasing_ops: 1
  slug: dolby-publishtokenv2-api
- baseURL: https://api.theo.live/v2
  baseurl_source: declared
  description: The RecordFiles API from Dolby — 8 operation(s) for recordfiles.
  name: Dolby Record Files API
  phrasing_intents:
  - id: RecordFiles_GetRecordFile
    intent: Get a recorded file and download link
    question: How do I get a temporary download link for one recording file?
  - id: RecordFiles_DeleteRecordFile
    intent: Delete a recorded file
    question: How do I delete one recording from storage?
  - id: RecordFiles_DeleteRecordFiles
    intent: Delete several recorded files
    question: Can I delete a batch of recordings in one request?
  - id: RecordFiles_DeleteAllRecordFiles
    intent: Delete every recorded file
    question: Is there a way to wipe all recordings from storage at once?
  - id: RecordFiles_ListRecordFiles
    intent: List recorded files
    question: Which recordings do I have stored on my account?
  - id: RecordFiles_ListRecordFilesByToken
    intent: List recorded files for a publish token
    question: Which recordings were made with a particular publish token?
  - id: RecordFiles_ListRecordFilesByStream
    intent: List recorded files for a stream
    question: What recordings exist for one stream name?
  - id: RecordFiles_RecordFileUsage
    intent: Get current recording storage bytes
    question: How many bytes of recordings am I storing right now?
  phrasing_ops: 9
  slug: dolby-recordfiles-api
- baseURL: https://api.theo.live/v2
  baseurl_source: declared
  description: The Regions API from Dolby — 4 operation(s) for regions.
  name: Dolby Regions API
  phrasing_intents:
  - id: get-regions
    intent: List available streaming regions
    question: Which regions can I run my channels in?
  - id: get-region
    intent: Get a region's details
    question: What are the details of a specific region?
  - id: get-region-sdi-devices
    intent: List SDI devices in an on-prem region
    question: Which SDI capture devices are available in my on-prem region?
  - id: get-region-ndi-sources
    intent: List NDI sources in an on-prem region
    question: Which NDI sources can my on-prem region see on the network?
  phrasing_ops: 4
  slug: dolby-regions-api
- baseURL: https://api.theo.live/v2
  baseurl_source: declared
  description: The Schedulers API from Dolby — 2 operation(s) for schedulers.
  name: Dolby Schedulers API
  phrasing_intents:
  - id: get-schedulers
    intent: List channel schedulers
    question: Which schedules are set up to start my channels automatically?
  - id: create-scheduler
    intent: Schedule channels to run at a set time
    question: How do I schedule a channel to go live at a specific date and time?
  - id: get-scheduler
    intent: Get a scheduler's details
    question: When does a particular scheduler start and end?
  - id: update-scheduler
    intent: Update a scheduler
    question: Can I change the start time of a scheduler I already made?
  - id: delete-scheduler
    intent: Delete a scheduler
    question: How do I cancel a schedule permanently?
  phrasing_ops: 5
  slug: dolby-schedulers-api
- baseURL: https://api.theo.live/v2
  baseurl_source: declared
  description: The Stream API from Dolby — 3 operation(s) for stream.
  name: Dolby Stream API
  phrasing_intents:
  - id: Stream_StopStream
    intent: Stop one active stream
    question: How do I force-stop a single live stream that's broadcasting?
  - id: Stream_StopByAccount
    intent: Stop every active stream on the account
    question: Is there an emergency way to stop all live streams on my account at once?
  - id: Stream_ReprioritizeStream
    intent: Change an active stream's priority
    question: Can I change the priority of a stream that's already live?
  phrasing_ops: 3
  slug: dolby-stream-api
- baseURL: https://api.theo.live/v2
  baseurl_source: declared
  description: The SubscribeTokenV1 API from Dolby — 4 operation(s) for subscribetokenv1.
  name: Dolby Subscribe Token V1 API
  phrasing_intents:
  - id: SubscribeTokenV1_ReadToken
    intent: Get a subscribe token
    question: What streams and restrictions does a subscribe token have?
  - id: SubscribeTokenV1_DeleteToken
    intent: Delete a subscribe token
    question: How do I revoke a viewer's subscribe token for good?
  - id: SubscribeTokenV1_UpdateToken
    intent: Update a subscribe token
    question: How do I add another stream to an existing subscribe token?
  - id: SubscribeTokenV1_ListTokens
    intent: List subscribe tokens
    question: Which subscribe tokens exist on my account?
  - id: SubscribeTokenV1_ListTokensByName
    intent: Find subscribe tokens by label or stream
    question: Which subscribe tokens grant access to a particular stream name?
  - id: SubscribeTokenV1_CreateToken
    intent: Create a subscribe token for viewers
    question: How do I create a token so viewers can watch a secure stream?
  phrasing_ops: 6
  slug: dolby-subscribetokenv1-api
- baseURL: https://api.theo.live/v2
  baseurl_source: declared
  description: The SubscribeTokenV2 API from Dolby — 1 operation(s) for subscribetokenv2.
  name: Dolby Subscribe Token V2 API
  phrasing_intents:
  - id: SubscribeTokenV2_UpdateToken
    intent: Update a subscribe token (v2)
    question: How do I add streams to a subscribe token with the v2 endpoint?
  phrasing_ops: 1
  slug: dolby-subscribetokenv2-api
- baseURL: https://api.theo.live/v2
  baseurl_source: declared
  description: The Templates API from Dolby — 2 operation(s) for templates.
  name: Dolby Templates API
  phrasing_intents:
  - id: getApiV1Templates
    intent: List ad break templates
    question: Which reusable ad break templates have I defined?
  - id: postApiV1Templates
    intent: Create an ad break template
    question: How do I create a reusable template with a default break duration?
  - id: deleteApiV1Templates
    intent: Bulk delete break templates
    question: Can I delete several break templates in one go?
  - id: getApiV1TemplatesByTemplateId
    intent: Get one break template
    question: What variants and playback controls does a particular template define?
  - id: patchApiV1TemplatesByTemplateId
    intent: Update a break template
    question: Can I change the default duration on an existing break template?
  - id: deleteApiV1TemplatesByTemplateId
    intent: Delete a single break template
    question: How do I remove one break template I no longer need?
  phrasing_ops: 6
  slug: dolby-templates-api
- baseURL: https://api.theo.live/v2
  baseurl_source: declared
  description: The Thumbnails API from Dolby — 1 operation(s) for thumbnails.
  name: Dolby Thumbnails API
  phrasing_intents:
  - id: Thumbnails_TriggerThumbnail
    intent: Generate a thumbnail of a live stream
    question: Can I grab a thumbnail from a stream that's live right now?
  phrasing_ops: 1
  slug: dolby-thumbnails-api
- baseURL: https://api.theo.live/v2
  baseurl_source: declared
  description: The Transcoder API from Dolby — 7 operation(s) for transcoder.
  name: Dolby Transcoder API
  phrasing_intents:
  - id: Transcoder_GetTranscoder
    intent: Get a cloud transcoder
    question: What is the configuration of one of my cloud transcoders?
  - id: Transcoder_UpdateTranscoder
    intent: Update a cloud transcoder
    question: Can I change a transcoder's output height or frame rate without restarting it?
  - id: Transcoder_DeleteTranscoder
    intent: Delete a cloud transcoder
    question: How do I delete a transcoder and all its instances?
  - id: Transcoder_CreateTranscoder
    intent: Create a cloud transcoder for ABR
    question: How do I get adaptive bitrate simulcast without sending multiple contribution feeds?
  - id: Transcoder_ListTranscoders
    intent: List cloud transcoders
    question: Which cloud transcoders are configured on my account?
  - id: Transcoder_StartTranscoder
    intent: Start a cloud transcoder
    question: How do I enable a transcoder so it accepts incoming broadcasts?
  - id: Transcoder_StopTranscoder
    intent: Stop a cloud transcoder
    question: Can I shut down a transcoder without deleting its configuration?
  - id: Transcoder_GetTranscoderInstance
    intent: Get a transcoder instance
    question: What is the status of a single transcoder host instance?
  phrasing_ops: 10
  slug: dolby-transcoder-api
- baseURL: https://api.theo.live/v2
  baseurl_source: declared
  description: The TranscoderScheduler API from Dolby — 4 operation(s) for transcoderscheduler.
  name: Dolby Transcoder Scheduler API
  phrasing_intents:
  - id: TranscoderScheduler_CreateSchedule
    intent: Schedule transcoders to start and stop
    question: How do I schedule transcoders to start and stop automatically?
  - id: TranscoderScheduler_DeleteSchedule
    intent: Delete a transcoder schedule
    question: How do I cancel a transcoder schedule?
  - id: TranscoderScheduler_UpdateSchedule
    intent: Update a transcoder schedule
    question: Can I change the start or stop time of an existing transcoder schedule?
  - id: TranscoderScheduler_GetScheduleByScheduleId
    intent: Get a transcoder schedule
    question: What does one transcoder schedule look like in summary?
  - id: TranscoderScheduler_ListAllSchedules
    intent: List all transcoder schedules
    question: Which transcoder schedules exist on my account?
  - id: TranscoderScheduler_GetSchedulesForTranscoder
    intent: List schedules for one transcoder
    question: Which schedules apply to a specific transcoder?
  phrasing_ops: 6
  slug: dolby-transcoderscheduler-api
- baseURL: https://api.theo.live/v2
  baseurl_source: declared
  description: The Webhooks API from Dolby — 8 operation(s) for webhooks.
  name: Dolby Webhooks API
  phrasing_intents:
  - id: Webhooks_Get
    intent: Read a streaming webhook's details
    question: What URL and event types is one of my streaming webhooks set to?
  - id: Webhooks_UpdateWebhook
    intent: Update a streaming webhook or rotate its secret
    question: How do I refresh the signing secret on a streaming webhook?
  - id: Webhooks_RemoveWebhook
    intent: Remove a streaming webhook
    question: How do I delete a streaming account webhook by its webhook ID?
  - id: Webhooks_ListWebhooks
    intent: List streaming account webhooks
    question: Which webhooks are registered on my streaming account?
  - id: Webhooks_AddWebhook
    intent: Add a streaming account webhook
    question: How do I get notified when a feed starts or stops on my streaming account?
  - id: Webhooks_TestWebhook
    intent: Send a test webhook event
    question: Can I fire a sample event to check my webhook endpoint works?
  - id: get-webhooks
    intent: List live channel platform webhooks
    question: What webhooks exist on the channel management platform?
  - id: create-webhook
    intent: Create a channel platform webhook
    question: How do I create a named webhook for channel events?
  phrasing_ops: 13
  slug: dolby-webhooks-api
- baseURL: https://api.theo.live/v2
  baseurl_source: declared
  description: The Whep API from Dolby — 1 operation(s) for whep.
  name: Dolby Whep API
  phrasing_intents:
  - id: Whep_WhepSubscribe
    intent: Subscribe to a stream over WHEP
    question: How do I play back a stream with WHEP by sending an SDP offer?
  phrasing_ops: 1
  slug: dolby-whep-api
- baseURL: https://api.theo.live/v2
  baseurl_source: declared
  description: The Whip API from Dolby — 1 operation(s) for whip.
  name: Dolby Whip API
  phrasing_intents:
  - id: Whip_WhipPublish
    intent: Publish a stream over WHIP
    question: Can I publish a WebRTC stream with a WHIP-compatible encoder?
  phrasing_ops: 1
  slug: dolby-whip-api
- baseURL: https://api.theo.live/v2
  baseurl_source: declared
  description: The Media Assets API from Dolby — 5 operation(s) for media assets.
  name: Dolby Media Assets API
  phrasing_intents:
  - id: MediaAssets_CreateMediaAsset
    intent: Clip a segment from a live stream
    question: How do I make a clip from a stream that's live right now?
  - id: MediaAssets_ListMediaAssets
    intent: List recordings, clips and media assets
    question: Which recordings and clips do I have stored?
  - id: MediaAssets_DeleteMediaAssets
    intent: Delete selected media assets
    question: How do I delete several specific recordings or clips at once?
  - id: MediaAssets_GetUploadCredentials
    intent: Get credentials to upload media
    question: How do I upload my own video file into Dolby media storage?
  - id: MediaAssets_RegisterMediaAsset
    intent: Register an uploaded media file
    question: What do I call after uploading media so it gets processed?
  - id: MediaAssets_ReadMediaAsset
    intent: Get a media asset and its links
    question: Where can I download a finished recording?
  - id: MediaAssets_UpdateMediaAsset
    intent: Update a media asset's distribution
    question: Can I move a media asset to a different media distribution?
  - id: MediaAssets_DeleteMediaAssets2
    intent: Delete all media assets of a type
    question: Can I wipe every recording or every clip in one call?
  phrasing_ops: 8
  slug: dolby-media-assets-api
artifact_total: 54
asyncapis:
- description: ''
  name: Dolby Webhooks
  slug: dolby-webhooks
common:
- group: other
  href: https://artifacts.apis.io/dolby/capabilities/dolby-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/dolby-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/dolby/overlays/dolby-optiview-live-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/dolby-optiview-live-overlay.yaml
- group: other
  href: https://artifacts.apis.io/dolby/overlays/dolby-millicast-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/dolby-millicast-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/dolby/overlays/dolby-optiview-ads-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/dolby-optiview-ads-overlay.yaml
- group: other
  href: https://artifacts.apis.io/dolby/overlays/dolby-optiview-ad-engine-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/dolby-optiview-ad-engine-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.dolby.com
- group: start
  title: ''
  type: Portal
  url: https://optiview.dolby.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://optiview.dolby.com/docs/
- group: docs
  title: ''
  type: Documentation
  url: https://optiview.dolby.com/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://optiview.dolby.com/docs/millicast/api/millicast-api/
- group: start
  title: ''
  type: GettingStarted
  url: https://optiview.dolby.com/docs/theolive/api/full-example/
- group: operate
  title: ''
  type: Support
  url: https://support.dolby.io/hc/en-au
- group: company
  title: ''
  type: Blog
  url: https://optiview.dolby.com/resources/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://optiview.dolby.com/feed/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/THEOplayer
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/millicast
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/DolbyIO
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/dolbylaboratories
- group: commercial
  title: ''
  type: Pricing
  url: https://optiview.dolby.com/plans/
- group: start
  title: ''
  type: Login
  url: https://portal.theoplayer.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://optiview.dolby.com/policies/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://optiview.dolby.com/policies/privacy-policy/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/dolbyoptiview
- group: operate
  title: ''
  type: StatusPage
  url: https://status.dolby.io
- group: operate
  title: ''
  type: ChangeLog
  url: https://optiview.dolby.com/docs/millicast/changelog/changelog-rest-apis/
- group: agent
  href: https://artifacts.apis.io/dolby/llms/dolby-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dolby-llms.txt
- group: agent
  href: https://artifacts.apis.io/dolby/well-known/dolby-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dolby-well-known.yml
- group: auth
  href: https://artifacts.apis.io/dolby/well-known/dolby-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/dolby-security.txt
- group: auth
  href: https://artifacts.apis.io/dolby/security/dolby-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/dolby-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/dolby/security/dolby-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/dolby-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/dolby/security/dolby-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dolby-domain-security.yml
- group: build
  href: https://artifacts.apis.io/dolby/packages/dolby-packages.yml
  title: ''
  type: Packages
  url: packages/dolby-packages.yml
- group: build
  href: https://artifacts.apis.io/dolby/packages/dolby-packages.yml
  title: ''
  type: SDKs
  url: packages/dolby-packages.yml
- group: design
  href: https://artifacts.apis.io/dolby/components/dolby-components.yml
  title: ''
  type: Components
  url: components/dolby-components.yml
- group: build
  href: https://artifacts.apis.io/dolby/cli/dolby-cli.yml
  title: ''
  type: CLI
  url: cli/dolby-cli.yml
- group: auth
  href: https://artifacts.apis.io/dolby/authentication/dolby-authentication.yml
  title: ''
  type: Authentication
  url: authentication/dolby-authentication.yml
- group: design
  href: https://artifacts.apis.io/dolby/conventions/dolby-conventions.yml
  title: ''
  type: Conventions
  url: conventions/dolby-conventions.yml
- group: design
  href: https://artifacts.apis.io/dolby/conventions/dolby-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/dolby-conventions.yml
- group: design
  href: https://artifacts.apis.io/dolby/errors/dolby-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/dolby-problem-types.yml
- group: design
  href: https://artifacts.apis.io/dolby/data-model/dolby-data-model.yml
  title: ''
  type: DataModel
  url: data-model/dolby-data-model.yml
- group: design
  href: https://artifacts.apis.io/dolby/lifecycle/dolby-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/dolby-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/dolby/lifecycle/dolby-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/dolby-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/dolby/conformance/dolby-conformance.yml
  title: ''
  type: Conformance
  url: conformance/dolby-conformance.yml
- group: design
  href: https://artifacts.apis.io/dolby/asyncapi/dolby-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/dolby-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/dolby/mcp/dolby-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/dolby-mcp.yml
- group: agent
  href: https://artifacts.apis.io/dolby/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: operate
  href: https://artifacts.apis.io/dolby/changelog/dolby-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/dolby-changelog.yml
- group: commercial
  href: https://artifacts.apis.io/dolby/plans/dolby-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/dolby-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/dolby/rate-limits/dolby-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/dolby-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/dolby/finops/dolby-finops.yml
  title: ''
  type: FinOps
  url: finops/dolby-finops.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/dolbyio-samples
created: '2025-03-01'
description: Dolby Laboratories is an audio and video technology company whose developer platform, Dolby OptiView, is the merged surface of the original dolby.io platform, THEO Technologies (THEOplayer, THEOlive, THEOads) and Millicast. It ships publicly documented REST APIs for real-time WebRTC streaming, live channel orchestration, video playback, server-guided ad insertion and just-in-time ad conformance, alongside player SDKs for web, mobile, smart TV, Roku, React Native and Flutter. Dolby is also responsible for Dolby Atmos, Dolby Vision and Dolby Digital.
finops:
- has_sources: true
  method: derived
  name: Dolby Finops
  primary_unit: ''
  service_category: ''
  slug: dolby-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dolby.png
layout: provider
mcp_servers:
- description: ''
  name: Dolby MCP Server
  slug: dolby-mcp-yml
modified: '2026-09-06'
name: Dolby
nav: Providers
network: true
overview: 'Dolby publishes 41 API contracts indexed on the [APIs.io](https://apis.io/) network, including ABR Ladders API, Account API, Ad Engine API, and 38 more. Tagged areas include Audio, Video, Streaming, Media, and Real-Time.


  The Dolby catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Dolby''s developer surface includes developer portal, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 44 more developer resources.'
plans:
- name: Dolby Plans Pricing
  plan_count: 3
  slug: dolby-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 1
  name: Dolby Rate Limits
  slug: dolby-rate-limits
rules:
- authorship: generated
  effective_rule_count: 94
  extends:
  - spectral:oas
  name: Dolby API Rules
  rule_count: 53
  severity_counts:
    error: 32
    hint: 0
    info: 7
    warn: 14
  slug: dolby-rules
score:
  band: exemplar
  composite: 67.2
  coverage:
    artifact_dirs: 30
    catalog_earned: 59.5
    catalog_earned_first_party: 20.0
    catalog_gap: 55.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 69.7
    contract_governance: 18.2
    contract_quality: 57.8
    developer_ergonomics: 73.2
    discoverability: 69.6
    operational_transparency: 81.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 67.2
  provenance:
    conformance: derived
    contracts:
      callable: 80.0
      derived: 0
      marker_coverage: 0.0
      total: 40
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 27.8
screenshot: https://apis.io/screenshots/dolby/dolby-2026-06-20T180133.png
security:
- kind: authentication
  name: Dolby Authentication
  slug: dolby-authentication
  summary_line: apiKey/http · 5 schemes
- kind: domain-security
  name: Dolby Domain Security
  slug: dolby-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Dolby Vulnerability Disclosure
  slug: dolby-vulnerability-disclosure
  summary_line: Bugcrowd · security.txt · contact published
skill_count: 4
skills:
- name: dolby-clip-live-stream
  slug: dolby-clip-live-stream
- name: dolby-launch-live-channel
  slug: dolby-launch-live-channel
- name: dolby-provision-realtime-stream
  slug: dolby-provision-realtime-stream
- name: dolby-wire-webhooks
  slug: dolby-wire-webhooks
slug: dolby
tags:
- Audio
- Video
- Streaming
- Media
- Real-Time
- WebRTC
- Advertising
- Video Player
- Live Streaming
- Broadcasting
website: https://www.dolby.com
---
