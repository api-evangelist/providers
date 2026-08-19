---
access_model:
  confidence: high
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: true
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 47.0
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Bifrost Agentic Access
  operation_count: 3
  slug: bifrost-agentic-access
  summary_line: 3 operations · 2 acting
api_count: 4
apis:
- description: The Bifrost Go SDK provides a native Go client for embedding the Bifrost AI gateway directly into Go applications using the github.com/maximhq/bifrost/core package.
  name: Bifrost Go SDK
  slug: bifrost-go-sdk
- description: The Bifrost Model Context Protocol (MCP) Gateway enables AI agents to discover and execute external tools through a standardized protocol, with OAuth 2.0 authentication and tool approval controls.
  name: Bifrost MCP Gateway
  slug: bifrost-mcp-gateway
- description: Chat completions compatible with OpenAI chat API
  name: Bifrost Chat API
  slug: bifrost-chat-api
- description: Gateway health and status endpoints
  name: Bifrost Health API
  slug: bifrost-health-api
artifact_total: 57
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Bifrost HTTP Gateway Chat API
  slug: open-bifrost-chat-api
- collection_type: open
  name: Bifrost HTTP Gateway Chat Health API
  slug: open-bifrost-health-api
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/maximhq/bifrost/issues
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/maximhq/bifrost/blob/dev/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/maximhq/bifrost/blob/dev/CODE_OF_CONDUCT.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/maximhq/bifrost/blob/dev/LICENSE
- group: company
  title: ''
  type: Blog
  url: https://www.getmaxim.ai/blog
- group: design
  title: ''
  type: Webhooks
  url: https://docs.getbifrost.ai/features/webhooks
- group: build
  title: ''
  type: CLI
  url: https://docs.getbifrost.ai/quickstart/cli/getting-started
- group: build
  title: ''
  type: SDKs
  url: https://www.getmaxim.ai/docs/sdk/overview
- group: operate
  title: ''
  type: StatusPage
  url: https://status.getmaxim.ai/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.getmaxim.ai/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.getmaxim.ai/terms-of-service
- group: commercial
  title: ''
  type: Pricing
  url: https://www.getmaxim.ai/pricing
- group: start
  title: ''
  type: Signup
  url: https://app.getmaxim.ai/sign-up
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/bifrost-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/bifrost-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bifrost-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/bifrost-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://www.getmaxim.ai/bifrost/enterprise
- group: docs
  title: ''
  type: Documentation
  url: https://docs.getbifrost.ai
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.getbifrost.ai/quickstart/gateway/setting-up
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/maximhq/bifrost
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/maximhq
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/maximhq/bifrost/releases
- group: operate
  title: ''
  type: Community
  url: https://discord.gg/exN5KAydbU
- group: design
  title: ''
  type: SpectralRules
  url: https://raw.githubusercontent.com/api-evangelist/bifrost/refs/heads/main/rules/bifrost-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/bifrost/refs/heads/main/vocabulary/bifrost-vocabulary.yaml
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.getbifrost.ai/llms.txt
created: '2026-03-16'
description: Bifrost is a high-performance open-source AI gateway that unifies access to 20+ AI providers through a single OpenAI-compatible API. It supports 1,000+ models with adaptive load balancing, automatic failover, semantic caching, and enterprise observability features. Bifrost is open-source under Apache 2.0.
examples:
- key_count: 3
  name: Bifrost Chat Choice Example
  slug: bifrost-chat-choice-example
- key_count: 7
  name: Bifrost Chat Completion Request Example
  slug: bifrost-chat-completion-request-example
- key_count: 6
  name: Bifrost Chat Completion Response Example
  slug: bifrost-chat-completion-response-example
- key_count: 2
  name: Bifrost Chat Message Example
  slug: bifrost-chat-message-example
- key_count: 3
  name: Bifrost Health Response Example
  slug: bifrost-health-response-example
- key_count: 2
  name: Bifrost Provider Status Example
  slug: bifrost-provider-status-example
- key_count: 3
  name: Bifrost Usage Stats Example
  slug: bifrost-usage-stats-example
features:
- description: Single API interface compatible with OpenAI SDK for all 20+ providers.
  name: OpenAI-Compatible API
- description: Distribute requests across providers and models based on availability and performance.
  name: Adaptive Load Balancing
- description: Automatically retry failed requests on alternative providers without client changes.
  name: Automatic Failover
- description: Cache semantically similar prompts to reduce latency and API costs.
  name: Semantic Caching
- description: Model Context Protocol gateway for AI agent tool discovery and execution.
  name: MCP Gateway
- description: Native Go library for embedding Bifrost gateway directly into applications.
  name: Go SDK
- description: Built-in metrics, tracing, and logging for production AI gateway deployments.
  name: Enterprise Observability
