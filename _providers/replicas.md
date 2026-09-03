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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: verified
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 39.4
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 57
  human_in_the_loop: 5
  name: Replicas Agentic Access
  operation_count: 99
  slug: replicas-agentic-access
  summary_line: 99 operations · 57 acting · 5 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.tryreplicas.com
  baseurl_source: declared
  description: 'Read aggregated activity and usage metrics for your organization: compute minutes, workspaces created by source, and pull request throughput over a time range.'
  name: Replicas Analytics API
  slug: replicas-analytics-api
- baseURL: https://api.tryreplicas.com
  baseurl_source: declared
  description: The API Keys API from Replicas — 2 operation(s) for api keys.
  name: Replicas API Keys API
  slug: replicas-api-keys-api
- baseURL: https://api.tryreplicas.com
  baseurl_source: declared
  description: Create and manage automations that trigger replicas on a schedule or in response to events
  name: Replicas Automation API
  slug: replicas-automation-api
- baseURL: https://api.tryreplicas.com
  baseurl_source: declared
  description: Manage coding-agent credentials for an organization or the authenticated user
  name: Replicas Credentials API
  slug: replicas-credentials-api
- baseURL: https://api.tryreplicas.com
  baseurl_source: declared
  description: Download Replicas applications
  name: Replicas Downloads API
  slug: replicas-downloads-api
- baseURL: https://api.tryreplicas.com
  baseurl_source: declared
  description: Manage environments — the primitive that workspaces are created from. Variables, files, skills, MCPs, warm-hooks, and warm-pools are all scoped to an environment. Every organization has a singleton Gl
  name: Replicas Environments API
  slug: replicas-environments-api
- baseURL: https://api.tryreplicas.com
  baseurl_source: declared
  description: Read Search Console properties, performance, sitemaps, and URL inspection results through a connected Google account
  name: Replicas Google Search Console API
  slug: replicas-google-search-console-api
- baseURL: https://api.tryreplicas.com
  baseurl_source: declared
  description: Manage public preview URLs for workspace ports
  name: Replicas Preview API
  slug: replicas-preview-api
- baseURL: https://api.tryreplicas.com
  baseurl_source: declared
  description: Read and update the authenticated user's profile
  name: Replicas Profile API
  slug: replicas-profile-api
- baseURL: https://api.tryreplicas.com
  baseurl_source: declared
  description: Manage replicas (workspaces) for AI agents
  name: Replicas Replica API
  slug: replicas-replica-api
- baseURL: https://api.tryreplicas.com
  baseurl_source: declared
  description: Read repositories and repository sets connected to your organization. Repositories are the underlying GitHub-connection layer; bind them to an environment to use them in workspaces.
  name: Replicas Repository API
  slug: replicas-repository-api
- baseURL: https://api.tryreplicas.com
  baseurl_source: declared
  description: Route Slack threads to Replicas workspaces
  name: Replicas Slack API
  slug: replicas-slack-api
- baseURL: https://api.tryreplicas.com
  baseurl_source: declared
  description: Manage interactive terminal sessions in active workspaces
  name: Replicas Terminal API
  slug: replicas-terminal-api
artifact_total: 32
asyncapis:
- description: ''
  name: Replicas Webhooks
  slug: replicas-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Replica Analytics API
  slug: open-replicas-analytics-api
- collection_type: open
  name: Replica Analytics API Keys API
  slug: open-replicas-api-keys-api
- collection_type: open
  name: Replica Analytics Automation API
  slug: open-replicas-automation-api
- collection_type: open
  name: Replica Analytics Credentials API
  slug: open-replicas-credentials-api
- collection_type: open
  name: Replica Analytics Downloads API
  slug: open-replicas-downloads-api
- collection_type: open
  name: Replica Analytics Environments API
  slug: open-replicas-environments-api
- collection_type: open
  name: Replica Analytics Google Search Console API
  slug: open-replicas-google-search-console-api
- collection_type: open
  name: Replica Analytics Profile API
  slug: open-replicas-profile-api
- collection_type: open
  name: Analytics Replica API
  slug: open-replicas-replica-api
- collection_type: open
  name: Replica Analytics Repository API
  slug: open-replicas-repository-api
- collection_type: open
  name: Replica Analytics Slack API
  slug: open-replicas-slack-api
- collection_type: open
  name: Replica Analytics Terminal API
  slug: open-replicas-terminal-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/replicas-openapi-overlay.yaml
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
- description: Official Replicas MCP server for managing cloud workspaces (replicas) for AI coding agents from MCP clients such as Claude Desktop, Claude Code, and Poke.
  name: Replicas MCP Server
  slug: replicas-mcp-server
modified: '2026-07-20'
name: Replicas
nav: Providers
network: true
overview: 'Replicas publishes 13 APIs on the [APIs.io](https://apis.io/) network, including Analytics API, API Keys API, Automation API, and 10 more. Tagged areas include Company, Artificial Intelligence, Coding Agents, Developer Tools, and Automation.


  The Replicas catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Replicas'' developer surface includes documentation, API reference, getting-started guide, signup flow, pricing, engineering blog, GitHub presence, and 23 more developer resources.'
random_paper: 11
score:
  band: developing
  composite: 51.6
  coverage:
    artifact_dirs: 21
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 4.5
    contract_quality: 64.5
    developer_ergonomics: 66.1
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 39.5
  previous_composite: 51.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 13
    mcp: first-party
    skills: derived
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/replicas/refs/heads/main/screenshots/replicas-2026-08-17T081523.png
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
- Artificial Intelligence
- Coding Agents
- Developer Tools
- Automation
- Cloud Workspaces
- MCP
- DevOps
website: https://docs.tryreplicas.com
---
