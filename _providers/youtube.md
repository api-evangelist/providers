---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 50.5
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 55
  human_in_the_loop: 0
  name: Youtube Agentic Access
  operation_count: 91
  slug: youtube-agentic-access
  summary_line: 91 operations · 55 acting
api_count: 36
apis:
- description: Manages sections that a channel has chosen to feature on its channel page, including inserting, updating, and deleting channel sections.
  name: Youtube Channel Sections API
  slug: youtube-channel-sections-api
- description: Enables uploading a new banner image to a YouTube channel, returning the URL that identifies the uploaded image for use with the channels.update method.
  name: Youtube Channel Banners API
  slug: youtube-channel-banners-api
- description: Provides access to channel membership data, allowing channel owners to retrieve a list of paying members who support the channel in exchange for exclusive benefits.
  name: Youtube Members API
  slug: youtube-members-api
- description: Provides information about membership pricing tiers that a channel has set up, allowing retrieval of the levels that members can subscribe to.
  name: Youtube Memberships Levels API
  slug: youtube-memberships-levels-api
- description: Manages custom video thumbnail images, enabling upload of a custom thumbnail image for a video that the authenticated user owns.
  name: Youtube Thumbnails API
  slug: youtube-thumbnails-api
- description: Manages images that display in the corner of a player during playback of a channel's videos, supporting upload and deletion of channel watermarks.
  name: Youtube Watermarks API
  slug: youtube-watermarks-api
- description: Retrieves a list of reasons that can be used to report abusive videos, supporting programmatic submission of video abuse reports.
  name: Youtube Video Abuse Report Reasons API
  slug: youtube-video-abuse-report-reasons-api
- description: Enables embedding a YouTube video player on websites and controlling playback through JavaScript. The API supports queuing and playing videos, adjusting volume, retrieving video information, and subsc
  name: YouTube IFrame Player API
  slug: youtube-iframe-player-api
- description: Provides an embeddable subscribe button that website owners can configure and add to their pages, enabling one-click channel subscriptions for visitors without leaving the page.
  name: YouTube Subscribe Button
  slug: youtube-subscribe-button
- description: Manages thumbnail images associated with YouTube playlists, supporting retrieval, insertion, update, and deletion of custom playlist thumbnail images.
  name: Youtube Playlist Images API
  slug: youtube-playlist-images-api
- description: Enables YouTube content partners to interact with the rights management system, allowing creation and management of assets, content references, ownership data, claims, and policies for intellectual pr
  name: YouTube Content ID API
  slug: youtube-content-id-api
- description: Provides an oEmbed-compliant endpoint that returns embed code and metadata for YouTube videos in JSON or XML format, enabling easy embedding of YouTube content on external websites.
  name: YouTube oEmbed API
  slug: youtube-oembed-api
- description: Operations for managing analytics group definitions
  name: Youtube Analytics Groups API
  slug: youtube-analytics-groups-api
- description: Operations for retrieving YouTube Analytics reports and metrics
  name: Youtube Analytics Reports API
  slug: youtube-analytics-reports-api
- description: Operations related to YouTube video caption tracks
  name: Youtube Captions API
  slug: youtube-captions-api
- description: Operations related to YouTube channel resources
  name: Youtube Channels API
  slug: youtube-channels-api
- description: Operations related to individual YouTube comments
  name: Youtube Comments API
  slug: youtube-comments-api
- description: Operations related to YouTube comment threads
  name: Youtube CommentThreads API
  slug: youtube-commentthreads-api
- description: Operations for managing items within analytics groups
  name: Youtube Group Items API
  slug: youtube-group-items-api
- description: Operations for managing items within YouTube Analytics groups
  name: Youtube GroupItems API
  slug: youtube-groupitems-api
- description: Operations for managing YouTube Analytics groups
  name: Youtube Groups API
  slug: youtube-groups-api
- description: Operations related to internationalization resources
  name: Youtube I18n API
  slug: youtube-i18n-api
- description: Operations for managing YouTube reporting jobs
  name: Youtube Jobs API
  slug: youtube-jobs-api
- description: Operations for managing YouTube live broadcast events
  name: Youtube LiveBroadcasts API
  slug: youtube-livebroadcasts-api
- description: Operations for managing messages in YouTube live chat
  name: Youtube LiveChatMessages API
  slug: youtube-livechatmessages-api
- description: Operations for managing moderators in YouTube live chat
  name: Youtube LiveChatModerators API
  slug: youtube-livechatmoderators-api
- description: Operations for managing YouTube live video streams
  name: Youtube LiveStreams API
  slug: youtube-livestreams-api
- description: Operations for managing items within playlists
  name: Youtube Playlist Items API
  slug: youtube-playlist-items-api
- description: Operations related to items within YouTube playlists
  name: Youtube PlaylistItems API
  slug: youtube-playlistitems-api
- description: Operations related to YouTube playlist resources
  name: Youtube Playlists API
  slug: youtube-playlists-api
- description: Operations for querying YouTube Analytics report data
  name: Youtube Reports API
  slug: youtube-reports-api
- description: Operations for listing available report types
  name: Youtube ReportTypes API
  slug: youtube-reporttypes-api
- description: Operations for searching YouTube content
  name: Youtube Search API
  slug: youtube-search-api
- description: Operations related to YouTube channel subscriptions
  name: Youtube Subscriptions API
  slug: youtube-subscriptions-api
- description: Operations related to YouTube video categories
  name: Youtube VideoCategories API
  slug: youtube-videocategories-api
- description: Operations related to YouTube video resources
  name: Youtube Videos API
  slug: youtube-videos-api
arazzos:
- description: ''
  name: _Index
  slug: _index
- description: Read a channel, list the comment threads on its discussion, and reply to the first thread.
  name: YouTube Channel Comment Threads and Reply
  slug: youtube-channel-comment-threads-reply-workflow
- description: Resolve a channel, list its playlists, then list the items inside the first playlist.
  name: YouTube Channel Playlists and Items
  slug: youtube-channel-playlists-items-workflow
- description: Create a destination playlist, read items from a source playlist, and copy the first two across.
  name: YouTube Copy Playlist Items
  slug: youtube-copy-playlist-items-workflow
- description: Create a new playlist and insert two videos into it in sequence.
  name: YouTube Create Playlist and Add Items
  slug: youtube-create-playlist-add-items-workflow
- description: Search for a video, confirm its details, then post a top-level comment on it.
  name: YouTube Discover and Comment
  slug: youtube-discover-and-comment-workflow
- description: Resolve the authenticated user's uploads playlist, list its items, then batch-fetch video details.
  name: YouTube My Channel Uploads
  slug: youtube-mine-channel-uploads-workflow
