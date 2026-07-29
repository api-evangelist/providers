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
    agent_card: near-conformant
    agent_skills: true
    agentic_access: derived
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
    well_known_catalog: true
  schema_version: 0.2
  score: 53.0
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Interfaze Agentic Access
  operation_count: 1
  slug: interfaze-agentic-access
  summary_line: 1 operation · 1 acting
api_count: 1
apis:
- description: The Chat API from Interfaze — 1 operation(s) for chat.
  name: Interfaze Chat API
  slug: interfaze-chat-api
artifact_total: 5
common:
- group: other
  title: ''
  type: AgentCard
  url: a2a/interfaze-a2a.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://interfaze.ai/docs
- group: docs
  title: ''
  type: Documentation
  url: https://interfaze.ai/docs
- group: docs
  title: ''
  type: APIReference
  url: https://interfaze.ai/docs/api/chat-completion
- group: start
  title: ''
  type: GettingStarted
  url: https://interfaze.ai/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://interfaze.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://interfaze.ai/dashboard
- group: operate
  title: ''
  type: Support
  url: https://interfaze.ai/help
- group: company
  title: ''
  type: Blog
  url: https://interfaze.ai/blog
- group: operate
  title: ''
  type: StatusPage
  url: https://status.interfaze.ai
- group: commercial
  title: ''
  type: TermsOfService
  url: https://interfaze.ai/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://interfaze.ai/legal/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/InterfazeAI
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/interfaze-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/interfaze-well-known.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/interfaze-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/interfaze-openapi-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/interfaze-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/interfaze-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/interfaze-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/interfaze-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: conventions/interfaze-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/interfaze-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/interfaze-data-model.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/interfaze-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/interfaze-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/interfaze-domain-security.yml
created: '2026-07-17'
description: Interfaze is a Y Combinator (P26) startup building a new model architecture for deterministic developer tasks. Interfaze-beta is a multimodal, OpenAI-compatible Chat Completion API (a hybrid Mixture-of-Architecture combining specialized DNN/CNN vision and audio models with a transformer layer) tuned for high accuracy, precision, and consistency on jobs like OCR, speech-to-text, strict structured/JSON output, object detection with bounding boxes, web search, and web scraping through a single endpoint. It exposes a 1M-token context window, 32k max output, verifiable outputs with confidence scores, built-in sandboxed compute and headless browser tools, and works with the OpenAI, Vercel AI, and LangChain SDKs by swapping the base URL. Founded in 2025 by Yoeven D Khemlani and Harsha Vardhan Khurdula (evolved from JigsawStack) and based in San Francisco.
image: https://interfaze.ai/banner.png
layout: provider
mcp_servers:
- description: ''
  name: interfaze-mcp.yml
  slug: interfaze-mcpyml
modified: '2026-07-19'
name: Interfaze
nav: Providers
network: true
overview: 'Interfaze publishes 1 API on the [APIs.io](https://apis.io/) network: Chat API. Tagged areas include Company, Artificial Intelligence, Machine Learning, LLM, and OCR.


  Interfaze''s developer surface includes documentation, API reference, getting-started guide, pricing, signup flow, support, engineering blog, and 21 more developer resources.'
random_paper: 77
score:
  band: developing
  composite: 50.6
  delta: -0.9
  facets:
    commercial_clarity: 44.7
    contract_quality: 58.5
    developer_ergonomics: 60.9
    discoverability: 87.0
    governance: 11.5
    operational_transparency: 36.8
  previous_composite: 51.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: first-party
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/interfaze/refs/heads/main/screenshots/interfaze-2026-07-25T222700.png
security:
- kind: authentication
  name: Interfaze Authentication
  slug: interfaze-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Interfaze Domain Security
  slug: interfaze-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: interfaze
tags:
- Company
- Artificial Intelligence
- Machine Learning
- LLM
- OCR
- Speech to Text
- Structured Output
- Object Detection
- Web Scraping
- Web Search
- Multimodal
- Developer Tools
website: https://interfaze.ai/docs
---