- description: Centralized API key management for all connected AI providers.
  name: Provider Key Management
finops:
- name: Bifrost Finops
  service_category: AI Infrastructure / Gateway
  slug: bifrost-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bifrost.png
integrations:
- description: Route to OpenAI GPT-4o, GPT-4, and other OpenAI models.
  name: OpenAI
- description: Route to Claude 3.5 Sonnet, Claude 3 Opus, and other Anthropic models.
  name: Anthropic
- description: Route to Cohere Command and other Cohere models.
  name: Cohere
- description: Route to models hosted on AWS Bedrock including Titan and Claude.
  name: AWS Bedrock
- description: Route to Azure-hosted OpenAI deployments.
  name: Azure OpenAI
- description: Route to Gemini and other models on Google Vertex AI.
  name: Google Vertex AI
json_schemas:
- name: ChatChoice
  property_count: 3
  slug: bifrost-chat-choice
- name: ChatCompletionRequest
  property_count: 7
  slug: bifrost-chat-completion-request
- name: ChatCompletionResponse
  property_count: 6
  slug: bifrost-chat-completion-response
- name: ChatMessage
  property_count: 2
  slug: bifrost-chat-message
- name: HealthResponse
  property_count: 3
  slug: bifrost-health-response
- name: ProviderStatus
  property_count: 2
  slug: bifrost-provider-status
- name: UsageStats
  property_count: 3
  slug: bifrost-usage-stats
json_structures:
- name: Bifrost Chat Choice Structure
  property_count: 3
  slug: bifrost-chat-choice-structure
- name: Bifrost Chat Completion Request Structure
  property_count: 7
  slug: bifrost-chat-completion-request-structure
- name: Bifrost Chat Completion Response Structure
  property_count: 6
  slug: bifrost-chat-completion-response-structure
- name: Bifrost Chat Message Structure
  property_count: 2
  slug: bifrost-chat-message-structure
- name: Bifrost Health Response Structure
  property_count: 3
  slug: bifrost-health-response-structure
- name: Bifrost Provider Status Structure
  property_count: 2
  slug: bifrost-provider-status-structure
- name: Bifrost Usage Stats Structure
  property_count: 3
  slug: bifrost-usage-stats-structure
jsonld:
- class_count: 8
  name: Bifrost Context
  property_count: 16
  slug: bifrost-context
layout: provider
modified: '2026-05-19'
name: Bifrost
nav: Providers
network: true
overview: 'Bifrost publishes 2 APIs on the [APIs.io](https://apis.io/) network: Chat API and Health API. Tagged areas include AI Gateway, LLM, Load Balancing, Open Source, and OpenAI Compatible.


  The Bifrost catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Bifrost''s developer surface includes engineering blog, CLI, pricing, signup flow, authentication, developer portal, documentation, and 20 more developer resources.'
plans:
- name: Bifrost Plans Pricing
  plan_count: 2
  slug: bifrost-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 3
  name: Bifrost Rate Limits
  slug: bifrost-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Bifrost API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: bifrost-jsonschema-spectral-rules
- effective_rule_count: 69
  extends:
  - spectral:oas
  name: Bifrost API Rules
  rule_count: 28
  severity_counts:
    error: 7
    hint: 0
    info: 0
    warn: 21
  slug: bifrost-spectral-rules
score:
  band: developing
  composite: 46.8
  delta: -7.3
  facets:
    access_clarity: 65.8
    commercial_clarity: 65.8
    contract_governance: 25.0
    contract_quality: 21.0
    developer_ergonomics: 61.9
    discoverability: 72.2
    governance: 25.0
    operational_transparency: 44.7
  previous_composite: 54.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 2
      marker_coverage: 100.0
      total: 2
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/bifrost/refs/heads/main/screenshots/bifrost-2026-06-20T173231.png
security:
- kind: authentication
  name: Bifrost Authentication
  slug: bifrost-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Bifrost Domain Security
  slug: bifrost-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Bifrost Trust Center
  slug: bifrost-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, GDPR
slug: bifrost
tags:
- AI Gateway
- LLM
- Load Balancing
- Open Source
- OpenAI Compatible
- MCP
use_cases:
- description: Build applications that can seamlessly switch between OpenAI, Anthropic, and other providers.
  name: Multi-Provider AI Applications
- description: Route requests to cheaper providers during peak costs or use caching to reduce API spend.
  name: Cost Optimization
- description: Ensure AI features remain available by failing over across multiple provider accounts.
  name: High Availability AI
- description: Enable AI agents to discover and execute tools through the MCP gateway protocol.
  name: AI Agent Tooling
- description: A/B test different models and providers without changing application code.
  name: LLM Provider Evaluation
website: https://www.getmaxim.ai/bifrost/enterprise
---
