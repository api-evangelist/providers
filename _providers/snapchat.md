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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 37.8
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 18
  human_in_the_loop: 0
  name: Snapchat Agentic Access
  operation_count: 42
  slug: snapchat-agentic-access
  summary_line: 42 operations · 18 acting
api_count: 16
apis:
- description: The Snapchat Ads API (Marketing API) allows developers to programmatically create, manage, and optimize advertising campaigns on the Snapchat platform. It provides endpoints for managing organizations
  name: Snapchat Ads API
  slug: snapchat-ads-api
- description: Creative Kit allows developers to let users share content including Lenses, AR experiences, filters, GIFs, videos, links, and captions from a website or app directly to Snapchat's camera or preview sc
  name: Snapchat Creative Kit
  slug: snapchat-creative-kit
- description: Camera Kit enables developers to integrate Snap's AR camera technology directly into iOS, Android, and web applications, giving users access to Snap's lens library and AR experiences without leaving t
  name: Snapchat Camera Kit
  slug: snapchat-camera-kit
- description: Lens Studio is Snap's desktop application for building augmented reality lenses for Snapchat and Spectacles. Provides an API for scripting lens behaviors, integrating dynamic data, and publishing to t
  name: Lens Studio
  slug: snapchat-lens-studio
- description: Ad Accounts are owned by an Organization and contain Ad Campaigns. They have one or more Funding Sources.
  name: Snapchat Ad Accounts API
  slug: snapchat-ad-accounts-api
- description: Ad Squads organize ads within a campaign, defining targeting, budget, schedule, and bid strategy.
  name: Snapchat Ad Squads API
  slug: snapchat-ad-squads-api
- description: Audience Segments allow advertisers to define and manage custom audiences for ad targeting, including Snap Audience Match, lookalike audiences, and pixel-based audiences.
  name: Snapchat Audience Segments API
  slug: snapchat-audience-segments-api
- description: Campaigns define a business objective and organize Ad Squads, allowing advertisers to view aggregate statistics.
  name: Snapchat Campaigns API
  slug: snapchat-campaigns-api
- description: Endpoints for sending web, app, and offline conversion events to Snap for campaign measurement and optimization.
  name: Snapchat Conversion Events API
  slug: snapchat-conversion-events-api
- description: Creatives define the visual and interactive content of ads, including images, videos, and call-to-action overlays.
  name: Snapchat Creatives API
  slug: snapchat-creatives-api
- description: Funding Sources represent payment methods associated with an organization, including credit cards, PayPal, and lines of credit.
  name: Snapchat Funding Sources API
  slug: snapchat-funding-sources-api
- description: Measurement endpoints provide campaign performance statistics and reporting data at various levels of the ad hierarchy.
  name: Snapchat Measurement API
  slug: snapchat-measurement-api
- description: Media endpoints handle uploading and managing media assets such as images and videos used in creatives.
  name: Snapchat Media API
  slug: snapchat-media-api
- description: OAuth 2.0 authorization and token management endpoints for authenticating users via their Snapchat account.
  name: Snapchat OAuth API
  slug: snapchat-oauth-api
- description: Organizations represent brands, partners, or ad agencies. Organizations are created via Snap Business Manager.
  name: Snapchat Organizations API
  slug: snapchat-organizations-api
- description: Endpoints for retrieving authenticated user profile information including display name and Bitmoji avatar.
  name: Snapchat User Profile API
  slug: snapchat-user-profile-api
artifact_total: 57
collections:
- collection_type: open
  name: Snapchat Ads API
  slug: open-snapchat-ads-api
- collection_type: open
  name: Snapchat Conversions API
  slug: open-snapchat-conversions-api
- collection_type: open
  name: Snapchat Login Kit API
  slug: open-snapchat-login-kit
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/snapchat-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/snapchat-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/snapchat-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/snapchat-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/snap-inc-co
- group: company
  title: ''
  type: Website
  url: https://snap.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.snap.com
- group: docs
  title: ''
  type: Documentation
  url: https://developers.snap.com/api/marketing-api/Ads-API/introduction
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Snapchat
- group: commercial
  title: ''
  type: TermsOfService
  url: https://snap.com/en-US/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://snap.com/en-US/privacy/privacy-policy
- group: company
  title: ''
  type: Blog
  url: https://eng.snap.com
- group: operate
  title: ''
  type: Support
  url: https://businesshelp.snapchat.com
- group: start
  title: ''
  type: Login
  url: https://kit.snapchat.com/manage/
- group: commercial
  title: ''
  type: Pricing
  url: https://ads.snapchat.com
- group: start
  title: ''
  type: Signup
  url: https://kit.snapchat.com/manage/
- group: agent
  title: ''
  type: LlmsText
  url: https://developers.snap.com/llms.txt
