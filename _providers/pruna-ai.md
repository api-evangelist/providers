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
  band_gated_from: agent-native
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
    mcp_server: derived
    openapi_examples: verified
    rate_limit_signal: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 51.1
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Pruna Ai Agentic Access
  operation_count: 4
  slug: pruna-ai-agentic-access
  summary_line: 4 operations · 2 acting
api_count: 3
apis:
- description: Download generated content files
  name: Pruna AI Content Delivery API
  slug: pruna-ai-content-delivery-api
- description: Upload files to be used as input for predictions
  name: Pruna AI File Management API
  slug: pruna-ai-file-management-api
- description: Core prediction workflow operations
  name: Pruna AI Predictions API
  slug: pruna-ai-predictions-api
artifact_total: 8
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/pruna-ai-openapi-overlay.yaml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.api.pruna.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.pruna.ai/en/stable/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.api.pruna.ai/apis/models-api-0/versions/d086a242-3813-4148-a087-e724d4b333f8
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.api.pruna.ai/guides/quickstart
- group: start
  title: ''
  type: SignUp
  url: https://dashboard.pruna.ai/login
- group: commercial
  title: ''
  type: Pricing
  url: https://www.pruna.ai/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.pruna.ai/blog
- group: operate
  title: ''
  type: Support
  url: https://discord.gg/JFQmtFKCjd
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/PrunaAI
- group: commercial
  title: ''
  type: TermsOfService
  url: https://docs.api.pruna.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.pruna.ai/privacy-notice
- group: start
  title: ''
  type: Sandbox
  url: https://demo.pruna.ai/
- group: auth
  title: ''
  type: Authentication
  url: authentication/pruna-ai-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/pruna-ai-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/pruna-ai-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/pruna-ai-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/pruna-ai-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/pruna-ai-data-model.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/pruna-ai-rate-limits.yml
- group: build
  title: ''
  type: Packages
  url: packages/pruna-ai-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/pruna-ai-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/pruna-ai-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/pruna-ai-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/pruna-ai-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pruna-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.pruna.ai/
created: '2026-07-17'
description: 'Pruna AI builds Performance Models (P-Series) — optimized image and video generation models engineered to be faster, cheaper, and smaller than standard alternatives while keeping quality high. It ships three ways: a hosted HTTP API (P-API) that exposes ~20 models (text-to-image, image editing, upscaling, virtual try-on, text/image-to-video, avatar, animation and replacement, plus LoRA trainers) behind a single endpoint selected via a request header; an open-source Python optimization framework (pruna / pruna-pro) for caching, quantization, pruning, distillation and compilation of your own models; and hosted demos. The P-API uses apikey-header auth with an async submit/poll/download workflow and an optional synchronous mode. Pruna AI is a portfolio company of EQT Ventures.'
image: https://framerusercontent.com/images/tM3dYw39zvWf45dsZXfTkZm0jNc.png
layout: provider
mcp_servers:
- description: ''
  name: pruna-ai-mcp.yml
  slug: pruna-ai-mcpyml
modified: '2026-07-20'
name: Pruna AI
nav: Providers
network: true
overview: 'Pruna AI publishes 3 APIs on the [APIs.io](https://apis.io/) network: Content Delivery API, File Management API, and Predictions API. Tagged areas include Company, Artificial Intelligence, Machine Learning, Image Generation, and Video Generation.


  Pruna AI''s developer surface includes documentation, API reference, getting-started guide, signup flow, pricing, engineering blog, support, and 21 more developer resources.'
random_paper: 101
rate_limits:
- limit_count: 1
  name: Pruna Ai Rate Limits
  slug: pruna-ai-rate-limits
score:
  band: developing
  composite: 51.7
  delta: -1.8
  facets:
    commercial_clarity: 44.7
    contract_quality: 64.2
    developer_ergonomics: 69.0
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 26.3
  previous_composite: 53.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: derived
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
security:
- kind: authentication
  name: Pruna Ai Authentication
  slug: pruna-ai-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Pruna Ai Domain Security
  slug: pruna-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: pruna-ai
tags:
- Company
- Artificial Intelligence
- Machine Learning
- Image Generation
- Video Generation
- Generative AI
- Model Optimization
- Inference
- Developer Tools
website: https://www.pruna.ai/
---
