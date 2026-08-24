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
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 42.3
  scored_at: '2026-08-24'
api_count: 1
apis:
- description: OpenAI-compatible inference API for open-source, frontier, and custom language models — chat completions, batch/async inference, function calling, structured outputs, and vision — authenticated with a
  name: Inference.net API
  slug: inferencenet-api
artifact_total: 7
asyncapis:
- description: ''
  name: Inference Webhooks
  slug: inference-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/inference-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://inference.net
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.inference.net
- group: docs
  title: ''
  type: Documentation
  url: https://docs.inference.net
- group: docs
  title: ''
  type: APIReference
  url: https://docs.inference.net/api/api-quickstart
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.inference.net/api/api-quickstart
- group: company
  title: ''
  type: Blog
  url: https://inference.net/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://inference.net/pricing
- group: start
  title: ''
  type: SignUp
  url: https://inference.net/register
- group: start
  title: ''
  type: Login
  url: https://inference.net/signin
- group: commercial
  title: ''
  type: TermsOfService
  url: https://inference.net/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://inference.net/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/context-labs
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.inference.net
- group: auth
  title: ''
  type: Authentication
  url: authentication/inference-authentication.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/inference-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/inference-plans.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/inference-mcp.yml
- group: build
  title: ''
  type: CLI
  url: cli/inference-cli.yml
- group: build
  title: ''
  type: Packages
  url: packages/inference-packages.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/inference-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/inference-lifecycle.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/inference-webhooks.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/inference-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/inference-llms.txt
created: '2026-07-17'
description: Inference (inference.net) is an AI infrastructure platform for AI-native teams. It offers an OpenAI-compatible inference API for open-source, frontier, and custom fine-tuned language models, alongside Catalyst — its observability, tracing, evaluation, training, and deployment platform. Developers call chat completions, batch/async inference, function calling, structured outputs, and vision endpoints at https://api.inference.net/v1 using a Bearer API key; route and monitor traffic through the Catalyst Gateway; fine-tune and deploy custom models; and optimize agents end to end with HALO. The platform ships a first-party CLI (inf), a hosted MCP server, and webhooks for asynchronous inference. Backed by Multicoin Capital.
image: https://inference.net/og/home.png
layout: provider
mcp_servers:
- description: 'The Inference MCP server lets compatible AI coding assistants query and operate Catalyst resources (projects, agents, models, datasets, rubrics, evals, training jobs, deployments, inferences, traces, '
  name: Inference MCP Server
  slug: inference-mcp-server
modified: '2026-07-19'
name: Inference
nav: Providers
network: true
overview: 'Inference publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Machine-Learning, LLM, and Inference.


  The Inference catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Inference''s developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, signup flow, authentication, and 18 more developer resources.'
plans:
- name: Inference Plans
  plan_count: 3
  slug: inference-plans
random_paper: 19
rate_limits:
- limit_count: 4
  name: Inference Rate Limits
  slug: inference-rate-limits
score:
  band: strong
  composite: 54.5
  delta: 0.0
  facets:
    access_clarity: 80.3
    commercial_clarity: 80.3
    contract_governance: 18.2
    contract_quality: 45.1
    developer_ergonomics: 59.5
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 42.1
  previous_composite: 54.5
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/inference/refs/heads/main/screenshots/inference-2026-07-25T222358.png
security:
- kind: authentication
  name: Inference Authentication
  slug: inference-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Inference Domain Security
  slug: inference-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: inference
tags:
- Company
- Artificial Intelligence
- Machine-Learning
- LLM
- Inference
- Observability
- Model Training
- Model Deployment
- MCP
- Crypto Web3
website: https://inference.net
---
