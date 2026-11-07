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
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: derived
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: three_quarters
    openapi_examples: verified
    operation_distinctiveness: mostly
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 47.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 57
  human_in_the_loop: 0
  name: Gumlet Agentic Access
  operation_count: 89
  slug: gumlet-agentic-access
  summary_line: 89 operations · 57 acting
api_count: 24
apis:
- baseURL: https://api.gumlet.com/v1
  baseurl_source: declared
  description: Add additional audio tracks to an existing asset.
  name: Gumlet Audio Upload API
  phrasing_intents:
  - id: asset-audio-upload
    intent: Add audio tracks to a video
    question: Can I attach extra audio language tracks to a video I already uploaded?
  - id: complete-audio-upload
    intent: Finish an audio track upload
    question: What do I call after I've PUT my audio files to the upload URLs?
  phrasing_ops: 2
  slug: gumlet-audio-upload-api
- baseURL: https://api.gumlet.com/v1
  baseurl_source: declared
  description: Get detailed user activity logs for the entire organisation.
  name: Gumlet Audit Logs API
  phrasing_intents:
  - id: fetch-audit-logs
    intent: Fetch user activity audit logs
    question: Who in my organisation changed settings last week?
  phrasing_ops: 1
  slug: gumlet-audit-logs-api
- baseURL: https://api.gumlet.com/v1
  baseurl_source: declared
  description: Get / change all details about billing and invoices.
  name: Gumlet Billing API
  phrasing_intents:
  - id: list-invoices
    intent: List past invoices
    question: Where can I see all the invoices Gumlet has billed me so far?
  - id: fetch-billing-details
    intent: View the organization's billing details
    question: What billing address and GST number are on file for my organization?
  - id: update-billing-details
    intent: Update billing address and tax details
    question: Can I change the company name and address printed on my invoices?
  - id: fetch-upcoming-invoice
    intent: Preview the upcoming invoice
    question: What will my next invoice look like before it's issued?
  phrasing_ops: 4
  slug: gumlet-billing-api
- baseURL: https://api.gumlet.com/v1
  baseurl_source: declared
  description: Invite and remove viewers on a private video channel.
  name: Gumlet Channel Viewers API
  phrasing_intents:
  - id: invite-channel-viewers
    intent: Invite viewers to a members-only channel
    question: Can I give specific people access to my members-only video channel?
  - id: remove-channel-viewers
    intent: Remove viewers from a channel
    question: How can I revoke a viewer's access to my channel by email?
  - id: invite-channel-viewers-csv
    intent: Bulk-invite channel viewers from a CSV
    question: Can I upload a spreadsheet of emails to invite viewers to my channel?
  - id: list-channel-subscribers
    intent: List a channel's subscribers
    question: Who is subscribed to my video channel?
  phrasing_ops: 4
  slug: gumlet-channel-viewers-api
- baseURL: https://api.gumlet.com/v1
  baseurl_source: declared
  description: Organize video assets into folders within a workspace.
  name: Gumlet Folders API
  phrasing_intents:
  - id: create-folder
    intent: Create a folder in a video workspace
    question: How do I organize my videos into a new folder?
  - id: list-folders
    intent: List folders in a video workspace
    question: What folders exist in my video workspace?
  - id: get-folder
    intent: Get a folder's details
    question: What are the details of one specific folder in my workspace?
  - id: update-folder
    intent: Rename, move or fill a folder
    question: Can I rename a folder or move it under a different parent?
  - id: delete-folder
    intent: Delete a folder and its contents
    question: What happens to the videos and subfolders when I delete a folder?
  - id: remove-assets-folder
    intent: Take videos out of their folder
    question: Can I pull videos out of a folder without deleting them?
  phrasing_ops: 6
  slug: gumlet-folders-api
- baseURL: https://api.gumlet.com/v1
  baseurl_source: declared
  description: Search all video assets / playlists / folders etc across workspaces.
  name: Gumlet Global Search API
  phrasing_intents:
  - id: global-search
    intent: Search videos, playlists and folders everywhere
    question: Can I search for a video by name across all my workspaces at once?
  phrasing_ops: 1
  slug: gumlet-global-search-api
