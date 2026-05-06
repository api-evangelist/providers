---
aid: youtube
url: https://raw.githubusercontent.com/api-search/videos/main/_apis/youtube/apis.md
apis:
  - aid: youtube:youtube-activities-api
    name: Youtube Activities API
    tags:
      - Activities
      - Videos
    image: https://www.youtube.com/img/desktop/yt_1200.png
    humanURL: https://developers.google.com/youtube/v3/docs/activities
    baseURL: https://www.googleapis.com/youtube/v3
    properties:
      - url: https://developers.google.com/youtube/v3/docs/activities/list
        type: Documentation
      - url: https://developers.google.com/youtube/v3/getting-started
        type: GettingStarted
      - url: https://developers.google.com/youtube/v3/guides/authentication
        type: Authentication
      - url: openapi/youtube-data-api-openapi.yml
        type: OpenAPI
    description: Manages YouTube user activities, including videos liked, channels subscribed to, and other user interactions on YouTube.
  - aid: youtube:youtube-channels-api
    name: Youtube Channels API
    tags:
      - Channels
      - Videos
    image: https://www.youtube.com/img/desktop/yt_1200.png
    humanURL: https://developers.google.com/youtube/v3/docs/channels
    baseURL: https://www.googleapis.com/youtube/v3
    properties:
      - url: https://developers.google.com/youtube/v3/docs/channels/list
        type: Documentation
      - url: https://developers.google.com/youtube/v3/getting-started
        type: GettingStarted
      - url: https://developers.google.com/youtube/v3/guides/authentication
        type: Authentication
      - url: openapi/youtube-data-api-openapi.yml
        type: OpenAPI
      - url: json-schema/youtube-channel-schema.json
        type: JSONSchema
    description: Provides access to YouTube channel data including channel metadata, statistics, and settings for both the authenticated user and other public channels.
  - aid: youtube:youtube-comments-api
    name: Youtube Comments API
    tags:
      - Comments
      - Videos
    image: https://www.youtube.com/img/desktop/yt_1200.png
    humanURL: https://developers.google.com/youtube/v3/docs/comments
    baseURL: https://www.googleapis.com/youtube/v3
    properties:
      - url: https://developers.google.com/youtube/v3/docs/comments/list
        type: Documentation
      - url: https://developers.google.com/youtube/v3/getting-started
        type: GettingStarted
      - url: https://developers.google.com/youtube/v3/guides/authentication
        type: Authentication
      - url: openapi/youtube-data-api-openapi.yml
        type: OpenAPI
    description: Manages individual comments on YouTube videos and other resources, supporting retrieval, creation, update, deletion, and moderation operations.
  - aid: youtube:youtube-comment-threads-api
    name: Youtube Comment Threads API
    tags:
      - Comments
      - Videos
    image: https://www.youtube.com/img/desktop/yt_1200.png
    humanURL: https://developers.google.com/youtube/v3/docs/commentThreads
    baseURL: https://www.googleapis.com/youtube/v3
    properties:
      - url: https://developers.google.com/youtube/v3/docs/commentThreads/list
        type: Documentation
      - url: https://developers.google.com/youtube/v3/getting-started
        type: GettingStarted
      - url: https://developers.google.com/youtube/v3/guides/authentication
        type: Authentication
      - url: openapi/youtube-data-api-openapi.yml
        type: OpenAPI
    description: Provides access to comment threads on YouTube videos and channels, where a comment thread includes a top-level comment and any replies to that comment.
  - aid: youtube:youtube-playlists-api
    name: Youtube Playlists API
    tags:
      - Playlists
      - Videos
    image: https://www.youtube.com/img/desktop/yt_1200.png
    humanURL: https://developers.google.com/youtube/v3/docs/playlists
    baseURL: https://www.googleapis.com/youtube/v3
    properties:
      - url: https://developers.google.com/youtube/v3/docs/playlists/list
        type: Documentation
      - url: https://developers.google.com/youtube/v3/getting-started
        type: GettingStarted
      - url: https://developers.google.com/youtube/v3/guides/authentication
        type: Authentication
      - url: openapi/youtube-data-api-openapi.yml
        type: OpenAPI
    description: Manages YouTube playlists including creating, updating, deleting, and listing playlists associated with a channel or the authenticated user.
  - aid: youtube:youtube-playlist-items-api
    name: Youtube Playlist Items API
    tags:
      - Playlists
      - Videos
    image: https://www.youtube.com/img/desktop/yt_1200.png
    humanURL: https://developers.google.com/youtube/v3/docs/playlistItems
    baseURL: https://www.googleapis.com/youtube/v3
    properties:
      - url: https://developers.google.com/youtube/v3/docs/playlistItems/list
        type: Documentation
      - url: https://developers.google.com/youtube/v3/getting-started
        type: GettingStarted
      - url: https://developers.google.com/youtube/v3/guides/authentication
        type: Authentication
      - url: openapi/youtube-data-api-openapi.yml
        type: OpenAPI
    description: Manages individual items within a YouTube playlist, enabling retrieval, addition, update, and removal of videos from playlists.
  - aid: youtube:youtube-search-api
    name: Youtube Search API
    tags:
      - Search
      - Videos
    image: https://www.youtube.com/img/desktop/yt_1200.png
    humanURL: https://developers.google.com/youtube/v3/docs/search
    baseURL: https://www.googleapis.com/youtube/v3
    properties:
      - url: https://developers.google.com/youtube/v3/docs/search/list
        type: Documentation
      - url: https://developers.google.com/youtube/v3/getting-started
        type: GettingStarted
      - url: https://developers.google.com/youtube/v3/guides/authentication
        type: Authentication
      - url: openapi/youtube-data-api-openapi.yml
        type: OpenAPI
    description: Searches across YouTube content including videos, channels, and playlists matching specified query parameters, returning a collection of results.
  - aid: youtube:youtube-subscriptions-api
    name: Youtube Subscriptions API
    tags:
      - Subscriptions
      - Videos
    image: https://www.youtube.com/img/desktop/yt_1200.png
    humanURL: https://developers.google.com/youtube/v3/docs/subscriptions
    baseURL: https://www.googleapis.com/youtube/v3
    properties:
      - url: https://developers.google.com/youtube/v3/docs/subscriptions/list
        type: Documentation
      - url: https://developers.google.com/youtube/v3/getting-started
        type: GettingStarted
      - url: https://developers.google.com/youtube/v3/guides/authentication
        type: Authentication
      - url: openapi/youtube-data-api-openapi.yml
        type: OpenAPI
    description: Manages YouTube channel subscriptions, allowing retrieval, creation, and deletion of subscriptions for the authenticated user.
  - aid: youtube:youtube-videos-api
    name: Youtube Videos API
    tags:
      - Videos
    image: https://www.youtube.com/img/desktop/yt_1200.png
    humanURL: https://developers.google.com/youtube/v3/docs/videos
    baseURL: https://www.googleapis.com/youtube/v3
    properties:
      - url: https://developers.google.com/youtube/v3/docs/videos/list
        type: Documentation
      - url: https://developers.google.com/youtube/v3/getting-started
        type: GettingStarted
      - url: https://developers.google.com/youtube/v3/guides/authentication
        type: Authentication
      - url: openapi/youtube-data-api-openapi.yml
        type: OpenAPI
      - url: json-schema/youtube-video-schema.json
        type: JSONSchema
    description: Provides access to YouTube video data including metadata, statistics, and content details, and supports uploading, updating, rating, and deleting videos.
  - aid: youtube:youtube-captions-api
    name: Youtube Captions API
    tags:
      - Captions
      - Videos
    image: https://www.youtube.com/img/desktop/yt_1200.png
    humanURL: https://developers.google.com/youtube/v3/docs/captions
    baseURL: https://www.googleapis.com/youtube/v3
    properties:
      - url: https://developers.google.com/youtube/v3/docs/captions
        type: Documentation
      - url: https://developers.google.com/youtube/v3/getting-started
        type: GettingStarted
      - url: https://developers.google.com/youtube/v3/guides/authentication
        type: Authentication
      - url: openapi/youtube-data-api-openapi.yml
        type: OpenAPI
    description: Manages caption tracks associated with YouTube videos. A caption track is associated with exactly one YouTube video and supports upload, update, download, and deletion operations.
  - aid: youtube:youtube-channel-sections-api
    name: Youtube Channel Sections API
    tags:
      - Channels
      - Videos
    image: https://www.youtube.com/img/desktop/yt_1200.png
    humanURL: https://developers.google.com/youtube/v3/docs/channelSections
    baseURL: https://www.googleapis.com/youtube/v3
    properties:
      - url: https://developers.google.com/youtube/v3/docs/channelSections
        type: Documentation
      - url: https://developers.google.com/youtube/v3/getting-started
        type: GettingStarted
      - url: https://developers.google.com/youtube/v3/guides/authentication
        type: Authentication
    description: Manages sections that a channel has chosen to feature on its channel page, including inserting, updating, and deleting channel sections.
  - aid: youtube:youtube-channel-banners-api
    name: Youtube Channel Banners API
    tags:
      - Channels
      - Videos
    image: https://www.youtube.com/img/desktop/yt_1200.png
    humanURL: https://developers.google.com/youtube/v3/docs/channelBanners
    baseURL: https://www.googleapis.com/youtube/v3
    properties:
      - url: https://developers.google.com/youtube/v3/docs/channelBanners
        type: Documentation
      - url: https://developers.google.com/youtube/v3/getting-started
        type: GettingStarted
      - url: https://developers.google.com/youtube/v3/guides/authentication
        type: Authentication
    description: Enables uploading a new banner image to a YouTube channel, returning the URL that identifies the uploaded image for use with the channels.update method.
  - aid: youtube:youtube-members-api
    name: Youtube Members API
    tags:
      - Members
      - Monetization
      - Videos
    image: https://www.youtube.com/img/desktop/yt_1200.png
    humanURL: https://developers.google.com/youtube/v3/docs/members
    baseURL: https://www.googleapis.com/youtube/v3
    properties:
      - url: https://developers.google.com/youtube/v3/docs/members
        type: Documentation
      - url: https://developers.google.com/youtube/v3/getting-started
        type: GettingStarted
      - url: https://developers.google.com/youtube/v3/guides/authentication
        type: Authentication
    description: Provides access to channel membership data, allowing channel owners to retrieve a list of paying members who support the channel in exchange for exclusive benefits.
  - aid: youtube:youtube-memberships-levels-api
    name: Youtube Memberships Levels API
    tags:
      - Members
      - Monetization
      - Videos
    image: https://www.youtube.com/img/desktop/yt_1200.png
    humanURL: https://developers.google.com/youtube/v3/docs/membershipsLevels
    baseURL: https://www.googleapis.com/youtube/v3
    properties:
      - url: https://developers.google.com/youtube/v3/docs/membershipsLevels
        type: Documentation
      - url: https://developers.google.com/youtube/v3/getting-started
        type: GettingStarted
      - url: https://developers.google.com/youtube/v3/guides/authentication
        type: Authentication
    description: Provides information about membership pricing tiers that a channel has set up, allowing retrieval of the levels that members can subscribe to.
  - aid: youtube:youtube-thumbnails-api
    name: Youtube Thumbnails API
    tags:
      - Thumbnails
      - Videos
    image: https://www.youtube.com/img/desktop/yt_1200.png
    humanURL: https://developers.google.com/youtube/v3/docs/thumbnails
    baseURL: https://www.googleapis.com/youtube/v3
    properties:
      - url: https://developers.google.com/youtube/v3/docs/thumbnails
        type: Documentation
      - url: https://developers.google.com/youtube/v3/getting-started
        type: GettingStarted
      - url: https://developers.google.com/youtube/v3/guides/authentication
        type: Authentication
    description: Manages custom video thumbnail images, enabling upload of a custom thumbnail image for a video that the authenticated user owns.
  - aid: youtube:youtube-watermarks-api
    name: Youtube Watermarks API
    tags:
      - Videos
      - Watermarks
    image: https://www.youtube.com/img/desktop/yt_1200.png
    humanURL: https://developers.google.com/youtube/v3/docs/watermarks
    baseURL: https://www.googleapis.com/youtube/v3
    properties:
      - url: https://developers.google.com/youtube/v3/docs/watermarks
        type: Documentation
      - url: https://developers.google.com/youtube/v3/getting-started
        type: GettingStarted
      - url: https://developers.google.com/youtube/v3/guides/authentication
        type: Authentication
    description: Manages images that display in the corner of a player during playback of a channel's videos, supporting upload and deletion of channel watermarks.
  - aid: youtube:youtube-video-categories-api
    name: Youtube Video Categories API
    tags:
      - Categories
      - Videos
    image: https://www.youtube.com/img/desktop/yt_1200.png
    humanURL: https://developers.google.com/youtube/v3/docs/videoCategories
    baseURL: https://www.googleapis.com/youtube/v3
    properties:
      - url: https://developers.google.com/youtube/v3/docs/videoCategories
        type: Documentation
      - url: https://developers.google.com/youtube/v3/getting-started
        type: GettingStarted
      - url: https://developers.google.com/youtube/v3/guides/authentication
        type: Authentication
      - url: openapi/youtube-data-api-openapi.yml
        type: OpenAPI
    description: Provides a list of categories that can be associated with YouTube videos, allowing retrieval of video categories available in a given region.
  - aid: youtube:youtube-video-abuse-report-reasons-api
    name: Youtube Video Abuse Report Reasons API
    tags:
      - Moderation
      - Videos
    image: https://www.youtube.com/img/desktop/yt_1200.png
    humanURL: https://developers.google.com/youtube/v3/docs/videoAbuseReportReasons
    baseURL: https://www.googleapis.com/youtube/v3
    properties:
      - url: https://developers.google.com/youtube/v3/docs/videoAbuseReportReasons
        type: Documentation
      - url: https://developers.google.com/youtube/v3/getting-started
        type: GettingStarted
      - url: https://developers.google.com/youtube/v3/guides/authentication
        type: Authentication
    description: Retrieves a list of reasons that can be used to report abusive videos, supporting programmatic submission of video abuse reports.
  - aid: youtube:youtube-i18n-languages-api
    name: Youtube I18n Languages API
    tags:
      - Localization
      - Videos
    image: https://www.youtube.com/img/desktop/yt_1200.png
    humanURL: https://developers.google.com/youtube/v3/docs/i18nLanguages
    baseURL: https://www.googleapis.com/youtube/v3
    properties:
      - url: https://developers.google.com/youtube/v3/docs/i18nLanguages
        type: Documentation
      - url: https://developers.google.com/youtube/v3/getting-started
        type: GettingStarted
      - url: https://developers.google.com/youtube/v3/guides/authentication
        type: Authentication
      - url: openapi/youtube-data-api-openapi.yml
        type: OpenAPI
    description: Returns a list of application languages that the YouTube website supports, providing the language codes and human-readable names for localization purposes.
  - aid: youtube:youtube-i18n-regions-api
    name: Youtube I18n Regions API
    tags:
      - Localization
      - Videos
    image: https://www.youtube.com/img/desktop/yt_1200.png
    humanURL: https://developers.google.com/youtube/v3/docs/i18nRegions
    baseURL: https://www.googleapis.com/youtube/v3
    properties:
      - url: https://developers.google.com/youtube/v3/docs/i18nRegions
        type: Documentation
      - url: https://developers.google.com/youtube/v3/getting-started
        type: GettingStarted
      - url: https://developers.google.com/youtube/v3/guides/authentication
        type: Authentication
      - url: openapi/youtube-data-api-openapi.yml
        type: OpenAPI
    description: Returns a list of content regions that the YouTube website supports, providing region codes and human-readable names used for region-specific content filtering.
  - aid: youtube:youtube-analytics-api
    name: YouTube Analytics API
    tags:
      - Analytics
      - Reporting
      - Videos
    image: https://www.youtube.com/img/desktop/yt_1200.png
    humanURL: https://developers.google.com/youtube/analytics
    baseURL: https://youtubeanalytics.googleapis.com/v2
    properties:
      - url: https://developers.google.com/youtube/analytics
        type: Documentation
      - url: https://developers.google.com/youtube/reporting/guides/authorization
        type: GettingStarted
      - url: https://developers.google.com/youtube/analytics/reference
        type: APIReference
      - url: https://developers.google.com/youtube/reporting/guides/authorization
        type: Authentication
      - url: https://developers.google.com/youtube/reporting/v1/code_samples
        type: CodeExamples
      - url: openapi/youtube-analytics-openapi.yml
        type: OpenAPI
    description: Generates custom reports containing YouTube Analytics data for channels and content owners. Reports can be filtered by dimensions such as date, country, and video, and measured by metrics including views, likes, and watch time.
  - aid: youtube:youtube-reporting-api
    name: YouTube Reporting API
    tags:
      - Analytics
      - Reporting
      - Videos
    image: https://www.youtube.com/img/desktop/yt_1200.png
    humanURL: https://developers.google.com/youtube/reporting
    baseURL: https://youtubereporting.googleapis.com
    properties:
      - url: https://developers.google.com/youtube/reporting
        type: Documentation
      - url: https://developers.google.com/youtube/reporting/guides/authorization
        type: GettingStarted
      - url: https://developers.google.com/youtube/reporting/v1/reference/rest
        type: APIReference
      - url: https://developers.google.com/youtube/reporting/guides/authorization
        type: Authentication
      - url: https://developers.google.com/youtube/reporting/v1/reports
        type: Documentation
      - url: https://developers.google.com/youtube/reporting/v1/code_samples
        type: CodeExamples
      - url: openapi/youtube-reporting-openapi.yml
        type: OpenAPI
    description: Retrieves bulk YouTube Analytics data through predefined reports for a channel or content owner. Reports are generated daily as CSV datasets covering 24-hour periods and are accessible for 30 to 60 days depending on the report type.
  - aid: youtube:youtube-live-streaming-api
    name: YouTube Live Streaming API
    tags:
      - Broadcasting
      - Live Streaming
      - Videos
    image: https://www.youtube.com/img/desktop/yt_1200.png
    humanURL: https://developers.google.com/youtube/v3/live/getting-started
    baseURL: https://www.googleapis.com/youtube/v3
    properties:
      - url: https://developers.google.com/youtube/v3/live/getting-started
        type: GettingStarted
      - url: https://developers.google.com/youtube/v3/live/docs
        type: Documentation
      - url: https://developers.google.com/youtube/v3/live/docs
        type: APIReference
      - url: https://developers.google.com/youtube/v3/guides/authentication
        type: Authentication
      - url: https://developers.google.com/youtube/v3/live/code_samples
        type: CodeExamples
      - url: https://developers.google.com/youtube/v3/live/support
        type: Support
      - url: openapi/youtube-live-streaming-openapi.yml
        type: OpenAPI
    description: Enables creating, updating, and managing live events on YouTube including scheduling broadcasts, linking video streams, managing live chat, and controlling ad insertion during live events. The API provides resources for liveBroadcasts, liveStreams, liveChatMessages, liveChatModerators, liveChatBans, and superChatEvents.
  - aid: youtube:youtube-iframe-player-api
    name: YouTube IFrame Player API
    tags:
      - Embed
      - Player
      - Videos
    image: https://www.youtube.com/img/desktop/yt_1200.png
    humanURL: https://developers.google.com/youtube/iframe_api_reference
    properties:
      - url: https://developers.google.com/youtube/iframe_api_reference
        type: Documentation
      - url: https://developers.google.com/youtube/iframe_api_reference#Getting_started
        type: GettingStarted
      - url: https://developers.google.com/youtube/player_parameters
        type: APIReference
    description: Enables embedding a YouTube video player on websites and controlling playback through JavaScript. The API supports queuing and playing videos, adjusting volume, retrieving video information, and subscribing to player state change events.
  - aid: youtube:youtube-subscribe-button
    name: YouTube Subscribe Button
    tags:
      - Embed
      - Videos
      - Widgets
    image: https://www.youtube.com/img/desktop/yt_1200.png
    humanURL: https://developers.google.com/youtube/subscribe
    properties:
      - url: https://developers.google.com/youtube/subscribe
        type: Documentation
      - url: https://developers.google.com/youtube/subscribe/reference
        type: APIReference
    description: Provides an embeddable subscribe button that website owners can configure and add to their pages, enabling one-click channel subscriptions for visitors without leaving the page.
  - aid: youtube:youtube-playlist-images-api
    name: Youtube Playlist Images API
    tags:
      - Images
      - Playlists
      - Videos
    image: https://www.youtube.com/img/desktop/yt_1200.png
    humanURL: https://developers.google.com/youtube/v3/docs/playlistImages
    baseURL: https://www.googleapis.com/youtube/v3
    properties:
      - url: https://developers.google.com/youtube/v3/docs/playlistImages
        type: Documentation
      - url: https://developers.google.com/youtube/v3/docs/playlistImages/list
        type: APIReference
      - url: https://developers.google.com/youtube/v3/getting-started
        type: GettingStarted
      - url: https://developers.google.com/youtube/v3/guides/authentication
        type: Authentication
    description: Manages thumbnail images associated with YouTube playlists, supporting retrieval, insertion, update, and deletion of custom playlist thumbnail images.
  - aid: youtube:youtube-content-id-api
    name: YouTube Content ID API
    tags:
      - Content ID
      - Monetization
      - Rights Management
      - Videos
    image: https://www.youtube.com/img/desktop/yt_1200.png
    humanURL: https://developers.google.com/youtube/partner
    baseURL: https://www.googleapis.com/youtube/partner/v1
    properties:
      - url: https://developers.google.com/youtube/partner
        type: Documentation
      - url: https://developers.google.com/youtube/partner/reference/rest
        type: APIReference
      - url: https://developers.google.com/youtube/partner/terms
        type: TermsOfService
    description: Enables YouTube content partners to interact with the rights management system, allowing creation and management of assets, content references, ownership data, claims, and policies for intellectual property on YouTube.
  - aid: youtube:youtube-oembed-api
    name: YouTube oEmbed API
    tags:
      - Embed
      - oEmbed
      - Videos
    image: https://www.youtube.com/img/desktop/yt_1200.png
    humanURL: https://oembed.com/
    baseURL: https://www.youtube.com/oembed
    properties:
      - url: https://oembed.com/
        type: Documentation
    description: Provides an oEmbed-compliant endpoint that returns embed code and metadata for YouTube videos in JSON or XML format, enabling easy embedding of YouTube content on external websites.
