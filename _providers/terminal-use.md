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
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: verified
    mcp_server: derived
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 55.2
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 78
  human_in_the_loop: 2
  name: Terminal Use Agentic Access
  operation_count: 151
  slug: terminal-use-agentic-access
  summary_line: 151 operations · 78 acting · 2 human-in-the-loop
api_count: 28
apis:
- description: The Agent APIKeys API from Terminal Use — 4 operation(s) for agent apikeys.
  name: Terminal Use Agent APIKeys API
  slug: terminal-use-agent-apikeys-api
- description: The Agent Task Tracker API from Terminal Use — 2 operation(s) for agent task tracker.
  name: Terminal Use Agent Task Tracker API
  slug: terminal-use-agent-task-tracker-api
- description: The Agents API from Terminal Use — 7 operation(s) for agents.
  name: Terminal Use Agents API
  slug: terminal-use-agents-api
- description: The API Keys API from Terminal Use — 3 operation(s) for api keys.
  name: Terminal Use API Keys API
  slug: terminal-use-api-keys-api
- description: The Authentication API from Terminal Use — 1 operation(s) for authentication.
  name: Terminal Use Authentication API
  slug: terminal-use-authentication-api
- description: The Branch Events API from Terminal Use — 1 operation(s) for branch events.
  name: Terminal Use Branch Events API
  slug: terminal-use-branch-events-api
- description: The Branches API from Terminal Use — 10 operation(s) for branches.
  name: Terminal Use Branches API
  slug: terminal-use-branches-api
- description: The Builds API from Terminal Use — 3 operation(s) for builds.
  name: Terminal Use Builds API
  slug: terminal-use-builds-api
- description: The CLI Authentication API from Terminal Use — 2 operation(s) for cli authentication.
  name: Terminal Use CLI Authentication API
  slug: terminal-use-cli-authentication-api
- description: The Environments API from Terminal Use — 4 operation(s) for environments.
  name: Terminal Use Environments API
  slug: terminal-use-environments-api
- description: The Events API from Terminal Use — 2 operation(s) for events.
  name: Terminal Use Events API
  slug: terminal-use-events-api
- description: The Filesystems API from Terminal Use — 9 operation(s) for filesystems.
  name: Terminal Use Filesystems API
  slug: terminal-use-filesystems-api
- description: The Groups API from Terminal Use — 8 operation(s) for groups.
  name: Terminal Use Groups API
  slug: terminal-use-groups-api
- description: The Logs API from Terminal Use — 3 operation(s) for logs.
  name: Terminal Use Logs API
  slug: terminal-use-logs-api
- description: The Messages v2 API from Terminal Use — 2 operation(s) for messages v2.
  name: Terminal Use Messages v2 API
  slug: terminal-use-messages-v2-api
- description: The Namespaces API from Terminal Use — 5 operation(s) for namespaces.
  name: Terminal Use Namespaces API
  slug: terminal-use-namespaces-api
- description: The OAuth API from Terminal Use — 2 operation(s) for oauth.
  name: Terminal Use OAuth API
  slug: terminal-use-oauth-api
- description: The Organizations API from Terminal Use — 7 operation(s) for organizations.
  name: Terminal Use Organizations API
  slug: terminal-use-organizations-api
- description: The Projects API from Terminal Use — 4 operation(s) for projects.
  name: Terminal Use Projects API
  slug: terminal-use-projects-api
- description: The Raw Events API from Terminal Use — 1 operation(s) for raw events.
  name: Terminal Use Raw Events API
  slug: terminal-use-raw-events-api
- description: The Registry API from Terminal Use — 1 operation(s) for registry.
  name: Terminal Use Registry API
  slug: terminal-use-registry-api
- description: The Schedules API from Terminal Use — 5 operation(s) for schedules.
  name: Terminal Use Schedules API
  slug: terminal-use-schedules-api
- description: The Search API from Terminal Use — 1 operation(s) for search.
  name: Terminal Use Search API
  slug: terminal-use-search-api
