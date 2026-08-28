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
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.9
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Instagram Agentic Access
  operation_count: 25
  slug: instagram-agentic-access
  summary_line: 25 operations · 8 acting
api_count: 9
apis:
- description: 'The Messenger API support for Instagram consolidates Instagram and Facebook Page messaging into a unified platform. Enables businesses and creators to manage conversations, send and receive messages, '
  name: Instagram Messaging API
  slug: instagram-messaging-api
- description: The Instagram oEmbed endpoint returns HTML and metadata for embedding Instagram photos, videos, reels, and carousels on third-party websites using the standard oEmbed protocol.
  name: Instagram oEmbed API
  slug: instagram-oembed-api
- description: Comment management and moderation
  name: Instagram Comments API
  slug: instagram-comments-api
- description: Hashtag search and media discovery
  name: Instagram Hashtags API
  slug: instagram-hashtags-api
- description: Account and media level analytics
  name: Instagram Insights API
  slug: instagram-insights-api
- description: Photos, videos, stories, reels, and carousels
  name: Instagram Media API
  slug: instagram-media-api
- description: Content where account was mentioned
  name: Instagram Mentions API
  slug: instagram-mentions-api
- description: Content creation and publishing workflow
  name: Instagram Publishing API
  slug: instagram-publishing-api
- description: Instagram Business and Creator account profiles
  name: Instagram Users API
  slug: instagram-users-api
artifact_total: 95
collections:
- collection_type: postman
  name: Instagram Graph Comments API
  slug: postman-instagram-comments-api
- collection_type: postman
  name: Instagram Graph Comments Hashtags API
  slug: postman-instagram-hashtags-api
- collection_type: postman
  name: Instagram Graph Comments Insights API
  slug: postman-instagram-insights-api
- collection_type: postman
  name: Instagram Graph Comments Media API
  slug: postman-instagram-media-api
- collection_type: postman
  name: Instagram Graph Comments Mentions API
  slug: postman-instagram-mentions-api
- collection_type: postman
  name: Instagram Graph Comments Publishing API
  slug: postman-instagram-publishing-api
- collection_type: postman
  name: Instagram Graph Comments Users API
  slug: postman-instagram-users-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Instagram Graph Comments API
  slug: open-instagram-comments-api
- collection_type: open
  name: Instagram Graph Comments Hashtags API
  slug: open-instagram-hashtags-api
- collection_type: open
  name: Instagram Graph Comments Insights API
  slug: open-instagram-insights-api
- collection_type: open
  name: Instagram Graph Comments Media API
  slug: open-instagram-media-api
- collection_type: open
  name: Instagram Graph Comments Mentions API
  slug: open-instagram-mentions-api
- collection_type: open
  name: Instagram Graph Comments Publishing API
  slug: open-instagram-publishing-api
- collection_type: open
  name: Instagram Graph Comments Users API
  slug: open-instagram-users-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/instagram/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/instagram-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/instagram-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/instagram-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/instagram-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/instagram
- group: start
  title: ''
  type: Portal
  url: https://developers.facebook.com/docs/instagram-platform
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.facebook.com/docs/instagram-api/getting-started
- group: auth
  title: ''
  type: Authentication
  url: https://developers.facebook.com/docs/instagram-api/overview#authentication
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developers.facebook.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.facebook.com/privacy/explanation
- group: operate
  title: ''
  type: StatusPage
  url: https://developers.facebook.com/status/
- group: operate
  title: ''
  type: ChangeLog
  url: https://developers.facebook.com/docs/instagram-api/changelog
- group: operate
  title: ''
  type: Support
  url: https://developers.facebook.com/support
- group: company
  title: ''
  type: Blog
  url: https://developers.facebook.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/fbsamples
created: '2024-01-01'
description: Instagram is a photo and video sharing social networking platform owned by Meta. The Instagram APIs allow developers to build integrations with Instagram Business and Creator accounts for content publishing, media management, comment moderation, hashtag discovery, insights and analytics, messaging, and embedding. Available through the Meta Developer Platform with Facebook Login or Instagram Login authentication.
examples:
- key_count: 7
  name: Instagram Graph Api Comment Example
  slug: instagram-graph-api-comment-example