name: Youtube
tags:
  - Google
  - Media
  - Social
  - Streaming
  - Video
  - Videos
common:
  - url: https://developers.google.com/youtube/v3
    name: Portal
    type: Portal
  - url: https://developers.google.com/youtube/v3/getting-started
    name: Getting Started
    type: GettingStarted
  - url: https://developers.google.com/youtube/v3
    name: Documentation
    type: Documentation
  - url: https://developers.google.com/youtube/v3/getting-started
    name: Guides
    type: GettingStarted
  - url: https://developers.google.com/youtube/v3/code_samples
    name: Code Examples
    type: CodeExamples
  - url: https://developers.google.com/youtube/v3/support
    name: Support
    type: Support
  - url: https://developers.google.com/youtube/v3/libraries
    name: SDK
    type: SDK
  - url: https://developers.google.com/youtube/v3/guides/authentication
    name: Authentication
    type: Authentication
  - url: https://developers.google.com/youtube/v3/revision_history
    name: Change Log
    type: ChangeLog
  - url: https://developers.google.com/youtube/v3/determine_quota_cost
    name: Rate Limits
    type: RateLimits
  - url: https://github.com/youtube/api-samples
    name: GitHub Repository
    type: GitHubRepository
  - url: https://github.com/youtube
    name: GitHub Organization
    type: GitHubOrganization
  - url: https://www.youtube.com/user/YouTubeDev
    name: YouTube
    type: YouTube
  - url: https://developers.google.com/youtube/terms/api-services-terms-of-service
    name: Terms of Service
    type: TermsOfService
  - url: https://developers.google.com/youtube/terms/branding-guidelines
    name: Branding
    type: Branding
  - url: https://developers.google.com/youtube/terms/revision-history
    name: Change Log
    type: ChangeLog
  - url: https://issuetracker.google.com/issues?q=componentid:186600
    name: Support
    type: Support
  - url: https://stackoverflow.com/questions/tagged/youtube-api
    name: Stack Overflow
    type: StackOverflow
  - url: https://developers.google.com/youtube/registering_an_application
    name: Sign Up
    type: SignUp
  - url: https://developers.google.com/youtube/v3/docs
    name: API Reference
    type: APIReference
  - url: https://developers.google.com/youtube/v3/docs/errors
    name: Errors
    type: Errors
  - url: https://developers.google.com/youtube/terms/developer-policies
    name: Compliance
    type: Compliance
  - url: https://developers.google.com/youtube/v3/guides/quota_and_compliance_audits
    name: Compliance
    type: Compliance
  - url: https://developers.google.com/youtube/v3/guides/implementation
    name: Guides
    type: GettingStarted
  - url: https://x.com/YouTubeDev
    name: X
    type: X
  - url: https://developers.google.com/youtube/documentation/
    name: Documentation
    type: Documentation
  - url: https://status.cloud.google.com
    name: Status Page
    type: StatusPage
  - url: https://blog.youtube/news-and-events/
    name: Blog
    type: Blog
  - url: https://policies.google.com/privacy
    name: Privacy Policy
    type: PrivacyPolicy
  - url: https://github.com/youtube/geo-search-tool
    name: Geo Search Tool
    type: CodeExamples
  - url: https://github.com/youtube/youtube-ios-player-helper
    name: iOS Player Helper
    type: SDK
  - url: json-ld/youtube-context.jsonld
    name: JSON-LD
    type: JSONLD
  - url: json-ld/youtube-data-context.jsonld
    name: JSON-LD Data API
    type: JSONLD
  - url: json-ld/youtube-analytics-context.jsonld
    name: JSON-LD Analytics API
    type: JSONLD
  - url: json-ld/youtube-live-context.jsonld
    name: JSON-LD Live Streaming API
    type: JSONLD
  - url: json-ld/youtube-reporting-context.jsonld
    name: JSON-LD Reporting API
    type: JSONLD
  - url: json-schema/youtube-video-schema.json
    name: JSON Schema
    type: JSONSchema
  - url: json-schema/youtube-channel-schema.json
    name: JSON Schema
    type: JSONSchema
  - url: rules/youtube-spectral-rules.yml
    name: Spectral Rules
    type: SpectralRules
  - url: vocabulary/youtube-vocabulary.yaml
    name: Vocabulary
    type: Vocabulary
  - url: capabilities/content-management.yaml
    name: Content Management Capability
    type: NaftikoCapability
  - url: capabilities/community-engagement.yaml
    name: Community Engagement Capability
    type: NaftikoCapability
  - url: capabilities/live-streaming.yaml
    name: Live Streaming Capability
    type: NaftikoCapability
  - url: capabilities/analytics-and-reporting.yaml
    name: Analytics And Reporting Capability
    type: NaftikoCapability
  - data:
      - id: free
        name: Free
        entries:
          - geo: US
            unit: 1
            label: User
            limit: 1
            price: Free
            metric: user
            timeFrame: month
            description: Free tier.
        description: Youtube has only free tier.
    name: Plans
    type: Plans
  - url: https://developers.google.com/youtube/v3/determine_quota_cost
    data:
      - cost: 1
        name: Rate Limits
        rate: credit
        type: Type of Rate Limits
        limit: 200
        metric: request
        domains:
          - googleapis.com
        timeframe: hours
        operations:
          - getActivities
          - getChannels
          - getChannelSections
          - getComments
          - getCommentThreads
          - getGuideChategories
          - getI18nLanguages
          - getI18nRegions
          - getMemebers
          - getMembershipLevels
          - getPlayListItems
          - getPlayLists
          - getSubscriptions
          - getvideoAbuseReportReasons
          - getVideoCategories
          - getVideos
        description: This is a description of these rate limits.
        userMultiplied: true
    name: Rate Limits
    type: RateLimits
    description: The single credit cost rate limits operations.
  - name: Features
    type: Features
    data:
      - 'YouTube (Google): hundreds of services across Video Platform'
      - 'Detailed pricing: see https://developers.google.com/youtube/v3/getting-started'
      - 'Service: YouTube Data API v3 (free, quota-limited at 10K units/day)'
      - 'Service: YouTube Live Streaming API'
      - 'Service: YouTube Analytics API'
      - 'Service: YouTube Reporting API'
      - 'Service: YouTube Player API'
      - 'Service: YouTube oEmbed'
      - 'Service: Google Cloud quota increases via cloud console'
    sources:
      - https://developers.google.com/youtube/v3/getting-started
      - https://focus.finops.org/
    updated: '2026-05-04'
  - name: Use Cases
    type: UseCases
    data:
      - name: Video Publishing Platform
        description: Build automated video upload and management workflows for content creators and media companies.
      - name: Social Media Dashboard
        description: Aggregate YouTube analytics with other social platforms for unified performance monitoring.
      - name: Content Moderation
        description: Automate comment moderation and abuse reporting for community management at scale.
      - name: Live Event Management
        description: Schedule and manage live streaming events with real-time chat and audience interaction.
      - name: Education Platform
        description: Organize educational video content into playlists with searchable course catalogs.
      - name: Digital Rights Management
        description: Track and manage content ownership, claims, and monetization policies using Content ID.
      - name: Video Search Application
        description: Build custom video search experiences with filters for topics, dates, and regions.
      - name: Analytics Dashboard
        description: Create custom reporting dashboards with channel and video performance metrics.
      - name: Accessibility Tools
        description: Manage captions and translations to improve video accessibility across languages.
      - name: Embedded Video Experience
        description: Create branded video experiences with customized embedded players on external websites.
  - name: Integrations
    type: Integrations
    data:
      - name: Google Cloud Platform
        description: Integrates with GCP for authentication, hosting, and infrastructure services.
      - name: Google Analytics
        description: Combine YouTube Analytics data with Google Analytics for comprehensive web and video metrics.
      - name: Google Ads
        description: Connect YouTube content with Google Ads for video advertising campaigns.
      - name: Firebase
        description: Use Firebase with YouTube APIs for mobile app development with video features.
      - name: Google Workspace
        description: Embed YouTube videos in Google Docs, Slides, and Sites for collaborative content.
created: '2025-07-29'
modified: '2026-05-04'
description: YouTube APIs provide programmatic access to YouTube data including videos, playlists, channels, user interactions, live streaming, analytics, captions, and embedded player controls.
maintainers:
  - FN: Kin Lane
    url: https://apievangelist.com
    email: kin@apievangelist.com
specificationVersion: '0.20'
image: https://www.youtube.com/img/desktop/yt_1200.png
---
