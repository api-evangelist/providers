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
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: true
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 38.1
  scored_at: '2026-07-28'
api_count: 2
apis:
- description: Answer operations
  name: Seltz answer API
  slug: seltz-answer-api
- description: Search operations
  name: Seltz search API
  slug: seltz-search-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/seltz-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://console.seltz.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.seltz.ai
- group: docs
  title: ''
  type: APIReference
  url: https://docs.seltz.ai/api-reference/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.seltz.ai/quickstart
- group: start
  title: ''
  type: Sandbox
  url: https://console.seltz.ai/playground
- group: commercial
  title: ''
  type: Pricing
  url: https://seltz.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://console.seltz.ai
- group: commercial
  title: ''
  type: TermsOfService
  url: https://seltz.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://seltz.ai/privacy-policy
- group: company
  title: ''
  type: Blog
  url: https://seltz.ai/blog
- group: operate
  title: ''
  type: Support
  url: https://seltz.ai/contact
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/seltz-ai
- group: build
  title: ''
  type: Packages
  url: packages/seltz-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/seltz-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/seltz-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/seltz-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/seltz-well-known.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/seltz-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.seltz.ai/
- group: auth
  title: ''
  type: TrustCenter
  url: security/seltz-trust-center.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/seltz-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/seltz-changelog.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: 'Seltz is a San Francisco-based AI infrastructure company building the web retrieval and knowledge layer for the agentic internet. Its Web Knowledge API gives LLMs, RAG pipelines, and autonomous agents real-time, context-engineered web data through a single call: POST /v1/search returns ranked, cleaned source documents, POST /v1/answer returns a direct RAG answer with citations, and an OpenAI-compatible /v1/chat/completions endpoint serves web-grounded chat. Rather than returning raw snippets like a traditional search API, Seltz shapes web content to maximize usefulness for machine reasoning. Founded in 2025 by Antonio Mallia (Amazon, Pinecone) and backed by Speedinvest and B Capital, Seltz ships official Python and TypeScript SDKs, a hosted MCP server, and integrations for OpenAI, Anthropic, Mistral, LlamaIndex, Agno, Langroid, Dify, n8n, and Zapier.'
image: https://seltz.ai/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: seltz-mcp.yml
  slug: seltz-mcpyml
modified: '2026-07-21'
name: Seltz
nav: Providers
network: true
overview: 'Seltz publishes 2 APIs on the [APIs.io](https://apis.io/) network: answer API and search API. Tagged areas include Company, Web Search, AI Infrastructure, Retrieval, and RAG.


  Seltz''s developer surface includes documentation, API reference, getting-started guide, sandbox, pricing, signup flow, engineering blog, and 17 more developer resources.'
random_paper: 9
score:
  band: developing
  composite: 51.4
  delta: 0.3
  facets:
    commercial_clarity: 60.5
    contract_quality: 54.2
    developer_ergonomics: 64.7
    discoverability: 87.0
    governance: 11.5
    operational_transparency: 21.1
  previous_composite: 51.1
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: first-party
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Seltz Authentication
  slug: seltz-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Seltz Domain Security
  slug: seltz-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Seltz Trust Center
  slug: seltz-trust-center
  summary_line: trust center published
slug: seltz
tags:
- Company
- Web Search
- AI Infrastructure
- Retrieval
- RAG
- Agents
- LLM
- Knowledge API
- Developer Tools
- MCP
website: https://console.seltz.ai
---
