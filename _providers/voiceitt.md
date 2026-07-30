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
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 41.7
  scored_at: '2026-07-28'
api_count: 3
apis:
- description: Socket.IO WebSockets API for real-time speech recognition. After JWT login via the HTTP API, clients set recognition options (set_options), then send recognize_audio_samples for pre-segmented speech o
  name: Voiceitt WebSockets API
  slug: voiceitt-websockets-api
- description: The Auth API from Voiceitt — 3 operation(s) for auth.
  name: Voiceitt Auth API
  slug: voiceitt-auth-api
- description: The Rec API from Voiceitt — 1 operation(s) for rec.
  name: Voiceitt Rec API
  slug: voiceitt-rec-api
artifact_total: 7
asyncapis:
- description: Socket.IO WebSockets API for real-time speech recognition of non-standard speech. Clients authenticate with a JWT (token + refresh_token in the Socket.IO auth option, obtained from the Voiceitt HTTP A
  name: Voiceitt WebSockets API
  slug: voiceitt-websockets-asyncapi
common:
- group: company
  title: ''
  type: Website
  url: https://voiceitt.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.voiceitt.com/
- group: docs
  title: ''
  type: Documentation
  url: https://voiceitt-si-api.readme.io/
- group: docs
  title: ''
  type: APIReference
  url: https://voiceitt-si-api.readme.io/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://voiceitt-si-api.readme.io/reference/getting-started-with-the-voiceitt-rest-api-copy
- group: operate
  title: ''
  type: Support
  url: https://www.voiceitt.com/faq
- group: commercial
  title: ''
  type: Pricing
  url: https://www.voiceitt.com/faq
- group: start
  title: ''
  type: SignUp
  url: https://web.voiceitt.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.voiceitt.com/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.voiceitt.com/legal/privacy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/voiceitt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/voiceitt-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/voiceitt-authentication.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/voiceitt-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/voiceitt-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/voiceitt-rest-api-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/voiceitt-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.voiceitt.com/
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/voiceitt-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/voiceitt-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/voiceitt-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/voiceitt-data-model.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/voiceitt-websockets-asyncapi.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/voiceitt-domain-security.yml
created: '2026-07-17'
description: Voiceitt builds inclusive voice AI — automatic speech recognition designed for people with non-standard speech, including speech disabilities, aging adults, and accented speakers. Its speaker-independent and personalized speech-to-text power an AAC/dictation app, live captioning integrations for Zoom, Microsoft Teams, and WebEx, a Chrome extension, and Alexa smart-home control. Developers integrate the same engine through the Voiceitt HTTP API (JWT-authenticated audio-file transcription at api2.voiceitt.com) and a Socket.IO WebSockets API for real-time streaming recognition with partial results.
image: https://cdn.prod.website-files.com/64bcd35b2013e5d1f0557e8c/64bce732fa9c2b4c2df390a5_voiceittLogo.svg
layout: provider
mcp_servers:
- description: ''
  name: voiceitt-mcp.yml
  slug: voiceitt-mcpyml
modified: '2026-07-21'
name: Voiceitt
nav: Providers
network: true
overview: 'Voiceitt publishes 3 APIs on the [APIs.io](https://apis.io/) network: WebSockets API, Auth API, and Rec API. Tagged areas include Speech Recognition, Speech-to-Text, Voice, Accessibility, and Assistive Technology.


  The Voiceitt catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Voiceitt''s developer surface includes documentation, API reference, getting-started guide, support, pricing, signup flow, authentication, and 18 more developer resources.'
random_paper: 51
score:
  band: developing
  composite: 46.3
  delta: -1.8
  facets:
    commercial_clarity: 52.6
    contract_quality: 56.2
    developer_ergonomics: 53.8
    discoverability: 92.6
    governance: 20.8
    operational_transparency: 0.0
  previous_composite: 48.1
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 41.7
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Voiceitt Authentication
  slug: voiceitt-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Voiceitt Domain Security
  slug: voiceitt-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: voiceitt
tags:
- Speech Recognition
- Speech-to-Text
- Voice
- Accessibility
- Assistive Technology
- Artificial Intelligence
- Transcription
- Captioning
- Company
website: https://voiceitt.com/
---
