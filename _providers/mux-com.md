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
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.6
  scored_at: '2026-09-01'
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
- description: APIs for retrieving animated images from videos hosted using Mux.
  name: Mux Animated Images API
  slug: mux-com-animated-images-api
- description: Annotations allow you to add notes at a specific datetime to view in the Mux Data dashboard.
  name: Mux Annotations API
  slug: mux-com-annotations-api
- description: Ask questions about a video and get structured answers.
  name: Mux Ask Questions API
  slug: mux-com-ask-questions-api
- description: An asset refers to a piece of media content that is stored or is being live streamed through the Mux system. An asset always has a duration and one or more tracks (audio, video, and text data). The me
  name: Mux Assets API
  slug: mux-com-assets-api
- description: APIs for retrieving captions and transcripts from videos hosted using Mux that have had captions generated automatically.
  name: Mux Captions and Transcripts API
  slug: mux-com-captions-and-transcripts-api
- description: The Delivery Usage API allows you to get delivery/streaming usage details for each asset and across all assets. Delivery usage details are aggregated every hour at the top of the hour and can be reque
  name: Mux Delivery Usage API
  slug: mux-com-delivery-usage-api
- description: Dimensions are the types of metadata that can be collected for a video view. Some dimensions are collected automatically based on the playback or device, such as the viewer's Country or the device inf
  name: Mux Dimensions API
  slug: mux-com-dimensions-api
- description: Direct upload allows you to push assets directly to Mux storage instead of needing to go through your own first. When you create a new direct upload, we'll give you back a signed URL for a Google Clou
  name: Mux Direct Uploads API
  slug: mux-com-direct-uploads-api
- description: DRM Configurations allow you to adjust the security level of content delivered through Mux Video's Digital Rights Management (DRM) feature.
  name: Mux DRM Configurations API
  slug: mux-com-drm-configurations-api
- description: Edit an existing caption track with find-and-replace edits and optional profanity censoring. This workflow is currently in beta.
  name: Mux Edit Captions API
  slug: mux-com-edit-captions-api
- description: Playback errors are tracked and aggregated by Mux Data. Errors can be listed by the API, which contains data about the error code, message, and how often the error occurred.
  name: Mux Errors API
  slug: mux-com-errors-api
- description: Exports allow you to download the daily CSV files that are generated from the video views that occurred in the previous day. Please contact [support](mailto:support@mux.com) for information about enab
  name: Mux Exports API
  slug: mux-com-exports-api
- description: Deprecated, please refer to the Dimensions APIs.
  name: Mux Filters API
  slug: mux-com-filters-api
- description: Identify key moments in a video.
  name: Mux Find Key Moments API
  slug: mux-com-find-key-moments-api
- description: Generate chapters for a video.
  name: Mux Generate Chapters API
  slug: mux-com-generate-chapters-api
- description: Incidents occur when an anomaly alert is triggered in Mux Data. The Incidents API provides operations related to the raising and managing of alerting incidents.
  name: Mux Incidents API
  slug: mux-com-incidents-api
- description: List and cancel jobs across all workflows.
  name: Mux Jobs API
  slug: mux-com-jobs-api
- description: A Live Stream represents a unique live stream of video being pushed to Mux. It includes configuration details (a Stream Key) for live broadcasting software/hardware and a Playback ID for playing the s
  name: Mux Live Streams API
  slug: mux-com-live-streams-api
- description: Historical metrics are used for tracking KPIs, diagnosing issues, and measuring viewers' quality of experience. Metrics are calculated using the video views that have been completed and are bucketed o
  name: Mux Metrics API
  slug: mux-com-metrics-api
- description: Analyze a video for inappropriate content.
  name: Mux Moderate API
  slug: mux-com-moderate-api
- description: Monitoring metrics are used for operational monitoring of a video platform. The metrics are aggregated in five second intervals, across the views that are currently being watched. The real-time metric
  name: Mux Monitoring API
  slug: mux-com-monitoring-api
- description: Operations related to the manipulation of playback IDs, through which users are able to stream videos and live streams from Mux.
  name: Mux Playback ID API
  slug: mux-com-playback-id-api
