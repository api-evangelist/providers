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
  band: agent-aware
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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 17
  human_in_the_loop: 1
  name: Tiktok For Developers Agentic Access
  operation_count: 18
  slug: tiktok-for-developers-agentic-access
  summary_line: 18 operations · 17 acting · 1 human-in-the-loop
api_count: 4
apis:
- description: OAuth 2.0 authorization and token management
  name: TikTok for Developers OAuth API
  slug: tiktok-for-developers-oauth-api
- description: Video publishing operations
  name: TikTok for Developers Post API
  slug: tiktok-for-developers-post-api
- description: Comment data operations
  name: TikTok for Developers Research Comments API
  slug: tiktok-for-developers-research-comments-api
- description: Social graph data
  name: TikTok for Developers Research Social API
  slug: tiktok-for-developers-research-social-api
- description: User information for research
  name: TikTok for Developers Research Users API
  slug: tiktok-for-developers-research-users-api
- description: Video search and query operations
  name: TikTok for Developers Research Videos API
  slug: tiktok-for-developers-research-videos-api
- description: User profile information
  name: TikTok for Developers User API
  slug: tiktok-for-developers-user-api
- description: Video metadata and management
  name: TikTok for Developers Video API
  slug: tiktok-for-developers-video-api
arazzos:
- description: Check creator settings, initiate a PULL_FROM_URL direct post, then poll publish status until it completes.
  name: TikTok Direct Post a Video from a URL
  slug: tiktok-for-developers-direct-post-video-workflow
- description: Confirm creator settings, send a video to the user's TikTok inbox as a draft, then poll until it lands.
  name: TikTok Upload a Draft to the Creator Inbox
  slug: tiktok-for-developers-inbox-draft-upload-workflow
- description: Exchange an authorization code for an access token, then immediately read the authenticated user's profile.
  name: TikTok OAuth Login and Profile Bootstrap
  slug: tiktok-for-developers-oauth-login-and-profile-workflow
- description: Refresh an expired access token, then list the authenticated user's recent videos with the new token.
  name: TikTok Refresh Token and List Videos
  slug: tiktok-for-developers-refresh-token-and-list-videos-workflow
- description: Resolve a handle, fetch the user's pinned videos, then pull comments on the first pinned video.
  name: TikTok Research Pinned Video Comments
  slug: tiktok-for-developers-research-pinned-video-comments-workflow
- description: Search public videos by keyword and date range, then pull comments on the first matching video.
  name: TikTok Research Video Search and Comments
  slug: tiktok-for-developers-research-search-and-comments-workflow
- description: Resolve a handle, then collect the user's liked videos and reposted videos.
  name: TikTok Research User Video Activity
  slug: tiktok-for-developers-research-user-activity-workflow
- description: Look up a public user by handle, then pull their followers and the accounts they follow.
  name: TikTok Research User Social Graph
  slug: tiktok-for-developers-research-user-social-graph-workflow
- description: Read the authenticated user's profile, list their recent videos, then refresh metadata for the newest video.
  name: TikTok User Profile and Recent Videos
  slug: tiktok-for-developers-user-profile-and-videos-workflow
artifact_total: 54
collections:
- collection_type: postman
  name: TikTok Content Posting OAuth API
  slug: postman-tiktok-for-developers-oauth-api
- collection_type: postman
  name: TikTok Content Posting OAuth Post API
  slug: postman-tiktok-for-developers-post-api
- collection_type: postman
  name: TikTok Content Posting OAuth Research Comments API
  slug: postman-tiktok-for-developers-research-comments-api
- collection_type: postman
  name: TikTok Content Posting OAuth Research Social API
  slug: postman-tiktok-for-developers-research-social-api
- collection_type: postman
  name: TikTok Content Posting OAuth Research Users API
  slug: postman-tiktok-for-developers-research-users-api
- collection_type: postman
  name: TikTok Content Posting OAuth Research Videos API
  slug: postman-tiktok-for-developers-research-videos-api
- collection_type: postman
  name: TikTok Content Posting OAuth User API
  slug: postman-tiktok-for-developers-user-api
- collection_type: postman
  name: TikTok Content Posting OAuth Video API
  slug: postman-tiktok-for-developers-video-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: TikTok Content Posting API
  slug: open-tiktok-content-posting
- collection_type: open
  name: TikTok Display API
  slug: open-tiktok-display
- collection_type: open
  name: TikTok Content Posting OAuth API
  slug: open-tiktok-for-developers-oauth-api
- collection_type: open
  name: TikTok Content Posting OAuth Post API
  slug: open-tiktok-for-developers-post-api
- collection_type: open
  name: TikTok Content Posting OAuth Research Comments API
  slug: open-tiktok-for-developers-research-comments-api
- collection_type: open
  name: TikTok Content Posting OAuth Research Social API
  slug: open-tiktok-for-developers-research-social-api
- collection_type: open
  name: TikTok Content Posting OAuth Research Users API
  slug: open-tiktok-for-developers-research-users-api
- collection_type: open
  name: TikTok Content Posting OAuth Research Videos API
  slug: open-tiktok-for-developers-research-videos-api
- collection_type: open
  name: TikTok Content Posting OAuth User API
  slug: open-tiktok-for-developers-user-api
- collection_type: open
  name: TikTok Content Posting OAuth Video API
  slug: open-tiktok-for-developers-video-api
- collection_type: open
  name: TikTok Login Kit API
  slug: open-tiktok-login-kit
