---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 6.0
  scored_at: '2026-09-01'
api_count: 10
apis:
- description: Versioned external REST API introduced in Sourcegraph 7.0 and intended as the stable integration surface going forward. Each Sourcegraph instance exposes its own /api-reference path where the live Ope
  name: Sourcegraph REST API
  slug: sourcegraph-rest-api
- description: The historical GraphQL API used by most Sourcegraph integrations to date. It is still available but Sourcegraph now recommends migrating to the versioned REST API for compatibility guarantees. Also ex
  name: Sourcegraph GraphQL API
  slug: sourcegraph-graphql-api
- description: Server-sent-event API that streams search results as they are produced, used by the Sourcegraph UI and by integrations that want incremental result delivery instead of batched responses. Exposed per-i
  name: Sourcegraph Streaming Search API
  slug: sourcegraph-streaming-search-api
- description: API surface for pulling usage and search analytics from a Sourcegraph instance.
  name: Sourcegraph Analytics API
  slug: sourcegraph-analytics-api
- description: Sourcegraph instances expose three distinct webhook surfaces. Outgoing webhooks (Site Admin > Configuration > Outgoing webhooks) push batch_change, changeset, and user:create events to external HTTP e
  name: Sourcegraph Webhooks
  slug: sourcegraph-webhooks
- description: Model Context Protocol server exposed by Sourcegraph so MCP-compatible AI agents can use Sourcegraph search and code intelligence as tools.
  name: Sourcegraph MCP Server
  slug: sourcegraph-mcp-server
- description: Cody is Sourcegraph's AI coding assistant. It runs inside VS Code and JetBrains IDEs, uses Sourcegraph code intelligence for codebase-aware context, and can write, explain, and fix code grounded in th
  name: Cody by Sourcegraph
  slug: cody
- description: Amp is Sourcegraph's frontier coding agent, designed for pay-as-you-go use against leading AI models. It ships a CLI for macOS, Linux, WSL, and Windows, supports plugins (slash commands in .agents/com
  name: Amp Coding Agent
  slug: amp
- description: Deep Search is a natural-language code research agent that answers complex questions about a codebase by combining Sourcegraph search, code intelligence, and AI.
  name: Sourcegraph Deep Search
  slug: deep-search
- description: src is Sourcegraph's command-line client for code search, code intelligence, batch changes, and administrative operations against a Sourcegraph instance.
  name: src CLI
  slug: src-cli
artifact_total: 37
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/sourcegraph/cody-public-snapshot/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/sourcegraph/cody-public-snapshot/releases
- group: commercial
  title: ''
  type: License
  url: https://github.com/sourcegraph/cody-public-snapshot/blob/main/LICENSE
- group: auth
  title: ''
  type: TrustCenter
  url: security/sourcegraph-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/sourcegraph-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sourcegraph-domain-security.yml
- group: start
  title: ''
  type: Portal
  url: https://sourcegraph.com
- group: docs
  title: ''
  type: Documentation
  url: https://sourcegraph.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://sourcegraph.com/docs/api
- group: company
  title: ''
  type: Blog
  url: https://sourcegraph.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/sourcegraph
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/sourcegraph/sourcegraph-public-snapshot
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/sourcegraph/cody-public-snapshot
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/sourcegraph/amp-contrib
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/sourcegraph/src-cli
- group: build
  title: ''
  type: CLI
  url: https://sourcegraph.com/docs
- group: build
  title: ''
  type: CLI
  url: https://ampcode.com
- group: agent
  title: ''
  type: MCPServer
  url: https://sourcegraph.com/docs/api
- group: commercial
  title: ''
  type: Pricing
  url: https://ampcode.com/pricing
- group: operate
  title: ''
  type: Support
  url: https://sourcegraph.com/docs
created: '2026-05-23'
description: Sourcegraph is a code intelligence platform that lets developers and AI agents search, navigate, understand, and modify code across very large, multi-repo codebases. The platform pairs classic code search and code intelligence (jump-to-definition, references, batch changes) with AI products — Cody (in-IDE AI coding assistant), Amp (frontier coding agent with its own CLI and plugin system), and Deep Search (a natural-language code research agent). Sourcegraph instances expose a versioned external REST API introduced in v7.0, a streaming search API, an analytics API, webhooks, an MCP server, and the historical GraphQL API kept available for migration. The src CLI is the long-standing command-line client.
features:
- description: Search across every branch of every repository on every code host connected to Sourcegraph.
  name: Multi-Repo Code Search