- key_count: 2
  name: Instagram Graph Api Comment List Example
  slug: instagram-graph-api-comment-list-example
- key_count: 1
  name: Instagram Graph Api Container Response Example
  slug: instagram-graph-api-container-response-example
- key_count: 8
  name: Instagram Graph Api Create Container Request Example
  slug: instagram-graph-api-create-container-request-example
- key_count: 1
  name: Instagram Graph Api Error Response Example
  slug: instagram-graph-api-error-response-example
- key_count: 1
  name: Instagram Graph Api Insights Response Example
  slug: instagram-graph-api-insights-response-example
- key_count: 10
  name: Instagram Graph Api Media Example
  slug: instagram-graph-api-media-example
- key_count: 2
  name: Instagram Graph Api Media List Example
  slug: instagram-graph-api-media-list-example
- key_count: 3
  name: Instagram Graph Api Paging Example
  slug: instagram-graph-api-paging-example
- key_count: 1
  name: Instagram Graph Api Success Response Example
  slug: instagram-graph-api-success-response-example
- key_count: 9
  name: Instagram Graph Api User Example
  slug: instagram-graph-api-user-example
features:
- description: Publish photos, videos, reels, carousels, and stories to Instagram Business and Creator accounts programmatically.
  name: Content Publishing
- description: Retrieve, manage, and organize published media including photos, videos, stories, and albums.
  name: Media Management
- description: Read, reply to, hide, and delete comments on Instagram media for brand safety and engagement.
  name: Comment Moderation
- description: Search for hashtags and discover top and recent media associated with specific hashtags.
  name: Hashtag Discovery
- description: Identify and retrieve media where your account has been mentioned by other Instagram users.
  name: Mention Tracking
- description: Access account-level and media-level metrics for reach, impressions, engagement, and audience demographics.
  name: Insights and Analytics
- description: Send and receive messages through Instagram Direct for customer service and business communication.
  name: Instagram Direct Messaging
- description: Publish ephemeral story content including photos and videos that disappear after 24 hours.
  name: Stories Publishing
- description: Create and publish short-form video content as Instagram Reels.
  name: Reels Publishing
- description: Embed Instagram posts, reels, and videos on third-party websites using the standard oEmbed protocol.
  name: oEmbed
- description: Receive real-time notifications for comments, mentions, messages, and story insights via webhooks.
  name: Webhooks
- description: Send private direct messages in response to public comments on your Instagram media.
  name: Private Replies
finops:
- name: Instagram Finops
  service_category: Social Media APIs
  slug: instagram-finops
image: /assets/icons/instagram.png
integrations:
- description: Unified management of Instagram and Facebook content, messaging, and advertising through the Meta platform.
  name: Facebook
- description: Centralized dashboard for managing Instagram and Facebook business accounts, content, and insights.
  name: Meta Business Suite
- description: Cross-platform messaging through Meta unified messaging infrastructure.
  name: WhatsApp
- description: Real-time event notifications for comments, mentions, messages, and story insights.
  name: Webhooks
json_schemas:
- name: CommentList
  property_count: 2
  slug: instagram-graph-api-comment-list
- name: Comment
  property_count: 7
  slug: instagram-graph-api-comment
- name: ContainerResponse
  property_count: 1
  slug: instagram-graph-api-container-response
- name: CreateContainerRequest
  property_count: 8
  slug: instagram-graph-api-create-container-request
- name: ErrorResponse
  property_count: 1
  slug: instagram-graph-api-error-response
- name: InsightsResponse
  property_count: 1
  slug: instagram-graph-api-insights-response
- name: MediaList
  property_count: 2
  slug: instagram-graph-api-media-list
- name: Media
  property_count: 14
  slug: instagram-graph-api-media
- name: Paging
  property_count: 3
  slug: instagram-graph-api-paging
- name: SuccessResponse
  property_count: 1
  slug: instagram-graph-api-success-response
- name: User
  property_count: 9
  slug: instagram-graph-api-user
json_structures:
- name: Instagram Graph Api Comment List Structure
  property_count: 2
  slug: instagram-graph-api-comment-list-structure
- name: Instagram Graph Api Comment Structure
  property_count: 7
  slug: instagram-graph-api-comment-structure
