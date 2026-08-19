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
  band_gated_from: agent-native
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
    mcp_server: documented
    openapi_examples: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 50.0
  scored_at: '2026-08-19'
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
artifact_total: 9
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Relace Code API
  slug: open-relace-code-api
- collection_type: open
  name: Relace Code Repo API
  slug: open-relace-repo-api
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
  url: openapi/_original/relace-openapi-original.json
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
random_paper: 24
score:
  band: developing
  composite: 45.9
  delta: -4.7
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 30.3
    contract_quality: 51.0
    developer_ergonomics: 68.5
    discoverability: 75.9
    governance: 30.3
    operational_transparency: 2.6
  previous_composite: 50.6
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: first-party
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/relace/refs/heads/main/screenshots/relace-2026-08-17T081505.png
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
