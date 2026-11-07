---
access_model:
  confidence: medium
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
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: true
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: mostly
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 46.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 52
  human_in_the_loop: 2
  name: Mux Com Agentic Access
  operation_count: 124
  slug: mux-com-agentic-access
  summary_line: 124 operations · 52 acting · 2 human-in-the-loop
api_count: 2
apis:
- description: Mux Webhooks deliver signed HTTP callbacks for asset, upload, live stream, and robots job lifecycle events (video.asset.created, video.asset.ready, video.live_stream.active, video.upload.asset_created
  name: Mux Webhooks
  slug: webhooks
- baseURL: https://api.mux.com
  baseurl_source: declared
  description: APIs for retrieving animated images from videos hosted using Mux.
  name: Mux Animated Images API
  phrasing_intents:
  - id: get-animated
    intent: Get an animated GIF or WebP clip from a video
    question: How do I turn a segment of my Mux video into an animated GIF?
  phrasing_ops: 1
  slug: mux-com-animated-images-api
- baseURL: https://api.mux.com
  baseurl_source: declared
  description: Annotations allow you to add notes at a specific datetime to view in the Mux Data dashboard.
  name: Mux Annotations API
  phrasing_intents:
  - id: list-annotations
    intent: List annotations on my video analytics
    question: Which annotations have been added to my Mux Data charts?
  - id: create-annotation
    intent: Add an annotation to analytics charts
    question: How do I mark a deploy date on my Mux Data charts with a note?
  - id: get-annotation
    intent: Get one annotation's details
    question: What does annotation I created earlier say, and what date is it on?
  - id: update-annotation
    intent: Edit an existing annotation
    question: Can I change the note or date on an annotation that already exists?
  - id: delete-annotation
    intent: Delete an annotation
    question: How do I remove an annotation I no longer want on my charts?
  phrasing_ops: 5
  slug: mux-com-annotations-api
- baseURL: https://api.mux.com
  baseurl_source: declared
  description: Ask questions about a video and get structured answers.
  name: Mux Ask Questions API
  phrasing_intents:
  - id: create-ask-questions-job
    intent: Ask AI questions about a video asset
    question: Can AI answer questions about what happens in one of my Mux videos?
  - id: get-ask-questions-job
    intent: Get answers from an ask-questions job
    question: Where do I find the answers from an ask-questions job I started?
  phrasing_ops: 2
  slug: mux-com-ask-questions-api
- baseURL: https://api.mux.com
  baseurl_source: declared
  description: An asset refers to a piece of media content that is stored or is being live streamed through the Mux system. An asset always has a duration and one or more tracks (audio, video, and text data). The me
  name: Mux Assets API
  phrasing_intents:
  - id: listAssets
    intent: List video assets
    question: Which video assets are in my Mux environment?
  - id: createAsset
    intent: Create a video asset
    question: How do I create a new video asset in Mux from a file?
  - id: getAsset
    intent: Get a video asset's details
    question: Is my video asset ready to play yet?
  - id: updateAsset
    intent: Update a video asset
    question: Can I change settings on a video asset after it's created?
  - id: deleteAsset
    intent: Delete a video asset
    question: How do I permanently delete a video from Mux?
  - id: get-asset-input-info
    intent: See the inputs used to create an asset
    question: What source files and input settings were used to build this asset?
  - id: create-asset-playback-id
    intent: Add a playback ID to an asset
    question: How do I get a new playback ID so viewers can stream my asset?
  - id: get-asset-playback-id
    intent: Get an asset's playback ID details
    question: What policy is set on a particular playback ID of my asset?
  phrasing_ops: 17
  slug: mux-com-assets-api
- baseURL: https://api.mux.com
  baseurl_source: declared
  description: APIs for retrieving captions and transcripts from videos hosted using Mux that have had captions generated automatically.
  name: Mux Captions and Transcripts API
  phrasing_intents:
  - id: get-vtt-text-track
    intent: Download a text track as a WebVTT file
    question: How do I download the captions of a video as a .vtt file?
  - id: get-transcript
    intent: Download a plain-text transcript of a video
    question: Can I get a plain text transcript of what's said in my video?
  phrasing_ops: 2
  slug: mux-com-captions-and-transcripts-api
- baseURL: https://api.mux.com
  baseurl_source: declared
  description: The Delivery Usage API allows you to get delivery/streaming usage details for each asset and across all assets. Delivery usage details are aggregated every hour at the top of the hour and can be reque
  name: Mux Delivery Usage API
  phrasing_intents:
  - id: list-delivery-usage
    intent: Report video delivery usage
    question: How many minutes of video did I deliver per asset last month?
  phrasing_ops: 1
  slug: mux-com-delivery-usage-api
- baseURL: https://api.mux.com
  baseurl_source: declared
  description: Dimensions are the types of metadata that can be collected for a video view. Some dimensions are collected automatically based on the playback or device, such as the viewer's Country or the device inf
  name: Mux Dimensions API
  phrasing_intents:
  - id: list-dimensions
    intent: List the dimensions I can break views down by
    question: What dimensions can I slice my video view data by?
  - id: list-dimension-values
    intent: List values of a dimension with view counts
    question: Which browsers are my viewers using, and how many views does each have?
  - id: list-dimension-elements
    intent: List elements of a trace dimension
    question: How do I see individual CDN hops in the video_cdn_trace dimension?
  phrasing_ops: 3
  slug: mux-com-dimensions-api
- baseURL: https://api.mux.com
  baseurl_source: declared
  description: Direct upload allows you to push assets directly to Mux storage instead of needing to go through your own first. When you create a new direct upload, we'll give you back a signed URL for a Google Clou
  name: Mux Direct Uploads API
  phrasing_intents:
  - id: listUploads
    intent: List direct uploads
    question: Which direct uploads have been created in my environment?
  - id: createUpload
    intent: Create a direct upload URL
    question: How do I let users upload a video straight from their browser?
  - id: getUpload
    intent: Check a direct upload's status
    question: Has a user's direct upload finished and turned into an asset?
  - id: cancel-direct-upload
    intent: Cancel a pending direct upload
    question: How do I stop a direct upload that hasn't completed yet?
  phrasing_ops: 4
  slug: mux-com-direct-uploads-api
- baseURL: https://api.mux.com
  baseurl_source: declared
  description: DRM Configurations allow you to adjust the security level of content delivered through Mux Video's Digital Rights Management (DRM) feature.
  name: Mux DRM Configurations API
  phrasing_intents:
  - id: list-drm-configurations
    intent: List DRM configurations
    question: Which DRM configurations are available in my account?
  - id: get-drm-configuration
    intent: Get one DRM configuration
    question: What are the details of a specific DRM configuration?
  phrasing_ops: 2
  slug: mux-com-drm-configurations-api
- baseURL: https://api.mux.com
  baseurl_source: declared
  description: Edit an existing caption track with find-and-replace edits and optional profanity censoring. This workflow is currently in beta.
  name: Mux Edit Captions API
  phrasing_intents:
  - id: create-edit-captions-job
    intent: Edit captions with replacements or censoring
    question: Can I automatically bleep out profanity in my video's captions?
  - id: get-edit-captions-job
    intent: Get the result of an edit-captions job
    question: Is my caption editing job done yet?
  phrasing_ops: 2
  slug: mux-com-edit-captions-api
- baseURL: https://api.mux.com
  baseurl_source: declared
  description: Playback errors are tracked and aggregated by Mux Data. Errors can be listed by the API, which contains data about the error code, message, and how often the error occurred.
  name: Mux Errors API
  phrasing_intents:
  - id: list-errors
    intent: List playback errors viewers hit
    question: What playback errors are my viewers running into most?
  phrasing_ops: 1
  slug: mux-com-errors-api
- baseURL: https://api.mux.com
  baseurl_source: declared
  description: Exports allow you to download the daily CSV files that are generated from the video views that occurred in the previous day. Please contact [support](mailto:support@mux.com) for information about enab
  name: Mux Exports API
  phrasing_intents:
  - id: list-exports
    intent: List view export links (legacy)
    question: Where are the download links for my older video view exports?
  - id: list-exports-views
    intent: List available video view exports
    question: How do I download my raw video view data exports?
  phrasing_ops: 2
  slug: mux-com-exports-api
- baseURL: https://api.mux.com
  baseurl_source: declared
  description: Deprecated, please refer to the Dimensions APIs.
  name: Mux Filters API
  phrasing_intents:
  - id: list-filters
    intent: List analytics filters (legacy)
    question: What basic and advanced filters exist in the old filters API?
  - id: list-filter-values
    intent: List values of a filter (legacy)
    question: Can I still get values and view counts for a filter via the old API?
  phrasing_ops: 2
  slug: mux-com-filters-api
- baseURL: https://api.mux.com
  baseurl_source: declared
  description: Identify key moments in a video.
  name: Mux Find Key Moments API
  phrasing_intents:
  - id: create-find-key-moments-job
    intent: Find key moments in a video with AI
    question: Can AI pick out the highlight moments in one of my videos?
  - id: get-find-key-moments-job
    intent: Get key moments found by a job
    question: Where do I read the key moments a job found in my video?
  phrasing_ops: 2
  slug: mux-com-find-key-moments-api
- baseURL: https://api.mux.com
  baseurl_source: declared
  description: Generate chapters for a video.
  name: Mux Generate Chapters API
  phrasing_intents:
  - id: create-generate-chapters-job
    intent: Generate video chapters with AI
    question: Can Mux automatically split my video into chapters?
  - id: get-generate-chapters-job
    intent: Get chapters from a generate-chapters job
    question: Where can I get the chapter list an AI job produced for my video?
  phrasing_ops: 2
  slug: mux-com-generate-chapters-api
- baseURL: https://api.mux.com
  baseurl_source: declared
  description: Incidents occur when an anomaly alert is triggered in Mux Data. The Incidents API provides operations related to the raising and managing of alerting incidents.
  name: Mux Incidents API
  phrasing_intents:
  - id: list-incidents
    intent: List video quality incidents
    question: Are there any open playback incidents affecting my viewers right now?
  - id: get-incident
    intent: Get an incident's details
    question: What happened during a specific playback incident?
  - id: list-related-incidents
    intent: List incidents related to an incident
    question: Which other incidents seem connected to this one?
  phrasing_ops: 3
  slug: mux-com-incidents-api
- baseURL: https://api.mux.com
  baseurl_source: declared
  description: List and cancel jobs across all workflows.
  name: Mux Jobs API
  phrasing_intents:
  - id: list-jobs
    intent: List AI robot jobs
    question: Which AI jobs have I run against my video assets?
  - id: cancel-job
    intent: Cancel a pending or running AI job
    question: How do I stop an AI job that's still processing?
  phrasing_ops: 2
  slug: mux-com-jobs-api
- baseURL: https://api.mux.com
  baseurl_source: declared
  description: A Live Stream represents a unique live stream of video being pushed to Mux. It includes configuration details (a Stream Key) for live broadcasting software/hardware and a Playback ID for playing the s
  name: Mux Live Streams API
  phrasing_intents:
  - id: listLiveStreams
    intent: List live streams (live_streams path)
    question: Is there an older underscore live_streams route to list my streams?
  - id: createLiveStream
    intent: Create a live stream (live_streams path)
    question: Can I create a live stream through the live_streams underscore route?
  - id: getLiveStream
    intent: Get a live stream (live_streams path)
    question: Can I fetch a stream's details through the underscore live_streams route?
  - id: create-live-stream
    intent: Create a live stream
    question: How do I set up a new live stream my encoder can broadcast to?
  - id: list-live-streams
    intent: List live streams
    question: Which of my live streams are currently active?
  - id: get-live-stream
    intent: Get a live stream's details
    question: What's the stream key and status of one of my live streams?
  - id: delete-live-stream
    intent: Delete a live stream
    question: What happens to an active broadcast if I delete the live stream?
  - id: update-live-stream
    intent: Update a live stream's settings
    question: Can I change the latency mode of a stream I already created?
  phrasing_ops: 22
  slug: mux-com-live-streams-api
- baseURL: https://api.mux.com
  baseurl_source: declared
  description: Historical metrics are used for tracking KPIs, diagnosing issues, and measuring viewers' quality of experience. Metrics are calculated using the video views that have been completed and are bucketed o
  name: Mux Metrics API
  phrasing_intents:
  - id: list-breakdown-values
    intent: Break a metric down by a dimension
    question: Which countries have the worst rebuffering on my videos?
  - id: get-overall-values
    intent: Get a metric's overall value
    question: What's my overall video startup time compared to the Mux global average?
  - id: list-insights
    intent: Find what hurts a metric most
    question: Which segments of my audience are dragging down playback quality the most?
  - id: get-metric-timeseries-data
    intent: Chart a metric over time
    question: How has my rebuffer percentage trended over the past week?
  - id: list-all-metric-values
    intent: Compare all metrics for one dimension value
    question: For a single browser or country, what do all my quality metrics look like?
  phrasing_ops: 5
  slug: mux-com-metrics-api
- baseURL: https://api.mux.com
  baseurl_source: declared
  description: Analyze a video for inappropriate content.
  name: Mux Moderate API
  phrasing_intents:
  - id: create-moderate-job
    intent: Check a video for inappropriate content
    question: Can AI screen my uploaded videos for inappropriate content?
  - id: get-moderate-job
    intent: Get a moderation job's results
    question: Did the moderation job flag anything in my video?
  phrasing_ops: 2
  slug: mux-com-moderate-api
- baseURL: https://api.mux.com
  baseurl_source: declared
  description: Monitoring metrics are used for operational monitoring of a video platform. The metrics are aggregated in five second intervals, across the views that are currently being watched. The real-time metric
  name: Mux Monitoring API
  phrasing_intents:
  - id: list-monitoring-dimensions
    intent: List live monitoring dimensions
    question: What dimensions can I break live monitoring data down by?
  - id: list-monitoring-metrics
    intent: List live monitoring metrics
    question: Which metrics can I watch in real time while people are viewing?
  - id: get-monitoring-breakdown
    intent: Get a live breakdown of a monitoring metric
    question: Right now, which CDN or region has the most concurrent viewers struggling?
  - id: get-monitoring-breakdown-timeseries
    intent: Chart a live breakdown over time
    question: How has each dimension value's live metric changed over the last few minutes?
  - id: get-monitoring-histogram-timeseries
    intent: Get a live histogram timeseries for a metric
    question: Can I see the live distribution of a monitoring metric as a histogram over time?
  - id: get-monitoring-timeseries
    intent: Get a live metric timeseries with concurrent viewers
    question: How many people are watching right now and how is the metric trending?
  phrasing_ops: 6
  slug: mux-com-monitoring-api
- baseURL: https://api.mux.com
  baseurl_source: declared
  description: Operations related to the manipulation of playback IDs, through which users are able to stream videos and live streams from Mux.
  name: Mux Playback ID API
  phrasing_intents:
  - id: get-asset-or-livestream-id
    intent: Find the asset or live stream behind a playback ID
    question: Which asset or live stream does this playback ID belong to?
  phrasing_ops: 1
  slug: mux-com-playback-id-api
- baseURL: https://api.mux.com
  baseurl_source: declared
  description: Playback Restrictions allows you to set additional rules for playing videos. You can set the domains/hostnames allowed to play your videos. For instance, viewers can play videos embedded on the `https
  name: Mux Playback Restrictions API
  phrasing_intents:
  - id: create-playback-restriction
    intent: Create a playback restriction
    question: How do I stop other websites from embedding my videos?
  - id: list-playback-restrictions
    intent: List playback restrictions
    question: Which playback restrictions have I set up?
  - id: delete-playback-restriction
    intent: Delete a playback restriction
    question: How do I remove a playback restriction I no longer need?
  - id: get-playback-restriction
    intent: Get a playback restriction
    question: Which domains does a given playback restriction allow?
  - id: update-referrer-domain-restriction
    intent: Change allowed referrer domains
    question: How do I update which domains are allowed to play my videos?
  - id: update-user-agent-restriction
    intent: Change user agent playback rules
    question: Can I block playback from high-risk user agents?
  phrasing_ops: 6
  slug: mux-com-playback-restrictions-api
- baseURL: https://api.mux.com
  baseurl_source: declared
  description: Signing keys are used to sign JSON Web Tokens (JWTs) for securing certain requests, such as secure playback URLs and access to real-time viewer counts in Mux Data. **One signing key can be used to sig
  name: Mux Signing Keys API
  phrasing_intents:
  - id: create-signing-key
    intent: Create a signing key
    question: How do I get a key pair for signing secure playback tokens?
  - id: list-signing-keys
    intent: List signing keys
    question: Which signing keys exist for signing my playback JWTs?
  - id: get-signing-key
    intent: Get a signing key
    question: When was a particular signing key created?
  - id: delete-signing-key
    intent: Delete a signing key
    question: What happens to tokens signed with a key after I delete it?
  phrasing_ops: 4
  slug: mux-com-signing-keys-api
- baseURL: https://api.mux.com
  baseurl_source: declared
  description: APIs for retrieving storyboards, sprites, and metadata about the storyboards from videos hosted using Mux.
  name: Mux Storyboards API
  phrasing_intents:
  - id: get-image-storyboard
    intent: Get a storyboard image for hover previews
    question: How do I show thumbnail previews when viewers hover over the video timeline?
  - id: get-vtt-storyboard
    intent: Get storyboard tile coordinates as WebVTT
    question: Where do I get the WebVTT file mapping storyboard tiles to timestamps?
  - id: get-json-storyboard
    intent: Get storyboard tile coordinates as JSON
    question: Can I get storyboard thumbnail positions and time ranges as JSON?
  phrasing_ops: 3
  slug: mux-com-storyboards-api
- baseURL: https://api.mux.com
  baseurl_source: declared
  description: APIs for streaming video content via HLS and MP4 with customizable playback options.
  name: Mux Streaming API
  phrasing_intents:
  - id: get-hls-manifest
    intent: Get the HLS playlist for a video
    question: How do I get the .m3u8 stream URL to play a Mux video?
  - id: get-static-rendition
    intent: Download a static MP4 or M4A rendition
    question: How do I download an MP4 file of my video?
  phrasing_ops: 2
  slug: mux-com-streaming-api
- baseURL: https://api.mux.com
  baseurl_source: declared
  description: Generate a title, description, and tags for a video.
  name: Mux Summarize API
  phrasing_intents:
  - id: create-summarize-job
    intent: Generate a title, description and tags with AI
    question: Can AI write a title and description for my video?
  - id: get-summarize-job
    intent: Get the result of a summarize job
    question: Where do I read the AI-generated title and tags for my video?
  phrasing_ops: 2
  slug: mux-com-summarize-api
- baseURL: https://api.mux.com
  baseurl_source: declared
  description: APIs for retrieving still thumbnails from videos hosted using Mux.
  name: Mux Thumbnails API
  phrasing_intents:
  - id: get-thumbnail
    intent: Get a thumbnail image from a video
    question: How do I grab a still frame from my video at a specific second?
  phrasing_ops: 1
  slug: mux-com-thumbnails-api
- baseURL: https://api.mux.com
  baseurl_source: declared
  description: Transcription Vocabularies allows you to provide collections of phrases like proper nouns, technical jargon, and uncommon words as part of captioning workflows. When using Auto-Generated Captions, Tra
  name: Mux Transcription Vocabularies API
  phrasing_intents:
  - id: create-transcription-vocabulary
    intent: Create a custom transcription vocabulary
    question: How do I teach auto-captions brand names and jargon they keep getting wrong?
  - id: list-transcription-vocabularies
    intent: List transcription vocabularies
    question: Which custom transcription vocabularies have I created?
  - id: get-transcription-vocabulary
    intent: Get a transcription vocabulary
    question: What phrases are in one of my transcription vocabularies?
  - id: delete-transcription-vocabulary
    intent: Delete a transcription vocabulary
    question: What happens to live streams using a vocabulary when I delete it?
  - id: update-transcription-vocabulary
    intent: Update a transcription vocabulary's phrases
    question: Can I change a vocabulary while a live stream is using it?
  phrasing_ops: 5
  slug: mux-com-transcription-vocabularies-api
- baseURL: https://api.mux.com
  baseurl_source: declared
  description: Translate captions from one language to another.
  name: Mux Translate Captions API
  phrasing_intents:
  - id: create-translate-captions-job
    intent: Translate a video's captions to another language
    question: Can I translate my English captions into Spanish automatically?
  - id: get-translate-captions-job
    intent: Get the result of a caption translation job
    question: Is my caption translation finished?
  phrasing_ops: 2
  slug: mux-com-translate-captions-api
- baseURL: https://api.mux.com
  baseurl_source: declared
  description: 'A URL signing key is used as the secret when signing any Mux URL. Mux requires a [JSON Web Token](https://jwt.io/) as the value of the token query parameter. The token query parameter must be set for '
  name: Mux URL Signing Keys API
  phrasing_intents:
  - id: create-url-signing-key
    intent: Create a URL signing key (deprecated)
    question: Does the deprecated video signing-keys route still create key pairs?
  - id: list-url-signing-keys
    intent: List URL signing keys (deprecated)
    question: Can I still list keys through the older video URL signing keys route?
  - id: get-url-signing-key
    intent: Get a URL signing key (deprecated)
    question: Can I look up a key through the old video URL signing keys route?
  - id: delete-url-signing-key
    intent: Delete a URL signing key (deprecated)
    question: Will deleting a legacy URL signing key break my existing signed URLs?
  phrasing_ops: 4
  slug: mux-com-url-signing-keys-api
- baseURL: https://api.mux.com
  baseurl_source: declared
  description: Collection of utility methods for using Mux APIs. There's only one thing in here right now, maybe there will be more later.
  name: Mux Utilities API
  phrasing_intents:
  - id: get-whoami
    intent: Check which account an access token belongs to
    question: Which organization and environment is my access token for?
  phrasing_ops: 1
  slug: mux-com-utilities-api
- baseURL: https://api.mux.com
  baseurl_source: declared
  description: An individual video view tracked by Mux Data. For the full list of properties for each view please refer to the table of data fields in the [Export raw video view data guide](https://docs.mux.com/guid
  name: Mux Video Views API
  phrasing_intents:
  - id: list-video-views
    intent: List individual video views
    question: Can I see every view a particular viewer had?
  - id: get-video-view
    intent: Get the details of one video view
    question: What happened during one specific playback session?
  phrasing_ops: 2
  slug: mux-com-video-views-api
- baseURL: https://api.mux.com
  baseurl_source: declared
  description: API for retrieving the real-time count of views and viewers based on ID as collected by Mux Data.
  name: Mux View and Viewer Counts API
  phrasing_intents:
  - id: get-engagement-counts
    intent: Get real-time view and viewer counts
    question: How many people are watching my video right now?
  phrasing_ops: 1
  slug: mux-com-view-and-viewer-counts-api
- baseURL: https://api.mux.com
  baseurl_source: declared
  description: Manage playback IDs for assets.
  name: Mux Playback IDs API
  phrasing_intents:
  - id: createPlaybackId
    intent: Create a playback ID for an asset
    question: How do I create a playback ID so an asset can be streamed?
  phrasing_ops: 1
  slug: mux-com-playback-ids-api
- baseURL: https://api.mux.com
  baseurl_source: declared
  description: The Mux API API from Mux — 0 operation(s) for mux api.
  name: Mux API
  slug: mux-com-mux-api-api
- baseURL: https://api.mux.com
  baseurl_source: declared
  description: 'The Mux Data Real-time API has been deprecated, please refer to the Mux Data `Monitoring` APIs which provide the same functionality. Mux Data Monitoring metrics are available to Mux Data customers on '
  name: Mux Realtime API
  phrasing_intents:
  - id: list-realtime-dimensions
    intent: List real-time dimensions (deprecated)
    question: Which dimensions does the deprecated real-time API expose?
  - id: list-realtime-metrics
    intent: List real-time metrics (deprecated)
    question: Which metrics does the older real-time API offer?
  - id: get-realtime-breakdown
    intent: Get a real-time breakdown (deprecated)
    question: Can I still pull a concurrent-viewer breakdown from the old real-time API?
  - id: get-realtime-histogram-timeseries
    intent: Get a real-time histogram timeseries (deprecated)
    question: Is the older real-time histogram timeseries still available?
  - id: get-realtime-timeseries
    intent: Get a real-time timeseries (deprecated)
    question: Can the deprecated real-time API still give me concurrent viewers over time?
  phrasing_ops: 5
  slug: mux-com-realtime-api
arazzos:
- description: Confirm the active environment with whoami, then list per-asset delivery usage for a timeframe to audit billed delivery.
  name: Mux Account Delivery Usage Audit
  slug: mux-com-account-delivery-usage-workflow
- description: Create an asset, wait until ready, queue an AI summarize job against it, then poll the job until it completes.
  name: Mux AI Summarize Asset
  slug: mux-com-ai-summarize-asset-workflow
- description: Create a Mux Data annotation marking a deploy or event, read it back, update its note, then list annotations to confirm.
  name: Mux Manage Data Annotation
  slug: mux-com-annotation-manage-workflow
- description: Create an asset, wait until ready, attach a text caption track, then poll the track until it is ready.
  name: Mux Add Caption Track to Asset
  slug: mux-com-asset-add-caption-track-workflow
- description: Create an asset, wait until it is ready, then attach a new playback ID and confirm it resolves.
  name: Mux Add Playback ID to Asset
  slug: mux-com-asset-add-playback-id-workflow
- description: List assets in the environment, then read the first asset's full detail and its input info.
  name: Mux Asset Library Drilldown
  slug: mux-com-asset-library-drilldown-workflow
- description: Create an asset, wait until ready, request a static MP4 rendition, then poll until the rendition is ready for download.
  name: Mux Generate Downloadable Static Rendition
  slug: mux-com-asset-mp4-rendition-workflow
- description: Create an asset, wait until ready, attach title and external-id metadata, then delete it to demonstrate full lifecycle management.
  name: Mux Asset Tag and Cleanup
  slug: mux-com-asset-tag-and-cleanup-workflow
- description: Ingest a video from a hosted URL, poll the new asset until ready, and confirm the input details Mux processed.
  name: Mux Create Asset From URL
  slug: mux-com-create-asset-from-url-workflow
- description: List the available Mux Data dimensions, then enumerate the distinct values of a chosen dimension over a timeframe.
  name: Mux Dimension Exploration
  slug: mux-com-dimension-exploration-workflow
- description: Create a direct upload URL, poll the upload until Mux creates an asset, then poll the asset until it is ready to play.
  name: Mux Direct Upload to Ready Asset
  slug: mux-com-direct-upload-to-asset-workflow
- description: List the playback errors in a timeframe, then read the overall playback-failure rate so errors can be weighed against total traffic.
  name: Mux Errors Impact Analysis
  slug: mux-com-errors-impact-analysis-workflow
- description: List open Mux Data incidents, read the first incident in detail, and pull the incidents related to it.
  name: Mux Incident Drilldown
  slug: mux-com-incident-drilldown-workflow
- description: Create a live stream, add a second playback ID with a chosen policy, and confirm the playback ID resolves.
  name: Mux Add Playback ID to Live Stream
  slug: mux-com-live-stream-add-playback-id-workflow
- description: Create a live stream, enable automated speech-recognition subtitles for it, then read it back to confirm the subtitle config.
  name: Mux Live Stream Generated Subtitles
  slug: mux-com-live-stream-generated-subtitles-workflow
- description: Create a live stream, disable it, re-enable it, and signal it complete to walk the operational lifecycle.
  name: Mux Live Stream Lifecycle Control
  slug: mux-com-live-stream-lifecycle-workflow
- description: Create a live stream, read it back, add an RTMP simulcast target, and confirm the target is registered.
  name: Mux Live Stream With Simulcast Target
  slug: mux-com-live-stream-with-simulcast-workflow
- description: Read a metric's overall value for a timeframe, then break it down by a dimension to see which segments drive it.
  name: Mux Metric Breakdown Analysis
  slug: mux-com-metric-breakdown-analysis-workflow
- description: Read a metric's overall value for a timeframe, then pull its timeseries to see how the metric trended over time.
  name: Mux Metric Timeseries Trend
  slug: mux-com-metric-timeseries-trend-workflow
- description: List the available monitoring dimensions, then break a chosen monitoring metric down by a dimension at a timestamp.
  name: Mux Monitoring Metric Breakdown
  slug: mux-com-monitoring-breakdown-workflow
- description: Create a playback restriction, tighten its referrer and user-agent rules, then read it back to confirm the policy.
  name: Mux Configure Playback Restriction
  slug: mux-com-playback-restriction-setup-workflow
- description: List the available real-time metrics and dimensions, then break a chosen real-time metric down by a dimension right now.
  name: Mux Real-Time Metric Breakdown
  slug: mux-com-realtime-breakdown-workflow
- description: Create a live stream, reset its stream key, and read it back to confirm the new key is in place.
  name: Mux Rotate Live Stream Key
  slug: mux-com-reset-stream-key-workflow
- description: Create a new system-level signing key for Mux Data SDK auth, read it back, list keys, then delete the previous key.
  name: Mux Rotate System Signing Key
  slug: mux-com-system-signing-key-rotation-workflow
- description: Create a new URL signing key, read it back, list all keys, then delete the previous key to complete a rotation.
  name: Mux Rotate URL Signing Key
  slug: mux-com-url-signing-key-rotation-workflow
- description: List recent video views in a timeframe, then fetch the full detail of the first matching view.
  name: Mux Video View Drilldown
  slug: mux-com-video-view-drilldown-workflow
artifact_total: 155
collections:
- collection_type: postman
  name: Mux API
  slug: postman-mux
- collection_type: open
  name: Mux Animated Images API
  slug: open-mux-com-animated-images-api
- collection_type: open
  name: Mux Animated Images Annotations API
  slug: open-mux-com-annotations-api
- collection_type: open
  name: Mux Animated Images Ask Questions API
  slug: open-mux-com-ask-questions-api
- collection_type: open
  name: Mux Animated Images Assets API
  slug: open-mux-com-assets-api
- collection_type: open
  name: Mux Animated Images Captions and Transcripts API
  slug: open-mux-com-captions-and-transcripts-api
- collection_type: open
  name: Mux Animated Images Delivery Usage API
  slug: open-mux-com-delivery-usage-api
- collection_type: open
  name: Mux Animated Images Dimensions API
  slug: open-mux-com-dimensions-api
- collection_type: open
  name: Mux Animated Images Direct Uploads API
  slug: open-mux-com-direct-uploads-api
- collection_type: open
  name: Mux Animated Images DRM Configurations API
  slug: open-mux-com-drm-configurations-api
- collection_type: open
  name: Mux Animated Images Edit Captions API
  slug: open-mux-com-edit-captions-api
- collection_type: open
  name: Mux Animated Images Errors API
  slug: open-mux-com-errors-api
- collection_type: open
  name: Mux Animated Images Exports API
  slug: open-mux-com-exports-api
- collection_type: open
  name: Mux Animated Images Filters API
  slug: open-mux-com-filters-api
- collection_type: open
  name: Mux Animated Images Find Key Moments API
  slug: open-mux-com-find-key-moments-api
- collection_type: open
  name: Mux Animated Images Generate Chapters API
  slug: open-mux-com-generate-chapters-api
- collection_type: open
  name: Mux Animated Images Incidents API
  slug: open-mux-com-incidents-api
- collection_type: open
  name: Mux Animated Images Jobs API
  slug: open-mux-com-jobs-api
- collection_type: open
  name: Mux Animated Images Live Streams API
  slug: open-mux-com-live-streams-api
- collection_type: open
  name: Mux Animated Images Metrics API
  slug: open-mux-com-metrics-api
- collection_type: open
  name: Mux Animated Images Moderate API
  slug: open-mux-com-moderate-api
- collection_type: open
  name: Mux Animated Images Monitoring API
  slug: open-mux-com-monitoring-api
- collection_type: open
  name: Mux Animated Images Playback ID API
  slug: open-mux-com-playback-id-api
- collection_type: open
  name: Mux Video Assets Playback IDs API
  slug: open-mux-com-playback-ids-api
- collection_type: open
  name: Mux Animated Images Playback Restrictions API
  slug: open-mux-com-playback-restrictions-api
- collection_type: open
  name: Mux Animated Images Real-Time API
  slug: open-mux-com-real-time-api
- collection_type: open
  name: Mux Animated Images Signing Keys API
  slug: open-mux-com-signing-keys-api
- collection_type: open
  name: Mux Animated Images Storyboards API
  slug: open-mux-com-storyboards-api
- collection_type: open
  name: Mux Animated Images Streaming API
  slug: open-mux-com-streaming-api
- collection_type: open
  name: Mux Animated Images Summarize API
  slug: open-mux-com-summarize-api
- collection_type: open
  name: Mux Animated Images Thumbnails API
  slug: open-mux-com-thumbnails-api
- collection_type: open
  name: Mux Animated Images Transcription Vocabularies API
  slug: open-mux-com-transcription-vocabularies-api
- collection_type: open
  name: Mux Animated Images Translate Captions API
  slug: open-mux-com-translate-captions-api
- collection_type: open
  name: Mux Animated Images URL Signing Keys API
  slug: open-mux-com-url-signing-keys-api
- collection_type: open
  name: Mux Animated Images Utilities API
  slug: open-mux-com-utilities-api
- collection_type: open
  name: Mux Animated Images Video Views API
  slug: open-mux-com-video-views-api
- collection_type: open
  name: Mux Animated Images View and Viewer Counts API
  slug: open-mux-com-view-and-viewer-counts-api
- collection_type: open
  name: Mux API
  slug: open-mux
common:
- group: other
  href: https://artifacts.apis.io/mux-com/capabilities/mux-com-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/mux-com-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/mux-com/agentic-access/mux-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/mux-com-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/mux-com/security/mux-com-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/mux-com-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/mux-com/security/mux-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/mux-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/mux-com/security/mux-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/mux-com-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/mux-com/authentication/mux-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/mux-com-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/mux/overview
- group: design
  href: https://artifacts.apis.io/mux-com/arazzo/mux-com-account-delivery-usage-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/mux-com-account-delivery-usage-workflow.yml
- group: design
  href: https://artifacts.apis.io/mux-com/arazzo/mux-com-ai-summarize-asset-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/mux-com-ai-summarize-asset-workflow.yml
- group: design
  href: https://artifacts.apis.io/mux-com/arazzo/mux-com-annotation-manage-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/mux-com-annotation-manage-workflow.yml
- group: design
  href: https://artifacts.apis.io/mux-com/arazzo/mux-com-asset-add-caption-track-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/mux-com-asset-add-caption-track-workflow.yml
- group: design
  href: https://artifacts.apis.io/mux-com/arazzo/mux-com-asset-add-playback-id-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/mux-com-asset-add-playback-id-workflow.yml
- group: design
  href: https://artifacts.apis.io/mux-com/arazzo/mux-com-asset-library-drilldown-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/mux-com-asset-library-drilldown-workflow.yml
- group: design
  href: https://artifacts.apis.io/mux-com/arazzo/mux-com-asset-mp4-rendition-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/mux-com-asset-mp4-rendition-workflow.yml
- group: design
  href: https://artifacts.apis.io/mux-com/arazzo/mux-com-asset-tag-and-cleanup-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/mux-com-asset-tag-and-cleanup-workflow.yml
- group: design
  href: https://artifacts.apis.io/mux-com/arazzo/mux-com-create-asset-from-url-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/mux-com-create-asset-from-url-workflow.yml
- group: design
  href: https://artifacts.apis.io/mux-com/arazzo/mux-com-dimension-exploration-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/mux-com-dimension-exploration-workflow.yml
- group: design
  href: https://artifacts.apis.io/mux-com/arazzo/mux-com-direct-upload-to-asset-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/mux-com-direct-upload-to-asset-workflow.yml
- group: design
  href: https://artifacts.apis.io/mux-com/arazzo/mux-com-errors-impact-analysis-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/mux-com-errors-impact-analysis-workflow.yml
- group: design
  href: https://artifacts.apis.io/mux-com/arazzo/mux-com-incident-drilldown-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/mux-com-incident-drilldown-workflow.yml
- group: design
  href: https://artifacts.apis.io/mux-com/arazzo/mux-com-live-stream-add-playback-id-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/mux-com-live-stream-add-playback-id-workflow.yml
- group: design
  href: https://artifacts.apis.io/mux-com/arazzo/mux-com-live-stream-generated-subtitles-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/mux-com-live-stream-generated-subtitles-workflow.yml
- group: design
  href: https://artifacts.apis.io/mux-com/arazzo/mux-com-live-stream-lifecycle-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/mux-com-live-stream-lifecycle-workflow.yml
- group: design
  href: https://artifacts.apis.io/mux-com/arazzo/mux-com-live-stream-with-simulcast-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/mux-com-live-stream-with-simulcast-workflow.yml
- group: design
  href: https://artifacts.apis.io/mux-com/arazzo/mux-com-metric-breakdown-analysis-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/mux-com-metric-breakdown-analysis-workflow.yml
- group: design
  href: https://artifacts.apis.io/mux-com/arazzo/mux-com-metric-timeseries-trend-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/mux-com-metric-timeseries-trend-workflow.yml
- group: design
  href: https://artifacts.apis.io/mux-com/arazzo/mux-com-monitoring-breakdown-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/mux-com-monitoring-breakdown-workflow.yml
- group: design
  href: https://artifacts.apis.io/mux-com/arazzo/mux-com-playback-restriction-setup-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/mux-com-playback-restriction-setup-workflow.yml
- group: design
  href: https://artifacts.apis.io/mux-com/arazzo/mux-com-realtime-breakdown-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/mux-com-realtime-breakdown-workflow.yml
- group: design
  href: https://artifacts.apis.io/mux-com/arazzo/mux-com-reset-stream-key-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/mux-com-reset-stream-key-workflow.yml
- group: design
  href: https://artifacts.apis.io/mux-com/arazzo/mux-com-system-signing-key-rotation-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/mux-com-system-signing-key-rotation-workflow.yml
- group: design
  href: https://artifacts.apis.io/mux-com/arazzo/mux-com-url-signing-key-rotation-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/mux-com-url-signing-key-rotation-workflow.yml
- group: design
  href: https://artifacts.apis.io/mux-com/arazzo/mux-com-video-view-drilldown-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/mux-com-video-view-drilldown-workflow.yml
- group: company
  title: ''
  type: Website
  url: https://www.mux.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.mux.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://www.mux.com/docs/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://www.mux.com/docs/core/make-your-first-api-request
- group: auth
  title: ''
  type: Authentication
  url: https://www.mux.com/docs/guides/signing-jwts
- group: start
  title: ''
  type: Console
  url: https://dashboard.mux.com/
- group: start
  title: ''
  type: Signup
  url: https://dashboard.mux.com/signup
- group: commercial
  title: ''
  type: Pricing
  url: https://www.mux.com/pricing/video
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.mux.com/docs/changelog
- group: company
  title: ''
  type: Blog
  url: https://www.mux.com/blog
- group: operate
  title: ''
  type: StatusPage
  url: https://status.mux.com/
- group: operate
  title: ''
  type: Support
  url: https://www.mux.com/support
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.mux.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.mux.com/privacy
- group: auth
  title: ''
  type: Security
  url: https://www.mux.com/security
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/muxinc
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/mux/
- group: company
  title: ''
  type: X-Twitter
  url: https://x.com/MuxHQ
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@MuxHQ
- group: build
  title: ''
  type: SDKs
  url: https://github.com/muxinc/mux-node-sdk
- group: build
  title: ''
  type: SDKs
  url: https://github.com/muxinc/mux-python
- group: build
  title: ''
  type: SDKs
  url: https://github.com/muxinc/mux-ruby
- group: build
  title: ''
  type: SDKs
  url: https://github.com/muxinc/mux-php
- group: build
  title: ''
  type: SDKs
  url: https://github.com/muxinc/mux-go
- group: build
  title: ''
  type: SDKs
  url: https://github.com/muxinc/mux-elixir
- group: build
  title: ''
  type: CLI
  url: https://github.com/muxinc/cli
- group: build
  title: ''
  type: SDKs
  url: https://github.com/muxinc/upchunk
- group: build
  title: ''
  type: SDKs
  url: https://github.com/muxinc/elements
- group: build
  title: ''
  type: SDKs
  url: https://github.com/muxinc/media-chrome
- group: build
  title: ''
  type: SDKs
  url: https://github.com/muxinc/next-video
- group: build
  title: ''
  type: SDKs
  url: https://github.com/muxinc/mux-stats-sdk-avplayer
- group: build
  title: ''
  type: SDKs
  url: https://github.com/muxinc/mux-stats-sdk-exoplayer
- group: build
  title: ''
  type: SDKs
  url: https://github.com/muxinc/swift-upload-sdk
- group: build
  title: ''
  type: SDKs
  url: https://github.com/muxinc/mux-player-swift
- group: design
  href: https://artifacts.apis.io/mux-com/rules/mux-com-rules.yml
  title: ''
  type: Rules
  url: rules/mux-com-rules.yml
- group: design
  href: https://artifacts.apis.io/mux-com/json-ld/mux-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/mux-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/mux-com/vocabulary/mux-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/mux-com-vocabulary.yml
- group: commercial
  href: https://artifacts.apis.io/mux-com/plans/mux-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/mux-com-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/mux-com/rate-limits/mux-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/mux-com-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/mux-com/finops/mux-com-finops.yml
  title: ''
  type: FinOps
  url: finops/mux-com-finops.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://www.mux.com/llms.txt
- group: docs
  title: ''
  type: OpenAPI
  url: https://www.mux.com/api-spec.json
created: '2026-05-25'
description: Mux is a video infrastructure platform that gives developers an end-to-end API for ingesting, encoding, storing, delivering, and analyzing video. The platform spans Mux Video (on-demand and live streaming), Mux Data (quality-of-experience analytics), Mux Robots (AI workflows for captions, chapters, summarization, and moderation), and Mux Player (drop-in playback components). Mux exposes a unified REST API at api.mux.com plus delivery hosts at stream.mux.com, image.mux.com, and stats.mux.com, backed by official SDKs in Node, Python, Ruby, PHP, Go, and Elixir, a CLI, and player integrations across web, iOS, Android, Roku, and major HTML5 players.
features:
- description: Adaptive bitrate encoding with smart per-title settings and average playback-ready times under 2 seconds.
  name: Video Encoding
- description: Resumable chunked PUT uploads via UpChunk that bypass the application server.
  name: Direct Uploads
- description: Managed RTMP and SRT (with HEVC) ingest with 4-second standard latency and reduced-latency mode.
  name: Live Streaming
- description: Restream a single live broadcast to YouTube, Twitch, Facebook, and other RTMP destinations.
  name: Simulcast Targets
- description: Drop-in HTML5 player available as React component, web component, and iframe embed.
  name: Mux Player
- description: Real-time and on-demand caption generation across multiple languages with Transcription Vocabularies for domain terms.
  name: Auto-Generated Captions
- description: Quality-of-experience analytics covering views, rebuffering, startup time, exits before video starts, and player errors.
  name: Mux Data Analytics
- description: Live concurrent viewer counts and stream health monitoring for live broadcasts.
  name: Real-Time Metrics
- description: Asynchronous AI jobs for summarization, chaptering, key-moment detection, captions translation, content moderation, and video Q&A.
  name: Mux Robots AI
- description: JWT-signed playback URLs and Media-grade DRM (Widevine, FairPlay, PlayReady) at $100/month plus $0.003/play.
  name: Signed Playback and DRM
- description: Domain, geo, and user-agent restriction policies enforced at the manifest layer.
  name: Playback Restrictions
- description: On-the-fly JPG/PNG/WebP thumbnails, animated GIFs, and VTT storyboards via image.mux.com.
  name: Thumbnails and Storyboards
- description: HMAC-SHA256 signed webhook events covering asset, upload, live stream, and robots job lifecycle.
  name: Webhooks
- description: 100K free monthly delivery minutes and up to 10 stored videos with no credit card required.
  name: Self-Serve Free Tier
finops:
- has_sources: true
  method: derived
  name: Mux Com Finops
  primary_unit: minute
  service_category: ''
  slug: mux-com-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mux-com.png
integrations:
- description: First-party next-video package for adding video components to Next.js apps.
  name: Next.js
- description: Mux Player and Mux Elements React components for embedding playback.
  name: React
- description: Astro framework integration documented in Mux guides.
  name: Astro
- description: WordPress plugin for embedding Mux video in posts and pages.
  name: WordPress
- description: PHP SDK and Laravel guides for Mux Video integration.
  name: Laravel
- description: Flutter integration for playing Mux video in mobile apps.
  name: Flutter
- description: roku-mux SDK for Mux Data analytics on the Roku platform.
  name: Roku
- description: chromecast-mux SDK for measuring playback on Google Cast receivers.
  name: Chromecast
- description: mux-stats-sdk-exoplayer for Mux Data analytics on Android.
  name: ExoPlayer
- description: mux-stats-sdk-avplayer for iOS, tvOS, and visionOS analytics.
  name: AVPlayer
- description: Mux Data SDKs for JWPlayer on iOS and web.
  name: JWPlayer
- description: Mux Data SDKs for THEOplayer on iOS and Android.
  name: THEOplayer
- description: Mux Data analytics SDK for the Video.js HTML5 player.
  name: Video.js
- description: Use Mux delivery behind Cloudflare for edge caching and access controls.
  name: Cloudflare
- description: No-code workflow automation via Zapier connectors.
  name: Zapier
jsonld:
- class_count: 45
  name: Mux Com Context
  property_count: 4
  slug: mux-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.mux.com over HTTP; 2 tools listed.
  name: Mux MCP Server
  slug: mux-com
modified: '2026-09-16'
name: Mux
nav: Providers
network: true
overview: 'Mux publishes 38 API contracts indexed on the [APIs.io](https://apis.io/) network, including Animated Images API, Annotations API, Ask Questions API, and 35 more. Tagged areas include Video Infrastructure, Video Streaming, Live Streaming, Video Analytics, and Video AI.


  The Mux catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Mux''s developer surface includes authentication, documentation, API reference, getting-started guide, developer console, signup flow, pricing, and 68 more developer resources.'
plans:
- name: Mux Com Plans Pricing
  plan_count: 11
  slug: mux-com-plans-pricing
- name: Mux Com Price Estimates
  plan_count: 0
  slug: mux-com-price-estimates
random_paper: 14
rate_limits:
- limit_count: 5
  name: Mux Com Rate Limits
  slug: mux-com-rate-limits
rules:
- authorship: unmarked
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: Mux API Rules
  rule_count: 9
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 9
  slug: mux-com-rules
score:
  band: exemplar
  composite: 72.2
  coverage:
    artifact_dirs: 23
    catalog_earned: 71.3
    catalog_earned_first_party: 12.0
    catalog_gap: 43.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 92.1
    contract_governance: 25.0
    contract_quality: 60.1
    developer_ergonomics: 79.8
    discoverability: 75.0
    operational_transparency: 55.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 72.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 37
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 35.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 27.8
screenshot: https://apis.io/screenshots/mux-com/mux-com-2026-08-07T184502.png
security:
- kind: authentication
  name: Mux Com Authentication
  slug: mux-com-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Mux Com Domain Security
  slug: mux-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Mux Com Vulnerability Disclosure
  slug: mux-com-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Mux Com Trust Center
  slug: mux-com-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, PCI DSS, HIPAA, FedRAMP, GDPR, CSA STAR
slug: mux-com
solutions:
- description: 100K monthly delivery minutes, up to 10 stored videos, on-demand only, no credit card.
  name: Free Plan
- description: Usage-based billing with $20 monthly credit, unlimited storage, on-demand and live, Robots access.
  name: Pay As You Go
- description: $20/month for $100 in monthly credits.
  name: Launch (Pre-pay)
- description: $500/month for $1,000 in monthly credits.
  name: Scale (Pre-pay)
- description: Volume discounts above $3k/month, account security, SLAs, 24/7 support, custom pricing.
  name: Enterprise
tags:
- Video Infrastructure
- Video Streaming
- Live Streaming
- Video Analytics
- Video AI
- Encoding
use_cases:
- description: Power video upload, transcoding, and playback for social, community, and creator apps.
  name: User-Generated Content Platforms
- description: Host and deliver outputs from generative video models with analytics on viewer behavior.
  name: AI Video Generation Platforms
- description: Ingest concerts, sports, gaming streams, and conferences via RTMP/SRT with simulcasting.
  name: Live Events and Broadcast
- description: Embed product, demo, and shoppable video into storefronts with low-latency live shopping.
  name: E-Commerce Video
- description: Course platforms and LMS providers using on-demand and live with captions and chapters.
  name: Education and Training
- description: Internal town halls, webinars, and corporate communications with DRM and access controls.
  name: Enterprise Communications
- description: News organizations and publishers delivering editorial video with quality analytics.
  name: Media and Publishing
website: https://www.mux.com/
---
