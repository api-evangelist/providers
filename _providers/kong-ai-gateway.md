---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 6.0
  scored_at: '2026-09-01'
api_count: 21
apis:
- description: Kong AI Gateway is the connectivity and governance layer for AI-native applications. Built on Kong Gateway, it provides a universal LLM API across 16+ providers, semantic caching, prompt firewalls and
  name: Kong AI Gateway
  slug: kong-ai-gateway
- description: The AI Proxy plugin transforms and proxies requests to a configured AI provider and model, shielding client applications from provider-specific request and response shapes.
  name: AI Proxy Plugin
  slug: ai-proxy-plugin
- description: The AI Proxy Advanced plugin extends AI Proxy with load balancing, weighted distribution, and fallback across multiple providers and models simultaneously.
  name: AI Proxy Advanced Plugin
  slug: ai-proxy-advanced-plugin
- description: Token-aware rate limiting tailored for LLM traffic, with per-consumer and per-model budgets rather than just request counts.
  name: AI Rate Limiting Advanced Plugin
  slug: ai-rate-limiting-advanced-plugin
- description: Enforces allow- and deny-lists for prompts and text completions, blocking disallowed content before it reaches the model.
  name: AI Prompt Guard Plugin
  slug: ai-prompt-guard-plugin
- description: Topic-aware variant of AI Prompt Guard that classifies prompts by meaning and blocks restricted topics regardless of phrasing.
  name: AI Semantic Prompt Guard Plugin
  slug: ai-semantic-prompt-guard-plugin
- description: Detects and redacts personally identifiable information from prompts and responses traversing the gateway.
  name: AI PII Sanitizer Plugin
  slug: ai-pii-sanitizer-plugin
- description: Caches LLM responses by prompt similarity so semantically equivalent requests can be served from cache, reducing latency and provider spend.
  name: AI Semantic Cache Plugin
  slug: ai-semantic-cache-plugin
- description: Automates retrieval-augmented generation by injecting retrieved context into prompts at the gateway, so application code does not need to implement RAG plumbing.
  name: AI RAG Injector Plugin
  slug: ai-rag-injector-plugin
- description: Provides reusable, fill-in-the-blank prompt templates managed at the gateway layer.
  name: AI Prompt Template Plugin
  slug: ai-prompt-template-plugin
- description: Prepends or appends messages to chat history before requests reach the model.
  name: AI Prompt Decorator Plugin
  slug: ai-prompt-decorator-plugin
- description: Reduces prompt token count before forwarding to the provider to lower latency and cost.
  name: AI Prompt Compressor Plugin
  slug: ai-prompt-compressor-plugin
- description: Integrates Azure AI Content Safety for content moderation on prompts and responses.
  name: AI Azure Content Safety Plugin
  slug: ai-azure-content-safety-plugin
- description: Integrates Amazon Bedrock Guardrails for safety enforcement on traffic passing through Kong AI Gateway.
  name: AI AWS Guardrails Plugin
  slug: ai-aws-guardrails-plugin
- description: Integrates Google Cloud Model Armor for safety inspection on prompts and responses.
  name: AI GCP Model Armor Plugin
  slug: ai-gcp-model-armor-plugin
- description: Integrates Lakera Guard for prompt-injection and jailbreak detection.
  name: AI Lakera Guard Plugin
  slug: ai-lakera-guard-plugin
- description: Inspects model responses by meaning and blocks responses that violate configured semantic policies.
  name: AI Semantic Response Guard Plugin
  slug: ai-semantic-response-guard-plugin
- description: Lets operators define custom guardrail logic for prompts and responses without writing a full Kong plugin.
  name: AI Custom Guardrail Plugin
  slug: ai-custom-guardrail-plugin
- description: Uses LLMs at the gateway to transform request and response payloads (for example, reshaping JSON or translating fields) on the data path.
  name: AI Request/Response Transformer Plugin
  slug: ai-request-response-transformer-plugin
- description: Kong Agent Gateway is a capability of Kong AI Gateway (GA April 2026 with AI Gateway 3.14) that governs agent-to-agent (A2A) communication. It enforces agent identity verification, real-time policy an
  name: Kong Agent Gateway
  slug: kong-agent-gateway
- description: Kong MCP Registry (launched February 2026) is an enterprise directory inside Kong Konnect for registering, discovering, and governing MCP servers and AI-native tools. It provides dynamic discovery for
  name: Kong MCP Registry
  slug: kong-mcp-registry
artifact_total: 46
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/Kong/kong/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/Kong/kong/releases
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/Kong/kong/blob/master/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/Kong/kong/blob/master/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/Kong/kong/blob/master/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/Kong/kong/blob/master/LICENSE
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kong-ai-gateway-domain-security.yml
- group: start
  title: ''
  type: Portal
  url: https://konghq.com/products/kong-ai-gateway
- group: docs
  title: ''
  type: Documentation
  url: https://developer.konghq.com/ai-gateway/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.konghq.com/ai-gateway/get-started/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.konghq.com/ai-gateway/ai-providers/
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.konghq.com/gateway/changelog/
- group: company
  title: ''
  type: Blog
  url: https://konghq.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Kong
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/Kong/kong
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Kong/sdk-konnect-go
- group: build
  title: ''
  type: CLI
  url: https://github.com/Kong/kongctl
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/Kong/mcp-konnect
- group: commercial
  title: ''
  type: Pricing
  url: https://konghq.com/pricing
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/konghq
- group: operate
  title: ''
  type: Support
  url: https://discuss.konghq.com/
