---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 13
  human_in_the_loop: 0
  name: Zhipu Ai Agentic Access
  operation_count: 14
  slug: zhipu-ai-agentic-access
  summary_line: 14 operations · 13 acting
api_count: 3
apis:
- description: The Agents API from Zhipu AI — 3 operation(s) for agents.
  name: Zhipu AI Agents API
  slug: zhipu-ai-agents-api
- description: The Paas API from Zhipu AI — 10 operation(s) for paas.
  name: Zhipu AI Paas API
  slug: zhipu-ai-paas-api
- description: The Tools API API from Zhipu AI — 1 operation(s) for tools api.
  name: Zhipu AI Tools API API
  slug: zhipu-ai-tools-api-api
artifact_total: 11
collections:
- collection_type: open
  name: Z.AI API
  slug: open-zhipu-ai
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/zhipu-ai-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/zhipu-ai-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/zhipu-ai-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/zhipu-ai-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/zai-org
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/zhipuai
- group: company
  title: ''
  type: Website
  url: https://www.zhipuai.cn/
- group: company
  title: ''
  type: AlternateWebsite
  url: https://z.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.z.ai
- group: commercial
  title: ''
  type: Plans
  url: plans/zhipu-ai-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/zhipu-ai-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/zhipu-ai-finops.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.z.ai/llms.txt
created: '2026-05-08'
description: Zhipu AI (Z.ai / BigModel) is a Chinese AI research lab and the developer of the GLM (General Language Model) family. The Z.ai open platform exposes chat completions, vision, image generation, video generation, web search, audio transcription, embeddings, fine-tuning, and agent APIs across the GLM-5, GLM-4.7, GLM-4.6, and GLM-4.5 model series.
finops:
- name: Zhipu Ai Finops
  service_category: AI and Machine Learning
  slug: zhipu-ai-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/zhipu-ai.png
layout: provider
modified: '2026-05-19'
name: Zhipu AI
nav: Providers
network: true
overview: 'Zhipu AI publishes 3 APIs on the [APIs.io](https://apis.io/) network: Agents API, Paas API, and Tools API API. Tagged areas include AI, LLM, Inference, GLM, and ChatGLM.


  Zhipu AI''s developer surface includes authentication, documentation, and 11 more developer resources.'
plans:
- name: Zhipu Ai Plans Pricing
  plan_count: 3
  slug: zhipu-ai-plans-pricing
random_paper: 59
rate_limits:
- limit_count: 3
  name: Zhipu Ai Rate Limits
  slug: zhipu-ai-rate-limits
score:
  band: thin
  composite: 38.3
  delta: 3.3
  facets:
    commercial_clarity: 39.5
    contract_quality: 46.6
    developer_ergonomics: 19.6
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 35.0
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/zhipu-ai/refs/heads/main/screenshots/zhipu-ai-2026-06-20T201901.png
security:
- kind: authentication
  name: Zhipu Ai Authentication
  slug: zhipu-ai-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Zhipu Ai Domain Security
  slug: zhipu-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Zhipu Ai Vulnerability Disclosure
  slug: zhipu-ai-vulnerability-disclosure
  summary_line: disclosure policy published
slug: zhipu-ai
tags:
- AI
- LLM
- Inference
- GLM
- ChatGLM
- Multimodal
website: https://www.zhipuai.cn/
---