- description: List held-for-review comment threads on a video and set the top one's moderation status.
  name: YouTube Moderate Comment Threads
  slug: youtube-moderate-comment-threads-workflow
- description: Post a top-level comment on a video, then immediately set its moderation status.
  name: YouTube Post and Moderate a Comment Thread
  slug: youtube-post-and-moderate-comment-workflow
- description: Post a top-level comment on a video and then add a reply to it.
  name: YouTube Post Comment Thread and Reply
  slug: youtube-post-comment-thread-reply-workflow
- description: Search for a channel, confirm it exists, then subscribe the authenticated user to it.
  name: YouTube Search Channel and Subscribe
  slug: youtube-search-channel-subscribe-workflow
- description: Search for a playlist, read its full resource, then list the videos it contains.
  name: YouTube Search Playlist and List Items
  slug: youtube-search-playlist-list-items-workflow
- description: Search for a video, read its details, then list the caption tracks available on it.
  name: YouTube Search Video and List Captions
  slug: youtube-search-video-captions-workflow
- description: Search for a video, fetch its full details, then list the comment threads on it.
  name: YouTube Search to Video Comment Threads
  slug: youtube-search-video-comment-threads-workflow
- description: Subscribe the authenticated user to a channel, then confirm by listing their subscriptions.
  name: YouTube Subscribe and Confirm
  slug: youtube-subscribe-and-confirm-workflow
- description: Pull the most popular videos for a region, create a playlist, and add the top trending video to it.
  name: YouTube Trending Videos to Playlist
  slug: youtube-trending-to-playlist-workflow
- description: Read a video's current snippet, then update its title, description, and category.
  name: YouTube Update Video Metadata
  slug: youtube-update-video-metadata-workflow
- description: Upload a draft caption track for a video, then publish it by updating its draft status.
  name: YouTube Upload and Update a Caption Track
  slug: youtube-upload-update-caption-workflow
- description: Insert a video resource, create a playlist, and add the new video to that playlist.
  name: YouTube Upload Video and Add to Playlist
  slug: youtube-upload-video-add-to-playlist-workflow
- description: Pull a video's statistics, its top comment thread, and the replies under that thread's top comment.
  name: YouTube Video Engagement Report
  slug: youtube-video-engagement-report-workflow
artifact_total: 417
collections:
- collection_type: postman
  name: YouTube Analytics API
  slug: postman-youtube-analytics
- collection_type: postman
  name: YouTube Data API v3
  slug: postman-youtube-data-api
- collection_type: postman
  name: YouTube Live Streaming API
  slug: postman-youtube-live-streaming
- collection_type: postman
  name: YouTube Reporting API
  slug: postman-youtube-reporting
- collection_type: open
  name: YouTube Analytics API
  slug: open-youtube-analytics
- collection_type: open
  name: YouTube Data API v3
  slug: open-youtube-data-api
- collection_type: open
  name: YouTube Live Streaming API
  slug: open-youtube-live-streaming
- collection_type: open
  name: YouTube Reporting API
  slug: open-youtube-reporting
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/youtube-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/youtube-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/youtube-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/youtube-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/youtube-scopes.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/youtube/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/youtube-channel-comment-threads-reply-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/youtube-channel-playlists-items-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/youtube-copy-playlist-items-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/youtube-create-playlist-add-items-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/youtube-discover-and-comment-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/youtube-mine-channel-uploads-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/youtube-moderate-comment-threads-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/youtube-post-and-moderate-comment-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/youtube-post-comment-thread-reply-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/youtube-search-channel-subscribe-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/youtube-search-playlist-list-items-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/youtube-search-video-captions-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/youtube-search-video-comment-threads-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/youtube-subscribe-and-confirm-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/youtube-trending-to-playlist-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/youtube-update-video-metadata-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/youtube-upload-update-caption-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/youtube-upload-video-add-to-playlist-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/youtube-video-engagement-report-workflow.yml
- group: build
  title: ''
  type: Packages
  url: packages/youtube-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/youtube-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/youtube-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/youtube-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/youtube-data-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/youtube-analytics-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/youtube-live-streaming-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/youtube-reporting-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/youtube-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/youtube-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/youtube-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/youtube-changelog.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/youtube-conventions.yml
- group: design
  title: ''
  type: Components
  url: components/youtube-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/youtube-data-model.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/youtube
- group: start
  title: ''
  type: Portal
  url: https://developers.google.com/youtube/v3
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.google.com/youtube/v3/getting-started
- group: docs
  title: ''
  type: Documentation
  url: https://developers.google.com/youtube/v3
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.google.com/youtube/v3/getting-started
- group: build
  title: ''
  type: CodeExamples
  url: https://developers.google.com/youtube/v3/code_samples
- group: operate
  title: ''
  type: Support
  url: https://developers.google.com/youtube/v3/support
- group: build
  title: ''
  type: SDKs
  url: https://developers.google.com/youtube/v3/libraries
- group: auth
  title: ''
  type: Authentication
  url: https://developers.google.com/youtube/v3/guides/authentication
- group: operate
  title: ''
  type: ChangeLog
  url: https://developers.google.com/youtube/v3/revision_history
- group: operate
  title: ''
  type: RateLimits
  url: https://developers.google.com/youtube/v3/determine_quota_cost
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/youtube/api-samples
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/youtube
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/user/YouTubeDev
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developers.google.com/youtube/terms/api-services-terms-of-service
- group: other
  title: ''
  type: Branding
  url: https://developers.google.com/youtube/terms/branding-guidelines
- group: operate
  title: ''
  type: ChangeLog
  url: https://developers.google.com/youtube/terms/revision-history
- group: operate
  title: ''
  type: Support
  url: https://issuetracker.google.com/issues?q=componentid:186600
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/youtube-api
- group: start
  title: ''
  type: Signup
  url: https://developers.google.com/youtube/registering_an_application
- group: docs
  title: ''
  type: APIReference
  url: https://developers.google.com/youtube/v3/docs
- group: design
  title: ''
  type: ErrorCodes
  url: https://developers.google.com/youtube/v3/docs/errors
- group: auth
  title: ''
  type: Compliance
  url: https://developers.google.com/youtube/terms/developer-policies
- group: auth
  title: ''
  type: Compliance
  url: https://developers.google.com/youtube/v3/guides/quota_and_compliance_audits
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.google.com/youtube/v3/guides/implementation
- group: other
  title: ''
  type: X
  url: https://x.com/YouTubeDev
- group: docs
  title: ''
  type: Documentation
  url: https://developers.google.com/youtube/documentation/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cloud.google.com
