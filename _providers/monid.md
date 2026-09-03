---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 56.5
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 9
  human_in_the_loop: 3
  name: Monid Agentic Access
  operation_count: 33
  slug: monid-agentic-access
  summary_line: 33 operations · 9 acting · 3 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.monid.ai
  baseurl_source: declared
  description: The API Keys API from Monid — 2 operation(s) for api keys.
  name: Monid API Keys API
  slug: monid-api-keys-api
- baseURL: https://api.monid.ai
  baseurl_source: declared
  description: The Auth API from Monid — 2 operation(s) for auth.
  name: Monid Auth API
  slug: monid-auth-api
- baseURL: https://api.monid.ai
  baseurl_source: declared
  description: The Controls API from Monid — 6 operation(s) for controls.
  name: Monid Controls API
  slug: monid-controls-api
- baseURL: https://api.monid.ai
  baseurl_source: declared
  description: The Discover API from Monid — 1 operation(s) for discover.
  name: Monid Discover API
  slug: monid-discover-api
- baseURL: https://api.monid.ai
  baseurl_source: declared
  description: The Endpoints API from Monid — 1 operation(s) for endpoints.
  name: Monid Endpoints API
  slug: monid-endpoints-api
- baseURL: https://api.monid.ai
  baseurl_source: declared
  description: The Inspect API from Monid — 1 operation(s) for inspect.
  name: Monid Inspect API
  slug: monid-inspect-api
- baseURL: https://api.monid.ai
  baseurl_source: declared
  description: The Public Registry API from Monid — 5 operation(s) for public registry.
  name: Monid Public Registry API
  slug: monid-public-registry-api
- baseURL: https://api.monid.ai
  baseurl_source: declared
  description: The Resources API from Monid — 5 operation(s) for resources.
  name: Monid Resources API
  slug: monid-resources-api
- baseURL: https://api.monid.ai
  baseurl_source: declared
  description: The Runs API from Monid — 5 operation(s) for runs.
  name: Monid Runs API
  slug: monid-runs-api
- baseURL: https://api.monid.ai
  baseurl_source: declared
  description: The Wallet API from Monid — 2 operation(s) for wallet.
  name: Monid Wallet API
  slug: monid-wallet-api
artifact_total: 16
collections:
- collection_type: open
  name: Monid API
  slug: open-monid
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/monid-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/monid-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/monid-scopes.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/monid-domain-security.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/monid-mcp.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/monid-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/monid-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/monid-conformance.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/monid-well-known.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/monid-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.monid.ai
- group: design
  title: ''
  type: DataModel
  url: data-model/monid-data-model.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/monid-openapi-overlay.yaml
- group: build
  title: ''
  type: Packages
  url: packages/monid-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/monid-cli.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/monid-llms.txt
- group: company
  title: ''
  type: Website
  url: https://monid.ai
- group: start
  title: ''
  type: DeveloperPortal
  url: https://monid.ai/docs
- group: docs
  title: ''
  type: Documentation
  url: https://monid.ai/docs
- group: docs
  title: ''
  type: APIReference
  url: https://monid.ai/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://monid.ai/docs/guide/quickstart-api.md
- group: company
  title: ''
  type: Blog
  url: https://monid.ai/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/monid-ai
- group: start
  title: ''
  type: SignUp
  url: https://app.monid.ai
created: 2026-07-23
description: Monid is a San Francisco-based data-access and agent-tool integration platform that gives developers and AI agents on-demand, pay-per-use access to hundreds of web data endpoints and 1,300+ tools across 13+ providers (Semrush, Apollo, ElevenLabs, web scrapers, and more) through a single integration. Agents discover, inspect, compare, and execute tools at runtime and pay only for actual usage, with a unified balance and no per-tool API key management or subscriptions. Monid exposes its catalog through four connection methods — an MCP (Model Context Protocol) server for Claude and other AI assistants, a Skill integration for Claude Code and Cursor, a CLI for shell access, and an HTTP API for programmatic integration — with OAuth, proxy, and master API key options for embedded use.
layout: provider
mcp_servers:
- description: Official hosted Monid MCP server (Streamable HTTP). Gives an AI client tools to discover, inspect, and run hundreds of data endpoints across the web, with pay-per-use billing against a Monid workspace
  name: Monid MCP Server
  slug: monid-mcp-server
modified: 2026-07-23
name: Monid
nav: Providers
network: true
overview: 'Monid publishes 10 APIs on the [APIs.io](https://apis.io/) network, including API Keys API, Auth API, Controls API, and 7 more. Tagged areas include Company, Agents, MCP, Tools, and Data.


  Monid''s developer surface includes authentication, CLI, documentation, API reference, getting-started guide, engineering blog, signup flow, and 18 more developer resources.'
random_paper: 10
scopes:
- name: Monid Scopes
  scope_count: 5
  slug: monid-scopes
  summary_line: 5 scopes · authorizationCode
score:
  band: thin
  composite: 36.3
  coverage:
    artifact_dirs: 20
    catalog_gap: 80.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 18.2
    contract_quality: 52.7
    developer_ergonomics: 66.7
    discoverability: 72.2
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 36.3
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
    mcp: first-party
    skills: first-party
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/monid/refs/heads/main/screenshots/monid-2026-08-07T184201.png
security:
- kind: authentication
  name: Monid Authentication
  slug: monid-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Monid Domain Security
  slug: monid-domain-security
  summary_line: TLSv1.3 · DNSSEC
slug: monid
tags:
- Company
- Agents
- MCP
- Tools
- Data
- API Marketplace
website: https://monid.ai
---
