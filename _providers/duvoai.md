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
    agent_card: flavored
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: true
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: verified
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 60.4
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 124
  human_in_the_loop: 7
  name: Duvoai Agentic Access
  operation_count: 213
  slug: duvoai-agentic-access
  summary_line: 213 operations · 124 acting · 7 human-in-the-loop
api_count: 1
apis:
- description: Organize agents into folders
  name: duvo.ai Agent Folders API
  slug: duvoai-agent-folders-api
- description: Read an agent's memory files (the Memory feature in the Duvo UI)
  name: duvo.ai Agent Memory API
  slug: duvoai-agent-memory-api
- description: Create and manage agents for automation workloads
  name: duvo.ai Agents API
  slug: duvoai-agents-api
- description: Configure case triggers that automatically dispatch agent runs (Runs in the Duvo UI) for cases added to a queue
  name: duvo.ai Case Triggers API
  slug: duvoai-case-triggers-api
- description: Create, list, and manage cases and their labels within queues
  name: duvo.ai Cases API
  slug: duvoai-cases-api
- description: The Clarity API from duvo.ai — 17 operation(s) for clarity.
  name: duvo.ai Clarity API
  slug: duvoai-clarity-api
- description: Manage Clarity v2 process snapshots, transformation proposals, and the extra-capture-request follow-up loop
  name: duvo.ai ClarityV2 API
  slug: duvoai-clarityv2-api
- description: Manage your connected integrations
  name: duvo.ai Connections API
  slug: duvoai-connections-api
- description: Manage logins (domain + username + password + TOTP) used by agents to sign in to websites and desktop applications, and attach them to assignment revisions
  name: duvo.ai Credentials API
  slug: duvoai-credentials-api
- description: Create, list, iterate on, and delete Duvo Pulse dashboards — live, agent-generated visualizations of your Duvo data
  name: duvo.ai Duvo Pulse API
  slug: duvoai-duvo-pulse-api
- description: Manage team files.
  name: duvo.ai Files API
  slug: duvoai-files-api
- description: Browse the team's catalog of available integration types
  name: duvo.ai Integrations API
  slug: duvoai-integrations-api
- description: MCP JSON-RPC endpoint exposing public API routes as LLM-callable tools
  name: duvo.ai MCP API
  slug: duvoai-mcp-api
- description: Inspect organizations you belong to and the teams within them
  name: duvo.ai Organizations API
  slug: duvoai-organizations-api
- description: Discover plugins that can be referenced from a revision.
  name: duvo.ai Plugins API
  slug: duvoai-plugins-api
- description: Manage queues and their agent bindings
  name: duvo.ai Queues API
  slug: duvoai-queues-api
- description: Attach integrations to assignment revisions, pin specific connections, and link queues
  name: duvo.ai Revision Integrations API
  slug: duvoai-revision-integrations-api
- description: Create and manage agent revisions — the underlying Setup for an Agent
  name: duvo.ai Revisions API
  slug: duvoai-revisions-api
- description: Start, monitor, and manage agent runs (Runs in the Duvo UI)
  name: duvo.ai Runs API
  slug: duvoai-runs-api
- description: Create sandboxes and upload files for agent runs
  name: duvo.ai Sandboxes API
  slug: duvoai-sandboxes-api
- description: List schedules configured for an agent
  name: duvo.ai Schedules API
  slug: duvoai-schedules-api
- description: Manage env-var secrets injected into runs, and attach them to assignment revisions. Only metadata is exposed; values are never returned
  name: duvo.ai Secrets API
  slug: duvoai-secrets-api
- description: Manage team and system skills (reusable knowledge packs).
  name: duvo.ai Skills API
  slug: duvoai-skills-api
- description: List, apply, and dismiss an Agent's improvement suggestions (the suggestions inbox in the Duvo UI)
  name: duvo.ai Suggestions API
  slug: duvoai-suggestions-api
- description: Inspect the team and members associated with the API key
  name: duvo.ai Team API
  slug: duvoai-team-api
- description: Configure event triggers that start a Run automatically when an external event fires (e.g. an email arrives, a Linear issue is created, or a file changes in Google Drive)
  name: duvo.ai Triggers API
  slug: duvoai-triggers-api
artifact_total: 59
asyncapis:
- description: ''
  name: Duvoai Webhooks
  slug: duvoai-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Duvo Public Agent Folders API
  slug: open-duvoai-agent-folders-api
- collection_type: open
  name: Duvo Public Agent Folders Agent Memory API
  slug: open-duvoai-agent-memory-api
- collection_type: open
  name: Duvo Public Agent Folders Agents API
  slug: open-duvoai-agents-api
- collection_type: open
  name: Duvo Public Agent Folders Case Triggers API
  slug: open-duvoai-case-triggers-api
- collection_type: open
  name: Duvo Public Agent Folders Cases API
  slug: open-duvoai-cases-api
- collection_type: open
  name: Duvo Public Agent Folders Clarity API
  slug: open-duvoai-clarity-api
- collection_type: open
  name: Duvo Public Agent Folders ClarityV2 API
  slug: open-duvoai-clarityv2-api
- collection_type: open
  name: Duvo Public Agent Folders Connections API
  slug: open-duvoai-connections-api
- collection_type: open
  name: Duvo Public Agent Folders Credentials API
  slug: open-duvoai-credentials-api
- collection_type: open
  name: Duvo Public Agent Folders Duvo Pulse API
  slug: open-duvoai-duvo-pulse-api
