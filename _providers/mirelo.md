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
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 6.0
  scored_at: '2026-08-26'
api_count: 1
apis:
- description: Self-serve REST API to generate and edit sound effects from video or text. Bearer-token (API key) auth; JSON request/response returning generated audio asset URLs; synchronous and asynchronous (job-po
  name: Mirelo SFX API
  slug: mirelo-sfx-api
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://mirelo.ai
- group: docs
  title: ''
  type: Documentation
  url: https://mirelo.ai/api-docs
- group: docs
  title: ''
  type: APIReference
  url: https://mirelo.ai/api-docs
- group: company
  title: ''
  type: Blog
  url: https://mirelo.ai/blog
- group: company
  title: ''
  type: BlogRSS
  url: https://mirelo.ai/feed.xml
- group: commercial
  title: ''
  type: Pricing
  url: https://mirelo.ai/pricing
- group: operate
  title: ''
  type: Support
  url: https://mirelo.ai/support
- group: start
  title: ''
  type: SignUp
  url: https://mirelo.ai/sfx
- group: commercial
  title: ''
  type: TermsOfService
  url: https://mirelo.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://mirelo.ai/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/mirelo-ai
- group: operate
  title: ''
  type: StatusPage
  url: https://status.mirelo.ai
- group: auth
  title: ''
  type: Authentication
  url: authentication/mirelo-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/mirelo-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/mirelo-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/mirelo-changelog.yml
- group: build
  title: ''
  type: Packages
  url: packages/mirelo-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/mirelo-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/mirelo-mcp.yml
- group: design
  title: ''
  type: Components
  url: components/mirelo-components.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mirelo-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/mirelo-llms.txt
created: '2026-07-17'
description: Mirelo is a Berlin-based AI research lab building state-of-the-art audio foundation models for visual media. Its flagship Mirelo SFX model generates production-ready, perfectly synced sound effects directly from video (or from text prompts) with no background-music noise, plus iterative editing, audio inpainting, sound extension, and a multi-instrument Audio-to-MIDI model. Mirelo ships a self-serve REST API (https://api.mirelo.ai/v2/), the Mirelo Studio web app, official Node.js and Python SDKs, and editor plugins for Adobe Premiere Pro, DaVinci Resolve, Reaper, and Roblox Studio. The models are also distributed on fal.ai, Replicate, and Runware. Founded by musicians-turned-AI researchers from Amazon, Google Brain, Max Planck and ETH Zurich, Mirelo raised a $41M seed round co-led by Index Ventures and Andreessen Horowitz in December 2025.
image: https://mirelo.ai/opengraph-image.png
layout: provider
mcp_servers:
- description: Community-published Model Context Protocol server wrapping the Mirelo v2 HTTP API. Not first-party, but functional against the same API key and endpoints. No official hosted/remote MCP server is publi
  name: Mirelo MCP Server
  slug: mirelo-mcp-server
modified: '2026-07-20'
name: Mirelo
nav: Providers
network: true
overview: 'Mirelo publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Ai Ml, Audio, Sound Effects, and Generative AI.


  Mirelo''s developer surface includes documentation, API reference, engineering blog, pricing, support, signup flow, authentication, and 15 more developer resources.'
random_paper: 18
score:
  band: thin
  composite: 29.6
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 42.9
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 29.6
  provenance:
    mcp: first-party
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mirelo/refs/heads/main/screenshots/mirelo-2026-08-07T183717.png
security:
- kind: authentication
  name: Mirelo Authentication
  slug: mirelo-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Mirelo Domain Security
  slug: mirelo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: mirelo
tags:
- Company
- Ai Ml
- Audio
- Sound Effects
- Generative AI
- Video
- Text to Audio
- Audio to MIDI
- Machine-Learning
website: https://mirelo.ai
---
