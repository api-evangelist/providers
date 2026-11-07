---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
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
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 20.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 13
  human_in_the_loop: 0
  name: Whereby Agentic Access
  operation_count: 27
  slug: whereby-agentic-access
  summary_line: 27 operations · 13 acting
api_count: 1
apis:
- description: Bearer-authenticated REST API for creating meeting rooms, managing live sessions, retrieving recordings, transcriptions, summaries, and pulling usage insights. Base URL https://api.whereby.dev/v1.
  name: Whereby REST API
  slug: whereby-rest-api
- description: Outbound webhook notifications for room and session lifecycle events including client join/leave, knock, session start/end, recording finished, transcription started/finished/failed, and assistant req
  name: Whereby Webhooks
  slug: whereby-webhooks
- baseURL: https://api.whereby.dev/v1
  baseurl_source: spec
  description: The Insights API from Whereby — 4 operation(s) for insights.
  name: Whereby Insights API
  slug: whereby-insights-api
- baseURL: https://api.whereby.dev/v1
  baseurl_source: spec
  description: The Meetings API from Whereby — 2 operation(s) for meetings.
  name: Whereby Meetings API
  slug: whereby-meetings-api
- baseURL: https://api.whereby.dev/v1
  baseurl_source: spec
  description: The Recordings API from Whereby — 4 operation(s) for recordings.
  name: Whereby Recordings API
  slug: whereby-recordings-api
- baseURL: https://api.whereby.dev/v1
  baseurl_source: spec
  description: The Rooms API from Whereby — 4 operation(s) for rooms.
  name: Whereby Rooms API
  slug: whereby-rooms-api
- baseURL: https://api.whereby.dev/v1
  baseurl_source: spec
  description: The Summaries API from Whereby — 2 operation(s) for summaries.
  name: Whereby Summaries API
  slug: whereby-summaries-api
- baseURL: https://api.whereby.dev/v1
  baseurl_source: spec
  description: The Transcriptions API from Whereby — 4 operation(s) for transcriptions.
  name: Whereby Transcriptions API
  slug: whereby-transcriptions-api
artifact_total: 37
asyncapis:
- description: ''
  name: Review
  slug: review
collections:
- collection_type: open
  name: Whereby REST Insights API
  slug: open-whereby-insights-api
- collection_type: open
  name: Whereby REST Insights Meetings API
  slug: open-whereby-meetings-api
- collection_type: open
  name: Whereby REST Insights Recordings API
  slug: open-whereby-recordings-api
- collection_type: open
  name: Whereby REST Insights Rooms API
  slug: open-whereby-rooms-api
- collection_type: open
  name: Whereby REST Insights Summaries API
  slug: open-whereby-summaries-api
- collection_type: open
  name: Whereby REST Insights Transcriptions API
  slug: open-whereby-transcriptions-api
- collection_type: open
  name: Whereby REST API
  slug: open-whereby
common:
- group: commercial
  href: https://artifacts.apis.io/whereby/plans/whereby-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/whereby-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/whereby/rate-limits/whereby-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/whereby-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/whereby/finops/whereby-finops.yml
  title: ''
  type: FinOps
  url: finops/whereby-finops.yml
- group: agent
  href: https://artifacts.apis.io/whereby/agentic-access/whereby-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/whereby-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/whereby/security/whereby-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/whereby-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/whereby/security/whereby-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/whereby-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/whereby/authentication/whereby-authentication.yml
  title: ''
  type: Authentication
  url: authentication/whereby-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://whereby.com
- group: other
  title: ''
  type: Product
  url: https://whereby.com/information/embedded/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.whereby.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.whereby.com/reference/whereby-rest-api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.whereby.com/reference/getting-started
- group: auth
  title: ''
  type: Authentication
  url: https://docs.whereby.com/reference/authentication
- group: commercial
  title: ''
  type: Pricing
  url: https://whereby.com/information/embedded/pricing
- group: start
  title: ''
  type: Signup
  url: https://whereby.com/org/signup/embedded?signupFlowPlanType=embedded_free
- group: other
  title: ''
  type: Product
  url: https://whereby.com/information/select-product
