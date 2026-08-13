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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: derived
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 37.4
  scored_at: '2026-08-12'
api_count: 1
apis:
- description: 'Real-time generative video platform. A REST token endpoint mints session-scoped JWTs; a WebRTC data channel carries the command/event interface that controls model generation and streams video frames '
  name: Reactor Realtime Video API
  slug: reactor-realtime-video-api
artifact_total: 5
asyncapis:
- description: 'Real-time video generation control channel for Reactor''s Helios model, exchanged over a WebRTC data channel after a session reaches "ready". Clients send commands; the model emits state and lifecycle '
  name: Reactor Helios Realtime API
  slug: reactor-helios-asyncapi
common:
- group: company
  title: ''
  type: Website
  url: https://reactor.inc
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.reactor.inc
- group: docs
  title: ''
  type: Documentation
  url: https://docs.reactor.inc
- group: docs
  title: ''
  type: APIReference
  url: https://docs.reactor.inc/model-api-reference/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.reactor.inc/quickstart
- group: operate
  title: ''
  type: Support
  url: https://discord.gg/tMcJM8N5N3
- group: company
  title: ''
  type: Blog
  url: https://www.reactor.inc/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/reactor-team
- group: start
  title: ''
  type: SignUp
  url: https://www.reactor.inc/dashboard
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.reactor.inc/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.reactor.inc/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.reactor.inc
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.reactor.inc/changelog
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/reactor-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/reactor-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/reactor-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/reactor-cli.yml
- group: design
  title: ''
  type: Components
  url: components/reactor-components.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/reactor-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/reactor-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/reactor-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/reactor-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/reactor-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/reactor-conformance.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/reactor-sandbox.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/reactor-helios-asyncapi.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/reactor-domain-security.yml
created: '2026-07-17'
description: Reactor is a real-time video AI platform that streams generative video from GPU-hosted models to web and mobile applications over WebRTC, with sub-second round-trip latency and no infrastructure to manage. Developers connect through a JavaScript/React SDK or an async Python SDK, mint short-lived session tokens from a long-lived account API key, and control generation with a command/event channel (set_prompt, start, pause, reset). Its model catalog includes Helios (interactive real-time generation), SANA-Streaming (video-to-video editing), LingBot and LingBot World 2 (navigable worlds), X2, LongLive-2.0 and HappyOyster. Reactor is backed by Amplify Partners and Lightspeed Venture Partners and is currently in public beta.
image: https://www.reactor.inc/icon.png
layout: provider
mcp_servers:
- description: ''
  name: reactor-mcp.yml
  slug: reactor-mcpyml
modified: '2026-07-20'
name: Reactor
nav: Providers
network: true
overview: 'Reactor publishes 1 API on the [APIs.io](https://apis.io/) network: Realtime Video API. Tagged areas include Company, Ai Ml, Video, Generative AI, and Real-Time.


  The Reactor catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Reactor''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, changelog, and 21 more developer resources.'
random_paper: 32
score:
  band: developing
  composite: 48.0
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 49.4
    developer_ergonomics: 80.4
    discoverability: 75.9
    governance: 3.1
    operational_transparency: 36.8
  previous_composite: 48.0
  provenance:
    conformance: derived
    mcp: derived
    skills: first-party
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
security:
- kind: authentication
  name: Reactor Authentication
  slug: reactor-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Reactor Domain Security
  slug: reactor-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: reactor
tags:
- Company
- Ai Ml
- Video
- Generative AI
- Real-Time
- WebRTC
- Streaming
- SDK
- Media
website: https://reactor.inc
---
