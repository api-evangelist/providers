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
    openapi_examples: partial
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.1
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Sambanova Agentic Access
  operation_count: 4
  slug: sambanova-agentic-access
  summary_line: 4 operations · 3 acting
api_count: 5
apis:
- description: The SambaCloud API exposes OpenAI-compatible chat completions over SambaNova's RDU-accelerated infrastructure. It serves multiple open model families including DeepSeek V3, Llama 3.3 and Llama 4, Gemm
  name: SambaCloud API
  slug: sambacloud-api
- description: The Chat API from SambaNova — 1 operation(s) for chat.
  name: SambaNova Chat API
  slug: sambanova-chat-api
- description: The Completions API from SambaNova — 1 operation(s) for completions.
  name: SambaNova Completions API
  slug: sambanova-completions-api
- description: The Embeddings API from SambaNova — 1 operation(s) for embeddings.
  name: SambaNova Embeddings API
  slug: sambanova-embeddings-api
- description: The Models API from SambaNova — 1 operation(s) for models.
  name: SambaNova Models API
  slug: sambanova-models-api
artifact_total: 18
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: SambaCloud Chat API
  slug: open-sambanova-chat-api
- collection_type: open
  name: SambaCloud Chat Completions API
  slug: open-sambanova-completions-api
- collection_type: open
  name: SambaCloud Chat Embeddings API
  slug: open-sambanova-embeddings-api
- collection_type: open
  name: SambaCloud Chat Models API
  slug: open-sambanova-models-api
- collection_type: open
  name: SambaCloud API
  slug: open-sambanova
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/sambanova-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/sambanova-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sambanova-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/sambanova-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://sambanova.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.sambanova.ai
- group: start
  title: ''
  type: DeveloperPortal
  url: https://cloud.sambanova.ai
- group: operate
  title: ''
  type: Community
  url: https://community.sambanova.ai
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/sambanova
- group: other
  title: ''
  type: StarterKits
  url: https://github.com/sambanova/ai-starter-kit
- group: other
  title: ''
  type: Hardware
  url: https://sambanova.ai/products/sn50-rdu
- group: company
  title: ''
  type: Blog
  url: https://sambanova.ai/blog
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/sambanova-systems
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/SambaNovaAI
created: '2026-05-23'
description: SambaNova Systems designs the SN-series Reconfigurable Dataflow Unit (RDU) AI chips and operates SambaCloud, a managed inference platform serving open-source models including the DeepSeek, Llama, Gemma, MiniMax, and gpt-oss families. The SambaCloud API is OpenAI-compatible and is consumed through first-party Python and TypeScript SDKs as well as the SambaNova AI Starter Kit collection on GitHub. SambaNova additionally ships SambaStack as an integrated chips-to-model on-prem appliance, SambaManaged managed services, and SambaRack rack-scale systems. The company emphasizes sovereign AI partnerships in Australia, Europe, and the UK and a recently announced heterogeneous inference collaboration with Intel.
finops:
- name: Sambanova Finops
  service_category: API
  slug: sambanova-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sambanova.png
layout: provider
modified: '2026-05-23'
name: SambaNova
nav: Providers
network: true
overview: 'SambaNova publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Chat API, Completions API, Embeddings API, and 1 more. Tagged areas include AI Inference, Large Language Models, Dataflow, Hardware, and Cloud.


  SambaNova''s developer surface includes authentication, documentation, engineering blog, and 11 more developer resources.'
plans:
- name: Sambanova Plans Pricing
  plan_count: 1
  slug: sambanova-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 2
  name: Sambanova Rate Limits
  slug: sambanova-rate-limits
score:
  band: developing
  composite: 39.3
  delta: -1.1
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 57.3
    developer_ergonomics: 35.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 23.7
  previous_composite: 40.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sambanova/refs/heads/main/screenshots/sambanova-2026-06-20T193358.png
security:
- kind: authentication
  name: Sambanova Authentication
  slug: sambanova-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Sambanova Domain Security
  slug: sambanova-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Sambanova Trust Center
  slug: sambanova-trust-center
  summary_line: SOC 2, ISO 27001
slug: sambanova
tags:
- AI Inference
- Large Language Models
- Dataflow
- Hardware
- Cloud
- OpenAI Compatible
- Sovereign AI
- SDK
- Accelerator
- Open Source
website: https://sambanova.ai
---
