---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: true
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
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 48.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Snapchat Agentic Access
  operation_count: 5
  slug: snapchat-agentic-access
  summary_line: 5 operations · 3 acting
api_count: 2
apis:
- description: Creative Kit allows developers to let users share content including Lenses, AR experiences, filters, GIFs, videos, links, and captions from a website or app directly to Snapchat's camera or preview sc
  name: Snapchat Creative Kit
  slug: snapchat-creative-kit
- description: Camera Kit enables developers to integrate Snap's AR camera technology directly into iOS, Android, and web applications, giving users access to Snap's lens library and AR experiences without leaving t
  name: Snapchat Camera Kit
  slug: snapchat-camera-kit
- description: Lens Studio is Snap's desktop application for building augmented reality lenses for Snapchat and Spectacles. Provides an API for scripting lens behaviors, integrating dynamic data, and publishing to t
  name: Lens Studio
  slug: snapchat-lens-studio
- baseURL: https://tr.snapchat.com/v3
  baseurl_source: declared
  description: Endpoints for sending web, app, and offline conversion events to Snap for campaign measurement and optimization.
  name: Snapchat Conversion Events API
  phrasing_intents:
  - id: sendWebConversionEvents
    intent: Send website conversion events to a Snap Pixel
    question: How do I send purchases and page views from my website to Snapchat server-side?
  - id: sendAppConversionEvents
    intent: Send in-app conversion events for a Snap App
    question: How do I tell Snapchat about installs and in-app purchases from my mobile app?
  phrasing_ops: 2
  slug: snapchat-conversion-events-api
- baseURL: https://kit.snapchat.com/v1
  baseurl_source: declared
  description: Endpoints for retrieving authenticated user profile information including display name and Bitmoji avatar.
  name: Snapchat User Profile API
  phrasing_intents:
  - id: getUserProfile
    intent: Get the signed-in Snapchat user's profile
    question: How do I get the display name of the user who logged in with Snapchat?
  phrasing_ops: 1
  slug: snapchat-user-profile-api
- description: Snap's first-party hosted Model Context Protocol server for the Snapchat Ads API. A supported agent connects over streamable HTTP to https://mcp.snapchat.com/ads and authenticates with OAuth 2.0 (auth
  name: Snapchat Ads MCP Server
  slug: snapchat-ads-mcp
- baseURL: https://tr.snapchat.com/v3
  baseurl_source: declared
  description: OAuth 2.0 authorization and token management endpoints for authenticating users via their Snapchat account.
  name: Snapchat O Auth API
  phrasing_intents:
  - id: authorize
    intent: Start Snapchat login and request user consent
    question: How do I send a user to Snapchat to log in and approve my app?
  - id: exchangeToken
    intent: Exchange an auth code or refresh an access token
    question: How do I turn the Snapchat authorization code into an access token?
  phrasing_ops: 2
  slug: snapchat-oauth-api
artifact_total: 66
collections:
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
- group: commercial
  href: https://artifacts.apis.io/snapchat/finops/snapchat-finops.yml
  title: ''
  type: FinOps
  url: finops/snapchat-finops.yml
- group: other
  href: https://artifacts.apis.io/snapchat/overlays/snapchat-oauth-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/snapchat-oauth-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/snapchat/capabilities/snapchat-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/snapchat-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/snapchat/overlays/snapchat-ad-accounts-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/snapchat-ad-accounts-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/snapchat/overlays/snapchat-ad-squads-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/snapchat-ad-squads-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/snapchat/overlays/snapchat-audience-segments-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/snapchat-audience-segments-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/snapchat/overlays/snapchat-campaigns-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/snapchat-campaigns-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/snapchat/overlays/snapchat-creatives-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/snapchat-creatives-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/snapchat/overlays/snapchat-funding-sources-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/snapchat-funding-sources-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/snapchat/overlays/snapchat-measurement-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/snapchat-measurement-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/snapchat/overlays/snapchat-media-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/snapchat-media-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/snapchat/overlays/snapchat-organizations-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/snapchat-organizations-api-overlay.yaml
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/Snapchat/creative-kit/issues
- group: agent
  href: https://artifacts.apis.io/snapchat/agentic-access/snapchat-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/snapchat-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/snapchat/security/snapchat-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/snapchat-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/snapchat/authentication/snapchat-authentication.yml
  title: ''
  type: Authentication
  url: authentication/snapchat-authentication.yml
- group: auth
  href: https://artifacts.apis.io/snapchat/scopes/snapchat-scopes.yml
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
  href: https://artifacts.apis.io/snapchat/packages/snapchat-packages.yml
  title: ''
  type: Packages
  url: packages/snapchat-packages.yml
- group: build
  href: https://artifacts.apis.io/snapchat/packages/snapchat-packages.yml
  title: ''
  type: SDKs
  url: packages/snapchat-packages.yml
