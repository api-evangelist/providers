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
  band: agent-native
  dimensions:
    agent_skills: true
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 65.4
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 11
  human_in_the_loop: 5
  name: Captions Agentic Access
  operation_count: 23
  slug: captions-agentic-access
  summary_line: 23 operations · 11 acting · 5 human-in-the-loop
api_count: 7
apis:
- description: The Audio API from Captions — 1 operation(s) for audio.
  name: Captions Audio API
  slug: captions-audio-api
- description: The health API from Captions — 1 operation(s) for health.
  name: Captions health API
  slug: captions-health-api
- description: The internal API from Captions — 8 operation(s) for internal.
  name: Captions internal API
  slug: captions-internal-api
- description: The Meta Text Overlays API from Captions — 2 operation(s) for meta text overlays.
  name: Captions Meta Text Overlays API
  slug: captions-meta-text-overlays-api
- description: The root API from Captions — 1 operation(s) for root.
  name: Captions root API
  slug: captions-root-api
- description: The Video Captions API from Captions — 3 operation(s) for video captions.
  name: Captions Video Captions API
  slug: captions-video-captions-api
- description: The Videos API from Captions — 3 operation(s) for videos.
  name: Captions Videos API
  slug: captions-videos-api
artifact_total: 12
common:
- group: start
  title: ''
  type: Portal
  url: https://platform.mirage.app/
- group: docs
  title: ''
  type: Documentation
  url: https://captions.ai/help/docs/api/overview
- group: docs
  title: ''
  type: APIReference
  url: https://captions.ai/help/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://captions.ai/help
- group: operate
  title: ''
  type: Support
  url: https://captions.ai/help
- group: company
  title: ''
  type: Blog
  url: https://captions.ai/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://captions.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://captions.ai/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://mirage.app/legal/captions-terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://mirage.app/legal/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/captions-ai
- group: company
  title: ''
  type: Website
  url: https://captions.ai
- group: operate
  title: ''
  type: StatusPage
  url: https://mirage.statuspage.io
- group: auth
  title: ''
  type: Compliance
  url: https://captions.ai/solutions/enterprise
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/captions-mirage-openapi-original.json
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/captions-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/captions-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/captions-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/captions-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/captions-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/captions-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/captions-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/captions-domain-security.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/captions-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/captions-agentic-access.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/captions-plans.yml
created: '2026-07-17'
description: 'Captions is an AI video editor and generator built by Mirage, an AI research company headquartered in New York City. The consumer and enterprise apps automate the most time-consuming parts of video production — cutting scenes, adding B-roll, inserting music and sound effects, generating and styling captions, dubbing into 30+ languages, correcting eye contact, and generating entirely new videos from a text prompt or a selfie via AI Avatars, AI Actors, and AI Twins. The Mirage Video API (api.mirage.app) exposes this pipeline to developers: asynchronous AI video generation, adding stylized captions to videos, caption-template discovery, text-to-speech audio, and meta text overlays. Authentication is a simple x-api-key header, keys are minted in the Mirage platform dashboard, and long-running jobs are polled for status.'
image: https://captions.ai/logo256.png
layout: provider
mcp_servers:
- description: ''
  name: captions-mcp.yml
  slug: captions-mcpyml
modified: '2026-07-18'
name: Captions
nav: Providers
network: true
overview: 'Captions publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Audio API, health API, internal API, and 4 more. Tagged areas include Company, Video, Artificial Intelligence, Video Editing, and Video Generation.


  Captions'' developer surface includes developer portal, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 20 more developer resources.'
plans:
- name: Captions Plans
  plan_count: 5
  slug: captions-plans
random_paper: 49
score:
  band: developing
  composite: 54.4
  delta: 0.0
  facets:
    commercial_clarity: 84.2
    contract_quality: 45.5
    developer_ergonomics: 67.4
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 54.4
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Captions Authentication
  slug: captions-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Captions Domain Security
  slug: captions-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: captions
tags:
- Company
- Video
- Artificial Intelligence
- Video Editing
- Video Generation
- Captions
- Subtitles
- Text to Speech
- AI Avatars
- Content Creation
- Media
website: https://captions.ai
---
