---
access_model:
  confidence: high
  label: Enterprise · Contact sales
  onboarding: unknown
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
    agent_card: false
    agent_skills: true
    agentic_access: derived
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.4
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 156
  human_in_the_loop: 0
  name: Google Display Video 360 Agentic Access
  operation_count: 282
  slug: google-display-video-360-agentic-access
  summary_line: 282 operations · 156 acting
api_count: 2
apis:
- description: The full Display & Video 360 API surface — 179 operations across advertisers, partners, campaigns, insertion orders, line items, ad groups, creatives, ad assets, audiences, inventory sources, guarante
  name: Google Display & Video 360 API
  slug: google-display-video-360-api
- description: The advertiser-scoped slice of the Display & Video 360 API — 103 operations under /v4/advertisers covering campaigns, insertion orders, line items, ad groups, ad group ads, creatives, ad assets, chann
  name: Google Display & Video 360 Advertisers API
  slug: google-display-video-360-advertisers-api
artifact_total: 17
collections:
- collection_type: postman
  name: Google Display & Video 360 Advertisers API
  slug: postman-google-display-video-360-advertisers-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Google Display & Video 360 Advertisers API
  slug: open-google-display-video-360-advertisers-api
- collection_type: open
  name: Google Display & Video 360 API
  slug: open-google-display-video-360-api
- collection_type: open
  name: Google Display & Video 360 API
  slug: open-openapi
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/google-display--video-360/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/google-display-video-360-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-display-video-360-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://g.co/vrp
- group: auth
  title: ''
  type: DomainSecurity
  url: security/google-display-video-360-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/google-display-video-360-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/google-display-video-360-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/google-display-video-360-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/google-display-video-360-security.txt
- group: build
  title: ''
  type: Packages
  url: packages/google-display-video-360-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/google-display-video-360-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/google-display-video-360-llms.txt
- group: design
  title: ''
  type: Conventions
  url: conventions/google-display-video-360-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/google-display-video-360-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/google-display-video-360-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/google-display-video-360-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://developers.google.com/display-video/api/deprecations
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/google-display-video-360-changelog.yml
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://developers.google.com/display-video/api/release-notes
- group: design
  title: ''
  type: DataModel
  url: data-model/google-display-video-360-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: MCP
  url: mcp/google-display-video-360-mcp.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/google-display-video-360-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/google-display-video-360-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/google-display-video-360-finops.yml
- group: design
  title: ''
  type: Rules
  url: rules/google-display-video-360-jsonschema-spectral-rules.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/googleads
- group: start
  title: ''
  type: Portal
  url: https://developers.google.com/display-video
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.google.com/display-video/api/guides/getting-started/overview
- group: docs
  title: ''
  type: Documentation
  url: https://developers.google.com/display-video/api
- group: docs
  title: ''
  type: APIReference
  url: https://developers.google.com/display-video/api/reference/rest
- group: auth
  title: ''
  type: Authentication
  url: https://developers.google.com/display-video/api/guides/how-tos/authorizing
- group: company
  title: ''
  type: Blog
  url: https://ads-developers.googleblog.com/search/label/display_video_360
- group: start
  title: ''
  type: Login
  url: https://displayvideo.google.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://marketingplatform.google.com/about/display-video-360/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developers.google.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://policies.google.com/privacy
- group: operate
  title: ''
  type: Support
  url: https://developers.google.com/display-video/api/support
- group: design
  title: ''
  type: JSONLD
  url: json-ld/json-ld.yml
created: '2026-03-13'
description: Display & Video 360 is Google's enterprise demand-side platform for programmatic media buying, sold through Google Marketing Platform. Its API automates the whole buying structure — partners and advertisers, campaigns, insertion orders, line items, ad groups and ads, creatives and ad assets, first-party and Customer Match audiences, guaranteed orders and inventory sources, and the assigned targeting options that decide what a line item actually buys — plus Structured Data File bulk export and import. One REST surface at displayvideo.googleapis.com, version v4, 179 operations across 16 resource families, described by a first-party Google API Discovery Document. Google OAuth 2.0 only; there is no API key, and an access token is not sufficient on its own — the calling Google Account must also hold a Display & Video 360 user profile with permission on the partner or advertiser being addressed.
finops:
- name: Google Display Video 360 Finops
  service_category: API
  slug: google-display-video-360-finops
graphqls:
- description: Google DV360 is a demand-side platform for programmatic media buying. The API covers advertiser management, insertion orders, line items, targeting options, creatives, channels, and reporting.
  name: Google Display & Video 360 GraphQL API
  slug: google-display-video-360-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/google-display-video-360.png
layout: provider
modified: '2026-08-13'
name: Google Display & Video 360
nav: Providers
network: true
overview: 'Google Display & Video 360 publishes 2 APIs on the [APIs.io](https://apis.io/) network, including Advertisers API, and 1 more. Tagged areas include Campaign Management, Display Ads, DV360, Programmatic Advertising, and Targeting.


  The Google Display & Video 360 catalog on APIs.io includes 1 Spectral governance ruleset.


  Google Display & Video 360''s developer surface includes authentication, changelog, release notes, developer portal, getting-started guide, documentation, API reference, and 32 more developer resources.'
plans:
- name: Google Display Video 360 Plans Pricing
  plan_count: 0
  slug: google-display-video-360-plans-pricing
random_paper: 132
rate_limits:
- limit_count: 4
  name: Google Display Video 360 Rate Limits
  slug: google-display-video-360-rate-limits
rules:
- name: Google Display & Video 360 API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: google-display-video-360-jsonschema-spectral-rules
scopes:
- name: Google Display Video 360 Scopes
  scope_count: 4
  slug: google-display-video-360-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: strong
  composite: 65.3
  delta: 12.2
  facets:
    commercial_clarity: 52.6
    contract_quality: 66.0
    developer_ergonomics: 69.6
    discoverability: 87.0
    governance: 79.2
    operational_transparency: 47.4
  previous_composite: 53.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/google-display-video-360/refs/heads/main/screenshots/google-display-video-360-2026-06-20T182156.png
security:
- kind: authentication
  name: Google Display Video 360 Authentication
  slug: google-display-video-360-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Google Display Video 360 Domain Security
  slug: google-display-video-360-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Google Display Video 360 Vulnerability Disclosure
  slug: google-display-video-360-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: google-display-video-360
tags:
- Campaign Management
- Display Ads
- DV360
- Programmatic Advertising
- Targeting
- Video Ads
- Advertising
- AdTech
- Demand Side Platform
- Media Buying
- Audiences
- Google Marketing Platform
website: https://developers.google.com/display-video
---
