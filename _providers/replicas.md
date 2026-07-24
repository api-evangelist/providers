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
    asyncapi_events: true
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
  score: 71.2
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 57
  human_in_the_loop: 5
  name: Replicas Agentic Access
  operation_count: 99
  slug: replicas-agentic-access
  summary_line: 99 operations · 57 acting · 5 human-in-the-loop
api_count: 13
apis:
- description: 'Read aggregated activity and usage metrics for your organization: compute minutes, workspaces created by source, and pull request throughput over a time range.'
  name: Replicas Analytics API
  slug: replicas-analytics-api
- description: The API Keys API from Replicas — 2 operation(s) for api keys.
  name: Replicas API Keys API
  slug: replicas-api-keys-api
- description: Create and manage automations that trigger replicas on a schedule or in response to events
  name: Replicas Automation API
  slug: replicas-automation-api
- description: Manage coding-agent credentials for an organization or the authenticated user
  name: Replicas Credentials API
  slug: replicas-credentials-api
- description: Download Replicas applications
  name: Replicas Downloads API
  slug: replicas-downloads-api
- description: Manage environments — the primitive that workspaces are created from. Variables, files, skills, MCPs, warm-hooks, and warm-pools are all scoped to an environment. Every organization has a singleton Gl
  name: Replicas Environments API
  slug: replicas-environments-api
- description: Read Search Console properties, performance, sitemaps, and URL inspection results through a connected Google account
  name: Replicas Google Search Console API
  slug: replicas-google-search-console-api
- description: Manage public preview URLs for workspace ports
  name: Replicas Preview API
  slug: replicas-preview-api
- description: Read and update the authenticated user's profile
  name: Replicas Profile API
  slug: replicas-profile-api
- description: Manage replicas (workspaces) for AI agents
  name: Replicas Replica API
  slug: replicas-replica-api
- description: Read repositories and repository sets connected to your organization. Repositories are the underlying GitHub-connection layer; bind them to an environment to use them in workspaces.
  name: Replicas Repository API
  slug: replicas-repository-api
- description: Route Slack threads to Replicas workspaces
  name: Replicas Slack API
  slug: replicas-slack-api
- description: Manage interactive terminal sessions in active workspaces
  name: Replicas Terminal API
  slug: replicas-terminal-api
artifact_total: 19
asyncapis:
- description: ''
  name: Replicas Webhooks
  slug: replicas-webhooks
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.tryreplicas.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.tryreplicas.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.tryreplicas.com/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.tryreplicas.com/features/api
- group: start
  title: ''
  type: SignUp
  url: https://tryreplicas.com/auth
- group: commercial
  title: ''
  type: Pricing
  url: https://tryreplicas.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://tryreplicas.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://tryreplicas.com/privacy
- group: company
  title: ''
  type: Blog
  url: https://tryreplicas.com/blog
- group: build
  title: ''
  type: GitHub
  url: https://github.com/tryreplicas
- group: operate
  title: ''
  type: Support
  url: mailto:founders@replicas.dev
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.tryreplicas.com/changelog
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/replicas-changelog.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/replicas-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/replicas-mcp.yml
- group: build
  title: ''
  type: CLI
  url: cli/replicas-cli.yml
- group: build
  title: ''
  type: Packages
  url: packages/replicas-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/replicas-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/replicas-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/replicas-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/replicas-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/replicas-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/replicas-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/replicas-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/replicas-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/replicas-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/replicas-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://tryreplicas.com/responsible-disclosure
created: '2026-07-17'
description: Replicas (tryreplicas.com), a Y Combinator (Spring 2026) company, runs end-to-end background coding agents in isolated cloud sandboxes. Teams delegate engineering tasks - from Slack, Linear, GitHub, GitLab, Sentry, the web dashboard, a CLI, or a native macOS app - to frontier coding agents (Claude Code, Codex, Cursor, OpenCode) that work in their own VM-backed workspaces with databases, environment variables, files, skills, and MCP servers, then open pull requests for review. The Replica API (OpenAPI 3.1, base https://api.tryreplicas.com/v1, bearer API-key auth) exposes environments, replicas/workspaces, chats, event streaming (SSE), repositories, automations (cron + webhook triggered), and Google Search Console tooling, plus an official hosted MCP server at api.tryreplicas.com/v1/mcp.
image: https://tryreplicas.com/opengraph-image.png
layout: provider
mcp_servers:
- description: ''
  name: replicas-mcp.yml
  slug: replicas-mcpyml
modified: '2026-07-20'
name: Replicas
nav: Providers
network: true
overview: 'Replicas publishes 13 APIs on the [APIs.io](https://apis.io/) network, including Analytics API, API Keys API, Automation API, and 10 more. Tagged areas include Company, AI, Coding Agents, Developer Tools, and Automation.


  The Replicas catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Replicas'' developer surface includes documentation, API reference, getting-started guide, signup flow, pricing, engineering blog, GitHub presence, and 22 more developer resources.'
random_paper: 35
score:
  band: developing
  composite: 55.5
  delta: 0.0
  facets:
    commercial_clarity: 44.7
    contract_quality: 66.7
    developer_ergonomics: 73.9
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 39.5
  previous_composite: 55.5
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Replicas Authentication
  slug: replicas-authentication
  summary_line: http/apiKey · 3 schemes
- kind: domain-security
  name: Replicas Domain Security
  slug: replicas-domain-security
  summary_line: TLSv1.3
- kind: vulnerability-disclosure
  name: Replicas Vulnerability Disclosure
  slug: replicas-vulnerability-disclosure
  summary_line: contact published
slug: replicas
tags:
- Company
- AI
- Coding Agents
- Developer Tools
- Automation
- Cloud Workspaces
- MCP
- DevOps
website: https://docs.tryreplicas.com
---
