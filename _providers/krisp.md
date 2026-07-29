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
    asyncapi_events: true
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 50.2
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Krisp Agentic Access
  operation_count: 3
  slug: krisp-agentic-access
  summary_line: 3 operations
api_count: 2
apis:
- description: Programmatic retrieval of licensed SDK packages and model files.
  name: Krisp SDK Distribution API
  slug: krisp-sdk-distribution-api
- description: Session minting and language discovery for the real-time voice translation service.
  name: Krisp Voice Translation API
  slug: krisp-voice-translation-api
artifact_total: 8
asyncapis:
- description: NOT PUBLISHED BY KRISP. Krisp publishes no AsyncAPI document. This is a faithful transcription by the API Evangelist enrichment pipeline of the WebSocket protocol Krisp documents in prose at https://s
  name: Krisp Voice Translation WebSocket API
  slug: krisp-voice-translation-asyncapi
common:
- group: company
  title: ''
  type: Website
  url: https://krisp.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://krisp.ai/developers/
- group: docs
  title: ''
  type: Documentation
  url: https://sdk-docs.krisp.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://sdk-docs.krisp.ai/docs/voice-translation-api.md
- group: start
  title: ''
  type: GettingStarted
  url: https://sdk-docs.krisp.ai/docs/getting-started.md
- group: operate
  title: ''
  type: Support
  url: https://help.krisp.ai
- group: company
  title: ''
  type: Blog
  url: https://krisp.ai/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/krispai
- group: commercial
  title: ''
  type: Pricing
  url: https://krisp.ai/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://account.krisp.ai/trial/signup
- group: start
  title: ''
  type: Login
  url: https://developers.krisp.ai/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://krisp.ai/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://krisp.ai/privacy-policy/
- group: auth
  title: ''
  type: Security
  url: https://krisp.ai/security/
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.krisp.ai/
- group: auth
  title: ''
  type: Compliance
  url: https://krisp.ai/security-for-ai-meeting-assistant/
- group: operate
  title: ''
  type: ChangeLog
  url: https://sdk-docs.krisp.ai/changelog
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/krisp-changelog.yml
- group: start
  title: ''
  type: Sandbox
  url: https://lab.krisp.ai/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/krisp-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/krisp-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/krisp-security.txt
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/krisp-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/krisp-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/krisp-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/krisp-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/krisp-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/krisp-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/krisp-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/krisp-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/krisp-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/krisp-data-model.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/krisp-agentic-access.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: 'Krisp is a Voice AI platform whose real-time speech-enhancement models run on over 200 million devices, licensed by Discord, Twilio, and VMware among others. Beyond its consumer AI Note Taker, Krisp ships a developer surface: the AI Voice SDK family (VIVA for voice AI agents — voice isolation, turn prediction, interruption prediction, VAD; and RTC for human-to-human calls — accent conversion, bidirectional noise cancellation, background voice cancellation) across Windows, macOS, Linux, Web (JS/WASM), iOS, and Android with C++, Python, Node.js, Go, Rust, and JavaScript bindings, plus framework integrations for LiveKit, WebRTC, and Pipecat. Krisp also runs a self-serve Voice Translation API — a streaming WebSocket speech-to-speech translation service covering 61 languages behind a REST session-token mint — and a programmatic SDK and model download REST API for CI/CD pipelines.'
image: https://krisp.ai/wp-content/uploads/2025/08/thumb1.jpg
layout: provider
modified: '2026-07-19'
name: Krisp
nav: Providers
network: true
overview: 'Krisp publishes 2 APIs on the [APIs.io](https://apis.io/) network: SDK Distribution API and Voice Translation API. Tagged areas include Company, Ai, Voice AI, Speech, and Audio.


  The Krisp catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Krisp''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 27 more developer resources.'
random_paper: 14
score:
  band: strong
  composite: 59.6
  delta: 1.2
  facets:
    commercial_clarity: 60.5
    contract_quality: 75.4
    developer_ergonomics: 66.8
    discoverability: 87.0
    governance: 20.8
    operational_transparency: 31.6
  previous_composite: 58.4
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/krisp/refs/heads/main/screenshots/krisp-2026-07-25T224259.png
security:
- kind: authentication
  name: Krisp Authentication
  slug: krisp-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Krisp Domain Security
  slug: krisp-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Krisp Vulnerability Disclosure
  slug: krisp-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Krisp Trust Center
  slug: krisp-trust-center
  summary_line: SOC 2, PCI DSS, HIPAA
slug: krisp
tags:
- Company
- Ai
- Voice AI
- Speech
- Audio
- Noise Cancellation
- Speech Translation
- Real Time Communications
- WebRTC
- Conversational AI
- SDK
- Machine Learning
website: https://krisp.ai/
---
