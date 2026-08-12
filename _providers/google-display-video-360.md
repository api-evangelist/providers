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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Google Display Video 360 Agentic Access
  operation_count: 5
  slug: google-display-video-360-agentic-access
  summary_line: 5 operations
api_count: 1
apis:
- description: The Advertisers API from Google Display & Video 360 — 5 operation(s) for advertisers.
  name: Google Display & Video 360 Advertisers API
  slug: google-display-video-360-advertisers-api
artifact_total: 13
collections:
- collection_type: postman
  name: Google Display & Video 360 Advertisers API
  slug: postman-google-display-video-360-advertisers-api
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
- group: auth
  title: ''
  type: Authentication
  url: https://developers.google.com/display-video/api/guides/authentication
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
  type: StatusPage
  url: https://status.cloud.google.com/
- group: operate
  title: ''
  type: Support
  url: https://developers.google.com/display-video/api/support
- group: design
  title: ''
  type: JSONLD
  url: json-ld/json-ld.yml
created: '2026-03-13'
description: The Display & Video 360 API enables programmatic management of display, video, and audio advertising campaigns. It provides access to advertisers, campaigns, insertion orders, line items, creatives, targeting, and audience management for enterprise-scale programmatic buying.
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
modified: '2026-05-19'
name: Google Display & Video 360
nav: Providers
network: true
overview: 'Google Display & Video 360 publishes 1 API on the [APIs.io](https://apis.io/) network: Advertisers API. Tagged areas include Campaign Management, Display Ads, DV360, Programmatic Advertising, and Targeting.


  The Google Display & Video 360 catalog on APIs.io includes 1 Spectral governance ruleset.


  Google Display & Video 360''s developer surface includes authentication, developer portal, getting-started guide, documentation, pricing, support, and 11 more developer resources.'
plans:
- name: Google Display Video 360 Plans Pricing
  plan_count: 3
  slug: google-display-video-360-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 5
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
  scope_count: 1
  slug: google-display-video-360-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: developing
  composite: 53.1
  delta: -8.4
  facets:
    commercial_clarity: 47.4
    contract_quality: 66.0
    developer_ergonomics: 47.8
    discoverability: 68.5
    governance: 58.3
    operational_transparency: 28.9
  previous_composite: 61.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: falling
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
website: https://developers.google.com/display-video
---
