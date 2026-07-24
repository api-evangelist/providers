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
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 33
  human_in_the_loop: 0
  name: Unify Ai Agentic Access
  operation_count: 48
  slug: unify-ai-agentic-access
  summary_line: 48 operations · 33 acting
api_count: 8
apis:
- description: Send messages to and retrieve messages from assistants
  name: Unify Agent API
  slug: unify-ai-agent-api
- description: Create and manage AI assistants within your workspace
  name: Unify Assistants API
  slug: unify-ai-assistants-api
- description: Named sub-collections of logs within a project
  name: Unify Contexts API
  slug: unify-ai-contexts-api
- description: Structured logging — create, query, derive, and manage log entries
  name: Unify Logs API
  slug: unify-ai-logs-api
- description: Multi-user organization management
  name: Unify Organizations API
  slug: unify-ai-organizations-api
- description: Platform-level utilities including credits and user info
  name: Unify Platform API
  slug: unify-ai-platform-api
- description: Create and manage projects for organizing logs and contexts
  name: Unify Projects API
  slug: unify-ai-projects-api
- description: Collaboration spaces for grouping assistants
  name: Unify Spaces API
  slug: unify-ai-spaces-api
artifact_total: 22
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/unify-ai-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/unify-ai-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/unify-ai-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/unify-ai-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/unify-ai-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://unify.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.unify.ai
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/unifyai
- group: company
  title: ''
  type: LinkedIn
  url: https://uk.linkedin.com/company/letsunifyai
- group: company
  title: ''
  type: Blog
  url: https://unify.ai/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://unify.ai/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://statusgator.com/services/unify
- group: other
  title: ''
  type: X
  url: https://x.com/letsunifyai
- group: commercial
  title: ''
  type: Plans
  url: plans/unify-ai-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/unify-ai-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/unify-ai-finops.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/unify-ai-vocabulary.yml
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/unify-ai-context.jsonld
created: '2026-06-12'
description: Unify is an LLM routing and model gateway platform that enables developers to access 100+ large language model providers through a single unified REST API and API key. The platform dynamically routes each prompt to the optimal model based on user-defined preferences across quality, speed, and cost dimensions, using live runtime benchmarks updated continuously across providers including OpenAI, Anthropic, Mistral, Together AI, Replicate, Groq, DeepSeek, and many more. Unify provides an observability dashboard for comparing model and provider performance, automatic fallback routing, and caching capabilities to reduce redundant API calls. Developers can benchmark models on their own prompts using standardized datasets and switch providers without rewriting application code using the unified model@provider endpoint syntax.
examples:
- key_count: 4
  name: Unify Ai Create Log Example
  slug: unify-ai-create-log-example
- key_count: 4
  name: Unify Ai Send Message Example
  slug: unify-ai-send-message-example
finops:
- name: Unify Ai Finops
  service_category: ''
  slug: unify-ai-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/unify-ai.png
json_schemas:
- name: Unify Assistant
  property_count: 4
  slug: unify-ai-assistant
- name: Unify Log Entry
  property_count: 5
  slug: unify-ai-log
jsonld:
- class_count: 12
  name: Unify Ai Context
  property_count: 20
  slug: unify-ai-context
layout: provider
modified: '2026-06-12'
name: Unify
nav: Providers
network: true
overview: 'Unify publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Agent API, Assistants API, Contexts API, and 5 more. Tagged areas include LLM, AI, Large Language Models, LLM Routing, and Model Gateway.


  The Unify catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Unify''s developer surface includes authentication, documentation, engineering blog, pricing, and 14 more developer resources.'
plans:
- name: Unify Ai Plans Pricing
  plan_count: 3
  slug: unify-ai-plans-pricing
random_paper: 37
rate_limits:
- limit_count: 5
  name: Unify Ai Rate Limits
  slug: unify-ai-rate-limits
rules:
- name: Unify API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: unify-ai-jsonschema-spectral-rules
score:
  band: strong
  composite: 61.7
  delta: 0.0
  facets:
    commercial_clarity: 57.9
    contract_quality: 74.3
    developer_ergonomics: 21.7
    discoverability: 100.0
    governance: 86.8
    operational_transparency: 52.6
  previous_composite: 61.7
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/unify-ai/refs/heads/main/screenshots/unify-ai-2026-06-20T200030.png
security:
- kind: authentication
  name: Unify Ai Authentication
  slug: unify-ai-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Unify Ai Domain Security
  slug: unify-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Unify Ai Vulnerability Disclosure
  slug: unify-ai-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Unify Ai Trust Center
  slug: unify-ai-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: unify-ai
tags:
- LLM
- AI
- Large Language Models
- LLM Routing
- Model Gateway
- AI Gateway
- OpenAI
- Anthropic
- Mistral
- Benchmarking
- Model Comparison
- AI Infrastructure
- Machine Learning
website: https://unify.ai
---