- name: Instagram Graph Api Container Response Structure
  property_count: 1
  slug: instagram-graph-api-container-response-structure
- name: Instagram Graph Api Create Container Request Structure
  property_count: 8
  slug: instagram-graph-api-create-container-request-structure
- name: Instagram Graph Api Error Response Structure
  property_count: 1
  slug: instagram-graph-api-error-response-structure
- name: Instagram Graph Api Insights Response Structure
  property_count: 1
  slug: instagram-graph-api-insights-response-structure
- name: Instagram Graph Api Media List Structure
  property_count: 2
  slug: instagram-graph-api-media-list-structure
- name: Instagram Graph Api Media Structure
  property_count: 14
  slug: instagram-graph-api-media-structure
- name: Instagram Graph Api Paging Structure
  property_count: 3
  slug: instagram-graph-api-paging-structure
- name: Instagram Graph Api Success Response Structure
  property_count: 1
  slug: instagram-graph-api-success-response-structure
- name: Instagram Graph Api User Structure
  property_count: 9
  slug: instagram-graph-api-user-structure
jsonld:
- class_count: 11
  name: Instagram Graph Api Context
  property_count: 37
  slug: instagram-graph-api-context
layout: provider
modified: '2026-04-17'
name: Instagram
nav: Providers
network: true
overview: 'Instagram publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Comments API, Hashtags API, Insights API, and 4 more. Tagged areas include Instagram, Meta, Photos, Social-Media, and Videos.


  The Instagram catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Instagram''s developer surface includes authentication, developer portal, getting-started guide, changelog, support, engineering blog, and 10 more developer resources.'
plans:
- name: Instagram Plans Pricing
  plan_count: 2
  slug: instagram-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 6
  name: Instagram Rate Limits
  slug: instagram-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Instagram API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: instagram-jsonschema-spectral-rules
- effective_rule_count: 65
  extends:
  - spectral:oas
  name: Instagram API Rules
  rule_count: 24
  severity_counts:
    error: 14
    hint: 0
    info: 2
    warn: 8
  slug: instagram-spectral-rules
scopes:
- name: Instagram Scopes
  scope_count: 7
  slug: instagram-scopes
  summary_line: 7 scopes · authorizationCode
score:
  band: developing
  composite: 42.3
  delta: 3.3
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 13.6
    contract_quality: 60.4
    developer_ergonomics: 50.0
    discoverability: 74.1
    governance: 13.6
    operational_transparency: 26.3
  previous_composite: 39.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/instagram/refs/heads/main/screenshots/instagram-2026-06-20T183411.png
security:
- kind: authentication
  name: Instagram Authentication
  slug: instagram-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Instagram Domain Security
  slug: instagram-domain-security
  summary_line: TLSv1.3 · DMARC
slug: instagram
solutions:
- description: Native Instagram authentication for Business and Creator accounts with full API access.
  name: Instagram API with Instagram Login
- description: Facebook Page-linked authentication for Instagram Business accounts with hashtag discovery.
  name: Instagram API with Facebook Login
- description: Unified messaging across Instagram Direct and Facebook Messenger for business communication.
  name: Instagram Messaging
- description: oEmbed and embed tools for displaying Instagram content on third-party websites.
  name: Instagram Embedding
tags:
- Instagram
- Meta
- Photos
- Social-Media
- Videos
- Content Publishing
use_cases:
- description: Automate content publishing, scheduling, and media management across Instagram accounts.
  name: Social Media Management
- description: Track mentions, comments, and hashtags to monitor brand sentiment and engagement.
  name: Brand Monitoring
- description: Manage Instagram Direct conversations for customer support and business inquiries.
  name: Customer Service
- description: Retrieve insights and metrics for measuring content performance and audience growth.
  name: Analytics and Reporting
- description: Discover and curate content through hashtag search and mention tracking.
  name: Content Curation
- description: Connect product catalogs and shopping features with Instagram content for social commerce.
  name: E-commerce Integration
- description: Track creator account metrics, media performance, and audience insights for influencer campaigns.
  name: Influencer Marketing
- description: Embed Instagram posts, reels, and galleries on websites and blogs using oEmbed.
  name: Website Embedding
website: https://developers.facebook.com/docs/instagram-platform
---