- group: company
  title: ''
  type: Blog
  url: https://blog.youtube/news-and-events/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://policies.google.com/privacy
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/youtube/geo-search-tool
- group: build
  title: ''
  type: SDKs
  url: https://github.com/youtube/youtube-ios-player-helper
- group: design
  title: ''
  type: JSONLD
  url: json-ld/youtube-context.jsonld
- group: design
  title: ''
  type: JSONLD
  url: json-ld/youtube-data-context.jsonld
- group: design
  title: ''
  type: JSONLD
  url: json-ld/youtube-analytics-context.jsonld
- group: design
  title: ''
  type: JSONLD
  url: json-ld/youtube-live-context.jsonld
- group: design
  title: ''
  type: JSONLD
  url: json-ld/youtube-reporting-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/youtube-video-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/youtube-channel-schema.json
- group: design
  title: ''
  type: SpectralRules
  url: rules/youtube-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/youtube-vocabulary.yaml
- group: commercial
  title: ''
  type: Plans
  url: ''
- group: operate
  title: ''
  type: RateLimits
  url: https://developers.google.com/youtube/v3/determine_quota_cost
created: '2025-07-29'
description: YouTube APIs provide programmatic access to YouTube data including videos, playlists, channels, user interactions, live streaming, analytics, captions, and embedded player controls.
examples:
- key_count: 3
  name: Youtube Analytics Column Header Example
  slug: youtube-analytics-column-header-example
- key_count: 1
  name: Youtube Analytics Error Response Example
  slug: youtube-analytics-error-response-example
- key_count: 2
  name: Youtube Analytics Group Content Details Example
  slug: youtube-analytics-group-content-details-example
- key_count: 5
  name: Youtube Analytics Group Example
  slug: youtube-analytics-group-example
- key_count: 5
  name: Youtube Analytics Group Item Example
  slug: youtube-analytics-group-item-example
- key_count: 3
  name: Youtube Analytics Group Item List Response Example
  slug: youtube-analytics-group-item-list-response-example
- key_count: 4
  name: Youtube Analytics Group List Response Example
  slug: youtube-analytics-group-list-response-example
- key_count: 3
  name: Youtube Analytics Query Response Example
  slug: youtube-analytics-query-response-example
- key_count: 4
  name: Youtube Data Caption Example
  slug: youtube-data-caption-example
- key_count: 3
  name: Youtube Data Caption List Response Example
  slug: youtube-data-caption-list-response-example
- key_count: 7
  name: Youtube Data Channel Example
  slug: youtube-data-channel-example
- key_count: 6
  name: Youtube Data Channel List Response Example
  slug: youtube-data-channel-list-response-example
- key_count: 7
  name: Youtube Data Channel Snippet Example
  slug: youtube-data-channel-snippet-example
- key_count: 4
  name: Youtube Data Channel Statistics Example
  slug: youtube-data-channel-statistics-example
- key_count: 4
  name: Youtube Data Comment Example
  slug: youtube-data-comment-example
- key_count: 5
  name: Youtube Data Comment List Response Example
  slug: youtube-data-comment-list-response-example
- key_count: 5
  name: Youtube Data Comment Thread Example
  slug: youtube-data-comment-thread-example
- key_count: 5
  name: Youtube Data Comment Thread List Response Example
  slug: youtube-data-comment-thread-list-response-example
- key_count: 1
  name: Youtube Data Error Response Example
  slug: youtube-data-error-response-example
- key_count: 3
  name: Youtube Data I18N Language List Response Example
  slug: youtube-data-i18n-language-list-response-example
- key_count: 3
  name: Youtube Data I18N Region List Response Example
  slug: youtube-data-i18n-region-list-response-example
- key_count: 2
  name: Youtube Data Page Info Example
  slug: youtube-data-page-info-example
- key_count: 6
  name: Youtube Data Playlist Example
  slug: youtube-data-playlist-example
- key_count: 6
  name: Youtube Data Playlist Item Example
  slug: youtube-data-playlist-item-example
- key_count: 6
  name: Youtube Data Playlist Item List Response Example
  slug: youtube-data-playlist-item-list-response-example
- key_count: 6
  name: Youtube Data Playlist List Response Example
  slug: youtube-data-playlist-list-response-example
- key_count: 7
  name: Youtube Data Search List Response Example
  slug: youtube-data-search-list-response-example
- key_count: 4
  name: Youtube Data Search Result Example
  slug: youtube-data-search-result-example
- key_count: 4
  name: Youtube Data Subscription Example
  slug: youtube-data-subscription-example
- key_count: 6
  name: Youtube Data Subscription List Response Example
  slug: youtube-data-subscription-list-response-example
- key_count: 1
  name: Youtube Live Error Response Example
  slug: youtube-live-error-response-example
- key_count: 12
  name: Youtube Live Live Broadcast Content Details Example
  slug: youtube-live-live-broadcast-content-details-example
- key_count: 7
  name: Youtube Live Live Broadcast Example
  slug: youtube-live-live-broadcast-example
- key_count: 6
  name: Youtube Live Live Broadcast List Response Example
  slug: youtube-live-live-broadcast-list-response-example
- key_count: 11
  name: Youtube Live Live Broadcast Snippet Example
  slug: youtube-live-live-broadcast-snippet-example
- key_count: 5
  name: Youtube Live Live Broadcast Status Example
  slug: youtube-live-live-broadcast-status-example
- key_count: 5
  name: Youtube Live Live Chat Message Example
  slug: youtube-live-live-chat-message-example
- key_count: 7
  name: Youtube Live Live Chat Message List Response Example
  slug: youtube-live-live-chat-message-list-response-example
- key_count: 4
  name: Youtube Live Live Chat Moderator Example
  slug: youtube-live-live-chat-moderator-example
- key_count: 6
  name: Youtube Live Live Chat Moderator List Response Example
  slug: youtube-live-live-chat-moderator-list-response-example
- key_count: 2
  name: Youtube Live Live Stream Content Details Example
  slug: youtube-live-live-stream-content-details-example
- key_count: 7
  name: Youtube Live Live Stream Example
  slug: youtube-live-live-stream-example
- key_count: 6
  name: Youtube Live Live Stream List Response Example
  slug: youtube-live-live-stream-list-response-example
- key_count: 5
  name: Youtube Live Live Stream Snippet Example
  slug: youtube-live-live-stream-snippet-example
- key_count: 2
  name: Youtube Live Live Stream Status Example
  slug: youtube-live-live-stream-status-example
- key_count: 2
  name: Youtube Live Page Info Example
  slug: youtube-live-page-info-example
