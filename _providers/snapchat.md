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
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.9
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 18
  human_in_the_loop: 0
  name: Snapchat Agentic Access
  operation_count: 42
  slug: snapchat-agentic-access
  summary_line: 42 operations · 18 acting
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
- description: Endpoints for sending web, app, and offline conversion events to Snap for campaign measurement and optimization.
  name: Snapchat Conversion Events API
  slug: snapchat-conversion-events-api
- description: OAuth 2.0 authorization and token management endpoints for authenticating users via their Snapchat account.
  name: Snapchat OAuth API
  slug: snapchat-oauth-api
- description: Endpoints for retrieving authenticated user profile information including display name and Bitmoji avatar.
  name: Snapchat User Profile API
  slug: snapchat-user-profile-api
- description: Snap's first-party hosted Model Context Protocol server for the Snapchat Ads API. A supported agent connects over streamable HTTP to https://mcp.snapchat.com/ads and authenticates with OAuth 2.0 (auth
  name: Snapchat Ads MCP Server
  slug: snapchat-ads-mcp
artifact_total: 64
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
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/snapchat-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/snapchat-ad-accounts-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/snapchat-ad-squads-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/snapchat-audience-segments-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/snapchat-campaigns-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/snapchat-creatives-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/snapchat-funding-sources-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/snapchat-measurement-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/snapchat-media-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/snapchat-organizations-api-overlay.yaml
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/Snapchat/creative-kit/issues
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
- description: Snap ships a first-party, hosted, remote MCP server for the Snapchat Ads API. A supported agent POSTs directly to https://mcp.snapchat.com/ads over streamable HTTP and authenticates with OAuth 2.0 (au
  name: Snapchat Ads MCP Server
  slug: snapchat-ads-mcp-server
modified: '2026-08-13'
name: Snapchat
nav: Providers
network: true
overview: 'Snapchat publishes 3 APIs on the [APIs.io](https://apis.io/) network: Conversion Events API, OAuth API, and User Profile API. Tagged areas include Advertising, AR, Augmented Reality, Marketing, and Messaging.


  The Snapchat catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Snapchat''s developer surface includes authentication, documentation, engineering blog, support, pricing, signup flow, sandbox, and 47 more developer resources.'
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
- effective_rule_count: 6
  extends: []
  name: Snapchat API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: snapchat-jsonschema-spectral-rules
- effective_rule_count: 51
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
  composite: 56.9
  coverage:
    artifact_dirs: 33
    catalog_gap: 51.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.5
  facets:
    access_clarity: 71.1
    commercial_clarity: 71.1
    contract_governance: 31.8
    contract_quality: 65.3
    developer_ergonomics: 73.2
    discoverability: 66.7
    governance: 31.8
    operational_transparency: 57.9
  open_source:
    applies: true
    score: 0.0
  previous_composite: 57.4
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
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
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
- Social-Media
website: https://snap.com
---
