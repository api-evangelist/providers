---
access_model:
  confidence: high
  label: Freemium · Self-serve signup · 100 free credits
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - https://konbiniapi.com/pricing
  trial: true
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 49.4
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Konbiniapi Agentic Access
  operation_count: 67
  slug: konbiniapi-agentic-access
  summary_line: 67 operations · 3 acting
api_count: 6
apis:
- description: Ten Instagram endpoints covering profiles, posts, reels, tagged media, story highlights, post comments, location feeds and trending media search, normalized to ActivityStreams 2.0.
  name: KonbiniAPI Instagram API
  slug: konbiniapi-instagram-api
- description: Twenty-one TikTok endpoints covering profiles, videos, likes, reposts, collections, stories, following and follower lists, live streams, comments and replies, WebVTT transcripts, hashtags, audio track
  name: KonbiniAPI TikTok API
  slug: konbiniapi-tiktok-api
- description: Seven X (Twitter) endpoints covering public profiles, user post timelines, the Highlights tab, single posts, and X Communities including community metadata, posts and media — all as visible to a logge
  name: KonbiniAPI X API
  slug: konbiniapi-x-api
- description: Twenty-two Reddit endpoints — the provider's deepest surface — covering users, subreddits and their structured rules, posts, comments and reply threads, duplicates and crossposts, site-wide feeds, thr
  name: KonbiniAPI Reddit API
  slug: konbiniapi-reddit-api
- description: Seven LinkedIn endpoints covering public member profiles, member posts and published articles, company pages and company posts, single posts with inline comments, and video post transcripts. The newes
  name: KonbiniAPI LinkedIn API
  slug: konbiniapi-linkedin-api
- description: Hosted remote MCP server exposing one typed tool for every one of the 67 REST operations, over streamable HTTP with OAuth 2.1 (authorization code + PKCE) or a Bearer API key. Adds three MCP-only proje
  name: KonbiniAPI MCP Server
  slug: konbiniapi-mcp
artifact_total: 106
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Konbini Instagram API
  slug: open-konbiniapi-instagram-api
- collection_type: open
  name: Konbini LinkedIn API
  slug: open-konbiniapi-linkedin-api
- collection_type: open
  name: Konbini TikTok API
  slug: open-konbiniapi-tiktok-api
- collection_type: open
  name: Konbini X API
  slug: open-konbiniapi-x-api
- collection_type: open
  name: KonbiniAPI
  slug: open-konbiniapi
common:
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/konbiniapi-openapi.json
- group: agent
  title: ''
  type: MCPServer
  url: mcp/konbiniapi-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/konbiniapi-tool-crosswalk.yml
- group: other
  title: ''
  type: AgentCard
  url: a2a/konbiniapi-a2a.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/konbiniapi-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/konbiniapi-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/konbiniapi-security.txt
- group: auth
  title: ''
  type: Security
  url: security/konbiniapi-vulnerability-disclosure.yml
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
  type: OAuthScopes
  url: scopes/konbiniapi-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/konbiniapi-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/konbiniapi-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/konbiniapi-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/konbiniapi-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/konbiniapi-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/konbiniapi-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/konbiniapi-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/konbiniapi-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/konbiniapi-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/konbiniapi-finops.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/konbiniapi-agentic-access.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/konbiniapi-vocabulary.yml
- group: design
  title: ''
  type: SpectralRules
  url: rules/konbiniapi-rules.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/konbiniapi-context.jsonld
- group: build
  title: ''
  type: PostmanCollection
  url: collections/konbiniapi.postman_collection.json
- group: build
  title: ''
  type: OpenCollection
  url: collections/konbiniapi.opencollection.json
- group: other
  title: ''
  type: APICatalog
  url: well-known/konbiniapi-api-catalog.json
- group: build
  title: ''
  type: OpenAIPluginManifest
  url: well-known/konbiniapi-ai-plugin.json