- key_count: 6
  name: Youtube Reporting Job Example
  slug: youtube-reporting-job-example
- key_count: 2
  name: Youtube Reporting List Jobs Response Example
  slug: youtube-reporting-list-jobs-response-example
- key_count: 2
  name: Youtube Reporting List Report Types Response Example
  slug: youtube-reporting-list-report-types-response-example
- key_count: 2
  name: Youtube Reporting List Reports Response Example
  slug: youtube-reporting-list-reports-response-example
- key_count: 7
  name: Youtube Reporting Report Example
  slug: youtube-reporting-report-example
- key_count: 4
  name: Youtube Reporting Report Type Example
  slug: youtube-reporting-report-type-example
- key_count: 6
  name: Youtube Youtubeanalyticsgroupitemsinsert Example
  slug: youtube-youtubeanalyticsgroupitemsinsert-example
- key_count: 6
  name: Youtube Youtubeanalyticsgroupitemslist Example
  slug: youtube-youtubeanalyticsgroupitemslist-example
- key_count: 6
  name: Youtube Youtubeanalyticsgroupsinsert Example
  slug: youtube-youtubeanalyticsgroupsinsert-example
- key_count: 6
  name: Youtube Youtubeanalyticsgroupslist Example
  slug: youtube-youtubeanalyticsgroupslist-example
- key_count: 6
  name: Youtube Youtubeanalyticsgroupsupdate Example
  slug: youtube-youtubeanalyticsgroupsupdate-example
- key_count: 6
  name: Youtube Youtubeanalyticsreportsquery Example
  slug: youtube-youtubeanalyticsreportsquery-example
- key_count: 6
  name: Youtube Youtubecaptionsinsert Example
  slug: youtube-youtubecaptionsinsert-example
- key_count: 6
  name: Youtube Youtubecaptionslist Example
  slug: youtube-youtubecaptionslist-example
- key_count: 6
  name: Youtube Youtubecaptionsupdate Example
  slug: youtube-youtubecaptionsupdate-example
- key_count: 6
  name: Youtube Youtubechannelslist Example
  slug: youtube-youtubechannelslist-example
- key_count: 6
  name: Youtube Youtubechannelsupdate Example
  slug: youtube-youtubechannelsupdate-example
- key_count: 6
  name: Youtube Youtubecommentsinsert Example
  slug: youtube-youtubecommentsinsert-example
- key_count: 6
  name: Youtube Youtubecommentslist Example
  slug: youtube-youtubecommentslist-example
- key_count: 6
  name: Youtube Youtubecommentsupdate Example
  slug: youtube-youtubecommentsupdate-example
- key_count: 6
  name: Youtube Youtubecommentthreadsinsert Example
  slug: youtube-youtubecommentthreadsinsert-example
- key_count: 6
  name: Youtube Youtubecommentthreadslist Example
  slug: youtube-youtubecommentthreadslist-example
- key_count: 6
  name: Youtube Youtubecommentthreadsupdate Example
  slug: youtube-youtubecommentthreadsupdate-example
- key_count: 6
  name: Youtube Youtubei18Nlanguageslist Example
  slug: youtube-youtubei18nlanguageslist-example
- key_count: 6
  name: Youtube Youtubei18Nregionslist Example
  slug: youtube-youtubei18nregionslist-example
- key_count: 6
  name: Youtube Youtubelivebroadcastsbind Example
  slug: youtube-youtubelivebroadcastsbind-example
- key_count: 6
  name: Youtube Youtubelivebroadcastsinsert Example
  slug: youtube-youtubelivebroadcastsinsert-example
- key_count: 6
  name: Youtube Youtubelivebroadcastslist Example
  slug: youtube-youtubelivebroadcastslist-example
- key_count: 6
  name: Youtube Youtubelivebroadcaststransition Example
  slug: youtube-youtubelivebroadcaststransition-example
- key_count: 6
  name: Youtube Youtubelivebroadcastsupdate Example
  slug: youtube-youtubelivebroadcastsupdate-example
- key_count: 6
  name: Youtube Youtubelivechatmessagesinsert Example
  slug: youtube-youtubelivechatmessagesinsert-example
- key_count: 6
  name: Youtube Youtubelivechatmessageslist Example
  slug: youtube-youtubelivechatmessageslist-example
- key_count: 6
  name: Youtube Youtubelivechatmoderatorsinsert Example
  slug: youtube-youtubelivechatmoderatorsinsert-example
- key_count: 6
  name: Youtube Youtubelivechatmoderatorslist Example
  slug: youtube-youtubelivechatmoderatorslist-example
- key_count: 6
  name: Youtube Youtubelivestreamsinsert Example
  slug: youtube-youtubelivestreamsinsert-example
- key_count: 6
  name: Youtube Youtubelivestreamslist Example
  slug: youtube-youtubelivestreamslist-example
- key_count: 6
  name: Youtube Youtubelivestreamsupdate Example
  slug: youtube-youtubelivestreamsupdate-example
- key_count: 6
  name: Youtube Youtubeplaylistitemsinsert Example
  slug: youtube-youtubeplaylistitemsinsert-example
- key_count: 6
  name: Youtube Youtubeplaylistitemslist Example
  slug: youtube-youtubeplaylistitemslist-example
- key_count: 6
  name: Youtube Youtubeplaylistsinsert Example
  slug: youtube-youtubeplaylistsinsert-example
- key_count: 6
  name: Youtube Youtubeplaylistslist Example
  slug: youtube-youtubeplaylistslist-example
- key_count: 6
  name: Youtube Youtubeplaylistsupdate Example
  slug: youtube-youtubeplaylistsupdate-example
- key_count: 6
  name: Youtube Youtubereportingjobscreate Example
  slug: youtube-youtubereportingjobscreate-example
- key_count: 6
  name: Youtube Youtubereportingjobsget Example
  slug: youtube-youtubereportingjobsget-example
- key_count: 6
  name: Youtube Youtubereportingjobslist Example
  slug: youtube-youtubereportingjobslist-example
- key_count: 6
  name: Youtube Youtubereportingreportsget Example
  slug: youtube-youtubereportingreportsget-example
- key_count: 6
  name: Youtube Youtubereportingreportslist Example
  slug: youtube-youtubereportingreportslist-example
- key_count: 6
  name: Youtube Youtubereportingreporttypeslist Example
  slug: youtube-youtubereportingreporttypeslist-example
- key_count: 6
  name: Youtube Youtubesearchlist Example
  slug: youtube-youtubesearchlist-example
- key_count: 6
  name: Youtube Youtubesubscriptionsinsert Example
  slug: youtube-youtubesubscriptionsinsert-example