- collection_type: open
  name: TikTok Research API
  slug: open-tiktok-research
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/tiktok-for-developers/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/tiktok-for-developers-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tiktok-for-developers-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/tiktok-for-developers-authentication.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/tiktok-for-developers-direct-post-video-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/tiktok-for-developers-inbox-draft-upload-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/tiktok-for-developers-oauth-login-and-profile-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/tiktok-for-developers-refresh-token-and-list-videos-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/tiktok-for-developers-research-pinned-video-comments-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/tiktok-for-developers-research-search-and-comments-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/tiktok-for-developers-research-user-activity-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/tiktok-for-developers-research-user-social-graph-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/tiktok-for-developers-user-profile-and-videos-workflow.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/tiktok-for-developers
- group: company
  title: ''
  type: Website
  url: https://www.tiktok.com/
- group: start
  title: ''
  type: Portal
  url: https://developers.tiktok.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.tiktok.com/doc/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.tiktok.com/doc/overview
- group: auth
  title: ''
  type: Authentication
  url: https://developers.tiktok.com/doc/login-kit-manage-user-access-tokens
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tiktok
- group: build
  title: ''
  type: SDKs
  url: https://github.com/tiktok/tiktok-opensdk-ios
- group: build
  title: ''
  type: SDKs
  url: https://github.com/tiktok/tiktok-opensdk-android
- group: build
  title: ''
  type: SDKs
  url: https://github.com/tiktok/tiktok-business-api-sdk
- group: operate
  title: ''
  type: ChangeLog
  url: https://developers.tiktok.com/doc/changelog
- group: company
  title: ''
  type: Blog
  url: https://developers.tiktok.com/blog
- group: operate
  title: ''
  type: Forums
  url: https://developers.tiktok.com/community
- group: operate
  title: ''
  type: StatusPage
  url: https://status.tiktok.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developers.tiktok.com/doc/tiktok-api-terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://developers.tiktok.com/doc/tiktok-api-data-privacy
- group: start
  title: ''
  type: Signup
  url: https://developers.tiktok.com/
- group: start
  title: ''
  type: Login
  url: https://developers.tiktok.com/login
created: '2025-07-29'
description: TikTok for Developers provides a suite of REST APIs enabling third-party platforms to integrate with TikTok's social video ecosystem. Products include Login Kit, Display API, Content Posting API, Research API, and the TikTok API for Business, supporting use cases from user authentication and video publishing to advertising campaign management and academic research.
examples:
- key_count: 2
  name: Tiktok Content Posting Initvideopublish Example
  slug: tiktok-content-posting-initVideoPublish-example
- key_count: 2
  name: Tiktok Display Getuserinfo Example
  slug: tiktok-display-getUserInfo-example
- key_count: 2
  name: Tiktok Research Queryresearchvideos Example
  slug: tiktok-research-queryResearchVideos-example
finops:
- name: Tiktok For Developers Finops
  service_category: Social Platform APIs
  slug: tiktok-for-developers-finops
graphqls:
- description: TikTok for Developers API covers login kit, share kit, content posting API, display API for creator content, business account management, and TikTok Shop integration.
  name: TikTok for Developers GraphQL API
  slug: tiktok-for-developers-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tiktok-for-developers.png
json_schemas:
- name: TikTok User
  property_count: 12
  slug: tiktok-for-developers-user
- name: TikTok Video
  property_count: 19
  slug: tiktok-for-developers-video
json_structures:
- name: Tiktok For Developers Video Structure
  property_count: 0
  slug: tiktok-for-developers-video-structure
jsonld:
- class_count: 27
  name: Tiktok For Developers Context
  property_count: 0
  slug: tiktok-for-developers-context
layout: provider
modified: '2026-05-19'
name: TikTok for Developers
nav: Providers
network: true
overview: 'TikTok for Developers publishes 8 APIs on the [APIs.io](https://apis.io/) network, including OAuth API, Post API, Research Comments API, and 5 more. Tagged areas include Advertising, Analytics, Authentication, Content, and Social-Media.


  The TikTok for Developers catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  TikTok for Developers'' developer surface includes authentication, developer portal, documentation, getting-started guide, changelog, engineering blog, signup flow, and 24 more developer resources.'
plans:
- name: Tiktok For Developers Plans Pricing
  plan_count: 4
  slug: tiktok-for-developers-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 3
  name: Tiktok For Developers Rate Limits
  slug: tiktok-for-developers-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: TikTok for Developers API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: tiktok-for-developers-jsonschema-spectral-rules
- effective_rule_count: 50
  extends:
  - spectral:oas
  name: TikTok for Developers API Rules
  rule_count: 9
  severity_counts:
    error: 3
    hint: 0
    info: 1
    warn: 5
  slug: tiktok-for-developers-rules
score:
  band: developing
  composite: 48.7
  coverage:
    artifact_dirs: 19
    catalog_gap: 53.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 22.4
    commercial_clarity: 22.4
    contract_governance: 13.6
    contract_quality: 67.8
    developer_ergonomics: 69.0
    discoverability: 74.1
    governance: 13.6
    operational_transparency: 34.2
  previous_composite: 48.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tiktok-for-developers/refs/heads/main/screenshots/tiktok-for-developers-2026-06-20T195354.png
security:
- kind: authentication
  name: Tiktok For Developers Authentication
  slug: tiktok-for-developers-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Tiktok For Developers Domain Security
  slug: tiktok-for-developers-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: tiktok-for-developers
tags:
- Advertising
- Analytics
- Authentication
- Content
- Social-Media
- Video
website: https://www.tiktok.com/
---
