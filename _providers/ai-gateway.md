---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 20.3
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 32
  human_in_the_loop: 0
  name: Ai Gateway Agentic Access
  operation_count: 60
  slug: ai-gateway-agentic-access
  summary_line: 60 operations · 32 acting
api_count: 1
apis:
- description: Portkey is a production-grade AI gateway and control plane that fronts 1,600+ LLMs with unified routing, fallbacks, semantic caching, guardrails, cost attribution, and prompt management. The open-sour
  name: Portkey
  slug: portkey
- description: OpenRouter is a unified inference marketplace exposing 400+ models from 60+ providers behind one OpenAI-compatible API, with automatic provider fallback, pay-as-you-go credits, custom data policies, a
  name: OpenRouter
  slug: openrouter
- description: LiteLLM (BerriAI) is an open-source LLM gateway that exposes 100+ LLM providers — OpenAI, Anthropic, Azure, Bedrock, Gemini — through a single OpenAI-compatible API. The LiteLLM Proxy adds virtual key
  name: LiteLLM
  slug: litellm
- description: Helicone is an open-source AI observability and routing platform centered on requests, sessions, prompts, datasets, rate limits, and alerts. Integrates with OpenAI, Anthropic, Google Gemini, DeepSeek,
  name: Helicone
  slug: helicone
- description: Cloudflare AI Gateway is an edge-deployed proxy that fronts AI providers — Workers AI, Anthropic, Google Gemini, OpenAI, Replicate, and more — with caching, rate limiting, analytics, and request loggi
  name: Cloudflare AI Gateway
  slug: cloudflare-ai-gateway
- description: The Kong AI Gateway is delivered as the AI Proxy plugin for Kong Gateway, transforming and proxying requests across 16+ providers including OpenAI, Azure OpenAI, Anthropic, Amazon Bedrock, Gemini, Ver
  name: Kong AI Gateway
  slug: kong-ai-gateway
- description: The Apache APISIX ai-proxy plugin streamlines integration with LLMs by converting plugin settings into the appropriate request format for OpenAI, DeepSeek, Azure OpenAI, Anthropic, Google Gemini, Vert
  name: Apache APISIX AI Proxy
  slug: apisix-ai-proxy
- description: Tetrate Agent Router Service is an Envoy AI Gateway-as-a-service from the creators of Envoy, providing an approved LLM catalog, unified model access, automatic fallback, cost management, AI guardrails
  name: Tetrate Agent Router Service
  slug: tetrate-agent-router
- description: NVIDIA NIM is a set of inference microservices for streamlined AI model deployment, prebuilt and optimized for low-latency, high-throughput inference on NVIDIA-accelerated infrastructure. Includes Ten
  name: NVIDIA NIM
  slug: nvidia-nim
- description: 'Traefik AI Gateway is an enterprise, self-hosted, Kubernetes-native AI gateway with safety and governance (NVIDIA Safety NIMs, jailbreak detection, content filtering across 22+ categories), multi-LLM '
  name: Traefik AI Gateway
  slug: traefik-ai-gateway
- description: 'Together AI is a full-stack AI Native Cloud for inference, fine-tuning, and GPU clusters powered by research, exposing serverless inference, batch processing, dedicated model and container inference, '
  name: Together AI
  slug: together-ai
- description: Anyscale is the production-scale AI platform built on Ray by the creators of Ray, supporting LLM inference and other data-intensive AI workloads across distributed GPU clusters. Integrates with vLLM a
  name: Anyscale
  slug: anyscale
- description: LangDB is an enterprise AI gateway for routing and governing LLM traffic across providers, with observability, cost tracking, and policy enforcement. Public homepage was unreachable for direct verific
  name: LangDB
  slug: langdb
- description: Envoy AI Gateway is an open-source extension to Envoy Proxy and Envoy Gateway, providing a Kubernetes-native AI traffic plane for routing, governing, and observing LLM calls across providers. Apache 2
  name: Envoy AI Gateway
  slug: envoy-ai-gateway
- description: Gentrace was an AI evaluation and observability product; the company has shut down and its codebase is now MIT-licensed open source on GitHub. Included here for historical completeness in the AI gatew
  name: Gentrace
  slug: gentrace
- baseURL: https://api.portkey.ai
  baseurl_source: declared
  description: The Analytics API from AI Gateway — 2 operation(s) for analytics.
  name: AI Gateway Analytics API
  slug: ai-gateway-analytics-api
