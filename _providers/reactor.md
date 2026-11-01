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
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 23.0
  scored_at: '2026-10-31'
api_count: 1
apis:
- baseURL: https://api.reactor.inc
  baseurl_source: declared
  description: 'Real-time generative video platform. A REST token endpoint mints session-scoped JWTs; a WebRTC data channel carries the command/event interface that controls model generation and streams video frames '
  name: Reactor Realtime Video API
  slug: reactor-realtime-video-api
artifact_total: 9
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
  href: https://artifacts.apis.io/reactor/llms/reactor-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/reactor-llms.txt
- group: build
  href: https://artifacts.apis.io/reactor/packages/reactor-packages.yml
  title: ''
  type: Packages
  url: packages/reactor-packages.yml
- group: build
  href: https://artifacts.apis.io/reactor/packages/reactor-packages.yml
  title: ''
  type: SDKs
  url: packages/reactor-packages.yml
- group: build
  href: https://artifacts.apis.io/reactor/cli/reactor-cli.yml
  title: ''
  type: CLI
  url: cli/reactor-cli.yml
- group: design
  href: https://artifacts.apis.io/reactor/components/reactor-components.yml
  title: ''
  type: Components
  url: components/reactor-components.yml
- group: agent
  href: https://artifacts.apis.io/reactor/mcp/reactor-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/reactor-mcp.yml
- group: agent
  href: https://artifacts.apis.io/reactor/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://artifacts.apis.io/reactor/authentication/reactor-authentication.yml
  title: ''
  type: Authentication
  url: authentication/reactor-authentication.yml
- group: design
  href: https://artifacts.apis.io/reactor/conventions/reactor-conventions.yml
  title: ''
  type: Conventions
  url: conventions/reactor-conventions.yml
- group: design
  href: https://artifacts.apis.io/reactor/errors/reactor-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/reactor-problem-types.yml
- group: design
  href: https://artifacts.apis.io/reactor/lifecycle/reactor-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/reactor-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/reactor/conformance/reactor-conformance.yml
  title: ''
  type: Conformance
  url: conformance/reactor-conformance.yml
- group: start
  href: https://artifacts.apis.io/reactor/sandbox/reactor-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/reactor-sandbox.yml
- group: docs
  href: https://artifacts.apis.io/reactor/asyncapi/reactor-helios-asyncapi.yml
  title: ''
  type: AsyncAPI
  url: asyncapi/reactor-helios-asyncapi.yml
- group: auth
  href: https://artifacts.apis.io/reactor/security/reactor-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/reactor-domain-security.yml
created: '2026-07-17'
description: Reactor is a real-time video AI platform that streams generative video from GPU-hosted models to web and mobile applications over WebRTC, with sub-second round-trip latency and no infrastructure to manage. Developers connect through a JavaScript/React SDK or an async Python SDK, mint short-lived session tokens from a long-lived account API key, and control generation with a command/event channel (set_prompt, start, pause, reset). Its model catalog includes Helios (interactive real-time generation), SANA-Streaming (video-to-video editing), LingBot and LingBot World 2 (navigable worlds), X2, LongLive-2.0 and HappyOyster. Reactor is backed by Amplify Partners and Lightspeed Venture Partners and is currently in public beta.
image: https://www.reactor.inc/icon.png
layout: provider
modified: '2026-07-20'
name: Reactor
nav: Providers
network: true
overview: 'Reactor is listed with 1 API on the [APIs.io](https://apis.io/) network: Realtime Video API. Tagged areas include Company, Artificial Intelligence, Video, Generative AI, and Real-Time.


  The Reactor catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Reactor''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, changelog, and 21 more developer resources.'
random_paper: 8
score:
  band: developing
  composite: 46.5
  coverage:
    artifact_dirs: 20
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    contract_governance: 4.5
    contract_quality: 39.6
    developer_ergonomics: 85.7
    discoverability: 66.1
    operational_transparency: 36.8
  previous_composite: 46.5
  provenance:
    conformance: derived
    mcp: derived
    skills: first-party
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 22.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/reactor/reactor-2026-08-17T081450.png
security:
- kind: authentication
  name: Reactor Authentication
  slug: reactor-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Reactor Domain Security
  slug: reactor-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 5
skills:
- name: helios-prompts
  slug: reactor-helios-prompts
- name: lingbot-world-2-prompts
  slug: reactor-lingbot-world-2-prompts
- name: lingbot-world
  slug: reactor-lingbot-world
- name: reactor-sdk
  slug: reactor-reactor-sdk
- name: sana-streaming-prompts
  slug: reactor-sana-streaming-prompts
slug: reactor
tags:
- Company
- Artificial Intelligence
- Video
- Generative AI
- Real-Time
- WebRTC
- Streaming
- SDK
- Media
website: https://reactor.inc
---
