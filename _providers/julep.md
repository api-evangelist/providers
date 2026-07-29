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
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 52
  human_in_the_loop: 0
  name: Julep Agentic Access
  operation_count: 78
  slug: julep-agentic-access
  summary_line: 78 operations · 52 acting
api_count: 12
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
artifact_total: 15
common:
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
modified: '2026-07-19'
name: Julep
nav: Providers
network: true
overview: 'Julep publishes 12 APIs on the [APIs.io](https://apis.io/) network, including Agents API, Docs API, Embed API, and 9 more. Tagged areas include Company, AI Agents, LLM, Agents, and Workflows.


  Julep''s developer surface includes documentation, API reference, getting-started guide, CLI, changelog, and 9 more developer resources.'
random_paper: 70
score:
  band: thin
  composite: 34.8
  delta: -0.9
  facets:
    commercial_clarity: 0.0
    contract_quality: 50.6
    developer_ergonomics: 49.5
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 21.1
  previous_composite: 35.7
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
  schema_version: 0.6
  scored_at: '2026-07-28'
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
- Open Source
website: https://docs.julep.ai
---
