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
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 39
  human_in_the_loop: 8
  name: Stacklok Agentic Access
  operation_count: 84
  slug: stacklok-agentic-access
  summary_line: 84 operations · 39 acting · 8 human-in-the-loop
api_count: 13
apis:
- description: The ToolHive Registry Server API for discovering, governing, and controlling access to MCP servers and agent skills — MCP Registry API v0.1 (read) plus a /v1 admin API. OpenAPI 3.1.
  name: ToolHive Registry API
  slug: toolhive-registry-api
- description: The clients API from Stacklok — 5 operation(s) for clients.
  name: Stacklok clients API
  slug: stacklok-clients-api
- description: The discovery API from Stacklok — 1 operation(s) for discovery.
  name: Stacklok discovery API
  slug: stacklok-discovery-api
- description: The groups API from Stacklok — 2 operation(s) for groups.
  name: Stacklok groups API
  slug: stacklok-groups-api
- description: The logs API from Stacklok — 2 operation(s) for logs.
  name: Stacklok logs API
  slug: stacklok-logs-api
- description: The registry-servers API from Stacklok — 2 operation(s) for registry-servers.
  name: Stacklok registry-servers API
  slug: stacklok-registry-servers-api
- description: The registry-skills API from Stacklok — 2 operation(s) for registry-skills.
  name: Stacklok registry-skills API
  slug: stacklok-registry-skills-api
- description: The secrets API from Stacklok — 4 operation(s) for secrets.
  name: Stacklok secrets API
  slug: stacklok-secrets-api
- description: The skills API from Stacklok — 12 operation(s) for skills.
  name: Stacklok skills API
  slug: stacklok-skills-api
- description: The system API from Stacklok — 3 operation(s) for system.
  name: Stacklok system API
  slug: stacklok-system-api
- description: The v1 API from Stacklok — 10 operation(s) for v1.
  name: Stacklok v1 API
  slug: stacklok-v1-api
- description: The version API from Stacklok — 1 operation(s) for version.
  name: Stacklok version API
  slug: stacklok-version-api
- description: The workloads API from Stacklok — 13 operation(s) for workloads.
  name: Stacklok workloads API
  slug: stacklok-workloads-api
artifact_total: 17
common:
- group: company
  title: ''
  type: Website
  url: https://www.stacklok.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.stacklok.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.stacklok.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.stacklok.com/toolhive/reference/api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.stacklok.com/toolhive/guides-cli/install
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/stacklok
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/stacklok/toolhive
- group: company
  title: ''
  type: Blog
  url: https://stacklok.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://discord.gg/stacklok
- group: commercial
  title: ''
  type: TermsOfService
  url: https://stacklok.com/platform-terms/
- group: build
  title: ''
  type: Packages
  url: packages/stacklok-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/stacklok-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/stacklok-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/stacklok-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/stacklok-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/stacklok-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/stacklok-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/stacklok-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/stacklok-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/stacklok-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/stacklok-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/stacklok-data-model.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/stacklok-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/stacklok-domain-security.yml
created: '2026-07-17'
description: Stacklok is an open-source company building trust and governance infrastructure for AI agents and the Model Context Protocol (MCP). Its flagship open-source project, ToolHive (Apache 2.0), runs, secures, and governs MCP servers and agent skills across desktop, CLI, and Kubernetes, while the Stacklok Enterprise Platform and AI Gateway add centralized policy (Cedar/RBAC), OIDC authorization, LLM spend control, and a governed registry. Stacklok exposes two OpenAPI 3.1 surfaces — the ToolHive control API (thv serve, /api/v1beta) and the ToolHive Registry Server API (MCP Registry API v0.1 plus a /v1 admin API) — plus the thv CLI. Founded by Craig McLuckie and Luke Hinds; backed by Accel and Bain Capital Ventures.
image: https://github.com/stacklok.png
layout: provider
mcp_servers:
- description: ''
  name: stacklok-mcp.yml
  slug: stacklok-mcpyml
modified: '2026-07-21'
name: Stacklok
nav: Providers
network: true
overview: 'Stacklok publishes 13 APIs on the [APIs.io](https://apis.io/) network, including ToolHive Registry API, clients API, discovery API, and 10 more. Tagged areas include Company, Open Source, MCP, AI Agents, and API Governance.


  Stacklok''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, CLI, authentication, and 18 more developer resources.'
random_paper: 44
score:
  band: thin
  composite: 43.5
  delta: 0.0
  facets:
    commercial_clarity: 10.5
    contract_quality: 50.5
    developer_ergonomics: 80.4
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 43.5
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Stacklok Authentication
  slug: stacklok-authentication
  summary_line: oauth2/openIdConnect · 1 scheme
- kind: domain-security
  name: Stacklok Domain Security
  slug: stacklok-domain-security
  summary_line: TLSv1.3 · DMARC
slug: stacklok
tags:
- Company
- Open Source
- MCP
- AI Agents
- API Governance
- Security
- Model Context Protocol
- Developer Tools
website: https://www.stacklok.com/
---