- key_count: 6
  name: Youtube Youtubesubscriptionslist Example
  slug: youtube-youtubesubscriptionslist-example
- key_count: 6
  name: Youtube Youtubevideocategorieslist Example
  slug: youtube-youtubevideocategorieslist-example
- key_count: 6
  name: Youtube Youtubevideosinsert Example
  slug: youtube-youtubevideosinsert-example
- key_count: 6
  name: Youtube Youtubevideoslist Example
  slug: youtube-youtubevideoslist-example
- key_count: 6
  name: Youtube Youtubevideosupdate Example
  slug: youtube-youtubevideosupdate-example
features:
- 'YouTube (Google): hundreds of services across Video Platform'
- 'Detailed pricing: see https://developers.google.com/youtube/v3/getting-started'
- 'Service: YouTube Data API v3 (free, quota-limited at 10K units/day)'
- 'Service: YouTube Live Streaming API'
- 'Service: YouTube Analytics API'
- 'Service: YouTube Reporting API'
- 'Service: YouTube Player API'
- 'Service: YouTube oEmbed'
- 'Service: Google Cloud quota increases via cloud console'
finops:
- name: Youtube Finops
  service_category: Video Platform
  slug: youtube-finops
graphqls:
- description: YouTube does not expose a native public GraphQL API. The YouTube Data API v3 is a REST-based API served at `https://www.googleapis.com/youtube/v3`. This GraphQL schema is a community-defined type mapp
  name: YouTube GraphQL Schema
  slug: youtube-graphql
image: https://www.youtube.com/img/desktop/yt_1200.png
integrations:
- description: Integrates with GCP for authentication, hosting, and infrastructure services.
  name: Google Cloud Platform
- description: Combine YouTube Analytics data with Google Analytics for comprehensive web and video metrics.
  name: Google Analytics
- description: Connect YouTube content with Google Ads for video advertising campaigns.
  name: Google Ads
- description: Use Firebase with YouTube APIs for mobile app development with video features.
  name: Firebase
- description: Embed YouTube videos in Google Docs, Slides, and Sites for collaborative content.
  name: Google Workspace
json_schemas:
- name: ColumnHeader
  property_count: 3
  slug: youtube-analytics-column-header
- name: ErrorResponse
  property_count: 1
  slug: youtube-analytics-error-response
- name: GroupContentDetails
  property_count: 2
  slug: youtube-analytics-group-content-details
- name: GroupItemListResponse
  property_count: 3
  slug: youtube-analytics-group-item-list-response
- name: GroupItem
  property_count: 5
  slug: youtube-analytics-group-item
- name: GroupListResponse
  property_count: 4
  slug: youtube-analytics-group-list-response
- name: Group
  property_count: 5
  slug: youtube-analytics-group
- name: QueryResponse
  property_count: 3
  slug: youtube-analytics-query-response
- name: AnalyticsReportResponse
  property_count: 3
  slug: youtube-analyticsreportresponse
- name: Caption
  property_count: 4
  slug: youtube-caption
- name: CaptionListResponse
  property_count: 3
  slug: youtube-captionlistresponse
- name: CaptionSnippet
  property_count: 12
  slug: youtube-captionsnippet
- name: YouTube Channel
  property_count: 10
  slug: youtube-channel
- name: ChannelContentDetails
  property_count: 1
  slug: youtube-channelcontentdetails
- name: ChannelListResponse
  property_count: 6
  slug: youtube-channellistresponse
- name: ChannelSnippet
  property_count: 7
  slug: youtube-channelsnippet
- name: ChannelStatistics
  property_count: 4
  slug: youtube-channelstatistics
- name: ColumnHeader
  property_count: 3
  slug: youtube-columnheader
- name: Comment
  property_count: 4
  slug: youtube-comment
- name: CommentListResponse
  property_count: 5
  slug: youtube-commentlistresponse
- name: CommentSnippet
  property_count: 9
  slug: youtube-commentsnippet
- name: CommentThread
  property_count: 5
  slug: youtube-commentthread
- name: CommentThreadListResponse
  property_count: 5
  slug: youtube-commentthreadlistresponse
- name: CommentThreadReplies
  property_count: 1
  slug: youtube-commentthreadreplies
- name: CommentThreadSnippet
  property_count: 6
  slug: youtube-commentthreadsnippet
- name: CaptionListResponse
  property_count: 3
  slug: youtube-data-caption-list-response
- name: Caption
  property_count: 4
  slug: youtube-data-caption
- name: ChannelListResponse
  property_count: 6
  slug: youtube-data-channel-list-response
- name: Channel
  property_count: 7
  slug: youtube-data-channel
- name: ChannelSnippet
  property_count: 7
  slug: youtube-data-channel-snippet
- name: ChannelStatistics
  property_count: 4
  slug: youtube-data-channel-statistics
- name: CommentListResponse
  property_count: 5
  slug: youtube-data-comment-list-response
- name: Comment
  property_count: 4
  slug: youtube-data-comment
- name: CommentThreadListResponse
  property_count: 5
  slug: youtube-data-comment-thread-list-response
- name: CommentThread
  property_count: 5
  slug: youtube-data-comment-thread
- name: ErrorResponse
  property_count: 1
  slug: youtube-data-error-response
- name: I18nLanguageListResponse
  property_count: 3
  slug: youtube-data-i18n-language-list-response
- name: I18nRegionListResponse
  property_count: 3
  slug: youtube-data-i18n-region-list-response
- name: PageInfo
  property_count: 2
  slug: youtube-data-page-info
- name: PlaylistItemListResponse
  property_count: 6
  slug: youtube-data-playlist-item-list-response
- name: PlaylistItem
  property_count: 6
  slug: youtube-data-playlist-item
- name: PlaylistListResponse
  property_count: 6
  slug: youtube-data-playlist-list-response
- name: Playlist
  property_count: 6
  slug: youtube-data-playlist
- name: SearchListResponse
  property_count: 7
  slug: youtube-data-search-list-response
- name: SearchResult
  property_count: 4
  slug: youtube-data-search-result
- name: SubscriptionListResponse
  property_count: 6
  slug: youtube-data-subscription-list-response
- name: Subscription
  property_count: 4
  slug: youtube-data-subscription
- name: VideoCategoryListResponse
  property_count: 3
  slug: youtube-data-video-category-list-response
- name: VideoCategory
  property_count: 4
  slug: youtube-data-video-category
- name: VideoContentDetails
  property_count: 6
  slug: youtube-data-video-content-details
- name: VideoListResponse
  property_count: 6
  slug: youtube-data-video-list-response
