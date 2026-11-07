---
access_model:
  confidence: high
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
  - scopes
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: false
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 35.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 120
  human_in_the_loop: 0
  name: Wistia Agentic Access
  operation_count: 221
  slug: wistia-agentic-access
  summary_line: 221 operations · 120 acting
api_count: 4
apis:
- description: Wistia's first-party hosted Model Context Protocol server, exposing 125 tools across the media, folders, channels, captions, customizations, tags, webinars, sharing, account, analytics, stats and remi
  name: Wistia MCP Server
  slug: mcp
- description: Endpoint for uploading video files directly to a Wistia account, typically used in conjunction with the Data API to manage uploaded media. Authentication uses the same API access token.
  name: Wistia Upload API
  slug: upload-api
- description: Real-time webhook deliveries from Wistia for documented media lifecycle events. Deliveries are HTTP POST with a JSON body and are signed via HMAC-SHA256 using the consumer's configured webhook secret,
  name: Wistia Webhooks
  slug: webhooks
- baseURL: https://api.wistia.com/v1
  baseurl_source: declared
  description: The Account API from Wistia — 1 operation(s) for account.
  name: Wistia Account API
  phrasing_intents:
  - id: getAccountDetails
    intent: View my account summary
    question: What is the name, description and URL of my Wistia account?
  - id: getAccountUsage
    intent: Check plan usage and limits
    question: How close am I to my plan's storage and bandwidth limits?
  - id: getTokenDetails
    intent: Inspect the current API token
    question: Why is my API request getting a permission error?
  phrasing_ops: 3
  slug: wistia-account-api
- baseURL: https://api.wistia.com/v1
  baseurl_source: declared
  description: The Captions API from Wistia — 3 operation(s) for captions.
  name: Wistia Captions API
  phrasing_intents:
  - id: getMediasByMediaHashedIdCaptions
    intent: List a video's captions
    question: Which caption languages does this video already have?
  - id: postMediasByMediaHashedIdCaptions
    intent: Add captions to a video
    question: How do I upload my own caption file to a video?
  - id: getCaptions
    intent: List captions across my account
    question: Which captions exist across all the videos in my account?
  - id: postMediasByMediaHashedIdCaptionsPurchase
    intent: Order professional captions
    question: Can I pay Wistia to caption a video for me?
  - id: getMediasByMediaHashedIdCaptionsByLanguageCode
    intent: Show captions in one language
    question: How do I get the Spanish captions text for a specific video?
  - id: putMediasByMediaHashedIdCaptionsByLanguageCode
    intent: Replace captions in one language
    question: How do I fix a typo in a video's existing captions?
  - id: deleteMediasByMediaHashedIdCaptionsByLanguageCode
    intent: Delete captions in one language
    question: How do I remove a caption language from a video?
  - id: postMediasByMediaHashedIdCaptionsByLanguageCodeEdits
    intent: Correct words in a caption transcript
    question: Can I fix a few misspelled words in a transcript without re-uploading the caption file?
  phrasing_ops: 15
  slug: wistia-captions-api
- baseURL: https://api.wistia.com/v1
  baseurl_source: declared
  description: The Channels API from Wistia — 2 operation(s) for channels.
  name: Wistia Channels API
  phrasing_intents:
  - id: getChannels
    intent: List my channels
    question: What channels do I have in my account?
  - id: postChannels
    intent: Create a channel
    question: Can I create a new channel for my videos?
  - id: getChannelsByChannelHashedId
    intent: Show a channel
    question: What settings and details does one of my channels have?
  - id: putChannelsByChannelHashedId
    intent: Update a channel
    question: How do I rename or edit one of my channels?
  - id: deleteChannelsByChannelHashedId
    intent: Delete a channel
    question: How do I permanently remove a channel?
  - id: getChannel
    intent: Show a channel via the legacy route
    question: Does the older hashed-ID channel route still return a single channel?
  - id: updateChannel
    intent: Update a channel via the legacy route
    question: Can I still update a channel through the legacy hashed-ID route?
  - id: deleteChannel
    intent: Delete a channel via the legacy route
    question: Can the legacy hashed-ID route still delete a channel?
  phrasing_ops: 8
  slug: wistia-channels-api
- baseURL: https://api.wistia.com/v1
  baseurl_source: declared
  description: The Customizations API from Wistia — 1 operation(s) for customizations.
  name: Wistia Customizations API
  phrasing_intents:
  - id: getMediasByMediaIdCustomizations
    intent: Show a video's player customizations
    question: What player customizations are applied to a specific video?
  - id: postMediasByMediaIdCustomizations
    intent: Set player customizations on a video
    question: How do I customize the player for a video that uses the defaults?
  - id: putMediasByMediaIdCustomizations
    intent: Change a video's player customizations
    question: How do I tweak the player settings already customized on a video?
  - id: deleteMediasByMediaIdCustomizations
    intent: Reset a video's player customizations
    question: How do I reset a video's player back to the account defaults?
  - id: getMediasByMediaIdCustomizationsAppearance
    intent: Show a video's appearance customizations
    question: What player color, rounded corners and logo settings are set on a video?
  - id: putMediasByMediaIdCustomizationsAppearance
    intent: Update a video's player appearance
    question: Can I change the player color and add a gradient on just one video?
  - id: getMediasByMediaIdCustomizationsPlayback
    intent: Show a video's playback customizations
    question: Is autoplay or mute turned on for a particular video?
  - id: putMediasByMediaIdCustomizationsPlayback
    intent: Update a video's playback settings
    question: Can I make one video autoplay muted?
  phrasing_ops: 28
  slug: wistia-customizations-api
