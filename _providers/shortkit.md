---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    asyncapi_events: true
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.1
  scored_at: '2026-07-28'
api_count: 5
apis:
- description: How ad slots are interleaved into the feed.
  name: ShortKit Ad Configuration API
  slug: shortkit-ad-configuration-api
- description: Events and metrics for user interaction with your content.
  name: ShortKit Analytics API
  slug: shortkit-analytics-api
- description: Videos, image carousels, and video carousels in your feed.
  name: ShortKit Content API
  slug: shortkit-content-api
- description: Real-time broadcasts that appear in the feed alongside on-demand content.
  name: ShortKit Live Streams API
  slug: shortkit-live-streams-api
- description: Short polls injected between content items in the feed.
  name: ShortKit Surveys API
  slug: shortkit-surveys-api
artifact_total: 9
asyncapis:
- description: ''
  name: Shortkit Webhooks
  slug: shortkit-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/shortkit-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.shortkit.dev
- group: start
  title: ''
  type: DeveloperPortal
  url: https://portal.shortkit.dev
- group: docs
  title: ''
  type: Documentation
  url: https://www.shortkit.dev/docs
- group: docs
  title: ''
  type: APIReference
  url: https://www.shortkit.dev/docs/api/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://www.shortkit.dev/docs/quickstart
- group: commercial
  title: ''
  type: Pricing
  url: https://www.shortkit.dev/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.shortkit.dev/blog
- group: start
  title: ''
  type: SignUp
  url: https://portal.shortkit.dev
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.shortkit.dev/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.shortkit.dev/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/shortkit
- group: build
  title: ''
  type: Packages
  url: packages/shortkit-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/shortkit-packages.yml
- group: design
  title: ''
  type: Components
  url: components/shortkit-components.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/shortkit-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/shortkit-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/shortkit-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/shortkit-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/shortkit-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/shortkit-webhooks.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/shortkit-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/shortkit-llms.txt
- group: start
  title: ''
  type: Sandbox
  url: sandbox/shortkit-sandbox.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: ShortKit is a Y Combinator-backed short-form vertical video platform that gives product teams a drop-in, TikTok-quality video experience without the infrastructure complexity. It ships native SDKs for iOS, Android, Flutter, React Native, Expo and Web alongside a REST API for managing content, direct uploads, live streams, in-feed surveys, analytics events and ad configuration. The platform handles adaptive-bitrate HLS transcoding, global CDN delivery across 300+ points of presence, automatic caption generation with language detection, protected/signed playback, and native ad insertion (Google Ad Manager / VAST / IMA). Developer docs are partner-gated but the Mintlify API reference and the iOS SDK are published openly on GitHub.
image: https://www.shortkit.dev/icon.svg
layout: provider
mcp_servers:
- description: ''
  name: shortkit-mcp.yml
  slug: shortkit-mcpyml
modified: '2026-07-21'
name: ShortKit
nav: Providers
network: true
overview: 'ShortKit publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Ad Configuration API, Analytics API, Content API, and 2 more. Tagged areas include Company, Video, Short-Form Video, Video SDK, and Streaming.


  The ShortKit catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  ShortKit''s developer surface includes documentation, API reference, getting-started guide, pricing, engineering blog, signup flow, sandbox, and 18 more developer resources.'
random_paper: 68
score:
  band: developing
  composite: 48.1
  delta: -2.1
  facets:
    commercial_clarity: 44.7
    contract_quality: 64.2
    developer_ergonomics: 53.8
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 13.2
  previous_composite: 50.2
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Shortkit Authentication
  slug: shortkit-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Shortkit Domain Security
  slug: shortkit-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: shortkit
tags:
- Company
- Video
- Short-Form Video
- Video SDK
- Streaming
- Live Streaming
- Content Delivery
- Analytics
- Advertising
- Y Combinator
website: https://www.shortkit.dev
---
