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
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: true
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 58.3
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 24
  human_in_the_loop: 5
  name: Gumloop Agentic Access
  operation_count: 49
  slug: gumloop-agentic-access
  summary_line: 49 operations · 24 acting · 5 human-in-the-loop
api_count: 14
apis:
- description: The Agents API from Gumloop — 5 operation(s) for agents.
  name: Gumloop Agents API
  slug: gumloop-agents-api
- description: The Artifacts API from Gumloop — 2 operation(s) for artifacts.
  name: Gumloop Artifacts API
  slug: gumloop-artifacts-api
- description: The Brain API from Gumloop — 1 operation(s) for brain.
  name: Gumloop Brain API
  slug: gumloop-brain-api
- description: The Chat completions API from Gumloop — 1 operation(s) for chat completions.
  name: Gumloop Chat completions API
  slug: gumloop-chat-completions-api
- description: The Data Access API from Gumloop — 5 operation(s) for data access.
  name: Gumloop Data Access API
  slug: gumloop-data-access-api
- description: The Evaluations API from Gumloop — 4 operation(s) for evaluations.
  name: Gumloop Evaluations API
  slug: gumloop-evaluations-api
- description: The Execution API from Gumloop — 2 operation(s) for execution.
  name: Gumloop Execution API
  slug: gumloop-execution-api
- description: The File Handling API from Gumloop — 4 operation(s) for file handling.
  name: Gumloop File Handling API
  slug: gumloop-file-handling-api
- description: The MCP API from Gumloop — 4 operation(s) for mcp.
  name: Gumloop MCP API
  slug: gumloop-mcp-api
- description: The Models API from Gumloop — 1 operation(s) for models.
  name: Gumloop Models API
  slug: gumloop-models-api
- description: The Organization API from Gumloop — 5 operation(s) for organization.
  name: Gumloop Organization API
  slug: gumloop-organization-api
- description: The Sessions API from Gumloop — 4 operation(s) for sessions.
  name: Gumloop Sessions API
  slug: gumloop-sessions-api
- description: The Skills API from Gumloop — 3 operation(s) for skills.
  name: Gumloop Skills API
  slug: gumloop-skills-api
- description: The Teams API from Gumloop — 1 operation(s) for teams.
  name: Gumloop Teams API
  slug: gumloop-teams-api
artifact_total: 21
asyncapis:
- description: ''
  name: Gumloop Webhooks
  slug: gumloop-webhooks
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.gumloop.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.gumloop.com/getting-started/introduction
- group: docs
  title: ''
  type: APIReference
  url: https://docs.gumloop.com/api-reference/getting-started
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.gumloop.com/api-reference/getting-started
- group: auth
  title: ''
  type: Authentication
  url: authentication/gumloop-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/gumloop-scopes.yml
- group: build
  title: ''
  type: Packages
  url: packages/gumloop-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/gumloop-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/gumloop-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/gumloop-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/gumloop-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/gumloop-llms.txt
- group: design
  title: ''
  type: Conventions
  url: conventions/gumloop-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/gumloop-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/gumloop-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/gumloop-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/gumloop-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.gumloop.com
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/gumloop-changelog.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/gumloop-webhooks.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.gumloop.com
- group: auth
  title: ''
  type: DomainSecurity
  url: security/gumloop-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/gumloop-agentic-access.yml
- group: company
  title: ''
  type: Blog
  url: https://gumloop.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://gumloop.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.gumloop.com
- group: operate
  title: ''
  type: Support
  url: mailto:support@gumloop.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://gumloop.com/tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://gumloop.com/privacy-policy
- group: company
  title: ''
  type: Website
  url: https://www.gumloop.com
created: '2026-07-17'
description: Gumloop is an AI-agent automation platform for building, deploying, and governing agents that automate real work — data analysis, customer support, CRM management, and back-office tasks — across tools like Slack, Microsoft Teams, and Gmail. Its public REST API (https://api.gumloop.com/api/v1) exposes 49 operations spanning flow execution, agents and sessions, an OpenAI-compatible chat/completions endpoint, Company Brain search, agent skills, artifacts, MCP server management, evaluations, file handling, teams, and organization administration. Gumloop ships first-party Python and JavaScript SDKs, a `gumloop` CLI, a hosted MCP server for Claude/Cursor/ VS Code, OAuth 2.0 with PKCE, webhook/schedule/event triggers, and enterprise controls (SSO/SAML/SCIM, audit logging, app policies).
image: https://gumloop.com/images/link-preview.webp
layout: provider
mcp_servers:
- description: ''
  name: gumloop-mcp.yml
  slug: gumloop-mcpyml
modified: '2026-07-19'
name: Gumloop
nav: Providers
network: true
overview: 'Gumloop publishes 14 APIs on the [APIs.io](https://apis.io/) network, including Agents API, Artifacts API, Brain API, and 11 more. Tagged areas include Company, Artificial Intelligence, AI Agents, Automation, and Workflow Automation.


  The Gumloop catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Gumloop''s developer surface includes documentation, API reference, getting-started guide, authentication, CLI, changelog, engineering blog, and 24 more developer resources.'
random_paper: 42
scopes:
- name: Gumloop Scopes
  scope_count: 5
  slug: gumloop-scopes
  summary_line: 5 scopes · authorizationCode
score:
  band: strong
  composite: 58.4
  delta: 0.0
  facets:
    commercial_clarity: 52.6
    contract_quality: 67.9
    developer_ergonomics: 75.5
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 39.5
  previous_composite: 58.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 14
    mcp: first-party
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/gumloop/refs/heads/main/screenshots/gumloop-2026-07-25T220434.png
security:
- kind: authentication
  name: Gumloop Authentication
  slug: gumloop-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Gumloop Domain Security
  slug: gumloop-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Gumloop Trust Center
  slug: gumloop-trust-center
  summary_line: trust center published
slug: gumloop
tags:
- Company
- Artificial Intelligence
- AI Agents
- Automation
- Workflow Automation
- Agent Platform
- MCP
- LLM
- No-Code
- Developer Tools
website: https://www.gumloop.com
---
