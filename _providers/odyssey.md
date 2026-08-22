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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 12.0
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: Real-time world-model API. Embeds continuous, interactive video simulations into applications via interactive streams, viewable/broadcast streams, and asynchronous simulations, over WebRTC + WebSocket
  name: Odyssey-2 Pro API
  slug: odyssey-2-pro-api
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://odyssey.world
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.odyssey.ml/dashboard
- group: docs
  title: ''
  type: Documentation
  url: https://documentation.api.odyssey.ml/
- group: docs
  title: ''
  type: APIReference
  url: https://documentation.api.odyssey.ml/sdk/javascript/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://documentation.api.odyssey.ml/api-quick-start
- group: start
  title: ''
  type: SignUp
  url: https://developer.odyssey.ml/dashboard
- group: operate
  title: ''
  type: Support
  url: https://discord.com/invite/CmV5DgJMAW
- group: company
  title: ''
  type: Blog
  url: https://odyssey.ml/writing
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/odysseyml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://odyssey.ml/legal
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://odyssey.ml/legal
- group: auth
  title: ''
  type: Authentication
  url: authentication/odyssey-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/odyssey-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/odyssey-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/odyssey-llms.txt
- group: design
  title: ''
  type: Conventions
  url: conventions/odyssey-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/odyssey-error-codes.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/odyssey-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/odyssey-lifecycle.yml
- group: design
  title: ''
  type: Components
  url: components/odyssey-components.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/odyssey-domain-security.yml
created: '2026-07-17'
description: 'Odyssey is an AI research lab pioneering general-purpose world models — causal, multimodal systems that learn to understand and simulate the world beyond language. Its flagship, Odyssey-2 Pro, is a frontier world model that outputs continuous, interactive, multi-minute video simulations in real time from text or image prompts. Odyssey exposes this as a developer API: three surfaces (interactive streams, viewable/broadcast streams, and asynchronous simulations) delivered over WebRTC media plus a WebSocket signaling channel, driven by official JavaScript/ TypeScript and Python SDKs. Auth is an `ody_` API key with a client-credentials pattern that mints short-lived session JWTs so browsers can connect without exposing the key. Odyssey is backed by a16z, EQT Ventures, General Catalyst, GV, and Union Square Ventures and is based in Menlo Park, California.'
image: https://odyssey.ml/logo-black.png
layout: provider
modified: '2026-07-20'
name: Odyssey
nav: Providers
network: true
overview: 'Odyssey publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, World Models, Generative AI, and Video Generation.


  Odyssey''s developer surface includes documentation, API reference, getting-started guide, signup flow, support, engineering blog, authentication, and 14 more developer resources.'
random_paper: 7
score:
  band: emerging
  composite: 25.2
  delta: -3.7
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 54.8
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 18.4
  previous_composite: 28.9
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/odyssey/refs/heads/main/screenshots/odyssey-2026-08-07T185956.png
security:
- kind: authentication
  name: Odyssey Authentication
  slug: odyssey-authentication
  summary_line: apiKey/bearer-jwt · 3 schemes
- kind: domain-security
  name: Odyssey Domain Security
  slug: odyssey-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: odyssey
tags:
- Company
- Artificial Intelligence
- World Models
- Generative AI
- Video Generation
- Machine Learning
- Real-Time Streaming
- SDK
- WebRTC
website: https://odyssey.world
---