- baseURL: https://api.wistia.com/v1
  baseurl_source: declared
  description: The Folders API from Wistia — 3 operation(s) for folders.
  name: Wistia Folders API
  phrasing_intents:
  - id: getFolders
    intent: List folders
    question: What folders do I have in my Wistia account?
  - id: postFolders
    intent: Create a folder
    question: How do I make a new folder for my videos?
  - id: getFoldersById
    intent: Show a folder
    question: How do I get the details of one folder?
  - id: putFoldersById
    intent: Update a folder
    question: How do I rename a folder or change its description?
  - id: deleteFoldersById
    intent: Delete a folder
    question: How do I delete a folder I no longer need?
  - id: postFoldersByIdCopy
    intent: Copy a folder with its media
    question: How do I duplicate a folder along with all its media and subfolders?
  phrasing_ops: 6
  slug: wistia-folders-api
- baseURL: https://api.wistia.com/v1
  baseurl_source: declared
  description: The Medias API from Wistia — 8 operation(s) for medias.
  name: Wistia Medias API
  phrasing_intents:
  - id: listMedia
    intent: List my media
    question: What videos do I have in my account?
  - id: createMedia
    intent: Upload or import media
    question: How do I upload a new video to Wistia?
  - id: getMedia
    intent: Retrieve a media item
    question: How do I look up the details of a single video?
  - id: updateMedia
    intent: Update a media item
    question: How do I rename a video or edit its description?
  - id: deleteMedia
    intent: Delete a media item
    question: How do I permanently delete a video?
  - id: copyMedia
    intent: Duplicate one media item
    question: How do I make a copy of one video?
  - id: swapMedia
    intent: Swap a video's source file
    question: How do I replace a video's file but keep its embed codes and stats?
  - id: moveMedia
    intent: Move several media items
    question: How do I move a batch of videos into a different project?
  phrasing_ops: 11
  slug: wistia-medias-api
- baseURL: https://api.wistia.com/v1
  baseurl_source: declared
  description: The Tags API from Wistia — 3 operation(s) for tags.
  name: Wistia Tags API
  phrasing_intents:
  - id: getTags
    intent: List my tags
    question: What tags exist in my account?
  - id: postTags
    intent: Create a tag
    question: Can I create a new tag to organize my videos?
  - id: deleteTagsByName
    intent: Delete a tag
    question: Can I delete a tag I no longer use?
  - id: bulkCreateTaggings
    intent: Tag many media at once
    question: How do I add tags to several videos at once?
  phrasing_ops: 4
  slug: wistia-tags-api
- baseURL: https://api.wistia.com/v1
  baseurl_source: declared
  description: The Tokens API from Wistia — 1 operation(s) for tokens.
  name: Wistia Tokens API
  phrasing_intents:
  - id: getCurrentToken
    intent: Show current API token details
    question: What scopes and permissions does my current API token have?
  phrasing_ops: 1
  slug: wistia-tokens-api
- baseURL: https://api.wistia.com/v1
  baseurl_source: declared
  description: The Webinars API from Wistia — 3 operation(s) for webinars.
  name: Wistia Webinars API
  phrasing_intents:
  - id: getWebinars
    intent: List my webinars
    question: What webinars have I set up?
  - id: postWebinars
    intent: Schedule a new webinar
    question: Can I schedule a new webinar?
  - id: getWebinarsById
    intent: Show a webinar
    question: What are the details of one of my webinars?
  - id: putWebinarsById
    intent: Update a webinar
    question: Can I reschedule or retitle an existing webinar?
  - id: deleteWebinarsById
    intent: Delete a webinar
    question: Can I delete a webinar I no longer need?
  - id: registerWebinar
    intent: Register someone for a webinar
    question: How do I sign someone up for one of my webinars?
  phrasing_ops: 6
  slug: wistia-webinars-api
- baseURL: https://api.wistia.com/v1
  baseurl_source: declared
  description: The Allowed Domains API from Wistia — 2 operation(s) for allowed domains.
  name: Wistia Allowed Domains API
  phrasing_intents:
  - id: getAllowedDomains
    intent: List allowed embed domains
    question: Can I page through and sort my account's allowed domains?
  - id: postAllowedDomains
    intent: Permit a domain to embed my media
    question: Can I permit a specific website to show my videos?
  - id: getAllowedDomainsByDomain
    intent: Look up one allowed domain
    question: Is a specific website currently permitted on my allowed-domains list?
  - id: deleteAllowedDomainsByDomain
    intent: Revoke an allowed domain
    question: Can I revoke a website's permission to play my embeds?
  - id: listAllowedDomains
    intent: List allowed domains
    question: Which domains are allowed to embed my videos?
  - id: createAllowedDomain
    intent: Add an allowed domain
    question: How do I restrict my videos so they only play on my own website?
  - id: getAllowedDomain
    intent: Show one allowed domain
    question: Is a particular domain already on my embed allowlist?
  - id: deleteAllowedDomain
    intent: Remove an allowed domain
    question: How do I stop a website from embedding my videos?
  phrasing_ops: 8
  slug: wistia-allowed-domains-api
- baseURL: https://api.wistia.com/v1
  baseurl_source: declared
  description: The Analytics:Account API from Wistia — 4 operation(s) for analytics:account.
  name: Wistia Analytics:Account API
  phrasing_intents:
  - id: getAnalyticsAccount
    intent: Show account-wide analytics
    question: How many plays did my whole account get last month?
  - id: getAnalyticsAccountTimeseries
    intent: Chart account analytics over time
    question: How did my account's plays trend day by day over the last quarter?
  - id: getAnalyticsAccountTopContent
    intent: Rank my top-performing content
    question: What were my most-watched videos last month?
  - id: getAnalyticsAccountEmbedLocations
    intent: See where my account's videos are embedded
    question: Which websites embed my videos the most?
  phrasing_ops: 4
  slug: wistia-analytics-account-api