- baseURL: https://api.portkey.ai
  baseurl_source: declared
  description: The APIKeys API from AI Gateway — 1 operation(s) for apikeys.
  name: AI Gateway APIKeys API
  slug: ai-gateway-apikeys-api
- baseURL: https://api.portkey.ai
  baseurl_source: declared
  description: The Assistants API from AI Gateway — 1 operation(s) for assistants.
  name: AI Gateway Assistants API
  slug: ai-gateway-assistants-api
- baseURL: https://api.portkey.ai
  baseurl_source: declared
  description: The Audio API from AI Gateway — 3 operation(s) for audio.
  name: AI Gateway Audio API
  slug: ai-gateway-audio-api
- baseURL: https://api.portkey.ai
  baseurl_source: declared
  description: The Batches API from AI Gateway — 2 operation(s) for batches.
  name: AI Gateway Batches API
  slug: ai-gateway-batches-api
- baseURL: https://api.portkey.ai
  baseurl_source: declared
  description: The Chat API from AI Gateway — 1 operation(s) for chat.
  name: AI Gateway Chat API
  slug: ai-gateway-chat-api
- baseURL: https://api.portkey.ai
  baseurl_source: declared
  description: The Completions API from AI Gateway — 1 operation(s) for completions.
  name: AI Gateway Completions API
  slug: ai-gateway-completions-api
- baseURL: https://api.portkey.ai
  baseurl_source: declared
  description: The Configs API from AI Gateway — 1 operation(s) for configs.
  name: AI Gateway Configs API
  slug: ai-gateway-configs-api
- baseURL: https://api.portkey.ai
  baseurl_source: declared
  description: The Embeddings API from AI Gateway — 2 operation(s) for embeddings.
  name: AI Gateway Embeddings API
  slug: ai-gateway-embeddings-api
- baseURL: https://api.portkey.ai
  baseurl_source: declared
  description: The Feedback API from AI Gateway — 1 operation(s) for feedback.
  name: AI Gateway Feedback API
  slug: ai-gateway-feedback-api
- baseURL: https://api.portkey.ai
  baseurl_source: declared
  description: The Files API from AI Gateway — 2 operation(s) for files.
  name: AI Gateway Files API
  slug: ai-gateway-files-api
- baseURL: https://api.portkey.ai
  baseurl_source: declared
  description: The FineTuning API from AI Gateway — 2 operation(s) for finetuning.
  name: AI Gateway FineTuning API
  slug: ai-gateway-finetuning-api
- baseURL: https://api.portkey.ai
  baseurl_source: declared
  description: The Guardrails API from AI Gateway — 1 operation(s) for guardrails.
  name: AI Gateway Guardrails API
  slug: ai-gateway-guardrails-api
- baseURL: https://api.portkey.ai
  baseurl_source: declared
  description: The Images API from AI Gateway — 1 operation(s) for images.
  name: AI Gateway Images API
  slug: ai-gateway-images-api
- baseURL: https://api.portkey.ai
  baseurl_source: declared
  description: The Integrations API from AI Gateway — 2 operation(s) for integrations.
  name: AI Gateway Integrations API
  slug: ai-gateway-integrations-api
- baseURL: https://api.portkey.ai
  baseurl_source: declared
  description: The Logs API from AI Gateway — 2 operation(s) for logs.
  name: AI Gateway Logs API
  slug: ai-gateway-logs-api
- baseURL: https://api.portkey.ai
  baseurl_source: declared
  description: The MCP API from AI Gateway — 2 operation(s) for mcp.
  name: AI Gateway MCP API
  slug: ai-gateway-mcp-api
- baseURL: https://api.portkey.ai
  baseurl_source: declared
  description: The Policies API from AI Gateway — 2 operation(s) for policies.
  name: AI Gateway Policies API
  slug: ai-gateway-policies-api
- baseURL: https://api.portkey.ai
  baseurl_source: declared
  description: The Prompts API from AI Gateway — 6 operation(s) for prompts.
  name: AI Gateway Prompts API
  slug: ai-gateway-prompts-api
- baseURL: https://api.portkey.ai
  baseurl_source: declared
  description: The Responses API from AI Gateway — 1 operation(s) for responses.
  name: AI Gateway Responses API
  slug: ai-gateway-responses-api
- baseURL: https://api.portkey.ai
  baseurl_source: declared
  description: The Threads API from AI Gateway — 3 operation(s) for threads.
  name: AI Gateway Threads API
  slug: ai-gateway-threads-api