- description: The Secrets API from Terminal Use — 4 operation(s) for secrets.
  name: Terminal Use Secrets API
  slug: terminal-use-secrets-api
- description: The States API from Terminal Use — 2 operation(s) for states.
  name: Terminal Use States API
  slug: terminal-use-states-api
- description: The Tasks API from Terminal Use — 14 operation(s) for tasks.
  name: Terminal Use Tasks API
  slug: terminal-use-tasks-api
- description: The Version Events API from Terminal Use — 1 operation(s) for version events.
  name: Terminal Use Version Events API
  slug: terminal-use-version-events-api
- description: The Versions API from Terminal Use — 6 operation(s) for versions.
  name: Terminal Use Versions API
  slug: terminal-use-versions-api
artifact_total: 33
asyncapis:
- description: ''
  name: Terminal Use Webhooks
  slug: terminal-use-webhooks
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/terminal-use-agentic-access.yml
- group: company
  title: ''
  type: Website
  url: https://www.terminaluse.com
- group: start
  title: ''
  type: Portal
  url: https://app.terminaluse.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.terminaluse.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.terminaluse.com/api-reference/authentication
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.terminaluse.com/introduction/quickstart
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/terminal-use
- group: start
  title: ''
  type: SignUp
  url: https://app.terminaluse.com
- group: auth
  title: ''
  type: Authentication
  url: authentication/terminal-use-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/terminal-use-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/terminal-use-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/terminal-use-cli.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/terminal-use-llms.txt
- group: design
  title: ''
  type: Conventions
  url: conventions/terminal-use-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/terminal-use-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/terminal-use-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/terminal-use-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/terminal-use-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/terminal-use-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/terminal-use-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/terminal-use-openapi-overlay.yaml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/terminal-use-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/terminal-use-domain-security.yml
created: '2026-07-17'
description: Terminal Use is a deployment and orchestration platform for background AI agents — "Vercel for background agents." It gives agents that need long-lived task state, persistent files at /workspace, and production deployment primitives (versions, rollback, logs, environment secrets) a single runtime model and one deploy flow. Teams write agent code in Python with the AgentServer runtime, ship it with the tu CLI, then call deployed agents from their own app with the Python or TypeScript SDKs (including a Vercel AI SDK provider for streaming chat UIs). The platform is model- and framework- agnostic — run the Claude Agent SDK, Codex SDK, or your own framework inside sandboxed compute with forkable, shareable filesystems. The HTTP API exposes namespaces, projects, agents, branches, versions, tasks, events, messages, state, filesystems, schedules, secrets, API keys, and webhook keys. Terminal Use is a Y Combinator (W26) company founded by Vivek Raja, Filip Balucha, and Stavros Filosidis.
image: https://www.terminaluse.com/icon.svg
layout: provider
mcp_servers:
- description: ''
  name: terminal-use-mcp.yml
  slug: terminal-use-mcpyml
modified: '2026-07-21'
name: Terminal Use
nav: Providers
network: true
overview: 'Terminal Use publishes 28 APIs on the [APIs.io](https://apis.io/) network, including Agent APIKeys API, Agent Task Tracker API, Agents API, and 25 more. Tagged areas include Company, Agents, AI Agents, Background Agents, and Agent Infrastructure.


  The Terminal Use catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Terminal Use''s developer surface includes developer portal, documentation, API reference, getting-started guide, signup flow, authentication, CLI, and 17 more developer resources.'
random_paper: 53
score:
  band: thin
  composite: 40.2
  delta: -3.6
  facets:
    commercial_clarity: 13.2
    contract_quality: 55.3
    developer_ergonomics: 62.5
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 13.2
  previous_composite: 43.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 28
    mcp: derived
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Terminal Use Authentication
  slug: terminal-use-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Terminal Use Domain Security
  slug: terminal-use-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: terminal-use
tags:
- Company
- Agents
- AI Agents
- Background Agents
- Agent Infrastructure
- Deployment
- Orchestration
- Sandboxed Compute
- Filesystems
- Developer Tools
- SDK
- CLI
website: https://www.terminaluse.com
---