- group: agent
  title: ''
  type: LlmsText
  url: https://developer.konghq.com/llms.txt
created: '2026-05-23'
description: Kong AI Gateway is the AI-native capability layer built on top of Kong Gateway and managed through Kong Konnect. It exposes a normalized, provider-agnostic LLM API across 16+ providers (OpenAI, Anthropic, Azure AI, Amazon Bedrock, Google Gemini, Vertex AI, Cohere, Hugging Face, Llama, Mistral, xAI, DashScope, Cerebras, Ollama, Databricks, DeepSeek, vLLM), and adds prompt firewalls, PII sanitization, semantic caching, automated RAG injection, token-level observability, per-agent cost allocation, MCP traffic governance, and Agent Gateway support for agent-to-agent (A2A) communication. It is profiled here as a standalone product surface; the parent provider profile lives at github.com/api-evangelist/kong.
features:
- description: One normalized request shape across 16+ providers (OpenAI, Anthropic, Azure AI, Bedrock, Gemini, Vertex AI, Cohere, Hugging Face, Llama, Mistral, xAI, DashScope, Cerebras, Ollama, Databricks, DeepSeek, vLLM).
  name: Universal LLM API
- description: AI Prompt Guard, AI Semantic Prompt Guard, and AI PII Sanitizer block disallowed content and redact sensitive data before it hits the model.
  name: Prompt Firewalls and PII Sanitization
- description: AI Semantic Cache serves semantically similar prompts from cache to cut latency and provider spend.
  name: Semantic Caching
- description: AI Rate Limiting Advanced enforces per-consumer and per-model token budgets, not just request counts.
  name: Token-Aware Rate Limiting
- description: AI RAG Injector pulls retrieved context into prompts at the gateway so application code stays simple.
  name: Automated RAG Injection
- description: AI Proxy Advanced distributes traffic across providers with weighted distribution and fallback.
  name: Multi-Provider Load Balancing
- description: Built-in integrations with Azure Content Safety, AWS Bedrock Guardrails, GCP Model Armor, and Lakera Guard.
  name: Content Safety Integrations
- description: Kong MCP Registry registers and governs MCP servers and tools that AI agents discover and call through the gateway.
  name: MCP Traffic Governance
- description: Kong Agent Gateway (GA April 2026 with AI Gateway 3.14) governs A2A traffic with identity, policy, and observability.
  name: Agent-to-Agent Governance
- description: Per-request, per-agent, and per-model token and cost telemetry surfaced into Konnect dashboards.
  name: Token-Level Observability
finops:
- name: Kong Ai Gateway Finops
  service_category: API
  slug: kong-ai-gateway-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/kong-ai-gateway.png
integrations:
- description: Native provider integrations exposed through the AI Proxy plugin's normalized API.
  name: OpenAI, Anthropic, Azure AI, Bedrock, Gemini, Vertex AI
- description: Additional native provider targets for AI Proxy and AI Proxy Advanced.
  name: Cohere, Hugging Face, Llama, Mistral, xAI, DashScope, Cerebras, Ollama, Databricks, DeepSeek, vLLM
- description: Prompt-injection and jailbreak detection as a guardrail plugin.
  name: Lakera Guard
- description: Cloud-native content safety integrations available as Kong AI plugins.
  name: Azure AI Content Safety / AWS Bedrock Guardrails / GCP Model Armor
- description: Standard Kong Gateway observability stack carries LLM, MCP, and A2A telemetry.
  name: Prometheus, Grafana, OpenTelemetry
layout: provider
mcp_servers:
- description: ''
  name: Kong Konnect MCP Server
  slug: kong-konnect-mcp-server
modified: '2026-05-23'
name: Kong AI Gateway
nav: Providers
network: true
overview: 'Kong AI Gateway publishes 21 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include AI Gateway, LLM, MCP, A2A, and AI Governance.


  Kong AI Gateway''s developer surface includes developer portal, documentation, getting-started guide, API reference, changelog, engineering blog, CLI, and 15 more developer resources.'
plans:
- name: Kong Ai Gateway Plans Pricing
  plan_count: 1
  slug: kong-ai-gateway-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 2
  name: Kong Ai Gateway Rate Limits
  slug: kong-ai-gateway-rate-limits
score:
  band: developing
  composite: 40.2
  coverage:
    artifact_dirs: 7
    catalog_gap: 61.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 59.5
    discoverability: 72.2
    governance: 0.0
    operational_transparency: 50.0
  open_source:
    applies: true
    score: 100.0
  previous_composite: 40.2
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kong-ai-gateway/refs/heads/main/screenshots/kong-ai-gateway-2026-06-20T184133.png
security:
- kind: domain-security
  name: Kong Ai Gateway Domain Security
  slug: kong-ai-gateway-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: kong-ai-gateway
tags:
- AI Gateway
- LLM
- MCP
- A2A
- AI Governance
- Konnect
- Kong
use_cases:
- description: Give applications a stable LLM endpoint while swapping providers and models behind the gateway.
  name: Provider-Agnostic LLM Access
- description: Apply token budgets, semantic caching, and prompt compression to keep LLM spend bounded.
  name: AI Cost Control
- description: Enforce prompt firewalls, PII redaction, jailbreak detection, and content safety on every prompt and response.
  name: AI Safety and Compliance
- description: Govern which MCP tools agents can discover and call, and inspect agent-to-agent traffic in production.
  name: Agentic Tool Governance
- description: Inject retrieval context into prompts at the gateway without changing client code.
  name: RAG at the Edge
website: https://konghq.com/products/kong-ai-gateway
---
