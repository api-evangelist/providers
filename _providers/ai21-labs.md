---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: true
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: derived
    idempotency: false
    mcp_server: verified
    mcp_tool_quality: full
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 32.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Ai21 Labs Agentic Access
  operation_count: 5
  slug: ai21-labs-agentic-access
  summary_line: 5 operations · 3 acting
api_count: 1
apis:
- description: Conversational completions endpoint backed by the Jamba family of hybrid Mamba/Transformer models (Jamba 1.5 Mini, Jamba 1.5 Large, Jamba 1.6). Accepts a message array, system prompts, temperature, ma
  name: AI21 Jamba Chat Completions API
  slug: chat-completions
- description: Dynamic planning system that, at inference time, determines the optimal sequence of actions to solve a task. Exposes run creation and retrieval endpoints, supports validated output for strict instruct
  name: AI21 Maestro API
  slug: maestro
- description: Managed file storage for RAG workflows. Upload, list, retrieve, update, and delete documents that Maestro and Jamba endpoints can ground on at inference time.
  name: AI21 File Library API
  slug: library
- description: Asynchronous batch processing for large volumes of Jamba completions. Submit a batch job, poll for status, and download results when the run completes.
  name: AI21 Batch API
  slug: batch
- description: Fine-tuning service for Jamba models supporting full, LoRA, and QLoRA strategies. Create training jobs from uploaded datasets and deploy the resulting model variants behind the standard chat completio
  name: AI21 Fine-Tuning API
  slug: fine-tuning
- description: Official Python SDK (ai21 on PyPI) wrapping the AI21 Studio REST API with sync and async clients, streaming support, LangChain / LlamaIndex integrations, and helpers for chat, Maestro, library, and ba
  name: AI21 Python SDK
  slug: python-sdk
- description: Official TypeScript and JavaScript client for the AI21 Studio API, with typed request and response models and streaming helpers for browser and Node.js runtimes.
  name: AI21 TypeScript / JavaScript SDK
  slug: typescript-sdk
- description: Open-weight releases of the Jamba family on Hugging Face for self-hosted inference via vLLM, Transformers, and other runtimes.
  name: AI21 Jamba on Hugging Face
  slug: huggingface
- baseURL: https://api.ai21.com/studio/v1
  baseurl_source: declared
  description: The Library API from AI21 Labs — 1 operation(s) for library.
  name: AI21 Labs Library API
  slug: ai21-labs-library-api
- baseURL: https://api.ai21.com/studio/v1
  baseurl_source: declared
  description: The Maestro API from AI21 Labs — 2 operation(s) for maestro.
  name: AI21 Labs Maestro API
  slug: ai21-labs-maestro-api
- baseURL: https://api.ai21.com/studio/v1
  baseurl_source: declared
  description: The Chat Completions API from AI21 Labs — 1 operation(s) for chat completions.
  name: AI21 Labs Chat Completions API
  slug: ai21-labs-chat-completions-api
artifact_total: 24
asyncapis:
- description: AsyncAPI description of AI21 Labs' documented streaming surface. The AI21 Studio Jamba chat completions endpoint streams partial responses over HTTP using Server-Sent Events (SSE) when the `stream` re
  name: AI21 Studio Streaming API
  slug: ai21-labs-asyncapi
collections:
- collection_type: open
  name: AI21 Studio Chat API
  slug: open-ai21-labs-chat-api
- collection_type: open
  name: AI21 Studio Chat Library API
  slug: open-ai21-labs-library-api
- collection_type: open
  name: AI21 Studio Chat Maestro API
  slug: open-ai21-labs-maestro-api
- collection_type: open
  name: AI21 Studio API
  slug: open-ai21-labs
common:
- group: operate
  href: https://artifacts.apis.io/ai21-labs/rate-limits/ai21-labs-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/ai21-labs-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/ai21-labs/finops/ai21-labs-finops.yml
  title: ''
  type: FinOps
  url: finops/ai21-labs-finops.yml