- baseURL: https://api.portkey.ai
  baseurl_source: declared
  description: The VirtualKeys API from AI Gateway — 1 operation(s) for virtualkeys.
  name: AI Gateway VirtualKeys API
  slug: ai-gateway-virtualkeys-api
- baseURL: https://api.portkey.ai
  baseurl_source: declared
  description: The Workspaces API from AI Gateway — 4 operation(s) for workspaces.
  name: AI Gateway Workspaces API
  slug: ai-gateway-workspaces-api
artifact_total: 108
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Portkey AI Gateway Analytics API
  slug: open-ai-gateway-analytics-api
- collection_type: open
  name: Portkey AI Gateway Analytics APIKeys API
  slug: open-ai-gateway-apikeys-api
- collection_type: open
  name: Portkey AI Gateway Analytics Assistants API
  slug: open-ai-gateway-assistants-api
- collection_type: open
  name: Portkey AI Gateway Analytics Audio API
  slug: open-ai-gateway-audio-api
- collection_type: open
  name: Portkey AI Gateway Analytics Batches API
  slug: open-ai-gateway-batches-api
- collection_type: open
  name: Portkey AI Gateway Analytics Chat API
  slug: open-ai-gateway-chat-api
- collection_type: open
  name: Portkey AI Gateway Analytics Completions API
  slug: open-ai-gateway-completions-api
- collection_type: open
  name: Portkey AI Gateway Analytics Configs API
  slug: open-ai-gateway-configs-api
- collection_type: open
  name: Portkey AI Gateway Analytics Embeddings API
  slug: open-ai-gateway-embeddings-api
- collection_type: open
  name: Portkey AI Gateway Analytics Feedback API
  slug: open-ai-gateway-feedback-api
- collection_type: open
  name: Portkey AI Gateway Analytics Files API
  slug: open-ai-gateway-files-api
- collection_type: open
  name: Portkey AI Gateway Analytics FineTuning API
  slug: open-ai-gateway-finetuning-api
- collection_type: open
  name: Portkey AI Gateway Analytics Guardrails API
  slug: open-ai-gateway-guardrails-api
- collection_type: open
  name: Portkey AI Gateway Analytics Images API
  slug: open-ai-gateway-images-api
- collection_type: open
  name: Portkey AI Gateway Analytics Integrations API
  slug: open-ai-gateway-integrations-api
- collection_type: open
  name: Portkey AI Gateway Analytics Logs API
  slug: open-ai-gateway-logs-api
- collection_type: open
  name: Portkey AI Gateway Analytics MCP API
  slug: open-ai-gateway-mcp-api
- collection_type: open
  name: Portkey AI Gateway Analytics Policies API
  slug: open-ai-gateway-policies-api
- collection_type: open
  name: Portkey AI Gateway Analytics Prompts API
  slug: open-ai-gateway-prompts-api
- collection_type: open
  name: Portkey AI Gateway Analytics Responses API
  slug: open-ai-gateway-responses-api
- collection_type: open
  name: Portkey AI Gateway Analytics Threads API
  slug: open-ai-gateway-threads-api
- collection_type: open
  name: Portkey AI Gateway Analytics VirtualKeys API
  slug: open-ai-gateway-virtualkeys-api
- collection_type: open
  name: Portkey AI Gateway Analytics Workspaces API
  slug: open-ai-gateway-workspaces-api
- collection_type: open
  name: Portkey AI Gateway API
  slug: open-ai-gateway
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/Portkey-AI/gateway/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/Portkey-AI/gateway/releases
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/Portkey-AI/gateway/blob/main/.github/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/Portkey-AI/gateway/blob/main/.github/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/Portkey-AI/gateway/blob/main/.github/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/Portkey-AI/gateway/blob/main/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/ai-gateway-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ai-gateway-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ai-gateway-authentication.yml
- group: docs
  title: AI Gateway Route Schema
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/ai-gateway/refs/heads/main/json-schema/ai-gateway-route-schema.json
- group: docs
  title: AI Gateway Provider Schema
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/ai-gateway/refs/heads/main/json-schema/ai-gateway-provider-schema.json
- group: docs
  title: AI Gateway Policy Schema
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/ai-gateway/refs/heads/main/json-schema/ai-gateway-policy-schema.json
- group: design
  title: AI Gateway Route Structure
  type: JSONStructure
  url: https://raw.githubusercontent.com/api-evangelist/ai-gateway/refs/heads/main/json-structure/ai-gateway-route-structure.json