- group: operate
  title: ''
  type: Support
  url: https://whereby.frontkb.com/en
- group: operate
  title: ''
  type: StatusPage
  url: https://wherebystatus.com/
- group: company
  title: ''
  type: Blog
  url: https://whereby.com/blog/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://whereby.com/information/tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://whereby.com/information/tos/privacy-policy/
- group: company
  title: ''
  type: Careers
  url: https://careers.whereby.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/whereby
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/whereby
- group: build
  title: ''
  type: SDKs
  url: https://docs.whereby.com/reference/sdks
- group: design
  title: ''
  type: WebComponent
  url: https://docs.whereby.com/reference/web-component
- group: build
  title: ''
  type: BrowserSDK
  url: https://docs.whereby.com/reference/browser-sdk
- group: build
  title: ''
  type: AndroidSDK
  url: https://docs.whereby.com/reference/android-sdk
- group: build
  title: ''
  type: iOSSDK
  url: https://docs.whereby.com/reference/ios-sdk
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.whereby.com/llms.txt
created: '2026-05-23'
description: Whereby is an embeddable video API plus standalone meetings product that lets developers add browser-based, no-download video calls to their apps with a few lines of code or build deeply customized experiences via SDKs. The REST API at api.whereby.dev/v1 covers meetings, rooms, recordings, transcriptions, summaries, and insights.
features:
- Embeddable video calls via iframe, Web Component, or React Browser SDK
- Native Android and iOS SDKs
- REST API for programmatic meeting and room creation
- Cloud recording with retrieval via API
- AI-generated transcriptions and meeting summaries
- Breakout groups, in-call chat, and file sharing
- Pre-call device and connectivity checks
- Webhooks for room, session, recording, transcription, and assistant events
- Whereby-Signature HMAC verification on webhook deliveries
- Point-based rate limiting (100/min Build, 1000/min Enterprise)
- GDPR and ISO 27001 compliance, optional HIPAA configuration
- Global mesh network for low-latency media
finops:
- has_sources: true
  method: derived
  name: Whereby Finops
  primary_unit: subscription
  service_category: ''
  slug: whereby-finops
  template: false
image: https://whereby.com/static/whereby-logo.svg
layout: provider
modified: '2026-05-23'
name: Whereby
nav: Providers
network: true
overview: 'Whereby publishes 8 API contracts indexed on the [APIs.io](https://apis.io/) network, including Insights API, Meetings API, Recordings API, and 5 more. Tagged areas include Video, Communications, Real-Time, WebRTC, and Embedded.


  The Whereby catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Whereby''s developer surface includes authentication, documentation, API reference, getting-started guide, pricing, signup flow, support, and 23 more developer resources.'
plans:
- name: Whereby Plans Pricing
  plan_count: 3
  slug: whereby-plans-pricing
- name: Whereby Price Estimates
  plan_count: 0
  slug: whereby-price-estimates
random_paper: 14
rate_limits:
- limit_count: 2
  name: Whereby Rate Limits
  slug: whereby-rate-limits
rules:
- authorship: generated
  effective_rule_count: 93
  extends:
  - spectral:oas
  name: Whereby API Rules
  rule_count: 52
  severity_counts:
    error: 50
    hint: 0
    info: 1
    warn: 1
  slug: whereby-rules
score:
  band: developing
  composite: 53.1
  coverage:
    artifact_dirs: 18
    catalog_earned: 48.5
    catalog_earned_first_party: 12.0
    catalog_gap: 66.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 92.1
    contract_governance: 13.6
    contract_quality: 49.7
    developer_ergonomics: 54.8
    discoverability: 55.4
    operational_transparency: 26.3
  previous_composite: 53.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/whereby/whereby-2026-06-20T201431.png
security:
- kind: authentication
  name: Whereby Authentication
  slug: whereby-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Whereby Domain Security
  slug: whereby-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
- kind: trust-center
  name: Whereby Trust Center
  slug: whereby-trust-center
  summary_line: ISO 27001, HIPAA, GDPR
slug: whereby
tags:
- Video
- Communications
- Real-Time
- WebRTC
- Embedded
- Meetings
- Collaboration
website: https://whereby.com
---
