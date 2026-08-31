---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.1
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Flexai Agentic Access
  operation_count: 8
  slug: flexai-agentic-access
  summary_line: 8 operations · 7 acting
api_count: 1
apis:
- description: Speech-to-text and text-to-speech
  name: FlexAI Audio API
  slug: flexai-audio-api
- description: Chat completions
  name: FlexAI Chat API
  slug: flexai-chat-api
- description: Legacy text completions
  name: FlexAI Completions API
  slug: flexai-completions-api
- description: Vector embeddings
  name: FlexAI Embeddings API
  slug: flexai-embeddings-api
- description: Image generation
  name: FlexAI Images API
  slug: flexai-images-api
- description: Model catalog
  name: FlexAI Models API
  slug: flexai-models-api
- description: Video generation
  name: FlexAI Video API
  slug: flexai-video-api
artifact_total: 28
collections:
- collection_type: postman
  name: FlexAI Token Factory Audio API
  slug: postman-flexai-audio-api
- collection_type: postman
  name: FlexAI Token Factory Audio Chat API
  slug: postman-flexai-chat-api
- collection_type: postman
  name: FlexAI Token Factory Audio Completions API
  slug: postman-flexai-completions-api
- collection_type: postman
  name: FlexAI Token Factory Audio Embeddings API
  slug: postman-flexai-embeddings-api
- collection_type: postman
  name: FlexAI Token Factory Audio Images API
  slug: postman-flexai-images-api
- collection_type: postman
  name: FlexAI Token Factory Audio Models API
  slug: postman-flexai-models-api
- collection_type: postman
  name: FlexAI Token Factory Audio Video API
  slug: postman-flexai-video-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: FlexAI Token Factory Audio API
  slug: open-flexai-audio-api
- collection_type: open
  name: FlexAI Token Factory Audio Chat API
  slug: open-flexai-chat-api
- collection_type: open
  name: FlexAI Token Factory Audio Completions API
  slug: open-flexai-completions-api
- collection_type: open
  name: FlexAI Token Factory Audio Embeddings API
  slug: open-flexai-embeddings-api
- collection_type: open
  name: FlexAI Token Factory Audio Images API
  slug: open-flexai-images-api
- collection_type: open
  name: FlexAI Token Factory Audio Models API
  slug: open-flexai-models-api
- collection_type: open
  name: FlexAI Token Factory Audio Video API
  slug: open-flexai-video-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/flexai/overview
- group: auth
  title: ''
  type: DomainSecurity
  url: security/flexai-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/flexai-agentic-access.yml
- group: company
  title: ''
  type: Website
  url: https://www.flex.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.flex.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.flex.ai
- group: docs
  title: ''
  type: APIReference
  url: https://docs.flex.ai/inference-api/reference/openai-compatibility
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.flex.ai/inference-api/quickstart
- group: company
  title: ''
  type: Blog
  url: https://flex.ai/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://flex.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://tokens.flex.ai/signup
- group: operate
  title: ''
  type: Support
  url: mailto:support@flex.ai
- group: commercial
  title: ''
  type: TermsOfService
  url: https://flex.ai/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://flex.ai/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.flex.ai
- group: auth
  title: ''
  type: TrustCenter
  url: https://security.flex.ai
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/flexai-llms.txt
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/flexai-token-factory-openapi.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/flexai-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/flexai-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/flexai-rate-limits.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/flexai-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/flexai-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/flexai-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/flexai-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/flexai-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/flexai-token-factory-overlay.yaml
- group: commercial
  title: ''
  type: Plans
  url: plans/flexai-plans.yml
created: '2026-07-17'
description: FlexAI is managed inference for builders — an OpenAI-compatible API (Token Factory) that provides a single API key across open models for text, code, reasoning, vision, embeddings, image, video, and audio, priced by usage per model. Beyond serverless inference the platform offers dedicated GPU endpoints, managed LoRA/QLoRA fine-tuning, distributed training, an Agent SDK (in trial), and a private AI cloud (AI Factory) deployable to VPC, on-prem, or air-gapped environments. Because the inference API is a drop-in OpenAI replacement, teams point the OpenAI SDK at the FlexAI base URL and change only the key. FlexAI is backed by Partech and profiled in the API Evangelist network for its developer surface and agent-native infrastructure.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/flexai.png
layout: provider
mcp_servers:
- description: Candidate MCP tool surface derived from the FlexAI Token Factory OpenAPI operations. FlexAI does not publish an official hosted MCP server; this is a starting point that maps each documented operation
  name: FlexAI MCP Server
  slug: flexai-mcp-server
modified: '2026-07-19'
name: FlexAI
nav: Providers
network: true
overview: 'FlexAI publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Audio API, Chat API, Completions API, and 4 more. Tagged areas include Company, Ai/Ml, Artificial Intelligence, Machine-Learning, and Inference.


  FlexAI''s developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, signup flow, support, and 22 more developer resources.'
plans:
- name: Flexai Plans
  plan_count: 3
  slug: flexai-plans
random_paper: 3
rate_limits:
- limit_count: 3
  name: Flexai Rate Limits
  slug: flexai-rate-limits
score:
  band: developing
  composite: 44.7
  coverage:
    artifact_dirs: 19
    catalog_gap: 54.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.6
  facets:
    access_clarity: 71.1
    commercial_clarity: 71.1
    contract_governance: 4.5
    contract_quality: 13.9
    developer_ergonomics: 63.7
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 47.4
  previous_composite: 45.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 7
      marker_coverage: 100.0
      total: 7
    mcp: derived
    skills: derived
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/flexai/refs/heads/main/screenshots/flexai-2026-07-25T214748.png
security:
- kind: authentication
  name: Flexai Authentication
  slug: flexai-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Flexai Domain Security
  slug: flexai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: flexai
tags:
- Company
- Ai/Ml
- Artificial Intelligence
- Machine-Learning
- Inference
- LLM
- Large Language Models
- OpenAI-Compatible
- GPU Compute
- Embeddings
- Fine-Tuning
- Agents
website: https://www.flex.ai/
---
