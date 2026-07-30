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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 18.9
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: 'Unified, OpenAI- and Anthropic-compatible LLM gateway providing access to 200+ models from leading providers through a single endpoint. Documented operations: POST /v1/chat/completions (OpenAI-compati'
  name: Martian Gateway API
  slug: martian-gateway-api
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/martian-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://withmartian.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.withmartian.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.withmartian.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.withmartian.com/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.withmartian.com/quickstart
- group: operate
  title: ''
  type: Support
  url: https://docs.withmartian.com/resources/support
- group: company
  title: ''
  type: Blog
  url: https://withmartian.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/withmartian
- group: start
  title: ''
  type: SignUp
  url: https://app.withmartian.com/
- group: start
  title: ''
  type: Login
  url: https://app.withmartian.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.withmartian.com
- group: build
  title: ''
  type: Packages
  url: packages/martian-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/martian-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/martian-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/martian-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/martian-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/martian-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/martian-conformance.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/martian-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/martian-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/martian-llms.txt
created: '2026-07-17'
description: Martian operates the Martian Gateway, a unified LLM API that provides access to 200+ AI models from leading providers (OpenAI, Anthropic, and others) through a single OpenAI- and Anthropic-compatible endpoint. Developers point the standard OpenAI or Anthropic SDK at https://api.withmartian.com/v1, authenticate with a bearer API key, and call models using a provider/model-name identifier, with real-time pricing, a usage dashboard, and model routing across providers. Martian is also an AI interpretability research organization, publishing open-source frameworks such as ARES (Agentic Research and Evaluation Suite), K-Steering, RouterBench, and a model-router / judges SDK.
image: https://withmartian.com/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: martian-mcp.yml
  slug: martian-mcpyml
modified: '2026-07-20'
name: Martian
nav: Providers
network: true
overview: 'Martian publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, LLM, LLM Gateway, and Model Router.


  Martian''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, authentication, and 15 more developer resources.'
random_paper: 10
score:
  band: emerging
  composite: 27.8
  delta: -0.3
  facets:
    commercial_clarity: 13.2
    contract_quality: 0.0
    developer_ergonomics: 60.9
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 21.1
  previous_composite: 28.1
  provenance:
    conformance: first-party
    mcp: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/martian/refs/heads/main/screenshots/martian-2026-07-25T230258.png
security:
- kind: authentication
  name: Martian Authentication
  slug: martian-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Martian Domain Security
  slug: martian-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: martian
tags:
- Company
- Artificial Intelligence
- LLM
- LLM Gateway
- Model Router
- Machine Learning
- Interpretability
- Inference
- OpenAI Compatible
- Developer Tools
website: https://withmartian.com
---
