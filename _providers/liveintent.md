---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 54.5
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 12
  human_in_the_loop: 0
  name: Liveintent Agentic Access
  operation_count: 20
  slug: liveintent-agentic-access
  summary_line: 20 operations · 12 acting
api_count: 4
apis:
- description: Programmatically create and manage LiveIntent custom audiences. Partners create an audience, mint a signed URL to upload member hashes out of band, poll upload status, read daily total and match count
  name: LiveIntent Audiences API
  slug: audiences
- description: Submit data subject requests to LiveIntent programmatically to satisfy CCPA and GDPR obligations. Supports RESTRICT (opt out of sale), ERASURE (delete) and ACCESS (produce a report) actions against ha
  name: LiveIntent Privacy Management API
  slug: privacy
- description: Query LiveIntent publisher and advertiser reporting data. A single executeQuery endpoint accepts a report type, an absolute or dynamic date interval, a granularity of day, week, month or all, plus spl
  name: LiveIntent Reporting API
  slug: reporting
- description: LiveIntent's exchange-side real-time bidding integration for demand-side platforms. It implements a subset of the IAB OpenRTB API Specification 2.5 together with OpenRTB Native Ads 1.1 and 1.2, passin
  name: LiveIntent Programmatic Bidding API
  slug: programmatic-bidding
artifact_total: 10
asyncapis:
- description: ''
  name: Liveintent Events
  slug: liveintent-events
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/liveintent-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/liveintent-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.liveintent.com
- group: company
  title: ''
  type: Blog
  url: https://www.liveintent.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://support.liveintent.com/hc/en-us
- group: docs
  title: ''
  type: Documentation
  url: https://support.liveintent.com/hc/en-us
- group: start
  title: ''
  type: Login
  url: https://platform.liveintent.com/login/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.liveintent.com/privacy-policy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/LiveIntent
- group: build
  title: ''
  type: Packages
  url: packages/liveintent-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/liveintent-packages.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/liveintent-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/liveintent-llms.txt
- group: docs
  title: ''
  type: APIReference
  url: https://support.liveintent.com/hc/en-us/sections/360009709692-LiveIntent-APIs
- group: start
  title: ''
  type: SignUp
  url: https://www.liveintent.com/get-started/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.liveintent.com
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/liveintent-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/liveintent-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/liveintent-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/liveintent-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/liveintent-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/liveintent-sandbox.yml
- group: build
  title: ''
  type: CLI
  url: cli/liveintent-cli.yml
- group: design
  title: ''
  type: Components
  url: components/liveintent-components.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/liveintent-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/liveintent-rate-limits.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/liveintent-audiences-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/liveintent-privacy-overlay.yaml
created: '2026-07-17'
description: LiveIntent is a people-based email marketing, advertising and identity platform serving more than 2,500 businesses. It connects marketers and publishers through email-native audience targeting, publisher inventory monetization (LiveTag and native ad blueprints), and identity resolution across the digital ecosystem, including its HIRO first-party data solution and email reactivation services. LiveIntent publishes four partner APIs — an Audiences API and a Privacy Management API, both backed by OpenAPI 3.0.0 definitions rendered through Redocly; a Reporting API for publisher and advertiser metrics; and a Programmatic Bidding API implementing a subset of IAB OpenRTB 2.5 with OpenRTB Native 1.1 and 1.2 — alongside the open-source LiveConnect first-party identity library (npm live-connect-js) and partner data integrations with Segment, Oracle, Adobe, Merkle and LiveRamp. All API access is bearer-token based and provisioned by a LiveIntent account team rather than self-service. LiveIntent
  has been acquired by Zeta Global. Backed by Battery Ventures and Bullpen Capital.
image: https://www.liveintent.com/favicon.ico
layout: provider
modified: '2026-08-12'
name: LiveIntent
nav: Providers
network: true
overview: 'LiveIntent publishes 2 APIs on the [APIs.io](https://apis.io/) network: Audiences API and Privacy Management API. Tagged areas include Company, Advertising, AdTech, Identity, and Email Marketing.


  The LiveIntent catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  LiveIntent''s developer surface includes authentication, engineering blog, support, documentation, API reference, signup flow, sandbox, and 22 more developer resources.'
plans:
- name: Liveintent Plans Pricing
  plan_count: 0
  slug: liveintent-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 0
  name: Liveintent Rate Limits
  slug: liveintent-rate-limits
score:
  band: developing
  composite: 42.1
  delta: 26.6
  facets:
    commercial_clarity: 23.7
    contract_quality: 52.6
    developer_ergonomics: 58.7
    discoverability: 72.2
    governance: 20.8
    operational_transparency: 21.1
  previous_composite: 15.5
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/liveintent/refs/heads/main/screenshots/liveintent-2026-07-25T225352.png
security:
- kind: authentication
  name: Liveintent Authentication
  slug: liveintent-authentication
  summary_line: apiKey/http · 1 scheme
- kind: domain-security
  name: Liveintent Domain Security
  slug: liveintent-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: liveintent
tags:
- Company
- Advertising
- AdTech
- Identity
- Email Marketing
- Audience
- Publishers
- Marketers
- Data
website: https://www.liveintent.com
---