- baseURL: https://api.gumlet.com/v1
  baseurl_source: declared
  description: Manage image sources, view image analytics, and purge the image cache.
  name: Gumlet Image Sources API
  phrasing_intents:
  - id: create-image-source
    intent: Create an image source
    question: How do I connect my storage bucket so Gumlet can optimize my images?
  - id: list-sources
    intent: List image sources
    question: Which image sources are set up on my account?
  - id: get_image-sources-source-id
    intent: Get an image source's settings
    question: What origin and cache settings does one of my image sources use?
  - id: update-image-source
    intent: Update an image source's configuration
    question: Can I change the CDN or browser cache time on an existing image source?
  - id: delete-source
    intent: Delete an image source
    question: What happens to image delivery if I delete an image source?
  - id: purge-image-cache
    intent: Purge cached images by subdomain
    question: Can I clear the cache for images served from a particular subdomain?
  - id: image-purge
    intent: Purge cached image paths by source id
    question: How do I force fresh copies of specific images after I replace them at the origin?
  phrasing_ops: 7
  slug: gumlet-image-sources-api
- baseURL: https://api.gumlet.com/v1
  baseurl_source: declared
  description: Query aggregated and chart-ready image usage analytics data.
  name: Gumlet Image Usage Analytics API
  phrasing_intents:
  - id: retrieve-image-analytics
    intent: Get image delivery usage analytics
    question: How much bandwidth did my image delivery use this month?
  phrasing_ops: 1
  slug: gumlet-image-usage-analytics-api
- baseURL: https://api.gumlet.com/v1
  baseurl_source: declared
  description: Get usage analytics for live streams.
  name: Gumlet Live Stream Analytics API
  phrasing_intents:
  - id: live-usage-analytics
    intent: Get live stream usage analytics
    question: How many minutes did my live streams use last month?
  phrasing_ops: 1
  slug: gumlet-live-stream-analytics-api
- baseURL: https://api.gumlet.com/v1
  baseurl_source: declared
  description: Create, control, and monitor live stream assets.
  name: Gumlet Live Stream Assets API
  phrasing_intents:
  - id: create-live-asset
    intent: Create a live stream
    question: How do I set up a new live stream to push video into?
  - id: create-live-asset-copy
    intent: Rename or reschedule a live stream
    question: Can I change the title of a live stream I already created?
  - id: get-live-asset-status
    intent: Check a live stream's status
    question: Is my live stream currently connected and broadcasting?
  - id: delete-live-asset
    intent: Delete a live stream
    question: Will deleting a live stream also remove its recording and URLs?
  - id: complete-live-stream
    intent: End a live stream for good
    question: How do I mark a live stream as finished so it stops accepting input?
  - id: filter-live-assets
    intent: List live streams by status
    question: Which of my live streams are currently active?
  - id: start-live
    intent: Start a live stream
    question: What call actually kicks off a live broadcast?
  - id: thumbnail-upload-live
    intent: Upload thumbnails for live stream states
    question: Can I show a custom image while my live stream is preparing or disconnected?
  phrasing_ops: 9
  slug: gumlet-live-stream-assets-api
- baseURL: https://api.gumlet.com/v1
  baseurl_source: declared
  description: Create and manage live stream workspaces.
  name: Gumlet Live Stream Workspaces API
  phrasing_intents:
  - id: list-live-workspaces
    intent: List live stream workspaces
    question: What live stream workspaces do I have?
  - id: live-workspace-create
    intent: Create a live stream workspace
    question: How do I set up a separate workspace for live streaming?
  - id: live-workspace-update
    intent: Update a live stream workspace
    question: Can I rename a live stream workspace?
  - id: live-workspace-delete
    intent: Delete a live stream workspace
    question: Can I delete a live streaming workspace I no longer need?
  phrasing_ops: 4
  slug: gumlet-live-stream-workspaces-api
- baseURL: https://api.gumlet.com/v1
  baseurl_source: declared
  description: Upload large video files in parts and complete the multipart upload.
  name: Gumlet Multipart Upload API
  phrasing_intents:
  - id: retrieve-part-url
    intent: Get a signed URL for one upload part
    question: How do I upload a very large video in chunks?
  - id: complete-multipart-upload
    intent: Finish a multipart video upload
    question: What do I do after all the parts of a large video are uploaded?
  phrasing_ops: 2
  slug: gumlet-multipart-upload-api
