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
    agent_skills: true
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 33.7
  scored_at: '2026-07-27'
api_count: 1
apis:
- description: REST control plane that powers all index lifecycle operations for Moss. Every action is multiplexed through a single authenticated POST /v1/manage endpoint (initUpload, startBuild, getJobStatus, getIn
  name: Moss Control Plane API
  slug: moss-control-plane-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/moss-trust-center.yml
- group: company
  title: ''
  type: Website
  url: https://www.moss.dev/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://portal.usemoss.dev
- group: docs
  title: ''
  type: Documentation
  url: https://docs.moss.dev/docs
- group: docs
  title: ''
  type: APIReference
  url: https://docs.moss.dev/docs/api-reference/v1/getting-started/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.moss.dev/docs/start/quickstart
- group: company
  title: ''
  type: Blog
  url: https://www.moss.dev/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/usemoss
- group: operate
  title: ''
  type: Support
  url: https://moss.link/discord
- group: commercial
  title: ''
  type: Pricing
  url: https://www.moss.dev/pricing
- group: start
  title: ''
  type: SignUp
  url: https://portal.usemoss.dev/auth/sign-up
- group: commercial
  title: ''
  type: TermsOfService
  url: https://docs.moss.dev/docs/tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://docs.moss.dev/docs/privacy
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/moss-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/moss-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/moss-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/moss-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/moss-mcp.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/moss-changelog.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/moss-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/moss-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/moss-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/moss-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/moss-data-model.yml
- group: design
  title: ''
  type: Components
  url: components/moss-components.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/moss-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.moss.dev
- group: auth
  title: ''
  type: DomainSecurity
  url: security/moss-domain-security.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Moss is a high-performance runtime for real-time semantic search built for conversational and multimodal AI. It delivers sub-10ms retrieval so voice agents, copilots, and chat interfaces can retrieve, reason, and respond without waiting, running where the agent lives - in the cloud, in the browser, or on-device. Moss Cloud handles ingestion, embedding, index builds, and distribution through the Moss Control Plane API, while the SDKs (JavaScript, Python, Swift, Elixir, C, and Browser/WASM) load indexes and run queries locally with built-in embedding models, hybrid search, and metadata filtering. Moss is a Y Combinator (F25) company. This profile was enriched from Moss's public developer surface (docs.moss.dev, package registries, and GitHub).
image: https://www.moss.dev/og-image.png
layout: provider
mcp_servers:
- description: ''
  name: moss-mcp.yml
  slug: moss-mcpyml
modified: '2026-07-20'
name: Moss
nav: Providers
network: true
overview: 'Moss publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Semantic Search, Vector Search, Retrieval, and AI Agents.


  Moss'' developer surface includes documentation, API reference, getting-started guide, engineering blog, support, pricing, signup flow, and 22 more developer resources.'
random_paper: 42
score:
  band: thin
  composite: 40.2
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 0.0
    developer_ergonomics: 80.4
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 40.2
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
security:
- kind: authentication
  name: Moss Authentication
  slug: moss-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Moss Domain Security
  slug: moss-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Moss Trust Center
  slug: moss-trust-center
  summary_line: SOC 2, HIPAA
slug: moss
tags:
- Company
- Semantic Search
- Vector Search
- Retrieval
- AI Agents
- Voice AI
- Embeddings
- RAG
- Developer Tools
- On-Device AI
website: https://www.moss.dev/
---