created: '2026-05-02'
description: Snap Inc. operates Snapchat, a visual messaging app and camera platform with developer tools including the Marketing API for programmatic advertising, Conversions API for server-side conversion tracking, Login Kit for OAuth-based user authentication, Creative Kit for content sharing to Snapchat, Camera Kit for embedding Snap AR technology into third-party apps, and Lens Studio for building augmented reality experiences.
examples:
- key_count: 4
  name: Snapchat Create Campaign Example
  slug: snapchat-create-campaign-example
- key_count: 4
  name: Snapchat Send Conversion Events Example
  slug: snapchat-send-conversion-events-example
finops:
- name: Snapchat Finops
  service_category: Advertising
  slug: snapchat-finops
graphqls:
- description: This is a conceptual GraphQL schema for the Snapchat platform, covering the Snap Kit developer APIs (Login Kit, Creative Kit, Camera Kit), the Snapchat Ads API (Marketing API), the Conversions API, an
  name: Snapchat GraphQL Schema
  slug: snapchat-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/snapchat.png
json_schemas:
- name: Snapchat Ad Campaign
  property_count: 0
  slug: snapchat-ad-campaign
- name: Ad
  property_count: 8
  slug: snapchat-ad
- name: AdAccount
  property_count: 11
  slug: snapchat-adaccount
- name: AdSquad
  property_count: 14
  slug: snapchat-adsquad
- name: AppData
  property_count: 3
  slug: snapchat-appdata
- name: AudienceSegment
  property_count: 9
  slug: snapchat-audiencesegment
- name: Campaign
  property_count: 11
  slug: snapchat-campaign
- name: ContentItem
  property_count: 5
  slug: snapchat-contentitem
- name: Snapchat Conversion Event
  property_count: 1
  slug: snapchat-conversion-event
- name: ConversionEvent
  property_count: 8
  slug: snapchat-conversionevent
- name: ConversionEventRequest
  property_count: 1
  slug: snapchat-conversioneventrequest
- name: ConversionEventResponse
  property_count: 2
  slug: snapchat-conversioneventresponse
- name: Creative
  property_count: 12
  slug: snapchat-creative
- name: CustomData
  property_count: 8
  slug: snapchat-customdata
- name: ErrorResponse
  property_count: 3
  slug: snapchat-errorresponse
- name: FundingSource
  property_count: 9
  slug: snapchat-fundingsource
- name: Media
  property_count: 7
  slug: snapchat-media
- name: OAuthError
  property_count: 2
  slug: snapchat-oautherror
- name: Organization
  property_count: 13
  slug: snapchat-organization
- name: Stats
  property_count: 4
  slug: snapchat-stats
- name: TokenResponse
  property_count: 5
  slug: snapchat-tokenresponse
- name: UserData
  property_count: 18
  slug: snapchat-userdata
- name: UserProfile
  property_count: 1
  slug: snapchat-userprofile
json_structures:
- name: Snapchat Campaign Structure
  property_count: 0
  slug: snapchat-campaign-structure
- name: Snapchat Structure
  property_count: 0
  slug: snapchat-structure
jsonld:
- class_count: 0
  name: Snapchat Context
  property_count: 10
  slug: snapchat-context
layout: provider
modified: '2026-05-19'
name: Snapchat
nav: Providers
network: true
overview: 'Snapchat publishes 13 APIs on the [APIs.io](https://apis.io/) network, including Ads API, Ad Accounts API, Ad Squads API, and 10 more. Tagged areas include Advertising, AR, Augmented Reality, Marketing, and Messaging.


  The Snapchat catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Snapchat''s developer surface includes authentication, documentation, engineering blog, support, pricing, signup flow, and 11 more developer resources.'
plans:
- name: Snapchat Plans Pricing
  plan_count: 1
  slug: snapchat-plans-pricing
random_paper: 40
rate_limits:
- limit_count: 2
  name: Snapchat Rate Limits
  slug: snapchat-rate-limits
rules:
- name: Snapchat API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: snapchat-jsonschema-spectral-rules
- name: Snapchat API Rules
  rule_count: 10
  severity_counts:
    error: 1
    hint: 0
    info: 4
    warn: 5
  slug: snapchat-rules
scopes:
- name: Snapchat Scopes
  scope_count: 1
  slug: snapchat-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: strong
  composite: 57.0
  delta: -2.5
  facets:
    commercial_clarity: 73.7
    contract_quality: 72.7
    developer_ergonomics: 34.8
    discoverability: 64.8
    governance: 58.3
    operational_transparency: 26.3
  previous_composite: 59.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 13
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 58.3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/snapchat/refs/heads/main/screenshots/snapchat-2026-06-20T194106.png
security:
- kind: authentication
  name: Snapchat Authentication
  slug: snapchat-authentication
  summary_line: apiKey/http/oauth2 · 3 schemes
- kind: domain-security
  name: Snapchat Domain Security
  slug: snapchat-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: snapchat
tags:
- Advertising
- AR
- Augmented Reality
- Marketing
- Messaging
- Social Media
website: https://snap.com
---
