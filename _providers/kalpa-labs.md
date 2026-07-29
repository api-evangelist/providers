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
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 39.4
  scored_at: '2026-07-28'
api_count: 3
apis:
- description: Health checks and capability discovery.
  name: Kalpa Labs Meta API
  slug: kalpa-labs-meta-api
- description: Text-to-speech and conversational generation.
  name: Kalpa Labs Speech API
  slug: kalpa-labs-speech-api
- description: Per-key usage and metering.
  name: Kalpa Labs Usage API
  slug: kalpa-labs-usage-api
artifact_total: 7
common:
- group: company
  title: ''
  type: Website
  url: https://kalpalabs.ai
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.kalpalabs.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.kalpalabs.ai
- group: docs
  title: ''
  type: APIReference
  url: https://docs.kalpalabs.ai/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.kalpalabs.ai/quickstart
- group: start
  title: ''
  type: Sandbox
  url: https://studio.kalpalabs.ai
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/kalpalabs
- group: operate
  title: ''
  type: Support
  url: mailto:hello@kalpalabs.ai
- group: auth
  title: ''
  type: Authentication
  url: authentication/kalpa-labs-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kalpa-labs-domain-security.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/kalpa-labs-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/kalpa-labs-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/kalpa-labs-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/kalpa-labs-lifecycle.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/kalpa-labs-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/kalpa-labs-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/kalpa-labs-openapi-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/kalpa-labs-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/kalpa-labs-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/kalpa-labs-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/kalpa-labs-packages.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/kalpa-labs-converse-stream-asyncapi.json
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: 'Kalpa Labs is a San Francisco audio-research lab (Y Combinator Fall 2025) building generalist speech models that unify text-to-speech, multi-speaker conversation, voice cloning, and speech-in / speech-out reasoning behind one API — steerable with natural instructions and in-context learning the way a large language model is. Their Kalpa Speech API exposes stable public model ids over a clean REST interface: POST /v1/tts turns text into 24 kHz WAV audio, POST /v1/converse completes the open turn of a conversation (authored speech or contextual TTS), and a stateful WebSocket streams multi-speaker sessions. The developer surface ships a committed OpenAPI 3.1 contract, an AsyncAPI 3.0 WebSocket protocol, docs with a markdown twin per page, an llms.txt, and a browser Studio playground. Founded by Prashant Shishodia and Gautam Jha.'
image: https://kalpalabs.ai/og.png
layout: provider
mcp_servers:
- description: ''
  name: kalpa-labs-mcp.yml
  slug: kalpa-labs-mcpyml
modified: '2026-07-19'
name: Kalpa Labs
nav: Providers
network: true
overview: 'Kalpa Labs publishes 3 APIs on the [APIs.io](https://apis.io/) network: Meta API, Speech API, and Usage API. Tagged areas include Company, Speech, Text to Speech, Voice, and Audio.


  Kalpa Labs'' developer surface includes documentation, API reference, getting-started guide, sandbox, support, authentication, and 17 more developer resources.'
random_paper: 36
rate_limits:
- limit_count: 0
  name: Kalpa Labs Rate Limits
  slug: kalpa-labs-rate-limits
score:
  band: thin
  composite: 36.5
  delta: -3.8
  facets:
    commercial_clarity: 0.0
    contract_quality: 56.5
    developer_ergonomics: 66.8
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 5.3
  previous_composite: 40.3
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
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
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kalpa-labs/refs/heads/main/screenshots/kalpa-labs-2026-07-25T223437.png
security:
- kind: authentication
  name: Kalpa Labs Authentication
  slug: kalpa-labs-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Kalpa Labs Domain Security
  slug: kalpa-labs-domain-security
  summary_line: TLSv1.3 · DMARC
slug: kalpa-labs
tags:
- Company
- Speech
- Text to Speech
- Voice
- Audio
- Conversational AI
- Machine Learning
- Artificial Intelligence
website: https://kalpalabs.ai
---
