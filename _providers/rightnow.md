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
    auth_clarity: false
    consent_identity: true
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: verified
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 28.8
  scored_at: '2026-07-28'
api_count: 7
apis:
- description: The Audio API from RightNow AI — 2 operation(s) for audio.
  name: RightNow AI Audio API
  slug: rightnow-audio-api
- description: The Chat API from RightNow AI — 1 operation(s) for chat.
  name: RightNow AI Chat API
  slug: rightnow-chat-api
- description: The Embeddings API from RightNow AI — 1 operation(s) for embeddings.
  name: RightNow AI Embeddings API
  slug: rightnow-embeddings-api
- description: The Images API from RightNow AI — 1 operation(s) for images.
  name: RightNow AI Images API
  slug: rightnow-images-api
- description: The Models API from RightNow AI — 2 operation(s) for models.
  name: RightNow AI Models API
  slug: rightnow-models-api
- description: The Rerank API from RightNow AI — 1 operation(s) for rerank.
  name: RightNow AI Rerank API
  slug: rightnow-rerank-api
- description: The Responses API from RightNow AI — 1 operation(s) for responses.
  name: RightNow AI Responses API
  slug: rightnow-responses-api
artifact_total: 11
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/rightnow-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/rightnow-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://runinfra.ai/docs
- group: docs
  title: ''
  type: Documentation
  url: https://runinfra.ai/docs
- group: docs
  title: ''
  type: APIReference
  url: https://runinfra.ai/docs/api-reference/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://runinfra.ai/docs/introduction/quickstart
- group: start
  title: ''
  type: Quickstart
  url: https://runinfra.ai/docs/introduction/quickstart
- group: start
  title: ''
  type: SignUp
  url: https://runinfra.ai/sign-up
- group: start
  title: ''
  type: Login
  url: https://runinfra.ai/sign-in
- group: commercial
  title: ''
  type: Pricing
  url: https://runinfra.ai/pricing
- group: company
  title: ''
  type: Blog
  url: https://runinfra.ai/news
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/RightNow-AI
- group: operate
  title: ''
  type: Support
  url: https://runinfra.ai/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://runinfra.ai/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://runinfra.ai/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.runinfra.ai/
- group: company
  title: ''
  type: Twitter
  url: https://x.com/runinfrai
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/showcase/runinfra/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/rightnow-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/rightnow-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/rightnow-security.txt
- group: build
  title: ''
  type: SDKs
  url: packages/rightnow-packages.yml
- group: build
  title: ''
  type: Packages
  url: packages/rightnow-packages.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/rightnow-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/rightnow-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/rightnow-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/rightnow-changelog.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/rightnow-conformance.yml
- group: auth
  title: ''
  type: Security
  url: security/rightnow-vulnerability-disclosure.yml
created: '2026-07-17'
description: RightNow AI (RunInfra) turns plain-English descriptions of an inference workload into production, OpenAI-compatible AI endpoints. The platform selects open-source models from Hugging Face, benchmarks GPU options, applies kernel optimizations (quantization, speculative decoding, KV-cache tuning, Forge kernels), and deploys serverless, pay-per-token inference APIs on RunInfra Cloud, RunPod, Modal, or self-hosted GPUs. Its REST API is OpenAI-shaped and covers chat completions, responses, embeddings, rerank, image generation, audio speech and transcription, and model listing. A Y Combinator-backed research lab, RightNow AI also publishes open-source GPU-kernel and inference tooling.
image: https://runinfra.ai/favicon.ico
layout: provider
modified: '2026-07-21'
name: RightNow AI
nav: Providers
network: true
overview: 'RightNow AI publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Audio API, Chat API, Embeddings API, and 4 more. Tagged areas include Company, Artificial Intelligence, Machine Learning, LLM Inference, and GPU.


  RightNow AI''s developer surface includes documentation, API reference, getting-started guide, quickstart, signup flow, pricing, engineering blog, and 22 more developer resources.'
random_paper: 35
score:
  band: developing
  composite: 55.0
  delta: 0.2
  facets:
    commercial_clarity: 60.5
    contract_quality: 61.9
    developer_ergonomics: 47.8
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 55.3
  previous_composite: 54.8
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: derived
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Rightnow Authentication
  slug: rightnow-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Rightnow Domain Security
  slug: rightnow-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Rightnow Vulnerability Disclosure
  slug: rightnow-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Rightnow Trust Center
  slug: rightnow-trust-center
  summary_line: SOC 2, HIPAA, GDPR
slug: rightnow
tags:
- Company
- Artificial Intelligence
- Machine Learning
- LLM Inference
- GPU
- Model Deployment
- Serverless
- OpenAI Compatible
- Embeddings
- MLOps
website: https://runinfra.ai/docs
---