- baseURL: https://api.wistia.com/v1
  baseurl_source: declared
  description: The Analytics:Media API from Wistia — 7 operation(s) for analytics:media.
  name: Wistia Analytics:Media API
  phrasing_intents:
  - id: getAnalyticsMediasByMediaId
    intent: Show a video's analytics
    question: How many plays did one video get over a date range?
  - id: getAnalyticsMediasByMediaIdTimeseries
    intent: Chart a video's analytics over time
    question: How have a video's plays trended day by day?
  - id: getAnalyticsMediasByMediaIdEmbedLocations
    intent: See where a video is embedded
    question: Which pages is one of my videos embedded on?
  - id: getAnalyticsMediasByMediaIdEmbedLocationsTimeseries
    intent: Chart a video's embed locations over time
    question: How have plays on each embed page of a video changed over time?
  - id: getAnalyticsMediasByMediaIdTraffic
    intent: Break down a video's traffic sources
    question: Which UTM campaigns drove views to a video?
  - id: getAnalyticsMediasByMediaIdConversions
    intent: List a video's form conversions
    question: Who filled out the form on one of my videos?
  - id: getAnalyticsMediasByMediaIdLanguages
    intent: Break down a video's plays by viewer language
    question: What browser languages are my viewers using on a video?
  phrasing_ops: 7
  slug: wistia-analytics-media-api
- baseURL: https://api.wistia.com/v1
  baseurl_source: declared
  description: The Analytics:Webinar API from Wistia — 5 operation(s) for analytics:webinar.
  name: Wistia Analytics:Webinar API
  phrasing_intents:
  - id: getAnalyticsWebinarsByWebinarId
    intent: Show a webinar's analytics
    question: How many people registered for and attended a webinar?
  - id: getAnalyticsWebinarsByWebinarIdRegistration
    intent: Chart a webinar's registrations over time
    question: How did registrations for a webinar build up over time?
  - id: getAnalyticsWebinarsByWebinarIdTraffic
    intent: Break down a webinar's traffic sources
    question: Which UTM sources drove registrations to a webinar?
  - id: getAnalyticsWebinarsByWebinarIdAudience
    intent: List a webinar's audience
    question: Who attended a webinar and how engaged were they?
  - id: getAnalyticsWebinarsByWebinarIdHistograms
    intent: Get a webinar's engagement histograms
    question: When during a webinar was chat activity highest?
  phrasing_ops: 5
  slug: wistia-analytics-webinar-api
- baseURL: https://api.wistia.com/v1
  baseurl_source: declared
  description: The Background Job Status API from Wistia — 1 operation(s) for background job status.
  name: Wistia Background Job Status API
  phrasing_intents:
  - id: getBackgroundJobStatusByBackgroundJobStatusId
    intent: Check the status of a background job
    question: How can I tell whether a Wistia bulk job or folder copy has finished?
  phrasing_ops: 1
  slug: wistia-background-job-status-api
- baseURL: https://api.wistia.com/v1
  baseurl_source: declared
  description: The Brands API from Wistia — 1 operation(s) for brands.
  name: Wistia Brands API
  phrasing_intents:
  - id: getBrands
    intent: List the account's brands
    question: Which saved brands with colors, fonts and logos does my Wistia account have?
  phrasing_ops: 1
  slug: wistia-brands-api
- baseURL: https://api.wistia.com/v1
  baseurl_source: declared
  description: The Bulk Actions API from Wistia — 1 operation(s) for bulk actions.
  name: Wistia Bulk Actions API
  phrasing_intents:
  - id: postBulk
    intent: Submit a batch of bulk actions
    question: How do I create, update, move or delete up to 1000 Wistia records in one request?
  phrasing_ops: 1
  slug: wistia-bulk-actions-api
- baseURL: https://api.wistia.com/v1
  baseurl_source: declared
  description: The Channel Collaborators API from Wistia — 2 operation(s) for channel collaborators.
  name: Wistia Channel Collaborators API
  phrasing_intents:
  - id: getChannelsByChannelHashedIdCollaborators
    intent: List a channel's collaborators
    question: Who has been given access to collaborate on this channel?
  - id: postChannelsByChannelHashedIdCollaborators
    intent: Invite a collaborator to a channel
    question: How do I invite someone by email to collaborate on a channel?
  - id: deleteChannelsByChannelHashedIdCollaboratorsById
    intent: Remove a collaborator from a channel
    question: How do I revoke a collaborator's access to a channel?
  phrasing_ops: 3
  slug: wistia-channel-collaborators-api
- baseURL: https://api.wistia.com/v1
  baseurl_source: declared
  description: The Channel Episodes API from Wistia — 6 operation(s) for channel episodes.
  name: Wistia Channel Episodes API
  phrasing_intents:
  - id: getChannelsByChannelHashedIdChannelEpisodesByChannelEpisodeId
    intent: Show one episode within a channel
    question: How do I look up a single episode by its id inside a specific channel?
  - id: getChannelsByChannelHashedIdChannelEpisodes
    intent: List the episodes of one channel
    question: What episodes are in this particular channel?
  - id: postChannelsByChannelHashedIdChannelEpisodes
    intent: Add a new episode to a channel
    question: How do I add a video as a new episode in my Wistia channel?
  - id: getChannelEpisodes
    intent: List channel episodes across the account
    question: How do I list every channel episode across all my channels?
  - id: putChannelEpisodesByChannelEpisodeHashedId
    intent: Update a channel episode
    question: How do I change the title or description of an existing episode?
  - id: deleteChannelEpisodesByChannelEpisodeHashedId
    intent: Delete a channel episode
    question: How do I permanently delete an episode from a channel?
  - id: putChannelEpisodesByChannelEpisodeHashedIdPublish
    intent: Publish a channel episode
    question: How do I make a draft episode live on my channel?
  - id: putChannelEpisodesByChannelEpisodeHashedIdUnpublish
    intent: Unpublish a channel episode
    question: How do I take an episode off my channel without deleting it?
  phrasing_ops: 8
  slug: wistia-channel-episodes-api
