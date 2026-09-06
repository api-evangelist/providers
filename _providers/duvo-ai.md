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
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: true
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: true
    idempotency: documented
    mcp_server: verified
    openapi_examples: partial
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 63.1
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 124
  human_in_the_loop: 7
  name: Duvo Ai Agentic Access
  operation_count: 213
  slug: duvo-ai-agentic-access
  summary_line: 213 operations · 124 acting · 7 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.duvo.ai
  baseurl_source: declared
  description: Organize agents into folders
  name: Duvo Ai Agent Folders API
  slug: duvo-ai-agent-folders-api
- baseURL: https://api.duvo.ai
  baseurl_source: declared
  description: Read an agent's memory files (the Memory feature in the Duvo UI)
  name: Duvo Ai Agent Memory API
  slug: duvo-ai-agent-memory-api
- baseURL: https://api.duvo.ai
  baseurl_source: declared
  description: Create and manage agents for automation workloads
  name: Duvo Ai Agents API
  slug: duvo-ai-agents-api
- baseURL: https://api.duvo.ai
  baseurl_source: declared
  description: Configure case triggers that automatically dispatch agent runs (Runs in the Duvo UI) for cases added to a queue
  name: Duvo Ai Case Triggers API
  slug: duvo-ai-case-triggers-api
- baseURL: https://api.duvo.ai
  baseurl_source: declared
  description: Create, list, and manage cases and their labels within queues
  name: Duvo Ai Cases API
  slug: duvo-ai-cases-api
- baseURL: https://api.duvo.ai
  baseurl_source: declared
  description: The Clarity API from Duvo Ai — 17 operation(s) for clarity.
  name: Duvo Ai Clarity API
  slug: duvo-ai-clarity-api
- baseURL: https://api.duvo.ai
  baseurl_source: declared
  description: Manage Clarity v2 process snapshots, transformation proposals, and the extra-capture-request follow-up loop
  name: Duvo Ai ClarityV2 API
  slug: duvo-ai-clarityv2-api
- baseURL: https://api.duvo.ai
  baseurl_source: declared
  description: Manage your connected integrations
  name: Duvo Ai Connections API
  slug: duvo-ai-connections-api
- baseURL: https://api.duvo.ai
  baseurl_source: declared
  description: Manage logins (domain + username + password + TOTP) used by agents to sign in to websites and desktop applications, and attach them to assignment revisions
  name: Duvo Ai Credentials API
  slug: duvo-ai-credentials-api
- baseURL: https://api.duvo.ai
  baseurl_source: declared
  description: Create, list, iterate on, and delete Duvo Pulse dashboards — live, agent-generated visualizations of your Duvo data
  name: Duvo Ai Duvo Pulse API
  slug: duvo-ai-duvo-pulse-api
- baseURL: https://api.duvo.ai
  baseurl_source: declared
  description: Manage team files.
  name: Duvo Ai Files API
  slug: duvo-ai-files-api
- baseURL: https://api.duvo.ai
  baseurl_source: declared
  description: Browse the team's catalog of available integration types
  name: Duvo Ai Integrations API
  slug: duvo-ai-integrations-api
- baseURL: https://api.duvo.ai
  baseurl_source: declared
  description: MCP JSON-RPC endpoint exposing public API routes as LLM-callable tools
  name: Duvo Ai MCP API
  slug: duvo-ai-mcp-api
- baseURL: https://api.duvo.ai
  baseurl_source: declared
  description: Inspect organizations you belong to and the teams within them
  name: Duvo Ai Organizations API
  slug: duvo-ai-organizations-api
- baseURL: https://api.duvo.ai
  baseurl_source: declared
  description: Discover plugins that can be referenced from a revision.
  name: Duvo Ai Plugins API
  slug: duvo-ai-plugins-api
- baseURL: https://api.duvo.ai
  baseurl_source: declared
  description: Manage queues and their agent bindings
  name: Duvo Ai Queues API
  slug: duvo-ai-queues-api
- baseURL: https://api.duvo.ai
  baseurl_source: declared
  description: Attach integrations to assignment revisions, pin specific connections, and link queues
  name: Duvo Ai Revision Integrations API
  slug: duvo-ai-revision-integrations-api
- baseURL: https://api.duvo.ai
  baseurl_source: declared
  description: Create and manage agent revisions — the underlying Setup for an Agent
  name: Duvo Ai Revisions API
  slug: duvo-ai-revisions-api
- baseURL: https://api.duvo.ai
  baseurl_source: declared
  description: Start, monitor, and manage agent runs (Runs in the Duvo UI)
  name: Duvo Ai Runs API
  slug: duvo-ai-runs-api
