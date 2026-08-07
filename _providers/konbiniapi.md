---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.9
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Konbiniapi Agentic Access
  operation_count: 30
  slug: konbiniapi-agentic-access
  summary_line: 30 operations
api_count: 2
apis:
- description: Instagram data endpoints
  name: KonbiniAPI Instagram API
  slug: konbiniapi-instagram-api
- description: TikTok data endpoints
  name: KonbiniAPI TikTok API
  slug: konbiniapi-tiktok-api
artifact_total: 95
collections:
- collection_type: open
  name: KonbiniAPI
  slug: open-konbiniapi
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/konbiniapi-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/konbiniapi-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/konbiniapi-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/konbiniapi-authentication.yml
- group: auth
  title: ''
  type: Authentication
  url: https://docs.konbiniapi.com/getting-started/authentication
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.konbiniapi.com/getting-started/quickstart
- group: docs
  title: ''
  type: Documentation
  url: https://docs.konbiniapi.com
- group: start
  title: ''
  type: Signup
  url: https://app.konbiniapi.com
- group: commercial
  title: ''
  type: Pricing
  url: https://konbiniapi.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://konbiniapi.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://konbiniapi.com/privacy
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/konbiniapi
- group: operate
  title: ''
  type: Contact
  url: mailto:hello@konbiniapi.com
created: '2026-05-06'
description: KonbiniAPI is the social data layer for Instagram and TikTok, normalizing real-time public profile, post, video, comment, audio, location, and search data into a consistent ActivityStreams 2.0 (W3C) format. The service exposes one Bearer-authenticated REST API and an MCP (Model Context Protocol) interface so developers, AI agents, and automation platforms can fetch normalized social data without managing platform-specific JSON quirks, TLS fingerprinting, sessions, or pagination internals.
examples:
- key_count: 4
  name: Konbiniapi Instagramgethighlightstories Example
  slug: konbiniapi-instagramGetHighlightStories-example
- key_count: 4
  name: Konbiniapi Instagramgetlocationposts Example
  slug: konbiniapi-instagramGetLocationPosts-example
- key_count: 4
  name: Konbiniapi Instagramgetpost Example
  slug: konbiniapi-instagramGetPost-example
- key_count: 4
  name: Konbiniapi Instagramgetpostcomments Example
  slug: konbiniapi-instagramGetPostComments-example
- key_count: 4
  name: Konbiniapi Instagramgetuser Example
  slug: konbiniapi-instagramGetUser-example
- key_count: 4
  name: Konbiniapi Instagramgetuserhighlights Example
  slug: konbiniapi-instagramGetUserHighlights-example
- key_count: 4
  name: Konbiniapi Instagramgetuserposts Example
  slug: konbiniapi-instagramGetUserPosts-example
- key_count: 4
  name: Konbiniapi Instagramgetuserreels Example
  slug: konbiniapi-instagramGetUserReels-example
- key_count: 4
  name: Konbiniapi Instagramgetusertagged Example
  slug: konbiniapi-instagramGetUserTagged-example
- key_count: 4
  name: Konbiniapi Instagramsearchmedia Example
  slug: konbiniapi-instagramSearchMedia-example
- key_count: 4
  name: Konbiniapi Tiktokgetaudio Example
  slug: konbiniapi-tiktokGetAudio-example
- key_count: 4
  name: Konbiniapi Tiktokgetaudiovideos Example
  slug: konbiniapi-tiktokGetAudioVideos-example
- key_count: 4
  name: Konbiniapi Tiktokgetcollectionvideos Example
  slug: konbiniapi-tiktokGetCollectionVideos-example
- key_count: 4
  name: Konbiniapi Tiktokgetcommentreplies Example
  slug: konbiniapi-tiktokGetCommentReplies-example
- key_count: 4
  name: Konbiniapi Tiktokgettagvideos Example
  slug: konbiniapi-tiktokGetTagVideos-example
- key_count: 4
  name: Konbiniapi Tiktokgetuser Example
  slug: konbiniapi-tiktokGetUser-example
- key_count: 4
  name: Konbiniapi Tiktokgetusercollections Example
  slug: konbiniapi-tiktokGetUserCollections-example
- key_count: 4
  name: Konbiniapi Tiktokgetuserfollowers Example
  slug: konbiniapi-tiktokGetUserFollowers-example
- key_count: 4
  name: Konbiniapi Tiktokgetuserfollowing Example
  slug: konbiniapi-tiktokGetUserFollowing-example
- key_count: 4
  name: Konbiniapi Tiktokgetuserlikes Example
  slug: konbiniapi-tiktokGetUserLikes-example
- key_count: 4
  name: Konbiniapi Tiktokgetuserlive Example
  slug: konbiniapi-tiktokGetUserLive-example
- key_count: 4
  name: Konbiniapi Tiktokgetuserreposts Example
  slug: konbiniapi-tiktokGetUserReposts-example
