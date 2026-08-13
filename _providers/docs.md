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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 12.6
  scored_at: '2026-08-12'
api_count: 1
apis:
- description: OpenAI-compatible model-inference API over Infini-AI's catalog of open- and closed-source models. Bearer (API Key) authentication; chat/completions, models, embeddings and image/video generation endpo
  name: Infini-AI GenStudio Large-Model Service (MaaS)
  slug: infini-ai-genstudio-large-model-service-maas
artifact_total: 3
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://cloud.infini-ai.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.infini-ai.com
- group: docs
  title: ''
  type: APIReference
  url: https://cloud.infini-ai.com/gen-studio/api/reference/maas.html
- group: start
  title: ''
  type: GettingStarted
  url: https://cloud.infini-ai.com/gen-studio/api/get-started/overview.html
- group: commercial
  title: ''
  type: Pricing
  url: https://cloud.infini-ai.com/gen-studio/api/usage-and-billing/billing.html
- group: start
  title: ''
  type: SignUp
  url: https://cloud.infini-ai.com
- group: auth
  title: ''
  type: Authentication
  url: authentication/docs-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/docs-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/docs-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/docs-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/docs-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/docs-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/docs-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://docs.infini-ai.com
created: '2026-07-17'
description: Infini-AI (无问芯穹 / Infinigence AI) is a Chinese AGI compute and model-service platform, backed by Qiming, that helps teams optimize model development, fine-tuning, and inference across heterogeneous compute. Its GenStudio large-model service (MaaS) exposes an OpenAI-compatible REST API over a broad catalog of open- and closed-source models (LLM chat/completions plus image and video generation), with LoRA/SFT fine-tuning and multi-LoRA deployment. The platform also offers a fully managed ComfyUI workflow-hosting service (with a WebSocket API) and an Agent Service Platform for building and deploying agent applications and skills. Developers authenticate with a tenant-managed API Key sent as a Bearer token; tenant/IAM, usage analytics, rate limits, billing, and error-code references are documented at docs.infini-ai.com and the cloud console.
image: https://content.cloud.infini-ai.com/platform-web-prod/logo_small.png
layout: provider
modified: '2026-07-18'
name: Infini-AI (无问芯穹)
nav: Providers
network: true
overview: 'Infini-AI (无问芯穹) publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Machine Learning, Large Language Models, and Model as a Service.


  Infini-AI (无问芯穹)''s developer surface includes documentation, API reference, getting-started guide, pricing, signup flow, authentication, and 8 more developer resources.'
random_paper: 65
score:
  band: emerging
  composite: 21.8
  delta: 0.0
  facets:
    commercial_clarity: 23.7
    contract_quality: 0.0
    developer_ergonomics: 45.7
    discoverability: 75.9
    governance: 3.1
    operational_transparency: 0.0
  previous_composite: 21.8
  provenance:
    conformance: derived
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/docs/refs/heads/main/screenshots/docs-2026-07-25T212217.png
security:
- kind: authentication
  name: Docs Authentication
  slug: docs-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Docs Domain Security
  slug: docs-domain-security
  summary_line: TLSv1.3 · DMARC
slug: docs
tags:
- Company
- Artificial Intelligence
- Machine Learning
- Large Language Models
- Model as a Service
- Inference
- ComfyUI
- Agents
- AGI Compute
- OpenAI-Compatible
website: https://docs.infini-ai.com
---
