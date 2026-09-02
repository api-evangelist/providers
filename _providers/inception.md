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
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 31.5
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Inception Agentic Access
  operation_count: 7
  slug: inception-agentic-access
  summary_line: 7 operations · 3 acting
api_count: 1
apis:
- description: Chat completion endpoints (OpenAI-compatible).
  name: Inception Chat API
  slug: inception-chat-api
- description: Code edit completion endpoints.
  name: Inception Edit API
  slug: inception-edit-api
- description: Fill-in-the-middle code completion endpoints.
  name: Inception FIM API
  slug: inception-fim-api
- description: List available models.
  name: Inception Models API
  slug: inception-models-api
artifact_total: 16
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Inception Chat API
  slug: open-inception-chat-api
- collection_type: open
  name: Inception Chat Edit API
  slug: open-inception-edit-api
- collection_type: open
  name: Inception Chat FIM API
  slug: open-inception-fim-api
- collection_type: open
  name: Inception Chat Models API
  slug: open-inception-models-api
common:
- group: company
  title: ''
  type: Website
  url: https://inceptionlabs.ai
- group: start
  title: ''
  type: DeveloperPortal
  url: https://platform.inceptionlabs.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.inceptionlabs.ai/get-started/get-started
- group: docs
  title: ''
  type: APIReference
  url: https://docs.inceptionlabs.ai/api-reference/chat/create-a-chat-completion
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.inceptionlabs.ai/get-started/get-started
- group: auth
  title: ''
  type: Authentication
  url: authentication/inception-authentication.yml
- group: company
  title: ''
  type: Blog
  url: https://www.inceptionlabs.ai/blog
- group: operate
  title: ''
  type: Support
  url: https://docs.inceptionlabs.ai/support/support
- group: commercial
  title: ''
  type: Pricing
  url: https://docs.inceptionlabs.ai/get-started/models
- group: start
  title: ''
  type: SignUp
  url: https://platform.inceptionlabs.ai/auth/login
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
  type: GitHubOrganization
  url: https://github.com/inception-ai-inc
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/inception-openapi-original.json
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/inception-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/inception-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/inception-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/inception-mcp.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/inception-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/inception-plans.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/inception-finops.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/inception-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/inception-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/inception-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/inception-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/inception-data-model.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/inception-openapi-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/inception-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/inception-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/inception-domain-security.yml
created: '2026-07-17'
description: Inception Labs builds diffusion-based large language models (dLLMs) branded Mercury. Unlike autoregressive models that emit tokens one at a time, Mercury generates many tokens in parallel through discrete diffusion, running 5-10x faster at roughly half the cost of comparable frontier models. The Inception API is OpenAI-compatible and exposes chat completions (Mercury 2, a reasoning dLLM with a 128K context, tool calling, and structured outputs), plus fill-in-the-middle and next-edit code completions (Mercury Edit 2) for IDE-style autocomplete. It ships official Python and TypeScript SDKs, a streaming/diffusion mode, and enterprise deployment via the Inception API, AWS Bedrock, and Azure AI Foundry. Backed by Amplify Partners.
finops:
- name: Inception Finops
  service_category: ''
  slug: inception-finops
image: https://www.inceptionlabs.ai/logo.png
layout: provider
mcp_servers:
- description: ''
  name: Inception MCP Server
  slug: inception-mcp-server
modified: '2026-07-19'
name: Inception
nav: Providers
network: true
overview: 'Inception publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Chat API, Edit API, FIM API, and 1 more. Tagged areas include Company, Ai Ml, LLM, Artificial Intelligence, and Diffusion Models.


  Inception''s developer surface includes documentation, API reference, getting-started guide, authentication, engineering blog, support, pricing, and 24 more developer resources.'
plans:
- name: Inception Plans
  plan_count: 3
  slug: inception-plans
random_paper: 3
rate_limits:
- limit_count: 0
  name: Inception Rate Limits
  slug: inception-rate-limits
score:
  band: developing
  composite: 51.2
  coverage:
    artifact_dirs: 19
    catalog_gap: 63.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 77.6
    commercial_clarity: 77.6
    contract_governance: 4.5
    contract_quality: 61.9
    developer_ergonomics: 58.9
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 2.6
  previous_composite: 51.2
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
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/inception/refs/heads/main/screenshots/inception-2026-07-25T222332.png
security:
- kind: authentication
  name: Inception Authentication
  slug: inception-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Inception Domain Security
  slug: inception-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: inception
tags:
- Company
- Ai Ml
- LLM
- Artificial Intelligence
- Diffusion Models
- Code Completion
- Machine-Learning
- Developer Tools
website: https://inceptionlabs.ai
---
