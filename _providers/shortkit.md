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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.6
  scored_at: '2026-09-02'
api_count: 1
apis:
- baseURL: https://api.shortkit.dev/v1
  baseurl_source: declared
  description: How ad slots are interleaved into the feed.
  name: ShortKit Ad Configuration API
  slug: shortkit-ad-configuration-api
- baseURL: https://api.shortkit.dev/v1
  baseurl_source: declared
  description: Events and metrics for user interaction with your content.
  name: ShortKit Analytics API
  slug: shortkit-analytics-api
- baseURL: https://api.shortkit.dev/v1
  baseurl_source: declared
  description: Videos, image carousels, and video carousels in your feed.
  name: ShortKit Content API
  slug: shortkit-content-api
- baseURL: https://api.shortkit.dev/v1
  baseurl_source: declared
  description: Real-time broadcasts that appear in the feed alongside on-demand content.
  name: ShortKit Live Streams API
  slug: shortkit-live-streams-api
- baseURL: https://api.shortkit.dev/v1
  baseurl_source: declared
  description: Short polls injected between content items in the feed.
  name: ShortKit Surveys API
  slug: shortkit-surveys-api
artifact_total: 15
asyncapis:
- description: ''
  name: Shortkit Webhooks
  slug: shortkit-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: ShortKit Ad Configuration API
  slug: open-shortkit-ad-configuration-api
- collection_type: open
  name: ShortKit Ad Configuration Analytics API
  slug: open-shortkit-analytics-api
- collection_type: open
  name: ShortKit Ad Configuration Content API
  slug: open-shortkit-content-api
- collection_type: open
  name: ShortKit Ad Configuration Live Streams API
  slug: open-shortkit-live-streams-api
- collection_type: open
  name: ShortKit Ad Configuration Surveys API
  slug: open-shortkit-surveys-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/shortkit-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/shortkit-openapi-overlay.yaml
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
  name: ShortKit MCP Server
  slug: shortkit-mcp-server
modified: '2026-07-21'
name: ShortKit
nav: Providers
network: true
overview: 'ShortKit publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Ad Configuration API, Analytics API, Content API, and 2 more. Tagged areas include Company, Video, Short-Form Video, Video SDK, and Streaming.


  The ShortKit catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  ShortKit''s developer surface includes documentation, API reference, getting-started guide, pricing, engineering blog, signup flow, sandbox, and 20 more developer resources.'
random_paper: 6
score:
  band: developing
  composite: 43.4
  coverage:
    artifact_dirs: 21
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 4.5
    contract_quality: 60.3
    developer_ergonomics: 49.4
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 10.5
  previous_composite: 43.4
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/shortkit/refs/heads/main/screenshots/shortkit-2026-08-17T081844.png
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
