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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 11.7
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: 'The Wit.ai HTTP API extracts structured meaning (intents, entities, traits) from text and audio, transcribes speech (speech / dictation), synthesizes speech (text-to-speech), and manages an app''s NLP '
  name: Wit.ai HTTP API
  slug: witai-http-api
artifact_total: 4
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://wit.ai
- group: docs
  title: ''
  type: Documentation
  url: https://wit.ai/docs
- group: docs
  title: ''
  type: APIReference
  url: https://wit.ai/docs/http/latest
- group: start
  title: ''
  type: GettingStarted
  url: https://wit.ai/docs/quickstart
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/wit-ai
- group: start
  title: ''
  type: SignUp
  url: https://wit.ai/apps
- group: commercial
  title: ''
  type: TermsOfService
  url: https://opensource.facebook.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://opensource.facebook.com/legal/privacy
- group: build
  title: ''
  type: Packages
  url: packages/witai-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/witai-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/witai-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/witai-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/witai-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/witai-domain-security.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/witai-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/witai-llms.txt
created: '2026-07-17'
description: Wit.ai is a natural language processing (NLP) platform from Meta that lets developers build applications and devices you can talk or text to. It turns spoken or written user input into structured, machine-readable data — extracting intents, entities, and traits — and provides speech recognition (speech-to-text), dictation, and speech synthesis (text-to-speech). Developers train an app with example utterances, then call the Wit HTTP API with a Bearer server access token to parse messages, transcribe audio, and manage an app's entities, intents, traits, and utterances. Wit.ai is free to use and ships official client SDKs for Node.js, Python, Ruby, Go, iOS, Unity, and Unreal. It was founded in 2013, backed by a16z, and acquired by Facebook (now Meta) in 2015.
image: https://avatars.githubusercontent.com/u/4723433?v=4
layout: provider
mcp_servers:
- description: ''
  name: witai-mcp.yml
  slug: witai-mcpyml
modified: '2026-07-21'
name: Wit.AI
nav: Providers
network: true
overview: 'Wit.AI publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Natural Language Processing, NLP, Speech Recognition, and Speech to Text.


  Wit.AI''s developer surface includes documentation, API reference, getting-started guide, signup flow, authentication, and 11 more developer resources.'
random_paper: 50
score:
  band: emerging
  composite: 26.3
  delta: -2.7
  facets:
    commercial_clarity: 34.2
    contract_quality: 0.0
    developer_ergonomics: 54.3
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 29.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 27.8
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Witai Authentication
  slug: witai-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Witai Domain Security
  slug: witai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: witai
tags:
- Company
- Natural Language Processing
- NLP
- Speech Recognition
- Speech to Text
- Text to Speech
- Intents
- Entities
- Voice
- Conversational AI
- Machine Learning
- Meta
website: https://wit.ai
---
