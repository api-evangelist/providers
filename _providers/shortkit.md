---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  - sandbox
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
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 26.0
  scored_at: '2026-10-31'
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
artifact_total: 18
asyncapis:
- description: ''
  name: Shortkit Webhooks
  slug: shortkit-webhooks
collections:
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
- group: commercial
  href: https://artifacts.apis.io/shortkit/plans/shortkit-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/shortkit-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/shortkit/capabilities/shortkit-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/shortkit-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/shortkit/overlays/shortkit-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/shortkit-openapi-overlay.yaml
- group: auth
  href: https://artifacts.apis.io/shortkit/security/shortkit-domain-security.yml
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
  href: https://artifacts.apis.io/shortkit/packages/shortkit-packages.yml
  title: ''
  type: Packages
  url: packages/shortkit-packages.yml
- group: build
  href: https://artifacts.apis.io/shortkit/packages/shortkit-packages.yml
  title: ''
  type: SDKs
  url: packages/shortkit-packages.yml
- group: design
  href: https://artifacts.apis.io/shortkit/components/shortkit-components.yml
  title: ''
  type: Components
  url: components/shortkit-components.yml
- group: design
  href: https://artifacts.apis.io/shortkit/conventions/shortkit-conventions.yml
  title: ''
  type: Conventions
  url: conventions/shortkit-conventions.yml
- group: design
  href: https://artifacts.apis.io/shortkit/errors/shortkit-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/shortkit-problem-types.yml
- group: design
  href: https://artifacts.apis.io/shortkit/conformance/shortkit-conformance.yml
  title: ''
  type: Conformance
  url: conformance/shortkit-conformance.yml
- group: design
  href: https://artifacts.apis.io/shortkit/lifecycle/shortkit-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/shortkit-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/shortkit/data-model/shortkit-data-model.yml
  title: ''
  type: DataModel
  url: data-model/shortkit-data-model.yml
- group: design
  href: https://artifacts.apis.io/shortkit/asyncapi/shortkit-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/shortkit-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/shortkit/mcp/shortkit-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/shortkit-mcp.yml
- group: agent
  href: https://artifacts.apis.io/shortkit/llms/shortkit-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/shortkit-llms.txt
- group: start
  href: https://artifacts.apis.io/shortkit/sandbox/shortkit-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/shortkit-sandbox.yml
- group: agent
  href: https://artifacts.apis.io/shortkit/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: ShortKit is a Y Combinator-backed short-form vertical video platform that gives product teams a drop-in, TikTok-quality video experience without the infrastructure complexity. It ships native SDKs for iOS, Android, Flutter, React Native, Expo and Web alongside a REST API for managing content, direct uploads, live streams, in-feed surveys, analytics events and ad configuration. The platform handles adaptive-bitrate HLS transcoding, global CDN delivery across 300+ points of presence, automatic caption generation with language detection, protected/signed playback, and native ad insertion (Google Ad Manager / VAST / IMA). Developer docs are partner-gated but the Mintlify API reference and the iOS SDK are published openly on GitHub.
finops:
- has_sources: true
  method: derived
  name: Shortkit Finops
  primary_unit: ''
  service_category: ''
  slug: shortkit-finops
  template: true
image: https://www.shortkit.dev/icon.svg
layout: provider
modified: '2026-07-21'
name: ShortKit
nav: Providers
network: true
overview: 'ShortKit publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Ad Configuration API, Analytics API, Content API, and 2 more. Tagged areas include Company, Video, Short-Form Video, Video SDK, and Streaming.


  The ShortKit catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  ShortKit''s developer surface includes documentation, API reference, getting-started guide, pricing, engineering blog, signup flow, sandbox, and 21 more developer resources.'
plans:
- name: Shortkit Plans Pricing
  plan_count: 2
  slug: shortkit-plans-pricing
random_paper: 0
score:
  band: developing
  composite: 50.4
  coverage:
    artifact_dirs: 25
    catalog_earned: 45.0
    catalog_earned_first_party: 8.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 4.2
  facets:
    access_clarity: 65.8
    contract_governance: 4.5
    contract_quality: 53.2
    developer_ergonomics: 68.5
    discoverability: 66.1
    operational_transparency: 13.2
  previous_composite: 46.2
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/shortkit/shortkit-2026-08-17T081844.png
security:
- kind: authentication
  name: Shortkit Authentication
  slug: shortkit-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Shortkit Domain Security
  slug: shortkit-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 3
skills:
- name: shortkit-in-feed-survey
  slug: shortkit-in-feed-survey
- name: shortkit-live-stream
  slug: shortkit-live-stream
- name: shortkit-upload-video
  slug: shortkit-upload-video
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
