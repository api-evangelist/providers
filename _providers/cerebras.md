---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.1
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Cerebras Agentic Access
  operation_count: 3
  slug: cerebras-agentic-access
  summary_line: 3 operations · 2 acting
api_count: 4
apis:
- description: The Cerebras Inference API exposes ultra-low-latency inference for open-weight large language models including Llama 3.1, Llama 4, Qwen, and other frontier open models. The API is OpenAI-compatible at
  name: Cerebras Inference API
  slug: cerebras-inference-api
- description: OpenAI-compatible chat completions.
  name: Cerebras Chat API
  slug: cerebras-chat-api
- description: Text completions.
  name: Cerebras Completions API
  slug: cerebras-completions-api
- description: Discover available models.
  name: Cerebras Models API
  slug: cerebras-models-api
artifact_total: 16
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Cerebras Inference Chat API
  slug: open-cerebras-chat-api
- collection_type: open
  name: Cerebras Inference Chat Completions API
  slug: open-cerebras-completions-api
- collection_type: open
  name: Cerebras Inference Chat Models API
  slug: open-cerebras-models-api
- collection_type: open
  name: Cerebras Inference API
  slug: open-cerebras
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cerebras-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/cerebras-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cerebras-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cerebras-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://cerebras.ai
- group: docs
  title: ''
  type: Documentation
  url: https://inference-docs.cerebras.ai
- group: start
  title: ''
  type: DeveloperPortal
  url: https://cloud.cerebras.ai
- group: commercial
  title: ''
  type: Pricing
  url: https://www.cerebras.ai/inference
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Cerebras
- group: other
  title: ''
  type: ModelZoo
  url: https://github.com/Cerebras/modelzoo
- group: company
  title: ''
  type: Blog
  url: https://www.cerebras.ai/blog
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cerebras-systems
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/CerebrasSystems
- group: operate
  title: ''
  type: Status
  url: https://status.cerebras.ai
- group: agent
  title: ''
  type: LlmsText
  url: https://inference-docs.cerebras.ai/llms.txt
created: '2026-05-23'
description: Cerebras Systems designs the wafer-scale WSE-3 chip and the CS-2/CS-3 AI systems built around it, and operates Cerebras Inference, a high-throughput cloud platform for running open-source large language models including Llama, Qwen, and DeepSeek families. Cerebras Inference is positioned as one of the fastest token-generation services in the market, with OpenAI-compatible REST endpoints, first-party Python and Node.js SDKs, and dedicated and on-prem deployment options for enterprise customers. The company partners with OpenAI, AWS, GSK, Mayo Clinic, and Notion, and maintains an active open source presence including its model garden and inference cookbook on GitHub.
finops:
- name: Cerebras Finops
  service_category: API
  slug: cerebras-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cerebras.png
layout: provider
modified: '2026-05-23'
name: Cerebras
nav: Providers
network: true
overview: 'Cerebras publishes 3 APIs on the [APIs.io](https://apis.io/) network: Chat API, Completions API, and Models API. Tagged areas include AI Inference, Large Language Models, Wafer Scale, Hardware, and Cloud.


  Cerebras'' developer surface includes authentication, documentation, pricing, engineering blog, status page, and 10 more developer resources.'
plans:
- name: Cerebras Plans Pricing
  plan_count: 1
  slug: cerebras-plans-pricing
random_paper: 94
rate_limits:
- limit_count: 2
  name: Cerebras Rate Limits
  slug: cerebras-rate-limits
score:
  band: developing
  composite: 42.4
  delta: -0.4
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 60.1
    developer_ergonomics: 33.3
    discoverability: 81.5
    governance: 0.0
    operational_transparency: 23.7
  previous_composite: 42.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cerebras/refs/heads/main/screenshots/cerebras-2026-06-20T174140.png
security:
- kind: authentication
  name: Cerebras Authentication
  slug: cerebras-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Cerebras Domain Security
  slug: cerebras-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Cerebras Trust Center
  slug: cerebras-trust-center
  summary_line: SOC 2, GDPR
slug: cerebras
tags:
- AI Inference
- Large Language Models
- Wafer Scale
- Hardware
- Cloud
- OpenAI Compatible
- LLM
- SDK
- Accelerator
- High Performance Computing
website: https://cerebras.ai
---
