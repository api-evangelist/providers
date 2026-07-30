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
    agent_skills: derived
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: derived
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.7
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 3
  human_in_the_loop: 1
  name: Keyframe Labs Agentic Access
  operation_count: 8
  slug: keyframe-labs-agentic-access
  summary_line: 8 operations · 3 acting · 1 human-in-the-loop
api_count: 4
apis:
- description: The LLM models API from Keyframe Labs — 2 operation(s) for llm models.
  name: Keyframe Labs LLM models API
  slug: keyframe-labs-llm-models-api
- description: The Meet bots API from Keyframe Labs — 3 operation(s) for meet bots.
  name: Keyframe Labs Meet bots API
  slug: keyframe-labs-meet-bots-api
- description: The Sessions API from Keyframe Labs — 1 operation(s) for sessions.
  name: Keyframe Labs Sessions API
  slug: keyframe-labs-sessions-api
- description: The Voices API from Keyframe Labs — 2 operation(s) for voices.
  name: Keyframe Labs Voices API
  slug: keyframe-labs-voices-api
artifact_total: 8
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/keyframe-labs-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/keyframe-labs-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/keyframe-labs-authentication.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/keyframe-labs-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/keyframe-labs-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/keyframe-labs-packages.yml
- group: design
  title: ''
  type: Components
  url: components/keyframe-labs-components.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/keyframe-labs-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/keyframe-labs-sessions-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/keyframe-labs-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/keyframe-labs-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/keyframe-labs-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/keyframe-labs-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/keyframe-labs-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: company
  title: ''
  type: Website
  url: https://www.keyframelabs.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.keyframelabs.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.keyframelabs.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.keyframelabs.com/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.keyframelabs.com/guides/getting-started/quickstart-hosted
- group: start
  title: ''
  type: SignUp
  url: https://platform.keyframelabs.com
- group: commercial
  title: ''
  type: Pricing
  url: https://www.keyframelabs.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.keyframelabs.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/keyframelabs
- group: operate
  title: ''
  type: Support
  url: https://discord.gg/Wfce5xHNd5
- group: start
  title: ''
  type: Demo
  url: https://demo.keyframelabs.com
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/keyframe-labs-inc
- group: company
  title: ''
  type: Twitter
  url: https://x.com/KeyframeLabs
created: '2026-07-17'
description: Keyframe Labs builds real-time foundation models that turn AI voice and text agents into lifelike, emotionally expressive video calls. Its Persona-1.5-Live product lets developers add photoreal AI avatars ("personas") to their agents and applications with a few lines of embed code, at roughly 500ms latency and from $0.06 per minute. The platform exposes a REST Sessions API (create a live session, manage meeting bots for Zoom/Meet/Teams, and list voices and LLM models), JavaScript/TypeScript SDKs, and embeddable UI elements, with hosted and self-managed integration paths that plug into agent frameworks such as LiveKit Agents, ElevenLabs Agents, and OpenAI Realtime. Founded in 2025 and backed by Y Combinator (Spring 2026), Keyframe Labs is based in San Francisco.
image: https://platform.keyframelabs.com/og.png
layout: provider
mcp_servers:
- description: ''
  name: keyframe-labs-mcp.yml
  slug: keyframe-labs-mcpyml
modified: '2026-07-19'
name: Keyframe Labs
nav: Providers
network: true
overview: 'Keyframe Labs publishes 4 APIs on the [APIs.io](https://apis.io/) network, including LLM models API, Meet bots API, Sessions API, and 1 more. Tagged areas include Company, AI, Avatars, Video, and Conversational AI.


  Keyframe Labs'' developer surface includes authentication, documentation, API reference, getting-started guide, signup flow, pricing, engineering blog, and 21 more developer resources.'
random_paper: 3
score:
  band: thin
  composite: 38.5
  delta: -5.2
  facets:
    commercial_clarity: 23.7
    contract_quality: 54.9
    developer_ergonomics: 62.5
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 5.3
  previous_composite: 43.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 23.6
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/keyframe-labs/refs/heads/main/screenshots/keyframe-labs-2026-07-25T223654.png
security:
- kind: authentication
  name: Keyframe Labs Authentication
  slug: keyframe-labs-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Keyframe Labs Domain Security
  slug: keyframe-labs-domain-security
  summary_line: TLSv1.3 · HSTS
slug: keyframe-labs
tags:
- Company
- AI
- Avatars
- Video
- Conversational AI
- Agents
- Real-Time
- Personas
- Voice
- Y Combinator
website: https://www.keyframelabs.com
---