- baseURL: https://api.duvo.ai
  baseurl_source: declared
  description: Create sandboxes and upload files for agent runs
  name: Duvo Ai Sandboxes API
  slug: duvo-ai-sandboxes-api
- baseURL: https://api.duvo.ai
  baseurl_source: declared
  description: List schedules configured for an agent
  name: Duvo Ai Schedules API
  slug: duvo-ai-schedules-api
- baseURL: https://api.duvo.ai
  baseurl_source: declared
  description: Manage env-var secrets injected into runs, and attach them to assignment revisions. Only metadata is exposed; values are never returned
  name: Duvo Ai Secrets API
  slug: duvo-ai-secrets-api
- baseURL: https://api.duvo.ai
  baseurl_source: declared
  description: Manage team and system skills (reusable knowledge packs).
  name: Duvo Ai Skills API
  slug: duvo-ai-skills-api
- baseURL: https://api.duvo.ai
  baseurl_source: declared
  description: List, apply, and dismiss an Agent's improvement suggestions (the suggestions inbox in the Duvo UI)
  name: Duvo Ai Suggestions API
  slug: duvo-ai-suggestions-api
- baseURL: https://api.duvo.ai
  baseurl_source: declared
  description: Inspect the team and members associated with the API key
  name: Duvo Ai Team API
  slug: duvo-ai-team-api
- baseURL: https://api.duvo.ai
  baseurl_source: declared
  description: Configure event triggers that start a Run automatically when an external event fires (e.g. an email arrives, a Linear issue is created, or a file changes in Google Drive)
  name: Duvo Ai Triggers API
  slug: duvo-ai-triggers-api
- baseURL: https://api.duvo.ai
  baseurl_source: declared
  description: Organize agents into folders
  name: duvo.ai Agent Folders API
  slug: duvoai-agent-folders-api
- baseURL: https://api.duvo.ai
  baseurl_source: declared
  description: Read an agent's memory files (the Memory feature in the Duvo UI)
  name: duvo.ai Agent Memory API
  slug: duvoai-agent-memory-api
- baseURL: https://api.duvo.ai
  baseurl_source: declared
  description: Create and manage agents for automation workloads
  name: duvo.ai Agents API
  slug: duvoai-agents-api
- baseURL: https://api.duvo.ai
  baseurl_source: declared
  description: Configure case triggers that automatically dispatch agent runs (Runs in the Duvo UI) for cases added to a queue
  name: duvo.ai Case Triggers API
  slug: duvoai-case-triggers-api
- baseURL: https://api.duvo.ai
  baseurl_source: declared
  description: Create, list, and manage cases and their labels within queues
  name: duvo.ai Cases API
  slug: duvoai-cases-api
- baseURL: https://api.duvo.ai
  baseurl_source: declared
  description: The Clarity API from duvo.ai — 17 operation(s) for clarity.
  name: duvo.ai Clarity API
  slug: duvoai-clarity-api
- baseURL: https://api.duvo.ai
  baseurl_source: declared
  description: Manage Clarity v2 process snapshots, transformation proposals, and the extra-capture-request follow-up loop
  name: duvo.ai ClarityV2 API
  slug: duvoai-clarityv2-api
- baseURL: https://api.duvo.ai
  baseurl_source: declared
  description: Manage your connected integrations
  name: duvo.ai Connections API
  slug: duvoai-connections-api
- baseURL: https://api.duvo.ai
  baseurl_source: declared
  description: Manage logins (domain + username + password + TOTP) used by agents to sign in to websites and desktop applications, and attach them to assignment revisions
  name: duvo.ai Credentials API
  slug: duvoai-credentials-api
- baseURL: https://api.duvo.ai
  baseurl_source: declared
  description: Create, list, iterate on, and delete Duvo Pulse dashboards — live, agent-generated visualizations of your Duvo data
  name: duvo.ai Duvo Pulse API
  slug: duvoai-duvo-pulse-api
- baseURL: https://api.duvo.ai
  baseurl_source: declared
  description: Manage team files.
  name: duvo.ai Files API
  slug: duvoai-files-api
- baseURL: https://api.duvo.ai
  baseurl_source: declared
  description: Browse the team's catalog of available integration types
  name: duvo.ai Integrations API
  slug: duvoai-integrations-api
- baseURL: https://api.duvo.ai
  baseurl_source: declared
  description: MCP JSON-RPC endpoint exposing public API routes as LLM-callable tools
  name: duvo.ai MCP API
  slug: duvoai-mcp-api
