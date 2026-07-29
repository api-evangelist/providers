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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: derived
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.7
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 64
  human_in_the_loop: 0
  name: Onecli Agentic Access
  operation_count: 116
  slug: onecli-agentic-access
  summary_line: 116 operations · 64 acting
api_count: 24
apis:
- description: Endpoints agents and orchestrators use to bootstrap gateway access (container config, credential stubs, gateway skill).
  name: Onecli Agent Setup API
  slug: onecli-agent-setup-api
- description: Manage agents and their access tokens, secrets, and configuration.
  name: Onecli Agents API
  slug: onecli-agents-api
- description: Long-poll for pending manual-approval requests and submit approve/deny decisions.
  name: Onecli Approvals API
  slug: onecli-approvals-api
- description: Manage app connections (OAuth and direct credentials), BYOC configuration, permission catalogs, and blocklists.
  name: Onecli Apps API
  slug: onecli-apps-api
- description: App connections as a top-level resource.
  name: Onecli Connections API
  slug: onecli-connections-api
- description: Migrate data from a self-hosted instance to OneCLI Cloud.
  name: Onecli Migration API
  slug: onecli-migration-api
- description: Connect apps (OAuth and direct credentials) and manage BYOC app configuration at the organization level. Available on OneCLI Cloud and self-hosted Enterprise.
  name: Onecli Organization App Config API
  slug: onecli-organization-app-config-api
- description: Long-poll for manual-approval requests across every project in the organization. Available on OneCLI Cloud and self-hosted Enterprise.
  name: Onecli Organization Approvals API
  slug: onecli-organization-approvals-api
- description: Manage app connections at the organization level. Available on OneCLI Cloud and self-hosted Enterprise.
  name: Onecli Organization Connections API
  slug: onecli-organization-connections-api
- description: Inspect and detach an organization's partner relationship. Cloud only.
  name: Onecli Organization Partner API
  slug: onecli-organization-partner-api
- description: Manage policy rules at the organization level. Organization rules apply across all projects. Available on OneCLI Cloud and self-hosted Enterprise.
  name: Onecli Organization Rules API
  slug: onecli-organization-rules-api
- description: Manage secrets at the organization level. Organization secrets apply across all projects. Available on OneCLI Cloud and self-hosted Enterprise.
  name: Onecli Organization Secrets API
  slug: onecli-organization-secrets-api
- description: Organization-wide policy settings. Available on OneCLI Cloud and self-hosted Enterprise.
  name: Onecli Organization Settings API
  slug: onecli-organization-settings-api
- description: Cap how much an organization can spend on a partner LLM key. Owner or admin only. Cloud only.
  name: Onecli Partner Budgets API
  slug: onecli-partner-budgets-api
- description: Manage who can sign in to your partner portal. Owner or admin only. Cloud only.
  name: Onecli Partner Members API
  slug: onecli-partner-members-api
- description: Create and manage customer organizations as a partner. Requires a Partner API key. Cloud only.
  name: Onecli Partner Organizations API
  slug: onecli-partner-organizations-api
- description: Manage projects within an unclaimed partner organization. Cloud only.
  name: Onecli Partner Projects API
  slug: onecli-partner-projects-api
- description: Manage partner-level secrets inherited by every organization you manage. Cloud only.
  name: Onecli Partner Secrets API
  slug: onecli-partner-secrets-api
- description: Manage projects within your organization. Requires admin role for create/update and owner role for delete. Cloud only.
  name: Onecli Projects API
  slug: onecli-projects-api
- description: Manage policy rules that control how agents interact with external services.
  name: Onecli Rules API
  slug: onecli-rules-api
- description: Manage credentials that the gateway injects into outbound requests.
  name: Onecli Secrets API
  slug: onecli-secrets-api
- description: Provision team members programmatically. Requires admin role. Cloud only.
  name: Onecli Team API
  slug: onecli-team-api
- description: Manage your user profile and API keys.
  name: Onecli User API
  slug: onecli-user-api
- description: Health check and project resource summaries.
  name: Onecli Utility API
  slug: onecli-utility-api
artifact_total: 28
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/onecli-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/onecli-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/onecli-authentication.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://onecli.sh
- group: docs
  title: ''
  type: Documentation
  url: https://onecli.sh/docs
- group: docs
  title: ''
  type: APIReference
  url: https://onecli.sh/docs/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://onecli.sh/docs/quickstart
- group: commercial
  title: ''
  type: Pricing
  url: https://onecli.sh/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.onecli.sh
- group: commercial
  title: ''
  type: TermsOfService
  url: https://onecli.sh/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://onecli.sh/privacy
- group: company
  title: ''
  type: Blog
  url: https://onecli.sh/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/onecli
- group: operate
  title: ''
  type: Support
  url: https://discord.gg/PSztzsQB3g
- group: build
  title: ''
  type: Packages
  url: packages/onecli-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/onecli-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/onecli-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/onecli-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/onecli-llms.txt
- group: design
  title: ''
  type: Conventions
  url: conventions/onecli-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/onecli-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/onecli-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/onecli-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/onecli-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/onecli-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: OneCLI is an open-source credential gateway and identity layer for AI agents. Agents connect to Gmail, GitHub, Slack, AWS, Jira and 50+ other services through a network-layer proxy that injects real API keys and OAuth tokens at request time, so the agent only ever sees placeholder credential stubs and a compromised or misbehaving agent can never leak secrets. Teams get per-agent access control, policy rules (allow, block, rate-limit, manual approval), a built-in encrypted secrets vault, and full audit logs. The REST API manages agents, secrets, policy rules, and app connections programmatically; OneCLI runs as hosted Cloud or as a self-hosted (Docker) community edition. Founded by ex-Argon Security / Aqua Security engineers and backed by Y Combinator; licensed Apache-2.0.
image: https://onecli.sh/og.png
layout: provider
mcp_servers:
- description: ''
  name: onecli-mcp.yml
  slug: onecli-mcpyml
modified: '2026-07-20'
name: Onecli
nav: Providers
network: true
overview: 'Onecli publishes 24 APIs on the [APIs.io](https://apis.io/) network, including Agent Setup API, Agents API, Approvals API, and 21 more. Tagged areas include Company, Security, Identity, AI Agents, and Secrets Management.


  Onecli''s developer surface includes authentication, documentation, API reference, getting-started guide, pricing, signup flow, engineering blog, and 19 more developer resources.'
random_paper: 67
score:
  band: developing
  composite: 49.9
  delta: -1.5
  facets:
    commercial_clarity: 44.7
    contract_quality: 55.0
    developer_ergonomics: 69.0
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 21.1
  previous_composite: 51.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 24
    mcp: derived
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Onecli Authentication
  slug: onecli-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Onecli Domain Security
  slug: onecli-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: onecli
tags:
- Company
- Security
- Identity
- AI Agents
- Secrets Management
- Credentials
- Gateway
- OAuth
- Developer Tools
- MCP
- Vault
website: https://onecli.sh
---