- baseURL: https://api.gumlet.com/v1
  baseurl_source: declared
  description: Endpoints to get organization details.
  name: Gumlet Organization Data API
  phrasing_intents:
  - id: fetch-org
    intent: Get organization details
    question: What organization details does Gumlet have for my account?
  phrasing_ops: 1
  slug: gumlet-organization-data-api
- baseURL: https://api.gumlet.com/v1
  baseurl_source: declared
  description: Endpoints to list deleted assets and restore them.
  name: Gumlet Recycle Bin API
  phrasing_intents:
  - id: recover
    intent: Restore a deleted video
    question: I deleted a video by mistake; can I get it back?
  - id: list-recycle-bin
    intent: List deleted videos in the recycle bin
    question: Which deleted videos can still be recovered in my workspace?
  phrasing_ops: 2
  slug: gumlet-recycle-bin-api
- baseURL: https://api.gumlet.com/v1
  baseurl_source: declared
  description: Add subtitles to an existing asset.
  name: Gumlet Subtitle Upload API
  phrasing_intents:
  - id: upload-subtitles
    intent: Add subtitle files to a video
    question: Can I upload my own .srt or .vtt captions to a video?
  - id: complete-subtitle-upload
    intent: Finish a subtitle upload
    question: What do I call after PUTting my subtitle files to the upload URLs?
  phrasing_ops: 2
  slug: gumlet-subtitle-upload-api
- baseURL: https://api.gumlet.com/v1
  baseurl_source: declared
  description: Endpoints to get user details.
  name: Gumlet User Data API
  phrasing_intents:
  - id: fetch-user
    intent: Get my user account details
    question: Which user account is my API key signed in as?
  phrasing_ops: 1
  slug: gumlet-user-data-api
- baseURL: https://api.gumlet.com/v1
  baseurl_source: declared
  description: Query aggregated and chart-ready video analytics data.
  name: Gumlet Video Analytics API
  phrasing_intents:
  - id: analytics-chart-data
    intent: Chart viewer analytics over time
    question: How many people watched my videos each day last month?
  - id: analytics-breakdown-data
    intent: Break down viewer analytics by a dimension
    question: Which countries or devices do most of my viewers watch from?
  - id: analytics-aggregated-data
    intent: Get aggregated viewer totals
    question: What are my total views and watch time for a workspace?
  phrasing_ops: 3
  slug: gumlet-video-analytics-api
- baseURL: https://api.gumlet.com/v1
  baseurl_source: declared
  description: Upload, manage, and retrieve video assets, including thumbnails, subtitles, audio tracks, and chapters.
  name: Gumlet Video Assets API
  phrasing_intents:
  - id: create-asset
    intent: Ingest a video from a URL
    question: How do I import a video from a public URL into my workspace for processing?
  - id: create-asset-direct-upload
    intent: Upload a video file from my computer
    question: Can I upload a video file directly from my local machine instead of a URL?
  - id: get-asset-details
    intent: Get a video's details and status
    question: Has my video finished processing yet?
  - id: delete-asset
    intent: Delete a single video
    question: What happens to a video's URLs once I delete it?
  - id: update-asset
    intent: Edit a video's title, tags or metadata
    question: Can I change a video's title and description after uploading?
  - id: thumbnail-select
    intent: Use a video frame as its thumbnail
    question: Can I pick a frame from the video to be its thumbnail?
  - id: thumbnail-upload
    intent: Upload a custom thumbnail image
    question: Can I upload my own image file as a video's thumbnail?
  - id: create-update-chapter
    intent: Set chapters on a video
    question: Can I add chapter markers to a long video?
  phrasing_ops: 13
  slug: gumlet-video-assets-api