- key_count: 4
  name: Konbiniapi Tiktokgetuserstories Example
  slug: konbiniapi-tiktokGetUserStories-example
- key_count: 4
  name: Konbiniapi Tiktokgetuservideos Example
  slug: konbiniapi-tiktokGetUserVideos-example
- key_count: 4
  name: Konbiniapi Tiktokgetvideo Example
  slug: konbiniapi-tiktokGetVideo-example
- key_count: 4
  name: Konbiniapi Tiktokgetvideocomments Example
  slug: konbiniapi-tiktokGetVideoComments-example
- key_count: 4
  name: Konbiniapi Tiktokgetvideotranscript Example
  slug: konbiniapi-tiktokGetVideoTranscript-example
- key_count: 4
  name: Konbiniapi Tiktoksearchcontent Example
  slug: konbiniapi-tiktokSearchContent-example
- key_count: 4
  name: Konbiniapi Tiktoksearchusers Example
  slug: konbiniapi-tiktokSearchUsers-example
- key_count: 4
  name: Konbiniapi Tiktoksearchvideos Example
  slug: konbiniapi-tiktokSearchVideos-example
finops:
- name: Konbiniapi Finops
  service_category: ''
  slug: konbiniapi-finops
image: https://konbiniapi.com/konbini-logo.svg
json_schemas:
- name: InstagramAttachment
  property_count: 5
  slug: konbiniapi-instagram-attachment
- name: InstagramAudio
  property_count: 7
  slug: konbiniapi-instagram-audio
- name: InstagramCarouselItem
  property_count: 5
  slug: konbiniapi-instagram-carousel-item
- name: InstagramComment
  property_count: 9
  slug: konbiniapi-instagram-comment
- name: InstagramEmbeddedUser
  property_count: 8
  slug: konbiniapi-instagram-embedded-user
- name: InstagramHighlight
  property_count: 6
  slug: konbiniapi-instagram-highlight
- name: InstagramImage
  property_count: 2
  slug: konbiniapi-instagram-image
- name: InstagramImageWithDimensions
  property_count: 0
  slug: konbiniapi-instagram-image-with-dimensions
- name: InstagramLink
  property_count: 3
  slug: konbiniapi-instagram-link
- name: InstagramLocation
  property_count: 6
  slug: konbiniapi-instagram-location
- name: InstagramPost
  property_count: 23
  slug: konbiniapi-instagram-post
- name: InstagramStoryItem
  property_count: 10
  slug: konbiniapi-instagram-story-item
- name: InstagramTag
  property_count: 3
  slug: konbiniapi-instagram-tag
- name: TikTokAudio
  property_count: 14
  slug: konbiniapi-tik-tok-audio
- name: TikTokCollection
  property_count: 7
  slug: konbiniapi-tik-tok-collection
- name: TikTokComment
  property_count: 14
  slug: konbiniapi-tik-tok-comment
- name: TikTokEmbeddedUser
  property_count: 22
  slug: konbiniapi-tik-tok-embedded-user
- name: TikTokImage
  property_count: 4
  slug: konbiniapi-tik-tok-image
- name: TikTokLink
  property_count: 3
  slug: konbiniapi-tik-tok-link
- name: TikTokLiveStreamAttachment
  property_count: 8
  slug: konbiniapi-tik-tok-live-stream-attachment
- name: TikTokStoryAttachment
  property_count: 9
  slug: konbiniapi-tik-tok-story-attachment
- name: TikTokStory
  property_count: 19
  slug: konbiniapi-tik-tok-story
- name: TikTokTag
  property_count: 5
  slug: konbiniapi-tik-tok-tag
- name: TikTokVideoAttachmentHeaders
  property_count: 2
  slug: konbiniapi-tik-tok-video-attachment-headers
- name: TikTokVideoAttachment
  property_count: 9
  slug: konbiniapi-tik-tok-video-attachment
- name: TikTokVideo
  property_count: 22
  slug: konbiniapi-tik-tok-video
json_structures:
- name: Konbiniapi Instagram Attachment Structure
  property_count: 0
  slug: konbiniapi-instagram-attachment-structure
- name: Konbiniapi Instagram Audio Structure
  property_count: 0
  slug: konbiniapi-instagram-audio-structure
- name: Konbiniapi Instagram Carousel Item Structure
  property_count: 0
  slug: konbiniapi-instagram-carousel-item-structure
- name: Konbiniapi Instagram Comment Structure
  property_count: 0
  slug: konbiniapi-instagram-comment-structure
- name: Konbiniapi Instagram Embedded User Structure
  property_count: 0
  slug: konbiniapi-instagram-embedded-user-structure
- name: Konbiniapi Instagram Highlight Structure
  property_count: 0
  slug: konbiniapi-instagram-highlight-structure
