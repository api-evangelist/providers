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
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 47.7
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Sourcebot Agentic Access
  operation_count: 17
  slug: sourcebot-agentic-access
  summary_line: 17 operations · 5 acting
api_count: 1
apis:
- description: Enterprise endpoints for user management and audit logging.
  name: Sourcebot Enterprise (EE) API
  slug: sourcebot-enterprise-ee-api
- description: Git history, diff, and file content endpoints.
  name: Sourcebot Git API
  slug: sourcebot-git-api
- description: Repository listing and metadata endpoints.
  name: Sourcebot Repositories API
  slug: sourcebot-repositories-api
- description: Code search and symbol navigation endpoints.
  name: Sourcebot Search & Navigation API
  slug: sourcebot-search-navigation-api
- description: System health and version endpoints.
  name: Sourcebot System API
  slug: sourcebot-system-api
artifact_total: 15
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Sourcebot Public Enterprise (EE) Enterprise (EE) Enterprise (EE) API
  slug: open-sourcebot-enterprise-ee-api
- collection_type: open
  name: Sourcebot Public Enterprise (EE) Enterprise (EE) Git API
  slug: open-sourcebot-git-api
- collection_type: open
  name: Sourcebot Public Enterprise (EE) Enterprise (EE) Repositories API
  slug: open-sourcebot-repositories-api
- collection_type: open
  name: Sourcebot Public Enterprise (EE) Enterprise (EE) Search & Navigation API
  slug: open-sourcebot-search-navigation-api
- collection_type: open
  name: Sourcebot Public Enterprise (EE) Enterprise (EE) System API
  slug: open-sourcebot-system-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/sourcebot-public-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/sourcebot-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sourcebot-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.sourcebot.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.sourcebot.dev/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.sourcebot.dev/api-reference/search-&-navigation/search-code
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.sourcebot.dev/docs/deployment/deploy-sourcebot
- group: start
  title: ''
  type: Quickstart
  url: https://docs.sourcebot.dev/docs/deployment/deploy-sourcebot
- group: company
  title: ''
  type: Website
  url: https://www.sourcebot.dev
- group: company
  title: ''
  type: Blog
  url: https://www.sourcebot.dev/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.sourcebot.dev/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.sourcebot.dev
- group: operate
  title: ''
  type: Support
  url: https://github.com/sourcebot-dev/sourcebot/issues
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/sourcebot-dev
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.sourcebot.dev/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.sourcebot.dev/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.sourcebot.dev
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.sourcebot.dev/docs/upgrade/v4-to-v5-guide
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.sourcebot.dev/changelog
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/sourcebot-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/sourcebot-lifecycle.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/sourcebot-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: Packages
  url: packages/sourcebot-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/sourcebot-cli.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/sourcebot-sandbox.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/sourcebot-well-known.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/sourcebot-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/sourcebot-llms.txt
created: '2026-07-17'
description: Sourcebot is a self-hosted code understanding platform built by Taqla Inc. that helps developers and AI agents search, navigate, and understand large enterprise codebases. It indexes every repository across GitHub, GitLab, Bitbucket, Azure DevOps, Gerrit, and Gitea and runs entirely inside your own infrastructure, so source code never leaves your deployment. Alongside a fast regex- and symbol-aware code search UI with file explorer and git history/blame, Sourcebot ships "Ask Sourcebot" natural-language codebase Q&A and an agent code context layer (an MCP server) that gives coding agents like Cursor and Claude Code grounded context across every repo. Its public REST API exposes search, symbol navigation, repository listing, git history/blame/diff, and enterprise user/audit endpoints, secured with API keys (and EE OAuth for agent clients). Free self-hosted Basic tier, paid Pro tier for AI and enterprise security.
image: https://github.com/sourcebot-dev.png
layout: provider
mcp_servers:
- description: Sourcebot's "agent code context layer" — an MCP server that gives coding agents (Cursor, Claude Code, VS Code, and any MCP-compatible client) grounded search and navigation context across every repo i
  name: Sourcebot MCP Server
  slug: sourcebot-mcp-server
modified: '2026-07-21'
name: Sourcebot
nav: Providers
network: true
overview: 'Sourcebot publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Enterprise (EE) API, Git API, Repositories API, and 2 more. Tagged areas include Company, Code Search, Code Intelligence, Developer Tools, and Source Code.


  Sourcebot''s developer surface includes documentation, API reference, getting-started guide, quickstart, engineering blog, pricing, signup flow, and 22 more developer resources.'
random_paper: 16
score:
  band: developing
  composite: 48.5
  coverage:
    artifact_dirs: 21
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.6
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 4.5
    contract_quality: 53.5
    developer_ergonomics: 73.2
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 26.3
  previous_composite: 49.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: first-party
    skills: derived
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sourcebot/refs/heads/main/screenshots/sourcebot-2026-08-17T082010.png
security:
- kind: authentication
  name: Sourcebot Authentication
  slug: sourcebot-authentication
  summary_line: http/apiKey/oauth2 · 3 schemes
- kind: domain-security
  name: Sourcebot Domain Security
  slug: sourcebot-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: sourcebot
tags:
- Company
- Code Search
- Code Intelligence
- Developer Tools
- Source Code
- Git
- MCP
- AI Coding Agents
- Enterprise Search
- Self-Hosted
website: https://www.sourcebot.dev
---
