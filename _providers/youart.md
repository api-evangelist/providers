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
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: Hosted, OAuth-secured Model Context Protocol (MCP) server that gives AI agents access to YouArt's catalog of 60+ image, video, audio, and TTS models plus its node-based workflow builder, asset library
  name: YouArt MCP & Model Platform
  slug: youart-mcp-model-platform
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/youart-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://youart.ai
- group: start
  title: ''
  type: DeveloperPortal
  url: https://youart.ai/mcp
- group: docs
  title: ''
  type: Documentation
  url: https://youart.ai/model
- group: docs
  title: ''
  type: APIReference
  url: https://youart.ai/model
- group: commercial
  title: ''
  type: Pricing
  url: https://youart.ai/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://youart.ai/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://youart.ai/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://youart.typeform.com/enterprise
- group: agent
  title: ''
  type: MCPServer
  url: mcp/youart-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/youart-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/youart-authentication.yml
created: '2026-07-17'
description: YouArt is an all-in-one AI creative studio out of Y Combinator (founded 2025, San Francisco), positioned as "Patreon for AI Originals." It lets creators browse and run 60+ leading image, video, audio, and text-to-speech models — GPT Image 2, Nano Banana, Seedream, Sora 2, Kling, Veo 3, ElevenLabs v3, Suno — or compose them into multi-model, node-based creative workflows on a canvas. Agents and developers connect over a hosted, OAuth-secured Model Context Protocol (MCP) server to generate images, video, and audio and assemble workflows from chat, sharing the same account, credits, and projects as the web application. Creators can also launch original AI films and series, get funded directly by fans, and earn subscription revenue.
image: https://youart.ai/opengraph-image.png
layout: provider
mcp_servers:
- description: ''
  name: youart-mcp.yml
  slug: youart-mcpyml
modified: '2026-07-21'
name: Youart
nav: Providers
network: true
overview: 'Youart publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Generative AI, Image Generation, and Video Generation.


  Youart''s developer surface includes documentation, API reference, pricing, support, authentication, and 7 more developer resources.'
random_paper: 36
score:
  band: emerging
  composite: 23.5
  delta: -1.6
  facets:
    commercial_clarity: 31.6
    contract_quality: 0.0
    developer_ergonomics: 47.8
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 25.1
  provenance:
    mcp: first-party
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Youart Authentication
  slug: youart-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Youart Domain Security
  slug: youart-domain-security
  summary_line: TLSv1.3
slug: youart
tags:
- Company
- Artificial Intelligence
- Generative AI
- Image Generation
- Video Generation
- Text to Speech
- Creative Tools
- Model Context Protocol
- AI Agents
- Y Combinator
website: https://youart.ai
---
