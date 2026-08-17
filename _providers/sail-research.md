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
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: true
    idempotency: documented
    mcp_server: true
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 60.1
  scored_at: '2026-08-17'
api_count: 5
apis:
- description: Submit and manage batches of requests.
  name: Sail Research Batches API API
  slug: sail-research-batches-api-api
- description: OpenAI-compatible Chat Completions API endpoints.
  name: Sail Research Chat Completions API API
  slug: sail-research-chat-completions-api-api
- description: Anthropic-compatible Messages API endpoints.
  name: Sail Research Messages API API
  slug: sail-research-messages-api-api
- description: Model discovery endpoints.
  name: Sail Research Models API API
  slug: sail-research-models-api-api
- description: OpenAI-compatible Responses API endpoints.
  name: Sail Research Responses API API
  slug: sail-research-responses-api-api
artifact_total: 15
asyncapis:
- description: ''
  name: Sail Research Webhooks
  slug: sail-research-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Sail Batches API API
  slug: open-sail-research-batches-api-api
- collection_type: open
  name: Sail Batches API Chat Completions API API
  slug: open-sail-research-chat-completions-api-api
- collection_type: open
  name: Sail Batches API Messages API API
  slug: open-sail-research-messages-api-api
- collection_type: open
  name: Sail Batches API Models API API
  slug: open-sail-research-models-api-api
- collection_type: open
  name: Sail Batches API Responses API API
  slug: open-sail-research-responses-api-api
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.sailresearch.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.sailresearch.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.sailresearch.com/api-reference/chat-completions-api/create-a-chat-completion
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.sailresearch.com/quickstart
- group: commercial
  title: ''
  type: Pricing
  url: https://docs.sailresearch.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.sailresearch.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.sailresearch.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.sailresearch.com/privacy
- group: company
  title: ''
  type: Blog
  url: https://www.sailresearch.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/sailresearch
- group: operate
  title: ''
  type: StatusPage
  url: https://status.sailresearch.com
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.sailresearch.com
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/sail-research-openapi-original.json
- group: auth
  title: ''
  type: Authentication
  url: authentication/sail-research-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sail-research-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/sail-research-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/sail-research-mcp.yml
- group: build
  title: ''
  type: Packages
  url: packages/sail-research-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/sail-research-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/sail-research-cli.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/sail-research-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/sail-research-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/sail-research-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/sail-research-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/sail-research-conformance.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/sail-research-webhooks.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/sail-research-data-model.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/sail-research-openapi-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: 'Sail Research provides infrastructure for long-horizon agents: cost-efficient inference for leading open-source models (GLM, DeepSeek, Kimi, Nemotron and others) run on demand. Its API is OpenAI- and Anthropic-compatible (Chat Completions, Responses, Messages, Batches), so existing clients migrate by changing the base URL and key. Completion windows (asap/priority/standard/flex) trade latency for lower per-token price for background and agentic workloads, and Sailboxes provide full persistent VMs for long-running agents. Sail raised $80M and is backed by Kleiner Perkins. This profile was enriched by the API Evangelist pipeline from Sail''s public OpenAPI, docs, SDKs, CLI, and MCP surface.'
image: https://www.sailresearch.com/og-image.png
layout: provider
mcp_servers:
- description: ''
  name: sail-research-mcp.yml
  slug: sail-research-mcpyml
modified: '2026-07-21'
name: Sail Research
nav: Providers
network: true
overview: 'Sail Research publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Batches API API, Chat Completions API API, Messages API API, and 2 more. Tagged areas include Company, Artificial Intelligence, LLM, Inference, and Agents.


  The Sail Research catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Sail Research''s developer surface includes documentation, API reference, getting-started guide, pricing, signup flow, engineering blog, authentication, and 22 more developer resources.'
random_paper: 123
score:
  band: developing
  composite: 55.2
  delta: 0.0
  facets:
    commercial_clarity: 52.6
    contract_quality: 68.5
    developer_ergonomics: 71.2
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 28.9
  previous_composite: 55.2
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: first-party
    skills: derived
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
security:
- kind: authentication
  name: Sail Research Authentication
  slug: sail-research-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Sail Research Domain Security
  slug: sail-research-domain-security
  summary_line: TLSv1.2 · DMARC
slug: sail-research
tags:
- Company
- Artificial Intelligence
- LLM
- Inference
- Agents
- Machine Learning
- Developer Tools
website: https://docs.sailresearch.com
---