- baseURL: https://api.wistia.com/v1
  baseurl_source: declared
  description: The Custom Metadata Field Definitions API from Wistia — 3 operation(s) for custom metadata field definitions.
  name: Wistia Custom Metadata Field Definitions API
  phrasing_intents:
  - id: getCustomMetadataFieldDefinitions
    intent: List custom metadata field definitions
    question: What custom metadata fields are defined in my Wistia account?
  - id: postCustomMetadataFieldDefinitions
    intent: Define a new custom metadata field
    question: How do I add a new custom metadata field for my videos?
  - id: getCustomMetadataFieldDefinitionsByKey
    intent: Show a custom metadata field definition
    question: How do I see the type and options of one custom metadata field?
  - id: putCustomMetadataFieldDefinitionsByKey
    intent: Update a custom metadata field definition
    question: Can I relabel a custom metadata field without changing its key?
  - id: deleteCustomMetadataFieldDefinitionsByKey
    intent: Archive a custom metadata field definition
    question: How do I retire a custom metadata field I no longer use?
  - id: postCustomMetadataFieldDefinitionsByKeyRestore
    intent: Restore an archived metadata field definition
    question: How do I bring back a custom metadata field I archived?
  phrasing_ops: 6
  slug: wistia-custom-metadata-field-definitions-api
- baseURL: https://api.wistia.com/v1
  baseurl_source: declared
  description: The Custom Metadata Field Values API from Wistia — 2 operation(s) for custom metadata field values.
  name: Wistia Custom Metadata Field Values API
  phrasing_intents:
  - id: getMediasByMediaHashedIdCustomMetadataFieldValues
    intent: List a media's custom metadata values
    question: What custom metadata values are set on this video?
  - id: putMediasByMediaHashedIdCustomMetadataFieldValuesByKey
    intent: Set a custom metadata value on a media
    question: How do I set or replace a custom metadata value on a video?
  - id: deleteMediasByMediaHashedIdCustomMetadataFieldValuesByKey
    intent: Clear a custom metadata value on a media
    question: How do I blank out a custom metadata value on a video?
  - id: getMediasByMediaHashedIdCustomMetadataFieldValuesByKey
    intent: Get one custom metadata value on a media
    question: How do I read a single custom metadata field's value on a video?
  phrasing_ops: 4
  slug: wistia-custom-metadata-field-values-api
- baseURL: https://api.wistia.com/v1
  baseurl_source: declared
  description: The Deleted Media API from Wistia — 2 operation(s) for deleted media.
  name: Wistia Deleted Media API
  phrasing_intents:
  - id: getDeletedMedia
    intent: List deleted media that can be restored
    question: Which videos are in the trash and still recoverable?
  - id: postDeletedMediaRestore
    intent: Restore deleted media
    question: How do I undelete a video I removed by mistake?
  phrasing_ops: 2
  slug: wistia-deleted-media-api
- baseURL: https://api.wistia.com/v1
  baseurl_source: declared
  description: The Expiring Access Tokens API from Wistia — 1 operation(s) for expiring access tokens.
  name: Wistia Expiring Access Tokens API
  phrasing_intents:
  - id: postExpiringToken
    intent: Create an expiring access token
    question: How do I generate a short-lived token for an iframe embed?
  phrasing_ops: 1
  slug: wistia-expiring-access-tokens-api
- baseURL: https://api.wistia.com/v1
  baseurl_source: declared
  description: The Extended Audio Descriptions API from Wistia — 4 operation(s) for extended audio descriptions.
  name: Wistia Extended Audio Descriptions API
  phrasing_intents:
  - id: getMediaExtendedAudioDescriptions
    intent: List extended audio descriptions
    question: Which extended audio descriptions exist in my account?
  - id: getMediaExtendedAudioDescriptionsById
    intent: Show an extended audio description
    question: How do I get the download links for an extended audio description?
  - id: deleteMediaExtendedAudioDescriptionsById
    intent: Delete an extended audio description
    question: How do I remove an extended audio description from my account?
  - id: postMediaExtendedAudioDescriptionsOrder
    intent: Order an extended audio description
    question: How do I order an extended audio description for a video?
  - id: getMediaExtendedAudioDescriptionsOrderStatusById
    intent: Check an audio description order's status
    question: Is my extended audio description order ready yet?
  phrasing_ops: 5
  slug: wistia-extended-audio-descriptions-api
- baseURL: https://api.wistia.com/v1
  baseurl_source: declared
  description: The Folder Sharings API from Wistia — 2 operation(s) for folder sharings.
  name: Wistia Folder Sharings API
  phrasing_intents:
  - id: getFoldersByFolderIdSharings
    intent: List who a folder is shared with
    question: Who has this folder been shared with?
  - id: postFoldersByFolderIdSharings
    intent: Share a folder with someone
    question: How do I share a folder with a colleague by email?
  - id: getFoldersByFolderIdSharingsBySharingId
    intent: Show one folder sharing
    question: What permissions does a specific folder sharing grant?
  - id: putFoldersByFolderIdSharingsBySharingId
    intent: Change a folder sharing
    question: How do I change what someone can do in a folder I shared?
  - id: deleteFoldersByFolderIdSharingsBySharingId
    intent: Stop sharing a folder with someone
    question: How do I remove someone's access to a shared folder?
  phrasing_ops: 5
  slug: wistia-folder-sharings-api
- baseURL: https://api.wistia.com/v1
  baseurl_source: declared
  description: The Live Stream Event Registrations API from Wistia — 1 operation(s) for live stream event registrations.
  name: Wistia Live Stream Event Registrations API
  phrasing_intents:
  - id: postLiveStreamEventsByLiveStreamEventIdRegistrations
    intent: Register a person for a live event
    question: How do I sign someone up for a Wistia live event?
  phrasing_ops: 1
  slug: wistia-live-stream-event-registrations-api
