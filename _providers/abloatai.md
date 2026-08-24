---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: true
    idempotency: verified
    mcp_server: documented
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 57.3
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 19
  human_in_the_loop: 2
  name: Abloatai Agentic Access
  operation_count: 32
  slug: abloatai-agentic-access
  summary_line: 32 operations · 19 acting · 2 human-in-the-loop
api_count: 8
apis:
- description: A public, anonymous, stateless Streamable-HTTP MCP server Ablo runs on its own domain so an AI coding assistant writing an Ablo integration can search the real docs, inspect the actual SDK export surf
  name: Ablo Integration-Helper MCP Server
  slug: ablo-integration-helper-mcp-server
- description: The branches API from Ablo — 4 operation(s) for branches.
  name: Ablo Branches API
  slug: ablo-branches-api
- description: The claims API from Ablo — 7 operation(s) for claims.
  name: Ablo Claims API
  slug: ablo-claims-api
- description: The commits API from Ablo — 2 operation(s) for commits.
  name: Ablo Commits API
  slug: ablo-commits-api
- description: The credentials API from Ablo — 5 operation(s) for credentials.
  name: Ablo Credentials API
  slug: ablo-credentials-api
- description: The logs API from Ablo — 2 operation(s) for logs.
  name: Ablo Logs API
  slug: ablo-logs-api
- description: The models API from Ablo — 2 operation(s) for models.
  name: Ablo Models API
  slug: ablo-models-api
- description: The schema API from Ablo — 1 operation(s) for schema.
  name: Ablo Schema API
  slug: ablo-schema-api
artifact_total: 16
asyncapis:
- description: ''
  name: Abloatai Webhooks
  slug: abloatai-webhooks
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.abloatai.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.abloatai.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.abloatai.com/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.abloatai.com/quickstart
- group: operate
  title: ''
  type: Support
  url: https://github.com/Abloatai/abloatai/issues
- group: company
  title: ''
  type: Blog
  url: https://www.abloatai.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Abloatai
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/Abloatai/ablo
- group: commercial
  title: ''
  type: Pricing
  url: https://docs.abloatai.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://dashboard.abloatai.com
- group: start
  title: ''
  type: Login
  url: https://dashboard.abloatai.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.abloatai.com/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.abloatai.com/privacy-policy
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/Abloatai/abloatai/blob/main/CHANGELOG.md
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/abloatai-changelog.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.abloatai.com/migration
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/abloatai-lifecycle.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/abloatai-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/abloatai-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/abloatai-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/abloatai-error-codes.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/abloatai-data-model.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/abloatai-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/abloatai-plans-pricing.yml
- group: build
  title: ''
  type: Packages
  url: packages/abloatai-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/abloatai-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/abloatai-cli.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/abloatai-sandbox.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/abloatai-webhooks.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/abloatai-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/abloatai-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/abloatai-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/abloatai-api-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/abloatai-conformance.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/abloatai-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/abloatai-domain-security.yml
created: '2026-08-19'
description: 'Ablo is collaboration infrastructure for AI agents: one API that lets agents, apps and people claim, change and confirm the same database rows without clobbering each other. Rows stay in the customer''s own Postgres — Ablo holds only an ordered transaction log and the coordination state — while durable claims (leases with a wait-line, which make a second writer wait and then hand it the fresh row rather than lock), guarded idempotent writes with stale premises, atomic batch commits and signed webhook delivery turn concurrent multi-agent editing into something that serializes instead of racing. The surface is a 32-operation OpenAPI 3.1 REST API, a WSS realtime stream, a TypeScript SDK and CLI released in lockstep with the API, and two MCP servers.'
image: https://www.abloatai.com/logo-black.svg
layout: provider
mcp_servers:
- description: ''
  name: Ablo MCP Server
  slug: ablo-mcp-server
- description: ''
  name: Ablo MCP Server
  slug: ablo-mcp-server-2
modified: '2026-08-19'
name: Ablo
nav: Providers
network: true
overview: 'Ablo publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Branches API, Claims API, Commits API, and 4 more. Tagged areas include Agent Infrastructure, multi-agent-coordination, concurrency-control, State Management, and Database.


  The Ablo catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Ablo''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 30 more developer resources.'
plans:
- name: Abloatai Plans Pricing
  plan_count: 3
  slug: abloatai-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 6
  name: Abloatai Rate Limits
  slug: abloatai-rate-limits
score:
  band: strong
  composite: 60.5
  delta: -5.9
  facets:
    access_clarity: 63.2
    commercial_clarity: 63.2
    contract_governance: 16.7
    contract_quality: 59.8
    developer_ergonomics: 75.6
    discoverability: 92.6
    governance: 16.7
    operational_transparency: 50.0
  previous_composite: 66.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: first-party
    skills: derived
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: falling
security:
- kind: authentication
  name: Abloatai Authentication
  slug: abloatai-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Abloatai Domain Security
  slug: abloatai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: abloatai
tags:
- Agent Infrastructure
- multi-agent-coordination
- concurrency-control
- State Management
- Database
- Postgres
- real-time-sync
- MCP
- Developer Tools
- backend-infrastructure
website: https://docs.abloatai.com
---