- name: VideoPlayer
  property_count: 3
  slug: youtube-data-video-player
- name: Video
  property_count: 9
  slug: youtube-data-video
- name: VideoSnippet
  property_count: 11
  slug: youtube-data-video-snippet
- name: VideoStatistics
  property_count: 5
  slug: youtube-data-video-statistics
- name: VideoStatus
  property_count: 6
  slug: youtube-data-video-status
- name: ErrorDetails
  property_count: 3
  slug: youtube-errordetails
- name: ErrorItem
  property_count: 5
  slug: youtube-erroritem
- name: ErrorResponse
  property_count: 1
  slug: youtube-errorresponse
- name: Group
  property_count: 5
  slug: youtube-group
- name: GroupContentDetails
  property_count: 2
  slug: youtube-groupcontentdetails
- name: GroupCreateRequest
  property_count: 2
  slug: youtube-groupcreaterequest
- name: GroupItem
  property_count: 5
  slug: youtube-groupitem
- name: GroupItemCreateRequest
  property_count: 2
  slug: youtube-groupitemcreaterequest
- name: GroupItemListResponse
  property_count: 3
  slug: youtube-groupitemlistresponse
- name: GroupItemResource
  property_count: 2
  slug: youtube-groupitemresource
- name: GroupListResponse
  property_count: 4
  slug: youtube-grouplistresponse
- name: GroupSnippet
  property_count: 2
  slug: youtube-groupsnippet
- name: GroupUpdateRequest
  property_count: 2
  slug: youtube-groupupdaterequest
- name: I18nLanguageListResponse
  property_count: 3
  slug: youtube-i18nlanguagelistresponse
- name: I18nRegionListResponse
  property_count: 3
  slug: youtube-i18nregionlistresponse
- name: Job
  property_count: 6
  slug: youtube-job
- name: ListJobsResponse
  property_count: 2
  slug: youtube-listjobsresponse
- name: ListReportsResponse
  property_count: 2
  slug: youtube-listreportsresponse
- name: ListReportTypesResponse
  property_count: 2
  slug: youtube-listreporttypesresponse
- name: ErrorResponse
  property_count: 1
  slug: youtube-live-error-response
- name: LiveBroadcastContentDetails
  property_count: 12
  slug: youtube-live-live-broadcast-content-details
- name: LiveBroadcastListResponse
  property_count: 6
  slug: youtube-live-live-broadcast-list-response
- name: LiveBroadcast
  property_count: 7
  slug: youtube-live-live-broadcast
- name: LiveBroadcastSnippet
  property_count: 11
  slug: youtube-live-live-broadcast-snippet
- name: LiveBroadcastStatus
  property_count: 5
  slug: youtube-live-live-broadcast-status
- name: LiveChatMessageListResponse
  property_count: 7
  slug: youtube-live-live-chat-message-list-response
- name: LiveChatMessage
  property_count: 5
  slug: youtube-live-live-chat-message
- name: LiveChatModeratorListResponse
  property_count: 6
  slug: youtube-live-live-chat-moderator-list-response
- name: LiveChatModerator
  property_count: 4
  slug: youtube-live-live-chat-moderator
- name: LiveStreamContentDetails
  property_count: 2
  slug: youtube-live-live-stream-content-details
- name: LiveStreamListResponse
  property_count: 6
  slug: youtube-live-live-stream-list-response
- name: LiveStream
  property_count: 7
  slug: youtube-live-live-stream
- name: LiveStreamSnippet
  property_count: 5
  slug: youtube-live-live-stream-snippet
- name: LiveStreamStatus
  property_count: 2
  slug: youtube-live-live-stream-status
- name: PageInfo
  property_count: 2
  slug: youtube-live-page-info
- name: LiveBroadcast
  property_count: 7
  slug: youtube-livebroadcast
- name: LiveBroadcastContentDetails
  property_count: 12
  slug: youtube-livebroadcastcontentdetails
- name: LiveBroadcastListResponse
  property_count: 6
  slug: youtube-livebroadcastlistresponse
- name: LiveBroadcastSnippet
  property_count: 11
  slug: youtube-livebroadcastsnippet
- name: LiveBroadcastStatus
  property_count: 5
  slug: youtube-livebroadcaststatus
- name: LiveChatMessage
  property_count: 5
  slug: youtube-livechatmessage
- name: LiveChatMessageListResponse
  property_count: 7
  slug: youtube-livechatmessagelistresponse
- name: LiveChatModerator
  property_count: 4
  slug: youtube-livechatmoderator
- name: LiveChatModeratorListResponse
  property_count: 6
  slug: youtube-livechatmoderatorlistresponse
- name: LiveStream
  property_count: 7
  slug: youtube-livestream
- name: LiveStreamContentDetails
  property_count: 2
  slug: youtube-livestreamcontentdetails
- name: LiveStreamListResponse
  property_count: 6
  slug: youtube-livestreamlistresponse
- name: LiveStreamSnippet
  property_count: 5
  slug: youtube-livestreamsnippet
- name: LiveStreamStatus
  property_count: 2
  slug: youtube-livestreamstatus
- name: PageInfo
  property_count: 2
  slug: youtube-pageinfo
- name: Playlist
  property_count: 6
  slug: youtube-playlist
- name: PlaylistContentDetails
  property_count: 1
  slug: youtube-playlistcontentdetails
- name: PlaylistInsertRequest
  property_count: 2
  slug: youtube-playlistinsertrequest
- name: PlaylistItem
  property_count: 6
  slug: youtube-playlistitem
- name: PlaylistItemContentDetails
  property_count: 2
  slug: youtube-playlistitemcontentdetails
- name: PlaylistItemInsertRequest
  property_count: 1
  slug: youtube-playlistiteminsertrequest
- name: PlaylistItemListResponse
  property_count: 6
  slug: youtube-playlistitemlistresponse
- name: PlaylistItemSnippet
  property_count: 9
  slug: youtube-playlistitemsnippet
- name: PlaylistListResponse
  property_count: 6
  slug: youtube-playlistlistresponse
- name: PlaylistSnippet
  property_count: 6
  slug: youtube-playlistsnippet
- name: PlaylistStatus
  property_count: 1
  slug: youtube-playliststatus
- name: PlaylistUpdateRequest
  property_count: 2
  slug: youtube-playlistupdaterequest
- name: QueryResponse
  property_count: 3
  slug: youtube-queryresponse
- name: Report
  property_count: 7
  slug: youtube-report
- name: Job
  property_count: 6
  slug: youtube-reporting-job
- name: ListJobsResponse
  property_count: 2
  slug: youtube-reporting-list-jobs-response
