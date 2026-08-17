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
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 55.9
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 18
  human_in_the_loop: 0
  name: Snapchat Agentic Access
  operation_count: 42
  slug: snapchat-agentic-access
  summary_line: 42 operations · 18 acting
api_count: 17
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
- description: Snap's first-party hosted Model Context Protocol server for the Snapchat Ads API. A supported agent connects over streamable HTTP to https://mcp.snapchat.com/ads and authenticates with OAuth 2.0 (auth
  name: Snapchat Ads MCP Server
  slug: snapchat-ads-mcp
artifact_total: 74
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Snapchat Ads Ad Accounts API
  slug: open-snapchat-ad-accounts-api
- collection_type: open
  name: Snapchat Ads Ad Accounts Ad Squads API
  slug: open-snapchat-ad-squads-api
- collection_type: open
  name: Snapchat Ad Accounts Ads API
  slug: open-snapchat-ads-api
- collection_type: open
  name: Snapchat Ads Ad Accounts Audience Segments API
  slug: open-snapchat-audience-segments-api
- collection_type: open
  name: Snapchat Ads Ad Accounts Campaigns API
  slug: open-snapchat-campaigns-api
- collection_type: open
  name: Snapchat Ads Ad Accounts Conversion Events API
  slug: open-snapchat-conversion-events-api
- collection_type: open
  name: Snapchat Conversions API
  slug: open-snapchat-conversions-api
- collection_type: open
  name: Snapchat Ads Ad Accounts Creatives API
  slug: open-snapchat-creatives-api
- collection_type: open
  name: Snapchat Ads Ad Accounts Funding Sources API
  slug: open-snapchat-funding-sources-api
- collection_type: open
  name: Snapchat Login Kit API
  slug: open-snapchat-login-kit
- collection_type: open
  name: Snapchat Ads Ad Accounts Measurement API
  slug: open-snapchat-measurement-api
- collection_type: open
  name: Snapchat Ads Ad Accounts Media API
  slug: open-snapchat-media-api
- collection_type: open
  name: Snapchat Ads Ad Accounts OAuth API
  slug: open-snapchat-oauth-api
- collection_type: open
  name: Snapchat Ads Ad Accounts Organizations API
  slug: open-snapchat-organizations-api
- collection_type: open
  name: Snapchat Ads Ad Accounts User Profile API
  slug: open-snapchat-user-profile-api
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
- group: build
  title: ''
  type: Packages
  url: packages/snapchat-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/snapchat-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/snapchat-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/snapchat-security.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/snapchat-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/snapchat-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/snapchat-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/snapchat-ads-api-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/snapchat-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/snapchat-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/snapchat-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/snapchat-lifecycle.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/snapchat-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/snapchat-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/snapchat-trust-center.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/snapchat-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/snapchat-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/snapchat-changelog.yml
- group: design
  title: ''
  type: Components
  url: components/snapchat-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/snapchat-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/snapchat-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/snapchat-rate-limits.yml
- group: docs
  title: ''
  type: APIReference
  url: https://developers.snap.com/marketing-api/Ads-API/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.snap.com/marketing-api/home
- group: operate
  title: ''
  type: ChangeLog
  url: https://developers.snap.com/marketing-api/Ads-API/changelog
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
mcp_servers:
- description: ''
  name: snapchat-mcp.yml
  slug: snapchat-mcpyml
modified: '2026-08-13'
name: Snapchat
nav: Providers
network: true
overview: 'Snapchat publishes 13 APIs on the [APIs.io](https://apis.io/) network, including Ads API, Ad Accounts API, Ad Squads API, and 10 more. Tagged areas include Advertising, AR, Augmented Reality, Marketing, and Messaging.


  The Snapchat catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Snapchat''s developer surface includes authentication, documentation, engineering blog, support, pricing, signup flow, sandbox, and 36 more developer resources.'
plans:
- name: Snapchat Plans Pricing
  plan_count: 1
  slug: snapchat-plans-pricing
random_paper: 105
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
  scope_count: 7
  slug: snapchat-scopes
  summary_line: 7 scopes · authorizationCode/implicit
score:
  band: exemplar
  composite: 69.9
  delta: 17.7
  facets:
    commercial_clarity: 65.8
    contract_quality: 72.3
    developer_ergonomics: 80.4
    discoverability: 72.2
    governance: 79.2
    operational_transparency: 44.7
  previous_composite: 52.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 13
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/snapchat/refs/heads/main/screenshots/snapchat-2026-06-20T194106.png
security:
- kind: authentication
  name: Snapchat Authentication
  slug: snapchat-authentication
  summary_line: oauth2/http/apiKey · 5 schemes
- kind: domain-security
  name: Snapchat Domain Security
  slug: snapchat-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Snapchat Vulnerability Disclosure
  slug: snapchat-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Snapchat Trust Center
  slug: snapchat-trust-center
  summary_line: trust center published
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
