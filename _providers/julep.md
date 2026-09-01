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
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 18.2
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 52
  human_in_the_loop: 0
  name: Julep Agentic Access
  operation_count: 78
  slug: julep-agentic-access
  summary_line: 78 operations · 52 acting
api_count: 1
apis:
- description: The Agents API from Julep — 13 operation(s) for agents.
  name: Julep Agents API
  slug: julep-agents-api
- description: The Docs API from Julep — 1 operation(s) for docs.
  name: Julep Docs API
  slug: julep-docs-api
- description: The Embed API from Julep — 1 operation(s) for embed.
  name: Julep Embed API
  slug: julep-embed-api
- description: The Executions API from Julep — 5 operation(s) for executions.
  name: Julep Executions API
  slug: julep-executions-api
- description: The Files API from Julep — 2 operation(s) for files.
  name: Julep Files API
  slug: julep-files-api
- description: The Jobs API from Julep — 1 operation(s) for jobs.
  name: Julep Jobs API
  slug: julep-jobs-api
- description: The Projects API from Julep — 2 operation(s) for projects.
  name: Julep Projects API
  slug: julep-projects-api
- description: The Responses API from Julep — 2 operation(s) for responses.
  name: Julep Responses API
  slug: julep-responses-api
- description: The Secrets API from Julep — 2 operation(s) for secrets.
  name: Julep Secrets API
  slug: julep-secrets-api
- description: The Sessions API from Julep — 5 operation(s) for sessions.
  name: Julep Sessions API
  slug: julep-sessions-api
- description: The Tasks API from Julep — 2 operation(s) for tasks.
  name: Julep Tasks API
  slug: julep-tasks-api
- description: The Users API from Julep — 5 operation(s) for users.
  name: Julep Users API
  slug: julep-users-api
artifact_total: 29
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Julep Agents API
  slug: open-julep-agents-api
- collection_type: open
  name: Julep Agents Docs API
  slug: open-julep-docs-api
- collection_type: open
  name: Julep Agents Embed API
  slug: open-julep-embed-api
- collection_type: open
  name: Julep Agents Executions API
  slug: open-julep-executions-api
- collection_type: open
  name: Julep Agents Files API
  slug: open-julep-files-api
- collection_type: open
  name: Julep Agents Jobs API
  slug: open-julep-jobs-api
- collection_type: open
  name: Julep Agents Projects API
  slug: open-julep-projects-api
- collection_type: open
  name: Julep Agents Responses API
  slug: open-julep-responses-api
- collection_type: open
  name: Julep Agents Secrets API
  slug: open-julep-secrets-api
- collection_type: open
  name: Julep Agents Sessions API
  slug: open-julep-sessions-api
- collection_type: open
  name: Julep Agents Tasks API
  slug: open-julep-tasks-api
- collection_type: open
  name: Julep Agents Users API
  slug: open-julep-users-api
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/julep-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/julep-openapi-overlay.yaml
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/julep-ai/julep/issues
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/julep-ai/julep/blob/main/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/julep-ai/julep/blob/main/LICENSE
- group: auth
  title: ''
  type: DomainSecurity
  url: security/julep-domain-security.yml
- group: docs
  title: ''
  type: Documentation
  url: https://docs.julep.ai
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.julep.ai
- group: docs
  title: ''
  type: APIReference
  url: https://docs.julep.ai/api-reference/agents/list-agents
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.julep.ai/introduction/quickstart
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/julep-ai
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/julep-ai/julep
- group: build
  title: ''
  type: Packages
  url: packages/julep-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/julep-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/julep-cli.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/julep-llms.txt
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/julep-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/julep-changelog.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Julep is an open-source platform for building stateful AI agents that remember past interactions and execute long-running, multi-step tasks. Its cloud API and self-hostable server expose agents, sessions, tasks, executions, documents (RAG), tools, users, projects, secrets, and files, along with a task-workflow engine that supports decisions, loops, parallel branches, and integrations to external tools and APIs. Official Python and TypeScript SDKs and a command-line interface wrap the REST API; authentication is via API key. Julep is Apache-2.0 licensed and backed by Version One Ventures.
image: https://avatars.githubusercontent.com/u/112750682?v=4
layout: provider
mcp_servers:
- description: ''
  name: Julep MCP Server
  slug: julep-mcp-server
modified: '2026-07-19'
name: Julep
nav: Providers
network: true
overview: 'Julep publishes 12 APIs on the [APIs.io](https://apis.io/) network, including Agents API, Docs API, Embed API, and 9 more. Tagged areas include Company, AI Agents, LLM, Agents, and Workflows.


  Julep''s developer surface includes documentation, API reference, getting-started guide, CLI, changelog, and 14 more developer resources.'
random_paper: 19
score:
  band: thin
  composite: 36.0
  coverage:
    artifact_dirs: 18
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 4.5
    contract_quality: 53.9
    developer_ergonomics: 66.1
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 18.4
  open_source:
    applies: true
    score: 25.0
  previous_composite: 36.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 12
    mcp: derived
    skills: derived
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/julep/refs/heads/main/screenshots/julep-2026-07-25T223304.png
security:
- kind: authentication
  name: Julep Authentication
  slug: julep-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Julep Domain Security
  slug: julep-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: julep
tags:
- Company
- AI Agents
- LLM
- Agents
- Workflows
- RAG
- Memory
- Orchestration
- Developer Tools
- Open-Source
website: https://docs.julep.ai
---
