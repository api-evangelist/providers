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
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 10
  human_in_the_loop: 0
  name: Relace Agentic Access
  operation_count: 11
  slug: relace-agentic-access
  summary_line: 11 operations · 10 acting
api_count: 2
apis:
- description: The Code API from Relace — 5 operation(s) for code.
  name: Relace Code API
  slug: relace-code-api
- description: The Repo API from Relace — 5 operation(s) for repo.
  name: Relace Repo API
  slug: relace-repo-api
artifact_total: 6
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.relace.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.relace.ai/docs/introduction
- group: docs
  title: ''
  type: APIReference
  url: https://docs.relace.ai/api-reference/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.relace.ai/docs/instant-apply/quickstart
- group: start
  title: ''
  type: Quickstart
  url: https://docs.relace.ai/docs/instant-apply/quickstart
- group: start
  title: ''
  type: SignUp
  url: https://app.relace.ai/sign-up
- group: commercial
  title: ''
  type: Pricing
  url: https://relace.ai/pricing
- group: company
  title: ''
  type: Blog
  url: https://relace.ai/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://relace.ai/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://relace.ai/legal/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/squack-io
- group: operate
  title: ''
  type: StatusPage
  url: https://status.relace.ai/
- group: auth
  title: ''
  type: Compliance
  url: https://relace.ai/pricing
- group: auth
  title: ''
  type: Authentication
  url: authentication/relace-authentication.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/relace-openapi-original.json
- group: agent
  title: ''
  type: MCPServer
  url: mcp/relace-mcp.yml
- group: build
  title: ''
  type: Packages
  url: packages/relace-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/relace-packages.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/relace-llms.txt
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/relace-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/relace-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/relace-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/relace-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/relace-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/relace-sandbox.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/relace-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/relace-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/relace-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://relace.ai
created: '2026-07-17'
description: Relace builds purpose-built AI models and infrastructure for coding agents. Its hosted API exposes fast, specialized models — Instant Apply (relace-apply-3) for merging LLM code edits at over 10k tok/s, a Code Reranker (relace-rank) and code embeddings for semantic codebase retrieval, and Compact for compressing agent traces — alongside Relace Repos, a "GitHub for AI agents" source-control layer with built-in two-stage retrieval and Fast Agentic Search. Authentication is a Bearer API key (rlc- prefix); official Python and TypeScript SDKs and an MCP server are published, and enterprise SOC 2, on-premise, and VPC-isolated deployments are offered. Backed by Matrix Partners and Y Combinator.
image: https://framerusercontent.com/images/D6XFBAXygf3ZHyjrXSmLmItnPI.png
layout: provider
mcp_servers:
- description: ''
  name: relace-mcp.yml
  slug: relace-mcpyml
modified: '2026-07-21'
name: Relace
nav: Providers
network: true
overview: 'Relace publishes 2 APIs on the [APIs.io](https://apis.io/) network: Code API and Repo API. Tagged areas include Company, AI, Coding Agents, Code Generation, and Developer Tools.


  Relace''s developer surface includes documentation, API reference, getting-started guide, quickstart, signup flow, pricing, engineering blog, and 23 more developer resources.'
random_paper: 8
score:
  band: developing
  composite: 50.1
  delta: 0.0
  facets:
    commercial_clarity: 52.6
    contract_quality: 49.6
    developer_ergonomics: 76.1
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 50.1
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
security:
- kind: authentication
  name: Relace Authentication
  slug: relace-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Relace Domain Security
  slug: relace-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: relace
tags:
- Company
- AI
- Coding Agents
- Code Generation
- Developer Tools
- Machine Learning
- Code Search
- LLM
website: https://relace.ai
---
