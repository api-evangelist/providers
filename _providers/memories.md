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
  band: agent-native
  dimensions:
    agent_skills: true
    agentic_access: true
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.1
  score: 81.7
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 27
  human_in_the_loop: 1
  name: Memories Agentic Access
  operation_count: 34
  slug: memories-agentic-access
  summary_line: 34 operations · 27 acting · 1 human-in-the-loop
api_count: 3
apis:
- description: The Serve API from Memories — 30 operation(s) for serve.
  name: Memories Serve API
  slug: memories-serve-api
- description: The Stream Understanding API from Memories — 2 operation(s) for stream understanding.
  name: Memories Stream Understanding API
  slug: memories-stream-understanding-api
- description: The Understand API from Memories — 2 operation(s) for understand.
  name: Memories Understand API
  slug: memories-understand-api
artifact_total: 10
asyncapis:
- description: ''
  name: Memories Webhooks
  slug: memories-webhooks
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/memories-trust-center.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api-platform.memories.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://api-tools.memories.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://api-tools.memories.ai/visual-intelligence/getting-started/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://api-tools.memories.ai/visual-intelligence/getting-started/introduction
- group: start
  title: ''
  type: SignUp
  url: https://api-platform.memories.ai/
- group: commercial
  title: ''
  type: Pricing
  url: https://api-tools.memories.ai/visual-search/pricing
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Memories-ai-labs
- group: auth
  title: ''
  type: Compliance
  url: https://memories.ai/security
- group: auth
  title: ''
  type: Authentication
  url: authentication/memories-authentication.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/memories-agentic-access.yml
- group: build
  title: ''
  type: Packages
  url: packages/memories-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/memories-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/memories-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/memories-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/memories-webhooks.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/memories-error-codes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/memories-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/memories-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/memories-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/memories-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/memories-data-model.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/memories-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/memories-well-known.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/memories-platform-overlay.yaml
- group: company
  title: ''
  type: Website
  url: http://memories.ai
created: '2026-07-17'
description: 'Memories.ai (MAVI) is a video-intelligence platform that turns raw video into searchable, agent-ready understanding. It ships three products on a shared video-understanding stack: Visual Intelligence (stateless REST APIs for transcription, captioning, frame description, embeddings, social-media scraping, and real-time audio/video stream moderation via VLMs such as Gemini, Nova, and Qwen), Visual Search (an auto-indexed private and public video/image library searchable by text, image, or transcript), and Visual Agents (pre-built workflows for video search, AI video editing, and screenplay extraction). The platform authenticates with sk-mavi- API keys, bills on a unified per-endpoint credit model, and is HIPAA, SOC 2 Type 2, and GDPR compliant. It is a Seedcamp portfolio company.'
image: https://mintcdn.com/memories/xyhRN3OJaXxxzcxh/logo/logo.png
layout: provider
mcp_servers:
- description: ''
  name: memories-mcp.yml
  slug: memories-mcpyml
modified: '2026-07-20'
name: Memories
nav: Providers
network: true
overview: 'Memories publishes 3 APIs on the [APIs.io](https://apis.io/) network: Serve API, Stream Understanding API, and Understand API. Tagged areas include Company, Video Intelligence, Video Understanding, Video Search, and Transcription.


  The Memories catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Memories'' developer surface includes documentation, API reference, getting-started guide, signup flow, pricing, authentication, CLI, and 20 more developer resources.'
random_paper: 49
rate_limits:
- limit_count: 4
  name: Memories Rate Limits
  slug: memories-rate-limits
score:
  band: developing
  composite: 52.8
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 62.5
    developer_ergonomics: 67.4
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 44.7
  previous_composite: 52.8
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
security:
- kind: authentication
  name: Memories Authentication
  slug: memories-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Memories Domain Security
  slug: memories-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Memories Trust Center
  slug: memories-trust-center
  summary_line: SOC 2, HIPAA, GDPR
slug: memories
tags:
- Company
- Video Intelligence
- Video Understanding
- Video Search
- Transcription
- Embeddings
- Multimodal AI
- Content Moderation
- AI Agents
- Machine Learning
website: http://memories.ai
---