- description: Jump-to-definition, find references, hover documentation, and dependency graphs powered by SCIP indexes.
  name: Code Intelligence
- description: Apply large-scale code modifications across many repositories from a single specification.
  name: Batch Changes
- description: Codebase-aware AI assistant for writing, explaining, and fixing code inside VS Code and JetBrains.
  name: Cody AI Assistant
- description: Frontier coding agent with its own CLI, plugin model, and pay-as-you-go pricing.
  name: Amp Coding Agent
- description: Natural-language code research agent for complex questions about large codebases.
  name: Deep Search
- description: Stable, backwards-compatible REST API introduced in v7.0 with per-instance OpenAPI schema.
  name: Versioned REST API
- description: SSE streaming search and an analytics API for pulling usage data.
  name: Streaming Search and Analytics
- description: Push events to external systems and expose Sourcegraph as a tool surface to AI agents via MCP.
  name: Webhooks and MCP Server
finops:
- name: Sourcegraph Finops
  service_category: API
  slug: sourcegraph-finops
graphqls:
- description: The historical GraphQL API used by most Sourcegraph integrations to date. It is still available but Sourcegraph now recommends migrating to the versioned REST API for compatibility guarantees. Also ex
  name: Sourcegraph GraphQL API
  slug: sourcegraph-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sourcegraph.png
integrations:
- description: Cody and Amp IDE integration for Visual Studio Code.
  name: VS Code
- description: Cody plugin for JetBrains IDEs.
  name: JetBrains
- description: Connects to all major code hosts.
  name: GitHub, GitLab, Bitbucket
- description: Exposes Sourcegraph as a tool to MCP-compatible AI agents.
  name: MCP Server
- description: Event push to CI, chat, and ticketing systems.
  name: Webhooks
layout: provider
mcp_servers:
- description: ''
  name: Sourcegraph MCP Server
  slug: sourcegraph-mcp-server
modified: '2026-05-30'
name: Sourcegraph
nav: Providers
network: true
overview: 'Sourcegraph publishes 10 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Code Intelligence, Code Search, Cody, AMP, and AI Coding Agent.


  Sourcegraph''s developer surface includes developer portal, documentation, API reference, engineering blog, CLI, pricing, support, and 13 more developer resources.'
plans:
- name: Sourcegraph Plans Pricing
  plan_count: 1
  slug: sourcegraph-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 2
  name: Sourcegraph Rate Limits
  slug: sourcegraph-rate-limits
score:
  band: thin
  composite: 30.9
  coverage:
    artifact_dirs: 7
    catalog_gap: 61.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 52.4
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 39.5
  open_source:
    applies: true
    score: 25.0
  previous_composite: 30.9
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sourcegraph/refs/heads/main/screenshots/sourcegraph-2026-06-20T194223.png
security:
- kind: domain-security
  name: Sourcegraph Domain Security
  slug: sourcegraph-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Sourcegraph Vulnerability Disclosure
  slug: sourcegraph-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Sourcegraph Trust Center
  slug: sourcegraph-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: sourcegraph
tags:
- Code Intelligence
- Code Search
- Cody
- AMP
- AI Coding Agent
- GraphQL
- REST API
- MCP
use_cases:
- description: Find anything across millions of lines of code across many repositories.
  name: Code Search at Scale
- description: Use Cody and Amp to write, refactor, and fix code with codebase context.
  name: AI-Assisted Coding
- description: Apply consistent changes across hundreds of repositories with Batch Changes.
  name: Large-Scale Refactors
- description: Use Deep Search to answer architectural questions about an unfamiliar codebase.
  name: Codebase Research
- description: Expose Sourcegraph code intelligence as MCP tools for AI agents.
  name: Agentic Code Tooling
website: https://sourcegraph.com
---
