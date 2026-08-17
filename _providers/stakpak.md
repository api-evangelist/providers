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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 46.6
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 52
  human_in_the_loop: 1
  name: Stakpak Agentic Access
  operation_count: 99
  slug: stakpak-agentic-access
  summary_line: 99 operations · 52 acting · 1 human-in-the-loop
api_count: 20
apis:
- description: Account API
  name: StakPak Account API
  slug: stakpak-account-api
- description: The Account (V2) API from StakPak — 2 operation(s) for account (v2).
  name: StakPak Account (V2) API
  slug: stakpak-account-v2-api
- description: Agents API
  name: StakPak Agents API
  slug: stakpak-agents-api
- description: The Agents (V2) API from StakPak — 2 operation(s) for agents (v2).
  name: StakPak Agents (V2) API
  slug: stakpak-agents-v2-api
- description: The Billing (V2) API from StakPak — 6 operation(s) for billing (v2).
  name: StakPak Billing (V2) API
  slug: stakpak-billing-v2-api
- description: The Chat API from StakPak — 2 operation(s) for chat.
  name: StakPak Chat API
  slug: stakpak-chat-api
- description: The Commands API from StakPak — 1 operation(s) for commands.
  name: StakPak Commands API
  slug: stakpak-commands-api
- description: The Knowledge API from StakPak — 2 operation(s) for knowledge.
  name: StakPak Knowledge API
  slug: stakpak-knowledge-api
- description: The Knowledge Registry API from StakPak — 5 operation(s) for knowledge registry.
  name: StakPak Knowledge Registry API
  slug: stakpak-knowledge-registry-api
- description: The MCP API from StakPak — 1 operation(s) for mcp.
  name: StakPak MCP API
  slug: stakpak-mcp-api
- description: The Memory API from StakPak — 2 operation(s) for memory.
  name: StakPak Memory API
  slug: stakpak-memory-api
- description: The Memory (V2) API from StakPak — 2 operation(s) for memory (v2).
  name: StakPak Memory (V2) API
  slug: stakpak-memory-v2-api
- description: The Organizations API from StakPak — 11 operation(s) for organizations.
  name: StakPak Organizations API
  slug: stakpak-organizations-api
- description: The Recovery API from StakPak — 3 operation(s) for recovery.
  name: StakPak Recovery API
  slug: stakpak-recovery-api
- description: Rules API
  name: StakPak Rules API
  slug: stakpak-rules-api
- description: The Rules (V2) API from StakPak — 5 operation(s) for rules (v2).
  name: StakPak Rules (V2) API
  slug: stakpak-rules-v2-api
- description: The Runners (V2) API from StakPak — 6 operation(s) for runners (v2).
  name: StakPak Runners (V2) API
  slug: stakpak-runners-v2-api
- description: The Sessions API from StakPak — 4 operation(s) for sessions.
  name: StakPak Sessions API
  slug: stakpak-sessions-api
- description: The Telemetry API from StakPak — 1 operation(s) for telemetry.
  name: StakPak Telemetry API
  slug: stakpak-telemetry-api
- description: The Upload API from StakPak — 1 operation(s) for upload.
  name: StakPak Upload API
  slug: stakpak-upload-api
artifact_total: 45
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Stakpak Account API
  slug: open-stakpak-account-api
- collection_type: open
  name: Stakpak Account Account (V2) API
  slug: open-stakpak-account-v2-api
- collection_type: open
  name: Stakpak Account Agents API
  slug: open-stakpak-agents-api
- collection_type: open
  name: Stakpak Account Agents (V2) API
  slug: open-stakpak-agents-v2-api
- collection_type: open
  name: Stakpak Account Billing (V2) API
  slug: open-stakpak-billing-v2-api
- collection_type: open
  name: Stakpak Account Chat API
  slug: open-stakpak-chat-api
- collection_type: open
  name: Stakpak Account Commands API
  slug: open-stakpak-commands-api
- collection_type: open
  name: Stakpak Account Knowledge API
  slug: open-stakpak-knowledge-api
- collection_type: open
  name: Stakpak Account Knowledge Registry API
  slug: open-stakpak-knowledge-registry-api
- collection_type: open
  name: Stakpak Account MCP API
  slug: open-stakpak-mcp-api