- baseURL: https://api.gumlet.com/v1
  baseurl_source: declared
  description: Create and manage playlists, and control which assets belong to them.
  name: Gumlet Video Playlists API
  phrasing_intents:
  - id: create-playlist
    intent: Create a playlist
    question: How do I group videos into a new playlist?
  - id: get-all-playlists
    intent: List playlists in a workspace
    question: What playlists do I have in my video workspace?
  - id: add-asset-playlist
    intent: Add videos to a playlist
    question: Can I add several videos to a playlist in one call?
  - id: remove-asset-playlist
    intent: Remove videos from a playlist
    question: Can I take a video out of a playlist without deleting the video?
  - id: update-playlist
    intent: Update a playlist's details or visibility
    question: Can I rename a playlist or hide it from my channel page?
  - id: delete-playlist
    intent: Delete a playlist
    question: Can I delete a playlist I no longer need?
  - id: get-playlist-assets
    intent: List the videos in a playlist
    question: Which videos are inside a given playlist?
  - id: reorder-asset-playlist
    intent: Reorder the videos in a playlist
    question: Can I change the order videos play in within a playlist?
  phrasing_ops: 8
  slug: gumlet-video-playlists-api
- baseURL: https://api.gumlet.com/v1
  baseurl_source: declared
  description: Create and manage encoding/output profiles for video assets.
  name: Gumlet Video Profiles API
  phrasing_intents:
  - id: create-profile
    intent: Create a reusable video profile
    question: Can I save a set of encoding settings to reuse across many videos?
  - id: list-profiles
    intent: List video processing profiles
    question: What video profiles have I already created?
  - id: update-profile
    intent: Change a video profile's settings
    question: Can I change the format or resolution in an existing profile?
  - id: get-profile
    intent: Get a video profile's settings
    question: What settings are inside a particular video profile?
  - id: delete-profile
    intent: Delete a video profile
    question: Will deleting a profile affect videos already created with it?
  phrasing_ops: 5
  slug: gumlet-video-profiles-api
- baseURL: https://api.gumlet.com/v1
  baseurl_source: declared
  description: Query video analytics and streaming duration usage data.
  name: Gumlet Video Usage Analytics API
  phrasing_intents:
  - id: retrieve-analytics
    intent: Get video usage and bandwidth analytics
    question: How much video bandwidth did I consume last month?
  - id: top-assets
    intent: List the most-streamed videos
    question: Which of my videos were streamed the longest between two dates?
  phrasing_ops: 2
  slug: gumlet-video-usage-analytics-api
- baseURL: https://api.gumlet.com/v1
  baseurl_source: declared
  description: Create and manage video workspaces.
  name: Gumlet Video Workspaces API
  phrasing_intents:
  - id: list-workspaces
    intent: List video workspaces
    question: What video workspaces can my API token access?
  - id: create-workspace
    intent: Create a video workspace
    question: How do I create a separate video workspace for another team?
  - id: update-workspace
    intent: Update a video workspace's settings
    question: Can I change the default profile or player settings on a workspace?
  - id: get-workspace
    intent: Get a video workspace's settings
    question: What settings does a specific video workspace have?
  - id: delete-workspace
    intent: Delete a video workspace
    question: Does deleting a video workspace remove all of its videos too?
  phrasing_ops: 5
  slug: gumlet-video-workspaces-api
- baseURL: https://api.gumlet.com/v1
  baseurl_source: declared
  description: Configure webhooks for account and asset events.
  name: Gumlet Webhooks API
  phrasing_intents:
  - id: create-webhook
    intent: Register a webhook
    question: How do I get notified when a video finishes processing?
  - id: list-webhooks
    intent: List webhooks
    question: Which webhook endpoints have I registered?
  - id: update-webhook
    intent: Update a webhook
    question: Can I change the URL or events on an existing webhook?
  - id: delete-webhook
    intent: Delete a webhook
    question: Can I stop a webhook from sending events entirely?
  - id: webhook-history
    intent: View a webhook's delivery history
    question: Did my webhook deliveries succeed or fail recently?
  phrasing_ops: 5
  slug: gumlet-webhooks-api
artifact_total: 46
asyncapis:
- description: Asynchronous webhook events Gumlet POSTs to your configured endpoint for video and live-stream lifecycle changes. Configure via the org/webhooks API or the dashboard. An optional secret token is echoe
  name: Gumlet Webhooks
  slug: gumlet-webhooks-asyncapi
collections:
- collection_type: open
  name: Gumlet Analytics API
  slug: open-gumlet-analytics-api
- collection_type: open
  name: Gumlet Analytics Image Sources API
  slug: open-gumlet-image-sources-api