- group: commercial
  href: https://artifacts.apis.io/ai21-labs/plans/ai21-labs-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/ai21-labs-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/ai21-labs/capabilities/ai21-labs-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/ai21-labs-capability-edges.yml
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/AI21Labs/ai21-python/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/AI21Labs/ai21-python/releases
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/AI21Labs/ai21-python/blob/main/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/AI21Labs/ai21-python/blob/main/LICENSE
- group: agent
  href: https://artifacts.apis.io/ai21-labs/agentic-access/ai21-labs-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/ai21-labs-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/ai21-labs/security/ai21-labs-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ai21-labs-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/ai21-labs/authentication/ai21-labs-authentication.yml
  title: ''
  type: Authentication
  url: authentication/ai21-labs-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.ai21.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ai21.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.ai21.com/reference
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AI21Labs
- group: other
  title: ''
  type: HuggingFace
  url: https://huggingface.co/ai21labs
- group: company
  title: ''
  type: Blog
  url: https://www.ai21.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.ai21.com/pricing/
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.ai21.com/changelog
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ai21/
- group: other
  title: ''
  type: X
  url: https://x.com/AI21Labs
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.ai21.com/llms.txt
created: '2026-05-23'
description: AI21 Labs is an enterprise foundation-model company best known for the Jamba family of open-weight hybrid Mamba/Transformer models and AI21 Maestro, a dynamic planning system that orchestrates tools, retrieval, and validated output during inference. The platform exposes a Bearer-token REST API at api.ai21.com covering chat completions, conversational RAG over a managed file library, batch processing, fine-tuning, and function calling. Official Python and TypeScript SDKs wrap the API with sync and async clients and integrate natively into LangChain and LlamaIndex. Jamba weights are also published on Hugging Face for self-hosted vLLM deployment.
finops:
- has_sources: true
  method: derived
  name: Ai21 Labs Finops
  primary_unit: 1m input tokens
  service_category: ''
  slug: ai21-labs-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ai21-labs.png
layout: provider
mcp_servers:
- description: Remote MCP server at docs.ai21.com over HTTP.
  name: AI21 Labs MCP Server
  slug: ai21-labs
modified: '2026-05-29'
name: AI21 Labs
nav: Providers
network: true
overview: 'AI21 Labs publishes 11 API contracts indexed on the [APIs.io](https://apis.io/) network, including AI21 Jamba Chat Completions API, Library API, Maestro API, and 8 more. Tagged areas include Artificial Intelligence, Foundation Models, LLM, Jamba, and Mamba.


  The AI21 Labs catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  AI21 Labs'' developer surface includes authentication, documentation, API reference, engineering blog, pricing, changelog, and 16 more developer resources.'
plans:
- name: Ai21 Labs Plans Pricing
  plan_count: 7
  slug: ai21-labs-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 2
  name: Ai21 Labs Rate Limits
  slug: ai21-labs-rate-limits
rules:
- authorship: generated
  effective_rule_count: 35
  extends:
  - spectral:asyncapi
  name: AI21 Labs — asyncapi rules
  rule_count: 8
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 7
  slug: ai21-labs-asyncapi-spectral-rules
score:
  band: developing
  composite: 41.1
  coverage:
    artifact_dirs: 20
    catalog_earned: 57.8
    catalog_earned_first_party: 12.0
    catalog_gap: 57.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 50.0
    contract_governance: 11.4
    contract_quality: 55.7
    developer_ergonomics: 31.0
    discoverability: 75.0
    operational_transparency: 23.7
  open_source:
    applies: true
    score: 50.0
  previous_composite: 41.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: first-party
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 10.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/ai21-labs/ai21-labs-2026-06-20T170826.png
security:
- kind: authentication
  name: Ai21 Labs Authentication
  slug: ai21-labs-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Ai21 Labs Domain Security
  slug: ai21-labs-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ai21-labs
tags:
- Artificial Intelligence
- Foundation Models
- LLM
- Jamba
- Mamba
- RAG
- Agents
- Maestro
- Inference
- Enterprise AI
- Fine-Tuning
website: https://www.ai21.com/
---