- description: Playback Restrictions allows you to set additional rules for playing videos. You can set the domains/hostnames allowed to play your videos. For instance, viewers can play videos embedded on the `https
  name: Mux Playback Restrictions API
  slug: mux-com-playback-restrictions-api
- description: 'The Mux Data Real-time API has been deprecated, please refer to the Mux Data `Monitoring` APIs which provide the same functionality. Mux Data Monitoring metrics are available to Mux Data customers on '
  name: Mux Real-Time API
  slug: mux-com-real-time-api
- description: Signing keys are used to sign JSON Web Tokens (JWTs) for securing certain requests, such as secure playback URLs and access to real-time viewer counts in Mux Data. **One signing key can be used to sig
  name: Mux Signing Keys API
  slug: mux-com-signing-keys-api
- description: APIs for retrieving storyboards, sprites, and metadata about the storyboards from videos hosted using Mux.
  name: Mux Storyboards API
  slug: mux-com-storyboards-api
- description: APIs for streaming video content via HLS and MP4 with customizable playback options.
  name: Mux Streaming API
  slug: mux-com-streaming-api
- description: Generate a title, description, and tags for a video.
  name: Mux Summarize API
  slug: mux-com-summarize-api
- description: APIs for retrieving still thumbnails from videos hosted using Mux.
  name: Mux Thumbnails API
  slug: mux-com-thumbnails-api
- description: Transcription Vocabularies allows you to provide collections of phrases like proper nouns, technical jargon, and uncommon words as part of captioning workflows. When using Auto-Generated Captions, Tra
  name: Mux Transcription Vocabularies API
  slug: mux-com-transcription-vocabularies-api
- description: Translate captions from one language to another.
  name: Mux Translate Captions API
  slug: mux-com-translate-captions-api
- description: 'A URL signing key is used as the secret when signing any Mux URL. Mux requires a [JSON Web Token](https://jwt.io/) as the value of the token query parameter. The token query parameter must be set for '
  name: Mux URL Signing Keys API
  slug: mux-com-url-signing-keys-api
- description: Collection of utility methods for using Mux APIs. There's only one thing in here right now, maybe there will be more later.
  name: Mux Utilities API
  slug: mux-com-utilities-api
- description: An individual video view tracked by Mux Data. For the full list of properties for each view please refer to the table of data fields in the [Export raw video view data guide](https://docs.mux.com/guid
  name: Mux Video Views API
  slug: mux-com-video-views-api
- description: API for retrieving the real-time count of views and viewers based on ID as collected by Mux Data.
  name: Mux View and Viewer Counts API
  slug: mux-com-view-and-viewer-counts-api
- description: Manage playback IDs for assets.
  name: Mux Playback IDs API
  slug: mux-com-playback-ids-api
- description: The Mux API API from Mux — 0 operation(s) for mux api.
  name: Mux Mux API
  slug: mux-com-mux-api-api
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
  name: API Collection
  slug: open-.refine-report
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
  title: ''
  type: CapabilityMap
  url: capabilities/mux-com-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/mux-com-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/mux-com-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/mux-com-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mux-com-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/mux-com-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/mux/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/mux-com-account-delivery-usage-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/mux-com-ai-summarize-asset-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/mux-com-annotation-manage-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/mux-com-asset-add-caption-track-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/mux-com-asset-add-playback-id-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/mux-com-asset-library-drilldown-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/mux-com-asset-mp4-rendition-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/mux-com-asset-tag-and-cleanup-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/mux-com-create-asset-from-url-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/mux-com-dimension-exploration-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/mux-com-direct-upload-to-asset-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/mux-com-errors-impact-analysis-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/mux-com-incident-drilldown-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/mux-com-live-stream-add-playback-id-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/mux-com-live-stream-generated-subtitles-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/mux-com-live-stream-lifecycle-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/mux-com-live-stream-with-simulcast-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/mux-com-metric-breakdown-analysis-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/mux-com-metric-timeseries-trend-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/mux-com-monitoring-breakdown-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/mux-com-playback-restriction-setup-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/mux-com-realtime-breakdown-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/mux-com-reset-stream-key-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/mux-com-system-signing-key-rotation-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/mux-com-url-signing-key-rotation-workflow.yml
- group: design
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
  title: ''
  type: Rules
  url: rules/mux-com-rules.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/mux-com-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/mux-com-vocabulary.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/mux-com-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/mux-com-rate-limits.yml
- group: commercial
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
- name: Mux Com Finops
  service_category: Video Infrastructure
  slug: mux-com-finops
graphqls:
- description: Mux does not currently offer a public GraphQL API. All Mux Video and Mux Data operations are available exclusively through the Mux REST API, served from `https://api.mux.com` and authenticated via HTT
  name: Mux GraphQL
  slug: mux-com-graphql
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
modified: '2026-08-08'
name: Mux
nav: Providers
network: true
overview: 'Mux publishes 37 APIs on the [APIs.io](https://apis.io/) network, including Animated Images API, Annotations API, Ask Questions API, and 34 more. Tagged areas include Video Infrastructure, Video Streaming, Live Streaming, Video Analytics, and Video AI.


  The Mux catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Mux''s developer surface includes authentication, documentation, API reference, getting-started guide, developer console, signup flow, pricing, and 68 more developer resources.'
plans:
- name: Mux Com Plans Pricing
  plan_count: 11
  slug: mux-com-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 5
  name: Mux Com Rate Limits
  slug: mux-com-rate-limits
rules:
- effective_rule_count: 50
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
  composite: 76.4
  coverage:
    artifact_dirs: 18
    catalog_gap: 26.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 92.1
    commercial_clarity: 92.1
    contract_governance: 60.6
    contract_quality: 67.1
    developer_ergonomics: 83.3
    discoverability: 70.4
    governance: 60.6
    operational_transparency: 78.9
  previous_composite: 76.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 36
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mux-com/refs/heads/main/screenshots/mux-com-2026-08-07T184502.png
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
