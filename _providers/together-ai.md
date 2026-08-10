---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 42.3
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 57
  human_in_the_loop: 2
  name: Together Ai Agentic Access
  operation_count: 116
  slug: together-ai-agentic-access
  summary_line: 116 operations · 57 acting · 2 human-in-the-loop
api_count: 28
apis:
- description: The Audio API from Together AI — 5 operation(s) for audio.
  name: Together AI Audio API
  slug: together-ai-audio-api
- description: The Batches API from Together AI — 3 operation(s) for batches.
  name: Together AI Batches API
  slug: together-ai-batches-api
- description: The Chat API from Together AI — 1 operation(s) for chat.
  name: Together AI Chat API
  slug: together-ai-chat-api
- description: The Code Interpreter API from Together AI — 2 operation(s) for code interpreter.
  name: Together AI Code Interpreter API
  slug: together-ai-code-interpreter-api
- description: The Completion API from Together AI — 1 operation(s) for completion.
  name: Together AI Completion API
  slug: together-ai-completion-api
- description: The Compute API from Together AI — 6 operation(s) for compute.
  name: Together AI Compute API
  slug: together-ai-compute-api
- description: The Deployments API from Together AI — 3 operation(s) for deployments.
  name: Together AI Deployments API
  slug: together-ai-deployments-api
- description: The DeploymentsStorage API from Together AI — 1 operation(s) for deploymentsstorage.
  name: Together AI DeploymentsStorage API
  slug: together-ai-deploymentsstorage-api
- description: The DeploymentsVolumes API from Together AI — 1 operation(s) for deploymentsvolumes.
  name: Together AI DeploymentsVolumes API
  slug: together-ai-deploymentsvolumes-api
- description: The Embeddings API from Together AI — 1 operation(s) for embeddings.
  name: Together AI Embeddings API
  slug: together-ai-embeddings-api
- description: The Endpoints API from Together AI — 3 operation(s) for endpoints.
  name: Together AI Endpoints API
  slug: together-ai-endpoints-api
- description: The evaluation API from Together AI — 4 operation(s) for evaluation.
  name: Together AI evaluation API
  slug: together-ai-evaluation-api
- description: The Files API from Together AI — 4 operation(s) for files.
  name: Together AI Files API
  slug: together-ai-files-api
- description: The Fine-tuning API from Together AI — 10 operation(s) for fine-tuning.
  name: Together AI Fine-tuning API
  slug: together-ai-fine-tuning-api
- description: The GPUClusterService API from Together AI — 5 operation(s) for gpuclusterservice.
  name: Together AI GPUClusterService API
  slug: together-ai-gpuclusterservice-api
- description: The Hardware API from Together AI — 1 operation(s) for hardware.
  name: Together AI Hardware API
  slug: together-ai-hardware-api
- description: The Images API from Together AI — 1 operation(s) for images.
  name: Together AI Images API
  slug: together-ai-images-api
- description: The Jobs API from Together AI — 2 operation(s) for jobs.
  name: Together AI Jobs API
  slug: together-ai-jobs-api
- description: The Models API from Together AI — 1 operation(s) for models.
  name: Together AI Models API
  slug: together-ai-models-api
- description: The Queue API from Together AI — 4 operation(s) for queue.
  name: Together AI Queue API
  slug: together-ai-queue-api
- description: The RegionService API from Together AI — 2 operation(s) for regionservice.
  name: Together AI RegionService API
  slug: together-ai-regionservice-api
- description: The Rerank API from Together AI — 1 operation(s) for rerank.
  name: Together AI Rerank API
  slug: together-ai-rerank-api
- description: The RL API from Together AI — 14 operation(s) for rl.
  name: Together AI RL API
  slug: together-ai-rl-api
- description: The Secrets API from Together AI — 2 operation(s) for secrets.
  name: Together AI Secrets API
  slug: together-ai-secrets-api
- description: The SharedVolumeService API from Together AI — 5 operation(s) for sharedvolumeservice.
  name: Together AI SharedVolumeService API
  slug: together-ai-sharedvolumeservice-api
- description: The Video API from Together AI — 2 operation(s) for video.
  name: Together AI Video API
  slug: together-ai-video-api
- description: The Voices API from Together AI — 1 operation(s) for voices.
  name: Together AI Voices API
  slug: together-ai-voices-api
- description: The Volumes API from Together AI — 1 operation(s) for volumes.
  name: Together AI Volumes API
  slug: together-ai-volumes-api
artifact_total: 41
asyncapis:
- description: AsyncAPI 2.6 description of Together AI's streaming (Server-Sent Events) inference surface. Together AI exposes OpenAI-compatible HTTP endpoints that upgrade to a `text/event-stream` response when the
  name: Together AI Streaming Inference API
  slug: together-ai-asyncapi
collections:
- collection_type: open
  name: remediation.proto
  slug: open-together-ai-clusters-remediation
- collection_type: open
  name: API Collection
  slug: open-together-ai-tcloud
- collection_type: open
  name: Together APIs
  slug: open-together-ai
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/together-ai-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/together-ai-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/together-ai-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/together-ai-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/togethercomputer
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/togethercomputer
- group: company
  title: ''
  type: Website
  url: https://www.together.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.together.ai/
- group: commercial
  title: ''
  type: Plans
  url: plans/together-ai-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/together-ai-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/together-ai-finops.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.together.ai/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://www.together.ai/blog/rss.xml
created: '2026-05-08'
description: Together AI is an AI acceleration cloud delivering fast, scalable, and reliable generative-AI infrastructure. The Together API serves open-source and proprietary foundation models for chat, embeddings, vision, audio, image and video generation, fine-tuning, code execution, and dedicated GPU compute.
finops:
- name: Together Ai Finops
  service_category: AI and Machine Learning
  slug: together-ai-finops
graphqls:
- description: This directory contains a conceptual GraphQL schema for the Together AI platform — an AI acceleration cloud that provides fast, scalable, and reliable generative-AI infrastructure. The Together API se
  name: Together AI GraphQL Schema
  slug: together-ai-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/together-ai.png
layout: provider
modified: '2026-05-29'
name: Together AI
nav: Providers
network: true
overview: 'Together AI publishes 28 APIs on the [APIs.io](https://apis.io/) network, including Audio API, Batches API, Chat API, and 25 more. Tagged areas include AI, LLM, Inference, Foundation Models, and GPU.


  The Together AI catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Together AI''s developer surface includes authentication, documentation, engineering blog, and 10 more developer resources.'
plans:
- name: Together Ai Plans Pricing
  plan_count: 6
  slug: together-ai-plans-pricing
random_paper: 69
rate_limits:
- limit_count: 5
  name: Together Ai Rate Limits
  slug: together-ai-rate-limits
rules:
- name: Together AI API Rules
  rule_count: 9
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 8
  slug: together-ai-asyncapi-spectral-rules
score:
  band: developing
  composite: 45.8
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 67.7
    developer_ergonomics: 21.7
    discoverability: 68.5
    governance: 41.7
    operational_transparency: 36.8
  previous_composite: 45.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 28
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/together-ai/refs/heads/main/screenshots/together-ai-2026-06-20T195434.png
security:
- kind: authentication
  name: Together Ai Authentication
  slug: together-ai-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Together Ai Domain Security
  slug: together-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Together Ai Vulnerability Disclosure
  slug: together-ai-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: together-ai
tags:
- AI
- LLM
- Inference
- Foundation Models
- GPU
- Open Source AI
website: https://www.together.ai/
---
