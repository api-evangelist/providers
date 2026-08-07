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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Ngrok Ai Agentic Access
  operation_count: 2
  slug: ngrok-ai-agentic-access
  summary_line: 2 operations · 2 acting
api_count: 3
apis:
- description: 'ngrok AI Gateway exposes an OpenAI-compatible HTTP interface for routing requests across multiple AI providers and self-hosted models. Each AI Gateway instance has a unique base URL of the form https:'
  name: ngrok AI Gateway
  slug: ai-gateway
- description: The Anthropic API from ngrok AI Gateway — 1 operation(s) for anthropic.
  name: ngrok AI Gateway Anthropic API
  slug: ngrok-ai-anthropic-api
- description: The OpenAI API from ngrok AI Gateway — 1 operation(s) for openai.
  name: ngrok AI Gateway OpenAI API
  slug: ngrok-ai-openai-api
artifact_total: 28
collections:
- collection_type: open
  name: ngrok AI Gateway API
  slug: open-ngrok-ai
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/ngrok-ai-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/ngrok-ai-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/ngrok-ai-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ngrok-ai-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ngrok-ai-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ngrok
- group: company
  title: ''
  type: Website
  url: https://ngrok.com/ai-gateway
- group: docs
  title: ''
  type: Documentation
  url: https://ngrok.com/docs/ai-gateway/
- group: start
  title: ''
  type: GettingStarted
  url: https://ngrok.com/docs/ai-gateway/quickstart/
- group: company
  title: ''
  type: Blog
  url: https://ngrok.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://ngrok.com/pricing
- group: operate
  title: ''
  type: Support
  url: https://ngrok.com/support
- group: operate
  title: ''
  type: StatusPage
  url: https://status.ngrok.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ngrok
- group: agent
  title: ''
  type: LlmsText
  url: https://ngrok.com/llms.txt
created: '2026-03-16'
description: ngrok AI Gateway provides traffic management and security for AI APIs including multi-provider routing, automatic failover, LLM prompt inspection, rate limiting, caching, observability, PII redaction, and access control. It enables teams to manage, secure, and monitor traffic to AI model providers (OpenAI, Anthropic, Google, DeepSeek) and self-hosted models such as Ollama and vLLM through an OpenAI-compatible interface.
features:
- description: Direct requests to AI providers including OpenAI, Anthropic, Google, and DeepSeek through a single gateway endpoint.
  name: Multi-Provider Routing
- description: If one provider or model fails, the gateway automatically tries the next configured model.
  name: Automatic Failover
- description: Works with official and third-party OpenAI SDKs by changing only the base URL.
  name: OpenAI SDK Compatibility
- description: Route requests to local systems such as Ollama or vLLM alongside hosted providers.
  name: Self-Hosted Model Support
- description: Use ngrok/auto for intelligent model picking based on configured strategies.
  name: Automatic Model Selection
- description: Define custom routing logic using Common Expression Language expressions.
  name: CEL-Based Selection Strategies
- description: Direct traffic to the cheapest available model option meeting requirements.
  name: Cost-Based Routing
- description: Restrict which providers and models clients can use by API key, identity, or policy.
  name: Access Control
- description: Inspect and modify content to remove personally identifiable information from prompts and responses.
  name: PII Redaction
- description: Modify and filter responses before they reach clients.
  name: Response Sanitization
- description: Access OpenAI and Anthropic models without individual provider signup, using ngrok credits.
  name: No Provider Account Required
finops:
- name: Ngrok Ai Finops
  service_category: API
  slug: ngrok-ai-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ngrok-ai.png
layout: provider
modified: '2026-04-28'
name: ngrok AI Gateway
nav: Providers
network: true
overview: 'ngrok AI Gateway publishes 2 APIs on the [APIs.io](https://apis.io/) network: Anthropic API and OpenAI API. Tagged areas include AI, AI Gateway, API Gateway, LLM, and OpenAI Compatible.


  ngrok AI Gateway''s developer surface includes authentication, documentation, getting-started guide, engineering blog, pricing, support, and 9 more developer resources.'
plans:
- name: Ngrok Ai Plans Pricing
  plan_count: 3
  slug: ngrok-ai-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 5
  name: Ngrok Ai Rate Limits
  slug: ngrok-ai-rate-limits
score:
  band: developing
  composite: 47.0
  delta: 0.0
  facets:
    commercial_clarity: 57.9
    contract_quality: 55.0
    developer_ergonomics: 37.0
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 52.6
  previous_composite: 47.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ngrok-ai/refs/heads/main/screenshots/ngrok-ai-2026-06-20T190315.png
security:
- kind: authentication
  name: Ngrok Ai Authentication
  slug: ngrok-ai-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Ngrok Ai Domain Security
  slug: ngrok-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Ngrok Ai Vulnerability Disclosure
  slug: ngrok-ai-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Ngrok Ai Trust Center
  slug: ngrok-ai-trust-center
  summary_line: SOC 2, HIPAA, GDPR
slug: ngrok-ai
tags:
- AI
- AI Gateway
- API Gateway
- LLM
- OpenAI Compatible
- Routing
- Security
- Traffic Management
use_cases:
- description: Manage all AI provider traffic through a single gateway with unified observability and policy enforcement.
  name: Centralized AI API Management
- description: Route traffic to the most cost-effective model that meets quality requirements.
  name: Cost Optimization
- description: Enforce PII redaction and prompt inspection policies before requests leave the organization.
  name: Compliance and Data Protection
- description: Failover automatically across providers to maintain AI service availability.
  name: Multi-Provider Resilience
- description: Route between hosted providers and self-hosted models such as Ollama or vLLM.
  name: Local and Hybrid Model Routing
website: https://ngrok.com/ai-gateway
---