- baseURL: https://api.duvo.ai
  baseurl_source: declared
  description: Inspect organizations you belong to and the teams within them
  name: duvo.ai Organizations API
  slug: duvoai-organizations-api
- baseURL: https://api.duvo.ai
  baseurl_source: declared
  description: Discover plugins that can be referenced from a revision.
  name: duvo.ai Plugins API
  slug: duvoai-plugins-api
- baseURL: https://api.duvo.ai
  baseurl_source: declared
  description: Manage queues and their agent bindings
  name: duvo.ai Queues API
  slug: duvoai-queues-api
- baseURL: https://api.duvo.ai
  baseurl_source: declared
  description: Attach integrations to assignment revisions, pin specific connections, and link queues
  name: duvo.ai Revision Integrations API
  slug: duvoai-revision-integrations-api
- baseURL: https://api.duvo.ai
  baseurl_source: declared
  description: Create and manage agent revisions — the underlying Setup for an Agent
  name: duvo.ai Revisions API
  slug: duvoai-revisions-api
- baseURL: https://api.duvo.ai
  baseurl_source: declared
  description: Start, monitor, and manage agent runs (Runs in the Duvo UI)
  name: duvo.ai Runs API
  slug: duvoai-runs-api
- baseURL: https://api.duvo.ai
  baseurl_source: declared
  description: Create sandboxes and upload files for agent runs
  name: duvo.ai Sandboxes API
  slug: duvoai-sandboxes-api
- baseURL: https://api.duvo.ai
  baseurl_source: declared
  description: List schedules configured for an agent
  name: duvo.ai Schedules API
  slug: duvoai-schedules-api
- baseURL: https://api.duvo.ai
  baseurl_source: declared
  description: Manage env-var secrets injected into runs, and attach them to assignment revisions. Only metadata is exposed; values are never returned
  name: duvo.ai Secrets API
  slug: duvoai-secrets-api
- baseURL: https://api.duvo.ai
  baseurl_source: declared
  description: Manage team and system skills (reusable knowledge packs).
  name: duvo.ai Skills API
  slug: duvoai-skills-api
- baseURL: https://api.duvo.ai
  baseurl_source: declared
  description: List, apply, and dismiss an Agent's improvement suggestions (the suggestions inbox in the Duvo UI)
  name: duvo.ai Suggestions API
  slug: duvoai-suggestions-api
- baseURL: https://api.duvo.ai
  baseurl_source: declared
  description: Inspect the team and members associated with the API key
  name: duvo.ai Team API
  slug: duvoai-team-api
- baseURL: https://api.duvo.ai
  baseurl_source: declared
  description: Configure event triggers that start a Run automatically when an external event fires (e.g. an email arrives, a Linear issue is created, or a file changes in Google Drive)
  name: duvo.ai Triggers API
  slug: duvoai-triggers-api
artifact_total: 85
asyncapis:
- description: ''
  name: Duvo Ai Webhooks
  slug: duvo-ai-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Duvo Public Agent Folders API
  slug: open-duvo-ai-agent-folders-api
- collection_type: open
  name: Duvo Public Agent Folders Agent Memory API
  slug: open-duvo-ai-agent-memory-api
- collection_type: open
  name: Duvo Public Agent Folders Agents API
  slug: open-duvo-ai-agents-api
- collection_type: open
  name: Duvo Public Agent Folders Case Triggers API
  slug: open-duvo-ai-case-triggers-api
- collection_type: open
  name: Duvo Public Agent Folders Cases API
  slug: open-duvo-ai-cases-api
- collection_type: open
  name: Duvo Public Agent Folders Clarity API
  slug: open-duvo-ai-clarity-api
- collection_type: open
  name: Duvo Public Agent Folders ClarityV2 API
  slug: open-duvo-ai-clarityv2-api
- collection_type: open
  name: Duvo Public Agent Folders Connections API
  slug: open-duvo-ai-connections-api
- collection_type: open
  name: Duvo Public Agent Folders Credentials API
  slug: open-duvo-ai-credentials-api
- collection_type: open
  name: Duvo Public Agent Folders Duvo Pulse API
  slug: open-duvo-ai-duvo-pulse-api
- collection_type: open
  name: Duvo Public Agent Folders Files API
  slug: open-duvo-ai-files-api
- collection_type: open
  name: Duvo Public Agent Folders Integrations API
  slug: open-duvo-ai-integrations-api
- collection_type: open
  name: Duvo Public Agent Folders MCP API
  slug: open-duvo-ai-mcp-api
- collection_type: open
  name: Duvo Public Agent Folders Organizations API
  slug: open-duvo-ai-organizations-api