- collection_type: open
  name: Duvo Public Agent Folders Files API
  slug: open-duvoai-files-api
- collection_type: open
  name: Duvo Public Agent Folders Integrations API
  slug: open-duvoai-integrations-api
- collection_type: open
  name: Duvo Public Agent Folders MCP API
  slug: open-duvoai-mcp-api
- collection_type: open
  name: Duvo Public Agent Folders Organizations API
  slug: open-duvoai-organizations-api
- collection_type: open
  name: Duvo Public Agent Folders Plugins API
  slug: open-duvoai-plugins-api
- collection_type: open
  name: Duvo Public Agent Folders Queues API
  slug: open-duvoai-queues-api
- collection_type: open
  name: Duvo Public Agent Folders Revision Integrations API
  slug: open-duvoai-revision-integrations-api
- collection_type: open
  name: Duvo Public Agent Folders Revisions API
  slug: open-duvoai-revisions-api
- collection_type: open
  name: Duvo Public Agent Folders Runs API
  slug: open-duvoai-runs-api
- collection_type: open
  name: Duvo Public Agent Folders Sandboxes API
  slug: open-duvoai-sandboxes-api
- collection_type: open
  name: Duvo Public Agent Folders Schedules API
  slug: open-duvoai-schedules-api
- collection_type: open
  name: Duvo Public Agent Folders Secrets API
  slug: open-duvoai-secrets-api
- collection_type: open
  name: Duvo Public Agent Folders Skills API
  slug: open-duvoai-skills-api
- collection_type: open
  name: Duvo Public Agent Folders Suggestions API
  slug: open-duvoai-suggestions-api
- collection_type: open
  name: Duvo Public Agent Folders Team API
  slug: open-duvoai-team-api
- collection_type: open
  name: Duvo Public Agent Folders Triggers API
  slug: open-duvoai-triggers-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/duvoai-openapi-overlay.yaml
- group: other
  title: ''
  type: AgentCard
  url: a2a/duvoai-a2a.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.duvo.ai/developers
- group: docs
  title: ''
  type: Documentation
  url: https://docs.duvo.ai
- group: docs
  title: ''
  type: APIReference
  url: https://www.duvo.ai/api-reference.md
- group: start
  title: ''
  type: GettingStarted
  url: https://www.duvo.ai/getting-started.md
- group: company
  title: ''
  type: Blog
  url: https://www.duvo.ai/blog
- group: operate
  title: ''
  type: Support
  url: https://www.duvo.ai/contact
- group: commercial
  title: ''
  type: Pricing
  url: https://www.duvo.ai/pricing.md
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.duvo.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.duvo.ai/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/duvoai
- group: auth
  title: ''
  type: Authentication
  url: authentication/duvoai-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/duvoai-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/duvoai-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/duvoai-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/duvoai-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/duvoai-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/duvoai-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/duvoai-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/duvoai-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/duvoai-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/duvoai-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/duvoai-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/duvoai-llms.txt
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/duvoai-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/duvoai-agentic-access.yml
- group: company
  title: ''
  type: Website
  url: https://www.duvo.ai
created: '2026-07-17'
description: Duvo (taskcrew Inc.) is an enterprise process-intelligence and automation platform that captures how work actually happens and turns it into shared process catalogues, role-specific training, improvement plans, transformation roadmaps, SAP migration fact bases, and governed automation across existing systems. Its Public API (api.duvo.ai, v2) lets developers register agent workers, start and inspect agent-backed runs, manage durable queue cases, respond to human approval gates, drive Clarity process capture and Duvo Pulse dashboards, and connect a hosted MCP server. Duvo ships an npm CLI (@duvoai/cli), official agent skills on GitHub, webhooks, and an agent-discovery surface. Duvo is a portfolio company of Index Ventures.
image: https://www.duvo.ai/logo/duvo-logo-icon.svg
layout: provider
mcp_servers:
- description: ''
  name: Duvo MCP
  slug: duvo-mcp
modified: '2026-07-18'
name: duvo.ai
nav: Providers
network: true
overview: 'duvo.ai publishes 26 APIs on the [APIs.io](https://apis.io/) network, including Agent Folders API, Agent Memory API, Agents API, and 23 more. Tagged areas include Company, Ai Ml, Process Intelligence, Automation, and Agents.


  The duvo.ai catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  duvo.ai''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, pricing, authentication, and 22 more developer resources.'
random_paper: 18
scopes:
- name: Duvoai Scopes
  scope_count: 8
  slug: duvoai-scopes
  summary_line: 8 scopes
score:
  band: developing
  composite: 45.9
  coverage:
    artifact_dirs: 24
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.6
  facets:
    access_clarity: 31.6
    commercial_clarity: 31.6
    contract_governance: 4.5
    contract_quality: 63.2
    developer_ergonomics: 71.4
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 10.5
  previous_composite: 46.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 26
    mcp: first-party
    skills: first-party
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/duvoai/refs/heads/main/screenshots/duvoai-2026-07-25T212701.png
security:
- kind: authentication
  name: Duvoai Authentication
  slug: duvoai-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Duvoai Domain Security
  slug: duvoai-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: duvoai
tags:
- Company
- Ai Ml
- Process Intelligence
- Automation
- Agents
- MCP
- Enterprise Operations
- SAP Migration
- Workflows
website: https://www.duvo.ai
---
