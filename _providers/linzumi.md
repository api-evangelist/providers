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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 27.0
  scored_at: '2026-08-11'
api_count: 1
apis:
- description: The private product API behind the Linzumi web workspace and the local Commander runner, served from serve.linzumi.com under a /api/v2 URI-versioned path. It is not a published developer API — there i
  name: Linzumi Runner API
  slug: runner-api
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://linzumi.com/
- group: start
  title: ''
  type: Login
  url: https://serve.linzumi.com/
- group: operate
  title: ''
  type: Support
  url: mailto:hello@linzumi.com
- group: other
  title: ''
  type: Download
  url: https://downloads.linzumi.com/macos-beta/linzumi_macos_latest.dmg
- group: other
  title: ''
  type: Profile
  url: https://www.ycombinator.com/companies/linzumi
- group: build
  title: ''
  type: Packages
  url: packages/linzumi-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/linzumi-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/linzumi-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/linzumi-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/linzumi-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/linzumi-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/linzumi-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/linzumi-changelog.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/linzumi-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/linzumi-llms.txt
created: '2026-07-17'
description: Linzumi is a Y Combinator (Spring 2026) company in San Francisco building a Slack-shaped team chat that runs a fleet of AI coding agents inside every channel. Engineering teams kick off work, watch agent activity in real time, review output, and ship code without leaving the thread. Unlike sandboxed cloud agent products, Linzumi runs agents on the developer's own machine through a local "Commander" runner installed from the @linzumi/cli npm package, so agents work against real environment variables, dotfiles, and branches inside explicitly trusted folders. The product adds a decision inbox that surfaces only the choices needing a human, continuously compiled team context, git safety snapshots taken before each agent turn, and a bundled local MCP server that lets coding agents read scoped Linzumi message, thread, and channel context. It supports OpenAI Codex today with Claude Code announced as coming soon. The service is in beta via a macOS desktop app and a web workspace; there
  is no public developer API program, documentation portal, or published OpenAPI at this time.
image: https://storage.googleapis.com/ployai/d195dfe3-6a0f-4051-8d67-1a4376685f60/user/3e1aeaf5-og-home-en.jpg
layout: provider
mcp_servers:
- description: ''
  name: linzumi-mcp.yml
  slug: linzumi-mcpyml
modified: '2026-07-19'
name: Linzumi
nav: Providers
network: true
overview: 'Linzumi publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Developer Tools, Coding Agents, and Team Chat.


  Linzumi''s developer surface includes support, CLI, authentication, changelog, and 11 more developer resources.'
random_paper: 80
score:
  band: emerging
  composite: 19.5
  delta: 0.0
  facets:
    commercial_clarity: 13.2
    contract_quality: 0.0
    developer_ergonomics: 30.4
    discoverability: 87.0
    governance: 0.0
    operational_transparency: 15.8
  previous_composite: 19.5
  provenance:
    mcp: first-party
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/linzumi/refs/heads/main/screenshots/linzumi-2026-07-25T225305.png
security:
- kind: authentication
  name: Linzumi Authentication
  slug: linzumi-authentication
  summary_line: oauth2-device-code/oauth2-authorization-code · 3 schemes
- kind: domain-security
  name: Linzumi Domain Security
  slug: linzumi-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: linzumi
tags:
- Company
- Artificial Intelligence
- Developer Tools
- Coding Agents
- Team Chat
- Collaboration
- MCP
- Command Line Interface
- Y Combinator
website: https://linzumi.com/
---
