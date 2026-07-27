---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 117
  human_in_the_loop: 5
  name: Brightcove Agentic Access
  operation_count: 219
  slug: brightcove-agentic-access
  summary_line: 219 operations · 117 acting · 5 human-in-the-loop
api_count: 53
apis:
- description: Handles ingestion of videos and media assets into Video Cloud, supporting remote URL ingestion and upload from local files.
  name: Brightcove Dynamic Ingest API
  slug: brightcove-dynamic-ingest-api
- description: Retrieves analytics data programmatically for Video Cloud accounts, including dimensions like device type, geography, player, and video performance metrics.
  name: Brightcove Analytics API
  slug: brightcove-analytics-api
- description: Fetches video and playlist data for players and mobile apps, providing optimized delivery of media metadata and playback URLs.
  name: Brightcove Playback API
  slug: brightcove-playback-api
- description: Creates, edits, and manages Brightcove players as publishable resources with full configuration control.
  name: Brightcove Player Management API
  slug: brightcove-player-management-api
- description: Creates and manages live streams with comprehensive streaming controls including RTMP, RTP, RTP-FEC, and SRT input protocols and HLS output delivery.
  name: Brightcove Live API
  slug: brightcove-live-api
- description: Implements OAuth 2.0 client credentials flow for managing credentials and obtaining access tokens for all Brightcove REST APIs.
  name: Brightcove OAuth API
  slug: brightcove-oauth-api
- description: Enables server-side ad stitching directly into video streams, supporting VOD and live stream monetization with seamless ad insertion.
  name: Brightcove SSAI API
  slug: brightcove-ssai-api
- description: Manages profiles that define video processing during ingestion, controlling encoding settings and rendition creation.
  name: Brightcove Ingest Profiles API
  slug: brightcove-ingest-profiles-api
- description: Customizes media delivery to meet specific business objectives, enabling conditional logic for rendition selection and CDN routing.
  name: Brightcove Delivery Rules API
  slug: brightcove-delivery-rules-api
- description: Manages cloud-based linear channel playout with EPG (Electronic Programming Guide) and Channels APIs for scheduled programming.
  name: Brightcove Cloud Playout APIs
  slug: brightcove-cloud-playout-apis
- description: Retrieves viewing event and lead data for marketing automation workflows, enabling integration with MAP and CRM platforms.
  name: Brightcove Audience API
  slug: brightcove-audience-api
- description: Retrieves social sharing status and history for videos distributed to social media platforms.
  name: Brightcove Social API
  slug: brightcove-social-api
- description: Provides scalable playback management including DRM, concurrency controls, and geographic and domain restrictions.
  name: Brightcove Playback Restrictions API
  slug: brightcove-playback-restrictions-api
- description: Get access tokens to authenticate API requests.
  name: Brightcove Access Tokens API
  slug: brightcove-access-tokens-api
- description: Operations for managing default profiles for the account.
  name: Brightcove Account Configuration API
  slug: brightcove-account-configuration-api
- description: Operations for tracking ad calls - used primarily for debugging.
  name: Brightcove Ad Call Tracking API
  slug: brightcove-ad-call-tracking-api
- description: Operations for managing ad configurations.
  name: Brightcove Ad Configurations API
  slug: brightcove-ad-configurations-api
- description: Full analytics reports with many options for filtering, date ranges, formats, and more.
  name: Brightcove Analytics Report API
  slug: brightcove-analytics-report-api
- description: Clear_sources endpoints expose unencrypted sources to the preview players in the studio for customers who are using [Playback Rights](/playback-restrictions/references/index.html) to protect DRM and H
  name: Brightcove Clear-Sources API
  slug: brightcove-clear-sources-api
- description: Create client credentials needed to get access tokens.
  name: Brightcove Client Credentials API
  slug: brightcove-client-credentials-api
- description: Operations for creating and managing credentials for secure destinations.
  name: Brightcove Credentials API
  slug: brightcove-credentials-api
- description: Operations for creating and managing custom fields.
  name: Brightcove Custom Fields API
  slug: brightcove-custom-fields-api
- description: Operations for creating, reading, updating and deleting Delivery Rule Actions
  name: Brightcove Delivery Rule Actions API
  slug: brightcove-delivery-rule-actions-api
- description: Operations for reading and updating Delivery Rule Conditions
  name: Brightcove Delivery Rule Conditions API
  slug: brightcove-delivery-rule-conditions-api
- description: Operations for reading Delivery Rules
  name: Brightcove Delivery Rules API
  slug: brightcove-delivery-rules-api
- description: Operations for managing player embed (child player) configurations.
  name: Brightcove Embed Configurations API
  slug: brightcove-embed-configurations-api
- description: Detailed engagement reports by account, video or player. Detailed engagement is available only for the most recent 32 days.
  name: Brightcove Engagement Report API
  slug: brightcove-engagement-report-api
- description: Operations for managing folders to organize your videos.
  name: Brightcove Folders API
  slug: brightcove-folders-api
- description: Operations for getting the history of all or a specific video.
  name: Brightcove History API
  slug: brightcove-history-api
- description: The Ingest API from Brightcove — 2 operation(s) for ingest.
  name: Brightcove Ingest API
  slug: brightcove-ingest-api
- description: Operations for managing folders to organize your videos. See [Working with Labels](/cms/managing-videos/working-with-labels.html) for more information.
  name: Brightcove Labels API
  slug: brightcove-labels-api
- description: Get leads for a Video Cloud account.
  name: Brightcove Leads API
  slug: brightcove-leads-api
- description: Analytics for Live streams
  name: Brightcove Live Analytics API
  slug: brightcove-live-analytics-api
