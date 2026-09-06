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
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 39.0
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Instagram Agentic Access
  operation_count: 25
  slug: instagram-agentic-access
  summary_line: 25 operations · 8 acting
api_count: 1
apis:
- description: 'The Messenger API support for Instagram consolidates Instagram and Facebook Page messaging into a unified platform. Enables businesses and creators to manage conversations, send and receive messages, '
  name: Instagram Messaging API
  slug: instagram-messaging-api
- description: The Instagram oEmbed endpoint returns HTML and metadata for embedding Instagram photos, videos, reels, and carousels on third-party websites using the standard oEmbed protocol.
  name: Instagram oEmbed API
  slug: instagram-oembed-api
- baseURL: https://graph.instagram.com
  baseurl_source: declared
  description: Comment management and moderation
  name: Instagram Comments API
  slug: instagram-comments-api
- baseURL: https://graph.facebook.com
  baseurl_source: declared
  description: Hashtag search and media discovery
  name: Instagram Hashtags API
  slug: instagram-hashtags-api
- baseURL: https://graph.instagram.com
  baseurl_source: declared
  description: Account and media level analytics
  name: Instagram Insights API
  slug: instagram-insights-api
- baseURL: https://graph.instagram.com
  baseurl_source: declared
  description: Photos, videos, stories, reels, and carousels
  name: Instagram Media API
  slug: instagram-media-api
- baseURL: https://graph.instagram.com
  baseurl_source: declared
  description: Content where account was mentioned
  name: Instagram Mentions API
  slug: instagram-mentions-api
- baseURL: https://graph.instagram.com
  baseurl_source: declared
  description: Content creation and publishing workflow
  name: Instagram Publishing API
  slug: instagram-publishing-api
- baseURL: https://graph.instagram.com
  baseurl_source: declared
  description: Instagram Business and Creator account profiles
  name: Instagram Users API
  slug: instagram-users-api
artifact_total: 97
asyncapis:
- description: ''
  name: Instagram Webhooks
  slug: instagram-webhooks
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
- group: company
  title: ''
  type: Website
  url: https://www.instagram.com/
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/instagram-capability-edges.yml
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
  url: https://metastatus.com/
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
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.facebook.com/docs/instagram-platform/instagram-api-with-instagram-login/get-started
- group: docs
  title: ''
  type: Documentation
  url: https://developers.facebook.com/docs/instagram-platform
- group: docs
  title: ''
  type: APIReference
  url: https://developers.facebook.com/docs/instagram-api/reference
- group: start
  title: ''
  type: Login
  url: https://developers.facebook.com/apps/
- group: build
  title: ''
  type: Packages
  url: packages/instagram-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/instagram-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/instagram-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/instagram-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/instagram-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/instagram-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/instagram-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/instagram-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/instagram-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/instagram-data-model.yml
- group: design
  title: ''
  type: Components
  url: components/instagram-components.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/instagram-sandbox.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/instagram-changelog.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/instagram-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/instagram-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/instagram-vulnerability-disclosure.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/instagram-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/instagram-plans-pricing.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/instagram-finops.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/instagram-vocabulary.yaml
- group: design
  title: ''
  type: SpectralRules
  url: rules/instagram-spectral-rules.yml
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/instagram-graph-api-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/instagram-graph-api-media-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/instagram-graph-api-comment-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/instagram-graph-api-user-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/instagram-graph-api-error-response-schema.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/instagram-graph-api-media-structure.json
- group: build
  title: ''
  type: Examples
  url: examples/instagram-graph-api-media-example.json
- group: build
  title: ''
  type: Examples
  url: examples/instagram-graph-api-comment-example.json
- group: build
  title: ''
  type: Examples
  url: examples/instagram-graph-api-error-response-example.json
- group: build
  title: ''
  type: PostmanCollection
  url: collections/instagram-media-api.postman_collection.json
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
modified: '2026-08-29'
name: Instagram
nav: Providers
network: true
overview: 'Instagram publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Comments API, Hashtags API, Insights API, and 4 more. Tagged areas include Instagram, Meta, Photos, Social-Media, and Videos.


  The Instagram catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 2 Spectral governance rulesets.


  Instagram''s developer surface includes authentication, developer portal, changelog, support, engineering blog, getting-started guide, documentation, and 46 more developer resources.'
plans:
- name: Instagram Plans Pricing
  plan_count: 2
  slug: instagram-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 8
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
  scope_count: 19
  slug: instagram-scopes
  summary_line: 19 scopes · authorizationCode
score:
  band: strong
  composite: 66.1
  coverage:
    artifact_dirs: 34
    catalog_earned: 80.5
    catalog_earned_first_party: 20.0
    catalog_gap: 34.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 52.6
    commercial_clarity: 52.6
    contract_governance: 47.0
    contract_quality: 70.3
    developer_ergonomics: 74.4
    discoverability: 75.9
    governance: 47.0
    operational_transparency: 76.3
  previous_composite: 66.1
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/instagram/refs/heads/main/screenshots/instagram-2026-06-20T183411.png
security:
- kind: authentication
  name: Instagram Authentication
  slug: instagram-authentication
  summary_line: oauth2 · 2 schemes
- kind: domain-security
  name: Instagram Domain Security
  slug: instagram-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Instagram Vulnerability Disclosure
  slug: instagram-vulnerability-disclosure
  summary_line: Hackerone
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
website: https://www.instagram.com/
---
