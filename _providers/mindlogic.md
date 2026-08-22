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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.0
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Mindlogic Agentic Access
  operation_count: 17
  slug: mindlogic-agentic-access
  summary_line: 17 operations · 9 acting
api_count: 7
apis:
- description: The Audio API from Mindlogic — 1 operation(s) for audio.
  name: Mindlogic Audio API
  slug: mindlogic-audio-api
- description: The Chat API from Mindlogic — 1 operation(s) for chat.
  name: Mindlogic Chat API
  slug: mindlogic-chat-api
- description: The Credits API from Mindlogic — 1 operation(s) for credits.
  name: Mindlogic Credits API
  slug: mindlogic-credits-api
- description: The gateway API from Mindlogic — 7 operation(s) for gateway.
  name: Mindlogic gateway API
  slug: mindlogic-gateway-api
- description: The Images API from Mindlogic — 2 operation(s) for images.
  name: Mindlogic Images API
  slug: mindlogic-images-api
- description: The Models API from Mindlogic — 2 operation(s) for models.
  name: Mindlogic Models API
  slug: mindlogic-models-api
- description: The Video API from Mindlogic — 3 operation(s) for video.
  name: Mindlogic Video API
  slug: mindlogic-video-api
artifact_total: 19
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Fast Audio API
  slug: open-mindlogic-audio-api
- collection_type: open
  name: Fast Audio Chat API
  slug: open-mindlogic-chat-api
- collection_type: open
  name: Fast Audio Credits API
  slug: open-mindlogic-credits-api
- collection_type: open
  name: Fast Audio gateway API
  slug: open-mindlogic-gateway-api
- collection_type: open
  name: Fast Audio Images API
  slug: open-mindlogic-images-api
- collection_type: open
  name: Fast Audio Models API
  slug: open-mindlogic-models-api
- collection_type: open
  name: Fast Audio Video API
  slug: open-mindlogic-video-api
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.mindlogic.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.mindlogic.ai/docs
- group: docs
  title: ''
  type: APIReference
  url: https://docs.mindlogic.ai/docs/general/api-gateway/reference/chat-completions
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.mindlogic.ai/docs/general/api-gateway/getting-started/overview
- group: auth
  title: ''
  type: Authentication
  url: authentication/mindlogic-authentication.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/mindlogic-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/mindlogic-error-codes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/mindlogic-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/mindlogic-conformance.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/mindlogic-api-gateway-overlay.yaml
- group: design
  title: ''
  type: DataModel
  url: data-model/mindlogic-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/mindlogic-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/mindlogic-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mindlogic-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/mindlogic-agentic-access.yml
- group: company
  title: ''
  type: Blog
  url: https://blog.mindlogic.ai/
- group: operate
  title: ''
  type: Support
  url: https://docs.mindlogic.ai/docs/general/factchat/support/help-center
- group: commercial
  title: ''
  type: TermsOfService
  url: https://factchat-public.s3.ap-northeast-2.amazonaws.com/public/pdf/ko_terms_of_service.pdf
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://factchat-public.s3.ap-northeast-2.amazonaws.com/public/pdf/ko_privacy_policy.pdf
- group: company
  title: ''
  type: Website
  url: https://mindlogic.ai/
created: '2026-07-17'
description: Mindlogic is a South Korean generative-AI company whose products include FactChat (a multi-LLM enterprise chat platform with Studio chatbot building, deep research, meeting notes, and image/video generation), Bliss (a persona chatbot that learns a person's voice and personality for fan engagement), and Informe (a multilingual document-grounded website chatbot). For developers, Mindlogic operates the FactChat API Gateway — a unified, OpenAI- and Anthropic-compatible LLM proxy that fronts models from OpenAI, Anthropic, Google Gemini, xAI and Perplexity behind a single API key, metered in credits, with chat completions, an OpenAI Responses pass-through, an Anthropic Messages pass-through, text-to-speech, and image/video generation.
image: https://mindlogic.ai/apple-icon.png
layout: provider
mcp_servers:
- description: ''
  name: mindlogic-mcp.yml
  slug: mindlogic-mcpyml
modified: '2026-07-20'
name: Mindlogic
nav: Providers
network: true
overview: 'Mindlogic publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Audio API, Chat API, Credits API, and 4 more. Tagged areas include Company, AI/ML, Generative AI, Conversational AI, and LLM Gateway.


  Mindlogic''s developer surface includes documentation, API reference, getting-started guide, authentication, engineering blog, support, and 15 more developer resources.'
random_paper: 5
score:
  band: thin
  composite: 39.1
  delta: 1.1
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 30.3
    contract_quality: 45.1
    developer_ergonomics: 58.9
    discoverability: 81.5
    governance: 30.3
    operational_transparency: 0.0
  previous_composite: 38.0
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: derived
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mindlogic/refs/heads/main/screenshots/mindlogic-2026-08-07T172941.png
security:
- kind: authentication
  name: Mindlogic Authentication
  slug: mindlogic-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Mindlogic Domain Security
  slug: mindlogic-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: mindlogic
tags:
- Company
- AI/ML
- Generative AI
- Conversational AI
- LLM Gateway
- Chatbots
- API Gateway
- Korea
website: https://mindlogic.ai/
---