- description: Operations for creating and managing VOD clips, including scheduling clips for SEP jobs
  name: Brightcove Live Job Clip API
  slug: brightcove-live-job-clip-api
- description: Operations for creating live jobs, listing live jobs, getting job details, and canceling live jobs. There are also operations for activating and deactivating SEP jobs, scheduling activation and deacti
  name: Brightcove Live Jobs API
  slug: brightcove-live-jobs-api
- description: Operations for managing renditions, manifests, and other media assets. These operations are used mainly for remote assets.
  name: Brightcove Media Assets API
  slug: brightcove-media-assets-api
- description: Operations for creating and managing hierarchical labels that can be associated with videos.
  name: Brightcove Media Sharing API
  slug: brightcove-media-sharing-api
- description: Operations for setting up and managing notifications of changes to your video library.
  name: Brightcove Notifications API
  slug: brightcove-notifications-api
- description: Operations for managing player configurations.
  name: Brightcove Player Configurations API
  slug: brightcove-player-configurations-api
- description: Operations for managing player embeds (child players).
  name: Brightcove Player Embeds API
  slug: brightcove-player-embeds-api
- description: Operations for managing players.
  name: Brightcove Players API
  slug: brightcove-players-api
- description: Operations for managing video playlists.
  name: Brightcove Playlists API
  slug: brightcove-playlists-api
- description: Operations for working with the player plugin registry.
  name: Brightcove Plugin Registry API
  slug: brightcove-plugin-registry-api
- description: Operations creating and managing ingest profiles.
  name: Brightcove Profiles API
  slug: brightcove-profiles-api
- description: Operations for creating redundant groups of live jobs for failover in case one stream fails
  name: Brightcove Redundant Groups API
  slug: brightcove-redundant-groups-api
- description: Operations for creating and managing RTMP outputs. Note that RTMP output hours will be billed against event hours.
  name: Brightcove RTMP Outputs API
  slug: brightcove-rtmp-outputs-api
- description: Operations for scheduling the creation of a VOD clip for SEP jobs only.
  name: Brightcove Schedule Clip API
  slug: brightcove-schedule-clip-api
- description: Operations for scheduling the activation and deactivation of an SEP job.
  name: Brightcove Schedule SEP Job Start Stop API
  slug: brightcove-schedule-sep-job-start-stop-api
- description: Operations for managing server-side ad insertion with live streams.
  name: Brightcove SSAI API
  slug: brightcove-ssai-api
- description: Operations for getting the status of all or a specific video.
  name: Brightcove Status API
  slug: brightcove-status-api
- description: Low latency endpoints for quickly retrieving a single piece of data.
  name: Brightcove Video Data API
  slug: brightcove-video-data-api
- description: Operations for managing videos, video metadata, audio tracks, and more.
  name: Brightcove Videos API
  slug: brightcove-videos-api
- description: Get view events for a Video Cloud account
  name: Brightcove View Events API
  slug: brightcove-view-events-api
artifact_total: 62
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/brightcove-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/brightcove-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/brightcove-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/brightcove-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/brightcove-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://www.brightcove.com
- group: docs
  title: ''
  type: Documentation
  url: https://apis.support.brightcove.com/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/brightcove
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/brightcove
- group: company
  title: ''
  type: Blog
  url: https://www.brightcove.com/en/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.brightcove.com/en/contact/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.brightcove.com/
- group: other
  title: ''
  type: X
  url: https://x.com/brightcove
- group: commercial
  title: ''
  type: Plans
  url: plans/brightcove-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/brightcove-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/brightcove-finops.yml
created: '2026-06-13'
description: Brightcove is an online video platform providing REST APIs for uploading and managing videos, encoding, CDN delivery, player configuration, analytics, and live streaming management. Its Video Cloud platform serves media companies, broadcasters, marketers, and OTT providers globally.
finops:
- name: Brightcove Finops
  service_category: ''
  slug: brightcove-finops
graphqls:
- description: 'Brightcove is a cloud video platform for businesses. The API covers video ingestion and management, player configuration, dynamic delivery, analytics, social sharing, live streaming, video cloud CMS, '
  name: Brightcove GraphQL API
  slug: brightcove-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/brightcove.png
layout: provider
modified: '2026-06-13'
name: Brightcove
nav: Providers
network: true
overview: 'Brightcove publishes 42 APIs on the [APIs.io](https://apis.io/) network, including SSAI API, Delivery Rules API, Access Tokens API, and 39 more. Tagged areas include Video, Media, Streaming, Live Streaming, and Analytics.


  Brightcove''s developer surface includes authentication, documentation, engineering blog, pricing, and 12 more developer resources.'
plans:
- name: Brightcove Plans Pricing
  plan_count: 2
  slug: brightcove-plans-pricing
random_paper: 49
rate_limits:
- limit_count: 0
  name: Brightcove Rate Limits
  slug: brightcove-rate-limits
scopes:
- name: Brightcove Scopes
  scope_count: 33
  slug: brightcove-scopes
  summary_line: 33 scopes · clientCredentials
score:
  band: thin
  composite: 40.7
  delta: 0.0
  facets:
    commercial_clarity: 47.4
    contract_quality: 56.4
    developer_ergonomics: 21.7
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 40.7
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/brightcove/refs/heads/main/screenshots/brightcove-2026-06-20T173711.png
security:
- kind: authentication
  name: Brightcove Authentication
  slug: brightcove-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Brightcove Domain Security
  slug: brightcove-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Brightcove Trust Center
  slug: brightcove-trust-center
  summary_line: ISO 27001, GDPR, CSA STAR
slug: brightcove
tags:
- Video
- Media
- Streaming
- Live Streaming
- Analytics
- CDN
- OTT
- Player
- Ad Insertion
website: https://www.brightcove.com
---