- collection_type: open
  name: Duvo Public Agent Folders Plugins API
  slug: open-duvo-ai-plugins-api
- collection_type: open
  name: Duvo Public Agent Folders Queues API
  slug: open-duvo-ai-queues-api
- collection_type: open
  name: Duvo Public Agent Folders Revision Integrations API
  slug: open-duvo-ai-revision-integrations-api
- collection_type: open
  name: Duvo Public Agent Folders Revisions API
  slug: open-duvo-ai-revisions-api
- collection_type: open
  name: Duvo Public Agent Folders Runs API
  slug: open-duvo-ai-runs-api
- collection_type: open
  name: Duvo Public Agent Folders Sandboxes API
  slug: open-duvo-ai-sandboxes-api
- collection_type: open
  name: Duvo Public Agent Folders Schedules API
  slug: open-duvo-ai-schedules-api
- collection_type: open
  name: Duvo Public Agent Folders Secrets API
  slug: open-duvo-ai-secrets-api
- collection_type: open
  name: Duvo Public Agent Folders Skills API
  slug: open-duvo-ai-skills-api
- collection_type: open
  name: Duvo Public Agent Folders Suggestions API
  slug: open-duvo-ai-suggestions-api
- collection_type: open
  name: Duvo Public Agent Folders Team API
  slug: open-duvo-ai-team-api
- collection_type: open
  name: Duvo Public Agent Folders Triggers API
  slug: open-duvo-ai-triggers-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/duvo-ai-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/duvo-ai-openapi-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/duvo-ai-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/duvo-ai-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/duvo-ai-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/duvo-ai-scopes.yml
- group: build
  title: ''
  type: Packages
  url: packages/duvo-ai-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/duvo-ai-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/duvo-ai-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/duvo-ai-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/duvo-ai-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/duvo-ai-llms.txt
- group: design
  title: ''
  type: Conventions
  url: conventions/duvo-ai-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/duvo-ai-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/duvo-ai-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/duvo-ai-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/duvo-ai-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/duvo-ai-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/duvo-ai-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
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
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/duvoai
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
  url: https://www.duvo.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.duvo.ai/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.duvo.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.duvo.ai/privacy
- group: company
  title: ''
  type: Website
  url: https://www.duvo.ai
created: '2026-07-17'
description: Duvo (taskcrew Inc.) is a process intelligence and automation platform that captures how work really happens, reveals improvement and transformation opportunities, and delivers reliable governed automation across existing enterprise systems. It builds evidence-backed process catalogues, role-specific training, improvement plans, transformation roadmaps, and SAP migration fact bases, then runs cross-system operational workflows — purchase orders, invoice matching, inventory exceptions, supplier onboarding, master data — through agents, queues, human approvals, files, webhooks, and browser automation. Duvo exposes a 213-operation workspace-scoped public API (api.duvo.ai), a hosted MCP server, an official CLI, agent skills, and a full agent-native discovery surface (.well-known agent + MCP cards, llms.txt). Backed by Northzone.
image: https://www.duvo.ai/logo/duvo-logo-icon.svg
layout: provider
mcp_servers:
- description: ''
  name: Duvo MCP
  slug: duvo-mcp
modified: '2026-07-18'
name: Duvo Ai
nav: Providers
network: true
overview: 'Duvo Ai publishes 52 APIs on the [APIs.io](https://apis.io/) network, including Agent Folders API, Agent Memory API, Agents API, and 49 more. Tagged areas include Company, Enterprise AI, Process Intelligence, Automation, and Agents.


  The Duvo Ai catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Duvo Ai''s developer surface includes authentication, CLI, documentation, API reference, getting-started guide, engineering blog, support, and 25 more developer resources.'
random_paper: 0
scopes:
- name: Duvo Ai Scopes
  scope_count: 8
  slug: duvo-ai-scopes
  summary_line: 8 scopes
score:
  band: developing
  composite: 47.4
  coverage:
    artifact_dirs: 25
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 38.2
    commercial_clarity: 38.2
    contract_governance: 4.5
    contract_quality: 62.4
    developer_ergonomics: 73.2
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 10.5
  previous_composite: 47.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 52
    mcp: first-party
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/duvo-ai/refs/heads/main/screenshots/duvo-ai-2026-07-25T212653.png
security:
- kind: authentication
  name: Duvo Ai Authentication
  slug: duvo-ai-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Duvo Ai Domain Security
  slug: duvo-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: duvo-ai
tags:
- Company
- Enterprise AI
- Process Intelligence
- Automation
- Agents
- SAP Migration
- ERP
- Transformation
- Approvals
- Audit
- MCP
website: https://www.duvo.ai
---
