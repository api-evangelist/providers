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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: derived
    idempotency: na
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 31.5
  scored_at: '2026-08-26'
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
artifact_total: 12
asyncapis:
- description: NOT PUBLISHED BY KRISP. Krisp publishes no AsyncAPI document. This is a faithful transcription by the API Evangelist enrichment pipeline of the WebSocket protocol Krisp documents in prose at https://s
  name: Krisp Voice Translation WebSocket API
  slug: krisp-voice-translation-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Krisp Developers SDK Distribution API
  slug: open-krisp-sdk-distribution-api
- collection_type: open
  name: Krisp Developers SDK Distribution Voice Translation API
  slug: open-krisp-voice-translation-api
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/krisp-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/krisp-developers-overlay.yaml
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
mcp_servers:
- description: ''
  name: Krisp MCP Server
  slug: krisp-mcp-server
modified: '2026-07-19'
name: Krisp
nav: Providers
network: true
overview: 'Krisp publishes 2 APIs on the [APIs.io](https://apis.io/) network: SDK Distribution API and Voice Translation API. Tagged areas include Company, Artificial Intelligence, Voice AI, Speech, and Audio.


  The Krisp catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Krisp''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 29 more developer resources.'
random_paper: 7
score:
  band: developing
  composite: 41.7
  delta: 0.0
  facets:
    access_clarity: 53.9
    commercial_clarity: 53.9
    contract_governance: 30.3
    contract_quality: 23.4
    developer_ergonomics: 55.4
    discoverability: 75.9
    governance: 30.3
    operational_transparency: 21.1
  previous_composite: 41.7
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 2
      marker_coverage: 100.0
      total: 2
    mcp: derived
    skills: derived
  schema_version: 0.15.0
  scored_at: '2026-08-26'
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
- Artificial Intelligence
- Voice AI
- Speech
- Audio
- Noise Cancellation
- Speech Translation
- Real-Time Communications
- WebRTC
- Conversational AI
- SDK
- Machine-Learning
website: https://krisp.ai/
---