- baseURL: https://api.wistia.com/v1
  baseurl_source: declared
  description: The Live Stream Events API from Wistia — 2 operation(s) for live stream events.
  name: Wistia Live Stream Events API
  phrasing_intents:
  - id: getLiveStreamEvents
    intent: List live stream events
    question: What live stream events are set up in my account?
  - id: postLiveStreamEvents
    intent: Create a live stream event
    question: How do I schedule a new live stream event?
  - id: getLiveStreamEventsById
    intent: Show a live stream event
    question: How do I get the details of one live stream event?
  - id: putLiveStreamEventsById
    intent: Update a live stream event
    question: How do I change the details of a live event I already scheduled?
  - id: deleteLiveStreamEventsById
    intent: Delete a live stream event
    question: How do I cancel and delete a live stream event?
  phrasing_ops: 5
  slug: wistia-live-stream-events-api
- baseURL: https://api.wistia.com/v1
  baseurl_source: declared
  description: The Localizations API from Wistia — 2 operation(s) for localizations.
  name: Wistia Localizations API
  phrasing_intents:
  - id: getMediasByMediaHashedIdLocalizations
    intent: List a media's localizations
    question: Which languages has this video been localized into?
  - id: postMediasByMediaHashedIdLocalizations
    intent: Localize a media into another language
    question: How do I translate a Wistia video into another language?
  - id: getMediasByMediaHashedIdLocalizationsByLocalizationHashedId
    intent: Show one localization of a media
    question: How do I see the details of one specific localization?
  - id: deleteMediasByMediaHashedIdLocalizationsByLocalizationHashedId
    intent: Delete a localization
    question: How do I remove a language localization from a video?
  phrasing_ops: 4
  slug: wistia-localizations-api
- baseURL: https://api.wistia.com/v1
  baseurl_source: declared
  description: The Media API from Wistia — 11 operation(s) for media.
  name: Wistia Media API
  phrasing_intents:
  - id: getMedias
    intent: List my media
    question: What videos do I have in my account?
  - id: getMediasByMediaHashedId
    intent: Retrieve a media item
    question: How do I look up the details of a single video?
  - id: putMediasByMediaHashedId
    intent: Update a media item
    question: How do I rename a video or edit its description?
  - id: deleteMediasByMediaHashedId
    intent: Delete a media item
    question: How do I permanently delete a video?
  - id: postMediasByMediaHashedIdCopy
    intent: Duplicate one media item
    question: How do I make a copy of one video?
  - id: putMediasByMediaHashedIdSwap
    intent: Swap a video's source file
    question: How do I replace a video's file but keep its embed codes and stats?
  - id: getMediasByMediaHashedIdStats
    intent: Show a video's aggregated stats
    question: How many plays and visitors has one of my videos had overall?
  - id: postMediasByMediaHashedIdTranslate
    intent: Translate a video's transcript
    question: Can I translate a video's transcript into another language?
  phrasing_ops: 13
  slug: wistia-media-api
- baseURL: https://api.wistia.com/v1
  baseurl_source: declared
  description: The Project Sharings API from Wistia — 2 operation(s) for project sharings.
  name: Wistia Project Sharings API
  phrasing_intents:
  - id: getProjectsByProjectIdSharings
    intent: List who a project is shared with
    question: Who has access to this Wistia project?
  - id: postProjectsByProjectIdSharings
    intent: Share a project with someone
    question: How do I share a project with a colleague by email?
  - id: getProjectsByProjectIdSharingsBySharingId
    intent: Show one project sharing
    question: What permissions does a specific project sharing grant?
  - id: putProjectsByProjectIdSharingsBySharingId
    intent: Change a project sharing
    question: How do I change what someone can do in a project I shared?
  - id: deleteProjectsByProjectIdSharingsBySharingId
    intent: Stop sharing a project with someone
    question: How do I revoke someone's access to a shared project?
  phrasing_ops: 5
  slug: wistia-project-sharings-api
- baseURL: https://api.wistia.com/v1
  baseurl_source: declared
  description: The Projects API from Wistia — 3 operation(s) for projects.
  name: Wistia Projects API
  phrasing_intents:
  - id: getProjects
    intent: List projects
    question: What projects are in my Wistia account?
  - id: postProjects
    intent: Create a project
    question: How do I create a new project for my videos?
  - id: getProjectsById
    intent: Show a project and its media
    question: How do I see a project and the media inside it?
  - id: putProjectsById
    intent: Update a project
    question: How do I rename a project or change its description?
  - id: deleteProjectsById
    intent: Delete a project
    question: How do I delete a project I'm done with?
  - id: postProjectsByIdCopy
    intent: Copy a project
    question: How do I duplicate an existing project?
  phrasing_ops: 6
  slug: wistia-projects-api
- baseURL: https://api.wistia.com/v1
  baseurl_source: declared
  description: The Push Devices API from Wistia — 2 operation(s) for push devices.
  name: Wistia Push Devices API
  phrasing_intents:
  - id: postDevices
    intent: Register a device for push notifications
    question: How do I register a device to get push notifications about comments and views?
  - id: deleteDevicesByDeviceToken
    intent: Unregister a push notification device
    question: How do I stop push notifications going to a device?
  phrasing_ops: 2
  slug: wistia-push-devices-api
- baseURL: https://api.wistia.com/v1
  baseurl_source: declared
  description: The Remix API from Wistia — 5 operation(s) for remix.
  name: Wistia Remix API
  phrasing_intents:
  - id: postRemixes
    intent: Start an AI video remix
    question: How do I use AI to remix my videos into a new edit?
  - id: getRemixesByRemixHashedId
    intent: Check a remix job's status
    question: Is my remix ready to preview yet?
  - id: postRemixesByRemixHashedIdContinue
    intent: Send a follow-up edit to a remix
    question: How do I ask for changes to a remix I already made?
  - id: postRemixesByRemixHashedIdExport
    intent: Export a finished remix to a folder
    question: How do I render a finished remix into a real video in my account?
  - id: getRemixAccountStatus
    intent: Check remix credit usage and limits
    question: How many remix credits have I used this period?
  phrasing_ops: 5
  slug: wistia-remix-api