- collection_type: open
  name: Gumlet Analytics Live Streaming API
  slug: open-gumlet-live-streaming-api
- collection_type: open
  name: Gumlet Analytics Uploads API
  slug: open-gumlet-uploads-api
- collection_type: open
  name: Gumlet Analytics Video Assets API
  slug: open-gumlet-video-assets-api
- collection_type: open
  name: Gumlet Analytics Video Collections API
  slug: open-gumlet-video-collections-api
- collection_type: open
  name: Gumlet API
  slug: open-gumlet
common:
- group: other
  href: https://artifacts.apis.io/gumlet/capabilities/gumlet-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/gumlet-capability-edges.yml
- group: design
  href: https://artifacts.apis.io/gumlet/asyncapi/gumlet-webhooks-asyncapi.yml
  title: ''
  type: Webhooks
  url: asyncapi/gumlet-webhooks-asyncapi.yml
- group: docs
  href: https://artifacts.apis.io/gumlet/asyncapi/gumlet-webhooks-asyncapi.yml
  title: ''
  type: AsyncAPI
  url: asyncapi/gumlet-webhooks-asyncapi.yml
- group: auth
  href: https://artifacts.apis.io/gumlet/well-known/gumlet-help-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/gumlet-help-security.txt
- group: design
  href: https://artifacts.apis.io/gumlet/rules/gumlet-rules.yml
  title: ''
  type: Spectral
  url: rules/gumlet-rules.yml
- group: design
  href: https://artifacts.apis.io/gumlet/json-ld/gumlet-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/gumlet-context.jsonld
- group: design
  href: https://artifacts.apis.io/gumlet/vocabulary/gumlet-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/gumlet-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/gumlet/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/gumlet/data-model/gumlet-data-model.yml
  title: ''
  type: DataModel
  url: data-model/gumlet-data-model.yml
- group: design
  href: https://artifacts.apis.io/gumlet/components/gumlet-components.yml
  title: ''
  type: Components
  url: components/gumlet-components.yml
- group: build
  href: https://artifacts.apis.io/gumlet/cli/gumlet-cli.yml
  title: ''
  type: CLI
  url: cli/gumlet-cli.yml
- group: design
  href: https://artifacts.apis.io/gumlet/conventions/gumlet-conventions.yml
  title: ''
  type: Conventions
  url: conventions/gumlet-conventions.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.gumlet.com/
- group: auth
  href: https://artifacts.apis.io/gumlet/security/gumlet-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/gumlet-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/gumlet/security/gumlet-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/gumlet-vulnerability-disclosure.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.gumlet.com/
- group: design
  href: https://artifacts.apis.io/gumlet/lifecycle/gumlet-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/gumlet-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/gumlet/errors/gumlet-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/gumlet-problem-types.yml
- group: design
  href: https://artifacts.apis.io/gumlet/conformance/gumlet-conformance.yml
  title: ''
  type: Conformance
  url: conformance/gumlet-conformance.yml
- group: agent
  href: https://artifacts.apis.io/gumlet/llms/gumlet-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/gumlet-llms.txt
- group: build
  href: https://artifacts.apis.io/gumlet/mcp/gumlet-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/gumlet-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/gumlet/mcp/gumlet-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/gumlet-mcp.yml
- group: auth
  href: https://artifacts.apis.io/gumlet/well-known/gumlet-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/gumlet-security.txt
- group: agent
  href: https://artifacts.apis.io/gumlet/well-known/gumlet-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/gumlet-well-known.yml
- group: build
  href: https://artifacts.apis.io/gumlet/packages/gumlet-packages.yml
  title: ''
  type: SDKs
  url: packages/gumlet-packages.yml
- group: build
  href: https://artifacts.apis.io/gumlet/packages/gumlet-packages.yml
  title: ''
  type: Packages
  url: packages/gumlet-packages.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.gumlet.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.gumlet.com/terms/
- group: operate
  title: ''
  type: Support
  url: https://help.gumlet.com/en/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.gumlet.com/privacy/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.gumlet.com/pricing/
- group: start
  title: ''
  type: Login
  url: https://www.gumlet.com/login/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.gumlet.com/docs/getting-started