- group: agent
  href: https://artifacts.apis.io/snapchat/well-known/snapchat-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/snapchat-well-known.yml
- group: auth
  href: https://artifacts.apis.io/snapchat/well-known/snapchat-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/snapchat-security.txt
- group: agent
  href: https://artifacts.apis.io/snapchat/mcp/snapchat-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/snapchat-mcp.yml
- group: build
  href: https://artifacts.apis.io/snapchat/mcp/snapchat-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/snapchat-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/snapchat/llms/snapchat-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/snapchat-llms.txt
- group: other
  href: https://artifacts.apis.io/snapchat/overlays/snapchat-ads-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/snapchat-ads-api-overlay.yaml
- group: design
  href: https://artifacts.apis.io/snapchat/conformance/snapchat-conformance.yml
  title: ''
  type: Conformance
  url: conformance/snapchat-conformance.yml
- group: design
  href: https://artifacts.apis.io/snapchat/errors/snapchat-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/snapchat-problem-types.yml
- group: design
  href: https://artifacts.apis.io/snapchat/lifecycle/snapchat-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/snapchat-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/snapchat/lifecycle/snapchat-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/snapchat-lifecycle.yml
- group: auth
  href: https://artifacts.apis.io/snapchat/security/snapchat-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/snapchat-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/snapchat/security/snapchat-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/snapchat-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/snapchat/security/snapchat-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/snapchat-trust-center.yml
- group: start
  href: https://artifacts.apis.io/snapchat/sandbox/snapchat-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/snapchat-sandbox.yml
- group: design
  href: https://artifacts.apis.io/snapchat/conventions/snapchat-conventions.yml
  title: ''
  type: Conventions
  url: conventions/snapchat-conventions.yml
- group: operate
  href: https://artifacts.apis.io/snapchat/changelog/snapchat-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/snapchat-changelog.yml
- group: design
  href: https://artifacts.apis.io/snapchat/components/snapchat-components.yml
  title: ''
  type: Components
  url: components/snapchat-components.yml
- group: design
  href: https://artifacts.apis.io/snapchat/data-model/snapchat-data-model.yml
  title: ''
  type: DataModel
  url: data-model/snapchat-data-model.yml
- group: agent
  href: https://artifacts.apis.io/snapchat/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  href: https://artifacts.apis.io/snapchat/plans/snapchat-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/snapchat-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/snapchat/rate-limits/snapchat-rate-limits.yml
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
- has_sources: true
  method: derived
  name: Snapchat Finops
  primary_unit: ''
  service_category: ''
  slug: snapchat-finops
  template: true
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
- description: Snap ships a first-party, hosted, remote MCP server for the Snapchat Ads API. A supported agent POSTs directly to https://mcp.snapchat.com/ads over streamable HTTP and authenticates with OAuth 2.0 (au
  name: Snapchat Ads MCP Server
  slug: snapchat-ads-mcp-server
modified: '2026-08-13'
name: Snapchat
nav: Providers
network: true
overview: 'Snapchat publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Conversion Events API, User Profile API, O Auth API, and 4 more. Tagged areas include Advertising, Augmented Reality, Marketing, Messaging, and Social Media.


  The Snapchat catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Snapchat''s developer surface includes authentication, documentation, engineering blog, support, pricing, signup flow, sandbox, and 49 more developer resources.'
plans:
- name: Snapchat Plans Pricing
  plan_count: 1
  slug: snapchat-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 2
  name: Snapchat Rate Limits
  slug: snapchat-rate-limits
rules:
- authorship: generated
  effective_rule_count: 6
  extends: []
  name: Snapchat — jsonschema rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: snapchat-jsonschema-spectral-rules
- authorship: unmarked
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: Snapchat API Rules
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
  band: strong
  composite: 65.7
  coverage:
    artifact_dirs: 36
    catalog_earned: 60.5
    catalog_earned_first_party: 16.0
    catalog_gap: 54.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 63.2
    contract_governance: 31.8
    contract_quality: 55.2
    developer_ergonomics: 73.2
    discoverability: 66.7
    operational_transparency: 57.9
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 65.7
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 13
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 45.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 27.8
screenshot: https://apis.io/screenshots/snapchat/snapchat-2026-06-20T194106.png
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
skill_count: 4
skills:
- name: snapchat-authenticate
  slug: snapchat-authenticate
- name: snapchat-launch-campaign
  slug: snapchat-launch-campaign
- name: snapchat-report-performance
  slug: snapchat-report-performance
- name: snapchat-send-conversion-events
  slug: snapchat-send-conversion-events
slug: snapchat
tags:
- Advertising
- Augmented Reality
- Marketing
- Messaging
- Social Media
website: https://snap.com
---