- collection_type: open
  name: Stakpak Account Memory API
  slug: open-stakpak-memory-api
- collection_type: open
  name: Stakpak Account Memory (V2) API
  slug: open-stakpak-memory-v2-api
- collection_type: open
  name: Stakpak Account Organizations API
  slug: open-stakpak-organizations-api
- collection_type: open
  name: Stakpak Account Recovery API
  slug: open-stakpak-recovery-api
- collection_type: open
  name: Stakpak Account Rules API
  slug: open-stakpak-rules-api
- collection_type: open
  name: Stakpak Account Rules (V2) API
  slug: open-stakpak-rules-v2-api
- collection_type: open
  name: Stakpak Account Runners (V2) API
  slug: open-stakpak-runners-v2-api
- collection_type: open
  name: Stakpak Account Sessions API
  slug: open-stakpak-sessions-api
- collection_type: open
  name: Stakpak Account Telemetry API
  slug: open-stakpak-telemetry-api
- collection_type: open
  name: Stakpak Account Upload API
  slug: open-stakpak-upload-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/stakpak-openapi-overlay.yaml
- group: commercial
  title: ''
  type: License
  url: https://github.com/stakpak/agent/blob/main/LICENSE
- group: start
  title: ''
  type: DeveloperPortal
  url: https://stakpak.dev
- group: docs
  title: ''
  type: Documentation
  url: https://stakpak.gitbook.io/docs
- group: docs
  title: ''
  type: APIReference
  url: https://apiv2.stakpak.dev/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://stakpak.gitbook.io/docs/get-started/install-stakpak
- group: commercial
  title: ''
  type: Pricing
  url: https://stakpak.gitbook.io/docs/get-started/oss-vs-cloud-vs-enterprise
- group: start
  title: ''
  type: SignUp
  url: https://stakpak.dev
- group: operate
  title: ''
  type: Support
  url: https://discord.gg/QTZjETP7GB
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/stakpak
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/stakpak/agent
- group: build
  title: ''
  type: Packages
  url: packages/stakpak-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/stakpak-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/stakpak-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/stakpak-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/stakpak-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/stakpak-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/stakpak-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/stakpak-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/stakpak-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/stakpak-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/stakpak-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://stakpak.dev
created: '2026-07-17'
description: Stakpak is an open-source autonomous DevOps AI agent, distributed as a single Rust binary, that runs 24/7 on your machines to keep applications running — performing health checks, auto-healing failures, monitoring cloud cost, rotating secrets, renewing certificates, and alerting teams only when human intervention is needed ("all the upside of a PaaS, none of the lock-in"). It ships as a CLI with an interactive TUI, an autopilot daemon, an MCP server, and an ACP endpoint, backed by a hosted REST API (apiv2.stakpak.dev) covering accounts, organizations, agent sessions and checkpoints, a knowledge/memory store, rulebooks, the Paks knowledge registry, and an OpenAI-compatible chat-completion endpoint. Surfaced originally as a 500 Global portfolio company.
image: https://stakpak.dev/favicon.png
layout: provider
mcp_servers:
- description: ''
  name: stakpak-mcp.yml
  slug: stakpak-mcpyml
modified: '2026-07-21'
name: StakPak
nav: Providers
network: true
overview: 'StakPak publishes 20 APIs on the [APIs.io](https://apis.io/) network, including Account API, Account (V2) API, Agents API, and 17 more. Tagged areas include Company, DevOps, Infrastructure, AI Agents, and MCP.


  StakPak''s developer surface includes documentation, API reference, getting-started guide, pricing, signup flow, support, CLI, and 17 more developer resources.'
random_paper: 6
score:
  band: developing
  composite: 45.0
  delta: 0.0
  facets:
    commercial_clarity: 23.7
    contract_quality: 53.2
    developer_ergonomics: 73.4
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 21.1
  previous_composite: 45.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 20
    mcp: first-party
    skills: derived
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
security:
- kind: authentication
  name: Stakpak Authentication
  slug: stakpak-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Stakpak Domain Security
  slug: stakpak-domain-security
  summary_line: TLSv1.3 · DMARC
slug: stakpak
tags:
- Company
- DevOps
- Infrastructure
- AI Agents
- MCP
- Developer Tools
- CLI
- Cloud
website: https://stakpak.dev
---
