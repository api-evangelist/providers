---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_skills: true
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 65.4
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Inception Labs Agentic Access
  operation_count: 7
  slug: inception-labs-agentic-access
  summary_line: 7 operations · 3 acting
api_count: 4
apis:
- description: Chat completion endpoints (OpenAI-compatible).
  name: Inception Labs Chat API
  slug: inception-labs-chat-api
- description: Code edit completion endpoints.
  name: Inception Labs Edit API
  slug: inception-labs-edit-api
- description: Fill-in-the-middle code completion endpoints.
  name: Inception Labs FIM API
  slug: inception-labs-fim-api
- description: List available models.
  name: Inception Labs Models API
  slug: inception-labs-models-api
arazzos:
- description: ''
  name: _Index
  slug: _index
- description: List the available Mercury chat models, then send a chat completion.
  name: Inception — discover a chat model and generate a completion
  slug: inception-labs-chat-completion.arazzo
- description: Confirm a FIM model then generate an inline code completion with Mercury Edit 2.
  name: Inception — fill-in-the-middle code autocomplete
  slug: inception-labs-code-autocomplete.arazzo
artifact_total: 11
common:
- group: company
  title: ''
  type: Website
  url: https://inceptionlabs.ai
- group: start
  title: ''
  type: DeveloperPortal
  url: https://platform.inceptionlabs.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.inceptionlabs.ai
- group: docs
  title: ''
  type: APIReference
  url: https://docs.inceptionlabs.ai/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.inceptionlabs.ai/get-started/get-started
- group: company
  title: ''
  type: Blog
  url: https://www.inceptionlabs.ai/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/inception-ai-inc
- group: commercial
  title: ''
  type: Pricing
  url: https://www.inceptionlabs.ai/models
- group: start
  title: ''
  type: SignUp
  url: https://platform.inceptionlabs.ai
- group: operate
  title: ''
  type: Support
  url: https://docs.inceptionlabs.ai/support/support
- group: commercial
  title: ''
  type: TermsOfService
  url: https://docs.inceptionlabs.ai/support/tou
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://docs.inceptionlabs.ai/support/privacy
- group: build
  title: ''
  type: SDKs
  url: packages/inception-labs-packages.yml
- group: build
  title: ''
  type: Packages
  url: packages/inception-labs-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/inception-labs-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/inception-labs-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/inception-labs-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/inception-labs-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/inception-labs-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/inception-labs-conformance.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/inception-labs-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/inception-labs-llms.txt
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/inception-labs-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/inception-labs-domain-security.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/inception-labs-chat-completion.arazzo.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/inception-labs-code-autocomplete.arazzo.yml
created: '2026-07-17'
description: Inception Labs builds Mercury, the first family of commercial-scale diffusion large language models (dLLMs) that generate tokens in parallel for 5-10x faster inference than comparable speed-optimized models. The Inception API is an OpenAI-compatible REST interface exposing Mercury 2 (a 128K-context reasoning dLLM) and Mercury Edit 2 (a coding-focused model) through chat, fill-in-the-middle, and code-edit completion endpoints, with server-sent-event streaming, tool calling, structured JSON-schema outputs, and an "instant" low-latency reasoning mode for realtime voice. Founded in 2024 by Stanford professor Stefano Ermon, the company is backed by Mayfield and ships official Python and TypeScript client libraries plus AWS Bedrock and Azure Foundry enterprise deployment.
image: https://docs.inceptionlabs.ai/logo.png
layout: provider
mcp_servers:
- description: ''
  name: inception-labs-mcp.yml
  slug: inception-labs-mcpyml
modified: '2026-07-19'
name: Inception Labs
nav: Providers
network: true
overview: 'Inception Labs publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Chat API, Edit API, FIM API, and 1 more. Tagged areas include Artificial Intelligence, Machine Learning, Large Language Models, Diffusion Models, and Generative AI.


  Inception Labs'' developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, signup flow, support, and 20 more developer resources.'
random_paper: 4
score:
  band: developing
  composite: 50.3
  delta: 0.0
  facets:
    commercial_clarity: 44.7
    contract_quality: 63.7
    developer_ergonomics: 73.9
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 50.3
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Inception Labs Authentication
  slug: inception-labs-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Inception Labs Domain Security
  slug: inception-labs-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: inception-labs
tags:
- Artificial Intelligence
- Machine Learning
- Large Language Models
- Diffusion Models
- Generative AI
- Code Completion
- LLM API
- OpenAI Compatible
- Developer Tools
- Company
website: https://inceptionlabs.ai
---
