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
    event_surface_described: derived
    idempotency: false
    mcp_server: true
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 54.7
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Osmosis Agentic Access
  operation_count: 5
  slug: osmosis-agentic-access
  summary_line: 5 operations · 3 acting
api_count: 3
apis:
- description: Operations for enhancing agent interactions and decisions
  name: Osmosis agent API
  slug: osmosis-agent-api
- description: Operations for managing the knowledge base
  name: Osmosis knowledge API
  slug: osmosis-knowledge-api
- description: The Osmosis Agent Improvement API API from Osmosis — 1 operation(s) for osmosis agent improvement api.
  name: Osmosis Osmosis Agent Improvement API API
  slug: osmosis-osmosis-agent-improvement-api-api
artifact_total: 8
asyncapis:
- description: ''
  name: Osmosis Webhooks
  slug: osmosis-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://osmosis.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.osmosis.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.osmosis.ai
- group: docs
  title: ''
  type: APIReference
  url: https://docs.osmosis.ai/openapi.json
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.osmosis.ai/platform/quickstart
- group: company
  title: ''
  type: Blog
  url: https://osmosis.ai/blog
- group: operate
  title: ''
  type: Support
  url: https://osmosis.ai/contact
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Osmosis-AI
- group: start
  title: ''
  type: SignUp
  url: https://platform.osmosis.ai
- group: commercial
  title: ''
  type: TermsOfService
  url: https://osmosis.ai/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://osmosis.ai/legal/privacy
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.osmosis.ai
- group: build
  title: ''
  type: Packages
  url: packages/osmosis-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/osmosis-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/osmosis-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/osmosis-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/osmosis-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/osmosis-well-known.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/osmosis-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/osmosis-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/osmosis-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/osmosis-changelog.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/osmosis-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/osmosis-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/osmosis-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/osmosis-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/osmosis-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/osmosis-authentication.yml
created: '2026-07-17'
description: Osmosis (Gulp AI Inc.) is a forward-deployed reinforcement-learning platform for post-training large language models. Teams implement an AgentWorkflow and a Grader in Python, then use the Osmosis CLI and web platform to submit evaluation and training runs (GRPO/DAPO, multi-turn tool training) that produce task-specific LoRA models which beat foundation models at a fraction of the cost. Osmosis also ships an Agent Improvement REST API for storing agent interaction knowledge and enhancing agent tasks from past interactions, an open-source Python SDK/CLI (osmosis-ai), a TypeScript logging SDK, an open-source MCP server (Osmosis-Apply), webhooks, and hosted documentation. Backed by CRV, Felicis, and Paradigm.
image: https://raw.githubusercontent.com/Osmosis-AI/osmosis-sdk-python/main/.github/osmosis-logo-light.svg
layout: provider
mcp_servers:
- description: ''
  name: osmosis-mcp.yml
  slug: osmosis-mcpyml
modified: '2026-07-20'
name: Osmosis
nav: Providers
network: true
overview: 'Osmosis publishes 3 APIs on the [APIs.io](https://apis.io/) network: agent API, knowledge API, and Osmosis Agent Improvement API API. Tagged areas include Company, AI, Reinforcement Learning, LLM, and Post-Training.


  The Osmosis catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Osmosis'' developer surface includes documentation, API reference, getting-started guide, engineering blog, support, signup flow, CLI, and 22 more developer resources.'
random_paper: 21
score:
  band: developing
  composite: 54.3
  delta: 0.0
  facets:
    commercial_clarity: 42.1
    contract_quality: 65.5
    developer_ergonomics: 75.5
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 28.9
  previous_composite: 54.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: first-party
    skills: derived
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
security:
- kind: authentication
  name: Osmosis Authentication
  slug: osmosis-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Osmosis Domain Security
  slug: osmosis-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: osmosis
tags:
- Company
- AI
- Reinforcement Learning
- LLM
- Post-Training
- Model Training
- Agents
- Machine Learning
- Developer Tools
website: https://osmosis.ai/
---