- name: ListReportTypesResponse
  property_count: 2
  slug: youtube-reporting-list-report-types-response
- name: ListReportsResponse
  property_count: 2
  slug: youtube-reporting-list-reports-response
- name: Report
  property_count: 7
  slug: youtube-reporting-report
- name: ReportType
  property_count: 4
  slug: youtube-reporting-report-type
- name: ReportType
  property_count: 4
  slug: youtube-reporttype
- name: ResourceId
  property_count: 4
  slug: youtube-resourceid
- name: SearchListResponse
  property_count: 7
  slug: youtube-searchlistresponse
- name: SearchResult
  property_count: 4
  slug: youtube-searchresult
- name: SearchResultSnippet
  property_count: 6
  slug: youtube-searchresultsnippet
- name: Subscription
  property_count: 4
  slug: youtube-subscription
- name: SubscriptionContentDetails
  property_count: 2
  slug: youtube-subscriptioncontentdetails
- name: SubscriptionInsertRequest
  property_count: 1
  slug: youtube-subscriptioninsertrequest
- name: SubscriptionListResponse
  property_count: 6
  slug: youtube-subscriptionlistresponse
- name: SubscriptionSnippet
  property_count: 6
  slug: youtube-subscriptionsnippet
- name: Thumbnail
  property_count: 3
  slug: youtube-thumbnail
- name: ThumbnailDetails
  property_count: 5
  slug: youtube-thumbnaildetails
- name: YouTube Video
  property_count: 10
  slug: youtube-video
- name: VideoCategory
  property_count: 4
  slug: youtube-videocategory
- name: VideoCategoryListResponse
  property_count: 3
  slug: youtube-videocategorylistresponse
- name: VideoContentDetails
  property_count: 6
  slug: youtube-videocontentdetails
- name: VideoInsertRequest
  property_count: 2
  slug: youtube-videoinsertrequest
- name: VideoListResponse
  property_count: 6
  slug: youtube-videolistresponse
- name: VideoPlayer
  property_count: 3
  slug: youtube-videoplayer
- name: VideoSnippet
  property_count: 11
  slug: youtube-videosnippet
- name: VideoStatistics
  property_count: 5
  slug: youtube-videostatistics
- name: VideoStatus
  property_count: 6
  slug: youtube-videostatus
- name: VideoUpdateRequest
  property_count: 2
  slug: youtube-videoupdaterequest
json_structures:
- name: Youtube Analytics Column Header Structure
  property_count: 3
  slug: youtube-analytics-column-header-structure
- name: Youtube Analytics Error Response Structure
  property_count: 1
  slug: youtube-analytics-error-response-structure
- name: Youtube Analytics Group Content Details Structure
  property_count: 2
  slug: youtube-analytics-group-content-details-structure
- name: Youtube Analytics Group Item List Response Structure
  property_count: 3
  slug: youtube-analytics-group-item-list-response-structure
- name: Youtube Analytics Group Item Structure
  property_count: 5
  slug: youtube-analytics-group-item-structure
- name: Youtube Analytics Group List Response Structure
  property_count: 4
  slug: youtube-analytics-group-list-response-structure
- name: Youtube Analytics Group Structure
  property_count: 5
  slug: youtube-analytics-group-structure
- name: Youtube Analytics Query Response Structure
  property_count: 3
  slug: youtube-analytics-query-response-structure
- name: Youtube Data Caption List Response Structure
  property_count: 3
  slug: youtube-data-caption-list-response-structure
- name: Youtube Data Caption Structure
  property_count: 4
  slug: youtube-data-caption-structure
- name: Youtube Data Channel List Response Structure
  property_count: 6
  slug: youtube-data-channel-list-response-structure
- name: Youtube Data Channel Snippet Structure
  property_count: 7
  slug: youtube-data-channel-snippet-structure
- name: Youtube Data Channel Statistics Structure
  property_count: 4
  slug: youtube-data-channel-statistics-structure
- name: Youtube Data Channel Structure
  property_count: 7
  slug: youtube-data-channel-structure
- name: Youtube Data Comment List Response Structure
  property_count: 5
  slug: youtube-data-comment-list-response-structure
- name: Youtube Data Comment Structure
  property_count: 4
  slug: youtube-data-comment-structure
- name: Youtube Data Comment Thread List Response Structure
  property_count: 5
  slug: youtube-data-comment-thread-list-response-structure
- name: Youtube Data Comment Thread Structure
  property_count: 5
  slug: youtube-data-comment-thread-structure
- name: Youtube Data Error Response Structure
  property_count: 1
  slug: youtube-data-error-response-structure
- name: Youtube Data I18N Language List Response Structure
  property_count: 3
  slug: youtube-data-i18n-language-list-response-structure
- name: Youtube Data I18N Region List Response Structure
  property_count: 3
  slug: youtube-data-i18n-region-list-response-structure
- name: Youtube Data Page Info Structure
  property_count: 2
  slug: youtube-data-page-info-structure
- name: Youtube Data Playlist Item List Response Structure
  property_count: 6
  slug: youtube-data-playlist-item-list-response-structure
- name: Youtube Data Playlist Item Structure
  property_count: 6
  slug: youtube-data-playlist-item-structure
- name: Youtube Data Playlist List Response Structure
  property_count: 6
  slug: youtube-data-playlist-list-response-structure
- name: Youtube Data Playlist Structure
  property_count: 6
  slug: youtube-data-playlist-structure
- name: Youtube Data Search List Response Structure
  property_count: 7
  slug: youtube-data-search-list-response-structure
- name: Youtube Data Search Result Structure
  property_count: 4
  slug: youtube-data-search-result-structure
- name: Youtube Data Subscription List Response Structure
  property_count: 6
  slug: youtube-data-subscription-list-response-structure
- name: Youtube Data Subscription Structure
  property_count: 4
  slug: youtube-data-subscription-structure
- name: Youtube Data Video Category List Response Structure
  property_count: 3
  slug: youtube-data-video-category-list-response-structure
- name: Youtube Data Video Category Structure
  property_count: 4
  slug: youtube-data-video-category-structure
- name: Youtube Data Video Content Details Structure
  property_count: 6
  slug: youtube-data-video-content-details-structure
- name: Youtube Data Video List Response Structure
  property_count: 6
  slug: youtube-data-video-list-response-structure
- name: Youtube Data Video Player Structure
  property_count: 3
  slug: youtube-data-video-player-structure
- name: Youtube Data Video Snippet Structure
  property_count: 11
  slug: youtube-data-video-snippet-structure
- name: Youtube Data Video Statistics Structure
  property_count: 5
  slug: youtube-data-video-statistics-structure