- baseURL: https://api.wistia.com/v1
  baseurl_source: declared
  description: The Resource URLs API from Wistia — 1 operation(s) for resource urls.
  name: Wistia Resource URLs API
  phrasing_intents:
  - id: getResourceUrls
    intent: Get the app link for a resource
    question: How do I turn a hashed id into a link I can open in the Wistia app?
  phrasing_ops: 1
  slug: wistia-resource-urls-api
- baseURL: https://api.wistia.com/v1
  baseurl_source: declared
  description: The Review Bundles API from Wistia — 2 operation(s) for review bundles.
  name: Wistia Review Bundles API
  phrasing_intents:
  - id: getReviewBundles
    intent: List review bundles
    question: What review bundles have I shared for feedback?
  - id: postReviewBundles
    intent: Create a review bundle
    question: How do I share several videos for review under one link?
  - id: deleteReviewBundlesByReviewBundleHashedId
    intent: Delete a review bundle
    question: How do I take down a review link I shared?
  phrasing_ops: 3
  slug: wistia-review-bundles-api
- baseURL: https://api.wistia.com/v1
  baseurl_source: declared
  description: The Search API from Wistia — 1 operation(s) for search.
  name: Wistia Search API
  phrasing_intents:
  - id: getSearch
    intent: Search across the account's content
    question: How do I search my videos, folders, channels and webinars at once?
  phrasing_ops: 1
  slug: wistia-search-api
- baseURL: https://api.wistia.com/v1
  baseurl_source: declared
  description: The Share Links API from Wistia — 2 operation(s) for share links.
  name: Wistia Share Links API
  phrasing_intents:
  - id: getShareLinksByIdentifier
    intent: Resolve a share link to its media
    question: Which video does a given /s/ share link point to?
  - id: getMediasByMediaIdShareLink
    intent: Get a media's share link
    question: How do I get the share link for a video?
  - id: putMediasByMediaIdShareLink
    intent: Change a media share link's visibility
    question: How do I change who can open a video's share link?
  - id: deleteMediasByMediaIdShareLink
    intent: Revoke a media's share link
    question: How do I revoke a share link so the old URL stops working?
  phrasing_ops: 4
  slug: wistia-share-links-api
- baseURL: https://api.wistia.com/v1
  baseurl_source: declared
  description: The Stats:Account API from Wistia — 2 operation(s) for stats:account.
  name: Wistia Stats:Account API
  phrasing_intents:
  - id: getStatsAccount
    intent: Get account-wide video stats
    question: How many loads, plays and hours watched does my whole account have?
  - id: getStatsAccountByDate
    intent: Get account stats day by day
    question: How did my account's plays change day by day last month?
  phrasing_ops: 2
  slug: wistia-stats-account-api
- baseURL: https://api.wistia.com/v1
  baseurl_source: declared
  description: The Stats:Events API from Wistia — 2 operation(s) for stats:events.
  name: Wistia Stats:Events API
  phrasing_intents:
  - id: getStatsEvents
    intent: List viewing events
    question: How do I list the viewing events for a video?
  - id: getStatsEventsByEventKey
    intent: Show a single viewing event
    question: How do I get the details of one specific viewing event?
  phrasing_ops: 2
  slug: wistia-stats-events-api
- baseURL: https://api.wistia.com/v1
  baseurl_source: declared
  description: The Stats:Media API from Wistia — 3 operation(s) for stats:media.
  name: Wistia Stats:Media API
  phrasing_intents:
  - id: getStatsMediasByMediaId
    intent: Get a video's overall stats
    question: How many plays and loads has this video had in total?
  - id: getStatsMediasByMediaIdByDate
    intent: Get a video's stats day by day
    question: How did one video perform each day over a date range?
  - id: getStatsMediasByMediaIdEngagement
    intent: Get a video's engagement data
    question: How engaged are viewers with this video, and where do they drop off?
  phrasing_ops: 3
  slug: wistia-stats-media-api
- baseURL: https://api.wistia.com/v1
  baseurl_source: declared
  description: The Stats:Projects API from Wistia — 1 operation(s) for stats:projects.
  name: Wistia Stats:Projects API
  phrasing_intents:
  - id: getStatsProjectsByProjectId
    intent: Get a project's stats
    question: How are the videos in one project performing overall?
  phrasing_ops: 1
  slug: wistia-stats-projects-api
- baseURL: https://api.wistia.com/v1
  baseurl_source: declared
  description: The Stats:Visitors API from Wistia — 2 operation(s) for stats:visitors.
  name: Wistia Stats:Visitors API
  phrasing_intents:
  - id: getStatsVisitors
    intent: List visitors who watched videos
    question: Who has been watching videos in my account?
  - id: getStatsVisitorsByVisitorKey
    intent: Show one visitor's details
    question: How do I see details about one specific viewer?
  phrasing_ops: 2
  slug: wistia-stats-visitors-api
- baseURL: https://api.wistia.com/v1
  baseurl_source: declared
  description: The Taggings API from Wistia — 1 operation(s) for taggings.
  name: Wistia Taggings API
  phrasing_intents:
  - id: postTaggingsBulkCreate
    intent: Tag many media at once
    question: How do I add the same tags to a batch of videos?
  phrasing_ops: 1
  slug: wistia-taggings-api
- baseURL: https://api.wistia.com/v1
  baseurl_source: declared
  description: The Trims API from Wistia — 1 operation(s) for trims.
  name: Wistia Trims API
  phrasing_intents:
  - id: postMediasByMediaHashedIdTrims
    intent: Create a trimmed copy of a video
    question: How do I cut sections out of a video and save the result as new media?
  phrasing_ops: 1
  slug: wistia-trims-api
