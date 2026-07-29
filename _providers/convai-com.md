---
access_model:
  confidence: high
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: true
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 31
  human_in_the_loop: 0
  name: Convai Com Agentic Access
  operation_count: 34
  slug: convai-com-agentic-access
  summary_line: 34 operations · 31 acting
api_count: 10
apis:
- description: The Characters API from Convai — 6 operation(s) for characters.
  name: Convai Characters API
  slug: convai-com-characters-api
- description: The Chat History API from Convai — 2 operation(s) for chat history.
  name: Convai Chat History API
  slug: convai-com-chat-history-api
- description: The Custom LLM API from Convai — 4 operation(s) for custom llm.
  name: Convai Custom LLM API
  slug: convai-com-custom-llm-api
- description: The Evaluation API from Convai — 1 operation(s) for evaluation.
  name: Convai Evaluation API
  slug: convai-com-evaluation-api
- description: The Interaction API from Convai — 1 operation(s) for interaction.
  name: Convai Interaction API
  slug: convai-com-interaction-api
- description: The Knowledge Bank API from Convai — 4 operation(s) for knowledge bank.
  name: Convai Knowledge Bank API
  slug: convai-com-knowledge-bank-api
- description: The Live API from Convai — 1 operation(s) for live.
  name: Convai Live API
  slug: convai-com-live-api
- description: The Narrative API from Convai — 11 operation(s) for narrative.
  name: Convai Narrative API
  slug: convai-com-narrative-api
- description: The Streaming API from Convai — 1 operation(s) for streaming.
  name: Convai Streaming API
  slug: convai-com-streaming-api
- description: The TTS API from Convai — 3 operation(s) for tts.
  name: Convai TTS API
  slug: convai-com-tts-api
artifact_total: 40
collections:
- collection_type: postman
  name: Convai Character Characters API
  slug: postman-convai-com-characters-api
- collection_type: postman
  name: Convai Character Characters Chat History API
  slug: postman-convai-com-chat-history-api
- collection_type: postman
  name: Convai Character Characters Custom LLM API
  slug: postman-convai-com-custom-llm-api
- collection_type: postman
  name: Convai Character Characters Evaluation API
  slug: postman-convai-com-evaluation-api
- collection_type: postman
  name: Convai Character Characters Interaction API
  slug: postman-convai-com-interaction-api
- collection_type: postman
  name: Convai Character Characters Knowledge Bank API
  slug: postman-convai-com-knowledge-bank-api
- collection_type: postman
  name: Convai Character Characters Live API
  slug: postman-convai-com-live-api
- collection_type: postman
  name: Convai Character Characters Narrative API
  slug: postman-convai-com-narrative-api
- collection_type: postman
  name: Convai Character Characters Streaming API
  slug: postman-convai-com-streaming-api
- collection_type: postman
  name: Convai Character Characters TTS API
  slug: postman-convai-com-tts-api
- collection_type: open
  name: Convai Character API
  slug: open-convai-character-api
- collection_type: open
  name: Convai Chat History API
  slug: open-convai-chat-history-api
- collection_type: open
  name: Convai Custom LLM API
  slug: open-convai-custom-llm-api
- collection_type: open
  name: Convai Evaluation API
  slug: open-convai-evaluation-api
- collection_type: open
  name: Convai Interaction API
  slug: open-convai-interaction-api
- collection_type: open
  name: Convai Knowledge Bank API
  slug: open-convai-knowledge-bank-api
- collection_type: open
  name: Convai Live API
  slug: open-convai-live-api
- collection_type: open
  name: Convai Narrative Design API
  slug: open-convai-narrative-design-api
- collection_type: open
  name: Convai Streaming Transcription API
  slug: open-convai-streaming-transcription-api
- collection_type: open
  name: Convai Text-to-Speech API
  slug: open-convai-tts-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/convai/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/convai-com-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/convai-com-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/convai-com-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://convai.com
- group: start
  title: ''
  type: Sandbox
  url: https://convai.com/playground
- group: docs
  title: ''
  type: Documentation
  url: https://docs.convai.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.convai.com/api-docs/welcome
- group: docs
  title: ''
  type: Documentation
  url: https://docs.convai.com/api-docs/api-reference/core-api-reference
- group: commercial
  title: ''
  type: Pricing
  url: https://convai.com/pricing
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Conv-AI
- group: operate
  title: ''
  type: Forums
  url: https://forum.convai.com
- group: company
  title: ''
  type: Blog
  url: https://convai.com/blog
- group: company
  title: ''
  type: About
  url: https://convai.com/about
- group: operate
  title: ''
  type: ContactSales
  url: https://convai.com/contact-sales
- group: commercial
  title: ''
  type: TermsOfService
  url: https://convai.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://convai.com/privacy-policy
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Conv-AI/Convai-UnrealEngine-SDK-V4
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Conv-AI/Convai-UnrealEngine-SDK
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Conv-AI/Convai-Web-SDK-Old
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Conv-AI/Convai-JS-SDK-Alpha
- group: build
  title: ''
  type: Tools
  url: https://github.com/Conv-AI/convai-analytics
- group: build
  title: ''
  type: Tools
  url: https://github.com/Conv-AI/convai-evals
- group: build
  title: ''
  type: Tools
  url: https://github.com/Conv-AI/Convai-UnrealEngine-ModdingTool
- group: build
  title: ''
  type: Tools
  url: https://github.com/Conv-AI/Convai-UnrealEngine-PakManager
- group: commercial
  title: ''
  type: Pricing
  url: plans/convai-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/convai-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/convai-finops.yml
created: '2026-05-25'
finops:
- name: Convai Finops
  service_category: AI and Machine Learning
  slug: convai-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/convai-com.png
json_schemas:
- name: Convai Character
  property_count: 10
  slug: convai-character
- name: Convai Interaction
  property_count: 2
  slug: convai-interaction
jsonld:
- class_count: 0
  name: Convai Context
  property_count: 6
  slug: convai-context
layout: provider
modified: '2026-05-25'
name: Convai
nav: Providers
network: true
overview: 'Convai publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Characters API, Chat History API, Custom LLM API, and 7 more. Tagged areas include AI, Conversational AI, Characters, NPCs, and Virtual Worlds.


  The Convai catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Convai''s developer surface includes authentication, developer portal, sandbox, documentation, pricing, engineering blog, tooling, and 21 more developer resources.'
plans:
- name: Convai Plans Pricing
  plan_count: 5
  slug: convai-plans-pricing
random_paper: 44
rate_limits:
- limit_count: 7
  name: Convai Rate Limits
  slug: convai-rate-limits
rules:
- name: Convai API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: convai-com-jsonschema-spectral-rules
score:
  band: strong
  composite: 59.5
  delta: -2.6
  facets:
    commercial_clarity: 71.1
    contract_quality: 66.7
    developer_ergonomics: 56.5
    discoverability: 55.6
    governance: 58.3
    operational_transparency: 36.8
  previous_composite: 62.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/convai-com/refs/heads/main/screenshots/convai-com-2026-06-20T174957.png
security:
- kind: authentication
  name: Convai Com Authentication
  slug: convai-com-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Convai Com Domain Security
  slug: convai-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: convai-com
tags:
- AI
- Conversational AI
- Characters
- NPCs
- Virtual Worlds
- Games
- Avatars
- Speech
- TTS
- WebRTC
website: https://convai.com
---
