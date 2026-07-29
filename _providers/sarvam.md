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
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 52.0
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 23
  human_in_the_loop: 0
  name: Sarvam Agentic Access
  operation_count: 28
  slug: sarvam-agentic-access
  summary_line: 28 operations · 23 acting
api_count: 8
apis:
- description: The chat API from Sarvam — 1 operation(s) for chat.
  name: Sarvam chat API
  slug: sarvam-chat-api
- description: The documentIntelligence API from Sarvam — 5 operation(s) for documentintelligence.
  name: Sarvam documentIntelligence API
  slug: sarvam-documentintelligence-api
- description: The pronunciationDictionary API from Sarvam — 2 operation(s) for pronunciationdictionary.
  name: Sarvam pronunciationDictionary API
  slug: sarvam-pronunciationdictionary-api
- description: The speechToText API from Sarvam — 2 operation(s) for speechtotext.
  name: Sarvam speechToText API
  slug: sarvam-speechtotext-api
- description: The speechToTextJob API from Sarvam — 5 operation(s) for speechtotextjob.
  name: Sarvam speechToTextJob API
  slug: sarvam-speechtotextjob-api
- description: The speechToTextTranslateJob API from Sarvam — 5 operation(s) for speechtotexttranslatejob.
  name: Sarvam speechToTextTranslateJob API
  slug: sarvam-speechtotexttranslatejob-api
- description: The text API from Sarvam — 3 operation(s) for text.
  name: Sarvam text API
  slug: sarvam-text-api
- description: The textToSpeech API from Sarvam — 2 operation(s) for texttospeech.
  name: Sarvam textToSpeech API
  slug: sarvam-texttospeech-api
artifact_total: 13
asyncapis:
- description: ''
  name: Endpoints
  slug: sarvam-streaming-asyncapi
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.sarvam.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.sarvam.ai
- group: docs
  title: ''
  type: APIReference
  url: https://docs.sarvam.ai/api-reference/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.sarvam.ai/api/getting-started/quickstart
- group: commercial
  title: ''
  type: Pricing
  url: https://docs.sarvam.ai/api/getting-started/pricing
- group: start
  title: ''
  type: SignUp
  url: https://dashboard.sarvam.ai
- group: operate
  title: ''
  type: Support
  url: https://docs.sarvam.ai/api/getting-started/help
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/sarvamai
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.sarvam.ai/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.sarvam.ai/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.sarvam.ai
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.sarvam.ai/api/getting-started/changelog
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/sarvam-changelog.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/sarvam-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/sarvam-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/sarvam-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/sarvam-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/sarvam-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/sarvam-openapi-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/sarvam-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/sarvam-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/sarvam-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/sarvam-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/sarvam-data-model.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sarvam-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/sarvam-agentic-access.yml
created: '2026-07-17'
description: Sarvam AI is an Indian-language AI platform offering a unified REST and WebSocket API across speech-to-text (Saaras / Saarika), text-to-speech (Bulbul, 30+ voices), translation and transliteration (Mayura / Sarvam-Translate) for 22 Indian languages, multilingual chat completion (Sarvam-30B and Sarvam-105B, OpenAI-compatible), and document digitization (Sarvam Vision). The API is authenticated with an api-subscription-key header, billed in Indian Rupees with ₹100 free credits on signup, and shipped with official Python and JavaScript SDKs, published OpenAPI and AsyncAPI specs, a documentation MCP server, a status page, and a dated changelog. Sarvam is backed by Bessemer Venture Partners.
image: https://avatars.githubusercontent.com/u/139587482?v=4
layout: provider
mcp_servers:
- description: ''
  name: sarvam-mcp.yml
  slug: sarvam-mcpyml
modified: '2026-07-21'
name: Sarvam
nav: Providers
network: true
overview: 'Sarvam publishes 8 APIs on the [APIs.io](https://apis.io/) network, including chat API, documentIntelligence API, pronunciationDictionary API, and 5 more. Tagged areas include Company, Ai Ml, Artificial Intelligence, Machine Learning, and Speech To Text.


  The Sarvam catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Sarvam''s developer surface includes documentation, API reference, getting-started guide, pricing, signup flow, support, changelog, and 20 more developer resources.'
random_paper: 18
score:
  band: developing
  composite: 52.1
  delta: -3.1
  facets:
    commercial_clarity: 44.7
    contract_quality: 65.5
    developer_ergonomics: 66.8
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 44.7
  previous_composite: 55.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 34.7
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Sarvam Authentication
  slug: sarvam-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Sarvam Domain Security
  slug: sarvam-domain-security
  summary_line: TLSv1.3 · DMARC
slug: sarvam
tags:
- Company
- Ai Ml
- Artificial Intelligence
- Machine Learning
- Speech To Text
- Text To Speech
- Translation
- Large Language Models
- Document Intelligence
- Indian Languages
- Voice
website: https://docs.sarvam.ai
---