- name: Youtube Data Video Status Structure
  property_count: 6
  slug: youtube-data-video-status-structure
- name: Youtube Data Video Structure
  property_count: 9
  slug: youtube-data-video-structure
- name: Youtube Live Error Response Structure
  property_count: 1
  slug: youtube-live-error-response-structure
- name: Youtube Live Live Broadcast Content Details Structure
  property_count: 12
  slug: youtube-live-live-broadcast-content-details-structure
- name: Youtube Live Live Broadcast List Response Structure
  property_count: 6
  slug: youtube-live-live-broadcast-list-response-structure
- name: Youtube Live Live Broadcast Snippet Structure
  property_count: 11
  slug: youtube-live-live-broadcast-snippet-structure
- name: Youtube Live Live Broadcast Status Structure
  property_count: 5
  slug: youtube-live-live-broadcast-status-structure
- name: Youtube Live Live Broadcast Structure
  property_count: 7
  slug: youtube-live-live-broadcast-structure
- name: Youtube Live Live Chat Message List Response Structure
  property_count: 7
  slug: youtube-live-live-chat-message-list-response-structure
- name: Youtube Live Live Chat Message Structure
  property_count: 5
  slug: youtube-live-live-chat-message-structure
- name: Youtube Live Live Chat Moderator List Response Structure
  property_count: 6
  slug: youtube-live-live-chat-moderator-list-response-structure
- name: Youtube Live Live Chat Moderator Structure
  property_count: 4
  slug: youtube-live-live-chat-moderator-structure
- name: Youtube Live Live Stream Content Details Structure
  property_count: 2
  slug: youtube-live-live-stream-content-details-structure
- name: Youtube Live Live Stream List Response Structure
  property_count: 6
  slug: youtube-live-live-stream-list-response-structure
- name: Youtube Live Live Stream Snippet Structure
  property_count: 5
  slug: youtube-live-live-stream-snippet-structure
- name: Youtube Live Live Stream Status Structure
  property_count: 2
  slug: youtube-live-live-stream-status-structure
- name: Youtube Live Live Stream Structure
  property_count: 7
  slug: youtube-live-live-stream-structure
- name: Youtube Live Page Info Structure
  property_count: 2
  slug: youtube-live-page-info-structure
- name: Youtube Reporting Job Structure
  property_count: 6
  slug: youtube-reporting-job-structure
- name: Youtube Reporting List Jobs Response Structure
  property_count: 2
  slug: youtube-reporting-list-jobs-response-structure
- name: Youtube Reporting List Report Types Response Structure
  property_count: 2
  slug: youtube-reporting-list-report-types-response-structure
- name: Youtube Reporting List Reports Response Structure
  property_count: 2
  slug: youtube-reporting-list-reports-response-structure
- name: Youtube Reporting Report Structure
  property_count: 7
  slug: youtube-reporting-report-structure
- name: Youtube Reporting Report Type Structure
  property_count: 4
  slug: youtube-reporting-report-type-structure
- name: Youtube Structure
  property_count: 0
  slug: youtube-structure
jsonld:
- class_count: 0
  name: Youtube Analytics Context
  property_count: 8
  slug: youtube-analytics-context
- class_count: 0
  name: Youtube Context
  property_count: 10
  slug: youtube-context
- class_count: 0
  name: Youtube Data Context
  property_count: 31
  slug: youtube-data-context
- class_count: 0
  name: Youtube Live Context
  property_count: 16
  slug: youtube-live-context
- class_count: 0
  name: Youtube Reporting Context
  property_count: 6
  slug: youtube-reporting-context
layout: provider
mcp_servers:
- description: ''
  name: youtube-mcp.yml
  slug: youtube-mcpyml
modified: '2026-06-20'
name: Youtube
nav: Providers
network: true
overview: 'Youtube publishes 24 APIs on the [APIs.io](https://apis.io/) network, including Analytics Groups API, Analytics Reports API, Captions API, and 21 more. Tagged areas include Google, Media, Social, Streaming, and Video.


  The Youtube catalog on APIs.io includes 5 JSON-LD contexts and 2 Spectral governance rulesets.


  Youtube''s developer surface includes authentication, changelog, developer portal, getting-started guide, documentation, code examples, support, and 75 more developer resources.'
plans:
- name: Youtube Plans Pricing
  plan_count: 3
  slug: youtube-plans-pricing
random_paper: 103
rate_limits:
- limit_count: 2
  name: Youtube Rate Limits
  slug: youtube-rate-limits
rules:
- name: Youtube API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: youtube-jsonschema-spectral-rules
- name: Youtube API Rules
  rule_count: 58
  severity_counts:
    error: 22
    hint: 0
    info: 13
    warn: 23
  slug: youtube-spectral-rules
scopes:
- name: Youtube Scopes
  scope_count: 7
  slug: youtube-scopes
  summary_line: 7 scopes · authorizationCode
score:
  band: exemplar
  composite: 71.1
  delta: 0.0
  facets:
    commercial_clarity: 68.4
    contract_quality: 81.4
    developer_ergonomics: 65.2
    discoverability: 68.5
    governance: 80.2
    operational_transparency: 57.9
  previous_composite: 71.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 24
    mcp: derived
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/youtube/refs/heads/main/screenshots/youtube-2026-06-20T201752.png
security:
- kind: authentication
  name: Youtube Authentication
  slug: youtube-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Youtube Domain Security
  slug: youtube-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Youtube Vulnerability Disclosure
  slug: youtube-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: youtube
tags:
- Google
- Media
- Social
- Streaming
- Video
- Videos
use_cases:
- description: Build automated video upload and management workflows for content creators and media companies.
  name: Video Publishing Platform
- description: Aggregate YouTube analytics with other social platforms for unified performance monitoring.
  name: Social Media Dashboard
- description: Automate comment moderation and abuse reporting for community management at scale.
  name: Content Moderation
- description: Schedule and manage live streaming events with real-time chat and audience interaction.
  name: Live Event Management
- description: Organize educational video content into playlists with searchable course catalogs.
  name: Education Platform
- description: Track and manage content ownership, claims, and monetization policies using Content ID.
  name: Digital Rights Management
- description: Build custom video search experiences with filters for topics, dates, and regions.
  name: Video Search Application
- description: Create custom reporting dashboards with channel and video performance metrics.
  name: Analytics Dashboard
- description: Manage captions and translations to improve video accessibility across languages.
  name: Accessibility Tools
- description: Create branded video experiences with customized embedded players on external websites.
  name: Embedded Video Experience
website: https://developers.google.com/youtube/v3
---
