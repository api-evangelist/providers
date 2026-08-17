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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 44.8
  scored_at: '2026-08-17'
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
- description: List the available Mercury chat models, then send a chat completion.
  name: Inception — discover a chat model and generate a completion
  slug: inception-labs-chat-completion.arazzo
- description: Confirm a FIM model then generate an inline code completion with Mercury Edit 2.
  name: Inception — fill-in-the-middle code autocomplete
  slug: inception-labs-code-autocomplete.arazzo
artifact_total: 15
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Inception Chat API
  slug: open-inception-labs-chat-api
- collection_type: open
  name: Inception Chat Edit API
  slug: open-inception-labs-edit-api
- collection_type: open
  name: Inception Chat FIM API
  slug: open-inception-labs-fim-api
- collection_type: open
  name: Inception Chat Models API
  slug: open-inception-labs-models-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/inception-labs-openapi-overlay.yaml
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


  Inception Labs'' developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, signup flow, support, and 21 more developer resources.'
random_paper: 91
score:
  band: developing
  composite: 48.1
  delta: 0.0
  facets:
    commercial_clarity: 44.7
    contract_quality: 65.7
    developer_ergonomics: 62.5
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 5.3
  previous_composite: 48.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
    skills: derived
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/inception-labs/refs/heads/main/screenshots/inception-labs-2026-07-25T222329.png
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