- name: Konbiniapi Instagram Image Structure
  property_count: 0
  slug: konbiniapi-instagram-image-structure
- name: Konbiniapi Instagram Image With Dimensions Structure
  property_count: 0
  slug: konbiniapi-instagram-image-with-dimensions-structure
- name: Konbiniapi Instagram Link Structure
  property_count: 0
  slug: konbiniapi-instagram-link-structure
- name: Konbiniapi Instagram Location Structure
  property_count: 0
  slug: konbiniapi-instagram-location-structure
- name: Konbiniapi Instagram Post Structure
  property_count: 0
  slug: konbiniapi-instagram-post-structure
- name: Konbiniapi Instagram Story Item Structure
  property_count: 0
  slug: konbiniapi-instagram-story-item-structure
- name: Konbiniapi Instagram Tag Structure
  property_count: 0
  slug: konbiniapi-instagram-tag-structure
- name: Konbiniapi Tik Tok Audio Structure
  property_count: 0
  slug: konbiniapi-tik-tok-audio-structure
- name: Konbiniapi Tik Tok Collection Structure
  property_count: 0
  slug: konbiniapi-tik-tok-collection-structure
- name: Konbiniapi Tik Tok Comment Structure
  property_count: 0
  slug: konbiniapi-tik-tok-comment-structure
- name: Konbiniapi Tik Tok Embedded User Structure
  property_count: 0
  slug: konbiniapi-tik-tok-embedded-user-structure
- name: Konbiniapi Tik Tok Image Structure
  property_count: 0
  slug: konbiniapi-tik-tok-image-structure
- name: Konbiniapi Tik Tok Link Structure
  property_count: 0
  slug: konbiniapi-tik-tok-link-structure
- name: Konbiniapi Tik Tok Live Stream Attachment Structure
  property_count: 0
  slug: konbiniapi-tik-tok-live-stream-attachment-structure
- name: Konbiniapi Tik Tok Story Attachment Structure
  property_count: 0
  slug: konbiniapi-tik-tok-story-attachment-structure
- name: Konbiniapi Tik Tok Story Structure
  property_count: 0
  slug: konbiniapi-tik-tok-story-structure
- name: Konbiniapi Tik Tok Tag Structure
  property_count: 0
  slug: konbiniapi-tik-tok-tag-structure
- name: Konbiniapi Tik Tok Video Attachment Headers Structure
  property_count: 0
  slug: konbiniapi-tik-tok-video-attachment-headers-structure
- name: Konbiniapi Tik Tok Video Attachment Structure
  property_count: 0
  slug: konbiniapi-tik-tok-video-attachment-structure
- name: Konbiniapi Tik Tok Video Structure
  property_count: 0
  slug: konbiniapi-tik-tok-video-structure
jsonld:
- class_count: 25
  name: Konbiniapi Context
  property_count: 24
  slug: konbiniapi-context
layout: provider
modified: '2026-05-19'
name: KonbiniAPI
nav: Providers
network: true
overview: 'KonbiniAPI publishes 2 APIs on the [APIs.io](https://apis.io/) network: Instagram API and TikTok API. Tagged areas include API, Social Media, Instagram, TikTok, and ActivityStreams 2.0.


  The KonbiniAPI catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  KonbiniAPI''s developer surface includes authentication, getting-started guide, documentation, signup flow, pricing, and 8 more developer resources.'
plans:
- name: Konbiniapi Plans Pricing
  plan_count: 5
  slug: konbiniapi-plans-pricing
random_paper: 43
rate_limits:
- limit_count: 0
  name: Konbiniapi Rate Limits
  slug: konbiniapi-rate-limits
rules:
- name: KonbiniAPI API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: konbiniapi-jsonschema-spectral-rules
- name: KonbiniAPI API Rules
  rule_count: 10
  severity_counts:
    error: 7
    hint: 0
    info: 0
    warn: 3
  slug: konbiniapi-rules
score:
  band: developing
  composite: 55.5
  delta: 0.0
  facets:
    commercial_clarity: 71.1
    contract_quality: 81.4
    developer_ergonomics: 30.4
    discoverability: 68.5
    governance: 58.3
    operational_transparency: 5.3
  previous_composite: 55.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 57.4
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/konbiniapi/refs/heads/main/screenshots/konbiniapi-2026-06-20T184125.png
security:
- kind: authentication
  name: Konbiniapi Authentication
  slug: konbiniapi-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Konbiniapi Domain Security
  slug: konbiniapi-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
- kind: vulnerability-disclosure
  name: Konbiniapi Vulnerability Disclosure
  slug: konbiniapi-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: konbiniapi
tags:
- API
- Social Media
- Instagram
- TikTok
- ActivityStreams 2.0
- Scraping
- Data Extraction
- Public Data
- Influencer Marketing
- Social Listening
- Creator Tools
- MCP
- Model Context Protocol
---