- group: design
  title: AI Gateway Provider Structure
  type: JSONStructure
  url: https://raw.githubusercontent.com/api-evangelist/ai-gateway/refs/heads/main/json-structure/ai-gateway-provider-structure.json
- group: design
  title: AI Gateway Policy Structure
  type: JSONStructure
  url: https://raw.githubusercontent.com/api-evangelist/ai-gateway/refs/heads/main/json-structure/ai-gateway-policy-structure.json
- group: design
  title: ''
  type: JSONLD
  url: https://raw.githubusercontent.com/api-evangelist/ai-gateway/refs/heads/main/json-ld/ai-gateway-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/ai-gateway/refs/heads/main/vocabulary/ai-gateway-vocabulary.yml
- group: build
  title: ''
  type: Examples
  url: https://raw.githubusercontent.com/api-evangelist/ai-gateway/refs/heads/main/examples/
- group: start
  title: ''
  type: Portal
  url: https://github.com/api-evangelist/ai-gateway
- group: company
  title: ''
  type: Blog
  url: https://apievangelist.com/category/ai-gateway/
created: '2026-05-22'
description: An API Evangelist landscape index of AI gateways — the LLM routers, prompt firewalls, model fallback proxies, cost-control planes, and policy engines that sit between applications and AI providers. AI gateways unify access across OpenAI, Anthropic, Google, AWS Bedrock, Azure OpenAI, and self-hosted models behind a common interface and apply caching, routing, guardrails, observability, rate limiting, budgets, RBAC, and audit controls. This index catalogs commercial SaaS gateways, open-source projects, API gateway AI plugins, and cloud-provider AI proxies, with a shared schema and vocabulary for describing model routes, fallbacks, guardrails, and budgets across vendors.
examples:
- key_count: 9
  name: Ai Gateway Cost Route Example
  slug: ai-gateway-cost-route-example
- key_count: 9
  name: Ai Gateway Fanout Route Example
  slug: ai-gateway-fanout-route-example
- key_count: 7
  name: Ai Gateway Policy Budget Example
  slug: ai-gateway-policy-budget-example
- key_count: 7
  name: Ai Gateway Policy Pii Example
  slug: ai-gateway-policy-pii-example
- key_count: 10
  name: Ai Gateway Provider Example
  slug: ai-gateway-provider-example
- key_count: 12
  name: Ai Gateway Route Example
  slug: ai-gateway-route-example
features:
- description: A unified, typically OpenAI-compatible API surface that lets clients call any supported LLM provider without provider-specific SDK juggling.
  name: Provider Abstraction
- description: Route requests to the right model and provider based on alias, header, request content, identity, time-of-day, cost, or latency.
  name: Model Routing
- description: Automatically retry failed requests against backup providers or models when a primary upstream is degraded, rate-limited, or down.
  name: Fallback and Failover
- description: Distribute traffic across multiple providers or replicas using weighted, priority-based, or RPM/TPM-aware load balancing.
  name: Load Balancing and Fanout
- description: Exact-match and semantic caching of model responses to cut latency and provider spend; some gateways claim 40-70 percent cost savings.
  name: Response Caching
- description: Per-user, per-team, per-key, per-project budgets, spend tracking, and hard or soft caps on token consumption.
  name: Cost Controls and Budgets
- description: RPM, TPM, concurrency, and per-key quotas enforced at the gateway, decoupled from each upstream provider's limits.
  name: Rate Limiting and Quotas
- description: Prompt injection detection, jailbreak filtering, content moderation, PII redaction, and topic control applied to requests and responses.
  name: Guardrails and Prompt Firewall
- description: Request, response, token, cost, latency, error, and trace data exported via OpenTelemetry, Langfuse, Phoenix, Langsmith, or built-in dashboards.
  name: Observability
- description: Virtual keys, JWT, OAuth2, SSO, and role-based access control over which clients can use which models with which budgets.
  name: Authentication and RBAC
- description: Bring-your-own provider API keys, with the gateway holding and injecting them so clients never see upstream credentials.
  name: BYOK and Secret Management
- description: Per-tenant isolation of keys, budgets, logs, and policies for platform teams serving multiple internal product teams.
  name: Multi-Tenant Governance