- group: operate
  title: ''
  type: ChangeLog
  url: https://community.gumlet.com/tag/release-notes/9
- group: agent
  href: https://artifacts.apis.io/gumlet/agentic-access/gumlet-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/gumlet-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/gumlet/security/gumlet-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/gumlet-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/gumlet/security/gumlet-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/gumlet-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/gumlet/authentication/gumlet-authentication.yml
  title: ''
  type: Authentication
  url: authentication/gumlet-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/gumlet
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/gumlet
- group: company
  title: ''
  type: Website
  url: https://www.gumlet.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.gumlet.com/
- group: commercial
  href: https://artifacts.apis.io/gumlet/plans/gumlet-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/gumlet-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/gumlet/rate-limits/gumlet-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/gumlet-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/gumlet/finops/gumlet-finops.yml
  title: ''
  type: FinOps
  url: finops/gumlet-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.gumlet.com/blog/rss/
created: '2026-07-01'
description: Gumlet is a video hosting, streaming, and image optimization platform. Its video APIs cover on-demand and live streaming, per-title encoding, DRM, subtitles, and analytics, while its image APIs provide real-time resize, compression, and CDN delivery from cloud storage sources. All surfaces run under a single REST API at api.gumlet.com/v1 authenticated with a bearer API key.
finops:
- has_sources: true
  method: derived
  name: Gumlet Finops
  primary_unit: subscription
  service_category: ''
  slug: gumlet-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/gumlet.png
jsonld:
- class_count: 1
  name: Gumlet Context
  property_count: 1
  slug: gumlet-context
layout: provider
mcp_servers:
- description: Gumlet ships an official hosted (remote) MCP server exposing 74 tools across video assets, live streaming, image sources, workspaces, folders, playlists, profiles, webhooks, analytics and account mana
  name: Gumlet MCP Server
  slug: gumlet-mcp-server
modified: '2026-07-01'
name: Gumlet
nav: Providers
network: true
overview: 'Gumlet publishes 23 API contracts indexed on the [APIs.io](https://apis.io/) network, including Audio Upload API, Audit Logs API, Billing API, and 20 more. Tagged areas include Video, Streaming, Image Optimization, CDN, and Encoding.


  The Gumlet catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Gumlet''s developer surface includes CLI, support, pricing, getting-started guide, changelog, authentication, documentation, and 39 more developer resources.'
plans:
- name: Gumlet Plans Pricing
  plan_count: 6
  slug: gumlet-plans-pricing
- name: Gumlet Price Estimates
  plan_count: 0
  slug: gumlet-price-estimates
random_paper: 6
rate_limits:
- limit_count: 0
  name: Gumlet Rate Limits
  slug: gumlet-rate-limits
rules:
- authorship: generated
  effective_rule_count: 59
  extends:
  - spectral:oas
  name: Gumlet API Rules
  rule_count: 18
  severity_counts:
    error: 14
    hint: 0
    info: 1
    warn: 3
  slug: gumlet-rules
score:
  band: strong
  composite: 61.9
  coverage:
    artifact_dirs: 33
    catalog_earned: 65.8
    catalog_earned_first_party: 12.0
    catalog_gap: 49.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.3
  facets:
    access_clarity: 69.7
    contract_governance: 35.6
    contract_quality: 73.1
    developer_ergonomics: 56.4
    discoverability: 80.0
    operational_transparency: 36.8
  previous_composite: 71.2
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 23
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 28.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/gumlet/gumlet-2026-07-25T220430.png
security:
- kind: authentication
  name: Gumlet Authentication
  slug: gumlet-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Gumlet Domain Security
  slug: gumlet-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Gumlet Vulnerability Disclosure
  slug: gumlet-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Gumlet Trust Center
  slug: gumlet-trust-center
  summary_line: ISO 27001:2022, SOC 2
skill_count: 3
skills:
- name: gumlet-configure-webhooks
  slug: gumlet-configure-webhooks
- name: gumlet-set-up-live-stream
  slug: gumlet-set-up-live-stream
- name: gumlet-upload-and-publish-video
  slug: gumlet-upload-and-publish-video
slug: gumlet
tags:
- Video
- Streaming
- Image Optimization
- CDN
- Encoding
- Analytics
website: https://www.gumlet.com/
---