- group: auth
  title: ''
  type: Authentication
  url: https://docs.konbiniapi.com/getting-started/authentication
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.konbiniapi.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.konbiniapi.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.konbiniapi.com/reference/api/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.konbiniapi.com/getting-started/quickstart
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.konbiniapi.com/changelog
- group: start
  title: ''
  type: SignUp
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
- group: other
  title: ''
  type: DPA
  url: https://konbiniapi.com/dpa
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/konbiniapi
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/konbiniapi
- group: agent
  title: ''
  type: X-llms-txt
  url: https://docs.konbiniapi.com/llms.txt
- group: agent
  title: ''
  type: X-llms-full-txt
  url: https://docs.konbiniapi.com/llms-full.txt
- group: agent
  title: ''
  type: X-mcp
  url: https://mcp.konbiniapi.com
- group: operate
  title: ''
  type: Support
  url: mailto:hello@konbiniapi.com
- group: operate
  title: ''
  type: Contact
  url: mailto:hello@konbiniapi.com
created: '2026-05-06'
description: KonbiniAPI is the social data layer for Instagram, TikTok, X, Reddit and LinkedIn, normalizing real-time public profile, post, video, comment, audio, community, subreddit, location and search data into a single consistent ActivityStreams 2.0 (W3C) shape. Sixty-seven endpoints are exposed through one Bearer-authenticated REST API and, one-for-one, through a hosted remote MCP (Model Context Protocol) server at mcp.konbiniapi.com with OAuth 2.1, so developers, AI agents and automation platforms can fetch normalized social data without managing platform-specific JSON quirks, TLS fingerprinting, sessions or pagination internals. Billing is a flat credit model — one successful request costs one credit, failed and upstream-error requests are refunded, and the provider publishes no rate limits at all.
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
mcp_servers:
- description: ''
  name: konbiniapi-mcp.yml
  slug: konbiniapi-mcpyml
modified: '2026-08-13'
name: KonbiniAPI
nav: Providers
network: true
overview: 'KonbiniAPI publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Instagram API, TikTok API, X API, and 2 more. Tagged areas include API, Social Media, Instagram, TikTok, and X.


  The KonbiniAPI catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  KonbiniAPI''s developer surface includes authentication, changelog, documentation, API reference, getting-started guide, signup flow, pricing, and 42 more developer resources.'
plans:
- name: Konbiniapi Plans Pricing
  plan_count: 6
  slug: konbiniapi-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 0
  name: Konbiniapi Rate Limits
  slug: konbiniapi-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: KonbiniAPI API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: konbiniapi-jsonschema-spectral-rules
- effective_rule_count: 51
  extends:
  - spectral:oas
  name: KonbiniAPI API Rules
  rule_count: 10
  severity_counts:
    error: 7
    hint: 0
    info: 0
    warn: 3
  slug: konbiniapi-rules
scopes:
- name: Konbiniapi Scopes
  scope_count: 0
  slug: konbiniapi-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: exemplar
  composite: 73.7
  delta: 0.9
  facets:
    access_clarity: 84.2
    commercial_clarity: 84.2
    contract_governance: 41.7
    contract_quality: 74.1
    developer_ergonomics: 66.7
    discoverability: 81.5
    governance: 41.7
    operational_transparency: 28.9
  previous_composite: 72.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 75.9
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/konbiniapi/refs/heads/main/screenshots/konbiniapi-2026-06-20T184125.png
security:
- kind: authentication
  name: Konbiniapi Authentication
  slug: konbiniapi-authentication
  summary_line: http/oauth2 · 3 schemes
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
- X
- Reddit
- LinkedIn
- ActivityStreams 2.0
- Scraping
- Data Extraction
- Public Data
- Influencer Marketing
- Social Listening
- Creator Tools
- MCP
- Model Context Protocol
- Agent Skills
- Agents
website: https://docs.konbiniapi.com
---