- description: Some AI gateways also front Model Context Protocol servers, aggregating tools and exposing a single MCP endpoint to agents.
  name: MCP Federation
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ai-gateway.png
integrations:
- description: Front OpenAI's GPT, embeddings, and image models behind the gateway with virtual keys and budgets.
  name: OpenAI
- description: Route Claude requests through the gateway for fallback, caching, and central observability.
  name: Anthropic
- description: Proxy Google Gemini and Vertex AI calls with OpenAI-format translation where supported.
  name: Google Gemini and Vertex AI
- description: Bridge OpenAI-format clients to Bedrock-hosted Anthropic, Mistral, Cohere, Meta, and Amazon models.
  name: AWS Bedrock
- description: Route to Azure-hosted OpenAI deployments with per-region failover and key rotation.
  name: Azure OpenAI
- description: Front self-hosted Ollama and vLLM inference servers for hybrid cloud and on-prem inference.
  name: Ollama and vLLM
- description: Export request, token, cost, and trace data to any OTel-compatible observability backend.
  name: OpenTelemetry
- description: Stream prompts, completions, and evaluations to Langfuse and Arize Phoenix for prompt and model analytics.
  name: Langfuse and Phoenix
- description: Some AI gateways federate MCP servers alongside LLM routes, exposing a unified agent endpoint.
  name: Model Context Protocol
json_schemas:
- name: AIGatewayPolicy
  property_count: 12
  slug: ai-gateway-policy
- name: AIGatewayProvider
  property_count: 10
  slug: ai-gateway-provider
- name: AIGatewayRoute
  property_count: 12
  slug: ai-gateway-route
json_structures:
- name: Ai Gateway Policy Structure
  property_count: 12
  slug: ai-gateway-policy-structure
- name: Ai Gateway Provider Structure
  property_count: 9
  slug: ai-gateway-provider-structure
- name: Ai Gateway Route Structure
  property_count: 10
  slug: ai-gateway-route-structure
jsonld:
- class_count: 9
  name: Ai Gateway Context
  property_count: 70
  slug: ai-gateway-context
layout: provider
modified: '2026-05-22'
name: AI Gateway
nav: Providers
network: true
overview: 'AI Gateway publishes 23 APIs on the [APIs.io](https://apis.io/) network, including Analytics API, APIKeys API, Assistants API, and 20 more. Tagged areas include AI Gateway, LLM Router, LLM Proxy, Model Routing, and Prompt Firewall.


  The AI Gateway catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  AI Gateway''s developer surface includes authentication, code examples, developer portal, engineering blog, and 16 more developer resources.'
random_paper: 14
rules:
- effective_rule_count: 5
  extends: []
  name: AI Gateway API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: ai-gateway-jsonschema-spectral-rules
score:
  band: thin
  composite: 38.8
  coverage:
    artifact_dirs: 13
    catalog_earned: 51.3
    catalog_earned_first_party: 0.0
    catalog_gap: 63.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 25.0
    contract_quality: 58.5
    developer_ergonomics: 42.9
    discoverability: 59.3
    governance: 25.0
    operational_transparency: 28.9
  open_source:
    applies: true
    score: 65.0
  previous_composite: 38.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 23
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ai-gateway/refs/heads/main/screenshots/ai-gateway-2026-06-20T170650.png
security:
- kind: authentication
  name: Ai Gateway Authentication
  slug: ai-gateway-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Ai Gateway Domain Security
  slug: ai-gateway-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: ai-gateway
tags:
- AI Gateway
- LLM Router
- LLM Proxy
- Model Routing
- Prompt Firewall
- Guardrails
- AI Observability
- Cost Controls
- AI Governance
- API Gateway
use_cases:
- description: Front many LLM providers behind one API so application teams can switch models without changing client code.
  name: Provider-Agnostic LLM Access
- description: Apply caching, routing to cheaper models, and per-team budgets to keep generative-AI spend predictable.
  name: Cost Containment for AI
- description: Survive single-provider outages by automatically failing over to backup models when the primary degrades.
  name: Reliability and Failover
- description: Enforce content, PII, and policy controls in one place for every AI request leaving the organization.
  name: Centralized AI Governance
- description: Attribute cost and latency to teams, projects, and users; expose token-level metrics to FinOps and SRE.
  name: Observability and FinOps
- description: Build internal AI platforms where each product team gets its own virtual keys, budgets, and logs.
  name: Multi-Tenant AI Platforms
---
