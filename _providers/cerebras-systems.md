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
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: derived
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 44.8
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Cerebras Systems Agentic Access
  operation_count: 8
  slug: cerebras-systems-agentic-access
  summary_line: 8 operations · 3 acting
api_count: 5
apis:
- description: The Chat API from Cerebras Systems — 1 operation(s) for chat.
  name: Cerebras Systems Chat API
  slug: cerebras-systems-chat-api
- description: The Completions API from Cerebras Systems — 1 operation(s) for completions.
  name: Cerebras Systems Completions API
  slug: cerebras-systems-completions-api
- description: The Models API from Cerebras Systems — 2 operation(s) for models.
  name: Cerebras Systems Models API
  slug: cerebras-systems-models-api
- description: The Public Models API from Cerebras Systems — 2 operation(s) for public models.
  name: Cerebras Systems Public Models API
  slug: cerebras-systems-public-models-api
- description: The Tcp Warming API from Cerebras Systems — 1 operation(s) for tcp warming.
  name: Cerebras Systems Tcp Warming API
  slug: cerebras-systems-tcp-warming-api
artifact_total: 17
collections:
- collection_type: postman
  name: Cerebras Inference Chat API
  slug: postman-cerebras-systems-chat-api
- collection_type: postman
  name: Cerebras Inference Chat Completions API
  slug: postman-cerebras-systems-completions-api
- collection_type: postman
  name: Cerebras Inference Chat Models API
  slug: postman-cerebras-systems-models-api
- collection_type: postman
  name: Cerebras Inference Chat Public Models API
  slug: postman-cerebras-systems-public-models-api
- collection_type: postman
  name: Cerebras Inference Chat Tcp Warming API
  slug: postman-cerebras-systems-tcp-warming-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/cerebras-systems/overview
- group: auth
  title: ''
  type: TrustCenter
  url: security/cerebras-systems-trust-center.yml
- group: company
  title: ''
  type: Website
  url: https://www.cerebras.ai
- group: start
  title: ''
  type: DeveloperPortal
  url: https://inference-docs.cerebras.ai
- group: docs
  title: ''
  type: Documentation
  url: https://inference-docs.cerebras.ai
- group: docs
  title: ''
  type: APIReference
  url: https://inference-docs.cerebras.ai/api-reference/chat-completions
- group: start
  title: ''
  type: GettingStarted
  url: https://inference-docs.cerebras.ai/quickstart
- group: operate
  title: ''
  type: Support
  url: https://inference-docs.cerebras.ai/support/overview
- group: company
  title: ''
  type: Blog
  url: https://www.cerebras.ai/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Cerebras
- group: commercial
  title: ''
  type: Pricing
  url: https://www.cerebras.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://cloud.cerebras.ai
- group: start
  title: ''
  type: Login
  url: https://cloud.cerebras.ai
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cerebras.ai/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cerebras.ai/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cerebras.ai
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.cerebras.ai
- group: auth
  title: ''
  type: Compliance
  url: https://trust.cerebras.ai
- group: auth
  title: ''
  type: Security
  url: https://trust.cerebras.ai
- group: operate
  title: ''
  type: ChangeLog
  url: https://inference-docs.cerebras.ai/support/change-log
- group: operate
  title: ''
  type: Deprecation
  url: https://inference-docs.cerebras.ai/support/deprecation
- group: build
  title: ''
  type: Packages
  url: packages/cerebras-systems-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/cerebras-systems-packages.yml
- group: build
  title: ''
  type: Python SDK
  url: https://github.com/Cerebras/cerebras-cloud-sdk-python
- group: build
  title: ''
  type: Node.js SDK
  url: https://github.com/Cerebras/cerebras-cloud-sdk-node
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cerebras-systems-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/cerebras-systems-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cerebras-systems-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/cerebras-systems-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/cerebras-systems-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/cerebras-systems-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/cerebras-systems-lifecycle.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/cerebras-systems-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/cerebras-systems-plans.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/cerebras-systems-inference-overlay.yaml
- group: design
  title: ''
  type: DataModel
  url: data-model/cerebras-systems-data-model.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cerebras-systems-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cerebras-systems-agentic-access.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/cerebras-systems-changelog.yml
created: '2026-07-17'
description: 'Cerebras Systems builds the Wafer-Scale Engine (WSE) — the largest computer chip ever made — and the CS-3 systems built around it, delivering AI training and inference at speeds far beyond conventional GPUs. Cerebras Inference is the company''s cloud API: an OpenAI-compatible REST interface at api.cerebras.ai that serves open-weight frontier models (OpenAI GPT-OSS, Gemma 4, Z.ai GLM 4.7) at industry-leading tokens-per-second. Developers authenticate with a bearer API key and call chat/completions, completions, and models endpoints, with streaming, tool calling, structured outputs, vision, prompt caching, and batch inference. Custom model weights can be deployed on dedicated endpoints. Official Python and Node.js SDKs, a Cloud Console with a playground, and coding-tool integrations (VS Code, Cline, Kilo Code, OpenCode) round out the developer surface.'
image: https://github.com/Cerebras.png
layout: provider
mcp_servers:
- description: ''
  name: cerebras-systems-mcp.yml
  slug: cerebras-systems-mcpyml
modified: '2026-07-18'
name: Cerebras Systems
nav: Providers
network: true
overview: 'Cerebras Systems publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Chat API, Completions API, Models API, and 2 more. Tagged areas include Company, Ai Infrastructure, Artificial Intelligence, Machine Learning, and Inference.


  Cerebras Systems'' developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 33 more developer resources.'
plans:
- name: Cerebras Systems Plans
  plan_count: 3
  slug: cerebras-systems-plans
random_paper: 76
rate_limits:
- limit_count: 0
  name: Cerebras Systems Rate Limits
  slug: cerebras-systems-rate-limits
score:
  band: strong
  composite: 64.9
  delta: -0.8
  facets:
    commercial_clarity: 92.1
    contract_quality: 54.1
    developer_ergonomics: 75.5
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 55.3
  previous_composite: 65.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cerebras-systems/refs/heads/main/screenshots/cerebras-systems-2026-07-25T204949.png
security:
- kind: authentication
  name: Cerebras Systems Authentication
  slug: cerebras-systems-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Cerebras Systems Domain Security
  slug: cerebras-systems-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Cerebras Systems Trust Center
  slug: cerebras-systems-trust-center
  summary_line: SOC 2, GDPR
slug: cerebras-systems
tags:
- Company
- Ai Infrastructure
- Artificial Intelligence
- Machine Learning
- Inference
- Large Language Models
- Developer Tools
- Cloud Computing
- Semiconductors
website: https://www.cerebras.ai
---
