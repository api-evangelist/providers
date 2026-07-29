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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 46.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 38
  human_in_the_loop: 0
  name: Nex Agentic Access
  operation_count: 61
  slug: nex-agentic-access
  summary_line: 61 operations · 38 acting
api_count: 16
apis:
- description: The AI Lists API from Nex — 2 operation(s) for ai lists.
  name: Nex AI Lists API
  slug: nex-ai-lists-api
- description: The Compounding API from Nex — 2 operation(s) for compounding.
  name: Nex Compounding API
  slug: nex-compounding-api
- description: The Context API from Nex — 3 operation(s) for context.
  name: Nex Context API
  slug: nex-context-api
- description: The Graph API from Nex — 1 operation(s) for graph.
  name: Nex Graph API
  slug: nex-graph-api
- description: The Insights API from Nex — 2 operation(s) for insights.
  name: Nex Insights API
  slug: nex-insights-api
- description: The Integrations API from Nex — 4 operation(s) for integrations.
  name: Nex Integrations API
  slug: nex-integrations-api
- description: The Lists API from Nex — 4 operation(s) for lists.
  name: Nex Lists API
  slug: nex-lists-api
- description: The Notes API from Nex — 2 operation(s) for notes.
  name: Nex Notes API
  slug: nex-notes-api
- description: The Notifications API from Nex — 4 operation(s) for notifications.
  name: Nex Notifications API
  slug: nex-notifications-api
- description: The Objects API from Nex — 1 operation(s) for objects.
  name: Nex Objects API
  slug: nex-objects-api
- description: The Records API from Nex — 3 operation(s) for records.
  name: Nex Records API
  slug: nex-records-api
- description: The Relationships API from Nex — 4 operation(s) for relationships.
  name: Nex Relationships API
  slug: nex-relationships-api
- description: The Schema API from Nex — 4 operation(s) for schema.
  name: Nex Schema API
  slug: nex-schema-api
- description: The Search API from Nex — 1 operation(s) for search.
  name: Nex Search API
  slug: nex-search-api
- description: The Tasks API from Nex — 2 operation(s) for tasks.
  name: Nex Tasks API
  slug: nex-tasks-api
- description: The Timeline API from Nex — 1 operation(s) for timeline.
  name: Nex Timeline API
  slug: nex-timeline-api
artifact_total: 21
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.nex.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.nex.ai
- group: docs
  title: ''
  type: APIReference
  url: https://docs.nex.ai/api-reference/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.nex.ai
- group: company
  title: ''
  type: Website
  url: https://nex.ai
- group: company
  title: ''
  type: Blog
  url: https://nex.ai/blog
- group: operate
  title: ''
  type: Support
  url: https://nex.ai/support
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/nex-crm
- group: commercial
  title: ''
  type: Pricing
  url: https://nex.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.nex.ai
- group: commercial
  title: ''
  type: TermsOfService
  url: https://nex.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://nex.ai/privacy-policy
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/nex-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/nex-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/nex-scopes.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/nex-mcp.yml
- group: build
  title: ''
  type: CLI
  url: cli/nex-cli.yml
- group: build
  title: ''
  type: Packages
  url: packages/nex-packages.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/nex-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/nex-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/nex-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/nex-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/nex-lifecycle.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/nex-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nex-domain-security.yml
created: '2026-07-17'
description: 'Nex is the workflow execution and context layer for AI-native business operations — where AI workflows become reliable business software. It builds a unified context graph from a company''s connected tools (email, calendar, Slack, and CRMs like HubSpot, Salesforce, and Attio) plus ingested unstructured context, then grounds AI agents in that shared organizational memory. The Nex Developer API is a REST API over the context graph: define object types and attributes, create records and typed relationships, group them into lists, attach tasks and notes, read record timelines, ingest context, ask grounded natural-language questions, stream AI-derived insights over SSE, run full-text search, and trigger compounding intelligence jobs. Authentication is via scoped API keys, and organizational context is also exposed to agents through a first-party Model Context Protocol (MCP) server shipped as the nex CLI.'
image: https://raw.githubusercontent.com/nex-crm/docs/main/logo/nex-logo-light.svg
layout: provider
mcp_servers:
- description: ''
  name: nex-mcp.yml
  slug: nex-mcpyml
modified: '2026-07-20'
name: Nex
nav: Providers
network: true
overview: 'Nex publishes 16 APIs on the [APIs.io](https://apis.io/) network, including AI Lists API, Compounding API, Context API, and 13 more. Tagged areas include Company, AI Agents, Knowledge Graph, Context, and Memory.


  Nex''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, pricing, signup flow, and 19 more developer resources.'
random_paper: 11
scopes:
- name: Nex Scopes
  scope_count: 18
  slug: nex-scopes
  summary_line: 18 scopes
score:
  band: developing
  composite: 47.2
  delta: -1.6
  facets:
    commercial_clarity: 44.7
    contract_quality: 56.8
    developer_ergonomics: 69.0
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 5.3
  previous_composite: 48.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 16
    mcp: first-party
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Nex Authentication
  slug: nex-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Nex Domain Security
  slug: nex-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: nex
tags:
- Company
- AI Agents
- Knowledge Graph
- Context
- Memory
- MCP
- Model Context Protocol
- Workflow Automation
- Integrations
- Developer API
website: https://nex.ai
---