- baseURL: https://api.wistia.com/v1
  baseurl_source: declared
  description: The Webinar Collaborators API from Wistia — 2 operation(s) for webinar collaborators.
  name: Wistia Webinar Collaborators API
  phrasing_intents:
  - id: getWebinarsByWebinarIdCollaborators
    intent: List a webinar's producers
    question: Who has producer access to this webinar?
  - id: postWebinarsByWebinarIdCollaborators
    intent: Invite a producer to a webinar
    question: How do I add someone as a producer on a webinar?
  - id: deleteWebinarsByWebinarIdCollaboratorsById
    intent: Remove a producer from a webinar
    question: How do I take away someone's producer access to a webinar?
  phrasing_ops: 3
  slug: wistia-webinar-collaborators-api
- baseURL: https://api.wistia.com/v1
  baseurl_source: declared
  description: The Webinar Registrations API from Wistia — 1 operation(s) for webinar registrations.
  name: Wistia Webinar Registrations API
  phrasing_intents:
  - id: getWebinarsByWebinarIdRegistrations
    intent: List a webinar's registrations
    question: Who has registered for one of my webinars?
  - id: postWebinarsByWebinarIdRegistrations
    intent: Register a person for a webinar
    question: Can I register someone for a webinar and get their personal join link?
  phrasing_ops: 2
  slug: wistia-webinar-registrations-api
- baseURL: https://api.wistia.com/mcp/api
  baseurl_source: declared
  description: The Sub Folders API from Wistia — 5 operation(s) for sub folders.
  name: Wistia Sub Folders API
  phrasing_intents:
  - id: getFoldersByFolderIdSubfolders
    intent: List subfolders in a folder
    question: What subfolders are inside this folder?
  - id: postFoldersByFolderIdSubfolders
    intent: Create a subfolder in a folder
    question: How do I add a subfolder inside a folder?
  - id: getFoldersByFolderIdSubfoldersBySubfolderId
    intent: Show a subfolder in a folder
    question: How do I see a subfolder of a folder and the media in it?
  - id: putFoldersByFolderIdSubfoldersBySubfolderId
    intent: Rename or describe a subfolder in a folder
    question: How do I rename a subfolder inside a folder?
  - id: deleteFoldersByFolderIdSubfoldersBySubfolderId
    intent: Delete one subfolder from a folder
    question: What happens to the media when I delete a single subfolder in a folder?
  - id: deleteFoldersByFolderIdSubfoldersBulkDelete
    intent: Delete several subfolders at once
    question: How do I delete many subfolders in one request?
  - id: getProjectsByProjectIdSubfolders
    intent: List subfolders in a project
    question: What subfolders does this project contain?
  - id: postProjectsByProjectIdSubfolders
    intent: Create a subfolder in a project
    question: How do I add a subfolder inside a project?
  phrasing_ops: 11
  slug: wistia-sub-folders-api
artifact_total: 77
asyncapis:
- description: AsyncAPI 2.6 description of Wistia's webhook surface. Wistia delivers real-time notifications about media lifecycle events to a consumer endpoint configured in your Wistia account. All webhooks are de
  name: Wistia Webhooks API
  slug: wistia-asyncapi
- description: ''
  name: Wistia Webhooks
  slug: wistia-webhooks
collections:
- collection_type: open
  name: Wistia Data Account API
  slug: open-wistia-account-api
- collection_type: open
  name: Wistia Data Account AllowedDomains API
  slug: open-wistia-alloweddomains-api
- collection_type: open
  name: Wistia Data Account Captions API
  slug: open-wistia-captions-api
- collection_type: open
  name: Wistia Data Account Channels API
  slug: open-wistia-channels-api
- collection_type: open
  name: Wistia Data Account Customizations API
  slug: open-wistia-customizations-api
- collection_type: open
  name: Wistia Data Account Folders API
  slug: open-wistia-folders-api
- collection_type: open
  name: Wistia Data Account Medias API
  slug: open-wistia-medias-api
- collection_type: open
  name: Wistia Data Account Tags API
  slug: open-wistia-tags-api
- collection_type: open
  name: Wistia Data Account Tokens API
  slug: open-wistia-tokens-api
- collection_type: open
  name: Wistia Data Account Webinars API
  slug: open-wistia-webinars-api
- collection_type: open
  name: Wistia Data API
  slug: open-wistia
common:
- group: other
  href: https://artifacts.apis.io/wistia/capabilities/wistia-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/wistia-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/wistia/agentic-access/wistia-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/wistia-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/wistia/security/wistia-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/wistia-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/wistia/security/wistia-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/wistia-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/wistia/authentication/wistia-authentication.yml
  title: ''
  type: Authentication
  url: authentication/wistia-authentication.yml
- group: auth
  href: https://artifacts.apis.io/wistia/scopes/wistia-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/wistia-scopes.yml
- group: agent
  href: https://artifacts.apis.io/wistia/well-known/wistia-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/wistia-well-known.yml
- group: build
  href: https://artifacts.apis.io/wistia/packages/wistia-packages.yml
  title: ''
  type: Packages
  url: packages/wistia-packages.yml
- group: build
  href: https://artifacts.apis.io/wistia/packages/wistia-packages.yml
  title: ''
  type: SDKs
  url: packages/wistia-packages.yml
- group: build
  href: https://artifacts.apis.io/wistia/cli/wistia-cli.yml
  title: ''
  type: CLI
  url: cli/wistia-cli.yml
- group: design
  href: https://artifacts.apis.io/wistia/components/wistia-components.yml
  title: ''
  type: Components
  url: components/wistia-components.yml
- group: design
  href: https://artifacts.apis.io/wistia/conventions/wistia-conventions.yml
  title: ''
  type: Conventions
  url: conventions/wistia-conventions.yml
- group: design
  href: https://artifacts.apis.io/wistia/errors/wistia-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/wistia-problem-types.yml
- group: design
  href: https://artifacts.apis.io/wistia/data-model/wistia-data-model.yml
  title: ''
  type: DataModel
  url: data-model/wistia-data-model.yml
