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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: true
    error_semantics: documented
    event_surface_described: true
    idempotency: verified
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 52.8
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 51
  human_in_the_loop: 0
  name: Archastro Agentic Access
  operation_count: 89
  slug: archastro-agentic-access
  summary_line: 89 operations · 51 acting
api_count: 10
apis:
- description: The Activity Feed API from Archastro — 1 operation(s) for activity feed.
  name: Archastro Activity Feed API
  slug: archastro-activity-feed-api
- description: The Agents API from Archastro — 17 operation(s) for agents.
  name: Archastro Agents API
  slug: archastro-agents-api
- description: The auth API from Archastro — 9 operation(s) for auth.
  name: Archastro auth API
  slug: archastro-auth-api
- description: The Files API from Archastro — 2 operation(s) for files.
  name: Archastro Files API
  slug: archastro-files-api
- description: The Oauth API from Archastro — 5 operation(s) for oauth.
  name: Archastro Oauth API
  slug: archastro-oauth-api
- description: The s2s API from Archastro — 2 operation(s) for s2s.
  name: Archastro s2s API
  slug: archastro-s2s-api
- description: The Slack Channel Bindings API from Archastro — 2 operation(s) for slack channel bindings.
  name: Archastro Slack Channel Bindings API
  slug: archastro-slack-channel-bindings-api
- description: The Teams API from Archastro — 11 operation(s) for teams.
  name: Archastro Teams API
  slug: archastro-teams-api
- description: The Threads API from Archastro — 10 operation(s) for threads.
  name: Archastro Threads API
  slug: archastro-threads-api
- description: The Users API from Archastro — 7 operation(s) for users.
  name: Archastro Users API
  slug: archastro-users-api
artifact_total: 26
asyncapis:
- description: ''
  name: Archastro Webhooks
  slug: archastro-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: ArchAstro Platform Activity Feed API
  slug: open-archastro-activity-feed-api
- collection_type: open
  name: ArchAstro Platform Activity Feed Agents API
  slug: open-archastro-agents-api
- collection_type: open
  name: ArchAstro Platform Activity Feed auth API
  slug: open-archastro-auth-api
- collection_type: open
  name: ArchAstro Platform Activity Feed Files API
  slug: open-archastro-files-api
- collection_type: open
  name: ArchAstro Platform Activity Feed Oauth API
  slug: open-archastro-oauth-api
- collection_type: open
  name: ArchAstro Platform Activity Feed s2s API
  slug: open-archastro-s2s-api
- collection_type: open
  name: ArchAstro Platform Activity Feed Slack Channel Bindings API
  slug: open-archastro-slack-channel-bindings-api
- collection_type: open
  name: ArchAstro Platform Activity Feed Teams API
  slug: open-archastro-teams-api
- collection_type: open
  name: ArchAstro Platform Activity Feed Threads API
  slug: open-archastro-threads-api
- collection_type: open
  name: ArchAstro Platform Activity Feed Users API
  slug: open-archastro-users-api
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.archastro.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.archastro.ai/docs
- group: docs
  title: ''
  type: APIReference
  url: https://docs.archastro.ai/docs/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.archastro.ai/docs/start-here/getting-started
- group: auth
  title: ''
  type: Authentication
  url: authentication/archastro-authentication.yml
- group: build
  title: ''
  type: SDKs
  url: packages/archastro-packages.yml
- group: build
  title: ''
  type: Packages
  url: packages/archastro-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/archastro-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/archastro-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/archastro-sandbox.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/archastro-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/archastro-llms.txt
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/archastro-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/archastro-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/archastro-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/archastro-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/archastro-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/archastro-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/archastro-conformance.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/archastro-webhooks.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/archastro-platform-overlay.yaml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/archastro-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/archastro-agentic-access.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ArchAstro
- group: commercial
  title: ''
  type: TermsOfService
  url: https://archastro.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://archastro.ai/privacy
- group: company
  title: ''
  type: Website
  url: https://archastro.ai
created: '2026-07-17'
description: 'ArchAstro is a Seattle-area startup building a runtime for cross-company AI agents: privacy-aware agents deployed on both sides of a business relationship that collaborate on integrations, migrations, upgrades, onboarding, testing, and bug fixes, with shared test visibility and human approval gates. The ArchAstro Platform API is an agent-first developer control plane covering users, teams, agents, routines, threads, messages, knowledge, tools, installations, workflows, sandboxes, integrations, and inbound webhooks, with first-party TypeScript and Python SDKs and a CLI. Founded in 2026 by engineering veterans from Microsoft, Stripe, Statsig, and Meta; backed by a $6.2M pre-seed.'
image: https://archastro.ai/og-image.png
layout: provider
mcp_servers:
- description: ''
  name: archastro-mcp.yml
  slug: archastro-mcpyml
modified: '2026-07-18'
name: Archastro
nav: Providers
network: true
overview: 'Archastro publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Activity Feed API, Agents API, auth API, and 7 more. Tagged areas include Company, AI Agents, Agentic, Developer Platform, and Automation.


  The Archastro catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Archastro''s developer surface includes documentation, API reference, getting-started guide, authentication, CLI, sandbox, changelog, and 21 more developer resources.'
random_paper: 1
score:
  band: developing
  composite: 44.9
  delta: -1.1
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 16.7
    contract_quality: 57.5
    developer_ergonomics: 63.7
    discoverability: 81.5
    governance: 16.7
    operational_transparency: 26.3
  previous_composite: 46.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 10
    mcp: derived
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/archastro/refs/heads/main/screenshots/archastro-2026-07-25T201021.png
security:
- kind: authentication
  name: Archastro Authentication
  slug: archastro-authentication
  summary_line: http/apiKey/oauth2 · 3 schemes
- kind: domain-security
  name: Archastro Domain Security
  slug: archastro-domain-security
  summary_line: TLSv1.3
slug: archastro
tags:
- Company
- AI Agents
- Agentic
- Developer Platform
- Automation
- Integration
- MCP
- Workflows
website: https://archastro.ai
---