- group: operate
  href: https://artifacts.apis.io/wistia/rate-limits/wistia-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/wistia-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/wistia/plans/wistia-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/wistia-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/wistia/lifecycle/wistia-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/wistia-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.wistia.com
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.wistia.com/docs/wistia-deprecation-schedule
- group: operate
  href: https://artifacts.apis.io/wistia/changelog/wistia-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/wistia-changelog.yml
- group: design
  href: https://artifacts.apis.io/wistia/conformance/wistia-conformance.yml
  title: ''
  type: Conformance
  url: conformance/wistia-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://security.wistia.com/
- group: agent
  href: https://artifacts.apis.io/wistia/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/wistia/mcp/wistia-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/wistia-mcp.yml
- group: build
  href: https://artifacts.apis.io/wistia/mcp/wistia-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/wistia-tool-crosswalk.yml
- group: other
  href: https://artifacts.apis.io/wistia/overlays/wistia-data-api-2026-01-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/wistia-data-api-2026-01-overlay.yaml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/wistia
- group: company
  title: ''
  type: Website
  url: https://wistia.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.wistia.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.wistia.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.wistia.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.wistia.com/docs/making-api-requests
- group: commercial
  title: ''
  type: Pricing
  url: https://wistia.com/pricing
- group: start
  title: ''
  type: Signup
  url: https://wistia.com/signup
- group: operate
  title: ''
  type: Support
  url: https://wistia.com/support
- group: other
  title: ''
  type: Developers
  url: https://docs.wistia.com
- group: company
  title: ''
  type: Blog
  url: https://wistia.com/learn
- group: commercial
  title: ''
  type: TermsOfService
  url: https://wistia.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://wistia.com/privacy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/wistia
- group: agent
  href: https://artifacts.apis.io/wistia/llms/wistia-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/wistia-llms.txt
created: '2026-05-11'
description: 'Wistia is an all-in-one video marketing platform for businesses that combines branded video hosting, webinars, video editing, webcam and screen recording, and deep viewer analytics for B2B marketing teams focused on lead generation, brand control, and content performance. Founded in 2006, Wistia is used by more than 425,000 businesses and integrates with major marketing automation and CRM platforms. Wistia ships an unusually complete developer surface for its category: a frozen evergreen Data API at https://api.wistia.com/v1 alongside a header-versioned modern API at https://api.wistia.com/modern with dated stable releases (2026-01), OpenAPI 3.1 descriptions made discoverable through an RFC 9727 api-catalog linkset, OAuth 2.0 with RFC 8414/9728 discovery and dynamic client registration, a hosted MCP server at https://api.wistia.com/mcp/api, a Go CLI, a Speakeasy-generated TypeScript SDK, and the Aurora `<wistia-player>` web component.'
finops:
- has_sources: true
  method: derived
  name: Wistia Finops
  primary_unit: subscription
  service_category: ''
  slug: wistia-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/wistia.png
layout: provider
mcp_servers:
- description: 'Wistia operates a first-party, hosted MCP server that exposes the Wistia Data API to agents: media, folders, channels, captions, analytics and AI remix. It is a REMOTE streamable-HTTP endpoint — an ag'
  name: Wistia API MCP Server
  slug: wistia-api-mcp-server
modified: '2026-08-14'
name: Wistia
nav: Providers
network: true
overview: 'Wistia publishes 49 API contracts indexed on the [APIs.io](https://apis.io/) network, including Webhooks, Account API, Captions API, and 46 more. Tagged areas include Video Hosting, Video Marketing, Video Analytics, Lead Generation, and Webinars.


  The Wistia catalog on APIs.io includes 2 event-driven AsyncAPI specifications and 1 Spectral governance ruleset.


  Wistia''s developer surface includes authentication, CLI, changelog, documentation, API reference, getting-started guide, pricing, and 34 more developer resources.'
plans:
- name: Wistia Plans Pricing
  plan_count: 4
  slug: wistia-plans-pricing
- name: Wistia Price Estimates
  plan_count: 0
  slug: wistia-price-estimates
random_paper: 9
rate_limits:
- limit_count: 4
  name: Wistia Rate Limits
  slug: wistia-rate-limits
rules:
- authorship: generated
  effective_rule_count: 35
  extends:
  - spectral:asyncapi
  name: Wistia — asyncapi rules
  rule_count: 8
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 7
  slug: wistia-asyncapi-spectral-rules
scopes:
- name: Wistia Scopes
  scope_count: 7
  slug: wistia-scopes
  summary_line: 7 scopes
score:
  band: exemplar
  composite: 75.8
  coverage:
    artifact_dirs: 32
    catalog_earned: 70.8
    catalog_earned_first_party: 24.0
    catalog_gap: 44.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 4.3
  facets:
    access_clarity: 100.0
    contract_governance: 29.5
    contract_quality: 64.0
    developer_ergonomics: 73.2
    discoverability: 80.0
    operational_transparency: 73.7
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-kingdom
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 71.5
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 46
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: fedramp
    jurisdictions_satisfied: 2
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 39.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 11.1
screenshot: https://apis.io/screenshots/wistia/wistia-2026-06-20T201532.png
security:
- kind: authentication
  name: Wistia Authentication
  slug: wistia-authentication
  summary_line: http/oauth2 · 4 schemes
- kind: domain-security
  name: Wistia Domain Security
  slug: wistia-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Wistia Trust Center
  slug: wistia-trust-center
  summary_line: SOC 2, PCI DSS, FedRAMP, GDPR
skill_count: 4
skills:
- name: wistia-audit-and-archive-library
  slug: wistia-audit-and-archive-library
- name: wistia-caption-and-localize-video
  slug: wistia-caption-and-localize-video
- name: wistia-import-and-organize-media
  slug: wistia-import-and-organize-media
- name: wistia-run-a-webinar
  slug: wistia-run-a-webinar
slug: wistia
tags:
- Video Hosting
- Video Marketing
- Video Analytics
- Lead Generation
- Webinars
- B2B Marketing
- Video Captions
- Localization
- MCP
- Media Management
website: https://wistia.com
---
